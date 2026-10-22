# Humanness test (run 2026-10-22)

Checker: `scripts/humanness_check.py`. Data: published garlic paper (J Herbmed Pharmacol 2023). Same facts, three Discussion drafts.

## Baselines (human-written)

| Source | Mean len | CV | Short % | MATTR | LLM tells/1k | Stock trans./1k |
|---|---|---|---|---|---|---|
| Author: Amla SPJ 2023 | 23.1 | 0.36 | 9 | 0.73 | 0.8 | 1.5 |
| Author: garlic JHP 2023 | 25.6 | 0.32 | 1 | 0.75 | 2.3* | 2.9 |
| Author: ACE2 JAVAR 2021 | 25.2 | 0.42 | 6 | 0.73 | 1.5* | 0.0 |
| Nat Commun 2018 (5-LO, vitamin E) | 35.7† | 0.42 | 0 | 0.75 | 0.0 | 3.3 |
| J Med Chem 2019 (15-LOX-1 inhibitor) | 34.2† | 0.78 | 10 | 0.67 | 0.0 | 1.2 |
| J Med Chem 2008 (relaxed-complex VS) | 43.2† | 0.87 | 2 | 0.71 | 1.1 | 1.1 |
| Sci Rep 2016 (docking + MD) | 29.9† | 1.66† | 9 | 0.62 | 1.0 | 0.8 |

*Author values before the tells list was refined: "a wide spectrum of", "plays a vital role", "pave the way" and "robust" occur naturally, about 1–2 per paper. Treat ≤ 1.2/1k as the target.
†Inflated by sentences the regex could not split (Greek letters, inline tables).

## Drafts

| Draft | Mean len | CV | Short % | LLM tells/1k | Stock/1k | Verdict |
|---|---|---|---|---|---|---|
| A. Default LLM prose (no skill) | 20.7 | 0.27 | 0 | **113** | **21** | fail: uniform rhythm, saturated with tells |
| B. Skill draft, first pass | 15.5 | 0.49 | **38** | 0 | 0 | fail: too clipped, not the author's voice |
| B2. Skill draft, clauses merged with whereas/compared to/which | 21.6 | 0.37 | 11 | 0 | 0 | **pass** |

Lessons:
1. The main risk is the vocabulary (delve, pivotal, underscore, showcase…) and uniform sentence length. Both are easy to detect and easy to remove.
2. Over-correcting into short sentences is a second failure mode. The author writes medium-long sentences joined by comparative connectors.
3. Non-native academic English naturally has low burstiness (CV 0.32–0.42). AI detectors are known to false-flag such writing, so detector scores are not proof either way. Match the author's own fingerprint instead.

## Example of passing prose (B2, first paragraph)

> Here, we report that an aqueous garlic extract inhibited soybean 15-LOX and protected human erythrocytes from hypotonic lysis, and that rhamnetin is a candidate inhibitor of both human 15-LOX isoforms. The extract inhibited 15-LOX with an IC50 of 250.05 ± 8.48 µg/mL, roughly 13-fold weaker than quercetin (19.62 ± 6.52 µg/mL), which is expected for a crude extract in which the active constituents are diluted. Membrane stabilization was comparatively stronger, as the extract exhibited an IC50 of 147.59 ± 2.98 µg/mL in the hemolysis assay, whereas aspirin had an IC50 of 59.08 ± 3.02 µg/mL.

## Ranking against recent high-impact biology (2024–25), run 2026-10-22

Corpus:
- 17 of the most-cited 2024–25 open-access research papers from Nat Commun, PNAS, eLife, PLoS Biol, NAR, Cell Rep, Sci Adv, EMBO J, Nature and STTT (Europe PMC, Intro + Discussion prose).
- The 5 pre-LLM benchmark papers.
- The author's 3 papers.
- The 2 test drafts.

The human score (0–100) is computed by `humanness_check.py`.

| Group | Median human score | Median LLM-tell words / 1k | Range of tells / 1k |
|---|---|---|---|
| Pre-LLM high-impact (2008–2020) | **96** | 0.0 | 0–1.1 |
| Author's papers (2021–2023) | **91** | 1.5 | 0.8–2.3 |
| 2024–25 high-impact biology | **81** | 3.2 | 0–18.9 |
| Skill draft B2 | **100** | 0.0 | — |
| Default LLM draft | **0** | 113 | — |

Most frequent tells in the 2024–25 papers: comprehensive, notably, "not only … but also", "a wide range/array of", crucial, furthermore, moreover, elucidate, pivotal, "plays a crucial role", intricate. 6 of the 17 papers score below 75. Prestige does not protect against this vocabulary drift.

The score is a style heuristic. It is not an AI detector and not evidence that any paper used AI; words like "comprehensive" and "crucial" also appear in pre-LLM writing. The aim is narrower: drafts produced with this skill should score ≥ 90, at or above the author's own published baseline.
