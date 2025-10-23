# Peer review - Round 1

Editors:
- Hristo Dimitrov, https://ror.org/013meh722 University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.86132.sa0](https://doi.org/10.7554/eLife.86132.sa0)

This study presents a valuable dataset and tool that can aid in arthropathies' assessment, potentially enabling such evaluation to be done outside the lab. There is convincing evidence supporting the comparison between the force plate and insole data but the evidence for distinguishing disease signatures is inconclusive and would need further development. This work will be of interest to physical therapists, clinicians, and researchers in the field of lower limb joint diseases.


---

# Peer review - Round 1

Editors:
- Hristo Dimitrov, https://ror.org/013meh722 University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.86132.sa1](https://doi.org/10.7554/eLife.86132.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Analysis of a digital insole versus clinical standard gait assessments in participants with knee arthropathy and health controls: development of a machine learning model" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Tamar Makin as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. We kindly request your attention to the following essential revisions. Additionally, we would greatly appreciate it if you could review the complete feedback and consider addressing the remaining concerns, if feasible.

Essential revisions (for the authors):

1) There is a need for improved cross-validation. Specifically, clarify the number of cross-validation folds and method for data splits (subject-wise or across the whole dataset) for the XGBoost model, reporting both the mean and standard deviation for the cross-validation split. Furthermore, for the CNN, leave-one-out cross-validation across 44 participants, results in only 2.3% of the data used for a test set, which can very likely result in overfitting, thus needs to be more stringently tested for this.

2) Explicitly state how much data were discarded due to missing signal from one or more sensors or to outliers and regularity of repeated patterns (address concerns that only regular patterns were used, how this can skew the data, and why it was not done for the force plate data). Furthermore, why was the data from the clinical trial processed differently (different exclusion criteria for percentage of missing data and Pearson r coefficient threshold)?

3) If possible, quantitatively compare the simultaneous recordings of the two systems (force plates and pressure insoles) or amend the statements regarding such comparison to reflect the concern and state that it is only qualitative.

4) State whether a correction for multiple comparisons was applied to the t-tests, and if it is not included, it should be applied and the new results should be reported.

5) There is a need for an additional data analysis regarding the specification of the severity or type of gait impairment (can you classify different severity and discriminate between affected joints). This is vital when there are claims about disease signatures, or disease classifications, as otherwise, the results can reflect general cautious, slow, or antalgic gait rather than the disease.

6) There is a need for further evidence against the possibility that the only thing that the model classifies is slow vs normal pace walking. For example, can a simple model trained on walking speed compare in performance to the current results?

7) Compare the deep learning models developed here to the performance of simpler models like linear regression and support vector machine.

8) Provide further information and manuscript changes in accordance with the reviewers' comments.

Reviewer #1 (Recommendations for the authors):

(1) The made equivalency of ground reaction forces (GRFs) obtained via force platforms (load cells or force transducers) and pressure insoles (pressure sensors) can be misleading (e.g. line 415). The same applies to comparing the abilities of the pressure insoles to those of force platforms by using one (vertical GRF – vGRF) of the multiple variables (3-axial forces and moments as well as centre of pressure) to compare their performance, while in some cases (raw sensor data and derived gait characteristics) utilizing all of the data from the pressure insoles. Although it can be understandable to use vGRF to compare to the one from pressure insoles (as this is the most consistent variable obtained with pressure insoles), it can lead the readers to believe that the system equivalence is apt. The statements equating measurements from these two systems and stating the outcomes of such analysis should be amended to reflect that.

2) Similarly, the comparison of vGRF between force platforms and pressure insoles is only qualitative (demonstrating that the two measurements look similar in the control case) and even then, the pattern for knee OA is significantly different from the one of knee arthropathies demonstrated from the force platforms. If possible, can simultaneous recordings of the two systems (force plates and pressure insoles) be quantitively compared, or if such data does not exist in the dataset, amend the statements regarding the comparison to reflect that?

3) Digital insole data pre-processing:

a. In the Methods Section, it is stated that since the digital insoles do not collect data in regular intervals the data was interpolated. This is confusing since data collection intervals should not matter as the analysis is not done in real-time. Can you clarify what is meant by this? Does it mean that the data is sampled at 100 Hz but these 100 samples per second are not regular (i.e. the first 100ms contain 20 samples while the next 100ms contain 5 samples) or is it meant that the data was up-sampled to 1000 Hz from 100 Hz to match the force plate data sampling rate? Also, state the force plate sampling rate and the brand/model of the equipment.

b. Further in the section, it states that walks with missing data from 1 or more sensors, or with missing data from 1% of the walk were discarded. Can you state how much data was discarded as a percentage of the overall data?

c. Similarly, data was discarded not only based on outliers but also on the regularity of repeated patterns. How much of the data was discarded as a percentage of the overall data in this part? Also, this is skewing the data to consider only regular patterns, which should be explicitly stated when comparing results and discussing them as it is a vital detail and was also not a thing done for the force plate data.

d. Why was the data from the clinical trial processed differently (different exclusion criteria for percentage of missing data and Pearson r coefficient threshold)? These have to be the same no matter what for comparative reasons.

