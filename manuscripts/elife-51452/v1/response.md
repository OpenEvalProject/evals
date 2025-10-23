# Author response - Round 1

Authors:
- Ryoji Amamoto ([ORCID: 0000-0002-9335-112X](https://orcid.org/0000-0002-9335-112X))
- Mauricio D Garcia
- Emma R West
- Jiho Choi
- Sylvain W Lapan
- Elizabeth A Lane
- Norbert Perrimon ([ORCID: 0000-0001-7542-472X](https://orcid.org/0000-0001-7542-472X))
- Constance L Cepko ([ORCID: 0000-0002-9945-6387](https://orcid.org/0000-0002-9945-6387))

## Response text

DOI: [10.7554/eLife.51452.sa2](https://doi.org/10.7554/eLife.51452.sa2)

Summary:

This manuscript provides an innovative, non-transgenic method to purify genetically defined populations of cells from a variety of tissues in diverse organisms. The reviewers are positive about the manuscript but raise several issues that should be addressed in a revision, including:

1) What is the purity of populations FAC-sorted based on their SABER signal?

To determine the purity of populations FAC-sorted based on their SABER signal, we placed them on a microscope slide after FACS isolation. We then quantified the percentage of cells that had Vsx2 puncta. This analysis showed 92.3 ± 0.6% purity based on three individual sorts. In the text, we have added, “To determine the purity of populations isolated using FACS, based on their SABER signal, the cells were placed on a microscope slide after FACS, and the percentage of cells that had Vsx2 puncta was quantified. This analysis showed 92.3 ± 0.6% had Vsx2 puncta, based on three individual sorts.”

2) How much does the SABER procedure affect the quality of RNA?

To answer this question, we measured the 3’ bias using the Qualimap software. Measurement of 3’ bias is a more reliable method to assess RNA quality, relative to the RNA Integrity Number (RIN). The RIN method measures RNA quality based only on ribosomal RNA, while the 3’ bias method takes into account the 10,000 most highly expressed genes. We used 100,000 cells from the Grik1-Live cell population (FACS isolated and RNA extracted by Trizol) and 100,000 cells from the Grik1-Probe-Seq population. The cell composition and number were nearly identical in these two populations. As expected, the gene body coverage of the Live cell population showed no 3’ bias, suggesting little to no RNA degradation. In comparison, the Probe-Seq gene body coverage showed 3’ bias, likely corresponding to a RIN score of 4-6 (Figure 1—figure supplement 4). In the Results section, we added, “To measure the RNA quality of the Live cells and Probe-Seq cells, 100,000 GFP- Live cells (n=3) and 100,000 Grik1- Probe-Seq cells (n=3) were collected. Based on the gene body coverage of the 10,000 most highly expressed genes, a slightly higher 3’-5’ bias was observed for the RNA originating in the Probe-Seq population (1.02 ± 0.02) compared to the Live cell population (0.90 ± 0.01), indicating mild degradation of RNA with the Probe-Seq protocol. Based on the gene body coverage graph, the level of degradation for the Probe-Seq population would project to a RIN score of approximately 4-6(Sigurgeirsson, Emanuelsson and Lundeberg, 2014) (Figure 1—figure supplement 4).”

3) The data presented suggest that 12 tiling oligonucleotides are not sufficient for a confident separation of gene-positive and negative populations for highly expressed genes.

We agree that the gene-positive events using 12 tiling oligonucleotides were difficult to separate from the gene-negative events when using a histogram. Therefore, we added a new figure panel (Figure 1—figure supplement 5D) showing the 2-dimensional flow cytometry plots which more clearly show the separation between negative and positive populations. In the text, we added, “However, with an SI cutoff of 2, 12 oligos were sufficient for confidence in the separation of gene-positive and negative populations. This was evident only when the events were displayed in a 2-dimensional flow cytometry plot (Figure 1—figure supplement 5).”

The original reviews are included below.

In addition to the necessary revisions above, we chose to address the following concerns from the individual reviews as we believe that these changes further improve the manuscript.

Reviewer #2:

[…] - Validation of CDH12 as a marker enriched in GRM6-sorted cells is not supported by the in situ hybridization presented in Figure 2F. Indeed, expression of CDH12 can be observed in other cell layers/cell types.

The strong fluorescence was detected in the Outer Plexiform Layer, which we believe is due to autofluorescence, as the signals were not punctate. We have added an asterisk in the figure to indicate this.

Reviewer #3:

[…] 3) Do the authors know why Neto1 (lowest expression) has the best stain index and Grik1 (highest expression) has the worst when using 12 oligos? Is this something systematic about the method or just a particular finding with these genes? How was the cutoff of SI = 2 selected for this analysis? For people who would want to use this method, is SI > 2 what is being recommended?

It is unclear to us why Neto1, which had the lowest expression of the three genes tested, gave the highest staining index with 12 oligos. We suspect that this is a particular finding with these genes, suggesting that the staining index is not always linearly correlated with the number of tiling oligonucleotides. It is also possible that if we picked 12 different oligonucleotides (out of 48), then the staining index could differ. SI = 2 cutoff was determined empirically as we were able to see a distinct population with SI = 2.4. However, with such a low staining index, we were only able to see a clear separation between negative and positive populations using a 2D plot instead of a histogram (Figure 1—figure supplement 5).

4) For the majority of FACS plots, the fluorescence of the gene of interest is plotted against autofluorescence. Is this a proxy for cell size or side scatter? Are there any specific advantages to using autofluorescence the readers should know about?

We added the following to Materials and methods, “The empty channel was used to determine autofluorescence, and the events that displayed high intensity for both the channel of interest and the empty channel were deemed negative as they may be events with high autofluorescence in all channels.”

Additional Changes:

We have also re-analyzed the Drosophila Probe-Seq dataset using an updated single cell RNA sequencing dataset (Hung et al., 2019) that now includes significantly more cells. However, the conclusion remains the same as the previous analysis.
