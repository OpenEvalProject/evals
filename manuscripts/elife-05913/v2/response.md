# Author response - Round 1

Authors:
- Federico Stella
- Alessandro Treves

## Response text

DOI: [10.7554/eLife.05913.011](https://doi.org/10.7554/eLife.05913.011)

1) In the Abstract (and in many other places in the paper): The focus seems to be on predictions for bat experiments. Why do the authors single out the bat as the only relevant animal model for 3D grids? The predictions in the paper are very general, and may hold also for monkeys, dolphins, cats, or humans that also move through 3D space. The focus on bats is too narrow, and should be broadened throughout.

We agree, with the qualification that the prevalence of an allocentric coding of the animal’s own position in space has yet to be established for most mammalian orders. We would not want our model to be seen as taking a stand, for example, on the controversial issue of place vs. spatial view codes in monkeys. To avoid that, while still pointing at the potential generality of the conclusions, we have added, in the Abstract, “… bats, or perhaps dolphins…”, and, as a second sentence of the Introduction, “how does it code for space extending in three dimensions?”

Still in the first paragraph, we have expanded a sentence to read: “… and it provides an indication possibly valid also for other animals living and moving extensively in three dimensions, like for example dolphins, monkeys and even nonmammalian species”. And, in the second: “the form that grid cells will exhibit in higher dimensionality (currently tested in flying bats; Jeffery, 2013) is still not clear.” We have also concluded the Introduction with the sentence: “We use bats as our reference, as it is the species currently available for experiments during roughly homogeneous navigation along the three dimensions of physical space.”

In the Discussion, instead of just asking “expressed by a flying bat?” we now ask “expressed in 3D, and that can be tested in a flying bat?” and see below (point 5) for the sentence inserted at the very end of the Discussion.

2) In the subsection “The network”, the authors mention that sigma_p = 0.05L. Does changing the sigma_p of the place cells affect any of the final properties of the grids, and/or their developmental time course?

That paragraph has now been extended to clarify this point:

“Place field centers are homogeneously distributed in the volume (consistently with the experimental data presented in Yartsev, 2013). […] the properties of the developing grid fields depend on the time scale of adaptation and not on the size of the place fields.”

3) In the end of the subsection “HCP symmetry”: It is unclear why the authors write that small kz is equivalent to columns spreading over the z-axis (height) entire room. An alternative possibility is having only one layer of spherical blobs in the XY plane, without any additional layers repeating in the z-dimension. Are these options equivalent in terms of the minimization of the cost function?

We have hopefully clarified this point by expanding the relevant paragraph:

“… of the inter-layer spacing (and also the wavelength of the activity modulation along the zaxis), this value […] with no activity above and below them, a situation that does not entail the regular, three dimensional configurations we are interested in.”

4) Results section, subsection headed “Which is the most favorable analytical solution?”: The authors focus on HCP and FCC, but it is unclear here to which degree do they see also other solutions, besides HCP and FCC, e.g. random order of layers: ABCABABACBCBA… which is an arrangement that pack 3D space just as well as FCC or HCP but does not have any large-scale structure along the z-axis. Did you observe such neurons in your simulations?

We have added this discussion at the end of section A of the Results, on the most favourable analytical solution:

“The discrepancy between the configurations observed and the symmetric solutions […] additional layers would just propagate further this situation without leading to the appearance of FCC and HCP mixtures.”

5) In the Discussion: The impression one gets from the end of the Discussion is that almost no cells at all are expected to exhibit perfect FCC or HCP - but in fact, according to Figure 4 (left), it seems that at least some of the grid cells are actually expected to develop a perfect FCC or a perfect HCP; is this correct? These cells might be a minority, but at least some are expected to develop FCC or FCP. So I think it's worthwhile to write it here explicitly, because right now the discussions seems to suggest the opposite.

We have added a passage to clarify this point at the end of the Discussion:

“In our model this distance varies across a population of cells […] possibly including other species experiencing three-dimensional navigation.

6) The model does not allow for plasticity between grid cells. The spatially localized structure for grid cell firing is essentially built in by hand through hand tuning, ahead of time, the lateral synapses. Note that this is only a suggestion for a future avenue of research and does not need to be addressed for the manuscript to be deemed acceptable. The progress made on addressing this difficult theoretical problem is sufficient for publication already.

In the section on “Collateral Weights”, we have now clarified in the very beginning that “the appearance of fields in the output layer of the model is fully independent of the presence of collateral connections. Instead, their basic function…”

7) The Results section could be written to be in a somewhat more accessible form for the general, less mathematical reader.

We have made some adjustments to the Results and Methods section, for example in the first paragraph of the Methods, we have added for clarity the sentence: “The path the animal performs is generated as a correlated random walk in which the direction of movement at any time step depends on the previous one”.

We have also added some clarifications in the “Volume Dependence” subsection of the Results, where the issue of dimensional scaling is discussed.

We have introduced a new figure (Figure 1) to provide a pictorial explanation of the model and of the main idea conveyed in the Results section: the model does indeed produce three-dimensional grids but this process requires an extensive amount of time. We also extended Figure 2 to include an additional visualization of the FCC and HCP arrangements of fields from a different point of view. The panels in the second row now highlight the different tiling of the layers in the two structures.

==========
