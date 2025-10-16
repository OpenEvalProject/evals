# Peer review - Round 1

Editors:
- Michael J Frank, Brown University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.56151.sa1](https://doi.org/10.7554/eLife.56151.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This works provides rigorous and novel insight into the brain mechanisms underlying psychosis, with distinct processes relating to hallucinations and delusions. The authors provide evidence for a hierarchical process in which alterations in the dynamics of somatosensory brain systems are related to delusions, whereas alterations in dynamics of auditory perceptual brain systems are related to hallucinations. Simulations from a computer model recapitulate these findings by altering the balance between excitation and inhibition in distinct hierarchical layers of a simulated circuit.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Distinct hierarchical alterations of intrinsic neural timescales account for different manifestations of psychosis" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Claire M Gillan as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Philip R Corlett (Reviewer #2).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

As will be clear from the reviews, the reviewers agreed that the study posed an interesting, important and timely question, given much discussion in the field around abnormal hierarchical processing dysfunctions in schizophrenia. The premise was compelling and the use of relatively large pre-existing datasets and a new analysis methodology were all strengths. We each enjoyed reading it, but had similar reservations that led us to agree that this study would be better suited to a more specialist psychiatry journal. We think this work lays an important foundation for future research, which we suspect may require even larger samples to arrive at definitive conclusions.

In terms of the key factors that contributed to our decision the main result regarding the relationship between INT and auditory hierarchies was particularly striking, but all of the reviewers ultimately questioned the statistical robustness of the conclusion. This was due to a combination of factors that include (i) the somewhat arbitrary decision with respect to the ordering of regions within the auditory hierarchy, (ii) the fact that the result was marginal and would not survive some reasonable tests of alternative orderings within the hierarchy, (iii) that exploratory analyses appear to indicate effects of a similar magnitude for other symptoms of schizophrenia. The interpretation of the results with respect to delusions were perhaps less well-received, with multiple reviewers noting that results which failed to reach significance were, in parts, over-stated and over-discussed. The authors may like to take these opinions into account in a future submission to a more specialist journal, reducing the emphasis on the delusion result and presenting more fully the exploratory analyses so that future work can build on this excellent study in a more systematic way.

Reviewer #1:

This is a well-motivated and interesting paper that applies recently developed fMRI methods to study intrinsic neural timescales (INT) in a relatively large sample of schizophrenia patients. The findings are novel and I read it with great interest, the key result being that hallucinations are associated with an increase in INT at lower levels of the hierarchy of auditory cortex. Delusions did not show this pattern and trended towards the opposite, an increase in INT at higher levels of the hierarchy. The authors frame this in the context of recent theories of schizophrenia, where delusions are thought to arise from alterations in higher-order processing of information (concepts, beliefs, etc), while hallucinations are posited to stem from alternations in low-level stimulus processing. Again, I thought this was well-presented and I enjoyed reading it.

My key concern is that the results themselves are not 100% compelling. There is no statement about statistical power. All of the key effects are quite small and the significance levels are all just under p<.05. The key result is from auditory cortex, but there is clearly multiple testing (e.g. analyses at whole brain, and also in multiple sub-regions), but no correction has been applied beyond the permutation testing (which as I understand does not control for this), nor are stronger interaction tests (by brain region) carried out. Were a more strict criterion applied, results would not achieve significance. The exploratory analyses, which were not the focus of the study, indicate several other symptoms of schizophrenia that are associated with alterations in the gradient. Hallucinations was significant at p=.04, conceptual disorganisation p=.06 and blunted affect at p=.08 (the authors don't indicate direction). This casts some doubt over the specificity of these results, although I appreciate these are exploratory analyses that were in part predicated on seeing an opposing pattern or delusions. It would of course be more compelling to observe significant differences between hallucinations and all of the other symptoms.

That said, this is a new area and this paper serves as a nice foundational set of analyses for others to probe in the future. Should the authors be penalised for results that are more equivocal than they would have liked (or simply just a bit weaker)? Probably not. I suspect people will read with interest, we just need to ensure that the results are not over-stated.

Reviewer #2:

I read and enjoyed Wengler and colleagues' report of intrinsic resting state functional connectivity within sensory hierarchies and its relationship to hallucinations and delusions in patients with schizophrenia. They claim that hallucinations are related to perturbations lower in the hierarchy whereas delusions are related to higher hierarchical problems, in the auditory (and sensorimotor) but not visual hierarchies.

This is an important finding that may help to contextualize behavioural and computational findings that appear to show delusions relate to aberrant prediction errors (and apparently weak priors) and hallucinations to strong priors.

Whilst I am positively predisposed to this work, I have some concerns that I think should be addressed before publication.

1) Statistics. The claims the authors are making demand a significant omnibus f-test for the interaction between symptom (delusions vs hallucinations), system (visual, auditory, sensorimotor), vs level (high vs low). They report various components of this analysis as post-hoc t-tests, but no overall f-value rather t scores for some comparisons but not others, and the absence of significant effects for some comparisons, rather than testing the full interaction. If the overall comparison is significant, the unpacking will be appropriate and the result will be more believable.

2) Symptom contents. This may prove enlightening. There are some delusions that are more hallucination like, like delusions of parasitosis: the belief that one is infested with insects, which may be associated with tactile and visual hallucinations, where do people with these delusions fall on the hierarchical perturbations

