# Early prediction of in-hospital death of COVID-19 patients: a machine-learning model based on age, blood analyses, and chest x-ray score

## Authors

- Emirena Garrafa<sup>1</sup> ([ORCID: 0000-0003-4761-6892](https://orcid.org/0000-0003-4761-6892)) †
- Marika Vezzoli<sup>1</sup>
- Marco Ravanelli<sup>3</sup> ([ORCID: 0000-0002-4841-2771](https://orcid.org/0000-0002-4841-2771))
- Davide Farina<sup>3</sup>
- Andrea Borghesi<sup>3</sup>
- Stefano Calza<sup>1</sup>
- Roberto Maroldi<sup>3</sup>

### Affiliations

1. Department of Molecular and Translational Medicine, University of Brescia Brescia Italy
2. ASST Spedali Civili di Brescia, Department of Laboratory Brescia Italy
3. Department of Medical and Surgical Specialties, Radiological Sciences and Public Health, University of Brescia Brescia Italy
4. ASST Spedali Civili di Brescia, Department of Radiology Brescia Italy

† Corresponding author

## Abstract

An early-warning model to predict in-hospital mortality on admission of COVID-19 patients at an emergency department (ED) was developed and validated using a machine-learning model. In total, 2782 patients were enrolled between March 2020 and December 2020, including 2106 patients (first wave) and 676 patients (second wave) in the COVID-19 outbreak in Italy. The first-wave patients were divided into two groups with 1474 patients used to train the model, and 632 to validate it. The 676 patients in the second wave were used to test the model. Age, 17 blood analytes, and Brescia chest X-ray score were the variables processed using a random forests classification algorithm to build and validate the model. Receiver operating characteristic (ROC) analysis was used to assess the model performances. A web-based death-risk calculator was implemented and integrated within the Laboratory Information System of the hospital. The final score was constructed by age (the most powerful predictor), blood analytes (the strongest predictors were lactate dehydrogenase, D-dimer, neutrophil/lymphocyte ratio, C-reactive protein, lymphocyte %, ferritin std, and monocyte %), and Brescia chest X-ray score (https://bdbiomed.shinyapps.io/covid19score/). The areas under the ROC curve obtained for the three groups (training, validating, and testing) were 0.98, 0.83, and 0.78, respectively. The model predicts in-hospital mortality on the basis of data that can be obtained in a short time, directly at the ED on admission. It functions as a web-based calculator, providing a risk score which is easy to interpret. It can be used in the triage process to support the decision on patient allocation.

## Introduction

Starting from late February 2020, the COVID-19 outbreak struck the north of Italy causing more than 30,000 deaths in Lombardy alone, up to the end of March 2021. At the beginning of the outbreak, the Spedali Civili di Brescia (SCBH), the university hospital of one of the hardest hit cities in Europe, was faced with a ‘flash flood’ of severely ill patients seeking admission to the emergency department (ED). For several weeks, their number exceeded the available resources, obliging a continuous organizational restructuring of the hospital wards (Garrafa et al., 2020b).

In those weeks, given the limited evidence of clinically proven predictors (Marengoni et al., 2021; Wynants et al., 2020; Sperrin et al., 2020), prioritizing hospital admission of non-critical patients was an arduous task. Essentially, the criteria were based on the presence of fever, respiratory symptoms, and the level of blood oxygenation. A significant drawback of this approach was that patients referring to the ED with very similar clinical findings underwent inconsistent assessments. In this scenario, the availability of predictors would have been extremely beneficial, not only to triage patients, but also to monitor hospitalized patients and warn of exacerbation of the outbreaks.

Starting from March 2020, all patients referred to EDs underwent a chest X-ray at admission or within a few hours. With the purpose of grading pulmonary involvement and tracking changes objectively over time, a chest X-ray severity score was developed (Brescia X-ray score) (Borghesi and Maroldi, 2020; Maroldi et al., 2021; Borghesi et al., 2020a; Borghesi et al., 2020b). The score was able to predict in-hospital mortality in 302 patients. In addition to the chest X-ray severity score, a dedicated blood sampling profile was included in the COVID-19 ED work-up (Garrafa et al., 2020a). Among its 17 blood analytes, the sampling profile encompassed hemachrome, inflammation biomarkers such as C-reactive protein (CRP), lactate dehydrogenase (LDH), and ferritin, and coagulation markers (fibrinogen and D-dimer). Since that time, the medical literature began to encompass an increasing number of studies advocating the prognostic value of single or grouped blood parameters (Bonetti et al., 2020; Borghi et al., 2020; Avouac et al., 2021; Knight et al., 2020). All these parameters were present in our COVID-19 sampling profile.

This study aims to develop and validate an early-warning model (BS-EWM), predictive of in-hospital death, based on data that could easily be acquired on admission to the ED: age, simple blood biomarkers, and chest X-ray. The model was constructed based on the analysis of a cohort of 2872 COVID-19 patients treated in a single reference center over a 10-month period.

This paper adheres to the TRIPOD checklist for predictive model development and validation (Collins et al., 2015).

The study was approved by the local ethics committee (COVID-SURG-BS; NP 4059).

## Results

### Description of the sample

The entire sample analyzed in this paper contained 2782 COVID-19 patients (1010 female [36.3%] and 1772 male [63.7%]), admitted to the ED and hospitalized at SCBH from March to December 2020. During these 10 months, the pandemic had two temporal waves: March–April (MA) (2106 patients, 75.70% of the entire sample) and May–December (MD) (676 patients, 24.30% of the entire sample) (Supplementary file 1a). The model was trained on a subsample extracted from the first wave (70%) and tested (i) on data not used to calibrate the model (remaining 30% from the first wave) and (ii) on data from the second wave (Figure 1).

![Figure 1.](https://cdn.elifesciences.org/articles/70640/elife-70640-fig1-v3.jpg)

**Figure 1.:** The early-warning model (BS-EWM) was trained with a random forest on 70% of first-wave patients (rebalanced with the synthetic minority oversampling technique [SMOTE] procedure) and (i) validated on remaining 30% of first-wave patients (ii) tested on 676 second-wave patients. In detail, 2106 patients were randomly in training and validating, maintaining the same death prevalence of the first wave.

The first-wave subsample contained 2106 COVID-19 patients hospitalized in March–April 2020 at SCBH: 744 females (35.3%) and 1362 males (64.7%) (Table 1). During that period, 423 patients died (20.09% of the total): 131 females (31%) and 292 males (69%). Their mean age ± SD was 66.89 ± 14.19: 67.93 ± 15.40 for females and 66.32 ± 13.45 for males (p-value = 0.001). The mean age of deceased patients was 76.21 ± 9.12, while for living patients, it was 64.55 ± 14.27 (p-value < 0.001). Mean hospital stay was 13.58 ± 11.58 days (from a minimum of 0 to a maximum of 140 days): 11.33 ± 10.98 days for patients who died, 14.15 ± 11.66 days for surviving patients (p-value < 0.001).

**Table 1.**
 Descriptive statistics on all variables in the dataset stratified respect alive–dead. Comparison between first (March–April) and second (May–December) wave.


<table>
  <thead>
    <tr>
      <th rowspan="2">Variables</th>
      <th colspan="2">First wave: March–April (MA) 2020</th>
      <th rowspan="2">p-Value</th>
      <th colspan="2">Second wave: May–December (MD) 2020</th>
      <th rowspan="2">p-Value</th>
    </tr>
    <tr>
      <th>Alive(N = 1683)</th>
      <th>Dead(N = 423)</th>
      <th>Alive (N = 594)</th>
      <th>Dead (N = 82)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Age</td>
      <td></td>
      <td></td>
      <td>&lt;0.001*</td>
      <td></td>
      <td></td>
      <td>&lt;0.001*</td>
    </tr>
    <tr>
      <td>Mean (SD)</td>
      <td>64.55 (14.27)</td>
      <td>76.21 (9.12)</td>
      <td></td>
      <td>65.30 (15.20)</td>
      <td>76.72 (10.79)</td>
      <td></td>
    </tr>
    <tr>
      <td>Median(Q1, Q3)</td>
      <td>65.00(55.00, 75.00)</td>
      <td>77.00(72.00, 82.00)</td>
      <td></td>
      <td>67.00(55.00, 77.00)</td>
      <td>80.00(72.25, 84.75)</td>
      <td></td>
    </tr>
    <tr>
      <td>Range</td>
      <td>19.00–97.00</td>
      <td>44.00–98.00</td>
      <td></td>
      <td>18.00–97.00</td>
      <td>44.00–98.00</td>
      <td></td>
    </tr>
    <tr>
      <td>Sex</td>
      <td></td>
      <td></td>
      <td>0.036†</td>
      <td></td>
      <td></td>
      <td>0.131†</td>
    </tr>
    <tr>
      <td>F</td>
      <td>613 (36.4%)</td>
      <td>131 (31.0%)</td>
      <td></td>
      <td>240 (40.4%)</td>
      <td>26 (31.7%)</td>
      <td></td>
    </tr>
    <tr>
      <td>M</td>
      <td>1,070 (63.6%)</td>
      <td>292 (69.0%)</td>
      <td></td>
      <td>354 (59.6%)</td>
      <td>56 (68.3%)</td>
      <td></td>
    </tr>
    <tr>
      <td>Days in hospital</td>
      <td></td>
      <td></td>
      <td>&lt;0.001*</td>
      <td></td>
      <td></td>
      <td>0.008*</td>
    </tr>
    <tr>
      <td>N-Miss</td>
      <td>1</td>
      <td>0</td>
      <td></td>
      <td>95</td>
      <td>0</td>
      <td></td>
    </tr>
    <tr>
      <td>Mean (SD)</td>
      <td>14.15 (11.66)</td>
      <td>11.33 (10.98)</td>
      <td></td>
      <td>14.95 (11.67)</td>
      <td>17.77 (10.75)</td>
      <td></td>
    </tr>
    <tr>
      <td>Median(Q1, Q3)</td>
      <td>11.00(7.00, 18.00)</td>
      <td>8.00(4.00, 15.00)</td>
      <td></td>
      <td>12.00(7.00, 20.00)</td>
      <td>17.50(9.00, 25.00)</td>
      <td></td>
    </tr>
    <tr>
      <td>Range</td>
      <td>0.00–140.00</td>
      <td>0.00–88.00</td>
      <td></td>
      <td>0.00–79.00</td>
      <td>2.00–46.00</td>
      <td></td>
    </tr>
    <tr>
      <td>Score</td>
      <td></td>
      <td></td>
      <td>&lt;0.001*</td>
      <td></td>
      <td></td>
      <td>&lt;0.001*</td>
    </tr>
    <tr>
      <td>Mean (SD)</td>
      <td>6.92 (4.40)</td>
      <td>8.77 (4.39)</td>
      <td></td>
      <td>5.65 (4.48)</td>
      <td>8.23 (4.63)</td>
      <td></td>
    </tr>
    <tr>
      <td>Median(Q1, Q3)</td>
      <td>7.00(3.00, 10.00)</td>
      <td>9.00(6.00, 12.00)</td>
      <td></td>
      <td>5.00(2.00, 9.00)</td>
      <td>9.00(5.25, 11.00)</td>
      <td></td>
    </tr>
    <tr>
      <td>Range</td>
      <td>0.00–18.00</td>
      <td>0.00–18.00</td>
      <td></td>
      <td>0.00–18.00</td>
      <td>0.00–17.00</td>
      <td></td>
    </tr>
    <tr>
      <td>D-dimer</td>
      <td></td>
      <td></td>
      <td>&lt;0.001*</td>
      <td></td>
      <td></td>
      <td>&lt;0.001*</td>
    </tr>
    <tr>
      <td>N-Miss</td>
      <td>406</td>
      <td>113</td>
      <td></td>
      <td>128</td>
      <td>16</td>
      <td></td>
    </tr>
    <tr>
      <td>Mean (SD)</td>
      <td>1155.03 (2218.51)</td>
      <td>3124.25 (8070.21)</td>
      <td></td>
      <td>1538.17 (3123.38)</td>
      <td>4712.44 (8897.82)</td>
      <td></td>
    </tr>
    <tr>
      <td>Median(Q1, Q3)</td>
      <td>443.00(262.00, 985.00)</td>
      <td>944.50(476.50, 2970.75)</td>
      <td></td>
      <td>739.50(427.50, 1341.25)</td>
      <td>1112.00(725.50, 3619.25)</td>
      <td></td>
    </tr>
    <tr>
      <td>Range</td>
      <td>200.00–47228.00</td>
      <td>200.00–60,342.00</td>
      <td></td>
      <td>190.00–33,501.00</td>
      <td>190.00–35,000.00</td>
      <td></td>
    </tr>
    <tr>
      <td>Fibrinogen</td>
      <td></td>
      <td></td>
      <td>0.951*</td>
      <td></td>
      <td></td>
      <td>0.778*</td>
    </tr>
    <tr>
      <td>N-Miss</td>
      <td>339</td>
      <td>117</td>
      <td></td>
      <td>54</td>
      <td>8</td>
      <td></td>
    </tr>
    <tr>
      <td>Mean (SD)</td>
      <td>530.53 (194.13)</td>
      <td>530.55 (213.69)</td>
      <td></td>
      <td>523.94 (169.43)</td>
      <td>519.77 (213.05)</td>
      <td></td>
    </tr>
    <tr>
      <td>Median(Q1, Q3)</td>
      <td>520.00(381.00, 650.00)</td>
      <td>515.00(381.00, 654.00)</td>
      <td></td>
      <td>512.00(405.00, 612.00)</td>
      <td>510.00(330.50, 649.00)</td>
      <td></td>
    </tr>
    <tr>
      <td>Range</td>
      <td>119.00–1339.00</td>
      <td>68.00–1333.00</td>
      <td></td>
      <td>147.00–1371.00</td>
      <td>153.00–1287.00</td>
      <td></td>
    </tr>
    <tr>
      <td>LDH</td>
      <td></td>
      <td></td>
      <td>&lt;0.001*</td>
      <td></td>
      <td></td>
      <td>&lt;0.001*</td>
    </tr>
    <tr>
      <td>N-Miss</td>
      <td>188</td>
      <td>92</td>
      <td></td>
      <td>61</td>
      <td>7</td>
      <td></td>
    </tr>
    <tr>
      <td>Mean (SD)</td>
      <td>321.25 (227.50)</td>
      <td>433.71 (205.10)</td>
      <td></td>
      <td>308.30 (196.23)</td>
      <td>443.49 (707.95)</td>
      <td></td>
    </tr>
    <tr>
      <td>Median(Q1, Q3)</td>
      <td>283.00(222.00, 373.00)</td>
      <td>406.00(269.50, 545.50)</td>
      <td></td>
      <td>273.00(218.00, 354.00)</td>
      <td>332.00(257.00, 442.50)</td>
      <td></td>
    </tr>
    <tr>
      <td>Range</td>
      <td>90.00–6689.00</td>
      <td>123.00–1365.00</td>
      <td></td>
      <td>108.00–2565.00</td>
      <td>122.00–6310.00</td>
      <td></td>
    </tr>
    <tr>
      <td>Neutrophils</td>
      <td></td>
      <td></td>
      <td>&lt;0.001*</td>
      <td></td>
      <td></td>
      <td>&lt;0.001*</td>
    </tr>
    <tr>
      <td>N-Miss</td>
      <td>23</td>
      <td>19</td>
      <td></td>
      <td>4</td>
      <td>1</td>
      <td></td>
    </tr>
    <tr>
      <td>Mean (SD)</td>
      <td>5.67 (3.61)</td>
      <td>7.17 (4.39)</td>
      <td></td>
      <td>5.80 (3.97)</td>
      <td>7.21 (4.13)</td>
      <td></td>
    </tr>
    <tr>
      <td>Median(Q1, Q3)</td>
      <td>4.83(3.29, 7.03)</td>
      <td>6.20(4.12, 9.02)</td>
      <td></td>
      <td>4.78(3.42, 7.11)</td>
      <td>6.72(4.00, 9.77)</td>
      <td></td>
    </tr>
    <tr>
      <td>Range</td>
      <td>0.00–53.99</td>
      <td>0.17–30.45</td>
      <td></td>
      <td>0.10–47.03</td>
      <td>0.19–23.02</td>
      <td></td>
    </tr>
    <tr>
      <td>Lymphocytes</td>
      <td></td>
      <td></td>
      <td>&lt;0.001*</td>
      <td></td>
      <td></td>
      <td>&lt;0.001*</td>
    </tr>
    <tr>
      <td>N-Miss</td>
      <td>23</td>
      <td>19</td>
      <td></td>
      <td>4</td>
      <td>1</td>
      <td></td>
    </tr>
    <tr>
      <td>Mean (SD)</td>
      <td>1.43 (5.48)</td>
      <td>1.19 (4.29)</td>
      <td></td>
      <td>1.22 (0.81)</td>
      <td>1.38 (4.63)</td>
      <td></td>
    </tr>
    <tr>
      <td>Median(Q1, Q3)</td>
      <td>1.04(0.75, 1.42)</td>
      <td>0.81(0.55, 1.18)</td>
      <td></td>
      <td>1.06(0.72, 1.52)</td>
      <td>0.74(0.47, 1.06)</td>
      <td></td>
    </tr>
    <tr>
      <td>Range</td>
      <td>0.10–177.63</td>
      <td>0.04–85.51</td>
      <td></td>
      <td>0.08–10.28</td>
      <td>0.08–42.20</td>
      <td></td>
    </tr>
    <tr>
      <td>Neutrophils on lymphocytes</td>
      <td></td>
      <td></td>
      <td>&lt;0.001*</td>
      <td></td>
      <td></td>
      <td>&lt;0.001*</td>
    </tr>
    <tr>
      <td>N-Miss</td>
      <td>23</td>
      <td>19</td>
      <td></td>
      <td>4</td>
      <td>1</td>
      <td></td>
    </tr>
    <tr>
      <td>Mean (SD)</td>
      <td>6.18 (5.87)</td>
      <td>10.72 (11.71)</td>
      <td></td>
      <td>7.19 (9.92)</td>
      <td>12.84 (13.09)</td>
      <td></td>
    </tr>
    <tr>
      <td>Median(Q1, Q3)</td>
      <td>4.52(2.84, 7.50)</td>
      <td>7.13(4.47, 13.06)</td>
      <td></td>
      <td>4.32(2.63, 8.40)</td>
      <td>8.50(4.05, 15.19)</td>
      <td></td>
    </tr>
    <tr>
      <td>Range</td>
      <td>0.00–101.90</td>
      <td>0.01–129.67</td>
      <td></td>
      <td>0.12–143.25</td>
      <td>0.11–70.56</td>
      <td></td>
    </tr>
    <tr>
      <td>Neutrophils %</td>
      <td></td>
      <td></td>
      <td>&lt;0.001*</td>
      <td></td>
      <td></td>
      <td>&lt;0.001*</td>
    </tr>
    <tr>
      <td>N-Miss</td>
      <td>22</td>
      <td>19</td>
      <td></td>
      <td>4</td>
      <td>1</td>
      <td></td>
    </tr>
    <tr>
      <td>Mean (SD)</td>
      <td>0.73 (0.13)</td>
      <td>0.80 (0.12)</td>
      <td></td>
      <td>0.73 (0.13)</td>
      <td>0.79 (0.16)</td>
      <td></td>
    </tr>
    <tr>
      <td>Median(Q1, Q3)</td>
      <td>0.74(0.66, 0.82)</td>
      <td>0.82(0.75, 0.88)</td>
      <td></td>
      <td>0.73(0.64, 0.83)</td>
      <td>0.83(0.69, 0.89)</td>
      <td></td>
    </tr>
    <tr>
      <td>Range</td>
      <td>0.00–0.97</td>
      <td>0.01–0.97</td>
      <td></td>
      <td>0.10–0.99</td>
      <td>0.10–0.96</td>
      <td></td>
    </tr>
    <tr>
      <td>Lymphocytes %</td>
      <td></td>
      <td></td>
      <td>&lt;0.001*</td>
      <td></td>
      <td></td>
      <td>&lt;0.001*</td>
    </tr>
    <tr>
      <td>N-Miss</td>
      <td>22</td>
      <td>19</td>
      <td></td>
      <td>4</td>
      <td>1</td>
      <td></td>
    </tr>
    <tr>
      <td>Mean (SD)</td>
      <td>0.18 (0.11)</td>
      <td>0.13 (0.09)</td>
      <td></td>
      <td>0.18 (0.11)</td>
      <td>0.13 (0.13)</td>
      <td></td>
    </tr>
    <tr>
      <td>Median(Q1, Q3)</td>
      <td>0.16(0.11, 0.23)</td>
      <td>0.11(0.07, 0.17)</td>
      <td></td>
      <td>0.17(0.10, 0.25)</td>
      <td>0.10(0.06, 0.18)</td>
      <td></td>
    </tr>
    <tr>
      <td>Range</td>
      <td>0.01–0.97</td>
      <td>0.01–0.99</td>
      <td></td>
      <td>0.01–0.88</td>
      <td>0.01–0.88</td>
      <td></td>
    </tr>
    <tr>
      <td>PCR</td>
      <td></td>
      <td></td>
      <td>&lt;0.001*</td>
      <td></td>
      <td></td>
      <td>0.004*</td>
    </tr>
    <tr>
      <td>N-Miss</td>
      <td>47</td>
      <td>12</td>
      <td></td>
      <td>21</td>
      <td>0</td>
      <td></td>
    </tr>
    <tr>
      <td>Mean (SD)</td>
      <td>77.25 (75.76)</td>
      <td>117.68 (95.97)</td>
      <td></td>
      <td>64.28 (73.38)</td>
      <td>98.59 (102.49)</td>
      <td></td>
    </tr>
    <tr>
      <td>Median(Q1, Q3)</td>
      <td>55.65(17.30, 111.60)</td>
      <td>99.20(42.80, 170.45)</td>
      <td></td>
      <td>39.10(12.30, 91.10)</td>
      <td>74.80(20.12, 140.73)</td>
      <td></td>
    </tr>
    <tr>
      <td>Range</td>
      <td>0.30–479.00</td>
      <td>0.70–471.10</td>
      <td></td>
      <td>0.30–483.20</td>
      <td>0.30–593.80</td>
      <td></td>
    </tr>
    <tr>
      <td>WBC</td>
      <td></td>
      <td></td>
      <td>&lt;0.001*</td>
      <td></td>
      <td></td>
      <td>0.011*</td>
    </tr>
    <tr>
      <td>N-Miss</td>
      <td>21</td>
      <td>19</td>
      <td></td>
      <td>4</td>
      <td>1</td>
      <td></td>
    </tr>
    <tr>
      <td>Mean (SD)</td>
      <td>7.73 (7.13)</td>
      <td>9.13 (7.46)</td>
      <td></td>
      <td>7.65 (4.17)</td>
      <td>9.23 (6.25)</td>
      <td></td>
    </tr>
    <tr>
      <td>Median(Q1, Q3)</td>
      <td>6.62(4.87, 9.11)</td>
      <td>7.62(5.60, 10.74)</td>
      <td></td>
      <td>6.67(5.02, 8.90)</td>
      <td>8.34(5.55, 12.04)</td>
      <td></td>
    </tr>
    <tr>
      <td>Range</td>
      <td>0.72–191.02</td>
      <td>0.32–92.23</td>
      <td></td>
      <td>0.97–48.19</td>
      <td>0.97–47.79</td>
      <td></td>
    </tr>
    <tr>
      <td>Basophils</td>
      <td></td>
      <td></td>
      <td>0.073*</td>
      <td></td>
      <td></td>
      <td>0.419*</td>
    </tr>
    <tr>
      <td>N-Miss</td>
      <td>23</td>
      <td>19</td>
      <td></td>
      <td>4</td>
      <td>1</td>
      <td></td>
    </tr>
    <tr>
      <td>Mean (SD)</td>
      <td>0.02 (0.02)</td>
      <td>0.02 (0.02)</td>
      <td></td>
      <td>0.02 (0.04)</td>
      <td>0.02 (0.02)</td>
      <td></td>
    </tr>
    <tr>
      <td>Median(Q1, Q3)</td>
      <td>0.01(0.01, 0.02)</td>
      <td>0.01(0.01, 0.02)</td>
      <td></td>
      <td>0.02(0.01, 0.03)</td>
      <td>0.01(0.01, 0.03)</td>
      <td></td>
    </tr>
    <tr>
      <td>Range</td>
      <td>0.00–0.31</td>
      <td>0.00–0.15</td>
      <td></td>
      <td>0.00–0.84</td>
      <td>0.00–0.11</td>
      <td></td>
    </tr>
    <tr>
      <td>Basophils %</td>
      <td></td>
      <td></td>
      <td>&lt;0.001*</td>
      <td></td>
      <td></td>
      <td>0.024*</td>
    </tr>
    <tr>
      <td>N-Miss</td>
      <td>22</td>
      <td>19</td>
      <td></td>
      <td>4</td>
      <td>1</td>
      <td></td>
    </tr>
    <tr>
      <td>Mean (SD)</td>
      <td>0.00 (0.00)</td>
      <td>0.00 (0.00)</td>
      <td></td>
      <td>0.00 (0.00)</td>
      <td>0.00 (0.00)</td>
      <td></td>
    </tr>
    <tr>
      <td>Median(Q1, Q3)</td>
      <td>0.00(0.00, 0.00)</td>
      <td>0.00(0.00, 0.00)</td>
      <td></td>
      <td>0.00(0.00, 0.00)</td>
      <td>0.00(0.00, 0.00)</td>
      <td></td>
    </tr>
    <tr>
      <td>Range</td>
      <td>0.00–0.02</td>
      <td>0.00–0.06</td>
      <td></td>
      <td>0.00–0.05</td>
      <td>0.00–0.01</td>
      <td></td>
    </tr>
    <tr>
      <td>Eosinophils</td>
      <td></td>
      <td></td>
      <td>&lt;0.001*</td>
      <td></td>
      <td></td>
      <td>0.015*</td>
    </tr>
    <tr>
      <td>N-Miss</td>
      <td>23</td>
      <td>19</td>
      <td></td>
      <td>4</td>
      <td>1</td>
      <td></td>
    </tr>
    <tr>
      <td>Mean (SD)</td>
      <td>0.06 (0.12)</td>
      <td>0.04 (0.10)</td>
      <td></td>
      <td>0.06 (0.14)</td>
      <td>0.05 (0.13)</td>
      <td></td>
    </tr>
    <tr>
      <td>Median(Q1, Q3)</td>
      <td>0.01 (0.00, 0.07)</td>
      <td>0.00 (0.00, 0.02)</td>
      <td></td>
      <td>0.01 (0.00, 0.06)</td>
      <td>0.00 (0.00, 0.03)</td>
      <td></td>
    </tr>
    <tr>
      <td>Range</td>
      <td>0.00–2.19</td>
      <td>0.00–0.79</td>
      <td></td>
      <td>0.00–1.95</td>
      <td>0.00–0.97</td>
      <td></td>
    </tr>
    <tr>
      <td>Eosinophils %</td>
      <td></td>
      <td></td>
      <td>&lt;0.001*</td>
      <td></td>
      <td></td>
      <td>0.013*</td>
    </tr>
    <tr>
      <td>N-Miss</td>
      <td>22</td>
      <td>19</td>
      <td></td>
      <td>4</td>
      <td>1</td>
      <td></td>
    </tr>
    <tr>
      <td>Mean (SD)</td>
      <td>0.01 (0.02)</td>
      <td>0.00 (0.01)</td>
      <td></td>
      <td>0.01 (0.02)</td>
      <td>0.01 (0.01)</td>
      <td></td>
    </tr>
    <tr>
      <td>Median(Q1, Q3)</td>
      <td>0.00(0.00, 0.01)</td>
      <td>0.00(0.00, 0.00)</td>
      <td></td>
      <td>0.00(0.00, 0.01)</td>
      <td>0.00(0.00, 0.00)</td>
      <td></td>
    </tr>
    <tr>
      <td>Range</td>
      <td>0.00–0.27</td>
      <td>0.00–0.12</td>
      <td></td>
      <td>0.00–0.25</td>
      <td>0.00–0.07</td>
      <td></td>
    </tr>
    <tr>
      <td>Monocytes</td>
      <td></td>
      <td></td>
      <td>&lt;0.001*</td>
      <td></td>
      <td></td>
      <td>0.683*</td>
    </tr>
    <tr>
      <td>N-Miss</td>
      <td>23</td>
      <td>19</td>
      <td></td>
      <td>4</td>
      <td>1</td>
      <td></td>
    </tr>
    <tr>
      <td>Mean (SD)</td>
      <td>0.56 (0.68)</td>
      <td>0.69 (3.32)</td>
      <td></td>
      <td>0.55 (0.32)</td>
      <td>0.58 (0.41)</td>
      <td></td>
    </tr>
    <tr>
      <td>Median(Q1, Q3)</td>
      <td>0.47(0.32, 0.68)</td>
      <td>0.41(0.25, 0.63)</td>
      <td></td>
      <td>0.49(0.33, 0.68)</td>
      <td>0.48(0.27, 0.77)</td>
      <td></td>
    </tr>
    <tr>
      <td>Range</td>
      <td>0.01–23.31</td>
      <td>0.02–66.34</td>
      <td></td>
      <td>0.02–2.45</td>
      <td>0.07–2.01</td>
      <td></td>
    </tr>
    <tr>
      <td>Monocytes %</td>
      <td></td>
      <td></td>
      <td>&lt;0.001*</td>
      <td></td>
      <td></td>
      <td>0.034*</td>
    </tr>
    <tr>
      <td>N-Miss</td>
      <td>22</td>
      <td>19</td>
      <td></td>
      <td>4</td>
      <td>1</td>
      <td></td>
    </tr>
    <tr>
      <td>Mean (SD)</td>
      <td>0.08 (0.04)</td>
      <td>0.07 (0.05)</td>
      <td></td>
      <td>0.08 (0.04)</td>
      <td>0.07 (0.05)</td>
      <td></td>
    </tr>
    <tr>
      <td>Median(Q1, Q3)</td>
      <td>0.07 (0.05, 0.10)</td>
      <td>0.06 (0.04, 0.08)</td>
      <td></td>
      <td>0.07 (0.05, 0.10)</td>
      <td>0.06 (0.04, 0.09)</td>
      <td></td>
    </tr>
    <tr>
      <td>Range</td>
      <td>0.00–0.70</td>
      <td>0.01–0.72</td>
      <td></td>
      <td>0.01–0.31</td>
      <td>0.01–0.27</td>
      <td>p-Value</td>
    </tr>
    <tr>
      <td>Ferritin F</td>
      <td>613 patients(82.39%)</td>
      <td>131 patients(17.61%)</td>
      <td>&lt;0.001*</td>
      <td>240 patients(90.23%)</td>
      <td>26 patients(9.77%)</td>
      <td>0.372*</td>
    </tr>
    <tr>
      <td>N-Miss</td>
      <td>158</td>
      <td>34</td>
      <td></td>
      <td>43</td>
      <td>5</td>
      <td></td>
    </tr>
    <tr>
      <td>Mean (SD)</td>
      <td>674.53 (817.61)</td>
      <td>1237.07 (2308.64)</td>
      <td></td>
      <td>564.63 (526.39)</td>
      <td>2006.00 (4680.23)</td>
      <td></td>
    </tr>
    <tr>
      <td>Median(Q1, Q3)</td>
      <td>459.00(212.00, 820.50)</td>
      <td>700.00(353.00, 1347.00)</td>
      <td></td>
      <td>433.00(216.00, 750.00)</td>
      <td>510.00(269.00, 722.00)</td>
      <td></td>
    </tr>
    <tr>
      <td>Range</td>
      <td>4.00–7687.00</td>
      <td>19.00–20,572.00</td>
      <td></td>
      <td>11.00–3397.00</td>
      <td>81.00–20,941.00</td>
      <td></td>
    </tr>
    <tr>
      <td>Ferritin M</td>
      <td>1070 patients(78.56%)</td>
      <td>292 patients(21.44%)</td>
      <td>&lt;0.001*</td>
      <td>354 patients(90.23%)</td>
      <td>56 patients(9.77%)</td>
      <td>0.007*</td>
    </tr>
    <tr>
      <td>N-Miss</td>
      <td>257</td>
      <td>96</td>
      <td></td>
      <td>50</td>
      <td>5</td>
      <td></td>
    </tr>
    <tr>
      <td>Mean (SD)</td>
      <td>1353.00 (1359.86)</td>
      <td>1825.25 (1945.47)</td>
      <td></td>
      <td>1181.95 (3295.92)</td>
      <td>1372.04 (1258.14)</td>
      <td></td>
    </tr>
    <tr>
      <td>Median(Q1, Q3)</td>
      <td>939.00(461.00, 1705.00)</td>
      <td>1262.50(572.25, 2323.25)</td>
      <td></td>
      <td>737.50(405.25, 1283.00)</td>
      <td>1159.00(598.00, 1500.00)</td>
      <td></td>
    </tr>
    <tr>
      <td>Range</td>
      <td>23.00–11,513.00</td>
      <td>55.00–13,289.00</td>
      <td></td>
      <td>25.00–56,039.00</td>
      <td>112.00–7058.00</td>
      <td></td>
    </tr>
  </tbody>
</table>

_In bold and italics p-values < 0.05.*Wilcoxon rank-sum test.†Fisher’s exact test._

The second-wave subsample contained 676 COVID-19 patients hospitalized in MD 2020 at SCBH: 266 females (39.3%), 410 males (60.7%) (Table 1). During the 8 months of the second wave, 82 patients died (12.13%): 26 females (31.7%) and 56 males (68.3%). The mean age of deceased patients was 76.72 ± 10.79 vs. 65.30 ± 15.20 for surviving patients (p-value < 0.001). The mean hospital stay was 15.35 ± 11.58 days (from a minimum of 0 to a maximum 79 days): 17.77 ± 10.75 days for patients who died, 14.95 ± 11.67 days for surviving patients (p-value = 0.008).

The descriptive statistics for all variables in the dataset are presented in Supplementary file 1b and were computed and stratified by the two waves (MA vs. MD) and by outcome (alive vs. dead). The two subsets were similar for most variables.

The correlations between the 17 analytes and the Brescia X-ray score were investigated using Spearman correlation coefficients and visualized using a correlation plot (Figure 2). The Brescia X-ray score was positively correlated with neutrophil to lymphocyte ratio (NLR), CRP, LDH, standardized ferritin, and D-dimer, and was negatively correlated with lymphocyte %, monocyte %, and basophil %.

![Figure 2.](https://cdn.elifesciences.org/articles/70640/elife-70640-fig2-v3.jpg)

**Figure 2.:** The relationships between 17 analytes and Brescia chest X-ray score are inspected with the Spearman correlation coefficients, ρs, which are represented in this correlation plot by means of blue and red circles (positive and negative correlation, respectively). The diameter of the circle is proportional to the magnitude of ρs and black crosses on them identify correlation not significantly different from zero (p-values > 0.05). The correlation matrix is reordered according to the hierarchical cluster analysis on the quantitative variables.

### BS-EWM

A machine-learning model (BS-EWM) was developed by inputting a dataset of 2782 COVID-19 patients admitted to the ED and hospitalized at SCBH from March to December 2020. The majority of patients (2106/2782, 75.70%) belonged to the first wave (MA), the remaining fraction (676/2782, 24.30%) to the second wave (MD). As outcome, the machine-learning model had the condition dead/alive, and, as covariates: age, Brescia X-ray score, and 17 blood sample analytes.

Figure 1 reports the flowchart that describes how data were divided for training, validation, and testing the BS-EWM.

The synthetic minority oversampling technique (SMOTE) procedure, rebalancing the dead/alive ratio (50% vs. 50%) from the original 20.09%, improved accuracy, specificity, and sensitivity of the random forest applied on it (see Supplementary file 1c which compares performance metrics with/without the SMOTE method).

The relative variable importance measure (rel VIM) and partial dependence plot (PDP) were extracted from the random forests (Figures 3 and 4, respectively). In Figure 3, the rel VIM of BS-EWM based on age, Brescia X-ray score, and 17 blood analytes are reported on a bar plot. Since age was strongly associated with the risk of death, it masked the role of the other covariates. For completeness, the relevance of the 17 analytes and Brescia X-ray score was estimated in an additional EWM, in which the covariate ‘age’ was excluded. In Figure 4, 9/17 analytes and the Brescia X-ray score were noted as being important in predicting the risk of death (rel VIM >60). The effects of changes in covariate values on the risk of death threshold of the EWM were reported by means of a PDP (a 2D plot in the x–y plane) (Figure 4). Only fibrinogen was excluded from this graphical representation since in Table 1, it was not significantly different in the two subpopulations deceased/alive. Most PDPs showed nonmonotonic increasing relationships between the x-variable and the EWM, resulting in a plateau corresponding to high values of x.

![Figure 3.](https://cdn.elifesciences.org/articles/70640/elife-70640-fig3-v3.jpg)

**Figure 3.:** In , Figure 3, A1, there is the rel VIM based on Gini index. It was extracted from a random forest where the outcome is dead/alive and covariates are: the 17 biomarkers, Brescia X-ray score, and age. The algorithm grows 10,000 trees where the number of splitting variables at each tree node is √(# covariates in the model). Missing values are imputed with the ‘on-the-fly-imputation’ algorithm. A model with the same features was run (Figure 3, A2) excluding the covariate ‘age’ since it was strongly associated with the risk of death, masking the role of remaining covariates.

![Figure 4.](https://cdn.elifesciences.org/articles/70640/elife-70640-fig4-v3.jpg)

**Figure 4.:** Considering the random forest that excludes the ‘age’ variable, the PDPs were computed in correspondence of covariates with relative variable importance measure (rel VIM) of Appendix 1—figure 2 > 60 (cut-off identified by the red dashed line) and p-value in Table 1 < 0.05. Of 10 most important variables in Appendix 1—figure 2, nine satisfy these two conditions (only fibrinogen was excluded since it was not significantly different in the two subpopulations deceased/alive). PDPs measure the effects of changes in covariate values taken one per time, on the risk of death. They are displayed from the most to the less important variable.

When compared to other models such as gradient boosting machine (GBM) and logistic regression, the random forest showed better performance in terms of area under the curve (AUC), sensitivity, and specificity. The in-sample sensitivity (0.93) yielded by the model was the highest, and it maintained an important 0.82 in validating the out-of-sample sensitivity, and this decreased to 0.73 when testing the MD subgroup (see Table 2 which contains details on all the metrics extracted from the ROC analysis). ROC curves are visualized in Figure 5 where, for each model (random forest, GBM, and logistic regression), the performances in training, validating, and testing are compared in a unique graph.

![Figure 5.](https://cdn.elifesciences.org/articles/70640/elife-70640-fig5-v3.jpg)

**Figure 5.:** ROC curves of three methods: (i) random forest, (ii) GBM, and (iii) logistic regression. Each graph reports the ROC curve computed in training (blue line, 70% of March–April’s patients), validating (dashed red line, 30% of March–April’s patients), and testing (dashed green lined, May–December’s patients).

**Table 2.**
 Performance metrics of methods: random forest, gradient boosting machine (GBM), and logistic regression.


<table>
  <thead>
    <tr>
      <th rowspan="2">Metrics</th>
      <th colspan="3">Random forest</th>
      <th colspan="3">GBM</th>
      <th colspan="3">Logistic regression</th>
    </tr>
    <tr>
      <th>TrainingMarch–April (MA)</th>
      <th>ValidatingMarch–April (MA)</th>
      <th>TestingMay–Dec(MD)</th>
      <th>TrainingMarch–April (MA)</th>
      <th>ValidatingMarch–April (MA)</th>
      <th>TestingMay–Dec(MD)</th>
      <th>TrainingMarch–April (MA)</th>
      <th>ValidatingMarch–April (MA)</th>
      <th>TestingMay–Dec(MD)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AUC (DeLong)(95% CI)</td>
      <td>0.97(0.97–0.98)</td>
      <td>0.83(0.80–0.87)</td>
      <td>0.78(0.73–0.84)</td>
      <td>0.88(0.86–0.89)</td>
      <td>0.84(0.80–0.88)</td>
      <td>0.78(0.73–0.83)</td>
      <td>0.84(0.82–0.86)</td>
      <td>0.83(0.79–0.87)</td>
      <td>0.52(0.44–0.60)</td>
    </tr>
    <tr>
      <td>Sensitivity(95% CI)</td>
      <td>0.93(0.91–0.97)</td>
      <td>0.82(0.72–0.92)</td>
      <td>0.73(0.54–1.00)</td>
      <td>0.85(0.80–0.88)</td>
      <td>0.80(0.66–0.90)</td>
      <td>0.77(0.65–0.94)</td>
      <td>0.80(0.77–0.84)</td>
      <td>0.84(0.76–0.91)</td>
      <td>0.87(0.18–1.00)</td>
    </tr>
    <tr>
      <td>Specificity(95% CI)</td>
      <td>0.92(0.88–0.94)</td>
      <td>0.75(0.63–0.83)</td>
      <td>0.73(0.41–0.89)</td>
      <td>0.77(0.73–0.81)</td>
      <td>0.75(0.65–0.87)</td>
      <td>0.71(0.50–0.79)</td>
      <td>0.74(0.70–0.77)</td>
      <td>0.73(0.65–0.79)</td>
      <td>0.26(0.11–0.94)</td>
    </tr>
  </tbody>
</table>

_Comparison between the performances of three methods: random forest, GBM, and logistic regression model applied on the rebalanced dataset obtained with SMOTE methodology. Logistic regression predictions are computed using the 10-fold cross-validation in order to be comparable with random forest and GBM predictions (which use out-of-bag and 10-fold cross-validation, respectively)._

In order to compare the BS-EWM score with univariate models based on single biomarkers, three random forest (on training, validation, and testing) are estimated on the most important biomarkers (LDH, D-dimer, neutr/lymph, neutrophils %, fibrinogen, CRP, Brescia chest X-ray, lymphocytes %, ferritin std, monocytes %). Results of these 30 models are reported in Supplementary file 1d. It is evident that considering one biomarker per time, the model provides good predictions in training, but bad performances out of sample (contrary to the BS-EWM score it loses its predictive power on fresh data). Hence, it is evident that a score based on a multivariate model provide better results since it also considers interactions among variables.

## Discussion

The dataset for the development, validation, and testing of the BS-EWM originated entirely from an Italian region, potentially limiting the generalizability of the risk score in other areas of the world. Additional validation studies from different geographic areas are welcomed. Furthermore, though the BS-EWM has been validated using blood sample values obtained by instruments that satisfy internal and external quality control, different equipment could lead to divergent results (Martens et al., 2021; Lippi et al., 2020). Therefore, it would be appropriate to harmonize the results. Another limit could have been the presence of missing values, though the BS-EWM has also performed adequately in this condition since it used a multiple imputation technique to overcome the problem. Finally, it is important to point out that the BS-EWM risk score should not be used for asymptomatic COVID-19 patients or for the pediatric population. It will be interesting, in the future, to verify if the BS-EWM could be applied by general practitioners to the unhospitalized population. This could allow the generalizability of the model outside the hospital context to be tested.

Though the BS-EWM has been developed on a cohort of 2106 patients belonging to the COVID-19 first wave, the model also demonstrated a sensitivity greater than 70% in the early prediction of high risk in patients in the second wave, when in-hospital mortality was 40% lower.

Several predictive models have recently been applied to COVID-19 cohorts with variable results, some of them previously developed to predict mortality for community-acquired pneumonia, such as the Pneumonia Severity Index, CURB-65, qSOFA, and MuLBSTA (Genc Yavuz et al., 2021; Lazar Neto et al., 2021; Artero et al., 2021), NEWS2 criteria (Myrstad et al., 2020; Gidari et al., 2020), and SCAP score (Anurag and Preetam, n.d.). Novel early-warning scores have been specifically built on COVID-19 patient series using different techniques such as parametric and non-parametric tests (Linssen et al., 2020) or artificial intelligence techniques such as the COVID-GRAM score (Liang et al., 2020).

While these models are mostly based on age and a set of vital (clinical) parameters, in addition to age, the BS-EWM depends on blood parameters. It is conceivable that blood analytes capture a snapshot at hospital admission signaling a specific bodily reaction to viral infection in terms of hyperinflammation, immune response, and thrombophilia. On the other hand, the other models are more influenced by the general status of the patient, which may be determined by concomitant and pre-existing diseases.

According to the International Federation of Clinical Chemistry (Bohn et al., 2020), no single biochemical or hematological marker is sufficiently sensitive or specific to predict the outcome of SARS-CoV-2 infection. Notably, the IFCC recommends that the interpretation of laboratory abnormalities should be based on groups of analytes (Bohn et al., 2020). In the BS-EWM, three analytes reached a significant value in predicting death: LDH, D-dimer, and NLR. LDH is a non-specific indicator of tissue damage (Bohn et al., 2020; Liang et al., 2020) that emerges as one of the most consistently elevated markers in patients at higher risk of developing adverse outcomes, probably because COVID-19 infection is characterized by systemic tissue damage. Another key feature of SARS-CoV-2 is the coagulopathy: high levels of D-dimers have been reported to correlate with unfavorable disease progression in several cohorts of patients. The coagulopathy linked to COVID-19 infection is likely to involve a complex interplay between pro-thrombotic and inflammatory factors, thus the combined analysis of both inflammatory and thrombophilic markers could play an important role in the early identification of patients at higher risk of unfavorable progression (Bohn et al., 2020; Lazzaroni et al., 2021). Finally, lymphopenia has become a hallmark of SARS-CoV-2. It has been demonstrated in almost all symptomatic patients, though in varying degrees. Disease severity has been correlated with the level of lymphocyte count reduction. A direct infection of lymphocytes, which express the coronavirus receptor ACE-2, is among the mechanisms proposed. A poor prognosis is also associated with an elevated neutrophil count combined with lymphopenia, resulting in a high NLR. The increase in granulocytes is the result of the cytokine storm induced by the virus and is responsible for tissue damage (Bonetti et al., 2020; Bohn et al., 2020).

A further remark concerning the blood analytes is that, in the BS-EWM, the thresholds of the single analytes (namely the point where the functions in Figure 4 become constant and the probability of death no longer increases/decreases) closely overlap with the values recently proposed by other authors (Webb et al., 2020; Caricchio et al., 2021). For completeness, the optimal threshold (computed through the Youden index) for each biomarker to predict the outcome (dead or alive) are reported in Supplementary file 1e.

The present study is not unique in encompassing radiological findings combined with blood analysis. The study by Schalekamp et al., 2021, integrated blood analysis parameters and radiological information derived by grading chest X-rays (0–8 scale points). Unlike the cited study, with the BS-EWM in this study, the radiological score did not reach a high relevance (rel VIM) in predicting high risk. This difference can be explained by the different approaches used to build the model (logistic regression vs. random forests) and by the high degree of correlation of the X-ray score with multiple blood analytes: ‘collinearity’ thus could have ‘stolen’ importance from the information provided by imaging. Nevertheless, at admission, the chest X-ray score of patients who subsequently died was significantly higher than for patients who survived. Furthermore, the chest X-ray score may provide additional stability to the model, playing an important role in the case of missing data in the blood sample counterpart.

Further, the BS-EWM delivers high prediction performance and only requires a limited number of readily available variables with easy operability, no time consuming, no extra money since these analytes are required for COVID-19 diagnosis and monitoring. An important and pragmatic aspect offered by the BS-EWM is that the biomarkers employed may be obtained by the emergency laboratory in less than an hour (Garrafa et al., 2020a) and, differently from other biomarkers (Kyriazopoulou et al., 2021), they are non-expensive and frequently used also in developing countries. It is important to note that the same methodology could be applied to other infections and be practical to triage people.

Most laboratories, including the small or peripheral ones, may provide results in a short time. At the Spedali Civili of Brescia, the BS-EWM is integrated within the Laboratory Information System (LIS). It works as a web-based calculator and is easy to interpret. The online calculator allows an easy assessment of the EWM, requiring only the entering of analyte values and X-ray score. The score is calculated even if some of the values are missing. Furthermore, in our center the system may be integrated with the electronic health record and the radiology information system, allowing a completely automatic data retrieval and entering, without any operator interaction. It provides a risk threshold of 0.5, above which patients are graded as having a potentially high death-risk, thus supporting closer clinical observation or admission to a high-intensive care ward. In patients yielding a low risk (score 0–0.49), the decision by clinicians to allocate them to a low-intensive care ward or to monitoring is further sustained. The online calculator allows an easy assessment of the EWM, requiring only the entering of analyte values and X-ray score. The score is calculated even if some of the values are missing. Furthermore, in our center the system may be integrated with the electronic health record and the radiology information system, allowing a completely automatic data retrieval and entering, without any operator interaction.

Finally, the need to regularly update models and closely monitor their performances over time and geographically should be underlined, given the rapidly changing nature of the disease and its management.

## Materials and methods

The dataset contained 2782 COVID-19 symptomatic patients, hospitalized between March and December 2020 at SCBH after referring to the ED. In all patients, the following variables were retrieved from the SCBH database: age, sex, length of hospitalization, Brescia X-ray score (Borghesi and Maroldi, 2020), alive/dead, and 17 blood analytes acquired at admission (D-dimer, fibrinogen, LDH, neutrophils, lymphocytes, NLR, lymphocytes %, neutrophils %, CRP, white blood cell (WBC) count, basophils, basophils %, eosinophils, eosinophils %, monocytes, monocytes %, standardized ferritin). Blood tests were acquired within 24 hr after admission to the hospital.

According to the two temporal peaks of incidence of the COVID-19 outbreak in Lombardy, the 2782 patients were divided into two groups: (i) MA including 2106 patients admitted during the first wave; (ii) MD including 676 patients in the second wave. Quantitative variables were described using mean (SD), median (IQR), and range (min–max), while categorical variables were reported as counts and percentages. The comparisons between groups were performed using the Wilcoxon rank-sum test for quantitative variables and Fisher’s exact test for qualitative variables.

The relationships between the 17 analytes and the Brescia X-ray score were inspected using the Spearman correlation coefficient, ρs, and visualizing results using a correlation plot (Dancelli et al., 2013; Marziano et al., 2019; Figure 2).

To estimate the BS-EWM, the outcome (alive/dead) was modeled using as covariates: (i) Brescia X-ray score, (ii) 17 analytes, (iii) age. Since most of the covariates analyzed were strongly correlated (multi-collinearity) (Figure 2) and their relationships with the outcome were non-linear, the BS-EWM was estimated using random forests (Breiman, 2001; Carpita and Vezzoli, 2012), a non-parametric machine-learning method (Vezzoli, 2011; Vezzoli et al., 2017). Moreover, the algorithm is able to manage missing values which are common in clinical studies. The ‘on-the-fly-imputation’ algorithm (Hong and Lynn, 2020) imputes data when it grows the forest handling interactions and non-linearity in the dataset.

Since the prevalence rate of death in the two waves was different (20% in MA vs. 12% in MD), a strategy to generalize results in unbalanced datasets was applied, adopting a rebalancing method able to improve the detection of patients with a high death-risk.

The EWM was developed using the 2106 patients in the first COVID-19 wave (MA 2020) when in-hospital death prevalence was 20%. Seventy percent of them (1474 patients) were used for training the model and the remainder (632 patients) for testing it. Patients were randomly assigned to the two subgroups, and further stratified according to the outcome (alive/dead). Consequently, both the training and testing subgroups included the same rate of deaths (20.09%) as the full sample (2106 patients). With such a ‘moderate’ incidence of death, the dataset was statistically unbalanced. This limitation could have implied the development of a model yielding unsatisfactory results in predicting new observations for the minority class, that is, patients with death as outcome. An approach to address this limitation is to oversample the minority class (deceased patients) and, subsequently, create the predictive model (BS-EWM). The SMOTE (Chawla et al., 2002) was chosen. The SMOTE function oversamples the minority class by using bootstrapping and k-nearest neighbor to synthetically create additional observations belonging to that class (dead). The procedure is combined with under-sampling of the majority class (alive). To determine the optimum number of k-groups into which to assign the dataset, a matrix containing the 17 analytes and the Brescia X-ray score was used to compute the hierarchical cluster analysis (Salvi et al., 2019; Codenotti et al., 2016). By means of silhouette analysis, k = 2 was determined as the optimal number of clusters into which to assign the dataset. Hence, a synthetic rebalanced dataset was obtained with an equal number of living and deceased patients (888 + 888). The rebalancing procedure enabled a risk score to be devised ranging from 0 to 1 with a threshold of 0.5 to separate non-severely affected from severely affected patients. Subsequently, the model was tested on the subgroup of 632 patients in the first wave excluding the training set. A further validation of the EWM was conducted on the 676 COVID-19 patients in the second wave (Wynants et al., 2020).

The rel VIM (Carpita and Vezzoli, 2012, Doglietto et al., 2020b) and the PDP (Friedman, 2001; Doglietto et al., 2020a) were extracted from the model for a better understanding of the relationship between outcome and covariates.

The predictions extracted from the random forests classification were interpreted as in-hospital death probability conditional on the combination of the values of analytes, Brescia X-ray score, and age in COVID-19 patients at admission to the ED.

The BS-EWM performance was evaluated by AUC of an ROC curve. The robustness of the model was compared to other models by running GBM (a machine-learning approach and competitor to random forests), and logistic regression, and computing the same metrics.

The BS-EWM score is available for use online (https://bdbiomed.shinyapps.io/covid19score). In the SCBH it is integrated within LIS returning the death-risk score directly from the medical report.

All the analyses were performed by R, version 4.0.0 (R Development Core Team, 2020). The code is available at 288 https://github.com/biostatUniBS/BS_EWS copy archived at swh:1:rev:7416ba71075402e6a0ed997e7aa6a527e93247b2 (Garrafa et al., 2021).
