# Peer review - Round 1

Editors:
- Brice Bathellier, CNRS France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.53462.sa1](https://doi.org/10.7554/eLife.53462.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study elegantly compares spatial organisation of frequency tuning in auditory cortex across two very different species, mice and ferrets, which had never been done. Beyond showing marked similarities between the two species, this work highlights the complexity of frequency receptive as a major factor contributing in two species to the apparent local disorganisation of the frequency map. This strongly reinforces the view, that irrespective of the species, auditory cortex not only implements a map of frequency but also builds elaborate representations of sounds likely useful for capturing the acoustic diversity of real-world auditory stimuli.

Decision letter after peer review:

Thank you for submitting your article "Complexity of frequency receptive fields predicts tonotopic variability across species" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Brice Bathellier as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Richard Ivry as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Daniel B Polley (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Using both calcium imaging and Neuropixel electrophysiology , this study shows that in ferrets, the tonotopic map is locally heterogenous, and that double and multi-peak tuning curves contribute more to tonotopic map heterogeneity than single peak cells. The study also shows that multi-peak cells have also a best frequency less attuned to the surrounding BFs in mice, but that double peak cells have the same degree of heterogeneity as single peak cells.

This paper provides a new important dataset, with the first two-photon imaging observations in AC in a carnivorous species, complemented with Neuropixel data. It also provides interesting analyses suggesting that the source of tonotopic map heterogeneity is the increasing complexity of frequency receptive fields in the auditory cortex, particularly in ferrets. The comparison of species (ferret vs mouse) is a strength of the study and the comparison of methods (single unit electrophysiology versus 2p calcium imaging) as well. The most interesting and surprising conclusion is that the ferret and mouse have comparable degrees of local heterogeneity in best frequency tuning. The main discovery of the paper – that the orderly arrangement of tonotopy in L2/3 predominantly arises from cells with well-defined tuning to a single of frequencies – has already been discovered at least twice before (Guo et al., 2012; Romero et al., 2019), but the study here confirms and extends this observation to a different species and with a slightly different analysis.

Yet there are several non-trivial – but solvable – problems with the data analysis that deserve careful consideration because they could affect many of the main conclusions. In addition, the reviewer noted several issues with the accuracy, clarity, scholarship and general writing style.

Essential revisions:

1) The point that double and multipeak cells are strong contributors to the local imprecision of tonotopic is convincing for ferrets, but less in mice. The discrepancy may be due to less precise frequency tuning in mice (broader tuning curves), which may lower the fraction of multipeak cells (as peaks would be less well defined).

It will be useful to compare tuning width in both species, especially for single-peak cells. Indeed, if we follow the authors' idea, that the more imprecision there is in the BF definition, the more likely it is to be far from the mean local BF, then tuning width would be an important factor.

For example, the authors could provide a graph for both species in which some generalized bandwidth (say the fraction of the frequency range above half max response) is plotted against distance to mean frequency. All three categories could be displayed in the graph so that one could evaluate if the broadly tuned cells in mice tend to be the one cells that are not following tonotopy.

2) Authors use both GCaMP6m and GCaMP6f. It is well known that GCaMP6f underreports spiking. How does this affect the observed tuning diversity? One would expect that the tuning diversity is similar to that of GCaMP3.

3) There is a need to improve the statistical criteria for determining whether a neuron was frequency-sensitive. The authors use a 2-way ANOVA with frequency and level as factors and label a neuron as frequency-sensitive only if there is a main effect for frequency or a significant freq x level interaction term. There is a concern about Type-II error because a neuron either with very narrow tuning (e.g. responds to only 1-2 frequencies) or a neuron with very broad tuning and low-threshold would quite possibly not be included in the analysis. Because only 20% of cells were found to be frequency sensitive, this deserves consideration, particularly because the most important factor in this paper is to contrast cells with very well-defined tuning versus cells with broad/complex tuning. Looking at Figure 1C, for example, it seems clear that they are excluding many cells with frequency sensitivity. It makes much more sense to include cells in the analysis based on whether they are responsive to the tone (e.g. a paired t-test of peak amplitude in the pre-stimulus baseline vs post-stimulus period across trials) and then break them down according to their frequency/level preference in the next stage of analysis.

4) There are some serious issues with the way BF variance is calculated.

4a) There is a problem with using the mean BF within the ROI instead of the median. The Tischbirek and Romero studies used the median, not the mean to avoid the high frequency artifact that comes from performing a linear operation (mean) on log2 data (BF). The authors should take the mean of the log2 BF values (to avoid high frequency BF artifact) or just take the median, which has the added benefit of being less sensitive to outliers.

