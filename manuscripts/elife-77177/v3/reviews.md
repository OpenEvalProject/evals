# Peer review - Round 1

Editors:
- Ishmail Abdus-Saboor, https://ror.org/00hj8s172 Columbia University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77177.sa0](https://doi.org/10.7554/eLife.77177.sa0)

The thalamus is the hub connecting sensory inputs to cortical processing. The elegant study here used 2-photon calcium imaging and behavioral tasks to reveal a role for the posteromedial nucleus of the thalamus in goal directed forepaw behaviors in mice.


---

# Peer review - Round 1

Editors:
- Ishmail Abdus-Saboor, https://ror.org/00hj8s172 Columbia University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77177.sa1](https://doi.org/10.7554/eLife.77177.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Higher order thalamus flexibly encodes correct goal-directed behavior" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Joshua Gold as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) As is, the optogenetic experiments have some weaknesses. It would be helpful if the authors inhibited during different epochs. For example, their interpretation of what the activity during the reward epoch means is unclear. It would help if authors would inhibit POm during reward- if done in naïve animals, is learning affected? Another potential experiment could be to perform imaging in another circuit terminating in S1. Relatedly, reviewers were concerned that POM targets to output areas beyond somatosensory cortex may contribute to the observed optogenetic inhibition experiments.

2) The main conclusion about the role of POM remains unclear, and additional alternatives should be considered. For example, terms like "behavioral flexibility" are used to describe its purpose, but the connection of this term to POm is not explained.

Reviewer #1:

1. Figure 1 – Supp 1 suggests that virus expression was always limited to POm. Drawing borders expressing areas from epifluorescence images is probably very dependent on imaging parameters. The Methods indicate that the authors scaled so that no pixels were saturated. This could mean that there was some weak expression of GCaMP6f or ArchT outside of POm. As I understand it, the authors set exposure/gains by the brightest points in the image. The limited extent of the infection in the figures might just reflect its center, which is brightest, rather than its full extent. If there were GCaMP or ArchT in VPL, some results would need to be reinterpreted.

2. Calcium responses are weaker during the naïve state than the expert state (Figure 1D,E), similar to the start of the reversal training (Figure 4G,H). If POm encodes correct actions, why is there any response at all in naïve mice? Is that not also a sign of stimulus encoding? Might there be another correlate of correctness with regard to the task, such as an expert mouse holding their paw more firmly or still on the stimulating rod? This could alter the effective stimulus or involve different motor signals to POm.

3. The authors are rightly concerned that licking might contribute to POm activity and expend some good effort checking this. The reversal is a good control, but doesn't produce identical POm activity. The other licking analyses, while good, did not completely rule out licking effects. First, lines 110-111 state "…as there was no correlation between licking frequency and POm axonal activity (Figure 1I)", but Figure 1I doesn't seem to support that statement. Second, the authors analyze isolated spontaneous licks, but these probably involve less licking and less overall motion than during a real response.

