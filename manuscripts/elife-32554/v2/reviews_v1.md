# Peer review - Round 1

Editors:
- Timothy E Behrens, University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.32554.016](https://doi.org/10.7554/eLife.32554.016)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Phase-tuned neuronal firing encodes human contextual representations for navigational goals" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Timothy Behrens as the Senior and Reviewing Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Electrophysiological studies in the rodent hippocampus have provided compelling evidence for neural phase coding during spatial navigation. Such studies observe spiking activity to be coordinated with specific phases of locomotion related theta oscillations. Observing similar coding properties in the human medial temporal lobe is exceedingly difficult. In their manuscript, Watrous et al. attempt to address this challenging question by recording spiking and LFP activity in epilepsy patients, while performing a virtual navigation task. Naturally, these data are highly novel and of great utility in establishing evidence of spike-phase coding in the human brain. The study is a clear advance on the authors paper which reported the LFP data, as they are now able to report the relationship between spiking and LFP activities. The study also proposes new methodologies that, subject to some concerns below, will likely be very useful to the field. All told, the reviewers agreed that it is an exciting and strong study.

Essential revisions:

There were many overlapping concerns amongst all three reviewers. I have tried to cluster them into themes where the reviewers are making overlapping points so that you find it easier to address the concerns together. You will see that although there was a consensus that the data are potentially extremely exciting, there was also a frustration that much of the data is hidden in the presentation, and that a number of technical issues need to be addressed.

Behaviour:

1) As a general comment, much of the results presentation is without any reference to the experimental task conditions or the anatomical sites of recording. While I appreciate the authors are trying to be concise, it does seem that talk about 'neural coding' requires clear grounding in what is being coded and where. Is it the author's key prediction that specifically the hippocampus should display spike-phase coupling during navigational goal planning, as apposed to other task conditions? Is this motivated by rodent work?

In a related comment, evidence for spike-phase coding would suggest a strong sensitivity to behavioral state, such that a critical test for the authors is comparing their analysis to different task periods, e.g. planning vs. navigation vs. arrival. These comparisons are important as the evidence shown for goal information coding is (despite looking large) a difference of ~1 spike between the preferred and non-preferred goals.

2) The link to behavior is unclear. No task description and behavioral readout is provided and the phase-coding theory could be epiphenomenal. This is particularly concerning given that most (93%) exhibit a very slow theta rhythm, which is unusual – even human studies often find theta around 6 Hz.

Technical concerns:

1) The authors introduce a new algorithm to separate oscillatory activity from 1/f fractal components. While this approach is timely and important, introducing a new algorithm requires some kind of validation that it actually works. MODAL seems to be a combination of 1/f slope fitting (e.g. like Gao and Voytek, NeuroImage) and the Cohen frequency sliding method and should be compared against established algorithms such as CGSA (coarse-grained spectral analyses, e.g. He 2010 Neuron) or IRASA (Wen and Liu 2016 BrainTopography and JNeuro). Reviewers agreed in discussion that it was important to validate the new algorithm.

2) The authors use a novel method for tracking the shifting frequency of oscillations. Is there evidence the authors can provide that supports phase-coding when the center frequency of an oscillation is unstable? In visual cortex, work by Xing et al. (2012) has argued that the variability in peak frequency and stochastic bursting nature of gamma oscillations greatly limits their coding ability. A similar critique may be applicable to the author's data.

3) The authors previously used HFA (high gamma) as a surrogate marker for spiking to demonstrate phase-coding in the MTL. Here they extend it to SUA. It would be of great interest to directly compare these metrics and to develop a better understanding how phase coding (at the population level) guides HFA, MUA and SUA. The authors could then test for how much variance is explained by theta alone (power and/or phase) as well as theta-HFA, theta-MUA and theta-SUA coupling.

4) It is unclear if there were any power differences in the theta band that might explain why some sites show more pronounced interactions. Differences in signal-to-noise could affect phase estimates.

5) Were LFPs and units extracted from the same or adjacent wires? Do the effects still hold true when the LFP is extracted from the most distal depth electrode?

6). Why was the frequency range limited to <10 Hz, which seems arbitrary given that the authors detected individual oscillations and e.g. work by the Miller group indicated a relevance of alpha/beta oscillations.

7) Was the seizure onset zone excluded or only epileptiform epochs? The Gelinas algorithm only detects sharp spikes, how did the authors deal with slowing? This could confound the 3 Hz range.

8) Was the theta oscillation sinusoidal (e.g. Cole and Voytek)? How did the authors deal with sites that had multiple low frequency peaks?

9) The difference score (DS) is not defined and it is unclear what this metric does.

Presentation of data:

