# Peer review - Round 1

Editors:
- Mark CW van Rossum, University of Edinburgh , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.20147.027](https://doi.org/10.7554/eLife.20147.027)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Understanding both enhanced and impaired learning with enhanced plasticity: a saturation hypothesis" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Timothy Behrens as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

While over the years the link between learning and synaptic plasticity has become tighter and tighter, the effect of changes in plasticity can sometimes be puzzling. Nguyen-vu et al. use a relatively simple and well-studied form of cerebellum-dependent motor learning to explore the issue of how genetically enhanced synaptic plasticity impacts learning. Combining behavioral genetics, in-vivo physiology, computational modeling, and mathematical analysis, they conclude that enhanced LTD can lead to both an increase and a decrease of the VOR depending on the history of synaptic changes and the details of the synaptic plasticity model.

Essential revisions:

– The different models used by the authors assume that LTD transition probabilities are increased in KO mice compared to WT, but that LTP transition probabilities are unchanged. As a result, baseline synaptic strengths should be lower in KO than in WT. Some of these authors have presented data in the McConnell et al. 2009 paper, where the amplitude of baseline EPSCs is shown in Figure 3, but it is not fully clear there whether they are identical in WT and KO.

If they are identical, then this data might be consistent with a model in which the LTP transition rates are also increased, so that the baseline synaptic strengths are identical in both types of mice. Does such a model reproduce the data? Alternatively, if the McConnell data show a difference in WT and KO amplitudes, it would be interesting to directly compare this to the model.

– Generally the parameter space of the models is not very well analyzed. So the reader is left with the impression that parameters are chosen such that the effect can or cannot be reproduced. Particularly for the model classes that do not allow analytical arguments a more comprehensive parameter check is necessary, or the choice of the parameters has to justified more convincingly.

– Concerning the optogenetic experiments: If the optogenetic experiments really provide a test of the ideas regarding cascade models, then this experiment should be explicitly modeled using the various different plasticity models discussed. If the optogenetic results are also predicted by standard/simpler models then the discussion of this experiment and its significance should be modified, i.e. toned down, accordingly.

– Are other cell types in cerebellum or vestibular system affected by the mutation? If so this should be mentioned and the implications discussed.

– There are a number of straightforward experimental predictions that naturally follow from the model that are not mentioned by the authors. One straightforward prediction is that with enough VOR-increase training, the advantage of the KO mice should eventually disappear, and in fact the WT should again become better, since the memory of initial conditions should eventually decay away. I am not suggesting the authors perform the corresponding experiments, but I believe it would be good to clarify this issue in simulations.

Related to that, in the Discussion section, the authors write “Within a given training session, VOR learning appears to asymptote within a few tens of minutes”. This does not seem to be true in the experiments reported in Figure 2. These experiments leave open the possibility that these effects are only transient, and that given enough time WT and KO would reach the same level of learning.

Finally, the issue of time scales needs more discussion. For instance, on longer time scales already the 2 state model WT can overtake the KO (the top one in Figure 3B).

– The rates of activity in granule cells in the flocculus in vivo seems important for the modeling but has never been directly measured. Granule cells might be expected to fire very little spontaneously. What rates were assumed in the model? How do conclusions of the model depend on assumed activity levels in granule cells?

– A previous study by McConnell et al. found that rotorod learning and retention was enhanced in the same mutant mice. This seems at odds with the present findings. The authors should discuss possible explanations based on their work.

– The Abstract and Introduction should be rewritten to deal more fairly with the previous literature. While the combination of techniques is novel, many elements are not. The manuscript falls short of acknowledging the fact that many researches since several decades have been studying these types problems from a variety of directions sometimes termed "plasticity stability dilemma". Just to name a few of these approaches:

a) From the theoretical perspective palimpsest models (Amit and Fusi, 1994; and many others) have very early laid out early on that an increase in learning rate also increases forgetting. b) Studies on trafficking of receptor molecules come to similar conclusions (reviewed in Gerrow and Triller, 2010) c) Papers on synaptic metaplasticity and tagging/consolidation raising similar problems

[Editor’s note: Further clarifications were requested on acceptance. The authors’ response follows.]

Congratulations, we are pleased to inform you that your article, "A saturation hypothesis to explain both enhanced and impaired learning with enhanced plasticity", has been accepted for publication in eLife.

While over the years the link between learning and synaptic plasticity has become tighter and tighter. The effect of changes in plasticity can sometimes be puzzling. Nguyen-vu et al. use a relatively simple and well-studied form of cerebellum-dependent motor learning to explore the issue of how genetically enhanced synaptic plasticity impacts learning. Combining behavioral genetics, in-vivo physiology, computational modeling, and mathematical analysis, they conclude that enhanced LTD can lead to both an increase and a decrease of the VOR depending on the history of synaptic changes and the details of the synaptic model.

Reviewer #2:

I feel the authors have largely done a good job in revising the manuscript.

The discussion of time scales has not become as transparent in the main text as I initially hoped, but the treatment in the Appendix is fine.

I'm still not fully satisfied the new statement "Whereas the plasticity stability dilemma is a memory deficit with enhanced plasticity, what we are reporting is a learning deficit." In fact people know about "Learning" problems related to too high learning rates in neural networks since half a century. E.g. see any textbook on the perceptron rule or gradient decent rule etc.

Reviewer #3:

I am generally satisfied by the revisions made by the authors.

However, I am somewhat disappointed by the answer to the first issue

(whether baseline EPSCs have different amplitudes in WT or KO).

I would have imagined that in such experiments stimulation strengths are recorded by the experimentalist. But of course I have never done such experiments, so I am not really qualified to make such a statement.
