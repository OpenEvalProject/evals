# Peer review - Round 1

Editors:
- J Gage Crump, Keck School of Medicine of University of Southern California United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.54695.sa1](https://doi.org/10.7554/eLife.54695.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper elegantly uses single-cell RNA sequencing to refine our understanding of the mesenchymal components of the bone marrow. A major population of adipocyte lineage cells is found that functions to stabilize blood vessels and suppress bone formation. The findings also suggest that early multipotent progenitors may represent a much smaller fraction of the marrow than previously appreciated.

Decision letter after peer review:

Thank you for submitting your article "Single cell transcriptomics identifies a unique adipose cell population that regulates bone marrow environment" for consideration by eLife. Your article has been reviewed by three peer reviewers, including J Gage Crump as the guest Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Clifford Rosen as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

This is an interesting study that uses single-cell RNA sequencing to dissect heterogeneity of the bone marrow mesenchyme from young to adult stages in mouse. The authors report a new pre-adipocyte-like bone marrow cell population named MERA, which they define as a downstream population of MSCs by single cell RNA-seq analysis. In the first part of the paper, they computationally redefine MSCs as Sca1+ cells based on large-scale stromal scRNA-seq datasets. In the second part, they report that ablation of MERAs by Adipoq-Cre causes disruption in marrow vasculature and an increase in bone formation. Together this study is significant in clarifying the cell types in the marrow that give rise to adipocytes and osteocytes, as well as revealing a type of stromal cell with adipocyte potential that restricts bone formation and ensures proper marrow structure. What sets this study apart from preceding single-cell RNA sequencing studies is that it provides functional validation of the computational discoveries.

While the reviewers recognize the potential significance of the study, there were major concerns that would need to be addressed before it is suitable for publication.

1) The authors need to deposit their sequencing data in GEO. The data could be password protected and only accessible to the reviewers. Four out of six figures contain computational data. The reviewers found it difficult to assess the bioinformatic analysis without this raw data access.

2) Use of a new acronym "MERA" appears unwarranted as these cells have many features of previously published CXCL12 abundant reticular cells (CAR cells). Along these lines, the Morrison group described Lepr+ perivascular stromal population back in 2012 (Ding et al.). In 2014 Zhou et al., again from Morison's group, demonstrated that Lepr+ cells gave rise to adipocytes and osteoblasts. In 2019 both Baryawno et al. (Figure 2C) and Tikhonova et al. (Sub Figure 4A) reported that a Lepr-high mesenchymal population expresses high levels of Adipoq, Cxcl12, Lpl, etc. Validation of previously published data using Adipoq-Cre-TdT system does not substantiate a discovery of a novel population. Furthermore, Lepr-high cells are pericytes, which by definition are cells that wrap around the endothelial cells, and maintain homeostasis of blood vessels. The authors should better relate their findings to these previous studies, and clarify if "MERA" cells are equivalent to CAR cells or a specific CAR cell subtype. The term "MERA" should be dropped unless they clearly demonstrate why this is a previously unreported population.

3) The authors used Monocle and Slingshot to infer the ancestor of adipocytes and osteoblasts. They identified markers Sca1, Cd34, and Thy1 specific to that population. As correctly state those tools are used to infer differentiation trajectory and without convincing functional biological data MSC identification is an overstatement and should be greatly toned down. Can the authors identify Sca1+CD34+Thy1+ population by imaging? What is the location of that MSC population relative to the bone marrow? The authors should also reanalyze their datasets with UMAP-based dimensionality reduction to redefine the position of this 'MSC' cluster as tSNE is not considered a good way to visualize inter-cluster relationships. An updated version of Seurat and Monocle has this function readily available in the package. In addition, the authors might consider avoiding the use of the term "MSC" to describe cells in vivo. MSC is a historical term largely used to describe in vitro cultured cells.

4) The authors should more carefully validate the specificity of Adipoq-CreER. This line could accidentally mark 'MSCs' as defined in their scRNA-seq analysis. Further, as pointed out by the authors, this line also labels subcutaneous adipocytes, which can exert non-cell autonomous effects on bone formation. The study using the same Adipoq-Cre; DTA 'fatless' mice showed that circulating adiponectin and leptin released by subcutaneous adipocytes negatively regulate bone formation (Zou et al., 2019). The authors should highlight the caveats of this study better.

5) The definition of pericytes and stromal cells of this study is not accurate. The authors use the term pericytes to refer to the entire perivascular stromal cell populations. The general consensus is that pericytes specifically refer to a subset of perivascular stromal cells surrounding small arteries, arterioles. What they refer to as pericytes in this study are reticular cells surrounding sinusoidal vessels. Pericytes and perisinusoidal reticular cells have different morphologies and functions. The authors should clarify the characteristics of Adipoq-Cre labeled cells in the revised manuscript.

6) Rather than disputing the Aifantis and Scadden annotations, a suggestion would be to correlate their clusters in a more balanced way with these previous studies.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Single cell transcriptomics identifies a unique adipose cell population that regulates bone marrow environment" for consideration by eLife. Your article has been reviewed by three peer reviewers, including J Gage Crump as the guest Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Clifford Rosen as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Iannis Aifantis (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

The reviewers agree that this is a beautiful manuscript that details a number of novel computational and biological findings that fit well to a number of closely related datasets. While the majority of issues have been addressed in this revision, I ask that you address the following concerns before we can formally accept your manuscript.

1) The reviewers all agree that use of the term MSC is problematic, especially given the lack of direct lineage data supporting the Sca1+ population behaving as stem cells in this study. The term "MSC" should be dropped and replaced by a more neutral term such as "mesenchymal progenitor". Perhaps "early mesenchymal progenitor" and "late mesenchymal progenitor" and stress that early/late refers to interpretation of scRNA-seq analysis rather than direct lineage tracing. Discussion of these populations as "stem cells" should also be removed throughout the manuscript.

2) Some additional language highlighting similarities of MALP cells to previously reported CAR cells should be provided.

3) The simple lineage diagram provided in the response letter (Author response image 1) would be good to include in the main Figure 1. I would also suggest using LiLA instead of Ad to denote mature adipocytes in Figure 1 and beyond.

4) I would show Author response image 2 in the paper – potentially as supplementary data. This is a nice image and confirms the presence of rare Sca1+ cells. However, not essential to include if authors feel otherwise.

5) Subsection “Single cell transcriptomic profiling of bone marrow mesenchymal lineage cells”: better to say "unlikely" rather than "very unlikely".

6) Should not say "mature adipocyte-specific Adipoq-Cre reporter" as data clearly suggest it labels a broader population. It would be better to introduce use of this Cre given the ability of Adipoq to label a broad population of stromal MALP cells. Rather than referring to previous publications saying Adipoq-Cre is a mature adipocyte marker, a more agnostic view should be taken as to what this Cre actually labels.
