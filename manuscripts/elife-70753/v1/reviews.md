# Peer review - Round 1

Editors:
- Bérénice A Benayoun, University of Southern California United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70753.sa1](https://doi.org/10.7554/eLife.70753.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

Garrido-Gomez et al., generate a unique dataset profiling the transcriptomes late-stage endometrium of women with prior pregnancies leading to severe preeclampsia (sPE) compared to that of non-preeclamptic pregnancies. Although the question of molecular drivers preeclampsia has been explored at the molecular level directly in the placenta, this study provides a unique view in the endometrium of women years after the pregnancy in question, which is consistent with the fact that a previous preeclamptic pregnancy is one of the best predictors for a subsequent preeclamptic pregnancy.

Decision letter after peer review:

Thank you for submitting your article "Disrupted PGR-B and ESR1 signaling underlies preconceptional defective decidualization linked to severe preeclampsia" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Kathryn Cheah as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Although the 3 reviewers noted the potential of the study, major concerns were raised about the soundness/clarity of the transcriptomics analysis, as well as lack of clarity on the study population. Specifically:

1. The manuscript needs to undergo major revisions in the statistics and transcriptomics analyses (see specific points with details in reviewers 1 and 2 comments):

a. The use of fold-change thresholding needs to be removed/updated.

b. Multiple hypothesis correction needs to be used prior to determining significance with genome-wide datasets. Please use FDR correction or other accepted methods.

c. Only use Student t-tests when data normality can be confirmed, otherwise, use non-parametric tests.

d. Since this study is done on endometria sampled years after actual pregnancy, it would be crucial to compare to public datasets on actual placentas, to determine overlap and differences.

e. PCA cannot be used to determine clustering or lack thereof, as well as whether differences exist or not.

f. There are concerns about batches and co-variates not taken into account (see reviewers 1 and 3 points) which could lead to the absence of DEGs. These need to be clearly stated and provided in a table. They also need to be corrected for, either using batch removal and/or multivariate modeling.

g. A continuous GSEA-type analysis would be more informative than a thresholded approach for functional enrichment (i.e. GO) analysis.

h. RT-qPCR (especially on the exact same sample set) is not an appropriate validation for robust RNA-seq datasets.

2. The authors needs to substantially revise and improve the details on methodology (i.e. RIN threshold), as well as deposit all code and data to public databases for re-analysis. This is crucial for long-term reproducibility and use of this as a resource. Analytical choices against the general rule of the field (such as using hg19 and not the more recent better annotated hg38) should be justified or at least explicitly addressed.

3. The patient population needs to be better defined (see reviewer 3 points, and to a lesser degree reviewer 1).

4. Make sure to define all abbreviations, and avoid using non-standard abbreviations to improve readability.

Reviewer #1 (Recommendations for the authors):

1. There are major concerns about the statistics in the analysis of the dataset.

a. Fold-change thresholding is used in multiple places in the analysis (e.g. line 94, 112, 128, etc.). This is a big problem, as it is known to lead to poor FDR control in the case of statistical tests not designed to take fold change into account (like edgeR used here). Thus, the practice of fold-change filtering without FDR control is considered problematic by statisticians (see PMID: 19176553). Thus, either the authors need to update their results after removing this problematic criteria to properly control for FDR, or all analyses should be rerun with a method that takes fold-change into account for FDR control (e.g. the TREAT method PMID: 19176553).

b. For the GO enrichment analysis (line 133), the authors only indicate a p-value filter (p < 0.005). Was there not implementation of multiple testing correction? The data should be re-analyzed after proper multiple hypothesis correction control (native DEseq2 FDR, Bonferroni, or other). In addition, what was the gene list background used to compute enrichment? The nature of the background has been shown to hugely impact results and needs to be explicitly detailed in the methods.

c. The authors reports using Student t-tests (section starting line 404). Unless normality is proven (e.g. with a Shapiro-Wilkes test), parametric tests that relie on normal distributions should never be used. We recommend that all tests be rerun with non-parametric equivalents (e.g. Wilcoxon or Mann Whitney) to guarantee these assumptions are not violated.

2. With human sample studies, it is unlikely that all samples were processed exactly in parallel (i.e. all samples collected the same day, kept in stabilizer for the same amount of time, etc.), which all but guarantees the existence of batch effects. There are also a number of stated parameters (i.e. age of the donor, time since pregnancy 1-8 years, day in cycle 22-32, etc.) that could influence results without a relevant biological driver.

a. In addition to an aggregated table (Table 1), the authors should generate a table for each anonymized sample for key characteristics so that the resource can be analyzed with these caveats considered both in this current paper and to facilitate all future reanalysis attempts. This should include for each sample individually:

i. age of the donor.

ii. time since last pregnancy.

iii. day of cycle for biopsy.

iv. date of processing/batch (including biopsy batch, library batch AND sequencing batch).

v. RIN of RNA sample.

vi. Sequencing depth (raw reads per library).

vii. Percent reads mapping to the genome reference (here hg19).

viii. Ethnicity of donor.

b. The authors should implement a multivariate model to account for all these potential confounding effects so as to focus on the core biological signal. In addition, the use of a software like SVA or RUVseq is recommended to remove unwanted technical variation prior to analyses.

3. Additional methodological information is needed for long-term reproducibility of analyses.

a. For reproducibility of code and analyses, all analytical code for this study should be deposited in a repository such as Github or made available as a Supplementary file.

b. Please include all version numbers for all used software (e.g. R, etc.) packages and R packages (e.g. edgeR, goana, etc.), as well as all command parameters where relevant. The same should be applied to annotation databases (i.e. GO used here), and if a version number doesn't exist, date of access should be provided.

c. There is no mention of the softwares (nor versions) used to trim RNA-seq reads, to map to the hg19 genome or to aggregate counts to genes. All used software should be clearly named and their use described with all necessary options for reproducibility.

d. Line 84-88/Figure 1A, were the subtypes of "control" samples (pre vs. full-term) equally distributed in training vs. testing? Indeed, although the authors argue that the subtype made no difference on transcriptional profiles (i.e. Sup Figure 1A PCA), this reviews sees a general (if not clean separation) on PC1, that would probably be enhanced if sources of spurious variation (see point #2) were taken into account. In any case, the data provided cannot be used to support the statement "demonstrated an absence of clustering" (line 80), since the statistical tests used are not meant to prove the null hypothesis but to reject it when possible (i.e. confusion between type I and II error). Please amend the analysis to reflect this.

e. cDNA library cannot be validated for RIN (line 330), as only total RNA samples can be. The entire method section needs to be completely rechecked and rewritten for accuracy to avoid this kind of errors.

f. All used QC filters should be stated explicitly in the methods (see lines 338-342).

4. Since RT-qpCR is known to be less sensitive and more prone to normalizing biases (due to the choice of control genes which may vary themselves) than RNA-seq (which performs unbiased normalization at the transcriptome-wide level), it is unclear why validation was performed on the same samples that were processed by RNA-seq (line 375-389). Unless the authors want to include RT-qPCR data on an INDEPENDENT cohort of patients, these results are circular and shouldn't be included in a revised manuscript. If RT-qPCR on a new cohort is included, make sure to include information on which normalizing amplicons were used for δ CT calculation.

5. Can the authors explain why 3 specific samples (C20, 21, 22; line 147-152) do NOT cluster appropriately with their "signature"? Did they have any biological specificities (see need for sample-by-sample information as raised in point #2)? The fact that 3 control samples cluster with the sPE samples somewhat invalidate the signature as a signature of sPE, and may be the result of improper correction for batching or other technical (or irrelevant biological) noise. Please discuss explicitly what may be happening here in a revised manuscript.

Reviewer #2 (Recommendations for the authors):

In sum, I feel that this paper brings some interesting insights on the decidua status and preeclampsia; the degree of novelty is nevertheless unclear to me, and the clinical application seems far-fetched. There are several points that may be better presented and discussed.

Detail of the recommendations to the authors:

1. The study of the decidual transcriptome in preeclampsia has also already been performed by other teams in the past, rather at the moment of the disease than later. For instance, the paper of Mari Loset (Am J Obst Gynecol, 2011), is, I feel, an important base for comparison with the results presented here. So much so, that it used the same type of expressional approaches, and detected differential transcripts and cascades. I feel that the authors should analyze their own datasets in light of this type of seminal papers and discuss the commonalities and differences found.

2. In the overrepresented pathways in the Loset's work, the regulation by ESR1 and PGR was not obvious. Does it mean that analyzing samples 3-4 years after the event (normal or pathological pregnancy) leads to remnants of the disease at the uterine level, or is there a genetic predisposition? This is a question that cannot be truly addressed by the present dataset, and is important if the objective is to define markers, as stated below.

The introduction gives the necessary details to understand the question raised, finding a signature that could help assessing the risk of preeclampsia.

3. However, the genetic part of preeclampsia is estimated by a heritability of ~55%. The genetic decomposition of this heritability presented by Cnattingius and coworkers (2004) indicate that only part of this genetics is connected to the maternal genetic background (which concerns two organs: the uterus and thus the decidua) and the placenta for half of its genetics. Part of the genetics of preeclampsia is associated only to the paternal genetics (estimated at ~1/3 of the heritability), therefore, it is clear that the risk cannot systematically be found by analysis of the female (uterine-decidua) expression profile only. Alternatively, the difference observed by the authors may be a consequence of the previous preeclampsia not based on a predisposition, but if this is the case, it limits considerably the usefulness of the markers found since preeclampsia, and in particular severe preeclampsia is at 75% a disease of the first pregnancy. The authors should recognize this as an important limit as an early prenatal screening strategy.

The initial analysis is based upon the endometrial tissue of 24 women that had a severe preeclampsia, 16 controls (8 preterm and 8 term births). Gestational age at delivery had apparently no influence on the 'control' groups. Since the samples were not collected at the end of gestation, which means that the occurrence of preterm may be connected to the placenta and not to the maternal uterine situation.

4. Nevertheless, there are only 8+8 samples so it is not possible to prove that in some case a decidual expression is not involved. In addition, using PCA to check that there is no clustering is not enough to certify that there are no differentially expressed genes that separate the two groups, it means only that the number of differential genes compared to the mass of genes that are not differentially expressed is not enough to cluster the groups, which may be the case if the percentage of genes changed is small. There are some published evidences that recurrent spontaneous abortion, pre-term birth and preeclampsia share common mechanisms. The observation here seems to indicate that the uterus of women with PTB is identical to the one of term pregnancies. From the clinical data, the authors acted wisely in taking PTB without hypertension. But it is not clear from the data that the women that had PTB had a recurrent occurrence in this (not mentioned in Table S1).

5. In addition, the absence of DEG genes visible (Supplementary Figure 1B) is presented against FDR and not p-value which is unusual and I think a bot too stringent. Even random samples should give some significant genes (one out of 20) Using FDR leads to no significant genes, which is not a complete surprise. However, it does not mean that individual genes are not relevant for the difference between the two situations analyzed. Another interesting approach should be to check for enrichment of pathways using GSEA approaches, that do not rest on the establishment of thresholds that are always arbitrary. In sum excluding totally the existence of DEG between the two groups seem a bit rapid.

6. In the legend of Suppl figure S1, I do not understand 'Plot based on 728 genes labeled as fc (blue) and 17,748 genes labeled as none (purple)'. Nevertheless, it is admissible that the differences due to preterm or term are negligible compared to the differences induced by sPE.

The decomposition of the samples between sets for simulations is unusual in the field, but mathematically sound. The authors discovered 859 DEG at a threshold of 2-fold, and some genes (9) were validated by qRT-PCR.

7. It would be nice to analyze the data not only relative to a threshold of induction, but taking the complete dataset and using GSEA-like approaches to see whether they are consistent with the gene clusters found by threshold-volcano plots analyses.

Previous studies by the authors evaluate gene expression differences in decidualization either from human endometrial stromal cells (hESCs) from women with sPE versus normal. The authors identified 18 genes differentially expressed in vivo and in vitro in sPE compared to control.

8. The authors do question the observation of having only 18 common genes between in vivo and in vitro, out of 129 or 859 (in vitro – previous study- and in vivo -present study- respectively), and base them upon cell composition that is much more complex in vivo, which is reasonable. However, in the search for a signature, which is one of the justifications of the work, it could mean that the in vivo dataset could contain more 'relevant' genes compared to a in vitro model. The comparison with the results of Wang, which is much better (and focused better on a simple cell model) on the single-cell transcriptome may belong rather to a discussion rather than a results part of the paper. The validation by qRT-PCR is good, but the choice of the genes leads to a very high correlation (2D), that may be due to the use of only one induced gene (and only 5 genes used). About the actin as a control housekeeping gene, it is not sure that it is the best reporter gene in the uterine context. Generally, it is advised to normalize against the geometric mean of two to four different reporter genes.

A selection of 166 highly deregulated genes (>4 fold) is then selected, and were shown to be enough to separate efficiently the samples, which is not surprising, given that this corresponds to a semi-supervised analysis from genes found differential between the two gene sets.

9. The identification of Estrogen/progesterone receptor is not a surprise, when uterus function is concerned. I would suggest that the authors complete their analyses using network analyses such as provided by the combination of Stringdb and Cytoscape. This would help to visualize the pivotal position of ESR1 and PGR more clearly, or maybe to find other important hubs that were overlooked in their current study. Also using GSEA or other tools on transcription factor binding sites databases, showing the actual involvement (through measuring the enrichment, and calculation of FDRs) of the Estrogen Responsive Element and Progesterone Responsive Element would be an essential element that must be shown to prove a genuine enrichment in these cascades

Reviewer #3 (Recommendations for the authors):

There is much debate on whether the risk of PE is higher/lower in women with male vs. female fetuses. Additionally, the maternal response to pregnancy differs based on the sex of the fetus. The manuscript should therefore report on this variable and whether it impacts the results of the analysis.

Please clarify whether biopsies were done for clinical or research purposes only.

Why did the authors choose to use hg19 as their reference genome and not the better annotated hg38?

Methods (line 321) – What RIN value was defined as appropriate for making RNAseq libraries.

I cannot find anywhere where DD is defined. Can the authors please clearly define what they mean when they use DD?

Introduction – PE also significantly contributes to maternal mortality, not just infant.

Figure 3B – what is the axis label?

Figure 4 – I believe the authors mean sPE (not Spe).

Data availability: authors state that the RNAseq data is available for download in GEO.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Disrupted PGR-B and ESR1 signaling underlies defective decidualization linked to severe preeclampsia" for further consideration by eLife. Your revised article has been evaluated by Kathryn Cheah (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Essential revisions:

The authors failed to properly respond to key reviewer concerns, which were considered to be necessary changes by the consensus of reviewer's discussion. Thus, the manuscript cannot be further considered until these points raised by the reviewers are appropriately addressed.

1. The editor and reviewers understood the method used for fold change thresholding. No additional explanation was required. The method is still wrong, as post-FDR fold-change thresholding is the problem that was raised and cannot be used in a rigorous analysis. Thus, the authors should implement one of the previously given options so that this major problem is corrected: (i) get rid of fold-change thresholding completely, or (ii) use a method that does it, while appropriately controlling for FDR (e.g. TREAT).

2. Similarly, using multiple corrections for GO and KEGG analysis is not a suggestion but a necessity for rigorous analysis, especially when performing so many tests. If term redundancy is a major concern for the authors in the GO database, they are advised to look at the GOSlim framework which was put together to specifically respond to this concern. In any case, enrichment results without FDR control are non-reproducible and not statistically supported.

3. The authors have not responded to the requirement to upload all code/scripts generated for the study. They refer to the software repository (i.e. edgeR), but not the actual code for analysis. The specific scripts that were written to run all analyses need to be made available as well on GitHub or as a supplement, as per eLife policy.
