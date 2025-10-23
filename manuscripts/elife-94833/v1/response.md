# Author response - Round 1

Authors:
- Aurélie Anne-Gaëlle Gabriel ([ORCID: 0000-0002-0606-3622](https://orcid.org/0000-0002-0606-3622))
- Julien Racle ([ORCID: 0000-0002-0100-0323](https://orcid.org/0000-0002-0100-0323))
- Maryline Falquet
- Camilla Jandus
- David Gfeller ([ORCID: 0000-0002-3952-0930](https://orcid.org/0000-0002-3952-0930))

## Response text

DOI: [10.7554/eLife.94833.4.sa3](https://doi.org/10.7554/eLife.94833.4.sa3)

The following is the authors’ response to the previous reviews.

Recommendations for the authors:

Reviewer #1 (Recommendations For The Authors):

I praise the authors for their impressive work; all my major concerns have been addressed. I believe the revised article is much stronger and will surely raise the interest of a broad readership.

I list in the following a few minor points that the authors might want to consider when finalizing the work:

- It might be helpful for the reader to know if EPIC-ATAC can also be used on tissues different from tumors and PBMC/blood, and how (i.e. which reference should they use).

We thank the reviewer for this comment. In the discussion, we have clarified this point as follows:

“Although not tested in this work, the TME marker peaks and profiles could be used on normal tissues where immune cells are expected to be present. In cases where specific cell types are expected in a sample but are not part of our list of reference profiles (e.g., neuronal cells in brain tumors or tissues other than human PBMCs or tumor samples), custom marker peaks and reference profiles can be provided to EPIC-ATAC to perform cell-type deconvolution. To this end, users should select markers that are cell-type specific, which could be identified using pairwise differential analysis performed on ATAC-Seq data from sorted cells from the populations of interest, following the approach developed in this work (Figure 1, see Code availability).”

- In Fig 2 the numbers are hard to read as they are too close or overlapping.

We have updated Figure 2 to avoid the overlap between the numbers.

- In Fig 5 I see some squared around the sub-panels, but it might be due to the PDF compression.

We do not see these squares on the Figure 5 but have seen such squares on Figure 1. We have checked that all the PDF files uploaded on the eLife submission system do not contain the previously mentioned squares.

- In the Introduction, some "deconvolution concepts" are introduced (e.g. Line 63-65), but not explained/illustrated. It might be helpful to refer to a "didactic" review.

We have added two references to these sentences in the introduction:

“As described in more details elsewhere (Avila Cobos et al., 2018; Sturm et al., 2019), many of these tools model bulk data as a mixture of reference profiles either coming from purified cell populations or inferred from single-cell genomic data for each cell type.”
