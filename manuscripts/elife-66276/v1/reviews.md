# Peer review - Round 1

Editors:
- Dwight Kravitz, The George Washington University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66276.sa1](https://doi.org/10.7554/eLife.66276.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This manuscript utilizes intracranial ECOG data and multivariate computational simulations and modeling to explore potential changes in semantic representations within the human anterior temporal lobe (ATL). The study addresses some long-standing issues in the collection of data from this area and the corresponding analyses. Overall, this work highlights the extremely complex and dynamic representations that can form in cortical areas that receive a wealth and diversity of inputs. This manuscript will be of interest to neuroscientists and psychologists interested in how semantic information is encoded in the brain.

Decision letter after peer review:

Thank you for submitting your article "Evidence for a deep, distributed and dynamic semantic code in human ventral anterior temporal cortex" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Chris Baker as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Stephen J Gotts (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Multiple reviewers noted the lack of direct quantifications/tests for some of the claims that will need to be added.

2) Some attenuation of the claims about the ATL as a semantic hub (or at least more discussion) are likely appropriate given the restricted area from which data has been collected (limiting possible direct comparisons) and the alternative interpretations brought up by Reviewer 3.

Reviewer #1 (Recommendations for the authors):

The main problem here lies in the interpretation of the results due to the lack of direct tests of those interpretations. If the central claim is about the distinction between anterior and posterior ATL, there must be more direct tests of that difference. In the central claim is about the need to use dynamic multivariate models to capture the differences, then the results here should be compared with simpler models.

Put the plot of the anterior electrode decoding only on the same axes as the decoding presented in the main paper. Also add in the companion analyses of the posterior electrodes alone.

Reviewer #2 (Recommendations for the authors):

1) Please provide more information about dynamic coding in individual patients. For example, are the red electrodes in Figure SI-4 all in the anterior aspects of the fusiform gyrus? Alternatively, can you show code switching in the vATL classifier weights for single patients (with stable coding in pATL) (as in Figure 4E) ?

2) The authors use "category correlation" in multiple figures (e.g. Figure 1B; Figure 2D; Figure SI-4), although they do not explain in much detail how this correlation is actually calculated. Please give a better verbal (or mathematical) description.

3) The current model has a lot of "compression" in terms of units per stimulus learned (25 units vs. 90 stimuli). How important is that for the code switching in the Hub hidden layer? If you were to increase all of the hidden layers to 100 units each, does this tendency decrease? As the current network tries to map similar visual inputs to dissimilar verbal outputs, it will benefit from strong attactor dynamics. It seems like the benefit will be amplified with a greater amount of compression in the hidden layers, forcing units to code 2 to 3 domains of stimuli. Is there an alternative argument as to how such compression might happen in the brain, as opposed to the network? (e.g. weight decay with effectively no limit on unit number). The context of this question is that there are many more neurons in a given brain region than the number of objects that humans know. If this variable does matter, perhaps it should be added to SI-1 ?

Reviewer #3 (Recommendations for the authors):

1. The methods need to be greatly improved. (1) It isn't clear to me what exactly the inputs are to the network. Is the input static (on/off) or also dynamic? This should be shown in Figure 2 (2) I found it hard to determine what was done for many things (methods). Examples: It is never explicitly stated what is decoded (living vs nonliving), what features of the LFP are used (raw voltage?)

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Evidence for a deep, distributed and dynamic semantic code in human ventral anterior temporal cortex" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Chris Baker as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Stephen J Gotts (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

1) There are a few outstanding considerations to be addressed in the manuscript regarding the statistical measures (see esp. Reviewer 2). These issues need to be clarified/corrected.

2) There remains a conceptual problem that needs to be addressed as well. Both reviewers have expressed some concerns with the strength of the central claim on conceptual grounds. The distinction between living and non-living is ultimately binary and a graded distinction would be stronger. If such a characterization is not possible, it must be acknowledged and the central claims attenuated.

3) There is a concern about the use of raw voltages as opposed to gamma, which can be addressed either by presenting a gamma analysis or simply attenuating the claim that motivates the already presented analysis.

Reviewer #2 (Recommendations for the authors):

The authors have responded well to most of my comments. However, I do have some follow-up comments on the new statistical analyses that they provide (in response to both my comments and those of the other reviewers). These comments pertain mainly to the results shown in the panels of Figure 5:

1) In panel 5A, the authors do not appear to correct for multiple comparisons (as they did in Figures 3B and 4B). Rather than the conservative Bonferroni correction used in other analyses, I think False Discovery Rate correction would be fine here (and note that it would not require non-overlapping classification windows, since positive dependence is permitted). The point of this analysis is to show local temporal generalization, so if it's still the case after correction that the best classifier performs significantly better than others in its preferred time window (which I strongly suspect will be the case), I think the point is made.

2) In panel 5B, the authors have evaluated the relationship between 'Classifier fit time' and 'Proportion of processing window reliably decoded'. However, the choice of a cut-off time for a piecewise linear fit (0-500 ms) is not independently motivated. The degrees of freedom for the correlation test are also likely to be incorrect, since the classifier windows used are overlapping (50-ms windows advanced each 10 ms). The authors should use a more automated method (rather than visual inspection) to choose the time cut-off, and they should at least use non-overlapping windows (as done in Figures 3B and 4B) to ensure that the adjacent classifier measures are statistically independent of one another.

3) In panel 5C, the authors have partly responded to one of my prior comments (asking whether or not the variable anterior coding versus stable posterior coding is reliable in individual subjects). However, there are two ambiguities present in the current analysis: i) The authors have not clarified whether each subject contributes data to each decile bin of electrodes along the y-coordinate axis, and ii) as in comment #2 above, the degrees of freedom for this test are likely incorrect. We don't know whether adjacent electrophysiological measures are statistically independent or not (and most would probably assume not). I see 2 possible solutions: i) the authors could calculate a slope of y-coordinate on 'Variance of coefficient change' for each subject and then calculate a one-sample t-test versus 0 across subjects on these slopes, or ii) the authors could instead use permutation testing on the slope as currently calculated (by randomly permuting the deciles of the y-coordinate, recalculating the slope each time for 1000 iterations or more); the actual slope could then be tested against the permuted null distribution to derive a p-value.

Reviewer #3 (Recommendations for the authors):

In this revised version, the authors made minor changes to the text and added statistical tests to support the key claims.

However, my major critiques the authors did not address: showing evidence of a semantic code (as opposed to the simple binary decoding) and usage of the raw voltages. Due to this I can’t see how the broad claims made are supported by this analysis.

First, while I recognize that the 'living vs non-living' distinction is used extensively in the literature for behavioral studies, I cannot see how one can conclude that a representation that allows this kind of decoding forms a 'deep semantic code'. To me these claims seem much too broad and would require much more extensive evidence to support (something like done in Huth et al. 2016, which rightly claims a semantic code). If something really is a deep semantic code, it must support encoding of many different semantic features (at different levels of abstraction, thus the deep) rather than just one. To jump from a simple binary distinction to a 'deep semantic code' is in my opinion not supported by the analysis presented here.

Second, the assertion added to the main text that raw voltages (iEEG voltages, not LFP as claimed here) are the 'closest analog to unit activity' is simply not true. There is ample evidence that gamma-band power correlates with firing rates (i.e. Nir et al. 2007) in many brain areas (which in turn correlates with the BOLD signal). But there is no evidence that firing rates correlate with ERPs in these brain areas. Indeed ERPs are largely a reflection of synaptic activity and not local unit activity. As such it is unclear what is analyzed here is reflective of processing occurring in the areas under the electrode rather than reflecting input from somewhere else.
