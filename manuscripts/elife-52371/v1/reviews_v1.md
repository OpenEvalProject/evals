# Peer review - Round 1

Editors:
- Ronald L Calabrese, Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.52371.sa1](https://doi.org/10.7554/eLife.52371.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This beautifully illustrated manuscript describes a model that captures the trajectories of animal movement during tracking and related exploratory behaviors. The central features of the model are the statistics of information in the environment, and the energetic costs of movement. Simulations using the model produce trajectories that are similar to those produced by animals. This work is a very nice and somewhat provocative contribution to our thinking about active sensing in animals.

Decision letter after peer review:

Thank you for submitting your article "Sense organ control in moths to moles is a gamble on information" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Ronald Calabrese as the Senior and Reviewing Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The paper by Chen et al. poses a new strategy for interpreting active sensation produced by animal movements. Established in earlier work, the expected information distribution (EID) specifies how future observations would reduce the uncertainty (entropy) of the belief that an agent (animal or robot) has developed about the location of a sensory object. As I understand it, previous work has developed infotaxis, a search algorithm to move towards the position (or other state) where there is a maximum in the EID. Here, the authors identify a problem with this earlier approach that it may allow convergence to distractors and favor locking to an offset point during tracking. The authors use a new strategy (ergodic information harvesting – EIH), posed in an earlier paper, that plans an optimal route through an EID to best reduce uncertainty in the sensory representation while balancing energetic costs. This routing is iteratively refined as the estimate of the object position, the belief, is updated. The authors suggest that this strategy avoids local convergence by encouraging exploration and establishing a tradeoff which may explain the "wiggles" and occasional large divergences animals show

This is a strong presentation and assessment of an interesting hypothesis. The insights that the authors have into active sensing and information acquisition are interesting and represent a clear advance in thinking. The data mining and re-analysis of published literature is clever, carefully done and seems excellent.

Essential revisions:

1) Reviewer #1 provides extensive comments on how the presentation can be revised. "…this manuscript requires significant revision. Rather than focusing on the model and results, most of which have been pushed to the supplemental sections, the manuscript reads as more of a review paper. That the model can be applied to multiple systems is a critical issue, but the manuscript should be more focused on the model rather than the breadth of systems. Further, while I appreciate the scholarship involved in writing the rather broad review of animal movement systems, I found myself constantly asking "what about" other systems and examples that were not covered in the review. This undermines the strength of the argument.

Instead, focus on the model and the remarkable fact that it can be usefully applied to the four systems with appropriate data sets (fish, moles, moths, and roaches). Conclude by saying that this is likely a general mechanism, which can be tested by applying the model to other systems not examined in the current manuscript. It is in this context that you can then usefully review other systems near the end of the manuscript." The comments which follow can guide a revision of the manuscript. We ask the authors to consider this approach. Please provide a rationale for any of the suggested revisions or lack thereof.

2) Reviewer #2 is concerned that Figure 3 be clarified and that "…the authors should make the distinction about the two different EIH conditions (uncertain single targets, and dual targets) more clear in the Introduction." Please address reviewer 2's major comments.

Reviewer #1:

The manuscript describes a new model that better captures the trajectories of movements of animals and sensor organs during tracking and exploratory behavior. This model, based on previous work by Miller et al., 2016, posits that 1) animals use movements that are not directly related to achieving the motor task to obtain information and 2) that these movements are controlled in in relation to the statistics of information in the environment and the energetic costs of movement. The main point of the paper is best expressed in a sentence that comes in the last paragraph:

“If, however, one is in an uncertain world full of surprises that cannot be anticipated, using energy to more fully measure the world's properties makes sense.”

The work is, to my knowledge, the first model that generates somewhat realistic trajectories of certain animal movements based on energetics and the quality of sensory information. This is an important contribution for two reasons. A noted in the Discussion, most previous studies of movement related to moment-to-moment control of movement for sensing have been "under-specified" – that is, those models were not designed to simulate movement trajectories. This complete system is a useful addition to the field that I expect will affect how sensing-related movements are studied. Second, as this model generates real trajectories, it can be applied to the control of artificial systems, potentially improving their performance. I am excited by this prospect.

That said, this manuscript requires significant revision. Rather than focussing on the model and results, most of which have been pushed to the supplemental sections, the manuscript reads as more of a review paper. That the model can be applied to multiple systems is a critical issue, but the manuscript should be more focussed on the model rather than the breadth of systems. Further, while I appreciate the scholarship involved in writing the rather broad review of animal movement systems, I found myself constantly asking "what about" other systems and examples that were not covered in the review. This undermines the strength of the argument.

