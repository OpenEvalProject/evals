# Peer review - Round 1

Editors:
- Megan R Carey, Champalimaud Foundation Portugal

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.36781.021](https://doi.org/10.7554/eLife.36781.021)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "A cerebellar role in evidence-guided decision-making" for consideration by eLife. Your article has been reviewed Richard Ivry as the Senior Editor, a Reviewing Editor, and three reviewers. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This is an interesting study describing a potential role for the lateral posterior cerebellum in a novel decision-making task. The cerebellum has received much less focus than cortex in decision-making research despite clear evidence from, among other sources, human imaging and lesion studies that the cerebellum is involved in a wide range of cognitive processes. There is also a rich tradition of theoretical modeling inspired by the cerebellum's unique circuit organization and role in sensorimotor coordination that appears potentially relevant to many cognitive operations, raising interesting questions about what the cerebellum might contribute to decision-making. Therefore, the approach and data reported in the current manuscript are promising and could provide meaningful novel insight into the neural basis of decision-making. Despite this potential, and that it does report some interesting observations, the main limitation of this work is that it is hard to say what the cerebellum is doing during the task. In particular, it is not clear that it is possible to conclude that the cerebellum is truly involved in evidence accumulation. The concern about the support for evidence accumulation holds for the inactivation experiments as well as for the imaging.

Essential revisions:

1) Inactivation results: Inactivation results are suggestive of an important role for the cerebellum in this task. However, from the data presented, it is not clear that it is possible to conclude that the cerebellar inactivations are interfering with evidence accumulation itself, and not just somatosensation or motor output. At a minimum, the authors should show psychometric curves for the 5 individual muscimol-treated animals. Assessing the effects on the slopes and offsets of the individual psychometric curves might be more revealing about which aspects of task performance were affected by inactivation of crus I. Further, there is the possibility that with this experimental design, muscimol inactivation may not be adequate to determine whether the cerebellum is accumulating evidence, because changes in the psychometric function can also be explained by a decrease in sensory sensitivity alone. Careful modeling of the data may help.

2) Evidence for evidence accumulation signals from imaging of somatic calcium in Purkinje cells: The authors report that appear similar to evidence-dependent and choice-selective ramping responses previously reported in many cortical and subcortical areas of primates and rodents. The manuscript reports temporal dynamics of Purkinje cell somatic calcium signals that, in many cells, manifest as a gradual ramping response during the cue period that is correlated with both the number of pulses on one or the other side (evidence) and/or the animal's eventual response (choice). These responses are interpreted with analogy to the ramping responses in trial-averaged spike rates recorded from parietal cortex (along with other forebrain regions) that are thought to encode the time-integral of sensory evidence. However, the manuscript does not convincingly demonstrate that cerebellar neurons are actually encoding accumulated evidence. In general, given the uncertainty about the origin of these signals, more caution is warranted in interpretation of the apparent ramping signals. Specifically:

a) While there appear to be lots of time-modulated signals, the link to evidence accumulation and choice is not clear. It is apparent that the most salient feature of the recorded cerebellar population is a constant modulation, either upwards or downwards, with the passage of time in the trial. The presence of this signal complicates the interpretation of any ramping activity as being attributable to evidence accumulation. However, the statistical analyses (i.e. the linear model reported in subsection “Neuronal signatures of choice and evidence in Purkinje cells”) ignore this component of the responses. This might be valid if the representation of time were truly independent from the representation of evidence. But no such independence is established. For example, cells that are more strongly driven by evidence might also be more strongly driven by time, or more likely to be driven by time in one direction or another. The authors should more carefully consider the relationship between the different components of the cerebellar responses and/or formally control for potentially confounding effects of the time-related responses in the statistical models.

b) Given the temporal resolution of the calcium indicator, it is difficult to interpret any evidence-related signal dynamics as reflecting an underlying ramp in neuronal firing rate. The original description of the use of somatic calcium imaging to track changes in Purkinje cell simple spike rate (Ramirez and Stell, 2016) found that these signals were so slow that step changes in simple spike rate could result in ramps of fluorescence like those seen here. This technical concern would best be addressed by at least some recordings comparing the calcium signals to simple spike rate with electrophysiology. Although the authors have tried to be careful in their writing, the text currently leaves plenty of room for misinterpretation by less technical readers. They should clarify the text further to be much more clear about the limitations of interpreting the temporal dynamics of the calcium signals.

