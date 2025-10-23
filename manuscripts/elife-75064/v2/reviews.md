# Peer review - Round 1

Editors:
- Daniel R Larson, https://ror.org/01cwqze88 National Cancer Institute, National Institutes of Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75064.sa0](https://doi.org/10.7554/eLife.75064.sa0)

This work on dissecting the function of transcription factors using single-molecule methods is likely to appeal to the broad eLife readership and the gene regulation community at large. In particular, the role of transcription activation domains in transcriptional specificity is a timely contribution to the field.


---

# Peer review - Round 1

Editors:
- Daniel R Larson, https://ror.org/01cwqze88 National Cancer Institute, National Institutes of Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75064.sa1](https://doi.org/10.7554/eLife.75064.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Mechanisms Governing Target Search and Binding Dynamics of Hypoxia-Inducible Factors" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Kevin Struhl as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: David M Suter (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. As you can see below, there was broad enthusiasm for the single-molecule imaging approach for uncoupling DNA binding domains and trans-activation domains. However, there was also a consensus that the key potential advance of this paper is connecting reaction diffusion kinetics to the specificity of DNA binding. Yet, the specificity aspect, although given as a primary motivation, is not adequately established experimentally. Such data are essential to include in a revision.

2) Analysis of single-molecule tracking data is central to the claims, and there were a number of concerns raised by each referee about the choice of algorithms, models, use of controls, types of mobility, etc. These issues need to be addressed in detail in a revised manuscript.

Reviewer #1 (Recommendations for the authors):

1. The authors motivate the work with the fact that different HIF1 isoforms have similar in vitro binding specificity but different biological activity. Yet, they don't ultimately resolve this question or even shed much light on it. For example, nothing in the present analysis says whether the different dimer moieties actually bind different sequences (for example ChIP-seq or in vitro gel shift). As such, the claim of specificity being determined by IDRs is a little oblique. Dynamics are clearly determined by IDRs as the authors nicely show, but the connection back to binding specificity is very indirect. However, this group could easily carry out gel shift binding assays or even single-molecule kinetic assays in vitro to solidify this point.

2. All the conclusions are essentially reached exclusively through the SPT assay with a new analysis approach that has not yet been peer-reviewed. As such, there is not much to latch on to from a referee perspective. Either an orthogonal assay or comparison to existing approaches of SPT analysis would greatly increase the confidence in the results.

Reviewer #2 (Recommendations for the authors):

The authors should improve their manuscript by including the following points:

– They should quantify the expression levels of all endogenous fusion proteins and exogeneously expressed transcription factors and mutants by several independent Western Blots, otherwise it is hard to judge whether a change in bound fraction or peak diffusion coefficient is due to the condition tested or rather due to differences in expression levels.

– They should control for proper gene transcription of their mutants, in particular the domain-swap mutants, analogous to the experiments using the luciferase reporter gene for HIF-2a.

– They should control that their high laser power of 1100 mW for illumination does not harm the cells.

– They should perform more measurements to arrive at statistically sound analysis. in particular, more biological replicates should enter each determination of bound fraction or peak diffusion coefficient.

– In addition to bound fractions, the authors should quantify the peak diffusion coefficient for each mutant and experimental condition and compare the relative changes between bound fraction and diffusion coefficient for each mutant and experimental condition, to allow estimating which property is more important.

The authors could further improve the impact of their manuscript by including the following points:

– For now, the authors only characterise the effect of different domains of HIF-a on HIF-1b or HIF-a binding. It would be informative if the authors also could characterise the effect of HIF-1b domains on its bound fraction and diffusion properties.

– Previously, the confinement of single particles was analysed (Lerner et al., Mol Cell 2020). The extent of confinement was shown to depend on the intrinsicall disordered domain of glucocorticoid receptors (Garcia et al., Mol Cell 2021). It would be good to see to which extent the intrinsically disordered domain of HIF mediates different confinement states, and whether there are differences between the IDRs of HIF-1a and HIF-2a.

– To answer the question whether IDRs actually contribute to differential DNA sequence specificity, the authors could perform ChIP experiments analogous to Figure S2D for the domain-swapped mutants of HIF-a.

Additional points:

– Line 145-158: analysis of diffusion behaviour using non-parametric Bayesian approach: the authors use a novel method to analyse their data. Although they provide a reference, there need to be more details in the text on how this method works

– Figure S4B: it is unclear which cell line was used, an unedited cell line with endogeous HIF-2a or a Halo-HIF-2a edited cell line?

– Line 247: …we do not observe a significant change in the overall speed of the diffusing population.

– Diffusion does not have a speed, please use other wording.

– Figure 1D, E: missing scale bar description.

– What is does V5 refer to?

– Line 92: please correct: HIF isoforms.

– Line 923: should read "as in Figure 4".

Reviewer #3 (Recommendations for the authors):

Overall this is a solid piece of work that convincingly shows the role of transactivation domains in determining the TF bound fraction. Although the impact of TADs on search is not entirely new, the dissection performed here using state of the art SPT and analysis is very valuable.

I do have a few suggestions that may further strengthen and enrich their findings, which mainly imply further analysis of their already acquired datasets:

1. The authors show that the different TADs of the α subunits have a differential impact on the bound fraction of HIF-1beta. They suggest that this is due to a difference in search capacity. Are the authors implying differences in on-rates? The bound fraction will be influenced both by on-rates and off-rates.

I suggest that using their already acquired data, the authors compute and show the off-rates (or dwell times) for all the TFs they analyze. In addition, I suggest they also compute a pseudo on-rate (as in Raccaud et al. 2019 for example), which they can easily do from their data as the relative concentration of each TF they study is already captured from their data. This would provide more information on the relative contribution of on- vs off-rate to the bound fraction.

2. Concerning the stoichiometry differences between the β and α subunits, I do agree that this is consistent with the western blots but these are not very quantitative (and also the band intensities were not quantified). The authors could perform image-based quantification using epifluorescence microscopy with a Halo dye for a more precise quantification.

3. It would be valuable to classify the diffusive behaviours of the different TF they looked at in brownian, super-diffusion and sub-diffusion behaviour as these may reflect the size of the complex they are part of.
