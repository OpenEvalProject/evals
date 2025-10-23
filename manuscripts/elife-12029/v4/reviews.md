# Peer review - Round 1

Editors:
- Upinder S Bhalla, National Centre for Biological Sciences , India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.12029.013](https://doi.org/10.7554/eLife.12029.013)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for choosing to send your work entitled "TANs adjust striatal learning as a function of population uncertainty: Computational models in stochastic environments" for consideration at eLife. Your full submission has been evaluated by Timothy Behrens (Senior editor) and three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the decision was reached after discussions between the reviewers. Based on our discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife in its current form.

The reviewers felt that the modelling and results sections were not explained with sufficient clarity for them to properly evaluate the manuscript. They felt that the question was important and that the findings would potentially be important. However, on top of technical questions, there were substantial concerns about the clarity and articulation of the work, which meant that the reviewers were not comfortable offering a clear recommendation.

The reviewers all agreed that there were some specific aspects of the paper presentation that needed to be addressed should the authors wish to resubmit the paper:

1) The model and previous work were poorly explained, figures incomplete and the explanations assumed familiarity with the authors' previously published work.

2) It would be desirable to have more detailed figures of activity and connectivity in the network, rather than high-level summaries.

3) The relationship to experiments should be much better defined. Specific model explanations and predictions of experimental results should be presented.

4) The use of the terms 'entropy' and 'uncertainty' was unclear and needs to be better defined and motivated.

In addition, each of the reviewers felt there were specific gaps in the completeness of the study that weakened its conclusions. These are detailed in the reviewer comments. At least some of these specific suggestions should be incorporated, should the authors wish to resubmit the paper.

The two technical points that raised most concern in reviewer discussions were the points that relating to the effect of rebound phase after the TAN pause (Reviewer 3 point 1), and the possible mechanisms for computation of uncertainty or entropy within the network.

Reviewer #1:

This study pulls together existing models of reinforcement learning and several streams of experimental results to develop an interesting model of learning in a changing environment.

The study develops a model of a striatal learning, adding a critical component by asking what would happen if variability in the MSN pool could be treated as a measure of uncertainty about a changing environment. Under such circumstances, the authors show how modulation by TANs may allow the network to improve its learning rate depending on uncertainty.

Major comments:

1) I had some difficulty understanding how the TAN input acted on the MSN population. This was presented in the text in words, and in the figures through secondary readouts such as accuracy and entropy. I would like to see the simulated activity patterns (e.g., spike rasters) reported for TANS and MSNs in the various conditions. Additionally, an input-output relationship of TAN activity, pauses, and MSN excitability would help to clarify the physiological assumptions of the model.

2) As per Methods, the time constant of the TANs "was transformed such that pause duration in the network varied linearly with entropy."

I was disappointed that the study fell short of modeling how the TANs would compute the entropy of the network. This is just plugged in to the firing patterns. Given that the model incorporates the MSN population, it would have been nice to see a mechanistic implementation of the entropy computation step. The authors don't clearly state a mechanism for this: the closest sees to be a line in the Discussion:

"A measure of uncertainty could be approximated by summing the activity over multiple sources, either directly from MSNs or indirectly through other interneurons. "

I'm not sure how just summing activity will give this measure. I feel that the authors must suggest a more detailed mechanism for this essential step. I would strongly prefer that they also model such a mechanism; it would complete a missing link in the model.

Reviewer #2:

This paper addresses the question of reinforcement learning in an uncertain environment. The theoretical premise is that common reinforcement learning algorithms are not sensitive to uncertainty, and would not operate well in such an environment. They propose that Cholinergic interneurons in striatum can sense this uncertainty and modulate circuit dynamics and plasticity to make the system operate better in an uncertain environment.

Major concerns:

The notion of uncertainty is not well defined here. I suppose they mean an uncertain environment, but this in itself is still not well defined. It could be an environment that is not stationary as in a reversal task, or an environment in which reward is uncertain, that is a reward is given just with a certain probability. This is just the beginning of the problem here, because the uncertainty of the environment becomes confounded with the response distribution of MSN neurons.

