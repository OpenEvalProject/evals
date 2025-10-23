# Peer review - Round 1

Editors:
- Doris Y Tsao, California Institute of Technology , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.12215.018](https://doi.org/10.7554/eLife.12215.018)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "Active sensing in the categorization of visual patterns" for consideration by eLife. Your article has been favourably reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors. The evaluation has been overseen by this Reviewing Editor and Eve Marder as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Having conferred about this paper, we agree that it is acceptable for publication pending revision. However, there was an extended discussion among the reviewers about the extent to which the current results apply to natural vision. The reviewers agree that the authors need to qualify their conclusions to clearly state that while they were trying to emulate natural vision, their task was unnatural in several important ways (e.g. very small exposures, uniform statistics, small saccades not allowed, and reviewing for up to 60s after presentation in the passive conditions), all of which may have changed the participants' strategy from that used in natural vision. Natural vision works under entirely different constrains – larger exposures, natural scene statistics, all saccades allowed, and limited time. Under these constrains the selection of targets may (or may not) be completely different. These differences between the paradigm used in the study and natural vision should be carefully discussed, and relevant parts of the Abstract and Discussion should be modified accordingly.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The previous decision letter after peer review is shown below.]

Thank you for choosing to send your work entitled "Active sensing in the categorization of visual patterns" for consideration at eLife. Your full submission has been evaluated by Eve Marder (Senior editor) and three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the decision was reached after discussions between the reviewers. Based on our discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

While all of the reviewers appreciated the significance of the work, they were very concerned about potential confounds due to letting subjects continue viewing the display for 60s after the last revealing. Given this confound, the reviewers were not certain that a revision would adequately deal with this problem, which led to the decision to reject the paper at this time. If you feel you can adequately answer the concerns of this review, the reviewers were sufficiently potentially positive about your manuscript that eLife would allow a submission of a new manuscript that addresses these concerns.

Reviewer #1:

Summary

The present work utilizes an innovative gaze-contingent paradigm where subjects have to identify the category of a texture and can actively reveal locations based on where they saccade to. The authors compare the fixation density maps for the three different stimulus categories and find that they are consistent and category-specific across participants, i.e. each stimulus category evokes a specific pattern of fixations. When revealing locations randomly controlled by the computer the categorization performance decreases indicating that active sensing does increase the information yield for the participants. Next, they construct an ideal observer model that computes the posterior probability of each category given the revealed pixel values, and fit the parameters prior bias, perception noise and decision noise to predict the subject's choice of category. Based on these parameters fitted to the subject's category choice the authors try to predict saccade choices using a Bayesian active sensor algorithm which chooses the saccade location which maximizes the expected information gain, taking into account saccade inaccuracies. They claim that the subject's saccades are predicted well by their Bayesian active sensor algorithm, as the predicted category-specific fixation density maps are significantly correlated with the actual density maps. As a better measure of the goodness of their model they compare the information (in the ideal observer sense) gained by the subject's saccades to the information gained by their simulated saccades, random saccades and saccades based on other strategies. They find that the information gained by the subject's saccades is higher than random saccades and saccades based on three heuristic strategies but lower than the information of the saccades simulated by the Bayesian active sensor, even if prior bias, perception noise and category decision noise are taken into account. They call the latter discrepancy a 30% inefficiency of saccade choice. To show that the saccade choices made by the subject are indeed not optimal in efficiency of making the category choice, they reveal the fixation locations computer-controlled based on the optimal locations predicted by the active Bayesian sensor model without biases and low noise. Thereby, the subject's categorization performance is increased. The efficiency of saccade choice does not vary over time, so there does not appear to be any learning.

Remarks

1) In Figure 1, it is not clear to me, why the patch surrounded by the red circle should have more information about zebra vs. cheetah than other blue patches, so maybe use a better example.

2) In Figure 2C, the blue condition titled Random should be called passive or computer-controlled random locations to avoid confusion. Also, please clarify the term "gaze-contingent".

3) In Formula 1, D is not defined.

4) Regarding Figure 4B, I don't understand why the first term of the formula isn't maximal at locations as far as possible from previous locations (i.e. on the borders of the image). Given that spatial correlations of the stimulus decrease with distance, the uncertainty about pixel values at a far distance from known pixel values should be highest.

