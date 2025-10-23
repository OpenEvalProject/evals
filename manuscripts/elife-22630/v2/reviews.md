# Peer review - Round 1

Editors:
- Upinder S Bhalla, National Centre for Biological Sciences , India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.22630.022](https://doi.org/10.7554/eLife.22630.022)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Complementary codes for odor identity and intensity in olfactory cortex" for consideration by eLife. Your article has been favorably evaluated by a Senior Editor and three reviewers, one of whom is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal his identity: Dmitry Rinberg (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors record ensembles of individual neurons in the anterior piriform cortex of awake head-fixed rats using polytrode probes, while changing identity and concentration of different odorants. They investigate possible coding strategies for odor identity and intensity, and propose that two different codes – a rate code (for identity) and a time code (for intensity) are used in a multiplexed fashion to extract these stimulus features. All reviewers agreed that the study was potentially a valuable advance in our understanding of odor and concentration representations in the piriform cortex. They felt that the data analysis and presentation could be strengthened.

Essential revisions:

1) The authors should analyze the concentration coding using a formal model that quantifies fit and confidence. This should address the observations of latency, inhibitory contributions, and synchrony.

2) The classifier analysis should be should be extended to establish whether the coding is sparse.

3) The authors should revisit the temporal analysis and conclusions, and clearly state how strong is the confidence in them.

4) Some details of methodology need further elaboration: e.g., analysis, bulb recordings, and unit isolation.

The outcome of the analysis above may suggest that the claims in the title should be reconsidered.

Additional specific comments are also indicated in individual reviewer comments below.

Reviewer #1:

This is a systematic and large study of single-unit activity in anterior piriform cortex of awake mice. The authors examine odor response patterns for monomolecular odorants. This is a valuable dataset as it covers many neurons, in awake animals, and over several odors. Consistent with previous data, the authors find a spectrum of response strengths, precision, and selectivity.

The authors have a key result on concentration-dependent coding. This is valuable but could be sharpened. There is quite a bit of data here, which is potentially very informative, however the analysis could probably be taken a bit further.

Then the authors pursue an analysis of concentration-dependent latency. There are two aspects to this, both of which could be strengthened.

1) First, can the concentration-dependence be explained simply by bulbar concentration-dependent latency? To their credit, the authors have directly recorded and shown the bulbar concentration-dependence. At present it isn't clear if the piriform is doing any substantial transformation of the response.

2) There is a nice experiment wherein the authors investigate the mechanisms behind concentration coding by optogenetically targeting inhibitory interneurons and delivering light pulses to identify the neurons from the recorded dataset. They characterized the responses of these neurons. Using this, the authors seem to have an implicit model whereby the inhibitory timing in the piriform acts to separate out the second peak in excitatory neurons from the first one. This implies that concentration dependence of the inhibitory peaks (Figure 6G) should account for the shift in second peak timing for the remaining cells (Figure 6H, Figure 3J and K). Does such a model work? Does it improve on the already present concentration-dependent latency response from the bulb? Whether or not my interpretation is what the authors had in mind, it would be useful for the authors to make their response model explicit, and test it.

Reviewer #2:

Bolding & Franks in 'Complementary codes for odor identity and intensity in olfactory cortex' record ensembles of individual neurons in the anterior piriform cortex of awake head-fixed rats using polytrode probes, while changing identity and concentration of different odorants. They investigate possible coding strategies for odor identity and intensity, and propose that two different codes – a rate code (for identity) and a time code (for intensity) are used in a multiplexed fashion to extract these stimulus features. Consistent with previous reports, the authors find sparse odor representations in the cortex. Individual responsive neurons were unambiguously suppressed, or activated, and only on rare occasions, the same neurons showed both types of responses. Across a 30-fold concentration range, cortical neurons had diverse and non-monotonic responses, more neurons becoming suppressed with increases in concentration. The latency of the early responding principal cells (within 100 ms from odor onset) was generally not affected by changes in concentration, while late responders showed decreased average latency with increasing concentration. Expressing ChR2 in inhibitory interneurons (VGAT+), enabled the authors to determine that their response latency decreases with increasing concentration. Using three coding strategies (ensemble membership, summed spike count and binned spike count), the identity and concentration of odorants could be extracted with high accuracy by pooling together the ~450 recorded neurons. On average, for same number of cells included in the analysis, the decoding accuracy was higher for odor identity vs. intensity. Using a time-based coding strategy (binned spike count) substantially increased accuracy compared to a rate code (summed spike count) for intensity decoding, and only to a less degree for identity decoding. Using either an expanding or a sliding window strategy, the authors find that identity decoding accuracy is highest early after stimulus onset (~100ms), while intensity decoding accuracy is poor to begin with and steadily increases over the next 100 ms.

In my opinion this is a very interesting study that brings novel, and exciting information about cortical neurons responds to changes in odor identity and intensity. The experiments are carefully executed, and the data appears rich and of high quality.

However, I disagree with the current interpretation of the results and main message of the manuscript, as described by its title. I think the data presented here does not support some of the central claims made by the authors. I will explain below my concerns.

