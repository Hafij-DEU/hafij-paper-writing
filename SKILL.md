---
name: hafij-paper-writing
description: Write or revise research papers in Md. Hafijur Rahman's own published style (plant extract bioactivity, 15-lipoxygenase/anti-inflammatory, antioxidant and anticoagulant assays, ADMET, molecular docking, molecular dynamics, in silico drug design), raised to high-impact journal standards. Use when the user asks to write, draft, outline, expand, rewrite, polish or review a manuscript, abstract, introduction, methods, results, discussion, conclusion, title, cover letter or reviewer response "in my style", or for phytochemical/in vitro/in silico papers.
---

# Hafij paper-writing skill

Draft and revise manuscripts so they sound like the user's published papers. Then apply the conventions of older, high-impact journals in the same field, and avoid the errors that reached print before.

Two reference layers. Read both before writing any section:

- `references/voice-profile.md`: the user's own voice. It has the measured stats, section moves, sentence templates, lexicon and the recurring errors to avoid. **This decides how the text sounds.**
- `references/benchmark-conventions.md`: conventions taken from well-cited, high-impact PubMed Central papers on LOX inhibitors, natural-product pharmacology, docking and MD. **This decides how rigorous the text is.**
- `references/section-templates.md`: fill-in skeletons for each section, with both layers merged.
- `references/humanness-test.md`: a worked example of a default AI draft vs a skill draft, with checker scores.
- `scripts/humanness_check.py`: measures rhythm, vocabulary and LLM tells against the author's baseline.

When the two layers conflict, keep the user's structure and vocabulary. Take the benchmark's rigor: hedging, statistics, limitations and reproducibility detail.

## Workflow

1. **Collect the inputs.** Ask only for what is missing: plant or compound, solvent, the assays done, the raw numbers (IC50/EC50 ± SD, n, p-values), the targets and PDB IDs, the docking software, MD length and engine, the control drug, the target journal and its word limit. Never invent data, numbers, PDB IDs, PubChem CIDs, ethics codes, grant numbers or citations. Leave `[[TODO: …]]` placeholders instead.
2. **Pick the format.** Use the target journal's style for abstract structure, heading names (e.g. "Materials and Methods"), citation style (Vancouver numbers or author–year) and figure labels ("Figure 1A" or "Fig. 1(a)"). Default: structured abstract, Vancouver numbers, "Figure 1A".
3. **Outline first.** Show a bullet outline of each section's moves (from `section-templates.md`). Wait for the user's OK, unless they asked for a full draft straight away.
4. **Draft one section at a time**, in this order: Methods → Results → Discussion → Introduction → Abstract → Title → Conclusion. Abstract and title come last, so they match the final numbers.
5. **Humanness check.** Save each drafted section to a temp file and run:
   `python3 -I ~/.claude/skills/hafij-paper-writing/scripts/humanness_check.py <file>`
   Revise until the verdict reads "reads human (matches author baseline)" and HUMAN SCORE ≥ 90. Then show the user the score. For reference: pre-LLM high-impact papers have a median of 96, the author's papers 91, and 2024–25 high-impact biology papers 81 (`references/humanness-test.md`).
6. **Self-check** each section against the checklist below. Then report what is still `[[TODO]]`.

## Humanization rules (calibrated on the author's prose)

These are measured on the author's Intro and Discussion prose and on pre-LLM high-impact papers (2008–2019). The checker script enforces them.

- **Rhythm.** Mean sentence length 19–27 words, coefficient of variation (CV) of 0.32 or more, and 3–25% short sentences (12 words or fewer). Do **not** write clipped, punchy prose; it is not the author's voice. Join related clauses the way the author does: "…, whereas <standard> had…", "…, compared to…", "…, which…", "…, respectively". Mix in one short sentence after a dense one.
- **Zero LLM vocabulary.** Never use: delve, intricate, pivotal, underscore, tapestry, realm, landscape, multifaceted, nuanced, meticulous, paramount, "plays a crucial/pivotal role", "it is worth noting", "shed light", "pave the way", "a testament to", harness, holistic, seamless, leverage, notably, comprehensive, robust, crucial, showcase, unveil, elucidate, foster, bolster, garner, underpin, "not only … but also", "serves as a", "a wide range/array/spectrum of".
- **Stock transitions** (Furthermore, Moreover, Additionally, In conclusion, Overall) are the author's own habit, but use them no more than 3 times per 1,000 words. Prefer the author's comparative connectors (whereas, on the other hand, similarly, compared to) and content-bearing openers ("Because erythrocytes lack nuclei, …").
- **No em dashes** (the author never uses them). Use commas, parentheses or a new sentence.
- **No ornamental triplets.** Do not use three-adjective or three-noun lists for rhythm; list items only when the data has that many.
- **Specific over generic.** Every sentence carries a number, a named compound, a residue, a citation or a mechanism. Delete sentences that only frame or praise ("These findings are significant for the field").
- **Commit, then qualify once.** State the claim plainly, then give the reason or caveat in the same or the next sentence. Do not stack hedges ("may potentially suggest").
- **Vary sentence openers.** No 2-word opener should start more than 15% of sentences. Avoid starting runs of sentences with "The extract…".
- **Disclosure.** Many journals require a statement on AI-assisted writing. Remind the user to add one if their target journal asks for it.

