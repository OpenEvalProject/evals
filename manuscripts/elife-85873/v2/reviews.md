# Peer review - Round 1

Editors:
- Murim Choi, https://ror.org/04h9pn542 Seoul National University Republic of Korea

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85873.sa0](https://doi.org/10.7554/eLife.85873.sa0)

This paper represents a valuable single-cell level analysis of tendon enthesis development. The study allows further understanding of this specific process with clinical implications. The authors provided convincing evidence for the heterogeneity of postnatal enthesis growth and the molecular dynamics and signaling networks during enthesis formation.


---

# Peer review - Round 1

Editors:
- Murim Choi, https://ror.org/04h9pn542 Seoul National University Republic of Korea

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85873.sa1](https://doi.org/10.7554/eLife.85873.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Single-cell RNA sequencing reveals cellular and molecular heterogeneity in fibrocartilaginous enthesis formation" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Murim Choi as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Xiao Chen (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Although the editors and reviewers agreed that the work is valuable, it needs further improvements to warrant publication in eLife. Major issues are:

1) The paper should be discussed relative to the results in Fang et al., Cell Stem Cell, 2022.

2) The importance of P7 as a critical differentiation timepoint is not well supported.

3) Validation is needed (e.g., IHC and/or FISH) for many of the scRNAseq results (e.g., CellChat pathways).

Reviewer #1 (Recommendations for the authors):

