# Peer review - Round 1

Editors:
- Maureen Murphy, The Wistar Institute United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.44310.045](https://doi.org/10.7554/eLife.44310.045)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "A four-DNA methylation biomarker predicts survival of patients with cutaneous melanoma" for consideration by eLife. Your article has been reviewed by 3 peer reviewers and the evaluation has been overseen by a Reviewing Editor and Maarten van Lohuizen as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In the current manuscript, Guo et al. use published data on cutaneous melanoma including DNA methylation status to develop a 4-DNA methylation biomarker that is predictive of overall survival based on historical case data.

Significant points:

1) The identification of a novel epigenetic four-DNA methylation signature that can successfully stratify patients into high- and low-risk groups, with AUC estimates exceeding 0.80 and 0.75 in training and validation cohorts.

2) Confirmation of the prognostic value of this signature in an independent (though smaller) cohort.

3) The finding that the four-DNA methylation signature was effective in distinguishing the high-risk patients from low-risk patients, independent of clinical parameters like Breslow thickness.

4) The finding that the 4-gene methylation signature is inversely correlated with expression of immune-checkpoint genes.

Essential revisions:

1) Absence of functional data: Does the methylation pattern of the 4 genes correlate with the expression of these genes? The authors are encouraged to analyze RNA Seq data from TCGA to address this issue. This issue is important because if methylation correlates with expression, then these four genes may (also) be important therapeutic targets. More specific questions to address at a basic level – Are the genes at/near the methylation sites expressed in melanomas at the RNA or protein level? Does expression (in at least a subset or other dataset) correlate with the methylation status at the loci? Some plausible roles for the genes GBP5, RAB37, etc. are offered in the discussion, but some functional analysis of these genes or the pathways hypothesized to be affected (as described in the Discussion) would substantially increase the degree to which this study could move the field forward.

2) Questions about the analysis: The authors should carefully control for clinical features from the very beginning of their analysis rather than estimating that clinical features seem to not have an effect on their predictor after the model is fully built. It is hard to evaluate and interpret any intermediate findings (are they driven by clinical biases or actual signal in methylation data?). Specifically: was univariate analysis in the training cohort adjusted for age, tumor stage/grade and tumor tissue site? To perform a search for markers independent from clinical features it seems to be critical to adjust for clinical differences first. Will this change marker selection for prediction model? The authors should introduce a comparison with known melanoma methylation signals in (e.g. MITF region, etc.) as a positive control for their model. Interestingly, they do cite and use the data from M. Lauss et al. who found the MITF signal, but never check whether their predictor-building approach captures the same signal.

Also: subsection “Statistical analysis”. "The univariate Cox proportional hazard analysis was first conducted in the training cohort to identify methylation markers significantly (P < 0.001) associated with patient survival."

How was the significance level was determined? According to the manuscript 461 samples with 485,577 DNA methylation sites were analyzed. Most-widely used Bonferroni correction (might be too aggressive cutoff, I am not insisting on using this particular one) should result in P < 0.05 / 485,577 ~ 1x10-7. Subsection “Derivation of prognostic DNA methylation markers from the training cohort”: 4,454 markers were included into the multivariate regression analysis (above comment on significance level determination applies).

3) Validation: The four-DNA methylation signature "beats" the other biomarkers in Supplementary file 2/Figure 4A-C. Data may not be available for all of these studies, but for those based on DNA methylation, how does the four-DNA signature compare to the datasets used to generate other methylation predictive markers (Supplementary file 2 17-DNA methylation, CTLA-4, etc.)? Presumably these had validation datasets as well (it seems unfair to expect the four-DNA signature of this study to "beat" the training set for another marker, but other validation sets should be a reasonable comparator). The authors did include a comparison using their validation set, but additional validation datasets would strengthen the generalizability of their biomarker/signature.

4) It would be helpful to include a supplemental figure/panel illustrating distribution of the 4-site methylation risk predictor score value for the TCGA melanoma cohort and then plot the threshold dividing "low-risk" and "high-risk" groups (median). Subsequently, the Figure 3 (main text) and supplementary figure legends need to be explained better (e.g. in Figure 3A "low-risk (28/69)" what does (28/69) mean? I seem to be unable to find this in the text or figure caption.)

5) One additional panel in Figure 1 (or supplement) might be helpful: principal component analysis plot using methylation values at 4 selected biomarkers that illustrates separation between "high" and "low" survival groups. This should clearly illustrate direct effect of methylation level on survival differences.

6) Subsection “Association of the four-DNA methylation signature with ICB immunotherapy-related signature”: "significantly negatively correlated with PD-1, PD-L1, PD-L2, CTLA-4 (P < 0.05 [..,]". Multiple hypothesis testing significance adjustment should be considered. Based on Figure 4D – 4-meth signature correlation was estimated against 7 other signatures (or 6 if GBP5-meth is considered a part of 4-meth), thus significance should be determined using P-value threshold P < 0.05/7 (if Bonferroni correction is used). Please, report raw p-values for this analysis in the supplement.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A four-DNA methylation biomarker is a superior predictor of survival of patients with cutaneous melanoma" for further consideration at eLife. Your revised article has been favorably evaluated by Maarten van Lohuizen (Senior Editor), a Reviewing Editor, and three reviewers.

The manuscript has been improved but there are some minor remaining issues that need to be addressed before acceptance, as outlined below:

The reviewers appreciate the effort made by the authors to address their concerns. The result is a strengthened manuscript.

1) Without another validation dataset (major point #3), the generalizability of the results will remain a potential weakness but publishing this study with this caveat noted in the text/discussion is of value.

It is recommended that the authors mention this, for example by adding the following sentence to the end of the third paragraph of the Discussion section: When further samples become available it will be important to analyze this methylation signature in another validation dataset.

2) The DNA variant in intron of OCA2 has been found to have a protective effect in melanoma GWAS (rs4778138, β = -0.18, PMID: 26237428). The authors state that cg18456782 (OCA2) marker "had positive coefficients, indicating a correlation between higher DNA methylation level and shorter overall survival". If one looks at the TCGA survival data and separates melanoma patients by median OCA2 expression, there is a significant differential survival (p~1e-5) with low expression favoring better survival. This is consistent with the presented data and suggests that while in GWAS the OCA2 variant has been found having a protective function, survival and expression data suggests a risk pattern for OCA2 gene.

Discussing this in the Discussion section would strengthen the manuscript because there is no sufficient experimental data on OCA2.

3) Prior to the analysis the training cohort was not adjusted for clinical parameters like age, tumor stage/grade and tumor tissue site; the authors have explained how they controlled for this, but this fact should be mentioned in the Discussion section so that results could be interpreted with the appropriate caution.

4) The Abstract should be modified as follows:

Cutaneous melanoma (CM) is a life-threatening form of skin cancer. Prognosticbiomarkers can reliably stratify patients at initial melanoma diagnosis according to risk, and may inform clinical decisions. Here, we performed a retrospective, cohort-based study analyzing genome-wide DNA methylation of 461 patients with CM from the TCGA database. Cox regression analyses were conducted to establish a four-DNA methylation signature that was significantly associated with the overall survival (OS) of patients with CM, and that was validated in an independent cohort. Corresponding Kaplan-Meier analysis displayed a distinct separation in OS. The ROC analysis confirmed that the predictive signature performed well. Notably, this signature exhibited much higher predictive accuracy in comparison with known biomarkers. This signature was significantly correlated with immune checkpoint blockade (ICB) immunotherapy-related signatures, and may have potential as a guide for measures of responsiveness to ICB immunotherapy.
