# Peer review - Round 1

Editors:
- Lisa M Giocomo, https://ror.org/0232r4451 Stanford School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.89851.3.sa0](https://doi.org/10.7554/eLife.89851.3.sa0)

In this valuable study, the authors use a computational model to investigate how recurrent connections influence the firing patterns of grid cells, which are thought to play a role in encoding an animal's position in space. The work suggests that a one-dimensional network architecture may be sufficient to generate the hexagonal firing patterns of grid cells, a possible alternative to attractor models based on recurrent connectivity between grid cells. However, the support for this proposal was incomplete, as some conclusions for how well the model dynamics are necessary to generate features of grid cell organization were not well supported.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.89851.3.sa1](https://doi.org/10.7554/eLife.89851.3.sa1)

I'll begin by summarizing what I understand from the results presented, and where relevant how my understanding seems to differ from the authors' claims. I'll then make specific comments with respect to points raised in my previous review (below), using the same numbering. Because this is a revision I'll try to restrict comments here to the changes made, which provide some clarification, but leave many issues incompletely addressed.

As I understand it the main new result here is that certain recurrent network architectures promote emergence of coordinated grid firing patterns in a model previously introduced by Kropff and Treves (Hippocampus, 2008). The previous work very nicely showed that single neurons that receive stable spatial input could 'learn' to generate grid representations by combining a plasticity rule with firing rate adaptation. The previous study also showed that when multiple neurons were synaptically connected their grid representations could develop a shared orientation, although with the recurrent connectivity previously used this substantially reduced the grid scores of many of the neurons. The advance here is to show that if the initial recurrent connectivity is consistent with that of a line attractor then the network does a much better job of establishing grid firing patterns with shared orientation.

Beyond this point, things become potentially confusing. As I understand it now, the important influence of the recurrent dynamics is in establishing the shared orientation and not in its online generation. This is clear from Figure S3, but not from an initial read of the abstract or main text. This result is consistent with Kropff and Treves' initial suggestion that 'a strong collateral connection... from neuron A to neuron B... favors the two neurons to have close-by fields... Summing all possible contributions would result in a field for neuron B that is a ring around the field of neuron A.' This should be the case for the recurrent connections now considered, but the evidence provided doesn't convincingly show that attractor dynamics of the circuit are a necessary condition for this to arise. My general suggestion for the authors is to remove these kind of claims and to keep their interpretations more closely aligned with what the results show.

Major (numbered according to previous review)

(1) Does the network maintain attractor dynamics after training? Results now show that 'in a trained network without feedforward Hebbian learning the removal of recurrent collaterals results in a slight increase in gridness and spacing'. This clearly implies that the recurrent collaterals are not required for online generation of the grid patterns. This point needs to be abundantly clear in the abstract and main text so the reader can appreciate that the recurrent dynamics are important specifically during learning.

(2) Additional controls for Figure 2 to test that it is connectivity rather than attractor dynamics (e.g. drawing weights from Gaussian or exponential distributions). The authors provide one additional control based on shuffling weights. However, this is far from exhaustive and it seems difficult on this basis to conclude that it is specifically the attractor dynamics that drive the emergence of coordinated grid firing.

(3) What happens if recurrent connections are turned off? The new data clearly show that the recurrent connections are not required for online grid firing, but this is not clear from the abstract and is hard to appreciate from the main text.

(4) This is addressed, although the legend to Fig. S2D could provide an explanation / definition for the y-axis values.

(5) Given the 2D structure of the network input it perhaps isn't surprising that the network generates 2D representations and this may have little to do with its 1D connectivity. The finding that the networks maintain coordinated grids when recurrent connections are switched off supports my initial concern and the authors explanation, to me at least, remain confusing. I think it would be helpful to consider that the connectivity is specifically important for establishing the coordinated grid firing, but that the online network does not require attractor dynamics to generate coordinated grid firing.

(6) Clarity of the introduction. This is somewhat clearer, but I wonder if it would be hard for someone not familiar with the literature to accurately appreciate the key points.

(7) Remapping. I'm not sure why this is ill posed. It seems the proposed model can not account for remapping results (e.g. Fyhn et al. 2007). Perhaps the authors could just clearly state this as a limitation of the model (or show that it can do this).

Previous review:

