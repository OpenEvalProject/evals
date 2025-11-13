# Modelling the contribution of the hypnozoite reservoir to Plasmodium vivax transmission

## Authors

- Michael T White<sup>1</sup> †
- Stephan Karl<sup>2</sup>
- Katherine E Battle<sup>4</sup>
- Simon I Hay<sup>4</sup> ([ORCID: 0000-0002-0611-7272](https://orcid.org/0000-0002-0611-7272))
- Ivo Mueller<sup>2</sup>
- Azra C Ghani<sup>1</sup>

### Affiliations

1. MRC Centre for Outbreak Analysis and Modelling, Department of Infectious Disease Epidemiology Imperial College London London United Kingdom
2. Department of Infection and Immunity Walter and Eliza Hall Institute Melbourne Australia
3. Department of Medical Biology University of Melbourne Melbourne Australia
4. Spatial Ecology and Epidemiology Group, Department of Zoology University of Oxford Oxford United Kingdom
5. Fogarty International Center National Institutes of Health Bethesda United States
6. Centre de Recerca en Salut Internacional de Barcelona Barcelona Spain

† Corresponding author

## Abstract

Plasmodium vivax relapse infections occur following activation of latent liver-stages parasites (hypnozoites) causing new blood-stage infections weeks to months after the initial infection. We develop a within-host mathematical model of liver-stage hypnozoites, and validate it against data from tropical strains of P. vivax. The within-host model is embedded in a P. vivax transmission model to demonstrate the build-up of the hypnozoite reservoir following new infections and its depletion through hypnozoite activation and death. The hypnozoite reservoir is predicted to be over-dispersed with many individuals having few or no hypnozoites, and some having intensely infected livers. Individuals with more hypnozoites are predicted to experience more relapses and contribute more to onwards P. vivax transmission. Incorporating hypnozoite killing drugs such as primaquine into first-line treatment regimens is predicted to cause substantial reductions in P. vivax transmission as individuals with the most hypnozoites are more likely to relapse and be targeted for treatment.

## Introduction

The study of the transmission dynamics of vector-borne diseases such as Plasmodium falciparum malaria has a rich history, with a theoretical foundation based on the Ross-Macdonald models (malERA Consultative Group on Modeling, 2011; Smith et al., 2012; Reiner et al., 2013; Smith et al., 2014), a class of mathematical models describing the transmission of a pathogen between human and vector hosts. In the case of P. falciparum, the parasite has a reservoir in both the human host and the Anopheles mosquito, with transmission occurring when a mosquito takes a blood meal from a human. Ross-Macdonald models have provided insights into the dynamics of P. falciparum transmission resulting in valuable guidance for historical and contemporary malaria control programmes, most notably the large reductions in transmission that are achievable if the lifespan of the mosquito is reduced through vector control (Macdonald, 1952a; Macdonald, 1952b).

In contrast to the extensive theory of the mathematical epidemiology of P. falciparum malaria (Smith et al., 2012), P. vivax malaria has been comparatively neglected. This is in spite of P. vivax being the geographically most widely distributed species of malaria in the world, causing in the region of 80–300 million clinical episodes every year (Mueller et al., 2009a; Gething et al., 2012). P. falciparum models are not applicable to P. vivax as they fail to account for the reservoir of dormant liver stages (hypnozoites) which give rise to relapsing infections—one of the defining characteristics of the biology and epidemiology of P. vivax (Mueller et al., 2009a). In natural transmission settings relapses are often undistinguishable from re-infections from new mosquito bites or recrudescences of existing blood-stage infections. When the origin of renewed parasitemia following primary P. vivax infection is unknown, it can be classified as a recurrent infection (Battle et al., 2014).

Most existing models of malaria transmission do not account for the additional reservoir of parasites in the liver, but the hypnozoite reservoir has been incorporated into some P. vivax transmission models as a state to denote hypnozoite infection (Ishikawa et al., 2003; Chamchod and Beier, 2013; Roy et al., 2013) or as up to two broods of hypnozoites (Dezoysa et al., 1991). Relapse patterns and their implications for transmission have also been investigated using statistical distributions for the time to first relapse (Lover et al., 2014). Here we advance on existing work by considering how the number of hypnozoites in the liver contributes to patterns of relapse infections and the epidemiology and control of P. vivax.

When a P. vivax infected mosquito takes a blood meal from a human, sporozoites are injected into the skin and migrate to the liver, where they invade hepatocytes and develop into either actively dividing schizonts or dormant hypnozoites. The development of actively dividing schizonts may lead to a primary blood-stage infection and potentially clinical malaria (Mueller et al., 2013). Hypnozoites will lie dormant in the liver for weeks to years before activating to initiate new blood-stage infections. The biological mechanisms regulating the activation of hypnozoites remain unknown (Mueller et al., 2009a), although a number of triggers for relapses have been proposed, including fever caused by other pathogens such as P. falciparum (Shanks and White, 2013) and exposure to Anopheles-specific proteins (Hulden and Hulden, 2011).

There is considerable geographical variation in the timing and frequency of P. vivax relapse infections, with strains from tropical areas having an average time to first relapse of 3–6 weeks and long-latency strains from temperate areas relapsing within 6–9 months (Lover and Coker, 2013; Battle et al., 2014). Beyond the first relapse, periodic patterns in multiple relapses from a single mosquito bite have been observed (White, 2011). For example, following a single infection with a tropical strain of P. vivax the time until next relapse has been observed to increase with each successive relapse (Berliner et al., 1948; White, 2011). In contrast, temperate strains are associated with a long latency period until first relapse (of the order of 6 months) followed by short intervals between successive relapses (Coatney et al., 1950; Hankey et al., 1953; White, 2011). A descriptive epidemiology of P. vivax relapses will thus require estimation of three key quantities: (i) the time to first relapse, (ii) the number of relapses per primary infection, and (iii) the duration of hypnozoite carriage.

In this manuscript, a within-host model of hypnozoites in liver hepatocytes is developed to demonstrate that many of the epidemiological patterns of relapse infections can be explained by making the assumption that hypnozoites activate and die at a constant rate. This model is integrated into the existing theory of Ross-Macdonald models to account for the relapse infections characteristic of P. vivax malaria. We use this model to provide qualitative insights into the relative contribution of relapses to P. vivax transmission and illustrate the consequences for controlling P. vivax with vector control and anti-malarial drugs.

## Results

### Within-host relapse model

Figure 1 shows the best fit within-host relapse model to data on time to first relapse infection from three ecological zones with tropical strains of P. vivax: South America, South East Asia and Melanesia (Battle et al., 2014). In each ecological zone, the number of hypnozoites N and the hypnozoite activation rate α were correlated (see Figure 1—figure supplement 1). For example, a short time to relapse could be explained by a single fast activating hypnozoite or a large number of slow activating hypnozoites. Longitudinal data where multiple relapses are observed in individuals would allow better estimation of the number of hypnozoites in the liver and the duration of hypnozoite carriage.

![Figure 1.](https://cdn.elifesciences.org/articles/04692/elife-04692-fig1-v2.jpg)

**Figure 1.:** Time to first relapse infection from the within-host model fitted to data from three ecological zones with tropical strains of P. vivax (Battle et al., 2014). The red curves show the model fits with estimated posterior median parameters.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/04692/elife-04692-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** The likelihood in Equation 12 was sampled using a Metropolis–Hastings Markov Chain Monte Carlo (MCMC) algorithm and the posterior parameter distributions were estimated. 100,000 MCMC iterations were sampled and visually checked for convergence and mixing. The top row shows the MCMC chains. The middle row shows the correlation between pairs of parameters. The bottom row shows the sampled posterior distributions. Prior distributions are shown in blue. Note the high degree of correlation between N and α.

The within-host model can be used to simulate beyond the first relapse infection. Figure 2 shows some sample relapse patterns from the within-host models for tropical and temperate strains of P. vivax. This model predicts notable dose-dependency with increased numbers of hypnozoites associated with a greater number of relapses and shorter time to first relapse. Following the long latency to first relapse in temperate strains, the interval between subsequent relapses is considerably shorter. The within-host model assumes that hypnozoites act independently of each other, and hence the time to next relapsing hypnozoite is exponentially distributed. In particular we do not predict periodicity between relapsing hypnozoites (in the absence of external triggers [White, 2011; Shanks and White, 2013]). If the simulated data are censored such that relapses occurring within 14 days of a previous relapse remain undetected (due to either prophylaxis by blood-stage anti-malarials or the presence of parasites from an existing infection) then there is an apparent periodicity in detected relapses. The observed periodicity of relapses will be determined by the duration of prophylactic protection and not via the biological mechanisms considered here. The periodicity in detected relapses is most evident for large numbers of hypnozoites with the period being determined by the assumed duration of prophylactic protection (Figure 2—figure supplement 1). However, as has been previously argued, periodicity in relapses could also be attributable to a cycle of fevers initiating hypnozoite activation which in turn cause new blood-stage infections and malaria-associated fevers (White, 2011).

![Figure 2.](https://cdn.elifesciences.org/articles/04692/elife-04692-fig2-v2.jpg)

**Figure 2.:** A relapse is assumed to be undetected if it occurs within 14 days of a detected relapse. Both tropical and temperate phenotypes exhibit dose dependency, with a larger number of hypnozoites giving rise to a greater number of relapses and shorter times to first relapse. For larger numbers of hypnozoites (N = 50), periodicity in detected relapses is observed. The appearance of this periodicity is due to the undetected relapses.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/04692/elife-04692-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** For the tropical phenotype the time between relapses was calculated as the mean duration between consecutive relapses over the first 6 months based on 10,000 stochastic simulations. For the temperate phenotype the time between relapses was calculated as the mean duration between consecutive relapses over the first 12 months based on 10,000 stochastic simulations. The red curves denote the time between detected relapses: it is assumed that within 14 days of a detected relapse some activating hypnozoites can go undetected due to anti-malarial prophylaxis or the presence of blood-stage parasites. The grey curve denotes the expected time between all consecutively activating hypnozoites. The dashed line denotes a 3 week duration which has been regularly been observed as a common period between consecutive relapses (White, 2011).

Figure 3 shows the predicted number of relapsing hypnozoites in a population exposed to P. vivax in the absence of new infections. For tropical strains the mean number of hypnozoites in the liver is expected to decrease exponentially, but the proportion of individuals carrying hypnozoites is expected to decrease at a slower rate as an individual can relapse even if they have just one hypnozoite (Figure 3A). For temperate strains the mean number of hypnozoites in the liver decreases slowly, as hypnozoites remain in the long-latency phase for approximately 6 months (Figure 3B). The model allows estimation of time to second, third and consecutive relapses in addition to estimates of time to first relapse obtainable via survival analysis of patient data (Lover and Coker, 2013; Battle et al., 2014) (Figure 3C,D). The expected number of relapsing hypnozoites per individual is expected to follow an approximately exponential distribution (Figure 3E,F) in agreement with empirical observations (Horing, 1947; White, 2011).

![Figure 3.](https://cdn.elifesciences.org/articles/04692/elife-04692-fig3-v2.jpg)

**Figure 3.:** (A and B) Duration of hypnozoite carriage (orange) and expected number of hypnozoites in the liver (dashed). For the temperate strain, the dashed blue line shows the number of hypnozoites in the relapsing phase. (C and D) Survival time until nth relapsing hypnozoite. The red curve is equivalent to the Kaplan–Meier curve for time to first blood-stage infection that would be observed in the absence of new infections from mosquito bites. Only the curves for the first five relapses are shown. (E and F) Proportion of individuals with at least n relapsing hypnozoites following primary infection.

### Dynamics and steady states of P. vivax transmission

Figure 4A shows the predicted steady states (the equilibrium blood-stage prevalence in the absence of seasonally varying transmission) as a function of entomological inoculation rate (EIR). EIR is a measurement of the number of infectious bites per person per year. The proportion of people infected with hypnozoites is predicted to be higher than the proportion infected with P. vivax blood-stage parasites. For a given EIR, P. vivax blood-stage prevalence is predicted to be higher than P. falciparum prevalence as a single mosquito bite can give rise to multiple blood-stage infections. However this does not account for the longer duration of P. falciparum infections as a consequence of antigenic switching (Molineaux et al., 2001), and the important role of heterogeneity in exposure (Smith et al., 2005). With the exception of the P. vivax hypnozoite rate, these quantities can be measured in epidemiological field studies (Smith et al., 2005; Kelly-Hope and McKenzie, 2009).

![Figure 4.](https://cdn.elifesciences.org/articles/04692/elife-04692-fig4-v2.jpg)

**Figure 4.:** (A) The statics (estimated equilibrium prevalence) of P. vivax and P. falciparum transmission for different values of the entomological inoculation rate (EIR). EIR was varied by changing the number of mosquitoes per person m. (B) The number of hypnozoites per person is expected to increase with transmission intensity. The black line denotes the median number of hypnozoites, and the shaded areas denote the 50% and 95% ranges. (C) The distribution of the hypnozoite reservoir when PvPR = 50%. The grey bar represents individuals with zero hypnozoites.

Figure 4B shows how the median number of hypnozoites increases with increasing P. vivax transmission. Figure 4C shows the distribution in the number of hypnozoites when PvPR = 50%. The number of hypnozoites per individual is predicted to be over-dispersed following a negative binomial distribution. Thus some individuals will harbour a large number of hypnozoites while some will have none. This phenomenon will be further amplified if there is heterogeneity in exposure where some individuals receive a large number of mosquito bites.

### Control of P. vivax

The impact of malaria control interventions will depend on how effectively the parasite is targeted in each of the reservoirs in the mosquito, the blood and the liver. Figure 5 shows the qualitative effects of malaria control on the transmission dynamics of P. falciparum and P. vivax. Vector control with insecticide treated nets (ITNs) or indoor residual spraying (IRS) is assumed to increase mosquito mortality. The introduction of vector control is expected to cause a rapid decline in P. falciparum parasite rate (PfPR), and a smaller and slower decline in P. vivax (Figure 5A).

![Figure 5.](https://cdn.elifesciences.org/articles/04692/elife-04692-fig5-v2.jpg)

**Figure 5.:** (A) The introduction of vector control with ITNs or IRS (assumed to increase mosquito mortality by 30%) is predicted to cause substantial reductions in both PvPR and PfPR. (B) Simulated effect of expanding first-line treatment with blood-stage anti-malarial drugs (e.g., chloroquine or ACTs) so that 20% and 40% of new blood-stage infections are treated. (C) Simulated effect of first-line treatment with a combined regimen of blood-stage anti-malarials and primaquine to remove liver-stage hypnozoites.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/04692/elife-04692-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** Treatment coverage χ is assumed, that is, the proportion of new blood-stage infections that receive treatment with blood-stage anti-malarials. There will be a delay between the emergence of parasites into the blood-stream and the administration of treatment following symptoms. This stage is described by treatment compartment Ti and lasts 1/ν = 7 days. Importantly, transmission to mosquitoes is possible during this stage as P. vivax gametocytes (the sexual stage of the parasite that can be transmitted to mosquitoes) are present in the blood very early on in the infection. Following treatment, individuals progress to a period of prophylactic protection Pi, during which they are not susceptible to new blood-stage infections but may still acquire hypnozoites from new bites from infectious mosquitoes. It is assumed that individuals remain under prophylactic protection for 1/ξ = 14 days after which they return to being susceptible Si.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/04692/elife-04692-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** The incorporation of primaquine into first-line treatment regimens is accounted for by assuming that treatment clears all hypnozoites from the liver as well as clearing blood-stage infections. A 14 day daily dosing regimen of primaquine which has proven efficacy at preventing relapses. In particular we assume treatment eliminates all hypnozoites, so that treated individuals move to compartment P0 (under prophylaxis from treatment and with all hypnozoites removed). The 14 day treatment regimen is assumed to provide a period of prophylactic protection against new hypnozoite infection, that is, new hypnozoites cannot be acquired while primaquine is being administered.

Figure 5B shows the effect of targeting the parasite reservoir in the blood by providing first-line treatment for new blood-stage infections with anti-malarial drugs such as chloroquine or artemisinin combination therapies (ACTs). See details of how treatment was implemented in the model are provided in Figure 5—figure supplement 1,2. Increasing treatment coverage leads to reductions in blood-stage prevalence of both P. falciparum and P. vivax. Notably the reduction in the P. vivax hypnozoite rate is slow as the hypnozoite reservoir is not directly targeted.

The hypnozoite reservoir can be directly targeted using a drug such as primaquine that can eliminate hypnozoites from the liver (Wells et al., 2010). The inclusion of primaquine in first-line treatment regimens is predicted to cause substantial reductions in both the P. vivax parasite rate and hypnozoite rate (Figure 5C), as individuals being treated for blood-stage P. vivax infections will also have their hypnozoites removed. A consequence of this strategy is that the hypnozoite reservoir can be targeted efficiently, as individuals with the most hypnozoites are most likely to relapse and potentially be detected by health systems. Figure 6 shows how the inclusion of primaquine in first-line treatment regimens preferentially targets the most intense infections, with the greatest reductions observed in individuals with the most hypnozoites.

![Figure 6.](https://cdn.elifesciences.org/articles/04692/elife-04692-fig6-v2.jpg)

**Figure 6.:** Proportion of the population infected with 1–2, 3–9 or 10+ hypnozoites following the introduction of a first-line treatment regimen with blood-stage anti-malarial drugs and primaquine. Individuals with large numbers of hypnozoites are more likely to experience new blood-stage infections and hence become targeted for treatment and have their hypnozoites removed. This results in a selective targeting of the most intensely infected individuals.

## Discussion

Relapse infections arising from the activation of hypnozoites in the human liver have important consequences for the transmission dynamics of P. vivax. Hypnozoites in the liver constitute a third malaria parasite reservoir, in addition to the reservoirs in the blood circulation and mosquito also present for P. falciparum. Relapses can be incorporated into Ross-Macdonald models of malaria transmission through the addition of a state to represent the hypnozoite reservoir (Roy et al., 2013), or as demonstrated here, through consideration of the number of hypnozoites in the liver. This allows the intensity of hypnozoite infection to be estimated which is crucial for understanding patterns of relapse infections (White, 2011) and evaluating the effect of interventions such as primaquine treatment that directly target the hypnozoite reservoir. Hypnozoites are assumed to be subjected to two processes: activation at constant rate α, and death at constant rate µ. By considering infection with batches of hypnozoites, these simple processes can explain many of the complex patterns observed in P. vivax relapses (see Box 1).

A key assumption in the proposed model is the constant activation of hypnozoites. This implies that relapses can occur immediately after primary P. vivax infection, in contrast to suggestions that the first relapse does not occur until 2–3 weeks later. The best evidence on early relapses comes from treatment efficacy studies where patients treated for P. vivax are followed for recurrent infection for 42 days (Douglas et al., 2010). Except in cases with documented chloroquine resistance (Price et al., 2014), recurrent infections are rarely observed prior to day 14, however the inclusion of long-lasting anti-malarials in treatment regimens provides prophylaxis during this period making detection of parasites unlikely. In a recent study of the slowly eliminated drug dihydroartemisinin-piperaquine (DP) Tarning et al. (2014) tested a model where relapses occur in bursts every 3 weeks, but it arguably provided no better fit to the data than a model of constant hypnozoite activation. Testing the hypothesis of constant activation would require follow up of patients treated with rapidly eliminated artemisinin monotherapy, a challenging proposition given the concerns over artemisinin resistant P. falciparum (Ashley et al., 2014).

Although the model captures the key drivers of the dynamics of P. vivax transmission, it is a simplified representation subject to a number of limiting assumptions. The potential role of triggers of hypnozoite activation such as febrile illness (Shanks and White, 2013) are not accounted for. There is no heterogeneity or seasonality in transmission, and no age structure. Incorporation of the acquisition of natural immunity into the model will be particularly important for settings with high transmission intensity where immunity has a role in regulating blood-stage infections (Mueller et al., 2013). It is assumed that all individuals infected with blood-stage parasites are capable of transmitting to mosquitoes. Similar to the corresponding P. falciparum models, incorporation of these factors would change the quantitative predictions of the model, but not its qualitative behaviour.

P. falciparum and P. vivax parasite prevalence (PfPR and PvPR) are the most widely reported and best validated metrics of malaria transmission from epidemiological studies (Gething et al., 2011a; Gething et al., 2012) providing measurements of the proportion of individuals with detectable blood-stage parasites. In settings with similar levels of P. vivax and P. falciparum transmission, the model predicts PvPR to be greater than PfPR due to the additional blood-stage infections arising from relapses. However, this does not agree with empirical observations which find PfPR to be similar to or greater than PvPR (Snounou and White, 2004; Mueller et al., 2009b). This is most likely explained by the rapid acquisition of immunity to P. vivax (Koepfli et al., 2013; Mueller et al., 2013) the low detectability of P. vivax blood-stage infections (Harris et al., 2010), and the longer durations of P. falciparum blood-stage infection (Molineaux et al., 2001) not captured in the model. Furthermore, the additional P. vivax parasite reservoir in the liver means that PfPR and PvPR are not directly comparable metrics. Thus if a parasitological survey indicates similar parasite prevalence, a greater control effort will be required to reduce P. vivax transmission than to reduce P. falciparum transmission because of the additional infections emerging from the hypnozoite reservoir. The model described here allows the proportion of individuals harbouring hypnozoites to be estimated given metrics such as PvPR. The number of hypnozoites per person is predicted to be over-dispersed with some individuals with intensely infected livers and most carrying few or no hypnozoites (Figure 4C). Estimates of the prevalence and intensity of hypnozoite infection will be dependent on both the uncertainty in the measurable data and the model assumptions.

Vector control with ITNs or IRS, and treatment with effective anti-malarial drugs are the cornerstones of malaria control efforts targeting the parasite in the vector and the human host, however they are predicted to have different effects on P. vivax and P. falciparum transmission. Vector control interventions that increase mosquito mortality are expected to cause greater reductions in PfPR than PvPR (Figure 5A), as higher levels of P. vivax transmission can be maintained with fewer mosquito bites. This has been observed in both Thailand (Sattabongkot et al., 2004) and Brazil (Coura et al., 2006) where increased vector control has caused greater reductions in P. falciparum than P. vivax.

First-line treatment of new blood-stage infections with anti-malarial drugs such as chloroquine or ACTs is predicted to cause moderate reductions in blood-stage prevalence of both P. falciparum and P. vivax (Figure 5B). The addition of primaquine to first-line treatment regimens is expected to cause large reductions in P. vivax blood-stage prevalence, as individuals with the most intense hypnozoite infections are more likely to relapse and be targeted for treatment and hence have their hypnozoites eliminated. The potential to simultaneously target parasite reservoirs in the blood and liver may turn the cause of P. vivax parasites' robust transmission into its Achilles' heel.

In P. vivax and P. falciparum co-endemic regions, heterogeneity in exposure to mosquito bites may cause associations between P. falciparum fevers and the risk of future P. vivax relapses (Douglas et al., 2011). Thus the inclusion of primaquine in first-line treatment for P. falciparum may also reduce P. vivax transmission. In addition to inclusion in first-line treatment regimens, primaquine can also be administered as part of mass drug administration (MDA) programmes. In treatment-reinfection studies of Papua New Guinean children (Betuela et al., 2012; Robinson et al., unpublished), mass administration of drugs such as chloroquine or artemether-lumefantrine successfully cleared P. vivax blood-stage infections but rapid recurrence of infection was observed during follow-up—most likely due to relapses. The addition of primaquine to the treatment regimen caused large reductions in the rate of recurrent infections.

Although primaquine treatment clears the hypnozoite reservoir, it requires a difficult 14 day treatment regimen, and is not without risk due to vulnerability to haemolytic toxicity among glucose-6-phosphate dehydrogenase (G6PD) deficient patients (Howes et al., 2013). Individuals should thus be tested for G6PD deficiency (Kim et al., 2011) before the administration of primaquine. A primaquine analogue, tafenoquine, is currently undergoing phase three trials and is likely to be licensed for use by 2017 (Llanos-Cuentas et al., 2014). Tafenoquine requires a single dose alongside a 3 day chloroquine regimen, but is subject to the same risks in G6PD deficient patients. A quantitative model of P. vivax transmission will allow for the benefits of primaquine treatment to be weighed against the risks of G6PD deficiency and the costs of G6PD testing.

Mathematical models of malaria transmission that account for P. vivax relapses can provide valuable insights into the impact of malaria control interventions on the parasite's reservoirs in the vector, the blood and the liver. In the absence of effective diagnostics for detecting liver-stage parasites (malERA Consultative Group on Diagnoses and Diagnostics, 2011), models will play a crucial role in estimating and predicting the effectiveness of interventions that target the hypnozoite reservoir, either indirectly via vector control and blood-stage anti-malarials or directly via primaquine treatment.

## Materials and methods

### Within-host model for tropical relapses

Following infection with a tropical strain of P. vivax, the population dynamics of hypnozoites in the liver can be described by a within-host model where each hypnozoite is subject to two processes: (i) activation leading to relapse infection; and (ii) death, either of the hypnozoite itself or the host hepatocyte (Malato et al., 2011). Constant activation (α) and death (µ) rates are assumed implying hypnozoite residence time in the liver is exponentially distributed. The long latency of temperate strains before first relapse can be accounted for by assuming a period of dormancy during which hypnozoites must wait before they can activate. A schematic representation of the within-host model is presented in Figure 7.

![Figure 7.](https://cdn.elifesciences.org/articles/04692/elife-04692-fig7-v2.jpg)

**Figure 7.:** Hypnozoites from tropical strains of P. vivax will progress to the relapsing phase where they are subject to two processes: death and activation leading to relapse. Hypnozoites from temperate strains will begin in a temperate long-latency phase where they must wait before progressing to the relapsing phase.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/04692/elife-04692-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** Orange compartments denote the temperate long-latency phase. Green compartments denote the relapsing phase. Superscript N denotes that the infection began with N hypnozoites. In the long-latency phase, sub-script i, j denotes i hypnozoites in the jth compartment for progressing through the long-latency phase. In the relapsing phase, subscript i denotes the number of hypnozoites. An individual infected with N hypnozoites of a tropical strain begins in the HNN compartment and progresses to HN0 as hypnozoites activate or die. An individual infected with N hypnozoites of a temperate strain begins in the LNN,1 compartment, and progresses down the flow diagram through the M steps during the period of long-latency. During this time they may also move to the right along the flow diagram as the number of hypnozoites reduces due to death. After passing through the M compartments for the long-latency phase, infections will enter the relapsing phase where relapse can occur.

The tropical relapse model is assumed to begin with an initial population of N hypnozoites, each of which can either activate at rate α, or die at rate µ, independently of each other. The number of hypnozoites in the liver will decay exponentially with an expected Ne−(µ+α)t hypnozoites at time t. Let $H_{i}^{N}(t)$ denote the probability that i of N hypnozoites remain in the liver after time t. The hypnozoite population dynamics can be described by the following set of equations:

$$
\frac{dH_{N}^{N}}{dt}=−(\mu+\alpha)NH_{N}^{N}\frac{dH_{i}^{N}}{dt}=−(\mu+\alpha)iH_{i}^{N}+(\mu+\alpha)(i+1)H_{i+1}^{N},i=0…N−1
$$

Equation 1 can be solved analytically to give:

$$
H_{i}^{N}(t)=(Ni)e^{−N(\mu+\alpha)t}(e^{(\mu+\alpha)t}−1)^{N−i}
$$

Define $P_{j}^{N}(t)$ to be the probability that j relapses have occurred by time t. This can be calculated as follows: if i hypnozoites remain in the liver, then N − i have either activated or died. The probability of each hypnozoite activating is $\frac{\alpha}{\mu+\alpha}$. The probability that j of N − i hypnozoites have activated can thus be calculated from a binomial distribution. Summing over the allowable number of hypnozoites (at least j hypnozoites must have activated or died for j relapses to be observed) gives:

$$
P_{j}^{N}(t)=\sumi=0N−j(N−ij)(\frac{\alpha}{\mu+\alpha})^{j}(\frac{\mu}{\mu+\alpha})^{N−i−j}H_{i}^{N}(t)=(Nj)\frac{\alpha^{j}\mu^{N−j}}{(\mu+\alpha)^{N}}(1−e^{−(\mu+\alpha)t})^{N}(1+\frac{\mu+\alpha}{\mu}\frac{1}{e^{(\mu+\alpha)t}−1})^{N−j}
$$

Equations 1–3 describe the population dynamics of hypnozoites in a single individual with N hypnozoites in the absence of exposure to new infections. In a population of individuals, we would expect substantial variation in the numbers of hypnozoites due to heterogeneity in exposure and the variation in sporozoite inoculum from each infectious mosquito bite (Beier et al., 1991; Medica and Sinnis, 2005; White et al., 2013). Based on evidence that the number of sporozoites injected with a mosquito bite approximately follows a geometric distribution (Beier et al., 1991), we assume that the number of hypnozoites following a primary infection is also geometrically distributed. If the mean number of hypnozoites is N, then the probability of k hypnozoites is $(\frac{N}{N+1})^{k}\frac{1}{N+1}$. Assuming a geometrically distributed number of hypnozoites, the three quantities describing the epidemiology of relapses can be estimated in terms of the within-host parameters. The expected number of relapsing hypnozoites is:

$$
h=\sumk=0∞(\frac{N}{N+1})^{k}\frac{1}{N+1}︸probability of k initial hypnozoites  k  \frac{\alpha}{\alpha+\mu}︸probability of each hypnozoite relapsing=N\frac{\alpha}{\mu+\alpha}
$$

The mean duration of hypnozoite carriage is:

$$
\frac{1}{\gamma}=\sumk=0∞(\frac{N}{N+1})^{k}\frac{1}{N+1}︸probability of k initial hypnozoites\sumi=1k\frac{1}{i}\frac{1}{\mu+\alpha}︸duration of k hypnozoites=\frac{log(N+1)}{\mu+\alpha}
$$

The expected time to first relapse is:

$$
\frac{1}{f}=\sumk=1∞[(\frac{N}{N+1})^{k}\frac{1}{N}]︸probability of k initial hypnozoites\sumi=1k[(\frac{\mu}{\mu+\alpha})^{k−i}\frac{\alpha}{\mu+\alpha}/(1−(\frac{\mu}{\mu+\alpha})^{k})]︸probability of hypnozoite i being first to relapse\sumj=0k−i\frac{1}{k−j}\frac{1}{\mu+\alpha}︸time to relapse
$$

The within-host relapse model describes a baseline scenario in the absence of potential external triggers for relapse such as fever (Shanks and White, 2013). Underlying assumptions of this model are: (i) each hypnozoite acts independently of other hypnozoites, for example, hypnozoites will not activate in batches due to mechanisms such as quorum sensing; and, (ii) hypnozoite death occurs at a constant rate, due to either death of the hypnozoite within the hepatocyte or death of the hepatocyte itself (Malato et al., 2011). The activation of a hypnozoite may not directly correspond to a detected relapse. For example, an infection arising from two hypnozoites activating within a day of each other is likely to be classified as a single relapse.

### Within-host model for temperate relapses

The within-host model can be extended to account for temperate strains of P. vivax. We assume that before a hypnozoite is capable of activating, it must undergo a long-latency phase of duration d. During this period hypnozoites are subject to death at rate µ. In particular, we assume that the time spent in the temperate long-latency phase can be described by a gamma distribution with mean d and variance d2/M. This gamma distribution can be simulated by M successive compartments with exponential waiting times 1/δ = d/M. Increasing the number of compartments M reduces the variance in the duration of the dormancy period (Wearing et al., 2005). Following a primary infection where N hypnozoites of a temperate phenotype develop in the liver, we define $L_{i,j}^{N}$ as the probability that i of N hypnozoites are waiting in long-latency compartment number j, then the number of dormant and potentially active hypnozoites can be described by the following system of differential equations.

$$
\frac{dL_{N,1}^{N}}{dt}=−\deltaL_{N,1}^{N}−N\muL_{N,1}^{N}\frac{dL_{i,1}^{N}}{dt}=−\deltaL_{i,1}^{N}−i\muL_{i,1}^{N}+(i+1)\muL_{i+1,1}^{N}i=1…N−1\frac{dL_{N,j}^{N}}{dt}=−\deltaL_{N,j}^{N}+\deltaL_{N,j+1}^{N}−N\muL_{N,j}^{N}j=2…M\frac{dL_{i,j}^{N}}{dt}=−\deltaL_{i,j}^{N}+\deltaL_{i,j+1}^{N}−i\muL_{i,j}^{N}+(i+1)\muL_{i+1,j}^{N}i=1…N−1, j=2…M\frac{dH_{N}^{N}}{dt}=\deltaL_{N,M}^{N}−N(\mu+\alpha)H_{N}^{N}\frac{dH_{i}^{N}}{dt}=\deltaL_{i,M}^{N}−i(\mu+\alpha)H_{i}^{N}+(i+1)(\mu+\alpha)H_{i+1}^{N}i=1…N−1\frac{dH_{0}^{N}}{dt}=\sumj=1M\muL_{1,j}^{N}+(\mu+\alpha)H_{1}^{N}
$$

The equations are presented schematically in Figure 7—figure supplement 1. Equation 7 cannot be solved analytically and must be computed numerically to calculate $H_{i}^{N}(t)$ and $L_{i,j}^{N}(t)$. A greater deal of uncertainty surrounds the biological processes accounting for the initial long-latency phase observed in temperate strains of P. vivax. In the model implemented here, it is assumed that all hypnozoites in an infection must undergo some waiting period before any of them can activate, and that during the long-latency phase hypnozoites are at risk of death due to natural hepatocyte death.

### P. vivax transmission model

We next embedded the within-host model for tropical relapses in a model for the transmission of P. vivax between humans and mosquitoes (Figure 8). The transmission dynamics are driven by two processes: (i) transmission of parasites through mosquito bites; and (ii) relapsing of liver-stage hypnozoites to cause new blood-stage infections. As per the standard Ross-Macdonald theory, the force of blood-stage infections in humans can be calculated as the product of the number of mosquitoes per human m, the rate at which each mosquito bites a human host a, the probability of transmission from mosquito to human following an infectious bite b, and the proportion of mosquitoes that are infectious IM, to give λ = mabIM. Parameter values are provided in Table 1. The force of infection on mosquitoes can be calculated in a similar manner. We assume that people can be susceptible (Si) or infected with blood-stage parasites (Ii), where i denotes the number of hypnozoites in the liver.

![Figure 8.](https://cdn.elifesciences.org/articles/04692/elife-04692-fig8-v2.jpg)

**Figure 8.:** Within-host model for tropical relapses embedded in a transmission model. Si denotes the proportion of humans susceptible to blood-stage infection with i hypnozoites. Ii denotes the proportion of humans with blood-stage infections carrying i hypnozoites. Individuals in all compartments are exposed to primary infections at rate λ, following which they will move down the flow diagram to a compartment representing blood-stage infection and carrying a greater number of hypnozoites.

**Table 1.**
 Description of model parameters


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Description</th>
      <th>Value</th>
      <th>Reference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="4">Within-host</td>
    </tr>
    <tr>
      <td>N</td>
      <td>number of hypnozoites per infection</td>
      <td>8.5</td>
      <td>estimate*</td>
    </tr>
    <tr>
      <td>α</td>
      <td>rate of hypnozoite activation</td>
      <td>1/332 day−1</td>
      <td>estimate*</td>
    </tr>
    <tr>
      <td>µ</td>
      <td>rate of hypnozoite/hepatocyte death</td>
      <td>1/425 day−1</td>
      <td>estimate*</td>
    </tr>
    <tr>
      <td>d</td>
      <td>duration of temperate long-latency</td>
      <td>180 days</td>
      <td>(Battle et al., 2014)</td>
    </tr>
    <tr>
      <td>σd</td>
      <td>standard deviation of temperate long-latency</td>
      <td>30 days</td>
      <td>(Battle et al., 2014)</td>
    </tr>
    <tr>
      <td>M</td>
      <td>number of compartments for simulating long-latency: M = (d/σd)2</td>
      <td>36</td>
      <td></td>
    </tr>
    <tr>
      <td>δ</td>
      <td>rate of progression through long-latency compartments: δ = M/d</td>
      <td>0.2 day−1</td>
      <td></td>
    </tr>
    <tr>
      <td colspan="4">Humans</td>
    </tr>
    <tr>
      <td>b</td>
      <td>transmission probability: mosquito to human</td>
      <td>0.5</td>
      <td>(Smith et al., 2010)</td>
    </tr>
    <tr>
      <td>r</td>
      <td>rate of clearance of blood-stage infections</td>
      <td>1/60 day−1</td>
      <td>(Collins et al., 2003)</td>
    </tr>
    <tr>
      <td>f</td>
      <td>relapse frequency (1/time to first relapse)</td>
      <td>1/76 day−1</td>
      <td>Equation 6</td>
    </tr>
    <tr>
      <td>h</td>
      <td>expected number of relapses</td>
      <td>4.7</td>
      <td>Equation 4</td>
    </tr>
    <tr>
      <td>γ</td>
      <td>rate of hypnozoite clearance</td>
      <td>1/420 day−1</td>
      <td>Equation 5</td>
    </tr>
    <tr>
      <td colspan="4">Mosquitoes</td>
    </tr>
    <tr>
      <td>a</td>
      <td>mosquito biting frequency</td>
      <td>0.21 day−1</td>
      <td>(Garrett-Jones, 1964)</td>
    </tr>
    <tr>
      <td>g</td>
      <td>mosquito death rate (1/mosquito life expectancy)</td>
      <td>0.1 day−1</td>
      <td>(Gething et al., 2011b)</td>
    </tr>
    <tr>
      <td>m</td>
      <td>number of mosquitoes per human</td>
      <td>calculated</td>
      <td></td>
    </tr>
    <tr>
      <td>n</td>
      <td>duration of sporogony in mosquito</td>
      <td>12 days</td>
      <td>(Gething et al., 2011b)</td>
    </tr>
    <tr>
      <td>c</td>
      <td>transmission probability: human to mosquito</td>
      <td>0.23</td>
      <td>(Bharti et al., 2006)</td>
    </tr>
  </tbody>
</table>

_*Based on estimates from South East Asian tropical strains._

The increase in hypnozoites in the liver is determined by the force of infection λ and the number of hypnozoites per infection N, and the decrease is due to hypnozoite activation α and death µ. The model depicted in Figure 8 can be described by the following set of equations:

$$
\frac{dS_{i}}{dt}=−\lambdaS_{i}−i(\mu+\alpha)S_{i}+(i+1)\muS_{i+1}+ρ_{i}I_{i}i=0…∞\frac{dI_{i}}{dt}=−\lambdaI_{i}+\sumj=0i\lambda_{j→i}(S_{j}+I_{j})−i(\mu+\alpha)I_{i}+(i+1)(\mu+\alpha)I_{i+1}+(i+1)\alphaS_{i+1}−ρ_{i}I_{i}i=0…∞\frac{dS_{M}}{dt}=g−ac(\sumi=0∞I_{i})(e^{−gn}−I_{M})−gS_{M}\frac{dI_{M}}{dt}=ac(\sumi=0∞I_{i})(e^{−gn}−I_{M})−gI_{M}
$$

where $\lambda_{j→i}=\lambda(\frac{N}{N+1})^{i−j}\frac{1}{N+1}$. In the absence of super-infection, the recovery from blood-stage infection is $ρ_{i}=r$. Accounting for super-infections (Dietz and Molineaux, 1973; Smith et al., 2012) gives $ρ_{i}=\frac{\lambda+i\alpha}{e^{\frac{\lambda+i\alpha}{r}}−1}$.

### Model parameterisation

The within-host model for tropical relapses was fitted in a Bayesian framework to data on time to first relapse infection from three ecological zones with tropical strains of P. vivax: South America, South East Asia and Melanesia (see Source data 1). The data are described in detail by Battle et al. (2014). Individual-level data on time to first recurrence was collated from individuals exposed to P. vivax infection (either via natural exposure or artificial challenge) and mostly followed up in the absence of exposure to new infections (Battle et al., 2014). The likelihood of the tropical relapse model can be evaluated by applying the model to the data on time to first relapse infection. The first detected relapse will occur after clearance of parasites from the primary infection and after the period of prophylactic protection from anti-malarial drugs. Define QN(t) to be the probability that at least 1 of N hypnozoites has relapsed by time t.

$$
Q^{N}(t)=1−P_{0}^{N}(t)=1−(\frac{\mu+\alphae^{−(\mu+\alpha)t}}{\mu+\alpha})^{N}
$$

Accounting for a geometrically distributed number of hypnozoites gives:

$$
Q^{G(N)}(t)=\sumk=0∞\frac{1}{N+1}(\frac{N}{N+1})^{k}Q^{k}(t)
$$

where G(N) denotes a geometric distribution.

An individual j followed up after a primary P. vivax infection will either relapse (Ij = 1) or avoid infection (Ij = 0). Denote τj to be the time of detection of infection, or if uninfected, the time until the end of follow up. The likelihood of the parameters θ = {N, α, µ} given the data Dj = {Ij, τj} is:

$$
L(\theta|D_{j})=(\frac{dQ^{G(N)}}{dt}|_{t=\tau_{j}})^{I_{j}}(1−Q^{G(N)}(\tau_{j}))^{1−I_{j}}
$$

The log-likelihood (LL) for all j individuals is:

$$
LL=\sumj(I_{j}log(\frac{dQ^{G(N)}}{dt}|_{t=\tau_{j}})+(1−I_{j})log(1−Q^{G(N)}(\tau_{j})))
$$

Data on time to first relapse were not sufficiently informative to estimate the three parameters simultaneously and hence prior distributions were assumed. N was assumed to have an informative gamma prior distribution with median 10 (95% credible interval (CrI): 1, 28) (Beier et al., 1991). µ was assumed to have an informative gamma prior distribution with median 1/200 (95% CrI: 1/309, 1/140) day−1 (Malato et al., 2011). α was assumed to have an uninformative uniform prior distribution U(0,1). The likelihood in equation (Ishikawa et al., 2003) was sampled using a Metropolis–Hastings Markov Chain Monte Carlo (MCMC) algorithm and the posterior parameter distributions estimated (Figure 1—figure supplement 1). The posterior median parameter estimates and 95% credible intervals are presented in Supplementary file 1.
