# Peer review - Round 1

Editors:
- Oliver Stegle, European Molecular Biology Laboratory, European Bioinformatics Institute United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.57345.sa1](https://doi.org/10.7554/eLife.57345.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript describes an in vitro system to study inter-individual variation of transcriptional and epigenetic responses to hypoxia using iPSC derived cardiomyocytes. Changes in gene expression are found without changes in chromatin accessibility or methylation, providing insight into key questions about the necessity of epigenetic changes for changes in gene expression. It also identifies regions of the genome responsible for context dependent-changes in gene expression.

Decision letter after peer review:

Thank you for submitting your article "Dynamic effects of genetic variation on gene expression revealed following hypoxic stress in cardiomyocytes" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Patricia Wittkopp as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Senior Editor has drafted this decision to help you prepare a revised submission.

Both reviewers agree that this manuscript is in principle appropriate for publication in eLife without any further experimentation; however, they both also raise a number of concerns about the data analysis and presentation that would need to be addressed satisfactorily before we can consider this work further. Although the typical practice for eLife is to provide authors with a single consolidated review, I felt it would be more beneficial in this case to provide the two reviews as is. They are generally consistent and both explain why they recommend the changes they do in detail.

Reviewer #2:

1) The authors present the range of cardiomyocyte purity. However, I think it would be helpful for this data to be presented in a table. Further, how do the purities correlate between the individual at different time points collected? Could some of the eQTLs identified really be a result of the variation in purity of the differentiations? Investigation and results regarding this possibility would be helpful if included in the manuscript.

2) The inferences made in this paper about the identification of dynamic eQTLs (and their absence) for a given loci rests on the assumption that the power to detect an eQTL is the same in every cell-type by condition. This is addressed in subsection “Dynamic eQTLs are revealed following hypoxia”, where it is clearly show (and acknowledged) that this is not the case. To avoid this problem the authors chose a lenient secondary cut-off at the point where p-values deviate from uniformity. Firstly, it would be helpful to formally test for deviation of uniformity here (rather than appearance on a graph). More importantly, utilising the same p-value threshold when the distribution of p-values is different will lead to variation in the false positive / false negative rates between conditions. This would lead to bias in the identification of dynamic eQTLs, as variation in eQTL detection is a function of the FP/FN rates. Can this be addressed, and it clearly demonstrated that the comparison between conditions is based on the same ability to detect a true eQTL?

3) In subsection “Dynamic eQTLs are revealed following hypoxia”, the authors state that the genes that were not eQTLs in any condition were uniform. However, the figures suggest significant skewing to more significant p-values. Please test for the uniform distribution with a chi-squared test. The authors suggest that they would expect the eQTLs identified in one condition to be uniform in another condition. This relies a the huge assumption that the largest contributing factor to significant eQTLs in each condition is the condition itself, not the cell type and that there will not be a significant number of eQTLs that are consistent across all conditions. However, the authors have provided no evidence to support this claim or this assumption. Please provide the requisite evidence to support these claims and assumptions.

4) Related to this, in paragraph three, it is indicated that based on the FDR calculations, half of the dynamic eQTLs that they identified are not truly dynamic. However, given this is the main conclusion of the paper, it really would be beneficial if some additional work could be done to ascertain the true from false dynamic eQTLs. Particularly if this work is going to be used for any translational research. One option would be to create a null distribution of the effect sizes for genes in each condition and test for enrichment of the "dynamic eQTLs" across the different conditions to test demonstrate whether they are actually identifying truly dynamic eQTLs. Further, I think different FDR cutoffs would have been more appropriate for identifying truly dynamic eQTLs since that is the main focus of the manuscript.

5) The analysis of the GTEx and GWAS overlap is unclear and would benefit from some more careful explanations. Reading this section, I had the following concerns:

i) How were the 14 tissue types randomly selected? And why not include all GTEx tissue types?

ii) How was overlap between dynamic eQTL and GTEx eQTL determined? Many eGenes are regulated by different eQTL – was the overlap based ona. Rank test of p-values between datasets for example? That would help provide confidence it is a true shared effect rather than unlinked eQTL.

