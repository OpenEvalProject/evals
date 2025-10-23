# Peer review - Round 1

Editors:
- Laura Colgin, The University of Texas at Austin, Center for Learning and Memory United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.36275.028](https://doi.org/10.7554/eLife.36275.028)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for sending your article entitled "Real-time classification of experience-related ensemble spiking patterns for closed-loop applications" for peer review at eLife. Your article is being reviewed by Sabine Kastner as the Senior Editor, a Reviewing Editor, and three reviewers.

Given the list of essential revisions, the editors and reviewers invite you to respond with an action plan for the completion of the additional work. We plan to share your responses with the reviewers and then issue a binding recommendation.

All reviewers were generally positive about your manuscript and saw the potential for the real-time decoding methods to permit experiments that are not currently possible. However, the reviewers engaged in a thoughtful discussion and agreed that there are five key issues that should be addressed to ensure that the study makes a substantial impact on the field. These five specific issues are listed below (and followed by the reviews in their entirety, which include other minor comments that should also be addressed prior to resubmission):

1) The authors should better define their parameter space in which their algorithm is effective (e.g., what are the minimum number of tetrodes and spikes per time bin required for effective online replay detection?). To assess this, the authors could subsample their data (or perhaps use others' datasets that are available online) and focus on how these parameters affect detection of false positives and false negatives.

2) The authors should make their dataset available for comparison with other datasets or future datasets. The authors should also make their code for online and offline detection available for comparison with others.

3) The authors should be sure to more clearly explain how the present paper provides valuable insights that were not provided in their previous report (e.g., parameters necessary for effective online detection of replay).

4) The authors should provide a better explanation of the differences between the new real-time algorithm and standard offline methods.

5) The authors should clarify how examples were selected. Are the presented examples representative or are they the best examples? Perhaps a supplemental figure could be added in which the authors show multiple detected replay events selected in an unbiased/less biased way (e.g., all detected replay events from one example episode of awake rest, or all detected replay episodes from all rest epochs from an example behavioral session).

Reviewer #1:

In the current manuscript, Ciliberti et al., describe a novel closed-loop method for online detection of the spatial content encoded by ripple events to allow for near-real-time feedback during specific replay events. This method addresses an important technical problem for in vivo hippocampal research, namely that current work on hippocampal sequences is necessarily correlative. To demonstrate causal relationships between ripple-based reactivation (or other sequences, such as theta sequences) and behavior/memory, one must manipulate neural activity only during expression of specific sequences. As the authors note, one prior replay detection algorithm has been published, although the method described in the current manuscript is distinct from that described by Deng et al.

I have very few concerns regarding the methodology described in the manuscript. I think the authors have done an excellent job of quantifying the accuracy of their algorithm with the dataset they collected, and the authors have convinced me that their method is generally effective at identifying specific replay trajectories in one rat. However, I do have concerns regarding the general applicability of this method beyond the single example recording described in this paper.

If the authors were using this methodology to address a specific scientific question, then it would be acceptable to demonstrate how well it works on their dataset and stop there. However, if the authors are attempting to provide this methodology as a general tool to the scientific community, it becomes much more important to establish the parameter space in which it works and in which it fails. The authors do explore some parameter tuning, but this is largely limited to adjusting θsharp and θmua. It seems to me that many additional parameters necessarily impact both the quality and the speed of this algorithm. While it is impractical for the authors to examine all possible parameters that may ever be encountered, there are two critical parameters that I feel should be examined by the authors to make this method generally useful to the broader scientific community.

The first of these parameters is the total number of spikes that are entering the algorithm per time bin. From my understanding of the Bayesian decoding algorithm, more spikes generally produces a higher maximum posterior probability, which would be expected to result in more θsharp crossings. I also presume that more spikes might generally produce a more accurate representation of the current information representation in the hippocampus and thus increase the likelihood of true replay detection. Further, a higher average spike rate would likely serve to lower bin-to-bin spike density fluctuations, thereby reducing spurious θmua crossings. Finally, based on Figure 1C, it seems that more spikes slows the decoding algorithm. Thus, I wonder if there is an optimum number of spikes/ms for this method. In other words, would too many recording electrodes actually become detrimental to implementation of this method (by slowing the decoding too much or making the posterior probabilities too high)? Alternatively, are there a critical number of electrodes or spikes/ms that are required for this method to be effective (to avoid too many spurious θmua crossings or to ensure faithful decoding)? These questions could be addressed by subsampling the authors' datasets in order to test whether there is a minimum required spike rate. In addition, there are several publicly available datasets that may contain more spikes/ms or the authors could artificially add spikes to their existing dataset to test the effect of increasing total sampling on the algorithm's performance.

The second parameter is the effective 'coverage' of the environment by the spiking activity. While the authors report that there was sufficient coverage in order to faithfully decode the animal's location during exploration (these data should be shown), it was not reported whether the decoding was more/less accurate on specific arms or whether that accuracy impacted the performance of the algorithm in detecting replays of that arm. This would be important information for researchers to have in order to allow them to know when this method can be properly utilized and when it can't. Specifically, is there a critical decoding accuracy (during active behavior using a 200-300 ms decoding window) that must be met before the replay detection algorithm is effective? This could be examined by the authors by selectively subsampling the spikes detected on specific arms to reduce the effectiveness of the encoding model in order to correlate decoding accuracy with replay detection. This additionally addresses how long RUN1 needs to be for the algorithm to work (i.e., are five laps sufficient to build the encoding model or does it require 20 laps?).

These two parameters could also be tested, perhaps more convincingly, by obtaining data from additional rats, although I do not believe that this is strictly necessary.

Reviewer #2:

