# Peer review - Round 1

Editors:
- Floris de Lange, Donders Institute for Brain, Cognition and Behaviour Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.41541.022](https://doi.org/10.7554/eLife.41541.022)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Brain Signatures of a Multiscale Process of Sequence Learning in Humans" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Floris de Lange as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Timothy Behrens as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Marta Garrido (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Maheu et al. perform a systematic and thorough investigation of the effects of item frequency (IF), alternation frequency (AF) and transition probability (TP) of auditory events on the MEG response in different time windows. They find that IF, estimated over long temporal windows, explains the brain response in very early auditory sensory processing, whereas TP, estimated over progressively shorter time windows, explains the brain response at progressively later time points.

Essential revisions:

1) Task-dependency of results?

The participants were explicitly required to judge the predictability of the patterns. It is therefore very likely that the observed brain responses (especially the later ones) reflect this perceptual state and therefore cannot be interpreted as automatic processes reflecting the brain's modus operandi as a statistical learning machine. It would have been far better, if the task performed by participants was unrelated to the sequence dimension being investigated, e.g. some sort of omission detection task? Or an entirely unrelated (e.g. visual) task. The present choice limits the interpretation of the results. It will be important to better qualify what inferences can and cannot be drawn on the basis of these data.

Related, the major findings that (1) brain responses reflect the statistics of sound sequences (2) early responses reflect adaptation-like effects whereas later effects reflect increasingly complex models is not new. The authors themselves review lots of relevant literature. Notably, they fail to relate their results to the modelling work of Rubin et al., 2006. Though the paper is cited in the present report in the context of the claim that brain responses are larger for deviants than standards, the actual work has employed extensive modelling to understand how neural responses to sequences similar to those used here are affected by the preceding history. Notably, they have concluded that responses are affected by quite a lengthy context (more than 10 tones) but that the representation of the transition probabilities is coarse. Is it possible that the different effects observed here are driven by the behavioral task (see my comment no. 1, above)?

2) Choice of time window:

The spatial filter analysis is focused on the late time window. The one that is most contaminated by the behavioral task. What is the justification of using that time window and not and earlier one?

In previous and later figures, IF and AF seem to be doing all the work at much earlier time windows.

3) Various methodological concerns: a) Figure 5 the time course of max R2 nicely aligns with the three MEG peaks. Could it be that the appearance of "3 distinct time windows" is just a consequence of MEG power?

b) Figure 2 shows significant differences between conditions (B vs. A, and Rep vs. Alt) overlaid on MEG topography for the 4 different sequence conditions. While it is interesting to observe the differences in topography for the MEG difference wave across sequence conditions, this remains a qualitative observation. Statistical maps would be required to really pin down whether those patterns are indeed significantly different between conditions, and if yes, where in space-time. For example Figure 2B, it appears that from 400 ms onwards the contrast of Rep vs. Alt is a little different between fully stochastic and repetition biased sequences, but, is this difference (interaction) really significant?

c) Figure 4 shows a remarkable similarity between empirical MEG data and the surprise levels predicted by the transition probability model for 500-730 ms, which is very impressive and pleasing. It was unclear, however, whether this time window was a priori chosen or whether the whole window was fully explored with appropriate multiple testing correction. If a priori chosen then more explanation for the rationale is needed given that a) strong evidence exists for MMN window 100-250 ms and b) Figure 3A shows significant differences for earlier periods – in fact for the alternation biased condition no significant differences between rep and alt exist beyond 400 ms so that's difficult to reconcile with the later time window. If based on Figure 5D then why not from 160ms from which point TP wins?

d) Still related to the findings in Figure 4 that related to a local integration window parameterised by ω =6. My understanding is that this parameter was optimised for each subject and that 55 values (as many as the max of observations made) were explored. How consistent was this value across participants (ω =16 is also mentioned)? It appears this was also optimised for each of the 3 times windows – can this be made more explicit and also again whether that was consistent over subjects. Did it correlate with their task accuracy (more accurate prediction judgments on upcoming stimuli for greater ω)? This is not necessary but could strengthen the interpretation.

e) The fact that global statistic violations such as item frequency violation modulates earlier (not late) responses matches nicely Garrido 2013 narrow/broad Gaussian paper showing that variance (a global statistic) modulates early latency responses. However, it appears at odds with Bekinschtein's 2009 local-global paper showing that global violations modulate P300 (not MMN). Can we reconcile these findings? The Discussion appears to point to chunk vs. continuous sequences as potentially explaining the divergence (which would again be consistent with Garrido 2013), but it still remains unclear why would chunking make such a difference?
