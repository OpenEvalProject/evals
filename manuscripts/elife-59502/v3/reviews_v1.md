# Peer review - Round 1

Editors:
- Megan R Carey, Champalimaud Foundation Portugal

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.59502.sa1](https://doi.org/10.7554/eLife.59502.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This timely study employs an arsenal of tools, from precise behavioral measurement, to careful anatomical tracing, with optogenetic perturbations and large-scale imaging to identify a subset of neurons in the female Drosophila brain that modulate internal state. It links minutes-long persistent changes in behavior with recurrent circuit architecture and persistent neural activity. The paper is a technical tour de force that opens new avenues to explore how lasting behavioral states are instantiated and how these might relate to sustained brain states.

Decision letter after peer review:

Thank you for submitting your article "The Neural Basis for a Persistent Internal State in Drosophila Females" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Laura Colgin as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Michael M Yartsev (Reviewer #1); Marta A Moita (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The full reviews are appended below, and we look forward to receiving a revised manuscript and response to reviewers that addresses the points raised by the reviewers. The most serious concerns, raised by multiple revisions, are synthesized and highlighted under "Essential Revisions," below.

As the editors have judged that your manuscript is of interest, but as described below that additional substantive revisions are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

In addition, we are aware of a related bioRxiv preprint by Schretter et al. and we encourage you to refer to that paper in your revision and/or rebuttal where it may be appropriate to strengthen support for the claims.

Essential revisions:

1) The most serious concerns related to the accuracy of the cell-type identification. This concern comprises the bulk of the feedback from reviewer 2, and related points were raised by reviewer 3 (Methodological points 1, 3).

2) Physiological relevance of optogenetically-induced behaviors, particularly in light of the extremely long duration stimulation (5min). This issue was raised by both reviewer 2 (last point) and reviewer 3 (Conceptual point 2). The long stimulation protocol should be directly addressed in the manuscript. Ideally, shorter stimulation times would be included, but at an absolute minimum the limitations need to be recognized. The Anderson lab showed that a 7.5 s stimulation of P1 neurons (the male analogues of pC1) could produce a persistent activity in a downstream population. If Deutsch et al. tried shorter times and they didn't work, this should be discussed. There were related issues about how naturalistic the elicited behaviors were. This point was raised by both reviewer 1 (point 4) and reviewer 3 (Conceptual point 1).

3) Need for additional quantification and statistics was a general concern, highlighted specifically by reviewers 1 and 3 (see reviewer 1, points 2 and 5; reviewer 3 Methodological points 2 and 4).

The remainder of the concerns, such as justification or toning down of 'emotional state' (reviewer 3 Conceptual point 3), precision of driver lines, and the completeness of the EM reconstruction of upstream and downstream connectivity, can likely be dealt with through textual revisions adjusting the strength/justification of the claims.

Reviewer #1:

The manuscript by Deutsch and colleagues present an intriguing account for the potential role of persistent neural activity in the female Drosophila during social interaction. As a bat researcher I am very jealous by the impressive arsenal employed by the group of researchers ranging from precise behavioral measurement, to carefully anatomical delineation, optical stimulation and through large-scale imaging approaches. Using these, the authors identify an important subset of neurons in the female Drosophila brain that are participating in long-term (minutes) changes in female behavior. This work will serve as a cornerstone for continued study of social behavior and communication and beyond. I congratulate the authors on this spectacular body of work.

Substantive comments: My comments primarily aim towards suggestions for clarifications.

1) What behavioral changes, if any, could be driven by the male song played back to the female but without the male actually being present?

2) The authors state that "the weights of 8 out of 17 parameters were significantly different from zero". To ease the reader, it might be helpful for the author to elaborate how significance was corrected for multiple comparisons and false-discovery rate (FDR)?

3) The authors describe an intriguing clustering of distinct behaviors emerging from stimulation. I wonder if the authors can extend their analysis into behavioral sequences? It particular, if such sequences can be described it would be intriguing to know the relationships between their prevalence and delay of stimulation.

4) Further, it would be interesting to know how the behavioral sequences following stimulation compare to those exhibited around copulation independent of stimulation? Basically how "natural are those sequences"? For example, the author could do something like a reverse analysis and set time 'zero' as the time of copulation (or any other major behavioral event to be consider the 'end-point') and then work backwards looking at the sequences of behavioral events that led to the 'end-point'. How similar are the behaviors leading to the 'end-point' behavior under the two conditions? Are they similar and if so, for how long? Perhaps the correlation between the sequence following stimulation and that not following stimulation decays (or increases) as a function of time? Given the wealth of knowledge from this group about the social behavior of flies I think the readers would appreciate seeing a comparison to the behavior following stimulation.

5) In the imaging experiments (Figure 6) the authors note that they clustered ROIs based on response patterns (Figure 6D). How were those clustered? Was it done by eye? If so, perhaps it would be possible to either validate this clustering using a machine-learning or statistical classification approach or alternatively demonstrate the robustness/reproducibility of the responses within a given cluster? Similarly, for the ROI's exhibiting sustained activity on the minutes scale. It would be helpful to get a sense of this variability in a quantitative manner.

