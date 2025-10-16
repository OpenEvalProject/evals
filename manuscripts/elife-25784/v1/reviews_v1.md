# Peer review - Round 1

Editors:
- Nicole Rust, University of Pennsylvania United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.25784.030](https://doi.org/10.7554/eLife.25784.030)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Dynamic representation of partially occluded objects in primate prefrontal and visual cortex" for consideration by eLife. Your article has been favorably evaluated by David Van Essen (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this letter to crystallize our concerns going forward. We feel the work is important and interesting but key issues remain unresolved that must be addressed satisfactorily to produce an acceptable manuscript.

At this point we are unable to render a binding recommendation and require a response from you indicating the feasibility of your completing the essential tasks in a reasonable period of time – around 2 months. The Board member and reviewers will consider your response and provide a binding decision.

General assessment:

This paper characterizes responses of V4 and vlPFC neurons to partially occluded visual stimuli and suggests that feedback from vlPFC to V4 boosts V4 responses to occluded shapes and helps resolve stimulus identity. The authors recorded vlPFC and V4 neurons from the same monkeys performing the same task, although in separate experimental sessions. They demonstrate that vlPFC neurons respond more strongly and more selectively to occluded stimuli, unlike V4 neurons, which commonly respond most strongly and selectively to unoccluded images. The authors suggest that a subset of V4 neurons respond to occluded images with two distinct peaks (but not all reviewers are convinced that the distinction between subpopulations with one and two peaks are real). The second peak follows the vlPFC response peak and shows similar characteristics to vlPFC. Based on these observations, the authors construct a two-layer neural network in which V4 and vlPFC model units are reciprocally connected and vlPFC responses shape the second peak of V4 units.

The reviewers find the proposal that PFC interacts with V4 to resolve the challenge of solving shape discrimination in the presence of occlusion to be timely and of significant interest. At the same time, the reviewers identified problematic issues with the data analysis that must be resolved before this work could be considered for publication.

Summary:

General concerns about the experimental aspects of the paper include the reproducibility of the main result and the impact of using different approaches when recording from the two brain areas that are compared. General concerns about the model include that it may be unnecessarily complex for the current illustrations provided, and that, even with this complexity, the current illustrations do not reflect population average effects.

Essential revisions:

1) The main claims of the paper rest on the assertion that V4 shape selectivity increases as a function of time. The concerns about this claim are two-fold:

1A) The current illustration is made via an argument that there are two subpopulations of neurons, those that have a second, shape selective peak and those that do not. The reviewers are concerned that the existence of these two subpopulations will not be reproducible. This includes some confusion about the methods that were employed to identify the two peaks, as well as the suspicion that the specific parameters used for this identification were overfit to this particular data set.

The way that the two peaks are identified (subsection “Peak finding algorithm”) is hard to understand: "were within ± 12 ms of at least one third of the peaks identified based on the PSTHs for individual occlusion levels".

How sensitive are these findings to the parameters of the ad hoc peak finding algorithm? Similarly, one may think that the algorithm for detecting double-peak V4 cells has many false positives and the true frequency of cells with two peaks is lower than that suggested in the paper. Can you clarify?

In Figure 6C, how can the "Time to peak" for V4 neurons be greater than 300 ms, if the second peak was required to be before 300 ms ("The second peak was constrained to be no later than 300 ms after test stimulus onset")?

The manuscript states: "However, shape selectivity for occluded shapes, particularly at intermediate occlusion levels (visible area 72- 95%), was different for the two groups: neurons with two peaks had significantly greater shape selectivity than neurons without two peaks in the time interval ~200-260 ms after test stimulus onset (t-Test, p < 0.05)." The supporting figure is Figure 8A vs. B. What this is stating exactly? Is the significance tested for each occlusion level separately and it was significant for visible area conditions of 72, 82, 90, and 95%? If so, was Bonferroni correction or another correction applied? How was this time period selected (~200-260 ms)? Was there a correction for testing multiple time periods? Do the results hold in different time periods?

To examine the tuning of the "second peak" the authors use as baseline the activity in an earlier phase of the visual response. Hence, if the neurons respond strongly early on, their response will decrease more strongly during the second peak. In other words, there is suspicion that the results presented in Figure 7 where activity of the second peak decreases if the visible area is large is simply an artifact of this erroneous choice of a time window to compute the baseline. Instead the authors should use the pre-stimulus activity as baseline for all epochs. This choice implies in the subsection “Response change”, in the first equation that b depends on i, in incoming input. In Figure 7D, E the y-axis is in units of "normalized response change". How was the normalization?

