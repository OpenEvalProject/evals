# Author response - Round 1

Authors:
- Rob Bierman ([ORCID: 0000-0001-8513-7425](https://orcid.org/0000-0001-8513-7425))
- Jui M Dave
- Daniel M Greif ([ORCID: 0000-0002-9842-3751](https://orcid.org/0000-0002-9842-3751))
- Julia Salzman ([ORCID: 0000-0001-7630-3436](https://orcid.org/0000-0001-7630-3436))

## Response text

DOI: [10.7554/eLife.87517.2.sa4](https://doi.org/10.7554/eLife.87517.2.sa4)

Reviewer #1:

We agree with Reviewer 1 that the flexibility of SPRAWL also makes it difficult to interpret its outputs. We consider SPRAWL to be a hypothesis-generation tool to answer simple questions of subcellular localization in a statistically robust manner. In this paper we include examples of how it can be incorporated with other tools and wetlab experimentation to build biological intuition. Our hope is that the SPRAWL software, or even the underlying simple statistical ideas are of use to others in the field.

Reviewer #2:

We agree with Reviewer #2 that this manuscript does not demonstrate biological significance of the observed results of applying SPRAWL to massively multiplexed FISH datasets. We agree it would require additional wetlab experiments such as cell-type specific and isoform-resolved fluorescence in-situ hybridization, which we consider beyond the scope of this paper. We believe that the observed correlations of subcellular localization detected by SPRAWL and the differential 3’ UTR usage detected by ReadZS are compelling, although not conclusive, as are the Timp3 experimental studies.

Our understanding is that Baysor is primarily a cell-segmentation algorithm, which is not what SPRAWL attempts to achieve. Baysor states that it identifies “cells of a distinct type will give rise to small molecular neighborhoods with stereotypical transcriptional composition, making it possible to interpret such neighborhoods without performing explicit cell segmentation” which we understand to mean that Baysor identifies spatial groupings of cells with “stereotypical transcriptional composition” rather than subcellular RNA localization. We do not think that SPRAWL and Baysor are comparable, but instead Baysor could be used as an upstream step to SPRAWL to potentially improve cell segmentation.

Reviewer #3:

We thank Reviewer #3 for identifying discrepancies in the paper which we addressed to the best of our abilities.
