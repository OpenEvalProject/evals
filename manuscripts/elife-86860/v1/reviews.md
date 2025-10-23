# Peer review - Round 1

Editors:
- Fred Rieke, https://ror.org/00cvxb145 University of Washington United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.86860.sa0](https://doi.org/10.7554/eLife.86860.sa0)

This study presents a fundamental and very technically strong dataset of mouse ganglion cells responding to natural stimuli that include more natural chromatic properties. Fits of convolutional neural networks to experimental measurements highlighted a novel form of color opponency in suppressed-by-contrast ganglion cells. More generally, the work provides a compelling example of how modern experimental and computational tools can be used to generate and test hypotheses about sensory function under natural conditions.


---

# Peer review - Round 1

Editors:
- Fred Rieke, https://ror.org/00cvxb145 University of Washington United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.86860.sa1](https://doi.org/10.7554/eLife.86860.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "A chromatic feature detector in the retina signals visual context changes" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Lois Smith as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

All reviewers were impressed by the technical aspects of the work. Three key issues emerged in review and were emphasized in discussions among the reviewers. First, the MEI consists of a single linear visual feature to represent a neuron's spatial and temporal stimulus selectivity. Such a linear feature cannot capture many key nonlinear aspects of retinal signaling (e.g. direction selectivity among many others). This limitation needs to be clearer in the paper. It is, for example, important that a reader does not come away thinking that the paper provides a general approach to identifying stimulus selectivity. Second, the MEIs in some ways resemble more standard measures of receptive field properties and in others differ strongly. A more complete comparison is needed of MEIs vs. standard measures, as well as a discussion of why they might differ (which could be related to the first main point above). Third, the paper emphasizes the possible role of these cells in horizon detection, but the analyses that support this role are based on ground-to-sky transitions, and the horizon itself was excluded from the stimulus set. Hence it does not seem possible to evaluate the role of horizon detection. It is important that discussions of ethological function are more grounded in the analyses provided in the paper.

Reviewer #1 (Recommendations for the authors):

Line 170-171: Suggest modifying the sentence "This established that …" to be more objective. It's not clear that a correlation of 0.5 supports that sentence.

Line 173: Isn't the linearized CNN equivalent to a straight linear filter model? If so I would state that – it's a simpler description. If not, I would clarify how it is different.

Line 357-359: What is the indication that the warping is in the color opponent region?

Reviewer #2 (Recommendations for the authors):

1. Line 856. Why were clips restricted to a certain mean intensity range, and how did this influence the analysis? The concern is that allowing a more natural range of means would then violate the sky-ground transition specificity, as cells might fire in a broader range of conditions.

2. Figure S2. Add UV / Green labels to the two grayscale maps as in Figure 4a.

3. Figure 2A. Number of channels should be added to the figure.

4. Figure 2A. 'Receptive fields' label is only indicated in the last layer but is defined by the whole network. This is confusing, perhaps for the last layer something should be labelled with something more specifically relating to spatial localization?

5. Figure 2A. Is the Kronecker (or 'tensor') product symbol really intended? If so, please state so in the legend and clarify in methods how this relates to convolution implementation. If it is just generally meant to be convolution, a different symbol should be used and stated. In other words, it helps understanding to be formally correct with symbols, with more formalized mathematics or physics usage preferred to less regulated machine learning usage.

6. Figure 2B. How can so many cells be above the maximum set by the cell's response reliability?

7. Figure 2c. A 'linear model' is stated, but from the methods, it seems like an LN model (the final threshold is still present). If it really is a linear model, this is an inappropriate straw man (a threshold should be included) but if it is an LN model, that should be stated correctly.

8. Line 240 -241. Due to "the fixed contrast budget across channels", the contrast of most MEIs is shifted toward the UV. Please explain what is meant by the fixed contrast budget and its effects.

9. Figure 4G. The block structure of Figure 4G is hard to interpret, because it is not clear what the expectation is. For many of the cells, the MEI is not the most effective input, not even for the model. Attention is focused on the one cell that has the most distinctive response to its MEI, but is this just a random occurrence? Some guidance clarifying the interpretation of this confusion matrix would be helpful, or whether it is just interesting but we are not supposed to have any real interpretation of it.

10. Line 255. If only 2/3 of the cells have color opponent MEIs, are they really a cell class? Does this call into question the classification approach or the MEI approach?

11. Related to the difficulties of the representation analysis, it is not clear what 'sacrifice' occurs in favor of chromatic discrimination. If cell 28 did not exist, some chromatic discrimination would be lost, but other cell types would still be there to represent other features.

12. Figure 7d. the retinal cross-section image is confusing. Due to retinal warping, the ChAT bands droop below the IPL boundaries indicated, and therefore the arborization level seen in the maximal projection is misleading. It would be better to use the ChAT bands to correct for warping at each spatial location so that the dendritic arborization could be interpreted.

13. Line 609. This section relates to a previous claim, summarized as 'the dumber the animal the smarter the retina'. This is regarded as a myth, and experimental evidence does not support this (see Gollisch and Meister, 2010 discussion, point 2). It would be better for the field not to revive this idea.

