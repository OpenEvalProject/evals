# Peer review - Round 1

Editors:
- Vadim N Gladyshev, Brigham and Women's Hospital, Harvard Medical School United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.37462.014](https://doi.org/10.7554/eLife.37462.014)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Epigenetic Age-Predictor for Mice based on Three CpG Sites" for consideration by eLife. Your article has been reviewed by three peer reviewers and the evaluation has been overseen by a Reviewing Editor and Jessica Tyler as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. We consider this work more appropriate in the category of a Tools and Resources paper rather than as a Research Article.

Summary:

The submitted study presents a new methylation clock for mouse blood based on analysis of only three CpG sites. This seems to be a useful and practical tool, as previous studies produced accurate methylation clocks based on ~100 sites. The training set included 24 blood samples obtained from C57BL/6 mice representing 12 age groups ranging from 11 to 117 week old. Although the number of samples is not large, fair representation of age groups seems to make the clock usable across ages. The authors focused on 9 genomic regions enriched in age-associated sites obtained from previous studies. Three individual sites with the highest correlation with the training set were then selected, and the clock was built based on a simple multivariate linear model. The validation set included 21 mice from the same site (University of Ulm) and 19 mice from a different site (University of Groningen). Precision of the clock was equal to MAE = 3.6 weeks for the training set and MAE = 5 and MAE = 5.9 weeks for validation sets. This is comparable with the available clocks produced by other methods. The new clock was applied to 25 samples of DBA/2 mice having a shorter lifespan. The clock showed a higher age for these short-lived mice compared to C57BL/6 mice of the same chronological age.

Essential revisions:

1) Methods used for site selection are not completely clear. The authors explain their selection by choosing the sites with maximal correlation with age. However, first, it's not clear why exactly three sites were chosen. Second, selection of sites with maximal individual correlation doesn't guarantee that the multivariate model based on these sites would result in highest precision. To make site selection more convincing, you may apply a machine learning approach (linear model with L1 regularization) to the whole set of sites (all sites from 9 genomic regions) and vary the regularization parameter to obtain models with different numbers of sites. Then, these models can be applied to the validation set 1, and precision can be calculated. In this case, you could show how precision changes with the number of sites (the number of remaining sites in the model on the x axis and precision (R2 or MAE) on the y axis). This will tell how much precision you lose when proceeding to the model with fewer sites. Based on this plot, you could select the model with the optimal number of sites (minimal number of sites that provides precision, which doesn't significantly increase with the addition of additional sites). And then apply it to the validation set 2 to get the unbiased estimate of precision. This approach could make the analysis much more convincing and also explain the choice of the number of sites.

2) R2 is shown for every training and validation set as a metric of quality. However, in the text it is explained as Spearman correlation. This complicates interpretation of the results as usually the ratio of explained variance is denoted by R2, which is equal to the square of Pearson correlation, but not to the Spearman correlation. Please, either change the symbol you use (for example, correlation coefficient is usually denoted as ρ), or explain the R2 in the text (for example, specify that this is Spearman correlation squared).

3) You didn't specify the number of age groups used for the development of the clock. From the figure, it seems 12 age groups were used. We recommend adding this information to the text as it supports the analysis (12 age groups is a broad range that makes the results more convincing).

4) Comparison of age prediction for C57BL/6 and DBA/2 mice is questionable. DBA/2 samples represent a narrow range of ages, which includes almost no young mice (based on the figure it appears that only 4 samples represent mice <75 weeks old). This reduces quality of the analysis, as nonlinear behavior is often observed in the old ages, which can partly explain the difference between the ages predicted for C57BL/6 and DBA/2 mice. Development of the clock for DBA/2 samples is even more dependent on the age range. Therefore, quality of the clock built for DBA/2 does not look reliable. Additional samples of young DBA/2 mice could improve quality of the findings. Alternatively, this drawback should be clearly noted in the text and text revised accordingly.

5) In the Abstract, you state "DBA/2J mice revealed accelerated epigenetic aging as compared to C57BL6 mice" In fact, Figure 2 appears to show that the DBA/2 mice are about "40 weeks older" at every age – there is barely any age-associated divergence of the predicted aged for DBA/2 and C57BL/6. In other words, it does not seem as if the DBA/2 are aging faster. Rather, they appear to be born older and remain so throughout life. This is perhaps best explained by a need for re-calibrating the clock in different strains of mice. Figure 4E appears to confirm this. So, we agree with the authors conclusion that "age-predictors should be adjusted for different inbred mice strains" but do not agree that "DBA/2J mice revealed accelerated epigenetic aging as compared to C57BL6 mice."

6) You didn't specify if both training and validation sets or only validation sets of C57BL/6 mice were used when the predicted age was compared between this strain and DBA/2. To make the analysis unbiased from the construction of the clock, only validation sets should be used there. Based on the figure, it seems this was indeed the case, but anyway it should be specified in the text as this is important from the methodological point of view.

7) There is far too much emphasis placed on age prediction. Ultimately, the residual or difference between chronological and epigenetic age is of the most interest. The goal is not to develop near perfect age predictors. In humans, the clocks with the strongest age predictions typically do not contribute the most to differential risk of aging-related conditions, which should be the goal. This point can be addressed by revision of the text.

8) Is this new measure specific to blood? Were any experiments done to validate it in any other tissue or in sorted cells? It is possible that changes in methylation may be confounded by blood cell composition, etc. If it is not possible to address it experimentally within the revision timeframe, it should at the very least be discussed as a limitation.

9) Epigenetic measures in mice will only be useful if (a) they track difference in lifespan/healthspan both between and within strains, and (b) they show response to intervention. We feel like the utility of this clock is being over-sold prior to the necessary validations being shown.

10) "These results provide further evidence that age-associated DNAm is generally rather related to biological age […]" is an overstatement. If the DBA/2J mice are not aging epigenetically, there is little data in this manuscript to support the idea that the epigenetic clock is a measure of biological age as opposed to chronological age. The clock that the authors have reported here was calibrated vs. chronological age and appears to function well as such. However, there is no direct evidence that it reports on biological age.
