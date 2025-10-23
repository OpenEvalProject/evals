# Assessing the danger of self-sustained HIV epidemics in heterosexuals by population based phylogenetic cluster analysis

## Authors

- Teja Turk<sup>1</sup> ([ORCID: 0000-0003-3065-8578](https://orcid.org/0000-0003-3065-8578))
- Nadine Bachmann<sup>1</sup> ([ORCID: 0000-0002-7303-9542](https://orcid.org/0000-0002-7303-9542))
- Claus Kadelka<sup>1</sup>
- Jürg Böni<sup>2</sup>
- Sabine Yerly<sup>3</sup>
- Vincent Aubert<sup>4</sup>
- Thomas Klimkait<sup>5</sup>
- Manuel Battegay<sup>6</sup>
- Enos Bernasconi<sup>7</sup>
- Alexandra Calmy<sup>8</sup>
- Matthias Cavassini<sup>9</sup>
- Hansjakob Furrer<sup>10</sup> ([ORCID: 0000-0002-1375-3146](https://orcid.org/0000-0002-1375-3146))
- Matthias Hoffmann<sup>11</sup>
- Huldrych F Günthard<sup>1</sup>
- Roger D Kouyos<sup>1</sup> ([ORCID: 0000-0002-9220-8348](https://orcid.org/0000-0002-9220-8348)) †
- V Aubert
- V Aubert
- M Battegay
- E Bernasconi
- J Böni
- DL Braun
- HC Bucher
- A Calmy
- M Cavassini
- A Ciuffi
- G Dollenmaier
- M Egger
- L Elzi
- J Fehr
- J Fellay
- H Furrer
- CA Fux
- HF Günthard
- D Haerry
- B Hasse
- HH Hirsch
- M Hoffmann
- I Hösli
- C Kahlert
- L Kaiser
- O Keiser
- T Klimkait
- RD Kouyos
- H Kovari
- B Ledergerber
- G Martinetti
- B Martinez de Tejada
- C Marzolini
- KJ Metzner
- N Müller
- D Nicca
- G Pantaleo
- P Paioni
- A Rauch
- C Rudin
- AU Scherrer
- P Schmid
- R Speck
- M Stöckle
- P Tarr
- A Trkola
- P Vernazza
- G Wandeler
- R Weber
- S Yerly

### Affiliations

1. Division of Infectious Diseases and Hospital Epidemiology University Hospital Zurich Zurich Switzerland
2. Institute of Medical Virology University of Zurich Zurich Switzerland
3. Laboratory of Virology Geneva University Hospitals Geneva Switzerland
4. Division of Immunology and Allergy University Hospital Lausanne Lausanne Switzerland
5. Molecular Virology, Department of Biomedicine - Petersplatz University of Basel Basel Switzerland
6. Division of Infectious Diseases and Hospital Epidemiology University Hospital Basel Basel Switzerland
7. Division of Infectious Diseases Regional Hospital Lugano Lugano Switzerland
8. Division of Infectious Diseases Geneva University Hospitals Geneva Switzerland
9. Service of Infectious Diseases, Department of Medicine Lausanne University Hospital Lausanne Switzerland
10. Department of Infectious Diseases Bern University Hospital, University of Bern Bern Switzerland
11. Division of Infectious Diseases Cantonal Hospital St. Gallen St. Gallen Switzerland

† Corresponding author

## Abstract

10.7554/eLife.28721.001 Assessing the danger of transition of HIV transmission from a concentrated to a generalized epidemic is of major importance for public health. In this study, we develop a phylogeny-based statistical approach to address this question. As a case study, we use this to investigate the trends and determinants of HIV transmission among Swiss heterosexuals. We extract the corresponding transmission clusters from a phylogenetic tree. To capture the incomplete sampling, the delayed introduction of imported infections to Switzerland, and potential factors associated with basic reproductive number , we extend the branching process model to infer transmission parameters. Overall, the R 0 is estimated to be R 0 ( 0.44 -confidence interval 95 % — 0.42 ) and it is decreasing by 0.46 per 11 % years ( 10 — 4 % ). Our findings indicate rather diminishing HIV transmission among Swiss heterosexuals far below the epidemic threshold. Generally, our approach allows to assess the danger of self-sustained epidemics from any viral sequence data. 17 %

## Introduction

Epidemics of HIV and other blood-borne and sexually transmitted diseases (for instance syphilis, HBV and HCV) can be subdivided into concentrated and generalized epidemics. While for the former, the rapid infectious agent transmission is restricted to core transmission groups involved in high-risk behaviors (such as men who have sex with men and injecting drug users), the generalized epidemic refers to fast pathogen spreading in the heterosexual (general) population resulting in higher overall disease prevalence. Mechanistically, the key factor explaining whether the HIV transmission is concentrated or generalized, is the ability of HIV to spread among heterosexuals. If the epidemic in this population is not self-sustained, the HIV epidemic remains concentrated; otherwise the virus is spreading rapidly in the broad population leading to a generalized HIV epidemic.

In most resource-rich settings HIV transmission is concentrated, that is, driven mostly by transmission among men who have sex with men (MSM) and injecting drug users (IDU), whereas the limited transmission among heterosexuals is maintained by either imported infections or spillovers from other transmission groups (Kouyos et al., 2010; von Wyl et al., 2011; Ragonnet-Cronin et al., 2016; Xiridou et al., 2010; Esbjörnsson et al., 2016; Sallam et al., 2017). This suggests that in most Western European countries and similar epidemiological settings the basic reproductive number R0 among heterosexuals is below 1. However, it is not clear how far away from self-sustained the epidemic is in heterosexuals. Moreover, the change in HIV transmission among heterosexuals over time is another important, yet unknown, factor, especially with evidenced increasing risky sexual behavior (Kouyos et al., 2015). It is therefore crucial to assess both the transmission and its time trend in order to obtain meaningful insights into the epidemic.

Assessing the subcritical transmission of HIV in the general population shares some methodological similarities with the analysis of stage III zoonoses, for instance, monkeypox (Wolfe et al., 2007), which also exhibit stuttering transmission chains. Both cases follow a source-sink dynamics, i.e., a flux of infections from a subpopulation in which the disease is self-sustained to a population where it is not. For the case of stage III zoonoses and tuberculosis, it has been shown that the distribution of outbreak sizes can be used to quantify the pathogen spread (Blumberg and Lloyd-Smith, 2013b; Blumberg and Lloyd-Smith, 2013a; Borgdorff et al., 1998). The fundamental approach of our study is to apply this concept to transmission of HIV in the general population. However, there are two key differences between emerging zoonotic pathogens and human-to-human infectious agents. Firstly, while the contact tracing data are not available for many sexually transmitted infections (STI), the viral sequences carry valuable information about the transmission chain size distribution. Thus, the approach of quantifying transmissibility from chain size distributions needs to be combined with a tool to derive clusters from viral sequences. Compared to the animal-human transmission the delayed introduction of the index case of an STI or blood-borne virus to the subpopulation of interest plays an important role, especially in viruses like HIV with long infectious periods in the absence of treatment and higher transmissibility during the acute phase (Marzel et al., 2016; Powers et al., 2011; Rieder et al., 2010; Rodger et al., 2016; Hollingsworth et al., 2008; Cohen et al., 2011b; Cohen et al., 2011a; Cohen et al., 2016). This is especially important because a considerable fraction of HIV cases in heterosexuals is found in migrants (Del Amo et al., 2004; von Wyl et al., 2011; European Centre for Disease Prevention and Control/WHO Regional Office for Europe, 2016). If, for example, a migrant infected with HIV abroad moves to Switzerland in the chronic stage of the infection, he/she has (from the perspective of the Swiss population) lost some transmission potential upon entering Swiss heterosexual transmission network.

In order to quantify the subcritical transmission we combine phylogenetic cluster analysis with an adapted version of a branching process model based estimator that derives the basic reproductive number R0 from the size distribution of transmission chains. We further extend this approach to determine the impact of calendar time and other potential determinants on R0; especially in order to assess whether R0 exhibits an increasing time trend or is high in particular subgroups. Applying this method to the phylogenetic transmission clusters among heterosexuals in the Swiss HIV Cohort Study (SHCS), we can assess transmission of HIV in this population and in particular the risk of a generalized HIV epidemic together with the main determinants of transmission.

## Results

We developed a method to assess how far HIV transmission in populations with basic reproductive number R0<1 is from the epidemic threshold, that is, how far it is from being self-sustained in these populations (see Materials and methods). A classical application of this question/method is HIV-1 transmission in heterosexuals in settings with a concentrated epidemic. Heterosexual HIV-1 transmission in Switzerland is a case in point for such a non-self-sustained HIV epidemic. We identified 3,100 transmission clusters among heterosexuals in the SHCS. These clusters were small in size (Table 1) and comprised individuals of broad demographic background (see Table 2). Based on the most likely geographic origin of the transmission clusters, we classified 1,133 transmission chains as being of Swiss origin, that is, to represent introductions from other transmission groups in Switzerland into the heterosexual population, and 1,967 to be of non-Swiss origin. For these latter transmission chains, we assumed that the R0 of the index case was reduced by a factor of ρindex=0.35 (see Materials and methods). To take into account the imperfect sampling density we fixed the subtype-depending sampling probabilities based on the results from the study by Shilaih et al. (2016), corrected by the proportion of the HIV infected individuals linked to care (80% based on Kohler et al., 2015) and the fraction of heterosexuals from the SHCS with an HIV sequence in the phylogenetic tree (57.22%). The model parameters used in this study are summarized in Table 1 (see Sensitivity analyses, Appendix 1—figure 1 and Appendix 1—figure 2 for the corresponding sensitivity analyses).

## R0 of the HIV transmission in Swiss heterosexuals

To obtain an overall estimate for the R0 of HIV transmission in Swiss heterosexuals, the baseline model was fitted to all of the previously described transmission chain data. In this baseline model the R0 was estimated to be 0.44 (95%-confidence interval (CI) 0.42—0.46). The fact that R0 was clearly below 1 (p-value <0.001 from one-sided Wald hypothesis testing H0:R0=1 against the alternative HA:R0<1) indicated that HIV transmission is far away from a self-sustained epidemic.

Although the overall R0 estimate was clearly below 1, individual subtypes represent different epidemiological settings and hence individual subtypes may have R0 closer to the epidemic threshold. The subtype-stratified analyses indeed yielded lower R0 of 0.35 (95%-CI 0.33—0.39) for subtype B as compared to the non-B subtypes (Figure 1). The recombinant form CRF02_AG had the highest estimated R0 of 0.62 (95%-CI 0.56—0.69). Despite these differences among the R0 estimates for different subtypes they were all significantly below 1 (with all p-values from the one-sided test smaller than 0.001). Therefore, we concluded that there is no danger of a self-sustained HIV epidemic in Swiss heterosexuals of any HIV subtype.

![Figure 1.](https://cdn.elifesciences.org/articles/28721/elife-28721-fig1-v2.jpg)

**Figure 1.:** and R0 per subtype from stratified analysis.R0The dark gray point indicates the overall basic reproductive number  estimate (by neglecting the transmission chain subtypes) and the corresponding R0-confidence interval is shown with the dark gray line and the gray-shaded band. The analogous results from the per-subtype stratified analysis are represented by colored points and lines, each color corresponding to one of the subtypes (B, C, CRF01_AE, CRF02_AG or A) or the group of subtypes (other).95%

## Time trend of the R0

Despite consistently low R0 estimates, an increasing time trend for R0 would impose a potential concern, especially if the time trend would predict a crossing of the epidemic threshold in the near future. To investigate this, we fitted a univariate model with log⁡(R0) as a linear function of the establishment date of the transmission chain. We found that overall the R0 is decreasing at a factor 0.89 per 10 years (95%-CI 0.83—0.96). The per subtype-stratified analyses showed the consistently decreasing time trend among the subtypes ranging from factor 0.65 per 10 years for subtype A to 0.89 for B-subtype.

To better capture the changes of R0 over time we included higher-order polynomials of the establishment date to our model (Figure 2). With the reference date on the 1st of January 1996 (which corresponds to the median estimated date of infection - see Table 2) a cubic spline (without the linear term) was identified as the optimal model according to the Bayesian information criterion (BIC). This model exhibits a mild increase of the R0 from the mid 1980’s to the mid 1990’s, with a peak-R0 of 0.49 (95%-CI 0.46—0.53) reached in 1996 and followed by a steep and monotonic decrease. It is noteworthy that the time of peak-R0 coincided with the introduction of highly active antiretroviral therapy. Shortly after the R0 started to rapidly decrease and has never rebounded. This extrapolation should be, however, taken with a grain of salt and seen more as a trend rather than a prognosis, since only a few transmission chains have been observed for the recent years (which is reflected by wide confidence intervals).

![Figure 2.](https://cdn.elifesciences.org/articles/28721/elife-28721-fig2-v2.jpg)

**Figure 2.:** .R0The upper smaller panels show the time trends for  from the subtype-stratified analyses, in which the R0’s were modeled as linear functions of establishment date (i.e., for each subtype the time trend rate was assumed to be constant). The colored shaded-bands correspond to the l⁢o⁢g⁢(R0)-prediction bands. The (best-fitting) nonlinear time trend for 95% from the overall analysis is displayed in the lower panel (dark gray curve) together with the R0-prediction band (gray-shaded area). The black points represent the 95% estimates from the per establishment year stratified analyses and the gray vertical lines the corresponding R0-confidence intervals.95%

## Determinants of the HIV-transmission

Finally, we identified the characteristics associated with higher R0 and therefore potential focal subpopulations, in which the basic reproductive number R0 could be above 1. The simplest model containing only the linear terms of risk factors showed that the R0 is decreasing with the establishment date of the transmission chain and that all non-B subtypes have higher R0 compared to subtype B, which was consistent with the findings from the univariate model and per-subtype stratified analyses. Moreover, we found that reporting sex with occasional partners and longer time to HIV diagnosis of the index case are associated with higher R0, whereas the earliest CD4 cell count and the age do not have significant effects (Figure 3).

![Figure 3.](https://cdn.elifesciences.org/articles/28721/elife-28721-fig3-v2.jpg)

**Figure 3.:** from the multivariate model with only linear factor terms.R0The black square and the black line show the reference basic reproductive number  and its R0-confidence interval (for a transmission chain of subtype B which started on 1.1.1996, and in which the index case was diagnosed 3 years after the infection, was 32 years old upon infection, never reported on having sex with occasional partner and had the earliest CD4 cell count of 350 cells per μL). The vertical gray line separates the factors associated with lower 95% (left; effect factor R0) and from the factors contributing to higher <1 (right; effect factor R0). The black points on this line refer to the reference transmission chain. The colored and dark gray lines represent the effect sizes from multivariate model (black circles depicting the estimates) for different factors and their >1-confidence intervals. The corresponding 95%-values are shown in the rightmost column. FUP, follow-up visit.p

These trends remained robust (Figure 4) when allowing the covariables to enter the model non-linearly (for instance as polynomials like in the case of the time trend above). The final multivariate model identified subtype, establishment date of the transmission chain, frequency of reporting sex with occasional partner and time to diagnosis of the index case as the significant risk factors associated with R0 (see Selection of the predictive models). Allowing nonlinear terms for the time to diagnosis provided better goodness-of-fit than the linear model. The steep increase of R0 in the early/acute phase (see Figure 4) of the infection indicates the importance of early diagnosis (which is nowadays closely related to early treatment initiation) while the time becomes less relevant in the cases diagnosed late in the chronic phase.

![Figure 4.](https://cdn.elifesciences.org/articles/28721/elife-28721-fig4-v2.jpg)

**Figure 4.:** .R0The vertical dotted lines depict the reference transmission chain (of subtype B, started on 1.1.1996, in which the observed index case did not report having sex with occasional partner and was diagnosed after 3 years after the infection). The left -axis represents the basic reproductive number whereas the right y-axis corresponds to the relative values of y as compared to the baseline R0. The R0 as the function of specific factor (with the other factors held fixed at the reference value) is displayed by the colored (for HIV-1 subtype) and the dark gray (establishment date, sexual risk behavior and time to diagnosis) lines. The vertical bars and the shaded bands, respectively, correspond to the R0-confidence intervals.95%

## Discussion

Our approach demonstrates that viral sequences combined with basic demographic information can be successfully used not only to estimate the basic reproductive number R0 of HIV in a subcritical setting and thereby assess the danger of a generalized HIV epidemic but also to shed light on the trends and other determinants of viral transmission. As a proof of concept, this approach was applied to HIV transmission in Swiss heterosexuals, for which we found an R0 far below the epidemic threshold with a decreasing time trend - indicating a low and decreasing danger of a generalized epidemic. Even though the Swiss HIV epidemic is captured in outstanding detail and representativeness by the SHCS, our approach can be easily used in other non-self-sustained epidemics since viral sequences from genotypic resistance testing are nowadays routinely produced in most resource-rich settings. Moreover, the generalizability of our approach might be broadened to other settings and viruses due to the increased availability of viral sequences boosted by decreasing sequencing costs and the ability of the method to adjust for imperfect sampling.

To our knowledge our study represents the first systematic assessment of the basic reproductive number for subcritical HIV transmission among heterosexuals, which makes it difficult to compare our results to other estimates. In addition, it was conducted in one of the most densely sampled settings. Most of the studies investigated the transmission route composition of larger transmission clusters across different B and non-B subtypes (Esbjörnsson et al., 2016; Chaillon et al., 2017; Ragonnet-Cronin et al., 2016; Sallam et al., 2017; Kouyos et al., 2010; von Wyl et al., 2011), or focused on homosexual men or injecting drug users as the main drivers of HIV transmission (Amundsen et al., 2004). Stadler et al. (2012) previously presented a birth-death process based analysis of HIV transmission in Switzerland. However, since this approach is restricted to sufficiently large clusters, it is not suitable for subcritical settings and might potentially overestimate R0 due to selection bias. Hence, our approach, which is tailored to subcritical viral transmission, is complementary to theirs. Among other studies specific for heterosexual populations, Hughes et al. (2009) focused on the clusters of size at least 2 across non-B subtypes, and Xiridou et al. (2010) studied the impact of sexual behavior of migrants on the HIV prevalence, while none of them directly assessed the danger of self-sustained epidemics.

Epidemiological differences between the HIV-1 subtypes, especially between B and non-B subtypes, have been pointed out previously (Kouyos et al., 2010; von Wyl et al., 2011). Yet the exact factors contributing to the differences are difficult to identify. On the one hand, the non-B subtypes are often seen in relation to the infections imported from abroad, which could be introduced either by immigrants or by residents who got infected while temporarily abroad. A proportion of these introductions could be attributed to the sex tourism (Rogstad, 2004). However, even the differences between the various non-B subtypes could be substantial, as they represent different epidemiological settings. For instance, the CRF01_AE is often found in Asians and it also most likely originates from Southeastern Asia (Angelis et al., 2015), while subtypes originating from Africa, such as CRF02_AG (Mir et al., 2016), are frequently found in people of black ethnicity. Additionally, poverty and different policies regulating prostitution worldwide also have an impact on the transmission patterns, like on rate of condom use, access to HIV testing and treatment (Shannon et al., 2015). On the other hand, disentangling the effect of different epidemiological characteristics and even of the strains remains challenging, as R0 was significantly affected by the HIV subtype even in the multivariate model (Figure 3).

One of the key components of our model is the index case relative transmission potential ρindex, which is also associated with some degree of uncertainty. To illustrate its role and influence on the transmission parameters we performed a range of sensitivity analyses (Appendix 1—figure 1). On the one hand, omitting the reduced transmissibility of the index case, that is, assuming ρindex=1, leads to largely underestimated R0 (overall R0 of 0.33, 95%-CI 0.31—0.35) affirming the importance of this extension. Then again, the concrete value chosen may be debatable, especially due to arguable infectivity in chronic phase (studied by Bellan et al., 2015); thus a small ρindex can be caused both by immigration later during chronic infection and by elevated infectivity in the acute phase. To address this issue we lowered the ρindex for the transmission chains of non-Swiss origin to 0.25 to obtain a more conservative estimate of R0, which was, nevertheless, still safely below 1 (0.47, 95%-CI 0.44—0.49). Furthermore, even though theoretically the transmission potential of some index cases could also be enhanced (i.e., ρindex>1), for instance for sex workers, we do not expect that this is the case for many transmission chains and would therefore have only marginal effect on our estimates. Besides, since a ρindex>1 would lead to even lower R0, our main conclusions would not change (in fact, the assumption of ρindex<1 is conservative with respect to our conclusion of R0<1).

The presented model is based on source-sink dynamics, which is reflected in the importance of the index case and its immigration background, while the role of emigration is neglected. However, in many resource-rich settings similar source-sink patterns can be observed, both in the migration related influxes and the new virus introductions in the heterosexual population from other risk groups. Namely, the immigration from a setting with a generalized epidemic to a setting with a concentrated epidemic is by far more likely than the emigration. Similarly, occasional spillovers from other risk groups, such as MSM and IDU, to the generalized population are more probable than the reverse. Therefore, the assumption of absence of such outflow from the epidemiological setting under consideration is not problematic when considering a country like Switzerland, but might present a potential limitation if the unit of interest is smaller, like a region or a city.

Our approach has theoretically several limitations, which we, however, expect to have only moderate impact. First, we assumed stuttering transmission chains, or in other words, that the basic reproductive number R0 is below 1. If R0 was larger than 1 the observed transmission chains would have been much longer (see Sensitivity analyses and Appendix 1—figure 5) which is inconsistent with rather small clusters observed in HIV transmission among Swiss heterosexuals (Kouyos et al., 2010; von Wyl et al., 2011 and Shilaih et al., 2016). Second, some transmission chains might still be active, meaning that some patients from the chain could be still infectious and therefore able to further spread the virus. The consequence of this would be an underestimation of R0 for recent years. However, given much higher transmissibility of HIV in the acute and recent infection (Marzel et al., 2016) and estimated mean time to being non-infectious of approximately 2—2.5 years in recent years (Stadler et al., 2012; Hughes et al., 2009) the majority of the observed transmission chains had most likely been stopped by the time of sampling and hence we do expect that this issue will not lead to a major bias of our estimates (see Sensitivity analyses and Appendix 1—figure 4). Third, since our method is based on transmission clusters their misidentification and negligence of their structure could be another constraint. Possible overlapping transmission chains (as it was also noted in Blumberg and Lloyd-Smith, 2013b), that is, misidentifying two transmission chains resulting from two separate introductions of closely related viruses as one single chain, represent the biggest concern in this regard. Failing to identify separate clusters would lead to a higher R0 estimate. However, this means that our method will tend to overestimate R0 and is hence conservative with respect to its main aim of assessing the danger of self-sustained epidemics; thus, if the method predicts an R0 strongly below 1, the corresponding epidemic will indeed be far away from being self-sustained. Moreover, our method neglects the transmission chain structure and consequently uses only the aggregated number of infections, and assumes the same R0 for the entire chain except for the index case. Yet, this issue is likely to have a weak impact, since we focus on subcritical transmission; the transmission chains are hence short (see Table 1), and their structure conveys only limited information. Indeed, although a huge variation in sexual behavior has been shown previously (Liljeros et al., 2001), our sensitivity analyses exhibited no major impact of varying sexual risk behavior on risk determinants (Sensitivity analyses and Appendix 1—figure 6). Finally, even though the negative binomial model was proposed as the favorable choice for the offspring distribution compared to the Poisson distribution (Blumberg and Lloyd-Smith, 2013b) we did not observe any significant differences in the R0 estimates (see Sensitivity analyses and Appendix 1—figure 7). On the contrary, due to the simplicity of the Poisson distribution we managed to integrate the index case transmission potential reduction and the heterogeneity between the transmission chains into our Poisson-based model in a more systematic manner through the observed variability of the demographic characteristics.

## Conclusion

Generally, our approach allows the assessment of the danger of a concentrated epidemic to become generalized based on the viral sequence data. We demonstrated this approach for the case of heterosexual HIV transmission in Switzerland. In particular, even though the study highlighted some heterogeneity between the HIV subtypes, our findings indicate that there is no imminent danger of a self-sustained epidemic among Swiss heterosexuals, but rather diminishing HIV transmission far below the epidemic threshold. Hence, the HIV epidemic in Switzerland is and most likely will remain restricted to high risk core groups, especially MSM. Moreover, the results suggest that integrated prevention measures in Switzerland taken over time were successful within the heterosexual population.

## Materials and methods

We combined a phylogenetic cluster detection approach to identify transmission chains in the population under consideration with an adapted version of the model developed in Blumberg and Lloyd-Smith (2013a) to infer the basic reproductive number R0 (Figure 5). In particular, we accounted for both imperfect detection (included in Blumberg and Lloyd-Smith, 2013a) and modified transmissibility of the index case (not included in Blumberg and Lloyd-Smith, 2013a) from the perspective of the setting under consideration because it enters the population only (late) in chronic infection – e.g., via immigration. Moreover, we included the baseline transmission chain characteristics (such as HIV-1 subtype, date of infection, time to diagnosis, risky sexual behavior, etc.) to explain the heterogeneity among transmission chains. Note that our approach in principle estimates the effective reproductive number defined as the number of secondary infections for the current state of population; however, in case of a non-self-sustained epidemic with low prevalence, the vast majority of the population is susceptible and hence the effective reproductive number is a very good approximation for the basic reproductive number.

![Figure 5.](https://cdn.elifesciences.org/articles/28721/elife-28721-fig5-v2.jpg)

**Figure 5.:** (i): HIV transmission among heterosexuals in Switzerland (white arrow) has never led to a self-sustained epidemic. However, the unknown potential of imported infections (black arrows) either from abroad or from other transmission groups in Switzerland remains a large concern. (ii): The HIV transmission chains corresponding to Swiss heterosexuals (depicted in red) were identified from the phylogenetic tree containing the SHCS and background viral sequences. (iii): Our mathematical model is based on the discrete-time branching process with nodes of three different types: sampled Swiss infection (red), unsampled Swiss infection (light red) and foreign infection infected by a Swiss index case before moving to Switzerland (green). (iv): Our method for inferring  accounts for both imperfect sampling and modified transmission potential of the index case. (v): Moreover, it includes the baseline transmission chain characteristics to assess the determinants of R0.R0

## SHCS and viral sequences

The SHCS is a multicenter, nationwide, prospective observational study of HIV infected individuals in Switzerland, established in 1988 (Swiss HIV Cohort Study et al., 2010). The SHCS was approved by the ethics committees of the participating institutions (Kantonale Ethikkommission Bern, Ethikkommission des Kantons St. Gallen, Comite Departemental d’Ethique des Specialites Medicales et de Medicine Communataire et de Premier Recours, Kantonale Ethikkommission Zürich, Repubblica e Cantone Ticino–Comitato Ethico Cantonale, Commission Cantonale d’Étique de la Recherche sur l’Être Humain, Ethikkommission beiderBasel; all approvals are available on http://www.shcs.ch/206-ethic-committee-approval-and-informed-consent), and written informed consent was obtained from all participants. Up to December 2016 over 19,500 patients have been enrolled. The SHCS is highly-representative as it covers more than 75% HIV-positive individuals on antiretroviral therapy (ART) in Switzerland (Swiss HIV Cohort Study et al., 2010). In addition to the extensive demographic and clinical data collected at biannual/quarterly follow-up (FUP) visits, for approximately 60% of the patients at least one partial pol sequence from the genotypic resistance testing is available (in total 22,036 sequences from the SHCS resistance database until August 2015). The patients with heterosexual contact as the most likely transmission route comprise about one third of all SHCS participants.

## Phylogenetic tree

The phylogenetic tree was constructed from the Swiss HIV sequences of the SHCS patients and non-Swiss background sequences exported from the Los Alamos National Laboratory, 2016 database (241,783 HIV-1 viral sequences of any subtype and including the circulating recombinant forms 01–74 retrieved on February 23rd, 2016 spanning over the protease and RT regions with fragments of at least 250 nucleotides; the HXB2 sequence and sequences from Switzerland were removed afterwards). The sequences of 8 HIV-1 subtypes and circulating recombinant forms (B, C, CRF01_AE, CRF02_AG, A(1-2)), G, D and F(1-2)) were pairwise aligned to the reference genome HXB2 (accession number K03455) using Muscle v3.8.31 (Edgar, 2004). Sequences with insufficient sequencing quality of the protease region (coverage of less than 200 nucleotides between the positions 2253 and 2549 of HXB2) or reverse transcriptase region (less than 500 nucleotides between positions 2550 and 3869) were excluded. Using the earliest available of the remaining sequences for each patient, the phylogenetic tree was built with the FastTree algorithm under the generalized time-reversible model of nucleotide evolution (Price et al., 2009) including 10,840 SHCS and 90,933 background sequences.

## Transmission chains

The Swiss heterosexual transmission chains were defined as clusters in the phylogenetic tree containing exclusively Swiss HIV sequences from individuals with heterosexual contact as the most likely route of the transmission, regardless of the respective genetic distances and local support values (see Sensitivity analyses and Appendix 1—figure 8 for alternative definition). The transmission chains and the patients enrolled in the SHCS forming them were identified with custom written functions in R (version 3.3.2).

For each transmission chain we determined if it was introduced to the Swiss HIV heterosexuals either as an imported infection from abroad or from other HIV transmission groups within Switzerland. The geographic origin for a given chain was obtained as the country of the closest sequence, which did not belong to Swiss heterosexuals. Specifically, we considered the smallest clade that contained both the transmission chain and either a non-Swiss or non-heterosexual sequence, and chose the sequence with the smallest pairwise genetic distance to the transmission chain (with respect to the Jukes and Cantor (JC69) model).

Additionally, in each extracted transmission chain the observed index case was identified as the patient with the earliest estimated date of infection in the chain. The date of HIV infection for each single individual was imputed with the model described by Taffé et al. (2008) if the patient had enough CD4 cell count measurements before the ART initiation and the estimated date of infection fell within the seroconversion window; otherwise the midpoint of the seroconversion window was used. The demographic characteristics (Table 2) of the index case were extracted from the SHCS, including age at infection, time to diagnosis, first available CD4 cell count and sexual risk behavior. The latter was quantified as the fraction of semiannual follow-up visits at which the patient reported sex with occasional partners. The patients with no available questionnaire regarding the sexual risk behavior were assumed to have never reported on having sex with occasional partner (see Sensitivity analyses and Appendix 1—figure 9 for the corresponding sensitivity analysis). The characteristics of the index case were then used to define the features of each corresponding transmission chain.

## Estimating the basic reproductive number from a model

Our model is based on the basic discrete-time branching process. The basic reproductive number R0 was inferred from the model as the expected number of offsprings, therefore the offspring distribution represents the crucial component of the chain size distribution model. In the following sections we describe the main extensions of the basic branching process theory, which were implemented in our model. The detailed derivations can be found in Appendix 3.

## Offspring distribution

We modeled the offspring distribution in a transmission chain using a Poisson distribution, which is a special case of the negative binomial distribution. The latter has been suggested in the literature (Blumberg and Lloyd-Smith, 2013b) in order to infer R0; however since we did not observe any large differences between the two distributions (see Sensitivity analyses and Appendix 1—figure 7), we decided to use the simpler Poisson model.

Suppose that Rk,n denotes the number of secondary infections of transmission degree n caused by the kth individual from the preceding generation (i.e., infected individuals with transmission degree n-1), where the transmission degree refers to the number of transmissions needed to transfer the pathogen from the index case (see Appendix 3 for detailed model description). Under the Poisson offspring distribution the number of secondary infections is modeled byRk,n∼Pois⁡(R0),

which coincides with the definition of the basic reproductive number R0=𝔼⁢[Rk,n]. Some index cases may have lower transmission potential, e.g., immigrants that arrive during their chronic infection phase, while other index cases may exhibit enhanced transmissibility, for example, sex workers or foreigners living in Switzerland without a partner. To capture a potentially modified transmissibility of the index case we assumed a different offspring distribution of the root, namelyR1,0∼Pois⁡(ρindex⁢R0),

where ρindex denotes the index case relative transmission potential.

To assess the trends and determinants of R0, we further extended the offspring distribution based on the baseline characteristics 𝐱 of the transmission chain. More precisely, we assumed that the logarithm of R0 can be linearly described by the chain characteristics which resulted in the offspring distributionsRk,n∼Pois⁡(exp⁡(βTx))andR1,0∼Pois⁡(ρindexexp⁡(βTx))

for the secondary and the index cases, respectively. Hence, the R0 can be predicted from the effect sizes β of factors 𝐱 asR0=exp⁡(𝜷𝖳⁢𝐱).

Note that since each transmission chain i has its specific baseline characteristics 𝐱i (perhaps even sampling density pi and index case relative transmission potential ρindex,i) the notation above represents a simplification. More precisely, the R0 of the ith transmission chain equals R0,i=exp⁡(βTxi).

## Likelihood function

The likelihood function was expressed in terms of the probability generating function (PGF) of the transmission chain size distribution assuming independent and stuttering (i.e., R0<1 assures that each transmission chain goes extinct almost surely) transmission chains. The following assumptions were made when incorporating the incomplete sampling of the sequences:

Let T denote the true size of a transmission chain and T~ the size of the corresponding observed transmission chain. The above two assumptions can be summarized asT~∣T∼Bin(T,p),

and the PGF 𝒯~ of the observed transmission chain size hence equals𝒯~⁢(z;R0,ρindex,p)=𝒯⁢((1-p)+p⁢z;R0,ρindex)

in terms of the PGF 𝒯 of T. The probability that a transmission chain has observed size of t~≥0 (where t~=0 means that none of the cases of the transmission chain is detected) is given byℙ[T~=t~]=1t~!𝒯~(t~)(0;R0,ρindex,p).

In particular, the probability that a transmission chain is observed (i.e., the observed size is strictly positive) can be calculated asℙ[T~>0]=1-ℙ[T~=0]=1-𝒯~(0;R0,ρindex,p).

However, since only the transmission chains with at least one detected case can be extracted from the phylogeny (and therefore to account for the unobserved transmission chains) we are interested in the probability that an observed transmission chain has a specific size. The probability of observing a transmission chain of size t~>0 isℙ[T~=t~|T~>0]=ℙ[T~=t~]ℙ[T~>0]=1t~!𝒯~(t~)⁢(0;R0,ρindex,p)1-𝒯~⁢(0;R0,ρindex,p).

Finally, for a set of independent observed transmission chain sizes {t~i}i=1I the likelihood function equalsL(R0|{t~i}i=1I,ρindex,p)=∏i=1I1t~i!𝒯~(t~i)⁢(0;R0,ρindex,p)1-𝒯~⁢(0;R0,ρindex,p)

if the same R0, ρindex and p are assumed for all transmission chains. For transmission chains with different baseline characteristics and different parameters, the generalized likelihood function isL(𝜷|{t~i,𝐱i,ρindex,i,pi}i=1I)=∏i=1I1t~i!𝒯~(t~i)⁢(0;exp⁡(𝜷𝖳⁢𝐱i),ρindex,i,pi)1-𝒯~⁢(0;exp⁡(𝜷𝖳⁢𝐱i),ρindex,i,pi).

## Model fit

The maximum likelihood (ML) estimator for 𝜷, the predictor for R0 and the corresponding statistics (confidence intervals, p-values, etc.) were implemented in the R package PoisTransCh (Turk, 2017, https://github.com/tejaturk/PoisTransCh; copy archived at https://github.com/elifesciences-publications/PoisTransCh). The provided confidence intervals are the Wald-type 95%-confidence intervals (see Sensitivity analyses for the comparison against different types) and the p-values are based on the Wald statistic. Initially, we assessed the impact of covariables potentially associated with HIV transmission. Specifically, we considered HIV-1 subtype, establishment date of the transmission chain (i.e., the earliest estimated date of infection in the transmission chain), reported sex with occasional partner, age at infection, first measured CD4 cell count and time to diagnosis of the index case. Final model selection was carried out by the forward selection and backward elimination algorithms based on the Akaike and Bayesian information criterion (AIC and BIC, respectively). The detailed steps are provided in Selection of the predictive models.

## Datasets

Previously published datasets from ​Kouyos et al. (2010) and ​von Wyl et al. (2011) were used in this study. As previously discussed in these publications, due to the large sampling density this data would, in principle, allow for the reconstruction of entire transmission networks and could thereby endanger the privacy of the patients. This is especially problematic because HIV-1 sequences frequently have been used in court cases. Therefore, a random subset of 10% of the sequences are accessible via GenBank. These accession numbers are as follows: GU344102-GU344671, EF449787, EF449788, EF449796, EF449798, EF449828, EF449829, EF449838, EF449844, EF449852, EF449853, EF449854, EF449860, EF449880, EF449883, EF449889, EF449895, EF449901, EF449904, EF449905, EF449917, EF449921, EF449928, EF449930, EF449943, EF449950, EF449960, EF449971, EF449980, EF449987, EF450004, EF450005, EF450011, EF450024, EF450026, GQ848113, GQ848120, GQ848140, GQ848145, GQ848149, JF769777-JF769851
