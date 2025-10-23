# Peer review - Round 1

Editors:
- Tadeusz Wladyslaw Kononowicz, Cognitive Neuroimaging Unit, CEA DRF/Joliot, INSERM, Université Paris-Sud, Université Paris-Saclay, NeuroSpin center France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62825.sa1](https://doi.org/10.7554/eLife.62825.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The authors show a novel and important finding that participants use self-knowledge to optimize learning. Participants in a time estimation task used post-response information about their temporal errors to optimize learning. This is evident in the neural prediction error signals that indexed deviations from the intended target response. This work nicely integrates reinforcement-learning, time estimation and performance monitoring.

Decision letter after peer review:

Thank you for submitting your article "I knew that! Response-based Outcome Predictions and Confidence Regulate Feedback Processing and Learning" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Tadeusz Wladyslaw Kononowicz as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Richard Ivry as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Simon van Gaal (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors tested 40 human volunteers in a time production task and post-production performance evaluation (with an initially unknown target duration and feedback scale) while recording EEG. The authors tested the hypothesis that confidence (both its absolute value and its calibration to performance) have an effect on learning and that it affects the processing of reward and sensory prediction errors.

The reviewers all found the results to be interesting and the work was well-conducted. At the same time the reviewers agreed that the authors should be able to address several issues and clarify multiple aspects of the task, performed analyses, and data interpretation. The comments were compiled into essential revisions where we summarize the remarks that should involve additional data analysis and those proposing changes in the manuscript.

Essential revisions:

Additional analyses:

1. The authors analyze correlations between Error Magnitude, Predicted Outcome and Confidence, however before proceeding to analysis of ERPs the manuscript could be improved by including similar analysis of confidence correlations with RPE and SPE, beyond the one relying only on Predicted Outcome (Table 1).

2. Related to point 1, panel 3A should belong to Figure 1, especially if analyses proposed in the first point are included.

3. The authors showed that Error Magnitude decreases on average. However, all ERP analyses were focused on the current trial. If these ERP signals indeed reflect some "updating of internal representations" they should have a relationship with the behavior or neural measures observed on the next trial. It would've been very interesting to see how the processing of feedback (in behavior and ERP responses) relates to performance on the next trial. These analyses should better support the claims of "updating of internal representations", which would considerably improve in impact and quality if these analyses will be reported.

4. Plausible changes of precision (variance) of temporal performance over the course of experiment. Variance dynamics across experimental session could affected the outcome of the confidence calibration. The authors rightfully show that Confidence Calibration was not related to Average Error Magnitude. The same check should be performed for Time Production variance. Moreover, the effects within participants and over the course of experiment should be considered and presumably included as covariates in the LMM.

5. Specific point from one of the reviewers: The authors mention again on page 24: "We also found that confidence modulated RPE effects on P3b amplitude, such that in initial blocks, where most learning took place, RPE effects were amplified for higher confidence, whereas this effect reversed in later blocks, where RPE effects were present for low, but not high confidence. This shift is intriguing and may indicate a functional change in feedback use as certainty in the response-outcome mapping increases and less about this mapping is learned from feedback, but the effect was not directly predicted and therefore warrants further research and replication." This is the one result where confidence interacts with other behavioral measures, in this case RPE, which is interesting, however it does so in an unpredicted and counterintuitive way. I wonder whether the authors can in some way get a better understanding of what's going on here? Possibly the paper by Colizoli et al. (2018, Sci Rep.) may be relevant. The authors here show how task difficulty (related to confidence) and error processing are reflecting in pupil size responses.

Other reviewer raised concerns on how different Confidence splits were computed. Although, the authors provide and an intriguing interpretation reference in the paragraph above, is it possible that the early and late effects originate in fact from different group of subjects?

To sum up, extending the analyses with respect to the interaction of confidence and RPE in modulation of P3b component would strongly benefit the manuscript.

6. There is not explicit statement on what exact instructions were given to participants beyond the following one: "participants were required to predict the feedback they would receive on each trial". The caption of Figure 1B says that "scaled relative to the feedback anchors". Therefore, it is not clear what was the primary objective of the task – accurate time production or predicting the feedback accurately? Participants could have increased time production variance to perform better on feedback prediction. If participants employed that kind of strategy that could have impact indices of learning from feedback.

Given the lack of clarity of what instruction was provided to participants it is still unclear on which aspect of the task the participants focused on in their learning. Error Magnitude decreases over trial, however does RPE and SPE increase over trials as well?

Reshaping the manuscript:

1. It was evident from all reviews that at many places an explicit link between interpretative statements and performed analyses were far from clear. Below we list a few specific examples:

– "Taken together, our findings provide evidence that feedback evaluation is an active constructive process that is fundamentally affected by an individual's internal representations of their own performance at the time of feedback." I wonder what results the authors refer to here and on what results this statement is based on.

– The authors say "In line with the notion that positive feedback is more informative than error feedback in motor learning, we, like others in the time estimation task (65,66), observed increasing P3b amplitude after more positive feedback, in addition to prediction error effect". It is not clear which outcome the authors are referring to. Is "better than expected" referred to as "positive feedback"? In this case "worse than expected" triggered higher P3b amplitude.

– On page 24 the authors conclude that "Learning was further supported by the adaptive regulation of uncertainty-driven updating via confidence." Although this sounds interesting I do not see the results supporting this conclusion (but maybe I have missed those). I also think this conclusion is rather difficult to follow. The sentence thereafter they say "Specifically, as deviations from the goal were predicted with higher confidence, these more precise outcome predictions enhanced the surprise elicited by a given prediction error. Thus, a notable finding revealed by our simulations and empirical data is that, counterintuitively, agents and participants learned more from feedback when confidence in their predictions had been high." Also here I have difficulty extracting what the authors really mean. What does it mean "surprise elicited by a prediction error"? To me these are two different measures, one signed one unsigned. Further, where is it shown that participants learn more from feedback when confidence in their prediction was high?

– Differences between blocks in the effect of confidence. This result is discussed twice: in the Results (p. 19) and Discussion. Only in the latter do the authors acknowledge that their interpretation of the effect is rather speculative. I would also flag that in Results, as it was neither part of the model predictions or their design.

2. Performed transformations involving confidence should be clearly explained.

3. Model specification (the formula) should be included in the table legend to aid readability and interpretation as it makes it immediately clear what was defined as a random or fixed effect.

4. On more conceptual level, the authors rely on the assumption that 'Feedback Prediction' is derived from efference copy, which carries motor noise only. In light of the goal of the current manuscript, that is an appropriate strategy. However, I think it should be acknowledged that in the employed paradigm part of behavioral variance may originate from inherent uncertainty of temporal representations (Balci, 2011). Typically, time production variance is partition into a 'clock' variance and 'motor' variance. I have a feeling that this distinction should be spelled out in the manuscript and if assumptions are made they shall be spelled out clearer. Moreover, recent work attempted to tease apart origins of 'Feedback Predictions', indicating that it is unlikely that they originate solely from motor variability (Kononowicz and Van Wassenhove, 2019).

5. The main predictions of the experiment are described in the first paragraph of the Results. But they are not reflected in Figure 1, which is referenced in that paragraph. I would have expected an illustration of the effects of confidence, and instead that only appears on Figure 2. The authors have clear predictions that drive the analysis, but this is not reflected in the flow of the text.

6. Simulations (Figure 2. B, D): As far as I can tell, the model does not capture the data in two ways: it fails to address the cross-over effect (which the authors address) but also does not account for the apparent tendency of the data to increase the error on later trials (whereas the model predict a strict decrease in error over the course of the experiment). The second aspect is not addressed in the Discussion, I think (or I missed it). Do the authors think this is just fatigue, and therefore not consider it as a reason to modify the model? Also Panels 2.A. And C do not really match in the sense that the simulation is done over a much wider range of predicted outcomes. It seems like the model parameters were not fine-tuned to the data. Perhaps this is not strictly necessary if the quantitative predictions of the effects of confidence remain unchanged with a narrower range, but it is perhaps worth discussing.

7. "… it is unknown whether reward prediction errors signaled by the FRN rely on predictions based only on previous feedback, or whether they might incorporate ongoing performance monitoring". I think that phrase should be rephrased based on the findings of Miltner et al. (1997), correctly cited in the manuscript, which showed that FRN was responsive to correct and incorrect feedback in time estimation.

8. Relevance of the dart-throwing example: In the task, participants initially had no idea about the length of the to-be-reproduced interval, and instead had to approximate it iteratively. It was not immediately clear to me how this relates to a dart-throw, where the exact target position is known. I think I understand the authors that the unknown target here is "internal" – the specific motor commands that would lead to a bulls-eye are unknown and only iteratively approximated. If that interpretation is correct, I would recommend the authors clarify it explicitly in the paper, to aid the reader to make a connection. Or perhaps I misunderstood it. Either way it would be important to clarify it.

Balci, F., Freestone, D., Simen, P., Desouza, L., Cohen, J. D., and Holmes, P. (2011). Optimal temporal risk assessment. Front Integr Neurosci, 5, 56.

Colizoli, O., De Gee, J. W., Urai, A. E., and Donner, T. H. (2018). Task-evoked pupil responses reflect internal belief states. Scientific reports, 8(1), 1-13.

Correa, C. M., Noorman, S., Jiang, J., Palminteri, S., Cohen, M. X., Lebreton, M., and van Gaal, S. (2018). How the level of reward awareness changes the computational and electrophysiological signatures of reinforcement learning. Journal of Neuroscience, 38(48), 10338-10348.

Kononowicz, T. W., and Van Wassenhove, V. (2019). Evaluation of Self-generated Behavior: Untangling Metacognitive Readout and Error Detection. Journal of cognitive neuroscience, 31(11), 1641-1657.
