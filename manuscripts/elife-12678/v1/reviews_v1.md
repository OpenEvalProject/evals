# Peer review - Round 1

Editors:
- Michael J Frank, Brown University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.12678.013](https://doi.org/10.7554/eLife.12678.013)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for choosing to send your work entitled "Dopamine controls stimulus generalization in the human hippocampus" for consideration at eLife. Your full submission has been evaluated by Timothy Behrens (Senior Editor), Michael Frank (Reviewing Editor), and two peer reviewers. Based on our discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife in its current form.

All reviewers and editors expressed interest in the findings and framework, but questioned the level of advance over and above what your group has published in 2012 with a similar model and relation to hippocampal-striatal connectivity. The main issues that came up in the review discussion (some of which are reiterated by the individual reviewer comments below) are as follows.

– First and foremost, while the dopaminergic effect is of real potential interest, all were concerned that there was no observable effect of the drug on generalization behavior, but only through the lens of the model parameters. In general a model can certainly be helpful to refine behavioral analysis, but (1) it has to be shown to fit the data well before its parameters can be interpreted, (2) it should be compared to alternative potential models, and (3) if both of these are successful the winning model should then guide an analysis of the behavioral data that would reveal the significant effects. Reviewers were also concerned that other (unmodelled) factors (e.g. new learning during testing session affected by dopamine) could be at play which make it less clear that dopamine is specifically changing the hippocampal generalization gradient, and that the current findings weren't well integrated with your previous findings.

– The specificity of the effects was not fully established. Reviewers suggest control analyses that would address whether indeed what was seen in the hippocampus is something that is unique to the hippocampus, or whether it was a general effect of pharmacology in BOLD signal that was not observed elsewhere.

Reviewer #1: This study examined the role of dopamine in modulation of perceptual generalization, combining pharmacology, fMRI and computational modeling.

On the first day participants trained on a visual discrimination task. On the second day they were tested for generalization of the training to new samples varying in similarity to the trained items. The generalization test took place either under drug (D2 receptor blocker) or under placebo, in a between-subject design. The results suggest that both groups generalize similarly, overall. But the application of a computational model of generalization revealed subtle but interesting differences in the width of the generalization gradient, with a narrower gradient in the drug-treated group. This difference in the generalization gradient was associated with differences in BOLD activity in the hippocampus, with the drug group showing a weaker generalization-related BOLD response.

Overall this is a solid and informative study using a convergence of methods to address an interesting question. I have just a few comments:

1) As with any pharmacological study, one must raise concerns about selectivity. How do you know the effects of the drug are not due to global differences in dopamine transmission, that are having an impact on BOLD activity in multiple places in parallel with (but not necessarily related to) the subtle differences in behavior? The study already addresses this somewhat by showing selectivity of effects on functional connectivity between the hippocampus and the midbrain, but not with the striatum. And the findings ruling out mere differences in perception also help address this point. But similar control analyses are also needed for the generalization gradient, to determine whether there is really a selective effect of the drug in the hippocampus, as the authors currently conclude. For example, Paz and colleagues have suggested an important role for the amygdala and the PFC in perceptual generalization. These regions are also targets of midbrain region and it would be useful to know whether or not they show parallel effects.

– Related to the point about possible global differences between drug and placebo, were there any reaction time differences between the groups?

2) The Discussion makes the important distinction between associative and perceptual generalization, but this distinction is muddled in the introduction where the two appear to be conflated. It will help readers if this distinction is clarified earlier on.

Reviewer #2: The study by Kahnt and Tobler investigates the role of dopamine in stimulus generalization using fMRI, computational modeling and dopamine blockade (D2R). Two groups of subjects first learnt which of two oriented gabor patches (CS+ 39 deg, CS- 51) were associated with positive or neutral outcome. Following drug (PA) or placebo (PP) administration they then performed the generalization test where they responded to 15 different orientations not presented during training (between 17-73 deg; no outcome presented) with multiple repetitions of each item. Main findings of interest: i) as in their (2012) and other studies a classic peak shift generalization curve was observed (i.e. away from CS-) ii) whilst there was no significant difference between the groups in the raw data, groups different when a similarity based model of generalization was used (i.e. excitatory generalization coefficient was larger in PP group; n.s. trend for inhib coefficient). Iii) Modelled prediction errors during generalization were observed in the hippocampus, and greater in the PP group. Further there was a reduction in midbrain-hippocampus functional connectivity in the PA group, that was associated with individual differences in modeled inhibitory coefficient. Overall findings are discussed as implicating dopaminergic circuit and hippocampus in flexible stimulus generalization based on neuromodulatory state.

This study addresses a question of importance and the findings are potentially of interest. However, I have some concerns about the interpretation of the findings (see below). In addition I am not sure whether the current paper represents a substantial enough advance above their published 2012 work (where an analogous computational model was used and interactions between the hippocampus-striatum implicated) to warrant publication in eLife. The main novel aspect is the dopaminergic manipulation, but as I see it there are some inconsistencies between the 2012 and this paper which make it difficult to have a coherent picture.

Major concerns:

Given the effect of drug on generalization curve is relatively small (i.e. only detectable by model fitting), it seems important that the authors consider alternative models. If these also showed a significant difference in group parameters this would make the findings appear more robust. In particular, exemplar models (e.g. Nosofsky, 1984) and models of similarity based generalization (e.g Shepard, 1987) typically use an exponential similarity function. Was there a particular reason for opting for a Gaussian function instead, and could the authors please provide results from an analogous model with exponential function for comparison? This would be particularly useful given the possible relationship between exemplar models and the hippocampus.

