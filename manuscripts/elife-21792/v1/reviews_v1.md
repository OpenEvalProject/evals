# Peer review - Round 1

Editors:
- Lila Davachi, New York University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.21792.025](https://doi.org/10.7554/eLife.21792.025)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Multivariate cross-frequency coupling via generalized eigendecomposition" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and David Van Essen as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Christopher J Honey (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The paper nicely addresses an alternative method to measuring cross-frequency coupling, namely using a multivariate-components-based framework. The paper notes a number of challenges for existing analytic approaches and proposes and examines a new analytic framework named generalized eigendecomposition CFC (gedCFC).

The reviewers all agreed that the basics of the paper are novel, important and sound. However, they also all agreed that the paper was in need of an extensive rewriting coupled with some additional analyses to bring this to a level appropriate for eLife readership. Although we typically at eLife will provide a condensed list of essential revisions, in this case, I am appending the actual reviews below because they all nicely describe the needed changes.

Reviewer #1:

This paper reports results of various methods of applying generalized eigendecomposition to perform cross-frequency correlation analysis. The discussion in the Introduction seems to be too cursory to be of much benefit to those not already familiar with the idea, so depending on the purpose and target audience, some elaboration may be warranted.

There seems to be an error in the statement of the equation: SW = LRW (where L stands for Λ) – I think SW = RWL is meant.

I would humbly suggest giving an intuitive illustrative example in the Introduction to demonstrate the "maximization and minimization" effect referred to, perhaps using the Rayleigh coefficient framework.

The Discussion seems to be somewhat lacking in structure. It may be helpful to move some of the discussion in the corresponding Methods sections to the general Discussion section. The identification of different methods is interesting, but it would be nice to have a prior list of "general CFC contexts" in the Introduction, in which one would like to apply the GED framework, perhaps with simple examples of each case, then the methods description referring to the corresponding contexts, focusing on detailed description of the simulation/data used and method employed, followed by a more general discussion in the Discussion section.

I believe the paper could benefit from a quantitative report of the resulting covariances obtained with the covariance matrices, e.g. the theta and gamma template vectors with each of the two covariance matrices used in the method, as well as the generalized eigenvalue. And it would be of use to know the relative power in the high and low frequency bands used in the simulations, with some corresponding discussion of minimal relative power necessary e.g. gamma, to obtain interpretable results, and the applicability of the required power levels assumptions to real data, e.g. EEG.

The paper is likely to be useful for specialists working in the area, but if a wider audience is intended, a more generous introductory section and structured Discussion section would be helpful.

Reviewer #2:

The goal of this paper is "to highlight that significant insights into the neural mechanisms and implications of CFC can be gained by expanding the repertoire of data analyses, as well as theoretical conceptualizations, from a single-electrode-sinusoid-based framework to a multivariate-components-based framework." The author notes a number of challenges for existing CFC approaches include non-stationarities and sharp transients in signal, non-uniform phase distributions, and the fact that CFC sources and targets are spatially distributed and potentially overlapping. To address these challenges they propose a new analytic framework named generalized eigendecomposition CFC (gedCFC). Although the method proposed is very promising, the manuscript reads more like a proof of principle than a convincing demonstration. This is not because the framework is flawed, but because the range of applications discussed (5 different settings) leads to a lack of focus, and so the strengths and weaknesses of the framework are not clearly enough tested and reported within each setting.

1) The paper describes five methods for characterizing changes in spatiotemporal properties of brain data, using a common linear algebraic formalism. On the one hand, the range of methods is valuable because CFC measures are applied in a range of contexts to address a range of hypotheses. However, this also means that manuscript lacks conceptual unity and focus. For example, it is not entirely clear which of the 5 methods are solutions to which of the problems (e.g. non-stationarities, sharp transients, non-uniform phase distributions, etc.) with existing CFC methods. I would recommend:i) try to group the 5 methods into clusters with a common purpose (for example Methods 1 and 2 could be grouped), rather than simply using numeric labels;ii) assign names to the different approaches;iii) create a table which summarizes, for each method, the kind of hypothesis it is best suited for testing, which problems it solves, and which problems it does not solve;iv) for each of the claims above concerning the problems solved by gedCFC, please design a test that specifically demonstrates that claim. The manuscript already includes valuable demonstration examples that do perform this function, but it is not always explicitly specified which facet of gedCFC they are meant to test.

More generally, I found that the readability of the manuscript decreased from Method 3 onward, as more complex methods were introduced. In method 4 delay-coordinate embedding is introduced, just in passing, but this is a complicated and rich area of research. The investigation of how to choose the correct parametrization (e.g. number of time delays) in Method 4 could be a paper of its own. So, again, it is nice to see how the gedCFC framework can be applied, but the range of uses also limits the manuscript's depth and clarity.

