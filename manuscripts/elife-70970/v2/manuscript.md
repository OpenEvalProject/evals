# Ten months of temporal variation in the clinical journey of hospitalised patients with COVID-19: An observational cohort

## Authors

- Sheryl Ann Abdukahil
- Matthew D Hall<sup>1</sup> ([ORCID: 0000-0002-2671-3864](https://orcid.org/0000-0002-2671-3864)) †
- Joaquín Baruch<sup>2</sup>
- Gail Carson<sup>2</sup>
- Barbara Wanjiru Citarella<sup>2</sup>
- Andrew Dagens<sup>2</sup>
- Emmanuelle A Dankwa<sup>3</sup>
- Christl A Donnelly<sup>3</sup>
- Jake Dunning<sup>2</sup>
- Martina Escher<sup>2</sup>
- Christiana Kartsonaki<sup>5</sup>
- Laura Merson<sup>2</sup> ([ORCID: 0000-0002-4168-1960](https://orcid.org/0000-0002-4168-1960))
- Mark Pritchard<sup>2</sup>
- Jia Wei<sup>1</sup>
- Peter W Horby<sup>2</sup>
- Amanda Rojek<sup>2</sup>
- Piero L Olliaro<sup>2</sup>

### Affiliations

1. Big Data Institute, Nuffield Department of Medicine, University of Oxford Oxford United Kingdom
2. ISARIC Global Support Centre, Centre for Tropical Medicine and Global Health, Nuffield Department of Medicine, University of Oxford Oxford United Kingdom
3. Department of Statistics, University of Oxford Oxford United Kingdom
4. MRC Centre for Global Infectious Disease Analysis, Abdul Latif Jameel Institute for Disease and Emergency Analytics and Department of Infectious Disease Epidemiology, Imperial College London London United Kingdom
5. MRC Population Health Research Unit, Clinical Trials Service Unit and Epidemiological Studies Unit, Nuffield Department of Population Health, University of Oxford Oxford United Kingdom
6. Infectious Diseases Data Observatory, Centre for Tropical Medicine and Global Health, University of Oxford Oxford United Kingdom
7. Royal Melbourne Hospital, Melbourne, Australia Centre for Integrated Critical Care, University of Melbourne Melbourne Australia

† Corresponding author

## Abstract

Background:There is potentially considerable variation in the nature and duration of the care provided to hospitalised patients during an infectious disease epidemic or pandemic. Improvements in care and clinician confidence may shorten the time spent as an inpatient, or the need for admission to an intensive care unit (ICU) or high dependency unit (HDU). On the other hand, limited resources at times of high demand may lead to rationing. Nevertheless, these variables may be used as static proxies for disease severity, as outcome measures for trials, and to inform planning and logistics.Methods:We investigate these time trends in an extremely large international cohort of 142,540 patients hospitalised with COVID-19. Investigated are: time from symptom onset to hospital admission, probability of ICU/HDU admission, time from hospital admission to ICU/HDU admission, hospital case fatality ratio (hCFR) and total length of hospital stay.Results:Time from onset to admission showed a rapid decline during the first months of the pandemic followed by peaks during August/September and December 2020. ICU/HDU admission was more frequent from June to August. The hCFR was lowest from June to August. Raw numbers for overall hospital stay showed little variation, but there is clear decline in time to discharge for ICU/HDU survivors.Conclusions:Our results establish that variables of these kinds have limitations when used as outcome measures in a rapidly evolving situation.Funding:This work was supported by the UK Foreign, Commonwealth and Development Office and Wellcome [215091/Z/18/Z] and the Bill & Melinda Gates Foundation [OPP1209135]. The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.

## Introduction

During an epidemic or pandemic of a novel infectious disease, variations in the duration of each stage of a hospitalised patient’s progress from symptom onset, to hospital admission, and hence to outcome are critical for an effective response. Clinicians use these data as a proxy for disease severity, and to provide prognostic information to patients and their families. Policy makers use these data to inform system wide planning for staffing, infrastructure, to predict requirements for consumables (such as personal protective equipment), and to assess performance of the hospital system. And for clinical research, these measures are used as trial outcomes to determine the efficacy of novel treatments.

Often, the extent to which patient journeys vary during an epidemic is not understood. There are changes in clinical practice (World Health Organisation, 2021) – clinical understanding of the natural history of diseases improves with time (Docherty et al., 2021), and so too does confidence in safe discharge criteria or in alternative models of care (Rojek and Horby, 2016), such as remote monitoring (Nunan et al., 2020; Bell et al., 2021). Moreover, the introduction of effective treatments (Rochwerg et al., 2020) and standardisation of care may rapidly reduce the severity or time course of illness (Dennis et al., 2021). However, decisions about whether to admit or escalate care are also dependent on logistic factors such as the availability of resources (e.g. ventilators, intensive care beds, staff) that may be rationed during the peak of a pandemic, but abundant at other phases of an outbreak (Tyrrell et al., 2021; National Institute for Health and Care Excellence, 2021; Pagel et al., 2020). There may also be changes in policy to admit patients for indications that are not clinical – such as to facilitate effective quarantine (Wuhan Novel Coronavirus, 2021) or supervise provision of treatments in clinical trials. We hypothesise that there is significant variation in the patient journey over a pandemic period, and that this variability may limit the way these data can be responsibly used.

In this paper, we assess temporal changes in hospital admission, length of stay, and escalation of care for hospitalised patients with SARS-CoV-2 infection included in the International Severe Acute Respiratory and emerging Infection Consortium (ISARIC) WHO Clinical Characterisation Protocol International cohort (ISARIC Clinical Characterisation Group, 2020). This is to our knowledge the largest, prospective international cohort including standardised clinical data, and, as of the time of writing, includes data collected from 26 January 2020 to 20 September 2021 on 708,085 people hospitalised with COVID-19 in 1669 sites in 64 countries.

We use this dataset to determine whether these variables did indeed change over the course of the SARS-CoV-2 pandemic during 2020, and where there are changes, explore if there are predictable influences that account for this.

## Methods

As previously described (ISARIC Clinical Characterisation Group, 2021), eligible for recruitment were patients with confirmed or suspected COVID-19 infection admitted to an ISARIC partner site and submitted to the ISARIC-hosted REDCap system. Additional data contributed to ISARIC via other mechanisms have not been included due to differences in data structure. The datasets used in analyses in this paper are drawn from a population of all patients with a symptom onset date, or hospital admission date, recorded between March and December 2020 inclusive. Follow-up could be conducted until 8 March 2021, at which point the dataset was closed. Some patients had a recorded hospital admission date before their symptom onset date. In most cases, this would represent a nosocomial infection, but sometimes it could instead be that the patient was coincidentally admitted for a separate medical condition during their incubation period. In either case their admission date would not represent the start of their hospital treatment for COVID-19, and so we recorded the latter variable, hereafter ‘COVID-19 admission date’, as the later of the symptom onset date and hospital admission date. Patients were followed until they left the study site, due to death, hospital discharge, or another reason (such as transfer to another facility). Patients lost to follow-up before any of these outcome events were included, unless the time to that event was the variable of interest in a particular analysis. (For example, in question 5, below, time to death and discharge were used as dependent variables, and patients lost to follow-up, for whom this time was not recorded, were excluded.)

We used the complete dataset described above to explore temporal variation in six variables or collections of variables. Not all patients had recorded information for the variables of interest in each question, so, in each case, a subset was analysed. The questions and data subsets were as follows:

Question 1

Variation in the time from symptom onset to hospital admission. Patients were excluded if this variable was not available, or if they were admitted prior to symptom onset.

Question 2

Variation in the proportion of patients being admitted to an ICU or HDU. Patients were excluded if this variable was not available.

Question 3

Variation in the time from COVID-19 admission to ICU/HDU admission. Patients were excluded if they were never admitted to an ICU or HDU, or if this variable was otherwise not available.

Question 4

Variation in the overall case fatality rate. Patients were excluded if the final outcome of their hospital stay was either not recorded or recorded as something other than “death” or “discharge” (for example, transfer to another facility).

Question 5

Variation in the time from COVID-19 admission to death or discharge. (We describe either as an “outcome”.) Exclusions were as in question 4, as well as patients who had a recorded outcome but no recorded outcome date.

Question 6

Variation in the status of patients (admitted, ICU/HDU admitted, dead, discharged, or unknown outcome) on a given day after admission. Excluded here were patients whose ICU/HDU status on the day of admission was unknown.

Further filtering was done to (a) remove any nonsensical values (such as recorded time of hospital admission after hospital exit), (b) remove patients admitted to hospital in 2021 for all questions except 1 (such patients were included when exploring the latter due to right censoring concerns if they were omitted), and (c) when considering hospital admission (question 1), ICU/HDU admission (questions 2 and 3) or final outcome (questions 4–6), exclude patients for whom the time to that event was in the top 2.5 % of recorded values (as this range included extreme outliers that may have been the result of incorrect data entry). We designate these three limits by ladmission, lICU and Ioutcome respectively.

The values of lICU and Ioutcome also define a time period over which the events of ICU/HDU admission and final outcome (respectively) can be defined for questions 2 and 4. Thus, in question 4, the actual variable of interest is death or discharge within Ioutcome days. For question 2, the variable is ICU/HDU admission within lICU days of observation. As a result, we additionally excluded patients with incomplete follow-up who were observed for less than lICU days from COVID-19 admission without experiencing ICU/HDU admission, as such an event may have occurred within the time limit without it being observed.

For all analyses with a single outcome variable, we plotted its mean value against the epidemiological week of symptom onset (question 1) or COVID-19 admission (others), both overall and with respect to various variables of interest (e.g. age group).

For the exploration of patient status by day after COVID-19 admission (question 6), the progress of a patient along the course of their hospital stay was visualised by means of Sankey diagrams. Five states were considered: ward occupancy, ICU/HDU occupancy, the final outcomes of death or discharge, and unknown outcome. We recorded the state of each patient on the day of admission, on every subsequent day, and their final outcome. Where a patient’s exact location (ward or ICU/HDU) in the hospital was not recorded on a given day, their last known location was used. For the figures in this article, we present only the data on day of COVID-19 admission (A), 3 days later (A + 3), 7 days later (A + 7), and final outcome (O + 1). An interactive version of this diagram is currently under development and will be made available to the research community as soon as possible.

The four most frequent symptoms at admission were cough, fatigue, fever, and shortness of breath. We introduced a new variable to the dataset counting the number of these present at admission for each patient. Missing data was disregarded here, so this represents a lower bound.

### Statistical analysis

Multivariable linear regression was used to investigate factors associated with time from onset of symptoms to hospital admission (question 1), time from COVID-19 admission to ICU/HDU admission (question 3), and time from COVID-19 admission to death or discharge (question 5). In all cases, the dependent variable was log-transformed and a pseudocount of 1 added in order to prevent taking logarithms of zero. Multivariable logistic regression was used to investigate factors associated with ICU/HDU admission (question 2) and fatal outcome (question 5), and to adjust for these factors as potential confounders for our primary outcome variables; for a full list of these variables, see Supplementary file 1. For all regression analyses, we analysed the presence of comorbidities as covariables. As there was a considerable amount of missing data for each of these, we introduced an ‘unknown’ class to the regression models for these variables rather than exclude patients without values for them entirely. After this modification, every regression analysis was performed as a complete case analysis.

The significance of every dependent variable in every model, including interaction terms used in regressions for hCFR (question 4) and time to outcome (question 5) was assessed using the Wald test.

### Software

All analyses were performed in R 4.0.3 (R Development Core Team, 2013), with packages including the tidyverse (Wickham et al., 2019), and ggalluvial (Brunson, 2020). Code for processing the data and performing the regression analyses is available, copy archived at swh:1:rev:ce42035d6cf80852089d95264215f7bb487cb998 (Hall, 2021).

## Results

### Patient characteristics

Our complete dataset consisted of 142,540 patients (60,977 female, 81,325 male, 238 unknown sex), of median age 70 [IQR 56–82], admitted at 620 sites in 47 countries. Table 1 shows a summary of baseline characteristics, and more detail, including country of origin and cross tabulation by month of admission, can be found in Supplementary file 2.

**Table 1.**
 Baseline characteristics of the included patients.*Some patients admitted in early 2021 are included in order to fully represent patients with symptom onset in December 2020.


<table>
  <thead>
    <tr>
      <th>Variable</th>
      <th>Value</th>
      <th>Count</th>
      <th>%</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Month of admission</td>
      <td>March</td>
      <td>27,108</td>
      <td>19.4</td>
    </tr>
    <tr>
      <td></td>
      <td>April</td>
      <td>42,267</td>
      <td>30.3</td>
    </tr>
    <tr>
      <td></td>
      <td>May</td>
      <td>12,311</td>
      <td>8.82</td>
    </tr>
    <tr>
      <td></td>
      <td>June</td>
      <td>5,342</td>
      <td>3.83</td>
    </tr>
    <tr>
      <td></td>
      <td>July</td>
      <td>2,811</td>
      <td>2.01</td>
    </tr>
    <tr>
      <td></td>
      <td>August</td>
      <td>2,218</td>
      <td>1.59</td>
    </tr>
    <tr>
      <td></td>
      <td>September</td>
      <td>5,265</td>
      <td>3.77</td>
    </tr>
    <tr>
      <td></td>
      <td>October</td>
      <td>13,822</td>
      <td>9.91</td>
    </tr>
    <tr>
      <td></td>
      <td>November</td>
      <td>15,155</td>
      <td>10.9</td>
    </tr>
    <tr>
      <td></td>
      <td>December</td>
      <td>13,205</td>
      <td>9.47</td>
    </tr>
    <tr>
      <td>Sex</td>
      <td>Female</td>
      <td>59,719</td>
      <td>42.8</td>
    </tr>
    <tr>
      <td></td>
      <td>Male</td>
      <td>79,550</td>
      <td>57</td>
    </tr>
    <tr>
      <td></td>
      <td>Unknown</td>
      <td>235</td>
      <td>0.168</td>
    </tr>
    <tr>
      <td>Age group</td>
      <td>0–19</td>
      <td>2,697</td>
      <td>1.93</td>
    </tr>
    <tr>
      <td></td>
      <td>20–39</td>
      <td>9,302</td>
      <td>6.67</td>
    </tr>
    <tr>
      <td></td>
      <td>40–59</td>
      <td>30,399</td>
      <td>21.8</td>
    </tr>
    <tr>
      <td></td>
      <td>60–69</td>
      <td>22,815</td>
      <td>16.4</td>
    </tr>
    <tr>
      <td></td>
      <td>70–79</td>
      <td>29,901</td>
      <td>21.4</td>
    </tr>
    <tr>
      <td></td>
      <td>80+</td>
      <td>41,571</td>
      <td>29.8</td>
    </tr>
    <tr>
      <td></td>
      <td>Unknown</td>
      <td>2,819</td>
      <td>2.02</td>
    </tr>
    <tr>
      <td>Symptom onset post-admission</td>
      <td>No</td>
      <td>118,874</td>
      <td>85.2</td>
    </tr>
    <tr>
      <td></td>
      <td>Yes</td>
      <td>11,695</td>
      <td>8.38</td>
    </tr>
    <tr>
      <td></td>
      <td>Unknown</td>
      <td>8,935</td>
      <td>6.4</td>
    </tr>
  </tbody>
</table>

Table 2 shows the prevalence of symptoms at admission and comorbidities. A total of 1030 individuals (0.7%) were pregnant women.

**Table 2.**
 Prevalence of symptoms at hospital admission and comorbidities.The final column gives the number of times the condition is recorded as present over the number of times its presence or absence is recorded (i.e. the data is non-missing). Designated “common” symptoms are indicated with a (C); the number and percentages of patients presenting with combinations of these are separately presented.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Name</th>
      <th>% present</th>
      <th>N (present)/n (data recorded)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Symptoms at admission</td>
      <td>Cough (C)</td>
      <td>66.6</td>
      <td>(87218/131002)</td>
    </tr>
    <tr>
      <td></td>
      <td>Shortness of breath (C)</td>
      <td>64.4</td>
      <td>(89611/139244)</td>
    </tr>
    <tr>
      <td></td>
      <td>Fever (C)</td>
      <td>63.4</td>
      <td>(84665/133494)</td>
    </tr>
    <tr>
      <td></td>
      <td>Fatigue (C)</td>
      <td>44.7</td>
      <td>(52837/118184)</td>
    </tr>
    <tr>
      <td></td>
      <td>Confusion</td>
      <td>24.9</td>
      <td>(31167/125123)</td>
    </tr>
    <tr>
      <td></td>
      <td>Vomiting</td>
      <td>19.9</td>
      <td>(24577/123625)</td>
    </tr>
    <tr>
      <td></td>
      <td>Myalgia</td>
      <td>18.8</td>
      <td>(20921/111419)</td>
    </tr>
    <tr>
      <td></td>
      <td>Diarrhoea</td>
      <td>18.2</td>
      <td>(22375/123121)</td>
    </tr>
    <tr>
      <td></td>
      <td>Headache</td>
      <td>12</td>
      <td>(13424/112069)</td>
    </tr>
    <tr>
      <td></td>
      <td>Abdominal pain</td>
      <td>11.1</td>
      <td>(13294/120175)</td>
    </tr>
    <tr>
      <td></td>
      <td>Ageusia</td>
      <td>8.8</td>
      <td>(6758/76396)</td>
    </tr>
    <tr>
      <td></td>
      <td>Wheezing</td>
      <td>7.7</td>
      <td>(8846/115511)</td>
    </tr>
    <tr>
      <td></td>
      <td>Anosmia</td>
      <td>6.8</td>
      <td>(5281/77751)</td>
    </tr>
    <tr>
      <td></td>
      <td>Runny nose</td>
      <td>3.4</td>
      <td>(3704/108623)</td>
    </tr>
    <tr>
      <td></td>
      <td>Ulcers</td>
      <td>2.2</td>
      <td>(2291/105394)</td>
    </tr>
    <tr>
      <td></td>
      <td>Bleeding</td>
      <td>1.8</td>
      <td>(2093/119266)</td>
    </tr>
    <tr>
      <td></td>
      <td>Rash</td>
      <td>1.5</td>
      <td>(1713/113636)</td>
    </tr>
    <tr>
      <td></td>
      <td>Seizures</td>
      <td>1.5</td>
      <td>(1801/120755)</td>
    </tr>
    <tr>
      <td></td>
      <td>Lymphadenopathy</td>
      <td>0.7</td>
      <td>(774/112245)</td>
    </tr>
    <tr>
      <td></td>
      <td>Conjunctivitis</td>
      <td>0.5</td>
      <td>(553/113083)</td>
    </tr>
    <tr>
      <td></td>
      <td>Ear pain</td>
      <td>0.5</td>
      <td>(484/94873)</td>
    </tr>
    <tr>
      <td>Number of recorded ‘common’ symptoms (C)</td>
      <td>0</td>
      <td>7.6</td>
      <td>(10836/142540)</td>
    </tr>
    <tr>
      <td></td>
      <td>1</td>
      <td>20.5</td>
      <td>(29257/142540)</td>
    </tr>
    <tr>
      <td></td>
      <td>2</td>
      <td>26.4</td>
      <td>(37681/142540)</td>
    </tr>
    <tr>
      <td></td>
      <td>3</td>
      <td>29</td>
      <td>(41359/142540)</td>
    </tr>
    <tr>
      <td></td>
      <td>4</td>
      <td>16.4</td>
      <td>(23407/142540)</td>
    </tr>
    <tr>
      <td>Comorbidities</td>
      <td>Hypertension</td>
      <td>47.6</td>
      <td>(50174/105433)</td>
    </tr>
    <tr>
      <td></td>
      <td>Chronic cardiac disease</td>
      <td>29.7</td>
      <td>(38175/128374)</td>
    </tr>
    <tr>
      <td></td>
      <td>Diabetes</td>
      <td>16.8</td>
      <td>(20037/119155)</td>
    </tr>
    <tr>
      <td></td>
      <td>Chronic pulmonary disease</td>
      <td>16.5</td>
      <td>(22040/133662)</td>
    </tr>
    <tr>
      <td></td>
      <td>Chronic kidney disease</td>
      <td>15.7</td>
      <td>(20894/133256)</td>
    </tr>
    <tr>
      <td></td>
      <td>Obesity</td>
      <td>14.4</td>
      <td>(16624/115463)</td>
    </tr>
    <tr>
      <td></td>
      <td>Asthma</td>
      <td>13.2</td>
      <td>(17656/133341)</td>
    </tr>
    <tr>
      <td></td>
      <td>Dementia</td>
      <td>12.9</td>
      <td>(16404/127239)</td>
    </tr>
    <tr>
      <td></td>
      <td>Smoking</td>
      <td>12.8</td>
      <td>(7299/57164)</td>
    </tr>
    <tr>
      <td></td>
      <td>Chronic neurological disorder</td>
      <td>11.5</td>
      <td>(15248/132789)</td>
    </tr>
    <tr>
      <td></td>
      <td>Rheumatological disorder</td>
      <td>11.2</td>
      <td>(13814/123453)</td>
    </tr>
    <tr>
      <td></td>
      <td>Malignant neoplasm</td>
      <td>9.3</td>
      <td>(12343/132537)</td>
    </tr>
    <tr>
      <td></td>
      <td>Chronic haemotologic disease</td>
      <td>4.1</td>
      <td>(5117/123739)</td>
    </tr>
    <tr>
      <td></td>
      <td>Liver disease</td>
      <td>3.5</td>
      <td>(4443/128733)</td>
    </tr>
    <tr>
      <td></td>
      <td>Malnutrition</td>
      <td>2.6</td>
      <td>(3094/119518)</td>
    </tr>
    <tr>
      <td></td>
      <td>HIV/AIDS</td>
      <td>0.4</td>
      <td>(515/119235)</td>
    </tr>
  </tbody>
</table>

A basic summary of the various components of the patient journey that we investigated can be found in Table 3.

**Table 3.**
 Summary of the components of the inpatient journey and their variation over the course of 2020.All time periods are in days. Patients are categorised by month of symptom onset for onset to admission, and by month of COVID admission in all other cases. Patients with COVID admission in 2021, who are included in the analysis of time from onset to admission if their onset date was in 2020, are not listed here as they are excluded from any analysis where the outcome variable is not time from onset to admission. “Outcome” is either death or discharge, and the ‘admission to outcome’ column gives the total length of hospital stay. For all durations, the top 2.5 % of values are excluded as potentially mis-entered.


<table>
  <thead>
    <tr>
      <th>Month</th>
      <th colspan="2">Onset to hospital admission</th>
      <th>Proportion entering ICU/HDU</th>
      <th colspan="2">COVID-19 admission to ICU/HDU</th>
      <th>hCFR</th>
      <th colspan="2">COVID-19 admission to death</th>
      <th colspan="2">COVID-19 admission to discharge</th>
      <th colspan="2">COVID-19 admission to outcome</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>Mean</td>
      <td>SD</td>
      <td></td>
      <td>Mean</td>
      <td>SD</td>
      <td></td>
      <td>Mean</td>
      <td>SD</td>
      <td>Mean</td>
      <td>SD</td>
      <td>Mean</td>
      <td>SD</td>
    </tr>
    <tr>
      <td>March</td>
      <td>6.82</td>
      <td>5.15</td>
      <td>0.25</td>
      <td>1.78</td>
      <td>2.34</td>
      <td>0.33</td>
      <td>11</td>
      <td>8.41</td>
      <td>10.9</td>
      <td>9.71</td>
      <td>10.8</td>
      <td>9.29</td>
    </tr>
    <tr>
      <td>April</td>
      <td>4.27</td>
      <td>4.53</td>
      <td>0.16</td>
      <td>1.63</td>
      <td>2.36</td>
      <td>0.33</td>
      <td>9.1</td>
      <td>7.96</td>
      <td>10.3</td>
      <td>9.14</td>
      <td>9.91</td>
      <td>8.78</td>
    </tr>
    <tr>
      <td>May</td>
      <td>4.09</td>
      <td>4.58</td>
      <td>0.17</td>
      <td>1.45</td>
      <td>2.45</td>
      <td>0.3</td>
      <td>10</td>
      <td>8.41</td>
      <td>11</td>
      <td>9.62</td>
      <td>10.9</td>
      <td>9.28</td>
    </tr>
    <tr>
      <td>June</td>
      <td>4.4</td>
      <td>4.51</td>
      <td>0.3</td>
      <td>1.04</td>
      <td>2.12</td>
      <td>0.27</td>
      <td>10</td>
      <td>8.65</td>
      <td>10.5</td>
      <td>8.83</td>
      <td>10.5</td>
      <td>8.78</td>
    </tr>
    <tr>
      <td>July</td>
      <td>4.77</td>
      <td>4.22</td>
      <td>0.35</td>
      <td>1.1</td>
      <td>2.29</td>
      <td>0.21</td>
      <td>11</td>
      <td>8.68</td>
      <td>9.53</td>
      <td>8.37</td>
      <td>9.88</td>
      <td>8.46</td>
    </tr>
    <tr>
      <td>August</td>
      <td>5.49</td>
      <td>4.6</td>
      <td>0.36</td>
      <td>1.41</td>
      <td>2.49</td>
      <td>0.22</td>
      <td>12</td>
      <td>8.82</td>
      <td>8.88</td>
      <td>7.88</td>
      <td>9.44</td>
      <td>8.16</td>
    </tr>
    <tr>
      <td>September</td>
      <td>6.3</td>
      <td>5.01</td>
      <td>0.24</td>
      <td>1.38</td>
      <td>2.21</td>
      <td>0.22</td>
      <td>14</td>
      <td>9.81</td>
      <td>9.25</td>
      <td>8.64</td>
      <td>10.2</td>
      <td>9.08</td>
    </tr>
    <tr>
      <td>October</td>
      <td>5.72</td>
      <td>4.89</td>
      <td>0.19</td>
      <td>1.69</td>
      <td>2.59</td>
      <td>0.26</td>
      <td>12</td>
      <td>8.69</td>
      <td>9.78</td>
      <td>8.75</td>
      <td>10.5</td>
      <td>8.81</td>
    </tr>
    <tr>
      <td>November</td>
      <td>5.17</td>
      <td>4.75</td>
      <td>0.18</td>
      <td>1.48</td>
      <td>2.49</td>
      <td>0.26</td>
      <td>12</td>
      <td>8.38</td>
      <td>9.1</td>
      <td>8.08</td>
      <td>9.78</td>
      <td>8.24</td>
    </tr>
    <tr>
      <td>December</td>
      <td>4.42</td>
      <td>4.21</td>
      <td>0.22</td>
      <td>1.51</td>
      <td>2.48</td>
      <td>0.29</td>
      <td>11</td>
      <td>8</td>
      <td>9.52</td>
      <td>8.16</td>
      <td>10</td>
      <td>8.15</td>
    </tr>
  </tbody>
</table>

### Time from symptom onset to hospital admission (Question 1)

A total of 11,695 patients (8.2%) were recorded as having symptom onset following hospital admission, while for 8,935 (6.3%) patients this information was missing. After excluding these, we analysed length of illness before hospitalisation for those patients for whom it was recorded (n = 127,915, 89.7%). The 97.5 % quantile of time to admission (ladmission) was 24 days, and patients with recorded durations longer than this were excluded as described above. The median time from symptom onset to admission was 5 days (IQR 1–8). This variable showed a marked decline during March, from a median of 9 days (IQR 5–14) for patients with onset in the week beginning March 1–3 (IQR 0–7) in that beginning April 5. Little further variation occurred until late July, when a gradual increase started, which then peaked at a median of 6 (IQR 2–9) for the weeks in late August and early September before a decline to a low of a median 4 (IQR 1–7) days in November; this was followed by another slight increase in December. Times from onset of symptoms to admission were shortest in the oldest and youngest age groups (Figure 1b). Patients with a fatal outcome had, generally, shorter time from onset of symptoms until admission compared to survivors (Figure 1c).

![Figure 1.](https://cdn.elifesciences.org/articles/70970/elife-70970-fig1-v2.jpg)

**Figure 1.:** (A) Blue cells represent binned patients, with darker colours corresponding to more individuals. The black line represents the mean. (B)-(D) Mean time to admission plotted by patient characteristics: (B) age group, (C) final outcome, (D) number of the four most common symptoms (cough, fatigue, fever, and shortness of breath) present upon admission.

The four most frequent symptoms at admission were cough, fever, shortness of breath, and fatigue; we class these as ‘common’ (see Methods). The number of these that were present increased with time to hospital admission (Figure 1d), with the shortest durations of all occurring amongst those presenting with none of them. Amongst the 4636 patients in this analysis presenting with none, the most common other symptoms were confusion (51.6%), vomiting (31.7%), abdominal pain (26%), and diarrhoea (18.9%). Within this group, confusion was the single most common presenting symptom documented in patients over 60, while in younger age groups the most prevalent symptoms were gastrointestinal (see Supplementary file 3).

We further explored this question using a multivariable linear regression analysis (Supplementary file 4). When compared to April, times from symptom onset to admission were shorter in May and June, and longer in March and from August onwards (all p < 0.01; see Supplementary file 4 for confidence intervals). There was very strong evidence of an overall effect of month of onset on time from onset to admission (Wald test p < 0.001). Patients aged 40–59 showed the longest times to admission when compared to any other age group (all p < 0.001; see Supplementary file 4 for CIs). Time from symptom onset to admission was also positively associated with the number of ‘common’ symptoms (25.1 % increase per symptom, 95% CI 24.5%–25.7%), male sex (3.3 % increase, 95% CI 2.2%–4.4%) and discharge as the final outcome (14.3 % increase, 95% CI 12.9%–15.7%).

### ICU/HDU admission and time to ICU/HDU admission (questions 2 and 3)

Of the 139,504 patients with COVID-19 admission in 2020, 136,849 (98.1%) had recorded data on whether they ever admitted to an ICU/HDU or not; of these, 28,171 (20.6%) had been admitted at least once. Where time to ICU/HDU was recorded, the 97.5 % quantile of this duration (lICU) was 13 days. We excluded patients for whom this variable was greater than that or unknown, along with those whose outcome was unknown and who had follow-up for less than 13 days with no ICU/HDU admission, for a total of 122,368 patients. The outcome variable in this section is thus ICU/HDU admission within 13 days of COVID-19 admission. The proportion of individuals experiencing this showed a marked decline over March followed by a renewed peak, and then subsequent decline, in June through August (Figure 2A). The oldest age group (80+) had by far the smallest proportion of ICU/HDU admissions over the whole timeline (5.2%, compared with, for example, 33.5 % in the age-group 60–69). In a multivariable logistic regression model (Supplementary file 5), the following patterns were observed: there were higher odds of ICU/HDU admission during all months except May and November, when compared to April (all p < 0.05, see Supplementary file 5 for CIs); those aged 80+ had lower odds of ICU/HDU admission (OR 0.12 for admission when compared to the 40–59 age group, 95% CI 0.11–0.13). Males were more likely to be admitted to ICU/HDU (OR 1.57, 95% CI 1.45–1.63). Patients who died had greatly increased odds of having been previously admitted (OR 6.1, 95% CI 5.8–6.41). Compared to those with symptom onset less than a week before hospital admission, patients with admitted prior to onset had lower odds of being admitted to ICU/HDU (OR 0.32, 95% CI 0.28–0.36), whereas those with longer times to hospital admission had increased odds (OR 1.43 for 7–13 days, 95% CI 1.37–1.5, 1.31 for 14 or more days, 95% CI 1.22–1.4). An overall effect of month of COVID admission on odds of ICU/HDU admission was highly significant (Wald test p < 0.0001). Comorbidities associated with higher odds of admission were hypertension (OR 1.27, 95% CI 1.21–1.34) and obesity (OR 1.78, 95% CI 1.69–1.88), whereas a wide variety of serious or chronic medical conditions were associated with lower odds (see Supplementary file 5), as was smoking (OR 0.79, 95% CI 0.72–0.87). The most extreme fitted odds ratio for a comorbidity with a positive association was 1.78 for obesity, while that for an inverse association was 0.19 for dementia.

![Figure 2.](https://cdn.elifesciences.org/articles/70970/elife-70970-fig2-v2.jpg)

**Figure 2.:** Each line is the proportion (A) or mean value (B) amongst all patients (black, dotted) or patients in each age group (coloured).

Of the 28,171 patients with recorded ICU/HDU admission, 27,167 (96.4%) had non-missing data for time from COVID-19 admission to first ICU/HDU admission. The 97.5 % quantile rule again excluded patients whose value of this variable was greater than 13 days. The median time to ICU/HDU was 1 day (IQR 0–2). Raw time trends in this variable were modest (Figure 2B). Multivariable linear regression (Supplementary file 6) nevertheless did show evidence for an overall association with month of COVID-19 admission (Wald test p < 0.001), with, when compared to April, evidence for longer times to ICU/HDU in March, October, November and December (all p < 0.05; see Supplementary file 6). Time to ICU/HDU also showed a general increase with age (Wald test for overall association p < 0.001). There was no evidence of an association with final outcome (death or discharge) or with sex. Compared to patients admitted to hospital within a week of symptom onset, those admitted prior to onset had a 67.6 % increase in time to ICU/HDU (95% CI 55.9–80.2%) while those with longer times to admission had shorter times to ICU/HDU (8.6 % decrease for 7–13 days, 95% CI 6.6–10.6%, 14.9 % decrease for 14 or more days, 95% CI 11.9–17.8%). Comorbidities associated with longer time to ICU/HDU were asthma (6.5 % increase, 95% CI 3.3–9.7%), chronic haematological disease (20.4 % increase, 95% CI 12.6–28.8%), and chronic kidney disease (9.9 % increase, 95% CI 6–14.1%). In contrast, obesity (7.7 % decrease, 95% CI 5.2–10%), diabetes (3.7 % decrease, 95% CI 0.9–6.3%) and smoking (5.2 % decrease, 95% CI 0.4–9.8%) were associated with shorter time to ICU. There was also evidence of a longer time to ICU/HDU amongst pregnant patients (compared to non-pregnant females) (15.6%, 95% CI 1.7–31.4%).

### Case fatality rate and time from COVID-19 admission to outcome (questions 4 and 5)

We next analysed the final outcome of death or discharge, and the total time from hospital admission to one of those outcomes, in a set of 116,537 patients admitted during 2020 with one of those outcomes recorded (83.5 % of the total admitted during 2020). The 97.5 % quantile of time to outcome (loutcome) was 45 days, and once more patients with recorded durations in hospital longer than this were excluded; as a result, in practice the outcome here is death or discharge within 45 days. (As patient data was collected until 8 March 2021 and all patients here were admitted in 2020, patients admitted at the end of the period of interest had the same chance of complete follow-up as any other.) The raw hCFR was 0.3. The median time to death was 8 days (IQR 4–15) and to discharge 7 (IQR 4–14). (Amongst patients with no recorded outcome, excluded here, the median follow-up time was 9 days with an IQR of 2–22; the median follow-up for all patients regardless of outcome, recorded or not, was also 9 days with an IQR of 5–16). Over the entire 10-month period of interest (Figure 3—figure supplement 1), peak hCFR was 0.35 in the week beginning 8 March. There was a decline over the spring to a low of 0.17 in the week beginning 12 July, but this trend subsequently reversed and reached 0.32 by mid-December. At the same time, the mean time from admission to outcome in this whole population showed very little change following a dramatic decline during March, from 16 days in the week beginning 1 March to 10 at the start of April (Figure 3—figure supplement 2). These overall patterns, however, mask substantial variation by on ICU/HDU admission and, in the latter case, outcome (Figure 3). The trend in hCFR is largely driven by patients who were not admitted to an ICU or HDU. The most consistent decline in time to outcome was observed in ICU/HDU admissions who survived (a decline in the mean of 7.6 days between the first and last weeks studied, Figure 3B, bottom left) while survivors with no ICU/HDU admission showed, as with the overall trend, little change after March (bottom right). Variation in time to death appeared very modest amongst patients with an ICU/HDU admission (top left), while there was a distinct peak around August and September in those without (top right). When age is also considered (Figure 3—figure supplements 3 and 4), a notable additional pattern is the clear correlation of time to discharge and age in surviving non-ICU/HDU patients, which is much less obvious, if present at all, in patients with an ICU/HDU admission.

![Figure 3.](https://cdn.elifesciences.org/articles/70970/elife-70970-fig3-v2.jpg)

**Figure 3.:** (A) Case fatality ratio in patients experiencing death or discharge within 45 days of COVID-19 admission, by recorded ICU/HDU admission. (B) Mean time from COVID-19 admission to the outcome of death or discharge, further faceted by ICU/HDU admission. Error bars represent 95 % confidence intervals. Numbers along the x-axis indicate the numbers of patients involved in each category.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/70970/elife-70970-fig3-figsupp1-v2.jpg)

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/70970/elife-70970-fig3-figsupp2-v2.jpg)

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/70970/elife-70970-fig3-figsupp3-v2.jpg)

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/70970/elife-70970-fig3-figsupp4-v2.jpg)

The results of the three multivariable regression analyses can be seen in Table 4; some variables (country and the ‘unknown’ class for comorbidities) are excluded for brevity, but the full version is provided as Supplementary file 7. Note that all variables are adjusted for all others, which is also the case for all the other regressions presented in this paper. There was strong evidence of an association of month of COVID-19 admission with all three variables (Wald test p < 0.001 in all cases).

**Table 4.**
 Combined results of a logistic regression analysis identifying predictors of death as an outcome, and two linear regression analyses identifying correlates of time to death and time to discharge.All analyses are multivariable. For brevity, the country variable, as well as the ‘unknown’ class for each comorbidity (representing patients with missing data for that condition) are omitted here; see Supplementary file 7 for a version with them included. The p-values of Wald tests for the inclusion of each variable in each regression are included as a separate column; these were calculated including the ‘unknown’ class for comorbidities.


<table>
  <thead>
    <tr>
      <th rowspan="2"></th>
      <th colspan="3">Odds ratio (death v discharge)</th>
      <th colspan="3">Time to death (% change, days)</th>
      <th colspan="3">Time to discharge (% change, days)</th>
    </tr>
    <tr>
      <th>Estimate</th>
      <th>95 % confidence interval</th>
      <th>Wald test p-value</th>
      <th>Estimate</th>
      <th>95 % confidence interval</th>
      <th>Wald test p-value</th>
      <th>Estimate</th>
      <th>95 % confidence interval</th>
      <th>Wald test p-value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Month of COVID admission (ref: April)</td>
      <td></td>
      <td></td>
      <td>&lt; 0.001</td>
      <td></td>
      <td></td>
      <td>&lt; 0.001</td>
      <td></td>
      <td></td>
      <td>&lt; 0.001</td>
    </tr>
    <tr>
      <td>March</td>
      <td>1.1</td>
      <td>(1.1, 1.2)</td>
      <td></td>
      <td>14.7</td>
      <td>(12.2, 17.3)</td>
      <td></td>
      <td>3.7</td>
      <td>(2.1, 5.2)</td>
      <td></td>
    </tr>
    <tr>
      <td>May</td>
      <td>0.7</td>
      <td>(0.7, 0.8)</td>
      <td></td>
      <td>15.5</td>
      <td>(12.1, 19.1)</td>
      <td></td>
      <td>1.3</td>
      <td>(–0.6, 3.3)</td>
      <td></td>
    </tr>
    <tr>
      <td>June</td>
      <td>0.5</td>
      <td>(0.5, 0.6)</td>
      <td></td>
      <td>20.8</td>
      <td>(14.2, 27.7)</td>
      <td></td>
      <td>–2.8</td>
      <td>(−5.6,–0.02)</td>
      <td></td>
    </tr>
    <tr>
      <td>July</td>
      <td>0.3</td>
      <td>(0.3, 0.4)</td>
      <td></td>
      <td>28.1</td>
      <td>(14.9, 42.8)</td>
      <td></td>
      <td>–8.5</td>
      <td colspan="2">(−12.2,–4.7)</td>
    </tr>
    <tr>
      <td>August</td>
      <td>0.4</td>
      <td>(0.3, 0.5)</td>
      <td></td>
      <td>47.2</td>
      <td>(29.5, 67.3)</td>
      <td></td>
      <td>–10.8</td>
      <td colspan="2">(−15.0,–6.4)</td>
    </tr>
    <tr>
      <td>September</td>
      <td>0.6</td>
      <td>(0.5, 0.6)</td>
      <td></td>
      <td>40.7</td>
      <td>(32.6, 49.3)</td>
      <td></td>
      <td>–3.2</td>
      <td>(−5.8,–0.5)</td>
      <td></td>
    </tr>
    <tr>
      <td>October</td>
      <td>0.6</td>
      <td>(0.6, 0.7)</td>
      <td></td>
      <td>33.2</td>
      <td>(28.9, 37.7)</td>
      <td></td>
      <td>–1.4</td>
      <td>(–3.2, 0.4)</td>
      <td></td>
    </tr>
    <tr>
      <td>November</td>
      <td>0.6</td>
      <td>(0.6, 0.7)</td>
      <td></td>
      <td>26.7</td>
      <td>(22.8, 30.8)</td>
      <td></td>
      <td>–3.5</td>
      <td>(−5.2,–1.8)</td>
      <td></td>
    </tr>
    <tr>
      <td>December</td>
      <td>0.8</td>
      <td>(0.8, 0.9)</td>
      <td></td>
      <td>26.3</td>
      <td>(22.3, 30.4)</td>
      <td></td>
      <td>2.2</td>
      <td>(0.2, 4.2)</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Age group (ref: 40–59)</td>
      <td></td>
      <td></td>
      <td>&lt; 0.001</td>
      <td></td>
      <td></td>
      <td>&lt; 0.001</td>
      <td></td>
      <td></td>
      <td>&lt; 0.001</td>
    </tr>
    <tr>
      <td>10–19</td>
      <td>0.3</td>
      <td>(0.2, 0.4)</td>
      <td></td>
      <td>–0.5</td>
      <td colspan="2">(–24.3, 30.6)</td>
      <td>–33.6</td>
      <td colspan="2">(−35.7,–31.4)</td>
    </tr>
    <tr>
      <td>20–39</td>
      <td>0.3</td>
      <td>(0.2, 0.3)</td>
      <td></td>
      <td>–1.7</td>
      <td colspan="2">(–15.9, 14.8)</td>
      <td>–16.9</td>
      <td colspan="2">(−18.5,–15.3)</td>
    </tr>
    <tr>
      <td>60–69</td>
      <td>2.9</td>
      <td>(2.7, 3.2)</td>
      <td></td>
      <td>–2.1</td>
      <td>(–6.8, 3.0)</td>
      <td></td>
      <td>17.4</td>
      <td colspan="2">(15.6, 19.2)</td>
    </tr>
    <tr>
      <td>70–79</td>
      <td>6.1</td>
      <td>(5.7, 6.6)</td>
      <td></td>
      <td>1.9</td>
      <td>(–2.6, 6.6)</td>
      <td></td>
      <td>36.4</td>
      <td colspan="2">(34.3, 38.6)</td>
    </tr>
    <tr>
      <td>80+</td>
      <td>10.9</td>
      <td>(10.1, 11.8)</td>
      <td></td>
      <td>4.3</td>
      <td>(–0.3, 9.0)</td>
      <td></td>
      <td>52.9</td>
      <td colspan="2">(50.4, 55.4)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>ICU/HDU admission</td>
      <td>7.6</td>
      <td>(6.8, 8.4)</td>
      <td>&lt; 0.001</td>
      <td>68.3</td>
      <td>(59.1, 78.0)</td>
      <td>&lt; 0.001</td>
      <td>140.1</td>
      <td>(133.0, 147.3)</td>
      <td>&lt; 0.001</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Sex (ref: female)</td>
      <td></td>
      <td></td>
      <td>&lt; 0.001</td>
      <td></td>
      <td></td>
      <td>&lt; 0.001</td>
      <td></td>
      <td></td>
      <td>0.0059</td>
    </tr>
    <tr>
      <td>Male</td>
      <td>1.3</td>
      <td>(1.3, 1.4)</td>
      <td></td>
      <td>2.9</td>
      <td>(1.4, 4.5)</td>
      <td></td>
      <td>1.2</td>
      <td>(0.2, 2.1)</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="2">Pregnant (ref: female, no)</td>
      <td></td>
      <td>0.097</td>
      <td></td>
      <td></td>
      <td>0.069</td>
      <td></td>
      <td></td>
      <td>&lt; 0.001</td>
    </tr>
    <tr>
      <td>Female, yes</td>
      <td>0.6</td>
      <td>(0.4, 1.0)</td>
      <td></td>
      <td>–5.4</td>
      <td colspan="2">(–27.4, 23.3)</td>
      <td>–18.6</td>
      <td colspan="2">(−22.3,–14.6)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Days from symptom onset to hospital admission (ref: 0–6)</td>
      <td></td>
      <td></td>
      <td>&lt; 0.001</td>
      <td></td>
      <td></td>
      <td>&lt; 0.001</td>
      <td></td>
      <td></td>
      <td>&lt; 0.001</td>
    </tr>
    <tr>
      <td>Symptom onset post-admission</td>
      <td>1.3</td>
      <td>(1.2, 1.3)</td>
      <td></td>
      <td>20.7</td>
      <td>(17.9, 23.5)</td>
      <td></td>
      <td>45.7</td>
      <td colspan="2">(42.9, 48.6)</td>
    </tr>
    <tr>
      <td>7–13</td>
      <td>0.7</td>
      <td>(0.7, 0.8)</td>
      <td></td>
      <td>–1.7</td>
      <td>(–3.5, 0.1)</td>
      <td></td>
      <td>–3.6</td>
      <td>(−4.6,–2.5)</td>
      <td></td>
    </tr>
    <tr>
      <td>14+</td>
      <td>0.7</td>
      <td>(0.7, 0.8)</td>
      <td></td>
      <td>–0.2</td>
      <td>(–2.9, 2.5)</td>
      <td></td>
      <td>–6.1</td>
      <td>(−7.6,–4.5)</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="2">Comorbidities</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Asthma</td>
      <td>0.9</td>
      <td>(0.9, 1.0)</td>
      <td>&lt; 0.001</td>
      <td>2.5</td>
      <td>(0.2, 4.9)</td>
      <td>0.11</td>
      <td>–1.6</td>
      <td>(−2.9,–0.3)</td>
      <td>0.048</td>
    </tr>
    <tr>
      <td>Chronic cardiac disease</td>
      <td>1.2</td>
      <td>(1.2, 1.3)</td>
      <td>&lt; 0.001</td>
      <td>–2.8</td>
      <td>(−4.4,–1.3)</td>
      <td>&lt; 0.001</td>
      <td>1.3</td>
      <td>(0.1, 2.6)</td>
      <td>0.075</td>
    </tr>
    <tr>
      <td>Chronic haemotologic disease</td>
      <td>1.2</td>
      <td>(1.1, 1.3)</td>
      <td>&lt; 0.001</td>
      <td>0.2</td>
      <td>(–3.1, 3.6)</td>
      <td>0.62</td>
      <td>5.8</td>
      <td>(3.1, 8.6)</td>
      <td>&lt; 0.001</td>
    </tr>
    <tr>
      <td>Chronic kidney disease</td>
      <td>1.4</td>
      <td>(1.4, 1.5)</td>
      <td>&lt; 0.001</td>
      <td>–2.4</td>
      <td>(−4.1,–0.6)</td>
      <td>0.012</td>
      <td>5.8</td>
      <td>(4.2, 7.4)</td>
      <td>&lt; 0.001</td>
    </tr>
    <tr>
      <td>Chronic neurological disorder</td>
      <td>1.4</td>
      <td>(1.3, 1.4)</td>
      <td>&lt; 0.001</td>
      <td>–0.7</td>
      <td>(–2.7, 1.4)</td>
      <td>0.61</td>
      <td>15.3</td>
      <td>(13.4, 17.2)</td>
      <td>&lt; 0.001</td>
    </tr>
    <tr>
      <td>Chronic pulmonary disease</td>
      <td>1.4</td>
      <td>(1.3, 1.4)</td>
      <td>&lt; 0.001</td>
      <td>–2.2</td>
      <td>(−3.9,–0.5)</td>
      <td>0.034</td>
      <td>3.9</td>
      <td>(2.4, 5.3)</td>
      <td>&lt; 0.001</td>
    </tr>
    <tr>
      <td>Dementia</td>
      <td>1.5</td>
      <td>(1.4, 1.6)</td>
      <td>&lt; 0.001</td>
      <td>–1.2</td>
      <td>(–3.1, 0.8)</td>
      <td>0.43</td>
      <td>9</td>
      <td>(7.0, 11.0)</td>
      <td>&lt; 0.001</td>
    </tr>
    <tr>
      <td>Diabetes</td>
      <td>1.1</td>
      <td>(1.1, 1.2)</td>
      <td>&lt; 0.001</td>
      <td>–4.2</td>
      <td>(−6.0,–2.3)</td>
      <td>&lt; 0.001</td>
      <td>1.8</td>
      <td>(0.4, 3.2)</td>
      <td>&lt; 0.001</td>
    </tr>
    <tr>
      <td>HIV/AIDS</td>
      <td>1.2</td>
      <td>(1.0, 1.6)</td>
      <td>0.005</td>
      <td>4</td>
      <td>(–8.2, 17.8)</td>
      <td>0.58</td>
      <td>2.2</td>
      <td>(–5.1, 10.1)</td>
      <td>0.0025</td>
    </tr>
    <tr>
      <td>Hypertension</td>
      <td>1</td>
      <td>(0.9, 1.0)</td>
      <td>&lt; 0.001</td>
      <td>0.2</td>
      <td>(–1.5, 1.9)</td>
      <td>0.14</td>
      <td>2</td>
      <td>(0.8, 3.2)</td>
      <td>&lt; 0.001</td>
    </tr>
    <tr>
      <td>Liver disease</td>
      <td>1.4</td>
      <td>(1.3, 1.6)</td>
      <td>&lt; 0.001</td>
      <td>5.2</td>
      <td>(1.1, 9.5)</td>
      <td>&lt; 0.001</td>
      <td>12</td>
      <td>(9.0, 15.1)</td>
      <td>&lt; 0.001</td>
    </tr>
    <tr>
      <td>Malignant neoplasm</td>
      <td>1.4</td>
      <td>(1.4, 1.5)</td>
      <td>&lt; 0.001</td>
      <td>3.5</td>
      <td>(1.2, 5.8)</td>
      <td>0.0059</td>
      <td>2.2</td>
      <td>(0.3, 4.1)</td>
      <td>&lt; 0.001</td>
    </tr>
    <tr>
      <td>Malnutrition</td>
      <td>1.3</td>
      <td>(1.2, 1.5)</td>
      <td>&lt; 0.001</td>
      <td>0.6</td>
      <td>(–3.6, 5.0)</td>
      <td>0.81</td>
      <td>11.5</td>
      <td>(7.5, 15.7)</td>
      <td>&lt; 0.001</td>
    </tr>
    <tr>
      <td>Obesity</td>
      <td>1.1</td>
      <td>(1.1, 1.2)</td>
      <td>&lt; 0.001</td>
      <td>–5.5</td>
      <td>(−7.7,–3.2)</td>
      <td>&lt; 0.001</td>
      <td>6.3</td>
      <td>(4.8, 7.9)</td>
      <td>&lt; 0.001</td>
    </tr>
    <tr>
      <td>Rheumatological disorder</td>
      <td>1</td>
      <td>(0.9, 1.0)</td>
      <td>0.045</td>
      <td>2.3</td>
      <td>(0.1, 4.7)</td>
      <td>0.052</td>
      <td>0.6</td>
      <td>(–1.0, 2.2)</td>
      <td>0.44</td>
    </tr>
    <tr>
      <td>Smoking</td>
      <td>1.1</td>
      <td>(1.1, 1.2)</td>
      <td>&lt; 0.001</td>
      <td>4.2</td>
      <td>(0.5, 8.0)</td>
      <td>0.1</td>
      <td>2.2</td>
      <td>(0.04, 4.4)</td>
      <td>0.034</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Interaction: ICU/HDU admission _ month of admission (ref: April)</td>
      <td></td>
      <td></td>
      <td>&lt; 0.001</td>
      <td></td>
      <td></td>
      <td>&lt; 0.001</td>
      <td></td>
      <td></td>
      <td>&lt; 0.001</td>
    </tr>
    <tr>
      <td>March</td>
      <td>1</td>
      <td>(0.9, 1.1)</td>
      <td></td>
      <td>–14.3</td>
      <td colspan="2">(−18.1,–10.4)</td>
      <td>0.6</td>
      <td>(–3.1, 4.5)</td>
      <td></td>
    </tr>
    <tr>
      <td>May</td>
      <td>1.1</td>
      <td>(0.9, 1.3)</td>
      <td></td>
      <td>–12</td>
      <td colspan="2">(−17.6,–6.1)</td>
      <td>-9</td>
      <td colspan="2">(−13.9,–3.9)</td>
    </tr>
    <tr>
      <td>June</td>
      <td>1.2</td>
      <td>(1.0, 1.5)</td>
      <td></td>
      <td>–9.1</td>
      <td colspan="2">(−16.8,–0.8)</td>
      <td>–11.3</td>
      <td colspan="2">(−17.1,–5.1)</td>
    </tr>
    <tr>
      <td>July</td>
      <td>1.4</td>
      <td>(1.1, 1.9)</td>
      <td></td>
      <td>–14.8</td>
      <td colspan="2">(−25.8,–2.1)</td>
      <td>–18.8</td>
      <td colspan="2">(−25.2,–11.8)</td>
    </tr>
    <tr>
      <td>August</td>
      <td>1.1</td>
      <td>(0.8, 1.6)</td>
      <td></td>
      <td>–27.9</td>
      <td colspan="2">(−38.4,–15.6)</td>
      <td>–15.6</td>
      <td colspan="2">(−23.2,–7.3)</td>
    </tr>
    <tr>
      <td>September</td>
      <td>1.1</td>
      <td>(0.9, 1.4)</td>
      <td></td>
      <td>–16.6</td>
      <td colspan="2">(−24.1,–8.4)</td>
      <td>–6.9</td>
      <td colspan="2">(−13.0,–0.3)</td>
    </tr>
    <tr>
      <td>October</td>
      <td>1.1</td>
      <td>(1.0, 1.3)</td>
      <td></td>
      <td>–13.7</td>
      <td colspan="2">(−18.9,–8.2)</td>
      <td>–11.6</td>
      <td colspan="2">(−15.9,–7.0)</td>
    </tr>
    <tr>
      <td>November</td>
      <td>1.1</td>
      <td>(1.0, 1.3)</td>
      <td></td>
      <td>–6.6</td>
      <td colspan="2">(−12.1,–0.7)</td>
      <td>–15.9</td>
      <td colspan="2">(−20.0,–11.6)</td>
    </tr>
    <tr>
      <td>December</td>
      <td>0.8</td>
      <td>(0.7, 0.9)</td>
      <td></td>
      <td>–11.6</td>
      <td colspan="2">(−17.0,–5.8)</td>
      <td>–27.9</td>
      <td colspan="2">(−31.4,–24.2)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Interaction: ICU/HDU admission _ age group (ref: 40–59)</td>
      <td></td>
      <td></td>
      <td>&lt; 0.001</td>
      <td></td>
      <td></td>
      <td>&lt; 0.001</td>
      <td></td>
      <td></td>
      <td>&lt; 0.00</td>
    </tr>
    <tr>
      <td>10–19</td>
      <td>0.8</td>
      <td>(0.4, 1.4)</td>
      <td></td>
      <td>–42.8</td>
      <td colspan="2">(−59.3,–19.6)</td>
      <td>1.7</td>
      <td>(–6.0, 10.2)</td>
      <td></td>
    </tr>
    <tr>
      <td>20–39</td>
      <td>1.8</td>
      <td>(1.4, 2.4)</td>
      <td></td>
      <td>–11.8</td>
      <td>(–25.9, 4.9)</td>
      <td></td>
      <td>0.8</td>
      <td>(–3.6, 5.4)</td>
      <td></td>
    </tr>
    <tr>
      <td>60–69</td>
      <td>0.7</td>
      <td>(0.7, 0.8)</td>
      <td></td>
      <td>2.5</td>
      <td>(–3.7, 9.0)</td>
      <td></td>
      <td>–7.2</td>
      <td colspan="2">(−10.4,–3.9)</td>
    </tr>
    <tr>
      <td>70–79</td>
      <td>0.6</td>
      <td>(0.5, 0.7)</td>
      <td></td>
      <td>–11.8</td>
      <td colspan="2">(−16.8,–6.6)</td>
      <td>–21.8</td>
      <td colspan="2">(−24.9,–18.5)</td>
    </tr>
    <tr>
      <td>80+</td>
      <td>0.4</td>
      <td>(0.3, 0.5)</td>
      <td></td>
      <td>–28.4</td>
      <td colspan="2">(−32.9,–23.6)</td>
      <td>–40.1</td>
      <td colspan="2">(−43.6,–36.4)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Observations</td>
      <td>102,147</td>
      <td></td>
      <td></td>
      <td>31,250</td>
      <td></td>
      <td></td>
      <td>70,897</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

Amongst non-ICU/HDU patients, the month with the greatest odds of death was March (OR 1.12 compared to April, 95% CI 1.07–1.17), while that with the smallest was July (OR 0.35, 95% CI 0.29–0.43). April (the reference category) was the month with the shortest time to death, while August had the longest (54.2 % increase, 95% CI 32.9–78.8%). Variation in time to discharge was more modest; the month with the largest value of this variable was March (3.7 % increase, 95% CI 1.9–5.5%), and that with the shortest was August (12.3 % decrease, 95% CI 7.2–17.1%).

ICU/HDU admission was associated with a 7.56-fold higher odds of death (95% CI 6.81–8.4), a 81.8 % increase in time to death (95% CI 70.3–94.2%) and a 171.6 % increase in time to discharge (95% CI 162.3–181.3%). As a result of the patterns observed in Figure 3, we also fitted interaction terms of month of COVID-19 admission with IDU/HCU admission. Their inclusion was consistently statistically significant (Wald test p < 0.001 in all cases), although for odds of death this ceases to be true when December is removed (p = 0.23). Hence, the overall increased odds of death amongst ICU/HDU patients was significantly mitigated in December (combined OR 6.07 vs non-ICU/HDU admissions in December, 95% CI 5.23–7.06). There was no evidence that ICU/HDU patients admitted in March, May, or August had a longer time to death than April, but the estimates for all other months were significantly greater, with the peak in November (21.5 % increase, 95% CI 15.1–28.2%). The longest times to discharge in these patients were in March (4.2 % increase vs April, 95% CI 0.8–7.8%) and the shortest in December (28.1 % decrease, 95% CI 24–32%).

Increasing age was associated with monotonic increases in odds of death and time to discharge, with and without ICU/HDU admission. Time to death showed little evidence of variation by age in non-ICU/HDU patients except for marginal evidence for an increase in the oldest age group (5.7 % increase vs 40–59, 95% CI 0.3–11.2%). In ICU/HDU patients, however, where an interaction term was again fitted, the shortest times to death were recorded in both the youngest (49.2% decrease, 95% CI 35.8–59.9%) and oldest (27.6 % decrease, 95% CI 24.2–30.9%) groups; longest times to death were in middle-aged adults (40-69). Male sex was associated with higher odds of death (OR 1.33, 95% CI 1.29–1.38), and small increases in time to both death (3.4 % increase, 95% CI 1.7–5.2%) and discharge (1.6 % increase, 95% CI 0.5–2.7%). Symptom onset following admission was also associated with higher odds of death (OR 1.28, 95% CI 1.21–1.35) and large increases in time to death (24.4 % increase, 21.1–27.8%) and discharge (53.2 % increase, 95% CI 49.7–56.7%). Patients admitted more than a week from symptom onset had lower odds of death, and shorter stays in hospital, regardless of outcome (see Table 4). Where associations with comorbidities were detected, the majority were in the direction of poorer outcomes (increased hCFR, decreased time to death, and increased time to discharge), with a few exceptions. Most notably, asthma was associated with lower odds of death (OR 0.93, 95% CI 0.88–0.97), longer times to death (2.9 % increase, CI 0.2–5.6%) and shorter times to discharge (1.9 % decrease, 95% CI 0.3–3.4%).

To further illustrate these findings, Figure 4 displays time trends in model predictions for hCFR, time to death and time to discharge for typical patients of both sexes in every age group, both for those with disease serious enough to trigger ICU/HDU admission and those without. These patients were assumed to be admitted in the UK after less than a week of symptoms. Each was assigned the median number of comorbidities for their combination of sex and age group in the real dataset, and the exact comorbidities chosen were also the most common in that demographic group; see inset table, Figure 4. (For example, males in the 60–69 age group had a median of two comorbidities recorded, and the two most common were hypertension and chronic cardiac disease.)

![Figure 4.](https://cdn.elifesciences.org/articles/70970/elife-70970-fig4-v2.jpg)

**Figure 4.:** Lines are plotted by month of COVID-19 admission (y-axis), age group (facets, left to right), sex (red: female, blue: male), and ICU admission (solid lines: at least once, dotted lines: never). The inset table (D) lists the comorbidities assigned to the individuals in each combination of sex and age group.

### Status by days since admission

Figure 5 displays Sankey diagrams reflecting the location of patients within hospital (ward or ICU) or their final status (dead, discharged, or unknown) on the day of COVID-19 admission (A), 3 days later (A + 3), 7 days later (A + 7) or, to represent the final status only, 1 day after the last day in hospital (O + 1). The plot is facetted by age group and month of COVID-19 admission. For simplicity, only four months (April, June, August and October) appear in the main figure, but see Figure 5—figure supplement 1 for all months, featuring a total of 129,044 patients (90.5%).

![Figure 5.](https://cdn.elifesciences.org/articles/70970/elife-70970-fig5-v2.jpg)

**Figure 5.:** Bars are presented for the day of admission (A), 3 and 7 days later (A + 3 and A + 7), and the day after final outcome (O + 1).

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/70970/elife-70970-fig5-figsupp1-v2.jpg)

## Discussion

To the best of our knowledge and at the time of publication, this is the largest international cohort of COVID-19 patients in the world. Considerable temporal variations in the events preceding and during hospitalisation for patients with confirmed COVID-19 were observed during the period March to December 2020. We specifically looked at length of illness before admission, probability of ICU/HDU admission, time to ICU/HDU admission for those so admitted, case fatality rate, and duration of admission overall.

These results highlight key findings with practical implications for case management, resource allocation, performance benchmarking, and reporting of outcomes in research, and point to the fact that patients’ journeys vary over time and must be interpreted with the background of transmission intensity, policy, and practice where cases occur. Therefore, static ‘snapshots’ of the situation at any one time may lead to misguided practice and management if not regularly monitored and approaches adapted accordingly.

In a recent preprint (Kirwan et al., 2021), analysed temporal variation on time from hospital admission to death, discharge or ICU/HDU admission amongst a smaller cohort of UK patients. We confirm many of the trends that they identified, including the lower hCFRs over the summer and the increased odds of ICU/HDU admission in middle-aged age groups. They did not, however, detect the increase in the proportion of patients with an ICU/HDU admission during the summer, or the decline in time to discharge amongst non-ICU/HDU patients over the entire time period. As there were many fewer hospitals included in that study than in ours (31 vs 620) this may be suggestive of variation in available ICU/HDU capacity and usage amongst participating sites in the two studies.

### Prior to admission

Across all age groups, the length of illness before seeking hospital care was longest in July and August when case numbers were lower, and shortest at the extremities of the age distribution and for females. The latter variations may, at least partially, be explained by differences in health-care-seeking behaviour by different demographics, and by differences in clinical progression of disease for different groups. Along similar lines, the fact that patients who died had consistently shorter duration of illness before hospital admission may reflects the fact that more serious cases evolve more rapidly and those affected seek care earlier. In this scenario, patients admitted after experiencing symptoms for longer than 1 week would be less likely to die because they were less serious cases and the individuals acted accordingly. The peak in time to admission during late summer and early autumn in the Northern Hemisphere may reflect delayed presentation following return from holiday, particularly given the high proportion of UK patients in this dataset and known viral importations to the UK from continental Europe around that time (Hodcroft et al., 2021).

At the same time, when considering the four most frequent symptoms at admission (fever, short of breath, cough, or fatigue), more symptoms were associated with a longer period between onset of symptoms and admission – and this was consistently so across the entire period under observation. This could be ascribed at least in part to variations in individual behaviour; some patients may present to hospital with a single symptom while others may wait a longer period until several have emerged. In addition, these phenomena could also partially be attributed to how case definitions are applied by physicians, or to the patient’s own perceptions, or to those of their families. Some presentations are likely to be more alarming to the latter two groups than others; for example, individuals with none of the four symptoms described above were admitted fastest of all and, amongst these, confusion was the most prevalent other symptom.

### During hospitalisation

Treating variables such as final outcome, ICU/HDU admission, or length of stay, as variables that remain static throughout an evolving epidemic is problematic, as demonstrated by our analyses. To give three examples: first, the case fatality rate showed an overall decline from 0.35 for cases admitted in March to 0.21 in July, followed by a renewed increase to 0.29 in December (Figure 3—figure supplement 1). Second, the data underlying the alluvial plots (Figure 5) allow us to determine that the proportion of patients discharged within a week of admission rose from 0.24 in March to a peak of 0.34 in September. Third, the proportion of still-admitted patients occupying an ICU/HDU bed showed considerable variation: for example, at day three this went from 0.19 in March to 0.13 in April, then rose to a peak of 0.38 in August before declining again, reaching a low of 0.15 in November. Variations in clinical care, the influence of treatments, and changes in available bed capacity are all likely to account for many of these differences. In older patients, the availability of social care space is another important variable.

Patients older than 80 had odds of being admitted to ICU/HDU over eight times smaller than those in the 40–59 category, which may reflect prognosis and the expected benefits of ICU/HDU admission, as well as patient preferences. Many serious chronic conditions were also associated with decreased odds, independently of age, likely for similar reasons. These decreased odds are also reflective of the temporality of the data. March and April represent our data’s highest volume, which might reflect hospital capacity and the necessity for ICU/HDU prioritisation. For the patients who were admitted to ICU/HDU, there was no clear trend in the time from hospital admission to transfer to ICU/HDU after March. Length of illness before admission to the hospital and young age were associated with a shorter time from hospital admission to ICU/HDU (for example, a 9.2 % decrease for those waiting 7–13 days from onset compared to those waiting less than a week, and 32 % decrease amongst under-20s compared to the 40–59 age group), while a smaller proportion of older patients are escalated to ICU/HDU (OR 0.51 for ICU/HDU admission in the 70–79 age group) and after a longer time spent in the ward (a 4.2 % increase in the same age group).

### Outcome

As mentioned above, in patients with an outcome of death or discharge, hCFRs decreased from 0.35 in March to 0.21 by mid-2020 to increase again to 0.29 in December, mostly following the waves in the pandemic and therefore the number of admissions. System capacity may be an important predictor of patient outcome and may supersede other factors such as increasing case management skills and the influence of new therapies. This also warns against using outcome data that are not adequately controlled to assess efficacy and safety of treatments or other interventions, as effects may rather reflect capacity of a system to provide high-quality care.

We found that shorter time to death is associated with female sex, lack of ICU/HDU admission, and, amongst ICU/HDU patients, the extremes of age. Shorter time to discharge is also associated with female sex and lack of ICU/HDU admission, and this variable increases monotonically with age.

The finding of an association of asthma with reduced disease severity in COVID-19 is not unique to this study (Alberca et al., 2021; Matsumoto and Saito, 2020), but is also not a universal finding (Choi et al., 2021a; Choi et al., 2021b). A number of possible mechanisms for a protective effect have been suggested, including reduced ACE2 expression in the airway (Jackson et al., 2020), eosinophilia (Ferastraoaru et al., 2021), or simply the existing use of beneficial corticosteroids in this population (Halpin et al., 2020).

Cautionary notes in interpreting these findings. First, the dataset analysed is made of patients on the more severe end of the spectrum of disease compared to cases occurring in the community. Second, about half of these patients were hospitalised in just 2 months (March-April), were predominantly from the UK, and about half were over 70 years old. These demographics explain the high raw hCFR and the large proportion of patients presenting with age-related comorbidities – nearly half have hypertension, one-in-five chronic cardiac disease, and one-in-six diabetes. The regression results here should, however, be quite generalisable to hospitalised populations worldwide as country was accounted for as a predictor. Third, there are inherent limitations of observational data, however large the dataset; in particular, we cannot attribute a cause to many of the phenomena described here. It is most notably not entirely possible to unpick biological effects from clinical decisions. As one example, the association of ICU/HDU admission with male sex is may be due not just to increased disease severity amongst males, but also clinician knowledge of the potential for more severe disease. Similarly, we see a lower rate of ICU/HDU admissions amongst individuals whose symptoms started following admission. On the one hand, it is likely that the population of patients with symptoms emerging in hospital had on average less severe disease, as mild community-acquired infections are less likely to present to hospital. On the other, as those patients will receive clinical care starting at the moment of diagnosis, the need for ICU/HDU is likely reduced even in more serious cases. Fourth, some variables are based on patient self-report which can be inexact; for example, it can be clearly seen in Figure 1a that multiples of seven reported days from symptom onset to admission are overrepresented, suggesting reports in units of weeks. Fifth, some variables are not available to us; for example, resuscitation status and suitability for intensive care admission was not collected in our cohort, and without those variables the reasons for death or lack of ICU/HDU admission cannot be entirely unpicked. Similarly, we are not aware of what resource or bed capacity constraints may have affected individual sites at different times. Sixth, there may be a selection bias with respect to calendar time as a result of case volumes. Recruitment was performed by sites, upon identification of a patient with COVID-19 symptoms, according to their capacity, which was determined by the availability of staff to invite informed consent (as applicable) and complete data forms. Capacity will be subject to both geographical and temporal variations, and it is likely that both the proportion of patients recruited and the proportion completing follow-up would be reduced at times of high pressure on the site and the national healthcare system. However, enrolment was prospective, and as such staff would be blind to our outcomes of interest. In addition, while it is possible that individual sites chose patients to recruit (or cease following up) based on clinical characteristics, it is unclear why the basis for these decisions would show a consistent direction of bias amongst diverse locations. Lastly, one should refrain from overinterpreting data: some of the changes observed reflect adjustments in practice and logistics, or combined pressure on health systems, more than actual effects of interventions.

### Implications of findings

Often, in high-income countries, patient outcomes are seen through the lens of individualised treatment provided at the clinician patient interface. This paper demonstrates that outbreak epidemiology has an important influence on patient outcomes – the patient journey from likelihood of admission, through to disposition and length of stay in hospital, and overall outcome, change over the course of a pandemic. There are various explanations for variability – systems may at times be overwhelmed and unable to provide the usual quality of care to their patients; patient behaviour may change depending on perceptions of the status of the outbreak and the performance of the healthcare system at a given time; clinician familiarity with management of patients may vary; and changes in transmissibility and virulence are expected to occur.

The observed variability should inform on the limitations of using observational data during a long-lasting pandemic for management purposes in practice, and also question the use of some variables, such as length of stay in hospital or in ICU, as clinical trial outcomes. This demonstrates the importance of controlling for patient outcome data when designing clinical trials; for example, using our data, assessing a new treatment during the months of March to July will have shown a decrease in hCFR from 33%, to 21 % that may have been falsely attributed to a treatment effect without a concurrent randomised control.

At the same time, these findings also highlight the need for preparedness and resilience; the crucial importance of pre-positioned observational data collection systems that are adhered upon by a representative number of sites and are maintained for as long as the pandemic lasts; and the need for such capacity to be kept in-between epidemics.