c) The relevant decision variable in the pulse accumulation task is the *difference* in pulses between the two sides. The authors seem to know this point well based on how they plot the psychometric functions. Yet at best a small minority of Purkinje cells encode this value. Subsection “Neuronal signatures of choice and evidence in Purkinje cells” reports that 39/843 cells (less than 5%) encode either a sum or difference of the number of pulses on each side. The specific figure for the number of cells encoding a difference is not reported, but Figure 3 suggests that it is about 5 cells (so ~2% of evidence-modulated cells or ~0.5% of all cells). These numbers question strong conclusions about the representation of the decision variable and accumulated evidence in cerebellum. Further, this result could be taken to show that responses in rodent cerebellum are different from those in primate cortex that are often interpreted as a representation of the decision variable for perceptual discrimination. Notably, it also indicates a dissociation between rodent cerebellum and neocortex, as Scott et al., estimate that as many as 1/3 of evidence-modulated cortical cells are better explained by the difference between sides. Therefore, the data strongly suggest that the critical decision-making operations are actually implemented downstream of the recorded cerebellar population. This strikes me as highly relevant to how the overall results should be interpreted, and it should be emphasized more strongly in the summary and discussion.

d) The analysis of the representation of accumulated evidence (subsection “Neuronal signatures of choice and evidence in Purkinje cells” and Figure 3) ignores the time course of representation, focusing on a short window immediately before the decision. Even if we disregard technical problems explained above in 2a-c, it is unclear whether the cerebellar neurons represent integration of evidence over time or merely its final outcome. Note that the population analysis for the representation of evidence (Figure 2F) does not answer this question (and is generally not quite informative) because evidence is defined as the "correct" choice in that analysis rather than the magnitude of evidence (#R-#L).

3) "Error-related" dendritic responses

In addition to somatic calcium signals, the authors analyzed dendritic calcium signals and found that these were higher on error vs. correct trials. The implications of this observation are emphasized heavily; for example, the Discussion section concludes that "the cerebellum, which learns from error to guide action, may help in the learning and tuning of accurate responses". This is an interesting proposal, but one might have had the same belief prior to seeing the results reported here (given existing human data and theories about the cerebellum), and it's not clear how the data should update it.

a) There is speculation about how the observed error responses could be used as error signals to guide learning, in line with existing models of cerebellar learning. However, it was not clear to the reviewers how that would work, especially given that the error responses observed were not directional. Typically, Purkinje cell complex spikes are thought to provide a directional signal for learning, not just a correct/ incorrect signal. There are no analyses to support the proposed functional role of these error related responses as being involved in "tuning" responses or correcting errors. Yet, it should be possible to provide a more thorough analysis of the error signals:

What do error signals predict about future behavior? An obvious analysis would be to ask whether the magnitude of the error signal on trial n−1 influences choice accuracy on trial n. This seems to be a clear prediction from the proposal that the cerebellum "tunes" behavior or "corrects errors".

c) How do the error signals relate to the strength of evidence on each trial? This is briefly mentioned at the end of the Results section and in Figure 4—figure supplement 1, but without any statistical tests or interpretation. Whether and how the error signals are modulated by the strength of evidence seems key to determining their functional role in updating behavior, if any. In particular, we would have expected that true "error" responses would be higher for easier trials, but the opposite appears to be true.

4) Ruling out sensory and motor confounds as potential sources of somatic and dendritic calcium signals

a) Figure 3B indicates that isolated puffs produce a calcium response that gradually rises and falls over ~1 s. On trials with strong evidence, these signals will overlap. Assuming that they sum reasonably linearly, overlapping calcium responses from neurons that encode only the transient presentation of evidence would nevertheless give the impression of a gradual ramp with a slope that depends on the quantity of evidence. Note that this is a different issue from the point raised in the Discussion section about distinguishing single-trial ramps from steps. Rather, it makes it unclear whether the evidence-related cerebellar responses correspond to a representation of the momentary sensory evidence or to the magnitude of accumulated evidence that drives choice. This distinction is critical to interpreting proposed neural implementations of evidence accumulation models. One possible way to address this would be to record responses during stimulus presentation from animals that are not engaged in making a decision.

