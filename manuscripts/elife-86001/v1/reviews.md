# Peer review - Round 1

Editors:
- Bérénice A Benayoun, https://ror.org/03taz7m60 University of Southern California United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.86001.sa0](https://doi.org/10.7554/eLife.86001.sa0)

In this study, Li and al describe valuable insights into mechanisms underlying sex-differences for diet-induced obesity in mice, demonstrating a role for macrophage-derived RELMa secretion in determining female-specific obesity protection. They provide evidence for the impact of RELMa signaling in eosinophil recruitment for diet-induced obesity protection in female mice. Single-cell RNA-seq analysis of the stromal vascular fraction of control and RELMa deficient animals were used to investigate molecular mechanisms underlying the protection. The conclusion of these findings provides evidence supporting dysregulation of cell differentiation pathways.


---

# Peer review - Round 1

Editors:
- Bérénice A Benayoun, https://ror.org/03taz7m60 University of Southern California United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.86001.sa1](https://doi.org/10.7554/eLife.86001.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Sexual dimorphism in obesity is governed by RELMα regulation of adipose macrophages and eosinophils" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Shlomo Melmed as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Sarah R. Ocanas (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

After consulting together with the reviewer, we believe these are the essential revisions required to support the claims in the manuscript:

1. Increased clarity/details in the methodology, specifically in the processing and analysis of the scRNAseq dataset (including parameters, batch correction method, and immediate availability of code) [Rev 1 and 3].

2. Better discussion of why eosinophils could not be detected [Rev 1 and 3].

3. Trimming down conclusions from introductions and results, make it clear what is directly supported and what is conjecture [Rev 1, 2 and 3].

4. Check of mutilplexing/demultiplexing, since a top-regulated gene in females, Gm47283, is Y encoded [Rev 3]

Reviewer #1 (Recommendations for the authors):

1. The nature of the t-SNE analysis provided in Figure 2 is not well explained. What is the input data? How is the clustering performed? How are cell types annotated in the analysis? In general, neither the text nor the figure legend gives a good description of the content of Figure 2 in its current state.

2. There is a general lack of details on the analytical strategies and methods, especially computational methods, that is not acceptable for the evaluation of results and long-term reproducibility. The authors need to provide extensive additional information about used bioinformatic tools and/or analyses.

a. The authors give only very generic text about using "standard" data processing, which does not inform about specific algorithm choices for analysis. For instance, the authors mention using batch correction but do not specify the algorithm used (or its parameters). The pipeline for CMO deconvolution is also not described and needs to be described, especially for any future reanalysis of the data. In addition, the version of R, and all versions of R packages should be provided as well (e.g. monocle), as this can impact the final results. There is also no mention of which test was used to identify markers in Seurat, and how the tests were set up. Thus, it is crucial that the method section be revised to include all necessary information for readers to evaluate and reproduce the bioinformatics analyses of the scRNA-seq data.

b. Although a functional enrichment analysis is mentioned in the text [lines 230-232], there are no details about the algorithm used for enrichment beyond the name "shinyGO". Is this a hypergeometric enrichment or ranked list-type algorithm? What version of the GO database was used, and was it the 3 domains of GO? What background gene list was used to compute enrichment? All this information needs to be explicitly included. A supplementary table with all enriched terms would also be invaluable.

c. The code availability section uses language to say that the code is generic, following established tutorials. Since there are always choices made in the R implementation of a pipeline with a specific dataset (in terms of parameters), this is not acceptable for reproducibility or peer-review evaluation. In addition, it seems like different sources had to be used since batch correction is mentioned as well. For long-term reproducibility, it is crucial to either deposit all R scripts that were used to a public repository such as GitHub or provide it as a supplemental archive to accompany the manuscript. A reference to standard pipelines is not compatible with the methodological review.

d. The methods provide no description of the infection paradigm used to harvest eosinophils.

e. The authors do not provide any information about the time of day of euthanasia of animals, which impacts many phenotypes (including immune phenotypes) due to circadian rhythms.

