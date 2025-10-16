# Peer review - Round 1

Editors:
- Nicholas E Banovich, Translational Genomics Research Institute United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.96852.3.sa0](https://doi.org/10.7554/eLife.96852.3.sa0)

This is a solid study that follows a well-established canvas for variant-to-gene prioritization using 3D genomics, applying it to activated T cells. The authors go some way in validating the lists of candidate genes, as well as exploring the regulatory architecture of a candidate GWAS locus. Jointly with data from previous studies performing variant-to-gene assignment in activated CD4 T cells (and other immune cells), this work provides a useful additional resource for interpreting autoimmune disease-associated genetic variation.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.96852.3.sa1](https://doi.org/10.7554/eLife.96852.3.sa1)

Summary:

The authors profile gene expression, chromatin accessibility and chromosomal architecture (by Hi-C) in activated CD4 T cells and use this information to link non-coding variants associated with autoimmune diseases with putative target genes. They find over a 1000 genes physically linked with autoimmune disease loci in these cells, many of which are upregulated upon T cell activation. Focusing on IL2, they dissect the regulatory architecture of this locus, including the allelic effects of GWAS variants. They also intersect their variant-to-gene lists with data from CRISPR screens for genes involved in CD4 T cell activation and expression of inflammatory genes, finding enrichments for regulators. Finally, they showed that pharmacological inhibition of some of these genes impacts T cell activation.

This is a solid study that follows a well-established canvas for variant-to-gene prioritisation using 3D genomics, applying it to activated T cells. The authors go some way in validating the lists of candidate genes, as well as explore the regulatory architecture of a candidate GWAS locus. Jointly with data from previous studies performing variant-to-gene assignment in activated CD4 T cells (and other immune cells), this work provides a useful additional resource for interpreting autoimmune disease-associated genetic variation.

Autoimmune disease variants were already linked with genes in CD28-stimulated CD4 T cells using chromosome conformation capture, specifically Promoter CHi-C and the COGS pipeline (Javierre et al., Cell 2016; Burren et al., Genome Biol 2017; Yang et al., Nat Comms 2020). The authors cite these papers and present a comparative analysis of their variant-to-gene assignments (in addition to scRNA-seq eQTL-based assignments). Furthermore, they find that the Burren analysis yields a higher enrichment for gold standard genes.

I thank the authors for their revisions in response to my initial review. The revised version now includes a more comprehensive comparative analysis of different datasets and V2G approaches and discusses the potential sources of differences in the results. Most significantly, the authors have now included an interesting comparison of their methodology with the popular ABC technique and outlined the key limitations of ABC relative to their method and other (Capture) Hi-C-based V2G approaches.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.96852.3.sa2](https://doi.org/10.7554/eLife.96852.3.sa2)

Summary:

There is significant interest in characterizing the mechanisms by which genetic mutations linked to autoimmunity perturb immune processes. Pahl et al. collect information of dynamic accessible regions, genes, and 3D contacts in primary CD4+ T cell samples that have been stimulated ex vivo. The study includes a variety of analyses characterizing these dynamic changes. With TF footprinting they propose factors linked to active regulatory elements. They compare the performance of their variant mapping pipeline that uses their data versus existing datasets. Most compelling there was a deep dive into additional study of regulatory elements nearby the IL2 gene. Finally, they perform a pharmacological screen targeting several genes they suggest are involved in T cell proliferation.

Strengths:

- The work done characterizing elements at the IL2 locus is impressive.

Weaknesses:

- There are extensive studies performed on resting and activated immune cell states (CD4+ T cells and other cell types) and some at multiple time points or concentrations of stimuli that collect ATAC-seq and/or RNA-seq. Several analyses performed in published studies were similarly performed in this study. I expected the authors to at least briefly mention published studies and whether their conclusions generally agree or disagree. Are the same dynamic regulatory regions or genes identified upon T cell activation? Are the same TF footprints enriched in these dynamic regulatory elements? In the revision, I appreciate that the authors now include additional data from several studies that I had initially suggested for the purposes of nominating disease genes in their precision-recall analysis.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.96852.3.sa3](https://doi.org/10.7554/eLife.96852.3.sa3)

Summary:

This paper used RNAseq, ATACseq, and Hi-C to assess gene expression, chromatin accessibility, and chromatin physical associations for native CD4+ T cells as they respond to stimulation through TCR and CD28. With these data in hand, the author identified 423 GWAS signals to their respective target genes, where most of these were not in the proximal promoter, but rather distal enhancers. The IL-2 gene was used as an example to identify new distal cis regulatory regions required for optimal IL-2 gene transcription. These distal elements interact with the proximal IL2 promoter region. When the distal enhancer contained an autoimmune SNP, it affected IL-2 gene transcription. The authors also identified genetic risk variants that were associated to genes upon activation. Some of these regulate proliferation and cytokine production, but others were novel.

Strengths:

This paper provides a wealth of data related to gene expression after CD4 T cells are activated through the TCR and CD28. An important strength of this paper is that these data were intensively analyzed to uncover autoimmune disease SNPs in cis acting regions. Many of these could be assigned to likely target genes even though they often are in distal enhancers. These findings help to provide a better understanding concerning the mechanism by which GWAS risk elements impact gene expression.

Another strength to this study was the proof-of-principle studies examining the IL-2 gene. Not only were new cis acting enhancers discovered, but they were functionally shown to be important in regulating IL-2 expression, including susceptibility to colitis. Their importance was also established with respect to such distal enhancers harboring disease relevant SNPs, which were shown to affect IL-2 transcription.

The data from this study were also mined against past Crispr screens that identified genes that control aspects of CD4 T cell activation. From these comparisons, novel genes were identified that function during T cell activation.

Weaknesses:

A weakness from this study is that few individuals were analyzed, i.e., RNAseq and ATACseq (n = 3) and HiC (n = 2). Thus, the authors may have underestimated potentially relevant risk associations by their chromatin capture-based methodology. This might account for low overlap of their data with the eQTL-based approach or the HIEI truth set.

The authors explain that the low overlap is not due to few GWAS associations by HiC. The expanded discussion in the revised manuscript provides a framework to help explain inherent differences between these methods that may contribute to the low overlap.

Impact:

This study indicates that defining distal chromatin interacting regions help to identify distal genetic elements, including relevant variants, that contribute to gene activation.
