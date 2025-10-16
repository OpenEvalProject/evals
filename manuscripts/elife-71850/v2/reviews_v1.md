# Peer review - Round 1

Editors:
- Neil Burgess, https://ror.org/02jx3x895 University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71850.sa0](https://doi.org/10.7554/eLife.71850.sa0)

This manuscript will be of interest to theoretical neuroscientists broadly defined and potentially also to experimentalists investigating the hippocampus. A biologically plausible spiking neural network model of subregion CA3 of the hippocampus is proposed and studied in order to pinpoint the mechanistic sources of sharp wave ripples and replay observed in vivo.


---

# Peer review - Round 1

Editors:
- Neil Burgess, https://ror.org/02jx3x895 University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71850.sa1](https://doi.org/10.7554/eLife.71850.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Hippocampal sharp wave-ripples and the associated sequence replay emerge from structured synaptic interactions in a network model of area CA3" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Laura Colgin as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Daniel McNamee (Reviewer #1); Bruce Graham (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers agree that this manuscript is worthy of acceptance, but that the authors should be encouraged to further clarify or explain the mechanisms causing ripples and replay, as detailed in their responses below. The main broad issues for consideration are: (1) What causes forward versus backwards replay; (2) The necessity or otherwise for the recurrent connectivity created by the specific STDP rule used in generating replay; (3) The necessity of adaptation in causing replay, when cells might fire only once per event; (4) Whether the contribution of an extra inhibitory neuronal cell type might produce a more accurate model of the duration of SWRs; (5) Whether any explicit experimental predictions can be made.

Reviewer #1 (Recommendations for the authors):

Thank you for the well-written manuscript and also for providing your source code. I had a few queries and suggestions that I hope may be helpful.

1. What is the functional role of the non-spatial PCs?

2. It seems that the heavy-tailed step size distribution of Pfeiffer and Foster is replicated (line 160). Can the gaussian step size distribution of diffusive reactivations be induced? (observed during rest, see Stella et al., Neuron, 2019). Furthermore, beyond the bidrectionality of replay, recent experiments have demonstrated that sequential hippocampal reactivations make take on even more exotic forms such as generative cycling (Kay et al., Cell, 2020). It would be interesting to speculate how such flexible dynamism may emerge in this circuit model e.g. based on entorhinal input.

3: it seems (line 538) that the exploring rodents moved at a constant velocity. If this interpretation is correct, Im wondering if the replay phenomenology is robust to heterogeneous velocities during naturalistic movement (e.g. stop/starts)?

4: Can the model be successfully deployed in an open box environment?

Reviewer #2 (Recommendations for the authors):

Below is a list of questions and comments in ascending order with respect to the line number. I have marked some with an 'S' to highlight that I find them pretty significant. Some of these points are already made in the Public Review and I allow myself to repeat them here so that they are easier to understand. Apologies if this unduly increases the length of the review.

l. 95- 96: Could the authors highlight the main characteristics of the connection probabilites in their model? What are their typical numerical values? They are given in Methods, but I think it is nicer to have an idea about them without having to go consult that section.

(S) Figure 1: How important is it that the STDP kernel is temporally broad (broader than the timescale of a ripple oscillation)?

l. 110: To which figures does the reference refer to? To Figure 1A or its Supplement? Or is Methods and Figure 1A simultaneously referenced? Then, 'Methods and Figure 1A' would be more appropriate. Please clarify.

l. 130: Chenkov et al., also use a symmetric learning rule (see their Figure 8) supporting reverse replay, so this part of the manuscript is not novel. The authors should rephrase this part to clarify the point.

After l. 134: it should be made clearer what the 'spatially and temporally unstructured' external inputs to the network are, and which cells (all? only a fraction?) are receiving them.

l. 172: At least in CA1, PVBCs fire at the ripple frequency of 200 Hz, see e.g. Ylinen et al., 1995. Is this comparatively low inhibitory population firing rate important for the model?

l. 178: Are the weights scaled after the initial learning phase, or before? Please clarify this.

l. 192: The reference should be to Supplementary Figure 3 since there are no spectral measures shown in Supplementary Figure 1.

(S) l. 195: The main result of Stark et al., 2014 is that interactions between PCs and PVBCs underlie ripple oscillations, and that both cell types are needed for ripples. So citing this reference when saying that ripples start from the PVBC population and then propagate to the pyramidal cells does not seem to be right.

Figure 3B bottom plot: To which scaling factor does 100% LFP power correspond to?

l. 222: Did Theodoni et al., show that one needs a symmetric STDP kernel to generate both forward and reverse replay? If so, it would be good to state this explicitly.

l. 238 ff. Is it important that a 97-3 split is done on the weight matrix? What would happen if, for example, a 50-50 split was done? The choice for the split seems arbitrary and should be better justified.

