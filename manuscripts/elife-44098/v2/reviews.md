# Peer review - Round 1

Editors:
- Nicole Rust, University of Pennsylvania United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.44098.026](https://doi.org/10.7554/eLife.44098.026)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Mechanisms underlying sharpening of visual response dynamics with familiarity" for consideration by eLife. Your article has been reviewed by two peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Michael Frank as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this paper, Lim addresses questions related to the cortical mechanisms that support learning through an innovative modeling-based approach. The specific focus of this paper is a model of how the stimulus-evoked response dynamics of IT neurons along timescales of a few hundred ms differ for novel as compared to highly familiar images. Previous experimental work found that familiarity leads to a sharp reduction in firing rate following the initial peak (phasic) response, then a rebound of firing that when taken together resemble a damped oscillation. Modeling this response could provide important insights into learning mechanisms of the brain.

The author builds on her earlier model of IT familiarity acquisition, which uses changes in tuning functions to argue that familiarity plasticity resides in synaptic plasticity of recurrent connections within IT. Here she proposes 1) synaptic plasticity in the recurrent connections, 2) rate adaptation and 3) plasticity in the feedforward inputs, are sufficient to account for experimentally observed changes in visual response between novel and familiar images. In particular, this work extends the work Lim et al., 2015. It focuses on reproducing a damped oscillatory component of the visual response after learning, which was not present before learning in experimental data.

The reviewers find the work interesting and exciting, but have also identified a number of issues that must be addressed for the manuscript to be suitable for publication. They also have provided a number of suggestions for improvement.

Essential revisions:

1) The BCM type rule was derived assuming there is only plasticity in the recurrent network (Lim et al., 2015). Then it is used here with plasticity in the feedforward network. That seems inconsistent. If I understand correctly, the rule should be re-inferred with plasticity both in feedforward and recurrent connections in the first place.

2) Describing this rebound/oscillatory component mechanistically is interesting, in terms of fitting the data. However, the functional implications are less clear. The work could be extended to show the functional implications of a network with the 3 ingredients: plasticity in the feedforward, in the recurrent and the rate adaptation, leading to this transition between overshoot and damped oscillations.

3) Is this model fully consistent with the experimental results that motivate it? Specifically, wouldn't turning off the image still induce an oscillatory response due to the positive/negative recurrent feedback? This seems counter to work the author cites (Meyer et al., 2014 Figure 5C, D – notice how when a familiar image is presented then left with a blank screen 'F-' there is no oscillation).

4) The paper focuses exclusively on excitatory neurons – is there a good reason for this? Can the model account for both excitatory and inhibitory response dynamics?

5) The author needs to include all the information to reproduce the paper.

6) The writing should be improved for both technical expects as well as a general audience, particularly in the subsection “Interactions between synaptic plasticity and slow negative feedback”.

7) The author must provide code for the reviewers (both for the network with fitted parameters and the code for the fitting procedure) and post the code publicly after publication.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for submitting your article "Mechanisms underlying sharpening of visual response dynamics with familiarity" for consideration by eLife. Your article has been reviewed by two peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Michael Frank as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The reviewers would like to thank the authors for all the work they did. The paper has improved as a result of these clarifications. A few remaining items should be addressed before the manuscript is accepted for publication.

Essential revisions:

1) In the first round of reviews, the reviewers pointed out that the BCM type rule was derived in 2015 assuming that plasticity was only in the recurrent network but in the current manuscript it was applied to a network with feedforward plasticity; the reviewers asked whether the rule should be re-derived. The author reply focused on a normalization procedure applied to the neural data. It is not clear to the reviewers how this normalization procedure relates to the issues raised about recurrent versus feedforward processing. Please justify the use of the BCM type rule in the model with multiple types of plasticity.

2) In the first round of reviews, the reviewers requested that the work be extended to show the functional implications of the proposed network. The authors responded by incorporating a paragraph into the Discussion highlighting the bridge between two classes of models, and these are nice points to make. However, the reviewers would like to clarify their request to complement the current presentation, which focuses on the network architectures required to recapitulate an experimentally-observed phenomenology, with more insight into the functional implications of this work. For example, beyond constraining mechanistic models, why do we care about the damped oscillatory response?

What are its functional implications for representation in IT and/or behavior? What types of functions is a network with the 3 proposed ingredients capable of?
