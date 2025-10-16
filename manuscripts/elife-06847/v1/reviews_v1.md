# Peer review - Round 1

Editors:
- Chi Van Dang, University of Pennsylvania , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.06847.002](https://doi.org/10.7554/eLife.06847.002)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Registered report: Discovery and preclinical validation of drug indications using compendia of public gene expression data” for consideration at eLife. Your article has been favorably evaluated by Stylianos Antonarakis (Senior editor), Chi Dang (Reviewing editor), and 3 reviewers, one of whom is a biostatistician.

The Reviewing editor and the reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

In this study, the authors propose a study to reproduce the findings reported in Figure 4C/D and Supplementary Figure 1 from a previously published manuscript (Sirota et al. Sci Trans Med, 2010), which aimed at assessing the ability to predict drug repurposing opportunities based on connectivity map data analysis. Specifically, the previous Sci Trans Med paper reports that cimetidine, a histamine-2 (H2) receptor agonist commonly used to treat peptic ulcers, can diminish lung cancer tumorigenesis in vivo. There are several key concerns about the design of the study. The first concern is about the duration of the experiment and statistical analysis, and the second about conclusions drawn from using only one lung cancer cell line.

1) At the beginning of the Materials and methods section: The authors plan to follow the mice for 11 days instead of 12 days. Is there a good reason to follow the mice one day short? In addition, the experiment contains five cohorts. Among the five cohorts, cohort 2 only has 5 mice while the other 4 cohorts have 14 mice. Please justify.

2) Power calculation was based on t-test. It is suggested that the authors use two-tailed unequal variance t-test if normality is not violated or the use of Wilcoxon rank-sum test if normality is violated. The authors propose the use of two-way ANOVA followed by t-test for analyzing tumor weight data (in the subsection headed “Confirmatory analysis plan”). Please make sure that the data do not violate the assumptions of ANOVA: normality and homoscedasiticity. If the data do not fit the assumptions well enough, please try to find a data transformation that makes them fit. If this doesn't work, please apply a nonparametric counterpart of ANOVA such as Kruskal–Wallis test. In addition, I suggest the use of contrast within the ANOVA framework instead of t-test if the assumptions of ANOVA are met.

3) To compare growth curves of tumors, the authors propose ANCOVA followed by Bonferroni corrected t-test. Please make sure that the data do not violate the assumptions of ANCOVA and perform transformation or use non-parametric ANCOVA if needed.

4) For the additional comparison of PBS-treated A459 tumors to Doxorubicin treated tumors (in the subsection headed “Confirmatory analysis plan” and in the subsection headed “Test family”), I suggest the use of two-tailed unequal variance t-test instead of t-test if normality is not violated or the use of Wilcoxon rank-sum test if normality is violated.

5) Although the reproducibility project is aimed toward reproducing previously published results, the reviewers would like for the authors to address the limitation of drawing conclusions for the use of only one cell line, A549. Specifically, activity of drugs in cell lines and xenografts is generally highly idiosyncratic. As a result, most journals require that any in vitro and in vivo experiments are replicated in multiple cell lines and in vivo models.
