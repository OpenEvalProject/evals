# Determinants of MDA impact and designing MDAs towards malaria elimination

## Authors

- Bo Gao<sup>1</sup> ([ORCID: 0000-0002-7405-7507](https://orcid.org/0000-0002-7405-7507))
- Sompob Saralamba<sup>2</sup>
- Yoel Lubell<sup>1</sup>
- Lisa J White<sup>1</sup>
- Arjen M Dondorp<sup>1</sup> ([ORCID: 0000-0001-5190-2395](https://orcid.org/0000-0001-5190-2395))
- Ricardo Aguas<sup>1</sup> ([ORCID: 0000-0002-6507-6597](https://orcid.org/0000-0002-6507-6597)) †

### Affiliations

1. Centre for Tropical Medicine and Global Health, Nuffield Department of Medicine, University of Oxford Oxford United Kingdom
2. Mahidol-Oxford Tropical Medicine Research Unit, Faculty of Tropical Medicine, Mahidol University Bangkok Thailand

† Corresponding author

## Abstract

Malaria remains at the forefront of scientific research and global political and funding agendas. Malaria models have consistently oversimplified how mass interventions are implemented. Here, we present an individual based, spatially explicit model of P. falciparum malaria transmission that includes all the programmatic implementation details of mass drug administration (MDA) campaigns. We uncover how the impact of MDA campaigns is determined by the interaction between implementation logistics, patterns of human mobility and how transmission risk is distributed over space. Our results indicate that malaria elimination is only realistically achievable in settings with very low prevalence and can be hindered by spatial heterogeneities in risk. In highly mobile populations, accelerating MDA implementation increases likelihood of elimination; if populations are more static, deploying less teams would be cost optimal. We conclude that mass drug interventions can be an invaluable tool towards malaria elimination in low endemicity areas, specifically when paired with effective vector control.

## Introduction

In Southeast Asia, and particularly the Greater Mekong Sub-region (GMS), Plasmodium falciparum transmission has decreased substantially over the last two decades (World Health Organization, 2011; World Health Organization, 2010b), setting the stage for pre-elimination scenarios, with all GMS countries committing to ambitious elimination timelines (World Health Organization, 2013a). Alignment of global funding bodies’ goodwill with sound national malaria control programmes is crucial for elimination timelines to be met (World Health Organization, 2013c; Alonso and Tanner, 2013), but spreading artemisinin resistance creates a race against time before malaria becomes untreatable with currently available drugs (World Health Organization, 2010a; World Health Organization, 2013b).

Vector control and early diagnosis followed by effective antimalarial treatment have been the mainstay of malaria control programmes, but modelling based projections indicate these approaches alone are unlikely to achieve P. falciparum malaria elimination before failing drug efficacy becomes an issue. Elimination will require more intensive measures to clear the infectious reservoir in asymptomatic populations, especially in the GMS where existing vector bionomics make vector control particularly challenging. The most abundant vector species in the GMS are exophilic (mainly bite outdoors), do not preferentially bite humans, and can bite quite early in the evening (Sinka et al., 2011), rendering typical vector control measures such as insecticide treated nets (ITNs) and indoor residual spraying (IRS) sub-optimal.

Population wide interventions, including mass drug administration (MDA), are under consideration to clear the infectious reservoir in asymptomatic populations and potentially hasten progress toward elimination (Poirot et al., 2013; World Health Organization, 2015a). The proportion of the target population receiving these interventions (‘coverage’) is believed to determine their success (World Health Organization, 2013c; Slater et al., 2015; Okell, 2015; Stuckey et al., 2016). This success can be considered at two spatial levels: global or local. Whilst malaria elimination campaigns have been carried out successfully in some countries or locally in specific regions (Snow et al., 2013; John et al., 2009; World Health Organization, 2015b), reintroductions of malaria from surrounding endemic areas are a constant threat (Cohen et al., 2012; Galappaththy et al., 2013). The importance of mobile populations as a source of malaria transmission in the GMS has been emphasized in recent years (Pindolia et al., 2012; Prosper et al., 2012; Pindolia et al., 2014; Smith and Whittaker, 2014; Edwards et al., 2015; Guyant et al., 2015). Prompt treatment of new clinical cases through village malaria worker (VMW) or village health worker (VHW) networks has proven to be an effective case management strategy (Maude et al., 2014; Rutta et al., 2012) and would be an essential barrier against malaria reintroduction.

We argue that the way in which mass interventions are deployed is what determines their success likelihood. The most efficient and effective roll-outs are laid on a solid community engagement foundation, thus ensuring subsequent adherence and coverage, while preventing malaria reintroduction from adjacent areas. Here, we model target areas as a collection of discrete villages (unit of intervention) and define coverage as the proportion of individuals receiving the intervention within a village and also as proportion of villages receiving the intervention within an area. Critically, we also simulate the minutia of mass intervention roll outs, with all its relevant deployment logistics, thus assigning coverage a temporal dimension which measures the time it takes for all target villages to receive the intervention.

Conducting enough clinical trials to understand the interaction between all variables at play during a mass drug administration, as well as their individual and combined contribution to the expected outcome, is prohibitive. Hence, we turn to computational modelling to explore the relationships between logistical aspects of MDA implementation and demographic aspects such as human population mobility in diverse epidemiological settings (characterized by prevalence, seasonality patterns and heterogeneity in mosquito densities across space). Our focus in on how the predicted impact of mass intervention strategies on malaria transmission changes when these logistical intricacies are taken into consideration, and its implication for the likelihood of P. falciparum elimination. Our research questions are threefold: 1) what is the relevance of logistical implementation details to the outcome of mass interventions? 2) How fast does target coverage need to be reached for the strategy to be successful? 3) What are the key modulators of malaria elimination likelihood in a short timeframe? To offer strategic guidance to national malaria control programmes we also need to understand how the answers to these questions hinge on key features of malaria transmission in specific areas such as artemisinin resistance levels, population mobility networks, transmission heterogeneity over space, and seasonality patterns.

### Model description

We developed a modular simulation platform that is customizable to any malaria transmission setting to provide realistic outcome predictions for local and global level interventions. The modules are the building blocks of an individual based, discrete time, spatially explicit, stochastic model, with explicit mosquito population dynamics and human population movements. We thus have villages with different mosquito densities connected by a human flow network, on which different interventions are deployed at different times (Figure 1). One particular innovation compared to previous published work (Gatton and Cheng, 2010; Okell et al., 2011; Maude et al., 2012; Gerardin et al., 2015; Nikolov et al., 2016) is the inclusion of very detailed logistical processes related to intervention deployment in the field.

![Figure 1.](https://cdn.elifesciences.org/articles/51773/elife-51773-fig1-v2.jpg)

**Figure 1.:** (A) Flow diagram representing the natural history of Plasmodium falciparum infections in human populations. Uninfected individuals (S) can be infected at rate λ, with the probability of developing clinical symptoms (σ) depending on their immunity level i and number of lifetime infections j. Clinical infections (C) can be detected and subsequently treated at rate τ to a treated state (T), or naturally subside into an asymptomatic parasite carrier stage (A) at rate ε. Treated individuals lose their drug at rate ω. After recovery or treatment, individuals become susceptible with an added level of clinical immunity (Si+1). Clinical immunity level decays at rate α. (B) Probability of developing clinical malaria depending on individual’s history of infection (cumulative number of infections) for each immunity level considered here. (C) Village connectivity network. Geo-located villages appear as circles the size of which is proportional to the number of people living there. Edge width reflects individuals’ probability of travel between connected villages. (D) Each village is assigned a specific mosquito density/vectorial capacity, with transmission heterogeneity over space characterized by three different distributions.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/51773/elife-51773-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** Depicts the age distribution of the simulated individuals.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/51773/elife-51773-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** Displays the simultaneous fit to 4 measured relationships between age and clinical immunity. The black dots refer to the data points offering a measurement for clinical immunity in each of these endemic settings. The red line shows the output of $1-[(imm_a*exp(-0.1(cml-1))+exp(-imm_b*(cml+1)))/sqrt(lvl)]$, for the estimated values of imm_a and imm_b taking as inputs the mean values of cml and lvl (taken from the model output) in individuals of age given by the X-axis. The grey bands represent the 95% credible intervals.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/51773/elife-51773-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** The black dots depict the data points in the Guerra et al. (2007) database. The colored dots show 100 thousand individual model predictions for the observable prevalence in a village (aggregated over 100 runs with 1000 villages each) with EIR given in the X-axis. These 100 runs scan the biting rate parameter space, increasing the mean biting rate in 1000 village for each run, until a desirable coverage of EIR values is obtained. Each color signifies a different distribution of how mosquito densities vary over space. The more extreme distribution (Pareto) displays a higher variance, more in line with that observed in the data, particularly for low EIR values. This is caused by population movement, with people living in these low EIR villages potentially being infected in very high EIR villages when they visit them.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/51773/elife-51773-fig1-figsupp4-v2.jpg)

**Figure 1—figure supplement 4.:** Compares the predicted clinical malaria case incidence for varying levels of prevalence (red), with the data (black) published in Patil et al. (2009). Much like in the previous figure, 100 thousand individual village model predictions of the observable clinical incidence in a village (aggregated over 100 runs with 1000 villages each) for varying prevalence levels. These 100 runs scan the biting rate parameter space, increasing the mean biting rate in 1000 village for each run, until a desirable coverage of prevalence values is obtained.

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/51773/elife-51773-fig1-figsupp5-v2.jpg)

**Figure 1—figure supplement 5.:** Shows how the distribution of malaria clinical cases across age bins changes with increasing all-age true prevalence.

![Figure 1—figure supplement 6.](https://cdn.elifesciences.org/articles/51773/elife-51773-fig1-figsupp6-v2.jpg)

**Figure 1—figure supplement 6.:** The black triangles and dots refer to the prevalence measured at baseline and at month 12 post MDA in the MDA trials performed in the Thai-Myanmar border (Landier et al., 2018). We refrained from plotting the data error bars here, since the plot is already quite busy. We simulate a targeted MDA strategy in all similar to the one carried out in the aforementioned study, with a prevalence survey carried out in the year prior to MDA start and another exactly 12 months (M12) after the fist MDA round. The prevalence surveys consist of sampling 50 random individuals from each village and assessing the prevalence assuming a diagnostic sensitivity of 85%. For each village, only the runs in which that village was selected for MDA (having a baseline prevalence over 5%) are used to calculate the mean prevalence at baseline and month 12. Note that these are not meant to be the same villages. The modelled villages are synthetic villages with no relation to or input from the original dataset. The only commonality is that the modelled mean prevalence at baseline in the entire population (also including villages that do not receive MDA) is the same as that in the data (~5%).

Whilst previously published models are extremely good at representing the biological processes underlying malaria transmission, some even making very realistic assumptions on how coverage increases over time (Nikolov et al., 2016), they fail to explicitly model how these interventions are carried out in the field. In practice, teams of workers visit villages sequentially one by one, usually spending 4–7 days to deploy one MDA round in each village, which is quite different from having an unlimited number of teams slowly treating everyone in the target population until a certain coverage is reached. The number of implementation teams is then an input parameter in our simulation platform and each team behaves as an agent. They remain in each village for a fixed period of time (process = 4 days), assumed to be the time needed to complete one round of MDA per village, and move to the next village according to a gravity model. Given a total number of villages V, and a processing time process, the total number of days taken from start of first MDA round in the first village to end of first MDA round in the final village (D) depends on the number of implementing teams (Teams): D = V*process/Teams.

## Results

Initially, we simulated thousands of parameter sets that explore how a wide range of key transmission parameters (e.g. mean initial parasite prevalence, proportion of artemisinin resistant parasites) and logistical constraints – Table 1 – modulate the expected outcome of MDA campaigns. Figure 2 illustrates the sensitivity of the predicted proportional decrease in prevalence over 5 years to each parameter. Clearly, the number of MDA campaigns and the initial mean prevalence across all villages are critical covariates when predicting MDA outcome. The distributions characterizing how malaria risk is distributed over space also seem quite important. Artemisinin resistance spread is very sensitive to those same covariates as well as to the number of intervention teams and the intensity of human population mobility (Figure 2—figure supplements 4 and 5).

![Figure 2.](https://cdn.elifesciences.org/articles/51773/elife-51773-fig2-v2.jpg)

**Figure 2.:** The box plots show the median and interquartile ranges of the proportional reduction in malaria prevalence for all simulated parameter sets. Each parameter set consists of a combination of initial mean prevalence (Prevalence), initial proportion of artemisinin resistance parasites (Resistance), population mobility (Mobility), number of teams deployed in the field (# Teams), number of MDA campaigns (# Campaigns), and number of transmission peaks per year (Seasonality). An overall mean and interquartile range for the effect of transmission heterogeneity, independent of any other parameter, is displayed on the top panel. The reduction in prevalence is evaluated as the proportional difference in the integral in prevalence in the 5 years following MDA relative to the 5 years preceding MDA.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/51773/elife-51773-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Model outcome (measured as the proportional decrease in parasite prevalence) sensitivity to logistical (Teams – speed of coverage, and number of MDA campaigns), epidemiological (initial mean prevalence in the target area, given in black background over each panel), and behavioral (mobility – daily probability of spending nights in a place other than the habitual residence) parameters. Points and adjacent lines indicate the median and interquantile (5th to 95th) ranges (based on 100 simulations for each parameter set).

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/51773/elife-51773-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Intervention outcome sensitivity to spatial transmission heterogeneity in settings with different population mobility patterns. The vectorial capacity distributions associated with these simulations are displayed in Figure 1D. Points and adjacent lines indicate the median and interquartile ranges (based on 100 simulations for each parameter set).

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/51773/elife-51773-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** Model predicted interaction of logistical MDA considerations (speed of coverage – teams) with different population mobility levels (given in black background over each panel) in determining intervention impact for the explored transmission heterogeneity distributions. Points and adjacent lines indicate the median and interquartile ranges (based on 100 simulations for each parameter set).

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/51773/elife-51773-fig2-figsupp4-v2.jpg)

**Figure 2—figure supplement 4.:** In all similar to Figure 2, it shows how the different model parameters modulate the predicted proportional decrease in artemisinin resistance after MDA. Negative numbers then reflect a rise in artemisinin resistant infections from start of the campaign to the end of the simulation (a −100% value indicates a 2-fold increase in the number of resistant parasites).

![Figure 2—figure supplement 5.](https://cdn.elifesciences.org/articles/51773/elife-51773-fig2-figsupp5-v2.jpg)

**Figure 2—figure supplement 5.:** Illustrates how human population mobility (y-axis) interacts with how transmission risk is distributed over space (colored groups) to modulate the extent to which artemisinin resistance is able to spread (x-axis).

**Table 1.**
 Factors explored by the model and their respective sets of values.


<table>
  <thead>
    <tr>
      <th>Factor</th>
      <th>Meaning</th>
      <th>Values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Teams</td>
      <td>Number of teams performing prevalence surveys and distributing ACTs simultaneously. Translated into coverage speed in square brackets, that is, the number of days it takes to perform one MDA round in a region of 1000 villages.</td>
      <td>15 [267] 25 [160] 50 [80] 100 [40] 200 [20] 400 [10]</td>
    </tr>
    <tr>
      <td>Prevalence</td>
      <td>Mean initial malaria u-PCR prevalence across all villages.</td>
      <td>0.5, 0.1, 0.15, 0.2, 0.25, 0.3</td>
    </tr>
    <tr>
      <td>Resistance</td>
      <td>Mean initial proportion of parasites which are artemisinin resistant.</td>
      <td>0.1, 0.2, 0.3</td>
    </tr>
    <tr>
      <td>Distribution</td>
      <td>Transmission heterogeneity distribution, underlying spatial heterogeneity of malaria transmission, manifested by differential mosquito density distributions.</td>
      <td>Gaussian, Log-normal, Pareto</td>
    </tr>
    <tr>
      <td>Mobility</td>
      <td>Describes the intensity of population movement in the general population. Indicates the per person average daily probability of moving to places other than their home village for short-term visits (see Mobility section in the Simulation Protocol). that is a population of individuals whose short-term movement occurs on average 25 times per year (25/365) has a relatively static population with low mobility.</td>
      <td>5/365 25/365 125/365 250/365</td>
    </tr>
    <tr>
      <td>Campaigns</td>
      <td>The number of MDA Campaigns</td>
      <td>1, 2</td>
    </tr>
    <tr>
      <td>Peaks</td>
      <td>The number of annual seasonal peaks</td>
      <td>1, 2</td>
    </tr>
  </tbody>
</table>

We found that there is an intricate relationship between the optimal timing of MDA campaign start, its implementation logistics, and malaria seasonality patterns. Deploying a higher number of MDA teams will yield a higher likelihood of reaching malaria elimination within 2 years, only when population mobility is high – Figure 3. Using a smaller number of intervention teams is predicted to be advantageous in a population of lower mobility, especially when there is only one annual transmission peak and when the MDA start is delayed to day 60 (instead of the default start at the beginning of the calendar year). In settings with 2 malaria seasons per year, the first transmission peak occurs earlier in the year, making the faster 400 team implementation a better option in general. The only exceptions are very static populations in which two MDA campaigns are deployed. We should note that overall, a slower implementation is preferable, especially for the single peak seasonal profiles (Figure 3—figure supplement 1). For the two peak scenarios, a higher number of teams would be beneficial as prevalence increases from 1%. When addressing how to maximize the chances of reaching elimination within a short time span by implementing an MDA strategy, we found that different transmission heterogeneity distributions (depicted in Figure 1D) incur quite different prospects – Figure 4 (Normal), Figure 4—figure supplement 1 (Log-Normal), and Figure 4—figure supplement 2 (Pareto). The likelihood of reaching elimination is strikingly different when comparing the Pareto distribution (most skewed) with the other two (Normal and Log-Normal distributions), except when an extremely efficient vector control program is carried out for a couple of years. Coupling vector control with an MDA campaign vastly improves the chances for elimination across the low prevalence settings explored here, and the longer vector control can be sustained the more likely elimination becomes. Once again, there seems to be a correlation between population mobility and number of MDA teams, with faster MDA implementations being preferred when the human population is more mobile – Figure 4.

![Figure 3.](https://cdn.elifesciences.org/articles/51773/elife-51773-fig3-v2.jpg)

**Figure 3.:** Demonstrates under what conditions using 400 implementation teams is preferable over 15 teams when deploying an MDA campaign. We investigate different epidemiological contexts, characterized by different prevalence and seasonality profiles can be accounted for in deciding the appropriate campaign start day (delay) when maximizing the chances for malaria elimination. ‘MDA (delay)’ means MDA start is delayed to day 60 instead of the default start at the beginning of the calendar year. ‘#Peaks’ indicates the number of transmission peaks per year. The left four columns have 1 peak whereas the right four columns have 2 peaks.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/51773/elife-51773-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Illustrates the interaction between human population mobility, seasonality patterns, and MDA operational parameters (number of teams and campaign start time). Colors indicate the proportion of simulations in which elimination was reached for each parameter combination, evaluated at different time points.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/51773/elife-51773-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** Shows how the relationship between human population mobility (rows), seasonality patterns (blocks of columns), MDA operational parameters – number of teams (block of rows), campaigns and campaign start time (columns) – and selection for the starting villages for MDA (colors) influences the probability of malaria elimination (y-axis).

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/51773/elife-51773-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** Illustrates how a lower infectiousness assumption for asymptomatic malaria (red line) drives the likelihood of malaria elimination up for independently of the remaining model parameters.

![Figure 4.](https://cdn.elifesciences.org/articles/51773/elife-51773-fig4-v2.jpg)

**Figure 4.:** These surface plots show the proportion of simulations (out of 100) in which elimination was achieved within a 5 year time horizon. Hypothetical interventions that decrease the vectorial capacity by a proportion given in the y-axis are maintained for a period of time defined in the x-axis. These transmission blocking interventions are layered on top of a global MDA campaign consisting of 3 ACT rounds in all villages and including widespread village malaria workers. Different panels give different combinations of mean initial malaria prevalence, human population mobility and MDA implementation speed. The white dashed line represents the 80% likelihood of elimination contour line.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/51773/elife-51773-fig4-figsupp1-v2.jpg)

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/51773/elife-51773-fig4-figsupp2-v2.jpg)

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/51773/elife-51773-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** These surface plots show a drastic improvement in transmission reduction impact when comparing implementations of MDA in setting with varying vector control (VC), against VC only intervention strategies. As shown in columns 2, 4, and 6, implementations of strategies including VC alone are unlikely to achieve elimination.

Finally, we explored the value of targeting the top 10 or 20% of villages (sorted by vectorial capacity) and compared its predicted outcome with a full MDA campaign – Figure 5. We confirm that the log-normal and gaussian distributions explored here produce the same elimination likelihood profiles. For very efficacious vector control strategies, the vectorial capacity in the transmission foci will be greatly reduced, causing a greater drop in mean vectorial capacity across all villages in the more skewed distribution (where most villages have negligible numbers or no mosquitoes), compared to the others. This causes the likelihood of elimination in settings with a Pareto distributed risk of infection to be greater on the long-term under those circumstances. Once again, sustaining the vector control for longer, greatly improves the expected outcome (Figure 5—figure supplement 1.

![Figure 5.](https://cdn.elifesciences.org/articles/51773/elife-51773-fig5-v2.jpg)

**Figure 5.:** Illustrates the likelihood of elimination within 5 years of an elimination strategy consisting of 3 MDA rounds and a vector control strategy sustained over 1 year. We compare elimination prospects across different prevalence levels, human population mobility, and transmission heterogeneity over space. Vector control (VC) efficacy refers to the coefficient by which vectorial capacity is reduced for the duration of the intervention. The vector control target sizes refer to the quantile of villages, sorted by descending vectorial capacity, targeted by the intervention.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/51773/elife-51773-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** The same as in Figure 5, except that vector control is extended to last 5 years.

## Discussion

A series of key interacting features of the transmission-intervention system emerge when intricate logistics are incorporated in spatial-temporal transmission dynamics. Mapping MDA campaign expected outcomes to a specific malaria endemic setting is a complex multivariate problem. Here, we elucidate the way in which the most critical interactions determine MDA success:

Although the elucidation of these intricate relationships is of great scientific interest, National Malaria Control Programmes (NMCPs) might find this exploration to be devoid of applicability, specifically those concerned with drug resistance issues. We have demonstrated that more MDA rounds translate into higher likelihoods of malaria elimination but also show how resistance is very likely to increase dramatically if elimination is not achieved. To explicitly inform policy decisions of NMCPs aiming to eliminate P. falciparum malaria in a short time frame, we provide insights into integrated strategies that combine vector control interventions with a minimal number of MDA rounds:

We have refrained from doing a cost-effectiveness analysis, since we do not have enough information on most unit costs, which are currently being assessed in different settings, and are likely to be quite variable across countries in the GMS. Any recommendation and cost-effectiveness analysis would have to be tailored to each specific country/area. We also have not extensively addressed synchronous migration patterns but have included long term and seasonal migration events in the simulation platform. The sensitivity of the model’s predictions to these types of migration is much lower than to the general population’s short-term mobility actions explored to great lengths throughout. This is, in all likelihood, a result of the low proportion of seasonal or long-term migrants in the overall population. In settings where migrants constitute a more considerable (>20%) fraction of the population, the predicted impact might vary. We also considered an uncorrelated uptake of ACT rounds during MDA, meaning there is no relationship between the likelihood of receiving a future ACT round and having received a previous one. This can be an issue in areas where religious and/or cultural beliefs cause individuals to refuse any and all drug treatments, but if that is the case, then it would manifest itself at the time of the prevalence survey, when blood would have to be drawn. In practice, we concede that we may be unable to deploy MDA in whole villages due to these constraints, but in the absence of data we refrain from making any assumptions. For simplicity, we have assumed that asymptomatic and clinical infections are equally infective to mosquitoes throughout. In reality, further empirical studies are greatly needed to better characterise this controversial quantity that bears critical consequences for malaria elimination prospects (Aguas et al., 2018). In Figure 3—figure supplement 3 we demonstrate this critical nature, with malaria elimination becoming more amenable if asymptomatic infections are less infectious. To keep the mosquito population comparable to that in all other simulations shown here, we leverage the biting rate in simulations with lower infectivity of asymptomatic infection to obtain comparable prevalence levels. That means that for a given prevalence value, we took the mosquito density in previous simulations and calibrate the biting rate (proxy for effective number of human/mosquito contacts) needed to obtain the same prevalence at equilibrium when infectivity is lowered. Since the overall infectiousness of asymptomatic infections is decreased, the biting rate will have to increase to reach the same level of prevalence. Therefore, the infection pool will be sustained in a smaller population of mosquitoes which bite humans more frequently to make up for the decrease in human to mosquito infection efficiency. We can then conclude that the true catalyst of malaria elimination is the crash of the infectious population of mosquitoes after MDA, rather than a complete elimination of infections in the human population.

Here, we present a theoretical exploration of the potential impact of MDA strategies in different settings of the GMS, with special emphasis on the sensitivity of the predicted impact to logistical constraints, and transmission or population topologies. The ranges of parameters and distributions explored are meant to represent the current malaria situation in the GMS but need to be adjusted for application to specific areas/countries. In conclusion, we propose that mass drug interventions can be an invaluable tool towards malaria elimination in the right context. The model presented here predicts that an MDA’s success likelihood is bounded by the initial malaria prevalence and we elucidate how those chances can be improved through tailoring of implementation logistics. Although MDA is being revisited by the global community, very little attention has been paid to implementation logistics, and there seems to be no protocol adjustment across settings with completely different seasonality and human mobility patters, thus risking a sub-optimal MDA outcome.

## Materials and methods

We developed an individual based, discrete time, spatially explicit, stochastic model, with mosquito population dynamics and human population movement. The flow diagram in Figure 1A describes the natural history of malaria infection in the human population. Details of how the dynamics of malaria transmission, human mobility and interventions are simulated are provided in the simulation protocol section below. All model parameters are presented in Table 2 along with their respective references when applicable. The simulated synthetic population mimics the demographics of a set of 1000 villages in SE Asia, with the distribution of villages over space, village sizes and age distribution of people likely not applicable to African settings. They should be generic enough to give a fair representation of rural settings in SE Asia. The parameter exploration presented here provides the limits of plausibility in terms of how people are expected to move, the levels of drug resistance and malaria prevalence, and how spatially heterogeneous transmission is.

**Table 2.**
 List of parameters used in the model.


<table>
  <thead>
    <tr>
      <th>#</th>
      <th>Name</th>
      <th>Description</th>
      <th>Value</th>
      <th>Reference</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>V</td>
      <td>Set of villages</td>
      <td>|V| = 1000</td>
      <td></td>
    </tr>
    <tr>
      <td>2</td>
      <td>N</td>
      <td>Set of individuals across all villages</td>
      <td>|N| = 314,795</td>
      <td>-</td>
    </tr>
    <tr>
      <td>3</td>
      <td>ml</td>
      <td>Proportion of males in the population</td>
      <td>0.48</td>
      <td>(National Institute of Statistics, 2008)</td>
    </tr>
    <tr>
      <td>4</td>
      <td>maxage</td>
      <td>Maximum age</td>
      <td>80 years</td>
      <td>-</td>
    </tr>
    <tr>
      <td>5</td>
      <td>beta</td>
      <td>Biting rate</td>
      <td>variable*</td>
      <td>-</td>
    </tr>
    <tr>
      <td>6</td>
      <td>previ</td>
      <td>Initial proportion of infectious people</td>
      <td>variable*</td>
      <td>-</td>
    </tr>
    <tr>
      <td>7</td>
      <td>resit</td>
      <td>Initial proportion of artemisinin resistant infections</td>
      <td>variable*</td>
      <td>-</td>
    </tr>
    <tr>
      <td>8</td>
      <td>netuse</td>
      <td>Proportion of individuals that own an insecticide treated bed net</td>
      <td>0.5</td>
      <td>-</td>
    </tr>
    <tr>
      <td>9</td>
      <td>itneffect</td>
      <td>proportional decrease of individual susceptibility/infectiousness related to ITN usage</td>
      <td>0.2</td>
      <td>-</td>
    </tr>
    <tr>
      <td>10</td>
      <td>ovstay</td>
      <td>Mean number of nights spent somewhere when undertaking short-term population movement</td>
      <td>3</td>
      <td>-</td>
    </tr>
    <tr>
      <td>11</td>
      <td>crit</td>
      <td>Critical distance below which overnight stays somewhere other than your home are made very unlikely</td>
      <td>4 km</td>
      <td>-</td>
    </tr>
    <tr>
      <td>12</td>
      <td>timecomp</td>
      <td>Mean time to complete ACT routine treatment</td>
      <td>4 days</td>
      <td>Best guess</td>
    </tr>
    <tr>
      <td>13</td>
      <td>fullcourse</td>
      <td>Proportion that receives treatment full course</td>
      <td>0.8</td>
      <td>(Yeung et al., 2008)</td>
    </tr>
    <tr>
      <td>14</td>
      <td>covab</td>
      <td>Proportion of symptomatic cases that receive antimalarials</td>
      <td>0.6</td>
      <td>(Yeung et al., 2008)</td>
    </tr>
    <tr>
      <td>15</td>
      <td>nomp</td>
      <td>Relative probability of receiving treatment in a non-malaria post village</td>
      <td>0.1</td>
      <td>Best guess</td>
    </tr>
    <tr>
      <td>16</td>
      <td>asymtreat</td>
      <td>Relative probability of receiving treatment without clinical symptom</td>
      <td>10−4</td>
      <td>-</td>
    </tr>
    <tr>
      <td>17</td>
      <td>tauab</td>
      <td>Daily probability of receiving ACT in a village under MDA</td>
      <td>1/1.5</td>
      <td>-</td>
    </tr>
    <tr>
      <td>18</td>
      <td>gamma</td>
      <td>Mean liver stage duration</td>
      <td>5 days</td>
      <td>(Collins and Jeffery, 1999; Eyles and Young, 1951)</td>
    </tr>
    <tr>
      <td>19</td>
      <td>sigma</td>
      <td>Mean time to infectiousness after liver emergence</td>
      <td>15 days</td>
      <td>(Jeffery and Eyles, 1955)</td>
    </tr>
    <tr>
      <td>20</td>
      <td>mellow</td>
      <td>Mean duration of symptoms</td>
      <td>3 days</td>
      <td>(Church et al., 1997)</td>
    </tr>
    <tr>
      <td>21</td>
      <td>xa0</td>
      <td>Daily probability of going below the minimum effective artemisinin concentration</td>
      <td>1/7</td>
      <td>(Karbwang et al., 1998)</td>
    </tr>
    <tr>
      <td>22</td>
      <td>xai</td>
      <td>Daily probability losing the DHA effect as part of ACT</td>
      <td>1/3</td>
      <td>(Rijken et al., 2011; Tarning et al., 2008)</td>
    </tr>
    <tr>
      <td>23</td>
      <td>xab</td>
      <td>Daily probability of going below the minimum effective piperaquine concentration</td>
      <td>1/30</td>
      <td>(Rijken et al., 2011; Tarning et al., 2008)</td>
    </tr>
    <tr>
      <td>24</td>
      <td>xpr</td>
      <td>Daily probability of going below the minimum effective primaquine concentration</td>
      <td>1/2</td>
      <td>(Burgess and Bray, 1961)</td>
    </tr>
    <tr>
      <td>25</td>
      <td>delta</td>
      <td>Mean duration of a malaria untreated infection</td>
      <td>160 days</td>
      <td>(Eyles and Young, 1951; Babiker et al., 1998; Franks et al., 2001)</td>
    </tr>
    <tr>
      <td>26</td>
      <td>imm_min</td>
      <td>Minimum clinical immunity period</td>
      <td>40 days</td>
      <td>Best guess</td>
    </tr>
    <tr>
      <td>27</td>
      <td>alpha</td>
      <td>Average permanence in each immunity level</td>
      <td>60 days</td>
      <td>-</td>
    </tr>
    <tr>
      <td>28</td>
      <td>phic</td>
      <td>Relative infectiousness of symptomatic infections compared to sub-patent ones</td>
      <td>1</td>
      <td>-</td>
    </tr>
    <tr>
      <td>29</td>
      <td>mdi</td>
      <td>Mosquito daily probability of dying while infectious</td>
      <td>1/7</td>
      <td>(Dawes et al., 2009)</td>
    </tr>
    <tr>
      <td>30</td>
      <td>mdn</td>
      <td>Mosquito daily probability of dying while infected but not yet infectious</td>
      <td>1/20</td>
      <td>(Dawes et al., 2009)</td>
    </tr>
    <tr>
      <td>31</td>
      <td>mgamma</td>
      <td>Mean extrinsic incubation period</td>
      <td>14 days</td>
      <td>(Smith et al., 2014)</td>
    </tr>
    <tr>
      <td>32</td>
      <td>amp</td>
      <td>Amplitude of mosquito density seasonal variation</td>
      <td>0.6</td>
      <td>Best guess</td>
    </tr>
    <tr>
      <td>33</td>
      <td>process</td>
      <td>Days needed to administer a full ACT course in one village</td>
      <td>4 days</td>
      <td>Optimistic guess</td>
    </tr>
    <tr>
      <td>34</td>
      <td>rounds</td>
      <td>Number of drug rounds in an MDA campaign</td>
      <td>3</td>
      <td>Standard practice</td>
    </tr>
    <tr>
      <td>35</td>
      <td>btrounds</td>
      <td>Number of days between drug rounds in an MDA campaign</td>
      <td>32</td>
      <td>Standard practice</td>
    </tr>
    <tr>
      <td>36</td>
      <td>vcefficacy</td>
      <td>Vector control efficacy</td>
      <td>variable*</td>
      <td>-</td>
    </tr>
    <tr>
      <td>37</td>
      <td>cb∙r0∙a</td>
      <td>Daily probability of clearing blood stage drug sensitive parasites with circulating dha</td>
      <td>1/5</td>
      <td>(Adjuik et al., 2004; Pukrittayakamee et al., 2004)</td>
    </tr>
    <tr>
      <td>38</td>
      <td>cb∙ra∙a</td>
      <td>Daily probability of clearing blood stage artemisinin resistant parasites with dha</td>
      <td>0.27*cb∙r0∙a (0.05)</td>
      <td>(Dondorp et al., 2009)</td>
    </tr>
    <tr>
      <td>39</td>
      <td>ci∙r0∙a</td>
      <td>Daily probability of clearing infectious stage drug sensitive parasites with circulating dha</td>
      <td>1/3</td>
      <td>(Adjuik et al., 2004; Pukrittayakamee et al., 2004)</td>
    </tr>
    <tr>
      <td>40</td>
      <td>ci∙ra∙a</td>
      <td>Daily probability of clearing infectious stage artemisinin resistant parasites with dha</td>
      <td>0.27*ci∙r0∙a (0.09)</td>
      <td>(Dondorp et al., 2009)</td>
    </tr>
    <tr>
      <td>41</td>
      <td>cb∙ro∙ab</td>
      <td>Daily probability of clearing blood stage drug sensitive parasites with circulating dha- piperaquine</td>
      <td>1/3</td>
      <td>(Adjuik et al., 2004; Pukrittayakamee et al., 2004)</td>
    </tr>
    <tr>
      <td>42</td>
      <td>cb∙ra∙ab</td>
      <td>Daily probability of clearing blood stage artemisinin resistant parasites with dha- piperaquine</td>
      <td>0.27*cb∙ro∙ab + (1.0–0.27)*cb∙r0∙b (0.33)</td>
      <td>(Dondorp et al., 2009)</td>
    </tr>
    <tr>
      <td>43</td>
      <td>ci∙r0∙ab</td>
      <td>Daily probability of clearing infectious stage drug sensitive parasites with circulating dha- piperaquine</td>
      <td>1/3</td>
      <td>(Bustos et al., 2013)</td>
    </tr>
    <tr>
      <td>44</td>
      <td>ci∙ra∙ab</td>
      <td>Daily probability of clearing infectious stage artemisinin resistant parasites with dha- piperaquine</td>
      <td>0.27*ci∙r0∙ab + (1.0–0.27)*ci∙r0∙b (0.126)</td>
      <td>-</td>
    </tr>
    <tr>
      <td>45</td>
      <td>cb∙r0∙b</td>
      <td>Daily probability of clearing blood stage drug sensitive parasites with circulating piperaquine</td>
      <td>1/3</td>
      <td>(Chen et al., 1982)</td>
    </tr>
    <tr>
      <td>46</td>
      <td>cb∙ra∙b</td>
      <td>Daily probability of clearing blood stage artemisinin resistant parasites with piperaquine</td>
      <td>1/3</td>
      <td>(Chen et al., 1982)</td>
    </tr>
    <tr>
      <td>47</td>
      <td>ci∙r0∙b</td>
      <td>Daily probability of clearing infectious stage drug sensitive parasites with circulating piperaquine</td>
      <td>1/20</td>
      <td>(Myint et al., 2007)</td>
    </tr>
    <tr>
      <td>48</td>
      <td>ci∙ra∙b</td>
      <td>Daily probability of clearing infectious stage artemisinin resistant parasites with piperaquine</td>
      <td>1/20</td>
      <td>(Myint et al., 2007)</td>
    </tr>
    <tr>
      <td>49</td>
      <td>ci∙r0∙p</td>
      <td>Daily probability of clearing infectious stage drug sensitive parasites with primaquine</td>
      <td>1/1.5</td>
      <td>(Burgess and Bray, 1961; Smithuis et al., 2010)</td>
    </tr>
    <tr>
      <td>50</td>
      <td>ci∙ra∙p</td>
      <td>Daily probability of clearing infectious stage artemisinin resistant parasites with primaquine</td>
      <td>1/1.5</td>
      <td>-</td>
    </tr>
    <tr>
      <td>51</td>
      <td>k</td>
      <td>Steepness of susceptibility increase with age</td>
      <td>0.14</td>
      <td>(Aguas et al., 2008)</td>
    </tr>
    <tr>
      <td>52</td>
      <td>r</td>
      <td>Amplitude of susceptibility increase with age</td>
      <td>0.99</td>
      <td>(Aguas et al., 2008)</td>
    </tr>
  </tbody>
</table>

_*the values are varied in different simulation settings. Their values are given in the description of each set of experiments and the set of possible values is given in Table 1._

Spatial demographics for both mosquitoes and humans are implemented at the village level, that is, humans can only move between villages and transmission within each village follows a pseudo-homogenous process where each mosquito is equally likely to bite a given individual. We assume villages are transmission units that encapsulate the village itself and the surrounding farms/forest areas. Whilst clearly a simplification of reality, we know that mosquitoes can easily cover the distance between village and proximal farms over the course of a single day, and most SE-Asian vector species engage in late afternoon biting (some even having a near flat biting rate throughout the day). Given that people tend to move freely within their village during those hours we can reasonably assume that all humans in one village can potentially be bitten by any one mosquito in that village. Having villages as both the transmission and intervention units is obviously computationally convenient, since all model processes related to transmission and intervention can then be evaluated at the same scale.

Malaria transmission in the Greater Mekong Sub-region (GMS) has been reported to be spatially heterogeneous (Gryseels et al., 2015; Cui et al., 2012; Erhart et al., 2005). However, there is very little evidence as to the relative abundance of the main vector species and no quantification of densities exists at a large enough scale. Given the lack of data to inform the discrepancies in mosquito densities across different villages, we chose to explore three mosquito density distributions (Mn, Ml, and Mp). Two of those distributions represent extreme scenarios: one in which all villages have approximately the same biting rate (Gaussian distribution); another where the vast majority has very low biting rates with a few hotspots (Pareto). The third distribution illustrates a scenario possibly more applicable to most areas in which some villages have a quite high transmission intensity, but where most have low mosquito abundance. These distributions were chosen arbitrarily and are parameterised as follows:

$$
Gaussian:Mn~N(0.0172,0.0075)Lognormal:Ml~Logn(\mu, \sigma)\mu=Log(\frac{0.0172^{2}}{\sqrt{(0.0172^{2}+0.0001)}})\sigma=\sqrt{Log(\frac{0.0001}{0.0172^{2}}+1)}ParetoMp~Pareto(0.37,0.0075,0.001)
$$

We take these distributions of mosquito density across villages as reference ($M(t=0)$) and impose some seasonal variation to reflect the observed malaria incidence seasonal patterns. Mosquito density at time t in village j, for all mosquito density distributions is then given by:

$$
M_{i}(t)=M_{i}(0)+amp\timesM_{i}(0)\timescos(2\pi(\frac{t−90}{365})),
$$

where amp reflects the amplitude of the seasonal fluctuation.

Transmission in a given simulation is characterised by a single extra parameter, the mosquito biting rate, which determines the vectorial capacity and is adjusted to reach a specific baseline malaria prevalence in the human population. The mosquito biting rate calibration was performed for each combination of transmission heterogeneity distribution, population mobility intensity and malaria mean prevalence. Thus, for each population mobility and mosquito density distribution, hundreds of model runs were performed until the desired mean malaria prevalence was reached with a specific mosquito biting rate within the first 5 years of simulation.

Population movement patterns and their importance for infectious disease transmission and emergence has recently garnered a lot of increased scientific interest, with new tools and analysis frameworks being developed for mobility inference (Tatem et al., 2014; Tatem et al., 2009). Whilst census data and mobile phone data can help in proposing a connectivity network for a given region, the lack of general precision in questionnaires and the relative difficulty in capturing a lot of outside home overnight stays in mobile phone records, begs for a new source of data to resolve transmission relevant mobility patterns. Spatially explicit malaria models have in so far used gravity models to describe population movement, which is supported by some data (notably, daytime travel data). Whilst we agree that a gravity model can be the most appropriate to describe some seasonal and long-term migration patterns, we argue that overnight stays a very short distance from your home are generally unlikely. It is more likely for someone to return home for the night if they are within a certain critical distance threshold (crit) in km, instead of staying overnight somewhere else. We thus consider that daily population flow (FL_short) between villages i and j is best characterised by a modified gravity model given by:

$$
FL_short_{ij}=FL_{ij}/(1+\frac{1}{1+e^{10\times(disti,j-crit)}})
$$

where FLij refers to the daily population flow of a standard gravity model

$$
FL_{ij}=\frac{pop_{i}\timespop_{j}}{\sqrt{dist(i,j)}}
$$

where pop refers to village population size, and dist to the Euclidean distance (in km) between villages i and j.

The frequency of general population’s short-term movements (very small number of nights spent somewhere other than their own village at a time) is given by the overall population mobility parameter – mobility – which is explored at length in the main text and assumes 2 extreme values (5 and 250 nights spent somewhere other than the home village, per year). The population is further partitioned into temporary (seasonal) or long-term migrant groups. Seasonal migration can only occur during a 3 month period. This roughly corresponds to the duration of crop seasons, at which time people typically go back to their village of origin to help their families harvest crops or for other economic/personal reasons. After 3 months they return to larger villages or surrounding cities following FLij. Long-term migrants only move between a priori defined (at random) economic hubs, comprising 2% of the target villages, spending an average of 6 months in each before moving to the next. For simplicity, we only explore the effects of short-term movements throughout this paper, excluding seasonal and long-term migration events from the simulations presented here. We should note that the sensitivity of the model’s predictions to seasonal and long-term migration is much lower than to the general population short-term movements explored to great lengths throughout this paper. We simulate malaria elimination strategies composed of MDA, a village malaria worker (VMW) network for improved case management, and an annual bed net distribution program. Villages are given an MDA of one full course (3 monthly rounds) of artemisinin combination therapy (ACT) plus one dose of primaquine, irrespective of their illness or infection status. Logistically, intervention teams sweep through all villages and give out ACTs without any prior screening, staying for a given number of days and then moving on to the next village. The details of how implementation logistics were incorporated into the simulation protocol can be found in the Simulation Protocol below.

When exploring the factors driving MDA outcome prediction, we explored all possible combinations of parameter values presented in Table 1, comprising 3888 sets of parameters. The model was run 100 times for each parameter set.

We also explored the layering of further intervention efforts on top of a global MDA initiative (with 3 ACT rounds), such as the implementation of indoor residual spraying (IRS) or larvicidal deployment, for example. Vector control effect size can be modelled as a reduction in vectorial capacity or EIR, as a direct consequence of a decrease in life expectancy, increase in sporogony cycle length and/or decreased biting rate on humans. Depending on what vector control measure one considers and how the mosquito life cycle is modelled, there might be interest in detailing the impact of a vector control intervention on a particular aspect of the mosquito life cycle. That is beyond the scope of what is intended in this paper, and we present vector control effect size as a measure of how much vectorial capacity is decreased when vector control interventions are in place. Thus, a transmission reduction efficacy of 0.10 means that the implemented vector control strategy reduces the number of infectious bites per person per year by 10%. Whilst MDA is programmatically well defined, with a specific number of ACT rounds being deployed, it is less clear how vector control strategies are sustained over time. Thus, we ran simulations for a range of vector control efficacy/duration of intervention pairs and evaluated the proportion of simulations in which elimination is reached.

### Simulation protocol

In this section, we give detailed description of the agent-based malaria simulation model results from which were discussed in the main text. We start by defining the interacting agents and their properties in the next section. Model processes and functions executed during the simulation are then documented in another two sections according to their positions in the simulation sequence.

#### Agents

The simulation model presented here is a multi-level agent-based model containing three interconnected groups of agents: Villages, Humans and Mosquitoes. Each agent has group-specific properties:

#### Villages

#### Humans

#### Mosquitoes

### Model set-up

To explore the effect of malaria interventions using dynamic transmission models, one usually assures that the model is run until an equilibrium is reached (thus establishing a control scenario), and then implements whatever the intervention of interest is. The intervention’s outcome or effectiveness can then be derived from a direct comparison between the integral of the control scenario and that of the intervention scenario over the same time period. Throughout the manuscript we present simulations for settings of a specific malaria prevalence. That value is the mean malaria prevalence over the last year of a 200 year run of a control scenario. To calibrate model runs to a specific prevalence we vary a free parameter beta [5], the mosquito biting rate, whilst keeping all other parameters fixed.

From the end of each successful calibration run to a given prevalence, we extract individual level information to inform the age, immunity level, number of cumulative infections, and infection status of each individual. This information forms a human input file used for model initialisation in the runs where intervention is simulated. The calibrated vectorial capacity distributions used in the calibrated runs are added to a village input file containing village location and population size and is also used for model initialisation.

More specifically, the following processes are involved in setting up the human population and village properties at the start of the 200 year prevalence calibration runs:

### Human properties

#### Gender and age

Age and gender information of human agents are generated according to parameterised distributions. The probability of a human agent being male is ml [3]. The age of a human is sampled from a discrete distribution specified by a vector of size maxage [4]. This vector is given by a csv file with maxage [4] integers, containing a discrete age profile taken from Cambodian census data.

#### Prevalence

The probability of a human agent being infectious is previ [6], and the probability of that infection being resistant to artemisinin is resit [7].

#### ITN usage

Each human agent is assigned with an ITN with a probability of netuse [8]. Ownership of an ITN reduces the human agent’s susceptibility/infectivity by itneffect [9]. Note that ITN distribution is not explored further in the model runs contained here. If that were a consideration, then the control scenarios would have both netuse and itneffect at their minimum acceptable values.

#### Immunity

Each human agent is assigned two properties in relation to immunity, namely Cumulative Number of Exposures and Immunity Level. Both properties are set to 0 for newborns. The likelihood of clinical symptoms brought on by a single infection is given by

$$
clinical_prob_{n}=e^{(-0.15\times(moi_{n}-1))}\times\frac{0.1\timese^{-(cml_{n}-2)\times0.1}+e^{-0.9\timescml_{n}}}{lvl_{n}^{0.5}}
$$

where moi, cml and lvl denote the multiplicity of infection, cumulative exposure to malaria and immunity level properties of the human agent respectively. Although we only increase immunity level if individuals resolve their infection (presumably due to increased antibodies killing activity), the cumulative exposure is updated with each infectious bite received. Thus, individuals can accrue some immunity with superinfections.

### Village properties

#### Mobility network

Geo-spatial human mobility amongst the population is a key element simulated in our model. Using the location and population information provided for each village, a complete graph ($FL$) is constructed linking all villages during initialisation. Let $M$ denote the set of villages in the simulation, $FL$ is constructed using a generic gravity model, with each edge denoting the flow of human movements between village $i,j\inV$ as

$$
FL_{ij}=\frac{pop_{i}\timespop_{j}}{\sqrt{dist(i,j)}}
$$

where $pop_{i}$ denotes the population of village $i$, and $disti,j$ denotes the earth-surface distance between $i$ and $j$.

#### Mosquito density

Each village has a property describing the number of mosquitoes per person. At model setup, each village is assigned a mosquito density by randomly sampling from the distribution describing the spatial heterogeneity in risk used for a particular model run. Given the lack of data to inform these distributions, we chose to explore three different ones (Mn, Ml, and Mp). Two of those distributions represent extreme scenarios: one in which all villages have approximately the same biting rate (Gaussian); another where the vast majority have very low biting rates with only a few hotspots (Pareto). The third distribution (Lognormal) illustrates an intermediate scenario in which some villages have a quite high transmission intensity, but where most have low mosquito abundance. These distributions were chosen arbitrarily and are parameterised as follows:

$$
Gaussian:Mn∼N(0.0172,0.0075)
$$



$$
Lognormal:Ml∼Logn(\mu,\sigma)
$$



$$
\mu=Log⟮\frac{0.0172^{2}}{\sqrt{(0.0172^{2}+0.0001)}}⟯
$$



$$
\sigma=\sqrt{Log⟮\frac{0.0001}{0.0172^{2}}+1⟯}
$$



$$
Pareto:Mp∼Pareto(0.37,0.0075,0.001)
$$

We take these distributions of mosquito density across villages as reference ($M(t=0)$) and impose some seasonal variation to reflect the observed malaria incidence seasonal patterns (described below).

For simplicity, we chose not to create infectious mosquitoes during model set-up. This is essentially due to the extremely fast timeframes of life events in mosquitoes compared to humans. The mosquito infection prevalence reaches equilibrium in a matter of days and thus its initialisation to non-zero values bears a negligible benefit. We use a free parameter beta [5], the mosquito biting rate, to calibrate each simulation to the desired malaria prevalence. Biting rates are calibrated for each combination of mobility, transmission distribution, and prevalence to ensure the system is at equilibrium.

### Model initialisation

The developed malaria micro-simulation platform takes inputs from two CSV-formatted input files and a JSON-formatted configuration file. The two input files provide the model with a list of villages and a list of humans respectively. Each row in these files describes the properties (as listed in the previous section) of either a village or a human agent. Model-wide and process-specific, as opposed to agent-specific, parameters are given by the configuration file. Most parameters specified in Table 2 of the main text are associated with processes and functions (rather than individual agents), and therefore are given by the configuration file. In this section, we use the numbers in square brackets to refer to the associated parameter number whose description and value can be found in Table 2.

The initialisation process starts by processing the configuration file where the location of the input files is stored. Then a list of village agents and a list of human agents are created according to information given in the input files. Human agents are randomly assigned a home village from a list of all possible villages. Once all agents have been created, the software initialises the parameterised functions of the model using the information given in the rest of the configuration file.

### Implementation of malaria relevant dynamics

Once initialisation finishes, the main body of the model simulation starts. We assume time zero to be the 1st of January 5 years prior to the first malaria post establishment/MDA initiation.

The simulation protocols detailed in this section illustrate the flow of events and processes taking place each day. Each process has a daily probability of occurrence. For each individual and for every simulated daily time step, a uniform random number is drawn between 0 and 1 for each possible and valid (according to the individual’s status) transition process (e.g. whether the individual dies, is infected, is treated, etc) associated with that individual. The transition process occurs if and only if the number drawn is lower than its daily probability of occurrence. Note that not all events are valid to an individual given its status on a given day. For instance, a clinical resolution event is not valid to an individual until that individual develops clinical symptoms.

### Human population dynamics

#### Birth and death

The age profile presented here are taken from Cambodia census data. When we initialize individuals in the model and assign them a random age given the age frequencies in the data (through representative sampling), and run that model for 200 years, whilst assuming that individuals have a life expectancy of 1/mu, we end up with a different age profile from the one we started with. That means an adjustment in life expectancy is needed to reflect differences in mortality rates across ages. To that end, we fit the data age profile to an 8th order polynomial function, which we normalised to obtain representation weights for each age, w(a). We then calculate the death probability of individual n of age a as:

$$
death_prob_{n}a=\frac{1}{80-a}w(a)
$$

Whilst this provided a large improvement is the long-term age profiles produced by the model, we still good not replicate the flattening around age 30. Research into the census data for LMICs revealed that there is a significant drop in life expectancy in teenager and young adults, presumably due to involvement in higher risk activities. We explored several age range mortality modifiers and found that the data is best fit when multiplying $w(a_{15-25})$ by 4.

When a death event happens, a new infant agent is generated as a replacement. The new agent is placed in the same village where the death took place to keep population size constant, and all its immunity and exposure related parameters reset.

#### Mobility

Every human agent can display short-term mobility patterns, characterised by overnight stays in villages other than their home for a mean period of ovstay [10] days. For every agent who is currently located at their home village, the daily probability of such short-term movement is given by the factor Mobility in Table 1. Thus, the number of human agents embarking on short-term movement on a given day is

$$
N_{move}~B(N_{home},Mobility)
$$

The destination of each agent’s movement varies and is determined using the mobility network $FL$ constructed during initialisation. Let the flow of short-term movement between village $i,j\inV$ be

$$
FL_short_{ij}=FL_{ij}/(1+\frac{1}{1+e^{10\times(disti,j-crit)}})
$$

where crit [11] denotes the critical distance below which overnight stays at a village other than home are made very unlikely. The probability of a human agent to move from $home$ to village $j$ is

$$
short_move_prob_{home,j}=FL_short_{home,j}/\sumv\inVFL_short_{home,v}
$$

#### Clinical outcome

The likelihood of clinical symptoms brought on by a single infection is given by

$$
clinical_prob_{n}=e^{(-0.15\times(moi_{n}-1))}\times\frac{0.1\timese^{-(cml_{n}-2)\times0.1}+e^{-0.9\timescml_{n}}}{lvl_{n}^{0.5}}
$$

where moi, cml and lvl denote the multiplicity of infection, cumulative exposure to malaria and immunity level properties of the human agent respectively.

#### Treatment

The probability for a human agent to receive a full course of ACT treatment is dependent on symptomatology as well as the presence of a local malaria post. In a village with a malaria post, a human agent with clinical symptom would receive treatment with probability

$$
treatment_prob_mp_clinical=\frac{1}{timecomp}\timesfullcourse\timescovab
$$

where timecomp [12], fullcourse [13] and covab [14] are described in Table 2. In a village with no malaria worker presence, this treatment probability is reduced by nomp [15]. Treatment rates of asymptomatic human agent is negligible as treatment is conditional on a positive RDT, which is very unlikely in sub-patent infections. The probability of a human agent with asymptomatic infection getting treatment is given by asymtreat [16]. The assumed figure of 60% treatment coverage may seem low but it was the coverage reported in a very comprehensive study designed specifically to evaluate access to treatment in remote areas covered by the Cambodian village malaria worker network and/or malaria outreach teams (Yeung et al., 2008) Nevertheless, in Cambodia, the Thai-Myanmar border and other areas of Myanmar (Landier et al., 2018) there has been a substantial decrease in incidence over the past 5 years, mostly due to better clinical case management. The model presented here does predict a substantial effect size on prevalence when village malaria posts are open for this low of a coverage value (~20% decrease for starting prevalence of 5%).

In a village under MDA, the daily probability for a human agent to receive a round of ACT treatment is tauab [17].

#### Intrinsic incubation

Parasites emerge from the liver at a rate of 1/gamma [18], thus the liver stage takes on average gamma [18] days to complete.

#### Gametocytaemia

Parasites start reproducing sexually, and thus generating gametocytes with 1/sigma [19] daily probability.

#### Clinical resolution

Malaria induced fevers gradually recede at a rate of 1/mellow [20], meaning that a person is feverish for mellow [25] days on average.

#### PK/PD

We describe waning drug efficacy over time through explicit daily probabilities of drug effect loss. Upon receiving treatment (with DHA-pip), each human agent will gradually lose the effect of both DHA and Piperaquine, according to xai [22] and xab [23] respectively. The single remaining drug will be lost at rates xa0 [21] and xab [23] for Artesunate and Piperaquine respectively. Single dose Primaquine is lost at rate xpr [24].

Parasite killing rates depend on the person’s transmission status ($s\in{blood,infectious}$), with parasite clearance in not yet infectious people generally slower than that in individuals carrying gametocytes. Clearance of parasites with drug resistance phenotype $h$ by drug $d$ then follows

$$
Clearance_{s∙h∙d}~B(N_{s∙h∙d},c_{s∙h∙d})
$$

where $c_{s∙h∙d}$ is an element of a 3-dimensional drug clearance rate matrix $C$ of size $|S|\times|H|\times|D|$. Values of the elements of $C$ are given by parameters [37-50] in Table 2. $B$ denotes a binomial distribution.

#### Recovery

Each infection in a human agent’s infection list has a daily probability of being naturally cleared given by 1/delta [25].

#### Immunity

One level of clinical immunity is gained by a human agent every time his infection list is emptied. Immunity loss starts imm_min [26] days after one level of immunity is gained. Immunity is lost at a rate of 1/alpha [27]. Therefore, each human agent is clinically immune an average of imm_min [26] + alpha [27] days. A loss in immunity prompts a reduction in immunity level and not the immune status per se.

#### Susceptibility/Infectiousness

Susceptibility was implemented as being age dependent and be modulated by ITN usage. Each individual’s baseline susceptibility increases during the first years of life, saturating at around age 10 (Smith et al., 2004). We define the susceptibility of individuals with age a to a mosquito bite as:

$$
\deltaa=1-r*exp(-k*a));
$$

If someone sleeps under a bed net, their susceptibility to receive an infectious mosquito bite is reduced by itneffect [9]. Individuals sleeping under a bed net are also less infectious compared to people that don’t.

Clinical status modulates infectiousness through phic [28], which determines the relative infectiousness of clinical malaria infections compared to sub-patent ones (here assumed to be 1). We recently published a paper stressing the need for further empirical studies to better characterise this critical but very controversial quantity (Aguas et al., 2018), where we demonstrate how the relative infectivity of chronic infections has severe consequences for malaria elimination prospects.

#### Infection

Given the time dependent vectorial capacity of each village, we can extrapolate the number of mosquito bites landed on humans each day. We exclude all bites from non-infectious mosquitoes. Infectious bites are distributed across humans according to a Gaussian distribution of mean of 1 and a standard deviation of 0.5, reflecting how some individuals are more likely to be bitten than others. This is done through proportional sampling. For each infectious bite, the probability of causing a new infection in a human agent $n$ is given by

$$
Infection_{n}~B(1,susceptibility_{n})
$$

A resulting infection is then added to the human agent’s infection list and inherits the drug resistance phenotype of the infecting mosquito. The number of that agent’s cumulative number of exposures and multiplicity of infection is adjusted accordingly.

### Mosquito dynamics

Note that only infected and infectious mosquito agents exist in our model.

#### Survival

We assume adult female mosquito’s life expectancy to be 1/mdi [29] + 1/mdn [30] days on average. Meaning for each mosquito agent, its daily probability of dying while infectious is 1/mdi [29], and 1/mdn [30] while infected but not infectious.

#### Extrinsic incubation

Parasite development in mosquitoes takes an average of mgamma [31] days. Meaning for a mosquito agent, it takes mgamma [31] days from gametocyte infection to having sporozoites in the salivary glands and thus becoming infectious to humans.

#### Seasonality

Mosquito density at time $t$ in village $i$, for all mosquito density distributions follows an annual seasonal cycle given by

$$
M_{i}t=M_{i}0+amp\timesM_{i}0\timescos⁡(2\pi(\frac{t-90}{365}))
$$

when only 1 seasonal peak is modelled in a year, and

$$
M_{i}t=M_{i}0+amp\timesM_{i}0\timescos⁡(4\pi(\frac{t-40}{365}))
$$

when 2 seasonal peaks are modelled in one year, with amp [32] denoting the amplitude of the seasonal variation of mosquito density.

#### Infection

Given the time dependent vectorial capacity for each village, we can easily extrapolate the number of mosquito bites landed on humans each day. For all bites handed out by mosquitoes that land on infectious humans we generate a new infection in the corresponding mosquito with the same resistant phenotype as a randomly sampled infection in the human’s infected list. There is no limit as to the number of infections a given mosquito can acquire during its lifetime. Their adult survivorship is quite limited though, with only 26% of female mosquitoes having more than one infection at the time of death. That number drops to ~ 14% for values of prevalence amenable to elimination. Note that on a daily basis, the set of humans a mosquito can bite is assessed, based on the human movement across villages. If a human spends a night in village A, they are included in the set of possible humans bitten by mosquitoes in that village, even though that person might live in village B.

### Interventions

#### Malaria post

Malaria posts are established over time by placing a village malaria worker upon MDA initiation in each village. The presence of a malaria post improves the access to treatment as mentioned in the Human treatment section above.

#### MDA

In order to coordinate MDA teams to visit all villages without overlapping and repetition, a complete graph $VG$ connecting all villages to each other is first constructed. The weight of the edge between village $i$ and $j$ is given by $dist(i,j)$. This complete graph $VG$ is then reduced to its minimum spanning tree form, denoted $MST(VG)$, which we use to represent the road network connecting all villages.

Given that the MDA campaign includes $T$ teams (Table 1), $T$ starting locations are randomly selected from the nodes/villages of $MST(VG)$. Then, $T$ breadth-first-search algorithms are started from each of the $T$ starting locations. These search algorithms run simultaneously in coordinated rounds. Each round, an algorithm proposes the next village to be visited. Villages are added to the path of the algorithm which reaches it first. When an algorithm reaches a village that has been added/visited to the path of another algorithm, it continues searching until it finds an un-visited village in the same round. Once all villages have been visited, all algorithms stop. Each algorithm’s path is used as the sequence of villages to be visited by each of the $T$ MDA teams.

An MDA team stays in a village for process [33] days for each one of the rounds [34] number of ACT courses administered. There are btrounds [35] days between drug rounds.

#### Vector Control and targeted Vector Control

Each village’s mosquito density is reduced by 1-vcefficacy [36] during vector control. During a targeted vector control campaign, only a selected subset of villages’ mosquito density property is reduced.

### Model Calibration

The simulated synthetic population mimics the demographics of a set of 1000 villages in SE Asia. Whilst not using data from real villages, some properties describing the demographic fabric of the synthetic population are taken from SE Asian settings. Notably, the distribution of village population sizes and the shape of Euclidean distance network used to determine human population mobility are informed by data from the Thai-Myanmar border, whilst the age profile is extracted from the Cambodian population census. The population demographics simulated here should be generic enough to give a fair representation of rural settings in SE Asia but are not necessarily applicable to African settings.

To ensure the simulation platform produces outcomes that represent reasonable falciparum malaria transmission dynamics, we performed several model calibrations using malaria metadata. By doing so, we safeguard the generalizability of the results presented in the paper as well as the applicability of the model to any specific setting moving forward. The mentioned meta datasets describe fundamental relationships between malariometric indices measured in as many different endemic settings as possible.

A preliminary model calibration done independently of this work, allowed the estimation of an age-dependent force of infection function. Using data from 8 endemic countries in sub-Saharan Africa, we were able to estimate how age modulates the risk of infection during the first years of life, saturating at around age 10 (Aguas et al., 2008). The susceptibility of individuals with age a to a mosquito bite is then given by:

$$
\deltaa=1-r*exp(-k*a));
$$

Where k [51] determines how steeply susceptibility increases with age, and r [52] controls the amplitude of that increase. Given that this relationship is primarily the result of an increasing body weight and surface with age (Smith et al., 2004), and secondarily with the potentially increased protection conferred to infants and small children, we believe it is transferable to any other setting.

An initial model calibration was carried out to better characterise how immunity is developed over age, which remains a contentious and unresolved issue in falciparum malaria. To do so we use a dataset of immunity markers collected in 4 Cambodian sites, that describes seroconversion rates over time and extrapolates age profiles of clinical immunity (Cook et al., 2012). It is important to define what measured immunity means in this context. The data presents percent positivity of each collected specimen (hence single individual) as that defined by a cut-off of the mean optical density of the seronegative population plus three standard deviations (Corran et al., 2008). More importantly, this refers to measured MSP-119 antibodies which have demonstrated a significant association with a decrease in clinical falciparum malaria incidence (Fowkes et al., 2010), and display a very strong linear correlation with EIR (R2 = 0.78) (Corran et al., 2007). Critically, a 15% reduction in symptomatic P. falciparum per doubling of antibody levels was observed (Fowkes et al., 2010), thus painting a picture of piecemeal acquisition of clinical immunity over age, and explaining the quasi-linear relationship with EIR. We take the seroconversion rates reported in this paper as the probability of immune positivity and translate that into a probability function governing the likelihood that a newly infected person of a given age will eventually develop clinical symptoms and thus account for a new clinical malaria case. We then calibrate our model to the prevalence metrics reported for each setting and output the age, number of cumulative infections and immunity level of each person at the last timestep of the model. If we define the probability of clinical outcome as:

$$
probclin=(imm_a*exp(-0.1(cml-1))+exp(-imm_b*(cml+1)))/sqrt(lvl);
$$

we can then jointly estimate the set of parameters $\theta={imm_a,imm_b}$, that minimise the difference between the mean probability of clinical symptoms derived from the mean number of cumulative infections (cml) and mean immunity level (lvl) for each age category in the model output for each prevalence, and the measured probability of immunity (Pi). We thus minimise the following objective function:

$$
f(\theta)=\sumi\sqrt{(probclin(i)-Pi(i))^{2}}
$$

where i are the ages in the dataset.

The resulting estimates of imm_a (0.5631 [0.4201–0.7061]) and imm_b (0.9652 [0.4976–1.433]) determine the shape of the probability of developing clinical symptoms relative to previous exposure as is depicted in Figure 1C of the main text. The model adjustment to the data can be visualised in Figure 1—figure supplement 2.

The second calibration performed was to the relationship between entomological inoculation rate (EIR) and falciparum malaria prevalence. The data shows a non-linear relationship between EIR and Pf prevalence measured by microscopy (Guerra et al., 2007) in over 90 endemic countries, that suggests a marked heterogeneity in individual infection risk (Smith et al., 2005). The relationship produced by the model described here is compared with the data in Figure 1—figure supplement 3. For a direct comparison with the data, we had to convert the prevalence obtained from the model (Pm) to a metric akin to the one obtained when using microscopy for diagnosis (Pd). We assume that an model equivalent of Pd can be derived from: Pm = sPd + sp(1 − Pd), thus correcting for microscopy’s sensitivity (s) and specificity (sp). We assumed these to be 85% and 96%, respectively. Note that the model was not fit to the data. Rather, 1000 simulations were run using different mosquito biting rates (and thus EIR) and susceptibility distributions but keeping all other parameters (as defined here) fixed, and their outputs plotted against the data. Here we present model calibrations using a Gaussian bite receptivity distribution with mean of 1 and a standard deviation of 0.5 (See Infection section for more details). Note that the Pareto distribution for vector density across villages (blue dots) replicates the observed prevalence variance for a fixed EIR value much better than the Gaussian equivalent (red dots).

We opted to plot a point per village for each simulation, to try to reproduce the variance observed in the real data, instead of plotting a single median prevalence value per EIR. This enables us to explore how the relationship between EIR and prevalence can be modulated by factors such as the existence of a village malaria worker, or proximity to a high/low incidence village.

The third calibration assessed the relationship between Pf prevalence and clinical case incidence. This calibration is done to the subset of SE-Asian datapoints contained in the dataset published in Patil et al. (2009) and assumes the same relationship between true and measured prevalence as stated above. The incidence reported here is interpreted as the number of people with a febrile illness testing positive for P. falciparum independently of aetiology. We thus include a term (asymtreat [16]) to describe the proportion of malaria asymptomatic infections in the model outcome that might test Pf positive and have a concurrent fever of another aetiology, to adjust the model to the data. Here we present a calibrated model output assuming asymtreat = 10−4 (Figure 1—figure supplement 4).

The fourth model calibration is done in the absence of data, since we don’t have access to a sufficiently detailed dataset to inform the relationship between age and prevalence in SE-Asia. Instead, we present the patterns generated by our model and compare them with outputs from other models where a rigorous fitting procedure to such data was performed (Griffin et al., 2014). Figure 1—figure supplement 5 summarises how clinical cases are distributed across 4 age ranges according to prevalence.

Lastly, to assess the realism of the MDA implementations simulated throughout, we compare the predicted model outcomes after MDA, with those obtained in the MDA trials performed in the Thai-Myanmar border. We extracted the data on baseline and post MDA prevalence from a supplementary figure in Landier et al. (2018). The model comparators are medians and percentiles of the prevalence in specific villages across one hundred simulations. The model was set up such that MDA would be done focally, that is, only villages with a prevalence over a certain threshold (5%) were eligible to receive an MDA. As per the trial protocol, during the year prior to MDA programme rollout, all 1000 villages were surveyed to establish a baseline prevalence. These surveys consisted of sampling 50 individuals from each village and perform a uPCR to determine their infection status. Here we assume that uPCR can detect 85% of all infections. Once a list of villages eligible to receive MDA is compiled, the model proceeds to compile a schedule for each village to be visited by an intervention team. This process is repeated 100 times, and for each village only the runs in which that village was selected for MDA are used to calculate the summary statistics. A comparison of the model’s output with the empirical trial is presented in Figure 1—figure supplement 6.
