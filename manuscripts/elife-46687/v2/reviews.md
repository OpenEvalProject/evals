# Peer review - Round 1

Editors:
- Upinder Singh Bhalla, Tata Institute of Fundamental Research India

Reviewers:
- Yi Gu, Princeton University United States

## Review text

DOI: [10.7554/eLife.46687.035](https://doi.org/10.7554/eLife.46687.035)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "A geometric attractor mechanism for self-organization of entorhinal grid modules" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Laura Colgin as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Yi Gu (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This study presents a model for MEC grid module formation emerging from a series of attractor networks (based on the Burak-Fiete model) coupled by excitatory interactions. The coupling causes the length-scales of each network to cluster into discrete bands, reminiscent of experimental modules of increasing scale. The orientation of the networks also cluster, again consistent with experiment. Thus a rather simple addition to the network model architecture brings it into agreement with a large body of experiments.

Essential revisions:

1) The authors must provide more links from model predictions to experiments. The reviewers have made some suggestions both to link the model to existing data, and for new predictions, and the authors could of course come up with further such links.

2) The authors must examine the assumption of precise positional projections between networks. We would prefer to see some test simulations that explore imprecision in this quantity.

3) The authors should address some of the other key parameters of the simulations, particularly the network size, noise, spiking dynamics, and plasticity. The reviewers would prefer to see simulations for at least some of these, though we understand that others may be a substantial effort and the authors can address those in the Discussion.

Reviewer #1:

This study presents a model for MEC grid module formation emerging from a series of attractor networks (based on the Burak-Fiete model) coupled by excitatory interactions. The coupling causes the length-scales of each network to cluster into discrete bands, reminiscent of experimental modules of increasing scale. The orientation of the networks also cluster, again consistent with experiment. Thus a rather simple addition to the network model architecture brings it into agreement with a large body of experiments. Some aspects of these findings have been seen in models proposed by Treves and co-workers, but the authors point out that there are features such as orientation, that only the current model predicts.

1) The model makes several predictions, including the modules, their orientation, firing rate variability. These all emerge from this rather parsimonious elaboration to the attractor network model. This is a strong point of this study.

2) A key requirement for these outcomes is the coupling between networks, which requires a certain precision of connectivity between successive networks. The authors have made predictions for the outcome of lesion experiments, but I would like to ask if there are any more direct projection or connectivity studies that support this proposed circuitry. They mention some studies involving recurrent connectivity among grid cells, but it isn't clear to me that these studies demonstrate the spatial structure that the current model requires.

3) Another possible and testable manipulation would be to make a small focal lesion rather than a sub-network wide one. It would be interesting to see how this affects the z<lesion networks, and this might provide a more stringent and nuanced prediction for experiments.

4) In an ideal world one would like to compare predictions for specific manipulations between the current model and others in the field. I would specifically be interested in seeing if there are manipulations which would strongly contrast the properties of the current model and that of Treves and co-workers.

5) The authors explore a range of simulation parameters, notably coupling strengths and the ratio of inhibition distances. However, they barely touch on spiking dynamics and plasticity in a line in the Discussion. I therefore get a sense that the model has been sensitivity tested only along a very few dimensions. It would be reassuring to see somewhat more exploration of these properties, especially those that relate to more biological realism.

Reviewer #2:

This paper proposed a mechanism for generating discrete grid modules (Stensola et al., 2012) in attractor networks of medial entorhinal cortex (MEC) by combining lateral inhibition within individual "networks" and excitatory interactions between networks. Modulating the balance between the inhibition and excitation led to constant scale ratios and orientation differences between adjacent modules, which were consistent with experimental data. This paper is very well written and this first demonstration of a potential mechanism for generating grid modules in attractor networks of the MEC would be of high interest to neuroscience readers. However, providing additional connections between the proposed theory and experimental observations would make this work more significant.

