# Peer review - Round 1

Editors:
- Srdjan Ostojic, https://ror.org/05a0dhs15 Ecole Normale Superieure Paris France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69841.sa0](https://doi.org/10.7554/eLife.69841.sa0)

This paper will be of interest to neuroscientists studying the navigation system, and in particular, those who study the ability of animals to path integrate. This study proposes an elegant synaptic plasticity rule that maintains the connectivity required for path integration by integrating visual and self-motion input arriving at different dendritic locations in a neuron. This idea is applied to the central complex of Drosophila, a well-characterized experimental system.


---

# Peer review - Round 1

Editors:
- Srdjan Ostojic, https://ror.org/05a0dhs15 Ecole Normale Superieure Paris France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69841.sa1](https://doi.org/10.7554/eLife.69841.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Learning accurate path integration in ring attractor models of the head direction system" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Ronald Calabrese as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Hervé Rouault (Reviewer #4).

The reviewers have discussed their reviews with one another, and believe the manuscript is potentially suitable for publication, provided a number of comments are addressed or discussed. The Reviewing Editor has drafted a merged feedback to help you prepare a revised submission.

Essential revisions:

Plasticity:

– A main question is whether the type of synaptic plasticity proposed by the authors is necessary and operative in the CX. One motivation for the plasticity rule is that, as the authors state, ring attractors "require that synaptic connections are precisely tuned (Hahnloser, 2003). Therefore, if the circuit was completely hardwired, the amount of information that an organism would need to genetically encode connection strenghts would be exceedingly high." However, in Figure 3 and S3, it is shown that the learnedPI "far outperforms" flies, so the authors add random noise to the synaptic weights in order to make a more realistic model. But this means that the synaptic weights don't actually need to be that precise. Doesn't this mean that the connectivity may in fact be genetically encoded?

– Another proposed function of the plasticity rule is in adjusting to changes in relative gain between proprioceptive signals. The authors cite Jayakumar et al. (2019) in the introduction as motivation for this, without noting until later that the study used rodents rather than flies. In the discussion, it is mentioned that Seelig and Jayaraman (2015) actually did not find evidence for gain adjustments in flies. This seems to go against the plasticity mechanism being proposed as being relevant for flies. Is there any evidence for this in flies?

– Biologically plausible learning rule: One of the main assumptions that allows the authors to claim for a biologically plausible learning rule is that the 'firing rate' of the neuron is available for all synapses at the axon-distal compartment due to the assumed back-propagation (line 167). As this seems to be crucial, it will be good to give references showing that there is a back-propagation AP in E-PG neurons, or to explain what the alternatives are.

– Writing style: The paper would be easier to understand if some of the key relevant equations, for example those that describe the synaptic plasticity rule, were included in the main text.

– Analysis of connectome data. The connectome data is a nice support for why using a learning rule that relies on a two-compartment model. However, some points could be clarified. What is exactly is X,Y position? Can the authors plot the shape of the neuron on the same plot, and maybe also to give access to a 3D video of this cloud points? Also, why showing only 1 example, instead of analyzing all the EPG neurons and showing all of them in a supplementary figure. Then, the authors should do a statistical analysis to support their claim, such as doing some clustering analysis. You want to at least convince the reader that you can reject the null hypothesis that inputs are not segregated.

– Predictions: It would be good if the authors could try and give more concrete predictions, or better, suggest testable predictions. While a theory doesn't have to give predictions, as mentioned in the public review, in this specific case it would be good if the authors could spend one or two paragraphs on concrete predictions and maybe even suggest new experiments to the community. In other words, while not necessary for publishing the paper, the authors could go beyond saying that PI requires supervised learning during development, which seems more like a hypothesis of the model than a real prediction.

– Network initial architecture: It is not clear how the results depend on the specific initialization of the network and how sensitive the main conclusions of the paper are to these choices. More specifically:

– It is not completely clear what the initial recurrent connectivity in the network is, and how the results depend on this choice. For example, does the symmetry, which the authors rely upon to derive their reduced model, persist if the initial connectivity is random?

– Would the results and conclusions of the paper change if the authors use a different choice of the HD->HR connections? Could they be random? Could they be connected to more than one neuron? Could they be plastic as well?

Related to this issue, in line 266 the authors claim that 'circular symmetry is a crucial property for any ring attractor'. While this might be a common knowledge in the field, please see Darshan and Rivkind 21 that argue against it. Following this, it is unclear if symmetry is needed for the authors to derive the reduced model, or if it is a principle that they think the system must have. The former is rather technical, while the latter is an important principle. It would be good if the authors could address this in their discussion.

– Saturation: It seems that saturation is crucial in this work. Is it known that E-PG neurons reach saturation levels? For example, in cortex this rarely happens, where neurons are usually active around an expensive non-linearity regime and are far from saturation. It will be beneficial if the authors could show that similar phenomena hold with different types of non-linearities, in which neurons are not saturated. Alternatively, the authors can explain in the manuscript why they think that E-PG neurons in reality are saturated (maybe give references?).

