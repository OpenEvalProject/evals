# A transmission-virulence evolutionary trade-off explains attenuation of HIV-1 in Uganda

## Authors

- François Blanquart<sup>1</sup> ([ORCID: 0000-0003-0591-2466](https://orcid.org/0000-0003-0591-2466)) †
- Mary Kate Grabowski<sup>4</sup>
- Joshua Herbeck<sup>6</sup> ([ORCID: 0000-0003-4577-7406](https://orcid.org/0000-0003-4577-7406))
- Fred Nalugoda<sup>8</sup>
- David Serwadda<sup>8</sup>
- Michael A Eller<sup>10</sup>
- Merlin L Robb<sup>10</sup>
- Ronald Gray<sup>4</sup>
- Godfrey Kigozi<sup>8</sup>
- Oliver Laeyendecker<sup>12</sup>
- Katrina A Lythgoe<sup>1</sup>
- Gertrude Nakigozi<sup>8</sup>
- Thomas C Quinn<sup>12</sup>
- Steven J Reynolds<sup>12</sup>
- Maria J Wawer<sup>4</sup>
- Christophe Fraser<sup>1</sup>

### Affiliations

1. MRC Centre for Outbreak Analysis and Modelling Imperial College London London United Kingdom
2. Department of Infectious Disease Epidemiology Imperial College London London United Kingdom
3. School of Public Health Imperial College London London United Kingdom
4. Department of Epidemiology Johns Hopkins University Baltimore United States
5. Bloomberg School of Public Health Johns Hopkins University Baltimore United States
6. International Clinical Research Center University of Washington Seattle United States
7. Department of Global Health University of Washington Seattle United States
8. Rakai Health Sciences Program Entebbe Uganda
9. School of Public Health Makerere University Kampala Uganda
10. U.S. Military HIV Research Program Walter Reed Army Institute of Research Silver Spring United States
11. Henry M. Jackson Foundation for the Advancement of Military Medicine Bethesda United States
12. Laboratory of Immunoregulation National Institute of Allergy and Infectious Diseases, National Institutes of Health Bethesda United States
13. Division of Intramural Research National Institute of Allergy and Infectious Diseases, National Institutes of Health Bethesda United States
14. Department of Zoology University of Oxford Oxford United Kingdom
15. Big Data Institute, Li Ka Shing Centre for Health Information and Discovery, Nuffield Department of Medicine University of Oxford Oxford United Kingdom

† Corresponding author

## Abstract

Evolutionary theory hypothesizes that intermediate virulence maximizes pathogen fitness as a result of a trade-off between virulence and transmission, but empirical evidence remains scarce. We bridge this gap using data from a large and long-standing HIV-1 prospective cohort, in Uganda. We use an epidemiological-evolutionary model parameterised with this data to derive evolutionary predictions based on analysis and detailed individual-based simulations. We robustly predict stabilising selection towards a low level of virulence, and rapid attenuation of the virus. Accordingly, set-point viral load, the most common measure of virulence, has declined in the last 20 years. Our model also predicts that subtype A is slowly outcompeting subtype D, with both subtypes becoming less virulent, as observed in the data. Reduction of set-point viral loads should have resulted in a 20% reduction in incidence, and a three years extension of untreated asymptomatic infection, increasing opportunities for timely treatment of infected individuals.

## Introduction

To spread, a pathogen must multiply within the host to ensure transmission, while simultaneously maintaining opportunities for transmission by avoiding host morbidity or death (Anderson and May, 1982; Alizon et al., 2009). This creates a trade-off between transmission and virulence. This hypothesis permeates theoretical work on the evolution of virulence, but empirical evidence remains scarce (Dwyer et al., 1990; Mackinnon and Read, 1999; Fraser et al., 2007; de Roode and Yates, 2008; Alizon et al., 2009; Cressler et al., 2015). In HIV-1 infection, set-point viral load (SPVL), the stable viral load in the asymptomatic phase of infection, is a viral trait which is both variable and heritable (Hollingsworth et al., 2010; Fraser et al., 2014; Hodcroft et al., 2014), and has an important impact on the transmission cycle of the pathogen. In untreated infection, higher SPVL translates into higher per-contact transmission rates but also faster disease progression to AIDS and death. From the perspective of the transmission cycle, this creates a trade-off, under which an intermediate SPVL value maximises opportunities for transmission (Fraser et al., 2007). Indeed the transmission potential of a parasite is the product of the transmission rate and the time during which the host is alive and can transmit. The latter is approximately the time to AIDS in HIV as host death occurs shortly after the onset of AIDS and sexual activity may be reduced in the AIDS phase because of AIDS-associated symptoms (Hollingsworth et al., 2008). The virulence-transmission trade-off in HIV is important for understanding pathogenesis and is a possible explanation for the significant changes in HIV virulence reported over the last decades in North America and Europe. There, SPVL increased at an estimated rate of 0.013 (Herbeck et al., 2012) and 0.020 log10 copies/mL/year (Pantazis et al., 2014) over the last 28 years. Since many persons at risk of infection do not routinely obtain HIV testing (Paz-Bailey et al., 2013), such changes may lead to more transmission and more newly diagnosed patients presenting with advanced infection, despite the widespread availability of antiretroviral therapy (ART).

The virulence-transmission trade-off is a promising hypothesis to explain changes in virulence of HIV, but this hypothesis and its predictions have so far been approached in a piecemeal manner, by combining data on infectiousness, AIDS-free survival and the dynamics of SPVL from very different cohorts (Fraser et al., 2007; Herbeck et al., 2012; Pantazis et al., 2014). Here we integrated extensive data from a single cohort in Uganda into an epidemiological-evolutionary model describing the transmission cycle of HIV. We then compared predictions on the evolution of SPVL evolution to the observed trends in SPVL in this cohort.

## Results

We focused on one of the longest established generalised HIV epidemics, in rural Uganda, and used data collected as part of the Rakai Community Cohort Study (RCCS), a large and long-standing population-based open cohort conducted by the Rakai Health Sciences Program (RHSP) in Rakai District. We combined data on transmission rates and survival to estimate the evolutionary optimal distribution of SPVL for the RCCS cohort, and then compared it to the dynamics of SPVL over time from 1995 to 2012. ART probably had little effect on the evolutionary dynamics of SPVL in Uganda because it only became available in 2004 and is initiated at relatively late stage infection (CD4 < 250 cells/mm3 from 2004 to January 2011, and at < 350 cells/mm3 from February, 2011 to the time of writing, August 2016).

As in other HIV epidemics, we found that SPVL is highly variable in this population, with values ranging from 102 copies/mL to 107 copies/mL. SPVL was calculated for 647 individuals who had a positive HIV serologic test within two study visits of their last negative test ('HIV incident cases', Table 1; median time between last negative visit and first positive visit is 1.25 years), and for 817 participants in a serodiscordant partnership ('serodiscordant couples', Table 2).

**Table 1.**
 Epidemiological and demographic characteristics of the HIV-1 incident cases in the Rakai cohort, used for the analysis of time trends in SPVL and for the analysis of time to AIDS. *Multiple subtypes (possibly dual infection) ** Recombinants, primarily A/D.


<table>
  <thead>
    <tr>
      <th>Gender</th>
      <th>N</th>
      <th>Mean SPVL, [0.025; 0.975] quantiles</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>F</td>
      <td>362</td>
      <td>4.3 [2.3; 5.85]</td>
    </tr>
    <tr>
      <td>M</td>
      <td>285</td>
      <td>4.54 [2.3; 6.03]</td>
    </tr>
    <tr>
      <td>Date of infection</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>1995–1999</td>
      <td>269</td>
      <td>4.47 [2.3; 6.01]</td>
    </tr>
    <tr>
      <td>2000–2004</td>
      <td>297</td>
      <td>4.46 [2.3; 5.83]</td>
    </tr>
    <tr>
      <td>2005–2009</td>
      <td>54</td>
      <td>3.98 [2.3; 5.77]</td>
    </tr>
    <tr>
      <td>≥2010</td>
      <td>27</td>
      <td>3.97 [2.2; 5.33]</td>
    </tr>
    <tr>
      <td>HIV-1 subtype</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>A</td>
      <td>96</td>
      <td>4.34 [2.78; 5.61]</td>
    </tr>
    <tr>
      <td>C</td>
      <td>6</td>
      <td>3.92 [3.42; 4.71]</td>
    </tr>
    <tr>
      <td>D</td>
      <td>292</td>
      <td>4.56 [2.62; 5.92]</td>
    </tr>
    <tr>
      <td>M*</td>
      <td>14</td>
      <td>3.99 [2.48; 5.35]</td>
    </tr>
    <tr>
      <td>R**</td>
      <td>74</td>
      <td>4.38 [2.33; 5.84]</td>
    </tr>
    <tr>
      <td>Unknown</td>
      <td>165</td>
      <td>4.22 [2.3; 6.03]</td>
    </tr>
    <tr>
      <td>Age at infection</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>15–19</td>
      <td>61</td>
      <td>4.17 [2.3; 5.51]</td>
    </tr>
    <tr>
      <td>20–29</td>
      <td>327</td>
      <td>4.43 [2.3; 5.97]</td>
    </tr>
    <tr>
      <td>30–39</td>
      <td>182</td>
      <td>4.45 [2.3; 5.88]</td>
    </tr>
    <tr>
      <td>40–49</td>
      <td>67</td>
      <td>4.43 [2.28; 6.09]</td>
    </tr>
    <tr>
      <td>≥50</td>
      <td>10</td>
      <td>4.05 [2.3; 5.94]</td>
    </tr>
  </tbody>
</table>

**Table 2.**
 Epidemiological and demographic characteristics of the infected individual in serodiscordant couples in the Rakai cohort, used for the analysis of time trends in SPVL and for the analysis of time to AIDS. ** Including recombinants, primarily A/D.


<table>
  <thead>
    <tr>
      <th>Gender</th>
      <th>N</th>
      <th>Mean SPVL, [0.025; 0.975] quantiles</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>F</td>
      <td>324</td>
      <td>3.99 [2.3; 5.61]</td>
    </tr>
    <tr>
      <td>M</td>
      <td>493</td>
      <td>4.23 [2.3; 5.85]</td>
    </tr>
    <tr>
      <td>Date of infection</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Unknown</td>
      <td>595</td>
      <td>4.1 [2.3; 5.64]</td>
    </tr>
    <tr>
      <td>1995–1999</td>
      <td>93</td>
      <td>4.13 [2.3; 5.53]</td>
    </tr>
    <tr>
      <td>2000–2004</td>
      <td>96</td>
      <td>4.41 [2.3; 5.98]</td>
    </tr>
    <tr>
      <td>2005–2009</td>
      <td>30</td>
      <td>4.08 [2.3; 5.62]</td>
    </tr>
    <tr>
      <td>≥2010</td>
      <td>3</td>
      <td>3.19 [2.36; 3.77]</td>
    </tr>
    <tr>
      <td>HIV-1 subtype</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>A</td>
      <td>54</td>
      <td>4.11 [2.42; 5.72]</td>
    </tr>
    <tr>
      <td>D</td>
      <td>430</td>
      <td>4.27 [2.4; 5.77]</td>
    </tr>
    <tr>
      <td>Other/Unknown**</td>
      <td>333</td>
      <td>3.97 [2.3; 5.67]</td>
    </tr>
  </tbody>
</table>

We analysed transmission in 817 serodiscordant couples, in which one partner was positive (index partner), while the other was initially negative and at risk of infection during follow-up. This analysis revealed that higher SPVL was associated with significantly increased rate of transmission. Transmission between partners was modelled as a Poisson process, in which the instantaneous transmission rate is constant (Fraser et al., 2007). We allowed the transmission rate to be a function of SPVL, β(v). We estimated all parameters by maximum likelihood and compared different models based on Akaike Information Criterion (AIC) (Materials and methods, Figure 1—figure supplement 1). The best model fit was one where transmission rates increases from 0.019/year to 0.14/year in a stepwise fashion as SPVL increases with three plateaus (Figure 1a) (ΔAIC = −75.96 compared to null model with a fixed transmission rate, n = 817). A function with three steps was favoured over others, but we also show a continuous function, the generalised Hill function, that may be considered more biologically realistic (ΔAIC = - 71.17 compared to the null model, n = 817) (Figure 1a). The two functions fitted the data well, as shown by comparison with non-parametric estimates of the transmission rate in the data stratified by SPVL (Figure 1a), and by a Kaplan-Meier plot comparing data to the model prediction (Figure 1b). We also allowed the parameters of the function β(v) to vary with the covariates subtype, gender, and male circumcision status. In accordance with previous studies (Kiwanuka et al., 2009), subtype A had a higher transmission rate than subtype D for all SPVL values (Figure 3) (ΔAIC = −3.32 compared to the model without subtype, n = 817). We will examine the evolutionary consequences of subtype differences later on. Gender did not have an effect on transmission (ΔAIC = 1.66 compared to model without gender, n = 817), and male circumcision reduced transmission both from female to male and from male to female (ΔAIC = −3.74 for female to male, n = 321; ΔAIC = −3.17 for male to female, n = 487, compared to model without circumcision) (Figure 1—figure supplement 3).

![Figure 1.](https://cdn.elifesciences.org/articles/20492/elife-20492-fig1-v3.jpg)

**Figure 1.:** On the left panels, black lines show the maximum likelihood relationships and shaded areas the bootstrap 95% confidence intervals. Both the step function (horizontal lines) and the generalised Hill function (curved line) are shown. The red lines show a non-parametric estimation of the transmission rate (a) and the time to AIDS (c) curves, when the data is stratified by SPVL in 8 bins of equal size. The right panels show Kaplan Meier plots when the data is partitioned in three SPVL groups defined by the maximum likelihood relationships. There was good agreement between the data (step functions) and the maximum likelihood function (smooth functions).

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/20492/elife-20492-fig1-figsupp1-v3.jpg)

**Figure 1—figure supplement 1.:** Functional forms include power (red), Hill (blue), generalised Hill (green), step function with three steps (black). The equivalent relationships as inferred in Fraser et al. (2007) are shown for comparison (black, dashed line).

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/20492/elife-20492-fig1-figsupp2-v3.jpg)

**Figure 1—figure supplement 2.:** In each panel, the maximum likelihood step function (black line) with bootstrap confidence intervals (grey) is shown together with the maximum likelihood function when undetectable SPVL values are removed (dashed line).

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/20492/elife-20492-fig1-figsupp3-v3.jpg)

**Figure 1—figure supplement 3.:** Lines are the maximum likelihood functions; shaded intervals are the bootstrap confidence intervals.

We assessed the relationship between SPVL and time to AIDS from 562 incident cases with a SPVL value and information on time to AIDS, and found that higher SPVL was associated with significantly shorter time to AIDS (Figure 1c). The time to AIDS was assumed to follow a gamma distribution, where the expected value was a function of SPVL (Fraser et al., 2007). We optimized the likelihood function and compared different models for the dependence of time to AIDS on SPVL based on AIC. The best model was a step function with three plateaus, with time to AIDS decreasing from 40 years to 5 years from low to high SPVL (Figure 1c; ΔAIC = 137.22 compared to null model with fixed time to AIDS). Again, non-parametric estimation of the time to AIDS (Figure 1c) and a Kaplan-Meier survival plot (Figure 1d) showed good fit of the model to the data. We also allowed the relationship between SPVL and time to AIDS to vary by subtype and gender. The inferred gamma distribution had shape parameter 1.2, similar to an exponential distribution (which is the special case where shape parameter is 1). We found, in agreement with previous studies ( Kiwanuka et al., 2008), that subtype D tended to confer faster disease progression, but this effect was not statistically significant here (Figure 1, ΔAIC = 15.41 compared to the model without subtype, n = 562). However, subtype D-infected individuals who progressed rapidly were not included in the analysis because they had no SPVL value (among the 33 individuals who progressed to AIDS within 10 years but had no SPVL value, there were 12 subtype D, 1 recombinant, and 20 unknown subtype). Time to AIDS did not significantly vary by gender (Figure 1, ΔAIC = 7.85 compared to the model without gender, n = 562).

Next, we predicted how SPVL might change over time under the trade-off between virulence and transmission, incorporating our setting-specific estimates of the virulence-transmission trade-off into an evolutionary and epidemiological model. The model is an analytically tractable Susceptible-Infected compartmental ordinary differential equation (ODE) model, where the viral population is stratified by SPVL, similar to previous models of virulence evolution (Day and Proulx, 2004; Day and Gandon, 2007) (Material and methods). SPVL of an infected individual is the sum of a viral genetic effect g, which is transmitted with mutation from a donor to a recipient, and an environmental effect e, which includes host and other environmental factors and is independently drawn in a normal distribution with mean 0 in each newly infected individual. The evolution of mean SPVL in the population is determined by the evolution of the mean viral genetic effect g. In this model the transmission rate of a virus with SPVL v is the inferred function $\beta(v)$ (Figure 1a), while death is assumed to occur at a constant rate $\mu(v)$ given by the inverse of the mean time to AIDS (Figure 1c). In the ODE model, the time to AIDS follows an exponential distribution because the rate of AIDS-death is constant. The individual based model presented later on relaxes this assumption and considers gamma-distributed time to AIDS as inferred from the data.

We first developed an analytical expression for the evolution of SPVL. Because prevalence of HIV in this cohort is approximately constant (at 14% on average in the period 1995 to 2013, Figure 2—figure supplement 1) and the distribution of SPVL can be closely approximated by a normal distribution, we were able to use an approximation of the Price equation (Price, 1970) inspired by a classical quantitative genetics model (Lande, 1976), to write the change in mean genetic effect of SPVL in prevalent cases over time as (Appendix):

$$
\frac{dg¯}{dt}=V_{P} h^{2}\frac{\mu¯^{2}}{\beta¯}\frac{∂(\beta¯/\mu¯)}{∂g¯}⏟transmission−virulencetrade−off+\alpha\mu¯⏟within−hostevolution
$$

The equation has two terms that respectively describe the effects of selection and of inheritance on SPVL evolution. The first term describes selection under a virulence-transmission trade-off, maximising the ratio of the mean transmission rate over the mean severity of infection, β¯/μ¯, which is the mean fitness of the viral population. The SPVL that maximises mean fitness is 3.4 log10 mL/copies (95% bootstrap CI [2.6; 4.0], Figure 2a). Adaptation of the viral population will proceed at a rate proportional to phenotypic variance VP (the variance in SPVL) and heritability h2 (the fraction of variance explained by viral genetic factors, assumed to be at equilibrium). The second term describes biased mutation that changes the mean SPVL from one infection to the next, where α is the mean effect of mutations from the donor to the recipient, recapitulating the effect of within-host selection on mean SPVL. The effects of the transmission-virulence trade-off were very similar when we used the generalised Hill functional form to fit the relationships between SPVL and transmission and time to AIDS (Figure 2a).

![Figure 2.](https://cdn.elifesciences.org/articles/20492/elife-20492-fig2-v3.jpg)

**Figure 2.:** (a), mean fitness of the viral population as a function of mean SPVL when transmission and time to AIDS are fitted as step functions (solid line; shaded area shows the 95% C.I.) or generalised Hill functions (dashed line). (b), evolutionary predictions for the temporal dynamics of mean SPVL given by the ODE model (thin solid and dashed lines), and the stochastic IBM (dotted lines), under three scenarios for the impact of within-host evolution (biased mutation) on SPVL in blue (1, α = −0.47 log10 copies/mL), red (2, α = −0.093 log10 copies/mL) and green (3, α = +0.057 log10 copies/mL). The thick line is the data, showing the linear regression of SPVL on date of seroconversion, with 95% bootstrap confidence intervals shown as a shaded area. (c), distribution of SPVL in the population over time; grey points show the data, and the line is the unadjusted regression of SPVL over time. (d) coefficient of regression of SPVL over time in the adjusted linear regression, with confidence intervals, in various subsets of the data (Material and methods). All data; SPVL strict definition; SPVL measured with Abbott assay and Roche 1.5 assay; SPVL measured at Walter Reed (WR), John Hopkins (JH) and RHSP laboratories; SPVL in males and females; subtype A, subtype D, and other/unknown subtype viruses.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/20492/elife-20492-fig2-figsupp1-v3.jpg)

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/20492/elife-20492-fig2-figsupp2-v3.jpg)

**Figure 2—figure supplement 2.:** This is shown for the full dataset ('All') and several subsets of data. Confidence intervals are determined assuming normality of the coefficients.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/20492/elife-20492-fig2-figsupp3-v3.jpg)

