# Peer review - Round 1

Editors:
- Timothy Behrens, Oxford University , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.08825.018](https://doi.org/10.7554/eLife.08825.018)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for submitting your work entitled “Normative evidence accumulation in unpredictable environments” for peer review at eLife. Your submission has been favorably evaluated by Timothy Behrens (Senior and Reviewing Editor) and three peer reviewers.

The reviewers have discussed the reviews with one another and the editor has drafted this decision to help you prepare a revised submission.

The study of how the brain integrates a history of evidence into a single expectation has been a remarkably profitable avenue of research in forming quantitative understandings of neural mechanisms over recent years and decades. However, two largely distinct literatures have tackled this problem from very different perspectives. One set of researchers have considered the mathematics and neurophysiology of integrating continuous streams of evidence using approaches such as the drift diffusion model and the sequential probability ratio test. Another set of researchers have considered the integration of discrete events or trials using Bayesian models that can, for example, optimally determine when to integrate evidence together, and when to separate new evidence because the world has changed.

The current paper presents an important step towards a unification of these two literatures, by presenting an elegant mathematical analysis of the Bayesian change-point models to demonstrate that they can be viewed as modified sequential probability ratio tests, and are therefore directly applicable to the large set of researchers who are interested in continuous evidence integration. It makes new and interesting predictions about the stream integration case in situations when the evidence is non-stationary and it tests these predictions in behaviour. All three reviewers considered this to be a very interesting and potentially important step.

As you will see below, the reviewers did not have major criticisms of the model that is presented or data, which they broadly found to be convincing. Most important in terms of solidifying the conclusions, however, are Reviewer 1's and 3's similar points about the demonstration of the qualitative reason for the improvement of the current model (Reviewer 1) and the absence of a reasonable analysis of other (sub-optimal) models (Reviewer 3).

In the discussion, the reviewers and editor were also clear that the manuscript is really written for a technical audience. eLife readership is broad and the reviewers and editor would appreciate a reframing of the paper that makes the central points clearer to this broad audience.

One suggestion that emerged during the discussion was a clearer framing of the manuscript as follows:

a) The same Bayesian learning framework, that has been used in other contexts (work by Behrens, Adams, Kording and also Nassar and Gold) is here derived for evidence accumulation in perceptual decision-making tasks like RDM;

b) This normative framework can be described, in both discrete and continuous cases, as a leaky accumulator with non-absorbing bounds, with the leak rate and the height of the bounds being explicit functions of the environmental change rate;

c) Show that this is the case in their data (their paradigm with variable hazard rate is a good test even if atypical of RDM experiments);

d) Provide some justification why this model helps our understanding of perceptual decision-making (can the relationship with change point detection explain or offer insight into previously unexplained data?);

e) Provide some clear commentary on the relationship to previous models of change point detection (can the relationship with RDMs explain or offer insight into previously unexplained data?).

We urge you to consider this, or other possible reframings in which the strong message can be understood clearly without an understanding of the technical details.

Reviewer #1:

In this study, Glaze, Kable and Gold present a model of evidence integration over time in which the relative weighting given to new and past observations can be adjusted to reflect the hazard rate for change in the environment. They show that this model can be generalized to both discrete and continuous time cases and that it fits human performance better than a model without adjustable hazard rate, in two very different decision-making tasks – a random dot motion task with within-trial reversals, and a task in which evidence is accumulated over many discrete trials.

This is a good quality paper which I think will be of interest to people across the field of perceptual decision-making, since it presents a clear framework that is applicable in diverse tasks. It could be an influential and highly cited paper in the field.

If I were to make a case why the manuscript should be published in eLife, I would point out that the adaptation of the Bayesian framework to the random dot motion case does represent a major conceptual advance over the more typical approaches in that field (SPRT models with fixed leak rates or the drift diffusion model), and the model does better at explaining participants' performance than those more typical models. However, I would then suggest that the paper could be strengthened by exploring in more detail why the current model outperforms others (especially, the leaky accumulator with hazard rate as a free parameter by block). Is this because the leaky accumulator down weights past beliefs about the correct response without taking into account evidence strength? If so the reason for the current model's superiority is not really to do with estimating the hazard rate, although the text implies that it is. Furthermore, to what extent does the current model address burning questions in that field, such as how confidence judgements are made or when the evidence accumulation process should terminate?

Reviewer #2:

In this manuscript by Glaze et al., the authors present a normative model for evidence accumulation in a non-stationary environment in which the successive simples are drawn from one of two alternative distributions for an unknown and variable duration. The main part of the manuscript is to compare the performance of human subjects in two different behavioral tasks with the predictions of this normative model and a simpler alternative model based on leaky integration. The results show that human subjects differ significantly from the predictions of normative model, in that subjective estimate of the rate of change (hazard rate) is close to 0.5, suggesting that they tend to give insufficient weight to the history of evidence. Although the manuscript is quite technical in nature, it is written clearly, and the findings would be of high value to many researchers in the field. There are only a few, relatively minor, comments:

1) The overall conclusion of the authors is that the subjective estimates of hazard rate are biased, but this quantity is used in a normative way. However, this might be misleading. Namely, is it fair to refer to an algorithm as “normative” if the quantity used in this algorithm is biased? Does such an algorithm behave differently, for example, from a model that uses the accurate estimate of hazard rate in non-normative way? Unless the authors can clarify how these two different scenarios can be distinguished, how the word “normative” is used in this manuscript might need to be improved.

2) In the subsection “Psychophysics”, the authors should indicate for how many sessions, trial-by-trial feedback was provided in the beginning and end of each block.

3) What do green and blue colors in Figure 7A indicate?

Reviewer #3:

This is an interesting paper that provides a significant contribution through the clear derivation of a normative approach for accumulation of evidence under conditions where the evidence is not stationary. The derivation and the description of how changes in the rate of change of environments correspond to leakiness in accumulation was very appealing.

I found the experimental section convincing in terms of showing that humans do indeed try to estimate the rate of change of the environment, and that this estimate affects how they make decisions. But the further claim made in the paper that humans behave according to the normative model was harder to be convinced by – it seemed that other (suboptimal) models that use an estimate of the hazard rate might also be consistent with the data, but this wasn't much explored in the paper. Instead, the straw man such as a model where the estimated hazard rate is a single value fixed for all time was used, but it seemed rather a weak straw man.

In addition, much greater clarity in the exposition would be desirable.

Despite these concerns, the nice derivation of the normative results under changes in environments makes me see the paper positively.
