# Peer review - Round 1

Editors:
- Michael B Eisen, University of California, Berkeley United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.87099.3.sa0](https://doi.org/10.7554/eLife.87099.3.sa0)

This valuable work fills a gap in the mapping of gene expression patterns in the early embryo of C. elegans. The presented data are solid and provides a resource for future analysis.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87099.3.sa1](https://doi.org/10.7554/eLife.87099.3.sa1)

C. elegans is a pre-eminent model for developmental genetics, and its invariant lineage makes it possible in theory to define molecular features such as gene expression comprehensively and at single cell resolution across the organism.

Previously published single-cell RNA-seq studies have mapped gene expression across the lineage through the 16-cell stage (Tintori et al 2017, Hashimshony et al 2016), and at later stages (Packer et al 2019, with good coverage starting at the 100-cell stage and some coverage at the ~50-cell stage). This left the critical period around gastrulation (~28-cell and ~50-cell) without comprehensive transcriptome data. This study covers this gap with a heroic effort involving the manual isolation and analysis of over 800 cells from embryos of known stage, combined with painstaking curation using known markers from small scale studies and larger imaging-based expression atlases. Importantly, the dataset overlaps at early and late stages with data prior studies.

The data quality and overlap with Tintori and Packer datasets both appear high, but to make this inference required additional analysis from Supplemental Table 6 by this reviewer as it is not explored or described in the manuscript. Analyses demonstrating continuity with these datasets would greatly increase the value of the resource.

The authors show that specific lineages and stages preferentially express TFs with different classes of DNA binding domains. This extends previous work implicating homeodomains as preferentially involved in nervous system patterning and as enriched in neural and muscle progenitors in mid-stage embryos.

They also show that C. elegans homologs of Drosophila early embryonic regulators (which function based on spatial position in that system) tend to also be patterned in early C. elegans embryos, but with lineage-specific patterns. This conserved use of regulators would be fairly remarkable given the dramatically different developmental modes in these two species, although this observation is not backed up by quantitative analyses.

Finally, there is an argument that combinations of TFs expressed in lineage-specific patterns give rise to "stripe" patterns. This section is also not based on statistical analyses but suggests the possibility that lineage and positional regulation may be more convoluted than was previously thought.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87099.3.sa2](https://doi.org/10.7554/eLife.87099.3.sa2)

The C. elegans embryo has been model system of study for more than 30 years because of the ease of doing forward and reverse genetics, coupled with its nearly invariant lineage which allows a description of development at high resolution. 4D time lapse imaging coupled with spatially resolved gene expression has enabled identification of transcriptional signatures of cells in space and time, and in the past decade this has been advanced with single-cell transcriptomics methods, using individually isolated embryonic cells (which can retain their identity) or by deconvolving complex mixtures of early cells. Recent work using these methods has resolved spatiotemporal expression patterns for many genes, defining cells up to gastrulation stage, but then changing to more tissue-specific patterns during morphogenesis. A key paradigm of specification in C. elegans and other systems is that early maternal factors initiate or restrict patterns of transcription factor expression from the zygotic genome. Combinatorial expression patterns and some symmetries broken by autonomous or extrinsic cell inductions ultimately program lineages towards their fates. To date, only simple networks have been elucidated, as the increasing complexity of these networks and the high level of redundancy has made functional dissection of such pathways difficult. Hence, almost all of the work in recent years has been descriptive.

In this work the authors fill a knowledge gap from the early embryo (~16 cells) to the ~100-cell stage and describe new patterns of gene expression. They reconcile their findings with that of others who have defined expression patterns using other methods, such as scRNA-Seq from complex mixtures of cells, and from transcription factor expression analyses. The resulting description of embryonic develop is the most precise to date, and offers a potentially useful resource for other researchers.

The authors attempt to use their results to find patterns of gene expression that could hint at phylogenetic conservation of specification mechanisms. They find some supporting evidence that expression of homeobox genes occurs in anterior-posterior stripes, which recalls the elaborate A/P patterning system elucidated in the Drosophila embryo, which belongs to the sister phylum Arthropoda in the Ecdysozoan clade of molting animals. It felt as if the authors chose the Hox genes they need to support this conclusion.

Some caveats exist to the work. The expression patterns seem to be well-validated, and following prior work from the Yanai group are likely to be strongly correlated with expression in living embryos. When cells are separated, they could lose some expression patterns that require cell-cell interactions, so it is expected that there might be a small minority of expression patterns that are more complex than what has been documented here.

A major caveat is the idea of the stripes of Hox expression. I just did not find these arguments to be compelling. Seeing these 'stripes' requires organizing the data in a way that maximizes their appearance, for one. Since there is not a lot of movement of cells away from their birth in the early embryo, the AB descendants are anterior to those of MS, anterior to those of E, anterior to those of C, D, and P4. Lineage-specific expression will just naturally fall into 'stripes'. Second, the conservation of Hox expression patterns typically comes with collinearity of the genes along the length of a chromosome (i.e. the so-called Hox clusters) with expression along the body axis, as well as posterior-to-anterior fate transformations when Hox specification is disrupted.

A minor note is the detection of an enrichment of GATA factors in the early E lineage. This has now been found to be a derived condition even within the genus see Broitman-Maduro et al. Development 149 (21): dev200984, as other species like C. angaria show only a simpler network of elt-3 -> elt-2. This suggests that many of the other patterns of gene expression, particularly in the early embryo, could be highly derived as well; some caution is warranted in generalizing the results as being conserved with arthropods as some of this could be convergent.

Given what the authors are proposing about Hox stripes, some omissions of prior work were surprising (or maybe I missed them). For example, a comprehensive study of Hox genes in C. elegans by Hench et al. (2015) (PLoS One 10(5): e0126947) evaluated all the homeobox genes and examined their genomic locations and expression patterns in the embryo at high spatiotemporal resolution. Work from the Hobert lab (Nature 2020, 584(7822):595-601) showed how homeobox codes specify classes of C. elegans neurons, and the Murray lab (PLoS Genet. 18(5):e1010187) examined Hox control of posterior lineage specification at high resolution, with functional assays.

The Discussion section of the paper is brief, consistent with the descriptive nature of the work overall, but it would have been nice to see the findings related to other published studies as indicated above.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87099.3.sa3](https://doi.org/10.7554/eLife.87099.3.sa3)

The authors claim that this dataset covers a timepoint of embryogenesis that is not well covered in the other published single cell datasets (Tintori et al 2016 and Packer et al 2019). The Tintori data indeed do not cover the 28-102-cell stages sufficiently, but it is unclear how the data presented here compare to the Packer et al data. It is true that the Packer et al data have fewer cells at earlier timepoints than at later ones, but given that they sequenced tens of thousands of cells, they report that they still have ~10,000 cells <210 min of embryogenesis. It seems that if the authors want to make any claims about how their data enables exploration of a stage that was previously not accessible, this would require a better comparison to the available data.

The authors provide thorough support for how they assigned cell identities in their data. It is surprising though that at the 102-cell stage they only identify 37 unique cell identities. They suggest that this is because there are many equivalence groups at this stage. However, I would strongly encourage the authors to perform a similar analysis or otherwise compare their obtained identities with the data from Packer et al. 2019. It seems possible that given the low number of cells in this dataset, the authors are missing certain identities and it would be important to know this.

The main analysis the authors perform is to look at expression patterns of various classes of TFs and ask whether they are enriched in particular lineages or at specific timepoints. This analysis is interesting but would be more informative if the authors provided in Figure 3d the numbers of each class of TFs. The authors then focus on the homeodomain class of TFs as they display interesting lineage-specific expression patterns, which when mapped on the embryo form stripes. The stripe pattern however is not that obvious, at least not as shown in Figure 4b. Perhaps separate embryo schematics showing the different TF expression patterns would show this more clearly. Moreover, given the relatively small number of cell identities found in this dataset (particularly at the 102-cell stage), a similar analysis using the Packer data would provide further support to these patterns. The localization of cells with shared expression patterns does show a stripe pattern at the 28-cell stage, but also not so clearly beyond this timepoint.

I am also unsure about the validity/value of the comparison of the stripes to Drosophila and the centrality of homeodomain TFs to anterior-posterior positional identity. First, it would be important to map other TFs, very likely there are several other TFs that correlate with positional identity. Also, even if the expression of the homeodomain TFs in C. elegans form stripes, there are still several cells within that stripe that do not express these TFs, it is thus unclear whether these TFs encode positional information or the identity of cells with different positions in the embryo.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87099.3.sa4](https://doi.org/10.7554/eLife.87099.3.sa4)

This is an admirable piece of work. The authors build on a previous dataset they assembled, but expand it to include all stages of early development in the nematode Caenorhabditis elegans. Cell collection was done manually, which is very impressive, and is clearly far better than pooled unidentified cells. I will not comment on the specific sequencing and analysis, since this is not my expertise, but will comment on the general conclusions and comparative framework in which the authors place their results.

While the Introduction and Discussion sections are actually fairly short, much of the presentation of the results is based on a certain comparative framework, which is explicitly a comparison between C. elegans and Drosophila melanogaster. This is an important perspective, but I feel the authors' interpretation is in some places exaggerated and in other places almost trivial.

Drosophila and C. elegans are two of the main models for developmental biology. However, it has been clear for over two decades that both species are highly derived and specialized and therefore, treating them as representative for their taxa is problematic. Much of the authors' discussion hinges on the question of comparing syncytial and lineage-dependent development. The syncytial early development of Drosophila is very specific and is clearly a recent innovation within a restricted group of flies. The canonical Drosophila segmentation cascade is mostly a novelty and most elements within the cascade are recent. Specifically, the expression of gap genes in regional stripes is not found very broadly. Conversely, the polarizing role of Caudal is very ancient and is probably found in all Bilateria. When making comparisons with a distantly related species, it is important to keep this in mind. Not as much is known about development of other nematodes, but the little that is known indicates that C. elegans is also unusual, and specifically the eutelic development (conserved cell lineages in development) is not found in all nematodes.

The authors suggest that regional expression of transcription factors in stripes is a conserved characteristic of development. This is true for Hox genes and has been known for decades. The regional expression they show for other genes is not convincing as "stripes". It is no surprise that developmental transcription factors are regionalized, but linking this to the stripes of Drosophila gap genes and even more so to Drosophila pair-rule and segment-polarity genes is a bit far-fetched. Yes, many genes are expressed in restricted domains along the A-P axis, but that is all that can be said based on the data. Calling them "Drosophila-like" is unfounded.
