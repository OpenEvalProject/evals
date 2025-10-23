# Peer review - Round 1

Editors:
- Jeremy L England, GlaxoSmithKline Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.92870.3.sa0](https://doi.org/10.7554/eLife.92870.3.sa0)

The authors presented a valuable bioinformatics pipeline for screening and identifying inhibitory receptors for potential drug targets. They provided solid evidence showing a sequential reduction in the search space through various screening tools and algorithms and demonstrated that this pipeline can be used to "rediscover" known targets. Further experimental validation on putative and unknown inhibitory receptors will strengthen the evidence reported in this work. This study will be of interest to bioinformaticians and computational biologists working on immune regulation, sequence screening, and target identification of immune checkpoint inhibitors.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.92870.3.sa1](https://doi.org/10.7554/eLife.92870.3.sa1)

Summary:

The authors developed a bioinformatic pipeline to aid the screening and identification of inhibitory receptors suitable as drug targets. The challenge lies in the large search space and lack of tools for assessing the likelihood of their inhibitory function. To make progress, the authors used a consensus protein membrane topology and sequence motif prediction tool (TOPCOS) combined with both a statistical measure assessing their likelihood function and a machine learning protein structural prediction model (AlphaFold) to greatly cut down the search space. After obtaining a manageable set of 398 high confidence known and putative inhibitory receptors through this pipeline, the authors then mapped these receptors to different functional categories across different cell types based on their expression both in the resting and activated state. Additionally, by using publicly available pan cancer scRNA-seq for tumor-infiltrating T cells data, they showed that these receptors are expressed across various cellular subsets.

Strengths:

The authors presented sound arguments motivating the need to efficiently screen inhibitory receptors and to identify those that are functional. Key components of the algorithm were presented along with solid justification for why they addressed challenges faced by existing approaches. To name a few:

• TOPCON algorithm was elected to optimize the prediction of membrane topology

• A statistical measure was used to remove potential false positives

• AlphaFold is used to filter out putative receptors that are low confidence (and likely intrinsically disordered)

To examine receptors screened through this pipeline through a functional lens, the authors proposed to look at their expression of various immune cell subsets to assign functional categories. This is a reasonable and appropriate first step for interpreting and understanding how potential drug targets are differentially expressed in some disease contexts. They also presented an example showing this pipeline can be used to "rediscover" known targets.

Weaknesses:

The paper has strength in the pipeline they presented, but the weakness, in my opinion, lies in the lack of direct experimental validation on putative receptors. That said, the authors presented in the revised manuscript, as a proof-of-concept, an analytic approach for using functional categorization of putative inhibitory receptors to select therapeutic targets based on in vitro RNAseq. Such analysis will benefit from further investigation across different cancer types using in vivo expression.
