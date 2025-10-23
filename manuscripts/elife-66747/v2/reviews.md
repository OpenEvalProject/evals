# Peer review - Round 1

Editors:
- Alex K Shalek, Broad Institute of MIT and Harvard United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66747.sa1](https://doi.org/10.7554/eLife.66747.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

The development of single-cell genomic methods has transformed our understanding of cell types and their attributes across organisms. Here, Tarashansky et al. develop SAMap (Self-Assembling Manifold mapping), a graph-based data integration method which builds upon their previously described SAM algorithm, to facilitate assignment of homologous genes and cell types across diverse species. As the authors show, this empowers comparative analyses across phyla to facilitate cellular annotation and examine the evolutionary origins of cellular diversity. Overall, the algorithm has the potential to be broadly enabling for comparative cellular atlasing.

Decision letter after peer review:

Thank you for submitting your article "Mapping single-cell atlases throughout Metazoa unravels cell type evolution" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Alex K Shalek as the Reviewing Editor and Naama Barkai as the Senior Editor. The reviewers have opted to remain anonymous.

The Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. While authors clearly demonstrate the promise of SAMap, the manuscript would benefit from an accessible discussion of the algorithm's potential applications, limitations and drawbacks to help inform use. For example, how does the algorithm depend on cell numbers, data quality, or the use of a consistent experimental method? If a cell type is missing from one atlas (e.g., due to limited cell numbers), will the algorithm overfit? Performing downsampling analyses, leaving one cluster out (e.g., when comparing zebrafish and Xenopus (Figure 2)), or linking datasets across methods (e.g., Smart-Seq2 and 10x; inDrop and 10x) would help to address these points.

2. The authors' analyses present several intriguing evolutionary observations such as those on widespread paralog substitution, the multifunctionality of ancestral contractile cells, and the existence of a deeply conserved gene module associated with multipotency. Each would benefit from further investigation. For example, with respect to the paralogs, are similar levels of substitution observed when paralogs are excluded during manifold assembly (i.e., do they drive cell type assignments)? Similarly, how does paralog substitution depend on how recently those paralogs arose or their stability? Meanwhile, the points on multifunctionality and multipotency would benefit from deeper analysis and discussion, or more cautious language. Re: the first point above, each observation would also benefit from presentation of potential alternative interpretations in the Discussion section.

Reviewer #1 (Recommendations for the authors):

I am very supportive of this manuscript and agree with the authors assessment of the utility of the method they have developed. My major concerns emerge from some of the evolutionary interpretations of the results. In particular, I wonder whether it would be possible to exclude the paralog pairs for which substitution has been observed during manifold assembly to determine whether those paralogs are driving cell type assignments leading to a tautology. I would recommend that in the three instances where evolutionary conclusions are proposed, the authors consider alternative interpretations within their discussion.

Reviewer #2 (Recommendations for the authors):

The paper is solid.

Reviewer #3 (Recommendations for the authors):

The study and methods give a great conceptual overview of the novel approach, but the details for implementation are not clear, and the github is not well documented. I would encourage further details and more clear documentation on the github – for example the paralog substitution findings are an important result and use case, but there is limited methods description and it is unclear how to run the function.

Finally, the reciprocal BLAST is slow to run, especially for all by all transcripts, but it only needs to run once. I would consider posting the results of this analysis on the github for widely used species pairs, which could also accelerate adoption by reducing the barrier to running the full suite.
