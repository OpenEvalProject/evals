# Revisiting the guidelines for ending isolation for COVID-19 patients

## Authors

- Yong Dam Jeong<sup>1</sup> ([ORCID: 0000-0002-3970-7690](https://orcid.org/0000-0002-3970-7690))
- Keisuke Ejima<sup>3</sup> ([ORCID: 0000-0002-1185-3987](https://orcid.org/0000-0002-1185-3987)) †
- Kwang Su Kim<sup>1</sup>
- Shoya Iwanami<sup>1</sup>
- Ana I Bento<sup>3</sup>
- Yasuhisa Fujita<sup>1</sup>
- Il Hyo Jung<sup>2</sup>
- Kazuyuki Aihara<sup>4</sup>
- Koichi Watashi<sup>5</sup>
- Taiga Miyazaki<sup>8</sup>
- Takaji Wakita<sup>5</sup>
- Shingo Iwami<sup>1</sup> ([ORCID: 0000-0002-1780-350X](https://orcid.org/0000-0002-1780-350X)) †
- Marco Ajelli<sup>3</sup>

### Affiliations

1. interdisciplinary Biology Laboratory (iBLab), Division of Biological Science, Graduate School of Science, Nagoya University Nagoya Japan
2. Department of Mathematics, Pusan National University Busan Republic of Korea
3. Department of Epidemiology and Biostatistics, Indiana University School of Public Health-Bloomington Bloomington United States
4. International Research Center for Neurointelligence, The University of Tokyo Tokyo Japan
5. Department of Virology II, National Institute of Infectious Diseases Tokyo Japan
6. Research Center for Drug and Vaccine Development, National Institute of Infectious Diseases Tokyo Japan
7. Department of Applied Biological Science, Tokyo University of Science Noda Japan
8. Department of Infectious Diseases, Nagasaki University Graduate School of Biomedical Sciences Nagasaki Japan
9. Division of Respirology, Rheumatology, Infectious Diseases, and Neurology, Department of Internal Medicine, Faculty of Medicine, University of Miyazaki Miyazaki Japan
10. Institute of Mathematics for Industry, Kyushu University Fukuoka Japan
11. Institute for the Advanced Study of Human Biology (ASHBi), Kyoto University Kyoto Japan
12. NEXT-Ganken Program, Japanese Foundation for Cancer Research (JFCR) Tokyo Japan
13. Science Groove Inc Fukuoka Japan
14. Laboratory for the Modeling of Biological and Socio-technical Systems, Northeastern University Boston United States

† Corresponding author

## Abstract

Since the start of the COVID-19 pandemic, two mainstream guidelines for defining when to end the isolation of SARS-CoV-2-infected individuals have been in use: the one-size-fits-all approach (i.e. patients are isolated for a fixed number of days) and the personalized approach (i.e. based on repeated testing of isolated patients). We use a mathematical framework to model within-host viral dynamics and test different criteria for ending isolation. By considering a fixed time of 10 days since symptom onset as the criterion for ending isolation, we estimated that the risk of releasing an individual who is still infectious is low (0–6.6%). However, this policy entails lengthy unnecessary isolations (4.8–8.3 days). In contrast, by using a personalized strategy, similar low risks can be reached with shorter prolonged isolations. The obtained findings provide a scientific rationale for policies on ending the isolation of SARS-CoV-2-infected individuals.

## Introduction

Since the first case of a novel coronavirus (SARS-CoV-2) was identified in China in December of 2019, its associated disease, COVID-19, spread quickly around the world, with the number of cases reaching 80 million by the end of 2020. During this time, nonpharmaceutical interventions (NPIs) were used on a massive scale to suppress or mitigate SARS-CoV-2 transmission (Cowling et al., 2020). As of January 2021, several countries had started vaccination campaigns aimed at controlling SARS-CoV-2 spread (Centers for Disease Control and Prevention, 2021). Still, until such vaccination programs reach a sizable fraction of the population, NPIs will likely continue to play a crucial role for epidemic control (Yang et al., 2021a).

A simple but effective NPI is the isolation of SARS-CoV-2-infected individuals. This can be done either in the infected person’s place of residence (as is the case for most Western countries [European Centre for Disease Prevention and Control, 2020b]) or in dedicated facilities (as is the case in China [Burki, 2020]). In both cases, a criterion for determining when to end the isolation phase is needed. Although a longer isolation period may decrease the chance of transmission, it also entails both a higher burden on the mental and physical health of the patient (Mian et al., 2021) and cause higher economic loss (Ash et al., 2021). Scientifically sound guidelines for determining when to end isolation are thus warranted.

So far, two main approaches have been adopted by countries around the globe. The first approach is to isolate patients for a fixed time period (i.e. a one-size-fits-all approach). For example, the Centers for Disease Control and Prevention (CDC) created guidelines for health care practitioners concerning the discontinuation of transmission-based precautions for COVID-19 patients in health care settings that are based on the time since symptom onset or disappearance (i.e. symptom-based strategy) (Centers for Disease Control and Prevention, 2020a). In the CDC guidelines, those with mild to moderate illness can end isolation (or precautions) when the following three conditions are met: ‘At least 10 days have passed since symptoms first appeared,’ ‘At least 24 hr have passed since last fever without the use of fever-reducing medications,’ and ‘Symptoms (e.g. cough, shortness of breath) have improved.’ However, such a one-size-fits-all approach does not account for the individual variability in viral load (Iwanami et al., 2020), which is associated with both severity (Zheng et al., 2020) and persistence of symptoms (Long et al., 2020), and may thus not fully prevent further transmission.

The second approach is based on the assessment of the viral load of each isolated patient (i.e. personalized approach), and isolation ends when the viral load drops below a certain threshold value, which is associated with a low risk of further spreading the pathogen (He et al., 2020). The viral load can be measured by reverse transcription polymerase chain reaction (PCR), which can be used not only for diagnosing infection but also in determining when to end the isolation period. As an example, the CDC recommends using PCR testing in particular circumstances, such as for patients with severe immunodeficiency. The guidelines include both the resolution of symptoms and PCR test results, that is, ‘Results are negative from at least two consecutive respiratory specimens collected ≥24 hr apart’ (Centers for Disease Control and Prevention, 2020a).

The purpose of this study was to assess whether the personalized approach based on PCR test results minimizes the length of the isolation period while limiting the risk of prematurely releasing infectious individuals as compared with the one-size-fits-all approach. Moreover, we define best practices for the use of a PCR-based personalized approach. To do so, we developed a mathematical model of SARS-CoV-2 viral load dynamics (Ejima et al., 2020; Iwanami et al., 2020) that accounts for individual heterogeneity and is calibrated on longitudinal viral load data.

## Results

### Descriptive statistics

We identified four papers meeting the inclusion criteria (Kim et al., 2020a; Wölfel et al., 2020; Young et al., 2020; Zou et al., 2020). Among the patients reported in these four studies, 30 patients (approximately 60% of the participants in the original studies) met our inclusion criteria (Table 1). Three studies were from Asia and one was from Europe. The lowest and highest detection limit among those studies were 15.3 copies/mL and 68 copies/mL, respectively. These are relatively lower than the commonly used threshold values (the median was 100 copies/mL [Fung et al., 2020; Giri et al., 2021; van Kasteren et al., 2020]). The data were collected by February of 2020, which was during the early phase of the COVID-19 pandemic. Participants were hospitalized patients of ages ranging from 28 to 78 years; the sex ratio was mostly even.

**Table 1.**
 Summary of the viral load data used for modeling.


<table>
  <thead>
    <tr>
      <th>Source</th>
      <th>Country</th>
      <th># of included (excluded) patients</th>
      <th>Sampling site</th>
      <th>Reporting unit</th>
      <th>Detection limit (copies/mL)</th>
      <th>Symptom onset of patients</th>
      <th>Age‡</th>
      <th>Sex (M:F)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Young et al.</td>
      <td>Singapore</td>
      <td>12 (6)</td>
      <td>nasopharynx</td>
      <td>cycle threshold*</td>
      <td>68.0</td>
      <td>1/21 - 1/30</td>
      <td>37.5 (31–56)</td>
      <td>6:6</td>
    </tr>
    <tr>
      <td>Zou et al.</td>
      <td>China</td>
      <td>8 (8)</td>
      <td>nose</td>
      <td>cycle threshold*</td>
      <td>15.3</td>
      <td>1/11 - 1/26</td>
      <td>52.5 (28–78)</td>
      <td>3:5</td>
    </tr>
    <tr>
      <td>Kim et al.</td>
      <td>Korea</td>
      <td>2 (7)</td>
      <td>nasopharynx and oropharynx</td>
      <td>cycle threshold*</td>
      <td>68.0</td>
      <td>NA</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>Wölfel et al.</td>
      <td>Germany</td>
      <td>8 (1)</td>
      <td>pharynx</td>
      <td>viral load (copies/swab)†</td>
      <td>33.3</td>
      <td>1/23 - 2/4</td>
      <td>NA</td>
      <td>NA</td>
    </tr>
  </tbody>
</table>

_*Viral load was calculated from cycle threshold values using the conversion formula: log10⁡(Viral \ load \ [copies/mL])=−0.32×Ct \ values \ [cycles]+14.11 (Peiris et al., 2003).† One swab = 3 mL (Wölfel et al., 2020).‡ Median (range)._

### Model fitting

Three models were fitted to the data: the baseline model, the ‘eclipse phase’ model, and the ‘innate immune response’ model. The estimated model parameters, the estimated (mean) curves and the individual fitted curves are reported in Supplementary file 1, Figure 1, respectively. Although all the three models lead to similar results (Figure 1), the baseline model shows a longer tail than the two other models, due to the lower estimated death rate of infected cells (Supplementary file 1). Further, the three models showed similar values of the Akaike information criterion (AIC) and the Bayesian information criterion (BIC) (Supplementary file 2). Unless otherwise stated, the results presented in thereafter refer to the baseline model.

![Figure 1.](https://cdn.elifesciences.org/articles/69340/elife-69340-fig1-v1.jpg)

**Figure 1.:** The solid lines are the estimated viral load curves of the three models for the best fit parameters (Blue: baseline model, Green: ‘ecliplse phase’ model, Yellow: ‘innate immune response’ model). The shaded regions correspond to 95% predictive intervals. The 95% predictive interval was created using bootstrap approach.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/69340/elife-69340-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** The dots and curves represent the observed and estimated viral load (Blue: baseline model, Green: ‘ecliplse phase’ model, Yellow: ‘innate immune response’ model), respectively. The detection limit for each patient is shown as dotted horizontal line.

### One-size-fits-all approach

By considering a fixed time of 10 days since symptom onset as the criterion for ending isolation, the probability of releasing patients who are still infectious was estimated to be 0.9% (95%CI: 0.6 to 1.2), with a lengthy prolonged isolation of 6.8 days (95% empirical CI: 1 to 8) when considering 105 copies/mL as the infectiousness threshold value (Figure 2AB). The estimated probability of prematurely ending isolation becomes 6.6% (95%CI: 5.8 to 7.4) and 0% with a prolonged isolation of 4.8 days (95% empirical CI: −2 to 8) and 8.3 days (95% empirical CI: 6 to 10) if we consider 104.5 and 105.5 copies/mL as infectiousness threshold values, respectively (Figure 2A). To guarantee a probability lower than 5%, we estimated that patients need to be isolated for 7 days, 11 days, and 5 days for infectiousness threshold values of 105.0, 104.5, and 105.5 copies/mL, respectively (Figure 2A). In this case, again, the length of the prolonged isolation was estimated to be substantial (Figure 2B): 3.8 days (95% empirical CI: −2 to 5), 5.8 days (95% empirical CI: −2 to 8), and 3.3 days (95% empirical CI: 0 to 4) for infectiousness threshold values of 105.0, 104.5, and 105.5 copies/mL, respectively. In sum, to guarantee low probabilities to prematurely end the isolation and thus release patients who are still infectious, the associate cost is to have unnecessary long isolations for the majority of patients.

![Figure 2.](https://cdn.elifesciences.org/articles/69340/elife-69340-fig2-v1.jpg)

**Figure 2.:** (A) Probability of prematurely ending the isolation of infectious patients for different lengths of the isolation period and for different infectiousness threshold values. (B) Mean length of unnecessarily prolonged isolation for different lengths of the isolation period and for different infectiousness threshold values. Color keys and symbols apply to both panels. Note that the symbols correspond to the shortest isolation periods when the condition is met.

### Personalized approach using PCR test results

By considering two consecutive negative test results repeated at an interval of 1 day as the criterion for ending isolation, the probability of prematurely ending isolation was estimated to be 8.1% (95%CI: 7.2 to 9.0) with a negligible length of prolonged isolation of 1.2 days (95% empirical CI: −1 to 3) when considering 105.0 copies/mL as the infectiousness threshold value (Figure 3A). By acting on the testing strategy, we can control both the probability of prematurely ending isolation and the length of prolonged isolation. The probability of ending isolation of infectious patients decreased with a longer interval between testing and more consecutive negative results (the upper panel in Figure 3A). However, the length of prolonged isolation increased at the same time (the lower panel in Figure 3A). If a 5% or lower risk of prematurely ending isolation is considered, three consecutive negative test results with the tests performed every day minimizes the length of unnecessary isolation (2.3 days [95% empirical CI: 0 to 5]) (Figure 3A). We repeated the same analyses using different infectiousness threshold values (104.5 and 105.5 copies/mL). Both the probability of prematurely ending isolation and the length of prolonged isolation were not much influenced by infectiousness threshold values, because the viral load is directly measured in the personalized approach (Figure 3B,C).

![Figure 3.](https://cdn.elifesciences.org/articles/69340/elife-69340-fig3-v1.jpg)

**Figure 3.:** (A) Probability of prematurely ending isolation (upper panels) and mean length of unnecessarily prolonged isolation (lower panels) for different values of the interval between PCR tests and the number of consecutive negative results necessary to end isolation; the infectiousness threshold value is set to 105.0 copies/mL. The areas surrounded by purple and pink dotted lines are those with 1% or 5% or lower of risk of prematurely ending isolation of infectious patients, respectively, and the triangles and circles correspond to the conditions which realize the shortest prolonged isolation within each area. (B) Same as A, but for an infectiousness threshold value of 104.5 copies/mL. (C) Same as A, but for an infectiousness threshold value of 105.5 copies/mL. Color keys and symbols apply to all panels.

### Comparison between the one-size-fits-all and the personalized approach

To highlight the differences between the one-size-fits-all and the personalized approaches, we systematically compared the two approaches by looking at the length of the prolonged isolation for a 5% or lower (Figure 4A) or 1% or lower (Figure 4B) risk of prematurely ending isolation. For the personalized approach, the best combination of the number of consecutive negative test results and the interval of tests was selected for each infectiousness threshold value. The personalized approach was not influenced by the infectiousness threshold values and yielded to shorter prolonged isolation compared with the one-size-fits-all approach. However, because the prolonged isolation for the one-size-fits-all approach was influenced by infectiousness threshold values, the difference between the one-size-fits-all and personalized approaches in prolonged isolation became smaller with higher infectiousness threshold values.

![Figure 4.](https://cdn.elifesciences.org/articles/69340/elife-69340-fig4-v1.jpg)

**Figure 4.:** (A) Mean length of prolonged isolation for different infectiousness threshold values and for the two approaches when considering a 5% or lower risk of prematurely ending isolation. Note that for the personalized approach, the interval between PCR tests and the number of consecutive negative results necessary to end isolation were selected to minimize the duration of prolonged isolation. (B) Same as A, but considering a 1% or lower risk of prematurely ending isolation. Color keys apply to both panels.

### Influence of model selection

Figure 5 shows the length of the prolonged isolation for a 5% or lower or 1% or lower risk of prematurely ending the isolation for all the analyzed models. Regardless of the considered models, the personalized approach allows shorted length of unnecessarily isolation. Nonetheless, it is important to remark that the length of prolonged isolation is slightly different among the analyzed models. For example, under the one-size-fits-all approach, it was longer for the ‘innate immune response’ model as compared with the other two; this is due to larger variability in viral load especially at the late phase of the infection (Figure 1). Under the personalized approach, the length of prolonged isolation was longer in the baseline model as compared to the two alternative models (Figure 1). In summary, by comparing the three models, we can conclude that the one-size-fits-all approach is sensitive to the variability of the viral load curve, whereas the personalized approach is sensitive to the decay speed of the viral load.

![Figure 5.](https://cdn.elifesciences.org/articles/69340/elife-69340-fig5-v1.jpg)

**Figure 5.:** (A) Mean length of prolonged isolation for different infectiousness threshold values and for the two approaches when considering a 5% or lower risk of prematurely ending isolation and for the three analyzed models. Note that for the personalized approach, the interval between PCR tests and the number of consecutive negative results necessary to end isolation were selected to minimize the duration of prolonged isolation. (B) Same as A, but considering a 1% or lower risk of prematurely ending isolation. Color keys apply to both panels.

## Discussion

Guidelines for ending the isolation of COVID-19 patients that balance the risk of prematurely ending isolation with the burden of prolonged isolation are a crucial topic of discussion. Here, we propose a highly flexible modeling framework to quantify both viral dynamics and measurement errors. Using this approach, we tested alternative policies regulating the isolation of SARS-CoV-2-infected individuals by accounting for individual variability in the immune response. We estimated the probability of prematurely ending isolation and the length of unnecessarily prolonged isolation with two approaches: the one-size-fits-all approach and the personalized approach using PCR test results.

By considering a risk of 5% or lower of prematurely ending the isolation of a SARS-CoV-2-infected individual, our central estimate for the one-size-fits-all approach requires an isolation period of 7 days after symptom onset, with a prolonged isolation phase lasting about 4 days, depending on the threshold for infectiousness considered. On the other hand, the personalized approach entails a prolonged isolation phase of approximately 2 days, independently of the considered infectiousness threshold values. The better performance of the personalized approach is not surprising. In this approach, viral load is observed directly and is compared against the threshold by using PCR test results. By contrast, the one-size-fits-all approach considers only the time since symptom onset and does not refer to viral load, which has substantial interindividual variation. Further, the personalized approach can be optimized by choosing the best testing schedule (i.e. interval of testing and the number of consecutive negative test results). However, it should be noted that the personalized approach is more costly, due to the need for performing multiple PCR tests, thus entailing logistic challenges because patients need to be tested by health care professionals. The logistics of testing isolated patients is particularly challenging in Western countries, where patients not requiring hospital care are isolated in their place of residence (European Centre for Disease Prevention and Control, 2020b), in contrast with countries like China, where they are isolated in dedicated facilities (Burki, 2020). The development of PCR tests using saliva samples may help to overcome some of these challenges, promising to decrease the work burden and lower the risk of infection for health care workers (Azzi et al., 2020; Tu et al., 2020; Wyllie et al., 2020). Indeed, the viral load measured from saliva is comparable to or slightly higher than that from nasopharyngeal samples, which guarantees a similar level of sensitivity (Tu et al., 2020; Wyllie et al., 2020).

In this study, we used PCR tests to define the end of an isolation period in the personalized approach. PCR tests provides quantitative viral load estimates, which can be directly compared against the infectiousness threshold. Meanwhile, reverse transcription loop-mediated isothermal amplification (RT-LAMP) tests and rapid antigen tests for SARS-CoV-2 have been developed and recommended for repeated screenings, given that they are less expensive and with a shorter turnaround time than PCR tests (less than an hour vs. a day or two) (Butler et al., 2021; Dao Thi et al., 2020; Larremore et al., 2021; Yang et al., 2021b). Although these tests have lower sensitivity (the detection limit is about 105.0 copies/mL; Butler et al., 2021; Dao Thi et al., 2020; Miyakawa et al., 2021; Yang et al., 2021b) than PCR tests, they can help mitigating SARS-CoV-2 transmission when used for population screenings (Larremore et al., 2021) and contact tracing (Quilty et al., 2021); in fact, the viral load threshold of infectiousness is considered to be higher than the detection limits of RT-LAMP tests and rapid antigen tests. Epidemiological studies are needed to assess whether isolation strategies based on RT-LAMP or rapid tests have a similar mitigation effect to those based on PCR testing.

Two guidelines for ending isolation were considered in this study. In most countries, the one-size fits-all approach is employed; however, the duration is slightly different among countries. The WHO recommends isolation for 10 days after symptom onset or a positive test for asymptomatic individuals (World Health Organization, 2020). The ECDC recommends isolation of 10 or 20 days for mild/moderate or severe cases, respectively, whereas for asymptomatic individuals, 10 days isolation after a positive test is recommended (European Centre for Disease Prevention and Control, 2020a). However, these durations actually vary from 7 to 14 days depending on each member state of the European Union (European Comission, 2020).

We submit that our approach can be used as a scientific backup or to adjust isolation guidelines currently in use in different countries. Nonetheless, the following limitations should be kept in mind. First, the number of samples analyzed were relatively small (30 patients), they did not cover all age groups, and pertained to symptomatic hospitalized patients only. This did not allow us to test whether the duration of the isolation is influenced by the severity of the disease. In particular, the duration may be shorter than that predicted in this study, as the analyzed samples were composed by hospitalized patients. Guidelines considering fixed durations of the isolation depending on disease severity may be easier to implement and limit the length of unnecessary prolonged isolations. Still concerning the analyzed sample, it is important to stress that patients were infected in the early stages of the pandemic and thus likely infected by the historical SARS-CoV-2 lineages. To what extent our findings can be generalized to other categories of individuals (e.g. asymptomatic infections) and SARS-CoV-2 variants remains to be seen. The confidence intervals reported in this paper need to be cautiously interpreted as the extent and quality of relevant viral load data is unfortunately quite limited. Further, should the input data be non-representative, this could have caused a bias in our estimates of the duration of the isolation period. It is, however, important to stress that exactly in light of this scarcity of longitudinal data, model-based simulations are a powerful tool for properly integrating temporal trends in the collected data and for assessing individual variabilities. Second, we did not explicitly model the longitudinal clinical course of symptoms in SARS-CoV-2-infected individuals because of the lack of data associating the clinical course with viral load. Further research in this direction is warranted (He et al., 2020), especially as several countries (including the US) consider the presence or absence of symptoms among the criteria for ending isolation. Third, a deeper knowledge of the association between the viral load and the transmission risk would be a key to narrow the uncertainty surrounding the minimum viral load level that still allows SARS-CoV-2 transmission. Specifically, 104.5, 105.0, and 105.5 copies/mL were used and were based on epidemiological observations of transmission events from contact tracing data (Hu et al., 2020; Sun et al., 2021). Other studies used a different perspective to approach the same research question and investigated the threshold relying on experimental virological data (i.e. culturability). For example, van Kampen et al., 2021; Wölfel et al., 2020 found that the virus was culturable if the viral load is above 106.0 copies/mL. Such uncertainty is reflected in the high variability in the results obtained for the one-size-fits-all approach; on the other hand, the personalized approach provided stable results with respect to the infectiousness threshold values. Fourth, we considered arbitrary values for the risk of prematurely ending isolation (namely, 1% or 5%). Whether such risks are acceptable depends on several factors such as the epidemiological context (e.g. the prevalence of the infection and disease burden), the aim of the adopted policies (e.g. suppression of transmission, mitigation of disease burden), propensity to take risks. Nonetheless, it is worth remarking that, if for a certain level of risk, the difference between the personalized and one-size-fits-all approaches is small, the fixed duration approach may have the advantage in terms of simplicity, cost, and resources. We also note that in the personalized approach, we used qualitative PCR test results only (i.e. whether the viral load is above or below a given threshold). The use of quantitative PCR test results may enable us to predict the optimal day to end isolation for each patient. Finally, although some of patients were tested (and isolated) before symptom onset or a few days after symptom onset, in this study, we assumed the testing starts immediately after symptom onset. As this analysis primarily focuses on the time when the viral load crosses the infectiousness threshold, we do not expect that the timing of the first test does not influence much our findings. However, starting the tests too early since isolation (or symptom onset) might be impractical and it should be determined based on operational and cost constraints. Future research could be dedicated to examining whether the starting day of testing could be defined on the basis of disease severity.

The guidelines regulating the length of isolation of COVID-19 patients require further updating following new epidemiologic and clinical knowledge, patient characteristics, and the capability of health sectors, such as test availability. Indeed, in several countries, these guidelines have been updated several times throughout the course of the pandemic (Centers for Disease Control and Prevention, 2020a; European Centre for Disease Prevention and Control, 2020a; Public Health England, 2020) and the emergence of new variants can spark new adjustments in the future as well. Our proposed modeling framework is very flexible and could be easily adapted to simulate the immune response and effect of antiviral therapies as well as to the study of other infectious diseases. In particular, it might prove quite relevant should new SARS-CoV-2 variants show different temporal infectiousness profiles than the historical lineage (Davies et al., 2021).

In conclusion, until the vaccination effort successfully suppresses the widespread circulation of SARS-CoV-2, nonpharmaceutical interventions, and patient isolation in particular, will continue to be a primary tool for mitigating SARS-CoV-2 spread. Understanding when isolated patients may be released will thus remain a key component in the fight against COVID-19.

## Materials and methods

### Viral load data

We searched PubMed and Google Scholar for papers reporting longitudinal viral load data of COVID-19 patients. We set five inclusion criteria: (1) multiple observations of the viral load were reported per patient (if cycle thresholds were reported instead of viral load, they were transformed to viral load by using the following conversion formula [Zou et al., 2020]: $log_{10}⁡(Viral load [copies/mL])=−0.32\timesCt values [cycles]+14.11$); (2) viral load was measured from upper respiratory specimens (i.e. nose, pharynx) for consistency; (3) viral load along with the time since symptom onset was reported; (4) the patients were not under antiviral treatment (antiviral therapy can directly influence the viral dynamics); and (5) patients were symptomatic (because we used the time since symptom onset as the time scale). We used the de-identified secondary data from published studies, and thus ethics approval for this study was not necessary.

### Modeling SARS-CoV-2 viral dynamics

We developed a mathematical model of SARS-CoV-2 viral dynamics (Ikeda et al., 2016; Kim et al., 2020b; Perelson, 2002). The model is composed of two components: (1) the ratio between the number of uninfected target cells at time $t$ and the number of uninfected target cells at time 0 ($t=0$ corresponds to the time of symptom onset),$ f(t)$; and (2) the amount of virus per unit in sample specimen (copies/mL) at time $t$, $V(t)$. $V(t)$ exponentially increases since infection, reaches a peak, and starts declining because of the depletion of target cells, which is consistent with the observed viral dynamics. Model parameters were calibrated by fitting the longitudinal data with a mixed-effect model. Details on the model and the fitting procedure are reported in Appendix 1. To account for individual variability in the viral dynamics, we simulated $V(t)$ for 1000 patients by sampling from the posterior distributions of the model parameters. To simulate the viral load measured by a PCR test,$ V^(t)$, we added a measurement error to $V(t)$ (see Appendix 1 for details). The model used here (baseline model) is one of the simplest models for viruses causing acute respiratory infection. Given that the biological infection process has not been fully understood yet, we believe using a simple model represents an appropriate baseline choice. Specifically in the literature of SAS-CoV-2 studies, several different models have been used including the baseline model (Gonçalves et al., 2020; Goyal et al., 2020; Goyal et al., 2021; Kim et al., 2020b). Nonetheless, to investigate to what extent the model choice affects our findings, we considered two alternative models: the ‘eclipse phase’ model (Baccam et al., 2006; Gonçalves et al., 2020) and the ‘innate immune response’ model (Baccam et al., 2006). The detailed description of the analyzed models is reported in Appendix 1.

### Assessment and comparison of the one-size-fits-all and the personalized approach

In the one-size-fits-all approach, we assumed isolation to end after a fixed time since symptom onset, whereas in the personalized approach using PCR tests, isolation ends after obtaining a given number of consecutive negative test results (with a given time interval between the tests). As the baseline scenario for the one-size-fits-all approach (here referred to as the ‘symptom-based strategy’), we considered a fixed time of 10 days. As the baseline scenario for the personalized approach (here referred to as the ‘test-based strategy’), we considered two consecutive negative test results repeated at a daily interval (in agreement with the CDC guidelines [Centers for Disease Control and Prevention, 2020a]). Here, we assumed the testing starts immediately after symptom onset.

Epidemiological studies based on contact tracing data suggest that infectiousness nearly disappears 8 days after symptom onset (Hu et al., 2020; Sun et al., 2021). According, to Kim et al., 2020b, the 97.5 percentile of the viral load 8 days after symptom onset is 105.0 copies/mL (Kim et al., 2021). We thus use 105.0 copies/mL as threshold to define whether a patient is still infectious (i.e. able to transmit the infection). All the obtained results are reported also by considering viral load threshold values of 104.5 copies/mL and 105.5 copies/mL as sensitivity analyses.

To evaluate the different strategies, we computed two metrics based on the simulated viral loads: the probability of prematurely ending isolation and the length of unnecessarily prolonged isolation. The probability of prematurely ending isolation is the chance that infected patients are released from isolation while they are still infectious. The length of prolonged isolation is defined as the difference between the time at which a patient is no longer infectious and the time when her or his isolation ends. Note that when the prolonged isolation is negative, it means that the isolation period has ended when the patient is still infectious.

As sensitivity analyses, we considered the length of isolation in the range of 2 to 20 days for the one-size-fits-all approach. For the personalized approach, the frequency of testing (i.e. the interval between consecutive tests) was considered to vary between 1 and 5 days and the number of consecutive negative test results to vary between 1 and 5. Details about the performed analyses are reported in Appendix 1 and a schematic of the methodology is shown in Figure 6.

![Figure 6.](https://cdn.elifesciences.org/articles/69340/elife-69340-fig6-v1.jpg)