2) Why compare gedCFC against methods, such as PACz, which are (according to the citations in the introduction) known to be flawed? The manuscript would be more compelling if gedCFC was compared against state-of-the-art methods (some of which are mentioned in the Introduction) and/or against the most successful of the methods reviewed in Tort et al. (2010, J Neurophys). In addition, when existing methods fail, it would help to specify precisely why they are failing. For example, it could be that gedCFC has, effectively, greater statistical power when applied to multi-channel data due to pooling of information across multiple electrodes, but it was unclear to me whether this was the core reason for its advantage over PACz.

3) "This alleviates the feature of principle components analysis that makes it suboptimal for brain data: components are forced to be orthogonal but neural dynamics (certainly at the meso- to macroscopic scale of LFP and EEG) are not orthogonal."

It seems unlikely to me that this undesirable feature of PCA – the fact that, e.g., the second eigenvector's direction is constrained by the direction of the first eigenvector – is truly absent from the gedCFC framework. Generally, there is a distinction drawn between (i) dimensionality reduction methods, such as PCA, which rotate data so that it can be compactly re-expressed; and (ii) source separation methods, such as ICA, which aim to identify statistically distinct generators within a mixed signal. Although in many cases PCA does approximate the function of source separation, this is not its goal, and the orthogonality assumption is a testament to the fact that compact expression is prioritized over source separation.

My (admittedly intuitive) impression is that the gedCFC framework is closer to a dimensionality reduction method than to a source separation method. Specifically, even though the components in gedCFC are not, in general, constrained to be orthogonal, this does not imply that (e.g.) the direction of the eigenvector of second-largest eigenvalue is unaffected by the direction of the eigenvector whose eigenvalue is largest. Consider the special case in which R^(-1)S is indeed symmetric: in this case, the eigenvectors are again constrained to be orthogonal and the well-known PCA problems return. So, should we expect PCA-like difficulties whenever R^(-1)S is near-symmetric? What is our guarantee that these issues do not arise even when R^(-1)S is far from symmetric?

The manuscript already presents some examples of cases where gedCFC successfully extracts signals from a mixture, but in these cases the mixed signals have different frequencies, so the filtering operations may be doing much of the work. To demonstrate that gedCFC really does not run into the interpretational difficulties seen with PCA, I recommend setting up a situation in which multiple signals (say 3) with similar spatial profiles, similar frequencies, and overlapping functional response profiles, are mixed – a case in which PCA should fail – and then show that gedCFC does not suffer from similar problems.

4) Because the model works by comparing a reference covariance to a target covariance, it assumes a binary transition between two modes. But how well would the model perform if the underlying generative process is actually changing continuously? For example if the generative model of gamma power is something like probability(gamma burst) ~ phase(theta), then a method that assumes a continuous variation as a function of phase will have far greater statistical power than a method which simply contrasts peak and off-peak data? Now, Method 3 may present an answer this "binary assumption" issue, because a continuous time-varying signal is convolved and included the model. But in this case, does not one not re-encounter the problem of non-stationarity and sharp transients, because now the estimation of the low-frequency envelope matrix, B, could be affected by these factors? Similar to the point I made in (1) above, I would like to see a more careful discussion of the strengths and weaknesses of each method, so that the manuscript explicitly describes for each method, which of the common challenges for CFC are overcome, and which are not overcome.

5) The paper would be more practically useful if it provided a slightly more thorough treatment of at least one of the statistical methods for testing components, and noted briefly any problems that may arise in this setting.

Reviewer #3:

This paper describes a novel technique to calculate cross-frequency coupling using generalized eigenvalue decomposition. The technique is novel and has several significant advantages that have currently not been clearly addressed, such as its independence of selecting electrodes and not assuming a sinusoidal shape. Moreover, the technique can be used in several ways (5 methods are described in the paper). The paper is well written; as I was reading it and wrote down questions, a subsequent section would often already provide an answer. Overall, I think the paper is of high quality and I only have a few comments that can be easily addressed.

1) It is not quite clear to me whether the method assumes that multiple electrodes have the exact same phase for an underlying rhythm. For example, if the method were to be used to analyze LFP recordings across motor cortex, with traveling β oscillations, where there is a shift in phase across electrodes, how would that reflect upon component waves?

2) It is said that the quality of gedCFC components is related to the quality of the covariance matrices, and a sufficient amount of clean data ensures high-quality covariance matrices. Can this be quantified: is there a way to compute from one of the data sets used in the paper how the amount of data used relates to the quality of the gedCFC components?

3) In method 3 example recordings from a human epilepsy patient are used with recordings of the medial temporal lobe and electrode Cz. Why would there be any coupling in these data? How does referencing affect the method? More anterior temporal lobe channels are also closer the face with potential muscle artifacts, which may not even be removed with bipolar referencing.