This Tools and Resources article is the first to demonstrate classification of hippocampal replay using real-time ensemble decoding. This is an achievement that anyone with an interest in replay has likely dreamed of for many years, and to see it finally done is cause for celebration. The ability to detect specific replay content with sufficiently short latency to apply closed-loop (Kloost-loop?) interventions such as medial forebrain stimulation, or optogenetic inhibition of a downstream target, is a major step forward that heralds a potentially transformative wave of experiments.

Of course, this report stops short of actually implementing a closed-loop manipulation, but I do not think that diminishes the magnitude and importance of what the authors have accomplished. The key result is that the required computations, notably clusterless ensemble decoding and subsequent classification, can be performed with impressively short latency (<2 ms, Figure 1D) in a fully working system that is streaming data from a single "proof-of-principle" subject.

In combining ensemble decoding and application to replay, this demonstration is a clear advance compared to previous work, although the authors could be more comprehensive in referencing not only the de Lavilleon et al., (2015) paper in the introduction, but also the work by Guger et al., (2011) and that of Bartic, Battaglia and colleagues (Nguyen et al., 2014; Bartic et al., 2016). Similarly, there is an extensive literature on brain-machine interfaces for control of prosthetic limbs and computer cursors, including real-time decoding systems by Nicolelis, Donohue, Schwartz, Andersen and others. The manuscript would benefit from a paragraph clarifying the similarities and differences with that body of work.

The hardware and software components of the system are clearly described and visualized (Figure 1—figure supplement 1 is particularly helpful). The extensive set of offline data analyses are well justified and appropriate, and the authors provide a fair and balanced discussion highlighting areas where the system can be improved.

I have only one major comment, and several minor suggestions, which I expect the authors to be able to address in short order.

I strongly suggest that the authors make the data sets used publicly available. Doing so would greatly facilitate comparison of potential future improvements built by others to the original results and therefore enhance the impact of the work. Relatedly, it was unclear to me from the manuscript whether the described system is currently implemented in the current version of the open-source Falcon software, please clarify.

Reviewer #3:

Hippocampal replay is one of the more interesting information-carrying phenomena identified in the brain. Despite more than a decade of study, however, we know less. The authors present a characterization of a real-time replay detection algorithm. Their tool would be broadly useful in experiments in which one wished to understand how the information represented in hippocampal activity during sharp wave ripples impacts learning and memory. The need for these experiments was further brought home to me as I tried to summarize my concerns about how true-positive and false-positive events were selected. Consequently, I am very excited about this work.

The main innovation I find in the paper is developing and characterizing a real-time replay detection algorithm. It builds on the authors' development of a real-time processing architecture (Ciliberti and Kloosterman, 2017). As much as I am sympathetic with the need to elevating the profile of innovation in neuroengineering, it is unclear to me whether this work is appropriate for eLife. In particular, there did not appear to be a scientific discovery. I believe that there are hints that there may be something interesting revealed about the hippocampus in the performance of the real-time algorithm, insofar as the presence of a complete replay event and its spatial content may be predictable from some fraction of the initial portion. Clearly if this was a focus of the paper that would meet the standard. Absent such a scientific result, the work might be more appropriate for a more engineering-focused journal.

An alternative scientific result would have been some behavioral effect of disruption of replay. The lack of such an effect, which the presence in the methods of a description of implantation of stimulation electrodes into the ventral hippocampal commissure suggests was the subject of experimental exploration, is striking. Specifically, the authors explore how the parameters of their real-time system affect the detection performance relative to an offline standard. The performance is quite good, but what if this reflects the fact that the offline standard is in appropriate? How the choice of offline-standard parameters affects the relative real-time detection is not explored.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Real-time classification of experience-related ensemble spiking patterns for closed-loop applications" for further consideration at eLife. Your revised article has been favorably evaluated by Eve Marder (Senior Editor), a Reviewing Editor, and three reviewers.

We are almost ready to accept your manuscript, but there are a few remaining issues that need to be addressed before acceptance, as outlined below:

Specifically, the reviewers would like the figures included in the rebuttal letter to be included as figure supplements or elsewhere. Please follow this suggestion or provide a rebuttal explaining why you prefer not to do so.

We expect the Editors to be able to make a final decision without requiring review.

Reviewer #1:

The revised manuscript is much improved, and the authors have largely addressed my concerns.

I would have much preferred for Figure 6 to have examined the effect of spike or cell number rather than tetrode number, as one can put in 100 tetrodes and get no cells or put in 12 tetrodes and get 150 cells (Wilson and McNaughton, 1993). However, I think the figure included in the response (Figure A) addresses this concern and should be included as Figure 1—figure supplement 4.

I appreciate the analyses included in Author response image 2 in the response, and I think it is valuable information for someone planning to use this method, but I don't consider it strictly necessary (given the relatively modest improvement in accuracy beyond 1 lap). Considering that there are no limits (as far as I know) for supplemental data, and considering that the figure is already made, I see no reason not to include it.

Reviewer #2:

In this revision, the authors have added major new analyses to what was already an impressive demonstration of the first real-time ensemble decoding system for hippocampal replay content. The new analyses are important in delineating the tradeoffs involved in configuring the system, and the conditions that need to be met for adequate performance.

Among these additions is the subsampling analysis which suggests a nonlinear performance improvement around 10 tetrodes, and continued improvement as more tetrodes are added. Also useful is the analysis describing how much sampling of the environment is required to build a usable encoding model (Author response image 2 in the rebuttal). If the authors prefer to not include this figure as a supplement, I think a statement in the text along with some descriptive statistics would be helpful in making the point that for this data set, a few trials appear to be sufficient.

My other comments, such as the suggestion to make the data freely available, have also been satisfactorily addressed.

Reviewer #3):

The authors additions have satisfied my concerns.