(S) l. 251: This reads as if the PC-PC coupling structure 'does everything', i.e. it generates replay but also ripple oscillations. This raises the interesting question whether ripples could in principle also be observed in unstructured networks. Could the authors comment on this (for example, by showing a PC spike raster for Figure 6F, where ripple oscillations seem to be present for large PC weight multipliers)?

(S) l. 258 ff. There seems to be a dichotomy revealed by the model: the PC-PC connections are crucial, but the ripple oscillation is generated by PVBCs and is only present in the LFP, but not in the PC firing activity- although the model was designed to show ripple oscillations in the PC activity (Equation 9). Is there an easy intuitive reason for why this is the case?

Figure 7B: It is confusing that the PCs with the highest indices in the rasterplot have the same color (orange) as the BCs in the scheme on top of the figure. Similarly at the top of Figure 2.

(S) l. 295: Similarly to comment about l. 195, Stark et al., 2014 seem to be cited incorrectly: in that study, driving PVBCs did not result in ripple frequency oscillations in the LFP, see their Figure 5. E and F and 6.

l. 321-322: This reads like an addition, while it is a summary of the paragraph above. Please consider re-writing to reflect this.

(S) l. 262: The spike-triggered adaptation must be quite strong because a single PC spikes only once or twice during a given ripple, so the adaptation variable gets only one kick and then decays. This means that either the adaptation starts already at quite a high value or the kick size is large, because otherwise there would be no effect on the membrane voltage. Could the authors comment on this?

l. 347- 348: What is a stochastically initiated buildup period? Was it described before?

l. 365: Given that after learning, the distribution of the PC-PC synaptic strengths is also long-tailed, it might well be that the effective connectivity is lower than 10% because only strongly connected cells fire and the rest stays silent. Is this plausible?

l. 422: Maybe the authors would find the study 'Generation of Sharp Wave-Ripple Events by Disinhibition' (Evangelista et al., J Neurosci 2020) interesting. This study contains a mechanism for the generation of SPW/R events by disinhibition of PCs by a third inhibitory cell population. Here, short-term depression acts on the connection between PVBCs and the third cell population.

Table 3: The decay time constant for PC-PC synapses is large (more than 5 ms). Is this a realistic value for AMPAergic synapses?

(S) l. 604/ 620 (and also the section beginning on l. 291): The network was optimized to generate strong ripple-frequency oscillations in both the PC and PVBC population (Equation 9). In Figure 1D, however, it looks as if there was no ripple oscillation in the PC rate, but only in the LFP. Could the authors please clarify this? It would be nice to see a magnification of the spike rasterplot at the top of Figure 1D. I also wonder whether there could be a ripple oscillation present in the spiking activity of PCs shown in Figure 8C. It isn't present in the LFP as shown in Figure 8D, but since the network was optimized to display ripple oscillations in the PC activity (Equation 9) and since there still is bi-directional replay in the model, it might well be that there are still ripple oscillations in the PC population activity, as shown in Figure 3—figure supplement 1 for a different setup. It is also not defined how the population rates for PCs and PVBCs are calculated, but the temporal resolution (for example in Figure 1D middle plot) looks rather low and this might mask fast oscillations. Could the authors comment on this?

Figure 2, supplement 2: it looks like some fraction of PC and PVBCs is bursting (very small ISIs). Are they important for the network dynamics? Is the adaptation maybe only effective in the bursting PCs? This might be important to gain a better mechanistic understanding of the model.

Reviewer #3 (Recommendations for the authors):

The authors are careful to consider some of the limitations of their simple model. However, their study would certainly be strengthened if some of these and other questions could be addressed. Specific consideration should be given to the following:

Spike adaptation alone does not result in a match to the experimentally-recorded durations of SWRs, as the authors acknowledge. It would be good at least to see results from the simulations that have been tried using an extra inhibitory neuron type to try to address this mismatch; and other mechanisms also could be explored here.

What specific spatio-temporal characteristics of spike activity trigger a sequence replay? For example, how sensitive is this to the number of closely associated place cells that spike contemporaneously and does it require some sequencing in this spiking? Is it such initial sequencing that determines whether forward or backward replay occurs?

As discussed, there are biases towards forward or backward replay in different animal situations. How can such biases arise in this model? The "cued" replay results (Figure 2C) demonstrate the obvious of forward replay if the cue is at the track beginning, with backward replay if the cue is at the end of the track, but how in general may such "beginnings" and "ends" be defined in terms of place cells? The strict beginning and end here is somewhat artificial. How can a bias for forwards or backwards replay be introduced at intermediate points along the track? Insights into the characteristics of spike activity triggering replay, as asked for above, should help answer this.

Why do we not see simultaneous forward and backward replay from a single trigger point?
