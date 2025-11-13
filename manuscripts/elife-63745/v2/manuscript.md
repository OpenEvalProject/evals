# Perinatal granulopoiesis and risk of pediatric asthma

## Authors

- Benjamin A Turturice<sup>1</sup> ([ORCID: 0000-0001-9382-4612](https://orcid.org/0000-0001-9382-4612)) †
- Juliana Theorell<sup>2</sup>
- Mary Dawn Koenig<sup>3</sup>
- Lisa Tussing-Humphreys<sup>4</sup>
- Diane R Gold<sup>5</sup>
- Augusto A Litonjua<sup>7</sup>
- Emily Oken<sup>8</sup>
- Sheryl L Rifas-Shiman<sup>8</sup>
- David L Perkins<sup>9</sup> †
- Patricia W Finn<sup>1</sup> †

### Affiliations

1. Department of Microbiology and Immunology, University of Illinois Chicago United States
2. Department of Medicine, Division of Pulmonary, Critical Care, Sleep, and Allergy, University of Illinois Chicago United States
3. Department of Women, Children and Family Health Science, College of Nursing, University of Illinois Chicago United States
4. Department of Medicine and Cancer Center, University of Illinois Chicago United States
5. Channing Division of Network Medicine, Department of Medicine, Brigham and Women's Hospital, Harvard Medical School Boston United States
6. Department of Environmental Health, Harvard T.H. Chan School of Public Health Boston United States
7. Division of Pulmonary Medicine, Department of Pediatrics, University of Rochester Rochester United States
8. Division of Chronic Disease Research Across the Life Course, Department of Population Medicine, Harvard Medical School and Harvard Pilgrim Health Care Institute Boston United States
9. Department of Medicine, Division of Nephrology, University of Illinois Chicago United States
10. Department of Bioengineering, University of Illinois Chicago United States

† Corresponding author

## Abstract

There are perinatal characteristics, such as gestational age, reproducibly associated with the risk for pediatric asthma. Identification of biologic processes influenced by these characteristics could facilitate risk stratification or new therapeutic targets. We hypothesized that transcriptional changes associated with multiple epidemiologic risk factors would be mediators of pediatric asthma risk. Using publicly available transcriptomic data from cord blood mononuclear cells, transcription of genes involved in myeloid differentiation was observed to be inversely associated with a pediatric asthma risk stratification based on multiple perinatal risk factors. This gene signature was validated in an independent prospective cohort and was specifically associated with genes localizing to neutrophil-specific granules. Further validation demonstrated that umbilical cord blood serum concentration of PGLYRP-1, a specific granule protein, was inversely associated with mid-childhood current asthma and early-teen FEV1/FVCx100. Thus, neutrophil-specific granule abundance at birth predicts risk for pediatric asthma and pulmonary function in adolescence.

## Introduction

Several risk factors for pediatric asthma can be ascertained in the perinatal period. These risk factors include maternal characteristics (e.g., maternal atopy, maternal body mass index [BMI], race/ethnicity), demographics (e.g., newborn sex), and birth characteristics (e.g., birthweight, gestational age at birth, mode of delivery) (Bisgaard and Bønnelykke, 2010). Meta-analyses have provided strong evidence for associations between the variables stated above and risk for pediatric asthma (Jaakkola et al., 2006; Mu et al., 2014; Thavagnanam et al., 2008; Xu et al., 2014). Many of these risk factors co-occur (e.g., low birthweight and preterm birth), and it has yet to be discerned whether their imparted risk is mediated through similar biologic processes.

Meta-analyses assessing peripheral blood leukocytes of school-aged children have identified differentially methylated regions proximal, or within, genes specifically transcribed in eosinophils as a common signature in pediatric asthma (Xu et al., 2018; Reese et al., 2019). These findings are consistent with observations of enhanced T2 inflammatory responses in children with asthma (Wenzel, 2012). However, when assessing cord blood mononuclear cell (CBMC) samples, differential methylation did not extend to these and other classically T2-associated loci (Reese et al., 2019). Interestingly, some individuals are predisposed at birth to generating T2 responses ex vivo to common asthma triggers (e.g. aeroallergens) or having detectable IgE concentrations in cord blood but neither has been shown to predict asthma later in life (Schaub et al., 2005; Turturice et al., 2017a; Shah et al., 2011). These findings are suggestive of limited prognostication in asthma risk provided by the variation in T2 immunity at birth. Additionally, efforts aimed at modulating immunity in utero and through early life (e.g. vitamin D, probiotics) have failed to demonstrate benefit in the prevention of asthma (Litonjua et al., 2020; Azad et al., 2013). Further investigation is required to understand the aspects of newborn immunity associated with pediatric asthma.

The neonatal immune system undergoes many developmental changes throughout gestation and early life. Throughout the majority of gestation, fetal hematopoiesis generates mainly lymphoid and erythroid lineages. While the bone marrow capacity to produce all cell lineages increases toward term gestation, the ability to produce myeloid lineages is most pronounced in later gestational ages (Forestier et al., 1991; Glasser et al., 2015). Further highlighting the unique immunology of the perinatal time period, there are cell populations (e.g. CXCL8-producing T cells, myeloid-derived suppressor cells) that are highly abundant in cord blood that are rapidly depleted over the first week (Gibbons et al., 2014; Olin et al., 2018; Rieber et al., 2013). Importantly, in utero factors, such as preterm birth and gestational hypertension, can impact perinatal hematopoiesis. These events can impair neutrophil abundance and function at birth but return to adult levels within days of birth similar to that of those who did not have such an exposure (Glasser et al., 2015; Olin et al., 2018; Schmutz et al., 2008). This highlights great variability in the early-life hematopoietic composition driven by in utero differences that rapidly converges to a new baseline as the neonates adapts to its new environment.

This variability in immunity the perinatal time period might be reflective of the presence of multiple risk factors for asthma and facilitate a more detailed risk stratification and, ultimately, identification of potential therapeutic targets. Our focus was to determine biologic processes – extending to both transcriptional and serologic levels – associated with pediatric asthma risk that are detectable at birth. We hypothesized that transcriptional changes in CBMCs associated with multiple epidemiologic risk factors would be mediators of pediatric asthma risk. CBMCs have been previously studied with regards to cytokine production, DNA methylation, and outcomes (Reese et al., 2019; Turturice et al., 2017a; Lin et al., 1993; Ly et al., 2007; Turturice et al., 2019; den Dekker et al., 2019), making them ideal candidates for investigation. Here, we identify a novel association between epidemiologic risk, neutrophil-specific granules, and pediatric pulmonary outcomes including childhood asthma.

## Results

### Approach to identify immunologic differences associated with risk for pediatric asthma

We developed an analytic approach to identify genes whose expression in CBMCs are associated with newborns with higher or lower risk for asthma. We conducted a meta-analysis to increase power and generalizability (Figure 1A,B). In our approach, we queried NCBI’s Gene Expression Omnibus for CBMC microarray datasets that included metadata regarding the demographics and birth characteristics that are risk factors for pediatric asthma. We identified 354 datasets from our original search, of which 17 datasets contained relevant metadata. Of the 17 studies, the most common maternal and neonatal characteristics reported were newborn sex, gestational age at birth, birthweight, and maternal pre-pregnancy BMI (PP BMI) at 69.96%, 51.59%, 30.27%, and 19.32% of samples, respectively. Metadata regarding maternal smoking and mode of delivery (i.e., vaginal vs. cesarean section) was reported for three datasets; however, two of these datasets originated from the same laboratory group and contributed the majority of samples reporting these factors. None of the identified datasets reported metadata about maternal atopy or child’s ethnicity. Therefore, we chose to focus the analysis on gene expression associated with newborn sex, gestational age at birth, newborn weight, and maternal PP BMI. Six datasets were excluded due to homogenous metadata (e.g., all female). Datasets and the corresponding analysis are reported; a total of 605 unique transcriptomes were included (Table 1; Bukowski et al., 2017; Edlow et al., 2016; Kallionpää et al., 2014; Mason et al., 2010; Rager et al., 2014; Smith et al., 2014; Stünkel et al., 2012; Turan et al., 2012; Votavova et al., 2011; Votavova et al., 2012; Winckelmans et al., 2017).

![Figure 1.](https://cdn.elifesciences.org/articles/63745/elife-63745-fig1-v2.jpg)

**Figure 1.:** (A) Previously described perinatal risk factors for development of pediatric asthma: preterm birth, low birthweight, male, and maternal obesity. (B) Flow diagram of search, inclusion, exclusion, and univariate testing for transcriptomic analysis. (C) Cohorts, types of biosamples, and outcomes used for validation.

**Table 1.**
 GSE data sets used for meta-analyses.


<table>
  <thead>
    <tr>
      <th>GSE</th>
      <th>GPL</th>
      <th>N</th>
      <th>Newborn sex</th>
      <th>Gestational age</th>
      <th>Birthweight</th>
      <th>Maternal pre-pregnancy BMI</th>
      <th>Title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>GSE21342</td>
      <td>GPL6947</td>
      <td>37</td>
      <td></td>
      <td></td>
      <td></td>
      <td>+</td>
      <td>Maternal influences on the transmission of leukocyte gene expression profiles in population samples</td>
    </tr>
    <tr>
      <td>GSE25504</td>
      <td>GPL570</td>
      <td>20</td>
      <td>+</td>
      <td></td>
      <td></td>
      <td></td>
      <td>Whole blood mRNA expression profiling of host molecular networks in neonatal sepsis</td>
    </tr>
    <tr>
      <td>GSE27272</td>
      <td>GPL6883</td>
      <td>64</td>
      <td></td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>Comprehensive study of tobacco smoke-related transcriptome alterations in maternal and fetal cells</td>
    </tr>
    <tr>
      <td>GSE30032</td>
      <td>GPL6883</td>
      <td>47</td>
      <td></td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td>Deregulation of gene expression induced by environmental tobacco smoke exposure in pregnancy</td>
    </tr>
    <tr>
      <td>GSE36828</td>
      <td>GPL6947</td>
      <td>48</td>
      <td></td>
      <td>+</td>
      <td>+</td>
      <td></td>
      <td>Genome-wide analysis of gene expression levels in placenta and cord blood samples from newborns babies</td>
    </tr>
    <tr>
      <td>GSE37100</td>
      <td>GPL14550</td>
      <td>38</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td></td>
      <td>Transcriptome changes affecting hedgehog and cytokine signaling in the umbilical cord in late pregnancy: implications for disease risk</td>
    </tr>
    <tr>
      <td>GSE48354</td>
      <td>GPL16686</td>
      <td>38</td>
      <td>+</td>
      <td>+</td>
      <td>+</td>
      <td></td>
      <td>Prenatal arsenic exposure and the epigenome: altered gene expression profiles in newborn cord blood</td>
    </tr>
    <tr>
      <td>GSE53473</td>
      <td>GPL13667</td>
      <td>128</td>
      <td>+</td>
      <td>+</td>
      <td></td>
      <td></td>
      <td>Standard of hygiene and immune adaptation in newborn infants</td>
    </tr>
    <tr>
      <td>GSE60403</td>
      <td>GPL570</td>
      <td>16</td>
      <td>+</td>
      <td></td>
      <td></td>
      <td>+</td>
      <td>The obese fetal transcriptome</td>
    </tr>
    <tr>
      <td>GSE73685</td>
      <td>GPL6244</td>
      <td>23</td>
      <td></td>
      <td>+</td>
      <td></td>
      <td></td>
      <td>Unique inflammatory transcriptome profiles at the maternal fetal interface and onset of human preterm and term birth</td>
    </tr>
    <tr>
      <td>GSE83393</td>
      <td>GPL17077</td>
      <td>146</td>
      <td>+</td>
      <td></td>
      <td></td>
      <td></td>
      <td>Newborn sex-specific transcriptome signatures and gestational exposure to fine particles: findings from the ENVIRONAGE Birth Cohort</td>
    </tr>
    <tr>
      <td></td>
      <td>N</td>
      <td>605</td>
      <td>386</td>
      <td>386</td>
      <td>235</td>
      <td>164</td>
      <td></td>
    </tr>
  </tbody>
</table>

To validate the findings of the meta-analysis, we assessed three independent cohorts to confirm which genes are associated with asthma risk (Figure 1C). Further details regarding validation and outcomes are discussed in the Results section. In brief, the goal of validation was to assess gene expression in an independent cohort (UIH Cohort [Koenig et al., 2020]) where all subjects had complete metadata regarding newborn sex, gestational age, birthweight, and PP BMI. We sought to further understand whether transcriptomic differences in CBMCs corresponded to differences at the protein level (all three cohorts) or cell population level (Olin et al., 2018). Finally, we assessed two identified proteins in another independent cohort (Project Viva Cohort [Oken et al., 2015]) to test for association with pediatric asthma and pulmonary function outcomes at two follow-up time points.

### Meta-analysis of CBMC transcription associated with individual perinatal risk factors

Univariate random-effects models were generated to assess transcriptional changes in CBMCs with regards to newborn sex, gestational age, birthweight, and maternal PP BMI (Figure 2A). Differential expression (false discovery rate [FDR] < 1%) was observed in 122, 34, 4, and 12 genes when comparing fetal sex, gestational age, birthweight, and maternal pre-pregnancy BMI, respectively (Supplementary file 1–4). When evaluating sex and gestational age, several expected genes were identified to have large transcriptional changes. With regards to sex-associated transcriptional changes, although there was no X or Y chromosome-wide gene enrichment, several genes located on X (KDM5C, SMC1A, TXLNG, and KDM6A) and Y (KDM5D and EIF1AY) chromosomes exhibited the largest effect sizes and most significant differences. In addition to expected sex-associated transcriptional changes, HBE1, a hemoglobin subunit associated with fetal erythropoiesis, was significantly associated with preterm gestational ages. To further validate our gestational age findings, we compared our univariate analysis with previously published results of differentially methylated regions associated with gestational age at birth estimated by last menstrual period (Bohlin et al., 2016; Figure 2—figure supplement 1). A significant association was observed between differentially methylated genes and the effect size in our gestational age analysis, such that genes whose methylation increased with gestational age as reported by Bohlin et al., 2016 showed on average decreased expression with gestational age in our meta-analysis.

![Figure 2.](https://cdn.elifesciences.org/articles/63745/elife-63745-fig2-v2.jpg)

**Figure 2.:** Significant (FDR < 1%) genes and gene sets are colored by their association with either higher (red) or lower (blue) risk. (A) Volcano plots of gene expression for univariate analyses. Top 10 most significant genes labeled. (B) Word clouds of GO terms significantly enriched (FDR < 1%) using the pooled z-score as pre-ranked list for GSEA. (C) Protein coding transcripts per million reads (pTPM) in peripheral blood cells (Human Protein Atlas and Monaco et al (Uhlen et al., 2010; Monaco et al., 2019) relative to pooled z-score. Each line represents one cell type; neutrophils highlighted in orange. (D) Spearman’s correlation between pooled z-statistic and individual analyses (diamonds). Average Spearman’s correlations between individual analyses and combination of all other analyses (circle), SD indicated by error bars.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/63745/elife-63745-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Comparison of effect size associated with gestational age for genes that were reported as differentially methylated by Bohlin et al., 2016. Gene with increased methylation associated with gestational age demonstrate reduced expression with increasing gestational age.

### Pooled meta-analysis gene expression signature

To identify the biological processes that are enriched by genes with transcriptional changes associated with higher or lower risk of asthma, the z-scores from each univariate meta-analysis were averaged, such that negative z-statistics were associated with lower risk (female, older gestational ages, higher birthweights, and lower maternal PP BMI) and positive z-statistics were associated with increased risk. Thus, the pooled z-score indicates the average probability that a gene’s expression is associated with either increased or decreased risk of asthma based on an individual’s demographics and birth characteristics. The averaged z-statistic was used as a pre-ranked list for gene set enrichment analysis. GO terms were assessed for enrichment; 18 and 19 GO terms were significantly enriched (FDR < 1%) with regards to low- and high-risk profiles, respectively (Figure 2B). Genes associated with lower risk exhibited increased representation in GO terms involving innate immune signaling and defense, whereas high-risk genes were enriched in pathways involving translation and RNA metabolic processes.

Gene expression studies from pooled cellular populations (e.g. CBMCs, peripheral blood mononuclear cells, and tissues) can be influenced by the cellular composition. To determine whether specific cell population enrichment was associated with the pooled z-score, the Human Protein Atlas (HPA; Uhlen et al., 2010, Monaco et al., 2019) was utilized to assess the abundance of transcripts in peripheral blood leukocyte RNA transcriptomes in relationship to the pooled z-score. We observed a generalized increase in expression of low-risk genes in myeloid cells and high-risk genes in lymphoid cells. This pattern of expression was most pronounced in neutrophils (Figure 2C). These results suggest that lower risk individuals have increased populations of myeloid cells in their CBMCs.

A potential confounder in pooling results is the potential over-representation of any one analysis. To assess bias in the pooled z-score, two analyses were performed (Figure 2D). In the first assessment, z-scores from each individual analysis correlated with the pooled z-score. The highest correlations with the pooled z-score were the z-scores from the meta-analyses assessing gestational age at birth, newborn sex, and birthweight. Individual dataset z-scores for each dataset demonstrated a similar trend. In the second assessment, z-scores from each individual analysis were correlated with the combination of all other z-scores. Again, the pooled z-score had the highest average correlation followed by the meta-analyses. Together, this demonstrates that the pooled z-score does, indeed, amalgamate information across all of the analyses, with the most influence arising from gestational age at birth, newborn sex, and birthweight.

### Specific granule gene expression association with multiple pediatric asthma risk factors

To confirm gene expression changes associated with asthma risk stratification, pooled z-scores from the meta-analysis were compared with the UIH cohort, a cohort of individuals in which newborn sex, maternal PP BMI, gestational age at birth, and birthweight were known (Supplementary file 5). UIH cohort z-scores were calculated from mRNAseq of CBMCs, where gene expression was modeled as a function of number of risk factors (Supplementary file 6). We developed a method to validate the congruence between the UIH cohort and the pooled meta-analysis, which we termed the replication score (RS). This RS is the product of the pooled z-score from the meta-analysis and the UIH z-score (see Materials and methods). We assessed the relationship between RS cutoff, p-values, and number of genes (Figure 3—figure supplement 1). Genes with a RS greater than three were identified as being sufficiently congruent. Fifty-one genes, 0.4% of all genes, tested had a RS greater than 3 (Figure 3A). These identified genes corresponded well with the results of pooled z-score for gestational age at birth, newborn sex and birthweight, but showed limited correlation to maternal PP BMI. They had median p-values of 0.02, 0.01, 0.11, and 0.58 in the gestational age at birth, newborn sex, birthweight, and maternal PP BMI meta-analyses, and median p-value of 0.02 in the UIH cohort.

![Figure 3.](https://cdn.elifesciences.org/articles/63745/elife-63745-fig3-v2.jpg)

**Figure 3.:** Color labeling indicating association with either higher (red) or lower (blue) risk of pediatric asthma development. (A) Dot-plot demonstrating validation between meta-analysis pooled z-score and UIH cohort mRNAseq z-score. Colored and labeled dots indicate those with non-parametric replication score greater than 3 and 4, respectively. (B,C) Association between number of risk factors or individual risk factors and eigenvalue of gene signature (validation score > 3), UIH cohort.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/63745/elife-63745-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Splines (colored according to analysis) of median p-values (left y-axis) for genes with replication scores greater than corresponding cut-off (x-axis). Percentage of genes with replication score greater than corresponding cut-off. Vertical dashed lines two cutoffs: RS > 0 and RS > 3.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/63745/elife-63745-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** (A) Protein–protein interaction network of candidate genes inferred from STRING (Szklarczyk et al., 2019). Nodes are labeled by risk association: low (blue) and high (red) risk candidate genes. Nodes are colored (purple) if they are associated with GO cellular component term enrichment. (B) Word clouds of GO terms significantly enriched in candidate genes.

Replicating genes were enriched for processes involved in vesicle biology (Figure 3—figure supplement 2). Specifically, replicating genes associated with low risk were enriched for genes that are components of granulocyte specific granules (MS4A3, CEACAM8, OLR1, CAMP, LTF, CHI3L1, SLPI, PGLYRP1). With regards to genes associated with higher risk, genes involved in vesicle sorting/production (VPS28, VTI1B, FIS1) as well as several genes involved in vesicle membrane biology (AGPAT3, ELOVL6, TM7SF2) were identified.

To test whether replicating genes were associated with the number of risk factors, these 51 genes were assessed using principal component analysis. Using the first Eigenvector (explaining 41.3% of variance in replicating genes), a significant association (R [95% confidence interval (CI)=−0.51 [–0.73, –0.18], p-value<0.01) was observed between UIH cohort Eigenvalues and number of epidemiologic risk factors (Figure 3B). Positive eigenvalues represent increased expression of low-risk genes and negative eigenvalues represent increased expression of high-risk genes. Although the associations with individual risk factors were in the expected directions, they were not significant (Figure 3C), suggesting that the additive effect is greater than the individual.

### Cellular and protein abundance in relation to pediatric asthma risk factors

To further determine whether these changes are due to differences in cellular populations, we analyzed mass cytometry data published by Olin et al. for abundance of 21 different cell types in relationship to number of epidemiologic risk factors for pediatric asthma (Votavova et al., 2011). Cord blood neutrophil abundance was inversely associated (R [95% CI]=−0.57 [–0.73, –0.34], Bonferroni p-adj<0.001) with the number of risk factors (Figure 4A). Other myeloid cell types, CD14+ monocytes, and myeloid-derived dendritic cells also had negative correlations but were weaker and not significant after multiple testing correction (data not shown).

![Figure 4.](https://cdn.elifesciences.org/articles/63745/elife-63745-fig4-v2.jpg)

**Figure 4.:** (A–C) Re-analysis of publicly available data from Olin et al., 2018. (A) Percentage of neutrophils in cord blood (transformed using centered log-ratios, CLR) correlated with number of risk factors. Pearson’s correlation (R) and Bonferroni adjusted p-value reported. (B) Pearson’s correlation coefficients (R) for plasma-protein concentration and number of risk factors distributed based on risk association of proteins as per Figure 3. Corresponding mRNA from CBMCs were identified for low-risk associated proteins (blue) and no risk associated proteins (dark gray). Most significant negative protein correlations with neutrophil-enriched mRNA (Human Protein Atlas [Uhlen et al., 2010]) are notated. Proteins identified in previous analysis without corresponding mRNA shown light gray. (C) Heatmap of Pearson’s correlations between neutrophils and neutrophil-derived proteins identified in (B). (D) Association between PGLYRP-1 umbilical cord serum concentration, PGLYRP-1 CBMC mRNA, and number of risk factors in UIH cohort.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/63745/elife-63745-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Scatter plot displaying association between PGLYRP-1 and sIL6Rα in UIH (blue) and Project Viva (yellow) cohorts. Univariate regression lines are shown for both cohorts. Distributions for PGLYRP-1 and sIL6Rα are shown in the margins for each cohort.

Extending these findings from gene expression to protein abundance, reported umbilical cord plasma-protein abundance data was correlated with number of risk factors in a secondary analysis (Olin et al., 2018). Serum proteins from genes that replicated with low risk had on average negative correlations with number of risk factors (Figure 4B). No proteins from the high-risk genes were tested in plasma, due to their intracellular localization. Notably, proteins (CEACAM8, PGLYRP-1, CHIT1, sIL6Rα, MMP-9, and OSM) predicted to be enriched in neutrophils by the HPA (Uhlen et al., 2010) had strong correlations with both neutrophil abundance and number of risk factors (Figure 4B,C).

We hypothesized that the serum concentration of proteins identified as low risk in our transcriptomic analysis would correlate with mRNA abundance in CBMCs, whereas those not associated with risk would not correlate with mRNA in CBMCs. To test this hypothesis, we used the UIH cohort to correlate mRNA abundance with serum protein concentration of PGLYRP-1 (low risk) and sIL6Rα (no risk). We observed a significant (R [95% CI]=0.39 [0.03, 0.66], p<0.05) association between PGLYRP-1 protein concentration and mRNA (Figure 4D). Consistent with transcriptomic results, PGLYRP-1 cord blood serum concentration was inversely associated with number of risk factors (R [95% CI]=−0.51 [–0.74, –0.17], p<0.01). sIL6Rα was neither associated with its mRNA in CBMCs (R [95% CI]=0.37 [–0.22, 0.77], p=0.21) nor associated with the number of risk factors (R [95% CI]=0.20 [–0.39, 0.67], p=0.50).

### Demographic associations with serum neutrophil proteins in UIH and Project Viva cohorts

We tested the association between PGLYRP-1 and sIL6Rα, individual risk factors, and demographics in the UIH and Project Viva cohorts. Cord blood serum was available in a subset of individuals (n = 358) from Project Viva (Supplementary file 7). There was no significant difference (p>0.05, Wilcoxon rank sum test) in PGLYRP-1 or sIL6Rα between UIH and Project Viva cohorts (Figure 4—figure supplement 1). Consistent with our previous observations, PGLYRP-1 and sIL6Rα were positively correlated in both UIH (R [95% CI]=0.21 [−0.16, 0.54]) and Project Viva (R [95% CI]=0.19 [0.09, 0.29]) cohorts. Similar to the observation in the UIH cohort, there was a negative association between PGLYRP-1 and number of risk factors in Project Viva (β [95% CI]=−0.22 [−0.36, –0.07], p-value=0.003) (Table 2). This association was driven by the relationship between PGLYRP-1, gestational age, and sex. There was no association with PP BMI or birthweight when taking into account gestational age and sex. Furthermore, there was no association of sIL6Rα with the number or risk factors or any individual risk factor. Interestingly, there was an inverse relationship observed in both the UIH and Project Viva cohorts between sIL6Rα and self-reported maternal race as Black/African-American. Collectively, these results suggest that increased abundance of mRNA from genes localizing to neutrophil-specific granules are associated with the number of risk factors for pediatric asthma. These changes in mRNA are reflected in the abundance of these specific granule proteins in serum and plasma.

**Table 2.**
 Univariate associations between demographics and serum proteins.


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="2">UIH (n = 29)</th>
      <th colspan="2">Project viva (n = 358)</th>
    </tr>
    <tr>
      <th></th>
      <th>β (95% CI)</th>
      <th>p-value</th>
      <th>β (95% CI)</th>
      <th>p-value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>PGLYRP-1 Z-score*</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Number of risk factors†</td>
      <td>−0.54 (–0.88, –0.19)</td>
      <td>0.005</td>
      <td>−0.22 (–0.36, –0.07)</td>
      <td>0.003</td>
    </tr>
    <tr>
      <td>Maternal race: White (ref)</td>
      <td>0 (ref)</td>
      <td></td>
      <td>0 (ref)</td>
      <td></td>
    </tr>
    <tr>
      <td>Maternal race: Black</td>
      <td>0.01 (–0.83, 0.86)</td>
      <td>0.97</td>
      <td>0.15 (–0.16, 0.46)</td>
      <td>0.34</td>
    </tr>
    <tr>
      <td>Maternal race: Hispanic</td>
      <td>1.03 (0.05, 2.01)</td>
      <td>0.04</td>
      <td>0.40 (–0.07, 0.86)</td>
      <td>0.10</td>
    </tr>
    <tr>
      <td>Maternal race: Other</td>
      <td>1.54 (–0.46, 3.54)</td>
      <td>0.12</td>
      <td>0.10 (–0.25, 0.46)</td>
      <td>0.57</td>
    </tr>
    <tr>
      <td>Maternal atopy</td>
      <td>−0.14 (–0.92, 0.64)</td>
      <td>0.72</td>
      <td>0.06 (–0.16, 0.28)</td>
      <td>0.58</td>
    </tr>
    <tr>
      <td>Maternal pre-pregnancy BMI</td>
      <td>−0.03 (–0.09, 0.02)</td>
      <td>0.25</td>
      <td>0.01 (–0.01, 0.03)</td>
      <td>0.56</td>
    </tr>
    <tr>
      <td>Maternal smoking: never (ref)</td>
      <td>0 (ref)</td>
      <td></td>
      <td>0 (ref)</td>
      <td></td>
    </tr>
    <tr>
      <td>Maternal smoking: former</td>
      <td>0.09 (–0.92, 1.12)</td>
      <td>0.84</td>
      <td>−0.16 (–0.44, 0.11)</td>
      <td>0.25</td>
    </tr>
    <tr>
      <td>Maternal smoking: during pregnancy</td>
      <td>–</td>
      <td>–</td>
      <td>−0.12 (–0.47, 0.22)</td>
      <td>0.48</td>
    </tr>
    <tr>
      <td>Maternal college graduate</td>
      <td>0.07 (–0.80, 0.93)</td>
      <td>0.87</td>
      <td>−0.12 (–0.34, 0.10)</td>
      <td>0.27</td>
    </tr>
    <tr>
      <td>Any antibiotic use during pregnancy</td>
      <td>–</td>
      <td>–</td>
      <td>0.20 (-0.02, 0.43)</td>
      <td>0.08</td>
    </tr>
    <tr>
      <td>Gestational age weeks</td>
      <td>0.25 (–0.01, 0.51)</td>
      <td>0.06</td>
      <td>0.12 (0.06, 0.19)</td>
      <td>0.0003</td>
    </tr>
    <tr>
      <td>Birthweight adj GA and Sex (Z-score)</td>
      <td>0.33 (–1.07, 1.74)</td>
      <td>0.63</td>
      <td>0.03 (–0.09, 0.14)</td>
      <td>0.66</td>
    </tr>
    <tr>
      <td>Female</td>
      <td>0.39 (–0.37, 1.15)</td>
      <td>0.30</td>
      <td>0.31 (0.11, 0.52)</td>
      <td>0.003</td>
    </tr>
    <tr>
      <td>C-section</td>
      <td>−0.08 (–0.89, 0.74)</td>
      <td>0.85</td>
      <td>−0.29 (–0.55, –0.02)</td>
      <td>0.03</td>
    </tr>
    <tr>
      <td>Child’s race: White (ref)</td>
      <td>–</td>
      <td>–</td>
      <td>0 (ref)</td>
      <td></td>
    </tr>
    <tr>
      <td>Child’s race: Black</td>
      <td>–</td>
      <td>–</td>
      <td>0.16 (–0.14, 0.46)</td>
      <td>0.31</td>
    </tr>
    <tr>
      <td>Child’s race: Hispanic</td>
      <td>–</td>
      <td>–</td>
      <td>0.18 (–0.31, 0.68)</td>
      <td>0.46</td>
    </tr>
    <tr>
      <td>Child’s race: Other</td>
      <td>–</td>
      <td>–</td>
      <td>0.06 (-0.27, 0.38)</td>
      <td>0.73</td>
    </tr>
    <tr>
      <td>sIL6Rα Z-score*</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Number of risk factors†</td>
      <td>−0.14 (–0.54, –0.25)</td>
      <td>0.48</td>
      <td>0.02 (–0.13, 0.16)</td>
      <td>0.81</td>
    </tr>
    <tr>
      <td>Maternal race: White (ref)</td>
      <td>0 (ref)</td>
      <td></td>
      <td>0 (ref)</td>
      <td></td>
    </tr>
    <tr>
      <td>Maternal race: Black</td>
      <td>−1.04 (–1.90, –0.19)</td>
      <td>0.02</td>
      <td>−0.29 (–0.60, 0.02)</td>
      <td>0.07</td>
    </tr>
    <tr>
      <td>Maternal race: Hispanic</td>
      <td>−0.36 (–1.34, 0.62)</td>
      <td>0.45</td>
      <td>0.34 (-0.12, 0.80)</td>
      <td>0.15</td>
    </tr>
    <tr>
      <td>Maternal race: Other</td>
      <td>0.4 (–1.61, 2.42)</td>
      <td>0.68</td>
      <td>−0.03 (–0.39, 0.32)</td>
      <td>0.85</td>
    </tr>
    <tr>
      <td>Maternal atopy</td>
      <td>−0.23 (–1.01, 0.54)</td>
      <td>0.55</td>
      <td>−0.08 (–0.30, 0.14)</td>
      <td>0.47</td>
    </tr>
    <tr>
      <td>Maternal pre-pregnancy BMI</td>
      <td>−0.04 (–0.10, 0.01)</td>
      <td>0.12</td>
      <td>0.00 (–0.02, 0.02)</td>
      <td>0.72</td>
    </tr>
    <tr>
      <td>Maternal smoking: never (ref)</td>
      <td>0 (ref)</td>
      <td></td>
      <td>0 (ref)</td>
      <td></td>
    </tr>
    <tr>
      <td>Maternal smoking: former</td>
      <td>−0.90 (–1.86, 0.06)</td>
      <td>0.07</td>
      <td>−0.23 (–0.50, 0.05)</td>
      <td>0.10</td>
    </tr>
    <tr>
      <td>Maternal smoking: during pregnancy</td>
      <td>–</td>
      <td>–</td>
      <td>−0.12 (–0.46, 0.22)</td>
      <td>0.48</td>
    </tr>
    <tr>
      <td>Maternal college graduate</td>
      <td>0.44 (–0.41, 1.29)</td>
      <td>0.29</td>
      <td>−0.02 (–0.24, 0.19)</td>
      <td>0.84</td>
    </tr>
    <tr>
      <td>Any antibiotic use during pregnancy</td>
      <td>–</td>
      <td>–</td>
      <td>0.04 (–0.19, 0.26)</td>
      <td>0.76</td>
    </tr>
    <tr>
      <td>Gestational age weeks</td>
      <td>−0.11 (–0.39, 0.17)</td>
      <td>0.43</td>
      <td>−0.04 (–0.10, 0.03)</td>
      <td>0.29</td>
    </tr>
    <tr>
      <td>Birthweight adj GA and sex (Z-score)</td>
      <td>−0.15 (–1.57, 1.26)</td>
      <td>0.82</td>
      <td>−0.07 (–0.18, 0.04)</td>
      <td>0.23</td>
    </tr>
    <tr>
      <td>Female</td>
      <td>0.48 (–0.28, 1.23)</td>
      <td>0.21</td>
      <td>0.05 (–0.16, 0.26)</td>
      <td>0.63</td>
    </tr>
    <tr>
      <td>C-section</td>
      <td>−0.60 (–1.38, 0.18)</td>
      <td>0.12</td>
      <td>−0.14 (–0.41, 0.12)</td>
      <td>0.29</td>
    </tr>
    <tr>
      <td>Child’s race: White (ref)</td>
      <td>–</td>
      <td>–</td>
      <td>0 (ref)</td>
      <td></td>
    </tr>
    <tr>
      <td>Child’s race: Black</td>
      <td>–</td>
      <td>–</td>
      <td>−0.24 (–0.54, 0.05)</td>
      <td>0.11</td>
    </tr>
    <tr>
      <td>Child’s race: Hispanic</td>
      <td>–</td>
      <td>–</td>
      <td>0.27 (–0.22, 0.76)</td>
      <td>0.28</td>
    </tr>
    <tr>
      <td>Child’s race: Other</td>
      <td>–</td>
      <td>–</td>
      <td>0.02 (–0.30, 0.34)</td>
      <td>0.90</td>
    </tr>
  </tbody>
</table>

_*Serum protein concentrations for UIH and Project Viva were log10 transformed and converted into an internal Z-score.†Number of risk factors determined by preterm birth, maternal BMI > 29.9, male, birthweight (z-score) < −1._

### Serum neutrophil protein association with pediatric pulmonary outcomes

In context of our previous results, we hypothesized that specific granule protein abundance in serum is associated with risk of pediatric asthma and this process is independent of neutrophil abundance. To evaluate this hypothesis, we measured PGLYRP-1 (present in neutrophil-specific granule and correlates with its mRNA in CBMCs) and sIL6Rα (derived from neutrophils but not present in specific granules and does not correlate with its mRNA in CBMCs) in umbilical cord blood serum. At two follow-up time points, asthma outcomes and expiratory flow volumes were modeled as a function of PGLYRP-1 and sIL6Rα in a subset of individuals in Project Viva (Figure 5—figure supplement 1). The demographics of the subset of individuals from Project Viva from which umbilical cord serum was available had a similar demographic profile as the full cohort. One notable difference was a sizeable decreased response rate for asthma outcomes at the early-teenage follow-up compared to the full cohort (32% subset vs. 47% full cohort).

PGLYRP-1 and sIL6Rα were modeled as predictors for current asthma at mid-childhood (median age ~7.7 years old) and early-teen (median age ~12.3 years old) follow ups (Table 3). Four regression models were used to estimate the association between asthma outcomes: univariate, adjustment for child’s birth characteristics and demographics, adjustment for mother’s demographics, and adjustment for birth characteristics and all demographics (reported in manuscript). The abundance of PGLYRP-1 was significantly associated with current asthma at mid-childhood (adjusted odds ratio [OR] [95% CI]: 0.50 [0.31, 0.77] per 1 SD increase, p-value=0.003) (Figure 5A). There were no significant associations between current asthma and PGLYRP-1 at the early-teen follow up; however, the CI at this time point was much wider, likely secondary to the smaller sample size. There were no significant associations between sIL6Rα with any asthma outcome at either time point.

![Figure 5.](https://cdn.elifesciences.org/articles/63745/elife-63745-fig5-v2.jpg)

**Figure 5.:** Samples and data derived from a subset of Project Viva (n=358). Odds ratio and coefficient estimates are based on 1 SD increase in serum proteins (PGLYRP-1, sIL6Rα). Error bars indicate 95% CI. Adjusted model co-variates: gestational age, birthweight adjusted for gestational age and sex, mode of delivery, child’s sex, child's race/ethnicity, maternal pre-pregnancy BMI, maternal level of education, maternal atopy, antibiotic exposure during pregnancy, and early-life smoke exposure. (A) PGLYRP-1 and sIL6Rα concentrations in umbilical cord blood serum association with current asthma at mid-childhood and early-teenage time points (determined by questionnaire responses). (B) PGLYRP-1 and sIL6Rα concentrations in umbilical cord blood serum association with FEV1/FVCx100 at mid-childhood and early-teenage follow ups. ***p<0.001, **p<0.01, *p<0.05, #p<0.1.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/63745/elife-63745-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** (A) PGLYRP-1 concentration in umbilical cord blood serum in relationship to current asthma determined by questionnaire response and (B) FEV1/FVCx100 at mid-childhood and early-teenage follow ups. (C) sIL6Rα concentration in umbilical cord blood serum in relationship to current asthma determined by questionnaire response and (D) FEV1/FVCx100 at mid-childhood and early-teenage follow ups.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/63745/elife-63745-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** Relative importance, displayed as percent of variance explained, for variables used in regressions (Table 3, model 3) for current asthma at mid-childhood and FEV1/FVC in early-teen years. Variance estimated for logistic regression as Mcfadden’s pseudo-R (Jaakkola et al., 2006).

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/63745/elife-63745-fig5-figsupp3-v2.jpg)

**Figure 5—figure supplement 3.:** Funnel plot demonstrating relationship effect size estimates and measurement error for subset analyses for (A) current mid-childhood asthma and (B) FEV1/FVCx100 in early-teen years. 95% CI (botted lines) and 99% CI (dashed lines) displayed.

**Table 3.**
 Association between serum protein concentration and asthma outcomes.


<table>
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th colspan="2">Mid-childhood</th>
      <th colspan="2">Early-teen</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td>Current asthma, OR (95% CI)</td>
      <td>Ever asthma, OR (95% CI)</td>
      <td>Current asthma, OR (95% CI)</td>
      <td>Ever asthma, OR (95% CI)</td>
    </tr>
    <tr>
      <td>PGLYRP-1 Z-score*</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Univariate</td>
      <td>0.52 (0.35, 0.75)</td>
      <td>0.52 (0.36, 0.74)</td>
      <td>0.65 (0.39, 1.10)</td>
      <td>0.64 (0.45, 0.89)</td>
    </tr>
    <tr>
      <td></td>
      <td>Model 1†</td>
      <td>0.57 (0.37, 0.85)</td>
      <td>0.54 (0.36, 0.79)</td>
      <td>0.86 (0.48, 1.54)</td>
      <td>0.72 (0.50, 1.03)</td>
    </tr>
    <tr>
      <td></td>
      <td>Model 2‡</td>
      <td>0.57 (0.26, 0.65)</td>
      <td>0.41 (0.26, 0.61)</td>
      <td>0.62 (0.35, 1.09)</td>
      <td>0.61 (0.42, 0.87)</td>
    </tr>
    <tr>
      <td></td>
      <td>Model 3#</td>
      <td>0.50 (0.31, 0.77)</td>
      <td>0.48 (0.31, 0.77)</td>
      <td>0.88 (0.45, 1.72)</td>
      <td>0.74 (0.51, 1.07)</td>
    </tr>
    <tr>
      <td>sIL6Rα Z-score*</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Univariate</td>
      <td>0.87 (0.61, 1.23)</td>
      <td>0.93 (0.67, 1.29)</td>
      <td>0.75 (0.42, 1.28)</td>
      <td>0.93 (0.66, 1.29)</td>
    </tr>
    <tr>
      <td></td>
      <td>Model 1†</td>
      <td>0.83 (0.56, 1.23)</td>
      <td>0.89 (0.63, 1.30)</td>
      <td>0.68 (0.37, 1.21)</td>
      <td>0.90 (0.63, 1.27)</td>
    </tr>
    <tr>
      <td></td>
      <td>Model 2‡</td>
      <td>0.83 (0.57, 1.24)</td>
      <td>0.90 (0.63, 1.28)</td>
      <td>0.67 (0.33, 1.27)</td>
      <td>0.93 (0.65, 1.31)</td>
    </tr>
    <tr>
      <td></td>
      <td>Model 3#</td>
      <td>0.83 (0.55, 1.25)</td>
      <td>0.90 (0.62, 1.30)</td>
      <td>0.60 (0.27, 1.19)</td>
      <td>0.88 (0.61, 1.27)</td>
    </tr>
  </tbody>
</table>

_*Serum protein concentrations were log10 transformed and converted into an internal Z-score.†Serum protein concentrations were log10 transformed and conver gestational age, birthweight adjusted for gestational age, mode of delivery, child’s sex, child’s race/ethnicity.‡(Mother’s demographics): adjusted for maternal pre-pregnancy BMI, maternal race/ethnicity, maternal level of education, maternal atopy, antibiotic exposure during pregnancy, smoking during pregnancy, 6 months or 1 year.#Model 3 (all demographics and birth characteristics): adjusted for all demographics and characteristics in models 1 and 2 except maternal race/ethnicity. This reported value in manuscript._

We also performed analyses to estimate the relationship of cord blood PGLYRP-1 and sIL6Rα with FEV1/FVCx100 ratio and bronchodilator response (BDR) at mid-childhood and early-teen follow-up time points (Table 4). There was no significant association between sIL6Rα and FEV1/FVCx100 ratio at either time point. PGLYRP-1 and sIL6Rα were not associated with BDR at either time point. However, there was trend toward an association between PGLYRP-1 concentration and FEV1/FVCx100 ratio at mid-childhood (adjusted β [95% CI]: 1.18 [–0.18, 2.56] per 1 SD increase, p-value=0.09) and significant association at the early-teen follow up (adjusted β [95% CI]: 1.15 [0.20, 2.10] per 1 SD increase, p-value=0.02) (Figure 5B).

**Table 4.**
 Association between serum protein concentration and pulmonary function.


<table>
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th colspan="2">Mid-childhood</th>
      <th colspan="2">Early-teen</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th>FEV1/FVCx100 β (95% CI)</th>
      <th>BDR β (95% CI)</th>
      <th>FEV1/FVCx100 β (95% CI)</th>
      <th>BDR β (95% CI)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>PGLYRP-1 Z-score*</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Univariate</td>
      <td>1.38 (0.15, 2.61)</td>
      <td>0.10 (−1.83, 2.03)</td>
      <td>1.45 (0.49, 2.42)</td>
      <td>−0.68 (−1.54, 0.17)</td>
    </tr>
    <tr>
      <td></td>
      <td>Model 1†</td>
      <td>1.12 (−0.18, 2.41)</td>
      <td>0.53 (−1.44, 2.51)</td>
      <td>1.05 (0.11, 1.98)</td>
      <td>−0.49 (−1.40, 0.41)</td>
    </tr>
    <tr>
      <td></td>
      <td>Model 2‡</td>
      <td>1.38 (0.08, 2.69)</td>
      <td>0.61 (−1.40, 2.63)</td>
      <td>1.53 (0.54, 2.53)</td>
      <td>−0.58 (−1.49, 0.34)</td>
    </tr>
    <tr>
      <td></td>
      <td>Model 3#</td>
      <td>1.19 (−0.19, 2.56)</td>
      <td>1.00 (−1.04, 3.04)</td>
      <td>1.15 (0.20, 2.10)</td>
      <td>−0.35 (−1.29, 0.59)</td>
    </tr>
    <tr>
      <td>sIL6Rα Z-score*</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>Univariate</td>
      <td>0.95 (−0.31, 2.20)</td>
      <td>−0.38 (−2.45, 1.69)</td>
      <td>0.11 (−0.86, 1.09)</td>
      <td>0.65 (−0.24, 1.54)</td>
    </tr>
    <tr>
      <td></td>
      <td>Model 1†</td>
      <td>0.96 (−0.30, 2.21)</td>
      <td>−0.37 (-2.41, 1.67)</td>
      <td>0.02 (−0.87, 0.92)</td>
      <td>0.71 (−0.19, 1.61)</td>
    </tr>
    <tr>
      <td></td>
      <td>Model 2‡</td>
      <td>0.88 (−0.40, 2.16)</td>
      <td>−0.62 (−2.62, 1.39)</td>
      <td>−0.02 (−1.00, 0.97)</td>
      <td>0.75 (−0.17, 1.66)</td>
    </tr>
    <tr>
      <td></td>
      <td>Model 3#</td>
      <td>0.92 (−0.36, 2.20)</td>
      <td>−0.11 (−0.96, 0.70)</td>
      <td>−0.05 (−0.94, 0.85)</td>
      <td>0.79 (−0.12, 1.69)</td>
    </tr>
  </tbody>
</table>

_*Serum protein concentrations were log10 transformed and converted into an internal Z-score.†Serum protein concentrations were log10 transformed and converted into an internal Z-scoreupplemental Data\\Table 4_Association pulmonary outcomes.xlsx’ "Shed's race/ethnicity.‡(Mother's demographics): adjusted for maternal pre-pregnancy BMI, maternal race/ethnicity, maternal level of education, maternal atopy, antibiotic exposure during pregnancy, smoking during pregnancy, 6 months or 1 year.#Model 3 (all demographics and birth characteristics): adjusted for all demographics and characteristics in models 1 and 2 except maternal race/ethnicity. This the reported value in manuscript._

To further our understanding of the relationship between PGLYRP-1 and outcomes, we performed two secondary analyses of models adjusted for all demographics and birth characteristics. First, we assessed the total variance explained by the regression model adjusting for both birth characteristics and demographics, and the variance explained by each of the individual predictors in the model. Assessing current asthma risk at mid-childhood, the regression model explained approximately 18% of the variance, and PGLYRP-1 was the most important predictor. Assessing current FEV1/FVCx100 at early-teen time point, the model explained approximately 26% of variance, and PGLYRP-1 was the second most important predictor (Figure 5—figure supplement 2). Second, to identify covariates that modify the effect of PGLYRP-1, we performed subset analyses (Figure 5—figure supplement 3). Small for gestational age and children identified by their mothers as ‘Other’ race/ethnicity displayed significantly different associations between PGLYRP-1 and mid-childhood asthma. Small for gestational age and children with obese mothers displayed significantly different associations between PGLYRP-1 and FEV1/FVC.

## Discussion

Our study has identified a novel association between epidemiologic risk, neutrophil-specific granules, and pediatric pulmonary outcomes. These findings implicate a role for PGLYRP-1 and other specific granule proteins as predictors of pediatric asthma risk and pulmonary function. This is in contrast to sIL6Rα, which is not localized to specific granules, its protein abundance is not regulated by transcription, and is not associated with any pulmonary outcomes.

By pooling the meta-analysis results, we established an association between multiple risk factors and the expression of genes involved in innate immunity and nucleic acid metabolism. We hypothesized that this gene signature represents increased myelopoiesis in utero and correlates with perinatal risk for pediatric asthma. During the process of myeloid cell differentiation, production of proteins responsible for defense against microbes and pro-inflammatory signaling (e.g., IL-1β) are amplified, while translational activity and nucleolar size wane (Zhu et al., 2017; Grassi et al., 2018). In our analysis, lower risk genes had higher expression in myeloid cells, most notably neutrophils. The low-risk genes were enriched for those that are implicated in defense responses towards bacteria and fungi. Additionally, this gene signature was strongly correlated with gestational age at birth, newborn sex, and birthweight (weaker association with maternal PP BMI). Our findings parallel previous literature, which has demonstrated that preterm birth, male sex, and low birthweight are associated with reduced abundance of neutrophils and monocytes (Glasser et al., 2015).

Our replication of the pooled meta-analysis with the UIH cohort pointed toward genes located and involved in the biology of neutrophil-specific (secondary) granules. In particular, lower risk individuals had higher expression of genes whose protein products are luminal (PGLRYP1, LTF, PTX3, CHI3L1, CAMP, SLPI) and membrane (CEACAM8, MS4A3, OLR1) components of specific granules (Rørvig et al., 2013). We demonstrate that the additive effect of multiple risk factors is associated with the reduction of transcription and protein products of specific granules in umbilical cord blood serum. Notably, our re-analysis of mass cytometry and proteomic data demonstrated a correlation between PGLYRP-1 in serum and neutrophil abundance (Olin et al., 2018). Previous literature has shown that deficiency of secretory leukocyte protease inhibitor (SLPI) leads to impairment of neutrophil development and abundance (Klimenkova et al., 2014). Furthermore, individuals with specific granule deficiency syndrome have abnormal neutrophil morphology, increased susceptibility to infections, and increased risk of acute myeloid leukemia (Lekstrom-Himes et al., 1999). Thus, this further supports the notion that neutrophil differentiation and survival is partially dependent on secondary granule generation.

To further investigate how these findings are related to pediatric asthma, we chose to compare PGLYRP-1, sIL6Rα, and their associations with asthma and lung function outcomes. PGLYRP-1 and sIL6Rα were chosen because both were correlated with neutrophil abundance, yet they are derived from different processes. Variation in abundance of PGLYRP-1 in serum is due to changes in neutrophil degranulation and transcription of PGLYRP1, whereas sIL6Rα is derived from receptor shedding and differential splicing of its mRNAs (Jones et al., 2001; Read et al., 2015). Thus, if perinatal neutrophil abundance is associated with pediatric asthma, both PGLYRP-1 and sIL6Rα should demonstrate associations with these outcomes. In contrast, we observed a significant relationship between mid-childhood asthma and PGLYRP-1, not sIL6Rα. These data indicate that serum abundance of specific granule contents likely has a larger and more significant association with pediatric asthma risk compared to the abundance of cord blood neutrophils.

PGLYRP-1 concentration was associated with gestational age, sex, and mode of delivery. Gestational age at birth, sex, mode of delivery, and birthweight may influence not only the abundance of neutrophils, but also their functionality (e.g. phagocytosis, cytokine production, respiratory burst) (Lawrence et al., 2017). In contrast, sIL6Rα was only associated with maternal self-reported race, specifically in those who were Black/African-American. Notably, individuals of African descent on average have baseline lower neutrophil counts without any functional consequences (Reich et al., 2009). Together, this highlights that PGLYRP-1 is a potential serologic marker of neutrophil functional maturity whereas sIL6Rα likely represents the total neutrophil abundance at birth.

Whether PGLYRP-1 has a causal role in asthma pathogenesis or is merely a biomarker for risk remains to be determined. PGLYRP-1 has antimicrobial function, although the concentration we observed in cord blood is below those reported for in vitro studies (Kashyap et al., 2011; Liu et al., 2000; Wang et al., 2007). PGLYRP-1 functions synergistically in vitro with other antimicrobials (e.g. lysozyme), so potential benefit as an antimicrobial cannot be ruled out considering that pglyrp-1−/− mice are more susceptible to infections (Liu et al., 2000; Wang et al., 2007; Dziarski et al., 2003; Ghosh et al., 2009; Gupta et al., 2020; Osanai et al., 2011). Interestingly, mammalian PGLYRP-1 does not hydrolyze peptidoglycan, and its orthologs appear divergent from ancestral PGLYRPs, which contain enzymatic activity; thus, it may have roles other than that of an antimicrobial (Dziarski and Gupta, 2006). It is also possible that other individual specific granule proteins or their cumulative effects are associated with pediatric asthma. Further studies will be required to determine a mechanistic role for either PGLYRP-1 or other specific granule proteins.

Several murine studies link PGLYRP-1 to increased airway resistance and perturbed immunity in response to house dust mite (Park et al., 2013; Yao et al., 2013). Contextualization of the murine studies with our results is largely confounded by the fact these murine studies have utilized adult mice deficient in PGLYRP-1 via germ-line deletion. These studies have largely demonstrated that the genetic absence of pglyrp1 leads to moderately reduced airway resistance, IgE, and T2 cytokine production in response to house dust mite exposure after sensitization. Notably, genetic absence of pglyrp1 does not completely protect against airway inflammatory changes. Furthermore, one study has demonstrated that bone marrow reconstitution with WT bone marrow prior allergen sensitization abrogates this effect (Yao et al., 2013), suggesting PGLYRP-1 presence in adult mice at the time of sensitization is responsible for increased airway resistance and perturbed immunity. These results are not entirely surprising as PGLYRP-1 is reported to be a pro-inflammatory TREM-1 ligand and thus may propagate inflammation (Read et al., 2015). Extending this point, there are reported associations between increased serum PGLYRP-1 and systemic inflammatory conditions in adulthood (e.g. rheumatoid arthritis, cardiovascular disease) (Luo et al., 2019; Rohatgi et al., 2009). Beyond its role at time sensitization, PGLYRP-1 and many of the other specific granule proteins are dramatically reduced in serum concentration 1 week postnatal compared to cord blood and not well correlated with their cord blood concentration, suggesting an important temporal role and variation of these proteins (Olin et al., 2018). This temporal variation is largely ignored in experimental approaches such as germ-line knock outs.

Although our findings contribute to our understanding of the risk for pediatric asthma, there are several limitations. Our data is derived from observational data that limits any interpretation of causation and is potentially susceptible to confounding by unmeasured variables. The findings of association between PGLYRP-1 mid-childhood asthma and adolescent FEV1/FVC were robust when adjusting for measured confounders and subset analysis. Additionally, transcription in cord blood pglyrp1 in our meta-analysis and PGLYRP-1 concentration in the three cohorts was significantly associated with both sex and gestational age. This suggests that our results are plausibly generalizable to a larger population. Additionally, as with many prospective cohorts, the Project Viva cohort had increasing loss to follow up over time. At the early-teen follow up, we did not observe a significant association with current asthma. It is important to note that there was still an association between PGLYRP-1 and FEV1/FVC at this time point. These observations could be due to two possibilities. First, at early-teen follow up, there was only 9% prevalence of current asthma in the Project Viva subset, whereas the full cohort had a 15% prevalence. This difference is likely due to higher non-response rates in the asthmatic sub-group as 24 of the 35 (68%) had missing responses, whereas only 46 of 171 (27%) of non-asthmatics had missing responses. This lead to a reduction in power at the early-teen follow-up time point, potentially leading to a false negative result. Second, PGLYRP-1 might be inversely associated with FEV1/FVC in adolescence secondary to early-life pulmonary dysfunction (e.g. mid-childhood asthma). Reduced expiratory pulmonary function later in adolescences and even into adulthood is associated with individuals who were diagnosed with asthma in childhood (Bui et al., 2018; Lo et al., 2020; Piccioni et al., 2015; Turturice et al., 2017b). We view these possibilities as equally probable as current pediatric asthma can also impair FEV1/FVC (Tse et al., 2013). Further investigation will be needed to elucidate the role of PGLYRP-1 in adolescent asthma.

In conclusion, we have identified a neutrophil development gene signature that is associated with perinatal asthma risk. A soluble specific granule protein, PGLYRP-1, was strongly associated with odds of asthma in childhood and pulmonary function in childhood and adolescence. This suggests that perinatal granulopoiesis has a significant impact on the development of pediatric asthma and lung function.

## Materials and methods

**Key resources table**


<table>
  <thead>
    <tr>
      <th>Reagent type (species) or resource</th>
      <th>Designation</th>
      <th>Source or reference</th>
      <th>Identifiers</th>
      <th>Additional information</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Gene (Homo sapiens)</td>
      <td>Homo sapiens Genome Assembly</td>
      <td>Ensembl</td>
      <td>GRCh38.12</td>
      <td></td>
    </tr>
    <tr>
      <td>Biological sample (Homo sapiens)</td>
      <td>Primary Cord Blood Mononuclear Cells</td>
      <td>Volunteers</td>
      <td>UIH Cohort</td>
      <td>Demographics reported in Supplementary file 5</td>
    </tr>
    <tr>
      <td>Biological sample (Homo sapiens)</td>
      <td>Cord Blood Serum</td>
      <td>Volunteers</td>
      <td>UIH Cohort Project Viva</td>
      <td>Demographics reported in Supplementary files 5 and 7</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Human PGLYRP1/PGRP-S DuoSet ELISA</td>
      <td>R and D Systems</td>
      <td>DY2590</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Human IL6Ra DuoSet ELISA</td>
      <td>R and D Systems</td>
      <td>DY227</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>RNeasy Mini Kit</td>
      <td>Qiagen</td>
      <td>74104</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>RNA 6000 Nano Kit</td>
      <td>Agilent</td>
      <td>5067–1511</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Qubit RNA HS Assay Kit</td>
      <td>Thermo Fisher Scientific</td>
      <td>Q32852</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>TruSeq Stranded mRNA Library Prep Kit</td>
      <td>Illumina</td>
      <td>20020594</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>HiSeq × Ten Reagent Kit v2.5</td>
      <td>Illumina</td>
      <td>FC-501–2501</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>R</td>
      <td>R</td>
      <td>Version 3.6.3</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>geoquery</td>
      <td>Bioconductor</td>
      <td>Version: 2.36.0</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GeneMeta</td>
      <td>Bioconductor</td>
      <td>Version: 1.54.0</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>tximport</td>
      <td>Bioconductor</td>
      <td>Version: 1.10.1</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>DESeq2</td>
      <td>Bioconductor</td>
      <td>Version: 1.22.2</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>relaimpo</td>
      <td>CRAN</td>
      <td>Version: 2.2–3</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>salmon</td>
      <td>Github</td>
      <td>Version 0.12.00</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GSEA</td>
      <td>gsea-msigdb.org</td>
      <td>Version 4.0</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Human subject Project Viva cohort

The current study was approved by the University of Illinois at Chicago IRB (#2016–0326) and the IRB of Harvard Pilgrim Health Care. Volunteers were recruited from women attending their first prenatal visit at one of eight practices of Atrius Harvard Vanguard Medical Associates. The exclusion criteria were multiple gestation, inability to answer questions in English, gestational age ≥ 22 weeks at recruitment, and plans to move away before delivery. The cohort profile was previously described by Oken and colleagues (Oken et al., 2015).

Current mid-childhood asthma was defined as a ‘yes’ response to ‘Has a health professional ever told you that your child has asthma?’ and ‘yes’ to either ‘In the past 12 months, has child taken or been prescribed Albuterol, Cromolyn, Nedocromil, Montelukast, inhaled corticosteroids, or Prednisone’ or ‘In the past 12 months, has your child ever had wheezing (or whistling in the chest)?’. We used as a comparison group those with no asthma diagnosis and no asthma medication use or wheezing in the past 12 months. We used the same definition for current asthma in early adolescence, except the time reference for asthma medication was ‘in the past month’. Ever asthma was defined as a ‘yes’ response to ‘Has a health professional ever told you that your child has asthma?’ within either the mid-childhood or early-teen follow-up periods. We used as a comparison group those with no asthma diagnosis. Individuals with missing data were not used in regression models assessing current or ever asthma outcomes. Individuals with missing data are reported in demographics tables and displayed in figure as ‘Missing Data’.

Methods for obtaining spirometric measurements and BDR have been described previously (Tse et al., 2013). In brief, spirometry was performed with the EasyOne Spirometer (NDD Medical Technologies, Andover, MA). Post-bronchodilator spirometric measures were obtained at least 15 min after administration of two puffs (90 μg per puff) of albuterol. Spirometric performance was required to meet American Thoracic Society criteria for acceptability and reproducibility, with each subject producing at least three acceptable spirograms, two of which must have been reproducible (Oken et al., 2015; Miller, 2005).

### Human subject University of Illinois Hospital cohort

The current study was approved by the University of Illinois at Chicago IRB (#2015–0353). Women seeking prenatal care at the University of Illinois at Chicago (UIC) Center for Women’s Health were recruited as volunteers in their third trimester (29–33 weeks of gestation) between 2014 and 2017. The cohort profile has been previously described by Koenig and colleagues (Koenig et al., 2020). Inclusion criteria were as follows: singleton pregnancy; naturally conceived pregnancy; 17–45 years of age; pre-pregnancy BMI ≥ 18.5; <34 weeks of gestation; sufficient fluency in English to provide consent and complete the study; and ability to independently provide consent. Exclusion criteria were as follows: live birth or another pregnancy (including ectopic and molar pregnancies) in the previous 12 months; pre-eclampsia; gestational diabetes mellitus or previously diagnosed type 1 or type 2 diabetes; autoimmune disorder; current or previous premature rupture of membranes or chorioamnionitis; previous spontaneous premature birth; current bacterial or viral infection; current steroid or anti-inflammatory treatment; history of bariatric surgery; malabsorptive condition (e.g., celiac disease); current hyperemesis; hematologic disorder (e.g., sickle cell anemia or trait, hemochromatosis); current tobacco use; alcohol consumption or illicit drug use; and current use of medications that decrease nutrient absorption (e.g., proton pump inhibitors). All women provided written informed consent.

### Umbilical cord blood specimens

For Project Viva, procedures for obtaining umbilical cord blood serum have been describe previously (Schaub et al., 2005). For the UIH cohort, umbilical cord blood was obtained by venipuncture shortly after time of delivery. Blood (approximately 5 mL per tube) was drawn into Red Top Serum Plus and Green Top Sodium Heparin 95 USP Units Blood Collection Tubes (BD Vacutainer). Red Tops were allowed to stand upright at room temperature for 30 min prior centrifugation at 1500 × g for 10 min at room temperature. Supernatants (serum) were collected, aliquoted, and stored at −80°C until further processing. Heparinized blood obtained in Green Tops was diluted 1:1 in 1× phosphate-buffered saline, pH 7.4 (PBS) and overlaid onto Ficoll-Paque Plus (GE Healthcare) density gradients. Density gradients were centrifuged at 400 × g for 30 min at room temperature without brake. Upper phase (diluted plasma) was drawn off, aliquoted, and stored at −80°C. Buffy coats (CBMCs) were drawn off, washed twice with 10 mL of 1× PBS, aliquoted, and stored in 500 mL of RNAlater (Qiagen). Viability and number of cells isolated were determined by diluting cellular suspensions 1:1 with Trypan Blue Solution 0.4% (wt/vol) in PBS (Corning) and counting live/dead cells > 7 μM using a TC20 Automated Cell Counter (Bio-Rad). The viability of isolated cells was >90% for all samples. Time from delivery to storage was recorded for every sample.

### RNA extraction and sequencing

Total RNA was extracted from CBMCs using RNeasy kits (QIAGEN) following manufacturers protocol except for switching 70% ethanol for 100% ethanol. The quality and quantity of all the extracted RNA were analyzed with a RNA 6000 Nano Kit on the 2100 Bioanalyzer Instrument (Agilent) and ssRNA High Sensitivity Kit and Qubit (Invitrogen). RIN for all samples was >8. RNA was constructed into barcoded libraries using the TruSeq Stranded mRNA Library Prep Kit (Illumina). The pooled libraries were sequenced for a paired-end 151 read length. The DNA libraries were sequenced on HiSeq X Ten platform using HiSeq Reagent v2.5 kit (Illumina), following manufacturer's protocol.

### Enzyme-linked immunosorbent assays (ELISA)

PGLYRP-1 and sIL6Rα were assessed using Human PGLYRP1/PGRP-S DuoSet Elisa and Human IL-6 R alpha DuoSet Elisa (R and D Systems). Serum was diluted with 1% bovine serum albumin in PBS (pH 7.2–7.4, 0.2 micron filtered) at 1:100 for PGLYRP-1 and 1:300 for sIL6Rα. ELISAs were performed according to manufacturer’s protocol. All samples were run in duplicate. Optical densities were assessed at 450 and 540 using a Spectra Max M5 (Molecular Devices). The intra- and inter-plater CVs for PGLYRP-1 were 2.4% and 11.0%. The intra- and inter-plater CVs for sIL6Rα were 3.8% and 18.9%.

### Statistical analysis

All statistical analyses were performed in R (https://www.r-project.org/) unless otherwise specified.

### Meta-analysis

To identify dataset studies used in the meta-analysis, NCBI’s Gene Expression Omnibus (https://www.ncbi.nlm.nih.gov/geo) was searched using the search ‘(cord blood) AND ‘Homo sapiens’ [porgn:_txid9606]’ and was limited to study types that included expression profiling by array. This search yielded 352 studies that were further examined for cell types assessed and metadata reported. Seventeen studies met inclusion criteria of reporting metadata regarding at least one perinatal risk factor (e.g. gestational age at birth, newborn sex, birthweight, maternal pre-pregnancy BMI, smoke exposure, mode of delivery), and expression data from either whole cord blood or CBMCs derived from human subjects. Expression, feature, and subject demographic data were extracted using geoquery (Davis and Meltzer, 2007). If expression data was non-normalized, it was quantile normalized and log2 transformed. Six studies were excluded due to no variability in demographic data (i.e. only males) or low data quality, leaving 605 unique cord blood gene expression samples. To assess associations between gene expression and perinatal risk factors, univariate, inverse variance weighted, random-effects models were constructed for genes using the GeneMeta package (GeneMeta, 2020). Newborn sex (Male vs. Female), maternal pre-pregnancy BMI (continuous: 0 = BMI < 18.5, 1 = 18.5 ≤ BMI < 25, 2 = 25 ≤ BMI < 30, 3 = 30 ≤ BMI), gestational age at birth in weeks (continuous), and birthweight in grams (continuous) were assessed as perinatal risk factors. Significant genes were defined as Benjamini–Hochberg correct p-value<0.01. The z-score for each gene was averaged across each univariate test (Equation 1) and termed pooled z-score. It was used to assess how likely a gene is effected by multiple risk factors. If a gene was not assessed in one of the univariate analyses while assessed in others, the missing data was inferred as a z-score of zero. To determine cell enrichment, genes expression in each cell as defined by HPA (Uhlen et al., 2010; Monaco et al., 2019) were modeled as a function of the pooled z-score using general additive model with cubic splines function. To determine biological processes enriched in the low- vs. high-risk individuals, the pooled z-score was used a pre-ranked list for gene set enrichment analysis for GO biologic processes using GSEA (Subramanian et al., 2005). Significantly enriched GO terms were defined as Benjamini-Hochberg correct p-value<0.01. Spearman’s correlations between pooled z-score, univariate z-scores, and individual dataset z-scores were determined in R.

$$
Z_{pooled}=\frac{((Z_{Male}+ Z_{PPBMI}) −(Z_{GA}+ Z_{BW}))}{4}
$$

### RNA sequencing statistical analysis (UIH cohort)

The sequences were quality controlled by filtering out all low-quality reads (<25 on Phred quality score) and short reads (<50 bp). Transcripts were annotated using salmon v0.12.0 and Ensembl Homo sapiens Genome Assembly GRCh38.12 (Patro et al., 2017). Transcript counts were aggregated in gene-level counts using the tximport package in R (Soneson et al., 2015). Genes with median counts across samples < 10 were filtered out, leaving 14,055 genes remaining whose expression normalized using median sum scaling. Normalized gene expression was modeled as function of the number of perinatal risk factors (gestational age < 37 weeks, birthweight < 3000 g, PP BMI >30, male) using DESeq2 (Love et al., 2014). Genes were ranked for replication by their product of their pooled z-score and RNAseq z-score, termed RS (Equation 2). A cutoff of RS > 3 was used to determine candidate genes associated with pediatric asthma risk. Candidate gene biologic process and cellular component enrichment were performed using STRING with default settings (Szklarczyk et al., 2019). Data from RNAseq is available on NCBI SRA database ID PRJNA577955.

$$
RS_{}=Z_{pooled}\timesZ_{RNAseq}
$$

### Secondary statistical analysis of mass cytometry and ProSeek data (Olin et al.)

Methods for data acquisition for cell population percentages and protein abundances using mass cytometry and ProSeek are reported by Olin et al., 2018. Cell population percentages were transformed using centered log-ratios. Cell populations and protein abundances, and number of risk factors for each individual (gestational age < 37 weeks, male, birthweight < 3000 g, birth via c-section) were correlated (Pearson’s method). For cell population correlations with number of risk factors, significance was defined as Bonferroni corrected p-value<0.05. Proteins determined to neutrophil associated were determined by those expressed in CBMC (UIH cohort) and enriched in neutrophils HPA (Uhlen et al., 2010).

### Asthma and pulmonary outcome statistical analysis (Project Viva)

Outcomes assessed in Project Viva Categorical outcomes were modeled using logistic regression. Continuous outcomes were modeled using linear regression. Four regression models were used for each outcome: univariate/unadjusted model 1 adjusted for child’s demographics (gestational age at birth in weeks, birthweight adjusted for gestational age and sex, mode of delivery, sex, and race/ethnicity), model 2 adjusted for maternal demographics (PP BMI, race/ethnicity, level of education, atopy, antibiotic use during pregnancy, and smoking during pregnancy, 6 months, or 1 year), and model 3 adjusted for both mother and child’s demographics (excluding maternal race/ethnicity). For regression models, PGLYRP-1 and sIL6Rα were log10 transformed and standardized to internal z-score. Subset analysis was performed by splitting the full data set by categorical variables and modeling outcomes as function of PGLYRP-1 in each subset using the univariate model. R (Jaakkola et al., 2006) for each variable in linear regression model 3 was determined using the relaimpo package (Groemping, 2006). Mcfadden’s pseudo-R (Jaakkola et al., 2006) for each variable in model 3 was calculated for logistic regression using full models minus the variable of interest.