e. Can you clarify more on the treatment population groups and the number of participants? Line 587 states 13 patients per treatment group aiming for a total of 30 patients, but the different treatment groups were not stated.

4) Can you comment on the pressure insoles size and fit for the participants, were there any cables connecting the insole leads to devices on other parts of the body, were the fit and the presence of insoles affecting the normal gait of the participants?

5) Concerning the derived gait parameters – It is explicitly mentioned in the Methods Section that the investigated gait parameters were less influenced by walking speed, but the Results section states that walking speed correlates were excluded rather than that they were significantly reduced. It is an important distinction, especially since the threshold was "Spearman rho > 0.7".

6) Lack of model cross-validation folds information:

a. For the XGBoost model – the force plate dataset was randomly split into 85% training and 15% testing datasets. Which force plate dataset was used (GaitRec?) and, more importantly, how many times was this repeated (how many cross-validation folds)? Was the split done across participants (85% of participants for training and 15% for testing) or across the whole dataset? If it is for the whole dataset, can you report a participant split? This will indicate how general the model is and testify to its strength to be used in a typical scenario when you want to predict OA in new patients.

The mean and standard deviation (SD) for the cross-validation needs to be reported. Furthermore, this trained model was further tested using the R5069-OA-1849 clinical study dataset only, is that correct?

b. Similarly, leave-one-out cross-validation (LOOCV) was applied for the convolutional neural network (CNN) model but there are no mentions of how many folds. How many participants, in total, was this model trained on and did you cycle over all of them (number of folds = number of participants) or was this done only once? If done only once, it needs to be repeated for all participants and the results for the mean and SD from these need to be reported.

c. Furthermore, the CNN results need to be tested for overfitting. For example, if the LOOCV of the CNN included 44 participants, then 1 participant represents only ~2.3 % of the data, meaning that the model most likely overfits this dataset. Thus, this needs to be checked by including more participants in the cross-validation (i.e. 85%/15% split across participants). This is raised since the CNN performance for the classification of knee OA using derived gait characteristics achieves auROC = 1 and auPR = 0.999, which can be strongly indicative of overfitting and needs to be checked.

d. Why was the cross-validation split different for the individuality and consistency CNN models and why is the last output consisting of a 23-element vector (shouldn't that be 44 to reflect the 44 different participants from the R5069-OA-1849 clinical study?)?

7) The results for subject-specific gait signatures are very exciting. However, the further claims on the ability to identify clinical attributes beyond knee disease as well as generalizability of the method are not substantiated. The results demonstrate that if data is included from both days of recording (day 1 and day 85 of treatment), there is a trend (P=0.033) suggesting it could be possible to identify the subject from others even across days. However, for this to work, you need training data from both timepoints of treatment, which is not the overall aimed application. It is still great that the distinction between individual participants is preserved regardless of the treatment time point! Although, the statement for the generalization across days has to be amended to reflect the results as the results from training on day 1 only reflect that it cannot distinguish between the day 85 data from the same participant and the rest. Similarly, the claim for a richness of data to help identify other clinical attributes is not corroborated by these results since they indicate that one is able to find different classification boundaries between participants. This does not necessarily reflect differences in clinical attributes as they could be solely based on different walking patterns and symmetry in pressure distribution.

8) Statistics – was there a correction for multiple comparisons for the t-tests? If so, that should be stated in the methods and, if not, it should be included and reported. Can you also overlay statistical significance on the plots?

9) Can you include comments on the additional benefit of using pressure insoles instead of inertial measurement units (IMUs) and include classification results using just the acceleration and angular velocity data? In the manuscript, it is mentioned a few times that gait speed (a feature that can be derived from a much cheaper IMU) is one of the main features to help classify OA. The further analysis in the paper demonstrates that features that are less correlated with speed can achieve a better performance, which is great. However, it will be good to quantify explicitly the IMU role and clarify further what else could be possible by having the additional pressure data, which can excite the reader even more and give further perspective.

10) Similarly, can you elaborate more on the importance of identifying participants using the CNN approach investigated in this work? There is a sentence about this on line 405 but it would be beneficial for the reader to understand more and will show the importance of your results.

11) The inclusion of the foot as an important dependable for classification in the XGBoost model (line 269) should be stated to be because the OA participants were injured only unilaterally (left leg), thus, this will generate these differences regardless and should be put as a confound. Have you tried classifying only from the "healthy" leg in OA participants, to demonstrate that the affected side does not matter?

12) Can you comment on the fact that knee OA participants are walking more slowly, which is indicated by the clustered data for vGRF and less by the gait characteristics, but the raw sensor data clusters the OA right next to the fast walking control group (Figure 4 A-C)? What causes this different and counterintuitive clustering?

13) Can you elaborate on the linear model fitted to each point along the vGRF curve (visualization of knee arthropathy signatures from vGRF data, Supplementary Figure 2) in the Methods Section?

Reviewer #3 (Recommendations for the authors):

– Insoles have been used for gait assessment in multiple groups, and validation studies exist. The introduction might benefit from a summary of these findings.

