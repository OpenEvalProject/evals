# Peer review - Round 1

Editors:
- Damon A Clark, https://ror.org/03v76x132 Yale University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74971.sa0](https://doi.org/10.7554/eLife.74971.sa0)

This paper will be of broad interest to readers in the field of visual processing. The authors use concurrent psychophysics and single unit recordings, along with modeling, to investigate how visual signals in primate cortical area MT can distinguish between visual motion induced by self-motion and the motion of other objects in the world. The experiments provide an explanation for otherwise puzzling discrepancies in the depth tuning of MT cells.


---

# Peer review - Round 1

Editors:
- Damon A Clark, https://ror.org/03v76x132 Yale University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74971.sa1](https://doi.org/10.7554/eLife.74971.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "A neural mechanism for detecting object motion during self-motion" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Tirin Moore as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Anirvan S Nandy (Reviewer #2); Oliver W. Layton (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers agreed that this was an interesting study and with careful controls. During the discussion, there were 3 consensus points that will require addressing in your revision, as you will also see in the individual reviews below.

1) There should be more discussion of the relationship between the incongruency mechanism explored here and the more general mechanism of flow parsing. How would this mechanism relate to or be combined with or substitute for flow parsing under different conditions?

2) The authors should perform neurometric analyses and modeling to more directly substantiate their claims. In particular, the population of cells included in this analysis could be more directly tied to populations of cells that include no incongruent cells, include only incongruent cells, or include some range of congruencies, to see directly how these different tunings in a population of cells affect decoding. This would go further than the current less direct analyses, and strengthen conclusions about the role of incongruent cells.

3) In Figure S2, two reviewers were a bit confused about the implications of a monkey getting the monocular presentation wrong 90-95% of the time, if we are reading that plot correctly. Reviewers expected this to be more like 50% performance. How should this be interpreted?

Reviewer #1 (Recommendations for the authors):

1) In this paper, starting in the abstract, the authors emphasize the role played by these incongruent MP/BD neurons. In the discussion, they say (quoting in full because there are no line numbers to reference): "our findings support the idea that a sensory representation consisting of a mixture of congruent and opposite cells provides a useful sensory substrate for causal inference (Rideaux et al. 2021). To our knowledge, these findings provide the first empirical evidence for a specific contribution of opposite neurons to perceptual inference about causes of sensory signals." However, as far as I could tell, the analyses and modeling never actually pulled out the incongruent neurons in particular to analyze them in isolation or analyze the performance without them. Thus, I had a hard time feeling this claim was supported.

In particular, in Figure 5G, the authors conclude: "Thus, the MT neurons that most strongly predict decisions to detect the dynamic object (on ambiguous trials) are those with incongruent tuning that makes them selective for dynamic objects." But this is a bit indirect, because the figure shows correlation between detection probability and neurometric performance, and the neurometric performance is correlated with congruency. Why not just correlate DP with a direct measure of non-congruence?

(On that same plot (Figure 5G), I'm puzzled why there are so few DP and NP values <0.5, when roughly half of all neurons were congruent in their BD and MP tuning – wouldn't one expect those neurons to have NP<0.5 and DP<0.5?)

Most generally, I'm still unclear about how much congruent neurons can contribute to these decisions compared to the incongruent ones. Given how well the population decoding works, it would be interesting to know if it still worked this well with *only* congruent or *only* incongruent neurons included. Is there an alternative hypothesis where having a range of different MP vs. BD tunings is what allows correct identification of the moving object, and it's the tuning variability rather than the incongruent neurons per se that matters? One could test this directly by including different ranges of neuronal tunings into a predictive model. Overall, it seems like there should be more direct analyses of the incongruent neuron population to provide support for the strong claims the authors are making about their role.

2) Figure S2: I'm a little puzzled at how a monkey could get it wrong 95% of the time in the monocular +1.5 degree \Δ Depth condition. What's going on there? Doesn't this mean that there *are* monocular cues for solving this task and they're just being interpreted entirely wrongly by the monkey? How should this be interpreted?