14. Line 624. There is a misstatement about how this paper contributes to 'how' a computation is implemented, as there is no mechanistic information here about the circuitry.

15. Line 871. Please make clear that the two channels are chromatic, and a different word should be used than 'channel' because the layer has 16 channels by the usual meaning.

16. Line 874. More detail should be given about the Fourier parameterization.

17. The limitations of the slow frame rate should be more clearly acknowledged.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A chromatic feature detector in the retina signals visual context changes" for further consideration by eLife. Your revised article has been evaluated by Lois Smith (Senior Editor), a Reviewing Editor and the three original reviewers.

All the reviewers agreed that the manuscript has improved in revision and appreciated the new data and analyses that were added. There are a few remaining issues that need to be addressed, as outlined in the reviews below. Most important is clarifying the limitations of the MEI analysis earlier in the paper. These are detailed in the individual reviews below.

Reviewer #1 (Recommendations for the authors):

This paper has improved with the new analyses and revisions added in response to reviews. These changes have clarified several issues, provided stronger evidence for others, and brought the results and text closer in alignment. A few issues have either emerged or been highlighted in the revision:

MEI and temporal tuning. The text at times could be read as saying that the MEIs reflect a better way to measure tuning properties. A concern about this terminology is the dependence of the MEI on the approach used to optimize responses (e.g. on the time window used in that approach). For example, the temporal frequencies that contribute to the time course of the MEI are quite low – likely reflecting the optimization procedure. One suggestion is to clarify in the section starting on line 204 that the MEIs reflect a combination of a cell's own properties and the optimization procedure (as you have already for the oscillations in MEIs for some cells).

Figure 6b, c: What do the contrasts beyond -1 or 1 mean?

Figure 6e, f: This cell does not look opponent, with both UV and green producing On responses. Is this the only cell this experiment was performed on? If not, were other cells more in alignment with the predictions from the model?

Figure 7i: The colors are hard to see and match to those in the rest of the figure. In addition, the gray bars and labels should be defined in the caption.

Reviewer #2 (Recommendations for the authors):

The paper has improved but still does not acknowledge its limitations sufficiently.

1. With respect to the difference between the MEI and the linear receptive field, there was no misunderstanding in the previous review, and the current manuscript still does not acknowledge the limitations of the MEI analysis. This point could have been made more explicit in the previous review, and so the following is an attempt to do so.

By analogy, in a topographic map of the world, the MEI is the location of Mt. Everest. The linear receptive field is a plane fit to the direction of the steepest ascent fit to the world map, additionally including an average slope. A Linear-Nonlinear model allows variation in height along that single direction. But a full understanding between the relationship between change in spatial position and height requires the full two-dimensional map.

In the retina, and in a CNN model of the retina, parallel rectified pathways create sensitivity to many more different directions in stimulus space, commonly referred to as features. Each separate interneuron with a threshold potentially creates a different feature or dimension, with firing rate and sensitivity varying in each point of the high-dimensional space spanned by the set of features.

Linear-Nonlinear models and MEIs only encode sensitivity to a single feature. However, multiple distinct features are required to produce a wide set of important phenomenon, including nonlinear subunits that cause sensitivity to fine textures, direction selectivity for both light and dark objects (On-Off), object motion sensitivity, latency coding, the omitted stimulus response, responses to motion reversal, and pattern adaptation (reviewed in Gollisch and Meister, 2010). All of these properties rely on multiple distinct features and their interactions. Any analysis based solely on an MEI necessarily abandons consideration of how sensitivity along these different features combines to produce a computation. The new Figure 6c, which examines two stimulus directions near the MEI is an improvement, but it is only two directions in one region of stimulus space.

There is substantial concern that readers will misinterpret the 'Most Exciting' input to mean the 'Most Important'. It would therefore serve the field for a clear statement to be made that analysis of MEIs alone (1) will not capture interactions of multiple nonlinear neural pathways, (2) therefore will not capture nonlinear interactions between multiple stimulus features, and (3) will consequently not explain the set of phenomena that rely on these neural pathways and stimulus features.

In response to the authors rebuttal, to clarify the nonlinear analysis that one might do beyond the analysis of MEIs to identify multiple dimensions, these would include Spike-Triggered Covariance (Fairhall et al., 2006), Maximally Informative Dimensions (Sharpee et al., 2003), Maximum Noise Entropy (Globerson et al., 2009), Nonnegative Matrix Factorization (Liu et al., 2017), proximal algorithms (Maheswaranathan et al., 2018), and model reduction approaches to reduce to the CNN model to fewer dimensions (Maheswaranathan et al., 2023) among others.

2. It should be made explicit for each analysis whether it is based on measured responses or stimuli presented to the model. In Figure 7, a proper signal detection analysis cannot be performed without accounting for noise on single trials. It is unclear whether analyzed responses are directly from data, or from stimuli presented to the model. For extrapolation to different speeds, these are clearly from new stimuli presented to the model. It should be stated that without accounting for measured noise, ROC analyses will overestimate detection of ground-sky transitions.
