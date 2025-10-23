# Peer review - Round 1

Editors:
- Peter Kok, https://ror.org/02jx3x895 University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71736.sa0](https://doi.org/10.7554/eLife.71736.sa0)

This is an intriguing study using cleverly designed stimuli to investigate the representation of physical stability in the human brain. This paper will be of interest to readers wondering when human cognition uses pattern matching similar to that used by machine learning algorithms, and when it relies on more specialised processes evolved for specific tasks. The well-crafted experiments provide convincing support for the authors' claim that the human brain computes an abstract representation of the physical stability of visual scenes.


---

# Peer review - Round 1

Editors:
- Peter Kok, https://ror.org/02jx3x895 University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71736.sa1](https://doi.org/10.7554/eLife.71736.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Invariant representation of physical stability in the human brain" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Peter Kok as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Floris de Lange as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Jaqueline Snow (Reviewer #3).

The reviewers have discussed their reviews with one another, and agreed that the study is of interest, but they had serious concerns about the interpretation of the main results. Several alternative explanations of the results will need to be ruled out conclusively, likely requiring new (behavioural) data, in order for the paper to be suitable for publication in eLife. Note that given the seriousness of the concerns, simply acknowledging them will not be sufficient. The reviewing editor has drafted this letter to help you prepare a revised submission, should you feel that you are able to resolve these issues.

Essential revisions:

1. One major concern with the interpretation of the findings is that while the stimuli in the Animals-People condition seem to be relatively straightforward to understand whether they are "unstable" or "stable" scenes, the stimuli in the Physical-People condition seem more difficult to comprehend when they are "unstable" versus "stable", perhaps due to their unusual scene composition. For instance, it can take a moment to understand what is going on in the scene depicting a man precariously perched atop a ladder, with the ladder balanced on one leg over a stairwell (Figure 2A). This leaves open the possibility that the elevated activity observed in the fronto-parietal areas may not reflect forward simulation of unstable (over stable) scenes involving physical objects and people, but instead, the requirements of parsing difficult-to-comprehend scenes (which happen to be unstable and physical) over straightforward scenes (which are either stable or involve animals). Put simply, the fMRI responses recorded in fronto-parietal cortex may have more to do with scene comprehension than with physical stability. This confound will need to be ruled out conclusively. This will likely require collecting and analysing new data. For instance, the authors could collect behavioral questionnaire data to gauge for each stimulus ease of comprehension, as well as anticipated motion and likelihood of change (see point 2). The behavioral data could then be correlated with the fMRI responses, and it can be tested whether fMRI results are explained better by physical stability or one or more of these other factors. Of course, the authors may have a different approach in mind, which is perfectly fine, as long as the confounds are resolved convincingly.

2. Can the effects of physical stability reported here be dissociated from effects of implied motion, or likeliness-to-change? In the current study, a higher response to unstable vs stable scenes in reported in motion area MT, which the authors describe in terms of implied motion. It therefore seems possible to describe the results in the "Physics Network" in terms of implied motion, rather than physical stability, as well. As for the first point, this alternative explanation will need to be ruled out conclusively.

3. The perilous-vs-non-perilous (Animals-People) condition is a crucial control for attention. However, it seems the relevant interaction, i.e. more generalization for stable-to-stable than stable-to-perilous, is not statistically tested. This test seems crucial to demonstrate that generalization is specific to physical stability.

4. The current study, and its findings, should be situated more deeply in the context of what has been done before. Fischer et al., (2016) showed that specific regions of frontal and parietal cortex responded more strongly when observers performed a physical reasoning task about which direction a tower of blocks would fall (versus a control task). Schwettmann et al., (2019) examined how object mass is represented in these same dorsal areas, and in the ventral visual pathway. The differential pattern of results, including the finding of generalizability across scenarios, was the same as with the present findings, but for object mass, rather than scene stability. Yet Schwettmann et al., (2019) is only briefly mentioned despite its many methodological and conceptual similarities to the present study. The authors should more effectively situate the present findings relative to their previous work (in the Introduction), as well as explain what is novel and surprising about these most recent findings (in the Discussion).

5. Can the authors clarify why they used block towers, Physical-People scenes, and Physical-Objects scenes with the CNN, but used Physical-People scenes, Physical-Objects scenes, and Animals-People scenes with the human observers? Because the comparison of the CNN to human observers is central to the paper, it is worth explaining why different stimulus sets were used between the two.

