# Peer review - Round 1

Editors:
- Birte U Forstmann, University of Amsterdam Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.60185.sa1](https://doi.org/10.7554/eLife.60185.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The Adolescent Brain Cognitive Development (ABCD) study is an unprecedented longitudinal neuroimaging sample that tracks the brain development of over 10,000 9-10 year olds through adolescence. Three tasks are completed repeatedly in the MRI scanner including the stop-signal task (SST). By analyzing the data of the SST, the authors identified eight design issues that could potentially limit the value of the ABCD. In this paper, prospective solutions for future users next to retrospective solutions for ongoing data users are provided overcoming potential limitations of the ABCD.

Decision letter after peer review:

Thank you for submitting your article "Design issues and solutions for stop-signal data from the Adolescent Brain Cognitive Development [ABCD] study" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Birte Forstmann as the Reviewing Editor and Richard Ivry as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Hans Colonius (Reviewer #1); Andrew Heathcote (Reviewer #2); René Huster (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper focuses on one of the benchmark magnetic resonance imaging (MRI) datasets, the so-called Adolescent Brain Cognitive Development (ABCD). In total, eight design issues observed in the stop signal task of the longitudinal ABCD study by Casey et al. (2018) are pointed out. The design issues are described in detail, ordered by importance, and a number of suggestions are given on how to overcome potential limitations. Given the importance and prominence of the ABCD study in the field of cognitive neurosciences, both the reviewers and editors believe this paper to highlight essential issues in a constructive way. Finally, we believe this paper will elicit a fruitful discussion including the adjustments of the design of the stop signal task.

Overall, this manuscript is well written, interesting, timely and will help resolve the debate in the field. We have the following suggestions to improve the manuscript.

Essential revisions:

1) As the authors suggest, the most important issue is the potential violation of the context invariance assumption due to the variability of the go stimulus duration across different stop signal delays (SSDs). This is a plausible concern even if the number of "clear" violations is relatively small (447 out of 7231 subjects). Nevertheless, the authors' point would be made even more convincing if they could point to some (simulation?) results showing the effect of a weaker go signal at short SSDs on the estimate of the stop signal response time (SSRT).

2) We suggest using the term "context invariance" instead of "context independence" , in order not to confound the assumptions of “context” and “stochastic” independence in the Logan-Cowan race model. It should be pointed out that the prediction of the race model concerning faster stop failures than go responses is conditional on both context invariance AND stochastic independence between go and stop signal processing being true (see Colonius and Diederich, 2018).

3) We recommend you perform and additional analysis: Let us suppose, as you suggest, that the RT distribution of responses to the go signal is indeed affected by the duration of the go signal. As a first approximation, let us assume that the observed RT distribution is a binary mixture of responses: slow RTs to a weak/short go stimulus and fast RTs to a strong/long gos stimulus. Without making specific assumptions about the two components of the mixture, one could employ a mixture distribution test first suggested by Falmagne (1968, British J. Math. Statist. Psychology): The RT ("density") distributions, plotted separately for each SSD and go signal trials, should all cross at one and the same point in time. Of course, this is not a foolproof test but if some evidence in favor of this prediction is found it would strengthen the authors' point.

4) There was some concern on whether the paper is appropriate for eLife given our reading of the most relevant aim, which is to publish "studies that use computational methods, models and software to provide important biological insights in all areas of the life sciences". The present paper does not make the sort of positive contribution that this statement seems to imply. Although the paper mentions that "new models for stopping must be developed to accommodate context dependence (Bissett et al., 2019), the latter of which we consider to be of utmost importance to advancing the stop-signal literature", it does not discuss such models and neither does it show the potentially severe consequences of context independence violations in the ABCD data set. Efforts on this issue would strengthen the contribution.

5) The authors write: "Given the above, if analyzing or disseminating existing ABCD stopping data, we would recommend caution in drawing any strong conclusions from the stopping data, and any results should be clearly presented with the limitation that the task design encourages context dependence and therefore stopping behavior (e.g., SSRT) and neuroimaging contrasts may be contaminated". We feel that this recommendation is too lenient and would suggest the following alternative: Unless the ABCD community conclusively shows that the design flaw does not distort conclusions based on SSRT estimates (or any other stop-signal measure), researchers should not use the ABCD data set to estimate SSRTs at all.

6) The authors suggest removing subjects who have severe violations as evidenced by mean stop-failure RT > mean no-stop-signal RT. We are concerned that this recommendation impacts on the representativeness of the sample. Also, this recommendation ignores the fact that violations are not an all-or-none phenomenon but are a matter of degree and can come in varying shapes and sizes.

7) The authors recommend that "any results be verified when only longer SSDs are used, perhaps only SSDs > 200ms". Figure 3 does not seem to support the recommended cut-off of 200ms: at 200ms accuracy is still far from asymptotic.

8) In general, we feel that recommendations based on removing participants and trials are not sufficient such practices will affect the representativeness of the sample and will increase estimation uncertainty and hence decrease power. The real solution here seems to be to develop measurement models that can account for the dependence of the go and the stop process.
