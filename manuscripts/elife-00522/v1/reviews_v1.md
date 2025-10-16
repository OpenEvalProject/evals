# Peer review - Round 1

Editors:
- Roderic Guigo, Center for Genomic Regulation , Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.00522.028](https://doi.org/10.7554/eLife.00522.028)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Cellular resolution models for even skipped regulation in the entire Drosophila embryo” for consideration at eLife. Your article has been favorably evaluated by a Senior editor and 3 reviewers, one of whom is a member of our Board of Reviewing Editors.

The following individuals responsible for the peer review of your submission each wish to reveal their identity: Roderic Guigo (Reviewing editor); Mike Levine (peer reviewer).

The Reviewing editor and the other reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

1) Two of the reviewers raised concerns about the statistical methods employed to validate the model. Specifically, one of the reviewers stated that the conclusions should be drawn from a blind test or N-fold cross validation; however, the authors used this to test the model over-fitting as a separate section. Nevertheless, if we understood them correctly, the main conclusions presented are drawn from using the entire set of data points, including those used for training. This is circular, and the authors should clarify this point in the main text. The over-fitting assessment is not generally necessary here, as the number of parameters is considerably below the number of independent data points.

2) Two of the reviewers also suggested that the authors should further investigate the correlation between the input variables and test models including fewer variables. One of the reviewers suggested that you might use stepwise logistic regression as a way to select those variables that are truly informative. Using all combinations of 4 variables (in the case of stripe 2) did not seem the optimal way to infer the minimum combination of maximally informative variables.

3) Two of the reviewers also raised concerns about the way you attempted to simulate the effects of perturbation by manipulating the input signal of the regression model without changing its learned coefficients. One of the referees specifically believes that this practice is incorrect, simply because the model was learned and optimized based on 3 input signal, and should be re-optimized if you decided to remove one input. Again the model comparison should be conducted by a blind test, not all entire dataset used for training.

4) Two of the reviewers asked themselves whether it would not be of interest to test the stability of the models during development. One of the referees specifically encouraged the authors to extend their models to earlier stages of development, namely the first 20 min of nuclear cleavage cycle 14.

5) The utility of the models rely on their capacity to generate testable hypotheses. In this regard, one of the referees asked whether any novel prediction that could be experimentally tested has been derived from the model. This is an issue that should be made more explicit by the authors.
