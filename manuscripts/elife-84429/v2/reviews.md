# Peer review - Round 1

Editors:
- Emilia Huerta-Sanchez, https://ror.org/05gq02987 Brown University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84429.sa0](https://doi.org/10.7554/eLife.84429.sa0)

In this important study, the authors develop a neural network to investigate assortative mating and sex-bias in admixed populations from the Americas. Applying their method to modern-day human genomes, they estimate sex-biased admixture and ancestry-based assortative mating. The evidence supporting their claims is solid, and their results will be of interest to population geneticists, anthropologists, and those interested in the history of the Americas.


---

# Peer review - Round 1

Editors:
- Emilia Huerta-Sanchez, https://ror.org/05gq02987 Brown University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84429.sa1](https://doi.org/10.7554/eLife.84429.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "The genomic footprint of social stratification in admixing American populations" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Molly Przeworski as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Full reviews are attached below, and should be carefully considered. Briefly, the most central areas to address include:

1) Assumption of known admixture timing: further simulations and/or empirical calculations to understand the role of this assumption, as well as careful discussion of the implications/choices, particularly because of the known impact of the timing of admixture on the variance of ancestry (which underlies the main inference).

2) Uncertainty: further estimates about the distributions/uncertainty/errors of key parameters of interest, specifically the level of sex bias and assortative mating. Consideration of alternative contributions to uncertainty are also important, particularly the role of potential errors in local ancestry inference on the X vs autosomes.

3) Contextualizing and discussing certain results (e.g. ASW mating patterns) that may be unintuitive and/or potentially conflict with previous publications. A more structured introduction and conclusion may help here.

Reviewer #1 (Recommendations for the authors):

– Regarding admixture dates, I suggest two analyses to tackle this possible issue. First, the authors may test how admixture date misspecification can bias AM estimation by using simulations as pseudo-empirical data, by setting an admixture time for the pseudo-empirical data that is largely different from the admixture time set for the simulations. Second, the authors could estimate admixture times in the observed data using the approach described in Zaitlen et al., Genetics 2017 (see also Korunes et al., G3 2022), and perform simulations with the corresponding admixture times, to train the neural network. A third, more demanding (but very interesting) option would be to co-estimate AM, SB and the admixture date using a deep neural network and the ancestry tract length distribution.

– Regarding local ancestry errors, could the authors compare the MSE of SB and AM estimation for pseudo-empirical simulated data where exact local ancestry is tracked (done already) and where local ancestry is inferred by RFMix from phased genotypes? This may be done for a small subset of models only, if the effect is minimal.

– Regarding the measure of uncertainty, could the authors report prediction intervals for their SB and AM estimates? This is particularly important, given the relatively low correlations obtained between estimated and true parameter values. Most intervals may include one.

– The authors report the composite likelihood ratio of the 1P vs. 2P models but do not test the significance of the ratio (probably because it is a composite likelihood) and do not assess how accurate is the choice between the two models. An option is to define a threshold for this composite likelihood ratio for which the probability to choose the true model is high, estimated from simulations and a confusion matrix.

– The Results section on the empirical data is somehow difficult to follow because no estimates of AM and SB are provided in the text. It is also missing some interpretation and discussion. If the authors are confident with their model choice, how do they interpret the higher fit for the 2P model for autosomes, relative to 1P model? Can the authors comment their results in light of previous findings (e.g., a positive SB value for ASW while negative in Bryc et al., AJHG 2015 and Ongaro et al., Genes 2021)?

Reviewer #2 (Recommendations for the authors):

I would love to see more data on the empirical ancestry inference, given that it's the input for the neural network and downstream analyses. It would be useful to have a figure that shows the continuous ancestry length profiles (and/or global ancestry proportion distributions) for all populations, potentially separated by males and females.

Could you include standard errors for the ancestry proportions in Table 1?

Can you add a supplemental table reporting the parameter estimates (either mean/variance or sex bias/assortative mating) from empirical data?

Can you specify what is being plotted in Figure 3? (I assume this is 95% confidence intervals and outliers but did not find this explicitly stated in the text.)

What was the rationale for a model where the second pulse occurs at generation 10?

Figure 4B is not referenced in the text and from the figure caption alone, it was unclear how the figure was constructed or how to interpret this result.

Are 1000 Genomes individuals used as reference populations in RFMix used again in downstream analyses? (In principle, I don't think there's a problem with doing so – was just unclear on the analysis pipeline.)

Does the extent of admixture impact the inference? For example, on average, 95.5% of the ancestry in ACB individuals comes from two ancestries, but ACB is still modeled as a 3-way admixture. It is promising that the mean squared error from simulations is similar between ACB and other populations, but I'm curious whether you've thought about modeling this as a 2-way admixture (and/or whether you'd expect the results to change if you did so).

I don't know what to make of the fact that strong assortative mating along one ancestry component (e.g. African ancestry in ASW) is not accompanied by strong assortative mating along any other ancestry component, especially in populations that are primarily by two out of the three ancestries. For example, in ASW, if males with high African ancestry are more likely to mate with females with low African ancestry, should this not automatically mean that males with low European ancestry are more likely to mate with females with high European ancestry?

Can you provide more details on the "joint parameter space" used to perform simulations and train the neural network?
