# External validation of postnatal gestational age estimation using newborn metabolic profiles in Matlab, Bangladesh

## Authors

- Malia SQ Murphy<sup>1</sup> ([ORCID: 0000-0002-4566-4957](https://orcid.org/0000-0002-4566-4957))
- Steven Hawken<sup>1</sup> ([ORCID: 0000-0002-3341-9022](https://orcid.org/0000-0002-3341-9022))
- Wei Cheng<sup>1</sup> ([ORCID: 0000-0002-1475-4079](https://orcid.org/0000-0002-1475-4079))
- Lindsay A Wilson<sup>1</sup> ([ORCID: 0000-0002-9910-3338](https://orcid.org/0000-0002-9910-3338))
- Monica Lamoureux<sup>3</sup>
- Matthew Henderson<sup>3</sup>
- Jesmin Pervin<sup>4</sup>
- Azad Chowdhury<sup>5</sup>
- Courtney Gravett<sup>6</sup>
- Eve Lackritz<sup>6</sup>
- Beth K Potter<sup>2</sup>
- Mark Walker<sup>1</sup>
- Julian Little<sup>2</sup>
- Anisur Rahman<sup>4</sup>
- Pranesh Chakraborty<sup>3</sup>
- Kumanan Wilson<sup>1</sup> ([ORCID: 0000-0002-1741-7705](https://orcid.org/0000-0002-1741-7705)) †

### Affiliations

1. Clinical Epidemiology Program Ottawa Hospital Research Institute Ottawa Canada
2. Department of Epidemiology and Community Health University of Ottawa Ottawa Canada
3. Newborn Screening Ontario Children’s Hospital of Eastern Ontario Ottawa Canada
4. International Centre for Diarrhoeal Disease Research Dhaka Bangladesh
5. Dhaka Shishu (Children) Hospital Dhaka Bangladesh
6. Global Alliance to Prevent Prematurity and Stillbirth Lynnwood United Stares

† Corresponding author

## Abstract

This study sought to evaluate the performance of metabolic gestational age estimation models developed in Ontario, Canada in infants born in Bangladesh. Cord and heel prick blood spots were collected in Bangladesh and analyzed at a newborn screening facility in Ottawa, Canada. Algorithm-derived estimates of gestational age and preterm birth were compared to ultrasound-validated estimates. 1036 cord blood and 487 heel prick samples were collected from 1069 unique newborns. The majority of samples (93.2% of heel prick and 89.9% of cord blood) were collected from term infants. When applied to heel prick data, algorithms correctly estimated gestational age to within an average deviation of 1 week overall (root mean square error = 1.07 weeks). Metabolic gestational age estimation provides accurate population-level estimates of gestational age in this data set. Models were effective on data obtained from both heel prick and cord blood, the latter being a more feasible option in low-resource settings.

## Introduction

Complications related to preterm birth are the leading cause of death among children under 5 years of age (March of Dimes, 2012). Estimating the burden of preterm birth in low-resource settings is challenging due to the absence of ultrasound technology and the unreliability of recall of last menstrual period. Commonly used estimates obtained late in gestation or postnatally (e.g. fundal height, and Ballard or Dubowitz scores) are subject to high inter-user variability and poor reliability in small for gestational age and preterm infants (Taylor et al., 2010; Spinnato et al., 1984; Robillard et al., 1992). In addition, data on preterm birth are not routinely documented in some countries and may not be classified according to international standards (Quinn et al., 2016), thus impeding the development of strategies for resource allocation to support global and local health initiatives. Strengthened data surveillance systems to more accurately assess and track changes in preterm birth across jurisdictions are urgently required (March of Dimes, 2012).

Algorithms based on newborn metabolic profiles in combination with clinical covariates such as sex and birthweight have demonstrated the potential to accurately categorize infants across preterm birth categories in high-resource settings (Jelliffe-Pawlowski et al., 2016; Ryckman et al., 2016; Wilson et al., 2016). Data from newborn screening programs in North America have been used to create models capable of estimating gestational age to within 1–2 weeks, but their performance among other infant populations is uncertain. Recent work has focused on refining these models and tailoring them for use across a range of environments and sub-populations, and has suggested that while the models perform well among infants from a variety of backgrounds, ethnicity-specific models may improve the models’ performance (Wilson et al., 2017; Hawken et al., 2017). More recent model iterations have been strenthened by the addition of variables such as newborn hemoglobin peak percentages (calculated from the ratio of fetal to adult hemoglobin levels), which have demonstrated strong associations with gestational age (Wilson et al., 2017). While these algorithms have the potential to provide reliable population estimates of preterm birth burden where prenatal ultrasound data are not available, the models’ generalizability to all infant populations, as well as the feasibility of collecting samples for analysis in low-resource settings, is uncertain. In this paper, we explore the performance of gestational age estimation models in an infant population born in Matlab, Bangladesh. We also comment on the effect of timing of sample collection on newborn metabolic profiles and the feasibility of newborn blood sample collection and analysis in this setting.

### Patient characteristics

One cord blood sample was excluded because 100% of analyte values were missing. Imputation was conducted for the remaining samples missing analyte values (n = 28 heel samples and 21 cord samples; no individual sample had more than 5/47 (11%) analyte values missing). The final cohort consisted of 1523 samples from 1069 unique individual newborns. 1036 samples were collected immediately after birth (range: 0 min - 2 hr 1 min) from the umbilical cord, and 487 heel prick samples were collected an average of 14 hr 58 min after birth (range: 25 min - 40 hr 30 min). The majority of samples received (93.2% of heel prick samples; 89.9% of cord blood samples) were from term infants (gestational age ≥37 weeks). 18.1% of heel prick samples and 15.9% of cord blood samples were derived from infants with a birthweight <2500 g. Of the 1069 infants included in the study, 454 contributed both heel and cord blood samples. A summary of participant demographics is provided in Table 1.

**Table 1.**
 Characteristics of infants and samples obtained from them.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Heel samples (n = 487)</th>
      <th>Cord samples (n = 1036)</th>
      <th>Paired heel and cord samples (n = 454 pairs)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Completeness of analyte data†, n (%)</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>No missing analytes</td>
      <td>459 (94.3%)</td>
      <td>1015 (98.0%)</td>
      <td>427 (94.1%)</td>
    </tr>
    <tr>
      <td>≥1 analyte missing, missing values imputed</td>
      <td>28 (5.7%)</td>
      <td>21 (2.0%)</td>
      <td>27 (5.9%)</td>
    </tr>
    <tr>
      <td>Sex, n (%)</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Male</td>
      <td>246 (50.5%)</td>
      <td>538 (51.9%)</td>
      <td>234 (51.5%)</td>
    </tr>
    <tr>
      <td>Female</td>
      <td>241 (49.5%)</td>
      <td>498 (48.1%)</td>
      <td>220 (48.5%)</td>
    </tr>
    <tr>
      <td>Gestational Age (wks), overall mean (SD)</td>
      <td>39.1 ± 1.5</td>
      <td>39.0 ± 1.7</td>
      <td>39.2 ± 1.4</td>
    </tr>
    <tr>
      <td>Gestational Age Category (wksdays), n (%)</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>≥37 weeks</td>
      <td>454 (93.2%)</td>
      <td>931 (89.9%)</td>
      <td>425 (93.6%)</td>
    </tr>
    <tr>
      <td>320-366 weeks</td>
      <td>32 (6.6%)</td>
      <td>102 (9.8%)</td>
      <td>29 (6.4%)</td>
    </tr>
    <tr>
      <td>&lt;320 weeks</td>
      <td>1 (0.2%)</td>
      <td>3 (0.3%)</td>
      <td>0 (0.0%)</td>
    </tr>
    <tr>
      <td>Birth Weight (g), mean (SD)</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Overall</td>
      <td>2837.8 ± 433.7</td>
      <td>2862.1 ± 445.9</td>
      <td>2846.8 ± 414.0</td>
    </tr>
    <tr>
      <td>Term infants only</td>
      <td>2879.5 ± 392.9</td>
      <td>2916.5 ± 401.7</td>
      <td>2879.2 ± 389.9</td>
    </tr>
    <tr>
      <td>Preterm infants only</td>
      <td>2264.2 ± 554.8</td>
      <td>2380.3 ± 524.5</td>
      <td>2372.1 ± 470.4</td>
    </tr>
    <tr>
      <td>Birth Weight Category, n (%)</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>≥4000 g</td>
      <td>3 (0.6%)</td>
      <td>15 (1.5%)</td>
      <td>3 (0.7%)</td>
    </tr>
    <tr>
      <td>2500 g to &lt; 4000 g</td>
      <td>396 (81.3%)</td>
      <td>856 (82.6%)</td>
      <td>374 (82.4%)</td>
    </tr>
    <tr>
      <td>1500 g to &lt; 2500 g</td>
      <td>84 (17.3%)</td>
      <td>158 (15.2%)</td>
      <td>75 (16.5%)</td>
    </tr>
    <tr>
      <td>1000 g to &lt; 1500 g</td>
      <td>4 (0.8%)</td>
      <td>4 (0.4%)</td>
      <td>2 (0.4%)</td>
    </tr>
    <tr>
      <td>&lt;1000 g</td>
      <td>0 (0.0%)</td>
      <td>3 (0.3%)</td>
      <td>0 (0.0%)</td>
    </tr>
    <tr>
      <td>Multiple Birth, n (%)</td>
      <td>7 (1.4%)</td>
      <td>19 (1.8%)</td>
      <td>8 (1.8%)</td>
    </tr>
    <tr>
      <td>Newborn age at sample collection (hrs), mean (SD)</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Overall</td>
      <td>14.97 ± 6.54</td>
      <td>0.06 ± 0.25</td>
      <td>15.06 ± 6.38 (heel) 0.06 ± 0.25 (cord)</td>
    </tr>
    <tr>
      <td>Term infants only</td>
      <td>14.74 ± 6.42</td>
      <td>0.06 ± 0.25</td>
      <td>14.86 ± 6.22 (heel) 0.06 ± 0.25 (cord)</td>
    </tr>
    <tr>
      <td>Preterm infants only</td>
      <td>18.00 ± 7.50</td>
      <td>0.09 ± 0.28</td>
      <td>17.97 ± 7.93 (heel) 0.07 ± 0.26 (cord)</td>
    </tr>
  </tbody>
</table>

_Data are presented as mean±standard deviation unless otherwise specified. †One cord blood sample was excluded in the data preparation step because 100% of analyte data was missing). All other samples with missing analyte data had no more than 5/47 (11%) missing analyte predictors._

### Performance of gestational age estimation models using heel prick data

We determined the performance of previously published metabolic gestational dating algorithms in heel prick-derived data from the Bangladeshi infant cohort. Results of linear regression analyses for heel prick metabolic profiles demonstrated optimal performance among term infants between 38 and 39 completed gestational weeks (Figure 1). Residual plots for each of the three models in both heel and cord samples are provided in Figure 2. In general, all models predicted gestational ages close to full term with the highest accuracy, while tending to overestimate gestational age in preterm infants and underestimate gestational age in post-term infants, in the Bangladesh cohort.

![Figure 1.](https://cdn.elifesciences.org/articles/42627/elife-42627-fig1-v1.jpg)

**Figure 1.:** (A) Comparison of overall RMSE for heel prick sample and cord blood samples across gestational age models. Performance of gestational age models by infant birthweight for (B) heel prick samples and (C) cord blood samples. Sample sizes are denoted in the graphs. RMSE, root mean square error (average absolute deviation of observed vs. predicted gestational age in weeks). Reported results are the average over 10 imputations.

![Figure 2.](https://cdn.elifesciences.org/articles/42627/elife-42627-fig2-v1.jpg)

**Figure 2.:** Heel prick samples: (A) Model 1: Baseline Model, (B) Model 2: Analyte Model, and (C) Model 3: Full Model. Cord blood samples: (D) Model 1: Baseline Model, (E) Model 2: Analyte Model, and (F) Model 3: Full Model.

A baseline model including only clinical covariates (infant sex, birthweight and multiple birth status, Model 1) provided the least accurate estimation of gestational age relative to ultrasound-validated gestational age estimates, RMSE 1.46 weeks. By comparison, a model including analyte covariates (Model 2) had an RMSE of 1.35 weeks. A full model containing all clinical and analyte data (Model 3) demonstrated the lowest RMSE (best performance) of 1.07 weeks and correctly estimated gestational age to within 1 week for 63.9%, and within 2 weeks for 94.3% of all heel prick samples. Among small for gestational age infants, the full heel prick model had an RMSE of 1.12 weeks when growth restriction was defined as birthweight below the 10th percentile for gestational age and an RMSE of 1.30 weeks when defined as birthweight below the 3rd percentile for gestational age. By these definitions, our model accurately estimated gestational age to within 1 week for 62.8% and 53.4% of growth-restricted infants, respectively.

### Performance of gestational age estimation models using cord blood data

As with heel prick data, algorithmic estimates of gestational age most accurate among term infants (Table 2). When applied to cord blood-derived data, the baseline model (Model 1) and model including analytes (Model 2) performed comparably (RMSE of 1.51 weeks and 1.45 weeks, respectively). As with heel prick data, the full model (Model 3) provided the best estimates of gestational age (RMSE of 1.23). Here, gestational age was correctly estimated to within 2 weeks for 90.4% of infants overall (90.7% and 85% for growth-restricted infants with birthweight below the 10th and 3rd percentiles, respectively; 84.2% for infants < 2500 g). A comparison of the two sample types indicated that metabolic dating models using data derived from heel prick samples provided more accurate gestational age estimates than models using cord blood samples.

**Table 2.**
 Proportion of samples with gestational age correctly estimated within 1 week, 2 weeks of ultrasound-validated gestational age.


<table>
  <thead>
    <tr>
      <th rowspan="2"></th>
      <th rowspan="2"></th>
      <th colspan="4">Heel prick samples</th>
      <th colspan="4">Cord blood samples</th>
    </tr>
    <tr>
      <th>Overall, n(%)</th>
      <th>SGA10, n(%)</th>
      <th>SGA3, n(%)</th>
      <th>&lt;2500 g, n(%)</th>
      <th>Overall, n(%)</th>
      <th>SGA10, n(%)</th>
      <th>SGA3, n(%)</th>
      <th>&lt;2500 g, n(%)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Model 1: Baseline Model</td>
      <td>RMSE n(%) within 1 week n(%) within 2 weeks</td>
      <td>1.46 267 (54.8) 408 (83.8)</td>
      <td>1.76 103 (44.6) 177 (76.6)</td>
      <td>2.32 17 (14.4) 64 (54.2)</td>
      <td>2.22 25 (28.4) 54 (61.4)</td>
      <td>1.51 549 (53.0)  861 (83.1)</td>
      <td>1.82 180 (42.5) 318 (75.0)</td>
      <td>2.38 31 (14.4) 111 (51.6)</td>
      <td>2.21 61 (37.0) 112 (67.9)</td>
    </tr>
    <tr>
      <td>Model 2: Analyte Model</td>
      <td>RMSE n(%) within 1 week n(%) within 2 weeks</td>
      <td>1.35  279 (57.3) 431 (88.5)</td>
      <td>1.40 123 (53.4) 204 (88.1)</td>
      <td>1.38 64 (54.6) 104 (88.1)</td>
      <td>1.47 38 (43.2) 74 (84.1)</td>
      <td>1.45  544 (52.5)  874 (84.4)</td>
      <td>1.43 221 (52.0) 362 (85.4)</td>
      <td>1.48 113 (52.5) 181 (84.1)</td>
      <td>1.94 62 (37.6) 116 (70.3)</td>
    </tr>
    <tr>
      <td>Model 3: Full Model</td>
      <td>RMSE n(%) within 1 week n(%) within 2 weeks</td>
      <td>1.07  311 (63.9)  459 (94.3)</td>
      <td>1.12 145 (62.8) 218 (94.3)</td>
      <td>1.30 63 (53.4) 108 (91.4)</td>
      <td>1.21 52 (59.1) 83 (94.3)</td>
      <td>1.23  615 (59.4) 937 (90.4)</td>
      <td>1.20 267 (63.1) 385 (90.7)</td>
      <td>1.40 116 (54.1) 183 (85.0)</td>
      <td>1.44 88 (53.3) 139 (84.2)</td>
    </tr>
  </tbody>
</table>

_Data are presented as the percentage of the number correctly classified within the total of each birthweight category. Counts were based on the average from 10 imputations rounded to the closest integer._

### Dichotomous discrimination of gestational age

We evaluated the discrimination of gestational age across a dichotomous preterm birth threshold (≥37 weeks vs <37 weeks gestational age) (Figure 3). Gestational age estimation models performed best when applied to metabolic profiles derived from heel prick samples. For both types of samples, the best performance was achieved by the full model containing all clinical and analyte data (Model 3) (area under the curve [AUC] 0.945 (95% CI 0.890, 0.999) for heel prick profiles and AUC 0.894 (95% CI 0.853, 0.935) for cord blood profiles).

![Figure 3.](https://cdn.elifesciences.org/articles/42627/elife-42627-fig3-v1.jpg)

**Figure 3.:** Receiver operator curves for: (A) Model 1: Heel prick AUC 0.840 (95% CI 0.754, 0.925), Cord blood AUC 0.806 (95% CI 0.755, 0.858); (B) Model 2: Heel prick AUC 0.895 (95% CI 0.823, 0.968), Cord Blood AUC 0.823 (95% CI 0.773, 0.873). (C) Model 4, Heel prick AUC 0.945 (95% CI 0.890, 0.999), Cord Blood AUC 0.894 (95% CI 0.853, 0.935). Receiver operator curves for models applied to a cross-section of Ontario-derived heel prick samples (Wilson et al., 2017) are provided for comparison.

**Table 3.**
 Areas under the ROC curve (AUC) for Bangladesh heel prick and cord blood models, and Ontario reference models.


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="3">AUC (lower, upper 95% confidence limits),</th>
    </tr>
    <tr>
      <th></th>
      <th>A) Model 1: Sex, Multiple Birth Status, Birthweight Model</th>
      <th>B) Model 2: Analytes, Sex, Multiple Birth Status Model</th>
      <th>C) Model 3: Full Model</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>0.840 (0.754, 0.925)</td>
      <td>0.895 (0.823, 0.968)</td>
      <td>0.945 (0.890, 0.999)</td>
    </tr>
    <tr>
      <td>Bangladesh Cord</td>
      <td>0.806 (0.755, 0.858)</td>
      <td>0.823 (0.773, 0.873)</td>
      <td>0.894 (0.853, 0.935)</td>
    </tr>
    <tr>
      <td>Ontario Reference (Wilson et al., 2017)</td>
      <td>0.915 (0.909, 0.921)</td>
      <td>0.946 (0.941, 0.952)</td>
      <td>0.967 (0.963, 0.971)</td>
    </tr>
  </tbody>
</table>

### Discussion

In this paper, we demonstrate that algorithms developed using newborn screening data from Ontario, Canada are effective in deriving estimates of gestational age in infants born in Matlab, Bangladesh that are accurate to within approximately 1 to 2 weeks of ultrasound-validated gestational age. Data derived from newborn heel prick samples consistently yielded more accurate estimates of gestational age than cord blood-derived data, likely reflecting the fact that our models were originally developed from data obtained from this sample type. Indeed, we have shown that the correlation between cord blood and heel prick-derived data varies significantly across analyte subtypes (Appendix 1).

Accurate assessment of gestational age, preterm birth and small for gestational age is a recognized priority area where there is a need to improve program tracking and accountability (March of Dimes, 2012; WHO, 2014). Although birthweight data are collected in most settings, it is an unreliable surrogate for gestational age that is prone to overestimation of preterm birth rates in low- and middle-income settings where a high proportion of infants are born small for gestational age. Commonly-used gestational age assessments applied after birth are hampered by their reliance on complex scoring systems. A recent systematic review and meta-analysis of 18 newborn assessments based on a variety of neuromuscular, physical and other criteria determined that the most popular scoring systems (the Ballard and Dubowitz scores) systematically overestimated gestational age with wide margins of error (Lee et al., 2016). Whereas gold standard first trimester ultrasound scans are accurate to within one week, the accuracy of measurements based on newborn examination varies from 2 to 4 weeks. Furthermore, newborn clinical assessments of gestational age such as Dubowitz and Ballard scoring, and neonatal anthropometrics have been demonstrated to be inaccurate surrogate markers of gestational age, specifically in rural communities of Bangladesh (Lee et al., 2016).

Metabolic gestational dating approaches emerged in response to the urgent need to improve the epidemiology and surveillance of preterm birth. Circulating newborn metabolites are known to be affected by gestational age and gestational age is routinely considered in the interpretation of newborn screening analysis (Slaughter et al., 2010; Oladipo et al., 2011; Newborn Screening Ontario, 2017). To date, three groups in North America have developed metabolic dating algorithms based on newborn health administrative datasets (Jelliffe-Pawlowski et al., 2016; Ryckman et al., 2016; Wilson et al., 2016). Research has since sought to refine existing models through the addition of analytes known to correlate with gestational age and develop tiered models of varying complexity. Our own group has demonstrated that proportions of fetal and adult hemoglobins are some of the strongest individual predictors of gestational age, (Wilson et al., 2017) and we have also validated our algorithms across ethnic subgroups in Ontario (Hawken et al., 2017). Efforts are currently underway to begin implementing metabolic gestational age dating in low-resource settings to determine the burden of preterm birth and intrauterine growth restriction. The results from our study offer a reason to be optimistic about these efforts. While the intent of metabolic gestational age dating at present is to provide population-based estimates of the burden of preterm birth, it is conceivable that this approach could also be used to guide care for individual newborns who are identified as preterm.

Our study had a number of important strengths and limitations. Strengths of our approach include the use of internationally-derived samples to externally validate our models and using samples from a well-described cohort of infants with gestational age confirmed by first trimester ultrasound. The study design of the PreSSMat cohort in which our study was nested ensured that enrollment was open to a representative selection of women and newborns delivering in the Matlab icddr,b service area. Other strengths include the high quality of samples received for analysis, and the use of paired cord blood and heel prick samples to compare model performance metrics. The primary limitation of this study is the participation bias against very preterm and extremely preterm infants, whose parents expressed reluctance to subjecting their newborn to these collection procedures. As a result, we had a relatively small number of samples collected from very preterm and extremely preterm infants, limiting our ability to comment on model performance in these sub-groups. In this Bangladesh cohort, the gestational ages estimated from our models were most accurate in infants who were confirmed to be close to full-term by first trimester ultrasound. Algorithm-derived gestational ages tended to be overestimated in preterm infants and underestimated in post-term infants. This suggests that calibration in the large (i.e. introducing a calibration slope adjustment (Steyerberg, 2010) to model predictions could improve overall model performance in this external cohort, although this was not conducted in the current study.

Our findings are encouraging for several reasons. First, this work provides early evidence that gestational dating models developed using metabolic data derived from a North American cohort perform well in low-resource populations. The model originally published by our group was developed using data from a Canadian-born cohort of 250,000 infants. In Ontario, the model was able to estimate gestational age to within one week (RMSE 1.06 vs 1.07 for the Bangladeshi cohort) overall and correctly ascertain gestational age to within 2 weeks for 94.9% of infants (vs. 94.3% for the Bangladeshi cohort) (Wilson et al., 2016); estimates that compare favorably against other currently-used postnatal gestational age estimation methods that produce estimates varying in accuracy from 2 to 4 weeks gestational age (Taylor et al., 2010; Spinnato et al., 1984; Robillard et al., 1992; Lee et al., 2016; Alexander et al., 1992). Second, our metabolic models provided significantly improved estimates of gestational age among infants with birthweights < 2500 g, cases where current estimates based on symphysis fundal height and neuromuscular assessments perform poorly (Spinnato et al., 1984; Goto, 2013). Lastly, we are encouraged by the potential utility of cord blood profiles for deriving gestational age estimates. Differences in cord blood and heel prick profiles described in our analysis likely stem from a number of factors related to timing of collection, including early postnatal fluctuations in neonatal TSH levels, (Ryckman et al., 2012; Büyükgebiz, 2013) and infant feeding status prior to collection. Although the performance of the models when applied to cord-blood-derived data was somewhat attenuated relative to heel prick data, development of cord-blood-specific models restricted to analytes less susceptible to fluctuations in the postnatal environment may further improve gestational age estimation.

Ultimately, acceptable levels of error in gestational age measurements will need to be determined by public health and maternal child health officials. Given the acknowledged limitations of existing alternatives to ultrasound estimation, metabolic gestational dating approaches appear to offer reliable estimates that are unencumbered by user variability. As we prepare for the scale-up and implementation of metabolic gestational dating approaches for robust population-level estimates of preterm birth, our findings highlight a number of opportunities and challenges. First, heel prick samples taken for newborn screening are typically collected at least 24 hr after birth to accommodate postpartum fluctuations in analyte levels. In many settings around the world, mother-infant pairs are discharged from healthcare settings within the first 24 hr after delivery (Campbell et al., 2016). As a result, the accuracy of existing metabolic dating algorithms would be compromised by the change in timing of sample collection. Second, newborn screening is not a standard service of practice in low- and middle-income countries, including Bangladesh. It was therefore unsurprising that anecdotal feedback from field nurses assisting with this study indicated that parents were hesitant to consent to heel prick procedures for their infants. Although on-site research staff received extensive training through videos, visual guides and in-person training, a preference for collection of cord blood samples over heel prick amongst research staff may also have affected the number and quality of samples collected. A quality assurance trial was required to improve sample collection and handling techniques. While our current models were originally optimized for application to heel prick data, we highlight an opportunity to optimize these algorithms for use on cord blood data. Transitioning to cord blood-based models would additionally bypass the need to impose discomfort on the child, stress on parents and staff, and also avoid the requirement for extensive training and screening of sample collection techniques. Finally, population-level metabolic screening provides the additional opportunity to provide insight into the prevalence of congenital conditions in participating jurisdictions.

In summary, metabolic gestational age dating approaches offer a novel means for providing accurate population-level gestational age estimates. As we work toward implementing preterm birth surveillance initiatives in a variety of low-income settings (Mundel, 2017), the level of acceptable accuracy of metabolic algorithms should be considered. Application of models to cord blood metabolic profiles is the most feasible option at present, although derivation and optimization of such models are warranted. Utility of other maternal, pregnancy and infant factors that were not available to us in the current analysis for improving existing metabolic dating models may also be of benefit. Where population-level surveillance of preterm birth might be supported through the analysis of a few drops of blood taken shortly after birth, future work should aim to derive models that determine other priority birth outcomes.

## Materials and methods

### Objectives

Our objective was to validate the performance of previously published gestational age estimation models developed in Ontario, Canada (Wilson et al., 2016; Wilson et al., 2017) in a cohort of infants born in Bangladesh. Specifically, we sought to compare estimates of gestational age derived from our algorithms, through the analysis of newborn blood spots, against estimates of gestational age determined by first-trimester ultrasound. A version of the protocol for this study has been published (Murphy et al., 2017). Due to logistical challenges in initiating the study, fewer samples were collected than initially anticipated in our protocol and low numbers of infants with gestational age below 34 weeks. Our methods of sample collection and analysis remained the same.

### Newborn screening

Newborn screening is a public health initiative that screens for rare, treatable conditions that typically produce no symptoms in the neonatal period. Programs vary in scope by jurisdiction, screening for one to over 50 conditions (Therrell et al., 2015). In Ontario, as in many regions, drops of blood are taken by infant heel prick, typically within the first few days after birth, and dried onto filter paper. Dried blood spot samples are then analyzed by a series of assays including tandem mass spectrometry, colorimetric and immunoassays as well as high-performance liquid chromatography for metabolic, genetic and other analyte markers.

### Study design

Sample collection was conducted in the Matlab sub-district of Chandpur, Bangladesh where the International Centre for Diarrhoeal Disease Research, Bangladesh (icddr,b) has been running a Health and Demographic Surveillance System (HDSS) in Matlab since 1966. Based on service provision, the HDSS area is divided into two jurisdictions: 1) the icddr,b service area where women of reproductive age and their children under 5 years of age receive care though icddr,b facilities; and 2) the government service area where individuals receive care from government facilities as in other areas of the country. The present study was conducted in the icddr,b service area, and nested within a cohort study entitled ‘Preterm and Stillbirth Study, Matlab’ (PreSSMat) that was designed to capture data on the biological determinants of adverse pregnancy outcomes, including preterm births. In the PreSSMat cohort, pregnant women were followed prospectively along the pregnancy continuum, with scheduled visits at 11–14 (enrollment and ultrasound), 22–24, and 32 weeks’ gestation, at delivery, and at 6 weeks post-partum to collect socio-demographic and clinical data as well as biological specimens. Preterm births were defined as all births that occurred at <37 weeks’ gestation. ‘Very preterm births’ were those that occurred at <32 weeks, and ‘extremely preterm births’ were those that occurred at <28 weeks. Small for gestational age (SGA10) was defined as cases where birthweight was below the 10th percentile within categories of week of gestational age at delivery and infant sex. The percentiles were calculated and applied based on a North American distribution of birthweight within sex and gestational age categories. We also calculated SGA3, which identifies infants below the 3rd percentile within gestational age and sex categories and is much more likely to reflect infants who suffered intrauterine growth restriction, especially in low and middle-income countries such as Bangladesh where birthweights are lower. Pregnant women were identified by community health workers through monthly home visits. All enrolled women underwent a gestational dating ultrasound at enrollment; otherwise no explicit inclusion or exclusion criteria were applied. All women enrolled in the PreSSMat cohort were eligible for participation in the current study.

### Sample collection and analysis

To examine the effect of timing of sample collection on newborn metabolic profiles, cord blood was collected immediately after birth and spotted on Whatman 903 filter paper. A second dried blood spot sample was also collected via heel prick within 72 hr of delivery or immediately prior to discharge, whichever happened first. The latter reflects the timing of collection for samples used to develop our previously published gestational age estimation models (recommended timing of sample collection for healthy newborns in Ontario, Canada is 24–48 hr after birth). Samples were collected onto filter paper, air-dried and shipped weekly to Newborn Screening Ontario (NSO), the provincial newborn screening facility in Ottawa, Canada. Samples were stored in a temperature and humidity-controlled environment prior to shipment. Eight 3.2 mm diameter samples were punched from each sample for testing of the following analytes: hemoglobin profiles; 17α hydroxyprogesterone (17-OHP); thyroid stimulating hormone (TSH); immunoreactive trypsinogen (IRT); a panel of 12 amino acids and 31 acylcarnitines; t-cell receptor excision circles (TREC); biotinidase activity; and galactose-1-phosphate uridylyltransferase activity. Hemoglobin profiles were determined by high-performance liquid chromatography on a Bio Rad Variant nbs system; neonatal 17-OHP, TSH and IRT were measured using PerkinElmer AutoDELFIA Immunoassays; amino acid and acylcarnitine analysis was performed by electrospray ionization tandem mass spectrometry (Waters TQD); total TREC copy number was measured by quantitative polymerase chain reaction using a ThermoFisher Scientific Viia 7; biotinidase and galactose-1-phosphate uridyltransferase levels were measured using the Astoria-Pacific SPOTCHECK Pro system. Clinical covariates were retrieved from the PreSSMat database to facilitate clinical interpretation of newborn screening data, and also for inclusion as model parameters in this study. Figure 4 summarizes the study design.

![Figure 4.](https://cdn.elifesciences.org/articles/42627/elife-42627-fig4-v1.jpg)

**Figure 4.:** The current study was nested within the PreSSMat cohort operating in Matlab, Bangladesh. Samples were collected from infants born into the cohort and sent to Ottawa, Canada for analysis at a provincial newborn screening facility.

Newborn screening blood spots are subject to degradation if collected or handled inappropriately. Samples with insufficient good-quality dried blood to complete the full panel of assays were excluded from analysis. Samples with missing analyte values had the missing levels imputed (see Appendix 1 for details). In the process of applying newborn screening procedures for the analysis of samples, results of ‘screen negative’ and ‘screen positive’ were generated for conditions screened for by the NSO program. Management of incidental clinical findings (screen-positive cases) has been reported elsewhere (Murphy et al., 2017).

### Statistical analyses

#### Validation of algorithms

We sought to compare estimates of gestational age and preterm birth based on our analysis of blood spots against first trimester ultrasound estimates, which are considered the gold standard for gestational age measurement (Committee on Obstetric Practice, the American Institute of Ultrasound in Medicine, and the Society for Maternal-Fetal Medicine, 2017). The performance of the following models was assessed:

Statistical modeling approaches are described in Appendix 1. In brief, sample data were scored using multivariable models previously developed using heel prick blood spot samples in a large cohort of infants born in Ontario, Canada (Wilson et al., 2017). The fitted models used for scoring the Bangladesh data included numerous main effects and interaction terms including both analytes and clinical measures (sex, multiple birth, birthweight). However, there was a subset of predictors that were clearly the strongest contributors to the model in terms of independent contribution to explained variance: birthweight (in base and full models) and fetal/adult hemoglobin ratio, TSH, 17OHP, ALA, c5, C4DC and TYR (in the sex +multiple birth +analytes and full models). All analyses were conducted using SAS 9.4 (SAS Institute, 2017) and R 3.3.2 (R core team, 2017).

### Informed consent and ethical approval

Mothers provided informed consent for their infants to be included in the PreSSMat birth cohort and to have clinical data, cord blood and newborn heel prick samples collected and analysed. The present study was approved by the Research Review and Ethical Review Committees of the International Centre for Diarrhoeal Disease Research, Bangladesh (PR-16039) on July 10, 2016. Approvals were also obtained from the Research Ethics Boards of the Ottawa Health Science Network (20160219–01H) on June 10, 2016, and the Children’s Hospital of Eastern Ontario (16/20E) on June 8, 2016.
