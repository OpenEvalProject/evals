# The effect of climate change on yellow fever disease burden in Africa

## Authors

- Katy AM Gaythorpe<sup>1</sup> ([ORCID: 0000-0003-3734-9081](https://orcid.org/0000-0003-3734-9081)) †
- Arran Hamlet<sup>1</sup>
- Laurence Cibrelus<sup>2</sup>
- Tini Garske<sup>1</sup>
- Neil M Ferguson<sup>1</sup>

### Affiliations

1. Imperial College London London United Kingdom
2. World Health Organisation Geneva Switzerland

† Corresponding author

## Abstract

Yellow Fever (YF) is an arbovirus endemic in tropical regions of South America and Africa and it is estimated to cause 78,000 deaths a year in Africa alone. Climate change may have substantial effects on the transmission of YF and we present the first analysis of the potential impact on disease burden. We extend an existing model of YF transmission to account for rainfall and a temperature suitability index and project transmission intensity across the African endemic region in the context of four climate change scenarios. We use these transmission projections to assess the change in burden in 2050 and 2070. We find disease burden changes heterogeneously across the region. In the least severe scenario, we find a 93.0%[95%CI(92.7, 93.2%)] chance that annual deaths will increase in 2050. This change in epidemiology will complicate future control efforts. Thus, we may need to consider the effect of changing climatic variables on future intervention strategies.

## Introduction

Yellow Fever (YF) is a vaccine preventable, zoonotic, arbovirus endemic in tropical regions of Africa and Latin America. It is responsible for approximately 78,000 deaths per year, although under reporting is high and since YF has a non-specific symptom set, misdiagnosis is an issue (Garske et al., 2014). YF has three transmission ‘cycles’ in Africa: urban, zoonotic and intermediate. The urban cycle, mediated by Aedes Aegypti mosquitoes, is responsible for explosive outbreaks such as the one seen in Angola in 2016 (Ingelbeen et al., 2018; Wilder-Smith and Monath, 2017).

While the urban cycle can rapidly amplify transmission, the majority of YF infections are thought to occur as a result of zoonotic spillover from the sylvatic reservoir in non-human primates (NHP). This zoonotic cycle is mediated by a variety of mosquito vectors including Aedes africanus and, as the NHP hosts are mostly unaffected by the infection in Africa, the force of infection due to spillover is fairly constant, although land use change has been shown to affect this (Monath and Vasconcelos, 2015). The intermediate cycle is sometimes called the savannah cycle and is mediated by mosquitoes such as Ae. luteocephalus, who feed opportunistically on humans and NHP, although human-human transmission is limited (Barrett and Higgs, 2007).

The Intergovernmental Panel on Climate Change (IPCC) states that global mean temperatures are likely to rise by 1.5°C, compared with pre-industrial levels, by between 2030 and 2052 if current trends continue (Masson-Delmotte et al., 2018). Increases are projected not only in mean temperature but also in the extremes of temperature, extremes of precipitation and the probability of drought (Kharin et al., 2013; Dunning et al., 2018).

With multiple mosquito vectors and a zoonotic cycle depending on NHP hosts, the impact of climate change on YF is likely to be complex. Focusing on the main urban vector, A. aegypti, there is strong evidence that projected climate change will alter its global distribution and thus, the risk of diseases it carries (Ryan et al., 2019; World Health Organisation, 2018; World Health Organisation, 2018). Climate change has been predicted to increase the regions at risk from dengue and Zika transmission, although seasonal variation in temperature may mitigate the likelihood of outbreaks in areas at the edges of the endemic zone (Mordecai et al., 2017; Huber et al., 2018).

Long-term projections of the future disease burden of YF are needed to inform vaccination planning (VIMC, 2019). Furthermore, differences due to climate change may increase the risk of epidemics, a key consideration for the Eliminate YF Epidemics (EYE) strategy (World Health Organization, 2017).

In this manuscript, we extend an existing model of YF occurrence and disease burden to incorporate a nonlinear temperature suitability metric (Garske et al., 2014). We estimate temperature suitability for YF based on the thermal response of the urban vector, Ae. aegypti, and the YF virus. We combine this with YF occurrence data in a Bayesian hierarchical model in order to account for uncertainty at each stage of the modelling process. This, along with established estimates of transmission intensity informed by serological survey data, allow us to predict current and future transmission intensity. Finally, we use ensemble climate model predictions of future temperature and precipitation to project transmission and thus, burden in 2050 and 2070. Our results are the first examination of YF burden under the potential future effect of climate change.

## Results

As we estimate a static force of infection, we focus on transmission as a result of sylvatic spillover rather than including the urban transmission cycle explicitly. As such, the results can be considered the estimated effect of climate change on sylvatic transmission and resulting burden.

### Model predictions for baseline scenario

Figure 1 (left) shows occurrence of YF across Africa from 1984 to 2018. Incidence is focused in the West of Africa and, more recently, Angola and the Democratic Republic of the Congo. The model predicts a high probability of YF report in these areas and reflects the general patterns of YF occurrence, see Figure 1 for comparison. Model fit can be characterised by the Area Under the Curve (AUC) statistic (Huang and Ling, 2005), which was 0.9004, similar to the original model formulation of Garske et al., 2014.

![Figure 1.](https://cdn.elifesciences.org/articles/55619/elife-55619-fig1-v1.jpg)

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/55619/elife-55619-fig1-figsupp1-v1.jpg)

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/55619/elife-55619-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** In each survey, 100 samples for force of infection are compared.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/55619/elife-55619-fig1-figsupp3-v1.jpg)

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/55619/elife-55619-fig1-figsupp4-v1.jpg)

