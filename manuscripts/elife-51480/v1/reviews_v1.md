# Peer review - Round 1

Editors:
- Alfonso Valencia, Barcelona Supercomputing Center - BSC Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.51480.sa1](https://doi.org/10.7554/eLife.51480.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The analysis of breast cancers at the level of Copy Number Alterations to asses intra-tumoral genetic heterogeneity at the level of single-cell sequencing is an important advance, especially because the results translate into a number of interesting new biological observations, for example, X-loss in ER- tumors and pseudo-diploid cells, among others.

Decision letter after peer review:

Thank you for submitting your article "Novel insights into breast cancer copy number genetic heterogeneity revealed by single-cell genome sequencing" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jeffrey Settleman as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Jonas Demeulemeester (Reviewer #1); Daniel Rico (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Baslan et al. present an in-depth characterization of intratumor copy number heterogeneity in a cohort of 16 primary breast cancer cases: 4 each of the Luminal A, Luminal B, HER2+ and Basal subtype They also generated bulk RNA-seq and bulk genome sequencing for the same samples. The authors isolate nuclei, sort populations with distinct ploidy using FACS, and perform low-pass whole-genome sequencing on an average 116 cells per tumor. Analyses reveal intriguing patterns of both focal and whole-genome copy number heterogeneity which are likely to have clinical relevance. The previous single-cell genome sequencing study in breast cancer primary tumors only included 2 patients (Navin et al., 2011). Therefore, the new dataset presented is the most comprehensive single cell genome sequencing for breast cancer to date. However, the manuscript was not easy to read as there were many different "short stories", which may be difficult to follow for a non-specialized audience. Also, some of the analysis were not clear, which could be improved by making the code and the data available.

Essential revisions:

1) In the second paragraph of the subsection “CNAs and genetic heterogeneity of stromal, non-cancer cells”, the authors describe their breakpoint analysis. At the resolution provided by low-pass whole-genome sequencing, the inferred breakpoints are rough approximations of the true breakends at best. Indeed, authors describe using a window of 3 genomic bins in the Materials and methods. Vice versa, random noise can lead to distinct segmentation in single cells which share a breakend (e.g. the jumps from CN 1 to 2 for the leukaemic cells in Figure 1D). As such, conclusions such as "indicating unique TCRa recombination events", "none of the T-cells shared identical breakpoints" and "genetically distinct as judged by the deletion breakpoints at their respective TCRa locus" should be stated considerably more carefully.

2) Pseudo-diploid cells are identified in the samples and authors conclude they are not precursors to the main tumor clone based on their distinct CNAs. Authors should further assess whether these cells represent early, potential evolutionary dead-end tumor subclones or do indeed stem from normal breast epithelia. To do this, authors could carefully call SNVs on the pooled low-pass sequencing data and subsequently genotype the called variants in the single cells.

3) "High-throughput sequence data should be uploaded before resubmission, with a private link for reviewers provided (these are available from both GEO and ArrayExpress)" The data availability section is not very clear: is it already available, in which case I could not find the related project on SRA (= Short Read Archive, not Short Reach Achieve) nor any link to the data.

4) The analyses of the data shown on Figure 1D are not sufficiently quantitative. Breakpoints accuracy is inherently limited with shallow coverage sequencing and will correlate with technical aspects, such as number of reads, duplicates, noise in the data, etc. The authors merge breakpoints if in adjacent bins but that these four profiles on Figure 1D visually look different is not enough to persuade readers that biological rather than technical effects are driving the differences. As this is a major claim in the manuscript, the authors are encouraged to make the analyses more quantitative (at least consider the impact of one noise metric related to "depth of coverage" in the comparison, as it could be driving the differences between the batches of single nuclei).

5) Figure 2B: The more single nuclei were sequenced and included in the analyses, the more likely that some events will be considered subclonal (>=10 nuclei with a different state). Hence, before reaching any conclusions, the authors should explicitly correct the fraction of genome subclonal for this. It looks from other figures that the number of nuclei per cancer sample can vary quite substantially thus potentially influencing the subclonal fraction. As a quick check, an easy way to correct for the number of nuclei analyzed would be for each patient, to downsample to the number of nuclei in the patient with the lowest number.

6) Figure 5A same remark as Figure 2B applies.

7) It would be useful to also have the processed data available. I could not see if it is actually included in the SRA BioProject (I guess the accession ID is not yet publicly available) but it would be good to have the patient metadata, the gene expression data, CNA calls of both the bulk and the single-cell samples in supplementary data files and/or in a relevant repository for direct download. As gene expression levels and CNA calls do not contain sequence information, these data should be made available without any restrictions.

8) The results of different interesting analyses are presented to illustrate the usefulness of the data. However, I had the impression that there were several inconclusive stories: the loss of chromosome X, for example, in connection with BRCA1 and X inactivation is intriguing but it is not further investigated. The authors may want to choose if they want to further invest in making the resource data available for different types of users or choose one of the observations (there are up to nine different conclusions in the Discussion!) to extend further for a more solid and complete "Research Article".

9) Some strong claims are made regarding the association with biological subtypes and patient stratification. For example, the sub-clonality of each tumor is precisely calculated with hundreds of cells per tumor, but at the end of the day there are only 16 patients, just four per sub-group based on gene expression. Indeed, there are some statistical tests that yielded small p-values (e.g. Figures 3C and 5A) but it is unclear what where the unit of analysis – is the patient the unit of analysis or the cell? The inclusion of the R code used, together with the data, would make the interpretation of these results clearer.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Novel insights into breast cancer copy number genetic heterogeneity revealed by single-cell genome sequencing" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jeffrey Settleman as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Daniel Rico (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The revised version of the in-depth characterisation of breast cancer cases at the level of copy number heterogeneity at the cell level builds an interesting data set, represents an advanced use of the technology and provides information of potential clinical relevance.

Summary:

The revised version of the manuscript has essentially addressed all the key points (i.e. accuracy and level of resolution of the data, cell of origin and linages, and clarification of the narrative and conclusions) but the issues with data and software accessibility have only been partially addressed.

Essential revisions:

For the publication of this article, like for any other one, it is essential that the research community has the ability to the reproduce the reported results. In this case, the metadata associated with the processed data in the supplementary file is missing and the software code to reproduce the various analyses presented is not available. These are significant issues that have to be corrected.
