# Author response - Round 1

Authors:
- Anthony S Findley ([ORCID: 0000-0001-9922-3076](https://orcid.org/0000-0001-9922-3076))
- Alan Monziani
- Allison L Richards
- Katherine Rhodes
- Michelle C Ward ([ORCID: 0000-0003-1485-320X](https://orcid.org/0000-0003-1485-320X))
- Cynthia A Kalita
- Adnan Alazizi
- Ali Pazokitoroudi
- Sriram Sankararaman
- Xiaoquan Wen
- David E Lanfear
- Roger Pique-Regi ([ORCID: 0000-0002-1262-2275](https://orcid.org/0000-0002-1262-2275))
- Yoav Gilad ([ORCID: 0000-0001-8284-8926](https://orcid.org/0000-0001-8284-8926))
- Francesca Luca ([ORCID: 0000-0001-8252-9052](https://orcid.org/0000-0001-8252-9052))

## Response text

DOI: [10.7554/eLife.67077.sa2](https://doi.org/10.7554/eLife.67077.sa2)

Essential revisions:

1. In your analysis of ASE overlap with eQTLs, you only focussed on cardiomyocytes and the heart tissue from GTEx. While this analysis is solid, it raises some issues around how well are your cardiomyocytes matched to the heart tissue in GTEx and how well does your claim that 47% of the genes with dynamic regulatory interactions are missed in existing large eQTL datasets generalise to the other two cell types in your study (LCLs and IPSCs). Fortunately, high-resolution eQTL maps for the other two cell types (iPSCs and LCLs ) do exist, so it should be possible to check this.

We thank the reviewers for this excellent suggestion. We have now added comparisons to eQTL results also for LCLs and IPSCs. For LCLs, we compared our ASE and cASE results to the eQTLs from the GEUVADIS dataset, for the IPSCs we have made a comparison to the eQTLs from the I2QTLs consortium. For both cell types, we find similar results to what we observed from the CMs, with a 1.5-fold enrichment for the ASE but no significant enrichment for the cASE. We have now added these results in figure 3E and we have added the following text to the manuscript:

Abstract

"On average half of the genes with dynamic regulatory interactions were missed by large eQTL mapping studies, indicating the importance of exploring multiple treatments to reveal previously unrecognized regulatory loci that may be important for disease."

Results

"We next investigated whether these genetic effects on gene expression have been previously observed in large scale eQTL mapping studies that largely ignored dynamic regulatory interactions. […] In IPSCs, there were 3,113 genes with ASE, and 80% were eGenes in i2QTL (1.49-fold enrichment, p = 1.0 x 10-10). Of the 352 genes with cASE in IPSCs, 284 were eGenes in i2QTL. As with the CMs, these cASE genes were not significantly enriched (odds ratio = 1.03)."

Discussion

"This is reflected in the lack of enrichment for cASE genes in eQTLs from large studies in three tissues/cell-types. […] However, this does not seem to be the case, as we obtained similar results for LCLs and IPSCs, compared to the eQTL results in the Geuvadis and i2QTL datasets, respectively, with ASE genes being enriched in eGenes, but not cASE."

Methods

"We used Fisher's exact test to test for an enrichment in ASE and cASE genes in eGenes from three large eQTL studies for CMs, IPSCs, and LCLs, respectively: GTEx left ventricle and atrial appendage (Aguet et al., 2020), i2QTL (Bonder et al., 2021), and Geuvadis (Lappalainen et al. 2013, Wen et al., 2015). […] Geuvadis eGenes were downloaded from https://www.ebi.ac.uk/arrayexpress/experiments/E-GEUV-3/files/analysis_results/EUR373.gene.cis.FDR5.best.rs137.txt.gz. The list of tested Geuvadis genes were downloaded from http://www-personal.umich.edu/~xwen/geuvadis/geuv.fm.tar.gz."

2. The authors show that their cASE catalogue captures genes that are missed by GTEx and identifies potentially novel GWAS genes. For these analyses, they focus mostly on the CM data where it's not clear that GTEx has a directly comparable cell type and ASE signal is not the same signal GTEx is generating. Because measuring ASE is not the same as measuring eQTL, such a comparison might not be fair due to statistical power and MAF differences. It could be better to compare ASE within the GTEx data. Also, the CM pool was sequenced to very high depth, and because the power to detect allelic bias is based on read depth, this study should have high power. I wonder how many of the (c)ASE they report (that's not observed in GTEx) is just a reflection of the high statistical power in this study due to read depth.

We agree with the reviewers that it would be interesting to compare our results to the ASE analysis in the GTEx dataset. We requested access to the GTEx ASE results per gene/tissue (Castel et al., 2020) which are now publicly available, and made this comparison for the CM ASE and the GTEx heart tissues ASE. We found similar results to the ones originally reported for the eGenes (see Figure 3E and specific changes below).

To investigate whether the additional cASE that we find and were not detected in GTEx could be partially explained by our high statistical power in the CMs, and also to do a direct comparison across the same cell types, we repeated the same analysis in the LCLs and IPSCs, which were sequenced at lower depth (146M and 148M, compared to 273M in CMs). Our new results (see response to comment above) show that even when considering LCLs and IPSCs, we can still identify 141 and 68 genes with cASE that were missed in eQTL studies in LCLs (Geuvadis) and IPSCs (i2QTL), respectively. We have added the results of these analyses in figure 3E and the relevant changes to the manuscript are reported below.

Results

"In addition to eQTL mapping, GTEx also used ASE to measure cis-regulatory effects (Castel et al., 2020). As with GTEx eGenes, GTEx left ventricle and atrial appendage genes with ASE were enriched for CM ASE genes (odds ratio = 1.75, 1.66 for each tissue, respectively, p<10-16), but not CM cASE genes."

Discussion

"Indeed a large fraction of CM cASE genes (>47%) are not eGenes in GTEx as detected by eQTL mapping or ASE. […] While comparisons across studies may be complicated by several factors including differences in haplotype structures, study populations, and sequencing depth, the results are highly concordant and support the same conclusion."

Methods

"GTEx ASE data were downloaded from https://github.com/secastel/phaser/blob/master/gtex_v8_analyses/gtex_v8_tissue_by_gene_imbalance.tar.gz. i2QTL eGenes and tested genes were found in Supplementary File 1c and Supplementary File 1g (Supplemental Tables 3 and 7 in version with tracked changes) in Bonder et al., 2021. […] The list of tested Geuvadis genes were downloaded from http://www-personal.umich.edu/~xwen/geuvadis/geuv.fm.tar.gz."

3. You report that 55% of the variance in gene expression in cardiomyocytes was assigned to differences between individuals, whereas this was much lower in LCLs (36%) and iPSC (28%). Could this simply reflect the fact that in your experimental design, genetic differences between individuals are confounded by CM differentiation batch and CM differentiation just happens to be highly variable? As far as I understood, you only performed one differentiation from each individual and thus you are not able to separate out the effect of differentiation batch from the effect of the individual?

We agree with the reviewers that besides genetics, other factors may also contribute to the individual component of the variance in gene expression. To specifically address the question of a contribution from the differentiation process, we considered the expression of the gene TNNT2 which encodes for the Cardiac muscle troponin T. The expression of this gene is used as a marker of differentiation of CMs and a surrogate of CM purity. We repeated the analysis of variance for the CMs by including TNNT2 expression as an additional factor. The results show that the proportion of variance explained by the individual component does not change and that the median percent variance explained by TNNT2 expression is 6% for expression and 3% for splicing. These results are presented in the Results section and in Figure 2—figure supplement 1

(supplemental figure 9 in version with tracked changes).

"To investigate whether this result may reflect variation in the purity of the CMs, we considered the expression of the gene TNNT2 which encodes for the cardiac muscle troponin T. […] The results show that the proportion of variance explained by the individual component does not change and that the median percent variance explained by TNNT2 expression is 6% (Figure 2—figure supplement 1). "
