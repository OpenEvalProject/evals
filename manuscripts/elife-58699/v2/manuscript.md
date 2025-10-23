# The contribution of asymptomatic SARS-CoV-2 infections to transmission on the Diamond Princess cruise ship

## Authors

- Jon C Emery<sup>1</sup> ([ORCID: 0000-0001-6644-7604](https://orcid.org/0000-0001-6644-7604))
- Timothy W Russell<sup>1</sup>
- Yang Liu<sup>1</sup>
- Joel Hellewell<sup>1</sup>
- Carl AB Pearson<sup>1</sup>
- Katherine E Atkins<sup>1</sup>
- Katherine E Atkins
- Petra Klepac
- Akira Endo
- Christopher I Jarvis
- Nicholas G Davies
- Eleanor M Rees
- Sophie R Meakin
- Alicia Rosello
- Kevin van Zandvoort
- James D Munday
- W John Edmunds
- Thibaut Jombart
- Megan Auzenbergs
- Emily S Nightingale
- Mark Jit
- Sam Abbott
- David Simons
- Nikos I Bosse
- Quentin J Leclerc
- Simon R Procter
- C Julian Villabona-Arenas
- Damien C Tully
- Arminder K Deol
- Fiona Yueqian Sun
- Stéphane Hué
- Anna M Foss
- Kiesha Prem
- Graham Medley
- Amy Gimma
- Rachel Lowe
- Samuel Clifford
- Matthew Quaife
- Charlie Diamond
- Hamish P Gibbs
- Billy J Quilty
- Kathleen OReilly
- Gwenan M Knight<sup>1</sup> ([ORCID: 0000-0002-7263-9896](https://orcid.org/0000-0002-7263-9896))
- Rosalind M Eggo<sup>1</sup>
- Adam J Kucharski<sup>1</sup> ([ORCID: 0000-0001-8814-9421](https://orcid.org/0000-0001-8814-9421))
- Sebastian Funk<sup>1</sup> ([ORCID: 0000-0002-2842-3406](https://orcid.org/0000-0002-2842-3406))
- Stefan Flasche<sup>1</sup>
- Rein MGJ Houben<sup>1</sup> ([ORCID: 0000-0003-4132-7467](https://orcid.org/0000-0003-4132-7467)) †

### Affiliations

1. Centre for Mathematical Modelling of Infectious Diseases, Department of Infectious Disease Epidemiology, Faculty of Epidemiology and Population Health, London School of Hygiene and Tropical Medicine London United Kingdom

† Corresponding author

## Abstract

A key unknown for SARS-CoV-2 is how asymptomatic infections contribute to transmission. We used a transmission model with asymptomatic and presymptomatic states, calibrated to data on disease onset and test frequency from the Diamond Princess cruise ship outbreak, to quantify the contribution of asymptomatic infections to transmission. The model estimated that 74% (70–78%, 95% posterior interval) of infections proceeded asymptomatically. Despite intense testing, 53% (51–56%) of infections remained undetected, most of them asymptomatic. Asymptomatic individuals were the source for 69% (20–85%) of all infections. The data did not allow identification of the infectiousness of asymptomatic infections, however low ranges (0–25%) required a net reproduction number for individuals progressing through presymptomatic and symptomatic stages of at least 15. Asymptomatic SARS-CoV-2 infections may contribute substantially to transmission. Control measures, and models projecting their potential impact, need to look beyond the symptomatic cases if they are to understand and address ongoing transmission.

## Introduction

The ongoing COVID-19 pandemic has spread rapidly across the globe, and the number of individuals infected with SARS-CoV-2 outstrips the number of reported cases (Wang et al., 2020; Golding et al., 2020). One key reason for this may be that a substantial proportion of cases proceed asymptomatically, that is, they either do not experience or are not aware of symptoms throughout their infection but may still transmit to others. In this sense, asymptomatic infections differ from presymptomatic infections, which describes the portion of the incubation period before symptoms develop during which onward transmission is possible.

While pre- and asymptomatic individuals do not directly contribute to morbidity or mortality in an outbreak, they can contribute to ongoing transmission, as has been shown for COVID-19 (Rothe et al., 2020; Chen et al., 2020; Ganyani et al., 2020) and other diseases (Dean et al., 2016; Slater et al., 2019; Esmail et al., 2018). In particular, purely symptom-based interventions (e.g., self-isolation upon onset of disease) will not interrupt transmission from asymptomatic individuals and hence may be insufficient for outbreak control if a substantial proportion of transmission originates from pre- and asymptomatic infections (Chen et al., 2020).

An estimate of the proportion of infections that progress to symptomatic disease, also known as the case-to-infection ratio, provides an indicator of what proportion of infections will remain undetected by symptom-based case detection (Salomon and COVID-19 Statistics, Policy modeling, and Epidemiology Collective, 2020). Evidence so far have suggested that the proportion of SARS-CoV-2 infections that proceed asymptomatically is likely non-trivial (Li et al., 2020; Liu et al., 2020a; He et al., 2020; Mizumoto et al., 2020; Lavezzo et al., 2020; Bendavid et al., 2020), although empirical data are often difficult to interpret due to opportunistic sampling frames (Nishiura et al., 2020) combined with low (Fontanet et al., 2020) and imbalanced participation from individuals with and without symptoms (Gudbjartsson et al., 2020). While it is likely that transmission from asymptomatic individuals can occur, (Bai et al., 2020) quantitative estimates are effectively absent. Improved understanding of the relative infectiousness of asymptomatic SARS-CoV-2 infection, and its contribution to overall transmission will greatly improve the ability to estimate the impact of intervention strategies (Salomon and COVID-19 Statistics, Policy modeling, and Epidemiology Collective, 2020). What is known is that in the presence of active case-finding, presymptomatic infections and symptomatic cases contribute almost equally to overall transmission, as both modelling and empirical studies have shown (Liu et al., 2020a; He et al., 2020).

Documented outbreaks in a closed population with extensive testing of individuals regardless of symptoms provide unique opportunities for improved insights into the dynamics of an infection, as knowledge of the denominator and true proportion infected are crucial, yet often unavailable in other datasets. Here, we use data from the well-documented outbreak on the Diamond Princess cruise ship to capture the mechanics of COVID-19 in a transmission model with explicit asymptomatic and presymptomatic states to infer estimates for the proportion, infectiousness and contribution to transmission of asymptomatic infections. Available data included the date of symptom onset for symptomatic disease for passengers and crew, the number of symptom-agnostic tests administered each day, and the date of positive tests for asymptomatic and presymptomatic individuals (Mizumoto et al., 2020; Nishiura, 2020; NIID, 2020).

## Results

## Model calibration

The model reflected the data well (Figure 1), including the differently timed peaks for confirmed symptomatic cases for crew (Figure 1A) and passengers (Figure 1B). In addition, the model matched the expected impact of quarantine of passengers on transmission from February 4th as illustrated by the drop in reproductive number (Figure 1E), followed by a later drop in transmission after February 10th, which was driven by a change in contact pattern in crew. See Figure 1—figure supplements 1–2 for full calibration outputs.

## Asymptomatic infections

We estimated that 74% of infections proceeded asymptomatically (70–78%, 95% Posterior Interval (PI)) (see Figure 2A). The strong identifiability of this parameter is driven by the relative proportions of individuals testing positive with and without symptoms, combined with the time-delay between symptom-based and symptom-agnostic testing. As a result, our model estimated that in total 1304 (1,198–1,416) individuals were infected, representing 35% (32–38%) of the initial total population on the Diamond Princess. Over half of these infections had not been detected at disembarkation on February 21 st (53%, 51–56%) consisting of infected individuals who had recovered and became test negative before they were tested (37%, 34–40%), were yet to be tested (15%, 13–16%), or had recently been exposed and were not yet detectable at that point (1%, 1–3%). Nearly two-thirds of pre- and asymptomatic infections (67%, 66–68%) and 8% (6–9%) of symptomatic infections went undetected up until disembarkation (Figure 2C).

In contrast to the strong identifiability of the proportion of infections that were asymptomatic, the model was unable to identify the relative infectiousness of asymptomatic infections from the data, that is, a uniform prior was effectively returned (see Figure 2B). This is because the relative infectiousness of asymptomatic infections was degenerate with the overall contact rate, meaning the data were consistent with either relatively frequent contact with less infectious individuals or relatively infrequent contact with more infectious individuals (see Figure 1—figure supplement 1). Despite this, the estimated proportion of transmission due to asymptomatic infections is 69%, with a wide confidence interval (20–85%) and an interquartile range of 56–76% (Figure 2D). The reason this estimate is not effectively 0–100%, as might be expected by the unidentifiable relative infectiousness, is the combination of the strongly identified, relatively high proportion of infections that are asymptomatic and the non-linear relationship between the relative infectiousness of asymptomatics and their contribution to transmission, which quickly saturates to its maximal value (see Figure 2—figure supplement 1). The result is that only a modest relative infectiousness is required to produce a non-trivial contribution to transmission. The relative infectiousness of presymptomatics was also unidentifiable, however, in all scenarios the remaining transmission was equally distributed between the presymptomatic (14%, 1–44%) and symptomatic (17%, 11–42%) individuals. Figure 3 shows the instantaneous proportion of transmission from symptomatic (A), presymptomatic (B) and asymptomatic (C) individuals over the course of the epidemic.

![Figure 3.](https://cdn.elifesciences.org/articles/58699/elife-58699-fig3-v2.jpg)

**Figure 3.:** Instantaneous proportion of transmission from symptomatic (A), presymptomatic (B) and asymptomatic (C) individuals over the course of the epidemic, following the introduction of a single symptomatic individual on 20th Jan. Red lines = median, shading = 95% posterior interval. Two vertical lines show the date of the first confirmed diagnosis (left) and the start of quarantine measures (right).

Because of the non-identifiability of the relative infectiousness of asymptomatic infections we investigated marginal posterior estimates (Table 1). We find that low relative infectiousness of asymptomatic infections (0–25% compared to symptomatic individuals) would need to be compensated by a net reproduction number for individuals during their presymptomatic and symptomatic phase of 15.5–29.1.

## Sensitivity analyses

Without an asymptomatic state the model was unable to reconstruct the dynamics of the outbreak (Appendix 2—figures 1–3, Deviance Information Criterion (DIC) = 974 vs 329 for the primary analysis). Moreover, adjusting the relative value for mixing between crew and passengers did not have a qualitative effect on the results (Appendix 2—figures 4–11).

Biased symptom-agnostic testing had a greater impact on the results. Those testing negative having a 50% higher probability of being tested compared to the primary analysis led to a corresponding greater proportion of infections that were asymptomatic (84%, 82–87%), total number infected (2,097, 1,914-2,292) and contribution of asymptomatics to transmission (78%, 36–91%) (see Appendix 2—figures 12–15). Conversely, those testing positive having a 50% higher probability of being tested compared to the primary analysis led to a corresponding smaller proportion of infections that were asymptomatic (66%, 61–71%), total number infected (1,051, 965-1,161) and contribution of asymptomatics to transmission (59%, 9–79%) (see Appendix 2—figures 16–19).

When we assumed a fixed age-specific ratio for the proportion of infections that progress asymptomatically, the model was able to fit the data, although the number of correlated parameters was high. Overall results were similar to the main analysis, with a proportion asymptomatic of 42% (41–44%) and 89% (85–91%) for passengers and crew, respectively. The proportion of all transmission from asymptomatics was 69% (IQR = 59–74%). Relative infectiousness was again unidentifiable. See Appendix 2—figures 20–23 for details.

A longer latent period provided a poorer fit to the data (DIC = 361) (Appendix 2—figures 24–27). Adjusting the duration of the asymptomatic state to half or double the sum of the presymptomatic and symptomatic states made little qualitative difference to the results (Appendix 2—figures 28–35), although the shorter asymptomatic period was a marginally poorer fit to the data (DIC = 338). Finally, recalibrating the model assuming the 35 confirmed pre/asymptomatic cases where a test date was not available were allocated to the last feasible day (13th Feb) made no qualitative difference to our results (see Appendix 2—figures 36–39).

## Discussion

## Summary

We find that in this well-documented outbreak in a closed population, 74% (70–78%) of infections proceeded asymptomatically, equaling a 1:3.8 (1:3.3-1:4.4) case-to-infection ratio. The majority of asymptomatic infections remained undetected, but may have contributed substantially to ongoing transmission. While the relative infectiousness of asymptomatic infections could not be identified, low infectiousness (e.g. 0–25% compared to symptomatic individuals) would have required a very high net reproduction number for individuals during their presymptomatic and symptomatic stages of (15.5–29.1).

## Interpretation

Our results are strongly informed by data, which show that when extensive symptom-agnostic testing was ramped up, substantial numbers of pre- or asymptomatic infections were identified. Given the clear suppression of transmission through quarantining, as indicated by the drop in incident symptomatic disease, this finding is most likely explained by a large proportion of undetected asymptomatic individuals.

The model and data were unable to identify a value for the relative infectiousness, although we showed how different ranges for this key parameter required specific trade-offs, as reflected in the net reproduction number for infected individuals who will develop symptomatic disease. One can argue that a net reproduction number for presymptomatic passengers at the start of the outbreak of over 20 in this population, as required if asymptomatic individuals are effectively unable to transmit (range for relative infectiousness of 0–1%) is unlikely. Such high reproductive numbers are not usually seen, exceeding for example values found for norovirus outbreaks on cruise ships (Gaythorpe et al., 2018). While SARS-CoV-2 has been shown to survive on surfaces (van Doremalen et al., 2020), this does not seem to be the primary mode of transmission. In combination with growing evidence around viral load in asymptomatic infections and their involvement in transmission chains (Lavezzo et al., 2020), as well as anecdotal evidence about transmission from asymptomatic individuals (Bai et al., 2020; Chau et al., 2020) including in closed populations (Arons et al., 2020), it is reasonable to assume that asymptomatic infections play some role in ongoing SARS-CoV transmission. In our model, asymptomatic infections were responsible for more than half of all transmission in 83% of the scenarios compatible with the data.

It is important to note that our conclusion that asymptomatic infections may have contributed substantially to ongoing transmission is critically dependent on the setting. In this case symptomatic infections were quickly identified and removed from the ship before symptom-agnostic testing began, thereby leaving asymptomatic infections to dominate transmission. Such dominance should therefore not be interpreted as a constant of nature, but instead an important consideration in settings where prompt isolation of symptomatic infections is already in place but with little to no consideration for asymptomatic infections.

## Comparison to other studies

Our estimated proportion of asymptomatic infections in this outbreak is higher than previous studies, which relied on diagnosed cases only (Mizumoto et al., 2020). As we have shown, a substantial number of infections were not detected, which would explain some of the difference. Other empirical studies have found usually lower values, while some found similar ranges. While underestimation in other estimates due to low (Fontanet et al., 2020) and imbalanced participation from individuals with and without symptoms (Gudbjartsson et al., 2020) will be part of the explanation, there remains scope for unexplained variation from more complete samples (Lavezzo et al., 2020). In addition, it is possible that PCR-based testing has a lower sensitivity for asymptomatic individuals, which would further increase the proportion of infections that were asymptomatic (Chau et al., 2020).

A sensitivity analysis showed that our results were robust to age-specific probabilities of progressing to asymptomatic infections, as well as other assumptions made in the model, and driven by trends in the data.

Our estimated substantial contribution to transmission from asymptomatic infections confirms a hypothesis from Nishiura after analysing symptomatic cases occurring post-disembarkation (Nishiura, 2020). Our initial reproduction number of 9.3 (7.4–10.6) reflects the high transmission environment expected on cruise ships via increased contacts in a confined space, although lower than the value found in an earlier analysis by Rocklöv et al., 2020.

Our finding of similar contribution to transmission from presymptomatic and symptomatic individuals also matches findings by others (Ganyani et al., 2020; Liu et al., 2020a; He et al., 2020). In line with this, it is clear that having symptoms, or at least being aware of them, is not required in the transmission of SARS-CoV-2 (Ganyani et al., 2020; Liu et al., 2020a; He et al., 2020; Kimball et al., 2020; Wei et al., 2020). Although cough is often considered essential for transmission of respiratory infections (Patterson and Wood, 2019), work in tuberculosis, influenza and other coronaviruses has shown that while a cough may increase spread, it is not a requirement. Transmission from breathing, talking and sneezing is also possible, as well as transmission from contaminated surfaces (van Doremalen et al., 2020; Leung et al., 2020; Asadi et al., 2019; Williams et al., 2020).

## Limitations

Additional data, in particular on the distribution of asymptomatic infections across crew and passengers, by age and shared quarantine environments would have benefited the model and potentially enabled us to estimate a range for the relative infectiousness of asymptomatic infections. A serological survey of the population, and the date and testing history of individuals who developed symptoms post-disembarkation, would also have likely informed more precise model estimates. In addition, better evidence on performance of the test used, and the associated likelihood of false-negative or false-positive results would help refine estimates. As more data become available, future model analyses of SARS-CoV-2 dynamics in closed populations should further inform the key questions we have looked to address here.

Whilst symptom-agnostic testing provided valuable insights into the pre- and asymptomatic states, such testing was not necessarily random, as was assumed in our primary analysis. Indeed, it is known that individuals were generally screened in reverse-age order (NIID, 2020). Sensitivity analyses considering biased testing still produced non-trivial results for the proportion of infections that were asymptomatic however.

Our model also assumed that the infectiousness of all transmissible states was constant over time. If instead symptomatic individuals are most infectious immediately after symptom onset (He et al., 2020), an estimate of their contribution to transmission would in principle increase. Given the likely heightened awareness of symptoms on board however, such an increase is likely to be marginal. Indeed, since our assumption of an average one-day, exponentially distributed delay between symptom onset and removal from the ship is likely to be an overestimate, a prompter removal distribution would at least in part offset such an increase.

A similar simplification was made by assuming that the probability of an individual progressing to either a presymptomatic or asymptomatic infection was independent of who infected whom. It is possible, however, that transmission from a symptomatic infection may be more likely to ultimately result in another symptomatic infection, owing to a higher infecting dose for example.

## Conclusion

Asymptomatic SARS-CoV-2 infections may contribute substantially to transmission. This is essential to consider for countries when assessing the potential effectiveness of ongoing control measures to contain COVID-19.

## Materials and methods

## Data

Data from the Diamond Princess outbreak have been widely reported. (Mizumoto et al., 2020; Nishiura, 2020; NIID, 2020) On January 20th, the Diamond Princess cruise ship departed from Yokohama on a tour of Southeast Asia. A passenger that disembarked on January 25th in Hong Kong subsequently tested positive for SARS-CoV-2 on February 1st, reporting the date of symptom onset as January 23rd.

After arriving back in Yokohama on February 3rd, all passengers and crew were screened for symptoms, and those screening positive were then tested. The ship began quarantine on February 5th with all passengers confined to their cabins and crew undertaking essential activities only. At the start of quarantine there were 3711 individuals on board (2666 passengers and 1045 crew) with a median age of 65 (45–75 interquartile range).

Testing capacity was limited until February 11th and before then the majority of individuals tested had reported symptoms, referred to here as ‘symptom-based testing’. All individuals with a positive test at any stage were promptly removed from the ship and isolated. After February 11th, testing capacity increased and the testing of individuals irrespective of symptoms, referred to here as ‘symptom-agnostic testing’, was scaled up. In total, 314 symptomatic and 320 pre- or asymptomatic infections were reported before disembarkation was principally completed on February 21st.

We extracted the following data from Mizumoto et al., 2020; Nishiura, 2020; NIID, 2020 (see Figure 1). Firstly, the number of symptomatic cases per day (i.e. those testing positive having reported symptoms) by date of symptom onset, separately for passengers and crew. The date of symptom onset was not available for 115 cases, which we accounted for in our model structure by assuming they were distributed over time proportional to those cases with a reported date of symptom onset (see Appendix 1—table 1). Secondly, we extracted the number of pre- or asymptomatic infections identified per day (i.e. individuals testing positive having not reported symptoms) by date of test. The test date was not available for 35 pre- or asymptomatic individuals between the February 6-14th, which we assumed were distributed over time proportional to the daily number of tests performed amongst individuals not reporting symptoms. No data were available on how many individuals that tested positive in the absence of symptoms became symptomatic after disembarkation. Finally, we extracted the number of tests performed per day amongst individuals not reporting symptoms (see Appendix 1—table 2).

## Model

We built a deterministic, compartmental model to capture transmission, disease development and the effect of interventions on board the Diamond Princess. Following exposure, after which an individual is assumed to test negative for SARS-CoV-2 for the duration of the latent phase (see Table 2), a proportion of individuals proceed asymptomatically with the remainder becoming presymptomatic. This proportion equates to a universal probability of becoming either presymptomatic or asymptomatic, independent of who infected whom. Individuals in the presymptomatic, asymptomatic or symptomatic state are assumed to test positive and have independent infectiousness, expressed relative to those with symptomatic disease.

Individuals with presymptomatic infection are either detected through symptom-agnostic testing before being removed from the ship, or develop symptomatic disease. Once symptomatic disease starts, individuals can either recover undetected on the ship or, following the start of quarantine on February 5th, be detected through symptom-based testing and removed from the ship with an average delay of one day following symptom onset. We allowed for individuals to test positive after their infectious period for an average of seven days (Woelfel et al., 2020). After this, we assume they would test negative.

Individuals with asymptomatic infections either recover undetected on the ship, or are detected by symptom-agnostic testing before being removed from the ship. See Appendix 1—figure 1 for a diagram of the model.

Symptom-agnostic testing was assumed to have been random amongst those not reporting symptoms and no delay was introduced between testing and removal of those that tested positive from the ship. As such, the number of people that tested positive through symptom-agnostic testing before being removed from the ship per day was calculated using the number of tests performed per day (Figure 1F) and the proportion of individuals that were either presymptomatic, asymptomatic or recovered but continued to test positive for up to seven days, amongst all individuals on the ship not reporting symptoms. All testing was assumed to have 100% sensitivity and specificity.

Crew and passengers were modelled separately, using stratified data on the number of confirmed symptomatic cases (Figure 1A–B). We estimated the within-crew and within-passenger contact rates through calibration to the data, but assumed that the between-group contact rate was a fixed factor of 1/10th of the within-passenger rate, and explored the impact of this assumption in sensitivity analyses. We enabled the model to capture potential changes in contact behaviour between individuals by representing contact rates as sigmoid functions over time, reflecting any reductions in contact. The dates and extent of the changes were determined solely through model calibration to the data.

## Model parameterisation

We used data from the literature to inform the natural history of COVID-19, in particular for the duration of presymptomatic and symptomatic phases (see Table 2).

## Model calibration

The model was calibrated in a Bayesian framework. We fitted to the daily incidence of confirmed symptomatic cases with a known onset date, separately for passengers and crew, assuming a Poisson distribution in the likelihood. We simultaneously fitted to the daily number of confirmed pre- and asymptomatic infections for passengers and crew combined by using the number of tests administered per day and the prevalence of presymptomatic, asymptomatic and post-infection test-positive individuals, assuming a binomial distribution in the likelihood. We used uniform priors for the parameters to be estimated (see Table 2) and sampled the posterior of the model parameters using sequential Markov Chain Monte-Carlo (MCMC). A burn in phase during which the proposal distributions were adapted in both scale and shape to provide optimal sampling efficiency was discarded, leaving chains with 1.5 million iterations. The resultant MCMC chains were visually inspected for convergence.

## Model outputs

Model outputs were calculated by randomly sampling 100,000 parameter values from the posterior distribution. Model trajectories were generated and compared to the data in Figure 1A–C to inspect model fit. The basic reproduction number was also calculated over time using the next-generation matrix (Diekmann et al., 2010), as a measure of ongoing transmission. We estimated the proportion of infections that become asymptomatic and the relative infectiousness of asymptomatic infections using their respective marginal posterior parameter values. Finally, the contribution of asymptomatic infections to overall transmission, as well as the net reproduction number for presymptomatic passengers at the beginning of the outbreak (i.e. the typical number of infections generated by a single presymptomatic individual) were estimated, both overall and by specific ranges of relative infectiousness. We report the median and 95% equal-tailed posterior intervals throughout.

## Sensitivity analyses

We recalibrated the model for a number of alternative scenarios to assess model sensitivity. Firstly, we assessed the impact of removing the asymptomatic phase (i.e. 100% of infections progressed to symptomatic disease). Secondly, we explored the impact of assuming different values for the relative mixing between crew and passengers as well as shorter and longer durations of asymptomatic infection. Thirdly, we considered the impact of biased symptom-agnostic testing. Specifically, we first assumed that those that would test positive were 50% more likely to be tested, before then assuming that those that would test negative were 50% more likely to be tested, both compared to purely random testing as per the primary analysis. We also explored the impact of assuming a different proportion of asymptomatic infections for crew and passengers based on their distinct median ages (36 years for crew, 69 years for passengers), using a fixed ratio for the two proportions taken from the results of a model fitted to epidemic data in six countries by Davies et al., 2020. In addition, we explored a longer latent period given the relatively high age in our population (Jiang et al., 2020). Finally, we recalibrated the model assuming the 35 confirmed pre/asymptomatic cases where a test date was not available were allocated to the last feasible day (13th Feb) instead of proportionate to the overall number of tests over the period February 6-14th(see Appendix 2 for further details).

All analyses were conducted using R version 3.5.0 (R Development Core Team, 2014). Bayesian calibration was performed in LibBi (Murray, 2013) using RBi (Funk, 2019) as an interface. Replication data and analyses scripts are available on GitHub at https://github.com/thimotei/covid19_asymptomatic_trans (Emery et al., 2020; copy archived at https://github.com/elifesciences-publications/covid19_asymptomatic_trans).

## Role of funding source

The funder of the study had no role in study design, data collection, data analysis, data interpretation, or writing of the report. The corresponding author had full access to all the data in the study and had final responsibility for the decision to submit for publication.