– Line 221 (and 389) "…our work reproduces this feature of the fly HD as an emergent property of learning". It is not clear what the authors mean by this. Is the impairment of PI in small angular velocities a result of the finite number of neurons in the network, or an emergent property of the learning? For example, what would happen if the authors would take 2000 neurons, will they still see this 'emergent property'? This also goes against what is written in Line 465 of the discussion.

– Timescales: there are many timescales in the model. Although it is addressed, to some extent, in the supplementary material, it would be good to add a paragraph stating what are the requirements on these timescales. For example, does the model fail if one of the timescales is smaller\larger than the others? Did the authors assume in the derivation that one timescale is slower than the rest? Why tauδ can be ignored in the derivation? Can the authors show the failure modes of the network\derivation when changing the timescale?

– Randomness in network connectivity- Figure S3. In case of the random connectivity, as the network is so small, the behavior of the network depends on the specific network realization and, therefore, it is hard to assess how representative FigS3D-E are. it will be good to show some statistical analysis of the diffusion across these networks.

– Noise in the dynamics- Figure S4. It is unclear if the diffusion is larger in this case just because the authors added noise, which stays after training, or it is something deeper than that. Could the authors compare the diffusivity in networks that were trained with and without noise? Also, in FigS4 panel E- it seems that in contrast to the finite-size network effects, in this case there is no problem to integrate at very small velocities. Why is that? Does the noise contribute to smoothing the barriers and helps to go from a discrete to a more continuous representation when doing PI? Does this have to do with the small number of involved neurons in the fly central complex? One of the reviewers disagrees with the remark about a feature build-in by hand in previous models l220-222. This is not something the learning rule per se allows to understand.

– What is the limitation of the adaptation in the network? For example, the authors claim that 'we test whether our network can rewire to learn an arbitrary gain between the two', but in fact only showed examples for a 50% increase or decrease in gain and only mentioned a negative gain without showing it. It will be useful to have a figure, showing how the performance varies with changing the gain. Is there a maximal\minimal gain that above\below it the network always fail to perform? Which of the network parameters are important for these gain changes?

– The authors seem to assimilate path integration with angular integration (l31-40). The way insects manage to perform path integration (i.e. integrate distances) is still undetermined to our knowledge. Clearly, the angular integration performed in the central complex is not enough. The authors should try to disambiguate this point.

– The authors mention the existence of two PEN populations (PEN-1 and PEN-2). Could the proposed model could shed light on the presence of these two populations. Would they account for the inhibitory and excitatory part of the HR curves on Figure 3C?

– On l 625, the authors state that the constant inhibitory drive contributes to the uniqueness of the bump. One of the reviewers was not convinced of this statement as this constant inhibition does not play a role in the competition between several bumps. Only the inhibitory recurrent connectivity within the HD population or going through the HR populations would play such a role.

– In Figure S5B, the bump velocity goes to zero around 500º/s. Could this come from a defect in the network that would, for instance, abolish the presence of a bump in left and right HR populations? In a more robust behavior, only one of the left or right bumps would disappear, and the HD bump would go at a max constant velocity.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Learning accurate path integration in ring attractor models of the head direction system" for further consideration by eLife. Your revised article has been evaluated by Ronald Calabrese (Senior Editor) and a Reviewing Editor (Srdjan Ostojic).

The manuscript has been much improved but there are some remaining issues related to the lack of evidence for plasticity in CX. After consultation, the reviewers agreed that the current lack of evidence for plasticity should be pointed out earlier in the manuscript, and suggested presenting the need for plasticity in younger flies as a prediction of the model. One of the reviewers provided additional suggestions listed below.

Reviewer #2 (Recommendations for the authors):

The authors have made a number of improvements to the manuscript. My central concern, which is that there isn't any evidence for this plasticity being present in the CX, still stands. Obviously, a purely modeling study is unable to address this concern. The authors have argued in Appendix 3 that asymmetries in the architecture can severely disrupt the performance of the model and that this supports the need for plasticity. Here are a few suggestions related to this central issue.

1) The authors refer to the performance of flies from Seelig and Jayaraman (2015), stating at various points whether their models outperform the actual performance or not. This should actually be quantified in the figures and/or text. Specifically, both Figure 2 and Appendix 3 would benefit from a quantitative comparison to real fly performance.

2) It would be useful to show how much imprecision must be added to the synaptic connections before the model can account for the performance of actual flies. This would answer the question of "how much precision must be genetically encoded to account for fly behavior."

Reviewer #3 (Recommendations for the authors):

I find the paper to be timely and very interesting. The paper was well presented already in the first version, but I did have a few concerns. The authors did a great job in addressing all of these concerns and comments in the new version of their manuscript.

I strongly recommend it for publications in eLife.
