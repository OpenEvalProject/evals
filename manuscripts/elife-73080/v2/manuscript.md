# Anopheles salivary antigens as serological biomarkers of vector exposure and malaria transmission: A systematic review with multilevel modelling

## Authors

- Ellen A Kearney<sup>1</sup> ([ORCID: 0000-0001-8912-8067](https://orcid.org/0000-0001-8912-8067))
- Paul A Agius<sup>1</sup>
- Victor Chaumeau<sup>4</sup> ([ORCID: 0000-0003-0171-2176](https://orcid.org/0000-0003-0171-2176))
- Julia C Cutts<sup>1</sup>
- Julie A Simpson<sup>2</sup> ([ORCID: 0000-0002-2660-2013](https://orcid.org/0000-0002-2660-2013))
- Freya JI Fowkes<sup>1</sup> ([ORCID: 0000-0001-5832-9464](https://orcid.org/0000-0001-5832-9464)) †

### Affiliations

1. The McFarlane Burnet Institute of Medical Research and Public Health Melbourne Australia
2. Centre for Epidemiology and Biostatistics, Melbourne School of Population and Global Health, The University of Melbourne Melbourne Australia ([ROR:01ej9dk98](https://ror.org/01ej9dk98))
3. Department of Epidemiology and Preventive Medicine, Monash University Melbourne Australia ([ROR:02bfwt286](https://ror.org/02bfwt286))
4. Shoklo Malaria Research Unit, Mahidol-Oxford Tropical Medicine Research Unit, Faculty of Tropical Medicine, Mahidol University Mae Sot Thailand ([ROR:03fs9z545](https://ror.org/03fs9z545))
5. Centre for Tropical Medicine and Global Health, Nuffield Department of Medicine, University of Oxford Oxford United Kingdom ([ROR:052gg0110](https://ror.org/052gg0110))
6. Department of Medicine at the Doherty Institute, The University of Melbourne Melbourne Australia ([ROR:01ej9dk98](https://ror.org/01ej9dk98))

† Corresponding author

## Abstract

Background:Entomological surveillance for malaria is inherently resource-intensive and produces crude population-level measures of vector exposure which are insensitive in low-transmission settings. Antibodies against Anopheles salivary proteins measured at the individual level may serve as proxy biomarkers for vector exposure and malaria transmission, but their relationship is yet to be quantified.Methods:A systematic review of studies measuring antibodies against Anopheles salivary antigens (PROSPERO: CRD42020185449). Multilevel modelling (to account for multiple study-specific observations [level 1], nested within study [level 2], and study nested within country [level 3]) estimated associations between seroprevalence with Anopheles human biting rate (HBR) and malaria transmission measures.Results:From 3981 studies identified in literature searches, 42 studies across 16 countries were included contributing 393 study-specific observations of anti-Anopheles salivary antibodies determined in 42,764 samples. A positive association between HBR (log transformed) and seroprevalence was found; overall a twofold (100% relative) increase in HBR was associated with a 23% increase in odds of seropositivity (OR: 1.23, 95% CI: 1.10–1.37; p<0.001). The association between HBR and Anopheles salivary antibodies was strongest with concordant, rather than discordant, Anopheles species. Seroprevalence was also significantly positively associated with established epidemiological measures of malaria transmission: entomological inoculation rate, Plasmodium spp. prevalence, and malarial endemicity class.Conclusions:Anopheles salivary antibody biomarkers can serve as a proxy measure for HBR and malaria transmission, and could monitor malaria receptivity of a population to sustain malaria transmission. Validation of Anopheles species-specific biomarkers is important given the global heterogeneity in the distribution of Anopheles species. Salivary biomarkers have the potential to transform surveillance by replacing impractical, inaccurate entomological investigations, especially in areas progressing towards malaria elimination.Funding:Australian National Health and Medical Research Council, Wellcome Trust.

## Introduction

Sensitive and accurate tools to measure and monitor changes in malaria transmission are essential to track progress towards malaria control and elimination goals. Currently, the gold standard measurement of malaria transmission intensity is the entomological inoculation rate (EIR), a population measure defined as the number of infective Anopheles mosquito bites a person receives per unit of time. EIR is calculated as the human biting rate (HBR; measured at the population level by entomological vector-sampling methodologies [gold standard: human landing catch]) multiplied by the sporozoite index (proportion of captured Anopheles with sporozoites present in their salivary glands). However, estimation of EIR and HBR via entomological investigations is inherently labour and resource intensive, requiring trained collectors, specialised laboratories, and skilled entomologists. Furthermore, these approaches provide a crude population-level estimate of total vector exposure at a particular time and location, precluding investigation of heterogeneity and natural transmission dynamics of individual-level vector–human interactions (Monroe et al., 2020). For example, indoor human landing catches provide poor estimates of outdoor biting and thus total vector exposure (Mathenge et al., 2005). The sensitivity of EIR is further compromised in low transmission settings where the number of Plasmodium-infected specimens detected is low and often zero.

Evaluation of the human antibody response to Anopheles spp. salivary proteins has the potential to be a logistically practical approach to estimate levels of exposure to vector bites at an individual level. Several Anopheles salivary proteins have been shown to be immunogenic in individuals naturally exposed to the bites of Anopheles vectors and have been investigated as serological biomarkers to measure Anopheles exposure (Badu et al., 2012b; Drame et al., 2013a; Drame et al., 2010a; Drame et al., 2010b; Drame et al., 2015; Rizzo et al., 2011a; Rizzo et al., 2011b; Stone et al., 2012; Drame et al., 2012), malaria transmission (Londono-Renteria et al., 2015a; Ya-Umphan et al., 2017; Noukpo et al., 2016), and as an outcome for vector control intervention studies (Drame et al., 2013a; Drame et al., 2010a; Drame et al., 2010b; Noukpo et al., 2016; Idris et al., 2017). However, a major shortcoming of the literature is that studies are largely descriptive and do not quantify the association between entomological and malariometric measures and anti-Anopheles salivary antibody responses. We undertook a systematic review with multilevel modelling to quantify the association between HBR, EIR, and other markers of malaria transmission, with anti-Anopheles salivary antibody responses, and to understand how these associations vary according to transmission setting and dominant Anopheles vectors which can exhibit different biting behaviours. In particular, we were interested in comparing the African context (where Anopheles gambiae and Plasmodium falciparum predominates) to non-African settings (where An. gambiae is absent and where both P. falciparum and Plasmodium vivax are prevalent). This knowledge is pertinent to advance the use of salivary antibody biomarkers as a vector and malaria transmission serosurveillance tool.

## Methods

### Search strategy and selection criteria

We performed a systematic review with multilevel modelling according to the Meta-analysis of Observational Studies in Epidemiology (MOOSE) and Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) guidelines (Moher et al., 2009; Stroup et al., 2000) (Reporting Standards Document). Five databases were searched for published studies investigating antibodies to Anopheles salivary antigens as a biomarker for mosquito exposure or malaria transmission published before 30 June 2020. The protocol (Appendix 1) was registered with PROSPERO (CRD42020185449).

The primary criterion for inclusion in this systematic review was the reporting of estimates of seroprevalence or total levels of immunoglobulin (Ig) in human sera against Anopheles salivary antigens. We considered for inclusion cross-sectional, cohort, intervention, and case–control studies of individuals or populations living in all geographies with natural exposure to Anopheles mosquitoes. Studies that were solely performed in participants not representative of the wider naturally exposed population (i.e. mosquito-allergic patients, soldiers, returned travellers) were excluded.

### Measures

#### Outcomes

The primary outcome of our systematic review was antibodies (seroprevalence or levels, including all Ig isotypes and subclasses) against any Anopheles salivary antigens (full-length recombinant proteins, peptides, and crude salivary extract). Study-reported salivary antibody data was extracted at the most granular level (i.e. for each site; time point), with each observation of seroprevalence or levels included as a study-specific salivary antibody observation. As measurement of antibody levels does not produce a common metric between studies, only values of seroprevalence could be included in multilevel modelling analyses. Therefore, to maximise data, authors of studies that reported only antibody levels were contacted and asked to classify their participants as ‘responders’ or ‘non-responders’ according to seropositivity (antibody level relative to unexposed sera). Studies that provided antibody levels or categorised seropositivity based upon arbitrary cut-offs are included in narrative terms only.

#### Exposures

The primary exposures of interest were the entomological metrics HBR (average number of bites received per person per night) and EIR (infectious bites received per person per year). Secondary exposures included study-reported prevalence of Plasmodium spp. infection (confirmed by either microscopy, rapid diagnostic test (RDT), or polymerase chain reaction [PCR]) and seroprevalence of antimalarial antibodies against pre-erythrocytic and blood stage Plasmodium spp. antigens. Where exposure estimates were not provided, we attempted to source data from other publications by the authors or used the site geolocation (longitude and latitude) and year to obtain estimates of EIR from the Pangaea dataset (Yamba et al., 2018), P. falciparum rates in 2–10 year olds (PfPR2-10), and dominant vector species (DVS) from the Malaria Atlas Project (MAP; The Malaria Atlas, 2017). Malarial endemicity classes were derived by applying established endemicity cut-offs to MAP PfPR2-10 estimates (Bhatt et al., 2015). For the purposes of the modelling analyses, we defined DVS as where An. gambiae sensu lato (s.l.) was the only DVS, where An. gambiae s.l. was present with additional DVS, or where An. gambiae s.l. was absent. Studies of salivary antigens where exposure variables could not be sourced and data could not be extracted were excluded.

### Statistical analysis

Where observations of the seroprevalence of antibodies against the same salivary antigen and exposure of interest were reported in more than one study, generalised linear multilevel modelling (mixed effects, logistic) was used to quantify associations between the exposures of interest and salivary antibody seroprevalence measurements (Song et al., 2019). Random intercepts for study and country were estimated to account for nested dependencies induced from multiple study-specific salivary antibody observations (level 1) from the same study (level 2) and studies from the same country (level 3). Additionally, study-level random slopes for the entomological and malariometric exposure parameters were estimated to model study-specific heterogeneity in the effect of the exposure of interest (HBR/EIR/malaria prevalence/antimalarial antibody seroprevalence). The associations between the various exposures and the different salivary antigens were analysed separately; however, observations of IgG seroprevalence against the recombinant full-length protein (gSG6) and synthetic peptide (gSG6-P1, the one peptide determined in all studies utilising peptides) form of the gSG6 antigen were analysed together.

Potential effect modification of the associations between exposures and anti-Anopheles salivary antibody responses was explored. In analyses quantifying the associations between HBR, as well as EIR, and seropositivity, we included an interaction term with DVS and for vector collection method (human landing catch or other indirect measures, e.g. light traps, spray catches, etc.). For the association between Plasmodium spp. prevalence and seropositivity, interaction terms with malaria detection methodology (light microscopy or PCR) and malarial species (P. falciparum only, or P. falciparum and P. vivax) were estimated.

For the exposure measures (HBR, EIR, malaria prevalence, and antimalarial antibody seroprevalence), the data were log transformed since there were non-linear associations between the exposure measures on the original scale and seroprevalence – supported empirically by superior model fit as indicated by Akaike’s information criterion (AIC) and Bayesian information criterion (BIC) fit indices (Appendix 1—table 1). To aid interpretation, we present our results as a relative increase in the odds of the gSG6 IgG seropositivity for a twofold or, in other words, a 100% relative increase in the exposures. Intraclass correlation coefficients (ICCs) were estimated for country- and study-specific heterogeneity using estimated model variance components. In order to explore the presence of study-level influence in (HBR and EIR) effect estimate modelling, the Generalised Linear Latent and Mixed Models (gllamm) package (Rabe-Hesketh et al., 2000) was used to produce Cooks distance statistics (Cook, 1977) at the study level from the generalised linear multilevel models. A conservative cut-off threshold for Cooks distance (4 /n) was used to guide sensitivity analyses, where studies were excluded, in turn, to assess outlier influence. All statistical analyses were performed using STATA v15.1.

### Risk of bias in individual studies

Risk of bias was assessed by one reviewer using the Risk of Bias in Prevalence Studies tool (Hoy et al., 2012). The risk of bias pertains to the reported observations of anti-Anopheles salivary antibody seroprevalence included in the multilevel modelling.

## Results

Literature searches identified 158 potentially relevant studies, of which 42 studies were included in the systematic review (Figure 1) and are described in Table 1. From these studies, we extracted n = 393 study-specific observations of anti-Anopheles salivary antibodies determined from antibody measurements in a total of 42,764 sera samples. These studies were performed in 16 countries mostly in hypo- or mesoendemic areas of Africa (32 studies), with a minority performed in South America (four studies), Asia (four studies), and the Pacific (two studies). Studies were classified according to their DVS which reflected the region where the study was conducted. An. gambiae s.l. was a DVS in all African study sites (n = 151 study-specific observations from 23 studies where An. gambiae s.l. was the only DVS and n = 68 from 16 studies where An. gambiae s.l. was present with additional DVS [i.e. Anopheles funestus, Anopheles pharoensis]), with the exception of one study, which together with the 10 non-African studies contributed n = 174 study-specific estimates where An. gambiae s.l. was absent. Most observations came from cross-sectional (n = 191 from 16 studies) or repeated cross-sectional studies (n = 137 from 18 studies), with n = 60 from cohort studies (six studies) and n = 5 from case–control studies (two studies).

![Figure 1.](https://cdn.elifesciences.org/articles/73080/elife-73080-fig1-v2.jpg)

**Figure 1.:** Excluded studies are detailed in Appendix 3.

**Table 1.**
 Key descriptive information from included studies.


<table>
  <thead>
    <tr>
      <th>Study year</th>
      <th>Country</th>
      <th>Malarial endemicity class</th>
      <th>Dominant malaria vector species</th>
      <th>Study design</th>
      <th>No.participants(samples)</th>
      <th>Study-specific n</th>
      <th>Vector and malariometric variables</th>
      <th>Salivary antibody outcomes(seroprevalence [%];[L]evels)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Africa</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Brosseau et al., 2012</td>
      <td>Angola</td>
      <td>Hypoendemic;mesoendemic</td>
      <td>An. gambiae s.l.;An. funestus</td>
      <td>Cross-sectional‡</td>
      <td>-(1584)</td>
      <td>6</td>
      <td>Plas+LM; PfPR</td>
      <td>gSGE IgG [L]</td>
    </tr>
    <tr>
      <td>Drame et al., 2010a</td>
      <td>Angola</td>
      <td>Hypoendemic</td>
      <td>An. gambiae s.l.</td>
      <td>Cohort</td>
      <td>105(1470)</td>
      <td>12</td>
      <td>HBR; Plas+LM; PfPR</td>
      <td>gSG6-P1 IgG [%; L]</td>
    </tr>
    <tr>
      <td>Drame et al., 2010b</td>
      <td>Angola</td>
      <td>Hypoendemic</td>
      <td>An. gambiae s.l.</td>
      <td>Cohort</td>
      <td>109(1279)</td>
      <td>12</td>
      <td>HBR; Plas+LM; PfPR</td>
      <td>gSGE IgG [L]</td>
    </tr>
    <tr>
      <td>Marie et al., 2015</td>
      <td>Angola</td>
      <td>Hypoendemic</td>
      <td>An. gambiae s.l.</td>
      <td>Cohort</td>
      <td>71(852)</td>
      <td>12</td>
      <td>HBR; PfPR</td>
      <td>gcE5 IgG [L]</td>
    </tr>
    <tr>
      <td>Drame et al., 2015</td>
      <td>Benin</td>
      <td>Hyperendemic</td>
      <td>An. gambiae s.l.;An. funestus</td>
      <td>Cohort‡</td>
      <td>133(532)</td>
      <td>4</td>
      <td>HBR; PfPR</td>
      <td>gSG6-P1 IgG and IgM [%; L]</td>
    </tr>
    <tr>
      <td>Rizzo et al., 2011b</td>
      <td>Burkina Faso</td>
      <td>Hyperendemic*</td>
      <td>An. gambiae s.l.</td>
      <td>Repeated cross-sectional</td>
      <td>-(2066)</td>
      <td>14</td>
      <td>HBR; EIR; Plas+LM§</td>
      <td>gSG6 IgG [%; L]</td>
    </tr>
    <tr>
      <td>Rizzo et al., 2011a</td>
      <td>Burkina Faso</td>
      <td>Hyperendemic*</td>
      <td>An. gambiae s.l.</td>
      <td>Repeated cross-sectional</td>
      <td>335(335)</td>
      <td>3</td>
      <td>HBR</td>
      <td>fSG6 IgG [%; L]</td>
    </tr>
    <tr>
      <td>Rizzo et al., 2014a</td>
      <td>Burkina Faso</td>
      <td>Hyperendemic*</td>
      <td>An. gambiae s.l.</td>
      <td>Repeated cross-sectional</td>
      <td>-(359)</td>
      <td>3</td>
      <td>HBR</td>
      <td>gcE5 IgG [%; L]; IgG1 and IgG4 [L]</td>
    </tr>
    <tr>
      <td>Rizzo et al., 2014b</td>
      <td>Burkina Faso</td>
      <td>Hyperendemic*</td>
      <td>An. gambiae s.l.</td>
      <td>Repeated cross-sectional</td>
      <td>270(270)</td>
      <td>6</td>
      <td>HBR</td>
      <td>gSG6 IgG1 and IgG4 [L]</td>
    </tr>
    <tr>
      <td>Soma et al., 2018</td>
      <td>Burkina Faso</td>
      <td>Mesoendemic</td>
      <td>An. gambiae s.l.</td>
      <td>Cross-sectional</td>
      <td>1,728(273)</td>
      <td>6</td>
      <td>HBR; EIR; Plas+LM; PfPR</td>
      <td>gSG6-P1 IgG [%; L]</td>
    </tr>
    <tr>
      <td>Koffi et al., 2015</td>
      <td>Cote d'Ivoire</td>
      <td>Hypoendemic;mesoendemic</td>
      <td>An. gambiae s.l.;An. funestus†</td>
      <td>Cross-sectional</td>
      <td>94(94)</td>
      <td>3</td>
      <td>Plas+LM; Pf-IgG; PfPR</td>
      <td>gSG6-P1 IgG [%; L]</td>
    </tr>
    <tr>
      <td>Koffi et al., 2017</td>
      <td>Cote d'Ivoire</td>
      <td>Hypoendemic</td>
      <td>An. gambiae s.l.;An. funestus†</td>
      <td>Repeated cross-sectional</td>
      <td>234(234)</td>
      <td>5</td>
      <td>Pf-IgG; PfPR</td>
      <td>gSG6-P1 IgG [%; L]</td>
    </tr>
    <tr>
      <td>Traoré et al., 2018</td>
      <td>Cote d'Ivoire</td>
      <td>Hypoendemic</td>
      <td>An. gambiae s.l.</td>
      <td>Repeated cross-sectional‡</td>
      <td>89 (178)</td>
      <td>4</td>
      <td>HBR; Plas+LM; PfPR</td>
      <td>gSG6-P1 IgG [L]</td>
    </tr>
    <tr>
      <td>Traoré et al., 2019</td>
      <td>Cote d'Ivoire</td>
      <td>Hypoendemic</td>
      <td>An. gambiae s.l.;An. funestus†</td>
      <td>Repeated cross-sectional‡</td>
      <td>-(442)</td>
      <td>6</td>
      <td>HBR; Plas+LM; PfPR</td>
      <td>gSG6-P1 IgG [%; L]</td>
    </tr>
    <tr>
      <td>Sadia-Kacou et al., 2019</td>
      <td>Cote d'Ivoire</td>
      <td>Mesoendemic</td>
      <td>An. gambiae s.l.</td>
      <td>Repeated cross-sectional‡</td>
      <td>775(775)</td>
      <td>8</td>
      <td>PfPR</td>
      <td>gSG6-P1 IgG [L]</td>
    </tr>
    <tr>
      <td>Badu et al., 2015</td>
      <td>Ghana</td>
      <td>Mesoendemic</td>
      <td>An. gambiae s.l.;An. funestus†</td>
      <td>Repeated cross-sectional‡</td>
      <td>295(885)</td>
      <td>3</td>
      <td>Plas+LM; Pf-IgG; PfPR</td>
      <td>gSG6-P1 IgG [%; L]</td>
    </tr>
    <tr>
      <td>Badu et al., 2012b</td>
      <td>Kenya</td>
      <td>Hypoendemic;mesoendemic</td>
      <td>An. gambiae s.l.</td>
      <td>Repeated cross-sectional</td>
      <td>-(1366)</td>
      <td>5</td>
      <td>EIR; Plas+LM§; PfPR</td>
      <td>gSG6-P1 IgG [%; L]</td>
    </tr>
    <tr>
      <td>Sagna et al., 2013b</td>
      <td>Senegal</td>
      <td>Hypoendemic;mesoendemic</td>
      <td>An. gambiae s.l.</td>
      <td>Cohort‡</td>
      <td>265(1325)</td>
      <td>25</td>
      <td>HBR; Plas+LM§; PfPR</td>
      <td>gSG6-P1 IgG [%; L]</td>
    </tr>
    <tr>
      <td>Drame et al., 2012</td>
      <td>Senegal</td>
      <td>Hypoendemic</td>
      <td>An. gambiae s.l.</td>
      <td>Cross-sectional</td>
      <td>1010(1010)</td>
      <td>16</td>
      <td>HBR; PfPR</td>
      <td>gSG6-P1 IgG [%; L]</td>
    </tr>
    <tr>
      <td>Poinsignon et al., 2010b</td>
      <td>Senegal</td>
      <td>Hypoendemic</td>
      <td>An. funestus</td>
      <td>Cohort‡</td>
      <td>87(261)</td>
      <td>3</td>
      <td>HBR; Plas+LM§; PfPR</td>
      <td>gSG6-P1 IgG [L]</td>
    </tr>
    <tr>
      <td>Sarr et al., 2012</td>
      <td>Senegal</td>
      <td>Hypoendemic;mesoendemic</td>
      <td>An. gambiae s.l.;An. funestus†</td>
      <td>Repeated cross-sectional‡</td>
      <td>-(401)</td>
      <td>4</td>
      <td>HBR; Plas+LM§; Pf-IgG; PfPR</td>
      <td>gSG6-P1 IgG [%; L]</td>
    </tr>
    <tr>
      <td>Lawaly et al., 2012</td>
      <td>Senegal</td>
      <td>Mesoendemic</td>
      <td>An. gambiae s.l.</td>
      <td>Cohort</td>
      <td>387(711)</td>
      <td>4</td>
      <td>HBR; Plas+LM§; PfPR</td>
      <td>gSGE IgG, IgG4 and IgE [L]</td>
    </tr>
    <tr>
      <td>Ali et al., 2012</td>
      <td>Senegal</td>
      <td>Hypoendemic;*mesoendemic;*hyperendemic*</td>
      <td>An. gambiae s.l.;An. funestus;An. pharoensis</td>
      <td>Cross-sectional</td>
      <td>-(134)</td>
      <td>3</td>
      <td>HBR; EIR</td>
      <td>gSG6 IgG [%; L] fSG6 IgG [%; L]; f5’nuc IgG [%; L]; g5’nuc IgG [%; L]</td>
    </tr>
    <tr>
      <td>Ambrosino et al., 2010</td>
      <td>Senegal</td>
      <td>Hypoendemic;*mesoendemic;*hyperendemic*</td>
      <td>An. gambiae s.l.;An. funestus;An. pharoensis</td>
      <td>Cross-sectional</td>
      <td>-(123)</td>
      <td>3</td>
      <td>EIR; Pf-IgG</td>
      <td>gSG6-P1 IgG [%]; gSG6-P2 IgG [%]</td>
    </tr>
    <tr>
      <td>Perraut et al., 2017</td>
      <td>Senegal</td>
      <td>Hypoendemic;mesoendemic</td>
      <td>An. gambiae s.l.; An. funestus</td>
      <td>Repeated cross-sectional</td>
      <td>-(798)</td>
      <td>4</td>
      <td>EIR; Plas+LM; Plas+PCR; Pf-IgG; PfPR</td>
      <td>gSG6-P1 IgG [%]</td>
    </tr>
    <tr>
      <td>Poinsignon et al., 2008a</td>
      <td>Senegal</td>
      <td>Mesoendemic</td>
      <td>An. gambiae s.l.</td>
      <td>Cross-sectional‡</td>
      <td>241(241)</td>
      <td>3</td>
      <td>HBR; PfPR</td>
      <td>gSG6-P1 IgG [L]; gSG6-P2 IgG [L]</td>
    </tr>
    <tr>
      <td>Poinsignon et al., 2009</td>
      <td>Senegal</td>
      <td>Mesoendemic</td>
      <td>An. gambiae s.l.</td>
      <td>Repeated cross-sectional‡</td>
      <td>61 (122)</td>
      <td>2</td>
      <td>HBR; Plas+LM§; PfPR</td>
      <td>gSG6-P1 IgG [L]</td>
    </tr>
    <tr>
      <td>Remoue et al., 2006</td>
      <td>Senegal</td>
      <td>Mesoendemic</td>
      <td>An. gambiae s.l.</td>
      <td>Cross-sectional‡</td>
      <td>448(448)</td>
      <td>4</td>
      <td>HBR; Plas+LM§; PfPR</td>
      <td>gSGE IgG [%; L]</td>
    </tr>
    <tr>
      <td>Sagna et al., 2019</td>
      <td>Senegal</td>
      <td>Hypoendemic</td>
      <td>An. gambiae s.l.†</td>
      <td>Cross-sectional‡</td>
      <td>809(809)</td>
      <td>4</td>
      <td>PfPR</td>
      <td>gSG6-P1 IgG [L]</td>
    </tr>
    <tr>
      <td>Stone et al., 2012</td>
      <td>Tanzania</td>
      <td>Mesoendemic;hyperendemic</td>
      <td>An. gambiae s.l.</td>
      <td>Cross-sectional‡</td>
      <td>636(636)</td>
      <td>16</td>
      <td>HBR; Pf-IgG; PfPR</td>
      <td>gSG6 IgG [%; L]</td>
    </tr>
    <tr>
      <td>Yman et al., 2016</td>
      <td>Tanzania</td>
      <td>Mesoendemic;holoendemic*</td>
      <td>An. gambiae s.l.;An. funestus</td>
      <td>Repeated cross-sectional‡</td>
      <td>668(668)</td>
      <td>16</td>
      <td>Pf-IgG; PfPR</td>
      <td>gSG6 IgG [%]</td>
    </tr>
    <tr>
      <td>Proietti et al., 2013</td>
      <td>Uganda</td>
      <td>Mesoendemic</td>
      <td>An. gambiae s.l.;An. funestus†</td>
      <td>Repeated cross-sectional</td>
      <td>509(509)</td>
      <td>3</td>
      <td>Pf-IgG; PfPR</td>
      <td>gSG6 IgG [%]</td>
    </tr>
    <tr>
      <td>South America</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Andrade et al., 2009</td>
      <td>Brazil</td>
      <td>Eliminating;hypoendemic</td>
      <td>An. darlingi</td>
      <td>Cross-sectional</td>
      <td>204(204)</td>
      <td>3</td>
      <td>Plas+LM¶; Plas+PCR¶; PfPR</td>
      <td>dSGE IgG [L||]</td>
    </tr>
    <tr>
      <td>Londono-Renteria et al., 2015a</td>
      <td>Colombia</td>
      <td></td>
      <td>An. albimanus</td>
      <td>Cross-sectional</td>
      <td>42(42)</td>
      <td>2</td>
      <td>Plas+PCR¶</td>
      <td>gSG6-P1 IgG [L||]</td>
    </tr>
    <tr>
      <td>Londono-Renteria et al., 2020a</td>
      <td>Colombia</td>
      <td>Eliminating</td>
      <td>An. albimanus</td>
      <td>Cross-sectional</td>
      <td>337(337)</td>
      <td>2</td>
      <td>Plas+PCR; PfPR</td>
      <td>aPEROX-P1, P2 and P3 IgG [L]; aTRANS-P1 and P2 IgG [L]</td>
    </tr>
    <tr>
      <td>Montiel et al., 2020</td>
      <td>Colombia</td>
      <td>Eliminating</td>
      <td>An. albimanus</td>
      <td>Case–control</td>
      <td>113(113)</td>
      <td>2</td>
      <td>Plas+LM; Plas+PCR¶; PfPR</td>
      <td>gSG6-P1 IgG [L ||]; dSGE IgG [L ||]; aSTECLA SGE IgG [L ||]; aCartagena SGE IgG [L ||]</td>
    </tr>
    <tr>
      <td>Asia</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Kerkhof et al., 2016</td>
      <td>Cambodia</td>
      <td>Hypoendemic</td>
      <td>An. dirus</td>
      <td>Cross-sectional</td>
      <td>-(8438)</td>
      <td>113</td>
      <td>Plas+PCR; Pf-IgG; Pv-IgG; PfPR</td>
      <td>gSG6-P1 IgG [%; L]; gSG6-P2 IgG [%; L]</td>
    </tr>
    <tr>
      <td>Charlwood et al., 2017</td>
      <td>Cambodia</td>
      <td>Eliminating</td>
      <td>An. dirus</td>
      <td>Repeated cross-sectional</td>
      <td>454(1180)</td>
      <td>6</td>
      <td>HBR; Plas+PCR; Pf-IgG; PfPR</td>
      <td>gSG6 IgG [L]</td>
    </tr>
    <tr>
      <td>Ya-Umphan et al., 2017</td>
      <td>Myanmar</td>
      <td>Eliminating</td>
      <td>An. minimus;An. maculatus;An. dirus s.l.</td>
      <td>Repeated cross-sectional</td>
      <td>2602(9425)</td>
      <td>28</td>
      <td>HBR; EIR;Plas+PCR;Pf-IgG; PfPR</td>
      <td>gSG6-P1 IgG [%; L]</td>
    </tr>
    <tr>
      <td>Waitayakul et al., 2006</td>
      <td>Thailand</td>
      <td></td>
      <td>An. dirus</td>
      <td>Case–control</td>
      <td>139 (139)</td>
      <td>3</td>
      <td>Plas+LM</td>
      <td>dirSGE IgG and IgM [L ||]</td>
    </tr>
    <tr>
      <td>Pacific</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Pollard et al., 2019</td>
      <td>Solomon Islands</td>
      <td>Eliminating;hypoendemic</td>
      <td>An. farauti</td>
      <td>Repeated cross-sectional</td>
      <td>686(791)</td>
      <td>9</td>
      <td>HBR; EIR; PfPR</td>
      <td>gSG6-P1 IgG [%; L]</td>
    </tr>
    <tr>
      <td>Idris et al., 2017</td>
      <td>Vanuatu</td>
      <td>Eliminating;hypoendemic;mesoendemic</td>
      <td>An. farauti</td>
      <td>Repeated cross-sectional</td>
      <td>905(905)</td>
      <td>3</td>
      <td>Plas+LM; Pf-IgG; Pv-IgG; PfPR</td>
      <td>gSG6 IgG [%; L]</td>
    </tr>
  </tbody>
</table>

_Data are given as study, year of publication, country, malarial endemicity class, malarial DVS, study design (‡ indicates that study was performed solely in children), number of participants and number of samples, number of study-specific salivary antibody outcome observations (study-specific n), entomological and malariometric parameters, and salivary antibody outcomes assessed. Malarial endemicity class (categorical) is derived from P. falciparum prevalence rate in 2–10 year olds (PfPR) extracted from MAP using site geolocations and year of study, and applying established cut-offs reported in Bhatt et al., 2015. If PfPR data were not available (e.g. surveys prior to 2000; or unable to determine study site geolocation and year), endemicity class is given as stated in the study (indicated by *). DVS is as stated in the study or extracted from MAP (indicated by †). Of note, An. gambiae sensu lato (s.l.) includes both An. gambiae sensu stricto and An. arabiensis. Entomological and malariometric parameters include HBR, EIR, prevalence estimates of Plasmodium spp. (Plas+): detected by LM, or PCR, with § indicating prevalence of P. falciparum only and ¶ indicating prevalence of P. vivax only (no footnote indicates P. falciparum and P. vivax co-endemic), as well as PfPR extracted from MAP (The Malaria Atlas, 2017). Salivary antibody outcomes are indicated as either seroprevalence [%] or levels [L], or both [%; L], with || indicating that studies reported results stratified by malarial infection status. Salivary antigens include recombinant full-length proteins, synthetic peptides, and whole SGE. Italicised prefix of salivary antigen indicates species: An. gambiae (g), An. funestus (f), An. darlingi (d), An. albimanus (a), An. dirus (dir).DVS: dominant vector species; MAP: Malaria Atlas Project; HBR: human biting rate; EIR: entomological inoculation rate; LM: light microscopy; PCR: polymerase chain reaction; SGE: salivary gland extracts._

The salivary antigen most commonly assessed was An. gambiae salivary gland 6 (gSG6), as a full-length protein (n = 67 from 8 studies) and synthetic peptide (An. gambiae salivary gland 6 peptide 1 [gSG6-P1]; n = 270 from 24 studies). Additional salivary antigens assessed included An. gambiae gSG6-P2 (n = 119 from three studies), recombinant cE5 (n = 15 from two studies), g-5’nuc (n = 3 from one study), and recombinant An. funestus fSG6 (n = 6 from two studies) and f-5’nuc (n = 3 from one study). Seven studies measured antibodies to whole salivary gland extracts (SGE) from An. gambiae (n = 24 from four studies), Anopheles darlingi (n = 5 from two studies), Anopheles albimanus (n = 2 from one study), and Anopheles dirus (n = 3 from one study), while one study assessed antibodies against synthetic peptides of An. albimanus (n = 2) (Table 1). All studies investigated total IgG and only five determined an additional isotype or subclass (Drame et al., 2015; Lawaly et al., 2012; Rizzo et al., 2014a; Rizzo et al., 2014b; Waitayakul et al., 2006). The paucity of studies investigating these latter-mentioned antibody types and Anopheles salivary biomarkers precluded extensive multilevel analyses; instead, we present their associations in narrative terms in Appendix 10. Analyses reported below focus on quantifying the relationships between HBR, EIR, and markers of malaria transmission with total IgG to An. gambiae gSG6. The distributions of exposure observations were: HBR (n = 197 from 24 studies, median: 3.0 bites per person per night, IQR: 0.9–12.1; range: 0–121.4), EIR (n = 60 from 8 studies, median: 7.3 infectious bites received per person per year, IQR: 0–36.4; range: 0–585.6), and Plasmodium spp. prevalence (n = 266 from 22 studies, median: 9.1%; IQR: 4–22%; range: 0–94.6%).

Generalised linear multilevel modelling (mixed effects, logistic) of n = 132 study-specific observations from 12 studies estimated a positive association between Anopheles spp.-HBR (log transformed) and seroprevalence of IgG to An. gambiae gSG6 salivary antigen (Drame et al., 2010a; Drame et al., 2015; Rizzo et al., 2011a; Stone et al., 2012; Drame et al., 2012; Ya-Umphan et al., 2017; Soma et al., 2018; Traoré et al., 2019; Sagna et al., 2013b; Sarr et al., 2012; Ali et al., 2012; Pollard et al., 2019; Figure 2, Appendix 4—table 1). As we have log transformed HBR to account for the non-linear relationship between HBR and log odds of gSG6 IgG seropositivity, we have presented estimated odds ratios for different incremental percent increases in HBR (Figure 2—figure supplement 1). For example, the magnitude of the association was such that a twofold (100% relative) increase in HBR was associated with a 23% increase (OR: 1.23; 95% CI: 1.10–1.37; p<0.001) in the odds of anti-gSG6 IgG seropositivity (Figure 2). Heterogeneity in the effect of HBR on gSG6 across studies was observed (likelihood ratio χ2(1) = 109.25, p<0.001); the 95% reference range of study-specific effects for a twofold increase in HBR ranged from a 12% reduction to a 70% increase in odds (OR: 0.88–1.70). There was no evidence that the association between HBR and gSG6 IgG varied according to vector collection method (human landing catch or other indirect methods; p=0.443) or study design (longitudinal cohort or cross-sectional/repeated cross-sectional; p=0.138). Given the global heterogeneity in the distribution of Anopheles species, we sought to quantify the extent to which the association between An. gambiae gSG6 IgG seropositivity and HBR is moderated by DVS. We observed that the magnitude of the association between An. gambiae gSG6 IgG seropositivity and HBR was greatest in African studies where An. gambiae s.l. was the only dominant vector (p<0.001, Appendix 5); a twofold increase in HBR was associated with a 37% increase (OR: 1.37; 95% CI: 1.19–1.58; p<0.001) in the odds of gSG6 IgG seropositivity compared to an attenuated association for African studies where An. gambiae s.l. was not the only DVS (OR: 1.14 per twofold increase in HBR; 95% CI: 0.98–1.33; p=0.079) and non-African studies where An. gambiae s.l. was absent (OR: 1.05 per twofold increase in HBR; 95% CI: 1.03–1.08; p<0.001). In order to quantify the relationship between gSG6 IgG seroprevalence and HBR, for given HBR values we estimated gSG6 IgG seroprevalence by producing model-based predicted probabilities overall and by DVS (Figure 3). In African studies where An. gambiae s.l. is the only DVS, predicted seroprevalence of An. gambiae gSG6 ranged from 21% (95% CI: 0–45%) to 86% (95% CI: 67–100%) for an HBR of 0.1–100 bites per person per night, respectively (Figure 3, Figure 3—figure supplement 1).

![Figure 2.](https://cdn.elifesciences.org/articles/73080/elife-73080-fig2-v2.jpg)

**Figure 2.:** Figure shows the observed anti-gSG6 (either recombinant or peptide form) IgG seroprevalence (%) and HBR for each study-specific observation, as well as the predicted average anti-gSG6 IgG seroprevalence (predicted probability for the average study and country) with 95% confidence intervals (95% CI). Circles are proportional to the size of the sample for each study-specific observation, with colours indicating sample size: black (<50), red (50–100), navy (100–150), and green (>150). Association estimated using generalised linear multilevel modelling (mixed effects, logistic) to account for the hierarchical nature of the data, where study-specific anti-gSG6 IgG observations are nested within study and study is nested within country (model output shown in Appendix 4; p<0.001).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/73080/elife-73080-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** HBR has been log transformed to account for the non-linear relationship between HBR and log odds of gSG6 IgG seropositivity, where a 100% relative increase in HBR corresponds to a twofold increase in HBR. Estimated using generalised linear multilevel modelling (mixed effects, logistic) of the association between anti-gSG6 IgG seropositivity and log HBR, with random effects for country-specific and study-specific heterogeneity in gSG6 IgG seroprevalence and study-specific heterogeneity in effect of HBR (see Appendix 4).

![Figure 3.](https://cdn.elifesciences.org/articles/73080/elife-73080-fig3-v2.jpg)

**Figure 3.:** Panels show the predicted average anti-gSG6 IgG seroprevalence (predicted probability for the average study and country) with 95% confidence intervals for given HBR, for all Anopheles spp. (using model output from Appendix 4) and for specific-dominant vector species (DVS): where An. gambiae s.l. is the only DVS, where other DVS were present in addition to An. gambiae s.l. and where An. gambiae s.l. was absent (using model output from Appendix 5).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/73080/elife-73080-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Figure shows the observed anti-gSG6 (either recombinant or peptide form) IgG seroprevalence (%) and HBR for each study-specific observation coloured by dominant vector species (DVS), as well as the predicted average anti-gSG6 IgG seroprevalence (predicted probability for the average study and country) with 95% confidence intervals (95% CI). Coloured circles and lines denote DVS, with red indicating where An. gambiae s.l. is the only DVS, navy where other DVS were present in addition to An. gambiae s.l., and green where An. gambiae s.l. was absent. Circles are proportional to the size of the sample for each study-specific estimate. Association estimated using generalised linear multilevel modelling (mixed effects, logistic) to account for the hierarchical nature of the data, where study-specific anti-gSG6 IgG observations, are nested within study, and study is nested within country.

A positive association was also found between seroprevalence of anti-gSG6 IgG antibodies and EIR in analysis of n = 38 study-specific observations from eight studies (Figure 4, Appendix 6) [Rizzo et al., 2011b; Ya-Umphan et al., 2017; Soma et al., 2018; Ali et al., 2012; Ambrosino et al., 2010; Perraut et al., 2017; Pollard et al., 2019; Badu et al., 2012b]. For a twofold increase in EIR, the odds of anti-gSG6 IgG seropositivity increased by 11% (OR: 1.11; 95% CI: 1.05–1.17; p<0.001), with heterogeneity in the study-specific effects (95% reference range: 1.00–1.24; likelihood ratio χ2(1) = 15.02, p<0.001). There was no evidence of effect modification by either vector collection method (p=0.095) or DVS (p=0.080) on the association between seroprevalence of anti-gSG6 IgG and EIR.

![Figure 4.](https://cdn.elifesciences.org/articles/73080/elife-73080-fig4-v2.jpg)

**Figure 4.:** Figure shows the observed anti-gSG6 (either recombinant or peptide form) IgG seroprevalence (%) and EIR for each study-specific observation, as well as the predicted average anti-gSG6 IgG seroprevalence (predicted probability for the average study and country) with 95% confidence intervals (95% CI). Circles are proportional to the size of the sample for each study-specific estimate, with colours indicating sample size: black (<50), red (50–100), navy (100–150), and green (>150). Association estimated using generalised linear multilevel modelling (mixed effects, logistic) to account for the hierarchical nature of the data, where study-specific anti-gSG6 IgG observations are nested within study and study is nested within country (model output shown in Appendix 6; p<0.001).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/73080/elife-73080-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** EIR has been log transformed to account for the non-linear relationship between EIR and log odds of gSG6 IgG seropositivity, where a 100% relative increase in EIR corresponds to a twofold increase in EIR. Estimated using generalised linear multilevel modelling (mixed effects, logistic) of the association between anti-gSG6 IgG seropositivity and log EIR, with random effects for country-specific and study-specific heterogeneity in gSG6 IgG seroprevalence and study-specific heterogeneity in effect of EIR (see Appendix 6).

Similar positive associations were also found between anti-gSG6 IgG levels, HBR, and EIR in 11 studies [Drame et al., 2015; Drame et al., 2012; Stone et al., 2012; Soma et al., 2018; Ali et al., 2012; Rizzo et al., 2011a; Rizzo et al., 2011b; Poinsignon et al., 2010b; Poinsignon et al., 2008a; Charlwood et al., 2017; Sagna et al., 2013b] and 3 studies [Rizzo et al., 2011b; Ya-Umphan et al., 2017; Ali et al., 2012], respectively, but 7 studies showed no association between HBR and levels of IgG to gSG6 [Drame et al., 2010a; Ya-Umphan et al., 2017; Traoré et al., 2018; Traoré et al., 2019; Sarr et al., 2012; Poinsignon et al., 2009; Pollard et al., 2019].

The association between anti-gSG6 IgG seroprevalence and population-level prevalence of Plasmodium spp. infection was investigated. Generalised linear multilevel modelling (mixed effects, logistic) of n = 212 from 14 studies that measured Plasmodium spp. prevalence contemporaneously in their study [Badu et al., 2012b; Rizzo et al., 2011b; Ya-Umphan et al., 2017; Soma et al., 2018; Koffi et al., 2015; Traoré et al., 2019; Badu et al., 2015; Sagna et al., 2013b; Sarr et al., 2012; Perraut et al., 2017; Drame et al., 2010a; Idris et al., 2017; Proietti et al., 2013; Kerkhof et al., 2016] showed that for a twofold increase in the prevalence of Plasmodium spp. infection the odds of gSG6 IgG seropositivity increased by 38%, although the confidence intervals were wide (OR: 1.38; 95% CI: 0.89–2.12; p=0.148) and heterogeneity in the study-specific effects was observed (95% reference range: 0.30–6.37; likelihood ratio χ2(1) = 235.5, p<0.001) (Figure 5 and Appendix 7). In the association between gSG6 IgG seropositivity and Plasmodium spp. infection, there was no evidence for a moderating effect of Plasmodium spp. detection method (light microscopy or PCR, p=0.968), or species (African studies with P. falciparum versus non-African studies where P. falciparum and P. vivax are co-prevalent, p=0.538).

![Figure 5.](https://cdn.elifesciences.org/articles/73080/elife-73080-fig5-v2.jpg)

**Figure 5.:** Figure shows the observed anti-gSG6 (either recombinant or peptide form) IgG seroprevalence (%) and prevalence of any Plasmodium spp. infection (%) for each study-specific observation, as well as the predicted average anti-gSG6 IgG seroprevalence (predicted probability for average study) with 95% confidence intervals (95% CI). Circles are proportional to the size of the sample for each study-specific observation, with colours indicating sample size: black (<50), red (50–100), navy (100–150), and green (>150). Association estimated using generalised linear multilevel modelling (mixed effects, logistic) to account for the hierarchical nature of the data, where study-specific anti-gSG6 IgG observations are nested within study. See Appendix 7 for model output.

Additionally, 14 studies reported observations of anti-gSG6 IgG levels and the prevalence of Plasmodium spp. infections measured contemporaneously in their study. The median anti-gSG6 IgG antibody levels increased with increasing Plasmodium spp. prevalence in six of these studies (Drame et al., 2010a; Ya-Umphan et al., 2017; Idris et al., 2017; Poinsignon et al., 2010b; Sarr et al., 2012; Kerkhof et al., 2016), or in Plasmodium spp.-infected compared to non-infected individuals (Londono-Renteria et al., 2015a; Montiel et al., 2020), but showed no association in eight studies (Rizzo et al., 2011b; Soma et al., 2018; Koffi et al., 2015; Traoré et al., 2018; Traoré et al., 2019; Badu et al., 2015; Sagna et al., 2013b; Poinsignon et al., 2009). Furthermore, we also investigated associations with serological measures of malaria exposure and found that for a twofold increase in pre-erythrocytic and blood stage antigen seroprevalence there was a 2.19-fold (OR: 2.19; 95% CI: 1.18–4.04; p=0.013) and 41% to 5.69-fold (OR range: 1.41–5.69; p range: <0.001 to 0.523) increase in the odds of anti-gSG6 IgG seropositivity, respectively (Appendix 8).

To give epidemiological context, we estimated anti-gSG6 seroprevalence by producing model-based predicted probabilities by malarial endemicity class (a categorical variable derived by applying established cut-off values for the PfPR2-10 extracted from MAP). Generalised linear multilevel modelling (mixed effects, logistic) on 297 study-specific salivary antibody observations from 22 studies shows that the estimated anti-gSG6 IgG seroprevalence is higher for the higher endemicity classes (eliminating malaria: 20% [95% CI: 8–31%]; hypoendemic: 34% [95% CI: 19–49%]; mesoendemic: 52% [95 CI: 35–68%]; hyperendemic settings: 47% [95% CI: 27–64%]; holoendemic: 78% [95% CI: 67–90%]; p<0.001; Table 2). Interactions with DVS or region (Africa/non-Africa) could not be explored due to collinearity with malaria endemicity class. Therefore, in addition using Bayes best linear unbiased predictions (BLUPs) we estimated country-specific gSG6 IgG seroprevalence from an intercept-only multilevel model fitted to 301 study-specific salivary antibody observations from 22 studies. It showed that IgG seroprevalence to An. gambiae gSG6 was lowest in countries in the Pacific region where An. gambiae is absent (Vanuatu [31%] and Solomon Islands [32%]) and highest in countries where An. gambiae is a DVS (Benin [72%] and Burkina Faso [65%]; Appendix 9).

**Table 2.**
 Association between gSG6 IgG seroprevalence (%) and malarial endemicity (PfPR2-10).Table shows the odds ratio (OR), 95% confidence interval (95% CI), p-value, as well as the predicted gSG6 IgG seroprevalence and associated 95%CI† for associations between endemicity class (categorical: derived from P. falciparum parasite rates in 2–10 year olds [PfPR]) and anti-gSG6 IgG seropositivity.


<table>
  <thead>
    <tr>
      <th>Malaria endemicity class*</th>
      <th>OR</th>
      <th>95% CI</th>
      <th>p-Value</th>
      <th>Predicted gSG6 IgG seroprevalence (%)</th>
      <th>95% CI</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Eliminating malaria(PfPR &lt;1%)</td>
      <td>Ref.</td>
      <td></td>
      <td></td>
      <td>20.0</td>
      <td>8.3–31.7</td>
    </tr>
    <tr>
      <td>Hypoendemic(PfPR 1-10%)</td>
      <td>2.04</td>
      <td>1.43–2.90</td>
      <td>&lt;0.001</td>
      <td>33.7</td>
      <td>18.9–48.5</td>
    </tr>
    <tr>
      <td>Mesoendemic(PfPR 10-50%)</td>
      <td>4.19</td>
      <td>2.80–6.08</td>
      <td>&lt;0.001</td>
      <td>51.5</td>
      <td>34.6–67.7</td>
    </tr>
    <tr>
      <td>Hyperendemic(PfPR 50-75%)</td>
      <td>3.36</td>
      <td>1.98–5.71</td>
      <td>&lt;0.001</td>
      <td>46.5</td>
      <td>27.4–63.8</td>
    </tr>
    <tr>
      <td>Holoendemic(PfPR &gt;75%)</td>
      <td>14.4</td>
      <td>9.72–21.36</td>
      <td>&lt;0.001</td>
      <td>78.2</td>
      <td>66.8–89.7</td>
    </tr>
  </tbody>
</table>

_*Generalised linear multilevel modelling (mixed effects, logistic) estimating the association between anti-gSG6 IgG seropositivity and endemicity class with random effects for study-specific heterogeneity in gSG6 IgG. Model fitted to n = 297 study-specific observations from 22 studies. Of note, nine studies that measured Plasmodium spp. prevalence and IgG antibodies to gSG6 were excluded from this analysis as eight only reported gSG6 IgG levels and one was a case–control study. Endemicity class membership is derived from PfPR from The Malaria Atlas, 2017 (MAP) using cut-offs taken from Bhatt et al., 2015, or where MAP data were unavailable, endemicity was included as indicated in the study.†Predicted gSG6 IgG seroprevalence (predicted probability in the average study) is estimated from generalised linear multilevel modelling (mixed effects, logistic)._

Assessments of internal and external study validity revealed there was a moderate risk of selection bias (Appendix 2) due to the study-specific inclusion criteria of populations at higher risk of malaria which contributed gSG6 seroprevalence observations. Sensitivity analyses exploring potential study-level outlier influence on the estimated associations between anti-gSG6 IgG seroprevalence, HBR, and EIR showed no evidence of bias (effect estimates for each sensitivity analysis were consistent with model estimates overall) for studies identified as exhibiting potential influence (HBR: n = 6; EIR: n = 6).

## Discussion

This systematic review and multilevel modelling analysis provides the first quantification of a positive non-linear association between seroprevalence of An. gambiae gSG6 IgG antibodies and HBR and demonstrated that its magnitude varied with respect to the DVS present in the area. Importantly, this review identified a paucity of studies conducted outside of Africa, as well as investigating salivary antigens representing different Anopheles spp. and antigenic targets. gSG6 antibodies were positively associated with the prevalence of Plasmodium spp. infection as well as established epidemiological measures of malaria transmission: malaria endemicity class and EIR. Overall, our results demonstrate that antibody seroprevalence specific for Anopheles spp. salivary antigens has the potential to be an effective measure of vector exposure and malaria transmission at the population and, potentially, individual level.

An. gambiae gSG6 IgG seropositivity increased with increasing HBR, although these increases had diminishing impact on An. gambiae gSG6 IgG seropositivity at higher levels of HBR (approximately greater than two bites per person per night). In our study, 17 studies performed across Africa (Angola, Benin, Burkina Faso, Cote d’Ivoire, and Senegal) and the Asia Pacific (Cambodia, Myanmar, and the Solomon Islands) reported an HBR < 2, demonstrating the applicability of gSG6 as a biomarker of HBR across a broad range of malaria-endemic regions. We also observed that the association was strongest in areas where An. gambiae s.l. was the only DVS (i.e. concordant An. gambiae species-specific HBR with An. gambiae gSG6 antibodies). Associations, albeit weaker, were also observed between discordant species-specific HBR and gSG6, most likely because the An. gambiae SG6 gene shares moderate sequence identity with vector species that are dominant in other regions (Africa: 80% An. funestus; Asia: 79% Anopheles stephensi and Anopheles maculatus; 54% An. dirus; Pacific: 52.5% Anopheles farauti), and is absent from the DVS of the Americas (An. albimanus and An. darlingi) (Arcà et al., 2017). The generalisability of An. gambiae gSG6 IgG as a biomarker of exposure to other Anopheles spp. may therefore be limited. However, our review also identified a paucity of studies investigating additional salivary antigenic targets and Anopheles species not present in Africa. The identification of novel salivary antigens that are species-specific will be valuable in quantifying exposure to the other Anopheles vectors that share limited identity with An. gambiae SG6 (such as An. farauti and An. dirus), as well as Anopheles spp. which lack SG6 (as done for An. albimanus and An. darlingi; Londono-Renteria et al., 2020a; Londono-Renteria et al., 2020b). An Anopheles species-specific serological platform could advance vector surveillance by more accurately capturing exposure to DVS in the South American and Asia Pacific regions which exhibit diverse biting behaviours and vector competence (DVS typically bite outdoors during the night and day, respectively; The Malaria Atlas, 2017; Sinka et al., 2012; Sinka et al., 2010; Trung et al., 2005; Herrera et al., 2015; Chaumeau et al., 2018), as well as the increasing threat of urban malaria from An. stephensi in Africa (Takken and Lindsay, 2019; Sinka et al., 2020).

This review demonstrated that the prevalence of Anopheles salivary antibodies increased with increasing prevalence of Plasmodium spp. infection (although confidence intervals were wide and we observed heterogeneity in the effect between studies) as well as established epidemiological measures of malaria transmission: malaria endemicity class and EIR. Anti-salivary antibodies, such as SG6 IgG, may therefore have the potential to serve as a proxy measure for receptivity of a population to sustain malaria transmission. Their application could be particularly relevant in pre-elimination areas, or non-endemic areas under threat of imported malaria, where Anopheles salivary antibodies are more readily detectable than parasites; salivary antibodies were predicted to be prevalent (20%) in areas defined as eliminating malaria (<1% PfPR2-10). Furthermore, if SG6 IgG seroprevalence can be effectively combined with a measurement of the sporozoite index, salivary antibodies as a marker of HBR could help overcome sensitivity limitations of EIR in low transmission areas. Additional measures could include estimates of malaria prevalence or serological biomarkers that are species- or life stage-specific (e.g. Plasmodium spp. pre-erythrocytic antigens as biomarkers for recent parasite inoculation). Indeed, positive associations between antibodies specific for Plasmodium spp. pre-erythrocytic and blood stage antigens with gSG6 were demonstrated in analyses of data from diverse malaria-endemic areas. Serological tools combining salivary antigens with antigens specific for the different Plasmodium spp. could be easy to employ and complement malaria surveillance programmes. These tools may be particularly useful in the Asia Pacific, a region of relatively low malaria transmission with goals of elimination, but the highest burden of P. vivax malaria where blood stage infection can be caused by relapses from dormant liver stages. In these areas, parasite prevalence may therefore overestimate ongoing malaria transmission, making vector surveillance tools essential to informing elimination strategies in the Asia Pacific and other regions where P. vivax is endemic.

The gold standard entomological measures HBR and EIR provide crude population-level estimates of vector and malaria exposure that are specific in space and time and preclude investigation of individual-level heterogeneity and natural transmission dynamics. Our study demonstrated that salivary biomarkers measured at the individual level, such as gSG6 IgG, can be used to quantify total vector exposure at the population level, without requiring laborious entomological experiments. However, validating an individual-level serological measure, which demonstrates considerable individual-level variation, against the imperfect population-level gold standards of HBR and EIR is challenging and reflected in the variation in study-specific estimates in the association between gSG6 IgG and HBR in modelling analyses. However, the accuracy of salivary antibodies to measure individual-level exposure to Anopheles bites is yet to be validated; literature searches identified no studies investigating this association at the individual level. Without detailed measurements of individual-level vector exposure, or a detailed knowledge of the half-life of Anopheles salivary antibodies post biting event, the true accuracy of salivary antibodies, such as SG6 IgG, to measure individual-level HBR remains unknown. This knowledge is particularly pertinent where Anopheles salivary biomarkers might be applied to assess the effectiveness of a vector control intervention or used to measure temporal changes in malaria transmission; particularly in areas or populations where there is considerable heterogeneity in individual-level risk of Anopheles exposure (e.g. unmeasured outdoor biting due to occupational exposure for forest workers; Sandfort et al., 2020).

The broad nature of our inclusion and quality criteria was a key strength of our systematic review, which aimed to provide a comprehensive analysis of all Anopheles salivary biomarkers and determine their associations with entomological and malariometric measures of transmission. However, this review has two main limitations. First, despite the inclusive nature, assessment of the external validity of the review revealed a moderate risk of bias; some studies exhibited a high risk of selection bias as they were performed in specific high-risk populations not representative of the overall population (i.e. children only). This is accounted for to some degree by specification of a random effect (i.e. intercept) for study, which accounts for unmeasured study-specific factors that may introduce study-specific measurement error to measurement of the outcome. Second, with respect to internal validity, there may be potential selection bias introduced by the exclusion of studies reporting zero HBR (7 observations from three studies; Rizzo et al., 2011b; Pollard et al., 2019; Sagna et al., 2013b), EIR (22 observations from three studies; Ya-Umphan et al., 2017; Rizzo et al., 2011b; Soma et al., 2018), and malaria prevalence (15 observations from three studies; Idris et al., 2017; Sagna et al., 2013b; Kerkhof et al., 2016) estimates, given we modelled the log of these factors. However, adding a small constant (e.g. 0.001) to a zero value to permit modelling of a log estimate can also introduce considerable bias (i.e. seemingly small differences between values become very large on the log scale). In light of this, we also chose to provide estimates of association and gSG6 IgG seroprevalence according to a selected range of epidemiologically relevant hypothetical HBRs (no widely accepted HBR classification exists in the literature) and according to widely accepted, discrete, endemicity classes according to MAP estimates (which permitted inclusion of all studies) to provide epidemiological context. However, there is the potential for misclassification of malarial endemicity class derived from geospatially extracted MAP predictions of PfPR2-10 which increase in uncertainty in areas with scarce data. Similarly, we used MAP vector occurrence data to inform DVS categories for 7 (out of 42) studies. Cross-referencing these 7 studies with a 2017 updated database for African vectors (using data for the nearest neighbouring village) identified 10 discrepant datapoints from 3 studies (from a total of 28 datapoints from 7 studies) (Snow, 2017). Any misclassification events may cause us to underestimate the standard error in the effect of malaria endemicity class and DVS on gSG6 IgG.

### Conclusions

In order to advance progress towards malaria elimination, the World Health Organization has called for innovative tools and improved approaches to enhance vector surveillance and monitoring and evaluation of interventions (World Health Organization, 2017). Our systematic review has provided evidence that Anopheles salivary antibodies are serological biomarkers of vector and malaria exposure, by quantifying their positive association with Anopheles-HBR and established epidemiological measures of malaria transmission. These salivary biomarkers have the potential to replace crude population-level estimates of entomological indices with a precise and scalable tool that measures Anopheles vector exposure at the individual level. This approach could be expanded into a serosurveillance tool to assess the effectiveness of vector control interventions, define heterogeneity in malaria transmission, and inform efficient resource allocation that would ultimately accelerate progress towards elimination.
