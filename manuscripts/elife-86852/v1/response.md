# Author response - Round 1

Authors:
- David J Bacsik ([ORCID: 0000-0003-4912-0209](https://orcid.org/0000-0003-4912-0209))
- Bernadeta Dadonaite ([ORCID: 0000-0003-0908-6982](https://orcid.org/0000-0003-0908-6982))
- Andrew Butler ([ORCID: 0000-0003-3608-0463](https://orcid.org/0000-0003-3608-0463))
- Allison J Greaney
- Nicholas S Heaton
- Jesse D Bloom ([ORCID: 0000-0003-1267-3408](https://orcid.org/0000-0003-1267-3408))

## Response text

DOI: [10.7554/eLife.86852.2.sa2](https://doi.org/10.7554/eLife.86852.2.sa2)

We thank eLife and the reviewer for the nice summary of our manuscript. We largely agree with the summary and review, and just add a few small points.

First, the review asks about the reproducibility of our findings, and suggests that they are only from a single experiment. In fact, our manuscript reports data from two independent single-cell experiments: one performed at low multiplicity of infection (MOI), and another at higher MOI. The broad trends, including the lack of strong correlations between viral mRNA transcription and progeny production, are consistent across both experiments.

Second, the reviewer asks about what happens when two different virions bearing the same viral barcode infect two different cells, given that we estimate 4-8% of barcodes to be shared between multiple infecting virions. When two cells are infected by different virions with the same barcode, this breaks the one-to-one link between transcription in that cell and progeny in the supernatant, since it is not possible to determine which cell contributed the progeny with that barcode. This means that between 4-8% of the points on our correlation plots could be affected by this factor, meaning that a few outliers should be expected. Another scenario, where a single cell is infected by two barcodes, is not problematic for our method because we can simply sum the progeny output for both barcodes from that cell.

Finally, the reviewer notes that some cells appear to produce progeny virions despite failing to express one or more viral genes. Such cells can be explained in one of two ways. First, as noted immediately above, we expect a small fraction (4-8%) of the points to be erroneous due to a lack of a guaranteed one-to-one link between cell and progeny for non-unique barcodes. Second, in some cases the missing viral gene could be a technical artifact caused by a stochastic failure to capture modestly expressed transcripts from the gene; this phenomenon, known as gene dropout, occurs at a fairly high rate in single-cell experiments (see Qiu Nature Communications 2020 for a detailed discussion). Genes that are expressed at lower levels, like the Influenza virus polymerase genes, are more likely to be missed during single-cell RNA sequencing. The absent viral genes in each infected cell can be explored in detail using the interactive plots at https://jbloomlab.github.io/barcoded_flu_pdmH1N1/
