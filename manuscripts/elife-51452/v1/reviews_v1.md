# Peer review - Round 1

Editors:
- Francois Guillemot, The Francis Crick Institute United Kingdom

Reviewers:
- Sydney Shaffer

## Review text

DOI: [10.7554/eLife.51452.sa1](https://doi.org/10.7554/eLife.51452.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript describes an innovative non-transgenic method called Probe-seq, to purify and transcriptionally profile genetically-defined populations of cells. The protocol involves FACS-sorting cells based upon strong fluorescence signals produced by a new method of fluorescent RNA in situ hybridization. Cells or nuclei collected with this protocol can produce high-quality RNA sequencing data. The method therefore allows deep sequencing of rare cell populations and it compares well to the efficiency of single cell RNA sequencing using the SMART-seq method. The authors show that Probe-Seq can be applied to a variety of tissues from different organisms and to frozen nuclei isolated from archival material. The method described in this paper can therefore have many applications and will be of interest to large numbers of biologists from diverse fields.

Decision letter after peer review:

Thank you for submitting your manuscript "Probe-Seq enables transcriptional profiling of specific cell types from heterogeneous tissue by RNA-based isolation" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Marianne Bronner as Senior Editor and Francois Guillemot as Reviewing Editor. Sydney Shaffer (Reviewer #3) has agreed to reveal his identity. The reviewers have discussed with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript provides an innovative, non-transgenic method to purify genetically defined populations of cells from a variety of tissues in diverse organisms. The reviewers are positive about the manuscript but raise several issues that should be addressed in a revision, including:

1) What is the purity of populations FAC-sorted based on their SABER signal?

2) How much does the SABER procedure affect the quality of RNA?

3) The data presented suggest that 12 tiling oligonucleotides are not sufficient for a confident separation of gene-positive and negative populations for highly expressed genes.

The original reviews are included below.

Reviewer #1:

In this manuscript, Amamoto et al. describe an innovative non-transgenic method, Probe-seq, to purify genetically defined populations of cells. They developed a protocol in which FACS sorting of cells is performed based upon strong fluorescence signals produced by SABER-FISH, a method that allows specific labeling of RNAs. They subsequently demonstrate that cells/nuclei collected under this protocol can produce high-quality RNA sequencing data.

Accordingly, the manuscript shows that Probe-Seq allows deep transcriptome profiling of a rare population of cells and compares well to the efficiency of scRNA using the SMART-seq. Several strengths of this manuscript are notable. First, the isolation of cells via RNA FISH has not been very straightforward, and I find this study a major technical achievement. Second, the authors demonstrate that Probe-Seq can be applied not only to mouse retina, but also to a variety of tissues from different organisms, including human, fly, and chick embryos, as well as nuclear samples. Therefore, this study is likely relevant to a broad biological community. The Materials and methods section of this manuscript is clearly written, and supplementary data provide the necessary information, including DNA sequences, to reproduce their data. Overall, I found the data is well presented and convincing.

One minor weakness of the study is that it's not clear how this method fares with more traditional scRNA-seq given only a few comparisons. Also, while the isolation of even finer cell types using sequential cell sorting is impressive, sequencing data from the sorted population is not presented in this manuscript to support whether this workflow is indeed feasible for RNA-seq. The manuscript will be significantly improved and more impactful if these data can be added.

Reviewer #2:

This methodological paper combines fluorescent in situ hybridization (FISH) and RNA-sequencing for cell sorting and transcriptional analysis of enriched cell populations. The principal advantage of this approach is its versatility, as it can be applied to a variety of tissues and species without the need for transgenesis.

Authors show that the FISH procedure is compatible with the identification of differentially expressed genes in various contexts. Although the approach is interesting, I believe that it would be considerably strengthened by performing a more direct quantification of the consequences of the FISH procedure on RNA quality and subsequent transcriptional analysis. The comparison of the Probe-Seq data with those obtained from freshly dissociated cells following retina electroporation, performed in the first part of the manuscript, is not sufficient. Indeed, cells labelled by the two procedures are not directly comparable, thereby preventing a direct comparison of the transcriptional results. A more direct comparison (i.e. RNA quality/transcriptional differences observed following FAC-sorting, vs. Probe-Seq vs. repeated Probe-Seq) should be performed to validate the approach and demonstrate its full potential.

Please find additional comments below:

- Figure 1 summarizes the procedure workflow as well as main results obtained for the adult mouse retina. It is accompanied by four supplementary figures, some of which containing important information (e.g. Figure 1—figure supplement 3). I would suggest splitting this figure in order to incorporate some of these data within the main body of the manuscript.

- Figures 2 and 3 follow the exact same workflow to demonstrate that the approach can be transposed to frozen post-mortem cells and/or other species. These two figures could be merged, as they essentially convey a similar message.

- Figure 1H and Figure 1—figure supplement 5: although authors conclude that 12 tiling oligonucleotides is sufficient for a confident separation of gene-positive and negative populations, a close look at flow cytometry histograms presented on Figure 1—figure supplement 5 rather suggests that it is insufficient for highly expressed genes (Grik1). Please revise.

- Demonstration of ON BC cell enrichment by GRM6 Probe-Seq is not convincing if one refers to Figure 2E, as markers of ON BC are barely enriched when compared to those of OFF BC cells on the presented heat map.

- Validation of CDH12 as a marker enriched in GRM6-sorted cells is not supported by the in situ hybridization presented in Figure 2F. Indeed, expression of CDH12 can be observed in other cell layers/cell types.

Reviewer #3:

This paper describes a new method for isolating specific cell populations based on gene expression for RNA sequencing. This method uses in situ labeling of specific RNA species using an RNA FISH amplification method called SABER-FISH. The SABER-FISH signal is specific to the gene of interest and sufficiently bright for isolated cells using fluorescently activated cell sorting. They use this strategy to sort their desired cell populations that can then be analyzed by bulk RNA seq to give a more in-depth expression profile of specific types of cells. To show the broad applicability of this method, they apply it on mouse, human, Drosophila, and chick tissue, and they also show that it is compatible with nuclei from frozen tissue as well. Overall, I believe this is a very practical and useful method for getting in depth and high-quality RNA-seq data on a specific population of cells within a tissue. I can imagine many applications and biological questions where this method will be really useful!

1) In general, it would be helpful to know the expected purities from these SABER + FACS protocols. The authors show images after sorting the populations of cells (particularly in Figure 1E), but it would be useful to show more quantification of these sorted cells. What fraction of the sorted cells that are supposed to show a particular marker combination actually have that combination of SABER signal when imaging (the Vsx2+/Grik1- and Vsx2+/Grik1+ samples)? This helps give an idea of how pure these populations are prior to bulk-seq. Do these fractions match what is expected from previous literature/data?

2) It would be helpful to provide some quantification for the data shown in Figure 2F. For example, how many of the GRM6+ cells are also CDH12+ and vice versa? In these images, why does GRM6 have larger (and more irregularly sized) spots than CDH12?

3) Do the authors know why Neto1 (lowest expression) has the best stain index and Grik1 (highest expression) has the worst when using 12 oligos? Is this something systematic about the method or just a particular finding with these genes? How was the cutoff of SI = 2 selected for this analysis? For people who would want to use this method, is SI > 2 what is being recommended?

4) For the majority of FACS plots, the fluorescence of the gene of interest is plotted against autofluorescence. Is this a proxy for cell size or side scatter? Are there any specific advantages to using autofluorescence the readers should know about?
