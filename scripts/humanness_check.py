#!/usr/bin/env python3
"""Score how "human" a manuscript draft reads, against the author's own baseline.

Usage: python3 -I humanness_check.py draft.txt [more.txt ...]
       python3 -I humanness_check.py --json draft.txt

Metrics are heuristics, not an AI detector. They flag the patterns that make
LLM prose read machine-made: uniform sentence length, stock vocabulary,
formulaic transitions, repeated sentence openers and over-tidy lists.
"""
import json
import re
import statistics
import sys

# Calibrated on the author's published Intro + Discussion prose
# (Amla SPJ 2023 / garlic JHP 2023 / ACE2 JAVAR 2021 measured:
#  mean 23.1/25.6/25.2 words, CV 0.36/0.32/0.42, short 9/1/6 %, MATTR .73/.75/.73,
#  LLM tells 0.8/1.1/1.0, stock transitions 1.5/2.8/0, triplets 6.9/5.1/4.9 per 1k).
# Ranges are widened slightly toward higher burstiness, which reviewers read as natural.
BASELINE = {
    "sent_len_mean": (19, 27),
    "sent_len_cv": (0.32, 0.90),      # burstiness: SD / mean of sentence length
    "short_sent_pct": (3, 25),        # sentences <= 12 words
    "mattr": (0.68, 0.80),            # moving-average type-token ratio, window 100
    "llm_tells_per_1k": (0, 1.2),
    "stock_transitions_per_1k": (0, 3.0),
    "opener_repeat_pct": (0, 15),     # most common 2-word sentence opener share
    "em_dash_per_1k": (0, 0.5),       # author never uses em dashes
    "triplet_lists_per_1k": (0, 8),
}

# Words the author already uses natively; fine in moderation
STOCK_TRANSITIONS = [r"furthermore", r"moreover", r"additionally", r"in conclusion", r"overall,"]

# Vocabulary and phrasing typical of LLM output, rare in the author's papers
LLM_TELLS = [
    r"delv\w*", r"intricat\w*", r"pivotal", r"underscor\w*", r"tapestry", r"realm",
    r"landscape", r"multifaceted", r"nuanc\w*", r"meticulous\w*", r"paramount",
    r"plays? a (crucial|pivotal|vital|key) role", r"it is (worth|important to) not(e|ing)",
    r"shed(s|ding)? light", r"pav(e|es|ing) the way", r"a testament to", r"harness\w*",
    r"in the realm of", r"navigat\w* the", r"holistic", r"seamless\w*", r"leverag\w*",
    r"notabl[ey]", r"comprehensive\w*",
    r"robust\w*", r"crucial\w*", r"showcas\w*", r"unveil\w*", r"elucidat\w*", r"foster\w*",
    r"bolster\w*", r"garner\w*", r"underpin\w*",
    r"not only\b.*\bbut also", r"serves? as a", r"a (wide|broad|diverse) (range|array|spectrum) of",
]

def sentences(text):
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\b(et al|e\.g|i\.e|Fig|vs|approx|ca|no|Eq|Ref)\.", lambda m: m.group(0)[:-1] + "§", text)
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9(\[])", text)
    return [p.replace("§", ".") for p in parts if len(p.split()) >= 3]

def mattr(words, w=100):
    if len(words) < w:
        return len(set(words)) / max(len(words), 1)
    return statistics.mean(len(set(words[i:i + w])) / w for i in range(0, len(words) - w + 1, 10))

def score(text):
    text = re.sub(r"\[\d[\d,\s\-–]*\]|\([A-Z][^()]*\d{4}[a-z]?\)", "", text)  # drop citations
    s = sentences(text)
    lens = [len(x.split()) for x in s]
    words = re.findall(r"[a-z]+(?:-[a-z]+)*", text.lower())
    k = max(len(words), 1) / 1000
    def count(pats):
        found = {}
        for pat in pats:
            n = len(re.findall(r"\b" + pat, text, re.I))
            if n:
                found[pat] = n
        return found
    tells = count(LLM_TELLS)
    stock = count(STOCK_TRANSITIONS)
    openers = [" ".join(x.split()[:2]).lower() for x in s]
    top_open = max((openers.count(o) for o in set(openers)), default=0)
    m = {
        "words": len(words),
        "sentences": len(s),
        "sent_len_mean": round(statistics.mean(lens), 1) if lens else 0,
        "sent_len_cv": round(statistics.pstdev(lens) / statistics.mean(lens), 2) if len(lens) > 1 else 0,
        "short_sent_pct": round(100 * sum(l <= 12 for l in lens) / max(len(lens), 1)),
        "mattr": round(mattr(words), 3),
        "llm_tells_per_1k": round(sum(tells.values()) / k, 2),
        "stock_transitions_per_1k": round(sum(stock.values()) / k, 2),
        "opener_repeat_pct": round(100 * top_open / max(len(s), 1)),
        "em_dash_per_1k": round(text.count("—") / k, 2),
        "triplet_lists_per_1k": round(len(re.findall(r"\b\w+, \w+,? and \w+\b", text)) / k, 2),
    }
    flags = [f"{key}={m[key]} outside {lo}-{hi}" for key, (lo, hi) in BASELINE.items() if not lo <= m[key] <= hi]
    m["tells_found"] = {**tells, **stock}
    m["flags"] = flags
    m["human_score"] = human_score(m)
    ok = m["human_score"] >= 90 and len(flags) <= 1 and not any(f.startswith("llm_tells") for f in flags)
    m["verdict"] = "reads human (matches author baseline)" if ok else "revise: " + ("; ".join(flags) or "score < 90")
    return m

def human_score(m):
    """0-100. Reference medians (2026-10-22): pre-LLM high-impact papers 96,
    author's papers 91, 2024-25 high-impact biology papers 81, default LLM prose 0."""
    penalty = (6 * m["llm_tells_per_1k"]
               + 4 * max(0, m["stock_transitions_per_1k"] - 3)
               + 40 * max(0, 0.32 - m["sent_len_cv"])
               + 3 * m["em_dash_per_1k"]
               + 0.5 * max(0, m["short_sent_pct"] - 25))
    return max(0, round(100 - penalty))

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--json"]
    if not args:
        sys.exit(__doc__)
    for path in args:
        res = score(open(path, encoding="utf-8", errors="ignore").read())
        if "--json" in sys.argv:
            print(json.dumps({path: res}, indent=1))
            continue
        print(f"== {path}")
        for key, val in res.items():
            if key not in ("tells_found", "flags", "verdict", "human_score"):
                rng = BASELINE.get(key)
                print(f"  {key:22} {val}" + (f"   (baseline {rng[0]}-{rng[1]})" if rng else ""))
        print("  tells:", res["tells_found"] or "none")
        print(f"  HUMAN SCORE: {res['human_score']}/100  (pre-LLM papers ~96, author ~91, 2024-25 papers ~81; target >= 90)")
        print("  VERDICT:", res["verdict"])
