# Peer review - Round 1

Editors:
- Ivan Topisirovic, McGill University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.107121.3.sa0](https://doi.org/10.7554/eLife.107121.3.sa0)

In this valuable study, Taber et al. used a battery of biophysical and structural approaches to characterize the impact of erythrocytosis-related mutations in prolyl hydroxylase domain protein 2 (PHD2). The authors show that PHD2 mutant proteins are destabilized, thus supporting the tenet that dysregulation of PHD2/hypoxia induced factor (HIF) axis underpins erythrocytosis, while providing solid evidence that N-terminal ODD prolyl hydroxylation of HIF is indispensable for these phenotypes. These findings were found to be of interest for researchers focusing on oxygen sensing in homeostasis and pathological states.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.107121.3.sa1](https://doi.org/10.7554/eLife.107121.3.sa1)

Summary:

Taber et al report the biochemical characterization of 7 mutations in PHD2 that induce erythrocytosis. Their goal is to provide a mechanism for how these mutations cause the disease. PHD2 hydroxylates HIF1a in the presence of oxygen at two distinct proline residues (P564 and P402) in the "oxygen degradation domain" (ODD). This leads to the ubiquitylation of HIF1a by the VHL E3 ligase and its subsequent degradation. Multiple mutations have been reported in the EGLN1 gene (coding for PHD2), which are associated with pseudohypoxic diseases that include erythrocytosis. Furthermore, 3 mutations in PHD2 also cause pheochromocytoma and paraganglioma (PPGL), a neuroendocrine tumour. These mutations likely cause elevated levels of HIF1a, but their mechanisms are unclear. Here, the authors analyze mutations from 152 case reports and map them on the crystal structure. They then focus on 7 mutations, which they clone in a plasmid and transfect into PHD2-KO to monitor HIF1a transcriptional activity via a luciferase assay. All mutants show impaired activation. Some mutants also impaired stability in pulse chase turnover assays (except A228S, P317R, and F366L). In vitro purified PHD2 mutants display a minor loss in thermal stability and some propensity to aggregate. Using MST technology, they show that P317R is strongly impaired in binding to HIF1a and HIF2a, whereas other mutants are only slightly affected. Using NMR, they show that the PHD2 P317R mutation greatly reduces hydroxylation of P402 (HIF1a NODD), as well as P562 (HIF1a CODD), but to a lesser extent. Finally, BLI shows that the P317R mutation reduces affinity for CODD by 3-fold, but not NODD.

Strengths:

(1) Simple, easy-to-follow manuscript. Generally well-written.

(2) Disease-relevant mutations are studied in PHD2 that provide insights into its mechanism of action.

(3) Good, well-researched background section.

Weaknesses:

(1) Poor use of existing structural data on the complexes of PHD2 with HIF1a peptides and various metals and substrates. A quick survey of the impact of these mutations (as well as analysis by Chowdhury et al, 2016) on the structure and interactions between PHD2 peptides of HIF1a shows that the P317R mutation interferes with peptide binding. By contrast, F366L will affect the hydrophobic core, and A228S is on the surface, and it's not obvious how it would interfere with the stability of the protein.

(2) To determine aggregation and monodispersity of the PHD2 mutants using size-exclusion chromatography (SEC), equal quantities of the protein must be loaded on the column. This is not what was done. As an aside, the colors used for the SEC are very similar and nearly indistinguishable.

(3) The interpretation of some mutants remains incomplete. For A228S, what is the explanation for its reduced activity? It is not substantially less stable than WT and does not seem to affect peptide hydroxylation.

(4) The interpretation of the NMR prolyl hydroxylation is tainted by the high concentrations used here. First of all, there is a likely a typo in the method section; the final concentration of ODD is likely 0.18 mM, and not 0.18 uM (PNAS paper by the same group in 2024 reports using a final concentration of 230 uM). Here, I will assume the concentration is 180 uM. Flashman et al (JBC 2008) showed that the affinity of the NODD site (P402; around 10 uM) for PHD2 is 10-fold weaker than CODD (P564, around 1 uM). This likely explains the much faster kinetics of hydroxylation towards the latter. Now, using the MST data, let's say the P317R mutation reduces the affinity by 40-fold; the affinity becomes 400 uM for NODD (above the protein concentration) and 40 uM for CODD (below the protein concentration). Thus, CODD would still be hydroxylated by the P317R mutant, but not NODD.

(5) The discrepancy between the MST and BLI results does not make sense, especially regarding the P317R mutant. Based on the crystal structures of PHD2 in complex with the ODD peptides, the P317R mutation should have a major impact on the affinity, which is what is reported by MST. This suggests that the MST is more likely to be valid than BLI, and the latter is subject to some kind of artefact. Furthermore, the BLI results are inconsistent with previous results showing that PHD2 has a 10-fold lower affinity for NODD compared to CODD.

(6) Overall, the study provides some insights into mutants inducing erythrocytosis, but the impact is limited. Most insights are provided on the P317R mutant, but this mutant had already been characterized by Chowdhury et al (2016). Some mutants affect the stability of the protein in cells, but then no mechanism is provided for A228S or F366L, which have stabilities similar to WT, yet have impaired HIF1a activation.

Comments on revision:

While the authors have addressed my concerns regarding the SEC experiments and the structural interpretation of most mutants, I remain unconvinced by their interpretation of the P317R mutant and affinity measurements. The BLI and MST data remain inconsistent for P317R binding to CODD, and the authors' response is essentially that the fluorescent labeling of P317R (but not other mutants) uniquely interferes with binding to the NODD/CODD peptides, which does not make a lot of sense. The fluorescent labeling target lysine residues; while there are lysine in PHD2 in proximity to the peptide binding site, labeling these sites would affect binding to all mutants, not only P317R (which does not introduce any new labeling site). Furthermore, the authors did not really address the discrepancy with the observations by Flashman et al (2008) that NODD binds more weakly than CODD, which is inconsistent with their BLI results. Another point that makes me doubt the validity of the BLI results is the poor fit of the sensorgrams and the slow dissociation kinetics, which is inconsistent with the relatively low affinity in the 2-6 uM range.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.107121.3.sa2](https://doi.org/10.7554/eLife.107121.3.sa2)

Summary:

Mutations in the prolyl hydroxylase, PHD2, cause erythrocytosis and, in some cases, can result in tumorigenesis. Taber and colleagues test the structural and functional consequences of seven patient-derived missense mutations in PHD2 using cell-based reporter and stability assays, and multiple biophysical assays, and find that most mutations are destabilizing. Interestingly, they discover a PHD2 mutant that can hydroxylate the C-terminal ODD, but not the N-terminal ODD, which suggests the importance of N-terminal ODD for biology. A major strength of the manuscript is the multidisciplinary approach used by the authors to characterize the functional and structural consequences of the mutations. However, the manuscript had several major weaknesses, such as an incomplete description of how the NMR was performed, a justification for using neighboring residues as a surrogate for looking at prolyl hydroxylation directly, or a reference to the clinical case studies describing the phenotypes of patient mutations. Additionally, the experimental descriptions for several experiments are missing descriptions of controls or validation, which limits their strength in supporting the claims of the authors.

Strengths:

(1) This manuscript is well-written and clear.

(2) The authors use multiple assays to look at the effects of several disease-associated mutations, which support the claims.

(3) The identification of P317R as a mutant that loses activity specifically against NODD, which could be a useful tool for further studies in cells.

Weaknesses:

Major:

(1) The source data for the patient mutations (Figure 1) in PHD2 is not referenced, and it's not clear where this data came from or if it's publicly available. There is no section describing this in the methods.

(2) The NMR hydroxylation assay.

A. The description of these experiments is really confusing. The authors have published a recent paper describing a method using 13C-NMR to directly detect proly-hydroxylation over time, and they refer to this manuscript multiple times as the method used for the studies under review. However, it appears the current study is using 15N-HSQC-based experiments to track the CSP of neighboring residues to the target prolines, so not the target prolines themselves. The authors should make this clear in the text, especially on page 9, 5th line, where they describe proline cross-peaks and refer to the 15N-HSQC data in Figure 5B.

B. The authors are using neighboring residues as reporters for proline hydroxylation, without validating this approach. How well do CSPs of A403 and I566 track with proline hydroxylation? Have the authors confirmed this using their 13C-NMR data or mass spec?

C. Peak intensities. In some cases, the peak intensities of the end point residue look weaker than the peak intensities of the starting residue (5B, PHD2 WT I566, 6 ct lines vs. 4 ct lines). Is this because of sample dilution (i.e., should happen globally)? Can the authors comment on this?

(3) Data validating the CRISPR KO HEK293A cells is missing.

(4) The interpretation of the SEC data for the PHD2 mutants is a little problematic. Subtle alterations in the elution profiles may hint at different hydrodynamic radii, but as the samples were not loaded at equal concentrations or volumes, these data seem more anecdotal, rather than definitive. Repeating this multiple times, using matched samples, followed by comparison with standards loaded under identical buffer conditions, would significantly strengthen the conclusions one could make from the data.

Minor:

(1) Justification for picking the seven residues is not clearly articulated. The authors say they picked 7 mutants with "distinct residue changes", but no further rationale is provided.

(2) A major finding of the paper is that a disease-associated mutation, P317R, can differentially affect HIF1 prolyhydroxylation, however, additional follow-up studies have not been performed to test this in cells or to validate the mutant in another method. Is it the position of the proline within the catalytic core, or the identity of the mutation that accounts for the selectivity?

Comments on revision:

The revised manuscript addresses most of my concerns, i.e performing SEC experiments under matched sample concentrations, and incorporating additional data to justify the use of surrogate residues to monitor proline hydroxylation. I appreciate the improvements in the text to clarify the NMR experiments, but I still find their description confusing. Although the authors are using neighboring residues to monitor proline hydroxylation (which they justify convincingly using supplementary data), the language in the text suggests they are (and can?) monitor them directly (i.e. referring to proline cross-peaks in an 15N-HSQC spectrum). The axis labels in Figure 5B also seem to have become mislabeled in this revised version.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.107121.3.sa3](https://doi.org/10.7554/eLife.107121.3.sa3)

Summary:

This is an interesting and clinically relevant in vitro study by Taber et al., exploring how mutations in PHD2 contribute to erythrocytosis and/or neuroendocrine tumors. PHD2 regulates HIFα degradation through prolyl-hydroxylation, a key step in the cellular oxygen-sensing pathway.

Using a time-resolved NMR-based assay, the authors systematically analyze seven patient-derived PHD2 mutants and demonstrate that all exhibit structural and/or catalytic defects. Strikingly, the P317R variant retains normal activity toward the C-terminal proline but fails to hydroxylate the N-terminal site. This provides the first direct evidence that N-terminal prolyl-hydroxylation is not dispensable, as previously thought.

The findings offer valuable mechanistic insight into PHD2-driven effects and refine our understanding of HIF regulation in hypoxia-related diseases.

Strengths:

The manuscript has several notable strengths. By applying a novel time-resolved NMR approach, the authors directly assess hydroxylation at both HIF1α ODD sites, offering a clear functional readout. This method allows them to identify the P317R variant as uniquely defective in NODD hydroxylation, despite retaining normal activity toward CODD, thereby challenging the long-held view that the N-terminal proline is biologically dispensable. The work significantly advances our understanding of PHD2 function and its role in oxygen sensing, and might help in the future interpretation and clinical management of associated erythrocytosis.

Weaknesses:

There is a lack of in vivo/ex vivo validation. This is actually required to confirm whether the observed defects in hydroxylation-especially the selective NODD impairment in P317R-are sufficient to drive disease phenotypes such as erythrocytosis.

The reliance on HRE-luciferase reporter assays may not reliably reflect the PHD2 function and highlights a limitation in the assessment of downstream hypoxic signaling.

The study clearly documents the selective defect of the P317R mutant, but the structural basis for this selectivity is not addressed through high-resolution structural analysis (e.g., cryo-EM).

Given the proposed central role of HIF2α in erythrocytosis, direct assessment of HIF2α hydroxylation by the mutants would have strengthened the conclusions.

Comments on revision:

The revised manuscript by Taber et al. addresses the key points raised during the review process in a comprehensive and appropriate manner. While some limitations remain, such as the lack of in vivo validation or direct HIF2α assessment, I agree with the authors that these are beyond the scope of the current in vitro-focused study. The authors' primary goal was to define the structural and functional defects caused by disease-associated PHD2 mutations. In this respect, the evidence they present is largely convincing and methodologically appropriate. Additional clarifications and an expanded discussion of the luciferase assay's limitations and the P317R structural context strengthen the manuscript further.
