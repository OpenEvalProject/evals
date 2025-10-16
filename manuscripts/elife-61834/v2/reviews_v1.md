# Peer review - Round 1

Editors:
- Laura L Colgin, University of Texas at Austin United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.61834.sa1](https://doi.org/10.7554/eLife.61834.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

SpikeInterface is an integrated set of tools that makes it straightforward for researchers to set up a complete spike sorting workflow. SpikeInterface supports many common data formats and modern spike sorters and provides post-processing tools for characterization of the spike sorting results. This allows for validation and comparison of multiple spike sorting results. Results suggest that combining the results of multiple spike sorters could help to reduce the number of false positive units, which is an interesting future direction that will likely inspire further investigation. This tool is expected to be useful for researchers in many different areas who are studying neuronal responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "SpikeInterface, a unified framework for spike sorting" for consideration by eLife. Your article has been reviewed by a Senior Editor, a Reviewing Editor, and three reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Fabian Kloosterman (Reviewer #2).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

There was a great deal of discussion about this manuscript among the reviewers and the editor after the individual reviews were received. Ultimately, the consensus was that this work in its present form is too preliminary to be useful to, and to make a major impact on, a broad range of users. At eLife, the standard revision period is approximately two months, and therefore papers are largely assessed "as is" to allow authors to decide when to publish the work at the stage when they feel it is ready. In this case, though, reviewers agreed that the work needs a number of major revisions that constitute a substantial amount of work in order to make a major impact across a broad range of readers (e.g., reviewers were not confident that this tool is ready to be used by anyone who is recording with Neuropixels). If you agree with the reviewers that major changes to the tool are necessary to make a major impact on the field, then we would encourage you to submit a majorly revised manuscript to us in the future, citing this manuscript number and requesting the same editor. We would be willing to re-assess the manuscript at that time. Otherwise, you can just move on to a more specialized journal, keeping your tool in its present form and perhaps improving on it in future publications.

The three original reviews are included in their entirety below. However, due to the extensive and constructive discussion that occurred after reviewers read each other's reviews, we would like to emphasize a number of interrelated major points that were discussed in the consultation:

1) A concern was raised that SpikeInterface limits the flexibility of the spike sorters it contains and makes spike sorting more of a "black box". Given the lack of real ground truth available for results comparison, this was viewed as a major weakness. Reviewers felt that users still need to be able to look carefully at the units, understand the different algorithms, and properly set the parameters. Using the default parameters could lead to suboptimal results, and the authors did not attempt to adjust parameters. Reviewers felt that the SpikeInterface toolbox could also be used to compare results of the same spike sorter using different parameters and that this would be useful to find optimal parameters and would increase the potential impact of this tool.

2) The analyses and presentation of the comparison of spike sorters was viewed as weak. Reviewers agreed that careful manual curation is still the only right way to compare spike sorting results. Reviewers felt that it would be a mistake for readers who are new to the spike sorting process to look at the analyses shown in the paper as the right way to compare spike sorting results. Reviewers felt that a manual curation step is necessary to make the spike sorter evaluation process more useful.

3) It was suggested that the authors should attempt to perform some sort of smart cluster merging strategy that utilizes the output of different sorters.

4) Another suggestion for a potentially useful addition was that users would be able to swap in and out different algorithmic components in the spike sorting pipeline. Combined with manual curation and comparison to "ground truth" data sets, reviewers felt that this could help users to determine the best algorithmic components for particular types of recordings.

Reviewer #1:

In this paper, the authors introduce a Python package for easily running many different spike sorters and exporting to many different formats. The goal is to make it easier for electrophysiologists to run their data through the spike sorters and output these results to Phy and other GUIs for data visualizations. While I agree that spike sorting is a hard problem and users need to be helped as much as possible, I don't think this framework helps a lot and will ultimately not find much use. I think Phy (already published and widely used) does most of the work that the authors suggest SpikeInterface should do, and in fact the main use case for SpikeInterface seems to be as an exporter to Phy. At its core, the code provided here is a set of file converters and code wrappers that further obfuscate the black-boxes that many spike sorters are, and make it more difficult for users to know how to build a successful spike sorting pipeline for their own data.

Reviewer #2:

The work presented in this manuscript is of great interest to both spike sorting users and developers. The unified framework bridges the gap between the plethora of recording file formats and spike sorting packages, which is a major improvement in terms of spike sorting experience. The framework also features many interesting features related to spike sorting for processing recordings and sorting results. The manuscript is clearly written and introduces the functionality that is at hand in the framework in a concise way. Below is a list of major and minor comments that need to be addressed, however.

1) Spikeinterface is portrayed as a general spike sorting framework. Still, the spike sorting workflow supported by spikeinterface appears to be geared towards specific kind of data and sorters, i.e. those that work on high electrode count continuous datasets. The authors should make explicit the assumptions that are made in spikeinterface regarding the data that is accepted (e.g. datasets with only waveform snippets appear not to be supported) and the minimal requirement for spike sorters (e.g. do spike sorters need to include their own spike detection algorithm and spike feature extraction?).