The average PSTH of V4 subpopulation with two response peaks is quite distinct from the single cell examples. For the population, the second peak is not obvious and responses to unoccluded stimuli stay above the occluded shapes, unlike the single cells in Figures 4 and 5. What causes the discrepancy? Is it the variability of the time of the second peak in V4 neurons? It will be helpful to have a supplementary figure with more single cell examples.

1B) More generally, the claim is that V4 shape selectivity changes as a function of time, and missing is the more direct comparison of shape selectivity for the same neurons early versus later in the response.

2) The broad tuning of neurons in vlPFC seems qualitatively inconsistent with it playing a role in enhancing V4 shape selectivity. The model does not currently resolve this nor is an explanation provided.

3) There are concerns that the functional differences between the responses in PFC and V4 may follow from differences in the experimental paradigm. These include:

3A) What was the effect of tailoring stimuli for neurons in one area and not doing so in another area? Can the latency of responses or their tolerance to occlusion be influenced by tailoring stimuli for neurons?

3B) It is unclear why the authors focus on the vlPFC neurons that are influenced by occlusion. There are also many neurons that do not care about the occlusion and we wonder whether these cells include some neurons that are tuned to the shape of the stimuli. If yes, is their tuning better or worse than that of the neurons that are influence by the occlusion?

What would Figure 3D look like if you included all of the 216 vlPFC neurons that were responsive during the test epoch?

Some cells have a stronger response if the visible area increases. Is it possible that these neurons are better tuned to the shapes than those neurons that are most active for high levels of occlusion?

Related to this last point: is it conceivable that the neurons that increase their response if there is more occlusion are tuned to some aspect of the occluders, e.g. the total surface area or the total perimeter of the occluding dots?

This latter possibility seems to be supported by the finding that the vlPFC preference for occlusion decreased when the occluders had the same color as the background (as is stated in the first paragraph of the subsection “Representation of occluded stimuli in vlPFC”).

There were 381 vlPFC neurons, 98 were significantly modulated by occlusion. How many of these 98 neurons are in monkey M vs. O?

4) Can the model replicate all aspects of the data? Including:

The shape selectivity index in vlPFC is considerably lower than in V4. Can the model in figure 9 work with reduced shape selectivity?

V4 cells are divided into two subpopulations, one with two peaks and another with a single peak. How can the feedback model explain that many V4 cells do not show two peaks in their responses to occluded stimuli? Are the authors assuming inhomogeneous feedback from vlPFC to V4? Alternatively, they may be suggesting that V4 population includes a continuum of responses that vary from single peak to double peaks and include in-between responses.

Can the model be adjusted to replicate population data in Figure 6? In its current form the model seems to best explain single cell examples. It is unclear how well these examples represent the population.

5) The gain mechanism that the authors propose in their model may be envisioned as PFC receiving two signals – an intertwined shape and occlusion signal and an occlusion-only signal, and then correcting the intertwined estimate with occlusion information. This seems like a bit of a chicken-and-egg problem: how and why would the brain extract occlusion level from occluded stimuli but not shape (preceding the locus at which it disambiguates shape)? Where could this v4-independent but occlusion dependent gain modulation be coming from? The authors suggest IT as a potential source, but IT units receive input from V4 and also feedback to V4. Does the model assume that gain modulation arrives at vlPFC with the same latency as the V4 inputs? Why can't feedback from IT to V4 be the source of the second V4 response peak? The authors cite their SfN abstract for occlusion selective signals in IT. It will be useful to provide more explanation about the results, especially for readers who did not stop by the SfN poster. What if there are two visible stimuli: one that is occluded and one that is not? Would the gain modulation then be different for the two stimuli? What if one stimulus occludes another stimulus?

6) Can the model be simplified? The proposed dynamic model has multiple degrees of freedom and several nonlinearities. Is all this complexity necessary? In the current version of the paper, it is difficult to gain intuition about the model based on the text. Simplifying the model can shine light on which components and nonlinearities are indispensable and therefore reasonable targets for follow-up studies. For example, the adaptation term for V4 projections to vlPFC seems a little arbitrary. Why such an adaptation does not happen for other connections in the model? A similar question can be asked about the half-rectified feedback from vlPFC to V4. Why other connections in the model are not half-rectified? More generally, we encourage the authors to explore the model space a little more extensively for simpler model architectures. As it stands, the network seems like a high-parameter model that one can tweak to get many different types of outputs. Establishing the necessity of the proposed architecture and parameterization requires a little more work.

7) On the interpretation of the effects in V4:

