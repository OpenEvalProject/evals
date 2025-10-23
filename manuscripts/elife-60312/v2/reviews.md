# Peer review - Round 1

Editors:
- Yibing Shan, DE Shaw Research United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.60312.sa1](https://doi.org/10.7554/eLife.60312.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Using machine learning and polymer physics simulations, Cheng and colleagues generated structural models of chromosomes that are broadly consistent with single-cell imaging and capture the key characteristics of genomic compartmentation. With continued increase of single-cell imaging data and improvement in accuracy for training and calibration of such computational modeling, this holds great potential in generating accurate and full-scale chromosome structures and revealing the underlying mechanism of epigenetic switching at an molecular level.

Decision letter after peer review:

Thank you for submitting your article "Exploring Chromosomal Structural Heterogeneity Across Multiple Cell Lines" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Yibing Shan as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Detlef Weigel as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Huafeng Xu (Reviewer #2); and Jie Liang (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

Cheng et al. combined two computational methods previously published by the authors – MiChroM and MEGABASE – to simulate structural models of chromatins across six cell lines. They demonstrated good correlation between the average pairwise segment-segment contacts in the simulated models and the contacts inferred from ligation experiments and found similar statistical properties in the simulated models and in the structures observed by super-resolution microscopy. A number of important findings have been obtained from this study. A key finding is the high structural variability and ensemble nature of chromatins and as a result a chromatin generally cannot be described by a single stable structural fold. Furthermore, the study suggests that the structural linker region connecting compact domains contains most of genes for a chromosome segment.

Revisions for this paper:

1) The authors showed that different epigenetics of different cell types lead to different distributions of A/B compartments, which further lead to active A compartments moving toward to the surface of chromosomes, and inactive B compartments with stronger self-attraction move to the interior. However, it is well-known that LAD attachment can have strong effects on chromatin phase separations, as shown experimentally by Solovei et al., 2013, on lamin, and more recently in phase-field modeling work of Lee et al., 2017, and Laghmach, Pierro and Potoyan, 2020. In fact, in some studies this appear to be a dominant factor. The authors may wish to clarify whether lamina is included in the model, and whether the effects of LAD association would affect the conclusion of the results. Can the author provides a physical explanation of the A-B compartmentation beyond the analogy to hydrophobic collapse, and the possible physical elements that might regulate the open-close transition.

2) Figure 1E showed that predicted and measured A/B compartments have generally good correlation, with R varying for different cell types. It will be useful to plot the correlation R for A/B predictions/measurement, and R for simulated/measured Hi-C maps together. Are these R(A/B) and R(heatmaps) correlated? If not strongly correlated, why? Knowing this is useful as it may shed light on understanding to what extent the physical interactions encoded in the model (e.g. B-B hydrophobic-like interactions) explain the Hi-C maps, and how sensitive the current chromatin folding model is to the accuracy of A/B compartments assignment. Further, can the author provides a physical explanation of the A-B compartmentation beyond the analogy to hydrophobic collapse, and the possible physical elements that might regulate the open-close transition?

3) The authors showed that inclusion of CTCF-loops improves agreement of simulation and measured Hi-C heatmaps. Is this property uniquely for CTCF? A recent study showed that a small set of driver interactions exists for many loci, not necessarily involving CTCF, where 15-35 judiciously selected specific driver interactions can fold loci of enhancers of 500KB-1.9MB, with excellent R (>0.95) between measured and simulated Hi-C at 5 KB (PMC6966897). The authors may wish to further elaborate on their finding, e.g. after conducting a control study where a randomly (or non-randomly) chosen non-CTCF loop is include/not included, and whether such effects are also observed.

4) Simulated Hi-C heatmaps are reported for 7 cell lines. What are the cell nuclei sizes of these cells, and whether this size difference is taken into account in the simulations, and in general, why this is or is not an issue. This is relevant, as different nuclear size may affect the overall folding landscape of chromatin, since the effects of nuclear size confinement is one of the most strong constraints of chromatin.

5.1) The comparison with single-cell imaging data of Binto et al. is very interesting. It will be helpful if the authors show more details with examples of the degree of agreement between simulation and imaging studies. For example, a side-by-side comparison of best examples of single-cell heatmaps of Euclidean distance/contact between Bintu et al. measured single cells and simulated chromatin single-cell conformations. This can be supplemented with an overall scatter-plot of correlations of the pair-conformations of simulated/imaged conformations. Recent studies have shown some success in reproducing single cell Dip-C data through modeling (PMID PMC6966897), but comparison with imaging data is currently lacking, and the authors' results may set the standard for the field.

5.2) The 3D coordinates are available for both the simulated and the experimental structural ensembles. Thus, in addition to analyses of macroscopic and statistical properties such as the distribution of Rg and the probability of open/close conformations, direct structural comparison should be feasible, which can show that indeed some of the structures generated by the simulations are highly consistent with the experimental structures. Can we compute the average accessible surface area for each 50kb segment and compare between simulations and experiments? Can we plot the contact probability for each pair of segments in the simulations against that in the experimental structures?

5.3) In Figure 1, the simulated structures appear to have significantly more contacts than inferred from ligation experiments. Does this imply that the simulated structures might be too compact? Is this because the experiment sampling is more limited than the simulations? Or because there is some potential systematic discrepancy despite the high-level consistency between the simulation and the experiment. This should be discussed.

6) While the clustering of both imaging and simulations clearly showed the heterogeneity of chromatin, how are clusters defined? If clustered by a different order parameter, e.g. Q instead of Rg, do we still have the same finding – I wonder if certain natural order emerges from clustering. If we cluster both the simulated and experimental structures together, do they mingle in the same clusters?

7) There is an interesting discussion of the two-state equilibrium model and the PMF estimated energy gap of 4KT (also in the eighth paragraph of the subsection “Chromatin structural ensembles from DNA tracing reveal coexistence of open and closed structures”). However, can imaging studies of Segment 1 of Bintu et al. really be thought as from thermodynamic equilibrium? Its experimental set-up may be quite complicated and it is unclear whether imaged cells are samples properly drawn from the equilibrium distribution. In fact, the authors stated that chromatins are highly dynamic and follow a non-equilibrium process (Discussion, first paragraph).

8) "The genomic distance-dependent interactions recaptures the effect of motors acting along the DNA polymer." There is also well-known loop length dependent entropic effects as well, which may be part of the observed genomic distance dependency. It will be helpful if the authors clarify that only the motor-driven active process are at play in their model, or a mixture of both factors, and perhaps other hidden unspecified events are effectively accounted for in their model? Also, a citation on the motor process here will be helpful.

9) The reported finding that the linker region connecting two compact domains contains most of genes for segment 1 is very nice. Is this observation general?

10) The finding reported provides guidance for further biophysical studies of chromatin, for example, simple approximations such as Gaussian network models for chromatin domains are unlikely to be successful in capturing the heterogeneity of chromatin. The authors may want to briefly discuss the Gaussian network model in light of their results.

Revisions expected in follow-up work:

There was agreement that the value of the work could be greatly enhanced if the authors used their model to address a question of biological interest. For example, can the authors use their structural models-which have much richer details than available from experiments-to shed light on the distinction between the structural differences across different cell types and the variations among individual cells within the same cell type? What do the structural models teach us about transcription regulation?
