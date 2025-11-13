# Gene–environment pathways to cognitive intelligence and psychotic-like experiences in children

## Authors

- Junghoon Park<sup>1</sup> ([ORCID: 0000-0001-8982-0387](https://orcid.org/0000-0001-8982-0387))
- Eunji Lee<sup>2</sup> ([ORCID: 0000-0002-2589-5395](https://orcid.org/0000-0002-2589-5395))
- Gyeongcheol Cho<sup>3</sup> ([ORCID: 0000-0002-9237-0388](https://orcid.org/0000-0002-9237-0388))
- Heungsun Hwang<sup>4</sup> ([ORCID: 0000-0002-5057-7479](https://orcid.org/0000-0002-5057-7479))
- Bo-Gyeom Kim<sup>2</sup> ([ORCID: 0000-0003-2685-877X](https://orcid.org/0000-0003-2685-877X))
- Gakyung Kim<sup>5</sup>
- Yoonjung Yoonie Joo<sup>2</sup> ([ORCID: 0000-0001-9506-8742](https://orcid.org/0000-0001-9506-8742)) †
- Jiook Cha<sup>1</sup> ([ORCID: 0000-0002-5314-7992](https://orcid.org/0000-0002-5314-7992)) †

### Affiliations

1. Interdisciplinary Program in Artificial Intelligence, College of Engineering, Seoul National University Seoul Republic of Korea ([ROR:04h9pn542](https://ror.org/04h9pn542))
2. Department of Psychology, College of Social Sciences, Seoul National University Seoul Republic of Korea ([ROR:04h9pn542](https://ror.org/04h9pn542))
3. Department of Psychology, College of Arts and Sciences, The Ohio State University Columbus United States ([ROR:00rs6vg23](https://ror.org/00rs6vg23))
4. Department of Psychology, McGill University Montréal Canada ([ROR:01pxwe438](https://ror.org/01pxwe438))
5. Department of Brain and Cognitive Sciences, College of Natural Sciences, Seoul National University Seoul Republic of Korea ([ROR:04h9pn542](https://ror.org/04h9pn542))
6. Department of Digital Health, Samsung Advanced Institute for Health Sciences & Technology (SAIHST), Sungkyunkwan University Seoul Republic of Korea ([ROR:04q78tk20](https://ror.org/04q78tk20))
7. Samsung Medical Center Seoul Republic of Korea ([ROR:05a15z872](https://ror.org/05a15z872))

† Corresponding author

## Abstract

In children, psychotic-like experiences (PLEs) are related to risk of psychosis, schizophrenia, and other mental disorders. Maladaptive cognitive functioning, influenced by genetic and environmental factors, is hypothesized to mediate the relationship between these factors and childhood PLEs. Using large-scale longitudinal data, we tested the relationships of genetic and environmental factors (such as familial and neighborhood environment) with cognitive intelligence and their relationships with current and future PLEs in children. We leveraged large-scale multimodal data of 6,602 children from the Adolescent Brain and Cognitive Development Study. Linear mixed model and a novel structural equation modeling (SEM) method that allows estimation of both components and factors were used to estimate the joint effects of cognitive phenotypes polygenic scores (PGSs), familial and neighborhood socioeconomic status (SES), and supportive environment on NIH Toolbox cognitive intelligence and PLEs. We adjusted for ethnicity (genetically defined), schizophrenia PGS, and additionally unobserved confounders (using computational confound modeling). Our findings indicate that lower cognitive intelligence and higher PLEs are significantly associated with lower PGSs for cognitive phenotypes, lower familial SES, lower neighborhood SES, and less supportive environments. Specifically, cognitive intelligence mediates the effects of these factors on PLEs, with supportive parenting and positive school environments showing the strongest impact on reducing PLEs. This study underscores the influence of genetic and environmental factors on PLEs through their effects on cognitive intelligence. Our findings have policy implications in that improving school and family environments and promoting local economic development may enhance cognitive and mental health in children.

## Introduction

Childhood is the critical developmental period in human life. Cognitive intelligence and mental health in this period significantly impact key life outcomes at later ages, including academic performance, economic productivity, physical health, intelligence, and psychopathology (Shonkoff, 2012; Walker et al., 2022). Literature shows the significant impact of social adversities on cognitive ability and mental health in early childhood. Lower family socioeconomic status (SES), particularly household income, is linked to lower neurocognitive ability and higher risk of psychopathology in childhood (Hair et al., 2015; Noble et al., 2015; Peverill et al., 2021; Tomasi and Volkow, 2021; Weissman et al., 2018).

Additional to family SES, the importance of neighborhood social environment on children’s neurocognitive ability has been also emphasized (Gard et al., 2021; Tooley et al., 2020). Adverse neighborhood environment, such as the percent of families below poverty line, low education levels, and exposure to violence, is associated with lower cognitive performance (CP) and a greater risk for psychosis in children (Butler et al., 2018; Karcher et al., 2021; Rakesh et al., 2021; Taylor et al., 2020). Conversely, as protective factors against familial and neighborhood socioeconomic challenges, supportive parenting (Brody et al., 2017; Brody et al., 2019; Holmes et al., 2018; Luby et al., 2012; Luby et al., 2016) and positive school environment (Gard et al., 2021; Piccolo et al., 2019; Rakesh et al., 2021) have been highlighted to improve child cognition and mental health.

Psychotic-like experiences (PLEs), which are prevalent in childhood, indicate the risk of psychosis (van der Steen et al., 2019; van Os and Reininghaus, 2016). Although they are not a direct precursor of schizophrenia, children reporting PLEs in ages of 9–11 years are at higher risk of psychotic disorders in adulthood (Kelleher and Cannon, 2011; Poulton et al., 2000). PLEs also point toward the potential for other psychopathologies including mood, anxiety, and substance disorders (van der Steen et al., 2019), are linked to deficits in cognitive intelligence (Cannon et al., 2002; Kelleher and Cannon, 2011) and show a stronger association with environmental risk factors during childhood than other internalizing/externalizing symptoms (Karcher et al., 2021).

Maladaptive cognitive intelligence may act as a mediator for the effects of genetic and environmental risks on the manifestation of psychotic symptoms (Cannon et al., 2000; Keefe et al., 2006; Reichenberg et al., 2005). Abnormal neurodevelopment, influenced by genetic factors, combined with disrupted cognitive processes resulting from socioenvironmental adversity, may eventually give rise to the positive symptoms of schizophrenia, relevant to PLEs (Garety et al., 2001; Howes and Murray, 2014). Family studies show a decline in cognitive intelligence preceding psychotic symptoms is related to genetic risk (Cosway et al., 2000; Curtis et al., 2001). In more recent studies, these associations have led to the model positing that cognitive intelligence mediates the genetic risk for psychopathology and PLEs (Karcher et al., 2022; Pat et al., 2022).

To minimize potential bias in the estimates of environmental effects, it is crucial to adjust for genetic confounding (Sariaslan et al., 2016), given the substantial genetic influence on intelligence (Bouchard and McGue, 1981; Deary et al., 2006; Plomin and Spinath, 2004) and PLEs (Bentall and Fernyhough, 2008; Maxwell et al., 2023). Recent advances in genetics have led to the development of the polygenic score (PGS) approach: a computational method to estimate the genetic loading for a complex trait using statistical associations of each single-nucleotide polymorphism (SNP) identified by genome-wide association studies (GWAS) (Cho et al., 2022). Particularly, PGS for two related but distinct phenotypes—CP and educational attainment (EA)—holds significant importance. As the two most frequently used proxies of cognitive intelligence in genetic studies, PGSs for CP and EA are positively correlated with intelligence, EA, income, self-rated health, and height (Judd et al., 2020; Lee et al., 2018; Okbay et al., 2022; Selzam et al., 2019). Furthermore, the PGS for EA is associated with a wide range of biological and social outcomes, including brain morphometry (Judd et al., 2020; Karcher et al., 2022), psychopathologies such as PLEs, autism, depression, Alzheimer’s disease, neuroticism (Karcher et al., 2022; Okbay et al., 2022), cognitive decline (Joo et al., 2022; Karcher et al., 2022; Ritchie et al., 2020), body mass index (BMI), time spent watching television, geographic residence (Abdellaoui et al., 2022), and wealth inequality (Barth et al., 2020). Similar to the terms used in prior research, we will collectively refer to these two PGSs of focus as ‘cognitive phenotypes PGSs’ throughout this paper (Joo et al., 2022; Okbay et al., 2022; Selzam et al., 2019). An important gap in the literature is the lack of integrated assessment of the effects of genetic and environmental factors at multiple levels (e.g., familial vs neighborhood) to dissect the genetic and environmental effects underlying abnormal cognitive intelligence and the PLEs. Addressing this with large multimodal data will allow for a more complete understanding of the factors related to the development of PLEs.

In this study, we systematically explore the longitudinal trajectories of genetic and environmental influences on PLEs, mediated through cognitive intelligence. Toward this goal, we firstly assess the associations of cognitive phenotype PGSs, family and neighborhood SES, and supportive environment with children’s cognitive intelligence and longitudinally measured PLEs. To maintain robustness of our assessment, we employed statistical and computational approaches to carefully consider potential confounding. We then test the mediating effect of cognitive intelligence on the relationship between genetic and environmental factors and PLEs. Our investigation traces these effects from the baseline and through the 1- and 2-year follow-ups, providing a nuanced understanding on the role of cognitive phenotype PGSs, family SES, neighborhood SES, and positive family and school environments in shaping PLEs in children aged 9–10 years.

## Materials and methods

### Study participants

We used the multimodal genetic and environmental data of 11,878 preadolescent children aged 9–10 years old collected from 21 research sites of the Adolescent Brain Cognitive Development (ABCD) Study, one of the largest longitudinal studies for children’s neurodevelopment in the United States. We analyzed the baseline, first year, and second year follow-up datasets included in ABCD Release 4.0, downloaded on January 25, 2022. After k-nearest neighbor imputation of missing values of covariates (categorical variables: sex, genetic ancestry, marital status of the caregiver, ABCD research sites; continuous variables: age, BMI, family history of psychiatric disorders; 4.67% of total observations imputed) using the R package VIM (Kowarik and Templ, 2016), we removed participants with missing data on study variables (missing genotype: N = 3260; follow-up observations: N = 1180; neighborhood information: N = 694; cognitive intelligence tests: N = 126; PLEs: N = 5; positive environment: N = 11). The final samples included 6602 multiethnic children, which comprised 890 of African ancestry (13.48%), 91 of East Asian ancestry (1.38%), 5211 of European ancestry (78.93%), 229 of Native American ancestry (3.47%), and 181 not specified (2.74%).

### Data

#### NIH toolbox CP

Children’s neurocognitive abilities were assessed using the NIH Toolbox Cognitive Battery, which has seven cognitive instruments for examining executive function, episodic memory, language abilities, processing speed, working memory, and attention (Thompson et al., 2019). We utilized baseline observations of uncorrected composite scores of fluid intelligence (Dimensional Change Card Sort Task, Flanker Test, Picture Sequence Memory Test, and List Sorting Working Memory Test), crystallized intelligence (Picture Vocabulary Task and Oral Reading Recognition Test), and total intelligence (all seven instruments) provided in the ABCD Study dataset.

### Psychotic-like experiences

Baseline and 1- and 2-year follow-up of PLEs were measured using the children’s responses to the Prodromal Questionnaire-Brief Child Version. In line with previous research (Karcher et al., 2018; Karcher et al., 2020; Karcher et al., 2021), we computed Total Score and Distress Score, each indicating the number of psychotic symptoms and levels of total distress. Considering self- and parent-reports of psychopathology may differ (Achenbach, 2006), we additionally used parent-rated PLEs derived from four items of the Child Behavior Checklist according to previous studies (Karcher et al., 2018; Karcher et al., 2020; Karcher et al., 2021). Self- and parent-reported PLEs had significant positive correlation (Pearson’s correlation of baseline year: r = 0.095–0.0989, p < 0.0001; 1-year follow-up: r = 0.1322–0.1327, p < 0.0001; 2-year follow-up: r = 0.1569–0.1632, p < 0.0001).

### Polygenic scores

To investigate the aggregated effect of genetic components, we estimated PGS of two representative cognitive phenotypes for each participant: EA and CP (Cho et al., 2022). We used the summary statistics released from a GWAS (Lee et al., 2018) of European-descent individuals for EA (n = 1,131,881) and CP (n = 257,841). EA was measured as the years of schooling; CP, measured as the respondent’s score on cognitive ability assessments of general cognitive function and verbal–numerical reasoning, was assessed in participants from the COGENT consortium and the UK Biobank. To construct PGS of schizophrenia for sensitivity analyses, we used the summary statistics from the multiple GWAS of European sample (n = 65,967; Ruderfer et al., 2018) and East Asian sample (n = 58,140; Lam et al., 2019). We applied PRS-CSx, a high-dimensional Bayesian regression framework that improves cross-population prediction via continuous shrinkage prior to SNP effect sizes (Ge et al., 2019) (for details, see Appendix 1). The two PGSs for cognitive phenotypes had a positive significant correlation (Pearson’s correlation: r = 0.4331, p < 0.0001).

### Family-, neighborhood-, and school-level environment

We assessed children’s family-level SES with family income, parental education, and family’s financial adversity based on parent self-reporting (Karcher et al., 2020; Taylor et al., 2020; Tomasi and Volkow, 2021). Higher family income and parental education and lower family’s financial adversity denote a higher family SES.

Neighborhood-level SES was assessed using the Area Deprivation Index (ADI), the percentage of individuals below −125% of the poverty level (henceforth ‘poverty’), and years of residence, which were associated with PLEs in prior research (Karcher et al., 2021). Higher values of ADI and poverty and fewer years of residence indicate a lower neighborhood SES.

Based on existing literature (Karcher et al., 2021; Rakesh et al., 2021), we measured the level of positive parenting behavior and positive school environment to assess the effect of positive family and school environment on each individual.

### Statistical modeling

In this study, we employ linear mixed models and a novel structural equation modeling (SEM) method to examine the longitudinal trajectories of genetic and environmental influences on PLEs mediated by cognitive intelligence. We specifically investigate the mediating role of cognitive intelligence within the impacts of cognitive phenotype PGSs, high family SES, low neighborhood SES, and positive family and school environments on PLEs. These influences are examined across three periods of PLEs observations: baseline, 1-year follow-up, and 2-year follow-up (Figure 1).

![Figure 1.](https://cdn.elifesciences.org/articles/88117/elife-88117-fig1-v2.jpg)

**Figure 1.:** This study examines the mediating role of cognitive intelligence within the effects of cognitive phenotype polygenic scores (PGSs), high family socioeconomic status (SES), low neighborhood SES, and positive family and school environments on PLEs observed at baseline, 1-year follow-up, and 2-year follow-up in children aged 9–10 years. Both direct and indirect effects, as well as total effects, were evaluated for statistical significance.

### Linear mixed models

Using linear mixed models to minimize potential population stratification from different household environments and geographical locations (Cho et al., 2022), we analyzed the genetic and environmental effects on cognitive intelligence and PLEs. Key variables of interest were PGS, family SES, neighborhood SES, and positive environment. To avoid multicollinearity, CP and EA PGSs were used separately in two other models. As a random factor, the variable indicating ABCD research sites was used. Variables within each model had no signs of multicollinearity (Fox and Monette, 1992) (generalized variance inflation factor <2.0 for every variable in all models). The child’s sex, age, genetic ancestry, BMI, marital status of the caregiver, and family history of psychiatric disorders were included as covariates in the model (Karcher et al., 2021). All continuous variables were standardized (z-scaled) beforehand to get standardized estimates, and the analyses were conducted with the lme4 package in R version 4.1.2. Throughout this paper, threshold for statistical significance was set at p < 0.05, with correction for multiple comparisons using the false discovery rate. 95% bootstrapped confidence intervals were obtained with 5000 iterations.

### Path modeling

To test the plausibility of whether cognitive intelligence may mediate the association between genetic and environmental factors and PLEs, we used an up-to-date SEM method, integrated generalized structured component analysis (IGSCA) (Hwang et al., 2021b). This approach is suited to our study using the multimodal genetic and environmental variables in that it estimates models with both factors and components as statistical proxies for the constructs.

Standard SEM using latent factors (i.e., indirectly measured indicators that explain the covariance among observed variables) to represent indicators such as PGS or family SES relies on the assumption that observed variables within each construct share a common underlying factor. If this assumption is violated, standard SEM cannot effectively control for estimation biases. The IGSCA method addresses this limitation by allowing for the use of composite indicators (i.e., components)—defined as a weighted sum of observed variables—as constructs in the model, more effectively controlling bias in estimation compared to the standard SEM. During estimation, the IGSCA determines weights of each observed variable in such a way as to maximize the variances of all endogenous indicators and components.

We assessed path-analytic relationships among the six key constructs: cognitive phenotypes PGSs, family SES, neighborhood SES, positive family and school environment, general intelligence, and PLEs. Considering that the observed variables of the PGSs, family SES, neighborhood SES, positive family and school environment, and PLEs are evaluated as a composite index by prior research, the IGSCA method can mitigate bias more effectively by representing these constructs as components. Notably, investigations carried out by Judd et al., 2020 and Martin et al., 2015 utilized composite indicators to examine the genetic influence on EA and Attention-Deficit/Hyperactivity Disorder. Moreover, socioenvironmental influences are often treated as composite indicators as highlighted in Judd et al., 2020. When considering the psychosis continuum, studies like that of van Os et al., 2009 postulate that psychotic disorders are likely underpinned by a multiplicity of background factors rather than a single common factor. This perspective is substantiated by a multitude of prior research that deploys composite indices for the measurement of psychotic symptoms. For these reasons, we statistically represented these constructs as the weighted sums of their observed variables or components (Cho et al., 2022). On the other hand, we represented general intelligence as a common factor that determines the underlying covariance pattern of fluid and crystallized intelligence, based on the classical g theory of intelligence (Jensen, 1998; Spearman, 1904).

The IGSCA model included the same covariates used in the linear mixed model as well as the ABCD research site as an additional covariate. We applied GSCA Pro 1.1 (Hwang et al., 2021a) to fit the IGSCA model to the data and checked the model’s goodness-of-fit index (GFI) (Jöreskog and Sörbom, 1986), standardized root mean square residual (SRMR), and total variance of all indicators and components explained (FIT) to assess its overall goodness-of-fit. Ranging from 0 to 1, a larger FIT value indicates more variance of all variables is explained by the specified model (e.g., FIT = 0.50 denotes that the model explains 50% of the total variance of all variables) (Hwang et al., 2021a). The rules-of-thumb cutoff criteria in IGSCA is GFI ≥0.93 and SRMR ≤0.08 for an acceptable fit (Cho et al., 2020). Finally, we conducted conditional process analyses to investigate further the indirect and total effects of the constructs in the model. As a trade-off for obtaining robust nonparametric estimates without distributional assumptions for normality, the IGSCA method does not return exact p values (Hwang et al., 2021b). As a reasonable alternative, we obtained 95% confidence intervals based on 5000 bootstrap samples to test the statistical significance of parameter estimates.

### Sensitivity analyses

To ensure robustness of the main analyses results, we conducted multiple sensitivity analyses. As the European-descent-based GWAS was used for constructing PGS, we reran the main analyses using participants of European ancestry (n = 5211) to adjust for ethnic confounding. Next, we tested effects of gene × environment interactions on cognitive intelligence and PLEs, respectively. We also tested the effects of cognitive phenotypes PGS adjusting for schizophrenia PGS, given the association of schizophrenia PGS and cognitive deficit in psychosis patients (Shafee et al., 2018) and individuals at-risk of psychosis (He et al., 2021). Lastly, we adjusted for unobserved confounding bias in the linear mixed model, using a recently developed framework for causal inference based on null treatments approach (Miao et al., 2023). Designed to discern causal effects from multiple treatment variables within non-randomized, observational data, the null treatments approach hinges on the assumption that no fewer than half of the confounded treatments exert no causal influence on the outcome. It circumvents the need for prior knowledge regarding which treatments are null and eliminates the necessity for independence among treatments. Given our model’s inclusion of numerous treatment variables with shared variances due to the presence of unobserved confounders (Abdellaoui et al., 2022; Okbay et al., 2022)—including cognitive phenotypes PGS, family and neighborhood SES, positive family and school environments— we opted to employ this method.

## Results

### Demographics

Table 1 presents the demographic characteristics of the final samples. For multiethnic subjects (main analyses, n = 6602), 47.15% were female, and the parents of 70.21% were married. In European ancestry samples (sensitivity analyses, n = 5211), 46.71% were female, and the parents of 77.47% were married. Children of European ancestry showed significantly different marital status (p < 0.0001), lower BMI (p < 0.0001), and family history of psychiatric disorders (p < 0.0001) compared to children of other genetic ancestries. Our linear mixed model and IGSCA analyses were adjusted using sex, age, marital status, BMI, family history of psychiatric disorders, and ABCD research sites as covariates.

**Table 1.**
 Demographic characteristics of the study participants.Of the initial 11,878 ABCD samples, we obtained data for the variables of interest for 6602 multiethnic children. For multiethnic subjects (main analyses, n = 6602), 47.15% were female, and the parents of 70.21% were married. In European ancestry samples (sensitivity analyses, n = 5211), 46.71% were female, and the parents of 77.47% were married. Children of European ancestry had significantly different marital status (p < 0.0001), lower body mass index (BMI; p < 0.0001), and higher family history of psychiatric disorders (p < 0.0001) than children of multiethnic ancestries. There were no significant differences in other characteristics between the two ancestry groups. The 6602 multiethnic participants consisted of 890 African-ancestry (13.48%), 229 Native American ancestry (3.47%), 91 East Asian ancestry (1.38%), 181 not specified (2.74%), and 5211 European ancestry (78.93%) children. Differences between genetic ancestry groups were calculated using χ2 tests for categorical variables and t-tests for continuous variables.


<table>
  <thead>
    <tr>
      <th>Demographic characteristics</th>
      <th></th>
      <th colspan="3">European ancestry (n = 5211)</th>
      <th colspan="3">Multiethnic (n = 6602)</th>
      <th colspan="2">Test statistics</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td>N</td>
      <td>Ratio (%)</td>
      <td>Mean (SD)</td>
      <td>N</td>
      <td>Ratio (%)</td>
      <td>Mean (SD)</td>
      <td>t(df)/χ2(df)</td>
      <td>p value</td>
    </tr>
    <tr>
      <td rowspan="2">Sex</td>
      <td>Male</td>
      <td>2777</td>
      <td>53.29</td>
      <td></td>
      <td>3489</td>
      <td>52.85</td>
      <td></td>
      <td rowspan="2">−0.4795 (11811)</td>
      <td rowspan="2">0.6316</td>
    </tr>
    <tr>
      <td>Female</td>
      <td>2434</td>
      <td>46.71</td>
      <td></td>
      <td>3113</td>
      <td>47.15</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="6">Marital status of the caregiver</td>
      <td>Married</td>
      <td>4037</td>
      <td>77.47</td>
      <td></td>
      <td>4635</td>
      <td>70.21</td>
      <td></td>
      <td rowspan="6">−10.2326 (11811)</td>
      <td rowspan="6">&lt;0.0001</td>
    </tr>
    <tr>
      <td>Widowed</td>
      <td>38</td>
      <td>0.73</td>
      <td></td>
      <td>50</td>
      <td>0.76</td>
      <td></td>
    </tr>
    <tr>
      <td>Divorced</td>
      <td>485</td>
      <td>9.31</td>
      <td></td>
      <td>610</td>
      <td>9.24</td>
      <td></td>
    </tr>
    <tr>
      <td>Separated</td>
      <td>155</td>
      <td>2.97</td>
      <td></td>
      <td>232</td>
      <td>3.51</td>
      <td></td>
    </tr>
    <tr>
      <td>Never married</td>
      <td>275</td>
      <td>5.28</td>
      <td></td>
      <td>718</td>
      <td>10.88</td>
      <td></td>
    </tr>
    <tr>
      <td>Living with partner</td>
      <td>221</td>
      <td>4.24</td>
      <td></td>
      <td>357</td>
      <td>5.41</td>
      <td></td>
    </tr>
    <tr>
      <td>Age(rounded to chronological month)</td>
      <td rowspan="3"></td>
      <td rowspan="3">5211</td>
      <td rowspan="3"></td>
      <td>118.99 (7.46)</td>
      <td rowspan="3">6602</td>
      <td rowspan="3"></td>
      <td>118.94 (7.41)</td>
      <td>0.3652 (11811)</td>
      <td>0.715</td>
    </tr>
    <tr>
      <td>BMI</td>
      <td>18.29 (3.67)</td>
      <td>18.72 (4.12)</td>
      <td>−5.8889 (11811)</td>
      <td>&lt;0.0001</td>
    </tr>
    <tr>
      <td>Family history of psychiatric disorders(proportion of first-degree relatives who experienced mental illness)</td>
      <td>0.10 (0.11)</td>
      <td>0.09 (0.11)</td>
      <td>4.4296 (11811)</td>
      <td>&lt;0.0001</td>
    </tr>
    <tr>
      <td rowspan="5">Genetic ancestry</td>
      <td>African</td>
      <td>-</td>
      <td></td>
      <td rowspan="5"></td>
      <td>890</td>
      <td>13.48</td>
      <td rowspan="5"></td>
      <td rowspan="5"></td>
      <td rowspan="5"></td>
    </tr>
    <tr>
      <td>Native American</td>
      <td>-</td>
      <td></td>
      <td>229</td>
      <td>3.47</td>
    </tr>
    <tr>
      <td>East Asian</td>
      <td>-</td>
      <td></td>
      <td>91</td>
      <td>1.38</td>
    </tr>
    <tr>
      <td>European</td>
      <td>5211</td>
      <td>100</td>
      <td>5211</td>
      <td>78.93</td>
    </tr>
    <tr>
      <td>Not specified</td>
      <td>-</td>
      <td></td>
      <td>181</td>
      <td>2.74</td>
    </tr>
  </tbody>
</table>

### Genetic influence on cognitive phenotypes correlates positively with intelligence and negatively with PLEs

As shown in Figure 2, higher PGSs of cognitive capacity phenotypes correlated significantly with higher intelligence (CP PGS: β = 0.1113–0.1793; EA PGS: β = 0.0699–0.1567). While CP PGS was associated only with lower baseline year Distress Score PLEs (β = −0.0323), EA PGS was associated with lower baseline year and follow-up PLEs of all measures (baseline: β = −0.0518 to −0.0519; 1 year: β = −0.0423 to −0.043; 2 years: β = −0.036 to −0.0463). No significant correlations were found between CP PGS and follow-up PLEs (p > 0.05). The effects of EA PGS were larger on baseline year PLEs than follow-up PLEs. The effect sizes of EA PGS on children’s PLEs were larger than those of CP PGS (EA PGS: β = −0.036 to −0.0519; CP PGS: β = −0.0323) (Supplementary file 1).

![Figure 2.](https://cdn.elifesciences.org/articles/88117/elife-88117-fig2-v2.jpg)

**Figure 2.:** Standardized coefficients of a linear mixed model with CP PGS (A, B) and EA PGS (C, D). The analyses included 6602 samples of multiethnicity. Cognitive intelligence and PLEs correlated with the PGSs, residential disadvantage, positive environment, and family SES in the opposite directions. Error bars indicate 95% bootstrapped confidence intervals with 5000 iterations. CP and EA denote cognitive performance and education attainment, respectively; PGS, polygenic scores; SES, socioeconomic status; PLEs, psychotic-like experiences; ADI, Area Deprivation Index; Poverty, percentage of individuals below −125% of the poverty level; Years, years of residence (*p-FDR <0.05).

### Family and neighborhood SES correlates positively with intelligence and negatively with PLEs

Parental education associated positively with all types of intelligence (β = 0.0699 to 0.1745) and negatively with baseline year Total and Distress Score PLEs (β = −0.0528 to −0.043), 1-year follow-up PLEs (β = −0.0538 to −0.0449), and 2-year follow-up PLEs (β = −0.0459 to −0.0389). Family income correlated positively with intelligence (β = 0.0723 to 0.1365) and negatively with 2-year follow-up parent-rated PLEs (β = −0.0503 to −0.0502). Family’s financial disadvantage correlated negatively with baseline year parent-rated PLEs (β = 0.0726–0.0728), 1-year follow-up PLEs of all types (β = 0.0307–0.0577), and 2-year follow-up PLEs of all types (β = 0.0461–0.0581).

The ADI correlated significantly negatively with all types of intelligence (β = −0.0684 to −0.054). Additionally, a higher ADI correlated significantly with higher baseline year PLEs (β = 0.0587–0.0914), 1-year follow-up PLEs (β = 0.0523–0.0613), and 2-year follow-up PLEs (β = 0.0397–0.0449).

We found no significant associations of poverty with any of the target variables (p > 0.05). Years of residence correlated significantly with crystallized intelligence (β = 0.035 to 0.0372) and baseline year Total Score PLEs (β = −0.029 to −0.0273) (Supplementary file 1).

### Positive family and school environments correlate positively with intelligence and negatively with the influence of PLEs

Positive parenting behaviors showed significant negative correlations with baseline year PLEs (β = −0.0702 to −0.0419), 1-year follow-up PLEs (β = −0.0588 to −0.0397), and 2-year follow-up PLEs (β = −0.0623 to −0.0356) (Figure 2). Positive school environment was associated positively with total intelligence (β = 0.0353 to 0.0397) and fluid intelligence (β = 0.0514 to 0.0545) and negatively with all three measures of baseline year PLEs (β = −0.1193 to −0.0468), 1-year follow-up PLEs (β = −0.1078 to −0.04), and 2-year follow-up PLEs (β = −0.1068 to −0.0586) (Supplementary file 1).

### SEM-IGSCA

The IGSCA model showed that intelligence mediated the effects of genes and environments on the risk for psychosis (PLEs) (Figure 3 and Table 2). Estimated factor loadings of latent factor variable and weights of component variables are presented in Supplementary file 1. Correlation matrices between component/factor variables are presented in Appendix 3—figure 1. The model showed a good model fit with a GFI of 0.9735, SRMR of 0.0359, and FIT value of 0.4912 (Cho et al., 2020). Intelligence was under significant direct influences of the cognitive phenotypes PGS (β = 0.2427), family SES (β = 0.2932), neighborhood SES (β = −0.1121), and positive environment (β = 0.0268). Family SES and positive environment had significant negative direct effects on PLEs of all years. Cognitive phenotypes PGS and neighborhood SES showed no significant direct effects on any of the PLEs (p > 0.05). Intelligence significantly mediated the effects of the PGS, family and neighborhood SES, and positive environment on PLEs of all years: the PGS (baseline year: β = −0.035; 1 year: β = −0.0355; 2 years: β = −0.0274), family SES (baseline year: β = −0.0423; 1 year: β = −0.0429; 2 years: β = −0.0331), neighborhood SES (baseline year: β = 0.0162; 1 year: β = 0.0164; 2 years: β = 0.0126), and positive environment (baseline year: β = −0.0039; 1 year: β = −0.0039; 2 years: β = −0.003).

![Figure 3.](https://cdn.elifesciences.org/articles/88117/elife-88117-fig3-v2.jpg)

**Figure 3.:** (A) Direct pathways from PGS, high family SES, low neighborhood SES, and positive environment to cognitive intelligence and PLEs. Standardized path coefficients are indicated on each path as direct effect estimates (significance level *p < 0.05). (B) Indirect pathways to PLEs via intelligence were significant for polygenic scores, high family SES, low neighborhood SES, and positive environment, indicating the significant mediating role of intelligence. (C) Relative effect sizes of direct and indirect pathways within the total effects on PLEs. The standardized effect sizes of direct pathways are colored within each bar. In (A–B), child sex, genetic ancestry, body mass index (BMI), marital status, family history of psychiatric disorders, and ABCD research sites were included as covariates. CP PGS and EA PGS denote polygenic scores of cognitive performance and education attainment, respectively; SES, socioeconomic status; PLEs, psychotic-like experiences; Crystallized and Fluid, crystallized and fluid intelligence; ADI, Area Deprivation Index; Poverty, percentage of individuals below −125% of the poverty level; Years, years of residence. Note: * indicates a statistically significant parameter estimate at α = 0.05.

**Table 2.**
 Integrated generalized structured component analysis (IGSCA) of multiethnic samples.Sex, age, genetic ancestry, body mass index (BMI), parental education, marital status of the caregiver, household income, and family’s financial adversity based on parents’ self-report, family history of psychiatric disorders, and ABCD research sites were included as covariates. Family socioeconomic status was included to confirm that the aassociations of polygenic score (PGS), neighborhood disadvantage, and positive environment are meaningful. SE and CI represent standard error and confidence intervals, respectively. Significant effects are marked with a star (*).


<table>
  <thead>
    <tr>
      <th colspan="7">Analysis of total/direct/indirect effects</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Effect type</td>
      <td>Paths</td>
      <td>Estimate</td>
      <td>SE</td>
      <td colspan="2">95% CI</td>
      <td>Significance</td>
    </tr>
    <tr>
      <td colspan="2">Effects from PGS to intelligence (baseline year)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Direct effect</td>
      <td>PGS → intelligence</td>
      <td>0.242736</td>
      <td>0.01277</td>
      <td>0.218202</td>
      <td>0.267954</td>
      <td>*</td>
    </tr>
    <tr>
      <td colspan="2">Effects from high family SES to intelligence (baseline year)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Direct effect</td>
      <td>High family SES → intelligence</td>
      <td>0.293171</td>
      <td>0.016737</td>
      <td>0.260337</td>
      <td>0.326413</td>
      <td>*</td>
    </tr>
    <tr>
      <td colspan="2">Effects from low neighborhood SES to intelligence (baseline year)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Direct effect</td>
      <td>Low neighborhood SES → intelligence</td>
      <td>−0.1121</td>
      <td>0.016768</td>
      <td>−0.14568</td>
      <td>−0.08118</td>
      <td>*</td>
    </tr>
    <tr>
      <td colspan="2">Effects from positive environment to intelligence (baseline year)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Direct effect</td>
      <td>Positive environment → intelligence</td>
      <td>0.026793</td>
      <td>0.012552</td>
      <td>0.003984</td>
      <td>0.052633</td>
      <td>*</td>
    </tr>
    <tr>
      <td colspan="2">Effects from intelligence to psychotic-like experiences (all years)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Direct effect</td>
      <td>Intelligence → psychotic-like experiences (baseline year)</td>
      <td>−0.14421</td>
      <td>0.027683</td>
      <td>−0.20344</td>
      <td>−0.09516</td>
      <td>*</td>
    </tr>
    <tr>
      <td>Direct effect</td>
      <td>Intelligence → psychotic-like experiences (1-year follow-up)</td>
      <td>−0.14638</td>
      <td>0.027507</td>
      <td>−0.20834</td>
      <td>−0.09983</td>
      <td>*</td>
    </tr>
    <tr>
      <td>Direct effect</td>
      <td>Intelligence → psychotic-like experiences (2-year follow-up)</td>
      <td>−0.11276</td>
      <td>0.028708</td>
      <td>−0.17428</td>
      <td>−0.063</td>
      <td>*</td>
    </tr>
    <tr>
      <td colspan="2">Effects from PGS to psychotic-like experiences (baseline year)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Total effect</td>
      <td>PGS → psychotic-like experiences</td>
      <td>−0.05017</td>
      <td>0.011354</td>
      <td>−0.07292</td>
      <td>−0.02853</td>
      <td>*</td>
    </tr>
    <tr>
      <td>Indirect effect</td>
      <td>PGS → intelligence → psychotic-like experiences</td>
      <td>−0.035</td>
      <td>0.007126</td>
      <td>−0.0508</td>
      <td>−0.02273</td>
      <td>*</td>
    </tr>
    <tr>
      <td>Direct effect</td>
      <td>PGS → psychotic-like experiences</td>
      <td>−0.01516</td>
      <td>0.01347</td>
      <td>−0.04085</td>
      <td>0.012389</td>
      <td></td>
    </tr>
    <tr>
      <td colspan="2">7 Effects from high family SES to psychotic-like experiences (baseline year)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Total effect</td>
      <td>High family SES → psychotic-like experiences</td>
      <td>−0.12126</td>
      <td>0.019087</td>
      <td>−0.15851</td>
      <td>−0.08313</td>
      <td>*</td>
    </tr>
    <tr>
      <td>Indirect effect</td>
      <td>High family SES → intelligence → psychotic-like experiences</td>
      <td>−0.04228</td>
      <td>0.008652</td>
      <td>−0.06139</td>
      <td>−0.02707</td>
      <td>*</td>
    </tr>
    <tr>
      <td>Direct effect</td>
      <td>High family SES → psychotic-like experiences</td>
      <td>−0.07898</td>
      <td>0.020747</td>
      <td>−0.11856</td>
      <td>−0.03698</td>
      <td>*</td>
    </tr>
    <tr>
      <td colspan="2">Effects from low neighborhood SES to psychotic-like experiences (baseline year)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Total effect</td>
      <td>Low neighborhood SES → psychotic-like experiences</td>
      <td>0.050374</td>
      <td>0.018277</td>
      <td>0.013545</td>
      <td>0.085934</td>
      <td>*</td>
    </tr>
    <tr>
      <td>Indirect effect</td>
      <td>Low neighborhood SES → intelligence → psychotic-like experiences</td>
      <td>0.016166</td>
      <td>0.003944</td>
      <td>0.009843</td>
      <td>0.025298</td>
      <td>*</td>
    </tr>
    <tr>
      <td>Direct effect</td>
      <td>Low neighborhood SES → psychotic-like experiences</td>
      <td>0.034209</td>
      <td>0.0184</td>
      <td>−0.00268</td>
      <td>0.069813</td>
      <td></td>
    </tr>
    <tr>
      <td colspan="2">Effects from positive environment to psychotic-like experiences (baseline year)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Total effect</td>
      <td>Positive environment → psychotic-like experiences</td>
      <td>−0.15256</td>
      <td>0.013871</td>
      <td>−0.17965</td>
      <td>−0.1252</td>
      <td>*</td>
    </tr>
    <tr>
      <td>Indirect effect</td>
      <td>Positive environment → intelligence → psychotic-like experiences</td>
      <td>−0.00386</td>
      <td>0.002065</td>
      <td>−0.00859</td>
      <td>−0.00058</td>
      <td>*</td>
    </tr>
    <tr>
      <td>Direct effect</td>
      <td>Positive environment → psychotic-like experiences</td>
      <td>−0.14869</td>
      <td>0.014025</td>
      <td>−0.17573</td>
      <td>−0.12073</td>
      <td>*</td>
    </tr>
    <tr>
      <td colspan="2">Effects from PGS to psychotic-like experiences (1-year follow-up)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Total effect</td>
      <td>PGS → psychotic-like experiences</td>
      <td>−0.035895</td>
      <td>0.011646</td>
      <td>−0.058499</td>
      <td>−0.013458</td>
      <td>*</td>
    </tr>
    <tr>
      <td>Indirect effect</td>
      <td>PGS → intelligence → psychotic-like experiences</td>
      <td>−0.03553</td>
      <td>0.007062</td>
      <td>−0.05176</td>
      <td>−0.02376</td>
      <td>*</td>
    </tr>
    <tr>
      <td>Direct effect</td>
      <td>PGS → psychotic-like experiences</td>
      <td>−0.00036</td>
      <td>0.013579</td>
      <td>−0.02566</td>
      <td>0.028107</td>
      <td></td>
    </tr>
    <tr>
      <td colspan="2">Effects from high family SES to psychotic-like experiences (1-year follow-up)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Total effect</td>
      <td>High family SES → psychotic-like experiences</td>
      <td>−0.11184</td>
      <td>0.018291</td>
      <td>−0.1478</td>
      <td>−0.07584</td>
      <td>*</td>
    </tr>
    <tr>
      <td>Indirect effect</td>
      <td>High family SES → intelligence → psychotic-like experiences</td>
      <td>−0.04291</td>
      <td>0.008569</td>
      <td>−0.06242</td>
      <td>−0.0288</td>
      <td>*</td>
    </tr>
    <tr>
      <td>Direct effect</td>
      <td>High family SES → psychotic-like experiences</td>
      <td>−0.06892</td>
      <td>0.019586</td>
      <td>−0.10522</td>
      <td>−0.02866</td>
      <td>*</td>
    </tr>
    <tr>
      <td colspan="2">Effects from low neighborhood SES to psychotic-like experiences (1-year follow-up)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Total effect</td>
      <td>Low neighborhood SES → psychotic-like experiences</td>
      <td>0.032947</td>
      <td>0.018055</td>
      <td>−0.00264</td>
      <td>0.068773</td>
      <td></td>
    </tr>
    <tr>
      <td>Indirect effect</td>
      <td>Low neighborhood SES → intelligence → psychotic-like experiences</td>
      <td>0.016409</td>
      <td>0.004003</td>
      <td>0.010133</td>
      <td>0.025893</td>
      <td>*</td>
    </tr>
    <tr>
      <td>Direct effect</td>
      <td>Low neighborhood SES → psychotic-like experiences</td>
      <td>0.016538</td>
      <td>0.018503</td>
      <td>−0.02066</td>
      <td>0.051855</td>
      <td></td>
    </tr>
    <tr>
      <td colspan="2">Effects from positive environment to psychotic-like experiences (1-year follow-up)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Total effect</td>
      <td>Positive environment → psychotic-like experiences</td>
      <td>−0.13149</td>
      <td>0.013154</td>
      <td>−0.15756</td>
      <td>−0.10589</td>
      <td>*</td>
    </tr>
    <tr>
      <td>Indirect effect</td>
      <td>Positive environment → intelligence → psychotic-like experiences</td>
      <td>−0.00392</td>
      <td>0.00208</td>
      <td>−0.0087</td>
      <td>−0.00059</td>
      <td>*</td>
    </tr>
    <tr>
      <td>Direct effect</td>
      <td>Positive environment → psychotic-like experiences</td>
      <td>−0.12757</td>
      <td>0.013237</td>
      <td>−0.15343</td>
      <td>−0.10137</td>
      <td>*</td>
    </tr>
    <tr>
      <td colspan="2">Effects from PGS to psychotic-like experiences (2-year follow-up)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Total effect</td>
      <td>PGS → psychotic-like experiences</td>
      <td>−0.03643</td>
      <td>0.012196</td>
      <td>−0.06027</td>
      <td>−0.01272</td>
      <td>*</td>
    </tr>
    <tr>
      <td>Indirect effect</td>
      <td>PGS → intelligence → psychotic-like experiences</td>
      <td>−0.02737</td>
      <td>0.007142</td>
      <td>−0.04307</td>
      <td>−0.01508</td>
      <td>*</td>
    </tr>
    <tr>
      <td>Direct effect</td>
      <td>PGS → psychotic-like experiences</td>
      <td>−0.00906</td>
      <td>0.014737</td>
      <td>−0.03696</td>
      <td>0.021152</td>
      <td></td>
    </tr>
    <tr>
      <td colspan="2">Effects from high family SES to psychotic-like experiences (2-year follow-up)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Total effect</td>
      <td>High family SES → psychotic-like experiences</td>
      <td>−0.11632</td>
      <td>0.018067</td>
      <td>−0.15258</td>
      <td>−0.08174</td>
      <td>*</td>
    </tr>
    <tr>
      <td>Indirect effect</td>
      <td>High family SES → intelligence → psychotic-like experiences</td>
      <td>−0.03306</td>
      <td>0.008796</td>
      <td>−0.05228</td>
      <td>−0.01807</td>
      <td>*</td>
    </tr>
    <tr>
      <td>Direct effect</td>
      <td>High family SES → psychotic-like experiences</td>
      <td>−0.08326</td>
      <td>0.019462</td>
      <td>−0.12066</td>
      <td>−0.04392</td>
      <td>*</td>
    </tr>
    <tr>
      <td colspan="2">Effects from low neighborhood SES to psychotic-like experiences (2-year follow-up)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Total effect</td>
      <td>Low neighborhood SES → psychotic-like experiences</td>
      <td>0.01921</td>
      <td>0.018684</td>
      <td>−0.01767</td>
      <td>0.055261</td>
      <td></td>
    </tr>
    <tr>
      <td>Indirect effect</td>
      <td>Low neighborhood SES → intelligence → psychotic-like experiences</td>
      <td>0.012641</td>
      <td>0.003814</td>
      <td>0.006533</td>
      <td>0.0215</td>
      <td>*</td>
    </tr>
    <tr>
      <td>Direct effect</td>
      <td>Low neighborhood SES → psychotic-like experiences</td>
      <td>0.006569</td>
      <td>0.019176</td>
      <td>−0.03173</td>
      <td>0.042823</td>
      <td></td>
    </tr>
    <tr>
      <td colspan="2">Effects from positive environment to psychotic-like experiences (2-year follow-up)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Total effect</td>
      <td>Positive environment → psychotic-like experiences</td>
      <td>−0.13627</td>
      <td>0.013881</td>
      <td>−0.1635</td>
      <td>−0.10926</td>
      <td>*</td>
    </tr>
    <tr>
      <td>Indirect effect</td>
      <td>Positive environment → intelligence → psychotic-like experiences</td>
      <td>−0.00302</td>
      <td>0.001703</td>
      <td>−0.0069</td>
      <td>−0.00043</td>
      <td>*</td>
    </tr>
    <tr>
      <td>Direct effect</td>
      <td>Positive environment → psychotic-like experiences</td>
      <td>−0.13325</td>
      <td>0.014009</td>
      <td>−0.16069</td>
      <td>−0.10565</td>
      <td>*</td>
    </tr>
  </tbody>
</table>

For all observed years, positive environment had largest total effects on PLEs (baseline year: β = −0.152; 1 year: β = −0.1316; 2 years: β = −0.1364), followed by family SES (baseline year: β = −0.1216; 1 year: β = −0.1119; 2 years: β = −0.1164), neighborhood SES (baseline year: β = 0.0504; 1 year: β = 0.0329; 2 years: β = 0.0192), and PGS (baseline year: β = −0.0498; 1 year: β = −0.036; 2 years: β = −0.0365). The total effects of each indicator on PLEs were significant except for those of neighborhood SES (p > 0.05).

### Sensitivity analyses

As sensitivity analyses, we reran our main analyses with adjustment for ethnic confounding, schizophrenia PGS, and unobserved confounding, respectively. Results of linear mixed model and IGSCA analyses were consistent (Supplementary file 1). See Appendix 2 for detailed results.

## Discussion

This study investigated the relationships of the genetic and environmental influences on the development of intelligence and the PLEs in youth, leveraging genetic data from the large epidemiological samples and a multi-level environmental (socioeconomic) data. Our results support the model that genetic factors (PGS for cognitive phenotypes), socioeconomic conditions, and family and school environments may influence cognitive intelligence in children, and this impact may lead to the individual variability of the current and future PLEs in children. Our analysis with integrated data shows the contributions of genetic and environmental factors, respectively, to cognitive and mental wellness in children, and further provides policy implications to improve them.

Our SEM shows that cognitive intelligence mediates the environmental and genetic influence on the current and future PLEs. The environmental factors (family SES, neighborhood SES, and positive parenting and schooling) and PGS of cognitive phenotypes exhibit significant indirect effects via cognitive intelligence on PLEs. Prior research identifying the mediation of cognitive intelligence focused on either genetic (Karcher et al., 2022) or environmental factors (Lewis et al., 2020) alone. Studies with older clinical samples have shown that cognitive deficit may be a precursor for the onset of psychotic disorders (Eastvold et al., 2007; Fett et al., 2020; Vorstman et al., 2015). Our study advances this by demonstrating the integrated effects of genetic and environmental factors on PLEs through the cognitive intelligence in 9- to 11-year-old children. Such comprehensive analysis contributes to assessing the relative importance of various factors influencing children’s cognition and mental health, and it can aid future studies designed for identifying health policy implications. Considering the directions and magnitudes of the effects, though the effects of PGS remain significant, aggregated effects of environmental factors account for much greater degrees on PLEs.

Our results of cognitive intelligence mediating the genetic and environmental effects on PLEs may be related to several potential mechanisms. Children raised in higher family SES may have sufficient nutrition and cognitive stimulants, whereas children living in deprived neighborhoods may be exposed to higher rates of crime, air pollution, and substance abuse (Lewis et al., 2020; Marshall et al., 2020; Taylor et al., 2020; Tomasi and Volkow, 2021). Environmental enrichment may be associated with longer periods of neural plasticity (e.g., myelination, maturation of brain circuitry), leading to higher cognitive ability and lower risk of mental disorders like PLEs (Tooley et al., 2021). This may be further linked to the cognitive reserve theory. The theory suggests that genetic influence for cognitive phenotypes and environmental enrichment promotes more efficient, flexible brain networks, which may lead to greater resilience against psychopathology (Stern, 2009). Indeed, prior clinical studies show the linkage between cognitive reserve and psychosis (Amoretti et al., 2018; Leeson et al., 2011).

Our results indicate that genetic influences on cognitive phenotypes are significantly linked to PLEs. PGSs for CP and EA were strongly correlated with PLEs (baseline year, 1-year follow-up, and 2-year follow-up). These associations were robust after adjustment for schizophrenia PGS, ethnic confounding and unobserved confounders. Cognitive phenotypes PGS generally show higher predictive performance than PGS of any other traits (Lee et al., 2018; Okbay et al., 2022; Plomin and von Stumm, 2018). Genetic variants associated with CP and EA are related to complex traits across the life span, including neuroticism, depressive symptoms, smoking in adulthood, cognitive decline at a later age (Joo et al., 2022), risk for Alzheimer’s disease (Lee et al., 2018; Okbay et al., 2022), brain volume, area, and thickness, as well as psychotic disorders (Karcher et al., 2022). Prior gene expression studies suggest that polygenic signals for schizophrenia, bipolar disorder, and EA are significantly enriched in the central nervous system, particularly the cerebellum (Finucane et al., 2018). Our findings emphasize the importance of cognitive phenotypes PGS as a biomarker which not only implicates cognitive traits but also exhibits genetic overlap with the PLEs.

The differing magnitudes of the PGS impact between EA and CP warrant attention. The effects of the EA PGS on the PLEs of all years were 160.68–371.67% larger than those of CP PGS. This discrepancy may result from that the larger sample size of EA GWAS than that of CP GWAS. Alternatively, the discrepancies in effect sizes may suggest different genetic compositions between EA and CP. Recent literature documents that more than half of the polygenic signal for EA is related to noncognitive and social skills required for successful EA (Demange et al., 2021), whereas CP may rather be linked to cognitive skills. This observation also supports the well-established relationships of the EA PGS with socioeconomic and life-course outcomes (e.g., social mobility Belsky et al., 2018), voter turnout (Aarøe et al., 2021), BMI, income, time spent watching television, geographic residence (Abdellaoui et al., 2022), and wealth inequality (Barth et al., 2020), which may be influenced by unobserved environmental factors (Young et al., 2019). In our analysis, the utilization of two PGSs a more comprehensive evaluation, contributing to an estimation of the genetic and environmental factors that attempted to minimize confounding bias.

Furthermore, the significant effects of cognitive phenotypes PGS on cognitive intelligence (β = 0.0699–0.1793) remained robust and similar in magnitude after adjusting for genetic ancestry (β = 0.0754–0.1866) and other (unobserved) confounding (β = 0.0546–0.1776). As we controlled for family-, neighborhood-, and school-level environmental factors and unobserved confounders, our results may be interpreted as significant genetic influences on individual’s cognitive intelligence. This interpretation is supported by a recent study (Isungset et al., 2022): Despite of the socioeconomic differences in Norway (a typical social democratic welfare state) and the United States (a typical liberal welfare state), the magnitudes of genetic influence on cognitive intelligence were similar (Norway: β = 0.18; United States: β = 0.17). Cognitive phenotypes PGS is an important genetic factor across the nations and societies. Therefore, analyses omitting the genetic influence may be subject to overestimation of the socioeconomic impact (Plomin and von Stumm, 2018; Sariaslan et al., 2016).

This study shows that a high SES and positive environment, particularly positive parenting behavior and school environment, is associated with higher intelligence and a lower risk for PLEs in children. While prior research has emphasized the dominant role of family SES (e.g., family income) (Tomasi and Volkow, 2021), our SEM analyses (IGSCA) showed that positive environmental factors such as supportive parenting and schooling have a greater impact on children’s PLEs. Specifically, the effect sizes were the highest in supportive family and school environment, followed by family and neighborhood SES. Even after adjusting for genetic ancestry and unobserved confounders, the strong associations of positive parenting and schooling with higher intelligence and fewer PLEs remained significant. These findings suggest that interventions that target positive family and school environments may be particularly effective. Recent research supports this notion, showing that interventions that promote supportive parenting and inclusive school environments can improve neurocognitive ability, academic performance, and decrease risk behaviors such as drinking and emotional eating (Brody et al., 2017; Brody et al., 2019; Holmes et al., 2018).

Moreover, our results showed that positive parenting and schooling in baseline year were associated not only with baseline year PLEs but also with PLEs 1–2 years later. This is in line with prior research showing that intervention focused on parenting behavior and school environment have long-lasting positive effects that extend into adulthood and even across generations (Cunha and Heckman, 2007; Hill et al., 2020).

While policy implications in observational studies like ours might be limited, our findings show the importance of comprehensive approaches considering the entire ecosystem of children’s lives—including residential, family, and school environment—for future research aimed to enhance children’s intelligence and mental health. When we combine the total effect sizes of neighborhood and family SES, as well as positive school environment and parenting behavior $(\sum|\beta|=0.2718∼0.3242)$ , they considerably surpass the total effect sizes of cognitive phenotypes PGSs $(|\beta|=0.0359∼0.0502)$. It has been suggested that a holistic and quantitative approach that takes into account the comprehensive ecosystem of family, school, and residential environments may ensure policy effects and efficient use of resources (Cree et al., 2018; Garner et al., 2021; Shonkoff, 2012). For example, the Health Impact in 5 Years Initiative of the US Centers for Disease Control and Prevention (CDC, 2018) includes 14 evidence-based interventions, such as providing school-based prevention programs, public transportation, home improvement loans, and earned income tax credits, to tackle the social determinants of public health. Our study strengthens the idea that an interdisciplinary science-driven, coordinated approach to intervening in the select environmental factors may allow practical improvements in child development, particularly in those who are at a disadvantage.

Our study has some limitations. First, due to data availability constraints in the ABCD Study, we only utilized baseline observations for NIH Toolbox cognitive intelligence, and we could not test whether PLEs might be a mediator of intelligence. Second, the generalizability of our findings may be limited since most of the participants included in our analysis are from European ancestry. Although the ABCD Study aimed to achieve its representativeness by recruiting from an array of school systems located around each of the 21 research sites, chosen for their diversity in geography, demographics, and SES, it is not fully representative of the US population (Compton et al., 2019). Third, the duration of the follow-up period utilized in this study is relatively short (1- and 2-year follow-up), which may limit the interpretability of our findings for understanding cognitive and psychiatric development during later childhood. Future research could potentially benefit from employing longer follow-up periods, as more follow-up observations are being collected in the ABCD Study. Fourth, while we used a wide range of statistical methods to adjust for confounding bias from observed and unobserved variables (e.g., genetic ancestry), we did not account for other types of potential bias such as sample selection bias. Fifth, despite a number of causal inference methods used in this study, the ABCD Study is a non-randomized dataset. Given the observational nature of the ABCD Study, interpreting our results as actual causality requires more caution. Finally, we did not include all important environmental variables, such as air pollution (Marshall et al., 2020) and social capital (Krabbendam and van Os, 2005), which are not collected in the ABCD Study.

In conclusion, our study provides potential pathways of genetic factors of cognitive phenotypes and environmental factors of family, school, and neighborhood to cognitive and mental wellness in children. Our findings underscore the importance of a comprehensive approach that considers both biological and socioeconomic features in promoting young children’s cognitive ability and mental health. Given the importance of child development, it requires joint efforts from multiple disciplines.
