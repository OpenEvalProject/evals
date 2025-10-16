# Peer review - Round 1

Editors:
- Y M Dennis Lo, The Chinese University of Hong Kong Hong Kong

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68758.sa1](https://doi.org/10.7554/eLife.68758.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript describes the use of infrared molecular fingerprinting for the detection of multiple types of cancer. The spectral differences between different cancer types have further expanded the diagnostic potential. This work has laid the foundation for future developments in this area.

Decision letter after peer review:

Thank you for submitting your article "Infrared molecular fingerprinting of blood-based liquid biopsies for the detection of cancer" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by myself as a Reviewing Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. The paper would benefit from further transparency on the numbers of patients used in the analysis. The authors state that they collected blood (serum and plasma) from 1927 individuals with cancer, symptomatic controls and healthy controls in the abstract. In depth reading and analysis of the paper shows that this dataset is then reduced to 1611 and that plasma samples are only available from a subset of lung and prostate cohorts. They should also explain why 316 patients were removed from the dataset. Further analysis of the supplementary highlights that some discriminations are performed with only 28 samples per disease type for instance the multi cancer discrimination in the female group between bladder, lung and breast and in the male group between bladder lung and prostate there are only 90 per group. As a major claim of the paper is the fact that the authors can distinguish between these types of tumours and that the signatures are significantly different enough a discussion on whether the size of the dataset analysed is sufficient to have that conclusion should be presented. Also the major class within the dataset analysed is the number of subjects with no related conditions (n=635) so essentially the non-symptomatic healthy controls. As the authors in the introduction highlight the fact that there is a need to adequately apply machine learning tools with involvement of a sufficient number of samples and they state that they address this in this paper they should highlight the number of samples involved in each of the analysis they perform or at least discuss the weaknesses that arise. This issue of low sample numbers is an issue in the field and the authors are correct to highlight this in the introduction. The authors state that a power calculation has been performed and is available on request. This should be provided with the paper to show that 28 samples per disease state achieves the required level of significance.

2. The authors utilise an unsupervised PCA based approach to show that there is no difference between the collection sites in supplementary figure 1. However, from experience it is known that a PCA would not show discrimination between the cancers that the authors have analysed. This may be one explanation as to why the authors needed to use an SVM in order to enable the discrimination of the tumour types. To properly enable this conclusion the authors could show the PCA (along with loadings and not just score plots) for the tumour types or perform an SVM on the samples from the three collection sites in order to fully support this conclusion.

3. The authors also state that the pre-processing of the IMFs did not affect the classification result indicating high quality raw data. In order to not mislead a reader is should be noted that what the authors refer to as raw data is not raw data. It is in fact the spectra after a water correction has been performed to correct for negative absorptions. From knowledge the negative absorptions are variable between spectra and it would be interesting for the reader to have a discussion on how often negative absorptions appear in the liquid serum or plasma. Fundamentally the spectra referred to by the authors for subsequent normalisation or 2nd derivatisation have had a correction performed and a such are not raw. In order to fully support this conclusion, it would be interesting to see the impact on the classification accuracy of the raw spectra (the spectra to which the negative absorption has not been applied)

4. Please further expand on what is meant by quality control serum sample – as there a particular serum used for this and what was the procedure for proving quality – do you have a quality test and did any fail at any point?

5. One key objective the study aims to achieve is to improve the specificity of the study by including more suitable control subjects. However, the study still fails to identify which parts of the signal were directly related to the existence of cancer-related molecules. It would be useful for the authors to try to dissect out the most representative cancer signals and to identify the molecules giving rise to those signals.

6. The authors used AUC of ROC curves to reflect the clinical utility of the test. However, for evaluating the usefulness of diagnostic markers, the sensitivities at a specificity of 95% and/or 99% (for screening markers) are frequently used. The presentation of these data would be useful to indicate if the test would be useful in clinical settings.

7. The authors showed that the ROC curves for plasma and serum had similar AUC and concluded that they provided similar infrared information. This point is incorrect. To prove that both plasma and serum can reflect signals from the cancer, the authors need to show that the actual infrared pattern from the plasma and serum are identical.

8. In the discussion, the authors need to discuss:

i. if the current performance of the test is sufficient for clinical use, and how that can assist in the clinical decision process;

ii. how the performance of the test can be improved.

(Merely increasing in the number of test/control subjects is unlikely to lead to a dramatic improvement in the accuracy which makes the test clinically useful.)

Reviewer #1:

The authors carried out a multi-center trial to evaluate the potential clinical use of infrared molecular fingerprinting (IMF) for detecting cancer signatures in the blood. In previous proof-of-principle studies, only small numbers of samples were analyzed and that would be subjected to bias related to preanalytical factors and the demographic difference between the cancer patients and control group.

This study performed a one-to-one match of the cancer patients and the controls, and also included symptomatic subjects with benign conditions as controls. This could much better reflect the clinical utility of the test in a real-world situation.

As the study used machine learning to identify the patterns associated with cancer in blood, it did not dissect out which parts of the signal are from the cancer and which are the baseline from the blood cells or other tissue organs. It is expected that the amounts of proteins and DNA from the cancer only constitute a small proportion, most of the signals detected are not from the cancer itself. Hence, this method is still subject to biases related to factors unrelated to cancer, e.g. inflammation. Future studies that involve even larger numbers of controls with a wider variety of benign conditions would be needed to confirm the specificity of the cancer patterns.

The authors used AUC of ROC curves to demonstrate the clinical utility of the test. The sensitivity and specificity of the test are still inadequate in this early version of the test.

This study is a good example of how the evaluation of liquid biopsy tests based on pattern recognition could be performed.

Reviewer #2:

The authors set out to achieve a multi institutional study of serum and plasma based IR analysis in order to determine if they could distinguish between breast, bladder, prostate and lung cancer. They have shown an interesting method that can discriminate between disease and symptomatic controls and have provide a good assessment that will surely be useful within the field.

The paper would however benefit from further transparency on the numbers of patients used in the analysis. The authors state that they collected blood (serum and plasma) from 1927 individuals with cancer, symptomatic controls and healthy controls in the abstract. In depth reading and analysis of the paper shows that this dataset is then reduced to 1611 and that plasma samples are only available from a subset of lung and prostate cohorts. They should also publish why there was removal of 316 patients from the dataset. Further analysis of the supplementary highlights that some discriminations are performed with only 28 samples per disease type for instance the multi cancer discrimination in the female group between bladder, lung and breast and in the male group between bladder lung and prostate there are only 90 per group. As a major claim of the paper is the fact that the authors can distinguish between these types of tumours and that the signatures are significantly different enough a discussion on whether the size of the dataset analysed is sufficient to have that conclusion should be presented. Also the major class within the dataset analysed is the number of subjects with no related conditions (n=635) so essentially the non-symptomatic healthy controls. As the authors in the introduction highlight the fact that there is a need to adequately apply machine learning tools with involvement of a sufficient number of samples and they state that they address this in this paper they should highlight the number of samples involved in each of the analysis they perform or at least discuss the weaknesses that arise. This issue of low sample numbers is an issue in the field and the authors are correct to highlight this in the introduction. The authors state that a power calculation has been performed and is available on request. This should be provided with the paper to show that 28 samples per disease state achieves the required level of significance.

The authors utilise an unsupervised PCA based approach to show that there is no difference between the collection sites in supplementary figure 1. However, from experience it is known that a PCA would not show discrimination between the cancers that the authors have analysed. Which is most likely why the authors needed to use an SVM in order to enable the discrimination of the tumour types. To properly enable this conclusion the authors could show the PCA (along with loadings and not just score plots) for the tumour types or perform an SVM on the samples from the three collection sites in order to fully support this conclusion.

The authors also state that the pre-processing of the IMFs did not affect the classification result indicating high quality raw data. In order to not mislead a reader is should be noted that what the authors refer to as raw data is not raw data. It is in fact the spectra after a water correction has been performed to correct for negative absorptions. From knowledge the negative absorptions are variable between spectra and it would be interesting for the reader to have a discussion on how often negative absorptions appear in the liquid serum or plasma. Fundamentally the spectra referred to by the authors for subsequent normalisation or 2nd derivatisation have had a correction performed and a such are not raw. In order to fully support this conclusion, it would be interesting to see the impact on the classification accuracy of the raw spectra (the spectra to which the negative absorption has not been applied)

The strongest aspect of this paper in my opinion is the comparison of lung cancer with common symptomatic diseases such as COPD. There has often been a question within FTIR based clinical spectroscopy of the specificity of the technique with other diseases that are similar in symptomology and that could potentially impact the outcome. The authors have shown this particular discrimination to a substantial level (n = 115 vs 118) which is significant. However it should also be noted that there is a substantial body of work on the use of FTIR on sputum that has shown the ability to differentiate between chronic lung diseases.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Infrared molecular fingerprinting of blood-based liquid biopsies for the detection of cancer" for further consideration by eLife. Your revised article has been evaluated by Y M Dennis Lo as Senior Editor and Reviewing Editor, and by the original two reviewers.

As can be seen below, Reviewer #2 has serious concerns about this revised manuscript.

Reviewer #1:

The authors have adequately addressed all the concerns I raised in the previous review.

Reviewer #2:

I thank the authors for their response, but I now have serious reservations over the paper

The paper in the author’s own words has had the statements weakened and they have removed references to "high-quality" data and as such I do not think it is of sufficient enough novelty and power for eLife. In addition there remains confusion over the actual number of samples that have been used.

1. There is still confusion over the numbers used – the authors state 1927, 1611 and 1637 samples. individuals. They only analyse or present 1611 individuals and then when I add up all the numbers in each of the groups in Table 1 supplementary it comes to 2150 so I am clearly confused as to where the samples have come from. I am sorry I my additions are incorrect but really this should be simple and accessible for the reader.

2. The authors have only matched their 200 cases vs 200 cases in 4 out of 64 of the classification they are doing in the entire manuscript and still it seems misleading that they have stated that they have done one. The manuscript overwhelmingly has more non powered classifications than powered ones

3. The authors conclude that the response is related to tumour volume but from looking at figure 5 all of the values are within the error bar of the previous T stage – can the authors comment on this

4. I do not understand why the authors are not including the information on point 2 within the paper – it is not enough to state that it is for review purposes only. This should go in the paper and not be hidden from the public – if the paper is accepted. Do the authors have a reason why they do not want to include this in the paper.

5. In response to point 4 there is quite a spread of the values in the scores plot that authors present, again just for review, the authors need to state the percent variance within this PCA and show the loadings for accurate analysis. Interestingly that this quality control procedure doesn't account for differences between collection sites – as this procedure and the analysis seems to be performed solely at one site and not at the three collection sites this points to an issue in the collection of the samples from different sites that enable to large differences to be observed that is presented in the table on Point 2 – can the authors explain this further – did they have issues with collection differences that are now coming through in the AUC differences between sites only when question by the reviewers?

6. In reference to point 6 in the response to reviews please can the authors comment on the sensitivity values – these are simply stated an don't discussed in the text at all

7. In table 1 why do the authors not compare breast and bladder cancer with SR or MR and instead only state the results for what is reasonably healthy people

8. The authors state if they have 200 versus 200 they have an AUC accuracy within a 0.054 bound on error. Yet at multiple points throughout the paper there error bound is less than 0.054 and they haven't provided the error on most of the classification that are within the 3 x 3 square confusion matrices in the figures

9. From reading this paper I do not think the authors have an independent blind test – the way it was presented first time I didn't pick up on this – please can the authors simply state how they validated the approach. What I would expect is to have a set of patients that is used for train the algorithm and then a completely independent set of patients as a blinded (algorithm blinded at least but hopefully operator blinded) set to prove that the signatures are valid – it seems like the authors have not blind tested the dataset?

Overall the authors have raised some serious concerns on the approach to their methodology by the clarifications provided. They state they have weakened the paper and removed high quality references. They don't want to publish the items performed for review along with the paper and these items raise significant questions about what is the impact of the quality test and even if the collection procedure of the samples is correct and it is also unclear if the classifications have been substantially tested by blinded analysis or if this is simply the results from training the model without testing
