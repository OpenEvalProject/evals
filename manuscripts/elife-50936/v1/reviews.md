# Peer review - Round 1

Editors:
- Wilbert Zwart, Netherlands Cancer Institute Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.50936.sa1](https://doi.org/10.7554/eLife.50936.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

As Prostate-Specific Antigen (PSA) testing in prostate cancer diagnostics suffers from high false-positive rates, a pressing unmet medical need presents to develop a sensitive and specific biomarker for prostate cancer diagnosis. The current work presents a flow-cytometry based approach to detect prostate cancer that may prove to be of high clinical value.

Decision letter after peer review:

Thank you for sending your article entitled "Identifying prostate cancer using Machine Learning of peripheral blood natural killer cell subset phenotyping data" for peer review at eLife. Your article is being evaluated by two peer reviewers, and the evaluation is being overseen by Reviewing Editor Wilbert Zwart and Eduardo Franco as the Senior Editor.

As you can appreciate from the detailed reviewer comments below, several important concerns were raised. The reviewers' unedited critiques are copied below.

Reviewer #1:

The authors present a machine-learning-based classification of 1) benign/prostate cancer patients and 2) high/low-risk patients. The authors used multiple machine learning algorithms (genetic algorithm and ensemble learning) and indicated their methods perform better than PSA-based classification.

Overall, though the key elements of the manuscript are machine learning and statistics, the description of both data and algorithms are mostly insufficient and poorly written. It is unclear why a particular algorithm is chosen, and how they are implemented. In particular, the genetic algorithm is typically an optimization algorithm, for which objective function needs to be defined. The genetic algorithm can be used for other problems (e.g., clustering) depends on how the objective function is designed. However, the authors just mention genetic algorithm as if this is a classification method, without defining an objective function. Also, the Ensemble learning algorithm takes multiple simple classification methods, but the choice of the simple classifier can vary and thus needs to be specified. In general, it is not clear if these complicated algorithms are really necessary, as the authors do not show the performance from the simpler classifier (i.e. weak classifier). Also, the text requires extensive re-writing. The text is jargon-rich (especially those related to machine learning), and often repetitive.

Specific comments:

1) Comparisons of the features between benign / prostate cancer patients are presented in figures and tables, but they are difficult to read. For instance, Figure 2 has two panels separated by the category (benign and cancer), but comparison per feature can be done if the authors simply put them side-by-side per feature in one boxplot. Also, per feature, a p-value from a simple t-test can help readers to understand if the features are different or not. Also, the authors should match the order of row/columns in Figure 4A and B.

2) It is unclear why the Ensemble learning is used. The authors should show if the simple classifier is sufficient to predict the outcome and then show if the performance improved by combining the simple classifiers.

3) It is not at all clear what genetic algorithm does. It completely depends on how objective function is chosen, and it is not defined in the text. Also, it is again unclear how the Genetic algorithm can perform feature selection.

4) The authors removed 3 patients with high-risk category (D'Amico High risk), but I do not understand why this is justifiable.

5) The authors discuss yet another Ensemble approach, namely the Random subspace dimension approach. However, the analysis is inconclusive and thus not clear why the authors brought this up.

6) It is not helping at all to mention the outcome without any data shown.

Reviewer #2:

This study extends their own research (Cosma et al., 2017) and tries to predict prostate cancer based on flow cytometric profiling of blood immune cell subsets. The computational algorithm is very straight forward. They first generate 32 features using flow cytometry. Then the genetic algorithm and statistical test is used for feature selection. The ensemble learning classifier is finally used with 10-fold cross validation for evaluation. Compared with their previous study, the technical difference is that they replace KNN classifier (used in the previous study) with the ensemble random subspace method used in this study. It is claimed that more patients are included in this study, and that peripheral blood NK cell phenotyping data is first-time used with computational modeling. As a computational scientist, I personally think that this study is limited in technical contribution. But I cannot fairly judge the contribution in medical domain. Overall the paper is well written and easily understood.

My major concerns are listed below:

