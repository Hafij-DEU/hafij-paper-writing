# Voice profile — Md. Hafijur Rahman

Derived from three published co-authored papers:

1. Sharif MA, Khan AM, … Rahman MH, et al. *Phyllanthus emblica* (Amla) methanolic extract regulates multiple checkpoints in 15-lipoxygenase mediated inflammopathies: computational simulation and in vitro evidence. **Saudi Pharm J** 2023. doi:10.1016/j.jsps.2023.06.014 (PMC10415228)
2. Khan AM, Sharif MA, … Rahman MH, et al. In vitro and in silico investigation of garlic's (*Allium sativum*) bioactivity against 15-lipoxygenase mediated inflammopathies. **J Herbmed Pharmacol** 2023;12(2):283–298. doi:10.34172/jhp.2023.31
3. Dey D, Paul PK, Al Azad S, Al Mazid MF, Khan AM, Sharif MA, Rahman MH. Molecular optimization, docking, and dynamic simulation profiling of selective aromatic phytochemical ligands in blocking the SARS-CoV-2 S protein attachment to ACE2 receptor. **J Adv Vet Anim Res** 2021. doi:10.5455/javar.2021.h481 (PMC8043340)

Group: Biotechnology and Genetic Engineering Discipline, Khulna University (Bangladesh). Rahman's role: computational section (docking, ADMET, MD).

## Measured style numbers

| Metric | Amla (SPJ) | Garlic (JHP) | ACE2 (JAVAR) | Target for new drafts |
|---|---|---|---|---|
| Mean sentence length (words) | ~30* | 27.0 | 30.8 | 22–26 |
| Sentences > 35 words | 29%* | 17% | 27% | < 12% |
| Sentences with passive verb | 54% | 54% | 44% | ~40–50% (Methods may be higher) |
| Sentences with we/our | 5% | 0% | 6% | 5–15% (Intro aim, Discussion) |
| Hedge words per 1k words | 8.1 | 6.3 | 2.8 | 8–12 |
| Booster words per 1k words | 8.5 | 8.4 | 3.5 | ≤ 5 |

*Amla value inflated by flattened table text.

Reading: the voice is long, passive, descriptive and leans on boosters (significant, substantial, potent). Keep the structure and vocabulary. Make sentences shorter. Use fewer boosters. Hedge in silico claims more (see `benchmark-conventions.md`).

## Signature structure (keep this)

**Title.** Pattern: `<Plant (common name)> <solvent> extract <verb: regulates / investigation of …> <target>-mediated inflammopathies: <computational simulation and in vitro evidence>`. Coined term "inflammopathies". Two-part titles with a colon.

**Abstract.** Structured (Objectives/Introduction · Methods · Results · Conclusion) or a single paragraph. Results carry every IC50/EC50 with the standard in parentheses, e.g. "IC50 of X µg/mL (IC50 of Y µg/mL for standard quercetin)". Last sentences name the in silico lead and the simulation length ("stable throughout the 100 ns simulation").

**Introduction funnel (4 moves).**
1. Mechanism chain: ROS → oxidative stress → LOX-mediated lipid peroxidation (arachidonic/linoleic acid → HPETE → HETEs, eoxins, leukotrienes) → pro-inflammatory cytokines → endothelial damage → tissue factor → serine-protease coagulation cascade.
2. Remedy: exogenous antioxidants; plant-derived extracts in ethnomedicine "with only a few adverse effects and toxicity".
3. The plant: common names in parentheses, traditional culinary or medicinal use, long list of reported pharmacological activities, then a list of reported phytochemicals (named compounds).
4. Gap → hypothesis → aims: "several studies focused on COX-2 … but there is a lack of organized study that focuses on 15-LOX"; "We hypothesize that …"; "this study aims to evaluate … We also aim to validate … by in silico docking … further assessed for stability by MD simulation."

