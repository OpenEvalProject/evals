# Peer review - Round 1

Reviewers:
- Frances K Skinner, University Health Network , Canada

## Review text

DOI: [10.7554/eLife.20515.036](https://doi.org/10.7554/eLife.20515.036)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "Lack of evidence for cross-frequency phase-phase coupling between theta and gamma oscillations in the hippocampus" for consideration by eLife. Your article has been favorably evaluated by Timothy Behrens (Senior Editor) and four reviewers, one of whom is a member of our Board of Reviewing Editors.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews, we regret to inform you that your work will not be considered further for publication in eLife at this time. Below we provide detailed feedback for your consideration if you choose to re-submit, and we encourage this possibility.

While all of the reviewers felt that this was an important and interesting paper, they also thought that it was presented in a confusing manner, was limited, and could lead to confusion rather than clarification for the field. Given the contrarian nature of the manuscript as presented, this would not be helpful. The reviewers' overall comments are provided here:

1) The paper presentation should be changed to be less confrontational and completely clear on what is being said and done. A well-crafted manuscript with clarity and sufficient explanations is lacking in the present submission.

A) Specifically, a more detailed review of the literature, a more careful presentation and discussion of the simulation results, and a more careful comparison with the procedures utilized in [Belluscio et al. 2012] is needed.

B) We note that phase-coupling is well defined theoretically from the tools of dynamical systems, but what is not clear is a selective measure of cross-frequency phase coupling. Defining an improved phase-phase coupling measure that detects true coupling and ignores artifactual coupling might be possible. Such a measure – even if it's not the optimal measure – might serve as a "patch" to existing approaches.

C) Finding the optimal phase-phase coupling measure (and assessing its statistical properties) would be a challenge. That is, a consistent and operational way to define how cross-frequency phase coupling can be measured (such that white noise or asymmetrical oscillation would not qualify). Clearly stating the lack of a clear measure as an open problem formally would be of value. In essence, the manuscript would need to make these aspects clear (i.e., present limitations of their work and others, possible fixes/challenges associated with having phase-phase coupling measures), and in this way can identify a methodological issue that's driving incorrect conclusions in the literature, and so be of service to the field.

2) Given that a clear measure of cross-frequency phase-coupling does not exist, a change of title should be considered.

3) A repository (of data and algorithms) should complement the work, and would be beneficial for the community moving forth as analyses, clear understanding and interpretation of artificial and biological data would be available.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for submitting your article "On cross-frequency phase-phase coupling between theta and gamma oscillations in the hippocampus" for consideration by eLife. Your article has been favorably evaluated by Timothy Behrens (Senior Editor) and four reviewers, one of whom is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

In this resubmitted paper on phase-phase coupling, all of the reviewers thought that several concerns had been addressed and suggestions implemented (such as the title change). The reviewers agreed that this is an important article that highlights a methodological issue impacting our understanding of the brain's activity and function. The authors are commended for sharing their analysis methods (on GitHub) and data.

The authors address three points in their paper: a statistical issue (using appropriates surrogate to detect n:m coupling), a conceptual issue (whether n:m coupling can be dissociated from asymmetrical oscillations), and an experimental one (whether n:m coupling is present in hippocampus). The first and last points are well made. However, this is not the case for the second, and other aspects remain unclear as presented. The authors are encouraged to revise and edit their paper to clarify all of the following issues.

1) A clear distinction between true phase versus estimated phase needs to be made as it is confusing as presented. Specifically:

A) As the authors' state, the theoretical quantity of n:m phase locking is well-defined. However, the estimated quantity of n:m phase locking as deduced from noisy neural data is fraught with difficulty. The authors show here that simply applying the theoretical n:m phase locking equation to data produces estimates that – without appropriate statistical tests – lead to spurious results. This is an important conclusion. Future work might seek to improve or correct (somehow) the estimation of the theoretical quantity, or propose a new theoretical quantity that is more easily estimated.

B) The point in the Discussion (subsection “Statistical inference of phase-phase coupling”, last paragraph) that true n:m coupling can be disentangled from asymmetrical oscillation by visual inspection of the LFP or EEG trace, precisely because they will look very much alike does not seem appropriate. This distinction may be hard to make at the macroscopic level (LFP/EEG) and could rather be searched for in how this signal is generated from the activity of distinct neural subpopulations. If the same gamma oscillations that are shown to phase-lock to theta oscillations can be dissociated neurally from theta oscillations (and indeed the authors did a tremendous job in previous publications at showing that hippocampal theta and gamma rely on distinct interconnected networks), then the evidence is rather of favor of genuine n:m locking. In the converse case, if no population selectively engaged in the faster oscillation can be identified, I would say that the asymmetrical oscillation is the most plausible explanation.

