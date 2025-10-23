# Peer review - Round 1

Editors:
- Deborah Bourc'his, Institut Curie France

Reviewers:
- Soeren Lukassen, Charité Germany

## Review text

DOI: [10.7554/eLife.43966.040](https://doi.org/10.7554/eLife.43966.040)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Unified single-cell analysis of testis gene regulation and pathology in 5 mouse strains" for consideration by eLife. Your article has been reviewed by Patricia Wittkopp as the Senior Editor, a Reviewing Editor, and two reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Soeren Lukassen (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this paper, the authors perform scRNA-seq in mouse testis to delineate the cellularity of this complex organ. What distinguishes this work from other recently published scRNA-seq experiments in testis is that the application of a recently developed statistical framework method, SDA, to decompose single-cell RNA-seq expression matrices into biologically meaningful modules. Using large datasets of wild-type and mutant mouse testis scRNA-seq samples, this method allowed soft clustering, imputation of missing expression values, and gene regulatory network analysis. The standard of reporting here is high, with the authors doing a commendable job of making an interface to their data and their analytic code available to reviewers.

Essential revisions:

All reviewers agreed regarding the interest of applying an SDA-type analysis to scRNA-seq data – in particular when comparing wild-type and mutant samples – and its wider potential for the field sc-omics in general.

However, as you will see, there were also an important number of concerns, some of them major, that need to be imperatively addressed in a revised version. Notably, you are asked to make efforts for additional benchmarking, to better place your approach in the context of other methods; to provide better explanation to guide the readers of not-yet-described analyses; to provide relevant references to support statements; fix an important number of errors or omissions; and clarify the observed cellular phenotypes.

See the requests for amendments below.

Reviewer #1:

In this paper, the authors perform scRNA-seq in mouse testis to better understand the cellularity of this important and complex organ. What sets this work apart from several recently published scRNA-seq experiments in testis is that the authors demonstrate the power of applying a recently developed statistical framework (SDA) to scRNA-seq data. It is noteworthy that the standard of reporting here is top-notch, with the authors doing a commendable job of making an interface to their data and their analytic code available to reviewers.

This paper reads like two papers studying the same data; the first, a "classical" scRNA-seq analysis, the second, a complete, and methodologically novel reanalysis of the data using SDA. Aside from a single paragraph near the end, there are few, if any cross-references between these apparently independent studies. The latter half is an intriguing demonstration of the power of novel statistical framework to study scRNA-seq data from a complex tissue. The first half, however, is peppered with inconsistencies (outlined in specific comments below). In addition, although I understand the need to distil complex analyses into straightforward axis labels, in this first part, the authors have done so at the expense of necessary detail. For most figures, the axis labels require far more detail and/or explanation in the legend. In performing this review, far too much guesswork was required. Overall, my simplest recommendation to the authors is to greatly reduce or eliminate the "classical" scRNA-seq analyses, and instead focus on improving the latter half of this rather long paper for publication.

For both parts of the paper, my major concern stems from the authors' decision to perform a joint analysis of wild-type and mutants together. For the "classical" scRNA-seq analysis, I am not convinced that the decision to do so is justified. The contribution of mutants to patterns of clustering is not convincingly explored, indeed, in the only figure provided where this can be evaluated (currently Supplementary Figure 2B), it appears that a specific mutant phenotype may be responsible for half of the defined clusters! In the second part of the paper, the joint analysis is potentially less of a concern because SDA, in theory, should facilitate a natural delineation of cell-types that are not found in wild-type. Nonetheless, it also presents some issues that are not addressed; in particular, that the vast majority of somatic and "early" meiotic cells in their analyses appear to come from genetic mutants. I understand the reasons for this, however; (1) presenting this caveat to the reader comes very late in the paper, despite being important for multiple earlier analyses; (2) the authors never explicitly broach this topic and highlight to the reader that very few such cells are derived from wild-type animals; and (3) the authors do not convincingly demonstrate that the wild type SDA components are faithfully recapitulated in the joint analysis. These issues should be far more carefully explained and dealt with by the authors.

Finally, the authors have admirably compiled this huge dataset into a semi-digestible paper, but there are numerous instances where an understanding of not-yet-described analyses are required to explain the data (i.e. the interpretation of Figure 5 is aided by understanding Figure 6). Extensive work to linearize the manuscript and eliminate such forward-references would greatly aid legibility.

Reviewer #2:

In their manuscript, the authors describe a method to decompose single-cell RNA-seq expression matrices into biologically meaningful modules, and apply this method to a large dataset of wild type and mutant mouse testis scRNA-seq. Their method allows for soft clustering, imputation of missing expression values, and gene regulatory network analysis.

The authors describe an exciting analysis technique applied to a good quality dataset. The expression data will be of interest to scientists in the area of testis biology. The analysis method described is highly relevant in the entire field of single-cell omics, especially but not exclusively where differentiating tissues are the focus.

The biological interpretation of the results is largely sound and both SDA and its results are convincing. As a method-focused manuscript, additional benchmarking and comparison to other, similar tools is needed.

Major comments:

Figure 1C: The plot presents a higher transcript than gene count for many cells, which is impossible.

Figure 3D: Most of the gene loadings seem to be non-zero. This conflicts the sparsity claims made before (e.g. Figure 3B).

Subsection “Identification of gene modules using SDA”: For 2D matrices, other (NMF) implementations such as NNLM use L1 regularization (Kim and Park 2007), which should perform better at shrinking coefficients to zero than SDA, judging from Figure 3D. Furthermore, least-squares based methods should theoretically have a lower complexity than KL-based ones, so approximate resource usage values (CPU core hours and memory usage, running time on a reference machine) should be mentioned. Several papers have been published where NMF was used for the analysis of scRNA-seq data and should be discussed (Shao and Höfer, 2017; Zhu et al., 2017; Duren et al., 2018).

Subsection “Identification of gene modules using SDA”: The data presented for wild type components seems to stem from the joint analysis instead (identical component numbers, tSNE…). This should be clarified.

Figure 6F: The curve for Cul4a indicates an accumulation of later stages rather than a pachytene block, possibly a defect in late spermiogenesis. This contrasts previous literature (Yin et al., 2011, histology in Kupanja et al., 2011) and should be discussed.

Subsection “Joint analysis of 5 mouse strains identifies pathology-related components”: This pseudotime mapping could be seriously hampered by dissociation bias. A more finely grained analysis using shorter time periods should be compared to the one presented (for timing of tubule stages see Oakberg, 1956).

Subsection “Joint analysis of 5 mouse strains identifies pathology-related components”: The absence of giant cells could be explained by a lower rate of encapsulation. A microscopic image of an emulsion with cells stained with SiR-DNA and CellTracker or similar dyes would prove that multinucleate giant cells can be encapsulated. Furthermore, the cell suspension should be imaged before encapsulation to verify the presence of giant cells after cell straining.

General comment: In addition to matrix factorization, other techniques, such as autoencoders (DCA) and self-organizing maps (Scrat) have been used to extract features that go beyond plain PCA. In the case of autoencoders, they are also useful when applied to imputation tasks. Similarly, the motif analysis presented here is conceptually different from, but may yield similar results, as SCENIC. The performance and results of SDA in a scRNA-seq context should briefly be compared to these tools (resource usage, components/regulons on tSNE or heatmap as figure/supplementary figure).
