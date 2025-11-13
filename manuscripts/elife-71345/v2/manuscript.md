# Estimation and worldwide monitoring of the effective reproductive number of SARS-CoV-2

## Authors

- Jana S Huisman<sup>1</sup> ([ORCID: 0000-0002-1782-8109](https://orcid.org/0000-0002-1782-8109)) †
- Jérémie Scire<sup>2</sup>
- Daniel C Angst<sup>1</sup> ([ORCID: 0000-0002-6512-4595](https://orcid.org/0000-0002-6512-4595))
- Jinzhou Li<sup>4</sup>
- Richard A Neher<sup>2</sup> ([ORCID: 0000-0003-2525-1407](https://orcid.org/0000-0003-2525-1407))
- Marloes H Maathuis<sup>4</sup>
- Sebastian Bonhoeffer<sup>1</sup> ([ORCID: 0000-0001-8052-3925](https://orcid.org/0000-0001-8052-3925))
- Tanja Stadler<sup>2</sup> ([ORCID: 0000-0001-6431-535X](https://orcid.org/0000-0001-6431-535X)) †

### Affiliations

1. Department of Environmental Systems Science, ETH Zurich, Swiss Federal Institute of Technology Zurich Switzerland ([ROR:05a28rw58](https://ror.org/05a28rw58))
2. Swiss Institute of Bioinformatics Lausanne Switzerland ([ROR:002n09z45](https://ror.org/002n09z45))
3. Department of Biosystems Science and Engineering, ETH Zurich, Swiss Federal Institute of Technology Basel Switzerland ([ROR:05a28rw58](https://ror.org/05a28rw58))
4. Department of Mathematics, ETH Zurich, Swiss Federal Institute of Technology Zurich Switzerland ([ROR:05a28rw58](https://ror.org/05a28rw58))
5. Biozentrum, University of Basel Basel Switzerland ([ROR:02s6k3f65](https://ror.org/02s6k3f65))

† Corresponding author

## Abstract

The effective reproductive number Re is a key indicator of the growth of an epidemic. Since the start of the SARS-CoV-2 pandemic, many methods and online dashboards have sprung up to monitor this number through time. However, these methods are not always thoroughly tested, correctly placed in time, or are overly confident during high incidence periods. Here, we present a method for timely estimation of Re, applied to COVID-19 epidemic data from 170 countries. We thoroughly evaluate the method on simulated data, and present an intuitive web interface for interactive data exploration. We show that, in early 2020, in the majority of countries the estimated Re dropped below 1 only after the introduction of major non-pharmaceutical interventions. For Europe the implementation of non-pharmaceutical interventions was broadly associated with reductions in the estimated Re. Globally though, relaxing non-pharmaceutical interventions had more varied effects on subsequent Re estimates. Our framework is useful to inform governments and the general public on the status of epidemics in their country, and is used as the official source of Re estimates for SARS-CoV-2 in Switzerland. It further allows detailed comparison between countries and in relation to covariates such as implemented public health policies, mobility, behaviour, or weather data.

## Introduction

During an infectious-disease outbreak, such as the SARS-CoV-2 pandemic, accurate monitoring of the epidemic situation is critical to the decision-making process of governments and public health authorities. The magnitude of an epidemic, as well as its spatial and temporal infection dynamics determine the exposure risk posed to citizens in the near and long-term future, the pressure on critical infrastructure like hospitals, and the overall burden of disease to society.

The effective reproductive number $R_{e}$ is a key indicator to describe how efficiently a pathogen spreads in a given population at a given time (Anderson and May, 1991; Cauchemez et al., 2006; Wallinga and Lipsitch, 2007). It quantifies the average number of secondary infections caused by a primary infected individual. It also has a natural threshold value of 1, below which the epidemic reduces in size Anderson and May, 1991; Nishiura and Chowell, 2009. $R_{e}$ typically changes during the course of an epidemic as a result of the depletion of susceptible individuals, changed contact behaviour, seasonality of the pathogen, or the effect of pharmaceutical and non-pharmaceutical interventions (NPIs) (Anderson and May, 1991; Delamater et al., 2019; Scire et al., 2020; Ali et al., 2020; Flaxman et al., 2020).

Different methods have been developed to estimate $R_{e}$. They broadly fall into two categories: those based on compartmental models, (e.g. Delamater et al., 2019; Kucharski et al., 2020; Zhou et al., 2020), and those that infer the number of secondary infections per infected individual directly, based on a time series of infection incidence, (e.g. Wallinga and Teunis, 2004; Cori et al., 2013). We focus on the latter class of methods as they rely on few, simple assumptions, are less prone to model misspecifications, and are well-suited for ongoing monitoring of the epidemic (Gostic et al., 2020). In particular, we consider the EpiEstim method of Cori et al., 2013.

The infection incidence based methods face the difficulty that infection events cannot be observed directly (Gostic et al., 2020). These events can only be surmised with a certain time lag, e.g. when individuals show symptoms and are tested, via contact tracing, or via periodic testing of a cohort of individuals (Nishiura and Chowell, 2009). To use these methods, one must thus employ a proxy for infection events (e.g. the observed incidence of confirmed cases, hospitalisations, or deaths). This proxy is either used directly in lieu of the infection incidence, or it is used as an indirect observation to infer past infections (Gostic et al., 2020). It is important to relate $R_{e}$ estimates to the timing of infection events because this allows multiple proxies of infection events, with differing delays, to be used separately to monitor the same epidemic (Scire et al., 2020). In addition, any factors that may affect transmission dynamics will do so at the time infections occurred. If $R_{e}$ is placed properly on this timescale, it can be compared directly to external covariates like weather and interventions (Flaxman et al., 2020; Soltesz et al., 2020). However, depending on the method used to infer the timing of infections from the observed incidence time series, one can also introduce biases such as smoothing sudden changes in $R_{e}$ (Gostic et al., 2020; Goldstein et al., 2009; Petermann and Wyler, 2020).

Several methods, software packages, and online dashboards have been developed to monitor developments in $R_{e}$ during the SARS-CoV-2 pandemic (e.g. Abbott et al., 2020b; Systrom et al., 2020; Tebé et al., 2020; Scott et al., 2020; Hamouda, 2020; Richter et al., 2020). A pipeline for the continuous estimation of $R_{e}$ using infection incidence based methods should include four critical steps: (i) gathering and curating observable proxy data of infection incidence, (ii) reconstruction of the unobserved infection events, (iii) $R_{e}$ estimation, and (iv) communication of the results, including uncertainty and potential biases. These four axes also define the differences between existing methods. The first step dictates e.g. the geographical scope of the $R_{e}$ estimates reported. During the SARS-CoV-2 epidemic, many local public health authorities have made case data publicly available. Depending on the data sources used, estimated $R_{e}$ values span from the scale of a city, region, country, or the entire globe (Systrom et al., 2020; Pan et al., 2020; Robert Koch-Institut, 2020). The second step, i.e. going from a noisy time series of indirect observations to an infection incidence time series, is technically challenging. Biases can be introduced easily, and accurately assessing the uncertainty around the inferred infection incidence is a challenge in itself (Gostic et al., 2020). For the third step, i.e. to estimate $R_{e}$ from a timeline of infection events, there are ready-to-use software packages (Cori et al., 2013; Obadia et al., 2012), which produce $R_{e}$ estimates along with an estimate of the uncertainty resulting from this step. Finally, the communication of results to the general public and decision makers is essential, but often overlooked. We present a pipeline, together with an online dashboard, for timely monitoring of $R_{e}$. We use publicly available data gathered by different public health authorities. Wherever possible, we show results obtained from different types of case reports (confirmed cases, hospitalisations or deaths). This allows comparison across observation types and to balance the biases inherent in the different types. Results are updated daily, and can be found on https://ibz-shiny.ethz.ch/covid-19-re-international/. The results of this method have been used directly in public health policy making in Switzerland for the past 2 years, and were also communicated by the Federal Office of Public Health on https://www.covid19.admin.ch/en/overview during that time. Through continuous engagement with the public, scientific experts, and thorough evaluation on simulated scenarios, we have created a robust and transparent method of enduring relevance for the current and future epidemics.

Because $R_{e}$ estimates reflect changes in virus transmission dynamics, they can be used to assess the impact of public health interventions. Prior work on the relative impact of specific non-pharmaceutical interventions on $R_{e}$ has shown conflicting results (Flaxman et al., 2020; Esra et al., 2020; Banholzer et al., 2021; Soltesz et al., 2020; Haug et al., 2020; Kohanovski et al., 2022). These differences can be attributed mostly to different model formulations (Soltesz et al., 2020; Sharma et al., 2020; Banholzer et al., 2022), including differing assumptions on the independence of NPIs (Sharma et al., 2020), differing timescales over which the effect of the NPI was analysed (Flaxman et al., 2020; Haug et al., 2020), whether the time point of the NPI was assumed fixed or allowed to vary (Kohanovski et al., 2022), and differing geographical scope. There is a need to address whether the strength of measures and the speed of their implementation resulted in a larger and faster decrease of $R_{e}$, and specifically whether highly restrictive lockdowns were necessary to achieve $R_{e}<1$. Further, it remains unclear how the impact of interventions differed across time and geographical regions. We add to this debate by using our $R_{e}$ estimates across geographical regions and timescales that include the lifting of many NPIs. While we cannot determine causal relationships, we use our method to assess likely associations.

## Results

### A pipeline to estimate the effective reproductive number of SARS-CoV-2

We have developed a pipeline to estimate the time-varying effective reproductive number of SARS-CoV-2 from observed COVID-19 case incidence time series (see Materials and Methods). The objective was to achieve stable estimates for multiple types of data, and with an adequate representation of uncertainty. At the core, we use the EpiEstim method (Cori et al., 2013) to estimate $R_{e}$ from a time series of infection incidence. To infer the infection incidence from a time series of (noisy) observations, we extended the deconvolution method by Goldstein et al. to deal with partially observed data and time-varying delay distributions (Gostic et al., 2020; Goldstein et al., 2009). We smooth the data prior to deconvolution to reduce numerical artefacts resulting from their weekly patterns and overall noisy nature. We compute point-wise 95% confidence intervals for the true $R_{e}$ values, using the union of a block bootstrap method, designed to account for variation in the case observations, and the credible intervals from EpiEstim. As observed incidence data we use COVID-19 confirmed case data, hospital admissions, and deaths (with type specific delay distributions, see Materials and Methods). We publish separate $R_{e}$ estimates for each of these types of incidence data. The most recent $R_{e}$ estimate lies further in the past than the most recent observed incidence data due to the delay between infection and case observation.

### Evaluation on simulated data

To evaluate our method, we used simulations of several epidemic scenarios (see Materials and Methods for more details). For each scenario, we specified an $R_{e}$ time series. The specified $R_{e}$ trajectories were parametrised in a piecewise linear fashion. To mimic the course of the COVID-19 outbreaks observed in many European countries in 2020 (Lemaitre et al., 2020), we started with $R_{e}$ values around 3, then dropped to a value below 1 (the ‘initial decrease’), stayed around 1 in summer and slightly above 1 (the ‘second wave’) in autumn (Figure 1). From each specified $R_{e}$ trajectory, we stochastically simulated 100 time series of infections and their resulting case observations. To account for reporting effects and to better mimic observed COVID-19 case data from around the world, we added additional autocorrelated noise to the case observations.

![Figure 1.](https://cdn.elifesciences.org/articles/71345/elife-71345-fig1-v2.jpg)

**Figure 1.:** (A) The specified $R_{e}$ trajectory (black line) was used to stochastically simulate 100 trajectories of observed cases. From each trajectory, we estimated $R_{e}$ (yellow boxplots) and constructed a 95% confidence interval (purple boxplots of the lower/upper endpoint). (B) Fraction of simulations for which the true $R_{e}$ value was within the 95% confidence interval. The dashed red line indicates the nominal 95% coverage. (C) Root mean squared relative error for every time point. (D) Fraction of simulations for which $R_{e}$ is estimated to be significantly above or below one, depending on the true value of $R_{e}$.

We then used our method to infer the infection incidence and $R_{e}$ from each simulated time series of case observations, and compared these to the true underlying $R_{e}$ values (Figure 1). The results show that the method accurately estimates the effective reproductive number (Figure 1; metrics described in Materials and Methods). Across most time points, the 95% confidence interval includes the true $R_{e}$ value (coverage; Figure 1B). The low root mean squared error (RMSE) indicates that our point estimates closely track the true $R_{e}$ value (Figure 1C). Importantly, we correctly infer whether $R_{e}$ is significantly above or below 1 in this scenario: we never infer that $R_{e}$ is significantly above 1 when the true value is below 1, and only for two time points the estimates are significantly below 1 for some simulations when the true value is a little above 1 (Figure 1D). Due to the smoothing step prior to deconvolution, we slightly misestimate $R_{e}$ during steep changes (see Appendix 2, and Appendix 3—figure 1 for more scenarios). However, the inclusion of smoothing greatly improves the performance across scenarios with different types of observation noise (Appendix 3—figures 2 and 3). For a wide range of infection incidences, the 95% confidence interval is informative and covers the true value of $R_{e}$ (Appendix 3—figures 4 and 5). Our block-bootstrapping method greatly improves coverage compared to the out-of-the-box EpiEstim method. Our method also outperforms the common approach of using a fixed delay to infer the infection incidence time series (Appendix 3—figure 6).

We further tested the impact of misspecifying the delay between infections and observations. Misspecifying the mean of the delay distribution between infection and case observation by up to 2 days does not have a strong effect on the $R_{e}$ estimates, whereas larger misspecifications by 5 or 10 days lead to a more substantial decrease in coverage (Appendix 3—figure 7). Correspondingly, allowing for time-varying delay distributions has a pronounced effect on the estimated $R_{e}$ only when changes in the mean of the delay distribution are large (Appendix 3—figure 8). The impact of other model misspecifications, e.g. of the generation time interval, have been investigated by Gostic et al., 2020 for this class of methods.

### Stability of the Re estimates in an outbreak monitoring context

As our $R_{e}$ estimates for SARS-CoV-2 were directly policy relevant in Switzerland, we investigated their stability as new data becomes available (up to 21 additional days of data; Figure 2). With each new day of incidence data, it becomes possible to estimate $R_{e}$ for an additional day in the past. The most recent available $R_{e}$ estimate will be delayed with respect to the observed case incidence by at least the median delay from infection to observation to ensures sufficient information is available in the data (and can be delayed further if required; see below). As time passes and more observations become available, one can estimate more recent values of $R_{e}$. Importantly, the estimated $R_{e}⁢(t)$ for a day $t$ is updated whenever additional data is added. This means that the $R_{e}⁢(t)$ estimates initially change with each passing day before they settle on a long-term, stable value. In the analysis of Swiss COVID-19 case data in Figure 2B, $R_{e}$ estimates for Sept. 1 2020 to April 1 2021 based on data up to April 30 2021 are referred to as ‘stable $R_{e}$ estimates’. During rapid changes in the real $R_{e}$, the initial estimates for $R_{e}⁢(t)$ can occasionally under- or overshoot the long-term stable value. However, with our improved 95% confidence intervals (CI), the percentage of the first estimated CI for $R_{e}⁢(t)$ that is contained within the stable CI is substantially improved compared to purely EpiEstim-based uncertainty intervals (Figure 2). This difference is particularly striking during periods of high case incidence (e.g. October 2020), when the EpiEstim uncertainty interval is very narrow.

![Figure 2.](https://cdn.elifesciences.org/articles/71345/elife-71345-fig2-v2.jpg)

**Figure 2.:** Stability of the Swiss $R_{e}$ estimates based on confirmed COVID-19 cases, upon adding additional days of observations.(A) Line segments correspond to 3 weeks of estimates made with the same input data (e.g. data up to December 1st). The segments were assigned an arbitrary colour for ease of distinction. For each day, $R_{e}$ estimates and associated 95% confidence intervals (CIs) are overlaid, from the first possible estimate for that day up to estimates including 3 additional weeks of data. The latter, always the left end of a line segment, corresponds to the stable estimate. (B) Percentage of the first estimated CI that is contained in the stable CI based on data from 30 April 2021. This percentage was calculated as the width of the intersection of both CIs, divided by the width of the first CI. The colour indicates whether the stable $R_{e}$ estimate was contained in the first reported CI. In both rows, the left column shows uncertainty intervals from EpiEstim on the original data, and the right our improved 95% CIs. Both columns use the same pipeline, and differ only in the construction of the uncertainty intervals.

We complemented this analysis on empirical data with an assessment of the stability of $R_{e}$ estimates on synthetic data. Using the set-up described before, we simulated 4 $R_{e}$ scenarios: a constant trend, a slow increase, a slow decrease, and an abrupt decrease in $R_{e}$. Contrary to before, we estimated $R_{e}$ repeatedly, adding an additional day to the simulation in each iteration (Appendix 4—figure 1). For each scenario, we compare ‘raw’ $R_{e}$ estimates to trajectories for which the 4 most recent $R_{e}$ estimates were removed. This analysis shows that the last few $R_{e}$ estimates can lay outside of the stabilized confidence interval, in particular when the real $R_{e}$ trend is increasing. Instead, the truncated trajectories appear more stable as their most recent estimate has already been consolidated over 4 days. This highlights a trade-off between timeliness and accuracy when publishing $R_{e}$ estimates. On our online dashboard we present truncated $R_{e}$ estimates for Swiss cantons since these estimates were directly policy-relevant in Switzerland.

### Detailed data allows more precise analysis: the example of Switzerland

When detailed epidemiological data about individual cases is available (in the form of a line list), the precision of our method can be increased by relaxing the assumptions that (i) distributions of delays between infection and observation do not change through time and (ii) outbreaks occur in populations that are isolated at the country-level. In particular, we collaborated with the Federal Office of Public Health (FOPH) in Switzerland to relax these assumptions and further refine the monitoring of the Swiss SARS-CoV-2 epidemic.

The FOPH line list contains information on the delays between onset of symptoms and reporting - of a positive test, hospitalisation or death - for a substantial fraction of the reported cases. For each of these three types of case report, we estimate the time-varying empirical delay distribution for the delay from infection to reporting. We use this time-varying distribution as input to the deconvolution step, instead of the fixed delay distribution from the literature which is used for countries without an available line list (for details see Materials and Methods section 4.3). Each delay distribution is thus tailored to the specifics of the Swiss population and health system. Since each distribution varies through time, it reflects changes caused by e.g. improved contact tracing or overburdened health offices (see Appendix 4—figure 2; Appendix 1). Whenever available in the FOPH line list, we use the symptom onset date of patients as the date of observation and thus only deconvolve the incubation period to obtain a time series of infection dates. This was most relevant until early 2021, after which the date of symptom onset was rarely recorded anymore. For most days, the effect of these modifications on the $R_{e}$ point estimates is slight (Appendix 4—figure 3; shown for confirmed case data), yet the difference for a particular day can be as big as 20%.

Using FOPH data on the fraction of cases infected abroad, we can correct our $R_{e}$ estimate for imported cases. This is especially important in phases during which the local epidemic is seeded from abroad, and local transmission occurs at a low rate relative to case importation (Appendix 4—figure 4). This correction, which relies on EpiEstim (Cori et al., 2013), treats imported cases as pure infectors, and not infectees. It further assumes that imported cases transmit at the same rate as local cases. When this is not the case, e.g. when strict quarantines are imposed on travellers or travellers have more contacts compared to the rest of the population, and when a large fraction of all cases are imported, this can bias results (Tsang et al., 2021). Additionally, since we do not have data on the number of cases infected in Switzerland that are “exported" to other countries, we cannot correct for exports. Thus, the estimated $R_{e}$ value corrected for imports is a lower bound for the $R_{e}$ estimate which would be obtained if we could account for the location of infection of all cases detected in Switzerland or exported out of the country.

### Comparison with existing methods

During the COVID-19 pandemic, research groups and local public health authorities around the world developed and used methods to estimate the effective reproductive number (Abbott et al., 2020a; Scott et al., 2020; Hamouda, 2020; Richter et al., 2020). To put our method into context, we compare against EpiNow2, a prominent R-package to estimate (Abbott et al., 2020a), and the official $R_{e}$ estimates for Germany (developed by the Robert Koch-Institut, 2020; RKI Hamouda, 2020) and Austria (developed by the Austrian Agency for Health and Food Safety; AGES Richter et al., 2020). A detailed comparison of the structure and features of these methods —with the addition of the epidemia R-package (Scott et al., 2020)— can be found in Supplementary file 2. To the best of our knowledge, our method is the only one that can account for variations through time in delay distributions and combine symptom onset data with case data.

We compiled publicly available $R_{e}$ estimates for Switzerland, Austria and Germany from these research groups and institutions (Figure 3; Abbott et al., 2022; Heiden, 2021; TU Graz AGES, 2021). In this case the underlying truth is unknown, yet we can compare how well the point estimates and confidence intervals correspond between different methods. Both the RKI and AGES publish very narrow confidence intervals, which are unlikely to accurately capture the uncertainty around the estimates (similar to Figure 2). In addition, the trend of AGES estimates appear shifted closer to the present than our estimates (Figure 3). This is because AGES applies EpiEstim directly to observed case data, thus indirectly assuming that case confirmation occurs on the day of infection. The estimates from EpiNow2 and ours follow a qualitatively similar trend, although the EpiNow2 estimates are smoother and there is a small lag between both estimates, likely due to differences in the specified observation delay distribution. An in-depth comparison exploring the accuracy and stability of estimates produced by all available methods lies beyond the scope of this work, but would certainly be beneficial to give a full picture of the state-of-the-art of $R_{e}$ estimation methods.

![Figure 3.](https://cdn.elifesciences.org/articles/71345/elife-71345-fig3-v2.jpg)

**Figure 3.:** Comparison of published $R_{e}$ estimates for three countries.Point estimates are presented with a solid line and 95% confidence intervals are presented as coloured ribbons.

### Monitoring Re during the COVID-19 pandemic

We developed an online dashboard (https://ibz-shiny.ethz.ch/covid-19-re-international/) on which we present daily-updated results of this $R_{e}$ estimation method applied to COVID-19 case data from 170 countries (Figure 4). For most countries, we include multiple observation sources, such as daily incidence of COVID-19 cases and deaths, and, when available, hospital admissions. We estimate $R_{e}$ separately from each incidence type and make the estimates available for download, as an open resource for other researchers and the general public alike.

![Figure 4.](https://cdn.elifesciences.org/articles/71345/elife-71345-fig4-v2.jpg)

**Figure 4.:** (A) Swiss case incidence with evidence of weekly testing patterns (top row), $R_{e}$ estimates with associated 95% confidence intervals from four types of observation data (middle row), and timeline of stringency index and vaccination coverage (bottom row). (B) World map of incidence per 100’000 inhabitants over the last 14 days. One can also display the worldwide $R_{e}$ estimates instead. (C) Comparison of $R_{e}$ estimates across four countries (Austria, Chile, India and Morocco), with timelines of stringency indices and vaccination coverage. All panels were extracted on May 12, 2022. Dashboard url: https://ibz-shiny.ethz.ch/covid-19-re-international.

The online app allows for comparison through time within a single country, between multiple observation traces, and between multiple countries. The data download further allows users to put these estimates in relation to external covariates such as mobility, weather, or behavioural data. The map view enables comparison across larger geographical areas and additionally reports the cases per 100’000 inhabitants per 14 days. We additionally show the Oxford Stringency Index and vaccination coverage for context (Hale et al., 2021; Roser et al., 2020).

### The effect of lockdowns in spring 2020 on the estimated Re of SARS-CoV-2

We assessed the association between non-pharmaceutical interventions (NPIs) and the estimated effective reproductive number $R_{e}$ during the early stage of the COVID-19 pandemic. We selected 20 European countries for which the reported data was free of major gaps or spikes, and for which we could estimate $R_{e}$ prior to the nationwide implementation of a lockdown in spring 2020. The dates of interventions were extracted from news reports (sources listed in Appendix 6—table 2), and ‘lockdown’ taken to refer to stay-at-home orders of differing intensity. Of the countries investigated, all except Sweden implemented a lockdown (19/20). Using case data, we inferred that $R_{e}$ was significantly above one prior to the lockdown measures in nearly all countries with a lockdown (15/19; Table 1). Denmark, which had a complex outbreak consisting of two initial waves, and Germany, which experienced a cluster of early cases, had an estimated $R_{e}$ significantly below one prior to this date. For countries with very short delays between the lockdown and the estimated date that $R_{e}<1$ (e.g. Austria, Switzerland) we can not exclude the possibility that the ‘true’ $R_{e}$ may have been below 1 prior to the lockdown since our pipeline introduces smoothing to the estimates (see Appendix 2). The results are remarkably consistent across the different observation types (Appendix 6—table 1). However, the 95% confidence intervals tend to be wider for the estimates based on death incidence data because the number of deaths is much smaller than the number of cases, and the relative noise in observations tends to be higher.

**Table 1.**
 Investigating the relation between the date of ‘lockdown’ and the date when the estimated $R_{e}$ based on case reports dropped below 1.Based on news reports, we report when a country implemented stay-at-home orders (a ‘lockdown’). The column ‘$R^_{e}<1$’ indicates when the $R_{e}$ point estimate first dropped below 1. The column ‘CI includes 1’ details the corresponding time interval where the 95% confidence interval included 1. Of the investigated countries that implemented a nationwide lockdown, four (Denmark, Germany, the Netherlands, Slovenia) had 95% confidence intervals that included 1 or were below before a nationwide lockdown was implemented. The column ‘Time until $R^_{e}<1$’ indicates the number of days between the lockdown and the date that the $R_{e}$ point estimate dropped below 1.


<table>
  <thead>
    <tr>
      <th>Country</th>
      <th>Lockdown</th>
      <th>Re &lt;1</th>
      <th>CI includes 1</th>
      <th>Time until Re &lt;1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Austria</td>
      <td>16–30</td>
      <td>20–30</td>
      <td>[20-03, 20-03]</td>
      <td>4 days</td>
    </tr>
    <tr>
      <td>Belgium</td>
      <td>18–30</td>
      <td>30–30</td>
      <td>[25-03, 03-04]</td>
      <td>12 days</td>
    </tr>
    <tr>
      <td>Denmark</td>
      <td>18–30</td>
      <td>≤10–03</td>
      <td>[≤10–03, 20–06]</td>
      <td>–8 days</td>
    </tr>
    <tr>
      <td>Finland</td>
      <td>16–30</td>
      <td>01-Feb</td>
      <td>[29-03, 30-04]</td>
      <td>17 days</td>
    </tr>
    <tr>
      <td>France</td>
      <td>17–30</td>
      <td>27–30</td>
      <td>[23-03, 07-04]</td>
      <td>10 days</td>
    </tr>
    <tr>
      <td>Germany</td>
      <td>22–30</td>
      <td>18–30</td>
      <td>[17-03, 19-03]</td>
      <td>–4 days</td>
    </tr>
    <tr>
      <td>Ireland</td>
      <td>27–30</td>
      <td>01–100</td>
      <td>[04–04, 15–04]</td>
      <td>12 days</td>
    </tr>
    <tr>
      <td>Italy</td>
      <td>01–300</td>
      <td>18–30</td>
      <td>[17-03, 19-03]</td>
      <td>8 days</td>
    </tr>
    <tr>
      <td>Netherlands</td>
      <td>23–30</td>
      <td>01-Jan</td>
      <td>[22-03, 10-04]</td>
      <td>13 days</td>
    </tr>
    <tr>
      <td>Norway</td>
      <td>14–30</td>
      <td>21–30</td>
      <td>[17-03, 19-03]</td>
      <td>7 days</td>
    </tr>
    <tr>
      <td>Poland</td>
      <td>25–30</td>
      <td>01-Jan</td>
      <td>[31-03, 17-04]</td>
      <td>8 days</td>
    </tr>
    <tr>
      <td>Portugal</td>
      <td>16–30</td>
      <td>28–30</td>
      <td>[23-03, 15-04]</td>
      <td>12 days</td>
    </tr>
    <tr>
      <td>Romania</td>
      <td>24–30</td>
      <td>01-Jun</td>
      <td>[31-03, 29-04]</td>
      <td>13 days</td>
    </tr>
    <tr>
      <td>Russian Federation</td>
      <td>30–30</td>
      <td>01-Apr</td>
      <td>[01–05, 08–05]</td>
      <td>35 days</td>
    </tr>
    <tr>
      <td>Slovenia</td>
      <td>20–30</td>
      <td>23–30</td>
      <td>[≤13–03, 26–03]</td>
      <td>3 days</td>
    </tr>
    <tr>
      <td>Spain</td>
      <td>14–30</td>
      <td>26–30</td>
      <td>[25-03, 26-03]</td>
      <td>12 days</td>
    </tr>
    <tr>
      <td>Sweden</td>
      <td></td>
      <td>01-Jan</td>
      <td>[06–03,≥03-05-2021]</td>
      <td></td>
    </tr>
    <tr>
      <td>Switzerland</td>
      <td>17–30</td>
      <td>22–30</td>
      <td>[20-03, 22-03]</td>
      <td>5 days</td>
    </tr>
    <tr>
      <td>Turkey</td>
      <td>21–30</td>
      <td>01-Aug</td>
      <td>[01–04, 13–04]</td>
      <td>18 days</td>
    </tr>
    <tr>
      <td>United Kingdom</td>
      <td>24–30</td>
      <td>30–30</td>
      <td>[28-03, 20-04]</td>
      <td>6 days</td>
    </tr>
  </tbody>
</table>

To consider the association between NPIs and the estimated $R_{e}$ for countries outside of Europe, we used the stringency index (SI) of the Blavatnik School of Government (Hale et al., 2020) to describe the public health response in different countries (Figure 4C). This is a compound measure describing e.g. whether a state has closed borders, schools, or workplaces. For example, a country with widespread information campaigns, partially closed borders, closed schools, and a ban on public events and gatherings with more than 10 people would have an SI slightly above 50. As reference date, we used the date when a country first exceeded a stringency index of 50 ($t_{S⁢I⁢50}$). Then, we investigated whether the estimated $R_{e}$ was significantly above 1 prior to the reference date (i.e. the lower bound of the 95% confidence interval was above 1). We excluded countries without $R_{e}$ estimates before the reference date $t_{S⁢I⁢50}$. Worldwide, for 35 out of the 42 countries which fulfilled the criteria for inclusion (list in Appendix 6), $R_{e}$ was significantly above 1 prior to $t_{S⁢I⁢50}$. As a sensitivity analysis, we performed the same calculation with a different reference date $t_{m⁢a⁢x}$, defined as the date with the biggest increase in SI in the preceding 7 days. The results were very similar, with 38/45 countries significantly above one before $t_{m⁢a⁢x}$ (Appendix 6).

### Insights into continent-specific impacts of NPIs

To further investigate the association between non-pharmaceutical interventions and changes in the estimated reproductive number of SARS-CoV-2, we extended our analysis beyond the first 2020 epidemic wave. We included both the implementation and lifting of NPIs until May 3rd 2021 (increases and decreases in stringency). For each week and each country, we calculated the change in stringency index over the preceding week ($Δ⁢S⁢I_{t}=S⁢I⁢(t)-S⁢I⁢(t-7)$) and the corresponding change in the estimated $R_{e}$ (during the same week $Δ⁢R^_{e,t}=R^_{e}⁢(t)-R^_{e}⁢(t-7)$, 1 week later $Δ⁢R^_{e,t+7}=R^_{e}⁢(t+7)-R^_{e}⁢(t)$, or 2 weeks later $Δ⁢R^_{e,t+14}=R^_{e}⁢(t+14)-R^_{e}⁢(t)$). If NPIs were effective, we expect increases in stringency to be associated with decreases in the estimated $R_{e}$ and vice versa. We do find such an association for increases in stringency e.g. in Europe. In Europe we also see that large increases in stringency are associated with larger decreases in $R_{e}$ 7–14 days after the change in SI. However, the association between decreases in stringency and changes in $R_{e}$ is heterogeneous on all continents (Figure 5A). This suggests that reversing non-pharmaceutical interventions had a different effect than introducing them.

![Figure 5.](https://cdn.elifesciences.org/articles/71345/elife-71345-fig5-v2.jpg)

**Figure 5.:** The association between the implementation or lifting of non-pharmaceutical interventions and changes in $R_{e}$ until May 2021.(A) The change in the estimated $R_{e}$ at the same time as ($R⁢(t)$) or following ($R⁢(t+7)$ and $R⁢(t+14)$) the implementation (above x-axis) or lifting (below x-axis) of NPIs in a given week. (B) The change in the estimated $R_{e}$ related to the change in mobility in the same week. The error bars indicate the Q1 and Q3 quartiles.

We repeated the same analysis for Europe, comparing against various measures of Google mobility data (Figure 5B). Increased mobility in residential areas, and decreased mobility at workplaces or grocery stores is associated with decreases in $R_{e}$.

## Discussion

We have developed a pipeline to estimate the effective reproductive number $R_{e}$ of SARS-CoV-2 for both timely monitoring and retrospective investigation. We evaluated our estimates on simulated data. We showed that the inferred $R_{e}$ curve can be over-smoothed on simulated data, but that this disadvantage is outweighed by the increased stability of the estimates. Overall, we show that the relative error in the $R_{e}$ estimates is small.

During the ongoing SARS-CoV-2 pandemic, $R_{e}$ estimates are of interest to health authorities, politicians, decision makers, the media and the general public. Because of this broad interest and the importance of $R_{e}$ estimates, it is crucial to communicate both the results as well as the associated uncertainty and caveats in an open, transparent and accessible way. This is why we display daily updated results on an online dashboard, accessible at https://ibz-shiny.ethz.ch/covid-19-re-international/. The dashboard shows $R_{e}$ estimates in the form of time series for each included country or region, and a global map containing the latest $R_{e}$ estimates and normalised incidence. For all countries, we further display a timeline of the stringency index of the Blavatnik School of Government (Hale et al., 2021), and current vaccination coverage.

A unique advantage of the monitoring method we have developed is the parallel use of different types of observation data, all reflecting the same underlying infection process (Scire et al., 2020). Wherever we have data of sufficient quality, we estimate $R_{e}$ separately based on confirmed cases, hospitalisations and death reports. The advantages and disadvantages of the different observation types are discussed in the Appendix 1. Comparing estimates from several types of data is a powerful way to evaluate the sensitivity of the results to the type of observations they were derived from. More generally, the method is applicable to any other type of incidence data, such as admissions to intensive care units or excess death data. We have also extended this method to make use of daily measurements of SARS-CoV-2 viral concentrations in wastewater (Huisman et al., 2022). The potential limitations of our $R_{e}$ estimation method are discussed in detail in the Appendix 1.

Any decision to implement, remove or otherwise adjust measures aimed at infection control will be informed by epidemiological, social and economic factors (Sebhatu et al., 2020). We can aid this decision making process by investigating the association between adjustments of public-health measures and the estimated $R_{e}$. In particular, the merits of nation-wide lockdowns in the context of the COVID-19 pandemic have been heavily discussed, both in the scientific literature and the public sphere (Flaxman et al., 2020; Haug et al., 2020; Banholzer et al., 2021; Soltesz et al., 2020; Karberg, 2020). Analyses showing that $R_{e}$ estimates had dropped below 1 before the strictest measures were enforced were frequently used to claim that a lockdown was not necessary (Karberg, 2020). We showed that this argumentation cannot be applied universally: for 15 out of 20 European countries, we found that the estimated $R_{e}$ was significantly above 1 prior to the lockdown in spring of 2020. Interestingly, the result we obtain for Germany critically depends on whether we use symptom onset data, or more widely available case reports.

Extending our analysis beyond the first wave, we find differences between continents in the association between changes in the stringency of NPIs and changes in $R_{e}$. This could reflect differences in the speed with which lockdowns were put into practice (Kohanovski et al., 2022), the de facto lockdown stringency, or socio-cultural aspects (Sebhatu et al., 2020; Mbow et al., 2020). It is often argued that, especially in countries with a large informal business sector, there may be a difference between the official containment measures and those adhered to or implemented de facto (Mbow et al., 2020). However, for continents where we find no significant correlation, this could also be because a large fraction of NPIs were implemented at a time for which we could not estimate changes in $R_{e}$. Many African countries had early and strict government responses, often prior to the first detected cases. These are thought to have delayed the virus in establishing a foothold on the continent (Mbow et al., 2020).

Importantly, our analysis suggests that reversing non-pharmaceutical interventions may have a very different effect than introducing them. This could be because the situation is not fully reverted: due to increased public awareness, testing, contact tracing, and quarantine measures still in place. In addition, the epidemic situation - in terms of number of infected individuals - is likely different when measures are implemented or lifted.

Our analysis could be confounded by economic, social, and psychological factors motivating the implementation or release of measures. With the current stringency measures we cannot account for diversity in adherence to NPIs across geographic regions and through time. Cultural norms, defiance towards public authorities, "lockdown fatigue", and economic pressures are all among the factors that may determine whether NPIs are in fact adhered to. In addition, there is increasing evidence that weather may be a factor influencing $R_{e}$ through its effect on people’s behaviour and on properties of the virus (Morris et al., 2021). In the future, our tools to estimate $R_{e}$ could be used to explore associations of these many factors with $R_{e}$ estimates, with the aim of identifying minimal sets of factors that may ensure an $R_{e}<1$ for a particular location.

## Materials and methods

### Overview of the software pipeline

The software pipeline we developed allows the estimation of $R_{e}$ from different proxies for the infection incidence, such as the time series of confirmed cases, hospitalisations or deaths. It provides a separate estimate of the $R_{e}$ trajectory through time for each proxy. In a first step, we smooth the case observations and deconvolve the smoothed observations by the type-specific delay distribution to obtain an estimate of the infection incidence time series. Second, we use the package EpiEstim to estimate the effective reproductive number Re from this infection incidence. We assess the uncertainty in the estimates using the union of a block bootstrap method, designed to account for variation in the case observations, and the credible intervals from EpiEstim.

### Smoothing the case observations

To reduce the influence of weekly patterns in case reporting data, as well as reporting irregularities, we smooth the observed incidence data prior to deconvolution. To smooth the incidence data, we use local polynomial regression (LOESS) with 1st order polynomials and tricubic weights. The smoothing parameter alpha is set such that we include 21 days of data in the local neighbourhood of each point. After smoothing, we normalise to the original total number of cases. Here we use smoothing parameter 21 because it performs best overall in our simulations. We investigated the effect of this tuning parameter in simulations, see Appendix 5—figure 5.

### Estimating the infection incidence through deconvolution

To recover the non-observed time series of infection incidence, we deconvolve the smoothed observed time series of COVID-19 case incidence with a delay distribution specific to the type of case detection (case confirmation, hospital admission, death). To this end, we extended the deconvolution method of Goldstein et al., 2009, which is itself an adaptation of the Richardson-Lucy algorithm (Richardson, 1972; Lucy, 1974) (essentially an expectation maximisation algorithm), to deal with zero-incidence case observations and time-varying delay distributions.

Formally, the method infers a deconvolved output time series $(\lambda_{1},…,\lambda_{N})$ from an input time series $(D¯_{K},…,D¯_{N})$, where $K\geq1$ and $D¯_{i}$ indicates the smoothed number of observations on day $i$ (e.g. confirmed cases, hospitalisations, or deaths). Let $m_{l}^{j}$ be the probability that an infection on day $j$ takes $l\geq0$ days to be observed. If no line list data is available, $m_{l}^{j}=m_{l}$ and no time-variation of the delay distribution is assumed. Let qj be the probability that an infection that occurred on day $j$ is observed during the time-window of observations, i.e. is counted towards $(D¯_{K},…,D¯_{N})$. Then:

$$
q_{j}=\sum_{l=K-j}^{N-j}m_{l}^{j}.
$$

Let $E_{i}$ be the expected number of observed cases on day $i$, for a given infection incidence $(\lambda_{k})$:

$$
E_{i}={\sumj=1i\lambda_{j}m_{i−j}^{j}forK\geqi\geqN0for0<i<K.
$$

The deconvolution algorithm uses expectation maximisation (Dempster et al., 1977) to find a final infection incidence estimate, which has the highest likelihood of explaining the observed input time series. To do so, it starts from an initial guess of the infection incidence time series $Λ^{0}=(\lambda_{1}^{0},…,\lambda_{N}^{0})$, used to compute $E_{i}^{0}$ according to equation 2, and updates the estimate in each iteration $n$ according to the following formula:

$$
\lambda_{j}^{n+1}=\frac{\lambda_{j}^{n}}{q_{j}}⋅\sumi=KN\frac{m_{i-j}^{j}⁢D¯_{i}}{E_{i}^{n}}.
$$

The iteration proceeds until a termination criterion is reached. Here, we follow Goldstein et al. and iterate until the $χ^{2}$ statistic drops below 1 (Goldstein et al., 2009):

$$
χ^{2}=\frac{1}{N-K+1}⁢\sumi=KN\frac{(E_{i}^{n}-D¯_{i})^{2}}{E_{i}^{n}},
$$

or 100 iterations have been reached.

Convergence is typically fast and the stopping criterion based on the $χ^{2}$ statistic is reached in a few iterations. Due to the smoothing prior to deconvolution, this is the case for the vast majority of the empirical data we analyzed. In some cases, e.g. when the observed incidence is especially noisy, convergence is slower and the threshold of 100 iterations is reached (on 26.5.2022, this was the case for 13 of the countries analyzed).

For the initial estimate of the incidence time series $Λ^{0}$, we shift the observation time series backwards in time by the mode of the delay distribution μ Goldstein et al., 2009. However, this leaves a gap of unspecified values at the start and end of the time series $Λ_{0}$. Contrary to Goldstein et al., we augment the shifted time series with the first observed value ($D¯_{K}$) on the left, and with the last observed value ($D¯_{N}$) on the right, to avoid initialising with a zero-value anywhere. If a day is initialised with zero incidence, it will also have zero incidence in the final estimate (compare equation (3)), which would be a potential source of bias.

We note that the Richardson-Lucy deconvolution algorithm accounts for ‘right truncation’, i.e. that not all infections are observed within the given observation time window (due to delay until symptoms/reporting), through the qj indices.

### Use of line list data

When information on the time variation of delays between symptom onset and observation is available (e.g. through a line list), this can be taken into account directly during the deconvolution step. In this case, we perform the deconvolution in two separate steps: first with the time-varying empirical onset-to-observation distributions, and then with the constant-through-time incubation period distribution. For those cases where symptom onset data is available, we only deconvolve with the incubation period distribution.

The $(m_{0}^{j},…,m_{l_{m⁢a⁢x}}^{j})$ time-varying delay distributions from onset of symptoms to observation are determined as follows: for each date $j$, at least 300 of the most recent recorded delays between symptom onset and observation, with onset date before $j$, are taken into account; $l_{m⁢a⁢x}$ being the highest observed delay. To avoid biases caused by the intensity of testing and reporting varying throughout the week, recorded delays are included in full weeks going in the past, until at least 00 delays are included.

As the incidence data is right-truncated, we have to fix the distribution for the reporting delay ($m_{l}^{j}$) after a certain day $j$, so that delay distributions are not downward biased for infection dates close to the present. Let $(m¯_{0},…,m¯_{l_{m⁢a⁢x}})$ be the empirical probability density function of the delay (aggregated over the entire window of observations) and $n$ the 99th percentile of this distribution ($n$ is the smallest integer for which $\sumi=1nm¯_{i}\geq0.99$). For infection dates $z$ that are closer to the present than $n$ (i.e. $N−z<n$, where $N$ is the index of the last available data point), we fix $(m_{0}^{z},…,m_{l_{m⁢a⁢x}}^{z})$ to be equal to $(m_{0}^{N-n},…,m_{l_{m⁢a⁢x}}^{N-n})$.

### Estimating the effective reproductive number Re

Once we have obtained an estimate for the time series of infection incidence, we use the method developed by Cori et al., 2013, implemented in the EpiEstim R package, to estimate $R_{e}$.

Disease transmission is modelled with a Poisson process. At time $t$, an individual infected at time $t-s$ causes new infections at a rate $R_{e}⁢(t)⋅w_{s}$, where ws is the value of the infectivity profile $s$ days after infection. The infectivity profile sums to 1, and can be approximated by the (discretised) serial interval distribution (Cori et al., 2013). The likelihood of the incidence $I_{t}$ at time $t$ is thus given by:

$$
P⁢(I_{t}|I_{0},…,I_{t-1},R_{e}⁢(t))=\frac{(R_{e}⁢(t)⁢Λ_{t})^{I_{t}}⁢e^{-R_{e}⁢(t)⁢Λ_{t}}}{I_{t}!},
$$



$$
where    Λ_{t}=\sum_{s=1}^{t}I_{t-s}⁢w_{s}.
$$

The $R_{e}$ inference is performed in a Bayesian framework, and an analytical solution can be derived for the posterior distribution of $R_{e}⁢(t)$ (see Cori et al., 2013; Web Appendix 1). We choose a gamma distributed prior on $R_{e}⁢(t)$ with mean 1, and standard deviation 5.

For the gradually-changing $R_{e}$ estimates, we assume $R_{e}$ is constant over a sliding window of 3 days ($\tau=3$ in EpiEstim), i.e. the reported $R_{e}$ estimate for day $T$ summarises the average $R_{e}$ over a 3 day period ending on day $T$. In addition to these smooth estimates, we provide step-wise estimates of $R_{e}$ on our dashboard. In the step-wise analysis, $R_{e}$ is assumed to be constant on a number of intervals spanning the entire epidemic time window. These intervals are determined by dates at which public health interventions were implemented, altered, or lifted. All results reported here are based on the smooth $R_{e}$ estimates. In both cases, we use the mean of the posterior distribution of $R_{e}$ as the point estimate.

### Estimating the uncertainty intervals

To account for the uncertainty in the case observations, we construct 95% bootstrap confidence intervals for $R_{e}$. We first re-sample case observations as follows: given the original case observations $D_{t},t=K,…,N$, we apply the LOESS with smoothing parameter 21 days on the log-transformed data $l⁢o⁢g⁢(D_{t}+1)$ to obtain the smoothed value $\mu^_{t}$ and additive residuals et. Here we use log-transformation to stabilise the variance of the residuals because it is the best overall choice among the transformations we tried. We compare to the commonly used square root transformation in Appendix 5—figure 1.

After obtaining the residuals et, we resample them to get bootstrap residuals $e_{t}^{*}$ and obtain the bootstrap case observations by

$$
D_{t}^{*}=max⁡(exp⁡(\mu^_{t}+e_{t}^{*})-1,0).
$$

We now discuss how we obtain a set of bootstrapped residuals $e_{t}^{*}$, $t=K,…,N$. Since the empirical residuals of most countries are autocorrelated (see Appendix 5—figure 2), we use an overlapping block bootstrap. Specifically, given the original residuals $(e_{K},…,e_{N})$, we start by taking a random block of $b$ consecutive residuals, which we denote by $(e_{1}^{*1},…,e_{b}^{*1})$. To account for weekly patterns in the case observations, we need to match the day of the week to the original case observations. That is, we keep the longest subvector $(e_{m_{1}}^{*1},…,e_{b}^{*1})$ of $(e_{1}^{*1},…,e_{b}^{*1})$ such that $e_{m_{1}}^{*1}$ has the same day of the week as $e_{K}$ (e.g., both correspond to Fridays). We then randomly take a new block of $b$ consecutive residuals, which we denote by $(e_{1}^{*2},…,e_{b}^{*2})$. We keep its longest part $(e_{m_{2}}^{*2},…,e_{b}^{*2})$ such that $e_{m_{2}}^{*2}$ has the day of the week that follows on that of $e_{b}^{*1}$ (e.g. if $e_{b}^{*1}$ corresponds to a Tuesday, then $e_{m_{2}}^{*2}$ must correspond to a Wednesday). We then glue these two sampled blocks together to get $(e_{m_{1}}^{*1},…,e_{b}^{*1},e_{m_{2}}^{*2},…,e_{b}^{*2})$. We repeat this process of adding blocks until the length of the re-sampled residuals is at least as large as that of the original residuals. If it is longer, we simply cut off the last part of the re-sampled residuals so that its length is the same. Finally, we re-index the re-sampled residuals as $(e_{K}^{*},…,e_{N}^{*})$. We present a concrete example in Appendix 2.

Choosing an optimal block size $b$ for the block bootstrap method is generally difficult. To capture week effects, we need a block size of at least 7. We tried different sizes and found that $b=10$ tended to work well in various simulation settings (Appendix 5—figure 6).

Given a set of bootstrap case observations $(D_{K}^{*},…,D_{N}^{*})$, we apply our method to obtain an estimate for $R_{e}⁢(t)$. For ease of notation, we now denote this by $\theta^^{*}⁢(t)$. By repeating the above steps 100 times, we obtain $\theta^_{1}^{*}⁢(t),…,\theta^_{100}^{*}⁢(t)$. Then, we construct a Normal based bootstrap confidence interval for each time point $t$ by:

$$
[\theta^⁢(t)-q_{z}⁢(1-\frac{\alpha}{2})⁢s⁢d^⁢(\theta^^{*}⁢(t)),\theta^⁢(t)+q_{z}⁢(1-\frac{\alpha}{2})⁢s⁢d^⁢(\theta^^{*}⁢(t))],
$$

where $\theta^⁢(t)$ denotes the estimated $R_{e}⁢(t)$ based on the original case observations, $q_{z}⁢(1-\frac{\alpha}{2})$ denotes the $1-\frac{\alpha}{2}$ quantile of the standard normal distribution, and $s⁢d^⁢(\theta^^{*})$ denotes the empirical standard deviation of $\theta^_{1}^{*}⁢(t),…,\theta^_{100}^{*}⁢(t)$. In this paper, we aim at a confidence interval level of 95%, so $\alpha=0.05$. We use the Normal based bootstrap interval because we found that it performed best overall with respect to coverage in our simulations, when compared to other common choices like quantile and reversed-quantile bootstrap confidence intervals (Appendix 3—figure 3).

The above bootstrap method implicitly assumes that the variance of the residuals et is constant over time $t$ and does not depend on the value of the log-transformed data $log⁡(D_{t}+1)$. This assumption roughly holds when the case incidence is high. During periods of low case incidence (e.g. deaths or regional data in summer 2020 in Switzerland), this assumption is no longer appropriate. Therefore, to be conservative and rather err on the side of too wide uncertainty intervals, we also consider the credible interval of $R_{e}$ which is obtained by taking the 0.025 and 0.975 quantiles from the posterior distribution of $R_{e}⁢(t)$ using EpiEstim based on the original data $(D_{K},…,D_{N})$. The final reported interval is then the union of the credible interval and the 95% bootstrap confidence interval. Based on our experience, the credible interval is typically wider during periods of very low case incidence and will then be reported. But at high case numbers, the bootstrap confidence interval will tend to be much wider than the credible interval and will be the reported one.

Finally, we point out that the choices of transformation, block size, smoothing parameters and type of bootstrap confidence interval in this paper might not be universal. The best choice can be different for different data sets (e.g., data sets from different countries).

### Data

We gather case incidence data directly from public health authorities. Whenever accessible, we rely on data from local authorities. Otherwise, we use data from ‘Our World in Data’ since the European Centre for Disease Control (ECDC) has stopped its daily updates (December 2020) (Roser et al., 2020; European Centre for Disease Prevention and Control (ECDC), 2022). A table summarising the incidence data sources is available in Supplementary file 1. Information on the start and end of interventions, or major changes in testing policy, are obtained from media reports and the websites of public health authorities. The stringency index of the Blavatnik School of Government is accessed from their publicly available github repository (Hale et al., 2020). The vaccination coverage is taken from ‘Our World in Data’ (Roser et al., 2020).

We parametrise the discretised infectivity profile ws using COVID-19 serial interval estimates from the literature (Nishiura et al., 2020). For a review of published serial interval estimates, see Griffin et al. (Griffin et al., 2020). The incubation period is parametrised by a gamma distribution with mean 5.3 days and SD 3.2 days (Linton et al., 2020). For countries for which we do not have access to line list data, i.e. all except Switzerland, Germany and Hong Kong at the time of writing, we assume delays from symptom onset to observation to be gamma-distributed, with parameters taken from the literature. Table 2 summarises the distributions used in our pipeline.

**Table 2.**
 Gamma distributions used in the pipeline: serial interval, incubation period, and the delay distributions assumed for each observation type.


<table>
  <thead>
    <tr>
      <th>Distribution</th>
      <th>Mean (days)</th>
      <th>SD (days)</th>
      <th>Reference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Serial interval</td>
      <td>4.8</td>
      <td>2.3</td>
      <td>Nishiura et al., 2020</td>
    </tr>
    <tr>
      <td>Infection to onset of symptoms</td>
      <td>5.3</td>
      <td>3.2</td>
      <td>Linton et al., 2020</td>
    </tr>
    <tr>
      <td>Onset of symptoms to case confirmation</td>
      <td>5.5</td>
      <td>3.8</td>
      <td>Bi et al., 2020</td>
    </tr>
    <tr>
      <td>Onset of symptoms to hospital admission</td>
      <td>5.1</td>
      <td>4.2</td>
      <td>Pellis et al., 2021</td>
    </tr>
    <tr>
      <td>Onset of symptoms to death</td>
      <td>15.0</td>
      <td>6.9</td>
      <td>Linton et al., 2020</td>
    </tr>
  </tbody>
</table>

For Switzerland, Germany and Hong Kong, we use line lists to build time-varying empirical distributions on delays between symptom onset and case confirmation, hospitalisation or death. During the deconvolution step we use the empirical delay distribution of the last 300 recorded cases prior to the infection date. Moreover, for the fraction of cases for which the date of onset of symptoms is known, we use the onset date directly instead of deconvolving a delay from onset to reporting, allowing for more precise estimation of the infection date. For Switzerland, line lists contain information on which cases were infected abroad. By considering imported cases and locally-transmitted cases separately in the deconvolution step, we obtain two separate time series, one for local infections and one for imported infections. EpiEstim can then estimate a corrected $R_{e}$ that excludes infections incurred abroad from the local transmission dynamics.

For comparison between methods, epiforecasts.io $R_{e}$ estimates were collected from https://github.com/epiforecasts/covid-rt-estimates/blob/master/national/cases/summary/rt.csv, accessing file versions from December 5 2020, March 15, June 24, October 1, November 10 2021 and January 10 2022. Robert Koch Institute estimates were collected from https://raw.githubusercontent.com/robert-koch-institut/SARS-CoV-2-Nowcasting_und_-R-Schaetzung/main/Nowcast_R_aktuell.csv, last accessed on January 10 2022. AGES estimates were collected from https://www.ages.at/fileadmin/AGES2015/Wissen-Aktuell/COVID19/R_eff.csv, last accessed on January 10 2022.

### Simulations

In the simulations, we start by specifying different $R_{e}$ trajectories. To assess a range of scenarios, we parametrise $R_{e}$ as a piecewise linear trajectory, where we fix its plateau values and the time-points at which its slope changes. From each $R_{e}$ trajectory, we stochastically simulate 100 time series of infections and their corresponding case observations. We then use our pipeline to estimate $R_{e}⁢(t)$ from each of these 100 times series and compare it to the true underlying value of $R_{e}⁢(t)$.

Assuming I0 infected individuals on the first day, the infection incidence is simulated forward in time. The infection incidence on day $t$ is drawn from a Poisson distribution, corresponding to equation (6), using the specified $R_{e}$ time series and the discretised serial interval for SARS-CoV-2 (Nishiura et al., 2020) as the infectivity profile (see Cori et al., 2013; Web Appendix 11). These simulated infections are convolved with the observation type-specific delay distribution (Linton et al., 2020) to obtain the raw observation time series $D~_{t}$.

Since the raw observation time series $D~_{t}$ are too smooth compared to the real data (Appendix 5—figure 4), we add noise to obtain our final simulated observation time series $D_{t}$. The additional noise accounts for aspects of the observation process that are not covered by the delay distribution, such as weekend and holiday effects, the random and occasional delay in the recording of confirmed cases, and irregular components such as confirmed cases that are imported from abroad.

To obtain a realistic noise model for $D_{t}$, we considered the empirical noise observed in real SARS-CoV-2 case data. For most countries the residuals are autocorrelated (Appendix 5—figure 2), which led us to fit ARIMA models to the observed residuals. We considered five simulation settings with different noise models obtained based on the confirmed case data from five countries (Switzerland, China, France, New Zealand, United States of America). Specifically, we first apply the LOESS smoother with smoothing parameter 21 days on the log-transformed confirmed case data to obtain additive residuals. We then chose the ARIMA model by fitting ARIMA models of various orders and assessing the resulting ACF and PACF plots of their residuals. This leads to five ARIMA models: ARIMA(2,0,1)(0,1,1), ARIMA(1,0,1)(0,0,0), ARIMA(0,0,6)(0,1,1), ARIMA(4,0,1)(1,0,0), and ARIMA(4,0,0)(0,0,0), based on the data from CHE, CHN, FRA, NZL, and USA, respectively. The final observation time series $D_{t}=D~_{t}⋅exp⁡(e_{t})$, where et is simulated from the fitted ARIMA model. We present the simulated observations with the noise model based on CHE data in Appendix 5—figure 4. We emphasize that the ARIMA model is only used in simulations to obtain simulated observations that look roughly realistic. Our main approach to obtain the estimated $R_{e}$ and the related confidence intervals does not require fitting an ARIMA model. In particular, the block bootstrap method is fully non-parametric.

In the case of time-varying delay distributions, we assume that the mean of the delay distribution decreases by a fixed amount (1/20) each day, to a minimum of 2 days (e.g. for the confirmed cases this results in a range from 5.5 to 2). When estimating with a time-varying delay distribution, we draw observations from the true distributions, similar to line list information recorded by public health authorities. To assess the added value of the deconvolution method, we further compare against a method where we estimate the infection time series by shifting the observations back by the mean of the delay distribution (termed ‘fixed shift method’).

To quantify the performance of our method on the simulated scenarios, we compute the root mean squared error (RMSE) at time point $j$:

$$
R⁢M⁢S⁢E⁢(j)=\sqrt{\frac{1}{M}⁢\sum_{m=1}^{M}(R^_{e}⁢(j,m)-R_{e}⁢(j))^{2}},
$$

where $M$ is the total number of simulations, $R^_{e}⁢(j,m)$ the estimated $R_{e}$ and $R_{e}⁢(j)$ the true $R_{e}$ at time $j$, for simulation $m$.

For each simulation we also compute the 95% confidence interval (CI) of our estimates across 100 bootstrap replicates. The empirical coverage indicates the fraction of simulations for which our CI includes the true $R_{e}$ value.

### Implementation and method availability

Daily updated results of our method on global COVID-19 data are available online on https://ibz-shiny.ethz.ch/covid-19-re-international/.

The source code of the software pipeline is openly accessible at https://github.com/covid-19-Re/shiny-dailyRe; Angst, 2022, and the code necessary to reproduce the figures and analyses presented in this paper is available at https://github.com/covid-19-Re/paper-code; Huisman, 2022.
