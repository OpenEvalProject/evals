# Peer review - Round 1

Editors:
- Michael Levitt, Stanford University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.08932.012](https://doi.org/10.7554/eLife.08932.012)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for submitting your work entitled “Codon-level information improves predictions of inter-residue contacts in proteins by correlated mutation analysis” for peer review at eLife. Your submission has been favorably evaluated by Aviv Regev (Senior Editor) and two reviewers, one of whom is a member of our Board of Reviewing editors. The Reviewing Editor has drafted this decision to help you prepare a revised submission.

The paper presents a potentially important advance in the area of deducing spatial contacts between amino acids in globular proteins, by proposing a simple yet elegant modification, which combines the analysis of amino acid and codon MSAs. While the results are potentially interesting, there are some important statistical analyses which are still lacking and need to addressed in the revision. In particular (1) the authors should incorporate statistical testing to assess the significance of the differences in accuracy with and without incorporating codon information. One would want to know if the improvement is robust, and it could be also that there are specific sub-classes where it is more/less beneficial. The scope of alternative methods to compare to should also be expanded. (2) The authors should show compelling analyses that address the question of over-fitting vs. generalization. This can be accomplished by cross-validation (the correct way to choose a set of parameters), and then with an additional test set (for seeing how the parameters chosen by cross validation perform on new data).

Essential revisions:

1) In Figure 1, there are differences shown for accuracy with and without incorporating codon information, but it is unclear if these differences are significant. Figure 1 shows the mean accuracy across the alignments, but it would be straightforward to also show or report the variance or standard deviation across the alignments. Then an explicit P-value could be put on a null hypothesis that incorporation of codon information increases or decreases accuracy. In general, the apparent result in Figure 1A that incorporation of codon information into SDCA either helps or hurts depending on how contacts are defined reduces confidence that incorporation of codon information is robustly improving the underlying algorithms.

2) In Figure 1B, the incorporation of codon information appears to help OMES and MI, but a more appropriate comparison might be to other algorithms that attempt to correct for phylogenetic artifacts (see for example http://bioinformatics.oxfordjournals.org/content/24/3/333.short; Mutual information without the influence of phylogeny or entropy dramatically improves residue contact prediction).

3) The data in Figure 2 should be on one plot. The figure needs to clearly emphasize that one set of lines are without the codon data and the other set are with it. This makes a huge difference and it the important conclusion of the work. The effect of how close distances are determined (Cβ or All) is minor and confusing.

4) In tuning a free parameter, such as is being performed in Figure 3, it is not surprising that a value for the free parameter alpha can be found that improves the performance. But does this just reflect over-fitting? It would perhaps be more informative to split the data into a training set and a test set, and evaluate the improvement on the test set which was not used to estimate alpha. By repeating this process on permutations of randomly chosen test sets and training sets, it might be possible to determine how stable estimates of alpha are or, alternatively, to demonstrate that the optimal value of alpha is highly variable from training set to training set.
