# Peer review - Round 1

Editors:
- Murim Choi, https://ror.org/04h9pn542 Seoul National University Republic of Korea

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78012.sa0](https://doi.org/10.7554/eLife.78012.sa0)

To test differential anticancer drug effects on different tissue types, and to understand drug response mechanism, the authors set up a series of RNA-seq and ATAC-seq experiments on drug responsive and non-responsive cell lines. Then they conducted bioinformatic analyses to pinpoint networks that are altered in responsive vs non-responsive cell lines. Remarkably, they used their analytic results to calculate tumor- and sample-specific response to the drug.


---

# Peer review - Round 1

Editors:
- Murim Choi, https://ror.org/04h9pn542 Seoul National University Republic of Korea

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78012.sa1](https://doi.org/10.7554/eLife.78012.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Decoding mechanism of action and susceptibility to drug candidates from integrated transcriptome and chromatin state" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Murim Choi as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Mone Zaidi as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Zilu Zhou (Reviewer #2); Jocelynn Pearl (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers thought that the quality of the manuscript is high, but also thought that it contains several aspects of potential improvements to assure publication in eLife. To briefly summarize their concerns:

1) Design aspect: biological and clinical performance of 3-CePs is not clearly described. Is there any data that illustrates that HCT-15 is low-sensitivity vs BxPC-3 is high-sensitivity?

2) Analytic aspect: is this approach capable of finding signals that are already constitutively expressed in different cell lines? Need more explanation for vCocena and hCoCena, and what are their differences with CoCena2. Were the tests corrected for multiple testing?

3) Application aspect: What about its prediction accuracy within an individual cancer subtype? Will it achieve high prediction accuracy on intra-tumor type heterogeneity? Can the algorithm be applied to other drugs in this same class?

Reviewer #1 (Recommendations for the authors):

The crosswise approach is not easily comprehendible. It appears to be a network analysis on the union of genes from RNA-seq and ATAC-seq. I wonder if the introduction can be more clear and state uniqueness compared to existing approaches.

Overall, figure quality is high. However, color coding in figures (cell lines, timepoint, drugs, etc) is unique but not intuitive. Therefore, I had to refer to legends all the way to the last figure. I would suggest changing the color scheme to more intuitively or just use numbers/texts.

Reviewer #2 (Recommendations for the authors):

Overall I found this manuscript very interesting to read and significant to the field. However, please consider the following questions/comments:

1. Authors mentioned that HCT-15 is low-sensitivity vs BxPC-3 is high-sensitivity. Is there any data that illustrates this point? Or any description of the phenotype after treatment?

2. Can the authors describe more about vCocena and hCoCena in Method/Supplement, and what are their differences with CoCena2? I wasn't able to find the answer from the provided citation.

3. I am also confused about Figure 5B panel 1 on GFC. I thought GFC is a relative fold change compared to treatment to control. What is the control group in this case to calculate GFC?

4. The pink module is clearly of interest as it showcases the necessity of this multi-omic approach. More generally, can we label all the modules that are only identifiable cross-wise but not by single omic? Can we show a few more detailed examples here? Why are they identified now but not by the single omics approach?

5. The prediction algorithm at the end shows good prediction power across cancer types. What about its prediction accuracy within an individual cancer subtype? Will it achieve high prediction accuracy on intra-tumor type heterogeneity?

Reviewer #3 (Recommendations for the authors):

I enjoyed reading your work and the approach you took to integrating multi-omics data to better understand the mechanism of action and epigenetic signatures of 3-CePs in cancer cell lines. The manuscript was clearly written, and I appreciated the thorough results and methods sections which allowed me to clearly follow the majority of the steps taken.

As for major revisions, I believe it would be valuable if the authors would test their sensitivity model for compound B in addition to compound M in cell lines described on page 12 and in Figure 6D.

It is great to see your work in this space and I am hopeful that it further strengthens the use of these data types and analysis methods for improving the drug development process. I will include my general thoughts and suggestions below.

General Thoughts

The paper is long – especially the Results section. But I think for this style of work it is better to have a longer, more thoroughly described results and methods section than to leave out key details.

I would prefer if the paper included p-values for key findings in the text of the article instead of having to locate them in the supplement or figures. I did not see FDRs or q values mentioned throughout the paper/findings – were these calculated? Was there a reason the authors chose to report p-value<0.05 findings as opposed to an FDR/q-value threshold? I find that with gene set enrichment analyses, it can be important to use FDR.

With regards to the crosswise integration method performed, the authors describe a threshold minimum of 15 nodes per cluster on page 23, line 757 of the manuscript. How was this threshold selected? It would be helpful to mention the total sample size input for constructing the network in these sections.

For the sensitivity signature, the authors selected LASSO regression – did the authors consider linear regression? How was LASSO chosen?

For the genes included in the perturbation-informed signature (294 up, 170 genes down), what was the p-value and fold change thresholds used?

For the sensitivity score (described page 12) – do the authors think that this is the ideal model for calculating a sensitivity score? Did they play around with changing the input for the sensitivity model or the model itself? It would be helpful to understand in greater detail why the authors felt that this was the best input for the model.

The validation of the sensitivity prediction on cancer cell lines is given a short, one-sentence description in the results. This could be better explained.

In the discussion and in other locations in the text, the authors describe their approach as 'efficient and versatile' which I think generally ignores the fact that this required next-generation sequencing, two assay types (RNA-seq, ATAC-seq) and in-depth systems biology approaches. Is the argument that the network model is now versatile in that it can be applied to other drugs in this same class? Or that the approach can be borrowed by other groups for other classes of drugs and sample types?

In the methods section, there were a few details I would like to see added. Product numbers including the ATCC product #s, propidium iodide product #, RNA tape station assay. EDTA concentration in ATAC-seq. For clarity, I recommend breaking the RNAseq and ATACseq methods sections apart. Please also include the sample numbers per group that were sequenced. This was hard to find.
