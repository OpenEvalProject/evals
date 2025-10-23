# Peer review - Round 1

Editors:
- David Badre, Brown University United States
- Michael J Frank, Brown University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.39497.020](https://doi.org/10.7554/eLife.39497.020)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "Integrated External and Internally Generated Task Predictions Jointly Guide Cognitive Control in Prefrontal Cortex" for consideration by eLife. Your article has been reviewed by a Senior Editor, a Reviewing Editor, and three reviewers.. The following individuals involved in review of your submission have agreed to reveal their identity: Carlo Reverberi (Reviewer #2).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that this submission will not be considered further for publication in eLife.

This paper takes a novel and sophisticated approach to an important problem. Understanding how internal predictions are integrated with external cues in order to manage task sets and control behavior is of high importance. The reviewers and editors all recognized this importance, and were impressed by the sophisticated approach to modeling behavior and the brain.

The "internal prediction" side of this problem is central to the theoretical impact of this study. However, as the reviews and the subsequent discussion of them made evident, it was unclear what this internal prediction reflects in this study. There appear to be several alternatives, with fairly different implications. For example, rather than an internal prediction, the internal effect could reflect some type of proactive interference (PI). Reviewer 2 points out that a more model-based internal prediction might have made qualitatively different predictions than PI that were not tested here. If true, this would complicate the interpretation of Pjoint, particularly if it did make different predictions. Reviewer 3 further raised a separate point that learning might occur over joint external/internal prediction, rather than keeping them separate.

After considerable deliberation, we decided that there is substantial work to be done to treat a number of alternative accounts of what is happening here and to specify the nature of internal prediction in this task. Some could be done with additional modeling; others might require additional data collection. At eLife, we only invite a resubmission in cases where a single revision is likely to conclusively address any major points. The amount to do here and the uncertain outcome of that process is more substantial than would be typical for this type of revision. So, we have decided to reject the paper in its current form. However, in light of the strengths we note above, if you were to undertake the extensive additional analysis and/or data collection required to better characterize these data, we would be willing to consider the paper at eLife as a new submission. Though, we must note, that this invitation does not guarantee that the new submission would be reviewed or accepted.

Reviewer #1:

The present study examined how internally and externally cued task sets are integrated using quantitative analysis of behavior and fMRI data. Externally cued task sets consisting of visually present probabilistic cues. Internally cued tasks sets were modeled by how much recent trial history affected present task performance. Each source (internal and external) can be formalized as a prediction of the forthcoming task. Violations of these predictions (i.e. prediction errors; PEs) were hypothesized to reduce performance. The authors found that both internal and external PEs slowed performance (or conversely, that accurate predictions sped performance). Based on behavior, individual reliance on both sources was estimated and related to fMRI signals. Joint task prediction was related to signals in the DLPFC, preparatory task-set updating was related to frontal-parietal cortices, and PEs were related to activation in the dmPFC. Collectively, these data indicate separable contributions of multiple control regions to flexible behavior.

There is a lot to like about this study, particularly regarding the formal quantification of internal and external predictions/PEs. I do feel as though there is some opacity with some of the methodological choices, which may breed misunderstanding. Indeed, it is possible that my most substantive concern stems from such misunderstandings. So, perhaps additional clarification is all that is needed.

Essential revisions:

If I understand correctly, Pjoint reflects the prediction of the color task, which was the harder of the two tasks. So, if activation correlated positively with Pjoint, that could reflect preparation for the color task or preparation for cognitive load (e.g., much like a univariate analysis of a color-word Stroop task would look if contrasting color vs word). It's quite difficult to discern among these possibilities and more general task-set prediction with the MVPA procedure employed by the authors. As I understand it, the MVPA procedure is very similar to a traditional univariate analysis, at least initially, with the key differences being that (A) a neighborhood of voxels is regressed onto a predictor rather than a single voxel, and (B) ridge regression is used to induce regularization. Given that the data are smoothed, I suspect that the use of a searchlight rather than a single voxel simply induces more smoothing (i.e. effectively mimic'd by a larger smoothing kernel during preprocessing), so then the only real difference is the use of ridge regression vs OLS. Then, where the methods differ substantively is that inference from a univariate method would interpret the sign of the resulting β values (e.g., positive is activation), whereas the sign is effectively removed in the MVPA procedure in the cross-validation step. In this case, cross-validation can succeed if the betas are positive in both the training and test data (i.e. more activity in the DLPFC in preparation for the color task/harder task), negative in both the training and test data (i.e. less activity in the DLPFC in preparation for the color task/harder task), or a mixture of the two. The mixture would be what would indicate an abstract task prediction. However, given the 30 or so years we've been contrasting harder tasks vs easier tasks and seeing the DLPFC engaged more for the former, I'm worried that what is being depicted is preparation for the harder task rather than an abstract task set. There is still something very interesting about that prediction being formulated by both internal and external sources, but the interpretation is quite different (e.g., representation vs processing).

