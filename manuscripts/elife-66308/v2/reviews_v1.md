# Peer review - Round 1

Editors:
- Jeffrey C Smith, National Institute of Neurological Disorders and Stroke United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66308.sa1](https://doi.org/10.7554/eLife.66308.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

Spontaneous temporally correlated neural activity in the mammalian central nervous system in the absence of sensory stimulus-evoked activity is a feature of supraspinal circuits, but less clearly established as a property of spinal cord circuits in unconsciousness when there is no motor output. In this paper, the authors convincingly provide novel direct cellular-level evidence of robust and temporally correlated spontaneous neuronal activity in the in vivo lumbar spinal cord of anesthetized unconscious rats, suggesting that such activity may be a general property of circuits throughout the central nervous system.

Decision letter after peer review:

Thank you for submitting your article "Spontaneous neural synchrony links intrinsic spinal sensory and motor networks during unconsciousness" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Jeffrey C Smith as the Reviewing Editor and Reviewer #3, and the evaluation has been overseen by Lu Chen as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. Below are essential revisions that need to be addressed in a substantially revised manuscript that will be re-reviewed.

Essential Revisions:

1) In the abstract and throughout the manuscript, the word "purpose" or "purposeful" should be replaced. It has inappropriate, unjustified, and unnecessary implications and connotations. Appropriate, non-freighted replacements are terms such as "non-random," "functional," "patterned." In the Intro and Discussion, the manuscript can then consider, as it does, the possible functional effects or outcomes of this non-random activity. For similar reasons, "network policy" in line 24 should be replaced. For example, Lines 24-5 might read: "…is consistent with the hypothesis that salient, experience-dependent…"

Methods and Results

2) Spike sorting is a procedure for detecting and identifying the extracellular action potentials of individual neurons in multi-neuron recording. A variety of algorithms have been applied for this purpose. The authors used the unsupervised wavelet-based clustering method developed by Quiroga and colleagues. Like similar algorithms, it requires manual analysis by the experimenter to verify and adjust the results. The authors discriminate ~55 neurons per trial, which translates to about two neurons from each recording electrode. Because the sorting procedure requires manual intervention to exclude false positives, perhaps the authors could provide references indicating that this is a reasonable yield per electrode. It would also be worthwhile for them to provide more information on the parameters used in the sorting procedure and possibly to compare the results with those of a more standard method (e.g., PCA).

3) Figure 1 shows the experimental setup and design, using actual data and their analyses. The figure is hard to understand because it is missing the temporal units for the raw-data trace, the raster plot, and the histograms. It is not clear whether the 4 red/orange action potentials are 4 different neurons or two neurons each detected from two electrodes. Also unclear are the meanings of the red lines and black arrows with the histograms.

4) The comparison between the real and the synthetic data is a crucial aspect of the paper, and the authors should provide more information and attention both in the Methods and the Discussion sections. It is not sufficiently clear how the data were shuffled and reconstructed to provide the synthetic data. What procedures were used to ensure that the synthetic data statistically matched the observed data? The main purpose of the synthetic data was to determine whether the connections found are likely to emerge merely by chance. The author stated that it is possible to directly compute the probabilities that significant connections will exist within or between regions if neurons are distributed at random. How have these probabilities been calculated? How did the authors verify that the bootstrapped synthetic data converged to the theoretical predictions?

5) Lines 495-542: The synthetic data do yield substantially percentages of connectivities, averaging roughly two-thirds the values for the actual data. Furthermore, it is of considerable concern and puzzlement that the synthetic connections for a number of regions are greater than the actual connections (Figure 8.b). What does this mean? For example, Figure 8 appears to show that dorsal and ventral horns are less connected in the actual data than in the supposedly random synthetic data. This seems to contradict the conclusion stated in the abstract that "we…demonstrate that spontaneous functional connectivity also links sensory and motor-dominant regions during unconsciousness."

6) The authors attribute the patterns of spontaneous activity found to reflect intrinsic spinal circuit activity, while acknowledging the possibility of sensory afferent feedback contributing to the spontaneous activity despite urethane anesthesia and isoflurane anesthesia in another experimental cohort. It would be important for the authors to discuss whether they have assessed if the spontaneous activity patterns are affected by deeper anesthetic levels than with the standard dose of urethane used for these studies. Also, despite the authors' arguments about some potential disadvantages of deafferentation, this is still an effective way to determine if there are any contributions of local afferent inputs after positioning the microelectrode arrays, particularly since they have confined their electrophysiological recordings to a single lumbar spinal segment and local deafferentation could readily be implemented. Additional information in this regard would be important to strengthen the authors' arguments about the recorded activity reflecting primarily intrinsic spinal circuit activity.

7) Unless motoneurons are completely inactive under the anesthesia, might high-amplitude spikes in VH identify likely motoneurons? If that is the case, it would be very interesting to assess motoneuron connectivities with other areas and neuronal populations. This deserves discussion.
