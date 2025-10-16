# Peer review - Round 1

Editors:
- Jan-Marino Ramirez, Seattle Children's Research Institute United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.50927.sa1](https://doi.org/10.7554/eLife.50927.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The computational model proposed by the authors is interesting, scientifically but also clinically since it simulates the mechanisms underlying seizures typically seen in focal cortical dysplasia. We are excited by this paper because the model has the ability to mimic the tonic-clonic transitions and the spatial expansion associated with EEG synchronization typical for these seizures. The authors also provide computational support for their overarching hypothesis that the seizure termination is caused by exhaustion of inhibition.

Decision letter after peer review:

Thank you for submitting your article "A theoretical model for focal seizure initiation, propagation, termination, and progression" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Jan-Marino Ramirez as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Ronald Calabrese as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Kevin Staley (Reviewer #2); A. N. Khambhati (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this work, Liou et al. develop and study a biophysical network model that recapitulates a repertoire of seizure dynamics observed during microelectrode recordings from human epileptic cortex. The authors identify biophysically plausible failure points of the otherwise healthy neocortical circuit model by pushing the model system to seizure threshold, via excitatory input, and parametrically varying synaptic conductance dynamics, spike-timing dependent plasticity, and background noise. Liou et al. demonstrate that inhibition and adaptation play critical roles in the spatiotemporal progression of seizures, from onset to termination; and that a naïve network model undergoing a breakthrough seizure can be subject to plasticity rules that increase the probability of subsequent, spontaneous seizures. This study is substantially strengthened by the link between model parameters and naturally occurring seizure dynamics. The idea of using the model as a test-bench to identify putative dysfunctional elements of a patient's seizure network is highly compelling. Strengths: the model generates realistic ictal activity, particularly progression and tonic-clonic transition, that closely conforms to human ictal EEG recordings. The model is less abstract than Epileptor.

Essential revisions:

1) The model does not generate spontaneous seizures, as suggested by the title phrase "model for focal seizure initiation". The model does not intrinsically terminate seizures; termination is not very clearly addressed but appears to involve a global "γ" inhibitory factor that is imposed on the network. Thus the use of "termination" in the title is also not advisable. The model excels at reproducing seizure propagation, the ictal wavefront proposed by the authors, and transitional EEG phenomena observed during seizures such as tonic-clonic transitions. The paper should be written from the title onward to clarify the strengths and limitations of the model, as suggested in the following recommendations:

2) With regards to Seizure initiation: The model is designed to reproduce the spatiotemporal elements of ictal EEG, and is based on the mechanistic hypotheses of the Abbott laboratory. The model does an excellent job of reproducing the ictal EEG and the ictal wavefront, which strengthens the evidence for the underlying mechanistic ictal hypotheses. Seizure propagation is the strength of this model.

a) Without any epochs of normal activity it is difficult to appreciate how well this model reflects the structure and function of human neural networks that do many things and seize only rarely. For example, the activity driven by the white noise inputs is not shown or compared to ictal activity. Does a white noise input applied at one node propagate through the network? If so, what is the nature of that propagating activity?

b) Figure 2—figure supplement 2 characterizes the exogenous input that triggers seizure activity. Without normal activity for comparison, it is difficult to appreciate from Figure 2—figure supplement 2 the nature of this ictogenic input. How does it compare in amplitude / duration to the white noise? If the ictogenic input needs to be sufficient to overcome inhibition, as appears to be the case from Figure 2—figure supplement 2, this would not be normal input, but rather input from an external epileptic focus. In that case, the model is one of seizure propagation, not seizure initiation.

c) Discussion paragraph four suggests seizures are shut off by an exogenous process that does not have a clear neurophysiological correlate (see point 2).

d) If 1a-c are accurate, the model does not generate spontaneous seizures – they are exogenously triggered and terminated. The model should be represented as a propagation model – how seizures spread through normal cortex. The title, Abstract and Discussion should reflect this strength, vs. the interictal-ictal transitions that rely on exogenously applied mechanisms.

3) With regards to Seizure spread: the model does not clarify the relationships of the 3 modulators of inhibition that are employed in this model: ionic gradients (Equation 3), the z factor (Equation 8) and the Î³ factor. Ionic factors are described in detail e.g. pp 10. The z factor is described in much less detail. The Î³ factor is also not described in detail but is suggested to be a global factor that inhibits the entire network equally (Figure 1A and Discussion paragraph four) and is responsible for seizure termination. Termination of seizure activity by a globally imposed external factor is a significant limitation of the model, at least in terms of how the model is currently represented e.g. in the current title. It would be important to meaningfully link a global termination factor such as Î³ to realistic candidate termination processes (e.g. Krishnan and Bazhenov J Neruosci 2011), that can be instantiated in a physiologically feasible manner.

a) The relationships between ionic determinants of inhibition (Equation 3 in the model) and the global inhibition efficacy factor z (Equation 8) and the Î³ factor are not clear.

b) It is not clear how these 3 inhibitory factors contribute to some of the transition phenomena such as those highlighted by the various white symbols in Figure 2A and Figure 2—figure supplement 4.

c) It would be very useful to show more than 1 seizure in the manner of Figure 2A, with the initiating conductance, average GABA conductance, Î³ conductance, and the z inhibitory conductance modulator plotted on the same time scale and amplitude scales.

4) The "Mexican hat" wiring of the neocortex requires more justification than the current references to other modeling studies. Interneurons are so called because they project locally; however in this model the interneurons have the longer range projections and the principal cells have the shorter connections. Rationalizing this connectivity from ictal surround inhibition is a circular argument – the network should start with the most accurate connectivity data available.

Please consider also the following comments:

5) The authors might add a more elaborate discussion about the clinical applications of a model with a more generalized description of biophysical mechanisms. How might the model help predict the therapeutic yield of different forms of therapy for a patient? Or test new therapies?

6) How might the authors reconcile the model's behavior of a gradual seizure termination process, one in which discharges progressively slow and the network becomes desynchronized, with the common observation on clinical iEEG montages of sudden stopping of ictal activity and subsequent suppression/quieting of activity? Please address this question in the Discussion.

7) A major assumption of this study is that any neuronal network, even one that resembles a healthy network, is capable of producing a seizure if provoked with an external input that is of sufficient strength and duration. Perhaps the authors might want to add a discussion on what the initial "external excitatory input" might represent in the context of a real-world breakthrough seizure? Is it possible that certain types of connectivity profiles and topographical distributions of conductances can make a breakthrough, and/or subsequent spontaneous seizure more likely (before any particular re-modelling has occurred)?

8) The authors show that pre-seizure discharges can travel toward the ictal core via centripetal connections formed after STDP remodeling. This raises several interesting thoughts about the putative role of discharges in seizure generation and maintenance, however the phenomenon is not further discussed in the manuscript. Could the authors discuss the functional significance of discharge travelling waves that converge onto the ictal core, rather than in the opposite direction?

9) What, if anything, might the model suggest about mechanisms underlying shorter sub-clinical events and burst-like epileptiform events that are not necessarily considered seizures? Do these events represent edge-cases of the proposed model? The authors may add these considerations into the Discussion.

10) The specificity of the mechanism associated with spiral wave termination is not clear. Did the wave terminate due to a non-specific "global" input or because the globally synchronizing pulse hit one or more of the correct targets to terminate the seizure? Could duration or direction of the pulse relative to the velocity of the wave impact the likelihood that the wave will terminate?

11) It seems that the seizure types studied here only occur in a small sample of the patients (2 patients included / 5 patients excluded). The authors should comment on the specificity of their results on patients with certain forms of epilepsy / types of seizures unique to those included/excluded.