3) Supplementary analyses. It is my understanding that eLife does not permit supplements. Why are supplements mentioned throughout? And why were some things relegated to the supplement? The sensorimotor analysis which is consistent with the auditory result is relevant to delusions of passivity too (and the apparent failures of corollary discharge/forward modeling that may under write them, this should be explored too if possible, are passivity delusions particularly related to changes in the sensorimotor hierarchy?

Furthermore, why did the authors exclude and then re-include DLPFC? It would seem very relevant to delusions from the lesion studies and some fMRI work.

Reviewer #3:

In this study, the authors use an approach first published by Watanabe et al., 2019, to estimate intrinsic neural timescales, INT (i.e. the rate of decay of the autocorrelation function) from resting state fMRI data in subjects with schizophrenia. They do this first in 100 healthy subjects from the HCP dataset, and find that INT can be reliably estimated from rsfMRI data, and that INT increases as one ascends the auditory and visual (and somatosensory) hierarchies. It doesn't have a clear relationship to other brain hierarchies (assessed using their T1w/T2w myelin content) however. They then analyse INT in some open schizophrenia datasets, and find INT is reduced globally in schizophrenia. They look at relations of INT gradient with hallucinations and delusions in the auditory and visual systems, and find that subjects with hallucinations have a positive relationship between INT and hallucinations in lower parts of the auditory hierarchy, despite their lower INT overall. There is a less convincing positive relationship between delusions and INT in the upper part of the auditory hierarchy. Neither is the case in the visual hierarchy. The authors go on to simulate these INT differences using a biophysical model, by increasing the self-connectivity in pyramidal cell populations more at the lower or higher ends of the hierarchy respectively.

This is an interesting paper and an important analysis to perform, given the widespread hypotheses about abnormal hierarchical message passing and pyramidal cell dysfunction in schizophrenia. The relationship between INT and auditory and visual hierarchies is striking. I do have some major reservations about some aspects of the paper, however:

1) My biggest reservation is that (unless I have misunderstood the statistics) the post-hoc test of the relative increase in INT at higher hierarchical levels in the auditory hierarchy in those with worse delusions is not significant (effect of hierarchy p=0.11). The actual p value for the delusion effect shown in Figure 3A seems to be given 32 pages later in the supplement (p=0.21). Yet the whole paper is framed around the hallucination and delusion effects. Really, all mention of any delusion effect should be removed from the paper, such an effect has not been found (unless I misunderstand, if so, many apologies). In addition, I find the motivation for the delusion effect far less persuasive than that for the hallucination effect (see below).