iii) Are the allelic effects in the same direction?

iv) Why perform two stage comparison between eQTL and GWAS variants from all traits, then cardiac traits? Was multiple testing corrected for?

v) How do you rule out whether the overlap is just by chance, pleiotropy, linkage, or a causal relationship? These different scenarios have significant impact on the conclusions that are drawn. As it currently stands, it is implied that the overlap is a shared causal relationship.

6) One of the premises of this work is the statement made at the end of paragraph one of the Introduction, where the authors conclude that because the majority GTEx eQTLs are shared across tissues, they probably do not contribute to disease in tissue-specific manners. However, this statement makes two significant assumptions that are not addressed. 1) They assume that the downstream effects and signalling are the same regardless of cell type given they have the same eQTL. However, because different genes and pathways are activated in different tissues, this assumption may not hold true across all tissues. 2) They ignore the ascertainment bias associated with large additive cis-eQTL (which are more likely to overlap between tissues). The mean proportion of expression h2 that can be found to overlap between tissues is 0.02 (2%) in GTEX. The assumption that the remaining 98% are shared between tissues isn't supported by evidence from trans-eQTL mapping or single cell eQTL analyses. In my opinion, clarifying this statement in the Introduction as justification for the work would be beneficial.

7) I found that manuscript in general to be difficult to read and easily interpret the analysis conducted, and conclusions based on specific results. I would suggest a careful eye on editing a review would be very helpful. But here are a few points that I noted specifically

i) The notation used for supplementary figures and tables presented as "Figure X – Supplement Y". It would help to refer to the supplementary figures as "Supplementary Figure X" instead.

ii) Subsection “Dynamic eGenes are enriched for response genes and transcription factors” – it is not always entirely clear whether the authors are referring to transcription factor genes or transcription factors regulating the genes. You could include the word "gene" following "transcription factor" throughout the paragraph.

iii) Defining clearly what response genes and why they are important.

iv) Subsection “Potential limitations of our model” states that the power analysis indicates a 6% power to detect 38% heritability. Firstly, I assume, but it is not clear, that the test is against H0: h2=0? I understand the maths behind this, but that seems a really odd way of explaining power. Why not give a power curve?

v) How are the genomic features tested for enrichment of DARs?

vi) Subsection “Genomic features associated with differentially accessible regions (DARs)” paragraph two and Discussion paragraph four are confusing and unclear. It is hard to understand what the has been done.

vii) Throughout the manuscript, it is difficult to identify which timepoint were used for each assay. Please clarify this when introducing a new assay. Altering Figure 1 to make this clear graphically would help as well.

8) Some of the RIN numbers in RIN table are very low (i.e. 0 for 18852 in condition D). It's not clear if these samples were included in the analyses, but if they were some justification is needed. I worry about impact on the analysis, as essentially it would induce bias in those samples.

9) The section "DNA methylation levels are largely stable following hypoxia and re-oxygenation" is confusing and difficult to read. It is first stated that no DMCpGs were identified and then later stated that they were identified.

10) In subsection “Chromatin accessibility changes following hypoxia and re-oxygenation”, it is stated that ATAC-seq reads were selected that did not show allelic mapping biases. However, later testing for differential accessible regions. This filtering step would remove the ability to effectively identify differentially accessible regions with this step. Could you please either explain the reasoning for removing allelic mapping biases at this step, and/or explain why it would not impact differential accessibility analyses downstream.

11) It is concluded that the data indicate that the "underlying DNA sequence features can affect their epigenetic profile". However, I do not think that the results demonstrate this. They only demonstrate differential methylation in differentially accessible regions which are themselves not associated with genetic variants. I would suggest altering this sentence by removing "that the underlying DNA sequence features of these regions can affect their epigenetic profile"

Reviewer #3:

The authors established an in vitro system to study inter-individual variation of transcriptional and epigenetic responses to hypoxia using iPSC derived cardiomyocytes. Despite the modest sample size, they discovered more than a thousand eQTLs in total, of which 367 are dynamic eQTLs modulating the transcriptional response to hypoxia with implications for disease susceptibility.

