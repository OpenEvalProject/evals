# Peer review - Round 1

Editors:
- Michael Levitt, Stanford University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.07454.017](https://doi.org/10.7554/eLife.07454.017)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Contacts-based prediction of binding affinity in protein-protein complexes” for consideration at eLife. Your article has been favorably evaluated by Michael Marletta (Senior editor), a Reviewing editor, and two reviewers.

Both reviewers found the manuscript interesting and we would like to invite the authors to submit a revised manuscript that addresses the reviewers' comments.

Reviewer #1:

The authors wish to predict binding affinity (BA), clearly a problem whose importance is hard to overstate. This is a mature field, and has an excellent tradition of methodological contributions with discussion of physicochemical significance. The authors find that ICs are more strongly correlated to BA than buried surface area (BSA) is. No explanation is provided for this, which I think should be corrected. I also think since prior workers have separated BSA into polar and nonpolar contributions, counted hydrogen bonds, etc., the authors should do the same for ICs, as this may improve the results.

It is interesting that IC appears to be a better predictor of BA compared to BSA, even though IC seems a cruder measure. Please try to find the underlying reason for this. I suspect I know the reason.

The fact that the 4Å cutoff is optimal is significant, in my opinion. The authors should try to explain.

It is not clear that the minimum correlation is at 20Å, since this is the largest interface distance tested.

Mean absolute error is not a very standard error measure. Please use a measure that is more common in the literature.

The fact that only three fitting parameters were used effectively eliminates the possibility of overfitting. Still, I think the success of the method raises important questions. Do all contacts contribute equally to BA? What if contacts were to be grouped into e.g. salt bridges, hydrogen bonds, hydrophobic, etc.? I don't think it would be hard to count these. Horton and Lewis did something like this, separating polar from nonpolar buried surface area. I don't see that they report the error, but their Table 2 suggests it is comparable to that in the present work. Chothia and Janin also indicate the importance of separating polar and nonpolar contacts. The current results are not compared quantitatively to methods from the literature. Doing this would make it clear to what extent the new method is better than the existing ones.

In general I think this paper is promising. I don't doubt that it will eventually be published, either here or elsewhere. However the questions it raises ought to be answered. Otherwise this paper will merely report a phenomenon, without adding understanding. Also the comparison to past methods should be improved.

Reviewer #2:

It is an interesting work dealing with the prediction of energies of protein - protein interactions. Some aspects of the work should be improved.

The authors do not report the performance of other methods when applied to the same dataset. I see only the comparison of the performance of inter-residue contacts to buried surface area. The report of an explicit comparison of results obtained on the same dataset by other approaches, well quoted into the Introduction, should improve the quality of the article.

In the paragraph “The effect of conformation changes on BA prediction's accuracy” the authors refers again to other models to indicate their method as preferred for being less sensitive to conformational changes, without reporting a comparison of the results obtained by that models for the two subsets of rigid and flexible complexes.

The training and prediction sets give quite different results. This should be discussed and explained. Maybe, the random division in the two sets could be repeated a high number of times, and a mean result could be considered.
