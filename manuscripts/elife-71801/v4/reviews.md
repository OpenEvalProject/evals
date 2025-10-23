# Peer review - Round 1

Editors:
- Srdjan Ostojic, Ecole Normale Superieure Paris France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71801.sa0](https://doi.org/10.7554/eLife.71801.sa0)

There has been a longstanding interest in developing normative models of how humans handle latent information in stochastic and volatile environments. This study examines recurrent neural network models trained on sequence-prediction tasks analogous to those used in human cognitive studies. The results demonstrate that such models lead to highly accurate predictions for challenging sequences in which the statistics are non-stationary and change at random times. These novel and remarkable results open up new avenues for cognitive modelling.


---

# Peer review - Round 1

Editors:
- Srdjan Ostojic, Ecole Normale Superieure Paris France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71801.sa1](https://doi.org/10.7554/eLife.71801.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Gated recurrence enables simple and accurate sequence prediction in stochastic, changing, and structured environments" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Srdjan Ostojic as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Michael Frank as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Mehrdad Jazayeri (Reviewer #2).

The three reviewers are enthusiastic about the manuscript, but have found that the main claims need to be contextualised or rephrased to avoid giving an overstated impression. In the absence of any direct comparison with human behavior and/or neural activity, and considering the high degree of abstraction in model (11 units with abstract computational building blocks), the paper needs a major revision in Discussion to highlight the gap between the results and neurobiology/behavior.

The Reviewing Editor has drafted a consolidated review to help you prepare a revised submission.

Essential revisions:

1. The most notable weakness of the paper is that is not clear whether its aim is to develop a neural model that is close to optimal or a neural model that explains how biological brains handle stochasticity and volatility. There is no serious and quantitative comparison to behavior or neural data recorded in humans or animal models. All the comparisons are with other algorithms and reduced GRU networks. One can appreciate these comparisons if the goal is to show that a full GRU network is close to optimal (which, in many cases, it is). But do humans exhibit a similar level of optimality? One possibility would have been to provide some sort of analysis that would show that the types of errors the model makes are in some counterintuitive (or even intuitive) way like the types of errors humans make. In some of the papers where certain heuristics were proposed, the entire goal was to explain characteristic sub-optimalities in human behavior. As an example, see the recent paper from the Koechlin group in Nature Human Behavior. More generally, there is no shortage of papers quantifying human behavior in stochastic volatile environments. It would be great to see that the errors humans make in at least some task map onto the errors GRU networks make. Imagine for example that such a comparison would show that human errors are more similar to a lesioned version of the GRU, even though the full GRU is closer to optimal. The natural conclusion for such an observation would be that some of the proposed mechanisms are in fact not at play. In any case, all the reviewers think the comparison to human behavior would be valuable, and should be at minimum extensively discussed.

2. On the importance of gating: a lot of emphasis is put on the necessity of gating (eg title, abstract, discussion line 478). But the methods used in the paper cannot demonstrate necessity. Indeed other studies (see eg Collins, Sohl-Dickenstein and Sussillo, arxiv 2016) have argued that gating in RNNs improves their trainability, but does not increase their capacity. That study argued that large vanilla RNNs are able to reach the same performance as gated RNNs with more extensive training and/or hyper-parameter tuning. The claims and discussion should be revised to reflect this limitation.

3. The biological relevance of gating seems also somewhat over-stated (eg in the abstract): while there is no doubt various forms of gating are present in the nervous system, how they map to the specific time-dependent form used in GRUs is far from clear. The relationship of these gate variables with actual synapses, neurons, or populations of neurons is at best speculative at this point.

4. In terms of comparing to biology, the discussion states that "mapping between artificial units and biological neurons may not be straightforward." But biological and artificial models can still be compared quite effectively in terms of activity in the state space, and these comparisons can help reject hypotheses quite effectively. Training RNNs have been a productive avenue for understanding neural computations in the past years, in many studies of this class networks are constrained or contrasted by experimental data (Mante and Sussillo et al., 2013, Rajan et al., 2016 or Finkelstein and Fontolan et al., 2021 as some examples). It could have been possible to try to understand the geometry of neural representations of latent variables in network dynamics and how it is learned and depends on the environment. Additionally, by performing dynamical system analysis (see eg Susillo and Barak, 2013 or Dubreuil and Valente et al., bioRxiv as examples) it might be possible to understand the role of gating in the network computations.

5. The focus on very small network does not necessarily seem relevant when comparing with biologic networks (the phrase "reasonably sized networks" on l.479 seems inappropriate). The analysis of network size in Figure 7 goes until 45 units, which remains very small, and it's difficult to extrapolate the results to larger networks. For instance, large vanilla RNNs implement an effective form of gating based on their non=linearity (Dubreuil et al. 2020), and this mechanism may be able to drastically increase sequence-prediction performance.

6. Another weakness of the paper is that, for each new task, it trains a new GRU. Humans seem to be able to adapt to changes in the latent structure of the generative process without massive retraining. How does this flexibility map onto the proposed scheme? In one of the supplements, cross-task performances have been shown. One notable result is that a GRU trained on a changing bigram with or without coupled change points does quite poorly on the changing unigram. This is an example of failed generalization from a much more complex latent structure to a simpler one, which is indicative of overfitting (to the structure of a generative model – not its parameters). Somewhat counterintuitively, for the GRU model (as well as various other models), the smallest hit on generalization performance occurs when the models are trained on the changing unigram, which is the simplest latent structure considered. This is consistent with several psychophysical studies suggesting that humans may not rely on accurate latent models and may instead rely on simpler heuristics. In the end, is it justified to train new GRUs for each task?

7. Note that LSTMs are able to perform similar computations like the ones in this study here as is shown in Wang and Kurt-Nelson et al., 2019.

8. As a more technical point, the comparison with networks without gating does not seem fully fair. Freezing gating effectively reduces the number of time-dependent variables by a factor 3. Also, when freezing gating, one could treat the gating parameters as fixed hyper-parameters to be optimized, rather than setting them by hand to one.
