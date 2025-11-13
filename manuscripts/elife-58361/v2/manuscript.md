# A Mendelian randomization study of the role of lipoprotein subfractions in coronary artery disease

## Authors

- Qingyuan Zhao<sup>1</sup> ([ORCID: 0000-0001-9902-2768](https://orcid.org/0000-0001-9902-2768)) †
- Jingshu Wang<sup>2</sup>
- Zhen Miao<sup>3</sup> ([ORCID: 0000-0002-3255-9517](https://orcid.org/0000-0002-3255-9517))
- Nancy R Zhang<sup>4</sup>
- Sean Hennessy<sup>3</sup>
- Dylan S Small<sup>4</sup> ([ORCID: 0000-0003-4928-2646](https://orcid.org/0000-0003-4928-2646))
- Daniel J Rader<sup>3</sup>

### Affiliations

1. Statistical Laboratory, University of Cambridge Cambridge United Kingdom
2. Department of Statistics, University of Chicago Chicago United States
3. Perelman School of Medicine, University of Pennsylvania Philadelphia United States
4. Department of Statistics, University of Pennsylvania Philadelphia United States
5. Department of Medicine, University of Pennsylvania Philadelphia United States

† Corresponding author

## Abstract

Recent genetic data can offer important insights into the roles of lipoprotein subfractions and particle sizes in preventing coronary artery disease (CAD), as previous observational studies have often reported conflicting results. We used the LD score regression to estimate the genetic correlation of 77 subfraction traits with traditional lipid profile and identified 27 traits that may represent distinct genetic mechanisms. We then used Mendelian randomization (MR) to estimate the causal effect of these traits on the risk of CAD. In univariable MR, the concentration and content of medium high-density lipoprotein (HDL) particles showed a protective effect against CAD. The effect was not attenuated in multivariable analyses. Multivariable MR analyses also found that small HDL particles and smaller mean HDL particle diameter may have a protective effect. We identified four genetic markers for HDL particle size and CAD. Further investigations are needed to fully understand the role of HDL particle size.

## Introduction

Lipoprotein subfractions have been increasingly studied in epidemiological research and used in clinical practice to predict the risk of cardiovascular diseases (CVD) (Rankin et al., 2014; Mora et al., 2009; China Kadoorie Biobank Collaborative Group et al., 2018). Several studies have identified potentially novel subfraction predictors for CVD (Mora et al., 2009; Hoogeveen et al., 2014; Williams et al., 2014; Ditah et al., 2016; Lawler et al., 2017; Fischer et al., 2014) and demonstrated that the addition of subfraction measurements can significantly improve the risk prediction for CVD (Würtz et al., 2012; van Schalkwijk et al., 2014; McGarrah et al., 2016; Rankin et al., 2014). However, these observational studies often provide conflicting evidence on the precise roles of the lipoprotein subfractions. For example, while some studies suggested that small, dense low-density lipoprotein (LDL) particles may be more atherogenic (Lamarche et al., 1997; Hoogeveen et al., 2014), others found that larger LDL size is associated with higher CVD risk (Campos et al., 2001; Mora, 2009). Some recent observational studies found that the inverse association of CVD outcomes with smaller high-density lipoprotein (HDL) particles is stronger than the association with larger HDL particles (Ditah et al., 2016; Kim et al., 2016; McGarrah et al., 2016; Silbernagel et al., 2017), but other studies reached the opposite conclusion in different cohorts (Li et al., 2016; Arsenault et al., 2009). Currently, the utility of lipoprotein subfractions or particle sizes in routine clinical practice remains controversial (Superko, 2009; Mora, 2009; Davidson et al., 2011; Bays et al., 2016), as there is still a great uncertainty about their causal roles in CVD, largely due to a lack of intervention data (Bays et al., 2016).

Mendelian randomization (MR) is an useful causal inference method that avoids many common pitfalls of observational cohort studies (Smith and Ebrahim, 2003). By using genetic variation as instrumental variables, MR asks if the genetic predisposition to a higher level of the exposure (in this case, lipoprotein subfractions) is associated with higher occurrences of the disease outcome (Didelez and Sheehan, 2007). A positive association suggests a causally protective effect of the exposure if the genetic variants satisfy the instrumental variable assumptions (Didelez and Sheehan, 2007; Davey Smith and Hemani, 2014). Since MR can provide unbiased causal estimate even when there are unmeasured confounders, it is generally considered more credible than other non-randomized designs and is quickly gaining popularity in epidemiological research (Gidding et al., 2012; Davies et al., 2018). MR has been used to estimate the effect of several metabolites on CVD, but most prior studies are limited to just one or a few risk exposures at a time (Emdin et al., 2016; Ference et al., 2017).

In this study, we will use recent genetic data to investigate the roles of lipid and lipoprotein traits in the occurrence of coronary artery disease (CAD) and myocardial infarction (MI). In particular, we are interested in discovering lipoprotein subfractions that may be causal risk factors for CAD and MI in addition to the traditional lipid profile (LDL cholesterol, HDL cholesterol, and triglycerides levels). To this end, we will first estimate the genetic correlation of the lipoprotein subfractions and particle sizes with the tradition risk factors and remove the traits that have a high genetic correlation. We will then use MR to estimate the causal effects of the selected lipoprotein subfractions and particle sizes on CAD and MI. Finally, we will explore potential genetic markers for the identified lipoprotein and subfraction traits.

## Materials and methods

### GWAS summary datasets and lipoprotein particle measurements

Table 1 describes all GWAS summary datasets used in this study, including two GWAS of the traditional lipid risk factors (Willer et al., 2013; Hoffmann et al., 2018), two recent GWAS of the human lipidome (Kettunen et al., 2016; Davis et al., 2017), and three GWAS of CAD or MI (Nikpay et al., 2015; Nelson et al., 2017; Abbott et al., 2018). In the two GWAS of the lipidome (Kettunen et al., 2016; Davis et al., 2017), high-throughput nuclear magnetic resonance (NMR) spectroscopy was used to measure the circulating lipid and lipoprotein traits (Soininen et al., 2009). We investigated the 82 lipid and lipoprotein traits measured in these studies that are related to very-low-density lipoprotein (VLDL), LDL, intermediate-density lipoprotein (IDL), and HDL subfractions and particle sizes. All the subfraction traits are named with three components that are separated by hyphens: the first component indicates the size (XS, S, M, L, XL, XXL); the second component indicates the fraction according to the lipoprotein density (VLDL, LDL, IDL, HDL); the third component indicates the measurement (C for total cholesterol, CE for cholesterol esters, FC for free cholesterol, L for total lipids, P for particle concentration, PL for phospholipids, TG for triglycerides). For example, M-HDL-P refers to the concentration of medium HDL particles.

**Table 1.**
 Information about the GWAS summary datasets used in this article.The columns are the phenotypes reported by the GWAS studies, the consortium or name of the first author of the publication, PubMed ID, population, sample size, other GWAS datasets with other lapping sample, and URLs we used to download the datasets.


<table>
  <thead>
    <tr>
      <th>Phenotype</th>
      <th>Dataset name</th>
      <th>PubMed ID</th>
      <th>Population</th>
      <th>Sample size</th>
      <th>Sample overlap with other datasets</th>
      <th>URL to summary dataset</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Traditional lipid traits</td>
      <td>GERA</td>
      <td>29507422 Hoffmann et al., 2018</td>
      <td>Multi-ethnic</td>
      <td>94,674</td>
      <td></td>
      <td>ftp://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/</td>
    </tr>
    <tr>
      <td></td>
      <td>GLGC</td>
      <td>24097068 Willer et al., 2013</td>
      <td>European</td>
      <td>188,578</td>
      <td>Kettunen, CARDIoGRAMplusC4D</td>
      <td>http://csg.sph.umich.edu/abecasis/public/lipids2013/</td>
    </tr>
    <tr>
      <td>Lipoprotein subfraction traits</td>
      <td>Davis</td>
      <td>29084231 Davis et al., 2017</td>
      <td>Finnish</td>
      <td>8372</td>
      <td></td>
      <td>http://csg.sph.umich.edu/boehnke/public/metsim-2017-lipoproteins/</td>
    </tr>
    <tr>
      <td></td>
      <td>Kettunen</td>
      <td>27005778 Kettunen et al., 2016</td>
      <td>European</td>
      <td>24,925</td>
      <td>GLGC, CARDIoGRAMplusC4D</td>
      <td>http://www.computationalmedicine.fi/data#NMR_GWAS</td>
    </tr>
    <tr>
      <td>Heart disease traits</td>
      <td>CARDIoGRAMplusC4D (CAD)</td>
      <td>26343387 Nikpay et al., 2015</td>
      <td>Mostly European</td>
      <td>185,000</td>
      <td>GLGC, Kettunen</td>
      <td>http://www.cardiogramplusc4d.org/data-downloads/</td>
    </tr>
    <tr>
      <td></td>
      <td>CARDIoGRAMplusC4D + UK Biobank (CAD)</td>
      <td>28714975 Nelson et al., 2017</td>
      <td>Mostly European</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>UK Biobank (MI)</td>
      <td>Interim round two release Abbott et al., 2018</td>
      <td>European</td>
      <td>360,420</td>
      <td></td>
      <td>http://www.nealelab.is/uk-biobank/</td>
    </tr>
  </tbody>
</table>

Aside from the concentration and content of lipoprotein subfractions, the two lipidome GWAS also measured the traditional lipid traits (TG, LDL-C, HDL-C), the average diameter of the fractions (VLDL-D, LDL-D, HDL-D) and the concentration of apolipoprotein A1 (ApoA1) and apolipoprotein B (ApoB). A full list of the lipoprotein measurements investigated in this article can be found in Appendix 1.

### Genetic correlation and phenotypic screening

Genetic correlation is a measure of association between the genetic determinants of two phenotypes. It is conceptually different from epidemiological correlation that can be directly estimated from cross-sectional data. In this study, we applied the LD-score regression (Bulik-Sullivan et al., 2015) to the lipidome GWAS (Kettunen et al., 2016; Davis et al., 2017) to estimate the genetic correlations between the lipoprotein subfractions, particle sizes, and traditional risk factors. We then removed lipoprotein subfractions and particle sizes that are strongly correlated with the traditional risk factors, defined as an estimated genetic correlation > 0.8 with TG, LDL-C, HDL-C, ApoB, or ApoA1 in the GWAS published by Davis et al., 2017. Because these traits are largely co-determined with the traditional risk factors, they do not represent independent biological mechanisms and may lead to multicollinearity issues in multivariate MR analyses. Finally, we obtained an independent estimate of the genetic correlations between the selected traits by applying the LD score regression to the GWAS published by Kettunen et al., 2016. We used Bonferroni's procedure to correct for multiple testing (familywise error rate at 0.05).

### Three-sample Mendelian randomization design

For MR, we employed a three-sample design (Zhao et al., 2019b) in which one GWAS was used to select independent genetic instruments that are associated with one or several lipoprotein measures. The other two GWAS were then used to obtain summary associations of the selected SNPs with the exposure and the outcome, as in a typical two-sample MR design (Pierce and Burgess, 2013; Hemani et al., 2016). More specifically, the selection GWAS was used to create a set of SNPs that are in linkage equilibrium with each other in a reference panel (distance >10 megabase pairs, $r^{2}<0.001$). This was done by ordering the SNPs by the p-values of their association with the trait(s) under investigation and then selecting them greedily using the linkage-disequilibrium (LD) clumping function in the PLINK software package (Purcell et al., 2007). To avoid winner's curse, we require the other two GWAS to have no overlapping sample with the selection GWAS.

As the GWAS published by Davis et al., 2017 has a smaller sample size, we used it to select the genetic instruments so the larger dataset can be used for statistical estimation. In univariable MR, associations of the selected SNPs with the exposure trait (a lipoprotein subfraction or a particle size trait) were obtained from the GWAS published by Kettunen et al., 2016 and the associations with MI were obtained using summary data from an interim release of UK BioBank (Abbott et al., 2018). To maximize the statistical power, we used the so-called ‘genome-wide MR’ design. Independent SNPs are selected by using LD clumping, but we do not truncate the list of SNPs by their p-values. More details about this design can be found in a previous methodological article (Zhao et al., 2019b).

To control for potential pleiotropic effects via the traditional risk factors, we performed two multivariable MR analyses for each lipoprotein subfraction or particle size under investigation. The first multivariable MR analysis considers four exposures: TG, LDL-C, HDL-C, and the lipoprotein measurement under investigation. The second multivariable MR analysis replaces LDL-C and HDL-C with ApoB and ApoA1, in accordance with some recent studies (Richardson et al., 2020). SNPs were ranked by their minimum p-values with the four exposures and are selected as instruments only if they were associated with at least one of the four exposures (p-value $\leq10^{-4}$). Both multivariable MR analyses used the Davis (Davis et al., 2017) and GERA (Hoffmann et al., 2018) datasets for instrument selection, the Kettunen (Kettunen et al., 2016) and GLGC (Willer et al., 2013) datasets for the associations of the instruments with the exposures, and the CARDIoGRAMplusC4D + UK Biobank (Nelson et al., 2017) dataset for the associations with CAD.

### Statistical estimation

For univariable MR, we used the robust adjusted profile score (RAPS) because it is more efficient and robust than many conventional methods (Zhao et al., 2020; Zhao et al., 2019b). RAPS can consistently estimate the causal effect even when some of the genetic variants violate instrumental variables assumptions. For multivariable MR, we used an extension to RAPS called GRAPPLE to obtain the causal effect estimates of multiple exposures (Wang et al., 2020). GRAPPLE also allows the exposure GWAS to have overlapping sample with the outcome GWAS, while the original RAPS does not. We assessed the strength of the instruments using the modified Cochran's Q statistic (Sanderson et al., 2019). Because many lipoprotein subfraction traits were analyzed simultaneously, we used the Benjamini-Hochberg procedure to correct for multiple testing (Benjamini and Hochberg, 1995) and the false discovery rate was set to be 0.05. More detail about the statistical methods can be found in Appendix 3.

**Table 2.**
 Results of some multivariable Mendelian randomization analyses.Each row in the table corresponds to a multivariable MR analysis with traditional lipid profile and the specified lipoprotein subfraction or particle size trait. Reported numbers are the point estimates and 95% confidence intervals of the exposure effect.


<table>
  <thead>
    <tr>
      <th>Trait</th>
      <th>Effect of TG</th>
      <th>Effect of LDL-C</th>
      <th>Effect of HDL-C</th>
      <th>Effect of subfraction/particle size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>None</td>
      <td>0.19 [0.09,0.29]</td>
      <td>0.38 [0.33,0.44]</td>
      <td>−0.053 [-0.13,0.03]</td>
      <td></td>
    </tr>
    <tr>
      <td>M-HDL-P</td>
      <td>0.37 [0.22,0.52]</td>
      <td>0.39 [0.32,0.45]</td>
      <td>0.30 [0.08,0.52]</td>
      <td>−0.69 [-1.09,–0.3]</td>
    </tr>
    <tr>
      <td>S-HDL-P</td>
      <td>0.23 [0.12,0.33]</td>
      <td>0.45 [0.38,0.52]</td>
      <td>−0.11 [-0.2,–0.02]</td>
      <td>−0.33 [-0.52,–0.15]</td>
    </tr>
    <tr>
      <td>HDL-D</td>
      <td>0.11 [0.00,0.22]</td>
      <td>0.42 [0.36,0.49]</td>
      <td>−0.44 [-0.69,–0.2]</td>
      <td>0.33 [0.11,0.56]</td>
    </tr>
    <tr>
      <td></td>
      <td>Effect of TG</td>
      <td>Effect of ApoB</td>
      <td>Effect of ApoA1</td>
      <td>Effect of Subfraction/Particle size</td>
    </tr>
    <tr>
      <td>None</td>
      <td>0.05 [-0.05,0.14]</td>
      <td>0.49 [0.38,0.60]</td>
      <td>−0.095 [-0.21,0.02]</td>
      <td></td>
    </tr>
    <tr>
      <td>M-HDL-P</td>
      <td>−0.00 [-0.18,0.17]</td>
      <td>0.50 [0.31,0.69]</td>
      <td>0.13 [-0.06,0.32]</td>
      <td>−0.47 [-0.80,–0.15]</td>
    </tr>
    <tr>
      <td>S-HDL-P</td>
      <td>0.07 [-0.03,0.17]</td>
      <td>0.53 [0.41,0.65]</td>
      <td>−0.13 [-0.25,–0.02]</td>
      <td>−0.24 [-0.40,–0.08]</td>
    </tr>
    <tr>
      <td>HDL-D</td>
      <td>0.06 [-0.04,0.15]</td>
      <td>0.61 [0.47,0.76]</td>
      <td>−0.46 [-0.73,–0.19]</td>
      <td>0.30 [0.08,0.52]</td>
    </tr>
  </tbody>
</table>

### Genetic markers for lipoprotein subfractions and CAD

To obtain genetic markers, we selected SNPs that are associated with the lipoprotein measurements identified in the MR (p-value $\leq5\times10^{-8}$) and CAD (p-value $\leq0.05$) but are not associated with LDL-C or ApoB (p-value $\geq10^{-3}$). To maximize the power of this exploratory analysis, we meta-analyzed the results of the two lipidome GWAS (Kettunen et al., 2016; Davis et al., 2017) by inverse-variance weighting. For the associations with LDL-C and CAD, we used the GWAS summary data reported by the GLGC (Willer et al., 2013) and CARDIoGRAMplusC4D (Nelson et al., 2017) consortia. We used LD clumping to obtain independent markers (Purcell et al., 2007) and then validate the markers using tissue-specific gene expression data from the GTEx project.

### Sensitivity analysis and replicability

Because we had multiple GWAS summary datasets for the lipoprotein subfractions and CAD/MI (Table 1), we swapped the roles of the GWAS datasets in the three-sample MR design whenever permitted by the statistical methods to obtain multiple statistical estimates. These estimates are not completely independent of the primary results, but they can nonetheless be used to assess replicability. As a sensitivity analysis, We further analyzed univariable MR using inverse-variance weighting (IVW) (Burgess et al., 2013) and weighted median (Bowden et al., 2016) and compared with the primary results obtained by RAPS. We also assessed the assumptions made by RAPS using some diagnostic plots suggested in previous methodological articles (Zhao et al., 2019b).

## Results

### Genetic correlations and phenotypic screening

We obtained the genetic correlations of the lipoprotein subfractions and particle sizes with the traditional lipid risk factors: TG, LDL-C, HDL-C, ApoB, and ApoA1 (Table 1). We found that almost all VLDL subfractions traits (besides those related to very small VLDL subfraction) and the mean VLDL particle diameter have an estimated genetic correlation with TG very close to 1. Most traits related to the large and very large HDL subfractions also have a high genetic correlation with HDL-C and ApoA1.

After removing traits that are strongly correlated with the traditional risk factors, we obtained 27 traits that may involve independent genetic mechanisms. Figure 1 shows the genetic correlation matrix for these traits and the traditional lipid factors. The selected traits can be divided into two groups based on whether they are related to VLDL/LDL/IDL particles or HDL particles. Within each group, most traits were strongly correlated with the others. In the first group, most traits had a positive genetic correlation with LDL-C and ApoB, while in the second group, most traits had a positive genetic correlation with HDL-C and ApoA1. Exceptions include LDL-D, which had a negative but statistically non-significant genetic correlation with LDL-C and ApoB, and S-HDL-P and S-HDL-L, which showed no or weak genetic correlation with HDL-C and ApoA1.

![Figure 1.](https://cdn.elifesciences.org/articles/58361/elife-58361-fig1-v2.jpg)

**Figure 1.:** White asterisk indicates the correlation is statistically significant after Bonferroni correction for multiple comparisons at level 0.05.

### Mendelian randomization

Figure 2 shows the estimated causal effect of the selected lipoprotein measurements on MI or CAD that are statistically significant (false discovery rate = 0.05). The unfiltered results can be found in Appendix 3, which also contains results of the sensitivity and replicability analyses.

![Figure 2.](https://cdn.elifesciences.org/articles/58361/elife-58361-fig2-v2.jpg)

The concentration and lipid content of VLDL, LDL, and IDL subfractions showed harmful and nearly uniform effects on MI in univariable MR. However, after adjusting for the traditional lipid risk factors, the effects of these ApoB-related subfractions become close to zero (besides IDL-FC in one multivariable analysis). The mean diameter of LDL particles (LDL-D) showed a harmful effect on MI in univariable MR, though the effect was smaller than those of the LDL subfractions in univariable MR. The estimated effect of LDL-D was attenuated in the multivariable MR analyses.

The concentration and content of medium HDL particles showed protective effects in univariable and multivariable MR analyses. In particular, adjusting for the traditional lipid risk factors did not attenuate the effect of traits related to medium HDL. The concentration of and total lipid in small HDL particles showed protective effects in multivariable MR analyses, though the effect sizes were smaller than those of the medium HDL traits. The mean diameter of HDL particles (HDL-D) had almost no effect on MI in the univariable MR analysis, but after adjusting for the traditional lipid risk factors, it showed a harmful effect.

Table 2 reports the estimated effects of M-HDL-P, S-HDL-P, HDL-D, and traditional lipid traits (TG, LDL-C, HDL-C, ApoB, ApoA1) in the multivariable MR analyses. To better understand the role of HDL subfractions and particle sizes, we also included in the table the results of the multivariate MR analyses for the traditional lipid risk factors only. Those baseline analyses suggested that HDL-C/ApoA1 had a weak, non-significant protective effect on CAD, which is consistent with prior studies (Holmes et al., 2015; Wang et al., 2020). Adding S-HDL-P to the MR analysis did not substantially alter the estimated effects of the traditional lipid traits. However, when M-HDL-P or HDL-D was included in the model, the estimated effects of M-HDL-P and HDL-D changed substantially. In particular, when M-HDL-P was included in the multivariable MR analyses, HDL-C/ApoA1 showed a harmful effect on CAD. When HDL-D was included, HDL-C/ApoA1 showed a protective effect.

### Genetic markers associated with HDL subfractions and CAD

We identified four genetic variants that are associated with S-HDL-P, M-HDL-P, or HDL-D, not associated with LDL-C or ApoB, and associated with CAD: rs838880 (SCARB1), rs737337 (DOCK6), rs2943641 (IRS1), and rs6065904 (PLTP) (Figure 3). These SNP-cis gene pairs are also supported by examining expression quantitative trait loci (eQTL) in the tissue-specific GTEx data (Appendix 4). The first three variants were not associated with S-HDL-P. However, they had uniformly positive associations with M-HDL-P, L-HDL-P, XL-HDL-P, HDL-D, ApoA1, and HDL-C, and a negative association with CAD. The last variant rs6065904 had positive associations with S-HDL-P and M-HDL-P, negative associations with L-HDL-P, XL-HDL-P, HDL-D, negative but smaller associations with ApoA1 and HDL-C, and a negative association with CAD.

![Figure 3.](https://cdn.elifesciences.org/articles/58361/elife-58361-fig3-v2.jpg)

### Sensitivity and replicability analysis

We also investigated the effects of lipoprotein subfractions and particle sizes on MI/CAD using multiple GWAS datasets, MR designs and statistical methods. The results are provided in Appendix 3 and are generally in agreement with the primary results reported above. The diagnostic plots for S-HDL-P and M-HDL-P did not suggest evidence of violations of the instrument strength independent of direct effect (InSIDE) assumption (Bowden et al., 2015) made by RAPS and GRAPPLE (Appendix 4).

## Discussion

By using recent genetic data and MR, this study examines whether some lipoprotein subfractions and particle sizes, beyond the traditional lipid risk factors, may play a role in coronary artery disease. We find that VLDL subfractions have extremely high genetic correlations with blood triglyceride level and thus offer little extra value. We find some weak evidence that larger LDL particle size may have a small harmful effect on myocardial infarction and coronary artery disease.

Our main finding is that the size of HDL particles may play an important and previously undiscovered role. Although the concentration and lipid content of small and medium HDL particles appear to be positively correlated with HDL cholesterol and ApoA1, their genetic correlations are much smaller than 1, indicating possible independent biological pathway(s). Moreover, the MR analyses suggested that the small and medium HDL particles may have protective effects on CAD. We also find that larger HDL mean particle diameter may have a harmful effect on CAD. Finally, we identified four potential genetic markers for HDL particle size that are independent of LDL cholesterol and ApoB.

There has been a heated debate on the role of HDL particles in CAD in recent years following the failure of several trials for CETP inhibitors (Barter et al., 2007; Schwartz et al., 2012; Lincoff et al., 2017) and recombinant ApoA1 (Nicholls et al., 2018) targeting HDL cholesterol. Observational epidemiology studies have long demonstrated strong inverse association between HDL cholesterol and the risk of CAD or MI (Miller and Miller, 1975; Lewington et al., 2007; Di Angelantonio et al., 2009), but conflicting evidence has been found in MR studies. In an influential study, Voight and collaborators found that the genetic variants associated with HDL cholesterol had varied associations with CAD and that almost all variants suggesting a protective effect of HDL cholesterol were also associated with LDL cholesterol or triglycerides (Voight et al., 2012). Other MR studies also found that the effect of HDL cholesterol on CAD is heterogeneous (Zhao et al., 2019b) or attenuated after adjusting for LDL cholesterol and triglycerides (Holmes et al., 2017; White et al., 2016).

Notice that the harmful effect of larger HDL particle diameter found in this study relies on including HDL-C or ApoA1 in the multivariable MR analysis. Thus, the role of HDL particles in preventing CAD may be more complicated than, for example, that of LDL cholesterol or ApoB. It is possible that HDL cholesterol, HDL subfractions, and HDL particle size are all phenotypic markers for some underlying causal mechanism. A related theory is the HDL function hypothesis (Rader and Hovingh, 2014). Cholesterol efflux capacity, a measure of HDL function, has been documented as superior to HDL-C in predicting CVD risk (Rohatgi et al., 2014; Saleheen et al., 2015). Recent epidemiologic studies found that HDL particle size is positively associated with cholesterol efflux capacity in post-menopausal women (El Khoudary et al., 2016) and in an asymptomatic older cohort (Mutharasan et al., 2017). However, mechanistic efflux studies showed that small HDL particles actually mediate more cholesterol efflux (Favari et al., 2009; Du et al., 2015). A likely explanation of this seeming contradiction is that a high concentration of small HDL particles in the serum may mark a block in maturation of small HDL particles (Mutharasan et al., 2017). This can also partly explain our finding that small HDL traits have a smaller effect than medium HDL traits, as increased medium HDL might indicate successful maturation of small HDL particles.

Among the reported genetic markers, SCARB1 and PLTP have established relations to HDL metabolism and CAD. SCARB1 encodes a plasma membrane receptor for HDL and is involved in hepatic uptake of cholesterol from peripheral tissues. Recently, a rare mutation (P376L) of SCARB1 was reported to raise HDL-C level and increase CAD risk (Zanoni et al., 2016; Samadi et al., 2019). This is opposite direction to the conventional belief that HDL-C is protective and could be explained by HDL dysfunction. PLTP encodes the phospholipid transfer protein and mediates the transfer of phospholipid and cholesterol from LDL and VLDL to HDL. As a result, PLTP plays a complex but pivotal role in HDL particle size and composition. Several studies have suggested that high PLTP activity is a risk factor for CAD (Schlitt et al., 2003; Schlitt et al., 2009; Zhao et al., 2019a).

Our study should be viewed in the context of its limitations, in particular, the inherent limitations of the summary-data MR design. Any causal inference from non-experimental data makes unverifiable assumptions, so does our study. Conventional MR studies assume that the genetic variants are valid instrumental variables. The statistical methods used by us make less stringent assumptions about the instrumental variables, but those assumptions could still be violated even though our model diagnosis does not suggest evidence against the InSIDE assumption. Our study did not adjust for other risk factors for CAD such as body mass index, blood pressure, and smoking. All the GWAS datasets used in this study are from the European population, so the same conclusions might not generalize to other populations. Furthermore, our study used GWAS datasets from heterogeneous subpopulations, which may also introduce bias (Zhao et al., 2019c). We also did not use more than one subfraction traits as exposures in multivariable MR because of their high genetic correlations. Alternative statistical methods could be used to select the best causal risk factor from high-throughput experiments (Zuber et al., 2019). Finally, as pointed out by revieweres, triglycerides has a greater intra-individual biological variability than HDL particle size. It is likely that triglycerides and HDL size represent a gene/environment interaction with a very large environmental component. Further investigations are needed to fully understand this mechanism.

Recently, a NMR spectroscopy method has been developed to estimate HDL cholesterol efflux capacity from serum (Kuusisto et al., 2019). That method can form the basis of a genetic analysis of HDL cholesterol efflux capacity and may complement the results here. We believe more laboratorial and epidemiological research is needed to clarify the roles of HDL subfractions and particle size in cardiovascular diseases.
