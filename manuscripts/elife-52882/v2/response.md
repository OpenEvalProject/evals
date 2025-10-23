# Author response - Round 1

Authors:
- Sophia Karpenko
- Sebastien Wolf
- Julie Lafaye
- Guillaume Le Goc
- Thomas Panier
- Volker Bormuth
- Raphaël Candelier ([ORCID: 0000-0002-1523-6249](https://orcid.org/0000-0002-1523-6249))
- Georges Debrégeas ([ORCID: 0000-0003-3698-4497](https://orcid.org/0000-0003-3698-4497))

## Response text

DOI: [10.7554/eLife.52882.sa2](https://doi.org/10.7554/eLife.52882.sa2)

Essential revisions:

1) The first two paragraphs should be re-written in a manner to better reflect the limits of the eventual conclusions of the paper. Specifically, a speculative hypothesis ("behavior is thus based as a set of statistic (sic) rules that defines how elementary motor motor actions are chained") is stated as fact. That this type of a model well-describes their data is sensible, but to cast all behavior – including non-foraging behavior – in this light seems well outside the scope of what they show here. If they want to make this (in our view, controversial) claim that behavior outside the foraging context all behave in this manner, it should be put forward in the Discussion section as a hypothesis emanating from the work rather than an underlying assumption. Notably, the text in the Discussion section was much more careful in this regard.

We agree that this claim was over-reaching. We modified the Introduction to immediately narrow the scope of this hypothesis to the locomotion of small animals.

2) In Figure 5—figure supplement 1, the authors show three illustrative trajectories produced by the model for different inter-bout intervals. It would be useful and important to provide the reader with a comparison of a set of trajectories of real fish and that simulated by the (full) stochastic model. This would permit the reader to judge the goodness of the reproduction of physical trajectories in addition to the statistical distributions (and density profiles of Figure 4B). At first, one might think that the trajectories shown in Figure 5—figure supplement 1 look more like those of Brownian particles than fish.

This perception is due to the scale of this particular figure, which encompasses very long sequences (much longer than experimentally measured trajectories). We added a supplementary figure (Figure 5—figure supplement 1) showing both real and simulated trajectories at a larger magnification for which individual bouts are visible. This figure establishes that the circuit-based simulation does correctly capture the fine-scale geometry of the trajectories.

3) In their Discussion, the authors argue about the advantages of testing the influence of contrast-driven orientation under constant overall illumination intensities. In the experiments of Figure 3, animals do not experience changes in light intensity as they move with respect to the virtual source. This (simplified) experimental paradigm is assumed to be sufficient to reveal the sensorimotor mechanism directing the klinotaxis/klinokinesis component of the orientation algorithm. Is the stochastic model sufficient to produce the ascent of light gradients in numerical simulations – a behavior more closely related to real-life situations?

Our aim was to characterize Zebrafish light-seeking strategies in the presence of a distant light source. In this case, the illumination angular profile experienced by the fish is independent of its (x,y) position in space – no spatial gradient – and thus also time-invariant. We showed that the fish is able to orient towards the light source (angular phototaxis), using either the contrast or the total brightness, and is thus able to progress towards it at constant (mean) speed. In a more realistic context, both the contrast and the total brightness would vary with the fish’s body orientation. However, because the two processes were shown to be independent from each other (acting on separate motor variables), these two mechanisms are expected to act in concert leading to efficient positive phototaxis.

When refering to real-life situations, the referee may imply contexts in which the source is located at a finite distance, such that the brightness also varies with the (x,y) spatial position of the fish. The increase in diffusivity induced by light decrement should allow the fish to progress in an illumination spatial gradient (even without contrast), by analogy with bacteria chemotaxis. However, we did not examine this process experimentally, and thus cannot provide quantitative comparison with experimental data. This particular condition is beyond the scope of our work.
