# Peer review - Round 1

Editors:
- Ronald L Calabrese, Emory University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.24482.017](https://doi.org/10.7554/eLife.24482.017)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The effects of background on detection and phase invariant coding of transient natural communication signals by correlated neural activity" for consideration by eLife. Your article has been favorably evaluated by Eve Marder (Senior Editor) and three reviewers, one of whom, Ronald L Calabrese (Reviewer #3), is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal their identity: Bruce A Carlson (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript is an advance on Metzen et al., 2016 in which the authors showed that correlations between the activities of peripheral afferents mediate a phase invariant representation of natural communication stimuli (chirps) that is refined across successive processing stages thereby leading to perception and behavior in the weakly electric fish Apteronotus leptorhynchus. In this advance, they explore how the phase invariance of neuronal responses and behavior to chirps is affected by background beat frequency determined by the difference in EOD frequency of two fish exhibiting steady EOD. The frequency contrast between the background beat and chirps decreases as the background beat frequency increases, but in contrast to previous studies that have focused on single neuron activity in afferents, in this study the authors show that it is correlations between the spiking activities of multiple afferents that determine behavioral responses. They show that the decreased signal detectability is due to the greater tendency of peripheral afferents to display phase locking to higher background beat frequencies, (a direct consequence of their high-pass frequency tuning characteristics). Such phase locking causes increased correlations among afferents during some portions of the background beat for which both afferents do not fire action potentials. This greater variability in correlation throughout the beat cycle then decreases signal detectability. The advance is well written and clearly illustrated, and it significantly extends the previous finding and gives new behavior relevance to afferent correlations, while explaining deterioration of behavioral responses with high frequency beat backgrounds.

Essential revisions:

There are some concerns in the detailed review of reviewer #1 (below) that must be addressed in revision. The most important are the technical points:

1) The measure of phase-locking (subsection “Electrophysiology”), which is based on a binary threshold decision.

2) The use of a sliding window for measuring correlations (subsection “Correlation between the spiking activities of electrosensory afferents”).

Moreover, there was a general concern among the reviewers about the major conclusion. The importance of correlation for invariant coding was demonstrated in the previous publication. The new result here is that the phase invariant coding breaks downs for high frequency beats. The fact that it breaks down at high frequency beats for both the afferent correlation coding and behavioral responses does strengthen the central claim of the first paper that correlated afferent firing mediates perception of the chirps. However, once behavior breaks down, we do not know whether it was because it relied on correlations or some other computation. Thus, the conclusion should be tempered by this caveat.

Reviewer #1:

The authors build on their recent finding of invariant coding of chirps with respect to chirp phase based on primary afferent correlations to address whether this coding of chirps is also invariant with respect to background frequency. They find that primary afferent correlations invariantly code for chirps only at relatively low background frequencies, and that this correlates with behavioral responses to chirps. This strengthens their previous conclusion that chirp perception is mediated by primary afferent correlations. This finding also meshes well with previous studies showing that chirps are more frequently produced on low-frequency, low-intensity backgrounds. This is a nice follow-up to the previous work, though I do have some concerns with the methods and conclusions.

1) The authors do a nice job of relating their findings to previous observations that chirps occur more frequently on lower baseline frequencies. However, I take issue with the authors' interpretation of cause and effect. They suggest that the inability to accurately encode chirps is the reason why the fish don't produce chirps at high baseline frequencies. It could be the exact opposite. If chirps don't occur on top of high-frequency beats, then why bother encoding them? I don't think the authors can conclude either way whether constraints of the sensory system are driving the behavior, or that behaviorally relevant signals are driving properties of the sensory system.

2) Related, do chirps vary quantitatively with baseline frequency? E.g. they may happen less frequently at high baseline frequencies, but do such chirps tend to involve higher frequency excursions? If so, then the use of a constant frequency change across baseline frequencies may not be a "natural stimulus." Whether or not chirps vary with baseline, it seems inaccurate to refer to all of these stimuli as "natural" if some of them tend not to occur naturally.

3) Subsection “Implications for other systems”: It is good to link the findings of this study to other sensory systems and taxonomic groups to make the case for general principles. However, it seems that these are fundamentally different kinds of invariance problems to solve. Detecting a chirp irrespective of background frequency or phase is different from detecting frequency irrespective of amplitude, or odor identity irrespective of concentration. The latter have nothing to do with "background." "Invariance" is being treated here as though it were a measurable physical thing, when really it is context-dependent and can refer to any kind of physical thing. The mechanisms for invariant coding are likewise likely to be context- and stimulus-dependent. This does not mean the findings do not have broad relevance, simply that they need to avoid implying that this is the solution to invariance.

4) Subsection “Implications for other systems”: Do not refer to animal species as higher or lower. This is simply not how evolution works. Further, if mammalian nervous systems can solve the problem, then so can fishy ones. It seems more likely that either: (i) these signals (chirp on high-frequency beat) are not behaviorally relevant, so there is no need to solve the problem, or (ii) that the problem of invariance being solved by these fish is a fundamentally different invariance problem from that solved by the other examples given.

5) I have concerns about the measure of phase-locking (subsection “Electrophysiology”). It is based on a binary threshold decision. Why is it done this way as opposed to a more standard, linear measure of vector strength (e.g. Goldberg and Brown 1969)? Your measure seems to nonlinearly exaggerate differences in the degree of phase-locking. Indeed, in Figure 2—figure supplement 1D, you can clearly see phase-locking across all 3 stimuli (though different in degree), but the metric used gives you values = 0 at all frequencies <10 Hz in Figure 2—figure supplement 1C. This is not a crucial metric for the conclusions reached, but it is somewhat perplexing why it is used.

6) I have concerns about the use of a sliding window for measuring correlations (subsection “Correlation between the spiking activities of electrosensory afferents”). If the window gets shorter as baseline frequency gets higher, then correlations might decrease artefactually due to both sampling fewer spikes and increasing the temporal precision needed for a correlation. A similar concern arises in the measurement of invariance across baseline frequencies, for which a window that varies with beat frequency is also used (subsection “Quantifying neural response invariance”). Regardless of this methodological issue, it's not clear how these variably sized windows are physiologically relevant. The integration time window of postsynaptic neurons that would detect these correlations should not change with beat frequency.
