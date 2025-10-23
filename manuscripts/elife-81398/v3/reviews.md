# Peer review - Round 1

Editors:
- Andrew C Kruse, Harvard Medical School United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81398.sa0](https://doi.org/10.7554/eLife.81398.sa0)

This paper reports the development and application of a proteo-genomic screening platform to identify protein-protein interactions between secreted proteins and their cell surface receptors. The authors use a CRISPRa-based approach to overexpress membrane proteins in cells and then use magnetic cell sorting to identify receptors that bind candidate ligands. This approach led to the identification of several novel interaction pairs that were then validated biochemically, including receptor tyrosine phosphatase ligands and other interactions with implications for immune system function. The work is likely to be relevant to a wide variety of fields including biochemistry and signal transduction research.


---

# Peer review - Round 1

Editors:
- Andrew C Kruse, Harvard Medical School United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81398.sa1](https://doi.org/10.7554/eLife.81398.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Identification of orphan ligand-receptor relationships using a cell-based CRISPRa enrichment screening platform" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jonathan Cooper as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers were uniformly enthusiastic about the work but raised a variety of small points for clarification which should be addressed in a revised manuscript. Some additional experiments were suggested (see reviewer 3 point 10) but reviewers agreed that this new data is not strictly essential, although it could strengthen the manuscript if it were to be added. We leave this latter decision to the authors' discretion.

Reviewer #1 (Recommendations for the authors):

This manuscript is well-written and made the workflow for a complex screen easy to follow for non-specialists. The data is rigorous and includes all appropriate controls. I have only a few comments/critiques:

1) It was surprising that CD36 was identified as a receptor for 4 out of 20 ligands tested on the screen. Can the authors comment on the potential of scavenger receptors or other promiscuous binders to outcompete other top hits? Did CD36 score highly for the other 16 ligands screened?

2) The authors should speculate on why TAFA-2 would selectively bind to D0-containing KIRs. Are KIR subtypes expressed on certain subsets of tissues or cells such that this makes biological sense?

3) The identification of PTPRU as the bona fide receptor for OSTN was notable in that it was not the top hit and required trajectory analysis of the three rounds of selection. On a high-throughput basis, deep sequencing of this many samples could become quite costly. The authors should comment on whether they recommend trajectory analysis as a routine operation in hit identification, or whether it could it be possible to circumvent this by performing additional rounds of selection.

Reviewer #3 (Recommendations for the authors):

1) The authors should more clearly state their use of the Chong et al., 2018 method paper as the starting point for this work. That paper describes a CRISPR activation screen that included sgRNAs targeting the whole human secretome in HEK 293 cells, which is then used to query soluble biotinylated GPCRs to identify novel interactions. The current authors should elaborate on the similarities and any specific differences between their approach and the Chong paper. The current treatment appears to give the Chong paper short shrift and reduces the purported novelty of the work.

2) The authors could go into more detail regarding their selection of the 80 soluble targets for expression. Contrary to statements made, many of the targets are directly related to one another (Ex: 8/80 are angiopoietin-related proteins). Also, over half of the targets screened are primarily found in the brain, so the tissue distribution doesn't seem that broad either. The text mentions that disease associations were taken into account; however, there are no data supporting this claim.

3) Have any of the 60 query proteins that failed to express been successfully expressed using other recombinant protein systems? Did the authors consider any rescue strategies for improving recombinant expression success rates?

4) Why were K562 cells chosen for this study as opposed to using HEK 293 cells that were used in other published CRISPRa screens? Are there observed differences in the CRISPR activation efficiency between these cell lines? HEK 293 cells are well established as a model system for high protein expression, especially for secreted and membrane proteins, suggesting it might be a better choice. Were other candidate cell lines tested?

5) What fraction of the library genes are upregulated to significant levels? In the assessment of the small TM1 screen, it is claimed that all 10 of the genes showed elevated cell surface expression. However, looking at the FACS plots in Figure S1 (B), this does not seem to be accurate. CD5 and IL6ST showed no change and others exhibited very modest increases in expression. Is this level of expression sufficient to identify known ligands of these proteins (e.g., weak binders)? This information would help to assess the robustness of this approach and how consistently it identifies targets with a range of different expression levels and different binding affinities.

6) The IL-2/CD25 test demonstrates that the TM1 screen can efficiently identify a high affinity (Kd ~10-8) interaction with high confidence. However, several of the interactions identified have affinities in the range of 10-6 or lower. The authors should consider running control screens against the full TM1 and TM2 libraries using soluble queries (CD80, CD200, etc.) that bind known receptors with μM affinities. These controls would help evaluate how well this approach identifies established, biologically relevant, low-affinity interactions.

7) In some of the screens (e.g., OMG, GAS1) other genes also show high ESP scores. Were any of the second or third highest scoring "hits" characterized further for potential enrichment in subsequent rounds of screening? The scale of the ESP plots also changes significantly depending on the screen. In the original Chong et al., paper, only one round of enrichment was used and all of the ERA plots are set to the same scale. They used a larger library and clearly demonstrated to ability to identify known weak interactions. Do multiple rounds of enrichment increase the potential for amplifying screening artifacts/nonspecific/nonrelevant interactions? The scoring scheme is also slightly different from Chong et al., making it difficult to directly compare the two studies.

8) In the OSTN screen no enrichment of PTPRU was observed until 3 rounds of selection, even though the measured affinity is higher than that determined for the OMG/PTPRU interaction. Is there an explanation as to why that was the case? The overall level of enrichment also seems lower. There is also a target gene (red dot) in Figure 3G between PTPRJ and PTPRU. Is there a strong correlation between rounds of enrichment and Kd? What is the identity of that target and what was its trajectory during the 3 rounds of enrichment?

9) For the SPR experiments, many of the runs required high analyte protein concentrations (80uM for TAFA2, 60uM for OMG). Are the authors confident that the proteins used for SPR were not forming soluble aggregates at the highest analyte concentrations used for binding? Soluble aggregates notoriously bind nonspecifically and can mimic low-affinity interactions.

10) For the cell binding experiments, negative control tetramer titrations should also be performed using a tetramerized protein not expected to bind. Also, the cell binding titrations do not saturate and the binding only appears statistically significant from controls at the highest concentrations used. Do the reciprocal cell experiments also show binding? These data would benefit from the inclusion of representative FACS plots and a description of the gating strategy used.

11) There are target genes (red dots) with relatively high ERA scores in the TM2+ screens that are not CD36 (For example in the NRN1L, TICN1, SCRG1, and MK screens). What are these targets and was binding further characterized for any of them? As CD36 seems to act as a scavenger receptor, are there sequence similarities or other shared characteristics between the receptors CD36 interacts with?
