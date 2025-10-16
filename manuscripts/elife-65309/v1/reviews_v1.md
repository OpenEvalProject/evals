# Peer review - Round 1

Editors:
- Maria N Geffen, University of Pennsylvania United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65309.sa1](https://doi.org/10.7554/eLife.65309.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

Your paper identifies an important mechanism for generation of novelty signals. It expands current understanding of the functional role of inhibitory plasticity, and makes predictions that can be tested experimentally in future studies.

Decision letter after peer review:

Thank you for submitting your article "The generation of cortical novelty responses through inhibitory plasticity" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Maria N Geffen as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Joshua Gold as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Please revise the paper to address the specific points raised by all reviewers.

2) Addressing points 1, 3, 4, 5 and 7 by reviewer 1 and points 1, 2, 3 and 5 by reviewer 3 will likely require additional evidence and discussion.

Reviewer #1 (Recommendations for the authors):

This is an interesting and well-written paper which presents the results of a model for cortical plasticity and resulting increase in neuronal responses to unexpected stimuli. Overall, this is an elegant study that provides a number of interesting, experimentally testable, hypotheses and develops a prediction for a mechanism for novelty response generation. The results are clearly presented. We have several suggestions that should allow to better integrate the study with known experimental results.

1. Whereas the authors use the term "novelty" response, it is unclear whether this is a true novelty response because a number of stimulus parameters differs from those identified in the literature. The network is not sensitive to temporal structure, which suggests that it does not completely replicate certain aspects of neuronal adaptation in cortex. MEG studies in humans (work from Maria Chait's lab), and Yaron et al., 2012 (SSA under different contexts in rats) all suggest that cortex should exhibit a differential response to different sequences of stimuli drawn from the same distribution. What modifications to the model would produce adaptation to temporal structure of the stimuli?

2. Figure 2 provides support for a key result of Homann et al., 2017. It would be interesting to see if the network behaves similarly with more complex stimuli and generates novelty responses to complex stimuli. In Homann et al., 2017 experiment, the stimuli were scenes comprised of many Gabor patches. These could potentially broadly activate visual cortex as opposed to the "simple" single stimuli used here. It would be interesting to consider how a broader pattern of stimulation would affect the results.

3. In the experimental results, a large majority of individual neurons exhibited the novelty response. Does this also occur in the model? Would it be possible to present statistics and single-neuronal data in addition to the population mean responses?

4. It is unclear how duration of pre-training relates to plasticity and novelty responses (Figure 4B). Would you expect increased pretraining duration affect the novelty response behavior? If so, perhaps the duration of pre-training should be varied systematically? Furthermore, how does the number of pre-training stimuli affect the performance?

5. It is difficult to interpret the differences in adaptation between different repeated stimuli (Figure 4C bottom -> green vs blue lines) as compared to the differences between the "late" and "intermediate" time points (4D bottom). Results depicted in figure 4D suggest multiple timescales of adaptation. Are the differences in 4C, which seem to be of similar magnitude, meaningful?

6. One of the primary findings of Natan et al., 2015 was the differential effect of optogenetic disinhibition of SOM vs PV interneurons on the SSA response. The differential effect is seen when disinhibiting the standards -1, +1, +2 etc. relative to the deviant. It would be interesting to see what the effect of disinhibition is on the network response (Figure 6), and how it relates to Natan's findings.

7. The motivation for having different STDP learning rules for E->E and I->E connections is unclear, other than citation of previous work. Can you please explore in more detail the differences between these learning rules?

8. An emerging theme from this paper and from other models such as Yarden and Nelken, 2017 and Park and Geffen, 2020, may be that the tonotopic organization of similarly tuned neurons helps facilitate adaptation. Tuned assemblies were a key feature of the models in these papers. Here, the tonotopic organization arises from the STDP rule here, and it would be interesting to discuss the relationship between tonotopic organization and plasticity.

9. Seay et al., 2020, have considered plasticity rules in adaptation as a function of facilitation of specific inhibitory interneurons in SSA. It would be interesting to speculate whether and how this model and the learning rules relates to those published results.

Reviewer #2 (Recommendations for the authors):

The units of the learning rate n of inhibitory plasticity on page 18 is listed in uF and only very briefly discussed? Since eta seems to be relatively important for the novelty detection, and determines e.g. how many trials a system will typically require to learn a stimulus (see also Figure 2) it should thus be discussed in more detail, possibly with an additional set of simulations that are complementary to those in Figure 2.

The inhibitory learning rule used here is stated to be confirmed on p. 15. This is arguable, and the jury may still be out. It may be worth discussing how other rules would perform?

Reviewer #3 (Recommendations for the authors):

1. The abstract is a bit cryptic: it states that "inhibitory synaptic plasticity readily generates novelty responses". Inhibitory plasticity is rather vague, it is necessary to read quite far into the results to figure out if the key is short-term synaptic inhibitory plasticity as in a number of models, or some form of long-term associative synaptic plasticity. The abstract should be more informative and explicitly state that the model relies on STDP of Inh->Ex synapse.

2. It would be helpful to provide a bit more information about the model architecture in Figure 1 and the start of the Results section so the reader does not immediately have to go to the Methods section (e.g., network size, ratio of E/I neurons, no STP).

3. In the Methods it would also be helpful to plot the STDP function for excitatory and inhibitory plasticity for spike pairs.
