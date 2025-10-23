# Peer review - Round 1

Editors:
- Ariel Amir, https://ror.org/03vek6s52 Harvard University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82654.sa0](https://doi.org/10.7554/eLife.82654.sa0)

The work of Bellotto et al. provides a comprehensive and compelling study of the diffusion of proteins in the cytoplasm of the bacterium Escherichia coli, using multiple measurement methods, notably Fluorescence Correlation Spectroscopy. It is found that fast diffusing proteins roughly follow the Stokes-Einstein relation, while proteins that strongly interact with the cytoplasm manifest subdiffusion. This study will be a valuable resource for scientists seeking to understand the temporal dynamics of proteins within cells.


---

# Peer review - Round 1

Editors:
- Ariel Amir, https://ror.org/03vek6s52 Harvard University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82654.sa1](https://doi.org/10.7554/eLife.82654.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "Dependence of diffusion in Escherichia coli cytoplasm on protein size, environmental conditions and cell growth" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Conrad W Mullineaux (Reviewer #1).

Comments to the Authors:

We are sorry to say that, after consultation with the reviewers, we have decided that this work will not be considered further for publication by eLife.

As you will see in the reviews, both reviewers have appreciated the technical rigor of your work and the characterization of diffusion within E. coli well beyond previous work and with superior methodology. However, both were concerned whether major conceptual advances were obtained based on these results. In light of this, we regretfully cannot accept the paper in its current form. If you believe that you can restructure the paper and interpret your data in a manner that will enable you to draw novel conclusions and obtain a fundamental advance, we will be glad to reconsider this decision.

Reviewer #1 (Recommendations for the authors):

A very thorough study of protein diffusion in the E. coli cytoplasm, looking at multiple proteins (including mutants in which specific interactions are disabled), multiple conditions and two different methods to measure diffusion. I don't think it leads to any major conceptual advances: basically the results confirm what was already inferred from the previous studies cited: smaller proteins roughly follow the Stokes-Einstein relation for the size dependence of the diffusion coefficient, larger proteins show subdiffusion, interactions with other cell components slow everything down, different measurement methods give comparable but not identical answers. There is merit in having such a comprehensive set of measurements all in one place: this will be a valuable reference point for anyone who wants to explore the physical nature of the cytoplasm further, or who wants to factor cytoplasmic protein diffusion into a model for some dynamic process in E. coli.

The paper is well-written and well-presented, and I cannot find any technical flaws with the parts that I am able to judge. The weakness is maybe a lack of novelty: this provides strong confirmation of things that were already inferred on the basis of less complete data, but I missed any major conceptual advances in the understanding of the dynamics of the cytoplasm. If there is anything I missed, please highlight it better!

Reviewer #2 (Recommendations for the authors):

Belotto and co-workers performed a systematic experimental study of the intracellular mobility of 28 (+3 discarded on the way) cytoplasmic proteins in E. coli, using fluorescence correlation spectroscopy (FCS), complemented by some computational/ modeling. This technique is underexplored in the body of work looking at intracellular diffusion in bacteria, and allows them to probe very short time scales compared to commonly used techniques such as single-particle tracking (SPT).

The manuscript is not really focused on a main finding, but a main finding may be that the data cannot falsify a Brownian diffusion model when confinement is accounted for (see below). Other interesting findings consider the temperature and growth-rate dependency, and the agreement of FCS with FRAP (recovery after photobleaching) data.

The work is well written and provides a useful and precise set of measurements to the community. Its main advantages are it being systematic (28 is a large set of proteins for this kind of study), the novelty of FCS in this context, and the use of physical models in support of the data. However, we have some major concerns about the main results and conclusions:

0) In the way it is written, the manuscript does not identify a central question, and the findings could be better connected to the current debate.

1) In our view the central question could become the fact that the authors argue that conventional diffusion seems to be supported (or at least cannot be ruled out) for these data, while previous (SPT) data have supported mild but clear subdiffusion for (larger) cytoplasmic particles, including protein complexes. However, we have some possibly important concerns about this analysis, and in any case we think it needs more experimental and data-analysis/modeling controls (see below).

2) The other main results (dependency on growth, temperature, etc.) are interesting, but most of these things have been quantified by SPT, and a more careful comparison appears to be needed. Additionally, these results also need controls on cell size and density/crowding levels (see below).

With these important revisions, we believe the work could make a nice addition to the current debate.

We try to detail our impressions in the comments below.

1) Our main concern is that the controls/support of the claim of conventional diffusion may be insufficient. If well supported, my impression is that this could become (either way) a central result of the study.

The authors clearly show using modeling that their data cannot falsify Brownian diffusion. However, it is not clear to us that they can falsify fBM or fLe subdiffusion. A22 treatment provides an interesting control but PMID: 34341116 (see Figure 3) clearly shows that this treatment affects dry-mass density (QPI measurements are actually a proxy of macromolecular density, hence crowding).

Previous studies have clearly supported the idea that density (crowding) affects cytoplasmic diffusion (see e.g. PMID: 33083729), hence it seems to us that we do not know whether the observed changes in FCS may come from the density changes rather than the confinement. For example the previously observed anomalous diffusion could be due to larger size of (non-interacting) proteins or protein complexes, or to the presence of the chromosome, or the current data would just not allow to falsify either scenario, etc.

Also, the lack of a clear Stokes-Einstein relation even using fairly complex models of diffusion makes us think of a possible complex underlying dynamics (due to disorder or viscoelasticity, or both) or more in general other possible (but possibly interesting) physical scenarios.

Below we try to propose some controls and analyses.

