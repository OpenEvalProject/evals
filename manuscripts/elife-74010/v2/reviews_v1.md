# Peer review - Round 1

Editors:
- C Daniela Robles-Espinoza, International Laboratory for Human Genome Research Mexico

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74010.sa0](https://doi.org/10.7554/eLife.74010.sa0)

In this work, Petrov and Alexeyenko present a novel network-based method to infer cancer driver genes that is not based on frequency of mutations, NEAdriver, and evaluate its performance across a large dataset. This manuscript addresses a topic of high interest in the cancer genomics community and is a welcome addition to the literature.


---

# Peer review - Round 1

Editors:
- C Daniela Robles-Espinoza, International Laboratory for Human Genome Research Mexico

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74010.sa1](https://doi.org/10.7554/eLife.74010.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Individualized discovery of rare cancer drivers in global network context" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Aleksandra Walczak as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Abel Gonzalez-Perez (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. The three reviewers agreed that the authors should provide a reasonable calculation of the rate of false positives that their method produces, as at the moment is hard to evaluate what this number may be. The authors do not seem to correct for the background mutation rate of genes in the calculation of MutSet. This may result in identifying false positive driver genes with abnormally high number of mutations across cohorts due to known covariates of the mutation rate, such as the replication time or the level of transcription. Correctly estimating the background mutation rate of genes across tumors is a key tenet of methods that search for signals of positive selection in genes. For further explanation on this subject see PMID 23770567 and PMID 29056346. This may explain why known highly mutated non driver genes like TTN, RYR1 and others appear as significant recurrently across different cohorts. This issue is key for any method that uses mutation data to identify driver genes and must be addressed by the authors. A reviewer also adds adds that one way to calculate the rate of false positives would be to compile a list of known artifactual genes identified by methods aiming at detecting signals of positive selection in their mutational pattern across tumors. Computing the overlap of the output of their method with this list across cohorts could provide such estimate. An example of such a list is also provided in the supplementary material of this paper: PMID 32778778.

2. Reviewers also noted that the paper would benefit from a clearer presentation of the algorithm. Specifically:

a) Have the authors performed any technical filtering of the mutations? If not, how can they ensure that their results are not affected by potential sequencing artifacts or germline contamination?

b) The authors state that "The procedure evaluated likelihood of each genomic alteration (either PM or CNA) being a driver in each tumor genome." However, apparently results are only provided at the level of gene-cohort. Can this be addressed, please?

c) How are different sample-specific MutSet values converted into a single cohort-wise value per gene?

d) Is the only difference between the MutSet channel and the summary computed in PathReg channel the fact that in the former the NEA is computed only for mutated genes, while in the latter it is computed for all genes in the network?

e) When explaining the PathReg, the authors state that "the μic value would reflect a general propensity of i to interact with constellations of putative cancer genes" and that "The μic profiles were rather scarce due to rare occurrence in MGS of true drivers that would interact with a given gene i". However, in the μic measures the NEA score of each gene with the mutated genes across samples, not with previously identified driver genes. Can the authors clarify this please?

f) How are p-values for the MutSet algorithm computed?

g) How were the cutoff qvalues of 0.05 and 0.01 selected? How do they compare in terms of number of genes that pass each?

h) Could the authors clarify the rationale under the selection of nine TCGA cohorts (among 34) to apply their algorithm?

i) It is not clear to some reviewers why the authors described their algorithm as "individualized". It may give the impression that it is aimed at identifying alterations driving a patient's tumor, rather than genes that are cancer drivers across tumors. Could this terminology be clarified please?

3. Please articulate more clearly what the conclusions of the study are. Results should provide a big picture summary of the method that is understandable to non-experts, while technical details might be better presented in the methods. Specifically, it would be good to answer the following questions:

a) How many driver genes are identified in each cohort? This information does not seem easy to find. A long supplementary Table contains q-values for all genes (>19,000) across all cohorts, but this is impractical to navigate. It would be easier to have a table containing only significant genes, with the numbers reported in the text and presented in Figures.

b) It was brought up that KEGG Pathways in Cancer may not be a good standard to evaluate the performance of an algorithm aimed at identifying driver genes from their mutations across tumors. Reasons are: First, they contain manually selected genes that fit functional interaction in pathways, which may leave out some relevant genes. Second, because they contain genes connected through functional interactions into pathways, some of them may not be drivers at all, but only connected to drivers. Since the NEAdriver method exploits network connections to identify significant genes it may not be surprising that its output shows the best overlap with these curated pathways. It may be better to do a more comprehensive comparison with gold standard lists of cancer driver genes, such as the Cancer Gene Census (this would be solved by doing the false positive rate calculation described in point 1).

c) What is the gold standard set used to compute the ROC curves shown in Figure 2? From the text it would seem that genes in KEGG pathways are used as true positives, but these are also evaluated, so the evaluation dataset must be external. Can the authors please clarify this?

d) There's a plethora of published methods that identify signals of positive selection in the mutational pattern of genes across tumors. For articles that summarize groups of such methods, see PMID 29625053 or PMID 32778778. This paper should include a thorough benchmark and comparison of the NEAdriver method to these state of the art algorithms.

e) Please specify which version of the genomics data was was used (the gcs.cancer.gov portal hosts multiple versions from the TCGA data -Hg19 and Hg38, multiple file formats). Linked to this – why did the authors not use a more recently processed version of the TCGA data than the one on GDC portal (e.g. there are multiple pan-cancer follow up publications)? And, could it be specified what type of data was downloaded from TCGA (VCFs, MAFs, Or BAMs)? This is not specified in the methods and without this information it is hard to assess what the authors have done to ensure that their variant calling is accurate. For example, a reviewer mentioned that there are a number of similar genes in the heatmaps (ITGB6, ITGA8, ITGAL etc). These may act in the same pathways but are also paralogues – how can the authors be sure that mutations detected in these are real and not an issue of mismapping?

f) Finally, more generally, is there a new class of driver genes that can be identified based on the authors' approach that could not be understood based on previous studies, or alternatively, could this method/strategies be expanded to predict other phenotypes than driver genes? Was a new cancer gene or driver mutation discovered that could not be explained previously and that can now be viewed in a new perspective based on the authors' work? Highlighting a few of these examples would make the impact of their paper much stronger.

4. Please add a code availability section (e.g. GitHub repository).
