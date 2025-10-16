# Peer review - Round 1

Editors:
- YM Dennis Lo, https://ror.org/00t33hh48 The Chinese University of Hong Kong Hong Kong

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71035.sa0](https://doi.org/10.7554/eLife.71035.sa0)

This work has generated valuable data demonstrating the potential utility of serum RNA for lung cancer detection.


---

# Peer review - Round 1

Editors:
- YM Dennis Lo, https://ror.org/00t33hh48 The Chinese University of Hong Kong Hong Kong

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71035.sa1](https://doi.org/10.7554/eLife.71035.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Serum RNAs can predict lung cancer up to 10 years prior to diagnosis" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by Y M Dennis Lo as the Senior Editor/Reviewing Editor. The following individual involved in review of your submission has agreed to reveal their identity: Shenglin Huang (Reviewer #2).

The reviewers have seen each other's reviews, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. The analysis and result of serum RNA sequencing were not clearly presented. RNA sequencing with an average of 18 million reads per sample was performed. How about the mapped rate? Since the samples are long-term stored and may be at different times of collection, it is important that the sequencing results should be consisent. How about the sample correlations? In addition, why many of the RNA candidates (1137 of 3306) are isomiRs? They are derived from miRs, or degradation?

2. The authors showed that the candidate biomarkers were invovled in the cancer-related pathways. This result is somewhat overestimated because these RNAs are small RNAs and the KEGG pathway enrichment analysis is based on the targets.

3. A strength of this study is the large sample size from prediagnostic cases and a large control group from cancer-free individuals from the same cohort. The authors obtained RNA-seq data from 1061 serum samples. However, only samples from a total of 645 individuals with smoking history were analyzed. It would be helpful to include the samples without smoking to investigate the specificity of the potential biomarkers.

4. There are concerns regarding multiple samples from the same cancer subject. If samples from one subject go to both the training and testing set, there would be issues of overfitting. In the revision, the authors need to remove the duplicate samples from the analysis.

5. Calculate the relative risk for future cancer development for individuals with positive and negative test results.

6. Instead of using sliding windows of fixed duration, use windows of increasing duration.

7. Address the issue of over-fitting for the analysis from line 338 onwards.

8. The proposed use of the analysis (Figure 5 and the discussion) does not appear to be realistic. The authors need to calculate the percentage of subjects falling into the test positive and negative groups based on their analysis. Then, for each group, what percentage of subjects will eventually develop LC.

Reviewer #2:

This study by Umu et al., investigated the biomarker potential of serum RNAs for the early detection of lung cancer (LC) in smokers at different prediagnostic time intervals and histological subtypes. They observed that smokers later diagnosed with LC can be robustly separated from healthy controls by using machine learning models with serum RNAs profiles. This work demonstrated that serum RNAs could be promising prediagnostic biomarkers in a LC screening setting. This finding is interesting but not convincing because only one sample cohort was evaluated in current study and the datasets generated for this manuscript are not available. Also there are some concerns as follows.

1.The analysis and result of serum RNA sequencing were not clearly presented. RNA sequencing with an average of 18 million reads per sample was performed. How about the mapped rate? Since the samples are long-term stored and may be at different times of collection, it is important that the sequencing results should be consisent. How about the sample correlations? In addition, why many of the RNA candidates (1137 of 3306) are isomiRs? They are derived from miRs, or degradation?

2.The authors showed that the candidate biomarkers were invovled in the cancer-related pathways. This result is somewhat overestimated because these RNAs are small RNAs and the KEGG pathway enrichment analysis is based on the targets.

3.A strength of this study is the large sample size from prediagnostic cases and a large control group from cancer-free individuals from the same cohort. The authors obtained RNA-seq data from 1061 serum samples. However, only samples from a total of 645 individuals with smoking history were analyzed. It would be helpful to include the samples without smoking to investigate the specificity of the potential biomarkers.

Reviewer #3:

The authors analyzed archived serum samples which were collected before the development of lung cancer (LC) for different species of RNA.

They used machine learning to investigate if the combination of the RNA markers would be useful for the prediction of the future development of LC. In the machine learning analysis, they used 70% samples for training and 30% samples for testing. The process was repeated 5 times so that the samples can be assigned to both training and testing groups.

The strength of the study is that they include a large cohort of samples collected years before the development of LC.

The weaknesses of the study include

1. the questionable biological basis of this approach. As the samples were collected years before cancer diagnosis, the amount of tumor-derived RNA is expected to be very low. In this regard, the aberrations in serum RNA, if any, are likely to reflect the background risk of the body as a whole.

2. multiple samples from the same cancer subject. If samples from one subject go to both the training and testing set, there would be issues of overfitting. The authors would need to remove the duplicate samples from the analysis.

3. the low diagnostic performance. The sensitivity and specificity of the models were both around 70%. This would not be useful clinically. In fact, the use of relative risk for individuals with positive and negative test results would be more useful for predictive models.

4. The authors used a sliding window of fixed duration for the analysis. This analysis is counter-intuitive. If a marker is useful for predicting cancer at 3-5 years before cancer, what is the reason why it cannot predict cancers that occur within 3 years. It would be better to use windows with flexible size e.g. prediction of cancer in the next 2, then next 3, then next 5 years, etc.

5. For the analysis on lines 338 onwards, the authors further select features identified in the previous machine learning models for evaluation. What is the testing group in this analysis? Did they use all the samples without separating training and testing groups? If so, the over-fitting problem would be significant.

6. The. proposed use of the analysis (Figure 5 and the discussion) does not appear to be realistic. The authors need to calculate the percentage of subjects falling into the test positive and negative groups based on their analysis. Then, for each group, what percentage of subjects will eventually develop LC.

7. Remove duplicated samples from the LC group.

8. Calculate the relative risk for future cancer development for individuals with positive and negative test results.

9. Instead of using sliding windows of fixed duration, use windows of increasing duration.

10. Address the issue of over-fitting for the analysis from line 338 onwards.

11. To address the issue of clinical utility raised in point 6 in the previous section.
