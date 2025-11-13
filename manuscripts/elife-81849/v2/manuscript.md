# Quantifying the impact of immune history and variant on SARS-CoV-2 viral kinetics and infection rebound: A retrospective cohort study

## Authors

- James A Hay<sup>1</sup> ([ORCID: 0000-0002-1998-1844](https://orcid.org/0000-0002-1998-1844))
- Stephen M Kissler<sup>1</sup> ([ORCID: 0000-0003-3062-7800](https://orcid.org/0000-0003-3062-7800))
- Joseph R Fauver<sup>2</sup>
- Christina Mack<sup>4</sup>
- Caroline G Tai<sup>4</sup>
- Radhika M Samant<sup>4</sup>
- Sarah Connolly<sup>4</sup>
- Deverick J Anderson<sup>5</sup>
- Gaurav Khullar<sup>6</sup>
- Matthew MacKay<sup>6</sup>
- Miral Patel<sup>6</sup>
- Shannan Kelly<sup>6</sup>
- April Manhertz<sup>6</sup>
- Isaac Eiter<sup>6</sup>
- Daisy Salgado<sup>6</sup>
- Tim Baker<sup>6</sup>
- Ben Howard<sup>6</sup>
- Joel T Dudley<sup>6</sup>
- Christopher E Mason<sup>6</sup>
- Manoj Nair<sup>7</sup> ([ORCID: 0000-0002-5994-3957](https://orcid.org/0000-0002-5994-3957))
- Yaoxing Huang<sup>7</sup>
- John DiFiori<sup>8</sup>
- David D Ho<sup>7</sup>
- Nathan D Grubaugh<sup>2</sup> †
- Yonatan H Grad<sup>1</sup> ([ORCID: 0000-0001-5646-1314](https://orcid.org/0000-0001-5646-1314)) †

### Affiliations

1. Harvard TH Chan School of Public Health Boston United States
2. Yale School of Public Health New Haven United States
3. University of Nebraska Medical Center Omaha United States ([ROR:00thqtb16](https://ror.org/00thqtb16))
4. IQVIA, Real World Solutions Durham United States ([ROR:01mk44223](https://ror.org/01mk44223))
5. Duke Center for Antimicrobial Stewardship and Infection Prevention Durham United States
6. Tempus Labs Chicago United States ([ROR:01gbymr57](https://ror.org/01gbymr57))
7. Vagelos College of Physicians and Surgeons, Columbia University New York United States ([ROR:00hj8s172](https://ror.org/00hj8s172))
8. Hospital for Special Surgery New York United States ([ROR:03zjqec80](https://ror.org/03zjqec80))
9. National Basketball Association New York United States

† Corresponding author

## Abstract

Background:The combined impact of immunity and SARS-CoV-2 variants on viral kinetics during infections has been unclear.Methods:We characterized 1,280 infections from the National Basketball Association occupational health cohort identified between June 2020 and January 2022 using serial RT-qPCR testing. Logistic regression and semi-mechanistic viral RNA kinetics models were used to quantify the effect of age, variant, symptom status, infection history, vaccination status and antibody titer to the founder SARS-CoV-2 strain on the duration of potential infectiousness and overall viral kinetics. The frequency of viral rebounds was quantified under multiple cycle threshold (Ct) value-based definitions.Results:Among individuals detected partway through their infection, 51.0% (95% credible interval [CrI]: 48.3–53.6%) remained potentially infectious (Ct <30) 5 days post detection, with small differences across variants and vaccination status. Only seven viral rebounds (0.7%; N=999) were observed, with rebound defined as 3+days with Ct <30 following an initial clearance of 3+days with Ct ≥30. High antibody titers against the founder SARS-CoV-2 strain predicted lower peak viral loads and shorter durations of infection. Among Omicron BA.1 infections, boosted individuals had lower pre-booster antibody titers and longer clearance times than non-boosted individuals.Conclusions:SARS-CoV-2 viral kinetics are partly determined by immunity and variant but dominated by individual-level variation. Since booster vaccination protects against infection, longer clearance times for BA.1-infected, boosted individuals may reflect a less effective immune response, more common in older individuals, that increases infection risk and reduces viral RNA clearance rate. The shifting landscape of viral kinetics underscores the need for continued monitoring to optimize isolation policies and to contextualize the health impacts of therapeutics and vaccines.Funding:Supported in part by CDC contract #200-2016-91779, a sponsored research agreement to Yale University from the National Basketball Association contract #21-003529, and the National Basketball Players Association.

## Introduction

The viral kinetics of SARS-CoV-2 underlie the epidemiology of COVID-19 and the policies surrounding infection control. The amount and duration of viral shedding influences infectiousness (Ke et al., 2021; Ke et al., 2022; Marc et al., 2021; Marks et al., 2021; Puhach et al., 2022; Sun et al., 2021) and the duration of test positivity affect isolation policies, test recommendations, and clinical care guidelines (Hellewell et al., 2021; Kissler et al., 2021a; Larremore et al., 2021; Mack et al., 2022; Néant et al., 2021; Quilty et al., 2021; Singanayagam et al., 2022). Descriptions of viral kinetics are also important for establishing baselines to measure the effectiveness of antiviral drugs. For example, rebounds of viral RNA concentrations and symptoms have been observed after antiviral treatment, but it has been unclear to what extent such rebounds also occur in the absence of drug (Boucau et al., 2022b; Charness et al., 2022). Most longitudinal viral kinetics studies pre-date the emergence of the Omicron variant, which features dramatic antigenic divergence from prior variants, as well as the rollout of third and fourth vaccine doses (Lusvarghi et al., 2022; van der Straten et al., 2022). Early findings on viral kinetics therefore need to be updated to account for extensive and heterogeneous immune experience across the population (Cevik et al., 2021; Kissler et al., 2021b).

To characterize the viral kinetics of SARS-CoV-2 infection, including rebounds, for the Delta and Omicron (BA.1 lineages BA.1.1529 and BA.1.1) variants in symptomatic and asymptomatic individuals with varied vaccination and infection histories, we measured viral RNA levels using densely-sampled RT-qPCR tests from 1,280 SARS-CoV-2 infections, each taken by combined anterior nares and oral swabs, that occurred between 7th July, 2020, and 26th January, 2022, prior to the detection of BA.2.12.1, BA.4 and BA.5, or the regular detection of BA.2, in this cohort. As a proxy for immune response to SARS-CoV-2, we used antibody titers against the ancestral SARS-CoV-2 (WA1) strain spike protein measured prior to the administration of booster doses, but predominantly after primary vaccination.

We interpreted the data in two ways. First, we estimated the probability of an individual having a PCR cycle threshold (Ct) value less than 30, as a proxy for infectiousness, on each day post detection using a logistic regression model. Second, we estimated the peak viral RNA concentrations, viral RNA proliferation rate, and viral RNA clearance rate across variants, immune statuses and age using a semi-mechanistic model. Our findings provide key estimates for the duration and magnitude of viral RNA shedding in the upper respiratory tract and its variation across age, symptom status, variants, immune states, and individuals.

## Methods

### Study design

The data reported here represent a convenience sample including team staff, players, arena staff, vendors, and others affiliated with the NBA as described previously (Kissler et al., 2021a; Kissler et al., 2021b). The retrospective study includes samples collected between 7th July 2020 and 26th January 2022 (Appendix 1—figure 1). Clinical samples were obtained by combined swabs of the anterior nares and oropharynx, collected separately from each anatomical site, for each patient administered by a trained provider. Daily testing was required for most individuals prior to vaccination availability, with less frequent testing but close monitoring required after vaccination. Cycle threshold (Ct) values were generated using the Roche cobas target 1 assay. For the viral kinetics model analyses, Ct values were converted to viral genome equivalents using a standard curve (Kissler et al., 2021a).

We classified all individuals as having Ct value <30 or not on each day post-detection. This threshold was chosen based on a combination of antigen sensitivity and studies of virus culture by Ct, where the presence of culturable virus is often assumed to correlate with infectivity (Brihn et al., 2021; Bullard et al., 2020; Pilarowski et al., 2021; Singanayagam et al., 2020; Thommes et al., 2021). We stratified infections by those who had a negative or inconclusive test ≤1 day prior to detection and those whose last negative or inconclusive test was ≥2 days ago. We assumed that individuals testing negative at the end of an acute infection remained negative for the remainder of the study period, whereas those ending in a positive test are right-censored. Rebound trajectories were defined as any trajectory with a sequence of two or more consecutive Ct values ≥30 or negative tests after the initial peak followed by two or more consecutive Ct values <30. We considered more stringent definitions both for initial clearance (3+ or 4+ days of Ct ≥30 or negative test following initial peak) and subsequent rebound (3+ or 4+ days of Ct <30). In some instances, individuals were tested multiple times per day and thus for ease of model fitting we excluded 3,751 positive or inconclusive and 14,713 negative samples from repeat tests on the same day in our analyses, prioritizing the earliest test and then lowest Ct value test on each day.

Vaccination information was reported and verified by NBA staff and a clinical operational team. 828 individuals had been boosted by the time of their last PCR test, 529 had completed their primary vaccination course (two doses of an mRNA vaccine or one dose of Janssen / Ad.26.COV2.S adenovirus vector-based vaccine), 8 had received one vaccine dose, and 13 confirmed to be unvaccinated. The vaccination statuses of the remaining individuals were unknown. The time course of individual vaccination and exposure times is shown in Appendix 1—figure 2.

### Study oversight

In accordance with the guidelines of the Yale Human Investigations Committee, this work with de-identified samples was approved for research not involving human subjects by the Yale Institutional Review Board (HIC protocol # 2000028599). This project was designated exempt by the Harvard Institutional Review Board (IRB20-1407).

### Classification of infections

We tagged each series of positive tests buffered by at least 14 days of negative or missing tests on each side as a distinct infection. After an infection was flagged, subsequent positives were not classified as a new infection for 90 days. Isolated positive tests with no other positive within 14 days either side were not considered as detections. We track the cumulative number of exposures (defined as either receiving a vaccination or infection) over time. Individuals who received the Janssen/Ad.26.COV2.S adenovirus vector-based vaccine were counted as having received two vaccine doses. A total of 351 additional infections were reported to the program outside of the main testing regime, either through an external PCR or rapid antigen test, or from a positive antibody test result (not including the Diasorin Trimeric Assay results described below). We consider these detections as contributing towards an individual’s infection history but are unable to include them in the Ct value trajectory analyses.

### Genome sequencing and lineage assignment

RNA was extracted and confirmed as SARS-CoV-2 positive by RT-qPCR (Vogels et al., 2021). Next Generation Sequencing was performed with the Illumina COVIDSeq ARTIC viral amplification primer set (V4, 384 samples, cat# 20065135). Library preparation was performed using the amplicon-based Illumina COVIDseq Test v033 and sequenced 2×74 on Illumina NextSeq 550 following the protocol as described in Illumina’s documentation. The resulting FASTQs were processed and analyzed on Illumina BaseSpace Labs using the Illumina DRAGEN COVID Lineage Application; (BaseSpace Labs, 2021) versions included are 3.5.0, 3.5.1, 3.5.2, 3.5.3, and 3.5.4. The DRAGEN COVID Lineage pipeline was run with default parameters recommended by Illumina. Lineage assignment and phylogenetics analysis using the most updated version of Pangolin (Rambaut et al., 2020) and NextClade (Aksamentov and Neher, 2021), respectively. All sequenced Omicron infections were lineage BA.1 apart from 1 BA.2.10 infection. Sequenced Delta infections were a combination of lineages B.1.617.2 and AY.x.

There were 3 and 482 non-sequenced infections in the window of time when Alpha was replaced by Delta (29th May 2021 to 18th July 2021) and after the first detection of Omicron BA.1 (3rd December 2021 onwards), respectively (Appendix 1—figure 3). We removed these 485 infections from variant-specific analyses and assigned all non-sequenced infections prior to the detection of Omicron BA.1 to the dominant lineage at the time of detection (i.e. all infections prior to 29th May 2021 were assumed ‘Other’ and all infections between 18th July 2021 and 3rd December 2021 were assumed ‘Delta’). We removed all non-sequenced infections detected after 3rd December 2021 from variant-specific analyses rather than classifying them as Omicron BA.1 due to the continued presence of Delta. Omicron BA.2 was not regularly detected until after this period, with only one confirmed BA.2 infection (BA.2.10), which was removed from these analyses.

### Antibody titers

Individuals were tested with the Diasorin Trimeric Assay for IgG antibody titers against the ancestral SARS-CoV-2 (WA1) strain spike protein during the 2021 pre-season period (September-October 2021). The majority (>90%) of blood draws were from mid-September to early October 2021. We classified individuals with a titer of >250 AU/ml as being in the high titer group and in the low titer group otherwise, chosen based on its correlation with authentic virus neutralization results for wildtype and Delta (Liu et al., 2021; Wang et al., 2021). Specifically, an authentic virus neutralization titer of 100 was found to be well correlated with a 50% protective neutralization level for wildtype (Khoury et al., 2021) and found to correspond to a DiaSorin AU of 189.09 (95%CI: 147.61–235.75) (Appendix 1—figure 4). The cutoff of 250 was therefore chosen as a conservative upper bound classifying an individual as at lower risk of infection with Delta or wildtype SARS-CoV-2. Note that this cutoff does not predict infection risk with Omicron and was simply chosen as a proxy for an individual’s immune competence.

### Logistic regression models

We used the RStan package brms to fit Bayesian logistic regression models estimating the probability of having Ct value <30 on each day post detection, fitting all models to the frequent testing and delayed detection datasets separately (Bürkner, 2022). As a baseline, we considered a model without variant-specific effects, using smoothing splines to estimate the probability of having a Ct value less than 30 on each day post detection. We then fitted additional logistic regression models, adding additional spline terms and intercepts for the category-specific effect of age group (<30 years, 30–50 years and >50 years), vaccination status, cumulative number of previous exposures, days since previous exposure (categorized as naive, <1 month, 1–3 months and >3 months), and/or variant with days since detection. In models including variant, we considered the interaction of variant with exposure history, vaccination status or days since exposure category. We did not add an interaction between age group and any other variable. All models were fitted to the frequent testing and delayed detection group datasets separately.

We ranked models based on the expected log predictive density and evaluated their classification accuracy and area under the receiver operator curve using k-folds cross-validation (25 folds). For the antibody titer analyses, we fitted Bayesian logistic regression models for the probability of Ct value <30 as a function of days since detection, stratified by the interaction of titer group (above or below 250 AU/ml), age group, variant and vaccination status. Further details on the fitting process can be found in the Appendix 1.

### Viral kinetic model

We extended a previously reported model for capturing SARS-CoV-2 viral kinetics to estimate the viral proliferation time, viral clearance time, and peak viral load by variant and immune status (Kissler et al., 2021a; Kissler et al., 2021b). The model approximates viral kinetics on a logarithmic scale as a piecewise linear function, corresponding to an exponential increase of virus followed by an exponential clearance at possibly different rates. To estimate the relationship between booster status and viral kinetics, we first stratified the model by (1) Omicron boosted and (2) Omicron non-boosted individuals. There were too few boosted individuals who were infected with other variants to reliably fit the model to non-Omicron infections. Next, to estimate the relationship between antibody titer and viral kinetics, we stratified the model by (1) Delta infections with titer ≤250, (2) Delta infections with titer >250, (3) Omicron infections with titer ≤250 (4) Omicron infections with titer >250, and finally (5) non-Delta and non-Omicron infections in individuals who had not had any prior exposure either through infection or vaccination, to serve as a baseline. Stratification was accomplished by choosing a reference category (Omicron BA.1 non-boosted in the first analysis, non-Delta and non-Omicron infections without prior exposure in the second analysis) and fitting independent additive random effects for the other categories. Full details on the fitting procedure may be found in Kissler et al., 2021a; Kissler et al., 2021b and Appendix 1.

## Results

### Data

We initially identified 2,875 distinct infections from 2,678 individuals in this cohort (Appendix 1—figure 1). By the time of their final test, 2,460 (91.9%) individuals had one detected infection, 214 (7.99%) had two detected infections, three (0.11%) had three detected infections, and one (0.04%) had four detected infections. None of the individuals received antiviral treatment. A total of 587 infections were detected within 1 day of a prior negative PCR test result, and thus the timing of the onset of test positivity can be assumed with reasonable accuracy. We defined these infections as the ‘frequent testing’ group. The remaining 2,288 infections were detected 2 days or more from a previous negative test result or were detected with no prior negative test in the dataset. These were predominantly tests following suspected exposure, recent symptom onset, or periodic clearance for occupational health requirements, and thus we consider this latter group of detections as a reasonable proxy for infection detection in the absence of frequent testing, which is the case for most populations. We define these infections as the ‘delayed detection’ group.

Of 1086 infections with known symptom status, 766 reported symptoms at some point during the infection (70.5%). Individuals in the delayed detection group were more likely to be symptomatic than in the frequent testing group (73.1% vs 64.9%; Chi-squared test statistic = 5.03; p-value <0.05). Most symptomatic individuals were detected around the time of symptom onset (Appendix 1—figure 5; median delay from detection to symptom onset of zero days (N=553) in the delayed detection group and one day (N=171) in the frequent testing group). Symptom onset preceded the peak measured Ct value by a median of two days (N=550) in the delayed detection group and three days (N=171) in the frequent testing group (Appendix 1—figure 6).

Based on genome sequencing, 1,561 infections were confirmed to be Omicron (one BA.2.10 isolate, the rest were lineages within BA.1), 266 confirmed to be Delta, and 247 confirmed as other lineages. An additional 801 infections were not sequenced; however, due to the rapid replacement of the circulating lineage in this cohort, we classified many of these as suspected Delta or other lineages based on the dominant variant at time of detection (Appendix 1—figure 3). We excluded non-sequenced samples following the detection of Omicron BA.1 due to the continued, albeit low-level, detection of Delta (N=490).

For further analysis, we reduced the dataset to a subset of 1,280 well-documented infections. Beginning with the 2,875 infections, we removed those with an unknown lineage (n=490) and one Omicron BA.2 infection, those with only binary test results (positive/negative but no Ct values; n=21), those for which all Ct-based tests results were beyond 25 days after the time of first detection (n=12), and those for which the vaccination status was missing (1,071). Characteristics of these infections are listed in Table 1.

**Table 1.**
 Characteristics of the documented infections.Counts (N) correspond to numbers of infections.


<table>
  <thead>
    <tr>
      <th>Variable</th>
      <th>Category</th>
      <th>N</th>
      <th>Percent</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Total</td>
      <td>–</td>
      <td>1280</td>
      <td>100</td>
    </tr>
    <tr>
      <td>Variant</td>
      <td>Delta</td>
      <td>180</td>
      <td>14.1</td>
    </tr>
    <tr>
      <td></td>
      <td>Omicron BA.1</td>
      <td>878</td>
      <td>68.6</td>
    </tr>
    <tr>
      <td></td>
      <td>Other</td>
      <td>222</td>
      <td>17.3</td>
    </tr>
    <tr>
      <td rowspan="4">Vaccination Status</td>
      <td>Unvaccinated</td>
      <td>228</td>
      <td>17.8</td>
    </tr>
    <tr>
      <td>First dose</td>
      <td>6</td>
      <td>0.5</td>
    </tr>
    <tr>
      <td>Second dose</td>
      <td>420</td>
      <td>32.8</td>
    </tr>
    <tr>
      <td>Boosted</td>
      <td>626</td>
      <td>48.9</td>
    </tr>
    <tr>
      <td rowspan="3">Antibody Titer</td>
      <td>13–250</td>
      <td>473</td>
      <td>37.0</td>
    </tr>
    <tr>
      <td>250–800</td>
      <td>504</td>
      <td>39.4</td>
    </tr>
    <tr>
      <td>Unknown</td>
      <td>303</td>
      <td>23.7</td>
    </tr>
    <tr>
      <td rowspan="3">Symptomatic</td>
      <td>No</td>
      <td>257</td>
      <td>20.1</td>
    </tr>
    <tr>
      <td>Yes</td>
      <td>664</td>
      <td>51.9</td>
    </tr>
    <tr>
      <td>Unknown</td>
      <td>359</td>
      <td>28</td>
    </tr>
    <tr>
      <td rowspan="2">Detection Speed</td>
      <td>Delayed detection</td>
      <td>877</td>
      <td>68.5</td>
    </tr>
    <tr>
      <td>Frequent testing</td>
      <td>403</td>
      <td>31.5</td>
    </tr>
    <tr>
      <td rowspan="4">Age Group</td>
      <td>0–30</td>
      <td>556</td>
      <td>43.4</td>
    </tr>
    <tr>
      <td>31–50</td>
      <td>568</td>
      <td>44.4</td>
    </tr>
    <tr>
      <td>50+</td>
      <td>155</td>
      <td>12.1</td>
    </tr>
    <tr>
      <td>Unknown</td>
      <td>1</td>
      <td>0.1</td>
    </tr>
    <tr>
      <td rowspan="4">Cumulative Infection Number</td>
      <td>1</td>
      <td>1128</td>
      <td>88.1</td>
    </tr>
    <tr>
      <td>2</td>
      <td>149</td>
      <td>11.6</td>
    </tr>
    <tr>
      <td>3</td>
      <td>2</td>
      <td>0.2</td>
    </tr>
    <tr>
      <td>4</td>
      <td>1</td>
      <td>0.1</td>
    </tr>
    <tr>
      <td rowspan="4">Days Since Previous Exposure</td>
      <td>Naïve (no prior exposure)</td>
      <td>220</td>
      <td>17.2</td>
    </tr>
    <tr>
      <td>&lt;1 month</td>
      <td>273</td>
      <td>21.3</td>
    </tr>
    <tr>
      <td>1–3 months</td>
      <td>403</td>
      <td>31.5</td>
    </tr>
    <tr>
      <td>&gt;3 months</td>
      <td>384</td>
      <td>30.0</td>
    </tr>
  </tbody>
</table>

### Interpersonal variation in viral RNA trajectories

Viral trajectories varied substantially across individuals regardless of variant (Figure 1A). To characterize the probability of an individual remaining potentially infectious on each day following detection, defined as having a Ct <30, we fitted a logistic regression model with a smoothing spline on days since detection as a predictor (more complex models are considered below). We fit this model to the frequent testing and delayed detection groups separately (Appendix 1—figure 7). Most individuals (posterior mean: 65.4%, 95% credible intervals [CrI]: 62.0–68.8%) in the frequent testing group remained potentially infectious on day 5 post detection. This fraction decreased to 20.0% (95% CrI: 17.3–22.8%) at day 10. In the delayed detection group, fewer individuals remained potentially infectious at days 5 and 10, likely because they were detected later in their infection. In this group, the proportion with Ct <30 was 51.0% (95% credible interval (CrI): 48.3–53.6%) on day 5 post detection and 9.37% (95% CrI: 7.98–10.9%) on day 10.

![Figure 1.](https://cdn.elifesciences.org/articles/81849/elife-81849-fig1-v2.jpg)

**Figure 1.:** (A) PCR Ct value trajectories for each acute Delta (red), Omicron BA.1 (blue), and other (black) infection. Individuals are grouped by the gap between detection and their most recent negative or inconclusive PCR test (Frequent testing vs. Delayed detection). Thick lines depict the mean Ct value over time, counting negative tests as Ct = 40. Thin lines depict individual level Ct values over time. The horizontal dotted lines mark Ct = 30, which we consider here as a proxy for possible infectiousness and antigen test positivity. (B) Subsets of PCR Ct value trajectories that were classified as rebounds, stratified by testing frequency group. Rebounds are defined here as any trajectory with an initial Ct value <30, followed by a sequence of two or more consecutive negative tests or tests with Ct value ≥30, and subsequently followed by two or more consecutive tests with Ct value <30.

### Incidence of rebounds

We next characterized the frequency of rebound viral RNA trajectories in this cohort. Viral rebounds may be characterized by the duration of the “quiescent” period of low viral concentration between distinct peaks, the duration of the subsequent rebound, and the timing of rebound onset relative to infection, but no consensus definition of viral rebound based on these quantities exists. We defined rebound as any viral trajectory with a decline in Ct value to <30 for 3+consecutive days of tests (the rebound) after 3+consecutive days of tests with Ct ≥30 or a negative result (the quiescent period) following an initial Ct value <30 (the first detection of infection). Testing often ceased following initial clearance, and thus to minimize the impact of right censoring we only considered those trajectories with at least three days of tests with negative or Ct ≥30 following a Ct value <30 as the denominator (N=999). We detected seven viral rebounds under this definition. Less stringent definitions led to more rebound classifications. For example, 40 (3.00%) of 1,334 infections were identified as rebounds when only 2+consecutive days of Ct ≥30 followed by 2+days of Ct <30 was required to be classified as such (Table 2; Figure 1B). All individual-level viral trajectories classified as rebounds under this less stringent definition are shown in Appendix 1—figure 8 Under this definition, we found that rebound infections were more likely in Omicron BA.1 infections, with 36 (4.10%; N=877) Omicron BA.1 infections resulting in rebound compared to one (0.562%; N=178) and three (1.08%; N=279) Delta and other infections, respectively (Appendix 1—table 1; Chi-squared test for Omicron BA.1 (N=877) vs. non-Omicron BA.1 infection (N=457), test statistic = 9.69, P-value <0.05). Similarly, we found that rebounds were more common in boosted individuals, with 32 (6.48%; N=494) rebounds in boosted individuals vs. three (0.929%; N=323) and two (1.26%; N=159) rebounds in vaccinated and unvaccinated individuals, respectively (Appendix 1—table 2; Chi-squared test for boosted (N=494) vs. not-boosted (N=478) infection, test statistic = 18.1, P-value <1e-4).

**Table 2.**
 Number of rebound infections classified under different definitions for initial clearance and subsequent rebound.


<table>
  <thead>
    <tr>
      <th>Initial clearance duration (consecutive days with Ct ≥30)</th>
      <th>Rebound duration (days above Ct value threshold)</th>
      <th>Ct value threshold of rebound</th>
      <th>Rebounds</th>
      <th>Total</th>
      <th>Percentage</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>≥4</td>
      <td>≥4</td>
      <td>Ct &lt;30</td>
      <td>0</td>
      <td>749</td>
      <td>0.00%</td>
    </tr>
    <tr>
      <td>≥4</td>
      <td>≥3</td>
      <td>Ct &lt;30</td>
      <td>1</td>
      <td>749</td>
      <td>0.13%</td>
    </tr>
    <tr>
      <td>≥4</td>
      <td>≥2</td>
      <td>Ct &lt;30</td>
      <td>4</td>
      <td>749</td>
      <td>0.53%</td>
    </tr>
    <tr>
      <td>≥3</td>
      <td>≥4</td>
      <td>Ct &lt;30</td>
      <td>2</td>
      <td>999</td>
      <td>0.20%</td>
    </tr>
    <tr>
      <td>≥3</td>
      <td>≥3</td>
      <td>Ct &lt;30</td>
      <td>7</td>
      <td>999</td>
      <td>0.70%</td>
    </tr>
    <tr>
      <td>≥3</td>
      <td>≥2</td>
      <td>Ct &lt;30</td>
      <td>16</td>
      <td>999</td>
      <td>1.60%</td>
    </tr>
    <tr>
      <td>≥2</td>
      <td>≥4</td>
      <td>Ct &lt;30</td>
      <td>7</td>
      <td>1334</td>
      <td>0.53%</td>
    </tr>
    <tr>
      <td>≥2</td>
      <td>≥3</td>
      <td>Ct &lt;30</td>
      <td>18</td>
      <td>1334</td>
      <td>1.35%</td>
    </tr>
    <tr>
      <td>≥2</td>
      <td>≥2</td>
      <td>Ct &lt;30</td>
      <td>40</td>
      <td>1334</td>
      <td>3.00%</td>
    </tr>
    <tr>
      <td>≥4</td>
      <td>≥4</td>
      <td>Ct &lt;25</td>
      <td>0</td>
      <td>749</td>
      <td>0.00%</td>
    </tr>
    <tr>
      <td>≥4</td>
      <td>≥3</td>
      <td>Ct &lt;25</td>
      <td>0</td>
      <td>749</td>
      <td>0.00%</td>
    </tr>
    <tr>
      <td>≥4</td>
      <td>≥2</td>
      <td>Ct &lt;25</td>
      <td>0</td>
      <td>749</td>
      <td>0.00%</td>
    </tr>
    <tr>
      <td>≥3</td>
      <td>≥4</td>
      <td>Ct &lt;25</td>
      <td>1</td>
      <td>999</td>
      <td>0.10%</td>
    </tr>
    <tr>
      <td>≥3</td>
      <td>≥3</td>
      <td>Ct &lt;25</td>
      <td>1</td>
      <td>999</td>
      <td>0.10%</td>
    </tr>
    <tr>
      <td>≥3</td>
      <td>≥2</td>
      <td>Ct &lt;25</td>
      <td>2</td>
      <td>999</td>
      <td>0.20%</td>
    </tr>
    <tr>
      <td>≥2</td>
      <td>≥4</td>
      <td>Ct &lt;25</td>
      <td>1</td>
      <td>1334</td>
      <td>0.08%</td>
    </tr>
    <tr>
      <td>≥2</td>
      <td>≥3</td>
      <td>Ct &lt;25</td>
      <td>2</td>
      <td>1334</td>
      <td>0.15%</td>
    </tr>
    <tr>
      <td>≥2</td>
      <td>≥2</td>
      <td>Ct &lt;25</td>
      <td>5</td>
      <td>1334</td>
      <td>0.38%</td>
    </tr>
  </tbody>
</table>

### Minimal differences across variants and vaccination histories in the probability of having low Ct values over time

To assess differences in the duration of test positivity and infectiousness by age, variant and immune status, we modeled the probability of an individual having Ct <30 on each day since detection. As a baseline model, we fitted a logistic regression model with a smoothing spline on days since detection as a predictor. We then fitted successively more complex models, adding independent category-specific smoothing splines for the interaction of age group (categorized as <30, 30–50 or >50 years old), variant, and exposure history with days since detection (factorized), and compared their predictive accuracy using k-fold cross-validation. All models were fit to the frequent testing and delayed detection datasets separately.

The best-performing model for predicting the time course of low Ct values included days since detection stratified by the cumulative number of previous exposures (infection or vaccination) and its interaction with variant, as well as age group (Appendix 1—table 3 and Appendix 1—table 4). This indicates that the variation in low Ct values over time is better captured by models that account for exposure history and age group than by models that account for time since detection alone. However, the models stratified by vaccination status or days since previous exposure in addition to variant and age group were also highly ranked, and the differences in classification accuracy among all of the models was small. The baseline model, which included only the number of days since detection as a predictor, gave an overall classification accuracy for an individual having Ct <30 or ≥30/negative of 81.7% with an AUC of 88.6% (group-level classification accuracies: Ct <30 = 60.6%; Ct ≥30/negative = 89.0%) for the frequent testing group, and an overall classification accuracy of 84.2% with an AUC of 90.5% (Ct <30 = 72.2%; Ct ≥30/negative = 88.0%) in the delayed detection group. In contrast, the best model, which included the cumulative number of exposures, variant and age, gave an overall classification accuracy of 82.8% with an AUC of 89.7% (Ct <30 = 64.7%; Ct ≥30/negative = 89.0%) for the frequent testing group and an overall classification accuracy of 85.0% with an AUC of 91.4% (Ct <30 = 71.2%; Ct ≥30/negative = 89.3%) in the delayed detection group. These results indicate that while exposure histories help to explain mean viral RNA kinetics, they provide little assistance in predicting an individual’s course of infectiousness over time, due to a high degree of individual-level variation, which may be dominated by stochastic effects or other unmeasured characteristics.

Vaccination provides multiple layers of protection against SARS-CoV-2, leading to reduced rates of infection (Tai et al., 2022) and faster clearance of the virus (Kissler et al., 2021b). Consistent with these findings, individuals who received two vaccine doses prior to infection with pre-Delta and pre-Omicron variants (N=12) cleared to negative results or high Ct values faster than unvaccinated individuals (N=209) (Appendix 1—figure 9). While boosting reduced rates of infection in our cohort,(Tai et al., 2022) boosted individuals with Omicron BA.1 infections (N=615) tended to sustain low Ct values for longer durations than individuals who had only undergone an initial vaccine course (N=251), defined as either two doses of an mRNA vaccine or a single dose of the Ad.26.COV2.S adenovirus vector-based vaccine (Figure 2A; Appendix 1—figure 9). This pattern was robust to refitting the model after excluding player infections, resulting in a subpopulation more representative of the general population in age and health status (Appendix 1—figure 10). We also found similar patterns after subsetting infections by their symptom status (Appendix 1—figure 11).

![Figure 2.](https://cdn.elifesciences.org/articles/81849/elife-81849-fig2-v2.jpg)

**Figure 2.:** Shown are the marginal effects of (A) vaccination status and (B) age group on the proportion of individuals with Ct <30 on each day post detection after conditioning on being an Omicron BA.1 infection and (A) <30 years old (B) boosted at the time of infection. Solid colored lines and shaded ribbons show the posterior mean (solid line) and 95% credible intervals (shaded ribbon) of each conditional effect. Dotted horizontal and vertical lines mark 5% probability and day 5 post detection, respectively.

It is important to consider the possible confounding effect of age, as boosted individuals in this cohort were typically older than non-boosted individuals at the time of BA.1 infection (mean age of 37.6 years in the BA-1 infected, boosted group vs. 31.3 years in the BA.1-infected, non-boosted group). The regression model including age group, vaccination status and variant found that older individuals do maintain Ct <30 for longer on average than younger individuals after conditioning on vaccination status (Figure 2B). However, the effect of a higher proportion with Ct <30 in boosted individuals relative to non-boosted individuals also remained within each age group, suggesting that both older age and booster status explain some variation in duration of Ct <30 (Appendix 1—figure 12). Furthermore, models including age were almost universally better supported in the model comparison analysis and provided improvements in classification accuracy, but in both cases the gains were small (Appendix 1—table 3 and Appendix 1—table 4).

### Pre-Omicron antibody titer explains variation in viral RNA clearance

To assess the mechanisms behind the unexpected slower clearance in boosted Omicron BA.1 infections, we analyzed viral kinetics stratified by antibody titer. In addition to exposure history information, 979 individuals were tested at least once (1,017 measurements total) with the Diasorin Trimeric Assay for antibody titers against the spike protein from the ancestral SARS-CoV-2 (WA1) strain (Appendix 1—figure 13). Most titers were obtained from mid-September to mid-October 2021, and thus we consider these titers to represent an individual’s post primary vaccination course response rather than post-boost/post-Omicron infection immunity (Appendix 1—figure 2). The median time between the most recent vaccine dose and the titer draw was 162 days (interquartile range: 129–180 days) (Appendix 1—figure 14).

We hypothesized that these single point-in-time SARS-CoV-2 antibody titer measurements represented a proxy of the strength of the immune response to SARS-CoV-2 and thus would be reflected in the features of viral kinetics over the course of infection. A total of 494 measurements were classified as low antibody titers (≤250 arbitrary units [AU]/ml) and 523 as high titers (>250 AU/ml). This cutoff was chosen as a conservative upper bound for defining risk of Delta infection.

We fitted a logistic regression model for the probability of having Ct <30 on each day since detection, stratified by the interaction of an individual’s booster status and their pre-booster antibody titer status, as well as an additional stratification by age group (Figure 3A). Boosted individuals with a low antibody titer had the highest and longest duration of Ct <30 over time since detection in both the frequent testing and delayed detection group. In the delayed detection group, individuals with low antibody titers were more likely to have Ct <30 than individuals with high antibody titers regardless of booster status, though boosted individuals with high antibody titers maintained Ct <30 for longer than non-boosted individuals with low titers.

![Figure 3.](https://cdn.elifesciences.org/articles/81849/elife-81849-fig3-v2.jpg)

**Figure 3.:** (A) Proportion of Omicron BA.1 infections with Ct value <30 on each day post detection, stratified by age group and the interaction of booster status at the time of infection and antibody titer group. Shown are posterior estimates from a generalized linear model predicting probability of Ct <30 with a spline term on days since detection, conditional on titer/vaccination status category and age group. Solid lines show posterior mean and shaded ribbons show 95% credible intervals of each conditional effect. (B) Distribution of measured antibody titers (colored points) stratified by variant and vaccination status of each detected infection, with mean titers (horizontal lines) and bootstrapped 95% confidence intervals (CIs) shown in text. Note that the 95% CIs are very small relative to the range and are thus not plotted. Grey bars are histograms of antibody titer counts in bins of 10 arbitrary units (AU)/ml. Note also that stratification is by infection event and not individual, and that antibody titers were measured at a single point in time rather than near the time of infection. The Diasorin Trimeric Assay values are truncated between 13 and 800 AU/ml.

The results were consistent with an age group-level effect also contributing towards differences in the proportion of individuals with Ct <30 over time. Trends were similar within each age group, but we note that at this level of stratification the sample sizes for some subgroups are small and thus there is considerable uncertainty for some combinations of age group, titer group, and vaccination status. We found that younger BA.1-infected individuals had higher antibody titers on average than older BA.1-infected individuals, but that BA.1-infected boosted individuals had consistently lower mean antibody titers than BA.1-infected non-boosted individuals within each age group (Appendix 1—figure 15).

To account for potential confounding from waning immunity, in which low titers simply represent a longer time since previous exposure, we restricted the dataset to include only individuals who had their titer measured within 100–200 days of a previous exposure with the aim of comparing antibody titers measured at a similar point in the waning process. We also repeated the analysis after restricting to only infections detected 60–90 days following an antibody titer measurement, here aiming to include only infections for which the measured titer reasonably proxies the titer at the time of infection. These time windows were chosen to improve comparability of immune states while also retaining reasonably large sample sizes. The trend of a higher and longer duration of Ct <30 in Omicron BA.1-infected, boosted, low titer individuals was maintained in both sensitivity analyses (Appendix 1—figure 16).

Based on these findings, we hypothesized that boosted individuals who nevertheless were infected with Omicron BA.1 may have had relatively poor BA.1-specific immune responses to prior SARS-CoV-2 exposures, leading to longer infection durations. This is demonstrated by stratifying antibody titers by variant and vaccination status at the time of infection (Figure 3B). Antibody titers were lower among fully vaccinated individuals who were subsequently infected with Delta than individuals who had been infected with a pre-Delta variant. This suggests that individuals with a high antibody titer at around the time of Delta circulation were less likely to be infected with Delta. In contrast, we found that mean antibody titers among Omicron BA.1-infected, fully vaccinated individuals were similar to individuals in the pre-Delta, unvaccinated group, suggesting that higher titer individuals were not substantially less likely to be infected than lower titer individuals. Finally, we found that antibody titers were lowest among Omicron BA.1 infected boosted individuals, suggesting that individuals with a high titer measurement prior to being boosted were less likely to have Omicron BA.1 infections.

### The effect of immune status and variant on viral proliferation, peak viral RNA titers, and clearance

We next adapted a framework to estimate the impact of antibody titer, vaccination status, and variant on peak viral RNA concentrations, proliferation phase duration, and clearance duration (Figure 4; Kissler et al., 2021a; Kissler et al., 2021b). According to the viral kinetic model, and among Omicron BA.1 infections, boosted individuals had a longer estimated viral clearance time than non-boosted individuals (8.4 days (95% CrI: 8.0–8.7) vs. 6.2 days (95% CrI: 5.8–6.6), respectively), in line with the results from the logistic regression model. Viral proliferation times and peak viral RNA were similar among boosted and non-boosted individuals with Omicron BA.1 infections (Appendix 1—table 5). When stratifying by post-initial vaccination antibody titer, Delta infections featured a consistently higher peak viral RNA than Omicron BA.1 infections. Among Omicron BA.1 infections, high antibody titers were associated with faster viral clearance times and lower peak viral RNA. Proliferation times were similar across variants and titers (Appendix 1—table 6).

![Figure 4.](https://cdn.elifesciences.org/articles/81849/elife-81849-fig4-v2.jpg)

**Figure 4.:** Points depict measured Ct values, lines depict the estimated population mean viral trajectories, and shaded regions depict the 95% credible intervals for the estimated population viral trajectories. (A) Non-Delta and non-Omicron infections in individuals who were previously unexposed (no prior record of vaccination or infection), (B) Delta infections with titer ≤250, (C) Delta infections with titer >250, (D) Omicron BA.1 infections with titer ≤250, (E) Omicron BA.1 infections with titer >250. Peak viral loads were higher for Delta infections than for Omicron BA.1 infections when stratifying by titer (i and ii), and titers ≤250 were associated with higher viral loads when stratifying by variant (iii and iv). Low titers were also associated with longer clearance times (v and vi).

We fitted the viral RNA kinetic model to Omicron BA.1 infections after stratifying individuals based on their symptom status as well as vaccination status or antibody titer group. We found the same pattern of longer clearance times for boosted individuals relative to fully vaccinated individuals, with symptomatic boosted individuals demonstrating longer clearance times than asymptomatic boosted individuals (Appendix 1—table 7). Among those with low antibody titer, presence of symptoms was associated with higher peak viral RNA and longer clearance times, while for those with high antibody titer, peak viral RNA and clearance times were similar between symptom statuses (Appendix 1—table 8).

Finally, we fitted the models allowing for BA.1 viral RNA kinetics to vary by age in addition to vaccination status or antibody titer. Consistent with the logistic regression results, older individuals demonstrated longer average clearance times than younger individuals across vaccination and antibody titer groups. When stratifying by immune status, individuals aged 50+years took between roughly 1–2 days longer to clear than individuals aged 30–50, and 2–3 days longer to clear than individuals under 30 (Appendix 1—table 9 and Appendix 1—table 10). However, we still found a consistent effect of antibody titer and booster status on clearance time despite this additional age effect. Individuals with low antibody titer and boosted individuals took 1–2 days longer to clear than individuals with high antibody titer and non-boosted individuals in both the <30 and 30–50 year age groups (Appendix 1—table 9 and Appendix 1—table 10).

## Discussion

We found that individuals infected with SARS-CoV-2 often had Ct values <30 beyond the five-day isolation period following SARS-CoV-2 infection currently recommended by the CDC (Centers for Disease Control and Prevention, 2022). This finding is in line with other studies measuring Ct values from upper respiratory tract samples, the duration of antigen test positivity, and the duration of infectious viral load or culturable virus (Boucau et al., 2022a; Earnest et al., 2022; Ke et al., 2022; Landon et al., 2022; Lefferts et al., 2022). While we do not have data on infectiousness by day to clarify the exact link between Ct and infectiousness, nearly half of the individuals in this cohort had potentially infectious viral loads (Ct <30) five days after their initial detection, even in those detected later in their infection course (Singanayagam et al., 2020). By day 10, the number of individuals with Ct <30 was substantially reduced but still high. The duration of positivity was highly variable across individuals, and low Ct values consistent with potential infectiousness were sometimes maintained for up to two weeks. These observations suggest the use of test-based, rather than time-based, protocols for defining the duration of isolation to limit the spread of SARS-CoV-2.

Rebounds with recurrence of symptoms and positive rapid antigen tests after a period of negative test results have been increasingly reported in individuals treated with SARS-CoV-2 antiviral drugs (Boucau et al., 2022b; Charness et al., 2022), but estimates for the frequency of viral rebounds in the absence of antiviral treatment have been lacking. Among infected boosted individuals in this cohort, who were predominantly infected with Omicron BA.1, we detected seven rebounds in viral trajectory, stringently defined as any Ct value trajectory with at least three consecutive days of negative tests or tests with Ct ≥30 after the initial peak followed by 3threeor more consecutive days with Ct <30. However, more rebounds were detected when using less stringent Ct value-based definitions and were more frequent in Omicron BA.1-infected or boosted individuals, occurring in ~6% of infections in contrast to ~1% of infections in the pre-booster pre-Omicron phase of the pandemic. It was not routine for testing to continue following suspected clearance in this cohort, and thus these results may represent a lower bound on the incidence of rebound infections. The frequency of viral trajectory rebounds depends on the definition of ‘rebound’, highlighting the need for standardized definitions to enable comparisons across studies. We did not measure the recurrence of culturable virus during these resurgent low Ct periods, and thus further work is needed to understand if viral RNA rebounds are a reliable proxy for infectivity. Moreover, we did not have sufficient information to define rebounds with respect to clearance and recurrence of symptoms, though the experience of the occupational health team is that rebounds of a clinical nature have been extremely rare, with only one documented case (Mack et al., 2021). Overall, these findings suggest that symptom monitoring after clearing isolation may be warranted, and a return to isolation may be necessary for individuals with rebound infections (Charness et al., 2022).

Boosted individuals in this cohort were less likely to be infected with Omicron BA.1, (Tai et al., 2022) and those who had a breakthrough infection tended to have a low antibody titer measurement to the WA1 spike protein after their initial vaccine course. In this context, test positivity following Omicron BA.1 infection lasted longer for boosted individuals than for non-boosted individuals, regardless of symptom status. This observation was further supported by a viral kinetic model that found longer clearance times for Omicron BA.1 infections in boosted relative to non-boosted individuals. Moreover, high antibody titers to the WA1 spike protein were associated with lower peak viral RNA concentrations and faster clearance times for both Delta and Omicron BA.1 infections. Together, these results suggest that the low antibody titers in infected boosted individuals conferred increased risk for infection as well as slower control and clearance of infection.

The effect of age on viral kinetics complicates the interpretation of these findings. Prior to the detection of Omicron BA.1, older individuals have been found to take longer to clear infection on average than younger individuals (Caputo et al., 2021; Cevik et al., 2021; Jones et al., 2021; Long et al., 2021; Néant et al., 2021; Singanayagam et al., 2022). However, these findings are not unequivocal, as a previous systematic review found the effect of age on viral kinetics was diminished after accounting for disease severity (Chen et al., 2021). Our data support an effect of age on viral clearance times, with longer times from peak to clearance in individuals >50 years compared to those <30 years regardless of variant and immune state. In this cohort, older individuals were more likely to be boosted prior to becoming infected with BA.1 than younger individuals, and thus the finding of delayed clearance in BA.1-infected, boosted individuals can be partially attributed to delayed clearance in older individuals. However, we found consistent delayed clearance in boosted relative to non-boosted individuals within each age group, notably in the <30 years group. Furthermore, the pattern of lower antibody titers to WA1 spike in BA.1-infected, boosted individuals relative to BA.1-infected, non-boosted individuals was also consistent within each age group, suggesting that low WA1 spike titers correlate with increased infection risk and slower clearance in addition to any age-specific effects.

An important limitation of this study is that the cohort is not representative of the general population, as it is predominately male, young, and includes professional athletes. However, our key findings were preserved in analyses after excluding the players. We did not test for the presence of infectious virus, and our findings are based on Ct values obtained from combined nasal and oropharyngeal swabs.(Ke et al., 2022) While low Ct values have been associated with potential infectiousness and antigen test positivity (Bullard et al., 2020; Jaafar et al., 2021; Jefferson et al., 2020; Singanayagam et al., 2020), this is an imperfect proxy. It is possible that some infections were undetected, and thus the reported number of prior infections should be interpreted as a lower bound for each member of the cohort. SARS-CoV-2 antibody titers were only measured from mid-September to mid-October 2021 and were taken at varying time points after initial vaccination course (between 0 and 290 days), so we could not assess the relationship between antibody waning and viral kinetics. Antibody titers were measured against the spike protein of the WA1 lineage, which correlate poorly with protection against the antigenically distinct Omicron lineages; thus, it is unclear how these data are associated specifically to Omicron-immunity, beyond representing a proxy for overall immune response.

Variants and immune statuses interact, sometimes in unexpected ways, to produce viral kinetics that differ in duration and intensity. Collecting longitudinal viral load data in more diverse cohorts will help to ensure that isolation and quarantine policies are based on the best available evidence and will help to properly contextualize results from ongoing drug and vaccine trials. Similarly, our findings suggest that SARS-CoV-2 control measures may be better informed by measurements of immune status than proxies such as number or timing of receipt of vaccine doses or of infections. Testing this hypothesis will require widespread collection and analysis of serological, infection, and vaccination data in diverse cohorts and broader availability of quantitative antibody tests designed for the spike protein of Omicron lineages.