2) More detail of why the stripes in phase-phase plot can be produced by asymmetry of the theta waves needs to be provided.

It is not clear how the authors can conclude for the dataset at hand that stripes in phase-phase plot are due to the asymmetry of the theta waves and not to genuine gamma activity (Results, eighth paragraph). The authors seem to somehow tie this possible caveat to the stripes in phase-phase plots. However, stripes are just a visual inspection for maintained relationship between the two phases, just as (properly controlled) Rnm should measure.

3) The discussion about the caveat of asymmetrical oscillations is unsatisfying for the following reasons:

A) This point is made in the middle of the analysis of experimental data. Since this has nothing to do with the data at hand, in which no evidence for phase coupling was found, this obscures the message. A separate section should be devoted to the caveat of the asymmetrical oscillations, possibly before the analysis of experimental data.

B) The point should be clarified, by not only focussing on the presence of stripes for asymmetrical oscillations, but by explaining conceptually why this dissociation emerges. Possibly it could be illustrated by showing how an asymmetrical wave resembles the sum of multiples sinusoids at the fundamental and harmonics frequencies n:m locked to each other (and possibly with also some phase-amplitude coupling, see Kramer et al.).

4) Any differences between the measure of the authors and that of Belluscio's needs to be made clear. As specified by one of the reviewers:

It is not quite clear whether the methods used are exactly the same. In Belluscio et al., I think the counts were performed first for each surrogate (corresponding to a specific time-shift), and then the distribution of counts over the distinct time-shift was computed for each bin (i.e. Single Run analysis, which should be the correct method). By contrast, it seems that here – not quite clear in the text – surrogates for distinct time shifts were merged before counts were done in Figure 5 and Figure 4—figure supplement 1 (i.e. Pooled analysis, which of course averages the count and creates many false positives). [Note that I use Single Run vs. Pooled terminology to refer to whether the metrics was computed for each surrogate independently (Single Run) or for merged data, the metrics applying yo either Rnm or counts.] I hope that I am being wrong here. Otherwise that would seriously limit the conclusions of the author about invalidating Belluscio's findings.

Note that there is still a statistical problem with the Single Run analysis of phase-phase counts, which relates to the absence of a correction for the number of tested bins (either for a given theta phase or across all theta phases). In any case, the p-value in Belluscio et al. reaches very low value (some p<10^-10), which would probably resist proper corrections. If this is the case, that would provide statistically sound evidence for n:m coupling (asymmetrical theta being still a possible confound). Do the authors observe such low values in their own dataset? Could they remove statistical significance in the stripes in white noise using an appropriate correction? Or does this deceiving statistical significance come from yet another explanation?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "On cross-frequency phase-phase coupling between theta and gamma oscillations in the hippocampus" for further consideration at eLife. Your revised article has been favorably evaluated by Timothy Behrens (Senior editor), a Reviewing editor, and three reviewers.

The manuscript has been improved but there are remaining issues that need to be addressed. All of the reviewers appreciated the authors' revisions and thought that this work could serve as a useful cautionary tale for neuroscientists as well as a useful starting point for continuing work. Even though it was felt that the results were not completely satisfying, it was also felt that it would be of great benefit in preventing researchers from wandering down the wrong analysis path. It was further noted that if this paper were presented as a statistics paper it could be improved more but then it would probably be less read and absorbed by the neuroscience community for some time.

An overall suggestion is that the authors should be more cautious in their interpretation and clearer about there being room for further progress in editing their manuscript.

Specific issues to address are:

1) The Abstract would benefit from significant revisions considering the various changes already done, and ones to be done. Sentences that should be targeted are: "filtered white noise has similar n:m phase-locking levels as actual data", and "the diagonal stripes in theta-gamma phase-phase histograms of actual data can be explained by theta harmonics".

2) Validity of Belluscio's analysis – overall conclusion:

A) In the rebuttal, the authors consider that the analysis by Belluscio is intrinsically flawed rather than being simply not well controlled statistically. I tend to defend the alternative option (clearly here I do not refer to the analysis of Mean Phase-Phase Plot, which the authors have convincingly showed that is flawed, but to the tests on phase counts; I also want to reassure the authors that I really do not have any personal motivation to go one way or the other). My intuition is that the presence of one single significant count in the phase-phase plot, if appropriately controlled for multiple comparisons, would provide a valid statistical measure. In essence it would not simply detect the presence of stripes (which surrogate run also feature) but measure whether their amplitude is larger than those of surrogates. This could be shown in a quite straightforward way by looking whether significant points in phase-phase plots obtained from white noise persist when a correction for multiple comparisons is applied. The authors seem to agree that they would not. (As for the type of correction, the Bonferroni method that the authors refer to looks too conservative as the bin counts clearly are non-independent; less stringent correction such as FDR or Holm-Bonferroni may be preferred). A count is not a metric for n:m coupling for sure, but it can inform of the particular concentration of the high frequency phase at one specific phase of the high frequency phase. More importantly, what matters here is not a metric of the coupling strength, but a reliable statistical test that selectively detects coupling, and my intuition is that counts in the phase-phase plot may provide one. If a simple correction can be applied to give a sound statistical test, this could allow Belluscio and colleagues to look back at their data and see whether the significant counts indeed resist correction for multiple comparisons.

B) About the very low p-values in Belluscio's data, the authors suggest that "it is possible that, by analyzing a longer epoch length, the influence of theta harmonics becomes more apparent and would lead to lower p-values, while the effect of the filtering-induced sinusoidality is washed out for both actual and surrogate epochs (of the same length)."

Well the manuscript previously demonstrates that n:m coupling measures as well as phase-phase plots cannot tear apart asymmetrical waves from true cross-frequency coupling. Thus, if indeed p-values remain lower than threshold when controlled appropriately, it could equally be due to asymmetrical theta or true theta-gamma phase coupling, but the latter could not be dismissed.

3) The reason for stripes in the phase-phase plot of hippocampal data:

A) In the manuscript authors state that "the diagonal stripes in phase-phase plots are due to theta harmonics and not to genuine gamma activity." If it were true harmonics, that would imply a consistent phase relationship between theta and gamma over sustained periods (not just over small periods as for white noise), i.e. would test positive for n:m coupling. So in my opinion here the effect is rather due to the temporary n:m alignment of phases, just as for white noise. In other words, stripes emerge also when analyzing white noise despite there being no harmonics in the signal.

B) In the rebuttal, the authors defend that "Believing in two different and genuine gamma activities – one coupled at 5 cycles per theta, the other at 4 cycles per theta – would go against the parsimonious principle." (this is when theta frequency evolves). However, as established by theoretical studies of coupled oscillators, n:m coupling is not a fixed property of the network but emerges as a combination of oscillator intrinsic dynamics and the characteristics of the connectivity pattern. See for example Arnold tongue: if we assume there is just one fixed gamma, a fluctuating theta and fixed connectivity, it is perfectly normal that n:m coupling will shift from 1:5 to 1:4 if the lower oscillator accelerates and the ratio of frequency goes from around 5 to around 4.

4) Asymmetrical theta vs. phase-coupled theta-gamma in general

I am coming back to the authors' comment on this in the rebuttal, although this is no longer present in the manuscript. This is a comment for the authors benefit and speaks to the overall comment mentioned above. Sharp edges in LFP/EEG are not by itself an indication that we are measuring a single asymmetrical oscillation as the superposition of a slow and a fast n:m coupled oscillation can also give rise to sharp edges (Figure 4C; note that this can even be obtained with just two oscillations). Thus, sharp edges is no more a selective feature of asymmetrical oscillations than n:m coherence is selective of phase-coupled oscillators. In other words, visual inspection cannot tell us more than statistics.

5) It looks like "Random Perm" is more powerful test than "Time Shift", as mentioned in the first paragraph of the subsection “Lack of evidence for n:m phase-locking in actual LFPs”. If this is the case then it could be stated as a conclusion of the work that "Random perm" should be preferred over "Time Shift" (and of course of the "Scrambling" procedure), as it is less likely to miss existing effects (lower False Rejections rate).

6) Conclusion: the very new paper by Lozano-Soldevilla and colleagues (Frontiers Comp Neuro) provides another example of spurious cross-frequency coupling measures due to asymmetrical oscillations, could be worth referencing.
