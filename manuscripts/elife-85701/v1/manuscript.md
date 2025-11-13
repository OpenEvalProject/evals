# Exploring factors shaping antibiotic resistance patterns in Streptococcus pneumoniae during the 2020 COVID-19 pandemic

## Authors

- Aleksandra Kovacevic<sup>1</sup> ([ORCID: 0000-0001-9740-6207](https://orcid.org/0000-0001-9740-6207)) †
- David RM Smith<sup>1</sup>
- Eve Rahbé<sup>1</sup> ([ORCID: 0000-0002-3828-3910](https://orcid.org/0000-0002-3828-3910))
- Sophie Novelli<sup>2</sup>
- Paul Henriot<sup>3</sup>
- Emmanuelle Varon<sup>6</sup>
- Robert Cohen<sup>7</sup>
- Corinne Levy<sup>7</sup>
- Laura Temime<sup>3</sup> ([ORCID: 0000-0002-8850-5403](https://orcid.org/0000-0002-8850-5403))
- Lulla Opatowski<sup>1</sup>

### Affiliations

1. Institut Pasteur, Université Paris Cité, Epidemiology and Modelling of Antibiotic Evasion (EMAE) unit Paris France ([ROR:0495fxg12](https://ror.org/0495fxg12))
2. Université Paris-Saclay, Université de Versailles Saint-Quentin-en-Yvelines, Inserm U1018, CESP, Anti-infective evasion and pharmacoepidemiology team Montigny-Le-Bretonneux France ([ROR:01ed4t417](https://ror.org/01ed4t417))
3. Modélisation, épidémiologie et surveillance des risques sanitaires (MESuRS), Conservatoire national des arts et métiers Paris France ([ROR:0175hh227](https://ror.org/0175hh227))
4. Health Economics Research Centre, Nuffield Department of Health, University of Oxford Oxford United Kingdom ([ROR:052gg0110](https://ror.org/052gg0110))
5. PACRI unit, Institut Pasteur, Conservatoire national des arts et métiers Paris France ([ROR:0175hh227](https://ror.org/0175hh227))
6. Centre National de Référence des Pneumocoques, Centre Hospitalier Intercommunal de Créteil Créteil France ([ROR:0175hh227](https://ror.org/0175hh227))
7. Institut Mondor de Recherche Biomédicale-Groupe de Recherche Clinique Groupe d’Etude des Maladies Infectieuses Néonatales et Infantiles (IMRB-GRC GEMINI), Université Paris Est, 94000 Créteil France ([ROR:04qe59j94](https://ror.org/04qe59j94))
8. Groupe de Pathologie Infectieuse Pédiatrique (GPIP), 06200 Nice France
9. Unité Court Séjour, Petits Nourrissons, Service de Néonatologie, Centre Hospitalier, Intercommunal de Créteil Créteil France ([ROR:04n1nkp35](https://ror.org/04n1nkp35))
10. Association Clinique et Thérapeutique Infantile du Val-de-Marne (ACTIV), 94000 Créteil France ([ROR:03t4ktv29](https://ror.org/03t4ktv29))
11. Association Française de Pédiatrie Ambulatoire (AFPA), 45000 Orléans France ([ROR:0495fxg12](https://ror.org/0495fxg12))

† Corresponding author

## Abstract

Non-pharmaceutical interventions implemented to block SARS-CoV-2 transmission in early 2020 led to global reductions in the incidence of invasive pneumococcal disease (IPD). By contrast, most European countries reported an increase in antibiotic resistance among invasive Streptococcus pneumoniae isolates from 2019 to 2020, while an increasing number of studies reported stable pneumococcal carriage prevalence over the same period. To disentangle the impacts of the COVID-19 pandemic on pneumococcal epidemiology in the community setting, we propose a mathematical model formalizing simultaneous transmission of SARS-CoV-2 and antibiotic-sensitive and -resistant strains of S. pneumoniae. To test hypotheses underlying these trends five mechanisms were built into the model and examined: (1) a population-wide reduction of antibiotic prescriptions in the community, (2) lockdown effect on pneumococcal transmission, (3) a reduced risk of developing an IPD due to the absence of common respiratory viruses, (4) community azithromycin use in COVID-19 infected individuals, (5) and a longer carriage duration of antibiotic-resistant pneumococcal strains. Among 31 possible pandemic scenarios involving mechanisms individually or in combination, model simulations surprisingly identified only two scenarios that reproduced the reported trends in the general population. They included factors (1), (3), and (4). These scenarios replicated a nearly 50% reduction in annual IPD, and an increase in antibiotic resistance from 20% to 22%, all while maintaining a relatively stable pneumococcal carriage. Exploring further, higher SARS-CoV-2 R0 values and synergistic within-host virus-bacteria interaction mechanisms could have additionally contributed to the observed antibiotic resistance increase. Our work demonstrates the utility of the mathematical modeling approach in unraveling the complex effects of the COVID-19 pandemic responses on AMR dynamics.

## Introduction

In the early 2020, international responses to the coronavirus disease 2019 (COVID-19) pandemic led to unprecedented worldwide change in population mixing, healthcare-seeking behavior, and infection prevention and control practices. This modified the ecology and epidemiology of many infectious diseases at a global scale. Strong impacts of COVID-19 on infectious disease dynamics have been reported for common viral and bacterial respiratory infections, sexually transmitted pathogens like HIV, vector-borne diseases like dengue, and even non-communicable diseases (Braunstein et al., 2020; Brueggemann et al., 2021; Chen et al., 2022; Palmer et al., 2020). Antimicrobial resistance (AMR), however, remains one of the leading threats to global health. In 2019, estimates showed that AMR in clinically relevant bacteria was associated with 4.95 million deaths, of which 1.27 million were described as directly attributable to resistance (Murray et al., 2022). Impacts of the COVID-19 pandemic on AMR dynamics remain relatively poorly understood.

A joint report from the WHO and European Centre for Disease Prevention and Control (ECDC) has reported 2020 AMR trends across 29 European countries for eight antibiotic-resistant bacterial pathogens of concern, including S. pneumoniae (European Centre for Disease Prevention and Control and World Health Organization, 2022). While the situation varies widely across bacterial species, antimicrobial groups, and regions, most European countries, including France, documented an increase in pneumococcal resistance to both penicillin and macrolides between 2019 and 2020. The resistance rates rose from 12.2% in 2019 to 15.6% in 2020 for penicillin and from 14.5% in 2019 to 16.9% in 2020 for macrolides, as reported in the EU/EEA (European Centre for Disease Prevention and Control and World Health Organization, 2022). However, increased pneumococcal resistance was accompanied by a sharp worldwide decline in invasive pneumococcal disease (IPD) incidence (Brueggemann et al., 2021; Shaw et al., 2023).

Similar declines in bacterial disease during early waves of COVID-19 have been observed in the context of sentinel community-acquired infections in New Zealand (Duffy et al., 2021), IPDs in Taiwan (Chien et al., 2021) and Hong Kong (Teng et al., 2022), and lower respiratory tract infections in China (Chen et al., 2021). Yet, surprisingly, a growing number of studies have reported mostly stable pneumococcal carriage throughout the COVID-19 pandemic containment, including among infants in Belgium (Willen et al., 2021), children in Vietnam (Nation et al., 2023), Serbia (Petrović et al., 2022), France (Rybak et al., 2022), South Africa (Olwagen et al., 2024), and Israel (Dagan et al., 2023), adults in Connecticut (Wyllie et al., 2023), and households in Seattle (Bennett et al., 2023). In contrast, a study conducted in Denmark reported a decrease in pneumococcal carriage among older adults during the COVID-19 lockdown (Tinggaard et al., 2023).

Understanding the cause of these trends is not straightforward, as many responses to the COVID-19 pandemic, such as the implementation of non-pharmaceutical interventions (NPIs), changes in healthcare-seeking behavior, and alterations in antibiotic prescribing, occurred over the period (Knight et al., 2021). To gain a comprehensive understanding of the changes in AMR epidemiology during the COVID-19 pandemic, it is essential to simultaneously consider a range of scales and indicators. These include the rates of incidence of invasive bacterial diseases (IBDs), the proportion of antibiotic-resistant isolates among total invasive bacterial isolates, and the prevalence of asymptomatic bacterial carriage in healthy individuals.

Several mechanisms may underlie the explanation of these contrasting observations. First, NPIs implemented to block SARS-CoV-2 transmission, such as lockdowns and mask mandates, may have led to reduced bacterial transmission. Containment measures also massively reduced circulation of common respiratory viruses, which are known to be associated with IBD (Domenech de Cellès et al., 2019; Smith and Opatowski, 2021). Second, the lockdown was associated with reductions in primary care consultations (Homeniuk and Collins, 2021; Read et al., 2023; Zhang et al., 2021) leading to a global decrease of antibiotic prescriptions (Högberg et al., 2021). In contrast, frequent antibiotic prescribing to COVID-19 outpatients may have exacerbated AMR (Clancy et al., 2020; Knight et al., 2021). Differences in the duration of pneumococcal carriage may have also played a role (Lehtinen et al., 2017). Finally, potential within-host interactions between SARS-CoV-2 and S. pneumoniae could also have an impact on infection risk (Amin-Chowdhury et al., 2021), although strong evidence for such interactions remains limited (Wong et al., 2023).

Mathematical models incorporating the co-transmission of multiple pathogens within the same host population provide a framework for investigating different hypotheses that underlie the observed patterns in antibiotic resistance and incidence of IPD in S. pneumoniae and help to enhance our understanding of the mechanisms involved. Co-circulation models have been used previously to disentangle the public health consequences of interactions between pathogens such as influenza and S. pneumoniae (Arduin et al., 2017; Domenech de Cellès et al., 2019; Shrestha et al., 2013) and could similarly be used to understand impacts of the COVID-19 pandemic on pathogens coinciding with SARS-CoV-2. However, in a systematic PubMed search conducted on 4 December 2023, we identified no epidemiological models describing the simultaneous transmission of SARS-CoV-2 and antibiotic-resistant bacteria specific to the community setting (Appendix 1).

Here, to disentangle how the COVID-19 pandemic has impacted the epidemiological dynamics of antibiotic resistance in S. pneumoniae, we propose a mathematical model that formalizes the transmission of SARS-CoV-2 and both antibiotic-sensitive and -resistant strains of S. pneumoniae in the community setting, and which includes mechanistic impacts of COVID-19 burden on epidemiological parameters. Through simulation, we assess all possible combinations of these mechanisms to evaluate their overall impact on IPD incidence, antibiotic resistance, and the prevalence of pneumococcal carriage. Furthermore, we assess the changes in the incidence of antibiotic-resistant IPD as we vary the basic reproduction number (R0) of SARS-CoV-2 during the first COVID-19 outbreak in Europe. We also consider assumed within-host pathogen interactions between SARS-CoV-2 and S. pneumoniae.

## Results

### Antibiotic resistance trends and incidence of invasive pneumococcal disease in 2020

In routine surveillance data reported to the European Antimicrobial Resistance Surveillance Network (EARS-Net), most European countries reported an increase in antibiotic resistance in S. pneumoniae from 2019 to 2020, as indicated by increases in the proportion of invasive isolates with phenotypic resistance to both penicillin and macrolides (Figure 1A). On the contrary, the total number of reported invasive isolates in the EU/EEA decreased by 44.3% from 2019 to 2020 (European Centre for Disease Prevention and Control and World Health Organization, 2022) suggesting a decrease in incidence of IPD (Appendix 2—table 1).

![Figure 1.](https://cdn.elifesciences.org/articles/85701/elife-85701-fig1-v1.jpg)

**Figure 1.:** (A) The proportion of invasive S. pneumoniae isolates resistant to penicillin and macrolides (azithromycin/ clarithromycin/ erythromycin) reported to EARS-Net (European Antimicrobial Resistance Surveillance Network) for 24 European countries. Error bars show 95% confidence intervals. (B) The proportion of invasive S. pneumoniae isolates resistant to penicillin (MIC >0.064 mg/L) and macrolides (erythromycin) according to age. Error bars show 95% confidence intervals. The total number of invasive pneumococcal isolates reported in France decreased by 45.1% from 2019 to 2020 (from 1119–614). Data are provided by the French National Reference Center for Pneumococci.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/85701/elife-85701-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** The proportion of invasive S. pneumoniae isolates resistant to penicillin (A) and macrolides (B) according to age. Error bars show 95% confidence intervals. Across the period 2017–2020, a consistent decline in antibiotic resistance is observed for both penicillin and macrolides. Notably, this general trend experienced an anomaly in 2020, coinciding with the onset of the COVID-19 pandemic. Data are provided by the French National Reference Center for Pneumococci.

Invasive pneumococcal isolate data for France provided by the French National Reference Center for Pneumococci (CNRP) revealed similar trends. In France, the total number of reported invasive pneumococcal isolates decreased by 45.1% from 2019 to 2020 (from 1119–614), while antibiotic resistance in S. pneumoniae isolates to penicillin and macrolides showed an increasing trend from 26.2% in 2019 to 35.5% in 2020 for penicillin, and from 20.9% in 2019 to 23.0% in 2020 for macrolides (Figure 1B). General decreasing trend in antibiotic resistance from 2017 to 2019 in S. pneumoniae was interrupted in 2020 (Figure 1—figure supplement 1). These variations in antibiotic resistance manifested differently across age, with some age groups showing an increase in antibiotic resistance in 2020 compared to 2019, while others showed no significant change (Figure 1B).

### Coinfection model of SARS-CoV-2 and Streptococcus pneumoniae

As mentioned above, several mechanisms may underlie the explanation of these contrasting observations (Figure 2A). COVID-19 NPIs may have led to reduced person-to-person bacterial transmission, potentially contributing to reduced rates of IPD incidence. These containment measures also massively reduced circulation of common respiratory viruses and the incidence of influenza-like-illnesses (ILIs). Respiratory viruses are known triggers and risk factors for developing an IBD from otherwise asymptomatic carriage; in that context, their reduction may have led to reduced infection risk (Domenech de Cellès et al., 2019; Smith and Opatowski, 2021). Due to reductions in primary care consultations in 2020, 26 European countries reported an estimated average decrease of 18.3% in overall antibiotic consumption, aligning with the global trend of reduced antibiotic prescriptions compared to 2019 (Högberg et al., 2021). On the other hand, frequent prescribing of azithromycin, a macrolide antibiotic initially hypothesized to be effective in COVID-19 treatment, has raised concerns for pandemic-associated antimicrobial overuse or misuse and may have exacerbated AMR during and following the first wave of the pandemic (Clancy et al., 2020; Knight et al., 2021; Kournoutou and Dinos, 2022; Langford et al., 2021; PRINCIPLE Trial Collaborative Group, 2021; Rusic et al., 2021). There are still uncertainties about pneumococcal ecology and the evolutionary processes that enable the robust coexistence of strains sensitive and resistant to antibiotics. The role of carriage duration, along with the impact of antibiotic consumption, is also not fully understood in this context. Longer carriage duration of antibiotic-resistant pneumococcal strains is a proposed explanation for this coexistence (Lehtinen et al., 2017). If so, antibiotic-resistant pneumococcal strains may have had an advantage during the lockdown period due to smaller clearance rates, ultimately leading to an increase in antibiotic resistance. Finally, among individuals with COVID-19, potential within-host interactions between SARS-CoV-2 and S. pneumoniae could also have had an impact on bacterial colonization and infection dynamics (Amin-Chowdhury et al., 2021).

![Figure 2.](https://cdn.elifesciences.org/articles/85701/elife-85701-fig2-v1.jpg)

**Figure 2.:** (A) Non-pharmaceutical interventions (NPIs) implemented to control SARS-CoV-2 transmission (lockdown, face mask use, improved hygiene practices, travel restrictions, quarantine, telemedicine, and physical distancing) may also modify transmission of other pathogens, in addition to impacting antibiotic prescribing due to altered inter-individual contact and health-care seeking behavior. (B) SEIR (Susceptible-Exposed-Infected-Recovered) model with antibiotic treatment compartments depicts interaction between SARS-CoV-2 infection and antibiotic prescribing, including both general community prescribing and azithromycin prescribing among individuals infected with SARS-CoV-2. (C) Diagram depicting how pneumococcal colonization and the community antibiotic prescribing are affected by the COVID-19 pandemic impacts. Initiation of antibiotic treatment is assumed independent of bacterial carriage, reflecting widespread bystander selection for commensal bacteria like S. pneumoniae. For a complete modeling framework, see section S2 in Supporting Information.

To test mechanistic impacts of responses to the COVID-19 pandemic on pneumococcal epidemiology, we developed a compartmental, deterministic transmission model describing infection with SARS-CoV-2 being introduced on 1 Jan 2020 (Figure 2B) after colonization with S. pneumoniae reached an equilibrium in a large, well-mixed human population (Figure 2C). Two lockdowns were implemented in the model in agreement with the two lockdowns implemented in France in 2020. The model was parameterized to S. pneumoniae and five mechanisms were built in into the model: (1) a population-wide reduction of antibiotic prescriptions in the community by 18% due to the reduced healthcare-seeking behavior, (2) lockdown reducing pneumococcal transmission by 25%, (3) a reduced risk of developing an IPD from asymptomatic carriage due to the absence of common respiratory viruses during the first lockdown (reduced by a factor IPDrisk = 0.2), which continues after the first lockdown, albeit at a diminished level (IPDrisk = 0.4), (4) community azithromycin use in 10% of COVID-19 infected individuals, (5) and a longer carriage duration of antibiotic-resistant pneumococcal strains giving them a fitness advantage over antibiotic-resistant strains (40 vs 30 days).

### Exploring the mechanisms and identifying the optimal scenario for explaining reported trends

We conducted assessments on five distinct hypotheses, each characterized by a precise underlying mechanism, and explored these hypotheses in combination within 31 pandemic scenarios, along with two pre-pandemic (baseline) scenarios, which assume no SARS-CoV-2 circulation in the population and allow for the same 30-day carriage duration (pre-pandemic 1) of both antibiotic-sensitive and -resistant strains (ds=dR) or a longer, 40-day carriage duration (pre-pandemic 2) of -resistant strains (ds> dR) (Table 1).

**Table 1.**
 Five mechanisms implemented in 31 pandemic scenarios proposed to explain the reported trends of IPD incidence, antibiotic resistance, and pneumococcal carriage in S. pneumoniae.Scenarios explore all possible combinations of mechanisms proposed to test hypotheses that can explain the reported trends of annual invasive pneumococcal disease incidence (annual no. of cases per 100,000 inhabitants), antibiotic resistance (% of annual antibiotic-resistant IPD cases among total IPD cases), and % change in the pneumococcal carriage prevalence at the end of the first 60-day lockdown compared the prevalence before the lockdown. Model simulations were initiated assuming the initial 20% antibiotic resistance. Two pre-pandemic scenarios assume no SARS-CoV-2 circulation in the population and allow for the same 30-day carriage duration of both antibiotic-sensitive and -resistant strains (dS = dR) or a longer, 40-day carriage duration of -resistant strains (dR > dS) . When implemented, these five mechanisms assume 18% reduction in community antibiotic prescribing, a reduced risk of developing an IPD during (0.2) and after the first lockdown (0.4), a 25% reduction in transmission of pneumococcal carriage during the first lockdown, a 10% of azithromycin use among COVID-19 infected individuals, and a longer 40-day carriage duration of -resistant strains. For a full list of parameters see Appendix 2—table 2. Reported trends in European countries showed a decrease in annual IPD incidence by 44.3% on average, an increase in antibiotic resistance, and generally stable asymptomatic pneumococcal carriage in healthy individuals during the first lockdown period. Only scenarios S19 and S29 fulfill all three reported trends during the COVID-19 pandemic in 2020 simultaneously while accounting for the reported reduction in community antibiotic prescribing ($d_{S}$ = carriage duration of antibiotic-sensitive pneumococcal strains; $d_{R}$ = carriage duration of antibiotic-resistant pneumococcal strains; PENI = penicillin; ERY = erythromycin).


<table>
  <thead>
    <tr>
      <th colspan="9"></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">Scenarios</td>
      <td colspan="5">Mechanisms</td>
      <td rowspan="2">IPD inc.</td>
      <td rowspan="2">AR (%)</td>
      <td rowspan="2">Sp. (%)</td>
    </tr>
    <tr>
      <td>1</td>
      <td>2</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
    </tr>
    <tr>
      <td>Pre-pandemic 1: (dS = dR)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>10.8</td>
      <td>20.0</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>Pre-pandemic 2: (dR &gt; dS)</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>x</td>
      <td>11.3</td>
      <td>20.0</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>Pandemic: S1</td>
      <td>x</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>10.9</td>
      <td>19.2</td>
      <td>+1.3</td>
    </tr>
    <tr>
      <td>S2</td>
      <td></td>
      <td>x</td>
      <td></td>
      <td></td>
      <td></td>
      <td>8.9</td>
      <td>20.1</td>
      <td>–36.1</td>
    </tr>
    <tr>
      <td>S3</td>
      <td></td>
      <td></td>
      <td>x</td>
      <td></td>
      <td></td>
      <td>5.9</td>
      <td>20.0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>S4</td>
      <td></td>
      <td></td>
      <td></td>
      <td>x</td>
      <td></td>
      <td>9.9</td>
      <td>23.7</td>
      <td>–9.1</td>
    </tr>
    <tr>
      <td>S5</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td>x</td>
      <td>11.3</td>
      <td>20.0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>S6</td>
      <td>x</td>
      <td>x</td>
      <td></td>
      <td></td>
      <td></td>
      <td>9.1</td>
      <td>19.4</td>
      <td>–35.2</td>
    </tr>
    <tr>
      <td>S7</td>
      <td>x</td>
      <td></td>
      <td>x</td>
      <td></td>
      <td></td>
      <td>6.0</td>
      <td>19.4</td>
      <td>+1.3</td>
    </tr>
    <tr>
      <td>S8</td>
      <td>x</td>
      <td></td>
      <td></td>
      <td>x</td>
      <td></td>
      <td>10.1</td>
      <td>22.9</td>
      <td>–8.0</td>
    </tr>
    <tr>
      <td>S9</td>
      <td>x</td>
      <td></td>
      <td></td>
      <td></td>
      <td>x</td>
      <td>11.5</td>
      <td>19.3</td>
      <td>+1.3</td>
    </tr>
    <tr>
      <td>S10</td>
      <td></td>
      <td>x</td>
      <td>x</td>
      <td></td>
      <td></td>
      <td>5.2</td>
      <td>20.0</td>
      <td>–36.1</td>
    </tr>
    <tr>
      <td>S11</td>
      <td></td>
      <td>x</td>
      <td></td>
      <td>x</td>
      <td></td>
      <td>8.9</td>
      <td>20.1</td>
      <td>–36.1</td>
    </tr>
    <tr>
      <td>S12</td>
      <td></td>
      <td>x</td>
      <td></td>
      <td></td>
      <td>x</td>
      <td>9.4</td>
      <td>20.9</td>
      <td>–34.3</td>
    </tr>
    <tr>
      <td>S13</td>
      <td></td>
      <td></td>
      <td>x</td>
      <td>x</td>
      <td></td>
      <td>5.6</td>
      <td>22.5</td>
      <td>–9.1</td>
    </tr>
    <tr>
      <td>S14</td>
      <td></td>
      <td></td>
      <td>x</td>
      <td></td>
      <td>x</td>
      <td>6.2</td>
      <td>20.0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>S15</td>
      <td></td>
      <td></td>
      <td></td>
      <td>x</td>
      <td>x</td>
      <td>10.4</td>
      <td>23.4</td>
      <td>–9.1</td>
    </tr>
    <tr>
      <td>S16</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td></td>
      <td></td>
      <td>5.3</td>
      <td>19.6</td>
      <td>–35.2</td>
    </tr>
    <tr>
      <td>S17</td>
      <td>x</td>
      <td>x</td>
      <td></td>
      <td>x</td>
      <td></td>
      <td>8.3</td>
      <td>22.4</td>
      <td>–41.3</td>
    </tr>
    <tr>
      <td>S18</td>
      <td>x</td>
      <td>x</td>
      <td></td>
      <td></td>
      <td>x</td>
      <td>9.6</td>
      <td>20.3</td>
      <td>–33.5</td>
    </tr>
    <tr>
      <td>S19</td>
      <td>x</td>
      <td></td>
      <td>x</td>
      <td>x</td>
      <td></td>
      <td>5.7</td>
      <td>22.0</td>
      <td>–8.0</td>
    </tr>
    <tr>
      <td>S20</td>
      <td>x</td>
      <td></td>
      <td>x</td>
      <td></td>
      <td>x</td>
      <td>6.3</td>
      <td>19.5</td>
      <td>+1.3</td>
    </tr>
    <tr>
      <td>S21</td>
      <td>x</td>
      <td></td>
      <td></td>
      <td>x</td>
      <td>x</td>
      <td>10.6</td>
      <td>22.7</td>
      <td>–7.9</td>
    </tr>
    <tr>
      <td>S22</td>
      <td></td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td></td>
      <td>5.0</td>
      <td>22.0</td>
      <td>–42.1</td>
    </tr>
    <tr>
      <td>S23</td>
      <td></td>
      <td>x</td>
      <td>x</td>
      <td></td>
      <td>x</td>
      <td>5.5</td>
      <td>20.6</td>
      <td>–34.3</td>
    </tr>
    <tr>
      <td>S24</td>
      <td></td>
      <td>x</td>
      <td></td>
      <td>x</td>
      <td>x</td>
      <td>8.7</td>
      <td>23.9</td>
      <td>–40.2</td>
    </tr>
    <tr>
      <td>S25</td>
      <td></td>
      <td></td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>5.9</td>
      <td>22.3</td>
      <td>–9.1</td>
    </tr>
    <tr>
      <td>S26</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td></td>
      <td>5.0</td>
      <td>21.6</td>
      <td>–41.3</td>
    </tr>
    <tr>
      <td>S27</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td></td>
      <td>x</td>
      <td>5.6</td>
      <td>20.1</td>
      <td>–33.5</td>
    </tr>
    <tr>
      <td>S28</td>
      <td>x</td>
      <td>x</td>
      <td></td>
      <td>x</td>
      <td>x</td>
      <td>8.8</td>
      <td>23.2</td>
      <td>–39.4</td>
    </tr>
    <tr>
      <td>S29</td>
      <td>x</td>
      <td></td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>5.9</td>
      <td>21.8</td>
      <td>–7.9</td>
    </tr>
    <tr>
      <td>S30</td>
      <td></td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>5.2</td>
      <td>22.5</td>
      <td>–40.2</td>
    </tr>
    <tr>
      <td>S31</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>x</td>
      <td>5.3</td>
      <td>22.1</td>
      <td>–39.4</td>
    </tr>
    <tr>
      <td></td>
      <td colspan="4"></td>
      <td colspan="3"></td>
      <td></td>
    </tr>
    <tr>
      <td>REPORTED TRENDS:</td>
      <td colspan="4">IPD inc.</td>
      <td colspan="3">AR (%)</td>
      <td>Sp. (%)</td>
    </tr>
    <tr>
      <td>Pre-pandemic (FR, 2019)</td>
      <td colspan="4">10.5 [10.3–10.7]</td>
      <td colspan="3">26.2 (PENI) and 20.9 (ERY)</td>
      <td>NA</td>
    </tr>
    <tr>
      <td>Pandemic (FR, 2020)</td>
      <td colspan="4">5.8 [5.7–5.9]</td>
      <td colspan="3">35.5 (PENI) and 23.0 (ERY)</td>
      <td>Stable</td>
    </tr>
    <tr>
      <td>Pandemic (EU/EEA, 2020)General trends</td>
      <td colspan="4">Decrease by 44.3% on avg.</td>
      <td colspan="3">Majority of EU countries report an increase</td>
      <td>Generally stable</td>
    </tr>
  </tbody>
</table>

_Mechanisms: (1) Reduced community antibiotic prescribing; (2) Lockdown effect on reducing transmission of S. pneumoniae; (3) Reduced risk of developing an IPD; (4) Community azithromycin use in COVID-19 infected individuals; (5) Longer carriage duration of antibiotic-resistant pneumococcal strains._

We assessed how different combinations of mechanisms may impact: (i) a change in the annual IPD incidence as compared to the pre-pandemic (baseline) period, (ii) antibiotic resistance rate in IPDs, defined as the annual number of antibiotic-resistant IPD cases over the total number of IPD cases, and (iii) daily prevalences of antibiotic-resistant and total pneumococcal carriage in a simulated population of 100,000 individuals (see Appendix 2—table 2 for parameter values). To identify scenarios most compatible with the reported trends, results from model simulations were compared to reported data trends from France in 2020 and more broadly to general EU/EEA reported trends that followed similar patterns. Surprisingly only two scenarios were compatible with reported trends. Scenarios S19 and S29 univocally reproduced increased antibiotic resistance in the general population (AR%) accompanied by a reduction in the annual IPD incidence by almost 50% (IPD inc) with generally stable pneumococcal carriage prevalence in healthy individuals during lockdown (Sp.). In contrast, model simulations revealed that a reduction in the community antibiotic consumption alone (–18%) could not explain the reported trends and generally led to a reduction of antibiotic resistance (Table 1, see scenario S1). Assuming a longer duration of antibiotic-resistant pneumococcal carriage alone did not explain either the rise in antibiotic resistance (Table 1, see scenario S5). Hypothesizing that lockdown reduced the transmission of pneumococcal carriage (by 25%) in addition to a reduced community antibiotic prescribing did not seem probable since, in simulations, this yielded a major reduction in pneumococcal carriage during containment measures in all scenarios where this mechanism was implemented. On the other hand, considering an indirect impact of lockdown on pneumococcal carriage where we implemented a reduction factor for the risk of developing and IPD from otherwise asymptomatic carriage due to the absence of viral respiratory infections during (IPDrisk = 0.2) and after lockdown (IPDrisk = 0.4) reproduced the reported reduction in the annual IPD incidence while maintaining a stable prevalence of pneumococcal carriage during lockdown (Table 1, see scenario S3). By itself however, this scenario did not allow to observe an increase in antibiotic resistance.

When we combined reduced antibiotic prescribing and a reduced risk of developing an IPD with community azithromycin use in a proportion of COVID-19 infected individuals, which remains in the body for an additional 15.5 days after the last dose, in a single scenario, this scenario satisfied the observed trends in AMR (Table 1, see scenario S19). A similar outcome was observed in scenario S29 when adding a longer carriage duration of antibiotic resistant strains on top of this, however, in the absence of community azithromycin use in COVID-19 infected (Table 1, see scenario S1, S5, S3, S19, and S20) trends of increasing antibiotic resistance cannot be reproduced. Therefore, our best model scenario for describing the observed trends combined: (1) a reduction in the overall community antibiotic consumption; (2) the assumption that lockdown effectively reduced SARS-CoV-2 transmission including transmission of other respiratory viruses, but not pneumococcal carriage transmission, indirectly reducing the risk of developing an IPD; (3) either identical or longer carriage durations of antibiotic-resistant strains compared to antibiotic-sensitive strains, and (4) the community azithromycin use in a proportion of COVID-19 infected individuals.

### Effect of age

Next, we used the pandemic scenario S19 that best explains the reported trends to test the model using different parameter combinations to mimic different subpopulations (children and the elderly) considering that SARS-CoV-2 infection risk, pneumococcal disease risk, disease severity, bacterial carriage prevalence, and antibiotic prescribing are all highly heterogeneous across age groups. Using scenario S19, we initialized the model with lower and higher baseline carriage prevalence (10%, 20%, and 30%) (Cohen et al., 2023; Rose et al., 2021; Rybak et al., 2022; Tinggaard et al., 2023; Wang et al., 2017), we varied durations of pneumococcal carriage (20, 30, and 45 days), pneumococcal invasion rate, and considered reductions of antibiotic consumption at various levels (–13%, –18%, and –39%) consistent with the French data along with a range of community azithromycin use in COVID-19 infected (0–20%). For a full list of parameters see Appendix 2—table 2. Simulations showed that annual IPD incidence decreased between 43% and 51% compared to the pre-pandemic (baseline) scenario for children, the elderly, and the general population (Figure 3, grey bars). Although the overall antibiotic prescribing in the community was reduced (between 13% and 39%), antibiotic resistance is expected to increase (from 20.1% up to 23.6% in the elderly and from 32.8% up to 36.0% in children) compared to the pre-pandemic period in all age groups and in all scenarios where azithromycin was used in COVID-19 infected individuals (Figure 3, red bars). Daily prevalence of total pneumococcal carriage remained relatively stable, exhibiting higher levels of decrease with increased azithromycin use, while the prevalence of antibiotic-resistant pneumococcal carriage is expected to increase since clearance of antibiotic-susceptible strains due to azithromycin use shifts the competitive balance in favor of the existing resistant strains (Figure 3, third panel).

![Figure 3.](https://cdn.elifesciences.org/articles/85701/elife-85701-fig3-v1.jpg)

**Figure 3.:** (A) The elderly (≥65 years-old) (B) general population (all ages), and (C) children (<5 years-old). Using pandemic scenario S19, which includes a combination of three different mechanisms: reduced community antibiotic prescribing, a reduced risk of developing an IPD, and community azithromycin use in COVID-19 infected individuals, we ran model simulations for three different subpopulations. For a full list of parameter values see Appendix 2—table 2. Annual IPD incidence (grey bars) decreased between 43% and 51% relative to the pre-pandemic (baseline) period with magnitude of a decrease depending on an age group and the level of azithromycin use in COVID-19 infected individuals. Antibiotic resistance (red bars) increased compared to the pre-pandemic (baseline) period in all age groups whenever azithromycin was used in COVID-19 infected. Black arrows indicate model outcomes that approximate the reported trends in antibiotic resistance in France for different age groups. Daily prevalence of total pneumococcal carriage remained relatively stable (solid-colored lines), exhibiting higher levels of decrease with increased azithromycin use. The prevalence of antibiotic-resistant pneumococcal carriage increased (dashed colored lines) over time in relation to SARS-CoV-2 outbreak (black dashed line) and higher azithromycin use. Highlighted time intervals (days 75–135 and 305–365) represent two lockdown periods.

General trends produced in model simulations using scenario S19 remained unchanged across different age groups. The extent of the impact depended on the combined magnitude of a decrease in the general antibiotic use in the community and a degree of azithromycin use in COVID-19 infected individuals belonging to a particular age group or a subpopulation. In the elderly (≥65 years-old) and the general population, antibiotic resistance is expected to increase due to azithromycin use in COVID-19 infected. Black arrows indicate model outcomes that approximate the reported trends in antibiotic resistance in France for different age groups including general population (Figure 3). Only in instances when there was no azithromycin use in COVID-19 infected individuals, we observed a decrease in antibiotic resistance relative to the pre-pandemic period (e.g. children <5 years-old). When combining the largest decrease in overall antibiotic use with no or minimal azithromycin use in COVID-19 infected individuals, we expect to see the largest decrease or no change in antibiotic resistance relative to the pre-pandemic period.

### Effect of SARS-CoV-2 basic reproduction number (R0) and within-host pathogen interactions on AMR

Considering that model simulations reproduced an absolute increase in antibiotic resistance comparable to that of 2% reported for macrolides in France but did not reproduce the reported larger increase in penicillin resistance, which was more than a 9% rise (35.5% relative increase) in France, we explored additional factors that may have amplified this increase. Using model scenario S19, we show that an association between higher values of SARS-CoV-2 R0 and a greater percentage of COVID-19 infected individuals taking azithromycin leads to increased cumulative incidence of antibiotic-resistant IPDs and elevated antibiotic resistance (Figure 4A). For example, if pre-lockdown R0 of SARS-CoV-2 was 3.8 instead of 3.2, model simulations predict an increase of 3.5% (23.5%) in antibiotic resistance from the pre-pandemic levels instead of 2%. As the R0 value increases, the impact of azithromycin use becomes more pronounced.

![Figure 4.](https://cdn.elifesciences.org/articles/85701/elife-85701-fig4-v1.jpg)

**Figure 4.:** Hypothetical within-host interactions contribute to an excess incidence of antibiotic-resistant IPDs. (A) Cumulative incidence of antibiotic-resistant IPDs and antibiotic resistance increase with greater values of SARS-CoV-2 R0 and higher percentage of the COVID-19 infected individuals taking azithromycin. The reproduction number for SARS-CoV-2 (R0) in the community corresponds to the most common estimates of R0 in France and other European countries ranging from R0=2–4 (Allieta et al., 2022; D’Arienzo and Coniglio, 2020; Di Domenico et al., 2020; Flaxman et al., 2020; Liu et al., 2020; Roux et al., 2020; Salje et al., 2020). (B) Annual excess in cumulative antibiotic-resistant IPD incidence in scenario S19 due to synergistic within-host ecological interactions compared to the same scenario with no within-host interactions and no azithromycin use (1.17 resistant IPD cases/100,000 inhabitants). A rate of disease progression increased by a factor $ψ_{c}=1$ (no within-host interaction) and $ψ_{c}=40$ in scenario S19 applied to the general population assuming azithromycin use in 10% of the infected individuals resulted in approximately 0.06 and 0.75 additional cases of antibiotic-resistant disease per 100,000 inhabitants over the course of 1 year, respectively, compared to the scenario S19 assuming no within-host interaction and no azithromycin use (indicated by the black arrow). For more details, see Appendix 2—figure 1.

Assuming within-host interactions where SARS-CoV-2 infection favors progression from pneumococcal colonization to disease $(ψ_{c}>1)$ , we found that surges in COVID-19 cases accompanied by increasing levels of azithromycin use lead to excess number of cases caused by antibiotic-resistant strains. Indeed, a rate of disease progression increased by a factor $ψ_{c}=40$ in scenario S19 with 10% of infected using azithromycin applied to the general population results in approximately 0.75 additional cases of antibiotic-resistant disease per 100,000 inhabitants over the course of 1 year compared to 0.06 additional cases if there are no within-host interactions (Figure 4B). This represents 5% rise in resistance from the pre-pandemic levels (25% relative increase).

## Discussion

We propose a novel co-circulation model describing the spread of SARS-CoV-2 and antibiotic-resistant bacteria in a community setting to show how human behavioral responses to the COVID-19 pandemic can differentially impact antibiotic resistance. Our model simulations assessed different hypotheses proposed to explain the observed trends of antibiotic resistance, IPD incidence, and pneumococcal carriage. We identified the most plausible mechanisms underlying the observed patterns of resistance and disease incidence, showing how lockdowns indirectly substantially reduce the incidence of IPD, while surges in COVID-19 cases accompanied by antibiotic prescribing in COVID-19 infected individuals increase antibiotic resistance.

Many studies have reported trends on the incidence of community-acquired bacterial infections since the onset of the pandemic (Brueggemann et al., 2021; Shaw et al., 2023). There was a significant reduction in the risk of invasive disease caused by S. pneumoniae (risk ratio 0·47; 95% CI 0·40–0·55; Shaw et al., 2023). Initially, this observation seemed to support the hypothesis that NPIs implemented to control SARS-CoV-2 transmission may have simultaneously reduced the incidence of bacterial infections by preventing bacterial transmission and acquisition (Brueggemann et al., 2021; Kadambari et al., 2022). Indeed, the scenario of lockdown impact on pneumococcal transmission reproduced such trends. However, incorporating a mechanism of reduced risk for developing an IPD due to the absence of circulation of common respiratory viruses led to similar estimates of the relative reduction in IPD incidence as reported in the EU/EEA for 2020 (Brueggemann et al., 2021; European Centre for Disease Prevention and Control and World Health Organization, 2022). This finding, coupled with the outcome of other studies that found a generally stable pneumococcal carriage prevalence in healthy individuals, both children and adults, during COVID-19 containment measures (Nation et al., 2023; Petrović et al., 2022; Rybak et al., 2022; Willen et al., 2021; Wyllie et al., 2023), supports the alternative hypothesis. This explanation accounts for the decreased incidence of IPD, rather than attributing it to reduced pneumococcal transmission, which resulted in a significant reduction in carriage according to the simulations (Smith and Opatowski, 2021). Furthermore, a study in Vietnam found that reductions in IPD associated with NPIs may be due to reductions in overall pneumococcal carriage density rather than carriage prevalence, driven by reductions in capsular pneumococcal carriage density frequently implicated in IPD (Nation et al., 2023). Considering that common respiratory viruses such as influenza increase pneumococcal carriage density, which contributes to transmission and disease, this hypothesis seems plausible (Alpkvist et al., 2015; Diavatopoulos et al., 2010; McCullers et al., 2010; Short et al., 2012; Wolter et al., 2014).

Globally, community antibiotic consumption dropped during the first year of the COVID-19 pandemic compared to the pre-pandemic period. Decreasing temporal trends were observed in England (Hussain et al., 2021), Canada (Mamun et al., 2021), the United States (Buehrle et al., 2021), China (Zhang et al., 2021), South Korea (Ryu et al., 2021), New Zealand (Duffy et al., 2021), and across European countries (Högberg et al., 2021). In France in particular, the number of antibiotic prescriptions decreased by 18.2% in the general population; however, this reduction ranged from 13% to 39% for the oldest and youngest age groups, respectively (Bara et al., 2022). These trends in antibiotic prescribing may largely be explained by reduced incidence of seasonal respiratory tract infections and reduced primary care consultations (Andrews et al., 2022; Homeniuk and Collins, 2021). On the other hand, the advent of telemedicine, pandemic-induced patient stress, and increased antibiotic demand may have partly offset prescription reductions due to decreased consultations and healthcare-seeking behavior (Hsu, 2020; Read et al., 2023). In a global analysis of antimicrobial sales, Khouja et al. found that antibiotic consumption initially increased by approximately 7% in March 2020, prior to subsequent declines through to August 2020 (Khouja et al., 2022). While overall antibiotic prescribing may have decreased, prescription of specific antibiotics has increased, particularly those associated with COVID-19 patient management. Across continents, a rise of 10% in monthly COVID-19 cases exhibited a correlative trend with elevated macrolide sales of 0.8%, 1.3%, and 1.5% in Europe, North America, and Africa, respectively (Nandi et al., 2023).

Community consumption of azithromycin, a macrolide, increased during the first year of the pandemic in multiple countries with significant variation across geographic locations and with greatest prescribing among older patients (Bara et al., 2022; Bednarčuk et al., 2023; Bogdanić et al., 2022; Crisafulli et al., 2021; Parveen et al., 2020; Weill et al., 2021). In an outpatient setting in southern Italy between February 2020 and January 2021, azithromycin represented 42.1% of all drug prescriptions to individuals diagnosed with COVID-19, while all other antibiotics combined represented just 20.9% (Crisafulli et al., 2021). A study in northwest London across two epidemic waves between January and August 2020 found that, among COVID-19 patients prescribed an antibiotic by a general practitioner during the study period, 31.5% received their prescription within 14 days of a positive SARS-CoV-2 test (Zhu et al., 2021). Two large USA-based studies have also described early pandemic antibiotic prescribing among COVID-19 patients. From April 2020 to April 2021, approximately 30% of outpatient COVID-19–related visits among Medicare beneficiaries (≥65 years-old) have resulted in a filled antibiotic prescription, 50.7% of which were for azithromycin (Tsay et al., 2022). For 0-to-5 year-olds and 45-to-64 year-olds, 4% and 16% of outpatient COVID-19–related visits have resulted in a filled antibiotic prescription, respectively (Wittman et al., 2023). In the Alsace region in France, there was a clear peak azithromycin prescribing during the first wave of the COVID-19 (Danion et al., 2023). During the first lockdown in France, community azithromycin consumption increased by 25.9%, with the increase varying from 13.4% to 47.3% depending on the week (Weill et al., 2021), while the overall number of azithromycin prescriptions across France in 2020 increased by 10.1% relative to 2019 (Bara et al., 2022). Azithromycin treatment usually lasts 3–5 days depending on the disease, but the drug stays in the system for about 15.5 days after the last dose due to the long half-life of more than 60 hr (Foulds et al., 1990; Girard et al., 2005). On the other hand, penicillin has an elimination half-life of approximately 1.4 hr and leaves the body in 7.7 hr after the last dose. This suggests that if azithromycin consumption increased during the first year of the pandemic, antibiotic exposure time also increased as a result, although the overall number of antibiotic prescriptions decreased. Moreover, the use of azithromycin has been associated with selection of both macrolide and non-macrolide resistance (Doan et al., 2020). In a study investigating the direct effect of antibiotic exposure on resistance in the oral streptococcal flora of healthy volunteers, use of azithromycin (500 mg once daily for 3 days) significantly increased the proportion of macrolide-resistant streptococci in healthy individuals (Malhotra-Kumar et al., 2007). Resistance peaked at day four in the azithromycin group and this increase remained significantly higher in the azithromycin group than in the placebo group until day 180 (Malhotra-Kumar et al., 2007). A clinical trial of mass azithromycin distributions for treating trachoma in Ethiopia resulted in an increase in resistant S. pneumoniae isolates among children under the age of 10 (Keenan et al., 2018; Keenan et al., 2015).

Our model simulations show that antibiotic resistance increases with surges in SARS-CoV-2 infections when there is a corresponding increase in azithromycin use, but that lockdowns can moderate this increasing trend by effectively limiting transmission of SARS-CoV-2 (Salje et al., 2020). Conversely, surges in azithromycin prescribing during SARS-CoV-2 outbreaks in the absence of effective measures to prevent transmission, as reported in certain regions and pandemic periods, may cause substantial increases in antibiotic resistance. Our model successfully captured the main trends of antibiotic resistance and IPD incidence observed in Europe in 2020 for S. pneumoniae. However, not all European countries reported an increase in antibiotic resistance. This inter-country heterogeneity may not be due only to heterogeneity of antibiotic use as shown in our model but may be attributed to other pandemic factors not directly implemented or assumed in the model scenario, such as different adherence to COVID-19 control measures across countries and different age groups, including impacts on disease surveillance and data reporting during the pandemic. Real-life scenarios are significantly more complicated and involve multiple alterations of many pandemic factors at different points in time and heterogeneity across populations (e.g. antibiotic prescribing increases in some demographic groups and decreases in others, multiple lockdowns, curfews, or telework).

In our model simulations, we used SARS-CoV-2 parameter value R0=3.2 (Liu et al., 2020) in the absence of population immunity, best reflecting epidemiological dynamics from early in the pandemic. The most common estimates of SARS-CoV-2 R0 in France and other European countries ranged from R0=2–4 (Flaxman et al., 2020; Liu et al., 2020). Modeling results suggest that higher SARS-CoV-2 R0 estimates combined with higher proportion of COVID-19 infected individuals using azithromycin exacerbated impacts of COVID-19 on antibiotic resistance (Figure 4A). However, the overall impacts of COVID-19 on AMR are difficult to predict, likely vary over the short, medium, and long term, and depend on the organism, setting, and subpopulation considered.

SARS-CoV-2 bacterial coinfection has been reported relatively rarely over the course of the pandemic, suggesting that most COVID-19 patients probably do not require antibiotic therapy (Garcia-Vidal et al., 2021; Karami et al., 2021; Langford et al., 2020), although extensive prophylactic antibiotic use may have limited observed co-infection incidence. The inflammatory immune response resulting from COVID-19 likely predisposes patients to subsequent progression to an IBD to some extent (Sender et al., 2021), but antibiotic use may also favor progression to IBD for patients colonized with drug-resistant strains (Baggs et al., 2018). We do not explicitly model the dynamics of interaction since strong evidence for such interactions remains limited (Wong et al., 2023). The results presented in Figure 4B suggest that such within-host interactions could have important consequences for the resistant IPD incidence during COVID-19 waves, especially in the elderly and high-risk groups. The model’s structure allows for easy integration of mechanistic interactions as more information becomes available on this phenomenon.

Our study focused on the general community, but COVID-19 distinctly influenced AMR in hospitals and long-term care facilities. Extensive antibiotic use in COVID-19 patients and disruptions to antibiotic stewardship programs may have increased antibiotic-resistant carriage in these settings. A meta-analysis conducted on studies published until June 2020 found that 68–81% of hospitalized COVID-19 patients and 74–94% in intensive care received antibiotics (Monnet and Harbarth, 2020). The disorganization in hospitals during the COVID-19 pandemic might have reduced antibiotic resistance surveillance, allowing resistant organisms to spread. However, the early implementation of antibiotic stewardship programs in March 2020, patient isolation, and widespread use of personal protective equipment (PPE) have mitigated this increase to some degree (Henig et al., 2021; Monnet and Harbarth, 2020; Seaton et al., 2020; Van Laethem et al., 2021). Models analyzing these impacts in hospitals contribute to understanding COVID-19’s specific role in the antibiotic resistance burden in different settings (Smith et al., 2023).

A limitation of our model is the lack of age structure and contact patterns between age groups, as SARS-CoV-2 infection risk, pneumococcal disease risk, disease severity, bacterial carriage prevalence and antibiotic prescribing are all highly heterogeneous across age groups. While this choice was made to keep the model as simple as possible, we tested the model using different parameter combinations to mimic different subpopulations (children and ≥65 years-old). This included varying durations of pneumococcal carriage, initializing the model with lower and higher baseline carriage prevalence, considering reductions of general antibiotic consumption at various levels, and varying a percentage of COVID-19 infected individuals using azithromycin. Simulations of the different age groups individually interestingly reproduced realistic trends by age.

In conclusion, we introduce the first epidemiological model outlining the impact of the COVID-19 pandemic on the dynamics of AMR in the community. Our work demonstrates the utility of mathematical modeling approach in unraveling the complex effects of the COVID-19 pandemic responses AMR dynamics. While our model was structured and parameterized based upon S. pneumoniae, its adaptability allows for application to various bacteria and epidemiological scenarios in the community (e.g. impacts of SARS-CoV-2-bacteria interactions in the context of seasonal outbreaks of endemic pathogens). Future research would benefit from fitting the model to real-world data for different bacterial species to enhance our understanding of AMR trends.

## Methods

### Streptococcus pneumoniae surveillance data

Antibiotic resistance trends reported in 2019 and 2020, provided by EARS-Net (European Antimicrobial Resistance Surveillance Network) were acquired from a joint 2022 report on AMR during 2020 by WHO and ECDC (European Centre for Disease Prevention and Control and World Health Organization, 2022). The annual incidence of S. pneumoniae invasive isolates for 2019 and 2020 was measured as the number of invasive isolates from blood or cerebrospinal fluid. The proportion of resistant isolates represents the proportion of isolates with phenotypic resistance to penicillin and macrolides using standardized bacterial culture methods and EUCAST breakpoints. Out of 28 European countries that reported antibiotic resistance data for S. pneumoniae, 24 countries had enough samples to establish 2019–2020 resistance trends for penicillin and macrolides. The resistance data for France, which were subsequently analyzed, were provided by the CNRP (The French National Reference Center for Pneumococci).

### Model structure

We developed a pathogen co-circulation model (Appendix 2—figure 2) written using systems of ordinary differential equations (ODEs) (Appendix 2-Equations; code available on GitHub, copy archived at Kovacevic, 2024). The model simultaneously describes potential infection with SARS-CoV-2 and colonization with antibiotic-sensitive and/or -resistant strains of S. pneumoniae in a well-mixed community population. SARS-CoV-2 infection is modeled by a Susceptible-Exposed-Infectious-Recovered (SEIR) process where individuals become exposed to SARS-CoV-2 at rate βC upon contact with other infected individuals. Infection begins with a non-infectious exposed period lasting 1/εdays and is followed by an infectious period lasting $1/\gamma^{C}$ days, eventually leading to recovery and immunization against future re-infection. Waning immunity and competitive multi-strain SARS-CoV-2 dynamics are not considered.

Individuals in S, E, I, and R compartments can be uncolonized with S. pneumoniae (U), colonized with either a drug-sensitive (CS) or a drug-resistant strain (CR), or co-colonized with two strains (CSS, CRR, CSR). Colonization with each respective strain is acquired at rates $\beta_{S}$ and $\beta_{s}f$ upon contact with other colonized individuals (Appendix 2—table 2). We assume a metabolic cost of resistance, whereby the drug-resistant strain has a reduced intrinsic transmission rate relative to the drug-sensitive strain due to reduced fitness, f. Bacterial carriage is cleared naturally after an average duration of $\frac{1}{\gamma^{S}}=\frac{1}{\gamma^{R}}=\frac{1}{\gamma^{SR}}=\frac{1}{\gamma^{SS}}=\frac{1}{\gamma^{RR}}$ days, which we assume to be the same for all types of carriers in our baseline scenario (in the scenarios assuming longer carriage duration of antibiotic-resistant strains, $\frac{1}{\gamma^{S}}=\frac{1}{\gamma^{SS}}$ and $\frac{1}{\gamma^{R}}=\frac{1}{\gamma^{SR}}=\frac{1}{\gamma^{RR}}$). We further assume that some share of the population is exposed to antibiotics at any given time, independent of bacterial carriage, with individuals initiating antibiotic therapy at rate $\tau$, which lasts for an average duration of $\frac{1}{r}$ days. Another model assumption is that a proportion $p_{az}$ of those infected with COVID-19 in the community (between 0% and 20% of individuals in an I compartment) receive azithromycin prescription from general practitioner reflecting azithromycin prescriptions in the early pandemic, while the rest of the infectious individuals ($1-p_{az}$) are exposed to the baseline antibiotic therapy. We assume baseline treatment duration of 7 days, on average, regardless of the antibiotic prescribed and without any assumed persistence of the antibiotic in the system after the last dose $\frac{1}{r}$ . In case of antibiotic treatment with azithromycin for COVID-19 infected individuals we assume the treatment lasts three days with antibiotics remaining in the system for additional 15.5 days after the last dose for a total of 18.5 days of antibiotic exposure where COVID-19 recovered individuals $R_{az}$ treated with azithromycin retain azithromycin in their system for an additional 11.5 days $\frac{1}{r_{az}}$ after COVID-19 recovery. Individuals treated with antibiotics are unable to acquire the sensitive strain. Antibiotics are assumed to clear colonization with sensitive strains at a rate $\omega$ while having no direct impact on colonization with resistant strains. This bacterial colonization process results in antibiotic selection for resistance via competition for limited hosts, facilitates epidemiological coexistence between strains and is adapted from previous models of S. pneumoniae (Colijn et al., 2010; Lipsitch et al., 2009; Mulberry et al., 2020). For a full list of parameter values see Appendix 2—table 2.

### Simulation in an early COVID-19 pandemic context

ODEs were integrated numerically using the R package deSolve to simulate and quantify epidemiological dynamics (Soetaert et al., 2010). First, bacterial dynamics were simulated until endemic equilibrium was achieved, under the assumption that S. pneumoniae was at endemic equilibrium upon the emergence of COVID-19. Second, using equilibrium states as initial conditions and re-initializing simulation time to t=0, a single SARS-CoV-2 infected individual was introduced into the population and ODEs were again integrated numerically to t=365 days. Parameter values used for simulation were taken from prior studies prioritizing French data and are provided in Appendix 2—table 2.

These simulations were conducted in the context of an ‘early pandemic scenario’ coinciding with the implementation of population-wide NPIs to slow SARS-CoV-2 transmission. This was conceived as the implementation of two 60 day lockdown periods starting on day 75 and on day 305 in response to the simulated surge in COVID-19 cases. Lockdowns were assumed to have three major potential impacts on population behavior and, in turn, the transmission dynamics of SARS-CoV-2 and S. pneumoniae. These impacts were incorporated into simulations by modifying epidemiological parameters in the model coincident with lockdowns. Three such modifications were considered and switched on and off, considering all possible combinations. First, lockdown led to reduced SARS-CoV-2 transmissibility by a factor $\theta_{c}$ . Second, lockdown led to a population-wide change in antibiotic initiation rate by a factor a (representing modified healthcare-seeking behavior leading to a reduction in the number of antibiotic prescriptions). Finally, lockdowns changed the pneumococcal disease risk by a factor $IPD_{risk}$ (representing a reduced risk of developing an IPD due to the absence of other respiratory viruses).

#### Effect of SARS-CoV-2 basic reproduction number (R0) on AMR

Impacts of SARS-CoV-2 on antibiotic-resistant IPD incidence may also depend on the characteristics of locally circulating SARS-CoV-2 R0. To account for potential impacts of SARS-CoV-2 transmissibility and azithromycin use in the community, in simulations we varied (i) values of R0 (basic reproduction number) for SARS-CoV-2 in France ($2\leqR_{0}\leq4$) and (ii) the proportion of the COVID-19 infected individuals using azithromycin at simulation outset (from 0% to 20%).

#### Effect of within-host interactions on AMR

SARS-CoV-2 infection may impact progression from bacterial colonization to IBD at the within-host level. To incorporate this mechanism in our model, we included a within-host interaction term in scenario S19: the ecological interaction term $(ψ_{c})$ increases the rate of progression to invasive disease among colonized individuals who are also infected with SARS-CoV-2. The equations for calculating daily IPD incidence assuming within-host interactions due to SARS-CoV-2 co-infection with accompanying details can be found in Appendix 2.