The predicted probability of a YF report is positively informed by temperature suitability with the median posterior predicted distribution shown in Figure 2 (left). This highlights the high suitability of countries such as Nigeria and South Sudan for YF transmission. In contrast, Rwanda, Burundi and areas of Mali and Mauritania have low average temperature suitability. The fit of the thermal response models is shown in Figure 2—figure supplements 1–4.

![Figure 2.](https://cdn.elifesciences.org/articles/55619/elife-55619-fig2-v1.jpg)

**Figure 2.:** (Left) Median posterior predicted temperature suitability for the African endemic region with average temperature. (Right) Median predicted FOI for the African endemic region at baseline.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/55619/elife-55619-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** Data is shown with red dots and posterior model samples are shown in grey with the black line indicating median predicted bite rate given temperature in °C. The bite rate of Aedes aegypti mosquitoes is informed by two data sets, that of Mordecai et al. and Martens et al.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/55619/elife-55619-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** Data is shown with red dots and posterior model samples are shown in grey with the black line indicating median predicted bite rate given temperature in °C. The data was collected experimentally in Tesla et al.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/55619/elife-55619-fig2-figsupp3-v1.jpg)

**Figure 2—figure supplement 3.:** Data is shown with red dots and posterior model samples are shown in grey with the black line indicating median predicted bite rate given temperature in °C. This is estimated using data from Davis which was calculated specifically for yellow fever in Aedes aegypti. The prediction of the median incubation period at 25°C is in line with that of Johansson et al., 2010 who found it to be 10 days [2.0 - 37] days.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/55619/elife-55619-fig2-figsupp4-v1.jpg)

**Figure 2—figure supplement 4.:** Data is shown with red dots and posterior model samples are shown in grey with the black line indicating median predicted bite rate given temperature in °C. The model is also informed by the YF occurrence data within the Bayesian hierarchical framework.

### Projected transmission intensity

Figure 2 (right) shows the median posterior predicted estimates of the force of infection for the baseline/current scenario, a comparison of the force of infection estimated only from serological studies, and those estimated from the GLM is provided in Figure 2—figure supplement 1. When we incorporate the ensemble projections of temperature and precipitation change we see heterogeneous impacts on force of infection. Figure 3 shows the percentage change in median force of infection for the year 2070. Projections for 2050 are shown in Figure 3—figure supplement 1.