6) Did the authors play male song (and other sounds) to the female during the head-fixed imaging experiments? I realize this is a highly unnatural state for the female but it would still be interesting to know if/how auditory stimulation modulated the responses.

Reviewer #2:

There is a great deal to like about this study, but I do have a significant concern about the classification of pC1 neurons that I feel must be clarified before making any firm recommendation. In addition I think that setting a lower limit on the duration of optogenetic stimulation required to induce persistent activity would be helpful.

The authors claim there are 5 pC1 cells / brain hemisphere and 7 types in all. Does this mean that some cells are so different from left to right that they form different cell types? Although there are reports of left-right differences in the fly literature, this situation seems unusual. Another explanation is that some cells have been incompletely or incorrectly reconstructed from EM data. The amazing recent advances in Drosophila EM connectomics, including the impressive flywire.ai resource presented in this study, means that we are in a somewhat unusual situation in which the exact same pC1 neurons central to this paper have been independently reconstructed from the same brain by two groups (this study; Wang F. et al., 2020, senior author Barry Dickson). Although Deutsch et al. note:

“Because our results are based on automated segmentation followed by manual

proofreading (in 3D), they may differ from results of manual tracing in 2D, even though we have used the same underlying EM dataset.”

If there are large differences in the morphology of reconstructed neurons, then presumably someone is right or wrong. After reviewing the morphologies in these two manuscripts, we believe that the neuron called pC1-Alpha-s in this manuscript is the contralateral homologue of the neuron called pC1e in this manuscript. This neuron does not have a ventromedial branch as presented in Figure 3; but a ventromedial branch is present in the manually traced version of what appears to be exactly the same neuron in Wang F. et al., 2020 – Figure 3D. Based on this comparison we conclude that:

pC1-Alpha-l = pC1d; pC1-Alpha-s = pC1e (Wang F. et al., 2020 nomenclature listed second)

pC1-Med = pC1c; one cell type according to Wang F. et al. – this does not appear to us to affect any of the results in this manuscript.

The presence or absence of this ventromedial branch is significant because the authors use it as a diagnostic feature when determining which EM cell types are present in their genetic driver lines. While describing their driver lines, the authors note:

“pC1-A has a medial projection (red arrow), similar to pC1-Alpha-l neurons found in EM (C); the medial projection was found in 7/7 imaged pC1-A female brains, in both hemispheres. This projection was not found in pC1-S imaged female brains (8/8 brains) – neurons labeled in pC1-S resemble pC1-e neurons found in EM (C).”

If we accept that pC1e and pC1-Alpha-s are indeed the same cell type, then "pC1-A line" most likely contains pC1d and pC1e (since it contains 2 cells per hemisphere). This is also consistent with multi color Flp out data present in Schretter et al., 2020, Supplementary Figure 5E. Furthermore in contrast to the conclusion of Deutsch et al., since it lacks the ventromedial branch, the "pC1-S line" most likely contains something other than pC1e (in Figure 3D it looks like there are both strong and weakly expressing cells and that it might contain all 3 of the remaining pC1 neurons).

This also implies that the behavioral phenotype observed with pC1-A line could be due to either pC1d or pC1e and therefore there is no reason to focus connectivity analyses only on pC1d and not pC1e. And the behavioral experiments done with the pC1-S line might likely reflect the functions of other pC1 types (a, b, c), but not pC1e.

To resolve these issues, further tracing of the neuron currently called pC1e is necessary ideally by comparing it with the published skeleton of pC1e from Wang F. et al., 2020, and/or the Janelia "hemibrain" dataset which now seems to have pC1a-e annotated. Without this, the data presented in Figure 4 is very hard to interpret. An MCFO experiment with both pC1-A and pC1-S could clarify what subtypes (and other neurons in the case of pC1-S) they label, or cite the relevant data for pC1-A from Schretter et al., 2020. In addition the synaptic tracing should probably include both pC1d and pC1e.

As a final note on the subject of EM data, when searching the hemibrain data (neuprint.janelia.org) for pC1 neurons in the course of this review, we noticed that the pC1d neuron in that dataset (which is presumably missing part of its contralateral branch) has 4369 upstream connections and 8945 downstream connections. Furthermore the preprint accompanying that dataset said that they estimate that on average only about a quarter of upstream connections are identified so the true number might be 15-20,000 upstream connections for a single pC1d neurons. In several places Deutsch et al. refer to about 400 pre and postsynaptic sites for their traced pC1-Alpha e.g.:

“After proofreading the pC1-Alpha cell and its input and output cells, and excluding weak connections (using 3 synapses as a threshold, see Materials and methods), we counted 417 presynaptic and 421 postsynaptic sites (Figure 5B, Video 4, and Table 2).”

I think these numbers must refer to presynaptic or postsynaptic partner neurons rather than synaptic sites as otherwise the difference in numbers is too huge. It would be very helpful if the authors could clarify their terminology and/or these differences in synapse numbers. It seems that everyone in the Drosophila circuits field will soon need to know how to critically assess EM data.

