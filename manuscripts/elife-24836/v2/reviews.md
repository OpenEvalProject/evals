# Peer review - Round 1

Editors:
- Magnus Nordborg, Vienna Biocenter , Austria

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.24836.013](https://doi.org/10.7554/eLife.24836.013)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Minimal-assumption inference from population-genomic data" for consideration by eLife. Your article has been favorably evaluated by Diethard Tautz (Senior Editor) and three reviewers, one of whom, Magnus Nordborg (Reviewer #1), is a member of our Board of Reviewing Editors. The following individuals involved in review of your submission have agreed to reveal their identity: Stephan Schiffels (Reviewer #2); Paul Marjoram (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Polymorphism data contains information about the evolutionary history of the population, and can be used for inference about the process that gave rise to the data. In the era of cheap genome sequencing, this is of great interest. However, generally speaking, the polymorphism data reflects an underlying "ancestral recombination graph", which, in itself, is a product of the evolutionary process. If we could infer this graph, we would not need the polymorphism data. This theoretical paper describes a method for extracting information about this graph under a fairly general model – information that can then be used for further dissection of the evolutionary process. As is demonstrated in the paper, this can be massively more efficient than trying to infer the details of this process directly from the polymorphism data.

Essential revisions:

The analysis of real data and its presentation could be improved, and help readers understand the method better. For example, Figure 4 shows that MAGIC apparently doesn't improve population size estimates in Yoruba over MSMC, even though the MSMC results are based on single individuals while MAGIC analyses all 9 simultaneously. At the same time, when estimating tip branch lengths, Figure 4 (right hand side) shows impressively how MAGIC's estimates are contradicting the Ne model from both MSMC and MAGIC based on pairwise coalescence times, thus perhaps revealing that the model is not good. This advantage should be made clearer, and it may also be useful to point out potential ways forward. For example, joint analysis of pairwise coalescence times and tip branch lengths might suggest better models, or generally improve estimates for certain parameter values?

This would emphasize MAGIC's utility as a flexible analysis tool that can handle large data sets.
