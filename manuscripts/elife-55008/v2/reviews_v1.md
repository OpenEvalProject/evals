# Peer review - Round 1

Editors:
- Kenton J Swartz, National Institute of Neurological Disorders and Stroke, National Institutes of Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55008.sa1](https://doi.org/10.7554/eLife.55008.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Parker's pioneering work established that the initial responses to low concentrations of IP3 comprise Ca2+ puffs, wherein a few IP3Rs within an immobile cluster almost simultaneously open to evoke a local and short-lived cytosolic Ca2+ signal. It has been widely assumed that Ca2+ released by these events recruits further Ca2+ puffs (by Ca2+-induced Ca2+ release) to give global Ca2+ signals. It has, however, been difficult to examine this hypothesis because as Ca2+ puffs become more frequent, it becomes impossible to resolve them from background signal. The present work applies an elegant noise analysis method (the principles of which were described in a recent short report from the group in Cell Calcium) to assess the subcellular heterogeneity of Ca2+ signals evoked by IP3. The results are both unexpected and important in that they suggest that most cytosolic Ca2+ signals are not associated with the noise expected from Ca2+ puffs. The results convincingly challenge prevailing dogma by suggesting that Ca2+ puffs contribute only a small fraction the cytosolic Ca2+ signals evoked by IP3, with the remainder likely arising from openings of single IP3Rs. The authors have done an excellent job of revising the manuscript to address the technical concerns of the reviewers, and overall this is a rigorous, well done and significant body of work that justifies publication in eLife.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Inositol trisphosphate mediated Ca2+ spikes arise through two temporally and spatially distinct modes of Ca2+ release" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Colin W Taylor (Reviewer #1); Grant Hennig (Reviewer #3).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

The reviewers agreed that your work is interesting and has the potential to be quite important, but there were major concerns with the SD approach, on which most of the presented findings hinge, involving the dynamic range of the Ca2+ indicators and the spatial and temporal Ca2+ release patterns.

The first concern is that after uncaging or after the addition of agonists, the cytoplasmic background fluorescence in cells increases to a seemingly very high level. As punctate release events are only observed when background levels are low to moderate, it brings into question whether the Ca2+ indicators have become saturated at peak cytoplasmic background Ca2+ levels (the author's have previously assessed a variety of Ca2+ indicators with Kd values in the 150-400nM range). This would make it essentially impossible to resolve punctate events, even though punctate release events may still be occurring – akin to "signal clipping". While SD analysis may provide some additional resolution in situations with narrow dynamic fluorescence ranges, it still depends on the indicator having some dynamic range. This concern needs to be carefully addressed so that readers are confident that the presented findings are accurate and biological.

Some ways that could be used to examine the potential dynamic range issue of the indicators include:

• use a ratiometric indicator (Fura) to estimate actual cytoplasmic Ca2+ levels during uncaging/agonists which could be compared to Kd/saturation mM of Cal-520 and GCamP etc.

• pharmacologically limit the increase in cytoplasmic Ca2+ using low/moderate levels of EGTA (to preserve the dynamic range of the indicator) and examine whether punctate release patterns are still reduced after uncaging etc.

• purposefully increase cytoplasmic Ca2+ levels to near maximum with ionomycin then initiate an uncaging event to see puncate release sites can still be resolved (temporally synchronized release).

• use quantitative shape analysis (not ROIs) of transient bright regions at high cytoplasmic Ca2+ concentrations. At these levels where there is extremely limited dynamic range and greater shot noise, noise aggregates and punctate release sites will appear similar – but they can be separated using perimeter:area ratios (high for noise aggregates), or Gaussian fitting (better for release sites). This will require no Gaussian filtering of the data and some form of deconvolution to reduce the smoothing of objects due to Z-smear (where appropriate).

The second concern is discussed adequately in the reviews below, but questions whether the SD approach can detect synchronous, widespread puffs/ release events, or high frequency puffs/release events that appear and behave like changes in cytoplasmic background. It would be useful to the reader to see how different duration timespans affect the variance signal (which is currently tailored for the timecourse of individual puffs), to assess what range of Ca2+ behaviors are included or filtered by varying the space/time variance parameters.

Without additional information to address the major concerns of the reviewers, it is not possible to assess whether the work represents a sufficient advance to warrant publication in eLife.

Reviewer #1:

Parker's pioneering work established that the initial responses to low concentrations of IP3 comprise Ca2+ puffs, wherein a few IP3Rs within an immobile cluster almost simultaneously open to evoke a local and short-lived cytosolic Ca2+ signal. It has been widely assumed that Ca2+ released by these events recruits further Ca2+ puffs (by Ca2+-induced Ca2+ release) to give global Ca2+ signals. It has, however, been difficult to examine this hypothesis because as Ca2+ puffs become more frequent, it becomes impossible to resolve them from background signal. The present work applies an elegant noise analysis method (the principles of which were described in a recent short report from the group in Cell Calcium) to assess the subcellular heterogeneity of Ca2+ signals evoked by IP3. The results are both unexpected and important in that they suggest that most cytosolic Ca2+ signals are not associated with the noise expected from Ca2+ puffs. The results convincingly challenge prevailing dogma by suggesting that Ca2+ puffs contribute only a small fraction the cytosolic Ca2+ signals evoked by IP3, with the remainder likely arising from openings of single IP3Rs. The rigour and significance of the work justify publication in eLife; none of my comments should detract from that recommendation.

1) Figure 1 provides compelling evidence that noise decreases as the IP3-evoked Ca2+ signals develop and that a comparable increase in global cytosolic [Ca2+] evoked by ionomycin is “noise-free”, as expected for homogenous Ca2+ release. My understanding is that after some filtering and spatial blurring, most analyses calculate the SD for each pixel as a 160-ms (ie 20 frames) boxcar average. The original view posits that a global Ca2+ signal reflects most Ca2+ puff sites firing very frequently (perhaps 20 or so sites active at each instant), each spreading a µm or more from its source. Might this cause elevations in cytosolic [Ca2+] that are less noisy than the infrequent Ca2+ puffs observed initially, because each pixel would be influenced by Ca2+ reaching it from several puffs? It's perhaps too tall an order to require quantitative simulation of this on SD measurements, but it would be helpful to have the authors consider the issue explicitly.

2) From results in Figure 5, the authors propose that loss of Ca2+ from the ER causes puffs to terminate without appreciably abrogating the global increase in cytosolic [Ca2+]. That proposal would align with a long-standing, but contentious, suggestion that luminal Ca2+ supports IP3R activity, but it seems difficult to align with other work from this lab:

A paper from this lab and under review with eLife (Mak et al) proposes that luminal Ca2+ inhibits IP3R activity, such that loss of ER Ca2+ would be expected to enhance Ca2+ puffs.

Substantial evidence, much of it form this lab, indicates that individual Ca2+ puffs do not detectably affect ER luminal [Ca2+], since steps during the falling phase of a Ca2+ puff (reflecting channel closures) are of fixed amplitude. It is not thereby clear that the flurry of puff activity would cause the loss of ER Ca2+ proposed to terminate Ca2+ puffs.

The authors should discuss both issues.

Reviewer #2:

In this manuscript, Lock and Parker expand the ongoing work in the Parker lab to examine the temporal and spatial properties and their regulation of Ca2+ release by the inositol trisphosphate receptor (IP3R) Ca2+ release channel. They use HEK and HeLa cells to examine by TIRF microscopy (the primary approach here, and previously used extensively by this group) and light sheet microscopy, and a heavy dose of image processing abd fluctuation aanlyses, to address the issue of the sources of Ca2+ release and their mechanisms of transitioning from discrete Ca2+ signals, referred to as puffs, to global ones.

They find that IP3-mediated Ca2+ release is associated with a flurry of noisy events during the rising phase of the global Ca2+ signal that terminates before the peak of the global Ca2+ signal is achieved. They suggest that the noisy events are Ca2+-release events from IP3R clusters, i.e. Ca2+ puffs, on a background of IP3R-mediated more diffuse release. Using procedures to partially deplete Ca2+ stores, they conclude also that the Ca2+ puffs terminate because of depletion of the ER stores, although they cannot determine whether it represents local or global store depletion, whereas the diffuse release, from what they consider to be a separate population of IP3R from those in the Ca2+-puff inducing clusters, continue to release Ca2+. By measuring the rate of cytoplasmic Ca2+ concentration relaxation following a pulse of cytoplasmic Ca2+, they calculate the relative contributions of Ca2+ puffs (punctate release) and diffuse release during the rising phase and during the entire Ca2+ transient.

This is an elegant analysis and an interesting set of studies, and an not least of all because they address and challenge a major model of IP3-mediated local and global Ca2+ signaling (mostly developed by Parker); and because they address a conundrum in the field regarding the role and existence of "silent" IP3Rs that are localized throughout the cell but were previously (Parker; Taylor) considered to not participate. Here, the suggestion is that in addition to active IP3R in clusters near the plasma-membrane, these other IP3R channels might indeed be active and contribute to the diffuse release that continues after puffs have stopped firing.

I have a few comments that might suggest that the authors could clarify a few points.

1) Why aren't local release events observed in the raw ratio images, as Parker has described many times?