– In the introduction, a rationale could be provided for why knee arthropathy was chosen for the current paper. In the eyes of the authors, what does this group reflect? Please also discuss previous studies regarding GRF in knee OA (e.g. Costello et al., Osteoarthr Cartilage 2021; Costello et al., Br J Sports Med 2023).

– In the methods, I missed information about which knee injuries were included. In line with my previous comment, did they all have pain above a certain threshold? This group can be very heterogeneous.

– The set-up of having only one group with disease vs controls, is severely limiting the potential impact of the ML model. If the authors would be able to test if this model could be trained to differentiate between pain levels, or which joints are involved, that would substantially improve the impact. See for example Leporace et al. Clin Biomech 2021.; Kushioka et al. Sensors 2022.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Digital wearable insole-based identification of knee arthropathies and gait signatures using machine learning" for further consideration by eLife. Your revised article has been evaluated by Tamar Makin (Senior Editor) and a Reviewing Editor.

After detailed discussions with our review panel, it is clear that significant concerns remain unaddressed. These issues are critical for the integrity and publication viability of your work.

Key areas requiring your immediate attention include:

1. Methodological Rigour: There are serious concerns about your choice of cross-validation method and modelling approach, given the heterogeneity of the OA population. A comparative analysis with simpler models is also lacking, raising questions about overfitting.

2. Data Presentation and Analysis: Discrepancies in data handling and presentation, particularly in Figure 4 and your exclusion criteria, are worrying. These issues cast doubts on the validity of your comparisons and findings.

3. Comprehensive Explanation: Essential details are missing or inadequately explained. This includes the need for clearer elaboration on the linear model in the Methods Section and a more thorough discussion on the limitations and assumptions of your study.

Below are detailed comments from our reviewers. These points are not merely suggestions but are critical for the scientific validity and integrity of your research. It is essential that each of these points is addressed thoroughly in your revision for further consideration of your manuscript for publication.

Reviewer #1 (Recommendations for the authors):

Thank you for the revisions made to your manuscript. While appreciative of your efforts, it is critical to address several key issues that remain outstanding. These revisions are necessary to ensure the scientific rigour and validity of your paper:

1) The lack of cross-validation or the use of leave-one-out (LOO) cross-validation in cases where the test set is representative only of <5% of the data under the reason of not having enough data while having 21 control and 35 OA participants. This is important since the OA population is highly heterogeneous and is difficult to make generalised assessments and statements based on such outcomes as the results can be clearly overfitting. Thus, it is still strongly felt that the authors have to improve the cross-validation and in cases where they feel that the data is not enough for the model use a simpler model such as a linear regression or a support vector machine with a proper cross-validation split for such analysis. Furthermore, if having slightly more or less data is such an issue for the model then this would be a raise for a further concern in any case.

2) It is imperative to include a comparative analysis with simpler models like logistic regression and SVM. This is necessary to substantiate the choice of your complex models and to address potential overfitting issues.

3) The difference in exclusion criteria for a percentage of missing data and Pearson r coefficient threshold between the control and OA population raises a major concern for making invalid comparisons. This was not corrected by the authors stating that because the data for patients were less the criteria differed, which is not a sufficient reason.

4) Discrepancies between the data clustering for slow and fast walking were also ignored and attributed to "likely just how the PCA algorithm processes the data", which is not correct. What is even more concerning is that now in the manuscript the figure looks different and the colours for fast and slow in Figure 4 C were switched without this being commented. This is a clear contradiction because the authors did not perceive the data to be wrong and any need to make any amendments, and yet the figure colour coding is switched for the very last tile of Figure 4.

5) Although information regarding the treatment groups is available online in Section 8.2.6.6 of the R5069-OA-1849 clinical study protocol, the manuscript will still benefit from a small clarification in the text regarding this as it is quite difficult for general readers to go through clinical studies for a brief detail like these.

6) Suggestions on the inclusion of a discussion regarding utilizing inertial measurement units for such an assessment as a cost-effective alternative for insoles, especially since walking speed parameters were identified as major markers, was also ignored and not stated to be included in the text.

7) Elaborations on the linear model fitted to each point along the vGRF curve (visualization of knee arthropathy signatures from vGRF data, Supplementary Figure 2) in the Methods Section were also not stated to be included in the text.

Reviewer #2 (Recommendations for the authors):

The authors have gone through the comments and addressed only some of them. However, a good amount of comments (from the other reviewers as well) remain. Please address them accordingly. For the comments I have given in the previous round, please see below for things that still need clarification:

1. Regarding the comment about the presence of osteoarthritis and the components of the ground reaction forces that are required for this. Indeed the insoles can only measure vertical GRF, but I believe a statement detailing the importance of the other components for OA should be added in the manuscript as a potential limitation.

2. I understand the study did not account for familiarization, but I would say it might be an important influencer. Therefore, at least adding a statement on this limitation might make the work clearer.

3. Please specify in the manuscript that the assumptions for the statistical tests were indeed checked for, as mentioned in the response to the reviewers' document.
