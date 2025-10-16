# Peer review - Round 1

Editors:
- Ronald L Calabrese, Emory University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.12572.032](https://doi.org/10.7554/eLife.12572.032)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "A stochastic neuronal model predicts random search behaviors at multiple spatial scales in C. elegans" for consideration by eLife. Your article has been reviewed by favorably evaluated by Eve Marder (Senior Editor) and three reviewers, one of whom, Ronald L. Calabrese, is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors present a kinematic analysis of random local search behavior in C. elegans at high resolution. This analysis leads to a Markov model of underlying neuronal network based on the C. elegans connectome. This inherently stochastic model not only accounts for the data but also predicts the sign and strengths of key connections which are then confirmed by electrophysiology/optogenetics. The model can be adjusted easily to account for other types of random searches by adjusting parameters compatible with sensory input or modulation. Further the model can be expanded to incorporate directed searches as in chemotaxis and can also account for 'deterministic' behavior such as escape movements. The model also accounts for counter intuitive results on dwell times associated with genetic manipulation and laser ablation of key command neurons. These findings conceptually inform experiments in the mammalian sleep network. Altogether this work is an impressive display of the power of modeling when combined with detailed experimental manipulation. The authors make a strong effort to cast their results in the context of other efforts to measure search motion and define pause states. They also explicitly address more neuronal-based determinist models of the network underlying random searches.

Essential revisions:

1) Results, second paragraph: The claim that this study represents "a 10-fold improvement over previously published tracking systems" seems to be a stretch. In some sense, centerline-tracking experiments operate at a much finer resolution than tracking a single dot on a worm, with papers such as Brown, et al., PNAS (2013) tracking many more worms with more detail and higher resolution. I agree that the authors appear to have done a fine job at spot tracking, but we don't believe that they have a claim to novelty here.

2) The authors should address the Stephens et al. (2011) paper in a different manner than they do here (particularly in the Discussion section, fifth paragraph). To begin with, the statement that the "mathematical relationship between tangential velocity and phase velocity (so defined) has not been delineated, but is likely to be complex" largely due to slippage between the worm and the substrate seems an overstatement. If the paper is interested in modeling the animal's neural control of motion, then shouldn't the model be more concerned about the dynamics actually being controlled – in this case, the postural dynamics? And while it is indeed theoretically possible to produce thrust without advancing the phase, the collection of papers from Stephens et al. show that the worms' dynamics lie almost entirely on a manifold of remarkably small dimension, showing that these types of potential postural changes occur only rarely. Moreover, the authors themselves admit (in the subsection “Wild type locomotion”, fifth paragraph) that "on an agar surface, the worm moves without slipping."

In addition, the authors state that the Stephens et al. (2010) paper shows that postural modeling does not accurately model the worm when its center of mass trajectory follows an arc. In fact, the cited paper shows the necessity of looking at arcing trajectories between reorientation events and not just using a run-and-tumble analogy from bacteria, showing that shape-space dynamics form a predictive relationship with foraging trajectories.

All this being said, we are not disputing the authors' modeling choice of only using the midpoint of the worm's body. We have no arguments that there is utility in using a simplified description of a system to gain quantitative insight, but we want to see the authors distinguish themselves from the Stephens (2011) paper differently, focusing instead on the fundamental difference of modeling via a hidden Markov model instead of fitting parameters in a set of deterministic/stochastic differential equations. The choice of measuring Euclidean velocity instead of phase velocity is a modeling choice. Put another way, if someone with comparable amounts of shape-space data were to fit a hidden Markov model of your form to their data using phase velocity instead of velocity, would they likely obtain the same results?

3) In Figure 4, could the result that there is no postural stereotypy entering into state X be the result of an over-zealous "pause" caller. Specifically, this model calls many more things pauses than other approaches because of the nature of the sub-frame-resolution hidden Markov fit. What do these plots look like if only the longest visits to the X states are included?

4) Is there any evidence that the time scales of neural activity in C. elegans' motor neurons can be as short as the pause states being predicted? Although the model is supposed to be an abstraction of what's occurring in the worm's nervous system, one should expect to predict reasonable numbers for this nonetheless.

5) In the first paragraph of the subsection “Wild type locomotion” the authors claim that their "tracking system is capable of revealing briefer visits" to the pause state and that this is the reason why their measured dwell time is much shorter than previously measured. Again, we are not yet convinced that this method is much more accurate than the posture tracking used in Stephens et al. (2011) to measure the forward dwell time. The Stephens paper, however, uses a slightly different definition of the dwell time, using cessation of the forward phase velocity instead. Although the paper here does not measure phase velocity, they could measure the dwell time between visits to the reversal state (i.e. ignoring F->P->F type transitions). What happens if this definition is used? Does the same result emerge?