Note that if the authors had used MVPA to predict the task itself (i.e. classification) this would not be an issue. Given the association between MVPA and classification, I'm worried that many readers will make this mistake. I think that this can be investigated fairly easily by either (A) doing a simple univariate analysis using Pjoint as a parametric modulator, or (B) examine the βs produced by the ridge regression procedure. If the DLPFC region is positive on these metrics, then it would seem it largely reflects preparation for the harder task.

Even if this holds true, all is not lost! I believe the data depicted in Figure 4—figure supplement 2 is what we really want here. Those data indicate the absolute deviation from chance (i.e. deviation from no prediction). I think that's really what a task set would reflect. So, perhaps it is as simple as swapping in Figure 4—figure supplement 2 for Figure 4 and changing the story from the DLPFC to rostrolateral PFC and the IPS.

Reviewer #2:

The manuscript contrasts two types of anticipatory control (i.e., control based on a prediction of future states of the environment): one "external" based on explicit cues, another "internal" based on observed history.

Notwithstanding no information on the next task is present in the task history, subjects seem to rely on it, even more than on informative cues.

The manuscript is interesting and well written. Nevertheless, I am not fully convinced on the interpretation that the authors offer on one of the primary measures.

If I correctly understood Figure 3 and the description of the model, Pint for the color task increases monotonically with the length of the most recent color-task series. Thus, to be clear, between these three series:a) […] c-m-c-c-m-m-mb) […] c-m-c-c-m-m-cc) […] m-m-c-m-c-c-c

Pint-color is c>b>a

In other words, subjects would strongly expect another color task in c) while they would be highly surprised to get a color task in a).

The task sequence, however, is actually (pseudo)random:

- There is no dependency between history and next trial

- The proportion of the two tasks is 50/50

- (I guess that) the distribution of the length of same-task series is roughly exponential with a mode of 1 and a median of 2 (?).

Given that, the subjects may rather fast realize that the probability of a long same-task series is a priori very low compared to a short one. The usual (invalid) psychological reaction to this situation (see e.g. studies on random sequences perception/prediction) is to expect/predict alternation.

Thus, overall, I would expect that for subjects the prediction of the probability of color task would not monotonically increase with the length of the color sequence. For example, I would guess thati) […] cii) […] c ciii) […] c c civ) […] c c c c csubjects would explicitly predict that another c would be more likely in i) or ii) rather than in iii) or iv).

Notice that here I am assuming that sequences like iv or iii were rare in the task. Things would change if this were not the case.

In this experiment, no explicit measures of future task prediction have been collected from subjects, so we cannot know for sure what subjects’ expectations were.

Overall, given the way Pint is computed, I would instead consider it a measure of the strength of proactive interference from past trials. This would be consistent with the observation that the interference is stronger with the most extended same-task series.

This view would produce a significant shift in the interpretation of the results.

On another point:

What incentive did the subjects have to perform any control adaptation in advance? Given the task, a "rational" option available to a subject would be to wait for the task phase in which all information is available. For example, in Wisniewski et al., 2015 we used monetary incentives + adaptive timing to keep subjects motivated to use advance information.

Reviewer #3:

