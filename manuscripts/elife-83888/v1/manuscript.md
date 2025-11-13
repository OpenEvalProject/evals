# ‘Skeletal Age’ for mapping the impact of fracture on mortality

## Authors

- Thach Tran<sup>1</sup> ([ORCID: 0000-0002-6454-124X](https://orcid.org/0000-0002-6454-124X)) †
- Thao Ho-Le<sup>1</sup>
- Dana Bliuc<sup>2</sup>
- Bo Abrahamsen<sup>4</sup>
- Louise Hansen<sup>7</sup> ([ORCID: 0000-0002-4400-2732](https://orcid.org/0000-0002-4400-2732))
- Peter Vestergaard<sup>8</sup>
- Jacqueline R Center<sup>2</sup> ([ORCID: 0000-0002-5278-4527](https://orcid.org/0000-0002-5278-4527))
- Tuan V Nguyen<sup>1</sup> ([ORCID: 0000-0002-3246-6281](https://orcid.org/0000-0002-3246-6281)) †

### Affiliations

1. School of Biomedical Engineering, University of Technology Sydney Sydney Australia ([ROR:03f0f6041](https://ror.org/03f0f6041))
2. Garvan Institute of Medical Research Sydney Australia ([ROR:01b3dvp57](https://ror.org/01b3dvp57))
3. Faculty of Medicine, UNSW Sydney New South Wales Australia ([ROR:03r8z3t63](https://ror.org/03r8z3t63))
4. Department of Medicine, Holbæk Hospital Holbæk Denmark
5. Department of Clinical Research, Odense Patient Data Explorative Network, University of Southern Denmark Odense Denmark ([ROR:03yrrjy16](https://ror.org/03yrrjy16))
6. Nuffield Department of Orthopaedics, Rheumatology and Musculoskeletal Sciences University of Oxford Oxford United Kingdom ([ROR:052gg0110](https://ror.org/052gg0110))
7. Kontraktenheden, North Denmark Region Denmark Denmark ([ROR:003gkfx86](https://ror.org/003gkfx86))
8. Department of Clinical Medicine, Aalborg University Aalborg Denmark ([ROR:04m5j1k67](https://ror.org/04m5j1k67))
9. Department of Endocrinology, Aalborg University Hospital Aalborg Denmark ([ROR:04m5j1k67](https://ror.org/04m5j1k67))
10. Steno Diabetes Center North Jutland Aalborg Denmark ([ROR:03aqyvf83](https://ror.org/03aqyvf83))
11. School of Medicine Sydney, University of Notre Dame Australia Sydney Australia ([ROR:02stey378](https://ror.org/02stey378))
12. School of Population Health, UNSW Medicine, UNSW Sydney Kensington Australia ([ROR:03r8z3t63](https://ror.org/03r8z3t63))

† Corresponding author

## Abstract

Background:Fragility fracture is associated with an increased risk of mortality, but mortality is not part of doctor-patient communication. Here, we introduce a new concept called ‘Skeletal Age’ as the age of an individual’s skeleton resulting from a fragility fracture to convey the combined risk of fracture and fracture-associated mortality for an individual.Methods:We used the Danish National Hospital Discharge Register which includes the whole-country data of 1,667,339 adults in Denmark born on or before January 1, 1950, who were followed up to December 31, 2016 for incident low-trauma fracture and mortality. Skeletal age is defined as the sum of chronological age and the number of years of life lost (YLL) associated with a fracture. Cox’s proportional hazards model was employed to determine the hazard of mortality associated with a specific fracture for a given risk profile, and the hazard was then transformed into YLL using the Gompertz law of mortality.Results:During the median follow-up period of 16 years, there had been 307,870 fractures and 122,744 post-fracture deaths. A fracture was associated with between 1 and 7 years of life lost, with the loss being greater in men than women. Hip fractures incurred the greatest loss of life years. For instance, a 60-year-old individual with a hip fracture is estimated to have a skeletal age of 66 for men and 65 for women. Skeletal Age was estimated for each age and fracture site stratified by gender.Conclusions:We propose ‘Skeletal Age’ as a new metric to assess the impact of a fragility fracture on an individual’s life expectancy. This approach will enhance doctor-patient risk communication about the risks associated with osteoporosis.Funding:National Health and Medical Research Council in Australia and Amgen Competitive Grant Program 2019.

## Introduction

Fragility fracture is a direct consequence of osteoporosis, just as stroke is a consequence of hypertension. Fracture, especially hip fracture, is associated with an increased risk of mortality. Indeed, patients with a fragility fracture have on average a twofold increase in the risk of mortality (Center et al., 1999). Between 22% (Brauer et al., 2009) and 58% (Rapp et al., 2008) of patients with a hip fracture die within 12 months post fracture. The identification of high-risk individuals for early intervention is a major priority in the control of osteoporotic fractures in the general community. In randomized controlled trials, treating high-risk individuals reduces the risk of fracture (Black et al., 2020), though whether the reduction translates into reduced mortality risk remains contentious (Bolland et al., 2010; Cummings et al., 2019). However, the treatment uptake has been low, with only 40% of hip fracture patients in the United States being given osteoporosis treatment within 1 month after discharge in 2002, which was then halved in 2011 (Solomon et al., 2014). This undertreatment is considered a crisis in the management of osteoporosis globally.

Despite the excess mortality after fracture, mortality is not part of doctor-patient communication about treatment or risk assessment, because there is a lack of an intuitive method of conveying risk. Traditionally, relative risk (e.g. "the risk of mortality is increased by twofold") has been used as a metric of excess risk, but this metric often gives an exaggerated impression (Trevena et al., 2013), and is perceived as larger than the absolute risk (Akl et al., 2011). On the other hand, absolute risk in terms of probability over a period of time is much harder to understand (Zipkin et al., 2014), even for doctors and patients (Gigerenzer et al., 2007). The underappreciation of post-fracture mortality’s gravity has caused patients to be hesitant towards treatment and prevention, contributing to the crisis of osteoporosis management. Thus, there is an urgent need for a more informative metric to internalize the combined risks of fracture and mortality in a way that patients and doctors can comprehend easily.

The concept of ‘Effective Age’ (Spiegelhalter, 2016) is useful here. In engineering, effective age is the age of a structure based on its current conditions; whereas in medicine, the effective age of an individual is the age of a typical healthy person who matches the specific risk profile of this individual (Spiegelhalter, 2016). Depending on whether the risk profile is not healthy (i.e. presence of risk factors) or healthy (i.e. absence of risk factors), the effective age is older or younger, respectively than the chronological age (Spiegelhalter, 2016). The best-known effective age in medicine is ‘Heart Age’ or ‘Vascular Age’ (NHS Health Check, 2022) and ‘Lung Age’ (Morris and Temple, 1985). The use of heart age and lung age has resulted in a better clinical impact than the traditional absolute risk metric (Kulendrarajah et al., 2020).

We consider that patients with osteoporosis and the general public are not sufficiently informed about the risk of post-fracture mortality, and this might have contributed to the current crisis of under management of osteoporosis (Roux and Briot, 2020; Beaudoin et al., 2019). In an effort to improve the management of osteoporosis, we advance the idea of the ‘Skeletal Age’ which is conceptually defined as the age of one’s skeleton as a consequence of fragility fracture. This new metric is not only one that quantifies the impact of fracture on mortality but also one that captures the risk of fracture and the risk of post-fracture mortality.

The aim of this study was to analyze the relationship between fracture and mortality, and then translate this relationship into the ‘Skeletal Age’ for each fracture site by leveraging data from the Danish National Hospital Discharge Registry (NHDR). The NHDR data are ideal for this analysis because, apart from comorbidities at the individual patient level, it has documented the incidence of fractures and post-fracture mortality for the entire Danish population.

## Methods

**Key resources table**


<table>
  <thead>
    <tr>
      <th>Reagent type (species) or resource</th>
      <th>Designation</th>
      <th>Source or reference</th>
      <th>Identifiers</th>
      <th>Additional information</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Software, algorithm</td>
      <td>R Project for Statistical Computing</td>
      <td>R Project for Statistical Computing</td>
      <td>RRID:SCR_001905</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Stata Statistical Software</td>
      <td>A Software resource for statistical analysis and presentation of graphics</td>
      <td>RRID:SCR_012763</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Study design

The Danish National Hospital Discharge Registry can be viewed as a retrospective population-based cohort. This analysis included all adults aged 50 years old and older as of January 1, 2001 in Denmark whose health status had been followed up until December 31, 2016 for mortality. Individuals who had sustained a fracture at 45+ years old between 1996 and 2000 were excluded to avoid potential bias that the incident fracture analyzed in this study was a second fracture (Figure 1). This is not a clinical trial. This analysis (Statistics Denmark project number 706667) was approved by the National Board of Health, the Danish Data Protection Agency, and Statistics Denmark, and is subject to independent control and monitoring by The Danish Health Data Authority. Written informed consent is waived for routinely collected, pseudonymized registry data. This study followed the Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) reporting guideline.

![Figure 1.](https://cdn.elifesciences.org/articles/83888/elife-83888-fig1-v1.jpg)

### Ascertainment of fracture and mortality

The initial incident fracture was defined as the first low-trauma fracture reported between January 1, 2001 and December 31, 2014. When more than one fracture occurred during a single event, only the fracture at the most proximal site was considered. We used the International Statistical Classification of Disease and Related Health Problems, tenth version (ICD-10) codes to identify individuals with specific fracture sites including hip, femur, pelvis, vertebrae, humerus, rib, clavicle (collectively known as proximal fractures), forearm, lower leg, knee, ankle, foot and hand (collectively known as distal fractures) from the Danish NHDR (Supplementary file 1). All fractures included in the analysis were radiologically ascertained. Face, skull, finger, or toe fractures and high-trauma fractures due to traffic accidents were excluded.

The study participants were followed up to December 31, 2016 for mortality, allowing at least 2 years of follow-up post fracture. Death was ascertained from the Danish Register on Causes of Death.

### Covariates assessment

The predefined covariates included age and comorbidities. We used the ICD-10 from the NHDR that includes any diagnosis documented between 1996 and 2000 to operationally define comorbidities at the study entry (i.e. January 1, 2001), and those within 5 years prior to the initial fracture to define comorbidities at fracture time. The severity of comorbidities was summarised using the Charlson comorbidity index (Quan et al., 2011).

### Statistical analysis

Skeletal age is operationally defined as the sum of the chronological age and the change in life expectancy associated with fracture. The changes in life expectancy resulting from a specific fracture were computed incorporating (i) the association between individual fracture sites and mortality from a Cox’s proportional hazards regression and (ii) the baseline hazards described by Gompertz distribution and the population life expectancy from the national lifetable data (Kulinskaya et al., 2020).

For the first aim, a Cox’s proportional hazards regression was used to quantify the association between an initial specific fracture and mortality, in which both fracture and confounding variables were analyzed in a time-dependent manner to minimize the risk of immortal time bias (Suissa, 2008). The analyses did not account for the possibility of subsequent or recurrent fractures as this falls outside the scope of the study. The models adjusted for confounding effects of age and severity of comorbidities (Quan et al., 2011). Age and comorbidities at baseline and those at the time of fracture were also used. For individuals without fracture, the follow-up time was calculated from the study entry to the study end (December 31, 2016) or date of death, whichever came first; while their covariates at baseline were adjusted in the analysis model (Figure 2). By contrast, the follow-up time for those with an incident fracture was split into the pre-fracture (i.e. unexposed) and post-fracture (i.e. exposed) period for which the clustering effect was accounted for in the Cox’s proportional hazards regression. We conducted a time-dependent analysis to quantify the relationship between an incident exposure (i.e. an incident fracture) and the primary outcome of interest (i.e. post-fracture mortality) accounting for the risk of immortal time bias (Suissa, 2008). The pre-fracture period was the time interval between the study entry and date of fracture, and used the covariates at study entry; whereas the post-fracture period was between the date of fracture and date of death or study end, whichever came first, and included the covariates at the time of fracture. The proportional hazards assumption was graphically checked using the Schoenfeld’s residuals.

![Figure 2.](https://cdn.elifesciences.org/articles/83888/elife-83888-fig2-v1.jpg)

For the second aim, we determined the skeletal age of an individual based on the individual’s specific risk profile. First, we calculated a prognostic index for an individual as a single-number summary of the combined effects of his/her specific fracture site and comorbidity severity (Henderson and Keiding, 2005). The prognostic index is a linear combination of the risk factors with weights derived from the regression coefficients. The individualized fracture-mortality association for an individual with a specific risk profile was then the difference between his/her prognostic index and the mean prognostic index of ‘typical’ people in the study population (Henderson and Keiding, 2005). In the second step, we used the Gompertz law of mortality and the Danish national lifetable data to transform the fracture-mortality association into life expectancy as a result of a fracture (Kulinskaya et al., 2020). The Gompertz law of mortality indicates the annual risk of dying at the age t can be expressed as $ht=Be^{kt}$ in which B~0.0000189 in women and 0.0000347 in men (Gompertz, 1825). Under the Gompertz law of mortality, the annual risk of dying associated with aging 1 year is remarkably consistent between ages 50 and 95 across ethnicities and over time (Brenner et al., 1993; Vaupel, 2010). Assuming the Gompertz baseline hazard, the log-hazards of mortality to specific fracture site i at the fracture time t is $a+bt$, where a and b are the estimated regression coefficients. The life expectancy for a specific fracture site at the fracture age z under the Gompertz distribution G(a,b) is obtained as $e_{Ga,b}z=\frac{b^{-1}exp⁡(b^{-1}e^{a})E_{1}(b^{-1}e^{a+bz})}{exp⁡(-e^{a}b^{-1}(e^{bz}-1))}$ , where $E_{1}(b^{-1}e^{a+bz})$ denotes the exponential integral. The loss of life years associated with specific fracture site was then calculated as the difference between the estimate life expectancy associated with fracture $e_{Ga,b}z$ and the population life expectancy (Kulinskaya et al., 2020). The skeletal age for each individual site of fracture was the sum of the individual’s chronological age at the time of fracture and the loss of life years as a result of the fracture. The 95% CI of the skeletal age was computed using the confidence limits of the adjusted hazards ratios to account for uncertainty of the magnitude of association between individual site of fracture and mortality. The analyses were performed using Stata (Stata Statistical Software: Release 16. College Station, TX: StataCorp LLC) and the R statistical environment on a Windows platform (R Development Core Team, 2020).

## Results

### Incidence of fractures

The present analysis was based on data from 793,815 men and 873,524 women aged 63.9 (standard deviation [SD] 10.3) and 65.5 (11.3) years old as of January 1, 2001, respectively (Figure 1). During a median of 14 years of follow-up (interquartile range [IQR]: 6.5, 14.0 years), 95,372 men and 212,498 women had sustained a fracture. The incidence of fractures was 10.9 fractures/1000 person-years (95% confidence interval [CI]: 10.8, 11.0) in men and 23.2 fractures/1000 person-years (23.1, 23.3) in women. Collectively, forearm, hip, and humerus fractures accounted for 55% of all fractures in men and 70% in women.

As expected, men and women with a fracture were on average older than those without a fracture. Individuals with a fracture had more comorbidities than those who did not sustain a fracture (Table 1). For instance, the prevalence of myocardial infarction among patients with a fracture (9.3% in men and 4.7% in women) was higher than that among individuals without a fracture (4% in men and 1.5% in women). Similar trend was also observed for stroke, diabetes, and cancer.

**Table 1.**
 Characteristics of the study population at baseline stratified by gender, fracture, and mortality status.


<table>
  <thead>
    <tr>
      <th rowspan="2">Characteristic</th>
      <th colspan="2">Non-fracture group</th>
      <th colspan="2">Fracture group</th>
    </tr>
    <tr>
      <th>Alive</th>
      <th>Dead</th>
      <th>Alive</th>
      <th>Dead</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Men</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Number of individuals</td>
      <td>466,936</td>
      <td>231,507</td>
      <td>54,355</td>
      <td>41,017</td>
    </tr>
    <tr>
      <td>Age at baseline1</td>
      <td>59.8 (7.7)</td>
      <td>71.1 (10.4)</td>
      <td>61.3 (8.9)</td>
      <td>72.4 (10.4)</td>
    </tr>
    <tr>
      <td>Age at fracture1</td>
      <td></td>
      <td></td>
      <td>68.2 (9.9)</td>
      <td>77.8 (10.5)</td>
    </tr>
    <tr>
      <td>Comorbidities*</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Charlson comorbidity index2</td>
      <td>0 (0, 0)</td>
      <td>0 (0, 1)</td>
      <td>0 (0, 1)</td>
      <td>1 (0, 2)</td>
    </tr>
    <tr>
      <td>0</td>
      <td>404,415 (86.7%)</td>
      <td>140,293 (60.6%)</td>
      <td>32,287 (59.4%)</td>
      <td>12,592 (30.7%)</td>
    </tr>
    <tr>
      <td>1–2</td>
      <td>56,701 (12.1%)</td>
      <td>70,841 (30.6%)</td>
      <td>17,557 (32.3%)</td>
      <td>19,073 (46.5%)</td>
    </tr>
    <tr>
      <td>3–4</td>
      <td>3,328 (0.7%)</td>
      <td>9,260 (4.0%)</td>
      <td>2,881 (5.3%)</td>
      <td>5,209 (12.7%)</td>
    </tr>
    <tr>
      <td>5+</td>
      <td>2,492 (0.5%)</td>
      <td>1,112 (4.8%)</td>
      <td>1,631 (3.0%)</td>
      <td>4,143 (10.1%)</td>
    </tr>
    <tr>
      <td>Specific comorbidities3</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Myocardial infarction</td>
      <td>18,734 (4.0%)</td>
      <td>22,225 (9.6%)</td>
      <td>5,055 (9.3%)</td>
      <td>6,071 (14.8%)</td>
    </tr>
    <tr>
      <td>Congestive heart failure</td>
      <td>12,814 (2.7%)</td>
      <td>26,623 (11.5%)</td>
      <td>5,109 (9.4%)</td>
      <td>8,655 (21.1%)</td>
    </tr>
    <tr>
      <td>Stroke</td>
      <td>21,792 (4.7%)</td>
      <td>31,253 (13.5%)</td>
      <td>9,458 (17.4%)</td>
      <td>11,567 (28.2%)</td>
    </tr>
    <tr>
      <td>Peripheral vascular disease</td>
      <td>10,912 (2.3%)</td>
      <td>18,058 (7.8%)</td>
      <td>4,240 (7.8%)</td>
      <td>5,660 (13.8%)</td>
    </tr>
    <tr>
      <td>Arrhythmias</td>
      <td>10,835 (2.3%)</td>
      <td>18,289 (7.9%)</td>
      <td>4,892 (9.0%)</td>
      <td>5,747 (18.4%)</td>
    </tr>
    <tr>
      <td>Hypertension</td>
      <td>14,340 (3.1%)</td>
      <td>15,279 (6.6%)</td>
      <td>7,718 (14.2%)</td>
      <td>7,875 (19.2%)</td>
    </tr>
    <tr>
      <td>Diabetes mellitus with no chronic complications</td>
      <td>19,805 (4.2%)</td>
      <td>21,067 (9.1%)</td>
      <td>6,305 (11.6%)</td>
      <td>6,317 (15.4%)</td>
    </tr>
    <tr>
      <td>Diabetes mellitus with chronic complications</td>
      <td>6,120 (1.3%)</td>
      <td>8,103 (3.5%)</td>
      <td>2,446 (4.5%)</td>
      <td>2,748 (6.7%)</td>
    </tr>
    <tr>
      <td>Renal disease</td>
      <td>4,290 (0.9%)</td>
      <td>8,797 (3.8%)</td>
      <td>2,120 (3.9%)</td>
      <td>3,609 (8.8%)</td>
    </tr>
    <tr>
      <td>Cancer</td>
      <td>26,126 (5.6%)</td>
      <td>43,523 (18.8%)</td>
      <td>8,914 (16.4%)</td>
      <td>11,813 (28.8%)</td>
    </tr>
    <tr>
      <td>Metastatic tumors</td>
      <td>1,894 (0.4%)</td>
      <td>9,492 (4.1%)</td>
      <td>1,033 (1.9%)</td>
      <td>3,035 (7.4%)</td>
    </tr>
    <tr>
      <td>Dementia</td>
      <td>2,869 (0.6%)</td>
      <td>7,640 (3.3%)</td>
      <td>2,663 (4.9%)</td>
      <td>6,071 (14.8%)</td>
    </tr>
    <tr>
      <td>Chronic lung disease</td>
      <td>16,600 (3.6%)</td>
      <td>25,697 (11.1%)</td>
      <td>6,740 (12.4%)</td>
      <td>8,696 (21.2%)</td>
    </tr>
    <tr>
      <td>Rheumatologic</td>
      <td>4,881 (1.1%)</td>
      <td>4,630 (2.0%)</td>
      <td>1,685 (3.1%)</td>
      <td>1,600 (3.9%)</td>
    </tr>
    <tr>
      <td>Mild liver disease</td>
      <td>2,647 (0.6%)</td>
      <td>3,704 (1.6%)</td>
      <td>1,468 (2.7%)</td>
      <td>1,805 (4.4%)</td>
    </tr>
    <tr>
      <td>Moderate/severe liver disease</td>
      <td>589 (0.1%)</td>
      <td>1,389 (0.6%)</td>
      <td>435 (0.8%)</td>
      <td>779 (1.9%)</td>
    </tr>
    <tr>
      <td>Hemiplegia</td>
      <td>661 (0.1%)</td>
      <td>927 (0.4%)</td>
      <td>461 (0.9%)</td>
      <td>480 (0.9%)</td>
    </tr>
    <tr>
      <td>HIV/AIDS</td>
      <td>108 (0.02%)</td>
      <td>81 (0.03%)</td>
      <td>37 (0.07%)</td>
      <td>23 (0.06%)</td>
    </tr>
    <tr>
      <td>Women</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Number of individuals</td>
      <td>465,559</td>
      <td>195,467</td>
      <td>130,771</td>
      <td>81,727</td>
    </tr>
    <tr>
      <td>Age at baseline1</td>
      <td>60.5 (8.3)</td>
      <td>74.0 (11.1)</td>
      <td>63.9 (9.7)</td>
      <td>76.3 (9.9)</td>
    </tr>
    <tr>
      <td>Age at fracture1</td>
      <td></td>
      <td></td>
      <td>70.9 (10.2)</td>
      <td>81.3 (9.6)</td>
    </tr>
    <tr>
      <td>Comorbidities*</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Charlson comorbidity index2</td>
      <td>0 (0, 0)</td>
      <td>0 (0, 1)</td>
      <td>0 (0, 1)</td>
      <td>1 (0, 2)</td>
    </tr>
    <tr>
      <td>0</td>
      <td>400,005 (85.9%)</td>
      <td>121,776 (62.3%)</td>
      <td>81,574 (62.4%)</td>
      <td>32,093 (39.3%)</td>
    </tr>
    <tr>
      <td>1–2</td>
      <td>59,923 (12.9%)</td>
      <td>57,663 (29.5%)</td>
      <td>41,114 (31.4%)</td>
      <td>35,866 (44.0%)</td>
    </tr>
    <tr>
      <td>3–4</td>
      <td>2,975 (0.6%)</td>
      <td>6,255 (3.2%)</td>
      <td>5,196 (4.0%)</td>
      <td>7,960 (9.8%)</td>
    </tr>
    <tr>
      <td>5+</td>
      <td>2,656 (0.6%)</td>
      <td>9,773 (5.0%)</td>
      <td>2,887 (2.2%)</td>
      <td>5,695 (7.0%)</td>
    </tr>
    <tr>
      <td>Specific comorbidities3</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Myocardial infarction</td>
      <td>7,164 (1.5%)</td>
      <td>10,946 (5.6%)</td>
      <td>6,109 (4.7%)</td>
      <td>7,562 (9.3%)</td>
    </tr>
    <tr>
      <td>Congestive heart failure</td>
      <td>7,307 (1.6%)</td>
      <td>18,374 (9.4%)</td>
      <td>8,056 (6.2%)</td>
      <td>13,615 (16.7%)</td>
    </tr>
    <tr>
      <td>Stroke</td>
      <td>16,329 (3.5%)</td>
      <td>22,870 (11.7%)</td>
      <td>17,143 (13.1%)</td>
      <td>19,247 (23.6%)</td>
    </tr>
    <tr>
      <td>Peripheral vascular disease</td>
      <td>6,517 (1.4%)</td>
      <td>10,555 (5.4%)</td>
      <td>6,196 (4.7%)</td>
      <td>7,309 (9.0%)</td>
    </tr>
    <tr>
      <td>Arrhythmias</td>
      <td>7,671 (1.7%)</td>
      <td>13,096 (6.7%)</td>
      <td>7,947 (6.1%)</td>
      <td>11,440 (14.0%)</td>
    </tr>
    <tr>
      <td>Hypertension</td>
      <td>12,910 (2.8%)</td>
      <td>12,510 (6.4%)</td>
      <td>17,970 (13.7%)</td>
      <td>15,727 (19.3%)</td>
    </tr>
    <tr>
      <td>Diabetes mellitus with no chronic complications</td>
      <td>14,151 (3.0%)</td>
      <td>14,074 (7.2%)</td>
      <td>9,960 (7.6%)</td>
      <td>9,214 (11.3%)</td>
    </tr>
    <tr>
      <td>Diabetes mellitus with chronic complications</td>
      <td>3,367 (0.7%)</td>
      <td>4,496 (2.3%)</td>
      <td>2,969 (2.3%)</td>
      <td>3,126 (3.8%)</td>
    </tr>
    <tr>
      <td>Renal disease</td>
      <td>2,386 (0.5%)</td>
      <td>4,300 (2.2%)</td>
      <td>2,697 (2.1%)</td>
      <td>3,561 (4.4%)</td>
    </tr>
    <tr>
      <td>Cancer</td>
      <td>30,913 (6.6%)</td>
      <td>34,989 (17.9%)</td>
      <td>20,246 (15.5%)</td>
      <td>18,785 (23.0%)</td>
    </tr>
    <tr>
      <td>Metastatic tumors</td>
      <td>2,302 (0.5%)</td>
      <td>8,796 (4.5%)</td>
      <td>2,221 (1.7%)</td>
      <td>4,632 (5.7%)</td>
    </tr>
    <tr>
      <td>Dementia</td>
      <td>3,035 (0.7%)</td>
      <td>7,428 (3.8%)</td>
      <td>7,169 (5.5%)</td>
      <td>13,136 (16.1%)</td>
    </tr>
    <tr>
      <td>Chronic lung disease</td>
      <td>18,759 (4.0%)</td>
      <td>20,915 (10.7%)</td>
      <td>15,065 (11.5%)</td>
      <td>14,018 (17.2%)</td>
    </tr>
    <tr>
      <td>Rheumatologic</td>
      <td>10,392 (2.2%)</td>
      <td>7,037 (3.6%)</td>
      <td>7,482 (5.7%)</td>
      <td>5,256 (6.4%)</td>
    </tr>
    <tr>
      <td>Mild liver disease</td>
      <td>2,599 (0.6%)</td>
      <td>2,346 (1.2%)</td>
      <td>2,165 (1.7%)</td>
      <td>1,802 (2.2%)</td>
    </tr>
    <tr>
      <td>Moderate/severe liver disease</td>
      <td>296 (0.1%)</td>
      <td>782 (0.4%)</td>
      <td>422 (0.3%)</td>
      <td>643 (0.8%)</td>
    </tr>
    <tr>
      <td>Hemiplegia</td>
      <td>524 (0.1%)</td>
      <td>573 (0.3%)</td>
      <td>577 (0.4%)</td>
      <td>475 (0.6%)</td>
    </tr>
    <tr>
      <td>HIV/AIDS</td>
      <td>14 (0.0%)</td>
      <td>9 (0.0%)</td>
      <td>12 (0.01%)</td>
      <td>4 (0.0%)</td>
    </tr>
  </tbody>
</table>

_Notes: 1: mean (SD); 2: median (IQR); 3: number (%). *: at baseline for individuals without fracture or at fracture time for fracture patients. Comorbidities included not only chronic diseases that require hospitalization, but also those documented as either secondary diagnoses or at outpatient or emergency visits._

### Incidence of mortality

During a median follow-up of 6.5 years (6.0 years (IQR: 2.5, 10.0) in men, 6.7 years (3.3, 10.8) in women), 272,524 men and 277,194 women had died, yielding unadjusted mortality incidence rates of 6.55 deaths/100 person-years (95% CI: 6.48, 6.61) in men and 5.42 deaths/100 person-years (5.39, 5.46) in women. More importantly, the unadjusted rate of mortality among patients with a fracture (6.54/100 person-years in men and 5.42/100 person-years in women) was greater than among those without a fracture (2.56/100 person-years in men and 2.24/100 person-years in women). Analysis by fracture site revealed that men and women with a fracture at the hip, pelvis, or vertebra had a much greater risk of mortality than other fractures (Table 2).

**Table 2.**
 Incidence of mortality following specific fracture sites stratified by gender.


<table>
  <thead>
    <tr>
      <th>Fracture</th>
      <th>Number</th>
      <th>Age at fracture (years)</th>
      <th>Number of deaths</th>
      <th>Follow-up time (person-years)</th>
      <th>Rate* of mortality (95% CI)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Men</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>No fracture</td>
      <td>698,443</td>
      <td>63.6** (10.2)</td>
      <td>231,507</td>
      <td>9,049,194</td>
      <td>2.6% (2.5, 2.6)</td>
    </tr>
    <tr>
      <td>Any fracture</td>
      <td>95,372</td>
      <td>72.3 (11.2)</td>
      <td>41,017</td>
      <td>626,733</td>
      <td>6.5% (6.5, 6.6)</td>
    </tr>
    <tr>
      <td>Hip fracture</td>
      <td>25,706</td>
      <td>79.5 (9.7)</td>
      <td>16,890</td>
      <td>107,789</td>
      <td>15.7% (15.4, 15.9)</td>
    </tr>
    <tr>
      <td>Femur</td>
      <td>1,910</td>
      <td>74.5 (10.8)</td>
      <td>997</td>
      <td>10,468</td>
      <td>9.5% (8.9, 10.1)</td>
    </tr>
    <tr>
      <td>Pelvis</td>
      <td>1,305</td>
      <td>77.0 (10.9)</td>
      <td>751</td>
      <td>6,465</td>
      <td>11.6% (10.8, 12.5)</td>
    </tr>
    <tr>
      <td>Vertebrae</td>
      <td>6,924</td>
      <td>72.7 (10.5)</td>
      <td>3,125</td>
      <td>41,746</td>
      <td>7.5% (7.2, 7.7)</td>
    </tr>
    <tr>
      <td>Humerus</td>
      <td>10,126</td>
      <td>72.6 (10.7)</td>
      <td>4,827</td>
      <td>62,350</td>
      <td>7.7% (7.5, 8.0)</td>
    </tr>
    <tr>
      <td>Rib</td>
      <td>6,867</td>
      <td>69.7 (10.4)</td>
      <td>2,350</td>
      <td>50,186</td>
      <td>4.7% (4.5, 4.9)</td>
    </tr>
    <tr>
      <td>Clavicle</td>
      <td>5,201</td>
      <td>68.2 (10.5)</td>
      <td>1,636</td>
      <td>39,731</td>
      <td>4.1% (3.9, 4.3)</td>
    </tr>
    <tr>
      <td>Lower leg</td>
      <td>6,296</td>
      <td>67.0 (9.5)</td>
      <td>1,796</td>
      <td>52,915</td>
      <td>3.4% (3.2, 3.6)</td>
    </tr>
    <tr>
      <td>Forearm</td>
      <td>15,268</td>
      <td>69.4 (10.2)</td>
      <td>4,675</td>
      <td>120,719</td>
      <td>3.9% (3.8, 4.0)</td>
    </tr>
    <tr>
      <td>Knee</td>
      <td>1,382</td>
      <td>70.2 (10.1)</td>
      <td>447</td>
      <td>10,886</td>
      <td>4.1% (3.7, 4.5)</td>
    </tr>
    <tr>
      <td>Ankle</td>
      <td>1,084</td>
      <td>67.6 (9.8)</td>
      <td>275</td>
      <td>9,081</td>
      <td>3.0% (2.7, 3.4)</td>
    </tr>
    <tr>
      <td>Hand</td>
      <td>8,309</td>
      <td>67.7 (10.1)</td>
      <td>2,178</td>
      <td>70,263</td>
      <td>3.1% (3.0, 3.2)</td>
    </tr>
    <tr>
      <td>Foot</td>
      <td>4,994</td>
      <td>65.3 (9.7)</td>
      <td>1,070</td>
      <td>44,136</td>
      <td>2.4% (2.3, 2.6)</td>
    </tr>
    <tr>
      <td>Women</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>No fracture</td>
      <td>661,026</td>
      <td>64.5** (11.1)</td>
      <td>195,467</td>
      <td>8,723,863</td>
      <td>2.2% (2.2, 2.3)</td>
    </tr>
    <tr>
      <td>Any fracture</td>
      <td>212,498</td>
      <td>74.9 (11.2)</td>
      <td>81,727</td>
      <td>1,506,940</td>
      <td>5.4% (5.4, 5.5)</td>
    </tr>
    <tr>
      <td>Hip fracture</td>
      <td>51,669</td>
      <td>82.1 (9.2)</td>
      <td>31,816</td>
      <td>259,087</td>
      <td>12.3% (12.1, 12.4)</td>
    </tr>
    <tr>
      <td>Femur</td>
      <td>3,529</td>
      <td>78.9 (10.9)</td>
      <td>1,921</td>
      <td>19,322</td>
      <td>9.9% (9.5, 10.4)</td>
    </tr>
    <tr>
      <td>Pelvis</td>
      <td>4,920</td>
      <td>81.2 (10.0)</td>
      <td>2,893</td>
      <td>26,761</td>
      <td>10.8% (10.4, 11.2)</td>
    </tr>
    <tr>
      <td>Vertebrae</td>
      <td>9,732</td>
      <td>76.6 (10.6)</td>
      <td>4,658</td>
      <td>60,295</td>
      <td>7.7% (7.5, 7.9)</td>
    </tr>
    <tr>
      <td>Humerus</td>
      <td>28,298</td>
      <td>74.4 (10.5)</td>
      <td>10,330</td>
      <td>202,662</td>
      <td>5.1% (5.0, 5.2)</td>
    </tr>
    <tr>
      <td>Rib</td>
      <td>3,153</td>
      <td>74.1 (11.9)</td>
      <td>1,218</td>
      <td>22,285</td>
      <td>5.5% (5.2, 5.8)</td>
    </tr>
    <tr>
      <td>Clavicle</td>
      <td>4,480</td>
      <td>72.7 (11.5)</td>
      <td>1,577</td>
      <td>31,755</td>
      <td>5.0% (4.7, 5.2)</td>
    </tr>
    <tr>
      <td>Lower leg</td>
      <td>11,460</td>
      <td>70.1 (10.8)</td>
      <td>3,130</td>
      <td>94,308</td>
      <td>3.3% (3.2, 3.4)</td>
    </tr>
    <tr>
      <td>Forearm</td>
      <td>68,333</td>
      <td>72.0 (10.3)</td>
      <td>18,470</td>
      <td>559,406</td>
      <td>3.3% (3.2, 3.3)</td>
    </tr>
    <tr>
      <td>Knee</td>
      <td>2,604</td>
      <td>71.3 (9.7)</td>
      <td>629</td>
      <td>21,085</td>
      <td>3.0% (2.8, 3.2)</td>
    </tr>
    <tr>
      <td>Ankle</td>
      <td>1,936</td>
      <td>70.0 (10.6)</td>
      <td>499</td>
      <td>15,726</td>
      <td>3.2% (2.9, 3.5)</td>
    </tr>
    <tr>
      <td>Hand</td>
      <td>12,489</td>
      <td>69.6 (10.2)</td>
      <td>2681</td>
      <td>108,112</td>
      <td>2.5% (2.4, 2.6)</td>
    </tr>
    <tr>
      <td>Foot</td>
      <td>9,916</td>
      <td>67.8 (9.6)</td>
      <td>1904</td>
      <td>86,136</td>
      <td>2.2% (2.1, 2.3)</td>
    </tr>
  </tbody>
</table>

_Notes: *: rates were calculated as number of deaths/100 person-years; **: age at baseline (years)._

However, the above observation could be confounded by age and comorbidities, because individuals with a fracture were on average older and had more comorbidities than those without a fracture. Therefore, we employed multivariable-adjusted Cox’s proportional hazards model to estimate the strength of the association between fracture and mortality, adjusting for age and severity of comorbidities (Figure 3). Individuals with any fragility fracture were associated with a 30–45% increased hazard of death (adjusted hazard ratio = 1.46 (95% CI: 1.45, 1.48) in men; 1.28 (1.27, 1.30) in women). For the same age and comorbidity profile, men and women with a hip or femur fracture had an almost twofold greater risk of death than those without a fracture.

![Figure 3.](https://cdn.elifesciences.org/articles/83888/elife-83888-fig3-v1.jpg)

**Figure 3.:** Legend * severity of comorbidities is assessed using the Charlson Comorbidity Index. Hazard ratio and the corresponding 95% confidence interval were estimated from a multivariable-adjusted Cox's proportional hazards regression.

The increased risk of mortality was also observed among those with a proximal fracture, such as the pelvis, vertebrae, humerus, rib, clavicle, and lower leg fracture after controlling for age and comorbidities. However, there was no significantly increased risk of death following a forearm, knee, ankle, hand, or foot fracture (Figure 3).

### Skeletal age

Based on the association between fracture and mortality and using the Gompertz law, we estimated the skeletal age for each fracture site and each chronological age (from the age of 50) in men and women (Figure 4; Supplementary file 2). Patients with a fracture - any fracture at all - have lost years of life, and hence their skeletal age was greater than their chronological age. For a given age, men with a fracture on average had greater skeletal age than women by approximately 1 year. In either sex, the loss of years of life was more pronounced in younger age groups and gradually converged in the older age groups.

![Figure 4.](https://cdn.elifesciences.org/articles/83888/elife-83888-fig4-v1.jpg)

As expected, patients with a hip fracture had the highest skeletal age than those with other fractures. For example, a 70-year-old man who had sustained a hip fracture would have a skeletal age of 75 years (i.e. a loss of 5 years of life); however, if a 50-year-old man with a hip fracture would have a skeletal age of 56.8 years which is equivalent to almost 7 years of life lost. Other fractures such as the femur, pelvis, vertebrae, and humerus also signified a significant loss of years of life (around 5 years); thus, 50-year-old patients with one of these fractures are estimated to have a skeletal age of around 55 years.

However, fractures are the rib, clavicle, and lower leg were associated with lower years of life lost, and the skeletal age of patients with one of these fractures was generally lower than patients with a more serious fracture (e.g. hip fracture). For instance, a 60-year-old patient with a lower leg fracture would be expected to have a skeletal age of 62.4 years for men or 61.9 years for women (Supplementary file 3).

## Discussion

It has been well established that fracture, especially hip fracture, is associated with an increased risk of mortality, and this excess risk is commonly expressed in terms of the relative risk metric. Here, we proposed a new effective age metric called ‘Skeletal Age’ to quantify the impact of fracture on mortality. Using data from a nationwide cohort of 1.7 million adults aged 50+ years old in Denmark, we showed that almost all types of fracture were associated with a loss of years of life, indicating that the skeletal age of individuals suffering from a fracture is greater than their chronological age. This finding has important implications that we discuss below.

Our finding confirmed the previous studies (Tran et al., 2018; Bliuc et al., 2009; Browner et al., 1996; Melton et al., 2013; Haentjens et al., 2010; Tran et al., 2017) that patients with a fragility fracture were associated with a significantly greater risk of mortality than their similarly aged and gender counterparts without fracture who had the same comorbidity profile. Our finding is also consistent with an earlier Danish study demonstrating reduced life expectancy in patients, with or without fractures, at the time of beginning osteoporosis treatment (Abrahamsen et al., 2015). However, the magnitude of the association between individual sites of fracture observed in our study is slightly lower than that documented in several previous cohort studies (Bliuc et al., 2009; Browner et al., 1996; Melton et al., 2013; Haentjens et al., 2010; Tran et al., 2017), with hip fractures being associated with a 1.7-to-6-fold increased risk of death (Haentjens et al., 2010). This discrepancy could be due to the difference in study populations. While cohort studies usually recruit healthy participants, our national registry-based study was able to document all individuals in Denmark. As a result, our control group (i.e. those without a fracture) included individuals in poor health conditions with multiple comorbidities who are usually unable to be recruited in a cohort study. Whether the association between fracture and mortality is causal or not is a matter of contention. It is commonly assumed that the association is confounded by comorbidities, but multiple studies have found that comorbidities contributed little to the excess risk of mortality among fractured patients (Vestergaard et al., 2007; Chen et al., 2018). In the present analysis, we have also adjusted for comorbidities, and the significant fracture – mortality association remained unchanged, suggesting that the association is unlikely due to comorbidities.

Regardless of the nature of the association, mortality is not a component of doctor-patient communication. Existing fracture risk assessment models such as Garvan (Nguyen et al., 2007) and FRAX (Kanis et al., 2007) provide the estimated probability (i.e. absolute risk) of fracture over a 10 year period without any information on mortality. However, doctors and patients have difficulty in understanding and interpreting probability (Gigerenzer et al., 2007). Only a fifth of a sample of highly educated American adults could understand one in 1000 is equivalent to 0.1% (Lipkus et al., 2001). Conveying a low, though clinically significant absolute risk (e.g. ‘Your risk of hip fracture over the next 10 years is 5%’) might provide a false peace of mind and underestimated risk perception, leading to increasing possibilities of refusing the recommended treatment (Trevena et al., 2013). Thus, poor communication about fracture risk and mortality consequences might have contributed to the global crisis of undertreatment of osteoporosis.

Based on the concept of effective age, we proposed the idea of ‘Skeletal Age’ as a new metric for communicating the risk of mortality following a fracture. Unlike the current fracture risk assessment tools (Beaudoin et al., 2019) which estimate the probability of fracture over time using probability-based metrics, such as relative risk and absolute risk, skeletal age quantifies the consequence of a fracture using a natural frequency metric. A natural frequency metric has been consistently shown to be easier and more friendly to doctors and patients than the probability-based metrics (Akl et al., 2011; Gigerenzer et al., 2007; Ahmed et al., 2012). It is not straightforward to appreciate the importance of the twofold increased risk of death (i.e. relative risk = 2.0) without knowing the background risk (i.e. twofolds of 1% would remarkably differ from twofolds of 10%). By contrast, for the same twofold mortality risk of hip fracture, telling a 60 year man with a hip fracture that his skeletal age would be 66 years old, equivalent to a 6 year loss of life, is more intuitive. The skeletal age of 66 years old can also be interpreted as the individual being in the same risk category as a 66-year-old with ‘favorable risk factors’ or at least the ones that are potentially modifiable. Hence, an older skeletal age also means a greater risk of fracture. In addition, the skeletal age can be also used to convey the possible benefit of treatment, providing an alternative metric to the conventional metrics such as relative risk or relative risk reduction. For instance, a patient might find the statement ‘Zoledronic acid treatment helps a patient with a hip fracture gain 3 years of life’ much easier to understand and probably more persuasive than ‘Zoledronic acid treatment reduced the risk of death by 28%’ (Lyles et al., 2007).

Skeletal age is an addition to the already available metrics such as ‘Heart Age,’ ‘Lung Age,’ and more recently ‘Covid Age’ which have been demonstrated to be superior to the conventional risk metrics (Grover et al., 2007; Lowensteyn et al., 1998; Lopez-Gonzalez et al., 2015; Bonner et al., 2015; Svendsen et al., 2020) in terms of positive behavioral changes. For instance, compared with usual care, individuals who were given heart age had a greater smoking cessation rate (Lopez-Gonzalez et al., 2015; Bonner et al., 2015), substantial improvement in weight, body mass index, and physical activity (Lopez-Gonzalez et al., 2015), and a greater proportion of high-risk patients returning for a follow-up appointment (Lowensteyn et al., 1998). The use of heart age also led to significantly greater improvement at 12 months in metabolic parameters (Lopez-Gonzalez et al., 2015) or lipid profiles (Grover et al., 2007). A recent cluster randomized controlled trial in Norway also found that heart age was a good way to communicate cardiovascular risk and to motivate individuals to reduce cardiovascular risk factors (Svendsen et al., 2020). Similarly, the use of lung age could also lead to a clinically significant increase in the reported smoking cessation rates (Kaminsky et al., 2011; Takagi et al., 2017; Parkes et al., 2008). Collectively, these data suggest that effective age metrics can help patients better understand their risk and lead to preventive changes. A web-based calculator ‘BONEcheck.org’ has been developed to assist healthcare professionals and the public to estimate the risk of fracture and skeletal age for an individual with specific risk profiles, potentially improving doctor-patient risk communication.

Our findings should be interpreted within the context of their strengths and limitations. First, we included a whole-country population with long follow-up and robust diagnostic data, minimizing potential selection bias and misclassification (Frank, 2000), and allowing us to examine mortality risk following individual fracture sites. Second, the current study analyzed both fracture and covariates, such as aging and the presence of comorbidities in a time-dependent manner, making it statistically rigorous in minimizing an immortal time bias and sufficiently accounting for confounding effects. The analysis thus provided accurate estimates of the association between specific fracture sites and mortality risk as it was able to control for confounding effects at both the study entry and the time of fracture.

However, the use of registry-based data, originally documented and coded for administrative or reimbursement purposes is prone to variable data accuracy, the lack of specific clinical information, and non-medical factors (Mazzali and Duca, 2015). Fortunately, all essential study variables (i.e. comorbidities, fracture, and death) were systematically obtained from the Danish NHDR that includes excellent, complete medical records and precise diagnoses for all individuals living in Denmark since 1995 (Andersen et al., 1999; Vestergaard and Mosekilde, 2002). The use of diagnosis-based comorbidities, though possibly associated with lower sensitivity than the self-reported ones (Lujic et al., 2017) is able to capture the severe health disorders that prompt the participants to seek for medical assistance. Second, the analyses could not make adjustments for lifestyle factors and physical activity, which are usually obtained in a cohort study. As they are closely related to aging and the presence of comorbidities which were already accounted for in our analysis, making further adjustments for these lifestyle factors is unlikely to substantially modify the findings. Third, mild, asymptomatic fractures or chronic diseases that did not require medical attention might not be registered in the Danish NHDR. It is nevertheless unlikely that these unregistered fractures and comorbidities would modify the findings significantly, as previous studies have indicated a high concordance between self-reported fractures and those registered in the NHDR (Hundrup et al., 2004), and a high positive predictive value of the self-reported comorbidities (Lujic et al., 2017). Finally, our analysis did not include the examination of the effect of bone metabolism-affecting medications on the assessment of skeletal health. However, these medications were prescribed to only a few individuals aged 50 years or over in Denmark (Vestergaard et al., 2005), even for those with a hip fracture (Roerholt et al., 2009), and there is no strong evidence from randomized controlled trials of their impact on post-fracture mortality (Cummings et al., 2019).

In conclusion, we advanced the concept of skeletal age as the age of an individual’s skeleton resulting from a fragility fracture. Unlike existing metrics (e.g. relative risk, probability of fracture), skeletal age combines the risk that an individual will sustain a fracture and the risk of mortality once a fracture has occurred, making the doctor-patient communication more intuitive and possibly more effective. Given the evidence of the successful implication of similar effective age metrics, skeletal age is expected to improve risk communication and ultimately improve treatment uptake among patients who are indicated for treatment. A randomized controlled trial aiming to compare the use of skeletal age and the current metrics in fracture risk communication is warranted.
