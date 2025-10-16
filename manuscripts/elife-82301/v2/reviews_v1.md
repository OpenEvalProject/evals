# Peer review - Round 1

Editors:
- Payam Piray, https://ror.org/03taz7m60 University of Southern California United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82301.sa0](https://doi.org/10.7554/eLife.82301.sa0)

This paper proposes a new, biologically realistic, computational model for the phenomenon of hippocampal replay. This is an important study with relevance for a broad audience in neuroscience. The proposed model convincingly simulates various aspects of experimental data discovered in the past.


---

# Peer review - Round 1

Editors:
- Payam Piray, https://ror.org/03taz7m60 University of Southern California United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82301.sa1](https://doi.org/10.7554/eLife.82301.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "A Model of Hippocampal Replay Driven by Experience and Environmental Structure Facilitates Spatial Learning" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Guest Reviewing Editor and Laura Colgin as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: H Freyja Ólafsdóttir (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Reviewers agreed that this is an important study with relevance for a broad audience in neuroscience. Reviewers specifically commended the simplicity and elegance of the proposed computational model and the clarity of the manuscript. There were, however, also several concerns that we would ask you to address in a revision.

1) All reviewers agreed that there should be further simulation analyses to address several seminal empirical data in the field of replay. Of particular importance are those studies that are simulated in Mattar and Daw 2018 paper. Is the model able to recapitulate reward over-representation in the open field and T-maze (Mattar and Daw's Figure 4). Another crucial experiment (also simulated in the Mattar and Daw 2018) is the phenomenon of non-local replay. Reviewers agree that it's important that computational models of replay capture these characteristic aspects of replay.

2) Reviewers also agreed that it is important that authors perform further simulation analyses to address other experiments simulated in Mattar and Daw 2018. These include responsiveness of reverse replay to reward change, replay counterintuitively entering an aversive zone, and the effect of experience on replay frequency. Even if the proposed model cannot account for all of these findings, it is important that authors transparently report them (maybe with supplementary figures) and discuss them extensively.

3) The fact that the model has two modes (default and reverse) to account for empirical findings is also a major issue. Reviewers agree that the underlying mechanism regarding these two modes is not clear. Do they work in parallel? or is there a dynamic switch between the two? How does the dynamic switch work computationally? And how is this aspect of the model related to experimental data? Please see specific comments by Reviewers 2 and 3 about this issue.

4) In addition, individual reviewers made a number of suggestions to improve the manuscript. Please carefully consider these additional points when preparing the revised manuscript.

Reviewer #1 (Recommendations for the authors):

My point is especially important in relation to the model by MandD. For example, does the current model explain evidence that replay over-represents reward locations (e.g. Figure 4 in MandD)? I suggest conducting additional simulation analysis, particularly for the experimental data explicitly presented in MandD and discussing any of those experiments that cannot be explained by the current model (if any).

Reviewer #2 (Recommendations for the authors):

In their paper, Diekmann and Cheng describe a model for replay generation that is able to replicate multiple seminal findings in the field. Specifically, in their model experiences get selected for replay depending on their strength (which is in turn determined by their frequency of occurrence and reward), their similarity to other experiences and inhibition that prohibits experiences that match the current one too much from being reactivated (which leads to the generation of replay sequences). Further, they adopt two different methods for computing similarity which they show produces complementary results. With this rather simple and intuitive model Diekmann and Cheng are able to re-produce important, but divergent, findings in the field. For example, why replay switches directionality at different time points on a maze, how it can generate synthetic experiences, respects boundaries, etc. Being able to account for these different findings with a single mechanism is an important goal and no small feat.

However, I still have some reservations about how much the current model differentiates itself – and represents an improvement – of a recently published model (the so-called prioritized memory access (PMA) model for replay Mattar and Daw, 2018). Further, although their model provides a relatively comprehensive account of multiple replay findings, it doesn't address many studies that show awake replay is non-local (even depicting experiences in remote environments). Finally, I would like the authors to elaborate on how their 'default' and 'reverse' policy could be implemented biologically and how these two modes relates to current thinking in the replay field. I elaborate on my points below:

– Benefit over PMA model: The authors maintain that their model represents a significant improvement from the PMA model as the latter is not biologically feasible. In the PMA model, replay gets selected based on the utility of a possible experience reactivation which is partly derived from its "gain" term. Here, the authors' critique is that if the calculation of gain requires access to all stored experiences, this becomes very computationally laborious and biologically unfeasible. Yet, it's not clear to me in the current model's implementation that it represents a clear advantage in this way. Namely, to compute similarity – which influences replay prioritization – the current experience state needs to be compared with all other experience states (or tuples). Thus, does their model not also require access to all stored experiences? If not, I think the authors need to spell out a bit more about how this still makes their model more efficient and biologically implementable than the PMA model. This is a particularly important point as one of the main 'selling points' of the paper is that it achieves what the PMA model achieves but in a physiologically realistic way.

– The authors show the model does well in replicating multiple replay findings in the field. However, they focus primarily on awake replay findings that show some relationship to current behaviour- e.g. depicting short cuts to goal locations, activating paths just taken, etc. However, many replay studies show that replay is very often non-local (e.g. Karlsson and Frank (2009); Olafsdottir et al. (2017)). How can their model accommodate these findings?

– In the current model there are two modes (policies) for computing experience similarity described; the default and reverse mode. The authors show you need both to effectively account for different replay phenomena (e.g. you need reverse for reward learning, particularly in environments where an animal's path is not prescribed). But what determines which policy is used? How would switching between the two be implemented in neural networks? Or do they propose they work in parallel?

– The default and reverse mode resonate with some contemporary theories of replay. Namely, a commonly held view is that awake replay may support planning/memory retrieval etc. whereas replay during rest periods supports memory consolidation. Perhaps the authors can elaborate on how their different modes, which resemble somewhat the planning vs consolidation mode, relate to these theories. Could it be that the default mode may be a sort of a planning mode – supporting on-going behaviour – whereas the reverse mode is more about learning?

Reviewer #3 (Recommendations for the authors):

In multiple instances the authors refer to the biological plausibility of their model, and the lack thereof in the model by Mattar and Daw. Intuitively, I agree with the authors. However, to my knowledge we don't know what is biologically plausible and what is not. I suggest some rewording to emphasize that their model is simpler and less computationally taxing compared to Mattar and Daw. Further, I would appreciate a more explicit discussion of the biological plausibility of their model. They get into this to some degree in the discussion, particularly with regards to the return of inhibition term (i.e., line 401). However, the description of how experience strength or distance could be computed could certainly be expanded beyond just referencing other studies. Importantly, the model occurs in two modes. How might the hippocampus gate these two modes?

In general I found the methods to be exquisitely articulated and comprehensive. However, the description of how replay is generated in their model could be expanded/clarified in the main text:

– I understood that an experience consists of a transition between two states (in addition to reward/action)- and that the entire experience (including both states) is reactivated during replay. However I think a supplementary figure showing how exactly one gets from the last panel of figure 2A to an ordered set of reactivated states as in Figure 5c could be helpful.

– Most importantly- I think it would be very useful for the authors to show more examples of replay events generated by their model, particularly with respect to Figure 3. For example, they report the directionality of replays in the open field/labyrinth, but I would like to know where the replays actually started/ended, and how this changed over trials. This would help clarify how the replays are behaviorally useful to the agent.

– The authors could better describe the logic/motivation of the default and reverse states. Initially I assumed that the default mode simply drives forward replay, and the reverse mode reverse replay- but this is not entirely the case. Why did the authors use just 2 modes (the first comparing the similarity between experience 1-state 1 and experience 2 state-1, and the second comparing the similarity between experience 1-state 1 and experience 2 state-2)- why not, for example, have other modes comparing experience 1-state 2 and experience 2 state-1, or experience 1-state 2 and experience 2 state-2? Many readers would benefit from a bit more intuition in terms of linking these modes to biological phenomenon.

– Can a single replay consist of both forward and reverse transitions? As mentioned above, a panel of example replays upfront could be very useful.

– Please confirm that only one map was constructed for linear environments. What was the reason for this choice, and would it impact the results to use two maps (one for each running direction, as in Mattar and Daw, and consistent with hippocampal fields on a linear track)?

– A description of how the default versus reverse modes are selected in the dynamic mode is provided in the methods, but should also be described in the main text.

– The definition of a replay epoch is in the methods but might be moved to the main text.

Can this model account for a broader scope of replay phenomena including: the sensitivity of reverse replay to reward magnitude or reward prediction error, over-representation of reward locations, or the tendency of forward replays to counter-intuitively lead towards an aversive (negatively rewarding) locations? As Mattar and Daw demonstrated that their model produces patterns of replay that match these arguably fundamental empirical findings, examining the fully overlapping set of scenarios would allow the models to be compared head-to-head. It is unclear whether either model can account for the recent observations that replay is enriched for locations not visited recently (Gillespie et al., 2021) or trajectories directed away from the animal's preferred goal location (Carey et al., 2019). I do not mean to suggest that the authors needs to perform all of the above tests. However, it would be of interest to at least include discussion about which empirical findings the current model could likely not account for.

Line 160: 'in our simulations the reverse mode produces more updates that were optimal than did the default mode'. Please define an optimal (policy?) update.

Line 165: I'm not sure what the authors mean by 'mixed' replays. Are they describing replays that traverse in one direction and then switch to the other (i.e., reverse to forward), as in Wu and Foster 2014?. If not, a better word choice might be 'interspersed'.

Line 188: Are there any statistical tests to accompany the statement that these log-log plots are linear?

Line 223: It is not clear to me what the alternating-alternating condition controls for.

Line 234: The explanation about the observed differences in short-cut replays under the different behavioral paradigms was somewhat confusing. A figure showing the relative amount of experience in each segment of the maze in each paradigm could help clarify.

Line 248: While it is interesting to ask whether the replay generated by your model facilitates learning in the task, I think it would be of broader interest and more informative to show specifically which replays are useful. For example, what was the distribution of replays that the default and reverse mode yielded on that task? How does task performance change if you limit replay to a subset, such as only reverse replays starting at the goal, or, most relevant here- only-short cut replays?

Figure 6A: What are reactivation maps? I.e., is this a summary or average of all reactivations, or an example of an individual replay epoch (I assume it's the former, but that should be specified). Individual replay examples would also useful.

Line 329: 'General representations of task structure in EC have been proposed to be forming hippocampal place cell code together with sensory information'- I suspect there was a typo in this sentence; I was unable to decipher its meaning.

Line 409: 'We argue that the minimum value should be applied after the summation of gain values" – what is the argument for applying the minimum value after summation? In general I wonder if the description of PMA's flaws (starting at line 404) should be moved to the related Supplemental Figure legend. I think more detail would be needed for most readers to understand the apparent error (for example, what is the 'special n-step update', what does it mean to apply before summation or after summation, and what makes one version better than the other)?

Figure 5e: Please state in the figure legend what happened at trial 100. Also, as noted elsewhere, I think it would be useful to compare performance with the dynamic mode (and possibly the PMA model).

Figure 5/Supplementary Figure 7: I'm confused as to why in Figure 5 there is little difference between the forward and reverse modes in the initial learning of the task, but a difference after the reward location switch, whereas in Supplementary Figure 7 the exact opposite pattern is shown on the T-Maze. In general, what explains the differences in the initial learning rate and the learning rate after the reward switch, especially on the T-maze? I don't see what information the agent learned in the initial phase that remained useful after the switch. Perhaps showing examples of the agents behavioral trajectory/decisions at different stages of the task would help.

Supplementary Figure 3: what is the take-home message of showing the displacement distributions with different inverse temperature parameters? Is the point that the results hold when using different temperatures? If so, why not provide a more quantitative metric, like the log-log plots using different inverse temperature parameters?

Supplementary Figure 8: The main text indicates that this figure was generated using the reverse mode, but the legend doesn't say so.

Methods line 463: 'The term in brackets is known as the temporal difference error'. This could perhaps be explained a bit more.