4. Many figures (Figure 1F, 2B, 3C, 4C) make it apparent that a population of axons respond very early to the stimulus itself. I understand the authors point that many of their analyses show that on average the axons are not strongly modulated by this stimulus, but this is not true of every axon. Either some of these axons are coming from cells outside of POm (see #1) or some POm cells are stimulus driven. In either case, if some axons are strongly stimulus driven, the activity of these axons will correlate with correct choices. The stimulus and correct choices are themselves highly correlated because the animals perform so well. I do not understand how stimulus encoding and choice encoding can be disentangled by either behavior or the two behaviors in comparison. Simple stimulus encoding might be further modulated by arousal or reward expectation that increases with task learning (see #6).

5. I was unable to understand the author's conclusion about what POm is doing. They use terms like "behavioral flexibility" to describe its purpose, but the connection of this term to POm is not explained. Is a role as a flexibility switch really supported? Why does S1 need POm to signal a correct choice? Figure 6 did not seem helpful here. Couldn't S1 just detect the stimulus on its own and transmit consequent signals to wherever they need to be to generate behavior?

6. Arousal or reward expectation may be better explanations than flexibility. Lines 323-324 say that POm activity increased with pupil diameter normally but reversed during reward delivery. Which data support this statement? With regards to pupil, the Results only seem to indicate that there is no difference in diameter between the two conditions (expert and 50% chance) using 3 bins of data. However, I could not find the time windows used for computing these. Pupil is known to be lagged and the timing could be critical.

7. There are other possible interpretations of the results when the authors target POm for optogenetic suppression (around lines 246-248). The effects here are also consistent with preventing tonic and evoked POm activity from reaching lots of target structures other than S1: S2, PPC, motor cortex, dorsolateral striatum, etc. Maybe one of these cannot respond to the stimulus as well and Hits decrease?

8. Line 689. What alerts the mouse that a catch trial is happening? Is there something like an audio cue for onset of stimulus trials and catch trials? If there is no cue, wouldn't mice be in a different behavioral state during catch trials than during stimulus trials? The trial types could differ by more than the presence of the stimulus.

9. Would it be more thorough to zoom in on areas like VPL, set exposures/gains very high, and show that there is no detectable VPL expression or gradient of expression crossing into VPL?

10. The authors indicate that they used video of the paw to exclude trials where the mouse removes the paw entirely from the rod. Why not quantify the paw movements as well and check if the paw is overall moving less in experienced than naïve/switched states? Quantified comparisons of paw stability and calcium are probably also good checks.

11. An analysis that might help would be to check the relationship of lick number/rate and calcium. Third, the authors point out that FA trials have licks but different POm activity (lines 132-134), but the FA and Hit licks may differ in number or frequency. Some check of this is needed.

12. There are many possible ways the authors might address these, and depends on them and the data.

13. Why not just plot the average pupil diameter traces of the two conditions over fairly long time periods?

14. Like 12, the authors may want to deal with these in a variety of ways. On a related note with 7, wouldn't Figure 5E be more informative if latency was broken out by Hits and FAs separately? Related to #1, it would be problematic if the infection had spread into VPL.

Reviewer #2 (Recommendations for the authors):

In this manuscript, D LaTerra et al. explored the function of POm neurons during a tactile-based, goal-directed reward behavior. They target POm neurons that project to forepaw S1 and use two-photon ca2+imaging in S1 to monitor activity as mice performed a task where forepaw tactile stimulation (200 Hz, 500 ms) predicted a reward if mice licked at a reward port within 1.5 seconds. If mice did not lick, there was a time-out instead of a reward. The authors found that POm-S1 axons showed enhanced responses during the baseline period, the response window after the cue, and during reward delivery. They then showed that a subset of neurons were active during the response window during correct trials when the tactile stimulus served as a cue, but not on catch trials where animals spontaneously licked for a reward.

They then showed that POm axonal activity in S1 increased during the response window for "HIT" trials where animals correctly responded to the tactile stimulus with licking but the activity was less during "MISS" trials where animals did not respond. In order to probe whether this activity in the response window was being driven by motor activity, they designed a suppression task in which animals had to learn to suppress licking in response to the tactile stimulus in order to the receive a reward. POm neurons also showed increased activity during the response window even though action was being suppressed. However, this activity was less than during the action task. Thus, although POm activity is not encoding action, its activity is significantly different during an action-based task than an action suppression one. They then analyzed calclium activity during the training period between the action task and the suppression task in which animals were learning the new contingency and were not performing as experts. In this non-expert context there was not a difference between in POm axonal activity between "HIT" and "MISS" trials.

Lastly, they used ArchT to inhibit POm cell body activity during the tactile stimulus and response window of some trials and showed that they reduced performance during the trials when light was on.

Altogether, this paper provides evidence that POm neurons are not simply encoding sensory information. They are modulated by learning and their activity is correlated to performance in this goal-directed task. However, the actual role of the POm input to S1 is not discernable from the current experiments. Subsets of neurons show significant activity during the response window as well as reward. In addition, the role of this input is different during the switch task than during expert performance. There are a number of outstanding questions, which, if answered, would help to directly define the role of these neurons in this specific paradigm. For instance, the authors record specifically from POm axons in S1. How distinct is this activity from other neurons in the POm? Some POm neurons still show significant activity during MISS trials. Do these neurons have a different function than those that show a preferential response during HIT trials? Does POm activity during the switch task, which has a component of extinction training, differ from when the animals are first learning the action-based task? Likewise, are the same neurons that acquire a response during the initial learning of the action-based task, the same neurons that are responding during the action suppression task?

The authors provide great evidence that POm neurons that project to the S1 do not simply encode sensory information or actions, but are instead signaling during correct performance. However, inhibition of cell bodies did not dramatically effect performance and it is still unclear what role this circuit actually plays in this behavior. Finer-tuned optogenetic experiments and analysis of cell bodies within POm may provide greater details that will help define this circuit's role.

1. Perform optogenetic inhibition during specific epochs of task (response window vs reward) in order to better define this circuit's function.

2. Perform optogenetic inhibition during initial training before learning, to assess if this circuit is necessary for learning this task

3. Calcium imaging was done in POm axons in S1 and was not perfomed in POm itself, yet inhibition was done in cell bodies in POm and the functional role of the projection to S1 was not isolated. Recording cell bodies in POm might help to better characterize sub populations of functional ensembles and how they change during learning. Likewise, inhibiting POm axon terminals in S1 would provide a more nuanced functional assessment of the calcium imaging data presented here.

Reviewer #3 (Recommendations for the authors):

In their paper "Higher order thalamus flexibly encodes correct goal-directed behavior", LaTerra et al. investigate the function of projections from the thalamic nucleus POm to primary somatosensory cortex (S1) in the performance of goal-directed behaviors. The authors performed in vivo calcium imaging of POm axons in layer 1 of the forepaw region of S1 (fpS1) to monitor the activity of POm-fpS1 projections while mice performed a tactile detection task. They report that the activity of POm-fpS1 axons on successful ('hit') trials was increased in trained mice relative to naïve mice. Additionally, the authors used an action suppression variant of the task to show that POm-fpS1 axon activity was higher on successful trials over unsuccessful ('miss') trials regardless of the correct motor response required. During transition between task conditions, when mice perform at chance levels, the increase of POm-fpS1 activity during correct trials is no longer seen. Finally, the authors use inhibitory optogenetic tools to suppress POm activity, revealing a modest suppression in behavioral success. The authors conclude from these data that POm-fpS1 axons preferentially "encode and influence correct action selection" during tactile goal-oriented behavior.

This study presents several interesting findings, particularly with respect to the change in activity of POm-fpS1 axons during successful execution of a trained behavior. Additionally, the similarity in responses of POm-fpS1 on both the 'goal-directed action' and 'action suppression' tasks provides convincing evidence that POm-fpS1 activity is not likely to encode the motor response. Overall, these results have important implications for how activity in higher order thalamic nuclei corresponds to learning a sensorimotor behavior, and the authors use several clever experiments to address these questions. Yet, the major claim that POm encodes 'correct performance' should be defined more clearly. As is, there are alternative explanations that could be raised and should be discussed in more depth (Points 1), especially as it relates to any causal role the authors ascribe to POm (Point 2). In addition some clarification as to which types of signals (i.e. frequency of active axons vs. amplitude of signal in the active axons) the authors feel are most informative would be helpful (Point 3).

1) The authors argue that POm activity reflects 'correct task performance' and that the increased activity of POm-fpS1 axons in the response epoch is not due to sensory encoding. An alternative explanation is that POm-fpS1 axons do convey sensory information, and these connections are facilitated with learning – meaning the activity of pathways conveying sensory signals that are correlated with task success could be facilitated with training, and this facilitation could be disrupted during the switching task. In this sense, the activity profiles do not encode 'correct action' per se, but rather represent the sensory responses whose correlation to rewarded action have been reinforced with training (which would also be a very interesting finding). This would be quite distinct from the "cognitive functions" they ascribe to this pathway (line 341). It might have helped to introduce a delay period in between the sensory stimulus and response epoch to try to distinguish responses that encode information about the sensory stimulus from those that might be involved in encoding task performance. However, as is, it is difficult to distinguish between these two scenarios with this data, and thus the interpretations the authors present could be rephrased with alternatives discussed in more depth.

