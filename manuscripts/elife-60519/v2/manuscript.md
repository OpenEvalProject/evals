# Early prediction of level-of-care requirements in patients with COVID-19

## Authors

- Boran Hao<sup>1</sup>
- Shahabeddin Sotudian<sup>1</sup> ([ORCID: 0000-0002-5864-6192](https://orcid.org/0000-0002-5864-6192))
- Taiyao Wang<sup>1</sup> ([ORCID: 0000-0002-0331-3892](https://orcid.org/0000-0002-0331-3892))
- Tingting Xu<sup>1</sup>
- Yang Hu<sup>1</sup>
- Apostolos Gaitanidis<sup>2</sup>
- Kerry Breen<sup>2</sup>
- George C Velmahos<sup>2</sup>
- Ioannis Ch Paschalidis<sup>1</sup> ([ORCID: 0000-0002-3343-2913](https://orcid.org/0000-0002-3343-2913)) †

### Affiliations

1. Center for Information and Systems Engineering, Boston University Boston United States
2. Division of Trauma, Emergency Services, and Surgical Critical Care Massachusetts General Hospital, Harvard Medical School Boston United States

† Corresponding author

## Abstract

This study examined records of 2566 consecutive COVID-19 patients at five Massachusetts hospitals and sought to predict level-of-care requirements based on clinical and laboratory data. Several classification methods were applied and compared against standard pneumonia severity scores. The need for hospitalization, ICU care, and mechanical ventilation were predicted with a validation accuracy of 88%, 87%, and 86%, respectively. Pneumonia severity scores achieve respective accuracies of 73% and 74% for ICU care and ventilation. When predictions are limited to patients with more complex disease, the accuracy of the ICU and ventilation prediction models achieved accuracy of 83% and 82%, respectively. Vital signs, age, BMI, dyspnea, and comorbidities were the most important predictors of hospitalization. Opacities on chest imaging, age, admission vital signs and symptoms, male gender, admission laboratory results, and diabetes were the most important risk factors for ICU admission and mechanical ventilation. The factors identified collectively form a signature of the novel COVID-19 disease.

## Introduction

As a result of the SARS-CoV-2 pandemic, many hospitals across the world have resorted to drastic measures: canceling elective procedures, switching to remote consultations, designating most beds to COVID-19, expanding Intensive Care Unit (ICU) capacity, and re-purposing doctors and nurses to support COVID-19 care. In the U.S., the CDC estimates more than 310,000 COVID-19 hospitalizations from March 1 to June 13, 2020 (CDC, 2020).

Much of the modeling work related to the pandemic has focused on spread dynamics (Kucharski et al., 2020). Others have described patients who were hospitalized (Richardson et al., 2020) (n = 5700) and (Buckner et al., 2020) (n = 105), became critically ill (Gong et al., 2020) (n = 372), or succumbed to the disease (n = 1625 (Onder et al., 2020), n = 270 [Wu et al., 2020]). In data from the New York City, 14.2% required ICU treatment and 12.2% mechanical ventilation (Richardson et al., 2020). With such rates, the logistical and ethical implications of bed allocation and potential rationing of care delivery are immense (White and Lo, 2020). To date, while state- or country-level prognostication has developed to examine resource allocation at a mass scale, there is inadequate evidence based on a large cohort on accurate prediction of the disease progress at the individual patient level. A string of recent studies developed models to predict severe disease or mortality based on clinical and laboratory findings, for example (Yan et al., 2020) (n = 485), (Gong et al., 2020) (n = 372), (Bhargava et al., 2020) (n = 197), (Ji et al., 2020) (n = 208), and (Wang et al., 2020) (n = 296). In these studies, several variables such as Lactate Dehydrogenase (LDH) (Gong et al., 2020; Ji et al., 2020; Yan et al., 2020) and C-reactive protein (CRP) have been identified as important predictors. All of these studies considered relatively small cohorts and, with the exception of Bhargava et al., 2020, considered patients in China. Although it is believed that the virus remains the same around the globe, the physiologic response to the virus and the eventual course of disease depend on multiple other factors, many of them regional (e.g. population characteristics, hospital practices, prevalence of pre-existing conditions) and not applicable universally. Triage of adult patients with COVID-19 remains challenging with most evidence coming from expert recommendations; evidence-based methods based on larger U.S.-based cohorts have not been reported (Sprung et al., 2020).

Leveraging data from five hospitals of the largest health care system in Massachusetts, we seek to develop personalized, interpretable predictive models of (i) hospitalization, (ii) ICU treatment, and (iii) mechanical ventilation, among SARS-CoV-2 positive patients. To develop these models, we developed a pipeline leveraging state-of-the-art Natural Language Processing (NLP) tools to extract information from the clinical reports for each patient, employing statistical feature selection methods to retain the most predictive features for each model, and adapting a host of advance machine learning-based classification methods to develop parsimonious (hence, easier to use and interpret) predictive models. We found that the more interpretable models can, for the most part, deliver similar predictive performance compared to more complex, ‘black-box’ models involving ensembles of many decision trees. Our results support our initial hypothesis that important clinical outcomes can be predicted with a high degree of accuracy upon the patient’s first presentation to the hospital using a relatively small number of features, which collectively compose a ‘signature’ of the novel COVID-19 disease.

## Results

We extracted data for all patients (n = 2566) who had a positive RT-PCR SARS-CoV-2 test between March 4 and April 13, 2020 at five Massachusetts hospitals, included in the same health care system (Massachusetts General Hospital (MGH), Brigham and Women’s Hospital (BWH), Faulkner Hospital (FH), Newton-Wellesley Hospital (NWH), and North Shore Medical Center (NSM)). The study was approved by the pertinent Institutional Review Boards.

Demographics, pre-hospital medications, and comorbidities were extracted for each patient based on the electronic medical record. Patient symptoms, vital signs, radiologic findings, and laboratory results were recorded at their first hospital presentation (either clinic or emergency department) before testing positive for SARS-CoV-2. A total of 164 features were extracted for each patient. ICU admission and mechanical ventilation were determined for each patient. Complete blood count values were considered as absolute counts. Representative statistics comparing hospitalized, ICU admitted, and mechanically ventilated patients are provided in Table A1 (Appendix). Table A2 (Appendix) reports how patients were distributed among the five hospitals.

Among the 2566 patients with a positive test, 930 (36.2%) were hospitalized. Among the hospitalized, 273 (29.4% of the hospitalized) required ICU care of which 217 (79.5%) required mechanical ventilation. The mean age over all patients was 51.9 years (SD: 18.9 years) and 45.6% were male.

### Hospitalization

The mean age of hospitalized patients was 62.3 years (SD: 18 years) and 55.3% were male. We employed linear and non-linear classification methods for predicting hospitalizations. Non-linear methods included random forests (RF) (Breiman, 2001) and XGBoost (Chen and Guestrin, 2016). Linear methods included support vector machines (SVM) (Cortes and Vapnik, 1995) and Logistic Regression (LR); each linear method used either ℓ1- or ℓ2-norm regularization and we report the best-performing flavor of each model.

Results are reported in Table 1. We report the Area Under the Curve (AUC) of the Receiver Operating Characteristic (ROC) and the Weighted-F1 score, both computed out-of-sample (in a test set not used for training the model). As we detail under Methods, we used two validation strategies. The ‘Random’ strategy randomly split the patients into a training and a test set and was repeated five times; from these five splits we report the average and the standard deviation of the test performance. The ‘BWH’ strategy trained the models on MGH, FH, NWH, and NSM patients, and evaluated performance on BWH patients.

**Table 1.**
 Hospitalization prediction model (test performance).The values inside the parentheses refer to the standard deviation of the corresponding metric. Random refers to test set results from the five random training/test splits. BWH refers to training on four other hospitals and testing on data from BWH. SVM-L1 and LR-L1 refer to the ℓ1-norm regularized SVM and LR models. For the parsimonious model, we list the LR coefficients of each variable (Coef), the correlation of the variable with the outcome (Y-corr), the mean of the variable (Y1-mean) in the positive class (hospitalized for this table), and the mean of the variable (Y0-mean) in the negative class (non-hospitalized). Binary Coef denotes the coefficient of the variables in the binarized model. We report the corresponding odds ratio (OR) and the 95% confidence intervals (CI). Thresholds used for the binarized model are provided in Appendix 1—table 5.


<table>
  <tbody>
    <tr>
      <td rowspan="2" colspan="2">Algorithm</td>
      <td colspan="4">AUC</td>
      <td colspan="4">F1-weighted</td>
    </tr>
    <tr>
      <td colspan="2">Random</td>
      <td colspan="2">BWH</td>
      <td colspan="2">Random</td>
      <td colspan="2">BWH</td>
    </tr>
    <tr>
      <td colspan="2"></td>
      <td colspan="8">Models using all 106 features</td>
    </tr>
    <tr>
      <td colspan="2">LR-L2</td>
      <td colspan="2">87.0% (1.7%)</td>
      <td colspan="2">85.9%</td>
      <td colspan="2">81.6% (1.3%)</td>
      <td colspan="2">84.2%</td>
    </tr>
    <tr>
      <td colspan="2">SVM-L1</td>
      <td colspan="2">87.0% (1.6%)</td>
      <td colspan="2">85.8%</td>
      <td colspan="2">81.5% (1.5%)</td>
      <td colspan="2">83.9%</td>
    </tr>
    <tr>
      <td colspan="2">XGBoost</td>
      <td colspan="2">87.8% (1.9%)</td>
      <td colspan="2">87.7%</td>
      <td colspan="2">80.9% (1.8%)</td>
      <td colspan="2">83.3%</td>
    </tr>
    <tr>
      <td colspan="2">RF</td>
      <td colspan="2">88.2% (1.6%)</td>
      <td colspan="2">88.1%</td>
      <td colspan="2">81.2% (1.1%)</td>
      <td colspan="2">83.2%</td>
    </tr>
    <tr>
      <td colspan="2"></td>
      <td colspan="8">Models using 74 statistically selected features</td>
    </tr>
    <tr>
      <td colspan="2">LR-L2</td>
      <td colspan="2">87.1% (1.7%)</td>
      <td colspan="2">86.0%</td>
      <td colspan="2">82.0% (1.3%)</td>
      <td colspan="2">83.9%</td>
    </tr>
    <tr>
      <td colspan="2">SVM-L1</td>
      <td colspan="2">87.1% (1.7%)</td>
      <td colspan="2">85.8%</td>
      <td colspan="2">82.0% (1.4%)</td>
      <td colspan="2">84.0%</td>
    </tr>
    <tr>
      <td colspan="2">XGBoost</td>
      <td colspan="2">87.9% (1.9%)</td>
      <td colspan="2">87.6%</td>
      <td colspan="2">81.2% (1.9%)</td>
      <td colspan="2">84.2%</td>
    </tr>
    <tr>
      <td colspan="2">RF</td>
      <td colspan="2">88.0% (1.7%)</td>
      <td colspan="2">88.1%</td>
      <td colspan="2">80.8% (1.7%)</td>
      <td colspan="2">83.9%</td>
    </tr>
    <tr>
      <td colspan="2"></td>
      <td colspan="8">Parsimonious Model using 11 features</td>
    </tr>
    <tr>
      <td colspan="2">LR-L2</td>
      <td colspan="2">83.4% (1.7%)</td>
      <td colspan="2">83.7%</td>
      <td colspan="2">78.7% (0.9%)</td>
      <td colspan="2">81.0%</td>
    </tr>
    <tr>
      <td colspan="2">SVM-L1</td>
      <td colspan="2">83.4% (1.7%)</td>
      <td colspan="2">83.8%</td>
      <td colspan="2">78.1% (1.1%)</td>
      <td colspan="2">79.9%</td>
    </tr>
    <tr>
      <td colspan="10">Variables for the Parsimonious Model</td>
    </tr>
    <tr>
      <td>Variable</td>
      <td>Coef</td>
      <td>Y1 mean</td>
      <td>Y0 mean</td>
      <td>p-value</td>
      <td>Y-corr</td>
      <td>Coef binary</td>
      <td>OR</td>
      <td colspan="2">OR 95% CI</td>
    </tr>
    <tr>
      <td>SpO2 (%)</td>
      <td>−11.90</td>
      <td>95.44</td>
      <td>97.11</td>
      <td>&lt;0.001</td>
      <td>−0.29</td>
      <td>1.74</td>
      <td>5.67</td>
      <td>3.97</td>
      <td>8.12</td>
    </tr>
    <tr>
      <td>Temperature</td>
      <td>10.36</td>
      <td>37.21</td>
      <td>37.06</td>
      <td>&lt;0.001</td>
      <td>0.08</td>
      <td>0.86</td>
      <td>2.36</td>
      <td>1.76</td>
      <td>3.18</td>
    </tr>
    <tr>
      <td>Respiratory Rate</td>
      <td>7.20</td>
      <td>22.82</td>
      <td>20.83</td>
      <td>&lt;0.001</td>
      <td>0.18</td>
      <td>−0.13</td>
      <td>0.88</td>
      <td>0.69</td>
      <td>1.13</td>
    </tr>
    <tr>
      <td>Age</td>
      <td>5.14</td>
      <td>62.31</td>
      <td>46.02</td>
      <td>&lt;0.001</td>
      <td>0.41</td>
      <td>0.88</td>
      <td>2.4</td>
      <td>1.86</td>
      <td>3.11</td>
    </tr>
    <tr>
      <td>Pulse</td>
      <td>4.60</td>
      <td>90.09</td>
      <td>90.4</td>
      <td>&lt;0.001</td>
      <td>−0.01</td>
      <td>0.7</td>
      <td>2.01</td>
      <td>1.49</td>
      <td>2.71</td>
    </tr>
    <tr>
      <td>Diastolic BP</td>
      <td>−3.56</td>
      <td>73.07</td>
      <td>77.21</td>
      <td>&lt;0.001</td>
      <td>−0.23</td>
      <td>1.51</td>
      <td>4.51</td>
      <td>2.88</td>
      <td>7.06</td>
    </tr>
    <tr>
      <td>Adrenal Insufficiency</td>
      <td>3.09</td>
      <td>0.013</td>
      <td>0.001</td>
      <td>&lt;0.001</td>
      <td>0.08</td>
      <td>2.58</td>
      <td>13.14</td>
      <td>1.57</td>
      <td>110.37</td>
    </tr>
    <tr>
      <td>BMI</td>
      <td>2.30</td>
      <td>31.34</td>
      <td>31.64</td>
      <td>&lt;0.001</td>
      <td>−0.04</td>
      <td>−0.09</td>
      <td>0.91</td>
      <td>0.71</td>
      <td>1.17</td>
    </tr>
    <tr>
      <td>Transplantation</td>
      <td>1.90</td>
      <td>0.023</td>
      <td>0.002</td>
      <td>&lt;0.001</td>
      <td>0.1</td>
      <td>1.43</td>
      <td>4.19</td>
      <td>1.04</td>
      <td>16.87</td>
    </tr>
    <tr>
      <td>Dyspnea</td>
      <td>1.85</td>
      <td>0.17</td>
      <td>0.02</td>
      <td>&lt;0.001</td>
      <td>0.26</td>
      <td>2</td>
      <td>7.41</td>
      <td>4.85</td>
      <td>11.32</td>
    </tr>
    <tr>
      <td>CKD</td>
      <td>1.55</td>
      <td>0.14</td>
      <td>0.02</td>
      <td>&lt;0.001</td>
      <td>0.25</td>
      <td>0.81</td>
      <td>2.25</td>
      <td>1.35</td>
      <td>3.74</td>
    </tr>
    <tr>
      <td>Intercept</td>
      <td>−2.51</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

_SpO2: oxygen saturation; BP: Blood pressure; BMI: Body Mass Index; CKD: Chronic Kidney Disease._

The hospitalization models used symptoms, pre-existing medications, comorbidities, and patient demographics. Laboratory results and radiologic findings were not considered since these were not available for most non-hospitalized patients. Full models used all (106) variables retained after several pre-processing steps described in Materials and methods. Applying the statistical variable selection procedure described in the Appendix (specifically, eliminating variables with a p-value exceeding 0.05), yields a model with 74 variables. To provide a more parsimonious, highly interpretable, and easier to implement model, we used recursive feature elimination (see Appendix) to select a model with only 11 variables. The best model using the random validation approach has an AUC of 88% while the best parsimonious (linear) model has an AUC of 83%, being though easier to interpret and implement. Validation on the BWH patients yields an AUC of 84% for the parsimonious model.

Table 1 also reports the 11 variables in the parsimonious LR model, including their LR coefficients, and a binarized version of this model as described in Materials and methods. The most important variables associated with hospitalization were: oxygen saturation, temperature, respiratory rate, age, pulse, blood pressure, a comorbidity of adrenal insufficiency, BMI, prior transplantation, dyspnea, and kidney disease.

Additionally, we assessed the role of pre-existing ACE inhibitor (ACEI) and angiotensin receptor blocker (ARB) medications by adding these variables into the parsimonious binarized model, while controlling for additional relevant variables (hypertension, diabetes, and arrhythmia comorbidities and other hypertension medications). We found that while ARBs are not a factor, ACEIs reduce the odds of hospitalization by 3/4, on average, controlling for other important factors, such as age, hypertension, and related comorbidities associated with the use of these medications.

### ICU admission

The mean age of ICU admitted patients was 63.3 years (SD: 15.1 years) and 63% were male. The ICU and ventilation prediction models used the features considered for the hospitalization, as well as laboratory results and radiologic findings. For these models, we excluded patients who required immediate ICU admission or ventilation (defined as within 4 hr from initial presentation). This was implemented in order to focus on patients where triaging is challenging and risk prediction would be beneficial. There were 2513 and 2525 patients remaining for the ICU and the mechanical ventilation prediction models, respectively.

For the model including 2513 patients (Table 2), we first developed a model using all 130 variables retained after pre-processing, then employed statistical variable selection to retain 56 of the variables, and then applied recursive feature elimination with LR to select a parsimonious model which uses only 10 variables. The following variables were included: opacity observed in a chest scan, respiratory rate, age, fever, male gender, albumin, anion gap, oxygen saturation, LDH, and calcium. In addition, we generated a binarized version of the parsimonious model. The parsimonious model for all 2513 patients has an AUC of 86%, almost as high as the model with all 130 features.

**Table 2.**
 ICU prediction model (test performance).Abbreviations are as in Table 1. Thresholds for the binarized model, PSI and CURB-65 scores are in the Appendix.


<table>
  <tbody>
    <tr>
      <td colspan="10">ICU prediction results with 2513 patients</td>
    </tr>
    <tr>
      <td rowspan="2" colspan="2">Algorithm</td>
      <td colspan="4">AUC</td>
      <td colspan="4">F1-weighted</td>
    </tr>
    <tr>
      <td colspan="2">Random</td>
      <td colspan="2">BWH</td>
      <td colspan="2">Random</td>
      <td colspan="2">BWH</td>
    </tr>
    <tr>
      <td colspan="2"></td>
      <td colspan="8">Models using all 130 features</td>
    </tr>
    <tr>
      <td colspan="2">XGBoost</td>
      <td colspan="2">86.0% (2.8%)</td>
      <td colspan="2">83.1%</td>
      <td colspan="2">90.0% (1.7%)</td>
      <td colspan="2">91.7%</td>
    </tr>
    <tr>
      <td colspan="2">SVM-L1</td>
      <td colspan="2">85.9% (2.5%)</td>
      <td colspan="2">80.2%</td>
      <td colspan="2">89.9% (1.0%)</td>
      <td colspan="2">89.2%</td>
    </tr>
    <tr>
      <td colspan="2">LR-L1</td>
      <td colspan="2">84.6% (2.8%)</td>
      <td colspan="2">76.8%</td>
      <td colspan="2">89.7% (1.0%)</td>
      <td colspan="2">89.9%</td>
    </tr>
    <tr>
      <td colspan="2">RF</td>
      <td colspan="2">86.9% (2.4%)</td>
      <td colspan="2">83.7%</td>
      <td colspan="2">90.4% (1.1%)</td>
      <td colspan="2">91.1%</td>
    </tr>
    <tr>
      <td colspan="2"></td>
      <td colspan="8">Models using 56 statistically selected features</td>
    </tr>
    <tr>
      <td colspan="2">XGBoost</td>
      <td colspan="2">86.8% (3.1%)</td>
      <td colspan="2">82.8%</td>
      <td colspan="2">90.4% (1.4%)</td>
      <td colspan="2">91.3%</td>
    </tr>
    <tr>
      <td colspan="2">SVM-L1</td>
      <td colspan="2">86.2% (2.6%)</td>
      <td colspan="2">82.6%</td>
      <td colspan="2">90.6% (1.2%)</td>
      <td colspan="2">90.8%</td>
    </tr>
    <tr>
      <td colspan="2">LR-L1</td>
      <td colspan="2">85.8% (2.9%)</td>
      <td colspan="2">81.8%</td>
      <td colspan="2">90.2% (1.3%)</td>
      <td colspan="2">91.3%</td>
    </tr>
    <tr>
      <td colspan="2">RF</td>
      <td colspan="2">86.7% (2.0%)</td>
      <td colspan="2">83.2%</td>
      <td colspan="2">90.5% (1.7%)</td>
      <td colspan="2">91.5%</td>
    </tr>
    <tr>
      <td colspan="2"></td>
      <td colspan="8">Parsimonious Model using 10 features</td>
    </tr>
    <tr>
      <td colspan="2">LR-L1</td>
      <td colspan="2">85.8% (2.6%)</td>
      <td colspan="2">83.9%</td>
      <td colspan="2">90.0% (1.4%)</td>
      <td colspan="2">89.1%</td>
    </tr>
    <tr>
      <td colspan="2">LR-L1 (binarized model)</td>
      <td colspan="2">84.2% (2.2%)</td>
      <td colspan="2">82.5%</td>
      <td colspan="2">89.8% (1.1%)</td>
      <td colspan="2">88.1%</td>
    </tr>
    <tr>
      <td colspan="2"></td>
      <td colspan="8">Model using PSI or CURB-65 score</td>
    </tr>
    <tr>
      <td colspan="2">PSI score</td>
      <td colspan="2">72.9% (4.9%)</td>
      <td colspan="2">78.8%</td>
      <td colspan="2">86.8% (0.7%)</td>
      <td colspan="2">88.2%</td>
    </tr>
    <tr>
      <td colspan="2">CURB-65 score</td>
      <td colspan="2">67.0% (5.0%)</td>
      <td colspan="2">75.4%</td>
      <td colspan="2">87.0% (0.5%)</td>
      <td colspan="2">88.1%</td>
    </tr>
    <tr>
      <td colspan="10">Variables for the parsimonious model</td>
    </tr>
    <tr>
      <td>Variable</td>
      <td>Coef</td>
      <td>Y1 mean</td>
      <td>Y0 mean</td>
      <td>p-value</td>
      <td>Y-corr</td>
      <td>Coef binary</td>
      <td>OR</td>
      <td colspan="2">OR 97.5% CI</td>
    </tr>
    <tr>
      <td>Radiology Opacities</td>
      <td>0.54</td>
      <td>0.76</td>
      <td>0.27</td>
      <td>&lt;0.001</td>
      <td>0.30</td>
      <td>1.41</td>
      <td>4.08</td>
      <td>2.83</td>
      <td>5.89</td>
    </tr>
    <tr>
      <td>Respiratory Rate</td>
      <td>0.46</td>
      <td>24.61</td>
      <td>21.37</td>
      <td>&lt;0.001</td>
      <td>0.16</td>
      <td>0.50</td>
      <td>1.66</td>
      <td>1.14</td>
      <td>2.41</td>
    </tr>
    <tr>
      <td>Age</td>
      <td>0.45</td>
      <td>62.61</td>
      <td>50.58</td>
      <td>&lt;0.001</td>
      <td>0.18</td>
      <td>0.56</td>
      <td>1.76</td>
      <td>1.27</td>
      <td>2.43</td>
    </tr>
    <tr>
      <td>Fever</td>
      <td>0.40</td>
      <td>0.64</td>
      <td>0.33</td>
      <td>&lt;0.001</td>
      <td>0.18</td>
      <td>0.61</td>
      <td>1.83</td>
      <td>1.32</td>
      <td>2.55</td>
    </tr>
    <tr>
      <td>Male</td>
      <td>0.35</td>
      <td>0.64</td>
      <td>0.44</td>
      <td>&lt;0.001</td>
      <td>0.12</td>
      <td>0.50</td>
      <td>1.65</td>
      <td>1.21</td>
      <td>2.26</td>
    </tr>
    <tr>
      <td>Albumin</td>
      <td>−0.34</td>
      <td>3.68</td>
      <td>3.84</td>
      <td>&lt;0.001</td>
      <td>−0.16</td>
      <td>0.58</td>
      <td>1.78</td>
      <td>1.10</td>
      <td>2.90</td>
    </tr>
    <tr>
      <td>Anion Gap</td>
      <td>0.33</td>
      <td>16.40</td>
      <td>15.35</td>
      <td>&lt;0.001</td>
      <td>0.13</td>
      <td>−0.05</td>
      <td>0.95</td>
      <td>0.46</td>
      <td>1.98</td>
    </tr>
    <tr>
      <td>SpO2 (%)</td>
      <td>−0.22</td>
      <td>94.72</td>
      <td>96.72</td>
      <td>&lt;0.001</td>
      <td>−0.24</td>
      <td>0.83</td>
      <td>2.29</td>
      <td>1.63</td>
      <td>3.21</td>
    </tr>
    <tr>
      <td>LDH</td>
      <td>0.22</td>
      <td>400.40</td>
      <td>327.48</td>
      <td>&lt;0.001</td>
      <td>0.15</td>
      <td>0.96</td>
      <td>2.62</td>
      <td>1.74</td>
      <td>3.94</td>
    </tr>
    <tr>
      <td>Calcium</td>
      <td>−0.21</td>
      <td>8.84</td>
      <td>9.01</td>
      <td>&lt;0.001</td>
      <td>−0.10</td>
      <td>0.55</td>
      <td>1.73</td>
      <td>1.21</td>
      <td>2.48</td>
    </tr>
    <tr>
      <td>Intercept</td>
      <td>−0.93</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

_SpO2: oxygen saturation; LDH: Lactate dehydrogenase._

For comparison purposes against well-established scoring systems, we implemented two commonly used pneumonia severity scores, CURB-65 (Lim et al., 2003) and the Pneumonia Severity Index (PSI) (Fine et al., 1997). Predictions based on the PSI and CURB-65 scores, have AUCs of 73% and 67%, respectively.

We also developed a model for a more restrictive set of patients. Specifically, the number of missing lab values for some patients is substantial. Given the importance of LDH and CRP, as revealed by our models, the more restricted patient set contains 669 patients with non-missing LDH and CRP values. After removing patients who required intubation or ICU admission within 4 hr of hospital presentation, we included 628 patients and 635 patients for the restricted ICU admission and ventilation models, respectively.

The best restricted model for the 628 patients (Table 3) is the nonlinear XGBoost model using 29 statistically selected features with an AUC of 83%, with a linear parsimonious LR model close behind (AUC 80%). An RF model using all variables yields an AUC of 77% when tested on BWH data. PSI- and CURB-65 models have AUCs below 59%.

**Table 3.**
 Restricted ICU prediction model (test performance).Abbreviations are as in Table 1. Thresholds for the binarized model, PSI and CURB-65 scores are in the Appendix.


<table>
  <tbody>
    <tr>
      <td colspan="10">ICU prediction results with 628 patients</td>
    </tr>
    <tr>
      <td rowspan="2" colspan="2">Algorithm</td>
      <td colspan="4">AUC</td>
      <td colspan="4">F1-weighted</td>
    </tr>
    <tr>
      <td colspan="2">Random</td>
      <td colspan="2">BWH</td>
      <td colspan="2">Random</td>
      <td colspan="2">BWH</td>
    </tr>
    <tr>
      <td colspan="2"></td>
      <td colspan="8">Models using all 130 features</td>
    </tr>
    <tr>
      <td colspan="2">XGBoost</td>
      <td colspan="2">82.5% (1.9%)</td>
      <td colspan="2">67.3%</td>
      <td colspan="2">81.4% (0.7%)</td>
      <td colspan="2">72.6%</td>
    </tr>
    <tr>
      <td colspan="2">SVM-L1</td>
      <td colspan="2">77.8% (3.8%)</td>
      <td colspan="2">72.8%</td>
      <td colspan="2">79.7% (1.2%)</td>
      <td colspan="2">73.6%</td>
    </tr>
    <tr>
      <td colspan="2">LR-L1</td>
      <td colspan="2">75.9% (3.6%)</td>
      <td colspan="2">69.7%</td>
      <td colspan="2">79.2% (2.5%)</td>
      <td colspan="2">73.7%</td>
    </tr>
    <tr>
      <td colspan="2">RF</td>
      <td colspan="2">80.9% (2.7%)</td>
      <td colspan="2">76.9%</td>
      <td colspan="2">78.8% (1.9%)</td>
      <td colspan="2">73.6%</td>
    </tr>
    <tr>
      <td colspan="2"></td>
      <td colspan="8">Models using 29 statistically selected features</td>
    </tr>
    <tr>
      <td colspan="2">XGBoost</td>
      <td colspan="2">82.7% (2.7%)</td>
      <td colspan="2">76.2%</td>
      <td colspan="2">80.6% (2.1%)</td>
      <td colspan="2">72.6%</td>
    </tr>
    <tr>
      <td colspan="2">SVM-L1</td>
      <td colspan="2">77.9% (3.7%)</td>
      <td colspan="2">73.1%</td>
      <td colspan="2">78.5% (1.4%)</td>
      <td colspan="2">73.6%</td>
    </tr>
    <tr>
      <td colspan="2">LR-L1</td>
      <td colspan="2">78.4% (4.1%)</td>
      <td colspan="2">71.5%</td>
      <td colspan="2">79.5% (2.6%)</td>
      <td colspan="2">74.4%</td>
    </tr>
    <tr>
      <td colspan="2">RF</td>
      <td colspan="2">82.1% (2.8%)</td>
      <td colspan="2">74.1%</td>
      <td colspan="2">79.0% (2.4%)</td>
      <td colspan="2">75.4%</td>
    </tr>
    <tr>
      <td colspan="2"></td>
      <td colspan="8">Parsimonious Model using 8 features</td>
    </tr>
    <tr>
      <td colspan="2">LR-L1</td>
      <td colspan="2">80.1% (2.9%)</td>
      <td colspan="2">74.2%</td>
      <td colspan="2">80.9% (2.1%)</td>
      <td colspan="2">77.2%</td>
    </tr>
    <tr>
      <td colspan="2">LR-L1 (binarized model)</td>
      <td colspan="2">72.5% (5.4%)</td>
      <td colspan="2">69.9%</td>
      <td colspan="2">73.4% (2.8%)</td>
      <td colspan="2">69.7%</td>
    </tr>
    <tr>
      <td colspan="2"></td>
      <td colspan="8">Model using PSI or CURB-65 score</td>
    </tr>
    <tr>
      <td colspan="2">PSI score</td>
      <td colspan="2">58.8% (7.4%)</td>
      <td colspan="2">68.3%</td>
      <td colspan="2">66.7% (2.2%)</td>
      <td colspan="2">65.3%</td>
    </tr>
    <tr>
      <td colspan="2">CURB-65 score</td>
      <td colspan="2">56.8% (4.5%)</td>
      <td colspan="2">76.9%</td>
      <td colspan="2">66.2% (1.5%)</td>
      <td colspan="2">63.8%</td>
    </tr>
    <tr>
      <td colspan="10">Variables for the parsimonious model</td>
    </tr>
    <tr>
      <td>Variable</td>
      <td>Coef</td>
      <td>Y1 mean</td>
      <td>Y0 mean</td>
      <td>p-value</td>
      <td>Y-corr</td>
      <td>Coef binary</td>
      <td>OR</td>
      <td colspan="2">OR 97.5% CI</td>
    </tr>
    <tr>
      <td>LDH</td>
      <td>0.53</td>
      <td>519.88</td>
      <td>304.40</td>
      <td>&lt;0.001</td>
      <td>0.15</td>
      <td>1.59</td>
      <td>4.88</td>
      <td>2.65</td>
      <td>8.99</td>
    </tr>
    <tr>
      <td>CRP (mg/L)</td>
      <td>0.47</td>
      <td>127.17</td>
      <td>67.43</td>
      <td>&lt;0.001</td>
      <td>0.35</td>
      <td>0.76</td>
      <td>2.13</td>
      <td>0.70</td>
      <td>6.47</td>
    </tr>
    <tr>
      <td>Calcium</td>
      <td>−0.35</td>
      <td>8.83</td>
      <td>9.01</td>
      <td>&lt;0.001</td>
      <td>−0.13</td>
      <td>0.71</td>
      <td>2.03</td>
      <td>1.25</td>
      <td>3.31</td>
    </tr>
    <tr>
      <td>IDDM</td>
      <td>0.30</td>
      <td>0.25</td>
      <td>0.12</td>
      <td>0.003</td>
      <td>0.15</td>
      <td>1.00</td>
      <td>2.73</td>
      <td>1.62</td>
      <td>4.60</td>
    </tr>
    <tr>
      <td>SpO2 (%)</td>
      <td>−0.29</td>
      <td>94.13</td>
      <td>95.59</td>
      <td>0.003</td>
      <td>−0.22</td>
      <td>0.34</td>
      <td>1.41</td>
      <td>0.92</td>
      <td>2.16</td>
    </tr>
    <tr>
      <td>Radiology Opacities</td>
      <td>0.25</td>
      <td>0.88</td>
      <td>0.71</td>
      <td>&lt;0.001</td>
      <td>0.16</td>
      <td>0.62</td>
      <td>1.86</td>
      <td>1.05</td>
      <td>3.29</td>
    </tr>
    <tr>
      <td>Anion Gap</td>
      <td>0.20</td>
      <td>16.66</td>
      <td>15.28</td>
      <td>&lt;0.001</td>
      <td>0.20</td>
      <td>0.34</td>
      <td>1.40</td>
      <td>0.48</td>
      <td>4.12</td>
    </tr>
    <tr>
      <td>Sodium</td>
      <td>−0.16</td>
      <td>136.13</td>
      <td>137.53</td>
      <td>&lt;0.001</td>
      <td>−0.14</td>
      <td>0.47</td>
      <td>1.60</td>
      <td>1.05</td>
      <td>2.43</td>
    </tr>
    <tr>
      <td>Intercept</td>
      <td>−0.34</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

_LDH: Lactate dehydrogenase; CRP: C-reactive protein; IDDM: Insulin-dependent diabetes mellitus; SpO2: oxygen saturation._

### Mechanical ventilation

The mean age of patients requiring mechanical ventilation was 63.3 years (SD: 14.7 years) and 63.6% were male. Again, we excluded patients who were intubated within 4 hr of their hospital admission.

For the model including 2525 patients (Table 4), we used statistical feature selection to select 55 variables, and recursive feature elimination with LR to select a parsimonious model with only eight variables. The following variables were included: lung opacities, albumin, fever, respiratory rate, glucose, male gender, LDH, and anion gap. In addition, we generated a binarized version of the parsimonious model. The best model for all 2525 patients was a nonlinear RF model using the 55 statistically selected variables and yielding an AUC of 86%. The best linear model was the parsimonious LR model with an AUC of 85%. PSI- and CURB-65 models yield AUCs of 74% and 67%, respectively.

**Table 4.**
 Ventilation prediction model (test performance).Abbreviations are as in Table 1. Thresholds for the binarized model, PSI and CURB-65 scores are in the Appendix.


<table>
  <tbody>
    <tr>
      <td colspan="10">Ventilation prediction results with 2525 patients</td>
    </tr>
    <tr>
      <td rowspan="2" colspan="2">Algorithm</td>
      <td colspan="4">AUC</td>
      <td colspan="4">F1-weighted</td>
    </tr>
    <tr>
      <td colspan="2">Random</td>
      <td colspan="2">BWH</td>
      <td colspan="2">Random</td>
      <td colspan="2">BWH</td>
    </tr>
    <tr>
      <td colspan="2"></td>
      <td colspan="8">Models using all 130 features</td>
    </tr>
    <tr>
      <td colspan="2">XGBoost</td>
      <td colspan="2">85.8% (4.0%)</td>
      <td colspan="2">83.8%</td>
      <td colspan="2">91.0% (0.4%)</td>
      <td colspan="2">91.6%</td>
    </tr>
    <tr>
      <td colspan="2">SVM-L1</td>
      <td colspan="2">82.6% (4.9%)</td>
      <td colspan="2">83.8%</td>
      <td colspan="2">90.9% (0.8%)</td>
      <td colspan="2">91.6%</td>
    </tr>
    <tr>
      <td colspan="2">LR-L1</td>
      <td colspan="2">80.7% (5.4%)</td>
      <td colspan="2">81.7%</td>
      <td colspan="2">90.4% (1.2%)</td>
      <td colspan="2">91.4%</td>
    </tr>
    <tr>
      <td colspan="2">RF</td>
      <td colspan="2">85.7% (3.9%)</td>
      <td colspan="2">83.7%</td>
      <td colspan="2">91.2% (0.9%)</td>
      <td colspan="2">91.8%</td>
    </tr>
    <tr>
      <td colspan="2"></td>
      <td colspan="8">Models using 55 statistically selected features</td>
    </tr>
    <tr>
      <td colspan="2">XGBoost</td>
      <td colspan="2">85.7% (3.3%)</td>
      <td colspan="2">86.3%</td>
      <td colspan="2">91.1% (0.6%)</td>
      <td colspan="2">91.6%</td>
    </tr>
    <tr>
      <td colspan="2">SVM-L1</td>
      <td colspan="2">83.9% (3.7%)</td>
      <td colspan="2">84.8%</td>
      <td colspan="2">90.9% (1.1%)</td>
      <td colspan="2">91.7%</td>
    </tr>
    <tr>
      <td colspan="2">LR-L1</td>
      <td colspan="2">83.3% (4.0%)</td>
      <td colspan="2">83.9%</td>
      <td colspan="2">90.8% (1.3%)</td>
      <td colspan="2">91.4%</td>
    </tr>
    <tr>
      <td colspan="2">RF</td>
      <td colspan="2">86.4% (3.4%)</td>
      <td colspan="2">86.7%</td>
      <td colspan="2">91.4% (1.1%)</td>
      <td colspan="2">91.3%</td>
    </tr>
    <tr>
      <td colspan="2"></td>
      <td colspan="8">Parsimonious Model using 8 features</td>
    </tr>
    <tr>
      <td colspan="2">LR-L1</td>
      <td colspan="2">85.2% (2.3%)</td>
      <td colspan="2">87.0%</td>
      <td colspan="2">90.3% (0.3%)</td>
      <td colspan="2">90.7%</td>
    </tr>
    <tr>
      <td colspan="2">LR-L1 (binarized model)</td>
      <td colspan="2">81.3% (3.1%)</td>
      <td colspan="2">82.6%</td>
      <td colspan="2">90.0% (0.6%)</td>
      <td colspan="2">90.2%</td>
    </tr>
    <tr>
      <td colspan="2"></td>
      <td colspan="8">Model using PSI or CURB-65 score</td>
    </tr>
    <tr>
      <td colspan="2">PSI score</td>
      <td colspan="2">73.6% (4.1%)</td>
      <td colspan="2">80.7%</td>
      <td colspan="2">89.4% (0.4%)</td>
      <td colspan="2">90.3%</td>
    </tr>
    <tr>
      <td colspan="2">CURB-65 score</td>
      <td colspan="2">66.8% (3.1%)</td>
      <td colspan="2">75.9%</td>
      <td colspan="2">89.7% (0.1%)</td>
      <td colspan="2">90.0%</td>
    </tr>
    <tr>
      <td colspan="10">Variables for the Parsimonious Model</td>
    </tr>
    <tr>
      <td>Variable</td>
      <td>Coef</td>
      <td>Y1 mean</td>
      <td>Y0 mean</td>
      <td>p-value</td>
      <td>Y-corr</td>
      <td>Coef binary</td>
      <td>OR</td>
      <td colspan="2">OR 97.5% CI</td>
    </tr>
    <tr>
      <td>Radiology opacities</td>
      <td>0.86</td>
      <td>0.77</td>
      <td>0.28</td>
      <td>&lt;0.001</td>
      <td>0.27</td>
      <td>1.58</td>
      <td>4.86</td>
      <td>3.25</td>
      <td>7.25</td>
    </tr>
    <tr>
      <td>Albumin</td>
      <td>−0.45</td>
      <td>3.65</td>
      <td>3.83</td>
      <td>&lt;0.001</td>
      <td>−0.16</td>
      <td>1.07</td>
      <td>2.91</td>
      <td>1.80</td>
      <td>4.72</td>
    </tr>
    <tr>
      <td>Fever</td>
      <td>0.43</td>
      <td>0.66</td>
      <td>0.33</td>
      <td>&lt;0.001</td>
      <td>0.17</td>
      <td>0.72</td>
      <td>2.05</td>
      <td>1.42</td>
      <td>2.95</td>
    </tr>
    <tr>
      <td>Respiratory rate</td>
      <td>0.42</td>
      <td>24.70</td>
      <td>21.44</td>
      <td>&lt;0.001</td>
      <td>0.15</td>
      <td>0.50</td>
      <td>1.64</td>
      <td>1.09</td>
      <td>2.47</td>
    </tr>
    <tr>
      <td>Glucose</td>
      <td>0.38</td>
      <td>170.17</td>
      <td>138.32</td>
      <td>&lt;0.001</td>
      <td>0.15</td>
      <td>0.97</td>
      <td>2.63</td>
      <td>1.71</td>
      <td>4.06</td>
    </tr>
    <tr>
      <td>Male</td>
      <td>0.34</td>
      <td>0.64</td>
      <td>0.44</td>
      <td>&lt;0.001</td>
      <td>0.10</td>
      <td>0.43</td>
      <td>1.54</td>
      <td>1.09</td>
      <td>2.18</td>
    </tr>
    <tr>
      <td>LDH</td>
      <td>0.33</td>
      <td>408.56</td>
      <td>328.78</td>
      <td>&lt;0.001</td>
      <td>0.14</td>
      <td>0.91</td>
      <td>2.48</td>
      <td>1.58</td>
      <td>3.89</td>
    </tr>
    <tr>
      <td>Anion gap</td>
      <td>0.31</td>
      <td>16.50</td>
      <td>15.37</td>
      <td>&lt;0.001</td>
      <td>0.13</td>
      <td>0.27</td>
      <td>1.31</td>
      <td>0.53</td>
      <td>3.25</td>
    </tr>
    <tr>
      <td>Intercept</td>
      <td>−1.06</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

_LDH: Lactate dehydrogenase._

The best model for the restricted case of 635 patients (Table 5) was the linear parsimonious LR model (with just five variables) achieving an AUC of 82%. PSI- and CURB-65 models do not exceed AUC of 58%.

**Table 5.**
 Restricted ventilation prediction model (test performance).Abbreviations are as in Table 1.Thresholds for the binarized, PSI and CURB-65 scores are in the Appendix.


<table>
  <thead>
    <tr>
      <th colspan="10">Ventilation prediction results with 635 patients</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2" colspan="2">Algorithm</td>
      <td colspan="4">AUC</td>
      <td colspan="4">F1-weighted</td>
    </tr>
    <tr>
      <td colspan="2">Random</td>
      <td colspan="2">BWH</td>
      <td colspan="2">Random</td>
      <td colspan="2">BWH</td>
    </tr>
    <tr>
      <td colspan="2"></td>
      <td colspan="8">Models using all 130 features</td>
    </tr>
    <tr>
      <td colspan="2">XGBoost</td>
      <td colspan="2">80.6% (1.9%)</td>
      <td colspan="2">74.7%</td>
      <td colspan="2">79.4% (2.6%)</td>
      <td colspan="2">75.7%</td>
    </tr>
    <tr>
      <td colspan="2">SVM-L1</td>
      <td colspan="2">79.4% (5.2%)</td>
      <td colspan="2">71.3%</td>
      <td colspan="2">80.8% (2.0%)</td>
      <td colspan="2">75.7%</td>
    </tr>
    <tr>
      <td colspan="2">LR-L1</td>
      <td colspan="2">76.9% (3.9%)</td>
      <td colspan="2">68.2%</td>
      <td colspan="2">78.6% (3.2%)</td>
      <td colspan="2">73.4%</td>
    </tr>
    <tr>
      <td colspan="2">RF</td>
      <td colspan="2">81.0% (3.1%)</td>
      <td colspan="2">75.8%</td>
      <td colspan="2">79.8% (4.2%)</td>
      <td colspan="2">72.7%</td>
    </tr>
    <tr>
      <td colspan="2"></td>
      <td colspan="8">Models using 29 statistically selected features</td>
    </tr>
    <tr>
      <td colspan="2">XGBoost</td>
      <td colspan="2">81.6% (3.2%)</td>
      <td colspan="2">76.9%</td>
      <td colspan="2">79.0% (2.9%)</td>
      <td colspan="2">71.7%</td>
    </tr>
    <tr>
      <td colspan="2">SVM-L1</td>
      <td colspan="2">79.1% (4.6%)</td>
      <td colspan="2">69.4%</td>
      <td colspan="2">80.6% (2.5%)</td>
      <td colspan="2">75.7%</td>
    </tr>
    <tr>
      <td colspan="2">LR-L1</td>
      <td colspan="2">80.9% (3.6%)</td>
      <td colspan="2">70.9%</td>
      <td colspan="2">80.4% (2.2%)</td>
      <td colspan="2">75.7%</td>
    </tr>
    <tr>
      <td colspan="2">RF</td>
      <td colspan="2">81.3% (2.6%)</td>
      <td colspan="2">75.4%</td>
      <td colspan="2">79.2% (1.7%)</td>
      <td colspan="2">69.6%</td>
    </tr>
    <tr>
      <td colspan="2"></td>
      <td colspan="8">Parsimonious Model using 5 features</td>
    </tr>
    <tr>
      <td colspan="2">LR-L1</td>
      <td colspan="2">82.4% (3.7%)</td>
      <td colspan="2">75.2%</td>
      <td colspan="2">81.8% (1.7%)</td>
      <td colspan="2">71.7%</td>
    </tr>
    <tr>
      <td colspan="2">LR-L1 (binarized model)</td>
      <td colspan="2">71.4% (6.2%)</td>
      <td colspan="2">65.5%</td>
      <td colspan="2">76.6% (3.5%)</td>
      <td colspan="2">68.3%</td>
    </tr>
    <tr>
      <td colspan="2"></td>
      <td colspan="8">Model using PSI or CURB-65 score</td>
    </tr>
    <tr>
      <td colspan="2">PSI score</td>
      <td colspan="2">57.6% (4.5%)</td>
      <td colspan="2">67.4%</td>
      <td colspan="2">73.2% (1.3%)</td>
      <td colspan="2">71.2%</td>
    </tr>
    <tr>
      <td colspan="2">CURB-65 score</td>
      <td colspan="2">56.9% (7.1%)</td>
      <td colspan="2">74.0%</td>
      <td colspan="2">72.4% (0.2%)</td>
      <td colspan="2">68.3%</td>
    </tr>
    <tr>
      <td colspan="10">Variables for the parsimonious model</td>
    </tr>
    <tr>
      <td>Variable</td>
      <td>Coef</td>
      <td>Y1 mean</td>
      <td>Y0 mean</td>
      <td>p-value</td>
      <td>Y-corr</td>
      <td>Coef binary</td>
      <td>OR</td>
      <td colspan="2">OR 97.5% CI</td>
    </tr>
    <tr>
      <td>CRP (mg/L)</td>
      <td>0.60</td>
      <td>134.52</td>
      <td>69.62</td>
      <td>&lt;0.001</td>
      <td>0.35</td>
      <td>0.42</td>
      <td>1.53</td>
      <td>0.51</td>
      <td>4.59</td>
    </tr>
    <tr>
      <td>LDH</td>
      <td>0.55</td>
      <td>550.41</td>
      <td>311.01</td>
      <td>&lt;0.001</td>
      <td>0.16</td>
      <td>1.87</td>
      <td>6.47</td>
      <td>3.19</td>
      <td>13.10</td>
    </tr>
    <tr>
      <td>Calcium</td>
      <td>−0.39</td>
      <td>8.82</td>
      <td>9.00</td>
      <td>&lt;0.001</td>
      <td>−0.13</td>
      <td>0.58</td>
      <td>1.79</td>
      <td>1.07</td>
      <td>2.98</td>
    </tr>
    <tr>
      <td>IDDM</td>
      <td>0.36</td>
      <td>0.26</td>
      <td>0.12</td>
      <td>0.002</td>
      <td>0.15</td>
      <td>1.18</td>
      <td>3.26</td>
      <td>1.90</td>
      <td>5.58</td>
    </tr>
    <tr>
      <td>Anion Gap</td>
      <td>0.29</td>
      <td>16.81</td>
      <td>15.32</td>
      <td>&lt;0.001</td>
      <td>0.19</td>
      <td>18.66</td>
      <td>1.27E+08</td>
      <td>0.00</td>
      <td>inf</td>
    </tr>
    <tr>
      <td>Intercept</td>
      <td>−0.39</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

_CRP: C-reactive protein; LDH: Lactate dehydrogenase; IDDM: Insulin-dependent diabetes mellitus._

### Time period between ICU/ventilation model prediction and corresponding outcomes

Table 6 reports the mean and the median time interval (in hours) between hospital admission time and ICU/ventilation outcomes. Specifically, we report statistics for ICU admission or intubation outcomes from the correct ICU/intubation predictions made by our models trained on four hospitals (MGH, NWH, NSM, FH) and applied to BWH patients (both the models making predictions for all patients and the restricted models). As we have noted earlier, our models use the lab results closest to admission (either on admission date or the following day). We also report the time interval between the last lab result used by the model and the corresponding ICU/intubation outcome.

**Table 6.**
 Mean and median hours between reference date/lab results to outcomes in full/restricted ICU and ventilation model prediction.


<table>
  <thead>
    <tr>
      <th></th>
      <th>From reference date (mean)</th>
      <th>From reference date (median)</th>
      <th>From lab results (mean)</th>
      <th>From lab results (median)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Restricted ICU</td>
      <td>38.13</td>
      <td>28.08</td>
      <td>22.55</td>
      <td>9.90</td>
    </tr>
    <tr>
      <td>Restricted intubation</td>
      <td>35.36</td>
      <td>26.40</td>
      <td>22.37</td>
      <td>10.39</td>
    </tr>
    <tr>
      <td>Full ICU</td>
      <td>22.86</td>
      <td>17.28</td>
      <td>15.86</td>
      <td>12.99</td>
    </tr>
    <tr>
      <td>Full intubation</td>
      <td>25.62</td>
      <td>22.20</td>
      <td>10.23</td>
      <td>8.97</td>
    </tr>
  </tbody>
</table>

## Discussion

We developed three models to predict need for hospitalization, ICU admission, and mechanical ventilation in patients with COVID-19. The prediction models are not meant to replace clinicians’ judgment for determining level of care. Instead, they are designed to assist clinicians in identifying patients at risk of future decompensation. Patient vital signs were the most important predictors of hospitalization. This is expected as vital signs reflect underlying disease severity, the need for cardiorespiratory resuscitation, and the risk of future decompensation without adequate medical support. Older age and BMI were also important predictors for hospitalization. Age has been recognized as an important factor associated with severe COVID-19 in previous series (Grasselli et al., 2020; Guan et al., 2020; Richardson et al., 2020). However, it is not known whether age itself or the presence of comorbidities place patients at risk for severe disease. Our results demonstrate that age is a stronger predictor of severe COVID-19 than a host of underlying comorbidities.

In terms of patient comorbidities, adrenal insufficiency, prior transplantation, and chronic kidney disease were strongly associated with need for hospitalization. Diabetes mellitus was associated with a need for ICU admission and mechanical ventilation, which might be due to its detrimental effects on immune function.

For the ICU and ventilation prediction models screening all at-risk (COVID-19-positive patients), opacities observed in a chest scan, age, and male gender emerge as important variables. Males have been found to have worse in-hospital outcomes in other studies as well (Palaiodimos et al., 2020).

We also identified several routine laboratory values that are predictive of ICU admission and mechanical ventilation. Elevated serum LDH, CRP, anion gap, and glucose, as well as decreased serum calcium, sodium, and albumin were strong predictors of ICU admission and mechanical ventilation. LDH is an indicator of tissue damage and has been found to be a marker of severity in P. jirovecii pneumonia (Zaman and White, 1988). Along with CRP, it was among the two most important predictors of ICU admission and ventilation in the parsimonious model among patients who had LDH and CRP measurements on admission. This finding is consistent with previous reports identifying LDH as an important prognostic factor (Gong et al., 2020; Ji et al., 2020; Mo et al., 2020; Yan et al., 2020). In addition, lower serum calcium is associated with cell lysis and tissue destruction, as it is often seen as part of the tumor lysis syndrome. Elevated serum anion gap is a marker of metabolic acidosis and ischemia, suggesting that tissue hypoxia and hypoperfusion may be components of severe disease.

For all three prognostic models, we developed predicting hospitalizations, ICU care, and mechanical ventilation, AUC ranges within 86–88%, which indicates strong predictive power. Interestingly, we can achieve AUC within 85–86% for ICU and ventilation prediction with a parsimonious linear model utilizing no more than 10 variables. In all cases, we can also develop a parsimonious model with binarized variables using medically suggested normal and abnormal variable thresholds. These binarized models have similar performance with their continuous counterparts. The ICU and ventilation models using all patients are very accurate, but, arguably, make a number of ‘easier’ decisions since more than 60% of the patients are never hospitalized. Many of these patients are younger, healthy, and likely present with mild-to-moderate symptoms. To test the robustness of the models to patients with potentially more ‘complex’ disease, we developed ICU and ventilation models on a restricted set of patients. This is the subset of patients who are hospitalized and most of the crucial labs are available for them (specifically CRP and LDH which emerged as important from our models). The best AUC for these models drops, but not below 82%, which indicates robustness of the model even when dealing with arguably harder to assess cases. LDH, CRP, calcium, lung opacity, anion gap, SpO2, sodium, and a comorbidity of insulin-controlled diabetes appear as the most significant for these patients. Interestingly, the corresponding binarized models have about 10% lower AUC; apparently, for the more severely ill, clinical variables deviate substantially from normal and knowing the exact values is crucial.

The models have been validated with two different approaches, using random splits of the data into training and testing, as well as training in some hospitals and testing at a different hospital. Performance metrics are relatively consistent with these two approaches. We also compared the models against standard pneumonia severity scores, PSI and CURB-65, establishing that our models are significantly stronger, which highlights the different clinical profile of COVID-19.

We also examined how much in advance of the ICU or ventilation outcomes our models are able to make a prediction. Of course, this is not entirely in our control; it depends on what state the patients get admitted and how soon their condition deteriorates to require ICU admission and/or ventilation. Table 6 reports the corresponding statistics. For example, the restricted ICU and ventilation models are making a correct prediction upon admission (using the lab results closest to that time) for outcomes that on average occur 38 and 35 hr later, respectively.

To further test the accuracy of the restricted ICU and ventilation models well in advance of the corresponding event, we considered an extended BWH test set (adding 11 more patients) and computed the accuracy of the models when the test set was restricted to patients whose outcome (ICU admission or ventilation) was more than x hours after the admission lab results based on which the prediction was made, with x being 6 hr, or 12 hr, or 18 hr, or 24 hr, or even 48 hr. The ICU model reaches an AUC of 87% and a weighted F1-score of 86% at x = 18 hr. The ventilation model reaches an AUC of 64% and an F1-score of 72% at x = 48 hr. These results demonstrate that the predictive models can indeed make predictions well into the future, when physicians would be less certain about the course of the disease and when there is potentially enough time to intervene and improve outcomes.

A manual review of the predictions by the models indicates that they performed well at predicting future ICU admissions for patients who presented with mild disease several days before ICU admission was necessary. Such patients were hemodynamically stable and had minimal oxygen requirements on the floor, before clinical deterioration necessitated ICU admission. We identified several such patients. A typical case is that of a 51-year-old male with a history of hypertension, obesity, and insulin-dependent type 2 diabetes mellitus, who presented with a 3-day history of dyspnea, cough and myalgias. In the emergency department, he was hemodynamically stable, saturating at 96–97% on 2 L of nasal cannula. The patient was admitted to the floor and did well for 3 days, saturating at 93–96% on room air. On the fourth day of hospitalization, he had increasing oxygen requirements and the decision was made to transfer him to the ICU. He was intubated and ventilated for 30 days. Our prediction models accurately predicted at the time of his presentation that he would eventually require ICU admission and mechanical ventilation. This prediction was based on such variables as an elevated LDH (241 U/L) and the presence of insulin-dependent diabetes mellitus. Another such case is that of a 59-year-old male without a significant prior medical history who presented with 2 days of dyspnea, nausea, and diarrhea. At the emergency department, he was tachycardic at 110 beats per minute and saturating at 96% on room air, and the patient was admitted. For 2 days, the patient was hemodynamically stable, saturating at 94–97% on room air. On the third day of hospitalization, he had increasing oxygen requirements, eventually requiring transfer to the ICU. He was intubated and ventilated for the next 14 days. Our prediction model predicted the patient’s decompensation at his presentation, due to elevations in LDH (348 U/L) and CRP (102.3 mg/L).

We also considered the role of ACEIs and ARBs and their potential association with the outcomes. It has been speculated that ACEIs may worsen COVID-19 outcomes because they upregulate the expression of ACE2, which the virus targets for cell entry. No such evidence has been reported in earlier studies (Kuster et al., 2020; Patel and Verma, 2020). In fact, a smaller study (Zhang et al., 2020) (n = 1128 vs. 2566 in our case) reported a beneficial effect and (Rossi et al., 2020) warn of potential harmful effects of discontinuing ACEIs or ARBs due to COVID-19. Our hospitalization model suggests that ACEIs do not increase hospitalization risk and may slightly reduce it (OR 95% CI is (0.52,1.04) with a mean of 0.73). In the ICU and ventilation models, the role of these two medications is statistically weaker to observe any meaningful association.

The models we derived can be used for a variety of purposes: (i) guiding patient triage to appropriate inpatient units, (ii) guiding staffing and resource planning logistics, and (iii) understanding patient risk profiles to inform future policy decisions, such as targeted risk-based stay-at-home restrictions, testing, and vaccination prioritization guidelines once a vaccine becomes available.

Calculators implementing the parsimonious models corresponding to each of the Tables 1, 2, 3, 4, 5 have been made available online (Hao et al., 2020).

## Materials and methods

### Data extraction

Natural Language Processing (NLP) was used to extract patient comorbidities (see Appendix for details), pre-existing medications, admission vital signs, hospitalization course, ICU admission, and mechanical intubation.

### Pre-processing

The categorical features were converted to numerical by ‘one-hot’ encoding. Each categorical feature, such as gender and race, was encoded as an indicator variable for each category. Features were standardized by subtracting the mean and dividing by the standard deviation.

Several pre-processing steps, including variable imputation, outlier elimination, and removal of highly correlated variables were undertaken (see Appendix). After completing these procedures, 106 variables for each patient remained to be used by the hospitalization model. For the ICU and ventilation prediction models, we added laboratory results and radiologic findings. We removed variables with more than 90% missing values out of the roughly 2500 patients retained for these models; the remaining missing values were imputed as described above. These pre-processing steps retained 130 variables for the ICU and ventilation models.

### Classification methods

We employed nonlinear ensemble methods including Random forests (RF) (Breiman, 2001) and XGBoost (Chen and Guestrin, 2016). We also employed ‘custom’ linear methods which yield interpretable models; specifically, support vector machines (SVM) (Cortes and Vapnik, 1995) and Logistic Regression (LR). In both cases, the variants we computed were robust to noise and the presence of outliers (Chen and Paschalidis, 2018), using proper regularization. LR, in addition to a prediction, provides the likelihood associated with the predicted outcome, which can be used as a confidence measure in decision making. Further details on these methods are in the Appendix.

For each outcome, we used the statistical feature selection and recursive feature elimination procedures described in the Appendix to develop an LR parsimonious model. The LR coefficients are comparable since the variables are standardized. Hence, a larger absolute coefficient indicates that the corresponding variable is a more significant predictor. Positive (negative) coefficients imply positive (negative) correlation with the outcome. We also developed a version of this model by converting all continuous variables into binary variables, using medically motivated thresholds (see Appendix). We report the coefficients of the ‘binarized’ model and the implied odds ratio (OR), representing how the odds of the outcome are scaled by having a specific variable being abnormal vs. normal, while controlling for all other variables in the model.

### Outcomes and performance metrics

Model performance metrics included the Area Under the Curve (AUC) of the Receiver Operating Characteristic (ROC) and the Weighted-F1 score. The ROC plots the true positive rate (a.k.a. recall or sensitivity) against the false positive rate (equal to one minus the specificity). We optimized algorithm parameters to maximize AUC.

The F1 score is the harmonic mean of precision and recall. Precision (or positive predictive value) is defined as the ratio of true positives over true and false positives. The Weighted-F1 score is computed by weighting the F1-score of each class by the number of patients in that class.

### Model validation

The data were split into a training (80%) and a test set (20%). Algorithm parameters were optimized on the training (derivation) set using fivefold cross-validation. Performance metrics were computed on the test set. This process was repeated five times, each time with a random split into training/testing sets. In columns labeled as Random in Tables 1, 2, 3, 4, 5, we report the average (and standard deviation) of the test performance metrics over the five random splits. We also performed a different type of validation. We trained the models on MGH, FH, NWH, and NSM patients, and evaluated performance on BWH patients. These results are reported under the columns BWH in the tables.