![Figure 3.](https://cdn.elifesciences.org/articles/55619/elife-55619-fig3-v1.jpg)

**Figure 3.:** Median predicted change in force of infection in the African endemic region in 2070 for the four emission scenarios.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/55619/elife-55619-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** Median predicted change in FOI in African endemic region in 2050 for the four emission scenarios.

The posterior distributions of predicted changes in force of infection in different African regions are shown in Figure 4 (region definitions shown in Figure 4—figure supplement 1). Projections for individual countries are given in the Appedix. In West Africa, the predicted change is clustered around zero in the majority of scenarios; this is particularly the case for year 2050. However, due to wider uncertainty in 2070 and for RCP scenario 8.5 in general, there is a more discernible increase. In the East and Central regions, a predicted increase in force of infection is more apparent. Whilst the differences between 2050 and 2070 are difficult to see for RCP scenario 2.6, both peak above zero. In RCP scenarios 4.5, 6.0 and 8.5, the distinction between years is clear, particularly in 8.5, with the greatest increases seen in 2070 as temperatures are expected to continue to rise.

![Figure 4.](https://cdn.elifesciences.org/articles/55619/elife-55619-fig4-v1.jpg)

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/55619/elife-55619-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** Sudan is a member of the North African region; however, due to the grouping of endemic countries, we include Sudan in the East African region.

When we examine the changes at country level, shown in the appendix, the changes are more heterogeneous. For RCP 2.6 Guinea Bissau, the change in force of infection in 2070 is potentially broad, with a credible interval spanning zero: 10.3% (95%CrI [−33.2% , 96.3%]). Whereas in Central African Republic, there is a notable increase by 87.1% (95%CrI [12.4% , 390.2%]).

### Projected burden

The projected percentage change in the annual number of deaths caused by YF across Africa is given in Table 1; the projected annual deaths per capita for endemic countries are shown in Figure 5 and in Figure 5—figure supplement 1. These projections assume vaccination is static from 2019 onwards that is that only routine vaccination continues at 2018 levels. Similarly, we assume case management is unvarying. Aggregated numbers of deaths per country and region are shown in the appendix.

**Table 1.**
 Predicted percentage change in deaths in the African endemic region in 2050 and 2070 compared to the baseline/current scenario.


<table>
  <thead>
    <tr>
      <th>Year</th>
      <th>Scenario</th>
      <th>95% CrI low</th>
      <th>50% CrI low</th>
      <th>Median</th>
      <th>50% CrI high</th>
      <th>95% CrI high</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2050</td>
      <td>RCP 2.6</td>
      <td>−2.36</td>
      <td>4.49</td>
      <td>10.84</td>
      <td>18.58</td>
      <td>37.91</td>
    </tr>
    <tr>
      <td>2050</td>
      <td>RCP 4.5</td>
      <td>−2.40</td>
      <td>7.32</td>
      <td>16.71</td>
      <td>28.16</td>
      <td>57.43</td>
    </tr>
    <tr>
      <td>2050</td>
      <td>RCP 6.0</td>
      <td>−2.78</td>
      <td>6.79</td>
      <td>15.49</td>
      <td>25.86</td>
      <td>51.85</td>
    </tr>
    <tr>
      <td>2050</td>
      <td>RCP 8.5</td>
      <td>−2.17</td>
      <td>11.03</td>
      <td>24.92</td>
      <td>41.84</td>
      <td>88.33</td>
    </tr>
    <tr>
      <td>2070</td>
      <td>RCP 2.6</td>
      <td>−0.74</td>
      <td>4.11</td>
      <td>9.99</td>
      <td>17.03</td>
      <td>34.10</td>
    </tr>
    <tr>
      <td>2070</td>
      <td>RCP 4.5</td>
      <td>−2.76</td>
      <td>7.77</td>
      <td>19.28</td>
      <td>33.56</td>
      <td>71.08</td>
    </tr>
    <tr>
      <td>2070</td>
      <td>RCP 6.0</td>
      <td>−4.56</td>
      <td>8.63</td>
      <td>21.35</td>
      <td>36.70</td>
      <td>77.70</td>
    </tr>
    <tr>
      <td>2070</td>
      <td>RCP 8.5</td>
      <td>−2.90</td>
      <td>16.08</td>
      <td>39.57</td>
      <td>72.43</td>
      <td>178.63</td>
    </tr>
  </tbody>
</table>

![Figure 5.](https://cdn.elifesciences.org/articles/55619/elife-55619-fig5-v1.jpg)

**Figure 5.:** Countries are ordered by longitude.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/55619/elife-55619-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** Countries are ordered by longitude.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/55619/elife-55619-fig5-figsupp2-v1.jpg)

**Figure 5—figure supplement 2.:** Countries are ordered by longitude.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/55619/elife-55619-fig5-figsupp3-v1.jpg)

**Figure 5—figure supplement 3.:** Countries are ordered by longitude.

While lower 95% credible intervals in Table 1 are negative, the overall posterior probabilities that climate change will increase YF mortality are very high for each climate scenario. The probability that deaths will increase is 95.5% (95% CrI [95.3%, 95.7%]) for RCP 2.6 in year 2070, rising to 95.9% (95% CrI [95.7%, 96.1%]) for RCP 8.5 in year 2070, values for all scenarios and years are shown in appendix 1.

As with the force of infection projections, the most severe increases are seen for RCP scenario 8.5, especially in year 2070. The distinction between current projected deaths per capita and those under each RCP scenario are most clearly seen for countries in Central Africa, such as Central African Republic, and East Africa, such as Ethiopia. The four countries with the least distinct change, Liberia, Guinea, Sierra Leone and the Gambia, are all in West Africa, commonly thought to see the most intense YF transmission. As such, it appears that the most marked increases in burden are found in East and central Africa.

## Discussion

We build on an established model of YF occurrence and transmission to accommodate temperature and precipitation projections for four climate emissions scenarios. Non-linear dependence on temperature was incorporated by utilising a function of temperature suitability, informed by thermal response data for A. aegypti. We jointly estimated parameters for the temperature suitability and occurrence models in a Bayesian framework, allowing us to quantify the uncertainty in our projections. We found that model fit remained good with a median AUC of 0.9004 despite necessary changes to the covariates used in the occurrence model compared with past work Garske et al., 2014; where changes were required in order to include covariates for which climate change projections were available. This gave us some confidence in the suitability of the model for projecting the impact of climate change on YF transmission through to 2070, the last year for which climate emission scenario projections are available for temperature and precipitation.

The force of infection is projected to increase for the majority of countries in each scenario. Consistently, the Central African Republic is one of the countries most likely to see an increase in transmission, while Liberia and Guinea Bissau have more uncertain projections. This highlights that the most severe proportional increases in force of infection are seen outside West Africa. However, as transmission is currently highest in West Africa, even a small future relative increase of 3% (seen for Liberia in scenario RCP 2.6 in year 2050, see appendix) could equate to a substantial increase in the projected absolute number of annual YF deaths.

In all scenarios, there is a high probability that the number of deaths and deaths per capita will increase in the African endemic region. The most marked changes are seen for RCP 8.5, the most severe emission scenario; however, changes are heterogeneous geographically with large proportional increases occurring in Central and East Africa. We expect the number of deaths per year to increase by 10.0% (95% CrI [−0.7, 34.1]) under RCP scenario 2.6 or 40.0% (95% CrI [−2.9, 178.6]) under RCP scenario 8.5 by 2070 (see Table 1 for other values).

We assume that the force of infection changes linearly between 2018 and 2050, and between 2050 and 2070. Video 1 illustrates this by showing posterior samples of the change in deaths by region for all years between 2018 and 2070. For RCP scenario 2.6, deaths largely cease increasing after year 2050, in line with the assumption that RCP 2.6 represents the situation where contributing carbon activities peak by 2030; however, this scenario has been suggested to be ‘unfeasible’ (Mora et al., 2013; van Vliet et al., 2009). In RCP scenario 8.5, carbon contribution activities are assumed to continue increasing throughout the century. A potential impact of this is seen in the number of YF deaths predicted by our model in East and Central Africa, which accelerate after 2050.

![Video 1.](https://cdn.elifesciences.org/articles/55619/elife-55619-video1.mp4.jpg)

**Video 1.:** 100 samples of the posterior predicted trajectories are shown.

Climate change may affect not only the magnitude of YF disease burden but also its distribution. We find that, through the projected changes in both temperature and rainfall, transmission may change heterogeneously across the region. This is emphasised by their individual contribution; in the appendix, we explore the effects of changes in only temperature or rainfall. This illustrates that whilst temperature change will drive the variation in transmission intensity with rainfall often acting to mitigate, in some countries there can be a ‘perfect storm’ of altering rainfall and temperature leading to increases in transmission that would not occur if only temperature was varying. This may lead to changing priorities with respect to vaccination. However, it is unclear whether the comparatively low proportional increase in burden seen for West Africa is due to more intensive vaccination or due to the limited increase in force of infection. Our results suggest that there could be drastic proportional increases in burden in East and Central Africa that may lead to greater vaccine demand in areas which have previously been of lower risk. Thus, whilst the countries experiencing the highest numbers of deaths will remain high risk, see Figure 1—figure supplement 3 and Figure 1—figure supplement 4 for the median distribution of deaths per year, countries such as Ethiopia and Somalia may become higher priority targets for vaccination.

Our analysis has a number of limitations. In order to utilise emission scenario projections, we were limited to covariates with projections in 2050 and 2070, namely temperature and precipitation. This meant that we adapted our previous best-fit model (Garske et al., 2014) to include temperature range, temperature suitability and precipitation rather than enhanced vegetation and landcover. This change slightly reduced fit quality, giving an AUC of 0.9004 as opposed to to 0.9157 (Gaythorpe et al., 2019). Vegetation is a key factor determining habitat of non-human primates, an element that may not be captured by the temperature suitability index which focuses on the vector A. aegypti. This omission may lead to an overestimation of the future burden as elements such as desertification and the impact of increasing frequencies of forest fires are not considered (Overpeck et al., 1990; Huang et al., 2016; James et al., 2013).

Similarly, whilst the RCP scenarios model socio-economic and land-use changes, we do not explicitly include these aspects here (van Vuuren et al., 2011). As such, we omit the human choices that may affect population distributions and behaviour, for example urbanisation which has been shown to both reduce disease burden (Wood et al., 2017) and increase emergence of arboviruses (Gubler, 2011; Hotez, 2017). In the same way, while our model accounts for migration through use of the UN WPP population data, climate scenario-specific migration is not included in the model. This may mean that we under estimate the potential increases in burden due to increased infringing of human environments on the sylvatic cycle. Projecting these non-linear relationships between human behaviour and transmission would be highly uncertain and is a source of ongoing research.

Vaccination is the main control method for yellow fever and whilst we account for vaccine coverage and efficacy in this mansucript, we do not explicitly propagate uncertainty in vaccination coverage. This will be uncertain not only through data scarcity on vaccination campaign doses, wastage and clustering of doses, but also through the uncertainty in demography. We have presented a comparison of scenarios where, in all cases, vaccination coverage distribution, is held to be the same. As such, whilst we focus on the effect of changing transmission, we will underestimate the uncertainty in our estimates of burden in the future.

Data availability constrains aspects of our modelling approach. We use A. aegypti and YF-specific datasets to inform the thermal response relationships and thus, temperature suitability index. However, some data, such as information on the extrinsic incubation period are severely limited; we use a dataset of experimental results from 1930s (Davis, 1932). These data may be outdated due to current mosquito species potentially adapting to different climates as well as improved experimental procedures. This is a key data gap for YF and new experimental results concerning the extrinsic incubation period could provide valuable insight into the dynamics of the virus in mosquitoes today.

As further experimental data on thermal responses for A. aegypti and other vectors of YF become available, the temperature suitability index developed here will be able to be enhanced. YF is known to have multiple vectors, each contributing to transmission cycles differently (Monath and Vasconcelos, 2015), which are likely to have different thermal responses. Focusing only on the urban vector of YF, as we have in this manuscript, means that we will likely under-estimated the uncertainty in the thermal response of the vectors of YF and thus future projections of burden. Additionally, whilst we have included a relatively detailed relationship between transmission and temperature, we have only assumed a simple relationship with rainfall. Currently models of thermal response for vectors of diseases such as YF are well parametrised with experimental results; however, this is not yet the case for the influence of rainfall on transmission although there are clear links with aspects such as vector breeding. As these relationships are better characterised, we can further refine the relationships in the current work to reflect the more nuanced relationships between temperature, rainfall and transmission.

We focus only on a constant force of infection model which is similar to assuming the majority of transmission occurs as a result of zoonotic spillover. This assumption is supported by recent studies Gaythorpe et al., 2019; however, the urban transmission cycle, driven by A. aegypti plays a crucial role in YF risk and was responsible for recent severe outbreaks such as that in Angola in 2016. Incorporating climate projections into models that examine multiple transmission routes and thermal responses for multiple vectors, would produce a more realistic picture of how the dynamics of this disease may change with climate.

Climate change is projected to have major global impacts on disease distribution and burden (Mordecai et al., 2017; Huber et al., 2018; Kraemer et al., 2015). Here, we examined the specific effects on YF and find that disease burden and deaths are likely to increase heterogeneously across Africa. This emphasises the need to implement and prepare for new vaccination activities, and consolidate existing control strategies in order to mitigate the rising risk from YF. Intervention through vaccination is the gold standard for YF, and new approaches are being implemented with respect to fractional dosing which is a useful resort to respond to urban outbreaks in case of vaccine shortage (Vannice et al., 2018). Yet, vaccination is not the only potentially effective control for YF, with novel vector control measures such as the use of Wolbachia showing promise, and perspectives to improve clinical management or urban resilience (Rocha et al., 2019; World Health Organization, 2017). Finally, in order to monitor and respond to changing transmission patterns, effective and sensitive surveillance will be essential.

## Materials and methods

A schematic of data sources and models is shown in Figure 1—figure supplement 1.

### Datasets

We use a number of data sets to inform both the generalised linear model (GLM) of YF occurrence and the temperature suitability model. Additionally, we rely on estimates of transmission intensity informed by serological studies which are detailed in Gaythorpe et al., 2019 and described below.

#### YF occurrence

Details of YF outbreaks occurring from 1984 to present day were collated into a database of occurrence, extended from Garske et al., 2014. These data were collected from the World Health Organisation (WHO) weekly epidemiological record (WER), disease outbreak news (DON), published literature and internal WHO reports (World Health Organization, 2009; World Health Organization, 1996). The database includes all outbreaks recorded for yellow fever and is resolved at province level, any reports that could not be resolved at province level were excluded. Additionally, reports of suspected YF cases were collected in the WHO African Regional Office YF surveillance database (YFSD); this included data from 21 countries in West and Central Africa. The database was based on the broad case definition of fever and jaundice leading to a large proportion of cases attributed to non-YF causes and cross-reactivity with other flaviviruses was not considered. However, the incidence of suspected cases can be used as a measure of surveillance effort and is included as a covariate in the generalised linear model. We assume this to be constant over time due to scarcity of data on the subject.

#### YF serological status

Surveys of seroprevalence were conducted in Central and East Africa. We use these to assess transmission intensity in specific regions of the African endemic zone. The current study includes surveys from published sources (Diallo et al., 2014; Kuniholm et al., 2006; Merlin et al., 1986; Omilabu et al., 1990; Tsai et al., 1987; Werner and Huber, 1984) and unpublished surveys from East African countries conducted between 2012 and 2015 as part of the YF risk assessment process (Mengesha Tsegaye et al., 2018). The surveys were included only if they represent the population at steady state, as such outbreak investigations were omitted (Garske et al., 2014). Additionally, in the majority of surveys, vaccinated individuals were not included; however, in South Cameroon, vaccination status is unclear and so we fit an additional vaccine factor for this survey. Summary details of the seroprevalence studies are included in the apendix.

#### Past vaccination coverage and demography

Vaccination coverage is estimated using data on historic large-scale mass vaccination activities taking place between 1940 and 1960 (Durieux, 1956; Moreau et al., 1999), routine infant immunisation reported by the WHO and UNICEF estimates of National Immunization Coverage (WUENIC) (World Health Organization/ UNICEF, 2015), outbreak response campaigns from 1970 onwards which are detailed in the WHO WER and DON (World Health Organization, 2009; World Health Organization, 1996) and recent preventive mass-vaccination campaigns carried out as part of the yellow fever initiative (World Health Organisation, 2016). The coverage is estimated with the methodology of Garske et al. and Hamlet et al. and is visualised in the polici shiny application (Garske et al., 2014; Hamlet et al., 2018a). The application provides vaccination coverage estimates at province level for 34 endemic countries in Africa which can be downloaded for years between 1940 and 2050. We assume all targeted age groups have an equal chance of vaccination irrespective of vaccination staus.

Demography is obtained from the UN World Population Prospect (UN WPP) (DoE United Nations, 2017). We dis-aggregate this to province level by combining it with estimates of spatial population distributions from LandScan 2014 (Dobson et al., 2000). This allows us to estimate population sizes at province level for each year of interest assuming that the age structure is relatively similar across all provinces in each country.

#### Environmental and climate projections

We use three main environmental covariates within the generalised linear model of YF occurrence: mean annual rainfall, average temperature and temperature range, shown in Figure 6 and listed in Table 2. These are gridded data at various resolutions, ranging from approximately 1 km to 10 km, which we average at the first administrative unit level (Nasa LPD, 2001; Xie and Arkin, 1996; Hijmans et al., 2004).

**Table 2.**
 Generalised linear model covariates.


<table>
  <thead>
    <tr>
      <th>Covariate</th>
      <th>Interpretation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>log(survey quality)</td>
      <td>Log of the survey quality for countries in YFSD.</td>
    </tr>
    <tr>
      <td>adm05</td>
      <td>Country factors for countries not in YFSD.</td>
    </tr>
    <tr>
      <td>longitude</td>
      <td>Longitude of province centroid</td>
    </tr>
    <tr>
      <td>temperature suitability</td>
      <td>Temperature suitability at average suitability of province.</td>
    </tr>
    <tr>
      <td>temperature range</td>
      <td>Temperature range in province.</td>
    </tr>
    <tr>
      <td>rainfall</td>
      <td>Mean Precipitation in province.</td>
    </tr>
    <tr>
      <td>log(pop)</td>
      <td>Log of the human population size of the province</td>
    </tr>
  </tbody>
</table>

![Figure 6.](https://cdn.elifesciences.org/articles/55619/elife-55619-fig6-v1.jpg)

**Figure 6.:** Countries shown in black are not considered endemic for YF. (a) Estimated mean monthly rainfall (mm) for baseline/current scenario. (b) Average temperature at baseline/current scenario in °C. (c) Longitude. (d) Range in temperature at baseline/current scenario in °C.

Projected temperature and rainfall changes under climate change scenarios were obtained from worldclim version 1.4 (Hijmans et al., 2005; Fick and Hijmans, 2017). These data provided the 5th Intergovernmental panel on climate change (IPPC5) climate projections for four Representative Concentration Pathways (RCPs): 2.6, 4.5, 6.0 and 8.5 (van Vuuren et al., 2011). The different RCPs indicate different possible emission scenarios and represent the resulting radiative forcing in 2100, measured in W/m2 or watts per square metre, see Table 3 for further information (Stocker, 2013). Each scenario is assumed to peak at a different times, with emissions peaking between 2010 and 2020 for RCP 2.6, but rising throughout the century for RCP 8.5. Projections of the mean global temperature rise by 2046–2065 are 1 or 2 °C for RCPs 2.6 or 8.5, respectively, compared to pre-industrial levels of the 1880s. By the end of the century, these projections suggest a rise of 1 [0.3 to 1.7] or 3.9 [2.6 to 4.8]°C for RCPs 2.6 or 8.5 (Stocker, 2013; Rogelj et al., 2012). Current warming is estimated to be 0.85 °C since pre-industrial levels (Stocker, 2013). Based on current commitments through aspects such as the Paris agreement, scenarios where temperatures are expected to rise by more than 3 °C have been suggested to be most likely (Sanford et al., 2014). As such, a recent study omitted the RCP 2.6 scenario as it is unlikely now to occur (Mora et al., 2013; van Vliet et al., 2009).

**Table 3.**
 Projected change in global mean surface air temperature and CO2 concentrations by 2100 relative to the reference period of 1986–2005 (Stocker, 2013).


<table>
  <thead>
    <tr>
      <th>Scenario</th>
      <th>Temperature rise (°C) [range]</th>
      <th>CO2 concentrations (ppm)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>RCP 2.6</td>
      <td>1 [0.3 to 1.7]</td>
      <td>421</td>
    </tr>
    <tr>
      <td>RCP 4.5</td>
      <td>1.8 [1.1 to 2.6]</td>
      <td>538</td>
    </tr>
    <tr>
      <td>RCP 6.0</td>
      <td>2.2 [1.4 to 3.1]</td>
      <td>670</td>
    </tr>
    <tr>
      <td>RCP 8.5</td>
      <td>3.7 [2.6 to 4.8]</td>
      <td>936</td>
    </tr>
  </tbody>
</table>

Projected mean rainfall, maximum temperature and minimum temperature are available for each RCP scenario in years 2050 and 2070. We take the midpoint and range of the temperature as inputs for the model of YF occurrence, where the midpoint temperature is used to calculate the temperature suitability index.

We do not model changes in climate prior to 2018, instead using Worldclim baseline estimates described as representative of conditions from 1960 to 1990 (Hijmans et al., 2005).

#### Temperature suitability

We estimate the components of the temperature suitability index from YF-specific sources of information on extrinsic incubation period, vector mortality and bite rate for A. aegypti, the urban vector of YF (Davis, 1932; Tesla et al., 2018; Hamlet et al., 2018b; Mordecai et al., 2017). The extrinsic incubation period was estimated from the experimental results of Davis which were calculated specifically for YF in A. aegypti (Davis, 1932). We included bite rate data from both Mordecai et al., 2017 and Martens, 1998 which both describe A. aegypti. Finally, vector mortality was estimated from the experimental data of Tesla et al., 2018. Where data was provided in figure form, plots were digitised to extract the information. All data used for fitting the temperature suitability model are made available in the GitHub repo (https://github.com/mrc-ide/YF_climateChange; Gaythorpe, 2020; copy archived at https://github.com/elifesciences-publications/YF_climateChange). Whilst we focus only on thermal response of the urban vector of YF due to data availability, we estimate the thermal response models within a Bayesian hierarchical framework in order to capture some of the uncertainty that we miss from examining one vector species.

### Models

We reformulate an established model of YF occurrence to accommodate nonlinear dependence on temperature and rainfall (Garske et al., 2014; Jean et al., 2020; Gaythorpe et al., 2019). We couple this with established results from a transmission model of serological status to estimate transmission intensity across the African endemic region at baseline/current environmental conditions . Then, we project transmission intensity for four climate scenarios given projected changes in temperature and rainfall.

#### YF occurrence

The generalised linear model (GLM) of YF occurrence provides the probability of a YF report at first administrative unit level for the African endemic region dependent on key climate variables. In order to assess the effect of climate change on YF transmission, we use the same methodology as (Garske et al., 2014; Jean et al., 2020; Gaythorpe et al., 2019); and incorporate covariates indicative of climate change that also have projections available in years 2050 and 2070 for different emission scenarios. As such, we omit enhanced vegetation index and land cover from the best fitting model of Garske et al., 2014 in favour of the temperature suitability index which depends on the average temperature, the temperature range and average rainfall. Temperature and rainfall are known to have implications on both the vectors of YF and the distribution of the non-human primate reservoir (Reinhold et al., 2018; Cowlishaw and Hacker, 1997). However, the effect of temperature, particularly on vectors, is highly non-linear with increased mortality seen at very low and high temperatures; as such, we include the range in temperature as a covariate of our occurrence model as well as the non-linear temperature suitability index (Mordecai et al., 2017; Tesla et al., 2018). A full listing of covariates used in given in the appendix.

#### Temperature suitability

We model suitability of the environment for YF transmission through temperature dependence. It has been shown that the characteristics of the virus and vector change with temperature (Brady et al., 2014; Kraemer et al., 2015; Mordecai et al., 2017; Tjaden et al., 2018). We model this using a function of temperature for the mosquito biting rate, the extrinsic incubation period and mortality rate for the mosquito which we combine to calculate the temperature suitability based on the Ross-MacDonald formula for the basic reproduction number of a mosquito-borne disease (Macdonald, 1957). In the below, we focus on A. aegypti.

The functional form used to model temperature suitability varies in the literature. We continue to use a form which can be parameterised solely from data specific to YF (Hamlet et al., 2018b; Garske et al., 2013). However, alternative formulations have been published in the context of other arboviral infections (Mordecai et al., 2017; Ryan et al., 2019; Brady et al., 2014; Brady et al., 2013; Tjaden et al., 2018).

Each input of the temperature suitability, $z⁢(T)$, is modelled as a function of average temperature where the individual thermal response follow the forms of Mordecai et al. The temperature suitability equation is as follows:

$$
z⁢(T)=\frac{a⁢(T)^{2}⁢exp⁡(-\mu⁢(T)⁢ρ⁢(T))}{\mu⁢(T)},
$$

where $T$ denotes mean temperature, $ρ$ is the extrinsic incubation period, $a$ is the bite rate and μ is the mosquito mortality rate. The thermal response models for $ρ$, $a$ and μ follow Mordecai et al., 2017 as follows:

$$
a(T)=a_{c}T(T−a_{T_{0}})(a_{T_{m}}−T)^{0.5},
$$



$$
ρ(T)=1/ρ_{c}T(T−ρ_{T_{0}})(ρ_{T_{m}}−T)^{0.5},
$$



$$
\mu(T)=1/(−\mu_{c}(T−\mu_{T_{0}})(\mu_{T_{m}}−T)),
$$

where the subscripts $T_{0}$ and $T_{m}$ indicate respectively the minimum and maximum values of each variable, and subscript $c$ labels the positive rate constant for each model. The three resulting parameters for each model are estimated by fitting to available experimental data. The mortality rate μ is limited to be positive.

#### Mapping probability of occurence to force of infection

We utilise previously estimated models of seroprevalence informed by serological survey data, demography and vaccination coverage information (Garske et al., 2014; Gaythorpe et al., 2019). The transmission intensity is assumed to be a static force of infection, akin to the assumption that most YF infections occur as a result of sylvatic spillover (Garske et al., 2014; Gaythorpe et al., 2019). The force of infection is assumed to be constant in each province over time and age. As such, we may model the serological status of the population in age group $u$ as the following:

$$
S⁢(\lambda,u)=1-(1-\frac{\sum_{a\inu}(1-exp⁡(-\lambda⁢a))⁢p_{a}}{\sum_{a\inu}p_{a}})⁢(1-\frac{\sum_{a\inu}v_{a}⁢p_{a}}{\sum_{a\inu}p_{a}})
$$

where $\lambda$ is the force of infection, $p_{a}$ the population in annual age group $a$ and $v_{a}$ the vaccination coverage in annual age group $a$. This provides us with estimates of force of infection in specific locations where serological surveys are available.

In order to estimate transmission intensity in areas where no serological survey data is available, we link the GLM predictions with seroprevalence estimates through a Poisson reporting process. The force of infection can be used to estimate the number of infections in any year. Thus, we may calculate the number of infections over the observation period. These will be reported with a certain probability to give the occurrence shown in the GLM. As such, we assume that the probability of at least one report in a province over the observation period, $q_{i}$, depends on the number of infections in the following way:

$$
q_{i}=1-(1-ρ_{i})^{n_{i⁢n⁢f,i}}
$$

where $ρ_{c}$ is the per-country reporting factor which we relate to the GLM in the following way:

$$
n_{i⁢n⁢f,i}⁢ln⁡(1-ρ_{c})=-exp⁡(X⁢\beta)
$$

where $X$ are the model covariates and $\beta$, the coefficients. The probability of detection can then be written in terms of the country factors, which are GLM covariates, $\beta_{c}$, and $b$, the baseline surveillance quality calculated from the serological survey data:

$$
ln⁡(-ln⁡(1-ρ_{c}))=\beta_{c}+b.
$$

Thus, we may transform the predictions given by the GLM of YF occurrence using the probability of detection obtained in the provinces where we have both serological studies and GLM predictions to produce FOI estimates for the entire endemic region.

### Estimation

We estimate the models of temperature suitability and YF report together within a Bayesian framework using Metropolis-Hastings Markov Chain Monte Carlo sampling with an adaptive proposal distribution (Andrieu and Thoms, 2008; McKinley et al., 2014; Roberts and Rosenthal, 2009; Sherlock et al., 2015; Tennant and McKinley, 2019). The likelihood contains components for the GLM of YF reports as well as the thermal response models and is given by the following:

$$
log⁡(L)=log⁡(L_{G⁢L⁢M})+log⁡(L_{a})+log⁡(L_{ρ})+log⁡(L_{\mu}),
$$

where $log⁡(L_{x})$ denotes the log likelihood of element $x$. The log likelihood for the GLM assumes that the binary YF occurrence data is Bernoulli distributed (Garske et al., 2014):

$$
log⁡(L_{G⁢L⁢M})=\sumi(y_{i}⁢log⁡(q_{i})+(1-y_{i})⁢log⁡(1-q_{i})),
$$

where $y_{i}$ is the binary occurrence and $q_{i}$ is the probability of at least one YF report in province $i$. We propagate uncertainty in the estimation of the GLM from the thermal response models as well as that from the seroprevalence into the resulting transmission intensity estimates.

The thermal response likelihoods are provided by an exponential distribution for bite rate, a Bernoulli distribution for mortality and a normal distribution for extrinsic incubation period.

The estimation, analysis and manuscript were all performed or written in R version 3.5.1, ridgeline plots were generated with packages ggplot2 and ggridges (R Development Core Team, 2014; Wickham, 2016; Wilke, 2018; Garnier, 2018).

### Future projections

In order to assess future changes in force of infection, and thus disease burden, we incorporate ensemble climate projections of temperature change and precipitation. We assume that the force of infection is constant until 2018 and then changes linearly between 2018, 2050 and 2070, the years for which climate projections are available. Furthermore, in order to compare only the influence of changing population and force of infection, we assume that vaccination after 2019 is kept at the routine levels of 2018. As such, the results will not be affected by country-specific preventive vaccination campaigns but, future burden will be over estimated as there are likely to be preventive and reactive campaigns in future. We estimate burden by calculating the proportion of infections who become severe cases and then, of those, the proportions that die, using published case fatality ratio estimates (Johansson et al., 2014). We compare burden estimates with a baseline scenario assuming the same demographic conditions and vaccination levels as the climate change scenarios but no change in climate variables (precipitation and temperature) over time.
