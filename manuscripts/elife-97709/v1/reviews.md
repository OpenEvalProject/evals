# Peer review - Round 1

Editors:
- Rosana Collepardo, University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.97709.3.sa0](https://doi.org/10.7554/eLife.97709.3.sa0)

This study describes the application of machine learning and Markov state models to characterize the binding mechanism of alpha-Synuclein to the small molecule Fasudil. The results suggest that entropic expansion can explain such binding. However, the simulations and analyses in their present form are inadequate.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97709.3.sa1](https://doi.org/10.7554/eLife.97709.3.sa1)

The manuscript by Menon et al describes a set of simulations of alpha-Synuclein (aSYN) and analyses of these and previous simulations in the presence of a small molecule.

Comments on latest version:

I have read the authors' response to my comments as well as to the other reviewers. Summarizing briefly, I don't think they provide substantial answer to the questions/comments by me or reviewer 3, and generally do not quantify the results/effects data. I still remain unconvinced about the analyses and conclusions. Rather than rewriting another set of comments, I think it will be more useful for all (authors and readers) simply to be able to see the entire set of reviews and responses together with the paper.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97709.3.sa2](https://doi.org/10.7554/eLife.97709.3.sa2)

In this manuscript Menon, Adhikari, and Mondal analyze explicit solvent molecular dynamics (MD) computer simulations of the intrinsically disordered protein (IDP) alpha-synuclein in the presence and absence of a small molecule ligand, Fasudil, previously demonstrated to bind alpha-synuclein by NMR spectroscopy without inducing folding into more ordered structures. In order to provide insight into the binding mechanism of Fasudil the authors analyze an unbiased 1500us MD simulation of alpha-synuclein in the presence of Fasudil previously reported by Robustelli et.al. (Journal of the American Chemical Society, 144(6), pp.2501-2510). The authors compare this simulation to a very different set of apo simulations: 23 separate1-4us simulations of alpha-synuclein seeded from different apo conformations taken from another previously reported by Robustelli et. al. (PNAS, 115 (21), E4758-E4766), for a total of ~62us.

To analyze the conformational space of alpha-synuclein - the authors employ a variational auto-encoder (VAE) to reduce the dimensionality of Ca-Ca pairwise distances to 2 dimensions, and use the latent space projection of the VAE to build Markov state Models. The authors utilize k-means clustering to cluster the sampled states of alpha-synuclein in each condition into 180 microstates on the VAE latent space. They then coarse grain these 180 microstates into a 3-macrostate model for apo alpha-synuclein and a 6-macrostate model for alpha-synuclein in the presence of fasudil using the PCCA+ course graining method. Few details are provided to explain the hyperparameters used for PCCA+ coarse graining and the rationale for selecting the final number of macrostates.

The authors analyze the properties of each of the alpha-synuclein macrostates from their final MSMs - examining intramolecular contacts, secondary structure propensities, and in the case of alpha-synuclein:Fasudil holo simulations - the contact probabilities between Fasudil and alpha-synuclein residues.

The authors utilize an additional variational autoencoder (a denoising convolutional VAE) to compare denoised contact maps of each macrostate, and project onto an additional latent space. The authors conclude that their apo and holo simulations are sampling distinct regions of the conformational space of alpha-synuclein projected on the denoising convolutional VAE latent space.

Finally, the authors calculate water entropy and protein conformational entropy for each microstate. To facilitate water entropy calculations - the author's take a single structure from each macrostate - and ran a 20ps simulation at a finer timestep (4 femtoseconds) using a previously published method (DoSPT), which computes thermodynamic properties of water from MD simulations using autocorrelation functions of water velocities. The authors report that water entropy calculated from these individual 20ps simulations is very similar.

For each macrostate the authors compute protein conformational entropy using a previously published Maximum Information Spanning tree approach based on torsion angle distributions - and observe that the estimated protein conformational entropy is substantially more negative for the macrostates of the holo ensemble.

The authors calculate mean first passage times from their Markov state models and report a strong correlation between the protein conformational entropy of each state and the mean first passage time from each state to the highest populated state.

As the authors observe the conformational entropy estimated from macrostates of the holo alpha-synuclein:Fasudil is greater than those estimated from macrostates of the apo holo alpha-synuclein macrostates - they suggest that the driving force of Fasudil binding is an increase in the conformational entropy of alpha-synuclein. No consideration/quantification of the enthalpy of alpha-synuclein Fasudil binding is presented.

Strengths:

The author's utilize MD simulations run with an appropriate force field for IDPs a99SB-disp and a99SB-disp water (Robustelli et. al, PNAS, 115 (21), E4758-E4766) - which has previously been used to perform MD simulations of alpha-synuclein that have been validated with extensive NMR data.

The contact probability between Fasudil and each alpha-synuclein residue observed in the previously performed 1500us MD simulation of alpha-synuclein in the presence of Fasudil (Robustelli et. al., Journal of the American Chemical Society, 144(6), pp.2501-2510) was previously found to be in good agreement with experimental NMR chemical shift perturbations upon Fasudil binding - suggesting that this simulation is a reasonable choice for understanding IDP:small molecule interactions.

Comments on the latest version:

While the authors have provided additional information in the updated manuscript, none of the additional analyses address the fundamental flaws of the manuscript.

The additional analyses do not convincingly demonstrate that these two extremely different simulation datasets (1500 microsecond unbiased MD for a-synuclein + fasudil, 23 separate 1-4 microsecond simulations of apo a-synuclein) are directly comparable for the purposes of building MSMs.

The additional analyses do not demonstrate that there are sufficient conformational transitions among kinetically metastable states observed in 23 separate 1-4 microsecond simulations of apo a-synuclein to build a valid MSM, or that the latent space of the VAE is kinetically meaningful.

If one is interested in modeling the kinetics and thermodynamics of transitions between a set of conformational states, and they run a small number of MD simulations that are too short to see conformational transitions between conformational states - any kinetics and thermodynamics modeled by an MSM will be inherently meaningless. This is likely to be the case with the apo a-synuclein dataset analyzed in this investigation.

Simulations of 1-4 microseconds are almost certainly far too short to see a meaningful sampling of conformational transitions of a highly entangled 140-residue IDP beyond a very local relaxation of the starting structures, and the authors provide no analyses to suggest otherwise.

Without convincingly demonstrating reasonable statistics of conformational changes from the very small apo simulation dataset analyzed here, it seems highly likely the apparent validity of the apo MSM results from learning a VAE latent space that groups structurally and kinetically distinct conformations into similar states, creating the spurious appearance of transitions between states. As such, the kinetics and thermodynamics of the resulting MSM are likely to be relatively meaningless, and comparisons with an MSM for a-synuclein in the presence of fasudil are likely to be meaningless.

In its present form, this study provides an example of how the use of black-box machine learning methods to analyze molecular simulations can lead to obtaining misleading results (such as the appearance of a valid MSM) - when more basic analyses are omitted.
