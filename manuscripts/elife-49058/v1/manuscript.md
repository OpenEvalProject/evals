# Modeling the dynamics of Plasmodium falciparum gametocytes in humans during malaria infection

## Authors

- Pengxing Cao<sup>1</sup> ([ORCID: 0000-0003-3721-9850](https://orcid.org/0000-0003-3721-9850)) †
- Katharine A Collins<sup>2</sup> ([ORCID: 0000-0002-7080-2215](https://orcid.org/0000-0002-7080-2215))
- Sophie Zaloumis<sup>4</sup> ([ORCID: 0000-0002-8253-8896](https://orcid.org/0000-0002-8253-8896))
- Thanaporn Wattanakul<sup>5</sup> ([ORCID: 0000-0002-7570-4665](https://orcid.org/0000-0002-7570-4665))
- Joel Tarning<sup>5</sup> ([ORCID: 0000-0003-4566-4030](https://orcid.org/0000-0003-4566-4030))
- Julie A Simpson<sup>4</sup> ([ORCID: 0000-0002-2660-2013](https://orcid.org/0000-0002-2660-2013))
- James McCarthy<sup>3</sup> ([ORCID: 0000-0001-6596-9718](https://orcid.org/0000-0001-6596-9718))
- James M McCaw<sup>1</sup> ([ORCID: 0000-0002-2452-3098](https://orcid.org/0000-0002-2452-3098)) †

### Affiliations

1. School of Mathematics and Statistics University of Melbourne Melbourne Australia
2. Department of Medical Microbiology Radboud University Medical Center Nijmegen Netherlands
3. QIMR Berghofer Medical Research Institute Brisbane Australia
4. Centre for Epidemiology and Biostatistics, Melbourne School of Population and Global Health University of Melbourne Melbourne Australia
5. Mahidol-Oxford Tropical Medicine Research Unit, Faculty of Tropical Medicine Mahidol University Bangkok Thailand
6. Centre for Tropical Medicine and Global Health, Nuffield Department of Medicine University of Oxford Oxford United Kingdom
7. Epidemiology Peter Doherty Institute for Infection and Immunity Parkville Australia

† Corresponding author

## Abstract

Renewed efforts to eliminate malaria have highlighted the potential to interrupt human-to-mosquito transmission — a process mediated by gametocyte kinetics in human hosts. Here we study the in vivo dynamics of Plasmodium falciparum gametocytes by establishing a framework which incorporates improved measurements of parasitemia, a novel gametocyte dynamics model and model fitting using Bayesian hierarchical inference. We found that the model provides an excellent fit to the clinical data from 17 volunteers infected with P. falciparum (3D7 strain) and reliably predicts observed gametocytemia. We estimated the sexual commitment rate and gametocyte sequestration time to be 0.54% (95% credible interval: 0.30–1.00%) per asexual replication cycle and 8.39 (6.54–10.59) days respectively. We used the data-calibrated model to investigate human-to-mosquito transmissibility, providing a method to link within-human host infection kinetics to epidemiological-scale infection and transmission patterns.

## Introduction

Malaria is a mosquito-borne parasitic disease caused by protozoan parasites of the Plasmodium genus. It is estimated to have caused approximately 219 million new cases and 435,000 deaths in 2017, primarily due to Plasmodium falciparum (The World Health Organization, 2018). New tools will be required to achieve the ambitious goal of malaria elimination. Among the tools proposed are novel interventions to block transmission from human hosts to vector mosquitoes (The malERA Refresh Consultative Panel on Tools for Malaria Elimination, 2017). P. falciparum malaria is transmitted from humans to the mosquito when terminally differentiated male and female sexual-stages of the parasite, called gametocytes, are taken up by female Anopheles mosquito during a blood meal (Bousema and Drakeley, 2011; Josling and Llinás, 2015). The level of gametocytes in the blood, often referred to as gametocytemia, is highly associated with the probability of human-to-mosquito transmission (Bradley et al., 2018; Churcher et al., 2013). Gametocyte levels below a certain threshold (i.e., <1000 per mL blood) minimize the probability that a mosquito will take up both a male and female gametocyte during a blood-meal, which is necessary to propagate infection (Collins et al., 2018). An accurate understanding of the kinetics of gametocyte development in the human host is essential to predict the probability of transmission. A mathematical model that accurately captures the processes that give rise to observed gametocyte kinetics would be an important predictive tool to facilitate the design and evaluation of effective intervention strategies.

There is significant uncertainty surrounding fundamental aspects of P. falciparum gametocyte dynamics in humans. Parameters such as how many gametocytes are produced during each asexual replication cycle, the period of time in which early gametocytes disappear from the circulation before mature gametocytes appear (referred to as sequestration), and the period in which gametocytes circulate are poorly quantified. These gaps in understanding are due to a range of technical and logistic limitations. The first is the relatively poor sensitivity of the standard diagnostic test, namely microscopic examination of blood-films. Previous in vivo estimates of gametocyte kinetic parameters have been primarily based on historical data from neurosyphilis patients who were treated with so-called malariotherapy (Diebner et al., 2000; Eichner et al., 2001). In these studies, the limit of quantification was approximately 104 parasites/mL blood, at least two orders of magnitude higher than that of current quantitative PCR (qPCR) assays (Rockett et al., 2011). This high limit of quantification prevents an accurate estimation of onset of emergence of both asexual parasites and mature gametocytes in peripheral blood. The second limitation is that the available estimates of gametocyte dynamics parameters based on in vitro cultures (Filarsky et al., 2018; Gebru et al., 2017) may not be applicable to natural infection with P. falciparum gametocytes due to in vitro conditions that may not mimic the human host (Bousema and Drakeley, 2011).

Recent advances in experimental medicine using volunteer infection studies (VIS), otherwise known as controlled human malaria infection (CHMI) studies (Coffeng et al., 2017), allow prospective study design and data collection with the explicit aim of collecting in vivo data (McCarthy et al., 2011), in particular an improved quantification of P. falciparum gametocyte kinetics by qPCR applied in a novel VIS (Collins et al., 2018). Furthermore, the models and fitting methods used in the neurosyphilis patient studies have been superseded for parameter estimation by increasingly sophisticated within-host models (Khoury et al., 2018) and improvements in computational algorithms for Bayesian statistical inference (Piray et al., 2019). Therefore, there is an emerging opportunity to improve our quantitative understanding of the dynamics of P. falciparum gametocytes in human hosts by combining the novel VIS data and advanced modeling approaches.

In this study, we developed a novel mathematical model of gametocyte dynamics, fitted the model to the VIS data and estimated the gametocyte dynamics parameters using a Bayesian hierarchical inference method. We demonstrate that the data-calibrated model can reliably predict the time-course of gametocytemia and thus should form an essential part of modeling studies of malaria transmission.

## Results

### Model fitting and validation

The outcome variable used in model fitting was the total parasitemia (total circulating asexual parasites and gametocytes per mL blood measured using qPCR) collected from a previously published VIS (Collins et al., 2018), with other measurements from the same study, such as the asexual parasitemia (circulating asexual parasites per mL blood) and gametocytemia (circulating female and male gametocytes per mL blood), used to validate model predictions.

The results of fitting the mathematical model to total parasitemia data for all 17 volunteers are given in Figure 1 where 12 of 17 volunteers experienced recrudescence. The median of posterior predictions and 95% prediction interval (PI) were computed from 5000 model simulations based on 5000 samples from the posterior parameter distribution (see Materials and methods). The results show that the predicted total parasitemia (median and 95% PI) is able to accurately capture the trends of the data through the (visual) posterior predictive check. Furthermore, the narrow 95% PI indicates a low level of uncertainty in predicted total parasitemia.

![Figure 1.](https://cdn.elifesciences.org/articles/49058/elife-49058-fig1-v1.jpg)

**Figure 1.:** Data are presented by circles. The median of posterior predictions (solid line) and 95% prediction interval (PI, shaded area) are generated by 5000 model simulations based on 5000 samples from the posterior parameter distribution as described in the Materials and methods. The histograms showing the posterior distributions of population mean and standard deviation hyperparameters are given in Figure 1—figure supplements 1 and 2. The posterior distribution of each model parameter (see the Materials and methods) for individual volunteers are given in Figure 1—figure supplements 3–14 Posterior distributions for some biological parameters are given in Figure 1—figure supplement 15, which are generated based on the posterior samples of population mean parameters (see the Materials and methods) and will be used to support the results in Table 1 shown later. The source data and computer code with instructions of implementation to generate Figure 1 and Figure 1—figure supplements 1–15 are fully publicly available at https://doi.org/10.26188/5cde4c26c8201.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/49058/elife-49058-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** 5000 samples are used to generate the distributions. The dashed curves indicate the uniform prior distributions. p.i.: post-inoculation. Note that the y-axis is probability density instead of number of samples. Relevant details of the hyperparameters are provided in the Materials and methods in the main text.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/49058/elife-49058-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** 5000 samples are used to generate the distributions. The dashed curves indicate the half-normal prior distributions. p.i.: post-inoculation. Note that the y-axis is probability density instead of number of samples. Relevant details of the hyperparameters are provided in the Materials and methods in the main text.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/49058/elife-49058-fig1-figsupp3-v1.jpg)

**Figure 1—figure supplement 3.:** The marginal posterior distributions of the individual parameter of $P_{init}$ (inoculation size) for all 17 volunteers.The violin plots (gray area) show the distributions of 5000 posterior samples. Box plots show the 25%, 50% (median) and 75% quantiles with outliers indicated by red dots. Relevant details of the individual parameter are provided in the Materials and methods in the main text.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/49058/elife-49058-fig1-figsupp4-v1.jpg)

**Figure 1—figure supplement 4.:** The violin plots (gray area) show the distributions of 5000 posterior samples. Box plots show the 25%, 50% (median) and 75% quantiles with outliers indicated by red dots. Relevant details of the individual parameter are provided in the Materials and methods in the main text.

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/49058/elife-49058-fig1-figsupp5-v1.jpg)

**Figure 1—figure supplement 5.:** The marginal posterior distributions of the individual parameter of $\sigma$ (Standard deviation of the initial parasite age distribution) for all 17 volunteers.The violin plots (gray area) show the distributions of 5000 posterior samples. Box plots show the 25%, 50% (median) and 75% quantiles with outliers indicated by red dots. Relevant details of the individual parameter are provided in the Materials and methods in the main text.

![Figure 1—figure supplement 6.](https://cdn.elifesciences.org/articles/49058/elife-49058-fig1-figsupp6-v1.jpg)

**Figure 1—figure supplement 6.:** The marginal posterior distributions of the individual parameter of $r_{P}$ (parasite replication rate) for all 17 volunteers.The violin plots (gray area) show the distributions of 5000 posterior samples. Box plots show the 25%, 50% (median) and 75% quantiles with outliers indicated by red dots. Relevant details of the individual parameter are provided in the Materials and methods in the main text.

![Figure 1—figure supplement 7.](https://cdn.elifesciences.org/articles/49058/elife-49058-fig1-figsupp7-v1.jpg)

**Figure 1—figure supplement 7.:** The marginal posterior distributions of the individual parameter of $k_{max}$ (maximum rate of parasite killing by PQP) for all 17 volunteers.The violin plots (gray area) show the distributions of 5000 posterior samples. Box plots show the 25%, 50% (median) and 75% quantiles with outliers indicated by red dots. Relevant details of the individual parameter are provided in the Materials and methods in the main text.

![Figure 1—figure supplement 8.](https://cdn.elifesciences.org/articles/49058/elife-49058-fig1-figsupp8-v1.jpg)

**Figure 1—figure supplement 8.:** The marginal posterior distributions of the individual parameter of $EC_{50}$ (half-maximum effective PQP concentration) for all 17 volunteers.The violin plots (gray area) show the distributions of 5000 posterior samples. Box plots show the 25%, 50% (median) and 75% quantiles with outliers indicated by red dots. Relevant details of the individual parameter are provided in the Materials and methods in the main text.

![Figure 1—figure supplement 9.](https://cdn.elifesciences.org/articles/49058/elife-49058-fig1-figsupp9-v1.jpg)

**Figure 1—figure supplement 9.:** The marginal posterior distributions of the individual parameter of $\gamma$ (Hill coefficient for PQP) for all 17 volunteers.The violin plots (gray area) show the distributions of 5000 posterior samples. Box plots show the 25%, 50% (median) and 75% quantiles with outliers indicated by red dots. Relevant details of the individual parameter are provided in the Materials and methods in the main text.

![Figure 1—figure supplement 10.](https://cdn.elifesciences.org/articles/49058/elife-49058-fig1-figsupp10-v1.jpg)

**Figure 1—figure supplement 10.:** The marginal posterior distributions of the individual parameter of $f$ (sexual commitment rate; not converted to percentage) for all 17 volunteers.The violin plots (gray area) show the distributions of 5000 posterior samples. Box plots show the 25%, 50% (median) and 75% quantiles with outliers indicated by red dots. Relevant details of the individual parameter are provided in the Materials and methods in the main text.

![Figure 1—figure supplement 11.](https://cdn.elifesciences.org/articles/49058/elife-49058-fig1-figsupp11-v1.jpg)

**Figure 1—figure supplement 11.:** The marginal posterior distributions of the individual parameter of $\delta_{P}$ (death rate of asexual and sexual parasites) for all 17 volunteers.The violin plots (gray area) show the distributions of 5000 posterior samples. Box plots show the 25%, 50% (median) and 75% quantiles with outliers indicated by red dots. Relevant details of the individual parameter are provided in the Materials and methods in the main text.

![Figure 1—figure supplement 12.](https://cdn.elifesciences.org/articles/49058/elife-49058-fig1-figsupp12-v1.jpg)

**Figure 1—figure supplement 12.:** The marginal posterior distributions of the individual parameter of $m$ (maturation rate of gametocytes) for all 17 volunteers.The violin plots (gray area) show the distributions of 5000 posterior samples. Box plots show the 25%, 50% (median) and 75% quantiles with outliers indicated by red dots. Relevant details of the individual parameter are provided in the Materials and methods in the main text.

![Figure 1—figure supplement 13.](https://cdn.elifesciences.org/articles/49058/elife-49058-fig1-figsupp13-v1.jpg)

**Figure 1—figure supplement 13.:** The marginal posterior distributions of the individual parameter of $\delta_{G}$ (death rate of sequestered gametocytes) for all 17 volunteers.The violin plots (gray area) show the distributions of 5000 posterior samples. Box plots show the 25%, 50% (median) and 75% quantiles with outliers indicated by red dots. Relevant details of the individual parameter are provided in the Materials and methods in the main text.

![Figure 1—figure supplement 14.](https://cdn.elifesciences.org/articles/49058/elife-49058-fig1-figsupp14-v1.jpg)

**Figure 1—figure supplement 14.:** The marginal posterior distributions of the individual parameter of $\delta_{Gm}$ (death rate of circulating gametocytes) for all 17 volunteers.The violin plots (gray area) show the distributions of 5000 posterior samples. Box plots show the 25%, 50% (median) and 75% quantiles with outliers indicated by red dots. Relevant details of the individual parameter are provided in the Materials and methods in the main text.

![Figure 1—figure supplement 15.](https://cdn.elifesciences.org/articles/49058/elife-49058-fig1-figsupp15-v1.jpg)

**Figure 1—figure supplement 15.:** 5000 samples from the posterior parameter distribution are used to generate the figures. Full details about the definitions and expressions of those biological parameters are provided in the Materials and methods in the main text. Note that a logarithm is taken for the mean lifespan of circulating gametocyte for a better visualisation of the distribution.

**Table 1.**
 Estimates of some key biological parameters and comparison with the literature.The estimates of the biological parameters (middle column) are shown as the median and 95% credible interval (CI) of the marginal posterior parameter distribution (Figure 1—figure supplement 15). Estimates from the literature (third column) are shown in the format of either ‘mean estimate (95% confidence interval)’ or ‘mean estimate [minimum – maximum estimate]’ or simply ‘a low estimate – a high estimate’. Note some quoted estimates are from either in vivo or in vitro studies of P. falciparum. The source data and computer code with instructions of implementation to generate our model estimates (middle column) in Table 1 are fully publicly available at https://doi.org/10.26188/5cde4c26c8201.


<table>
  <thead>
    <tr>
      <th>Biological parameters (unit)</th>
      <th>Median estimate (95% CI)</th>
      <th>Estimates in the literature</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Sexual commitment rate (%/asexual replication cycle)</td>
      <td>0.54 (0.30–1.00)</td>
      <td>11 (6.2–15.8) (Filarsky et al., 2018) (in vitro) 0.64 [0.027–13.5] (Eichner et al., 2001) (in vivo)</td>
    </tr>
    <tr>
      <td>Gametocyte sequestration time (days)</td>
      <td>8.39 (6.54–10.59)</td>
      <td>7.4 [4 – 12] (Eichner et al., 2001) (in vivo)</td>
    </tr>
    <tr>
      <td>Circulating gametocyte lifespan (days)</td>
      <td>63.5 (12.7–1513.9)</td>
      <td>16–32 (Gebru et al., 2017) (in vitro) 6.4 [1.3–22.2] (Eichner et al., 2001) (in vivo)</td>
    </tr>
    <tr>
      <td>Parasite multiplication factor (per asexual replication cycle)</td>
      <td>21.8 (17.6–26.9)</td>
      <td>10–33 (Wockner et al., 2017) (in vivo) 16.4 (15.1–17.8)a (in vivo)</td>
    </tr>
  </tbody>
</table>

_a JS McCarthy, personal communication, May 2019._

Having calibrated the model against total parasitemia, the 5000 posterior parameter sets were used to calculate the median of posterior predictions and 95% PI of the asexual parasitemia and gametocytemia versus time profiles. Model predictions of the asexual parasitemia and gametocytemia for all 17 volunteers are shown in Figure 2 and Figure 3 respectively (curves: median prediction; shaded areas: 95% PI) and are compared to the asexual parasitemia and gametocytemia data (circles). We emphasize that this was not a fitting exercise, rather an independent validation of the calibrated model.

![Figure 2.](https://cdn.elifesciences.org/articles/49058/elife-49058-fig2-v1.jpg)

**Figure 2.:** Data are presented by circles. The median of posterior predictions (solid curve) and 95% PI (shaded area) are generated by 5000 model simulations based on 5000 samples from the posterior parameter distribution as described in the Materials and methods. The data points with one parasite/mL (i.e., those points which lie on the dotted line) indicate measurements for which no parasites were detected. No data are available for Volunteer 101 and 106 to validate the model predictions. The source data and computer code with instructions of implementation to generate Figure 2 are fully publicly available at https://doi.org/10.26188/5cde4c26c8201.

![Figure 3.](https://cdn.elifesciences.org/articles/49058/elife-49058-fig3-v1.jpg)

**Figure 3.:** Data are presented by circles. The median of posterior predictions (solid curve) and 95% PI (shaded area) are generated by 5000 model simulations based on 5000 samples from the posterior parameter distribution as described in the Materials and methods. The data points with one parasite/mL (i.e. those points which lie on the dotted line) indicate measurements for which no parasites were detected. The source data and computer code with instructions of implementation to generate Figure 3 are fully publicly available at https://doi.org/10.26188/5cde4c26c8201.

For the majority of asexual parasitemia data the model predictions (median and 95% PI) can faithfully capture the trends of the data (Figure 2), in particular the accurate predictions for both the recrudescent case where a portion of asexual parasitemia data diverge from the total parasitemia measurement (e.g., Volunteer 103, 104, 105, 201, 203, 304 and 307) and the non-recrudescent case where the posterior-median prediction curve (solid red curve) lies below the limit of detection (one asexual parasite/mL) (e.g., Volunteer 202, 301 and 302). However, there are some discrepant observations. The model under-predicts (Volunteer 204) or over-predicts (Volunteer 303, 305 and 306) a portion of the asexual parasitemia data. Furthermore, for some volunteers such as 202, 301 and 302, the 95% PI (red shaded area) extends into the detectable region again after the asexual parasitemia reaches below the detection limit, indicating that there was a small chance that the patients may have suffered a recrudescence during the observation period (of course, they did not) or after the observation period (although this predication cannot be evaluated because artemisinin combination therapy was given immediately after the period).

Figure 3 shows the data and model predictions for the gametocytemia. Despite some discrepant observations for asexual parasitemia in Figure 2, we found that the model predictions of gametocytemia were able to capture the trends and levels of the gametocytemia data for all 17 volunteers.

### Estimation of gametocyte dynamics parameters

The model calibration process provided the joint posterior density for the model parameters, which were used to estimate some key biological parameters governing the dynamics of P. falciparum gametocytes (detailed in the Materials and methods). As shown in Table 1, the sexual commitment rate — the percentage of asexual parasites entering sexual development during each asexual replication cycle — is estimated to be 0.54%/asexual replication cycle (95% credible interval (CI): 0.30–1.00%). This in vivo estimate of 0.54%/asexual replication cycle is much lower than 11%/asexual replication cycle that was estimated from in vitro data (Filarsky et al., 2018). The proportion of committed asexual parasites that survive to become mature gametocytes, calculated by discounting the sexual commitment rate by the probability of survival from the immature (stages I–IV) to mature (stage V) gametocyte life-stage, is 0.52%/asexual replication cycle (95% CI: 0.28–0.95%). The gametocyte sequestration time is the average time that immature gametocytes (stages I–IV) cannot be observed in the peripheral circulation. They re-emerge in the peripheral circulation as mature gametocytes (stage V). It was estimated to be 8.39 days (95% CI: 6.54–10.59 days). The estimate for the circulating gametocyte lifespan is 63.5 days, with a broad 95% CI (12.7–1513.9 days) resulting from the long-tailed posterior distribution (Figure 1—figure supplement 15) and is much longer than the previous in vitro estimate of 16–32 days (Gebru et al., 2017) (note that our lower bound of the 95% CI is lower than the in vitro estimated range). The wide estimate for the circulating gametocyte lifespan, and in particular the high upper bound of the 95% CI, is due to the limited observation time in the VIS which does not enable the lifespan to be accurately determined (explored in more detail in the Discussion).

As shown in Table 1, there are similarities in parameter estimates for P. falciparum between our analysis and the analysis of historical neurosyphilis patient data (Eichner et al., 2001). We found that they exhibited similar in vivo sexual commitment rate (median 0.54%/asexual replication cycle vs. mean 0.64%/asexual replication cycle with overlapping plausible ranges) and gametocyte sequestration time (median 8.39 days vs. mean 7.4 days with overlapping plausible ranges).

Finally, we provided an estimate for the parasite multiplication factor which is the average number of infected red blood cells produced by a single infected red blood cells after one replication cycle. The parasite multiplication factor is an important parameter that quantifies the net growth of asexual parasites and thus influences the rate of gametocyte generation. Our posterior-median estimate is 21.8 parasites per asexual replication cycle (95% CI: 17.6–26.9), consistent with previous estimates which lie in the range 10–33 (Wockner et al., 2017), and a bit larger than an updated estimate calculated from a pooled analysis of parasite counts from 177 volunteers infected with the same P. falciparum strain using a statistical model (16.4 parasites per asexual replication cycle) (JS McCarthy, personal communication, May 2019).

### Predicting the impact of gametocyte kinetics on human-to-mosquito transmissibility

Having validated our mathematical model of asexual parasitemia and gametocyte dynamics, we were able to predict how the gametocyte dynamics parameters influence the transmissibility of P. falciparum malaria from humans to mosquitoes in various epidemiological scenarios. In particular, we focused on the early phase of infection where the innate immune response is minimal and treatment has not been administered (in order to avoid complications that our mathematical model was not designed to capture). Two scenarios were considered:

![Figure 4.](https://cdn.elifesciences.org/articles/49058/elife-49058-fig4-v1.jpg)

**Figure 4.:** (A) illustration of the first scenario: predicting the critical gametocytemia level (indicated by Gc) at the time when the total parasitemia reaches 108 parasites/mL. (B) illustration of the second scenario: predicting the non-infectious period (indicated by tc), which is defined to be time from inoculation of infected red blood cells to the time when the gametocytemia reaches 103 parasites/mL (a threshold below which human-to-mosquito transmission was not observed [Collins et al., 2018]). (C and D) Heatmaps showing the dependence of the critical gametocytemia Gc and the non-infectious period tc on the sexual commitment rate and gametocyte sequestration time. The black dots represent the value obtained by simulating the gametocyte dynamics model using the median estimates of the posterior samples of the population mean parameters as described in the Materials and methods. The red curve in C is the level curve for Gc = 103 parasites/mL. The red curve in D is the level curve for tc = 13.42 days which is the non-infectious period obtained by model simulation using the posterior estimates of the population mean parameters. The source data and computer code with instruction of implementation to generate Figure 4 are fully publicly available at https://doi.org/10.26188/5cde4c26c8201.

A higher sexual commitment rate or a lower gametocyte sequestration time leads to a higher gametocytemia (Gc) at the time of hospitalization (Figure 4C). The red curve in Figure 4C indicates the level curve of 103 gametocytes/mL (i.e., the threshold for infectiousness as mentioned above) dividing the heatmap into two regions. To the left, Gc is below 103 gametocytes/mL, suggesting clinical presentation precedes infectiousness, while to the right Gc is above 103 gametocytes/mL and the converse applies. The Gc value obtained by model simulation using the median estimates of the population mean parameters (indicated by the black dot) is below 103 gametocytes/mL, suggesting that newly hospitalized malaria patients are less likely to be infectious, and thus efforts to identify and treat infections in a timely manner may have a substantial impact in terms of reduced transmission potential. Note that patients from clinical observations of uncomplicated malaria in endemic settings may have higher gametocyte counts at the time of presentation than what our model predicts. For example one study from the TRACII clinical trial reported a range of 16–5120 gametocytes/µL, which is much higher than our prediction of below one gametocytes/µL (or 103 gametocytes/mL) (van der Pluijm et al., 2019). One plausible explanation for the difference is that our model predicted a very fast rise in total parasitemia to 108 parasites/mL while the rise in parasitemia among patients in endemic settings may be slower due to the effect of immunity on the parasite multiplication. Immunity was not considered in our model due to the design of our VIS where only malaria naïve volunteers were recruited.

Figure 4D reinforces the result in Figure 4C using the non-infectious period (tc). As the sexual commitment rate increases or the gametocyte sequestration time decreases, tc decreases. However, for large values of the sexual commitment rate (e.g., >20%), we observed an increase in tc as the sexual commitment rate increases (see the top-right corner of ). This is because an increased sexual commitment rate leads to both a decrease in the rate of asexual parasite growth (due to a direct loss of asexual parasites as they convert to gametocytes) and an increase in the number of sexually committed parasites. For a very high sexual commitment rate, the impact of the former more than counterbalances that of the latter.

## Discussion

We have developed a novel mathematical model of gametocyte dynamics that combines an existing multi-state asexual cycle model with a new model for the development of gametocytes. Model parameters were estimated by fitting the model to data from 17 malaria-naïve volunteers inoculated with P. falciparum-infected red blood cells (3D7 strain). Compared to previous studies, our work is distinguished by three novel contributions: (1) the use of a prospectively planned clinical trial to collect more accurate quantitative data of parasite levels measured by qPCR; (2) the development of a novel dynamics mathematical model which allows for robust and biologically-informed extrapolation and hypothesis testing/scenario analysis; and (3) the use of a Bayesian hierarchical inference method for model calibration and parameter estimation.

For gametocyte kinetic parameters, we found that our in vivo estimate of the P. falciparum sexual commitment rate was similar to that found in the neurosyphilis patient data (Eichner et al., 2001) but was much smaller than previous in vitro estimates (Table 1). Importantly, our estimate follows directly from the structure of our mathematical model, and accounts for the fact that some early committed gametocytes may not complete development and thus not emerge in peripheral circulation as mature gametocytes. Novel VIS data using biomarkers specific to early sexual parasites (e.g. AP2-G [Bancells et al., 2019] and PfGEXP5 [Tibúrcio et al., 2015]) would enable a direct (statistical) estimate of the sexual commitment rate, providing an independent validation of our gametocyte dynamics model. Our in vivo estimate for the circulating gametocyte lifespan is imprecise (i.e., has a very wide credible interval) due to the lack of available data for gametocyte clearance (treatment was initiated before gametocyte were naturally cleared in the VIS study). P. falciparum data with gametocytemia measurements over a longer period of time to capture the natural decay of circulating gametocytes, would greatly improve these estimates.

We also predicted the effects of altered gametocyte kinetic parameters on the transmissibility from humans to mosquitoes, focusing on two scenarios: the infectiousness of newly hospitalized clinical malaria cases (i.e., the gametocytemia when total parasitemia first reaches a level typically seen upon hospitalization — 108 parasites/mL in the model); and the non-infectious period of malaria patients (i.e., the time from the inoculation of infected red blood cells to the time when the gametocytemia reaches a minimal transmission threshold of 103 parasites/mL in the model). We explored how the sexual commitment rate and gametocyte sequestration time influenced the gametocyte level and the non-infectious period. We would like to emphasize that human-to-mosquito transmissibility is determined by both the level of gametocytemia and the relationship between gametocytemia and the probability of transmission per bite. A reliable prediction of the former is essential but not a sole determinant of transmissibility. Therefore, it is also important to improve our quantitative understanding of the probability of transmission per bite, which may be complicated by and also influenced by the densities and ratios of female and male gametocytes (Bradley et al., 2018; Churcher et al., 2013; Da et al., 2015).

Our study has some limitations. The gametocyte dynamics model, that has been shown to have sufficient complexity to reproduce the clinical observations, is still a rather coarse simplification of the actual biological processes. For example, the model does not assume an adaptive sexual commitment rate (Schneider et al., 2018), nor does it consider the mechanisms of sexual commitment (Bancells et al., 2019). Furthermore, the model assumes a constant gametocyte death rate but does not consider other non-constant formulations as have been previously proposed (Diebner et al., 2000). Another limitation is that we assumed a fixed duration for the asexual replication cycle of 42 hr, while previous work by our group suggests that the replication cycle may be altered by up to a few hours in response to antimalarial drugs (e.g., artemisinin [Cao et al., 2017; Dogovski et al., 2015]), though there is no evidence that piperaquine (which was administered in this VIS) has a similar effect.

In conclusion, we have developed a novel mathematical model of gametocyte dynamics, and demonstrated that it reliably predicts time series data of gametocytemia. The model provides a powerful predictive tool for informing the design of future volunteer infection studies which aim to test transmission-blocking interventions. Furthermore, the within human host transmission model can be incorporated into epidemiological-scale models to refine predictions of the impacts of various antimalarial treatments and transmission interventions.

## Materials and methods

### Study population and measurements

The data used in this modeling study are from a previously published VIS (Collins et al., 2018) where 17 malaria-naïve volunteers were inoculated with approximately 2800 P. falciparum-infected red blood cells (3D7 strain). The study was approved by the QIMR Berghofer Human Research Ethics Committee and registered with ClinicalTrials.gov (NCT02431637 and NCT02431650). The volunteers were treated with 480 mg piperaquine phosphate (PQP) on day 7 or 8 post-inoculation to attenuate asexual parasite growth and a second dose of 960 mg PQP was given to any volunteer for treatment of recrudescent asexual parasitemia. All volunteers received a course of artemether/lumefantrine and, if required, a single dose of primaquine (45 mg) to clear all parasites. Parasitemia in the volunteers was monitored approximately daily following inoculation, but with notable variability in the frequency of data collection at later times as described by Collins et al. (2018).

Molecular analysis of parasite levels was carried out throughout the study. The total parasitemia was measured by 18S qPCR (total circulating asexual parasites and gametocytes per mL blood), asexual parasitemia was measured by SBP1 qRT-PCR (circulating asexual parasites per mL blood), and gametocytemia was measured by Pfs25 and PfMGET qRT-PCR (circulating female and male gametocytes per mL blood). Plasma concentrations of PQP were also determined at multiple time points after inoculation. Further details about the VIS are given in Collins et al. (2018). It is important to note that the data used in model fitting is the total parasitemia (from the first measurement to the time before any treatment other than PQP) and the other data, that is asexual parasitemia and gametocytemia (also up to the time of treatment other than PQP) are used to validate the model.

### Gametocyte dynamics model

The mathematical model extends the published models of asexual parasite replication cycle (Saralamba et al., 2011; Zaloumis et al., 2012) by incorporating the development of gametocytes. The model is comprised of three parts describing three populations of parasites: asexual parasites (P), sexually committed parasites (PG) and gametocytes (G). A schematic diagram of the development of those populations based on current knowledge (Bancells et al., 2019; Filarsky et al., 2018) is shown in Figure 5.

![Figure 5.](https://cdn.elifesciences.org/articles/49058/elife-49058-fig5-v1.jpg)

**Figure 5.:** The model is comprised of three parts describing three populations of parasites: asexual parasites ($Pa,t$), sexually committed parasites ($P_{G}a,t$) and gametocytes ($Gt$). P and PG are functions of asexual parasite age $a$ and time $t$. Square compartments in the inner loop represent the asexual parasite population which follows a cycle of maturation and replication every $a_{L}$ hours. Sexual commitment occurs from age $a_{s}$ and a fraction of asexual parasites become sexually committed (the bigger square compartments in the outer loop) and eventually enter the development of stage I–V gametocytes (G1–G5). The compartments with a dashed boundary are sequestered to tissues and thus not measurable in a blood smear. The notation for each compartment is consistent with those in the model equations and is explained in the main text.

Asexual parasites develop and replicate in the red blood cells (RBCs) until cell rupture at the end of each replication cycle and the released free parasites (merozoites) can initiate new cycles of replication if they successfully invade susceptible RBCs. At the time of inoculation (i.e., $t=0$ hours in the model), we define the inoculum size to be $P_{init}$ and assume the age distribution of inoculated parasites is Gaussian with mean μ and standard deviation $\sigma$. As time increments by one hour, the asexual parasites of age $a$ at time $t$ (denoted as $P(a,t)$) follow the iterative equation:

$$
P(a,t)={P(a−1,t−1)e^{−k_{d}¯−\delta_{P}},a=2,3,...,a_{L}r_{P}P(a_{L},t−1)e^{−k_{d}¯−\delta_{P}},a=1
$$

where $k_{d}¯$ represents the average rate of asexual parasite killing by PQP and $\delta_{P}$ is the rate of asexual parasite death due to processes other than PQP. $k_{d}¯$ is approximated by the average of $k_{d}(t-1)$ and $k_{d}(t)$ and $k_{d}t=k_{max}Ct^{\gamma}/(Ct^{\gamma}+EC_{50}^{\gamma})$ where $k_{max}$ is the maximum killing rate, $EC_{50}$ is the PQP concentration at which half maximum killing is achieved, and $\gamma$ is the Hill coefficient determining the curvature of the dose-response curve. $Ct$ is the PQP concentration which is simulated by a pharmacokinetic model introduced below. $a_{L}$ is the length of each asexual replication cycle and $r_{P}$ is the parasite replication rate indicating the average number of newly infected RBCs attributable to the rupture of a single infected RBC. Note that we distinguish the parasite replication rate $r_{P}$ from the so-called parasite multiplication factor, the latter of which is a 'net replication rate' quantified by the (per cycle) increase in parasite numbers due to replication ($r_{P}$) and the decrease in parasite numbers due to death or sexual commitment. Sexual commitment is assumed to occur at the first age of the trophozoite stage (denoted to be $a_{s}$) and a fraction ($f$) of asexual parasites leave the asexual replication cycle and start sexual development in the next hour, which is modeled by

$$
P(a_{s}+1,t)=(1−f)P(a_{s},t−1)e^{−k_{d}¯−\delta_{P}}
$$



$$
P_{G}(a_{s}+1,t)=fP(a_{s},t−1)e^{−k_{d}¯−\delta_{P}}.
$$

The first equation describes the proportion of parasites remaining in the asexual replication cycle while the second equation describes the proportion of parasites becoming sexually committed parasites ($P_{G}$). According to Figure 5, the sexually committed parasites continue the rest of the replication cycle and a part of the next replication cycle (note that they appear indistinguishable from asexual parasites by microscopy) before becoming stage I gametocytes. The process is modeled by

$$
P(a,t)={P(a−1,t−1)e^{−\delta_{P}},a=2,3,...,a_{L}excepta=a_{s}anda=a_{s}+1r_{P}P(a_{L},t−1)e^{−\delta_{P}},a=1
$$

Note that we assumed in our model that PQP does not kill gametocytes. Our assumption was based on evidence from both in vitro and in vivo experiments that suggests that PQP has little activity against sexually committed parasites and gametocytes (Collins et al., 2018; Pasay et al., 2016; Bolscher et al., 2015), although we note there is some evidence that PQP might have activity against early-stage I/II gametocytes (Adjalley et al., 2011). The changes of the sequestered stage I–IV gametocytes ($G_{1}$–$G_{4}$) are governed by difference equations

$$
G_{1}(t)=G_{1}(t−1)e^{−(m+\delta_{G})}+\frac{P_{G}(a_{s}−1,t−1)e^{−\delta_{P}}(1−e^{−(m+\delta_{G})})}{m+\delta_{G}},
$$



$$
G_{2}(t)=G_{2}(t−1)e^{−(m+\delta_{G})}+\frac{mG_{1}(t−1)(1−e^{−(m+\delta_{G})})}{m+\delta_{G}},
$$



$$
G_{3}(t)=G_{3}(t−1)e^{−(m+\delta_{G})}+\frac{mG_{2}(t−1)(1−e^{−(m+\delta_{G})})}{m+\delta_{G}},
$$



$$
G_{4}(t)=G_{4}(t−1)e^{−(m+\delta_{G})}+\frac{mG_{3}(t−1)(1−e^{−(m+\delta_{G})})}{m+\delta_{G}},
$$

where m is the rate of gametocyte maturation and $\delta_{G}$ is the death rate of sequestered gametocytes. Stage V gametocytes are circulating in bloodstream (and therefore can be measured from the peripheral blood film) modeled by

$$
G_{5}(t)=G_{5}(t−1)e^{−\delta_{Gm}}+\frac{mG_{4}(t−1)(1−e^{−\delta_{Gm}})}{\delta_{Gm}},
$$

where $\delta_{Gm}$ is the death rate of mature circulating gametocytes.

The total parasitemia in the model is given by $\sum_{a=1}^{a=a_{s}-1}Pa,t+P_{G}a,t+G_{5}(t)$, which was fitted to the VIS data. After model fitting, we simulated the asexual parasitemia $\sum_{a=1}^{a=a_{s}-1}P(a,t)$ and gametocytemia $G_{5}(t)$ and compared them with associated data for model validation. Table 2 presents all the model parameters and their units and descriptions.

**Table 2.**
 Details of the gametocyte dynamics model parameters.The table includes the unit, description and prior distribution for each model parameter. For the uniform prior distributions (U), the lower bounds are non-negative based on the definitions of the model parameters and the upper bounds for the prior distributions were chosen to be sufficiently wide in order to accommodate all biologically plausible values from the literature (Zaloumis et al., 2012). We assumed parasites younger than 25h are circulating and thus fix $a_{s}$ to be 25h. For 3D7 strain, the asexual replication cycle is approximately 39–45h (based on in vitro estimates [Duffy and Avery, 2017] and personal communication [JS McCarthy, personal communication, May 2019]) and we fix $a_{L}$ to be 42h.


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Unit</th>
      <th>Description</th>
      <th>Prior distribution</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Pinit</td>
      <td>parasites/mL</td>
      <td>inoculation size</td>
      <td>U(0, 10)</td>
    </tr>
    <tr>
      <td>μ</td>
      <td>h</td>
      <td>mean of the initial parasite age distribution</td>
      <td>U(0, 35)</td>
    </tr>
    <tr>
      <td>σ</td>
      <td>h</td>
      <td>SD of the initial parasite age distribution</td>
      <td>U(0, 20)</td>
    </tr>
    <tr>
      <td>rP</td>
      <td>(unitless)</td>
      <td>parasite replication rate</td>
      <td>U(0, 100)</td>
    </tr>
    <tr>
      <td>kmax</td>
      <td>h−1</td>
      <td>maximum rate of parasite killing by PQP</td>
      <td>U(0, 1)</td>
    </tr>
    <tr>
      <td>EC50</td>
      <td>ng/mL</td>
      <td>half-maximum effective PQP concentration</td>
      <td>U(1, 100)</td>
    </tr>
    <tr>
      <td>γ</td>
      <td>(unitless)</td>
      <td>Hill coefficient for PQP</td>
      <td>U(0, 20)</td>
    </tr>
    <tr>
      <td>f</td>
      <td>(unitless)</td>
      <td>the fraction of parasites entering sexual development per asexual replication cycle</td>
      <td>U(0, 1)</td>
    </tr>
    <tr>
      <td>δP</td>
      <td>h−1</td>
      <td>death rate of asexual and sexual parasites</td>
      <td>U(0, 0.2)</td>
    </tr>
    <tr>
      <td>m</td>
      <td>h−1</td>
      <td>maturation rate of gametocytes</td>
      <td>U(0, 0.1)</td>
    </tr>
    <tr>
      <td>δG</td>
      <td>h−1</td>
      <td>death rate of sequestered gametocytes</td>
      <td>U(0, 0.1)</td>
    </tr>
    <tr>
      <td>δGm</td>
      <td>h−1</td>
      <td>death rate of circulating gametocytes</td>
      <td>U(0, 0.1)</td>
    </tr>
    <tr>
      <td>as</td>
      <td>h</td>
      <td>sequestration age of asexual parasites</td>
      <td>fixed to be 25</td>
    </tr>
    <tr>
      <td>aL</td>
      <td>h</td>
      <td>length of life cycle of asexual parasites</td>
      <td>fixed to be 42</td>
    </tr>
  </tbody>
</table>

_SD: standard deviation; h: hour._

### Pharmacokinetic model of piperaquine (PQP)

In the within-host model, the killing rate $k_{d}(t)$ is determined by PQP concentration $Ct$ which was simulated from a pharmacokinetic (PK) model introduced in this section. The PK model, provided by Thanaporn Wattanakul and Joel Tarning (Mahidol-Oxford Tropical Medicine Research Unit, Bangkok), is a three-compartment disposition model with two transit compartments for absorption (see the schematic diagram in Figure 6).

![Figure 6.](https://cdn.elifesciences.org/articles/49058/elife-49058-fig6-v1.jpg)

**Figure 6.:** The model is a three-compartment disposition model with two transit compartments for absorption. State D represents the dose of PQP. T1 and T2 represent the two transit compartments. C is the central compartment and PQP concentration in this compartment was measured (which are shown in Figure 6—figure supplement 1). P1 and P2 represent two peripheral compartments. kT, q1, q2 and qc are the rates of flow into or out of compartments.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/49058/elife-49058-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** The details of the optimization approach are provided in the Materials and methods in the main text and Appendix 1. Some volunteers have two peaks of PQP concentrations because they had recrudescent asexual parasitemia (see Figure 1 in the main text) and were treated with a second dose of 960 mg PQP. The source data and computer code with instructions of implementation to generate Figure 6—figure supplement 1 are fully publicly available at https://doi.org/10.26188/5cde4c26c8201.

Based on Figure 6, the model is formulated to be a system of ordinary differential equations:

$$
\frac{dD}{dt}=−k_{T}D,
$$



$$
\frac{dT_{1}}{dt}=k_{T}D−k_{T}T_{1},
$$



$$
\frac{dT_{2}}{dt}=k_{T}T_{1}−k_{T}T_{2},
$$



$$
\frac{dC}{dt}=\frac{k_{T}T_{2}+q_{1}P_{1}+q_{2}P_{2}−q_{1}C−q_{2}C−q_{c}C}{V_{c}}_{ },
$$



$$
\frac{dP_{1}}{dt}=\frac{q_{1}C−q_{1}P_{1}}{V_{1}}_{ },
$$



$$
\frac{dP_{2}}{dt}=\frac{q_{2}C−q_{2}P_{2}}{V_{2}}_{ },
$$

where $k_{T}$ and $q$’s are rate constants as shown in Figure 6 and $V_{c}$, $V_{1}$ and $V_{2}$ are the volume of distribution for the central compartment (in which PQP concentration is C), peripheral compartment 1 (in which PQP concentration is P1) and peripheral compartment 2 (in which PQP concentration is P2) respectively.

Under the sequential pharmacokinetic-pharmacodynamic (PK-PD) approach we have taken, a PQP concentration curve (C(t)) for each volunteer is a required input into the gametocyte dynamics model. The VIS, with its limited sampling of PQP for each volunteer, was not designed to provide this PQP concentration curve directly, so we used a PK model, informed by data from a previous VIS with rich sampling. We drew on an analysis of that previous VIS by Thanaporn Wattanakul and Joel Tarning (unpublished data and estimates). Their analysis provides population-level PQP PK model parameter estimates.

We used MATLAB’s (version 2016b; The MathWorks, Natick, MA) built-in least-squares optimizer lsqcurvefit (with the default setting) to optimize the PK curve for each volunteer in the VIS study. We applied the optimizer to each volunteer’s (limited) PQP data, using the parameter estimates provided by Thanaporn Wattanakul and Joel Tarning as initial values. We applied some further model parameter constraints as specified in Appendix 1. This approach provided us with a data-informed PK curve for each volunteer in the VIS, sufficient for our primary purpose of studying the asexual and sexual parasite dynamics. Of note, Volunteers 202, 301, 302 or 307 had fewer PK data points than PK model parameters, preventing application of this optimization procedure. For these volunteers, their predicted PQP PK curve was derived using the population-level mean PK parameter from Wattanakul and Tarning’s analysis. The MATLAB code (with detailed comments) is publicly available at https://doi.org/10.26188/5cde4c26c8201 The details of the initial conditions, starting point and constraints for the PK curve optimization procedure are provided in Appendix 1. The optimized PK curves and associated parameter values for all volunteers are provided in Figure 6—figure supplement 1 and Appendix 1.

### Fitting the model to parasitemia data

We took a Bayesian hierarchical modeling approach (Gelman et al., 2013) to fit the gametocyte dynamics model to the data from all 17 volunteers. In detail, each volunteer has 12 model parameters (i.e., those in Table 2 except $a_{s}$ and $a_{L}$; also called the individual parameters) and lower and upper bounds of the parameters are given in Table 2. If denoting the individual parameters to be $\theta_{ind}$and lower and upper bounds to be $b_{L}$ and $b_{U}$ respectively, the following transformations are used to convert the bounded individual parameters to unbounded ones (denoted by $\phi_{ind}$) in order to in order to improve computational efficiency (Lesaffre et al., 2007; Stan Development Team, 2017):

$$
\phi_{ind}=ln⁡(\frac{\theta_{ind}−b_{L}}{b_{U}−\theta_{ind}}),
$$

o$\phi_{ind}$ beys a multivariate normal distribution $𝒩$($\phi_{pop}$, $Ω_{pop}$) where

$$
\phi_{pop}=ln⁡(\frac{\theta_{pop}−b_{L}}{b_{U}−\theta_{pop}})
$$

and $\theta_{pop}$ is a vector containing 12 population mean parameters (hyperparameters) corresponding to the 12 gametocyte dynamics model parameters. $Ω_{pop}$ is the covariance matrix. For more efficient sampling process, $\phi_{ind}~𝒩$($\phi_{pop}$, $Ω_{pop}$) was reparameterised to a non-centerd form $\phi_{ind}=\phi_{pop}+\omega_{pop}Lη$, where $\omega_{pop}$ is the diagonal standard deviation (SD) matrix whose diagonal elements are the 12 population SD parameters (hyperparameters); $L$ is the lower Cholesky factor of the correlation matrix; $η$ obeys standard multivariate normal distribution. Note that $Ω_{pop}=\omega_{pop}LL^{T}\omega_{pop}$ where $LL^{T}$ is the correlation matrix. The prior distributions for the 12 population mean parameters $\theta_{pop}$ are given by uniform distributions with bounds given in Table 2. The prior distribution for the 12 population SD parameters is standard half-normal and the prior distribution for the lower Cholesky factor of the correlation matrix $L$ is given by Cholesky LKJ correlation distribution with shape parameter of 2 (Lewandowski et al., 2009; Stan Development Team, 2017). The distribution of the observed parasitemia measurements is assumed to be a log normal distribution with mean given by the model-simulated values and SD parameter with prior distribution of a half-Cauchy distribution with a location parameter of zero and a scale parameter of 5. The distribution for the observed parasitemia measurements was used to calculate the likelihood function and the M3 method (Ahn et al., 2008) was used to penalise the likelihood for data points below the limit of detection for the total parasitemia (10 parasites/mL; Collins et al., 2018).

Model fitting was implemented in R (version 3.2.3) (R Development Core Team, 2017) and Stan (RStan 2.17.3) (Stan Development Team, 2017) using the Hamiltonian Monte Carlo (HMC) optimized by the No-U-Turn Sampler (NUTS) to draw samples from the joint posterior distribution of the parameters including the individual parameters (12 parameters for each volunteer) and population mean parameters (12 hyperparameters). Five chains with different starting points (set by different random seeds) were implemented and 1000 posterior samples retained from each chain after a burn-in of 1000 iterations (in total 5000 samples were drawn from the joint posterior distribution). The marginal posterior and prior distributions of the population mean and SD parameters are shown in Figure 1—figure supplements 1 and 2. The marginal posterior distributions of the individual parameters for all 17 volunteers are shown in Figure 1—figure supplements 3–14 (using violin plots). For each volunteer, the 5000 sets of individual parameters are used to simulate the gametocyte dynamics model and generate 5000 simulated model outputs (e.g., 5000 time series of total parasitemia, asexual parasitemia or gametocytemia). The posterior prediction and 95% prediction interval (PI) are given by the median and quantiles of 2.5% and 97.5% of the 5000 model outputs at each time respectively (see Figures 1–3 for example).

The estimates of some key biological parameters (Table 1) were calculated using the 5000 posterior draws of the 12 population mean parameters, that is median and 2.5%- and 97.5%-quantile (95% credible interval). The sexual commitment rate was calculated by $f_{pop}\times100%$ ($f_{pop}$ is the population mean parameter for $f$) and the proportion of committed asexual parasites that survive to become mature gametocytes was calculated by $f_{pop}(m_{pop}/(m_{pop}+\delta_{G}_{pop}))^{4}$ where the factor of four arises due to the four sequestered gametocyte stages (I to IV). Circulating gametocyte lifespan was calculated by $1/\delta_{Gm}_{pop}/24$ (the factor of 24 converts hours into days). Gametocyte sequestration time was calculated by $4/m_{pop}/24$ where 4 indicates four sequestered state (stage I to IV) and 24 converts hours into days. Parasite multiplication factor is calculated by $r_{P}_{pop}exp⁡(-\delta_{P}_{pop}a_{L})(1-f_{pop})$ where the term $exp⁡(-\delta_{P}_{pop}a_{L})(1-f_{pop})$ gives the fraction of surviving asexual parasites after death and sexual conversion per replication cycle.

The gametocyte dynamics model with parameters given by the median estimates of the population mean parameters was used to simulate the two scenarios predicting the dependence of human-to-mosquito transmissibility on the sexual commitment rate and gametocyte sequestration time (Figure 4).

Final analysis and visualization were performed in MATLAB. All computer codes (R, Stan, MATLAB), data and fitting results (CSV and MAT files) and an instruction document (note that reading the document first will make the code much easy to follow) are publicly available at https://doi.org/10.26188/5cde4c26c8201.
