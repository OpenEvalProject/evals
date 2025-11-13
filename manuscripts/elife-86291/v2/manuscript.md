# VO2max prediction based on submaximal cardiorespiratory relationships and body composition in male runners and cyclists: a population study

## Authors

- Szczepan Wiecha<sup>1</sup> ([ORCID: 0000-0001-9458-557X](https://orcid.org/0000-0001-9458-557X)) †
- Przemysław Seweryn Kasiak<sup>2</sup> ([ORCID: 0000-0002-0303-6135](https://orcid.org/0000-0002-0303-6135))
- Piotr Szwed<sup>3</sup>
- Tomasz Kowalski<sup>4</sup>
- Igor Cieśliński<sup>1</sup>
- Marek Postuła<sup>3</sup>
- Andrzej Klusiewicz<sup>1</sup>

### Affiliations

1. Department of Physical Education and Health in Biala Podlaska, Faculty in Biala Podlaska, Jozef Pilsudski University of Physical Education Warsaw Poland ([ROR:043k6re07](https://ror.org/043k6re07))
2. Students' Scientific Group of Lifestyle Medicine, 3rd Department of Internal Medicine and Cardiology, Medical University of Warsaw Warsaw Poland ([ROR:04p2y4s44](https://ror.org/04p2y4s44))
3. Department of Experimental and Clinical Pharmacology, Center for Preclinical Research and Technology CEPT, Medical University of Warsaw Warsaw Poland ([ROR:04p2y4s44](https://ror.org/04p2y4s44))
4. Institute of Sport-National Research Institute Warsaw Poland

† Corresponding author

## Abstract

Background:Oxygen uptake (VO2) is one of the most important measures of fitness and critical vital sign. Cardiopulmonary exercise testing (CPET) is a valuable method of assessing fitness in sport and clinical settings. There is a lack of large studies on athletic populations to predict VO2max using somatic or submaximal CPET variables. Thus, this study aimed to: (1) derive prediction models for maximal VO2 (VO2max) based on submaximal exercise variables at anaerobic threshold (AT) or respiratory compensation point (RCP) or only somatic and (2) internally validate provided equations.Methods:Four thousand four hundred twenty-four male endurance athletes (EA) underwent maximal symptom-limited CPET on a treadmill (n=3330) or cycle ergometer (n=1094). The cohort was randomly divided between: variables selection (nrunners = 1998; ncyclist = 656), model building (nrunners = 666; ncyclist = 219), and validation (nrunners = 666; ncyclist = 219). Random forest was used to select the most significant variables. Models were derived and internally validated with multiple linear regression.Results:Runners were 36.24±8.45 years; BMI = 23.94 ± 2.43 kg·m−2; VO2max=53.81±6.67 mL·min−1·kg−1. Cyclists were 37.33±9.13 years; BMI = 24.34 ± 2.63 kg·m−2; VO2max=51.74±7.99 mL·min−1·kg−1. VO2 at AT and RCP were the most contributing variables to exercise equations. Body mass and body fat had the highest impact on the somatic equation. Model performance for VO2max based on variables at AT was R2=0.81, at RCP was R2=0.91, at AT and RCP was R2=0.91 and for somatic-only was R2=0.43.Conclusions:Derived prediction models were highly accurate and fairly replicable. Formulae allow for precise estimation of VO2max based on submaximal exercise performance or somatic variables. Presented models are applicable for sport and clinical settling. They are a valuable supplementary method for fitness practitioners to adjust individualised training recommendations.Funding:No external funding was received for this work.

## Introduction

The oxygen uptake (VO2) is considered an important metric in assessing cardiorespiratory fitness, health status, or endurance performance potential (Guazzi et al., 2012). With the application of standardised procedures and interpretation protocols, during graded exercise tests (GXT), the (maximal oxygen uptake) VO2max can be established (Bentley et al., 2007). GXT is the most widely used assessment to examine the dynamic relationship between exercise and integrated physiological systems (Albouaini et al., 2007; Bentley et al., 2007). The information from GXT during cardiopulmonary exercise testing (CPET) can be applied across the spectrum of sport performance, occupational safety screening, research, and clinical diagnostics (Guazzi et al., 2017).

VO2 max is often used as a boundary between severe and extreme intensity domains and by definition requires maximal effort from the tested subject (Gaesser and Poole, 1996). However, it is not always recommended or possible to undertake a test to exhaustion (Guazzi et al., 2012). For the athletes, the proximity of competition or injury history can allow submaximal testing, but not testing to exhaustion (Sassi et al., 2006). Testing that requires maximal effort may be disruptive to the training process or interfere with race performance (Coutts et al., 2007; Lamberts et al., 2011). Due to practical constraints, tests to exhaustion or peak-power-output tests are often performed only two or three times a year (Coutts et al., 2007).

However, VO2 values are widely used in sport science and the decision-making process (Mann et al., 2013). VO2 is widely considered one of the major endurance performance determinants (Joyner and Coyle, 2008). Using VO2max to guide the selection process, prescribing training intensity, assessing training adaptations, or predicting race times is a common practice in high-performance sports (Bassett and Howley, 2000; Bentley et al., 2007; Hawley and Noakes, 1992; Noakes et al., 1990).

VO2max is also one of the critical vital signs coordinating the function of the cardiovascular, respiratory, and muscular systems, it is an indicator of overall body health status (Kaminsky et al., 2017). Quantifying VO2max provides additional input regarding clinical decision-making, risk stratification, evaluation of therapy, and physical activity guidelines (Guazzi et al., 2012). For patients undertaking a test to exhaustion is rarely needed or possible due to health restraints or cardiac risk (Guazzi et al., 2016).

For many years researchers have studied indirect methods of estimating VO2max(Sartor et al., 2013). Protocols such as the Astrand-Ryhming Test, Six-Minute Walk Test, or YMCA Step Test have been established and validated (Astrand and Ryhming, 1954; Beutner et al., 2015; Carey, 2022; Jalili et al., 2018). Moreover, estimation of the VO2 and heart rate (HR) values below the ventilatory threshold can be based on cardiorespiratory kinetics assessment using randomised changes in the work rate known as a pseudo-random binary sequences testing (Hoffmann et al., 2022). However, with the development of technology, the accessibility of laboratory testing and mobile testing improved (Montoye et al., 2020; Pritchard et al., 2021). Therefore, new opportunities to develop more precise yet simple and accessible methods and models to assess VO2max occur (Jurov et al., 2023). This appears to be especially important considering the low prediction accuracy of most of the VO2max formulae that were validated in our previous study (Wiecha et al., 2023).

Recently, we have been observing the development of prediction methods with the usage of machine learning (ML) and artificial intelligence (AI) (Ashfaq et al., 2022). Both ML and AI are used in sport science as forecasting and decision-making support tools (Abut and Akay, 2015; Bobowik and Wiszomirska, 2022; Chmait and Westerbeek, 2021; Hammes et al., 2022; Rossi et al., 2021). There is growing evidence that VO2max prediction based on ML models, especially support vector ML and artificial neural network models, exhibits more robust and accurate results compared to MLR only (Abut and Akay, 2015; Ashfaq et al., 2022).

Therefore, in this research, with the support of ML, we look for algorithms and prediction patterns that allow us to use values obtained during submaximal CPET and somatic measurements to estimate maximal VO2max values in male runners and cyclists. We stipulate that prediction models allow for accurate calculation of VO2max based on somatic or submaximal CPET variables.

## Materials and methods

We have applied the development and validation of the prediction TRIPOD guidelines to conduct the study (see Supplementary Material 1TRIPOD Checklist for Prediction Model Development and Validation) (Collins et al., 2015). The study is based on retrospective data analysis from the CPET registry collected from 2013 to 2021 at the medical clinic (Sportslab, Warsaw, Poland). All CPET have been performed at the individual request of participants, as a part of regular training monitoring or performance assessment.

### Ethical approval

The Institutional Review Board of the Bioethical Committee at the Medical University of Warsaw (AKBE/32/2021) has approved the study protocol. The regulations of the Declaration of Helsinki were met during all parts of the study. Each study participant delivered written consent to undergo CPET and participate in the study.

### Derivation cohort

We selected the cohort with the use of rigorous exclusion/inclusion criteria. Due to the insufficient number of women in our database and the number of potential variables in the regression models for adequate power, we had to limit ourselves to conduct analysis in the male population only (Martens and Logan, 2021). Out of 6439 healthy, adult male cyclists and long-distance runners that undergone CPET, 4423 met the criteria as further: (1) age ≥18 years, (2) declared regular cycling or running training for ≥3 months, (3) had no extreme outliers ≤ or ≥±3 standard deviations (SD) from mean for all of the testing variables (beyond ≥±3 SD in VO2max), (4) lack of any injury, medical condition, or addiction in medical history that may affect exercise capacity, (5) not taking any medications with a modifying effect on exercise capacity, (6) maximum exertion achieved during CPET. We defined the maximum exertion in CPET as the fulfilment of the minimum six of the following criteria: (1) respiratory exchange ratio (RER) ≥1.10, (2) present VO2 plateau (growth <100 mL·min–1 in VO2 despite increased running speed or cycling power), (3) respiratory frequency (fR) ≥45 breaths·min–1, (4) declared subjective exertion intensity during CPET ≥18 in the Borg scale (Borg, 1970), (5) blood lactate concentration [La-]b ≥8 mmol·L–1, (6) growth in speed/power ≥10% of respiratory compensation point (RCP) values after exceeding the RCP, (7) peak heart rate (HRpeak) ≥15 beats·min–1 below predicted maximal heart rate (HRmax) (Lach et al., 2021).

Participants’ selection procedure has been shown in Figure 1.

![Figure 1.](https://cdn.elifesciences.org/articles/86291/elife-86291-fig1-v2.jpg)

**Figure 1.:** Abbreviations: EA, endurance athlete; CPET, cardiopulmonary exercise testing; SD, standard deviation; TE, treadmill; RER, respiratory exchange ratio; VO2, oxygen uptake (mL·min−1·kg−1); [La−]b, lactate concentration (mmol·L−1); fR, breathing frequency (breaths·min−1); RCP, respiratory compensation point; HRpeak, peak heart rate (beats·min−1); HRmax, maximal heart rate (bpm). At both stages of the selection, some participants met several (>1) exclusion criteria.

### Somatic measurements and CPET protocols

Body mass was measured with a body composition (BC) analyser (Tanita, MC 718, Japan) with the multifrequency of 5 kHz/50 kHz/250 kHz via the bioimpedance analysis and normal testing mode. The participants’ skin was cleaned with alcohol before placing the electrodes on the skin. Prior to the test, the participants received instructions to refrain from exercising for 2 hr, consume a light meal rich in carbohydrates 2–3 hr beforehand, and maintain hydration by drinking isotonic beverages. Additionally, they were advised to abstain from medications, caffeine, and cigarettes on the day of the test.

Running CPET (TE) was performed on a mechanical treadmill (h/p/Cosmos Quasar, Germany). Cycling CPET (CE) was performed on Cyclus-2 (RBM elektronik-automation GmbH, Leipzig, Germany). Hans Rudolph V2 mask (Hans Rudolph, Inc, Shawnee, KS, USA), breath-by-breath method with Cosmed Quark CPET gas exchange analysing device (Cosmed Srl, Rome, Italy), and Quark PFT Suite to Omnia 1.6 software were utilised. The gas analyser device was regularly calibrated with the reference gas (16% O2; 5% CO2) in accordance with the manufacturer’s instructions (Airgas USA, LLC, Plumsteadville, PA, USA). From 2013 to 2021, three Cosmed Quark CPET units were used. HR was measured with the Cosmed torso belt (Cosmed srl, Rome, Italy). [La-]b was measured via enzymatic-amperometric electrochemical technique with Super GL2 analyser (Müller Gerätebau GmbH, Freital, Germany). The [La-]b analyser was regularly calibrated before each measurement series. The 40 m2 indoor, air-conditioned laboratory with 20–22°C temperature and 40–60% humidity, and 100 m ASL provided the same conditions for all BC and CPET.

Each CPET began with a 5 min personalised warm-up (walk or easy jog with ‘conversational’ intensity for running, easy pedalling with ‘conversational’ intensity for cycling). Then after the preparation (about 5 min), the continuous progressive step test was conducted. Due to the population diversity (training status), the running test speed started from 7 to 12 km·hr–1 with a 1% treadmill incline. The choice of initial starting speed was determined by the interview and sports results achieved. For example, those running less than 60 min at a distance of 10 km started the test at 7 km/hr, while those running 10 km for less than 35 min started the test at an initial speed of 12 km/hr. The pace increased by 1 km·hr–1 every 2 min with no change in incline. The cycling test began at 60–150 W, depending on the athletes training status. The power increased by 20–30 W every 2 min. It was recommended to maintain a constant cadence of 80–90 (repetition·min–1) during the test. The tests were terminated due to exhaustion: volitional inability to continue the activity or/and VO2 and HR plateau with increasing load or/and observed disturbance of coordination in running or/and inability to maintain the set cadence. Due to the graded protocol used, the cycling power and running speed values have been calculated as a function of time to better reflect the actual level for the test moment being determined (Kuipers et al., 1985). Before the test, after every step, and 3 min after the termination of the effort technician took a 20 µL blood sample from a fingertip. Samples were collected during the test without interrupting the effort. The samples were taken from the initial puncture. The first blood drop was collected into the swab and the second blood drop was drawn for further analysis into the capillary. VO2max was recorded as the highest value (15 s intervals) before the termination of the test. HRmax was recorded as the highest value obtained at the end of the test, without averaging.

The anaerobic threshold (AT) was established with the following criteria: (1) common start of VE/VO2 and VE/VCO2 curves, (2) end-tidal partial pressure of oxygen raised constantly with the end-tidal partial pressure of carbon dioxide (Beaver et al., 1986). The was established with the following criteria: (1) PetCO2 must decrease after reaching maximal amount, (2) the presence of fast nonlinear growth in VE (second deflection), (3) the VE/VCO2 ratio achieved minimum and started to rise, and (4) a nonlinear increase in VCO2 versus VO2 (lack of linearity) (Beaver et al., 1986). The [La-]b was estimated for AT and RCP in relation to power or speed (Wiecha et al., 2022).

### Data analysis

Our comprehensive ML approach enables the evaluation of each formula by preliminary variables precision (at the stage of selection), then accuracy (during the model’s building) and recall (in internal validation).

Individual CPET results were saved into the Excel file (Microsoft Corporation, Redmond, WA, USA) and a custom-made script was used to generate the database in Excel (Python programming). Further, mean, SD, and 95% confidence intervals (CI) were calculated. The normality of the distribution of the data was examined using the Shapiro-Wilk test and intergroup differences were calculated using the Student’s t-test for independent variables.

Three-step variable selection procedures based on random forests were applied using the R package VSURF in RStudio software (R Core Team, Vienna, Austria; version 3.6.4) (Genuer et al., 2016). For each level of measurement (AT, RCP) and their combination (AT+RCP), significant variables were identified separately. The first step was dedicated to eliminate irrelevant variables from the dataset. Second step aimed to select all variables related to the response for interpretation purposes. The third step refined the selection by eliminating redundancy in the set of variables selected by the second step, for prediction purposes (Genuer et al., 2017). Each time for variables selection, the anthropometric variables as in Tables 1–2 and the CPET parameters given in Tables 3–4 from a specific level of measurement (AT; RCP) and their combinations were visible.

**Table 1.**
 Basic anthropometric characteristics for runners.


<table>
  <thead>
    <tr>
      <th rowspan="2">Variable (unit)</th>
      <th colspan="3">Derivation group n=1998</th>
      <th colspan="3">Testing group n=666</th>
      <th colspan="3">Validation group n=666</th>
    </tr>
    <tr>
      <th>Mean</th>
      <th>CI</th>
      <th>SD</th>
      <th>Mean</th>
      <th>CI</th>
      <th>SD</th>
      <th>Mean</th>
      <th>CI</th>
      <th>SD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Age (years)</td>
      <td>36.2</td>
      <td>35.6–36.9</td>
      <td>8.45</td>
      <td>35.9</td>
      <td>35.5–36.3</td>
      <td>8.05</td>
      <td>35.5</td>
      <td>34.9–36.2</td>
      <td>8.14</td>
    </tr>
    <tr>
      <td>Height (cm)</td>
      <td>180.0</td>
      <td>179.6–180.5</td>
      <td>6.04</td>
      <td>179.4</td>
      <td>179.1–179.7</td>
      <td>6.13</td>
      <td>179.7</td>
      <td>179.2–180.2</td>
      <td>6.61</td>
    </tr>
    <tr>
      <td>BM (kg)</td>
      <td>77.7</td>
      <td>77.0–78.4</td>
      <td>9.35</td>
      <td>77.7</td>
      <td>77.3–78.1</td>
      <td>9.29</td>
      <td>77.9</td>
      <td>77.1–78.6</td>
      <td>10.1</td>
    </tr>
    <tr>
      <td>BMI (kg·m–2)</td>
      <td>23.9</td>
      <td>23.8–24.1</td>
      <td>2.43</td>
      <td>24.1</td>
      <td>24.0–24.2</td>
      <td>2.41</td>
      <td>24.1</td>
      <td>23.9–24.3</td>
      <td>2.56</td>
    </tr>
    <tr>
      <td>BF (%)</td>
      <td>15.4</td>
      <td>15.1–15.7</td>
      <td>4.55</td>
      <td>15.5</td>
      <td>15.3–15.7</td>
      <td>4.52</td>
      <td>15.4</td>
      <td>15.1–15.8</td>
      <td>4.55</td>
    </tr>
    <tr>
      <td>FM (kg)</td>
      <td>12.2</td>
      <td>11.9–12.6</td>
      <td>4.68</td>
      <td>12.3</td>
      <td>12.1–12.5</td>
      <td>4.65</td>
      <td>12.3</td>
      <td>11.9–12.7</td>
      <td>4.92</td>
    </tr>
    <tr>
      <td>FFM (kg)</td>
      <td>65.5</td>
      <td>65.0–66.0</td>
      <td>6.43</td>
      <td>65.4</td>
      <td>65.1–65.7</td>
      <td>6.31</td>
      <td>65.6</td>
      <td>65.1–66.1</td>
      <td>6.86</td>
    </tr>
  </tbody>
</table>

_BM, body mass; BMI, body mass index; BF, body fat; FM, fat mass; FFM, fat-free mass; CI, 95% confidence interval; SD, standard deviation._

**Table 2.**
 Basic anthropometric characteristics for cyclists.


<table>
  <thead>
    <tr>
      <th rowspan="2">Variable (unit)</th>
      <th colspan="3">Derivation group n=656</th>
      <th colspan="3">Testing group n=219</th>
      <th colspan="3">Validation group n=219</th>
    </tr>
    <tr>
      <th>Mean</th>
      <th>CI</th>
      <th>SD</th>
      <th>Mean</th>
      <th>CI</th>
      <th>SD</th>
      <th>Mean</th>
      <th>CI</th>
      <th>SD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Age (years)</td>
      <td>37.3</td>
      <td>36.6–38.0</td>
      <td>9.13</td>
      <td>37.1</td>
      <td>35.9–38.4</td>
      <td>9.50</td>
      <td>37.6</td>
      <td>36.5–38.8</td>
      <td>8.46</td>
    </tr>
    <tr>
      <td>Height (cm)</td>
      <td>179.9</td>
      <td>179.4–180.4</td>
      <td>6.27</td>
      <td>180.1</td>
      <td>179.2–181.0</td>
      <td>6.96</td>
      <td>180.2</td>
      <td>179.4–181.0</td>
      <td>6.13</td>
    </tr>
    <tr>
      <td>BM (kg)</td>
      <td>78.8</td>
      <td>78.1–79.6</td>
      <td>9.80</td>
      <td>79.1</td>
      <td>77.7–80.5</td>
      <td>10.4</td>
      <td>79.8</td>
      <td>78.4–81.3</td>
      <td>10.9</td>
    </tr>
    <tr>
      <td>BMI (kg·m–2)</td>
      <td>24.3</td>
      <td>24.1–24.6</td>
      <td>2.63</td>
      <td>24.4</td>
      <td>24.0–24.7</td>
      <td>2.80</td>
      <td>24.6</td>
      <td>24.2–25.0</td>
      <td>2.96</td>
    </tr>
    <tr>
      <td>BF (%)</td>
      <td>16.4</td>
      <td>15.7–17.1</td>
      <td>4.99</td>
      <td>16.1</td>
      <td>15.7–16.5</td>
      <td>4.81</td>
      <td>16.2</td>
      <td>15.5–16.8</td>
      <td>4.87</td>
    </tr>
    <tr>
      <td>FM (kg)</td>
      <td>13.3</td>
      <td>12.6–14.1</td>
      <td>5.66</td>
      <td>13.0</td>
      <td>12.6–13.4</td>
      <td>5.27</td>
      <td>13.3</td>
      <td>12.5–14.0</td>
      <td>5.85</td>
    </tr>
    <tr>
      <td>FFM (kg)</td>
      <td>65.8</td>
      <td>64.9–66.6</td>
      <td>6.25</td>
      <td>65.8</td>
      <td>65.4–66.3</td>
      <td>6.06</td>
      <td>66.6</td>
      <td>65.7–67.4</td>
      <td>6.58</td>
    </tr>
  </tbody>
</table>

_BM, body mass; BMI, body mass index; BF, body fat; FM, fat mass; FFM, fat-free mass; CI, 95% confidence interval; SD, standard deviation._

**Table 3.**
 Cardiopulmonary exercise testing (CPET) characteristics for runners.


<table>
  <thead>
    <tr>
      <th rowspan="2">Variable (unit)</th>
      <th colspan="3">Derivation group n=1998</th>
      <th colspan="3">Testing group n=666</th>
      <th colspan="3">Validation group n=666</th>
    </tr>
    <tr>
      <th>Mean</th>
      <th>CI</th>
      <th>SD</th>
      <th>Mean</th>
      <th>CI</th>
      <th>SD</th>
      <th>Mean</th>
      <th>CI</th>
      <th>SD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>rVO2AT (mL·min–1·kg–1)</td>
      <td>38.4</td>
      <td>38.1–38.8</td>
      <td>5.01</td>
      <td>38.5</td>
      <td>38.3–38.7</td>
      <td>4.88</td>
      <td>38.1</td>
      <td>37.7–38.5</td>
      <td>5.16</td>
    </tr>
    <tr>
      <td>RERAT</td>
      <td>0.87</td>
      <td>0.86–0.87</td>
      <td>0.04</td>
      <td>0.87</td>
      <td>0.86–0.87</td>
      <td>0.04</td>
      <td>0.87</td>
      <td>0.86–0.87</td>
      <td>0.04</td>
    </tr>
    <tr>
      <td>HRAT (beats·min–1)</td>
      <td>151.5</td>
      <td>150.8–152.3</td>
      <td>10.3</td>
      <td>151.0</td>
      <td>150.6–151.5</td>
      <td>10.8</td>
      <td>152.0</td>
      <td>151.2–152.8</td>
      <td>10.8</td>
    </tr>
    <tr>
      <td>VEAT (L·min–1)</td>
      <td>79.1</td>
      <td>78.1–80.0</td>
      <td>12.2</td>
      <td>78.3</td>
      <td>77.8–78.9</td>
      <td>12.0</td>
      <td>77.2</td>
      <td>76.3–78.2</td>
      <td>12.0</td>
    </tr>
    <tr>
      <td>SPEEDAT (km·h–1)</td>
      <td>11.0</td>
      <td>10.9–11.1</td>
      <td>1.45</td>
      <td>11.0</td>
      <td>11.0–11.1</td>
      <td>1.36</td>
      <td>10.9</td>
      <td>10.8–11.0</td>
      <td>1.42</td>
    </tr>
    <tr>
      <td>LAAT (mmol·L–1)</td>
      <td>2.08</td>
      <td>2.02–2.14</td>
      <td>0.63</td>
      <td>1.80</td>
      <td>1.76–1.83</td>
      <td>0.62</td>
      <td>2.35</td>
      <td>2.27–2.42</td>
      <td>0.72</td>
    </tr>
    <tr>
      <td>rVO2RCP (mL·min–1·kg–1)</td>
      <td>47.5</td>
      <td>47.0–48.0</td>
      <td>5.88</td>
      <td>47.7</td>
      <td>47.4–48.0</td>
      <td>6.15</td>
      <td>47.3</td>
      <td>46.8–47.8</td>
      <td>6.16</td>
    </tr>
    <tr>
      <td>RERRCP</td>
      <td>1.00</td>
      <td>1.00–1.00</td>
      <td>0.04</td>
      <td>1.00</td>
      <td>1.00–1.00</td>
      <td>0.04</td>
      <td>1.00</td>
      <td>1.00–1.00</td>
      <td>0.03</td>
    </tr>
    <tr>
      <td>HRRCP (beats·min–1)</td>
      <td>173.4</td>
      <td>172.7–174.1</td>
      <td>9.21</td>
      <td>173.2</td>
      <td>172.8–173.6</td>
      <td>9.30</td>
      <td>174.3</td>
      <td>173.5–175.0</td>
      <td>9.50</td>
    </tr>
    <tr>
      <td>VERCP (L·min–1)</td>
      <td>114.7</td>
      <td>113.5–116.0</td>
      <td>15.9</td>
      <td>113.9</td>
      <td>113.1–114.6</td>
      <td>16.7</td>
      <td>112.7</td>
      <td>111.4–114.0</td>
      <td>16.2</td>
    </tr>
    <tr>
      <td>SPEEDRCP (km·h–1)</td>
      <td>14.0</td>
      <td>13.9–14.1</td>
      <td>1.77</td>
      <td>14.1</td>
      <td>14.0–14.1</td>
      <td>1.70</td>
      <td>13.9</td>
      <td>13.8–14.1</td>
      <td>1.75</td>
    </tr>
    <tr>
      <td>LARCP (mmol·L–1)</td>
      <td>4.72</td>
      <td>4.63–4.82</td>
      <td>1.04</td>
      <td>4.40</td>
      <td>4.34–4.45</td>
      <td>1.04</td>
      <td>4.81</td>
      <td>4.69–4.93</td>
      <td>1.14</td>
    </tr>
    <tr>
      <td>rVO2max (mL·min–1·kg–1)</td>
      <td>53.8</td>
      <td>53.3–54.3</td>
      <td>6.67</td>
      <td>54.3</td>
      <td>54.0–54.6</td>
      <td>6.95</td>
      <td>53.8</td>
      <td>53.3–54.3</td>
      <td>7.09</td>
    </tr>
  </tbody>
</table>

_CI, 95% confidence interval; SD, standard deviation; rVO2AT, oxygen uptake at anaerobic threshold relative to body mass; RERAT, respiratory exchange ratio at anaerobic threshold; HRAT, heart rate at anaerobic threshold; VEAT, pulmonary ventilation at anaerobic threshold; SPEEDAT, velocity at anaerobic threshold; LAAT, blood lactate concentration at anaerobic threshold; rVO2RCP, oxygen uptake at respiratory compensation point relative to body mass; RERRCP, respiratory exchange ratio at respiratory compensation point; HRRCP, heart rate at respiratory compensation point; VERCP, pulmonary ventilation at respiratory compensation point; SPEEDRCP, velocity at respiratory compensation point; LARCP, blood lactate concentration at respiratory compensation point; rVO2max, maximal oxygen uptake relative to body mass._

**Table 4.**
 Cardiopulmonary exercise testing (CPET) characteristics for cyclists.


<table>
  <thead>
    <tr>
      <th rowspan="2">Variable (unit)</th>
      <th colspan="3">Derivation group n=656</th>
      <th colspan="3">Testing group n=219</th>
      <th colspan="3">Validation group n=219</th>
    </tr>
    <tr>
      <th>Mean</th>
      <th>CI</th>
      <th>SD</th>
      <th>Mean</th>
      <th>CI</th>
      <th>SD</th>
      <th>Mean</th>
      <th>CI</th>
      <th>SD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>rVO2AT (mL·min–1·kg–1)</td>
      <td>33.0</td>
      <td>32.5–33.4</td>
      <td>5.84</td>
      <td>33.2</td>
      <td>32.4–33.9</td>
      <td>5.68</td>
      <td>33.7</td>
      <td>32.9–34.5</td>
      <td>5.89</td>
    </tr>
    <tr>
      <td>RERAT</td>
      <td>0.87</td>
      <td>0.87–0.87</td>
      <td>0.04</td>
      <td>0.87</td>
      <td>0.87–0.88</td>
      <td>0.04</td>
      <td>0.87</td>
      <td>0.87–0.88</td>
      <td>0.04</td>
    </tr>
    <tr>
      <td>HRAT (beats·min–1)</td>
      <td>142.2</td>
      <td>141.3–143.1</td>
      <td>11.7</td>
      <td>140.7</td>
      <td>139.1–142.3</td>
      <td>11.8</td>
      <td>141.2</td>
      <td>139.7–142.6</td>
      <td>10.8</td>
    </tr>
    <tr>
      <td>VEAT (L·min–1)</td>
      <td>64.9</td>
      <td>64.0–65.7</td>
      <td>11.0</td>
      <td>65.1</td>
      <td>63.7–66.5</td>
      <td>10.6</td>
      <td>67.4</td>
      <td>66.0–68.9</td>
      <td>11.2</td>
    </tr>
    <tr>
      <td>rPOWAT (W·kg–1)</td>
      <td>2.28</td>
      <td>2.24–2.32</td>
      <td>0.48</td>
      <td>2.27</td>
      <td>2.21–2.34</td>
      <td>0.48</td>
      <td>2.33</td>
      <td>2.27–2.39</td>
      <td>0.46</td>
    </tr>
    <tr>
      <td>LAAT (mmol·L–1)</td>
      <td>1.86</td>
      <td>1.82–1.90</td>
      <td>0.51</td>
      <td>1.84</td>
      <td>1.77–1.90</td>
      <td>0.50</td>
      <td>1.80</td>
      <td>1.74–1.87</td>
      <td>0.51</td>
    </tr>
    <tr>
      <td>rVO2RCP (mL·min–1·kg–1)</td>
      <td>44.0</td>
      <td>43.5–44.6</td>
      <td>7.38</td>
      <td>44.4</td>
      <td>43.4–45.4</td>
      <td>7.32</td>
      <td>44.9</td>
      <td>43.8–45.9</td>
      <td>7.63</td>
    </tr>
    <tr>
      <td>RERRCP</td>
      <td>1.01</td>
      <td>1.01–1.01</td>
      <td>0.04</td>
      <td>1.01</td>
      <td>1.01–1.02</td>
      <td>0.04</td>
      <td>1.01</td>
      <td>1.01–1.02</td>
      <td>0.04</td>
    </tr>
    <tr>
      <td>HRRCP (beats·min–1)</td>
      <td>168.8</td>
      <td>168.0–169.7</td>
      <td>10.5</td>
      <td>167.7</td>
      <td>166.2–169.2</td>
      <td>11.3</td>
      <td>168.4</td>
      <td>167.1–169.6</td>
      <td>9.11</td>
    </tr>
    <tr>
      <td>VERCP (L·min–1)</td>
      <td>106.2</td>
      <td>104.8–107.6</td>
      <td>17.7</td>
      <td>107.6</td>
      <td>105.3–109.8</td>
      <td>16.8</td>
      <td>110.4</td>
      <td>107.9–112.9</td>
      <td>18.7</td>
    </tr>
    <tr>
      <td>rPOWRCP (W·kg–1)</td>
      <td>3.34</td>
      <td>3.29–3.38</td>
      <td>0.63</td>
      <td>3.33</td>
      <td>3.25–3.42</td>
      <td>0.63</td>
      <td>3.40</td>
      <td>3.32–3.48</td>
      <td>0.61</td>
    </tr>
    <tr>
      <td>LARCP (mmol·L–1)</td>
      <td>4.54</td>
      <td>4.47–4.61</td>
      <td>0.97</td>
      <td>4.61</td>
      <td>4.48–4.75</td>
      <td>1.04</td>
      <td>4.47</td>
      <td>4.34–4.61</td>
      <td>1.03</td>
    </tr>
    <tr>
      <td>rVO2MAX (mL·min–1·kg–1)</td>
      <td>51.7</td>
      <td>51.1–52.4</td>
      <td>7.99</td>
      <td>52.0</td>
      <td>50.9–53.1</td>
      <td>8.01</td>
      <td>52.3</td>
      <td>51.2–53.4</td>
      <td>8.08</td>
    </tr>
  </tbody>
</table>

_CI, 95% confidence interval; SD, standard deviation; rVO2AT, oxygen uptake at anaerobic threshold relative to body mass; RERAT, respiratory exchange ratio at anaerobic threshold; HRAT, heart rate at anaerobic threshold; VEAT, pulmonary ventilation at anaerobic threshold; rPOWAT, power at anaerobic threshold relative to body mass; LAAT, blood lactate concentration at anaerobic threshold; rVO2RCP, oxygen uptake at respiratory compensation point relative to body mass; RERRCP, respiratory exchange ratio at respiratory compensation point; HRRCP, heart rate at respiratory compensation point; VERCP, pulmonary ventilation at respiratory compensation point; LARCP, blood lactate concentration at respiratory compensation point; rPOWRCP, power at respiratory compensation point relative to body mass; rVO2max, maximal oxygen uptake relative to body mass._

After selection variables were included in the further analysis, only selected parameters were put into multiple linear regression (MLR) modelling. The data for MLR model building were randomly distributed into sets, that is derivation, testing, validation representing 60%, 20%, and 20% of the cases, respectively. As a result, only significant predictors (with p<0.05) were included in the final models. Derived equations are characterised by the coefficient of determination (R2), root mean square error (RMSE), and mean absolute error (MAE). Bland-Altman plots analysis was used to establish the model’s precision and accuracy during validation (Altman and Bland, 1983). Other implemented tests to reach the complete fulfilment of MLR modelling requirements included Ramsey’s RESET test (for the correctness of specificity in MLR equations), Chow test (for stability assessment between different coefficients), and Durbin-Watson test (for autocorrelation of residuals). Each model was examined under the above-mentioned requirements and any irregularities have not been noted.

Ggplot 2 package in RStudio (R Core Team, Vienna, Austria; version 3.6.4), GraphPad Prism (GraphPad Software; San Diego, CA, USA; version 9.0.0 for Mac OS), and STATA software (StataCorp, College Station, TX, USA; version 15.1) were used in statistical analysis. A two-sided p-value <0.05 was considered as the significance borderline.

## Results

### Somatic measurements and CPET results

Anthropometric data of the runners models for derivation, testing, and validation groups are presented in Table 1, while cyclists are in Table 2. The runners groups consisted of 1998, 666, and 666 men for derivation, testing, and validation groups, respectively. In turn, the cyclists groups included 656, 219, and 219 men, respectively. Significant differences (p<0.05) between derivation cohorts of runners and cyclists were in BMI and age, between testing cohorts in all baseline parameters, whereas between validation cohorts only in BMI.

CPET results for runners models are presented in Table 3 and for cyclists in Table 4. Runners in the derivation cohort achieved relative to body mass VO2max (rVO2max) of 53.8±6.67 mL·min–1·kg–1 (95% CI: 53.3–54.3), in testing group 54.3±6.95 mL·min–1·kg–1 (95% CI: 54.0–54.6), and in validation group 53.8±7.09 mL·min–1·kg–1 (95% CI: 53.3–54.3). In cyclists groups mean rVO2max was 51.7±7.99 mL·min–1·kg–1 (95% CI: 51.1–52.4), 52.0±8.01 mL·min–1·kg–1 (95% CI: 50.9–53.1), and 52.3±8.08 mL·min–1·kg–1 (95% CI: 51.2–53.4) for derivation, testing, and validation cohorts, respectively. Relative to body mass oxygen uptake at anaerobic threshold (rVO2AT) in runners groups accounted for 71.6 ± 5.10% (95% CI: 71.2–71.9), 71.1 ± 4.91% (95% CI: 70.9–71.3), and 71.0 ± 5.42% (95% CI: 70.6–71.5) of rVO2max in derivation, testing, and validation cohorts, respectively. In cyclists, it was 63.7 ± 5.20% (95% CI: 63.3–64.1%), 63.8 ± 5.00% (95% CI: 63.1–64.4), and 64.4 ± 4.73% (95% CI: 63.8–65.0) of rVO2max, respectively. In turn, relative to body mass oxygen uptake at respiratory compensation point (rVO2RCP) in runners accounted for 87.8 ± 3.23% (95% CI: 87.5–88.0), 87.6 ± 3.60% (95% CI: 87.4–87.8), and 87.7 ± 3.35% (87.4–88.0) of rVO2max for derivation, testing, and validation cohorts, respectively, while in cyclists for 85.0 ± 4.18% (95% CI: 84.7–85.4), 85.4 ± 4.09% (95% CI: 84.8–85.9), and 85.7 ± 4.14% (95% CI: 85.1–86.2) of rVO2max, respectively. There were no significant differences in threshold-to-maximum percentages values between derivation, testing, and validation cohorts among the runners and cyclists groups, whereas variations between runners and cyclists threshold-to-maximum results were all significant (p<0.05).

### Prediction models based on AT and RCP

Full forms of MLR prediction models for cyclists are demonstrated in Table 5, whereas for runners in Table 6. The models prediction performance is presented as R2 along with RMSE and MAE. Briefly, R2 ranged for cyclists equations from 0.43 for somatic parameters (SOM) equation to 0.913 for RCP equations. For runners formulae, R2 ranged from 0.35 for SOM equation to 0.899 for AT and AT+RCP equations. Obtained RMSE for cyclists models was the lowest for RCP equations (=2.03) and the highest for SOM equation (=6.11). For runners, RMSE ranged from 2.0 for AT and AT+RCP equations to 5.54 for SOM equation. Similarly, observed MAE for cyclists was the lowest for RCP equation (=1.64 mL·min–1·kg–1) in the validation group and the highest for SOM equation (=4.74 mL·min–1·kg–1), while in runners the lowest for AT and AT+RCP equations (=1.58 mL·min–1·kg–1) and the highest for SOM equation (=4.37 mL·min–1·kg–1). The performance of prediction equations is demonstrated in Figure 2.

![Figure 2.](https://cdn.elifesciences.org/articles/86291/elife-86291-fig2-v2.jpg)

**Figure 2.:** Abbreviations: VO2max; maximal oxygen uptake; AT, anaerobic threshold; RCP, respiratory compensation point; Max, maximal; Som, somatic. All values are presented in mL·min–1·kg–1. Upper panel shows performance for running equations, while the lower panel shows performance for cycling equations. Panel A shows performance of the prediction model for AT; panel B for RCP; panel C for AT and RCP; panel D for somatic-only equation.

**Table 5.**
 VO2max prediction equations for cyclists.


<table>
  <thead>
    <tr>
      <th rowspan="2">Model’s category</th>
      <th rowspan="2">Multiple linear regression equation</th>
      <th rowspan="2">R2</th>
      <th colspan="2">Derivation group performance</th>
      <th colspan="2">Validation group performance</th>
    </tr>
    <tr>
      <th>RMSE</th>
      <th>MAE</th>
      <th>RMSE</th>
      <th>MAE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AT</td>
      <td>VO2max = 21.29 + 0.95 * rVO2AT + 1.74 * rPOWAT - 0.30 * BF</td>
      <td>0.811</td>
      <td>3.62</td>
      <td>2.89</td>
      <td>3.42</td>
      <td>2.72</td>
    </tr>
    <tr>
      <td>RCP</td>
      <td>VO2max = 8.57 + 1.08 * rVO2RCP - 0.04 * VERCP</td>
      <td>0.913</td>
      <td>2.12</td>
      <td>1.66</td>
      <td>2.03</td>
      <td>1.64</td>
    </tr>
    <tr>
      <td>AT+RCP</td>
      <td>VO2max = 10.57 + 0.98 * rVO2RCP - 0.12 * BF</td>
      <td>0.909</td>
      <td>2.26</td>
      <td>1.78</td>
      <td>2.11</td>
      <td>1.72</td>
    </tr>
    <tr>
      <td>SOM</td>
      <td>VO2max = 82.36–0.14 * BM - 0.66 * BF - 0.22 * Age</td>
      <td>0.43</td>
      <td>6.06</td>
      <td>4.70</td>
      <td>6.11</td>
      <td>4.74</td>
    </tr>
  </tbody>
</table>

_AT, equation based on anaerobic threshold; RCP, equation based on respiratory compensation point; SOM, equation based on somatic variables only; R2, adjusted R2; RMSE, root mean square error; MAE, mean absolute error (mL·min–1·kg–1); VO2max, maximal oxygen uptake relative to body mass (mL·min–1·kg–1); rVO2AT, oxygen uptake at anaerobic threshold relative to body mass (mL·min–1·kg–1); rPOWAT, power at anaerobic threshold relative to body mass (W·kg–1); rVO2RCP, oxygen uptake at respiratory compensation point relative to body mass (mL·min–1·kg–1); VERCP, pulmonary ventilation at respiratory compensation point (L·min–1); BF, body fat (%); BM, body mass (kg)._

**Table 6.**
 VO2max prediction equations for runners.


<table>
  <thead>
    <tr>
      <th rowspan="2">Model’s category</th>
      <th rowspan="2">Multiple linear regression equation</th>
      <th rowspan="2">R2</th>
      <th colspan="2">Derivation group performance</th>
      <th colspan="2">Validation group performance</th>
    </tr>
    <tr>
      <th>RMSE</th>
      <th>MAE</th>
      <th>RMSE</th>
      <th>MAE</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AT</td>
      <td>VO2max = 19.78 + 1.05 * rVO2AT + 0.94 * SPEEDAT - 0.12 * FFM - 0.06 * VEAT - 0.07 * HRAT</td>
      <td>0.775</td>
      <td>3.43</td>
      <td>2.61</td>
      <td>3.60</td>
      <td>2.74</td>
    </tr>
    <tr>
      <td>RCP</td>
      <td>VO2max = 1.98 + 1.03 * rVO2RCP + 0.23 * SPEEDRCP</td>
      <td>0.899</td>
      <td>2.0</td>
      <td>1.58</td>
      <td>2.08</td>
      <td>1.60</td>
    </tr>
    <tr>
      <td>AT+RCP</td>
      <td>VO2max = 1.98 + 1.03 * rVO2RCP + 0.23 * SPEEDRCP</td>
      <td>0.899</td>
      <td>2.0</td>
      <td>1.58</td>
      <td>2.08</td>
      <td>1.60</td>
    </tr>
    <tr>
      <td>SOM</td>
      <td>VO2max = 72.37–0.77 * BF - 0.19 * Age</td>
      <td>0.35</td>
      <td>5.53</td>
      <td>4.36</td>
      <td>5.54</td>
      <td>4.37</td>
    </tr>
  </tbody>
</table>

_AT, equation based on anaerobic threshold; RCP, equation based on respiratory compensation point; SOM, equation based on somatic variables only; R2, adjusted R2; RMSE, root mean square error; MAE, mean absolute error (mL·min–1·kg–1); VO2max, maximal oxygen uptake relative to body mass (mL·min–1·kg–1); rVO2AT, oxygen uptake at anaerobic threshold relative to body mass (mL·min–1·kg–1); SPEEDAT, velocity at anaerobic threshold (km·h–1); FFM, fat free mass (kg); VEAT, pulmonary ventilation at anaerobic threshold (L·min–1); HRAT, heart rate at anaerobic threshold (beats·min–1); BF, body fat (%); rVO2RCP, oxygen uptake at respiratory compensation point relative to body mass (mL·min–1·kg–1); SPEEDRCP, velocity at respiratory compensation point (km·h–1)._

### Models validation

Evaluation of each model for cyclists is presented in Table 5, while for runners in Table 6. In summary, the performance of our prediction equations was similar to that observed in the derivation cohort. A minorly higher RMSE and MAE were noted. Overall, RMSE values in cyclists are located between 2.03 and 6.11, whereas in runners between 2.0 and 5.54. MAE ranged from 1.64 to 4.74 mL·min–1·kg–1 in cyclists models and 1.58 to 4.37 mL·min–1·kg–1 in runners. The most accurate prediction was obtained in cyclists (defined as the highest replicability and the lowest risk of inaccuracies in the test set) by RCP equations (R2=0.913, RMSE=2.03, MAE=1.64). Interestingly, the models which worked the most accurately and the less precisely were the same in the derivation and validation. Figure 3 illustrates the Bland-Altman plots with a comparison of observed vs predicted VO2max using newly derived prediction models at the stage of validation.

![Figure 3.](https://cdn.elifesciences.org/articles/86291/elife-86291-fig3-v2.jpg)

**Figure 3.:** Abbreviations: VO2max; maximal oxygen uptake; AT, anaerobic threshold; RCP, respiratory compensation point; Max, maximal; Som, somatic. All values are presented in mL·min–1·kg–1. Upper panel shows performance for running equations, while the lower panel shows performance for cycling equations. Panel A shows performance of the prediction model for AT; panel B for RCP; panel C for AT and RCP; panel D for the somatic-only equation.

## Discussion

In the present study, we derived and internally validated novel advanced and accurate prediction models for VO2max. The main findings are as follows: (1) we can precisely predict VO2max based on submaximal CPET parameters, (2) inclusion of cardiopulmonary and BC variables enriches their prediction performance, (3) based only on somatic parameters, weak-to-low VO2max assessment is currently possible, (4) derived equations showed high transferability abilities during validation. Our findings indicate that prediction models based on AT and RCP variables allow for accurate VO2max calculation. Equations based on somatic variables allow for limited precision.

The main advantage of our research is the unified CPET protocol conducted on a wide cohort of endurance athletes with different levels of fitness. This approach enables the comprehensive evaluation of the most important predictors which were further applied to build prediction equations. In the current literature, prediction models for sports and performance diagnostics are mostly derived from narrow and specified athletic cohorts which limit their applicability to broader populations (Paap and Takken, 2014). Moreover, the advantage of the presented research was the fact that regression equations for the treadmill and cycle ergometer were derived based on the most commonly used machines and forms of activity or movement in the laboratory stress exercise tests.

An important issue addressed in publications on various attempts to estimate VO2max is the question of their usefulness in assessing changes in endurance over a training cycle (Klusiewicz et al., 2016). As reported by Klusiewicz et al., the suitability of the two indirect methods of assessing VO2max was statistically confirmed, their usefulness for estimating changes in the endurance of the trained individuals during the training cycle was rather low (Klusiewicz et al., 2016). The standard estimation error of these methods (ranged between 4.2% and 7.7% in the female and 5.1% and 7.4% in the male) was higher than the real differences in the VO2max values determined in the direct measurements (between the first and the second examination the VO2max rose by 3.0% in the female athletes and dropped by 4.3% in the male athletes) (Klusiewicz et al., 2016). Popularly used wearables provided substantial accuracy on population level when considered devices with exercise-based algorithms (Molina-Garcia et al., 2022). However, VO2max predictions on the individual’s level still need improvement in the context of both sports and clinical settings (Molina-Garcia et al., 2022).

In the Astrand-Ryhming method, a widely used VO2max prediction method for almost 70 years, in several papers published so far, the correlation coefficients of the measured values to the predicted values ranged from 0.63 to 0.85. Standard estimated error values (in L·min–1) generally exceeded 0.5 (Grant et al., 1995; Legge and Banister, 1986). In our study, the highest R2 was 0.913 and the lowest was 0.775. As an additional advantage, we propose an equation based only on somatic variables, which showed a low R2 - 0.35 for runners and 0.43 for cyclists. Although, it still presents that our models are more accurate than those widely described in the literature so far (Paap and Takken, 2014; Wiecha et al., 2023).

As VO2 is an exercise parameter that combines the function of the respiratory, circulatory, and muscular systems, the use of only somatic variables such as body fat, weight, or age was not sufficient for optimal prediction (Bassett and Howley, 2000). It is worth underlining that the main factors contributing to VO2max were submaximal variables VO2AT and VO2RCP, as well as running speed for runners and pedalling power for cyclists (Billat and Koralsztein, 1996). Thus, VO2 is a universal and interchangeable measurement of endurance (Albouaini et al., 2007). Our results suggest that VO2 is an indicator of both endurance and critical vital signs (Blair et al., 1989; Kaminsky et al., 2015). It is also in line with current standings as Kaminsky et al. and Blair et al. postulate that the higher the VO2max, the fitter the individual is (Kaminsky et al., 2015), and the lower its all-cause mortality (Blair et al., 1989).

In sports medicine and exercise physiology, evaluation of the body’s functional performance remains crucial (Sartor et al., 2013). Our results indicate that VO2max was possible to accurately predict based only on submaximal parameters (without the inclusion of maximal ones), which is reflected in R2 (Wiecha et al., 2022). This confirms that submaximal CPET is a valuable tool in assessing fitness levels. Thus, submaximal exercise testing appears to be more applicable by physicians and fitness professionals in their role as clinical exercise specialists (Noonan and Dean, 2000). For individuals who have a moderate to high possibility of cardiovascular diseases, exerting themselves up to their maximum abilities increases risk of adverse outcomes (Guazzi et al., 2012; Noonan and Dean, 2000). There are numerous possibilities to use results of submaximal CPET. Currently, pseudo-random binary sequencing appears as one of the feasible approaches. Its enables assessment of cardiorespiratory kinetics within the selected workload ranges (Hoffmann et al., 2022; Koschate et al., 2016). This is important as CPET until refusal is often impossible to conduct or highly dangerous (Guazzi et al., 2016). Such situations appear mainly in clinical cardiovascular conditions, such as heart failure, dyspnea of unknown aetiology, or risk evaluation for providing treatment protocol (Guazzi et al., 2016). Furthermore, previous studies have described that submaximal variables are significant predictors for performance measurements, as pointed out by Snowden et al., 2010, and Albouaini et al., 2007. In conclusion, ensuring high repeatability through submaximal prediction methods is crucial for monitoring endurance changes in both sports and medical diagnostics (Mann et al., 2013; Noonan and Dean, 2000).

It is worth mentioning the effect of body fat percentage on VO2max. This variable has been included in the majority of our models. With the increase in body fat percentage, VO2 decreased, and this relationship was particularly important in the somatic equation and is previously described in the literature (Shete et al., 2014). This is due to the fact that a higher level of adipose tissue and general body mass have both a negative impact on the results during long-term endurance sports (i.e. running and cycling) and with increasing fitness levels, the level of participant fatness decreases (Schwartz et al., 1991).

Results of internal validation show that our prediction models allow for an accurate assessment of VO2max. The observed RMSE and MAE values are significantly lower than in the validation of other prediction models on endurance athletes’ cohorts. Petek et al., 2022, and Malek et al., 2004, while validating the majority of widely used prediction models, observed MAE and RMSE on the level of 7–9 mL·kg–1·min–1. Our highest value of error for the somatic equation was in the cycling model (MAE; 4.74 mL·kg–1·min–1). Moreover, as we mentioned above, the somatic equation showed the lowest accuracy, and the remaining equations have RMSE between 1.94 and 6.11 and MAE in the range of 1.46–4.74 mL·kg–1·min–1.

Our study has some limitations. The applied exercise protocol may affect CPET results. There may be differences in performance measured in 2 min steps comparing to longer steps, but this should not significantly impact the participants’ exercise results. Additionally, longer constant intervals may increase accuracy in determining AT and RCP level, but have negligible impact on VO2max values (Muscat et al., 2015). The study, due to the insufficient number of women in the database to obtain reliable results, was restricted to men only. Therefore, the equations should be applied with more caution in women.

To summarise, our study has vast practical applications in the comprehensive assessment of an athlete’s training and is a valuable tool for coaches in the preparation of individualised training prescriptions (Mann et al., 2013). Targeting training regimens and diet to optimise the most important parameters contributing to the VO2max (i.e. VO2AT, VO2RCP, RER, body fat, etc.) will allow for achieving better results during the competition and they provide a useful indirect method for assessing changes in endurance during the training cycle (Mann et al., 2013). Various areas of application of prediction models have also been postulated in the literature so far, for example in submaximal and maximal efforts, or simulating the overcoming of the starting distance, or even at rest (Zhou et al., 1997). It is also worth mentioning their clinical implications in cardiology for the diagnosis of heart disease in athletes (where a reduction in VO2max may occur despite maintaining other parameters, e.g. RER) (Guazzi et al., 2016; Löllgen and Leyk, 2018).

### Conclusion

Briefly, we provided new prediction models for VO2max. The proposed method allows for precise prediction of VO2max based on submaximal results. Our equations were derived from a wide cohort of 6439 athletes with varied fitness levels which inflated the quality and transferability of the presented data. Higher accuracy was noted when applying submaximal predictors. Adding circulatory and respiratory variables enriches prediction performance. Body fat and fat-free mass had significant impacts on most of the VO2max prediction equations. The novel model based only on somatic parameters is presented. Derived equations showed high performance during internal validation and were fairly replicable. The inclusion of such a tool has practical usage for fitness professionals and personal coaches to prepare more precise training recommendations and establish competition pacing strategies.
