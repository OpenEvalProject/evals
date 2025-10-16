# Theoretical principles explain the structure of the insect head direction circuit

## Authors

- Pau Vilimelis Aceituno<sup>1</sup> ([ORCID: 0000-0002-1218-4009](https://orcid.org/0000-0002-1218-4009)) †
- Dominic Dall'Osto<sup>1</sup> ([ORCID: 0000-0002-9549-4490](https://orcid.org/0000-0002-9549-4490))
- Ioannis Pisokas<sup>2</sup> ([ORCID: 0000-0001-7426-3207](https://orcid.org/0000-0001-7426-3207)) †

### Affiliations

1. Institute of Neuroinformatics, University of Zürich and ETH Zürich Zurich Switzerland
2. https://ror.org/01nrxwf90 School of Informatics, University of Edinburgh Edinburgh United Kingdom

† Corresponding author

## Abstract

To navigate their environment, insects need to keep track of their orientation. Previous work has shown that insects encode their head direction as a sinusoidal activity pattern around a ring of neurons arranged in an eight-column structure. However, it is unclear whether this sinusoidal encoding of head direction is just an evolutionary coincidence or if it offers a particular functional advantage. To address this question, we establish the basic mathematical requirements for direction encoding and show that it can be performed by many circuits, all with different activity patterns. Among these activity patterns, we prove that the sinusoidal one is the most noise-resilient, but only when coupled with a sinusoidal connectivity pattern between the encoding neurons. We compare this predicted optimal connectivity pattern with anatomical data from the head direction circuits of the locust and the fruit fly, finding that our theory agrees with experimental evidence. Furthermore, we demonstrate that our predicted circuit can emerge using Hebbian plasticity, implying that the neural connectivity does not need to be explicitly encoded in the genetic program of the insect but rather can emerge during development. Finally, we illustrate that in our theory, the consistent presence of the eight-column organisation of head direction circuits across multiple insect species is not a chance artefact but instead can be explained by basic evolutionary principles.

## Introduction

Insects exhibit an impressive ability to navigate the world, travelling long distances to migrate, find food or reach places of interest before returning to their nests (Müller and Wehner, 1988; Menzel et al., 1996; Heinze et al., 2013; Collett, 2019), a feat that requires them to keep track of their orientation across long journeys (Mappes and Homberg, 2004; Merlin et al., 2012; Warren et al., 2019; Collett, 2019; Beetz et al., 2022). This orientation tracking is achieved by the use of visual cues as well as integrating angular velocity signals over time to maintain a heading estimate relative to a starting angle (Seelig and Jayaraman, 2015; Taube, 2007), known as heading integration.

Electrophysiological and calcium imaging studies have shown that the neural population encoding the head direction in insects has a sinusoid-shaped activation pattern (Labhart, 1988; Labhart, 2000; Loesel and Homberg, 2001; Pfeiffer et al., 2005; Pfeiffer and Homberg, 2007; Kinoshita et al., 2007; Heinze et al., 2009; Homberg et al., 2011; El Jundi et al., 2014; El Jundi et al., 2019). Furthermore, downstream neural populations also encode velocity signals as sinusoidal activations (Lyu et al., 2022).

Theoretical work has speculated that this recurring motif of sinusoidal activity patterns might be so prevalent because it enables easy elementwise vector addition, where vectors encoded as sinusoidal activity waveforms can be added together to give a sinusoidal waveform encoding the sum of the vectors (Touretzky et al., 1993; Wittmann and Schwegler, 1995; Vickerstaff and Di Paolo, 2005). This allows the encoded heading to be easily used by downstream circuitry to track the insect’s position (Mittelstaedt, 1985; Wittmann and Schwegler, 1995; Vickerstaff and Di Paolo, 2005; Haferlach et al., 2007; Wessnitzer et al., 2008; Sakura et al., 2008; Stone et al., 2017). Further studies have shown that models closely aligned with biological data can indeed implement heading integration using sinusoidal activity patterns (Pisokas et al., 2020; Turner-Evans et al., 2020), and that such circuits can be learned (Vafidis et al., 2022).

Here, we show that enabling easy vector addition cannot be the unique driving factor for the presence of sinusoidal heading encodings, as many other circuits with different activity patterns can perform vector addition in the same way. This finding led us to question whether the sinusoidal activation patterns seen in insect navigation circuits are a coincidence, or if they might offer a particular functional advantage that was selected for during evolution.

To address this question, we consider the basic principles necessary for a circuit encoding direction. Of all the circuits fulfilling these requirements, the sinusoidal activity pattern offers the best resilience to noise for the encoded information. However, obtaining this activity requires a circuit with a specific connectivity pattern between neurons. Thus, our theory predicts that the heading integration circuit will have a sinusoidal connectivity pattern. We compare our predicted circuit with connectivity data for the desert locust (Schistocerca gregaria) and fruit fly (Drosophila melanogaster) using network analysis tools, showing a strong agreement. We then ask how an insect brain might develop such a circuit, finding that a simple Hebbian learning rule is sufficient. Finally, we combine ideas from replication dynamics with our theory, which leads us to the conclusion that the eight-column structure is a consequence of basic theoretical principles, rather than an evolutionary coincidence.

## Results

## A theoretical circuit for heading integration

We consider a population of N ‘compass neurons’ with an activity that encodes the direction of the insect as an angular variable θ. We represent the activity of this population by a vector where each element corresponds to the activity of one neuron, a(θ)=[a1(θ),a2(θ),...,aN(θ)]. We take N=8 neurons, consistent with data from many insect species which possess an eight-column organisation, with each column encoding a different direction (Honkanen et al., 2019; Stone et al., 2017; Pisokas et al., 2020).

Each neuron’s activity is updated depending on its current firing rate and the inputs it receives, both from other neurons in the circuit and externally. We formulate this update rule as follows:(1)a˙(θ)=−a(θ)+ϕ[Wa(θ)+u(t)],

where W is the circuit’s weight matrix, representing the connections between neurons; ϕ is the neural activation function, that converts the total neural input into an output firing rate; and u(t) is the external input that encodes the insect’s angular velocity, via the PEN population of neurons (Green et al., 2017; Turner-Evans et al., 2017; Sayre et al., 2021; Pisokas et al., 2020; Turner-Evans et al., 2020; Hulse et al., 2021).

To simplify our derivations we allow the neural activity values to be both positive and negative, interpreting these values as being relative to a baseline neural firing rate. Similarly, we allow the weights to be both positive and negative, a common simplification in computational models (Li et al., 2023; Cornford et al., 2020; Kriegeskorte and Golan, 2019). This simplification will be addressed in section ‘Comparing the predicted circuit with biological data’ where we compare our model with experimental data.

## Mathematical principles for neural heading integration

A circuit capable of performing heading integration must fulfil the requirements outlined in Table 1. The first two requirements allow us to establish the family of possible path integration circuits. We then use the principle of noise minimisation to determine which circuits perform best.

## Constraints on the neural activity

The neural activity should encode the insect’s head direction with a matching topology. Because the heading is a single angular variable, the topology of the activity space should be a 1D circle.

Furthermore, the symmetry requirement implies that rotating the heading of the insect should rotate the neural activity vector without changing its shape. Concretely, whether the insect is facing north or east, the activity of the neural population as a whole should be the same, but with the identity of the neuron with each activity value being different.

We can formalise the symmetry requirement by considering a head direction, θ, and a rotation by an integer multiple, k, of the angular spacing between neurons, Δθ=2πkN. In this case, individual neuron activities follow the relation(2)an(θ+Δθ)=an−kmodN(θ),

which enforces that the neural activity vector is circularly rotated as the head direction changes. This relation can be expressed in the Fourier domain where, by the shift property, the circular rotation becomes a multiplication by a complex exponential:(3)Ff[a(θ+Δθ)]=Ff[a(θ)]ei2πkfN,

where i=−1 and f∈[0,...,N−1] is the index of the spatial frequency, also called the harmonic. Activity with spatial frequency f has f ‘bumps’ around the ring.

Since the complex exponential has unit norm, the magnitude of the Fourier components remains the same for any rotation, ‖F[a(θ+Δθ)]‖=‖F[a(θ)]‖∀Δθ. Therefore, the shape of the activity pattern, a≡a(0), can also be fully specified by its Fourier domain representation, F[a], and the phase of this activity profile around the network encodes the heading of the insect:(4)Ff[a(θ)]=Ff[a]eiθf.

Taking the inverse Fourier transform with the constraint that the neural activities must be real, we get the following form for the neural activity,(5)an(θ)=∑f=0N−1‖Ff[a]‖cos⁡(2πfnN+θf).

It should be noted that the phase offset, θf, of each cosine waveform scales with the spatial frequency. This is because higher frequency waveforms have shorter wavelengths (in terms of number of neurons), so need their phases to rotate more quickly to move at the same speed around the network.

To explain this in more detail, we consider the case where this scaling is not used and the phase offset is the same for all harmonics, shown in Figure 1 top row. For f=1 (red line in Figure 1), the waveform has one bump and a wavelength of 8 neurons, so a 180° rotation corresponds to the waveform moving 4 neurons. But for f=2 (blue line in Figure 1), the waveform has two bumps and a wavelength of 4 neurons, so a 180° rotation corresponds to moving only 2 neurons, while a 4 neuron shift would correspond to a full rotation. The fact that the waveforms for different frequencies move at different speeds through the network implies that, if multiple spatial frequencies are used to independently encode the heading, their positions would not be aligned and the combined waveform would change shape as different angles are encoded (purple line in Figure 1). This violates the rotational symmetry principle, as the activity would look significantly different when the insect is facing north compared to south.

![Figure 1.](https://cdn.elifesciences.org/articles/91533/elife-91533-fig1-v1.jpg)

**Figure 1.:** Each panel shows the activity profiles encoding a particular heading value. Curves , f=1, and f=2 respectively denote the waveform of the first harmonic, second harmonic, and the sum of the two. The vertical dashed (f=1+f=2 peak) and dotted lines (f=1 peaks) indicate the neurons which respond maximally for the first and second harmonic, respectively. Top row: Encoding the heading as the sum of two independent harmonics causes the waveform to change shape as the insect rotates, because the waveform for each harmonic can only rotate a distance of f=2 as the insect rotates a full revolution to ensure an unambiguous representation. Bottom row: If all harmonics are aligned to rotate at the same speed, the combined waveform shape does not change. However, this alignment implies that higher harmonic waveforms cannot be uniquely mapped back to a heading: here the 360∘f encoding is the same for f=2θ = 0° and 180°.

To solve this problem of misaligned harmonics, we return to the case specified in Equation 5 where the phase offset is scaled linearly with the spatial frequency so that all waveforms move at the same speed and rotational symmetry is ensured, which is shown in Figure 1 bottom row. For a network with N=8 neurons, a 180° rotation shifts the activity waveform by 4 neurons. This 4 neuron shift corresponds to a 48 or 180° phase offset for the f=1 waveform, which has a wavelength of 8 neurons, but a 44 or 360° phase offset for the f=2 waveform, which has a wavelength of 4 neurons. While this maintains rotational symmetry, it implies that the f=2 waveform is the same whether the heading angle 0° or 180° is encoded. As a consequence, a higher harmonic waveform (having f>1) cannot on its own specify the encoded angle. The activity in all harmonics must be considered simultaneously to decode the angle, but even then this decoding might not be unique in the presence of noise (see section ‘Ambiguities in multiple harmonics decoding with drift’). The difficulties associated with encodings utilising multiple harmonics will be further addressed in the following sections.

## Constraints on heading integration circuits

The basic assumptions outlined earlier also constrain the possible heading integration circuits – such circuits should allow for neural activity with the required topology and rotational symmetry to stably exist and propagate. Together, these two principles require that the activity in the circuit should have a constant total magnitude. We consider that this constraint is enforced by the nonlinear neural activation function, ϕ, in Equation 1, as detailed in section ‘Path integration dynamics for heading and position’.

If the network activity is at the desired level, and the external input u(t) is projected onto the ring attractor such that it does not alter the total network activity, then we can consider the network dynamics to be linear at this operating point. Therefore, while within the space of possible activities that corresponds to the ring attractor, our circuit dynamics are effectively described as,(6)a˙(θ)=−a(θ)+Wa(θ)+u(t).

The rotational symmetry principle also applies to the network. For the same shaped activity waveform to be able to stably exist at any position around the network, the network connectivity should also be rotationally symmetric. For example, the connection strength between the neurons encoding the north and north-east directions should be the same as between those encoding south and south-west. Mathematically, this imposes that the weight matrix, W, is circulant, specifically that Wn,m=Wn+k,m+k. This matrix is fully specified by its first row, called the connectivity profile and denoted ω, meaning that we can express the product of the matrix with the neural activity as(7)(Wa(θ))k=Wka(θ)=∑m=0N−1Wk,mam(θ)=∑m=0N−1W0,m−kam(θ)=∑m=0N−1ωm−kam(θ),

which can be simplified in terms of the convolution operation,(8)Wa(θ)=ω∗a(θ).

Considering the case where the insect is not moving, u(t)=0, and the network activity is stable, a˙(θ)=0, we can combine Equation 6 and Equation 8 to get a relation for the stable network activity(9)a(θ)=ω∗a(θ).

In the Fourier domain, this simplifies into(10)Ff[a(θ)]=Ff[ω]Ff[a(θ)].

As for the activity waveform analysis, we note that the Fourier transform is taken on the neural indices, not on the temporal domain.

Here, we have N equations that have to be satisfied, since the Fourier transform of an N-dimensional vector is also N-dimensional. For each harmonic frequency f, Equation 10 has two solutions:

## Minimising noise propagation in the circuit

The only constraint on the connectivity weights given by Equation 10 is that, if a frequency is used for encoding then Ff[ω]=1. There is no restriction on the weights for the inactive harmonics – they remain free parameters.

However, non-encoding channels can still propagate noise, which would be prevented by setting Ff[ω]=0. To illustrate this, we consider white noise, denoted by ϵ, that is added to the neural activity. When this noisy activity evolves in accordance with the dynamics from Equation 8, we have(11)ω∗(a(θ)+ϵ)=ω∗a(θ)+ω∗ϵ,

where the term ω∗ϵ corresponds to noise and should therefore be dampened. We want to minimise the strength of that noise, which is quantified by its variance(12)Var[ω∗ϵ]=E[‖ω∗ϵ‖2]=‖ω‖2Var[ϵ].

Hence the magnitude of the noise that passes from one time interval to the next is modulated by the magnitude of the weight vector. By Parseval’s theorem,(13)∑f|Ff[ω]|2=∑n|ωn|2=‖ω‖2,

which implies that to minimise noise propagation in the network we should impose Ff[ω]=0 for all harmonics, f, where Ff[a(θ)]=0. We show this in simulation in Figure 2, where only the first harmonic encodes information and we vary the weights of the other harmonics. The noise is indeed minimised if the weights for all non-encoding harmonics are set to zero.

![Figure 2.](https://cdn.elifesciences.org/articles/91533/elife-91533-fig2-v1.jpg)

**Figure 2.:** Increasing the number of active harmonic frequencies increases the effect of errors in the network. (A) Weight matrix profiles, , for networks with increasing numbers of harmonics. (ωB) Normally distributed noise with zero mean and standard deviation 0.3 was added to the network activity, then the network state updated until it reached steady state. Networks with fewer harmonics better filtered out noise. (C) Noise variance increases linearly as the number of active harmonics increases, as predicted by Equation 12. The sample size was n=1000 trials for each active harmonics set, and the error bars show the standard deviation over trials.

This result establishes that all non-encoding harmonics in the network should be set to 0 to minimise noise propagation, and allows us to recover the circuit connectivity(14)ωn=∑f∈Fcos⁡(2πnNf),

where F is the set of harmonics used to encode the head direction, F={f∈[1...N−1]:‖Ff[a]‖≠0}. The choice of F therefore determines both the harmonics used for encoding the angle in the activity and the connectivity of the circuit that supports this activity.

We leverage the same logic to prove that the number of encoding channels does not affect the signal-to-noise ratio in the network. If we have c encoding channels, each with the same activity, the total activity will grow linearly with c. The noise will also grow with ‖ω‖2=c, meaning that the signal-to-noise ratio will remain constant.

We now return to the question of whether using one or multiple harmonics is better. As mentioned, the signal-to-noise ratio in the network remains constant as additional encoding channels, c, are used. But additional channels imply additional harmonics, which by Parseval’s theorem require a higher total neural activity. If the total activity in the network is limited, the signal-to-noise ratio is in fact decreased when using more than one harmonic.(15)SNR∝‖a‖2‖ω‖2=‖a‖2c.

Additionally, as detailed in sections ‘Constraints on the neural activity’ and ‘Ambiguities in multiple harmonics decoding with drift’, circuits using multiple harmonics perform worse in high noise environments because they are not guaranteed to provide an unambiguous orientation encoding. Finally, as we will discuss in sections ‘Learning rules and development’ and ‘Convergence of Oja’s rule with multiple harmonics’, the use of multiple harmonics also complicates the circuit’s development. We therefore only select circuits that use a single harmonic for further analysis, reducing the number of possibilities to N.

## Determining the optimal circuit

As we consider networks with N=8 neurons, consistent with multiple insect species (Honkanen et al., 2019; Stone et al., 2017; Pisokas et al., 2020), the possible single harmonic circuits are f={1,2,3,4,5,6,7}, where the zeroth harmonic is discarded because it only represents the baseline neural activity. This gives the following activities and weights, derived from Equation 5 and Equation 14(16)an(θ)=cos⁡(2πnfN+θ)ωn=cos⁡(2πfnN).

The circuits for the first four harmonics are plotted in Figure 3, but not all of these circuits are valid. In particular, circuits with even spatial frequencies have multiple neurons with identical activity values because they share a common divisor with N=8, as explained in detail in section ‘Degenerate circuits’.

![Figure 3.](https://cdn.elifesciences.org/articles/91533/elife-91533-fig3-v1.jpg)

**Figure 3.:** We show four circuits corresponding to each of the individual harmonics  in panels (f=1,2,3,4A, B, C, and D), respectively. Excitatory synapses are marked in red and inhibitory in blue. Neurons are shown in yellow with each having a black arrow that marks the direction to which it is tuned from Equation 16. The  circuit is the simplest and constitutes our baseline. For the other cases we plot the original connectivity in the upper row and the rearranged network in the lower row. We find that the f=1 circuit consists of two independent subnetworks encoding orthogonal directions, the f=2 case is identical to f=3 after permuting neuron indices, and the f=1 case results in two connected groups of neurons inhibiting each other, hence it can only encode one direction. As such, all cases either have a degenerate ring structure (f=4) or are equivalent to f=2,4 after permutation.f=1

For f=4 there are only two unique activity values, an=±cos⁡(θ)∀n, so this circuit can only encode one dimension, not a circular topology (see Figure 3D). For f=2 and f=6 (not plotted), there are four unique activity values, allowing the angle to be properly encoded. However, these circuits are degenerate because they are composed of two independent subcircuits, each encoding one direction (see Figure 3B). Because the weights connecting the two subcircuits are all zero, the activity in each subcircuit is independent of the activity in the other, and so the overall activity cannot be constrained to have the required circular topology.

All circuits with odd harmonic frequencies are equivalent. For example, as shown in Figure 3, the connections in the circuit for f=3 are the same as those for the f=1 circuit after the neuron identities are permuted. As detailed in section ‘Equivalence under permutation’, the frequencies f={1,3,5,7} always give the same circuit because the odd frequencies are coprime with the number of neurons N=8.

Since the activities and weights of all the non-degenerate circuits f={1,3,5,7} are the same as the base harmonic f=1 up to a permutation, we choose the lowest harmonic f=1, which gives us the following activity and weights:(17)an(θ)=cos⁡(2πnN+θ)ωn=cos⁡(2πnN).

## Comparing the predicted circuit with biological data

Our theory proposes an optimally noise-resistant circuit for heading integration, and its corresponding activity. The prediction that heading should be encoded as a sinusoidal activity bump is consistent with previous theoretical models (Touretzky et al., 1993; Wittmann and Schwegler, 1995; Hartmann and Wehner, 1995; Zhang, 1996; Vickerstaff and Di Paolo, 2005; Haferlach et al., 2007; Stone et al., 2017), as well as experimental evidence in both the locust and fruit fly (Heinze et al., 2009; Turner-Evans et al., 2017). We note, however, that data from the fruit fly shows a more concentrated activity bump than what would be expected from a perfect sinusoidal profile (Seelig and Jayaraman, 2015; Turner-Evans et al., 2017), and that calcium imaging (which was used to measure the activity) can introduce biases in the activity measurements (Siegle et al., 2021; Huang et al., 2021). Thus the sinusoidal activity we model is an approximation of the true biological process rather than a perfect description.

Importantly, our theory proposes that the optimally noise-resilient heading integration circuit should have synaptic weights that follow a sinusoidal pattern, even though such weights are not necessary for producing sinusoidal activity as discussed in section ‘Minimising noise propagation in the circuit’. This is the main prediction of our theory and we sought to validate it using connectivity data from the locust and fruit fly.

However, before we can directly compare our model with biological circuits, we must address a number of modelling simplifications:

Therefore, we simplified the biological connectivity to produce an equivalent circuit that could be directly compared with our model prediction. The neural population in our theoretical model corresponds to the biological EPG neurons, as these encode the integrated heading. We considered the other 3 neuron types that are part of the compass circuit (PEG, PEN, and Delta7 – see Kakaria and de Bivort, 2017; Pisokas et al., 2020) as just implementing connections between EPG neurons in accordance with biological constraints. We counted the number of different paths between EPG neurons, accounting for the sign of the connections (whether the path passed through an inhibitory Delta7 neuron), and used the net path count as a proxy for connectivity strength. This process is explained in detail in section ‘Path counting’.

We then computed the average connectivity profile, i.e., how each neuron connected to its neighbours around the ring, and compared this profile to the closest fitting sinusoid. Because the neuron gains, absolute synaptic strength and biophysical properties of the neurons are unknown, the units of the net path count are not necessarily equivalent to our abstract connection strength. We therefore fit an arbitrarily scaled and shifted sinusoid to the connection counts:(18)ωm−n=βcos⁡(2π(m−n)N)+γ,

where m−n is the circular distance between 2 neurons while β and γ are constants that are fit to minimise the precision-weighted mean squared error compared with the experimental connectivity profile (see section ‘Fitting weights’).

Analysing the data from Pisokas et al., 2020, we consider the shortest excitatory and inhibitory paths between EPG (also known as CL1a) neurons in the locust, which have lengths of 2 and 3, respectively. There are no direct connections of length 1, and all the paths of length ≥4 must pass through the same neuron-type multiple times. This path counting analysis for the locust is shown in Figure 4A, and the procedure is detailed in section ‘Path counting’. We find that the connectivity profile between neurons for the locust is very close to sinusoidal in shape, supporting our theoretical prediction.

![Figure 4.](https://cdn.elifesciences.org/articles/91533/elife-91533-fig4-v1.jpg)

**Figure 4.:** The biological network models of (A) the locust and (B) the fruit fly, with four distinct neural populations each were simplified to equivalent networks with one population by counting paths of lengths 1, 2, and 3 between EPG neurons (which encode the integrated heading) and using the net signed path count as a proxy for connectivity strength. The average connectivity profile for each neuron to its neighbours around the ring was compared to the sinusoidal connectivity predicted by our theory. The locust network has no standard deviation because the data in Pisokas et al., 2020, are based on light microscopy which couldn’t resolve variations between columns. Excitatory connections are shown in red and inhibitory connections in blue, while the strength of a connection is indicated by the line width.

For the fruit fly, we used data from Scheffer et al., 2020, which provides synapse counts between pairs of neurons. These synapse counts were used as a proxy for connectivity strength, a view that has been validated in previous experiments (Liu et al., 2022; Barnes et al., 2022). After identifying the neurons and connections of interest, we grouped the neurons in eight columns following the logic presented in Pisokas et al., 2020, with detailed methodology explained in section ‘Data preprocessing’. We repeated the path counting analysis for the fruit fly with synapse count data (Figure 4B), and found that while the data are noisy, the connectivity profile fits a single sinusoid pattern reasonably well. However, the high variability in the synapse counts makes our hypothesis difficult to differentiate from alternative shapes (see section ‘Fitting weights’).

Taken together, this analysis shows that our theory is consistent with experimental data – using binary connectivity data for the desert locust and synapse count data for the fruit fly.

## Learning rules and development

Having validated the connectivity of our theoretical circuit by comparing it to experimental data, we ask whether our circuit lends itself to biological development. Specifically, we show that even though our circuit requires precise connection strengths, this connectivity can be developed naturally by a Hebbian learning rule. Our approach follows from previous research which has shown that simple Hebbian learning rules can lead to the emergence of circular line attractors in large neural populations (Stringer et al., 2002), and that a head direction circuit can emerge from a predictive rule (Vafidis et al., 2022). In contrast to this work, we focus only on the self-sustaining nature of the heading integration circuit in insects and show that our proposed sinusoidal connectivity profile can emerge naturally.

Because the weight matrix is circulant, its eigenvalues are equal to the Fourier spectrum of its first row, which we derived to only have one nonzero value, for f=1. The network therefore only has a single eigenvalue and so projects activity into a single dimension. This operation is similar to classical dimensionality reduction methods such as principal component analysis, which can be implemented by Hebbian-like learning rules (Dayan and Abbott, 2001). We thus analyse the effects of incorporating a modified Oja’s rule into our model, a classical variant of Hebbian learning where the synaptic strength between 2 neurons grows when both neurons are active simultaneously, and the total synaptic strength is regularised to prevent exploding weight growth,(19)dWn,mdt=ηdθdt(am(t)an(t)−an2(t)Wn,m),

where Wn,m is the synaptic connection strength from neuron m to neuron n, am and an are the pre- and post-synaptic activities, respectively, and ηdθdt is an adaptive learning rate where the plasticity is proportional to the rotational speed, whereas in the classical Oja’s rule it would be constant.

For our analysis we assume that the insect faces all possible directions, and therefore that the neural activity goes around the full circle. We then integrate the weight updates over some long period of time,(20)ΔWn,m=∫dWn,mdtdt=∫dWn,mdt(dθdt)−1dθ=η∫θ=02π[am(θ)an(θ)−an(θ)2Wn,m]dθ,

where θ is the integration space. Applying the activity from Equation 17, we can find the fixed point of this update rule, when ΔWn,m=0:(21)Wn,m=η∫θcos⁡(θ+2πnN)cos⁡(θ+2πmN)dθη∫θcos2⁡(θ+2πnN)dθ=cos⁡(2π(n−m)N).

Combined with Equation 7 and Equation 17, this result means that if there is sinusoidal activity in the network, the weights will naturally converge to the optimal sinusoidal values by way of our variant of Oja’s rule. This leads to the emergence of sinusoidal activity and weights from self-consistency: initial noisy sinusoidal activity will enforce weights that are close to a sinusoid, and those weights will filter out noise to make the activity even closer to a sinusoid, which will in turn make the weights more sinusoidal. This process will iteratively make the activity and the weights converge to the solution from Equation 17.

An important point in the use of Oja’s rule is that it would tend to concentrate the activity in a single harmonic. In a linear network, the harmonics would compete during learning, leading to one single harmonic emerging and all others being suppressed, as shown in section ‘Linear neurons’. For neurons with a nonlinear activation function, secondary harmonics would emerge, but would remain small under mild assumptions, as shown in section ‘Neurons with nonlinear activations’. Oja’s rule will still cause the weights to converge to approximately sinusoidal connectivity.

The finding that the weights will converge to a sinusoidal connectivity with learning has two interesting consequences from a biological standpoint: First, our circuit can emerge even when starting with only very coarse initial weights, without the need for high precision initial connectivity. Second, this simple plasticity rule allows the system to repair or recover from perturbations in its synapses as shown by simulations in Figure 5. However, this learning rule only applies to the weights that ensure stable, self-sustaining activity in the network. The network connectivity responsible for correctly integrating angular velocity inputs (given by the PEN to EPG connections in the fly) might require more elements than a purely Hebbian rule (Stringer et al., 2002), such as the addition of a predictive component (Vafidis et al., 2022).

![Figure 5.](https://cdn.elifesciences.org/articles/91533/elife-91533-fig5-v1.jpg)

**Figure 5.:** The synaptic weights converge to a sinusoidal pattern under our modified Oja’s rule when the network activity is dynamic and a sinusoidal input is provided. (A) The weights start at zero and slowly converge to the prescribed sinusoidal profile, showing that this connectivity can emerge from scratch. (B) The sinusoidal weights are perturbed by noise but learning ensures that the weight profile is corrected. In both cases the network’s initial activity is corrupted with zero mean Gaussian noise. Noisy sinusoidal input is provided to rotate the activity bump around the network at a constant speed of 1/8 neurons per timestep. The simulation runs for 100 periods. Parameters:  integration timestep N=8,.Δt=0.01,η=0.1,‖a‖=1,σW=0.2,σa=0.2,σu=0.2

## Evolution of the eight-column circuit

Having derived and experimentally validated the theoretical circuit, we now address another question: whether there might be a reason that insect head direction circuits have an eight-column architecture (Honkanen et al., 2019; Stone et al., 2017; Pisokas et al., 2020). The derivations leading to Equation 17 are valid for other values of N, so there is no a priori reason to expect N=8.

Our reasoning follows recent studies in genetics (Johnston et al., 2022; Dingle et al., 2018), which argue that an observed organism is more likely to have resulted from a simple than a more complex genome: evolution favours simplicity. We note that powers of two are easier to generate with replication dynamics than other numbers, because they just require each cell to divide a set number of times. Other numbers require that, at some point, two cells resulting from a division must behave differently, necessitating more complex signalling mechanisms and rendering this possibility less likely to have been developed by evolution without some other driving factor. We therefore expect N to be a power of two unless required to be otherwise.

As we show in section ‘Circuits with different neuron counts’, not all numbers of neurons enable a working circuit. The circuits for N=2 and N=4 are degenerate – either producing a single dimensional encoding, or two disconnected circuits that do not enforce the required circular topology. N=8 is the smallest power of two that could result in a non-degenerate circuit. This hints at the possibility that the eight-column architecture is not a chance evolutionary artefact, but rather that it is the genetically simplest circuit capable of performing heading integration.

## Discussion

In this work we derived an optimal noise-minimising circuit for encoding heading and verified that this circuit matches experimental data from insects. Furthermore, we showed that such a circuit can be developed and maintained by a biological learning rule, and proposed a mathematical argument for the eight-column structure found in insect compass circuits. In this section, we discuss the implications and limitations of these contributions, and outline potential future work.

Heading integration circuits in insects have been extensively studied, with models ranging in complexity from simplified conceptual networks (Wittmann and Schwegler, 1995; Cope et al., 2017) to sophisticated models constrained by biological data and featuring multiple neuron types (Kakaria and de Bivort, 2017; Su et al., 2017; Kim et al., 2017; Pisokas et al., 2020; Lyu et al., 2022). Previous theoretical work has argued that a sinusoidal activity encoding is such a common motif in insect navigation because it facilitates elementwise vector addition (Wittmann and Schwegler, 1995). However, this cannot be the only reason because as we show there is a whole family of circuits with different encoding patterns that enable easy vector addition. By showing that sinusoidal activity emerges from the theoretically most noise-resilient heading integration circuit, and verifying that the corresponding circuit matches experimental data, we close this explanatory gap.

We also show that our proposed circuit can be developed by a simple Hebbian-based learning rule, and that the presence of the eight-column structure can be explained from the perspective of replication dynamics. Both results align with the idea that evolution should be biased towards structures that are easier to encode in the genome (Johnston et al., 2022; Alon, 2007) and learn (Zador, 2019). To the best of our knowledge, this is the first time that such arguments have been put forward in the context of a specific circuit with a specific function.

Our work still has some unaddressed limitations, in particular regarding the topology of the activity. The use of a circular topology to encode the head direction of the insect is valid only in 2D environments. But many species, including the fruit fly, can navigate in a 3D environment. We argue that even if these insects live in a 3D environment, the third dimension (up-down) is different from the other two due to gravity and the existence of a hard boundary (the ground). Further studies would be required to investigate the full effects of 3D motion.

We could also investigate circuits that integrate position, not only heading, which would require the activity to have a 2D plane topology instead of a circle. This would be particularly relevant for foraging insects such as bees or ants, whose ability to remember their position with respect to their nest has been the subject of many experimental and computational studies (Collett, 2019; Wehner and Srinivasan, 2003). The position integrating neurons in these insects are also predicted to have sinusoidal activation patterns (Wittmann and Schwegler, 1995; Vickerstaff and Di Paolo, 2005; Stone et al., 2017).

Finally, another interesting avenue for future work is to compare the encoding of direction in insects with that of mammals, which encode heading in a fundamentally different way that uses many more neurons. This raises a critical question: why would the circuit and encoding be different if navigation follows similar principles across species? We speculate that the difference might lie in the type of navigation that the two classes of animals use. Insects often rely on a reference system that is globally anchored to a certain point or phenomenon, whether it is their nests for ants and bees, the sunlight polarisation pattern for locusts, or the milky way for dung beetles. On the other hand, mammals such as rodents typically do not use global cues but rely on local landmarks that are context-dependent and only occur in specific locations. Therefore, mammals must employ a flexible encoding that can be updated as different environments are explored. Further investigation of this possibility would require a different set of principles than those selected here.

## Materials and methods

## Path integration dynamics for heading and position

Here, we make more precise statements about the dynamics of the circuit. The topology of the activity is a circular line attractor, so that any perturbation falls back into a circle and the position of the activity around the circle represents an angle. In our circuit with the dynamics from Equation 1, this circular line attractor is achieved by setting(22)‖ϕ′[Wa]‖=1∀‖a‖=r‖ϕ′[Wa]‖<1∀‖a‖>r‖ϕ′[Wa]‖>1∀‖a‖<r

where r is the radius of the attractor. Given that the dynamics are effectively linear we can apply a Fourier transform and write the original dynamics around the line attractor directly in the spatial Fourier basis,(23)Ff[a˙]=Ff[−a+ω∗a+u(t)],

which we can expand to obtain(24)Ff[a˙]=−Ff[a]+Ff[ω]Ff[a]+Ff[u(t)],

which only applies to the circular activity where the dynamics are linear. To incorporate the dynamics that force the activity to return to the cycle, we add a new term into the network dynamics which fulfils Equation 22 – increasing ‖Ff[a]‖ if ‖a‖<r and decreasing it if ‖a‖>r. This increase or decrease can be incorporated as a simple scaling factor on the activity decay term(25)Ff[a˙]=−α(r−‖a‖)Ff[a]+Ff[ω]Ff[a]+Ff[u(t)],

where α(r−‖a‖) is a nonlinear smooth function with a single minimum and α(0)=1, which forces the activity to have the appropriate magnitude, ‖a‖=r.

Note that this doesn’t require the neurons to have access to a global activity magnitude signal because each neuron receives a sufficient number of inputs to locally compute the total activity in the network. See the f=1 circuit in Figure 3: each neuron receives inputs from all others except those tuned to an orthogonal direction, but the activity of these orthogonal neurons can be computed from the correlated neurons next to them. For example, neuron 1 receives input from all neurons except 3 and 7, but the activities of these neurons can be computed from the activities of neurons 2 and 4 or 6 and 8, respectively. Note also that this is not the case for degenerate circuits such as f=2 in Figure 3, which would require an activation function with access to global information to constrain the total activity.

As the activity always falls back to the circular line attractor, the heading integration is linear around the circle. This implies that any small movement of the animal or the perception of a sensory cue is first projected onto the circle, then linearly integrated. We therefore only consider how network inputs cause the activity to rotate around the network,(26)Ff[a˙]=−α(r−‖a‖)Ff[a]+Ff[ω]Ff[a]+Ff[u(t)]⊥a,

where Ff[u(t)]⊥a is the projection of the input signal perpendicular to the current activity pattern.

In more intuitive terms, the neurons have a saturating nonlinear activation function where they modulate their gain based on the total activity in the network. If the activity in the network is above the desired level, r, the gain is reduced and the activity decreases, and when the activity of the network is less than desired level, both the gain and the activity increase. Note that in this scenario transient deviations from the line attractor, which would induce nonlinear behaviour in the circuit dynamics, are tolerable. External inputs, u(t), could transiently modify the shape of the activity, producing activity shapes deviating from what the linear model can accommodate. For example, the shape of the bump attractor could be modified through nonlinearities while the insect attains high angular velocity (Turner-Evans et al., 2017).

Such nonlinear dynamics do not conflict with the theory developed here, which only requires linearity when the activity is projected onto the circular line attractor. In our framework, the linearity of integration at the circular line attractor is not a computational assumption, but rather it emerges from the principle of symmetry.

## Ambiguities in multiple harmonics decoding with drift

We consider the case where multiple harmonics are used, and their phases have drifted from each other. We only focus on angular drift, rather than noise in the full activity, because as noted in section ‘Path integration dynamics for heading and position’, any deviations in the overall activity level in the network will dissipate.

For example, we consider the harmonics f1 and f2. The activity is given by Equation 5(27)an(θ)=cos⁡(2πf1nN+f1θ)+cos⁡(2πf2nN+f2θ).

If the phase of the second harmonic drifts by δθ,(28)anδθ(θ)=cos⁡(2πf1nN+f1θ)+cos⁡(2πf2nN+f2θ+δθ).

We can calculate the alignment between the activity with drift and the activity without drift as a dot product of the activity vectors,(29)⟨a(θ),aδθ(θ)⟩‖a(θ)‖‖aδθ(θ)‖=1‖a(θ)‖2∑nan(θ)anδθ(θ)=1+cos⁡(δθ).

However, there are other angles where the alignment is better. For example, we can consider an estimate angle, θ^, with its corresponding activity, a(θ^), which gives(30)⟨a(θ^),aδθ(θ)⟩‖a(θ^)‖‖aδθ(θ)‖=1‖a(θ)‖2∑nan(θ^)anδθ(θ)=cos⁡(θ−θ^)+cos⁡(θ−θ^+δθ).

For small δθ, this is maximised when θ^=θ+δθ/2. However, since θ is circular, if the drift is π then there are two possible positions given by θ^=θ±π/2.

This implies that an encoding using multiple harmonics does not necessarily offer a unique decoding in the presence of noise.

## Equivalent circuits and degeneracies

## Equivalence under permutation

The activity of neurons given by Equation 5 implies that the preferred angle of neuron n is given by(31)φn=2πfnmodNN,

where in our case N=8. Table 2 shows nfmod(N) evaluated for all neurons in the network using different harmonics. We notice that for f={1,3,5,7} all the numbers from zero to seven appear, while for f={2,6} we only get the even numbers, for f=4 we get only zero and four, and for f=8 there is only zero.

The explanation is based on number theory. If f and N have the greatest common divisor gcd(N,f)=d, then nfmodN=0 for n=N/d. This implies that the preferred angle of neuron n=0 is the same as that of n=N/d. When N,f are coprime d=1, n goes from 0 to N−1 without repeating any value. However, when d>1, the neuron n=N/d has the same tuning as the neuron n=0, the neuron n=N/d+1 has the same tuning as the neuron n=1 and so on. In other words, the angular tuning of the neurons has a period of gcd(N,f).

This divides the possible circuits into the following groups:

## Degenerate circuits

Given the groupings presented in the previous subsection, we notice that not all of them allow the encoding of a full range of angles, (0°, 360°). Notably, for f=8 the neurons only encode one angle, and for f=4 only two complementary angles are encoded, 0 and π. This means that we cannot represent a full circle, because we need two different dimensions to do so, but in both of these cases we can only encode one.

For f=2,6 we obtain two groups of neurons, and in each group there are 2 neurons that encode two opposing directions, thus it is possible to cover a full circle. However, the circuit is degenerate, as shown in Figure 3. In this case there are no connections between even and odd neurons. Thus, we have two groups of neurons that are disconnected, and each group encodes only one direction (either north-south or east-west). While the encoding could work in principle, the circuit is decoupled, meaning that there is nothing in this circuit that prevents the activity from having activities outside the circular topology: as the two circuits are disconnected, a given value of activity in one group does not restrict the activity in the other.

## Circuits with different neuron counts

We evaluate the viability of circuits with other values of N. From findings in the the previous section, we note that choosing N to be a prime number implies that all frequencies will be coprime with N, and thus that all the neurons will have a different tuning.

For N=2, the two angles are 0,π, in which case the circuit can only encode one dimension and thus cannot encode a full circle, as was the case for N=8,f=4 in section ‘Degenerate circuits’.

For N=4, if f=2 the circuit can encode only the angles 0,π and we have the same case as for N=2. But if f=1 or f=3, the neurons are tuned to the angles 0,π/2,π,3π/2 which can encode a circle. However, by looking at the connectivity matrix from Equation 16, we find that neurons 1, 3 are connected to one another, but not to 2, 4, as was the case for N=8,f=2 in section ‘Degenerate circuits’. This implies that the circuit does not enforce a circular topology, and thus it does not work.

Notice that we could think of another structure where each neuron encodes a different direction. Intuitively, we would have a north-south neuron and an east-west neuron, as we would have in Cartesian coordinates. However, this would have the same problem as N=4, where the 2 neurons would not interact and thus the topology would be wrong. Additionally, when the insect heads north, the north-south neuron would be very active, while when it heads south it would be very inactive. This means that the circuit as a whole would have a different firing rate depending on the direction, breaking the symmetry assumption.

## Path counting

We counted the number of different paths between EPG neurons, accounting for the sign of the connections (whether the path passed through an inhibitory 7 neuron), and used the net path count as a proxy for connectivity strength. The results of this analysis are shown in section ‘Comparing the predicted circuit with biological data’, but we will detail the process here using the locust network from Pisokas et al., 2020, as an example, shown in Figure 6.

![Figure 6.](https://cdn.elifesciences.org/articles/91533/elife-91533-fig6-v1.jpg)

**Figure 6.:** (A) The full locust connectivity network from Pisokas et al., 2020, and (B) the connections with path lengths 2 and 3 from  to all other EPG1 neurons in the network. Because the network is rotationally symmetric these path counts generalise to all EPG neurons as shown in EPGTable 3.

We consider the shortest excitatory and inhibitory pathways between EPG neurons, which have lengths of 2 and 3 respectively. There are no direct paths between EPG neurons in the locust circuit. In this case there are two paths of length 2 that implement self-excitatory connections for EPG1:

And there is one connection of path length 2 that connects EPG1 to each of its nearest neighbours:

For inhibitory connections there are four paths of length 3 that connect EPG1 to the neuron on the opposite side of the ring, EPG5. These are:

There are three connections of path length 3 connecting EPG1 to EPG4:

Finally, there is one path of length 3 connecting EPG1 to the neuron perpendicular to it around the ring, EPG3:

We then add these connections together to obtain the net path count profile for the network. Because the network is rotationally symmetric, the connections from EPG1 are the same as the connections from EPG2 but with the neurons indices incremented by 1. The generalised profile is shown in Table 3.

## Data preprocessing

The following section details our data preprocessing to produce a central complex circuit for the fruit fly similar to that in Pisokas et al., 2020, using synaptic counts from the fruit fly connectome dataset (Scheffer et al., 2020). Full details are shown in our available code.

We first identified the 6 neuron types which corresponded to the neurons of interest in the central complex (Table 4).

We grouped the two PEN and two EPG populations together for further analysis.

From the connectome data we created a connectivity matrix (Figure 7) containing the number of synapses between all pairs of neurons of the above-mentioned types. This contained 129,473 synapses between 152 neurons in total.

![Figure 7.](https://cdn.elifesciences.org/articles/91533/elife-91533-fig7-v1.jpg)

**Figure 7.:** On the horizontal axis are the names of the pre-synaptic neurons while on the vertical axis the names of the post-synaptic neurons. Neurons of each cell type are ordered by the glomerulus they innervate and arbitrarily within glomerulus.

Next, neurons in the same glomerulus were grouped together. The EPG neurons were divided between 18 glomeruli, L1-L9 and R1-R9. The PEN neurons were also divided between 16 glomeruli, L2-L9 and R2-R9. The PEG neurons were divided into 18 glomeruli with only 1 neuron in each, L1-L9 and R1-R9. The Delta7 neurons had 10 unique sub-types (Table 5) which were grouped into eight glomeruli based on their left glomerulus index – i.e., L4R5_R and L4R6_R were grouped in L4.

After this grouping we had a connectivity matrix of 60 neurons in total (Figure 8).

![Figure 8.](https://cdn.elifesciences.org/articles/91533/elife-91533-fig8-v1.jpg)

**Figure 8.:** On the horizontal axis are the names of the pre-synaptic neurons while on the vertical axis the names of the post-synaptic neurons. Neuron groups are ordered by the glomerulus they innervate.

For the EPG, PEN, and PEG neurons we then grouped glomeruli mirrored in the two hemispheres together – i.e., L1 and R1 were grouped into glomerulus 1. This resulted in a connectivity matrix of 34 neurons (Figure 9).

![Figure 9.](https://cdn.elifesciences.org/articles/91533/elife-91533-fig9-v1.jpg)

**Figure 9.:** On the horizontal axis are the names of the pre-synaptic neuron groups while on the vertical axis are the names of the post-synaptic neuron groups. Neuron groups are ordered by the glomerulus they innervate.

Finally, as in Pisokas et al., 2020, we grouped the PEG9 and PEG1 neurons and EPG9 and EPG1 neurons together. The former because they both output to the same ellipsoid body segment, and the latter because they both receive common input. This resulted in a connectivity matrix with 32 neurons (Figure 10) which we used for the analysis in Figure 4 as this network had the eightfold rotational symmetry compatible with our theoretical model.

![Figure 10.](https://cdn.elifesciences.org/articles/91533/elife-91533-fig10-v1.jpg)

**Figure 10.:** On the horizontal axis are the names of the pre-synaptic neuron groups while on the vertical axis the names of the post-synaptic neuron groups. Neuron groups are ordered by the glomerulus they innervate.

## Fitting weights

Having calculated the paths or synaptic strengths between EPG neurons in the network, we next computed the average connectivity profile for the network – how each EPG neuron connected to its neighbours a certain distance around the ring. We then compared this connectivity profile to the closest fitting sinusoid to quantify to what degree our prediction of sinusoidal weights was consistent with biological data.

We use the vector(32)ω^d=βcos⁡(2πdN)+γ,

where d=((m−n)+4mod8)−4∈[−4...3] is the signed circular distance from neuron m to neuron n.

In the networks from Pisokas et al., 2020, the weights are rotationally symmetric, so we minimise the mean squared error between the sinusoidal profile and the biological connectivity profile,(33)β∗,γ∗=argminβ,γ1N∑d=−N/2N/2−1(ω^d(β,γ)−ωd)2,

by using least squares.

The network derived from the synaptic count data in Scheffer et al., 2020, is not rotationally symmetric so each value in the average connectivity profile, ωd, has a corresponding standard deviation, σd. In this case we minimise the precision-weighted mean squared error, which emphasises fitting connectivity profile values that are more consistently seen in the network:(34)β∗,γ∗=argminβ,γ1N∑d=−N/2N/2−1(ω^d(β,γ)−ωdσd)2.

The result of fitting sinusoidal profiles to the data is shown in section ‘Comparing the predicted circuit with biological data’. Since the fit for the fruit fly is not as clear as for the locust, we also compared the observed weights in the fruit fly with Gaussian and von Mises curves. Since both the Gaussian and von Mises distributions also have a parameter specifying their width, this requires fitting an extra parameter. For the Gaussian we have(35)βge−n2σg+γg,

where βg,σg,γg are parameters to fit. For the von Mises distribution we have(36)βveκvcos⁡(n)+γv,

where βv,κv,γv are parameters to fit. For both the Gaussian and von Mises, we find a good agreement with the weights in Figure 11, and a lower root mean square error (RMSE) than with any combination of harmonics. However, we note that our sinusoidal model has two parameters instead of three, so to make a fair comparison we use the corrected Akaike information criterion (AICc) (Burnham and Anderson, 2004), which is given by(37)AICc=2p−2ln⁡(L)+2p2+2pN−p−1=2p+2NRMSE2+2p2+2pN−p−1,

![Figure 11.](https://cdn.elifesciences.org/articles/91533/elife-91533-fig11-v1.jpg)

**Figure 11.:** When fixing the width parameters of these distributions to match the sinusoid, all three distributions provide a very similar fit. Note that the –4 and 4 neuron indices are the same and just duplicated for visualisation purposes.

where p is the number of distribution parameters, N the number of samples, and ln⁡(L) is the log-likelihood, which in this case is the sum of squared errors, ln⁡(L)=−NRMSE2. We find that the lowest AICc (corresponding to the best model) corresponds to the harmonic f=1 (Table 6).

As a complementary approach to evaluate the shape of the distribution, we first fit the Gaussian and von Mises distributions to the best fit f=1 curve. We then freeze the width parameters of the distributions (σg for the Gaussian and κv for the von Mises) and only optimise the amplitude and vertical offset parameters (β and γ) to fit the data. This approach limits the number of free parameters for the Gaussian and von Mises distributions to two, to match the sinusoid. The results are shown in Figure 11 and Table 6. Both the fixed-width Gaussian and von Mises distributions are a slightly better fit to the data than the sinusoid, but the differences between the three curves are very small.

In simplifying the fruit fly connectome data, we assumed all synapses of different types were of equal weight, as no data to the contrary were available. Different synapse types having different strengths could introduce nonlinear distortions between our net synaptic path count and the true synaptic strength, which could in turn make the data a better or worse fit for a sinusoidal compared to a Gaussian profile. As such, we don’t consider the 2% relative difference in RMSE between the f=1 sinusoid and fixed-width Gaussian and von Mises distributions to be conclusive.

Overall, we find that the cosine weights that emerge from our derivations are a very close match for the locust, but less precise for the fly, where other functions fit slightly better. Given the limitations in using the currently available data to provide an exact estimate of synaptic strength (for the locust), and due to the high variability of the synaptic count (for the fruit fly), we consider that our theory is compatible with the observed data.

## Convergence of Oja’s rule with multiple harmonics

## Linear neurons

Integrating our modified Oja’s learning rule updates (Equation 19) over all angles in the position space gives us the following:(38)Δω=a∗a−‖a‖2ω,

which we can transform into the Fourier domain:(39)Ff[Δω]=Ff[a]2−‖a‖2Ff[ω].

The steady-state solution when the weight update is 0 is:(40)Ff[ω]=Ff[a]2‖a‖2.

By Parseval’s theorem, ‖a‖2=∑f‖Ff[a]‖2 so the Fourier spectrum of the steady-state weights is just the normalised Fourier spectrum of the input:(41)Ff[ω]=Ff[a]2∑f‖Ff[a]‖2.

From this we can see that the stable L1 norm of F[ω] is 1,(42)∑f|Ff[ω]|=1∑f‖Ff[a]‖2∑f|Ff[a]2|=1.

If we combine this result with Equation 10, we find that in the case of a single encoding frequency, Ff∗[a]>0, Oja’s rule will result in a single stable harmonic with Ff∗[ω]=1 because ∑fFf[a]2=Ff∗[a]2.

If Oja’s rule has a normalising factor added to account for the number of encoding harmonics used, |F|,(43)Δω=a∗a−1|F|‖a‖2ω,

then the steady-state solution for the weights becomes(44)Ff[ω]=|F|Ff[a]2∑fFf[a]2,

where the L1 norm of ω=|F|. In this case multiple harmonics could develop stable values of Ff[ω]=1, but only if the activity magnitudes for these harmonics are identical. If any perturbation affects the activities, the harmonic which happens to have the larger activity will begin to dominate the other by the dynamics of Equation 43, until only one remains.

Therefore, the only case where our learning rule results in a stable solution robust to perturbations is when only one harmonic is used.

## Neurons with nonlinear activations

An analysis similar to the previous case applies when the firing rate of the neurons has a nonlinear activation. For a given activity profile, Equation 41 still applies. Thus, for an activity profile a, it will generate the weight profile(45)ω=1‖a‖2∑f|Ff[a]|2,

where we set ‖ω‖=1 for convenience of notation. Note that the squaring process will induce a weight distribution in which the larger harmonic will be enhanced more than the rest.

Having obtained the weights, the equation for the activity profile can be solved through the self-consistency setting in which u(t)=0 and the activity is maintained,(46)an(θ)=ϕ(∑m=0Nωman−m(θ)),

where ϕ is the nonlinear activation function. Given the rotational symmetry from our assumptions, it is enough to solve for an=an(0), which gives us a set of N/2 equations which can then be combined with Equation 45, which gives us the following equation to solve(47)an=ϕ(∑m=0N(∑f=1NFf[a]2‖a‖2cos⁡(2π(n−m)N))an−m)=ϕ(1‖a‖2∑m=0N(∑f=1N[∑k=0Nakcos⁡(2πkfN)]2cos⁡(2π(n−m)N))an−m).

Since an=a−nmodN, we obtain N/2 equations for N/2 values of an.

Note that there is no closed form solution in general, but some generic properties can be inferred. For example, as long as we have a single bump of activity, F1[a]>|Ff[a]|, ∀f>1, therefore F1[ω]>Ff[ω], ∀f>1. More specifically,(48)Ff[ω]=|Ff[a]|2|F1[a]|2F1[ω].

Figure 12 shows the results of the same simulation as section ‘Learning rules and development’, but using neurons with a nonlinear (tanh) activation function, and distorting the network input to be a more square wave-like sinusoid. As predicted theoretically, our rule still reinforces the dominant spatial frequency in the network, causing the weights to converge to the sinusoidal profile our theory predicts.

![Figure 12.](https://cdn.elifesciences.org/articles/91533/elife-91533-fig12-v1.jpg)

**Figure 12.:** The synaptic weights converge to a sinusoidal pattern under Oja’s rule when the neurons have a nonlinear () activation function and a distorted (more square wave-like) sinusoidal input is provided. (tanhA) The weights start at zero and slowly converge to the prescribed sinusoidal profile, showing that this connectivity can emerge from scratch. (B) The sinusoidal weights are perturbed by noise but learning ensures that the weight profile is corrected. (C) The distorted sinusoidal input (orange) compared to a sinusoid profile (blue). Noise was added to the initial activity, weights, and input with the same parameters as in Figure 5, the only difference being that these simulations were run for 2500 periods.
