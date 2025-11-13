# Reconstruction of transmission chains of SARS-CoV-2 amidst multiple outbreaks in a geriatric acute-care hospital: a combined retrospective epidemiological and genomic study

## Authors

- Mohamed Abbas<sup>1</sup> ([ORCID: 0000-0002-7265-1887](https://orcid.org/0000-0002-7265-1887)) †
- Anne Cori<sup>2</sup>
- Samuel Cordey<sup>3</sup> ([ORCID: 0000-0002-2684-5680](https://orcid.org/0000-0002-2684-5680))
- Florian Laubscher<sup>5</sup>
- Tomás Robalo Nunes<sup>1</sup>
- Ashleigh Myall<sup>7</sup>
- Julien Salamun<sup>9</sup>
- Philippe Huber<sup>10</sup>
- Dina Zekry<sup>10</sup>
- Virginie Prendki<sup>10</sup>
- Anne Iten<sup>1</sup>
- Laure Vieux<sup>12</sup>
- Valérie Sauvan<sup>1</sup>
- Christophe E Graf<sup>10</sup>
- Stephan Harbarth<sup>1</sup>

### Affiliations

1. Infection Control Programme & WHO Collaborating Centre on Patient Safety, Geneva University Hospitals Geneva Switzerland ([ROR:01swzsf04](https://ror.org/01swzsf04))
2. MRC Centre for Global Infectious Disease Analysis, Imperial College London London United Kingdom ([ROR:041kmwe10](https://ror.org/041kmwe10))
3. Faculty of Medicine, University of Geneva Geneva Switzerland ([ROR:01swzsf04](https://ror.org/01swzsf04))
4. Abdul Latif Jameel Institute for Disease and Emergency Analytics (J-IDEA), School of Public Health, Imperial College London London United Kingdom ([ROR:041kmwe10](https://ror.org/041kmwe10))
5. Laboratory of Virology, Department of Diagnostics, Geneva University Hospitals Geneva Switzerland ([ROR:01swzsf04](https://ror.org/01swzsf04))
6. Serviço de Infecciologia, Hospital Garcia de Orta, EPE Almada Portugal ([ROR:04jq4p608](https://ror.org/04jq4p608))
7. Department of Infectious Diseases, Imperial College London London United Kingdom ([ROR:041kmwe10](https://ror.org/041kmwe10))
8. Department of Mathematics, Imperial College London London United Kingdom ([ROR:041kmwe10](https://ror.org/041kmwe10))
9. Department of Primary Care, Geneva University Hospitals Geneva Switzerland ([ROR:01swzsf04](https://ror.org/01swzsf04))
10. Department of Rehabilitation and Geriatrics, Geneva University Hospitals Geneva Switzerland ([ROR:01swzsf04](https://ror.org/01swzsf04))
11. Division of Infectious Diseases, Geneva University Hospitals Geneva Switzerland ([ROR:01swzsf04](https://ror.org/01swzsf04))
12. Occupational Health Service, Geneva University Hospitals Geneva Switzerland ([ROR:01swzsf04](https://ror.org/01swzsf04))

† Corresponding author

## Abstract

Background:There is ongoing uncertainty regarding transmission chains and the respective roles of healthcare workers (HCWs) and elderly patients in nosocomial outbreaks of severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) in geriatric settings.Methods:We performed a retrospective cohort study including patients with nosocomial coronavirus disease 2019 (COVID-19) in four outbreak-affected wards, and all SARS-CoV-2 RT-PCR positive HCWs from a Swiss university-affiliated geriatric acute-care hospital that admitted both Covid-19 and non-Covid-19 patients during the first pandemic wave in Spring 2020. We combined epidemiological and genetic sequencing data using a Bayesian modelling framework, and reconstructed transmission dynamics of SARS-CoV-2 involving patients and HCWs, to determine who infected whom. We evaluated general transmission patterns according to case type (HCWs working in dedicated Covid-19 cohorting wards: HCWcovid; HCWs working in non-Covid-19 wards where outbreaks occurred: HCWoutbreak; patients with nosocomial Covid-19: patientnoso) by deriving the proportion of infections attributed to each case type across all posterior trees and comparing them to random expectations.Results:During the study period (1 March to 7 May 2020), we included 180 SARS-CoV-2 positive cases: 127 HCWs (91 HCWcovid, 36 HCWoutbreak) and 53 patients. The attack rates ranged from 10% to 19% for patients, and 21% for HCWs. We estimated that 16 importation events occurred with high confidence (4 patients, 12 HCWs) that jointly led to up to 41 secondary cases; in six additional cases (5 HCWs, 1 patient), importation was possible with a posterior probability between 10% and 50%. Most patient-to-patient transmission events involved patients having shared a ward (95.2%, 95% credible interval [CrI] 84.2%–100%), in contrast to those having shared a room (19.7%, 95% CrI 6.7%–33.3%). Transmission events tended to cluster by case type: patientnoso were almost twice as likely to be infected by other patientnoso than expected (observed:expected ratio 2.16, 95% CrI 1.17–4.20, p=0.006); similarly, HCWoutbreak were more than twice as likely to be infected by other HCWoutbreak than expected (2.72, 95% CrI 0.87–9.00, p=0.06). The proportion of infectors being HCWcovid was as expected as random. We found a trend towards a greater proportion of high transmitters (≥2 secondary cases) among HCWoutbreak than patientnoso in the late phases (28.6% vs. 11.8%) of the outbreak, although this was not statistically significant.Conclusions:Most importation events were linked to HCW. Unexpectedly, transmission between HCWcovid was more limited than transmission between patients and HCWoutbreak. This finding highlights gaps in infection control and suggests the possible areas of improvements to limit the extent of nosocomial transmission.Funding:This study was supported by a grant from the Swiss National Science Foundation under the NRP78 funding scheme (Grant no. 4078P0_198363).

## Introduction

Nosocomial acquisition of severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) in geriatric institutions and long-term care facilities (LTCFs) may account for large proportions of all declared coronavirus disease 2019 (Covid-19) cases in many countries, and contribute substantially to morbidity and mortality (Thiabaud et al., 2021; Bhattacharya et al., 2021; The Guardian, 2021b; The Guardian, 2021a). Because the reservoir of SARS-CoV-2 in healthcare environments may contribute to amplifying the pandemic (Knight et al., 2022), we need to better understand transmission dynamics in these settings.

The terms healthcare-associated, hospital-onset, and nosocomial Covid-19 reflect the uncertainty around defining and distinguishing community- versus healthcare-acquired Covid-19 cases (Abbas et al., 2021c). Nevertheless, in some settings, such as LTCFs and nursing homes, these definitions are relatively straightforward. In other settings, such as those with a high patient turnover, or where patients are admitted from the community and both Covid-19 and non-Covid-19 cases are hospitalised in the same institution, defining, and more importantly detecting cases is crucial to avoid cross-contamination. Determining sources and transmission pathways of infection may thus help improve infection prevention and control (IPC) strategies.

The role of healthcare workers (HCWs) in nosocomial Covid-19 transmission dynamics is complex, as they can be victims and/or vectors of SARS-CoV-2 infection, and can acquire from or transmit to their peers and patients and the community (Abbas et al., 2021b; Ellingford et al., 2021). There is ongoing controversy and uncertainty surrounding the role of HCWs in infecting patients during nosocomial outbreaks, and findings from acute-care hospitals cannot be applied directly to LTCFs and geriatric hospitals (Abbas et al., 2021a; Klompas et al., 2021; Lucey et al., 2021; Aggarwal et al., 2022).

The aim of this study was to reconstruct transmission dynamics in several nosocomial outbreaks of SARS-CoV-2 involving patients and HCWs in a Swiss university-affiliated geriatric hospital that admitted both Covid-19 and non-Covid-19 patients during the first pandemic wave in Spring 2020.

## Methods

We performed a retrospective cohort study of all patients with nosocomial Covid-19 in four outbreak-affected wards, and all SARS-CoV-2 RT-PCR positive HCWs from 1 March to 7 May 2020. This study is reported according to the STROBE (von Elm et al., 2007) (Strengthening the Reporting of Observational Studies in Epidemiology) and ORION (Stone et al., 2007) (Outbreak Reports and Intervention studies Of Nosocomial infection) statements.

### Setting

The Hospital of Geriatrics, part of the Geneva University Hospitals (HUG) consortium, has 196 acute-care and 100 rehabilitation beds. During the first pandemic wave, a maximum of 176 acute-care beds were dedicated to admitting geriatric patients with Covid-19 who were not eligible for escalation of therapy (e.g., intensive care unit admission) (Mendes et al., 2020). During the same period, patients were also admitted for non-Covid-19 hospitalisations, and the rehabilitation beds were also open to patients convalescing from Covid-19. Beginning on 1 April 2020, we use RT-PCR to screen all patients on admission for SARS-CoV-2. Between 7 April 2020 and 30 May 2020, we screened patients in non-Covid wards. We encouraged HCWs from outbreak wards to undergo PCR testing on nasopharyngeal swabs between 9 and 16 April 2020, even if they were asymptomatic. We described additional IPC measures in Appendix 1.

### Definitions

We defined healthcare-associated (HA) Covid-19 by an onset of symptoms ≥5 days after admission in conjunction with a strong suspicion of healthcare transmission, in accordance with Swissnoso guidelines (Swissnoso, 2021). We classified patients with HA-Covid-19 as ‘patientnoso’, the others were assumed to be community-acquired or ‘patientcommunity’. An outbreak was declared when ≥3 cases of HA-Covid-19 (HCWs and patients) with a possible temporal-spatial link were identified (Swissnoso, 2021). HCWs were included in the outbreak investigation if they had a positive RT-PCR for SARS-CoV-2. We classified HCWs as ‘HCWcovid’ if they worked in a Covid-19 cohorting ward admitting community-acquired cases, or ‘HCWoutbreak’ if they worked in a ‘non-Covid’ ward (i.e., not admitting community-acquired Covid-19 cases) in which nosocomial outbreaks occurred. HCWs worked in either one or another type of ward, except for one HCW who worked in both Covid and non-Covid wards (although the proportion and/or days worked in each type of ward is unknown). Six HCWs worked across multiple wards (e.g., on-call) and were attributed to Covid-wards for the analyses.

### Data sources

The data used for this study were from the sources described previously (Abbas et al., 2021a). First, we used prospectively collected data from the Swiss Federal Office of Public Health-mandated surveillance of hospitalised Covid-19 patients (Thiabaud et al., 2021). We also used prospectively collected data from HUG’s Department of Occupational Health for symptom-onset data and the Department of Human Resources (HR) for HCW shifts. Dates of symptom onset were available for both patients and HCWs from each source, respectively.

### Descriptive epidemiology

We produced an epidemic curve using dates of symptom onset; where these were unavailable (e.g., asymptomatic cases), we imputed them with the median difference between date of symptom onset and date of nasopharyngeal swab.

### Microbiological methods

All Covid-19 cases in the outbreak were confirmed by RT-PCR on nasopharyngeal swabs. We performed SARS-CoV-2 whole-genome sequencing (WGS) using an amplicon-based sequencing method to produce RNA sequences, as previously described (Abbas et al., 2021a) and summarised in Appendix 1.

### Phylogenetic analysis

We performed sequence alignment with MUSCLE (v3.8.31). We employed MEGA X (Kumar et al., 2018) using the Maximum Likelihood method and Tamura three-parameter model (Tamura, 1992) to conduct the evolutionary analyses. We integrated to the phylogenetic analysis all the complete genomes SARS-CoV-2 sequenced by the Laboratory of Virology (HUG) for the purposes of epidemiological surveillance in the community.

### Statistical analysis

We performed descriptive statistics with medians and interquartile ranges (IQRs), and counts and proportions, as appropriate.

### Reconstruction of transmission trees

We combined epidemiological and genomic data to reconstruct who infected whom using the R package outbreaker2 (Jombart et al., 2014; Campbell et al., 2018), as described elsewhere (Abbas et al., 2021a) and in Appendix 1. Briefly, the model uses a Bayesian framework, combining information on the generation time (time between infections in an infector/infectee pair), and contact patterns, with a model of sequence evolution to probabilistically reconstruct the transmission tree (see Appendix 1).

Because formal contact tracing was limited during the study period, we constructed contact networks based on ward or room presence for patients based on their ward movements, and on HCW shifts obtained from HR. We defined a contact as simultaneous presence on the same ward on a given day (see Appendix 1). The manner by which outbreaker2 handles these contacts is conservative in that it allows for non-infectious contacts to occur (false positives) and incomplete reporting of infectious contacts (false negatives). In addition, the model estimates the proportions of these contacts.

Using the reconstructed transmission trees, we determined the number of imported cases (with minimal posterior support of 10%), and the number of secondary cases generated by the imports. Imported caseswere defined as those that do not have apparent ancestors among the cases included in the outbreak. We also calculated the number of secondary (i.e., onward) infections for each case, that is, the individual reproductive number (R), which we stratified by epidemic phase (early or late with a cut-off on 9 April 2020) and case type (HCWcovid, HCWoutbreak, patientnoso, and patientcommunity, see Appendix 1).

We assessed the role of each case type in transmission by estimating the proportion of infections attributed to the case type (fcase), which we compared with the random expectation considering the prevalence of each case type (see Appendix 1). To better understand the transmission pathways between and within wards, we also estimated (for outbreak and non-outbreak wards), the proportion of infections attributed to infectors in the same ward. We also constructed a matrix representing ward-to-ward transmission. Patient movements between wards were constructed using the implementation of the vistime package (visualisation tool) as in the publication by Meredith et al., 2020. Statistical analyses were performed in R software version 4.0.3 (https://www.R-project.org/).

## Results

During the study period, we included a total of 180 SARS-CoV-2 positive cases: 127 HCWs of whom 91 HCWcovid, and 36 HCWoutbreak, and 53 patients from the four outbreak wards. Of the 53 included patients, post hoc epidemiological analysis showed that 4 of these likely acquired Covid-19 in the community (CA-Covid-19). The remaining 49 nosocomial cases represented 20.2% (49/242) of all patients hospitalised with Covid-19, and 81.7% (49/60) of nosocomial Covid-19 cases in the Geriatric Hospital. The ward-level attack rates ranged from 10% to 19% among patients. Moreover, 21% of all HCWs in the geriatric hospital had a PCR-positive test. The epidemic curve is shown in Figure 1, and ward-level epidemic curves in Figure 1—figure supplement 1. Characteristics of patients and HCWs are summarised in Tables 1 and 2, respectively. Strikingly, the time period between date of onset of symptoms and date of swab was shorter for HCWcovid (mean 1.6 days, SD 1.78) than for HCWoutbreak (mean 2.88 days, SD 4.84).

![Figure 1.](https://cdn.elifesciences.org/articles/76854/elife-76854-fig1-v2.jpg)

**Figure 1.:** Includes eight asymptomatic cases for whom date of onset was inferred (c.f., text). HCW, healthcare worker.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/76854/elife-76854-fig1-figsupp1-v2.jpg)

**Table 1.**
 Characteristics of Covid-19 patients with nosocomial acquisition.


<table>
  <thead>
    <tr>
      <th>Characteristics</th>
      <th>All patients(N=49)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Female, n (%)</td>
      <td>28 (57.1)</td>
    </tr>
    <tr>
      <td>Age, median (IQR)</td>
      <td>85.4 (83.5–89.3)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Asymptomatic, n (%)</td>
      <td>3 (6.1)</td>
    </tr>
    <tr>
      <td>Onset of symptoms before swab date, n (%)</td>
      <td>12 (24.5)</td>
    </tr>
    <tr>
      <td>Days from onset of symptoms to swab, median (IQR)</td>
      <td>0 (0–0)</td>
    </tr>
    <tr>
      <td>Days from onset of symptoms to swab, mean (SD)</td>
      <td>–0.29 (2.19)</td>
    </tr>
  </tbody>
</table>

**Table 2.**
 Characteristics of SARS-CoV-2 RT-PCR positive healthcare workers.


<table>
  <thead>
    <tr>
      <th>Characteristics</th>
      <th>All HCWs(N=127)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Female, n (%)</td>
      <td>92 (72.4)</td>
    </tr>
    <tr>
      <td>Age, median (IQR)</td>
      <td>32.0 (43.3–54.8)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Profession, n (%)</td>
      <td></td>
    </tr>
    <tr>
      <td>Nurse</td>
      <td>57 (44.9)</td>
    </tr>
    <tr>
      <td>Nurse assistant</td>
      <td>39 (30.7)</td>
    </tr>
    <tr>
      <td>Doctor</td>
      <td>19 (15.0)</td>
    </tr>
    <tr>
      <td>Care assistant</td>
      <td>4 (3.2)</td>
    </tr>
    <tr>
      <td>Transporter</td>
      <td>4 (3.2)</td>
    </tr>
    <tr>
      <td>Physical therapist</td>
      <td>2 (1.6)</td>
    </tr>
    <tr>
      <td>Speech therapist</td>
      <td>1 (0.8)</td>
    </tr>
    <tr>
      <td>Medical student</td>
      <td>1 (0.8)</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Asymptomatic, n (%) missing data for 5</td>
      <td>5 (3.9)</td>
    </tr>
    <tr>
      <td>Days from onset of symptoms to swab, median (IQR)</td>
      <td>1 (−2 to 21)</td>
    </tr>
    <tr>
      <td>HCWs in Covid-19 wards (HCWcovid)</td>
      <td>1 (1–2)</td>
    </tr>
    <tr>
      <td>HCWs in non-Covid (outbreak) wards (HCWoutbreak)</td>
      <td>1 (0–3)</td>
    </tr>
    <tr>
      <td>Days from onset of symptoms to swab, mean (SD)</td>
      <td>1.91 (2.86)</td>
    </tr>
    <tr>
      <td>HCWs in Covid-19 wards (HCWcovid)</td>
      <td>1.60 (1.78)</td>
    </tr>
    <tr>
      <td>HCWs in non-Covid (outbreak) wards (HCWoutbreak)</td>
      <td>2.88 (4.84)</td>
    </tr>
  </tbody>
</table>

### Phylogenetic tree

We obtained SARS-CoV-2 sequences for 148 isolates of the 180 cases (82.2%), including 105 HCWs (82.7%) and 43 patients (81.1%). A rooted phylogenetic tree found substantial genetic diversity, with at least nine clusters and sub-clusters (Figure 2). One cluster (with moderate bootstrap support [BS] 26%) comprised sequences from 17 HCWs, 3 patients, and 6 community isolates in multiple subclusters (e.g., BS 72% with signature mutation C5239T). Another cluster (BS 78% with signature mutations C28854T and A20268G) showed a HCW sequence (H1048) with high similarity with community isolates. There was also a large cluster (BS 68% with signature mutations C8293T, T18488C, and T24739C) with several subclusters includes 19 HCWs, 9 patients, and 3 community cases; ward movements for the patients are shown in Appendix 1—figure 1. A well-defined cluster (BS 100%) included isolates from patients and HCWs from the same ward.

![Figure 2.](https://cdn.elifesciences.org/articles/76854/elife-76854-fig2-v2.jpg)

**Figure 2.:** The tree includes 148 sequences related to the outbreak (patient and employee sequences are named C1xx [blue] and H10xx [red], respectively), alongside the community cases in the canton of Geneva, Switzerland, that were sequenced in March–April 2020 by the Laboratory of Virology (Geneva University Hospitals) and submitted to GISAID (virus names and accession ID [i.e., EPI_ISL_] are indicated) in the context of an epidemiological surveillance. For each sequence the date of the sample collection is mentioned (yyyy-mm-dd).

### Imported cases

From the reconstructed trees, we identified 22 imports in total (17 HCWs, 5 patients) with posterior support ≥10%. The 22 imported cases generated 41 secondary cases (posterior support ≥10%), with a median posterior support of 32.4% (IQR 17.0%–53.7%). When restricting to imports with ≥50% posterior support, there were 16 imported cases 16 (12 HCWs, 4 patients), generating 35 secondary cases. There was some degree of uncertainty, reflected by circular transmission pathways, in determination of imported cases and their secondary cases. There were six transmission pairs (C114-C115, C153-H1057, H1008-H1059, H1011-H1019, H1017-H12021, and H1052-H1082) where there was uncertainty as to which of the cases was imported and which was a secondary case, that is, for each case in the pair there was a ≥10% probability of importation, but also ≥10% probability of being a secondary case of an imported case. Therefore, in total, 29 cases were ‘pure’ secondary cases of imported cases (Table 3).

**Table 3.**
 Imported cases and secondary infections, patients and HCWs are named C1xx and H10xx, respectively.


<table>
  <thead>
    <tr>
      <th>Imported case</th>
      <th>Posterior probability of importation</th>
      <th>Secondary onward transmission by imported case</th>
      <th>Posterior probability of onward transmission</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>C107</td>
      <td>100</td>
      <td>H1077C131C124H1005C125H1034H1068C112C116</td>
      <td>10072.539.435.032.927.318.515.911.7</td>
    </tr>
    <tr>
      <td>C114*</td>
      <td>42.5</td>
      <td>C115*</td>
      <td>42.5</td>
    </tr>
    <tr>
      <td>C115*</td>
      <td>57.5</td>
      <td>C114*</td>
      <td>57.5</td>
    </tr>
    <tr>
      <td>C123</td>
      <td>96.4</td>
      <td>H1058H1036H1047</td>
      <td>90.116.011.1</td>
    </tr>
    <tr>
      <td>C153*</td>
      <td>51.7</td>
      <td>H1057*</td>
      <td>51.6</td>
    </tr>
    <tr>
      <td>H1008*</td>
      <td>85.7</td>
      <td>H1059*</td>
      <td>85.7</td>
    </tr>
    <tr>
      <td>H1011*</td>
      <td>65.9</td>
      <td>H1019*</td>
      <td>61.7</td>
    </tr>
    <tr>
      <td>H1012</td>
      <td>100</td>
      <td>N/A</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>H1013</td>
      <td>100</td>
      <td>N/A</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>H1015</td>
      <td>100</td>
      <td>N/A</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>H1017*</td>
      <td>52.3</td>
      <td>H1020H1021*</td>
      <td>100.052.3</td>
    </tr>
    <tr>
      <td>H1019*</td>
      <td>34.1</td>
      <td>H1011*</td>
      <td>28.2</td>
    </tr>
    <tr>
      <td>H1021*</td>
      <td>47.7</td>
      <td>H1017*</td>
      <td>47.7</td>
    </tr>
    <tr>
      <td>H1025</td>
      <td>86.6</td>
      <td>H1085H1031</td>
      <td>95.741.5</td>
    </tr>
    <tr>
      <td>H1048</td>
      <td>100</td>
      <td>N/A</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>H1052*</td>
      <td>18.9</td>
      <td>H1082*</td>
      <td>18.9</td>
    </tr>
    <tr>
      <td>H1057*</td>
      <td>48.3</td>
      <td>C153*</td>
      <td>48.3</td>
    </tr>
    <tr>
      <td>H1059*</td>
      <td>14.3</td>
      <td>H1008*</td>
      <td>14.3</td>
    </tr>
    <tr>
      <td>H1073</td>
      <td>100</td>
      <td>N/A</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>H1082*</td>
      <td>81.1</td>
      <td>H1052*</td>
      <td>81.1</td>
    </tr>
    <tr>
      <td>H1110</td>
      <td>85.1</td>
      <td>H1063H1064H1041H1024H1091H1065</td>
      <td>58.032.430.022.522.117.2</td>
    </tr>
    <tr>
      <td>H1122</td>
      <td>84.5</td>
      <td>C113C104H1033H1003H1004H1044</td>
      <td>53.726.017.015.515.010.6</td>
    </tr>
  </tbody>
</table>

_N/A: not applicable.*Uncertainty in transmission (i.e., case could either be an imported case or a secondary case)._

### Reconstructing who infected whom

Figure 3 shows the distribution of posterior support when considering the ancestry from the individual (i.e., Cxxx or Hxxx), case type (HCWcovid, HCWoutbreak, patientnoso, and patientcommunity), ward, or ward type (outbreak or non-outbreak wards). There was less confidence in attribution of ancestry when considering by individual or ward, when compared with case type or ward type. The output from the ancestry reconstruction is shown in Figure 3—figure supplement 1 and Figure 3—figure supplement 1—source code 1. The model estimated that the reporting probability was 91.2% (95% credible interval [CrI] 86.6%–95.2%), suggesting that only 8.8% of source cases involved in transmission were not identified. For most (90.8%) cases, the model identified the direct infector, without intermediate unobserved cases (Figure 3—figure supplement 2).

![Figure 3.](https://cdn.elifesciences.org/articles/76854/elife-76854-fig3-v2.jpg)

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/76854/elife-76854-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Infectors are on the vertical axis and infectees are on the horizontal axis. Each bubble represents the posterior probability of each infector-infectee transmission pair. The bottom row denotes the probability that an infectee was in fact an imported case. Patients and employees are named C1xx and H10xx, respectively.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/76854/elife-76854-fig3-figsupp2-v2.jpg)

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/76854/elife-76854-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** Each case is on the horizontal axis. The shading corresponds to a value indicating the magnitude of the difference in attribution of the case’s ancestor and the main analysis. For each infectee (case), we calculated the absolute difference in probabilities of infectors (ancestor) between the main analysis and each sensitivity analysis. Values of difference 1 indicate 100% difference in ancestry attribution, and 0 indicate absolute agreement. Sensitivity analysis #1: absence of contact data. Sensitivity analysis #2: longer serial interval (mean 5.2 days, SD 4.7).Sensitivity analysis #3: contacts were based on human resources data for HCWs and on infectious and susceptible periods. Sensitivity analysis #4: patients are considered to be no longer infectious after the date of the positive RT-PCR for SARS-CoV-2. Sensitivity analysis #5: higher value (3) for the threshold for identification of outliers. Sensitivity analysis #6: default value (5) for the threshold for identification of outliers. HCW, healthcare worker.

### Ward attribution

The epidemiological attribution of the presumptive ward on which patients became infected and that suggested by the model output (see Appendix 1) agree for 95% of the nosocomial cases. The modelling analysis modified the ward attribution for three patients.

### Transmission patterns

Among patient-to-patient transmission events, and across all posterior trees, 95.2% (95% CrI 84.2%–100%) involved patients who shared a ward during their hospital stay. In contrast, only 19.7% (95% CrI 6.7%–33.3%) of patient-to-patient transmissions involved patients who had shared a room. The model predicted that C107 infected C131 with a 72.5% probability although they did not share a ward (Appendix 1—figure 1B for ward movements); the probabilities that this was a direct infection and indirect infection with an unreported intermediate infector were 38.3% and 34.2%, respectively (Appendix 1—figure 1B for ward movements).

### Secondary infections

The number of secondary infections caused by each infected case (individual reproductive number R, estimated from the transmission tree reconstruction), ranged from 0 to 9 (Figure 4). We compared the proportion of cases with no secondary transmissions (non-transmitters) and of cases with ≥2 secondary transmissions (high transmitters) across case types and outbreak phase. We found that the proportion of non-transmitters among both HCWoutbreak and patientnoso was smaller in the early than in the late stage (approximately 32% in early and 55% in late phase for both groups), suggesting that the contribution of these groups to ongoing transmission decreased over the study period. Conversely, the proportion of non-transmitters among HCWcovid was stable at about 55%–60% across the early and the late phase. The proportions of high transmitters were higher among HCWoutbreak than either patientnoso or HCWcovid in the late phases (28.6% vs. 11.8% and 13.9%) of the outbreak. However, due to small numbers, these differences were not statistically significant. These trends were similar in the sensitivity analyses (Appendix 1—table 2).

![Figure 4.](https://cdn.elifesciences.org/articles/76854/elife-76854-fig4-v2.jpg)

**Figure 4.:** Number of cases in early phase: HCWoutbreak 19, HCWcovid 43, patientnoso 25, patientcommunity 1. Number of cases in late phase: HCWoutbreak 7, HCWcovid 36, patientnoso 17, patientcommunity 0. HCW, healthcare worker.

### Role of HCWs and patients in transmission events

We found that cases were significantly less likely than expected at random to be infected by HCWs from COVID wards (proportion infected by HCWcovid, fHCW=42%; 95% CrI 36%–49% vs. 53% expected at random; 95% CrI 44%–62%; p=0.042). This was true across all cases, but particularly among HCWs in outbreak wards (fHCW=31%, 95% CrI 17%–48%; p=0.07) and patients (fHCW=24%, 95% CrI 12%–37%, p=0.006). Conversely HCWoutbreak were significantly more likely than expected at random to become infected by other HCWoutbreak (proportion infected by HCWoutbreak, foutbreak = 38%, 95% CrI 22%–52% v. 18%; 95% CrI 4%–35%, p=0.03). Patients with nosocomial Covid-19 (patientnoso) were significantly more likely than expected at random to be infected by other patientnoso (proportion infected by patientnoso, fpat=56%, 95% CrI 41%–71% vs. 28%; 95% CrI 14%–45%, p=0.005). Full results are shown in Figure 5.

![Figure 5.](https://cdn.elifesciences.org/articles/76854/elife-76854-fig5-v2.jpg)

**Figure 5.:** The blue histograms indicate the expected random distributions of fcase, given the prevalence of each case type. The red histograms show the observed distribution of fcase, across 1000 transmission trees reconstructed by outbreaker2. (A) All cases. (B) Transmission to HCWs in Covid-19 wards only. (C) Transmission to HCWs in non-Covid-19 wards (i.e., outbreak wards) only. (D) Transmission to patients with nosocomial Covid-19 only. HCW, healthcare worker.

### Role of within-ward and between-ward transmission

Infected staff or patients in outbreak wards were responsible for significantly more transmission in general (54%; 95% CrI 48%–61%) than expected (43.7%, 95% CrI 35%–53%). This was driven in particular by transmission from staff or patients to other staff or patients in outbreak wards (73%, 95% CrI 63%–82%) (Figure 5). Within-ward transmission was more pronounced in outbreak wards (mean 48%; range: 20%–70% of all infections within a ward) than in non-outbreak wards (mean 14%; range 0%–63%) as shown in Appendix 1—figures 2 and 3.

## Discussion

This in-depth investigation of SARS-CoV-2 transmission between patients and HCWs in a geriatric hospital, including several nosocomial outbreaks, has provided many valuable insights on transmission dynamics. First, we showed that the combination of epidemiological and genetic data using sophisticated modelling enabled us to tease out overall transmission patterns. Second, we showed that transmission dynamics among HCWs differed according to whether they worked in Covid wards or in wards where outbreaks occurred. We found that HCW-to-HCW transmission in Covid wards was not higher than expected but the risk of transmission between HCWs in non-Covid wards was twofold higher than expected. Third, we identified excess patient-to-patient transmission events, most of which occurred within the same ward, but not necessarily the same room. Fourth, we identified multiple importation events that led to a substantial number of secondary cases or clusters; most were related to HCWs, but one was related to a patient with community-acquired Covid-19.

These results are particularly important, as settings which care for elderly patients, such as geriatrics and rehabilitation clinics or LTCFs have high attack rates of SARS-CoV-2 for both patients and HCWs (Abbas et al., 2021b). In an institution-wide seroprevalence study in our hospital consortium, the Department of Rehabilitation and Geriatrics, of which the hospital in this study was part, had the highest proportion of HCWs with anti-SARS-CoV-2 antibodies (Martischang et al., 2022).

The different transmission patterns between HCWs in Covid wards and outbreak wards (i.e., meant to be ‘Covid-free’) is intriguing. HCWs' behaviour may have affected transmission. Indeed, a previous study Ottolenghi et al., 2021 found that HCWs caring for Covid-19 patients were concerned about becoming infected while caring for patients, and therefore may apply IPC measures more rigorously than when caring for patients who do not have Covid-19. HCWs working in non-Covid wards may not have felt threatened by Covid-19 patients who were in principle allocated to other wards, and thus not in their direct care. HCWs in non-Covid wards also may have underestimated the transmission risk from their peers to a greater extent than those working in Covid wards, and thus may not have maintained physical distancing well. In addition, we found a higher mean duration (2.9 days) of presenteeism despite symptoms compatible with Covid-19 among HCWs working in non-Covid wards than for those working in Covid wards (1.6 days), which gives credence to the abovementioned possible explanations for the different transmission patterns. Other factors (e.g., work culture, baseline IPC practices) also may have affected transmission patterns.

Most patient-to-patient transmission events involved patients who were hospitalised in the same ward, and were therefore in close proximity. We cannot exclude transmission from a ‘point-source’ or via a HCW’s contaminated hands (i.e., an unidentified HCW who transmitted SARS-CoV-2 to multiple patients in the same ward). To date, we have little evidence to suggest that this is the case; indeed, the transmission patterns were robust to changes in the model assumptions. Mathematical models have suggested that single-room isolation of suspected cases could potentially reduce the incidence of nosocomial SARS-CoV-2 transmission by up to 35% (Evans et al., 2021). In the outbreaks we describe, symptomatic patients were identified promptly, with a median delay of 0 days between symptom onset and their first positive test. However, these precautions may not be sufficient as patients may transmit the virus when they are pre-symptomatic (Ferretti et al., 2020). Thus, infection prevention teams may need to identify patients at high risk of developing nosocomial Covid-19 (Myall et al., 2021) if single rooms are not available for all exposed patients (e.g., in cases of overcrowding). For example, a previous study Mo et al., 2021 found that exposure to community-acquired cases who were identified and segregated or cohorted was associated with half the risk of infection compared with exposure to hospital-acquired cases or HCWs who may be asymptomatic. One possible explanation for this finding is that patients with CA-Covid may have passed the peak of infectiousness when they are admitted, whereas patients with HA-Covid cases have frequent unprotected contact with HCWs and other patients during their period of peak infectiousness.

The current evidence does not support the use of real-time genomics for control of SARS-CoV-2 nosocomial outbreaks (Stirrup et al., 2021; Stirrup et al., 2022). Nevertheless, in this investigation, as in many others, we performed WGS to investigate transmission patterns (Aggarwal et al., 2022). Although we were able to gain considerable insight from the powerful combination of genetic sequencing data and rich epidemiological data, we controlled the outbreaks without using WGS, as was the case in many published reports (Arons et al., 2020; Taylor et al., 2020). Furthermore, WGS may be more useful for ruling out transmission rather than for confirmatory purposes, due to the low number of mutations accumulated in the SARS-CoV-2 genome between transmission pairs (Braun et al., 2021).

Our study has several strengths. To the best of our knowledge, it is the only extensive outbreak investigation that employed WGS and sophisticated modelling to assess SARS-CoV-2 transmission in a geriatric acute-care hospital. We performed WGS on isolates from a high proportion (80%) of cases, including those from HCWs which has been previously shown to improve understanding of transmission dynamics (Ellingford et al., 2021). In addition, we collected the data prospectively, thereby minimising the risk of bias.

Despite these strengths, some limitations must be acknowledged. First, we included only one sequence from a CA-Covid case. However the method we used to reconstruct who infected whom is able to cope with and identify missing intermediate cases, which allowed us to estimate that the overwhelming majority of cases (91.5%) was captured in our sample. Some misclassification may have occurred, for example, whether an imported cases is truly nosocomial or not. For example, the model predicted that patients C107 and C115 were imported cases. The predicted dates of infection were 14–22 March for case C107 and 8–24 March for case C115; their admission dates were 3 March and 18 March, respectively. The probability that infection occurred on or after date of admission for case C115 was 81%. So the fact that the cases are labelled as ‘imported’ does not preclude the fact that these were still nosocomial cases, simply that their infector was not identified in this outbreak. We did not collect data on adherence to Covid-specific IPC recommendations by HCWs in different wards. We were unable to relate the number of secondary infections with the population (ward) size; more complex models would be required to explain the underlying mechanisms in a context of fluctuating denominators, for example, due to ward closures, and so on. In addition, we performed these investigations during the first pandemic wave with a wild-type variant of SARS-CoV-2 in a susceptible population. For these reasons, the results may no longer be applicable in settings with high vaccination coverage and/or substantial natural immunity, or in later stages of the pandemic, also due to accrued experience in managing and preventing outbreaks. Nevertheless, the lessons learned may be useful in a large number of countries with slow vaccine roll-out due to vaccine hesitancy, particularly among HCWs where there is no vaccine mandate, or unequal access to vaccine supplies (The Lancet Infectious Diseases, 2021). Furthermore, nosocomial outbreaks of SARS-CoV-2 still occur despite high vaccination coverage (Burugorri-Pierre et al., 2021; Shitrit et al., 2021). Also, these valuable lessons may be applicable for nosocomial outbreak control in the case of future pandemics due to respiratory viruses with characteristics similar to SARS-CoV-2.

In conclusion, strategies to prevent nosocomial SARS-CoV-2 transmission in geriatric settings should take into account the potential for patient-to-patient transmission and the transmission dynamics between HCWs in non-Covid wards, which our study suggests may differ from those in dedicated Covid-19 wards.