2) Similarly, while the authors attempt to establish a causal role for POm in task performance by optogenetically inhibiting POm during the response epoch, the results are also consistent with a deficit in sensory processing, and cannot be interpreted strictly as a disruption of the encoding of 'correct action' task performance signals. Furthermore, these perturbation studies do not demonstrate that the POm-fpS1 projections they are studying are implicated in the modest behavioral deficits. As the authors state, POm projects to many targets (lines 63-66), and similar sensory-based, goal-directed behaviors do not require S1 (lines 302-305). In light of these points, some of the statements ascribing a causal role for these projections in task success could be rephrased (e.g. line 33 "to encode and influence correct action selection", line 252 "a direct influence", line 340 "plays an active role during correct performance").

3) Event amplitude and probability were both quantified, but were not consistently reported throughout the manuscript and figures. For example, Figure 1 reports both probability and amplitude (Figure 1G and H), whereas Figure 2 only reports probability. Thus, it was not always clear as to whether the authors were ascribing biological significance to one or both of these measures, given that in some cases differences were found in one and not the other, and which of the measures were reported was occasionally switched. It would be helpful for the authors to clarify the significance they assign to each measure, and report both measures side by side for all experiments if they interpret them both as relevant.

4. It was unclear why the authors did not attempt to use deconvolution and report spike probabilities, especially when considering the kinetics of GCaMP6f and the results presented in Figure 4, where event amplitude and event probability changed in opposing directions, which could reflect a change in burst firing since spikes in short high frequency bursts can appear as a single large amplitude event compared to single spikes. The authors could consider performing further analysis or discuss the caveats of analyzing the Ca signal across these large time windows.

