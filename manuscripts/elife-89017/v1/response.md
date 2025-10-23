# Author response - Round 1

Authors:
- Jose Mario Bello Pineda ([ORCID: 0000-0003-1417-9200](https://orcid.org/0000-0003-1417-9200))
- Robert K Bradley ([ORCID: 0000-0002-8046-1063](https://orcid.org/0000-0002-8046-1063))

## Response text

DOI: [10.7554/eLife.89017.3.sa3](https://doi.org/10.7554/eLife.89017.3.sa3)

The following is the authors’ response to the original reviews.

Reviewer #1:

Figure 1

The "matched primary tumors" from TCGA include n=424 from cutaneous melanoma; but it is unclear where this is coming from; the PanCan Atlas for melanoma shows n=81 primary and 367 metastatic tumors. There are also additional large cohorts of ICI-treated metastatic tumors with RNAseq data (e.g. a metastatic melanoma cohort with 100+ patients https://doi.org/10.1038/s41591-019-0654-5) that would increase the numbers here.

We thank the reviewer for their observation. We have replaced references to “primary” cancers as “TCGA” cancers as appropriate. While the TCGA analyses included metastatic samples, the majority of the TCGA tumors in most cohorts correspond to primary cancers or local metastases, a point which we added to the text. We retained Fig. 1D as the representative examples are actual primary samples. We have decided to defer analysis of additional melanoma cohorts for future inquiry.

Figure 2

What is the basis for the split between high and low Dux4 expressing tumors at 1 TPM? Is it arbitrary, or based on some structure in the distribution? (e.g. bimodal distribution)

Our previous analyses of RNA-seq datasets derived from early embryogenesis samples (PMID: 3132774, 28459457) showed that physiologic levels of DUX4 range from approximately 2 to 10 TPM. We added a description in the methods section, under “Genome annotations, gene expression, and Gene Ontology (GO) enrichment analyses,” of our conservative choice for the threshold: DUX4-positivity defined as expression levels > 1 TPM.

Figure 3

Overall claim is that Dux4 expression is associated with worse survival in metastatic urothelial carcinomas treated with PD-L1 inhibitor. However, the rationale for the choice of split (Dux4 expression < 0.5 and > 1 TPM) to show is unclear (is this the 25th percentile? 75th percentiles?), and the rationale/interpretation of the "partial adjustment" for TMB by removing the bottom quartile of TMB feels non-rigorous and prone to bias. It doesn't feel like Fig 3bc contributes very much; Figure 4 really is the more rigorous analysis.

We thank the reviewer for these comments and suggestions. We adjusted the analyses in Fig. 3C and Fig. S3 to be consistent with Fig. 1 and Fig. 2, in terms of the choice of split. We also clarified in the text how our initial, crude TMB adjustment served as an important indication for us to pursue more rigorous statistical approaches.

Figure 4

Dux4 expression is independently associated with worse survival considering other clinical and molecular characteristics

I would include TGFB in the features considered in the table (in the supplementary but not the main table or forest plots, not sure why not?)

The choice of Dux4 expression split ( < 0.25 and > 1 TPM) feels arbitrary and is different than the split in Figure 3; what is the rationale for this? Also, how many patients does this exclude? (TPM between 0.25 and 1). What does the continuous value or median split for Dux4 expression give you for the CoxPH model?

Re: building a predictive model, excluding patients (e.g. between <0.25 and > 1 Dux4 TPM) makes the model difficult to apply (e.g. cannot apply to patients with Dux4 levels in the missing interval); a better predictive model would include all patients in the cohort.

We thank the reviewer for their other suggestions. We have clarified in the text that our choice to define DUX4negative samples as those with DUX4 expression levels < 0.25 TPM was made to preemptively address potential misclassifications due to decreased sensitivity of bulk RNA-seq at very low expression levels (PMID: 18516045). We believe our classifications with the new scheme are more reliable. We have also now specified in the text that our categorization excludes 126 patients. We have decided to not pursue the addition of TGFB or exploration of the use of an alternative split or continuous version of DUX4 expression in the Cox Proportional Hazards analyses but appreciate the suggestions, which we will keep in mind for future studies.

Figure 5

An RSF (randomized survival forest) model predicts survival in Dux4+ vs Dux4- patient, and the Shapley values for landmark time analyses show time-varying effects of different features.

In some sense, the authors have already demonstrated that Dux4+ is associated with survival differences in ICI treated patients; so a model that predicts survival applied to Dux4+ and Dux4- patients that shows a difference in survival is unsurprising (even in a training/test set setting given that there is a difference in survival across the entire cohort). The quantified marginal effect (from a predictive perspective) of different features is what is interesting here. In that light, I'd like to see more validation of the model up front, specifically how close the predicted survival is to the actual survival of patients (e.g. the survival curves in Fig 5a but with actual survival of the Dux4- and Dux4+ cohorts superimposed on the predicted probabilities).

We thank the reviewer for this suggestion. We have added a plot showing the superimposed survival probability estimates over time for the RSF and KM models for patients assigned to either the test or training sets in Fig. 5.

SFig 5

Unclear how the authors got estimates of the # of expected deaths associated with covariates (e.g. "...we measured an increase in the number of predicted deaths associated with DUX4-positivity by approximately 16, over DUX4negative status (Fig S5F-G).") from Shapley values as shown in the indicated figure - is this 16 out of the entire cohort? At a given time point? Would recommend perhaps showing the inferred absolute change in mortality (e.g. 8% absolute increase in mortality)

Mortality is the expected number of deaths for the cohort over the observation window, measured as the sum of the CHF over time. We have clarified this in the Methods section, under “Random Survival Forest, feature importance, and partial dependence.” We have also changed the quantification to show the absolute mortality differences comparing patients with DUX4-negative and -positive tumors; we thank the reviewer for this suggestion. We have also clarified in the text that adjusted mortality was estimated via partial dependence, which operates using the correct units, as opposed to Shapley values, where attribution is scaled. Finally, we changed the referenced figure when discussing changes in mortality associated with TMB and DUX4 status (Fig. S5H-I); we appreciate the reviewer pointing out this error.

Figure S1B-C

The authors argue that Dux4 expression is not an artifact of FFPE tissue by analyzing a mixed tumor cohort sequenced with both poly-A and hybrid probe capture in matched flash-frozen and FFPE tumor samples, showing that it is (1) detectible both FFPE and flash-frozen tissue and (2) higher levels are detected in polyA sequencing/frozen tissue. However, the reference for this section (D. Robinson et al 2015) is a study of a cohort of prostate cancers with polyA bulk RNAseq sequencing; is this correct/is the data coming from a different study?

Analysis of scRNAseq (if available) would strengthen their analyses by better delineating the expression and response of interferon-gamma and downstream (e.g. antigen presentation) pathways in specific cell compartments, and potential differences in cell-cell interactions (e.g. using CellPhoneDB) associated with Dux4+ vs Dux4- tumors.

Do the investigators find similar findings in primary and metastatic tumors sequenced the same way (e.g. tcga primary vs met melanoma, albeit most of the met melanoma are Stage III lymph nodes)?

We thank the reviewer for finding the citation error. We have corrected the manuscript to reflect the correct study we analyzed (PMID: 28783718). We also thank the reviewer for their additional suggestions, which undoubtedly would strengthen the current study. However, we have respectfully decided to defer these additional analyses for future study.

Reviewer #2:

It is strange as a statistician to see BIC and AIC represented as barplots, e.g. Figure 4B. There is no knowledge to be gained through this visual representation that would not otherwise be conveyed by just giving the numbers.

We thank the reviewer for this suggestion. We understand that simply stating the numbers would be equally informative. However, we respectfully decided to retain our current versions of Figures 4 and S4 so that the numbers can be illustrated in a visual manner in the figures, rather than just stated in the text.
