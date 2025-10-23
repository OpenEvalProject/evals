# Peer review - Round 1

Editors:
- Sonia Q Sen, Tata Institute for Genetics and Society India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.88334.3.sa0](https://doi.org/10.7554/eLife.88334.3.sa0)

This useful study presents a genetically encoded barcoding system that could advance transcriptomic studies and that has the potential for further applications, such as in high-throughput population-scale behavioral measurements. The evidence supporting the claims of the authors is solid and highlights both the usefulness and the limitations of the approach.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88334.3.sa1](https://doi.org/10.7554/eLife.88334.3.sa1)

The aim of this paper is to describe a novel method for genetic labelling of animals or cell populations, using a system of DNA/RNA barcodes.

Strengths:

• The author's attempt at providing a straightforward method for multiplexing Drosophila samples prior to scRNA-seq is commendable. The perspective of being able to load multiple samples on a 10X Chromium without antibody labelling is appealing.

• The authors are generally honest about potential issues in their method, and areas that would benefit from future improvement.

• The article reads well. Graphs and figures are clear and easy to understand.

Weaknesses:

• The usefulness of TaG-EM for phototaxis, egg laying or fecundity experiments is questionable. The behaviours presented here are all easily quantifiable, either manually or using automated image-based quantification, even when they include a relatively large number of groups and replicates. Despite their claims (e.g., L311-313), the authors do not present any real evidence about the cost- or time-effectiveness of their method in comparison to existing quantification methods.

• Behavioural assays presented in this article have clear outcomes, with large effect sizes, and therefore do not really challenge the efficiency of TaG-EM. By showing a T-maze in Fig 1B, the authors suggest that their method could be used to quantify more complex behaviours. Not exploring this possibility in this manuscript seems like a missed opportunity.

• Experiments in Figs S3 and S6 suggest that some tags have a detrimental effect on certain behaviours or on GFP expression. Whereas the authors rightly acknowledge these issues, they do not investigate their causes. Unfortunately, this question the overall suitability of TaG-EM, as other barcodes may also affect certain aspects of the animal's physiology or behaviour. Revising barcode design will be crucial to make sure that sequences with potential regulatory function are excluded.

• For their single-cell experiments, the authors have used the 10X Genomics method, which relies on sequencing just a short segment of each transcript (usually 50-250bp - unknown for this study as read length information was not provided) to enable its identification, with the matching paired-end read providing cell barcode and UMI information (Macosko et al., 2015). With average fragment length after tagmentation usually ranging from 300-700bp, a large number of GFP reads will likely not include the 14bp TaG-EM barcode. When a given cell barcode is not associated with any TaG-EM barcode, then demultiplexing is impossible. This is a major problem, which is particularly visible in Figs 5 and S13. In 5F, BC4 is only detected in a couple of dozen cells, even though the Jon99Ciii marker of enterocytes is present in a much larger population (Fig 5C). Therefore, in this particular case, TaG-EM fails to detect most of the GFP-expressing cells. Similarly, in S13, most cells should express one of the four barcodes, however many of them (maybe up to half - this should be quantified) do not. Therefore, the claim (L277-278) that "the pan-midgut driver were broadly distributed across the cell clusters" is misleading. Moreover, the hypothesis that "low expressing driver lines may result in particularly sparse labelling" (L331-333) is at least partially wrong, as Fig S13 shows that the same Gal4 driver can lead to very different levels of barcode coverage.

• Comparisons between TaG-EM and other, simpler methods for labelling individual cell populations are missing. For example, how would TaG-EM compare with expression of different fluorescent reporters, or a strategy based on the brainbow/flybow principle?

• FACS data is missing throughout the paper. The authors should include data from their comparative flow cytometry experiment of TaG-EM cells with or without additional hexameric GFP, as well as FSC/SSC and fluorescence scatter plots for the FACS steps that they performed prior to scRNA-seq, at least in supplementary figures.

• The authors should show the whole data described in L229, including the cluster that they chose to delete. At least, they should provide more information about how many cells were removed. In any case, the fact that their data still contains a large number of debris and dead cells despite sorting out PI negative cells with FACS and filtering low abundance barcodes with Cellranger is concerning.

Overall, although a method for genetic tagging cell populations prior to multiplexing in single-cell experiments would be extremely useful, the method presented here is inadequate. However, despite all the weaknesses listed above, the idea of barcodes expressed specifically in cells of interest deserves more consideration. If the authors manage to improve their design to resolve the major issues and demonstrate the benefits of their method more clearly, then TaG-EM could become an interesting option for certain applications.

Comments on revisions:

The authors have addressed many important points, providing reassurances about the initial weaknesses of their work. Although the TaG-EM is unlikely to have a significant influence on the field due to its limited benefits, the results are now sound and provide the reader with an unbiased view of the possibilities and limitations of the method.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88334.3.sa2](https://doi.org/10.7554/eLife.88334.3.sa2)

The authors developed the TaG-EM system to address challenges in multiplexing Drosophila samples for behavioral and transcriptomic studies. This system integrates DNA barcodes upstream of the polyadenylation site in a UAS-GFP construct, enabling pooled behavioral measurements and cell type tracking in scRNA-seq experiments. The revised manuscript expands on the utility of TaG-EM by demonstrating its application to complex assays, such as larval gut motility, and provides a refined analysis of its limitations and cost-effectiveness.

Strengths

(1) Novelty and Scope: The study demonstrates the potential for TaG-EM to streamline multiplexing in both behavioral and transcriptomic contexts. The additional application to labor-intensive larval gut motility assays highlights its scalability and practical utility.

(2) Data Quality and Clarity: Figures and supplemental data are mostly clear and significantly enhanced in the revised manuscript. The addition of Supplemental Figures 18-21 addresses initial concerns about scRNA-seq data and driver characterization.

(3) Cost-Effectiveness Analysis: New analyses of labor and cost savings (e.g., Supplemental Figure 8) provide a practical perspective.

(4) Improvements in Barcode Detection and Analysis: Enhanced enrichment protocols (Supplemental Figures 18-19) demonstrate progress in addressing limitations of barcode detection and increase the detection rate of labeled cells.

Weaknesses

(1) Barcode Detection Efficiency: While improvements are noted, the low barcode detection rate (~37% in optimized conditions) limits the method's scalability in some applications, such as single-cell sequencing experiments with complex cell populations.

(2) Sparse Labeling: Sparse labeling of cell populations, particularly in scRNA-seq assays, remains a concern. Variability in driver strength and regional expression introduces inconsistencies in labeling density.

(3) Behavioral Applications: The utility of TaG-EM in quantifying more complex behaviors remains underexplored, limiting the generalizability of the method beyond simpler assays like phototaxis and oviposition.

(4) Driver Line Characterization: While improvements in driver line characterization were made, variability in expression patterns and sparse labeling emphasize the need for further refinement of constructs and systematic backcrossing to standardize the genetic background.
