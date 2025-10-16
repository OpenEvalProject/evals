# Peer review - Round 1

Editors:
- Jonathan Erik Peelle, Washington University in St. Louis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.53051.sa1](https://doi.org/10.7554/eLife.53051.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

A major challenge for the auditory system is to interpret fine acoustic cues present in the speech signal in order to identify words. This work uses intercranial recordings from human listeners to better understand voice onset time, a key distinction in speech sounds, showing that individual electrodes in temporal lobe are sensitive to voice onset time differences. Complementing experimental work is an example model illustrating how voice onset time might be coded in a neural network.

Decision letter after peer review:

Thank you for submitting your article "Transformation of a temporal speech cue to a spatial neural code in human auditory cortex" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Barbara Shinn-Cunningham as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Michael Wehr (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary

The authors report ECoG data from human listeners while listening to spoken syllables that varied in voice onset time (VOT). They found that VOT (a temporal cue) is encoded in the peak amplitude of high gamma activity in individual electrodes. A simple neural network is presented that qualitatively captures main features of the human data. The findings complement prior ECoG studies on the coding of basic speech properties in the temporal lobes.

Essential revisions

1) The rejection of a temporal code (or temporal contribution) for VOT representation was not entirely convincing. One concern is that the peak window may be too short to capture the temporal dynamics of the signal, so the fact that the classifier fails for temporal information could be artifactual. Examples of the types of dynamics that might temporally encode voicing would be onset latency, peak latency, or waveform shape. The 100 ms peak windows (150-250 ms) miss the onset, probably degrade peak latency information, and likely do not capture the waveform shape (e.g. single or double-peaked, fast or slow rise or decay times, etc). In other words, the HG amplitude appears to be mostly flat during this 100 ms window and thus cannot contain the timing information you wish to test for. Thus the classifier analysis seems almost designed to fail to decode timing information. A different (and possibly more straightforward) way to look at temporal information might be the following. Since you have already extracted the peak time and amplitude, and you want to know whether timing or amplitude convey information, why not just run a classifier on peak times, peak amplitudes, and both? This way instead of removing amplitude information by normalizing, or removing timing information by jittering, you can just directly ask whether the amplitude or timing values can be used to decode voicing. This could serve as a useful corroboration of the multivariate decoding results, or might instead reveal information in peak timing.

2) Although the inclusion of a model was a nice touch, the theoretical contribution of doing so was somewhat unclear. Are there other theoretical frameworks for understanding VOT representations that can be contrasted with the current one? Damper, 1994, is one that was identified by a reviewer (there may be others). Overall we had a difficult time discerning the theoretical advance gained from the model, and a clearer link to existing understandings (does it resolve a controversy?) or clearer way in which it might motivate further experimental approaches would be useful.

3) The focus in the current analysis is on high gamma oscillations. However, other work has suggested a role for low frequency oscillations in phoneme perception (Peelle and Davis 2012; Kösem et al., 2018). So, (a) what's the justification for focusing exclusively on high gamma, and (b) what is a framework for reconciling your high gamma responses with a potential role for lower frequencies?

4) The discussion of local or ensemble temporal coding and spatial coding would benefit from consideration of hierarchical organization and the construction of feature selectivity. If the observed spatial code is the result of some temporal-to-rate transformation, where might this occur and how does that relate to the types of feature selectivity seen in human and primate auditory cortex? As an analogy, your findings are reminiscent of call-echo sensitive cells in the bat. There, many cells in IC respond both to call and to echo (“double-peaked”), whereas other cells in IC respond only to the combination of call and an echo at a particular delay (“single-peaked”). The latter are not topographically organized in IC, but in the FM region of auditory cortex such cells form a topographic map of delay. Do you imagine that a similar hierarchical transformation is occurring in the human auditory system for the encoding of VOT? Where do your recordings and those of e.g. Steinschneider or Eggermont fit into this picture?

5) Please make the stimuli available as supplemental material.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Transformation of a temporal speech cue to a spatial neural code in human auditory cortex" for further consideration by eLife. We apologize for the delay in returning a decision to you – due to COVID19-related disruptions to the workflows of many of our editors and reviewers, the process is taking longer than we would like. Thank you for your patience with us.

Your revised article has been evaluated by Barbara Shinn-Cunningham (Senior Editor) and a Reviewing Editor. We agree that the manuscript has been improved but there are some remaining issues that need to be addressed before acceptance. Specifically, the issue of the distinction between the hypotheses laid out in subsection “Peak neural response amplitude robustly encodes voicing category”.

The issues are nicely laid out by reviewer 3's comments, which we include unedited (so will not repeat here). It seems clear that the manuscript makes a valuable contribution and we have no remaining major issues with the analyses. However, it will be important to address the apparent contradictions in the results and conclusions in discriminating between the hypothesses laid out in subsection “Peak neural response amplitude robustly encodes voicing category”.

Of course, there is a chance we all missed something obvious – please let us know, and perhaps some clarification in the text would be helpful in this case.

Reviewer #3:

The authors have done a good job addressing the comments and the revised manuscript is responsive to most of the points raised. The additional interpretation of the model results, robustness, and context are welcome additions. The discussion of coding and hierarchical processing are also good. Yet there is a remaining issue that sticks out and that needs to be resolved. This is the question of whether the temporal patterns of neural responses encode VOT information. To be clear, I don't have a dog in this fight – I'm neutral about spatial or temporal codes. I'm just pointing out that the manuscript is internally conflicted on this point, and the revisions haven't resolved the issue.

As the authors spell out in the rebuttal, "It is certainly the case that both sub-categorical and category-level information is carried by the onset latency of voiced-selective (V+) neural populations (Figure 3). However, this temporal information does not contribute to classification of voicing category (Figure 1F) because this information is not available during the peak window." Reading the reporting of the amplitude/timing decoding shown in Figure 1F, the take-home message from that is that peak amplitude, but not timing, contains VOT information. This message is wrong, because as shown in Figure 3 the onset latency encodes VOT information. So care must be taken to avoid leading readers towards that message.

Close reading of the Results section reporting Figure 1F reveals that the statements are accurate because they contain a clause such as "in the peak response window," for example: "In contrast, when amplitude information was corrupted and only temporal patterns in the peak response window were reliable (-Amplitude/+Timing), classifier performance was not different from chance." Even though this statement is accurate, I'd argue that it's misleading, especially because the set-up is to distinguish between 3 hypotheses: "Specifically, we evaluated three alternatives for how temporally-cued voicing category is encoded by high-gamma responses in cortex: (1) the spatial pattern of peak response amplitude across electrodes, (2) the temporal patterns of evoked responses across electrodes, or (3) both amplitude and timing of neural activity patterns." At the end of this section, after looking at Figure 1F, the reader is left with hypothesis (1) as the take-home. But your data rule out (1) and instead demonstrate hypothesis (3), but not until Figure 3. I get the motivation that you want to show encoding by peak amplitude in order to compare with previous findings from your group. That's fine. But there's no need to rule out a temporal code to do this. If the take-home message from Figure 1 is that VOT information is encoded in peak amplitude, a spatial code, just say that, and drop the temporal jitter analysis, because it's misleading and unnecessary. Or else expand the window to include onsets, which based on Figure 3 should support VOT classification.