3. Granulocytes, including eosinophils, are notoriously RNA-poor, and it has been established by 10xGenomics that special adjustments to the protocol (specifically, increased amplification of cDNA) are required for captured [https://kb.10xgenomics.com/hc/en-us/articles/360004024032-Can-I-process-neutrophils-or-other-granulocytes-using-10x-Single-Cell-applications-]. It would be important to discuss the RNA-poorness of these cells in the section discussing with eosinophils were not captured (lines 280-283), as this is more likely the reason for lack of capture over limited transcriptional identity or degranulation.

Reviewer #2 (Recommendations for the authors):

While we generally find the manuscript well written and well organized, there are some comments and concerns below we would like to share to help improve the manuscript:

Figure 1E: Small animal cohort size and large standard deviation in data. The figure would be strengthened by adding additional animals to improve the sample size.

Figure 1G: Differences in immune cell populations don't seem to correlate well with cytokine/chemokine expression (1E). Can classic cytokines known to increase during obesity like TNFa, IL-6, and IL-1b be looked at more carefully to better understand how the loss of RELMa influences their expression?

Figure 2A. Please state clearly in the body of the manuscript that this is flow cytometry data. This was not obvious from reading the text.

Figure 2E: Switch CD206 (main figure) and CD301 (supplementary).

Figure 2F: What is the significance of higher Siglec-F expression by eosinophils? please elaborate further on why this is important.

Line 206: It would be more proper to say M1-like macrophage, a classic M1 macrophage is defined by stimulation with LPS, and multiple papers over the years have shown CD11c+ macrophages in HFD models do not express classic M1 macrophage genes (PMID: 25242226).

Figure 4D-F does not seem to be representative flow plots based on the data graphed below. Recommend choosing a flow plot that represents the median of the graphed data.

Consider merging figures 5 and 6, as they are both limited in scope.

Figure 7a: Is the annotation able to differentiate fibroblast vs pre-adipocytes? Also in the Figure to the right of the TSNE plot, it is hard to determine the sex and genotype of these mice. Please draw groups on the x-axis like in 7C.

Reviewer #3 (Recommendations for the authors):

Below is a point-by-point critique to aid the authors in understanding specific points from the public review.

Title – We recommend including "in young mice" as part of the title.

Introduction – We believe that the introduction could benefit from editing down. Some of the details would be more appropriate for the discussion. Conclusions from the scRNA-Seq analyses will need to be updated after correcting the analyses.

Results – An experimental design figure prior to Figure 1 and Figure 4 would be helpful to the reader.

There are several instances in the text where the authors claim that there is a significant difference between the two groups, but the statistics for these comparisons are not shown in the figure.

– Line 97-98 – "Under both Ctr and HFD conditions, female mice had significantly higher RELMα in the serum and visceral adipose tissue than males (Figure 1A)." – It does not appear that there is a significant difference in RELMa within the female visceral fat under HFD.

– Figure 1B – Why was a t-test used for this figure when there were four groups to compare? Were any comparisons made between the Ctr groups? In the text (lines 100-101), it states "RELMα 101 deficiency did not affect Ctr or HFD weight gain in males…"; however these statistics are not described in the legend or text.

– Lines 107-108 – "The monocyte chemoattractant CCL2 was significantly elevated in HFD-males…" – Was this statistic assessed? It is not shown in Figure 1C.

– Lines 111-12 – "The higher level of IL-10 and GM-CSF in females were dependent on RELMα and were further decreased with exposure to HFD…" – In figure 1E, the effect of HFD was not shown to be statistically significant.

– Line 112 – "…while IL-5 was only decreased with HFD" – this statistic was not shown in Figure 1E.

– Figure 2B – Quantify and show statistics for the claim on lines 140-141 "Ctr-fed male and female mice had high eosinophil numbers, and this subset disappeared in male mice upon HFD".

– Figure 2E – It is difficult to determine which comparisons are being highlighted on the box plots. In the text (lines 154-156) the authors claim that this is an HFD effect – does this hold for both sexes?

It is unfortunate that eosinophils could not be identified in the single-cell analysis since this population of cells was shown to be important in rescuing the RELMα-deficiency in HFD-fed females. The authors should note in the discussion how future scRNA-Seq experiments could overcome this limitation (i.e., enriching immune cells prior to scRNA-Seq). Although another scRNA-Seq experiment including eosinophils would add to the report, we believe it is beyond the scope of this study.

– Lines 283-286 – "We employed targeted approaches to identify eosinophil clusters according to eosinophil markers (e.g. Siglecf, Prg2, Ccr3, Il5r), and relaxed the scRNA-Seq cutoff analysis to include more cells and intronic content, but still could not find eosinophils." – Please provide the feature plots showing expression across clusters for Siglecf, Prg2, Ccr3, Il5r as supplemental figures.

– Lines 286-288 – "We conclude that eosinophils may be absent due to the enzyme digestion required for SVF isolation and processing for single-cell sequencing, which could lead to specific eosinophil population loss due to RNases or cell viability issues." – Do you use the same single cell dissociation techniques for flow cytometry as were employed for the scRNA-seq? If so, what proportion of cells are eosinophils?

There is inconsistency in the presentation and interpretation of the correlations in Figure 3.

– The correlations in Figure 3A, 3B, and 3E appear to be driven entirely by diet effect. Is it possible that the HFD and not body weight are responsible for this effect?

– Figure 3C-G – Why are males absent from this analysis?

– Figure 3E – Why are all groups not included in this particular correlation, as in Figure 3A and Figure 3B? Is this a female-specific effect? I understand why the KO groups were not included, but the text does not describe the sex difference here.

– Lines 183-184 – "suggesting that the protective effect of RELMα may be impaired with body weight gain (Figure 3F-G)." – This result could also imply that HFD (and not body weight) is causing a decrease in RELMα. Do you think that this same effect would be seen in another obesogenic diet (i.e., a high carbohydrate diet)? We are not recommending adding these experiments to the current report, but authors may choose to comment on this in the discussion.

There are several issues with the scRNA-Seq analysis and interpretation. More details on the steps taken in the single-cell analyses should be included in the methods section.

– Deposition of code to a public repository (i.e., GitHub) would allow for rigor and reproducibility of the analyses.

With regards to the 'pseudobulk' analyses presented in Figures 5-6, several of the differentially expressed genes identified in Figure 6 are hemoglobin genes (i.e., Hba, Hbb genes). It is not uncommon to filter these genes out of single-cell analysis since their presence usually indicates red blood cell (RBC) contamination (PMID: 31942070, PMID: 35672358). We would recommend assessing RBC contamination as well as removing Figure 6 from the manuscript and focusing on cell-type-specific analyses.

– Figure 5D – It is unclear what comparisons are generating these lists of genes. Please provide a supplemental table with all differentially expressed genes from the analyses.

Within the text, there are several instances where the authors claim that a pathway is upregulated based on their Gene Ontology (GO) over-representation analysis (ORA). To come to this conclusion, the authors identify genes that are upregulated in one condition and then perform GO-ORA on these genes. However, the authors do not consider negative regulators, whose upregulation would actually decrease the pathway. Authors should either replace their GO-ORA analysis with one that considers the magnitude and direction of differentially expressed genes and provides an activation z-score (i.e., Ingenuity Pathway Analysis) or replace instances of 'upregulated' or 'downregulated' pathways with 'over-represented' pathways.

For Figure 7A, a representative tSNE plot for each group (WT Female, KO Female, WT Male, KO Male) should be shown to ensure there is proper integration of the clusters across groups. There are some instances where the scRNA-Seq data do not appear to be integrated properly (i.e., Supplemental Figure 2C). The authors should explore integration techniques (i.e., Seurat; PMID: 29608179) to correct for potential batch effects within the analysis.

– Lines 338-339 – "When analyzing scRNA-seq data from WT mice, RELMα (Retnla) is expressed in the Mono and Mac1 clusters (Figure 7D, F)." – It appears that RELMα is also expressed in the Mac4 cluster. Did you perform a plot to see if RELMα is present in any other clusters from Figure 7A?

LncRNA Gm47283 is identified as a gene that is differentially expressed by genotype in HFD females (Figure 7G); however, according to Ensembl this gene is encoded on the Y-chromosome (https://uswest.ensembl.org/Mus_musculus/Gene/Summary?g=ENSMUSG00000096768;r=Y:90796007-90827734). The authors should use the RELMα genotype and sex chromosomally-encoded genes to confirm that their multiplexing was appropriate.

For Figure 8, samples should be co-clustered and integrated across groups before performing trajectory analysis to allow for direct comparisons between groups.

– Line 289-291 – "The main population in the SVF, accounting for 50-75% of cells, were non-immune cells identified as Pdgrfa+ fibroblasts (green). These were significantly increased in WT females compared to the other groups (p<0.01, S2C)." – Were these data integrated using a feature like the "IntegrateData" command in Seurat? It does not appear that the cells cluster well when comparing males and females.

Scale bars on several heatmaps are not labeled with what they represent (Figures 5E, 7F, 7G, S2N, S2O, S4B, S4C).

Since the experiments presented in this report were from young mice using a single diet intervention, the authors should comment on how age and other obesogenic diets may impact the results found here. Also, the authors should expand their discussion as to what upstream regulators (i.e., hormones or genetics) may be driving the sex differences in RELMα expression in response to HFD.