1) Numbers of neurons in each module: the current theory was developed based on 12 "attractor networks" the MEC. Each network contained 160×160 neurons and these 307,200 grid cells mostly gave three modules. In reality, an animal could have four or five modules (Stensola et al., 2012), so there might be even a larger number of grid cells per animal based on the theory. Given the fact that grid cell population is only ~20% (or even less, ~5% in Miao C et al., Cell, 2017) of the MEC cells, and the relatively low number of grid cells per module recorded by tetrodes and imaging (Stensola et al., 2012; Gu et al., 2018), this theoretical number of grid cell seems unrealistically large. Although it would be hard to know exactly how many grid cells are in real animals, the question is how the conclusions are sensitive to the size of the network. For a network contains half or even a quarter of neurons used here (less number of neurons per network or less number of networks), are these conclusions (the coupled excitation and lateral inhibition generate constant scale ratio and orientation differences between adjacent modules) still true?

2) Neurons coupled by excitation: the theory is developed under the assumption that a neuron at a given position of a ventral network excited the neuron at the same position of a dorsal network (Figure 1D, bidirectionally if in Figure 3C). Thinking about the noise of real network connectivity, how tolerant is this theory to the disruption of this position correspondence of the excitatory connection across networks?

3) Variation of grid field amplitudes: the authors claimed that the excitation from the ventral to dorsal modules could lead to the variation in grid field amplitudes for cells in dorsal modules, as observed experimentally (Ismakov, 2017; Dunn, 2017). However, this statement is rather weak. Based on the theory, for a dorsal grid cell, its fields, which aligned with the fields of a ventral grid cell that excited this dorsal cell, should have higher amplitudes. The amplitude variation of grid fields should have a particular pattern (Figures 2B and 4D). It would be helpful to see more specific explanations for real examples of grid cell activity based on the current theory, i.e. what commensurate or discommensurate lattices could be responsible for generating a given pattern of grid field amplitudes and under what kind of excitation and inhibition.

4) Discommensurate lattices for real grid modules: the author claimed that discommensurate lattice relationships could produce realistic modules (Figure 5). Similar to (3), this statement would be more convincing if the author could give several examples of adjacent modules recorded from the same animal and explain the discommensurate lattices and the detailed parameters of excitation and inhibitions (strength and spread of excitation, and ratio of inhibition distances between modules) that used to form these modules.

5) Independent rescaling of grid modules in different environments: previous work showed that grid scales of different modules could change independently when an environment was deformed (Stensola et al., 2012, Figure 7). However, based the current theory, the scale ratio of adjacent modules seemed to be constant, unless the balance between the excitation and inhibition is changed. How could the current theory explain the independent rescaling of different modules? This question could also be in line with the last sentence in the "Discussion" about border cells and environmental deformation. In general, can the author expand this discussion by speculating the mechanism for the change of grid scales (maybe orientations too) in different modules in different (or deformed) environments and how border cells play roles in this process (i.e. how do border cells interfere with the balance of excitation and inhibition)?

Reviewer #3:

This paper is quite well written and comprehensive. It addresses an important question, namely, what are the mechanisms responsible for the modular organization of grid cells? In doing so it arrives at some general principles of network organization in the MEC. Overall, I think it needs no major changes.

An earlier paper by one of the authors showed that grid cell modules are arranged in a manner that minimizes the number of neurons required to encode location with a given resolution. In this paper, they look at how such a peculiar modular organization emerges in a model attractor network. To construct individual modules the authors used a well-known continuous attractor network by Burak and Fiete. The grid scale is determined by the spatial extent of inhibition in this network. The authors connected a set of 12 such attractor networks with a gradually varying grid scale using excitatory connections across neighboring networks. The observed spatial scale of grid cell receptive fields in each attractor network did not follow the gradual increase that would be the case if they were uncoupled, but clustered into groups, with the scale ratios across groups matching experimental observations.

This paper addresses an important question and does so using an innovative and simple extension of an existing model. The manuscript is clearly written, potential caveats have been addressed, and the figures are detailed (albeit tiny). The authors arrive at an intuitive explanation for the location of fractures where the grid cell receptive fields transition from one scale to the next. Given the complex dynamics of stellate cells and pyramidal cells in layer II, it is quite surprising that the patterns that emerge from this phenomenological model can be quantitatively compared to the results of experiments. What is particularly interesting is that the model is difficult to break, in that different excitatory connectivities (bi-directional and uni-directional in either direction), all seem to generate the same modularity ratios. It seems like the model hints at general principles at work in the MEC that the authors allude to in the Discussion.

The authors mention that at the boundaries an attractor network can be part of one module or the other depending on the initial conditions. Here it would be useful to understand whether a grid-like receptive field persists when temporal noise is added to the system.