This is a complex rate based network, and its behavior is not at all clear. This seems like a deterministic system, so why does it have any entropy? Entropy seems like an important concept here because somehow entropy of the network represents the uncertainty of the environment. I think what they do is that they make a histogram of (deterministic) network activity and use that as a probability distribution (even though the N dim state space is unique) and use that for the "Entropy" calculation. Note though that the network has no uncertainty. The term entropy here seems to obfuscate rather than clarify, but I think what they mean is that in an uncertain environment the network response is more spatially variable than in a certain environment. This leaves many questions. First, what is the origin of spatial variability in this network? I don't know how many units there are in this network, and have no idea why different units do not respond identically. Second, if there is this mapping from uncertainty to network variability, how does this happen? This is an example of a general problem with this paper, they run complex simulations and treat the results as an experimentalist would they describe the results, but seldom explain why the network generates these results.

The model needs to be rewritten. For example the acronym TAN is used in the title. How should a reader, who is not exactly in the same field, know what TAN's are? The Abstract is very technical, and can really only be appreciated by a very small group of scientists. Additionally, some statements that are made are too strong. For example the sentence: "The basal ganglia support adaptive reinforcement learning in accordance with algorithms that adjust action values using a static learning rate." Is this a fact, or a postulate supported by some evidence? Additionally, the rest of the paper is also hard to understand. The methods relay on previous papers, and there is never a good heuristic explanation of the network behavior. Even the training task is badly described, has no figures, and is mostly in the Methods section.

There is hardly any physiological data that this model is trying to account for, if it exists it is not evident in the paper. So this is a complex network, accounting for behavior, but it can receive little validation at the physiological level. Do we need this much complexity given the current state of the experimental data?

Reviewer #3:

This is an interesting manuscript, which incorporates ChIs into a basal ganglia model. ChIs are of ever-growing interest because of their increasingly apparent involvement in key functions of the basal ganglia and dysfunction in disease. The timely manuscript by Franklin & Frank is a follow-up study by this group (Frank, 2005). The authors incorporate striatal ChIs into their previous computational model which successfully mimics the basal ganglia function in normal and Parkinsonism conditions. In this study, the authors tested the role of ChIs in acquisition and reversal learning, by simulating M1, M2 receptormediated currents on medium spiny neurons (MSNs) and nicotinic receptor-mediated currents on GABAergic interneurons. The results replicated the experimental observations. In addition, the authors claimed that MSN entropy and ChIs pause feedback mechanism might control the pause duration which reveals a tradeoff between asymptotic accuracy and flexible learning.

This is an interesting and timely model but I have some concerns.

1) The major concern is that the model ignored the rebound phase of the pause response. The lack of this component will significantly lower the power and impact of the model. Compared to the initial excitation, which is only observed in about half of TANs, the rebound of the pause response, which has similar duration as the pause, is much more consistent observed across TANs (Aosaki et al., 2010). Combined with the facts that dopamine signals in striatum might last longer than phasic activities in cell bodies, and that the model only includes fast responses in MSNs, i.e. excitatory, inhibitory and leaking current, will the rebound of the pause response rewrite the learning process?

2) The authors propose a feedback loop from MSNs to ChIs. Although activating MSNs can induce inhibitory currents in ChIs, the currents are thought to be weak (Chuhma et al., 2011). Also the MSNs have very low firing frequency (Berke et al., 2004). Will these facts influence the conclusion of feedback loop of MSNs and ChIs? The conclusion that inhibitory currents from MSNs will slow the firing rate of ChIs is natural, especially from a model's point of view, but is that reasonable when compared with experimental data? Any justification, like the inhibitory current intensity, or average firing rate of MSNs needs to be provided.

3) The model used Go and NoGo units activities to represent the "weight for specific actions" and "the evidence against particular responses" respectively. At the same time, the model claimed that Go neurons are striatonigral MSNs and NoGo are striatopallidal MSNs, and further used their electrophysiological data, e.g. M1 only act on striatopallidal MSNs. This is a common setup of computational models, however, the reversal learning process, e.g. left v.s. right turn (Ragozzino et al., 2002), lever press for food v.s. water (Bradfield et al., 2013), are task choices rather than task stops. Is it appropriate to use Shannon's entropy across the population of MSNs here?

