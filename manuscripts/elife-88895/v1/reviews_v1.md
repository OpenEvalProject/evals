# Peer review - Round 1

Editors:
- Thomas R Gingeras, Cold Spring Harbor Laboratory United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.88895.3.sa0](https://doi.org/10.7554/eLife.88895.3.sa0)

This study of extrachromosomal DNA (ecDNA) identifies genes that distinguish ecDNA+ and ecDNA- tumors. The findings in the manuscript are important and the genomic analyses convincing. However, some of the data remain observational and the inferences would therefore be more robust with experimental validation. This manuscript could well be of relevance to biologists interested in cancer biology and gene regulation.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88895.3.sa1](https://doi.org/10.7554/eLife.88895.3.sa1)

Recently discovered extrachromosomal DNA (ecDNA) provides an alternative non-chromosomal means for oncogene amplification and a potent substrate for selective evolution of tumors. The current work aims to identify key genes whose expression distinguishes ecDNA+ and ecDNA- tumors and the associated processes to shed light on the biological mechanisms underlying ecDNA genesis and their oncogenic effects. This is clearly an important question and through detailed analysis this work points to specific GO processes associated (up and down) with ecDNA+ tumors, namely, specific DNA damage repair processes and specific oncogenic processes.

In the initial submission I had commented on lack of clarity of method, potential biases, and in some cases inappropriate interpretation. In the revised version, the authors have addressed all my comments satisfactorily and I think this is an important work furthering our understanding of mechanisms underlying ecDNA+ tumors.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88895.3.sa2](https://doi.org/10.7554/eLife.88895.3.sa2)

In their manuscript Lin et al. describe an important study on the transcriptional programs associated with the presence of extrachromosomal DNA in a cohort of 870 cancers of different origins. The authors find that compared to cancers lacking such amplifications, ecDNA+ cancers express higher levels of DNA damage repair-associated genes, but lower levels of immune-related gene programs.

This work is very timely and its findings have the potential to be very impactful, as the transcriptional context differences between ecDNA+ and ecDNA- cancers are currently largely unknown. The observation that immune programs are downregulated in ecDNA+ cancers may initiate new preclinical and translational studies that impact the way ecDNA+ cancers are treated in the future. Thus, this study has important theoretical implications that have the potential to substantially advance our understanding of ecDNA+ cancers.

Strengths:

The authors provide compelling evidence for their conclusions based on large patient datasets. The methods they used and analyses are rigorous.

Weaknesses:

The biological interpretation of the data remains observational. The direct implication of these genes in ecDNA(+) tumors is not tested experimentally.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88895.3.sa3](https://doi.org/10.7554/eLife.88895.3.sa3)

Summary:

Using a combination of approaches, including automated feature selection and hierarchical clustering, the author identified a set of genes persistently associated with extrachromosomal DNA (ecDNA) presence across cancer types. The authors further validated the gene set identified using gene ontology enrichment analysis and identified that upregulated genes in extrachromosomal DNA-containing tumors are enriched in biological processes like DNA damage and cell proliferation, whereas downregulated genes are enriched in immune response processes.

Comments for the previous version:

Major comments:

(1) The authors presented a solid comparative analysis of ecDNA-containing and ecDNA-free tumors. An established automated feature selection approach, Boruta, was used to select differentially expressed genes (DEG) in ecDNA(+) and ecDNA(-) TCGA tumor samples, and the iterative selection process and two-tier multiple hypothesis testing ensured the selection of reliable DEGs. The author showed that the DEG selected using Boruta has stronger predictive power than genes with top log-fold changes.

(2) The author performed a thorough interpretation of the findings with GO enrichment analysis of biological processes enriched in the identified DEG set and presented interesting findings, including the enrichment in DNA damage process among the genes upregulated in ecDNA(+) tumors.

(3) Overall, the authors achieved their aims with solid data mining and analysis approaches applied to public data tumor data sets.

(4) While it may not be the scope of this study, it will be interesting to at least have some justification for choosing Boruta over other feature selection methods, such as Recursive Feature Elimination (RFE) and backward stepwise selection.

(5) The authors showed that DESEQ-selected DEGs with top log-fold changes have less strong predictive power and speculated that this may be due to the fact that genes with top log-fold changes (LFC) are confined only to a small subset of samples. It will be interesting to select DEGs with top log-fold changes after first partitioning the tumor samples. For example, randomly partition the tumor samples, identify the DEGs with top LFC, combine the DEGs identified from each partition, then evaluate the predictive power of these DEGs against the Boruta-selected DEGs.

(6) While the authors showed that the presence of mutations was not able to classify ecDNA(+) and (-) tumor samples, it will be interesting to see if variant allele frequencies of the genes containing these mutations have predictive power.

Comments for the revised version:

The authors addressed the comments and recommendations with solid analysis and explanations in the revision. The added analysis using GLM is especially appreciated and provides convincing evidence for the predicting power of the Boruta-selected genes. The only comment is at this point is that it is recommended that the author provide some justification for choosing Boruta over other feature selection methods. It is not necessary to provide benchmarking results - justification based on the review of previous literature is sufficient, as it is not well explained in the paper why Boruta was chosen in the first place. Is it state-of-the-art? Has it demonstrated better performance in other settings? A few sentences answering these questions should suffice.