2) Figure 3—figure supplement 1 shows the sites with high standard deviation (SD) to be rather large, ~10 uM, a size that is inconsistent with the size of clusters of ~15 IP3R that generate the Ca2+ puffs. Rather their size suggests to me that these are entire regions of the endoplasmic reticulum (ER) that are near the plasma membrane in the TIRF evanescent field. If this is the case, are the authors selecting small sites within the large "contact" sites for the SD analyses? And, I would think that there is a "global"/homogenous signal at these sites that is contributed by Ca2+ that has diffused into these "contact" sites. This might also be consistent with the observation that the TIRF-detected high-SD signal terminates before the peak signal is achieved, because the peak is contributed by slow Ca2+ diffusion that persists after release has terminated.

3) The authors describe an inverted U relationship between the amplitude of the SD signal and the amplitude of the global response. What does it mean?

4) The authors conclude that elevated cytoplasmic Ca2+ doesn't inhibit the IP3R as a primary mechanism to terminate Ca puffs. Why doesn't it inhibit?

5) The authors examine the decay in cytoplasmic Ca2+ concentration after an elevation. They refer to this as sequestration. I'm not sure of their meaning. Although they suggest that the kinetics can be described by a single exponential, there must be at least two processes involved: sequestration by the ER, and extrusion by the plasm membrane Ca2+ pump. Indeed, in the discussion they use the phrase "efflux rate from the cytoplasm". I think what the authors mean to suggest in the sequestration away from the cytoplasm. If so, this should be stated more clearly.

Reviewer #3:

In this manuscript, the authors present a method that enables some resolution and measurement of small, punctate Ca2+ events in the context of global cytoplasmic Ca2+ levels. While previous studies used pharmacological tools to largely prevent global changes in Ca2+ in order to better reveal small discrete Ca2+ release events, the current study uses a variety of software routines that utilize fluorescence variance changes – from which punctate and global Ca2+ event behaviors are derived from. The authors surmise that punctate and global Ca2+ events are likely produced by 2 separate populations of IP3Rs. The experimental manipulations to investigate depletion of stores, Ca2+ entry, IP3R channel KO etc are well thought out and appropriate – but some concerns remain as to the ability of the authors to resolve puffs once background/cytoplasmic Ca2+ levels reach a certain intensity.

The use of signal variance to isolate different components of mixed fluorescence signals relies on those components having distinct (and variable) spatio-temporal signatures. However, if Ca2+ release events reach a steady state, then the variance technique becomes essentially useless. This is my main concern with some of the conclusions drawn from the analysis.

The ability to detect puffs is greatest during low background conditions, but the as global Ca2+ levels increase, the ability to detect puffs is hampered by i) closing of the max difference between background and puff sites and ii) an increase in the amplitude of shot noise that may start to mimick fast and small puff events. To resolve between genuine puff events, that are inherently Gaussian (1-2 µm) and random noise aggregates that occur during high background levels, is difficult – but is made worse by applying Gaussian filters to the data that reshape noise aggregates into more Gaussian shapes. Employing shape analysis before smoothing (perimeter:area ratios) is an effective way of resolving puffs (low P:A – smooth circles) even when surrounded by noise aggregates of equal intensity and size (high P:A – leafy looking). This may assuage some doubts as to the authors ability to resolve punctate events once background/global levels have reached moderate to high levels.

Similarly, the use of user-placed (or randomly positioned) ROIs based on visual inspection of bright spots in the videos is subjective and can heavily bias results to what the user wants to show. Many "hot spots" don't appear to have ROIs drawn over them and some ROIs appear to be sampling the same site. Small ROIs are more sensitive to spatial shifts in the position of the underlying fluorescent sites. The "flickering" variance may be a function of out-of-sync release events from a number of channels/clusters covered by each ROI. When these channels syncronize (in the open position?) or fluorescence sites increase in size, this will dramatically reduce the signal variance, even though puffs may still be occurring.

The shape of the cell and the distance and size of the cytoplasm located away from the evanescent field can dramatically affect the blurring of the background (cytoplasmic signal). How do the authors discriminate between "global" cytoplasmic changes and large puff sites that are heavily blurred being out of focus (see Figures 1 and 7). This effect still remains using lightsheet imaging.

The pixel resolution used during TIRF imaging was 0.5µm and is unlikely to fully resolve individual puffs, especially after smoothing. This may bias analysis to release events that are comprised of multiple channel clusters.

The use of black level subtraction can normalize absolute intensity levels, but does not compensate for the higher shot noise in areas with high static background. Was this taken into account?

Gaussian blur is reported as 2 pixels (in text) but as an SD of 2 pixels in the Materials and methods. What was the actual kernel size in pixels (3x3, 5x5?) and the SD.

Random ROIs were used for HEK cells devoid of IP3Rs. What does the data look like if the authors select the brightest spots in the 3KO video – or use random ROIs in controls?