This study investigates the impact of recurrent connections on grid fields generated in networks trained by adjusting the strength of feedforward spatial inputs. The main result is that if the recurrent connections in the network are given a 1D continuous attractor architecture, then aligned grid firing patterns emerge in the network following training. Detailed analyses of the low dimensional dynamics of the resulting networks are then presented. The simulations and analyses appear carefully carried out.

The feedforward model investigated by the authors (previously introduced by Kropff & Treves, 2008) is an interesting and important alternative to models that generate grid firing patterns through 2-dimensional continuous attractor network (CAN) dynamics. However, while both classes of model generate grid fields, in making comparisons the manuscript is insufficiently clear about their differences. In particular, in the CAN models grid firing is a direct result of their 2-D architecture, either a torus structure with a single activity bump (e.g. Guanella et al. 2007, Pastoll et al. 2013), or sheet with multiple local activity bumps (Fuhs & Touretzky, Burak & Fiete, 2009). In these models, spatial input can anchor the grid representations but is not necessary for grid firing. By contrast, in the feedforward models neurons transform existing spatial inputs into a grid representation. Thus, the two classes of model implement different computations; CANs path integrate, while the feedforward models transform spatial representations. A demonstration that a 1D CAN generates coordinated 2D grid fields would be surprising and important, but its less clear why coordination between grids generated by the feedforward mechanism would be surprising. As written, it's unclear which of these claims the study is trying to make. If the former, then the conclusion doesn't appear well supported by the data as presented, if the latter then the results are perhaps not so unexpected, and the imposed attractor dynamics may still not be relevant.

Whichever claim is being made, it could be helpful to more carefully evaluate the model dynamics given predictions expected for the different classes of model. Key questions that are not answered by the manuscript include:

- At what point is the 1D attractor architecture playing a role in the models presented here? Is it important specifically for training or is it also contributing to computation in the fully trained network?

- Is an attractor architecture required at all for emergence of population alignment and gridness? Key controls missing from Figure 2 include training on networks with other architectures. For example, one might consider various architectures with randomly structured connectivity (e.g. drawing weights from exponential or Gaussian distributions).

- In the trained models do the recurrent connections substantially influence activity in the test conditions? Or after training are the 1D dynamics drowned out by feedforward inputs?

- What is the low dimensional structure of the input to the network? Can the apparent discrepancy between dimensionality of architecture and representation be resolved by considering structure of the inputs, e.g. if the input is a 2 dimensional representation of location then is it surprising that the output is too?

