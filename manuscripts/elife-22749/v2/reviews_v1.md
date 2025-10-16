# Peer review - Round 1

Editors:
- Klaas Enno Stephan, University of Zurich and ETH Zurich , Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.22749.012](https://doi.org/10.7554/eLife.22749.012)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Neural markers of predictive coding under perceptual uncertainty revealed with Hierarchical Frequency Tagging" for consideration by eLife. Your article has been favorably evaluated by Timothy Behrens (Senior Editor) and three reviewers, one of whom, Klaas Enno Stephan (Reviewer #1), is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal their identity: Peter Kok (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary of manuscript:

This EEG study of healthy human volunteers tests a key corollary of predictive coding: that brain activity of visual areas during perceptual inference should reflect the integration of top-down predictions with bottom-up inputs. To test this hypothesis, this study uses a novel hierarchical frequency tagging method which combines a recently developed semantic wavelet induced frequency tagging (SWIFT) with classical SSVEP (here: a sinusoidal contrast modulation of images). This allows for studying the effects of predictions and sensory inputs on brain activity in separate frequency bands and, importantly, examine integration of both signals in terms of intermodulation components.

Summary of reviews:

Overall, all reviewers agreed that the paper contributes an important step forward in empirical investigations of predictive coding. In particular, all three reviewers liked the experimental approach adopted by this study and agreed that it represents a novel and clever method to test a central aspect of predictive coding theory. We had an engaging discussion (and slightly diverging opinions) about potential limits of interpretation due to experimental confounds; this is detailed below and represents a key issue that needs to be addressed convincingly in the revision of the manuscript.

The policy of the journal is to provide you with a single set of comments which reflect the consensus view amongst reviewers. These comments can be found below and must be addressed convincingly. We hope that you will find these comments helpful to further improve the paper.

Essential revisions:

1) IM components are said to reflect integration of predictions and sensory inputs, but could they be the result of sensory inputs alone? That is, if both SSVEP and SWIFT components are present in the occipital cortex (the fact that the scalp distribution for SWIFT also seems to include some more anterior sensors does not mean that these signals are absent in the occipital cortex), we wondered whether the IMs might also be present there as a result of sensory processing. To give an intuition for this: if certain neurons respond to, let's say, houses, and if their 'house response' is modulated by the contrast of the house stimulus (as is highly likely), wouldn't these neurons show IM components without any involvement of top-down predictions? This point requires, at the very least, detailed consideration in the Discussion. It could potentially be tested by source space analyses, examining whether responses in FFA/OFA and PPA, respectively, show interactions between semantic category and contrast. However, we appreciate that this is a non-trivial extension of the study and leave the decision to the authors.

2) We wondered to what degree the effects of certainty on SWIFT components might reflect adaptation effects. This is because under high certainty, consecutive images are more likely to be of the same category, thus possibly leading to adaptation in face/house sensitive neurons and hence a reduced SWIFT response. In other words, in the present design, certainty is confounded with stimulus adaptation. Again, this point would require a detailed discussion and the limits of interpretation should be acknowledged clearly.

3) We had an extensive discussion about the interpretation of the IM responses and their increase with certainty in Figure 4C in computational (Bayesian) and neurophysiological terms. There was some concern that it is difficult to interpret this slope in Figure 4C unless one proposes a particular neuronal model that implements predictive coding and emits the IMs observed here. To illustrate the range of possible interpretations, two possibilities may be worth considering: If these IMs (collectively) represented the expectation of posterior beliefs, one might expect them to decline with certainty because "certainty" in this study equals the precision of prediction which should downweight prediction errors / reduce synaptic gain (in contradistinction to precision of sensory input) in predictive coding. If, however, these IMs encoded (some approximation to the log) model evidence – a notion compatible with the argument put forward by the authors – one would expect them to increase with certainty, as shown in the plot.

4) A general point that deserves more detailed discussion is that using IM components as evidence for the operation of nonlinear integration has pros and cons. The beauty is that this circumvents the need to choose a particular implementation of predictive coding. The downside is that the absence of such a neuronal model renders it impossible to map distinct IM components to specific computational or neuronal processes. IMs simply provide evidence for a nonlinear interaction between different (experimentally controlled) frequencies. While this is indeed a corollary of predictive coding, it does not appear to be a specific one and may also emerge from other theories of perceptual inference.
