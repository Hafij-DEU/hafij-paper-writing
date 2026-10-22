# Section templates (user voice + high-impact rigor)

`<…>` = fill in from the user's data. `[[TODO]]` = data not supplied. Write fresh wording each time; these are skeletons, not text to paste.

## Title

- `<Plant> (<common name>) <solvent> extract <attenuates/inhibits/modulates> 15-lipoxygenase-mediated inflammopathies: in vitro and in silico evidence`
- `<Compound class> from <plant> as <target> inhibitors: integrated enzyme assays, molecular docking and molecular dynamics`

Keep it to 25 words or fewer. Name the plant, the target and the evidence types. Avoid "novel" and "first".

## Abstract (structured, 200–250 words)

- **Background/Objectives**: 1–2 sentences. Disease mechanism → plant → gap. Then "This study aimed to …".
- **Methods**: extract type; assays grouped by activity (antioxidant: …; anti-inflammatory: …; anticoagulant: …); in silico pipeline (library of N literature-reported compounds, ADMET, docking against <targets, PDB IDs>, <length> ns MD).
- **Results**: TPC/TFC. Then each IC50/EC50 ± SD with the standard in parentheses. Then the top docking score (kcal/mol) vs control. Then the MD stability statement with the lead compound.
- **Conclusion**: 1–2 sentences. Hedge proportionally ("These findings suggest …; isolation and in vivo testing are needed").

## Introduction (4–5 paragraphs, ~600–800 words)

1. **Mechanism.** ROS origin and roles → excess ROS → oxidative stress → LOX catalysis of PUFA (arachidonic/linoleic acid) → HPETE → HETEs, lipoxins, eoxins, leukotrienes → cytokines and disease list. Optional: oxidative endothelial damage → tissue factor → extrinsic coagulation (FVIIa–TF → Xa → thrombin).
2. **Therapeutic problem.** Current drugs (NSAIDs, synthetic antioxidants, anticoagulants) and their adverse effects. Then plant secondary metabolites as alternatives, with specific examples of LOX inhibitors from plants and their potency.
3. **The plant.** Botanical name (italic) and common names; traditional use; reported pharmacology with citations; LC-MS/GC-MS-reported constituents.
4. **Specific gap.** What has been tested (e.g. COX-2, carrageenan oedema) and what has not (15-LOX inhibition, human 15-LOX1/2 structural interaction, coagulation link). Cite the closest prior work.
5. **Aim and approach.** "Here, we hypothesised that … To test this, we (i) …, (ii) …, and (iii) …" End with one sentence on the contribution. Do not restate the results.

## Materials and Methods

Order: Chemicals and reagents (supplier, catalogue no., purity) → Plant material (source, date, GPS or market, taxonomic identification by <person>, voucher no., herbarium) → Extraction (mass, solvent, ratio, temperature, time, filtration, evaporation conditions, % yield, storage) → Ethics and blood collection (n donors, inclusion criteria, consent, approval code) → Phytochemical content (TPC/TFC/TTC: reagent, wavelength, calibration range, units) → Antioxidant assays → Anti-inflammatory assays → Anticoagulant assays → In silico (below) → Statistics.

Each assay paragraph: principle (1 sentence) → reference and modifications → concentrations tested (range, number of points) → volumes, buffer, pH, incubation time and temperature → readout wavelength → equation (numbered) → standard drug.

