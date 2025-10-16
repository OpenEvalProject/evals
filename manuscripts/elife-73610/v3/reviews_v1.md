# Peer review - Round 1

Editors:
- Tobias H Donner, https://ror.org/01zgy1s35 University Medical Center Hamburg-Eppendorf Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73610.sa0](https://doi.org/10.7554/eLife.73610.sa0)

This paper employs sophisticated modeling of human behavior in well-controlled tasks to study how limitations of working memory constrain decision-making. Because both are key cognitive processes, that have so far largely been studied in isolation, the paper will be of broad interest to neuroscientists and psychologists. The observed working memory limitations support previous findings and extend them in critical ways.


---

# Peer review - Round 1

Editors:
- Tobias H Donner, https://ror.org/01zgy1s35 University Medical Center Hamburg-Eppendorf Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73610.sa1](https://doi.org/10.7554/eLife.73610.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Strategy-dependent effects of working-memory limitations on human perceptual decision-making" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by Tobias Donner as the Reviewing Editor and Michael Frank as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Peter R Murphy (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Alternative strategies for sequential task.

The authors claim that some subjects follow the AtD strategy and others the DtA strategy but experimental evidence for this claim seems weak. Take Figure 10 as an example (Figure 6 is similar). The authors conclude from the data in Figure 10 that on the population level there is no significant difference between the models. On an individual subject level, the δLL values are small (for most subjects | δLL | < 3) which one could interpret as either model fitting the data equally well.

In order to claim that there are indeed two different strategies in place, it needs to be shown that the data can only be explained by heterogeneous strategies (for example following a methodology as in Stephan et al. Neurimage 2009 and Rigoux et al. Neuroimage 2014).

Regarding the sequential task: It may be worth considering a mixed strategy model as an alternative because it may explain the data better. Specifically, subjects would follow the DtA strategy until the last stimulus is observed and then switch to the AtD strategy until the end of the delay (i.e., compute the average in the middle of the trial, once all the evidence has been observed).

2) Appropriateness of modeling choices.

The A parameter, governing the relationship between the diffusion constant for a single point and the constants for multiple points, seems estimated differently in AtD and DtA models: in AtD, it's estimated using only data from Perceived blocks with set size > 1, and it plays no role in the AtD process (only, instead, in the memory maintenance process during the delay period of Perceived trials); whereas in DtA, it's estimate using data from both the same Perceived blocks, ‘and’ the Compute blocks at equivalent set sizes. This raises two concerns.

i. Because A parameters in each model are effectively fit to different data, any comparison of the parameter estimates (which is invited by placing them in same table and by some of the discussion in the text [p.9]) needs to be carefully qualified in the associated text.

ii. There is an implicit assumption that the A parameter is fixed across Perceived and Computed blocks. However, Perceived trials with set size > 1 require working memory maintenance of a ‘conjunction’ of stimulus features (location and colour), whereas the latter require maintenance (assuming the DtA process is employed) of only a single feature per stimulus (location); thus, it can reasonably be expected that the effect of load may be more severe in Perceived than Computed blocks. It seems that this possibility is not allowed for in the presented model fits.

Recommendations:

a. The above concerns could be addressed by fitting another round of models, this time fitting A in the DtA model using data from only Computed blocks.

b. In addition, A estimates should be compared between fits of the AtD and DtA models (something that is not possible given the fits as currently presented): if there is a systematic difference between the two, this would indicate that A is indeed different in Perceived and Computed blocks and this should be accounted for in the fits.

3) Implications of model fits.

The implications of strategy choice could be further illuminated by examining what factors if any (overall accuracy of judgments; magnitude of non-time-dependent model parameters) differentiate AtD and DtA adopters. Further clarification of what differentiates working memory from decision computations on the presented tasks could be achieved by addressing the following questions through further analysis and/or discussion: How should the decision-specific (etaMN) parameters be interpreted in the context of other prominent models of decision-making? How does their magnitude compare to other noise sources? Does this speak to the question of whether the predominant source of noise in decision-making is sensory-/motor- or memory-related or related the decision computation itself?

