# Inference of the SARS-CoV-2 generation time using UK household data

## Authors

- William S Hart<sup>1</sup> ([ORCID: 0000-0002-2504-6860](https://orcid.org/0000-0002-2504-6860)) †
- Sam Abbott<sup>2</sup>
- Akira Endo<sup>2</sup> ([ORCID: 0000-0001-6377-7296](https://orcid.org/0000-0001-6377-7296))
- Joel Hellewell<sup>2</sup>
- Elizabeth Miller<sup>3</sup> ([ORCID: 0000-0002-1884-0097](https://orcid.org/0000-0002-1884-0097))
- Nick Andrews<sup>5</sup>
- Philip K Maini<sup>1</sup> ([ORCID: 0000-0002-0146-9164](https://orcid.org/0000-0002-0146-9164))
- Sebastian Funk<sup>2</sup> ([ORCID: 0000-0002-2842-3406](https://orcid.org/0000-0002-2842-3406))
- Robin N Thompson<sup>6</sup> ([ORCID: 0000-0001-8545-5212](https://orcid.org/0000-0001-8545-5212))

### Affiliations

1. Mathematical Institute, University of Oxford Oxford United Kingdom ([ROR:052gg0110](https://ror.org/052gg0110))
2. Centre for the Mathematical Modelling of Infectious Diseases, London School of Hygiene and Tropical Medicine London United Kingdom ([ROR:00a0jsq62](https://ror.org/00a0jsq62))
3. Department of Infectious Disease Epidemiology, London School of Hygiene and Tropical Medicine London United Kingdom ([ROR:00a0jsq62](https://ror.org/00a0jsq62))
4. Immunisation and Countermeasures Division, UK Health Security Agency London United Kingdom ([ROR:00vbvha87](https://ror.org/00vbvha87))
5. Data and Analytical Sciences, UK Health Security Agency London United Kingdom
6. Mathematics Institute, University of Warwick Coventry United Kingdom ([ROR:01a77tt86](https://ror.org/01a77tt86))
7. Zeeman Institute for Systems Biology and Infectious Disease Epidemiology Research, University of Warwick Coventry United Kingdom ([ROR:01a77tt86](https://ror.org/01a77tt86))

† Corresponding author

## Abstract

The distribution of the generation time (the interval between individuals becoming infected and transmitting the virus) characterises changes in the transmission risk during SARS-CoV-2 infections. Inferring the generation time distribution is essential to plan and assess public health measures. We previously developed a mechanistic approach for estimating the generation time, which provided an improved fit to data from the early months of the COVID-19 pandemic (December 2019-March 2020) compared to existing models (Hart et al., 2021). However, few estimates of the generation time exist based on data from later in the pandemic. Here, using data from a household study conducted from March to November 2020 in the UK, we provide updated estimates of the generation time. We considered both a commonly used approach in which the transmission risk is assumed to be independent of when symptoms develop, and our mechanistic model in which transmission and symptoms are linked explicitly. Assuming independent transmission and symptoms, we estimated a mean generation time (4.2 days, 95% credible interval 3.3–5.3 days) similar to previous estimates from other countries, but with a higher standard deviation (4.9 days, 3.0–8.3 days). Using our mechanistic approach, we estimated a longer mean generation time (5.9 days, 5.2–7.0 days) and a similar standard deviation (4.8 days, 4.0–6.3 days). As well as estimating the generation time using data from the entire study period, we also considered whether the generation time varied temporally. Both models suggest a shorter mean generation time in September-November 2020 compared to earlier months. Since the SARS-CoV-2 generation time appears to be changing, further data collection and analysis is necessary to continue to monitor ongoing transmission and inform future public health policy decisions.

## Introduction

The generation time (or generation interval) of a SARS-CoV-2 infector-infectee pair is defined as the period of time between the infector and infectee each becoming infected (Anderson and May, 1992; Diekmann and Heesterbeek, 2000; Griffin et al., 2020; Svensson, 2007; Wallinga and Lipsitch, 2007). The generation time distribution of many infector-infectee pairs characterises the temporal profile of the transmission risk of an infected host (averaged over all hosts and normalised so that it represents a valid probability distribution; Fraser, 2007). Inferring the generation time distribution of SARS-CoV-2 is important in order to predict the effects of non-pharmaceutical interventions such as contact tracing and quarantine (Ashcroft et al., 2021; Ferretti et al., 2020b; Hart et al., 2021). In addition, the generation time distribution is widely used in epidemiological models for estimating the time-dependent reproduction number from case notification data (Abbott et al., 2020; Fraser, 2007; Gostic et al., 2020; Thompson et al., 2020) and is crucial for understanding the relationship between the reproduction number and the epidemic growth rate (Fraser, 2007; Parag et al., 2021; Park et al., 2020a; Wallinga and Lipsitch, 2007).

The SARS-CoV-2 generation time distribution has previously been estimated using data from known infector-infectee transmission pairs (Ferretti et al., 2020a; Ferretti et al., 2020b; Hart et al., 2021) or entire clusters of cases (Ganyani et al., 2020; Hu et al., 2021; Sun et al., 2021). These studies involved data (Cheng et al., 2020; Ferretti et al., 2020b; Ganyani et al., 2020; He et al., 2020; Xia et al., 2020; Zhang et al., 2020) collected between December 2019 and April 2020, almost entirely from countries in East and Southeast Asia (with the exception of four transmission pairs from Germany and four from Italy in Ferretti et al., 2020b). Evidence from January and February 2020 in China suggested a temporal reduction in the mean generation time due to non-pharmaceutical interventions (Sun et al., 2021). Specifically, effective isolation of infected individuals is likely to have reduced the proportion of transmissions occurring when potential infectors were in the later stages of infection, thereby shortening the generation time (Sun et al., 2021). Similarly, two other studies found a decrease in the serial interval (the difference between symptom onset times of an infector and infectee; Ali et al., 2020) and an increase in the proportion of presymptomatic transmissions (Bushman et al., 2021) in China over the same time period, which can be attributed to symptomatic hosts being isolated increasingly quickly over time.

Despite estimation of the SARS-CoV-2 generation time in Asia early in the pandemic, relatively little is known about the generation time distribution outside Asia, and whether or not any changes have occurred in the generation time since the early months of the pandemic. At the time of writing, we are aware of only one previous study in which the generation time was estimated using data from the UK (Challen et al., 2021). In that study (Challen et al., 2021), data describing symptom onset dates for 50 infector-infectee pairs, collected by Public Health England (PHE; now the UK Health Security Agency) between January and March 2020 as part of the ‘First Few Hundred’ case protocol (Boddington et al., 2021; Public Health England, 2020), were used to infer the generation time distribution. However, since these transmission pairs mostly consisted of international travellers and their household contacts, the authors concluded that their estimates of the generation time may have been biased downwards due to enhanced surveillance and isolation of these cases (Challen et al., 2021).

Here, we use data from a household study (Miller et al., 2021), conducted between March and November 2020, to estimate the SARS-CoV-2 generation time distribution in the UK under two different underlying transmission models. In the first model (the ‘independent transmission and symptoms model’), a parsimonious assumption is made that the generation time and the incubation period of the infector are independent (i.e. there is no link between the times at which infectors transmit the virus and the times at which they develop symptoms), as has often been employed in studies in which the SARS-CoV-2 generation time has been estimated (Challen et al., 2021; Ferretti et al., 2020a; Ganyani et al., 2020; Hart et al., 2021; Lehtinen et al., 2021; Table 1). In the second model (the ‘mechanistic model’), we use a mechanistic approach in which potential infectors progress through different stages of infection, first becoming infectious before developing symptoms (Hart et al., 2021). Infectiousness is therefore explicitly linked to symptoms in the mechanistic model. A feature of the mechanistic model is that individuals with longer incubation periods will (on average) be infectious for longer before developing symptoms, and so generate more transmissions, compared to those with shorter incubation periods.

By fitting separately to data from three different time intervals within the study period, we explore whether or not there was a detectable temporal change in the generation time distribution.

**Table 1.**
 Previous SARS-CoV-2 generation time estimates.Estimates of the mean and standard deviation of the generation time distribution, obtained under the assumption of independent transmission and symptoms. 95% credible intervals are shown in brackets where available.


<table>
  <thead>
    <tr>
      <th>Study</th>
      <th>Location</th>
      <th>Time period</th>
      <th>Mean generation time (days)</th>
      <th>Standard deviation of generation time distribution (days)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Ferretti et al., 2020b</td>
      <td>Various</td>
      <td>December 2019-February 2020</td>
      <td>5.0</td>
      <td>1.9</td>
    </tr>
    <tr>
      <td>Ganyani et al., 2020</td>
      <td>Singapore</td>
      <td>January-February 2020</td>
      <td>5.20 (3.78–6.78)</td>
      <td>1.72 (0.91–3.93)</td>
    </tr>
    <tr>
      <td>Ganyani et al., 2020</td>
      <td>China</td>
      <td>January-February 2020</td>
      <td>3.95 (3.01–4.91)</td>
      <td>1.51 (0.74–2.97)</td>
    </tr>
    <tr>
      <td>Hart et al., 2021</td>
      <td>Various</td>
      <td>December 2019-March 2020</td>
      <td>5.57 (5.08–6.09)</td>
      <td>2.32 (1.83–2.91)</td>
    </tr>
    <tr>
      <td>Ferretti et al., 2020a</td>
      <td>Various</td>
      <td>December 2019-March 2020</td>
      <td>5.5</td>
      <td>1.8</td>
    </tr>
    <tr>
      <td>Challen et al., 2021</td>
      <td>UK</td>
      <td>January-March 2020</td>
      <td>4.8 (4.3–5.41)</td>
      <td>1.7 (1.0–2.6)</td>
    </tr>
  </tbody>
</table>

## Results

### Inferring the generation time from UK household data

We fitted two models of infectiousness (the independent transmission and symptoms model and the mechanistic model) to data collected from 172 UK households in a study (Miller et al., 2021) conducted by PHE between March and November 2020 (Figure 1—source data 1). Each household was recruited to the study following a confirmed SARS-CoV-2 infection, and all household members were then followed to investigate whether or not they became infected (this was determined through PCR and antibody testing). If a household member was infected and developed symptoms, their symptom onset date was recorded (see Methods).

In our previous work (Hart et al., 2021), we fitted the same two models of infectiousness to data from infector-infectee transmission pairs collected in the early months of the COVID-19 pandemic. Here, we adapted the approach presented in that article (Hart et al., 2021) in order to estimate the generation time using household transmission data. Specifically, we used data augmentation MCMC, augmenting the observed data with both estimated times of infection and estimated precise times at which symptomatic infected hosts developed symptoms (within recorded symptom onset dates). This enabled us (in the likelihood function) to account for uncertainty about exactly who-infected-whom within a household by summing together likelihood contributions corresponding to infection by different possible infectors. In addition, we corrected for the regularity of household contacts to derive more widely applicable estimates of the generation time. We did this by including a factor in the likelihood to account for each infected individual avoiding infection from household contacts that occurred prior to their actual time of infection (see Methods for full details of our approach).

For the two fitted models, we calculated posterior estimates of the mean (Figure 1A) and standard deviation (Figure 1B) of the generation time distribution, in addition to the proportion of transmissions occurring prior to symptom onset (among infectors who develop symptoms; Figure 1C) and the overall infectiousness parameter, $\beta_{0}$ (see Methods; Figure 1D). Under the commonly used independent transmission and symptoms model, we obtained a point estimate of 4.2 days (95% credible interval (CrI) 3.3–5.3 days) for the mean generation time (Figure 1A, blue violin; we calculated point estimates for each model using the posterior means of fitted model parameters because the mode of the joint posterior distribution could not easily be calculated from the output of the MCMC procedure). This value is similar to a previous estimate obtained using data from China by Ganyani et al., 2020. It is slightly lower than estimates for Singapore obtained by Ganyani et al., 2020 and for several countries (predominantly in Asia) obtained by Ferretti et al., 2020b (Table 1), although those estimates lie within our credible interval. On the other hand, our estimated standard deviation of 4.9 days (95% CrI 3.0–8.3 days; Figure 1B, blue violin) is substantially higher than previous estimates (Table 1). Using our mechanistic model, we obtained a higher estimate for the mean generation time of 5.9 days (95% CrI 5.2–7.0 days; Figure 1A, red violin), and a similar estimate for the standard deviation (4.8 days, 95% CrI 4.0–6.3 days; Figure 1B, red violin), compared to those predicted by the independent transmission and symptoms model.

![Figure 1.](https://cdn.elifesciences.org/articles/70767/elife-70767-fig1-v2.jpg)

**Figure 1.:** Violin plots indicating posterior distributions of the mean (A) and standard deviation (B) of the generation time distribution, proportion of transmissions occurring prior to symptom onset (among infectors who develop symptoms; C), and overall infectiousness parameter, $\beta_{0}$ (describing the expected number of household transmissions generated by a single infected host) in a large, otherwise entirely susceptible, household; D). We show results obtained both using a model in which infectiousness is assumed to be independent of when symptoms develop (‘independent transmission and symptoms model’, blue), and using the mechanistic model from Hart et al., 2021 in which infectiousness is explicitly linked to symptoms (‘mechanistic model’, red).

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/70767/elife-70767-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** Prior distributions (black dashed lines), posterior distributions (blue bars), and posterior means (vertical red dashed lines) of fitted parameters in the independent transmission and symptoms model. (A). Mean generation time. (B). Standard deviation of the generation time distribution. (C). Overall infectiousness, $\beta_{0}$.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/70767/elife-70767-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** Prior distributions (black dashed lines), posterior distributions (blue bars), and posterior means (vertical red dashed lines) of fitted parameters in the mechanistic model. (A). Ratio of mean durations of the latent (E) and incubation (combined E and P) periods, $k_{E}/k_{inc}$. (B). Mean symptomatic infectious (I) period, $1/\mu$. (C). Ratio of transmission rates in the presymptomatic infectious (P) and symptomatic infectious (I) stages of infection, $\alpha_{P}$. (D). Overall infectiousness, $\beta_{0}$.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/70767/elife-70767-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** Using posterior mean parameter estimates, we predicted the distribution of the difference in successive symptom onset dates within households (this differs from the serial interval because an infected individual may not have been infected by the previous household member to develop symptoms) under the fitted independent transmission and symptoms model (red crosses) and mechanistic model (yellow stars). These distributions were compared to the UK household data (blue bars). The distributions for the fitted models were obtained by generating synthetic data from 16,700 households using the same distribution of household sizes as in the UK data.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/70767/elife-70767-fig1-figsupp4-v2.jpg)

**Figure 1—figure supplement 4.:** Violin plots indicating posterior distributions of the mean (A) and standard deviation (B) of realised generation times in the study households, and the realised proportion of transmissions occurring prior to symptom onset (C), for the independent transmission and symptoms model (blue) and mechanistic model (red).

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/70767/elife-70767-fig1-figsupp5-v2.jpg)

**Figure 1—figure supplement 5.:** Violin plots indicating posterior distributions of the mean (A) and standard deviation (B) of the generation time distribution, proportion of transmissions occurring prior to symptom onset (among infectors who develop symptoms; C), overall infectiousness parameter, $\beta_{0}$ (D), and probability of co-primary infection (E), for the independent transmission and symptoms model (blue) and mechanistic model (red), when the possibility of co-primary cases was included in our approach (see the Appendix).

![Figure 1—figure supplement 6.](https://cdn.elifesciences.org/articles/70767/elife-70767-fig1-figsupp6-v2.jpg)

**Figure 1—figure supplement 6.:** Violin plots indicating posterior distributions of the mean (A) and standard deviation (B) of the generation time distribution, proportion of transmissions occurring prior to symptom onset (among infectors who develop symptoms; C), and overall infectiousness parameter, $\beta_{0}$ (D), for the independent transmission and symptoms model, when the generation time was assumed to follow either a lognormal (blue, as in Figure 1) or a gamma (red) distribution, and the incubation period distribution followed a lognormal distribution (as in Figure 1).

![Figure 1—figure supplement 7.](https://cdn.elifesciences.org/articles/70767/elife-70767-fig1-figsupp7-v2.jpg)

**Figure 1—figure supplement 7.:** Violin plots indicating posterior distributions of the mean (A) and standard deviation (B) of the generation time distribution, proportion of transmissions occurring prior to symptom onset (among infectors who develop symptoms; C), and overall infectiousness parameter, $\beta_{0}$ (D), for the independent transmission and symptoms model, when the incubation period was assumed to follow either a lognormal distribution (blue, as in Figure 1) or a gamma distribution with the same mean and standard deviation (red), and the generation time followed a lognormal distribution (as in Figure 1).

![Figure 1—figure supplement 8.](https://cdn.elifesciences.org/articles/70767/elife-70767-fig1-figsupp8-v2.jpg)

**Figure 1—figure supplement 8.:** (A-B). Uncertainty in the incubation period distribution was accounted for by updating the parameters, $\mu_{inc}$ and $\sigma_{inc}$, of a lognormal incubation period distribution (these parameters represent the mean and standard deviation of the natural logarithm of the incubation period, respectively) alongside unknown model parameters during the MCMC procedure. Independent normal prior distributions (truncated at zero) consistent with the 95% confidence intervals obtained by McAloon et al., 2020 were assumed for $\mu_{inc}$ (prior mean 1.63 log(day), standard deviation 0.061, 95% CrI 1.51–1.75; panel A) and $\sigma_{inc}$ (prior mean 0.5 log(day), standard deviation 0.026, 95% CrI 0.45–0.55; panel B). This incubation period was used directly when evaluating the likelihood in the independent transmission and symptoms model. In the mechanistic model, we assumed a gamma distributed incubation period with the same mean and standard deviation as a lognormal distribution with parameters $\mu_{inc}$ and $\sigma_{inc}$. (C-F). Violin plots indicating posterior distributions of the mean (C) and standard deviation (D) of the generation time distribution, proportion of transmissions occurring prior to symptom onset (among infectors who develop symptoms; E), and overall infectiousness parameter, $\beta_{0}$ (F), for the independent transmission and symptoms model with either a fixed (as in Figure 1; blue) or variable (i.e. accounting for uncertainty in $\mu_{inc}$ and $\sigma_{inc}$ as described above; red) incubation period distribution, and for the mechanistic model with a fixed (orange) or variable (purple) incubation period distribution.

![Figure 1—figure supplement 9.](https://cdn.elifesciences.org/articles/70767/elife-70767-fig1-figsupp9-v2.jpg)

**Figure 1—figure supplement 9.:** (A-C). Violin plots indicating the posterior distributions of the mean (A) and standard deviation (B) of the generation time distribution, and proportion of transmissions occurring prior to symptom onset (among infectors who develop symptoms; C), for the independent transmission and symptoms model under different assumptions about the dependency of transmission on the household size. In these panels, infectiousness is assumed to scale with $n^{-ρ}$, where $n$ is the household size, for $ρ=1$ (frequency-dependent transmission, blue), $ρ=0.5$ (red), and $ρ=0$ (density-dependent transmission, orange). (D) Posterior distribution of the dependency, $ρ$, when it was fitted to the data (alongside other model parameters), assuming a uniform prior for $ρ$.

![Figure 1—figure supplement 10.](https://cdn.elifesciences.org/articles/70767/elife-70767-fig1-figsupp10-v2.jpg)

**Figure 1—figure supplement 10.:** Violin plots indicating the posterior distributions of the mean (A) and standard deviation (B) of the generation time distribution, and proportion of transmissions occurring prior to symptom onset (among infectors who develop symptoms; C), for the independent transmission and symptoms model under different assumptions about the dependency of transmission on the household size. In these panels, infectiousness is assumed to scale with either $1/n$ (blue) or $1/(n−1)$ (red).

![Figure 1—figure supplement 11.](https://cdn.elifesciences.org/articles/70767/elife-70767-fig1-figsupp11-v2.jpg)

**Figure 1—figure supplement 11.:** Violin plots indicating posterior distributions of the mean (A) and standard deviation (B) of the generation time distribution, proportion of transmissions occurring prior to symptom onset (among infectors who develop symptoms; C), and overall infectiousness parameter, $\beta_{0}$ (D), for the independent transmission and symptoms model, when the relative infectiousness of asymptomatic hosts (compared to hosts who develop symptoms, at the same time since infection) was assumed to be $\alpha_{A}=0.1$ (blue), $\alpha_{A}=0.35$ (red), and $\alpha_{A}=1.27$ (orange).

![Figure 1—figure supplement 12.](https://cdn.elifesciences.org/articles/70767/elife-70767-fig1-figsupp12-v2.jpg)

**Figure 1—figure supplement 12.:** (A-C). Violin plots indicating the posterior distributions of the mean (A) and standard deviation (B) of the generation time distribution, proportion of transmissions occurring prior to symptom onset (among infectors who develop symptoms; C), and overall infectiousness parameter, $\beta_{0}$ (D), for the independent transmission and symptoms model, when individuals of unknown infection status were assumed all uninfected (blue), excluded (red), or assumed all infected (orange).

The two models gave similar posterior distributions for the proportion of transmissions prior to symptom onset (Figure 1C). Specifically, point estimate values of model parameters led to an estimated proportion of transmissions prior to symptom onset of 0.72 (95% CrI 0.63–0.80) for the independent transmission and symptoms model, and 0.73 (95% CrI 0.61–0.83) for the mechanistic model. These estimates are higher than obtained in some previous studies in which the infectiousness profile of SARS-CoV-2 infected hosts at each time since infection and/or time since symptom onset has been estimated (Ashcroft et al., 2020; Ferretti et al., 2020a; He et al., 2020). On the other hand, our point estimates for the two models both lie within the 95% credible interval obtained for the mechanistic model in our previous work (0.53–0.77, point estimate 0.65; Hart et al., 2021). Similar or higher estimates also exist in the wider literature (Casey-Bryars et al., 2021; Ganyani et al., 2020; Tindale et al., 2020).

Posterior distributions for fitted model parameters are shown in Figure 1—figure supplement 1 and Figure 1—figure supplement 2, and point estimates and 95% credible intervals are given in Appendix 1—table 2 and Appendix 1—table 3. Since only the likelihood with respect to augmented data was calculated in the MCMC procedure, direct comparisons of the goodness of fit between the models were not readily available. However, comparing model predictions of the distribution of the interval between successive symptom onset dates in households to the analogous distribution in the data indicated that both models provided a similar fit to the data (Figure 1—figure supplement 3).

In Figure 1 (and elsewhere, unless otherwise stated), we characterise the generation time distribution assuming that a constant supply of susceptible individuals are available to infect during the course of infection. This distribution corresponds to the normalised expected infectiousness profile of an infected host at each time since infection, and is widely applicable to transmission outside of, as well as within, households. However, realised household generation times are expected to be shorter than the estimates shown in Figure 1. This is due to the depletion of susceptible household members before longer generation times can be obtained, especially in small households (Cauchemez et al., 2009; Fraser, 2007; Park et al., 2020a). As a result, we also predicted the mean and standard deviation of realised generation times within the study households (Figure 1—figure supplement 4A,B), accounting for the precise distribution of household sizes in the study. For both the independent transmission and symptoms model and the mechanistic model, the mean (point estimates 3.6 days and 4.9 days for the two models, respectively) and standard deviation (3.8 days and 4.1 days) of realised household generation times were lower than our main generation time estimates shown in Figure 1. Since household transmission typically occurs earlier in the infector’s course of infection than indicated by the estimates shown in Figure 1, we predicted a higher proportion of presymptomatic transmissions within the study households (Figure 1—figure supplement 4C) compared to the estimates in Figure 1C.

For both models, we then used point estimates of fitted model parameters to infer the distributions of the generation time (Figure 2A), the time from onset of symptoms to transmission (TOST; Figure 2B) and the serial interval (Figure 2C). The TOST distribution (which characterises the relative expected infectiousness of a host (who develops symptoms) at each time from symptom onset, as opposed to from infection [Ashcroft et al., 2020; Ferretti et al., 2020a; He et al., 2020; Lehtinen et al., 2021; Wells et al., 2021]) obtained using the mechanistic model was more concentrated around the time of symptom onset compared to that predicted assuming independent transmission and symptoms (Figure 2B), as we found in our previous work (Hart et al., 2021). In contrast, the estimated serial interval distributions were similar for the two models (Figure 2C). The means and standard deviations of the distributions shown in Figure 2 are given in Appendix 1—table 4.

![Figure 2.](https://cdn.elifesciences.org/articles/70767/elife-70767-fig2-v2.jpg)

**Figure 2.:** Inferred generation time (A), TOST (B) and serial interval (C) distributions for the two models, obtained using point estimate (posterior mean) parameters. The means and standard deviations of these distributions are given in Appendix 1—table 4. Similarly to Hart et al., 2021, the discontinuity in the red curve in (B) occurs because different transmission rates were fitted for infectors in the presymptomatic infectious (P) and symptomatic infectious (I) stages of infection. The reduction in transmission following symptom onset can be attributed to changes in behaviour in response to symptoms (Manfredi and D’Onofrio, 2013).

### Temporal variation in the generation time distribution

To explore whether or not the generation time distribution changed during the study period, we separately fitted the independent transmission and symptoms model to the data from households in which the index case was recruited in (i) March-April, (ii) May-August, or (iii) September-November 2020 (Figure 3). We chose these time periods to ensure the numbers of households recruited into the study during each interval were similar (Figure 3—figure supplement 1).

![Figure 3.](https://cdn.elifesciences.org/articles/70767/elife-70767-fig3-v2.jpg)

**Figure 3.:** Violin plots indicating posterior distributions of the mean (A) and standard deviation (B) of the generation time distribution, proportion of transmissions occurring prior to symptom onset (among infectors who develop symptoms; C), and overall infectiousness parameter, $\beta_{0}$ (D), for the independent transmission and symptoms model fitted to data from March-April (blue), May-August (red), or September-November 2020 (orange).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/70767/elife-70767-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A). Bars indicating the number of households recruited each month into the study from which we obtained the household transmission data used in our analyses, from March to November 2020 (excluding five households that were excluded from our analyses as described in Methods). (B). Stacked bars indicating the total number of individuals within the households recruited each month, distinguishing between those who were infected and developed symptoms (blue), those who were infected but never developed symptoms (red), those who remained uninfected (yellow), and those for whom it was unknown whether or not they were infected (purple).

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/70767/elife-70767-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** Violin plots indicating posterior distributions of the mean (A) and standard deviation (B) of the generation time distribution, proportion of transmissions occurring prior to symptom onset (among infectors who develop symptoms; C), and overall infectiousness parameter, $\beta_{0}$ (D), for the mechanistic model fitted to data from March-April (blue), May-August (red), or September-November 2020 (orange).

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/70767/elife-70767-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** (A-C). Inferred generation time (A), TOST (B) and serial interval (C) distributions, obtained using point estimate (posterior mean) parameters for the independent transmission and symptoms model fitted to data from March-April (blue), May-August (red), or September-November 2020 (orange). (D-F). Equivalent panels to (A-C) for the mechanistic model.

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/70767/elife-70767-fig3-figsupp4-v2.jpg)

**Figure 3—figure supplement 4.:** Violin plots indicating posterior distributions of the mean (A) and standard deviation (B) of the generation time distribution, proportion of transmissions occurring prior to symptom onset (among infectors who develop symptoms; C), and overall infectiousness parameter, $\beta_{0}$ (D), for the independent transmission and symptoms model fitted to data from September (blue), October (red), or November 2020 (orange).

![Figure 3—figure supplement 5.](https://cdn.elifesciences.org/articles/70767/elife-70767-fig3-figsupp5-v2.jpg)

**Figure 3—figure supplement 5.:** Violin plots indicating posterior distributions of estimated model parameters for the mechanistic model fitted to data from March-April (blue), May-August (red), or September-November 2020 (orange). (A). Ratio of mean durations of the latent (E) and incubation (combined E and P) periods, $k_{E}/k_{inc}$. (B) Mean symptomatic infectious (I) period, $1/\mu$. (C). Ratio of transmission rates in the presymptomatic infectious (P) and symptomatic infectious (I) stages of infection, $\alpha_{P}$. Corresponding estimates of the overall infectiousness parameter, $\beta_{0}$ (the other fitted model parameter) are shown in Figure 3—figure supplement 2D.

![Figure 3—figure supplement 6.](https://cdn.elifesciences.org/articles/70767/elife-70767-fig3-figsupp6-v2.jpg)

**Figure 3—figure supplement 6.:** Violin plots indicating posterior distributions of the mean (A) and standard deviation (B) of the generation time distribution, proportion of transmissions occurring prior to symptom onset (among infectors who develop symptoms; C), overall infectiousness parameter, $\beta_{0}$ (D), and probability of co-primary infection (E), for the independent transmission and symptoms model fitted to data from March-April (blue), May-August (red), or September-November 2020 (orange), when the possibility of co-primary cases was included in our approach (see the Appendix).

The results shown in Figure 3A suggest a shorter mean generation time in September-November 2020 (2.9 days, 95% CrI 1.8–4.3 days) compared to earlier months (4.9 days, 95% CrI 3.6–6.3 days, for March-April and 5.2 days, 95% CrI 3.4–7.2 days, for May-August). Comparing the posterior estimates for May-August and September-November (the red and orange violins in Figure 3A, respectively) indicated a 97% posterior probability of a shorter mean generation time in the later of these two time periods. A similar temporal reduction in the mean generation time was found when we instead fitted the mechanistic model to the data from the three time intervals (Figure 3—figure supplement 2). Estimates of the mean generation time using the mechanistic model were 6.5 days (95% CrI 5.6–8.1 days) for March-April, 7.1 days (95% CrI 5.7–9.6 days) for May-August, and 5.1 days (95% CrI 4.3–6.4 days) for September-November, with a 98% posterior probability of a shorter mean generation time in September-November than May-August. We also used point estimates of model parameters to compare the distributions of the generation time, TOST and serial interval between the time periods (Figure 3—figure supplement 3), with both models indicating that the transmission risk peaked earlier in infection for individuals infected in September-November compared to earlier months (Figure 3—figure supplement 3A,D).

Figure 3C shows posterior estimates for the proportion of transmissions occurring prior to symptom onset (among symptomatic infectors) across the three time periods for the independent transmission and symptoms model, indicating a very high proportion of presymptomatic transmissions in September-November (0.83, 95% CrI 0.72–0.93) compared to lower estimates for March-April (0.64, 95% CrI 0.51–0.77) and May-August (0.62, 95% CrI 0.41–0.79). Our results for the mechanistic model indicate a similar temporal increase in the proportion of presymptomatic transmissions during the study period (Figure 3—figure supplement 2C).

To explore the lower estimated generation time for September-November further, we also fitted the independent transmission and symptoms model to the data from each of these months individually (Figure 3—figure supplement 4). The shorter estimated generation time compared to earlier in the pandemic was consistent across each of the three months (Figure 3—figure supplement 4A). We note that, while the Alpha (B.1.1.7) variant had begun to emerge in the UK by the end of the study period (Public Health England, 2021), genomic surveillance as part of the study showed that this variant caused infections in only two study households. This variant was therefore unlikely to have been responsible for the temporal reduction in the generation time that we observed.

In Figure 3—figure supplement 5, we show the posterior distributions of the fitted parameters for the mechanistic model (other than the overall infectiousness, $\beta_{0}$, which is shown in Figure 3D) over the different time periods. These parameters represent the mean duration of the platent period (expressed as a proportion of the mean incubation period; Figure 3—figure supplement 5A), the mean duration of the symptomatic infectious period (Figure 3—figure supplement 5B), and the relative infectiousness of presymptomatic infectious hosts compared to those with symptoms (Figure 3—figure supplement 5C). However, there was substantial overlap in the credible intervals of posterior estimates of each parameter between the three time periods. We were therefore unable to identify the precise parameter(s) responsible for the decrease in generation time and increase in the proportion of presymptomatic transmissions that we observed.

### Sensitivity analyses

When we fitted the two models to the household transmission data, we assumed that each household transmission chain was initiated by a single primary case and all other infected household members were infected from within the household. However, we also extended our framework to account for the possibility of co-primary cases (Appendix 1, Figure 1—figure supplement 5 and Figure 3—figure supplement 6). This led to slightly higher estimates of the mean generation time (Figure 1—figure supplement 5A) under each model compared to the corresponding estimates shown in Figure 1A, with point estimates of 4.8 days (95% CrI 3.6–6.3 days) for the independent transmission and symptoms model and 6.8 days (95% CrI 5.7–8.6 days) for the mechanistic model. Estimates of the standard deviation of the generation time distribution were similar to those in Figure 1 (Figure 1—figure supplement 5B); point estimates were 4.8 days (95% CrI 2.9–7.9 days) for the independent transmission and symptoms model and 5.1 days (95% CrI 4.0–6.9 days for the mechanistic model). As part of the fitting procedure, we estimated the probability that each household member was infected during the primary transmission event (Figure 1—figure supplement 5E), obtaining point estimates of 0.17 (95% CrI 0.02–0.33) under the independent transmission and symptoms model and 0.27 (95% CrI 0.10–0.41) under the mechanistic model. We also repeated the analyses in Figure 3 but accounting for the possibility of co-primary cases (Figure 3—figure supplement 6). Our main qualitative finding remained unchanged: the mean generation time was found to decrease during the study period (Figure 3—figure supplement 6A).

In the independent transmission and symptoms model, we assumed that both the generation time and incubation period follow lognormal distributions. The mean and standard deviation of the generation time distribution were estimated by fitting the model to the household transmission data. In the fitting procedure, we assumed that the incubation period followed a lognormal distribution that was obtained in a previous meta-analysis (McAloon et al., 2020). In contrast, we assumed in our mechanistic approach that each infection could be decomposed into three gamma distributed stages (latent, presymptomatic infectious and symptomatic infectious), so that the incubation period was also gamma distributed (with the same mean and standard deviation as the lognormal distribution obtained by McAloon et al., 2020). An expression for the generation time distribution in the mechanistic model, which does not take a simple parametric form, is given in the Appendix. However, we conducted supplementary analyses in which we instead assumed that either the generation time (Figure 1—figure supplement 6) or incubation period (Figure 1—figure supplement 7) in the independent transmission and symptoms model was gamma distributed. In both cases, we obtained similar results to those shown for that model in Figure 1.

We also relaxed the assumption of a fixed incubation period distribution (Figure 1—figure supplement 8), using the confidence intervals obtained by McAloon et al., 2020 to account for uncertainty in the incubation period distribution (Figure 1—figure supplement 8A, B). For both the independent transmission and symptoms model and the mechanistic model, accounting for this uncertainty did not substantially affect posterior estimates of either the mean (Figure 1—figure supplement 8C) or the standard deviation (Figure 1—figure supplement 8D) of the generation time distribution.

In our main analyses, we assumed that household transmission was frequency-dependent, so that the force of infection exerted by an infected household member on each susceptible household member scales with $1/n$, where $n$ is the household size (Cauchemez et al., 2014; Cauchemez et al., 2004). However, since some studies of influenza virus transmission in households have found transmission to lie somewhere in between frequency- and density-dependent (Endo et al., 2019; Ferguson et al., 2005), we also considered alternative possibilities where infectiousness scales with $n^{-ρ}$, for different values of $ρ$. In Figure 1—figure supplement 9A-C, we compared estimates under our baseline value of $ρ=1$ (frequency-dependent transmission) with those obtained assuming either $ρ=0$ (density-dependent transmission) or the intermediate possibility of $ρ=0.5$ considered by Endo et al., 2019. In addition, we conducted an analysis in which the dependency, $ρ$, was estimated alongside other model parameters (Figure 1—figure supplement 9D). We found that our estimates of the mean and standard deviation of the generation time distribution were robust to the assumed value of $ρ$ (Figure 1—figure supplement 9A, B). However, when the value $ρ$ was fitted (Figure 1—figure supplement 9D), we estimated a value of 1.0 (95% CrI 0.6–1.5). This supported our assumption of frequency-dependent transmission, although the credible interval was relatively wide. In addition, we considered the possibility that infectiousness instead scales with $1/(n−1)$, so that the infector under consideration is not included in this scaling, and again obtained similar estimates of the mean and standard deviation of the generation time distribution compared to those shown in Figure 1 (Figure 1—figure supplement 10).

We also considered the sensitivity of our results to the assumed relative infectiousness of asymptomatic infected hosts (Figure 1—figure supplement 11). In most of our analyses, we assumed that the expected infectiousness of an infected host who remained asymptomatic throughout infection was a factor $\alpha_{A}=0.35$ times that of a host who develops symptoms, at each time since infection (Buitrago-Garcia et al., 2020). However, similar estimates of the mean (Figure 1—figure supplement 11) and standard deviation (Figure 1—figure supplement 11B) of the generation time distribution were obtained when we instead assumed $\alpha_{A}=0.1$ or $\alpha_{A}=1.27$ (these values corresponded to the lower and upper confidence bounds obtained by Buitrago-Garcia et al., 2020). Lower values of $\alpha_{A}$ did lead to slightly higher estimates of the overall infectiousness of infectors who develop symptoms, $\beta_{0}$ (Figure 1—figure supplement 11D). However, this effect was minimal, likely because very few cases in the household study were asymptomatic (27 out of 357).

Finally, we explored the robustness of our results to the exclusion of household members of unknown infection status (see Methods), considering the extreme possibilities where these individuals were instead assumed to have either all remained uninfected, or all become infected (Figure 1—figure supplement 12). Although the estimates of $\beta_{0}$ were affected by this assumption (Figure 1—figure supplement 12D), the estimated generation time distribution was robust to the assumed infection status of these individuals (Figure 1—figure supplement 12A,B).

## Discussion

In this study, we estimated the generation time distribution of SARS-CoV-2 in the UK by fitting two different models to data describing the infection status and symptom onset dates of individuals in 172 households. The first model was predicated on an assumption that transmission and symptoms are independent. While this assumption has often been made in previous studies in which the SARS-CoV-2 generation time has been estimated (Challen et al., 2021; Deng et al., 2021; Ferretti et al., 2020b; Ganyani et al., 2020; Knight and Mishra, 2020), it is not an accurate reflection of the underlying epidemiology (Bacallado et al., 2020; Lehtinen et al., 2021). Therefore, we also considered a mechanistic model based on compartmental modelling, which was shown in our earlier work (Hart et al., 2021) to provide an improved fit to data from 191 SARS-CoV-2 infector-infectee pairs compared to previous models that have been used to estimate the generation time. Here, infection times and the order of transmissions within households were unknown, whereas in Hart et al., 2021 the direction of transmission was assumed to be known for each infector-infectee pair. For that reason, we needed to extend the statistical inference methods underlying our previous work (Hart et al., 2021) to fit the two models to household data. To do this, we used a data augmentation MCMC approach similar to previous studies of household influenza virus transmission (Cauchemez et al., 2009; Cauchemez et al., 2004; Ferguson et al., 2005).

Under the model assuming independent transmission and symptoms, we estimated a mean generation time of 4.2 days (95% CrI 3.3–5.3 days) and a standard deviation of 4.9 days (95% CrI 3.0–8.3 days). The estimate of the mean generation time was comparable to previous estimates obtained under this assumption using data from elsewhere (Ferretti et al., 2020a; Ferretti et al., 2020b; Ganyani et al., 2020; Table 1). On the other hand, while our credible interval for the standard deviation was wide, the estimates obtained in those previous studies (Ferretti et al., 2020a; Ferretti et al., 2020b; Ganyani et al., 2020) all lay below our lower 95% credible limit of 3.0 days. One potential cause of this disparity is the difference in isolation policies for symptomatic hosts between countries. In particular, the UK’s policy of self-isolation may be expected to lead to a longer-tailed generation time distribution compared to countries with a policy of isolation outside the home, since under home isolation, some within-household transmission is likely to occur even following isolation. Isolation outside the home was commonplace in the East and Southeast Asian countries where the majority of the data underlying the estimates by Ferguson et al., 2005; Ferretti et al., 2020a; Ganyani et al., 2020 were collected.

Using the mechanistic model, we predicted a higher mean generation time of 5.9 days (95% CrI 5.2–7.0 days) compared to the value estimated under the assumption of independent transmission and symptoms. On the other hand, the inferred serial intervals for the independent transmission and symptoms model and mechanistic model were more similar (Figure 2C), with means of 4.2 days and 4.7 days, respectively. Temporal information in our household transmission data consisted mostly of symptom onset dates, with very few individuals testing positive before developing symptoms. Therefore, the variation in estimates of the generation time between the models can be attributed to differences in the assumed relationships between the generation time and serial interval under those models. For the independent transmission and symptoms model, the generation time and serial interval distributions have the same mean, as is commonly assumed to be the case (Lehtinen et al., 2021). However, this was not true for the mechanistic model, in which infected hosts with longer presymptomatic infectious periods generate (on average) a higher number of transmissions. As a result, under the mechanistic model, a randomly chosen infection is more likely to arise from an infector with a longer incubation period than from a host with a shorter incubation period, thereby leading to a longer generation time than serial interval (an analytical expression for the exact difference between the mean generation time and serial interval for that model is derived in the Appendix).

Our results do not indicate any clear difference in goodness of fit to the data between the two models (Figure 1—figure supplement 3). A range of factors should therefore be considered when deciding which of our estimates of epidemiological parameters to use in subsequent analyses. Although any model requires simplifying assumptions to be made, our mechanistic approach allows the standard assumption of independent transmission and symptoms to be relaxed by providing a mechanistic underpinning to the relationship between the times at which individuals display symptoms and become infectious. Furthermore, as described above, this model was shown in our previous work (Hart et al., 2021) to provide a better fit to an earlier SARS-CoV-2 dataset than a model assuming independence between transmission and symptoms (in our earlier work [Hart et al., 2021], the simpler setting of transmission pairs rather than households facilitated direct model comparison). On the other hand, the independent transmission and symptoms model has the advantage of producing an estimated generation time distribution with a simple parametric form. The choice of estimates to use may also depend on precisely what the estimates are being used for. For example, the generation time distribution inferred under the assumption of independent transmission and symptoms may be better suited for use in some models for estimating the time-dependent reproduction number, since those models often also involve the assumption that transmission and symptoms are independent (Abbott et al., 2020). In contrast, the parameter estimates from our mechanistic approach correspond naturally to parameters in compartmental epidemic models.

By fitting separately to data from three different intervals within the study period (March-November 2020), we investigated whether or not the generation time distribution in the UK changed as the pandemic progressed. Our results indicate a shorter mean generation time in September-November compared to earlier months (Figure 3A). One possible explanation for this is a higher proportion of time spent indoors in colder months leading to an increased transmission risk, particularly in the early stages of infection before symptoms develop (since symptomatic infected hosts are still likely to self-isolate). This explanation is consistent with our finding in Figure 3C of a higher proportion of transmissions occurring prior to symptom onset in September-November compared to March-April and May-August.

While behavioural changes may have been responsible for our finding of a temporal decrease in the generation time, an alternative explanation could be that evolutionary changes in the SARS-CoV-2 virus that occurred during the study period affected the generation time. For example, the B.1.177 lineage emerged in Spain in early summer 2020, and became the dominant SARS-CoV lineage in the UK around the beginning of October 2020 (Vöhringer et al., 2021). Subsequently, the Alpha (B.1.1.7) variant, which was first detected in September 2020, became dominant in the UK in December 2020 (Public Health England, 2021). The Alpha variant has been shown to possess different characteristics than earlier variants (Davies et al., 2021; Volz et al., 2021), causing an increased epidemic growth rate in the UK that has been attributed to an increase in transmissibility of 43%–90% (Davies et al., 2021). While in principle evolutionary changes could explain the variation in the generation time that we observed, sequencing data show that the Alpha variant was responsible for infections in only two households within our dataset. Consequently, the Alpha variant was not responsible for our main finding of a temporally decreasing generation time, and additional data are required to quantify the impact of the emergence of that variant (and subsequent variants, such as the Delta (B.1.617.2) and Omicron (B.1.1.529) variants) on the SARS-CoV-2 generation time.

In data collected from infector-infectee transmission pairs, shorter generation times are expected to be over-represented at times when case numbers are rising (Britton and Scalia Tomba, 2019; Ferretti et al., 2020b; Lehtinen et al., 2021), and vice versa. While we used data from households (rather than transmission pairs) in our analyses, a similar effect may have contributed to our shorter estimated mean generation time for September-November 2020 (national case numbers were mostly increasing in September-October 2020) compared to earlier months of the study (during which case numbers were mostly decreasing; Knock et al., 2021; Pouwels et al., 2021). However, we estimated the mean generation time to be similar in November (when case numbers were mostly decreasing [Knock et al., 2021; Pouwels et al., 2021]) compared to September and October (Figure 3—figure supplement 4), suggesting that this effect of background epidemic dynamics alone did not drive the temporal changes in generation time that we observed. We note, however, that sample sizes for individual months were small (Figure 3—figure supplement 1). Extending our household inference framework to explicitly account for background epidemic dynamics in generation time estimates (similar to methods that have been developed for transmission pair data [Britton and Scalia Tomba, 2019; Ferretti et al., 2020b]) is an avenue for future work.

Our finding of a temporal decrease in the mean generation time during the study period highlights the importance of obtaining up-to-date generation time estimates specific to the location under study. Should variations in the generation time distribution occur and not be accounted for, estimates of the time-dependent reproduction number may be incorrect (Park et al., 2021; Wallinga and Lipsitch, 2007). Specifically, if the mean generation time is shorter than assumed, then the true value of the time-dependent reproduction number is likely to be closer to one than the inferred value (Wallinga and Lipsitch, 2007), and vice versa.

One advantage of our approach compared to previous studies in which the SARS-CoV-2 generation time has been estimated (Ferretti et al., 2020a; Ganyani et al., 2020; Hart et al., 2021) is that we were able to include the contribution of asymptomatic infected hosts to household transmission chains in our analyses. We showed that our estimated generation time distribution was robust to the assumed relative infectiousness of infected hosts who remain asymptomatic, $\alpha_{A}$ (Figure 1—figure supplement 11). Similarly, while we assumed frequency-dependent household transmission in most of our analyses, we found that the exact relationship between the household size and transmission had little effect on our estimates of the mean and standard deviation of the generation time distribution (Figure 1—figure supplement 9 and Figure 1—figure supplement 10). We also considered estimating the exponent governing the dependency of transmission on household size (Figure 1—figure supplement 9D). This supported our assumption of frequency-dependent transmission, and is consistent with the finding of an inverse relationship between household size and secondary attack rate in the household study underlying our analyses (Miller et al., 2021). In previous studies of influenza transmission within households, evidence has been found both in favour of (Cauchemez et al., 2004) and against (Endo et al., 2019) frequency-dependent transmission.

While our generation time estimates were robust to the assumed relative infectiousness of infected hosts who remain asymptomatic and whether transmission was assumed to be frequency- or density-dependent, extending our approach to account for the possibility that household transmission chains originate with multiple co-primary cases led to slightly higher estimates of the generation time (Figure 1—figure supplement 5) compared to our main estimates (Figure 1). Despite the overall higher estimated generation time, our main qualitative finding of a temporal decrease in the generation time held when co-primary cases were incorporated (Figure 3—figure supplement 6).

Like any mathematical modelling study, our approach has some limitations. We used household data in our analyses, whereas some characteristics of wider community transmission may differ from those of transmission within households. However, we corrected for the regularity of household contacts to estimate the (expected) infectiousness profile of an infected host at each time since infection (accounting for behavioural factors), which provides a widely applicable generation time estimate (Figure 1). Specifically, the infectiousness profile gives the generation time distribution under the assumption that a constant supply of susceptible individuals are available throughout the course of infection. This distribution can then be conditioned to specific population structures, as we demonstrated by estimating the realised generation time distribution within the study households (Figure 1—figure supplement 4). The household generation time estimates shown in Figure 1—figure supplement 4 are shorter than our main generation time estimates (Figure 1), due to the regularity of household contacts and the depletion of susceptible individuals within households before longer generation times can be realised.

We also note that, while our dataset involved a larger sample size than used in most other studies in which the SARS-CoV-2 generation time was estimated (Ferretti et al., 2020a; Ferretti et al., 2020b; Ganyani et al., 2020; Hart et al., 2021), the demographics of the study households may not have been completely representative of the wider population. Exploring heterogeneity in the generation time distribution between individuals and/or households with different characteristics is an important topic for future work. This could involve, but is not limited to, estimating the generation time distribution for individuals of different age, sex, ethnicity, and socio-economic status. Nonetheless, as well as providing updated SARS-CoV-2 generation time estimates, our study demonstrates that changes in the generation time can be detected using data from household studies. Our finding that the generation time has become shorter highlights both the importance of continued monitoring of the generation time and the role of household studies in such monitoring efforts, particularly in light of the more recent emergence of novel SARS-CoV-2 variants.

In summary, we have inferred the SARS-CoV-2 generation time distribution in the UK using household data and two different transmission models. A key output of this research is one of the first estimates of the SARS-CoV-2 generation time outside Asia. Another crucial feature of our analysis is that it was based on data from beyond the first few months of the pandemic. Since this research suggests that the generation time may be changing, continued data collection and analysis is of clear importance.

## Methods

### Data

Data were obtained from a household study (Miller et al., 2021) conducted in 172 UK households (with 603 household members in total) by PHE between March and November 2020 (Figure 1—source data 1). In each household, an index case was recruited following a positive PCR test. The following were then recorded for each household member:

In the study, all household members who tested positive in either a PCR or antibody test were assumed to have been infected. Conversely, all individuals who tested negative for antibodies and did not return a positive PCR test (i.e. the two PCR tests were either negative or were not carried out) were assumed to have remained uninfected, irrespective of symptom status. For 34 individuals (6% of the study cohort), no antibody test was carried out and any PCR tests were negative. Since the available data were considered insufficient to determine whether or not these 34 individuals were infected, these individuals were excluded from our main analyses (but were counted in the household size), although we also considered the sensitivity of our results to this assumption.

In two households, at least one household member developed symptoms 55–56 days prior to the symptom onset date of the index case, with no other household members developing symptoms (or returning a positive PCR or antibody test) between these dates. In contrast, the maximum gap between successive symptom onset dates in the remaining households was 25 days (Figure 1—figure supplement 3). Data from these two households were excluded from our analyses, on the basis that the virus was most likely introduced multiple times into these households. Three other households were also excluded from our analyses because, other than the index cases in each household, all other household members were of unknown infection status (i.e. they were among the individuals for whom no antibody test was carried out and any PCR tests were negative).

Overall, aside from the five excluded households, the 167 remaining households comprised 587 individuals, of whom 330 became infected and developed symptoms, 27 became infected but remained asymptomatic, 200 remained uninfected, and the remaining 30 were of unknown infection status. The number of households and individuals recruited into the study by month is shown in Figure 3—figure supplement 1.

### Models

#### General modelling framework

Throughout, we denote the expected force of infection exerted by an infected host onto each susceptible member of their household, at time since infection $\tau$, by $\beta(\tau)$, where we assumed

$$
\beta(\tau)=(\beta_{0}/n)f(\tau),
$$

for a host who develops symptoms, and

$$
\beta(\tau)=\alpha_{A}(\beta_{0}/n)f(\tau),
$$

for a host who remains asymptomatic throughout infection. Here:

Except where otherwise stated, we considered the generation time distribution assuming a constant supply of susceptibles during infection, $f(\tau)$, which corresponds to the normalised expected infectiousness profile and gives a widely applicable generation time estimate (see Discussion). However, realised generation times within a household may be shorter than predicted by this distribution due to the depletion of susceptible household members before longer generation times can be realised (Cauchemez et al., 2009; Fraser, 2007; Park et al., 2020b). For example, if infected hosts are (on average) equally infectious at two times since infection, $\tau_{1}<\tau_{2}$, then $f(\tau_{1})=f(\tau_{2})$. However, because the number of susceptible household members may decrease between these two times (i.e. either the host under consideration, or another infected household member, may transmit the virus within the household in the intervening time), then transmission is in fact more likely to occur in a household at the earlier time, $\tau_{1}$, when more susceptibles are available. Therefore, we also predicted the mean and standard deviation of realised generation times within the study households in Figure 1—figure supplement 4.

We considered two different models of infectiousness, which are outlined below. Under each model, expressions were derived in Hart et al., 2021 for the generation time, TOST and serial interval distributions, in addition to the proportion of transmissions occurring before symptom onset. These expressions are given in the Appendix here (other than the generation time distribution and proportion of presymptomatic transmissions for the independent transmission and symptoms model, which are stated below).

#### Independent transmission and symptoms model

In this model, the infectiousness of an infected host (who does not remain asymptomatic throughout infection; asymptomatic infected hosts are considered separately) at a given time since infection, $\tau$, is assumed to be independent of exactly when the host develops symptoms – that is, the generation time and incubation period are independent. In our main analyses using this model, we assumed that the generation time distribution, $f(\tau)$, is the probability density function of a lognormal distribution (Ferguson et al., 2005; an alternative case of a gamma distributed generation time is considered in Figure 1—figure supplement 6). The mean and standard deviation of this distribution, in addition to $\beta_{0}$, were estimated when we fitted the model to the household transmission data.

Under the assumption of independent transmission and symptoms, the proportion of transmissions occurring prior to symptom onset (among infectors who develop symptoms) is given by (Ferretti et al., 2020b; Fraser et al., 2004)

$$
\int_{0}^{∞}f(\tau)(1−F_{inc}(\tau))d\tau,
$$

where $F_{inc}$ is the cumulative distribution function of the incubation period (this was assumed to be known; the exact incubation period distribution we used is given under ‘Parameter estimation’ below).

#### Mechanistic model

Under the mechanistic model (Hart et al., 2021), infectors who develop symptoms progress through independent latent (E), presymptomatic infectious (P) and symptomatic infectious (I) stages of infection. We assumed the duration of each stage to be gamma distributed, and infectiousness was assumed to be constant during each stage. Under these assumptions, an expression can be derived for the expected infectiousness, $\beta(\tau∣\tau_{inc})$, of a host (who develops symptoms) at each time since infection $\tau$, conditional on their incubation period $\tau_{inc}$. We assumed that entirely asymptomatic infected hosts follow the same stage progression as those who develop symptoms, although in this case the distinction between the P and I stages has no epidemiological meaning. Details of the mechanistic approach, including the formula for $\beta(\tau∣\tau_{inc})$, are provided in the Appendix.

When we fitted this model to the household transmission data, three model parameters were estimated in addition to $\beta_{0}$. These parameters correspond to:

### Likelihood function

Here, we consider a household of size $n$, in which $n_{I}$ household members become infected (of whom $n_{S}$ develop symptoms and $n_{A}$ remain asymptomatic throughout infection) and $n_{U}=n-n_{I}$ remain uninfected. We derive an expression for the likelihood of the parameters of either model of infectiousness, given the entire sequence of infection times of individuals in the household ($t_{1}<…<t_{n_{I}}$) as well as the precise symptom onset time ($t_{s,j}$) of each host, $j$, who develops symptoms. In the case of the mechanistic model, the likelihood also depends on the times at which entirely asymptomatic infected hosts enter the I stage of infection (these times are also denoted by $t_{s,j}$, although for asymptomatic infected individuals these times have no epidemiological meaning). Since exact infection times were not available within study households, and it was unknown exactly when each symptomatic infected host developed symptoms within their recorded symptom onset date, we used data augmentation MCMC to fit the two models to the UK household transmission data using this likelihood function (see further details below).

When deriving the likelihood, we made several simplifying assumptions:

We denote the expected infectiousness of household member $j$, at time $\tau$ since infection, by $\beta_{j}(\tau)$. For the mechanistic model in which transmission and symptoms are not independent, this infectiousness is conditional on the duration of the incubation period, $t_{s,j}-t_{j}$, for a host who develops symptoms (the infectiousness is also conditional on $(t_{s,j}−t_{j})$ for an entirely asymptomatic infected host, although this interval has no epidemiological meaning for such individuals). The total (instantaneous) force of infection exerted at time $t$ on each susceptible household member is then

$$
\lambda(t)=\sumj=1n_{I}\beta_{j}(t−t_{j}),
$$

where $\beta_{j}(t−t_{j})=0$ for $t\leqt_{j}$, and the cumulative force of infection is

$$
Λ(t)=\int_{−∞}^{t}\lambda(s)ds.
$$

For $k=2,…,n_{I}$, conditional on the sequence of infection times up to time $t_{k}$, the probability that host $k$ becomes infected at time $t_{k}$ is given by

$$
\lambda(t_{k})exp(−Λ(t_{k})),
$$

where $exp(−Λ(t_{k}))$ represents the probability of host $k$ avoiding infection from household contacts that occurred before their actual time of infection, $t_{k}$ (Cauchemez et al., 2004; Ferguson et al., 2005). This factor, which was not included in the likelihood when we previously estimated the generation time using data from infector-infectee transmission pairs (Hart et al., 2021), is required here because of the regularity of household contacts. Since household contacts occur frequently, it is necessary to account explicitly for contacts between infected and susceptible individuals that did not lead to transmission. The inclusion of this factor in the likelihood therefore corrects for the regularity of household contacts to ensure widely applicable generation time estimates (note that this factor is equal to one in the limit of a very small overall household infectiousness parameter, $\beta_{0}$).

For $k=n_{I}+1,…,n$, conditional on the entire sequence of infection times, $t_{1},…,t_{n_{I}}$, the probability of host $k$ never being infected is given by $exp(−Λ(∞))$. In the case of independent transmission and symptoms, we have

$$
exp(−Λ(∞))=exp⁡(−\beta_{0}(n_{S}+\alpha_{A}n_{A})/n),
$$

whereas for the mechanistic model, $exp(−Λ(∞))$ instead depends on the incubation periods of those hosts who develop symptoms, as well as the corresponding time periods for entirely asymptomatic infected hosts (see the Appendix).

The likelihood contribution from the household, $L(\theta)$, where $\theta$ is the vector of unknown model parameters, can therefore be written as

$$
L(\theta)=\prodk=1nL_{k,1}(\theta)L_{k,2}(\theta).
$$

Here, $L_{k,1}(\theta)$ is the contribution to the likelihood from the transmission, or absence of transmission, to host $k$, that is,

$$
L_{k,1}(\theta)={1,fork=1;\lambda(t_{k})exp(−Λ(t_{k})),fork=2,…,n_{I};exp(−Λ(∞)),fork=n_{I}+1,…,n.
$$

$L_{k,2}(\theta)$ is the contribution from the incubation period of host $k$ (where applicable), that is, for the independent transmission and symptoms model,

$$
L_{k,2}(\theta)={f_{inc}(t_{s,k}−t_{k}),ifhostkbecomesinfectedanddevelopssymptoms;1,otherwise;
$$

where $f_{inc}$ is the probability density function of the incubation period (this was assumed to be known; the exact incubation period distribution we used is given below). For the mechanistic model, we also have a contribution to the likelihood from the (in this case not epidemiologically meaningful) times $t_{s,k}-t_{k}$ for entirely asymptomatic infected hosts, so that

$$
L_{k,2}(\theta)={f_{inc}(t_{s,k}−t_{k}),fork=1,…,n_{I};1,fork=n_{I}+1,…,n.
$$

### Parameter estimation

#### Incubation period

For the independent transmission and symptoms model, we assumed a lognormal incubation period distribution with mean 5.8 days and standard deviation 3.1 days (McAloon et al., 2020). For the mechanistic model, we assumed a gamma distributed incubation period with the same mean and standard deviation; this was for mathematical convenience, since the incubation period could then be decomposed into the sum of independent gamma distributed latent and presymptomatic infectious periods. Results for the independent transmission and symptoms model using a gamma distributed incubation period are shown in Figure 1—figure supplement 7, and uncertainty in the exact parameters of the incubation period distribution is accounted for in Figure 1—figure supplement 8.

#### Parameter fitting procedure

Unknown model parameters were estimated using data augmentation MCMC. The observed data comprised information about whether or not individuals were ever infected and/or displayed symptoms, symptom onset dates, and for some individuals an upper bound on their infection time (corresponding to the date of a positive PCR test). These data were augmented with (estimated) precise times of infection and symptom onset (where applicable) for each infected host. No prior assumptions were made about the order of transmissions within each household.

Below, we outline the parameter fitting procedure that we used for the independent transmission and symptoms model. The procedure used for the mechanistic model was similar and is described in the Appendix.

Lognormal priors were assumed for fitted model parameters (these parameters were the mean and standard deviation of the generation time distribution, in addition to the overall infectiousness, $\beta_{0}$). The priors for the mean and standard deviation of the generation time distribution had medians of 5 days and 2 days, respectively (these choices were informed by previous estimates of the SARS-CoV-2 generation time distribution [Ferretti et al., 2020a; Ferretti et al., 2020b; Ganyani et al., 2020]), and were chosen to ensure a prior probability of only 0.025 that these parameters exceeded very high values of 10 days and 7 days, respectively. The exact priors we used are given in Appendix 1—table 2.

Here, we denote the vector of model parameters by $\theta$, and the augmented data by

$$
t=(t^{(1)},…,t^{(M)}),
$$

where $t^{(m)}$ represents the augmented data from household $m=1,…,M$, and $M$ is the total number of households. We write the (overall) likelihood as

$$
L(\theta;t)=\prodm=1ML^{(m)}(\theta;t^{(m)}),
$$

where the likelihood contribution, $L^{(m)}(\theta;t^{(m)})$, from each household, $m$, was computed as described in the previous section (i.e. all households in the study were assumed to be independent), and we denote the prior density of $\theta$ by $\pi(\theta)$.

In each step of the chain, we carried out (in turn) one of the following:

The chain was run for 10,000,000 iterations; the first 2,000,000 iterations were discarded as burn-in. Posteriors were obtained by recording every 100 iterations of the chain.

### Governance statement

The household study was approved by the PHE Research Ethics and Governance Group as part of the portfolio of PHE’s enhanced surveillance activities in response to the pandemic.
