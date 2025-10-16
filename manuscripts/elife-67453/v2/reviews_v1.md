# Peer review - Round 1

Editors:
- Vatsala Thirumalai, National Centre for Biological Sciences India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67453.sa1](https://doi.org/10.7554/eLife.67453.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

As animals mature, their locomotor patterns become varied, more flexible and complex. In this manuscript, Roussel et al., build models of the spinal network in embryonic and larval zebrafish based on experimental data to understand how these animals generate distinct behaviors during development.

Decision letter after peer review:

Thank you for submitting your article "Modelling spinal locomotor circuits for movements in developing zebrafish" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Ronald Calabrese as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Rishikesh Narayanan (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Reviewer #1 (Recommendations for the authors):

For the B panels in figures 2, 3 and 4, are these responses of isolated neurons or neurons in the fully connected network?

Wherever neuron traces are shown, showing rostrocaudal and left-right neuron traces in the same panel makes them too cluttered. In all cases, where the firing starts and stops is difficult to discern. It may suffice to show one rostral and one caudal neuron trace.

Single coiling:

Include sensitivity analysis in graphical form in Figure 2.

SBs are depolarizing and reverse at -40. How critical are they then for preventing simultaneous contralateral coiling? Why an analysis of neuron deletions has not been done?

Was sensitivity different for glycinergic synapses and electrical synapses?

Was bursting in PMs critical for generating single coiling? This can be included in Figure 2. Figure 2 can be improved to test the single coiling model in multiple ways. In its current form, it doesn't provide much data regarding the performance of the model.

Double coiling:

Line 219: what proportion of PMs were electrically coupled to rostral CENs?

The neuron traces are confusing with too many superimposed.

Line 240: Replace 'with' with 'to'.

What accounts for the long delay in firing between PMs and other neurons though they are electrically coupled? These seem much longer than segmental conduction delays. Such long delays seem critical for CENs to initiate the second coil on the contralateral side once the first coil is over. Yet, this seems inexplicable following known monosynaptic/conduction delays. Likewise, in this circuit configuration, what prevents the circuit from going into third or fourth coils? It is not clear which process decays slowly to disallow such multiple coils. Similarly, it is not clear how under conditions of glycinergic blockade in the model, multiple coilings are generated if inhibition is normally over before CENs are even activated.

Figure 3C-E: Why aren't there multiple traces for IEDs?

Figure 3H: Convert to color for better effect.

Beat and glide swimming:

Line 398: Do you mean 'few'?

Line 431: "Silencing…' – this sentence does not make sense.

How is swimming initiated?

Figure 4A: This schematic is too confusing. Do MNs receive only IED inputs? Do they not receive direct inhibition?

Figure 4C, F: Unable to discern any detail of MN activity due to overlap of traces. Show phase relationships between classes of neurons and comment.

Figure 4D: Same as above, cannot see the color coded information clearly as most angles appear red or blue and therefore are at the extremes of their scalebar. Why aren't there any values for body position 1.0 which should be the tail tip?

Figure 5B: Authors state in line 432 that removing CENs does not affect rhythmic firing in IEDs or MNs. When CENs are removed, is there left-right alternation? From the traces shown, there doesn't appear to be and the video shows what appear to be unilateral tail flicks. I couldn't tell for sure as they are at a fast playback speed. If that is the case, authors need to be more convincing of this result in the figure and the video and perhaps include L-R phase relationships to establish that alternation occurs. What do the peaks in Row3 correspond to? Is each cycle a bout? Seems too slow to be a tail beat? Do the dampened oscillations in the middle epoch qualify as bonafide swimming? If yes, what is the justification? Also please explain, 'sum of left and right motoneuron activity was summed'. Why use this parameter as motor output when you have the muscle transform calculated? Why is MN activity shown on a different scale compared to the other rows below?

Figure 7: The importance of bursting IED is not really clarified in this figure. Is there a quantitative difference in durations? Both long and short are produced. Why? Perhaps a phase plane analysis of contribution of IED parameters to durations will help sort out the underlying dynamics? Young prefeeding larvae do exhibit long duration swims, so the conclusion that bursting IEDs are essential for beat and glide swimming appears too strong for the results presented here.

The videos shown for CIN null and strychnine experiments show left-right tail beats while figure panels show different results.

Discussion:

Lines 604-635: Authors discuss differential recruitment of spinal neurons as a function of 'speed'. However, the studies cited looked at the recruitment of neurons as a function of frequency. It has recently become clear that speed can be changed even without changing swim frequency and that MNs are recruited as a function of forward speed and not frequency (Jha and Thirumalai 2020).

Methods:

A more detailed methods section is warranted.

It is not clear what the authors mean by tonic motor command- is it a DC current injection or a regular synaptic input?

Line 705: What is s here?

Line 739: Why is capacitance decreasing with age?

Line 745: How is deflection angle calculated per somite when three somites are collapsed into one muscle?

Line 756: 'muscle output' is vague – do you mean V or theta?

Figure 1D: The transformation from local body angle to an overall body midline position can be better schematized to help the reader.

Figure 1E: More intuitive to have time on x-axis as has been done in Figure 7F. Change elsewhere also.

Reviewer #2 (Recommendations for the authors):

1. The sensitivity analyses involving variability in individual parameters is useful. But, it is not clear from the description (starting line 721) on what specific parameters are governed by \σ_p, \σ_w and \σ_d. Importantly, these sensitivity analyses do not seem to cover cell-to-cell variability in Izhikevich model parameters (spanning a, b, c, d, k, C, V_r, V_t; it is not clear if \σ_p alters any of these parameters?). Specifically, all neurons of the same subtype seem to have the same model parameters. While the firing dynamics of Izhikevich model neuron are critically dependent on the model parameters, there are a range of model parameters (perturbations around the employed values) over which similar firing patterns could be achieved. How sensitive are the conclusions presented here to such variability across neurons of the same subtype in the network (with the variability reflecting electrophysiological recordings from larval neurons)?

What would be the impact of heterogeneities in gap junction connectivity? From the description provided, it seems like the model assumes identical weights for gap junction connectivity. How sensitive would the conclusions presented here to adding variability to gap junctional weights?

Additional sensitivity analyses could focus on the numbers of neurons per chain, number of connections within and across chains and glycinergic synaptic connectivity (there seem to be several unsubstantiated assumptions on these connections; e.g. paragraph spanning lines 126-137).

Apart from these, any parameter that has been fixed to be homogeneous should also be considered in addressing the question on whether the results observed are because of the homogeneous nature of that parameter in the simulations. The authors could consider incorporating some of these simulations involving networks with parametric variability, and mention the others in the discussion.

2. All interpretations of the authors from experimental data are based on the summary statistics, and do not account for heterogeneities across different larvae. For instance, the authors cite experimental data that adding CNQX and APV to block glutamatergic transmission precluded double coils while sparing single coils, and that blocking glycinergic synapses led to triple or even quadruple coils. They use these conclusions to drive their modeling outcomes. However, are the impacts of CNQX or APV or blockade of glycinergic synapses the same across all larvae? Do all larvae behave identically when treated with these pharmacological agents? If not, how do the authors account for these heterogeneities across larvae.

Employing summary statistics to define models or assess outcomes is perilous, and the authors should account for heterogeneities in experimental outcomes to define their models (Marder and Taylor, Nature Neuroscience, 2011). Heterogeneities and variability should be accounted for each measurement at each scale in interpreting modeling and experimental outcomes -- the CNQX/APV/Glycinergic synaptic blockers is just one instance. The ideal way to do this is to generate a population of heterogeneous models and derive conclusions from there (Marder and Taylor, Nature Neuroscience, 2011). I recommend that the authors mention this a future direction, refine their interpretations in the Discussion section accounting for heterogeneities across larvae and present the caveats of using summary statistics to drive experimental/model interpretations.

3. Are there several routes (in terms of neuronal intrinsic properties, neuronal firing patterns, network connectivity, electrical/chemical synapse weights, neuromodulatory tones, etc.) to achieving single coiling or double coiling or other locomotor movements? Or, is there a unique route to achieve these across larvae? Could the authors comment on potential degeneracy across scales in achieving the same behavioral outcomes (see Vogelstein et al., Science, 2014; Edelman and Gally, PNAS, 2001)? How would such degeneracy alter the conclusions presented here? How would such degeneracy relate to heterogeneities across larvae (Pt. 2 above) and variability in parameters (Pt. 1 above)? The authors should provide detailed discussion on these questions. They have considered single hand-tuned models across different developmental stages to make their points and demonstrate behavioral outcomes. But, it is important to ask if this is the only route to achieve these behavioral outcomes, and if zebrafish and their larvae might be using different structural combinations to elicit same functional outcomes?

While the authors have talk about potential ion-channel degeneracy in the discussion, they should also comment on circuit level degeneracy involving different neuronal subtypes and disparate synaptic components (in terms of neuronal intrinsic properties, neuronal firing patterns, network connectivity, electrical/chemical synapse weights, neuromodulatory tones, etc. e.g. Prinz et al., Nat Neuroscience, 2004). The authors could mention in the Discussion section about the possibility of using an unbiased stochastic search involving all parameters to assess such potential degeneracy involving intrinsic properties and synaptic connectivity across all stages of the developing fish. The authors could also mention in the discussion the disadvantages of using a single hand-tuned model and in deriving all interpretations from that single model (Marder and Taylor, Nat Neuroscience., 2011).

4. Please add a separate Discussion section on testable predictions that emerge from the model presented here, which provide clear pointers that would test the overall hypothesis.

Reviewer #3 (Recommendations for the authors):

Strengths and weaknesses

The key strength of this manuscript is the detailing of a set of related models detailing the motor output of the larval zebrafish across key stages of development. The models should form a basis for future research. It also a first of its kind – I don't know of similar models focusing on development of locomotor function. The main weakness is the reliance on assumptions of model connectivity. But I suggest that if the model is treated as a basis for the community to refine and validate it will be incredibly useful.
