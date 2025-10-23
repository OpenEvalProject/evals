# Peer review - Round 1

Editors:
- Gordon Freeman, Dana-Farber Cancer Institute United States

Reviewers:
- Hongbin Ji, Institute of Biochemistry and Cell Biology, Shanghai Institutes for Biological Sciences, Chinese Academy of Sciences China

## Review text

DOI: [10.7554/eLife.49020.035](https://doi.org/10.7554/eLife.49020.035)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Identification of biomarkers that can predict which patients will benefit from immune checkpoint inhibition therapy is clinically important. Wang et al., describe a new computational method to identify responders to immune checkpoint inhibitors by calculating a tumor immunogenicity score (TIGS). TIGS combines tumor mutational burden (TMB) with a gene set score of 18 genes associated with MHC class I Antigen Presentation Machinery (APM) score. They describe the APM score across cancer types in TCGA and correlate APM with other gene expression pathways and immune cell infiltration across cancers. In both a pan-cancer analysis of ICI objective response rates and an ICI clinical response prediction for individual patients, they show that TIGS predicts response to ICI better than TMB alone, PD-L1, immune infiltrate, or Interferon-gene signatures, and somewhat better than the TIDE method based on T cell dysfunction and exclusion gene expression signature. TIGS is a tumor inherent biomarker and may be valuable in predicting response to immunotherapy as well as guiding ways to enhance the immunogenicity of tumors.

Decision letter after peer review:

Thank you for submitting your article "Antigen presentation and tumor immunogenicity in cancer immunotherapy response prediction" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Tadatsugu Taniguchi as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Hongbin Ji (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Wang et al. have developed a method named tumor immunogenicity score (TIGS) that combines tumor mutational burden (TMB) and antigen processing and presenting machinery gene expression signature to measure tumor immunogenicity. They found that TIGS could outperform TMB and other known ICI response prediction biomarkers in both pan-cancer ICI objective response rates correlation and ICI clinical response prediction.

Essential revisions:

1) The results of Şenbabaoğlu should be cited more fully and their 18 gene APS compared to the 7 gene Şenbabaoğlu APM geneset. The antigen presenting set is all MHC class I. What is the reasoning behind not including MHC class II genes like DRB1, DRB2, CIITA?

2) TIGS should be compared to TIDE + TMB. Inflamed gene expression signatures have not been shown to be a highly predictive biomarker so I think that comparisons to interferon signatures will show superiority but not guide any advance in our thinking.

3) Multiple reviewers were perplexed by why high TIGs is associated with good outcome in some tumor types but poorer outcomes in other tumor types (Figure 3B). Expand the discussion here.

4) Improve the Cox regression analysis as suggested and make the definition of high or low marker expression consistent throughout.

5) The suggestion to apply the new analyses to many cancer types for ICI response prediction is limited by the available datasets that have all of the required information. The 3 datasets analyzed are what is available and these have been done.

6) Indicate the source or reference for their linear correlation formula – "objective response rate = 21.4 ×TIGS – 2.7, ".

7) If a patient has a beta2m mutation, is this captured by the APM signature and TIGS method?

Reviewer #1:

Identification of the biomarkers that predict which patients may benefit from immune checkpoint inhibition therapy is clinically important. In this study, Wang et al. developed a method named tumor immunogenicity score (TIGS) that combined tumor mutational burden (TMB) and antigen processing and presenting machinery gene expression signature to measure tumor immunogenicity. They found that TIGS could outperform TMB and other known ICI response prediction biomarkers in both pan-cancer ICI objective response rates correlation and ICI clinical response prediction. Thus, they proposed that TIGS is a potential tumor inherent biomarker for ICI response prediction. Overall, the study is novel and interesting. I list some of my concerns below.

1) The definition of high or low marker expression should be consistent throughout. For example, the authors defined patients with APS of first quartile as "APS-High", and those at the fourth quartile as "APS-Low". In contrast, they defined patients with TIGS above the median as "TIGS-high", and the remaining as "TIGS-low". Similar issues exist for the definition of TMB. Please make the correction and explain the rationale behind.

2) In Figure 3B, Cox regression analysis show that high TIGS is significantly associated with poor survival of patients in several types of malignancies such as adrenocortical carcinoma (HR=5.23, p=0.00105), Kidney Chromophobe (HR=89.9, p=0.01408), Thymoma (HR=8.22, p=0.00198)…etc. How to explain this phenomena given that TIGS reflects tumor immunogenicity and high TIGS predicts favorable prognosis in patients following immunotherapy.

3) In this study, the authors demonstrate an improved predictive power of TIGS in ICI clinical response when compared to TMB and other gene expression profiling based biomarkers, such as TIDE, IIS, IFNΓ. The authors should discuss the potential mechanisms underlying the superior performance of TIGS for immunotherapy clinical response prediction. The authors state "Furthermore, our linear correlation formula – objective response rate = 21.4 ×TIGS – 2.7, – can be used to.…". Please also indicate the source or reference for this formula.

Reviewer #2:

This well-written article describes a score, the Tumor Immunogenicity Score (TIGS) which combines tumor mutation burden (TMB) and a gene set score of 18 genes associated with Antigen Presentation Machinery (APM) score (APS). The 18 genes were described by Leone et al., 2013) and are PSMB5, PSMB6, PSMB7, PSMB8, PSMB9, PSMB10, TAP1, TAP2, ERAP1, ERAP2, CANX, CALR, PDIA3, TAPBP, B2M, HLA-A, HLA-B, and HLA-C. The author show that the TIGS (product of the natural log of TMB and the normalized APS) marginally outperforms TMB or APS in A) linear associated with Objective Response Rate (ORR), which is a rank order of tissue response to PD1 and PDL1 therapy and B) prediction of response in 2 tissue (Melanoma, Urothelial) in 3 studies (Van Allen, 2015, Hugo et al., 2016 and Snyder et al., 2017).