To help future readers, we would also suggest that the authors use the convention of presenting brain/neuron images in consistent anterior (frontal) rather than posterior views. Furthermore since Wang F. et al., 2020, have already reported pC1 cell types using a complete analysis of the same EM data with accompanying LM work, we would recommend against introducing a different nomenclature.

Another aspect of the paper that raised questions was the length of the stimulation required to evoke persistent neural activity. Do the authors have data about the effects of shorter stimulation? Was there a specific rationale for choosing 5 minutes? In a very similar circuit in male flies, Jung et al., 2019, use 7.5s of P1 stimulation to create minutes long sustained activity in pCd. It is unclear whether 5 minutes of constant excitation can happen in vivo as opposed to experimental manipulations like optogenetic activation.

Reviewer #3:

This study addresses the important, poorly understood and poorly defined topic of animals' internal states. This is a timely study that constitutes a technical tour the force that opens new avenues to explore how lasting behavioral states are instantiated and how these might relate to sustained brain states. This study, however, falls short of demonstrating the relationship between the artificially induced brain and behavioral states with natural, endogenous ones, as well as establishing a causal link between the recurrent connectivity, the persistent activity and the behavioral states. I have a few concerns, both at the conceptual and methodological levels.

Conceptual concerns:

Although the authors show that artificial stimulation of a specific set of neurons impacts female receptivity, aggressive behaviors, and neuronal activity in a lasting manner, caution in the interpretation of the reported findings is warranted. I believe a discussion that more openly addresses the short comings of their study is important.

1) The authors devote a section of the Discussion to the finding that activating pC1-int leads to an increase in receptivity while at the same time it triggers aggressive behaviors. They mention in this regard that within pC1 neuronal type there appears to be segregation of neurons that drive courtship behaviors and aggression. Still, alternative explanations, that question the induction of a receptivity state are possible, even if flies end up mating more. Stimulation of pC1-int neurons induces behaviors that normally do not occur in a receptive female. It could be, for example, that a stimulated female is not more receptive, but by displaying aggressive behaviors towards the male, the later becomes aroused and more efficient at mating. The authors should show how activation of the female affects courtship behaviors of the male, including but not exclusively regarding song.

2) The authors use a single form of neuronal stimulation: pulsed light at 100Hz for 5 minutes. It is unclear what kind of neuronal activity it induces during stimulation and how this neuronal activity compares to endogenous activity states in general, and during social interactions in particular. This is especially true in the light of a previous study (Zhou et al., 2014) showing transient activity of pC1 neurons to male song and pheromone (this may be different in a female interacting with a male during courtship). It would have been ideal to at least try different activation patterns, namely shorter stimulation protocols. It may be difficult for the authors to add further experiments with different activation protocols. Therefore, the authors should address this in the Discussion.

3) The authors mention in the Discussion that their observations may be in line with an 'emotional state', as they find lasting states that they claim to be scalable, as they report different decay functions of persistent activity across different brain regions. Although the authors do induce a persistent activity state, evidence for scalability is at best weak. Furthermore, there are multiple features of emotional states, such as somatic responses to the external triggers, that are not addressed in this study. Given that the only robust feature they find is lasting neuronal activity and behaviors, I believe the authors should avoid such claims.

Methodological concerns:

1) For the TNT experiments, Figure 1, the authors use the same control for TNT expression in pC1-int and pCd1 neurons. However, according to the table of genotypes used in this study, it seems that TNT is inserted in different chromosomes for the two experimental lines (2nd chromosome for pC1-int line and 3rd chromosome for pCd1 line). Importantly the control has the TNT insertion in the 3rd chromosome and is thus different from the main line of this study, the pC1-int line. It is also not clear to me if the control corresponds to an empty lex-A line or a parental control. The authors should clarify the controls used and if indeed the control does not have the same insertion sites as the mains experimental line. In this case the experiment should be repeated with the appropriate control, as it is our experience in the lab that these issues are often determinant in the experiment's outcome.

2) Figure 4F shows the probability density distributions of fraction of time spent shoving or chasing, for different experimental lines and different times points. They conclude from these plots that differences in behavior across experimental lines depend on the time point looked at. This is potentially an interesting finding, but I could not find the statistical comparisons that sustain such claim.

3) The authors claim that the neuronal subtype aIP-g-b is the most interconnected for cells that are also reciprocally connected with pC1-alpha. However, Figure 5H seems to show that cells of the aIP-g-c subtype show a similar pattern. It is unclear why the authors are singling out aIP-g-b neurons and how would it be relevant to the claims in the manuscript.

4) Figure 6G shows the activity levels in different brain regions at the 3 tested time points (0,3 and 6 minutes after stimulation). They use this information to say that different brain regions show different decay functions. Again, I could not find the statistical analysis that would be required to make such a claim. This is important as it is one of the pieces of evidence used to suggest that pC1 activation may lead to an emotion-like internal state. It is also not clear to me how different decay functions in different brain regions reflect scalability. To my knowledge scalability typically reflects effects of intensity on output, such as the well-established case of fear studies in rodents where stronger shocks leads to more freezing, or higher levels of corticosterone among other scalable outputs (whether these states correspond to fear is still a matter of debate).