4) Clarity of presentation.

The Results section is difficult read, and several key aspects of the approach and findings are only clarified during careful reading of the Methods section. Most prominently, there is insufficient explanation of key model predictions that may be counterintuitive for many readers; a lack of clarity around what individual model parameters capture; and confusing elements to how the model fits are presented. We encourage the authors to carefully revise the Results section with this concern in mind.

Specific recommendations:

a. Implications of AtD vs DtA strategy choice:

The fact that, all else being equal, the DtA strategy generates ‘more’ precise behaviour on Computed trials than the AtD model (at least for the parameter range human participants seem to occupy here) is the central feature that differentiates behaviour produced by the two strategies and renders the models identifiable. The authors also seem to take the direction of this effect to be self-evident, as no effort is made to explain to the reader why this pattern emerges. For instance, readers may wonder whether allowing for N = [2, 5] sources of gaussian noise compared to only 1 source should actually produce ‘more’ variability in behaviour. Now, the averaging over particles that takes place at the culmination of the DtA process counteracts the greater total noise to produce less variability in behavioural reports. But this was far from self-evident, and this key effect should be unpacked.

b. Model parameter descriptions:

There seems to be a general lack of clarity around what exactly each model parameter, and in particular different subscripts to different parameters, are supposed to capture. In Figure 2, for example, subscripts N, MN, 1, N(E/L) and MNSeq are all used but only explained in Methods.

c. Alternative strategy interpretation. (see also point 3):

Please clarify what exactly the finding is, because this currently seems ambiguous: Compare line 244 "(…) participants had roughly equal tendencies to use either of the two strategies" implying that we can distinguish which strategy individual subjects are following, vs. line 257 "(…) neither of which was more likely than the other for a given participant" which implies the opposite.

d. Model fitting procedures (see also point 2):

The role of the A parameter in the different fits is confusing, specifically, seeing fits of A for the AtD model since, this parameter does not seem to used at all in the AtD process. If our understanding is correct, the A parameter in these fits is only relevant to producing behavior in Perceived blocks with set size > 1 – a condition of the experiment to which the AtD process is never actually applied. But at no point is this made explicit, leaving room for quite considerable confusion when the reader encounters this important section of the Results.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Strategy-dependent effects of working-memory limitations on human perceptual decision-making" for further consideration by eLife. Your revised article has been evaluated by Michael Frank (Senior Editor) and a Reviewing Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. Both reviewers were overall very positive about your revisions and felt that the manuscript is much more accessible now. Both support publication in eLife.

Essential revisions:

1) Please address one outstanding clarification question by Reviewer #1, with which Reviewer #2 agreed. Rather than summarizing, we paste the original reviewer point below. Once this point is addressed, the paper can be accepted without additional review.

I only have one lingering point of confusion that I would welcome clarification on. This again centres around treatment of the A parameter in the AtD model. The authors write in the current manuscript (p.7) that in this model "the average is calculated immediately upon observing the evidence and then stored as a single particle in working memory" (lines 95-96) and then "the single estimate held in working memory diffuses with the same diffusion constant as a single perceived item (σMN2 = σ12) (lines 97-99). Based on this my understanding is that there is only ever one particle diffusing in the AtD model during Computed blocks, regardless of set size; this particle always has the same diffusion constant (σ12), and there is, therefore, ‘no role’ for set size/the A parameter in determining diffusion noise during Computed-block memory maintenance in the AtD model. Why, then, is it later written that "Because of the previously described relationships between σ12, σN2, and σMN2 it is therefore also true that in the AtD model σN2 = σMN2 * NA" (lines 109-110)? Given the earlier sentences, the only way I can see this being true is if N here refers to the number of ‘particles’ being maintained in memory (which, in the AtD model, is always equal to 1, and so the NA term is doing no work here and just causes considerable confusion) – and not the set size presented to the participant, as N is consistently used to denote elsewhere in the paper. I'm sorry if I'm missing something here, but this seems a key conceptual point to get right for clear presentation and differentiation between the two models. The new Table 1, and my careful reading of the Methods, seems consistent with my own intuition that A plays no role on Computed blocks in the AtD model. But this seems fundamentally inconsistent with the equation emphasized on lines 109-110; and indeed with the authors' response to point 2 in the first round of reviews, which I must confess I did not understand.