b) The authors attempt to rule out that the somatic signals are related directly to movement of the animal and less related to the "cognitive" variables. The analysis in the supporting figures is in line with the level of detail often applied in the field currently. But, is it possible that the activity is related to other movements of the animal rather than in the orofacial region? The authors should either cite strong evidence showing that these are the only relevant regions for the area of cerebellum examined or provide additional videography results from other parts of the body (e.g. paws). This is of course a significant point to make as strong as possible given the cerebellum's long-established role in motor behaviors.

c) The analyses in Figure 4—figure supplement 1 do not convincingly rule out the possibility that the difference in dendritic calcium signals on error trials resulted from differences in licking on error trials. That figure clearly shows that cessation of licking proceeds at different rates on error trials compared to other times. How does trial type (correct vs error) affect the relationship between licking (or changes of rate in licking) and dendritic calcium signals?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A cerebellar role in evidence-guided decision-making" for further consideration at eLife. Your revised article has been favorably evaluated by Richard Ivry (Senior Editor), Megan Carey (Guest Reviewing Editor), and two reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

The authors have made a concerted effort to clarify the text of their paper and have provided reasonable responses to many of the points raised. As was noted in the first round of reviews, rebuttal, and in the text, it remains unclear what the cerebellum's specific role or computation is during the task, and the reviewers were somewhat disappointed that most of the key questions are deferred to future studies. However, the reviewers also felt that defining cerebellum's exact role in the task may be asking too much for a first study, particularly given the limitations of the dataset and the conceptual and analytical complexities that prevent the authors from specifying the nature of neural representations and the source of the behavioral deficit following cerebellar inactivation.

Overall, there are several interesting leads about the role(s) of cerebellum in perceptual decisions in this paper. While none of these are firmly established by the current study, the reviewers agree that the writing and presentation of the results is generally fair and not greatly over-stated, and favor publication so that the results can be evaluated by the field and followed up in future studies from other groups.

The reviewers note that in the process of clarifying what can and cannot be claimed based on the existing data, the scope of the paper is limited to three points: successful training of mice to do the task, reduced accuracy following cerebellar inactivation, and representation of task-relevant variables in cerebellar neural population without specifying the exact nature of the represented variables. Before publication, the reviewers agree that it is important to ensure that after toning down its claims, the manuscript does not leave behind any statements that could mislead readers as to what is actually shown. The reviewers have identified the following statements from the Title, Abstract, and Discussion section that are potentially misleading and should be restated with more specific statements that more accurately match the conclusions that can be supported by the data.

Title

A cerebellar role in evidence-guided decision-making.

Impact Statement

The lateral posterior cerebellum participates in evidence-accumulation-based decision-making, and Purkinje neurons in this region encode choice-, evidence-, and error-related variables. [Suggest replacing this stronger statement with language more like that used in the rebuttal, such as "choice- and evidence-related information is present in lateral posterior cerebellum and could participate in decision-making computations during a decision-making task involving evidence accumulation."].

Abstract

- Here we show that during perceptual decision-making over a period of seconds, decision-, sensory-, and error-related information converge on the lateral posterior cerebellum in crus I, [The presence of task-related signals is shown. Convergence is not, and decision and sensory signals are not clearly dissociated].

- Demonstrated that cerebellar inactivation reduces behavioral accuracy without impairing motor parameters of action [Not all motor parameters were controlled for].

- We found that Purkinje cell somatic activity encoded choice- and evidence-related variables [Please avoid the suggestion that the specific variables that are encoded have been determined].

- Decision errors were represented by dendritic calcium spikes, which are known to drive plasticity [This could misleadingly suggest that they are known to drive plasticity in this context].

- We propose that cerebellar circuitry may contribute to the set of distributed computations in the brain that support accurate perceptual decision-making. [Should be more focused on task performance].

Discussion section

