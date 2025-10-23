# Peer review - Round 1

Editors:
- Deborah Bourc'his, Institut Curie France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.51373.sa1](https://doi.org/10.7554/eLife.51373.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The PRC2 complex – responsible for the deposition and maintenance of the repressive H3K27me3 chromatin mark – exists in different configurations, which can be altered in cancer. The authors report here that one PRCS2 co-factor, PHF9, is overexpressed in cellular models of prostate cancer. Surprisingly, upon knockdown of PHF19, PRC2 binding and deposition of H3K27me3 are enhanced, through the compensatory action of MTF2. This phenomenon seems important for proliferation and invasiveness of prostate cancer cells. In aggregate, this study reveals that the balance between PHF19 and MTF2 modulates PRC2 binding and activity on chromatin state and gene expression, and this could influence tumorigenesis.

Decision letter after peer review:

Thank you for submitting your article "PHF19 mediated regulation of proliferation and invasiveness in prostate cancer cells" for consideration by eLife. Your article has been reviewed by Kevin Struhl as the Senior Editor, a Reviewing Editor, and three reviewers. The following individual involved in review of your submission has agreed to reveal their identity: Celine Vallot (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The PRC2 complex – responsible for the deposition and maintenance of the repressive H3K27me3 chromatin mark – exists in different configurations, which can be altered in cancer. The authors report here that one co-factor of PRC2, PHF9, is overexpressed in cellular models of prostate cancer but only the long isoform of PHF19 (PHF19L) associates with PRC2. Surprisingly, knockdown of PHF19 enhances PRC2 binding and deposition of H3K27me3, which the authors link to compensation by MTF2. This phenomenon seems important for proliferation and invasiveness of prostate cancer cells. Studying the role of PHF19 in cancer cells is of importance to understand processes of gene misregulation in tumorigenesis. PHF19 had been previously studied in a variety of cancer models but this is the first report in prostate cancer. Most importantly, this study reveals that the balance between PHF19 and MTF2 modulates PRC2 binding and activity on chromatin and gene expression, and this could influence tumorigenesis. However, some conclusions are not sufficiently supported by experiments and statistical tests are too often lacking. Please address the following concerns in a revised version of the manuscript:

Essential revisions:

1) Two important and unanimous critics relate to the overall lack of information about replicates and insufficient statistical assessments.

Information on replication should be more comprehensive and systematically provided in Figure legends. For example (and not the least important), it is not known as to whether ChIP-seq experiments were performed in replicates or not. The use of spike-in is appreciated, but if there is no biological replicate, this should be acknowledged by the authors as a clear disclaimer in the text. This is particularly important as the conclusion from the ChIP-seq is at the center of the main conclusion of the study and also, because the increase in H3K27me3 (Figure 3A, right) is minor and would only be convincing if observed across replicates. On this point, the authors state that the increase is small albeit "significant", but no statistical test is presented.

Indeed, there is generally poor statistical back-up of the results. Some p-values are provided for Figure 4B and Figure 6C, but most of the other comparisons lack statistical testing. For example, in Figure 4D, no statistical testing is done to evaluate the significance of the overlaps. Please provide appropriate statistical tests. Moreover, it is suggested that all p-values should be corrected for multiple testing – Benjamini-Hochberg procedure for example.

2) About the conclusion that PRC2 binding is increased genome-wide upon shPHF19L: from Figure 3C, it is clear that there is an increase at existing PRC2 peaks. But is there as well an increase in the number of PRC2 peaks? This needs to be analyzed by comparing peak calling in shPHF19L vs shCTRL, as well as a proper differential analysis of ChIP-seq signal in common peaks (using Limma or edgeR for example). This comment is actually valid for all ChIP-seq analyses of the paper.

3) While a CRISPR-Cas9 mediated knockout of PHF19L would be preferable to shRNA approach, at minimum, the authors should include a second shRNA construct. This would ensure that the interesting observations from this manuscript (enhanced PRC2 recruitment and or gene expression changes) are not an artefact of one shRNA knockdown. Targeted approaches (ChIP-qPCR and RT-qPCR) on few loci would be appropriate.

4) For Figure 2E, plots representing the detail of the data are needed, not average plots only. One could use scatterplots comparing PHF19 enrichment signal (log2 IP/INPUT) versus EZH2 (SUZ12, H3K27me3) enrichment. Such plots would give the reader insight on the co-occupancy of the factors. These plots should be complemented with a correlation score to assess the significance of this co-occupancy for example.

Suggested revisions:

1) Are any of these gene expression changes presented in Figure 5 directly related to loss of PHF19 or gain of MTF2/PRC2 binding? It is very important the authors include this data to show whether or not these expression changes are as a direct result of PHF19 knockdown. Rescue experiments would be recommended.

2) It would be interesting to mine the TCGA database. On top of the present analysis of PC3 and DU145 prostate cancer cell lines, it may be useful to document that PHF19L/S is also overexpressed in tumor versus normal cells in prostate cancers. Cell lines can sometimes diverge from what happens in tumors.