Now, assuming my own interpretation is correct, and that indeed the A parameter is not doing any work on Computed blocks in the AtD model (instead, in this model it only serves to set the diffusion noise across different set sizes in ‘Perceived’ blocks), then I stand by my initial point that without clarification, it is misleading to include and invite comparison of fitted A parameters for the AtD and DtA models in the same table (new Table 2). In one case (AtD) the A parameter only captures (and in turn, will only be constrained by) behaviour in Perceived blocks; in the other (DtA) it captures (and is constrained by) behaviour in both Perceived and Computed blocks. But currently, this is never made explicit.

Reviewer #1 (Recommendations for the authors):

I thank the authors for engaging well with all comments and suggestions from the first round of reviews. In my opinion the new draft – including more detailed explanation of the models and their predictions early on – is a lot more accessible. I also found the new model identifiability analyses to be quite convincing, in the sense that they provide further evidence to support the claim the distinct strategies are indeed being used by different participants and that while the specifically identified proportions are subject to quite some uncertainty (especially for low set sizes), this key result is nonetheless recoverable given the data at the authors' disposal. Altogether, these additions reaffirm my initial impression that this manuscript is a valuable contribution to the field, breaking new ground in connecting working memory and decision-making.

I only have one lingering point of confusion that I would welcome clarification on. This again centres around treatment of the A parameter in the AtD model. The authors write in the current manuscript (p.7) that in this model "the average is calculated immediately upon observing the evidence and then stored as a single particle in working memory" (lines 95-96) and then "the single estimate held in working memory diffuses with the same diffusion constant as a single perceived item (σMN2 = σ12) (lines 97-99). Based on this my understanding is that there is only ever one particle diffusing in the AtD model during Computed blocks, regardless of set size; this particle always has the same diffusion constant (σ12), and there is, therefore, ‘no role’ for set size/the A parameter in determining diffusion noise during Computed-block memory maintenance in the AtD model. Why, then, is it later written that "Because of the previously described relationships between σ12, σN2, and σMN2 it is therefore also true that in the AtD model σN2 = σMN2 * NA" (lines 109-110)? Given the earlier sentences, the only way I can see this being true is if N here refers to the number of ‘particles’ being maintained in memory (which, in the AtD model, is always equal to 1, and so the NA term is doing no work here and just causes considerable confusion) – and not the set size presented to the participant, as N is consistently used to denote elsewhere in the paper. I'm sorry if I'm missing something here, but this seems a key conceptual point to get right for clear presentation and differentiation between the two models. The new Table 1, and my careful reading of the Methods, seems consistent with my own intuition that A plays no role on Computed blocks in the AtD model. But this seems fundamentally inconsistent with the equation emphasized on lines 109-110; and indeed with the authors' response to point 2 in the first round of reviews, which I must confess I did not understand.

Now, assuming my own interpretation is correct, and that indeed the A parameter is not doing any work on Computed blocks in the AtD model (instead, in this model it only serves to set the diffusion noise across different set sizes in ‘Perceived’ blocks), then I stand by my initial point that without clarification, it is misleading to include and invite comparison of fitted A parameters for the AtD and DtA models in the same table (new Table 2). In one case (AtD) the A parameter only captures (and in turn, will only be constrained by) behaviour in Perceived blocks; in the other (DtA) it captures (and is constrained by) behaviour in both Perceived and Computed blocks. But currently, this is never made explicit.

Reviewer #2 (Recommendations for the authors):

The authors have followed the recommendations of the previous decision letter and the additional analysis confirm the findings of the first version. I have no further issues.
