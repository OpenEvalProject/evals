# Peer review - Round 1

Editors:
- Ronald L Calabrese, Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.32605.038](https://doi.org/10.7554/eLife.32605.038)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Comprehensive machine learning analysis of Hydra behavior reveals a stable behavioral repertoire" for consideration by eLife. Your article has been reviewed by three peer reviewers,, one of whom, Ronald Calabrese is a member of our Board of Reviewing Editors and the evaluation has been overseen by Eve Marder as the Senior Editor. The following individual involved in review of your submission has also agreed to reveal his identity: Gordon J Berman.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission

Summary:

This is an interesting manuscript that reports the development a novel behavioral analysis pipeline using approaches from computer vision to assess various natural behaviors compatible with variable observation angles. It extracts visual information from videos of animals with arbitrary motion and deformation. It then integrates a few modern computational methods, including dense trajectory features, Fisher vectors and t-SNE embedding for robust recognition and classification of Hydra behaviors with the bag-of-words framework. The pipeline, which uses both supervised and unsupervised techniques, is suitable for use not only with Hydra, as demonstrated here, but compared with previously developed methods this method is particularly suitable for behaviors in natural conditions that involve animals with deformable body shapes. The pipeline is used to describe behaviors in Hydra and is successful in identifying previously-identified behaviors and novel behaviors not previously identified. The paper then goes on to specify the frequency and variance of these behaviors under a variety of conditions (e.g. fed vs. unfed) and surprisingly found similar behavioral statistics. They conclude that the behavioral repertoire of Hydra is robust which may reflect homeostatic neural principles or a particularly stable ground state of the nervous system. Comparisons with another distantly related Hydra species interestingly reveal some strong differences.

Essential revisions:

The reviewers found that there was a substantial contribution to methodology and behavioral analyses of Hydra in this paper but had concerns that these contributions were obscured by the explanation of the methodology and the presentation and interpretation of the behavioral results. There concerns are well summarized in the thorough review discussion. Reviewer #2 commented "I agree with the importance of quantifying Hydra behavior but have two reservations:

1) The choices for their particular pipeline need to be clarified and discussed. This includes Reviewer #3's concern on the 5-second window but extends to other choices in the stream. As machine learning techniques advance it is getting much easier to represent video information with numbers and I expect that as a result we will see many future advances in behavioral representation. However, these representations are often idiosyncratic and so it is important to understand what aspects are universal, or at the very least include a discussion about various choices. I also think it is important to discuss what kind of behavior might be missing in this approach.

2) They need to do a better job of motivating and discussing the important questions that their quantitative behavioral repertoire can answer. This is the science of behavior not simply representation of videos as numbers. And it's here that we can learn how Hydra compares to worms and flies what we might expect to find in the neural recordings."

Reviewer #3 then commented "I think that Reviewer #2 put it well. I would like to see them talk a bit more about:

1) The motivations for their representational choices and, importantly, the consequences and implications that these choices have.

2) How they anticipate using these numbers to answer biological questions. Any measurement representation should have a rational relationship to the questions being asked, so addressing what their method will be useful for (and what it won't be useful for) will be valuable for the literature moving forward. Will this simply be a better detection technique, or does their unsupervised approach allow the field fundamentally new types of behavioral measurements?"

These concerns and the minor issues from the original review that are appended can form the basis of a revision that clarifies the methodology and brings out the behavioral significance revealed by the new methodology.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Comprehensive machine learning analysis of Hydra behavior reveals a stable behavioral repertoire" for further consideration at eLife. Your revised article has been favorably evaluated by Eve Marder (Senior Editor), a Reviewing editor, and three reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

The authors have endeavored to address many of the major concerns of the previous review with further explanations of the method and its underlying assumptions and method choices, and the inherent limitations of the method/analysis. They have also tried to clarify how their method can be used to answer biological questions. There is still one major concern.

1a) The authors should try windows greater than 5 seconds. It's hardly surprising that less than five seconds is less effective, but why not 8, 10, 20? Just saying "we noticed 5 seconds is a reasonable length to define a single behavior" is hardly convincing (neither is Figure 1C).

1b) It still remains possible that the highly-fragmented t-SNE representation results form the fact that behaviors are unnecessarily chopped-up by imposing a 5 second window. Problems might occur because the behavior spans a window boundary. The analysis should be performed using a sliding 5-second window rather than separated windows. This may remove some of the observed over-segmentation of the space. There are several methods (including one in Berman, 2014, but others as well) for handling tens to hundreds of millions of data points. Since the space is one of the cruxes of the paper's arguments, and the authors might get better results with the sliding window, it seems somewhat remiss to not attempt this (it would be ~ 24 hours of running time on a machine that can handle a 30,000-point t-SNE). The Barnes-Hut implementation from: https://lvdmaaten.github.io/tsne/ may prove helpful.