Instead, focus on the model and the remarkable fact that it can be usefully applied to the four systems with appropriate data sets (fish, moles, moths, and roaches). Conclude by saying that this is likely a general mechanism, which can be tested by applying the model to other systems not examined in the current manuscript. It is in this context that you can then usefully review other systems near the end of the manuscript.

My suggestion is that you focus on the analysis of the electric fish data because of the depth of experiments and analysis that was done using these animals in your lab. Please bring some of the supplemental material into the main body of the manuscript. Only after the deep exploration of the fish data you then return to the cross-species analyses, concluding the manuscript with the excellent Figures 3 and 4 of the current manuscript. This will be easier to follow and more convincing than the current organization in which you show the broad application and then focus onto the fish example.

I made some line-by-line comments as I first read the manuscript, listed here.

Abstract: “are actively manipulated throughout stimulus-driven behaviors”

Sensory organs are actively manipulated in non-stimulus driven behaviors as well. Indeed, any movement that an animal makes, regardless of the control regime, manipulates sensory organs due to the simple fact that the receptors are attached to the animal.

I think that what is meant here is that the organs are often moved in ways that are somehow independent of the movements necessary to achieve the task. On one hand, perhaps this is a shorthand way to describe the issue, but it is the first sentence of the manuscript. That said, the subsequent sentences don't make sense if the reader interpreted the first sentence the way I did, so please revise.

Abstract: “While multiple theories for these movements exist…”

In the manuscript I only see a couple of theories – so why not just list them here?

Abstract: “Our approach combines information-theoretic approaches in sensory neuroscience with analyses of the energetics of movement. It can predict sense organ movements in animals and prescribe them in robotic tracking devices.”

This is the real main point of the manuscript – that you've developed a model that captures the tradeoff between information and energetics. Perhaps you can start the manuscript more directly: Movement can be used to obtain information that is not uniformly distributed in the environment. Because movement is energetically costly, there is likely a balance between the benefits of increased sensory information and energetic costs for obtaining that information. We developed a model that can be applied across sensory modalities and species that captures movements for sensing.

Introduction: “small lateral movements”

The movements are not always lateral, even in the examples that were listed here. You can simply omit the word “lateral” or rewrite the sentence.

Introduction: “several models in the literature that have been proposed”

While this is technically a true statement, it is misleading. These models share features but are largely tied to the details of the biological system under study. It might be better to state that there is no generally accepted theory for the control of these sorts of movements. Indeed, the interpretations are linked to the specifics of each model system.

You do not need to reject these ideas to propose your own. Indeed, I think that each of the authors that were cited have already informally considered the idea that there is a limitation for using movement for sensing related to the energetic costs. As stated in the Discussion, most of the previous work is "under-specified" which is to say that those works did not attempt to provide complete control framework as you have done. In this way, it is misleading to suggest some sort of equivalence of those previous models to your own. Your work goes beyond those previous works.

The contribution of this manuscript is a formal description of information gathering via movement that both can be used to analyze biological data and drive the design of artificial systems. Its core proposition is that there is a tradeoff between energy use for movement and the statistics of information generated by that movement.

Introduction paragraph one: “For example, […] Puzzling…”

It is a mistake to say "For example" because this is the start of a directed argument, not just one of the various examples from the literature. What I think that I am reading here is an attempt to "soften the blow" that you deliver here, that you are directly rejecting two hypotheses from the literature – the “signal slope” and “infotaxis” ideas. I don't see these ideas are widely accepted in the literature, and so using them as contrast for your theory is not necessary. I think the manuscript would be stronger if you eliminate this unnecessary background and jump straight to paragraph two: "Here we propose…" The other ideas are reviewed sufficiently in the Discussion.

Figure 1: I did not find this figure to be particularly informative. These traces do not look similar to my eyes, and I think that most people would also struggle to find exactly what compelling information is intended here. The caption states that these trajectories are "strikingly similar" but I can't help but imagine that an equally plausible caption would claim that the trajectories are "strikingly different."

Perhaps you are trying to highlight the fact that there are two categories of movement, task-related which is lower frequency and sensing-related which is higher frequency. But it is difficult to extract that without some stimulus to compare against. And consider, for example, that the cockroach movement which looks like a large oscillation around a mean while the snail has small, high-frequency oscillations with a baseline that is decreasing. And what is the reader expected to see in the nautilus panel? In sum, this figure is "telegraphic" in that the intended interpretation of the figure relies on information that is not available to the reader. Although I suspect that you will want to revise this figure, it is my suggestion that you simply eliminate it. And if you can't bring yourself to eliminate it, please move it to the supplemental.