1) The authors present a multitude of analyses and findings in only three figures and most analyses are not well described making it difficult to assess what was actually done. Figure 1 is merely a schematic to illustrate the oscillation detection method, Figure 2 shows summary data without providing any anatomical specificity and Figure 3 shows only a few single trial examples. Given that eLife does not have specific space constraints, a more careful and detailed presentation of the data would help to assess the findings.

2) Methods and results lack clarity. For example, the authors mention a decoding approach without providing any additional information on what was done or what the results were. From the description it would be impossible to replicate these analyses.

3) At several points in the Results there's a lack of specific details critical to interpretation. For example, in the last paragraph of the subsection “Phase-locked neuronal firing”, the authors mention 48 neurons that displayed two distinct oscillations. It's not clear where/why these 48 neurons are only mentioned, where they were recorded from, or what the two frequencies they are referring two. This is then followed by analysis that points to single subject data in Figure 2A, and a p-value without any reference to the test performed, and a claim of support for the SCERT model. As above, I think the author's attempt at concision has left out needed information for the reader.

4) The figures jump between data from different subjects (e.g. Figure 3) making it hard to follow an example finding across analyses for one subject, as an exemplar of the group data. Indeed much of the group data exist as p-values in text making it hard to get a sense for the effect size of the results and their across subject variability.

5) No waveforms are shown and it is unclear what kind of cells the authors isolated, how they were selected and grouped. Right now, it feels like a black-box approach and no information is provided to assess the data quality.

Further analyses:

1) How did theta differ between PFC and MTL ROIs? Was there any interaction?

2) Frontal cortex results. The statement is made that "phase coding cells were not significantly clustered by brain region". This should be clarified – so this means phase-coding cells were found in frontal cortex? If so, how many and where? Were their properties different given that the emphasis here is on MTL theta, which wouldn't be present in the non-MTL recordings.

3) It would be of great interest to assess the relationship of evoked firing vs. ongoing activity. Would one observe a theta oscillation in a spike-triggered average or is some of the very slow theta (3 Hz) driven by the stimulus (spatial navigation) or saccadic/micro-saccadic eye movements, which occur at a similar frequency. As it stands, one cannot rule out that the observed effects are solely stimulus-induced.

4) What is the relationship between the "phase coding cells" (28/158) with the phase-locked cells (n=119) ? Are the 28 a subset of the 119? More broadly, I wonder whether cells that have a phase-code could qualify as phase locked using the definition used to identify the 119 cells, since these cells (by definition) have a single preferred phase. Phase modulated cells, however, change their phase preference as a function of task. This issue would benefit from clarification.

5) Only the cells that do not exhibit a rate code for navigational code were examined. Are there also cells that have both a rate and a phase code?

Interpretation:

1) The Introduction and Discussion is too heavily focused on the "SCERT" theory – while this is certainly an interesting framework, many others have proposed similar ideas so the strong focus on this very recent "theory" is distracting and does not do the importance of this finding justice. This can be solved by more careful writing. For example, "it is unclear whether phase coding manifests in MTL neurons" is too broad of a claim, as demonstrated by the references that the authors already cite that show that MTL neurons prefer certain phases.

2) It would be helpful if the authors provide explicit predictions made by the SCERT model. I'm not sure it's clear what findings would refute their model, other than a null result of phase influence. For example, does the SCERT model make predictions about which frequencies should be influencing spiking? Or is it a more general claim that any oscillation is sufficient. Similarly, how does the model relate its framing of encoding/retrieval behavior to navigation, and specifically goal planning?

Anatomy:

1) It would be helpful if the authors made clearer reference to the anatomical sites of recording during the presentation of data. Going through the results it is often unclear where units are coming from and if they are being pool across regions.

2) No anatomical information is provided on where probes were exactly located.

3) "Frontal cortex" is too broad of a term, given the very specific frontal areas that were recorded.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Phase-tuned neuronal firing encodes human contextual representations for navigational goals" for further consideration at eLife. Your revised article has been favorably evaluated by Timothy Behrens (Senior and Reviewing Editor), and three reviewers.

Thanks for the substantive revisions. We all agree that they have dramatically improved the paper, but there are a number of outstanding concerns from the reviewers. I am passing these on verbatim to avoid confusing matters.

Reviewer #1:

The authors have provided a thoughtful response to reviewer comments, including several new analyses. The addition of supporting text clarifies several prior uncertainties regarding task structure, anatomical specificity and group data. I have a few remaining comments.

- The authors should qualify their reporting of phase-coding; it appears to occur in a small subset of cells, whose firing rates are sparse. Only ten percent of cells showed decodable goals from spiking phases, this should be more explicitly acknowledged throughout the manuscript. This statistic also needs to be clarified in relation to Figure 4C (caption is not clear).

