# Author response - Round 1

Authors:
- Chin-Hsuan Chia ([ORCID: 0000-0002-3343-9541](https://orcid.org/0000-0002-3343-9541))
- Xin-Wei Tang
- Yue Cao
- Hua-Teng Cao
- Wei Zhang
- Jun-Fa Wu
- Yu-Lian Zhu
- Ying Chen
- Yi Lin
- Yi Wu
- Zhe Zhang ([ORCID: 0000-0002-0899-8077](https://orcid.org/0000-0002-0899-8077))
- Ti-Fei Yuan ([ORCID: 0000-0003-0510-715X](https://orcid.org/0000-0003-0510-715X))
- Rui-Ping Hu ([ORCID: 0000-0002-7626-2061](https://orcid.org/0000-0002-7626-2061))

## Response text

DOI: [10.7554/eLife.65099.sa2](https://doi.org/10.7554/eLife.65099.sa2)

Essential revisions:

1. The main concern raised by all three reviewers regards the impossibility to disentangle between the contributions of circadian vs. homeostatic factors on the observed effects. The analyses have been performed only considering the homeostatic factor (i.e., the time spent awake). We recommend that you address this concern by the following additional analysis: comparisons between data points collected at the same time-of-day (i.e., controlling the circadian factor): 3 data points for the TMS measures [7 a.m, 11 a.m., and 5 p.m. of the first and second day (before vs. after sleep deprivation)] and 1 data point for EEG measures (11 a.m. of the first and second day).

We thank the reviewers for pointing out circadian factors can be a confounding factor in our analyses. Following the suggestions from the reviewer, we now implemented PLS regression (similar to Figure 3A) on matched timepoints with TMS (new Supp. Figure 4A) and EEG data (new supp. Figure 3B) towards SSS. We found that for the 7 a.m. and 11 a.m. timepoints, both TMS and EEG data show obvious separation between sleepiness states, indicating that these measurements indeed represent a strong homeostatic component that is independent of circadian effect. We did not observe good separation in the 5 p.m. TMS group. We argue that this is due to the fact that within this timepoint the average sleepiness showed small difference.

In addition, to further test whether the variance in TMS measurements reflect homeostatic (sleepiness) factors or circadian factors, we grouped similar SSS datapoints and constructed mixed-effect linear models between TMS and hour of the day (new Supp. Figure 4B). In all groups, we did not observe correlation between TMS measurements and circadian factors, corroborating our conclusion that TMS measurements reflect homeostatic factors.

2. Linking the wakefulness measure to synaptic homeostasis theory may be possible via literature references. It would be important to explain (in the introduction, at least) what synaptic homeostasis theory predicts about a >24h sleep-deprivation intervention including the 'rebound' effect on sleepiness after 24h, since that is what the authors have done.

We have now included text introducing the circadian effect in the introduction section (line 61-63). Additional analyses related to circadian effects are now included in the results and Discussion sections.

3. It would also make sense to test the model more rigorously with something like 5-fold cross-validation.

We agree with the reviewers that cross-validation is a common practice for machine learning analysis. In general, however, there is no consensus on how to perform cross-validation for mixed-effect models due to the nature of random effects cannot be predicted for new subjects. It is an area of active research in the field of statistics regarding how to circumvent this issue. Currently, potential solutions including estimating information criteria of the model (Statistical Science, 2013, 28(2), 135–167; Journal of Data Science, 2011, 9, 15-21) or using an iterative method to estimate random effects (Journal of Pharmacokinetics and Pharmacodynamics, 2013, 40, 243–252).

We implemented the second method and used the prediction error as the metrics for measuring model accuracy. Among 38 subjects, we used 60% (23 subjects) for training and 40% (15 subjects) for testing. Within the training subjects, we used a 5-fold random sampling to choose 18 subjects for estimating the initial model, and 5 subjects for evaluating the error. This is repeated for 500 times and the best model is refitted using the 23 subjects for estimating the random effects and calculating the training error. Next, we applied this model to the 15 subjects testing set by freezing the fixed effect and estimating the random effects, and finally calculating the testing error. We repeat this training-testing process for 500 times to get a robust and generalizable result. As a negative control, we used randomly shuffled SSS dataset for the same procedure.

These cross-validation analyses are plotted in the new Figure 3E. The training and testing errors are close to each other, indicating robust predicting power from TMS measurement to SSS. On the other hand, shuffled data produced chance level estimation, further supporting the validity of the model.

4. Line 352: "Pilot explorations adding sex and age as predictor variables show no effect of these variables." It would be interesting to know if the predictor "session" was also tested.

We have tested “session” as a predictor as the reviewers requested. We coded session into numeral 1-8 in the model. The result showed that “session” showed significant correlation to SSS:

However, we do not think “session” is a very meaningful variable as it contains mixed information about homeostatic and circadian information. As shown in Figure 1C, SSS is grossly correlated with session. Thus, this correlation is quite expected.

5. Figures 1.C. and 2.C-E.: if there are any significant differences between sessions, please report it in the figure.

We have now provided the pair-wise post-hoc tests for these panels in Supp. Figure 2.

6. Figure 1.D..: could you discuss the higher δ and theta activity observed in occipital areas (instead of fronto-central areas)?

We have now added this discussion in the result section (line 115-118). In summary, we observed consistent trends with data from individual EEG electrode but indeed see more prominent changes in the occipital regions. This is consistent with previous studies showing that sleep-associated changes happen most prominently in the occipital regions. This may reflect that our subjects are drifting in and out of sleep states throughout the program.

7. Line 128: MT abbreviation without previous definition in the text (but in line 307).

We have added the definition at its first appearance in the text (line 134).

8. Methods / Statistical analysis: specify if the main assumptions required by mixed-effect model were checked and met.

The core assumption of mixed-effect model is that the residuals and random effect coefficients are independent and identically distributed (Methods in Ecology and Evolution 11(9), 1141-1152, 2020). We have plotted these variables in our model:

We have added the description of this calculation in the method section (line 406-421), without including Author response image 1 , as we feel that this might be too technical for the readers.

9. Methods / Study flow: give a brief rational why SSS (instead of, for example, KSS, VAS, etc.).

We have added this information in the method section (line 310-311).

10. An interesting analysis could be to test if the model could also predict the EEG activity (mean or theta), as an objective marker of sleepiness (even though EEG was only recorded 3 times in a subgroup of 15 participants).

We thank the reviewers for the suggestion. We applied canonical correlation analysis between TMS and EEG measurements due to their multi-dimensional nature. We reported the results in the new Supp. Figure 5. There are 2 modes between TMS and EEG show significant correlations. The first mode primarily aligns with the sleepiness measurements, but not the second mode. This result indicates sleepiness is a major covariate that correlates between EEG and TMS.

11. The study participants do not actually report feeling very sleepy. The key behavioral measure is self-reported sleepiness on the Stanford Sleepiness Scale which is a 7-point scale, with only 6-7 indicating the participant is 'sleepy'. However participants reported level 6-7 sleepiness only at approximately 15 observations (fig3D, grey dots). This is from 38 participants * 8 testing moments i.e., >300 total observations. If participants were only actually sleepy in <5% of observations this could weaken the conclusions about sleep and sleepiness. And the clustering of the observations around the lower points 1-5 on the Sleepiness Scale might reduce confidence in the model fit. This is not necessarily a big issue but it might be sensible to acknowledge it in the discussion.

We agree with the reviewers that it would have been better if more level 6-7 datapoints are in the model. Nevertheless, our model does show a gradient effect that matched well for SSS levels 1-5. We have revised the manuscript to include this issue (line 278-282).

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

The authors made a deep and accurate revision, with some new control analyses. They responded to the points that were raised by the reviewers, and the manuscript is now quite improved. Two concerns need further consideration:

1. The authors provide some support to the relative independence from circadian factors. Please discuss the current results within the context of previous studies of cortical excitability as a function of circadian factors (e.g. Chellappa et al. Circadian dynamics in measures of cortical excitation and inhibition balance. Sci Rep. 2016 Sep 21;6:33661. doi: 10.1038/srep33661).

2. Concerning the theta and α activity across sleep onset, please also consider a preliminary finding on intracranial recordings of a pharmaco-resistant patient with epilepsy [supplementary Figure 1 in Marzano et al., 2013 (Sleep Med. 2013 Nov;14(11):1112-22. doi: 10.1016/j.sleep.2013.05.021)]

In this revision, we have made the following changes of the manuscript:

1. We have expanded our discussion on the potential confounding effect of circadian rhythm (lines233-245).

2. Regarding the findings in Marzano et al., 2013, we added two related discussions:

a. On our results of the occipital lobe showing the most prominent power in EEG(lines 123-126);

b. On the potential regional differences among brain regions (lines 285-290).

3. We have made some miscellaneous changes regarding authorship, affiliations and acknowledgements.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

The manuscript has been improved but there are some remaining issues that need to be addressed. In particular, we note that there were apparently some significant changes in the author list, which is a bit unusual at this stage of the process, as the current revisions were relatively minor. Can you please provide a rationale for each of the authorship changes?

We apologize for the confusion caused by the change on the author list made during our last revision. Specifically, we moved Dr. Hua-Teng Cao from 10th to 4th on the author list.

Dr. Cao is a postdoc scholar in Dr. Zhang’s laboratory and has been joining the project since the beginning, assisting Dr. Zhang on the analysis of the dataset. During the first round of revision, Dr. Cao has devoted substantial effort in completing the additional analyses. All corresponding authors (Drs. Zhe Zhang, Ti-Fei Yuan and Rui-Ping Hu) agreed that he should be acknowledged for his contribution. In re-submitting our manuscript, we have already changed Dr. Cao’s authorship in the online system, but failed to update the author list on the manuscript PDF file. We have corrected this error during our second round of revision, leading to the issue described above. Nevertheless, if you check the author list on the online system, you will see that his position was changed during the first round of revision, which correctly reflected his contribution to the study.
