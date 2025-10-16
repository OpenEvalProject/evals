# Integrative genomic analysis of the human immune response to influenza vaccination

## Authors

- Luis M Franco<sup>1</sup>
- Kristine L Bucasas<sup>1</sup>
- Janet M Wells<sup>3</sup>
- Diane Niño<sup>3</sup>
- Xueqing Wang<sup>4</sup>
- Gladys E Zapata<sup>4</sup>
- Nancy Arden<sup>5</sup>
- Alexander Renwick<sup>6</sup>
- Peng Yu<sup>1</sup>
- John M Quarles<sup>5</sup>
- Molly S Bray<sup>4</sup>
- Robert B Couch<sup>2</sup>
- John W Belmont<sup>1</sup> †
- Chad A Shaw<sup>1</sup>

### Affiliations

1. Department of Molecular and Human Genetics Baylor College of Medicine Houston United States
2. Department of Medicine Baylor College of Medicine Houston United States
3. Department of Molecular Virology and Microbiology Baylor College of Medicine Houston United States
4. Children’s Nutrition Research Center Baylor College of Medicine Houston United States
5. Department of Microbial and Molecular Pathogenesis Texas A&M University System Health Science Center College Station United States
6. Interdepartmental Program in Structural and Computational Biology and Molecular Biophysics Baylor College of Medicine Houston United States

† Corresponding author

## Abstract

10.7554/eLife.00299.001 Identification of the host genetic factors that contribute to variation in vaccine responsiveness may uncover important mechanisms affecting vaccine efficacy. We carried out an integrative, longitudinal study combining genetic, transcriptional, and immunologic data in humans given seasonal influenza vaccine. We identified 20 genes exhibiting a transcriptional response to vaccination, significant genotype effects on gene expression, and correlation between the transcriptional and antibody responses. The results show that variation at the level of genes involved in membrane trafficking and antigen processing significantly influences the human response to influenza vaccination. More broadly, we demonstrate that an integrative study design is an efficient alternative to existing methods for the identification of genes involved in complex traits. DOI: http://dx.doi.org/10.7554/eLife.00299.001

## Introduction

Influenza remains one of the major threats to human health worldwide and is responsible for an estimated 250,000–500,000 deaths each year (World Health Organization, 2009). Attempts at immunization pre-dated the isolation of the virus from humans in 1933 (Smith et al., 1933) and vaccination remains the cornerstone of prevention strategies. Since 1977, strains of influenza A (H3N2), influenza A (H1N1), and influenza B have been responsible for the majority of documented human infections and trivalent vaccines are updated annually to contain the circulating strains. Animal models have demonstrated that immune responses and susceptibility to influenza infection can be strongly influenced by host genetic factors (Trammell and Toth, 2008; Srivastava et al., 2009). As with viral infection, variability in the immune response to vaccination is likely to be influenced by genotype. Accordingly, twin and sibling studies have shown heritability estimates as high as 45% for a varicella vaccine (Klein et al., 2007) and 90% for a measles vaccine (Tan et al., 2001). Studies investigating influenza vaccine immunogenicity in humans have consistently shown large inter-individual variability, but the genetic contribution to this variability remains poorly understood.

Gene expression is strongly controlled by common genetic variants (Morley et al., 2004; Stranger et al., 2007) with both broad (Bullaughey et al., 2009) and tissue-specific effects (Innocenti et al., 2011; Rotival et al., 2011), referred to as expression quantitative trait loci (eQTL). Moreover, genome-wide association studies have identified hundreds of variants associated with human disease risk that are also eQTL, implying that the mechanism by which they influence risk involves variation in transcriptional responses (Emilsson et al., 2008; Cookson et al., 2009; Naukkarinen et al., 2010; Nicolae et al., 2010; Rotival et al., 2011; Barreiro et al., 2012) Finally, integrative genomic studies in model organisms (Schadt et al., 2005; Amit et al., 2009) have demonstrated that the combination of genetic and transcriptional information can allow direct tests of causal mechanisms in controlled experiments. We hypothesized that integrating genome-wide genotype data with serial measurements of the transcriptional and humoral responses to an influenza vaccine in a clinical study could be used to identify loci that influence vaccine responsiveness and subsequent immunity to influenza in humans.

