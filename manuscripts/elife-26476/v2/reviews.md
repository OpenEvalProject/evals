# Peer review - Round 1

Editors:
- Alfonso Valencia, Barcelona Supercomputing Center - BSC Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.26476.048](https://doi.org/10.7554/eLife.26476.048)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Simultaneous enumeration of cancer and immune cell types from bulk tumor gene expression data" for consideration by eLife. Your article has been favorably evaluated by Naama Barkai (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted these comments to understand if it will be possible for you to provide what the reviewers consider essential to the publication of this work. At this point we ask you to provide a detailed response with an action plan and timetable for the completion of the essential tasks noted below. We will have the Board and reviewer consider your responses and issue a binding recommendation as soon as possible.

Summary:

This manuscript describes the EPIC method to estimate the proportion of cancerous cells and immune cells of various types within a bulk gene expression profile of a tumor sample or PBMC. The work fits within the recent renewed interest in the area of expression deconvolution in tumor-infiltrating lymphocytes.

The method is based on the extrapolation of the proportion of RNA in standard cell types to determine the proportion of cell types in mixtures. The main features of the method are: it takes into account the estimated proportion of RNA in the samples, weights highly the contribution of less variable genes in the reference set, it does not make assumptions about the heterogeneity of the non-normal cells in the samples, and, it uses the expression of maker genes that are not expressed in cancer cells to normalize the proportion of tumor/non tumor cells in the samples. The data presented correspond mainly to metastatic melanoma samples with some additional colon cancer cases.

Essential revisions:

1) The works requires a clear demonstration of the capacity of the method to do well estimating cell subsets at higher resolution, as this seems to be the main advantage of the method.

2) A better analysis and clarification of what are the key steps of the procedure that improve the results.

3) Clarify the dependency of the results of outliers and in general revise the significance criteria.

4) Make the system accessible via a web interface.

Other concerns:

1) – The authors should consider to extend the reference gene expression profiles to additional cell types such as stromal and endothelial cells which are known to have a role in tumor microenvironment as well as deepen the separation between cytotoxic T cells (CD8 cells) and CD4 T cells gene expression profiles, which currently is low and at a level less than what has been shown to be important correlates for immune-tumor interactions/therapeutic response.

2) Consider rephrasing, the estimation of the tumor in 3D – it is not too surprising given that the melanoma forms the bulk of the tumor in most of these samples and is quite distinct – this is akin to getting neutrophil estimates correct in whole blood.

3) With respect to the second validation (comparing EPIC to IHC data), the authors claimed they observed "a good agreement between cell proportions measured by IHC and our predictions", however there is a weak non-significant correlation (r=0.3, p=0.09) between these factors in macrophages that should be mentioned in the text. This may be due to the maker used in IHC being expressed in other cell subsets or due to protein/mRNA differences – the former being relatively easy to distinguish.

4) The first test and comparison with other methods is carried out with normal blood samples and (Figure 2B). The EPIC method performs better (pearson R) than other methods. Notice that in whole blood (dataset 3 (Linsley et al., 2014)) the differences with CIBERSORT and DSA are minimal. It will be important to clarify if the additional information is provided by the inclusion of the estimated mRNA content in the calculations (Figure 2A versus 2C).

5) Reconsider the following claim "We observed a remarkable agreement between our predictions and experimentally determined cell fractions (Figure 3A). Of note, the proportion of melanoma cells could be very accurately predicted even in the absence of a priori information about their gene expression." in light of the small size of the data sets (4 donors of which two of them dominate the correlation).

6) Comment of the significance of the results in Figure 3B and Figure 3C where the differences are based on single outliers.

7) It will be good to check if in the information in Figure 5A (and supplementary figures) can be better interpreted comparing the method only in normal tissue samples (equivalent to Figure 5 supplementary figures).

8) Assess the significance of the results in Figure 5B.

