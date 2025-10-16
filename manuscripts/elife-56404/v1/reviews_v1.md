# Peer review - Round 1

Editors:
- Pierre Sens, Institut Curie, PSL Research University, CNRS France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.56404.sa1](https://doi.org/10.7554/eLife.56404.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Understanding homeostasis of tissues renewed by localised populations of stem cells requires the development of models to simulate the dynamics of cellular turnover. Savir etal. propose a 2D lattice-based Monte-Carlo model of stem cell renewal of the cornea, which is an interesting model system as it is renewed by localised populations of stem cells, requiring long-range flows to balance cell loss. They incorporate the main relevant features that include the modes of stem cell divisions (stochastic vs. deterministic), the spatial correlations between the locations of replication and cell removal, the directionality bias of the division planes and the replicative lifespan of progenitor cells. This model provides a general relationship between spatial correlations between duplication and removal and the replicative lifespan (number of cell division before death) of stem cells. The modelling approach is sufficiently generic so this this model should apply to other tissues with similar competitive dynamics. In the case of the cornea, the model predicts that the replicative lifespan is sufficient to allow the complete rejuvenation of the tissue, and that the spatial distribution of stem cells in the periphery of the cornea does not affect the competition between cell duplication and removal.

Decision letter after peer review:

Thank you for submitting your article "The role of replication‐removal spatial correlations and cellular replicative lifespan in corneal epithelium homeostasis" for consideration by eLife. Your article has been reviewed by Aleksandra Walczak as the Senior Editor, a Reviewing Editor, and two reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Shalev Itzkovitz (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

Understanding homeostasis of stem cell maintained tissues requires the development of models to simulate the dynamics of cellular turnover. In this manuscript, the authors propose a 2D computational model of stem cell renewal of the cornea, which is an interesting model system as it is renewed by localised populations of stem cells, requiring long-range flows to balance cell loss. They incorporate the main relevant features that include the modes of stem cell divisions (stochastic vs. deterministic), the spatial correlations between the locations of replication and cell removal, the directionality bias of the division planes and the replicative lifespan of progenitor cells.

The reviewers and myself find your work interesting and your approach elegant. Both the methodology and the results will be of interest to both systems biologists and cell biologists interested in the modelling of tissue dynamics. The geometry of the cornea system simulated is very interesting and leads to non-trivial results that really require this kind of computational approach. The paper is clearly written and the methods and theoretical approach well described.

However, the paper would strongly benefit from more links to experiments and to the existing literature. We also ask you to consider alternative hypotheses, in particular those involving spatial coupling through mechanical effects.

Please consider the list of comments below to help you revise your manuscript and increase the generality and impact of your work.

Essential revisions:

1) The title right now is quite general, could the title be reformulated to emphasise the findings (for instance on the tradeoffs, or the impact on clonal shapes).

2) The non expert readers would benefit from a better description of the experimental system you are modelling. This appears to be a lineage tracing mouse model for exploring clonal dynamics. Are all cells in the cornea labelled or rather only the stem cells? Is this a confetti mouse system? Could it be possible to reproduce some of the published experimental data next to your numerical results in a Supplementary information figure. This would be quite visual and demonstrative for readers not directly familiar with the system.

3) There addition of experimental data would strengthen your work.

(3.1) Are there measurements of EdU or BrdU incorporation in the cornea that could validate some of the model predictions, e.g. the radial positions where cells proliferate as well as the rates of proliferation? What are these rates (once per week? Once per month)? If such data exists it should be added to Table S1.

– Are there estimates of the number of stem cells per cornea? If yes, please add to Table S1.

(3.2) Can the velocity of cells as a function of radial position be analyse? If all cells divide with a complete radial bias, that cell movement would be accelerated as cell approach the centers, similarly to the situation in the intestinal crypts, where the higher cells are along the crypt axis the faster they move (e.g. PMID 28049136).

(3.3) Could experimentally measured value of the fraction of post-mitotic cells be added to Figure 6B.

4) Further comparison with existing literature is required.

(4.1) Regarding the spatial structure of the patches. You mention

Findlay et al., 2016; Kucerova et al., 2012; Mort et al., 2011; Douvaras et al., 2013;, where messy patches instead of continuous strips are observed, and use it to motivate your simulations in the condition of lost directionality. This is a nice idea, but looking at the references, it looks like in these mutants, patches are still incredibly sharp and distinct from one another, with really little dispersion (for instance Pax6 mutants). This is visually quite different from what is shown for instance on Figure 2. In fact, even for high directionality (Figure 3), stripes look much more messy than the experimental counterparts.

Does this mean that the spatial coupling should be smaller than the current value (m=5), which is based on a different system (epidermis in Mesa et al., 2018; Miroshnikova et al., 2018). Exploring this further would be valuable.

– The unmixing parameters seems quite influenced by the 1D stripe geometry: for instance, the green curve in Figure S1A shows fairly low value of \phi although it corresponds to very sharp and unmixed domains (from a 2D perspective). It is therefore important and helpful to experimentalists to quantify the clonal boundary roughness differently. Some work have explored the effect of stochastic clonal dispersion/competition on clone shape and size (for instance Rulands et al., 2018 as well as Corominas-Murtra et al., and Hallatschek et al., 2007 in the presence of net flows/expansion), which could have some useful theoretical formula/connections to this.

(4.2) You should discuss more in detail Moraki, Grima and Painter, 2019, which models the same system of cornea. You only mention it to say that it was a 1D model – and the 2D aspect is an important step forwards – but Moraki, Grima and Painter, 2019 did look at the influence of replication cycle, fraction of stem cells and division rates for cornea renewal, so it's necessary to compare and contrast in the Discussion.

(4.3) You explore the evolution of clone number as a function of time in Figure 7 but do not comment on the shape of these distributions, which have been derived analytically for a number of systems and geometries (Klein and Simons, 2011 for instance). Competition across a 1D ring in the limbus for instance is expected to give rise to gaussian distributions of clone sizes, average clone sizes increasing as sqrt(t) and number of clones decreasing as 1/sqrt(t). You should check if your distributions follow this expectation?

5) Alternative models could be considered, for instance removal driving the system. You only consider unidirectional correlations (division -> removal). But the reverse could be possible. Directional stripes could result from cells dying in the center of the patch, creating a negative pressure that would drive a centripetal flow of cell (in the hydrodynamic sense). In general, mechanics is entirely absent from the algorithm at present. Could it be included in the model, or at least discussed in a more quantitative way.

6) The Discussion already mentions the relation to pathologies and in particular cancer. It could be interesting to expand this a bit in relation with the proposed model. For instance, is there cancer of the cornea? If not, might this indicate optimality of the system to avoid accumulation of oncogenic mutations? How do the different models affect the accumulations/flushing of mutations in lineages with time? Purely asymmetric divisions can lead to higher accumulation of a series of oncogenic mutations whereas symmetric stem cell divisions can stochastically flush out oncogenic mutations. One may assume that the extent of replication and the geometry could also affect the “depth” of each lineage and consequently the numbers of mutations it would accumulate before oncogenic transformation. You could refer to PMID 14988930, 24264992 when discussing this point.

7) It would be nice to add the simulation code as a supplement.
