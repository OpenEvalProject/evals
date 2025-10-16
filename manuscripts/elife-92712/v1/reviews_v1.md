# Peer review - Round 1

Editors:
- Panayiota Poirazi, https://ror.org/01gzszr18 FORTH Institute of Molecular Biology and Biotechnology Greece

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.92712.3.sa0](https://doi.org/10.7554/eLife.92712.3.sa0)

This valuable study investigates how biologically plausible learning mechanisms can support assembly formation that encodes statistics of the environment, by enabling neural sampling that is based on within-assembly connectivity strength. It convincingly shows that assembly formation can emerge from predictive plasticity in excitatory synapses, while two types of plasticity in inhibitory synapses are required: inhibitory homeostatic (predictive) plasticity and inhibitory competitive (anti-predictive) plasticity.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.92712.3.sa1](https://doi.org/10.7554/eLife.92712.3.sa1)

The authors have successfully addressed most of the issues raised in the first review. Nevertheless, some of the mentioned problems require further attention, mostly regarding the formal derivation of the learning rules, as well as connections to previous research.

Regarding the derivations of learning rules: The authors have provided Goal functions for each of the plastic neural connections to give some insight into what these connections do. However, as I understand, this does not address the main concern raised in the previous review: Why do these rules lead to overall network dynamics that sample from the input distribution? Virtually all other work on neural sampling that I am aware of (e.g., from Maass Lab, Lengyel Lab, etc.) start from a single goal function for all connections that somehow quantifies the difference of network dynamics from the target distribution. In the presented work the authors specify different goal functions for the different weights, which does not make clear how the desired network dynamics are ultimately achieved.

This becomes especially evident looking at the two different recurrent connections (M and G). M minimizes the difference between network activity f and recurrent prediction DKL[f|phi(My)], but why is this alone not enough to ensure a good sampling? G minimizes the squared error [f-phi(Gy)]^2, but what does that mean? The problem is that the goal functions are self-consistent in the sense that both f and phi(Gy) depend on G, which makes an interpretation very difficult. Ultimately it's easier to interpret this by looking at the plasticity rule and see that it leads to a balance. For G the authors furthermore actually ignore the derived plasticity rule and switch to a rule similar to the one for M, meaning that the actual goal function for G is also something like DKL[f|phi(Gy)]. Overall, an overarching optimization goal for the entire network is missing, which makes the interpretation very difficult. I understand that this might be very difficult to provide at this stage, but the authors should at least point out this shortcoming as an open question for the proposed framework.

Regarding the relation to previous work the authors have provided a lot more detailed discussion, which very much clears up the contributions and novel ideas in their work. Still, there are some claims that are not consistent with the literature. Especially, in lines 767 ff. the authors state that Kappel et al "assumed plasticity only at recurrent synapses projecting onto the excitatory neurons. In addition, unlike our model, the cell assembly memberships need to be preconfigured in the [...] model." This is not correct, as Kappel et al learn both the feed-forward and recurrent connections, hence the main difference is that in Kappel et al sampling is sequential and not random. This is why I mentioned this work in the first review, as it speaks against the authors claims of novelty (719 ff.), which should be adjusted accordingly.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.92712.3.sa2](https://doi.org/10.7554/eLife.92712.3.sa2)

Summary:

The paper reconsiders the formation of Hebbian-type assemblies, with their spontaneous reactivation representing the statistics of the sensory inputs, in the light of predictive synaptic plasticity. It convincingly shows that not all plasticity rules can be predictive in the narrow sense. While plasticity for the excitatory synapses (the forward projecting and recurrent ones) are predictive, two types of plasticity in the recurrent inhibition is required: a homeostatic and competitive one.

Details:

Besides the excitatory forward and recurrent connections that are learned based on predictive synaptic plasticity, two types of inhibitory plasticity are considered. A first type of inhibition is homeostatic and roughly balances excitation within the cell assemblies. Plasticity in this type 1 inhibition is also predictive, analogous to the plasticity of the excitatory synapses. However, plasticity in type 2 inhibition is competitive and has a switched sign. Both types of inhibitory plasticity, the predictive (homeostatic) and the anti-predictive (competitive) one, work together with the predictive excitatory plasticity to form cell assemblies representing sensory stimuli. Only if the two types of homeostatic and competitive inhibitory plasticity are present, will the spontaneous replay of the assemblies reflect the statistics of the stimulus presentation.

Critical review:

The simulations include Dale's law, making them more biologically realistic. The paper emphasizes predictive plasticity and introduces type 1 inhibitory plasticity that, by construction, tries to fully explain away the excitatory input. In the absence of external inputs, however, due to the symmetry between the excitatory and inhibitory-type-1 plasticity rules, excitation and inhibition tend to fully cancel each other. Multiple options may solve the dilemma:

(1) As other predictive dendritic plasticity models assume, the presynaptic source for recurrent inhibition is typically less informative than the presynaptic source of excitation, so that inhibition is not able to fully explain away excitation.

(2) Beside the inhibitory predictive plasticity that mirrors the analogous excitatory predictive plasticity, and additional competitive plasticity can be introduced.

The paper chooses solution (2) and suggests and additional inhibitory recurrent pathway that is not predictive, but instead anti-predictive with a reversed sign. The combination of the two types of inhibitory plasticities lead to a stable formation of cell assemblies. The stable target activity of the plasticity rules in a memory recall is not anymore 0, as it would be with only type-1-inhibitory plasticity.

Instead, the target activity of plasticity is now enhanced within a winning assembly, and also positive but reduced in the loosing assemblies.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.92712.3.sa3](https://doi.org/10.7554/eLife.92712.3.sa3)

Summary:

The work shows how learned assembly structure and its influence on replay during spontaneous activity can reflect the statistics of stimulus input. In particular, stimuli that are more frequent during training elicit stronger wiring and more frequent activation during replay. Past works (Litwin-Kumar and Doiron, 2014; Zenke et al., 2015) have not addressed this specific question, as classic homeostatic mechanisms forced activity to be similar across all assemblies. Here, the authors use a dynamic gain and threshold mechanism to circumnavigate this issue and link this mechanism to a cellular monitoring of membrane potential history.

Strengths:

(1) This is an interesting advance, and the authors link this to experimental work in sensory learning in environments with non-uniform stimulus probabilities.

(2) The authors consider their mechanism in a variety of models of increasing complexity (simple stimuli, complex stimuli; ignoring Dale's law, incorporating Dale's law).

(3) Links a cellular mechanism of internal gain control (their variable h) to assembly formation and the non-uniformity of spontaneous replay activity. Offers a promise of relating cellular and synaptic plasticity mechanisms under a common goal of assembly formation.

Weaknesses:

(1) However, while the manuscript does show that assembly wiring does follow stimulus likelihood, it is not clear how the assembly specific statistics of h reflect these likelihoods. I find this to be a key issue.

(2) The authors model does take advantage of the sigmoidal transfer function, and after learning an assembly is either fully active or near fully silent (Fig. 2a). This somewhat artificial saturation may be the reason that classic homeostasis is not required, since runaway activity is not as damaging to network activity.

(3) Classic mechanisms of homeostatic regulation (synaptic scaling, inhibitory plasticity) try to ensure that firing rates match a target rate (on average). If the target rate is the same for all neurons then having elevated firing rates for one assembly compared to others during spontaneous activity would be difficult. If these homeostatic mechanisms were incorporated, how would they permit the elevated firing rates for assemblies that represent more likely stimuli?
