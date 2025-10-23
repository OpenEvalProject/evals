# Peer review - Round 1

Editors:
- Paul W Noble, https://ror.org/02pammg90 Cedars-Sinai Medical Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71008.sa0](https://doi.org/10.7554/eLife.71008.sa0)

The authors aim to show that fibroblasts have a heterogenous transcriptome that is retained throughout their lifetime due to their source of embryonic origin. Of great interest is that compelling evidence is provided that these transcriptional signatures have direct translational consequences. This is shown through coculture experiments, where coculture of cardiomyocytes with non-cardiac fibroblasts impairs integration and contractility, while cardiac fibroblasts integrate with cardiomyocyte cultures to create functional beating tissue. This memory is shown to be malleable: three days post implantation in the renal capsule, explanted fibroblasts largely maintained their original transcriptomic signature, while also showing the onset of adaptation to a new microenvironment. In addition, markers are identified which allow the separation of fibroblasts based on their anatomical origin. Considering the lack of tissue-specific markers for fibroblasts, this is a significant advance.


---

# Peer review - Round 1

Editors:
- Paul W Noble, https://ror.org/02pammg90 Cedars-Sinai Medical Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71008.sa1](https://doi.org/10.7554/eLife.71008.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Adult fibroblasts retain organ-specific transcriptomic identity" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Paul Noble as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Reviewer #1 (Recommendations for the authors):

The manuscript has strengths in: Figure 7 transplant data were strong; The authors have provided extensive data; Functional confirmation in cardiac lineage was very convincing. The recommendations are:

1. Verification and gene list. A weakness in the initial gene analysis is there are so many genes and pathways mentioned and used (Figure 2a) that it is difficult to determine why the genes in Figure 2 (b-g) were the ones chosen to be validated. The qPCR validation seems to support the hypothesis that these genes have organ specific expressions but their selection (top gene? Specific pathway node? Candidate gene?) from the initial analysis is unclear. It would help to simplify the schematic for Figure 2a and highlight the specific genes that are being validated. This is further compounded by the figure 3 data, which shows mixed results (PAX8 does not really seem to be expressed in the kidney and FOXD1 seems to have an odd pattern of expression; FOXA2 seems to be expressed in some nuclei and not others of the lung) and non-direct comparison between multiple organs.

2. The clusters of the scRNA-seq from both freshly isolated and cultured fibroblasts seem to be due to the batch effects, as it is not very possible that not a single overlapped cell was identified. The listed organ specific genes in heatmaps were hand-picked? as they are identical. Are there any specific genes between fresh isolated and cultured fibroblasts in each organ? A better suggestion should be listing all the shared maker genes and organ specific genes in both freshly isolated and cultured fibroblasts and discussing a little bit the possible related functions.

3. Immunocytochemistry validation should also include the staining on the negative fibroblasts to confirm the "organ specific markers" in Figure 3. More convincing staining experiments should be on the sections of freshly isolated organs with proper and necessary controls.

Reviewer #2 (Recommendations for the authors):

The reviewer has some comments on the data presentation, analysis and overall experimental approach that are listed below:

Data presentation:

1) Figure 6i: -LOG(p-value) should be underneath of the X-axis. It does not make sense to show pathways that are not significant, i.e. -LOG(p-value) < 1.3.

2) Figure 5 —figure supplement 1 and Figure supplement 2 are confusing. Figure5 – S1 shows mainly lung, and Figure 5 – S2 shows heart, and it is not clear why both figures also have some data on the kidney.

Analysis:

1) The authors have added single-cell profiling of fibroblasts from the published mouse dataset (Han et al. 2018). However, it would have been more informative to include instead published datasets on human fetal and adult tissues, as these datasets for the heart, kidney and lung are available.

2) Why was microarray and not RNA-seq has chosen to perform gene expression analysis? It is much better to have RNA-seq data instead of as it makes datasets easier to compare with other published datasets.

Experimental approach:

1) The authors used cultured fibroblasts to avoid contamination from parenchyma cells. However, this approach is not ideal, especially because the authors report that cultured cells present an activated/myofibroblast-like phenotype compared to freshly isolated cells. It might also be helpful to describe more in-depth the activated phenotype upon culture compared to freshly isolated cells. Are these get downregulated upon ectopic transplantation?

2) Tissue-specific functionality of fibroblasts in vitro (3D cardiac tissue function) and in vivo (ectopic transplantation) are performed after just 3 days, which might be not sufficient to reveal more differences or similarities. It might be interesting to have these compared to a prolonged period upon co-culture or transplantation, such as three weeks. The reviewer also finds it surprising that the authors observe the change in HOX genes expression as early as 3 days after transplantation, as one would think this should take longer.

Reviewer #3 (Recommendations for the authors):

The authors provide a well-written and comprehensive study of the positional "memory" and specialization of fibroblasts. As such, I have only minor comments. Please find below my part-by-part comments to the manuscript.

Abstract

The final sentence of the abstract does not fit with the narrative of the paper, it is too much of a future perspective.