2) I am also not clear on to what extent the significance of the results depends on the strict order of areas given here. For example, what is the evidence that the auditory hierarchy is a linear progression from A1-LBelt-MBelt-PBelt-RI-A4-A5? To my (imperfect) knowledge the auditory hierarchy is complex and not well understood, it may contain two parallel hierarchies (e.g. Hackett, 2011, Hearing Research) and numerous regions are on the same “level” and thus could be listed in any order (e.g. Figure 1, Kaas and Hackett, 2000). Do the key results stand up to different reasonable permutations of the “hierarchical level” order in Figure 3A? Given the closeness of the p values to 0.05 I am concerned they would not…

3) I applaud the use of the simulations but I wonder how much they really add to the paper. In a sense it is a trivial result to show that increasing self-connection strength increases autocorrelation and hence INT: how could it not do so? Perhaps the simulations could be used to more closely match the size of the empirical effects, and thus estimate the rough order of magnitude of the possible changes in parameters that underlie them?

Some other points follow:

Introduction: the authors hypothesize that "INT at these respective levels would increase with more severe symptoms, reflecting increased neural integration of prior information". To me this prediction does not make sense with respect to delusions. From a neurophysiological point of view, I would expect intrinsic neural timescales as measured by these studies to reflect the ability to sustain neural activity, e.g. due to NMDAR function in pyramidal cells, or pyramidal interactions with interneurons, or network attractor dynamics: all of these processes are of the order of up to a few seconds. Delusions seem a different process entirely, likely encoded by long term synaptic plasticity? I don't see why they would have anything to do with INT? (Ongoing hallucinations on the other hand do fit this hypothesis).

Results and Figure 1: I don't understand why Figure 1E shows a mixture of best fit lines from a) 3 networks and b) 3 groups which have no network relationships i.e. “anterior”, “posterior” and “temporal”. What is the logic behind these latter groupings? Why not use other network groupings?

Subsection “Hierarchical Differences in Intrinsic Neural Timescales Between Hallucinations and Delusions”: I don't think the authors can interpret an effect at p=0.11 with any confidence, I would suggest removing the sentence about delusions being associated with an increase in higher level INT from the manuscript. The authors also refer to this "expanded hierarchical gradient related to delusions" elsewhere in the manuscript, e.g. in Figure 3B, 4, Discussion etc. I don't think this can be accepted as a finding, if they wish to include all the simulations then that is fine, but they should not be described as if referring to an empirical result.

In the Discussion the authors state "patients with more severe hallucinations exhibited a less pronounced hierarchical gradient, consistent with increased timescales at lower levels". Could this be rephrased to emphasise the timescales at lower levels are not increased relative to controls, but just that their gradient is more shallow?

In the Discussion the authors say "distinct hierarchical alterations provide symptom-specific pathways that together may explain symptom co-occurrence", but given that apparently opposite relationships exist between INT gradients and delusions vs hallucinations, how does this explain symptom co-occurrence? Would one not expect these symptoms to correlate negatively if these opposite relationships were correct and causal? Also in the next paragraph, the authors claim these findings "fit well with the timescale of symptoms", but this is not the case for delusions, for which it is hard to motivate a relationship with INT (as discussed above).

Apologies if I missed it but does post-hoc testing show a significant effect of hierarchy for hallucinations in the somatosensory system? Or is it just the interactions that are significant?

Materials and methods: Motion is clearly a concern given the authors have shown it is associated with reduced INT in the HCP sample. I see that motion scrubbing was performed, as well as a motion quality check, but was the motion in the schizophrenia group significantly higher than the control group even after these procedures? And if motion is used as a nuisance regressor, is the schizophrenia group still significantly associated with lower INT?

In the simulations, were wEE in V1, V2 and V4 and also V2, V4 and MT increased by 10%, 5% and 2.5% respectively in both cases? Unless I misunderstand something there must be a misprint here, do you mean 2.5%, 5% and 10% for the latter set of areas?

