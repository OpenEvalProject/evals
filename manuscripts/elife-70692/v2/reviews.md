# Peer review - Round 1

Editors:
- Gene W Yeo, University of California, San Diego United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70692.sa1](https://doi.org/10.7554/eLife.70692.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This study describes an analysis of cell type-specific alternative splicing using 10x scRNA-seq data. This work shows that in spite of the challenges associated with the analysis of such datasets, it is possible to identify alternative exons with differential splicing between tissue compartments and to some extent reveal cell types by splicing profiles of single cells. This work is informative regarding what can be done to analyze alternative splicing using 10X data and fills in a gap in the field. Your revised manuscript addresses reviewers' concerns and strengthen the manuscript for the general audience and we are most appreciative of it.

Decision letter after peer review:

Thank you for submitting your article "RNA splicing programs define tissue compartments and cell types at single cell resolution" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Patricia Wittkopp as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The computational analysis appears to be solid in general but the presentation, as in the current form, need to be improved before publication.

2) Overall, there is little doubt that alternative exons near the 3' end of the transcripts can be studied by 10X data, but the scope is relatively limited. This is confirmed in this study, as only 1353 genes can be quantified at the exon level and only 22 genes were identified to have differential splicing. The study needs to be very clearly discuss this major limitation and balance the pros and cons of their method.

3) The algorithm is under review at another journal and has made the review process here difficult (several reviewers bowed out for this reason) – thus is is very important for SpliZ to be thoroughly discussed here. It would actually be even better if the paper describing the method were accepted for publication prior to publication of this work.

4) Some claims are made that are not fully substantiated by the data, which could be addressed by adding more context to the analyses. Furthermore, some figures can be tweaked or expanded upon in the text to improve clarity. In particular, the following sections should be amended:

"Supporting the idea that SpliZsites 31 discover real biological signal, 13% of the SpliZsites in the human are also identified as SpliZsites in the mouse lemur and/or mouse (Methods)."

Insufficient context is provided here for readers for this conclusion. The authors should compare this number to a shuffled dataset or other background data to demonstrate the supposed significance of the 13% number provided.

Reviewer #1 (Recommendations for the authors):

Some claims are made that are not fully substantiated by the data, which could be addressed by adding more context to the analyses. Furthermore, some figures can be tweaked or expanded upon in the text to improve clarity. In particular, the following sections should be amended:

"Supporting the idea that SpliZsites 31 discover real biological signal, 13% of the SpliZsites in the human are also identified as SpliZsites in the mouse lemur and/or mouse (Methods)."

Insufficient context is provided here for readers for this conclusion. The authors should compare this number to a shuffled dataset or other background data to demonstrate the supposed significance of the 13% number provided.

In Figure 2B the authors demonstrate prediction of cellular compartment of cells using k-means clustering analysis on SpliZ scores from two genes. The claim in the main text: "Setting k=3, cells from stromal, epithelial, and immune compartments were classified with accuracies of 78%, 84%, and 95% respectively independent of gene expression". Though these were the results from one of the two individuals in the dataset, the accuracies were much worse for the other individual, and the text is misleading here in only focusing on the cleaner data. The authors should acknowledge this in the text, and address the possible factors causing lower accuracy in individual 2. Furthermore, given the cells come from 4 tissue compartments (immune, epithelial, endothelial and stromal), the authors should elaborate on the decision to set k to 3.

Figure 3A, a legend for the squares and the circles, indicating 10X and Smart-seq can be more clear. (like those in Supp Figure 2)

Figure 7B, though the splicing changes are correlated across the species, the directionality of splice site usage is inverted across species. The authors can discuss more on the biological meaning.

Reviewer #2 (Recommendations for the authors):

The computational analysis appears to be solid in general but the presentation, as in the current form, need to be improved before publication.

1. Overall, I do not have doubt that alternative exons near the 3' end of the transcripts can be studied by 10X data, but the extend is relatively limited. This is confirmed in this study, as only 1353 genes can be quantified at the exon level and only 22 genes were identified to have differential splicing. I think despite the limitation, efforts to mine splicing using 10X data should still be encouraged, given the explosive number of datasets available. However, the discussion of the pro and cons should be balanced (e.g., the 3' bias should be discussed).

2. The authors used a new pipeline named SpliZ for analysis (preprint cited as ref. 26), and several variations SpliZsite and SpliZVD were also used. While it is fine to present technical details in separate publications, key features have to be described in the manuscript, which is required for understanding the results. For example, what does SpliZ measure (something similar to PSI I assume), what is SpliZsite (filtered splice sites from STAR alignments?), what is the difference beteen SpliZ and SpliZVD? How dropout and UMIs are handled in the pipeline?

3. Insufficient descriptions were provided in multiple figures.

Figure 2A, circles and squares were not explained (they were explained in Figure 3 below). How the dot plots are related to the splice sites shown in the sashimi plots and how the splice sites in the sashimi plots are related to the gene structure schematics (need some guesswork)? What is shown in the boxplot (labelled "Average 3' splice site per cell", which I assume it SpliZ score, but again is this the fraction of reads that uses the upstream 3' splice site?)

Figure 2C, D. Is each dot a single cell or a "meta cell" that averages a certain number of individual cells?

Figure 3A, how the gene structure schematic relate to the boxplot above is confusing. Also in the gene schematics of the three species further down, it is confusing why two parts of the human gene were highlighted (only the two 3' splice sites near the 3' end are relevant?). Unclear what is shown in the illustrations on the right of the gene schematics.

Figure 3D. How exons labeled 5,6,7 are related to site 1 and 2 in A-C (need guesswork)?

Figure 4. Only read fraction is shown but not SpliZ scores?

Figure 5A, similar to the question for Figure 2A, how the gene structure schematic relate to the boxplot above is confusing.

Figure 6C. It does not seem to be the evidence of a single exon to distinguish two subpopulations of monocytes are convincing. How do we know whether the two subpopulations reflect certain technical issues (potentially similar to the controversial "bimodal splicing" proposed in previous publications)?

Similar confusion in Figure 7 as in Figures 2 and 5.

4. I thought some global evaluation on the reliability of 10X results using independent datasets will be important (e.g., correlation of differential splicing in comparison with results from bulk RNA-seq and/or SMART-seq data). Some of the results presented in Supplementary Figures(e.g., Figure S6) can probably presented as the main figure.
