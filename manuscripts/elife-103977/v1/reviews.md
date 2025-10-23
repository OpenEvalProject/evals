# Peer review - Round 1

Editors:
- Paschalis Kratsios, University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.103977.3.sa0](https://doi.org/10.7554/eLife.103977.3.sa0)

NeuroSC is an accessible and interactive tool for streamlined observation of neuronal morphology, membrane contact, and synaptic connectivity across developmental stages in the nematode C. elegans. This important tool relies on solid electron microscopy datasets. This resource will be of high interest to C. elegans researchers interested in nervous system wiring and circuit function.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.103977.3.sa1](https://doi.org/10.7554/eLife.103977.3.sa1)

The authors have done a terrific job and addressed the questions raised in my previous review. There are only some minor requests that I have and list below.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.103977.3.sa2](https://doi.org/10.7554/eLife.103977.3.sa2)

Summary

The past several years has seen publication of both new (Witvliet et al., 2021) and newly analyzed (Cook et al., 2019; Moyle et al., 2021; Brittin et al., 2021) data for the C. elegans connectome. The increase in data availability for a single species allows researchers to examine variability due to both stochastic events and due to changes over development. The quantity of these data are huge. To help the community make these data more accessible, the authors present a new online tool that allows examination of 3D models for C. elegans neurons in the central neuropil across development. In addition to visualizing the overall structure of the neuronal processes and locations of synapses, the NeuroSC tool also allows users to probe into the C-PHATE visualization results, which this group previously pioneered to describe similarities in neuron adjacency (Moyle et al., 2021).

Strengths

The ability to visualize the data from both a connectomics and contactomics perspective across developmental time has significant power. The original C. elegans connectome (White et al., 1986) presented their circuits as line drawings with chemical and electrical synapses indicated through arrows and bars. While these line drawings are incredibly useful, they were necessary simplifications for a 2D publication and lack details of the complex architecture seen within each EM image. Koonce et al takes advantage of their own and others segmented image data of each neuronal process within the nerve ring to create a web interface where users can visualize 3D models for their neuron of choice. The C-PHATE visualization is intended to allow users to explore similarities among different neurons in terms of adjacency and then go directly to the 3D model for these neurons. The 3-D models it generates are beautiful and will likely be showing up in many future presentations and publications. The tool doesn't require any additional downloading and is open source. This revision includes an option where hovering over an individual neurons, synapse, or contact will pull up a statistics panel. The addition of text to the video tutorials in the revision is very useful.

Weaknesses

There are several bugs with this tool, which make it a bit clunky to use and suggest a lack of rigorous testing. There are also issues with data availability. I was disappointed that my "recommendations for the authors", which focused on the user interface, were not addressed in the response to reviewers.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.103977.3.sa3](https://doi.org/10.7554/eLife.103977.3.sa3)

Summary:

This work provides graphical tools for reconstructing the detailed anatomy of a nervous system from a series of sections imaged by electron microscopy. Contact between neuronal processes can direct outgrowth and is necessary for connectivity, thus function. A bioinformatic approach is used to group neurons according to shared features (e.g., contact, synapses) in a hierarchy of "relatedness" that can be interrogated at each step. In this work, Koonze et al analyze vEM data sets for the C. elegans nerve ring (NR), a dense fascicle of processes from181 neurons. In a bioinformatic approach, the clustering algorithm Diffusion Condensation (DC) groups neurons according to similar cell biological features in iterations that remove chunks of differences in feature data with each step ultimately merging all NR neurons in one cluster. DC results are displayed with C-Phate a 3D visualization tool to produce a trajectory that can be interrogated for cell identities and other features at each iterative step. In previous work by these authors, this approach was utilized to identify subgroups of neuronal processes or "strata" in the NR that can be grouped by physical contact and connectivity. Here they expand their analysis to include a series of available vEM data sets across C. elegans larval development. This approach suggests that strata initially established during embryonic development are largely preserved in the adult. Importantly, exceptions involving stage specific-specific reorganization of neuronal placement in specific strata were also detected. A case study featured in the paper demonstrates the utility of this approach for visualizing the integration of newly generated neurons into the existing NR anatomy. Visualization tools used in this work are publicly available at NeuroSCAN.

Strengths:

A web-based app, NeuroSCAN, that individual researchers can use to interrogate the structure and organization of the C. elegans nerve ring across development.

Weaknesses:

minor revisions

Comments on Revisions:

The authors have satisfactorily addressed my critiques.
