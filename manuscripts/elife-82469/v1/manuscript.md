# Estimating the contribution of subclinical tuberculosis disease to transmission: An individual patient data analysis from prevalence surveys

## Authors

- Jon C Emery<sup>1</sup> ([ORCID: 0000-0001-6644-7604](https://orcid.org/0000-0001-6644-7604)) †
- Peter J Dodd<sup>2</sup>
- Sayera Banu<sup>3</sup>
- Beatrice Frascella<sup>4</sup>
- Frances L Garden<sup>5</sup>
- Katherine C Horton<sup>1</sup>
- Shahed Hossain<sup>7</sup>
- Irwin Law<sup>8</sup>
- Frank van Leth<sup>9</sup>
- Guy B Marks<sup>5</sup>
- Hoa Binh Nguyen<sup>12</sup>
- Hai Viet Nguyen<sup>12</sup>
- Ikushi Onozaki<sup>13</sup>
- Maria Imelda D Quelapio<sup>14</sup>
- Alexandra S Richards<sup>1</sup>
- Nabila Shaikh<sup>1</sup>
- Edine W Tiemersma<sup>16</sup>
- Richard G White<sup>1</sup>
- Khalequ Zaman<sup>3</sup>
- Frank Cobelens<sup>17</sup>
- Rein MGJ Houben<sup>1</sup> ([ORCID: 0000-0003-4132-7467](https://orcid.org/0000-0003-4132-7467))

### Affiliations

1. TB Modelling Group, TB Centre and Centre for Mathematical Modelling of Infectious Diseases, Department of Infectious Disease Epidemiology, London School of Hygiene & Tropical Medicine London United Kingdom ([ROR:00a0jsq62](https://ror.org/00a0jsq62))
2. School of Health and Related Research, University of Sheffield Sheffield United Kingdom ([ROR:05krs5044](https://ror.org/05krs5044))
3. International Centre for Diarrhoeal Disease Research Dhaka Bangladesh ([ROR:04vsvr128](https://ror.org/04vsvr128))
4. School of Public Health, Vita-Salute San Raffaele University Milan Italy ([ROR:01gmqr298](https://ror.org/01gmqr298))
5. South West Sydney Clinical Campuses, University of New South Wales Sydney Australia ([ROR:03r8z3t63](https://ror.org/03r8z3t63))
6. Ingham Institute of Applied Medical Research Sydney Australia ([ROR:03y4rnb63](https://ror.org/03y4rnb63))
7. James P. Grant School of Public Health, BRAC University Dhaka Bangladesh ([ROR:00sge8677](https://ror.org/00sge8677))
8. Global Tuberculosis Programme, World Health Organization Geneva Switzerland ([ROR:01f80g185](https://ror.org/01f80g185))
9. Department of Health Sciences, VU University Amsterdam Netherlands ([ROR:008xxew50](https://ror.org/008xxew50))
10. Amsterdam Public Health Research Institute Amsterdam Netherlands
11. Woolcock Institute of Medical Research Sydney Australia ([ROR:04hy0x592](https://ror.org/04hy0x592))
12. National Lung Hospital, National Tuberculosis Control Program Ha Noi Viet Nam
13. Research Institute of Tuberculosis, Japan Anti-Tuberculosis Association Tokyo Japan ([ROR:012daep68](https://ror.org/012daep68))
14. Tropical Disease Foundation Makati City Philippines ([ROR:05jxxs868](https://ror.org/05jxxs868))
15. Sanofi Pasteur Reading United Kingdom
16. KNCV Tuberculosis Foundation The Hague Netherlands ([ROR:0287mpm73](https://ror.org/0287mpm73))
17. Department of Global Health and Amsterdam Institute for Global Health and Development, Amsterdam University Medical Centers, University of Amsterdam Amsterdam Netherlands ([ROR:037n2rm85](https://ror.org/037n2rm85))

† Corresponding author

## Abstract

Background:Individuals with bacteriologically confirmed pulmonary tuberculosis (TB) disease who do not report symptoms (subclinical TB) represent around half of all prevalent cases of TB, yet their contribution to Mycobacterium tuberculosis (Mtb) transmission is unknown, especially compared to individuals who report symptoms at the time of diagnosis (clinical TB). Relative infectiousness can be approximated by cumulative infections in household contacts, but such data are rare.Methods:We reviewed the literature to identify studies where surveys of Mtb infection were linked to population surveys of TB disease. We collated individual-level data on representative populations for analysis and used literature on the relative durations of subclinical and clinical TB to estimate relative infectiousness through a cumulative hazard model, accounting for sputum-smear status. Relative prevalence of subclinical and clinical disease in high-burden settings was used to estimate the contribution of subclinical TB to global Mtb transmission.Results:We collated data on 414 index cases and 789 household contacts from three prevalence surveys (Bangladesh, the Philippines, and Viet Nam) and one case-finding trial in Viet Nam. The odds ratio for infection in a household with a clinical versus subclinical index case (irrespective of sputum smear status) was 1.2 (0.6–2.3, 95% confidence interval). Adjusting for duration of disease, we found a per-unit-time infectiousness of subclinical TB relative to clinical TB of 1.93 (0.62–6.18, 95% prediction interval [PrI]). Fourteen countries across Asia and Africa provided data on relative prevalence of subclinical and clinical TB, suggesting an estimated 68% (27–92%, 95% PrI) of global transmission is from subclinical TB.Conclusions:Our results suggest that subclinical TB contributes substantially to transmission and needs to be diagnosed and treated for effective progress towards TB elimination.Funding:JCE, KCH, ASR, NS, and RH have received funding from the European Research Council (ERC) under the Horizon 2020 research and innovation programme (ERC Starting Grant No. 757699) KCH is also supported by UK FCDO (Leaving no-one behind: transforming gendered pathways to health for TB). This research has been partially funded by UK aid from the UK government (to KCH); however, the views expressed do not necessarily reflect the UK government’s official policies. PJD was supported by a fellowship from the UK Medical Research Council (MR/P022081/1); this UK-funded award is part of the EDCTP2 programme supported by the European Union. RGW is funded by the Wellcome Trust (218261/Z/19/Z), NIH (1R01AI147321-01), EDTCP (RIA208D-2505B), UK MRC (CCF17-7779 via SET Bloomsbury), ESRC (ES/P008011/1), BMGF (OPP1084276, OPP1135288 and INV-001754), and the WHO (2020/985800-0).

## Introduction

An estimated 1.5 million people died from tuberculosis (TB) disease in 2020, and TB is on course to retake its position as the largest cause of death by a single infectious agent (World Health Organisation, 2021). Fuelled by ongoing transmission through exhaled or expectorated Mycobacterium tuberculosis (Mtb) bacteria, TB incidence is declining at a rate of 1–2% per annum, which is too slow given the risk and scale of mortality (World Health Organisation, 2021; Ragonnet et al., 2021), lifelong impairment (Dodd et al., 2021; Alene et al., 2021), poverty (Pedrazzoli et al., 2021), and macroeconomic consequences (Silva et al., 2021). Problematically, most Mtb transmission in high-incidence settings remains unaccounted for (Dodd et al., 2021), with less than 1-in-10 occurrences of TB explained by transmission from a known contact (Glynn et al., 2015).

In recent decades the prevailing paradigm in TB policy held that symptoms and infectiousness commence simultaneously as part of ‘active disease’ (World Health Organization, 2020; World Health Organisation, 1974; Houben et al., 2019). As a consequence, a policy of passive case-finding (Golub et al., 2005), in which individuals are expected to attend a health facility with TB-related symptoms before receiving diagnosis and treatment, was relied upon to prevent deaths from TB, which it has (World Health Organisation, 2021; Mandal et al., 2017), and reduce incidence by interrupting transmission, which it has not (World Health Organisation, 2021).

Over the last decade, this classic paradigm of TB has been increasingly challenged (Barry et al., 2009; Drain et al., 2018; Behr et al., 2018). One important advance has been the finding in population surveys that not all individuals identified with bacteriologically confirmed TB report having symptoms such as cough at the time of screening for TB (Onozaki et al., 2015; Law et al., 2020). As such we can make a distinction between clinical and subclinical TB, where subclinical TB (sometimes referred to as ‘asymptomatic’ [Frascella et al., 2021] or ‘early’ TB [Kendall et al., 2021]) refers to individuals who have detectable Mtb bacteria in their sputum but do not experience, are not aware of, or do not report symptoms (Houben et al., 2019). In contrast, individuals with clinical TB disease report symptoms. We distinguish both disease states from Mtb infection, whereby individuals may test positive on a tuberculin skin test (TST) or interferon-gamma release assay (IGRA) but do not have bacteriologically confirmed disease.

Empirical data have shown that bacteriological state (i.e. whether Mtb is detectable in pulmonary secretions) is a strong predictor of the potential for transmission. For example, molecular epidemiological studies show that sputum smear-positive individuals (i.e. Mtb detected via microscopy) are 3–6 times more likely to be sources for TB disease in contacts compared to smear-negative individuals (Behr et al., 1999; Hernández-Garduño et al., 2004; Tostmann et al., 2008). Surveys of Mtb infection prevalence in household contacts provide similar values (Grzybowski et al., 1975). These studies focussed on passively diagnosed individuals with clinical disease. It is, however, increasingly clear that the presence of respiratory symptoms, such as a persistent cough, is not required for the exhalation of potentially Mtb-containing aerosols (Patterson and Wood, 2019; Asadi et al., 2019; Leung et al., 2020; Dinkele et al., 2022). Indeed, whilst recent empirical studies have suggested that tidal breathing may contribute significantly to Mtb transmission (Dinkele et al., 2022), exhalation of infectious aerosols appears unrelated to the presence of symptoms (Theron et al., 2020) or cough frequency (Williams et al., 2020) in TB patients. This supports the hypothesis that subclinical disease can contribute, potentially substantially, to transmission (Houben et al., 2019; Kendall et al., 2021; Dowdy et al., 2013).

A recent review found that about half of prevalent bacteriologically confirmed pulmonary TB disease is subclinical (Frascella et al., 2021) and it is becoming increasingly apparent that subclinical TB can persist for a long period without progressing to clinical disease (Richards et al., 2021; Ku et al., 2021). As individuals with subclinical TB will not be identified by current passive case-finding strategies, they will continue to contact susceptible individuals and, if infectious, transmit throughout their subclinical phase. It is therefore possible that those with subclinical TB may be a major contributor to ongoing, and unaccounted for, Mtb transmission. If this is the case, and if the ambitious goal to end TB as a global health problem by 2035 is to be met (World Health Organisation, 2022), TB policy needs to shift away from solely focussing on symptom-dependent case-finding (e.g. patient-initiated passive case-finding) towards strategies that are symptom-independent.

To motivate and inform such a shift in research and policy priorities, two key questions that to date remain unanswered must be addressed. Firstly, how infectious are individuals with subclinical TB compared to those with clinical TB per unit time, and, secondly, what is their contribution to overall transmission in the current TB epidemic?

In TB, data sources on the transmission potential from sputum smear-negative individuals relative to smear-positive (e.g. molecular epidemiological studies; Behr et al., 1999; Hernández-Garduño et al., 2004; Tostmann et al., 2008) have often been directly interpreted as relative infectiousness, which is incorrect (Kendall, 2021). Instead of representing the metric of interest, which is the potential for transmission per unit time for a particular group relative to a reference group (i.e. relative infectiousness), these data actually provided a relative estimate of cumulative exposure (as acknowledged by these studies’ authors; Behr et al., 1999; Hernández-Garduño et al., 2004; Tostmann et al., 2008). Cumulative exposure is a composite of relative infectiousness per unit time and disease duration (technically duration of infectiousness), which until now have been unavailable and can be hard to disentangle from each other (Kendall, 2021).

In this work we look to overcome these challenges by harnessing increased understanding of the natural history and prevalence of subclinical TB and re-analysing data from existing population studies.

## Methods

### Data

To estimate the infectiousness of subclinical TB relative to clinical TB, we considered studies in which Mtb infection surveys were performed amongst household contacts of culture and/or nucleic acid amplification test (NAAT) confirmed cases where data on their symptom and sputum smear status at the time of diagnosis was available. We considered only studies in which households with no index case were also surveyed for Mtb infection as a measure of the background rate of infection.

Such studies identified index cases using symptom-independent screening either via a TB prevalence survey (in which all individuals are screened with a chest X-ray; World Health Organisation, 2011) or community-wide active case-finding amongst a representative sample of a target population. Subclinical and clinical index cases were defined as being culture and/or NAAT-positive and responding negatively or positively to an initial symptom screening, respectively. Households with a single subclinical or clinical index case were defined as subclinical and clinical households, respectively. Such households were then stratified by the sputum smear status of the index case at the time of diagnosis. Background households were defined as having no index case. Finally, Mtb infection surveys were performed amongst all households, providing the prevalence of infection amongst each household type.

We reviewed the literature for household contact studies that measure Mtb infection via TST or IGRA as an outcome and provide sufficient information to stratify households by symptom and sputum smear status, including households with no index case (see Appendix 1 for the detailed search strategy). Individual, patient-level data from each of these studies were analysed to provide the prevalence of infection amongst each household type (see Appendix 1 for detailed data analysis). These data are presented in Appendix 1—table 1. Odds ratios (ORs) for infection in members of a household with a sputum smear-positive versus a smear-negative index case (irrespective of symptoms) and in members of a household with a clinical versus subclinical index case (irrespective of sputum smear status) were also calculated for purposes of illustration.

### Cumulative hazard model

To estimate the infectiousness of subclinical TB per unit time relative to clinical TB, we fitted a cumulative hazard model of infection to the prevalence of infection amongst each household type for each study separately using the data described above.

For each study, household contacts were pooled into five cohorts: background; subclinical and sputum smear-negative; subclinical and sputum smear-positive; clinical and sputum smear-negative; clinical and sputum smear-positive. It was assumed that each cohort is exposed to the same background hazard, reflecting the force of infection from outside the household. It was then assumed that all cohorts except the background were exposed to an additional hazard, reflecting the force of infection from the cohort’s respective index cases.

The final prevalence of infection in each cohort will then depend on the background cumulative hazard ΛB and an additional cumulative hazard ΛI specific to each household type I (see Appendix 1 for model equations). We use the cumulative hazard from clinical (C), smear-positive (+) index cases as a benchmark with which to define the cumulative hazards from the remaining index case types. We assume that being subclinical (S) or smear-negative (-) have separate, multiplicative effects, such that

$$
Λ_{C−}=r_{−}Λ_{C+}, Λ_{S+}=r_{s}Λ_{C+}, Λ_{S−}=r_{−}r_{s}Λ_{C+},
$$

where rs and r- are the subclinical and sputum smear-negative relative cumulative hazards, respectively.

#### Model fitting

The model described above was fitted to the prevalence of infection in each of the five household types for each study separately. Fitting was performed in a Bayesian framework using Markov-Chain Monte Carlo methods (see Appendix 1 for further details of model fitting). We report median and 95% equal-tailed posterior intervals (PoIs).

#### Relative infectiousness of subclinical TB

To infer the infectiousness of subclinical TB per unit time relative to clinical TB from our posterior estimate for the subclinical relative cumulative hazard rs, we note that, assuming constant hazards, the relative cumulative hazards from index cases will depend on the product of the relative per unit time infectiousness and relative durations of infectiousness. We assume that per unit time infectiousness depends on symptom status and sputum smear status, whilst durations of infectiousness depend on symptom status only. It follows then that:

$$
r_{s}=\alpha_{s}\gamma_{s},
$$



$$
r_{−} =\alpha_{−},
$$

where αs and α- are the per unit time infectiousness of subclinical relative to clinical index cases and sputum smear-negative relative to smear-positive index cases, respectively, and γs is the duration of infectiousness for subclinical relative to clinical index cases.

To provide a value for the duration of infectiousness of subclinical relative to clinical index cases, we used the results from a recent study that estimated the durations of subclinical and clinical TB using a Bayesian analysis of prevalence and notification data (Ku et al., 2021). With the result that the subclinical phase represented between 27% and 63% of the time as a prevalent case, we used a duration of subclinical TB relative to clinical TB of 0.8 (0.4–1.7, 95% PoI). We assumed that there was no difference in duration for sputum smear-negative versus smear-positive TB.

Finally, we sampled from the posterior estimate for the subclinical relative cumulative hazard and an assumed duration of disease for subclinical index cases relative to clinical index cases, providing a median and 95% equal-tailed posterior estimate for the relative infectiousness of subclinical index cases relative to clinical index cases for each study separately. Thereafter we provide a summary estimate by mixed-effects meta-analysing the individual estimates across the separate studies. Analogous results are presented for the relative infectiousness per unit time of sputum smear-negative TB relative to smear-positive TB.

### Subclinical versus clinical TB: Prevalence and bacteriological indicators

To estimate the proportion of overall transmission from subclinical TB, we first estimated the proportion of prevalent TB that is subclinical as well as the proportion of prevalent subclinical and clinical TB that is smear-positive.

We began with a recent review of TB prevalence surveys in Asia and Africa (Frascella et al., 2021) (see Appendix 1 for details of the search strategy). Such surveys generally performed an initial screening using both a questionnaire, which includes questions about recent symptoms typical of TB, as well a chest radiograph. Those screening positive from either method were then tested via culture and/or NAAT. A sputum smear test was often additionally performed.

We reviewed the surveys in Frascella et al., 2021 and, for each survey where sufficient information was available, extracted the number of culture and/or NAAT confirmed cases of TB, stratified by both symptom status at initial screening and sputum smear status (see Appendix 1 for detailed data analysis). Extracted data can be found in Appendix 1—table 2. We defined subclinical and clinical TB as being culture and/or NAAT-positive and responding negatively or positively to an initial symptom screen, respectively, consistent with the definitions for subclinical and clinical index cases in the previous section. The most common screening question was a productive cough of greater than 2-week duration, although other diagnostic algorithms were included.

For each survey, we calculated the proportion of prevalent TB that is subclinical (PSTB) as well as the proportion of prevalent subclinical and clinical TB that is smear-positive (P+S and P+C, respectively).

We performed univariate, random-effects meta-analyses on PSTB, P+S and P+C. We meta-analysed the inverse logit transformed variables, before transforming the results back to proportions and presenting a central estimate and 95% prediction interval for each variable.

### The contribution of subclinical TB to transmission

To estimate the contribution of subclinical TB to transmission, we applied our estimates of relative infectiousness to the prevalence surveys that reported the required data by symptom and smear status (see Appendix 1 for further details).

All analyses were conducted using R version 4.0.3 (R Development Core Team, 2014). Bayesian fitting was performed in Stan version 2.21.0 (Stan Development Team, 2021) using RStan (Stan Development Team, 2020) as an interface.

No new human subject data was collected for this work, which re-analysed individual patient data collected during four observational studies in three countries. Procedures, including consent where available, are described in the original publications. Local and institutional Ethics Approval was in place for each survey, through the Department of Health (the Philippines survey; Tupasi et al., 1999), Institutional Review Board of the Viet Nam National Lung Hospital (Viet Nam survey; Hoa et al., 2010), the Ministry of Health and Family Welfare of Bangladesh as well as the Research Review Committee and Ethics Review Committee of the iccdr,b (Bangladesh survey; Zaman et al., 2012), and Institutional Review Board of the Viet Nam National Lung Hospital as well as Human Research Ethics Committee of the University of Sydney (ACT3 survey; Marks et al., 2019). The ethics committee of the London School of Hygiene and Tropical Medicine gave ethical approval for this project (#16396).

### Sensitivity analyses

#### Sensitivity analysis 1

Given the different designs of the Bangladesh (2007) prevalence survey (Zaman et al., 2012) (which provided only sputum smear-positive index cases) and the active case-finding trial in Viet Nam (2017) (Marks et al., 2019) (which provided index cases via repeated case-finding-related screening and prevalence surveys), the above analysis was repeated omitting these studies.

#### Sensitivity analysis 2

As a sensitivity the above analysis was repeated with an alternative estimate for the relative duration of subclinical TB versus clinical TB using instead data from a recent systematic review and data synthesis study (Richards et al., 2021) and a simple competing risk model (see Appendix 1 for further details).

#### Sensitivity analysis 3

To explore the impact of a differential background risk of infection amongst households with and without index cases, the analysis was repeated assuming a 50% increase in the background risk of infection for those households with an index case.

#### Sensitivity analysis 4

Instead of assuming equal durations for sputum smear-positive and smear-negative TB, the above analysis was repeated assuming that sputum smear-positive TB has twice the duration of smear-negative TB.

#### Sensitivity analysis 5

In the main analysis, each study was modelled separately, with the results combined using meta-analyses. As a sensitivity we model all studies simultaneously, assuming local background risks of infection for each study and global values across all studies for the remaining cumulative hazards.

## Results

### Data

Four studies were included for analysis: three prevalence surveys of TB disease with associated Mtb infection surveys in Viet Nam (2007) (Hoa et al., 2010), Bangladesh (2007) (Zaman et al., 2012), and the Philippines (1997) (Tupasi et al., 1999) and a community-wide active case-finding trial in Viet Nam (2017) (Marks et al., 2019).

ORs for infection in members of a household with a clinical versus subclinical index case (irrespective of sputum smear status), based on the result of their symptom screen at the time of diagnosis, are shown in Figure 1A. A mixed-effects meta-analysis across studies provides OR = 1.2 (0.6–2.3, 95% confidence interval [CI]). Figure 1B shows the OR for infection in members of a household with a sputum smear-positive versus a smear-negative index case (irrespective of symptoms), where the Bangladesh prevalence survey is omitted as this study only included smear-positive individuals. In contrast to the analysis by symptom status, evidence for a difference in cumulative infection was found by smear status, with OR = 2.3 (1.3–3.9, 95% CI), which is in line with previous estimates (Grzybowski et al., 1975).

![Figure 1.](https://cdn.elifesciences.org/articles/82469/elife-82469-fig1-v1.jpg)

**Figure 1.:** Illustrated are central estimates and 95% confidence intervals for each study separately and the results of a mixed-effects meta-analysis. Results for sputum smear status are omitted for Bangladesh as the survey considered only sputum smear-positive individuals.

### Estimating the relative infectiousness of subclinical TB

The estimated infectiousness of subclinical TB per unit time relative to clinical TB is shown in Figure 2A, both for each study separately as well as the mixed-effects meta-analysed result across studies of 1.93 (0.62–6.18, 95% prediction interval [PrI]). Figure 2B shows the analogous results for the infectiousness per unit time of sputum smear-negative versus smear-positive TB, with a summary value of 0.26 (0.03–2.47, 95% PrI). Detailed model results are shown in Appendix 1—table 4 and Appendix 1—figures 2–5.

![Figure 2.](https://cdn.elifesciences.org/articles/82469/elife-82469-fig2-v1.jpg)

**Figure 2.:** Illustrated are the median and 95% confidence intervals for each study separately and the median and 95% prediction interval results from mixed-effects meta-analyses across studies with an associated measure of heterogeneity (I2).

### Prevalence and bacteriological indicators for subclinical and clinical TB

Data from 15 prevalence surveys where the proportion of subclinical and clinical TB was reported by sputum smear status were included, detailed in Appendix 1—table 2. These represented a range of high TB burden countries in Africa (n = 5) and Asia (n = 9, with two surveys in Viet Nam). In this subset, the overall proportion of prevalent TB that is subclinical was 58% (29–82%, 95% PrI), whilst the proportion smear-positive was 33% (18–52%, 95% PrI) for subclinical TB and 53% (25–80%, 95% PrI) for clinical TB. Detailed results for each variable are shown in Figure 3A–C.

![Figure 3.](https://cdn.elifesciences.org/articles/82469/elife-82469-fig3-v1.jpg)

**Figure 3.:** Illustrated are median and 95% confidence intervals for each study separately and the median and 95% prediction intervals from mixed-effects meta-analyses across studies with an associated measure of heterogeneity (I2). Also shown is the estimated proportion of transmission from subclinical TB at the time of and in the location of each of the prevalence surveys in Africa and Asia (D). Illustrated is the median and 95% prediction intervals for each study separately as well as the global value. DPR = Democratic People’s Republic; PDR = People’s Democratic Republic.

### The contribution of subclinical TB to transmission: Global and country levels

We quantified the contribution of subclinical TB to ongoing Mtb transmission by combining the estimates for the infectiousness of subclinical TB per unit time relative to clinical TB (Figure 2A), the infectiousness of sputum smear-negative TB relative to smear-positive TB (Figure 2B), and the proportion of prevalent TB that is subclinical and the proportion of subclinical and clinical TB that is sputum smear-positive (Figure 3A–C). The 14 included countries are a reasonable reflection of the geography and epidemiological characteristics of high TB burden countries in the WHO African, South-East Asia, and Western Pacific regions, which together represent around 85% of current global TB incidence (World Health Organisation, 2021). As such we used a summary value for the included surveys as a global estimate.

Figure 3D shows the results by country and globally, where 68% (27–92%, 95% PrI) of global Mtb transmission is estimated to come from prevalent subclinical TB, ranging from 45% (19–76%, 95% PrI) in Nigeria to 84% (60–95%, 95% PrI) in Mongolia.

### Sensitivity analyses

#### Sensitivity analysis 1

The above analysis was repeated excluding two studies with methodologies that differed from the remaining two: the Bangladesh (2007) prevalence survey (Zaman et al., 2012) (which provided sputum smear-positive index cases only) and the active case-finding trial in Viet Nam (ACT3 [2017]) (Marks et al., 2019) (which provided index cases via repeated screening related to case-finding as well as prevalence surveys). Affected results are shown in Appendix 1—figure 6. The infectiousness of subclinical TB per unit time relative to clinical TB decreased to 1.39 (0.17–11.2, 95% PrI), and the infectiousness of sputum smear-negative TB relative to smear-positive TB decreased to 0.12 (0.03–0.53, 95% PrI), with corresponding values of 57% (10–94%, 95% PrI) of global transmission from subclinical TB, ranging from 34% (6–81%, 95% PrI) in Nigeria to 76% (28–97%, 95% PrI) in Mongolia.

#### Sensitivity analysis 2

The above analysis was repeated using an alternative estimate for the relative duration of subclinical TB versus clinical TB of 0.72 (0.60–0.89, 95% PoI), from Richards et al., 2021. Affected results are shown in Appendix 1—figure 7. The infectiousness of subclinical TB per unit time relative to clinical TB increased to 2.19 (0.91–5.26, 95% PrI), with corresponding values of 71% (32–92%, 95% PrI) of global transmission from subclinical TB, ranging from 48% (25–74%, 95% PrI) in Nigeria to 86% (68–95%, 95% PrI) in Mongolia.

#### Sensitivity analysis 3

The above analysis was repeated assuming that households with an index case have a 50% greater background risk of infection than households with no index case. Affected results are shown in Appendix 1—figure 8. The infectiousness of subclinical TB per unit time relative to clinical TB increased to 2.44 (0.60–10.06, 95% PrI) whilst the infectiousness of sputum smear-negative TB relative to smear-positive TB increased to 0.36 (0.03–4.51, 95% PrI), with corresponding values of 74% (29–95%, 95% PrI) of global transmission from subclinical TB, ranging from 53% (20–85%, 95% PrI) in Nigeria to 88% (61–97%, 95% PrI) in Mongolia.

#### Sensitivity analysis 4

The above analysis was repeated assuming sputum smear-positive TB has twice the duration of smear-negative TB. Affected results are shown in Appendix 1—figure 9. The infectiousness of subclinical TB per unit time relative to clinical TB was largely unchanged at 1.94 (0.63–6.16, 95% PrI) whilst the infectiousness of sputum smear-negative TB relative to smear-positive TB increased to 0.51 (0.06–4.39, 95% PrI), with corresponding values of 70% (29–93%, 95% PrI) of global transmission from subclinical TB, ranging from 49% (21–79%, 95% PrI) in Nigeria to 86% (63–96%, 95% PrI) in Mongolia.

#### Sensitivity analysis 5

The above analysis was repeated with all studies modelled simultaneously, assuming local background risks of infection for each study and global values across all studies for the remaining cumulative hazards. Affected results are shown in Appendix 1—figure 10. The infectiousness of subclinical TB per unit time relative to clinical TB decreased to 1.39 (0.50–4.02, 95% PrI) whilst the infectiousness of sputum smear-negative TB relative to smear-positive TB decreased to 0.11 (0.02–0.68, 95% PrI), with corresponding values of 58% (20–88%, 95% PrI) of global transmission from subclinical TB, ranging from 34% (15–62%, 95% PrI) in Nigeria to 76% (52–91%, 95% PrI) in Mongolia.

## Discussion

By fitting a cumulative hazard model of infection to prevalence data amongst household contacts of subclinical and clinical index cases, we were able to provide quantitative estimates for the relative infectiousness per unit time of subclinical TB and its contribution to ongoing Mtb transmission. Despite wide uncertainty intervals, the raw data, as well as the results of our analysis, do not suggest subclinical TB is substantially less infectious than clinical TB. Given the high prevalence of subclinical TB found in surveys (Frascella et al., 2021), it is therefore likely that subclinical TB contributes substantially to ongoing Mtb transmission in high-burden settings.

Our results were relatively robust to the sensitivities that were performed. In two cases, that is, the removal of two studies (sensitivity analysis 1) and the use of a single model to account for all studies (sensitivity analysis 5), our estimates for the relative infectiousness of subclinical TB relative to clinical TB and the proportion of transmission from subclinical TB were lower than in the primary analysis. Our qualitative results and conclusions remain unchanged however. All other sensitivities resulted in higher estimates.

There are no other estimates for the infectiousness of subclinical TB relative to clinical TB in the literature with which to compare our results. Using data from the 2007 Viet Nam prevalence survey, however, Nguyen et al., 2023 find that among children aged 6–10 years, those living with clinical, smear-positive TB, and those living with subclinical, smear-positive TB had similarly increased risks of TST positivity compared with those living without TB. Moreover, a recent small study from Uganda found no evidence of a difference in cumulative infection rates in household contacts of patients who did or did not report symptoms (Baik et al., 2021). Our results are also in keeping with recent results from whole-genome sequencing (Xu et al., 2019) in which 36% of individuals likely transmitted Mtb before symptom onset, assuming a linear SNP mutation rate. We also note that previous hypothetical modelling of subclinical TB used assumed values for relative infectiousness that are in keeping with our estimated range (Dowdy et al., 2013; Arinaminpathy and Dowdy, 2015). More broadly, recent work on SARS-CoV-2 and malaria has similarly shown how ‘asymptomatic’ or ‘subpatent’ infections can be important drivers of transmission (Slater et al., 2019; Emery et al., 2020; Johansson et al., 2021), meaning a role for asymptomatic transmission would not be unique to TB.

Whilst we have presented a novel approach to investigating transmission from individuals with subclinical TB using pre-existing data, limitations in our methodology remain. Identifying relative infectiousness is challenging. Our estimates rely on studies which screened a minimum of 252,000 individuals for bacteriologically confirmed TB disease and 63,000 individuals for Mtb infection. Even at this scale, the small number of studies and diagnosed cases of TB still leads to substantial uncertainty, highlighting the challenge faced by single studies to estimate such values (Marks et al., 2019; Baik et al., 2021). Indeed, the paucity of the data provides an estimate that is consistent with subclinical TB being more infectious than clinical TB. Whilst we consider this to be implausible, we have avoided introducing priors that rule out this possibility. Instead we would emphasise that our results reflect the uncertainty of the data. The lower bound of our estimate precludes subclinical TB being significantly less infectious than clinical TB, while there is no evidence against subclinical TB being as infectious as clinical TB. Despite such uncertainty, this study brings together the best currently available epidemiological data which, combined with appropriate analysis techniques, provides a data-driven estimate for this important question.

Although infection studies in household contacts have provided a novel window into transmission from subclinical individuals, it is not possible to establish a transmission link between presumed index cases and infections amongst household contacts using molecular methods (Kendall, 2021). Such household contact studies are therefore liable to biases and our study necessarily inherits such limitations. For example, whilst our model does use a background rate of infection as a baseline from which to estimate the additional force of infection from presumed index cases within the household, there remains the residual risk that certain household types may systematically contain more or less infections from transmission outside the household than on average.

An important limitation of our cumulative hazard model is the assumption that index cases only ever had the disease type they were diagnosed with during screening (e.g. sputum smear-positive, subclinical). Instead, it is more likely that individuals will fluctuate between being, for example, subclinical and clinical (Richards et al., 2021). The impact such additional dynamics would have on our results remains uncertain since they would depend on the detailed model of tuberculosis natural history assumed. Such a model would require additional data to prevent the need for additional assumptions.

We estimated the contribution of subclinical TB to transmission at the population level, including transmission outside the household, using information on relative infectiousness inferred from household contact studies. A more refined estimate may need to take additional factors into account. For example, it is likely that, whilst inside the household the contact rates for subclinical and clinical individuals are likely to be similar, contact with individuals outside the household may differ (Glynn et al., 2020).

We defined subclinical and clinical TB as being culture and/or NAAT-positive and responding negatively or positively to an initial symptom screen, respectively. In practice subclinical and clinical TB are part of a continuous spectrum and alternative definitions could be defined according to different criteria. Here we have used the definition most closely aligned with the methodology of the majority of prevalence surveys, which is consistent with other studies of subclinical TB (Frascella et al., 2021) and pragmatic for inclusion of future surveys.

Meta-analyses were used to provide ranges for several quantities of interest. Whilst the heterogeneity for the relative infectiousness of subclinical and smear-negative TB were low (I2 = 0% and I2 = 36%, respectively), the heterogeneity for the proportion of prevalent TB that is subclinical and the proportions of subclinical and clinical TB that are smear-positive were high (I2 = 95%, I2 = 81% and I2 = 89%, respectively). As such, we have used the more conservative prediction interval (as opposed to credible interval) to reflect this heterogeneity in the final results (Riley et al., 2011; Deeks et al., 2021).

Finally, our data are from populations with a low prevalence of HIV co-infection and the HIV status of individuals with TB was mostly unavailable, making a sub-analysis by HIV and antiretroviral (ART) status impossible. Whilst the subclinical TB presentation is likely affected by HIV in terms of duration and prevalence, it is unknown whether or by how much the relative differences in duration and prevalence between subclinical and clinical TB also change (Frascella et al., 2021; National Department of Health - South Africa, 2021). If they exist, any such differences by HIV-coinfection status are likely to be reduced by effective viral suppression, which an estimated two-thirds of people living with HIV have achieved (UNAIDS, 2021). So while it remains highly valuable to accumulate additional relevant data (Baik et al., 2021), we feel our main findings are broadly robust to this limitation.

Our observation that reported symptoms are a poor proxy for infectiousness fits with historical and contemporary observations that symptom-independent TB screening and treatment policies can reduce TB burden at higher rates than usually seen under DOTS (Marks et al., 2019; Krivinka et al., 1974). This is in keeping with increasing data showing that symptoms, in particular the classic TB symptom of cough, are not closely correlated to the amount of Mtb exhaled (Williams et al., 2020) and observations of other pathogens, including SARS-CoV-2 infection (Emery et al., 2020; Johansson et al., 2021; Liu et al., 2020).

Whilst earlier diagnosis (i.e. before symptom onset) will likely bring individual-level benefits in terms of mortality and extent of post-TB sequelae (Allwood et al., 2019), the question of potential population benefits has hampered decisions from policymakers and funders on whether to invest resources in technologies and strategies that can identify subclinical TB. Our results suggest that a non-trivial proportion of all transmission would likely be unaffected by strategies that are insensitive to subclinical TB.

As our results show that subclinical TB likely contributes substantially to transmission, an increased emphasis on symptom agnostic screening in, for example, the TB screening guidelines (World Health Organization, 2021) should be considered, as should the inclusion of subclinical TB in the planned update of WHO case definitions. Target Product Profiles for diagnostic tools should consider all infectious TB, regardless of whether individuals are experiencing or aware of symptoms, and interventions using such tools should be critically evaluated for their impact on Mtb transmission and cost-effectiveness. While symptom-independent tools exist for screening (Williams et al., 2020; Marks et al., 2019; Yoon et al., 2017; Madhani et al., 2020; Scriba et al., 2021; Williams et al., 2014), specificity, costs, and logistics remain an obstacle. In addition, individuals are usually required to produce sputum as part of a confirmatory test, which around half of eligible adults in the general population are unable to do (Marks et al., 2019). Screening or diagnostic technologies that are symptom- as well as sputum-independent, while remaining low-tech and low-cost, remain the goal. Indeed, the advent of bio-aerosol measurements in TB may uncover additional infectious individuals whose sputum-based bacteriological test is negative, although these tools require validation in larger populations (Williams et al., 2020; Williams et al., 2014; Nathavitharana et al., 2022). Any bio-aerosol-positive, sputum-negative individuals are more likely to be subclinical and as such would mean we underestimated the contribution of subclinical TB to global Mtb transmission, even if their relative infectiousness may be lower than sputum-positive TB. As new diagnostic approaches are developed to capture the spectrum of TB disease, policymakers will need to decide on how to treat subclinical TB. In treatment, as in diagnosis, it is key that more tailored approaches are developed and tested so as to prevent over- or undertreatment of individuals with subclinical TB (Esmail et al., 2022).

### Conclusion

Subclinical TB likely contributes substantially to transmission in high-burden settings. If we are to meet EndTB targets for TB elimination, the TB community needs to develop technologies and strategies beyond passive case finding to address subclinical TB.