1) Looks like that the authors first run the genetic algorithm and statistical test to select subsets of features using the whole patient data. They then run 10 fold-cross validation with selected features. Considering that the feature selection is performed on the whole data, the prediction performance might be boosted. The typical procedure is that feature selection is performed on training set during each folder of cross-validation. The selected features are then applied on the corresponding testing set. Under the current evaluation process, the authors are suggested to include more patients for independent testing. The newly testing patients should not be used for feature selection.

2) It is not justified or explained why all features are used to predict L/I risk caner vs H risk cancer on 54 patients, without using feature selection?

3) It is suggested to provide quantitative comparisons with their own study (Cosma et al., 2017) during the experiments. Thus it would be more technical convincing that the new method is better than the previous one.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your revised article "Identifying prostate cancer and its clinical risk using Machine Learning of blood NK cell subset phenotyping data" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Eduardo Franco as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Yongsoo Kim (Reviewer #1); Hongming Xu (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare another revised submission. We are happy to see the effort you and your co-authors made addressing the first round of reviews. However, our conclusion sis that additional work is needed.

As the editors have judged that your manuscript is of interest, but as described below that additional analyses are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Overall, the authors revised the manuscript and there is a significant improvement in clarity of technical discussion. In particular, the benefit of the ensemble k-nearest neighbor classifier is well-described in the new version of the manuscript, by comparing it with the weak classifier. However, both reviewers and the reviewing editor felt that a number of issues are not sufficiently addressed at this point, which would be required for the paper to be considered eligible for publication.

Essential revisions:

1).The authors mention the co-linearity issue and found a substantial proportion of features are correlated to each other (376 out of 496 feature pairs; also indicated in Figure 3) in Results paragraph two. The authors claim that the final predictor should not combine features with a high correlation. Are the features sets suggested by the authors (8 features from STAT+GA) indeed not correlated? In Figure 3, we can find a high positive or negative correlation among 15th-18th features. And in statistical analysis, the 14th-18th features are statistically significant (in Table 2), which might correspond to the highly correlated features. If that is the case, it sounds like the authors did something they should not do, according to their own opinion. Please address this.

2) The authors chose λ=4 after examining the stability of GA. I do agree that stability is an important aspect. However, I think it is also important to know how good the performance of the final solution found by GA is. In that regard, it is worth reporting the final mutual information next to the Relative Frequency in Table 3.

3) The authors used the Random subspace dimension approach, which is the best performing. The authors did not present any data to support the claim. This should be provided.

4) The authors claimed that they demonstrated all of 32 features are required. However, the performance of the algorithm needs to be assessed with subsets of the features to make the claim.

5) In the revised version, overall, the authors have tried to address and answer the concerns I listed before. Because of difficulty and time-requirement for collecting more data, only cross-validation was performed in this study. External testing for the presented method is hard for current situation now. So it is suggested to mention this limitation in the paper's discussion part.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your revised article "Identifying prostate cancer and its clinical risk using Machine Learning of blood NK cell subset phenotyping data" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Yongsoo Kim (Reviewer #1); Hongming Xu (Reviewer #2).

We are happy to see the effort you made at amending the paper to accommodate the concerns and suggestions from the reviewers. Once again, we are unable to accept it in its present form for publication. However, we are willing to consider a new revised version if you can address the additional concerns and suggestions below. The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The authors have addressed the vast majority of issues raised, and all reviewers are in general satisfied with the revised work. One final question that remained unanswered in the previous round would still require attention at this stage.

Major comments

1) My main concern is still the Revision#4 question, which was asked in the second round review. In the experiments of predicting low/intermediate risk cancer vs high risk cancer, the authors used all 32 features to train the ensemble model by arguing due to the small dataset. But usually if the dataset is small, it is better to use a smaller number of features. In the experiments of benign disease and prostate cancer distinction, the author claimed that 8 features selected by GA+STAT provided the best performance. So it is still suggested to use those 8 features for L/I vs high risk distinction. If using those 8 features cannot provide better performance, the authors can provide some insight discussions about this phenomenon. In addition, for the distinction between L/I and H cancer, 16 more high risk cancer patients were included. Are there any reasons why these 16 patients were not used for cancer and benign distinction?
