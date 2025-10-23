# Peer review - Round 1

Editors:
- Bérénice A Benayoun, University of Southern California United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.88623.3.sa0](https://doi.org/10.7554/eLife.88623.3.sa0)

This work presents an important online platform designed to facilitate the exploration of genes and genetic pathways implicated in human aging. Leveraging a new inference methodology, the tool enables the identification and visualization of key genes and tissues impacted by aging, facilitating scientific discovery. The methods and analyses are convincing and will be broadly used by scientists aiming to mine human aging RNA-seq data.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88623.3.sa1](https://doi.org/10.7554/eLife.88623.3.sa1)

This fascinating paper by A.L. Schneider et al. describes voyAGEr, a shiny-based interface for easy exploration of the GTEx dataset by non- or novice programmers. Importantly, voyAGEr is open source and available from github, which could greatly accelerate additional development and further uses of this interesting tool.

The authors developed a pipeline for modeling age-related changes in gene expression in the GTEx data called ShARP-LM, fitting a linear model for age, sex and age&sex interaction terms. This pipeline underlies the later analyses that can be applied within voyAGEr. These analyses are labeled by tissue so that users can easily begin a query based on a tissue or a gene of possible interest.

voyAGEr implements many kinds of interesting R-based tools such as pathway overrepresentation analysis and gene co-expression module analysis, in a way that akes these approaches accessible to non-bioinformaticist aging researchers.

As the tidal wave of publicly available large, high-dimensional datasets such as transcriptomes continues to grow exponentially, the usefulness of tools such as voyAGEr will only increase. While test users may be able to imagine features or refinements they wish were already present, due to the open source approach they or anyone else including but not limited to the present authors can implement additional features in the future. I look forward to using this tool and to staying abreast of its future development.

Overall, this study describes a new tool of interest to the field. The manuscript is clearly written overall, with a few minor suggested corrections, as noted below. The figures and supplementary information are all clear and all add to the manuscript.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88623.3.sa2](https://doi.org/10.7554/eLife.88623.3.sa2)

The purpose of this study is to develop a tool that serves as a starting point for investigating and uncovering genes and pathways associated with aging. The tool utilizes information from the GTEx public database, which contains post-mortem human data. It focuses on identifying age-related gene expression changes across different age range, biological sexes, and medical histories, with a focus on specific tissues.

Additionally, the authors envision the platform as continuously evolving, with ongoing development and expansion to include new data and features, ensuring it remains a cutting-edge resource for researchers studying aging.

voyAGEr presents a tool for exploring gene expression changes across multiple tissues in the context of aging. One of the main strengths of the tool is its intuitive and user-friendly interface, which allows for easy navigation and exploration of gene expression patterns for biologists. Users can explore changes in gene expression of single genes across multiple tissues, enabling them to identify genes of interest that can be further investigated.

A particularly noteworthy strength of the tool is its ability to show tissue-specific gene expression patterns. This feature is essential for elucidating the paradigm of tissue-specific asynchronous aging and provides a unique and valuable resource for the aging community.

However, the choice of the R shiny platform for visualization may not be the most conducive to extensibility and open-source collaboration, owing to its lack of modularity. Alternatives like Flask or FastAPI, which are more production-oriented, could be more appropriate. Additionally, despite using preprocessed data and functioning primarily as a visualization platform, the tool occasionally experiences lag, indicating room for performance improvement. These aspects are worth considering for future versions of the tool.

Overall, voyAGEr offers an entry point for further investigation of genes involved in aging, and its ability to show tissue-specific gene expression patterns provides a unique and valuable resource for the scientific community.

Finally, the tool is complemented by a comprehensive tutorial that elucidates each functionality and includes examples. The authors have shared the code for preprocessing and the tool itself. They also acknowledge the limitations of the statistical inference tests and their interpretation in the manuscript, contributing to its transparency.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88623.3.sa3](https://doi.org/10.7554/eLife.88623.3.sa3)

In their manuscript, Schneider et al. aim to develop voyAGEr, a web-based tool that enables the exploration of gene expression changes over age in a tissue- and sex-specific manner. The authors achieved this goal by calculating the significance of gene expression alterations within a sliding window, using their unique algorithm, Shifting Age Range Pipeline for Linear Modelling (ShARP-LM), as well as tissue-level summaries that calculated the significance of the proportion of differentially expressed genes by the windows and calculated enrichments of pathways for showing biological relevance. Furthermore, the authors examined the enrichment of cell types, pathways, and diseases by defining the co-expressed gene modules in four selected tissues. Although their algorithm ShARP-LM has limited statistical power due to its calculation within a 16-year window, the voyAGEr was developed as a discovery tool, giving researchers easy access to the vast amount of transcriptome data from the GTEx project. Overall, the research design is unique and well-performed in simulating age-dependent changes in gene expression. The interesting results provide useful resources for the field of human genetics of aging.
