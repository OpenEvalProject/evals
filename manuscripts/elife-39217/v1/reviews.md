# Peer review - Round 1

Editors:
- Jeffrey Settleman, Calico Life Sciences United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.39217.038](https://doi.org/10.7554/eLife.39217.038)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Genetic determinants of cancer patient outcome" for consideration by eLife. Your article has been reviewed by Dr. Jeffrey Settleman as the Senior Editor, a Reviewing Editor, and three reviewers.

The reviewers have discussed the reviews with one another, and I have drafted this decision to help you prepare a revised submission. The reviewers feel that your paper should be accepted for publication after our concerns are addressed, either by performing additional analyses or by qualifying your findings in the writing.

Summary:

The manuscript by Sheltzer and coworkers "Genetic determinants of cancer patient outcome" provides an extensive evaluation of the prognostic information associated with frequent mutations and copy number alterations across multiple tumors from the TCGA and other validation sets. While overall the findings are intriguing, the reviewers have suggestions to correct gaps in this evaluation. If the authors can address the issues noted below however this could be a very interesting article.

We have the following suggestions to improve the manuscript.

1) The observation that copy number (CN) of driver genes and not mutations of the same genes associate with outcome is interesting and intriguing. However, the authors should clearly point out that their current analysis addresses whether CN of driver genes or mutations of various genes have inherent prognostic value in patients treated with standard chemotherapy regimens.

The authors need to state explicitly that their analysis does not address whether newer therapies targeted to inhibit specific activated oncoproteins (e.g. mutant EGFR in lung cancer) will ultimately have an important impact. This analysis must await adequate follow-up of patients treated with targeted drugs. The same caveat applies to oncogenes included in CN such as MDM2. Specific inhibitors may be especially active in these patients, but this will have to be addressed in future studies.

2) The authors should make some attempt to consider the impact of disease-specific mutations. For example, mutations occurring in >2% of patients are highlighted. However, EGFR mutations are more common in lung cancer than they are in other solid tumor types. I also note that specific variants known to influence function are not accounted for – noting EGFR as an example, there is no acknowledgment of exon 19 del or L858R mutations (as opposed to variants of unknown clinical significance). If these types of analyses are beyond the scope of what can be done in two months, the authors should clearly state that their paper is meant to highlight the role of CN in prognosis and acknowledge that disease- and mutation-specific analyses will be needed to assess the importance of mutations that activate specific oncoproteins in specific types of cancer.

3) Different statistical power for CN and mutations: perhaps the overall frequencies of mutations are too low and underpowered as compared to CN event frequencies (probably not the case for TP53 but for most other genes), thus explaining the lower number of statistically significant associations. In addition, a more meaningful comparison could be the hazards ratio from the Cox model, which would be independent of the number of samples with CN/mutations. Reporting z-scores (analogously to p-values) for the Cox regression is necessary to reject the null hypothesis but it would be informative to also provide hazards ratio and confidence interval for the Cox hazards regression (These data can be easily obtained from the R survival package Cox implementation even for continuous variables such as CN).

4) Gain/loss of function mutations and CN: From the data presented (Figure 3D) it is unclear whether gene focal CN and mutations overlap or tend to be mutually exclusive. A more exhaustive exploration of gain/loss of function through the directionality of prognostic associations would be desirable: It is interesting that TP53 shows significant and inverse association with survival in the METABRIC set (Figure 4J); that might be an expected behavior for tumor suppressor genes with loss of function mutations; As opposed to gain of function oncogene hot spots (BRAF600, RAS12, etc.), which should show positive, z-score for both CN and mutation. Is this directionality affecting the results presented in Figure 3D were EGFR shows loss of significance for the combined CN+ mutation bar? An oncoprint/table showing frequencies mutations overlaying CN would also be helpful to understand gain/loss of function events. Along these same lines, how do the authors know for sure which genes are the drivers within individual CN regions. Couldn't the affect on prognosis of some CN regions be based on the simultaneous loss or gain of function of two or more linked genes within a given region?

5) The approach to quantify aneuploidy (Taylor et al., 2018) didn't report any association with outcome in their original manuscript, despite previous literature reports (Kallioniemi et al., 1987; Kokal et al., 1986; Friedlander et al., 1984; Merkel and McGuire, 1990; Zimmerman et al., 1987) and only weak associations were found in this manuscript (Figure S10B). This measure of aneuploidy quantifies whole chromosome and whole arm numerical changes but doesn't account for focal events or other elements (i.e. structural variants) associated with chromosomal instability. As a consequence, the question of whether CN of driver genes carry prognostic information independently of overall chromosomal instability burden remains unanswered. The authors should be able to quantify the number of focal events per sample as an alternative measure of chromosomal instability and evaluate whether the prognostic capabilities of driver genes CN remain significant. Another measure of chromosomal instability could be the number of CN breakpoints (per Mbase) that can be obtained from segmentation data from TCGA samples.

6) Patient risk stratification is a highly complex, specialized and histology-type specific area of research. It would not be within the scope of this manuscript to review each tumor type strategy, however it would be useful if the authors could identify one or two real case scenarios in which their findings could potentially be integrated into clinical diagnostic practice (i.e., how MDM4 gain of copy number could be used to complement the Gleason score in predicting risk in prostate cancer).

The authors are also using outcomes data without providing definitions of how they were collected, though they do provide very detailed rationale for the choice of methods (Cox modeling in particular).

7) Copy number analysis is interesting but would benefit from a more in-depth look by disease type and perhaps by known oncogenic drivers within those cancer types. Pooling these data here may be missing critical signals within subsets. The need for further analysis by cancer type and histology should at least be acknowledged in the Discussion section if it cannot be completed within the timescale. Prognostic information based on gene or copy number depends to some extent on treatment. The authors should address the treatment that patients in this analysis received to the extent that they are able. Were any of the patients treated with modern day TKIs and immunotherapy?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Genetic determinants of cancer patient outcome" for further consideration at eLife. Your revised article has been favorably evaluated by Jeffrey Settleman (Senior Editor), a Reviewing Editor, and two reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

Can you please revise the Title to reflect more specifically the key conclusion regarding gene copy number information. Otherwise, it sounds like the title of a review article.

Reviewer #1:

The paper now meets my expectations and should be accepted as is.

Reviewer #3:

The authors thoroughly addressed the comments raised by reviewers and therefore my evaluation is positive and recommend for publication.
