# Peer review - Round 1

Editors:
- Julijana Gjorgjieva, Technical University of Munich Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.96303.3.sa0](https://doi.org/10.7554/eLife.96303.3.sa0)

This important study introduces a biologically constrained model of telencephalic area of adult zebrafish to highlight the significance of precisely balanced memory networks in olfactory processing. The authors provide compelling evidence that their model performs better in multiple situations (for e.g. in terms of network stability and shaping the geometry of representations), compared to traditional attractor networks and persistent activity. The work supports recent studies reporting functional E/I subnetworks in several sensory cortexes, and will be of interest to both theoretical and experimental neuroscientists studying network dynamics based on structured excitatory and inhibitory interactions.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.96303.3.sa1](https://doi.org/10.7554/eLife.96303.3.sa1)

Summary:

Meissner-Bernard et al present a biologically constrained model of telencephalic area of adult zebrafish, a homologous area to the piriform cortex, and argue for the role of precisely balanced memory networks in olfactory processing.

This is interesting as it can add to recent evidence on the presence of functional subnetworks in multiple sensory cortices. It is also important in deviating from traditional accounts of memory systems as attractor networks. Evidence for attractor networks has been found in some systems, like in the head direction circuits in the flies. However, the presence of attractor dynamics in other modalities, like sensory systems, and their role in computation has been more contentious. This work contributes to this active line of research in experimental and computational neuroscience by suggesting that, rather than being represented in attractor networks and persistent activity, olfactory memories might be coded by balanced excitation-inhibitory subnetworks.

Strengths:

The main strength of the work is in: (1) direct link to biological parameters and measurements, (2) good controls and quantification of the results, and (3) comparison across multiple models.

(1) The authors have done a good job of gathering the current experimental information to inform a biological-constrained spiking model of the telencephalic area of adult zebrafish. The results are compared to previous experimental measurements to choose the right regimes of operation.

(2) Multiple quantification metrics and controls are used to support the main conclusions, and to ensure that the key parameters are controlled for - e.g. when comparing across multiple models.

(3) Four specific models (random, scaled I / attractor, and two variant of specific E-I networks - tuned I and tuned E+I) are compared with different metrics, helping to pinpoint which features emerge in which model.

In the revised manuscript, the authors have also:

(a) made a good effort to provide a mechanistic explanation of their results (especially on the mechanism underlying medium amplification in specific E/I network models);

(b) performed a systematic analysis of the parameter space by changing different parameters of E and I neurons (specifically showing that different time constants of E and I neurons do not change the results and therefore the main effects result from connectivity);

(c) added further analysis and discussion on the potential functional and computational significance of balanced specific E-I subnetworks.

These additions substantially strengthen the study, presenting compelling evidence for how networks with specific E-I structure can underpin olfactory processing and memory representations. The findings have potential implications that extend beyond the olfactory system and may be applicable to other neural systems and species.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.96303.3.sa2](https://doi.org/10.7554/eLife.96303.3.sa2)

Summary:

The authors conducted a comparative analysis of four networks, varying in the presence of excitatory assemblies and the architecture of inhibitory cell assembly connectivity. They found that co-tuned E-I assemblies provide network stability and a continuous representation of input patterns (on locally constrained manifolds), contrasting with networks with global inhibition that result in attractor networks.

Strengths:

The findings presented in this paper are very interesting and cutting-edge. The manuscript effectively conveys the message and presents a creative way to represent high-dimensional inputs and network responses. Particularly, the result regarding the projection of input patterns onto local manifolds and continuous representation of input/memory is very Intriguing and novel. Both computational and experimental neuroscientists would find value in reading the paper.

Weaknesses:

Intuitively, classification (decodability) in discrete attractor networks is much better than in networks with continuous representations. This could also be shown in Figure 5B, along with the performance of the random and tuned E-I networks. The latter networks have the advantage of providing network stability compared to the Scaled I network, but at the cost of reduced network salience and, therefore, reduced input decodability. Thus, tuned E-I networks cannot always perform better than any other network.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.96303.3.sa3](https://doi.org/10.7554/eLife.96303.3.sa3)

Summary:

This work investigates computational consequences of assemblies containing both excitatory and inhibitory neurons (E/I assembly) in a model with parameters constrained by experimental data from the telencephalic area Dp of zebrafish. The authors show how this precise E/I balance shapes the geometry of neuronal dynamics in comparison to unstructured networks and networks with more global inhibitory balance. Specifically, E/I assemblies lead to the activity being locally restricted onto manifolds - a dynamical structure in-between high-dimensional representations in unstructured networks and discrete attractors in networks with global inhibitory balance. Furthermore, E/I assemblies lead to smoother representations of mixtures of stimuli while those stimuli can still be reliably classified, and allows for more robust learning of additional stimuli.

Strengths:

Since experimental studies do suggest that E/I balance is very precise and E/I assemblies exist, it is important to study the consequences of those connectivity structures on network dynamics. The authors convincingly show that E/I assemblies lead to different geometries of stimulus representation compared to unstructured networks and networks with global inhibition. This finding might open the door for future studies for exploring the functional advantage of these locally defined manifolds, and how other network properties allow to shape those manifolds.

The authors also make sure that their spiking model is well-constrained by experimental data from the zebrafish pDp. Both, spontaneous and odor stimulus triggered spiking activity is within the range of experimental measurements. But the model is also general enough to be potentially applied to findings in other animal models and brain regions.

Weaknesses:

All my previous points have been addressed.
