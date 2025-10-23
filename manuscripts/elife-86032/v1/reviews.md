# Peer review - Round 1

Editors:
- Paul R Barber, https://ror.org/0220mzb33 King's College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.86032.sa0](https://doi.org/10.7554/eLife.86032.sa0)

This study represents a valuable body of work in which the authors assemble a molecular description of colorectal cancer and a classification into subtypes. Overall, the evidence supporting the findings is solid, and consensus over a diverse range of data from publicly available sources is convincing. When added to existing knowledge this work may contribute to future biomarker discoveries for colorectal cancer.


---

# Peer review - Round 1

Editors:
- Paul R Barber, https://ror.org/0220mzb33 King's College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.86032.sa1](https://doi.org/10.7554/eLife.86032.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Comprehensive characterization of tumor microenvironment in colorectal cancer via histopathology-molecular analysis" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Tony Ng as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

We consider it essential that the following points are addressed in the revision, but also please consider all recommendations from the reviewers below, and refer to them for further details on these essential points:

1) Please comment on and show evidence for the robustness of the derived 4 classes (C1-C4).

2) Comment on the degree of intra-patient heterogeneity of CCCRC subtypes.

3) Please be explicit about why gene sets were chosen, and their completeness in the context of CRC, and any overlap between them.

4) Clarify why clinicopathological covariates were not included.

5) Clarify the derivation of the single-sample gene classifier, specifying exactly the genes considered and in the final classifier. Please make sure the final classifier is available.

6) To support the main claim that the CCCRC classification can facilitate biomarker discovery, please comment on how best to combine the CCCRC classification together with existing (and future) classifications, to achieve this aim.

Reviewer #1 (Recommendations for the authors):

Thank you for your manuscript. Here are my specific suggestions.

In Figure S1 A and B, better labels are required. Both seem to be labelled as TCGA. There are open circles that are not labelled.

Lines 142-144 – Sentence needs expansion. The "prognostic ability" of the signatures was evaluated. The "signatures associated with stromal and tumor compartments significantly correlated".

Line 152 has the only use of the term "TME panel scores", we presume you mean the signature scores?

Line 242 contains the first mention of the TCGA-CRC cohort, please reference the supplementary methods.

Line 642, please use "20X magnification" and "40X magnification", not "20 magnification" or "magnifications".

Line 349, "dominate" should be "dominant"?

Line 1134, I believe this is an UpSet plot, not a Venn plot. (Alexander Lex, Nils Gehlenborg, Hendrik Strobelt, Romain Vuillemot, Hanspeter Pfister. UpSet: Visualization of Intersecting Sets IEEE Transactions on Visualization and Computer Graphics (InfoVis), 20(12): 1983--1992, doi:10.1109/TVCG.2014.2346248, 2014.)

Figure 6C, D PFS/OS legend is the wrong way around.

Line 429, Please clarify where the filtered list of 81 genes came from.

Lines 452-462, Describe a single-sample gene classifier based on the CRC-RNAseq data with training and a hold-out set. It is also not clear if the 80 gene set was input to the model training or if the final gene list was.

Line 458: "The gene classifier based on the xgboost algorithm is publicly available at https://github.com/XiangkunWu/CCCRC" but the link does not contain the classifier nor the final list of genes. It has the code used but not the classifier itself. Please upload the classifier in a form that others can use.

Reviewer #2 (Recommendations for the authors):

– How robust is the clustering to the choice of clustering method and the choice of gene lists? For example, could the authors comment on what would happen if one of the "tumour cell" signatures is left out, given that "Energy" appears to be a relatively strong component of C2 and C3 for both CRC-AFFY and CRC-RNAseq?

This is important to expand on, at least as a Discussion point, because the CCCRC clustering (Figure 1) is a foundational part of this work, and the rest of this paper is structured around these definitions.

– Given that the 61 gene signatures appear to clearly separate CCR-AFFY and CRC-RNAseq into 4 clusters using the presented method (Figure 1A), could the authors comment on why the CCCRC and CMS subtypes were not more similar to each other (Figure 1G)? Is there a component captured by (or driving) CCCRC which is not captured by CMS, and vice versa?

