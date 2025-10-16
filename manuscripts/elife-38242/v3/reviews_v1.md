# Peer review - Round 1

Editors:
- Eilon Vaadia, The Hebrew University of Jerusalem Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.38242.sa1](https://doi.org/10.7554/eLife.38242.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

[Editors’ note: the authors were asked to provide a plan for revisions before the editors issued a final decision. What follows is the editors’ letter requesting such plan.]

Thank you for sending your article entitled ""Artiphysiology" reveals V4-like shape tuning in a deep network trained for image classification" for peer review at eLife. Your article is being evaluated by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Joshua Gold as the Senior Editor. The reviewers have opted to remain anonymous.

Given the list of essential revisions, including new experiments, the editors and reviewers invite you to respond within the next two weeks with an action plan and timetable for the completion of the additional work. We plan to share your responses with the reviewers and then issue a binding recommendation.

Summary:

The reviewers who read this paper had quite different views. In my role as the reviewing editor, here I integrate and summarize the different impressions and comments and provide the authors with some recommendations to revise the paper and best respond to the comments to improve the manuscript, with my hope that it will be possible to reconsider publication of this study.

This paper examines the hidden units of deep networks trained on image classification in order to determine whether their tuning properties are similar to those that have been reported previously in primate visual area V4. The authors probe a pre-trained deep network (AlexNet, used in many other computational neuroscience studies) with simple closed-contour binary shape stimuli. These stimuli were used in previous impactful neurophysiology studies from this group to probe contour curvature and angle tuning in area V4.

The paper reports three main general results. First, it shows that some units within the deep network can be well described by a model contour curvature model of V4 selectivity (the APC model) that was developed previously by the authors. Second, it shows that the deep network units well described by APC model also exhibit position invariance, similar to that observed in real V4 neurons and reported in several previous studies. Third, the authors use a network visualization method to show that deep network units well described by the APC model are predicted to be selective for a range of complex natural images and that the best natural images evoke larger responses from the APC units than are obtained using the simpler stimuli.

This is a well written and clear paper. The computational analyses appear to be solid. Treating a deep network trained on a natural image classification task as an object of synthetic neurophysiological investigation is an interesting enterprise, and it is gratifying to see the correspondence between units in the deep network and V4 neurons that are well fit by the APC model.

The "major concerns" section below provides details of the major question that we have faced, which is: What is the added value of this well-written paper? We see it in two almost opposite ways;

1) The paper has a significant and general value in highlighting the potential of advantages of computational models in interpreting neurophysiological data and cortical computations, as well as a potential of learning from neurophysiological data how to improve computational models.

2) The paper does not provide new insights. Instead, it is a reasonably good paper, oriented to a local community, that confirms the notion that hierarchical networks (either biological or artificial) end up representing similar hierarchical structure in natural images.

Essential revisions:

Most researchers agree that the critical questions regarding modeling of sensory system at large are the practical ones: (1) What stimulus should be used in neurophysiology data collection? (2) How much data should be collected? (3) How should models be validated? (4) What modeling framework should we use? The authors are invited to clarify and explain how the paper appropriately relate to these questions.

At some level, it seems like this study has to work out the way that it did. As several recent neurophysiology modeling studies using deep networks have argued, both deep networks and the primate visual system were "trained" (or evolved) using analyze natural images, and it is not surprising that both hierarchical networks end up representing similar hierarchical structure in natural images. From that point of view the results of the manuscript are unsurprising. The two major conclusions of the paper are that units in deep networks trained on classification and well fit by the APC model show selectivity for contour curvature and that they are locally positioned invariant. Both of these observations are completely consistent with an enormous amount of prior data. A wealth of prior research suggests that object borders are important for vision. Theoretical arguments suggest that object borders are a critical component of any viable representation of the objects in natural scenes, and many previous neurophysiology studies using both synthetic and natural images have shown that units in V2 and V4 are sensitive to object borders including curved borders. The demonstration that deep networks are positionally invariant is also not surprising. After all, the deep networks tested here are convolutional and therefore are designed to be locally positioned invariant. In fact, convolutional networks were inspired originally by the finding of position invariance in primate vision.

The important question, therefore, is not whether there is any correspondence between the tuning of visual neurons and the tuning of units in deep networks trained for image classification. Instead, the important questions concern the nature of this tuning, the distributional relationships between primate neurons and units in the deep networks and, ultimately, what that can tell us about the biophysical mechanisms underpinning the observed functional selectivity.

We would have been more enthusiastic if the analysis could reveal some new principles that could provide impetus to further experimental studies, or which could be used to help improve current models. For example, if the current deep network framework could support some fundamentally new approach to interpreting functional responses that would provide a foundation for building a mathematical model that can explain observed functional properties in terms of known biophysical building blocks present in cortical neurons, or if the deep networks could be used as the building blocks for such a model.

At this point, this is a well-done study that supports the current view that the primate visual system and deep networks trained on natural image classification both encode intermediate object structure such as contour curvature. However, this paper as written doesn't resolve controversies and doesn't provide information that would be useful for designing future experiments or models.
