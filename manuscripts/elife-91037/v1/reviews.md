# Peer review - Round 1

Editors:
- Shimon Sakaguchi, Osaka University Japan

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.91037.3.sa0](https://doi.org/10.7554/eLife.91037.3.sa0)

This important study shows, based on analyses of single-cell RNA-seq data sets of thymus cells, that transposable elements (TEs) are broadly expressed in thymic stromal cells, especially in medullary thymic epithelial cells and plasamacytoid dendritic cells. The authors also show that at least some TE-derived peptides are presented by MHC-I molecules in the thymus. The study provides solid findings supporting a role of TEs in thymic T-cell selection and immune self-tolerance.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91037.3.sa1](https://doi.org/10.7554/eLife.91037.3.sa1)

Summary:

Transposable Elements (TEs) are exogenously acquired DNA regions that have played important roles in the evolutional acquisition of various biological functions. TEs may have been important in the evolution of the immune system, but their role in thymocytes has not been fully clarified.

Using the human thymus scRNA dataset, the authors suggest the existence of cell type-specific TE functions in the thymus. In particular, it is interesting to show that there is a unique pattern in the type and expression level of TEs in thymic antigen-presenting cells, such as mTECs and pDCs, and that they are associated with transcription factor activities. Furthermore, the authors suggested that TEs may be non-redundantly regulated in expression by Aire, Fezf2, and Chd4, and that some TE-derived products are translated and present as proteins in thymic antigen-presenting cells. These findings provide important insights into the evolution of the acquired immune system and the process by which the thymus acquires its function as a primary lymphoid tissue.

Strengths:

(1) By performing single-cell level analysis using scRNA-seq datasets, the authors extracted essential information on heterogeneity within the cell population. It is noteworthy that this revealed the diversity of expression not only of known autoantigens but also of TEs in thymic antigen-presenting cells.

(2) The attempt to use mass spectrometry to confirm the existence of TE-derived peptides is worthwhile, even if the authors did not obtain data on as many transcripts as expected.

(3) The use of public data sets and the clearly stated methods of analysis improved the transparency of the results.

Weaknesses:

(1) The authors sometimes made overstatements largely due to the lack or shortage of experimental evidence.

For example in Figure 4, the authors concluded that thymic pDCs produced higher copies of TE-derived RNAs to support the constitutive expression of type-I interferons in thymic pDCs, unlike peripheral pDCs. However, the data was showing only the correlation between the distinct TE expression pattern in pDCs and the abundance of dsRNAs. We are compelled to say that the evidence is totally too weak to mention the function of TEs in the production of interferon. Even if pDCs express a distinct type and amount of TE-derived transcripts, it may be a negligible amount compared to the total cellular RNAs. How many TE-derived RNAs potentially form the dsRNAs? Are they over-expressed in pDCs?

The data interpretation requires more caution to connect the distinct results of transcriptome data to the biological significance.

We contend that our manuscript combines the attributes of a research article (novel concepts) and a resource article (datasets of TEs implicated in various aspects of thymus function). The critical strength of our work is that it opens entirely novel research perspectives. We are unaware of previous studies on the role of TEs in the human thymus. The drawback is that, as with all novel multi-omic systems biology studies, our work provides a roadmap for a multitude of future mechanistic studies that could not be realized at this stage. Indeed, we performed wet lab experiments to validate some but not all conclusions: (i) presentation of TE-derived MAPs by TECs and (ii) formation of dsRNAs in thymic pDCs. In response to Reviewer #1, we performed supplementary analyses to increase the robustness of our conclusions. Also, we indicated when conclusions relied strictly on correlative evidence and clarified the hypotheses drawn from our observations. Regarding the Reviewer's questions about TE-derived dsRNAs, LINE, LTR, and SINE elements all have the potential to generate dsRNAs, given their highly repetitive nature and bi-directional transcription (1). As ~32% of TE subfamilies are overexpressed in pDCs, we hypothesized that these TE sequences might form dsRNA structures in these cells. To address the Reviewer's concerns regarding the amount of TE-derived RNAs among total cellular RNAs, we also computed the percentage of reads assigned to TEs in the different subsets of thymic APCs (see Reviewer 1 comment #4).

------

I appreciate the authors' efforts to improve the quality of this valuable paper. The additional data proposed by the authors enhanced the possibility that the non-negligible amount of RNAs in pDCs is derived from TE elements. Their biological roles and significance will be demonstrated in future research.

(2) Lack of generality of specific examples. This manuscript discusses the whole genomic picture of TE expression. In addition, one good way is to focus on the specific example to clearly discuss the biological significance of the acquisition of TEs for the thymic APC functions and the thymic selection.

In Figure 2, the authors focused on ETS-1 and its potential target genes ZNF26 and MTMR3, however, the significance of these genes in NK cell function or development is unclear. The authors should examine and discuss whether the distinct features of TEs can be found among the genomic loci that link to the fundamental function of the thymus, e.g., antigen processing/presentation.

We thank the Reviewer for this highly relevant comment. We investigated the genomic loci associated with NK cell biology to determine if ETS1 peaks would overlap with TE sequences in protein-coding genes' promoter region. Figure 2h illustrates two examples of ETS1 significant peaks overlapping TE sequences upstream of PRF1 and KLRD1. PRF1 is a protein implicated in NK cell cytotoxicity, whereas KLRD1 (CD94) dimerizes with NKG2 and regulates NK cell activation via interaction with the nonclassical MHC-I molecule HLA-E (2, 3). Thus, we modified the section of the manuscript addressing these results to include these new analyses: "Finally, we analyzed publicly available ChIP-seq data of ETS1, an important TF for NK cell development (4), to confirm its ability to bind TE sequences. Indeed, 19% of ETS1 peaks overlap with TE sequences (Figure 2g). Notably, ETS1 peaks overlapped with TE sequences (Figure 2h, in red) in the promoter regions of PRF1 and KLRD1, two genes important for NK cells' effector functions (2, 3)."

------

I am convinced by the authors' explanation that TE elements may contribute to the functions of NK cells.

However, since I have understood that the main topic of this paper is about the thymus and thymic antigen-presenting cells, the mention of NK cells seems abrupt and unconnected to me. NK cells are a type of innate lymphocyte that arise in the bone marrow, and thymus is dispensable for their development and function. The readers might expect to find something more fundamental regarding the function of the thymus and immunological tolerance.

(3) Since the deep analysis of the dataset yielded many intriguing suggestions, why not add a discussion of the biological reasons and significance? For example, in Figure 1, why is TE expression negatively correlated with proliferation? cTEC-TE is mostly postnatal, while mTEC-TE is more embryonic. What does this mean?

We thank the Reviewer for this comment. To our knowledge, the relationship between cell division and transcriptional activity of TEs has not been extensively studied in the literature. However, a recent study has shown that L1 expression is induced in senescent cells. We therefore added the following sentences to our Discussion: "The negative correlation between TE expression and cell cycle scores in the thymus is coherent with recent data showing that transcriptional activity of L1s is increased in senescent cells (5). A potential rationale for this could be to prevent deleterious transposition events during DNA replication and cell division." We also added several discussion points regarding the regulation of TEs by KZFPs to answer concerns raised by Reviewer 2 (see Reviewer 2 comment #1).

------

I agree on the possibility suggested by the authors.

(4) To consolidate the experimental evidence about pDCs and TE-derived dsRNAs, one option is to show the amount of TE-derived RNA copies among total RNAs. The immunohistochemistry analysis in Figure 4 requires additional data to demonstrate that overlapped staining was not caused by technical biases (e.g. uneven fixation may cause the non-specifically stained regions/cells). To show this, authors should have confirmed not only the positive stainings but also the negative staining (e.g. CD3, etc.). Another possible staining control was showing that non-pDC (CD303- cell fractions in this case) cells were less stained by the ds-RNA probe.

We thank the Reviewer for this suggestion. We computed the proportion of reads in each cell assigned to two groups of sequences known to generate dsRNAs: TEs and mitochondrial genes (1). These analyses showed that the proportion of reads assigned to TEs is higher in pDCs than other thymic APCs by several orders of magnitude (~20% of all reads). In contrast, reads derived from mitochondrial genes had a lower abundance in pDCs. We included these results in Figure 4 - figure supplement 2 and included the following text in the Results section "To evaluate if these dsRNAs arise from TE sequences, we analyzed in thymic APC subsets the proportion of the transcriptome assigned to two groups of genomic sequences known as important sources of dsRNAs, TEs and mitochondrial genes (1). Strikingly, whereas the percentage of reads from mitochondrial genes was typically lower in pDCs than in other thymic APCs, the proportion of the transcriptome originating from TEs was higher in pDCs (~22%) by several orders of magnitude (Figure 4 - figure supplement 2)." As a negative control for the immunofluorescence experiments, we used CD123- cells. Indeed, flow cytometry analysis of the magnetically enriched CD303+ fraction was around 90% pure, as revealed by double staining with CD123 and CD304 (two additional markers of pDCs): CD123- cells were also CD304-/lo, showing that these cells are non- pDCs. Thus, we decided to compare the dsRNA signal between CD123+ cells (pDCs) and CD123- cells (non-pDCs). The difference between CD123+ and CD123- cells was striking (Figure 4d).

------

Although the technical concerns about immunostaining were not resolved, it is understandable that it would be difficult to rerun the experiment since the authors used the precious human thymi as the experimental material. Immunostaining co-staining requires careful interpretation so that careful experimental setup is needed.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91037.3.sa2](https://doi.org/10.7554/eLife.91037.3.sa2)

Summary:

Larouche et al show that TEs are broadly expressed in thymic cells, especially in mTECs and pDCs. Their data suggest a possible involvement of TEs in thymic gene regulation and IFN-alpha secretion. They also show that at least some TE-derived peptides are presented by MHC-I in the thymus.

Strengths:

The idea of high/broad TE expression in the thymus as a mechanism for preventing TE-mediated autoimmunity is certainly an attractive one, as is their involvement in IFN-alpha secretion therein. The analyses and experiments presented here are therefore a very useful primer for more in-depth experiments, as the authors point out towards the end of the discussion.

Weaknesses:

There are many dangers about analysing RNA-seq data at the subfamily level. Outputs may be greatly confounded by pervasive transcription, DNA contamination, and overlap of TEs with highly expressed genes. Whether TE transcripts are independent units or part of a gene also has important implications for the conclusions drawn. The authors have tried to mitigate against some of these issues, but they have not been completely ruled out.
