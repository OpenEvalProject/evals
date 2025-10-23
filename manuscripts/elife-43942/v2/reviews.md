# Peer review - Round 1

Editors:
- Jörn Diedrichsen, University of Western Ontario Canada

Reviewers:
- Michael Landy, New York University United States
- Samuel J Gershman, Harvard University United States

## Review text

DOI: [10.7554/eLife.43942.012](https://doi.org/10.7554/eLife.43942.012)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Unimodal statistical learning produces multimodal object-like representations" for consideration by eLife. Your article has been reviewed by three peer reviewers including the Reviewing Editor, and the evaluation has been overseen by Michael Frank as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Michael Landy (Reviewer #1); Samuel J Gershman (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The paper "Unimodal statistical learning produces multimodal object-like representations" presents an elegant series of two experiments, demonstrating that human adults can make cross-modal inferences without bimodal training. Participants learned either haptically or visually that two particular shapes tend to form an object. In the visual condition the critical cue was the probability of the co-occurrence of the two shapes, in the haptic condition the force necessary to pull them apart. The authors show that these learned regularities generalize to a test in the other domain. Overall, we found the paper clearly written, interesting, and insightful.

1) While all reviewers agreed that the experiments provided new interesting insights in the learning and cross-modal generalization of learning, the theoretical link to the formation of objects is not as well motivated and may require a more careful treatment (see major comment from Sam Gershman and Jörn Diedrichsen). Specifically, the extant literature on the principles of object perception clearly provides evidence that boundary cues are important in the formation of objects (Spelke, 1990, etc.). While the authors show that statistical regularities can be learned and generalized across modalities, the paper does not provide any insight into the importance of boundary cues vs. statistical regularities. This should be better reflected in paper.

2) Yildirim and Jacobs, 2012, 2013, 2015; see also Erdogan, Yildirim and Jacobs, 2015, have developed computational models and provided empirical evidence for modality-independent representations of objects. This literature should be cited and the current work placed better in this context.

3) The reviewers and the reviewing editor were not 100% convinced by the argument that conscious awareness did not drive the learning/generalization effects. The authors do not even report the average score on the explicit test. What would help is to present data on explicit knowledge and generalization as a scatter plot. If all subjects showed high levels of performance on the explicit task, the validity of the partial correlation approach would be seriously called into question.

I am appending the original 3 reviews below for more details.

Reviewing Editor:

The paper "Unimodal statistical learning produces multimodal object-like representations" presents two elegant experiments, in which participants either haptically or visually learn that two particular shapes tend to form an object. In the visual condition the critical cue was the probability of the co-occurrence of the two shapes, in the haptic condition the force necessary to pull them apart. The authors show that these learned regularities then generalized to a test in the other domain.

Overall, I found the paper clearly written, interesting and insightful. I believe there are overall some weaknesses in the presentation of the results, and particularly in the strength of some of the statistical results (i.e. there is really no real evidence for a haptic -> visual generalization at the group level).

Furthermore, the motivation for the study is based a lot on how objects are learned in childhood. This arises two critical questions: Do the authors believe that the learning rules uncovered from an experiment in adults has anything to do with how 4-month old start to understand the world. Secondly, "objectness" is probably learned to a large degree by visual or haptic (as in surface touch) boundaries. Showing that adults CAN learn statistical regularities does not show that this is indeed the driving mechanism behind the acquisition of objects. Indeed, one might argue that statistical co-occurrence is not enough. For example, I often wear pants, but that doesn't make them and me one object?

Reviewer #1:

OK, this isn't typical reviewer-speak: This paper is really fun! It's such a good example of true synergistic collaboration, since it so obviously combines the diverse threads of the authors' previous work. And the result is a cool paradigm and a convincing set of data. I really don't have much in the way of useful comments, which is not typical for me. (OK, my comments might not usually be useful, but at least there are usually a lot of comments; ^) And that you managed to work in one of your chimera namesakes… Really, these are very well-designed, careful experiments. I wonder if the "objecthood" led observers to perceive, fuzzy as they might have been, something in the way of illusory contours between objects, especially since the location of these contours was cued in the haptic pulling training in the second experiment.

Subsection “Visual statistical exposure”: Here I did my usual OCD check on the methods and couldn't come up with 444 as the number of distinct possible stimuli. By my count, there are 8 each configurations with 3 horizontal or 3 vertical pair placements, and assuming you place the pairs without replacement, that's 2x8x6 = 96 stimuli. And, there are 14 configurations each with either 2 horizontal and 1 vertical or vice versa, yielding 2x14x(3x2x3) = 504 stimuli, for a total of 600. I'm not sure where I went wrong or how you got 444.

