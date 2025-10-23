# Peer review - Round 1

Editors:
- Markus Ploner, https://ror.org/02kkvpp62 Technische Universität München Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74463.sa0](https://doi.org/10.7554/eLife.74463.sa0)

This article will be of great interest to researchers interested in the brain mechanisms of pain. It shows how the connectivity of brain networks associated with sustained pain changes over time. These findings are supported by compelling fMRI analyses of a tonic pain paradigm in two cohorts of healthy human participants. These important insights advance the understanding of the brain mechanisms of sustained pain, which is the hallmark of chronic pain as a major healthcare problem.


---

# Peer review - Round 1

Editors:
- Markus Ploner, https://ror.org/02kkvpp62 Technische Universität München Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74463.sa1](https://doi.org/10.7554/eLife.74463.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Dynamic Functional Brain Reconfiguration During Sustained Pain" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Markus Ploner as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Reviewing Editor and Timothy Behrens as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Tamas Spisak (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) It remains unclear whether the changes of brain networks over time simply reflect the duration of sustained pain or whether they essentially reflect different levels of pain intensity/avoidance. Therefore, analyzing and/or discussing whether brain network changes reflect pain duration or pain intensity would be crucial for the interpretation of the findings.

2) Although the manuscript is very well-written it might benefit from an even clearer and simpler explanation of what the consensus community structure and the underlying module allegiance measure assesses.

3) The added value of the assessment of the dynamics of brain networks remains unclear. Specifically, it is unclear whether the current analysis of brain networks dynamics allows for a clearer distinction between and prediction of pain and no-pain states than other measures of static or dynamic brain activity or static measures of brain connectivity. Therefore, clarifying the added value of the community structure analysis as compared to other more common analyses of brain activity and brain connectivity would significantly strengthen the case.

4) The Authors do not touch upon the concept of temporal summation of pain, historically associated with tonic pain. Please comment on the relationship of the present study to temporal summation particularly since chronic pain patients often exhibit increased temporal summation of pain.

5) Please consider a recent related paper by Cheng et al., Arthritis Rheumatol, 2021 that shares most of the methodological pipeline to highlight similarities and novelties and deepen the comparison with the associated literature.

6) The data analysis is entirely conducted on young healthy subjects. This is not a limitation per se, but the conclusion about offering new insights into understanding mechanisms at the basis of chronic pain is too far from the results. A similar pipeline has been actually applied to chronic pain patients (Cheng et al., Arthritis Rheumatol, 2021, Lee et al., Nat Med. 2021). Discussing the results of the present paper in relationship to those, could offer a more robust way to connect the Authors' results to networks behavior in pathological brains.

7) The behavioral measure used to assess evoked pain perception (avoidance ratings), has been developed for chronic pain patients and never validated on healthy controls. It might not be an appropriate measure considering the total absence of pain variability in the reported responses over forty-eight subjects. Please discuss this important point. Moreover, please address the following questions:

• How does the rating scale look like? Is the meaning of the anchors and of the thresholds for weak, moderate, strong, and very strong displayed on a screed during the scan? What are the instructions given to the participants before the start of the experiment? Do they induce any kind of pain expectancy (e.g., "After 6 minutes the pain should start decreasing" or analogous expressions)? A combination of those elements could explain the lack of pain variability.

• The behavioral outcome is called "pain avoidance" and the Authors hypothesize that it is proportional to the perceived pain. Is there any evidence proving this correlation? The collected ratings are the answer to the question "how much do you want to avoid this experience in the future?". Is it possible that this question is too generic to be called pain avoidance? Did the Authors quantify in any way the effect of laying down in a scanner for long time? It might play a role in the avoidance index.

8) The dynamic measure employed by the Authors is better described from the term "windowed functional connectivity". It is often considered a measure of dynamic functional connectivity and it gives information about fluctuations of the connectivity patterns over time. Nevertheless, the entire focus of the paper, including the title, is on dynamic networks, which inaccurately leads one to think of time-varying measures with higher temporal resolution. This allows one to follow network reorganization over time without averaging 2-min intervals in which several different brain mechanisms might play an important role. In summary, the assumption of constant response throughout 2-min periods of tonic pain and the use of Pearson correlations do not mirror the idea of dynamic analysis expressed by the Authors in title and introduction. Please consider removing "dynamic" from the title, reduce the emphasis on this concept, address possible confounds introduced by the choice of long windows and rephrase the aim of the study in terms of brain network reconfiguration over the main phases of tonic pain experience.