– In addition to the summary in Fig1G, it would be helpful if Figure 1A heatmap was also annotated with CMS and MSI annotations, reordering the samples within each CCCRC cluster if necessary.

– The completeness (or otherwise) of the gene lists chosen for the gene panel should be made more explicit. To what extent is the chosen gene panel likely to represent the components of CRC tumour-associated immune cells, tumour cells, etc? Does the panel of gene signatures capture all the biological differences previously described between CMS subtypes, e.g. TGFb activation; WNT and MYC activation; others?

– What is the overlap in samples between CRC-AFFY and those used for the development of the CMS classification, and/or the original papers which fed into the CMS? Are all of these cohorts similar to each other, or overlapping? Was there a similar balance of subtypes and clinicopathological variables? This would help the reader to understand all possible sources of the difference between CCCRC and the current consensus CMS.

– Please clarify why clinicopathological covariates were not included in the OS and PFS models (Figures1, 4-6). For example, left-sidedness, KRAS or BRAF mutations, MSI; e.g. see Guinney (2015) Table S13.

– Fig1I: "Forest plot of multivariate Cox proportional hazard regression analysis of PFS after adjusting for TNM stage and CMS subtype in the CRC-AFFY cohort." – is this intended to mean that CMS was a covariate? If yes, why?

– The discussion comparing the reported predictive or prognostic value of CCCRC subtypes (this work) and CMS subtypes (published) could be expanded. For which endpoints did the CMS subtypes (published) have superior or similar separation than the CCCRC classification (this work), and does this affect the biological interpretation of each classification scheme?

– The claims "the C4 subtype was suitable for ICB treatment" and "significance of CCCRC in guiding the clinical treatment of colorectal cancer", and any similar phrases about guiding treatment, need to be rephrased; this is a pre-clinical study.

– To support the main claim that the CCCRC classification can facilitate biomarker discovery, can the authors comment on how best to combine the CCCRC classification together with existing (and future) classifications, to achieve this aim?

– Could expand the Discussion on whether/how this "holistic" CCCRC classification might contribute towards understanding the heterogeneity in treatment outcomes seen in different CRC trials (e.g. FIRE-3, COIN, CALGB/SWOG 80405).

Reviewer #3 (Recommendations for the authors):

The authors' title "histopathology-molecular analysis" suggests the manuscript includes an emphasis on the investigation of histopathological parameters. Whilst the authors do examine the relationship between histopathological analysis of specimens with CCCRC subtypes this features as a minor aspect of the study which largely focuses on large-scale investigation of transcriptional signatures.

Figures1C, 2C, 3B and 4E – pvalues on plots illegible

Methodology for tumour evolution patterns needs comment/expansion – I could not identify this in the current methods.

Comment on the degree of intra-patient heterogeneity of CCCRC subtypes would be nice. A significant degree of overlap between immunosuppressive and immune excluded, and proliferative and immuno-modulatory signatures in Figure 1A is apparent and should be commented upon.

The addition of a spatially resolved RNA seq dataset (likely available from Nanostring of 10X genomics Visium platforms) would be nice to see the distribution of CCCRC subtypes within each patient.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Comprehensive characterization of tumor microenvironment in colorectal cancer via histopathology-molecular analysis" for further consideration by eLife. Your revised article has been evaluated by Tony Ng (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

1) Please remove the word "histopathology" from the title since that analysis was not a major driver of the results.

2) The limitations of the study have been added as requested. Could you please add a Limitations paragraph in the Discussion, to summarise all the study's limitations in one place.

3) Please add to the limitations paragraph that the removal of single signatures at the clustering stage was not evaluated. From the Response (page 13): "Since the effect of removing one of the TME-related signatures on the clustering results was not well evaluated, we attempted to remove the entire category."

4) Statements about clinical decisions still remain, for example:

Line 753: "The CCCRC classification system may facilitate clinical treatment decisions."

Line 757: "We demonstrated the suitability of C4 for immune checkpoint therapy".

and in other places.

Given the study limitations, all such statements should be toned down.

e.g. "in future … may contribute to.. subject to further work.. in combination with other classification systems.."
