# Author response - Round 1

Authors:
- Tai-Ying Lee ([ORCID: 0000-0001-8072-1219](https://orcid.org/0000-0001-8072-1219))
- Yves Weissenberger
- Andrew J King ([ORCID: 0000-0001-5180-7179](https://orcid.org/0000-0001-5180-7179))
- Johannes C Dahmen ([ORCID: 0000-0001-9889-8303](https://orcid.org/0000-0001-9889-8303))

## Response text

DOI: [10.7554/eLife.89950.4.sa4](https://doi.org/10.7554/eLife.89950.4.sa4)

The following is the authors’ response to the previous reviews.

Reviewer #2 (Public Review):

Weaknesses:

There are however, substantial concerns about the interpretation of the findings and limitations to the current analysis. In particular, Analysis of single unit activity is absent, making interpretation of population clusters and decoding less interpretable. These concerns should be addressed to make sure that the results can be interpreted clearly in an active field that already contains a number of confusing and possibly contradictory findings.

We addressed this important point (which was also made by reviewer #1) in our previous revision. Specifically, we included additional analyses that operate at the level of single units rather than the population level, as requested by the reviewer. For example, we assessed, separately for each recorded neuron, whether there was a statistically significant difference in the magnitude of neural activity between hit and miss trials. This approach allowed us to fully balance the numbers of hit and miss trials at each sound level that were entered into the analysis. The results revealed that a large proportion (close to 50%) of units were task modulated, i.e. had significantly different response magnitudes between hit and miss trials, and that this proportion was not significantly different between lesioned and non-lesioned mice. It is therefore no longer correct to say that “analysis of single unit activity is absent”, and we would be grateful if this statement could be changed.

Reviewer #2 (Recommendations For The Authors):

The authors have done a good job addressing the main concerns from the previous review. There are a few additional points that hopefully do not require substantial additional edits.

Figure 5/supplements. While the authors provide compelling evidence that clusters and overall activity patterns are similar for lesioned and control animals, there do appear to be some differences. For instance, the hit/miss difference for cluster 3 (the "auditory" cluster) appears to be absent for lesioned mice (Fig 5S3 D). Can the hit-miss difference be quantified?

We agree that there are some differences between the activity profiles of lesioned and non-lesioned mice: Inspection of panels A and C of Figure 5 – figure supplement 3, for instance, indicates that there is a relatively high proportion of neurons in cluster 3 of the non-lesioned mice that exhibit prolonged elevated activity in hit trials and a relatively lower proportion of those neurons in cluster 3 of lesioned mice. This likely explains the difference in the average response profiles of cluster 3 between the two groups pointed out by the reviewer. Furthermore, there is a slightly larger pre-stimulus dip in hit trial activity for lesioned than non-lesioned mice in cluster 1, a more pronounced short latency peak in hit trial activity for lesioned mice in cluster 2 as well as differences in other clusters. However, these differences are not inconsistent with our interpretation of these data in that we describe the activity profiles as being “similar” and exhibiting a “close correspondence” (rather than as being identical). Having considered this carefully, we do not believe that attempting to quantify these small differences would add much value here or help the reader with the interpretation of these data, especially given that the activity profiles of all neurons that make up each cluster are plotted in panels A and C.

Could the mice have been using somatosensory information to perform the task? A wideband click presented from a free-field speaker could have energy in a low frequency range that triggers a whisker response. Given the moderate but not insignificant somatosensory input into the IC shell, this doesn't seem like a trivial concern, and it could substantially impact interpretation of the results. Without wanting to complicate things too much, the authors might consider one or more of these questions: What's the frequency content of the click? Can a deaf mouse perform the task? Can an AC-lesioned mouse learn/perform the task with close-field acoustic stimulation? Or for a highfrequency tone target rather than a click?

This is an interesting suggestion. We have, in the context of another study, trained mice in our lab to detect somatosensory stimulation (a brush stroke to their whiskers) and consistently found that it takes them much longer (often two weeks or more) to learn to respond to a stimulation of their whiskers than to the presentation of a sound. The brush strokes applied to the whiskers in those experiments were 50-150 ms in duration and were thus orders of magnitude greater in both their duration and amplitude and considerably more salient than any somatosensory stimulus that could potentially arise from the clicks presented here. Therefore, we consider it highly unlikely that mice learned to use somatosensory information potentially picked up by their whiskers to perform the click detection task.

L. 63. The authors might want to cite some recent work from the Apostilides lab on the properties of AC-IC projections as well as non-auditory signals in the IC.

There are two recent papers from the Apostolides lab that are relevant to our study. We already cite Quass et al., 2023. We have now added Ford et al., 2024 as well.

Changes to manuscript:

Line 81: “This raises the possibility that these context-dependent effects may be inherited from the auditory cortex (Ford et al., 2024)”.

L. 220. "sound-responsive neurons" It is possible to report the representation of sound-responsive neurons in the different clusters? This might help tease apart what processes contribute to their respective activity. Not a big problem if the samples can't be registered easily.

Sound-driven neurons were identified on the basis of a subset (those trials in which sounds were presented at levels from 53 dB SPL to 65 dB SPL) of the trials used for the clustering analysis so the analyses are not directly comparable.

p. 603. "quieter stimuli" What sound level was actually used in the 2p experiments? Was it fixed at a single level per animal?

Sound level was not fixed at a single level. A total of nine different sound levels were used per mouse. We apologize that this was not made clear previously.

Changes to manuscript:

Line 603: “Once the mice had achieved a stable level of performance (typically two days with d’ > 1.5), quieter stimuli (41-71 dB SPL) were introduced. For each mouse a total of 9 different sound levels were used and the range of sound levels was adjusted to each animal’s behavioral performance to avoid floor and ceiling effects and could, therefore, differ from mouse to mouse.”

L. 747. Something is not right with this formula. It appears that it will always reduce to a value of 1/2.

Thanks for spotting this. There are two typos in this formula. This has been fixed and now reads (line 749):Balancedaccuracy=12∗(Ntruepos.Ntruepos.+Nfalseneg.+Ntrueneg.Ntrueneg.+Nfalsepos.).