9) Procedure chosen for evoking sustained pain. The measures in figure 1B suggest that the intensity of the painful stimulation is not constant as expected for sustained pain (probably the effect washes out with the saliva). In this case, the first six-minute interval requires particular attention because it encapsulates the real tonic pain phase, and the following ones require more appropriate labels. Ideally the authors should cite previous studies showing that tongue evoked pain elicits a very specific behavioral response (summation, habituation/decrease of pain, absence of pain perception). Moreover, please address the following points:

• Does the procedure include a calibration phase? If yes, please add description in the Methods section. If not, how do the Authors explain the relatively small standard error of the mean reported in Figure 1?

• If possible, add citation proving that there is a very consistent behavioral (pain related) response to the capsaicin: no pain variability against what most of the evoked pain experiments showed.

• Please report in the supplementary material the dots distribution (box plot with visible dots) of the ratings at minute 0, 6, 14, 20.

10) Community detection analysis. Please clarify the following issues:

• The thresholding of the connectivity matrices for the binarization of the networks is certainly a weakness of the study and, more in general, of most of the connectivity analysis (only few estimators have known null distributions). Here, the chosen optimal threshold is the one that maximize the difference between conditions (capsaicin vs controls) in terms of global graph measures, including modularity. I suggest adding a comment on the effect of maximizing a measure depending on the modularity of the networks, on the subsequent community detection algorithm, also based on maximizing modularity (within the network this time). What is the Authors' opinion on this possible confound? Also, what is the rationale/hypothesis behind this procedure for obtaining sparse matrices?

• Did the Authors consider running the analysis with other resolution parameters (γ and omega)?

Group-level consensus community detection: I found this section difficult to follow, especially in terms of reasoning for specific choices and steps of the analysis.

• Step III: the standard definition of allegiance is a binary matrix whose elements are equal to one only when the two correspondent nodes belong to the same community (as the Authors described). After step III, a new index is computed as the mean of allegiance matrices over time and across subjects. Its value indicates the proportion (percentage) of subjects showing the two nodes in the same community at specific time points. Or how many times the two nodes belong to the same community during the early/middle/late stage of the experiment. Using the name allegiance (a binary measure) to indicate those percentages, might be misleading. I suggest using more appropriate names (measures like "agreement", "dwell time" and similar might be useful) and providing more explanatory examples on how to read the value of the computed measures.

• Step IV: please specify number of permutations.

• Step VI: in the same spirit as the two previous comments, I suggest either reconsidering the necessity of this computation, or explaining the reasons for applying a community detection algorithm twice. I believe that additional layers of complexity always require a clear question that they can answer.

11) It remains unclear, how specific the results are to pain. Differences between the control resting state and the capsaicin trials might be – at least partially – driven by other factors, like motion artifacts, saliency, attention, axiety, etc. Differences between stages over the time-course might, additionally, be driven by scanner drifts (to which the applied approach might be less sensitive, but the possibility is still there ) or other gradual processes, e.g. shifts in arousal, attention shifts, alertness, etc. All the above factors might emerge as confounding bias in both of the predictive models. This problem should be thoroughly discussed, and at least the following extra analyses are recommended, in order to attenuate concerns related to the overall specificity and neurobiological validity of the results:

• Reporting of, and testing for motion estimates (mean, max, median framewise displacement or anything similar).

• Examining whether these factors might, at least partially, drive the predictive models.

• e.g. Applying the PCR model on the resting state data and verifying of the predicted timecourse is flat (no inverse U-shape, that is characteristic to all capsaicin trials).

12) Statistical inference. An important issue is the (apparent) lack of statistical inference when analyzing the differences in the group-level consensus community structures (both when comparing capsaicin to control and when analysing changes over the time-course of the capsaicin-challenge). Although the observed changes seem biologically plausible and fit very well to previous results, without proper statistical inference we can't determine, how likely such differences are to emerge just by chance. This makes all results on Figures 2 and 3, and points 1, 4 and 5 in the discussion partially or fully speculative or weakly underpinned, comprising a large proportion of the current version of the manuscript. There are two main ways of handling this issue:

• Enhancing (or clarifying potential misunderstandings regarding) the methodology (see my concrete, and hopefully feasible, suggestions in the "private part" of the review). There are likely many ways to test the significance of these differences. Two permutation testing-based ideas are (i) permuting the labels ctr-capsaicin, or early-mid-late, repeating the analysis, constructing the proper null distribution of e.g. the community size changes and obtain the p-values and (ii) "trace back" communities to the individual level and do (nonparametric) statistical inference there.

• De-weighting the presentation and the discussion of the related results.

Reviewer #1 (Recommendations for the authors):

• The authors emphasize the term "pain supersystem". This term is not very well-introduced yet and the necessity for such a term is unclear. I recommend that the authors rely less on this term and omit it at least from the abstract.

• The statement in the abstract "In the early stage, the orofacial areas of the primary somatomotor cortex were separated from the other primary somatomotor cortices and integrated with…" is a bit ambiguous. It might better read "In the early stage, the orofacial areas of the primary somatomotor cortex were separated from other areas of the primary somatomotor cortex and integrated with…"

Reviewer #2 (Recommendations for the authors):

• I suggest reducing the amount of text in the figures. All the information needed to understand the illustrations should be included in the captions. Figure 1 and Figure 7 are the ones that require the most attention in this respect.

• It might be a good idea to specify when any previous evidence used to justify the current analysis or to make inferences on the obtained results actually come from the Authors' previous publications. Especially if they are extracted from the same dataset, this information is relevant.

• In their previous paper, the Authors had access to a dataset including the experimental conditions: tonic capsaicin pain, tonic aversive taste, and tonic aversive odor. Did the Authors analyze the communities structure during those controls conditions? Did they consider testing their classifier on them? In my opinion, it would add a lot of robustness to the study findings, and it would make the obtained results reliable and unquestionably pain related (thinking of the more general avoidance ratings).

• In terms of data availability, the Authors declared that data and codes will be shared upon publication. I would appreciate their availability if there will be a second loop of revisions before potential publication.

Reviewer #3 (Recommendations for the authors):

– As the authors mention the cross-validated evaluation of the PCR model is biased due to hyperparameter optimization. While the independent evaluation resolves any related concerns, the authors might consider applying a nested cross-validation framework, to have unbiased estimates for the discovery dataset, as well.

– Optimizing the network density threshold in the same dataset, especially on one of the conditions-of-interest (Q1: capsaicin vs. controls) may be circular (as the optimized global network metrics may well be associated to the community structure). On the other hand, this potential circularity does not affect all he results (e.g definitely not the results based on the independent test dataset) and in general, I don't think this would significantly affect the results. Nevertheless, performing (or reproducing) the optimization on independent data would be reassuring. Alternatively, this issue must be discussed as a potential limitation/bias.

– While this is not explicitly stated, prediction performance is evaluated only on the within subject-level. For better comparability to other methods, please report and discuss the "between-subject" estimates, too (i.e. how well can we classify/predict from a single session/window of a single subject).

– Introduction: discussing the possible relation of the present work to chronic pain or other clinical pain conditions is not sufficient.

– More information is needed about the individual variability of the pain-related behavioral time-courses (maybe in the supplementary info). Was remission complete in all participants?

– Some participants might be more tolerant for capsaicin than others, due to eating habits. Please discuss whether this could potentially affect the results.

– At many points, e.g. in paragraph 25 on page x or 5 on page 25, it is mentioned that the models generalized across two datasets. While the terminology is currently heterogenous, I kindly suggest to use the term "generalization" only to the independent test dataset (here the models really had to generalize to scanning parameters, paradigm differences, etc.)

– it's a bit unclear why the pain avoidance ratings fall. One would, somewhat naively, hypothesize that if the participant once though she would never repeat this experiment again, why would she change her mind a couple of minutes later, when the memories of pain are still vivid. Please comment on this.

– Please add a short discussion of the differences of the behavioral ratings and how they might affect the findings. (this might be positive thing: a sign of generalization across behavioral assessment protocols).

– Please clarify why *pain* avoidance (slightly) increased in the control resting state scan.

– Please provide more rationale for the choice of ML algorithms.

– How were the hyperparameters set for the SVM? Why were those not optimized, too?

– Why was only one hub selected for the seed-based analysis in the case of the classifier?

– While the prediction performances are obviously significant, testing for this with bootstrapping may be suboptimal, as bootstrap samples may inherit non-normality from the parent dataset. Permutation test would be more "elegant" in my opinion.

– Discussion: relation to consciousness might be somewhat speculative, should be hedged.

– Will the raw data also be shared?
