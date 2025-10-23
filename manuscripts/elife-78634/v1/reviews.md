# Peer review - Round 1

Editors:
- Philip Boonstra, https://ror.org/00jmfr291 University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78634.sa0](https://doi.org/10.7554/eLife.78634.sa0)

This article proposes methodology and accompanying software for robustly fitting dose-response curves where response is a number between 0 and 1. When response is transformed using the common logistic transformation, values close to 0 or 1 become large in magnitude, unduly influencing the fitted curve after back-transformation and introducing bias in the estimate of certain parameters. As demonstrated through simulation and application to real data, the proposed approach, called Robust and Efficient Assessment of Potency, is less perturbed by these extreme measurements.


---

# Peer review - Round 1

Editors:
- Philip Boonstra, https://ror.org/00jmfr291 University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78634.sa1](https://doi.org/10.7554/eLife.78634.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Robust and Efficient Assessment of Potency (REAP): A Quantitative Tool for Dose-response Curve Estimation" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, including Philip Boonstra as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by and Aleksandra Walczak as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Following Reviewer 2's first comment, please clearly state what LRM is.

2) Related to this and as suggested above, please consider also comparing the REAP approach to a version of LRM with a heavy tailed error distribution such as t-distribution with 3 degrees of freedom, which would also seem to possess the same robustness properties as REAP.

3) Please conduct additional stress testing and debugging of the shiny app, if it is intended to be included and advertised in the manuscript. See Reviewer 1's comments for specific suggestions.

Reviewer #1 (Recommendations for the authors):

I would suggest running additional stress tests on the web app to address some of the bugs above. You might also add some additional features. For example, there is a little help key next to 'Add effect estimation' that, when you hover over it, explains what that does. Could more such keys be added to other user inputs?

As to the methodology, it seems to me like it would be worthwhile to consider an approach such as what I describe in my public review – essentially the linear model but with a heavy tailed error distribution that will be less sensitive to extreme values.

Reviewer #2 (Recommendations for the authors):

The topic of this manuscript is very interesting to many researchers who work on drug screening tests and development. The manuscript is well developed and well written. How I do have some comments for the authors to address.

(1) The authors should clearly state what the LRM is, I assume it is model (3) based on normal error assumption. However, the authors should clearly spell it out.

(2) The parameter β is estimated by minimizing (8) or (9), are the two equations (8) and (9) equivalent? If so, the authors should make the connection clear.

(3) In the method session, the authors mentioned the stability condition for the selection of the tuning parameter. What is the stability condition? The authors stated that "If the stability condition is satisfied before αmax is reached, then optimal α equals the minimal value in the grid of αk.". Do the authors imply that the optimal α equals the minimal value in the grids which met the stability condition?

Overall, this is a nice manuscript and will make a nice contribution to the field involving in-vitro drug screening and testing.
