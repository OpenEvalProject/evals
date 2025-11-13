# Transmission of West Nile and five other temperate mosquito-borne viruses peaks at temperatures between 23°C and 26°C

## Authors

- Marta S Shocket<sup>1</sup> ([ORCID: 0000-0002-8995-4446](https://orcid.org/0000-0002-8995-4446)) †
- Anna B Verwillow<sup>1</sup>
- Mailo G Numazu<sup>1</sup>
- Hani Slamani<sup>3</sup>
- Jeremy M Cohen<sup>4</sup>
- Fadoua El Moustaid<sup>6</sup>
- Jason Rohr<sup>4</sup>
- Leah R Johnson<sup>3</sup>
- Erin A Mordecai<sup>1</sup>

### Affiliations

1. Department of Biology, Stanford University Stanford United States
2. Department of Ecology and Evolutionary Biology, University of California Los Angeles Los Angeles United States
3. Department of Statistics, Virginia Polytechnic Institute and State University (Virginia Tech) Blacksburg United States
4. Department of Integrative Biology, University of South Florida Tampa United States
5. Department of Forest and Wildlife Ecology, University of Wisconsin Madison United States
6. Department of Biological Sciences, Virginia Polytechnic Institute and State University (Virginia Tech) Blacksburg United States
7. Department of Biological Sciences, Eck Institute of Global Health, Environmental Change Initiative, University of Notre Dame South Bend United States

† Corresponding author

## Abstract

The temperature-dependence of many important mosquito-borne diseases has never been quantified. These relationships are critical for understanding current distributions and predicting future shifts from climate change. We used trait-based models to characterize temperature-dependent transmission of 10 vector–pathogen pairs of mosquitoes (Culex pipiens, Cx. quinquefascsiatus, Cx. tarsalis, and others) and viruses (West Nile, Eastern and Western Equine Encephalitis, St. Louis Encephalitis, Sindbis, and Rift Valley Fever viruses), most with substantial transmission in temperate regions. Transmission is optimized at intermediate temperatures (23–26°C) and often has wider thermal breadths (due to cooler lower thermal limits) compared to pathogens with predominately tropical distributions (in previous studies). The incidence of human West Nile virus cases across US counties responded unimodally to average summer temperature and peaked at 24°C, matching model-predicted optima (24–25°C). Climate warming will likely shift transmission of these diseases, increasing it in cooler locations while decreasing it in warmer locations.

## Introduction

Temperature is a key driver of transmission of mosquito-borne diseases. Both mosquitoes and the pathogens they transmit are ectotherms whose physiology and life histories depend strongly on environmental temperature (Johnson et al., 2015; Mordecai et al., 2019; Mordecai et al., 2017; Mordecai et al., 2013; Paull et al., 2017; Rogers and Randolph, 2006; Shocket et al., 2018; Tesla et al., 2018). These temperature-dependent traits drive the biological processes required for transmission. For example, temperature-dependent fecundity, development, and mortality of mosquitoes determine whether vectors are present in sufficient numbers for transmission. Temperature also affects the mosquito biting rate on hosts and probability of becoming infectious.

Mechanistic models based on these traits and guided by principles of thermal biology predict that the thermal response of transmission is unimodal: transmission peaks at intermediate temperatures and declines at extreme cold and hot temperatures (Johnson et al., 2015; Liu-Helmersson et al., 2014; Martens et al., 1997; Mordecai et al., 2019; Mordecai et al., 2017; Mordecai et al., 2013; Parham and Michael, 2010; Paull et al., 2017; Shocket et al., 2018; Tesla et al., 2018; Wesolowski et al., 2015). This unimodal response is predicted consistently across mosquito-borne diseases (Johnson et al., 2015; Mordecai et al., 2019; Mordecai et al., 2017; Mordecai et al., 2013; Paull et al., 2017; Shocket et al., 2018; Tesla et al., 2018) and supported by independent empirical evidence for positive relationships between temperature and human cases in many settings (Stewart-Ibarra and Lowe, 2013; Paull et al., 2017; Peña-García et al., 2017; Siraj et al., 2015; Werner et al., 2012), but negative relationships at high temperatures in other studies (Gatton et al., 2005; Mordecai et al., 2013; Peña-García et al., 2017; Perkins et al., 2015; Shah et al., 2019). Accordingly, we expect increasing temperatures due to climate change to shift disease distributions geographically and seasonally, as warming increases transmission in cooler settings but decreases it in settings near or above the optimal temperature for transmission (Lafferty, 2009; Lafferty and Mordecai, 2016; Rohr et al., 2011; Ryan et al., 2015). Thus, mechanistic models have provided a powerful and general rule describing how temperature affects the transmission of mosquito-borne disease. However, thermal responses vary among mosquito and pathogen species and drive important differences in how predicted transmission responds to temperature, including the specific temperatures of the optimum and thermal limits for each vector–pathogen pair (Johnson et al., 2015; Mordecai et al., 2019; Mordecai et al., 2017; Mordecai et al., 2013; Paull et al., 2017; Shocket et al., 2018; Tesla et al., 2018). We currently lack a framework to describe or predict this variation among vectors and pathogens.

Filling this gap requires comparing mechanistic, temperature-dependent transmission models for many vector–pathogen pairs. However, models that incorporate all relevant traits are not yet available for many important pairs for several reasons. First, the number of relevant vector–pathogen pairs is large because many mosquitoes transmit multiple pathogens and many pathogens are transmitted by multiple vectors. Second, empirical data are costly to produce, and existing data are often insufficient because experiments or data reporting were not designed for this purpose. Here, we address these challenges by systematically compiling data and building models for understudied mosquito-borne disease systems, including important pathogens with substantial transmission in temperate areas like West Nile virus (WNV) and Eastern Equine Encephalitis virus (EEEV). Accurately characterizing the thermal limits and optima for these systems is critical for understanding where and when temperature currently promotes or suppresses transmission and where and when climate change will increase, decrease, or have minimal effects on transmission.

In this study, we model the effects of temperature on an overlapping suite of widespread, important mosquito vectors and viruses that currently lack complete temperature-dependent models. These viruses include: West Nile virus (WNV), St. Louis Encephalitis virus (SLEV), Eastern and Western Equine Encephalitis viruses (EEEV and WEEV), Sindbis virus (SINV), and Rift Valley fever virus (RVFV) (Adouchief et al., 2016; Go et al., 2014; Kilpatrick, 2011; Linthicum et al., 2016; Weaver and Barrett, 2004; summarized in Table 1). All but RVFV sustain substantial transmission in temperate regions (Adouchief et al., 2016; Go et al., 2014; Kilpatrick, 2011; Linthicum et al., 2016; Weaver and Barrett, 2004). We selected this group because many of the viruses share common vector species and several vector species transmit multiple viruses (Table 1, Figure 1). All the viruses cause febrile illness and severe disease symptoms, including long-term arthralgia and neuroinvasive syndromes with a substantial risk of mortality in severe cases (Adouchief et al., 2016; Go et al., 2014; Kilpatrick, 2011; Linthicum et al., 2016; Weaver and Barrett, 2004). Since invading North America in 1999, WNV is now distributed worldwide (Kilpatrick, 2011; Rohr et al., 2011) and is the most common mosquito-borne disease in the US, Canada, and Europe. SLEV, EEEV, and WEEV occur in the Western hemisphere (Table 1), with cases in North, Central, and South America (Centers for Disease Control and Prevention, 2018a; Centers for Disease Control and Prevention, 2018b; Go et al., 2014). For EEEV, North American strains are genetically distinct and more virulent than the Central and South American strains (Go et al., 2014). An unusually large outbreak of EEEV in the United States in 2019 has yielded incidence four times higher than average (31 cases, resulting in nine fatalities) and brought renewed attention to this disease (Bates, 2019). SINV occurs across Europe, Africa, Asia, and Australia, with substantial transmission in northern Europe and southern Africa (Adouchief et al., 2016; Go et al., 2014). RVFV originated in eastern Africa and now also occurs across Africa and the Middle East (Linthicum et al., 2016). These pathogens primarily circulate and amplify in wild bird reservoir hosts (except RVFV, which primarily circulates in livestock). For all six viruses, humans are dead-end or unimportant reservoir hosts (Go et al., 2014; Sang et al., 2017), in contrast to pathogens like malaria, dengue virus, yellow fever virus, and Ross River virus, which sustain infection cycles between humans and mosquitoes (Go et al., 2014; Gonçalves et al., 2017; Harley et al., 2001). Most transmission of RVFV to humans occurs through direct contact with infected livestock (that are infected by mosquitoes), and to a lesser extent via the mosquito-borne transmission from infected vectors (Sang et al., 2017).

![Figure 1.](https://cdn.elifesciences.org/articles/58511/elife-58511-fig1-v1.jpg)

**Figure 1.:** The six viruses in this study (WNV = West Nile virus, SLEV = St. Louis Encephalitis virus, EEEV = Eastern Equine Encephalitis virus, WEEV = Western Equine Encephalitis virus, SINV = Sindbis virus, RVFV = Rift Valley Fever virus) and the Culex (Cx.), Aedes (Ae.), Coquillettidia (Cq.), and Culiseta (Cs.) vectors that are most important for sustaining transmission to humans according to the following sources: (Adouchief et al., 2016; Braack et al., 2018; Golding et al., 2012; Linthicum et al., 2016; Sang et al., 2017; Weaver and Barrett, 2004). The importance of each vector for transmission varies over the geographic range of the virus, and this list of vectors is not exhaustive for any virus (see sources for more complete lists of confirmed and potential vectors). Grey shading indicates an important vector-virus pair; hatching indicates available temperature-dependent data for infection traits (pathogen development rate [PDR] and vector competence [bc], which is comprised of infection efficiency [c] and transmission efficiency [b]). Infection data were available for SINV and RVFV in Ae. taeniorhynchus, although this North American mosquito does not occur in the endemic range of these pathogens.

**Table 1.**
 Properties of six viruses transmitted by an overlapping network of mosquito vectors.


<table>
  <thead>
    <tr>
      <th>Virus (genus)</th>
      <th>Primary vector spp.</th>
      <th>Geographic range</th>
      <th>Presentation and mortality</th>
      <th>Epidemiology and Ecology</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>West Nile virus (WNV, Flavivirus)</td>
      <td>Cx. modestus, Cx. pipiens, Cx. quinquefasciatus, Cx. tarsalis</td>
      <td>Globally distributed</td>
      <td>Febrile illness and encephalitis. 10% mortality in neuro-invasive cases. Long-term physical and cognitive disabilities.</td>
      <td>The most common mosquito-borne disease in North America. Since invading in 1999, 7 million estimated infections, 22,999 neuroinvasive cases, and 2163 deaths in US; 5614 reported cases in Canada. Typically 100–300 cases annually in Europe, but over 1500 in 2018. Poor surveillance in Africa, but seroprevalence ~ 80% in some areas. Birds are main reservoir/amplification hosts.</td>
    </tr>
    <tr>
      <td>St. Louis Encephalitis virus (SLEV, Flavivirus)</td>
      <td>Cx. quinquefasciatus, Cx. tarsalis</td>
      <td>Western hemisphere; western, midwestern, and southern US</td>
      <td>Encephalitis. 5–15% mortality in diagnosed cases.</td>
      <td>92 cases and six deaths recorded in US from 2009 to 2018. Birds are main reservoir/amplification hosts.</td>
    </tr>
    <tr>
      <td>Eastern Equine Encephalitis virus (EEEV, Alphavirus)</td>
      <td>Ae. triseriatus, Cs. melanura</td>
      <td>Western hemisphere; eastern and midwestern US</td>
      <td>Febrile illness and encephalitis. 33% mortality in diagnosed cases. Long-term cognitive disabilities.</td>
      <td>73 cases and 30 deaths recorded in US from 2009 to 2018. Birds are main reservoir/amplification hosts.</td>
    </tr>
    <tr>
      <td>Western Equine Encephalitis virus (WEEV, Alphavirus)</td>
      <td>Cx. tarsalis</td>
      <td>Western hemisphere; western and midwestern US</td>
      <td>Febrile illness and encephalitis. Low mortality, except in infants.</td>
      <td>640 cases recorded in US from 1964 to 2010. Birds are main reservoir/amplification hosts. WEEV is derived from a recombinant event between the ancestors of EEEV and SINV.</td>
    </tr>
    <tr>
      <td>Sindbis virus (SINV, Alphavirus), also called Pogosta, Ockelbo, and Karelian Fever</td>
      <td>Cx. torrentium, Cx. pipiens, Cx. univittatus</td>
      <td>Europe, Africa, Asia and Australia, primarily northern Europe and southern Africa</td>
      <td>Febrile illness, rash, and joint pain. No mortality, but long-term disability.</td>
      <td>Poor surveillance except in Finland, where annual incidence is 2–26 per 100,000 people and seroprevalence can reach ~40%. Birds are main reservoir/amplification hosts. Long-distance migratory birds may spread the virus between temperate zones in Northern and Southern hemispheres.</td>
    </tr>
    <tr>
      <td>Rift Valley Fever virus (RVFV, Phlebovirus)</td>
      <td>Ae. mcintoshi, Ae. ochraceus, Ae. vexans, Cx. pipiens, Cx. poicilipes, Cx. theileri and many more</td>
      <td>Africa and the Middle East</td>
      <td>Febrile illness and encephalitis. &lt; 1% mortality in total cases. 50% mortality in hemorrhagic cases, permanent blindness in 50% of ocular cases (&lt;2% of cases).</td>
      <td>Livestock are main reservoir/amplification hosts, and suffer mortality and abortion after being infected by mosquitoes. Most transmission to humans occurs via direct contact with infected livestock. Vertical transmission in vectors (via dormant eggs) can initiate epidemics. In eastern and southern Africa, there are large epidemics every 5–15 years driven by rainfall and blooms of Ae. spp. from low-lying flooded areas known as dambos.</td>
    </tr>
  </tbody>
</table>

_Sources: WNV (Centers for Disease Control and Prevention, 2018c; European Centre for Disease Prevention and Control, 2018; Golding et al., 2012; Government of Canada, 2018; Kilpatrick, 2011; Petersen et al., 2013; Ronca et al., 2019; Weaver and Barrett, 2004); SLEV (Centers for Disease Control and Prevention, 2018a; Weaver and Barrett, 2004); EEEV (Centers for Disease Control and Prevention, 2018b; Weaver and Barrett, 2004); WEEV (Ronca et al., 2016; Weaver and Barrett, 2004); SINV (Adouchief et al., 2016); RVFV (Braack et al., 2018; Linthicum et al., 2016; Sang et al., 2017; World Health Organization, 2018)._

We primarily focus on Culex pipiens, Cx. quinquefasciatus, and Cx. tarsalis, well-studied species that are important vectors for many of the viruses and for which appropriate temperature-dependent data exist for nearly all traits relevant to transmission. Although the closely-related Cx. pipiens and Cx. quinquefasciatus overlap in their home ranges in Africa, they have expanded into distinct regions globally (Figure 2; Farajollahi et al., 2011). Cx. pipiens occurs in higher latitude temperate areas in the Northern and Southern hemisphere, while Cx. quinquefasciatus occurs in lower latitude temperate and tropical areas (Figure 2A). By contrast, Cx. tarsalis is limited to North America but spans the tropical-temperate gradient (Figure 2B). In this system of shared pathogens and vectors with distinct geographical distributions, we also test the hypothesis that differences in thermal performance underlie variation in vector and pathogen geographic distributions, since temperate environments have cooler temperatures and a broader range of temperatures than tropical environments. We also include thermal responses from other relevant vector or laboratory model species in some models: Aedes taeniorhynchus (SINV and RVFV), Ae. triseriatus (EEEV), Ae. vexans (RVFV), Cx. theileri (RVFV), and Culiseta melanura (EEEV). Additionally, we compare our results to previously published models (Johnson et al., 2015; Mordecai et al., 2017; Mordecai et al., 2013; Shocket et al., 2018; Tesla et al., 2018) for transmission of more tropical diseases by the following vectors: Ae. aegypti, Ae. albopictus, Anopheles spp., and Cx. annulirostris.

![Figure 2.](https://cdn.elifesciences.org/articles/58511/elife-58511-fig2-v1.jpg)

**Figure 2.:** The geographic distribution of the primary vectors of West Nile virus: (A) Culex pipiens (dark grey) and Cx. quinquefasciatus (red), adapted from Farajollahi et al., 2011; Smith and Fonseca, 2004; (B) Cx. tarsalis (blue), northern boundary from Darsie and Ward, 2016, southern boundary based on data from the Global Biodiversity Information Facility. Figure created by Michelle Evans for this paper.

We use a mechanistic approach to characterize the effects of temperature on vector–virus pairs in this network using the thermal responses of traits that drive transmission. Specifically, we use experimental data to measure the thermal responses of the following traits: vector survival, biting rate, fecundity, development rate, competence for acquiring and transmitting each virus, and the extrinsic incubation rate of the virus within the vector. We ask: (1) Do these vectors have qualitatively similar trait thermal responses to each other, and to vectors from previous studies? (2) Is transmission of disease by these vectors predicted to be optimized and limited at similar temperatures, compared to each other and to other mosquito-borne diseases in previous studies? (3) How do the thermal responses of transmission vary across vectors that transmit the same virus and across viruses that share a vector? (4) Which traits limit transmission at low, intermediate, and high temperatures? Broadly, we hypothesize that variation in thermal responses is predictable based on vectors’ and viruses’ geographic ranges.

Mechanistic models allow us to incorporate nonlinear effects of temperature on multiple traits, measured in controlled laboratory experiments across a wide thermal gradient, to understand their combined effect on disease transmission. This approach is critical when making predictions for future climate regimes because thermal responses are almost always nonlinear, and therefore current temperature–transmission relationships may not extend into temperatures beyond those currently observed in the field. We use Bayesian inference to quantify uncertainty and to rigorously incorporate prior knowledge of mosquito thermal physiology to constrain uncertainty when data are sparse (Johnson et al., 2015). The mechanistic modeling approach also provides an independently generated, a priori prediction for the relationship between temperature and transmission to test with observational field data on human cases, allowing us to connect data across scales, from individual-level laboratory experiments, to population-level patterns of disease transmission, to climate-driven geographic variation across populations. Using this approach, we build mechanistic models for 10 vector–virus pairs by estimating thermal responses of the traits that drive transmission. We validate the models using observations of human cases in the US over space (county-level) and time (month-of-onset). The validation focuses on WNV because it is the most common of the diseases we investigated and has the most complete temperature-dependent trait data. Preliminary results of this study—the thermal responses for traits and relative R0 models—were included in a review and synthesis article that was published last year (Mordecai et al., 2019). The present publication presents the complete methods and results, describes the vector and pathogen ecology in more detail, and provides original analyses of human case data.

### Model overview

To understand the effect of temperature on transmission and to compare the responses across vector and virus species, we used R0—the basic reproduction number (Diekmann et al., 2010). We use R0 as a static, relative metric of temperature suitability for transmission that incorporates the nonlinear effects of constant temperature on multiple traits (Dietz, 1993; Mordecai et al., 2019; Rogers and Randolph, 2006) and is comparable across systems, rather than focusing on its more traditional interpretation as a threshold for disease invasion into a susceptible population. Temperature variation creates additional nonlinear effects on transmission (Huber et al., 2018; Lambrechts et al., 2011; Murdock et al., 2017; Paaijmans et al., 2010) that are not well-captured by R0, (Bacaër, 2007; Bacaër and Ait Dads, 2012; Bacaër and Guernaoui, 2006; Diekmann et al., 2010; Parham and Michael, 2010) but could be incorporated in future work by integrating the thermal performance curves fit here over the observed temperature regime.

The basic R0 model for mosquito-borne diseases, originally developed for malaria (Equation 1; Dietz, 1993), includes the following traits that depend on temperature (T): adult mosquito mortality rate (µ, the inverse of lifespan [lf]), biting rate (a, the inverse of the gonotrophic [oviposition] cycle duration), pathogen development rate (PDR, the inverse of the extrinsic incubation period: the time required for exposed mosquitoes to become infectious), and vector competence (bc, the proportion of exposed mosquitoes that become infectious), where all rates are measured in inverse days. Vector competence is the product of infection efficiency (c, the proportion of exposed mosquitoes that develop a disseminated infection) and transmission efficiency (b, the proportion of infected mosquitoes that become infectious, with virus present in saliva). Mosquito density (M) also depends on temperature but is not an organism-level trait that can be measured in a laboratory setting. Two parameters do not depend on temperature: host density (N) and the rate at which infected hosts recover and are no longer infectious (r).

$$
BasicR_{0}:R_{0}(T)= (\frac{a(T)^{2}bc(T)e^{− \frac{\mu(T)}{PDR(T)}}M(T)}{N r \mu(T)})^{1/2}
$$

Because host density (N) and recovery rate (r) are not temperature-dependent, we omit them from our model (Equation 2), which isolates the effect of temperature on transmission (see explanation of ‘relative R0’ versus absolute R0 below). As in previous work (Johnson et al., 2015; Mordecai et al., 2019; Mordecai et al., 2017; Mordecai et al., 2013; Parham and Michael, 2010; Shocket et al., 2018; Tesla et al., 2018), we extend the basic R0 model to account for the effects of temperature on mosquito density (M) via additional temperature-sensitive life history traits (Equation 2): fecundity (as eggs per female per day, EFD), egg viability (proportion of eggs hatching into larvae, EV), proportion of larvae surviving to adulthood (pLA), and mosquito development rate (MDR, the inverse of the development period).

$$
FullR_{0}:R_{0}(T)= (\frac{a(T)^{2}bc(T)e^{− \frac{\mu(T)}{PDR(T)}}EFD(T)EV(T)pLA(T)MDR(T)}{\mu(T)^{3}})^{1/2}
$$

Fecundity data were only available as eggs per female per gonotrophic cycle (EFGC; for Cx. pipiens) or eggs per raft (ER; for Cx. quinquefasciatus). Thus, we further modified the model to obtain the appropriate units for fecundity: we added an additional biting rate (a) term to the numerator (to divide by the length of the gonotrophic cycle, Equations A1 and A2) and for Cx. quinquefasciatus we also added a term for the proportion of females ovipositing (pO; Equation A2).

We parameterized the full temperature-dependent R0 model (Equation 2) for each relevant vector–virus pair using previously published data. We conducted a literature survey to identify studies that measured the focal traits at three or more constant temperatures in a controlled laboratory experiment. From these data, we fit thermal responses for each trait using Bayesian inference. This approach allowed us to quantify uncertainty and formally incorporate prior data (Johnson et al., 2015) to constrain fits when data for the focal species were sparse or only measured on a limited portion of the temperature range (see Material and Methods for details).

For each combination of trait and species, we selected the most appropriate of three functional forms for the thermal response. As in previous work (Johnson et al., 2015; Mordecai et al., 2019; Mordecai et al., 2017; Mordecai et al., 2013; Shocket et al., 2018; Tesla et al., 2018), we fit traits with a symmetrical unimodal thermal response with a quadratic function (Equation 3) and traits with an asymmetrical unimodal thermal response with a Briére function (Briere et al., 1999; Equation 4). For some asymmetrical responses (e.g. pathogen development rate [PDR] for most vector–virus pairs), we did not directly observe a decrease in trait values at high temperatures due to a limited temperature range. In these cases, we chose to fit a Briére function based on previous studies with wider temperature ranges (Mordecai et al., 2017; Mordecai et al., 2013; Paull et al., 2017; Shocket et al., 2018) and thermal biology theory (Amarasekare and Savage, 2012); the upper thermal limit for these fits did not limit transmission in the R0 models, and therefore did not impact the results. Unlike in previous work, lifespan data for all vectors here exhibited a monotonically decreasing thermal response over the range of experimental temperatures available. We fit these data using a piecewise linear function (Equation 5) that plateaued at the coldest observed data point. By assuming a plateau, rather than extrapolating that lifespan continues to increase at temperatures below those measured in the laboratory, this approach is conservative, ensuring that lifespan was not a major driver of the temperature-dependence of R0 at temperatures where it was not measured and that the R0 models were instead constrained at reasonable temperatures by other traits. It is also consistent with the observed natural history of two of the vector species. To overwinter, Cx. pipiens and Cx. tarsalis enter reproductive diapause and hibernate (Nelms et al., 2013; Vinogradova, 2000), and Cx. pipiens can survive temperatures at or near freezing (0°C) for several months (Vinogradova, 2000). Cx. quinquefasciatus enters a non-diapause quiescent state (Diniz et al., 2017; Nelms et al., 2013) and is likely less tolerant of cold stress, but we wanted a consistent approach across models and other traits constrained the lower thermal limit of the Cx. quinquefasciatus R0 model to realistic temperatures. All vectors are likely to exhibit decreased lifespans at extremely low temperatures (near or below 0°C), limiting the accuracy of our inferred lifespan thermal performance curve at these temperatures.

$$
Quadraticfunction:f(T)= −q(T−T_{min})(T−T_{max})
$$



$$
Brie´refunction:f(T)= q⋅T(T−T_{min})\sqrt{(T_{max}−T)}
$$



$$
Linearfunction:f(T)= −mT+z
$$

In the quadratic and Briére functions of temperature (T), the trait values depend on a lower thermal limit (Tmin), an upper thermal limit (Tmax), and a scaling coefficient (q). In the linear function, the trait values depend on a slope (m) and intercept (z).

The fitting via Bayesian inference produced posterior distributions for each parameter in the thermal response functions (Equations 3, 4, 5) for each trait–species combination. These posterior distributions represent the estimated uncertainty in the parameters. We used these parameter distributions to calculate distributions of expected mean thermal performance functions for each trait over a temperature gradient (from 1°C to 45°C by 0.1°C increments). Then we substituted these samples from the distributions of the thermal responses for each trait into Equation 2 to calculate the posterior distributions of predicted R0 over this same temperature gradient for each vector–virus pair (see Material and methods and Appendix 1 for details). Thus, the estimated uncertainty in the thermal response of each trait is propagated through to R0 and combined to produce the estimated response of R0 to temperature, including the uncertainty in R0(T).

Because the magnitude of realized R0 depends on system-specific factors like breeding habitat availability, reservoir and human host availability, vector control, species interactions, and additional climate factors, we focused on the relative relationship between R0 and temperature (Mordecai et al., 2019). We rescaled the R0 model results to range from 0 to 1 (i.e. ‘relative R0’), preserving the temperature-dependence (including the absolute thermal limits and thermal optima) while making each model span the same scale. To compare trait responses and R0 models, we quantify three key temperature values: the optimal temperature for transmission (Topt) and the lower and upper thermal limits (Tmin and Tmax, respectively) where temperature is predicted to prohibit transmission (R0 = 0).

## Results

### Trait thermal responses

We fit thermal response functions from empirical data for all of the vector and virus traits that affect transmission for which data were available (Figure 1 and Appendix 1—table 1). All mosquito traits were temperature-sensitive (three main Culex species: Figure 3, Figure 4; Ae. taeniorhynchus, Ae. triseriatus, Ae. vexans, Cx. theileri, and Cs. melanura: Appendix 1—figure 1). For most species, the extensive data for larval traits (mosquito development rate [MDR] and survival [pLA]) produced clear unimodal thermal responses with relatively low uncertainty (Figure 3A,B, Appendix 1—figure 1A,B). For biting rate (a) and fecundity traits (proportion ovipositing [pO], eggs per female per gonotrophic cycle [EFGC], or per raft [ER], and egg viability [EV]), trait data were often more limited and fits were more uncertain, but still consistent with the expected unimodal thermal responses based on previous studies (Mordecai et al., 2017; Mordecai et al., 2013; Paull et al., 2017; Shocket et al., 2018) and theory (Amarasekare and Savage, 2012; Figure 3C, Figure 4, Appendix 1—figure 1C-F). However, adult lifespan (lf) data clearly contrasted with expectations from previous studies of more tropical mosquitoes. Lifespan (lf) decreased linearly over the entire temperature range of available data (coldest treatments: 14–16°C, Figure 3D; 22°C, Appendix 1—figure 1D) instead of peaking at intermediate temperatures (e.g. previously published optima for more tropical species: 22.2–23.4°C) (Johnson et al., 2015; Mordecai et al., 2017; Mordecai et al., 2013; Shocket et al., 2018; Tesla et al., 2018).

![Figure 3.](https://cdn.elifesciences.org/articles/58511/elife-58511-fig3-v1.jpg)

**Figure 3.:** The thermal responses of mosquito traits for the North American vectors of West Nile virus: Culex pipiens (dark grey), Cx. quinquefasciatus (red), and Cx. tarsalis (blue). (A) Mosquito development rate (MDR), (B) larval-to-adult survival (pLA), (C) biting rate (a), and (D) adult lifespan (lf). Points without error bars are reported means from single studies; points with error bars are averages of means from multiple studies (+ / - standard error, for visual clarity only; thermal responses were fit to reported means, see Appendix 1—figures 2, 3, 4, 5). Solid lines are posterior means; shaded areas are 95% credible intervals of the trait mean. See Appendix 1—figure 1 for thermal responses for Aedes taeniorhynchus, Ae. triseriatus, Ae. vexans, and Culiseta melanura. The mean thermal responses for these traits were printed in Mordecai et al., 2019 (as part of Figure 3 in that paper) without the trait data and 95% CIs, and along with thermal responses for six other vectors. See Appendix 1—tables 2, 3, 6 for data sources and Appendix 1—tables 7, 8, 9 for priors.

![Figure 4.](https://cdn.elifesciences.org/articles/58511/elife-58511-fig4-v1.jpg)

**Figure 4.:** The thermal responses of mosquito traits for the primary vectors of West Nile virus: Culex pipiens (dark grey) and Cx. quinquefasciatus (red). (A) Proportion ovipositing (pO), (B) fecundity (as eggs per female per gonotrophic cycle [EFGC] in Cx. pipiens, and eggs per raft, [ER] in Cx. quinequefasciatus), and (C) egg viability (EV). Points without error bars are reported means from single studies; points with error bars are averages of means from multiple studies (+ / - standard error, for visual clarity only; thermal responses were fit to reported means, see Appendix 1—figure 6). Solid lines are posterior distribution means; shaded areas are 95% credible intervals of the trait mean. See Appendix 1—figure 1 for thermal responses for Ae. vexans, Cx. theileri, and Culiseta melanura. The mean thermal responses for these traits were printed in Mordecai et al., 2019 (as part of Figure 3 in that paper) without the trait data and 95% CIs, and along with thermal responses for six other vectors. See Appendix 1—table 2 for data sources and Appendix 1—table 7 for priors.

The thermal responses for pathogen development rate (PDR) were similar among most vector–virus pairs (Figure 5), with a few notable exceptions: WNV in Cx. quinquefasciatus had a warmer lower thermal limit (Figure 5A); WNV in Cx. univittatus had a cooler optimum and upper thermal limit (Figure 5A); and SINV in Ae. taeniorhynchus had limited data that indicated very little response to temperature (Figure 5C). By contrast, the thermal response of vector competence (bc) and its component traits varied substantially across vectors and viruses (Figure 6). For example, infection efficiency (c) of Cx. pipiens peaked at warmer temperatures for WNV than for SINV (Figure 6A,G; 95% CIs: SINV = 14.1–30.5°C, WNV = 31.9–36.1°C), transmission efficiency (b) of Cx. tarsalis peaked at warmer temperatures for WNV and SLEV than for WEEV (Figure 6B,E,H; CIs: WEEV = 19.2–23.2°C, SLEV = 23.5–29.7°C, WNV = 23.9–29.3°C), and the lower thermal limit for vector competence (bc) for WNV was much warmer in Cx. pipiens than in Cx. univittatus (Figure 6C; CIs: Cx. univittatus = 1.5–7.1°C, Cx. pipiens = 15.0–17.9°C). Infection data (used to calculate pathogen development rate [PDR] and vector competence [bc]) for RVFV and SINV were only available in Ae. taeniorhynchus, a New World species that is not a known vector for these viruses in nature.

![Figure 5.](https://cdn.elifesciences.org/articles/58511/elife-58511-fig5-v1.jpg)

**Figure 5.:** Thermal responses of pathogen development rate (PDR). (A) West Nile virus in Culex pipiens (dark grey), Cx. quinquefasciatus (red), Cx. tarsalis (blue), and Cx. univitattus (orange). (B) Three viruses in Cx. tarsalis: West Nile virus (same as in A, blue), Western Equine Encephalitis virus (light blue), and St. Louis Encephalitis virus (dark blue). (C) Eastern Equine Encephalitis virus in Aedes triseriatus (violet), Rift Valley Fever virus in Ae. taeniorhynchus (light green), Sindbis virus in Ae. taeniorhynchus (dark green). We did not fit a thermal response for Sindbis virus in Ae. taeniorhynchus because the limited data responded weakly to temperature and did not match our priors. Points without error bars are reported means from single studies; points with error bars are averages of means from multiple studies (+ / - standard error, for visual clarity only; thermal responses were fit to reported means, see Appendix 1—figure 7). Solid lines are posterior distribution means; shaded areas are 95% credible intervals of the trait mean. The mean thermal responses for this trait were printed in Mordecai et al., 2019 (as part of Figure 4 in that paper) without the trait data and 95% CIs, combined into a single panel, and along with thermal responses for six other vector-pathogen pairs. See Appendix 1—table 5 for data sources and Appendix 1—table 8 for priors.

![Figure 6.](https://cdn.elifesciences.org/articles/58511/elife-58511-fig6-v1.jpg)

**Figure 6.:** Thermal responses of infection efficiency (c, # infected / # exposed; first column), transmission efficiency (b, # transmitting / # infected; second column) or vector competence (bc, # infected / # exposed; third column) for vector–virus pairs. First row (A,B,C): West Nile virus in Culex pipiens (dark grey), Cx. tarsalis (blue), and Cx. univitattus (yellow/orange). Second row: (D,E,F) Western Equine Encephalitis virus in Cx. tarsalis (light blue). Third row (G,H,I): Sindbis virus in Aedes taeniorhynchus (dark green), Sindbis virus in Cx. pipiens (light gray), St. Louis Encephalitis virus in Cx. tarsalis (dark blue), Eastern Equine Encephalitis virus in Ae. triseriatus (violet), and Rift Valley Fever virus in Ae. taeniorhynchus (light green). Points are means of replicates from single or multiple studies (+ / - standard error, for visual clarity only; thermal responses were fit to replicate-level data, see Appendix 1—figures 8 and 9). Solid lines are posterior distribution means; shaded areas are 95% credible intervals of the trait mean. The mean thermal responses for these traits were printed in Mordecai et al., 2019 (as part of Figure 4 in that paper) without the trait data and 95% CIs, combined into fewer panels, and along with thermal responses for six other vector-pathogen pairs. See Appendix 1—table 4 for data sources and Appendix 1—table 8 for priors.

### Temperature-dependent R0 models

Relative R0 responded unimodally to temperature for all the vector–virus pairs, with many peaking at fairly cool temperatures (medians: 22.7–26.0°C, see Table 2 for CIs; Figure 7). The lower thermal limits (medians: 8.7–19.0°C, see Table 2 for CIs; Figure 7) were more variable than the optima or the upper thermal limits (medians: 31.9–37.8°C, see Table 2 for CIs; Figure 7), although confidence intervals overlapped in most cases because lower thermal limits also had higher uncertainty (Figure 7). The Ae. taeniorhynchus models (both unnatural vector-pathogen pairs) were clear outliers, with much warmer distributions for the upper thermal limits, and optima that trended warmer as well.

![Figure 7.](https://cdn.elifesciences.org/articles/58511/elife-58511-fig7-v1.jpg)

**Figure 7.:** Posterior mean relative R0 for (A) West Nile virus (WNV) in Culex pipiens (dark grey), Cx. tarsalis (blue), Cx. quinquefasciatus (red), and Cx. univitattus (orange); (B) three viruses in Cx. tarsalis: WNV (same as in A, blue), Western Equine Encephalitis virus (WEEV, light blue), and St. Louis Encephalitis virus (SLEV, dark blue); (C) Sindbis virus (SINV) in Aedes taeniorhynchus (dark green) and Cx. pipiens (light grey), Rift Valley Fever virus (RVFV) in Ae. taeniorhynchus (light green), and Eastern Equine Encephalitis virus (EEEV) in Ae. triseriatus (violet). (D) Posterior median and uncertainty estimates for the lower thermal limit, optimum, and upper thermal limit. Points show medians, thick lines show middle 50% density, thin lines show 95% credible intervals. Models are ordered by increasing median optimal temperature. The thermal responses for R0 were printed in Mordecai et al., 2019 (as Figure 2 in that paper, reproduced here as Appendix 1—table 10), combined into two total panels and along with six other vector-pathogen pairs. See Appendix 1—figure 21 for histograms of lower thermal limit, optimum, and upper thermal limit for each model.

**Table 2.**
 Thermal optima and limits for transmission of mosquito-borne pathogens.Median temperature of the lower thermal limit (Tmin), optimum, and upper thermal limit (Tmax), with 95% credible intervals in parentheses. A version of this table (without thermal breadth, different order of R0 models) was published in Mordecai et al., 2019 (Table 2 in that paper).


<table>
  <thead>
    <tr>
      <th>R0 Model</th>
      <th>Tmin (°C)</th>
      <th>Optimum (°C)</th>
      <th>Tmax (°C)</th>
      <th>Thermal breadth (°C)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>From this study:</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>EEEV in Ae. triseriatus</td>
      <td>11.7 (8.8–16.3)</td>
      <td>22.7 (22.0–23.6)</td>
      <td>31.9 (31.1–33.0)</td>
      <td>20.0 (15.4–23.0)</td>
    </tr>
    <tr>
      <td>WEEV in Cx. tarsalis</td>
      <td>8.6 (6.3–13.0)</td>
      <td>23.0 (22.0–24.7)</td>
      <td>31.9 (30.3–35.2)</td>
      <td>23.3 (18.2–27.0)</td>
    </tr>
    <tr>
      <td>SINV in Cx. pipiens</td>
      <td>9.4 (6.9–13.3)</td>
      <td>23.2 (21.7–24.6)</td>
      <td>33.8 (28.2–37.0)</td>
      <td>23.8 (17.3–28.6)</td>
    </tr>
    <tr>
      <td>WNV in Cx. univittatus</td>
      <td>11.0 (8.0–15.3)</td>
      <td>23.8 (22.7–25.0)</td>
      <td>33.6 (31.2–36.9)</td>
      <td>22.5 (18.2–26.3)</td>
    </tr>
    <tr>
      <td>WNV in Cx. tarsalis</td>
      <td>12.1 (9.6–15.2)</td>
      <td>23.9 (22.9–25.9)</td>
      <td>32.0 (30.6–38.6)</td>
      <td>20.1 (16.3–26.7)</td>
    </tr>
    <tr>
      <td>SLEV in Cx. tarsalis</td>
      <td>12.9 (11.0–14.8)</td>
      <td>24.1 (23.1–26.0)</td>
      <td>32.0 (30.6–38.5)</td>
      <td>19.2 (16.5–25.6)</td>
    </tr>
    <tr>
      <td>WNV in Cx. pipiens</td>
      <td>16.8 (14.9–17.8)</td>
      <td>24.5 (23.6–25.5)</td>
      <td>34.9 (32.9–37.6)</td>
      <td>18.2 (15.8–21.2)</td>
    </tr>
    <tr>
      <td>WNV in Cx. quinquefasciatus</td>
      <td>19.0 (14.1–20.9)</td>
      <td>25.2 (23.9–27.1)</td>
      <td>31.8 (31.1–32.2)</td>
      <td>12.7 (10.6–17.6)</td>
    </tr>
    <tr>
      <td>RVFV in Ae. taeniorhynchus</td>
      <td>10.6 (8.6–14.4)</td>
      <td>25.9 (23.8–27.1)</td>
      <td>37.8 (34.4–39.1)</td>
      <td>27.0 (21.8–29.7)</td>
    </tr>
    <tr>
      <td>SINV in Ae. taeniorhynchus</td>
      <td>9.7 (8.3–13.6)</td>
      <td>26.0 (23.9–27.3)</td>
      <td>37.8 (34.4–39.2)</td>
      <td>27.7 (22.6–30.0)</td>
    </tr>
    <tr>
      <td>From previous studies:</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Falciparum malaria (Johnson et al., 2015)</td>
      <td>19.1 (16.0–23.2)</td>
      <td>25.4 (23.9–27.0)</td>
      <td>32.6 (29.4–34.3)</td>
      <td>13.2 (8.3–17.1)</td>
    </tr>
    <tr>
      <td>DENV in Ae. albopictus (Mordecai et al., 2017)</td>
      <td>16.2 (13.0–19.8)</td>
      <td>26.4 (25.4–27.6)</td>
      <td>31.4 (29.5–34.0)</td>
      <td>15.2 (11.2–19.3)</td>
    </tr>
    <tr>
      <td>Ross River virus (Shocket et al., 2018)</td>
      <td>17.0 (15.8–18.0)</td>
      <td>26.4 (26.0–26.6)</td>
      <td>31.4 (30.4–33.0)</td>
      <td>14.2 (12.8–16.2)</td>
    </tr>
    <tr>
      <td>ZIKV in Ae. aegypti (Tesla et al., 2018)</td>
      <td>22.8 (20.5–23.8)</td>
      <td>28.9 (28.2–29.6)</td>
      <td>34.5 (34.1–36.2)</td>
      <td>11.7 (10.4–14.5)</td>
    </tr>
    <tr>
      <td>DENV in Ae. aegypti (Mordecai et al., 2017)</td>
      <td>17.8 (14.6–21.2)</td>
      <td>29.1 (28.4–29.8)</td>
      <td>34.5 (34.1–35.8)</td>
      <td>16.7 (13.2–20.2)</td>
    </tr>
  </tbody>
</table>

Differences in relative R0 stemmed from variation both in vector traits (e.g. in Figure 7A, with WNV in different vector species) and in virus infection traits (e.g. in Figure 7B, with different viruses in Cx. tarsalis). The upper thermal limit was warmer for WNV transmitted by Cx. pipiens (34.9°C [CI: 32.9–37.5°C]) than by Cx. quinquefasciatus (31.8°C [CI: 31.1–32.2°C]), counter to the a priori prediction based on the higher-latitude range of Cx. pipiens in North America, South America, and Europe (Figure 2). This result implies that warming from climate change may differentially impact transmission by these two vectors. Additionally, the lower thermal limit for WNV varied widely (but with slightly overlapping 95% CIs) across different vector species (Figure 7D), from 19.0°C (14.2–21.0°C) in Cx. quinquefasciatus to 16.8°C (14.9–17.8°C) in Cx. pipiens to 12.2°C (9.7–15.3°C) in Cx. tarsalis to 11.1°C (8.1–15.4°C) in Cx. univittatus (an African and Eurasian vector; Table 2). Based on these trends in the thermal limits of R0, the seasonality of transmission and the upper latitudinal and elevational limits could vary for WNV transmitted by these different species.

Different traits determined the lower and upper thermal limits and optimum for transmission across vector–virus pairs. The lower thermal limit for transmission was most often determined by pathogen development rate (PDR; WNV and SLEV in Cx. tarsalis, WNV in Cx. quinquefasciatus) or biting rate (a; WNV in Cx. univitattus, WEEV in Cx. tarsalis, EEEV in Ae. triseriatus, RVFV and SINV in Ae. taeniorhynchus, SINV in Cx. pipiens; Appendix 1—figures 12–20), which tend to respond asymmetrically to temperature, with high optima and low performance at low temperatures. However, vector competence (bc) determined the lower limit for WNV in Cx. pipiens (Appendix 1—figure 11). The upper thermal limit was determined by biting rate (a) for the three Cx. tarsalis models and by adult lifespan (lf) for all others, although proportion ovipositing (pO) was also important for WNV in Cx. quinquefasciatus (Appendix 1—figures 11–20). In all models, lifespan (lf) and biting rate (a) had the strongest impact on the optimal temperature for transmission, with biting rate increasing transmission at low temperatures and lifespan decreasing transmission at high temperatures (Appendix 1—figures 11–20). This result is consistent with previous mechanistic models of tropical mosquito-borne diseases, despite the qualitative difference in the shape of the lifespan thermal response between those tropical mosquitoes and the more temperate mosquitoes investigated here (Johnson et al., 2015; Mordecai et al., 2017; Mordecai et al., 2013; Shocket et al., 2018; Tesla et al., 2018).

### Model validation with human case data

We validated the R0 models for WNV with independent data on human cases because the temperature-dependent trait data for those models were relatively high quality and because human case data were available from the Centers for Disease Control and Prevention across a wide climatic gradient in the contiguous United States. We averaged county-level incidence and mean summer temperatures across the entire period from 2001 to 2016 to estimate the impact of temperature over space, while ignoring interannual variation in disease that is largely driven by changes in host immunity and drought (Paull et al., 2017). We used generalized additive models (GAMs, which produce flexible, smoothed responses) to ask: does average incidence respond unimodally to mean summer temperature? If so, what is the estimated optimal temperature for transmission? Can we detect upper or lower thermal limits for transmission? Incidence of human neuroinvasive West Nile disease responded unimodally to average summer temperature and peaked at 24°C (23.5–24.2°C depending on the spline settings; Figure 8, Appendix 1—figure 24), closely matching the optima from the mechanistic models for the three North American Culex species (23.9–25.2°C; Table 2). However, the human disease data did not show evidence for lower or upper thermal limits: mean incidence remained positive and with relatively flat slopes below ~19°C and above ~28°C, although sample size was very low above 28°C and below 15°C resulting in wide confidence intervals (Figure 8, Appendix 1—figure 24).

![Figure 8.](https://cdn.elifesciences.org/articles/58511/elife-58511-fig8-v1.jpg)

**Figure 8.:** Grey line: predicted mean incidence from a generalized additive model (GAM) fit to county-level data (n = 3109) of mean temperature from May-September and incidence of neuroinvasive West Nile disease per 1000 people, both averaged from 2001 to 2016. Black points: mean incidence (with standard error bars) for bins of 42 counties (for visual clarity). See Appendix 1—figure 24 for fits across a range of smoothing parameters. See Appendix 1—figure 25 for LOESS (moving average) fits of the data. A version of the LOESS analysis was published as Figure S3 in Mordecai et al., 2019.

We used national month-of-onset data for WNV, EEEV, and SLEV to ask: is the seasonality of incidence consistent with our models for temperature-dependent transmission? The month-of-onset for cases of WNV was consistent with predicted transmission, R0(T) (Figure 9). As expected (based on previous studies and the time required for mosquito populations to increase, become infectious, and bite humans, and for humans to present symptoms and seek medical care [Mordecai et al., 2017; Shocket et al., 2018]), there was a 2-month lag between initial increases in R0(T) and incidence: cases began rising in June to the peak in August. The dramatic decline in transmission between September and October corresponds closely to the predicted decline in relative R0, but without the expected two-month lag. In general, the seasonal patterns of SLEV and EEEV incidence were similar to WNV, but differed by three orders of magnitude from ~20,000 cases of WNV to ~40–50 cases of EEEV and SLEV during the peak month (Figure 9). However, transmission of SLEV and EEEV are predicted to begin increasing 1 month earlier than WNV (March versus April, Figure 9), because the mechanistic models predict that the lower thermal limits for SLEV and EEEV are cooler than those for WNV in two of the three North American vectors (Cx. pipiens and Cx. quinquefasciatus, Figure 7). The month-of-onset data partially support this prediction, as cases of SLEV (but not EEEV) disease begin to increase earlier in the year than WNV, relative to the summer peak.

![Figure 9.](https://cdn.elifesciences.org/articles/58511/elife-58511-fig9-v1.jpg)

**Figure 9.:** Incidence (solid lines) lags behind predicted temperature-dependent R0 (dashed lines) for human cases of neuroinvasive disease caused by West Nile virus (WNV, black), St. Louis encephalitis virus (SLEV, dark gray), and Eastern Equine Encephalitis virus (EEEV, light gray) by 2 months. This lag matches patterns in other mosquito-borne diseases and is caused by the time required for mosquito populations to increase, become infectious, and bite humans, and for humans to present symptoms and seek medical care. However, the predicted lag is not present at the end of the transmission season in October, when R0(T) and incidence decline in tandem.

## Discussion

As the climate changes, it is critical to understand how changes in temperature will affect the transmission of mosquito-borne diseases. Toward this goal, we developed temperature-dependent, mechanistic transmission models for 10 vector–virus pairs. The viruses—West Nile virus (WNV), St. Louis Encephalitis virus (SLEV), Eastern and Western Equine Encephalitis viruses (EEEV and WEEV), Sindbis virus (SINV), and Rift Valley fever virus (RVFV)—sustain substantial transmission in temperate areas (except RVFV), and are transmitted by shared vector species, including Cx. pipiens, Cx. quinquefasciatus, and Cx. tarsalis (except EEEV; Figure 1). Although most traits responded unimodally to temperature, as expected (Johnson et al., 2015; Mordecai et al., 2019; Mordecai et al., 2017; Mordecai et al., 2013; Shocket et al., 2018; Tesla et al., 2018), lifespan decreased linearly with temperature over the entire temperature range of available data (>14°C) for these Culex vectors (Figure 3). Transmission responded unimodally to temperature, with the thermal limits and optima for transmission varying among some of the focal mosquito and virus species (Figure 7, Table 2), largely due to differences in the thermal responses of mosquito biting rate, lifespan, vector competence, and pathogen development rate. Human case data for WNV disease across the US exhibited a strong unimodal thermal response (Figure 8), and month-of-onset data for WNV, SLEV, and EEEV were largely consistent with the predicted seasonality of transmission (Figure 9). Thus, the mechanistic models captured geographical and seasonal patterns of human incidence, despite the complexity of the enzootic cycles and spillover into humans. Our analysis was somewhat limited by the lack of data for several trait-species combinations, or by data that were sparse, particularly at high temperatures. However, our key results—maximal transmission at intermediate temperatures—are unlikely to change, and underscore the importance of considering unimodal thermal responses when predicting how climate change will impact mosquito-borne disease transmission.

The monotonically decreasing thermal responses of lifespan (lf) within the range of the available experimental data for these more temperate mosquitoes (Figure 3D) contrast with the clearly unimodal responses of more tropical species (Mordecai et al., 2019; Mordecai et al., 2017; Mordecai et al., 2013; Shocket et al., 2018). This contrast may reflect differing thermal physiology between species that use diapause or quiescence, two forms of dormancy, to persist over winter and those that do not (Diniz et al., 2017; Nelms et al., 2013; Vinogradova, 2000). Both Cx. pipiens and Cx. tarsalis diapause (Nelms et al., 2013; Vinogradova, 2000), and Cx. pipiens can survive temperatures at or near freezing (0°C) for several months (Vinogradova, 2000). Cx. quinquefasciatus enters a non-diapause quiescent state (Diniz et al., 2017; Nelms et al., 2013). Ae. albopictus, a species that occurs in both tropical and temperate zones, exhibits a latitudinal gradient in the United States in which more temperate populations diapause while sub-tropical populations do not (Urbanski et al., 2010). Experiments could test this hypothesis by measuring whether the functional form of the thermal response for lifespan differs between northern (diapausing) and southern (non-diapausing) US Ae. albopictus populations. Despite the difference in the shape of the thermal response, lifespan played a similarly important role here as in previous studies of mosquito-borne pathogens, strongly limiting transmission at high temperatures (Appendix 1—figures 11–20). Nonetheless, the thermal responses for lifespan here ultimately promote higher transmission at relatively cool temperatures because unlike in more tropical species, lifespan did not decline at cool temperatures within the range measured (>14°C). Given the lack of rigorous trait data, we cannot be certain of the shape of the thermal response of lifespan (lf) below 14°C, although it is almost certainly unimodal, especially at more extreme temperatures expected to be fatal even for diapausing mosquitoes (i.e. below 0°C). Our decision to assume lifespan (lf) plateaued at temperatures below the observed data was based on vector natural history (Vinogradova, 2000) and intended to be conservative. This approach ensured that lifespan was not a major driver of the temperature-dependence of R0 at temperatures where it was not measured and that R0 was instead constrained by other traits. Accordingly, our functions for lifespan (lf) do not represent the real quantitative thermal responses below the coldest observations, which limits their utility for other applications, such as predicting survival at cold temperatures and lower thermal limits on survival.

Predicted transmission for many of the diseases in this study peaked at and extended to cooler temperatures than for previously studied diseases with more tropical distributions (see Figure 7 and Table 2 for 95% credible intervals)(Mordecai et al., 2019). Here, the optimal temperatures for transmission varied from 22.7–25.2°C (excluding Ae. taeniorhynchus models, Figure 7). By contrast, models predict that transmission peaks at 25.4°C for malaria (Johnson et al., 2015; Mordecai et al., 2013), 26.4°C for Ross River virus (Shocket et al., 2018) and dengue in Ae. albopictus (Mordecai et al., 2017), 28.9°C for Zika in Ae. aegypti (Tesla et al., 2018), and 29.1°C for dengue in Ae. aegypti (Mordecai et al., 2017). Models for several vector–virus pairs also had cooler lower thermal limits (medians: 8.7–19.0°C) than those of diseases with more tropical distributions (medians: 16.0–17.8°C)(Mordecai et al., 2019). In combination with similar upper thermal limits (see below), these patterns led to wider thermal breadths (18.2–27.7°C; Figure 7) for most of the viruses here compared to the more tropical pathogens (11.7–16.7°C), excepting WNV in Cx. quinquefasciatus (12.7°C), the vector most restricted to lower latitude, sub-tropical geographic areas (Figure 2). These results match a previous finding that temperate insects had wider thermal breadths than tropical insects (Deutsch et al., 2008), and may reflect thermal adaptation to greater variation in temperature in temperate areas compared to tropical areas (Sunday et al., 2011). Additionally, SINV—a virus with substantial transmission at very high latitudes in Finland (Adouchief et al., 2016)—had the second coolest lower thermal limit (Figure 7, Table 2). Further, lower latitude Cx. quinquefasciatus outperformed higher latitude Cx. pipiens at warmer temperatures for proportion ovipositing (pO; Figure 3A), while the reverse occurred at cooler temperatures for egg viability (EV; Figure 3C). Collectively, these results imply that, to some extent, measurements of physiological traits can predict geographic patterns of vectors or disease transmission at broad scales. However, geographic range differences (Figure 2) did not consistently predict variation in thermal responses among the Culex species in this study (e.g. biting rate [a, Figure 3C] and adult lifespan [lf, Figure 3D]), indicating that life history and transmission trait responses at constant temperatures do not always predict the geographic distributions of species. Instead, the ability to tolerate temperature extremes may limit species distributions more than their performance at average or constant temperatures (Overgaard et al., 2014). Moreover, although diseases like malaria and dengue are generally considered to be ‘tropical’, historically their distributions extended further into temperate regions (Brathwaite Dick et al., 2012; Hay et al., 2004). Thus, current distributions of disease may reflect a realized niche restricted by societal factors more than a fundamental niche based on ecological factors like temperature.

In contrast to the optima, lower thermal limits, and thermal breadths, the upper thermal limits for the vector–virus pairs in this study (31.9–34.9°C, excluding Ae. taeniorhynchus models; Figure 7D, Table 2) closely matched those of more tropical diseases (31.5–34.7°C) (Johnson et al., 2015; Mordecai et al., 2017; Mordecai et al., 2013; Shocket et al., 2018; Tesla et al., 2018). This similarity may arise because maximum summer temperatures in temperate areas can match or even exceed maximum temperatures in tropical areas (Sunday et al., 2011). Accordingly, there may be a fundamental upper thermal constraint on transmission that applies similarly to all mosquito-borne diseases, driven by short mosquito lifespans at high temperatures. The relatively high upper thermal limits in both Ae. taeniorynchus transmission models were driven by the thermal response of lifespan (lf), which was fit to few data points; more data are needed to determine whether it reflects the true thermal response in that species (Appendix 1—figure 1). These results indicate that as temperatures rise due to climate change, temperate diseases are unlikely to be displaced by warming alone, although they may also expand toward the poles, even as tropical diseases may expand farther into temperate zones.

Independent human case data support unimodal thermal responses for transmission and the importance of temperature in shaping geographic patterns of mosquito-borne disease. Human cases of WNV (Ahmadnejad et al., 2016; Hahn et al., 2015; Marcantonio et al., 2015; Platonov et al., 2008; Reisen et al., 2006; Semenza et al., 2016; Shand et al., 2016) and SINV (Brummer-Korvenkontio et al., 2002; Jalava et al., 2013) are often positively associated with temperature. Here, we found that incidence of neuroinvasive WNV disease peaked at intermediate mean summer temperatures (24°C) across counties in the US (Figure 8) that matched the optima predicted by our models. This result adds to prior evidence for reduced transmission of WNV (Mallya et al., 2018) and other mosquito-borne diseases (Gatton et al., 2005; Mordecai et al., 2013; Peña-García et al., 2017; Perkins et al., 2015; Shah et al., 2019) at high temperatures. Although we did not detect lower or upper thermal limits for West Nile neuroinvasive disease (Figure 8), this result is unsurprising based on fundamental differences between the types of temperature data used to parameterize and validate the models. The R0 model prediction is derived from data collected in a controlled laboratory environment at constant temperatures, while average incidence in the field reflects temperatures that vary at a variety of temporal scales (daily, seasonal, and interannual). Thus, we hypothesize that temperature variation over time may sustain transmission in regions with otherwise unsuitable mean summer temperatures by providing time windows that are suitable for transmission.

The temperature-dependent models also predict the general seasonality of human cases of WNV, EEEV, and SLEV (Figure 9). The 2-month lag between climate suitability and the onset of human cases, which matches previous results from other mosquito-borne diseases (Mordecai et al., 2017; Shocket et al., 2018), arises from the time following the onset of suitable conditions required for mosquito populations to increase (Stewart Ibarra et al., 2013), become infectious, and bite humans, and for humans to present symptoms and seek medical care (Hu et al., 2006; Jacups et al., 2008). Transmission of the more temperate viruses here may incur additional lags because human cases result from enzootic transmission, and multiple rounds of amplification within reservoir hosts may be required before prevalence is sufficiently high to spill over into humans. Additionally, as wild birds begin to migrate in late summer, both Cx. pipiens and Cx. tarsalis shift their feeding preferences from birds to humans, which should increase transmission to people later in the year (Kilpatrick et al., 2006). However, we found that cases decreased more quickly in autumn than expected from temperature effects alone. Human behavior may partially compensate for the shift in feeding preference and explain why the decrease of cases in autumn did not show the expected 2-month lag from temperature-dependent relative R0. For instance, if people wear clothing that exposes less skin and spend less time outdoors due to school schedules and changing daylight it may reduce contact with mosquitoes. Drought, precipitation, and reservoir and human immunity also strongly drive transmission of WNV (Ahmadnejad et al., 2016; Marcantonio et al., 2015; Paull et al., 2017; Shand et al., 2016) and may interact with temperature. SLEV, EEEV, and WEEV are less common in nature, and thus less well-studied, but the lower thermal limits in our study support previous findings that transmission of WEEV is favored over SLEV in cooler conditions (Hess et al., 1963). Additionally, the seasonal patterns of incidence data (Figure 9) provide some support for the model prediction that SLEV transmission is possible at cooler temperatures than WNV by North American vectors (Table 2). By contrast, mean temperature is not associated with outbreaks of RVFV, although they are highly predictable based on precipitation driven by El Niño–Southern Oscillation cycles (Anyamba et al., 2009; Linthicum et al., 1999). Thus, disease dynamics depend on the interaction between temperature and other environmental factors, and the relative importance of temperature versus other drivers varies across systems.

Most prior studies with mechanistic models for temperature-dependent transmission of WNV do not capture the unimodal thermal response that our mechanistic models predict and that we observe in the human case data (Table 3). Two previous models predicted that transmission of WNV would increase up to the warmest temperatures they considered, 28°C (Vogels et al., 2017) and 35°C (Kushmaro et al., 2015). In both cases, the vector daily survival rates estimated from lab experiments were far less sensitive to temperature than our measure of adult lifespan (lf), and neither model was validated with field data. A third study with models for Cx. pipiens, Cx. quiquefasciatus, and Cx. tarsalis, like our study, predicted unimodal thermal responses for transmission, with very similar optima but with lower thermal limits that were ~5°C warmer, resulting in much narrower thermal breadths (Appendix 1—figure 23; Paull et al., 2017). This previous set of models (Paull et al., 2017) was validated with annual, state-level WNV human case data (in contrast to our county-level data averaged over multiple years), and detected a positive effect of temperature, with no decline at high temperatures (Paull et al., 2017). The best spatial and temporal scales for validating temperature-dependent transmission models and detecting the impacts of temperature remain an open question. For instance, different approaches may be necessary to detect thermal optima and thermal limits. Critically, differences in modeling and validation approaches can lead to strongly divergent conclusions and predictions for the impact of climate change.

**Table 3.**
 Predicted optima for transmission of West Nile virus.Predicted optima for transmission from this study and previous models. A version of this table (with R0 models for additional viruses and including thermal limits) was published in Mordecai et al., 2019 (as Table 3 in that paper).


<table>
  <thead>
    <tr>
      <th>R0 Model</th>
      <th>Optimum (°C)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>From this study:</td>
      <td></td>
    </tr>
    <tr>
      <td>WNV in Cx. pipiens</td>
      <td>24.5</td>
    </tr>
    <tr>
      <td>WNV in Cx. quinquefasciatus</td>
      <td>25.2</td>
    </tr>
    <tr>
      <td>WNV in Cx. tarsalis</td>
      <td>23.9</td>
    </tr>
    <tr>
      <td>WNV in Cx. univittatus</td>
      <td>23.8</td>
    </tr>
    <tr>
      <td>From previous studies:</td>
      <td></td>
    </tr>
    <tr>
      <td>WNV in Cx. pipiens (Paull et al., 2017)</td>
      <td>24.9</td>
    </tr>
    <tr>
      <td>WNV in Cx. quinquefasciatus (Paull et al., 2017)</td>
      <td>24.3</td>
    </tr>
    <tr>
      <td>WNV in Cx. tarsalis (Paull et al., 2017)</td>
      <td>24.9</td>
    </tr>
    <tr>
      <td>WNV in Cx. pipiens (Vogels et al., 2017)</td>
      <td>28</td>
    </tr>
    <tr>
      <td>WNV in Cx. pipiens molestus (Vogels et al., 2017)</td>
      <td>28</td>
    </tr>
    <tr>
      <td>WNV in Cx. and Ae. spp. (Kushmaro et al., 2015)</td>
      <td>35</td>
    </tr>
  </tbody>
</table>

Given the unimodal relationship between temperature and transmission of these temperate mosquito-borne pathogens, we expect climate warming to lead to predictable shifts in disease transmission (Lafferty, 2009; Lafferty and Mordecai, 2016; Ryan et al., 2015). Warming should extend the transmission season earlier into the spring and later into the fall and increase transmission potential in higher latitudes and altitudes, although this prediction may be impacted by changes in bird migrations. However, the thermal optima for these temperate vector–virus pairs are relatively cool, so in many locations, warming could result in summer temperatures that exceed the thermal optima for transmission more frequently, reducing overall transmission or creating a bimodal transmission season (Molnár et al., 2013). Based on the average summer temperature data (2001–2016) in our analysis (Figure 8), currently the majority of people (70%) and counties (68%) are below the optimal temperature for transmission (23.9°C, fit by the GAM). The numbers are similar when restricted to counties with observed West Nile virus cases: 69% and 70%, respectively. Thus, all else being equal, we might expect a net increase in transmission of West Nile virus in response to the warming climate, even as hot temperatures suppress transmission in some places. Still, warming is unlikely to eliminate any of these more temperate pathogens since the upper thermal limits for transmission are well above temperatures pathogens regularly experience in their current geographic ranges. More generally, our results raise concerns about the common practice of extrapolating monotonic relationships between temperature and disease incidence fit from observational data into warmer climate regimes to predict future cases (Marcantonio et al., 2015; Semenza et al., 2016).

While the data-driven models presented here represent the most comprehensive synthesis to date of trait thermal response data and their impact on transmission for these mosquito–pathogen systems with substantial transmission in temperate regions, additional temperature-dependent trait data would increase the accuracy and decrease the uncertainty in these models where data were sparse or missing. Our data synthesis and uncertainty analysis suggest prioritizing pathogen development rate (PDR) and vector competence (bc) data and biting rate (a) data because those thermal responses varied widely among vector–virus pairs and determined the lower thermal limits and optima for transmission in many models. Additionally, vector competence (bc) and/or pathogen development rate (PDR) data were missing in many cases (WNV in Cx. quinquefasciatus and Cx. modestus [an important vector in Europe], EEEV in Cs. melanura, RVFV in vectors from endemic areas, transmission efficiency [b] for SINV) or sparse (EEEV and WNV in Cx. univittatus), as were biting rate data (Cx. univittatus, RVFV vectors). Lifespan (lf) data—key for determining transmission optima and upper thermal limits—were the missing for Ae. triseriatus, Cs. melanura, Cx. univittatus, and RVFV vectors, and at temperatures below 14°C for all vector species, so it was unclear which functional form these thermal responses should take (monotonic, saturating, or unimodal). While the other mosquito demographic traits did not determine thermal limits for transmission in models here, fecundity (typically as eggs per female per day, EFD), larval-to-adult survival (pLA), and egg viability (EV) determined thermal limits for malaria (Mordecai et al., 2013) and Ross River virus (Shocket et al., 2018). Thus, more fecundity data (missing for Cx. tarsalis, Cx. univittatus, and Ae. triseriatus; sparse for Cx. pipiens and Cx. quinquefasciatus) would also increase our confidence in the models. New data are particularly important for RVFV: the virus has a primarily tropical distribution in Africa and the Middle East, but the model depends on traits measured in Cx. pipiens collected from temperate regions and infection traits measured in Ae. taeniorhynchus, a North American species. This substitution of a mosquito species that is not a naturally occurring vector could reduce the relevance and utility of this model. RVFV is transmitted by a diverse community of vectors across the African continent, but experiments should prioritize hypothesized primary vectors (e.g. Ae. circumluteolus or Ae. mcintoshi) or secondary vectors that already have partial trait data (e.g. Ae. vexans or Cx. theileri) (Braack et al., 2018; Linthicum et al., 2016). Although temperature itself does not predict the occurrence of RVFV outbreaks, it may affect the size of epidemics once they are triggered by precipitation. More generally, thermal responses may vary across vector populations (Kilpatrick et al., 2010) and/or virus isolates even within the same species. Several studies have found differences in thermal performance across different populations of the same mosquito species (Dodson et al., 2012; Mogi, 1992; Reisen, 1995; Ruybal et al., 2016) or pathogen strains (Kilpatrick et al., 2008), but this variation was not systematically associated with their thermal environments of origin. Accordingly, the potential for thermal adaption in mosquitoes and their pathogens remains an open question. Regardless, more data may improve the accuracy of all the models, even those without missing data.

Our trait-based R0 models effectively isolated the physiological effects of temperature on transmission. However, in nature many other environmental and biological factors also impact transmission of mosquito-borne disease. For example, potential factors include rainfall, habitat and land-use, reservoir host community composition, host immunity, viral and mosquito genotypes, mosquito microbiome, vector control efforts, vector behavior, and human behavior (Kilpatrick et al., 2010; Kilpatrick et al., 2006; Paull et al., 2017; Shocket et al., 2020; Vaidyanathan and Scott, 2007; Vazquez-Prokopec et al., 2010). Our analyses here suggest that temperature is important for shaping broad-scale spatial and seasonal patterns of disease when cases are averaged over time and space. Other factors may be more important at finer spatial and temporal scales, and explain additional variation in human cases. For instance, a study of WNV and two other (non-mosquito-borne) pathogens found that biotic factors were significant drivers of disease distributions at local scales, while climate factors were only significant drivers at larger regional scales (Cohen et al., 2016). Given that our R0 models for WNV predicted very similar thermal optima across three distantly-related vector species, it is likely that our results are generalizable to other temperate locations with the same vectors (e.g. parts of Europe with transmission by Cx. pipiens) at similarly broad spatial and temporal scales, even if the other factors influencing local-scale patterns are quite different than in the US.

As carbon emissions continue to increase and severe climate change becomes increasingly inevitable (Intergovernmental Panel on Climate Change, 2014), it is critical that we understand how temperature change will affect the transmission of mosquito-borne diseases in a warmer future world. While data gaps are still limiting, the mechanistic, trait-based approach presented here is powerful for predicting similarities and differences across vectors and viruses and for making predictions for the impact of climate change (Mordecai et al., 2019). Accounting for the effects of temperature variation (Bernhardt et al., 2018; Lambrechts et al., 2011; Paaijmans et al., 2010) is an important next step for using these types of models to accurately predict transmission. In nature, mosquitoes and pathogens experience daily temperature variation that can dramatically alter performance compared to constant temperatures of the same mean (Lambrechts et al., 2011; Paaijmans et al., 2010). Rate summation is the most common method for predicting performance in variable temperatures based on experimental data at constant temperatures (Bernhardt et al., 2018; Lambrechts et al., 2011). This approach is ideal because mean temperature and daily temperature variation vary somewhat independently over space and time, and measuring vector and pathogen performance at sufficient combinations of both is logistically difficult. However, its accuracy for predicting mosquito and pathogen traits or mosquito-borne disease transmission has not been rigorously evaluated. Additionally, the potential for adaptive evolution to warmer climates is uncertain because of limited knowledge on the level of genetic variation in thermal responses for vectors or their pathogens within or between populations. Further, vectors and pathogens may experience different selective pressures, as mosquito populations may depend on either increased fecundity or longevity at high temperatures, while pathogens require longer vector lifespans (Mordecai et al., 2019). Thus, future trajectories of these diseases will depend not just on suitability of mean temperatures but also on temperature variation, thermal adaptation of vectors and viruses, land use (which governs mosquito–wildlife–human interactions), vector control activities, human and wildlife immune dynamics, and potential future emergence and spread of new vectors and viruses.

## Materials and methods

All analyses were conducted using R 3.1.3 (R Development Core Team, 2016).

### Vector species range maps

The distributions of Cx. pipiens and Cx. quinquefasciatus are georectified maps adapted from Farajollahi et al., 2011; Smith and Fonseca, 2004. The northern boundary of Cx. tarsalis was taken from Darsie and Ward, 2016. For the southern boundary, we drew a convex polygon using five datasets (Huerta Jiménez, 2018; López Cárdenas, 2018; Ortega Morales, 2018; Ponce García, 2018; Walter Reed Biosystematics Unit, 2018) in the Global Biodiversity Information Facility (https://www.gbif.org/).

### Temperature-dependent trait data

We found 38 studies with appropriate temperature-dependent trait data from controlled laboratory experiments (Paull et al., 2017; Reisen et al., 2006; Kilpatrick et al., 2008; Ruybal et al., 2016; Andreadis et al., 2014; Brust, 1967; Buth et al., 1990; Chamberlain and Sudia, 1955; Ciota et al., 2014; Cornel et al., 1993; Dodson et al., 2012; Dohm et al., 2002; Kramer et al., 1983; Li et al., 2017; Loetti et al., 2011; Lundström et al., 1990; Madder et al., 1983; Mahmood and Crans, 1997; Mahmood and Crans, 1998; McHaffey, 1972a; Mogi, 1992; Mpho et al., 2001; Mpho et al., 2002a; Mpho et al., 2002b; Nayar, 1972; Oda et al., 1980; Oda et al., 1999; Rayah and Groun, 1983; Reisen et al., 1992; Reisen et al., 1993; Reisen, 1995; Rueda et al., 1990; Shelton, 1973; Tekle, 1960; Teng and Apperson, 2000; Trpiš and Shemanchuk, 1970; Turell et al., 1985; Turell and Lundström, 1990; van der Linde TC de et al., 1990). When necessary, we digitized the data using Web Plot Digitizer (Rohatgi, 2018), a free online tool. When lifespan data were reported by sex, only female data were used. Vector competence trait data (b, c, or bc) were only included if time at sampling surpassed the estimated extrinsic incubation period (the inverse of PDR) at that temperature, which resulted in the exclusion of some studies (Fros et al., 2015; Vogels et al., 2016).

### Fitting thermal responses

We fit trait thermal responses with a Bayesian approach using the ‘r2jags’ package (Su and Yajima, 2009), an R interface for the popular JAGS program (Plummer, 2003) for the analysis of Bayesian graphical models using Gibbs sampling. It is a (near) clone of BUGS (Bayesian inference Using Gibbs Sampling) (Spiegelhalter et al., 2003). In JAGS, samples from a target distribution are obtained via Markov Chain Monte Carlo (MCMC). More specifically, JAGS uses a Metropolis-within-Gibbs approach, with an Adaptive Rejection Metropolis sampler used at each Gibbs step (for more information on MCMC algorithms see Gilks et al., 1998).

For each thermal response being fit to trait data, we visually identified the most appropriate functional form (quadratic, Briére, or linear; Equations 3–5) for that specific trait–species combination (Mordecai et al., 2019). For traits with ambiguous functional responses, we fit the quadratic and Briere and used the deviance information criterion (DIC) (Spiegelhalter et al., 2002) to pick the best fit. We assumed normal likelihood distributions with temperature-dependent mean values described by the appropriate function (Equations 3–5) and a constant standard deviation (σ) described by an additional fitted parameter (τ = 1/σ2). The 95% credible intervals in Figures 3–6 estimate the uncertainty in the mean thermal response.

We set all thermal response functions to zero when T < Tmin and T > Tmax (for Equation 3 and 4) or when T > -z/m (Equation 5) to prevent trait values from becoming negative. For traits that were proportions or probabilities, we also limited the thermal response functions at 1. For the linear thermal responses, we calculated the predicted thermal response in a piecewise manner in order to be conservative: for temperatures at or above the coldest observed data point, we used the trait values predicted by the fitted thermal response (i.e. the typical method); for temperatures below the coldest observed data point, we substituted the trait estimate at the coldest observed data point (i.e. forcing the thermal response to plateau, rather than continue increasing beyond the range of observed data).

For the fitting process, we ran three concurrent MCMC chains for 25,000 iterations each, discarding the first 5000 iterations for burn-in (convergence was checked visually). We thinned the resultant chains, saving every eighth step. These settings resulted in 7500 samples in the full posterior distribution that we kept for further analysis.

### Generating priors

We used data-informed priors to decrease the uncertainty in our estimated thermal responses and constrain the fitted thermal responses to be biologically plausible, particularly when data were sparse. These priors used our total dataset, which contained temperature-dependent trait data for all of the main species in the analysis (but with the focal species removed, see below), as well as from additional temperate Aedes and Culex species (Buth et al., 1990; Ciota et al., 2014; Kiarie-Makara et al., 2015; Madder et al., 1983; McHaffey, 1972b; McHaffey and Harwood, 1970; Mogi, 1992; Muturi et al., 2011; Oda et al., 1999; Oda et al., 1980; Olejnícek and Gelbic, 2000; Parker, 1982).

We fit each thermal response with a sequential two-step process, where both steps employed the same general fitting method (described above in Fitting Thermal Responses) but used different priors and data. In step 1, we generated high-information priors by fitting a thermal response to data from all species except the focal species of interest (i.e. a ‘leave-one-out’ approach). For example, for the prior for biting rate for Cx. pipiens, we used the biting rate data for all species except Cx. pipiens. For this step, we set general, low-information priors that represented minimal biological constrains on these functions (e.g. typically mosquitoes die if temperatures exceed 45°C, so all biological processes are expected to cease; Tmin must be less than Tmax). The bounds of these uniformly distributed priors were: 0 < Tmin < 24, 26 < Tmax < 45 (quadratic) or 28 < Tmax < 45 (Briére), 0 < q < 1,–10 < m < 10, and 0 < b < 250. Then in step 2, we fit a thermal response to data from the focal species using the high-information priors from step 1.

Because we cannot directly pass posterior samples from JAGS as a prior, we modified the results from step 1 to use them in step 2. We used the ‘MASS’ package (Venables and Ripley, 2002) to fit a gamma probability distribution to the posterior distributions for each thermal response parameter (Tmin, Tmax, and q [Equation 3 and 4]; or m and z [Equation 5]) obtained in step 1. The resulting gamma distribution parameters can be used directly to specify the priors in the JAGS model. Because the prior datasets were often very large, in many cases the priors were too strong and overdetermined the fit to the focal data. In a few other cases, we had philosophical reasons to strongly constrain the fit to the focal data even when they were sparse (e.g. to constrain Tmax to very high temperatures so that other traits with more information determine the upper thermal limit for R0). Thus, we deflated or inflated the variance as needed (i.e., we fixed the gamma distribution mean but altered the variance by adjusting the parameters that describe the distribution accordingly). See Appendix 1 for more details and specific variance modifications for each thermal response.

### Constructing R0 models

When data were missing for a vector–virus pair, we used two criteria to decide which thermal response to use as a substitute: 1) the ecological similarly (i.e. geographic range overlap) of species with available thermal responses, and 2) how restrictive the upper and lower bounds of the available thermal responses were. All else being equal, we chose the more conservative (i.e. least restrictive) option so that R0 would be less likely to be determined by trait thermal responses that did not originate from the focal species. See Appendix 1 for more information about specific models.

When there was more than one option for how to parameterize a model (e.g. vector competence data for WEEV in Cx. tarsalis were available in two forms: separately as b and c, and combined as bc), we calculated R0 both ways. The results were very similar, except for the model for RVFV with lifespan data from Cx. pipiens lifespan in place of Ae. taeniorhynchus (Appendix 1—figure 22). See Appendix 1 for sensitivity and uncertainty methods and Appendix 1—figures 11–20 for results.

### Model validation: spatial analysis

We obtained county-level neuroinvasive WNV disease data from 2001 to 2016 for the contiguous US (n = 3109) through the CDC’s county-level disease monitoring program (Centers for Disease Control and Prevention, 2018c). Data were available as total human cases per year, which we adjusted to average cases per 1000 people (using 2010 US county-level census data) to account for population differences. We averaged cases across years beginning with the first year that had reported cases in a given county to account for the initial spread of WNV and the strong impact of immunity on interannual variation (Paull et al., 2017). Ninety-eight percent of human cases of WNV in the US occur between June and October (data described below), and cases of mosquito-borne disease often lag behind temperature by 1–2 months (Shocket et al., 2018; Stewart Ibarra et al., 2013). Thus, we extracted monthly mean temperature data between the months of May–September for all years between 2001 and 2016 and averaged the data to estimate typical summer conditions for each county. Specifically, we took the centroid geographic coordinate for every county in the contiguous US with the ‘rgeos’ package Bivand and Rundel, 2012 and extracted corresponding historic climate data for monthly mean temperatures (Climate Research Unit 3.1 rasters) (Harris et al., 2014) from 0.5°2 cells (approximately 2500–3000 km2) using the ‘raster’ package (Hijmans, 2020). The monthly mean temperatures in this climate product are calculated by averaging daily mean temperatures at the station level (based on 4–8 observations per day at regular intervals) and interpolating these over a grid (World Meteorological Organization, 2009).

We fit a generalized additive model (GAM) for average incidence as a function of average summer temperature using the ‘mgcv’ package (Wood, 2006). We used a gamma distribution with a log-link function to restrict incidence to positive values and capture heteroskedasticity in the data (i.e. higher variance with higher predicted means), adding a small, near-zero constant (0.0001) to all incidence values to allow the log-transformation for counties with zero incidence. GAMs use additive functions of smooth predictor effects to fit responses that are extremely flexible in the shape of the response. We restricted the number of knots to minimize overfitting (k = 7; see Appendix 1—figure 24 for results across varying values of k). For comparison, we also used the ‘loess’ function in base R ‘stats’ package (R Development Core Team, 2016) to fit locally estimated scatterplot smoothing (LOESS) regressions of the same data. LOESS regression is a simpler but similarly flexible method for estimating the central tendency of data. See Appendix 1—figure 25 for LOESS model results. See Appendix 1—figure 26 for non-binned county-level data.

### Model validation: seasonality analysis

We calculated monthly temperature-dependent relative R0 to compare with month-of-onset data for neuroinvasive WNV, EEEV, and SLEV disease aggregated nationwide (the only spatial scale available) from 2001 to 2016 (Centers for Disease Control and Prevention, 2018c; Curren et al., 2018; Lindsey et al., 2018), using the same county-level monthly mean temperature data as above. For WNV, we used the subset of counties with reported cases (68% of counties). For SLEV and EEEV we used all counties from states with reported cases (16 and 20 states, respectively). We calculated a monthly R0(T) for each county, and then weighted each county R0(T) by its population size to calculate a national monthly estimate of R0(T). For WNV, the county-level estimates of R0(T) used models for three Culex species (Cx. pipiens, Cx. quinquefasciatus, and Cx. tarsalis) weighted according to the proportion of WNV-positive mosquitoes reported at the state level, reported in Paull et al., 2017. SLEV and EEEV both only had one R0 model. The estimated monthly temperature-dependent relative R0 values and month-of-onset data were compared visually.

### Availability of data and material

All data and code are available on Github in the following repository: https://github.com/mshocket/Six-Viruses-Temp (Shocket, 2020; copy archived at https://github.com/elifesciences-publications/Six-Viruses-Temp). All data and code are also available in the Dryad Data Repository.