6) A more general comment is that we would like to understand more what type of neural activity the authors would predict based on their model, connectome data, and polarity results from papers such as Rakowski (2013) despite imaging in a freely-behaving worm being well outside of the scope of this paper (although not nearly as impossible as the authors seem to suggest in the Discussion section). If this experiment were performed, what is the most likely neural instantiation of this model that is consistent with the current literature? The strength of this model is that it makes an attempt at getting at how this circuit may actually function. Accordingly, if possible, a concrete prediction or predictions to this end would greatly increase the value of this paper to researchers and could guide experimentalists performing imaging in freely-behaving animals in their measurements and analysis.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The previous decision letter after peer review is shown below.]

Thank you for choosing to send your work entitled "A stochastic neuronal flip-flop circuit regulates random search during foraging behavior" for consideration at eLife. Your full submission has been evaluated by Eve Marder (Senior editor) and three peer reviewers, one of whom, Ronald L. Calabrese, is a member of our Board of Reviewing Editors, and the decision was reached after discussions between the reviewers. Based on our discussions and the individual reviews below, we regret to inform you that your submission in its present form is not suitable for publication in eLife. That said, if you feel that you can adequately rebut, answer the reviews with a combination of rewriting or new work, we would be willing to consider a new submission of this material, as it clearly asks an important and interesting set of questions.

Consensus review:

The authors present a kinematic analysis of random local search behavior in C. elegans. The then use a Hidden Markov Model to quantitatively model such searches based their kinematic analyses. They then identify this HMM with known aspects of the worm connectome to understand the neural implementation of switches between different behavioral states. In particular, the model contains two populations of neurons, each controlling either forward or reverse locomotion, with the overall network resulting in four possible behaviors: forward, reverse, and two pause states. They perform a maximum likelihood fit of the model to measured time series, making predictions about the effect of neural ablations, the sign and strength of synaptic connections, effects of perturbations to membrane potentials. Moreover, they phenomenologically model a potential underlying neural mechanism for different search modalities.

The subject matter of the paper is definitely one of broad interest, and if the model is correct it would provide us with a substantive understanding into the neural implementation of the forward/pause/reversal/pause(?) dynamics it would be a major contribution. However, the reviewers are not fully convinced that the model is the simplest possible explanation of the animal's behavior and that the authors have shown that a clear connection can be drawn to neural correlates.

Enthusiasm for the subject matter and the potential neural correlates vs. concerns about the appropriateness of the approach and its rigor were weighed differently by the reviewers initially, but in consultation the concerns predominated. The detailed reviews of the expert reviewers are appended but their concerns are summarized below.

1) The model is not adequately placed within the context of previous work in the field. There have been other papers attempting to understand both exploitation/exploration behavioral generation (e.g. Flavell et al., Cell, 2013) and forward/reversing dynamics (e.g. Stephens, PNAS, 2011).

Moreover, a direct comparison to (Rakowski et al., 2013) is needed. This work, which is cited as Ref. 12, also develops a model of the command neuron network and uses this model to predict behavioral states and the effects of ablations.

2) The existence of two different pause states X and Y is not well supported in the data and the HMM does not have the power to confirm their existence.

3) The mapping of the HMM onto the underlying neuronal network is not convincing. In particular there little data in this paper or in any of the citations to support the contention that pause state X = all command neurons off and pause state Y = all command neurons on. Mapping synaptic weights onto coupling in the HMM is not rigorous.

For the paper to be suitable for eLife the following extensive changes would have to be made.

1) Relax the claims about the model's prediction of synaptic weights.

2) The authors need to establish firmly that tracking a single point provides an unbiased estimate of trajectory in light of Stephens, PLoS One (2010). Given their extensive data set, we presume that converting their point imaging into centerline tracking would be extremely difficult and time consuming, but the authors should at least place their analysis in this light. They should also bolster their arguments that there are two behaviorally distinct pause states and discuss how they are related to the two pause states of Stephens.

3) The authors should differentiate their work with respect to Rakowski (2013). Does their model provide different predictions? Can they be disambiguated? It would be great if they could show this, but minimally, they should suggest what experiments should be performed in the future.

4) Similarly – what measurements should be made to distinguish X and Y pause states map onto the electrical activity of the command neuron network at least at some coarse-grained level?

Reviewer #1:

The authors present a kinematic analysis of random local search behavior in C. elegans at high resolution. This analysis leads to a Markov model of underlying neuronal network based on the C. elegans connectome. This inherently stochastic model not only accounts for the data but also predicts the sign and strengths of key connections which are then confirmed by electrophysiology/optogenetics. The model can be adjusted easily to account for other types of random searches by adjusting parameters compatible with sensory input or modulation. Further the model can be expanded to incorporate directed searches as in chemotaxis and can also account for 'deterministic' behavior such as escape movements. The model also accounts for counter intuitive results on dwell times associated with genetic manipulation and laser ablation of key command neurons. These findings conceptually inform experiments in the mammalian sleep network.

Altogether this work is an impressive display of the power of modeling when combined with detailed experimental manipulation. Moreover the approach complements and expands other efforts using unbiased approaches that make no assumptions about whether and how behavioral categories can be mapped to specific states of the nervous system. This approach allows mapping of states on to the neuronal network. The paper is very clearly and crisply written. The figures are clear and contain useful data well organized. All essential data is presented.

This reviewer is not an expert in Markov models and the associated mathematics, so I would defer to the experts on any potential flaws in this analysis, but the behavioral analyses are very straightforward and carefully done, the electrophysiology is state of the art for C. elegans, and the mutant analysis and cell ablation experiments seem carefully controlled. The statistical analysis seems appropriate but I defer to the other more expert reviewers. Methods are a model of completeness. There are no major concerns noted by this reviewer. I really enjoyed reading this paper and I learned a lot.

Reviewer #2:

Roberts et al. present a study combining behavioral measurements of C. elegans locomotion, modeling of a two-state stochastic system, and measurements of functional connectivity between two command interneurons. The authors claim that using the stochastic model, they can make nontrivial predictions about the state of the underlying neural network, solely based on behavioral measurements. They also claim that using behavioral data and their two-state model they can predict the strengths of synaptic connections between interneurons. If these claims were valid, this would be a significant achievement and worthy of publication in eLife, although the novelty of this work is somewhat compromised by another recent publication (Rakowski et al., 2013).

My major concerns are:

1) The claim that there are two distinct pause states resulting from different levels of activity in the command interneurons is not supported by evidence presented in this paper or cited work.

2) The stochastic switch model is not grounded enough in the biology of the system to justify comparing model fit parameters to measurements made on individual neurons. In particular the comparison of the model fit parameters labeled "synaptic weights" to actual synaptic connections is inappropriate.

Behavioral Measurements and Hidden Markov Model:

In Figure 1, the authors present data obtained by tracking a fiducial marker painted onto the back of a freely moving worm. They show a distribution of "velocities" (1D) that appear to be the sum of 3 distributions, which they label "reverse, pause," and "forward." In Figure 1E, they then show a velocity vs. time graph that has been segmented into these states by thresholding the velocity at +/- 0.05 mm/s. In Figure 2E, they show a similar velocity vs. time graph that has been similarly segmented using a Hidden Markov Model. The claim is that this model does a much better job of describing the behavioral state than the process used in Figure 1E, although I cannot find any quantitative measures in the paper to support this assertion (more on this later).

The HMM differs from simple thresholding by (1) assigning different prior probabilities to transitions between states and staying in the same state and (2) including 2 pause states (called X and Y). The states of the HMM are related to behavior and to the stochastic flip flop model as follows.

F: worm is moving forward. "F" unit is active and "R" unit is inactive. What F and R represent is unclear in the paper? They are described as "binary stochastic elements," (subsection “The Stochastic Switch Model”, third paragraph), "single binary neuron-like units" (Figure 2 caption), and as a collection of neurons as in "self connections represent synaptic connections between neurons comprising a given unit." (Figure 2 caption). I will come back to this under Stochastic Switch Model, but for discussion of the hidden Markov model, the distinctions are not important.

R: worm is moving backward. "R" unit is active and "F" unit is inactive.

X: worm is not moving/moving slowly. Both units are inactive.

Y: worm is not moving/moving slowly. Both units are active.

A great deal of the argument in this paper relies on the existence of two pause states and of the identification of these two behaviorally identical pause states with specific patterns of activity in command interneurons, so I will go over in some detail the arguments the manuscript advances:

1) Using a speed threshold, pauses during forward->reverse transitions were found to be longer than pauses during reverse->forward transitions.