Although the analyses demonstrated in the manuscript are solid and the results are reliable, authors failed to present their results effectively. I would recommend the authors to rewrite the paper to increase the accuracy and readability in general (as I suggested below).

In addition, I have one particular concern regarding the following important (but vague) claim presented in this paper, that is the transcriptional response to hypoxia is not mediated through epigenetic changes. Although the authors repeated the claim multiple times throughout the paper, it is hugely confounded by the power to detect epigenetic variations between conditions/individuals (i.e., DARs, caQTLs and DMCpGs). If the authors would keep the claim, they need to address the power issue appropriately.

Here are my specific comments:

1) Figure 1A should explain the overview of the experiment in more detail. There are three replicates for the three of 15 donors (mentioned in the main text) which are hidden in the panel. It is also nice to combine panel A and D in one panel to illustrate the whole experiment. According to the main text, one donor was dropped in ATAC-seq and two donors were dropped in methylation data which should also be shown in the panel.

2) It would be nice to summarise the 4 x 21 RNA-seq samples in the main figure. The authors used a linear mixed model for differential expression (DE) analysis. I'm wondering if the model can be used to perform a variance components analysis to decompose the total variance (for each gene) into “condition”, “individual”, “replication”, and residual variances (where the condition and replication are also treated as random effects). The estimated variance parameters across all genes are then summarised by a boxplot or similar where the residual variance is standardised as 1.0. The authors could repeat the analysis for ATAC-seq and methylation data to compare the difference of explained variances between molecular phenotypes. The analysis will provide clear interpretation on why detectable DARs, caQTLs and DMCpGs are so few. The similar analysis was performed e.g., in (Kilpinen et al., 2017).

3) Figure 2H is not so informative. Instead, the authors could extend the heatmap in Figure 2F to show how much of eGenes are classified into baseline eGenes, dynamic eGenes and shared eGenes by showing all genes with eQTLs at least in one condition. The authors could also add additional columns next to the heatmap showing which eGenes are response genes and/or transcription factors to support the enrichment analysis in the section “Dynamic eGenes are enriched for response genes and…”.

4) The DE analysis result is frequently used in the manuscript, but there is no summary data shown in the main text (e.g., volcano plots, DE genes shared/not shared with different conditions, etc.). It would be ideal to have an independent figure for DE analysis. Currently, Figure 2A-C are the result of DE analysis which are inconsistent with the figure title (i.e., “Hundreds of dynamic eQTLs are revealed…”).

5) How many dynamic eGenes are overlapping with the baseline eGenes? The Chi-square test performed in the section “Dynamic eGenes are enriched for response genes and transcription factors” seems inappropriate because the authors double-count the same genes in baseline eGenes as the background distribution. They need to subtract dynamic eGenes from the baseline eGenes to perform a proper Chi-square test.

6) The authors performed the enrichment analysis of transcription factors (TFs) in dynamic eGenes which could be confounded by response genes, because dynamic eGenes are likely to be response genes. In addition, even if dynamic eGenes are enriched with TFs, what is the biological interpretation? Why do regulatory variants affect TF dynamic eGenes more than non-TF dynamic eGenes?

7) It is often the case that the main figures are used to show anecdotal examples of biological statements raised in the main text and important data/results are hidden in the supplementary figures. The main figures must be used to support the author's claims in general (without cherry-picking an example gene). For example, the authors stated “most DARs have returned to baseline levels of accessibility by the first re-oxygenation condition.” with just numbers of DARs and the FOXO1 example which do not strongly support the claim. The authors should perform and highlight global analyses to support each claim from different angles. In fact, the claim was partly supported by the supplementary figure 3 (supplement 4A-C). Therefore, the authors first consider rearranging the figures to better support each claim made in the main text. Then, they can clarify which analysis is needed to make a strong statement.

