# Inference from longitudinal laboratory tests characterizes temporal evolution of COVID-19-associated coagulopathy (CAC)

## Authors

- Colin Pawlowski<sup>1</sup> ([ORCID: 0000-0003-2781-7507](https://orcid.org/0000-0003-2781-7507))
- Tyler Wagner<sup>1</sup>
- Arjun Puranik<sup>1</sup>
- Karthik Murugadoss<sup>1</sup>
- Liam Loscalzo<sup>1</sup>
- AJ Venkatakrishnan<sup>1</sup>
- Rajiv K Pruthi<sup>2</sup>
- Damon E Houghton<sup>2</sup>
- John C O'Horo<sup>2</sup>
- William G Morice<sup>2</sup>
- Amy W Williams<sup>2</sup>
- Gregory J Gores<sup>2</sup>
- John Halamka<sup>2</sup>
- Andrew D Badley<sup>2</sup>
- Elliot S Barnathan<sup>5</sup>
- Hideo Makimura<sup>5</sup>
- Najat Khan<sup>5</sup>
- Venky Soundararajan<sup>1</sup> ([ORCID: 0000-0001-7434-9211](https://orcid.org/0000-0001-7434-9211)) †

### Affiliations

1. nference, inc Cambridge United States
2. Mayo Clinic Rochester United States
3. Mayo Clinic Laboratories Rochester United States
4. Mayo Clinic Platform Rochester United States
5. Janssen pharmaceutical companies of Johnson & Johnson (J&J) Spring House United States

† Corresponding author

## Abstract

Temporal inference from laboratory testing results and triangulation with clinical outcomes extracted from unstructured electronic health record (EHR) provider notes is integral to advancing precision medicine. Here, we studied 246 SARS-CoV-2 PCR-positive (COVIDpos) patients and propensity-matched 2460 SARS-CoV-2 PCR-negative (COVIDneg) patients subjected to around 700,000 lab tests cumulatively across 194 assays. Compared to COVIDneg patients at the time of diagnostic testing, COVIDpos patients tended to have higher plasma fibrinogen levels and lower platelet counts. However, as the infection evolves, COVIDpos patients distinctively show declining fibrinogen, increasing platelet counts, and lower white blood cell counts. Augmented curation of EHRs suggests that only a minority of COVIDpos patients develop thromboembolism, and rarely, disseminated intravascular coagulopathy (DIC), with patients generally not displaying platelet reductions typical of consumptive coagulopathies. These temporal trends provide fine-grained resolution into COVID-19 associated coagulopathy (CAC) and set the stage for personalizing thromboprophylaxis.

## Introduction

There is a growing body of evidence suggesting that severe COVID-19 outcomes may be associated with dysregulated coagulation (Tang et al., 2020), including stroke, pulmonary embolism, myocardial infarction, and other venous or arterial thromboembolic complications (Klok et al., 2020). This so-called COVID-19 associated coagulopathy (CAC) shares similarities with disseminated intravascular coagulation (DIC) and thrombotic microangiopathy but also has distinctive features (Levi et al., 2020). Given the significance of CAC to COVID-19 mortality, there is an urgent need for fine-grained resolution into the temporal manifestation of CAC, particularly in comparison to the broad-spectrum of other, better characterized coagulopathies. While there are studies suggesting associations between COVID-19 infection and mortality with thrombocytopenia, D-dimer levels, and prolongation of prothrombin time, the signatures of CAC onset and progression as well as their connection to clinical outcomes are not well defined (Tang et al., 2020; Gao et al., 2020; Panigada et al., 2020). An advanced understanding of this phenotype may aid in the risk stratification of patients, thus facilitating optimal monitoring strategies during disease evolution through the paradigm of precision medicine.

To this end, we instituted a holistic data science platform across an academic medical center that enables machine intelligence to augment the curation of phenotypes and outcomes from over 10 million electronic health record (EHR) clinical notes and associated 3.2 million lab tests from 2232 SARS-CoV-2 positive (COVIDpos) and 72,354 confirmed SARS-CoV-2 negative (COVIDneg) patients over a retrospectively defined 2-month observation period straddling the date of the PCR test. For the COVIDpos cohort, we center the 2-month observation period around the date of the first positive PCR test for SARS-CoV-2, and for the COVIDneg cohort, we center the 2-month observation period around the date of the first PCR test for SARS-CoV-2 (see Materials and methods). It is important to note that not all individuals infected by SARS-CoV-2 develop symptoms of COVID-19, but rather that a majority of patients are either asymptomatic or have mild-to-moderate symptoms not requiring hospitalization for COVID-19 (Wagner et al., 2020). Furthermore, the guidelines followed for PCR-testing included a routine screening of individuals, patients displaying COVID-19 symptoms as per the Mayo Clinic (Coronavirus disease, 2019) and CDC definitions (Website, 2020), and possibly contact with infected persons or underlying predisposing conditions (Wagner et al., 2020).

By compiling all available laboratory testing data for the 30 days preceding the first SARS-CoV-2 PCR positive diagnostic testing date (day 0), as well as the 30 days following the diagnostic testing date, and triangulating this information with medications and clinical outcomes, we were able to identify laboratory abnormalities significantly associated with the COVIDpos group. We identified coagulation-related parameters among this set of abnormalities and then studied aggregate as well as individual patient trajectories that could aid in extracting a temporal signature of CAC onset and progression. We also correlated these signals with the clinical outcomes of these patients.

In order to hone into longitudinal lab test trends that would apply at the individual patient level, we restricted our analysis to patients with available serial testing data, which had at least three test results of the same type during the observation period. After applying these inclusion criteria, 246 COVIDpos and 13,666 COVIDneg patients met study the inclusion criteria. The need for longitudinal data on the testing results, while constraining the study population size greatly, enables us to provide a fine-grained temporal resolution of CAC for the first time.

After filtering the patients with the available longitudinal testing data, the median age in the COVIDpos and COVIDneg groups were 60.8 years and 64.1 years, respectively (see Materials and methods and Table 1), and the numbers of males were 137 (56%) and 7129 (52%), respectively. The total numbers of pre-existing coagulopathies in the COVIDpos and COVIDneg groups were 31 (13%) and 3901 (29%), respectively. These counts of coagulopathies include the following phenotypes identified in the clinical notes from day −365 to day −31 relative to the PCR testing date: deep vein thrombosis, pulmonary embolism, myocardial infarction, venous thromboembolism, thrombotic stroke, cerebral venous thrombosis, and disseminated intravascular coagulation (see Table 1 for detailed breakdown). The number of COVIDpos patients hospitalized in the month prior to the SARS-CoV-2 PCR testing date was 41 (17%), compared to 1247 (9.1%) for the COVIDneg cohort.

**Table 1.**
 Summary of patient characteristics for the overall COVIDpos, COVIDneg (matched), and COVIDneg cohorts.The COVIDneg (matched) cohort was constructed using 1:10 propensity score matching to balance each of the clinical covariates, including demographics (age, gender, race), medication use (anticoagulant/antiplatelet use in the preceding 30 days/1 year of PCR testing date), medical history of thrombotic events from the past year, and hospitalization status in the month prior to the date of PCR testing.


<table>
  <thead>
    <tr>
      <th>Patient characteristics</th>
      <th>COVIDpos</th>
      <th>COVIDneg (matched)</th>
      <th>COVIDneg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Number of patients</td>
      <td>246</td>
      <td>2460</td>
      <td>13,666</td>
    </tr>
    <tr>
      <td>Age in years</td>
      <td>60.8</td>
      <td>60.9</td>
      <td>64.1</td>
    </tr>
    <tr>
      <td colspan="4">Gender:</td>
    </tr>
    <tr>
      <td>Male</td>
      <td>137 (56%)</td>
      <td>1388 (56%)</td>
      <td>7129 (52%)</td>
    </tr>
    <tr>
      <td colspan="4">Race:</td>
    </tr>
    <tr>
      <td>White</td>
      <td>154 (63%)</td>
      <td>1540 (63%)</td>
      <td>12,241 (90%)</td>
    </tr>
    <tr>
      <td>Black</td>
      <td>24 (9.8%)</td>
      <td>313 (13%)</td>
      <td>569 (4.2%)</td>
    </tr>
    <tr>
      <td>Asian</td>
      <td>18 (7.3%)</td>
      <td>207 (8.4%)</td>
      <td>274 (2.0%)</td>
    </tr>
    <tr>
      <td>American Indian</td>
      <td>23 (9.3%)</td>
      <td>81 (3.3%)</td>
      <td>81 (0.59%)</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>27 (11%)</td>
      <td>319 (13%)</td>
      <td>501 (3.7%)</td>
    </tr>
    <tr>
      <td colspan="4">Medication use in the preceding 30 days of PCR testing date:</td>
    </tr>
    <tr>
      <td>Anticoagulants</td>
      <td>63 (26%)</td>
      <td>596 (24%)</td>
      <td>5171 (38%)</td>
    </tr>
    <tr>
      <td>Antiplatelets</td>
      <td>30 (12%)</td>
      <td>298 (12%)</td>
      <td>2230 (16%)</td>
    </tr>
    <tr>
      <td colspan="4">Medication use in the preceding 1 year of PCR testing date:</td>
    </tr>
    <tr>
      <td>Anticoagulants</td>
      <td>86 (35%)</td>
      <td>819 (33%)</td>
      <td>7476 (55%)</td>
    </tr>
    <tr>
      <td>Antiplatelets</td>
      <td>40 (16%)</td>
      <td>419 (17%)</td>
      <td>3620 (26%)</td>
    </tr>
    <tr>
      <td colspan="4">Medical history of thrombotic events in 1 year prior to study period:</td>
    </tr>
    <tr>
      <td>Deep vein thrombosis</td>
      <td>15 (6.1%)</td>
      <td>153 (6.2%)</td>
      <td>2,110 (15%)</td>
    </tr>
    <tr>
      <td>Pulmonary embolism</td>
      <td>12 (4.9%)</td>
      <td>112 (4.6%)</td>
      <td>1258 (9.2%)</td>
    </tr>
    <tr>
      <td>Myocardial infarction</td>
      <td>11 (4.5%)</td>
      <td>142 (5.8%)</td>
      <td>1468 (11%)</td>
    </tr>
    <tr>
      <td>Venous thromboembolism</td>
      <td>4 (1.6%)</td>
      <td>44 (1.8%)</td>
      <td>615 (4.5%)</td>
    </tr>
    <tr>
      <td>Thrombotic stroke</td>
      <td>1 (0.41%)</td>
      <td>3 (0.12%)</td>
      <td>143 (1.0%)</td>
    </tr>
    <tr>
      <td>Cerebral venous thrombosis</td>
      <td>0</td>
      <td>1 (0.04%)</td>
      <td>7 (0.05%)</td>
    </tr>
    <tr>
      <td>Disseminated intravascular coagulation</td>
      <td>0</td>
      <td>1 (0.04%)</td>
      <td>30 (0.22%)</td>
    </tr>
    <tr>
      <td>Any thrombotic event</td>
      <td>31 (13%)</td>
      <td>308 (13%)</td>
      <td>3901 (29%)</td>
    </tr>
    <tr>
      <td>Hospitalized in the month prior to PCR testing date</td>
      <td>41 (17%)</td>
      <td>304 (12%)</td>
      <td>1247 (9%)</td>
    </tr>
  </tbody>
</table>

To balance these clinical covariates and others between the two cohorts, we applied 1:10 propensity score matching to define a subset of 2460 patients from the COVIDneg cohort to use for the final statistical analysis (see Materials and methods). In particular, the general categories of covariates considered for balancing included: demographics, anticoagulant/antiplatelet medication use, medical history of pre-existing coagulopathies, and hospital admission status. Population-level characteristics of the COVIDpos, COVIDneg, and the final propensity score-matched COVIDneg (matched) cohorts are summarized in Table 1. We observe that the COVIDpos and COVIDneg (matched) cohorts are well-balanced along these covariates which are potential confounding variables for thrombotic events and coagulopathy-related lab tests during the study period.

## Results

### Longitudinal analysis identifies lab test results characteristic of COVID-19 at specific prognostic time intervals

To identify laboratory test results that differ between COVIDpos and COVIDneg (matched) patients, we analyzed longitudinal trends of 194 laboratory test results in the 30 days before and after the day of PCR testing (designated as day 0). As most patients did not undergo laboratory testing for each assay on a daily basis, we grouped the measurements into nine time windows reflecting potential stages of infection as follows: pre-infection (days −30 to −11), pre-PCR (days −10 to −2), time of clinical presentation (days −1 to 0), and post-PCR phases 1 (days 1 to 3), 2 (days 4 to 6), 3 (days 7 to 9), 4 (days 10 to 12), 5 (days 13 to 15), and 6 (days 16 to 30). We only considered test-time window pairs in which at least three patients contributing to laboratory test results in both groups. During each time window, we then compared the distribution of results from COVIDpos versus COVIDneg (matched) patients, allowing us to identify any lab tests which were significantly altered in COVIDpos patients during any time of disease acquisition, onset, and/or progression.

Of the 1709 lab test-time window pairs with adequate data points for comparison, we identified 130 such pairs (comprising 66 unique lab tests) which met our thresholds for statistical significance (Cohen’s D >0.35, BH-adjusted Mann-Whitney p-value <0.05; Table 2). Among these were lab tests that may be considered positive controls for our analysis. From the time of clinical presentation onward, elevated titers of SARS-CoV-2 IgG antibodies (Figure 1A) and a reduction in blood oxygenation in COVIDpos patients were observed (Figure 1B). We also identified abnormalities in several other classes of lab tests, including immune cell counts (Figures 1C–E and 2A–B), red blood cell counts (Figure 2C), mean corpuscular volume (Figure 2D), calcium and magnesium levels (Figure 2E–F), and coagulation-related tests (Figure 3).

![Figure 1.](https://cdn.elifesciences.org/articles/59209/elife-59209-fig1-v2.jpg)

**Figure 1.:** Longitudinal trends in COVIDpos versus COVIDneg (matched) patients for the following lab tests: (A) SARS-CoV-2 IGG ratio, (B) oxygen saturation in arterial blood, (C) white blood cells, (D) monocytes absolute, and (E) neutrophils, blood. For any window of time during which at least three patients in each cohort had test results, data are shown as mean with standard errors. The normal range for each lab test is shaded in green. Values given horizontally along the top of the plot are Cohen’s D statistics comparing the COVIDpos and COVIDneg (matched) cohorts along with the BH-adjusted Mann-Whitney test p-values. Significant differences (adjusted p-value <0.05) are shown in black, while non-significant values are shown in gray. Values given horizontally along the bottom of the plot are the numbers of patients in the COVIDpos and COVIDneg cohorts, respectively (i.e. # COVIDpos | # COVIDneg). For certain lab tests, some data points are missing because these time windows had fewer than three data points in the COVIDpos cohort.

![Figure 2.](https://cdn.elifesciences.org/articles/59209/elife-59209-fig2-v2.jpg)

**Figure 2.:** Longitudinal trends in COVIDpos versus COVIDneg (matched) patients for the following lab tests: (A) eosinophils absolute, (B) basophils absolute, (C) red blood cell count, (D) mean corpuscular volume, (E) calcium total, plasma, and (F) magnesium total, serum/plasma. For any window of time during which at least three patients in each cohort had test results, data are shown as mean with standard errors. The normal range for each lab test is shaded in green. Values given horizontally along the top of the plot are Cohen’s D statistics comparing the COVIDpos and COVIDneg (matched) cohorts along with the BH-adjusted Mann-Whitney test p-values. Significant differences (adjusted p-value <0.05) are shown in black, while non-significant values are shown in gray. Values given horizontally along the bottom of the plot are the numbers of patients in the COVIDpos and COVIDneg cohorts, respectively (i.e. # COVIDpos | # COVIDneg). For certain lab tests, some data points are missing because these time windows had fewer than three data points in the COVIDpos cohort.

![Figure 3.](https://cdn.elifesciences.org/articles/59209/elife-59209-fig3-v2.jpg)

**Figure 3.:** Longitudinal trends of COVIDpos versus COVIDneg (matched) patients for the following lab tests: (A) fibrinogen, plasma, (B) platelets, and (C) other coagulation-related tests including prothrombin time (PT), activated partial thromboplastic time (aPTT), and D-dimers. For any window of time during which at least three patients in each cohort had test results, data are shown as mean with standard errors. The normal range for each lab test is shaded in green. Values given horizontally along the top of the plot are Cohen’s D statistics comparing the COVIDpos and COVIDneg (matched) cohorts along with the BH-adjusted Mann-Whitney test p-values. Significant differences (adjusted p-value <0.05) are shown in black, while non-significant values are shown in gray. Values given horizontally along the bottom of the plot are the numbers of patients in the COVIDpos and COVIDneg cohorts, respectively (i.e. # COVIDpos | # COVIDneg). For certain lab tests, some data points are missing because these time windows had fewer than three data points in the COVIDpos cohort.

**Table 2.**
 Summary of lab tests significantly different between COVIDpos and propensity score-matched COVIDneg cohorts during at least one clinical time window.Data from individual patients were averaged over the defined time windows, and the mean values were compared between COVIDpos and COVIDneg patients. The lab test-time window pairs shown are those which met our defined thresholds for statistical significance and substantial effect (BH-adjusted Mann-Whitney p-value <0.05 and Cohen’s D absolute value >0.35). In particular, 130 of the initial 1709 (test, time window) pairs with at least one patient met these thresholds. Rows are sorted alphabetically by test and then time window (from earliest to latest). Coagulation-related tests of particular interest (fibrinogen, platelets, prothrombin time, activated partial thromboplastin time, and D-dimer) are highlighted in gray. Sample sources are denoted as: P = plasma, S = serum, S/P = serum/plasma, B = blood, U = urine.


<table>
  <thead>
    <tr>
      <th>Test</th>
      <th>Units</th>
      <th>Time window</th>
      <th>Count COVIDpos</th>
      <th>Count COVIDneg</th>
      <th>Mean COVIDpos</th>
      <th>Mean COVIDneg</th>
      <th>Cohen's D</th>
      <th>BH-adj M-W p-value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ABGRS pH Arterial</td>
      <td>pH</td>
      <td>Days 16–30 Post-Dx</td>
      <td>18</td>
      <td>91</td>
      <td>7.45</td>
      <td>7.4</td>
      <td>0.775</td>
      <td>0.02</td>
    </tr>
    <tr>
      <td>ABGRS PO2 Arterial</td>
      <td>mm Hg</td>
      <td>Days 1–3 Post-Dx</td>
      <td>16</td>
      <td>204</td>
      <td>81.9</td>
      <td>129.6</td>
      <td>−0.797</td>
      <td>3.1E-03</td>
    </tr>
    <tr>
      <td>ABGRS PO2 Arterial</td>
      <td>mm Hg</td>
      <td>Days 4–6 Post-Dx</td>
      <td>25</td>
      <td>82</td>
      <td>78.1</td>
      <td>113.2</td>
      <td>−0.712</td>
      <td>8.8E-03</td>
    </tr>
    <tr>
      <td>ABGRS PO2 Arterial</td>
      <td>mm Hg</td>
      <td>Days 7–9 Post-Dx</td>
      <td>23</td>
      <td>58</td>
      <td>77.2</td>
      <td>121.9</td>
      <td>−0.807</td>
      <td>1.0E-03</td>
    </tr>
    <tr>
      <td>ABGRS PO2 Arterial</td>
      <td>mm Hg</td>
      <td>Days 10–12 Post-Dx</td>
      <td>18</td>
      <td>37</td>
      <td>76.4</td>
      <td>104.2</td>
      <td>−0.965</td>
      <td>2.6E-03</td>
    </tr>
    <tr>
      <td>ABGRS PO2 Arterial</td>
      <td>mm Hg</td>
      <td>Days 13–15 Post-Dx</td>
      <td>15</td>
      <td>31</td>
      <td>73.1</td>
      <td>112.3</td>
      <td>−0.964</td>
      <td>6.0E-03</td>
    </tr>
    <tr>
      <td>Activated Partial Thrombopl Time, P</td>
      <td>sec</td>
      <td>Days 7–9 Post-Dx</td>
      <td>22</td>
      <td>66</td>
      <td>50.5</td>
      <td>36.7</td>
      <td>0.727</td>
      <td>0.026</td>
    </tr>
    <tr>
      <td>Activated Partial Thrombopl Time, P</td>
      <td>sec</td>
      <td>Days 10–12 Post-Dx</td>
      <td>14</td>
      <td>54</td>
      <td>63.3</td>
      <td>39.2</td>
      <td>1.085</td>
      <td>2.4E-03</td>
    </tr>
    <tr>
      <td>Activated Partial Thrombopl Time, P</td>
      <td>sec</td>
      <td>Days 13–15 Post-Dx</td>
      <td>16</td>
      <td>48</td>
      <td>53.1</td>
      <td>37.6</td>
      <td>1.065</td>
      <td>5.6E-03</td>
    </tr>
    <tr>
      <td>Activated Partial Thrombopl Time, P</td>
      <td>sec</td>
      <td>Days 16–30 Post-Dx</td>
      <td>19</td>
      <td>149</td>
      <td>56.2</td>
      <td>37.5</td>
      <td>0.884</td>
      <td>0.027</td>
    </tr>
    <tr>
      <td>Alanine Aminotransferase (ALT), P</td>
      <td>U/L</td>
      <td>Days 10–12 Post-Dx</td>
      <td>27</td>
      <td>104</td>
      <td>77.3</td>
      <td>46</td>
      <td>0.512</td>
      <td>0.015</td>
    </tr>
    <tr>
      <td>Albumin, P</td>
      <td>g/dL</td>
      <td>Days 7–9 Post-Dx</td>
      <td>42</td>
      <td>188</td>
      <td>3.06</td>
      <td>3.41</td>
      <td>−0.54</td>
      <td>5.6E-03</td>
    </tr>
    <tr>
      <td>Albumin, S/P</td>
      <td>g/dL</td>
      <td>Clinical presentation</td>
      <td>85</td>
      <td>812</td>
      <td>3.43</td>
      <td>3.81</td>
      <td>−0.591</td>
      <td>4.8E-06</td>
    </tr>
    <tr>
      <td>Albumin, S/P</td>
      <td>g/dL</td>
      <td>Days 1–3 Post-Dx</td>
      <td>77</td>
      <td>525</td>
      <td>3.26</td>
      <td>3.6</td>
      <td>−0.541</td>
      <td>3.8E-05</td>
    </tr>
    <tr>
      <td>Albumin, S/P</td>
      <td>g/dL</td>
      <td>Days 10–12 Post-Dx</td>
      <td>61</td>
      <td>254</td>
      <td>3.35</td>
      <td>3.66</td>
      <td>−0.47</td>
      <td>2.6E-03</td>
    </tr>
    <tr>
      <td>Alkaline Phosphatase, P</td>
      <td>U/L</td>
      <td>Days 4–6 Post-Dx</td>
      <td>42</td>
      <td>139</td>
      <td>88.8</td>
      <td>126.7</td>
      <td>−0.395</td>
      <td>3.7E-03</td>
    </tr>
    <tr>
      <td>Arterial O2 PP Diff</td>
      <td>None</td>
      <td>Clinical presentation</td>
      <td>21</td>
      <td>106</td>
      <td>268.1</td>
      <td>152.1</td>
      <td>0.924</td>
      <td>9.7E-03</td>
    </tr>
    <tr>
      <td>Arterial O2 PP Diff</td>
      <td>None</td>
      <td>Days 1–3 Post-Dx</td>
      <td>22</td>
      <td>112</td>
      <td>225.9</td>
      <td>147.4</td>
      <td>0.639</td>
      <td>0.017</td>
    </tr>
    <tr>
      <td>Arterial O2 PP Diff</td>
      <td>None</td>
      <td>Days 4–6 Post-Dx</td>
      <td>17</td>
      <td>49</td>
      <td>271.4</td>
      <td>155</td>
      <td>0.891</td>
      <td>4.8E-03</td>
    </tr>
    <tr>
      <td>Aspartate Aminotransferase (AST), P</td>
      <td>U/L</td>
      <td>Days 10–12 Post-Dx</td>
      <td>27</td>
      <td>107</td>
      <td>67.6</td>
      <td>44.7</td>
      <td>0.404</td>
      <td>3.6E-04</td>
    </tr>
    <tr>
      <td>Basophils Absolute</td>
      <td>×10(9)/L</td>
      <td>Clinical presentation</td>
      <td>133</td>
      <td>1400</td>
      <td>0.0251</td>
      <td>0.0379</td>
      <td>−0.412</td>
      <td>5.8E-06</td>
    </tr>
    <tr>
      <td>Bicarbonate [MMOL/L] in Arterial Blood</td>
      <td>mmol/L</td>
      <td>Days 16–30 Post-Dx</td>
      <td>18</td>
      <td>91</td>
      <td>28.6</td>
      <td>24.3</td>
      <td>0.857</td>
      <td>7.6E-03</td>
    </tr>
    <tr>
      <td>Bicarbonate in Arterial Blood</td>
      <td>mmol/L</td>
      <td>Days 1–3 Post-Dx</td>
      <td>26</td>
      <td>193</td>
      <td>23.2</td>
      <td>21.4</td>
      <td>0.513</td>
      <td>0.027</td>
    </tr>
    <tr>
      <td>BUN, P</td>
      <td>mg/dL</td>
      <td>Days 16–30 Post-Dx</td>
      <td>49</td>
      <td>562</td>
      <td>31.4</td>
      <td>21.9</td>
      <td>0.555</td>
      <td>3.9E-03</td>
    </tr>
    <tr>
      <td>C-reactive Protein Quantative, S</td>
      <td>mg/L</td>
      <td>Clinical presentation</td>
      <td>85</td>
      <td>666</td>
      <td>100.2</td>
      <td>68.2</td>
      <td>0.375</td>
      <td>6.8E-05</td>
    </tr>
    <tr>
      <td>Calcium, Ionized, B</td>
      <td>mg/dL</td>
      <td>Clinical presentation</td>
      <td>14</td>
      <td>201</td>
      <td>4.36</td>
      <td>4.77</td>
      <td>−0.67</td>
      <td>0.015</td>
    </tr>
    <tr>
      <td>Calcium, Ionized, B</td>
      <td>mg/dL</td>
      <td>Days 1–3 Post-Dx</td>
      <td>18</td>
      <td>270</td>
      <td>4.42</td>
      <td>4.73</td>
      <td>−0.783</td>
      <td>8.5E-04</td>
    </tr>
    <tr>
      <td>Calcium, Total, P</td>
      <td>mg/dL</td>
      <td>Clinical presentation</td>
      <td>89</td>
      <td>1144</td>
      <td>8.71</td>
      <td>9.05</td>
      <td>−0.468</td>
      <td>5.5E-06</td>
    </tr>
    <tr>
      <td>Calcium, Total, P</td>
      <td>mg/dL</td>
      <td>Days 1–3 Post-Dx</td>
      <td>77</td>
      <td>910</td>
      <td>8.52</td>
      <td>8.81</td>
      <td>−0.459</td>
      <td>3.2E-04</td>
    </tr>
    <tr>
      <td>Calcium, Total, P</td>
      <td>mg/dL</td>
      <td>Days 7–9 Post-Dx</td>
      <td>71</td>
      <td>353</td>
      <td>8.61</td>
      <td>8.93</td>
      <td>−0.457</td>
      <td>1.8E-03</td>
    </tr>
    <tr>
      <td>Calcium, Total, S</td>
      <td>mg/dL</td>
      <td>Clinical presentation</td>
      <td>83</td>
      <td>941</td>
      <td>8.29</td>
      <td>8.91</td>
      <td>−0.854</td>
      <td>1.9E-13</td>
    </tr>
    <tr>
      <td>Calcium, Total, S</td>
      <td>mg/dL</td>
      <td>Days 1–3 Post-Dx</td>
      <td>98</td>
      <td>1025</td>
      <td>8.28</td>
      <td>8.77</td>
      <td>−0.717</td>
      <td>2.2E-10</td>
    </tr>
    <tr>
      <td>Calcium, Total, S</td>
      <td>mg/dL</td>
      <td>Days 4–6 Post-Dx</td>
      <td>87</td>
      <td>568</td>
      <td>8.4</td>
      <td>8.69</td>
      <td>−0.435</td>
      <td>2.3E-03</td>
    </tr>
    <tr>
      <td>Calcium, Total, S</td>
      <td>mg/dL</td>
      <td>Days 7–9 Post-Dx</td>
      <td>82</td>
      <td>433</td>
      <td>8.49</td>
      <td>8.76</td>
      <td>−0.384</td>
      <td>0.011</td>
    </tr>
    <tr>
      <td>Carboxyhemoglobin, ARTERIAL</td>
      <td>%</td>
      <td>Clinical presentation</td>
      <td>34</td>
      <td>356</td>
      <td>0.507</td>
      <td>0.991</td>
      <td>−0.71</td>
      <td>2.0E-04</td>
    </tr>
    <tr>
      <td>Carboxyhemoglobin, Arterial</td>
      <td>%</td>
      <td>Days 1–3 Post-Dx</td>
      <td>44</td>
      <td>436</td>
      <td>0.535</td>
      <td>0.9</td>
      <td>−0.711</td>
      <td>5.9E-05</td>
    </tr>
    <tr>
      <td>Carboxyhemoglobin, Arterial</td>
      <td>%</td>
      <td>Days 4–6 Post-Dx</td>
      <td>58</td>
      <td>166</td>
      <td>0.678</td>
      <td>0.974</td>
      <td>−0.544</td>
      <td>3.0E-03</td>
    </tr>
    <tr>
      <td>Carboxyhemoglobin, Arterial</td>
      <td>%</td>
      <td>Days 7–9 Post-Dx</td>
      <td>45</td>
      <td>102</td>
      <td>0.704</td>
      <td>0.97</td>
      <td>−0.472</td>
      <td>0.048</td>
    </tr>
    <tr>
      <td>Carboxyhemoglobin, Venous</td>
      <td>%</td>
      <td>Days 1–3 Post-Dx</td>
      <td>10</td>
      <td>73</td>
      <td>0.701</td>
      <td>1.16</td>
      <td>−0.862</td>
      <td>0.02</td>
    </tr>
    <tr>
      <td>Carboxyhemoglobin, Venous</td>
      <td>%</td>
      <td>Days 4–6 Post-Dx</td>
      <td>14</td>
      <td>47</td>
      <td>0.725</td>
      <td>1.29</td>
      <td>−0.837</td>
      <td>3.7E-03</td>
    </tr>
    <tr>
      <td>Chloride, P</td>
      <td>mmol/L</td>
      <td>Days 1–3 Post-Dx</td>
      <td>77</td>
      <td>906</td>
      <td>100.1</td>
      <td>101.9</td>
      <td>−0.363</td>
      <td>7.7E-03</td>
    </tr>
    <tr>
      <td>Eosinophils Absolute</td>
      <td>×10(9)/L</td>
      <td>Pre-diagnosis</td>
      <td>28</td>
      <td>547</td>
      <td>0.0689</td>
      <td>0.161</td>
      <td>−0.45</td>
      <td>1.7E-03</td>
    </tr>
    <tr>
      <td>Esosinophils Absolute</td>
      <td>×10(9)/L</td>
      <td>Days 4–6 Post-Dx</td>
      <td>133</td>
      <td>559</td>
      <td>0.0906</td>
      <td>0.172</td>
      <td>−0.358</td>
      <td>2.4E-06</td>
    </tr>
    <tr>
      <td>Fibrinogen, P</td>
      <td>mg/dL</td>
      <td>Clinical presentation</td>
      <td>51</td>
      <td>233</td>
      <td>528.9</td>
      <td>360.7</td>
      <td>0.859</td>
      <td>8.9E-07</td>
    </tr>
    <tr>
      <td>Fibrinogen, P</td>
      <td>mg/dL</td>
      <td>Days 1–3 Post-Dx</td>
      <td>18</td>
      <td>319</td>
      <td>432.6</td>
      <td>297.4</td>
      <td>0.836</td>
      <td>1.7E-03</td>
    </tr>
    <tr>
      <td>Fibrinogen, P</td>
      <td>mg/dL</td>
      <td>Days 4–6 Post-Dx</td>
      <td>26</td>
      <td>116</td>
      <td>477.8</td>
      <td>333.7</td>
      <td>0.744</td>
      <td>0.014</td>
    </tr>
    <tr>
      <td>Glucose, Random, S</td>
      <td>mg/dL</td>
      <td>Days 13–15 Post-Dx</td>
      <td>49</td>
      <td>314</td>
      <td>150</td>
      <td>126.5</td>
      <td>0.544</td>
      <td>0.013</td>
    </tr>
    <tr>
      <td>Hematocrit, B</td>
      <td>%</td>
      <td>Days 1–3 Post-Dx</td>
      <td>158</td>
      <td>1582</td>
      <td>36.5</td>
      <td>33.8</td>
      <td>0.433</td>
      <td>9.6E-06</td>
    </tr>
    <tr>
      <td>Hematocrit, B</td>
      <td>%</td>
      <td>Days 4–6 Post-Dx</td>
      <td>152</td>
      <td>851</td>
      <td>36</td>
      <td>32.1</td>
      <td>0.621</td>
      <td>2.2E-10</td>
    </tr>
    <tr>
      <td>Hematocrit, B</td>
      <td>%</td>
      <td>Days 7–9 Post-Dx</td>
      <td>132</td>
      <td>639</td>
      <td>35.5</td>
      <td>31.8</td>
      <td>0.587</td>
      <td>5.8E-08</td>
    </tr>
    <tr>
      <td>Hematocrit, B</td>
      <td>%</td>
      <td>Days 10–12 Post-Dx</td>
      <td>110</td>
      <td>505</td>
      <td>35.1</td>
      <td>31.8</td>
      <td>0.511</td>
      <td>1.7E-05</td>
    </tr>
    <tr>
      <td>Hemoglobin Arterial</td>
      <td>g/dL</td>
      <td>Days 1–3 Post-Dx</td>
      <td>31</td>
      <td>208</td>
      <td>12.1</td>
      <td>10.8</td>
      <td>0.651</td>
      <td>0.025</td>
    </tr>
    <tr>
      <td>Hemoglobin, B</td>
      <td>g/dL</td>
      <td>Days 1–3 Post-Dx</td>
      <td>158</td>
      <td>1682</td>
      <td>11.9</td>
      <td>11.1</td>
      <td>0.358</td>
      <td>2.2E-04</td>
    </tr>
    <tr>
      <td>Hemoglobin, B</td>
      <td>g/dL</td>
      <td>Days 4–6 Post-Dx</td>
      <td>152</td>
      <td>873</td>
      <td>11.8</td>
      <td>10.4</td>
      <td>0.636</td>
      <td>1.4E-10</td>
    </tr>
    <tr>
      <td>Hemoglobin, B</td>
      <td>g/dL</td>
      <td>Days 7–9 Post-Dx</td>
      <td>132</td>
      <td>653</td>
      <td>11.6</td>
      <td>10.4</td>
      <td>0.56</td>
      <td>2.0E-07</td>
    </tr>
    <tr>
      <td>Hemoglobin, B</td>
      <td>g/dL</td>
      <td>Days 10–12 Post-Dx</td>
      <td>110</td>
      <td>516</td>
      <td>11.4</td>
      <td>10.3</td>
      <td>0.49</td>
      <td>2.6E-05</td>
    </tr>
    <tr>
      <td>Ionized Calcium, Arterial</td>
      <td>mg/dL</td>
      <td>Days 16–30 Post-Dx</td>
      <td>8</td>
      <td>36</td>
      <td>4.93</td>
      <td>4.48</td>
      <td>1.561</td>
      <td>0.022</td>
    </tr>
    <tr>
      <td>Lactate Dehydrogenase, S</td>
      <td>U/L</td>
      <td>Days 10–12 Post-Dx</td>
      <td>21</td>
      <td>88</td>
      <td>406.2</td>
      <td>295.2</td>
      <td>0.463</td>
      <td>1.4E-03</td>
    </tr>
    <tr>
      <td>Lactate, P</td>
      <td>mmol/L</td>
      <td>Clinical presentation</td>
      <td>89</td>
      <td>954</td>
      <td>1.37</td>
      <td>1.93</td>
      <td>−0.462</td>
      <td>3.1E-06</td>
    </tr>
    <tr>
      <td>Lymphocytes Percent</td>
      <td>%</td>
      <td>Days 13–15 Post-Dx</td>
      <td>5</td>
      <td>66</td>
      <td>33.2</td>
      <td>15</td>
      <td>1.514</td>
      <td>0.048</td>
    </tr>
    <tr>
      <td>Lymphs Absolute</td>
      <td>×10(9)/L</td>
      <td>Days 13–15 Post-Dx</td>
      <td>56</td>
      <td>349</td>
      <td>3.12</td>
      <td>1.11</td>
      <td>0.44</td>
      <td>0.018</td>
    </tr>
    <tr>
      <td>Magnesium, Plasma</td>
      <td>mg/dL</td>
      <td>Days 10–12 Post-Dx</td>
      <td>20</td>
      <td>87</td>
      <td>2.14</td>
      <td>1.91</td>
      <td>0.772</td>
      <td>0.015</td>
    </tr>
    <tr>
      <td>Magnesium, S/P</td>
      <td>mg/dL</td>
      <td>Days 4–6 Post-Dx</td>
      <td>47</td>
      <td>279</td>
      <td>2.22</td>
      <td>1.98</td>
      <td>0.743</td>
      <td>3.0E-03</td>
    </tr>
    <tr>
      <td>Magnesium, S/P</td>
      <td>mg/dL</td>
      <td>Days 7–9 Post-Dx</td>
      <td>40</td>
      <td>215</td>
      <td>2.31</td>
      <td>1.97</td>
      <td>1.06</td>
      <td>4.1E-06</td>
    </tr>
    <tr>
      <td>Magnesium, S/P</td>
      <td>mg/dL</td>
      <td>Days 10–12 Post-Dx</td>
      <td>36</td>
      <td>187</td>
      <td>2.26</td>
      <td>1.91</td>
      <td>1.005</td>
      <td>2.9E-06</td>
    </tr>
    <tr>
      <td>Magnesium, S/P</td>
      <td>mg/dL</td>
      <td>Days 13–15 Post-Dx</td>
      <td>35</td>
      <td>179</td>
      <td>2.22</td>
      <td>1.89</td>
      <td>0.904</td>
      <td>1.8E-07</td>
    </tr>
    <tr>
      <td>Magnesium, S/P</td>
      <td>mg/dL</td>
      <td>Days 16–30 Post-Dx</td>
      <td>33</td>
      <td>317</td>
      <td>2.13</td>
      <td>1.89</td>
      <td>0.906</td>
      <td>1.6E-04</td>
    </tr>
    <tr>
      <td>Manual Diff Promyelocytes</td>
      <td>%</td>
      <td>Days 1–3 Post-Dx</td>
      <td>6</td>
      <td>55</td>
      <td>0.25</td>
      <td>0</td>
      <td>1.402</td>
      <td>0.027</td>
    </tr>
    <tr>
      <td>Mean Corpuscular Volume</td>
      <td>fL</td>
      <td>Days 10–12 Post-Dx</td>
      <td>110</td>
      <td>502</td>
      <td>89.5</td>
      <td>92</td>
      <td>−0.38</td>
      <td>8.8E-03</td>
    </tr>
    <tr>
      <td>Methemoglobin, ABG</td>
      <td>%</td>
      <td>Clinical presentation</td>
      <td>34</td>
      <td>356</td>
      <td>0.335</td>
      <td>0.571</td>
      <td>−0.629</td>
      <td>6.0E-03</td>
    </tr>
    <tr>
      <td>Methemoglobin, ABG</td>
      <td>%</td>
      <td>Days 1–3 Post-Dx</td>
      <td>44</td>
      <td>436</td>
      <td>0.425</td>
      <td>0.697</td>
      <td>−0.463</td>
      <td>1.5E-03</td>
    </tr>
    <tr>
      <td>Monocytes Absolute</td>
      <td>×10(9)/L</td>
      <td>Days 1–3 Post-Dx</td>
      <td>131</td>
      <td>1079</td>
      <td>0.447</td>
      <td>0.748</td>
      <td>−0.502</td>
      <td>2.6E-16</td>
    </tr>
    <tr>
      <td>Monocytes Absolute</td>
      <td>×10(9)/L</td>
      <td>Days 4–6 Post-Dx</td>
      <td>135</td>
      <td>584</td>
      <td>0.475</td>
      <td>0.715</td>
      <td>−0.597</td>
      <td>2.2E-10</td>
    </tr>
    <tr>
      <td>N-terminal-PRO-Brain Type Natriuretic Peptide, S</td>
      <td>pg/mL</td>
      <td>Days 4–6 Post-Dx</td>
      <td>10</td>
      <td>63</td>
      <td>415.6</td>
      <td>7609.7</td>
      <td>−0.525</td>
      <td>2.9E-03</td>
    </tr>
    <tr>
      <td>Neutrophils, B</td>
      <td>×10(9)/L</td>
      <td>Clinical presentation</td>
      <td>136</td>
      <td>1382</td>
      <td>5.31</td>
      <td>7.12</td>
      <td>−0.396</td>
      <td>6.3E-06</td>
    </tr>
    <tr>
      <td>Neutrophils, B</td>
      <td>×10(9)/L</td>
      <td>Days 1–3 Post-Dx</td>
      <td>130</td>
      <td>1141</td>
      <td>4.73</td>
      <td>6.32</td>
      <td>−0.385</td>
      <td>5.8E-05</td>
    </tr>
    <tr>
      <td>NT-PRO BNP, P</td>
      <td>pg/mL</td>
      <td>Clinical presentation</td>
      <td>25</td>
      <td>372</td>
      <td>1372.4</td>
      <td>5327.9</td>
      <td>−0.385</td>
      <td>0.046</td>
    </tr>
    <tr>
      <td>NT-PRO BNP, P</td>
      <td>pg/mL</td>
      <td>Days 4–6 Post-Dx</td>
      <td>14</td>
      <td>20</td>
      <td>815.3</td>
      <td>4388.8</td>
      <td>−0.929</td>
      <td>0.02</td>
    </tr>
    <tr>
      <td>Nucleated RBC</td>
      <td>/100 WBC</td>
      <td>Days 13–15 Post-Dx</td>
      <td>23</td>
      <td>189</td>
      <td>1.24</td>
      <td>0.447</td>
      <td>0.561</td>
      <td>1.7E-03</td>
    </tr>
    <tr>
      <td>O2 HB</td>
      <td>%</td>
      <td>Days 1–3 Post-Dx</td>
      <td>13</td>
      <td>242</td>
      <td>88.6</td>
      <td>95</td>
      <td>−1.37</td>
      <td>2.2E-03</td>
    </tr>
    <tr>
      <td>O2 HB</td>
      <td>%</td>
      <td>Days 4–6 Post-Dx</td>
      <td>32</td>
      <td>90</td>
      <td>92.1</td>
      <td>93.7</td>
      <td>−0.356</td>
      <td>0.013</td>
    </tr>
    <tr>
      <td>O2 HB</td>
      <td>%</td>
      <td>Days 7–9 Post-Dx</td>
      <td>24</td>
      <td>46</td>
      <td>91.5</td>
      <td>94.5</td>
      <td>−0.701</td>
      <td>3.3E-04</td>
    </tr>
    <tr>
      <td>Osmolality, U</td>
      <td>mOsm/kg</td>
      <td>Pre-diagnosis</td>
      <td>4</td>
      <td>80</td>
      <td>231.5</td>
      <td>478.8</td>
      <td>−1.509</td>
      <td>0.044</td>
    </tr>
    <tr>
      <td>Oxygen Content, Arterial</td>
      <td>vol %</td>
      <td>Days 4–6 Post-Dx</td>
      <td>32</td>
      <td>89</td>
      <td>16</td>
      <td>13.7</td>
      <td>0.839</td>
      <td>2.4E-03</td>
    </tr>
    <tr>
      <td>Oxygen Saturation (%) in Arterial Blood</td>
      <td>%</td>
      <td>Clinical presentation</td>
      <td>27</td>
      <td>189</td>
      <td>94.2</td>
      <td>96.2</td>
      <td>−0.52</td>
      <td>3.1E-03</td>
    </tr>
    <tr>
      <td>Oxygen Saturation (%) in Arterial Blood</td>
      <td>%</td>
      <td>Days 1–3 Post-Dx</td>
      <td>31</td>
      <td>216</td>
      <td>94.3</td>
      <td>97.1</td>
      <td>−1.293</td>
      <td>8.4E-09</td>
    </tr>
    <tr>
      <td>Oxygen Saturation (%) in Arterial Blood</td>
      <td>%</td>
      <td>Days 4–6 Post-Dx</td>
      <td>26</td>
      <td>70</td>
      <td>94.3</td>
      <td>95.7</td>
      <td>−0.578</td>
      <td>0.014</td>
    </tr>
    <tr>
      <td>Oxygen Saturation (%) in Arterial Blood</td>
      <td>%</td>
      <td>Days 10–12 Post-Dx</td>
      <td>18</td>
      <td>29</td>
      <td>93.4</td>
      <td>96.5</td>
      <td>−1.254</td>
      <td>3.1E-03</td>
    </tr>
    <tr>
      <td>Oxygen Saturation (%) in Arterial Blood</td>
      <td>%</td>
      <td>Days 13–15 Post-Dx</td>
      <td>17</td>
      <td>28</td>
      <td>94.8</td>
      <td>96.4</td>
      <td>−0.671</td>
      <td>0.043</td>
    </tr>
    <tr>
      <td>pH Blood Arterial</td>
      <td>None</td>
      <td>Days 1–3 Post-Dx</td>
      <td>26</td>
      <td>193</td>
      <td>7.42</td>
      <td>7.39</td>
      <td>0.539</td>
      <td>0.035</td>
    </tr>
    <tr>
      <td>pH Blood Venous</td>
      <td>pH</td>
      <td>Days 1–3 Post-Dx</td>
      <td>10</td>
      <td>82</td>
      <td>7.42</td>
      <td>7.36</td>
      <td>0.963</td>
      <td>0.031</td>
    </tr>
    <tr>
      <td>pH, POCT, B</td>
      <td>None</td>
      <td>Clinical presentation</td>
      <td>13</td>
      <td>202</td>
      <td>7.41</td>
      <td>7.33</td>
      <td>0.708</td>
      <td>0.042</td>
    </tr>
    <tr>
      <td>Platelets</td>
      <td>×10(9)/L</td>
      <td>Pre-diagnosis</td>
      <td>39</td>
      <td>649</td>
      <td>184.8</td>
      <td>225.9</td>
      <td>−0.393</td>
      <td>0.024</td>
    </tr>
    <tr>
      <td>PO2</td>
      <td>mm Hg</td>
      <td>Days 1–3 Post-Dx</td>
      <td>8</td>
      <td>145</td>
      <td>67.2</td>
      <td>179.7</td>
      <td>−1.301</td>
      <td>1.7E-03</td>
    </tr>
    <tr>
      <td>PO2</td>
      <td>mm Hg</td>
      <td>Days 7–9 Post-Dx</td>
      <td>14</td>
      <td>16</td>
      <td>71.1</td>
      <td>121.1</td>
      <td>−0.949</td>
      <td>0.027</td>
    </tr>
    <tr>
      <td>PO2 Arterial</td>
      <td>mm Hg</td>
      <td>Days 1–3 Post-Dx</td>
      <td>26</td>
      <td>193</td>
      <td>100.4</td>
      <td>150.9</td>
      <td>−0.87</td>
      <td>8.2E-05</td>
    </tr>
    <tr>
      <td>PO2 Arterial</td>
      <td>mm Hg</td>
      <td>Days 10–12 Post-Dx</td>
      <td>17</td>
      <td>25</td>
      <td>93.6</td>
      <td>134</td>
      <td>−0.755</td>
      <td>0.019</td>
    </tr>
    <tr>
      <td>Potassium, S</td>
      <td>mmol/L</td>
      <td>Pre-diagnosis</td>
      <td>10</td>
      <td>398</td>
      <td>3.93</td>
      <td>4.35</td>
      <td>−0.836</td>
      <td>0.049</td>
    </tr>
    <tr>
      <td>RABG Calculated O2 Hemoglobin</td>
      <td>%</td>
      <td>Days 1–3 Post-Dx</td>
      <td>22</td>
      <td>109</td>
      <td>93.6</td>
      <td>95</td>
      <td>−0.464</td>
      <td>2.9E-03</td>
    </tr>
    <tr>
      <td>RABG Calculated O2 Hemoglobin</td>
      <td>%</td>
      <td>Days 4–6 Post-Dx</td>
      <td>16</td>
      <td>49</td>
      <td>93.2</td>
      <td>95.3</td>
      <td>−0.859</td>
      <td>2.3E-03</td>
    </tr>
    <tr>
      <td>RABG Calculated O2 Hemoglobin</td>
      <td>%</td>
      <td>Days 10–12 Post-Dx</td>
      <td>13</td>
      <td>22</td>
      <td>94</td>
      <td>96.3</td>
      <td>−1.269</td>
      <td>0.038</td>
    </tr>
    <tr>
      <td>RABG PF Ratio</td>
      <td>None</td>
      <td>Days 4–6 Post-Dx</td>
      <td>17</td>
      <td>49</td>
      <td>1.46</td>
      <td>2.68</td>
      <td>−1.489</td>
      <td>6.9E-05</td>
    </tr>
    <tr>
      <td>RABG PF Ratio</td>
      <td>None</td>
      <td>Days 7–9 Post-Dx</td>
      <td>13</td>
      <td>22</td>
      <td>1.75</td>
      <td>2.56</td>
      <td>−1.006</td>
      <td>0.038</td>
    </tr>
    <tr>
      <td>RABG PF Ratio</td>
      <td>None</td>
      <td>Days 10–12 Post-Dx</td>
      <td>13</td>
      <td>22</td>
      <td>1.83</td>
      <td>3.22</td>
      <td>−1.518</td>
      <td>3.9E-03</td>
    </tr>
    <tr>
      <td>RBC (Red Blood Cell) Count</td>
      <td>×10(12)/L</td>
      <td>Clinical presentation</td>
      <td>151</td>
      <td>1671</td>
      <td>4.32</td>
      <td>3.99</td>
      <td>0.409</td>
      <td>2.0E-04</td>
    </tr>
    <tr>
      <td>RBC (Red Blood Cell) Count</td>
      <td>×10(12)/L</td>
      <td>Days 1–3 Post-Dx</td>
      <td>158</td>
      <td>1562</td>
      <td>4.13</td>
      <td>3.73</td>
      <td>0.524</td>
      <td>5.8E-08</td>
    </tr>
    <tr>
      <td>RBC (Red Blood Cell) Count</td>
      <td>×10(12)/L</td>
      <td>Days 4–6 Post-Dx</td>
      <td>152</td>
      <td>846</td>
      <td>4.08</td>
      <td>3.55</td>
      <td>0.693</td>
      <td>3.2E-12</td>
    </tr>
    <tr>
      <td>RBC (Red Blood Cell) Count</td>
      <td>×10(12)/L</td>
      <td>Days 7–9 Post-Dx</td>
      <td>132</td>
      <td>635</td>
      <td>4</td>
      <td>3.49</td>
      <td>0.656</td>
      <td>2.4E-09</td>
    </tr>
    <tr>
      <td>RBC (Red Blood Cell) Count</td>
      <td>×10(12)/L</td>
      <td>Days 10–12 Post-Dx</td>
      <td>110</td>
      <td>502</td>
      <td>3.95</td>
      <td>3.48</td>
      <td>0.587</td>
      <td>6.1E-07</td>
    </tr>
    <tr>
      <td>Red Cell Distribution Width CV</td>
      <td>%</td>
      <td>Days 4–6 Post-Dx</td>
      <td>137</td>
      <td>722</td>
      <td>14.1</td>
      <td>15.1</td>
      <td>−0.373</td>
      <td>3.4E-04</td>
    </tr>
    <tr>
      <td>Red Cell Distribution Width CV</td>
      <td>%</td>
      <td>Days 7–9 Post-Dx</td>
      <td>119</td>
      <td>552</td>
      <td>14.2</td>
      <td>15.4</td>
      <td>−0.431</td>
      <td>9.8E-05</td>
    </tr>
    <tr>
      <td>Red Cell Distribution Width CV</td>
      <td>%</td>
      <td>Days 10–12 Post-Dx</td>
      <td>97</td>
      <td>429</td>
      <td>14.5</td>
      <td>15.7</td>
      <td>−0.394</td>
      <td>1.2E-03</td>
    </tr>
    <tr>
      <td>Sodium, P</td>
      <td>mmol/L</td>
      <td>Clinical presentation</td>
      <td>89</td>
      <td>1141</td>
      <td>135.6</td>
      <td>137.3</td>
      <td>−0.375</td>
      <td>7.3E-03</td>
    </tr>
    <tr>
      <td>Sodium, P</td>
      <td>mmol/L</td>
      <td>Days 1–3 Post-Dx</td>
      <td>77</td>
      <td>927</td>
      <td>136.6</td>
      <td>138.1</td>
      <td>−0.377</td>
      <td>4.7E-03</td>
    </tr>
    <tr>
      <td>Sodium, S</td>
      <td>mmol/L</td>
      <td>Days 10–12 Post-Dx</td>
      <td>69</td>
      <td>334</td>
      <td>140.8</td>
      <td>138.3</td>
      <td>0.651</td>
      <td>2.0E-04</td>
    </tr>
    <tr>
      <td>Spont. Breaths/min</td>
      <td>None</td>
      <td>Days 4–6 Post-Dx</td>
      <td>23</td>
      <td>67</td>
      <td>25</td>
      <td>20.2</td>
      <td>0.767</td>
      <td>0.016</td>
    </tr>
    <tr>
      <td>Tacrolimus, B</td>
      <td>ng/mL</td>
      <td>Days 7–9 Post-Dx</td>
      <td>8</td>
      <td>81</td>
      <td>4.22</td>
      <td>8.12</td>
      <td>−1.102</td>
      <td>8.8E-03</td>
    </tr>
    <tr>
      <td>Tacrolimus, B</td>
      <td>ng/mL</td>
      <td>Days 10–12 Post-Dx</td>
      <td>8</td>
      <td>79</td>
      <td>3.8</td>
      <td>9.24</td>
      <td>−1.468</td>
      <td>2.5E-03</td>
    </tr>
    <tr>
      <td>Tacrolimus, B</td>
      <td>ng/mL</td>
      <td>Days 13–15 Post-Dx</td>
      <td>7</td>
      <td>71</td>
      <td>3.7</td>
      <td>8.52</td>
      <td>−1.47</td>
      <td>7.5E-03</td>
    </tr>
    <tr>
      <td>Tacrolimus, B</td>
      <td>ng/mL</td>
      <td>Days 16–30 Post-Dx</td>
      <td>10</td>
      <td>110</td>
      <td>4.93</td>
      <td>7.8</td>
      <td>−1.094</td>
      <td>0.022</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>None</td>
      <td>Clinical presentation</td>
      <td>23</td>
      <td>136</td>
      <td>37</td>
      <td>36.7</td>
      <td>0.591</td>
      <td>0.042</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>None</td>
      <td>Days 1–3 Post-Dx</td>
      <td>23</td>
      <td>189</td>
      <td>37</td>
      <td>36.4</td>
      <td>0.765</td>
      <td>4.8E-04</td>
    </tr>
    <tr>
      <td>Triglycerides, S/P</td>
      <td>mg/dL</td>
      <td>Days 4–6 Post-Dx</td>
      <td>16</td>
      <td>41</td>
      <td>326.2</td>
      <td>173</td>
      <td>1.196</td>
      <td>7.3E-03</td>
    </tr>
    <tr>
      <td>Triglycerides, S/P</td>
      <td>mg/dL</td>
      <td>Days 7–9 Post-Dx</td>
      <td>17</td>
      <td>24</td>
      <td>310.6</td>
      <td>191.5</td>
      <td>0.945</td>
      <td>0.016</td>
    </tr>
    <tr>
      <td>Triglycerides, S/P</td>
      <td>mg/dL</td>
      <td>Days 10–12 Post-Dx</td>
      <td>17</td>
      <td>35</td>
      <td>364.5</td>
      <td>174.4</td>
      <td>1.217</td>
      <td>4.0E-03</td>
    </tr>
    <tr>
      <td>Triglycerides, S/P</td>
      <td>mg/dL</td>
      <td>Days 16–30 Post-Dx</td>
      <td>10</td>
      <td>77</td>
      <td>276.1</td>
      <td>166.4</td>
      <td>0.83</td>
      <td>0.024</td>
    </tr>
    <tr>
      <td>Troponin T, 5TH GEN, P</td>
      <td>ng/L</td>
      <td>Days 4–6 Post-Dx</td>
      <td>18</td>
      <td>54</td>
      <td>21.4</td>
      <td>245.3</td>
      <td>−0.499</td>
      <td>7.5E-03</td>
    </tr>
    <tr>
      <td>Troponin T, Baseline, 5TH Gen, P</td>
      <td>ng/L</td>
      <td>Days 7–9 Post-Dx</td>
      <td>11</td>
      <td>43</td>
      <td>15.1</td>
      <td>53.7</td>
      <td>−0.538</td>
      <td>0.037</td>
    </tr>
    <tr>
      <td>VBGRS HGB</td>
      <td>g/dL</td>
      <td>Days 4–6 Post-Dx</td>
      <td>36</td>
      <td>99</td>
      <td>12.3</td>
      <td>10.5</td>
      <td>0.932</td>
      <td>3.6E-04</td>
    </tr>
    <tr>
      <td>White Blood Cells</td>
      <td>×10(9)/L</td>
      <td>Days 1–3 Post-Dx</td>
      <td>158</td>
      <td>1650</td>
      <td>6.67</td>
      <td>9.08</td>
      <td>−0.439</td>
      <td>3.2E-12</td>
    </tr>
  </tbody>
</table>

With respect to coagulation, we found that plasma fibrinogen was significantly elevated in COVIDpos patients at the time of diagnosis (Cohen’s D = 0.859, BH-adjusted Mann-Whitney p-value = 8.9e-7, Table 2, Figure 3A). This hyperfibrinogenemia generally resolved during the 7 days following diagnosis (Figure 3A). Conversely, platelet counts were lower in the COVIDpos cohort at the time of clinical presentation but tended to increase over the subsequent 10 days to levels significantly higher than those in COVIDneg patients (Cohen’s D = 0.229, BH-adjusted Mann-Whitney p-value = 3.6e-3, Table 2, Figure 3B). While thrombocytopenia has been reported in COVID-19 patients before (Xu et al., 2020; Yang et al., 2020), an upward trend in platelet counts after diagnosis has not been described to our knowledge. We observe extended prothrombin times in both the COVIDpos and COVIDneg (matched) cohorts significantly above the normal range; however, there was no differentiation between the cohorts. We observe extended activated partial thromboplastin times (aPTT) in the COVIDpos significantly above normal levels from day 7 onward (Figure 3D). D-dimer levels were frequently above normal limits in both the COVIDpos and COVIDneg cohorts and were not significantly different between these cohorts during any time window (Figure 3E). The above trends hold up even when the time windows are perturbed (Table 3).

**Table 3.**
 Sensitivity analysis of clinical time intervals for significant coagulation-related lab test trends.Results from sensitivity analysis perturbing the time intervals for the significant (coagulation-related lab test, time interval) pairs (i.e. highlighted rows of Table 2). Perturbed results that met both of the significance thresholds (BH-adjusted Mann-Whitney p-value <0.05 and Cohen’s D absolute value >0.35) are highlighted in light green, and perturbed results that only met one of the thresholds for either effect size or statistical significance are highlighted in yellow.


<table>
  <thead>
    <tr>
      <th>Test</th>
      <th>Units</th>
      <th>Perturbation</th>
      <th>Original time window</th>
      <th>Count COVIDpos</th>
      <th>Count COVIDneg</th>
      <th>Mean COVIDpos</th>
      <th>Mean COVIDneg</th>
      <th>Cohen's D</th>
      <th>BH-adjusted M-W p-value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Activated Partial Thrombopl Time, P</td>
      <td>sec</td>
      <td>−1 day</td>
      <td>Days 7−9 Post-Dx</td>
      <td>26</td>
      <td>72</td>
      <td>50.1</td>
      <td>38</td>
      <td>0.57</td>
      <td>0.034</td>
    </tr>
    <tr>
      <td>Activated Partial Thrombopl Time, P</td>
      <td>sec</td>
      <td>+1 day</td>
      <td>Days 7−9 Post-Dx</td>
      <td>17</td>
      <td>58</td>
      <td>55</td>
      <td>37.5</td>
      <td>0.81</td>
      <td>0.014</td>
    </tr>
    <tr>
      <td>Activated Partial Thrombopl Time, P</td>
      <td>sec</td>
      <td>−1 day</td>
      <td>Days 10−12 Post-Dx</td>
      <td>16</td>
      <td>57</td>
      <td>56.9</td>
      <td>38.4</td>
      <td>0.808</td>
      <td>9.10E-03</td>
    </tr>
    <tr>
      <td>Activated Partial Thrombopl Time, P</td>
      <td>sec</td>
      <td>+1 day</td>
      <td>Days 10−12 Post-Dx</td>
      <td>15</td>
      <td>60</td>
      <td>56.9</td>
      <td>38</td>
      <td>1.106</td>
      <td>2.60E-03</td>
    </tr>
    <tr>
      <td>Activated Partial Thrombopl Time, P</td>
      <td>sec</td>
      <td>−1 day</td>
      <td>Days 13−15 Post-Dx</td>
      <td>15</td>
      <td>52</td>
      <td>55.5</td>
      <td>37.8</td>
      <td>1.041</td>
      <td>0.014</td>
    </tr>
    <tr>
      <td>Activated Partial Thrombopl TIME, P</td>
      <td>sec</td>
      <td>+1 day</td>
      <td>Days 13−15 Post-Dx</td>
      <td>14</td>
      <td>48</td>
      <td>51.8</td>
      <td>37.1</td>
      <td>0.962</td>
      <td>0.015</td>
    </tr>
    <tr>
      <td>Activated Partial Thrombopl Time, P</td>
      <td>sec</td>
      <td>−1 day</td>
      <td>Days 16−30 Post-Dx</td>
      <td>22</td>
      <td>156</td>
      <td>55.2</td>
      <td>37</td>
      <td>0.913</td>
      <td>5.70E-03</td>
    </tr>
    <tr>
      <td>Activated Partial Thrombopl Time, P</td>
      <td>sec</td>
      <td>+1 day</td>
      <td>Days 16−30 Post-Dx</td>
      <td>19</td>
      <td>139</td>
      <td>56</td>
      <td>38.2</td>
      <td>0.725</td>
      <td>3.80E-02</td>
    </tr>
    <tr>
      <td>Fibrinogen, P</td>
      <td>mg/dL</td>
      <td>−1 day</td>
      <td>Clinical presentation</td>
      <td>25</td>
      <td>92</td>
      <td>584.9</td>
      <td>370.7</td>
      <td>1.067</td>
      <td>1.20E-04</td>
    </tr>
    <tr>
      <td>Fibrinogen, P</td>
      <td>mg/dL</td>
      <td>+1 day</td>
      <td>Clinical presentation</td>
      <td>37</td>
      <td>292</td>
      <td>488.2</td>
      <td>326.2</td>
      <td>0.885</td>
      <td>8.80E-06</td>
    </tr>
    <tr>
      <td>Fibrinogen, P</td>
      <td>mg/dL</td>
      <td>−1 day</td>
      <td>Days 1−3 Post-Dx</td>
      <td>41</td>
      <td>381</td>
      <td>494.5</td>
      <td>318</td>
      <td>1.023</td>
      <td>3.90E-07</td>
    </tr>
    <tr>
      <td>Fibrinogen, P</td>
      <td>mg/dL</td>
      <td>+1 day</td>
      <td>Days 1−3 Post-Dx</td>
      <td>21</td>
      <td>244</td>
      <td>420.3</td>
      <td>312.2</td>
      <td>0.616</td>
      <td>7.90E-03</td>
    </tr>
    <tr>
      <td>Fibrinogen, P</td>
      <td>mg/dL</td>
      <td>−1 day</td>
      <td>Days 4−6 Post-Dx</td>
      <td>27</td>
      <td>156</td>
      <td>432.2</td>
      <td>336</td>
      <td>0.495</td>
      <td>0.045</td>
    </tr>
    <tr>
      <td>Fibrinogen, P</td>
      <td>mg/dL</td>
      <td>+1 day</td>
      <td>Days 4−6 Post-Dx</td>
      <td>24</td>
      <td>105</td>
      <td>472.2</td>
      <td>333.2</td>
      <td>0.712</td>
      <td>0.025</td>
    </tr>
    <tr>
      <td>Platelets</td>
      <td>x10(9)/L</td>
      <td>−1 day</td>
      <td>Pre-diagnosis</td>
      <td>34</td>
      <td>575</td>
      <td>187.3</td>
      <td>225.6</td>
      <td>-0.357</td>
      <td>0.057</td>
    </tr>
    <tr>
      <td>Platelets</td>
      <td>x10(9)/L</td>
      <td>+1 day</td>
      <td>Pre-diagnosis</td>
      <td>118</td>
      <td>1533</td>
      <td>201.3</td>
      <td>234.4</td>
      <td>-0.328</td>
      <td>7.30E-04</td>
    </tr>
  </tbody>
</table>

We also performed similar analyses comparing the COVIDpos and COVIDneg (matched) cohorts using different time window definitions including daily trends (Figure 4). This approach offers the advantage of increased granularity at the cost of sample size per time point, but we did identify similar lab tests as altered in COVIDpos patients using each approach including the fibrinogen decline and platelet increase in the COVIDpos cohort after diagnosis (Figure 4).

![Figure 4.](https://cdn.elifesciences.org/articles/59209/elife-59209-fig4-v2.jpg)

**Figure 4.:** Longitudinal trends of COVIDpos versus COVIDneg (matched) patients for the following lab tests: (A) platelets; (B) fibrinogen, plasma; (C) prothrombin time, plasma; (D) activated partial thromboplastin time; (E) D-dimer; (F) magnesium, serum/plasma; (G) basophils absolute; (H) neutrophils, blood; (I) alkaline phosphatase, serum. The reference ranges are shown at the top of each plot. For each cohort, average lab values and standard errors are shown for each day with at least three observations. For certain lab tests, some data points are missing because these days had fewer than three data points in the COVIDpos cohort.

### Thrombosis is enriched among COVID-19 patients undergoing longitudinal lab testing

Given the recently described coagulopathies associated with COVID-19 (Tang et al., 2020; Klok et al., 2020; Levi et al., 2020), we were intrigued by the temporal trends in fibrinogen levels and platelet counts in the COVIDpos cohort (Figure 3). Next, we asked whether the observed coagulation-related laboratory trends were associated with clinical manifestations of thrombosis. To do so, we employed a BERT-based neural network (Devlin et al., 2018; see Materials and methods) to identify patients who experienced a thrombotic event after their SARS-CoV-2 PCR testing date. Specifically, we extracted diagnostic sentiment from EHR notes (e.g. whether a patient was diagnosed with a phenotype, suspected of having a phenotype, ruled out for having a phenotype, or other) regarding specific thromboembolic phenotypes including deep vein thrombosis, pulmonary embolism, myocardial infarction, venous thromboembolism, thrombotic stroke, cerebral venous thrombosis, and disseminated intravascular coagulation.

We found that 101 of the total 2232 COVIDpos cohort (4.5%) were positively diagnosed with one or more of the above-mentioned thrombotic phenotypes in the 30 days after PCR testing, with the majority of these patients (53 of 101) experiencing a deep vein thrombosis. Interestingly, we found that after creating subsets of the patients with longitudinal lab testing data (i.e. the patients meeting the criteria for inclusion in our study), 76 of the 246 patients (31%) had at least one EHR-derived clot diagnosis, including 47 patients with deep vein thrombosis (Table 4). Thus, the cohort under consideration here is highly enriched (Table 5; hypergeometric p-value <1×10−50) for patients experiencing thrombotic events compared to the overall COVIDpos cohort.

**Table 4.**
 Prevalence of thrombotic phenotypes after the clinical presentation in COVIDpos patients with and without available longitudinal lab testing data.For each clotting phenotype listed, a BERT-based neural network was used to extract diagnostic sentiment from individual EHR patient notes in which the phenotype (or a synonym thereof) was present. This automated curation was applied to clinical notes for each patient from day = −1 (clinical presentation) to day = 30 (end of the study period) relative to the PCR testing date. In this table, we show the absolute number of patients with each phenotype along with the percentage of patients in each cohort with the given specific thrombotic phenotype in parentheses.


<table>
  <thead>
    <tr>
      <th>Clotting phenotype</th>
      <th>Cohort 1: COVIDpos with longitudinal data</th>
      <th>Cohort 2: COVIDpos without longitudinal data</th>
      <th>Cohort 3: Complete COVIDpos cohort</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Deep vein thrombosis</td>
      <td>47 (19%)</td>
      <td>6 (0.30%)</td>
      <td>53 (2.4%)</td>
    </tr>
    <tr>
      <td>Pulmonary embolism</td>
      <td>22 (8.9%)</td>
      <td>9 (0.45%)</td>
      <td>31 (1.4%)</td>
    </tr>
    <tr>
      <td>Myocardial infarction</td>
      <td>10 (4.1%)</td>
      <td>8 (0.40%)</td>
      <td>18 (0.81%)</td>
    </tr>
    <tr>
      <td>Venous thromboembolism</td>
      <td>7 (2.8%)</td>
      <td>0</td>
      <td>7 (0.31%)</td>
    </tr>
    <tr>
      <td>Thrombotic stroke</td>
      <td>2 (0.81%)</td>
      <td>2 (0.10%]</td>
      <td>4 (0.18%)</td>
    </tr>
    <tr>
      <td>Cerebral venous thrombosis</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Disseminated intravascular coagulation</td>
      <td>5 (2.0%)</td>
      <td>0</td>
      <td>5 (0.22%)</td>
    </tr>
    <tr>
      <td>Total unique patients with clot</td>
      <td>76 (31%)</td>
      <td>25 (1.3%)</td>
      <td>101 (4.5%)</td>
    </tr>
    <tr>
      <td>Total patients</td>
      <td>246</td>
      <td>1986</td>
      <td>2232</td>
    </tr>
  </tbody>
</table>

**Table 5.**
 Enrichment of thrombotic phenotypes among COVIDpos patients with longitudinal lab testing data.Contingency table to calculate hypergeometric enrichment significance of thrombosis among patients with longitudinal lab testing data. The 246 patients with longitudinal testing data are those considered in this study, while the 1986 patients who did not have at least three results from one lab test over the defined 60-day window were excluded from this longitudinal analysis.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Patient has longitudinal data</th>
      <th>Patient does NOT have longitudinal data</th>
      <th>Total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Thrombosis</td>
      <td>76</td>
      <td>25</td>
      <td>101</td>
    </tr>
    <tr>
      <td>No thrombosis</td>
      <td>170</td>
      <td>1961</td>
      <td>2131</td>
    </tr>
    <tr>
      <td>Total</td>
      <td>246</td>
      <td>1986</td>
      <td>2232</td>
    </tr>
  </tbody>
</table>

_Hypergeometric enrichment: p-value <1×10−50._

**Table 6.**
 Validation of the BERT model to identify the sentiment of thrombotic phenotypes in clinical notes.Out-of-sample accuracy results of the BERT model to identify thrombotic phenotypes in 1000 randomly selected sentences from clinical notes which contained at least one mention of a thrombotic phenotype. The columns are (1) Clotting phenotype: thrombotic phenotype identified in the sentence, (2) TP (true positives): count of sentences in which the BERT model correctly identified the sentiment as ‘Yes’, (3) TN (true negatives): count of sentences in which the BERT model correctly identified the sentiment as not ‘Yes’, (4) FP (false positives): count of sentences in which the BERT model incorrectly identified the sentiment as ‘Yes’, (5) FN: (false negatives): count of sentences in which the BERT model incorrectly identified the sentiment as not ‘Yes’, (6) Recall: recall of the BERT model, equal to TP/(TP+FN), (7) Precision: precision of the BERT model, equal to TP/(TP+FP), (8) Accuracy: accuracy of the BERT model, equal to (TP+TN)/(TP+TN+FP+FN).


<table>
  <thead>
    <tr>
      <th>Clotting phenotype</th>
      <th>TP</th>
      <th>TN</th>
      <th>FP</th>
      <th>FN</th>
      <th>Recall</th>
      <th>Precision</th>
      <th>Accuracy</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Deep vein thrombosis</td>
      <td>136</td>
      <td>178</td>
      <td>24</td>
      <td>3</td>
      <td>98%</td>
      <td>85%</td>
      <td>92%</td>
    </tr>
    <tr>
      <td>Pulmonary embolism</td>
      <td>164</td>
      <td>78</td>
      <td>7</td>
      <td>6</td>
      <td>96%</td>
      <td>96%</td>
      <td>95%</td>
    </tr>
    <tr>
      <td>Myocardial infarction</td>
      <td>212</td>
      <td>65</td>
      <td>3</td>
      <td>3</td>
      <td>99%</td>
      <td>99%</td>
      <td>98%</td>
    </tr>
    <tr>
      <td>Venous thromboembolism</td>
      <td>3</td>
      <td>97</td>
      <td>7</td>
      <td>0</td>
      <td>100%</td>
      <td>30%</td>
      <td>93%</td>
    </tr>
    <tr>
      <td>Thrombotic stroke</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>100%</td>
      <td>100%</td>
      <td>100%</td>
    </tr>
    <tr>
      <td>Cerebral venous thrombosis</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>100%</td>
      <td>100%</td>
      <td>100%</td>
    </tr>
    <tr>
      <td>Disseminated intravascular coagulation</td>
      <td>4</td>
      <td>4</td>
      <td>0</td>
      <td>0</td>
      <td>100%</td>
      <td>100%</td>
      <td>100%</td>
    </tr>
    <tr>
      <td>Overall</td>
      <td>525</td>
      <td>422</td>
      <td>41</td>
      <td>12</td>
      <td>97.8%</td>
      <td>92.8%</td>
      <td>94.7%</td>
    </tr>
  </tbody>
</table>

### Longitudinal platelet count trends are not strongly associated with the development of thrombosis in COVID-19 patients

Among the 246 COVIDpos patients with longitudinal lab testing data, 81 were serially tested starting at clinical presentation for fibrinogen versus 245 tested for platelets. As such, we first analyzed whether associations exist between platelet counts (or temporal alterations thereof) and clotting propensity in this cohort. Among these 245, there were 169 patients without thrombosis after PCR-based diagnosis (non-thrombotic) and 76 patients with thrombosis (thrombotic). There is a statistically significant difference between the COVIDpos and COVIDneg cohorts in the platelet count at clinical presentation (Figure 5A). In particular, thrombocytopenia (platelet count <150×109/L) was observed in 29% (46 out of 154) COVIDpos and 21% (346 of 1661) COVIDneg patients at the time of diagnosis (Figure 5A). However, the platelet levels at this time point were not associated with the subsequent formation of a blood clot in the COVIDpos cohort (Figure 5B).

![Figure 5.](https://cdn.elifesciences.org/articles/59209/elife-59209-fig5-v2.jpg)

**Figure 5.:** Box plots of platelet counts, min/max values, and maximum levels of increase/decline at specific time intervals for COVIDpos and COVIDneg cohorts and subgroups of the COVIDpos cohort with and without thrombotic events after SARS-CoV-2 diagnosis. In the subplot (A), we show platelet counts for COVIDpos (red) and COVIDneg (blue) cohorts. In subplots (B-F), we show platelet counts for COVIDpos patients who did and did not subsequently develop thromboses (purple and black, respectively). Horizontal dotted gray lines correspond to upper and lower limits of normal platelet counts (150−450 × 109/L), and horizontal red line shows 100 × 109/L. At the top of each plot, Cohen’s D effect size and p-value from the Mann-Whitney statistical test are shown. (A) Platelet counts at the time of PCR testing for COVIDpos and COVIDneg cohorts. (B) Platelet counts at the time of PCR testing for COVIDpos patients who did and did not subsequently develop thromboses. (C) Maximum platelet counts (considering counts at and after positive PCR test date) for COVIDpos patients who did and did not subsequently develop thromboses. (D) Minimum platelet counts (considering counts at and after positive PCR test date) for COVIDpos patients who did and did not subsequently develop thromboses. (E) Maximum degree of platelet increases after positive PCR test date for COVIDpos patients who did and did not subsequently develop thromboses. (F) Maximum degree of platelet declines after positive PCR test date for COVIDpos patients who did and did not subsequently develop thromboses.

We hypothesized that the previously discussed increase in platelet counts after COVID-19 diagnosis may be associated with the development of blood clots. If true, then we would expect the thrombotic COVIDpos cohort to show significantly higher maximum platelet counts during their course of disease progression compared to the non-thrombotic COVIDpos cohort. We found that this was not the case, as maximum platelet counts were similar in the two groups (Figure 5C). Similarly, among the 147 COVIDpos patients with platelet counts both at the time of clinical presentation and post-diagnosis, the degree of maximal platelet increase was not associated with the development of thrombosis (Figure 5E). It would certainly be of interest to perform this same analysis on a larger COVIDpos cohort (n = 2232; 101 thrombotic vs. 2131 non-thrombotic), but we were not able to do so given the lack of longitudinal testing available for a large majority of non-thrombotic COVIDpos patients (Table 4).

Conversely, we explored whether some COVIDpos patients may experience clotting in the setting of low or declining platelets (e.g. consumptive coagulopathy) despite the population-level trend of increasing platelets over time. Indeed, we found that nine of 74 thrombotic patients showed absolute platelet counts below 100 × 109/L during at least one post-diagnosis time window (below dotted red line in Figure 5D). In addition, we analyzed post-diagnosis platelet reductions among COVIDpos patients. While the maximum degree of absolute platelet reduction was not associated with clot development in aggregate (Figure 5F), we did find that six of the 52 thrombotic patients experienced a reduction of at least 100 × 109/L relative to the time of diagnosis. Of note, similar fractions of non-thrombotic COVIDpos patients also showed these low or declining platelet counts, indicating that these trends are not specific indicators of thrombosis (Figure 5D,F).

### Consumptive coagulopathy contributes to only a small fraction of COVID-19 associated thromboses

The observed declining platelet counts and thrombocytopenia in the context of thrombosis in a small fraction of COVIDpos patients are consistent with previous reports that fewer than 1% of survivors, but over 70% of non-survivors, meet the International Society on Thrombosis and Hemostasis (ISTH) criteria for disseminated intravascular coagulation (DIC; Tang et al., 2020). As was previously noted, hyperfibrinogenemia was among the strongest lab test features distinguishing COVIDpos from COVIDneg patients at diagnosis, but the subsequent downward trend (Figure 3A) could be attributed to a resolving acute phase response and/or consumption of fibrinogen in a systemic coagulopathy. Using our BERT-based sentiment extraction, we found that only five of the 2232 COVIDpos patients that exhibited DIC-like symptoms, all of whom were included in our longitudinal cohort of 246 COVIDpos patients (Table 4). Upon manual review of the EHR data for each patient, we found that two out of these five patients had confirmed diagnosis of DIC, while the remaining had high clinical suspicion and pending tests for DIC. This finding suggests that declining fibrinogen after COVID-19 diagnosis typically represents a physiologic return to normal range rather than pathologic coagulation factor consumption. To further examine the plasma fibrinogen trends among COVID-19 patients with DIC, with non-DIC thrombosis, and without thrombosis, we examined patient-level lab test trends from 10 individuals who were tested for fibrinogen both at the time of diagnosis and at least two times subsequently. The 10 patients for individual analysis were selected as the first 10 individuals with longitudinal fibrinogen lab testing data available.

This patient-level analysis indeed revealed multiple distinct trajectories with respect to fibrinogen and other coagulation parameters in COVIDpos patients. Four of these ten individuals developed at least one blood clot during their hospital course. Only one was identified by our BERT model (and confirmed by manual EHR review) to have low-grade DIC, and as expected we found this patient’s longitudinal lab test pattern to be consistent with consumptive coagulopathy (Patient 124; Figure 6A). At the time of diagnosis, this patient showed significant hyperfibrinogenemia with elevated D-dimers (1304.5 ng/mL) and a borderline normal platelet count (153 × 109/L). Over the next 10 days, this patient’s fibrinogen levels consistently decreased, reaching a minimum of 110 mg/dL on day 9. Similarly, after an initial recovery to 190 × 109/L the platelet counts consistently declined starting on day 2 post-diagnosis, reaching a minimum of 117 × 109/L on day 11. D-dimer levels exponentially increased after 5 days, reaching a maximum of 41,300 ng/mL on day 10. Phenotypically, this patient experienced both thrombotic (right internal jugular vein and right superior thyroid artery) and hemorrhagic (oropharyngeal and pulmonary) events. This combination of lab results and clinical manifestations is consistent with the diagnosis of DIC-like consumptive coagulopathy during the first week after COVID-19 diagnosis.

![Figure 6.](https://cdn.elifesciences.org/articles/59209/elife-59209-fig6-v2.jpg)

**Figure 6.:** In each plot, shaded regions represent time periods when the patient was taking a specific anticoagulant or antiplatelet medication. Medications taken for prophylaxis are denoted in the legend with (ppx). (A) Patient 124 developed hemorrhagic and thrombotic phenotypes in the context of declining fibrinogen, declining platelets, and increasing D-dimers. This is consistent with a DIC-like coagulopathy. (B) Patient 23 developed clots in the setting of declining fibrinogen and elevated D-dimers but stable platelet counts which increased shortly thereafter. (C) Patient 79 developed clots while showing increases in platelet counts along with plasma fibrinogen and D-dimers. (D) Patient 94 developed clots with relatively stable platelet counts and steadily declining plasma fibrinogen. (E) Patient 13 did not develop clots or bleeding despite a coordinate decrease in platelet counts and fibrinogen which may be mistaken for a DIC-like coagulopathy. (F) Patient 51 did not develop clots despite showing a post-diagnosis decline in plasma fibrinogen similar to several patients in the thrombotic cohort.

Lab test results from three other non-DIC thrombotic patients with longitudinal fibrinogen testing confirm the presence of alternative forms of coagulopathy in the COVID-19 population. Patient 23 developed a clot on day 4 post-diagnosis in the context of a declining fibrinogen level and increasing D-dimers but steady platelet counts, which actually increased shortly thereafter (Figure 6B). Patient 79 developed several clots after day 3 post-diagnosis in the setting of upward trending platelets (which eventually exceed the upper limit of normal) and elevated levels of both fibrinogen and D-dimers (Figure 6C). Patient 94 developed a clot on day 8 post-diagnosis with relatively stable platelet counts within normal limits and steadily declining fibrinogen levels (Figure 6D).

One hypothesis is that early elevations in plasma fibrinogen contribute to the clotting observed in the non-DIC like COVIDpos cohort. This hypothesis may warrant further analysis in cohorts with more longitudinal fibrinogen data, but again it is important to note that several COVIDpos patients who presented with hyperfibrinogenemia did not go on to develop thromboses (Figure 6E–F). This emphasizes that a steady post-diagnosis decline in plasma fibrinogen may represent physiologic resolution of the acute phase response rather than a pathologic consumption of fibrinogen and other coagulation factors (Figure 6B,D–F).

Taken together, this analysis affirms that a DIC-like coagulopathy resulting in a combination of hemorrhage and thrombosis can develop in the setting of COVID-19 infection. However, the observations that DIC was formally diagnosed in only five of 2232 COVIDpos patients and emphasizes that consumptive coagulopathy is an exception rather than the rule as it pertains to thrombotic phenotypes in COVID-19 patients. These results should be considered as a preliminary characterization of COVID-associated coagulopathies (CAC) and will be updated as patient counts increase with the continued evolution of the COVID-19 pandemic.

## Discussion

Many studies on clinical characteristics and lab tests are shedding light on the spectrum of hematological parameters associated with COVID-19 patients. In an initial study of 41 patients from Wuhan, the blood counts in COVIDpos patients showed leukopenia and lymphopenia, and prothrombin time and D-dimer levels were higher in ICU patients than in non-ICU patients (Huang et al., 2020). Another study based on 343 Wuhan COVIDpos patients found that a D‐dimer level of at least 2.0 µg/mL could predict mortality with a sensitivity of 92.3% and a specificity of 83.3% (Zhang et al., 2020). An independent study of 43 COVID-19 patients found significant differences between mild and severe cases in plasma interleukin‐6 (IL‐6), D‐dimers, glucose, thrombin time, fibrinogen, and C‐reactive protein (p<0.05; Gao et al., 2020). While such studies indeed highlight that hematological and inflammatory abnormalities are prevalent in COVIDpos, a high-resolution temporal understanding of how these parameters evolve in COVID-19 patients post diagnosis has not been established. Specifically, in the wake of accumulating evidence for hypercoagulability in COVIDpos patients, there are important clinical questions emerging regarding the necessity of and guidelines for thromboprophylaxis in patient management.

DIC-like consumptive coagulopathy in COVID-19 has been a point of concern in severely ill COVID-19 patients. Particularly in patients with ARDS, multiple organ dysfunction syndrome (MODS) is the predominant cause of death. A recent study suggested that DIC was associated with MODS during the early stage of ARDS and that persistent DIC may also have a role in this association (Gando et al., 2020). Our study focusing on COVID-19 patients with longitudinal lab data suggests that COVID-19 is indeed associated with modulation of coagulation related parameters such as platelet counts, fibrinogen levels, and clotting time (Figure 2). However, the majority of thrombotic events in COVID-19 patients with longitudinal lab testing are not the result of a DIC-like consumptive coagulopathy, as this only occurs in a small subset (Table 4).

The ability to derive this longitudinal understanding of COVID-19 progression, including laboratory abnormalities and their associated clinical manifestations, mandates the synthesis of structured and unstructured EHR data (e.g. lab tests and clinical notes) at a large scale. The fact that tens of thousands of patients have undergone SARS-CoV-2 testing at major academic medical centers (AMCs) provides an abundance of potential data to perform this analysis but also poses significant challenges from a practicality standpoint. Manual review and curation of patient trajectories and associated testing results is not practical. It is not likely to provide comprehensive or even entirely accurate individual patient records. Rather, triangulation across datasets, including lab measurements, clinical notes, and prescription information, using a scalable digitized approach to extract structured data along with sentiment-surrounded clinical phenotypes and outcomes enables us to efficiently perform this analysis in a timely fashion.

By developing and deploying such a digitized platform on the entirety of EHR data from a large AMC, we have identified in an unbiased manner, laboratory test-based abnormalities that differentiate COVIDpos patients from COVIDneg patients. The abnormalities in coagulation-related tests, including fibrinogen and platelets, were intriguing in the context of literature reporting the occurrence of various clotting phenotypes in COVID-19 patients, including DIC-like consumptive coagulopathies along with more isolated clotting events in the lungs, central nervous system, and other tissues (Tang et al., 2020; Klok et al., 2020; Levi et al., 2020). Our finding that consumptive coagulopathy represents a minority of COVID-19 associated clotting events provides context for other studies, which have reported overt DIC or DIC-like disease in over 70% of non-survivors but far lower fractions of survivors (Tang et al., 2020). As the pandemic continues to evolve and the patient counts increase over the coming months, we will be monitoring and reporting any updates to the clinical and laboratory observations drawn in this study.

Notwithstanding the preliminary nature of the analysis presented in this study, the results highlight that consumptive coagulopathy should be considered in the minority of COVIDpos patients with significant serial reductions in platelet counts. It remains to be seen whether the post-diagnosis platelet increases or early hyperfibrinogenemia which we observed may contribute mechanistically to the clotting in the much larger non-DIC thrombotic COVID-19 population. It is important to note that despite the trend of increasing platelets, the platelet count only extended above the normal range (>450×109/L) after the PCR date in few COVIDpos patients with serial measurements, and the development of such outright thrombocytosis was observed with similar frequencies in the thrombotic and non-thrombotic cohorts (Figure 5C). Further, the fact that several patients with elevated fibrinogen (i.e. >400 mg/dL) at presentation did not develop thromboses suggests that early hyperfibrinogenemia is not a singular driver of subsequent clotting events, but a small sample size (n = 10 patients; nine non-thrombotic vs. one thrombotic) limited the power of this analysis (Figure 6).

Despite these caveats, this linking of longitudinal trends to patient outcomes provides several useful pieces of clinical information. First, hyperfibrinogenemia is to be expected in COVID-19 patients around the time of diagnostic testing. Furthermore, declining fibrinogen levels shortly after diagnosis are also expected and likely represent the resolution of acute phase response in most patients rather than a decline secondary to the onset of consumptive coagulation. In addition, borderline or overt thrombocytopenia is common in COVID-19 patients at the time of clinical presentation, and the initial platelet count does not robustly predict patients who are likely to develop thromboses. After diagnosis, COVID-19 patients generally show an upward trend in platelets. Patients whose platelets trend down after diagnosis should be monitored, as platelet reductions after clinical presentation are associated with thromboses and significant reductions may be indicative of ongoing consumptive coagulopathy.

One unavoidable limitation of this study is that we restrict our analysis to patients which have longitudinal lab testing data available. While the inclusion criteria is naturally biased, we consider this study population to be of high clinical interest because these patients are highly enriched for severe thrombotic events during the study period (see Table 5). Further, in the propensity score matching step of the analysis, we are able to construct a control cohort that is similar to the COVIDpos cohort in these enriched dimensions. To provide additional color on the distinctive attributes of the study population, we provide a summary of the clinical characteristics of the study population versus all patients with PCR tests during the same time period (see Table 7). In addition, we provide the median numbers of lab tests per patient for selected coagulation-related lab tests (fibrinogen, platelets, PTT, APTT, D-dimer) and total lab tests (Tables 8 and 9).

**Table 7.**
 General characteristics of patients with SARS-CoV-2 PCR testing.General demographic characteristics of all patients who underwent SARS-CoV-2 PCR testing in the Mayo Clinic EHR database from February 15, 2020 to May 28, 2020. Includes summary characteristics for: (A) all patients with at least one SARS-CoV-2 PCR test, and (B) patients with at least one SARS-CoV-2 PCR test and longitudinal testing data available (i.e. patient received the same lab test on 3 separate days within + / − 30 days of PCR testing date).


<table>
  <tbody>
    <tr>
      <td colspan="3">(A) Demographics of all patients with PCR testing data</td>
    </tr>
    <tr>
      <td></td>
      <td>COVIDpos</td>
      <td>COVIDneg</td>
    </tr>
    <tr>
      <td>Total number of patients</td>
      <td>2232</td>
      <td>72,354</td>
    </tr>
    <tr>
      <td>Gender:</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Male</td>
      <td>1153 (52%)</td>
      <td>31,613 (44%)</td>
    </tr>
    <tr>
      <td>Female</td>
      <td>1074 (48%)</td>
      <td>40,714 (56%)</td>
    </tr>
    <tr>
      <td>Race:</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>White</td>
      <td>1115 (50%)</td>
      <td>62,605 (87%)</td>
    </tr>
    <tr>
      <td>Black</td>
      <td>420 (19%)</td>
      <td>2792 (3.9%)</td>
    </tr>
    <tr>
      <td>Asian</td>
      <td>151 (6.8%)</td>
      <td>1719 (2.4%)</td>
    </tr>
    <tr>
      <td>American Indian</td>
      <td>29 (1.3%)</td>
      <td>302 (0.42%)</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>517 (23%)</td>
      <td>4936 (6.8%)</td>
    </tr>
    <tr>
      <td colspan="10">(B) Demographics of patients with PCR testing data and longitudinal testing data</td>
    </tr>
    <tr>
      <td>Test</td>
      <td>Units</td>
      <td>Perturbation</td>
      <td>Original time window</td>
      <td>Count COVIDpos</td>
      <td>Count COVIDneg</td>
      <td>Mean COVIDpos</td>
      <td>Mean COVIDneg</td>
      <td>Cohen's D</td>
      <td>BH-adjusted M-W p-value</td>
    </tr>
    <tr>
      <td>Activated Partial Thrombopl Time, P</td>
      <td>sec</td>
      <td>−1 day</td>
      <td>Days 7–9 Post-Dx</td>
      <td>26</td>
      <td>72</td>
      <td>50.1</td>
      <td>38</td>
      <td>0.57</td>
      <td>0.034</td>
    </tr>
    <tr>
      <td>Activated Partial Thrombopl Time, P</td>
      <td>sec</td>
      <td>+1 day</td>
      <td>Days 7–9 Post-Dx</td>
      <td>17</td>
      <td>58</td>
      <td>55</td>
      <td>37.5</td>
      <td>0.81</td>
      <td>0.014</td>
    </tr>
    <tr>
      <td>Activated Partial Thrombopl Time, P</td>
      <td>sec</td>
      <td>−1 day</td>
      <td>Days 10–12 Post-Dx</td>
      <td>16</td>
      <td>57</td>
      <td>56.9</td>
      <td>38.4</td>
      <td>0.808</td>
      <td>9.10E-03</td>
    </tr>
    <tr>
      <td>Activated Partial Thrombopl Time, P</td>
      <td>sec</td>
      <td>+1 day</td>
      <td>Days 10–12 Post-Dx</td>
      <td>15</td>
      <td>60</td>
      <td>56.9</td>
      <td>38</td>
      <td>1.106</td>
      <td>2.60E-03</td>
    </tr>
    <tr>
      <td>Activated Partial Thrombopl Time, P</td>
      <td>sec</td>
      <td>−1 day</td>
      <td>Days 13–15 Post-Dx</td>
      <td>15</td>
      <td>52</td>
      <td>55.5</td>
      <td>37.8</td>
      <td>1.041</td>
      <td>0.014</td>
    </tr>
    <tr>
      <td>Activated Partial Thrombopl Time, P</td>
      <td>sec</td>
      <td>+1 day</td>
      <td>Days 13–15 Post-Dx</td>
      <td>14</td>
      <td>48</td>
      <td>51.8</td>
      <td>37.1</td>
      <td>0.962</td>
      <td>0.015</td>
    </tr>
    <tr>
      <td>Activated Partial Thrombopl Time, P</td>
      <td>sec</td>
      <td>−1 day</td>
      <td>Days 16–30 Post-Dx</td>
      <td>22</td>
      <td>156</td>
      <td>55.2</td>
      <td>37</td>
      <td>0.913</td>
      <td>5.70E-03</td>
    </tr>
    <tr>
      <td>Activated Partial Thrombopl Time, P</td>
      <td>sec</td>
      <td>+1 day</td>
      <td>Days 16–30 Post-Dx</td>
      <td>19</td>
      <td>139</td>
      <td>56</td>
      <td>38.2</td>
      <td>0.725</td>
      <td>3.80E-02</td>
    </tr>
    <tr>
      <td>Fibrinogen, P</td>
      <td>mg/dL</td>
      <td>−1 day</td>
      <td>Clinical presentation</td>
      <td>25</td>
      <td>92</td>
      <td>584.9</td>
      <td>370.7</td>
      <td>1.067</td>
      <td>1.20E-04</td>
    </tr>
    <tr>
      <td>Fibrinogen, P</td>
      <td>mg/dL</td>
      <td>+1 day</td>
      <td>Clinical presentation</td>
      <td>37</td>
      <td>292</td>
      <td>488.2</td>
      <td>326.2</td>
      <td>0.885</td>
      <td>8.80E-06</td>
    </tr>
    <tr>
      <td>Fibrinogen, P</td>
      <td>mg/dL</td>
      <td>−1 day</td>
      <td>Days 1–3 Post-Dx</td>
      <td>41</td>
      <td>381</td>
      <td>494.5</td>
      <td>318</td>
      <td>1.023</td>
      <td>3.90E-07</td>
    </tr>
    <tr>
      <td>Fibrinogen, P</td>
      <td>mg/dL</td>
      <td>+1 day</td>
      <td>Days 1–3 Post-Dx</td>
      <td>21</td>
      <td>244</td>
      <td>420.3</td>
      <td>312.2</td>
      <td>0.616</td>
      <td>7.90E-03</td>
    </tr>
    <tr>
      <td>Fibrinogen, P</td>
      <td>mg/dL</td>
      <td>−1 day</td>
      <td>Days 4–6 Post-Dx</td>
      <td>27</td>
      <td>156</td>
      <td>432.2</td>
      <td>336</td>
      <td>0.495</td>
      <td>0.045</td>
    </tr>
    <tr>
      <td>Fibrinogen, P</td>
      <td>mg/dL</td>
      <td>+1 day</td>
      <td>Days 4–6 Post-Dx</td>
      <td>24</td>
      <td>105</td>
      <td>472.2</td>
      <td>333.2</td>
      <td>0.712</td>
      <td>0.025</td>
    </tr>
    <tr>
      <td>Platelets</td>
      <td>×10(9)/L</td>
      <td>−1 day</td>
      <td>Pre-diagnosis</td>
      <td>34</td>
      <td>575</td>
      <td>187.3</td>
      <td>225.6</td>
      <td>−0.357</td>
      <td>0.057</td>
    </tr>
    <tr>
      <td>Platelets</td>
      <td>×10(9)/L</td>
      <td>+1 day</td>
      <td>Pre-diagnosis</td>
      <td>118</td>
      <td>1533</td>
      <td>201.3</td>
      <td>234.4</td>
      <td>−0.328</td>
      <td>7.30E-04</td>
    </tr>
  </tbody>
</table>

**Table 8.**
 Lab test data availability in patients with SARS-CoV-2 PCR testing.Lab test data availability for all patients who underwent SARS-CoV-2 PCR testing in the Mayo Clinic EHR database from February 15, 2020 to May 28, 2020. Includes counts of lab tests and counts of patients with 1+ and 3+ lab tests both overall and for selected coagulation-related lab tests (activated partial thromboplastin time, D-dimer, fibrinogen, platelets, and prothrombin time).


<table>
  <thead>
    <tr>
      <th></th>
      <th>COVIDpos</th>
      <th>COVIDneg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Total number of patients</td>
      <td>2232</td>
      <td>72,354</td>
    </tr>
    <tr>
      <td>Number of patients with 1+ lab test</td>
      <td>566 (25%)</td>
      <td>35,188 (49%)</td>
    </tr>
    <tr>
      <td>Number patents with 1+ test from day −30 to day −1</td>
      <td>299 (13%)</td>
      <td>23,116 (32%)</td>
    </tr>
    <tr>
      <td>Number patents with 1+ test from day 0 to day 30</td>
      <td>452 (20%)</td>
      <td>28,666 (40%)</td>
    </tr>
    <tr>
      <td>Number of patients with 3+ lab tests of the same type</td>
      <td>246 (11%)</td>
      <td>13,666 (19%)</td>
    </tr>
    <tr>
      <td>Total number of lab tests</td>
      <td>98,753</td>
      <td>32,40,491</td>
    </tr>
    <tr>
      <td>Number of lab tests from day −30 to day −1</td>
      <td>12,120</td>
      <td>10,33,762</td>
    </tr>
    <tr>
      <td>Number of lab tests from day 0 to day 30</td>
      <td>86,633</td>
      <td>22,06,729</td>
    </tr>
    <tr>
      <td colspan="2">ACTIVATED PTT</td>
      <td></td>
    </tr>
    <tr>
      <td>Number of lab tests</td>
      <td>362</td>
      <td>6042</td>
    </tr>
    <tr>
      <td>Number of patients with 1+ lab test</td>
      <td>93 (4.0%)</td>
      <td>3544 (4.9%)</td>
    </tr>
    <tr>
      <td>Number of patients with 3+ lab tests</td>
      <td>20 (0.86%)</td>
      <td>406 (0.56%)</td>
    </tr>
    <tr>
      <td colspan="2">D-DIMER, P</td>
      <td></td>
    </tr>
    <tr>
      <td>Number of lab tests</td>
      <td>911</td>
      <td>2846</td>
    </tr>
    <tr>
      <td>Number of patients with 1+ lab test</td>
      <td>247 (11%)</td>
      <td>2395 (3.3%)</td>
    </tr>
    <tr>
      <td>Number of patients with 3+ lab tests</td>
      <td>99 (4.4%)</td>
      <td>56 (0.077%)</td>
    </tr>
    <tr>
      <td colspan="2">FIBRINOGEN, P</td>
      <td></td>
    </tr>
    <tr>
      <td>Number of lab tests</td>
      <td>278</td>
      <td>3,017</td>
    </tr>
    <tr>
      <td>Number of patients with 1+ lab test</td>
      <td>84 (3.8%)</td>
      <td>1217 (1.7%)</td>
    </tr>
    <tr>
      <td>Number of patients with 3+ lab tests</td>
      <td>18 (0.81%)</td>
      <td>273 (0.38%)</td>
    </tr>
    <tr>
      <td>PLATELETS</td>
      <td colspan="2"></td>
    </tr>
    <tr>
      <td>Number of lab tests</td>
      <td>2646</td>
      <td>1,08,722</td>
    </tr>
    <tr>
      <td>Number of patients with 1+ lab test</td>
      <td>500 (22%)</td>
      <td>30,732 (42%)</td>
    </tr>
    <tr>
      <td>Number of patients with 3+ lab tests</td>
      <td>231 (10%)</td>
      <td>11544 (16%)</td>
    </tr>
    <tr>
      <td>PROTHROMBIN TIME, P</td>
      <td></td>
    </tr>
    <tr>
      <td>Number of lab tests</td>
      <td>711</td>
      <td>28,007</td>
    </tr>
    <tr>
      <td>Number of patients with 1+ lab test</td>
      <td>197 (8.8%)</td>
      <td>10,446 (14%)</td>
    </tr>
    <tr>
      <td>Number of patients with 3+ lab tests</td>
      <td>46 (2.1%)</td>
      <td>2502 (3.5%)</td>
    </tr>
  </tbody>
</table>

**Table 9.**
 Lab test data availability in patients with SARS-CoV-2 PCR testing and longitudinal lab data.Lab test data availability for all patients who underwent SARS-CoV-2 PCR testing in the Mayo Clinic EHR database from February 15, 2020 to May 28, 2020 with longitudinal testing data available (i.e. patient received the same lab test on three separate days within + / − 30 days of PCR testing date). Includes counts of lab tests and counts of patients with 1+ and 3+ lab tests both overall and for selected coagulation-related lab tests (activated partial thromboplastin time, D-dimer, fibrinogen, platelets, and prothrombin time).


<table>
  <thead>
    <tr>
      <th></th>
      <th>COVIDpos</th>
      <th>COVIDneg</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Total number of patients</td>
      <td>246</td>
      <td>13,666</td>
    </tr>
    <tr>
      <td>Number patents with 1+ test from day −30 to day −1</td>
      <td>150 (61%)</td>
      <td>11,567 (85%)</td>
    </tr>
    <tr>
      <td>Number patents with 1+ test from day 0 to day 30</td>
      <td>240 (98%)</td>
      <td>13,501 (99%)</td>
    </tr>
    <tr>
      <td>Total number of lab tests</td>
      <td>89,587</td>
      <td>2,634,070</td>
    </tr>
    <tr>
      <td>Number of lab tests from day −30 to day −1</td>
      <td>8698</td>
      <td>763,808</td>
    </tr>
    <tr>
      <td>Number of lab tests from day 0 to day 30</td>
      <td>80,889</td>
      <td>1,870,262</td>
    </tr>
    <tr>
      <td>ACTIVATED PTT</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Number of lab tests</td>
      <td>355</td>
      <td>5186</td>
    </tr>
    <tr>
      <td>Number of patients with 1+ lab test</td>
      <td>86 (35%)</td>
      <td>2722 (20%)</td>
    </tr>
    <tr>
      <td>Number of patients with 3+ lab tests</td>
      <td>20 (8.1%)</td>
      <td>406 (3.0%)</td>
    </tr>
    <tr>
      <td>D-DIMER, P</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Number of lab tests</td>
      <td>855</td>
      <td>1720</td>
    </tr>
    <tr>
      <td>Number of patients with 1+ lab test</td>
      <td>197 (80%)</td>
      <td>1293 (9.5%)</td>
    </tr>
    <tr>
      <td>Number of patients with 3+ lab tests</td>
      <td>99 (40%)</td>
      <td>56 (0.41%)</td>
    </tr>
    <tr>
      <td>FIBRINOGEN, P</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Number of lab tests</td>
      <td>275</td>
      <td>2965</td>
    </tr>
    <tr>
      <td>Number of patients with 1+ lab test</td>
      <td>81 (33%)</td>
      <td>1168 (8.5%)</td>
    </tr>
    <tr>
      <td>Number of patients with 3+ lab tests</td>
      <td>18 (7.3%)</td>
      <td>273 (2%)</td>
    </tr>
    <tr>
      <td>PLATELETS</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Number of lab tests</td>
      <td>2343</td>
      <td>87,517</td>
    </tr>
    <tr>
      <td>Number of patients with 1+ lab test</td>
      <td>245 (100%)</td>
      <td>13,399 (98%)</td>
    </tr>
    <tr>
      <td>Number of patients with 3+ lab tests</td>
      <td>231 (94%)</td>
      <td>11,544 (84%)</td>
    </tr>
    <tr>
      <td>PROTHROMBIN TIME, P</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Number of lab tests</td>
      <td>676</td>
      <td>24,489</td>
    </tr>
    <tr>
      <td>Number of patients with 1+ lab test</td>
      <td>165 (67%)</td>
      <td>7209 (53%)</td>
    </tr>
    <tr>
      <td>Number of patients with 3+ lab tests</td>
      <td>46 (19%)</td>
      <td>2502 (18%)</td>
    </tr>
  </tbody>
</table>

It is important to note that while we center the study period around the PCR testing date, this date may not correspond to the same disease state of COVID-19 for each individual in the COVIDpos cohort. To account for the potential variability in disease progression, we have performed a sensitivity analysis on the time intervals (Table 3). Additionally, there are several covariates that may influence these longitudinal trends and should be explored further. For example, we have already considered whether previous or concomitant administration of anticoagulants or antiplatelet agents influences patient lab test results and/or outcomes. Similarly, in the future, we intend to explore whether longitudinal lab measurement trends differ between outpatient, inpatient, and ICU admitted patient cohorts. New datasets can also be utilized; for example, rather than grouping patients by the identified thromboembolic phenotypes extracted from the clinical notes alone, patients could be stratified by those who had imaging studies (duplex ultrasound, CT scan, etc.) performed, and phenotypes could be directly extracted from these procedural reports. As more data accumulates from COVIDpos and COVIDneg patients in the coming months, these analyses need to be expanded to assess similarities and differences in the temporal trends of laboratory test results among a wider range of patient subgroups relevant for COVID-19 outcomes, such as those who have pre-existing conditions (e.g. diabetes, hypertension, obesity, malignancies) or patients who are on specific medication (e.g. ACE inhibitors, statins, immunosuppressants).

In summary, this work demonstrates significant progress toward enabling scaled and digitized analyses of longitudinal unstructured and structured EHRs to identify variables (e.g. laboratory results) which are associated with relevant clinical phenotypes (e.g. COVID-19 diagnosis and outcomes). In doing so, we identified trends in lab test results which may be relevant to monitor in COVID-19 patients and warrant both clinical and mechanistic follow-up in more targeted and explicitly controlled prospective analyses.

## Materials and methods

### Study design, setting and patient population

This is a retrospective study of patients who underwent polymerase chain reaction (PCR) testing for suspected SARS-CoV-2 infection at the Mayo Clinic and hospitals affiliated to the Mayo health system. This research was conducted under IRB 20–003278, ‘Study of COVID-19 patient characteristics with augmented curation of Electronic Health Records (EHR) to inform strategic and operational decisions’. For further information regarding the Mayo Clinic Institutional Review Board (IRB) policy, and its institutional commitment, membership requirements, review of research, informed consent, recruitment, vulnerable population protection, biologics, and confidentiality policy, please refer to www.mayo.edu/research/institutional-review-board/overview.

### Longitudinal lab testing tied to COVID-19 PCR diagnostic testing

We analyzed data from 74,586 patients who received PCR tests from the Mayo Clinic between February 15, 2020 to May 28, 2020. Among this population, 2232 patients had at least one positive SARS-CoV-2 PCR test result, and 72,354 patients had all negative PCR test results. In order to align the data for the analysis of aggregate longitudinal trends, we selected a reference date for each patient. For patients in the COVIDpos cohort, we used the date of the first positive PCR test result as the reference date (day = 0). For patients with all negative PCR tests, we used the date of the first PCR test result as the reference date (day = 0). We defined the study period for each patient to be 30 days before and after the PCR testing date. Patients with contradictory PCR test results were excluded for the purpose of this analysis; for example, a positive PCR test result and a negative PCR test result on the same day, or a positive PCR test result followed immediately by several negative PCR test results.

Over 4 million test results from 6298 different types of lab tests were recorded for the patients who received PCR tests in the 60-day window surrounding their PCR testing dates at the Mayo Clinic campuses in Minnesota, Arizona, and Florida. Among these lab tests, we restricted our analysis to 194 tests with at least 1000 observations total and at least 10 observations from the COVIDpos cohort among the patients with PCR testing on or before May 8, 2020. In addition, we considered different subsets of the COVIDpos cohort for the analysis of each of the 194 lab tests, due to differences in availability of testing results. For each lab test, we consider the results from patients with three or more observations during the study period.

In the end, there are 246 SARS-COV-2 positive and 13,666 SARS-CoV-2 negative patients that had three or more test results during the study period for at least one of the assays among the 194 lab tests considered. We take this set of 246 COVID-19 positive patients to be the COVIDpos cohort. In order to construct the COVIDneg cohort from the 13,666 COVID-19 negative patients, we apply propensity score matching, which is described in the next section.

### Propensity score matching to select the final COVIDneg cohort

To construct a COVIDneg cohort similar in baseline clinical covariates to the COVIDpos cohort, we employ 1:10 propensity score matching (Austin, 2011). In particular, first we trained a regularized logistic regression model to predict the likelihood that each patient will have a positive or negative COVID-19 test result, using the following covariates: demographics (age, gender, race), anticoagulant/antiplatelet medication use (orders for alteplase, antithrombin III, apixaban, argatroban, aspirin, bivalirudin, clopidogrel, dabigatran, dalteparin, enoxaparin, eptifibatide, heparin, rivaroxaban, warfarin in the past year and in the past 30 days), pre-existing coagulopathies (medical history of thrombotic phenotypes including: deep vein thrombosis, pulmonary embolism, myocardial infarction, venous thromboembolism, thrombotic stroke, cerebral venous thrombosis, and disseminated intravascular coagulation from day −365 to day −31 relative to the PCR testing date), and hospitalization status (i.e. whether or not the patient was hospitalized within the past 30 days of PCR testing).

Using the predictions from the logistic regression model as propensity scores, we then matched each of the 246 patients in the COVIDpos cohort to 10 patients out of the 13,666 COVID-19 negative patients, using greedy nearest-neighbor matching without replacement (Austin, 2011; Austin, 2014). As a result, we ended up with a final COVIDneg cohort that included 2460 patients with similar baseline characteristics to the COVIDpos cohort. The characteristics of the two cohorts are summarized in Table 1.

Further, for the analyses conducted on individual lab tests, which include only a subset of patients from the COVIDpos cohort, we use the propensity scores to match each patient from the COVIDpos cohort to 10 patients from the COVIDneg cohort which have the most similar propensity scores and lab tests available. For example, for the fibrinogen lab test, in which we have data on 81 patients from the COVIDpos cohort, we select 810 patients from the COVIDneg cohort and the most similar propensity scores to be the control group. In this way, we ensure that all of the comparisons are done between subsets of the positive and negative cohorts with similar propensity scores, and therefore similar underlying characteristics.

### Statistical significance assessments for lab test differences over prognostic time intervals for SARS-CoV-2 infection

We conduct a systematic statistical analysis to identify tests that show significant differentiation among the COVIDpos cohort during a set of predetermined prognostic time intervals for SARS-CoV-2 infection. In particular, we group the lab test measurements for each patient into the following nine time intervals relative to their date of PCR testing: pre-infection (days −30 to −11), pre-PCR (days −10 to −2), time of clinical presentation (days −1 to 0), and post-PCR phases 1 (days 1 to 3), 2 (days 4 to 6), 3 (days 7 to 9), 4 (days 10 to 12), 5 (days 13 to 15), and 6 (days 16 to 30).

For each lab test and for each of each of our nine pre-specified time intervals, we compared the mean lab test value among patients who underwent at least one such lab test in the COVIDpos cohort over that time interval to the mean lab test value in the COVIDneg (matched) cohort over that time window. We only considered (lab test, time interval) pairs in which there were at least three patients contributing to laboratory test results in both groups. Specifically, for each (lab test, time interval) pair, we conducted the following procedure:

Once we have the statistics and p-values for each (test, time window) pair, in order to account for multiple hypotheses, we apply the Benjamini-Hochberg (BH) procedure with FDR controlled at 0.05. The results from the systematic comparisons which met our thresholds for effect size and statistical significance (Cohen’s D > 0.35, BH-adjusted Mann-Whitney p-value <0.05) are shown in Table 2.

### Sensitivity analysis to assess the impact of perturbed clinical time windows

We perform a sensitivity analysis to assess whether or not the key findings from the systematic statistical assessment remain the same if we perturb the considered time intervals. In particular, we repeat the statistical analysis with the time intervals shifted forward or backward 1 day for all patients. For the forward shifted sensitivity analysis, the new time intervals under consideration are: pre-infection (days −30 to −10), pre-PCR (days −9 to −1), time of clinical presentation (days 0 to 1), and post-PCR phases 1 (days 2 to 4), 2 (days 5 to 7), 3 (days 8 to 10), 4 (days 11 to 13), 5 (days 14 to 16), and 6 (days 17 to 30). For the backward shifted sensitivity analysis, the new time intervals under consideration are: pre-infection (days −30 to −12), pre-PCR (days −11 to −3), time of clinical presentation (days −2 to −1), and post-PCR phases 1 (days 0 to 2), 2 (days 3 to 5), 3 (days 6 to 8), 4 (days 9 to 11), 5 (days 12 to 14), and 6 (days 15 to 30). For both the forward and backward sensitivity analyses, we apply the same thresholds of effect size and significance (Cohen’s D > 0.35, BH-adjusted Mann-Whitney p-value <0.05), and we compare the results to the original time intervals.

From this analysis, we observe consistent results (i.e. comparisons meeting same criteria of significance and effect) on (i) both perturbations in 83 out of 130 (64%) lab test trends identified in Table 2 and (ii) at least one perturbation in 114 of 130 (87%) lab test trends. In Table 3, we report the specific results of the time shifted windows for five coagulation-related lab tests (fibrinogen, platelets, prothrombin time, activated partial thromboplastin time, and D-dimer).

### Augmented curation of anticoagulant administration and the coagulopathy outcomes from the unstructured clinical notes and their triangulation to structured EHR databases

A state-of-the-art BERT-based neural network (Devlin et al., 2018) was previously developed to classify sentiment regarding a diagnosis in the EHR (Wagner et al., 2020). Sentences containing phenotypes were classified into the following categories: Yes (confirmed diagnosis), No (ruled out diagnosis), Maybe (possibility of disease), and Other (alternate context, e.g. family history of disease). The neural network used to perform this classification was trained using nearly 250 different phenotypes and 18,500 sentences and achieves 93.6% overall accuracy and over 95% precision and recall for Yes/No sentiment classification (Wagner et al., 2020). Here, this model was used to classify the sentiment around coagulopathies in the unstructured text of the 246 COVIDpos and 13,666 COVIDneg patients’ clinical notes, structuring this information so that it could be compiled with longitudinal lab measurement and medication information.

In particular, we used the BERT model to identify the seven coagulopathy phenotypes mentioned in clinical notes in the Mayo Clinic EHR database, including: deep vein thrombosis, pulmonary embolism, myocardial infarction, venous thromboembolism, thrombotic stroke, cerebral venous thrombosis, and disseminated intravascular coagulation. We validated the performance of this model for these phenotypes on a set of 1000 randomly selected sentences from the clinical notes of the patients in the study population. In Table 6, we report the out-of-sample accuracy metrics for the BERT model on this set of sentences, using manually curated labels provided by one of the study’s authors (CP) to be the ground truth. We demonstrate that the model performs well in the task of identifying thrombotic phenotypes in clinical notes, with an overall accuracy of 94.7%, recall of 97.8%, and precision of 92.8%.
