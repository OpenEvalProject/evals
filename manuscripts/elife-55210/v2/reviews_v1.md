# Peer review - Round 1

Editors:
- Karel Svoboda, Janelia Research Campus, Howard Hughes Medical Institute United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55210.sa1](https://doi.org/10.7554/eLife.55210.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper presents a clever high-resolution imaging approach to measure spatial aspects of vesicles release at central synapses. Using a deconvolution approach the authors can distinguish single-vesicle and multi-vesicle release events. The key finding is that release events are inhomogeneously distributed across the active zone. Multi-vesicle events share release sites with single-vesicle events, and are more frequent at the center of the AZ, where the release probability is highest. This study provides an unprecedented view of spatial aspects of synaptic vesicles release.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Spatiotemporal dynamics of multi-vesicular release is determined by heterogeneity of release sites in central synapses" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation between the reviewers. Based on these discussions, we regret to inform you that your work will not be considered further for publication in eLife.

The reviewers and editor were excited by the approach and some of the data. However, the study is at a relatively preliminary stage and it is unlikely that the additional data and analysis required can be accomplished in two months. The eLife policy is to reject a paper under these conditions.

The mechanisms of release have often been studied with electrophysiological methods. However, these methods average over synapses, washing out interesting fluctuations that are informative about the function of single synapses. Over the last two decades a variety of postsynaptic and presynaptic imaging methods have been developed to look at synaptic transmission at single synapses. Some methods have high SNR and can be used for studying synapses in intact tissue (i.e. calcium imaging), whereas others (e.g. synaptopHluorin) promise better time resolution and spatial resolution, but are typically used in reduced preparations. The current study uses imaging synaptopHluorin to track single release events at individual synapses. The paper reports multi-vesicular release, with the dominant release site closer to the center of the active zone (AZ). Release probability was highest at the center of the AZ and dropped off towards the edge. This gradient, and spatial features of MVR, were similarly tightened by buffering intracellular calcium.

This is a nice imaging paper on vesicle release at single synapses. All reviewers agreed that the study is potentially very interesting, but don't find the data set and quantification convincing in their current state.

Essential revisions:

1) The paper has to be reframed. The Introduction might have been appropriate in the late 1990's, when UVR ("one bouton, one spike, one quantum") was a reasonable hypothesis based on prior work. Obviously, UVR was interesting in principle because it would pose serious biophysical riddles. If one vesicle releases, what signal tells other docked vesicles not to release? This signal would have to travel over microsecond timescales. The UVR came from work on the NMJ (misunderstood in this context) and, famously, the Mauthner cell. The original data has been reanalyzed and the statistical analysis has been questioned (some would say debunked, see Ninio, 2007, J. Neurophysiol.).

At central synapses support for UVR was always very spotty. In contrast, imaging studies with single synapse resolution tended to show MVR, as did many excellent electrophysiological studies using more indirect analyses. Yes, individual synapses often release single quanta, but this is because their overall release probability is often low. Under conditions of elevated release probability quanta are released based on the binomial model (e.g. Oertner et al., 2002; reviewed in Rudolph et al., 2015). It seems there is no evidence for UVR left and the whole thing is best forgotten except as a lesson in science sociology.

This means that MVR and UVR are likely the same process (operating independently at release sites/docked vesicles with different individual release probs). The authors have demonstrated that sites that host MVR could also harbor a UVR event later. This interchangeability actually suggests that they may be similarly regulated. In fact, none of the reviewers see support for a difference in spatial or temporal profile between MVR and UVR. Please analyze the distributions of time intervals for a UVR occurring at sites of an MVR, an MVR occurring at sites of an MVR, a UVR occurring at sites of a UVR, and a UVR occurring at sites of a UVR to see any difference. In Figure 1I the authors did not classify UVR into distal UVR and proximal UVR, as they did for MVR. This may have biased the comparison.

2) The authors concluded that they observed desynchronization of MVR events based on the ~8-10% difference in fluorescence intensity profiles of doublet events. However, from Figure 3A, the difference in the peak fluorescence intensities of two events is surely larger than 25%. Given 40 ms exposure time, it is hard to believe that ~4 ms of desynchronization generated such a large difference in fluorescence intensities. Moreover, if it is truly due to desynchronization, we would expect that the fluorescence intensity profiles of two events reversed over the next time point. Please explain.

3) Related to above. The second main finding is a desynchronization of MVR, with the more central release site leading and the peripheral site lagging by up to 4 ms. This evidence is indirect (via amplitude) and somewhat unconvincing (see above). How do we know that the amplitude difference is due to timing and not due to other factors (cleft pH, out-of-focus release, vesicle size etc.)?

As discussed in the 2017 Neuron paper, AZs may be tilted relative to the imaging plane, which could also affect the measured amplitude of distal events. Given these alternative explanations, it would be reassuring to have confirmatory evidence for delayed release events. A 4 ms delay is huge, twice the typical synaptic delay. Such delayed events, even if rare, should be readily visible in voltage clamp recordings. This is all a bit puzzling and needs to be explained better.

4) The authors argue that EGTA "affected the MVR event de-synchronization" and abolishes "the preferential localization of the earlier event in the MVR pair closer to the AZ center". In both cases, a significant difference under control conditions (Figure 3E, Figure 3C) was found 'non-significant' in EGTA (Figure 4B, Figure 4D). However, the number of analyzed synapses was more than twice as high under control conditions, which could account for the higher significance found in the t-tests. To compare t-tests of identical power, it may be necessary to conduct additional EGTA experiments. More importantly, the correct comparison is testing for changes in the difference between smaller and larger with and without EGTA. As is, the analysis is statistically flawed. This likely requires more experiments and analysis.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for choosing to send your work entitled "Spatiotemporal dynamics of multi-vesicular release is determined by heterogeneity of release sites in central synapses" for consideration at eLife.

Specifically, while the reviewers and editors found the manuscript much improved, they felt that a complete rewrite would still be necessary, and therefore this version still falls short of what is needed. One reviewer stated:

“In my opinion, the results strongly suggest that active zones close to the center of a synapse have a higher release probability than more distal AZs. This is an important and interesting finding that should be simple to understand. Unfortunately, it is (still) obfuscated by their MVR/UVR site classification, which they now partially take back ("our results cannot be interpreted to indicate that there are some specialized release sites that only support MVR or UVR"). But the confusion already starts at Figure 1A, where a release site is labeled in red (for MVR) that has in fact released only a single vesicle. So while it makes sense to talk about UVR and MVR events, it is very confusing to talk about UVR and MVR sites, only to state at the end that they are probably not fundamentally different. (Since typically only a single MVR event was observed per bouton, meaningful single bouton statistics is not possible). What is needed is a complete rewrite of the manuscript, including a change in nomenclature and analysis strategy, not just the addition of some text blocks.”