**Methods order.** Plant collection (market, city, exact date, voucher accession and herbarium) → extract preparation (drying, grinding, solvent ratio, temperature, duration, rotary evaporation, % yield) → blood collection and ethics (number of donors, consent, ethical code KUAEC-2017/08/14) → antioxidant assays (DPPH, reducing power) → phytochemical content (TPC as GAE, TFC as QE, TTC) → anti-inflammatory (HRBC membrane stabilization / hypotonicity hemolysis, soybean 15-LOX inhibition by Wangensteen's method) → anticoagulant (serine protease/trypsin–casein, prothrombin time) → statistics → in silico (library from MS-reported literature compounds → SwissADME/pkCSM ADMET → PDB retrieval or HHpred homology model + PROCHECK Ramachandran → UCSF Chimera preparation → PyRx 0.8/AutoDock Vina docking → LigPlot+ 2D interactions → Desmond 100 ns MD: RMSD, RMSF, Rg, P-L contacts, SID). Every assay gets its own subheading and a numbered % inhibition equation.

**Results sentence template (assay).**
> "<Activity> increased in a concentration-dependent manner (Figure 1A). At the highest concentration (400 µg/mL), the extract showed X% <activity>, compared to standard <drug> (Y%). The extract showed significant (P < 0.001) <activity> with an IC50 of A ± SD µg/mL, whereas <standard> had an IC50 of B ± SD µg/mL (Figure 1B)."

**Results sentence template (MD metric).** Open each MD subsection with one definitional sentence plus the accepted range and its citation. Then report the range per ligand with the plot colour. Close with a stability interpretation.
> "RMSD measures the average deviation of the complex from a reference frame over time; a variation of 1–3 Å between frames is considered acceptable (Ref). Ligands A, B and C complexed with 15-LOX2 showed RMSD between 1.1 and 3.0 Å (Figure 10a), whereas D fluctuated up to 3.5 Å (mean 1.97 Å)."

**Docking/interaction reporting.** Name residues with distances in parentheses: `ARG407 (3.02 Å)`, list hydrophobic residues, give H-bond counts compared with the control (ibuprofen, PubChem CID 3672). Docked ligands are compared against the natural substrates (arachidonic and linoleic acid) as a benchmark.

**Discussion moves.**
1. Restart from the pathophysiology. NSAIDs and synthetic antioxidants have side effects, so plant bioactives are a safer alternative.
2. Justify the solvent and assay choice (e.g. methanol extracts polar phenolics; RBCs have no nucleus, so they are a clean membrane model; soybean 15-LOX resembles the mammalian enzyme).
3. Go assay by assay. Compare with previous studies ("supporting previous studies that …", "consistent with …").
4. Give the mechanism through polyphenols: proton donation, metal chelation, radical neutralisation.
5. Restate statistics and the correlation, then interpret them.
6. In silico synthesis: all hits bind more strongly than the substrates. Then MD stability, then the lead compound: "on the basis of docking and MD, X was identified as the lead compound to block 15-LOX1". Finish with in vivo literature that supports the lead.

**Conclusion.** 2–4 sentences. Restate the activities. Say the results support the traditional use. Name next steps: isolation and MS identification of the compounds, then in vitro or in vivo trials.

**Back matter.** Author contributions (CRediT-like sentences), funding (KURC grant numbers), ethics statement, conflict of interest, acknowledgments.

## Lexicon (keep, but vary)

Verbs: exhibited, demonstrated, showed, possessed, manifested, revealed, displayed, substantiated, was observed, was found, was determined.
Comparators: compared to, whereas, in comparison to, with respect to, respectively, on the other hand, similarly.
Sequencers (Methods): following that, afterward, then, subsequently.
Domain terms: inflammopathies, P-L complex, phytochemical ligands, lead compound, pharmacophore, drug-likeness, concentration-dependent manner, prototype mimicking mammalian lipoxygenase, ethnotherapeutic.

Use sparingly (overused): "substantial", "potent", "significant" (use only when a statistical test was done), "validate" (in silico cannot validate in vitro data; use "support" or "corroborate"), "on the other hand" (use only for a real contrast), "and so on" / "etc." in lists.

## Recurring errors seen in the published versions (do NOT repeat)

- Wrong units: AutoDock Vina/PyRx scores are **kcal/mol**, not KJ/mol.
- Missing µ: "50–400 g/mL", "975 mL" written where µg/mL or µL was meant. Write µg/mL consistently, never "µgmL-1" in one paper and "µg/ml" in another.
- Typos that reached print: "essay" (assay), "violate" (violet), "noble" (novel), "trail" (trial), "poroteins", "linolic" (linoleic), "Ros" (ROS), "Principle component" (principal).
- Same species name spelled three ways (emblica/embelica/embilica). Italicise binomials. Write the genus in full at first use, abbreviated afterwards.
- "PTT" was used for prothrombin time. PTT means partial thromboplastin time. Prothrombin time is **PT**.
- Figure numbering out of order (Fig. 6 cited for two different figures). Panels cited as Fig. 11-b, Fig. 11(a) and Figure 10a in the same paper.
- Standard named inconsistently: aspirin in Methods, quercetin in Results for the same assay.
- Claims inflated beyond evidence: "clearly showed", "validated the anti-inflammatory potential in humans" (docking only), "only way of investigating biomolecular interactions".
- 1.1 ns MD presented as conclusive stability. Use ≥ 100 ns, ideally in triplicate.
- No limitations paragraph in any of the three papers.