## Voice rules (from the user's papers)

- Open the Introduction with the mechanism chain: ROS → oxidative stress → LOX lipid peroxidation → inflammatory mediators (and → coagulation when relevant). Then plants as safer ethnomedicine. Then the specific plant (common names, traditional use, reported activities, reported phytochemicals). Then gap → hypothesis → aims.
- Give each assay and each in silico step its own subheading. Cite the method source ("according to Wangensteen's method with minor modifications [n]"). Number every equation.
- Every Results value is paired with its standard: "IC50 of A ± SD µg/mL, whereas quercetin had an IC50 of B ± SD µg/mL (Figure 2D)."
- Start each MD metric subsection (RMSD, RMSF, Rg, SASA, H-bonds, contacts) with one definitional sentence and the accepted range with its citation. Then give the values per complex. Then interpret.
- Report docking residues as `ARG407 (3.02 Å)`. Compare against the control drug and the natural substrates.
- The Discussion goes assay by assay with prior-literature comparison. Then the polyphenol mechanism (proton donation, chelation, radical neutralisation). Then the in silico synthesis, ending with the named lead compound and in vivo literature that supports it.
- Keep the user's vocabulary: exhibited, demonstrated, possessed, manifested, concentration-dependent manner, P-L complex, lead compound, inflammopathies, compared to / whereas / respectively.
- Passive voice in Methods. Use "we" for the aims, the hypothesis and key interpretive claims.

## Upgrades over the published versions (always apply)

- Sentences average 19–27 words. Split any sentence over 40 words, but do not over-split (see Humanization rules).
- Use "significant" only where a statistical test supports it. Cap boosters (substantial, potent, strong, remarkable) at about one per paragraph.
- Calibrate in silico claims: docking and MD **predict**, **suggest** or **support**. They never **validate** or **confirm** in vitro or human activity.
- Name a specific, citable gap. Avoid vague wording such as "there is a lack of organized study"; say what has and has not been measured, in which system.
- Add a **Limitations** paragraph before the Conclusion: crude extract vs isolated compound; soybean vs human 15-LOX; literature-derived compound library (no LC-MS of this extract); docking scoring limits; single MD replicate; no in vivo or cell work.
- Statistics: report n, mean ± SD, the test and the post hoc test. Prefer one-way ANOVA with Dunnett's test vs control over many one-tailed t-tests. Fit IC50 by nonlinear regression and give 95% CI if available. State the software version.
- Reproducibility for in silico work: PDB ID and resolution, protonation, grid box centre and size, exhaustiveness, force field, water model, ions, ensemble (NPT), temperature, pressure, simulation length, number of replicates. Add MM-GBSA/PBSA free energy if it was run.
- Units: docking scores in **kcal/mol**. Concentrations as µg/mL (consistent). Prothrombin time is **PT**, not PTT. Italicise binomials and spell them the same way every time.
- Consistent figure and table numbering, cited in order. One panel style throughout.
- Conclusion: claims proportional to the evidence, plus a concrete next step (LC-MS/MS profiling, isolation, cell-based or in vivo assay).

## Self-check before returning text

- [ ] Every number traces to user data or carries `[[TODO]]`. No fabricated citations.
- [ ] Each IC50/EC50 has ± SD, units and the comparison standard.
- [ ] Hedges match the evidence type (in vitro vs in silico vs literature).
- [ ] Limitations paragraph is present (full manuscript).
- [ ] No banned errors from the list in `voice-profile.md` (KJ/mol, missing µ, PTT, essay/violate/noble, inconsistent binomial spelling).
- [ ] Abstract numbers match the Results exactly.
- [ ] Sentences over 40 words split. Boosters trimmed.
- [ ] `humanness_check.py` verdict: reads human. No LLM-tell words. No em dashes.

## Copyright note

The reference files hold patterns and short phrases only. Never paste long verbatim passages from the user's published papers or the benchmark papers into a new manuscript; that would be self-plagiarism or plagiarism. Reuse the structure and write fresh wording each time.
