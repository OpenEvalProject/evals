# Peer review - Round 1

Editors:
- Arvind Murugan, https://ror.org/024mw5h28 University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80927.sa0](https://doi.org/10.7554/eLife.80927.sa0)

This work makes an important contribution to the study of the cell cycle and inferring mechanisms by studying correlations in division timing between single cells. By treating the problem in a general way and computing over lineage trees, the authors can infer timescales in the underlying mechanism. The method is validated on data sets from bacterial and mammalian cells and can suggest when additional measurements are needed to distinguish competing models.


---

# Peer review - Round 1

Editors:
- Arvind Murugan, https://ror.org/024mw5h28 University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80927.sa1](https://doi.org/10.7554/eLife.80927.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Patterns of interdivision time correlations reveal hidden cell cycle factors" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Michael J Rust (Reviewer #1); Farshid Jafarpour (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) As suggested by reviewer 1, please include mechanistic details for circadian rhythm models (e.g., showing the inheritance matrix). Also, explain why whether leading order approximations are valid for oscillatory models as suggested by the same reviewer.

2) As suggested by reviewer 2, more intuition is needed for some of the results. E.g., intuition why only eigenvalues of the inheritance matrix matter + intuition for the alternator pattern.

Reviewer #1 (Recommendations for the authors):

Concretely, while section 4 of the supplement shows how some simple mechanistic models map onto this formalism, none of these include an explicit circadian rhythm. Since the authors did develop a model like this in Martins et al., it would be valuable to show what the inheritance matrix, etc. are for this kind of model, and indeed whether going to leading order in fluctuations works satisfactorily.

Reviewer #2 (Recommendations for the authors):

The paper is well-written, scientifically sound, and easy to follow. I only have a few minor suggestions/comments:

1) It is not clear what the variance in Equation 4 is. Is it the variance of generation times across a single lineage or across the whole tree or the population variance? If I understand it correctly from the derivation in SI, it should be a lineage variance, which may not be immediately obvious given that rho is a tree variable. So it would be nice to specify which one it is.

2) I find it very surprising that only the eigenvalues of the inheritance matrix determine the correlation patterns, while all the other parameters, including how noises are correlated (anticorrelated) and whether growth factors have a positive or negative effect on the inter-division times, are irrelevant. It would be nice if the authors could provide an intuition for why that is the case.

3) The authors have used the AIC method for the goodness of fit. Initially, without being familiar with the method, I found it surprising that in the case of mycobacteria, a more general model could have a worse fit than its special case. I think a one-sentence explanation of this method could prevent such potential confusion for readers not familiar with this method.

4) What is the intuition behind the alternator pattern, i.e. why is there a period 2 oscillation in a model with real eigenvalues?

5) In the model, the inter-division time is a deterministic function of the cell-cycle factors (Equations 1 and 3a). The noise is only allowed in the inheritance of these factors, not in the division itself. This puts a constraint on what variables of a given model can be used as cell-cycle factors. I think this would be worth mentioning in the paper.
