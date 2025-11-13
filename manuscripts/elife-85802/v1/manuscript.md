# Effect of an enhanced public health contact tracing intervention on the secondary transmission of SARS-CoV-2 in educational settings: The four-way decomposition analysis

## Authors

- Olivera Djuric<sup>1</sup> ([ORCID: 0000-0002-8574-5938](https://orcid.org/0000-0002-8574-5938)) †
- Elisabetta Larosa<sup>3</sup>
- Mariateresa Cassinadri<sup>3</sup>
- Silvia Cilloni<sup>3</sup>
- Eufemia Bisaccia<sup>3</sup>
- Davide Pepe<sup>3</sup>
- Laura Bonvicini<sup>1</sup>
- Massimo Vicentini<sup>1</sup>
- Francesco Venturelli<sup>1</sup> ([ORCID: 0000-0002-9190-8668](https://orcid.org/0000-0002-9190-8668))
- Paolo Giorgi Rossi<sup>1</sup> ([ORCID: 0000-0001-9703-2460](https://orcid.org/0000-0001-9703-2460))
- Patrizio Pezzotti<sup>4</sup>
- Alberto Mateo Urdiales<sup>4</sup>
- Emanuela Bedeschi<sup>3</sup>

### Affiliations

1. Epidemiology Unit, Azienda Unità Sanitaria Locale – IRCCS di Reggio Emilia Reggio Emilia Italy ([ROR:001bbwj30](https://ror.org/001bbwj30))
2. Centre for Environmental, Nutritional and Genetic Epidemiology (CREAGEN), University of Modena and Reggio Emilia Modena Italy ([ROR:02d4c4y02](https://ror.org/02d4c4y02))
3. Public Health Unit, Azienda Unità Sanitaria Locale-IRCCS di Reggio Emilia Reggio Emilia Italy ([ROR:001bbwj30](https://ror.org/001bbwj30))
4. Department of Infectious Diseases, Istituto Superiore di Sanità Rome Italy ([ROR:02hssy432](https://ror.org/02hssy432))

† Corresponding author

## Abstract

Background:The aim of our study was to test the hypothesis that the community contact tracing strategy of testing contacts in households immediately instead of at the end of quarantine had an impact on the transmission of SARS-CoV-2 in schools in Reggio Emilia Province.Methods:We analysed surveillance data on notification of COVID-19 cases in schools between 1 September 2020 and 4 April 2021. We have applied a mediation analysis that allows for interaction between the intervention (before/after period) and the mediator.Results:Median tracing delay decreased from 7 to 3.1 days and the percentage of the known infection source increased from 34–54.8% (incident rate ratio-IRR 1.61 1.40–1.86). Implementation of prompt contact tracing was associated with a 10% decrease in the number of secondary cases (excess relative risk –0.1 95% CI –0.35–0.15). Knowing the source of infection of the index case led to a decrease in secondary transmission (IRR 0.75 95% CI 0.63–0.91) while the decrease in tracing delay was associated with decreased risk of secondary cases (1/IRR 0.97 95% CI 0.94–1.01 per one day of delay). The direct effect of the intervention accounted for the 29% decrease in the number of secondary cases (excess relative risk –0.29 95%–0.61 to 0.03).Conclusions:Prompt contact testing in the community reduces the time of contact tracing and increases the ability to identify the source of infection in school outbreaks. Although there are strong reasons for thinking it is a causal link, observed differences can be also due to differences in the force of infection and to other control measures put in place.Funding:This project was carried out with the technical and financial support of the Italian Ministry of Health – CCM 2020 and Ricerca Corrente Annual Program 2023.

## Introduction

Closure of educational institutions was one of the non-pharmacological infection control measures often adopted during the pandemic of SARS-CoV-2, mostly based on the temporal coincidence between schools reopening and COVID-19 outbreaks in some countries and the concern regarding potential school-to-home transmissions of the virus from students to more susceptible family members.

Evidence of SARS-CoV-2 transmission in educational settings indicates not only that schools opening and closing have a small impact on the increase or decrease of SARS-CoV-2 rates in the population, but that transmission is even lower in schools than that in the general population (Winje et al., 2022; Gandini et al., 2021; Viner et al., 2022). However, the risk of in-school SARS-CoV-2 transmission is still considered high, making prevention measures vital to restoring in-person learning (European Centre for Disease Prevention and Control, 2020a; European Centre for Disease Prevention and Control, 2020b). The control of infection in school-age children became even more critical after the introduction of mass vaccination, which reduced transmission between adults, and with the spread of the Omicron variant, which has much higher transmissibility in indoor settings.

Timely reporting of COVID-19 cases to the health authorities and case investigation, followed by timely testing, contact tracing, and isolation, remain crucial to allow safe resumption of in-presence activities. Contact tracing practices have been subject to changes over time along with emerging evidence and the introduction of the vaccine. In the operational document from September 2021, the Centers for Disease Control and Prevention (CDC) recommended that people get tested at least after five days from close contact with a person with COVID-19 Centers for Disease Control and Prevention, 2021, while the European Centre for Disease Prevention and Control (ECDC) recommended testing all high-risk exposure contacts, whether vaccinated or not, as soon as possible after they have been identified to allow for further contact tracing (European Centre for Disease Prevention and Control, 2020b). Regardless of this, it has always been acknowledged that isolation of contacts is effective if initiated shortly after confirmation of the index case since the delay in isolation of contacts has a major impact on the transmission of the virus (Kretzschmar et al., 2020).

Enhanced contact tracing, such as backward contact tracing, has also been recommended to facilitate the identification of the primary case, also called ‘source’ or ‘original’ case from which an index case acquired his/her infection (European Centre for Disease Prevention and Control, 2020b; Centers for Disease Control and Prevention, 2021). The rationale behind this recommendation is to stop chain transmission that originates from this relatively small proportion of primary cases usually responsible for a large proportion of transmission. By extending the contact tracing window or performing source investigation, BCT aims to identify asymptomatic cases that are the actual source of newly detected (index) cases. Modeling studies show that primary cases generate 3–10 times more infections than a randomly chosen case (Endo et al., 2020). These cases would not have otherwise been identified and, in the case of educational settings, would not have been linked to school investigation. Given that BCT tends to ‘catch’ infection sources at the end of their infectious period, it is highly susceptible to testing and contact tracing delays, therefore, it is meaningful only in the presence of prompt tracing of contacts (Raymenants et al., 2022).

Starting from 27 November 2020, the local health authority of Reggio Emilia, Italy, improved contact tracing protocols by introducing prompt molecular tests for all contacts, whether symptomatic or asymptomatic, at the beginning of quarantine (test to trace), with the aim to identify all possible sources of infection in asymptomatic contacts. Before the intervention, contacts of index cases were only tested at the end of the isolation period (test to release). In this way, primary (asymptomatic) cases were not diagnosed or were diagnosed very late in their infection course and, given that they were not attending school since they were isolated, they were not indicated as a school contact until one of the school contacts become symptomatic (Figure 1 and Figure 2). Given that a large part of the infections in students is asymptomatic or paucisymptomatic, they are often identified when an adult in the same household presents symptoms. Prompt testing of all contacts in community allows the timely identification of positive children/teachers who may be primary cases in school outbreaks, thus, allowing a prompt investigation in the school setting to start.

![Figure 1.](https://cdn.elifesciences.org/articles/85802/elife-85802-fig1-v1.jpg)

**Figure 1.:** (A) In standard contact tracing, all close contacts were quarantined after identifying a case in the community. Contacts were only tested at the end of the quarantine or if symptomatic. Only for school contacts, immediate testing of all classmates was performed; if one or more classmates resulted positive, the whole class was quarantined. (B) In backward contact tracing, close contacts were also immediately tested, independently from the presence of symptoms. The tracing and quarantine policy in schools was similar. In the proposed example, after the diagnosis of a symptomatic household member, backward tracing would identify an asymptomatic child, thus allowing the extension of investigation to his school contacts and eventually stopping secondary transmission in the class.

![Figure 2.](https://cdn.elifesciences.org/articles/85802/elife-85802-fig2-v1.jpg)

**Figure 2.:** In panel A we report the scenario without prompt contact testing in community and its effect on the SARS-CoV-2 transmission in educational setting. Day 0: One of the children in a household became infected (primary case) but asymptomatic (gray). Day 5: One parent and one classmate became infected, also asymptomatic (gray). Day 10: The infected parent became symptomatic (orange), tested positive (red circle), and considered an index case of the household. Entire family is quarantined (bold line) but not tested immediately. Meanwhile, the primary case transmits infection further to two other classmates. Classmates of the primary case are not tested because they are not identified as school contacts due to late testing of the household contacts. Day 20: Family members of the index case are tested at the end of the quarantine. One positive classmate of the primary case became symptomatic, tested positive, and considered an index case in the school cluster given that the classmates were not considered contacts of the primary case since he was already isolated. Other classmates are tested only when an index case occurs. Panel B illustrates the scenario with prompt contact testing in community. Day 10: The infected parent became symptomatic, tested positive, and entire family was quarantined and tested at the beginning of quarantine. Primary case is identified promptly, his classmates are identified as contacts, tested, and isolated preventing further transmission of the virus.

This study aimed to estimate the impact of changing contact tracing intervention from testing contacts at the end of quarantine to testing contacts immediately, on the secondary transmission of SARS-CoV-2 in educational settings in Reggio Emilia Province. To better understand the mechanism of the possible impact that the intervention has on secondary transmission, we assessed whether this association is mediated by two process indicators, tracing delay and effective tracing, measured as known sources of infection of the index case and proportion of asymptomatic index cases, which were the actual target of the intervention, bearing in mind limits of the before-and-after design of this study conducted in a period when several changes could confound the results.

## Methods

### Design and setting

In the present study, population-based surveillance data were analysed including 1604 consecutive positive cases confirmed with RT-PCR for SARS-COV-2 infection between 1 September 2020 and 4 April 2021 in Reggio Emilia Province that led to an epidemiological investigation among children and adolescents (0–19 years old) or school staff in 1884 classes who may have been exposed or in contact with positive cases at school.

In Reggio Emilia Province (531,751 inhabitants, Emilia Romagna, Northern Italy) there are approximately 95,000 inhabitants from 6 months-olds to 19-year-olds attending infant-toddler centres (ages 0–3), preschools (ages 3–5), primary schools (ages 6–10), middle schools (ages 11–13), and high schools (ages 14–19), and about 12,000 teachers/school staff members.

During the study period, there were two peaks of infections: in November 2020 and in February/March 2021 (Figure 3; Istituto Superiore di Sanità, 2021). After the school reopening on 1 September 2020 for preschool and remedial courses and, on 15 September 2020, for the regular school year, in-class learning was in place until 26 October 2020 when policies to reduce crowding especially in high schools were introduced (reducing the in-class time by 50–75%) as were several short closures in the periods of highest incidence. In addition, because of the high circulation of the virus, the Christmas school holidays were extended to the second week of January (from 20 December to 11/15 January). Another lockdown led to the closing of schools on 3 March 2021. Only infant-toddler centres and preschools, schools that require laboratory work, and schools with pupils with disabilities or special needs continued in-presence didactic activities.

![Figure 3.](https://cdn.elifesciences.org/articles/85802/elife-85802-fig3-v1.jpg)

**Figure 3.:** The graph also reports the main changes in school opening and school closures and the proportion of Alpha variants (green area) among sequenced cases reported by the Italian National Institute of Health.

Infection control measures in place during the study period were previously described in detail Larosa et al., 2020; Djuric et al., 2022; Regione et al., 2020.

### Intervention

Starting from 27 November 2020, the local health authority improved contact tracing protocols and introduced immediate molecular tests for all contacts, whether symptomatic or asymptomatic, at the beginning of quarantine, with the aim to identify all possible sources of infection in asymptomatic contacts and facilitate backward tracing (Djuric et al., 2022). This strategy was applied to all contacts, independently from the setting of infection, including all household members of sporadic cases, and particular attention was given to testing of children and adolescents because they were most commonly asymptomatic. This strategy was explicitly thought to correctly identify in a timely manner the contacts of asymptomatic cases before they started the quarantine. Testing only at the end of quarantine guarantees a safe return to the community of contacts and to identify secondary transmission in the cluster, but, by definition, assumes that the asymptomatic cases are secondary cases and became infectious during the quarantine and thus could not have contacts.

### Outcome and variables of interest

The main outcome was the number of secondary cases per class; we preferred to use the absolute number instead of the attack rate, because we were interested in assessing whether the intervention limited the number of secondary cases and not the probability of being infected given that an exposure occurred. Three process indicators of contact tracing performance were considered. The first one, tracing delay, was calculated as the time from the swab positivity of the index case to the date on which the swab for (the majority of) classmates was scheduled. The second indicator was the proportion of index cases who had close contact with a known COVID-19 case in the ten days before the onset of symptoms or diagnosis. This indicator, called ‘the known source of infection of the index case,’ is a proxy of backward contact tracing success, which should reflect the extent to which school index cases were tested and linked to the school investigation because of a known contact with a positive person. Finally, the third indicator was the proportion of asymptomatic index cases. This indicator is also a proxy of backward tracing, because in the absence of screening, asymptomatic cases are mostly identified during contact tracing and to become an index case of school investigation this testing should not be done at the end of quarantine. We also reported testing delay, i.e., the delay in the diagnosis of the index case, defined as the number of days between symptom onset and the date of swab positivity, but this indicator is expected to only be marginally influenced by contact tracing strategies.

### Definitions and assumptions

The first case that tested positive (considering the date on which the swab was done) per class was considered an index case. If more than one case in a class tested positive on the same day, the one with the earliest symptom onset was considered the index case. The same class can be included more than once in the analysis because it may have been involved in more than one investigation during the study period.

When more than one class was included in a between-class transmission, index cases belonging to different classes had shared exposures, or there was a single index case for more than one class (usually, but not only, when the index case was a teacher), this was considered a multi-class cluster.

The overall attack rate was calculated by dividing the number of cases by the population at risk; i.e., classmates, teachers/staff who had had close contact with the index case in a period starting from 48 hr before symptom onset of the symptomatic index case and, for asymptomatic cases, 48 hr before diagnosis.

If a classmate was already in isolation prior to symptom onset or swab positivity of the index case, due to contact with a positive person or re-entry from abroad, he/she was excluded from the denominator. Any student or staff who refused to perform a swab was excluded from the denominator.

### Data sources

Following the identification and notification of a COVID-19 case, qualified Public Health Department (PHD) personnel performed a detailed field investigation and managed the index case and identified contacts according to the regional recommendations and control measures in place. Comprehensive surveillance data containing information on index cases, contacts, school and class characteristics, swabs performed, secondary cases, and measures undertaken, were collected by PHD, and stored in electronic forms. Each case and cluster were re-abstracted by a study investigator and checked for consistency and plausibility. Missing data were imputed from the COVID-19 Surveillance Registry software and a de-identified research database was constructed for the analysis.

### Statistical analysis

During the study period, many factors that could influence secondary transmission in schools occurred, including changes in overall incidence, changes in in-school and out-of-school (especially transport and leisure-time activities) control measures, time of in-person and distance teaching, and the spread of the Alpha variant. Therefore, simply measuring the outcome before and after the intervention would be surely biased and would not allow any causal inference.

To test the hypothesis that the contact tracing strategy in the community had an impact on the secondary case transmission in schools, we defined a direct acyclic graph identifying the possible causal pathways, including possible mediators and possible confounders (Figure 4).

![Figure 4.](https://cdn.elifesciences.org/articles/85802/elife-85802-fig4-v1.jpg)

First, we assessed if the possible known confounders were associated with the intervention (i.e. were they differently distributed in the before and after periods), and with the outcome (i.e. the number of secondary cases). Then we assessed if the introduction of the new strategy actually changed the tracing process analysing the trend of the timeliness of testing and effectiveness of tracing (measured as the proportion of index cases with a known source of infection and proportion of symptomatic index cases) during the study period. The class was the statistical unit for analyses. Median tracing delay and the proportion of index cases with the known source of infection were compared before and after the implementation of the intervention (27 November 2020). Second, we tested the association between the three process indicators that were the direct target of the new tracing strategy and the final health outcome (number of secondary cases). Three negative binomial regression models were constructed with the number of secondary cases per class as outcome and intervention indicators as exposures. Models were adjusted for types of school (infant-toddler centre, primary school, middle school, high school, other educational services), class size (<21 and ≥21 pupils), and types of the index case (student vs. teacher). Given that tracing delay and known contact were strongly negatively correlated (r=–0.76), their effects were analysed separately. With a similar model, we also measured the association between the intervention and the outcome.

Lastly, a novel effect decomposition method was used in a subset of pre-Alpha variant (before 31 December 2020) classes to test whether one of the two process indicators mediated the association between intervention and the number of secondary cases. This method was chosen because we assumed that there might be an association between exposure variables (before and after public health intervention) and mediator variables (process indicators). Assumptions about mediation analysis on unconfounded associations between variables were tested by performing a set of abovementioned analyses and following and based on the direct acyclic graph. The total effect of the intervention on the number of secondary cases is expressed as the excess relative risk (ERR); i.e., an incidence risk ratio (IRR) from the negative binomial regression minus one. In the presence of an intervention-mediator interaction, ERR is decomposed into four components: controlled directed effect (CDE) due to intervention only, at a fixed level of the mediator; pure indirect effect (PIE) due to mediation only; reference interaction (IntRef) due to interaction only; and mediated interaction (IntMed) due to mediation and interaction (VanderWeele, 2014). Supplementary file 1 reports a plain language definition of the mediation analysis definitions. Given that classes could not be randomly assigned to the intervention and control group, and that the period before the intervention was used for the comparison, we assume that there might be a substantial interaction between the period before and after the intervention and two mediators. Stata’s ‘Med4way’ command was used to estimate mediation and interaction effects simultaneously (Discacciati et al., 2019). Incidence rate ratios with a 95% confidence interval (CI) were reported and used for hypothesis testing. The Stata code used is provided in the Supplementary file 2. All analyses in this study were conducted using STATA 13.0 SE (Stata Corporation, Texas, TX).

## Results

### Description of investigated classes and secondary transmission

We investigated 1884 classes overall, 1882 in which at least one case/contact was recorded, and two classes where screening was done due to out-of-school contact with an index case from another class. One thousand seven hundred and five secondary cases (1047 students and 658 teachers/staff) were identified among 43,214 tested contacts linked to 1604 index cases, resulting in an overall secondary attack rate of 3.9% (95%CI 3.8–4.1).

The median number of secondary cases per class was 1 (IQR 1–3); 2 before, and 1 after the intervention (test of equal medians p=0.092) (Table 1). The proportion of classes where secondary transmission occurred was overall 38.6%; 37.4% before and 39.0% after the intervention.

**Table 1.**
 Characteristics of 1884 classes and 1604 index cases for which a school contact with COVID-19 cases was suspected, before, and after the intervention.


<table>
  <thead>
    <tr>
      <th></th>
      <th>n (%)</th>
      <th>Before interventionn=490</th>
      <th>After interventionn=1394</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Classes (n=1884)</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Type of school</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Infant-toddler centre</td>
      <td>350 (18.5)</td>
      <td>107 (21.8)</td>
      <td>243 (17.4)</td>
    </tr>
    <tr>
      <td>Primary school</td>
      <td>540 (28.7)</td>
      <td>125 (25.5)</td>
      <td>415 (29.8)</td>
    </tr>
    <tr>
      <td>Middle school</td>
      <td>496 (26.3)</td>
      <td>128 (26.1)</td>
      <td>368 (26.4)</td>
    </tr>
    <tr>
      <td>High school</td>
      <td>478 (25.4)</td>
      <td>129 (26.3)</td>
      <td>349 (25.0)</td>
    </tr>
    <tr>
      <td>Other educational services</td>
      <td>20 (1.1)</td>
      <td>1 (0.2)</td>
      <td>19 (1.4)</td>
    </tr>
    <tr>
      <td>Calendar period</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>September/October</td>
      <td>248 (13.1)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>November</td>
      <td>263 (13.9)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>December</td>
      <td>316 (16.8)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>January</td>
      <td>265 (14.1)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>February</td>
      <td>523 (27.8)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>March/April</td>
      <td>269 (14.3)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Class size</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>&lt;21</td>
      <td>862 (45.7)</td>
      <td>191 (39.0)</td>
      <td>671 (48.1)</td>
    </tr>
    <tr>
      <td>≥21</td>
      <td>1011 (53.7)</td>
      <td>293 (59.8)</td>
      <td>718 (51.5)</td>
    </tr>
    <tr>
      <td>Missing</td>
      <td>11 (0.6)</td>
      <td>6 (1.2)</td>
      <td>5 (0.4)</td>
    </tr>
    <tr>
      <td>Secondary transmission</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>No</td>
      <td>1157 (61.4)</td>
      <td>307 (62.6)</td>
      <td>850 (61.0)</td>
    </tr>
    <tr>
      <td>Yes</td>
      <td>727 (38.6)</td>
      <td>183 (37.4)</td>
      <td>544 (39.0)</td>
    </tr>
    <tr>
      <td>Number of secondary cases*</td>
      <td>1 (1-3)</td>
      <td>2 (1-3)</td>
      <td>1 (1-3)</td>
    </tr>
    <tr>
      <td>Mean attack rate</td>
      <td>0.1 (0.04–0.12)</td>
      <td>0.1 (0.04–0.12)</td>
      <td>0.1 (0.04–0.12)</td>
    </tr>
    <tr>
      <td>Part of a school cluster</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>No</td>
      <td>1 367 (72.6)</td>
      <td>368 (75.1)</td>
      <td>999 (71.7)</td>
    </tr>
    <tr>
      <td>Yes</td>
      <td>517 (27.4)</td>
      <td>122 (24.9)</td>
      <td>395 (28.3)</td>
    </tr>
    <tr>
      <td>Tracing delay*</td>
      <td>3 (2-5)</td>
      <td>7 (5-10)</td>
      <td>3 (2-4)</td>
    </tr>
    <tr>
      <td>Testing delay*</td>
      <td>4 (2-8)</td>
      <td>5 (3-8)</td>
      <td>4 (2-7)</td>
    </tr>
    <tr>
      <td>Index cases (n=1604)</td>
      <td></td>
      <td>n=429</td>
      <td>n=1,175</td>
    </tr>
    <tr>
      <td>Type of index case</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Student</td>
      <td>1213 (75.6)</td>
      <td>321 (74.8)</td>
      <td>892 (75·9)</td>
    </tr>
    <tr>
      <td>Teacher</td>
      <td>391 (24.4)</td>
      <td>108 (25.2)</td>
      <td>283 (24.1)</td>
    </tr>
    <tr>
      <td>Index case symptomatic</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>No</td>
      <td>298 (18.6)</td>
      <td>63 (14.7)</td>
      <td>235 (20)</td>
    </tr>
    <tr>
      <td>Yes</td>
      <td>1306 (81.4)</td>
      <td>366 (85.3)</td>
      <td>940 (80)</td>
    </tr>
    <tr>
      <td>Potential source of infection</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Unknown</td>
      <td>814 (50.7)</td>
      <td>283 (66·0)</td>
      <td>531 (45.2)</td>
    </tr>
    <tr>
      <td>Known</td>
      <td>790 (49.3)</td>
      <td>146 (34·0)</td>
      <td>644 (54.8)</td>
    </tr>
    <tr>
      <td>Type of source</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Household outbreak</td>
      <td>614 (77.7)</td>
      <td>97 (66.4)</td>
      <td>517 (80.3)</td>
    </tr>
    <tr>
      <td>Social contact</td>
      <td>26 (3.3)</td>
      <td>7 (4.8)</td>
      <td>19 (2.9)</td>
    </tr>
    <tr>
      <td>Sport contact</td>
      <td>18 (2.3)</td>
      <td>7 (4.8)</td>
      <td>11 (1.7)</td>
    </tr>
    <tr>
      <td>Unidentifiable contact</td>
      <td>132 (16.7)</td>
      <td>35 (24.0)</td>
      <td>97 (15.1)</td>
    </tr>
  </tbody>
</table>

_*Median (IQR), calculated only in classes with secondary transmission._

The number of symptomatic index cases decreased in the period after intervention from 85.3–80%. There were no changes in the number of classes that made up part of a multi-class cluster, as well as in the type of index case.

Secondary transmission was associated with the type of index case; it was lower among teachers than among students (IRR 0.75 95% CI 0.61–0.92) (Table 2).

**Table 2.**
 Association between class or index case characteristics (potential confounders) and number of secondary cases.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Number of classes with secondary transmission</th>
      <th>Number of secondary cases</th>
      <th>IRR* (95% CI)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Classes (n=1884)</td>
      <td>n=727</td>
      <td>n=1706</td>
      <td></td>
    </tr>
    <tr>
      <td>Type of school</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Infant-toddler centre</td>
      <td>131 (18.2)</td>
      <td>349</td>
      <td>ref</td>
    </tr>
    <tr>
      <td>Primary school</td>
      <td>217 (29.8)</td>
      <td>553</td>
      <td>1.03 (0.80–1.31)</td>
    </tr>
    <tr>
      <td>Middle school</td>
      <td>172 (23.7)</td>
      <td>386</td>
      <td>0.78 (0.60–1.01)</td>
    </tr>
    <tr>
      <td>High school</td>
      <td>202 (27.8)</td>
      <td>409</td>
      <td>0.86 (0.66–1.11)</td>
    </tr>
    <tr>
      <td>Other educational services</td>
      <td>5 (0.7)</td>
      <td>9</td>
      <td>0.45 (0.17–1.18)</td>
    </tr>
    <tr>
      <td>Class size</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>&lt;21</td>
      <td>316 (43.5)</td>
      <td>751</td>
      <td>ref</td>
    </tr>
    <tr>
      <td>≥21</td>
      <td>411 (56.5)</td>
      <td>955</td>
      <td>1.08 (0.91–1.29)</td>
    </tr>
    <tr>
      <td>Index cases (n=1604)</td>
      <td>n=640</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Type of index case</td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Student</td>
      <td>477 (74.5)</td>
      <td>1047</td>
      <td>ref</td>
    </tr>
    <tr>
      <td>Teacher</td>
      <td>163 (25.5)</td>
      <td>658</td>
      <td>0.75 (0.61–0.92)</td>
    </tr>
    <tr>
      <td>Screening</td>
      <td>0</td>
      <td>1</td>
      <td>na</td>
    </tr>
  </tbody>
</table>

_*Relative risks are computed with negative binomial models with the count of secondary cases as a dependent variable._

We also tested the association between class or index case characteristics and the process indicators (Table 3). There was no difference in the number of index cases with known sources between types of school and class size. Percentage of known sources of infection was higher when the index case was a student compared to teachers (56.3% vs 26.7%). Median tracing delay was 3 days in all types of schools and index cases. There was more symptomatic index cases in infant-toddler centres and high schools than in primary schools and other educational services.

**Table 3.**
 Association between class or index case characteristics and the process indicators (potential mediators).


<table>
  <thead>
    <tr>
      <th></th>
      <th>Totaln</th>
      <th>Known source of infection of the index casen (%)*</th>
      <th>Index case symptomaticn (%)*</th>
      <th>Tracing delayMedian (IQR)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Classes (n=1884)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Type of school</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Infant-toddler centre</td>
      <td>350</td>
      <td>157 (44.9)</td>
      <td>281 (80.3)</td>
      <td>3 (2-5)</td>
    </tr>
    <tr>
      <td>Primary school</td>
      <td>540</td>
      <td>255 (47.2)</td>
      <td>355 (65.7)</td>
      <td>3 (2-5)</td>
    </tr>
    <tr>
      <td>Middle school</td>
      <td>496</td>
      <td>206 (41.5)</td>
      <td>293 (59.1)</td>
      <td>3 (2-6)</td>
    </tr>
    <tr>
      <td>High school</td>
      <td>478</td>
      <td>216 (45.2)</td>
      <td>360 (75.3)</td>
      <td>3 (2-6)</td>
    </tr>
    <tr>
      <td>Other educational services</td>
      <td>20</td>
      <td>7 (35.0)</td>
      <td>10 (50.0)</td>
      <td>3 (1.5–5)</td>
    </tr>
    <tr>
      <td>P value†</td>
      <td></td>
      <td>0.378</td>
      <td>0.001</td>
      <td>0.147</td>
    </tr>
    <tr>
      <td>Class size</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>&lt;21</td>
      <td>862</td>
      <td>375 (41.4)</td>
      <td>587 (81.6)</td>
      <td>3 (2-5)</td>
    </tr>
    <tr>
      <td>≥21</td>
      <td>1011</td>
      <td>461 (45.6)</td>
      <td>707 (69.9)</td>
      <td>3 (2-6)</td>
    </tr>
    <tr>
      <td>Missing</td>
      <td>11</td>
      <td>5 (45.5)</td>
      <td>5 (45.5)</td>
      <td>6 (3-7)</td>
    </tr>
    <tr>
      <td>p value†</td>
      <td></td>
      <td>0.661</td>
      <td>0.782</td>
      <td>0.367</td>
    </tr>
    <tr>
      <td>Index cases (n=1604)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Type of index case</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Student</td>
      <td>1213</td>
      <td>683 (56.3)</td>
      <td>957 (78.9)</td>
      <td>3 (2-5)</td>
    </tr>
    <tr>
      <td>Teacher</td>
      <td>391</td>
      <td>104 (26.7)</td>
      <td>342 (87.5)</td>
      <td>3 (2-6)</td>
    </tr>
    <tr>
      <td>p value†</td>
      <td></td>
      <td>&lt;0.001</td>
      <td>&lt;0.001</td>
      <td>0.486</td>
    </tr>
  </tbody>
</table>

_*Values are numbers with row percentages.†Kruskal-Wallis test._

### Association between intervention and process indicators

Overall median tracing delay was 3 days (IQR 2–5), decreasing from 7 (IQR 5–10) in the period before intervention to 3.1 (IQR 2–4) days in the period after intervention (Table 1). The testing delay also decreased from 5 to 4 days following the implementation of the intervention. The percentage of index cases with a known source of infection was 49.3%, and it increased from 34% in November to 54.8% in the period after intervention. The number of index cases that were part of a household outbreak increased from 66.4% before the intervention to 80.3% after the intervention. Weekly average contact tracing delay decreased while the percentage of known sources of infection increased in the period after intervention implementation (Figure 5).

![Figure 5.](https://cdn.elifesciences.org/articles/85802/elife-85802-fig5-v1.jpg)

**Figure 5.:** Lower graph: Weekly average contact tracing delay and percentage of index cases with a known source of infection.

### Association between process indicators and outcome

Results of negative binomial regression covering the entire period show that both known sources of infection (IRR 0.75 95% CI 0.63–0.91) and decrease in tracing delay (1/IRR 0.97 95% CI 0.94–1.01 for each day of avoided delay) were associated with the decrease of the number of secondary cases (Table 4). Sensitivity analyses restricted to the period before the spread of the Alpha variant showed similar results (Table 4).

**Table 4.**
 Negative binomial regression of the association between the number of secondary cases (outcome) and intervention promptness indicators (mediators).


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="2">Entire period(n=1884)</th>
      <th colspan="2">Before Alpha variant (n=827)</th>
    </tr>
    <tr>
      <th></th>
      <th>IRR*</th>
      <th>95% CI</th>
      <th>IRR*</th>
      <th>95% CI</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Tracing delay</td>
      <td>1.01</td>
      <td>0.99–1.04</td>
      <td>1.03</td>
      <td>0.99–1.07</td>
    </tr>
    <tr>
      <td>Known source of infection of the index case</td>
      <td>0.75</td>
      <td>0.63–0.91</td>
      <td>0.73</td>
      <td>0.55–0.96</td>
    </tr>
    <tr>
      <td>Index case symptomatic</td>
      <td>1.21</td>
      <td>0.96–1.53</td>
      <td>1.30</td>
      <td>0.93–1.82</td>
    </tr>
  </tbody>
</table>

_*Adjusted for the type of school, type of index case, and class size._

### Mediation analysis

Only the known source of infection of the index case was associated with the outcome (number of secondary cases) in multivariable analysis and it was, therefore, tested for the mediation and interaction in the four-way decomposition method.

Implementation of prompt contact tracing was associated with a 10% decrease in the number of secondary cases (excess relative risk –0.1 95% CI –0.35–0.15) (Table 5). The direct effect of the intervention accounted for the large part of the excess in risk (excess relative risk –0.29 95%–0.61– 0.03), leading to the 29% decrease in the number of secondary cases if the source of infection of the index case is known. Interaction only accounted for the other large part of the excess risk (excess relative risk 0.35 95% 0.03–0.68); knowing the source of infection of the index case in the period before the intervention when tracing delay was high, would increase the risk of secondary cases by 35%. However, we found evidence of mediated interaction that had a negative effect on the secondary transmission (excess relative risk –0.14 95% CI –0.28–0.01). The known source of infection of the index case alone accounted for only a small percent of the reduction of excess risk (excess relative risk –0.02 95% –0.10–0.07).

**Table 5.**
 Four-way decomposition mediation analysis of the association between intervention and the number of secondary cases.


<table>
  <thead>
    <tr>
      <th></th>
      <th>ERR*</th>
      <th>95% CI</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Total effect</td>
      <td>–0.1</td>
      <td>–0.35–0.15</td>
    </tr>
    <tr>
      <td>Controlled direct effect</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Known contact (M=1)</td>
      <td>–0.29</td>
      <td>–0.61–0.03</td>
    </tr>
    <tr>
      <td>Unknown contact (M=0)</td>
      <td>0.31</td>
      <td>–0.49 to –0.02</td>
    </tr>
    <tr>
      <td>Pure indirect effect</td>
      <td>–0.02</td>
      <td>–0.10–0.07</td>
    </tr>
    <tr>
      <td>Mediated interaction</td>
      <td>–0.14</td>
      <td>–0.28 to –0.01</td>
    </tr>
    <tr>
      <td>Reference interaction</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Known contact (M=1)</td>
      <td>0.35</td>
      <td>0.03–0.68</td>
    </tr>
    <tr>
      <td>Unknown contact (M=0)</td>
      <td>–0.25</td>
      <td>–0.49 to –0.02</td>
    </tr>
  </tbody>
</table>

_*Adjusted for the type of school, type of index case, and class size.ERR, excess relative risk; M, mediator (known source of infection of the index case)._

## Discussion

We found that both process indicators used to evaluate the contact tracing intervention (tracing delay and known source of infection of the index case) improved after implementation of the public health intervention while the median number of secondary cases decreased, despite the higher daily absolute number of classes investigated in the period after the intervention. However, only the known source of infection of the index case evinced an association with a decrease in secondary transmission in school classes.

Our findings are consistent with those of modeling studies reporting that contact tracing efficacy decreases sharply with increasing delays between symptom onset and tracing and with a lower fraction of symptomatic infections being tested, fewer cases ascertained by contact tracing, and increasing transmission before symptom onset (Kretzschmar et al., 2020; Gardner and Kilpatrick, 2021; Bradshaw et al., 2021; Hellewell et al., 2020). Moreover, our previous modelling study showed that identifying positive cases within 5 days after exposure to their infector could reduce by 30% onward transmission at schools (Molina Grané et al., 2023). Observational studies also demonstrated that various improvements in contact tracing (Malheiro et al., 2020) can reduce the secondary transmission or even mortality in the community (Vecino-Ortiz et al., 2021). A few open-label and field trials conducted with intention to minimize confounding showed that daily testing and twice-a-week testing strategies are effective in limiting the secondary transmission while reducing the loss of in-person school days (Young et al., 2021; Harris-McCoy et al., 2021).

Our results suggest that there is a modest association between the intervention and the number of secondary cases. It has been shown that the effectiveness of contact tracing highly depends on the number of cases being traced, i.e., it decreases when the burden of new cases is too high for the tracing capacity of the health services (Gardner and Kilpatrick, 2021). In fact, BCT is more effective when community transmission is low to moderate (Ontario Agency for Health Protection and Promotion (Public Health Ontario), 2021). Similarly, increased new cases burden and high transmission during the winter months in our study could be factors that might have minimised the true effect of the intervention.

Interestingly, tracing delay was not associated with the decrease in the secondary transmission in schools, despite its notable decrease after intervention implementation. This unexpected finding might be explained by two factors. First, before the intervention, most classes were put in quarantine immediately independently of the presence of secondary transmission in the class, considering all classmates as close contacts, thus, delay in testing was not relevant for secondary transmission in these classes. Furthermore, the unmeasured tracing delay in the family/community better reflects the intervention efficacy and represents the timeliness in linking SARS-CoV-2 positive children to the school investigation. A better link between sporadic cases in households to school exposure after the intervention implementation is also supported by the higher fraction of asymptomatic index cases identified as well as the higher fraction of index cases that were part of a household cluster.

The direct effect of the intervention would lead to an almost 30% reduction in secondary transmission if the source of infection of all index cases was known. Moreover, the known source of infection had a greater impact on the secondary transmission when acting in the interaction with the intervention than independently (14% vs 2% reduction in the number of secondary cases).

The four-way decomposition analysis also showed that interaction alone accounted for a considerable part of the excess risk associated with the intervention. This practically means that knowing the source of infection of the index case in the period before the intervention, i.e., when contacts are not promptly tested, would have had a substantially detrimental effect on the secondary cases (35% increase). This possibly reflects that, before the intervention, often the source of infection for the school index case was identified during the field investigation and not before, thus, in the absence of BCT, knowing the source of infection is not a sign of timeliness at all.

The major limitation of the study is its before-and-after design; i.e., the impossibility to make an inference that observed changes are due to intervention and not due to other factors. In fact, multivariate and mediation analysis may not be enough to control for the fact that the force of infection was changing over the time series. It is often impossible to conduct properly designed experimental studies under a public health emergency. Nevertheless, it was impossible to apply our intervention to a limited number of schools, because it was an intervention targeting household clusters, in a particularly critical moment, i.e., during the peak of the second pandemic wave. The only way to assess the effectiveness of this intervention was to design an observational study trying to minimise the effect of confounding. A possible solution was testing the effect of mediators strictly linked to the intervention process (Accorsi et al., 2021). We adjusted analyses for major sources of confounding, but there are still unmeasured confounders. In fact, we could not classify the preventive measures put in place in each school, the time spent by each index case in the classroom, or the out-school contacts between classmates. Another important limitation is the lack of testing delay in a family/community as a process indicator, that we consider one of the real mechanisms of action of the new tracing strategy (first gray part of the conceptual scheme), but we assume this delay in the community follows the same trend as the delay observed in schools. Lastly, the same intervention may not yield the same results in a different epidemiological context, such as the presence of other variants of the virus (Omicron), or different control measures. However, it can have important public health implications in informing the management of the pandemic and the potential interaction between control measures in the family and in the school.

To our knowledge, this is the only study that attempted to quantify the potential effect of changing a contact tracing strategy in a community on secondary transmission in schools by estimating the excess risk associated with the intervention, through the application of a new mediation analysis method which allowed us to partition the total excess risk into separate effects of the intervention and its process indicators in the presence of their interaction (VanderWeele, 2014; Discacciati et al., 2019). As such it can have important methodological implications as well.

### Conclusion

Changing the contact tracing strategy in the community, from testing contacts at the end of quarantine to testing contacts immediately, reduced the time of contact tracing and increased the ability to identify the source of infection in school outbreaks. The improvement in tracing performance appears to be linked to a decrease in the number of secondary cases in school contacts, although the intervention was implemented in a changing context just after the incidence peak of the autumn wave, and we cannot exclude that the observed differences are due to differences in the force of infection and to other control measures put in place before as the reduction of in presence school attendance.