9) Benchmarking other methods, such as Cibersort by summing high-resolution cell subsets may be incorrect – a better approach would be to replace LM22 with the matrix derived by the authors – if not, I would suggest saying that this comparison is less than ideal.

10) It is not clear from the manuscript whether or not the advance over CIBERSORT is due to a better marker gene set and reference panel or due to the other methodological innovations that they made. This point should be clarified.

11) The reference to the use of "zeros" in the gene expression profile of cancerous tissue as informative to be leveraged in deconvolution in Gosink 2007 and Clarke 2010 should be included.

12) Respect to ISOpure, it is not clear from the description whether ISOpure was run just with signature genes or with the whole gene expression profile.

13) The ideas implicit in DeMix where the ratio of the variances provides an implicit importance weight (Ahn 2013) should be discussed.

Other points:

1) The authors should change the scale and marking of the statistical significance from (*p<0.1; **p<0.05; ***p<0.01) to (*p<0.05; **p<0.01; ***p<0.001) as p>0.05 is not considered significant.

2) The authors claimed that "Immune cells differ in their gene expression profiles depending on their state and site of origin (e.g., blood or tumors)" – a reference should be added.

3) There is a lack in specifying "Supplementary file 4" in the relevant places.

4) Figures and supplementary figures are not numbered in the manuscript, what makes difficult to know what the supplementary figures correspond to what text.

5) The use of a different scale for each method does not help to the interpretation of the figures.

6) Subsection “Validation in blood”: Renormalization by mRNA content is used in (Qiao 2012) to improve the estimates of cell-type proportions.

7) "Prediction of cancer and immune cell type proportions": I found this explanation somewhat confusing because Equation 1 is never actually used in the deconvolution – only Equations 6 and 7. Because Equation 1 is introduced, I expected EPIC to try to solve it at some point.

Regarding references:

1) The authors claim that this is the first deconvolution methodology to take into account total RNA differences between cell subsets is incorrect, to the best of this reviewers knowledge, Baron et al. (Cell Systems 2016) propose a method, Bseq-SC which uses total RNA to improve deconvolution estimates. Of relevance here, their estimates for total RNA levels come from the single cell expression data, information which could be incorporated into EPIC too to increase its resolution.

Other pertinent references include:

Clarke J, Seo P, Clarke B: Statistical expression deconvolution from mixed tissue samples. Bioinformatics. 2010, 26: 1043-1049

Gosink MM, Petrie HT, Tsinoremas NF: Electronically subtracting expression patterns from a mixed cell population. Bioinformatics. 2007, 23: 3328-3334.

Ahn J, Yuan Y, Parmigiani G, Suraokar MB, Diao L, Wistuba II, Wang W. DeMix: deconvolution for mixed cancer transcriptomes using raw measured data. Bioinformatics. 2013 Aug 1;29(15):1865-71.

Qiao W, Quon G, Csaszar E, Yu M, Morris Q, Zandstra PW. PERT: a method for expression deconvolution of human blood samples from varied microenvironmental and developmental conditions. PLoS Comput Biol. 2012

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Simultaneous enumeration of cancer and immune cell types from bulk tumor gene expression data" for further consideration at eLife. Your revised article has been favorably evaluated by Naama Barkai (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

Essential revisions:

The claim that "ISOpure is specifically designed to run genome-wide" does not appear anywhere in the ISOpure manuscript, is not consistent with the uses of ISOpure, and there is nothing obvious in the ISOpure algorithm that makes it specifically designed to be applied genome-wide (such a claim is made for PERT, and one could argue that PERT contains a gene-specific weighting mechanism, like EPIC, which makes it suitable for genome-wide use, but no such claim is made for ISOpure).

Indeed, an ISOpure-like method applied genome-wide in the PERT manuscript does quite badly at recovering the mixture proportions of the various cell types. Therefore, the new version in the revised version regarding ISOpure needs to be revised and inaccurate statements removed.

In conclusion, in the new version EPIC should be compared with ISOpure using the same inputs as CIBERSORT and EPIC.