In the first paragraph of the subsection “Representation of occluded stimuli in vlPFC” the authors argue that the responses of some of the vlPFC neurons that are stronger if occlusion is stronger does not depend on the increased task difficulty or attentional demands, but this reasoning is unclear. Furthermore, the authors seem to have changed their mind in the fourth paragraph of the subsection 2Representation of occluded stimuli in vlPFC”, where they argue that vlPFC may amplify weak signals and that vlPFC is engaged in tasks of greater difficulty or cognitive demand.

In the first paragraph of the subsection “Representation of occluded stimuli in vlPFC” the authors argue that because many vlPFC neurons were tuned to shape, that these neurons therefore cannot reflect task difficulty or attentional demands. This argument does not hold because neurons may well be tuned to multiple aspects of a task.

8) How did you know whether penetrations were indeed in vlPFC? Was histology performed?

9) [Additional comment sent to the authors in response to authors’ plan for revision]: The authors should clarify if there is a real dichotomy between neurons with one versus two peaks, as well as how broad the distribution of the timing for the second peak is. Can they really convince the reader that they are not simply amplifying noise with their analysis? Furthermore, they now make the point that the tuning is stronger during the second peak. We would like to know if this is not simply predicted by the presence of extra spikes – i.e. the presence of a peak implies some extra spikes at a certain point in time.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Dynamic representation of partially occluded objects in primate prefrontal and visual cortex" for further consideration at eLife. Your revised article has been favorably evaluated by David Van Essen (Senior Editor), a Reviewing Editor, and two reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as described below by reviewer #3. We envision that these revisions will be straightforward to carry out and that verification can be handled by the Reviewing Editor.

Reviewer #2:

The authors have addressed the most critical comments. There are structural weaknesses in the dataset that keep alternative interpretations plausible. However, I believe the authors' interpretation is strengthened by the new analyses and the paper passes threshold for publication.

Reviewer #3:

In their revision, Fyall et al. have addressed many of my concerns satisfactorily. They have made it clearer that some of the V4 neurons have a second peak that is more prominent in case of occlusion (Figure 4C represents a compelling example). Also, the peak detection method is now more convincing and it is also better documented. It remains unclear whether activity in vlPFC indeed contributes to late V4 activity and it is therefore conceivable that there are additional areas that could contribute to late V4 activity. Yet, I do realize that demonstrating the causal link between dlPFC and V4 would require a different approach, which would be beyond the scope of the present contribution. However, establishing such a causal link might be an important topic for future research, and the authors could mention this point, which could be added to the paragraph of suggested future work (subsection “Response dynamics in V4”, fifth paragraph).

Remaining points:

1) I find it difficult to understand why the vlPFC neurons do not respond so well when the occluders have the same color of the background (subsection “Representation of occluded stimuli in vlPFC”, second paragraph). I would suspect that the processes for shape recognition would remain the same. Or did the monkeys' performance show signs that this was not the case?

2) Quite some p-values are lacking, three examples:

"The responses of most of these occlusion-sensitive 155 neurons (71/98) increased with increasing occlusion level".

"Even for the small subset of vlPFC neurons that responded more strongly to unoccluded stimuli (27/98), shape selectivity was not stronger for unoccluded than occluded stimuli (see Figure 3—figure supplement 2A)."

"Shape selectivity for occluded shapes was significantly higher during the second peak than during the first peak."

3) "Of 85 neurons, 30 neurons (~35%) were classified as having two peaks". How were these cells distributed across the two monkeys?

4) The model with interactions between vlPFC and V4 seems still somewhat simplistic as there are only a few neurons and the variation (in effect size and timing) across neurons shown in the figures is actually a variation across neurons in different models rather than a variation of neurons within the same model. In networks with many units and reciprocal connections, the network dynamics might actually work against variation across neurons. The authors should discuss this. It would be great if it would be possible to show the same range of differences between neurons within a same model, but I will not insist on such a demonstration given that making such a larger model might require a substantial investment of time.

5) "We cannot rule out the possibility that IT responses also contribute to V4 responses during the second transient peak. However, our IT recordings suggest this is unlikely because, as in V4, shape selectivity in IT is stronger for unoccluded than occluded stimuli". Is it conceivable that some IT neurons also have two phases in their response where the second phase is more pronounced in the presence of occlusion? It would be great if the authors could look for this possibility in the previous data set by Namima and Pasupathy, 2016? If the two phases are there it would strengthen the paper, but it would also be interesting if that is not the case.

6) Equations 4/5: I failed to see the logic of these equations, would it be possible to clarify this? Equation 9: what is thr2?

7) I found Figure 8—figure supplement 6A confusing: how do you compute y/z for neurons with one peak?