**Figure 2—figure supplement 3.:** Mean SPVL as a function of date of infection in the IBM including ART treatment, for heritability h2=0.36 and no biased mutation. ART treatment started in 2004. Individuals with a CD4 count below 350 cells/mm3 are eligible for treatment, and we varied coverage (the probability to receive treatment when eligible) from 0 to 50%. Treatment started 1 year after eligibility, and complete adherence was assumed. Upon treatment, the viral load is assumed to drop at 50 copies/mL.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/20492/elife-20492-fig2-figsupp4-v3.jpg)

**Figure 2—figure supplement 4.:** The figure shows the 10% to 90% percentiles of the SPVL distribution as a function of time.

![Figure 2—figure supplement 5.](https://cdn.elifesciences.org/articles/20492/elife-20492-fig2-figsupp5-v3.jpg)

**Figure 2—figure supplement 5.:** Mean SPVL as a function of date of seroconversion in the ODE model, for heritability h2=0.36 and biased mutation α = −0.093 log10 copies/mL (scenario 2). The model with approximately stable prevalence at 14% (red plain line, same as on Figure 2) is shown together with a simulation of the ODE model where initial prevalence is 20%, and the baseline transmission rate is set such that prevalence decreases to 5% over the 20 years of the simulation.

![Figure 2—figure supplement 6.](https://cdn.elifesciences.org/articles/20492/elife-20492-fig2-figsupp6-v3.jpg)

**Figure 2—figure supplement 6.:** Mean SPVL is shown as a function of date of seroconversion (for incident cases) and year (for prevalent cases). The data is shown in black, for incident cases (regression line, same as in Figure 2B) and prevalent cases (points are average SPVL each year with 95% CI, line is the regression line). Simulations of the ODE model and predictions from the Price equation show the mean genetic effect as coloured lines, for heritability h2=0.36 and three scenarios for biased mutation shown in the three panels.

Next we simulated the ODE and assessed the precision of the analytical approximation. We parameterised the ODE model with the data and simulated the evolution of mean SPVL from 1995 to 2015. Parameterisation was as follows: the transmission rate was as in Figure 1a; the mortality rate was the inverse of time to AIDS (Figure 1c); heritability of SPVL in the Rakai cohort was previously estimated at 36% (confidence interval 6–66%), using 97 donor-recipient transmission pairs (Hollingsworth et al., 2010) (who are participants of the present cohort). We had little data to parameterise the effect of within-host evolution on SPVL, $\alpha$. Many different types of mutations may evolve within the host, and little is known on the net effect of these processes on SPVL. Within-host viral fitness is positively related to replicative capacity (RC), measured in the absence of an immune response, and immune escape, which is host-specific. Most studies of within-host HIV evolution have focused on CTL escape mutations, which are conditionally beneficial (i.e. their positive effect on fitness is host-specific). These usually sweep through during infection because the fitness benefit of evading the immune system outweighs the cost of reduced RC that these mutations also impose (Goepfert et al., 2008; Carlson and Brumme, 2008; Matthews et al., 2008). CTL escape mutations may be reverted if the virus harbouring a costly CTL-escape mutation is transmitted to an individual where the mutation does not help evade the new host’s immune system (Carlson et al., 2014; Zanini et al., 2015). Mutations that increase the replicative capacity of the virus in all hosts may also evolve (Kouyos et al., 2011). It is also a possibility that slightly deleterious or beneficial mutations get fixed by genetic drift. We explored three scenarios where available data allow rough estimation of plausible values for the impact of within-host evolution on viral load (the $\alpha$ parameter) (Material and methods). (i) Most mutations evolving are conditionally beneficial but carry a strong cost to RC ($\alpha=−0.47$ log10 copies/mL). (ii) Most mutations evolving are conditionally beneficial but carry a moderate cost to RC ($\alpha=−0.093$ log10 copies/mL). (iii) Most mutations have unconditionally beneficial effects on RC ($\alpha=+0.057$ log10 copies/mL).

The ODE simulations predicted a decline in mean SPVL in incident cases from 1995 to 2015, at a rate of −0.042, −0.013 and −0.0009 log10 copies/mL/year in the three scenarios chosen for within-host evolution, for a heritability of 36%. The Price equation predicted the outcome of the ODE simulations quite precisely (Figure 2b). The Price equation shows that the virulence-transmission trade-off – the first term in the equation – contributes initially a decline in mean SPVL of $−0.01$ log10 copies/mL/year, slowing down as the population gets closer to the optimum. Note that the Price equation concerns average genetic effect of SPVL in the prevalent cases, but the rate of evolution in the incident cases was similar in these simulations (Figure 2—figure supplement 6). Predictions of the ODE model were robust to the addition of a number of more realistic features of the HIV epidemic, as shown by a more comprehensive individual-based stochastic model (IBM) of HIV evolution (Herbeck et al., 2014, 2016). The IBM includes all features of the ODE model, in particular the fact that SPVL is the addition of a heritable genetic component and a random environmental component. In addition, it includes the phases of acute infection and AIDS, both characterized by viral loads being much higher than the set-point value. Disease progression was modelled as progression through a series of CD4 count categories until AIDS occurred, and the transition rates between these categories were tuned to reproduce the inferred gamma-distributed time to AIDS. Partnership formation and dissolution was also explicitly modelled, as well as some degree of behavioural heterogeneity in partnership duration and coital frequency. The IBM also predicted a decline in mean SPVL in the three scenarios, although at a somewhat faster rate compared to the simplified ODE model, confirming the generality and robustness of our results (Figure 2b).

Strikingly, the data was in qualitative agreement with the evolutionary model: SPVL in the Rakai cohort decreased with date of seroconversion between 1995 and 2012, at a rate of −0.022 log10 copies/mL per year after adjustment for other covariates (CI [−0.04; −0.002], p=0.027, n = 603) (Figure 2). Average SPVL in prevalent cases was also declining at a rate of −0.020 log10 copies/mL, although for those it is more difficult to adjust for covariates and test for significance (because the same participants are 'prevalent cases' at multiple time points) (Figure 2—figure supplement 6). The observed trends were best explained if mutations evolving within the host had a moderate negative impact on mean SPVL (scenario 2).

The agreement between the observed trend in mean SPVL and the evolutionary model suggests that genetic changes in the virus may be responsible for decreasing SPVLs. However, it is possible that other confounding effects might explain some or all of the decrease in SPVL. Because the Rakai cohort has been studied extensively, we were able to consider the potential impact of a number of confounders but none of them could explain the observed decline in mean SPVL of around 0.4 log10 copies/mL over 17 years (Figure 2). SPVL decline was significant in the linear model both without adjustment (−0.029 log10 copies/mL per year, CI [−0.045; −0.013], p=0.0005, n = 603, Figure 2c), and in the multivariate regression mentioned above, controlling for the laboratory where SPVL was measured, assay type, gender, age and subtype. Additionally, to verify the robustness of the decline in mean SPVL, we examined the trend in SPVL in a number of subsets of the population (Figure 2d). SPVL declined in a similar way: (i) when using the 'strict' definition of SPVL (i.e. the subset of measures that included more than one viral load measurement and where the standard error across viral loads of the same participant was less than one log10 copies/mL) (Appendix); (ii) within each gender (Figure 2d); (iii) within each assay type, when partitioning the data in viral loads measured with the 'Abbott' assays and the 'Roche 1.5' assays, showing that declining SPVL was not due to changing assays; (iv) for viral loads measured at the John Hopkins and at the RHSP laboratories; and it is unlikely there were independent downward shifts in assay reading over time in these two laboratories. Mean SPVL did not decline in the subset of SPVL measured in the Walter Reed laboratory, but 90% of those were for participants infected prior to 2003, limiting power to detect temporal trends.

Improvement in nutrition or health care could be hypothesised to cause a decline in SPVL over time. However, improvement in nutrition would probably have no impact on the mean SPVL, as improving micronutrient intake slows down disease progression, but does not reduce plasma viral load (Fawzi et al., 2005; Friis, 2006; Baum et al., 2013). According to a survey conducted in 2006 in the Rakai communities, households experience on average 2 months per year of food insecurity, and the Household Dietary Diversity Score is 7.7 / 12 (S. Haberlen, personal communication, August 2016), which is high enough to meet WHO dietary requirements in energy, proteins, minerals and vitamins (Steyn et al., 2006). Improved healthcare is also a possible confounder. ART was introduced in Uganda in 2004, but until 2011 ART was prescribed only at late stage infection (CD4 count below 250 cells/mL). Although we excluded post-ART viral load measures from SPVL calculations, unreported ART use could have become more frequent at later time points and therefore might have contributed the decline in mean SPVL. To exclude this possibility, we first verified that the entire distribution of SPVL shifted downward, and the decline in mean SVPL was not only due to more low viral loads at later time points (Figure 2—figure supplement 4). We also examined the individual viral load trajectories within participants to verify that the clear drop in viraemia caused by ART was not present in more recent participants without reported ART (Supplementary file 1). Last we examined the determinants of SPVL using the same linear model, focussing on the subset of SPVL values with viral loads measured before 2004, prior to ART availability in the region. We found a similar though non-significant linear decline in SPVL after non-significant 'laboratory' factors were removed (effect size = −0.019 log10 copies/mL, CI [−0.052; 0.014], p=0.26, n = 442). In this subset of data, all SPVL but one were measured with the Roche 1.5 assay. We had little power to distinguish between 'laboratory' and 'calendar time' effects because of a strong correlation between these factors (∆AIC = −1.9 for a model with “laboratory” relative to a model with 'calendar time'). However we know from the analysis of the full dataset that 'laboratory' has no significant effect on SPVL, and furthermore the inferred effects of 'laboratory' in the pre-2004 subset are consistent with confounding by calendar time and different from those of the full dataset, which suggests the temporal effect is the genuine effect here.

Coinfections such as tuberculosis, malaria, the herpes simplex virus 2, gonorrhea, or syphilis, might increase viral load in HIV infected individuals (Modjarrad and Vermund, 2010). Better health care in the Rakai district could have caused a population-level reduction in SPVL via a reduction in prevalence of these coinfections. However, none of these coinfections had a combination of high prevalence at the beginning of the study, a large reduction in prevalence between 1995 and 2012, and a large effect on SPVL, sufficient to explain a decline of 0.4 log10 copies/mL (Material and methods).

To corroborate the evolutionary model, we extended it to include data on the subtype-specific transmission rate and model jointly the evolution of SPVL and subtype A, D, and AD recombinants (the major subtypes circulating in the population). The evolutionary model predicted the observed dynamics of subtype A, D, and AD recombinants ('R') in the cohort (Figure 3). In particular, HIV subtype A was more transmissible than subtype D for a given SPVL (Kiwanuka et al., 2009), and therefore was predicted to increase in frequency in the population. Temporal trends in subtype frequency in the data were inferred by focusing on subtypes A, D, and R and fitting a multinomial linear model for the frequency of the three subtypes as a function of seroconversion date. This revealed significant changes in subtype frequencies (analysis of deviance, p=0.044, n = 551) an increase in the frequency of subtype A (0.009 per year, bootstrap CI [−0.0007; 0.022]) and recombinants (0.007 per year, CI [−0.005; 0.017]), and a decrease in subtype D (−0.016, CI [−0.027; −0.002]), in accordance with a previous study (Conroy et al., 2010). The rise of subtype A and R together with the lower SPVL associated with infection with these subtypes contributes additionally to the decline in mean SPVL, but this effect is estimated at −0.003 log10 copies/mL/year, very small compared to the within-subtype evolution of SPVL at a rate of −0.022 log10 copies/mL/year (Material and methods). To model the dynamics of subtype A, D, and R within the ODE model, we assumed co-infection by A and D occurred only transiently and resulted in an 'R' infection with probability r (Day and Gandon 2012). We assumed the transmission function for subtype R was intermediate between that of subtype A and subtype D. In spite of large uncertainty in the fitness function of subtype A due to smaller numbers of infected individuals (Figure 3c), the model accurately predicted the rise in frequency of both subtypes A and R for r=1 (Figure 3d). SPVL declined within subtype A and D, the two major subtypes co-circulating in the region (Figure 2d). The inferred fitness functions for subtype A and D were both consistent with a decline in SPVL within each subtype (Figure 3e). We note, though, that the model predicted a slower decline in SPVL within subtype A than the one observed, because this subtype is expanding in the population, which favours selection for transmission and slows down the attenuation of the virus.

![Figure 3.](https://cdn.elifesciences.org/articles/20492/elife-20492-fig3-v3.jpg)

**Figure 3.:** Maximum likelihood functions for transmission (a) and time to AIDS (b) as a function of SPVL, stratified by subtype, for heritability h2=0.36 and biased mutation α = −0.093 (scenario 2). Shaded areas are bootstrap confidence intervals. (c) Predicted fitness function for subtype A (red) and subtype D (blue). (d) Subtype dynamics in the Rakai cohort as inferred by fitting a multinomial linear model with a 'date seroconversion' effect (solid lines, and confidence intervals as a shaded area; points show the actual frequency in the data, binned in five time categories, with confidence intervals), together with subtype dynamics predicted by the ODE model stratified by subtype (dashed lines). Recombination occurs upon co-infection and generates 'R' subtypes (purple). (e) Rates of evolution of SPVL per year within subtype, in the data (points, with 95% confidence intervals) and in the ODE simulation stratified by subtype (open circles).

## Discussion

Using extensive data on a population-based cohort in the Rakai district, Uganda, we confirmed the existence of a virulence-transmission trade-off in HIV, and predicted that the viral population should evolve reduced SPVL to maximise transmission opportunities. This prediction was verified, as mean SPVL in newly infected participants declined by 0.4 log10 copies/mL in the Rakai cohort form 1995 to 2012. We had limited information on the impact of within-host evolution on mean SPVL. However, the virulence-transmission trade-off was not negligible compared to the potential impact of within-host evolution, and results in a decline in mean SPVL of −0.01 log10 copies/mL/year, i.e. about 50% of the observed trend. We systematically examined potential confounders in this well-studied cohort, but none of them could account for the trend of declining SPVL, suggesting viral genetic changes may be responsible for the observed attenuation. The evolutionary model also quantitatively reproduced how higher transmission of subtype A resulted in expansion of this subtype in the population.

The attenuation of HIV in this Ugandan cohort is in contrast to increasing virulence in Europe. The European dynamics were hypothesized to result from viral adaptation to a higher optimal SPVL of 4.5 log10 copies/mL (Fraser et al., 2007; Herbeck et al., 2014). However this higher optimum was computed using a Zambian cohort for transmission estimates, and a Dutch cohort for time to AIDS (Figure 1—figure supplement 1). Transient selection for increased virulence could also have been important in Europe, and in fact SPVL has declined since 2004 (Pantazis et al., 2014). Our finding of HIV attenuation is consistent with another study of the evolution of HIV virulence in Africa.Comparison between the epidemic in Botswana and the younger epidemic in South Africa revealed declines in SPVL, which was hypothesized to be due to the fixation of mutations conferring adaptation to HLA variants and decreased replicative capacity (Payne et al., 2014).

Although the agreement between the observed trend in mean SPVL and the evolutionary model are consistent with genetic changes in the virus causing decreasing SPVLs, genomic data is lacking to positively demonstrate viral genetic changes. Even if genomic data were available, this would be a challenging task since SPVL is probably determined by many loci of small effect (Bartha et al., 2013), and polygenic adaption is difficult to detect (Pritchard et al., 2010). However, adaptation of the viral population to the low optimum is a logical consequence of the impact of SPVL on transmission and time to AIDS, two robust relationships inferred from the data (Figure 1). These effects of SPVL on the viral transmission cycle, together with 30–40% viral heritability of SPVL (36% specifically in the Rakai cohort, but generally around 30–40% in different settings, [Fraser et al., 2014; Mitov and Stadler, 2016; Leventhal and Bonhoeffer, 2016]), is predicted to result in attenuation of the virus.

The detailed evolutionary model of HIV SPVL evolution presented here quantitatively reproduced the attenuation of HIV-1 virulence that happened in the last 20 years. This decline in virulence is predicted to continue into the future. This decline is unaffected by ART becoming more widely available, as even aggressive test-and-treat strategies have little predicted effect on these evolutionary dynamics (Roberts et al., 2015; Herbeck et al., 2016) (Figure 2—figure supplement 3). As ART becomes more widely available, essentially shortening the duration of infection, reduced SPVL will contribute to reductions in onwards transmission, and so synergise with efforts to eliminate the pathogen.

## Materials and methods

The RCCS has conducted regular surveys (approximately annual) of all consenting residents aged 15–49 in the same 50 communities since 1994, collecting detailed information on demographics, sexual behaviours and health status and obtaining blood for HIV testing from all consenting participants. Personal information on marital and long-term consensual partners is also collected, which enables retrospective identification of stable couples. All individuals found to be HIV-infected are referred for care, including CD4 T cells count and viral load measurements. Virtually all HIV transmission in this population is via heterosexual vaginal intercourse, and the rates of reported intercourse per week and month were found to be stable by HIV subtype and different study time periods.

### SPVL

SPVL was calculated for 817 participants in a serodiscordant partnership ('Serodiscordant couples', Table 2), and for 647 individuals who had a positive HIV serology test within two study visits of their last negative test ('HIV incident cases', Table 1; median time between last negative visit and first positive visit is 1.25 years). SPVL was defined as the mean log10 viral load for all visits occurring more than 6 months after estimated date of infection and before initiation of ART. Clinical records indicating ART initiation were available for participants who received care at an RHSP clinic prior to 2013. After 2013, ART care at most RHSP clinics was transferred to the Ugandan Ministry of Health. We determined receipt of treatment from clinics other than RHSP prior to 2013, or at any clinic post-2013, by self-reported ART treatment status (SI).

### Transmission

Transmission was modelled as a Poisson process, in which the instantaneous transmission rate is constant (Fraser et al., 2007). We allowed the transmission rate to be a function of SPVL and other epidemiological covariates. For a seropositive individual (the 'index') with SPVL v, the probability that infection of the seronegative partner occurs between time $t_{p,−}$ and $t_{p,+}$ (where the subscript p stands for partner) is given by:

$$
P[t_{p,−}<t_{p}^{*}<t_{p,+}]=e^{−\beta(v)(t_{p,−}−t_{init})}−e^{−\beta(v)(t_{p,+}−t_{init})}
$$

where $t_{init}$ is the time at which the index becomes infected (defined as the mid-point between last negative and first positive dates) or where observation of the couple starts, whichever occurs last and $\beta(v)$ is the transmission hazard. In a Poisson process, the time to transmission is exponentially distributed: thus the probability is obtained by integration of the probability density function of the exponential distribution between time $t_{p,−}$ and $t_{p,+}$. When infection occurred within the window of observation, $t_{p,−}$ and $t_{p,+}$ are simply the last time the partner was seen negative and the first time he/she was seen positive. When infection did not occur within the window of observation, $t_{p,−}$ is the last time the partner was seen and $t_{p,+}$ is infinity. The likelihood function is the product of these probabilities over all couples. We compared several functional forms for $\beta(v)$, including a flat function where viral load has no impact on transmission, a power function $\beta(v)=\beta_{0}10^{k v}$, the Hill function $\beta(v)=\beta_{max}\frac{1}{1+10^{−k (v−v_{50})} }$, a generalised Hill function $\beta(v)=\beta_{min}+\frac{\beta_{max}−\beta_{min}}{(1+10^{−k (v−v_{50})})^{\frac{1}{\gamma}} }$, a step function with three plateaus and one with four plateaus. We computed the likelihood of each model, searched for the maximum likelihood parameters using the Nelder-Mead method and compared different models based on Akaike Information Criterion (AIC). We tested how transmission varied with other epidemiological factors, including subtype, gender, and circumcision status, by allowing the parameters of the function $\beta(v)$ to vary with different values of these factors (Figure 1—source data 1).

### Time to AIDS

The time at which an individual was first diagnosed with AIDS was defined in one of three ways. For the majority of participants, it was defined as the time at which CD4 count is first below 200 cells per mm3, (n = 203 of the 288 participants who declared AIDS) or the time at which three symptoms of AIDS (Sewankambo et al., 2000) were first observed (n = 43), whichever came first. If AIDS was not defined according to these criteria, but the individual was known to have died of AIDS, the time to AIDS was taken to be the time to death (n = 42).

Time to AIDS was assumed to follow a gamma distribution whose expected value was a decreasing function of the viral load. For this decreasing function we used a flat function (as a null model), a decreasing Hill function $t^_{AIDS}(v)=t_{max}\frac{1}{1+10^{−a (v_{50}−v)} }$, a generalised Hill function $t^_{AIDS}(v)=t_{min}+\frac{t_{max}−t_{min}}{(1+10^{−a (v_{50}−v)})^{\frac{1}{b}} }$ and a step function with three plateaus. For the Hill function and the generalised Hill function, we set the maximum time a virus can be carried by its host to $t_{max}=40$ years. We also allowed these functions to vary by subtype and gender. For a participant, the probability that AIDS occurred between time $t_{no AIDS}$ and time $t_{AIDS}$ is:

$$
P[t_{no AIDS}<t<t_{AIDS}]=\frac{G(k, t_{AIDS}/\theta)}{Γ(k)}−\frac{G(k, t_{no AIDS}/\theta)}{Γ(k)}
$$

where $G(k, t_{AIDS}/\theta)/Γ(k)$ is the regularized gamma function which is the cumulative distribution function of the gamma distribution; $k$ is the shape parameter and $\theta$ is the scale parameter set to $t^_{AIDS}/k$ so that the expected value is $t^_{AIDS}$. When AIDS was not declared in the individual, $t_{no AIDS}$ was set to the date of last visit of this individual, and $ t_{AIDS}$ was set to infinity. The likelihood function was obtained by multiplying these probabilities across all participants. We computed the likelihood of each model, searched for the maximum likelihood parameters and compared different models based on Akaike Information Criterion (AIC).

### Epidemiological and evolutionary modelling

We developed a Susceptible-Infected compartmental ordinary differential equation (ODE) model, where the viral population is stratified by SPVL. The set-point viral load v of an individual is given by v=g+e where g is the genetic effect, transmitted with mutation from a donor to a recipient, and e is the environmental effect, which includes host and other environmental factors, and is independently drawn in each newly infected individual. The model is akin to classical quantitative genetics models and in particular to a previously described model of virulence evolution (Lande, 1976; Day and Proulx, 2004). The model neglects the impact on transmission of the higher viral loads in early and late phases of infection, however we relax this assumption in the individual-based model presented below. The number of infected with genetic and environmental effects (g, e) evolves as:

$$
\frac{dY(g,e,t)}{dt}=\int\gamma=−∞∞\intϵ=−∞∞\beta(\gamma+ϵ)X(t)Y(\gamma,ϵ,t)P(e)Q(\gamma→g)dϵ d\gamma⏟transmission −\mu(g+e)Y(g,e,t)⏟death
$$

and the number of uninfected individuals $X$changes as:

$$
\frac{dX}{dt}=bX−\beta¯X Y_{tot}
$$

The first term in the equation for the number of infected reflects the increase in the number of infected individuals with viral genetic effect g and environmental effect e due to new transmission events from all possible donors. The second term describes death of infected individuals. In these equations, $\beta(.)$ is the transmission rate as a function of SPVL, $P(e)$ is the distribution of environmental effects in newly infected individuals, $Q(\gamma→g)$ is the mutation kernel, which is the probability that a donor with virus of genetic effect $\gamma$ gives an infection with a virus of genetic effect $g$, $\mu(.)$ is the AIDS death rate as a function of SPVL (inversely related to the time to AIDS), b is the birth rate, $\beta¯$ is the mean transmission rate in the population, and $Y_{tot}$ is the total number of infected.

The evolution of mean SPVL in the population is determined by the evolution of the mean viral genetic effect g, as the mean environmental effect is set at 0 without loss of generality. Under this model, we find that evolution of mean genetic effect (denoted $g¯$) is determined by the Price equation (Price, 1970):

$$
\frac{dg¯}{dt}=cov[\betaX−\mu,g]+\alpha \beta¯ X
$$

(see SI for derivation). The parameter $\alpha$ is the mean effect of mutations on SPVL in log10 copies/mL. The first term of the equation is the Robertson-Price identity (Robertson, 1966; Price, 1970), which equates the change in character with the population covariance between a fitness measure, here $\betaX−\mu$, and the genetic value of this character. The dependence on the number of uninfected individuals sets the balance between selection for higher transmission rate and selection for lower mortality. For example, when the number of susceptible individuals is large relative to its long-term equilibrium value $\mu¯/\beta¯$, selection for higher transmission and higher mortality is favored, an effect that can be important in an emerging epidemic (Bolker et al., 2010; Shirreff et al., 2011; Berngruber et al., 2013). The second term describes the effect of biased mutation, proportional to incidence $\beta¯ X$.

We emphasize that knowledge of the molecular mechanism driving the decline in virulence is not needed to make evolutionary predictions. To derive further analytical insights, we assume that the number of susceptible individuals is approximately at its equilibrium value $\mu¯/\beta¯$. We take advantage of the approximately normal distribution of SPVL in the population to derive an expression for the change in mean SPVL in prevalent cases over time, akin to Lande’s classical quantitative genetic equation (Lande, 1976).

$$
\frac{dg¯}{dt}=V_{P} h^{2}\frac{\mu¯^{2}}{\beta¯}\frac{∂(\beta¯/\mu¯)}{∂g¯}+\alpha \mu¯
$$

where $V_{P}$ is the variance in SPVL and $ h^{2}$ is heritability of SPVL, the fraction of the variance explained by viral genetic factors. The mean SPVL in the population will evolve to the value maximizing mean fitness $\beta¯/\mu¯$, which is 3.4 log10 mL/copies (95% CI [2.6; 4.0], Figure 2a), at a pace proportional to heritability (which is assumed to be at equilibrium).

We parameterised the ODE model with our data, and solved it using the Euler method. Specifically, the initial SPVL in incident cases was 4.72 log10 copies/mL. The transmission rate and mortality due to AIDS as a function of SPVL were the inferred functions (Figure 1). We tuned the baseline transmission rate and the birth rate to achieve the stable prevalence of 14% observed in the Rakai communities and a total population size of 20 millions adults. Declining prevalence would not change much the evolution of mean SPVL (Figure 2—figure supplement 5).

We assumed that the mutation kernel $Q(\gamma→g)$ was the density of a normal distribution with a non-zero mean $\alpha$, and standard deviation $\sigma_{mut}=0.15$, evaluated at $g−\gamma$. The density of environmental effects $P(e)$ was given by the density of a normal distribution with mean 0 and standard deviation 0.76. The variance parameters were chosen to achieve an approximately stable phenotypic variance of SPVL $V_{P}=0.91$ and heritability at 36% as inferred in this cohort (Hollingsworth et al., 2010), and similar to the value of 30 to 40% established in a number of studies (Fraser et al., 2014; Mitov and Stadler, 2016).

Because only a small number of studies have linked within-host evolution to SPVL evolution, we explored three scenarios spanning a range of possibilities to parameterise $\alpha$. (i) The dominant process is the increase in the frequency of CTL escape mutations, or other host-specific beneficial mutations imposing a RC cost, resulting in a reduced viral fitness and SPVL in the next typical infected person. We first parameterize α in this scenario using data on the inferred decline in mean SPVL in Botswana (Payne et al., 2014). The mean SPVL in a cohort in South Africa was 4.47, compared to 4.19 log10 copies/mL in a cohort in Botswana where the epidemic started about 6 years earlier, giving an inferred decline of (4.19 – 4.47) / 6 = −0.047 log10 copies/mL/year, hypothesized to result from the rise of CTL escape mutations in the viral population. From the Price equation, the decline in mean SPVL is given by $\alpha \mu¯$, assuming constant prevalence and neglecting the virulence-transmission trade-off. Solving for $\alpha$ in $\alpha \mu¯=−0.047$, with a mean death rate of $\mu¯$ = 0.1 per year as in the present cohort, gives a rough estimate of $\alpha=−0.47$ log10 copies/mL under this scenario. (ii) Second, under a similar assumption that the dominant process is the increase in host-specific beneficial mutations imposing a RC cost, we now parameterize α assuming that these mutations impose a RC cost similar to that of random mutations. Indeed some immune escape mutations, for example CTL escape mutations arising in the pol, env or nef gene, appear neutral (Matthews et al., 2008; Troyer et al., 2009). In this scenario, the coefficient of variation of the distribution of SPVL effects within the host would be the same as that of the distribution of fitness effects of random mutations. This coefficient of variation was estimated at −1.609 in a previous study (Bonhoeffer et al., 2004), giving $\alpha=−\sigma_{mut}/1.609=−0.093$ log10 copies/mL. (iii) The dominant process is the increase in frequency of mutations causing a within-host increase in RC, resulting in higher viral fitness in the next host. To our knowledge increase in RC over the course of infection has been evidenced only in one study (Kouyos et al., 2011). This study predicted an increase in RC over the course of infection of + 0.02 per year. The relationship between RC and SPVL inferred in that study (SPVL = 4.297 + 0.572 * RC, Figure 1A in [Kouyos et al., 2011]), together with the fact that the mean time to transmission is 5 years (as inferred from simulation of our IBM), leads to $\alpha=0.02  \times 5 \times 0.572=+ 0.057$ log10 copies/mL in this scenario.

Predictions of the ODE model were robust to the addition of a number of more realistic features of the HIV epidemic, as shown by an individual-based stochastic model of HIV evolution (IBM) with a higher level of complexity, described in details previously (Herbeck et al., 2014; Herbeck et al., 2016). The IBM relaxed several assumptions of the ODE. In contrast to the ODE that described only the asymptomatic phase of infection characterized by a stable SPVL value, the IBM explicitly modelled the dynamics of viral load within individuals. This included the acute phase of infection and the AIDS phase, which are both characterized by a higher viral load. The viral load in the acute and AIDS phases, and the duration of acute phase did not vary across individuals. In the ODE, transmission was modelled using the law of mass action; in the IBM a changing network of sexual contacts was modelled (although sexes were not explicitly modelled). The number of partnerships in which each individual was engaged was variable, and there was heterogeneity in partnership duration (between 3 and 60 months). Furthermore, the behavioural dynamics were designed to reflect a core group of transmitters; individuals in the core group (10% of the overall population) had shorter partnership durations and increased coital frequency. The rate of overall partnership formation and the distribution of coital frequencies were both calibrated to result in an equilibrium prevalence of 14%, corresponding to the average prevalence in the 1995–2015 period, as for the main model.

### Temporal trends in SPVL

We inferred temporal trends in SPVL in incident cases using a multivariate linear model where we explained variation in SPVL as a function of the laboratory in which SPVL was measured, the assay used, whether VL was measured at a RCCS visit (individuals with unclear infection status), gender, circumcision status, age, date at seroconversion, and subtype (Figure 2). Significance was assessed using type II analysis of variance, and confidence intervals were computed assuming asymptotic normality of the coefficients. Viral loads were measured in three different laboratories and using two types of PCR assays. This heterogeneity of laboratory approaches could potentially confound other trends; however our multivariate regression controlled for these effects, and revealed that they had small and non-significant effect sizes (Figure 2—source data 1), such that they did not generate any systematic variability in SPVL. SPVL decreased at a pace of −0.033 log10 unit per year (CI [−0.057; −0.009], p=0.007, n = 603), resulting in a 0.66 log10 unit change over the 1995–2015 period. The estimated rate was −0.022 (CI [−0.041; −0.002], p=0.027, n = 603) after non-significant predictors were removed. The linear temporal trend in mean SPVL was more supported than a model where time was fitted as five discrete categories (∆AIC = 7.2). An important potential confounder of the reported trends in SPVL would have been the use of unreported antiretroviral therapy (ART) becoming more frequent at later time points. To exclude this possibility, we focused on the subset of SPVL values with viral loads measured before 2004, prior to ART availability in the region. Consistent with previous studies (Farzadegan et al., 1998; Gandhi et al., 2002), males had a higher SPVL than females (+0.259 log10 viral copies/mL, CI [0.14; 0.38], p=4.2 10–5, n = 603) subtype D conferred higher SPVL than other subtypes (+0.211 relative to subtype A, CI [0.038; 0.38], p=0.017, n = 603), and older age conferred slightly higher SPVL (+ 0.009 per year, CI [0.0008; 0.016], p=0.030, n = 603). The decreasing trend in SPVL as well as the effects of gender, and subtype D, were all robust, as they had similar magnitude in several subsets of data (Figure 2—figure supplement 2).

We also inferred temporal trends in mean SPVL in prevalent cases by calculating each year the mean SPVL for cases who are infected, alive, and not lost to follow-up. In this analysis we found a decline in mean SPVL at a rate of −0.020 log10 copies/mL/year (Figure 2—figure supplement 6). This decline was highly significant (p=5.06e−08, N = 18) but the p-value calculation did not account for non-independence across years (the same prevalent cases may be included in multiple years).

### Review of coinfections as potential confounders of the SPVL trend

Coinfections such as tuberculosis, malaria, the herpes simplex virus 2, gonorrhea, or syphilis, might increase viral load in HIV infected individuals (Modjarrad and Vermund, 2010). A reduction in prevalence $\deltap$ of a disease with an effect $\deltav$ on SPVL would cause a $\deltap \deltav$ decrease in mean SPVL in the population. We systematically reviewed these diseases and show that potential reduction in prevalence of these diseases is unlikely to cause the observed 0.4 log10 copies/mL decline in mean SPVL.

Tuberculosis results in a $\deltav=0.5$ log10 copies/mL increase in viral load (Modjarrad and Vermund, 2010), prevalence has decreased two-fold since 1995, and was 2.7% in 2014 among HIV infected persons screened for TB (WHO, 2015). This would result in a change in SPVL $\deltap \deltav=−0.027∗0.5=−0.013$ log10 copies/mL. Malaria incidence is high in Uganda (50.8 episodes per 100 person years in Uganda in 2001, [Mermin et al., 2006]), but malaria infection only causes a transient increase in SPVL of $\deltav=0.25$ log10 copies/mL during ~ 40 days (Kublin et al., 2005). The overall effect of a hypothetical two-fold reduction in malaria incidence from 1995 to 2012 (from 60 to 30 per 100 person years) would be $\deltap \deltav=−0.3∗40/465∗0.25= −0.006$ log10 viral copies per mL. Herpes simplex virus 2 (HSV-2) prevalence was roughly stable, from 70% in 1994–1998 (Serwadda et al., 2003) to 88% in 2007–2008 (Reynolds et al., 2012) in HIV infected individuals in the Rakai district, and the prevalence of genital ulcer disease in the general populations, mostly caused by HSV-2 (Brankin et al., 2009) was stable over this period (data not shown). The prevalence of gonorrhea and syphilis was 8.6% and 3.3% respectively in 1994–1998 (Ahmed et al., 2001); therefore, given these diseases confer $\deltav=0.04$ and $\deltav=0.1$ log10 copies/mL increase in HIV viral load (Modjarrad and Vermund, 2010), an hypothetical two-fold reduction of prevalence from 1995 to 2012 would have caused a $−0.043∗0.04= −0.0018$ log10 viral copies per mL and $− 0.017*0.1= −0.0017$ log10 viral copies per mL. Last, coinfection by helminths is rare in most of the Rakai communities (Wawer et al., 1999), although schistosomiasis is endemic in some fishing communities living near lake Victoria, with prevalence of up to 50% in 1998–2002 (Kabatereine et al., 2004). However, there is no evidence for an effect of helminth infection on HIV viral load (Brown et al., 2004; Modjarrad et al., 2005; Modjarrad and Vermund, 2010).

### Subtype-specific predictions

We extended the ODE model to account for subtype-specific dynamics, in particular the dynamics of subtype A, subtype D, and AD recombinants (called 'R'). The functions describing transmission as a function of SPVL were the inferred subtype-specific step functions (Figure 3a). The function describing time to AIDS as a function of SPVL was the step function inferred on the whole cohort, as there was little difference between subtypes (Figure 1c). Starting conditions were parameterised based on the data, as follows. Mean SPVL in incident cases in 1995 were $v¯_{A,0}=4.58$, $v¯_{D,0}=4.79$, $v¯_{R,0}=4.66$ log10 copies per mL of blood. The frequencies of the three types in 1995 were pA=0.17, pD=0.7, pR=0.13. The mutation kernel $Q(\gamma→g)$ was, for all three types, the density of a normal distribution with a non-zero mean $\alpha=−0.093$ (scenario 2), and standard deviation $\sigma_{mut}=0.15$, evaluated at $g−\gamma$. The density of environmental effects $P(e)$ was the density of a normal distribution with mean 0 and standard deviation 0.67. These parameters were chosen to achieve an approximately stable phenotypic variance of SPVL $V_{P}=0.7$ (the phenotypic variance in SPVL within subtype) and heritability at 36%.

We assumed super-infection occurred on a fast timescale and immediately resulted in one strain replacing the other. Super-infection with A and D, A and R, or D and R strains resulted in a recombinant subtype ('R') with probability r. We chose r=1 as it best reproduced the rise in frequency of recombinants (Figure 3d).

### Contributions of within-subtype and between-subtype evolution to SPVL trends

We decomposed the trend in mean SPVL into the sum of two components, one due to changes in subtype frequency, one due to within-subtype changes in SPVL. The change in mean SPVL between time 0 and t reads:

$$
Δv¯=\sumi \in{A, D, R}p_{i,t}v¯_{i,t}−\sumi \in{A, D, R}p_{i,0}v¯_{i,0}
$$

With linear trends in subtype frequencies, $p_{i,t}=p_{i,0}+\deltap_{i} t$, and in mean SPVL within subtypes, $v¯_{i,t}=v¯_{i,0}+\deltav¯_{i} t$. Replacing yields:

$$
Δv¯=\sumi \in{A, D, R}(p_{i,0}+\deltap_{i} t)(v¯_{i,0}+\deltav¯_{i} t)−\sumi \in{A, D, R}p_{i,0}v¯_{i,0}
$$

Because the changes are slow (i.e. $\deltap_{i}$ and $\deltav¯_{i}$ are small), we can neglect the term in $\deltap_{i}\deltav¯_{i}$ and approximate the change as:

$$
Δv¯=[\sumi \in{A, D, R}p_{i,0}\deltav¯_{i}+\sumi \in{A, D, R}\deltap_{i} v¯_{i,0}]t
$$

The first term reflects the changes in mean SPVL due to changes in mean SPVL within subtype. The second term reflects the changes in mean SPVL due to changing subtype frequencies. We have $v¯_{A,0}=4.58$, $v¯_{D,0}=4.79$, $v¯_{R,0}=4.66$ log10 copies/mL, and $\deltap_{A}=0.009$, $\deltap_{D}=−0.016$, $\deltap_{R}=0.007$, inferred from a generalized linear model with multinomial response describing subtype frequency as a function of calendar time. Thus the change in mean SPVL due to the rise in subtype A and R is −0.003 log10 copies/mL per year. Assuming the same rate of SPVL evolution in all subtypes, $\deltav¯_{A}=\deltav¯_{D}=\deltav¯_{R}=−0.022$ log10 copies/mL per year (a rate inferred from the linear model, adjusted for subtype and other covariates), the change in mean SPVL due to within-host evolution is also −0.022 log10 copies/mL per year. Thus the total mean SPVL change is $=−0.025$ log10 copies/mL per year and most of this change is due to within-subtype evolution.
