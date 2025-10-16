# Peer review - Round 1

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.39188.035](https://doi.org/10.7554/eLife.39188.035)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Integrated systems analysis reveals conserved gene networks underlying response to spinal cord injury" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Ole Kiehn as the Reviewing Editor and Patricia Wittkopp as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Tune Pers (Reviewer #1); Andrea Tedeschi (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The study by Squair et al. use an integrative approach to identify a set of genes predictive for spinal cord injury (SCI) severity and functional recovery. They use a combination of systematic literature reviews and WGCNA on public gene databases to develop a gene set enrichment analysis and consensus SCI network conserved in many species. They then perform functional enrichment analyses using cell-based ontologies and protein network analyses to validate the selected gene sets. They identify a microglia/vascular cell network ('M3') and an innate immune response microglia network ('M7') correlated with injury severity and functional recovery, respectively. Some of the most connected genes in the M3 gene was also found to be downregulated in a dataset where neurotrophin-3 (NT3)-coupled chitosan biomaterial was grafted into a gap of completely transected rat thoracic spinal cord. The systems approach applied to spinal cord injury is novel and the pipeline is well presented and spans over a large number of relevant experimental and computational techniques, which complement each other very well. The work is important and will most probably have an impact in SCI.

Essential revisions:

The reviewers were generally very supportive of the work as presented but had a number of comments and specific request for improving the work and its impact.

A) Additional analysis:

1) The literature curated genes share more protein-protein interactions (PPI). However, biases in the PPI database towards small-scale studies could confound the analysis. The authors should redo their analysis based on PPI data restricted to interactions from large-scale screens only (e.g. from the InWeb or, if possible, HINT database). The same bias may exist for the validation analysis focusing on the size of the largest connected component and the DIAMOnD analysis.

2) The authors should attempt to provide additional cell type specificity to the modules including M3 and M7 by using single cell RNA sequencing data from the spinal cord the following studies: a) www.biorxiv.org/content/early/2018/04/06/294918, b) Neuronal atlas of the dorsal horn defines its architecture and links sensory input to transcriptional cell types. Nature Neuroscience 2018; c) Massively Parallel Single Nucleus Transcriptional Profiling Defines Spinal Cord Neurons and Their Activity during Behavior, Cell 2018.

B) Request for deposit of material:

The authors should put together a Github repository with all of the code used to perform the extensive analyses represented here. Given that the large majority of the work product here is in silico analysis of existing public resources, it seems only right for the authors to give back to the community so that each figure can be re-constructed from source code they make publicly-available. This is critical for reproducibility.

C) Comments that may be addressed in the text:

1) In genetics, less than 4% of the results from small-scale approaches (candidate gene analyses) have not been robustly replicated (Hirschhorn, Genetics in Medicine 2002). The authors should comment on: What are the potential reasons that a literature-seed gene approach seems to work well for SCI? What were the characters of the literature small-scale study approaches and experimental techniques that yielded the most predictive genes for the M3 and M7 networks – any clear trends? Finally, were the M3 and M7 networks the top results in the RNA sequencing experiment, or were there WGCNA networks (or differentially expressed genes) stronger correlated with injury severity and functional recovery than the M3 and M7 networks, which would suggest additional relevant SCI pathways currently less well captured in literature?

2) The literature curated genes coalesce on common biological functions that depends on them being accurately annotated. Could the author comment if there is bias towards literature genes even if genes have to be annotated to at least three Gene Ontology terms?

3) The authors should mention that the assumption underlying their work is that gene expression data in control individuals is indicative of processes dysregulated in SCI. Even so this assumption seems to hold true in their case it remains to be shown whether it holds true in general.

4) As most inflammatory mediators are expressed at low levels in the uninjured spinal cord, and the subsequent increase in expression is a response to injury, they are likely to correlate with SCI severity. It may therefore be suspected to find a M3 module enriched for markers of microglia positively that correlate positively with injury severity. The authors could have consider to expand the significance of their work by including additional analysis from another publicly available dataset where a different strategy was shown to promote functional recovery after SCI. In absence of this analysis the authors should discuss the general predictivity of their analysis with respect to the different modules.
