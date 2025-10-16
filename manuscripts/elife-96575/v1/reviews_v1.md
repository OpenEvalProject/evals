# Peer review - Round 1

Editors:
- Weiwei Dang, Baylor College of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.96575.4.sa0](https://doi.org/10.7554/eLife.96575.4.sa0)

The study by Tsai et al. employed multi-omics approaches, including transcriptomic, methylomic, and single-cell RNA-seq, and provided a solid and comprehensive analysis of the correlation between retrotransposable element (RTE) expression and biological aging in human blood. Their findings highlight the differential roles of RTE families, providing valuable insights for understanding the mechanisms of human aging.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.96575.4.sa1](https://doi.org/10.7554/eLife.96575.4.sa1)

Tsai and Seymen et al. investigate associations between RTE expression and methylation and age and inflammation, using multiple public datasets. The text of the manuscript has been polished and the phrasing of several findings has been made clearer and more precise. The authors also provided ample discussion to the prior reviewer comments in their rebuttal, including new analyses.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.96575.4.sa2](https://doi.org/10.7554/eLife.96575.4.sa2)

Summary:

Yi-Ting Tsai and colleagues conducted a systematic analysis of the correlation between the expression of retrotransposable elements (RTEs) and aging, using publicly available transcriptional and methylome microarray datasets of blood cells from large human cohorts, as well as single-cell transcriptomics. Although DNA hypomethylation was associated with chronological age across all RTE biotypes, the authors did not find a correlation between the levels of RTE expression and chronological age. However, expression levels of LINEs and LTRs positively correlated with DNA demethylation, and inflammatory and senescence gene signatures, indicative of "biological age". Gene set variation analysis showed that the inflammatory response is enriched in the samples expressing high levels of LINEs and LTRs. In summary, the study demonstrates that RTE expression correlates with "biological" rather than "chronological" aging.

Strengths:

The question the authors address is both relevant and important to the fields of aging and transposon biology.

Comments on latest version:

The authors introduced the analysis of RNA-seq data, addressing the key concerns raised by Reviewer #1 and myself. They also adopted more explicit terminology in their latest version, reducing ambiguity. The RNA-seq analysis demonstrating that the expression of different transposon groups is not associated with chronological aging is convincing, though, in my opinion, it still lacks granularity.

I have two minor points:

(1) Previously, I have mentioned the following:

"The authors pool signals from RTEs by class or family, despite the fact that these groups include subfamilies and members with very different properties and harmful potentials. For example, while older subfamilies might be expressed through readthrough transcription, certain members of younger groups could be autonomously reactivated and cause inflammation... The aggregation of signals from different RTE biotypes may obscure potential reactivation of smaller groups or specific subfamilies."

The authors responded that they would lose statistical power by studying RTE subfamilies with limited microarray probes, which is a fair point. However, the suggested analysis could have been conducted using the RNA-seq data they explored in the second round of revision. Choosing not to leverage RNA-seq to increase the granularity of their analysis is a matter of choice. In my opinion, however, the authors could have acknowledged in the discussion that some smaller yet potentially influential RTE species may be masked by their global approach.

(2) Previously, I mentioned that 10x scRNA-seq is not ideal for analysing RTEs and requested a classical UMAP plot to visualize RTE expression across cell populations. The authors argued that they could only achieve sufficient statistical power by quantifying RTE classes through cumulative read counts for each cell type, which I accept. However, they divided cells into "high" and "low" BAR gene signature groups. I am surprised that the comparison of BAR signature expression between these groups was not presented using standard visualization methods commonly applied in scRNA-seq data analysis.
