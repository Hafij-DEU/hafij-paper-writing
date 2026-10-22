# High-impact benchmark conventions

Derived from five open-access PMC papers, analysed 2026-10-22. Patterns only; do not copy wording.

| # | Paper | Journal, year | PMCID | DOI |
|---|---|---|---|---|
| A | Endogenous vitamin E metabolites limit inflammation by targeting 5-lipoxygenase | Nat Commun 2018 | PMC6148290 | 10.1038/s41467-018-06158-5 |
| B | Novel 15-LOX-1 inhibitor protects macrophages from LPS-induced cytotoxicity | J Med Chem 2019 | PMC6511944 | 10.1021/acs.jmedchem.9b00212 |
| C | Ensemble-based virtual screening (MD relaxed complex) for avian influenza neuraminidase | J Med Chem 2008 | PMC2652358 | 10.1021/jm8001197 |
| D | Docking + MD of plasmodial cysteine proteases with a natural compound and analogues | Sci Rep 2016 | PMC4814779 | 10.1038/srep23690 |
| E | Phytochemical docking on the SARS-CoV-2 spike–ACE2 complex | Sci Rep 2020 | PMC7573581 | 10.1038/s41598-020-74715-4 |

**E is a counter-example.** It is highly cited but overclaims: activity "proved" in silico, QSAR "experimentally validated". It never uses "we" and hedges little. Avoid its style.

## Voice statistics (body text)

- Methods are 70–86% passive. Results and Discussion are only 33–40% passive.
- "We" is 6–10% overall, 20–70% in the Discussion and Conclusion, and about 0% in Methods.
- Hedges cluster in the Discussion: 1.5–4.6 per 1k words overall.
- Mean sentence length is 22–27 words. Pre-LLM papers show 0–1.1 LLM-tell words per 1k (see `humanness-test.md`).

## By section

**Abstract (150–250 words).** Context (1–2 sentences) → specific gap → "Here we show/report…" with the method in the same sentence → 2–3 key numbers → one hedged significance sentence ("our data suggest…").

**Introduction.**
- Funnel: burden → target biology → **known inhibitors with their IC50 values** (to position the new agent) → a precise mechanistic gap → aim.
- State the gap as a specific unknown ("the mechanism remained unclear because…"). Never write "few studies exist".
- The aim paragraph starts "Here, we…" or "In this study, we…". It previews what the reader gains.

**Methods.**
- Every assay names its readout (e.g. 15-LOX: 13-HpODE formation at 234 nm), its reference inhibitor (NDGA, PD-146176, zileuton, quercetin) and n independent experiments with mean ± SD/SEM.
- **Validate docking before using it**: redock the co-crystal ligand and report the pose RMSD (< 2 Å).
- MD: force field, water model, ions, ensemble, temperature, length, replicates, and the averaging window.

**Results.**
- Subheadings state findings ("Garlic extract inhibits 15-LOX in a concentration-dependent manner"), not topics.
- Paragraph pattern: purpose clause ("To determine whether…") → what was done → numbers with SD and units → figure reference → one interpretive sentence.
- Controls are reported explicitly (vehicle, reference inhibitor, aggregation or reversibility checks where relevant).
- **Docking is never a standalone result.** It explains the experimental data (SAR, potency ranking) or is tested experimentally (mutagenesis, enzyme kinetics).
- MD reporting:
  - State the convergence time first ("RMSD plateaued after 5 ns").
  - Report mean ± SD over the equilibrated window.
  - Compare apo and holo states.
  - Interpret RMSF by structural region (loops, active-site helix).
  - Treat Rg as compactness.
  - Add MM-PBSA/GBSA with per-residue decomposition.
  - Explain ligand RMSD by chemistry (rotatable bonds).

**Discussion.**
- Open with a one-sentence restatement of the main claim ("Here, we report…").
- Build the argument as an evidence list, numbered (i)–(n) if needed. Interpret the results; do not re-describe them.
- Label speculation ("we speculate", "it is tempting to propose", "we hypothesise").
- Compare with named prior studies and say plainly where they disagree.
- **Inline limitations** next to the claim they limit:
  - docking scoring error is about 2 kcal/mol
  - docking separates binders from non-binders but ranks them poorly
  - limited MD sampling
  - soybean vs human enzyme
  - other lipid-peroxidation pathways
  - in vitro to in vivo gap
- End with translational implications.

**Conclusion (5–10 sentences).** Active, first person. Recap each line of evidence. Make a calibrated significance statement. Name a concrete next step.

## Main differences from mid-tier writing (apply these)

1. Validate docking (redocking, reference ligand, SAR, mutagenesis); never treat binding energy as proof.
2. State the gap as a specific mechanism, not "limited reports on plant X".
3. Keep "demonstrate/show" for experimental data. In silico results "predict" or "suggest". Never write "proved in silico".
4. Every number has units, ± SD/SEM, n, a positive control and the statistical test. MD values come with the convergence window.
5. Use "we" in the aims, Discussion and Conclusion. Keep Methods passive.
6. Results follow purpose → finding → interpretation, under finding-type subheadings.
7. The Discussion argues and reconciles the literature; it does not re-list residues.
8. Place limitations inline and specifically, plus a short limitations paragraph if the journal expects one.