1. The results and their novelty should be discussed in comparison to the recent Cell Stem Cell study describing enthesis development using scRNAseq and lineage tracing approaches (https://doi.org/10.1016/j.stem.2022.11.007).

2. Figure 1d: The PCA for histomorphologic parameters (which typically have high variations) does not show any meaningful separations or groupings. I do not agree with the authors' conclusion that this analysis reveals P7 as a critical developmental timepoint. In general, PCA may not be appropriate for this data set.

3. According to the methods, it appears that the entire humeral head-supraspinatus tendon was used for cell isolation for scRNAseq. This results in the inclusion of cells from bone, growth plate, enthesis and tendon. As such, only a very small percentage of cells came from the enthesis, as is clear from the cell clusters in Figure 2b and 2c. This is a flaw in the approach; inclusion of such a wide range of cells makes interpretation of "enthesis" cells difficult, as described in more detail in the comments below.

4. The differentiation/pseudotime analysis described in Figure 3 is difficult to follow. I do not think it is useful to combine cell transcriptomes from vastly different tissues and then define a velocity map. There is too much varied information for the algorithm to create valid connections, as the there will be many many branches/paths from mesenchymal stem cell to osteoblast, tenocyte, chondrocyte, etc. Presumably, embedded in these maps are trajectories for osteoblast differentiation, chondrocyte differentiation, tenocyte differentiation, etc. There are too many layers of overlapping information to deduce anything meaningful for the small number of cells associated with the enthesis.

5. The authors uses the term "function" throughout the paper (e.g., "functional definition of fibrocartilage subpopulations"). However, this is a descriptive study, and "function" (or mechanism) can only be theoretically inferred from the various algorithms used to analyze the data. A role for any of the pathways or processes can only be defined with gain- and/or loss-of-function studies.

6. "C2 highly expressed biomineralization-related genes (Clec3a, Tnn, Acan)". The three example genes are not related to biomineralization.

7. The functional characterization of the three enthesis cell clusters is not convincing. For example, activation of metabolism-related processes is a vague result than can mean a lot of things (including changes in differentiation), yet the authors interpret it very specifically as " role in postnatal fibrochondrocyte formation and growth".

8. The pseudotime analysis of the enthesis cell clusters is not convincing. The three clusters are quite close and overlapping on the UMAP. Furthermore, the authors focus on Tnn as a novel and unique gene, yet the expression pattern shown in Figure 5g implies even expression of this gene across all three clusters.

9. The TC1 markers (Ly6a, Dlk3, Clec3b) imply a non-tendon-specific cell population. Perhaps a tendon progenitor pool or an endothelial cell phenotype is more appropriate.

10. Pseudotime analyses assume that your data set includes cells from progenitor through mature cell populations. It is unclear that the timepoints studied here included cells from early progenitor states.

11. The CellChat analysis is not useful, as the authors included 18 cell types. The number of possible interactions among so many cell types is enormous, and deducing valid connections between any two cell types in this case is questionable.

12. The authors should validate their key scRNAseq results with in situ hybridization. Only a single gene, Tpp, was validated on tissue sections. This validation is particularly important for this study because the authors included a wide variety of tissues/cells in their isolation and analyses.

13. The authors should demonstrate functional necessity of at least one gene/pathway identified by the scRNAseq analyses (e.g., through gene knockout).

Reviewer #2 (Recommendations for the authors):

1. As known, Fei Fang et al. have established single-cell transcriptomes of mouse supraspinatus tendon enthesis cells (Cell Stem Cell, 2022). It is suggested that the authors introduced Fei Fang et al.'s work in Introduction and emphasize the significant novelty compared with Fei Fang et al.'s work.

2. In Figure 1, the authors highlighted P7 was a critical stage for enthesis differentiation. But this section was less associated with the following content. The authors should link these results with the scRNASeq data. Is there any time-dependent change/signaling in scRNASeq data at this critical time point?

3. In the H and E staining of Figure 1A, the tendon structure was separated and random. It is suggested that the authors provide high-quality staining figures.

4. Figure 2 showed that the Scx+ or Sox9+ cells was decreased in enthesis over time. At least it should be co-staining to show the distribution and frequency of double positive and single positive cell populations. However, a previous study has demonstrated this finding (PLOS ONE, 2020). It is suggested to verify some new findings by IF or IHC staining.

5. There are some conflicts about trajectory analysis. In Figure 3C, RNA velocity showed that the arrow flowed from BTJ to MTJ and CTFb. However, in Fig3d, PAGA plot indicated that BTJ cells is independent of other cells. Furthermore, in supplementary figure S3, RNA velocity showed that the trajectory flowed from TC to BTJ. These figures were inconsistent with the described results. Please provide detailed explanation to avoid misleading readers.

6. Figure 5 showed that C1 was the original cluster, and whether C1 cluster expressed canonical progenic/stem cell markers.

7. The authors performed cell-cell interaction based on cellchat analysis. But the cell-cell interaction was not actively examined.

Reviewer #3 (Recommendations for the authors):

1. Fang et al. (A mineralizing pool of Gli1-expressing progenitors builds the tendon enthesis and demonstrates therapeutic potential. Cell stem cell. 2022) defined enthesis cell transcriptomes and differentiation trajectories, and identified Gli1+ progenitor population for enthesis. Please further clarify the innovation of your research, and in depth introduction or discussion is needed to compare and contrast the results between the two research.

2. In Figure 1, more evidence are needed to prove that Neonatal to postnatal day 7 (P7) is the critical stage for enthesis fibrocartilage cell differentiation, for example, immunofluorescence staining or qPCR for enthesis fibrocartilage cell makers, instead of relying on H and E only.

3. Line123. Figure 2e showed that the expression of Clec3a and Col2a1 were low in c4," which were ubiquitously expressed in bone-tendon junction cell (c4)" seems to be an inexact expression.

4. Line 117, which cell clusters belong to "fibroblast-associated cells"?

5. Line 125, it is better to co-staining the scx and Sox9 to validate the existence of BTJ cells. Scx and Sox9 are known markers of BTJ, do you have find new makers for BTJ by scRNA-seq?

6. Line 148, "stemness" degree? Are there other evidence, such as stem cell maker expression, to show that "growth plate cells and fibroblasts associated clusters are higher than other cell types". The expression of "stemness" seems exaggerated.

7. There is no description of figure 4b in the results.

8. In figure 5, 2-3 makers identified by scRNA-seq for fibrocartilage formation are suggested to be validated by immunofluorescence stainning or other methods, instead of only proving the Tnn expression in postnatal BTJ growth.

9. There are no verification of the signaling network for the enthesis postnatal growth which were revealed by Cellchat. It is suggested to validate the key signaling, such as Bmpr2 signaling.