- What happens to representations in the trained networks presented when place cells remap? Is the 1D manifold maintained as expected for CAN models, or does it reorganise?


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.89851.3.sa2](https://doi.org/10.7554/eLife.89851.3.sa2)

Summary:

The paper proposes an alternative to the attractor hypothesis, as an explanation for the fact that grid cell population activity patterns (within a module) span a toroidal manifold. The proposal is based on a class of models that were extensively studied in the past, in which grid cells are driven by synaptic inputs from place cells in the hippocampus. The synapses are updated according to a Hebbian plasticity rule. Combined with an adaptation mechanism, this leads to patterning of the inputs from place cells to grid cells such that the spatial activity patterns are organized as an array of localized firing fields with hexagonal order. I refer to these models below as feedforward models.

It has already been shown by Si, Kropff, and Treves in 2012 that recurrent connections between grid cells can lead to alignment of their spatial response patterns. This idea was revisited by Urdapilleta, Si, and Treves in 2017. Thus, it should already be clear that in such models, the population activity pattern spans a manifold with toroidal topology. The main new contributions in the present paper are (i) in considering a form of recurrent connectivity that was not directly addressed before. (ii) in applying topological analysis to simulations of the model. (iii) in interpreting the results as a potential explanation for the observations of Gardner et al.

Strengths:

The exploration of learning in a feedforward model, when recurrent connectivity in the grid cell layer is structured in a ring topology, is interesting. The insight that this not only align the grid cells in a common direction but also creates a correspondence between their intrinsic coordinate (in terms of the ring-like recurrent connectivity) and their tuning on the torus is interesting as well, and the paper as a whole may influence future theoretical thinking on the mechanisms giving rise to the properties of grid cells.

Weaknesses:

(1) In Si, Kropff and Treves (2012) recurrent connectivity was dependent on the head direction tuning, in addition to the location on a 2d plane, and therefore involved a ring structure. Urdapilleta, Si, and Treves considered connectivity that depends on the distance on a 2d plane. The novelty here is that the initial connectivity is structured uniquely according to latent coordinates residing on a ring.

(2) The paper refers to the initial connectivity within the grid cell layer as one that produces an attractor. However, it is not shown that this connectivity, on its own, indeed sustains persistent attractor states. Furthermore, it is not clear whether this is even necessary to obtain the results of the model. It seems possible that (possibly weaker) connections with ring topology, that do not produce attractor dynamics but induce correlations between neurons with similar locations on the ring would be sufficient to align the spatial response patterns during the learning of feedforward weights.

(3) Given that all the grid cells are driven by an input from place cells that span a 2d manifold, and that the activity in the grid cell network settles on a steady state which is uniquely determined by the inputs, it is expected that the manifold of activity states in the grid cell layer, corresponding to inputs that locally span a 2d surface, would also locally span a 2d plane. The result is not surprising. My understanding is that this result is derived as a prerequisite for the topological analysis, and it is therefore quite technical.

(4) The modeling is all done in planar 2d environments, where the feedforward learning mechanism promotes the emergence of a hexagonal pattern in the single neuron tuning curve. Under the scenario in which grid cell responses are aligned (i.e. all neurons develop spatial patterns with the same spacing and orientation) it is already quite clear, even without any topological analysis that the emerging topology of the population activity is a torus.

However, the toroidal topology of grid cells in reality has been observed by Gardner et al also in the wagon wheel environment, in sleep, and close to boundaries (whereas here the analysis is restricted to the a sub-region of the environment, far away from the walls). There is substantial evidence based on pairwise correlations that it persists also in various other situations, in which the spatial response pattern is not a hexagonal firing pattern. It is not clear that the mechanism proposed in the present paper would generate toroidal topology of the population activity in more complex environments. In fact, it seems likely that it will not do so, and this is not explored in the manuscript.

(5) Moreover, the recent work of Gardner et al. demonstrated much more than the preservation of the topology in the different environments and in sleep: the toroidal tuning curves of individual neurons remained the same in different environments. Previous works, that analyzed pairwise correlations under hippocampal inactivation and various other manipulations, also pointed towards the same conclusion. Thus, the same population activity patterns are expressed in many different conditions. In the present model, this preservation across environments is not expected. Moreover, the results of Figure 6 suggest that even across distinct rectangular environments, toroidal tuning curves will not be preserved, because there are multiple possible arrangements of the phases on the torus which emerge in different simulations.

(6) In real grid cells, there is a dense and fairly uniform representation of all phases (see the toroidal tuning of grid cells measured by Gardner et al). Thus, the highly clustered phases obtained in the model (Fig. S1) seem incompatible with the experimental reality. I suspect that this may be related to the difficulty in identifying the topology of a torus in persistent homology analysis based on the transpose of the matrix M.

(7) The motivations stated in the introduction came across to me as weak. As now acknolwledged in the manuscript, attractor models can be fully compatible with distortions of the hexagonal spatial response patterns - they become incompatible with this spatial distortions only if one adopts a highly naive and implausible hypothesis that the attractor state is updated only by path integration. While attractor models are compatible with distortions of the spatial response pattern, it is very difficult to explain why the population activity patterns are tightly preserved across multiple conditions without a rigid two-dimentional attractor structure. This strong prediction of attractor models withstood many experimental tests - in fact, I am not aware of any data set where substantial distortions of the toroidal activity manifold were observed, despite many attempts to challenge the model. This is the main motivation for attractor models. The present model does not explain these features, yet it also does not directly offer an explanation for distortions in the spatial response pattern.

(8). There is also some weakness in the mathematical description of the dynamics. Mathematical equations are formulated in discrete time steps, without a clear interpretation in terms of biophysically relevant time scales. It appears that there are no terms in the dynamics associated with an intrinsic time scale of the neurons or the synapses (a leak time constant and/or synaptic time constants). I generally favor simple models without lots of complexity, yet within this style of modelling, the formulation adopted in this manuscript is unconventional, introducing a difficulty in interpreting synaptic weights as being weak or strong, and a difficulty in interpreting the model in the context of other studies.

In my view, the weaknesses discussed above limit the ability of the model, as it stands, to offer a compelling explanation for the toroidal topology of grid cell population activity patterns, and especially the rigidity of the manifold across environments and behavioral states. Still, the work offers an interesting way of thinking on how the toroidal topology might emerge.