In any case, are the effects in Figure 4 of the same order of magnitude as the effects observed in the fMRI data? The upper and lower hierarchy effects are also quite different to each other. Why not simulate effects of similar orders of magnitude to the detected effects, this would convey what magnitude of changes to these parameters might be needed to cause these pathologies… Also, I would have thought the most realistic simulations would in fact be ones in which wEEdecreased throughout the hierarchy but in differing amounts depending on hierarchical level in the hallucination vs delusion cases. The simulation as it is has INT increasing above “normal” in the pathological cases, which is not what was observed in any area in the schizophrenia group, unless I'm mistaken?

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your article "Distinct hierarchical alterations of intrinsic neural timescales account for different manifestations of psychosis" for consideration by eLife. Your revised article has been reviewed by two peer reviewers, and the evaluation has been overseen by Michael Frank as the Senior Editor and Reviewing Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Overall the reviewers and I were impressed by your revision. As you will see however, there was variability in how convinced the reviewers were by the new results given that they depend on a new hierarchy. In the consultation session among reviewers, one reviewer noted that while the paper is innovating and exciting, they are troubled because they felt that links between brain and behavior should be tethered/grounded at both ends. They would like to be more sure that the new way that you have chosen to define the brain hierarchy isn't the one that happens to correlate with delusions, noting "would like to be convinced that there is independent validation of the hierarchy and that is indeed the one that we find in the brain, rather than the one that happens to work best for the authors' purpose".

The other reviewer was more convinced and thought your way of establishing the hierarchy via T1w/T2w and thickness was as good as you might get in humans, and that establishing this hierarchy would be a paper in itself, and that all 4 auditory rankings you obtained from the literature (without checking the primary sources) showed significant AVH effects and 3/4 significant delusion effects. So maybe the fine details of the middle-order ranking don't matter so much? In any case, looking at the Glasser et al., 2016, supplement, the myelin content fits the hierarchy you came up with. So all in all, this reviewer was fairly confident this auditory hierarchy is reasonable and not just picked for its data-fitting qualities.

They then followed this up noting that your winning visual hierarchy falls within the null distribution of model fits for myelin/thickness (Figure 1B). So it seems visual hierarchy is not very reliably measured at all. But the intrinsic timescale results weren't significant in the visual system either so that doesn't really matter. They noted "If anything I think they should stop treating all the sensory hierarchies similarly and point out the visual one seems quite different but this is a side issue".

Given these divergent opinions but with overall positive inclinations, I would like you to consider some more moderate way you could address this, e.g. by reporting more fully the AVH and delusion affects for all 4 auditory rankings and discussing the implications of the revised approach which then leads to relation to delusions.

Reviewer #2:

This revision and appeal is much improved.

It is challenging since we should not moderate our enthusiasm for a piece based on the specific results, however, the fact that the gradients now relate significantly and oppositely to hallucinations and delusions is encouraging.

Here is my remaining concern. The authors can't have it both ways. They reclassified the hierarchy and got this interesting and compelling pattern of findings. The pattern is even significant compared to a random ordering of regions. However, I would like to be reassured further that:

1) This is the most appropriate construction of hierarchy, i.e. the choice of hierarchy construction reflects biological reality (leveraging for example postmortem data on which there are also MRI data).

2) What impact the choice of hierarchy construction has on the symptom associations, that is, compared to some control other than random, how robust are the associations, given that they made some different choices and got a less robust set of effects.

To summarize, I would like to be more convinced that these effects are not being driven by the authors new choices about anatomy and hierarchy, and would like to be reassured that these are the best choices given what we know about the brain

Reviewer #3:

I think the authors have done a great job in responding to the comments and the paper is definitely stronger as a result. I have only a couple of comments.

I have some trouble understanding the new modelling part, the description is not clear in the text and neither in the figure legend. The different panels in Figure 4 are also not explicitly referenced in the text (at least not in the rebuttal letter). There is also not much labelling in Figure 4 itself. Could this all please be clarified? Some specific issues too:

The authors state "the best-fitting levels of the peak increase in local E/I ratio were levels 1 and 8" but this is a six node hierarchy? Should this be levels 1 and 6?

The in silico plots in Figure 4B look identical all along the row. Is that meant to be the case? I'm also not clear why in vivo auditory results are being compared with in silico visual ones?

The legend descriptions "insets for A" and "Insets for B" should be B and C respectively, I think?

Also in the phrase "Insets for A show predicted INT values" does “predicted” mean estimated from in vivo data? “Predicted” sounds like a model has been involved but I assume that is not the case? I don't understand the difference between the Insets for A and B?
