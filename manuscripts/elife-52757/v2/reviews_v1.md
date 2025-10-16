# Peer review - Round 1

Editors:
- Stephanie Palmer, University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.52757.sa1](https://doi.org/10.7554/eLife.52757.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

New imaging and genetic techniques have created an opportunity to peer inside the brain's "black box". At the same time, current theory work in neuroscience has suggested that the brain operates in a particular dynamical regime that supports flexible and reliable computation. This manuscript suggests new experimental protocols that connect these tools with these theories to probe the hidden processing dynamics at play in the vertebrate brain. It is a thorough and detailed modeling study that will have a broad impact on how new experiments are planned and interpreted.

Decision letter after peer review:

Thank you for submitting your article "Patterned perturbation of inhibition is necessary to detect feature-specific inhibitory stabilization" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper addresses how perturbation of neuronal activity can act as a probe to identify the dynamic properties of neuronal networks. The work focuses on "inhibition-stabilized networks (ISNs)" in which strong recurrent inhibition is required to stabilize strong recurrent excitation, and increased input to inhibitory neurons decrease both excitatory and inhibitory activities, called "the paradoxical effect." This manuscript investigates the response of inhibitory stabilized networks (ISNs) to "non-specific" and "patterned" perturbations of inhibitory cells in ISNs with feature-specific and non-specific connectivity rules. It aims to make explicit, experimentally testable predictions about such ISNs. The authors methodically demonstrate how such networks behave depending on the specificity of both the connections and perturbations to the network. Namely, they predict that inhibitory neurons will decrease their activity in response to patterned stimulation of inhibitory neurons when that perturbation aligns with neuronal receptive fields. They also show that ISNs with specific kinds of connectivity transition rapidly between different selectivity states. In general, the work is important and would potentially be of broad interest to both experimental and theoretically-minded readers.

Essential revisions, primarily computational:

While the theoretical investigation of the properties of ISNs that can guide the design of perturbation experiments is exciting and timely, the authors made several simplifying assumptions of network architectures and dynamics. Thus, the validity of the main results must be checked in more general and more biologically relevant settings:

1) Tuning widths, population sizes, connectivity: Request for more simulations:

As outlined above, this paper is attempting to make very clear connections to feasible experiments, which is fantastic to see. But, in general, we feel that the experiments reported in the manuscript build on top of each other before sufficiently establishing the generality and validity of the basic findings, and as a result, the same set of questionable model-assumptions are used throughout the paper. Specifically, equal numbers of excitatory and inhibitory cells with similar tuning properties are used in all simulations, but (1) It is known that there are fewer inhibitory neurons than excitatory neurons in real neural networks, (2) There are numerous papers that suggest, instead, broad tuning of inhibitory neurons. We would like to be convinced that the main conclusions will be supported by experiments using networks with biologically realistic architectures. Before exploring things like spiking networks, the authors should present results on more realistic inhibitory motifs with fewer inhibitory cells and broader inhibitory tuning.

The authors considered EI connectivity where all synaptic connectivity has the same tuning width. This seems too stringent as balanced states and ISN dynamics can be achieved with different spatial profiles of E and I connections. In that case, the relationship between the specific activity eigenmodes and connectivity or response similarity is less clear. Also, as pointed out in Figure 6—figure supplement 1B, the dynamic properties of ISNs are changed when E and I connectivities have different tuning widths.

2) Expanding to non-linear dynamics:

The main conclusion was derived mostly in the linear dynamics – the authors considered only a threshold-nonlinearity in the rate models and similarly in spiking networks as the f-I curve in I&F neurons is quite linear. Nonlinearities create interactions amongst the eigenmodes and may mitigate the "specific paradoxical effects." Also, in recently proposed networks with a supralinear transfer function, the dynamic range is divided into non-ISN and ISN regions by a "breakpoint" (Rubin et al., 2015). More simulations are needed to address how nonlinear dynamics might affect the conclusions of this work.

3) Exploration of stimuli that are the best perturbative probes of dynamics

The authors explore whether it is possible to design patterned perturbations based on stimulus response (a great thing to do!) and they report that some stimuli are not ideal for such experiments. Why not explore this further? If the goal is to make explicit experimental predictions, the authors should do a more detailed analysis of which stimuli would uncover the pattern of optical perturbation needed, and make that very clear to the reader.

Essential revisions, primarily textual:

1) Clarity of goals:

What are the actual goals of this paper? The way it is written, the central goal is to determine how optogenetic experiments could "reveal" specific ISNs (which is a slightly unclear goal in and of itself). But, then, what is the purpose of the final findings on transitions in selectivity states? On discussion does it become clear that the point of this paper is to more broadly determine what experiments could be done to test for the presence of ISNs with connection specificity in the brain. Both the perturbation results and the state transition results are effectively providing an experimental signature of such networks. But, this is not very clear as it stands. Moreover, once one realizes that the goal is to guide experiments (which is a great goal!), a host of other issues become apparent, as discussed in the following points.

2) Clarity for experimentalists:

Overall, we suspect that the paper would not be very easy to follow for an experimental neuroscientist. There is a great deal of jargon used throughout the paper, starting with the use of the term ISN in the fourth paragraph of the Introduction, without defining it for the reader. Other examples are references to eigenmode, selectivity state transitions, etc. This is all fine for computational readers, but given the goals of this paper, it would need a significant re-write to be interpretable for experimentalists. More broadly, the manuscript's clarity could be greatly enhanced, even for computational readers. For example, the authors write, "While uniform or non-specific perturbation was enough to reveal uniform ISNs, patterned perturbation as described above is necessary to reveal specific ISNs." What is meant by "reveal uniform/specific ISNs"? Do you mean "distinguish a specific ISN from a non-specific ISN"? Or something else? Throughout the paper, the language is confusing at times.

3) Additional Discussion sections:

Please discuss past ideas about 'detailed balance', i.e. Hennequin Vogels Gerstner 2012, Hennequin et al., 2014, Hennequin et al., 2017, and the inhibitory plasticity mechanism in Vogels et al., 2011.

Also, recent theoretical work suggested cortical circuits exhibit paradoxical effects because of disinhibitory loops rather than inhibition-stabilization mechanisms (Mahrach et al., BioRxiv 2019). This questions whether perturbations can reveal the dynamic properties in these complex, yet more biologically plausible networks. Please discuss the perturbation methods that can differentiate two prominent types of paradoxical effect mechanisms: disinhibitory loops vs. ISNs, and under which conditions similar conclusions as detailed in this paper can be derived.