The claim for a temporal code to extract odor intensity is weak. The main result plotted in Figure 4C shows that the binned cumulative curve reaches higher accuracy with fewer cells compared to the summed count, or ensemble membership coding. However, even for identity decoding, the trend is the same (superior accuracy for binned spike count). The claim rests on the observation that including temporal information only marginally improves identity decoding but substantially improves intensity decoding. But to begin with, the classification accuracy for odor identity is superior for the same number of included cells, perhaps leading to a ceiling effect.

To support a strong claim regarding the existence of two complementary and multiplexed codes in which odor identity is represented by specific ensembles of odor responsive neurons (using a rate code) and odor intensity is encoded using spike time information, the evidence in the data has to indicate that a rate-code is better for decoding odor identity and a time-code is superior for concentration. Importantly, the authors find, in fact, that including timing information increases the performance for decoding both odor identity and concentration. So, why not conclude that time-based code is superior to rate-based one for decoding both concentration and identity?

To my mind, the data presented here indicates that the accuracy of concentration decoding (as assessed by this classifier) is poorer than odor identity decoding in the piriform cortex. However, accuracy of classification for both stimulus features can be improved by including time information.

The authors observe that the latency of early responding cells remains invariant to changes in concentration. In principle, this could be an important component of coding odor identity, irrespective of concentration. It suggests that temporal information (lack of change in response latency) is important for coding odor identity, since the early responding cells provide an invariant reference to a potential downstream decoder. Furthermore, this finding, together with changes in response latency of later responding cells imposes certain constraints on the validity of theories in the field on primacy coding for odor identity. To my mind, this is an important observation that is unfortunately not clearly emphasized in the current version of the manuscript.

Reviewer #3:

This manuscript by Bolding et al. provides an account of odor representations in piriform cortex using electrophysiological recordings. The manuscript demonstrates that both odor identity and concentration information is encoded in this network. Through the use of linear classification of neural activity vectors, the authors compare potential coding schemes that may be used by the brain to decode odor identity and make the case that odor identity and concentration information are best encoded using different schemes. Odor identity information is encoded well with a "membership" code that eschews fine temporal and spike count information, while temporal information is much more useful for decoding concentration. By classifying cropped activity vectors, they demonstrate that concentration information in their recorded population is available later following inhalation than information needed to decode odor identity. Finally, the authors demonstrate that inhibitory network elements are responsible for attenuating late responses, which they claim increases synchrony with increases in odor concentration.

Overall this work is an important addition to our understanding of olfactory cortex and it coding schemes. However, I have some issues that I feel must be addressed before it is published.

1) Classifier analysis is used to build an argument that late representations contain more concentration information. This argument is true only for the authors' recorded units and using linear classification. While this methodology is sufficient to demonstrate that information is present within the network, it is not sufficient to prove the absence, or relative absence, of information in the network. The authors should discuss this in the manuscript.

2) Piriform cortical representations are sparse. Thus at least two factors need to be considered in the analysis. First, the authors demonstrated that early activity is useful for generalizable odor identity by training the classifier on 3 concentrations and testing on the left-out concentration. Using this training/testing paradigm, a linear classifier will weight stable dimensions (i.e. neurons) over dimensions that are unreliable across concentrations. Only a small subset of neurons may be encoding odor identity despite large variance within the population. Can authors provide an analysis of the degree to which their classifier is using sparse weightings in this task? Can they identify the best performing neurons?

3) Second, the authors presented the dependence of the classifier performances as a function of number of neurons, n. The classification analysis may not accurately represent the information contained in the population. It is possible that a discriminator with input from specific combinations of n neurons performs much better than an average performance of a discriminator for the same number of neurons. What is the distribution of the discriminator performances for a given number of neurons? How the dependencies on the Figure 4 change for the best (or almost the best) n performing neurons, but not for average subset of n neurons.

4) While I agree that the fitting of a mixture of 3 Gaussians to the latency data looks reasonable by eye, I would ask that the authors provide more formal model comparison to justify the model and the number of mixed Gaussians. Once this is established, the authors should provide some estimate of the confidence in the fit parameters, as this confidence is important in establishing how the latencies shift between the olfactory bulb and piriform and whether these differences are significant. Bootstrapping across units can be used to derive these statistics.

5) The authors find that concentration information in their recorded population of units is encoded later than that of identity. At the end of the subsection “Dissociating representations of identity and intensity”, they claim that this conveniently matches behavioral observations from Abraham et al. Such a comparison of discriminant performance with a behavioral result seems like a stretch – the cited paper attributed the longer reaction time to the difficulty of the task, rather than to a difference between identity and concentration discriminations. In addition, the authors may consider citing Resulaj 2015, which reported very fast concentration discrimination.

6) More description of the methods used in analysis would be helpful. Latency determination for neural responses should be described, especially given that many of these neurons' firing rates are non-stationary within the sniff cycle. Also, PSTH convolution methodology is not described well – uniform kernel or Gaussian? Are non-overlapping (invalid) portions of the signal discarded, and if so are the timings adjusted for the shift that this would incur?

7) No methodology for olfactory bulb recordings is given in the manuscript. Some statistics should also be provided about the recorded population (i.e. recording depths, number of units recorded).

8) The authors provided an argument that inhibition is responsible for an increase of synchrony in the network (Figure 6). I did not understand this argument. My impression was, that the authors demonstrated that inhibition attenuated the later response, thus making the earlier response more temporarily confined. How does this lead to increase of synchrony in early response?
