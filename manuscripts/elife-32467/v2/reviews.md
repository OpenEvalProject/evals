# Peer review - Round 1

Editors:
- Dominique Soldati-Favre, University of Geneva Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.32467.034](https://doi.org/10.7554/eLife.32467.034)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for sending your article entitled "Codon choice dictates constitutive mRNA levels in trypanosomes" for peer review at eLife. Your article is being evaluated by three peer reviewers, one of whom is a member of our Board of Reviewing Editors and the evaluation is being overseen by a Reviewing Editor and Wendy Garrett as the Senior Editor.

Given the list of essential revisions, including new experiments, the editors and reviewers invite you to respond within the next two weeks with an action plan and timetable for the completion of the additional work. We plan to share your responses with the reviewers and then issue a binding recommendation.

Summary:

This paper shows that in trypanosomes, as in yeast and metazoa, codon usage affects mRNA stability. The authors do this by measuring the abundance and stabilities of variously-coded GFP mRNAs in procyclic trypanosomes. They then use the information, combined with an RNASeq dataset, to calculate optimised scores for the effects of different codons. Importantly, the authors show that translation is required for the codon effects, however they do not demonstrate that the hairpins are really working to block translation as anticipated.

Essential revisions:

1) The authors need to improve the clarity of the paper in every section. Concepts need explaining, and the figures need much more detail in their accompanying legends to be comprehensible.

2) In regard to Figure 1 and Figure 7 as well as the others, the authors must Strengthen/weaken the significance of their analysis by showing that their index works on different RNAseq datasets:

The authors have optimized their CAI for one dataset (developmentally un-regulated genes and tested for mRNA from PF cells). The authors state that their dataset differs from all the others and therefore comparisons are meaningless.

However, the reviewers disagree. If their CAI only works with their own dataset then it is the CAI that is problematic. Also, although they claim that the CAI reflects mRNA half-life, the authors ignore the published transcriptome-wide half-life measurements.

Please show the following scatter plots (essential):a) CAI vs other procyclic form RNASeq datasets. (In addition to the datasets mentioned, there are also some procyclic ones in 10.1093/nar/gkv731, and the original Siegel et al. set.)

b) CAI vs a few bloodstream form datasets (excluding developmentally regulated mRNAs, of course)

c) CAI versus mRNA half-life (Fadda et al., 2014).

The results might be less compelling than those obtained using the dataset with which the CAI was trained, but probably not completely random. Nevertheless, the authors can then discuss the strengths and limitations of their CAI in a balanced way- and also, of course, the limitations of some of the datasets (e.g. use or not of poly(A)) selection, effects of Actinomycin D). The mRNAs showing clear discrepancies across all datasets could also be interesting, suggesting other types of regulation.

3) The authors must relate their results to the two other ribosome profiling datasets, which are more robust because they have more replicates: Jensen et al. 2014 and Antwi et al.

4) Overall the generation of the data and figures need to be more comprehensively described. (see comment 1).

Figure 1C: How does the new geCAI compare to the CAI or tAI? The authors should provide p-values of mRNA levels vs CAI and tAI score.

Figure 2: "The values for GFPs were adjusted to allow for an effectively 8-fold lower copy number that the endogenous genes." It is not clear to me what this statement means.

Figure 2—figure supplement 2: This figure does not contain sufficient information. E.g. it is not clear what was measured, how often, what cell lines etc. All raw measurements should be listed, otherwise it is impossible to understand what the authors show in panel B (I assume the left panel is A and the right panel B).

Subsection “Gene expression codon adaptation index, geCAI, a codon usage statistic to predictmRNA levels” and Materials and methods section: It is not clear if the RNAseq data was generated as part of the study or previously, as part of the study by Kelly et al., 2017, as that study contains a link to the same dataset.

If the RNA-seq data was generated as part of this study, more details on library preparation should be included, even if it was carried out by BGI. Also, it should be stated how many reads where obtained from the different replicates, what percentage could be mapped, and which genome was used for the alignment, 927 or 427.

[Editors' note: the authors’ plan for revisions was approved and the authors made a formal revised submission. Further revisions were then requested prior to acceptance, as described below.]

Thank you for submitting your article "Codon choice directs constitutive mRNA levels in trypanosomes" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Wendy Garrett as the Senior Editor. The following individual involved in review of your submission has agreed to reveal her identity: Christine Clayton (Reviewer #1).

The reviewers acknowledge the work and analyses done to improve clarity and thinking processes. They have discussed the reviews with one another and identified the points that still deserve the authors' attention. the Reviewing Editor has drafted this decision to help you prepare a revised submission. We hope you will be able to submit the revised version shortly.

Summary:

This paper shows that in trypanosomes, as in yeast and metazoa, codon usage affects mRNA stability. The authors used mRNA expression levels calculated from one RNAseq dataset to determine geCAI values for each codon and then tested the ability of these geCAI values to determine the protein and mRNA abundance of GFP transgenes with different codon usage. The protein and mRNA expression levels of these GFP transgenes were consistent with the predictions using geCAI.

Essential revisions:

1) In regard to the 8-fold lower copy of different GFP verses endogenous genes. The response by the authors does not make sense - there should be 4 copies of GFP compared to 8 copies of all single copy diploid genes, especially if there is contamination of one emission spectra with the others.

2) Materials and methods section: In the rebuttal letter, the authors go through great length outlining how differences among RNA-seq datasets may be due to technical reasons. Yet they do not provide much detail on how the RNA-seq libraries were generated for this study.

The first step to making RNA-seq datasets more comparable would be a very detailed description of how the libraries were generated. The authors should provide information on the variables they themselves list:

- The amount of time taken to wash the cells between culture flask and cell lysis; a 1, 5 or 10 minute centrifugation will have a differential effect on mRNA abundance of different genes depending on the half-life of that mRNA.

- The composition and temperature of any wash solution.

- The method used to prepare mRNA.

- The method used for library construction and RNAseq.

- The analysis of the RNAseq data to quantify mRNA expression levels.

In addition, information should be added on the polyA-enrichment step: e.g. what poly-dT beads were used? Magnetic or cellulose? From what manufacturer?