8) The statement “These results suggests that gene expression changes…” was supported only by a limited number of DARs and not totally addressed yet. Recently, the “gene activity score” was proposed in the single-cell ATAC-seq analysis to overcome the sparseness of chromatin data (Granja et al., 2020). I'm wondering if it improves the power to detect DARs in the paper. This quantification also allows the authors to easily colocalise DARs with eGenes/response genes to prove (or disprove) the statement.

9) It is very surprising that CHT found only tens of caQTLs, while it mapped more than a thousand eQTLs. The authors should comment on that. If the authors use only variants overlapping with the accessibility region, does the power to detect caQTL increase? It seems 25Kb cis-region is too broad.

10) The statement “Changes in DNA methylation are therefore…” is hugely confounded by the power to detect DMCpGs with the higher noise rate in DNA methylation arrays. It is not conclusive with the modest sample size.

11) The authors should perform a colocalisation analysis (Giambartolomei et al., 2014) if GWAS summary statistics are available. If not, the authors are still able to calculate linkage disequilibrium (LD) between the GWAS lead variant and eQTL lead variant from CHT to make sure the GWAS locus and the eQTL are reasonably colocalised. The authors should show locuszoom plots in conjunction with boxplots in Figure 6 to demonstrate both the magnitude of statistical significance of eQTLs and LD (r2 index) with GWAS lead variants.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Dynamic effects of genetic variation on gene expression revealed following hypoxic stress in cardiomyocytes" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Patricia Wittkopp as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

As stated by the reviewers in response to the first submission, the paper presents a timely, interesting and relevant advance. The initial comments raised have been largely addressed, however both reviewers continue raise concerns regarding the eQTL and GWAS overlap / colocalization analysis. We agree that these concerns are fundamental and should be addressed.

First, concerning the overlap with GTEX (R2), it seems entirely doable to perform this analysis on the level of individual variants, which also permit assessing consistency of effect directions, etc.

Second, both reviewers comment on the GWAS overlap/colocalization analysis. While we acknowledge that the resolution to definitely identify colocalization events will be limited, the authors should extend their analysis and/or town down the conclusions. The approach proposed by reviewer 3 seems sensible and viable, at least for a selected set of loci.

For reference, we have also included the complete reviewer reports.

Reviewer #2:

The authors have addressed most of the comments raised, although there are a couple of points that I feel would be beneficial to investigate further.

1) GTEX overlap – in the original review, a suggestion of testing for concordance of allelic effect direction be shown for the replication of the eQTL identified in this work and GTEX tissues. It is unclear what “analysis at the level of the gene” exactly means, but given that many genes are controlled by independent eQTL (loci) in difference tissues/cell types, overlapping an observation of eGenes doesn't allow conclusions of shared eQTL to be determined. Testing for the concordance of allelic effects for eSNPs identified from your analysis with GTEX eSNP results would provide much stronger evidence to support this conclusion.

2) GWAS overlap – "We next chose to analyze the data using a less stringent gene-based approach using GWAS traits of interest. The second analysis allows for the identification of potentially interesting regions where the causal SNP may be different in the eQTL and GWAS data" I am not sure what this means biologically and what conclusions can be drawn from this. What does it mean if there is no overlap in the SNPs between a eQTL and GWAS loci but that they are both in the same gene region? Is there an enrichment over what would be expected by chance? the statements "We did not mean to imply that the overlap is a shared causal relationship. We have changed the language to reflect this. Our goal is to illustrate that the dynamic eQTLs we identified may play a role in higher-level phenotypes." These sentences seems in opposition to one another.

Reviewer #3:

The authors have now addressed most of my questions and concerns. Yet, the result of GWAS colocalisation is still in question. I have previously suggested to perform a proper colocalisation analysis using COLOC package or to report the linkage disequilibrium index (r2 value) between GWAS index variant and eQTL lead variant. Unfortunately the authors just provided only P-values for associations which does not support the GWAS locus and eQTL are colocalised. The authors have to expand the cis-window (up to 1Mb) for a handful number of genes overlapping with GWAS loci to perform a proper colocalisation analsysis. It is crucial to provide the posterior probability of colocalisation for such a small number of GWAS overlapping genes.
