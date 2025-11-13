# Estimating the potential to prevent locally acquired HIV infections in a UNAIDS Fast-Track City, Amsterdam

## Authors

- Alexandra Blenkinsop<sup>1</sup> ([ORCID: 0000-0002-2328-8671](https://orcid.org/0000-0002-2328-8671)) †
- Mélodie Monod<sup>1</sup>
- Ard van Sighem<sup>3</sup> ([ORCID: 0000-0002-6656-0516](https://orcid.org/0000-0002-6656-0516))
- Nikos Pantazis<sup>4</sup>
- Daniela Bezemer<sup>3</sup>
- Eline Op de Coul<sup>5</sup>
- Thijs van de Laar<sup>6</sup>
- Christophe Fraser<sup>8</sup>
- Maria Prins<sup>9</sup>
- Peter Reiss<sup>2</sup>
- Godelieve J de Bree<sup>2</sup>
- Oliver Ratmann<sup>1</sup> †

### Affiliations

1. Department of Mathematics, Imperial College London London United Kingdom ([ROR:041kmwe10](https://ror.org/041kmwe10))
2. Amsterdam Institute for Global Health and Development Amsterdam Netherlands ([ROR:037n2rm85](https://ror.org/037n2rm85))
3. Stichting HIV Monitoring Amsterdam Netherlands ([ROR:02w6k4f12](https://ror.org/02w6k4f12))
4. Department of Hygiene, Epidemiology and Medical Statistics, University of Athens Athens Greece ([ROR:04gnjpq42](https://ror.org/04gnjpq42))
5. Center for Infectious Diseases Prevention and Control, National Institute for Public Health and the Environment (RIVM) Bilthoven Netherlands ([ROR:01cesdt21](https://ror.org/01cesdt21))
6. Department of Donor Medicine Research, Sanquin Amsterdam Netherlands ([ROR:01fm2fv39](https://ror.org/01fm2fv39))
7. Department of Medical Microbiology, Onze Lieve Vrouwe Gasthuis Amsterdam Netherlands ([ROR:01d02sf11](https://ror.org/01d02sf11))
8. Big Data Institute, Nuffield Department of Medicine, University of Oxford Oxford United Kingdom ([ROR:052gg0110](https://ror.org/052gg0110))
9. Academic Medical Center Amsterdam Netherlands ([ROR:03t4gr691](https://ror.org/03t4gr691))
10. Department of Global Health, Amsterdam University Medical Centers Amsterdam Netherlands ([ROR:05grdyy37](https://ror.org/05grdyy37))
11. Division of Infectious Diseases, Department of Internal Medicine, Amsterdam Infection and Immunity Institute Amsterdam Netherlands

† Corresponding author

## Abstract

Background:More than 300 cities including the city of Amsterdam in the Netherlands have joined the UNAIDS Fast-Track Cities initiative, committing to accelerate their HIV response and end the AIDS epidemic in cities by 2030. To support this commitment, we aimed to estimate the number and proportion of Amsterdam HIV infections that originated within the city, from Amsterdam residents. We also aimed to estimate the proportion of recent HIV infections during the 5-year period 2014–2018 in Amsterdam that remained undiagnosed.Methods:We located diagnosed HIV infections in Amsterdam using postcode data (PC4) at time of registration in the ATHENA observational HIV cohort, and used HIV sequence data to reconstruct phylogeographically distinct, partially observed Amsterdam transmission chains. Individual-level infection times were estimated from biomarker data, and used to date the phylogenetically observed transmission chains as well as to estimate undiagnosed proportions among recent infections. A Bayesian Negative Binomial branching process model was used to estimate the number, size, and growth of the unobserved Amsterdam transmission chains from the partially observed phylogenetic data.Results:Between 1 January 2014 and 1 May 2019, there were 846 HIV diagnoses in Amsterdam residents, of whom 516 (61%) were estimated to have been infected in 2014–2018. The rate of new Amsterdam diagnoses since 2014 (104 per 100,000) remained higher than the national rates excluding Amsterdam (24 per 100,000), and in this sense Amsterdam remained a HIV hotspot in the Netherlands. An estimated 14% [12–16%] of infections in Amsterdan MSM in 2014–2018 remained undiagnosed by 1 May 2019, and 41% [35–48%] in Amsterdam heterosexuals, with variation by region of birth. An estimated 67% [60–74%] of Amsterdam MSM infections in 2014–2018 had an Amsterdam resident as source, and 56% [41–70%] in Amsterdam heterosexuals, with heterogeneity by region of birth. Of the locally acquired infections, an estimated 43% [37–49%] were in foreign-born MSM, 41% [35–47%] in Dutch-born MSM, 10% [6–18%] in foreign-born heterosexuals, and 5% [2–9%] in Dutch-born heterosexuals. We estimate the majority of Amsterdam MSM infections in 2014–2018 originated in transmission chains that pre-existed by 2014.Conclusions:This combined phylogenetic, epidemiologic, and modelling analysis in the UNAIDS Fast-Track City Amsterdam indicates that there remains considerable potential to prevent HIV infections among Amsterdam residents through city-level interventions. The burden of locally acquired infection remains concentrated in MSM, and both Dutch-born and foreign-born MSM would likely benefit most from intensified city-level interventions.Funding:This study received funding as part of the H-TEAM initiative from Aidsfonds (project number P29701). The H-TEAM initiative is being supported by Aidsfonds (grant number: 2013169, P29701, P60803), Stichting Amsterdam Dinner Foundation, Bristol-Myers Squibb International Corp. (study number: AI424-541), Gilead Sciences Europe Ltd (grant number: PA-HIV-PREP-16-0024), Gilead Sciences (protocol numbers: CO-NL-276-4222, CO-US-276-1712, CO-NL-985-6195), and M.A.C AIDS Fund.

## Introduction

Human immunodeficiency virus (HIV) is concentrated in metropolitan areas (Joint United Nations Programme on HIV/AIDS, 2014). In response, as of March 2021 over 300 cities have joined the Fast-Track Cities initiative (www.fast-trackcities.org) by signing the Paris Declaration, committing to end the AIDS epidemic by 2030, by addressing disparities in access to basic health and social services, social justice and economic opportunities (UNAIDS, 2019). Several of these fast-track cities have successfully developed strategies which best address the needs of the local epidemic, including London’s HIV Prevention Programme and early ART initiation, and New York’s Status Neutral Prevention and Treatment Cycle (Public Health England, 2018; Myers et al., 2018). A central milestone in this agenda is to characterise the number of HIV infections that are acquired from sources within cities and are thus preventable through local interventions, as well as to identify the primary risk groups with infections from local sources.

In the Netherlands, Amsterdam is the city with the greatest HIV burden nationally, reflecting in part large communities of MSM and foreign-born individuals. Amsterdam has a long history of a collaborative HIV approach in combating the epidemic and joined the UNAIDS Fast-Track Cities initiative on 1 December 2014. City-level HIV responses were galvanised in the HIV Transmission Elimination Amsterdam project (H-Team) that same year (de Bree et al., 2019). The H-Team fast-track response, amongst others, focussed on outreach activities, encouraging repeat testing every 3–6 months to identify acute and early HIV infection, followed by immediate initiation of combination antiretroviral therapy (c-ART) in newly diagnosed patients, and roll-out of pre-exposure prophylaxis (PreP) in populations at increased risk of HIV infection (den Daas et al., 2018; Bartelsman et al., 2017; Hoornenborg et al., 2019; Dijkstra et al., 2019). Prior to the COVID-19 pandemic, the number of annual HIV diagnoses in Amsterdam residents has consistently declined from ~300 new city-level HIV diagnoses in 2010 to ~120 in 2018, primarily in Dutch-born and foreign-born MSM. Given these achievements, it is now unclear how many of the remaining new infections are locally acquired and could thus still be locally averted. Late diagnoses remain common and are a particular concern in this effort, both for individual health and the risk that unnoticed transmission chains pose to public health.

Here, we build on Amsterdam’s combined case and genomic surveillance data to reconstruct transmission chains at city level, defined as a single introduction of HIV into Amsterdam residents, followed by a direct infection chain among Amsterdam residents (Figure 1). We exploit clinical patient data to estimate times of HIV infection at individual level, which provides crucial temporal information for interpreting the observed transmission chains. This allows us to estimate the extent of undiagnosed infections at the forefront of the cities’ transmission chains, among infections that are estimated to have occured since Amsterdam joined the Fast-Track Cities network in 2014. We then characterise the growth and origins of Amsterdam transmission chains in 2014–2018, and quantify in particular the proportion of Amsterdam infections in this time period that had an Amsterdam resident as source, and could have been locally averted.

![Figure 1.](https://cdn.elifesciences.org/articles/76487/elife-76487-fig1-v2.jpg)

**Figure 1.:** Input data includes patient baseline data at registration, clinical biomarker data and viral sequence data. Biomarker data is used to estimate infection times, the proportion of undiagnosed infections, and thus the total population size of people living with HIV. HIV sequence data is used to reconstruct phylogenetic trees. Groups of Amsterdam residents with distinct virus are determined phylogeographically with phyloscanner, and without considering genetic distances or bootstrap support. Each such group of Amsterdam residents with distinct virus is interpreted as the partially observed part of a distinct transmission chain among Amsterdam residents, and analysed in calendar time based on the infection times estimated from individual biomarker data, as well as clinical data on viral suppression. The partial observations are used to infer the number, size and growth of the actual transmission chains among Amsterdam residents, and derive key epidemic quantities of interest.

## Materials and methods

### Demographic and clinical cohort data comprising city-level infections

Data were obtained from the prospective ATHENA cohort of all people living with HIV (PLHIV) in care in the Netherlands, including patient demographics and longitudinal CD4, HIV viral load, viral sequence, and treatment data (see Appendix 1, Section 2) (Boender et al., 2018). Sequencing methods are described previously (Bezemer et al., 2004). Cohort data are near complete in the sense that 2% of individuals opted out of participating in the ATHENA study, and 5.2% of individuals who entered ATHENA were lost to follow-up (Boender et al., 2018; Sighem et al., 2020). We geolocated diagnosed infections to Amsterdam based on patients’ postcode of residence at time of first registration in ATHENA or the most recent registration update, which includes PLHIV that changed residence to Amsterdam at a registration update (4%), PLHIV that changed residence to another Dutch municipality after first registration (4%), and PLHIV that were consistently resident in Amsterdam (92%).

Participants were stratified by region of birth: MSM (The Netherlands; Western Europe, North America, Oceania; Eastern and Central Europe; South America and the Caribbean; Other), and heterosexual individuals (The Netherlands; South America and the Caribbean; Sub-Saharan Africa; Other), resulting in 9 risk groups in total. Throughout, we denote transmission group (Amsterdam MSM or heterosexuals) by $t$, and geographic region of birth by $r$.

We here focus on city-level transmission chains growing in the period from 1 January 2014 to 31 December 2018, which for brevity we refer to as 2014–2018. Available demographic, clinical, and viral sequence data were obtained for HIV diagnoses in Amsterdam from the ATHENA database version closed on 1 May 2019.

### Estimating HIV infection dates and undiagnosed infections

Using longitudinal viral load and CD4 count data and further demographic and clinical information, we estimated time from infection to diagnosis for all HIV diagnosed patients with a Bayesian approach (Pantazis et al., 2019). Briefly, data from the CASCADE collaboration on 19,788 observed HIV seroconverters were used to parameterize a bivariate normal linear model of the joint time evolution of HIV viral load and CD4 cell count decline since time of infection in the context of additional covariates (sex, region of origin, mode of infection, age at time of diagnosis). Then we used the trained model to estimate infection times from longitudinal biomarker data for Amsterdam patients, with an average of four viral load observations and six CD4 cell count observations per patient. We next reconstructed characteristic time-to-diagnosis distributions for each of the nine Amsterdam risk groups (MSM/heterosexual, and region of birth) with a Bayesian hierarchical model from the individual-level estimates, modelling the individual-level estimates with a Weibull distribution. To avoid censoring of infection-to-diagnosis times, we focused analyses on the subset of infections in 2010–2012 which were diagnosed by 1 May 2019 since most infections in this window would have been diagnosed by the close of study, and assume as supported by mathematical models that time-to-diagnosis did not change substantially in 2010–2019 (Sighem, 2017; Sighem et al., 2017). The model was implemented with Stan version 2.21 (Carpenter et al., 2017). Full details are provided in Appendix 1, Section 3.

We then calculated the proportion of infections in each year $y=2014,...,2018$ in each of the 9 Amsterdam risk groups that were not diagnosed by database closure (which we denote by $\delta_{try }$) from the fitted model. To adjust for trends in incidence over time, the annual estimates were weighted by the estimated number of HIV infections in each year among Amsterdam MSM and heterosexual individuals without stratifiction by inmigrant status, according to the European Centre for Disease Control and Prevention (ECDC) HIV modelling tool for Amsterdam, version 1.3.0 (Stockholm: European Centre for Disease Prevention and Control, 2017) through weights,

$$
\omega_{ty}= \frac{N_{ty}^{Inf-ECDC}}{\sumz\inYN_{tz}^{Inf-ECDC} }
$$

where y=2014,...,2018 and $N_{ty}^{Inf-ECDC}$ are the estimated total number of infections in year $y$ in Amsterdam MSM or heterosexuals. We then obtained an overall estimate of the proportion of undiagnosed infections in 2014–2018, $\delta_{tr}$ , by applying these weights to the yearly proportions through

$$
\delta_{tr }=\sumy\inY\omega_{ty }\delta_{try }
$$

Recognizing the limitations in applying weights that do not account for differences by place of birth, we used in sensitivity analyses as weights the observed trends in the number of annual HIV diagnoses in the corresponding Amsterdam risk group. The total number of Amsterdam infections in 2014–2018 including the undiagnosed (which we denote by $N_{tr}^{Inf}$) was next estimated by dividing the number of diagnosed Amsterdam infections in 2014–2018 (which we denote by $N_{tr}^{D}$) with the estimated proportion of diagnosed individuals,

$$
N_{tr}^{Inf}=\frac{N_{tr}^{D} }{1-\delta_{tr }}
$$

### Phylogenetic reconstruction of transmission chains among Amsterdam residents

To reconstruct distinct HIV transmission chains among Amsterdam residents, we used the first available partial HIV-1 polymerase (pol) sequence from Amsterdam PLHIV, Dutch PLHIV from outside Amsterdam, and ~82,000 pol sequences from non-Dutch PLHIV. The non-Dutch viral sequences were retrieved from the Los Alamos HIV-1 sequence database subject to a length of at least 1300 in the pol gene on March 2, 2020 (www.hiv.lanl.gov). The basic local alignment search tool (BLAST v2.10.0) was used to select the top 20 closest background sequences to any Dutch sequence (Altschul et al., 1990). All sequences were subtyped using Comet v2.3 (Struck et al., 2014). Sequences with an uncertain subtype classification using Comet were analysed with Rega v3.0 (Pineda-Peña et al., 2013). Any remaining sequences for which a subtype could not be resolved were discarded from further analysis (n=122). Subtype-specific alignments were generated with Virulign (Libin et al., 2019) (Appendix 1 Section 4.1) and sequences from other subtypes were added as outgroup for the purpose of phylogenetic rooting. The final alignments were trimmed to positions 2253–3870 in the reference genome HXB2 (Ratner et al., 1985).

Subtype-specific HIV phylogenetic trees were generated for alignments with at least 50 Amsterdam sequences (subtypes and recombinant forms B, 01AE, 02AG, C, D, G, A1 or 06 cpx) using FastTree v2.1.8 (Price et al., 2010) rooted at the outgroup, and the outgroup taxa were then pruned from the phylogeny. Next, we attributed to all viral lineages in the phylogenies a ‘state’ label that included information on the transmission risk group (MSM, heterosexual, other) and location with phyloscanner version 1.8.0 (Wymant et al., 2018); see Bezemer et al., 2022 for details. Locations were classified into Amsterdam (for ATHENA patients with an Amsterdam postcode at time of registration or a registration update), the Netherlands (for other ATHENA patients), and the 9 world regions Africa, Western Europe, Eastern Europe and Central Asia, North America, Latin America and the Caribbean, Dutch Caribbean and Suriname, Middle East and North Africa, South and South-East Asia and Oceania (for non-Dutch sequences).

In the labelled phylogeny, the lineage labels jump backwards in time, for example from Amsterdam MSM associated with a lineage ending in a tip observed in Amsterdam MSM to Western Europe. Thus, we can group lineages according to the same label between jumps, and we follow Wymant et al., 2018 in referring to these groups as phyloscanner subgraphs. We assumed that we have sufficient background sequences such that no additional background sequences would further separate transmission chains among Amsterdam residents into more distinct chains. A subtle but important related point is that with the available location data at time of registration or a registration update, we are only able to phylogenetically reconstruct transmission chains by residence status rather than the location at which transmission actually occurred. For example, two Amsterdam residents appear in the same phyloscanner subgraph if they infected each other during a short-term visit in another Dutch, European or global location, if they were both infected from a common source during such a short-term visit and the source remained unsampled, if they infected each other before they began their residence in Amsterdam, or after they moved to another Dutch municipality. Diagnosed Amsterdam patients in the same subgraph were then interpreted as belonging to the same transmission chain, and the estimated state of the root of the subgraph was interpreted as the geographical origin of the transmission chain. Throughout, we refer to the subgraphs also as the phylogenetically observed (parts of) transmission chains. Using this approach, we note that unlike most phylogenetic clustering analyses (Burns et al., 2017), every infected patient with a sequence is included in one subgraph, and all partially observed transmission chains of size one are included in the analysis to ensure that the entire distribution of observed transmission chains is represented in the analysis (Bezemer et al., 2022). To capture phylogenetic uncertainty, phylogenetic analyses were repeated on 100 bootstrap replicates drawn from each subtype alignment, and transmission chains were enumerated across these replicate analyses.

We classified phylogenetically reconstructed transmission chains by the infection dates that we estimated from each patient’s diagnosis date, risk group, age, CD4 trajectory and viral load trajectory. Chains were classified as ‘pre-existing’ if at least one of its members had a posterior median infection date before 2014, and as ‘emerging’ if all members had a posterior median infection date after January 1, 2014.

### Virally unsuppressed transmission chains

For all pre-existing chains, we determined the number of infectious individuals at the start of 2014 from viral load data. Specifically, we defined patients as suppressed by 2014 if their last viral load measurement before 2014 was below 100 copies/ml, and count for each pre-existing chain its suppressed and unsuppressed members by 2014.

### Estimating the growth of city-level transmission chains

Because of the large number of late presenters and incomplete sequence coverage in diagnosed patients, the phylogenetically observed transmission chains are incomplete and statistical models were required to estimate the growth and origins of Amsterdam transmission chains. We here extended the Bayesian branching process model of Bezemer et al., 2022 to estimate the growth of pre-existing transmission chains. Specifically, given $m=1,...,M$ index cases of a chain that pre-existed, the final size distribution of stuttering transmission chains is under a Negative Binomial branching process model given by

$$
c(i|\mum,ϕm)=\frac{m}{m+i}NegBin(i|\mum,ϕm)
$$

where NegBin is the Negative Binomial distribution characterised by mean $\mum$ and dispersion parameter $ϕm$, $i=0,1,2,...$ is the number of new cases, and μ < 1. Incomplete sampling of new cases can be accommodated via

$$
c_{obs}(i|m,\mu,ϕ,ρ)=\sum_{k=1}^{∞}Bin(i|k,p)c(k|m,\mu,ρ)=\sum_{k=1}^{∞}Bin(i|k,ρ)\frac{m}{m+k}NegBin(k|\mum,ϕm),
$$

where $ρ$ denotes the probability that a new case in 2014–2018 is diagnosed and has a viral sequence sampled by database closure. In the model, the index cases are assumed to be infectious and defined by the number of unsuppressed members by 2014 in a pre-existing chain, adjusted for the sampling probability of such members. We further capped the infinite sum in (3) in the model, recognizing that the summands rapidly tend to zero. The corresponding equation for emergent transmission chains (since 2014 as defined above) is similar,

$$
c~_{obs}(n|m=1,\mu,ϕ,ρ)=\frac{\sumz=n∞Bin(n|z,ρ)\frac{1}{z}NegBin(z−1|\mu,ϕ)}{1−\sumz=n∞((1−ρ)^{z}\frac{1}{z}NegBin(z−1|\mu,ϕ)) }
$$

where $n=1,2,...$ are the total number of observed cases in an emerging chain. We then denote with $x_{s}$ and $x∼_{s}$ respectively the observed growth distributions for the phylogenetically observed, pre-existing and emergent transmission chains in the phylogeny of subtype/ recombinant form, and for either Amsterdam MSM or heterosexuals, which we denote by $s$. Here, $x_{s}$ is a matrix with rows indicating the number of index cases and columns indicating the number of new cases, and $x∼_{s}$ is a row vector with rows indicating the total number of cases in emerging chains. For ease of reading, we suppress the subscripts where possible from now on. The likelihood then comprises the growth distributions of emerging chains, pre-existing chains that continued to grow, and pre-existing chains with unsuppressed members that did not grow, with the following log-likelihood,

$$
l(x,x~|\mu,ϕ,ρ)=\sum_{m=1}^{M}\sum_{i=0}^{I}x_{mi}logc_{obs}(i|m,\mu,ϕ,ρ)+\sum_{n=1}^{N}x~_{n}logc~_{obs}(n|m=1,\mu,ϕ,ρ),
$$

where $M$ is the largest number of index cases observed across the chains after adjusting for sampling, $I$ is the largest number of new cases observed in pre-existing chains and $N$ is the largest number of new cases observed in emergent chains, including the first case. Pre-existing chains for which all members were suppressed by 2014 and which did not grow were not included, because these chains had no unsuppressed index case. Due to small counts, we grouped the observed growth distributions for the phylogenetically observed transmission chains for non-B subtypes together before fitting the model. We fitted the branching process model under a Bayesian framework with Stan version 2.21 to the observed growth distributions among MSM, borrowing information across subtypes B and non-B, and similarly for heterosexuals. The primary output of the model are posterior predictive distributions on the number, size and growth of the actual transmission chains among Amsterdam residents, both for MSM and heterosexuals, and by viral subtype. This includes emerging chains that were entirely unsampled. Full details are provided in Appendix 1, Section 6.

### Derived statistical estimates

Given estimates of the number and growth of both pre-existing and emergent transmission chains, it is straightforward to derive estimates of the proportion of HIV infections among Amsterdam residents in 2014–2018 that had an Amsterdam resident as source (which we denote by $\gamma$ and refer to as the proportion of locally acquired infections). This is because all infections originating from an individual living in Amsterdam had a local source, except the index cases in the emerging chains that were introduced from outside of Amsterdam. Ignoring population subgroups for the derivation, we have

$$
\gamma=\frac{N^{I} - \alpha N^{C}}{N^{I}},
$$

where $N^{I}$ is the estimated number of new infections between 2014 and 2018 in Amsterdam residents, $N^{C}$ is the estimated number of transmission chains which emerged between 2014 and 2018 and $\alpha$ is the estimated proportion of emergent transmission chains with an Amsterdam origin. Since each transmission chain has one index case, $\alpha N^{C}$ is the estimated number of infections with non-Amsterdam origin, and $N^{I}−\alphaN^{C}$ is the estimated number of infections that had an Amsterdam resident as a source.

Using Equation 8, we were able to obtain estimates (8) for Amsterdam MSM residents and Amsterdam heterosexual residents, and for each phylogeny, that is stratified further by each of the major subtypes and recombinant forms (which we denote by $\gamma_{s }$). To obtain estimates stratified by the nine Amsterdam risk groups of interest (where $t$ denotes transmission group MSM or heterosexual and $r$ denotes geographic region of birth), we calculated weighted averages of the $\gamma_{ts }$ across chains and subtypes, with the weight determined as the proportion of the infected individuals in transmission group $t$ (i.e. either MSM or heterosexuals) from region of birth $r$ that are infected with subtype/recombinant form s. Specifically,

$$
\gamma_{tr}=\sum_{sϵS}v_{tsr}\gamma_{ts},
$$

where the proportions $ν_{tsr}$ are for brevity defined in Appendix 1 Section 7. We interpret $\gamma_{tr }$ as the proportion of Amsterdam infections in transmission risk group $t$, from geographic region $r$, that have the potential to be preventable through local interventions.

### Ethics

As from 2002 ATHENA is managed by Stichting HIV Monitoring, the institution appointed by the Dutch Ministry of Public health, Welfare and Sport for the monitoring of people living with HIV in the Netherlands. People entering HIV care receive written material about participation in the ATHENA cohort and are informed by their treating physician on the purpose of data collection, thereafter they can consent verbally or elect to opt-out. Data are pseudonymised before being provided to investigators and may be used for scientific purposes. A designated data protection officer safeguards compliance with the European General Data Protection Regulation (Boender et al., 2018).

## Results

### Substantial declines in HIV diagnoses and infections in Amsterdam

Between 1 January 2014 and 1 May 2019, there were 846 HIV diagnoses in Amsterdam residents who self-identified as MSM (75%) or heterosexual (20%). Of the remaining diagnoses, 1 (<1%) was among injecting drug users (IDU), 12 (1%) were through other modes of transmission and 30 (3%) had an unknown mode of transmission. A total of 275 (33%) of the diagnoses in MSM and heterosexuals presented with a CD4 count below 350, with late presentation being higher among heterosexuals. All diagnosed patients had biomarker data available to estimate time to diagnosis, and 516 of 846 (61%) were estimated to have been infected between 2014 and 2018 based on the posterior median infection time estimate (Table 1). In the preceding 5-year period 2009–2013, there were 1436 HIV diagnoses in Amsterdam and a similar proportion of these presented late (567, 39%). There were 1128 diagnoses with estimated infection in 2009–2013, suggesting a substantial reduction in infections in 2014–2018. Yet, the rate of new Amsterdam diagnoses since 2014 (104 per 100,000) remained higher than the national rates excluding Amsterdam (24 per 100,000), and in this sense Amsterdam remains a HIV hotspot in the Netherlands.

**Table 1.**
 HIV infections among Amsterdam residents in 2014-2018.


<table>
  <thead>
    <tr>
      <th>Risk group</th>
      <th>Observed HIV diagnoses in Amsterdam residents in 2014-May 2019(n)</th>
      <th>Observed HIV diagnoses in Amsterdam residents in 2014-May 2019 with CD4 &lt;350(n)</th>
      <th>Observed HIV diagnoses in Amsterdam residents, estimated to have been infected in 2014–2018(n)</th>
      <th>Estimated undiagnosed HIV infections in Amsterdam residents until May 2019(%)</th>
      <th>Estimated HIV infections in Amsterdam residents in 2014–2018(n)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Total</td>
      <td>846</td>
      <td>275</td>
      <td>516</td>
      <td>19% [17–21%]</td>
      <td>636 [620-656]</td>
    </tr>
    <tr>
      <td>MSM (all)</td>
      <td>671</td>
      <td>192</td>
      <td>446</td>
      <td>14% [12–16%]</td>
      <td>516 [506-529]</td>
    </tr>
    <tr>
      <td>MSM (Dutch-born)</td>
      <td>298</td>
      <td>103</td>
      <td>190</td>
      <td>11% [9–13%]</td>
      <td>214 [209-219]</td>
    </tr>
    <tr>
      <td>MSM (Born in W. Europe, N. America and Oceania)</td>
      <td>100</td>
      <td>12</td>
      <td>80</td>
      <td>9% [6–14%]</td>
      <td>88 [85-93]</td>
    </tr>
    <tr>
      <td>MSM (Born in E. and C. Europe)</td>
      <td>51</td>
      <td>8</td>
      <td>32</td>
      <td>16% [11–24%]</td>
      <td>38 [36-42]</td>
    </tr>
    <tr>
      <td>MSM (Born in S. America and the Caribbean)</td>
      <td>124</td>
      <td>38</td>
      <td>83</td>
      <td>17% [13–22%]</td>
      <td>100 [95-107]</td>
    </tr>
    <tr>
      <td>MSM (Born in any other country)</td>
      <td>98</td>
      <td>31</td>
      <td>61</td>
      <td>20% [14–27%]</td>
      <td>76 [71-83]</td>
    </tr>
    <tr>
      <td>Heterosexuals (all)</td>
      <td>175</td>
      <td>83</td>
      <td>70</td>
      <td>41% [35–48%]</td>
      <td>119 [107-135]</td>
    </tr>
    <tr>
      <td>Heterosexuals (Dutch-born)</td>
      <td>51</td>
      <td>19</td>
      <td>23</td>
      <td>30% [21–44%]</td>
      <td>33 [29-41]</td>
    </tr>
    <tr>
      <td>Heterosexuals (Born in Sub-Saharan Africa)</td>
      <td>67</td>
      <td>36</td>
      <td>17</td>
      <td>57% [47–67%]</td>
      <td>40 [32-51]</td>
    </tr>
    <tr>
      <td>Heterosexuals (Born in S. America and the Caribbean)</td>
      <td>37</td>
      <td>18</td>
      <td>21</td>
      <td>28% [19–42%]</td>
      <td>29 [26-36]</td>
    </tr>
    <tr>
      <td>Heterosexuals (Born in any other country)</td>
      <td>20</td>
      <td>10</td>
      <td>9</td>
      <td>40% [25–57%]</td>
      <td>15 [12-21]</td>
    </tr>
  </tbody>
</table>

_Posterior estimated median time from infection to diagnosis [95% CI]._

### Nine of ten Amsterdam diagnoses and infections are in MSM

A total of 190 (37%) Amsterdam diagnoses with estimated infection in 2014–2018 were in Dutch-born MSM, 256 (50%) in foreign-born MSM, 23 (4%) in Dutch-born men and women identifying as heterosexuals, and 47 (9%) in foreign-born heterosexuals. Thus, the large majority of Amsterdam diagnoses with infection dates between 2014 and 2018 were in foreign-born and Dutch-born MSM, and an important question that we address below is if these diagnoses also likely had an Amsterdam source.

Overall, we find the individual-level time-to-diagnosis estimates varied substantially within each of the 9 Amsterdam risk groups shown in Table 1 (see also Appendix 1—figures 1 and 2). The posterior median time-to-diagnosis estimates among individuals were 14 months longer in heterosexuals than in MSM, 9 months longer in Dutch-born heterosexuals than Dutch-born MSM, and 19 months longer in foreign-born heterosexuals than foreign-born MSM (Appendix 1—figure 3). These substantial diagnosis delays continue to undermine the long-term prognosis of infected individuals and transmission prevention efforts.

### High proportion of infections since 2014 that remained undiagnosed by May 2019

Local estimates of the continuum of care indicate that Amsterdam has surpassed the 95-95-95 targets, with an estimated 5% of all people in Amsterdam living with HIV that remained undiagnosed by the end of 2019 (Sighem et al., 2020; UNAIDS, 2019). Based on the time-to-diagnosis estimates in our cohort, we can focus here at the forefront of ongoing transmission chains and quantify the proportion of recent Amsterdam infections in 2014–2018 that remained undiagnosed by 1 May 2019. Figure 2 shows that the estimated undiagnosed proportions are considerably higher when we focus on infections acquired since 2014. Accounting for declining diagnosis and infection trends (see Materials and methods), an estimated 14% [12–16%] of infections in Amsterdan MSM in 2014–2018 remained undiagnosed, and 41% [35–48%] in Amsterdam heterosexuals (Table 1). The highest proportion of undiagnosed Amsterdam infections in 2014–2018 are in heterosexuals born in Sub-Saharan Africa, with 57% [47–67%].

![Figure 2.](https://cdn.elifesciences.org/articles/76487/elife-76487-fig2-v2.jpg)

**Figure 2.:** Posterior median estimates are shown as bars and 95% credible intervals as error bars. Estimates generated from time-to-diagnosis estimates for 535 MSM and 97 heterosexuals.

While the bivariate model of biomarker data that underpins the individual-level time-to-diagnosis estimates has been validated (Pantazis et al., 2019), our estimates of the proportion of undiagnosed infections in 2014–2018 depend further on the trends in the number of infections in each year as shown in Equation 2. The main analysis is based on trends in HIV infections in Amsterdam MSM and heterosexuals that were estimated with the ECDC HIV Modelling Tool for Amsterdam. The ECDC estimates account for late diagnoses, but aggregate over region of birth. Recognizing this limitation, in sensitivity analyses we used instead trends in directly observed Amsterdam diagnoses, which apply to each Amsterdam risk group but do not account for confounding due to late diagnoses. In the sensitivity analysis, we estimate that 14% [13–17%] of infections in Amsterdam MSM in 2014–2018 remained undiagnosed, and 34% [28–41%] in Amsterdam heterosexuals. Further details are presented in Appendix 1, Section 3.3–3.5.

### More than 1800 distinct transmission chains among Amsterdam residents

We next adopted viral phylogenetic methods to understand how the diagnosed Amsterdam infections since 2014 are distributed across Amsterdam’s HIV transmission networks. A total 378 of the 516 (73%) individuals had a pol sequence available, of whom 341 were of the major subtypes or recombinant forms that are circulating in Amsterdam (B, 01AE, 02AG, C, D, G, A1 and 06 cpx). 37 individuals were excluded from further analysis as their subtype identification was inconclusive, or they were associated with other subtypes or recombinant forms with fewer than 50 sequences in Amsterdam. Appendix 1—table 1 summarises the characteristics of the study population, and those with a sequence available. We reconstructed viral phylogenies using the HIV sequence data from these individuals combined with viral sequences from 3647 Amsterdam diagnoses with estimated infection prior to 2014, 6087 diagnosed individuals from the Netherlands outside Amsterdam, and 14,222 viral sequences from outside the Netherlands that were genetically closest to those circulating in the Netherlands (Appendix 1—figures 4–25). Key statistics based on the bootstrap analysis are reported in Appendix 1—Tables 2 and 3.

We identified across the major HIV-1 subtypes and circulating recombinant forms 1829 distinct viral phylogenetic subgraphs that comprised at least one diagnosed Amsterdam infection prior to 2014, which we refer to as the phylogenetically observed pre-existing transmission chains (Figure 3 and Appendix 1—figure 26). There were 1253 pre-existing chains in MSM, of which 949 (76%) had all members virally suppressed as of 2014, and of those 906 (95%) had no new member in 2014–2018. The remaining 5% of subgraphs likely grew from unsuppressed index individuals that did not have an HIV sequence sampled. In heterosexuals, there were 576 pre-existing chains, of which 401 (70%) had all members virally suppressed as of 2014, and of those 391 (98%) had no new member in 2014–2018. The proportion of unsuppressed subgraphs in Amsterdam heterosexuals was indeed statistically significantly lower than in Amsterdam MSM, but not strongly so (p-value 0.02, one-sided chi-square test). To summarise, transmission appears to have stopped since 2014 in almost all phylogenetically observed pre-existing chains that had all their observed members suppressed by 2014.

![Figure 3.](https://cdn.elifesciences.org/articles/76487/elife-76487-fig3-v2.jpg)

**Figure 3.:** (A) All chains. Horizontal lines connect individuals in reconstructed transmission chains in Amsterdam by chains which had no new case since 2014, and those which continued to grow or emerged, among MSM (top) and heterosexuals (bottom), in order of last diagnosis per chain. (B) Subset of chains in which at least one individual was estimated to have been infected since 2014. Data are presented as in subfigure A.

### Growth of the phylogenetically observed parts of city-level transmission chains

Considering growth, 89 (7%) of the 1253 phylogenetically observed pre-existing chains in Amsterdam MSM had at least one new member diagnosed in 2014–2018, and 114 chains emerged (Table 2 and Figure 3). In Amsterdam heterosexuals, 15 (3%) of the 576 phylogenetically observed pre-existing chains had at least one new member diagnosed in 2014–2018, and 26 chains emerged. The emerging chains thus outnumbered the growing pre-existing chains in both Amsterdam MSM and heterosexuals. However, the observed phylogenetic data are challenging to interpret directly because larger proportions of recent infections remain undiagnosed, approximately half of diagnosed individuals did not have a sequence sampled, and small chains are more likely to remain entirely unobserved (see Materials and methods).

**Table 2.**
 Growth distribution of transmission chains among Amsterdam residents in 2014–2018.


<table>
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th colspan="4">Observed*</th>
      <th colspan="4">Predicted†</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td colspan="2">Pre-existing chains</td>
      <td colspan="2">Emerging chains</td>
      <td colspan="2">Pre-existing chains</td>
      <td colspan="2">Emerging chains</td>
    </tr>
    <tr>
      <td>Transmission group</td>
      <td>New cases</td>
      <td>(N)</td>
      <td>(%)</td>
      <td>(N)</td>
      <td>(%)</td>
      <td>(N)</td>
      <td>(%)</td>
      <td>(N)</td>
      <td>(%)</td>
    </tr>
    <tr>
      <td rowspan="10">Amsterdam MSM</td>
      <td>0</td>
      <td>220</td>
      <td>71.2%</td>
      <td>-</td>
      <td>-</td>
      <td>198 [175-221]</td>
      <td>64.1% [56.6–71.5%]</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>1</td>
      <td>59</td>
      <td>19.1%</td>
      <td>94</td>
      <td>82.5%</td>
      <td>52 [37-69]</td>
      <td>16.8% [12.0–22.3%]</td>
      <td>137 [118-158]</td>
      <td>79.7% [72.3–86.1%]</td>
    </tr>
    <tr>
      <td>2</td>
      <td>15</td>
      <td>4.9%</td>
      <td>11</td>
      <td>9.6%</td>
      <td>23 [14-35]</td>
      <td>7.4% [4.5–11.3%]</td>
      <td>19 [11-30]</td>
      <td>11.2% [6.3–17.0%]</td>
    </tr>
    <tr>
      <td>3</td>
      <td>6</td>
      <td>1.9%</td>
      <td>7</td>
      <td>6.1%</td>
      <td>13 [6-20]</td>
      <td>4.2% [1.9–6.5%]</td>
      <td>7 [2-13]</td>
      <td>4.1% [1.2–7.6%]</td>
    </tr>
    <tr>
      <td>4</td>
      <td>3</td>
      <td>1.0%</td>
      <td>2</td>
      <td>1.8%</td>
      <td>7 [3-14]</td>
      <td>2.3% [1.0–4.5%]</td>
      <td>3 [0–8]</td>
      <td>1.8% [0.0–4.3%]</td>
    </tr>
    <tr>
      <td>5</td>
      <td>2</td>
      <td>0.6%</td>
      <td>0</td>
      <td>0.0%</td>
      <td>4 [1-10]</td>
      <td>1.3% [0.3–3.2%]</td>
      <td>2 [0–5]</td>
      <td>1.1% [0.0–2.9%]</td>
    </tr>
    <tr>
      <td>6</td>
      <td>0</td>
      <td>0.0%</td>
      <td>0</td>
      <td>0.0%</td>
      <td>3 [0–7]</td>
      <td>1.0% [0.0–2.3%]</td>
      <td>1 [0–4]</td>
      <td>0.6% [0.0–2.1%]</td>
    </tr>
    <tr>
      <td>7+</td>
      <td>4</td>
      <td>1.3%</td>
      <td>0</td>
      <td>0.0%</td>
      <td>7 [2-14]</td>
      <td>2.3% [0.6–4.5%]</td>
      <td>2 [0–6]</td>
      <td>1.1% [0.0–3.2%]</td>
    </tr>
    <tr>
      <td>Total that grew</td>
      <td>89</td>
      <td></td>
      <td>114</td>
      <td></td>
      <td>111 [88-134]</td>
      <td></td>
      <td>172 [154-195]</td>
      <td></td>
    </tr>
    <tr>
      <td>Total</td>
      <td>309</td>
      <td></td>
      <td>114</td>
      <td></td>
      <td>309 [309-309]</td>
      <td></td>
      <td>172 [154-195]</td>
      <td></td>
    </tr>
    <tr>
      <td rowspan="10">Amsterdam heterosexual</td>
      <td>0</td>
      <td>150</td>
      <td>90.9%</td>
      <td>-</td>
      <td>-</td>
      <td>138 [123-150]</td>
      <td>83.6% [74.5–90.9%]</td>
      <td>-</td>
      <td></td>
    </tr>
    <tr>
      <td>1</td>
      <td>13</td>
      <td>7.9%</td>
      <td>25</td>
      <td>96.2%</td>
      <td>17 [9-28]</td>
      <td>10.3% [5.5–17.0%]</td>
      <td>50 [35-72]</td>
      <td>86.4% [74.1–95.6%]</td>
    </tr>
    <tr>
      <td>2</td>
      <td>2</td>
      <td>1.2%</td>
      <td>1</td>
      <td>3.8%</td>
      <td>5 [1-11]</td>
      <td>3.0% [0.6–6.7%]</td>
      <td>5 [1-12]</td>
      <td>9.3% [2.0–19.0%]</td>
    </tr>
    <tr>
      <td>3</td>
      <td>0</td>
      <td>0.0%</td>
      <td>0</td>
      <td>0.0%</td>
      <td>2 [0–6]</td>
      <td>1.2% [0.0–3.6%]</td>
      <td>1 [0–5]</td>
      <td>2.0% [0.0–7.8%]</td>
    </tr>
    <tr>
      <td>4</td>
      <td>0</td>
      <td>0.0%</td>
      <td>0</td>
      <td>0.0%</td>
      <td>1 [0–3]</td>
      <td>0.6% [0.0–1.8%]</td>
      <td>0 [0–2]</td>
      <td>0.0% [0.0–4.3%]</td>
    </tr>
    <tr>
      <td>5</td>
      <td>0</td>
      <td>0.0%</td>
      <td>0</td>
      <td>0.0%</td>
      <td>0 [0–2]</td>
      <td>0.0% [0.0–1.2%]</td>
      <td>0 [0–2]</td>
      <td>0.0% [0.0–2.6%]</td>
    </tr>
    <tr>
      <td>6</td>
      <td>0</td>
      <td>0.0%</td>
      <td>0</td>
      <td>0.0%</td>
      <td>0 [0–2]</td>
      <td>0.0% [0.0–1.2%]</td>
      <td>0 [0–1]</td>
      <td>0.0% [0.0–2.0%]</td>
    </tr>
    <tr>
      <td>7+</td>
      <td>0</td>
      <td>0.0%</td>
      <td>0</td>
      <td>0.0%</td>
      <td>0 [0–3]</td>
      <td>0.0% [0.0–1.8%]</td>
      <td>0 [0–1]</td>
      <td>0.0% [0.0–2.0%]</td>
    </tr>
    <tr>
      <td>Total that grew</td>
      <td>15</td>
      <td></td>
      <td>26</td>
      <td></td>
      <td>27 [15-42]</td>
      <td></td>
      <td>58 [42-83]</td>
      <td></td>
    </tr>
    <tr>
      <td>Total</td>
      <td>165</td>
      <td></td>
      <td>26</td>
      <td></td>
      <td>165 [165-165]</td>
      <td></td>
      <td>58 [42-83]</td>
      <td></td>
    </tr>
  </tbody>
</table>

_*Parts of the actual Amsterdam transmission chains were observed in viral phylogenies of the major subtypes and circulating recombinant forms (B, 01AE, 02AG, C, D, G, A1 or 06 cpx).†Predicted based on the Bayesian branching process growth model and accounting for undiagnosed and unsampled individuals._

### Emerging transmission chains outnumber pre-existing, growing transmission chains

We next used a Bayesian branching process growth model to predict the size and growth of the actual transmission chains (see Materials and methods and Appendix 1, Section 6). Model fit to the observed growth distributions was very good (Appendix 1—figure 27). We estimate that there are substantially more emerging chains in Amsterdam since 2014 than phylogenetically observed, 172 [154-195] in MSM and 58 [42-83] in heterosexuals, reflecting that emergent chains have a high probability to be entirely unobserved when growth is below the epidemic reproduction threshold of one (Table 2). Thus, the estimated actual, emerging chains outnumber the growing pre-existing chains in both Amsterdam MSM and heterosexuals more strongly than the phylogenetic data suggest.

In terms of proportions, an estimated 61% [55–67%] of the growing chains among Amsterdam MSM were emerging, and 69% [56–81%] of the growing chains among Amsterdam heterosexuals. We estimate further that 47% [39–55%] of the estimated infections among Amsterdam MSM in 2014–2018 were in emerging chains, and 61% [45–77%] of the estimated infections among Amsterdam heterosexuals (Table 3). Thus, on average the pre-existing chains contributed more new cases in 2014–2018 to Amsterdam infections than the emerging chains.

**Table 3.**
 Distribution of Amsterdam infections since 2014 in pre-existing and emerging transmission chains.


<table>
  <thead>
    <tr>
      <th></th>
      <th colspan="5">Observed*</th>
      <th colspan="5">Predicted†</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>Total</td>
      <td colspan="2">In pre-existing chains</td>
      <td colspan="2">In emerging chains</td>
      <td>Total</td>
      <td colspan="2">In pre-existing chains</td>
      <td colspan="2">In emerging chains</td>
    </tr>
    <tr>
      <td></td>
      <td>(N)</td>
      <td>(N)</td>
      <td>(%)</td>
      <td>(N)</td>
      <td>(%)</td>
      <td>(N)</td>
      <td>(N)</td>
      <td>(%)</td>
      <td>(N)</td>
      <td>(%)</td>
    </tr>
    <tr>
      <td>MSM (Dutch)</td>
      <td>145</td>
      <td>86</td>
      <td>59.30%</td>
      <td>59</td>
      <td>40.70%</td>
      <td>254 [202-318]</td>
      <td>136 [95-188]</td>
      <td>53.6% [44.1–62.4%]</td>
      <td>117 [93-147]</td>
      <td>46.4% [37.6–55.9%]</td>
    </tr>
    <tr>
      <td>MSM (W. Europe, N. America, Oceania)</td>
      <td>40</td>
      <td>25</td>
      <td>62.50%</td>
      <td>15</td>
      <td>37.50%</td>
      <td>68 [49-91]</td>
      <td>37 [23-56]</td>
      <td>54.8% [40.5–68.1%]</td>
      <td>31 [20-43]</td>
      <td>45.2% [31.9–59.5%]</td>
    </tr>
    <tr>
      <td>MSM (E. &amp; C. Europe)</td>
      <td>17</td>
      <td>9</td>
      <td>52.90%</td>
      <td>8</td>
      <td>47.10%</td>
      <td>29 [18-42]</td>
      <td>15 [8-25]</td>
      <td>53.6% [34.2–72.7%]</td>
      <td>13 [7-21]</td>
      <td>46.4% [27.3–65.8%]</td>
    </tr>
    <tr>
      <td>MSM (S. America &amp; Caribbean)</td>
      <td>53</td>
      <td>24</td>
      <td>45.30%</td>
      <td>29</td>
      <td>54.70%</td>
      <td>95 [72-126]</td>
      <td>50 [33-74]</td>
      <td>52.8% [40.3–64.8%]</td>
      <td>45 [31-61]</td>
      <td>47.2% [35.2–59.7%]</td>
    </tr>
    <tr>
      <td>MSM (Other)</td>
      <td>42</td>
      <td>14</td>
      <td>33.30%</td>
      <td>28</td>
      <td>66.70%</td>
      <td>76 [55-103]</td>
      <td>37 [22-57]</td>
      <td>48.4% [34.4–61.7%]</td>
      <td>39 [26-56]</td>
      <td>51.6% [38.3–65.6%]</td>
    </tr>
    <tr>
      <td>MSM (All)</td>
      <td>297</td>
      <td>158</td>
      <td>53.20%</td>
      <td>139</td>
      <td>46.80%</td>
      <td>523 [427-647]</td>
      <td>276 [200-377]</td>
      <td>52.8% [44.6–60.7%]</td>
      <td>246 [206-300]</td>
      <td>47.2% [39.3–55.4%]</td>
    </tr>
    <tr>
      <td>Heterosexual (Dutch)</td>
      <td>14</td>
      <td>2</td>
      <td>14.30%</td>
      <td>12</td>
      <td>85.70%</td>
      <td>38 [23-59]</td>
      <td>14 [5-29]</td>
      <td>37.8% [17.5–58.9%]</td>
      <td>23 [13-38]</td>
      <td>62.2% [41.1–82.5%]</td>
    </tr>
    <tr>
      <td>Heterosexual (Sub-Saharan Africa)</td>
      <td>11</td>
      <td>4</td>
      <td>36.40%</td>
      <td>7</td>
      <td>63.60%</td>
      <td>30 [17-51]</td>
      <td>10 [3-24]</td>
      <td>34.3% [11.3–58.6%]</td>
      <td>20 [11-34]</td>
      <td>65.7% [41.4–88.7%]</td>
    </tr>
    <tr>
      <td>Heterosexual (S. America &amp; Caribbean)</td>
      <td>14</td>
      <td>8</td>
      <td>57.10%</td>
      <td>6</td>
      <td>42.90%</td>
      <td>35 [20-58]</td>
      <td>14 [5-33]</td>
      <td>42.9% [18.6–65.8%]</td>
      <td>19 [10-34]</td>
      <td>57.1% [34.2–81.4%]</td>
    </tr>
    <tr>
      <td>Heterosexual (Other)</td>
      <td>5</td>
      <td>3</td>
      <td>60.0%</td>
      <td>2</td>
      <td>40.0%</td>
      <td>13 [6-23]</td>
      <td>5 [1-12]</td>
      <td>39.1% [9.1–70.0%]</td>
      <td>8 [3-15]</td>
      <td>60.9% [30.0–90.9%]</td>
    </tr>
    <tr>
      <td>Heterosexual (All)</td>
      <td>44</td>
      <td>17</td>
      <td>38.60%</td>
      <td>27</td>
      <td>61.40%</td>
      <td>117 [80-173]</td>
      <td>45 [22-83]</td>
      <td>38.7% [22.6–54.9%]</td>
      <td>71 [49-105]</td>
      <td>61.3% [45.1–77.4%]</td>
    </tr>
  </tbody>
</table>

_*Parts of the actual Amsterdam transmission chains were observed in viral phylogenies of the major subtypes and circulating recombinant forms (B, 01AE, 02AG, C, D, G, A1 or 06 cpx).†Predicted based on the Bayesian branching process growth model and accounting for undiagnosed and unsampled individuals._

### Proportion of locally preventable infections

From the emerging transmission chains, we can directly estimate the proportion of Amsterdam infections since 2014 that had an Amsterdam source (see Materials and methods). We interpret these infections as locally preventable, because they are within the reach of the HIV prevention efforts in Amsterdam. In Amsterdam MSM, an estimated 67% [60–74%] of infections in 2014–2018 were locally preventable, with little variation by region of birth (Figure 4, proportions next to error bars). In Amsterdam heterosexuals, an estimated 56% [41–70%] of infections in 2014–2018 were locally preventable, with more variation by region of birth, though we caution that the underlying sample sizes were small.

![Figure 4.](https://cdn.elifesciences.org/articles/76487/elife-76487-fig4-v2.jpg)

**Figure 4.:** Posterior median estimates of proportion (%) of preventable infections shown above bars. Estimates generated from 203 phylogenetic subgraphs among Amsterdam MSM, containing 297 individuals, and 41 subgraphs among Amsterdam heterosexuals, containing 44 individuals.

We next multiplied the proportions of locally preventable infections with the estimated number of infections in 2014–2018 in each of the 9 Amsterdam risk groups to obtain estimates of the absolute number of locally preventable infections in Amsterdam in 2014–2018 in each risk group (Figure 4, y-axis). Of the estimated 415 [316-542] locally preventable Amsterdam infections in 2014–2018, an estimated 178 [129-243] (43% [37–49%]) were in foreign-born MSM, 171 [124-231] (41% [35–47%]) in Dutch-born MSM, 45 [24-82] (10% [6–18%]) in foreign-born heterosexuals, and 21 [10-39] (5% [2–9%]) in Dutch-born heterosexuals.

## Discussion

More than 300 cities have by the end of 2021 signed the Fast-Track Cities Paris Declaration and committed to end the AIDS epidemic by 2030, addressing disparities in access to basic health and social services, social justice and economic opportunities. The city of Amsterdam reached the UNAIDS Fast-track Cities 95-95-95 targets before the onset of the COVID-19 pandemic, and has seen a decade of declines in city-level HIV diagnoses. Here, we characterised the number, size and growth of HIV transmission chains among Amsterdam residents, and quantified the further potential of preventing HIV infection at city level. It is important to recognize that through the analyses conducted here, the exact location of infection events cannot be identified. Rather, the available location data enable us to identify groups of Amsterdam residents with phylogenetically distinct HIV, which are the inferential basis for estimating the number, size, and growth of the actual unobserved transmission chains among Amsterdam residents. Regardless of the exact infection location, Amsterdam residents live in Amsterdam, and are thus within reach of Amsterdam public health and local prevention interventions.

We can structure our insights in four themes. First, when focusing on the denominator of recent infections that are estimated to have occurred in the 5-year period 2014–2018, the proportions of individuals that remained undiagnosed by early 2019 were high and variable, between 9% and 20% in (self-identified) Amsterdam MSM risk groups, and between 28% and 57% in Amsterdam heterosexual risk groups. These results underscore that strategies aimed at raising awareness of HIV infection, providing easy access to checking symptoms of early HIV infection, encouraging frequent testing, PrEP provision, addressing fears of a positive test and reducing stigma are vital to break the forefront of ongoing HIV transmission chains (https://hebikhiv.nl/en/; Dijkstra et al., 2017; Heijman et al., 2009; Burns et al., 2017; Myers et al., 2018). The estimated times to diagnosis document substantial disparities across risk groups in entering HIV care in Amsterdam, and separate efforts have characterised individuals with late diagnoses (Op de Coul et al., 2016; Bil et al., 2019; Slurink et al., 2021). We explored the impact of assumptions on incidence trends to the undiagnosed estimates and found some sensitivities (Appendix 1, Section 3.3), although estimates were all very similar as long as the assumed incidence trends reflected available data. Further sensitivity analyses are reported in Appendix 1 Section 3.4–3.5. We further validated the time-to-diagnosis estimates by comparing the estimated proportion of recent HIV infections (≤6 months) with those estimated in an independent study in Amsterdam using avidity assays (Slurink et al., 2021), and found them to be similar (Appendix 1—figure 28). The main limitation of our biomarker approach is thus that at present we cannot account for time trends in time-to-diagnosis.

Second, we documented the growth of Amsterdam HIV transmission chains in which all phylogenetically observed members were virally suppressed by 2014. We find that regardless of risk group, almost all such virally suppressed chains did not grow in the sense that no new infections were phylogenetically observed. These results are unsurprising and mirror the established relationship that treatment for HIV infection, which results in undetectable viral load equals untransmittable virus (Rodger et al., 2019).

Third, we initially speculated that with a decade of declining HIV diagnoses in Amsterdam, those infections that still occur might be concentrated in newly seeded, emerging transmission chains. It is challenging to interpret the directly observed data because high proportions of individuals remain undiagnosed and/or are not sequenced, and emerging chains are more likely to be completely undetected. We thus used statistical growth models accounting for unsampled cases, and we estimate in contrast to our initial speculations that 53% of new Amsterdam MSM infections in 2014–2018 grew from chains that existed prior to 2014, and 39% of new Amsterdam heterosexual infections. Following up and tracing back from known transmission chains is easier than discovering emerging chains, and so the many new infections that originate in existing chains have particularly high prevention potential (Oster et al., 2018; Little et al., 2021; Dennis et al., 2021).

Fourth, we quantified the locally preventable infections among Amsterdam residents in 2014–2018, defined as the infections in Amsterdam residents in 2014–2018 who are estimated to have as source another Amsterdam resident. Using the virus’ genetic code as an objective marker into infection events, we estimate that regardless of declining diagnoses and incidence, the majority of infections in Amsterdam residents in 2014–2018 remained locally preventable in all risk groups investigated. The statistical strength of evidence into this finding was strong for Amsterdam MSM (all 95% credible intervals for the proportion of locally preventable infections were above 50%), but more moderate for Amsterdam heterosexuals (wider credible intervals including 50%), reflecting that relatively few infections in Amsterdam heterosexuals in 2014–2018 were observed with a viral sequence by early 2019 due to frequent late diagnosis and incomplete viral sequencing. These findings are consistent with data from clinic surveys in migrants across Europe (Alvarez-Del Arco et al., 2017), which indicated similar levels of in-country HIV acquisition post migration of 51% in heterosexual women and 58% in heterosexual men.

In summary, our data from 2014 to 2018 indicates considerable potential to prevent HIV infections among Amsterdam residents through city-level interventions, even in the context of substantial improvements in curbing the number of diagnoses and infections in Amsterdam over the past 10 years. Within the similarities in demographics, HIV burden, access to care, and prevention approaches between Amsterdam and many cities in Western Europe and worldwide, our conclusions are relevant to the wider UNAIDS Fast-Track cities, and provide evidence-based support for locally targeted combination HIV prevention interventions in metropolitan areas. COVID-19 has severely disrupted prevention messaging, testing and PrEP services and early pathways to care, making innovative and targeted HIV prevention approaches all the more important.
