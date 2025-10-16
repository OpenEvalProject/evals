# Peer review - Round 1

Editors:
- Jonathan Flint, Wellcome Trust Centre for Human Genetics , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.11814.017](https://doi.org/10.7554/eLife.11814.017)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for submitting your work entitled "Genetic variation in offspring indirectly influences the quality of maternal behaviour in mice" for consideration by eLife. Your article has been favorably evaluated by Diethard Tautz (Senior editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper demonstrates that indirect genetic effects can be identified and genetically mapped. The authors adopt a cross-fostering design so that in families either the mothers or the offspring are genetically variable (from the BXD recombinant inbred panel) while the corresponding offspring or mothers show no genetic variation (i.e. are from the B6 inbred strain). The authors identify three indirect genetic effects, and three direct genetic effects. Overall this study represents a substantial and well-designed effort to address an important question.

Essential revisions:

1) Design limitations need to be acknowledged and discussed. In their design the in-utero maternal effects are perfectly confounded with offspring genotypes. This means that the results of part 1 could be interpreted as "Variation in BXD mothers genotypes causes variation in in-utero environment, which causes variation in BXD offspring behaviour later in early life, which causes variation in B6 adoptive mothers provisioning". This would effectively be IGE from BXD mothers on B6 mothers.

The results of part 2 could be interpreted as "Variation in BXD mothers genotypes causes variation in in-utero environment, which causes variation in BxD offspring weight gain and solicitation in early life" and Variation in BXD mothers genotypes independently causes variation in BXD biological mothers provisioning, in which case there would not be coadaptation between BXD offspring phenotypes and BXD maternal behaviour.

This caveat is sufficiently important that its implications should be discussed in the Discussion. As the authors note in the Discussion however, overcoming this limitation would be extremely challenging.

2) The results are only just significant. Given that they have tested multiple behaviors, and both direct and indirect effects, the chances are that a proportion of the loci are likely false positives. The authors should assess a false discovery rate and provide results corrected for the total number of tests carried out.

3) The mapping approach is relatively un-sophisticated and in particular environmental effects receive scant attention. Cage effects should be accounted for in all the analyses. In addition there may be unacknowledged environmental effects, which might be captured if they included the time when the experiment was carried out as a covariate. The fact that results for the genetic effects only just achieve significance means that there is a concern that even slight contributions from covariates may be giving rise to false positives.

4) It wasn't clear why they used per pup values. Why not fit litter size should be fitted as a covariate? They should repeat the analyses with litter fitted as a covariate.

5) The phenotypic correlation observed between BXD offspring solicitation and B6 maternal behaviour could arise from environmental effects only as BXD offspring and B6 mothers share a cage. It is not strong evidence that BXD genotypes affect B6 maternal behaviour, and can only weakly be linked to the QTLs identified as no overlap was found between DGE QTLs for offspring solicitation and IGE QTLs for maternal behaviour. Genetic correlation should be computed from the individual measurements.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Genetic variation in offspring indirectly influences the quality of maternal behaviour in mice" for further consideration at eLife. Your revised article has been favorably evaluated by Diethard Tautz (Senior editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors. The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

You state that you have "used the correct litter size to calculate per pup measures, namely adoptive litter size." That a litter size effect exists does not imply that per pup values are appropriate, i.e., it does not prove that per pup values are independent of litter size. This would only be correct if you could prove that total provisioning is exactly linear in litter size; the mere significance of a (linear) litter size effect is no proof thereof.

Intuitively, one would expect that provisioning per pup decreases with litter size, simply because there is some sort of limit to total provisioning that is feasible. If you can fit a litter size effect on total provisioning using linear models, then you can also do this on provisioning defined per pup.

While this may not be feasible in the Genenetwork software that you used for the mapping, it could be investigated in a prior analysis using simple linear models. Then the results should be reported in the manuscript, and if the litter size effect on per pup provisioning is significant in the prior analysis, then you should acknowledge in the manuscript that ideally a covariate for litter size would have been included in the mapping.

The correlation/covariance that may exist between direct and indirect environmental effects (IDE and IEE) should be modelled when calculating the correlation between mother and offspring phenotypes as it may increase or decrease the correlation reported in the manuscript.

Example of such a correlation between IDE and IEE: differences in noise across cages may lead to B6 mothers in noisy cages showing reduced maternal behaviour and BXD offspring in those same cages soliciting less (or more).

To account for this covariance, you would need to focus on the genetic component of the correlation and use the replicate structure of the data (3 replicates per genotype) to calculate something analogous to a genetic correlation but where phenotypes are measured in B6 mothers and BXD offspring (instead of in the same individual as is traditional) and the genotypes would be those of the BXD offspring.

Although a sentence was added in the Discussion with regard to in-utero effects, you still need to put the results of part 1 in perspective and address interpretation of the results of part 2 (co-adaptation).
