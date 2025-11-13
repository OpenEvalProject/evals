# Association of close-range contact patterns with SARS-CoV-2: a household transmission study

## Authors

- Jackie Kleynhans<sup>2</sup> ([ORCID: 0000-0001-7081-6273](https://orcid.org/0000-0001-7081-6273)) †
- Lorenzo Dall'Amico<sup>4</sup> ([ORCID: 0000-0002-7493-6421](https://orcid.org/0000-0002-7493-6421))
- Laetitia Gauvin<sup>4</sup>
- Michele Tizzoni<sup>4</sup>
- Lucia Maloma<sup>7</sup>
- Sibongile Walaza<sup>2</sup>
- Neil A Martinson<sup>7</sup>
- Anne von Gottberg<sup>2</sup> ([ORCID: 0000-0002-0243-7455](https://orcid.org/0000-0002-0243-7455))
- Nicole Wolter<sup>2</sup>
- Mvuyo Makhasi<sup>2</sup>
- Cheryl Cohen<sup>2</sup>
- Ciro Cattuto<sup>4</sup>
- Stefano Tempia<sup>2</sup>
- Amelia Buys

### Affiliations

1. Centre for Respiratory Diseases and Meningitis, National Institute for Communicable Diseases of the National Health Laboratory Service Johannesburg South Africa
2. Centre for Respiratory Diseases and Meningitis, National Institute for Communicable Diseases of the National Health Laboratory Service Johannesburg South Africa
3. School of Public Health, Faculty of Health Sciences, University of the Witwatersrand Johannesburg South Africa ([ROR:03rp50x72](https://ror.org/03rp50x72))
4. ISI Foundation Turin Italy ([ROR:03ebhsy64](https://ror.org/03ebhsy64))
5. Institute for Research on Sustainable Development Aubervilliers France ([ROR:05q3vnk25](https://ror.org/05q3vnk25))
6. Department of Sociology and Social Research, University of Trento Trento Italy ([ROR:05trd4x28](https://ror.org/05trd4x28))
7. Perinatal HIV Research Unit, University of the Witwatersrand Johannesburg South Africa ([ROR:03rp50x72](https://ror.org/03rp50x72))
8. Johns Hopkins University Center for TB Research Baltimore United States ([ROR:00za53h95](https://ror.org/00za53h95))
9. School of Pathology, Faculty of Health Sciences, University of the Witwatersrand Johannesburg South Africa ([ROR:03rp50x72](https://ror.org/03rp50x72))
10. Department of Informatics, University of Turin Turin Italy ([ROR:048tbm396](https://ror.org/048tbm396))

† Corresponding author

## Abstract

Background:Households are an important location for severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) transmission, especially during periods when travel and work was restricted to essential services. We aimed to assess the association of close-range contact patterns with SARS-CoV-2 transmission.Methods:We deployed proximity sensors for two weeks to measure face-to-face interactions between household members after SARS-CoV-2 was identified in the household, in South Africa, 2020–2021. We calculated the duration, frequency, and average duration of close-range proximity events with SARS-CoV-2 index cases. We assessed the association of contact parameters with SARS-CoV-2 transmission using mixed effects logistic regression accounting for index and household member characteristics.Results:We included 340 individuals (88 SARS-CoV-2 index cases and 252 household members). On multivariable analysis, factors associated with SARS-CoV-2 acquisition were index cases with minimum Ct value <30 (aOR 16.8 95% CI 3.1–93.1) vs >35, and female contacts (aOR 2.5 95% CI 1.3–5.0). No contact parameters were associated with acquisition (aOR 1.0–1.1) for any of the duration, frequency, cumulative time in contact, or average duration parameters.Conclusions:We did not find an association between close-range proximity events and SARS-CoV-2 household transmission. Our findings may be due to study limitations, that droplet-mediated transmission during close-proximity contacts plays a smaller role than airborne transmission of SARS-CoV-2 in the household, or due to high contact rates in households.Funding:Wellcome Trust (Grant number 221003/Z/20/Z) in collaboration with the Foreign, Commonwealth, and Development Office, United Kingdom.

## Introduction

South Africa has experienced five waves of SARS-CoV-2 infection, with over 4 million laboratory-confirmed cases by August 2022 (National Institute for Communicable Diseases, 2022a). The true burden is highly underestimated, since based on seroprevalence data, after the third wave of infection, 43 to 83% of the 59.5 million South African inhabitants had already been infected, varying by age and setting (Kleynhans et al., 2022a; Bingham et al., 2022).

SARS-CoV-2 transmission is mainly via the respiratory route, through both droplet-mediated and airborne transmission (Meyerowitz et al., 2021; Wang et al., 2021). Infection from contaminated surfaces has also been described (Meyerowitz et al., 2021). Although infection risk is highest in symptomatic individuals (Madewell et al., 2020), with the most infectious period one day before symptom onset (Meyerowitz et al., 2021), asymptomatic individuals can still transmit SARS-CoV-2 (Liu, 2019; Cohen et al., 2022). Households are a focal point for SARS-CoV-2 transmission (Aleta et al., 2022; Hsu et al., 2021), especially during peaks of non-pharmaceutical intervention (NPI) restrictions, when movement outside of the household was limited (Aleta et al., 2022). Transmission within households can in turn lead to spillover to the community (Nande et al., 2021).

Prior to the widespread availability of SARS-CoV-2 vaccines, most countries relied on NPIs to reduce the transmission of the virus, including wearing face masks, social and physical distancing. While mobility and contact survey data showed that the implementation of NPIs led to a reduction in community contacts (Aleta et al., 2022; Liu et al., 2021) and in turn opportunity for infection, it is still unknown what the role of contact patterns are in the transmission of SARS-CoV-2 in the household. Most analysis relating contact patterns and SARS-CoV-2 transmission done to date has been based on low-resolution data collected from contact tracing (McAloon et al., 2021), mobility data (Aleta et al., 2022), and contact surveys (Liu et al., 2021). To obtain high-resolution contact data, devices broadcasting and receiving radio frequency waves can be used to measure the frequency and duration of close-proximity contacts. This has been used previously to collect contact data in among others, schools (Salathé et al., 2010), workplaces (Cattuto et al., 2010), hospitals (Voirin et al., 2015), and households (Kiti et al., 2016), which can, in turn, be used for modeling disease transmission. Specifically, for SARS-CoV-2 so far, high-resolution contact data were collected on cruise ships to identify areas of high contact and to investigate the usefulness of NPIs (Pung et al., 1956).

Understanding the drivers of SARS-CoV-2 transmission in the household, especially contact patterns, can help inform NPIs for future SARS-CoV-2 resurgences and potentially future emerging pathogens with pandemic potential. We aimed to assess the association of household close-range contact patterns with the transmission of SARS-CoV-2 in the household using proximity sensors deployed after the identification of SARS-CoV-2 in the household.

## Methods

### Screening, enrolment, and follow-up

We nested a contact study within a case-ascertained, prospective, household transmission study for SARS-CoV-2, implemented in two urban communities in South Africa, Klerksdorp (North West Province) and Soweto (Gauteng Province) from October 2020 through September 2021. Sample size calculations were performed for the main study, but not the nested contact study. For the main study, we aimed to assess a significant difference in the household cumulative infection risk (HCIR) between household contacts exposed to SARS-CoV-2 by a HIV-infected vs HIV-uninfected index case for a 95% confidence interval and 80% power. The resulting total sample size was 440 exposed household members. Detailed sample size calculations and methods for the main study have been reported previously (Kleynhans et al., 2022b). In short, symptomatic adults (aged ≥18 years, symptom onset ≤5 days prior) consulting at clinics were screened for SARS-CoV-2 with real-time reverse transcription polymerase chain reaction (rRT-PCR) on nasopharyngeal swabs. We enrolled household contacts of SARS-CoV-2 infected individuals identified through screening (presumptive index) with ≥2 household contacts (for efficient investigation of risk factors for transmission in the household, weighting cost of household visits and data collected) of whom none reported symptoms prior to index case onset (reducing the probability of previous recent SARS-CoV-2 infection in the household). We visited enrolled households three times a week to collect nasal swabs and data on symptoms and healthcare seeking. At enrolment household characteristics (household size, number of rooms used for sleeping, smoking inside the household, and household income) and individual characteristics (demographics, education, employment, smoking, HIV infection, underlying illness, if SARS-CoV-2 index case was the main caregiver, or sleeping in the same room as index case) were collected. Nasopharyngeal (screening) and nasal swabs (follow-up) were tested for SARS-CoV-2 on rRT-PCR using the Allplex 2019-nCoV kit (Seegene Inc, Seoul, South Korea), and the first positive of each infection episode was characterized using the Allplex SARS-CoV-2 Variants I and II PCR assays (Seegene Inc, Seoul, Korea) and through whole genome sequencing on the Ion Torrent Genexus platform (Thermo Fisher Scientific, USA). We classified the infection episodes as Alpha, Beta, Delta, non-Alpha/Beta/Delta, or unknown variant where we were unable to classify the sample as a variant of concern due to primary testing done elsewhere, low viral load, or poor sequence quality. Households with multiple SARS-CoV-2 variants circulating at the same time (mixed clusters) were excluded from the analysis. We also collected serum at the first and final household visit for serological testing, using an in-house ELISA to detect antibodies against SARS-CoV-2 spike protein (Wibmer et al., 2021) and nucleocapsid protein using Roche Elecsys anti-SARS-CoV-2 assay. Individuals were considered seropositive if they tested positive on either assay. Individuals seropositive at the start of follow-up with no rRT-PCR confirmed SARS-CoV-2 infection during follow-up were excluded from the risk factor analysis for household SARS-CoV-2 acquisition as they may have been protected from infection (Torresi et al., 2022), but were still considered in the household size parameter.

### Contact pattern measurements

At the first or second visit during follow-up, we deployed wearable radio frequency (RF) proximity sensors (Cattuto et al., 2010) for two weeks to measure close-range interactions (<1.5 meters) between household members. The proximity sensors exchange low-power radio packets in the ISM (Industrial, Scientific, and Medical) radio band. Exchange of packets and Received Signal Strength Indicator (RSSI), suitably thresholded, are used to assess proximity between the devices. A contact interval between two devices is defined as a sequence of consecutive 20 second intervals within which at least one radio packet was exchanged. Each sensor had a unique hardware identifier that was linked to participant study identifiers. Sensors were worn in a PVC pouch either pinned to clothing on the chest, or on a lanyard around the neck based on participant preference. We asked participants to wear the device while at home, to store them separately from other household member sensors at night, and to complete a log sheet every day for the periods the sensors were put on and taken off. During each household visit during the sensor deployment period, field workers confirmed sensors were worn. A deployment log was completed for each household to link the sensor identifier to the participant identifier and to log the date and time sensors were deployed and collected. After sensor collection, batteries were removed to prevent further package exchange between sensors. Sensors were transported to the study office where each sensor was connected to a computer and data downloaded.

### Data analysis

We assumed the first individual with COVID-19-compatible symptoms in the household (individual screened at the clinic) was the index case. Any household member testing positive for SARS-CoV-2 within two weeks from the last positive result for the index case was considered a secondary SARS-CoV-2 case. Contact event data were cleaned using an automated pipeline. We excluded any close-range proximity events outside of the deployment period that occurred during a 5 min time slice that the accelerometer did not detect any movement of the sensor. Accelerometers are very sensitive and even a slight movement will be detected, therefore contacts that occurred while individuals were sitting/standing still will still be included. Due to a technical error, some sensors at the Klerksdorp site did not have a valid time stamp and needed additional processing to align the time series of close-range proximity events. This was achieved by computing, for each pair of tags X and Y, the temporal shift that maximizes the correlation between the time series of the number of packets per unit time transmitted by X and received by Y, and the reciprocal time series of the number of packets per unit time transmitted by Y and received by X (an operation that can be efficiently carried out working in the frequency domain via Fourier transformation). This allowed us to build a temporal alignment graph between sensors and – as long as there was at least one sensor with a valid timestamp in the household – to use such a graph to propagate the valid timestamp to all other sensors, thus recovering global temporal alignment. For the analysis, we only considered close-range proximity events that occurred one day after sensors were issued and one day before collection, hence excluding any false events logged when sensors were prepared, handed out, and collected in the household. Where no timestamp was available, we used data collected from one to ten days after deployment.

We assessed the following close-range proximity event parameters: (1) median daily duration (median of cumulative duration of close-range proximity events for each day of deployment, in minutes), (2) maximum duration (longest duration of a close-range proximity event during deployment, in minutes), (3) median average daily duration (median of cumulative duration of close-range proximity events in the day divided by the cumulative number of close-range proximity events during that day, in minutes), (4) cumulative time in contact (cumulative duration of close-range proximity events over the deployment period divided by the number of days sensor was worn, in minutes) (5) median daily frequency (median of number of close proximity events for each day of deployment), (6) maximum frequency (highest number of close proximity events in one day during deployment), and (7) daily average frequency (cumulative duration of close-range proximity events over the deployment period divided by the cumulative number of close-range proximity events during the deployment period). Median values were preferred over mean values due to the rightly skewed data, and the different number of days with measured contact data for each household after data cleaning. We assessed contact parameters in two ways: (1) median number of close-range proximity events with the presumptive index case and (2) median number of close-range proximity events with all SARS-CoV-2 infected household members (as confirmed by rRT-PCR). For the group analysis, we did not consider the timing of symptom onset for infected individuals. The latter assessment was to take into account that the transmission could have been from any of the infected household members, and not necessarily the index case, or that the index case was misclassified.

We constructed contact matrices by combining the median duration and frequency of close-range proximity events for all participants between each age group, respectively. To normalize the matrix based on the number of participants, we divided the cumulative contact duration and frequency by the total number of individuals in the two age groups being investigated in each cell.

We assessed the association of contact parameters with SARS-CoV-2 household transmission using the Wilcoxon rank-sum test (considering p<0.05 as significant) and through logistic regression controlling for individual characteristics associated with transmission. To assess factors associated with SARS-CoV-2 household transmission, we performed logistic regression with a mixed effects hierarchical regression model to account for household- and site-level clustering. For the analysis with a defined index case (i.e. investigating close-range proximity events with all presumptive index cases, the first person with COVID-19 symptoms), we included only household contacts with their SARS-CoV-2 infection status as the outcome, assessing both index (transmission) and contact (acquisition) characteristics. For the analysis with no defined index case (i.e. investigating close-range proximity events with all SARS-CoV-2 infected household members), we included all enrolled household members (originally considered presumptive index and household contacts), assessing only their own characteristics. For the analysis of close-range proximity events with all SARS-CoV-2 infected household members, we included an offset term in the model to account for the number of SARS-CoV-2 infected members in contact with. We first built the model using individual characteristics to assess factors associated with SARS-CoV-2 transmission (excluding contact parameters). We included age and SARS-CoV-2 variant a priori, and assessed other co-variates on univariate analysis, keeping those with p<0.2 in the multivariable analysis. We then performed backward elimination, keeping only those with p<0.05, and comparing each subsequent model to the previous using a likelihood ratio test. Finally, we generated a separate model for each close-range proximity parameter, including each parameter in the final model separately to assess the association with transmission, for both the index and infected household members analysis. As a sensitivity analysis, we also repeated the individual-level analysis restricted to households where no members were excluded due to baseline SARS-CoV-2 seropositivity.

## Results

We screened 1531 individuals and identified 277 (18%) positive for SARS-CoV-2, of which 124 (45%) were enrolled and included in the household cumulative infection risk analysis (Kleynhans et al., 2022b), with 373 household contacts. After data cleaning, we had contact data for 88 (71%) index cases and 252 (68%) household contacts (Figure 1). Ninety-three individuals (19%, 36 index cases, and 73 household contacts) were excluded due to non-compliance, where no contacts were logged, or sensors were stationary for the period based on accelerometer data. We were more likely to have contact data for individuals from the Soweto site, from larger households, and with no household member reporting smoking indoors (Table 1). The median number of household members included in the analysis was 4 (interquartile range [IQR] 3–5), with a median of 3 (IQR 1–4) SARS-CoV-2 cases per household and a median of 67% (IQR 50–100%) of household members infected (including index cases). Sixty-six percent (225/340) of individuals included in the analysis lived in a household with 3–5 members, and 49% (168/340) lived in a home with only 1–2 rooms used for sleeping, a third (53/340) living in households where crowding was reported (>2 people per sleeping room Table 1).

![Figure 1.](https://cdn.elifesciences.org/articles/84753/elife-84753-fig1-v2.jpg)

**Table 1.**
 Baseline characteristics of SARS-CoV-2 index cases (n=124) and their household contacts (n=373) included in the household cumulative infection risk study and included in the contact study, Klerksdorp and Soweto, South Africa, September 2020–October 2021.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Overall</th>
      <th colspan="2">No contact data</th>
      <th>Included in contact analysis</th>
      <th>p-value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>n=497</td>
      <td colspan="2">n=157</td>
      <td>n=340</td>
      <td></td>
    </tr>
    <tr>
      <td>Site</td>
      <td></td>
      <td colspan="2"></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Klerksdorp</td>
      <td>234 (47.1)</td>
      <td colspan="2">91 (58.0)</td>
      <td>143 (42.1)</td>
      <td>0.001</td>
    </tr>
    <tr>
      <td>Soweto</td>
      <td>263 (52.9)</td>
      <td colspan="2">66 (42.0)</td>
      <td>197 (57.9)</td>
      <td></td>
    </tr>
    <tr>
      <td>Index</td>
      <td></td>
      <td colspan="2"></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Index</td>
      <td>124 (24.9)</td>
      <td colspan="2">36 (22.9)</td>
      <td>88 (25.9)</td>
      <td>0.551</td>
    </tr>
    <tr>
      <td>Contact</td>
      <td>373 (75.1)</td>
      <td colspan="2">121 (77.1)</td>
      <td>252 (74.1)</td>
      <td></td>
    </tr>
    <tr>
      <td>Household size</td>
      <td></td>
      <td colspan="2"></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>3–5</td>
      <td>347 (69.8)</td>
      <td colspan="2">122 (77.7)</td>
      <td>225 (66.2)</td>
      <td>0.012</td>
    </tr>
    <tr>
      <td>6–10</td>
      <td>150 (30.2)</td>
      <td colspan="2">35 (22.3)</td>
      <td>115 (33.8)</td>
      <td></td>
    </tr>
    <tr>
      <td>Rooms used for sleeping</td>
      <td></td>
      <td colspan="2"></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>1–2</td>
      <td>244 (49.1)</td>
      <td colspan="2">76 (48.4)</td>
      <td>168 (49.4)</td>
      <td>0.387</td>
    </tr>
    <tr>
      <td>3–4</td>
      <td>203 (40.8)</td>
      <td colspan="2">69 (43.9)</td>
      <td>134 (39.4)</td>
      <td></td>
    </tr>
    <tr>
      <td>&gt;4</td>
      <td>50 (10.1)</td>
      <td colspan="2">12 (7.6)</td>
      <td>38 (11.2)</td>
      <td></td>
    </tr>
    <tr>
      <td>Crowding</td>
      <td></td>
      <td colspan="2"></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>No</td>
      <td>353 (71.0)</td>
      <td colspan="2">112 (71.3)</td>
      <td>241 (70.9)</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Yes</td>
      <td>144 (29.0)</td>
      <td colspan="2">45 (28.7)</td>
      <td>99 (29.1)</td>
      <td></td>
    </tr>
    <tr>
      <td>Child &lt;5 years</td>
      <td></td>
      <td colspan="2"></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>No</td>
      <td>423 (85.1)</td>
      <td colspan="2">136 (86.6)</td>
      <td>287 (84.4)</td>
      <td>0.611</td>
    </tr>
    <tr>
      <td>Yes</td>
      <td>74 (14.9)</td>
      <td colspan="2">21 (13.4)</td>
      <td>53 (15.6)</td>
      <td></td>
    </tr>
    <tr>
      <td>HH member smokes inside</td>
      <td></td>
      <td colspan="2"></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>No</td>
      <td>401 (80.7)</td>
      <td colspan="2">116 (73.9)</td>
      <td>285 (83.8)</td>
      <td>0.013</td>
    </tr>
    <tr>
      <td>Yes</td>
      <td>96 (19.3)</td>
      <td colspan="2">41 (26.1)</td>
      <td>55 (16.2)</td>
      <td></td>
    </tr>
    <tr>
      <td>Main water source inside home</td>
      <td></td>
      <td colspan="2"></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>No</td>
      <td>350 (70.4)</td>
      <td colspan="2">120 (76.4)</td>
      <td>230 (67.6)</td>
      <td>0.059</td>
    </tr>
    <tr>
      <td>Yes</td>
      <td>147 (29.6)</td>
      <td colspan="2">37 (23.6)</td>
      <td>110 (32.4)</td>
      <td></td>
    </tr>
    <tr>
      <td>Main cooking fuel</td>
      <td></td>
      <td colspan="2"></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Electricity</td>
      <td>480 (96.6)</td>
      <td colspan="2">152 (96.8)</td>
      <td>328 (96.5)</td>
      <td>1</td>
    </tr>
    <tr>
      <td>Gas/Paraffin</td>
      <td>17 (3.4)</td>
      <td colspan="2">5 (3.2)</td>
      <td>12 (3.5)</td>
      <td></td>
    </tr>
    <tr>
      <td>Monthly household income (US$)</td>
      <td colspan="2"></td>
      <td colspan="2"></td>
      <td></td>
    </tr>
    <tr>
      <td>0–50</td>
      <td>42 (8.5)</td>
      <td colspan="2">20 (12.7)</td>
      <td>22 (6.5)</td>
      <td>0.125</td>
    </tr>
    <tr>
      <td>51–100</td>
      <td>41 (8.2)</td>
      <td colspan="2">16 (10.2)</td>
      <td>25 (7.4)</td>
      <td></td>
    </tr>
    <tr>
      <td>101–190</td>
      <td>90 (18.1)</td>
      <td colspan="2">25 (15.9)</td>
      <td>65 (19.1)</td>
      <td></td>
    </tr>
    <tr>
      <td>191–375</td>
      <td>77 (15.5)</td>
      <td colspan="2">21 (13.4)</td>
      <td>56 (16.5)</td>
      <td></td>
    </tr>
    <tr>
      <td>376–750</td>
      <td>36 (7.2)</td>
      <td colspan="2">12 (7.6)</td>
      <td>24 (7.1)</td>
      <td></td>
    </tr>
    <tr>
      <td>&gt;750</td>
      <td>20 (4.0)</td>
      <td colspan="2">9 (5.7)</td>
      <td>11 (3.2)</td>
      <td></td>
    </tr>
    <tr>
      <td>Refused to disclose</td>
      <td>191 (38.4)</td>
      <td colspan="2">54 (34.4)</td>
      <td>137 (40.3)</td>
      <td></td>
    </tr>
    <tr>
      <td>Age (years)</td>
      <td></td>
      <td colspan="2"></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>&lt;5</td>
      <td>19 (3.8)</td>
      <td colspan="2">8 (5.1)</td>
      <td>11 (3.2)</td>
      <td>0.711</td>
    </tr>
    <tr>
      <td>5–12</td>
      <td>73 (14.7)</td>
      <td colspan="2">25 (15.9)</td>
      <td>48 (14.1)</td>
      <td></td>
    </tr>
    <tr>
      <td>13–17</td>
      <td>60 (12.1)</td>
      <td colspan="2">18 (11.5)</td>
      <td>42 (12.4)</td>
      <td></td>
    </tr>
    <tr>
      <td>18–34</td>
      <td>130 (26.2)</td>
      <td colspan="2">45 (28.7)</td>
      <td>85 (25.0)</td>
      <td></td>
    </tr>
    <tr>
      <td>35–59</td>
      <td>163 (32.8)</td>
      <td colspan="2">47 (29.9)</td>
      <td>116 (34.1)</td>
      <td></td>
    </tr>
    <tr>
      <td>60+</td>
      <td>52 (10.5)</td>
      <td colspan="2">14 (8.9)</td>
      <td>38 (11.2)</td>
      <td></td>
    </tr>
    <tr>
      <td>Sex</td>
      <td></td>
      <td colspan="2"></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Male</td>
      <td>196 (39.4)</td>
      <td colspan="2">61 (38.9)</td>
      <td>135 (39.7)</td>
      <td>0.935</td>
    </tr>
    <tr>
      <td>Female</td>
      <td>301 (60.6)</td>
      <td colspan="2">96 (61.1)</td>
      <td>205 (60.3)</td>
      <td></td>
    </tr>
    <tr>
      <td>Level of education*</td>
      <td></td>
      <td colspan="2"></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>No schooling/kindergarten</td>
      <td>18 (3.6)</td>
      <td colspan="2">5 (3.2)</td>
      <td>13 (3.8)</td>
      <td>0.959</td>
    </tr>
    <tr>
      <td>Primary</td>
      <td>23 (4.6)</td>
      <td colspan="2">8 (5.1)</td>
      <td>15 (4.4)</td>
      <td></td>
    </tr>
    <tr>
      <td>Secondary</td>
      <td>110 (22.1)</td>
      <td colspan="2">32 (20.4)</td>
      <td>78 (22.9)</td>
      <td></td>
    </tr>
    <tr>
      <td>Matriculation</td>
      <td>169 (34.0)</td>
      <td colspan="2">52 (33.1)</td>
      <td>117 (34.4)</td>
      <td></td>
    </tr>
    <tr>
      <td>Post-secondary</td>
      <td>20 (4.0)</td>
      <td colspan="2">7 (4.5)</td>
      <td>13 (3.8)</td>
      <td></td>
    </tr>
    <tr>
      <td>Unknown</td>
      <td>157 (31.6)</td>
      <td colspan="2">53 (33.8)</td>
      <td>104 (30.6)</td>
      <td></td>
    </tr>
    <tr>
      <td>Employment*</td>
      <td></td>
      <td colspan="2"></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Unemployed</td>
      <td>170 (34.2)</td>
      <td colspan="2">52 (33.1)</td>
      <td>118 (34.7)</td>
      <td>0.876</td>
    </tr>
    <tr>
      <td>Student</td>
      <td>33 (6.6)</td>
      <td colspan="2">9 (5.7)</td>
      <td>24 (7.1)</td>
      <td></td>
    </tr>
    <tr>
      <td>Employed</td>
      <td>109 (21.9)</td>
      <td colspan="2">34 (21.7)</td>
      <td>75 (22.1)</td>
      <td></td>
    </tr>
    <tr>
      <td>Unknown</td>
      <td>185 (37.2)</td>
      <td colspan="2">62 (39.5)</td>
      <td>123 (36.2)</td>
      <td></td>
    </tr>
    <tr>
      <td>Smoking cigarettes ‡</td>
      <td></td>
      <td colspan="2"></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>No</td>
      <td>65 (13.1)</td>
      <td colspan="2">22 (14.0)</td>
      <td>43 (12.6)</td>
      <td>0.558</td>
    </tr>
    <tr>
      <td>Yes</td>
      <td>426 (85.7)</td>
      <td colspan="2">132 (84.1)</td>
      <td>294 (86.5)</td>
      <td></td>
    </tr>
    <tr>
      <td>Unknown</td>
      <td>6 (1.2)</td>
      <td colspan="2">3 (1.9)</td>
      <td>3 (0.9)</td>
      <td></td>
    </tr>
    <tr>
      <td>Living with HIV</td>
      <td></td>
      <td colspan="2"></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>No</td>
      <td>241 (48.5)</td>
      <td colspan="2">87 (55.4)</td>
      <td>154 (45.3)</td>
      <td>0.095</td>
    </tr>
    <tr>
      <td>Yes</td>
      <td>56 (11.3)</td>
      <td colspan="2">17 (10.8)</td>
      <td>39 (11.5)</td>
      <td></td>
    </tr>
    <tr>
      <td>Unknown</td>
      <td>200 (40.2)</td>
      <td colspan="2">53 (33.8)</td>
      <td>147 (43.2)</td>
      <td></td>
    </tr>
    <tr>
      <td>Underlying illness†</td>
      <td></td>
      <td colspan="2"></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>No</td>
      <td>416 (83.7)</td>
      <td colspan="2">128 (81.5)</td>
      <td>288 (84.7)</td>
      <td>0.395</td>
    </tr>
    <tr>
      <td>Yes</td>
      <td>71 (14.3)</td>
      <td colspan="2">24 (15.3)</td>
      <td>47 (13.8)</td>
      <td></td>
    </tr>
    <tr>
      <td>Unknown</td>
      <td>10 (2.0)</td>
      <td colspan="2">5 (3.2)</td>
      <td>5 (1.5)</td>
      <td></td>
    </tr>
    <tr>
      <td>Body-mass index</td>
      <td></td>
      <td colspan="2"></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Underweight</td>
      <td>28 (5.6)</td>
      <td colspan="2">8 (5.1)</td>
      <td>20 (5.9)</td>
      <td>0.757</td>
    </tr>
    <tr>
      <td>Normal weight</td>
      <td>207 (41.6)</td>
      <td colspan="2">67 (42.7)</td>
      <td>140 (41.2)</td>
      <td></td>
    </tr>
    <tr>
      <td>Overweight</td>
      <td>100 (20.1)</td>
      <td colspan="2">31 (19.7)</td>
      <td>69 (20.3)</td>
      <td></td>
    </tr>
    <tr>
      <td>Obese</td>
      <td>152 (30.6)</td>
      <td colspan="2">46 (29.3)</td>
      <td>106 (31.2)</td>
      <td></td>
    </tr>
    <tr>
      <td>Unknown</td>
      <td>10 (2.0)</td>
      <td colspan="2">5 (3.2)</td>
      <td>5 (1.5)</td>
      <td></td>
    </tr>
    <tr>
      <td>SARS-CoV-2 infection</td>
      <td></td>
      <td colspan="2"></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Negative</td>
      <td>153 (30.8)</td>
      <td colspan="2">54 (34.4)</td>
      <td>99 (29.1)</td>
      <td>0.478</td>
    </tr>
    <tr>
      <td>Positive (index)</td>
      <td>124 (24.9)</td>
      <td colspan="2">36 (22.9)</td>
      <td>88 (25.9)</td>
      <td></td>
    </tr>
    <tr>
      <td>Positive (not index)</td>
      <td>220 (44.3)</td>
      <td colspan="2">67 (42.7)</td>
      <td>153 (45.0)</td>
      <td></td>
    </tr>
  </tbody>
</table>

_Values in headers indicate the number of individuals. p-values calculated using the Chi-squared test.*For individuals ≥18 years old.†Self-reported history of diabetes, hypertension, asthma, lung disease, heart disease, stroke, spinal cord injury, epilepsy, cancer, liver disease, renal disease, and pre-maturity.‡For individuals ≥15 years old._

The overall median daily and maximum duration of close-range proximity events was 18 min (IQR 9–45 min) and 61 min (IQR 25–142 min), respectively. The average duration per close-range proximity event was 0.7 min (IQR 0.5–0.8 min), with a median of 26 (IQR 10–58) close-range proximity events per day amongst household members (Figures 2 and 3, Table 2). The highest median daily contact duration was observed between individuals within the <5 year, 5–12 year and 35–59 year groups (Figure 4A and D). Similar patterns were also seen for median daily close-range proximity duration and frequency in children aged 5–12 and 13–17 years (Figure 4B–F).

![Figure 2.](https://cdn.elifesciences.org/articles/84753/elife-84753-fig2-v2.jpg)

**Figure 2.:** Median daily duration: median of cumulative duration of close-range proximity events for each day of deployment, in minutes. Maximum duration: longest duration of a close-range proximity event during deployment, in minutes. Median average daily duration: median of cumulative duration of close-range proximity events in the day divided by the cumulative number of close-range proximity events during that day, in minutes. Cumulative time in contact: cumulative duration of close-range proximity events over the deployment period divided by the number of days sensor was worn, in minutes. Horizontal line represents the median, box represents the 25th and 75th percentile, whiskers represent the 1st and 99th percentile, and circles indicate outliers.

![Figure 3.](https://cdn.elifesciences.org/articles/84753/elife-84753-fig3-v2.jpg)

**Figure 3.:** Median daily frequency: median of number of close proximity events for each day of deployment. Maximum frequency: highest number of close proximity events in one day during deployment. Daily average frequency: cumulative duration of close-range proximity events over the deployment period divided by the cumulative number of close-range proximity events during the deployment period. Horizontal line represents the median, box represents the 25th and 75th percentile, whiskers represent 1st and 99th percentile, and circles indicate outliers.

![Figure 4.](https://cdn.elifesciences.org/articles/84753/elife-84753-fig4-v2.jpg)

**Figure 4.:** Teal denotes the lowest value, purple highest, and white no data for age group combination.

**Table 2.**
 Close-range proximity event parameters by age group (year) and site, Klerksdorp and Soweto, South Africa, September 2020–October 2021.


<table>
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th>Median daily duration *</th>
      <th>Maximum duration †</th>
      <th>Median average daily duration ‡</th>
      <th>Cumulative time in contact (per day) §</th>
      <th>Median daily frequency ¶</th>
      <th>Maximum frequency **</th>
      <th>Daily average frequency ††</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Both sites</td>
      <td>n</td>
      <td colspan="7">Median (IQR)</td>
    </tr>
    <tr>
      <td>Overall</td>
      <td>340</td>
      <td>18.2 (6.6–45.1)</td>
      <td>60.5 (25.0–141.7)</td>
      <td>0.7 (0.5–0.8)</td>
      <td>3.3 (1.5–8.0)</td>
      <td>25.5 (10.0–58.1)</td>
      <td>75.0 (32.8–134.2)</td>
      <td>4.0 (2.0–8.7)</td>
    </tr>
    <tr>
      <td>&lt;5</td>
      <td>11</td>
      <td>40.7 (17.3–87.2)</td>
      <td>163.0 (37.3–200.8)</td>
      <td>0.7 (0.6–0.8)</td>
      <td>7.0 (3.4–11.8)</td>
      <td>73.5 (24.5–105.2)</td>
      <td>209.0 (48.5–277.0)</td>
      <td>9.5 (4.4–16.2)</td>
    </tr>
    <tr>
      <td>5–12</td>
      <td>48</td>
      <td>58.0 (22.1–106.3)</td>
      <td>134.3 (58.3–296.7)</td>
      <td>0.8 (0.6–1.0)</td>
      <td>8.4 (3.7–18.9)</td>
      <td>72.2 (24.8–112.5)</td>
      <td>139.0 (52.5–273.5)</td>
      <td>9.9 (4.6–19.8)</td>
    </tr>
    <tr>
      <td>13–17</td>
      <td>42</td>
      <td>22.4 (7.7–51.2)</td>
      <td>82.0 (40.8–164.1)</td>
      <td>0.6 (0.6–0.8)</td>
      <td>4.6 (2.1–11.1)</td>
      <td>33.2 (14.1–63.5)</td>
      <td>96.0 (38.5–169.5)</td>
      <td>5.6 (3.0–10.0)</td>
    </tr>
    <tr>
      <td>18–34</td>
      <td>85</td>
      <td>14.7 (4.0–43.2)</td>
      <td>59.0 (16.7–134.3)</td>
      <td>0.7 (0.6–0.8)</td>
      <td>2.8 (1.2–6.7)</td>
      <td>19.0 (5.5–47.0)</td>
      <td>66.0 (23.0–116.0)</td>
      <td>3.0 (1.8–7.3)</td>
    </tr>
    <tr>
      <td>35–59</td>
      <td>116</td>
      <td>14.2 (5.6–35.3)</td>
      <td>52.2 (23.8–99.5)</td>
      <td>0.6 (0.5–0.8)</td>
      <td>2.4 (1.3–4.3)</td>
      <td>20.8 (8.4–37.6)</td>
      <td>67.5 (32.8–105.5)</td>
      <td>3.3 (1.8–5.2)</td>
    </tr>
    <tr>
      <td>≥60</td>
      <td>38</td>
      <td>14.0 (6.6–25.4)</td>
      <td>42.0 (17.4–79.6)</td>
      <td>0.6 (0.5–0.7)</td>
      <td>2.6 (1.2–5.7)</td>
      <td>19.8 (12.2–36.9)</td>
      <td>55.5 (28.8–89.8)</td>
      <td>3.8 (1.8–6.8)</td>
    </tr>
    <tr>
      <td>Klerksdorp</td>
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
      <td>Overall</td>
      <td>143</td>
      <td>20.0 (6.5–56.8)</td>
      <td>66.7 (29.2–149.2)</td>
      <td>0.7 (0.5–0.9)</td>
      <td>3.3 (1.6–8.1)</td>
      <td>25.5 (9.8–65.2)</td>
      <td>80.0 (36.0–163.0)</td>
      <td>4.0 (2.2–8.7)</td>
    </tr>
    <tr>
      <td>&lt;5</td>
      <td>5</td>
      <td>20.0 (20.0–137.2)</td>
      <td>48.7 (41.0–294.3)</td>
      <td>0.8 (0.7–0.9)</td>
      <td>3.6 (3.3–22.9)</td>
      <td>29.5 (25.0–163.5)</td>
      <td>69.0 (58.0–290.0)</td>
      <td>4.9 (4.0–20.1)</td>
    </tr>
    <tr>
      <td>5–12</td>
      <td>21</td>
      <td>67.5 (21.3–159.7)</td>
      <td>133.3 (59.0–336.3)</td>
      <td>0.7 (0.6–1.1)</td>
      <td>8.2 (3.7–23.7)</td>
      <td>78.0 (20.5–192.0)</td>
      <td>138.0 (51.0–273.0)</td>
      <td>8.4 (3.5–20.5)</td>
    </tr>
    <tr>
      <td>13–17</td>
      <td>23</td>
      <td>30.7 (8.8–75.7)</td>
      <td>140.0 (45.8–282.8)</td>
      <td>0.7 (0.6–0.9)</td>
      <td>6.0 (2.4–12.0)</td>
      <td>34.0 (14.8–81.2)</td>
      <td>129.0 (53.0–179.0)</td>
      <td>8.0 (3.5–10.3)</td>
    </tr>
    <tr>
      <td>18–34</td>
      <td>38</td>
      <td>15.0 (3.5–48.0)</td>
      <td>61.5 (11.0–134.8)</td>
      <td>0.6 (0.6–0.8)</td>
      <td>3.1 (1.2–6.8)</td>
      <td>19.5 (4.0–61.6)</td>
      <td>63.5 (13.5–144.5)</td>
      <td>3.1 (1.8–7.4)</td>
    </tr>
    <tr>
      <td>35–59</td>
      <td>42</td>
      <td>13.8 (6.1–32.8)</td>
      <td>54.5 (26.8–98.1)</td>
      <td>0.6 (0.5–0.7)</td>
      <td>2.6 (1.3–5.2)</td>
      <td>20.8 (9.0–32.8)</td>
      <td>64.5 (36.5–98.8)</td>
      <td>3.4 (1.8–4.8)</td>
    </tr>
    <tr>
      <td>≥60</td>
      <td>14</td>
      <td>22.2 (6.8–41.9)</td>
      <td>51.7 (19.8–114.7)</td>
      <td>0.5 (0.5–0.7)</td>
      <td>2.2 (1.2–4.8)</td>
      <td>31.0 (10.8–45.9)</td>
      <td>80.5 (34.0–104.0)</td>
      <td>3.4 (2.1–4.7)</td>
    </tr>
    <tr>
      <td>Soweto</td>
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
      <td>Overall</td>
      <td>197</td>
      <td>16.7 (6.7–40.8)</td>
      <td>59.0 (22.3–122.7)</td>
      <td>0.6 (0.5–0.8)</td>
      <td>3.2 (1.4–7.1)</td>
      <td>25.5 (10.5–56.0)</td>
      <td>71.0 (32.0–116.0)</td>
      <td>4.1 (2.0–8.6)</td>
    </tr>
    <tr>
      <td>&lt;5</td>
      <td>**6</td>
      <td>52.5 (21.2–71.6)</td>
      <td>167.8 (53.5–184.4)</td>
      <td>0.6 (0.6–0.7)</td>
      <td>7.9 (6.4–8.9)</td>
      <td>86.2 (36.4–103.1)</td>
      <td>215.0 (74.0–253.2)</td>
      <td>9.9 (9.3–11.9)</td>
    </tr>
    <tr>
      <td>5–12</td>
      <td>27</td>
      <td>57.0 (23.7–95.8)</td>
      <td>135.3 (57.7–294.0)</td>
      <td>0.8 (0.6–0.9)</td>
      <td>9.1 (4.3–16.1)</td>
      <td>66.5 (35.5–111.8)</td>
      <td>140.0 (73.0–263.5)</td>
      <td>10.2 (6.1–18.3)</td>
    </tr>
    <tr>
      <td>13–17</td>
      <td>19</td>
      <td>21.3 (7.2–32.5)</td>
      <td>62.3 (20.0–98.3)</td>
      <td>0.6 (0.5–0.7)</td>
      <td>4.0 (1.2–5.7)</td>
      <td>33.0 (12.5–43.5)</td>
      <td>80.0 (28.5–105.0)</td>
      <td>4.2 (1.6–7.1)</td>
    </tr>
    <tr>
      <td>18–34</td>
      <td>47</td>
      <td>13.3 (4.1–39.2)</td>
      <td>59.0 (20.8–120.2)</td>
      <td>0.7 (0.6–0.9)</td>
      <td>2.1 (1.3–6.4)</td>
      <td>19.0 (6.0–41.2)</td>
      <td>67.0 (28.0–108.5)</td>
      <td>2.9 (1.9–6.9)</td>
    </tr>
    <tr>
      <td>35–59</td>
      <td>74</td>
      <td>14.8 (5.6–39.0)</td>
      <td>50.2 (22.6–98.8)</td>
      <td>0.6 (0.5–0.8)</td>
      <td>2.3 (1.1–4.1)</td>
      <td>20.5 (8.1–49.1)</td>
      <td>69.0 (30.0–109.8)</td>
      <td>3.3 (1.8–5.3)</td>
    </tr>
    <tr>
      <td>≥60</td>
      <td>24</td>
      <td>11.0 (7.0–20.7)</td>
      <td>37.0 (18.2–62.8)</td>
      <td>0.6 (0.5–0.7)</td>
      <td>3.6 (1.2–5.9)</td>
      <td>19.2 (12.8–30.0)</td>
      <td>49.0 (29.8–77.8)</td>
      <td>4.9 (1.6–7.2)</td>
    </tr>
  </tbody>
</table>

_*Median daily duration (median of cumulative duration of close-range proximity events for each day of deployment, in minutes).†Maximum duration (longest duration of a close-range proximity event during deployment, in minutes).‡Median average daily duration (median of cumulative duration of close-range proximity events in the day divided by the cumulative number of close-range proximity events during that day, in minutes).§Cumulative time in contact (cumulative duration of close-range proximity events over the deployment period divided by the number of days sensor was worn, in minutes).¶Median daily frequency (median of number of close proximity events for each day of deployment).**Maximum frequency (highest number of close proximity events in one day during deployment).††Daily average frequency (cumulative duration of close-range proximity events over the deployment period divided by the cumulative number of close-range proximity events during the deployment period)._

We did not find any association between any of the contact parameters (either with the index case or all SARS-CoV-2 infected household members) and SARS-CoV-2 infection in the household using the Wilcoxon rank-sum test (p-values ranging from 0.1–0.8, Table 3).

**Table 3.**
 Association of contact parameters with SARS-CoV-2 household acquisition * using the Wilcoxon rank-sum test, Klerksdorp and Soweto, South Africa, September 2020–October 2021.


<table>
  <thead>
    <tr>
      <th>Contact parameter</th>
      <th>p-value (including all households)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Median daily duration with index †</td>
      <td>0.83</td>
    </tr>
    <tr>
      <td>Maximum duration with index ‡</td>
      <td>0.32</td>
    </tr>
    <tr>
      <td>Median average daily duration with index §</td>
      <td>0.78</td>
    </tr>
    <tr>
      <td>Cumulative time in contact with index ¶</td>
      <td>0.83</td>
    </tr>
    <tr>
      <td>Median daily frequency with index **</td>
      <td>0.71</td>
    </tr>
    <tr>
      <td>Maximum frequency with index ††</td>
      <td>0.57</td>
    </tr>
    <tr>
      <td>Daily average frequency with index ‡ ‡</td>
      <td>0.54</td>
    </tr>
    <tr>
      <td>Median daily duration with infected household members †</td>
      <td>0.25</td>
    </tr>
    <tr>
      <td>Maximum duration with infected household members ‡</td>
      <td>0.79</td>
    </tr>
    <tr>
      <td>Median average daily duration with infected household members §</td>
      <td>0.27</td>
    </tr>
    <tr>
      <td>Cumulative time in contact with infected household members ¶</td>
      <td>0.14</td>
    </tr>
    <tr>
      <td>Median daily frequency with infected household members **</td>
      <td>0.32</td>
    </tr>
    <tr>
      <td>Maximum frequency with infected household members ††</td>
      <td>0.76</td>
    </tr>
    <tr>
      <td>Daily average frequency with infected household members ‡ ‡</td>
      <td>0.18</td>
    </tr>
  </tbody>
</table>

_*Outcome investigated: testing positive for SARS-CoV-2.†Median daily duration (median of cumulative duration of close-range proximity events for each day of deployment, in minutes).‡Maximum duration (longest duration of a close-range proximity event during deployment, in minutes).§Median average daily duration (median of cumulative duration of close-range proximity events in the day divided by the cumulative number of close-range proximity events during that day, in minutes).¶Cumulative time in contact (cumulative duration of close-range proximity events over the deployment period divided by the number of days sensor was worn, in minutes).**Median daily frequency (median of number of close proximity events for each day of deployment).††Maximum frequency (highest number of close proximity events in one day during deployment).‡ ‡Daily average frequency (cumulative duration of close-range proximity events over the deployment period divided by the cumulative number of close-range proximity events during the deployment period)._

When assessing factors associated with SARS-CoV-2 transmission from presumptive index cases and acquisition in household members, none of the contact parameters were associated with SARS-CoV-2 transmission on univariate analysis. Sleeping in the same room as the index case was also not associated with transmission (OR 0.94, 95% CI 0.47–1.88). On multivariable analysis after controlling for index age and SARS-CoV-2 infecting variant, factors significantly associated with higher SARS-CoV-2 transmission and acquisition was index case minimum Ct value <30 (aOR 16.8 95% CI 3.1–93.1) compared to Ct >35, and female contacts (aOR 2.5 95% CI 1.3–5.02). No contact parameters with the index case were associated with acquisition (Table 4). Similar results were observed in the sensitivity analysis when households with members seropositive at baseline were excluded (Table 5).

**Table 4.**
 Factors associated with SARS-CoV-2 household transmission from index cases and acquisition in household contacts (contact parameters with index case), Klerksdorp and Soweto, South Africa, 2020–2021 (n=252).


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="2">SARS-CoV-2 infection*</th>
      <th>Univariate analysis</th>
      <th colspan="2">Multivariable analysis</th>
      <th colspan="7">Multivariable analysis (including contact parameter)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>Negativen=99</td>
      <td>Positiven=153</td>
      <td colspan="2">OR (95% CI)</td>
      <td>aOR (95% CI)</td>
      <td>aOR (95% CI)</td>
      <td>aOR (95% CI)</td>
      <td>aOR (95% CI)</td>
      <td>aOR (95% CI)</td>
      <td>aOR (95% CI)</td>
      <td>aOR (95% CI)</td>
      <td>aOR (95% CI)</td>
    </tr>
    <tr>
      <td colspan="2">Index Characteristics</td>
      <td></td>
      <td colspan="2"></td>
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
      <td>Site</td>
      <td></td>
      <td></td>
      <td colspan="2"></td>
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
      <td>Klerksdorp</td>
      <td>47/106 (44%)</td>
      <td>59/106 (56%)</td>
      <td colspan="2">Reference</td>
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
      <td>Soweto</td>
      <td>52/146 (36%)</td>
      <td>94/146 (64%)</td>
      <td colspan="2">1.73 (0.72–4.14)</td>
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
      <td>Age (years)</td>
      <td></td>
      <td></td>
      <td colspan="2"></td>
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
      <td>18–34</td>
      <td>36/76 (47%)</td>
      <td>40/76 (53%)</td>
      <td colspan="2">Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
    </tr>
    <tr>
      <td>35–59</td>
      <td>48/137 (35%)</td>
      <td>89/137 (65%)</td>
      <td colspan="2">2.20 (0.80–6.02)</td>
      <td>2.21 (0.80–6.14)</td>
      <td>2.24 (0.79–6.32)</td>
      <td>2.17 (0.77–6.14)</td>
      <td>2.21 (0.79–6.15)</td>
      <td>2.51 (0.85–7.40)</td>
      <td>2.43 (0.85–6.94)</td>
      <td>2.19 (0.77–6.23)</td>
      <td>2.64 (0.89–7.85)</td>
    </tr>
    <tr>
      <td>≥60</td>
      <td>15/39 (38%)</td>
      <td>24/39 (62%)</td>
      <td colspan="2">1.86 (0.47–7.37)</td>
      <td>2.08 (0.51–8.50)</td>
      <td>2.10 (0.50–8.82)</td>
      <td>1.96 (0.47–8.25)</td>
      <td>2.06 (0.49–8.57)</td>
      <td>2.40 (0.55–10.49)</td>
      <td>2.34 (0.55–9.98)</td>
      <td>2.03 (0.48–8.59)</td>
      <td>2.43 (0.55–10.80)</td>
    </tr>
    <tr>
      <td colspan="2">Minimum Ct value</td>
      <td></td>
      <td colspan="2"></td>
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
      <td>&gt;35</td>
      <td>17/21 (81%)</td>
      <td>4/21 (19%)</td>
      <td colspan="2">Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
    </tr>
    <tr>
      <td>30–35</td>
      <td>23/50 (46%)</td>
      <td>27/50 (54%)</td>
      <td colspan="2">7.58 (1.21–47.43)</td>
      <td>7.07 (0.75–66.23)</td>
      <td>7.23 (0.76–68.84)</td>
      <td>6.83 (0.72–64.85)</td>
      <td>6.88 (0.72–65.28)</td>
      <td>7.98 (0.79–80.47)</td>
      <td>7.62 (0.78–74.23)</td>
      <td>6.59 (0.68–64.07)</td>
      <td>8.06 (0.78–83.67)</td>
    </tr>
    <tr>
      <td>&lt;30</td>
      <td>58/178 (33%)</td>
      <td>120/178 (67%)</td>
      <td colspan="2">16.84 (3.05–93.06)</td>
      <td>10.60 (1.40–80.08)</td>
      <td>10.77 (1.41–82.26)</td>
      <td>10.39 (1.36–79.27)</td>
      <td>10.36 (1.36–79.23)</td>
      <td>11.04 (1.38–88.37)</td>
      <td>11.08 (1.42–86.47)</td>
      <td>10.04 (1.29–78.05)</td>
      <td>11.05 (1.35–90.60)</td>
    </tr>
    <tr>
      <td>Unknown</td>
      <td>1/3 (33%)</td>
      <td>2/3 (67%)</td>
      <td colspan="2">15.69 (0.31–793.51)</td>
      <td>7.22 (0.12–438.47)</td>
      <td>7.27 (0.12–450.06)</td>
      <td>6.79 (0.11–423.55)</td>
      <td>7.37 (0.12–465.42)</td>
      <td>7.55 (0.11–503.58)</td>
      <td>7.42 (0.12–467.86)</td>
      <td>6.85 (0.10–453.16)</td>
      <td>7.92 (0.11–558.92)</td>
    </tr>
    <tr>
      <td colspan="2">SARS-CoV-2 variant</td>
      <td></td>
      <td colspan="2"></td>
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
      <td>non-Alpha/Beta/Delta</td>
      <td>5/14 (36%)</td>
      <td>9/14 (64%)</td>
      <td colspan="2">1.22 (0.22–6.93)</td>
      <td>2.04 (0.31–13.41)</td>
      <td>2.12 (0.32–14.08)</td>
      <td>2.15 (0.32–14.51)</td>
      <td>2.06 (0.31–13.72)</td>
      <td>2.00 (0.29–13.76)</td>
      <td>1.99 (0.30–13.26)</td>
      <td>1.99 (0.29–13.61)</td>
      <td>2.07 (0.29–14.67)</td>
    </tr>
    <tr>
      <td>Alpha</td>
      <td>2/13 (15%)</td>
      <td>11/13 (85%)</td>
      <td colspan="2">4.81 (0.59–39.19)</td>
      <td>5.02 (0.52–48.39)</td>
      <td>5.15 (0.48–55.49)</td>
      <td>5.48 (0.53–57.15)</td>
      <td>4.71 (0.43–51.12)</td>
      <td>3.45 (0.33–36.67)</td>
      <td>4.59 (0.47–44.90)</td>
      <td>5.02 (0.50–50.59)</td>
      <td>4.91 (0.47–51.69)</td>
    </tr>
    <tr>
      <td>Beta</td>
      <td>70/171 (41%)</td>
      <td>101/171 (59%)</td>
      <td colspan="2">Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
    </tr>
    <tr>
      <td>Delta</td>
      <td>8/38 (21%)</td>
      <td>30/38 (79%)</td>
      <td colspan="2">3.24 (0.93–11.32)</td>
      <td>3.76 (0.97–14.55)</td>
      <td>3.90 (0.99–15.29)</td>
      <td>3.79 (0.96–14.95)</td>
      <td>3.81 (0.97–14.89)</td>
      <td>3.86 (0.96–15.53)</td>
      <td>3.88 (0.99–15.27)</td>
      <td>3.87 (0.97–15.53)</td>
      <td>3.94 (0.96–16.23)</td>
    </tr>
    <tr>
      <td>Variant Unknown</td>
      <td>14/16 (88%)</td>
      <td>2/16 (12%)</td>
      <td colspan="2">0.06 (0.01–0.41)</td>
      <td>0.15 (0.01–1.60)</td>
      <td>0.16 (0.02–1.67)</td>
      <td>0.16 (0.01–1.66)</td>
      <td>0.15 (0.01–1.57)</td>
      <td>0.14 (0.01–1.56)</td>
      <td>0.14 (0.01–1.50)</td>
      <td>0.14 (0.01–1.55)</td>
      <td>0.14 (0.01–1.61)</td>
    </tr>
    <tr>
      <td colspan="2">Contact characteristics</td>
      <td></td>
      <td colspan="2"></td>
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
      <td>Age (years)</td>
      <td></td>
      <td></td>
      <td colspan="2"></td>
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
      <td>&lt;5</td>
      <td>8/11 (73%)</td>
      <td>3/11 (27%)</td>
      <td colspan="2">0.17 (0.03–1.05)</td>
      <td>0.28 (0.04–1.90)</td>
      <td>0.30 (0.04–2.04)</td>
      <td>0.31 (0.05–2.11)</td>
      <td>0.28 (0.04–1.90)</td>
      <td>0.24 (0.03–1.66)</td>
      <td>0.24 (0.03–1.70)</td>
      <td>0.27 (0.04–1.97)</td>
      <td>0.22 (0.03–1.59)</td>
    </tr>
    <tr>
      <td>5–12</td>
      <td>21/48 (44%)</td>
      <td>27/48 (56%)</td>
      <td colspan="2">0.69 (0.25–1.93)</td>
      <td>0.54 (0.19–1.52)</td>
      <td>0.53 (0.18–1.54)</td>
      <td>0.55 (0.19–1.56)</td>
      <td>0.51 (0.18–1.46)</td>
      <td>0.49 (0.17–1.42)</td>
      <td>0.47 (0.16–1.37)</td>
      <td>0.51 (0.17–1.48)</td>
      <td>0.48 (0.17–1.41)</td>
    </tr>
    <tr>
      <td>13–17</td>
      <td>11/42 (26%)</td>
      <td>31/42 (74%)</td>
      <td colspan="2">2.55 (0.78–8.32)</td>
      <td>2.41 (0.72–8.08)</td>
      <td>2.42 (0.72–8.16)</td>
      <td>2.42 (0.72–8.17)</td>
      <td>2.38 (0.70–8.03)</td>
      <td>2.47 (0.72–8.45)</td>
      <td>2.46 (0.73–8.34)</td>
      <td>2.39 (0.71–8.12)</td>
      <td>2.57 (0.75–8.83)</td>
    </tr>
    <tr>
      <td>18–34</td>
      <td>22/60 (37%)</td>
      <td>38/60 (63%)</td>
      <td colspan="2">Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
    </tr>
    <tr>
      <td>35–59</td>
      <td>27/68 (40%)</td>
      <td>41/68 (60%)</td>
      <td colspan="2">0.72 (0.28–1.87)</td>
      <td>0.60 (0.23–1.57)</td>
      <td>0.60 (0.23–1.59)</td>
      <td>0.61 (0.23–1.61)</td>
      <td>0.59 (0.22–1.56)</td>
      <td>0.60 (0.23–1.59)</td>
      <td>0.59 (0.22–1.57)</td>
      <td>0.58 (0.22–1.55)</td>
      <td>0.62 (0.23–1.65)</td>
    </tr>
    <tr>
      <td>≥60</td>
      <td>10/23 (43%)</td>
      <td>13/23 (57%)</td>
      <td colspan="2">0.78 (0.21–2.93)</td>
      <td>0.61 (0.17–2.24)</td>
      <td>0.61 (0.17–2.27)</td>
      <td>0.61 (0.17–2.27)</td>
      <td>0.61 (0.16–2.23)</td>
      <td>0.65 (0.17–2.46)</td>
      <td>0.64 (0.17–2.37)</td>
      <td>0.61 (0.16–2.26)</td>
      <td>0.66 (0.17–2.54)</td>
    </tr>
    <tr>
      <td>Sex</td>
      <td></td>
      <td></td>
      <td colspan="2"></td>
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
      <td>Male</td>
      <td>52/108 (48%)</td>
      <td>56/108 (52%)</td>
      <td colspan="2">Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
    </tr>
    <tr>
      <td>Female</td>
      <td>47/144 (33%)</td>
      <td>97/144 (67%)</td>
      <td colspan="2">2.51 (1.25–5.02)</td>
      <td>2.38 (1.17–4.84)</td>
      <td>2.37 (1.15–4.86)</td>
      <td>2.44 (1.18–5.03)</td>
      <td>2.32 (1.14–4.74)</td>
      <td>2.25 (1.09–4.63)</td>
      <td>2.20 (1.07–4.53)</td>
      <td>2.36 (1.14–4.88)</td>
      <td>2.21 (1.07–4.59)</td>
    </tr>
    <tr>
      <td colspan="2">Sleep in same room as index</td>
      <td></td>
      <td colspan="2"></td>
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
      <td>No</td>
      <td>68/171 (40%)</td>
      <td>103/171 (60%)</td>
      <td colspan="2">Reference</td>
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
      <td>Yes</td>
      <td>31/81 (38%)</td>
      <td>50/81 (62%)</td>
      <td colspan="2">0.94 (0.47–1.88)</td>
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
      <td colspan="2">Cared for by index</td>
      <td></td>
      <td colspan="2"></td>
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
      <td>No</td>
      <td>84/212 (40%)</td>
      <td>128/212 (60%)</td>
      <td colspan="2">Reference</td>
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
      <td>Yes</td>
      <td>15/40 (38%)</td>
      <td>25/40 (62%)</td>
      <td colspan="2">0.92 (0.36–2.34)</td>
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
      <td>Median daily duration †</td>
      <td>5 (1-11)</td>
      <td>4 (2-12)</td>
      <td colspan="2">0.99 (0.98–1.01)</td>
      <td></td>
      <td>1.00 (0.98–1.02)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Maximum duration ‡</td>
      <td>17 (5–48)</td>
      <td>14 (4–38)</td>
      <td colspan="2">1.00 (0.99–1.00)</td>
      <td></td>
      <td></td>
      <td>1.00 (0.99–1.01)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Median average daily duration §</td>
      <td>0.53 (0.43–0.69)</td>
      <td>0.56 (0.44–0.67)</td>
      <td colspan="2">1.15 (0.60–2.21)</td>
      <td></td>
      <td></td>
      <td></td>
      <td>1.08 (0.50–2.30)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Cumulative time in contact ¶</td>
      <td>0.87 (0.37–1.80)</td>
      <td>0.90 (0.33–2.27)</td>
      <td colspan="2">1.04 (0.92–1.17)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>1.08 (0.94–1.25)</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Median daily frequency ¶</td>
      <td>6 (3-15)</td>
      <td>7 (3-15)</td>
      <td colspan="2">1.00 (0.98–1.02)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>1.01 (0.99–1.03)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Maximum frequency **</td>
      <td>22 (8–52)</td>
      <td>19 (7–41)</td>
      <td colspan="2">1.00 (0.99–1.01)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>1.00 (0.99–1.01)</td>
      <td></td>
    </tr>
    <tr>
      <td>Daily average frequency ††</td>
      <td>1.00 (0.57–2.77)</td>
      <td>1.16 (0.53–2.70)</td>
      <td colspan="2">1.06 (0.95–1.18)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>1.10 (0.96–1.25)</td>
    </tr>
  </tbody>
</table>

_* n/ row N (%); Median (interquartile range).†Median daily duration (median of cumulative duration of close-range proximity events for each day of deployment, in minutes).‡Maximum duration (longest duration of a close-range proximity event during deployment, in minutes).§Median average daily duration (median of cumulative duration of close-range proximity events in the day divided by the cumulative number of close-range proximity events during that day, in minutes).¶Cumulative time in contact (cumulative duration of close-range proximity events over the deployment period divided by the number of days sensor was worn, in minutes).**Maximum frequency (highest number of close proximity events in one day during deployment).††Daily average frequency (cumulative duration of close-range proximity events over the deployment period divided by the cumulative number of close-range proximity events during the deployment period). aOR: adjusted odds ratio. Significant associations on multivariable analysis in boldface. Factors investigated but not found significant on multivariable analysis: index sex, HIV status, underlying conditions, body mass index, current smoking, episode duration, serostatus at follow-up end; contact HIV status, underlying conditions, body mass index, current smoking, cared for by index._

**Table 5.**
 Factors associated with SARS-CoV-2 household transmission from index cases and acquisition in household contacts (contact parameters with index case) in households with no members excluded from analysis, Klerksdorp and Soweto, South Africa, 2020–2021, (n=192).


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="2">SARS-CoV-2 infection*</th>
      <th colspan="2">Univariate analysis</th>
      <th colspan="3">Multivariable analysis</th>
      <th colspan="7">Multivariable analysis (including contact parameter)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>Negativen=66</td>
      <td colspan="2">Positiven=126</td>
      <td colspan="2">OR (95% CI)</td>
      <td colspan="2">aOR (95% CI)</td>
      <td colspan="7">aOR (95% CI)</td>
    </tr>
    <tr>
      <td colspan="2">Index Characteristics</td>
      <td colspan="2"></td>
      <td colspan="3"></td>
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
      <td>Site</td>
      <td></td>
      <td colspan="2"></td>
      <td colspan="3"></td>
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
      <td>Klerksdorp</td>
      <td>25/70 (36%)</td>
      <td colspan="2">45/70 (64%)</td>
      <td colspan="3">Reference</td>
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
      <td>Soweto</td>
      <td>41/122 (34%)</td>
      <td colspan="2">81/122 (66%)</td>
      <td colspan="3">1.30 (0.42–4.00)</td>
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
      <td>Age (years)</td>
      <td></td>
      <td colspan="2"></td>
      <td colspan="3"></td>
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
      <td>18–34</td>
      <td>20/48 (42%)</td>
      <td colspan="2">28/48 (58%)</td>
      <td colspan="3">Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
    </tr>
    <tr>
      <td>35–59</td>
      <td>32/111 (29%)</td>
      <td colspan="2">79/111 (71%)</td>
      <td colspan="3">2.52 (0.70–9.13)</td>
      <td>2.13 (0.60–7.55)</td>
      <td>1.88 (0.58–6.15)</td>
      <td>1.99 (0.60–6.55)</td>
      <td>2.09 (0.63–6.97)</td>
      <td>1.98 (0.55–7.11)</td>
      <td>2.02 (0.59–6.89)</td>
      <td>1.86 (0.54–6.38)</td>
      <td>2.09 (0.63–7.00)</td>
    </tr>
    <tr>
      <td>≥60</td>
      <td>14/33 (42%)</td>
      <td colspan="2">19/33 (58%)</td>
      <td colspan="3">1.01 (0.20–5.19)</td>
      <td>1.41 (0.24–8.22)</td>
      <td>1.22 (0.23–6.62)</td>
      <td>1.31 (0.24–7.23)</td>
      <td>1.38 (0.24–7.84)</td>
      <td>1.34 (0.23–7.74)</td>
      <td>1.35 (0.24–7.72)</td>
      <td>1.26 (0.23–6.94)</td>
      <td>1.43 (0.26–7.91)</td>
    </tr>
    <tr>
      <td colspan="2">Minimum Ct value</td>
      <td colspan="2"></td>
      <td colspan="3"></td>
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
      <td>&gt;35</td>
      <td>16/18 (89%)</td>
      <td colspan="2">2/18 (11%)</td>
      <td colspan="3">Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
    </tr>
    <tr>
      <td>30–35</td>
      <td>15/38 (39%)</td>
      <td colspan="2">23/38 (61%)</td>
      <td colspan="3">22.18 (2.39–205.39)</td>
      <td>23.38 (1.23–445.33)</td>
      <td>21.38 (1.41–325.01)</td>
      <td>22.55 (1.43–354.91)</td>
      <td>23.36 (1.40–389.09)</td>
      <td>21.73 (1.24–381.17)</td>
      <td>21.25 (1.30–347.22)</td>
      <td>18.86 (1.18–301.62)</td>
      <td>22.49 (1.37–368.46)</td>
    </tr>
    <tr>
      <td>&lt;30</td>
      <td>34/133 (26%)</td>
      <td colspan="2">99/133 (74%)</td>
      <td colspan="3">48.47 (5.80–404.75)</td>
      <td>39.72 (2.69–585.90)</td>
      <td>37.61 (3.28–431.72)</td>
      <td>38.32 (3.24–452.80)</td>
      <td>39.80 (3.20–495.62)</td>
      <td>37.67 (2.76–513.85)</td>
      <td>36.87 (3.03–448.62)</td>
      <td>32.87 (2.61–413.51)</td>
      <td>38.58 (3.14–473.57)</td>
    </tr>
    <tr>
      <td>Unknown</td>
      <td>1/3 (33%)</td>
      <td colspan="2">2/3 (67%)</td>
      <td colspan="3">30.11 (0.61–1,497.22)</td>
      <td>14.55 (0.18–1,148.81)</td>
      <td>13.46 (0.22–836.17)</td>
      <td>14.11 (0.22–923.86)</td>
      <td>15.49 (0.22–1,110.09)</td>
      <td>14.21 (0.20–1,025.63)</td>
      <td>13.14 (0.19–918.99)</td>
      <td>11.86 (0.19–755.20)</td>
      <td>13.83 (0.20–952.08)</td>
    </tr>
    <tr>
      <td colspan="2">SARS-CoV-2 variant</td>
      <td colspan="2"></td>
      <td colspan="3"></td>
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
      <td>non-Alpha/Beta/Delta</td>
      <td>3/8 (38%)</td>
      <td colspan="2">5/8 (62%)</td>
      <td colspan="3">0.68 (0.09–5.16)</td>
      <td>0.68 (0.09–5.16)</td>
      <td>1.79 (0.13–24.54)</td>
      <td>1.71 (0.14–20.48)</td>
      <td>1.76 (0.14–21.84)</td>
      <td>1.85 (0.14–23.74)</td>
      <td>1.75 (0.14–22.72)</td>
      <td>1.71 (0.13–21.95)</td>
      <td>1.60 (0.13–20.06)</td>
    </tr>
    <tr>
      <td>Alpha</td>
      <td>1/11 (9.1%)</td>
      <td colspan="2">10/11 (91%)</td>
      <td colspan="3">7.00 (0.47–103.30)</td>
      <td>7.00 (0.47–103.30)</td>
      <td>5.58 (0.32–96.65)</td>
      <td>8.18 (0.32–206.89)</td>
      <td>6.52 (0.32–132.55)</td>
      <td>5.76 (0.25–133.53)</td>
      <td>7.47 (0.29–194.23)</td>
      <td>5.51 (0.29–103.13)</td>
      <td>5.83 (0.36–94.07)</td>
    </tr>
    <tr>
      <td>Beta</td>
      <td>45/130 (35%)</td>
      <td colspan="2">85/130 (65%)</td>
      <td colspan="3">Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
    </tr>
    <tr>
      <td>Delta</td>
      <td>7/33 (21%)</td>
      <td colspan="2">26/33 (79%)</td>
      <td colspan="3">2.17 (0.61–7.64)</td>
      <td>2.17 (0.61–7.64)</td>
      <td>3.01 (0.67–13.53)</td>
      <td>2.82 (0.68–11.69)</td>
      <td>2.90 (0.68–12.35)</td>
      <td>3.01 (0.69–13.17)</td>
      <td>2.91 (0.68–12.50)</td>
      <td>2.85 (0.66–12.41)</td>
      <td>2.73 (0.65–11.51)</td>
    </tr>
    <tr>
      <td>Variant Unknown</td>
      <td>10/10 (100%)</td>
      <td colspan="2">0/10 (0%)</td>
      <td colspan="3">NA</td>
      <td>NA</td>
      <td>NA</td>
      <td>NA</td>
      <td>NA</td>
      <td>NA</td>
      <td>NA</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td colspan="2">Contact characteristics</td>
      <td colspan="2"></td>
      <td colspan="3"></td>
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
      <td>Age (years)</td>
      <td></td>
      <td colspan="2"></td>
      <td colspan="3"></td>
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
      <td>&lt;5</td>
      <td>7/8 (88%)</td>
      <td colspan="2">1/8 (12%)</td>
      <td colspan="3">0.01 (0.00–0.27)</td>
      <td>0.03 (0.00–0.50)</td>
      <td>0.03 (0.00–0.51)</td>
      <td>0.03 (0.00–0.48)</td>
      <td>0.03 (0.00–0.46)</td>
      <td>0.03 (0.00–0.52)</td>
      <td>0.03 (0.00–0.48)</td>
      <td>0.03 (0.00–0.65)</td>
      <td>0.03 (0.00–0.44)</td>
    </tr>
    <tr>
      <td>5–12</td>
      <td>14/37 (38%)</td>
      <td colspan="2">23/37 (62%)</td>
      <td colspan="3">0.38 (0.10–1.40)</td>
      <td>0.33 (0.09–1.20)</td>
      <td>0.38 (0.10–1.34)</td>
      <td>0.35 (0.10–1.23)</td>
      <td>0.33 (0.10–1.16)</td>
      <td>0.34 (0.09–1.23)</td>
      <td>0.35 (0.10–1.24)</td>
      <td>0.37 (0.10–1.37)</td>
      <td>0.33 (0.09–1.14)</td>
    </tr>
    <tr>
      <td>13–17</td>
      <td>7/33 (21%)</td>
      <td colspan="2">26/33 (79%)</td>
      <td colspan="3">1.68 (0.38–7.41)</td>
      <td>1.66 (0.34–8.03)</td>
      <td>1.57 (0.33–7.58)</td>
      <td>1.63 (0.33–7.96)</td>
      <td>1.65 (0.33–8.22)</td>
      <td>1.61 (0.34–7.72)</td>
      <td>1.68 (0.34–8.31)</td>
      <td>1.63 (0.35–7.65)</td>
      <td>1.66 (0.33–8.25)</td>
    </tr>
    <tr>
      <td>18–34</td>
      <td>10/42 (24%)</td>
      <td colspan="2">32/42 (76%)</td>
      <td colspan="3">Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
    </tr>
    <tr>
      <td>35–59</td>
      <td>23/57 (40%)</td>
      <td colspan="2">34/57 (60%)</td>
      <td colspan="3">0.36 (0.11–1.19)</td>
      <td>0.35 (0.11–1.13)</td>
      <td>0.36 (0.11–1.10)</td>
      <td>0.35 (0.11–1.10)</td>
      <td>0.35 (0.11–1.09)</td>
      <td>0.34 (0.10–1.09)</td>
      <td>0.36 (0.11–1.11)</td>
      <td>0.36 (0.11–1.16)</td>
      <td>0.34 (0.11–1.08)</td>
    </tr>
    <tr>
      <td>≥60</td>
      <td>5/15 (33%)</td>
      <td colspan="2">10/15 (67%)</td>
      <td colspan="3">0.47 (0.08–2.68)</td>
      <td>0.42 (0.08–2.30)</td>
      <td>0.41 (0.08–2.09)</td>
      <td>0.42 (0.08–2.16)</td>
      <td>0.43 (0.08–2.22)</td>
      <td>0.41 (0.08–2.19)</td>
      <td>0.43 (0.08–2.23)</td>
      <td>0.41 (0.08–2.19)</td>
      <td>0.41 (0.08–2.12)</td>
    </tr>
    <tr>
      <td>Sex</td>
      <td></td>
      <td colspan="2"></td>
      <td colspan="3"></td>
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
      <td>Male</td>
      <td>33/79 (42%)</td>
      <td colspan="2">46/79 (58%)</td>
      <td colspan="3">Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
    </tr>
    <tr>
      <td>Female</td>
      <td>33/113 (29%)</td>
      <td colspan="2">80/113 (71%)</td>
      <td colspan="3">2.40 (1.05–5.46)</td>
      <td>2.28 (0.96–5.43)</td>
      <td>2.42 (1.04–5.66)</td>
      <td>2.38 (1.01–5.62)</td>
      <td>2.30 (0.99–5.36)</td>
      <td>2.36 (0.99–5.63)</td>
      <td>2.34 (0.99–5.55)</td>
      <td>2.45 (1.02–5.87)</td>
      <td>2.29 (0.97–5.39)</td>
    </tr>
    <tr>
      <td colspan="2">Sleep in same room as index</td>
      <td colspan="2"></td>
      <td colspan="3"></td>
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
      <td>No</td>
      <td>46/133 (35%)</td>
      <td colspan="2">87/133 (65%)</td>
      <td colspan="3">Reference</td>
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
      <td>Yes</td>
      <td>20/59 (34%)</td>
      <td colspan="2">39/59 (66%)</td>
      <td colspan="3">0.90 (0.39–2.08)</td>
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
      <td colspan="2">Cared for by index</td>
      <td colspan="2"></td>
      <td colspan="3"></td>
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
      <td>No</td>
      <td>54/160 (34%)</td>
      <td colspan="2">106/160 (66%)</td>
      <td colspan="3">Reference</td>
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
      <td>Yes</td>
      <td>12/32 (38%)</td>
      <td colspan="2">20/32 (62%)</td>
      <td colspan="3">0.60 (0.19–1.86)</td>
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
      <td>Median daily duration †</td>
      <td>6 (1-14)</td>
      <td colspan="2">4 (1-12)</td>
      <td colspan="3">0.99 (0.97–1.01)</td>
      <td></td>
      <td>0.99 (0.97–1.02)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Maximum duration ‡</td>
      <td>18 (5–51)</td>
      <td colspan="2">13 (3–37)</td>
      <td colspan="3">1.00 (0.99–1.00)</td>
      <td></td>
      <td></td>
      <td>1.00 (0.99–1.01)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Median average daily duration §</td>
      <td>0.53 (0.43–0.75)</td>
      <td colspan="2">0.52 (0.42–0.67)</td>
      <td colspan="3">1.10 (0.53–2.27)</td>
      <td></td>
      <td></td>
      <td></td>
      <td>1.00 (0.42–2.34)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Cumulative time in contact ¶</td>
      <td>1.01 (0.37–2.26)</td>
      <td colspan="2">0.88 (0.32–2.34)</td>
      <td colspan="3">0.98 (0.85–1.12)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.96 (0.80–1.16)</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Median daily frequency **</td>
      <td>9 (3-16)</td>
      <td colspan="2">7 (3-15)</td>
      <td colspan="3">0.99 (0.97–1.01)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>1.00 (0.97–1.02)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Maximum frequency ††</td>
      <td>24 (8–68)</td>
      <td colspan="2">19 (6–40)</td>
      <td colspan="3">0.99 (0.98–1.00)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.99 (0.98–1.01)</td>
      <td></td>
    </tr>
    <tr>
      <td>Daily average frequency ‡ ‡</td>
      <td>1.40 (0.60–3.15)</td>
      <td colspan="2">1.07 (0.50–2.70)</td>
      <td colspan="3">0.98 (0.84–1.15)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.98 (0.81–1.18)</td>
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
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

_* n/ row N (%); Median (interquartile range).†Median daily duration (median of cumulative duration of close-range proximity events for each day of deployment, in minutes).‡Maximum duration (longest duration of a close-range proximity event during deployment, in minutes).§Median average daily duration (median of cumulative duration of close-range proximity events in the day divided by the cumulative number of close-range proximity events during that day, in minutes).¶Cumulative time in contact (cumulative duration of close-range proximity events over the deployment period divided by the number of days sensor was worn, in minutes).**Median daily frequency (median of number of close proximity events for each day of deployment).††Maximum frequency (highest number of close proximity events in one day during deployment).‡ ‡Daily average frequency (cumulative duration of close-range proximity events over the deployment period divided by the cumulative number of close-range proximity events during the deployment period). aOR: adjusted odds ratio. Significant associations on multivariable analysis in boldface._

When not considering transmission from the presumptive index case, but rather all SARS-CoV-2 infected household members, factors significantly associated with SARS-CoV-2 acquisition on multivariable analysis after controlling for age and SARS-CoV-2 infecting variant were being obese (aOR 4.1 95% CI 1.5–11.1) compared to normal weight, and not currently smoking (aOR 3.2 95% CI 1.2–9.2). No contact parameters with SARS-CoV-2 infected household members were associated with acquisition (Table 6).

**Table 6.**
 Factors associated with SARS-CoV-2 acquisition within the household (contact parameters with SARS-CoV-2 infected household members), Klerksdorp and Soweto, South Africa, 2020–2021, (n=340).


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="2">SARS-CoV-2 infection</th>
      <th>Univariate analysis</th>
      <th>Multivariable analysis</th>
      <th colspan="7">Multivariable analysis (including contact parameter)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>Negativen=99</td>
      <td>Positiven=241</td>
      <td>OR (95% CI)</td>
      <td>aOR (95% CI)</td>
      <td>aOR (95% CI)</td>
      <td>aOR (95% CI)</td>
      <td>aOR (95% CI)</td>
      <td>aOR (95% CI)</td>
      <td>aOR (95% CI)</td>
      <td>aOR (95% CI)</td>
      <td>aOR (95% CI)</td>
    </tr>
    <tr>
      <td>Site</td>
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
      <td></td>
    </tr>
    <tr>
      <td>Klerksdorp</td>
      <td>47/143 (33%)</td>
      <td>96/143 (67%)</td>
      <td>Reference</td>
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
      <td>Soweto</td>
      <td>52/197 (26%)</td>
      <td>145/197 (74%)</td>
      <td>1.70 (0.64–4.51)</td>
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
      <td>Contact Age (years)</td>
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
      <td></td>
    </tr>
    <tr>
      <td>&lt;5</td>
      <td>8/11 (73%)</td>
      <td>3/11 (27%)</td>
      <td>0.06 (0.01–0.41)</td>
      <td>1.88 (0.25–14.08)</td>
      <td>0.09 (0.01–0.71)</td>
      <td>0.12 (0.01–0.96)</td>
      <td>0.11 (0.01–0.89)</td>
      <td>0.08 (0.01–0.65)</td>
      <td>0.09 (0.01–0.75)</td>
      <td>0.15 (0.02–1.21)</td>
      <td>0.08 (0.01–0.63)</td>
    </tr>
    <tr>
      <td>5–12</td>
      <td>21/48 (44%)</td>
      <td>27/48 (56%)</td>
      <td>0.20 (0.07–0.57)</td>
      <td>9.43 (1.17–75.88)</td>
      <td>0.17 (0.05–0.56)</td>
      <td>0.24 (0.08–0.75)</td>
      <td>0.21 (0.07–0.62)</td>
      <td>0.16 (0.05–0.48)</td>
      <td>0.18 (0.05–0.59)</td>
      <td>0.25 (0.08–0.76)</td>
      <td>0.15 (0.05–0.48)</td>
    </tr>
    <tr>
      <td>13–17</td>
      <td>11/42 (26%)</td>
      <td>31/42 (74%)</td>
      <td>0.87 (0.28–2.70)</td>
      <td>10.08 (1.34–76.04)</td>
      <td>0.96 (0.28–3.28)</td>
      <td>1.00 (0.30–3.36)</td>
      <td>1.12 (0.34–3.74)</td>
      <td>0.93 (0.28–3.06)</td>
      <td>0.95 (0.28–3.25)</td>
      <td>1.05 (0.32–3.44)</td>
      <td>0.92 (0.28–3.04)</td>
    </tr>
    <tr>
      <td>18–34</td>
      <td>22/85 (26%)</td>
      <td>63/85 (74%)</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
    </tr>
    <tr>
      <td>35–59</td>
      <td>27/116 (23%)</td>
      <td>89/116 (77%)</td>
      <td>0.98 (0.41–2.30)</td>
      <td>8.79 (1.14–67.74)</td>
      <td>0.87 (0.34–2.23)</td>
      <td>0.91 (0.36–2.30)</td>
      <td>0.84 (0.34–2.12)</td>
      <td>0.86 (0.35–2.13)</td>
      <td>0.88 (0.34–2.24)</td>
      <td>0.92 (0.37–2.27)</td>
      <td>0.87 (0.35–2.15)</td>
    </tr>
    <tr>
      <td>≥60</td>
      <td>10/38 (26%)</td>
      <td>28/38 (74%)</td>
      <td>1.11 (0.34–3.58)</td>
      <td>8.71 (0.98–77.54)</td>
      <td>0.86 (0.24–3.05)</td>
      <td>0.86 (0.25–3.00)</td>
      <td>0.82 (0.24–2.78)</td>
      <td>0.85 (0.25–2.87)</td>
      <td>0.87 (0.25–3.05)</td>
      <td>0.89 (0.27–2.97)</td>
      <td>0.85 (0.25–2.88)</td>
    </tr>
    <tr>
      <td>Contact Sex</td>
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
      <td></td>
    </tr>
    <tr>
      <td>Male</td>
      <td>52/135 (39%)</td>
      <td>83/135 (61%)</td>
      <td>Reference</td>
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
      <td>Female</td>
      <td>47/205 (23%)</td>
      <td>158/205 (77%)</td>
      <td>2.64 (1.40–4.95)</td>
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
      <td>Body mass index</td>
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
      <td></td>
    </tr>
    <tr>
      <td>Normal weight</td>
      <td>50/140 (36%)</td>
      <td>90/140 (64%)</td>
      <td>Reference</td>
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
      <td>Underweight</td>
      <td>7/20 (35%)</td>
      <td>13/20 (65%)</td>
      <td>0.89 (0.22–3.53)</td>
      <td>0.90 (0.22–3.67)</td>
      <td>0.87 (0.20–3.87)</td>
      <td>1.04 (0.24–4.56)</td>
      <td>0.88 (0.21–3.73)</td>
      <td>0.78 (0.19–3.29)</td>
      <td>0.90 (0.20–3.96)</td>
      <td>1.01 (0.25–4.09)</td>
      <td>0.81 (0.19–3.38)</td>
    </tr>
    <tr>
      <td>Overweight</td>
      <td>22/69 (32%)</td>
      <td>47/69 (68%)</td>
      <td>1.61 (0.70–3.71)</td>
      <td>1.17 (0.49–2.76)</td>
      <td>1.17 (0.47–2.91)</td>
      <td>1.15 (0.47–2.83)</td>
      <td>1.17 (0.49–2.78)</td>
      <td>1.18 (0.49–2.82)</td>
      <td>1.16 (0.47–2.89)</td>
      <td>1.14 (0.48–2.67)</td>
      <td>1.17 (0.49–2.80)</td>
    </tr>
    <tr>
      <td>Obese</td>
      <td>17/106 (16%)</td>
      <td>89/106 (84%)</td>
      <td>7.47 (3.10–17.98)</td>
      <td>4.14 (1.54–11.11)</td>
      <td>4.31 (1.54–12.03)</td>
      <td>3.83 (1.40–10.48)</td>
      <td>3.91 (1.44–10.62)</td>
      <td>4.40 (1.62–11.92)</td>
      <td>4.20 (1.51–11.69)</td>
      <td>3.84 (1.44–10.23)</td>
      <td>4.33 (1.60–11.69)</td>
    </tr>
    <tr>
      <td>Unknown</td>
      <td>3/5 (60%)</td>
      <td>2/5 (40%)</td>
      <td>0.53 (0.03–10.58)</td>
      <td>NA</td>
      <td>NA</td>
      <td>NA</td>
      <td>NA</td>
      <td>NA</td>
      <td>NA</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>Current smoking</td>
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
      <td></td>
    </tr>
    <tr>
      <td>Yes</td>
      <td>18/43 (42%)</td>
      <td>25/43 (58%)</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
    </tr>
    <tr>
      <td>No</td>
      <td>80/294 (27%)</td>
      <td>214/294 (73%)</td>
      <td>3.02 (1.19–7.63)</td>
      <td>3.24 (1.15–9.18)</td>
      <td>3.12 (1.04–9.39)</td>
      <td>3.33 (1.12–9.94)</td>
      <td>3.54 (1.23–10.15)</td>
      <td>3.14 (1.10–8.97)</td>
      <td>3.16 (1.05–9.53)</td>
      <td>3.42 (1.21–9.69)</td>
      <td>3.10 (1.09–8.80)</td>
    </tr>
    <tr>
      <td>Unknown</td>
      <td>1/3 (33%)</td>
      <td>2/3 (67%)</td>
      <td>8.06 (0.17–386.04)</td>
      <td>NA</td>
      <td>NA</td>
      <td>NA</td>
      <td>NA</td>
      <td>NA</td>
      <td>NA</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>SARS-CoV-2 variant</td>
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
      <td></td>
    </tr>
    <tr>
      <td>non-Alpha/Beta/Delta</td>
      <td>5/19 (26%)</td>
      <td>14/19 (74%)</td>
      <td>1.21 (0.15–9.96)</td>
      <td>1.19 (0.14–10.06)</td>
      <td>1.13 (0.12–10.46)</td>
      <td>1.61 (0.18–14.66)</td>
      <td>1.27 (0.13–12.50)</td>
      <td>1.08 (0.12–9.43)</td>
      <td>1.17 (0.13–10.77)</td>
      <td>1.49 (0.18–12.64)</td>
      <td>1.08 (0.13–9.25)</td>
    </tr>
    <tr>
      <td>Alpha</td>
      <td>2/17 (12%)</td>
      <td>15/17 (88%)</td>
      <td>3.19 (0.24–42.01)</td>
      <td>4.61 (0.31–69.26)</td>
      <td>3.79 (0.24–60.31)</td>
      <td>7.77 (0.49–122.66)</td>
      <td>18.70 (0.95–368.10)</td>
      <td>3.19 (0.19–53.63)</td>
      <td>4.30 (0.28–65.69)</td>
      <td>5.42 (0.36–82.77)</td>
      <td>3.92 (0.26–60.08)</td>
    </tr>
    <tr>
      <td>Beta</td>
      <td>70/230 (30%)</td>
      <td>160/230 (70%)</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
      <td>Reference</td>
    </tr>
    <tr>
      <td>Delta</td>
      <td>8/50 (16%)</td>
      <td>42/50 (84%)</td>
      <td>3.00 (0.64–13.99)</td>
      <td>3.00 (0.60–14.89)</td>
      <td>2.78 (0.54–14.39)</td>
      <td>3.63 (0.72–18.44)</td>
      <td>4.08 (0.73–22.94)</td>
      <td>2.29 (0.44–11.95)</td>
      <td>2.92 (0.57–14.94)</td>
      <td>3.40 (0.69–16.67)</td>
      <td>2.33 (0.45–12.09)</td>
    </tr>
    <tr>
      <td>Variant Unknown</td>
      <td>14/24 (58%)</td>
      <td>10/24 (42%)</td>
      <td>0.48 (0.09–2.57)</td>
      <td>0.45 (0.08–2.48)</td>
      <td>0.45 (0.08–2.67)</td>
      <td>0.47 (0.08–2.72)</td>
      <td>0.37 (0.06–2.29)</td>
      <td>0.46 (0.08–2.56)</td>
      <td>0.46 (0.08–2.70)</td>
      <td>0.46 (0.09–2.44)</td>
      <td>0.46 (0.08–2.56)</td>
    </tr>
    <tr>
      <td>Median daily duration *</td>
      <td>460 (165–1,250)</td>
      <td>680 (160–1,760)</td>
      <td>1.00 (1.00–1.00)</td>
      <td></td>
      <td>1.00 (1.00–1.00)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Maximum duration †</td>
      <td>39 (10–81)</td>
      <td>39 (13–96)</td>
      <td>0.99 (0.99–1.00)</td>
      <td></td>
      <td></td>
      <td>1.00 (0.99–1.00)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Median average daily duration ‡</td>
      <td>33 (28–44)</td>
      <td>37 (28–47)</td>
      <td>0.98 (0.96–0.99)</td>
      <td></td>
      <td></td>
      <td></td>
      <td>0.98 (0.96–0.99)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Cumulative time in contact §</td>
      <td>95 (46–198)</td>
      <td>127 (40–363)</td>
      <td>1.00 (1.00–1.00)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>1.00 (1.00–1.00)</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Median daily frequency ¶</td>
      <td>13 (5–27)</td>
      <td>18 (4–38)</td>
      <td>0.99 (0.99–1.00)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>1.00 (0.99–1.01)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Maximum frequency **</td>
      <td>41 (15–83)</td>
      <td>46 (18–100)</td>
      <td>0.99 (0.99–1.00)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>1.00 (0.99–1.00)</td>
      <td></td>
    </tr>
    <tr>
      <td>Daily average frequency ††</td>
      <td>2.4 (1.0–3.7)</td>
      <td>2.9 (1.0–6.8)</td>
      <td>1.01 (0.98–1.04)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>1.03 (0.97–1.10)</td>
    </tr>
  </tbody>
</table>

_1 n/ row N (%); Median (interquartile range).*Median daily duration (median of cumulative duration of close-range proximity events for each day of deployment, in minutes).†Maximum duration (longest duration of a close-range proximity event during deployment, in minutes).‡Median average daily duration (median of cumulative duration of close-range proximity events in the day divided by the cumulative number of close-range proximity events during that day, in minutes).§Cumulative time in contact (cumulative duration of close-range proximity events over the deployment period divided by the number of days sensor was worn, in minutes).¶Median daily frequency (median of number of close proximity events for each day of deployment).**Maximum frequency (highest number of close proximity events in one day during deployment).††Daily average frequency (cumulative duration of close-range proximity events over the deployment period divided by the cumulative number of close-range proximity events during the deployment period). aOR: adjusted odds ratio. Significant associations on multivariable analysis in boldface. Factors investigated but not found significant on multivariable analysis: sex, HIV status, and underlying conditions._

## Discussion

In this case-ascertained, prospective household transmission study we did not find an association between the duration and frequency of close-range proximity events with SARS-CoV-2 infected household members and transmission in the household.

High-resolution contact patterns have been previously used in the context of pathogen transmission. Examples include investigating influenza virus transmission routes in a hospital setting (Whitney, 2016), and contact surveys to show the association between contacts, locations, and influenza infection (Kwok et al., 2014). For bacterial infections, the high correlation between pneumococcal infection risk and contact behavior has been shown (Qian et al., 2022), and in the context of tuberculosis transmission, it was shown that contact with adults is more important than contact with children (Dodd et al., 2016). To our knowledge, there are few data available on the direct association of close-range proximity events and SARS-CoV-2, and none make use of high-resolution contact data. During contact tracing efforts early in the pandemic in Singapore, it was found that sharing a bedroom with an index case and speaking to the index case for 30 min or longer increased the risk for infection (Ng et al., 2021). We did not see similar results when assessing sharing a bedroom with the index case, and this may be due to the already high level of crowding in included households. Although we observed an increase in infection risk with higher average contact durations with the index case on univariate analysis, this association was no longer seen when adjusting for age and other index and contact factors associated with transmission/acquisition. Mobile device geolocation has also been used to predict contact events between individuals on population level, and was used in transmission models to predict case numbers (Crawford et al., 2022). However, we did not find close-range proximity events to be an important driver for household transmission.

There are several possible reasons why we did not observe an association between close-range proximity events and SARS-CoV-2 transmission; these can be classified as related to transmission dynamics or study limitations. One possibility is that along with droplet-mediated transmission during close-proximity contacts, airborne (Meyerowitz et al., 2021; Wang et al., 2021), and to a lesser extent, fomite-mediated transmission (Meyerowitz et al., 2021) may also play a role in the transmission of SARS-CoV-2 in the household. More evidence is becoming available showing that aerosol transmission may be a more important transmission route for SARS-CoV-2 than initially anticipated, especially so in poorly ventilated indoor environments (Wang et al., 2021; Duval et al., 2022). Households in these communities do not have central air-conditioning or heating (Mathee et al., 2021), and during the winter months ventilation may be poorer than in summer, although we did not measure this. Furthermore, sensors only measure face-to-face interactions, and if individuals were close to each other but not directly facing one another for extended durations, we would not have measured this, although sharing of the same air may have occurred. The ventilation within households should be considered in future studies, as this can be a target for intervention strategies to reduce secondary transmission. The high level of interaction in relatively crowded South African households may already be above the threshold for transmission risk, with host characteristics like index viral load and contact age being more important to determine infection risk in this context. It is of interest that close-range proximity patterns within the household did not fully account for the differences in transmission based on age; with teenagers and adults experiencing the highest infection risk, but children aged 5–17 years having the highest contacts.

Our study had limitations both in design and execution. Due to the nature of the case-ascertained study design, we would have missed the period when the index case was most infectious, just before symptom onset (Meyerowitz et al., 2021), and the close-range contact patterns measured during the study may have been different after the household members were aware of the index SARS-CoV-2 case (leading to reduced contact), and again once secondary cases were informed of their infection status (leading to increased contact). We also did not collect any information on possible NPI usage in the households, like wearing masks. A study from South Africa showed that individuals staying at home were less likely to wear a mask (Burger et al., 2022), but these data were not ascertained during a time when a household member was infected with SARS-CoV-2. We also did not consider where contacts took place (indoors or outdoors), which relates to ventilation and may have influenced transmission. We may have also misclassified the true index case if they were asymptomatic, and did not consider tertiary transmission chains in the index-directed analysis. To adjust for possible misclassification, we performed a grouped assessment investigating close-range proximity events with all SARS-CoV-2 infected household members. This grouped analysis may also have diluted possible associations with the true infector. Furthermore, although based on legislation, close contacts (including household contacts) of SARS-CoV-2 cases were supposed to quarantine, compliance was not monitored. Therefore, household contacts could have been exposed to non-household SARS-CoV-2 cases during the follow-up period. We did not consider multiple introductions of SARS-CoV-2 within the household, although we did exclude households with more than one SARS-CoV-2 variant detected. During the peaks of waves of infection in South Africa, one variant was responsible for the majority of the infections (National Institute for Communicable Diseases, 2022b), and the additional introductions within the household were likely to have been the same as the initial variant. Higher resolution sequencing data may be useful to more accurately identify chains of transmission within the household. Combining contact data with clinical and virological/bacteriological data has been shown to be useful to reconstruct transmission networks (Campbell et al., 2019), and we will consider this for future analyses. Our measurement of close-range contact patterns was also limited by compliance, as during the cleaning process we identified 73 sensors that were not worn, based on accelerometer data. We also had limited data in some households, where some individuals did not consent to the contact aspect of the study, or where we were unable to retrieve data due to hardware failure, lost, or damaged tags. The small sample size may have reduced our power to detect small differences in close proximity event parameters between those infected with SARS-CoV-2 and those not infected.

In conclusion, we did not observe an association between close-proximity contacts and SARS-CoV-2 transmission in the household. A case-ascertained, prospective household transmission study may not be well suited to investigate this question. A possible other study design to consider is randomly selected prospective household cohorts, but the deployment of sensors for extended periods of time may be logistically challenging and lead to participant fatigue, and households in a cohort may not experience infection episodes unless the community attack rate is very high. High-resolution contacts in other settings like schools or workplaces where contacts are less frequent could be useful to identify the type of contact events that may lead to SARS-CoV-2 transmission. If aerosol transmission plays a more important role in transmission than droplet-mediated transmission, ventilation within households can also be an important consideration for future studies. Increased ventilation could potentially be a method to reduce secondary transmission in households. Nevertheless, our study provides high-resolution household contact data that can be used to parametrize future transmission models, not only for SARS-CoV-2, but other pathogens as well.
