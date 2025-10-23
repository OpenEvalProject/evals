# Peer review - Round 1

Editors:
- Virginie Courtier-Orgogozo, CNRS - Universite Paris Cite France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.94802.3.sa0](https://doi.org/10.7554/eLife.94802.3.sa0)

The authors examined the frequency of alternative splicing across prokaryotes and eukaryotes and found that the rate of alternative splicing varies with taxonomic groups and genome coding content. This solid work, based on nearly 1500 high-quality genome assemblies, relies on a novel genome-scale metric that enables cross-species comparisons and that quantifies the extent to which coding sequences generate multiple mRNA transcripts via alternative splicing. This timely study provides an important basis for improving our general understanding of genome architecture and the evolution of life forms.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.94802.3.sa1](https://doi.org/10.7554/eLife.94802.3.sa1)

Summary:

In this contribution, the authors investigate the degree of alternative splicing across the evolutionary tree, and identify a trend of increasing alternative splicing as you move from the base of the tree (here, only prokaryotes are considered) towards the tips of the tree. In particular, the authors investigate how the degree of alternative splicing (roughly speaking, the number of different proteins made from a single ORF (open reading frame) via alternative splicing) relates to three genomic variables: the genome size, the gene content (meaning the fraction of the genome composed of ORFs), and finally, the coding percentage of ORFs, meaning the ratio between exons and total DNA in the ORF.

The revised manuscript addresses the problems identified in the first round of reviews and now serves as a guide to understand how alternative splicing has evolved within different phyla, as opposed to making unsubstantiated claims about overall trends.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.94802.3.sa2](https://doi.org/10.7554/eLife.94802.3.sa2)

Summary:

In "Alternative Splicing Across the Tree of Life: A Comparative Study," the authors use rich annotation features from nearly 1,500 high-quality NCBI genome assemblies to develop a novel genome-scale metric, the Alternative Splicing Ratio, that quantifies the extent to which coding sequences generate multiple mRNA transcripts via alternative splicing (AS). This standardized metric enables cross-species comparisons and reveals clear phylogenetic patterns: minimal AS in prokaryotes and unicellular eukaryotes, moderate AS in plants, and high AS in mammals and birds. The study finds a strong negative correlation between AS and coding content, with genomes containing approximately 50% intergenic DNA exhibiting the highest AS activity. By integrating diverse lines of prior evidence, the study offers a cohesive evolutionary framework for understanding how alternative splicing varies and evolves across the tree of life.

Strengths:

By studying alternative splicing patterns across the tree of life, the authors systematically address an important yet historically understudied driver of functional diversity, complexity, and evolutionary innovation. This manuscript makes a valuable contribution by leveraging standardized, publicly available genome annotations to perform a global survey of transcriptional diversity, revealing lineage-specific patterns and evolutionary correlates. The authors have done an admirable job in this revised version, thoroughly addressing prior reviewer comments. The updated manuscript includes more rigorous statistical analyses, careful consideration of potential methodological biases, expanded discussion of regulatory mechanisms, and acknowledgment of non-adaptive alternatives. Overall, the work presents an intriguing view of how alternative splicing may serve as a flexible evolutionary strategy, particularly in lineages with limited capacity for coding expansion (e.g., via gene duplication). Notably, the identification of genome size and genic coding fraction thresholds (~20 Mb and ~50%, respectively) as tipping points for increased splicing activity adds conceptual depth and potential generalizability.

Weaknesses:

While the manuscript offers a broad comparative view of alternative splicing, its central message becomes diffuse in the revised version. The focus of the study is unclear, and the manuscript comes across as largely descriptive without a well-articulated hypothesis or explanatory evolutionary model. Although the discussion gestures toward adaptive and non-adaptive mechanisms, these interpretations are not developed early or prominently enough to anchor the reader. The negative correlation between alternative splicing and coding content is compelling, but the biological significance of this pattern remains ambiguous: it is unclear whether it reflects functional constraint, genome organization, or annotation bias. This uncertainty weakens the manuscript's broader evolutionary inferences.

Sections of the Introduction, particularly lines 72-90, lack cohesion and logical flow, shifting abruptly between topics without a clear structure. A more effective approach may involve separating discussions of coding and non-coding sequence evolution to clarify their distinct contributions to splicing complexity. Furthermore, some interpretive claims lack nuance. For example, the assertion that splicing in plants "evolved independently" seems overstated given the available evidence, and the citation regarding slower evolution of highly expressed genes overlooks counterexamples from the immunity and reproductive gene literature.

Presentation of the results is occasionally vague. For instance, stating "we conducted comparisons of mean values" (line 146) without specifying the metric undercuts interpretability. The authors should clarify whether these comparisons refer to the Alternative Splicing Ratio or another measure. Additionally, the lack of correlation between splicing and coding region fraction in prokaryotes may reflect a statistical power issue, particularly given their limited number of annotated isoforms, rather than a biological absence of pattern.

Finally, the assessment of annotation-related bias warrants greater methodological clarity. The authors note that annotations with stronger experimental support yield higher splicing estimates, yet the normalization strategy for variation in transcriptomic sampling (e.g., tissue breadth vs sequencing depth) is insufficiently described. As these factors can significantly influence splicing estimates, a more rigorous treatment is essential. While the authors rightly acknowledge that splicing represents only one layer of regulatory complexity, the manuscript would benefit from a more integrated consideration of additional dimensions, such as 3D genome architecture, e.g., the potential role of topologically associating domains in constraining splicing variation.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.94802.3.sa3](https://doi.org/10.7554/eLife.94802.3.sa3)

The manuscript reports on a large-scale study correlating genomic architecture with splicing complexity over almost 1,500 species. We still know relatively little about alternative splicing functional consequences and evolution, and thus, the study is relevant and timely. The methodology relies on annotations from NCBI for high-quality genomes and a main metric proposed by the authors and named Alternative Splicing Ratio (ASR). It quantifies the level of redundancy of each coding nucleotide in the annotated isoforms.

According to the authors' response to the first reviewers' comments, the present version of the manuscript seems to be a profoundly revised version compared to the original submission. I did not have access to the reviewers' comments.

Although the study addresses an important question and the authors have visibly made an important effort to make their claims more statistically robust, I have a number of major concerns regarding the methodology and its presentation.

(1) A large part of the manuscript is speculative and vague. For instance, the Discussion is very long (almost longer than the Results section) and the items discussed are sometimes not in direct connection with the present work. I would suggest merging the last 2 paragraphs, for instance, since the before last paragraph is essentially a review of the literature without direct connection to the present work.

(2) The Methods section lacks clarity and precision. A large part is devoted to explaining the biases in the data without any reference or quantification. The definition of ASR is very confusing. It is first defined in equation 2, with a different name, and then again in the next subsection from a different perspective on lines 512-518. Why build matrices of co-occurrences if these are, in practice, never used? It seems the authors exploit only the trace. A major revision, if I understood correctly, was the correction/normalisation of the ASR metric. This normalisation is not explained. The authors argue that they will write another paper about it, I do not think this is acceptable for the publication of the present manuscript. Furthermore, there is no information about the technical details of the implementation: which packages did the authors use?

(3) Could the authors motivate why they do not directly focus on the MC permutation test? They motivate the use of permutations because the data contains extreme outliers and are non normal in most cases. Hence, it seems the Welch's ANOVA is not adapted. "To further validate our findings, we also conducted

148 a Monte Carlo permutation test, which supported the conclusions (see Methods)." Where is the comparison shown? I did not see any report of the results for the non-permuted version of the Welch's ANOVA.

(4) What are the assumptions for the Phylogenetic Generalized Least Squares? Which evolution model was chosen and why? What is the impact of changing the model? Could the authors define more precisely (e.g. with equations) what is lambda? Is it estimated or fixed?

(5) I think the authors could improve their account of recent literature on the topic. For instance, the paper https://doi.org/10.7554/eLife.93629.3, published in the same journal last year, should be discussed. It perfectly fits in the scope of the subsection "Evidence for the adaptive role of alternative splicing". Methods and findings reported in https://doi.org/10.1186/s13059-021-02441-9 and https://www.genome.org/cgi/doi/10.1101/gr.274696.120 directly concern the assessment of AS evolutionary conservation across long evolutionary times and/or across many species. These aspects are mentioned in the introduction on p.3. but without pointing to such works. Can we really qualify a work published in 2011 as "recent" (line 348-350)?

The generated data and codes are available on Zenodo, which is a good point for reproducibility and knowledge sharing with the community.