On a side note – I am worried that the images are unreferenced uses of copyrighted materials from other works. More than worried, in truth. I used one of those images in one of my own efforts and received an e-mail complaint from the person who generated it. That person will certainly read this paper and I suspect be similarly annoyed. Please provide the appropriate citations/references for those images or replace them with your own materials.

Figure 3: Please replace the trajectory example used as the icon for ergotic harvesting. It is confusing because it looks like data. I'm not sure what icon to use for the model instead, but please try something else.

Figure 4: This is a complex figure that, rather than convincing me of the usefulness of the model, instead had me questioning it. In Figure 3, the trajectories are “eyeball-o metrically” convincing. Here in Figure 4 is an approach to quantify that perception. The challenge is that the data sets are quite different from each other, requiring different choices about how to analyze the data. These differences make the analysis appear arbitrary, as each panel is different. Further, the model does not produce output that matches the behavioral data – the data in the right most column do not match the data in the adjacent column. The main finding, that there is an increase in active movements in relation to the strength of the signal, is lost among the many details here.

It is my guess that the result is likely robust to the details of the frequency window, and perhaps you can devise a simpler window or analysis that can be applied to all of the examples, and then show the main result only. Perhaps, for clarity, the Fourier plots could be moved to supplemental for deeper discussion.

Figure S1: I was surprised to find this figure in the supplemental. I think that this should be Figure 1 of the main text as it is the conceptualization of the main contribution of the paper, which is the control model that shows how animals simultaneously manage the uncertain, non-uniform distribution of information in the environment and the costs of movement.

Figure S2: This figure covers an issue that I think will be of interest to most readers, and I also strongly suggest moving this to the main text.

Moving these two supplemental figures to the main text and eliminating the current Figure 1 will focus the manuscript on its important contribution, the model.

OK – to wrap up. I strongly suggest a rewrite with a focus on the model, transforming this paper from reading like a review paper with a model added to a research paper with good scholarship. I would start your edits with the title, which should focus on the main point. I'll hazard a suggestion just to get things rolling – "Tuning movements for sensing in an uncertain world"

“Sense organ control in moths to moles is a gamble on information through motion”

Also, I think that haptic touch and whisking, among the most well-studied systems in which movement is used for sensing, should be better represented in the manuscript.

Reviewer #2:

The paper by Chen et al. poses a new strategy for interpreting active sensation produced by animal movements. Established in earlier work, the expected information distribution (EID) specifies how future observations would reduce the uncertainty (entropy) of the belief that an agent (animal or robot) has developed about the location of a sensory object. As I understand it, previous work has developed infotaxis, a search algorithm to move towards the position (or other state) where there is a maximum in the EID. Here, the authors identify a problem with this earlier approach that it may allow convergence to distractors and favor locking to an offset point during tracking. The authors use a new strategy (ergodic information harvesting – EIH), posed in an earlier paper, that plans an optimal route through an EID to best reduce uncertainty in the sensory representation while balancing energetic costs. This routing is iteratively refined as the estimate of the object position, the belief, is updated. The authors suggest that this strategy avoids local convergence by encouraging exploration and establishing a tradeoff which may explain the "wiggles" and occasional large divergences animals show in the trajectories they take.

Overall I find this a very compelling presentation and assessment of an interesting hypothesis. The insights that the authors have into active sensing and information acquisition are interesting and represent a clear advance in thinking. The data mining and reanalysis of published literature is clever, carefully done on the whole and seems excellent. While I have a few comments for clarification, I am enthusiastic about this paper and think it will make a significant contribution to the literature.

The EIH algorithm has been posed earlier, but the authors take a very significant step forward in providing rigorous testing of this hypothesis in the context of single target tracking in several different animals. I especially like the breadth of systems. The prior algorithm development should be more clearly cited in the Introduction.

There is potential concern that the given experiments do not fully reject all alternative models. I don't think this is a deep problem. The authors acknowledge that a gain adjusting infotaxis model might make some of the same predictions at the EIH algorithm and discuss several alternatives. The contrast with fixed gain infotaxis is clear and the alternatives suggest future work to distinguish the "right" modification to simple EID based strategies.

The EIH algorithm seems to make predictions that deviate from infotaxis in two ways. One is when there are multiple targets and one is when there is uncertainty about a target such that a "false" target might be perceived. The authors argue that the latter is what they test and that the former while interesting is beyond the data that they have. I do find the repeated use of the two target EIH simulation a bit distracting when incorporated into the figures with actual animal data (Figure 3) because those experiments don't reflect that part of hypothesis and those specific predictions. This is especially confusing when comparing to tracking data with a moving target. I understand that the second target could be a "false" target rather than a physical multiple target, but it is difficult to gain an intuition that connects the animal data and this example where the second target is a fixed point in space.

