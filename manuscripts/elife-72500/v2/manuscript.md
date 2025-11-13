# Investigating phenotypes of pulmonary COVID-19 recovery: A longitudinal observational prospective multicenter trial

## Authors

- Thomas Sonnweber<sup>1</sup> ([ORCID: 0000-0002-5080-386X](https://orcid.org/0000-0002-5080-386X))
- Piotr Tymoszuk<sup>1</sup> ([ORCID: 0000-0002-0398-6034](https://orcid.org/0000-0002-0398-6034))
- Sabina Sahanic<sup>1</sup>
- Anna Boehm<sup>1</sup>
- Alex Pizzini<sup>1</sup>
- Anna Luger<sup>2</sup> ([ORCID: 0000-0002-0445-8372](https://orcid.org/0000-0002-0445-8372))
- Christoph Schwabl<sup>2</sup>
- Manfred Nairz<sup>1</sup>
- Philipp Grubwieser<sup>1</sup>
- Katharina Kurz<sup>1</sup>
- Sabine Koppelstätter<sup>1</sup>
- Magdalena Aichner<sup>1</sup>
- Bernhard Puchner<sup>3</sup>
- Alexander Egger<sup>4</sup>
- Gregor Hoermann<sup>4</sup>
- Ewald Wöll<sup>6</sup>
- Günter Weiss<sup>1</sup>
- Gerlig Widmann<sup>2</sup>
- Ivan Tancevski<sup>1</sup> ([ORCID: 0000-0001-5116-8960](https://orcid.org/0000-0001-5116-8960)) †
- Judith Löffler-Ragg<sup>1</sup> ([ORCID: 0000-0003-0873-7501](https://orcid.org/0000-0003-0873-7501)) †

### Affiliations

1. Department of Internal Medicine II, Medical University of Innsbruck Innsbruck Austria ([ROR:03pt86f80](https://ror.org/03pt86f80))
2. Department of Radiology, Medical University of Innsbruck Innsbruck Austria ([ROR:03pt86f80](https://ror.org/03pt86f80))
3. The Karl Landsteiner Institute Muenster Austria
4. Central Institute of Medical and Chemical Laboratory Diagnostics, University Hospital Innsbruck Innsbruck Austria ([ROR:03pt86f80](https://ror.org/03pt86f80))
5. Munich Leukemia Laboratory Munich Germany ([ROR:00smdp487](https://ror.org/00smdp487))
6. Department of Internal Medicine, St. Vinzenz Hospital Zams Austria

† Corresponding author

## Abstract

Background:The optimal procedures to prevent, identify, monitor, and treat long-term pulmonary sequelae of COVID-19 are elusive. Here, we characterized the kinetics of respiratory and symptom recovery following COVID-19.Methods:We conducted a longitudinal, multicenter observational study in ambulatory and hospitalized COVID-19 patients recruited in early 2020 (n = 145). Pulmonary computed tomography (CT) and lung function (LF) readouts, symptom prevalence, and clinical and laboratory parameters were collected during acute COVID-19 and at 60, 100, and 180 days follow-up visits. Recovery kinetics and risk factors were investigated by logistic regression. Classification of clinical features and participants was accomplished by unsupervised and semi-supervised multiparameter clustering and machine learning.Results:At the 6-month follow-up, 49% of participants reported persistent symptoms. The frequency of structural lung CT abnormalities ranged from 18% in the mild outpatient cases to 76% in the intensive care unit (ICU) convalescents. Prevalence of impaired LF ranged from 14% in the mild outpatient cases to 50% in the ICU survivors. Incomplete radiological lung recovery was associated with increased anti-S1/S2 antibody titer, IL-6, and CRP levels at the early follow-up. We demonstrated that the risk of perturbed pulmonary recovery could be robustly estimated at early follow-up by clustering and machine learning classifiers employing solely non-CT and non-LF parameters.Conclusions:The severity of acute COVID-19 and protracted systemic inflammation is strongly linked to persistent structural and functional lung abnormality. Automated screening of multiparameter health record data may assist in the prediction of incomplete pulmonary recovery and optimize COVID-19 follow-up management.Funding:The State of Tyrol (GZ 71934), Boehringer Ingelheim/Investigator initiated study (IIS 1199-0424).Clinical trial number:ClinicalTrials.gov: NCT04416100

## Introduction

The ongoing COVID-19 pandemic challenges health-care systems. As of December 2021, the John Hopkins dashboard (Dong et al., 2020)⁠ reports 276 million cases and 5.4 million COVID-19-related deaths worldwide (Johns Hopkins Coronavirus Resource Center, 2021)⁠. Although the vast majority of COVID-19 patients display mild disease, approximately 10–15% of cases progress to a severe condition and approximately 5% suffer from critical illness (Perez-Saez, 2021; Huang et al., 2020). Similar to severe acute respiratory syndrome (SARS) (Hui et al., 2005; Ng et al., 2004; Ngai et al., 2010; Lam et al., 2009)⁠, a significant portion of COVID-19 patients report lingering or recurring clinical impairment and cardiopulmonary recovery may take several months to years (Sonnweber et al., 2021; Sahanic et al., 2021; Caruso et al., 2021; Huang et al., 2021b; Huang et al., 2021a; Faverio et al., 2021; Hellemons et al., 2021; Zhou et al., 2021; Venkatesan, 2021)⁠. This observation has led to the introduction of the term ‘long COVID,’ defined by the persistence of COVID-19 symptoms for more than 4 weeks, and the ‘post-acute sequelae of COVID-19’ (PASC) referring to symptom persistence for more than 12 weeks (Sahanic et al., 2021; Shah et al., 2021; Sudre et al., 2021b)⁠. Evidence-based strategies for prediction, monitoring, and treatment of PASC are urgently needed (Raghu and Wilson, 2020)⁠.

We herein prospectively analyzed the prevalence of nonresolving structural and functional lung abnormalities and persistent COVID-19-related symptoms 6 months after diagnosis. Using univariate risk modeling as well as multiparameter clustering and machine learning (ML), we investigated sets of risk factors and tested the operability of ML classifiers at predicting protracted lung and symptom recovery. The classification and prediction procedures were implemented in an open-source risk assessment tool (https://im2-ibk.shinyapps.io/CovILD/).

## Methods

### Study design

The CovILD (‘Development of interstitial lung disease in COVID-19’) multicenter, longitudinal observational study (Sonnweber et al., 2021) was initiated in April 2020. Adult residents of Tyrol, Austria, with symptomatic, PCR-confirmed SARS-CoV-2 infection (WHO, 2021)⁠ were enrolled by the Department of Internal Medicine II at the Medical University of Innsbruck (primary follow-up center), St. Vinzenz Hospital in Zams, and the acute rehabilitation facility in Münster (Table 1). The participants were diagnosed with COVID-19 between 3 March and 29 June 2020. In course of the study, including the 2020 SARS-CoV-2 outbreak and follow-up visits, the regional health system was able to guarantee an unrestricted, optimal standard of diagnostics and care for all participants. Corticosteroids were not standard of care during the recruitment period of the study, thus were not administered as a therapy of acute COVID-19. Some participants with nonresolving pneumonia received systemic steroids beginning from week 4 post diagnosis at the discretion of the physician (Table 2). The analysis endpoints were the presence of any, mild (severity score ≤ 5), and moderate-to-severe (severity score > 5) lung computed tomography (CT) abnormalities, impaired lung function (LF), and persistent COVID-19 symptoms at the 180-day follow-up visit (Table 3).

**Table 1.**
 Characteristics of the study population.


<table>
  <thead>
    <tr>
      <th colspan="2">Characteristics (% cohort)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Total participants – no.</td>
      <td>145</td>
    </tr>
    <tr>
      <td>Mean age, years</td>
      <td>57.3 (SD = 14.3)</td>
    </tr>
    <tr>
      <td>Female sex</td>
      <td>42.4% (n = 63)</td>
    </tr>
    <tr>
      <td>Obesity (body mass index &gt;30 kg/m2)</td>
      <td>19.3% (n = 28)</td>
    </tr>
    <tr>
      <td>Ex-smoker</td>
      <td>39.3% (n = 57)</td>
    </tr>
    <tr>
      <td>Active smoker</td>
      <td>2.8% (n = 4)</td>
    </tr>
    <tr>
      <td colspan="2">Acute COVID-19 severity (% cohort)</td>
    </tr>
    <tr>
      <td>Mild: outpatient</td>
      <td>24.8% (n = 36)</td>
    </tr>
    <tr>
      <td>Moderate: inpatient without oxygen therapy</td>
      <td>25.5% (n = 37)</td>
    </tr>
    <tr>
      <td>Severe: inpatient with oxygen therapy</td>
      <td>27.6% (n = 40)</td>
    </tr>
    <tr>
      <td>Critical: intensive care unit</td>
      <td>22.1% (n = 32)</td>
    </tr>
    <tr>
      <td colspan="2">Comorbidities (% cohort)</td>
    </tr>
    <tr>
      <td>None</td>
      <td>22.8% (n = 33)</td>
    </tr>
    <tr>
      <td>Cardiovascular disease</td>
      <td>40% (n = 58)</td>
    </tr>
    <tr>
      <td>Pulmonary disease</td>
      <td>18.6% (n = 27)</td>
    </tr>
    <tr>
      <td>Metabolic disease</td>
      <td>43.4% (n = 63)</td>
    </tr>
    <tr>
      <td>Chronic kidney disease</td>
      <td>6.9% (n = 10)</td>
    </tr>
    <tr>
      <td>Gastrointestinal tract diseases</td>
      <td>13.8% (n = 20)</td>
    </tr>
    <tr>
      <td>Malignancy</td>
      <td>11.7% (n = 17)</td>
    </tr>
  </tbody>
</table>

**Table 2.**
 Hospitalization and medication during acute COVID-19.


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Outpatient (n = 36)</th>
      <th>Hospitalized (n = 37)</th>
      <th>Hospitalized oxygen therapy (n = 40)</th>
      <th>Hospitalized intensive care unit (n = 32)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Mean hospitalization time, days</td>
      <td>0 (SD = 0)</td>
      <td>6.9 (SD = 3.6)</td>
      <td>11.8 (SD = 6.3)</td>
      <td>34.8 (SD = 15.7)</td>
    </tr>
    <tr>
      <td>Hospitalized &gt;7 days</td>
      <td>0% (n = 0)</td>
      <td>43.2% (n = 16)</td>
      <td>80% (n = 32)</td>
      <td>100% (n = 32)</td>
    </tr>
    <tr>
      <td>Anti-infectives</td>
      <td>11.1% (n = 4)</td>
      <td>45.9% (n = 17)</td>
      <td>72.5% (n = 29)</td>
      <td>87.5% (n = 28)</td>
    </tr>
    <tr>
      <td>Antiplatelet drugs</td>
      <td>2.8% (n = 1)</td>
      <td>10.8% (n = 4)</td>
      <td>22.5% (n = 9)</td>
      <td>25% (n = 8)</td>
    </tr>
    <tr>
      <td>Anticoagulatives</td>
      <td>2.8% (n = 1)</td>
      <td>2.7% (n = 1)</td>
      <td>5% (n = 2)</td>
      <td>15.6% (n = 5)</td>
    </tr>
    <tr>
      <td>Corticosteroids*†</td>
      <td>2.8% (n = 1)</td>
      <td>5.4% (n = 2)</td>
      <td>22.5% (n = 9)</td>
      <td>40.6% (n = 13)</td>
    </tr>
    <tr>
      <td>Immunosuppression‡†</td>
      <td>0% (n = 0)</td>
      <td>2.7% (n = 1)</td>
      <td>5% (n = 2)</td>
      <td>9.4% (n = 3)</td>
    </tr>
  </tbody>
</table>

_*From the week 4 post diagnosis on, at the discretion of the physician.†Subsumed under ‘immunosuppression, acute COVID-19’ for data analysis.‡Immunosuppressive medication prior to COVID-19._

**Table 3.**
 Radiological, functional, and clinical study outcomes.


<table>
  <thead>
    <tr>
      <th>Outcome</th>
      <th>60-day follow-up</th>
      <th>100-day follow-up</th>
      <th>180-day follow-up</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Any lung CT abnormalities (complete: n = 103)</td>
      <td>74.8% (n = 77)</td>
      <td>60.2% (n = 62)</td>
      <td>48.5% (n = 50)</td>
    </tr>
    <tr>
      <td>Mild lung CT abnormalities (severity score ≤ 5) (complete: n = 103)</td>
      <td>26.2% (n = 27)</td>
      <td>36.9% (n = 38)</td>
      <td>29.1% (n = 30)</td>
    </tr>
    <tr>
      <td>Moderate-to-severe CT abnormalities (severity score &gt; 5) (complete: n = 103)</td>
      <td>48.5% (n = 50)</td>
      <td>23.3% (n = 24)</td>
      <td>19.4% (n = 20)</td>
    </tr>
    <tr>
      <td>Functional lung impairment (complete: n = 116)</td>
      <td>39.7% (n = 46)</td>
      <td>37.1% (n = 43)</td>
      <td>33.6% (n = 39)</td>
    </tr>
    <tr>
      <td>Persistent symptoms (complete: n = 145)</td>
      <td>79.3% (n = 115)</td>
      <td>67.6% (n = 98)</td>
      <td>49% (n = 71)</td>
    </tr>
  </tbody>
</table>

_CT = computed tomography._

In total, 190 COVID-19 patients were screened for participation. Thereof, n = 18 subjects refused to give informed consent, n = 27 declared difficulties to appear at the study follow-ups. Data of n = 145 participants were eligible for analysis (Figure 1). All participants gave written informed consent. The study was approved by the Institutional Review Board at the Medical University of Innsbruck (approval number: 1103/2020) and registered at ClinicalTrials.gov (NCT04416100).

### Procedures

We retrospectively assessed patient characteristics during acute COVID-19 and performed follow-up investigations at 60 days (63 ± 23 days [mean ± SD]; visit 1), 100 days (103 ± 21 days; visit 2), and 180 days (190 ± 15 days; visit 3) after diagnosis of COVID-19. Each visit included symptom and physical performance assessment with a standardized questionnaire, LF testing, standard laboratory testing, and a CT scan of the chest. The variables available for analysis with their stratification schemes are listed in Appendix 1—table 1.

Serological markers were determined in certified laboratories (Central Institute of Clinical and Chemical Laboratory Diagnostics, Rheumatology and Infectious Diseases Laboratory, both at the University Hospital of Innsbruck). C-reactive protein (CRP), interleukin-6 (IL-6), N-terminal pro natriuretic peptide (NT-proBNP), and serum ferritin were measured using a Roche Cobas 8000 analyzer. D-dimer was determined with a Siemens BCS-XP instrument using the Siemens D-Dimer Innovance reagent. Anti-S1/S2 protein SARS-CoV-2 immunoglobulin gamma (IgG) were quantified with LIAISON chemoluminescence assay (DiaSorin, Italy), expressed as binding antibody units (BAU, conversion factor = 5.7) and stratified by quartiles (Ferrari et al., 2021)⁠.

Low-dose (100 kVp tube potential) craniocaudal CT scans of the chest were acquired without iodine contrast and without ECG gating on a 128-slice multidetector CT (128 × 0.6 mm collimation, 1.1 spiral pitch factor, SOMATOM Definition Flash, Siemens Healthineers, Erlangen, Germany). In case of clinically suspected pulmonary embolism, CT scans were performed with a contrast agent. Axial reconstructions were done with 1 mm slices. CT scans were evaluated for ground-glass opacities, consolidations, bronchial dilation, and reticulations as defined by the Fleischner Society. Lung findings were graded with a semi-quantitative CT severity score (0–25 points) (Sonnweber et al., 2021)⁠.

Impaired LF was defined as (1) forced vital capacity (FVC) < 80% or (2) forced expiratory volume in 1 s (FEV1) < 80%, or (3) FEV1:FVC < 70% or (4) total lung capacity (TLC) < 80% or (5) diffusing capacity of carbon monoxide (DLCO) < 80% predicted.

### Statistical analysis

Statistical analyses were performed with R version 4.0.5 (Figure 1). Data transformation and visualization were accomplished by tidyverse (Wickham et al., 2019)⁠, ggplot2 (Wickham, 2016)⁠, ggvenn, plotROC (Sachs, 2017),⁠ and cowplot (Wilke, 2019)⁠ packages. The recorded variables were binarized as shown in Appendix 1—table 1. Acute COVID-19 severity strata were defined as presented in Table 1. p-Values were corrected for multiple comparisons with the Benjamini–Hochberg method (Benjamini and Hochberg, 1995), and effects were termed significant for p<0.05.

### Variable overlap, kinetics, and risk modeling

Overlap between the 180-day follow-up outcome features was assessed by analysis of quasi-proportional Venn plots (package nVennR) (Pérez-Silva et al., 2018)⁠ and calculation of the Cohen’s κ statistic (package vcd) (Fleiss et al., 1969)⁠. Kinetics of binary outcome variables in participants subsets with the complete longitudinal data record was modeled with mixed-effect logistic regression (random effect: individual, fixed effect: time, packages lme4 [Bates et al., 2015]⁠ and lmerTest [Kuznetsova et al., 2017]⁠). Analyses in the severity groups were done with separate models. Significance was assessed by the likelihood ratio test (LRT) against the random-term-only model. Univariate risk modeling was performed with fixed-effect logistic regression (Appendix 1—table 2). Odds ratio (OR) significance was determined by Wald Z test. In-house-developed linear modeling wrappers around base R tools are available at https://github.com/PiotrTymoszuk/lmqc.

### Cluster analysis

Clustering of non-CT and non-LF binary clinical features (Appendix 1—table 1) was accomplished with PAM algorithm (partitioning around medoids, package cluster) (Amato et al., 2019)⁠ and simple matching distance (SMD, package nomclust) (Boriah et al., 2008)⁠. Association analysis for the participants was performed with a combined procedure involving clustering of the observations by the self-organizing map algorithm (SOM, 4 × 4 hexagonal grid, SMD distance, kohonen package), followed by clustering of the SOM nodes by the Ward.D2 hierarchical clustering algorithm (Euclidean distance, hclust() function, package stats) (Vesanto and Alhoniemi, 2000; Kohonen, 1995; Wehrens and Kruisselbrink, 2018)⁠. Clustering analyses were performed in the participant subset with the complete set of clustering variables. The selection of the optimal clustering algorithm was motivated by the highest ratio of between-cluster to total variance and the best stability measured by mean classification error in 20-fold cross-validation (CV) (Figure 6—figure supplement 1A and B, Figure 7—figure supplement 1A and B; Lange et al., 2004)⁠. The optimal cluster number was determined by the bend of the within-cluster sum-of-squares curve (function fviz_nbclust(), package factoextra) and by the stability in 20-fold CV (Figure 6—figure supplement 1C and D, Figure 7—figure supplement 1D and F; Lange et al., 2004; Wang, 2010)⁠, as well as by a visual inspection of the SOM node clustering dendrograms (Figure 7—figure supplement 1E). Assignment of 180-day follow-up outcome features to the clusters of clinical parameters was accomplished with a k-nearest neighbor (kNN) label propagation algorithm (Appendix 1—table 3; Sahanic et al., 2021; Leng et al., 2013)⁠. Cluster assignment visualization in a four-dimensional principal analysis score plot was done with the PCAproj() tool (package pcaPP) (Croux et al., 2007)⁠. To determine the importance of particular clustering variables, the variance (between-cluster to total variance ratio) between the initial cluster structure and the structure with random resampling of the variable was compared, as initially proposed for the random forests ML classifier (Breiman, 2001)⁠. Frequencies of the outcome events in the participant clusters were compared with χ2 test. In-house-developed association analysis wrappers are available at https://github.com/PiotrTymoszuk/clustering-tools-2.

### Machine learning

ML classifiers C5.0 (package C50) (Quinlan, 1993)⁠, random forests (randomForest) (Breiman, 2001)⁠, support vector machines with radial kernel (kernlab) (Weston and Watkins, 1998)⁠, neural networks (nnet) (Ripley, 2014)⁠, and elastic net (glmnet) (Friedman et al., 2010)⁠ were trained to predict the 180-day follow-up outcomes employing non-CT and non-LF binary explanatory features (Appendix 1—table 1). The ML training was performed in the participant subsets with the complete set of explanatory and outcome variables. The training, optimization, and CV (20-fold, five repetitions) were accomplished by the train() tool from caret package, with the Cohen’s κ statistic as a model selection metric (Appendix 1—table 4; Kuhn, 2008)⁠. Classifier ensembles were constructed with the elastic net procedure (caretStack() function, caretEnsemble package, Appendix 1—table 4; Deane-Mayer and Knowles, 2019)⁠. Classifier performance in the training cohort and CV was assessed by receiver-operating characteristics (ROCs), Cohen’s κ and accuracy (packages caret and vcd, Appendix 1—table 5; Fleiss et al., 1969; Kuhn, 2008)⁠. Variable importance measures were extracted from the C5.0 (percent variable usage, c5imp() function, package C50) (Quinlan, 1993)⁠, random forests (Δ Gini index, importance(), package randomForest) (Breiman, 2001)⁠, and elastic net classifiers (regression coefficient β, coef(), package glmnet) (Friedman et al., 2010)⁠.

### Pulmonary recovery assessment app

Participant clustering and ML classifiers trained in the CovILD cohort were implemented in an open-source online pulmonary assessment R shiny app (https://im2-ibk.shinyapps.io/CovILD/; code: https://github.com/PiotrTymoszuk/COVILD-recovery-assessment-app). Prediction of the cluster assignment based on the user-provided patient data is done by the kNN label propagation algorithm (Sahanic et al., 2021; Leng et al., 2013)⁠.

## Results

### Patient characteristics

The CovILD study participants (n = 145) were predominantly male (57.8%), age ranging between 19 and 87 years. 77.2% of participants displayed preexisting comorbidity, predominantly cardiovascular and metabolic disease. The cohort included mild (outpatient care, 24.8%), moderate (hospitalization without oxygen supply, 25.5%), severe (hospitalization with oxygen supply, 27.6%), and critical (intensive care unit [ICU] treatment, 22.1%) cases of acute COVID-19 (Table 1). The majority of hospitalized participants received anti-infectives during acute COVID-19, anticoagulative, and/or antiplatelet treatment introduced primarily in the ventilated patients. Systemic steroid administration was initiated at the discretion of the physician beginning from week 4 after diagnosis (Table 2).

### Clinical recovery after COVID-19

Most patients, irrespective of the acute COVID-19 severity, showed a significant resolution of disease symptoms over time (Figure 1, Figure 2A). Persistent complaints at the 6-month follow-up were reported by 49% of the study subjects (Table 3), with self-reported impaired physical performance (34.7%), sleep disorders (27.1%), and exertional dyspnea (22.8%) as leading manifestations. The frequency of all investigated symptoms declined significantly, even though the pace of their resolution was remarkably slower in the late (100- and 180-day follow-ups) than in the early recovery phase (acute COVID-19 till 60-day follow-up) (Figure 2B).

![Figure 1.](https://cdn.elifesciences.org/articles/72500/elife-72500-fig1-v2.jpg)

![Figure 2.](https://cdn.elifesciences.org/articles/72500/elife-72500-fig2-v2.jpg)

**Figure 2.:** Recovery from any COVID-19 symptoms was investigated by mixed-effect logistic modeling (random effect: individual; fixed effect: time). Significance was determined by the likelihood ratio test corrected for multiple testing with the Benjamini–Hochberg method, and p-values and the numbers of complete observations are indicated in the plots. (A) Frequencies of individuals with any symptoms in the study cohort stratified by acute COVID-19 severity. (B) Frequencies of participants with particular symptoms. imp.: impaired.

Impaired LF was observed in 33.6% of the participants at the 6-month follow-up (Table 3). Except for the critical COVID-19 survivors (60 days: 66.7%; 180 days post-COVID-19: 50%), no significant reduction in the frequency of LF impairment over time was observed (Figure 3). At the 6-month follow-up, structural lung abnormalities were found in 48.5% of patients and moderate-to-severe radiological lung alterations (CT severity score > 5) were present in 19.4% of participants (Table 3). The majority of the participants with impaired LF displayed radiological lung findings. However, a substantial fraction of CT abnormalities, especially mild ones, were accompanied neither by persistent symptoms nor by LF deficits (Figure 3—figure supplement 1, Figure 3—figure supplement 2, Figure 3—figure supplement 3A).

![Figure 3.](https://cdn.elifesciences.org/articles/72500/elife-72500-fig3-v2.jpg)

**Figure 3.:** Recovery from any lung computed tomography (CT) abnormalities, moderate-to-severe lung CT abnormalities (severity score > 5), and recovery from functional lung impairment were investigated in the participants stratified by acute COVID-19 severity by mixed-effect logistic modeling (random effect: individual; fixed effect: time). Significance was determined by the likelihood ratio test corrected for multiple testing with the Benjamini–Hochberg method. Frequencies of the given abnormality at the indicated time points are presented, and p-values and the numbers of complete observations are indicated in the plots.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/72500/elife-72500-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Numbers and percentages of the study participants with any persistent symptoms, functional lung impairment, or lung CT abnormalities at the consecutive follow-up visits presented in quasi-proportional Venn diagrams. The numbers of participants with CT abnormalities, lung function (LF) impairment, and persistent symptoms are indicated in the diagrams, and the numbers of complete observations are shown under the plots.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/72500/elife-72500-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** Numbers and percentages of the study participants with any persistent symptoms, functional lung impairment, or moderate-to-severe lung CT abnormalities (severity score > 5) at the consecutive follow-up visits presented in quasi-proportional Venn diagrams. The numbers of participants with CT abnormalities, lung function (LF) impairment, and persistent symptoms are indicated in the diagrams, and the numbers of complete observations are shown under the plots.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/72500/elife-72500-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** Prognostic value of functional lung impairment and persistent symptoms for prediction of radiological lung abnormalities. (A) Relevance of functional lung impairment and persistent COVID-19 symptoms at predicting any lung CT abnormalities and moderate-to-severe lung CT abnormalities (severity score > 5) at the consecutive follow-up visits. The concordance of the outcome variables was determined by Cohen’s κ coefficient. Statistical significance (κ ̸ = 0) was assessed by two-tailed t-test corrected for multiple testing with the Benjamini–Hochberg method. Kappa with 95% confidence intervals and p values are presented as a heat map. The number of complete observations is indicated in the plot. (B) Percentages of mild (severity score ≤ 5) and moderate-to-severe lung CT abnormalities at the consecutive follow-up visits in the study participants stratified by the severity of acute COVID-19. Statistical significance of frequency differences was determined by χ2 test for trend corrected for multiple testing with the Benjamini–Hochberg method. The number of complete observations is indicated under the plots.

The frequency, scoring, and recovery of CT lung findings were related to the severity of acute infection. Pulmonary lesions scored > 5 CT severity points at the 180-day follow-up were most frequent in the individuals with severe and critical acute COVID-19 (Figure 3—figure supplement 3). Notably, the hospitalized group with oxygen therapy demonstrated the fastest recovery kinetics. As for the symptom resolution, LF and CT lung recovery decelerated in the late phase of COVID-19 convalescence (Figure 3).

### Risk factors of protracted recovery

To identify risk factors of delayed recovery at the 6-month follow-up, we screened a set of 52 binary clinical parameters (Appendix 1—table 1) recorded during acute COVID-19 and at the 60-day visit by univariate modeling (Appendix 1—table 2). By this means, no significant correlates for long-term symptom persistence were identified. Risk factors and readouts of severe and critical COVID-19 including multimorbidity, malignancy, male sex, prolonged hospitalization, ICU stay, and immunosuppressive therapy were significantly associated with persistent CT (Figure 4) and LF abnormalities (Figure 5). Persistently elevated inflammatory markers, IL-6 (>7 ng/L) and CRP (>0.5 mg/L), were strong unfavorable risk factors for incomplete radiological and functional pulmonary recovery. Additionally, the biochemical readout of microvascular inflammation, D-dimer (>500 pg/mL) was significantly linked to LF deficits. Low serum anti-S1/S2 IgG titers at the 60-day follow-up and ambulatory acute COVID-19 correlated with an improved pulmonary recovery (Figures 4 and 5).

![Figure 4.](https://cdn.elifesciences.org/articles/72500/elife-72500-fig4-v2.jpg)

**Figure 4.:** Association of 52 binary explanatory variables (Appendix 1—table 1) with the presence of any lung computed tomography (CT) abnormalities (A) or moderate-to-severe lung CT abnormalities (severity score > 5) (B) at the 180-day follow-up visit was investigated with a series of univariate logistic models (Appendix 1—table 2). Odds ratio (OR) significance was determined by Wald Z test and corrected for multiple testing with the Benjamini–Hochberg method. ORs with 95% confidence intervals for significant favorable and unfavorable factors are presented in forest plots. Model baseline (ref) and numbers of complete observations are presented in the plot axis text. Q1, Q2, Q3, Q4: first, second, third, and fourth quartile of anti-S1/S2 IgG titer; ICU: intensive care unit.

![Figure 5.](https://cdn.elifesciences.org/articles/72500/elife-72500-fig5-v2.jpg)

**Figure 5.:** Association of 52 binary explanatory variables (Appendix 1—table 1) with the presence of functional lung impairment at the 180-day follow-up visit was investigated with a series of univariate logistic models (Appendix 1—table 2). Odds ratio (OR) significance was determined by Wald Z test and corrected for multiple testing with the Benjamini–Hochberg method. ORs with 95% confidence intervals for the significant favorable and unfavorable factors are presented in a forest plot. Model baseline (ref) and n numbers of complete observations are presented in the plot axis text. Q1, Q2, Q3, Q4: first, second, third, and fourth quartile of anti-S1/S2 IgG titer; CKD: chronic kidney disease.

### Clusters of clinical features linked to persistent symptoms and lung abnormalities

Employing the unsupervised PAM algorithm (Amato et al., 2019)⁠, three clusters of co-occurring non-CT and non-LF clinical features of acute COVID-19 and early convalescence (Appendix 1—table 1) were identified (Figure 6—figure supplement 1, Appendix 1—table 3): (1) cluster 1 with male sex, hypertension, and cardiovascular and metabolic comorbidity; (2) cluster 2, including characteristics of acute COVID-19 severity and inflammatory markers; and (3) cluster 3 consisting of acute and persistent COVID-19 symptoms (Figure 6—figure supplement 2, Appendix 1—table 3).

The 6-month follow-up outcome variables were incorporated in the cluster structure using kNN prediction (Leng et al., 2013)⁠. Long-term symptom persistence was associated with acute and long-lasting COVID-19 symptoms in cluster 3, whereas pulmonary outcome parameters were grouped with cluster 2 features (Figure 6A, Figure 6—figure supplement 2, Appendix 1—table 3). Preexisting comorbidities such as malignancy, kidney, lung and gastrointestinal disease, obesity, and diabetes were found the closest cluster neighbors of mild CT abnormalities (severity score ≤ 5). Moderate-to-severe structural alterations (severity score > 5) and LF deficits were, in turn, tightly linked to markers of protracted systemic inflammation (IL-6, CRP, anemia of inflammation) (Sonnweber et al., 2020;⁠ Figure 6B).

![Figure 6.](https://cdn.elifesciences.org/articles/72500/elife-72500-fig6-v2.jpg)

**Figure 6.:** Clustering of 52 non-computed tomography (non-CT) and non-lung function binary explanatory variables recorded for acute COVID-19 or at the early 60-day follow-up visit (Appendix 1—table 1) was investigated by partitioning around medoids (PAM) algorithm with simple matching distance (SMD) dissimilarity measure (Figure 6—figure supplement 1, Appendix 1—table 3). The cluster assignment for the outcome variables at the 180-day follow-up visit (persistent symptoms, functional lung impairment, mild lung CT abnormalities [severity score ≤ 5] and moderate-to-severe lung CT abnormalities [severity score > 5]) was predicted by k-nearest neighbor (kNN) label propagation procedure. Numbers of complete observations and numbers of features in the clusters are indicated in (A). (A) Cluster assignment of the outcome variables (diamonds) presented in the plot of principal component (PC) scores. The first two major PCs are displayed. The explanatory variables are visualized as points. Percentages of the data set variance associated with the PC are presented in the plot axes. (B) Five nearest neighbors (lowest SMD) of the outcome variables presented in radial plots. Font size, point radius, and color code for SMD values. Q1, Q2, Q3, Q4: first, second, third, and fourth quartile of anti-S1/S2 IgG titer; GITD: gastrointestinal disease; CKD: chronic kidney disease; ICU: intensive care unit; COPD: chronic obstructive pulmonary disease.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/72500/elife-72500-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** Clustering of 52 non-computed tomography (non-CT) and non-lung function binary explanatory variables recorded for acute COVID-19 or at the early 60-day follow-up visit (Appendix 1—table 1). (A, B) Comparison of ‘explained’ variances (between-cluster to total sum-of-squares ratio) (A) and cluster stability (mean classification error in 20-fold cross-validation) (B) in clustering of the data set with several algorithms with k = 3 centers/branches (algorithms: K-means; PAM: partitioning around medoids; HCl Ward.D2: hierarchical clustering with Ward.D2 method; distances: SMD: simple matching distance; Jaccard, Dice, and Cosine). (C, D) The optimal number of the feature clusters in clustering with the optimally performing PAM algorithm with SMD dissimilarity measure was determined by the bend of the total within-cluster sum-of-squares curve (C) and confirmed by good stability (low mean classification error) in 20-fold cross-validation (D).

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/72500/elife-72500-fig6-figsupp2-v2.jpg)

**Figure 6—figure supplement 2.:** Clusters of 52 non-CT and non-lung function binary explanatory variables recorded for acute COVID-19 or at the 60-day follow-up visit (Appendix 1—table 1) were defined by the optimally performing partitioning around medoids (PAM) algorithm and simple matching distance (SMD) dissimilarity measure (Figure 6A, Figure 6—figure supplement 1, Appendix 1—table 3). The cluster assignment for the outcome variables at the 180-day follow-up visit (persistent symptoms, functional lung impairment, mild lung CT abnormalities [severity score ≤ 5], and moderate-to-severe lung CT abnormalities [severity score > 5]) was predicted by k-nearest neighbor (kNN) label propagation procedure. SMD between the features and their cluster assignments are shown in a heat map. The numbers of features in the clusters and the total number of observations are indicated under the plot. CVD: cardiovascular disease; Q1, Q2, Q3, Q4: first, second, third, and fourth quartile of anti-S1/S2 IgG titer; GI: gastrointestinal; PD: pulmonary disease; GITD: gastrointestinal disease; ICU: intensive care unit; COPD: chronic obstructive pulmonary disease; CKD: chronic kidney disease.

### Risk stratification for perturbed pulmonary recovery by unsupervised clustering

Next, we tested whether subsets of patients at risk of an incomplete 6-month recovery may be defined by a similar clustering procedure employing exclusively non-CT and non-LF clinical variables (Appendix 1—table 1). Applying a combined SOM – hierarchical clustering approach, three clusters of the study participants were identified (Figure 7, Figure 7—figure supplement 1; Vesanto and Alhoniemi, 2000; Kohonen, 1995)⁠. Prolonged hospitalization, anti-infective therapy, overweight or obesity, pain during acute COVID-19, and low anti-S1/S2 titers at the 60-day follow-up were found the most influential clustering features (Figure 7—figure supplement 2; Breiman, 2001)⁠. The patient subsets identified by the SOM approach differed significantly in frequency of radiological lung abnormalities and substantially, yet not significantly, in the frequency of LF impairment at the 180-day follow-up. In particular, most of the individuals assigned to the largest, low-risk (LR) subset were CT and LF abnormality-free. The frequency and severity of radiological pulmonary findings were elevated in the smallest intermediate-risk subset (IR) and peaked in the high-risk (HR) group (Figure 8A). Despite a comparable frequency of long-term symptoms between the LR, IR, and HR subsets (Figure 8A), the HR collective showed the lowest prevalence of dyspnea, cough, night sweating, pain, gastrointestinal manifestations, and complete absence of hyposmia at the 180-day follow-up (Figure 8B). Although the LR subset primarily comprised mild COVID-19 cases and the HR subset ICU survivors, the cluster assignment (IR vs. LR, HR vs. LR) remained an independent correlate of persistent CT and LF abnormalities after adjustment for the acute COVID-19 severity (Figure 8—figure supplement 1).

![Figure 7.](https://cdn.elifesciences.org/articles/72500/elife-72500-fig7-v2.jpg)

**Figure 7.:** Study participants (n = 133 with the complete variable set) were clustered with respect to 52 non-CT and non-lung function binary explanatory variables recorded for acute COVID-19 or at the 60-day follow-up visit (Appendix 1—table 1) using a combined self-organizing map (SOM: simple matching distance) and hierarchical clustering (Ward.D2 method, Euclidean distance) procedure (Figure 7—figure supplement 1). The numbers of participants assigned to low-risk (LR), intermediate-risk (IR), and high-risk (HR) clusters are indicated in (A). (A) Cluster assignment of the study participants in the plot of principal component (PC) scores. The first two major PCs are displayed. Percentages of the data set variance associated with the PC are presented in the plot axes. (B) Presence of the most influential clustering features (Figure 7—figure supplement 2) in the participant clusters presented as a heat map. Cluster #1, #2, and #3 refer to the feature clusters defined in Figure 6. Q1, Q2, Q3, Q4: first, second, third, and fourth quartile of anti-S1/S2 IgG titer; GITD: gastrointestinal disease; CKD: chronic kidney disease; CVD: cardiovascular disease; GI: gastrointestinal; PD: pulmonary disease.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/72500/elife-72500-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** Clustering of the study participants (n = 133 with the complete variable set) with respect to 52 non-computed tomography (non-CT) and non-lung function binary explanatory variables recorded for acute COVID-19 or at the 60-day follow-up visit (Appendix 1—table 1). The procedure involved clustering of the observations with self-organizing maps (SOM, 4 × 4 hexagonal grid, distances: SMD: simple matching distance, Jaccard, Dice, or Cosine) followed by clustering of the SOM nodes (algorithms: HCl ward.D2: hierarchical clustering with Ward.D2 method; K-means; PAM: partitioning around medoids; distance: Euclidean). Different combinations of observation dissimilarity measures and SOM node clustering algorithms were tested in the search for the optimal clustering algorithm. (A, B) Comparison of ‘explained’ variances (between-cluster to total sum-of-squares ratio) (A) and cluster stability (mean classification error in 20-fold cross-validation) (B) in clustering of the data set with different observation distance measures and SOM node clustering algorithms. (C) Training of the SOM algorithm, mean distance to the winning un as a function of lgorithm iterations is presented. Note the mean distance plateau indicative of the algorithm convergence (D–F) The optimal number of the SOM node clusters in clustering with the optimally performing SOM HCl algorithm with SMD observation dissimilarity measure. The optimal cluster number was determined by the bend of the total within-cluster sum-of-squares curve (D) and confirmed by visual inspection of the HCl dendrogram (E) and good stability (low mean classification error) in 20-fold cross-validation (F).

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/72500/elife-72500-fig7-figsupp2-v2.jpg)

**Figure 7—figure supplement 2.:** The clusters of participants clusters were defined with the optimally performing self-organizing map (SOM)/HCl algorithm with simple matching distance (SMD) observation dissimilarity measure as presented in Figure 7 and Figure 7—figure supplement 1. The impact of a particular clustering variable was determined by comparing the ‘explained’ clustering variance (between-cluster to total sum-of-squares ratio) between the initial cluster structure and the structure with random resampling of the variable. Differences in the clustering variances for the most influential clustering variables (Δ clustering variance > 0) are presented in the plot. Q1, Q3: first, third quartile of anti-S1/S2 IgG titer; CKD: chronic kidney disease; GI: gastrointestinal; CVD: cardiovascular disease; PD: pulmonary disease; GITD: gastrointestinal disease.

![Figure 8.](https://cdn.elifesciences.org/articles/72500/elife-72500-fig8-v2.jpg)

**Figure 8.:** The clusters of study participants were defined by non-lung function and non-computed tomography (non-CT) features as presented in Figure 7. Frequencies of outcome variables at the 180-day follow-up visit (mild [severity score ≤ 5], moderate-to-severe lung CT abnormalities [severity score > 5], functional lung impairment, and persistent symptoms) were compared between the low-risk (LR), intermediate-risk (IR), and high-risk (HR) participant clusters by χ2 test corrected for multiple testing with the Benjamini–Hochberg method. p-Values and numbers of participants assigned to the clusters are indicated in the plots. (A) Frequencies of the outcome features in the participant clusters. (B) Frequencies of specific symptoms in the participant clusters.

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/72500/elife-72500-fig8-figsupp1-v2.jpg)

**Figure 8—figure supplement 1.:** The clusters of participants were defined by non-lung function and non-computed tomography (non-CT) clinical features of acute COVID-19 and early convalescence (60-day follow-up visit, Appendix 1—table 1) with the optimally performing HCl algorithm with simple matching distance (SMD) observation dissimilarity measure as presented in Figure 7 and Figure 7—figure supplement 1. (A) Distribution of mild, moderate, severe, and critical acute COVID-19 cases in the participant clusters. Significance of the distribution differences was assessed with χ2 test. The numbers of participants assigned to the clusters are indicated under the plot. (B) Association of the participant cluster assignment (LR: low-risk; IR: intermediate-risk; HR: high-risk cluster) with the risk of any lung CT abnormalities and moderate-to-severe lung CT abnormalities (severity score > 5) at the 180-day follow-up visit was investigated by logistic modeling with and without inclusion of the acute COVID-19 severity effect (severity-adjusted). Odds ratio (OR) significance was determined by Wald Z test and corrected for multiple testing with the Benjamini–Hochberg method. ORs with 95% confidence intervals are presented in forest plots. Numbers of complete observations, outcome events, participants in the clusters, and the acute COVID-19 severity subsets are indicated under the plot.

### Prediction of persistent symptoms and pulmonary abnormalities by machine learning

Finally, we investigated if the 6-month follow-up outcome may be predicted by ML classifiers trained with a set of non-CT and non-LF variables recorded during acute COVID-19 and at the 60-day follow-up (Appendix 1—table 1). To this end, five technically unrelated ML classifiers were tested (Appendix 1—table 4; Kuhn, 2008)⁠: C5.0 (Quinlan, 1993)⁠, random forests (RF) (Breiman, 2001)⁠, support vector machines with radial kernel (SVM-R) (Weston and Watkins, 1998)⁠, shallow neural network (Nnet) (Ripley, 2014)⁠, and elastic net generalized linear regression (glmNet) (Friedman et al., 2010)⁠. In addition, the single classifiers with varying outcome-specific accuracy (Figure 9—figure supplement 1) were bundled into ensembles by the elastic net procedure (Figure 9—figure supplement 2, Appendix 1—table 4; Kuhn, 2008; Deane-Mayer and Knowles, 2019)⁠. Finally, the classifier and ensemble performance was investigated in the training cohort and 20-fold CV by ROC (Appendix 1—table 5).

All tested ML algorithms and ensembles demonstrated good accuracy (area under the curve [AUC] > 0.78) and sensitivity (>0.84) at predicting any lung CT abnormalities at the 6-month follow-up in the study cohort serving as a training data set. Their efficiency in CV was moderate (AUC: 0.69–0.81; sensitivity: 0.69–0.78) (Figure 9, Figure 9—figure supplement 3, Appendix 1—table 5). In turn, moderate-to-severe structural lung findings were recognized with markedly lower sensitivity both in the training data set (>0.43) and the CV (0.39–0.48). Even though impaired LF and persistent symptoms were common at the 6-month follow-up in the training data set (Figures 2 and 3), nearly half of the cases were not identified by any of the tested ML algorithms and their ensembles in the CV setting (Figure 9, Figure 9—figure supplement 3, Appendix 1—table 5). The sensitivity of the ensembles and single classifiers at predicting CT and LF abnormalities was substantially better in severe and critical COVID-19 survivors than in ambulatory and moderate cases (Figure 10, Appendix 1—table 6).

![Figure 9.](https://cdn.elifesciences.org/articles/72500/elife-72500-fig9-v2.jpg)

**Figure 9.:** Single machine learning classifiers (C5.0; RF: random forests; SVM-R: support vector machines with radial kernel; NNet: neural network; glmNet: elastic net) and their ensemble (Ens) were trained in the cohort data set with 52 non-computed tomography (non-CT) and non-lung function binary explanatory variables recorded for acute COVID-19 or at the 60-day follow-up visit (Appendix 1—table 1) for predicting outcome variables at the 180-day follow-up visit (any lung CT abnormalities, moderate-to-severe lung CT abnormalities [severity score > 5], functional lung impairment, and persistent symptoms) (Appendix 1—table 4). The prediction accuracy was verified by repeated 20-fold cross-validation (five repeats). Receiver-operating characteristics (ROCs) of the algorithms in the cross-validation are presented: area under the curve (AUC), sensitivity (Sens), and specificity (Spec) (Appendix 1—table 5). The numbers of complete observations and outcome events are indicated under the plots.

![Figure 9—figure supplement 1.](https://cdn.elifesciences.org/articles/72500/elife-72500-fig9-figsupp1-v2.jpg)

**Figure 9—figure supplement 1.:** Machine learning classifiers (C5.0; RF: random forests; SVM-R: support vector machines with radial kernel; NNet: neural network; glmNet: elastic net) were trained in the cohort data set with 52 non-computed tomography (non-CT) and non-lung function binary explanatory variables recorded for acute COVID-19 or at the early 60-day follow-up visit (Appendix 1—table 1) for predicting outcome variables at the 180-day follow-up visit (any lung CT abnormalities, moderate-to-severe lung CT abnormalities [severity score > 5], functional lung impairment, and persistent symptoms) (Figure 9, Appendix 1—table 4). The prediction accuracy was verified by repeated 20-fold cross-validation (five repeats). Pearson’s correlation coefficients of the classifier prediction accuracy in the cross-validation are presented as heat maps. Numbers of complete observations and outcome events are indicated under the plots.

![Figure 9—figure supplement 2.](https://cdn.elifesciences.org/articles/72500/elife-72500-fig9-figsupp2-v2.jpg)

**Figure 9—figure supplement 2.:** Single machine learning classifiers (C5.0; RF: random forests; SVM-R: support vector machines with radial kernel; NNet: neural network; glmNet: elastic net) were trained as shown in Figure 9. The model ensembles based on the single classifiers were constructed with the glmNet procedure (Appendix 1—table 4). glmNet regression coefficients (β) are presented in the plots. Point and text color correspond to the β value. Numbers of complete observations and outcome events are indicated under the plots.

![Figure 9—figure supplement 3.](https://cdn.elifesciences.org/articles/72500/elife-72500-fig9-figsupp3-v2.jpg)

**Figure 9—figure supplement 3.:** Single machine learning classifiers (C5.0; RF: random forests; SVM-R: support vector machines with radial kernel; NNet: neural network; glmNet: elastic net) and their ensembles were trained as shown in Figure 9. Performance of the classifiers in the training data sets was investigated by receiver-operating characteristic (ROC) of the algorithms (AUC: area under the curve; Sens: sensitivity; Spec: specificity, Appendix 1—table 5). Numbers of complete observations and outcome events are indicated under the plots.

![Figure 9—figure supplement 4.](https://cdn.elifesciences.org/articles/72500/elife-72500-fig9-figsupp4-v2.jpg)

**Figure 9—figure supplement 4.:** C5.0, random forests (RF), and elastic net (glmNet) classifiers were trained as presented in Figure 9 for prediction of any lung CT abnormalities at the 180-day follow-up visit. Variable importance measures (C5.0: % attribute/variable usage in the tree model (A); RF: difference in Gini index (B); glmNet: absolute value of the regression coefficient β (C)) for the 10 most influential explanatory variables are presented. CKD: chronic kidney disease; Q1, Q4: first, fourth quartile of anti-S1/S2 IgG titer; PD: pulmonary disease; CKD: chronic kidney disease.

![Figure 9—figure supplement 5.](https://cdn.elifesciences.org/articles/72500/elife-72500-fig9-figsupp5-v2.jpg)

**Figure 9—figure supplement 5.:** C5.0, random forests (RF), and elastic net (glmNet) classifiers were trained as presented in Figure 9 for prediction of moderate-to-severe lung CT abnormalities (severity score > 5) at the 180-day follow-up visit. Variable importance measures (C5.0: % attribute/variable usage in the tree model (A); RF: difference in Gini index (B); glmNet: absolute value of the regression coefficient β (C)) for the 10 most influential explanatory variables are presented. PD: pulmonary disease; GITD: gastrointestinal disease; Q1, Q2, Q4: first, second, fourth quartile of anti-S1/S2 IgG titer.

![Figure 9—figure supplement 6.](https://cdn.elifesciences.org/articles/72500/elife-72500-fig9-figsupp6-v2.jpg)

**Figure 9—figure supplement 6.:** C5.0, random forests (RF), and elastic net (glmNet) classifiers were trained as presented in Figure 9 for prediction of functional lung impairment at the 180-day follow-up visit. Variable importance measures (C5.0: % attribute/variable usage in the tree model (A); RF: difference in Gini index (B); glmNet: absolute value of the regression coefficient β (C)) for the 10 most influential explanatory variables are presented. CKD: chronic kidney disease; Q1, Q2: first. second quartile of anti-S1/S2 IgG titer.

![Figure 9—figure supplement 7.](https://cdn.elifesciences.org/articles/72500/elife-72500-fig9-figsupp7-v2.jpg)

**Figure 9—figure supplement 7.:** C5.0, random forests (RF), and elastic net (glmNet) classifiers were trained as presented in Figure 9 for prediction of persistent symptoms at the 180-day follow-up visit. Variable importance measures (C5.0: % attribute/variable usage in the tree model (A); RF: difference in Gini index (B); glmNet: absolute value of the regression coefficient β (C)) for the 10 most influential explanatory variables are presented. CVD: cardiovascular disease; GITD: gastrointestinal disease; COPD: chronic obstructive lung disease.

![Figure 10.](https://cdn.elifesciences.org/articles/72500/elife-72500-fig10-v2.jpg)

**Figure 10.:** The machine learning classifier ensemble (Ens) was developed as presented in Figure 9. Its performance at predicting outcome variables at the 180-day follow-up visit (any computed tomography [CT] lung abnormalities, moderate-to-severe lung CT abnormalities [severity score > 5], functional lung impairment, and persistent symptoms) in the entire cohort, mild-to-moderate (outpatient or hospitalized without oxygen), and severe-to-critical COVID-19 convalescents (oxygen therapy or ICU) in repeated 20-fold cross-validation (five repeats) was assessed by receiver-operating characteristic (ROC) (Appendix 1—table 6). ROC curves and statistics (AUC: area under the curve; Se: sensitivity; Sp: specificity) in the cross-validation are shown. Numbers of complete observations and outcome events are indicated in the plots.

The most important explanatory variables for pulmonary abnormalities by three unrelated classifiers (C5.0, RF, and glmNet) included preexisting malignancy, multimorbidity, markers of systemic inflammation (IL-6 and CRP), and anti-S1/S2 antibody levels at the 60-day follow-up (Figure 9—figure supplement 4, Figure 9—figure supplement 5, Figure 9—figure supplement 6). The highly influential parameters at prediction of symptoms at the 180-day follow-up encompassed symptom presence at the 60-day follow-up, as well as obesity and dyspnea during acute COVID-19 (Figure 9—figure supplement 7).

## Discussion

Herein, we prospectively evaluated trajectories of COVID-19 recovery in an observational cohort enrolled in the Austrian CovILD study (Sonnweber et al., 2021)⁠. Despite the resolution of symptoms and pulmonary abnormalities at the 6-month follow-up in a large fraction of the study participants, the recovery pace was substantially slower in the late convalescence when compared with the first three months after diagnosis (Sonnweber et al., 2021; Huang et al., 2021a)⁠. Persistent symptoms and CT findings were detected in more than 40% and reduced LF in approximately one-third of the cohort, which is in line with recovery kinetics and signs of lung lesion chronicity reported by others (Caruso et al., 2021; Huang et al., 2021b; Huang et al., 2021a; Faverio et al., 2021; Hellemons et al., 2021; Zhou et al., 2021)⁠. By comparison, similar protracted pulmonary recovery was reported for SARS (Hui et al., 2005; Ng et al., 2004; Ngai et al., 2010; Lam et al., 2009)⁠ and non-COVID-19 acute respiratory distress syndrome (Wilcox et al., 2013; Masclans et al., 2011)⁠. Of note, treatment approaches for hospitalized patients in our cohorts and similar cohorts recruited at the pandemic onset in early 2020 (Caruso et al., 2021; Huang et al., 2021b; Huang et al., 2021a; Faverio et al., 2021; Hellemons et al., 2021)⁠ differ significantly from the current standard of care for acute COVID-19, which includes early systemic steroid use and antiviral and various immunomodulatory medications. How improved standardized therapy and anti-SARS-CoV-2 vaccination affect the clinical and pulmonary recovery needs to be investigated.

In roughly half of our study participants with abnormal lung CT findings, and especially in those with low-grade structural abnormalities, no overt LF impairment at follow-up was discerned. Still, even subclinical lung alterations may bear the potential for clinically relevant progression of interstitial lung disease (Suliman et al., 2015; Hatabu et al., 2020) requiring systematic CT and LF monitoring. Conversely, symptom persistence was weakly associated with incomplete functional or structural pulmonary recovery.

Since PASC are found in as many as 10% of COVID-19 patients (Sahanic et al., 2021; Venkatesan, 2021; Sudre et al., 2021b)⁠, robust, resource-saving tools assessing the individual risk of pulmonary complications are urgently needed (Shah et al., 2021; Raghu and Wilson, 2020)⁠. Covariates and characteristics of severe acute COVID-19 such as male sex, age, and preexisting comorbidities, hospitalization, ventilation, and ICU stay were proposed as the risk factors of persistent pulmonary impairment (Sonnweber et al., 2021; Caruso et al., 2021; Huang et al., 2021a; Faverio et al., 2021; Raghu and Wilson, 2020)⁠. However, their applicability in predicting complications of pulmonary recovery from mild or moderate COVID-19 is limited. Our results of univariate modeling, clustering, and ML prediction point towards a distinct long-term pulmonary risk phenotype that manifests during acute COVID-19 and early recovery and whose central components are protracted systemic (IL-6, CRP, anemia of inflammation) and microvascular inflammation (D-dimer), and strong humoral response (anti-S1/S2 IgG) demographic risk factors and comorbidities (Sonnweber et al., 2020)⁠. Hence, consecutive monitoring of systemic inflammatory parameters analogous to concepts of interstitial lung disease in autoimmune disorders (Khanna et al., 2020) and anti-S1/S2 antibody levels may improve identification of the individuals at risk of chronic pulmonary damage irrespective of the acute COVID-19 severity.

Clustering and ML have been employed for deep phenotyping and predicting acute and post-acute COVID-19 outcomes in multivariable data sets (Sahanic et al., 2021; Sudre et al., 2021a; Estiri et al., 2021; Demichev et al., 2021; Benito-León et al., 2021)⁠. We demonstrate that subsets of COVID-19 patients that significantly differ in the risk for long-term CT abnormalities may be defined by an easily accessible clinical parameter set available at the early post-COVID-19 assessment. This approach did not involve any CT or LF variables. Furthermore, the cluster classification correlated with the risk of long-term pulmonary abnormalities independently of the acute COVID-19 severity. Thus, these characteristics provide a useful tool for broad screening of convalescent populations, including individuals who experienced mild or moderate COVID-19.

We show that technically unrelated ML classifiers and their ensemble trained without CT and LF explanatory variables can predict lung CT findings independently of their grading at the 6-month follow-up with good specificity and sensitivity in the training collective and CV. By contrast, the more specific prediction of moderate-to-severe lung CT or risk estimation for LF deficits demonstrated a limited sensitivity. For the moderate-to-severe CT abnormalities, this can be primarily traced back to their low frequency resulting in a suboptimal classifier training, especially in CV. A substantial fraction of the participants (20.7%, n = 30) suffered from a preexisting respiratory condition (pulmonary disease, asthma, or COPD) likely paralleled by LF reduction, which possibly confounded the prediction of the post-COVID-19 LF deficits both by clustering and ML. Accumulating evidence suggests that post-acute COVID-19 symptoms are highly heterogeneous conditions with multiorgan, neurocognitive, and psychological manifestations (Sahanic et al., 2021; Evans et al., 2021; Davis et al., 2021)⁠, which may differ in risk factor constellations. This could explain why univariate modeling, clustering, and ML failed to estimate persistent symptom risk in our small study cohort. In general, the ML prediction quality may greatly benefit from a larger training data set and inclusion of additional explanatory variables such as cellular readouts of inflammation, in-depth medication, and broader acute symptom data. Nevertheless, the herein described cluster- and ML classifiers represent resource-effective tools that may assist in the screening of medical record data and identification of COVID-19 patients requiring systematic CT and LF monitoring. To facilitate the identification of patients at risk for protracted respiratory recovery and enable validation in an external collective, we implemented the clustering and prediction procedures in an open-source risk assessment application (https://im2-ibk.shinyapps.io/CovILD/).

Our study bears limitations primarily concerning the low sample size and the cross-sectional character of the trial. Because of the impaired availability of the patients and the prolonged inpatient rehabiliation, the 60- and 100-day follow-up visits in part showed a temporal overlap that may have impacted the accuracy of the longitudinal data. Missingness of the consecutive outcome variable record and the participant dropout, particularly of mild and moderate COVID-19 cases, may have also potentially confounded the participant clustering results and ML risk estimation for CT abnormalities and LF impairment since prolonged hospitalization was found to be a crucial cluster-defining and influential explanatory feature. Additionally, even though the reproducibility of the risk assessment algorithms was partially addressed by CV, cluster and ML classifiers call for verification in a larger, independent multicenter collective of COVID-19 convalescents.

In summary, in our CovILD study cohort we found a high frequency of CT and LF abnormalities and persistent symptoms at the 6-month follow-up, and a flattened recovery kinetics after 3 months post-COVID-19. Systematic risk modeling reveled a set of clinical variables linked to protracted pulmonary recovery apart from the severity of acute infection such as inflammatory markers, anti-S1/S2 IgG levels, multimorbidity, and male sex. We demonstrate that clustering and ML classifiers may help to identify individuals at risk of persistent lung lesions and to relocate medical resources to prevent long-term disability.
