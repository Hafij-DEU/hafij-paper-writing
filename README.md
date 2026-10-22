# hafij-paper-writing

A Claude Code skill for drafting and revising research papers in the published writing style of Md. Hafijur Rahman. The topics it covers are plant-extract bioactivity, 15-lipoxygenase and anti-inflammatory work, antioxidant and anticoagulant assays, ADMET, molecular docking and molecular dynamics. On top of that style it applies the conventions of well-cited, high-impact journals.

## What it does

- Writes each section (Introduction, Methods, Results, Discussion, Abstract, Title, Conclusion, cover letter, reviewer response) using the author's section structure and vocabulary.
- Adds rigor taken from high-impact papers: a specific gap statement, calibrated in silico claims, inline limitations, statistics and reproducibility detail.
- Avoids errors that reached print in earlier papers (e.g. KJ/mol vs kcal/mol, PTT vs PT, missing µ).
- Runs a humanness check on every drafted section and revises it until it matches the author's own writing pattern.

## Install

```bash
git clone https://github.com/Hafij-DEU/hafij-paper-writing ~/.claude/skills/hafij-paper-writing
```

Claude Code picks the skill up automatically. Ask for it by name, e.g. "Use the hafij-paper-writing skill to draft an Introduction".

## Humanness checker

```bash
python3 -I scripts/humanness_check.py draft.txt
```

It reports sentence-length rhythm, vocabulary diversity, LLM-typical words, stock transitions and em dashes, and gives a 0–100 score. Reference medians: pre-LLM high-impact papers 96, the author's published papers 91, 2024–25 high-impact biology papers 81. The target is 90 or above. This is a style heuristic, not an AI detector.

## Files

| Path | Purpose |
|---|---|
| `SKILL.md` | Workflow, voice rules, humanization rules, self-check |
| `references/voice-profile.md` | Author's measured style, section moves, lexicon, recurring errors |
| `references/benchmark-conventions.md` | Conventions from high-impact LOX, docking and MD papers |
| `references/section-templates.md` | Section skeletons, cover letter, reviewer response |
| `references/humanness-test.md` | Calibration data and test results |
| `scripts/humanness_check.py` | Humanness scorer |

## Source papers

1. Sharif MA, Khan AM, … Rahman MH, et al. *Saudi Pharm J* 2023. doi:10.1016/j.jsps.2023.06.014
2. Khan AM, Sharif MA, … Rahman MH, et al. *J Herbmed Pharmacol* 2023;12(2):283–298. doi:10.34172/jhp.2023.31
3. Dey D, Paul PK, … Rahman MH. *J Adv Vet Anim Res* 2021. doi:10.5455/javar.2021.h481

The reference files hold style patterns and short phrases only. Do not paste text from source papers into new manuscripts.
