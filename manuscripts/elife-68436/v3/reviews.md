# Peer review - Round 1

Editors:
- Murim Choi, Seoul National University Republic of Korea

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68436.sa0](https://doi.org/10.7554/eLife.68436.sa0)

The study described an extremely rare type of adrenal pheochromocytoma that secretes both ACTH and CRH, in addition to catecholamines. Single-cell RNA sequencing of the tumor and other tumors revealed a group of cells that are responsible for the hormone secretion. We believe that this work will provide an interesting example of functional endocrine tumors and how they are formed.


---

# Peer review - Round 1

Editors:
- Murim Choi, Seoul National University Republic of Korea

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68436.sa1](https://doi.org/10.7554/eLife.68436.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your work entitled "Single-cell transcriptome analysis identifies a unique tumor cell type producing multiple hormones in ectopic ACTH and CRH secreting pheochromocytoma" for further consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Mone Zaidi as the Senior Editor.

Reviewer #1:

The authors identified an extremely rare case of ATCH-dependent Cushing syndrome due to ACTH&CRH secreting pheochromocytoma. They retrieved sugically resected samples from the tumor and subjected them to scRNA-seq, which led them to identify a group of cells that are double-positive for ACTH&CRH. They then performed a series of expriments to confirm that the cells are indeed present in the tissue, and attempted to identify genes that may lie upstream of the process.

Perhaps the most important point of the study is the identification of the double-positive (DP) cells from the patient. However, evidence supporting this observation is relatively scarce other than showing a cell cluster that express POMC, CRH etc (as displayed in Figure 3A, C). Gene expression pattern shown in Figure 3C supports that the DP cells share molecular characteristics with those of pheochromocytes. But in the t-SNE plot, these cells are located far from pheochromocytes in PHEO_T. Rather, the DP cell cluster seems to be branched out from immune cells. If I didn't read the t-SNP plot wrong, I wonder why the identity of DP cells is closer to the immune cells. Also, it needs to be clarified if the DP cells could be doublets? The authors did not show basic statistics and QA/QC data of the scRNA-seq experiment (as supplementary data for example). They should show that the DP cells are not technical doublet cells.

Another critical question would be what is the genetic driver that induces expression of both hormones in the DP cells? They propose GAL, but the evidence supporting its direct role is not strong and remains speculative.

Comments for the authors:

Overall, this study requires more carefully designed expriments and interpretation. Otherwise, it remains as a descriptive study with vague conclusions, leaving the uniqueness of the sample being the only strength of the study.

1. Colors in Figure 3A are confusing.

2. Figure 5 does not add much to the molecular mechanism. Rather it merely describes physiological consequences by the presence of DP cells. Please consider strengthen or remove it.

3. Isn't Figure 7B a duplication of Figure 3B?

4. IHC data in Figure 3E, F lack negative controls. And the readers need additional markers to be guided of its anatomical location.

5. Figure 4 compared DEGs between DP cells and other tumor cells. Since the cell groups that were being compared are too different, observing such dramatic differences is not unexpected and hard to coin physiological relevance. Wouldn't it be more meaningful to compare them to pheochromocytes?

6. The pseudotime analysis in Figure 6 does not answer the question of how the DP cells originated. It should be performed in a such way to suggest genes that marks critical points during the pseudotime branching or proceeding.

Reviewer #2:

In this manuscript Zhang et al. generated single cell RNA sequencing data for the adrenal gland tumors including extremely rare type of tumor, ACTH & CRH-secreting pheochromocytoma. Unbiased clustering analysis discovered a unique tumor cell type that expresses multiple hormones unlike normal adrenal gland cells and other tumor cell types that produce a single hormone. By comparing with other type of tumor cells, they identified specific marker genes of the novel tumor cell type. They also revealed the distinct immune and endothelial cell populations in the microenvironment of different tumor samples.

Although the gene expression profiles of novel cell type can be utilized to reveal the molecular mechanism of this rare tumor associated with Cushing's syndrome, the data was generated from only a single patient and have not validated in other samples. In addition, the results only provide the list of genes that were specifically expressed in the novel tumor cell type and their potentially related biological pathways, but not detail molecular and cellular characters of the cells. The single cell gene expression profiling data are definitely useful for the researches.

Comments for the authors:

I have several concerns and suggestions, which if addressed would improve the manuscript.

1. The major finding of this manuscript is the presence of multi-functional tumor cell type which produce multiple hormones such as POMC, the precursor of ACTH and CRH. But, this finding was only derived from a single sample and experimentally validated using the same tissue. I understand the sample is very rare, but could the authors validate the result in different tumor samples at least using IHC or IF? If sample is not available, the limitation of the study should be mentioned.

2. Please consider providing full list of marker genes that were used for cell type annotation.

3. Figure 3C does not seem to support the statement "We demonstrated that GAL was expressed in the ACTH+&CRH+ pheochromocyte and 'regulated the secretion of ACTH'".

4. The authors identified a unique and important multi-functional cell type but current analyses (differentially expressed genes identification and gene ontology analysis) seem insufficient to characterize molecular feature of ACTH+&CRH+ pheochromocyte. The authors could perform additional comprehensive analysis such as SCENIC analysis in order to identify the master transcription regulator of the cell type.

5. The pseudo-time analysis indicated that sustentacular cells transform to ACTH+&CRH+ pehochromocytes and then to pheochromocyte. The authors utilized Monocle3 in which user has to define the starting points. The authors can validate the result using RNA velocity analysis which also predicts cell transition without the need of prior knowledge about starting point cell type.

6. Given the diverse immune and endothelial cell type in the tumor microenvironment, it would be interesting to perform the cell-cell interaction analysis using the programs such as CellPhoneDB to see if they have distinct regulatory role in different tumor microenvironment.

7. How did the authors define the four subclusters of endothelial cells? Please consider providing list of marker genes.

8. In the method part, how did the authors determine different criteria for the maximum number of genes (no more than 5000, 3000, and 2500 genes for PHEO, ACA, and esPHEO samples, respectively)?

Reviewer #3:

Zhang et al. perform single cell RNA sequencing (scRNA-Seq) of one rare ACTH+CRH-secreting phenochromocytoma (3 anatomically distinct sites from the tumor and one peritumoral site), one typical pheochromocytoma, and two typical adrenocortical adenomas.

Their main findings are as follows: (1) They identify a unique cell type, which they term ACTH+CRH+ pheochromocyte, which appears to be the tumor cell present in the rare ACTH+CRH+ tumor (2) Marker gene analysis reveals that while known adrenal chromaffin markers (CHGA, PNMT) are present in both pheochromocytes and ACTH+CRH+ pheochromocyte, the latter has some unique markers such as GAL and POMC. They validate the marker genes with IHC. (3) Profiling of the non-tumor populations reveals distinct immune microenvironment profile and endothelial cell profile to the rare tumor compared with classical pheochromocytoma and adrenalocortical adenoma.

The main strength of this manuscript is that it involves single-cell profiling of an exceptionally rare tumor type and a distinction from the more common adrenal tumors (pheochromocytoma and adrenocortical adenoma). The broader implication of the authors' findings is with respect to Dale's principle, which states that a given neuron releases only one type of neurotransmitter. However, in the case of this tumor, single cell analysis clearly shows that ACTH, CRH, and chatacholemines are being released from the same cell. This is quite interesting and significant. The data will also potentially be valuable to others in the field for analysis in future studies.

There remain some unanswered questions – namely:

(1) What is the cell in normal physiology that gives rise to this ACTH+CRH+ pheochromocytoma?

(2) Do conventional phenochromocytomas differ from the ACTH+CRH+ pheochromocytoma in terms of the cell of origin that is transformed, or in the spectrum of genetic alterations that result in transformation?

Comments for the authors:

Overall, I think this study is of broad interest given the rarity of this tumor type. My comments to the authors to improve the manuscript are as follows:

1. Given how rare the ACTH+CRH+ pheochromocytoma is, I think the study would be substantially strengthened if the authors could perform DNA sequencing (WGS or WES) and describe how, if at all, the genomic landscape differs from conventional pheochromocytoma.

2. Can the authors comment on whether the hypothesis is whether the ACTH+CRH+ pheochromocytoma originates from a rare progenitor cell that is distinct from the chromaffin cell giving rise to pheochromocytoma? If so, can the authors stain a panel of normal adrenal glands with some of their marker genes to try and identify this cell in normal tissues?

3. While the tumor type is interesting for its rarity, the analysis performed is quite standard and comes across as a bit superficial in parts. Although it is understandable that the authors have only one ACTH+CRH+ sample I think they can do more with the data and this would significantly strengthen the manuscript. For example, it would be interesting if the authors can point to specific master regulatory factors that drive the distinct programs in pheochromocytes vs. ACTH+CRH+ pheochromocytes. The immune microenvironment analysis, while inherently descriptive, is also somewhat superficial.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your revised article "Single-cell transcriptome analysis identifies a unique tumor cell type producing multiple hormones in ectopic ACTH and CRH secreting pheochromocytoma" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Murim Choi as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Mone Zaidi as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Although the reviewers thought that many issues were addressed, they still concerned on the superficial analysis results. Nonetheless, they agreed that the manuscript contains a common interest for publication in eLife as the tumor is an extremely rare case. Please address reviewers' concerns below.

Reviewer #1:

Although the authors could not address all the questions, especially regarding the origin of DP cells and genetic driver for DP cells, it appears reasonable that they are hard to address as the tumor sample was extremely rare.

Reviewer #2:

Although the authors have satisfactorily addressed most of my points, there are remaining concerns about RNA velocity data.

Please cite any reference for the statement "For the high proportions of unspliced/spliced transcripts, stem-like characteristics of sustentacular cells were supported." Can global ratio of unspliced/spliced transcripts support stem-like characteristics?

Please elaborate Figure 5 C-F. Currently, they don't seem to add any information.

Reviewer #3:

In the revised manuscript Zhang et al. have included additional data and analyses including more exhaustive QC, RNA velocity analysis, regulome analysis, and have performed WES of the ACTH/CRH-secreting pheochromocytoma. They have generally addressed my technical concerns from the prior review. I maintain that the analysis remains somewhat superficial and descriptive in parts and this may be somewhat of a missed opportunity to more deeply explore the underlying biology of this unique case, understanding the caveats of its rarity. Nonetheless, I think a description of this tumor at single-cell resolution and availability of the dataset is of value to the scientific community.

However, I would like to see a more careful analysis of the WES data prior to publication. I do not see any basic metrics (mutation rate etc.), description of pathogenicity filtering/annotation, or copy number analysis. The mutations shown are primarily missense and I do not really see any obvious driver genes – how many of these are putative driver vs. passenger mutations? ACAN is mentioned, but what is its significance, if any? The somatic landscape should be discussed in comparison to typical phenochromocytomas and adrenocortical carcinomas, which have been more extensively sequenced. If there is no obvious genetic driver of this ACTH/CRH-secreting phenochromocytoma, that should be stated. If the claim is that ACAN alterations are somehow related to this tumor type, that needs to be substantiated. Or if the implication is that ACAN is a passenger alteration, that needs to be stated explicitly also.