- Cerebellar inactivation reduces animals' use of evidence and increases their use of choice history. [given the limitations of the interpretation of the inactivation experiments, this statement should be more conservative].

- Given the temporal resolution of calcium measurements, our somatic signals may correspond to firing rate ramps (Shadlen and Newsome, 2001), steps (Latimer et al., 2015), or more complex response profiles that form a temporal basis for evidence accumulation (Scott et al., 2017). [This statement, as well as the corresponding section of the Results section, should include an explicit reference to the time course of somatic calcium signals from Purkinje cells, which is at least an order of magnitude slower than typical calcium imaging (Ramirez and Stell, 2016).].

-The task-modulated activity we observe encodes both choice-related and evidence-related variables that may be used during the decision-making process. [Please avoid the suggestion that the specific variables that are encoded have been determined].

- We observed an excess of dendritic calcium events coincident with decision errors, demonstrating for the first time observations compatible with error-associated signalling in a decision-making reward context. [Given the limitations of the interpretation of these signals, this statement should be more conservative].

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Cerebellar involvement in an evidence-accumulation decision-making task" for further consideration at eLife. Your revised article has been favorably evaluated by Richard Ivry (Senior Editor), and Megan Carey (Guest Reviewing Editor).

The manuscript has been improved but there are some final issues that need to be addressed before acceptance, as outlined below:

In response to the request to re-evaluate the evidence for ramping signals that could be obtained with the somatic calcium imaging, the authors now state (Subsection “Purkinje cell somatic calcium encodes task-relevant information”), "Therefore our observed increasing and decreasing time courses of calcium could reflect various firing rate profiles, such as impulse responses, ramps, or steps."

In light of this revision, as well as the fact that the electrophysiological evidence provided in Figure 2—figure supplement 2 is from only a few cells, all of which show positive ramps of activity, the following statements should also be revised:

- (Subsection “Purkinje cell somatic calcium encodes task-relevant information”), "We did find that electrically recorded Purkinje cells exhibited gradually increasing rates of firing throughout the cue period (Figure 2—figure supplement 2), suggesting that on average across trials, the fluorescence signals we observed correspond to firing rate ramps."

- (Discussion section), "Our electrical recordings also showed ramps, suggesting that temporally filtered firing rate ramps are sufficient to account for our observed fluorescence signals."

In both instances, we suggest removing the second clause, starting with "suggesting that…"

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Cerebellar involvement in an evidence-accumulation decision-making task>" for further consideration at eLife. Your revised article has been favorably evaluated by our editors again, but there remain some issues that need to be addressed before acceptance, as outlined below. Given that this is the third request for revisions, we will be unable to follow with any more. Please attend to this final issue one way or the other so that the next letter will be the final one.

We appreciate the authors' desire to speculate here. However, in our view, the "suggests/ consistent with" was not the only problem with this sentence. There is also a problem with "sufficient". The electrophysiological evidence in Figure 2—figure supplement 2 is anecdotal and non-quantitative. For this statement to be left in, it would need to be adequately supported. In our view, this would require a quantitative comparison between imaging and electrophysiology results. In particular, we would want to know:

- How many Purkinje cells in total were recorded from electrophysiologically? How many of these showed ramping? (all of the cells they showed us show positive ramps, but it is not clear if those were selected from a larger data set)

- Did any Purkinje cells show ramping calcium signals without a transient increase in firing rate?

- Did any Purkinje cells show ramping calcium signals without ramps in firing rate (for instance, in cases where only a transient increase in firing may have been observed electrophysiologically)?

- Why are no decreasing activity ramps found with electrophysiology, but they are found with imaging?

- What accounts for the decreasing ramps that were observed with calcium imaging?

- What would the predicted calcium signals be for the examples shown if the spike rates recorded electrophysiologically (with and without the transient increase/ ramping components) were convolved according to Ramirez and Stell (2016)? And/or with the authors' own convolution/ deconvolution methods, from the simultaneous calcium imaging/ electrophysiological recordings that they performed?

We give the authors the choice of either fully addressing these points, or using compromise language, such as "Preliminary electrical recordings also showed ramps, consistent with the idea that temporally filtered firing rate ramps may account for the observed fluorescence signals."