2) "When both F and R are OFF (state X) it is assumed that movement ceases, consistent with studies showing that genetic ablation or silencing of all command interneurons induces prolonged pauses (Kawano et al., 2011; Zheng et al., 1999)." Zheng et. al (Zheng et al., 1999) report that glr-1::ICE (klys36) "moved significantly slower than wild type worms and also had long pauses during which no movement occurred." Kawano et al. (Kawano et al., 2011) report that silencing all of AVA, AVB, AVE, AVD, and PVC led to prolonged pausing with the body in a straight position and that using a combination of genetic and laser ablation to destroy these same methods resulted in worms that were "kinked" with odd body postures.

3) "In the event that F and R are simultaneously ON (state Y), the resulting motor commands are assumed to conflict at the level of the motor neurons of the body wall muscles, resulting in a second motionless state, as has been observed (Kawano et al., 2011)." The way this sentence is structured may leave a mistaken impression of what is reported in Kawano et al., 2011. Kawano et al., 2011 does not show that when F&R command interneurons are simultaneously active, worms stop moving. Instead it shows that in innexin mutants (unc-7 and unc-9), the "kink" state is correlated with the A and B type motorneurons having similar levels of calcium.

4) In the second paragraph of the subsection “Wild type locomotion“. Removing state Y (i.e., setting aFY=aRY=0) caused a large and highly significant reduction in the summed log-likelihood of the 5 wild type cohorts (𝑝 < 10-100) demonstrating that the second pause state greatly improves the fit.

Taken individually or together, these arguments fail to support the existence of multiple pause states or that these states can be reached by co-activation or inactivation of command neurons.

Argument 1 merely shows that the speed of a dot on a worm's midline recovers more quickly in the reverse to forward transition than the forward to reverse. This could be due to measurement artifacts, biomechanical differences, differences in the response latencies of A and B motorneurons, or differences elsewhere in the neural network.

Argument 2 shows that permanent inactivation of all command motor neurons leads to a worm with severe motion defects. It's quite a stretch to go from there to saying that transient decreases in the activities of these neurons will lead to immediate cessation of movement. It does seem at least plausible that if both forward and reverse command neurons are "off," the worm stops moving, although I question whether this cessation would really be immediate, especially since forward motion results from the propagation of a wave down the body due to proprioreceptive feedback (Wen et al., 2012)

Argument 3 does not show that co-activation of command neurons leads to pausing in wild type animals.

Argument 4 suffers from several flaws. First, the hidden Markov model used with the sole observable being the speed of a dot on the worm's midline may not be an appropriate description of the system (discussed in other comments). Second, the fact that one model produces a better fit than another does not show that either model is true. IE: that adding a state to the HMM improves the model's fit does not prove that state exists.

There are other ways we might improve the model fit that are incompatible with the stochastic switch model: Allowing the HMM to have 8 degrees of freedom rather than 6; adding a third pause state or a second forward state with a different velocity distribution; allowing direct transitions between X and Y or F and R. If any of these produce a significant improvement in the likelihood of the data given the model, what would that imply for the stochastic switch model? I would also like to see the likelihood ratio test applied to compare a model where the state is determined by simple thresholding (as in Figure 1E) to the 4-state HMM.

In summary, the authors present only weak evidence that there even are two distinct pause states. There is no data presented here or in the cited literature that show that simultaneous activation or deactivation of forward and reverse command neurons causes pausing. There is no evidence given for the correspondence of the two pause states in the HMM with two distinct states of the command neuron network. Finally, beyond a very thin justification about metabolic efficiency, there is nothing to support the assignment of state X to the R->F transition and state Y to the F->R.

I think the idea that the same behavioral state (pausing) can be the result of opposite patterns of activity in the command neurons is intriguing and worth pursuing.

The authors write that "The currently available set of optical probes of neuronal activity do not have sufficient temporal resolution to allow direct observation of the underlying states of the command network in intact, freely moving animals." The recovery time of GCaMP3 is ~300 ms and faster dynamics can be inferred by deconvolving the observed signal with the known GCaMP3 filter (Kato et al., 2014). And faster indicators, like GCaMP6f, are now available. The mean duration of inferred state X pauses is 480 ms and 20% of inferred state Y pauses are over 300 ms (Figure 2—figure supplement 3). The authors assert that in state X the activity in all command neurons will be much lower than in state Y. Surely in these longer pauses it would be possible to make a measurement that verifies this prediction.

A second approach would be to use optogenetic tools to determine the pause state. In state X (all command neurons off), ChR2 activation of AVB should induce forward locomotion by hyperpolarization of AVA via NpHR/halo should not. In state Y (all command neurons on), hyperpolarization of AVA should lead to forward locomotion.

The "Stochastic Switch Model":

