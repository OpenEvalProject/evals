# Dengue viremia kinetics and effects on platelet count and clinical outcomes: An analysis of 2340 patients from Vietnam

## Authors

- Nguyen Lam Vuong<sup>1</sup> ([ORCID: 0000-0003-2684-3041](https://orcid.org/0000-0003-2684-3041)) †
- Nguyen Than Ha Quyen<sup>2</sup>
- Nguyen Thi Hanh Tien<sup>2</sup>
- Kien Duong Thi Hue<sup>2</sup>
- Huynh Thi Le Duyen<sup>2</sup>
- Phung Khanh Lam<sup>1</sup> ([ORCID: 0000-0001-7968-473X](https://orcid.org/0000-0001-7968-473X))
- Dong Thi Hoai Tam<sup>2</sup>
- Tran Van Ngoc<sup>3</sup>
- Thomas Jaenisch<sup>4</sup>
- Cameron P Simmons<sup>6</sup> ([ORCID: 0000-0002-9039-7392](https://orcid.org/0000-0002-9039-7392))
- Sophie Yacoub<sup>2</sup>
- Bridget A Wills<sup>2</sup> ([ORCID: 0000-0001-9086-8804](https://orcid.org/0000-0001-9086-8804))
- Ronald Geskus<sup>2</sup> ([ORCID: 0000-0002-2740-3155](https://orcid.org/0000-0002-2740-3155)) †

### Affiliations

1. University of Medicine and Pharmacy at Ho Chi Minh City Ho Chi Minh City Viet Nam ([ROR:025kb2624](https://ror.org/025kb2624))
2. Oxford University Clinical Research Unit Ho Chi Minh City Viet Nam ([ROR:05rehad94](https://ror.org/05rehad94))
3. Hospital for Tropical Diseases Ho Chi Minh City Viet Nam ([ROR:040tqsb23](https://ror.org/040tqsb23))
4. Center for Global Health, Colorado School of Public Health Aurora United States ([ROR:005x9g035](https://ror.org/005x9g035))
5. Heidelberg Institute of Global Health (HIGH), Heidelberg University Hospital Heidelberg Germany ([ROR:013czdx64](https://ror.org/013czdx64))
6. Centre for Tropical Medicine and Global health, Nuffield Department of Clinical Medicine, University of Oxford Oxford United Kingdom ([ROR:052gg0110](https://ror.org/052gg0110))
7. World Mosquito Program, Monash University Clayton Australia ([ROR:02bfwt286](https://ror.org/02bfwt286))

† Corresponding author

## Abstract

Background:Viremia is a critical factor in understanding the pathogenesis of dengue infection, but limited data exist on viremia kinetics. This study aimed to investigate the kinetics of viremia and its effects on subsequent platelet count, severe dengue, and plasma leakage.Methods:We pooled data from three studies conducted in Vietnam between 2000 and 2016, involving 2340 dengue patients with daily viremia measurements and platelet counts after symptom onset. Viremia kinetics were assessed using a random effects model that accounted for left-censored data. The effects of viremia on subsequent platelet count and clinical outcomes were examined using a landmark approach with a random effects model and logistic regression model with generalized estimating equations, respectively. The rate of viremia decline was derived from the model of viremia kinetics. Its effect on the clinical outcomes was assessed by logistic regression models.Results:Viremia levels rapidly decreased following symptom onset, with variations observed depending on the infecting serotype. DENV-1 exhibited the highest mean viremia levels during the first 5–6 days, while DENV-4 demonstrated the shortest clearance time. Higher viremia levels were associated with decreased subsequent platelet counts from day 6 onwards. Elevated viremia levels on each illness day increased the risk of developing severe dengue and plasma leakage. However, the effect size decreased with later illness days. A more rapid decline in viremia is associated with a reduced risk of the clinical outcomes.Conclusions:This study provides comprehensive insights into viremia kinetics and its effect on subsequent platelet count and clinical outcomes in dengue patients. Our findings underscore the importance of measuring viremia levels during the early febrile phase for dengue studies and support the use of viremia kinetics as outcome for phase-2 dengue therapeutic trials.Funding:Wellcome Trust and European Union Seventh Framework Programme.

## Introduction

Dengue is the most common arboviral infection worldwide and is found mainly in tropical and subtropical areas. The disease has been a growing threat for decades, and in 2019 the World Health Organization (WHO) ranked it among the top 10 threats to global health (World Health Organization, 2009; World Health Organization, 2020). It is estimated that 105 million people are infected by dengue annually, of whom half develop symptoms (Cattarino et al., 2020). Although most infections are asymptomatic or self-limiting, the small proportion of patients who develop complications can still overwhelm health systems in dengue-endemic countries during seasonal epidemics. Climate change, increasing global travel, and urbanization all serve to amplify the distribution of Aedes aegypti, the main vector responsible for dengue transmission (Whitehorn and Yacoub, 2019; Yacoub et al., 2011). Although dengue has been known for centuries, specific treatment is still to be found, and the two licensed vaccines are of limited benefit (Kariyawasam et al., 2023; Redoni et al., 2020).

Exploring the variation in viremia levels could help improve our understanding of disease pathogenesis and potentially facilitate assessment of new vaccines and treatments for dengue. For example, knowing the natural kinetics of dengue viremia may help in selection of patient groups or timing of antiviral use in therapeutic intervention trials. Dengue viremia kinetics has been investigated in several studies (Ben-Shachar et al., 2016; Clapham et al., 2016; Clapham et al., 2014; Duyen et al., 2011; Matangkasombut et al., 2020; Nguyet et al., 2013; Simmons et al., 2007a; Tricou et al., 2011). The main findings are: (1) viremia rapidly decreases after symptom onset; (2) dengue virus (DENV)-1 infection gives higher viremia level than DENV-2 and DENV-3; and (3) primary infection gives higher viremia than secondary infection in DENV-1. However, these studies had limited sample sizes, particularly for DENV-4 serotype, and did not provide a full account of viremia kinetics. Three studies constructed mechanistic mathematical models and focused on investigating the role of the host immune response in controlling viremia (Ben-Shachar et al., 2016; Clapham et al., 2016; Clapham et al., 2014). Another study assessed viremia in infants aged under 18 months (Simmons et al., 2007a); the findings cannot be generalized to older children or adults. Others focused on peak viremia level after symptom onset, time to viral clearance and/or the probability of detecting virus on each illness day (Duyen et al., 2011; Matangkasombut et al., 2020; Nguyet et al., 2013; Tricou et al., 2011). In most analyses, viremia levels below the limit of detection were simply set as zero, which may not be appropriate.

Quantifying the effect of viremia level on clinical outcomes is important to understand the mechanisms leading to severe disease. We and others have previously found that higher viremia levels are associated with more severe dengue (Duyen et al., 2011; Endy et al., 2004; Morsy et al., 2020; Tang et al., 2010; Tricou et al., 2011; Vaughn et al., 2000; Vuong et al., 2021), but the effect size was not strong (Vuong et al., 2021). However, all analyses were based on a single viremia value per individual. Investigating how individual viremia levels at different times after symptom onset affect the risk of severe outcome potentially provides new insights into pathogenic mechanisms. Another important question is whether a more rapid decline in viremia is associated with a lower risk of more severe clinical outcomes. One study has shown a slower rate of viral clearance being associated with more severe outcomes (Wang et al., 2006), while others have shown no association (Fox et al., 2011; Vaughn et al., 2000). This lack of conclusive evidence underscores the need for further investigation. In addition, the relationship between viremia kinetics and platelet count kinetics – an important hematological indicator – has yet to be investigated.

This study aims to improve our understanding of viremia kinetics, how it is associated with patient characteristics and virus serotype, and how it impacts disease severity, using a dataset derived from several thousand individuals with symptomatic dengue. First, we fitted a model for individual viremia kinetics that treats values below the detection limit as censored data, and assessed whether viremia kinetics differed by age, sex, serotype, or immune status. Second, we modeled platelet count kinetics and explored dependence on viremia level. We investigated the potential existence of a lagged effect of viremia, by analyzing platelet counts measured on and following the day of viremia assessment. Third, we modeled the effect of viremia levels measured at different days after symptom onset and the effect of the rate of viremia decline on development of two clinical outcomes, plasma leakage and severe dengue.

## Methods

### Study population

We used data from three prospective observational studies performed as part of the longstanding collaboration between the Oxford University Clinical Research Unit (OUCRU) and the Hospital for Tropical Diseases (HTD) in Ho Chi Minh City, Vietnam. Protocol synopses for the three studies are presented in Appendix 1. Briefly, studies A and B simultaneously ran from 2000 to 2009 and enrolled children aged between 5 and 15 years. Study A included children with a febrile illness presenting to community outpatient clinics, while study B included children admitted to HTD with a febrile illness suspected to be dengue. Some patients from study A were subsequently enrolled in study B after admission to hospital. Study C ran from 2011 to 2016 and enrolled adults and children presenting with possible dengue within 3 days of fever onset (IDAMS study, NCT01550016) (Jaenisch et al., 2016). Clinical evaluation and blood sampling were performed daily for all three studies. All studies were approved by the Oxford Tropical Research Ethics Committee and the Institutional Ethics Committee.

We identified 3527 laboratory-confirmed dengue patients. Among them, 2340 had relevant data on viremia kinetics and were included in this analysis (Figure 1). Details of dengue diagnostics are in Appendix 2.

![Figure 1.](https://cdn.elifesciences.org/articles/92606/elife-92606-fig1-v1.jpg)

**Figure 1.:** @Among 385 laboratory-confirmed dengue patients in study A, 31 individuals were later included in study B upon hospitalization. Of these, nine had viremia measurements available in both studies and were consequently analysed in study A. The remaining 22 lacked viremia data in study A but had measurements in study B, leading to their inclusion in study B in the analysis. #Although study B spanned from 2000 to 2009, daily viremia levels were only measured between 2006 and 2008. $In study C, one study site in Vietnam did not have daily viremia measurements. Overall, a random sample of 2340 from 3527 laboratory-confirmed dengue patients had data on viremia kinetics. PCR, polymerase chain reaction.

### Plasma viremia measurement, dengue diagnostics, and clinical endpoints (details in Appendix 2)

Plasma viremia levels were measured by reverse transcription polymerase chain reaction (RT-PCR), which was an internally controlled, serotype-specific, real-time, two-step assay in studies A and B (Simmons et al., 2007b), and a one-step procedure using a validated assay in study C (Hue et al., 2011). There was no formal validation of the detection limit for viremia for the two-step PCR used in studies A and B; we set it at 1000 copies/ml. In the one-step PCR used in study C, the detection limit was 300 copies/ml for DENV-1 and DENV-3, 60 copies/ml for DENV-2, and 600 copies/ml for DENV-4 (Hue et al., 2011).

Patients were classified into probable primary (i.e., the first) or probable secondary (i.e., a second or subsequent) infection based on IgG results on paired samples. A probable primary infection was defined by two negative/equivocal IgG results on separate samples taken at least 2 days apart within the first 10 days of symptom onset, with at least one sample during the convalescent phase (days 6–10). A probable secondary infection was defined by at least one positive IgG result during the first 10 days. Cases without time-appropriate IgG results were classified as indeterminate.

For the clinical endpoints we selected severe dengue and plasma leakage. The definitions are based on the WHO 2009 guidelines (World Health Organization, 2009) and standard endpoint definitions for dengue trials (Tomashek et al., 2018). Severe dengue was defined as severe plasma leakage, severe bleeding, and/or severe organ impairment. Plasma leakage included moderate and severe leakage.

### Statistical analysis (details in Appendix 3)

In Appendix 3—figure 1 we show a directed acyclic graph (DAG) to display assumptions about the causal relationships between variables over illness day. Illness day is the number of days after symptom onset, where day 1 is the day of symptom onset. Potential confounders that needed to be corrected for were age, sex, DENV serotype, and primary/secondary immune status. In all analyses, we used a log-10 transformation for viremia levels.

We modeled viremia kinetics over time and explored dependence on age, sex, serotype, immune status, and PCR method using a linear mixed-effects regression model, allowing for left-censored values in the outcome variable. In the fixed effect, we allowed for interactions between serotype and immune status, and between illness day and all other covariates. Nonlinear trends by age and illness day were investigated using splines with three and four knots, respectively. We included a random effect with an intercept and splines for illness day with four knots to model the intra-person correlation. Due to the presence of a left-skewed distribution in log-10 viremia (Appendix 4—figure 1), a sensitivity analysis was conducted using the 10th-root transformation.

Platelet counts were transformed using a fourth-root transformation since the distribution was right-skewed (Appendix 4—figure 2). The effect of viremia on subsequent platelet count was investigated using the landmark approach (van Houwelingen and Putter, 2011). For each illness day from 1 to 7, a landmark dataset was created, which included viremia on that day, platelet count from that day to day 10, and the time-fixed variables (age, sex, serotype, immune status, and PCR method). For the supermodel that combined all landmark datasets, we used a linear mixed-effects model including viremia, age, sex, serotype, immune status, PCR method, illness day and landmark. In the fixed effect, we also included four-way interactions between viremia, serotype, PCR method and (1) and immune status, (2) illness day, and (3) landmark day. Splines with three knots were used to allow for nonlinear trends in log-10 viremia, age, illness day, and landmark day. We included a random effect with an intercept by the combination of individuals and landmark, and splines for illness day with three knots.

The effect of viremia on the clinical endpoints was investigated using a logistic regression model using the landmark approach (van Houwelingen and Putter, 2011). For each illness day from 1 to 7, a landmark dataset was created, which included viremia on that day, occurrence of the endpoint on or after that day, and the time-fixed variables similar to above. All individuals who had already experienced the relevant endpoint before that day were excluded. We fitted a logistic regression model for each landmark dataset and then fitted a supermodel that combined all the datasets. For the supermodel we used generalized estimating equations to account for repeated inclusion of individuals at multiple landmarks. We included viremia, age, sex, serotype, immune status, study, and landmark day, and allowed for the four-way interaction between viremia, serotype, immune status, and landmark day, and two-way interactions between viremia and all other covariates. Splines were used to allow for nonlinear trends in log-10 viremia (three knots), age (three knots), and landmark (three knots). Since plasma leakage had missing data, we performed an analysis with imputed data using multiple imputation by chained equations. The imputation was done in our previous study (Vuong et al., 2021).

To calculate the rate of viremia decline for each patient, we assumed a linear decline in log-10 viremia over time. We modified our viremia kinetics model by using a linear term for illness day rather than the original nonlinear terms, both in the fixed and in the random effect. For each patient, we then calculated fitted values using this model. The rate of viremia decline was defined as the daily difference in log-10 viremia. We assessed the impact of the decline rate on the clinical endpoints using logistic regression models. We did not use the landmark approach for this analysis since the decline rate was assumed to be constant over time. Covariates included the decline rate, serotype, immune status, and PCR method. Due to limited number of severe dengue cases, its model did not include any interaction terms. The plasma leakage model incorporated interactions between the decline rate and all other covariates.

In the analyses for platelet count and clinical outcomes, undetectable viremia levels were set as the specific detection limits, and a binary dummy variable (yes/no) was created to indicate whether the viremia value was undetectable. Since the individual spline terms are hard to interpret and the large dataset makes most differences statistically significant, results are primarily reported using plots of predicted values. All analyses were done using the statistical software R version 4.1.0 (R Core Team, 2021) with ‘MCMCglmm’ (Hadfield, 2010), ‘lme4’ (Bates et al., 2015), ‘geepack’ (Halekoh et al., 2006), and ‘rms’ (Harrell, 2021) packages for the models.

## Results

Baseline characteristics and outcomes are summarized in Table 1. Three quarters of the participants were children, and male sex predominated (60%). Most patients (85%) were enrolled on illness day 2 or 3. All four serotypes were included, but DENV-1 was the most prevalent (54%). Most infections (69%) were classified as probable secondary infection, while in 11% immune status could not be determined. There were 353 patients (15%) with plasma leakage and 65 patients (3%) with severe dengue. In Appendix 4—table 1, we summarize plasma leakage and severe dengue by serotype and immune status. DENV-2 had the highest proportion of these two outcomes. Patients with probable secondary infection were more likely to experience these outcomes than those with probable primary infection or indeterminate immune status, regardless of the infecting serotype.

**Table 1.**
 Baseline characteristics and clinical outcomes.


<table>
  <thead>
    <tr>
      <th></th>
      <th>N*</th>
      <th>All patients (N = 2340)</th>
      <th>Study A (N = 363)</th>
      <th>Study B (N = 622)</th>
      <th>Study C (N = 1355)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Age, years</td>
      <td>2340</td>
      <td>13 (10; 18)</td>
      <td>12 (9; 14)</td>
      <td>12 (10; 13)</td>
      <td>16 (10; 25)</td>
    </tr>
    <tr>
      <td>Sex male</td>
      <td>2340</td>
      <td>1403 (60)</td>
      <td>195 (54)</td>
      <td>412 (66)</td>
      <td>796 (59)</td>
    </tr>
    <tr>
      <td>Illness day at enrolment</td>
      <td>2340</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>1</td>
      <td></td>
      <td>310 (13)</td>
      <td>59 (16)</td>
      <td>7 (1)</td>
      <td>244 (18)</td>
    </tr>
    <tr>
      <td>2</td>
      <td></td>
      <td>848 (36)</td>
      <td>150 (41)</td>
      <td>155 (25)</td>
      <td>543 (40)</td>
    </tr>
    <tr>
      <td>3</td>
      <td></td>
      <td>1137 (49)</td>
      <td>114 (31)</td>
      <td>455 (73)</td>
      <td>568 (42)</td>
    </tr>
    <tr>
      <td>4</td>
      <td></td>
      <td>45 (2)</td>
      <td>40 (11)</td>
      <td>5 (1)</td>
      <td>0 (0)</td>
    </tr>
    <tr>
      <td>Serotype</td>
      <td>2340</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>DENV-1</td>
      <td></td>
      <td>1264 (54)</td>
      <td>233 (64)</td>
      <td>410 (66)</td>
      <td>621 (46)</td>
    </tr>
    <tr>
      <td>DENV-2</td>
      <td></td>
      <td>373 (16)</td>
      <td>48 (13)</td>
      <td>130 (21)</td>
      <td>195 (14)</td>
    </tr>
    <tr>
      <td>DENV-3</td>
      <td></td>
      <td>252 (11)</td>
      <td>80 (22)</td>
      <td>82 (13)</td>
      <td>90 (7)</td>
    </tr>
    <tr>
      <td>DENV-4</td>
      <td></td>
      <td>451 (19)</td>
      <td>2 (1)</td>
      <td>0 (0)</td>
      <td>449 (33)</td>
    </tr>
    <tr>
      <td>Immune status</td>
      <td>2340</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Probable primary</td>
      <td></td>
      <td>474 (20)</td>
      <td>134 (37)</td>
      <td>124 (20)</td>
      <td>216 (16)</td>
    </tr>
    <tr>
      <td>Probable secondary</td>
      <td></td>
      <td>1619 (69)</td>
      <td>219 (60)</td>
      <td>464 (75)</td>
      <td>936 (69)</td>
    </tr>
    <tr>
      <td>Indeterminate</td>
      <td></td>
      <td>247 (11)</td>
      <td>10 (3)</td>
      <td>34 (5)</td>
      <td>203 (15)</td>
    </tr>
    <tr>
      <td>Plasma leakage</td>
      <td>2288</td>
      <td>353 (15)</td>
      <td>43 (13)</td>
      <td>177 (29)</td>
      <td>133 (10)</td>
    </tr>
    <tr>
      <td>Missing</td>
      <td></td>
      <td>52</td>
      <td>39</td>
      <td>13</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Illness day of plasma leakage</td>
      <td>327</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>3</td>
      <td></td>
      <td>2 (1)</td>
      <td>0 (0)</td>
      <td>0 (0)</td>
      <td>2 (2)</td>
    </tr>
    <tr>
      <td>4</td>
      <td></td>
      <td>71 (22)</td>
      <td>12 (30)</td>
      <td>35 (23)</td>
      <td>24 (18)</td>
    </tr>
    <tr>
      <td>5</td>
      <td></td>
      <td>107 (33)</td>
      <td>12 (30)</td>
      <td>50 (32)</td>
      <td>45 (34)</td>
    </tr>
    <tr>
      <td>6</td>
      <td></td>
      <td>105 (32)</td>
      <td>12 (30)</td>
      <td>49 (32)</td>
      <td>44 (33)</td>
    </tr>
    <tr>
      <td>7</td>
      <td></td>
      <td>42 (13)</td>
      <td>4 (10)</td>
      <td>20 (13)</td>
      <td>18 (14)</td>
    </tr>
    <tr>
      <td>Missing</td>
      <td></td>
      <td>26</td>
      <td>3</td>
      <td>23</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Severe dengue</td>
      <td>2340</td>
      <td>65 (3)</td>
      <td>6 (2)</td>
      <td>40 (6)</td>
      <td>19 (1)</td>
    </tr>
    <tr>
      <td>Illness day of severe dengue</td>
      <td>65</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>3</td>
      <td></td>
      <td>2 (3)</td>
      <td>0 (0)</td>
      <td>2 (5)</td>
      <td>0 (0)</td>
    </tr>
    <tr>
      <td>4</td>
      <td></td>
      <td>13 (20)</td>
      <td>0 (0)</td>
      <td>12 (30)</td>
      <td>1 (5)</td>
    </tr>
    <tr>
      <td>5</td>
      <td></td>
      <td>24 (37)</td>
      <td>2 (33)</td>
      <td>16 (40)</td>
      <td>6 (32)</td>
    </tr>
    <tr>
      <td>6</td>
      <td></td>
      <td>20 (31)</td>
      <td>4 (67)</td>
      <td>7 (18)</td>
      <td>9 (47)</td>
    </tr>
    <tr>
      <td>7</td>
      <td></td>
      <td>6 (9)</td>
      <td>0 (0)</td>
      <td>3 (8)</td>
      <td>3 (16)</td>
    </tr>
  </tbody>
</table>

_Summary statistics are number of patients (%) or median (25th; 75th percentiles).DENV: dengue virus.*N represents the number of patients with available data (i.e., without missing data)._

### Viremia kinetics and the relationship with clinical characteristics

Individual viremia trajectories are shown in Figure 2. Most individuals had a decreasing trend from day 1 or 2 onwards. However, values higher than the baseline value were observed up to day 7 (Appendix 4—figure 3). The decreasing trend was consistent across all combinations of serotype and immune status (Figure 2).

![Figure 2.](https://cdn.elifesciences.org/articles/92606/elife-92606-fig2-v1.jpg)

**Figure 2.:** The dots represent the measured viremia levels and are connected by lines for each individual patient. The dashed lines indicate the detection limits, which are 300 copies/ml for DENV-1 and DENV-3, 60 copies/ml for DENV-2, and 600 copies/ml for DENV-4 in the one-step PCR cohort, and 1000 copies/ml in the two-step PCR cohort. Fifty-seven measured values that are lower than 1000 copies/ml in the two-step PCR cohort are considered as below the detection limit. Values below the detection limit are visually represented as 1/10 of the corresponding detection limit (on the original scale). DENV, dengue virus; PCR, polymerase chain reaction.

In Figure 3, we present the fitted values based on the model for viremia for the one-step PCR cohort. The mean viremia trajectory differed by serotype. DENV-1 gave the highest viremia levels, with DENV-2 in secondary infection giving similar levels from day 5 onwards. DENV-2, DENV-3, and DENV-4 had similar viremia levels during the first 3 days. However, viremia decreased rapidly in DENV-4, reaching undetectable levels in the shortest time, while DENV-2 showed the slowest decline. These differences between serotypes were more pronounced in case of probable primary infection (Figure 3A). In terms of immune status, probable primary infection showed higher viremia levels compared to probable secondary infection in DENV-1 from day 3 onwards. The disparity between probable primary and probable secondary infection was less pronounced in the other serotypes (Figure 3B). Mean viremia levels were comparable between females and males (Figure 3C), as well as across age (Figure 3D). The one-step PCR method resulted in longer viremia compared to the two-step PCR (Appendix 5—figure 1). P values for the differences by age, serotype, immune status, and illness day were all <0.0001 (Appendix 5—table 1). The sensitivity analysis using the 10th-root transformation of viremia gave results similar to the main analysis using log-10 viremia (Appendix 5—figure 2).

![Figure 3.](https://cdn.elifesciences.org/articles/92606/elife-92606-fig3-v1.jpg)

**Figure 3.:** The colored lines represent the estimated mean viremia levels, and the colored shaded regions represent the corresponding 95% credible intervals. The horizontal lines represent the detection limits (D1, D2, D3, and D4 denote DENV-1, DENV-2, DENV-3, and DENV-4, respectively). Dashed lines indicate fitted viremia levels that are below the detection limit. Viremia levels are shown for age of 10 years, male sex, serotype DENV-1, probable secondary infection, and using the one-step PCR. DENV, dengue virus; PCR, polymerase chain reaction.

### Effect of viremia on subsequent platelet count

Figure 4 shows the mean platelet counts by viremia levels based on the supermodel for the one-step PCR method. There was minimal impact of viremia on days 1–5 platelet count. However, higher viremia levels gave decreased subsequent platelet counts from day 6 onwards, for all serotypes. The strength of this effect increased with later illness day and was more pronounced in DENV-1 and DENV-2 compared to DENV-3 and DENV-4. All covariates had low p values (Appendix 6—table 1). The effect of viremia on subsequent platelet count remained consistent across subgroups of immune status, sex, and age. In the two-step PCR cohort, the effect of viremia on platelet count was less pronounced compared to the one-step PCR cohort, although the overall trends were similar (Appendix 6—figure 1).

![Figure 4.](https://cdn.elifesciences.org/articles/92606/elife-92606-fig4-v1.jpg)

**Figure 4.:** The colored lines or dots represent the estimated mean platelet counts. The colored shaded regions and whiskers indicate the corresponding 95% confidence intervals. Each row represents the effect of viremia on a specific day to platelet count from that day to day 10. No fitted trends are made for DENV-4 in LM day 7 since viremia was undetectable in almost all DENV-4 cases from day 7 onwards. The mean platelet counts are shown for age of 10 years, male sex, probable secondary infection, and using the one-step PCR. DENV, dengue virus; LM, landmark; PCR, polymerase chain reaction; U, under the limit of detection.

### Effect of viremia on clinical outcomes

Higher viremia levels increased the risk of severe dengue and plasma leakage for each of the serotypes (Figure 5). The effect of viremia on both endpoints decreased with later landmark day of viremia measurement, particularly for severe dengue (Appendix 7—table 1). However, these trends were not clear in the results obtained from the simple logistic regression models at each landmark time point (Appendix 7—figure 1). This trend remained consistent across subgroups of sex, age, and study (Appendix 7—figure 2). Furthermore, the results were consistent between the analyses with and without imputation (Appendix 7—figure 3).

![Figure 5.](https://cdn.elifesciences.org/articles/92606/elife-92606-fig5-v1.jpg)

**Figure 5.:** The colored lines or dots represent the probability of the endpoints. The colored shaded regions and whiskers indicate the corresponding 95% confidence intervals. Each column represents the effect of viremia on a specific day. No fitted trends are made for DENV-4 in LM day 7 since viremia was undetectable in almost all DENV-4 cases from day 7 onwards. Note that due to the limited number of severe dengue in primary infections (only 1 case in DENV-1) and plasma leakage in primary DENV-4 (see Appendix 4—table 1), the estimated probability of having these outcomes is nearly zero across all viremia levels within these subgroups. The probabilities are shown for age of 10 years, male sex, probable secondary infection, and from Study C. DENV, dengue virus, LM, landmark; PCR, polymerase chain reaction; U, under the limit of detection.

The supermodel revealed that older individuals had a relatively lower risk of developing severe dengue, but the trend was not significant. Males exhibited a slightly higher risk of severe dengue compared to females. The effect of serotype on the two endpoints was dependent on immune status. Individuals with probable secondary infection had a higher risk of experiencing both endpoints compared to those with probable primary infection (Appendix 7—figure 4).

From the model of viremia kinetics with a linear trend of illness day, the individual rate of viremia decline ranged from 0.58 to 2.01 log-10 copies/ml/day, with a median of 1.39 log-10 copies/ml/day. The logistic regression model demonstrated that a faster decline in viremia reduced the risk of severe dengue and plasma leakage (Figure 6). The effect on plasma leakage was stronger in the probable secondary infection group (Appendix 7—table 2).

![Figure 6.](https://cdn.elifesciences.org/articles/92606/elife-92606-fig6-v1.jpg)

**Figure 6.:** The colored lines represent the probability of the endpoints. The colored shaded regions indicate the corresponding 95% confidence intervals.

## Discussion

In this study, we conducted a comprehensive analysis using a large dataset of 2340 viremic dengue patients to examine viremia kinetics from first presentation, its association with various virus and patient characteristics, and its impact on subsequent platelet count and disease severity. As others have described, we found that plasma viremia declines rapidly following the onset of symptoms, with the kinetics primarily influenced by the specific infecting serotype. Higher viremia levels were associated with a decrease in subsequent platelet count from day 6 onwards. Elevated viremia levels were found to increase the risk of developing severe dengue and plasma leakage, with the effect becoming weaker at later days. The effects of viremia on platelet count and clinical outcomes did not differ much by different subgroups of serotype, immune status, age, and sex. Moreover, a faster decline in viremia was associated with a reduced risk of the more severe clinical outcomes.

There is a limited number of published papers that studied the individual trajectory of dengue viremia. Most used data from Vietnam (Ben-Shachar et al., 2016; Clapham et al., 2016; Clapham et al., 2014; Duyen et al., 2011; Nguyet et al., 2013; Simmons et al., 2007a; Tricou et al., 2011), while one was from Thailand (Matangkasombut et al., 2020). Our study has provided further evidence supporting previous findings. We confirmed that (1) viremia rapidly decreases following the onset of symptoms, (2) DENV-1 exhibits higher viremia levels compared to DENV-2 and DENV-3, and (3) primary infection is associated with higher and more prolonged detectable viremia than secondary infection in DENV-1, while this pattern was not consistent across other serotypes. We have added viremia kinetics of DENV-4, and showed that viremia levels declined more rapidly than the other serotypes. Furthermore, our study demonstrated that the new PCR test has the ability to detect plasma viremia for a longer period compared to the older test. This may be attributed to the lower detection limits of the new test. Explaining the differences in viremia kinetics between serotypes remains challenging, as the molecular factors of the virus that influence plasma viremia levels are still unknown. It is also important to note that our study focused on the time since symptom onset rather than the time since infection. We cannot rule out that some of the observed differences are explained by a difference in time from infection to symptom onset.

Our study suggests that higher viremia levels on any day before day 6 are associated with reduced platelet count on days 6–8, typically corresponding to the nadir of platelet count. Additionally, it is possible that viremia in the initial 4 days after symptom onset could affect platelet count with a delay of 3–4 days. The direct involvement of the dengue virus in triggering platelet activation and apoptosis can contribute to the development of thrombocytopenia. Thrombocytopenia in dengue infection is thought to occur through two mechanisms: bone marrow suppression, which reduces thrombopoiesis, and increased peripheral platelet clearance (Quirino-Teixeira et al., 2022). Various processes contribute to these mechanisms, including platelet–leukocyte and platelet–endothelial cell interactions, phagocytosis, complement-mediated lysis, aggregation, and clot formation. Additionally, several host immune response factors are involved in platelet activation (Balakrishna Pillai et al., 2022). In our analysis, we considered interactions between viremia level and both serotype and immune status. Interestingly, we observed that the effect of viremia level on subsequent platelet count did not differ much by serotype and immune status.

Higher plasma viremia levels increase the risk of worse clinical outcomes, as demonstrated in our previous study that only utilized viremia at enrollment during the febrile phase (Vuong et al., 2021). The diminishing impact of viremia on the two endpoints on later illness days may be attributed to the heightened immune responses that are likely triggered by higher viremia levels, and the resulting complex interplay between these factors that underlies progression to severe dengue. The effects of viremia, age, serotype, immune status, and illness day on the clinical endpoints in this study are consistent with those observed in the previous study. The similarity between these two analyses, along with the weaker effect of viremia at later days, suggests that viremia levels around the time of symptom onset could serve as a reliable predictor of dengue severity. It suggests that the early febrile phase, specifically illness days 1–3, is the critical period of measuring viremia levels in clinical practice and dengue studies. Secondary infection remains a substantial risk factor for more severe outcomes, while viremia kinetics are not influenced much by immune status. These findings suggest that immune status and viremia may be independent predictors of clinical outcomes, following distinct pathways.

The landmark approach enabled us to investigate the effect of viremia on platelet count and the clinical endpoints at each illness day, ranging from days 1 to 7, while ensuring that the viremia measurements preceded the occurrence of the outcomes. The supermodel allows for investigation of trends of the effects, while gaining power because we assume the effects of some fixed factors (e.g., age and sex) to remain constant over time. There might be other potential confounders such as host genetic and immune response factors, but these data were not available. Moreover, we assumed that the relation between viremia level and platelet count was one-way: viremia level affects platelet count. Whether platelet count affects viremia is unknown.

A notable strength of our study is the utilization of a large pooled dataset, which allowed for a flexible modeling approach to investigate the influence of age, sex, serotype, and immune status, as well as their interactions and nonlinear trends. The use of a model that accounts for left-censored data was needed for capturing the distribution of viremia levels, considering the significant proportion of undetectable values observed.

The study has several limitations. First, the study only included patients from Vietnam, which may restrict the generalizability of the findings to other countries and regions. Second, our study assessed viral RNA in the plasma, including both viable and non-viable viral particles, which could potentially lead to an overestimation of the infectious viral particles in the blood. Lastly, data during the incubation period were unavailable as patients are typically not diagnosed with dengue until symptom onset. Therefore, the trajectory of viremia from the time of infection onwards could not be demonstrated, and symptom onset was used as the reference point instead of infection. This could potentially lead to an inaccurate interpretation of the results if the incubation period is influenced by the same factors that we included in our analyses. For example, in cases of secondary infection, the immune response is stronger and quicker than in primary infection. This might lead to a shorter duration between infection and symptom onset, as well as faster viral clearance.

In conclusion, our findings reveal that viremia levels exhibit a rapid decline shortly after symptom onset, becoming undetectable after approximately 1 week in the majority of patients. Viremia kinetics display variations depending on the infecting serotype. Higher viremia levels are associated with a subsequent reduction in platelet count on illness days 6–8, and an increased risk of experiencing more severe clinical outcomes. Viremia serves as an important predictor of dengue outcomes, independent of the host immune status. However, when considering our previous analysis that involved single early viremia measurements, the addition of daily viremia measurements may not enhance the prediction of worse clinical outcomes. Thus, the measurement of viremia levels during the early febrile phase is an important marker for clinical practice and dengue-related research. Moreover, a faster decline in viremia was found to be associated with a reduced risk of more severe clinical outcomes, suggesting that viremia kinetics could be a good surrogate endpoint for phase-2 dengue therapeutic trials.
