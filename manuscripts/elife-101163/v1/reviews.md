# Peer review - Round 1

Editors:
- Genevieve Konopka, University of Texas Southwestern Medical Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.101163.3.sa0](https://doi.org/10.7554/eLife.101163.3.sa0)

This study presents a valuable conceptual approach that cell lineage can be determined using methylation data. However, the evidence supporting the claims of the author remains incomplete after revision. If clarified further as described in the reviews, this approach could be of broad interest to neuroscientists and developmental biologists.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.101163.3.sa1](https://doi.org/10.7554/eLife.101163.3.sa1)

Summary:

In this manuscript, Shibata describes a method to assess rapidly fluctuating CpG sites (fCpGs) from single-cell methylation sequencing (sc-MeSeq) data. Assuming that fCpGs are largely consistent over time with changes induced by inheritable events during replication, the author infers lineage relationships in available brain-derived sc-MeSeq. Supplementing current lineage tracing through genomic and mitochondrial mosaic variants is an interesting concept that could supplement current work or allow additional lineage analysis in existing data.

However, the author failed to convincingly show the power of fCpG analysis to determine lineages in the human brain. While the correlation with cellular division and distinction of cell types appears plausible and strong, the application to detect specific lineages is less convincing. Aspects of this might be due to a lack of clarity in presentation and erroneous use of developmental concepts. However, without addressing these problems it is challenging for a reader to come to the same conclusions as the author.

On the flip side, this novel application of fCpGs will allow the re-use of existing sc-MeSeq to infer additional features that were previously unavailable, once the biological relevance has been further elucidated.

Strengths:

• Novel re-analysis application of methylation data to infer the status of fCpGs and the use as a lineage marker

• Application of this method to an innovative existing data set to benchmark this framework against existing developmental knowledge

Weaknesses:

• Inconsistent or erroneous use of neurodevelopmental concepts which hinders appropriate interpretation of the results.

• Somewhat confusing presentation at times which makes it hard to judge the value of this novel approach.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.101163.3.sa2](https://doi.org/10.7554/eLife.101163.3.sa2)

Summary:

Cell lineage tracing necessitates continuous visible tracking or permanent molecular markers that daughter cells inherit from their progenitors. To successfully trace cell lineages, it is essential to generate and detect sufficient new markers during each cell division. Thus, molecular cell lineages have been predominantly studied with stably inherited genetic markers in animal models and somatic DNA mutations in the human brain. DNA methylation is unstable across cell divisions and differentiation, and is hardly called barcodes. The use of "Human Brain Barcodes" in the title and across the whole paper lacks convincing evidence - it is questionable that CpG methylation is always stably inherited by daughter cells.

Strengths:

Analysis of DNA methylation.

Weaknesses:

The unstable nature of CpG methylation would introduce significant problems in inferring the true cell lineage. To establish DNA methylation as a means for lineage tracing, it is necessary to test whether the DNA methylation patterns can faithfully track cell lineages with in vitro differentiated & visibly tracked cell lineages.

The unreliable CpG methylation status also raises the question of what the "Barcodes" refer to in the title and across this study. Barcodes should be stable in principle and not dynamic across cell generations, as defined in the Reference #1. The CRISPR/Cas9 mutable barcodes or the somatic mutations may be considered barcodes, but the reviewer is not convinced that the "dynamic" CpG methylation fits the "barcodes" terminology. This problem is even more concerning in the last section of the results, where CpG status fluctuates in post-mitotic cells.

The manuscript frequently states assumptions in a tone of conclusions and interprets results without rejecting alternative hypotheses. For example, the title "Human Brain Barcodes" should be backed with solid supporting evidence. For another example, the author assumed that the early-formed brain stem would resemble progenitors better and have a higher average methylation level than the forebrain - however, this difference in DNA methylation status could well reflect cell-type-specific gene expression instead of cell lineage progression.

Other points:

(1) The conclusion that excitatory neurons undergo tangential migration is unclear - how far away did the author mean for the tangential direction? Lateral dispersion is known, but it is hard to believe that the excitatory neurons travel across different brain regions. More importantly, how would the author interpret shared or divergent methylation for the same cell type across different brain regions?

(2) The sparsity and resolution of the single-cell DNA methylation data. The methylation status is detected in only a small fraction (~500/31,000 = 1.6%) of fCpGs per cell, with only 48 common sites identified between cell pairs. Given that the human genome contains over 28 million CpG sites, it is important to evaluate whether these fCpGs are truly representative.

(3) While focusing on the X-chromosome may simplify the identification of polymorphic fCpGs, the confidence in determining its methylation status (0 or 1) is questionable when a CpG site is covered by only one read.
