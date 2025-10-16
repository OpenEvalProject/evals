# Peer review - Round 1

Editors:
- Martin Vinck, https://ror.org/00ygt2y02 Ernst Strüngmann Institute (ESI) for Neuroscience in Cooperation with Max Planck Society Frankfurt Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80160.sa0](https://doi.org/10.7554/eLife.80160.sa0)

This paper provides important insights into the spatial organization of β-oscillatory activity in the human brain, which is a crucial dynamic feature of frontal and parietal networks involved in movement preparation and sensory prediction. Using high-resolution source reconstruction with Magnetoencephalography in humans, the authors provide compelling evidence demonstrating that β oscillations are organized as travelling waves in two distinct directions relative to the central sulcus. Furthermore, the study convincingly shows that the spatiotemporal organization of β bursts is systematically linked to behavior, specifically motor execution. These findings have important implications for our understanding of the neural mechanisms that underlie movement planning and execution in the human brain.


---

# Peer review - Round 1

Editors:
- Martin Vinck, https://ror.org/00ygt2y02 Ernst Strüngmann Institute (ESI) for Neuroscience in Cooperation with Max Planck Society Frankfurt Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80160.sa1](https://doi.org/10.7554/eLife.80160.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Spatiotemporal organization of human sensorimotor β burst activity" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Chris Baker as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Robert Law (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. As you can see from the reviews, there are a number of methodological/technical concerns that need to be addressed, although the reviewers considered the work generally sound in terms of methods. A more critical point is the nature of the conceptual advance in terms of understanding the mechanisms or functions of β bursts and waves. We expect the authors to expand their study in terms of the significance of the findings, by performing new analyses and analyzing new data. Thus, we are happy to invite a revision, but we expect new data and/or analyses that substantially improve the significance of the manuscript.

Essential revisions:

As you can see from the reviewers, the study received mixed evaluations. We focus here on comments pertaining to the technical aspects (comments 1-9), and the conceptual advance (comment 10).

1) Could the beamforming weights transform any activity (regardless of its original structure) into a profile that shows travelling waves? The authors do report a high correlation. Please clarify.

2) It seems that the authors do the analysis in the embedding space created by the 2D visualizer. To what extent does this bias the results? Why was the analysis not done in the 3D space?

3) Could there be a trivial explanation for the two wave directions that are reported. MEG is of course sensitive mostly to tangential current flow. This tangential current flow comes from the walls of the sulci or cortical tissue that folds around the midline or laterally. If you look at the orientation of the walls of the sulci then this predicts current flow in the anterior to posterior plane. And the medial/lateral axis as well.

4) Modifying the threshold at which β events are detected could alter their reported properties and expression in space and time. The authors should therefore perform parameter sweeps on e.g. the thresholds for detection of oscillation bursts to determine whether their conclusions on β properties and propagation hold. If this additional analysis does not change their story, it would lend confidence to the results/conclusions.

5) Determining the generators of β events at different locations is a tricky issue. The authors mentioned a single generator that is responsible for propagating β along the two axes described. However, it is not clear through what mechanism the β events could travel along the neural substrate without additional local generators along the way. Previous work on β events examined how a sequence of synaptic inputs to supra and

infragranular layers would contribute to a typical β event waveform. Although it is possible other mechanisms exist, how might this work as the β events propagate through space? Some further explanation/investigation on these issues is therefore warranted.

6) Given that the main angle of this paper is methodological, it would be important to provide the source code on github along with documentation and a standard "notebook".

7) The authors should describe in more detail the properties of the β bursts in both directions: Are there any distinguishing features for the β bursts that propagate along each primary direction? How far do each of the traveling waves go in each direction? Is the

frequency and properties nearly constant as the waves travel or do the dominant frequencies show any shifts the farther the waves get from their generator? If there is a single generator responsible for the β waves that travel in each direction, then through

what mechanism are the β events created as they propagate further from their source?

8) Introduction:

"Finally, our results suggest that sensorimotor β bursts occurring before and after a movement share the same generator but can be distinguished by their anatomical, spectral and spatiotemporal characteristics, indicating distinct functional roles." If β bursts before/after movements have the same generator, what distinguishes the initiation of movement vs lack of movement? As a result of their work here, would the authors hypothesize that β contributes to either generation or suppression of movement?

9) Spatial cancellation of β occurring simultaneously on both sides of the central sulcus may occur (these events would be near to one another and with opposite orientations, cancelling out the magnetic field, see Ahlfors et al. 2010). This would ultimately lead to fewer detected events on the sulcal walls, compared with the sulcal banks. Ultimately the study may be throwing out a lot of ground-truth events from the walls, and the fact that the authors keep more events from deep in the sulcus will bias the traveling wave analysis that follows.

In Figure 1, the authors seem to show a higher density of β events relatively deep in the sulcus compared to the sulcal walls. This is certainly an interesting result if true! But even given only the occasional synchronization of mesoscale cortical neighborhoods, it appears that events in the sulcal walls will still be systematically undersampled and those deep in the sulcus oversampled here, by vice or virtue of cortical geometry as it pertains to the magnetic field.

This spatial sampling bias could impact nearly all aspects of the event propagation analysis that follows, and so must be considered in sufficient detail.

A "worst-case scenario" is that ground-truth events may be uniformly distributed across much of the region of interest, and where both the reported directionality and relative incidence rates of traveling wave classes are artefactually biased. Treating this potential issue could, for instance, come in the form of (1) developing further controls and/or (2) repeating the analysis after resampling events to reflect a potential worst-case ground-truth scenario.

10) While the reviewers acknowledged the methodological advance, they were not sufficiently convinced that the present study provides sufficient functional advance. For example, no meaningful difference was found between bursts traveling along the two different principal modes of propagation, and importantly, no relation with behavior (response time) was found. The same stands for pre vs. post motor bursts, except for the expected finding that post-motor bursts are more frequent and tend to be of greater amplitude (yielding the observation of a so-called β rebound, on average across trials).