4) It would be useful to have the duration of pause in time rather than 15-25 (Figure 3, Figure 5, Figure 6).

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for resubmitting your work entitled "A cholinergic feedback circuit to regulate striatal population uncertainty and optimize reinforcement learning" for further consideration at eLife. Your revised article has been favorably evaluated by Timothy Behrens (Senior editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors. The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

The reviewers all felt that the paper was significantly improved from the previous submission, but that there were important aspects that needed to be addressed.

1) The model lacked a rebound phase in the pause response. The authors should analyze whether this might alter learning processes.

2) The authors should address the possibility that pause duration in TANs may simply reflect excitatory and DA input.

3) The authors must clear up a continuing lack of clarity about how uncertainty maps to entropy, stochasticity, and to sparseness of the distributed response.

4) The authors should address the concern that the presented model is complex yet at the same time biophysically implausible. Can they embed the core concepts in a much simpler model?

5) The authors should make extensive improvements in clarity throughout the paper, as indicated in many comments by the reviewers.

6) The authors should also suggest some other simple testable predictions in addition to the ones mentioned in paragraph nine, Discussion.

Reviewer #1:

Significance:

This modeling study considers how striatal reinforcement learning may incorporate uncertainty about the environment into controlling learning rate. This allows the system to ignore chance fluctuations in reliable environments, but also to learn more rapidly in cases where the environment is changeable. The revision is considerably improved and addresses all the main concerns I had previously raised.

Major comments:

1) Figure 8 results are good to see, they take the argument full circle by showing that a purely network-based implementation is able to achieve high performance in changing environments by appropriate control of TAN behavior.

2) The implication of Figure 6 is a bit confusing, especially the last panel. How do the network weight differences map to the performance in Figure 5? What would be a good outcome from the point of view of performance? Is the black line close to optimal?

Reviewer #2:

This manuscript incorporates cholinergic interneurons (Chls) into a basal ganglia model built by the same group (Frank, 2005). It is good to see that authors incorporate striatal ChIs into a computational model and simulated the interaction between spiny projection neurons and TANs. With this new model, the authors successfully tested their hypotheses of 1) changing of the duration of 'pause' in TANs could affect the balance of asymptotic accuracy and flexible learning in striatum, and 2) the spiny projection neurons and TANs system showed self-tuning property in learning rate and optimizing performance across stochastic environment.

This is an exciting model with some concerns.

1) The missing of rebound phase of the pause response will significantly lower the power of the model. The initial excitation of the pause response, which is included in the model, is only observed in about half of TANs. However, the rebound of the pause response showed in all the reported pause response (Aosaki et al., 2010). While the dopamine signals last longer in striatum than the phasic activities in cell bodies, will the rebound component of the pause response re-write the learning process, which built only upon the initial excitation and pause, of the model?

2) The hypothesis of the duration of the pause in TANs affecting the learning process is clever. However, the original studies of the pause response only compare the durations of pauses that are induced by aversive and appetitive stimuli (Apicella et al., 2009; Ravel et al., 2003). As mentioned in the Discussion, the model would not be suitable for the animals that are well trained. It is a little bit hard to argue the interaction between spiny projection neuron and TANs play the important role in regulating pause duration. Would it be possible that the pause duration in TANs might only reflect the excitatory and dopamine input (Ding et al., 2010)?

Reviewer #3:

This version of the paper is improved compared to the previous one, but I still have some concerns.

The basic idea here is that learning should depend on the level of uncertainty. The assumption is that the level of uncertainty is represented by the network of MSN neurons. If they are sparsely activated this implied high certainty and if they are activated in a distributed manner this means uncertainty. A key phase is "treated as uncertainty". The equations for entropy are not for true entropy, and the stochasticity to the extent it exists plays little role here, they are simply quantifications of a sparse or distributed response.

One improvement here is that rather than modulating the TAN pause completely via an external and biophysically implausible mechanism the detection of the "uncertainty" is now more biophysical, however if I understood correctly the control of the TAN pause duration is still external and non-biophysical.

This is a very complex model, yet it is not biophysically plausible. I have the feelings that the general concepts could be embedded in a much simpler model that would not obscure the main points in a mountain of details, on the other hand if it were truly biophysical it could be more directly compared to experimental results. Therefore, this is neither a clear lucid theory, nor a reasonable computational model.