- Authors note they "…were able to test if the spike-LFP phase locking was specific to an individual frequency band or present for both bands". They then report 12.5% of cells showed "frequency-specific phase locking, showing phase-locked firing in only one LFP frequency band". But it's not clear what the split is between the two frequencies for this value, and if we should infer the remaining percentage is for locking to both frequencies or none?

- The authors provide some benchmarking for the MODAL analysis technique, however, I would encourage them to pursue a separate publication of the method in the future, where the strengths and limits of the technique are rigorously quantified.

- ANOVA results are not consistently reported with degrees of freedom and F statistic – presented in some cases and not in others. This needs to be harmonized throughout the manuscript.

Reviewer #2:

The authors addressed all concerns in great detail, however, in some cases their responses fall a bit short and a few more details would help.

E.g. Technical concerns #1: applying their new algorithm to a different dataset does not constitute 'validating' it against a different established algorithm.

Technical concerns #3: While the authors demonstrate a correlation between HFA and spiking, they do not show the more obvious (which their Discussion actually implies): Phase coding as observed by Watrous et al. (2015) in eLife based on the HFA can also be detected based on unit activity. While the authors imply a direct link, an empirical demonstration would be more convincing. In other words, do phase-locked HFA and phase-locked spikes both support phase coding, i.e. are they separate processes or do they constitute the exact same process? This point remains unclear.

Technical concerns #5: Unfortunately, the authors state that they cannot access the macro data, which is puzzling per se, however, in many primate experiments (in particular on phase coding, e.g. Siegel et al., 2009), one typically uses phase and firing from adjacent and not the same wire.

Technical concerns #6: It seems trivial to open the band-pass up to 30 Hz and not restrict it to 10 Hz. This would allow for a better assessment of the data – in particular, since the authors show a beta band oscillation in Figure 2.

Reviewer #3:

The authors prepared an extensive and detailed revision that addresses most of the concerns I had raised. The manuscript reads much better now, and is more straightforward to understand now for me.

Beyond reproducing earlier findings, this manuscript shows two novel aspects: i) a novel theta-period detection algorithm is applied, which reveals 3-5Hz theta-frequency bouts in a number of human MTL and cortical areas. ii) it is shown that relative to these detected periods, a number of neurons phase-lock their spiking activity and the phase of this spiking activity is indicative of which goal is currently sought in a navigation task.

1) It is of some concern that the authors noted that it was not possible for them to know the seizure onset zone of the patients included. Having this information would have allowed to perform the critical control whether the same phenomena (phase locking and frequencies of detected theta periods) hold as a function of whether an electrode was inside vs. outside the seizure onset zone (i.e. to argue vs. the slowing). This information is typically easily accessible from the clinical record, so it is unclear why this was not done. Alternatively, perhaps this analysis could be done by using only neurons located on wires where the automatic "epileptic spike" algorithm did not have any hits?

2) The principle result is that for a subset of neurons, the phase of spikes is informative about the current navigation goal. It is further argued that for most such neurons, the firing rate was not informative about the current goal. However, I cannot see how it was excluded that what explains the differences in phase are aspects of the underlying LFP? i.e. the question is, for the neuron-LFP pairs for which the phase was indicative of the goal, was the LFP power used to define the phase also indicative of the goal? One argument the authors present to argue about this potential confound is to show that the number of detected oscillatory bouts does not correlate with whether a cell was phase coding (subsection “LFP-spike phase coding of goal information”). But it wasn't clear to me what exactly was measured here – please clarify. Why not specify for how many cells the detected nr bouts was indicative of the goal?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for submitting your article "Phase-tuned neuronal firing encodes human contextual representations for navigational goals" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Timothy Behrens as the Senior and Reviewing Editor. The reviewers have opted to remain anonymous.

– Reviewer #2:

It remains striking that the authors find that HFB and SUA are independently locked to the same theta rhythm, but are not correlated. This is surprising given their previous conclusions from Watrous (2015eLife) and no explanation for this finding is provided. Given that this is a direct follow-up submission, this should be discussed in more detail. In particular, given the results by Rich and Wallis (2017) and Watson (2017, European J Neurosci) it is concerning that the authors went through an elaborate analysis pipeline, which included the development of a new algorithm MODAL, to obtain these results, which are questionable if one assumes that HFB activity reflects MUA firing. What is the interpretation on the physiological level and how can this differential HFB and SUA coupling to the same theta rhythm come about? How would one reconcile these differences in terms of a mechanism?

Reviewer #3:

My remaining issues were addressed.
