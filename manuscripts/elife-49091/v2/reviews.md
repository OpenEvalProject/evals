# Peer review - Round 1

Editors:
- Brice Bathellier, CNRS France

Reviewers:
- Brice Bathellier, CNRS France
- Johannes C Dahmen, University of Oxford United Kingdom
- Daniel Llano

## Review text

DOI: [10.7554/eLife.49091.045](https://doi.org/10.7554/eLife.49091.045)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Tonotopic and multisensory organization of the mouse dorsal inferior colliculus revealed by two-photon imaging" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Brice Bathellier as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Andrew King as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Johannes C Dahmen (Reviewer #2); Daniel Llano (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript is an interesting and detailed investigation into the functional organization of the dorsal inferior colliculus of the mouse based on results from challenging two-photon calcium imaging experiments in unanesthetised animals. Several interesting results are reported, ranging from the lack of spatial organization of simple temporal envelope features, the prominence of inhibitory responses, the tonotopic organization in the dorsal colliculus and the presence of non-auditory activity related to facial movements. Information about the cellular identity of recorded neurons, as well as juxtacellularly recorded electrical signals and histological data, usefully complement this technically solid study.

While the reviewers are convinced that this paper will be a very valuable resource for researchers with an interest in the auditory system, a number of important concerns regarding the reproducibility of the analysis methods, the conclusions on the tonotopic organization of dorsal IC, the description of activity related to facial movements, and the presentation of some of the key results must be addressed before a final decision can be made. The title and Abstract should also be edited to better account for the different results of the study. The title could be broader, removing any reference to tonotopy and multisensory (which is debatable).

Essential revisions:

1) The authors should make sure to provide reproducible analyses based on a well-described statistical assessment. This is missing in several places:

- It is not clear in the manuscript what criteria are used to define each functional cell type (onset, offset, sustained) and how these criteria are measured and statistically assessed. This is particularly important as several claims of the paper are dependent on these classes. The authors should make sure that this is done in a reproducible manner and provide enough information about the algorithm used for cell classification.

- Figure 4D; "There were more sustained responses in cells with a larger size." This is unclear from the figure. The graph is complex and there is no statistical assessment. Why not just compute the mean size for each class and test for differences?

- Regarding the idea of cell classes, the data in Figure 4 are intriguing, but the figure is still confusing. The Legend shown in Figure 7 should actually appear in Figure 4. Beyond that, it would be helpful to have diagrams, similar to the 4 idealized waveforms shown in Figure 4, to describe the rest of the response types.

2) The analysis of the two horizontal tonotopic gradients in the dorsal part of the IC is interesting but incomplete. The authors state that this analysis is biased by more dense sampling at the center of the IC with deeper recordings here without resolving this bias. We know that the central nucleus of the IC is organised such that neurons with a preference for low frequencies are located at its dorsal tip. In the present manuscript the authors find that in a region that approaches the medial edge of the IC's surface low frequency neurons dominate. This overrepresentation of low frequency neurons seems to become particularly strong as soon as one images just 100um below the brain surface (Figure 6B), where almost no high frequency neurons can be encountered anymore. The most parsimonious explanation for this clustering of low frequency neurons just below the surface of the IC is that these neurons form the most dorsal tip of the central nucleus of the IC as hypothesized by Barnstedt et al., 2015 (who actually also see the continuation of the vertical gradient in the deepest recordings). The authors acknowledge this explanation (e.g. subsection “Spatial distribution of frequency tuning”, third paragraph) but nevertheless choose to regard the low frequency cluster as belonging to the shell of the IC (dorsal/lateral cortex) and go on to interpret the low frequency region as the site of a frequency reversal in a high-low-high frequency map. The authors are correct in saying that a gradient reversal along the dorsal surface of the IC was also observed in one mouse imaged by Barnstedt et al. However, that reversal was actually opposite in sign, i.e. low-high-low rather than the high-low-high reversal reported here.

More analysis is required to substantiate (or not) the discrepancy with Barnstedt's conclusions. As a minimum, the tonotopic gradient should be described in the first 50µm alone (without taking recordings deeper than 50µm into account). But it would be better to show the progressive changes in BF organization as one progresses more deeply into the IC. Does the tonotopy seen at the surface continue to project downward, as it does in the auditory cortex?

