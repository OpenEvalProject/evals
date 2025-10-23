# Peer review - Round 1

Editors:
- Mimi Liljeholm, https://ror.org/04gyf1771 University of California, Irvine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71315.sa0](https://doi.org/10.7554/eLife.71315.sa0)

The authors used an elegant design to tackle a longstanding question about the extent to which social learning relies on specialized computational and neural mechanisms. They found that learning about ostensible others is more accurate than learning about non-social objects, despite identical statistical information, and that such effects are mediated by brain regions previously implicated in social cognition. These important results should be of interest to a broad range of social, behavioral, clinical, and cognitive neuroscientists.


---

# Peer review - Round 1

Editors:
- Mimi Liljeholm, https://ror.org/04gyf1771 University of California, Irvine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71315.sa1](https://doi.org/10.7554/eLife.71315.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Neural activity tracking identity and confidence in social information" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) It is not just the "framing" of information as social that differs across conditions, but also the stimuli (i.e., faces vs. fruit). Ideally, the behavioral experiment should be performed again, with the same cover-story, but using abstract shapes or symbols as stimuli, to rule out the possibility that the complexity/familiarity/salience of faces elicit attentional processes that account for the results. If additional data collection is not possible, the authors need to make a compelling case for why the results can be interpreted despite this confound.

2) Make sure to place the main question (i.e., whether humans learn differently from social vs. non-social information) in the context of relevant previous neural and computational work, both in the Introduction and Discussion, and identify what specific novel conceptual insights can be gleaned from these particular results (see the reviewers' comments below for relevant papers).

3) Use model simulations to test some of the explanations proposed in the Discussion (e.g., does changing the learning index of the Bayesian model produce the observed confidence intervals?).

4) Please perform an MVPA searchlight to assess the specificity of the effects in dmPFC and TPJ.

5) Behavioural indices and analyses need to be better justified (e.g., why should the interval size exactly match the angular error?).

6) Please provide a full description of the computational model in the main text.

7) Carefully consider and respond to all the reviewers' comments, appended below. In your reply, list each specific reviewer comment, followed by the response and the relevant revision/rebuttal.

Reviewer #1 (Recommendations for the authors):

The authors should provide the full description of the computational model (rather than the schematic illustration).

For the GLM in Figure 2e, I would suggest the authors use the mixed-effect model.

Reviewer #2 (Recommendations for the authors):

Regarding point 1 in the public review: I would be happy if the authors simply engaged more deeply with prior theoretical accounts, both in the introduction and in the discussion. However, I do think the theoretical contributions of this paper could be strengthened by building on some of the proposals in the discussion. In the discussion, the authors propose a few reasons why participants' estimates may have been less influenced by subjective uncertainty in the social condition. In particular, participants could have stronger prior expectations about the stability of social sources, or they could show a steeper decline in uncertainty over time. (Though this latter proposal seems contradicted by the results – wouldn't you then expect to see a larger "learning index" after the first update?) The Bayesian model used in this paper could be used to demonstrate the plausibility of these proposals – if you simulate the model forward using different priors or learning rates, does the model capture qualitative patterns in human behavior?

Regarding point 2: It would be informative to pair the multivariate analysis with a whole-brain searchlight, to test whether any other regions show this effect.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Neural activity tracking identity and confidence in social information" for further consideration by eLife. Your revised article has been evaluated by Michael Frank (Senior Editor), Mimi Liljeholm (Reviewing Editor), and two expert reviewers.

The manuscript has been greatly improved and the only remaining request is that you characterize the additional analyses, prompted by the first round of reviews, as exploratory, since they were not planned in the original submission.

Reviewer #1 (Recommendations for the authors):

The authors have adequately addressed all the concerns.

Reviewer #2 (Recommendations for the authors):

I thank the authors for their thoughtful and thorough responses to reviewer comments. My past review raised two key concerns. First, I suggested that the paper could engage more deeply with past work on the computational basis of social learning, in order to ground their discussion on the differences between social and non-social learning. Second, I raised the concern that condition differences between social and non-social stimuli could be driven by lower-level features, such as the attentional salience or visual distinctiveness of the stimuli. Overall, I believe that the authors have gone above and beyond to address these concerns.

First, the authors revised their introduction and discussion to cite past scholarship in social learning. But, beyond that, they also substantially expanded their analyses to disentangle differences between the underlying mechanisms driving behavior in social and non-social conditions. The authors found that participants did not have different prior expectations about the performance of social vs. non-social predictors. Instead, using a modified, noisy Bayesian model, the authors suggest that differences between conditions may be driven by degrees of uncertainty in the belief update and that greater noise in the update process leads to larger changes in confidence across different encounters with the predictor. I agree that these analyses have significantly improved the manuscript and made a new theoretical contribution in their own right, as they suggest a common computational mechanism underlying observed behavioral differences between conditions.

If I can offer a small suggestion: Because these analyses and hypotheses were not planned in the initial submission, it would be helpful to specify that they are exploratory/an extension when they are first presented in the main text (p. 10-11).

Second, the authors added several control analyses as a supplement. In order to test whether condition differences could be accounted for by attentional engagement, the authors inspected the constant of the GLM. They found no condition differences unaccounted for by the parametric regressors included in the GLM, either in attentional regions or in the regions that were the focus of their study. Next, in order to test whether social and non-social stimuli differed in their visual distinctiveness, the authors used RSA to compare the EDI between conditions in early visual areas. Again, the authors found no difference, suggesting that observed condition differences are unlikely to be driven by these lower-level features.