Reviewer #2 (Recommendations for the authors):

I would like the authors to consider these two points:

(A) In each experimental session, the axis of translation was aligned with the preferred axis of the neuron under observation in order to elicit robust responses. What would be the role of these incongruent neurons when self-motion is not aligned to this axis? Will it be possible to show that a population code of such neurons is sufficient to detect dynamic objects in the face of an arbitrary axis of self-motion?

(B) The authors state that it is not a worthwhile exercise to find model parameters that best match the empirical data, noting that they would have to make assumptions about the structure of correlated noise. It appears that in their dataset they should have several sets of simultaneously recorded neurons (e.g. 70 neurons from 57 sessions in M2). Might these give a hint to this correlation structure?

Reviewer #3 (Recommendations for the authors):

I have a few questions and some suggestions that I think would improve the manuscript and better contextualize the findings.

1. The stimulus in the present study contains background dots in the periphery outside the masked region that produce retinal motion consistent with the observer's self-motion. It would be helpful if the authors clarified the extent to which this peripheral motion may activate MSTd neurons and potentially recruit a flow parsing mechanism. In other words, is it possible that the background motion engages flow parsing, perhaps interacting with the proposed mechanism to some extent?

2. In several places in the paper (e.g. bottom of p.3, p. 26, and p. 28) the authors' descriptions may be taken to mean that the proposed local mechanism circumvents the need for flow parsing. Some examples: "it allows detection of object motion without the need for more complex computations that discount the global flow field" (p.3); "this mechanism… may be relatively economical for the nervous system to implement" (p.3); " An advantage of our proposed mechanism over flow parsing is that it does not require estimation of the global flow field, nor a complicated mechanism …" (p. 28). Given that the authors acknowledge elsewhere in the manuscript that the proposed mechanism likely complements flow parsing, I think the authors would agree that the proposed mechanism is not a direct substitute in general and rather is likely synergistic (e.g. multiple solutions to the same problem enhance robustness in different contexts, the proposed mechanism may be especially useful when quick reaction time is needed, etc.). Flow parsing is a much broader process and addresses far more than moving object detection. I would suggest rephrasing some of these statements and being cautious with language like "advantages over" flow parsing because the proposed local mechanism is more specialized than flow parsing.

3. I think the limitations from the public review should be referenced/discussed in the paper.

4. Warren and Rushton (2009) have demonstrated that humans parse object motion from self-motion to a similar extent regardless of whether the background motion surrounding a moving object is present in a monocular display. Niehorster and Li (2017) found a similar result for stereo optic flow. Simulations by Layton and Fajen (2016; 2020) and Layton and Niehorster (2019) support the hypothesis that a global mechanism plays a primary role. Together, these findings suggest that local mechanisms may play a much smaller role, at least for flow parsing. How do these findings relate to the proposed mechanism?

5. I found Supplementary Figure 1b very helpful to develop an intuition about the displays (as was the included video). I know figure space is at a premium, but if possible, including Supplementary Figure 1b in the main manuscript would likely help readers because the stimulus design is rather complex.

6. Aspects of the paragraph related to opposite at the bottom of p. 29 sounded repetitive after reading the previous parts of the paper and I thought they could be condensed/removed.

7. I found the motion parallax light blue color difficult to see in Figure 2. I would appreciate it if the authors replaced it with a more salient color.

8 Supplementary Figure 2: Why is the proportion correct so much less than 50% on the monocular task? Given that the monocular task is very challenging and there are two possibilities, I would have expected the proportion correct to be roughly 50%.

9. p. 7. I don't think I understand the following statement and would appreciate clarification: "…animals were translated along an axis in the fronto-parallel plane that was aligned with the preferred-null axis of the neuron under study." Does fronto-parallel plane mean rotation about the Z axis (axis toward the stimulus)?
