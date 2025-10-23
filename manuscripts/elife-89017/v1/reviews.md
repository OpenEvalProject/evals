# Peer review - Round 1

Editors:
- Mark Linch

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.89017.3.sa0](https://doi.org/10.7554/eLife.89017.3.sa0)

This study presents a valuable finding on the association between DUX4 expression with features of immune evasion in human tissue and clinical outcomes in patients with advanced urothelial cancer. The evidence supporting the claims of the authors is convincing, using a range of corroborative statistical techniques. Compared to an earlier version, the quality of the manuscript has been enhanced, for example Figure 5 now illustrates the key features of survival probability estimates over time for patients assigned to with the test or training set.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.89017.3.sa1](https://doi.org/10.7554/eLife.89017.3.sa1)

Pineda et al investigate the association of the hypothesis that Dux4, an embryonic transcription factor, expression in tumor cells is associated with immune evasion and resistance to immunotherapy. They analyze existing cohorts of bulk RNAseq sequenced tumors across cancer types to identify Dux4 expression and association with survival. They find that Dux4 expression is detected in a higher proportion of metastatic tumors compared to primary tumors, is associated with decreased immune infiltrate and a variety of immune metrics and previously nominated immune signatures, and do an in depth evaluation of a cohort of metastatic urothelial cell carcinoma, finding that Dux4 expression is associated with a more immunodeficient tumor microenvironment (desert or excluded microenvironment) and worse survival in this aPDL1 treated cohort. They then find that Dux4 expression is a major independent predictor of survival in this cohort using different types of survival analyses (KM, Cox PH, and random survival forests). With prior existing biological data supporting the hypothesis (in prior work, the senior author has demonstrated Dux4 expression causally suppresses MHC-I expression in interferon-gamma treated cell lines), the current work links Dux4 expression with less immune activity in clinical tumor samples and with survival in ICI treated urothelial carcinomas, and demonstrates that Dux4 expression provides independent information towards survival including other molecular and clinical characteristics (TMB, ECOG PS as the other strongest markers), and provides interesting resolution on landmark analyses with TMB and Dux4 expression providing greater informativeness at later survival landmarks (e.g. 1 year and later), while ECOG PS has strong informativeness already at earlier time points. This work provides impetus towards more mechanistic and functional dissection of the mechanism of Dux4-associated changes with the tumor microenvironment (e.g. in vivo mouse studies) as well as potential interventional studies (e.g. Dux4 as a target in combination therapies). What the work does not provide is additional resolution on the mechanism of how Dux4 may be associated with a more immunodeficient microenvironment.

The conclusions are generally well supported, but there are issues that would benefit from clarification and extension:

- The finding that Dux4 expression is detected in a higher proportion of metastatic tumors and at higher levels compared to TCGA samples (Fig 1BC) is striking. However, at least for one tumor type (melanoma), the TCGA cohort is comprised of mostly locoregional metastatic (n=81 primary and 367 metastatic tumors in the PanCan Atlas). Since there are annotations for primary and (locoregional) metastatic samples in TCGA, an analysis of the primary vs. locoregional metastasis vs distant metastatic samples seems reasonable and likely informative. The analysis of tumors with matched FFPE and flash frozen samples with hybrid probe capture and polyA sequencing, respectively is a nice validation to show that the difference in Dux4 expression is not due to differences in preservation of starting material/sequencing in the metastatic samples vs TCGA samples (S1BC).

- The findings that Dux4 expression in the metastatic urothelial carcinoma setting is associated with a more immunodeficient microenvironment (Figure 2) is clear and unambiguous using multiple lines of data and analyses (bulk RNAseq, DUX4-positive vs DUX4-negative tumors, different immune cell and cytokine signatures; IHC showing an association with immune deserts and immune excluded phenotypes). However, this is an association and does not demonstrate causality.

- The survival analyses (Fig 3,4,5) show fairly convincingly that Dux4 provide independent predictive information beyond clinical variables and TMB towards survival in the aPDL1 treated metastatic urothelial carcinoma cohort. However, the choice to split the cohort into Dux4 negative (defined as < 0.25 TPM) and Dux4 positive (> 1 TPM) while excluding a large number of patients (n=126 pts) that fall in between has significant impact on the rigor of conclusions. This would benefit from showing all the data (e.g. including the 3rd group of in-betweens in the survival analyses as a separate group).

- The authors demonstrate that adding Dux4 to clinical markers and TMB results in an improved predictive model for survival, but there are a few questions regarding this model as a clinical biomarker

o Is Dux4 expression better than other correlated immune signatures/markers (e.g. interferon gamma, T effector signature, overall immune infiltrate) in providing additional information?

- The use of random survival forests to quantify the (predictive) marginal effect of Dux4+ vs Dux4- expression on survival in a non-parametric model as well as shed light on association with survival at different landmark times using Shapley values is quite interesting and well conducted.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.89017.3.sa2](https://doi.org/10.7554/eLife.89017.3.sa2)

Summary:

This article takes an expansive look at the potential role of DUX4 in cancer treatment and prognosis, including its correlation with other key biomarkers, the potential for cancer to be resistant to treatment, and risk prediction.

Strengths:

The primary strength of this work is the breadth of the analyses. The authors have linked DUX4 to not just one but multiple points in the trajectory of cancer, which increases the face validity of their conclusion that DUX4 is meaningfully related to the course of a cancer as well as the prognosis for a patient.

Statistically, the authors have taken care to properly validate their findings using appropriate bootstrapping and testing strategies.

Weaknesses:

Several weaknesses are noted. First, there is little-to-no description of the underlying sample population. It is only stated that "several large cohorts of patients with different metastatic cancers" were analyzed, and that a cohort of patients with advanced urothelial cancer was used for estimating associations with clinical outcomes. Lacking is information on the sampling mechanism, inclusion/exclusion criteria, treatment modalities, the definition of 'time = 0', the number of events observed, or even the sample size. Knowledge about the underlying study design would help explain some counterintuitive results, e.g. that the hazard of death among patients with Stage IV cancer is half that of those with Stage I cancer (Table 1); presumably this is not because Stage IV is actually protective but rather an artifact of the sampling scheme for these data. Second, the definition of negative versus positive DUX4 expression varies throughout the paper. In Figure 2B, Figure 3A, and Figure 3C, it is defined as >1 TPM vs. <= 1 TPM; in Figure 4A and Figure 5A, it is defined as >1 TPM vs. < 0.25 TPM; in Figure S1C it is partitioned into four groups, with boundaries defined at 0.25 TPM, 1 TPM, and 5 TPM. If categorization is needed, a rationale should be provided (ideally prospectively and not based upon the observed data, so as to avoid the perception of forking paths analyses), and it should be consistently applied. Third and finally, data seem to be occasionally excluded without rationale. For example, as mentioned above, the Cox model presented in Figure 4A seems to exclude all patients with DUX4 TPM between 0.25 and 1. Figure 3C excludes patients with TMB in the lowest quartile (although the decision was ostensibly to control for TMB confounding, there are more appropriate ways to do so that don't result in loss of data, e.g. a stratified KM plot). Excluding patients based upon a particular region of the covariate space makes interpreting the resulting model awkward.
