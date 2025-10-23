# Peer review - Round 1

Editors:
- Misha Tsodyks, Weizmann Institute of Science , Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.01239.012](https://doi.org/10.7554/eLife.01239.012)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “A diversity of localized timescales in network activity” for consideration at eLife. Your article has been favorably evaluated by a Senior editor and 2 reviewers, one of whom is a member of our Board of Reviewing Editors.

The Reviewing editor and the other reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

This is a very interesting article from a theoretical perspective. It shows how a combination of non-Hermiticity and broken translation invariance can lead generically to surprisingly localized eigenfunctions. Biological implications of this result are that neuronal networks in the brain could have localized modes of activation characterized by different time scales.

The main issue that should be addressed in the revision is that, while on one hand, the analytical method for estimation of eigenvectors is the major contribution, the method is presented in an incomprehensible manner. As a result, one cannot appreciate why is it advantageous to simply diagonalize the connectivity matrix numerically (this issue is not discussed by the authors). Here is the list of points that have to be clarified.

1) Equation (7) - it has to be solved for j0 and w to find the shape of the corresponding eigenvector. How do we know the eigenvalues of the matrix? This is never explained. Moreover, in the first example considered, of Equation (13), the authors simply say that they ‘match the eigenvalues to j0 and w, to find that w=pi’. Is there an analytical expression for the eigenvalues of the matrix of Eq. (13)? If yes, the authors should provide it. It would make this example very special though. What if there is no such expression, would they have to diagonalize the matrix numerically? This would also provide the eigenvectors, so the whole procedure would seem to be redundant.

2) In the next example, of Equation (18), apparently there is no analytical expression for the eigenvalues, and the final solution for the width of the eigenvactor, Equation (21) still depends on j0 and w. The authors don’t explain how they find those.

3) In the presentation of the second-order expansion approach, the authors seem to ignore that both first-order and second-order corrections to eigenvalues have to vanish. They only consider the second order. Why does it makes sense to ignore the first-order correction?