One important claim of the paper is that dopamine widens the generalization curve (e.g. modeled by increase in excitatory coefficient relating to width of Gaussian). Whilst this makes sense at face value, I wonder whether that there are potentially complicated interactions at play during the generalization test that may (also/instead) be affected by dopamine. In brief, and detailed subsequently: dopamine is known to affect the strength of hippocampal encoding and perhaps this is the reason for changes in the generalization curve. This would be important (apart from changing the mechanistic explanation) because it suggests that the dopamine/hippocampal effect is to some extent paradigm specific: it does not apply to "one-shot" generalization (perhaps more naturalistic), but only under settings where lots of stimuli are presented and generalization required.

To state this in more detail: subjects are learning during the generalization phase: i.e. storing new representations of the previously unseen test items and their predicted values (which are being constantly updated). It certainly seems conceivable that in this setting the hippocampus is important in setting up these representations, and the behavioral generalization curve then reflects the concurrent retrieval of these representations in parallel (i.e. as in exemplar models) to compute an EV for the current stimulus (as the authors suggest). My question is how a difference in the strength of these item representations in the hippocampus could influence the generalization curve? At present this is not modeled, and given the known role of dopaminergic modulation of hippocampal encoding this seems an additional factor to consider. Assuming the authors agree with this, could they incorporate this as an additional parameter in the model (distinct from the learning rate, which applies to value updating), and report the results?

It seems important for the authors relate these findings more closely to those of their previous study, which is not discussed in detail at present and consider possible inconsistencies. Firstly, no hippocampal PE signals were reported in that study: can the authors comment on any reasons for why this might be the case (e.g. paradigm differences etc? Secondly, stronger hippocampal-striatal connectivity in that study was associated with narrower generalization: here stronger midbrain-hippocampal connectivity was associated with broader generalization. Can the authors comment on the difference in findings, and also whether the midbrain-hippocampal connectivity result is replicable in the original dataset?

Hippocampal activity is reported to correlate with generalized PE during test phase. Given that no outcomes are presented, is the PE not equivalent to EV? If so, it would be worth stating this, partly because in recent years a number of studies have found EV to be reflected in hippocampal activity.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for resubmitting your work entitled "Dopamine regulates stimulus generalization in the human hippocampus" for further consideration at eLife. Your revised article has been favorably evaluated by Timothy Behrens (Senior Editor), Michael Frank (Reviewing Editor), and two reviewers. We all agreed that the manuscript has been substantially improved and that you have done a nice job addressing the main issues. Still, there are a few remaining issues that need to be addressed before acceptance, as outlined below by each reviewer in turn.

I highlight two points here.

First, both Reviewers appreciated the new analyses showing specificity of the effects to the hippocampus, but each would like to see a follow-up analysis to further evaluate this specificity. Reviewer 1 notes that any strong claims regarding specificity need to show a region by drug effect interaction and not just a significant effect in hippocampus and null effect elsewhere (see e.g., Nieuwenhuis, Forstmann & Waenmakkers 2011 Nature Neuroscience who emphasize this point strongly). Reviewer 2 asks whether you also see specificity in the PPI analysis.

Second, Reviewer 2 would like to see a somewhat more fleshed out motivation for the prediction error analysis and to clarify whether the PE was evaluated at the outcome or during the choice.

Please address these and the other comments below, and we will be able to make a decision without further review.

Reviewer #1: This is a resubmission of a previous paper relating to the role of the hippocampus & dopamine in stimulus generalization. Overall, the authors have been very responsive to the concerns I had with the original paper: I was convinced by the new findings that distinguish the effect of drug in the absence of a model (through differences in kurtosis), the results of the inclusion of a similarity based model with exponential function, and consideration of learning during test as a possible explanatory factor. Also the discussion of the current findings with respect to their previous paper is informative.

I have few remaining concerns:

– The authors report a significant difference between drug/placebo groups in terms of prediction error signals in the hippocampus, but report that this effect was not significant in other regions showing prediction error signals (e.g. amygdala). Can they confirm whether there was a significant interaction (i.e. drug/placebo x brain region), for example in an appropriately constructed region of interest analysis? This seems important to demonstrate the specificity of the drug effect on PE signals.

– They observe that midbrain-hippocampal functional connectivity correlates with the inhibitory (but not excitatory) generalization coefficient of the model. Although there is a comment that relates to this in the Discussion, could the authors expand on why the behavioral findings between drug groups should be driven by differences in the excitatory coefficient, but not the functional connectivity findings? Also was there a significant difference between placebo and drug group in this correlation?

Reviewer #2: The authors did an extensive revision in which they addressed the main concerns raised in the last round, particularly the lack of a behavioral difference under drug and the lack of specificity of the fMRI findings. The result is an interesting paper presenting solid findings that are likely to be of broad interest.

I have a couple of remaining comments:

1) The rational for the prediction error analysis in the test phase is not spelled out clearly enough. Perhaps I misunderstood, but I thought the authors were arguing that the effect of dopamine at test is essentially on the retrieval of a learned representation, the generalization itself, and that it is explicitly not related to trial by trial updating during the test phase. This leaves me questioning what the link is to the prediction error at the outcome phase rather than the response/choice at the stimulus presentation phase.

2) The selectivity of the fMRI effects to the hippocampus are reassuring. What about the PPI effects? Here too it seems important to show regional selectivity, ideally using the same control regions, to show that the PPI differences are not generally related to pharmacological effects on BOLD.
