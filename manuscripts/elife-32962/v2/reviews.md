# Peer review - Round 1

Editors:
- Doris Y Tsao, California Institute of Technology United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.32962.015](https://doi.org/10.7554/eLife.32962.015)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Distinct contributions of functional and deep neural network features to scene representation in brain and behavior" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Timothy Behrens as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The manuscript compares how three models of scene properties explain human behavior (scene similarity judgments) and fMRI activation patterns in scene-selective regions. Behavior can be explained by function/action labels and by features of a deep neural network (DNN). Brain activation patterns, on the other hand, were mainly explained by the DNN features, with little contribution from function/action features (or from the third model, based on object features). The authors emphasize the apparent distinction between behavior and brain activation patterns in their use of functional features.

Overall, this is a very clearly written, straightforward paper. The paper is informative and useful in understanding both the general organization of visual processing brain regions, and the relation between DNNs and human brains. The approach of pre-selecting images to minimize intrinsic correlations between the three feature spaces is clever. There's novelty in how they describe unique contributions of each models: in addition to a conventional RSA correlation, the paper reports results of a variance partitioning analysis along with Euler diagram visualization which allows readers to easily see independent and shared contribution of each models. Experiment 2 logically follows questions from Experiment 1, such as whether the discrepancy between behavioral and fMRI results comes from task differences.

Essential revisions:

1) My main concern was that the authors tend to over-generalize and overstate their results. The results will remain interesting when presented at face value, and the description will be much more accurate.

In an apparent effort to hype up the results (or maybe to keep the conclusions compatible with the previous related paper by Greene, 2016?), the authors insist that functional features explain behavior while DNN features explain brain activity. But in fact, DNN features explain a very large part of behavior as well. It would seem more accurate to conclude that both functional and DNN features explain behavior. As functional features do not contribute to brain activation patterns in scene regions (but DNN features do), there is still an interesting dissociation.

2) The authors talk about "behavior" as if the results could be generalized to any scene categorization behavior. But in practice, the functional (or DNN) features only explain a very specific type of behavior, a scene multi-arrangement similarity sorting task. This limitation is addressed a bit in the Discussion, but I would feel much more comfortable if the authors could systematically qualify their statements about behavior (in the title, Abstract, Results).

3) Similarly, DNN features are referred to as if that was a unique, unambiguous "thing", but there are many types of DNN features depending on network architecture, training data, and hierarchical layer. The authors address the latter two factors to some extent, by reporting correlations with all 8 layers of AlexNet, and with another version of AlexNet trained on places rather than objects. But these are not the only two possibilities. In particular, it seems plausible that a deep network trained on functional (or action) labels for each scene (like the AVA dataset or the YouTube-8M dataset) could behave very differently, and possibly explain more of the behavioral data. In addition, there are many more (and more advanced) image categorization architectures than AlexNet (VGG, Inception, ResNet, etc.). Talking about DNNs "in general" based on data from AlexNet alone is like talking about "mammals" based on mouse data alone. I am not suggesting that the study should include other DNNs, but rather that the descriptions and conclusions should more accurately reflect the actual experimental manipulations.

4) A mild concern is that some of the analysis and interpretations seem too post-hoc. In other words, a theoretical motivation for choosing the three models is not explained enough, other than that these are the models used in a previous study from the same group. These models are chosen with an assumption that feature spaces that were relevant for a behavioral scene study should be relevant for brain responses, which seems natural but creates a disadvantage that each models are not explained/introduced enough to understand why these models may be relevant for behavior and neural representation of scenes. These models deserve more background in the introduction. Are there any alternative models that might contribute which is not tested in their previous study? Does the scene categorization task (similarity sorting) used in behavioral task relates to what the visual system might naturally do while perceiving real world scenes?

5) Overall conclusion and a theoretical take home point seem relatively weak. It is clear that there is a discrepancy between behavioral and neural representations of scenes. What does this tell us about neural representations in scene cortex? For example, a discussion about what exactly different layers of DNN that contributes to neural response is/might be representing should help. It is vaguely mentioned that mid and high level DNN layers play important roles, with specific names of DNN layer, e.g., fc7. However, this doesn't clarify what features are represented in these layers and how it corresponds to different processes involved in scene perception/recognition. Richer introduction and discussion about DNN should help readers understand the theoretical contribution of this work on what and how features are represented in scene perception.

6) What does the current data tell us about existing behavioral findings by Greene et al., 2017? Should the contribution of functional model be interpreted differently and specifically for the behavioral scene categorization task or the types of images (e.g., images with humans/actions) used in the previous research? If not, that should be discussed too. In other words, there needs to be bi-directional discussion between what current discrepancy results inform us about behavioral and neural findings about scene representation.

Minor points [abridged]:

[…] 7.Doesn't the absence of DNN feature space similarity with brain activity (outside of the two small ventral and lateral occipitotemporal clusters) in the searchlight analysis contradict previous findings by Khaligh-Razavi & Kriegeskorte or Guclu & van Gerven? Shouldn't that be discussed explicitly?
