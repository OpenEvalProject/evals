# Peer review - Round 1

Editors:
- Peter Kok, https://ror.org/02jx3x895 University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77599.sa0](https://doi.org/10.7554/eLife.77599.sa0)

This important work provides the field of human neuroimaging with a new method to estimate single-trial fMRI responses. The authors provide compelling evidence that their GLMsingle method goes beyond the current state of the art and leads to more reliable estimates. Therefore, this tool will be of interest to researchers using human neuroimaging to study neural responses in condition-rich designs, as is increasingly common in cognitive neuroscience experiments.


---

# Peer review - Round 1

Editors:
- Peter Kok, https://ror.org/02jx3x895 University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77599.sa1](https://doi.org/10.7554/eLife.77599.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "GLMsingle: a toolbox for improving single-trial fMRI response estimates" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Peter Kok as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Floris de Lange as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Benjamin Turner (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Including more practical guidelines on implementation would strengthen the manuscript and ease the implementation for users. This especially pertains to the features the user needs to flag when running the toolbox (HRF estimation, noise regressors, ridge regression). The specific implementation is left up to the users and the authors mention that this should depend on one's experimental goals, but do not provide more concrete guidelines. From the manuscript it seems that including all of the features works best, but this is based on two condition-rich experiments that may differ a lot from a user's dataset. Therefore it would be useful to walk the user through potential considerations for each of those features, or consider the most common uses of the toolbox (e.g. condition-rich designs, repetition-suppression studies, looking at within-session learning effects etc.).

2) There are some examples where the authors provide guidelines, but this could be strengthened. For instance, they discuss that the use of ridge regression could bias temporally adjacent trials to be more similar in magnitude – so they caution against using this feature for studies specifically interested in the relative responses of neighbouring trials (e.g. looking into preparation-execution in motor studies, repetition suppression-type of designs, etc.). But from Figure 4 there seems an advantage when including ridge regression in addition to denoising and fitting HRF, leading to a further reduction of the temporal autocorrelation between nearby trials. So, a reader might take-away that this is the least biased estimate of neighbouring trials. But mightn't it also destroy 'real' (neural) autocorrelation between trials, due to e.g. stimulus-specific adaptation and serial dependence? What exactly would the authors suggest then for designs where estimation of subsequent trials (e.g. repetition suppression or serial dependence) is of primary interest?

3) The authors use cross validation to determine the number of nuisance regressors to add in the model. Thus, any variability in responses to a single condition is considered to be 'noise'. How might this influence a potential use of single-trial estimates to assess brain-behaviour correlations (e.g., differences in behavioural responses to a single condition), or within-session learning conditions? For such uses, would the authors suggest instead using LSS or a subset of their features in GLMsingle (i.e. not using GLMdenoise)?

4) More generally, it would be ideal to see somewhere addressed the idea that variability is not always noise. You do mention repetition-suppression at one point, which is a clear example of this, but non-ergodicity as well as individual differences are further examples. There is no need to change the aims of the toolbox, which are clear and reasonable, but this somewhat tangential issue should at least be alluded to.

5) In the results, using a fixed HRF leads to drastically lower performance on a variety of subsequent measures compared to fitting an HRF to each voxel, especially as regards to β map test-retest reliability (Figure 2-3). Have the authors ensured that the HRF chosen is the most appropriate one for the region of interest? In other words, is the chosen HRF also the one that most voxels are fitted in the flexible option? It should be possible to quantify whether there is substantial dissimilarity in the chosen HRF from voxel to voxel. Since the HRFs span an equidistant arc, it would be expected that HRFs at opposite ends of the set are maximally dissimilar. Since the HRF has a biological interpretation, if it were frequently the case that neighboring voxels had dissimilar HRFs, this would be concerning.

6) It is a very small effect, but it would be interesting if the authors could speculate on the cost imposed by GLMdenoise in the very most-reliable voxels. Is this an artifact of the relatively small number of voxels that surpass this threshold? Or is there a chance the GLMdenoise step is removing signal? This refers to the rightmost point in the left plot of 3A (solid purple vs red; green vs orange). This is evident again in Figure 5B intra-NSD plot in the non-monotonicity from b2 to b3 for higher thresholds, and again when the b2 and b3 lines in Figure 6A (NSD) cross at r=0.25. Given that this does not seem to happen at all for BOLD5000, it is probably just an artifact, but seems nonetheless interesting enough for the authors to double-check whether there is any other explanation apparent in the data.

7) The benefit of b4 vs. b1 seems much larger in the NSD dataset than in the BOLD5000 dataset (Figure 2A). Is this because GLMsingle was initially optimised for the NSD dataset, or is there a different reason for this? The authors mention the fact that were fewer stimulus repetitions in BOLD5000 – but isn't that exactly the scenario for which GLMsingle was intended? Could it be due to the longer ITIs in BOLD5000?

8) The two datasets GLMsingle was tested on did not have a jittered intertrial interval (although the second one had a quite long (9s) intertrial interval). So, it remains to be seen whether there are also such large improvements when applying this method to a design with jittered intervals.

9) It would also be useful to include some intermediate results for the interested reader. As an example for the two chosen dataset, it could be instructional to know how many different hrf functions were obtained using FitHRF, how the ridge regression affects shrinkage of betas etc. The provided example in the toolbox (Python / Matlab) serves well to explore some of these intermediary steps, but some of these could also be explained in further detail as supplementary material. This would have a didactic purpose, informing the reader more about the process under the hood rather than just how the choices influence final estimates of betas.

10) Some relevant information on the amount of data from the two datasets could be explained in their Results section, specifically including number of conditions, repetitions per condition, and functional runs. It is not so straightforward to figure out this from the methods section given that the authors provide information on the datasets themselves, and then also the amount of the data used. Having some metrics in the main text would help to orient the reader and more easily allow a comparison of the results to the types of designs readers may be considering.

11) Researchers who study reliability often will complain about the use of Pearson correlation in that context. For completeness, the authors might want to at least look into this debate and decide whether it is worth addressing in the manuscript.
