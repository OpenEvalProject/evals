# Peer review - Round 1

Editors:
- Alex Fornito, Monash University Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62324.sa1](https://doi.org/10.7554/eLife.62324.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper develops a new approach to disentangle various noise contributions, arising from different sources of non-neuronal physiological fluctuations and head motion, to functional magnetic resonance imaging signals. This work also shows that controlling for these different sources of noise improves the accuracy with which the imaging signals can be used to identify people, demonstrating that neuronal activity makes a large contribution to individual differences in patterns of inter-regional functional coupling.

Decision letter after peer review:

Thank you for submitting your article "Physiological and motion signatures in static and time-varying functional connectivity and their subject identifiability" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Timothy Behrens as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Both reviewers agree that the manuscript is well-written, thorough, timely, and useful. The authors use various motion and physiological traces to generate surrogate datasets reflecting their contribution to network properties and evaluate how these surrogate data compare to the empirical BOLD network properties measured after different levels of denoising. A strength is the systematic characterization of major physiological and head motion effects, along with widely used fMRI pre-processing pipelines, using a large set of subjects from HCP. While it is generally hard to tell whether a pipeline is reducing nuisance effects without also removing neural signal, consideration of both (i) similarity to nuisance patterns, and (ii) changes in fingerprinting accuracy present informative metrics.

Essential Revisions:

A limitation of this work is that the contributions of various noise sources are determined using zero-lag correlations between motion/physiological and BOLD time series. It is well documented that fluctuations in respiration and motion lead to delayed changes in the BOLD signal that can occur several TRs later, and which can persist for periods that extend beyond the duration of the physiological/motion event (Power et al., NeuroImage, 2015; Power et al., NeuroImage, 2017). This has limited the efficacy of traditional regression-based denoising methods such as RETROICOR (Power et al., NeuroImage, 2017). While the authors have developed a method for convolving these signals with appropriate response functions to obtain the SLFO measure, it is difficult to determine the degree to which this signal captures the key phenomena of interest. The same can be said for motion estimates. It would be very helpful to see examples of individual subjects, with key nuisance traces shown above carpet plots. This would allow readers to ascertain whether the proposed approach accurately captures noise contributions to the BOLD signal.

For evaluating preprocessing pipelines, the primary metric used here is the (dis)similarity between the resulting correlation matrices and those of the nuisance (physio, motion) profiles. Although this is a reasonable approach, it is not clear whether it leads to a more accurate quantification of neural patterns, as the authors also acknowledge. Support is provided by examining the associated fMRI fingerprinting accuracy. A complementary approach, which may further strengthen the claim, could be to compare the post-correction matrices of a high-motion (or high physio) subset of subjects against the raw FC matrices of a subset of subjects that had low motion (or physio) effects to begin with.

To test the significance of each nuisance process in its contribution to BOLD, a surrogate dataset was constructed by permuting the nuisance signals across subjects. It seems like the shuffling procedure was only performed once (for a given nuisance process), and a t-test was performed between the permuted and actual values within each brain region. It may help to shuffle multiple times and pool the results to construct null distributions.

Moreover, the method for generating surrogate data adds Gaussian noise to the estimated nuisance signal contributions. Gaussian noise is not a realistic benchmark for fMRI data and is likely to under-estimate the correlation between the surrogate and empirical data. An autocorrelated process may be a more appropriate choice here.

Could the addition of model-based regressors help to reduce physiological effects in the FCD analysis? In addition, while the FCD analysis focuses on pairwise correlations between time-windowed patterns, it doesn't consider how the patterns themselves are changing as a result of different processing steps. The authors might consider some analysis of the windowed FC patterns, such as summary metrics of their similarity to SLFO profiles.

The Discussion (3.4) mentions that overall, the benefits of GSR may outweigh the possible loss of neuronal signal. Although GSR improves connectome fingerprinting for several of the pipelines, the Results mention that GSR produces negative correlations with the SLFO profile for some scans. I might suspect that for scans in which SLFOs contribute strongly, GSR can help; whereas for scans in which physio is fairly constant over time, GSR is more likely to remove neuronal signal or induce artificial negative correlations, since the GS would contain a larger proportion of neural BOLD. I'd suggest including some discussion of these points in section 3.4.

While GSR is shown to substantially reduce SLFO effects, it has been shown that different brain areas have heterogenous responses to low-frequency physiology (e.g. JE Chen et al. NI 2020), suggesting that a single global regressor may not be the most effective. The authors may wish to provide some discussion of this point in the context of the current findings.

It is noted (p. 9) that GSR tended to cause more negative correlations when performed in volumetric, as opposed to surface, space. It would be helpful to provide some discussion about why this may be the case.

There are 25 regressors in the noise model. To what extent are these collinear?