In the present study by Jiang et al., differing progenitors of task-related demands on cognitive control are assessed behaviorally and neurally. Specifically, explicit demands guided by external cues and implicit demands driven by internal history are contrasted for their predictive impact on cognitive control. A probabilistic task-switching paradigm was utilized to dissociate these two sources of information. Additionally, prediction-error (PE) variables and a Q-learning-inspired computational model were used to more acutely probe the behavioral and neural data. Behaviorally, the findings include support of a 'joint guidance' hypothesis, which states that cognitive control is jointly informed by external and internal information. Neurally, prediction error derived from joint guidance was found to be integrated in a dorsolateral prefrontal cortex (dlPFC) region. Lastly, the demands of proactive task switching and reactive task updating were found to be encoded in the frontoparietal network (FPN) and dorsomedial prefrontal cortex (dmPFC), respectively. The foremost merit of this study is in addressing the varying sources of information that impact cognitive control in a manner that reveals them as distinct neurally. Thus, cognitive control is proposed to contain multiple processes.

Essential revisions:

1) One key assumption in this study is that the task allows external and internal sources of prediction to be separable. Moreover, the task is designed for trial history to be controlled for, such that this history is uninformative (e.g., "set to zero.", Introduction). However, given that there were pre-scan training trials, and many trials included in the scanning (test) sessions ("9 runs at 50 trials each", Discussion section), learning effects might be present that make external and internal information less dissociable. That is to say, even though the trials are randomized, trial history is informative because the probabilistic value of each cue is being stored in a way that constitutes 'internal history'. Therefore, even though it is noted that this task makes trial-history (internal info) and cueing (external info) independent and is exclusively informative on cueing, an alternative perspective is that the task is biased for internal history. After the initial training trials, cue-based predictions may be entangled with internal history, given that probabilities associated with each cue have been learned (approximately). Behavioral and computationally modeled findings reported here might support the latter. Firstly, trial history assessed by i-1 (and i-2 to i-3) trial reaction time biased behavior (subsection “Behavioral data – 130 Effects of external cues and cognitive history”). Secondly, trial history has a three-fold larger effect on behavior than cueing (subsection “Behavioral data – Model comparison.”). Lastly, prediction error for internal history was encoded by networks overlapping with a previous study that had "predictive trial sequences" (Results section). One suggestion is to examine if (and how) the variables derived from these assumptions change over time. More specifically, if such variables differ from run to run. For example, does the internal history prediction variable (Pint and related PEint) increase or decrease from the first 50 trials to the last 50 trials?

2) Relatedly, given that the intention was to set internal history to zero in terms of predictability, calling this source of information (during modeling and analyses) a type of 'prediction' is a bit confusing. That is to say, if internal history is truly set to zero, how can it be used as an independent factor in analyses and termed a source of prediction?

3) At various points, further context and/or justification for analytic choices would benefit the claims made herein.

3a. Firstly, what justifies using the following combinations that comprise the two guidance models: (1) prediction error related to the previous trial (PEprev) and PE of cueing (PEcue) amount to the "max benefit hypothesis", and (2) Pcue and prediction error related to internal trial-history (PEint) amount to "joint guidance" (subsection “Behavioral data – Model comparison”). Even though control models and a model with all three factors were also compared, what is the conceptual backing and/or prior literature supporting this choice?

3b. Next, why is reaction time used for the bulk of the modeling work (and development of variables) as opposed to accuracy?

3c. Why is it assumed that 'optimal performance' is equal to fastest performance? In interpreting results in terms of cost/benefit analyses (e.g., in the expected value of control framework), it is presumed herein that speedy responses are equivalent to optimal responses (subsection “Behavioral data – Quantifying respective contributions of cue-based and trial history-based task predictions.”, and Discussion section). Reaction time gain was found to be positively correlated with using cue-based information, therefore the stronger impact of history-based information on behavior was surprising (subsection “Behavioral data – Quantifying respective contributions of cue-based and trial history-based task predictions.”, and Discussion section), and this was explained in terms of history having a lower cost because it is more automatic. However, it is not clear why internal history would be more automatic and how accuracy factors into this line of reasoning on performance benefits. Mean accuracy was quite high (table 1, Materials and methods section), thus it is possible that the cost to reaction time is outweighed by the benefit to accuracy, and that the observed trial-history-bias supports this.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for resubmitting your work entitled "Integrated External and Internally Generated Task Predictions Jointly Guide Cognitive Control in Prefrontal Cortex" for further consideration at eLife. Your revised article has been favorably evaluated by Michael Frank (Senior Editor), David Badre (Reviewing Editor), and three reviewers.