Subsection “Visual familiarity test”: I also checked the arithmetic here. It works, but it assumes that the pseudopairs take a left-side pattern from one true pair and combine it with a right-side pattern from another true pair, and keep them on their former sides. That's a good choice for keeping the pseudopair statistics similar to the true pair statistics, but you don't state explicitly that that's what you did.

Subsection “Haptic statistical exposure”, last paragraph: There are fewer scenes to learn in this experiment than in the visual training experiment and they were visible for much more time (not restricted to 700 ms).

Supplementary Figure 3: I'm glad this figure was included, although I'd put it in the main text. It's worthwhile seeing how much the pulling forces were modulated relative to the correct values. You might even cite this as a learning "gain" proportion (about 20%, to my eye).

Reviewer #2:

This paper presents an elegant series of experiments of visual-haptic integration, demonstrating that human adults can make cross-modal inferences without bimodal training. The authors argue that these results support theories of object perception based on learned statistical regularities. The paper is well-written and thorough. My main concerns are about conceptual foundations and novelty.

The definition of an object as "a material thing that can be seen and touched" is too weak, because it does not adhere to the constraints evident in infant (and adult) object cognition (as an aside, it's rather odd to use a dictionary definition when so much ink has been spilled on this question in cognitive science). Spelke, 1990, defines physical objects as "persisting bodies with internal unity and stable boundaries" (p. 30). She presents evidence that infant object perception adheres to four constraints: cohesion, boundedness, rigidity, and no action at a distance. It's important to note that a material thing can have statistical regularities without satisfying any of these constraints. For example, consider the jet of steam spouting from a boiling teapot. It's a material thing with statistical regularities (following gas laws, thermodynamics, etc.); it can be seen and touched. But it is not cohesive, bounded, or rigid. The experiments of Kellman and Spelke, 1983, and many others, show that the same arrangement of visible surfaces can be perceived as an object or not, depending on whether it adheres to these constraints.

To continue this point, the conceptual issue here is that the authors consider objects to be bundles of statistical regularities that support inferences about hidden properties: "participants should be able to predict haptic properties of objects based on just visual statistics, without any prior haptic experience with them, and vice versa, predict visual properties based on haptic statistical exposure alone." No doubt observed statistical regularities do support such inferences (this is what Spelke refers to as the "empiricist" account, which she criticizes). But the key insight from Spelke and others is that object perception goes beyond observed statistical regularities. There are inductive constraints on objecthood that support stronger generalizations. This conceptual issue could be resolved if the authors step back from their strong claims about the nature of objecthood, and instead focus on more restricted claims about how statistical learning shapes multimodal generalization.

I was surprised that the authors don't cite the work of Yildirim and Jacobs, 2012, 2013, 2015; see also Erdogan, Yildirim and Jacobs, 2015, which seems highly relevant. In fact, I feel that these prior papers diminish the novelty of the present paper, since Yildirim and colleagues showed empirical evidence for modality-independent representations of objects, and moreover they developed sophisticated computational models of how these representations are acquired and used.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Unimodal statistical learning produces multimodal object-like representations" for further consideration at eLife. Your revised article has been favorably evaluated by a Reviewing Editor and Michael Frank as the Senior Editor.

The manuscript has been improved to address most of the remaining issues. However, before final acceptance, I would like to request a couple of clarifications on the explicit awareness task to be presented in the paper (Materials and methods, and Figure 4 legend):

You say that "Participants were asked whether they noticed that the shapes came in pairs and if so then the shapes were presented to them individually and they had to point to the shapes that they thought were part of the inventory."

Does this mean that some of the participants were not presented with the objects if they said they didn't know? If yes, how many participants? Was their performance labeled with 0?

The information in the caption seems to indicate that "explicitness" is the proportion of correctly identified pairs out of 6+4 =10 possible pairs. Why are the proportion correct not in {0, 0.1, 0.2.…, 1}?

I assume the test was conducted by placing 12 (or 8) objects on the table and let the participants pick out candidate pairs (although the Materials and methods state that you showed the objects individually). Please clarify. Also, please indicate whether you asked the participants to "guess" remaining pairs or did you let them stop when they did not feel they knew?

If you forced participants to guess, please indicate chance performance on your explicit memory test.

If the participants were not forced to guess remaining pairs, please state this clearly. Given the standards in the memory literature, a force-choice test is the most stringent way to assess the presence/absence of explicit memory. Subjects may say they do not "know", but still be able to "guess" very much above chance. Without a forced-choice assessment, one is testing mostly meta-memory, but not explicit memory. So if this is the approach you took, I think the limitations of the explicit test should be pointed out in the Discussion.
