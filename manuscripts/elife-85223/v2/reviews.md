# Peer review - Round 1

Editors:
- Tobias H Donner, https://ror.org/01zgy1s35 University Medical Center Hamburg-Eppendorf Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85223.sa0](https://doi.org/10.7554/eLife.85223.sa0)

This valuable study presents solid evidence for how change in reward contingency in the environment affects the dynamics of a realistic large-scale neural circuit model, human choice behavior, and fMRI responses. This study could be of interest to scientists studying the neural and computational bases of adaptive behavior.


---

# Peer review - Round 1

Editors:
- Tobias H Donner, https://ror.org/01zgy1s35 University Medical Center Hamburg-Eppendorf Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85223.sa1](https://doi.org/10.7554/eLife.85223.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your article "Competing neural representations of choice shape evidence accumulation in humans" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Floris de Lange as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Overall, reviewers felt that the study would benefit from (i) the derivation of more (and/or more specific) model predictions from the neural circuit model (ii) more in-depth analyses of the fMRI data, and (iii) further steps to link DDM, circuit model, and fMRI data.

For e.g. model-based analyses could be performed to elucidate the activity dynamics and link that to the circuit model. This could perhaps be done e.g. with slow and fast responses, and identify brain regions with ramping activities over time as in the model (e.g. Supp. Figure 1).

2) Please clarify the correlation between drift and model uncertainty (figure 2E) and drift and fMRI classifier uncertainty (figure 4B), and explain the largely weaker association between classier uncertainty and drift rate (Figure 4B), and the weak reaction time effects (Supp. Figure 2).

We assume that the posterior probability distributions shown are obtained from the HDDM single-trial regression mode. Should the spiking NN model and the fMRI results not be compared to a simpler null model (e.g. with a weighted average of past responses) to know how much it is an improvement over previous work?

3) Please discuss why the model's cortical neurons had no contralateral encoding, unlike the fMRI data.

4) Please clarify why the prediction of CBGT network choices (lines 130-131) is not 100%:

Presumably, all the relevant information (firing rates of all regions modelled) together should perfectly predict the choice. (How crucial is the choice of the LASSO-PCR classifier over other classifiers?)

5) Please clarify the terminology:

– Throughout, there are aspects of the manuscript that make it hard for the reader to follow. For instance, in Figure 1 the terms D1-SPN/D2-SPN are used interchangeably with dSPN and iSPN, and the legend and the text differ in what the time = 0 indicates (stimulus or decision).

– Change of mind in the literature is now more linked to a trial change in (impending) choices, a more recent research area (e.g. Resulaj et al., Nat. 2009), and the phrase change of mind is not as suitable for use in this work. I would replace such phrases with phrases like adaptive decision/choice (learned over trials) or similar.

6) Please revise the abstract: It is currently too general and vague.

Reviewer #1 (Recommendations for the authors):

Specific comments and recommendations:

1. Further analysis of the fMRI data may be needed. E.g. model-based analysis to elucidate the activity dynamics and link that to the biophysical data. This could perhaps be done e.g. with slow and fast responses, and identify brain regions with ramping activities over time as in the model (e.g. Supp. Figure 1).

2. Provide an explanation for the (order of magnitude) weaker association between classier uncertainty and drift rate (by participants) for human participants (Figure 4B), and the weak reaction time effects in Supp. Figure 2.

3. Discuss why the model's cortical neurons had no contralateral encoding, unlike in the neuroimaging data.

4. Change of mind in the literature is now more linked to within trial change in (impending) choices, a more recent research area (e.g. Result et al., Nat. 2009), and the phrase change of mind is not as suitable for use in this work. I would replace such phrases with phrases like adaptive decision/choice (learned over trials) or similar.

5. Supp. Figure 4. It would have been clearer to show the activity dynamics over time for the key brain regions, e.g. with fast and slow decisions. Is there actually ramping of activity over time? Could brain regions linked to dopaminergic activity be obtained and related to that in model simulations?

6. Supp. Figure 5A. Why are the weights for GPi so strong, but not much in humans?

7. Supp. Table 1. Why is the accuracy so low, hovering around the chance level?