The stochastic switch model uses a nonstandard description of neural state. Instead of parameterizing the state of a neuron by a continuous variable, e.g. membrane potential, the neuron is treated as a binary element, existing in one of two discrete states. Synaptic connections are also represented/modeled in a non-standard way. Normally, if A is presynaptic to B, activity in A causes a change in the membrane potential of B by an amount set by the weight of the synaptic connection from A to B. In this model, if A is active, the probability that B will spontaneously switch states is modified by an amount that depends exponentially on the "weight" of the connection. As a model of coupled two state systems, there is nothing inherently wrong with this approach, but comparing the resulting model fit parameters to biological parameters is confusing and potentially misleading.

Figure 5, "the stochastic switch model correctly predicts the sign and strength of synaptic connections" shows the confusion generated by the choice of terminology. Figure 5A shows model fit parameters that have no obvious biological interpretation, but the figure caption identifies these fit parameters as "synaptic weights." Then Figure 5B and C show "synaptic currents" (currents that result from functional, but not necessarily direct synaptic, connections) measured by recording the amount of current received by neuron B when neuron A is activated. The figure invites the reader to compare 5A to the 5B-5E even though 5A shows fit parameters from a model that does not even have synaptic currents. This presentation is at best confusing and at worst misleading.

In their description of the stochastic switch model, the authors should only use the term "binary stochastic elements" to describe F and R, and choose a term other than "synaptic weights" to describe the model fit parameters (hF, wff etc.), which are not synaptic weights as the term is commonly used. The chosen terminology will lead all but the most careful readers to misunderstand the work that has been done.

Measurements of functional connectivity, effect of ablations, and extensions to chemotaxis:

The measurements of functional connectivity appear to be well done; I have no major concerns with these, beyond that already noted in the text: different levels of ChR2 expression in AVA and AVB could complicate the interpretation of these results. Perhaps the current evoked by ChR2 activation could be directly measured and calibrated. In most of the literature about the C. elegans motor circuit, there is assumed to be reciprocal inhibition between AVA and AVB, but I think Figure 5 shows the first direct measurement, a significant contribution.

The rest of the paper (Figures 4, 6–8) relies on the results of the modeling and behavioral experiments.

Reviewer #3:

The submission by Roberts, et al., uses a Hidden Markov Model to quantitatively model the locomotory behavior of C. elegans, with a particular emphasis on understanding the neural implementation of switches between different behavioral states. In particular, the model contains two populations of neurons, each controlling either forward or reverse locomotion, with the overall network resulting in four possible behaviors: forward, reverse, and two pause states. They perform a maximum likelihood fit of the model to measured time series, making predictions about the effect of neural ablations, the sign and strength of synaptic connections, effects of perturbations to membrane potentials. Moreover, the phenomenologically model a potential underlying neural mechanism for different search modalities.

In general, I found the work to be careful done, and understanding the mechanisms of behavioral control is an important question in the field. My major concerns have to do with the novelty of the work.

As far as novelty is concerned, there have been other papers attempting to understand both exploitation/exploration behavioral generation (e.g. Flavell, et al., Cell, 2013) and forward/reversing dynamics (e.g. Stephens, PNAS, 2011), with both of the cited examples leading to the generation of long behavioral time scales. It would be useful for the authors to place their results in the context of these papers. In particular, the Stephens (2011) paper uses an analogous (but non-identical approach) of fitting a dynamical system to the data and makes (highly accurate) predictions about forward/reversal switching rates using Arrhenius-like stochastic dynamics. In addition, an earlier paper from the same group (Stephens, PLoS Comp Bio, 2008) shows that a 4-state system emerges naturally from a data set. Here, this set-up is assumed a priori.

Specific comments:

1) In Figure 4B, I find the excuse for omitting error bars to be relatively weak. Minimally, bootstrapped confidence intervals could be found, which would be significantly better than the current lack of any measure of variability.

2) In the fifth paragraph of the subsection “Genetic effects on command neuron function” and Figure 6. The claim is made that "changes in synaptic strength dominate the effects of changes in membrane potential on ΔF and ΔR." This certainly seems true for ΔF, but both models appear to give more-or-less identical predictions here for ΔR.

3) In the first paragraph of the subsection “The Stochastic Switch Model and other random search behaviors“. It is claimed that "changes are required in at least three weights to produce the full range of search behaviors." This is not actually shown anywhere in the paper, just that three weights are sufficient to induce the full range. A supplementary figure to this effect would be useful.

4) The predicted value for the dwell time in the forward state is not comparable to the rest of the literature, as a different definition is used here. What would happen if a standard definition was used? Does the same rate result?
