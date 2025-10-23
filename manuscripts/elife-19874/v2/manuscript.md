# Structure in the variability of the basic reproductive number (R0) for Zika epidemics in the Pacific islands

## Authors

- Clara Champagne<sup>1</sup> ([ORCID: 0000-0002-0369-6758](https://orcid.org/0000-0002-0369-6758)) †
- David Georges Salthouse<sup>1</sup>
- Richard Paul<sup>3</sup>
- Van-Mai Cao-Lormeau<sup>5</sup>
- Benjamin Roche<sup>6</sup>
- Bernard Cazelles<sup>1</sup> ([ORCID: 0000-0002-7972-361X](https://orcid.org/0000-0002-7972-361X)) †

### Affiliations

1. IBENS, UMR 8197 CNRS-ENS Ecole Normale Supérieure Paris France
2. CREST, ENSAE, Université Paris Saclay France
3. Department of Genomes and Genetics Institut Pasteur, Unité de Génétique Fonctionnelle des Maladies Infectieuses Paris France
4. Centre National de la Recherche Scientifique URA 3012 Paris France
5. Unit of Emerging Infectious Diseases Institut Louis Malardé Tahiti France
6. International Center for Mathematical and Computational Modeling of Complex Systems (UMMISCO) UPMC/IRD Bondy cedex France

† Corresponding author

## Abstract

10.7554/eLife.19874.001 Before the outbreak that reached the Americas in 2015, Zika virus (ZIKV) circulated in Asia and the Pacific: these past epidemics can be highly informative on the key parameters driving virus transmission, such as the basic reproduction number ( ). We compare two compartmental models with different mosquito representations, using surveillance and seroprevalence data for several ZIKV outbreaks in Pacific islands (Yap, Micronesia 2007, Tahiti and Moorea, French Polynesia 2013-2014, New Caledonia 2014). Models are estimated in a stochastic framework with recent Bayesian techniques. R 0 for the Pacific ZIKV epidemics is estimated between 1.5 and 4.1, the smallest islands displaying higher and more variable values. This relatively low range of R 0 suggests that intervention strategies developed for other flaviviruses should enable as, if not more effective control of ZIKV. Our study also highlights the importance of seroprevalence data for precise quantitative analysis of pathogen propagation, to design prevention and control strategies. R 0 DOI: http://dx.doi.org/10.7554/eLife.19874.001

## Introduction

In May 2015, the first local cases of Zika were recorded in Brazil and by December of the same year the number of cases had surpassed 1.5 million. On February 2016, the World Health Organization declared Zika as a public health emergency of international concern (Who, 2016) and in March 2016, local transmission of Zika was recognized in 34 countries. Previously the Zika virus had circulated in Africa and Asia but only sporadic human cases had been reported. In 2007 the outbreak on Yap (Micronesia) was the first Zika outbreak outside Africa and Asia (Duffy et al., 2009). Since, Zika outbreaks have been also reported in French Polynesia and in New Caledonia (Cao-Lormeau et al., 2014; Dupont-Rouzeyrol et al., 2015) between 2013 and 2014 and subsequently, there have been cases of Zika disease in the Cook Islands, the Solomon Islands, Samoa, Vanuatu, and Easter Island (Chile) (see Figure 1 in Petersen et al. [2016]).

Zika virus (ZIKV) is a flavivirus, mostly transmitted via the bites of infected Aedes mosquitoes, although non-vector-borne transmission has been documented (sexual and maternofoetal transmission, laboratory contamination, transmission through transfusion) (Musso and Gubler, 2016). The most common clinical manifestations include rash, fever, arthralgia, and conjunctivitis (Musso and Gubler, 2016) but a large proportion of infections are asymptomatic or trigger mild symptoms that can remain unnoticed. Nevertheless, the virus may be involved in many severe neurological complications, including Guillain-Barre syndrome (Cao-Lormeau et al., 2016) and microcephaly in newborns (Schuler-Faccini et al., 2015). These complications and the impressive speed of its geographically propagation make the Zika pandemic a public health threat (Who, 2016). This reinforces the urgent need to characterize the different facets of virus transmission and to evaluate its dispersal capacity. We address this here by estimating the key parameters of ZIKV transmission, including the basic reproduction number (R0), based on previous epidemics in the Pacific islands.

Defined as the average number of secondary cases caused by one typical infected individual in an entirely susceptible population, the basic reproduction number (R0) is a central parameter in epidemiology used to quantify the magnitude of ongoing outbreaks and it provides insight when designing control interventions (Diekmann et al., 2010). It is nevertheless complex to estimate (Diekmann et al., 2010; van den Driessche and Watmough, 2002), and therefore, care must be taken when extrapolating the results obtained in a specific setting, using a specific mathematical model. In the present study, we explore the variability of R0 using two models in several settings that had Zika epidemics in different years and that vary in population size (Yap, Micronesia 2007, Tahiti and Moorea, French Polynesia 2013–2014, and New Caledonia 2014). These three countries were successively affected by the virus, resulting in the first significant human outbreaks and they differ in several ways, including population size and location specific features. Hence, the comparison of their parameter estimates can be highly informative on the intrinsic variability of R0. For each setting, we compare two compartmental models using different parameters defining the mosquito populations. Both models are considered in a stochastic framework, a necessary layer of complexity given the small population size and recent Bayesian inference techniques (Andrieu et al., 2010) are used for parameter estimation.

## Results

We use mathematical transmission models and data from surveillance systems and seroprevalence surveys for several ZIKV outbreaks in Pacific islands (Yap, Micronesia 2007 (Duffy et al., 2009), Tahiti and Moorea, French Polynesia 2013–2014 (CHSP, 2014; Mallet et al., 2015; Aubry et al., 2015b), New Caledonia 2014 [DASS, 2014]) to quantify the ZIKV transmission variability.

Two compartmental models with vector-borne transmission are compared (cf.

![Figure 1.](https://cdn.elifesciences.org/articles/19874/elife-19874-fig1-v2.jpg)

**Figure 1.:** Squared boxes and circles correspond respectively to human and vector compartments. Plain arrows represent transitions from one state to the next. Dashed arrows indicate interactions between humans and vectors. (a) Pandey model (Pandey et al., 2013).  susceptible individuals; HS infected (not yet infectious) individuals; HE infectious individuals; HI recovered individuals; HR is the rate at which σ-individuals move to infectious class HE; infectious individuals (HI) then recover at rate HI; γ susceptible vectors; VS infected (not yet infectious) vectors; VE infectious vectors; VI constant size of total mosquito population; V is the rate at which τ-vectors move to infectious class VE; vectors die at rate VI. (μb) Laneri model (Laneri et al., 2010).  susceptible individuals; HS infected (not yet infectious) individuals; HE infectious individuals; HI recovered individuals; HR is the rate at which σ-individuals move to infectious class HE; infectious individuals (HI) then recover at rate HI; implicit vector-borne transmission is modeled with the compartments γ and κ; λ current force of infection; λ latent force of infection reflecting the exposed state for mosquitoes during the extrinsic incubation period; κ is the transition rate associated to the extrinsic incubation period.τDOI: http://dx.doi.org/10.7554/eLife.19874.003

By contrast, in the second model (Figure 1b) based on Laneri et al. (2010) the vector is modeled implicitly: the two compartments κ and λ do not represent the mosquito population but the force of infection for vector to human transmission. This force of infection passes through two successive stages in order to include the delay associated with the extrinsic incubation period: κ stands for this latent phase of the force of infection whereas λ corresponds directly to the rate at which susceptible humans become infected.

The basic reproduction number of the models (R0) is calculated using the next Generation Matrix method (Diekmann et al., 2010):R0Pandey=βHβVτγμ(μ+τ)R0Laneri=βγ

In addition, we consider that only a fraction ρ of the total population is involved in the epidemic, due to spatial heterogeneity, immuno-resistance, or cross-immunity. For both models we define N=ρ⋅H with H the total size of the population reported by census.

The dynamics of ZIKV transmission in these islands is highly influenced by several sources of uncertainties. In particular, the small population size (less than 7000 inhabitants in Yap) leads to high variability in transmission rates. Therefore all these models are simulated in a discrete stochastic framework (Poisson with stochastic rates [Bretó et al., 2009]), to take this phenomenon into account. Stochasticity requires specific inference techniques: thus estimations are performed with PMCMC algorithm (particle Markov Chain Monte Carlo [Andrieu et al., 2010]).

Using declared Zika cases from different settings, the two stochastic models (

![Figure 2.](https://cdn.elifesciences.org/articles/19874/elife-19874-fig2-v2.jpg)

**Figure 2.:** Posterior median number of observed Zika cases (solid line), 95% credible intervals (shaded blue area) and data points (black dots). First column: particle filter fit. Second column: Simulations from the posterior density. Third column:  posterior distribution. (R0a) Yap. (b) Moorea. (c) Tahiti. (d) New Caledonia. The estimated seroprevalences at the end of the epidemic (with 95% credibility intervals) are: (a) 73% (CI95: 68–77, observed 73%); (b) 49% (CI95: 45–53, observed 49%); (c) 49% (CI95: 45–53, observed 49%); (d) 39% (CI95: 8–92). See Figure 4.DOI: http://dx.doi.org/10.7554/eLife.19874.004

![Figure 3.](https://cdn.elifesciences.org/articles/19874/elife-19874-fig3-v2.jpg)

**Figure 3.:** Posterior median number of observed Zika cases (solid line), 95% credible intervals (shaded blue area) and data points (black dots). First column: particle filter fit. Second column: Simulations from the posterior density. Third column:  posterior distribution. (R0a) Yap. (b) Moorea. (c) Tahiti. (d) New Caledonia. The estimated seroprevalences at the end of the epidemic (with 95% credibility intervals) are: (a) 72% (CI95: 68–77, observed 73%); (b) 49% (CI95: 45–53, observed 49%); c) 49% (CI95: 45–53, observed 49%); d) 65% (CI95: 24–91). See Figure 5.DOI: http://dx.doi.org/10.7554/eLife.19874.005

Regarding model variability, R0 estimates are always higher and coarser with the Pandey model than with the Laneri model (cf. Tables 1–2). The Pandey model has two additional estimated parameters (in particular, the mosquito lifespan), which can explain the higher variability of the output. It is worth noting that these parameters are very sensitive (see Materials and methods). The difference in R0 may also be linked to the difference in the estimated initial number of infected individuals (HI(0)), which is higher in the Laneri model than in the Pandey model. Because of the high proportion of asymptomatic cases (the ratio of asymptomatic:symptomatic is estimated to be 1:1.3, V.-M Cao-Lormeau personal communication), it is hard to determine which scenario is more realistic, the time between introduction of the disease into the island and the first reported symptomatic case being unknown in most settings.

For the durations of infectious and intrinsic incubation (in human) and extrinsic incubation (in mosquito) periods, the posterior density ressembles the informative prior (cf. Figures 6–13), indicating the models’ incapacity to identify properly these parameters without more informative data. Moreover, these parameters have a clear sensitivity (see Materials and methods) and precise field measures are therefore crucial for reliable model predictions.

The fraction ρ of the population involved in the epidemic is well estimated when the seroprevalence is known (in Yap and French Polynesia). In these cases, the proportion of the population involved is slightly greater than the seroprevalence rate, indicating a very high infection rate among involved individuals. In New Caledonia, as no information on seroprevalence was available, the fraction of population involved displays very large confidence intervals (cf. Tables 1 and 2), indicating that the model did not manage to identify properly this parameter with the available data. In this case, this parameter is highly correlated to the observation rate r (cf Figures 17 and 21): r and ρ seem unidentifiable without precise information on seroprevalence.

## Discussion

The reproduction number R0 is a key parameter in epidemiology that characterizes the epidemic dynamics and the initial spread of the pathogen at the start of an outbreak in a susceptible population. R0 can be used to inform public health authorities on the level of risk posed by an infectious disease, vaccination strategy, and the potential effects of control interventions (Anderson and May, 1982). In the light of the potential public health crisis generated by the international propagation of ZIKV, characterization of the potential transmissibility of this pathogen is crucial for predicting epidemic size, rate of spread and efficacy of intervention.

Using data from both surveillance systems and seroprevalence surveys in four different geographical settings across the Pacific (Duffy et al., 2009; CHSP, 2014; Mallet et al., 2015; DASS, 2014; Aubry et al., 2015b), we have estimated the basic reproductive number R0 (see Figures 2–3 and Tables 1–2). Our estimate of R0 obtained by inference based on Particle MCMC (Andrieu et al., 2010) has values in the range 1.6 (1.5–1.7) – 3.2 (2.4–4.1). Our R0 estimates vary notably across settings. Lower and finer R0 values are found in larger islands. This phenomenon can at least in part be explained by large spatial heterogeneities and higher demographic stochasticity for islands with smaller populations, as well as the influence of stochasticity on biological and epidemiological processes linked to virus transmission. This phenomenon can also be specific to the selection of the studied islands or can reflect a highly clustered geographical pattern, the global incidence curve being the smoothed overview of a collection of more explosive small size outbreaks. However, it is notable that the two French Polynesian islands yield similar estimates of R0 despite differing population sizes. Indeed, other important factors differ among French Polynesia, New Caledonia and Yap, such as the human genetic background and their immunological history linked to the circulation of others arboviruses. Moreover, whilst both New Caledonia and French Polynesia populations were infected by the same ZIKV lineage and transmitted by the same principle vector species, Aedes aegypti, the epidemic in Yap occurred much earlier with a different ZIKV lineage (Wang et al., 2016) and vectored by a different mosquito species Aedes hensilli (Ledermann et al., 2014). In French Polynesia, the vector Aedes polynesiensis is also present and dominates in Moorea with higher densities than in Tahiti. Finally, different vector control measures have been conducted in the three countries.

To date, studies investigating Zika outbreaks in the Pacific have always estimated R0 using a deterministic framework. Using a similar version of the Pandey model in French Polynesia, Kucharski et al. (Kucharski et al., 2016) estimated R0 between 1.6 and 2.3 (after scaling to square root for comparison) for Tahiti and between 1.8 and 2.9 in Moorea. These estimates are slightly lower and less variable than ours. This difference can be explained firstly by the chosen priors on mosquito parameters and secondly because our model includes demographic stochasticity. Moreover, they predicted a seroprevalence rate at the end of the epidemic of 95–97%, far from the 49% measured. In Yap island, a study (Funk et al., 2016) used a very detailed deterministic mosquito model, and estimated an R0 for Zika between 2.9 and 8. In this case, our lower and less variable estimates may come from the fact that our model is more parsimonious in the number of uncertain parameters, especially concerning the mosquito population. Finally, a third study (Nishiura et al., 2016a) relied on another method for R0 calculation (based on the early exponential growth rate of the epidemic) in French Polynesia as a whole and in Yap. Again, the obtained parameters are lower than ours in French Polynesia and higher in Yap. The first estimations for South America using a similar methodology (Nishiura et al., 2016b; Towers et al., 2016; Gao et al., 2016) lead to similar R0 values. In all these studies a deterministic framework is used excluding the possibility of accounting for the high variability of biological and epidemiological processes exacerbated by the small size of the population. In these three studies, like in ours, it is worth noting that little insight is obtained regarding mosquito parameters. Posterior distribution mimics the chosen prior (cf. Figures 6–13). Both the simulation of the epidemics and the estimated R0 are highly sensitive to the choice of priors on mosquito parameters, for which precise field measures are rare.

In the absence of sufficient data, the modeling of mosquito-borne pathogen transmission is a difficult task due to non-linearity and non-stationarity of the involved processes (Cazelles and Hales, 2006). This work has then several limitations. First, our study is limited by the completeness and quality of the data, with regard to both incidence and seroprevalence, but, above all, by the scarcity of information available on mosquitoes. Incidence data is aggregated at the island scale and cannot disentangle the effects of geography and observation noise to explain bimodal curves observed in Yap and New Caledonia. Moreover, although all data came from national surveillance systems, we had very little information about the potential degree of under-reporting, especially due to the high proportion of mildly symptomatic cases, at a time when the dangerous complications associated with the virus were unknown. Moreover, some cases might have been misdiagnosed as other flaviviruses, due to similarity in clinical manifestations or cross-reactivity in assays. Seroprevalence data were gathered from small sample sizes and were also sensitive to cross reactivity in populations non naive to dengue. In addition, they were missing in New Caledonia, which leads to strong correlation between our estimation of the observation rate and the fraction of the population involved in the epidemic. Because of the high proportion of asymptomatic or mildly symptomatic cases, the magnitude of the outbreaks is difficult to evaluate without precise seroprevalence data (Metcalf et al., 2016) or detection of mild, asymptomatic or pre-symptomatic infections (Thompson et al., 2016). Considering vectors, no demographic data were available and this partly explains the large variability of our R0 estimations. Secondly, incidence and seroprevalence data were difficult to reconcile; the use of incidence data led to higher infection rates than those observed in the seroprevalence data. This difficulty has been overcome by considering that only a fraction of the population (ρ) is involved in the epidemic and then our model manages to reproduce the observed seroprevalence rate. This exposed fraction could be the result of spatial heterogeneity and high clustering of cases and transmission, as observed for dengue. The small dispersal of the mosquito and the limited population inter-mingling likely leads to considerable spatial variation in the extent of exposure to the virus and pockets of refugia in Tahiti as elsewhere (Telle et al., 2016). For instance, previous dengue infection rates in French Polynesia display large spatial variations even within islands (Daudens et al., 2009). Finer scale incidence and seroprevalence data would be useful to explore this. Another explanation for higher predicted than observed infection rates could be due to interaction with other flaviviruses. The Zika outbreak was concomitant with dengue outbreaks in French Polynesia (CHSP, 2014; Mallet et al., 2015) and New Caledonia (DASS, 2014). Examples of coinfection have been reported (Dupont-Rouzeyrol et al., 2015) but competition between these close pathogens may also have occurred. Finally, mathematical models with vectorial transmission may tend to estimate high attack rates, sometimes leading to a contradiction between observed incidence and observed seroprevalence. Assumptions on the proportionality between infected mosquitoes and the force of infection, as well as the density-dependence assumption in these models could be questioned. Indeed even if these assumptions are at the heart of the mathematical models of mosquito-borne pathogen transmission (Reiner et al., 2013; Smith et al., 2014), a recent review (Halstead, 2008) and recent experimental results (Bowman et al., 2014; Harrington et al., 2014) question these important points.

On a final note, the estimates of R0 for ZIKV are similar to but generally on the lower side of estimates made for two other flaviviruses of medical importance, dengue and Yellow Fever viruses (Favier et al., 2006; Imai et al., 2015; Massad et al., 2003), even though caution is needed in the comparison of studies with differing models, methods and data sources. Interventions strategies developed for dengue should thus enable as, if not more effective control of ZIKV, with the caveat that ZIKV remains principally a mosquito-borne pathogen with little epidemiological significance of the sexual transmission route. Even though further work and data are needed to support this hypothesis (Brauer et al., 2016), two recent studies indicated that sexual transmission alone is not sufficient to sustain an epidemic (Gao et al., 2016; Towers et al., 2016).

In conclusion, using recent stochastic modeling methods, we have been able to determine estimates of R0 for ZIKV with an unexpected relationship with population size. Further data from the current Zika epidemic in South America that is caused by the same lineage as French Polynesia lead to estimates in the same range of values (Nishiura et al., 2016b; Towers et al., 2016; Gao et al., 2016). Our study highlights the importance of gathering seroprevalence data, especially for a virus that often leads to an asymptomatic outcome and it would provide a key component for precise quantitative analysis of pathogen propagation to enable improved planning and implementation of prevention and control strategies.

## Materials and methods

## Data

During the 2007 outbreak that struck Yap, 108 suspected or confirmed Zika cases (16 per 1000 inhabitants) were reported by reviewing medical records and conducting prospective surveillance between April 1st and July 29th 2007 (Duffy et al., 2009). In French Polynesia, sentinel surveillance recorded more than 8700 suspected cases (32 per 1000 inhabitants) across the whole territory between October 2013 and April 2014 (CHSP, 2014; Mallet et al., 2015). In New Caledonia, the first Zika case was imported from French Polynesia on 2013 November 12th. Approximately 2500 cases (9 per 1000 inhabitants) were reported through surveillance between January (first autochtonous case) and August 2014 (DASS, 2014).

For Yap and French Polynesia, the post-epidemic seroprevalence was assessed. In Yap, a household survey was conducted after the epidemic, yielding an infection rate in the island of 73% (Duffy et al., 2009). In French Polynesia, three seroprevalence studies were conducted. The first one took place before the Zika outbreak, and concluded that most of the population was naive for Zika virus (Aubry et al., 2015a). The second seroprevalence survey was conducted between February and March 2014, at the end of the outbreak, and reported a seroprevalence rate around 49% (Aubry et al., 2015b). The third one concerned only schoolchildren in Tahiti and was therefore not included in the present study.

Demographic data on population size were based on censuses from Yap (Duffy et al., 2009), French Polynesia (Insee, 2012), and New Caledonia (Insee, 2014).

## Models and inference

## Model equations

Although the models are simulated in a stochastic framework, we present them with ordinary differential equations for clarity. The reactions involved in the stochastic models are the same as those governed by the deterministic equations, but the simulation process differs through the use of discrete compartments. It is described in the next section.

The equations describing Pandey model are:dHSdt=−βHvIHSdHEdt=βHvIHS−σHEdHIdt=σHE−γHIdHRdt=γHIdvSdt=μ−βVHINvS−μvSdvEdt=βVHINvS−τvE−μvEdvIdt=τvE−μvI

where vs=VSV is the proportion of susceptible mosquitoes, vE=VEV the proportion of exposed mosquitoes, and vI=VIV the proportion of infected mosquitoes. Since we are using a discrete model, we cannot use directly the proportions vS, vE and vI whose values are smaller than one. Therefore, we rescale using V=H, which leads to VS′=vS⋅H, VE′=vE⋅H, and VI′=vI⋅H. In this model, the force of infection for humans is λH=βH⁢vI, and the force of infection for mosquitoes is λV=βV⁢HIN

The equations describing Laneri model are:dHSdt=−λHSdHEdt=λHS−σHEdHIdt=σHE−γHIdHRdt=γHIdκdt=2βHIτN−2τκdλdt=2τκ−2τλ

In this model, the role of mosquitoes in transmission is represented only through the delay they introduce during the extrinsic incubation period (EIP, incubation period in the mosquito). For modeling reasons, this delay is included by representing the force of infection from infected humans to susceptible humans with two compartments κ and λ: in this formalism, the duration between the moment when an exposed individual becomes infectious and the moment when another susceptible individual acquires the infection has a gamma distribution of mean τ-1(Laneri et al., 2010; Roy et al., 2013; Lloyd, 2001). Therefore, λ represents the current force of infection for humans λH=λ . The compartment κ represents the same force of infection but at a previous stage, reflecting the exposed phase for mosquitoes during the extrinsic incubation period. As an analogy to Pandey model, the force of infection for mosquitoes is λV=β⁢HI⁢τvs⁢N, and therefore, the parameter β can be interpreted as the product of a transmission parameter β′ by the proportion of susceptible mosquitoes: β=vs⁢β′. The force of infection for mosquitoes is then similar to Pandey’s : λV=β′⁢τ⁢HIN.

Again, since we are using a discrete model, we cannot use directly the proportions λ and κ whose values are smaller than one. Therefore, we rescale up to a factor N, which leads to L=λ⁢N and K=κ⁢N.

In both models, following the dominant paradigm that diseases transmitted by Aedes mosquitoes are highly clustered, we restricted the total population H measured by census to a fraction N=ρ.H, in which the parameter ρ is estimated. This formulation makes the hypothesis that a fraction of the total population is not at risk from the epidemic, because of individual factors or because the individuals remain in areas where the virus is not present. Moreover as the vector’s flying range is small, the clustering of ZIKV infection may be reinforced. This may result in escapees from infection within the population, even at a single island scale. The available data does not allow further exploration of the mechanisms underlying these phenomena, which seem fundamental to understand ZIKV propagation. At the very least, the restriction to a fraction ρ enables the model to reproduce the observed seroprevalence rates, and to provide coherent results with respect to both data sources (seroprevalence and surveillance data).

## Stochastic framework

Both models are simulated in a stochastic and discrete framework, the Poisson with stochastic rates formulation (Bretó et al., 2009), to include the uncertainties related to small population size. In this framework, the number of reactions occurring in a time interval d⁢t is approximated by a multinomial distribution. In a model with m possible reactions and c compartments, zt being the state of the system at time t and θ the model parameters, the probability that each reaction with rate rk occurs nk times in d⁢t is calculated as follows (Dureau et al., 2013):p(n1,...nm|zt,θ)=∏i=1c{Mi(1−∑X(k)=ipk)ni¯∏X(k)=i(pk)nk}+o(dt)

with, zt(i) being the number of individual in compartment i at time t,

## Observation models

The only observed compartments are the infected humans (incidence measured every week) and the recovered humans (seroprevalence at the end of the outbreak when data is available). In order to link the model to the data, two observation models, for both incidence and seroprevalence data, are needed.

## Observation model on incidence data

The observed weekly incidence is assumed to follow a negative binomial distribution (Bretó et al., 2009) whose mean equals the number of new cases predicted by the model times an estimated observation rate r.

The observation rate r accounts for non observed cases, due to non reporting from medical centers, mild symptoms unseen by health system, and asymptomatic infections. Without additional data, it is not possible to make a distinction between these three categories of cases. We also implicitely make the assumption that these cases transmit the disease as much as reported symptomatic cases.

The observation model for incidence data is therefore :I⁢n⁢co⁢b⁢s=N⁢e⁢g⁢B⁢i⁢n⁢(ϕ-1,11+ϕ⁢r⁢I⁢n⁢c)

I⁢n⁢co⁢b⁢s being the observed incidence, and I⁢n⁢c the incidence predicted by the model. The dispersion parameter (Bretó et al., 2009) ϕ is fixed at 0.1.

## Observation model on seroprevalence data

Seroprevalence data is fitted for Tahiti, Moorea, and Yap settings. It is assumed that the observed seroprevalence at the end of the epidemic follows a normal distribution with fixed standard deviation, whose mean equals the number of individuals in the HR compartment predicted by the model.

The observation model for seroprevalence data is therefore :HRo⁢b⁢s=N⁢o⁢r⁢m⁢a⁢l⁢(HR,Λ)

at the last time step, with notations detailed for each model in Table 3.10.7554/eLife.19874.008Table 3.Details of the observation models for seroprevalenceDOI: http://dx.doi.org/10.7554/eLife.19874.008IslandDateStandard deviationObserved seroprevalenceΛHRo⁢b⁢sYap2007-07-291505005 (Duffy et al., 2009)Moorea2014-03-283250.49 × 16200 = 7938 (Aubry et al., 2015b)Tahiti2014-03-2835620.49 × 178100 = 87269 (Aubry et al., 2015b)

## Prior distributions

Informative prior distributions are assumed for the mosquito lifespan, the duration of infectious period, and both intrinsic and extrinsic incubation periods. The initial numbers of infected mosquitoes and humans are estimated, and the initial number of exposed individuals is set to the initial number of infected to reduce parameter space. We assume that involved populations are naive to Zika virus prior to the epidemic and set the initial number of recovered humans to zero. The other priors and associated references are listed in Table 4.10.7554/eLife.19874.009Table 4.Prior distributions of parameters. 'Uniform[0,20]' indicates a uniform distribution in the range [0,20]. 'Normal(5,1) in [4,7]' indicates a normal distribution with mean five and standard deviation 1, restricted to the range [4,7].DOI: http://dx.doi.org/10.7554/eLife.19874.009ParametersPandey modelLaneri modelReferencesR02squared basic reproduction numberUniform[0, 20]Uniform[0, 20]assumedβVtransmission from human to mosquitoUniform[0,10].assumedγ-1infectious period (days)Normal(5,1) in [4,7]Normal(5,1) in [4,7](Mallet et al., 2015)σ-1intrinsic incubation period (days)Normal(4,1) in [2,7]Normal(4,1) in [2,7](Nishiura et al., 2016b; Bearcroft, 1956; Lessler et al., 2016)τ-1extrinsic incubation period (days)Normal(10.5,1) in [4,20]Normal(10.5,1) in [4,20](Hayes, 2009; Chouin-Carneiro et al., 2016)μ-1mosquito lifespan (days)Normal(15,2) in [4,30].(Brady et al., 2013; Liu-Helmersson et al., 2014)ρfraction of population involvedUniform[0,1]Uniform[0,1]Initial conditions (t=0)Pandey modelLaneri modelHI(0)infected humansUniform[10-6,1]NUniform[10-6,1]NHE(0)exposed humansHI(0)HI(0)HR(0)recovered humans00infected vectorsVI(0)=Uniform[10-6,1]HL(0)=Uniform[10-6,1]Nexposed vectorsVE(0) = VI(0)K(0)=L(0)Local conditionsYapMooreaTahitiNew CaledoniaReferencesrobservation rateUniform[0,1]Uniform[0,1]Uniform[0,0.3]Uniform[0,0.23](Mallet et al., 2015; DASS, 2014)Hpopulation size6,89216,200178,100268,767(Duffy et al., 2009; Insee, 2012, 2014)

The range for the prior on observation rate is reduced for Tahiti and New Caledonia, in order to reduce the parameter space and facilitate convergence. In both cases, we use the information provided with the data source. In French Polynesia, 8750 cases we reported, but according to local health authorities, more than 32,000 people would have attended health facilities for Zika (Mallet et al., 2015) (8750/32000 ≤ 0.3). In New Caledonia, approximately 2500 cases were reported but more than 11,000 cases were estimated by heath authorities (DASS, 2014) (2500/11000 ≤ 0.23). In both cases, these extrapolations are lower bounds on the real number of cases (in particular, they do not estimate the number of asymptomatic infections), and therefore can be used as upper bounds on the observation rate.

## Estimations

## Inference with PMCMC

The complete model is represented using the state space framework, with two equation systems: the transition equations refer to the transmission models, and the measurement equations are given by the observation models.

In a deterministic framework, this model could be directly estimated using MCMC, with a Metropolis-Hastings algorithm targeting the posterior distribution of the parameters. This algorithm would require the calculation of the model likelihood at each iteration.

In our stochastic framework, the model output is given only through simulations and the likelihood is intractable. In consequence, estimations are performed with the PMCMC algorithm (particle Markov Chain Monte Carlo (Andrieu et al., 2010)), in the PMMH version (particle marginal Metropolis-Hastings). This algorithm uses the Metropolis-Hastings structure, but replaces the real likelihood by its estimation with Sequential Monte Carlo (SMC).

Algorithm 1 PMCMC (Andrieu et al., 2010) (PMMH version, as in SSM (Dureau et al., 2013))In a model with n observations and J particles. q(.|θ(i)) is the transition kernel.1: Initialize θ(0). 2: Using SMC algorithm, compute p^(y1:n|θ(0)) and sample x0:n∗ from p^(x0:n|y1:n,θ(0)). 3: for i=1...N do 4:  Sample θ∗ from q(.|θ(i)) 5:  Using SMC algorithm, compute L(θ∗)=p^(y1:n|θ∗) and sample x0:n∗ from p^(x0:n|y1:n,θ∗) 6:  Accept θ* (et x0:n∗) with probability 1∧L(θ(i))q(|θ∗)L(θ∗)q(θ∗|θ(i)) 7:  If accepted, θ(i+1)=θ∗ and x0:n(i+1)=x0:n∗. Otherwise θ(i+1)=θ(i) and x0:n(i+1)=x0:n(i). 8: end for

SMC (Doucet et al., 2001) is a filtering method that enables to recover the latent variables and estimate the likelihood for a given set of parameters. The data is treated sequentially, by adding one more data point at each iteration. The initial distribution of the state variables is approximated by a sample a particles, and from one iteration to the next, all the particles are projected according to the dynamic given by the model. The particles receive a weight according to the quality of their prediction regarding the observations. Before the next iteration, all the particles are resampled using these weights, in order to eliminate low weight particles and concentrate the computational effort in high probability regions. Model likelihood is also computed sequentially at each iteration (Dureau et al., 2013; Doucet and Johansen, 2011).

Algorithm 2 SMC (Sequential Monte Carlo, as implemented in SSM [Dureau et al., 2013])In a model with n observations and J particles.L is the model likelihood p(y1:T|θ). Wk(j) is the weight and xk(j) is the state associated to particle j at iteration k.1: Set L=1, W0(j)=1/J. 2: Sample (x0(j))j=1:J from p(x|θ0). 3: for k=0:n-1j=0:Jdo 4:  for j=0:jdo 5:   Sample (xk+1(j))j=1:J from p(xk+1|xk,θ) 6:   Set α(j)=p(yk+1|xk+1(j),θ) 7:  end for 8:  Set Wk+1(j)=α(j)∑l=1Jα(l) and L=L⁢1J⁢∑jα(l) 9:  Resample (x0:k+1(j))j=1:J from Wk+1(j) 10: end for

A gaussian kernel q(.|θ(i)) is used in the PMCMC algorithm, with mean θ(i) and fixed variance Σq (random walk Metropolis Hastings).

## Initialization

PMCMC algorithm is very sensitive to initialization of both the parameter values θ(0) and the covariance matrix Σq. Several steps of initialization are therefore used.

Firstly, parameter values are initialized by maximum likelihood through simplex algorithm on a deterministic version of the model. We apply the simplex algorithm to a set of 1000 points sampled in the prior distributions and we select the parameter set with the highest likelihood.

Secondly, in order to initialise the covariance matrix, an adaptative MCMC (Metropolis Hastings) framework is used (Roberts and Rosenthal, 2009; Dureau et al., 2013). It uses the empirical covariance of the chain Σ(i), and aims to calibrate the acceptance rate of the algorithm to an optimal value. The transition kernel is also mixed (with a probability α=0.05) with another gaussian using the identity matrix to improve mixing properties.qA(.|x(i))=αN(x(i),λ2.382dId)+(1−α)N(x(i),λ2.382dΣ(i))

The parameter λ is approximated by successive iterations using the empirical acceptance rate of the chain.λi+1=λi⁢ai⁢(A⁢c⁢c⁢R⁢a⁢t⁢ei-0.234)

The adaptative PMCMC algorithm itself may have poor mixing properties without initialization. A first estimation of the covariance matrix is computed using KMCMC algorithm (Dureau et al., 2013). In the KMCMC algorithm, the model is simulated with stochastic differential equations (intermediate between deterministic and Poisson with stochastic rates frameworks) and the SMC part of the adaptative PMCMC is replaced by the extended Kalman filter. When convergence is reached with KMCMC, then, adaptative PMCMC is used.

The PMCMC algorithm is finally applied on the output of the adaptative PMCMC, using 50,000 iterations and 10,000 particles. Calculations are performed with SSM software (Dureau et al., 2013) and R version 3.2.2.

## R0 Calculation

R0 is calculated using the Next Generation Matrix approach (NGM) (19).

## R0 Calculation in Pandey model

F=(000βH00000βv000000)v=(−σ0000−γ0000−(μ+τ)0000−μ)

Then we have,V−1=(−1/σ000−1/γ−1/γ0000−1/(μ+τ)000−τ/[μ(τ+μ)]−1/μ)

andFV−1=(00−βHτ/[μ(τ+μ)]−βH/μ0000−βv/γ−βv/γ000000)

We calculate the eigen values α of -F⁢V-1 :|−α0βHτ/[μ(τ+μ)]βH/μ0−α00βv/γβv/γ−α0000−α|=α2(α2−βHβVτγμ(τ+μ))=0

Then α=0 or α=±βHβVτγμ(τ+μ) and the highest eigenvalue is R0=βH⁢βV⁢τγ⁢μ⁢(τ+μ).

This formula defines R0 as "the number of secondary cases per generation" (Dietz, 1993): i.e R0 can be written as the geometric mean R0=R0v⁢R0h, where R0v is the number of infected mosquitoes after the introduction of one infected human in a naive population, and R0h is the number of infected humans after the introduction of one infected mosquito in a naive population. With this definition, herd immunity is reached when (1-R0-2) of the population is vaccinated (Dietz, 1993).

## R0 Calculation in Laneri model

Following the analogy with Pandey model, we compute the spectral radius of the NGM for the Laneri model.F=(000100000βτ000000)V=(−σ0000−γ0000−τ000τ−τ)

Then we have,V−1=(−1/σ000−1/γ−1/γ0000−1/τ000−1/τ−1/τ)

andFV−1=(00−1/τ−1/τ0000−βτ/γ−βτ/γ000000)

We calculate the eigen values α of -F⁢V-1 :|−α01/τ1/τ0−α00βτ/γβτ/γ−α0000−α|=α2(α2−βτγτ)=0

Then α=0 or α=±βγ and the highest eigenvalue is αR=βγ.

Because λ and κ can be seen as parameters rather than state variables, the interpretation of the spectral radius as the R0 of the model is not straightforward. Therefore, we computed the R0 of the model through simulations, by counting the number of secondary infections after the introduction of a single infected individual in a naive population. Since Laneri model is considered here as a vector model, the number of infected humans after the introduction of a single infected is considered as R02. We simulated 1000 deterministic trajectories, using parameter values sampled in the posterior distributions for all parameters except initial conditions. With this method, the confidence intervals for number of infected humans (R02) are similar to the ones of αR2 estimated by the model. As a consequence, R0 was approximated by the spectral radius of the NGM in our results with our stochastic framework (cf. Table 5).10.7554/eLife.19874.010Table 5.Square root of the number of secondary cases after the introduction of a single infected individual in a naive population. Median and 95% credible intervals of 1000 deterministic simulations using parameters from the posterior distribution.DOI: http://dx.doi.org/10.7554/eLife.19874.010Pandey modelLaneri modelYap3.1 (2.5–4.3)2.2 (1.9–2.6)Moorea2.6 (2.2–3.3)1.8 (1.6–2.0)Tahiti2.4 (2.0–3.2)1.6 (1.5–1.7)New Caledonia2.0 (1.8–2.2)1.6 (1.5–1.7)

As a robustness check, the same method was applied to Pandey model : the confidence intervals for the number of secondary cases in simulations are very similar to the ones of R02 (cf. Table 5).

## Sensitivity analysis

In order to analyse the influence of parameter values on the model’s outputs, a sensitivity analysis was performed, using LHS/PRCC technique (Blower and Dowlatabadi, 1994), on Tahiti example. Similar results were obtained for the other settings. Three criteria were retained as outputs for the analysis: the seroprevalence at the last time point, the intensity of the peak of the outbreak and the date of the peak. We used uniform distributions for all parameters, which are listed in Tables 6 and 7. For model parameters, we used the same range as for the prior distribution. For initial conditions, the observation rate r and the fraction involved in the epidemic ρ, we used the 95% confidence interval obtained by PMCMC, in order to avoid unrealistic scenarios.10.7554/eLife.19874.011Table 6.Sensitivity analysis in Pandey model. Tahiti island. 1000 parameter sets were sampled with latin hypercube sampling (LHS), using 'lhs' R package (Carnell, 2016). On each parameter set, the model was simulated deterministically in order to explore variability in parameters without interference with variations due to stochasticity. PRCC were computed using the 'sensitivity' R package (Pujol et al., 2016).DOI: http://dx.doi.org/10.7554/eLife.19874.011ParametersDistributionSeroprevalencePeak intensityPeak dateModel parametersR02Uniform[0,20]0.870.90−0.55βVUniform[0,10]−0.66−0.730.35γ-1Uniform[4,7]−0.250.100.20σ-1Uniform[2,7]−0.03−0.100.15τ-1Uniform[4,20]−0.05−0.070.06μ-1Uniform[4,30]−0.56−0.700.49Initial conditionsHI(0)Uniform[2.10-5,0.011]0.05−0.020.02VI(0)Uniform[10-4,0.034]0.11−0.00−0.26Fraction involved and observation modelρUniform[0.46,0.54]0.470.15−0.03rUniform[0.048,0.072]−0.040.030.0510.7554/eLife.19874.012Table 7.Sensitivity analysis in Laneri model. Tahiti island. 1000 parameter sets were sampled with latin hypercube sampling (LHS), using 'lhs' R package (Carnell, 2016). On each parameter set, the model was simulated deterministically in order to explore variability in parameters without interference with variations due to stochasticity. PRCC were computed using the 'sensitivity' R package (Pujol et al., 2016).DOI: http://dx.doi.org/10.7554/eLife.19874.012ParametersDistributionSeroprevalencePeak intensityPeak dateModel parametersR02Uniform[0,20]0.620.93−0.50γ-1Uniform[4,7]0.010.620.15σ-1Uniform[2,7]−0.03−0.540.21τ-1Uniform[4,20]−0.03−0.700.47Initial conditionsHI(0)Uniform[10-5,0.015]0.050.02−0.32L(0)Uniform[2.10-5,0.004]0.050.00−0.16Fraction involved and observation modelρUniform[0.49,0.59]0.800.340.02rUniform[0.048,0.068]−0.010.01−0.02

For all criteria, the key parameters in both models are transmission parameters (R0 and βV). High values for R0 are positively correlated with a large seroprevalence and a high and early peak. On the contrary, high values for the parameters introducing a delay in the model, the incubation periods in human (σ-1) and in mosquito (τ-1), are associated with a lower and later peak, and have no significant effect on seroprevalence. Moreover, the simulations are clearly sensitive to the other model parameters, in particular the mosquito lifespan (μ-1) in Pandey model.

Concerning other parameters, the initial conditions have a noticeable effect on the date of the peak only. As expected, the fraction involved in the epidemic (ρ) influences the magnitude of the outbreak, by calibrating the proportion of people than can be infected, but it has no significant effect on the timing of the peak.

## Complementary results

These complementary results include PMCMC results for both models in the four settings: the epidemic trajectories regarding the human compartments for infected and recovered individuals (

![Figure 4.](https://cdn.elifesciences.org/articles/19874/elife-19874-fig4-v2.jpg)

**Figure 4.:** Simulations from the posterior density: posterior median (solid line), 95% and 50% credible intervals (shaded blue areas) and observed seroprevalence (black dots). First column: Infected humans (). Second column: Recovered humans (HI). (HRa) Yap. (b) Moorea. (c) Tahiti. (d) New Caledonia.DOI: http://dx.doi.org/10.7554/eLife.19874.013

![Figure 5.](https://cdn.elifesciences.org/articles/19874/elife-19874-fig5-v2.jpg)

**Figure 5.:** Simulations from the posterior density: posterior median (solid line), 95% and 50% credible intervals (shaded blue areas) and observed seroprevalence (black dots). First column: Infected humans (). Second column: Recovered humans (HI). (HRa) Yap. (b) Moorea. (c) Tahiti. (d) New Caledonia.DOI: http://dx.doi.org/10.7554/eLife.19874.014

![Figure 6.](https://cdn.elifesciences.org/articles/19874/elife-19874-fig6-v2.jpg)

**Figure 6.:** Pandey model, Yap island.DOI: http://dx.doi.org/10.7554/eLife.19874.015

![Figure 7.](https://cdn.elifesciences.org/articles/19874/elife-19874-fig7-v2.jpg)

**Figure 7.:** Pandey model, Moorea island.DOI: http://dx.doi.org/10.7554/eLife.19874.016

![Figure 8.](https://cdn.elifesciences.org/articles/19874/elife-19874-fig8-v2.jpg)

**Figure 8.:** Pandey model, Tahiti island.DOI: http://dx.doi.org/10.7554/eLife.19874.017

![Figure 9.](https://cdn.elifesciences.org/articles/19874/elife-19874-fig9-v2.jpg)

**Figure 9.:** Pandey model, New Caledonia.DOI: http://dx.doi.org/10.7554/eLife.19874.018

![Figure 10.](https://cdn.elifesciences.org/articles/19874/elife-19874-fig10-v2.jpg)

**Figure 10.:** Laneri model, Yap island.DOI: http://dx.doi.org/10.7554/eLife.19874.019

![Figure 11.](https://cdn.elifesciences.org/articles/19874/elife-19874-fig11-v2.jpg)

**Figure 11.:** Laneri model, Moorea island.DOI: http://dx.doi.org/10.7554/eLife.19874.020

![Figure 12.](https://cdn.elifesciences.org/articles/19874/elife-19874-fig12-v2.jpg)

**Figure 12.:** Laneri model, Tahiti island.DOI: http://dx.doi.org/10.7554/eLife.19874.021

![Figure 13.](https://cdn.elifesciences.org/articles/19874/elife-19874-fig13-v2.jpg)

**Figure 13.:** Laneri model, New Caledonia.DOI: http://dx.doi.org/10.7554/eLife.19874.022

![Figure 14.](https://cdn.elifesciences.org/articles/19874/elife-19874-fig14-v2.jpg)

**Figure 14.:** Pandey model, Yap island.DOI: http://dx.doi.org/10.7554/eLife.19874.023

![Figure 15.](https://cdn.elifesciences.org/articles/19874/elife-19874-fig15-v2.jpg)

**Figure 15.:** Pandey model, Moorea island.DOI: http://dx.doi.org/10.7554/eLife.19874.024

![Figure 16.](https://cdn.elifesciences.org/articles/19874/elife-19874-fig16-v2.jpg)

**Figure 16.:** Pandey model, Tahiti island.DOI: http://dx.doi.org/10.7554/eLife.19874.025

![Figure 17.](https://cdn.elifesciences.org/articles/19874/elife-19874-fig17-v2.jpg)

**Figure 17.:** Pandey model, New Caledonia.DOI: http://dx.doi.org/10.7554/eLife.19874.026

![Figure 18.](https://cdn.elifesciences.org/articles/19874/elife-19874-fig18-v2.jpg)

**Figure 18.:** Laneri model, Yap island.DOI: http://dx.doi.org/10.7554/eLife.19874.027

![Figure 19.](https://cdn.elifesciences.org/articles/19874/elife-19874-fig19-v2.jpg)

**Figure 19.:** Laneri model, Moorea island.DOI: http://dx.doi.org/10.7554/eLife.19874.028

![Figure 20.](https://cdn.elifesciences.org/articles/19874/elife-19874-fig20-v2.jpg)

**Figure 20.:** Laneri model, Tahiti island.DOI: http://dx.doi.org/10.7554/eLife.19874.029

![Figure 21.](https://cdn.elifesciences.org/articles/19874/elife-19874-fig21-v2.jpg)

**Figure 21.:** Laneri model, New Caledonia.DOI: http://dx.doi.org/10.7554/eLife.19874.030

## Correlation between estimated parameters

The inference technique may fail to estimate some parameters due to identifiability issues. In particular, when two parameters are highly correlated to one another, the model manages to estimate the pair of parameters but not each one separately. The analysis of correlation between parameters’ posterior distributions can reveal such cases. The following graphics display for each model the correlation coefficients between all pairs of parameters across the MCMC chain. For example, in models for New Caledonia, the observation rate and the fraction of the population involved in the epidemic are strongly negatively correlated (Figures 17,21): the inference technique does not manage to estimate properly these two parameters, due to the lack of information on seroprevalence.

## Code and source data files

The estimation tools are provided by the open source software SSM (Dureau et al., 2013) (State Space Models, RRID:SCR_014647), available at https://github.com/JDureau/ssm and https://github.com/sballesteros/ssm-predict. The codes for the implementation of each model are provided as supplementary file.
