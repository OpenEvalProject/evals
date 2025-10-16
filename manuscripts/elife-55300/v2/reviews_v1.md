# Peer review - Round 1

Editors:
- Ingrid S Johnsrude, University of Western Ontario Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55300.sa1](https://doi.org/10.7554/eLife.55300.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Using fMRI and computation modeling, this study explores how age affects cortical responses to natural sounds with different spectrotemporal properties. Using both encoding and decoding analyses, the authors demonstrate that older listeners have broadened temporal rate tuning compared to younger listeners, but show no difference in spectral tuning.

Decision letter after peer review:

Thank you for submitting your article "Temporal selectivity declines in the aging human auditory cortex" for consideration by eLife. Your article has been reviewed by Barbara Shinn-Cunningham as the Senior Editor, Ingrid Johnsrude as Reviewing Editor, and two reviewers. The following individual involved in review of your submission has agreed to reveal their identity: Jonathan Z Simon (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. In recognition of the fact that revisions may take longer than the time we typically allow, until the research enterprise restarts in full, we will give authors as much time as they need to submit revised manuscripts.

Summary:

The researchers use fMRI and computational modeling to compare auditory cortical responses to natural sounds across subjects of varying ages (cross-sectional design), according to the spectrotemporal properties of the sounds.

Approaching age-based neural dedifferentiation (or neural "tuning") in the auditory domain has not been well handled in the literature to date. In that sense, reviewers found this work to be interesting, particularly with respect to the detailed and nuanced treatment the authors give to the analysis of auditory stimuli (i.e., rates, scales, frequencies).

The reviewers found the study to be well designed.

The analysis proceeds in two steps: first using an encoding framework, and then using a decoding framework. The authors find that older listeners have broadened temporal rate tuning compared to younger listeners, in contrast to spectral tuning which does not show such a difference.

The reviewers commented that the analysis methods are employed well and described clearly. It is evident that there is great attention to detail in the analysis, both in the formalism and the statistics.

The benefits and tradeoffs between the encoding and decoding approaches are handled well, and both reviewers commented on how nice it was to see both frameworks used on the same data.

Essential revisions:

The reviewers raise a number of concerns that must be adequately addressed before the paper can be accepted. Some of the required revisions may require further experimentation within the framework of the presented studies and techniques.

1) Subsection “Univariate encoding analysis: Model estimation”: How were subject data incorporated in the cross-validation scheme? It is clear how sounds were split, but not how subject data were handled. If all subjects are included and you simply split on stimuli, then the data are technically not "independent" per se in the classic between-subjects sense…one can always argue bias is present by having all subjects contribute at each cross-validation stage.

2) Subsection “Multivariate decoding analysis: Model estimation”: It seems to be a major choice to have a single sensory control region (calcarine sulcus) given the task type. Please justify this more.

3) Subsection “Sound identification accuracies”: the joint stimuli (texture + speech) are somehow "uniquely" identified despite texture being repeated 4x. Would results likely be even better without this repetition? Why was texture repetition required at all?

4) Subsection “Decoding results”: It was not clear why decoding accuracy should be highest at these values of freq, scale, and rate. Was there a hypothesis regarding these levels?

5) The age-based result in Figure 5E is questionable. This was plotted as a scatterplot in WebPlotDigitizer to examine the impact of data on the leftmost side of the plot (which visually are pulling the slope negative). Using a Spearman corr reduces the corr value to -.21 (p=.27). Holding out a single high leverage case (only the most extreme value detected by computing Cook's distance) also reduces the Pearson correlation to -.28 (p=.14) and Spearman to -.13 (p=.50). And taking out the three cases identified by a Cook's rule of thumb (Standard Cook's cutoff = 4/n), Pearson and Spearman corrs are reduced to -.19 and -.05 respectively.

6) The uni- and multivariate outliers need to be better addressed in Figure 5B/C as well. The distributions are not terribly well behaved. For example, without what seems like a young adult outlier at the highest SI level in Figure 5C, does the group effect remain?

7) The same should be investigated for Figure 6B also; the right tail of the young group appears to pull up the young adult mean in that case too. It does appear that Figure 6A may hold up however, but this needs to be verified.

8) Because of a lack of clarity in the results as they currently sit, little can be made of the current Discussion section, various aspects of what is discussed may fall away once the data are reanalyzed. The Discussion section (and Abstract) should therefore be revised in light of what the reanalysis shows.