The reviewers feel that their major concerns were addressed by your revision. They and the editors are in agreement that the manuscript is now acceptable for publication at eLife. However, you will note that two of the reviewers raised some additional suggestions of ways the manuscript could be clarified. Though these are not essential revisions, we return this to you once more to give you the opportunity to make changes based on these suggestions and questions. In particular, we encourage you to carefully consider the suggestions that would help make the task paradigm and analysis logic clearer (the first comment from both reviewers). The comments for further clarification from the are copied below.

Reviewer #2:

1) Introduction: This was brought up in the first round of review, and adequately addressed in the added analyses. However, concerns over the language used here bears repeating as it was a conceptual obstacle in following the logic of the present paradigm. 'Trial history' is a broad concept that likely has components, and the single component of "trial sequence" is fixed at zero with randomization. This appears to be the point of the chosen paradigm: e.g., that the potential confound of "sequence" is controlled for by randomization, so any internally driven predictions are based on the subject's choice to do so (sub-optimally, as is probed subsection “Behavioral data – Quantifying respective contributions of cue-based and trial history-based task predictions”). That is to say, internally driven factors become independently "discoverable" (via computational modeling) after randomization. The "fixed to zero" description confuses this. Perhaps re-wording this sentence to be less all-encompassing (e.g., it currently reads that all of "trial history", as a singular concept, is fixed at zero) would allay potential confusion on part of the average reader.

1a) Note that the utility of the paradigm became clearer as I read the Materials methods section and Results section, but only became very clear once reading the text. It should be clarified before results are even reported, hence the suggestion to adjust (or otherwise qualify) the phrasing of "fixed at zero".

1b) Note that this also has implications for adjusting the commentary introducing the "rational/max-benefit hypothesis"in subsection “Behavioral data – Effects of external cues and cognitive history”. If a reader doesn't understand that randomization is a beneficial manipulation that allows for computational modeling of the internal factor, then it becomes confusing to suggest that on one hand this paradigm allows us to adjudicate between the impact of external and internal factors (or their joint influence/a comparison), but on the other hand, the internal factor (in its entirety, as is currently suggested) is set to zero, thus the max-benefit hypothesis amounts to explicitly externally-driven processing. The typical reader might wonder: How could the internal factor be part of the adjudication if it's set to zero? Conversely, if there is some discoverable aspect of the internal factor, how could it be discounted from the rational hypothesis (in principle, not mathematically)?

Reviewer #3:

The reply of the authors clarified my concerns. I have only a few further comments.

It is now clearer what the authors meant for internal prediction. The use of the word "prediction" both for internal and external prediction misguided me to think that both predictions would be explicit, i.e., the subject would be aware of the prediction. The authors argue that this is not the case: while the cue-based prediction is explicit, the internal prediction is implicit and likely unconscious. Even more: the authors suggest the possibility of a dissociation between an explicit internal prediction vs. an implicit internal prediction.

For the sake of clarity, the authors may emphasize the qualitative distinction between the two types of predictions also in Introduction and Materials and methods section. Otherwise, the reader might realize it only in discussion. This detail seems important for a correct interpretation of the findings and the paradigm.

Besides, hot hand vs. gambler fallacy both depart from a correct interpretation of chance but the violations go in opposing directions. The major driver of the difference between the two is the belief of the subject about the situation. If she is assuming that the generation of events is random (as in the casino) then she will fall for the gambler fallacy, if she assumes that the generation is not random (as for a basket player) then she may fall in the hot hand fallacy. What do the subjects believe in your task? You did not provide any information on the way sequences are generated, thus in principle participants may hypothesize any of the two. Given the task context, it is likely that the subjects assume a random generation. Thus, they would show the gambler fallacy if asked for an explicit prediction. The effect does not emerge because subject's behavior is dominated by the implicit effect discussed above. If the authors think so, then the mention of the hot hand may be removed.

The fact that subjects relied more on internal predictions might follow from the fact that there was a low/no incentive in performing the task as fast and accurate as possible. In fact, given that there is no incentive subjects may rationally decide to rely more on the cheaper prediction from the sequence, rather than on the most cognitively expensive prediction from cue. Given that, the balance between the two types of prediction might be specific for this task context and it should be generalized with caution.
