# Peer review - Round 1

Editors:
- Peter Tontonoz, https://ror.org/046rm7j60 University of California, Los Angeles United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80167.sa0](https://doi.org/10.7554/eLife.80167.sa0)

This study elucidates transcriptional profiles of the stromal vascular fraction of murine brown adipose tissue in the context of thermogenic stimulation. The authors combine systems and reductionist approaches to show the reliance of mature brown adipocytes on adrenergic activation to indirectly stimulate progenitor proliferation and differentiation. This timely work will provide beneficial data for public use and further resolve the complexities underlying brown adipose physiology.


---

# Peer review - Round 1

Editors:
- Peter Tontonoz, https://ror.org/046rm7j60 University of California, Los Angeles United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80167.sa1](https://doi.org/10.7554/eLife.80167.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Deconstructing cold-induced brown adipocyte neogenesis in mice" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Peter Tontonoz as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Carlos Isales as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Patrick Seale (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers do not believe that any additional experiments are required. Please respond to the discussion points and technical concerns in a revised manuscript.

Reviewer #1 (Recommendations for the authors):

A pseudotime or latent time analysis (RNA velocity) would be an effective way to present the data showing ASC1 commitment to brown adipogenesis. CellRank is a newer method which can integrate time course, RNA velocity, and clustering analyses to determine terminal states of cells that can be easily adapted to the authors existing Seurat pipeline, if they so choose. Usage of a splicing-aware aligner can generate gene expression matrices of spliced and unspliced transcripts that can be appended to existing Seurat objects as assays and exported into Python for analysis with scVelo [PMID: 32747759] and CellRank [PMID: 35027767].

Reviewer #2 (Recommendations for the authors):

1. Please explain why mice were adapted to RT rather than thermoneutrality for the control mice used in the single cell experiments (since RT mice are also cold)? Could this affect interpretations?

2. It would be nice to include functional data showing that the ASC1 population is the exclusive source of brown adipocytes.

3. It was surprising that the authors did not test if KO of Adrb1 in other populations (e.g. BAs) inhibits NE-stimulated neogenesis as they showed by global KO that it is required. What's the key cell population?

4. These data are beautiful and establish interesting hypotheses, though I would have liked to see more functional analysis of potential mechanisms, for example between immune-BA interactions. Nevertheless, I do think this is appropriate for eLife.

Reviewer #3 (Recommendations for the authors):

Overall, I find the paper to be very compelling and strongly support publication in eLife without delay.