5) The correlation analysis done in Figure 3 should be repeated with simulated entropy-maximizing saccades, to show that the correlation analysis is meaningful. Just correlating the fixation density maps might not be the best measure to evaluate fit of the simulation, since it does not consider each fixation on a case-by-case basis given the prior information from previous saccades.

6) In addition to the BIC it would be nice to know the cross-validated prediction accuracy of category choice on a testing set.

7) Also, when showing the performance decrease when revealing at random locations, I would have matched the inter-saccadic distribution (including the variance) and the saccadic distance distribution, to ensure the performance decline is not due to the variance in fixation duration or the subject needing to recover from longer saccades.

Reviewer #2 (General assessment and major comments (Required)):

The paper addresses the strategy underlying the selection of gaze targets along the scanpath of fixations. Specifically, the paper compares human selections and performances with those of an optimal Bayesian algorithm. The authors conclude that while humans employ an information-based strategy, this strategy is sub-optimal. They also identify the sources of this sub-optimality and suggest that "participants select eye movements with the goal of maximizing information about abstract categories that require the integration of information from multiple locations".

This is potentially an important paper, which can contribute significantly to the understanding of perceptual processes. The topic is important, the work is, for the most part, elegant and the paper is in general well written. However, there are several crucial points that question the conclusions reached by the authors – these and other comments are listed below.

1) The authors employ a reductionist method, which is indeed necessary if one wants to reveal underlying mechanisms. However, some of the reductionist choices made in this work fuel the questioning of several of its conclusions. The most concerning reductionist steps are:

A) Small saccades (< 1 deg) were not allowed. The use of small ("micro") saccades is task dependent and it may be the case, for example, that with images like those used here a possible strategy is scanning a continuous region. This possibility was "reduced-out" here.

B) The exposed area was effectively < 0.5 deg and was scaled down in transparency from the center out – this reduced-out a meaningful drift-based scanning of the fixational region.

C) The images had uniform statistics, which preclude generalization to natural images.

The authors mention that "the task still allowed them to employ natural every-day eye movement strategies as evidenced by the inter-saccadic intervals (mean 408 ms) that were similar to those recorded for everyday activities […]" – evidently, normal ISIs do not indicate a natural strategy – a) there is much more into an active strategy and b) ISIs seems to be determined by hard-wired circuits that are only slightly modulated in different contexts – see a variety of tests of ISIs in the last decade.

2) The "last 60s" problem. Natural viewing involves a scanpath of fixations. However, natural viewing does not allow a re-scanning of the collection of previous fixation locations. The design of the trial is thus odd– why were the subjects given those extra 60s at the end of the trial to rescan their revealings? This is not justified in the paper and it is actually hidden, in a way, in the Materials and methods section – it took me some time to understand that this was the case. The implications of this design are significant:

A) How can the authors relate performance to either of the two different phases of the trial (the "acquiring" and the "rescanning")?

B) Even in the "acquiring" phase, how can the authors rule out brief rescanning of exposed revealings for periods shorter than the threshold period?

C) If performance depended on the perception during these 60s, then what was the underlying strategy while rescanning?

The authors must describe the procedure clearly at the outset, relate to all these issues explicitly, and explain how they affect (or not) their conclusions.

3) As indicated by the above, the primary characterization of the active strategy here is about which revealing were or should be selected, and less about when or in what order. True, order was a factor during the acquiring phase, but not during the rescanning phase. Order seems to play a role in the correlations in Figure 3B but it is not clear by how much. The collection of revealing locations may indeed be the most relevant factor when trying to categorize an image out of several known images with known structures. This is, however, not the case in most natural cases, in which real-time information is essential.

4) From the above and from further analysis it appears that the strong statements of the Abstract are not supported by the data in the paper.

A) "Categorization performance was markedly improved when participants were guided to fixate locations selected by an optimal Bayesian active sensor algorithm […]" – this statement sounds as if guiding the next saccade improves performance. This cannot be concluded here because of the "60 s problem" – during rescanning subjects could select any pattern they wanted. Moreover, performance may even depend on the rescanning period only.

B) "By using […] we show that a major portion of this apparent suboptimality of fixation locations arises from prior biases, perceptual noise and inaccuracies in eye movements[…]" – you do not really show this. You show that if you add these imperfections to your model you get performance level that resembles that of the subjects. However, there are so many ways to impair the performance of your model – where do you show that these are the crucial factors?

