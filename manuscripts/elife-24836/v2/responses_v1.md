# Author response - Round 1

Authors:
- Daniel B Weissman ([ORCID: 0000-0002-7799-1573](https://orcid.org/0000-0002-7799-1573))
- Oskar Hallatschek

## Response text

DOI: [10.7554/eLife.24836.014](https://doi.org/10.7554/eLife.24836.014)

Essential revisions:

The analysis of real data and its presentation could be improved, and help readers understand the method better.

For the analysis, the switch to the piecewise-exponential form has slightly improved the performance, and the additional curves in Figure 4 hopefully give a somewhat better sense for the levels and forms of noise and bias in the method.

For example, Figure 4 shows that MAGIC apparently doesn't improve population size estimates in Yoruba over MSMC, even though the MSMC results are based on single individuals while MAGIC analyses all 9 simultaneously.

Yes, this is an important point. We have added it in the first paragraph of the subsection “Human data”.

At the same time, when estimating tip branch lengths, Figure 4 (right hand side) shows impressively how MAGIC's estimates are contradicting the Ne model from both MSMC and MAGIC based on pairwise coalescence times, thus perhaps revealing that the model is not good. This advantage should be made clearer, and it may also be useful to point out potential ways forward. For example, joint analysis of pairwise coalescence times and tip branch lengths might suggest better models, or generally improve estimates for certain parameter values?

This would emphasize MAGIC's utility as a flexible analysis tool that can handle large data sets.

We have only added a few lines of text to this section and the Discussion, but we hope that they help make things a little clearer. The key part is –at the end of the subsection “Human data” – we think that MAGIC can be used with ad hoc ABC to match multiple inferred branch length distributions, or to check the results of multiple stand-alone inference methods. We have also added more on this point in the second paragraph of the subsection “Approach” and in the fourth paragraph of the Discussion.