8. Lines 470-471. Is there any non-decision latency (e.g. signal transduction and motor preparation) to bridge from decision time to reaction time?

9. Lines 604-605. The use of the classifier LASSO-PCR was not justified.

Reviewer #2 (Recommendations for the authors):

I will focus mostly on the behavioral task and HDDM model, as well as the link between behavior and the in silico model. My expertise does not lie in evaluating the details of the spiking neural network model, or the processing of fMRI data.

Specific questions:

– One methodological concern/clarification: the correlation between drift and model uncertainty (figure 2E) and drift and fMRI classifier uncertainty (figure 4B) seems the crucial test of the similarity between brain, behavior, and model. However, drift is not usually fit on a single trial level. So, I think the distributions shown are the posteriors from the HDDM regression model – but if so, should the spiking NN model + the fMRI results not be compared to a simpler null model (e.g. with a weighted average of past responses) to know how much it's an improvement over previous work?

– A block switch every 10 trials seems very easy to learn (i.e. simply by counting). Did any of the four humans take this strategy?

– I'm a bit puzzled the prediction of CBGT network choices (lines 130-131) is not 100%, since presumably all the relevant information (firing rates of all regions modelled) together should perfectly predict the choice. How crucial is the choice of the LASSO-PCR classifier (over other classifiers)?

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting the paper entitled "Competing neural representations of choice shape evidence accumulation in humans" for further consideration by eLife. Your revised article has been evaluated by a Senior Editor and a Reviewing Editor. We are sorry to say that we have decided that this submission will not be considered further for publication by eLife.

We appreciate your efforts in trying to address the reviewers' points. While the reviewers were satisfied with several of your responses, there are remaining issues. Most importantly, both reviewers felt that the study, while useful, appears a bit preliminary and the evidence in support of your conclusions remains incomplete.

Reviewer #1 (Recommendations for the authors):

The overall responses from the authors were mainly satisfactory, but further concerns remain.

1. Perhaps the authors can replace the spiking neural network model with simpler network-RL-based theoretical models that are more suitably linked and optimised to BOLD-fMRI data or remove the spiking neural network model which can be used and validated in their subsequent future work based on more precise neural recording.

2. Both CBGT and DDMs' parameters did not seem to be optimised. The authors' justification is that model optimisation based on experimental data could lead to 'circular' inference. Although I can understand this to some extent, especially with physiologically constrained model, I am not sure whether I fully agree with this claim. In any case, the authors should at least summarise clearly which CBGT and DDM parameters were free, which were constrained, and which were tuned – a summary table may help.

Overall, this work is interesting and could potentially contribute to the computational modelling and neuroscience of adaptive choice behaviour. However, a major component of the work, on the CBGT modelling, seems somewhat premature.

Reviewer #2 (Recommendations for the authors):

I thank the authors for clarifying various technical details.

While this is solid work, I am still unsure as to the main insights we can draw from this paper itself. The main argument for using the fine-scale model to account for fMRI data is that it sets the stage for future work, which will compare these model predictions with mouse data. As much as I understand that this is how science goes, the result for this paper is that linking fMRI and the detailed model is a bit strange (and makes it much harder to draw conclusions from). For the general readership of eLife, I'm not sure if the current insights are very helpful before knowing the results of the more fine-grained data that are currently being collected.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for choosing to send your work entitled "Competing neural representations of choice shape evidence accumulation in humans" for consideration at eLife.

Your letter of appeal has now been considered by myself as Senior Editor and Tobias as Reviewing Editor, and we had the time to discuss it. We apologize for the delay in responding to your appeal: it reached us when Tobias was just leaving for vacation; after his return, Floris was not available for some time.

After careful consideration, we are now prepared to receive a revised submission (with no guarantees of acceptance), which implements the revision plan you have outlined in your appeal.

We would like to stress that we do see the value of model-based neuroimaging in general, including work that uses biophysically detailed circuit models. We neither see the need for a general justification of such approaches, nor for references to other work using circuit modelling of fMRI data, in your paper. What we feel does need justification, in light of the comments by both reviewers, is the choice of your specific modeling approach for these particular (task) data. We also feel that a discussion of the limitations of your approach is warranted that takes into account the concerns raised by both reviewers.