C) "The central process of selecting fixation locations is around 70% efficient" – this is correct only for the specific task and context of your experiment. The statement sounds much more general than that.

D) "Participants select eye movements with the goal of maximizing information about abstract categories that require the integration of information from multiple locations" – again, a statement with a general flavor without such justification – the statement should be toned and tuned down to reflect the narrow context of the findings.

5) Audience and style. As written now the paper seems to address experts in Bayesian models of perception. Given that it is submitted to eLife I assume that the paper should address primarily, or at least to the same degree, biologists who are interested in understanding perception. And indeed, papers like this form a wonderful opportunity to create a productive dialogue between biologists and theoreticians. For this end, the style of writing must change. The amount of statistical details should be reduced, the biological meaning of the various strategies discussed should be provided, the rational for selecting the BAS algorithm as the optimal strategy should be explained, the meaning of each strategy in terms of actual eye movements in natural scenes should be explained. At the end, the reader should understand the biological meaning of each strategy (that is, a biologically-plausible description of the strategy employed by their subjects in this task, and a strategy they would employ in a natural task), the rational of why one strategy is better than the other, and in what sense humans are sub-optimal.

6) The discussions about active-sensing in the paper are written as if they come from a sort of a theoretical vacuum. Active sensing has been introduced, studied and discussed at various levels for various species and modalities for years, and intensively so for the last decade or two. Nevertheless, the paper sounds as if these concepts are only beginning to be addressed, and as if active vision is mostly covered by addressing saccades scanpath selections. This introduces a huge distortion of the concepts of active sensing and active vision. Active vision is much more than scanpath selections. Eye movements include saccades and drifts, and as far as we know today vision does not occur without the drift movements. Saccades include large and small ("micro") saccades, making a continuous spectrum of saccade amplitudes. In this study only large (> 1 deg) saccades were allowed. Thus, this study ignores a substantial portion of visually-crucial eye movements. While this is ok as a reductionist method, it is not ok to ignore the reduced-away components in the discussion and interpretation of the results. Thus:

A) There is no justification to use the term "eye movements" in this paper – the components of eye movements studied here should be termed properly (perhaps use terms like "fixation scanpath" or "saccadic order" or anything else that is appropriate).

B) Previous results and hypotheses about active sensing/active vision that refer to all kinds of movements must be discussed and referred to when interpreting the current results.

C) The results of the current study should be put in the context of this general active sensing context, and the generality of the conclusions should be phrased accordingly – mostly, they should be toned down and related to the specific reduced context of this study.

Minor comments:

1) Arbitrary selection of parameters – please explain the choice of every parameter you use (e.g., the criteria for saccades and fixations).

2) Figure 3B – please run a shuffling control analysis to show how much of the correlation is order-dependent.

Reviewer #3:

The authors investigated the control of eye movements in a visual categorization task. By using a gaze-contingent paradigm, they could show that eye movement patterns became more specific to the underlying image structure with increasing fixation number. A comparison with a Bayesian active sensor (BAS) model showed that humans were quite efficient, given certain biases and inaccuracies of eye movements.

The study should be interesting to a broad audience and is well conducted. A few further analyses could strengthen the message.

1) The authors corrected for errors in saccade targeting tangential and orthogonal to saccade direction. However, as they correctly stated in the Discussion, there are also other potential sources of errors due to biases along cardinal directions or the bias to fixate the center of an image. It would be very interesting to see how much of the performance reduction is caused by these biases. It should be possible to assess these biases directly from the existing data.

2) Since there were a lot of incorrect judgments overall, it would be interesting to compare the density maps for correct and incorrect judgments. If eye movements are indeed controlled by an active strategy, the differences and correlations should be more pronounced for correct judgments.

3) The example trial in Figure 4 provides a good illustration of BAS and the maximum entropy variant but it does not allow a quantitative comparison. It would be helpful to show the full distributions of percentile values with respect to BAS and entropy scores.

4) As I understand the task, the revealings stayed on screen after the last revealing for 60 s or an unlimited duration, depending on the condition. The behavior of the subjects after the last revealing should be reported because it could have influenced their perceptual judgment.
