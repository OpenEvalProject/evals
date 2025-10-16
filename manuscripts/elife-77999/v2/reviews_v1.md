# Peer review - Round 1

Editors:
- George H Perry, https://ror.org/04p491231 Pennsylvania State University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77999.sa0](https://doi.org/10.7554/eLife.77999.sa0)

The authors use a comparative genomics approach to predict gene function, in particular genes that have a role in eye development. After identifying the convergent loss of SERPINE3 with vision loss across mammals, the authors confirmed its involvement in eye development by characterizing zebrafish knockouts. This work highlights the power of comparative genomics to generate hypotheses that can be experimentally validated. This work is relevant to a broad audience interested in evolution and adaptation as well as for those studying eye development and eye pathologies.


---

# Peer review - Round 1

Editors:
- George H Perry, https://ror.org/04p491231 Pennsylvania State University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77999.sa1](https://doi.org/10.7554/eLife.77999.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Vision-related convergent gene losses reveal SERPINE3's unknown role in the eye" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and George Perry as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Stephen Treaster (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers were positive but also consistent in their major concerns about the pipeline and its output, requiring more clarity/data and at least some level of additional supporting validation, perhaps including manual curation. I agree that these concerns need to be addressed, including some further cross-checking of the database Hopefully this is possible with existing cross-species RNA-seq datasets, and does not require the generation of new experimental data.

Overall, congratulations on this nice study, and I look forward to seeing the manuscript at its next evolutionary stage!

Reviewer #1 (Recommendations for the authors):

I have only one comment: The authors identify a very large number of putative gene losses in many different species. Given that usually the majority of such bioinformatically identified gene losses are false positives due to annotation or sequencing artifacts, a manual curation is usually critical – even with the most sophisticated algorithms. According to the methods this has not been performed. I am aware that the authors are world experts in identifying gene losses, but I am still skeptical that all of these are true events (given the sheer number). I recommend that the authors use existing RNA-Seq data sets (for example from the naked mole rat) or PCR from genomic DNA to confirm at least a subset of the ones that they are showing.

Reviewer #2 (Recommendations for the authors):

Many of the filters are explained in the previous publications generating the dataset, however, there seem to be four additional thresholds to reuse that dataset for this analysis. While these filters may all be appropriate, it is opaque to the reader. (1) visual acuity cutoffs, (2) percent of high and low acuity lineages with assembly gaps, (3) requiring an intact score in >80% of high acuity lineages and lost in <10% in high acuity lineages, (4) requiring the gene be lost in at least three of the seven independent low-acuity lineages. There is a brief expansion on filter 1 by trying two other close acuity cutoffs. However, these other acuity cutoffs seem to have dramatic consequences that are not discussed. 20 of the 26 top hits vanish when using a cutoff of 2 instead of 1. With such an impact, it is difficult to interpret what exactly is being measured or what the "right" cutoff may be to get the best measure of vision loss. This is exacerbated by the unintuitive nature of visual acuity scores. Unlike the iconic convergence examples, the operational difference between visual acuity scores of 0.5, 1, and 2, or even 2 and 20, is not obvious. If a continuous measure is going to be binarized, there should be a more apparent argument for the cutoffs, particularly since the 0.5 cutoff has more significant results than 1, but is not the focus of the manuscript.

Filters 3 and 4 appear to be redundant with each other and convergence analysis itself. The analysis is already scoring genes for intactness in conjunction with the trait, so it seems unnecessary to exclude genes from the analysis based on patterns of intactness in conjunction with the trait. It's the same measurement, twice. The purpose of these filters is unclear. The consequences of these filters on p-value distributions, multiple hypothesis corrections, and top hits are unclear, and possibly inappropriate. The lack of a negative control again exacerbates these concerns. While it is non-trivial to select a control set (or many sets) of lineages with comparable topological relationships as the experimental group, it is necessary to demonstrate the robustness of the method and dataset.

Including entire gene lists in the supplemental tables for each method (as opposed to just the top 26 of a single method) would helpfully provide the raw p-values for the distributions mentioned above, allow more comparison and quantification of differences between cutoffs, and allow for future intersections with other datasets. This would dramatically increase the utility of the overall convergence results for the field. In conjunction, there is a truly impressive amount of genomic work here that is unlikely to be replicated by someone else that wants to do a similar analysis on a different phenotype, but the dataset itself does not seem to be available.