4b) The bigger issue is that if they calculated variance as a function of number of neurons within the set I suspect you would find a main effect for the number of neurons (more variance with smaller number of constituent neurons). If so, this is a confound as the number of units co-varies with single vs double vs complex FRA types. The way to solve this would be to bootstrap the measurement using a fixed number of neurons (e.g., always three).

5) Measurement of sound-evoked activity. Is this measure averaged across all levels at BF or measured at the conjunction of BF and BL? If the former, it would also be confounded by the number intensities that elicited a response (i.e., would be impacted by thresholds or for O-type neurons).

6) The CSD is troublesome. Apart from a discontinuity at L1 (which might just be the pial surface) all is seen is one distributed current sink across layers. One should see an early current sink (i.e., negative value) in layer 4 surrounded by a current source in L2/3 and L5/6 that then flips in polarity with time after stimulus onset. This pattern has been seen in dozens of papers, at least when the CSD is measured as the second spatial derivative (it was not clear if this is what they did). Generally, either the Materials and methods are missing a description of filtering/smoothing methods that are typically used for CSD analysis or else the description was correct and the problem is that the analysis is incomplete. The authors should refer to papers by Lakatos and Schroeder, Metherate and colleagues or Guo and Polley for a more detailed description of data processing for CSD analysis.

7) The signal correlation measurement is not convincing. If two units don't share the same set of frequency/level combinations in their FRAs their signal correlations could be lower. Alternatively, if the sound-evoked activity rates are systematically lower, the signal correlations could also be lower. This muddies the interpretation of what the signal correlation finding means. Instead, the authors might consider identifying the frequency-intensity combinations that fall inside the FRA for every neuron. Then they can take a pair of neurons and calculate the fraction of shared freq/intensity combinations that they share as a function of distance. With this approach, they are at least measuring receptive field similarity independent of systematic differences in activity rate.

Also the signal and noise correlations may be better placed in the supplementary figures.

8) This is more of a presentation problem, but generally speaking the presentation of the mouse data feels rushed and superficial. No information is given on where the images are being acquired, nor are we given any indication of the image or signal quality as was shown for the ferret. It seems entirely possible to me that they are not recording from mouse A1. Some anatomical data that shows the GCaMP expression relative to known landmarks for A1 in the mouse (as described in Romero et al., 2019) along the lines of what is carefully shown for the ferret in Figure 1—figure supplements 1 and 2 would help alleviate this concern somewhat.

The bottom line is that the cross-species comparison is one of the most interesting points of the paper. Counting all of the supplements, we get around 10 figures on the ferret data and then just a single combined figure on the mouse and the cross-species comparison.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Complexity of frequency receptive fields predicts tonotopic variability across species" for further consideration by eLife. Your revised article has been evaluated by Richard Ivry as the Senior Editor, Brice Bathellier as the Reviewing Editor, and two reviewers.

The manuscript has been improved and all reviewers are satisfied with the clarifications provided. However there is one remaining issue that needs to be addressed before acceptance, as outlined below:

The revised manuscript benefits from many improvements. In their response to major issue #3 (pasted below), the authors missed the main point and instead chose to focus on the choice of the test. The main point was that it seemed like they were undercounting the number of neurons that changed their activity rates when tones were presented. Figure 1C bears this out in that plenty of cells below their significance threshold have visible tuning, so type II error (too conservative test) can be an issue. The authors should show to which extent relaxing the significance threshold / type of test (which always has some arbitrariness) to include more cells changes (or not) their conclusions. This could be done by including all cells, or maybe the cells that pass a simple t-test for baseline against response but pooling all sounds together, or by using any other evaluation of global signal-to-noise ratio and varying the threshold.

Previous comment:

"3) There is a need to improve the statistical criteria for determining whether a neuron was frequency-sensitive. The authors use a 2-way ANOVA with frequency and level as factors and label a neuron as frequency-sensitive only if there is a main effect for frequency or a significant freq x level interaction term. There is a concern about Type-II error because a neuron either with very narrow tuning (e.g. responds to only 1-2 frequencies) or a neuron with very broad tuning and low-threshold would quite possibly not be included in the analysis. Because only 20% of cells were found to be frequency sensitive, this deserves consideration, particularly because the most important factor in this paper is to contrast cells with very well-defined tuning versus cells with broad/complex tuning. Looking at Figure 1C, for example, it seems clear that they are excluding many cells with frequency sensitivity. It makes much more sense to include cells in the analysis based on whether they are responsive to the tone (e.g. a paired t-test of peak amplitude in the pre-stimulus baseline vs post-stimulus period across trials) and then break them down according to their frequency/level preference in the next stage of analysis.”