In addition to clarifying the figure to avoid confusion, I think the authors should make the distinction about the two different EIH conditions (uncertain single targets, and dual targets) more clear in the Introduction. They can then focus on the former with the animal data, confidently simulate the second, and suggest experiments for the latter as they do in the excellent treatment of this in the Discussion. The way the manuscript is currently framed makes the distractor experiments sound very appealing because they would seem to be strong at distinguishing between the various alternative explanations in the Discussion.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Tuning movement for sensing in an uncertain world" for further consideration by eLife. Your revised article has been evaluated by Ronald Calabrese (Senior Editor).

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

The authors have made a strong revision, and they should consider the following feedback from the reviewers to fine-tune the manuscript. The further revision can be made expeditiously and will require only review by the Senior Editor.

Reviewer #1:

1) I feel that sections of the Introduction could be shortened or omitted. In the Introduction, most of the paragraph that starts with "An important quantity for implementing energy-constrained proportional betting…" could be deleted. I understand that this example is included to help the reader, but I felt like it didn't add much. It doesn't help because 1) the example of the fish seems clear enough, and 2) adding yet another example, finding a WiFi router, doesn't add much intuition. Indeed, that and the following two paragraphs would, I believe, be clearer if they were shortened and more focussed.

2) In a similar vein, I was surprised by Video 1, which rather than showing data from the manuscript, is a form of tutorial using other (sometimes unrelated) systems and tasks. I think your readers would appreciate videos of the animals in the manuscript – the primary data – perhaps side-by-side with the simulations. As most readers are unlikely to be directly familiar with these behaviors, that would be a contribution. Further, you could assemble video footage for each of the systems that you mention in the paper, something I would like to see! Also, the video is rather uneven in its production, particularly with regards to matching the narration to the video being shown. Please either replace them with data footage, or if you decide to keep the current strategy, spend some more time editing the video content to better match the narration.

Video 2 is a tutorial of the method, which I found (although unusual outside of JoVE) to be useful.

3) Consider adding a paragraph on "Optimal Foraging Theory" in the Discussion. As you know, these models explore the relations between resource distribution, cost of locomotion, and costs of predation (among other factors). These models were particularly popular in the 1990s, involving an approach that is at least parallel to this paper – examining animal behavior in relation to the performance of optimized models. I am not sufficiently familiar with this literature to suggest a paper that generated animal trajectories similar to what was done here. I do recall the Stephens and Krebs book (1986), and I remember reading a paper that had a comparison of locomotor strategies for foraging (https://dx.doi.org/10.1073%2Fpnas.98.3.1089).

4) I didn't mention this in the previous review, but I thought that it might be interesting to add a few sentences in the Discussion about the differences in perspective between your approach and perspective versus our perspective in the Stamper, 2012 active sensing paper. The data on fish tracking are remarkably similar (coincidentally Figure 3B in both your manuscript and our 2012 paper). Our attention was turned towards the brain and controller – proximate mechanisms – whereas the focus here is on “evolutionary” impacts – ultimate mechanisms. This difference in perspective has consequences that may be interesting to discuss. As you know, we did not build a model in the way you did here, but the structure (and implications) of that model would have been quite different. I leave it to you to decide what might be useful (if anything) to add to the Discussion.

Reviewer #2:

Overall I think the authors have done an admirable job responding to all of the review comments. I think this paper will make a nice and somewhat provocative addition to the literature. Given the extent of the changes I did have one follow-up comment. The authors have made many changes to the Introduction and I appreciate their efforts. However, I think the change in Figure 1 has gone a little too far in the opposite direction. While I appreciate the change to Figure 1 and the attention to minimizing the discussion of the two target case, it is now quite confusing to have this be the only figure in the Introduction. The Introduction now lacks a figure with strong biological ties especially because the Introduction is framed around an uncertain single target search or tracking problem, but the first figure now is only the two target case. Figure 1—figure supplement 2 is actually discussed more in the Introduction. That figure alone is also not sufficient because of the increased emphasis on the fish work. I really like the two target tracking simulation in Figure 1 and it should be in the paper, but it is confusing as the only motivation figure in the Introduction. Perhaps the easiest solution is to add Figure 1—figure supplement 2 or some of the examples from Figure 1—figure supplement 1 back into main Figure 1 keeping in mind the other reviewer's concern that some of the data in Figure 1—figure supplement 1 (originally Figure 1) were a bit underspecified. Alternatively a more schematic or simulated example of the tracking case could be included and discussed but this seems like more work.