**In silico subsections**
- *Ligand library*: N compounds, source (LC-MS literature, databases), selection criteria, PubChem CIDs in a supplementary table, 3D preparation (energy minimisation, force field, charges).
- *Target preparation*: PDB ID, resolution, chain; removal of water and heteroatoms; protonation state at pH 7.4; missing residues. For homology models: template, identity %, tool, validation (Ramachandran favoured %, ERRAT/ProSA z-score).
- *Docking*: software and version, grid centre (x, y, z) and size (Å), exhaustiveness, how the binding site was defined (co-crystal ligand or literature residues), **re-docking validation of the native ligand (RMSD < 2 Å)**, control drug and natural substrates.
- *ADMET*: tools (SwissADME, pkCSM, ProTox), rules applied (Lipinski, Veber), the filters used to shortlist.
- *MD simulation*: engine and version, force field, water model, box, ions or salt concentration, minimisation, NVT/NPT equilibration, temperature and pressure, production length, time step, replicates; analyses (RMSD, RMSF, Rg, SASA, H-bonds, contacts, MM-GBSA/PBSA).
- *Statistics*: n (biological or technical replicates), mean ± SD, test (one-way ANOVA + Dunnett vs control; or t-test justified), IC50 by nonlinear regression (log[inhibitor] vs response), significance threshold, software and version.

## Results

Order follows Methods. One subsection per assay family. Each paragraph:
1. Trend: "<Activity> increased in a concentration-dependent manner (Figure 1A)."
2. Max effect: "At 400 µg/mL, the extract showed X% <activity>, compared with Y% for <standard>."
3. Potency: "IC50 = A ± SD µg/mL (95% CI) vs B ± SD µg/mL for <standard> (Figure 1B; P < 0.001 vs control)."
4. No interpretation beyond one clause; save the rest for the Discussion.

In silico Results:
- Structure validation (Ramachandran %).
- ADMET table summary: how many pass Lipinski; toxicity flags.
- Docking: score range; top hits vs control vs substrates (kcal/mol); key residues with distances; shared residues with the co-crystal ligand.
- MD: each metric starts with a definition and accepted range [ref], then values per complex (mean ± SD over the last X ns), then a one-line stability verdict. Report both protein Cα and ligand RMSD. Report MM-GBSA ΔG if run.
- Correlation analysis between assays (Pearson r or R², P).

## Discussion (5–7 paragraphs)

1. **Main finding first.** One paragraph: what was shown and what it means, hedged to the evidence.
2. **Antioxidant and phenolic content** vs prior reports on the same plant and solvent. Mechanism: H-atom or electron donation, metal chelation.
3. **Anti-inflammatory**: membrane stabilisation logic (RBC as a lysosomal membrane model); 15-LOX inhibition vs published IC50s of known inhibitors (NDGA, quercetin, baicalein); soybean vs human enzyme caveat.
4. **Anticoagulant**: serine protease and PT findings; plausible constituents.
5. **In silico synthesis**: the lead binds more strongly than the substrates and control; residues overlap with the catalytic site (iron-coordinating His residues, the U-shaped substrate channel); MD stability. Literature supporting the lead's anti-inflammatory activity in cells or animals.
6. **Correlation and integration**: assays correlate, consistent with polyphenols as shared contributors (hedged).
7. **Limitations** (mandatory) and future work.

Each comparative sentence: "<Our value> was <higher/lower/comparable> to <prior value> reported for <system> [ref], which may reflect <solvent, cultivar, assay difference>."

## Conclusion (80–150 words)

Restate the findings with numbers only if the journal allows. Say what they support (traditional use, a candidate lead). Give a concrete next step (LC-MS/MS profiling of the extract, isolation of <lead>, enzyme kinetics with human recombinant 15-LOX1/2, cell or in vivo inflammation models). No new claims.

## Back matter

Author contributions (CRediT terms), Funding (agency, grant no.), Ethics statement (committee, code), Data availability (docking poses, MD trajectories, raw assay data), Conflict of interest, Acknowledgments.

## Cover letter (≤ 1 page)

Editor greeting → title and article type → 2–3 sentences on the gap and main finding → why it fits the journal's scope → declarations (originality, no simultaneous submission, all authors approved, conflicts) → 3–5 suggested reviewers if requested.

## Reviewer response

For each comment: the reviewer's text quoted in italics → "Response:" with thanks, the action taken and the location (page/line) → the changed text quoted. Polite and specific, with no argument without evidence.