Figure 3—figure supplement 3C appears to show a stochastic build up of high frequency events correlated to baseline increases – until background fluorescence levels may start to swamp out the ability to resolve small punctate events.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for choosing to send your work entitled "Inositol trisphosphate mediated Ca2+ spikes arise through two temporally and spatially distinct modes of Ca2+ release" for consideration at eLife. Your letter of appeal has been considered by a Senior Editor and the reviewers, and we are prepared to consider a revised submission.

The reviewers have also provided additional feedback below after reading your rebuttal to hopefully better convey the technical concerns.

Specific points:

1) Indicator Saturation/Clipping concerns:

In your rebuttal, you state (i) that "…maximal signal evoked by ionomycin is>2 fold higher than peak IP3-evoked fluorescence signals"

However, in Figure 1, the maximum raw signal during uncaging (1C) and after ionomycin (1F) looks exactly the same – both topping out at 8500 a.u – and suggests that IP3-stimulated Ca2+ release may be reaching levels that saturate the dye. Similarly, the large areas that show uniform white intensity (Figure 1, image v) are either due to: i) over zealous contrast/brightness adjustment, ii) indicator saturation @ max or iii) camera chip saturation (clipping). Assuming reasonable contrast adjustment and digitizing in 16-bits? (please add digitizer bit depth in Materials and methods), this suggests that saturation is still occurring. As none of the results figures presented data in absolute intensity values and used relative a.u. or F/F0 ratios which can give different "max levels" depending on the F0, it is hard for a reviewer to determine what the actual peak/max levels are and if indicator saturation was reached.

The importance of indicator saturation and/or Ca2+ release uniformity is magnified in using variance as the primary measure to resolve Ca2+ release events. Large, saturated areas have essentially no variance (after subtracting shot noise), and could dramatically underestimate SD values and obscure Ca2+ events. In a similar fashion, simultaneous firing of multiple puffs throughout a cell could also be difficult to interpret, as one would lose the ability to spatially discriminate individual events. This, also, would reduce SD values and make it hard to distinguish between cytoplasmic and "punctate" events.

While the use of Fluo8L, which has a much larger dynamic range in response to Ca2+ concentrations goes some way to assuage concerns over indicator saturation, Ca2+ levels may still be saturating this dye given the nature of the abrupt IP3-induced Ca2+ release. Out of curiosity, what does an IP3-uncaging event look like in a cell treated with ionomycin?

If the saturated/clipped regions from your recordings were dynamically filtered out using image processing and SD/intensity recalculated in parts of the cell in which the indicator is presumably unsaturated, this would help to allay saturation concerns on SD measurements.

2) Figure 1, ROIs

Towards the end of the rebuttal ("Summarizing key points…"), where you indicate the attention drawn to subjectively-placed ROIs was based on a "misconception", then one has to question ROIs were used at all. ROIs do illustrate important features of the Ca2+ release events, such as an apparent reduction in intensity variability in traces that reach near-maximal intensity (see first point).

3) 2 populations of IP3Rs…

Concerning point v) Figure 4 (we think you meant Figure 6), if potential methodological concerns are addressed – and indeed the punctate responses do drop out as global levels rise – the concluding statement that: "Our findings of a diffusive mode of Ca2+ liberation implicate a second population of IP3Rs with properties distinct from those clustered at puff sites" is too strong a statement given the evidence presented.

We think there needs to be experiments/analysis to show that punctate and global Ca2+ responses can be unrelated for this to be the case. In most examples presented the pattern of punctate release events appear to correlate with changes in cytoplasmic/global Ca2+.

For example, in Figure 2, the rate and amplitude of the SD events appears to be mirrored in the shape of the global responses. In E (puce color), the abrupt increase in SD is reflected as a sharp transition in global Ca2+ from baseline. In F (blue) the ramping up of SD events is reflected as a more gradual, sloping increase in global Ca2+. These relationships are illustrated nicely in G.

The maximum slope of global Ca2+ increases seems to occur at the point of maximum SD events. See Figure 4, Figure 5G and H (albeit de-amplified), Figure 6, Figure 8 (A: see 2 peaks in SD reflected in 2 steps in rate of Ca2+ intensity, like in Figure 3—figure supplement 3).

To disprove that there is just one population of IP3Rs, comparisons of the rate change of SD and global fluorescence should show little (or highly variable) correlation strength. Cumulative integration of SD and cumulative global fluorescence signals (akin to Ca2+ mass / SD mass) followed by regression, cross-correlation (with ∆ time offsets) and/or inflection analysis would be appropriate to examine those potential relationships. Performing this analysis on specific regions in cells to elucidate any potential zone-of-influence between punctate and global Ca2+ characteristics.