5. It would be helpful to clarify the basis upon which boutons or ROIs were excluded when determining the 'axon subset' of ROIs. How did Ca event probability, event amplitude, and event duration compare between ROIs that were assessed as being from the same axon? It was unclear what was deemed as 'similar activity profiles' for the exclusion of ROIs. It might help to include an additional figure supplement to Figure 1 showing the ROI correlations and exclusion criteria with images showing 'similar' or 'dissimilar' ROIs marked on an example field of view.

6. The heterogeneity of POm axons was briefly shown (Figure 1) but not discussed or explored in depth. It was unclear how the authors interpret the observation that a subset of POm-fpS1 axons showed a larger increase in the reward epoch compared to the stimulus and response epochs. While this diversity in responses could be relevant to their claim that POm-fpS1 axons encode task performance, the authors did not perform experiments inhibiting POm during the reward epoch, leaving unclear the interpretation of what the reward epoch responses might mean. More discussion of the interpretation of POm-fpS1 activity during the reward epoch would be helpful, given that several sections of the Results are dedicated to this point. Also, a clearer descriptions of row sorting in the figures (e.g. Figure 2B) would enable more direct comparison of activity of the same axon across different trial types.

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the second round of review.]

Thank you for resubmitting the paper entitled "Higher order thalamus flexibly encodes correct goal-directed behavior" for further consideration by eLife. Your revised article has been evaluated by a Senior Editor and a Reviewing Editor. We are sorry to say that we have decided that this submission will not be considered further for publication by eLife.

Although reviewers acknowledge improvement in the clarity of the manuscript, key experiments that were requested were not performed, such as inhibiting during different epochs or in naïve animals. Moreover, a major issue that was raised in the first round was to clarify what function the authors are ascribing to POm. Although the reviewers acknowledge improvement in language, the reviewers all felt that it is still not clear why Pom is needed to signal correct performance, and the data do not exactly support the conclusion that POm=correct.
