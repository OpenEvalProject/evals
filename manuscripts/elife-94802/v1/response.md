# Author response - Round 1

Authors:
- Rebeca de la Fuente ([ORCID: 0000-0003-1536-5689](https://orcid.org/0000-0003-1536-5689))
- Wladimiro Dı́az-Villanueva ([ORCID: 0000-0002-8970-4367](https://orcid.org/0000-0002-8970-4367))
- Vicente Arnau ([ORCID: 0000-0002-1388-6141](https://orcid.org/0000-0002-1388-6141))
- Andres Moya ([ORCID: 0000-0002-2867-1119](https://orcid.org/0000-0002-2867-1119))

## Response text

DOI: [10.7554/eLife.94802.3.sa4](https://doi.org/10.7554/eLife.94802.3.sa4)

The following is the authors’ response to the original reviews.

Reviewer #1

Methodological biases in annotation and sequencing methods

We acknowledge the reviewer’s concern regarding methodological heterogeneity in genome annotations, particularly regarding the use of CDS annotations derived from public databases. In response, we have properly addressed the potential sources of bias in estimating alternative splicing (AS) across such a broad taxonomic range.

Given the methodological challenges encountered in this study, we have undertaken an in-depth analysis of the biases associated with genome annotations and their impact on large-scale estimates of alternative splicing. This effort has resulted in the development of a comprehensive framework for quantifying, modeling, and correcting such biases, which we believe will be of interest to the broader genomics community. We are currently preparing a separate manuscript dedicated to this methodological aspect, which we intend to submit for publication in the near future.

To account for these biases, we performed a statistical evaluation of annotation quality by examining the relationship between ASR values and multiple features of the NCBI annotation pipeline, including both technical and biological variables. Specifically, we analyzed a set of metadata descriptors related to: (i) genome assembly quality (e.g., Contig N50, Scaffold N50, number of gaps, gap length, contig/scaffold count), (ii) the amount and diversity of experimental evidence used in annotation (e.g., number of RNA-Seq reads, number of tissues, number of experimental runs, number of proteins and transcripts, including those derived from Homo sapiens), and (iii) the nature of the annotated coding sequences (e.g., total number of CDSs, percentage of CDSs supported by experimental evidence, proportion of known CDSs, percentage of CDSs derived from ab initio predictions).

This comprehensive analysis revealed that the strongest bias affecting ASR values is associated with the proportion of fully supported CDSs, which showed a strong positive correlation with observed splicing levels. In contrast, the percentage of CDSs relying on ab initio models showed a negative correlation, indicating that computational predictions tend to underestimate splicing complexity. Based on these findings, we implemented a polynomial normalization model using the percentage of fully supported CDSs as the main predictor of annotation bias. The resulting normalized metric, ASR∗, corrects for annotation-related variability while preserving biologically meaningful variation.

We further verified the robustness of this correction by comparing the main results of our study using both the raw ASR and the normalized ASR* across all analyses. The qualitative and quantitative consistency of results obtained with both metrics demonstrates that our findings are not an artifact of methodological bias and validates the reliability of our approach.

Conceptual and Statistical Framework

Our aim was not to investigate specific regulatory mechanisms of alternative splicing, but rather to explore large-scale statistical patterns across the tree of life using a newly defined metric—the Alternative Splicing Ratio (ASR)—that enables genome-wide comparisons of splicing complexity across species. To clarify the conceptual framework, we have revised the manuscript to explicitly state our assumptions, objectives, and the scope of our conclusions. The ASR metric is now briefly introduced in the Results section, with a more detailed mathematical formulation included in the Methods section.

From a methodological standpoint, we have expanded the manuscript to better support the comparative framework through additional statistical analyses. In particular, we now include:

• Monte Carlo permutation tests to assess pairwise differences in splicing and genomic variables across taxonomic groups, which are robust to non-normality and heteroscedasticity in the data.

• Welch’s ANOVA with Bonferroni correction, which accounts for unequal variances when comparing group means.

• Phylogenetic Generalized Least Squares (PGLS) regression, which explicitly models phylogenetic non-independence between species and allows us to infer lineage-specific associations between genomic composition and alternative splicing.

• Coefficient of variation analysis, used to evaluate the relative variability of splicing and genomic traits across groups in a scale-independent manner.

• Variability ratio metrics, designed to compare the dispersion of splicing values relative to genomic features, thereby quantifying trends in regulatory plasticity versus structural constraints.

All methods are thoroughly described in the revised Methods section, and their application is presented in the Results section.

Functional vs. non-functional nature of AS events

We have included a new discussion paragraph addressing the ongoing debate regarding the functionality of alternative splicing and a possible non-adaptive explanation for the patterns observed. While many previous studies suggest that a considerable fraction of AS events might represent splicing noise or non-functional isoforms, our intention is not to adopt this view uncritically. Instead, we cite recent literature to provide a more nuanced interpretation, recognizing both the potential adaptive value and the uncertainty surrounding the functional relevance of many AS events. Thus, rather than assuming that all observed alternative splicing events are adaptive or biologically meaningful, we now emphasize that many patterns may emerge from other processes, such as those associated to genomic constraints.

Terminology and Result Interpretation

The manuscript has been thoroughly revised to improve both the scientific language and the conceptual framing. We have removed inappropriate terminology such as “higher/lower organisms” and “highly evolved”. Also, we have reinterpreted the results. As part of this process, the manuscript has been substantially rewritten to focus on the most meaningful findings. Ultimately, we have retained only those results that specifically concern broad-scale patterns of alternative splicing across taxa, which are now presented with greater clarity and methodological rigor.

Reviewer #2

Gene Regulatory Complexity Beyond Splicing Mechanisms

While alternative splicing represents a prominent mechanism of transcriptomic diversification, we agree with the reviewer that it constitutes only one component of the broader landscape of gene regulation. Structural and behavioral complexity in organisms arises from a combination of regulatory processes, and our study focuses specifically on alternative splicing as a measurable proxy within this multifactorial system. To clarify this point, we have added a paragraph in the Discussion section, where we explicitly contextualize alternative splicing within the wider regulatory architecture. In that paragraph, we discuss additional mechanisms that contribute to phenotypic complexity—such as transcriptional control, chromatin remodeling, epigenetic modifications, and RNA editing—citing key literature.

Alternative Splicing Measure and Methodology

While we agree that alternative splicing is not a definitive measure of organismal complexity, we argue that it remains a meaningful proxy for transcriptomic and regulatory diversification, especially when analyzed at large phylogenetic scale. In this version of the manuscript, our goal was not to equate alternative splicing with biological complexity, but rather to quantify its patterns across lineages and evaluate its relationship with genome structure. This point is now explicitly stated in both the Introduction and Discussion.

We also recognize the limitations associated with the use of coding sequence (CDS) annotations from public databases such as NCBI RefSeq. To address this concern, we have conducted a detailed analysis of the potential biases introduced by heterogeneous annotation quality, sequencing depth, and computational prediction, as previously addressed in our response to Reviewer #1.

In response to concerns about unsupported statements, we have completely rewritten the manuscript to ensure that all claims are now explicitly supported by data and grounded in up-to-date scientific literature. We have reformulated speculative statements, removed inappropriate generalizations, and improved the logical flow of the arguments throughout the text. In summary, we have strengthened both the conceptual framework and the methodological foundation of the study, while maintaining a cautious interpretation of the results.

Trends of Alternative Splicing

To address the reviewer’s concern, we have revised the interpretation of trends as used in our analysis. In this study, we define a trend not as a strict directional progression or a linear trajectory across all species, but rather as a broad statistical pattern observable in the relative distribution and variability of alternative splicing across major taxonomic groups. We do not claim that this pattern reflects a universal adaptive pathway. Instead, we interpret it as a signal of differences in regulatory strategies associated to the genome architecture. To avoid misinterpretation, we have rephrased several sentences in the manuscript and explicitly emphasized the variability within groups, and the lack of significant correlations in certain clades.

Inconsistent statistics

The discrepancies pointed out were due to differences between mean and median-based analyses. These have been clarified and consistently reported in the revised manuscript. Error bars, p-values, and a supplementary table summarizing all tests are now included. Furthremore, we have no removed any species from our dataset.
