# Peer review - Round 1

Editors:
- Thomas Surrey, https://ror.org/03wyzt892 Centre for Genomic Regulation (CRG) Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75931.sa0](https://doi.org/10.7554/eLife.75931.sa0)

Using improved optical imaging of growing microtubules and improved data analysis, the authors find that microtubule growth fluctuations are less pronounced than previously reported and that GTP hydrolysis in microtubules increases these fluctuations. A mathematical model of microtubule growth suggests that occasionally exposed GDP at the microtubule end can be responsible for increased growth fluctuations. This work provides new mechanistic insight into the molecular mechanism of microtubule growth.


---

# Peer review - Round 1

Editors:
- Thomas Surrey, https://ror.org/03wyzt892 Centre for Genomic Regulation (CRG) Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75931.sa1](https://doi.org/10.7554/eLife.75931.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Measurements and simulations of microtubule growth imply strong longitudinal interactions and reveal a role for GDP on the elongating end" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Anna Akhmanova as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Alex Mogilner (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Please provide more context and a broader motivation for the study in the Introduction making sure relevant literature is cited and shorten the summary of the results in the Introduction to avoid repetition.

2) Model: Please explain if/why a 2D model is needed for microtubule growth (instead of only single filament model).

3) Discussion: Please compare the model and the parameters used here to the relevant previous modelling studies, including a recent study of the authors (see reviewers' comments).

4) Please make sure that all error bars are provided and clearly stated.

5) Please make other editorial changes where appropriate to improve clarity of presentation, considering the suggestions made by the reviewers.

Reviewer #1 (Recommendations for the authors):

1. The Introduction currently provides a long summary of the results after a rather short introduction of previous work addressing the question of microtubule growth fluctuations. The topic could be introduced in a more comprehensive and a more conceptual manner and the summary of the results could in turn be shortened.

2. The Discussion could more clearly explain the difference between previous exclusively taper-shape dependent growth models and the model here which is a mixture of a taper shape and GTP hydrolysis model. Particularly why previous taper shape-dependent models that could explain even larger growth fluctuations now seem to fail for the reduced growth fluctuations of GTP microtubules as measured here.

Reviewer #2 (Recommendations for the authors):

I am not a serious experimental expert, but from my limited perspective the experiments are done very well. The model, simulations and comparison with the data are flawless.

Reviewer #3 (Recommendations for the authors):

The manuscript is rough and needs significant revisions:

– The Introduction devotes too much text to summarizing the results (all of page 3 basically) and too little text to introducing the question and the state of the debate. It's really only the 2nd paragraph that introduces pertinent papers. The authors should reach further back than Gardner 2011, because Gardner 2011 was itself part of a series of studies whose intent was to measure the kinetics of polymerization. E.g. Kerssemakers et al., Nature 2006 and Schek et al., Curr Biol 2007 come to mind. Classic citations relating to association kinetics, like Northrup and Erickson PNAS 1992, would help contextualize the tubulin results in a broader biochemical context. As it stands, the motivation for the paper appears to be "confirm Mickolajczyk but with bovine tubulin", and that's an under-sell.

– Several key figure panels not referred to in the text at all. E.g., I could not find a call out to Figure 1D and 1E, even though these figure panels are complex and difficult to understand. Please ensure that every figure panel is explained and called out individually. Figure 1D in particular is challenging for non-specialists.

– Many data points are missing error bars. See the bottom half of Figure 2. There should be error bars on the computational output as well, because stochastic simulations produce variable results. If the error is smaller than the displayed data point, please state so in the figure legend.

In addition, I recommend the following specific changes:

– The raw data kymographs are far too small (Figure 1B and Figure 3A). The quality of the raw IRM data looks very good, but it cannot be clearly assessed from such shrunken examples.

– When I compare Figure 1B (GMPCPP, low fluctuations) to Figure 3A (GTP, higher fluctuations), it's actually Figure 3A that appears to have smoother length vs. time plots. The issue is probably related to y-axis scaling, and I recommend consistent y-axes. In fact, it would be excellent to place GMCPP traces directly adjacent to GTP traces (perhaps in Figure 3), because that would allow for direct visualization of the core comparison being made in the manuscript. Figure 1-S1 does a nice job showing a side-by-side of pixel corrected vs. sub-pixel corrected.

– There is some inconsistency in the units used to describe bonds. E.g., Figure 2C uses molar affinities but Figure 2-S2 uses kT. I think in kT personally, but it's also fine if Figure 2-S2 shows affinity. Then the red arrow would point to 25 nM.

– Figure 2 S2 shows that the lateral bond strength parameter is not well specified, in the sense that the fitting residual is constant and minimal over at least a 4 kT range. Thus, the choice of lateral affinity (25 nM) is somewhat arbitrary, and the lateral affinity could be described as a "sloppy" parameter. Lateral bonds were also shown to be sloppy parameters that could be compressed out of a computational model of dynamic instability by Hsu et al., Biophys J 2020.

– Merge Figure 2 S4 and S5 --I understand the awkwardness there is that the other 3 show scaling of both k-on and K-D, while the best fit keeps the k-on of the "red" model and differs in K-D only. But right now I find it confusing, like there's a shadow parameter set that is not shown in some figures (main Figure 2, Figure 2 S3), but which is actually the most important parameter set. I encourage the authors to present all 4 parameter sets in a single, consistent format.

– In Figure 4, I recommend putting all of the model parameters in the figure itself. The parameters are currently found in the legend (4A), but the reader would find them more easily in the figure itself, and it would be clearer that the new parameters are NOT taken from previous figures, because of the new fitting to the GTP-growth data.