2) The authors have chosen to run the spike sorters with their default parameters and without manual or automated refinement (i.e. noise cluster rejection, cluster merging/splitting). As many spike sorting algorithms explicitly depend on a manual cluster merging/splitting step after they have been applied to the data, it would be interesting to also provide an automated cluster merging (e.g., based on the ground truth as in Wouters, Kloosterman and Bertrand, 2019). This will improve the understanding of the true potential of a spike sorting algorithm, when comparing it to others in a ground-truth study. As a bare minimum, the authors should discuss the need of a post-sorting split/merge curation step and discuss the effect of leaving the step out on their results. Without such discussion, it would be premature to talk about a "consensus-based strategy" to select clusters (subsection “Application 1: Comparing Spike Sorters on Neuropixels Data”).

3) The authors define an agreement score to match clusters from different sorters and use the score to classify clusters (as compared to ground truth) as "well-detected", "false positive", "redundant" and "over-merged". However, a low agreement score could result from a high number of false positive detections or a high number of false negative detections (or both), and the interpretation would be different in these cases. In the extremes of no false positives or false negatives, an agreement score of 0.2 could either mean all spikes in a cluster represent 20% of the ground truth spikes (i.e. a clean partial cluster) or it could mean that all ground truth spikes represent 20% of the spikes in a cluster (i.e. a "dirty" over-merged cluster). Thus, the agreement score is not a good metric for the classification of the clusters. Instead, the authors should consider a classification based on different metric(s), e.g. both precision and recall.

4) We do not find the swarm plot in Figure 4 that compares the accuracy, precision and recall for multiple sorters very informative. First, the number of non-matched clusters is not obvious in this plot (we assume point with zero score are non-matched?). More importantly, there is often a trade-off between the number of false positive and false negatives, and each sorter may make a different trade-off, depending on the parameters. The swarm plot does not show the relation between precision and recall for each sorter, and a precision-recall scatter plot would be more informative.

Reviewer #3:

This submission describes a software toolbox aimed to facilitate the comparison of spike sorting algorithms. It is targeted for a broad user base, who may not have the time or technical ability to make such comparisons on their own. This tool addresses a need of the neuroscience community. Outlined below are number of suggested corrections.

Introduction: Not all the listed sorters are truly fully-manual, ie Mclust is semiautomatic.

Subsection “Overview of SpikeInterface”: Roman numerals swapped for spikecomparison and spikewidgets.

Subsection “SpikeExtractors”: It is unclear how recordingextractor, a visualization tool, provides functionality required to excess data to evaluate the spike sorting pipeling. This becomes more clear later, but could be made more clear sooner.

Subsection “SpikeExtractors” and subsection “SpikeToolkit”: The code snippets could be expanded to give more context and be more relevant.

Subsection “Curation”: Instead of holding of for the future, this functionality would be nice to implement here, if it is not an unreasonable amount of work.

Subsection “Using the Python API”: It could be said that spikeinterface is also handmade, maybe clarify the point.

Figure 3B is hard to read.

Figure 3D, what are the color code agreement levels exactly, this is unclear.

In Figure 4 it would be nice to see plotted SNR vs agreement score.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "SpikeInterface, a unified framework for spike sorting" for consideration by eLife. Your article has been reviewed by Laura Colgin as the Senior Editor and Reviewing Editor and three reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Sonja Grün (Reviewer #2); Fabian Kloosterman (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

The authors describe SpikeInterface, which is an integrated set of tools that makes it straightforward for researchers to set up a complete spike sorting workflow. SpikeInterface is modular (and extendible) and supports many common data formats and modern spike sorters. It provides postprocessing tools for characterization of the spike sorting results and for validation and comparison of multiple spike sorting results (e.g. against ground truth). SpikeInterface allows users to focus on the spike sorting results and curation, rather than having to glue together or (re)implement disparate tools themselves.

Compared to the previous version, the authors have now more clearly outlined the goals of SpikeInterface in the introduction. In addition to comparing multiple sorters, they have added new results that indicate that combining the results of multiple spike sorters ("ensemble spike sorting") could help to reduce the number of false positive units, which is an interesting future direction that needs further investigation.

Essential revisions:

1) Regarding the ensemble spike sorting approach:

– From the results shown in Figure 3C, it seems that one won't need to run all 6 sorters to eliminate the false positives. Could the authors quantify the relative benefit of combining 2, 3 or more sorters over the use of a single sorter?

– One could imagine that combining the results of spike sorters that use a different class of algorithm would provide more benefit than combining two sorters that use the same algorithm. Do the authors observe this?

– If reviewers understand correctly, many spike sorters will return a slightly different output when run a second time on the same data set. To what extent does running the same sorter twice give the same benefit (i.e. low agreement on false positive clusters) as running two different sorters?

– Would using the ensemble spike sorting approach give similar results as using a more stringent selection of units found by a single sorter (e.g. based on cluster quality metrics, SNR, spike amplitude, etc.)?

2) The authors used an arbitrary agreement score threshold of 0.5, which they acknowledge is a pragmatic but not necessarily the best choice to match units found by multiple sorters. Reviewers did not think it is necessary to change the way units are matched, but to provide more insight into the matching process it would be helpful to know what the distribution of unit agreement scores for matching pairs looks like.

3) When evaluating the spike sorting results on the simulated data set, the authors only mention matches and false positives. Reviewers did not see a mention of the number of false negatives (i.e. number of ground units that were missed by the sorters). Could the authors also indicate to what extent spikes of the missed clusters actually show up as part of the false positive units (e.g. because false positive units are actually overly split/merged true units)?
