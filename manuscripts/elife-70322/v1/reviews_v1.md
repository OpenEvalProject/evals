# Peer review - Round 1

Editors:
- Bérénice A Benayoun, University of Southern California United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70322.sa1](https://doi.org/10.7554/eLife.70322.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

Maternal exposure to a certain phthalate (DEHP) has been shown to cause spermatogenesis defects in the male progeny, and in their offspring. In this manuscript, Tando et al. have investigated the molecular consequences of this maternal exposure on fetal and adult male germ cells by studying DNA methylation and gene expression by large-scale approaches. They found three genes previously known to be involved in spermatogenesis that are deregulated following maternal exposure to DEHP and which could contribute to the observed spermatogenesis defects.

Decision letter after peer review:

Thank you for submitting your article "Epi-mutations for spermatogenic defects by maternal exposure to Di (2-ethylhexyl) phthalate" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Jessica Tyler as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Ludwig Stenz (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

1. The reviewers had concerns about the robustness and clarity of the statistical analyses that need to be addressed in a revised manuscript. This includes (i) much more detailed description and clarifications on the statistical methods (i.e. inclusion of software version numbers, FDR cutoffs, etc.), (ii) need to revise any analysis relying on the deprecated use of the FPKM framework, (iii) use of Student t-test in the absence of proof of normal distribution.

2. There were some concerns about the small number of replicates used (n = 2), reduced to n=1 for one type (E19.5 DEHP RNAseq analysis). This small number of replicates provide extremely limited statistical power and thus will make it difficult to capture the extent of biological variation (potentially missing many true targets). The ideal solution, which the reviewers recognize may be too time-consuming and difficult to achieve right now, would be to add 2 additional replicates to these analyses (so as to be able to account for batch effects). However, if this is too difficult to achieve, the reviewers recommend that all general conclusions be strongly toned down in the abstract, text and discussion to reflect that there is strong statistical support only for 3 targets that are further validated (Hist1h2ba, Sycp1, and Taf7l). The limitation due to the small sample number should also be explicitly discussed.

3. Please clarify other reviewer concerns that may affect understanding/interpretation/reproducibility of results: Reviewer #2 point on Hoechst blue/Hoechst red, reviewer #3 point on the unusual GFRA1 signal in spermatocytes.

Reviewer #1 (Recommendations for the authors):

1. RNA-seq data need to be reanalyzed as described in the Public Review.

2. The Materials and methods section on RRBS analysis and RNA sequencing should include a detailed description on how significant regions or genes were defined (i.e. FDR significance threshold, etc.). The thresholds for false discovery rate should also be clearly indicated for the DAVID analysis (currently only p-values are indicated in Figure 2).

3. For long-term reproducibility of analyses, all version numbers of all software and packages should be provided in the Material and Methods (e.g. Tophat2, Bowtie, Cuffdiff, etc.). In addition, analytical code should be made available either as a Supplementary file or through a Github repository. Finally, all accession information should be available – it was not at the time of review (see lines 501-504).

4. Authors used unpaired two-sided Student's t-test to calculate statistical significance for a number of assays, including those in Figure 1C and Figure Supplement 1C. As a t-test can be applied when the dataset follows a normal distribution, a normality test should be performed and indicated. If normal distribution of the data points cannot be shown, a nonparametric statistical test (e.g.Wilcoxon test).

Reviewer #2 (Recommendations for the authors):

1) The figure supplement 2 is of high importance for understanding the cells purification process and should be more up in the manuscript instead of being a supplement; it is one of the key technical achievement of the work.

a) GFP-positive germ cells were extracted from adult by using a transgenic mice with GFP green produced under the control of the Oct4 promoter, Oct4 being a germ cell marker. That aspect is very clear. However, a breeding schema will be a plus for the reader to get a clear vision of the work. Panel A show how few the germ cells are in F1 embryos according to the Oct4-FACS sorting from the transgenic mice. This probably explain why the authors had to pool different experiments producing only two replicates.

b) The germ cells sub-population extracted from adult testis used another less clear approach (using propidium iodide, a red marker of death and Hoechst staining DNA in blue). Panel B of the Figure strangely mention Hoechst blue in one axe and Hoechst red in the other and propidium iodide appears in the material section, as if it was a mistake somewhere. Moreover, I do not understand really if the transgenic mice were also used for F1 adult and how GFP may interfere with the red and blue emission used to extract the cells.

c) The legend of the figure mention "C.D." but there is no panel D.

2) In the first paragraph of the results, tubules divided by the presence of vacuoles, which appear associated with defect in germ cells.

a) I think that germ cells default is the important aspect of the work, instead of vacuole. (i.e. "in tubule with large vacuole, germ cells were typically deleted" → tubule without germ cells contains large vacuole…). That explain the decreased sperm counts we and other observed in F1 male after prenatal exposure to DEHP. Please illustrate the vacuole in the different type of tubule with arrow in Figure 1.

b) Apoptotic cells detection required Tunnel assay.

3) For the heat map, such as in Figure 2 panel A, please explain the sense of the colors blue and red, as reflecting the sense of the promoter methylation changes.

4) Figure supplement 3, mention testicular somatic cells instead of somatic cells.

Reviewer #3 (Recommendations for the authors):

My main concern is the small number of replicates. At least a third replicate per sample type would be needed to produce an accurate list of DMRs and DEGs. Detailed statistical analyses should also be presented.

Another concern is that no statistical difference was found for the F2. I therefore don't think it is accurate to claim in the article that "Expression and methylation of those genes tended to be downregulated and increased, respectively in F2 spermatogonia following maternal DEHP exposure." (abstract and discussion).

Finally, can the authors explain why GFRA1 signal is strong in spermatocytes – as it is normally a spermatogonia marker?