We immunized an ethnically homogeneous group of 119 healthy adult male volunteers with licensed trivalent influenza vaccine. DNA was obtained from peripheral blood and genome-wide SNP genotyping was performed. We also measured global transcript abundance in peripheral blood RNA specimens before and at three time points (days 1, 3, and 14) after vaccination. Type-specific antibody measurements (H1N1, H3N2, and FluB) were made in serum samples before and at two time points (days 14 and 28) after vaccination. An identical study was then carried out with an independent validation cohort of 128 ethnically homogeneous healthy adult female volunteers. This experimental design allowed us to search for loci that show evidence of a transcriptional response to vaccination, genetic regulation of gene expression (cis-acting eQTL), and correlation between gene expression and the magnitude of the antibody response.

## Results

## Multiple genes show evidence of a transcriptional response to the vaccine and genetic regulation of expression

We performed mixed model regression analysis with SNPs located in 1-Mb intervals around each expression reporter sequence. We began by identifying SNP-transcript pairs with both significant evidence of a

![Figure 1.](https://cdn.elifesciences.org/articles/00299/elife-00299-fig1-v2.jpg)

**Figure 1.:** Manhattan plots of the genotype-expression—log10 p-values across the genome for the discovery (inner circle) and validation (outer circle) cohorts. Each dot represents a SNP-transcript pair. Red dots indicate SNP-transcript pairs for which there is evidence of significant genotype-expression association (genotype p<5 × 10−8) and evidence of a transcriptional response to the vaccine (day effect p<0.05). The 78 genes that showed both properties in the two cohorts are shown in the outer margin.DOI: http://dx.doi.org/10.7554/eLife.00299.003

## At some loci, the genetic effect is enhanced or only apparent after the experimental perturbation

We hypothesized that, at some loci, the magnitude of the genetic effect could be different before and at different time points after vaccination. This type of effect, which would not be observed in a cross-sectional study design, could be directly examined with our serial expression data. We analyzed the additive effect of genotype on expression at each day in the study. Using a

![Figure 2.](https://cdn.elifesciences.org/articles/00299/elife-00299-fig2-v2.jpg)

**Figure 2.:** (A) A specific example of this phenomenon: local Manhattan plots for the gene NECAB2 before and on day 3 after vaccination in each of the two cohorts, showing an increase in the magnitude of the genotype effect (R2g) after the experimental perturbation. (B) An increase in R2g after the experimental perturbation is a general feature of the SNP-transcript pairs that show a strong cis-eQTLs and a transcriptional response to vaccination (left). The within-genotype variance is unchanged (MSE, center), while the strength of the genotype effect on expression (slope of the additive association; β, right) increases, suggesting that the latter is the main driver for the observed increase in the genetic effect after vaccination.DOI: http://dx.doi.org/10.7554/eLife.00299.004

Theoretically, the observed temporal changes in the estimated genotype effect after vaccination could be driven by an increase in the effect size, a relative decrease in the variability within genotype strata, or both. We analyzed all SNP-transcript pairs for loci at which we observed both a strong cis-acting eQTL and a transcriptional response to vaccination, calculating the relative magnitude of slope and within-genotype variance between the pre-vaccination and maximal Rg2 time points. Figure 2B shows that an increase in the strength of the genotype effect (slope of the additive association) was the main driver for the observed change in Rg2, and that this amplitude change was a general feature of the loci in which we observed both a strong cis-acting eQTL and a transcriptional response to the vaccine stimulus. The delta-Rg2 values were consistent between the cohorts when evaluated by Spearman’s rank correlation analysis using all SNP-transcript pairs (Cor = 0.25, p<2 × 10−16). To select a conservative set of candidate loci based on this property for further analysis, we identified the SNP-transcript pairs that were in the top 1% of the delta-Rg2 distribution and also showed evidence of a strong cis-acting eQTL (genotype effect p<5 × 10−8), in both cohorts. Data for the resulting set of 146 SNP-transcript pairs, including Rg2 values, are provided in Table 2 via the Interactive Results Tool (which is also available to download from Zenodo and shown within Supplementary file 1).

## Content analysis shows enrichment for genes involved in membrane trafficking, antigen processing, and antigen presentation

Of the 78 genes that had the strongest validated evidence of a genotype effect and a transcriptional response to the vaccine, 14 were also in the list of 34 genes with the strongest evidence of an increase in the magnitude of the genetic effect after vaccination. Content analysis on the union of the two sets (98 genes) showed significant enrichment for genes involved in antigen processing and presentation, cytotoxic T-lymphocyte-mediated apoptosis of target cells, dendritic cell maturation and function, and membrane trafficking (

![Figure 3.](https://cdn.elifesciences.org/articles/00299/elife-00299-fig3-v2.jpg)

**Figure 3.:** Barplots show categories with significant overrepresentation in the list of 98 genes with a strong cis-eQTL and a response to vaccination expressed as either a transcriptional response or a change in the genetic effect in both cohorts. The negative log(p-value) is plotted on the x-axis.DOI: http://dx.doi.org/10.7554/eLife.00299.005

## Integration of genotype, expression, and antibody titer data identifies 20 genes with the strongest evidence for genetic variation influencing the humoral immune response to influenza vaccination

We and others have shown that for some transcripts there is significant correlation between the magnitude of the transcriptional and antibody responses to the vaccine stimulus (

![Figure 4.](https://cdn.elifesciences.org/articles/00299/elife-00299-fig4-v2.jpg)

**Figure 4.:** (A) Examples of positive (DYNLT1) and negative (ANKRD33) correlation between gene expression on day 1 and the magnitude of the antibody response to the vaccine. Data points and regression lines in the scatterplots display the results for the discovery (blue) and validation (magenta) cohorts. (B) A total of 301 genes showed evidence of significant correlation between gene expression and the antibody response to the vaccine in both cohorts. Of these, 281 showed evidence of positive correlation and 83 of negative correlation. Each individual is represented by a column in the heatmaps. The top heatmaps display the magnitude of the antibody response (titer response index). The bottom heatmaps display the deviations around the expression mean for each gene. Individual gene identifiers and correlation coefficients are presented in the Interactive Results Tool.DOI: http://dx.doi.org/10.7554/eLife.00299.006

![Figure 5.](https://cdn.elifesciences.org/articles/00299/elife-00299-fig5-v2.jpg)

**Figure 5.:** 20 genes show evidence of a transcriptional response to vaccination, significant genotype effects on gene expression, and correlation between the transcriptional and antibody responses. Remarkably, seven of these are involved in intracellular antigen transport, antigen processing, and antigen presentation.DOI: http://dx.doi.org/10.7554/eLife.00299.007

We determined genetic associations to the antibody response using 137 eQTL SNPs from these 20 loci. The quantile-quantile plot from the association tests performed on these SNPs shows marked deviation from the empirical null distribution for QTL associations (

![Figure 6.](https://cdn.elifesciences.org/articles/00299/elife-00299-fig6-v2.jpg)

**Figure 6.:** 137 SNP-transcript pairs with evidence of a strong cis-eQTL, a dynamic response to the vaccine (a change in transcript abundance or in the magnitude of the genetic effect), and correlation between the transcriptional and antibody responses were selected (result SNPs, in red). The empirical quantile-quantile plot of the result SNPs shows significant deviation from the empirical distribution of the entire data set (background SNPs, in blue).DOI: http://dx.doi.org/10.7554/eLife.00299.008

## The study design permits causal and reactive model analyses

We explored three types of associations in our work: genotype to gene expression (eQTL), gene expression to antibody titer, and genotype to antibody titer (QTL). We now considered alternative models for the relationships between these distinct types of association (

![Figure 7.](https://cdn.elifesciences.org/articles/00299/elife-00299-fig7-v2.jpg)

**Figure 7.:** (A) Three models were evaluated, each showing a candidate hypothesis for the three-way association between genotype (G), expression (E) and trait (T). In the independent model, expression and trait each associate with genotype but are not themselves directly related. In the causal model, expression mediates the association between genotype and trait. In the reactive model, genotype and expression relate through the trait, so that gene expression changes are a downstream response to the trait. (B) p-values for independent-versus-reactive and independent-versus-causal hypothesis tests. Each point shows the result for one SNP-transcript pair. Points to the right of the solid vertical line are significant (p<0.05) for the reactive hypothesis and points above the solid horizontal line are significant for the causal hypothesis. The dashed line shows a p=0.1 threshold. (C) Power for rejection of the independent hypothesis. Non-independent data were simulated with effect sizes and variances similar to those in the enrichment set (the set of SNP-transcript pairs that were found to be significant in our study). The curve shows the proportion of cases in which the simulated data rejected the independent (null) hypothesis. The dotted line indicates the combined sample size in our study.DOI: http://dx.doi.org/10.7554/eLife.00299.009

## Discussion

The results provide an unbiased integrative survey of the genetic and transcriptional components of the humoral immune response to influenza vaccination in humans. They suggest that variation at the level of genes involved in antigen processing and intracellular trafficking is an important determinant of vaccine immunogenicity. Even in healthy, young individuals, there are a significant number of people who do not develop a protective antibody response after influenza vaccination. If these individuals could be identified prior to vaccination, modifications to the type or dose of vaccine could be attempted, with the goal of reducing the number of unprotected vaccinated individuals. The genes identified in this study as playing a role in variation in the humoral response to vaccination would be a logical starting point for the development of DNA- or RNA-based predictive biomarkers. Prospective evaluation of such biomarkers would be the next step towards clinical implementation.

Understanding the mechanisms that underlie variation in response to the vaccine may also direct modification of factors that enhance the response. Most of the efforts to date have focused on vaccine adjuvants that activate known immunologic mechanisms. Surprisingly, many of the genes identified in this study encode proteins that are not specifically immune but play a more general role in membrane trafficking and intracellular transport. Interventions aimed at increasing vaccine antigen affinity to these proteins or altering their intracellular concentrations could represent new avenues in vaccine development.

More broadly, the results demonstrate that a longitudinal, integrative genomic analysis study design, applied to a clinical intervention, is an efficient alternative to cross-sectional methods for the identification of genes involved in medically relevant complex traits. By making repeated measurements on the same individual over time after a controlled experimental perturbation, we were able to account for individual variation in a way that would not have been possible otherwise. The dynamic nature of the measurements also allowed us to uncover genetic effects that are either enhanced by or only evident after the experimental perturbation. The specificity of gene identification in this study emerges from the genome’s acute response to the perturbation, which cannot be assessed by a cross-sectional eQTL analysis or a genome-wide association study. This approach could be used for a broad variety of medically important problems whenever there is the opportunity to test a well-controlled intervention such as drug, dietary, or vaccine responses.

Several limitations of the study are worth noting. First, we studied two samples of healthy young adults, thereby excluding the segments of the population that are most likely to have a poor response to influenza vaccination: children, the elderly, and individuals with severe illnesses. Second, in order to minimize the risk of false associations related to population stratification, we studied an ethnically homogeneous group of individuals. Third, while an interesting aspect of our study design is that it could open the door for direct comparisons of causal and reactive models, the sample size in this study was not sufficient to establish whether or not there is a causal relationship between the loci for which an association was identified and the antibody response to the vaccine. Finally, while antibody titers have historically been used to evaluate vaccine responsiveness, it is clear that they do not capture the complexity of the human immune response to vaccination. Additional studies would be necessary to determine whether the genes identified are also related to variation in influenza vaccine responses in groups other than the one chosen for this study, whether there is a causal relationship between these genes and the antibody response, or whether they also influence the cell-mediated immune response to the vaccine.

## Materials and methods

## Visual summary

A visual representation of the study design, the resulting data sets, and the integrative analysis scheme, is presented in

![Figure 8.](https://cdn.elifesciences.org/articles/00299/elife-00299-fig8-v2.jpg)

**Figure 8.:** (A) Individuals were immunized on day 0 and peripheral blood RNA samples were obtained on days 0, 1, 3, and 14. Antibody titers were measured on pre-immune sera and on days 14 and 28. Genotyping was carried out on a peripheral blood genomic DNA sample obtained on day 1. Identical sample collection schemes were used, 1 year apart, for the discovery (males) and validation (females) cohorts. (B) Sample sizes and data generation platforms. (C) Integrative analysis involved identification of loci that exhibit a transcriptional response to vaccination, evidence of genetic regulation of expression (constitutive eQTL), evidence of correlation between gene expression and the antibody response, and evidence of correlation between genotype and the antibody response (QTL). Because transcript abundance was measured serially, we were able to evaluate changes in the magnitude of the genetic effect on expression at different time points following vaccination. In addition, the study design permitted QTL analysis conditional on gene expression, which led to the identification of loci whose genetic effects on the antibody response are causally linked through the eQTL.DOI: http://dx.doi.org/10.7554/eLife.00299.010

## Study subjects

Healthy volunteers ages 18 to 40 years were enrolled. Individuals who were known to have received an influenza vaccine in the previous 3 years or who had signs or symptoms of an active infection at the time of enrollment were excluded. To minimize false-positive results related to population stratification, enrollment was limited to individuals of self-reported Caucasian ancestry. Enrollment, vaccination and sample collections were conducted at a university campus. The initial (discovery) cohort was restricted to males. The validation cohort was enrolled approximately 18 months after the initial cohort and was restricted to females. The protocol was approved by the institutional review boards of all participating institutions. Informed consent was obtained from each subject prior to enrollment.

## Vaccine

Study participants were immunized on day 0. Those enrolled in the initial cohort received the 2008–2009 inactivated trivalent influenza vaccine (A/Brisbane/59/2007[H1N1], A/Brisbane/10/2007[H3N2], B/Florida/4/2006; Sanofi-Pasteur, Lyon, France). The validation cohort received the 2009–2010 vaccine, which came from the same manufacturer and included (A/Brisbane/59/2007), (A/Brisbane/10/2007[H3N2]), and (B/Brisbane/60/2008) strains.

## DNA samples

Whole blood samples (7 ml) for DNA purification were collected in Vacutainer acid citrate dextrose (ACD) tubes (Beckton-Dickinson, Franklin Lakes, NJ), on day 1 after vaccination. DNA was purified using Qiagen Gentra Puregene Blood Kits (Qiagen Sciences, Germantown, MD). Quantitation and quality control were performed with a NanoDrop-1000 spectrophotometer (Thermo Fisher Scientific, Waltham, MA) and using the Quant-iT PicoGreen dsDNA Reagent (Life Technologies, Carlsbad, CA) in a Tecan GENios microplate reader (Tecan Group, Mannendorf, Switzerland).

## RNA samples

Peripheral blood samples for RNA purification were obtained immediately before (day 0) and on days 1, 3, and 14 after vaccination. To minimize changes in gene expression induced by sample handling and processing, whole-blood samples (2.5 ml) were collected in PAXgene RNA stabilization tubes (Qiagen Inc., Valencia, CA) and frozen at −80°C. RNA purification was performed using the PAXgene Blood RNA system (Qiagen Inc.). All RNA samples from an individual were consistently purified in the same batch. Spectrophotometry (NanoDrop-1000 Spectrophotometer; Thermo Fisher Scientific) and microfluidic electrophoresis (Experion Automated Electrophoresis System; Bio-Rad Laboratories, Hercules, CA) were used for quality control.

## Whole-genome genotyping

Genotyping was performed on Illumina HumanOmniExpress microarrays (Illumina, Inc., San Diego, CA) following the manufacturer’s instructions. The arrays include 730,525 SNP markers. Basic quality control of the genotyping data was performed on GenomeStudio software, version 2010 (Illumina, Inc.). All microarrays had call rates >0.99.

## Measurement of global transcript abundance

In vitro transcription was performed using Ambion Illumina TotalPrep RNA Amplification Kits (Applied Biosystems/Ambion, Austin, TX). cRNA was hybridized onto Illumina HumanHT-12v3 or HumanHT-12v4 Expression BeadChips (Illumina, Inc.), following the manufacturer’s protocol. All samples for a given individual were processed on the same slide. The arrays have 48,742 (v3) and 47,301 (v4) reporters, representing approximately 25,000 genes and non-annotated gene candidates.

## Serum samples and antibody titer measurements

Whole blood (10 ml) was collected in Vacutainer Serum Separator Tubes (Beckton–Dickinson). Serum was separated by centrifugation prior to storage at −20°C. Hemagglutination inhibition (HAI) tests were performed as previously described (Dowdle et al., 1979), except for a starting serum dilution of 1:4 and the use of turkey red blood cells. HAI test antigens were allantoic fluid harvests from infected embryonated hen’s eggs (whole-virus antigens). Neutralizing antibody tests were performed as previously described (Frank et al., 1980) except that hamster serum was not included. Test strains were the same as those used in the vaccine.

## Antibody titer data analysis

HAI and neutralizing antibody titers were measured for each viral antigen included in the vaccine. For all antigens, the change in antibody titer post-vaccination is known to be negatively correlated with the pre-vaccination titer. The responses to the individual viral antigens were correlated within individuals. For each individual, we computed a Titer Response Index (TRI), as previously described (Bucasas et al., 2011). The TRI characterizes the magnitude of an individual’s antibody rise accounting for their pre-vaccination titer and integrating the responses across the three vaccine components to provide an overall measure of vaccine responsiveness.

## Expression data processing and quality control

Raw signal intensity data from all individuals and all time points in the discovery cohort were first processed in a single batch. Background adjustment, variance stabilization transformation (Lin et al., 2008) and robust spline normalization were performed using the lumi package (Du et al., 2008) in R (R Development Core Team, 2009). Eight individuals had missing expression data from two or more time points and were excluded. We required a detection p-value of <0.01 in at least 80% of the samples for a transcript to be considered detected. We also aligned the entire set of expression reporter sequences to the human genome reference sequence (Build 36 [March 2006]/hg18) by applying the BLAT algorithm in BlatSuite34 software (Kent, 2002), and excluded any reporters that did not map or mapped to more than one region. Using these two thresholds for the data in the discovery cohort, the final data set included 9809 detected transcripts. This data set was then used for eQTL analysis in the discovery cohort.

Once data generation for the validation cohort was completed, the expression microarray signal intensity data from all individuals and all time points in that cohort were processed in a single batch. Background adjustment, variance stabilization transformation, robust spline normalization, and the application of detection thresholds were performed identically to the discovery cohort. Five individuals had missing expression data from two or more time points and were excluded. Because two different array versions were used (HT12-v3 and HT12-v4), unique reporter identifiers (ProbeID and nuID) for the 9809 reporters selected in the discovery cohort were used to subset the data from the validation cohort. This data set was then used for eQTL analysis in the validation cohort.

The analysis of correlation between gene expression and antibody titer in the discovery cohort was previously published (Bucasas et al., 2011). As part of the integrative genomic analysis described in the present study, we performed a similar analysis of this expression/titer correlation, but included expression data from both cohorts. For this purpose, the two data sets described above were combined, and an additional quantile normalization step was performed to account for batch effects between cohorts.

## Genotyping data processing and quality control

Array quality was initially assessed using GenomeStudio software (Illumina, Inc.). Default algorithms were used to normalize, generate SNP clusters, and make genotype calls. SNPs with minor allele frequency (MAF) <0.05 and Hardy-Weinberg Equilibrium (HWE) χ

![Figure 9.](https://cdn.elifesciences.org/articles/00299/elife-00299-fig9-v2.jpg)

**Figure 9.:** Pairwise identity-by-descent metrics were estimated based on genotype data from our two study samples and six HapMap populations. Multidimensional scaling analysis was performed on the resulting pairwise distances. Components 1–3 of this analysis are plotted for the male (top) and female (bottom) cohorts, and the comparison populations. As expected, the study samples cluster with the HapMap CEU population. 12 outliers were identified in each cohort and were removed prior to analysis.DOI: http://dx.doi.org/10.7554/eLife.00299.011

## Integrative genomic analysis

Analyses were carried out separately for each cohort and in the combined data set. Because we have repeated gene expression measurements on the same individuals over a series of time points, we performed a random effects linear model analysis. For each SNP-transcript pair, we fit a model with terms for day, additive effects for genotype and day–genotype interactions, and a random effect for each person:Where

![Figure 10.](https://cdn.elifesciences.org/articles/00299/elife-00299-fig10-v2.jpg)

**Figure 10.:** The figure displays hypothetical results for a single SNP-transcript pair. For any such pair, one may observe changes in transcript abundance at different time points after the experimental perturbation (lower box plots). In addition, gene expression at each time point may be different for different genotypes when there is evidence of an eQTL (upper box plots). Finally, the slope of the expression-genotype association (β), as well as the proportion of the variance in expression explained by genotype (R2g), may vary across time points.DOI: http://dx.doi.org/10.7554/eLife.00299.012

In addition to the random effects linear model, we analyzed each expression trait with respect to genotype at each time point usingwhere Yj denotes the matrix of expression traits of individuals j at a given time point (days 0, 1, 3, 14) and Gi,k is a matrix of genotypes for individuals j at SNP locus k such that each element is assigned 0, 1 or 2 according to the number of minor alleles at the kth locus of the jth individual. This allowed estimates of the proportion of expression variance explained by individual genotypes from the model’s coefficient of determination (R2g). This model permitted a more detailed examination of the changes in the strength of the genotypic association with expression at each time point. To detect SNP-transcript pairs where the magnitude of the genotype effect varied after immunization, we took the difference in R2g measures (ΔR2g) from pairwise linear models fitted after (days 1, 3 and 14) and before vaccination (day 0). We then took the top 1% ΔR2g values between day 0 and a later time point. This cis-acting eQTL subset represents the loci that show significant changes in the genetic effect as a result of the vaccine.Yj=βGi,k+e

## Correlation of transcripts with the humoral immune response

The titer response index was treated as a dependent variable and modeled as a linear combination of expression values for each transcript across the time course. A single F-statistic p-value was determined to evaluate the explanatory value of the expression data using all days. Separate evaluations were made in each cohort and in the combined data. The 301 genes displayed in Figure 4B had F-statistic p-values in the combined data <0.01 and absolute values of the maximum average correlation between expression and titer response in the two cohorts >0.15.

## Content analyses

Enriched biological and functional pathways were analyzed using DAVID Bioinformatics Resources (Dennis et al., 2003), and Ingenuity Pathway Analysis (IPA) software.

## Causal and reactive model analyses

To evaluate the relationship between the associations identified in our study, we extended a recently published analysis framework for causal modeling in eQTL data (Millstein et al., 2009). The relationship is modeled aswhere T is trait, E is gene expression, and G is genotype at a locus. In our experiment, the term E includes a separate value for each day. The term G has a separate effect on the trait under the independent null model, while under the causal alternative, where it acts through gene expression, its influence is entirely transmitted through E. The statistic used to assess the influence of G is the partial F reported by the ‘aov’ function in R (version 2.15.1). The analyses utilize an equivalence test approach, where the null hypothesis is that the second independent variable has an effect on the response conditional on the first variable, while the alternative is complete co-linearity in the associations. The null distribution of the F statistic–which under parametric assumptions would have a non-central F distribution—is derived using a permutation test procedure, as follows: The relationship between E and T is decoupled by regressing E on G, permuting the resulting residuals, then adding the permuted residuals to the predicted values to arrive at E*, which is independent of T but maintains the marginal variance and G-correlation of E. This procedure enforces the assumption of the independent model, while leaving other properties unchanged. The partial F statistic for G inrepresents a sample from the distribution under the independent null hypothesis. This process, repeated 1000 times, provided a null distribution. The p-value for the observed F is the proportion of the null distribution that is below the observed value.T∼E+GT∼E*+G

The reactive model is evaluated using the same approach, but with the expression and trait terms swapped, that isE∼T+G

This scheme tests the extent to which the trait value mediates the relationship between genotype and gene expression. In this analysis, the permutation step decouples the expression-to-trait relationship from the eQTL association and asks if the eQTL association disappears after accounting for the expression-to-trait association.

Power analyses for these models apply the same scheme to simulated data. The term G is simulated as binomial, while E and T are normal, with parameters chosen to match the minor allele frequency, variance, and correlations observed in our data set. The power to reject the false (independent) model is shown using a threshold of p<0.05. The power properties for the tests used to evaluate both the reactive and causal models are equivalent because the model structures and r2 relationships are symmetric between the two alternatives.