Discussion

Buechler et al. (Nature, 2021) defined in their fibroblast atlas two universal fibroblast populations, from which tissue-specific fibroblasts appear to be derived. The present manuscript does not provide such a cell type: rather than a continuum of states, discrete organ-specific cell states are found. The authors should comment on this discrepancy. Furthermore, the discussion should integrate the present findings with those of Buechler, who touches upon the concept of spatial fibroblast heterogeneity, making the manuscript a direct extension of his findings.

Line 409 seems like an overstatement, as the concept of fibroblasts as a cell type is not at stake here. Rather, the definition of cell state might require an amendment, taking into consideration anatomical location or the local microenvironment to which a cell is exposed.

Figures

The added value of Figure 1 is lost to me. It does not provide much information and would in my view better be suited for the supplements. Regarding Figure 1, lines 108 to 110 can be removed. The statement that is it surprising for a cell type designated mainly as ECM-producing to be rich in transcripts for nuclear and cytosolar proteins is confusing and should therefore be omitted. A cell's primary function does not mean that transcripts related to that function should by default make up the majority of the transcriptome.

Why are averaged raw signals used in Figure 2, rather than normalized expressions?

Figure 5 contains two clusters which cannot be linked back to the organ of origin. Perhaps regressing out the genes of the Hox cluster and the cell cycle can solve this issue?

Figure 6j is missing the cardiomyocyte signature in the Tbx20 KD, while it is the positive control.

Figure 8c does not have a legend. In 8d it would help to move the word 'FDR' next to the legend's color scale.

Results

The first subtitle mentions metabolic components. As these were part of larger gene sets, such as housekeeping, the cytoskeleton, proliferation, this word should be substituted by e.g. homeostatic. No metabolic profiling was performed.

The description of population "KidneyA" in lines 217 to 221 aims to explain a relatively higher expression of genes related to in the response to injury, linking this to tubular cells acquiring mesenchymal phenotypes in vivo. Considering the relative size of the cluster, this seems unlikely to me. It would be of interest to generate a module score for the genes associated to the collagenase-response described by O'Flanagan et al. (Genome Biology, 2019) and test if this cluster is not simply a group of fibroblasts with a stronger reaction to the enzymatic digestion. This can be done easily in Seurat v3 using the AddModuleScore() function.

Line 276: the use of the abbreviation 'HF' for heart failure is not defined. Considering that the abbreviation eHF is coined a few lines earlier to refer to heart fibroblasts, this leads to possible confusion.

Materials and Methods

Lines 493 and 610 mention 10cm dishes, which I believe should be 10 cm² dishes.

Lines 488 and 607 do not mention the basal medium in which the digestion took place.

Line 491 does not state the percentages of sodium pyruvate and pen/strep in the medium.

Line 493 contains a typo in the TrypLE.

Line 541: "log2 transformation and quantile normalization was done using R scripts and public Bioconductor packages". This is too vague to be reproducible, please elaborate and cite the packages used for the analysis.

Line 578: a citation of edgeR is missing (Robinson, Bioinformatics, 2010).

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Adult mouse fibroblasts retain organ-specific transcriptomic identity" for further consideration by eLife. Your revised article has been evaluated by Paul Noble (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Please address the batch effect issue as outlined by reviewer #3 as it impacts the significance of the findings.

Reviewer #1 (Recommendations for the authors):

The new version of manuscript has satisfactorily answered my concerns.

Reviewer #2 (Recommendations for the authors):

The authors have addressed all my comments, and I have no additional comments.

Reviewer #3 (Recommendations for the authors):

The authors have adequately addressed most of my comments in both the revisions and their responses. One issue which does persist in my opinion, and which is also mentioned by Reviewer 1 is the grouping of the cells in the scRNA-seq analysis. From a biological perspective at least some overlap would be expected in an analysis only including one cell type. However, there is a very strong separation based on organ, highly resembling a batch effect. In their response to Reviewer 1, the authors mention this could not be possible as all samples were sequenced in the same 10x lane. I believe that by this they mean the same 10x chip, as running 8 samples in the same lane would require additional multiplexing. Regardless, even within the same chip, some technical variation can be expected between lanes.

On this topic the authors also refer to figure 6 of the Mouse Cell Atlas (MCA) paper, but this does not make sense as different dimensionality reduction methods were used between these two papers. The MCA uses tSNE projection, which prioritizes finding local communities, while in this paper UMAP was used, which focuses preserving the global structure of the data. A side effect of the mathematical differences between these methods is that intercluster distance does not have much meaning in tSNE space, but reflects variation in a UMAP projection. Consequently, separation by organ in a UMAP projection as seen here does indeed support the claim of the manuscript. However, the strong separation of samples derived from the same organ (e.g. the two kidney samples) undermines this reasoning, as it implies the presence of a batch effect aiding in the separation. This is not sufficiently addressed by the authors.

– The caption of Figure 2 says b-g, while this should be b,c.

– Figure 7 is labelled a-i, l-m. The panel letters should be updated.