6. It seems that the CNNs simply didn’t do a great job classifying physical stability in the first place (60% classification accuracy). In that case, how generalisable should we expect their representations to be anyway? It could be that a CNN that does achieve high accuracy on physical stability judgments (90%?) would actually show this kind of general transfer; but we don’t know that from the data presented here, because it’s possible that the lack of generality arises from poor performance to begin with.

7. The Animals-People results in Table 1, third row, seem quite puzzling. Is it right that there is a far higher between- than within-correlation in all ROIs, especially the visual ones? How can this be explained?

8. Overall, the generalization effects reported in Table 1 seem quite subtle, and there are of course many statistical tests reported in this Table; have these been corrected for multiple comparisons?

9. Could the authors explain why they chose to split even and odd runs in the within-scenario analysis but not in the between-scenario analysis. As acknowledged in the caption for Figure 2, this prevents direct comparison of the correlation values between the two analyses, so the justification for the difference should be made explicit.

10. The brief discussion of the generalization effect (Animals-People to Physical-People) in LOC is not very satisfactory. For instance, what kind of similar shape information could be driving this effect that is not present in the other generalization effects? Also, from Table 1 there seems to be a significantly negative generalization effect in V1 for Physical-Objects to Animals-People, but this is not discussed at all.

11. “We reasoned that if the candidate physics regions are engaged automatically in simulating what will happen next, they should show a higher mean response when viewing physically unstable scenes (because there is more to simulate) than stable scenes (where nothing is predicted to happen).” It seems true enough that, once one knows that a scene is stable, one doesn’t then need a dynamically updated representation of its unfolding. But the question that this paper is about is how we determine, in the first place, that a scene is stable or not. The simulations at issue are simulations one runs before one knows their outcome. Stable scenes may well have a lot to simulate, even if we determine after those hefty simulations that the scene is stable after all. And of course unstable scenes might well have very little to simulate, if the scene is simple and the instability is straightforwardly evident. Can the authors say more about why it’s easier to determine that a stable scene is stable than that an unstable scene is unstable?

12. “Interestingness” ratings seem like a not-quite-adequate approach for evaluating how attention-grabbing the towers were. Why not a measure like how much they distract from another task? The authors could add a new measure of attention-grabbing-ness with a sounder basis in the visual psychophysics literature, or a stronger justification for why “interestingness” ratings are up for the job.

13. More examples of the stimuli used in each scenario should be provided, either as a supplemental figure or in a hyperlink, to help readers evaluate the stimuli.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled “Invariant representation of physical stability in the human brain” for further consideration by eLife. Your revised article has been evaluated by Floris de Lange (Senior Editor) and a Reviewing Editor.

The reviewers agree that the manuscript has been significantly improved. There are a couple of remaining issues to be addressed before the paper can be accepted, as outlined below:

1. The response to previous point 6, regarding the generalization of the CNN classification, is not completely satisfactory. It’s still a worry that the paper is conflating (1) whether CNNs can learn to discriminate stable from unstable with (2) whether whatever it is CNNs do learn is generalizable. The issue raised earlier was that CNN performance was so low that, for all we know, better performance would have revealed that the CNNs’ generalizability wasn’t so bad after all. To say that the poor performance “reinforces our point that pattern recognition systems are not very good at discerning physical stability” still feels a bit off-target. There are multiple ways to not be good at something, and the authors here are claiming that one of those ways is a lack of generalizability per se. But our previous point was that we can’t tell the difference between bad generalizability and bad overall performance. If the authors themselves are making this distinction (and they are in the paper), it seems crucial to separate those claims and support them independently. If they cannot be supported directly from the data, it would be appropriate to discuss this as a limitation of the study.

2. The response to previous point 3, regarding the specificity of decoding of representations in the Physics network, did not fully address the issue raised. The authors infer specificity from a null effect in ‘decoding’ stability/peril in the Animal-People condition, but of course a null effect is not evidence for absence. It would be more appropriate to test whether the decoding in the Physical-Object and Physical-People conditions is statistically better than in the Animal-People condition. E.g. in an ANOVA with two factors: Physical stability vs Animate stability and Within vs. Between. In other words, in their reply the authors cited two findings, (a) a null effect in the Animals-People condition and (b) a significant effect in the Physics condition, but to support their claims it would be useful to test whether b is significantly larger than a. Otherwise, the findings could for instance be due to the Animals-People null effect being based on very noisy measurements, i.e. a non-informative null effect, which does not constitute evidence for the specificity of the physical stability effects.
