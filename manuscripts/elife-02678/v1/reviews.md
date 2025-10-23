# Peer review - Round 1

Editors:
- Vivek Malhotra, Center for Genomic Regulation (CRG) , Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.02678.020](https://doi.org/10.7554/eLife.02678.020)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Mechanisms of organelle biogenesis shape stochastic fluctuations in organelle abundance” for consideration at eLife. Your article has been favorably evaluated by a Senior editor and 3 reviewers, one of whom, Vivek Malhotra, is a member of our Board of Reviewing Editors.

The Reviewing editor and the other reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

1) In the model, organelle abundances arise from a combination of creation (by whatever means) and first-order decay. The authors claim that the decay term represents “an aggregation of a number of processes such as cell division, heterotypic fusion or autophagy”. In a fissioning cell population for high abundances, dilution can be approximated by a first-order decay term; but this is not true for low abundances. Furthermore, non-trivial behaviour can arise if partitioning between parent and daughter cells is not binomial. The authors would have to show (by simulation or any other means) why an explicit incorporation of partitioning during cell division is not required in their model. It could be, for example, that in a budding organism the daughter does not significantly affect organelle properties in the mother, and therefore the authors' model is a reasonable approximation.

2) There will be cell cycle variation in any of the rates considered; this will appear as an “extrinsic” term in the coefficient of variation, or equivalently a term proportional to the mean in the Fano factor. I assume from the Methods section that the authors pool all cells together (i.e., use a mixed or asynchronous culture). Using images alone, it is possible for the data to be partitioned by cell-cycle phase. Does this reveal identical organelle number distributions for all phases? If not, how much variation does one see? Another way to experimentally estimate the size of the extrinsic term is to see the change in Fano factor as a function of the mean. The authors have shown how this can be achieved by a shift to oleic acid medium or by using diploid cells. Can they use the resulting measurements to bind the extrinsic term?

3) The extrinsic noise issue is relevant to the peroxisome data. Here, the authors infer, from obtaining a Fano factor that exceeds 1, that peroxisomes are generated primarily by fission in oleic acid medium. Since the organelle abundance data are from a mixed asynchronous population, it is important to establish that the increase in Fano factor is not due to a cell-cycle-dependent de-novo synthesis rate.

The cell cycle specific issues could be addressed more clearly – experimentally – by arresting cells in a specific stage, S-phase, for example, and then re testing the model.

4) Test if the late Golgi marked with Sec7 behaves the same way as the early Golgi. Either outcome is likely to be highly significant and should be tested experimentally.
