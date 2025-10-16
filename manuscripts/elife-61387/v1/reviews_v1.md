# Peer review - Round 1

Editors:
- Alexander Shackman, University of Maryland United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.61387.sa1](https://doi.org/10.7554/eLife.61387.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper examines the relationship between psychopathology and decision-making adaptation to changes in contingency volatility in the environment. Previous work from the senior author has shown that individuals with high trait anxiety were less able to appropriately adjust their learning rate to the level of volatility in the context of aversive learning. The current paper extends this previous work in several ways: first, it takes a transdiagnostic approach to symptoms across both anxiety and depression; second, it conducts a very comprehensive model comparison to select the most appropriate behavioral model; third, it includes both aversive and appetitive learning, to test for generality vs. domain specificity of any finding; finally, it also compares the effects of positive and negative prediction errors across the reward and punishment domains. The authors report impaired adaptation of learning rate – in both the reward and punishment domains – as a function on a general factor of internalizing psychopathology, rather than anxiety specifically.

Decision letter after peer review:

Thank you for submitting your article "Impaired adaptation of learning to contingency volatility as a transdiagnostic marker of internalizing psychopathology" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor, Dr Shackman, and Senior Editor, Joshua Gold. The following individuals involved in review of your submission have agreed to reveal their identity: Argyris Stringaris and Samuel J Gershman.

The Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary

This paper examines relations between psychopathology and decision-making adaptation to changes in contingency volatility in the environment. Previous work from the senior author has shown that individuals with high trait anxiety were less able to appropriately adjust their learning rate to the level of volatility in the context of aversive learning. The current paper extends this previous work in several ways: first, it takes a transdiagnostic approach to symptoms across both anxiety and depression; second, it conducts a very comprehensive model comparison to select the most appropriate behavioral model; third, it includes both aversive and appetitive learning, to test for generality vs. domain specificity of any finding; finally, it also compares the effects of positive and negative prediction errors across the reward and punishment domains. The authors report impaired adaptation of learning rate – in both the reward and punishment domains – as a function on a general factor of internalizing psychopathology, rather than anxiety specifically.

The reviewers and I found several strengths to the report:

An admirable paper. The topic is of great interest, the care to replicate is refreshing to see, and the modeling is meticulous. We think it could be an important contribution to the field.

Overall, we were impressed with this study. The modeling and analysis was carried out carefully, and is comprehensive almost to the point that I worry the main ideas are obscured by layers of model variations (though I think it's okay as is). The new results add nuance to the emerging literature on computational modeling of anxiety and depression. They highlight the need for a transdiagnostic understanding of these disorders with respect to learning in volatile environments. We also appreciated that the authors made an effort to establish the generality of their findings across multiple populations and task variants, with relatively large sample sizes.

This is a very interesting and well written paper. It has several strengths, including a hierarchical Bayesian approach to the model fitting, careful model comparisons, and simulations to validate the winning model, as well as the use of both reward and punishment tasks, which is quite rare in this kind of studies. Results from a laboratory experiment were also largely replicated in an online study.

This will be a nice addition to the literature on learning under uncertainty and how such learning is affected in psychopathology.

Major/general suggestions

1) Bifactor Modeling. Noted by several reviewers.

a) More needs to be done in terms of ensuring that the modeling of the clinical data is appropriate and to demonstrate that the authors are in a position to draw some of the inferences they are drawing.

b) A lot in this paper hinges on the appropriateness of the bifactor modeling. I will try to explain. The paper is an extension of previous work that the authors have done in anxiety. The main innovation here is the extension to include a) depression; b) a negative affectivity or general factor resulting from the bifactor modeling. The latter, broadly, refers to a model of (typically) clinical symptoms where their common variance is accounted for by a general factor, and other latent factors (in this case anxiety and depression) retain their unique variance (and are thus uncorrelated to each other). Such models have similarities to other hierarchical symptom models. They have enjoyed a recent resurgence for a variety of reasons. The problem with these models is that they are pretty flexible and can easily be mis-specified. Given how much in this paper depends on the right choice of model, I would encourage the authors to do more to demonstrate that a bivariate model is indeed appropriate and superior to more parsimonious alternative. In particular, I am concerned about two things: first, the loadings for the general factor are relatively low, which is an indication that it may not really be a superordinate factor at all. Second, I am concerned about the fact that the authors do not seem to be comparing their model to a simpler structure (apologies if I have missed this) or alternative specifications (e.g. a super-ordinate model). I strongly suggest they do so and use appropriate metrics, such as the NLM. A good overview of the problems with inference and interpretation of such models is by Markon et al., Ann Rev Clin Psych 2019 and references therein, particularly Eid et al., 2017. Editor: See also recent simulation studies by Irwin Waldman's group and the HiTOP consortium (Roman Kotov)

c) Likewise, another reviewer wondered, "Is the bifactor analysis necessary? What happens is a simple factor analysis, or PCA, are used? Are the first three eigenvectors similar to the ones assumed in the bifactor analysis?"

2) Power Analysis. It would be useful if the authors gave an indication of how much power they would have in order to detect meaningful effect sizes for some of the two- and particularly three-way interactions in the paper. It may be appropriate to highlight this as a limitation of the study.

3) Model Validation. Given the concerns that have been expressed about the problems with LOO (being unrepresentative and often anti correlated with the training dataset, see Poldrack, 2019 JAMA Psych), the authors should either provide a rationale for selecting LOO or recompute using k-folds.

4) Differences Across Experiments. How do the authors explain the discrepancy between the two experiments with respect to the block type (volatile vs. stable) effect? Is it possible that the populations differed in their factor scores? From eye-balling Figure 1, this explanation seems implausible, but it would be useful to address this question statistically.
