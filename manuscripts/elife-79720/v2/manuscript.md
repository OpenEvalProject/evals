# Genetically predicted high IGF-1 levels showed protective effects on COVID-19 susceptibility and hospitalization: a Mendelian randomisation study with data from 60 studies across 25 countries

## Authors

- Xinxuan Li<sup>1</sup> ([ORCID: 0000-0001-8922-661X](https://orcid.org/0000-0001-8922-661X))
- Yajing Zhou<sup>1</sup>
- Shuai Yuan<sup>1</sup>
- Xuan Zhou<sup>1</sup>
- Lijuan Wang<sup>1</sup>
- Jing Sun<sup>1</sup>
- Lili Yu<sup>1</sup>
- Jinghan Zhu<sup>3</sup>
- Han Zhang<sup>1</sup>
- Nan Yang<sup>1</sup>
- Shuhui Dai<sup>1</sup>
- Peige Song<sup>4</sup>
- Susanna C Larsson<sup>2</sup>
- Evropi Theodoratou<sup>6</sup>
- Yimin Zhu<sup>1</sup>
- Xue Li<sup>1</sup> ([ORCID: 0000-0001-6880-2577](https://orcid.org/0000-0001-6880-2577)) †

### Affiliations

1. Department of Big Data in Health Science School of Public Health, Center of Clinical Big Data and Analytics of The Second Affiliated Hospital, Zhejiang University School of Medicine Hangzhou China ([ROR:059cjpv64](https://ror.org/059cjpv64))
2. Unit of Cardiovascular and Nutritional Epidemiology, Institute of Environmental Medicine, Karolinska Institutet Stockholm Sweden ([ROR:056d84691](https://ror.org/056d84691))
3. The Second School of Clinical Medicine, Southern Medical University Guangzhou China ([ROR:01vjw4z39](https://ror.org/01vjw4z39))
4. School of Public Health and Women's Hospital, Zhejiang University School of Medicine Hangzhou China ([ROR:042t7yh44](https://ror.org/042t7yh44))
5. Unit of Medical Epidemiology, Department of Surgical Sciences, Uppsala University Uppsala Sweden ([ROR:048a87296](https://ror.org/048a87296))
6. Centre for Global Health, Usher Institute, University of Edinburgh Edinburgh United Kingdom ([ROR:01nrxwf90](https://ror.org/01nrxwf90))
7. Cancer Research UK Edinburgh Centre, Medical Research Council Institute of Genetics and Cancer, University of Edinburgh Edinburgh United Kingdom ([ROR:01nrxwf90](https://ror.org/01nrxwf90))

† Corresponding author

## Abstract

Background:Epidemiological studies observed gender differences in COVID-19 outcomes, however, whether sex hormone plays a causal in COVID-19 risk remains unclear. This study aimed to examine associations of sex hormone, sex hormones-binding globulin (SHBG), insulin-like growth factor-1 (IGF-1), and COVID-19 risk.Methods:Two-sample Mendelian randomization (TSMR) study was performed to explore the causal associations between testosterone, estrogen, SHBG, IGF-1, and the risk of COVID-19 (susceptibility, hospitalization, and severity) using genome-wide association study (GWAS) summary level data from the COVID-19 Host Genetics Initiative (N=1,348,701). Random-effects inverse variance weighted (IVW) MR approach was used as the primary MR method and the weighted median, MR-Egger, and MR Pleiotropy RESidual Sum and Outlier (MR-PRESSO) test were conducted as sensitivity analyses.Results:Higher genetically predicted IGF-1 levels have nominally significant association with reduced risk of COVID-19 susceptibility and hospitalization. For one standard deviation increase in genetically predicted IGF-1 levels, the odds ratio was 0.77 (95% confidence interval [CI], 0.61–0.97, p=0.027) for COVID-19 susceptibility, 0.62 (95% CI: 0.25–0.51, p=0.018) for COVID-19 hospitalization, and 0.85 (95% CI: 0.52–1.38, p=0.513) for COVID-19 severity. There was no evidence that testosterone, estrogen, and SHBG are associated with the risk of COVID-19 susceptibility, hospitalization, and severity in either overall or sex-stratified TSMR analysis.Conclusions:Our study indicated that genetically predicted high IGF-1 levels were associated with decrease the risk of COVID-19 susceptibility and hospitalization, but these associations did not survive the Bonferroni correction of multiple testing. Further studies are needed to validate the findings and explore whether IGF-1 could be a potential intervention target to reduce COVID-19 risk.Funding:We acknowledge support from NSFC (LR22H260001), CRUK (C31250/A22804), SHLF (Hjärt-Lungfonden, 20210351), VR (Vetenskapsrådet, 2019-00977), and SCI (Cancerfonden).

## Introduction

The COVID-19 pandemic has emerged as the most important health concern across the globe since December 2019. A notable finding that has been noted in many affected countries is a male predominance of COVID-19-related hospitalization and death (Grasselli et al., 2020; Peckham et al., 2020). Globally, more than 60% of deaths from COVID-19 are reported in males (Richardson et al., 2020). This epidemiological pattern indicates the need for urgent public health actions, as well as for further investigations on the contributing factors of sex differences in COVID-19 risk and its underlying biological mechanisms.

Sex hormones play important roles in the immune response in which estrogen was thought to be immune boosting and testosterone to be immunosuppressing (Strope et al., 2020). Due to the higher levels of testosterone in male than female, it has been hypothesized that testosterone might be a promoter of SARS‐CoV‐2 infection and progression in males, considering the regulatory effect of androgen receptor (AR) and testosterone on the transcription of a transmembrane protease serine 2, which is a critical factor enabling cellular infection by coronaviruses, including SARS‐CoV‐2 (Peckham et al., 2020; Pozzilli and Lenzi, 2020; Cattrini et al., 2020). Estrogen has been shown not only to enhance immunological markers and response, but also to be linked to T-cell proliferation, which might be involved in the immune response to the infection of SARS-CoV-2 (Taneja, 2018). Most hormone (about 60%) is tightly bound to sex hormone-binding globulin (SHBG), which is an important regulator of the bioactivities of estrogens and testosterone (Raverot et al., 2010; Dimou et al., 2021). In addition, sex hormone signaling could also regulate the insulin-like growth factor (IGF-1) concentrations, which were also reported to be associated with acute respiratory distress syndrome (Ahasic et al., 2012). It is therefore hypothesized that sex hormone and its related biomarkers might contribute to the sex difference of COVID-19 outcomes. A number of observational studies examined the associations between sex hormones and COVID-19 risk, however, the causality of these associations remains unestablished due to potential limitations of observational studies (e.g., residual confounding and reverse causality) and lack of high-quality data from randomized trials (Tsang et al., 2016).

Mendelian randomization (MR) analysis is an epidemiological approach that can strengthen the casual inference by utilizing genetic variants as instrumental variables to mimic biological effects of related biomarkers (Burgess and Thompson, 2015). Here, we conducted a two-sample MR (TSMR) study to explore the causal associations testosterone, estrogen, SHBG, and IGF-1 with the risk of COVID-19 (susceptibility, hospitalization, and severity) using genome-wide association study (GWAS) summary level data from the COVID-19 Host Genetics Initiative (COVID-19 HGI). Sex-stratified MR analyses for testosterone and estradiol were further performed to explore the associations in males and females separately.

## Materials and methods

### Study design

We firstly conducted a TSMR analysis to explore the causal links between testosterone, estrogen, SHBG, IGF-1, and the risk of COVID-19 (susceptibility, hospitalization, and severity), based on GWAS summary level data from COVID-19 HGI. We then performed sex-stratified MR analysis to further examine the associations between genetically determined circulating levels of testosterone and estrogen and COVID-19 outcomes in males and females separately. The design of this study is explained in Figure 1.

![Figure 1.](https://cdn.elifesciences.org/articles/79720/elife-79720-fig1-v2.jpg)

**Figure 1.:** Abbreviation: IGF-1, insulin-like growth factor-1; GWAS, genome-wide association study; SNP, single-nucleotide polymorphism; LD, linkage disequilibrium; IVW, inverse variance weighting; MR, Mendelian randomization.

### Genetic instruments of testosterone, estradiol, SHBG, and IGF-1

Single-nucleotide polymorphisms (SNPs) associated with testosterone, estradiol, SHBG, and IGF-1 levels were identified from genome-wide association analyses in up to 425,097 participants of European ancestry (Ruth et al., 2020; Sinnott-Armstrong et al., 2021). Sex-stratified SNPs related to estradiol were obtained from a GWAS including 147,690 males and 163,985 females in UK Biobank (Schmitz et al., 2021). We restricted the analysis to SNPs in linkage equilibrium which were identified in the relevant GWAS at p<5 × 10−8 clumped on r2=0.01 within 10,000 kb using the 1000 genomes reference panel (Hemani et al., 2018) to ensure sufficient statistical effectiveness. Among those pairs of SNPs that had LD r2 above the specified threshold (r2 = 0.01), only the SNP with the lower p value would be retained. SNPs absent from the LD reference panel were also removed. To test whether there was a weak instrumental variable bias, namely genetic variants selected as instrumental variables had a weak association with exposure, we calculated the F statistic if it is much greater than 10 for the instrument-exposure association, the possibility of weak instrumental variable bias is small. These analyses were conducted using the R package ‘TwoSampleMR’ (Yavorska and Burgess, 2017). Consequently, a total of 320, 316, 7, and 18 SNPs were used as instrumental variables for SHBG, testosterone, estradiol, and IGF-1, respectively. Given that genetic variants predicting testosterone and estradiol levels differ for men and women, we selected sex-specific SNPs for testosterone (130 SNPs in males, 151 SNPs in females) and estradiol (10 SNPs in males and females) separately for MR sensitivity analyses. Detailed information on the genetic instruments were provided in Supplementary file 1a-d. We used the STROBE case-control checklist when writing our report (von Elm et al., 2014).

### Data source from COVID-19 HGI

We obtained the summary level data of COVID-19 susceptibility, hospitalization, and severity from the COVID-19-HGI GWAS meta-analyses of data across 60 studies from 25 countries (Round 5, European population) where UK Biobank data were excluded (COVID-19 Host Genetics Initiative, 2020). The HGI dataset included 1,348,701 participants (32,494 laboratory-confirmed cases of SARS-CoV-2 infection and 1,316,207 population controls) for COVID-19 susceptibility, 1,557,411 participants (8316 hospitalized COVID-19 patients and 1,549,095 population controls) for COVID-19 hospitalization, and 1,059,456 participants (4792 very severe respiratory-confirmed COVID-19 cases and 1,054,664 controls) for COVID-19 severity. COVID-19-HGI defined very severe respiratory-confirmed COVID-19 cases as patients hospitalized for laboratory-confirmed SARS-CoV-2 infection who died or were given respiratory support. The characteristics of the participants are shown in Table 1.

**Table 1.**
 Sources of data for Mendelian randomization analysis in COVID-19 HGI.


<table>
  <thead>
    <tr>
      <th>Phenotype</th>
      <th>Participants</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">Susceptibility</td>
      <td>Meta-analysis of 35 GWAS performed in individuals of European ancestry</td>
    </tr>
    <tr>
      <td>Cases: 32,494 individuals with COVID-19 by laboratory confirmation, chart review, or self-report</td>
    </tr>
    <tr>
      <td>Controls: 1,316,207 individuals without confirmation or history of COVID-19</td>
    </tr>
    <tr>
      <td rowspan="3">Hospitalization</td>
      <td>Meta-analysis of 23 GWAS performed in individuals of European ancestry</td>
    </tr>
    <tr>
      <td>Cases: 8316 hospitalized individuals with COVID-19</td>
    </tr>
    <tr>
      <td>Controls: 1,549,095 individuals without confirmation or history of COVID-19</td>
    </tr>
    <tr>
      <td rowspan="3">Severity</td>
      <td>Meta-analysis of 14 GWAS performed in individuals of European ancestry</td>
    </tr>
    <tr>
      <td>Cases: 4792 SARS-CoV-2 infected hospitalized individuals who died or required respiratory support (intubation, CPAP, BiPAP, continuous external negative pressure, high flow nasal cannula).</td>
    </tr>
    <tr>
      <td>Controls:1,054,664 individuals without confirmation or history of COVID-19</td>
    </tr>
  </tbody>
</table>

_Notes: COVID-19 outcomes are taken from the COVID-19 HGI.HGI, Host Genetics Initiative; GWAS, genome-wide association study; UKB, UK Biobank; CPAP, continuous positive airway pressure ventilation; BiPAP, bilevel positive airway pressure ventilation._

### TSMR analyses

We applied the inverse variance weighted (IVW) method under the random-effects model as the primary MR analysis. We performed sensitivity analyses, including the weighted median, MR-Egger regression, leave-one-out analysis, and MR Pleiotropy RESidual Sum and Outlier (MR-PRESSO) methods, to examine the consistency of associations and to detect and correct for potential pleiotropy. The weighted median method was performed to provide unbiased causal estimates if at least 50% instrumental variables were valid (Bowden et al., 2016). MR-Egger regression was used to observe and correct potential directional pleiotropy, which was assessed by its intercept test (Bowden et al., 2015). MR-PRESSO method can detect SNP outliers and estimate the association after removal of these outliers. The differences in estimates between before and after outlier removal were examined by the embedded distortion test (Wu et al., 2020). Cochrane’s Q value was used to assess the heterogeneity among estimates of genetic instruments and the p value for intercept in MR-Egger was used to detect horizontal pleiotropy (Bowden et al., 2015). All statistical analyses were two-sided and performed in R 4.0.4 software using the R package TwoSampleMR and MR-PRESSO (Yavorska and Burgess, 2017).

### Sensitivity analyses

We additionally used the SNP rs7173595 in CYP19A1 gene, which encodes aromatase, an enzyme that converts androgens to estrogens. Rs7173595 has previously been shown to be strongly associated with serum E2 levels in GWAS of men (Ruth et al., 2020; Eriksson et al., 2018) and postmenopausal women (Thompson et al., 2016). This SNP was also associated with serum E2 in 25,502 premenopausal European women (<50 years of age and not reporting a hysterectomy or that menopause has occurred) in UK Biobank. The associations of serum E2 instrumented by rs7173595 in the CYP19A1 gene region with COVID-19 outcomes were estimated using the Wald ratio method. We further performed a sensitivity analysis using a list of genetic instruments consisting of 10 correlated SNPs (r2 < 0.4) located in the IGF-1 gene region (genomic position on build GRCh37/hg19: chromosome 12:102789652–102874341) and associated with IGF-1 levels at the genome-wide significance level. A matrix of linkage disequilibrium among these SNPs was introduced in the MR analysis model. To control potential data confounder, we selected SNPs associated with testosterone, estrogen, SHBG, and IGF-1 only, excluding SNPs associated with BMI which is thought to be a causal risk factor for COVID-19 (Freuer et al., 2021) at the threshold of 5×10–8 in European ancestry samples by querying PhenoScanner (Yavorska and Burgess, 2017). SNPs in estrogen were not excluded because their irrelevance to BMI.

## Results

Table 2 presents the TSMR estimates for the associations between sex hormones, SHBG, IGF-1, and the risk of COVID-19 susceptibility, hospitalization, and severity based on the data from HGI. Higher genetically predicted IGF-1 levels have nominally significant association with reduced risk of COVID-19 susceptibility and hospitalization. For one standard deviation increase in genetically predicted IGF-1 levels, the odds ratio was 0.77 (95% confidence interval [CI], 0.61–0.97, p=0.027) for COVID-19 susceptibility, 0.62 (95% CI: 0.25–0.51, p=0.018) for COVID-19 hospitalization, and 0.85 (95% CI: 0.52–1.38, p=0.513) for COVID-19 severity. Associations of IGF-1 levels with COVID-19 susceptibility and hospitalization were not statistically significant after Bonferroni correction, albeit showing a nominal significance at p<0.05. No outlying SNPs were identified by MR-PRESSO analyses. Estimates from the MR-Egger and weighted mode analyses were in the same direction as those from the IVW analysis (Figure 2, Figure 2—figure supplement 1, Figure 2—figure supplement 2). The MR-Egger intercept p was 0.614 and 0.595 for susceptibility and hospitalization, respectively, indicating the absence of directional pleiotropy. The associations remained directionally consistent in the sensitivity analysis based on SNPs located in the IGF-1 gene region as instrumental variables with risk of COVID-19 susceptibility (OR = 0.99, 95% CI: 0.91–1.07, p=0.777), hospitalization (OR = 0.90; 95% CI: 0.74–1.10, p=0.645), and severity (OR = 1.01; 95% CI: 0.82–1.24, p=0.415) (Table 3).

![Figure 2.](https://cdn.elifesciences.org/articles/79720/elife-79720-fig2-v2.jpg)

**Figure 2.:** Abbreviation: IGF-1, insulin-like growth factor-1; SNP, single-nucleotide polymorphism; IVW, inverse variance weighting; OR, odds ratio; CI, confidence interval.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/79720/elife-79720-fig2-figsupp1-v2.jpg)

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/79720/elife-79720-fig2-figsupp2-v2.jpg)

**Table 2.**
 Sex hormones, SHBG, IGF-1, and COVID-19 outcomes in Mendelian randomization (MR) analyses.


<table>
  <thead>
    <tr>
      <th rowspan="2">Exposure</th>
      <th rowspan="2">Method</th>
      <th colspan="5">Susceptibility</th>
      <th colspan="5">Hospitalization</th>
      <th colspan="5">Severity</th>
    </tr>
    <tr>
      <th>SNPs</th>
      <th>OR (95% CI)</th>
      <th>p Effect</th>
      <th>p Heterogeneity</th>
      <th>p Intercept</th>
      <th>SNPs</th>
      <th>OR (95% CI)</th>
      <th>p Effect</th>
      <th>p Heterogeneity</th>
      <th>p Intercept</th>
      <th>SNPs</th>
      <th>OR (95% CI)</th>
      <th>p Effect</th>
      <th>p Heterogeneity</th>
      <th>p Intercept</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="6">Testosterone</td>
      <td>IVW</td>
      <td rowspan="6">315</td>
      <td>0.94 (0.83, 1.06)</td>
      <td>0.309</td>
      <td>0.006</td>
      <td>–</td>
      <td rowspan="6">303</td>
      <td>0.82 (0.64, 1.04)</td>
      <td>0.103</td>
      <td>0.055</td>
      <td>–</td>
      <td rowspan="6">316</td>
      <td>0.83 (0.60, 1.15)</td>
      <td>0.256</td>
      <td>0.041</td>
      <td>–</td>
    </tr>
    <tr>
      <td>MR-Egger</td>
      <td>0.93 (0.76, 1.12)</td>
      <td>0.430</td>
      <td>0.005</td>
      <td>0.860</td>
      <td>0.79 (0.55, 1.15)</td>
      <td>0.217</td>
      <td>0.051</td>
      <td>0.819</td>
      <td>0.78 (0.48, 1.27)</td>
      <td>0.313</td>
      <td>0.038</td>
      <td>0.732</td>
    </tr>
    <tr>
      <td>Weighted median</td>
      <td>0.89 (0.71, 1.12)</td>
      <td>0.329</td>
      <td>–</td>
      <td>–</td>
      <td>0.81 (0.52, 1.28)</td>
      <td>0.370</td>
      <td>–</td>
      <td>–</td>
      <td>0.71 (0.40, 1.26)</td>
      <td>0.246</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Simple mode</td>
      <td>1.13 (0.73, 1.77)</td>
      <td>0.584</td>
      <td>–</td>
      <td>–</td>
      <td>0.77 (0.27, 2.20)</td>
      <td>0.623</td>
      <td>–</td>
      <td>–</td>
      <td>0.44 (0.09, 2.18)</td>
      <td>0.316</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Weighted mode</td>
      <td>0.91 (0.77, 1.08)</td>
      <td>0.300</td>
      <td>–</td>
      <td>–</td>
      <td>0.77 (0.52, 1.13)</td>
      <td>0.180</td>
      <td>–</td>
      <td>–</td>
      <td>0.65 (0.40, 1.05)</td>
      <td>0.081</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>MR-PRESSO</td>
      <td>0.94 (1.06, 0.84)</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>0.82 (1.04, 0.65)</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>0.83 (1.15, 0.59)</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td rowspan="6">SHBG</td>
      <td>IVW</td>
      <td rowspan="6">319</td>
      <td>0.91 (0.80, 1.04)</td>
      <td>0.182</td>
      <td>0.002</td>
      <td>–</td>
      <td rowspan="6">309</td>
      <td>0.86 (0.66, 1.11)</td>
      <td>0.255</td>
      <td>0.087</td>
      <td>–</td>
      <td rowspan="6">320</td>
      <td>0.92 (0.65, 1.29)</td>
      <td>0.618</td>
      <td>0.096</td>
      <td>–</td>
    </tr>
    <tr>
      <td>MR-Egger</td>
      <td>0.96 (0.78, 1.18)</td>
      <td>0.708</td>
      <td>0.002</td>
      <td>0.494</td>
      <td>0.83 (0.57, 1.22)</td>
      <td>0.352</td>
      <td>0.081</td>
      <td>0.818</td>
      <td>0.92 (0.56, 1.51)</td>
      <td>0.730</td>
      <td>0.090</td>
      <td>0.994</td>
    </tr>
    <tr>
      <td>Weighted median</td>
      <td>0.90 (0.72, 1.13)</td>
      <td>0.360</td>
      <td>–</td>
      <td>–</td>
      <td>0.82 (0.52, 1.29)</td>
      <td>0.391</td>
      <td>–</td>
      <td>–</td>
      <td>0.72 (0.41, 1.27)</td>
      <td>0.255</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Simple mode</td>
      <td>1.09 (0.66, 1.81)</td>
      <td>0.735</td>
      <td>–</td>
      <td>–</td>
      <td>1.18 (0.40, 3.44)</td>
      <td>0.767</td>
      <td>–</td>
      <td>–</td>
      <td>1.16 (0.25, 5.41)</td>
      <td>0.850</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Weighted mode</td>
      <td>0.94 (0.78, 1.14)</td>
      <td>0.547</td>
      <td>–</td>
      <td>–</td>
      <td>0.81 (0.56, 1.18)</td>
      <td>0.279</td>
      <td>–</td>
      <td>–</td>
      <td>0.79 (0.47, 1.33)</td>
      <td>0.376</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>MR-PRESSO</td>
      <td>0.91 (1.05, 0.80)</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>0.86 (1.11, 0.67)</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>0.91 (1.28, 0.65)</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td rowspan="6">Estradiol</td>
      <td>IVW</td>
      <td rowspan="6">7</td>
      <td>0.54 (0.15, 1.94)</td>
      <td>0.346</td>
      <td>0.188</td>
      <td>–</td>
      <td rowspan="6">7</td>
      <td>0.87 (0.11, 6.70)</td>
      <td>0.895</td>
      <td>0.769</td>
      <td>–</td>
      <td rowspan="6">7</td>
      <td>0.50 (0.03, 7.64)</td>
      <td>0.620</td>
      <td>0.987</td>
      <td>–</td>
    </tr>
    <tr>
      <td>MR-Egger</td>
      <td>0.73 (0.04, 14.11)</td>
      <td>0.845</td>
      <td>0.123</td>
      <td>0.830</td>
      <td>0.34 (0.00, 29.54)</td>
      <td>0.657</td>
      <td>0.685</td>
      <td>0.662</td>
      <td>0.04 (0.00, 17.04)</td>
      <td>0.345</td>
      <td>1.000</td>
      <td>0.401</td>
    </tr>
    <tr>
      <td>Weighted median</td>
      <td>0.36 (0.10, 1.35)</td>
      <td>0.130</td>
      <td>–</td>
      <td>–</td>
      <td>0.35 (0.03, 4.21)</td>
      <td>0.407</td>
      <td>–</td>
      <td>–</td>
      <td>0.30 (0.01, 7.26)</td>
      <td>0.458</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Simple mode</td>
      <td>0.29 (0.03, 2.60)</td>
      <td>0.313</td>
      <td>–</td>
      <td>–</td>
      <td>0.71 (0.01, 44.94)</td>
      <td>0.875</td>
      <td>–</td>
      <td>–</td>
      <td>0.33 (0.00, 43.56)</td>
      <td>0.673</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Weighted mode</td>
      <td>0.34 (0.07, 1.73)</td>
      <td>0.241</td>
      <td>–</td>
      <td>–</td>
      <td>0.38 (0.03, 4.81)</td>
      <td>0.482</td>
      <td>–</td>
      <td>–</td>
      <td>0.29 (0.01, 9.43)</td>
      <td>0.511</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>MR-PRESSO</td>
      <td>0.54 (1.94, 0.15)</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>0.87 (3.93, 0.19)</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>0.51 (1.52, 0.17)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td rowspan="6">IGF-1</td>
      <td>IVW</td>
      <td rowspan="6">16</td>
      <td>0.77 (0.61, 0.97)</td>
      <td>0.027</td>
      <td>0.175</td>
      <td>–</td>
      <td rowspan="6">16</td>
      <td>0.62 (0.25, 0.51)</td>
      <td>0.018</td>
      <td>0.715</td>
      <td>–</td>
      <td rowspan="6">18</td>
      <td>0.85 (0.52, 1.38)</td>
      <td>0.513</td>
      <td>0.601</td>
      <td>-</td>
    </tr>
    <tr>
      <td>MR-Egger</td>
      <td>0.84 (0.56, 1.26)</td>
      <td>0.408</td>
      <td>0.145</td>
      <td>0.614</td>
      <td>0.72 (0.37, 1.38)</td>
      <td>0.336</td>
      <td>0.668</td>
      <td>0.595</td>
      <td>1.45 (0.67, 3.10)</td>
      <td>0.358</td>
      <td>0.758</td>
      <td>0.096</td>
    </tr>
    <tr>
      <td>Weighted median</td>
      <td>0.76 (0.57, 1.02)</td>
      <td>0.071</td>
      <td>–</td>
      <td>–</td>
      <td>0.75 (0.44, 1.28)</td>
      <td>0.294</td>
      <td>–</td>
      <td>–</td>
      <td>0.76 (0.38, 1.53)</td>
      <td>0.446</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Simple mode</td>
      <td>0.64 (0.39, 1.05)</td>
      <td>0.097</td>
      <td>–</td>
      <td>–</td>
      <td>0.66 (0.30, 1.45)</td>
      <td>0.318</td>
      <td>–</td>
      <td>–</td>
      <td>0.82 (0.27, 2.47)</td>
      <td>0.730</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>Weighted mode</td>
      <td>0.77 (0.58, 1.02)</td>
      <td>0.084</td>
      <td>–</td>
      <td>–</td>
      <td>0.71 (0.44, 1.17)</td>
      <td>0.199</td>
      <td>–</td>
      <td>–</td>
      <td>0.70 (0.35, 1.38)</td>
      <td>0.319</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>MR-PRESSO</td>
      <td>0.77 (0.98, 0.61)</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>0.62 (0.88, 0.43)</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>0.85 (1.34, 0.54)</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
  </tbody>
</table>

_SNP, single-nucleotide polymorphism; OR, odds ratio; CI, confidence interval; IVW, inverse variance weighting; SHBG, sex hormones-binding globulin; IGF-1, insulin-like growth factor-1._

**Table 3.**
 Sensitive analysis between serum IGF-1 levels instrumented by 10 SNPs in the IGF-1 gene region and COVID-19 outcomes.


<table>
  <thead>
    <tr>
      <th rowspan="2">Method</th>
      <th colspan="4">Susceptibility</th>
      <th colspan="4">Hospitalization</th>
      <th colspan="4">Severity</th>
    </tr>
    <tr>
      <th>OR (95% CI)</th>
      <th>p Effect</th>
      <th>p Heterogeneity</th>
      <th>p Intercept</th>
      <th>OR (95% CI)</th>
      <th>p Effect</th>
      <th>p Heterogeneity</th>
      <th>p Intercept</th>
      <th>OR (95% CI)</th>
      <th>p Effect</th>
      <th>p Heterogeneity</th>
      <th>p Intercept</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>IVW</td>
      <td>0.99 (0.91, 1.07)</td>
      <td>0.777</td>
      <td>0.596</td>
      <td>–</td>
      <td>0.90 (0.74, 1.10)</td>
      <td>0.645</td>
      <td>0.104</td>
      <td>–</td>
      <td>1.01 (0.82, 1.24)</td>
      <td>0.415</td>
      <td>0.437</td>
      <td>–</td>
    </tr>
    <tr>
      <td>MR-Egger</td>
      <td>0.99 (0.93, 1.05)</td>
      <td>0.732</td>
      <td>0.541</td>
      <td>0.527</td>
      <td>0.97 (0.84, 1.11)</td>
      <td>0.338</td>
      <td>0.108</td>
      <td>0.375</td>
      <td>1.09 (0.92, 1.30)</td>
      <td>0.953</td>
      <td>0.372</td>
      <td>0.590</td>
    </tr>
    <tr>
      <td>Weighted median</td>
      <td>1.01 (0.96, 1.06)</td>
      <td>0.739</td>
      <td>–</td>
      <td>–</td>
      <td>0.97 (0.86, 1.10)</td>
      <td>0.620</td>
      <td>–</td>
      <td>–</td>
      <td>1.05 (0.93, 1.20)</td>
      <td>0.310</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Simple mode</td>
      <td>0.98 (0.89, 1.08)</td>
      <td>0.685</td>
      <td>–</td>
      <td>–</td>
      <td>1.12 (0.88, 1.43)</td>
      <td>0.395</td>
      <td>–</td>
      <td>–</td>
      <td>1.16 (0.88, 1.51)</td>
      <td>0.316</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Weighted mode</td>
      <td>0.98 (0.92, 1.05)</td>
      <td>0.596</td>
      <td>–</td>
      <td>–</td>
      <td>0.94 (0.82, 1.09)</td>
      <td>0.439</td>
      <td>–</td>
      <td>–</td>
      <td>1.12 (0.92, 1.37)</td>
      <td>0.279</td>
      <td>–</td>
      <td>–</td>
    </tr>
  </tbody>
</table>

_IGF-1, insulin-like growth factor-1; SNP, single-nucleotide polymorphism; IVW, inverse variance weighting; OR, odds ratio; CI, confidence interval._

In the analyses based on data from the genetic consortia, we found no causal associations of genetically predicted testosterone with the risk of COVID-19 susceptibility (OR = 0.94; 95% CI: 0.83–1.06, p=0.309), hospitalization (OR = 0.82; 95% CI: 0.64–1.04, p=0.103), risk of severity (OR = 0.83; 95% CI: 0.60–1.15, p=0.256). Null association was also noticed between SHBG and COVID-19 susceptibility (OR = 0.91; 95% CI: 0.80–1.04, p=0.182), hospitalization (OR = 0.86; 95% CI: 0.66–1.11, p=0.255), risk of severity (OR = 0.92; 95% CI: 0.65–1.29, p=0.618). Overall, no significant associations between testosterone, estrogen, SHBG, and COVID-19 outcomes were observed from TSMR analyses. Sex-specific associations of genetically testosterone and estradiol levels with COVID-19 risk (Table 4) were still nonsignificant. We noticed that the p for intercept in MR-Egger regression analysis was more than 0.05 for both genders, and no outlier was detected. Genetic predisposition to higher serum E2 levels proxied by rs7173595 in the CYP19A1 gene was not associated with the risk of COVID-19 susceptibility (OR = 0.32; 95% CI, 0.06–1.80, p = 0.195), hospitalization (OR = 0.28; 95% CI: 0.01–6.46, p=0.426), and severity (OR = 0.22; 95% CI: 0.00–12.73, p=0.469) in females; similarly, the associations remained directionally consistent in males with susceptibility (OR = 0.37; 95% CI, 0.08–1.67, p = 0.195), hospitalization (OR = 0.33; 95% CI: 0.02–5.11, p=0.426), and severity (OR = 0.27; 95% CI: 0.01–9.26, p=0.469) (Table 5). As shown in Table 6, after removing SNPs associated with BMI, we found similar associations of genetically predicted IGF-1 levels with the risk of COVID-19 susceptibility (OR = 0.76; 95% CI: 0.60–0.96, p=0.021), hospitalization (OR = 0.61; 95% CI: 0.41–0.90, p=0.014), risk of severity (OR = 0.84; 95% CI: 0.52–1.38, p=0.497) in which we detected no moderate heterogeneity, and no indication of horizontal pleiotropy in MR-Egger, and no outlier in MR-PRESSO analyses. No causal associations of genetically predicted testosterone and SHBG with COVID-19 were found, but the directions were consistent with results in Table 2.

**Table 4.**
 Sex-specific associations of genetically testosterone and estradiol levels with COVID-19 risk.


<table>
  <thead>
    <tr>
      <th rowspan="3">Exposure</th>
      <th rowspan="3">Method</th>
      <th colspan="4">Susceptibility</th>
      <th colspan="4">Hospitalization</th>
      <th colspan="4">Severity</th>
    </tr>
    <tr>
      <th colspan="2">Male</th>
      <th colspan="2">Female</th>
      <th colspan="2">Male</th>
      <th colspan="2">Female</th>
      <th colspan="2">Male</th>
      <th colspan="2">Female</th>
    </tr>
    <tr>
      <th>OR (95% CI)</th>
      <th>p</th>
      <th>OR (95% CI)</th>
      <th>p</th>
      <th>OR (95% CI)</th>
      <th>p</th>
      <th>OR (95% CI)</th>
      <th>p</th>
      <th>OR (95% CI)</th>
      <th>p</th>
      <th>OR (95% CI)</th>
      <th>p</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="5">Testosterone</td>
      <td>IVW</td>
      <td>0.96 (0.90, 1.05)</td>
      <td>0.463</td>
      <td>1.06 (0.97, 1.15)</td>
      <td>0.214</td>
      <td>0.96 (0.83, 1.10)</td>
      <td>0.547</td>
      <td>1.03 (0.87, 1.22)</td>
      <td>0.731</td>
      <td>1.07 (0.89, 1.27)</td>
      <td>0.479</td>
      <td>0.88 (0.69, 1.11)</td>
      <td>0.269</td>
    </tr>
    <tr>
      <td>MR-Egger</td>
      <td>0.97 (0.86, 1.09)</td>
      <td>0.644</td>
      <td>1.04 (0.85, 1.26)</td>
      <td>0.713</td>
      <td>0.88 (0.71, 1.10)</td>
      <td>0.270</td>
      <td>1.13 (0.76, 1.69)</td>
      <td>0.549</td>
      <td>0.81 (0.62, 1.08)</td>
      <td>0.152</td>
      <td>0.68 (0.39, 1.18)</td>
      <td>0.169</td>
    </tr>
    <tr>
      <td>Weighted median</td>
      <td>0.93 (0.83, 1.04)</td>
      <td>0.184</td>
      <td>1.06 (0.94, 1.19)</td>
      <td>0.370</td>
      <td>0.89 (0.72, 1.10)</td>
      <td>0.277</td>
      <td>1.08 (0.84, 1.39)</td>
      <td>0.523</td>
      <td>0.89 (0.67, 1.19)</td>
      <td>0.438</td>
      <td>0.81 (0.57, 1.14)</td>
      <td>0.227</td>
    </tr>
    <tr>
      <td>p for intercept</td>
      <td>1.00 (1.00, 1.00)</td>
      <td>0.998</td>
      <td>1.00 (0.99, 1.01)</td>
      <td>0.854</td>
      <td>1.00 (1.00, 1.01)</td>
      <td>0.348</td>
      <td>1.00 (0.99, 1.01)</td>
      <td>0.615</td>
      <td>1.01 (1.00, 1.02)</td>
      <td>0.017</td>
      <td>1.01 (0.99, 1.03)</td>
      <td>0.314</td>
    </tr>
    <tr>
      <td>MR-PRESSO</td>
      <td>0.97 (0.90, 1.05)</td>
      <td>0.464</td>
      <td>1.06 (0.97, 1.15)</td>
      <td>0.216</td>
      <td>0.96 (0.83, 1.10)</td>
      <td>0.549</td>
      <td>1.03 (0.87, 1.22)</td>
      <td>0.732</td>
      <td>1.07 (0.89, 1.27)</td>
      <td>0.478</td>
      <td>0.88 (0.69, 1.11)</td>
      <td>0.270</td>
    </tr>
    <tr>
      <td rowspan="5">Estradiol</td>
      <td>IVW</td>
      <td>0.99 (0.89, 1.11)</td>
      <td>0.923</td>
      <td>0.95 (0.71, 1.26)</td>
      <td>0.724</td>
      <td>0.98 (0.81, 1.18)</td>
      <td>0.826</td>
      <td>1.04 (0.63, 1.73)</td>
      <td>0.873</td>
      <td>0.90 (0.71, 1.15)</td>
      <td>0.403</td>
      <td>1.39 (0.74, 7.15)</td>
      <td>0.310</td>
    </tr>
    <tr>
      <td>MR-Egger</td>
      <td>1.00 (0.73, 1.36)</td>
      <td>0.993</td>
      <td>0.89 (0.59, 1.34)</td>
      <td>0.598</td>
      <td>0.93 (0.52, 1.67)</td>
      <td>0.812</td>
      <td>1.15 (0.56, 2.34)</td>
      <td>0.719</td>
      <td>0.61 (0.29, 6.15)</td>
      <td>0.233</td>
      <td>1.76 (0.74, 3.15)</td>
      <td>0.234</td>
    </tr>
    <tr>
      <td>Weighted median</td>
      <td>1.05 (0.92, 1.20)</td>
      <td>0.432</td>
      <td>0.95 (0.68, 1.32)</td>
      <td>0.745</td>
      <td>0.93 (0.74, 1.16)</td>
      <td>0.508</td>
      <td>1.32 (0.67, 2.57)</td>
      <td>0.422</td>
      <td>0.88 (0.65, 1.15)</td>
      <td>0.411</td>
      <td>1.96 (0.81, 5.15)</td>
      <td>0.135</td>
    </tr>
    <tr>
      <td>p for intercept</td>
      <td>1.00 (0.96, 1.04)</td>
      <td>0.980</td>
      <td>1.00 (0.99, 1.02)</td>
      <td>0.669</td>
      <td>1.01 (0.94, 1.08)</td>
      <td>0.856</td>
      <td>0.99 (0.96, 1.02)</td>
      <td>0.707</td>
      <td>1.05 (0.96, 0.15)</td>
      <td>0.312</td>
      <td>0.99 (0.95, 0.15)</td>
      <td>0.441</td>
    </tr>
    <tr>
      <td>MR-PRESSO</td>
      <td>0.99 (0.89, 1.11)</td>
      <td>0.925</td>
      <td>0.95 (0.71, 1.26)</td>
      <td>0.732</td>
      <td>0.98 (0.81, 1.18)</td>
      <td>0.831</td>
      <td>1.04 (0.63, 1.73)</td>
      <td>0.877</td>
      <td>0.90 (0.71, 1.15)</td>
      <td>0.425</td>
      <td>1.39 (0.74, 2.63)</td>
      <td>0.335</td>
    </tr>
  </tbody>
</table>

_OR, odds ratio; CI, confidence interval; IVW, inverse variance weighting._

**Table 5.**
 Associations of serum E2 levels instrumented by rs7173595 in the CYP19A1 gene region with COVID-19 outcomes.


<table>
  <thead>
    <tr>
      <th>Sex</th>
      <th>Phenotype</th>
      <th>beta</th>
      <th>SE</th>
      <th>OR (95% CI)</th>
      <th>p Effect</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">Female</td>
      <td>Susceptibility</td>
      <td>–1.14</td>
      <td>0.88</td>
      <td>0.32 (0.06, 1.80)</td>
      <td>0.195</td>
    </tr>
    <tr>
      <td>Hospitalization</td>
      <td>–1.27</td>
      <td>1.60</td>
      <td>0.28 (0.01, 6.46)</td>
      <td>0.426</td>
    </tr>
    <tr>
      <td>Severity</td>
      <td>–1.49</td>
      <td>2.06</td>
      <td>0.22 (0.00, 12.73)</td>
      <td>0.469</td>
    </tr>
    <tr>
      <td rowspan="3">Male</td>
      <td>Susceptibility</td>
      <td>–1.00</td>
      <td>0.77</td>
      <td>0.37 (0.08, 1.67)</td>
      <td>0.195</td>
    </tr>
    <tr>
      <td>Hospitalization</td>
      <td>–1.11</td>
      <td>1.40</td>
      <td>0.33 (0.02, 5.11)</td>
      <td>0.426</td>
    </tr>
    <tr>
      <td>Severity</td>
      <td>–1.31</td>
      <td>1.80</td>
      <td>0.27 (0.01, 9.26)</td>
      <td>0.469</td>
    </tr>
  </tbody>
</table>

_E2, estradiol; OR, odds ratio; CI, confidence interval._

**Table 6.**
 Testosterone, SHBG, IGF-1, and COVID-19 outcomes in Mendelian randomization (MR) analyses adjusting BMI.


<table>
  <thead>
    <tr>
      <th rowspan="2">Exposure</th>
      <th rowspan="2">Method</th>
      <th colspan="5">Susceptibility</th>
      <th colspan="5">Hospitalization</th>
      <th colspan="5">Severity</th>
    </tr>
    <tr>
      <th>SNPs</th>
      <th>OR (95% CI)</th>
      <th>p Effect</th>
      <th>p Heterogeneity</th>
      <th>p Intercept</th>
      <th>SNPs</th>
      <th>OR (95% CI)</th>
      <th>p Effect</th>
      <th>p Heterogeneity</th>
      <th>p Intercept</th>
      <th>SNPs</th>
      <th>OR (95% CI)</th>
      <th>p Effect</th>
      <th>p Heterogeneity</th>
      <th>p Intercept</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="6">Testosterone</td>
      <td>IVW</td>
      <td rowspan="6">306</td>
      <td>0.95 (0.83,1.07)</td>
      <td>0.386</td>
      <td>0.006</td>
      <td>–</td>
      <td rowspan="6">294</td>
      <td>0.83 (0.64,1.06)</td>
      <td>0.134</td>
      <td>0.041</td>
      <td>–</td>
      <td rowspan="6">307</td>
      <td>0.84 (0.60,1.17)</td>
      <td>0.304</td>
      <td>0.030</td>
      <td>–</td>
    </tr>
    <tr>
      <td>MR-Egger</td>
      <td>0.93 (0.77,1.13)</td>
      <td>0.484</td>
      <td>0.006</td>
      <td>0.855</td>
      <td>0.83 (0.56,1.21)</td>
      <td>0.324</td>
      <td>0.038</td>
      <td>0.991</td>
      <td>0.83 (0.50,1.37)</td>
      <td>0.466</td>
      <td>0.027</td>
      <td>0.949</td>
    </tr>
    <tr>
      <td>Weighted median</td>
      <td>0.90 (0.72,1.12)</td>
      <td>0.331</td>
      <td>–</td>
      <td>–</td>
      <td>0.82 (0.52,1.28)</td>
      <td>0.375</td>
      <td>–</td>
      <td>–</td>
      <td>0.71 (0.42,1.21)</td>
      <td>0.214</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Simple mode</td>
      <td>1.13 (0.70,1.82)</td>
      <td>0.610</td>
      <td>–</td>
      <td>–</td>
      <td>0.68 (0.24,1.91)</td>
      <td>0.465</td>
      <td>–</td>
      <td>–</td>
      <td>0.37 (0.07,1.88)</td>
      <td>0.229</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Weighted mode</td>
      <td>0.95 (0.79,1.13)</td>
      <td>0.540</td>
      <td>–</td>
      <td>–</td>
      <td>0.81 (0.56,1.17)</td>
      <td>0.273</td>
      <td>–</td>
      <td>–</td>
      <td>0.65 (0.40,1.06)</td>
      <td>0.085</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>MR-PRESSO</td>
      <td>0.94 (0.83,1.07)</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>0.83 (0.64,1.06)</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>0.83 (0.64,1.06)</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td rowspan="6">SHBG</td>
      <td>IVW</td>
      <td rowspan="6">308</td>
      <td>0.90 (0.79,1.04)</td>
      <td>0.160</td>
      <td>0.002</td>
      <td>–</td>
      <td rowspan="6">198</td>
      <td>0.84 (0.64,1.10)</td>
      <td>0.209</td>
      <td>0.047</td>
      <td>–</td>
      <td rowspan="6">309</td>
      <td>0.89 (0.62,1.26)</td>
      <td>0.511</td>
      <td>0.058</td>
      <td>–</td>
    </tr>
    <tr>
      <td>MR-Egger</td>
      <td>0.94 (0.76,1.15)</td>
      <td>0.538</td>
      <td>0.001</td>
      <td>0.663</td>
      <td>0.81 (0.54,1.21)</td>
      <td>0.299</td>
      <td>0.043</td>
      <td>0.794</td>
      <td>0.89 (0.53,1.49)</td>
      <td>0.666</td>
      <td>0.054</td>
      <td>0.978</td>
    </tr>
    <tr>
      <td>Weighted median</td>
      <td>0.90 (0.71,1.13)</td>
      <td>0.356</td>
      <td>–</td>
      <td>–</td>
      <td>0.81 (0.52,1.28)</td>
      <td>0.377</td>
      <td>–</td>
      <td>–</td>
      <td>0.72 (0.42,1.23)</td>
      <td>0.230</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Simple mode</td>
      <td>1.05 (0.60,1.84)</td>
      <td>0.860</td>
      <td>–</td>
      <td>–</td>
      <td>1.25 (0.42,3.78)</td>
      <td>0.689</td>
      <td>–</td>
      <td>–</td>
      <td>0.97 (0.22,4.22)</td>
      <td>0.967</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Weighted mode</td>
      <td>0.94 (0.77,1.15)</td>
      <td>0.570</td>
      <td>–</td>
      <td>–</td>
      <td>0.81 (0.55,1.20)</td>
      <td>0.295</td>
      <td>–</td>
      <td>–</td>
      <td>0.72 (0.43,1.22)</td>
      <td>0.224</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>MR-PRESSO</td>
      <td>0.90 (0.79,1.04)</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>0.84 (0.64,1.10)</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>0.89 (0.62,1.26)</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td rowspan="6">IGF-1</td>
      <td>IVW</td>
      <td rowspan="6">15</td>
      <td>0.76 (0.60,0.96)</td>
      <td>0.021</td>
      <td>0.172</td>
      <td>–</td>
      <td rowspan="6">15</td>
      <td>0.61 (0.41,0.90)</td>
      <td>0.014</td>
      <td>0.688</td>
      <td>–</td>
      <td rowspan="6">17</td>
      <td>0.84 (0.52,1.38)</td>
      <td>0.497</td>
      <td>0.534</td>
      <td>–</td>
    </tr>
    <tr>
      <td>MR-Egger</td>
      <td>0.88 (0.58,1.33)</td>
      <td>0.554</td>
      <td>0.168</td>
      <td>0.390</td>
      <td>0.77 (0.39,1.50)</td>
      <td>0.458</td>
      <td>0.676</td>
      <td>0.403</td>
      <td>1.55 (0.71,3.39)</td>
      <td>0.284</td>
      <td>0.757</td>
      <td></td>
    </tr>
    <tr>
      <td>Weighted median</td>
      <td>0.75 (0.57,0.99)</td>
      <td>0.046</td>
      <td>–</td>
      <td>–</td>
      <td>0.75 (0.45,1.24)</td>
      <td>0.260</td>
      <td>–</td>
      <td>–</td>
      <td>0.75 (0.38,1.48)</td>
      <td>0.410</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Simple mode</td>
      <td>0.65 (0.38,1.11)</td>
      <td>0.135</td>
      <td>–</td>
      <td>–</td>
      <td>0.64 (0.30,1.37)</td>
      <td>0.265</td>
      <td>–</td>
      <td>–</td>
      <td>0.75 (0.25,2.31)</td>
      <td>0.629</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Weighted mode</td>
      <td>0.76 (0.56,1.03)</td>
      <td>0.096</td>
      <td>–</td>
      <td>–</td>
      <td>0.71 (0.44,1.15)</td>
      <td>0.185</td>
      <td>–</td>
      <td>–</td>
      <td>0.72 (0.36,1.47)</td>
      <td>0.383</td>
      <td>–</td>
      <td>–</td>
    </tr>
    <tr>
      <td>MR-PRESSO</td>
      <td>0.76 (0.60,0.96)</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>0.61 (0.43,0.86)</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
      <td>0.84 (0.53,1.35)</td>
      <td>–</td>
      <td>–</td>
      <td>–</td>
    </tr>
  </tbody>
</table>

_SNP, single-nucleotide polymorphism; OR, odds ratio; CI, confidence interval; IVW, inverse variance weighting; SHBG, sex hormones-binding globulin; IGF-1, insulin-like growth factor-1._

## Discussion

In this study, we assessed whether there were any causal associations between sex hormone-related biomarkers and the risk of COVID-19 outcomes. We found suggestive evidence for associations between genetic liability to high IGF-1 levels and decreased risk of COVID-19 susceptibility and hospitalization. Our findings suggest a potential role of IGF-1 in COVID-19 risk and have implications for tailored treatment of COVID-19 patients.

Our MR findings were consistent with the multiple epidemiological studies that reported a nominal association between measured IGF-1 levels and COVID-19 illness. There is one observational study that demonstrated an inverse association between pre-diagnostic circulating levels of IGF-1 and COVID-19 mortality risk among COVID-19 patients in UK Biobank (Fan et al., 2021). Another observational study in Greece reported lower IGF-1 levels in critically ill COVID-19 patients compared to their counterparts with less severe disease or without COVID-19 (Ilias et al., 2021). A single-cell analysis revealed that the exhaustion of CD8+ T cells together with several cytokines including IGF-1 was associated with the pathogenesis of severe SARS-CoV-2 infection (He et al., 2021). Our MR analyses found a negative association between genetically determined high circulating IGF-1 levels and decreased risk of COVID-19 susceptibility and hospitalization, indicating IGF-1 may be a protective factor of COVID-19 risk.

IGF-1 has been found to be pro-survival/anti-aging, anti-inflammatory, and antioxidant with neuro- and hepatoprotective properties. A study by the Narasaraju group demonstrated that IGF-1 plays an important role in the repair of lung tissue by regulating the proliferation and differentiation of alveolar epithelial cells (AECs) (Narasaraju et al., 2006). Airway inflammation can be mitigated when apoptotic cells are engulfed by pulmonary epithelial cells (Juncadella et al., 2013). IGF-1 has also been shown to upregulate engulfment by professional phagocytes such as dendritic cells (Xuan et al., 2017), and inhibit IL-6 production from lipopolysaccharide-induced AECs (Wang et al., 2019). Both of these mechanisms are beneficial to the regression of local inflammation. Jakn et al. showed that IGF-1 binds to IGF-1 receptor (IGF-1R) on airway epithelial cells of non-professional phagocytic cells, which can promote the phagocytosis of microparticles by airway epithelial cells (Han et al., 2016). Transforming growth factor β1 derived from AECs activated alveolar macrophages (AMs) to secrete IGF-1 into the alveolar fluid in response to stimulation of the airway by inflammatory signals. This AM-derived IGF-1 attenuated the p38 mitogen-activated protein kinase inflammatory signal in AECs and promoted the phagocytosis of apoptotic cells by AECs. This two-way communication between AECs and AMs represents a well-tuned system for the regulation of the inflammatory response in alveoli (Mu et al., 2020). Taken together, these studies provide biological evidence supporting that IGF-1 might be an important anti-inflammatory factor in the alveolar microenvironment and thus may contribute to improve COVID-19 outcomes. More studies are required to determine whether novel therapeutic strategy targeting on IGF-1 pathway might improve COVID-19 prognosis.

IGF-1 level is regulated by estrogen and the functional interactions between estradiol and IGF-1 signaling system involve several transcriptional and posttranscriptional mechanisms. Specifically, IGF-1 can affect estrogen receptor α action by enhancing its expression and potentiating its transcriptional activity in a ligand-independent manner (Lange, 2004; Edwards et al., 1993; Shupnik, 2004). On the other hand, E2 can enhance IGF-1 signaling by upregulating the expression of IGF-1 (Umayahara et al., 1994), IGF-1R (Bartucci et al., 2001), and some IGF-1-binding proteins (Qin et al., 1999). This may explain the same direction from the IVW analysis of IGF-1, estradiol, and COVID-19 outcomes. Estrogen is found to have immune enhancing effect (Taneja, 2018) to trigger the local immune response by activating a plethora of cells such as phagocytes, dendritic cells, natural killers, and CD8+ T cells. Once these immune cells are activated, they could fight against the infection by destroying the virus and thus preventing its diffusion to the lower respiratory tract or by decreasing the viral load. Experimental tests have also reported that estradiol can affect angiotensin-converting enzyme 2 and FURIN expression, with the potential of mitigating SARS-CoV-2 infection (Glinsky, 2020). However, our study did not find any supportive evidence for the associations between estradiol and COVID-19, which might be due to the small variance of estradiol explained by genetic instruments.

Our studies showed that SHBG or testosterone may not be associated with COVID-19 outcomes, which is consistent with the research findings of Liu et al., 2022. They also observed a null causal relationship for testosterone or SHBG levels with COVID-19 outcomes in females and males. Meanwhile, epidemiologic data (Peckham et al., 2020) indicate that while men are not more predisposed to contracting COVID-19, they are more likely to develop severe illness following the infection compared with women. However, our study observed null causal relationship for testosterone levels with COVID-19 outcomes in both females and males. According to the available evidence on the role of testosterone in COVID-19, it appears that both high and low testosterone levels can be associated with poor COVID-19 outcomes (Ho et al., 2022). A study demonstrated androgen deprivation therapy (ADT) exposure was associated with a reduction in COVID-19 severity (Lee et al., 2022). By contrast, the Ohio study did not identify any protective effect of ADT on the severity of COVID-19 outcomes (Klein et al., 2021). Androgen-related treatments showed that transmembrane serine protease 2 (TMPRSS2) expression and SARS-CoV-2 entry in human lung cells have been reduced by antiandrogens (Leach et al., 2021; Deng et al., 2021; Qiao et al., 2020). Additionally, androgens have numerous immunosuppressive effects such as decreasing proinflammatory cytokine release (e.g., IFNγ and TNF) or increasing anti-inflammatory cytokine release (e.g., IL-4 and IL-10), reducing T helper 1 (Th1) and T helper 17 (Th17) cell differentiation, inducing Treg differentiation and regulating B-cell development (Olsen and Kovacs, 2011; Henze et al., 2020; Trigunaite et al., 2015). Paradoxically, these immunosuppressive effects of testosterone might be beneficial to overcome the heightened inflammatory environment that predisposes to severe COVID-19. Recent research has revealed that males with COVID-19 have lower testosterone levels (Ma et al., 2021). Another study found a negative association between total testosterone levels and biochemical markers of COVID-19 severity (Rastrelli et al., 2021). Lower testosterone concentrations were associated with higher concentrations of IL-6, CRP, IL-1 receptor antagonist, hepatocyte growth factor, and IFNγ-inducible protein 10 (Dhindsa et al., 2021). Therefore, additional research efforts need to be made to investigate the complex relationships furtherly.

The major advantage of our study is the design taking the advantages of MR approach and used several sensitivity analyses to test the robustness of the MR findings. The application of MR analysis reduces the influence of confounding factors and reverse causality so that reliable causal estimations were obtained to complement the observational findings. The potential limitations of this study also need to be acknowledged. Our study may suffer from weak instrument bias, especially within sensitivity analyses that restricted to smaller sets of genetic instruments. In TSMR, this bias would tend to make estimates closer to the null. Since there is no available data on recovery status for COVID-19 patients in UK Biobank, the current study did not take recovery as a potential competing risk into account. We could not assess the sex-specific associations in IGF-1 and COVID-19 due to no data by sex in HGI. Moreover, the MR was merely based on individuals of European ancestry. Our findings might not be generalized to other populations. It should also be noted that the study findings are based on evidence from genetic data, additional large and prospective cohort studies with available IGF-1 data and information on COVID-19 susceptibility and clinical outcomes are needed to validate the findings.

In conclusion, our study indicated that genetically predicted high IGF-1 levels were associated with decrease the risk of COVID-19 susceptibility and hospitalization, but these associations did not survive the Bonferroni correction of multiple testing. Further studies are needed to validate the findings and explore whether IGF-1 could be a potential intervention target to reduce COVID-19 risk.

### Data availability statement

Data analyzed in the present study are GWAS summary statistics, which have been made publicly available. GWAS summary level data of COVID-19 HGI could be downloaded from https://www.covid19hg.org/results/. GWAS summary level data of sex hormones and IGF-1 in UK Biobank could be downloaded from GWAS catalog. All genome-wide significant SNPs have been provided in Supplementary file 1a–d. All analyses were performed using R statistical package freely available at https://cran.r-project.org/mirrors.html. The TSMR package is available at https://mrcieu.github.io/TwoSampleMR/(Hemani et al., 2020).