The authors do not mention that (larger) protein particles like GFP muNS were also be reported to be subdiffusive by SPT. For example in PMID: 30374466 SPT was performed at 0.1s resolution and the MSDs of cytoplasmic particles do not show any sign of saturation.

One possible control would be to use velocity-velocity correlation functions (by SPT, PMID: 22713559, we do not know whether there is be a FCS analog of this). As far as we know this kind of analysis has not been published on cytoplasmic particles.

Movements on very small lags should not be affected by confinement. Since FCS allows to probe very small lags, the authors may try to examine how robust their results on confinement are if they limit the range of lags to the smaller values. For example repeating the analyses of Figure 2 as a function of an upper bound in the lag time.

Experimentally, the A22 control is not satisfactory unless the dry mass density is controlled for in some way. L forms may be obtained with several protocols, but once again density has to be measured and accounted for. Possibly FCS of GFP muNS particles can be of some use.

Side note: is A22 now in place of cephalexin or in addition to it? This may be important as there have been claims (Lobritz 2015, PNAS) of β-lactams increasing cell respiration rates (and thus change metabolic rates, and thus alter cytoplasmic metabolic stirring?). A control of diffusion in untreated cells VS cells treated with Cepha or Cepha+A22 is needed here.

One interesting control on width could use the cell-to-cell variability within a population, to check whether there is some effect.

2) The controls on cell size and density should apply also to the other main results.

Nutrient changes should keep the crowding levels (dry mass density, PMID: 4600702) constant but vary a lot cell geometry and width PMID: 13611202 (and thus are entangled with the control on cell width of the previous part of the study).

The other perturbations affect crowding (and some also cell geometry), and SPT results suggest that crowding levels recapitulate many (though not all) of the observed variations in mobility (see e.g. PMID: 33083729).

Regarding temperature effects, it would be interesting to compare with the results in

PMID: 22517744, which (using SPT) argues in favor of active (nonthermal) motion.

Regarding this point ATP depletion might also be an interesting control. Cell metabolism and. "stirring" is presumably pretty different at 25 or 35C.

Osmotic shocks (p19): besides checking cell size and density, it was not clear at what point before measurements was salt added. Were these cells shocked and allowed to recover?

Comparing measurements at the pole with measurements at midcell could also provide further insight (also maybe to claim a role for the chromosome).

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Dependence of diffusion in Escherichia coli cytoplasm on protein size, environmental conditions and cell growth" for further consideration by eLife. Your revised article has been evaluated by Naama Barkai (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Both reviewers acknowledged that the revised paper is significantly improved, and would be adequate for eLife.

However, please address the two comments by reviewer #2, regarding the consistency of the data with subdiffusive behavior, and the interpretation of the density measurements.

Reviewer #1 (Recommendations for the authors):

The authors have made a strong response to reviewers' comments on the first submission. I think the novelty and significance of the findings are now much clearer.

Reviewer #2 (Recommendations for the authors):

I have shared again the revisions with the same close experimental collaborator. We are happy about the changes but we still have two main outstanding issues that seem possibly important, and we would like the authors to address.

1) We appreciate that diffusion is the most parsimonious scenario, but there is a different (important) question. If the data were derived from subdiffusive particles, would the technique reveal it and to what quantitative extent the data must deviate from diffusion in order to be detected?

Probably several indications that the authors have could be used to support the authors' conclusions. For example, Figure 2 supplement 3 and the plot on time cutoffs provided in the reply seem in line with their interpretation.

Could the authors show with the technique used in Figure 2 supplement 3 that DnaK-sfGFP behaves differently?

Additionally, probably the authors can strengthen this point with additional arguments, e.g. by analyzing simulated data from subdiffusive particles and investigating the limitations of the technique in detecting this "ground truth".

In brief, we ask the authors not to lean automatically on the most parsimonious scenario, but to gather the existing evidence/arguments in the direction of rejecting subdiffusion, and address the point in a focused discussion in the text. Also extend the arguments whenever possible (also based on previous recommendations).

2) We are grateful that the authors provided extra measurements connected to the problem of density change, but we are not entirely convinced and/or we do not fully understand the results.

Looking at figure 2 supplement 2 it seems that cephalexin and A22 have quite some effect on density.

The authors quote a 0.1% but it is not clear where this number comes from.

Possibly from a quoted literature value of 1.1 g/ml = 1000 Kg/m^3 (but the source should be cited, and the estimate explained), but probably they did not measure directly density (?). Also note that in the Oldewurtel et al. paper the mean value seems closer to 0.35 g/ml (and in Figure 3 of the same paper density perturbations from A22 seem non-negligible) .

Additionally, looking at the plots in Figure 1 supplement 8 there seems to be a visible difference in 1/tauD: the quoted P-value is 0.08, which is not so large considering that there are so few points.

Going back to the density measurements in Figure 2 – Supplement 2, the slope between the two plots is clearly different. It also seems difficult to fit an exponential in the unperturbed case, so maybe the channel is too small to achieve good sensitivity in this case.

If one has to judge visually the differences in z0 between perturbed and unperturbed case they could be in the range of a factor of 10-100 (in the treated cases z0 seems of the order of the channel size, in the untreated case it is much larger).

Hence at fixed volume, δ rho would also be different by a factor of 10-100. Instead, it's only a factor of 2, which means that volume changes by a factor of 5-50. Already a factor of five seems quite large.

In brief, we would ask the authors to clarify their measurements of density and mobility (show the fits, quote the volume measurements, describe the estimates, possibly perform more measurements etc.)