Another important analysis is to test if there is any evidence of frequency gradients along the dorsal surface when the low frequency clusters are removed from the analysis (i.e. remove all neurons with a CF of, for example, 8kHz and below). Also, it might be informative to plot some frequency maps from individual mice rather than only aggregated ones.

The authors also state that they have oversampled the center of IC at larger depths. This is important information about the limitations of their dataset. It should, however, not be used as an argument in favor of their hypothesis, as it is done currently.

The dimension of depth is glossed over throughout the manuscript. It should also be addressed more directly for temporal features and non-auditory responses.

3) The analysis of calcium kinetics is not convincing, in particular, the rise time values seem much too large and spread out. This is likely because the equation used is underdetermined (i.e. too many free parameters – 4 instead of 3). The rising phase equation contains a parameter A for amplitude and trise which are totally redundant (there is an infinity of combination A and trise that lead to the same curve).

It is necessary to redo this analysis with a 3 parameter kernel, such as F1AP*f(t)/fmax with f(t)=(exp(-t/tdecay)-exp(-t/trise)) and fmax=max(f(t)).

It is also necessary to see how well the model performs by comparing real vs. model traces. This is described in the subsection “Electrophysiological correlates of response classes”, but the fits are not shown.

4) Contrary to what the title suggests, the manuscript tells us little about the relationship between neural activity in the dorsal IC and multisensory input. The authors show that a small proportion of neurons show activity patterns that vary with facial movements. That does not mean that these activity patterns are the consequence of stimulation of somatosensory receptors that results from these movements. However, that seems to be how the authors interpret this result. Provided the ROIs were on the whisker pad (which isn't actually clear from the figures – the ROI shown in Figure 8B appears to have been placed behind the whisker pad rather than on it), the data indicate that the activity of some IC neurons varies with self-generated movements of the whiskers. We do not know, however, whether the changes in neural activity reflect somatosensory stimulation arising from the whisker movement (such as when the whiskers touch a part of the experimental apparatus during those movements) or are related to, for instance, the preparation of the movement, its execution or the product of some change in internal state that accompanies the movement. Therefore, claims that these data indicate sensitivity of IC neurons to somatosensory (or even multisensory) input should be toned down. Unless direct stimulation data are provided, the term 'multisensory' should be removed from the title and the description of the results focused on non-auditory inputs, related to facial movements.

5) It is not clear what the analysis of PV/CR/GCaMP cells contributes to this manuscript. It should be more clearly linked to the main themes of the paper as the other conclusions are reframed ('multisensory', claims on tonotopy). Also the observation that there is strong inhibition should be better emphasized as it is one of the important observations of the paper.

6) Regarding the "modules" seen in Figure 9A, these look very different from the more traditional modules in Figure 9—figure supplement 1, which are larger and stain more strongly for GAD. It is an important distinction, because the presence of modules in the dorsal cortex would be new, as far as we are aware, but these modules look very different than those of Chernock et al. This distinction should be made in the text.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Tonotopic and non-auditory organization of the mouse dorsal inferior colliculus revealed by two-photon imaging" for further consideration at eLife. Your revised article has been favorably evaluated by Andrew King as the Senior Editor, and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

1) Figure 6—figure supplement 9, very convincingly addresses the question whether the tonotopy observed in this study is depth-dependent within the range of depths that were extensively sampled. Looking at it, it becomes evident that depth is not an issue. This figure should be presented as a new panel of the main Figure 6 not as a figure supplement.

Also, the caption of this figure should be changed. The current title does not describe it appropriately. Something like "tonotopy across different recording depths" would be better suited.

It is also necessary to mitigate the statement about horizontal localisation biases (more central) for high depth. It seems that just very few recordings were done below 100µm.

2) It seems that the acronym CF is nowhere defined. Please do so.

It is also important to describe in the method (Analysis) how the CF was computed, particularly as previous calcium imaging studies have focused on the best frequency (i.e., the sound frequency at which the strongest response was elicited).

3) Please check again for typos and duplications in the revised text. Here a few examples:

"For somatosensory inputs the dominant effect of somatosensory inputs appears to be inhibitory and only a minority of cells have been shown to respond to unimodal tactile stimuli" > Remove one 'somatosensory inputs'

"appreciated in neurons in individual animals" > remove 'in neurons'

"responses to "adjacent" stimuli by analogously calculated" > calculating.