This article represents an extension to Şenbabaoğlu et al., 2016 which showed that a 7-gene APM signature of (HLA-A/B/C, B2M, TAP1, TAP2, and TAPBP), that is contained in the authors 18-gene signature was associated of immune infiltration, TMB, and ORR to immune therapy in kidney. Many of the figures presented by the author duplicate or extend that article.

Some of the figures of APM and APS are redundant with Şenbabaoğlu et al., and I would suggest that these should be moved to the supplement. Instead could the authors should provide a more in-depth discussion of the TIGS scores, IFN etc. Figure 1 should be moved to the supplement.

Are the APS results different to the 7-gene signature described by Şenbabaoğlu et al., There should be a comparison of the performance of the 7-gene Şenbabaoğlu and the 18-gene signature here.

Which cells (CIBERSORT scores) or subsets of the IIS scores are most associated with the APS scores.

The authors should compare their TIGS/APS to recent scores for immune presentation PHBR scores for MHC I and II (Marty et al., 2017 and 2018). https://www.cell.com/cell/pdf/S0092-8674(18)31109-7.pdf https://www.cell.com/cell/pdf/S0092-8674(17)31144-3.pdf

Does APS correlate with PHBR I alone or does it capture both PHBR scores for MHC class I and II? Does TIGS outperform a product of PHBR and TMB?

The authors recently stated that TMB is associated with gender (Wang et al., 2019b). What is the association between TIGS, APS and gender.

In the Introduction, some of the statements are over-generalized and do not reflect the complexity in defining good predictors of immunotherapy response. Whilst a correlation exists, TMB does not always predict response, neither does TIL. Some cancers (e.g. renal) with high immune infiltrate have poor response. Please edit the Introduction to reduce broad over simplifications or generalizations.

Reviewer #3:

Wang et al., describe a new computational method to identify responders for immune checkpoint inhibitors (ICI) using gene expression data from the TCGA database. The authors calculate a tumor immunogenicity score (TIGS) by combining tumor mutational burden (TMB) with antigen processing and presentation machinery (APM) gene signatures. They describe APM signatures across cancer types in TCGA and correlate APM with other gene expression pathways and immune cell infiltration across cancers. They next evaluate the ability of TIGS to predict response to ICI and show improved predictions using this method, compared to TMB alone, the TIDE method by Liu and colleagues, and several biomarkers (PDL1, CD8, etc.). This study is timely given the broad interest in predicting clinical responses to ICI therapy, and the concept of combining antigen presentation gene expression with TMB is also novel and interesting. However, the study is lacking in benchmarking data that support the use of the APM gene signature, and in comprehensive comparisons to prior gene signatures that also synergize with TMB in predicting immune response to ICI. It is also unclear whether the authors have evaluated the performance of prior gene signatures combined with TMB, compared to the TIGS method. Without these comparisons, it is difficult for the reader to truly evaluate the value added by this method, and I suspect will result in lower adoption of the method by the community.

1) A major premise of using antigen presentation gene scores is the presence of mutations in a subset of these genes in non-responder patients (i.e. Zaretsky et al., 2016). Therefore, the authors should determine whether their APM analysis is able to actually capture these defects in tumor samples. In other words, if a patient has a b2m mutation, is this captured by the APM signature and TIGS method? Are these instances the major driver of the value of APM analysis, or are changes in expression levels (without mutation or LOH) also predictive of response?

2) The authors have compared the performance of TIGS to several other prediction tools, however this analysis is not fully described, and I have several questions:

- The comparisons to TIDE are interesting. As I understand it, TIDE only takes into account gene expression, and not TMB. In contrast, TIGS takes into account gene expression (APM) and TMB. The authors should show the data for APM signature alone in several of the figures, for example in Figure 5A-C.

- The authors should also clarify in the main text whether TIDE incorporates TMB into their calculations, and if not, the authors should compare the performance of TIDE +TMB to TIGS.

- Similarly, for PDL1, IFNΓ, and CD8 scores, were these also combined with TMB? Or were they used in isolation to predict response (Figure 5)? The question is: what is the real value added – is it the APM score, or combining gene expression with TMB?

- If TIGS remains a better predictor of response compared to TIDE + TMB, the authors should describe in a main figure the performance comparison in all TCGA cancer types, rather than showing the comparison in 3 (2 that currently perform similarly, and 1 where TIGS outperforms). This information, in a main figure, is critical for the reader to understand the value of this new method across many cancers.

- Since APM genes are turned on by the IFN pathway (as the authors discuss), I would like to see more comprehensive comparisons to IFN pathway signature predictions, beyond only the 6 IFNΓ gene signature score taken from the Ayers et al. manuscript. In particular, I would like to see comparisons to the ISG.RS and IFNΓ.GS signatures described in Benci et al., 2019.

3) The authors correlate APM score with immune infiltration (using IIS and TIGER). Given the prior concerns regarding data normalization in the TIGER method (Newman et al., 2017), I would suggest adding an additional comparison using CIBERSORT. The correlation of APM and immune cell infiltration is independently interesting (without the prediction of response rates), and I think it would be useful to dig into this a bit more – i.e. which cell types correlate most with high APM scores?
