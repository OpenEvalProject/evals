# Rapid feedback on hospital onset SARS-CoV-2 infections combining epidemiological and sequencing data

## Authors

- Oliver Stirrup<sup>1</sup> ([ORCID: 0000-0002-8705-3281](https://orcid.org/0000-0002-8705-3281)) †
- Joseph Hughes<sup>2</sup>
- Matthew Parker<sup>3</sup>
- David G Partridge<sup>6</sup> ([ORCID: 0000-0002-0417-2016](https://orcid.org/0000-0002-0417-2016))
- James G Shepherd<sup>2</sup>
- James Blackstone<sup>8</sup>
- Francesc Coll<sup>9</sup>
- Alexander Keeley<sup>6</sup>
- Benjamin B Lindsey<sup>6</sup> ([ORCID: 0000-0003-4227-2592](https://orcid.org/0000-0003-4227-2592))
- Aleksandra Marek<sup>10</sup>
- Christine Peters<sup>10</sup>
- Joshua B Singer<sup>2</sup>
- Asif Tamuri<sup>11</sup>
- Thushan I de Silva<sup>6</sup>
- Emma C Thomson<sup>2</sup>
- Judith Breuer<sup>14</sup> ([ORCID: 0000-0001-8246-0534](https://orcid.org/0000-0001-8246-0534)) †

### Affiliations

1. Institute for Global Health, University College London London United Kingdom
2. MRC-University of Glasgow Centre for Virus Research Glasgow United Kingdom
3. Sheffield Bioinformatics Core, The University of Sheffield Sheffield United Kingdom
4. Sheffield Institute for Translational Neuroscience, The University of Sheffield Sheffield United Kingdom
5. Sheffield Biomedical Research Centre, The University of Sheffield Sheffield United Kingdom
6. Sheffield Teaching Hospitals NHS Foundation Trust Sheffield United Kingdom
7. The Florey Institute for Host-Pathogen Interactions & Department of Infection, Immunity and Cardiovascular Disease, Medical School, University of Sheffield Sheffield United Kingdom
8. The Comprehensive Clinical Trials Unit at UCL , University College London London United Kingdom
9. Department of Infection Biology, Faculty of Infectious and Tropical Diseases, London School of Hygiene & Tropical Medicine London United Kingdom
10. Clinical Microbiology, NHS Greater Glasgow and Clyde Glasgow United Kingdom
11. Research Computing, University College London London United Kingdom
12. Institute of Infection, Immunity and Inflammation, College of Medical, Veterinary and Life Sciences, University of Glasgow Glasgow United Kingdom
13. Department of Infectious Diseases, Queen Elizabeth University Hospital Glasgow United Kingdom
14. Division of Infection and Immunity, University College London London United Kingdom

† Corresponding author

## Abstract

Rapid identification and investigation of healthcare-associated infections (HCAIs) is important for suppression of SARS-CoV-2, but the infection source for hospital onset COVID-19 infections (HOCIs) cannot always be readily identified based only on epidemiological data. Viral sequencing data provides additional information regarding potential transmission clusters, but the low mutation rate of SARS-CoV-2 can make interpretation using standard phylogenetic methods difficult. We developed a novel statistical method and sequence reporting tool (SRT) that combines epidemiological and sequence data in order to provide a rapid assessment of the probability of HCAI among HOCI cases (defined as first positive test >48 hr following admission) and to identify infections that could plausibly constitute outbreak events. The method is designed for prospective use, but was validated using retrospective datasets from hospitals in Glasgow and Sheffield collected February–May 2020. We analysed data from 326 HOCIs. Among HOCIs with time from admission ≥8 days, the SRT algorithm identified close sequence matches from the same ward for 160/244 (65.6%) and in the remainder 68/84 (81.0%) had at least one similar sequence elsewhere in the hospital, resulting in high estimated probabilities of within-ward and within-hospital transmission. For HOCIs with time from admission 3–7 days, the SRT probability of healthcare acquisition was >0.5 in 33/82 (40.2%). The methodology developed can provide rapid feedback on HOCIs that could be useful for infection prevention and control teams, and warrants further prospective evaluation. The integration of epidemiological and sequence data is important given the low mutation rate of SARS-CoV-2 and its variable incubation period. COG-UK HOCI funded by COG-UK consortium, supported by funding from UK Research and Innovation, National Institute of Health Research and Wellcome Sanger Institute.

## Introduction

Nosocomial transmission of SARS-CoV-2 presents a significant health risk to both vulnerable patients and to healthcare workers (HCWs) (Kursumovic et al., 2020; Wang et al., 2020; Leclerc et al., 2020; The DELVE Initiative, 2020; Shah et al., 2020). There is a variable incubation period, extending up to day 14 from exposure to the virus in symptomatic cases (Lauer et al., 2020). It is also known that transmission is possible from asymptomatic or presymptomatic carriers (He et al., 2020; Rivett et al., 2020; Oran and Topol, 2020; Lucey et al., 2021), complicating identification of hospital acquisition among hospital onset COVID-19 infections (HOCIs) and tracing of likely sources of infection.

There is now substantial evidence from retrospective studies that genome sequencing of epidemic viruses, together with standard infection prevention and control (IPC) practice, better excludes nosocomial transmissions and better identifies routes of transmission than IPC investigation alone (Brown et al., 2019; Houldcroft et al., 2018; Roy et al., 2019). The development of rapid sequencing methods capable of generating pathogen genomes within 24–48 hr has recently created the potential for clinical IPC decisions to be informed by genetic data in near-real time (Meredith et al., 2020). Although SARS-CoV-2 has a low mutation rate (Fauver et al., 2020), sufficient viral diversity exists for viral sequences to provide information regarding potential transmission clusters (van Dorp et al., 2020). However, phylogenetic methods alone cannot reliably identify linked infections, and the need for clinical teams to gather additional patient data presents challenges to the timely interpretation of SARS-CoV-2 sequence data.

To overcome these barriers, we have developed a sequence reporting tool (SRT) that integrates genomic and epidemiological data from HOCIs to rapidly identify closely matched sequences within the hospital and assign a probability estimate for nosocomial infection. The output report is designed for prospective use to reduce the delay from sequencing to impact on IPC practice. The work was conducted as part of the COVID-19 Genomics (COG) UK initiative, which sequences large numbers of SARS-CoV-2 viruses from hospitals and the community across the UK (COVID-19 Genomics UK (COG-UK), 2020). Here we describe the performance of the SRT using COG-UK sequence data for HOCI cases collected from Glasgow and Sheffield between February and May 2020 and explore how it may have provided additional useful information for IPC investigations.

## Materials and methods

The SRT methodology is applied to HOCI cases, defined here as inpatients with first positive SARS-CoV-2 test or symptom onset >48 hr after admission, without suspicion of COVID-19 at admission. The SRT algorithm returns an estimate of the probability that each HOCI acquired their infection post-admission within the hospital, with information provided on closely matching viral sequences from the ward location at sampling and wider hospital. Results for individual HOCIs are evaluated in relation to the IPC classification system recommended by Public Health England (PHE), based on interval from admission to positive test: 3–7 days post admission = indeterminate healthcare-associated infection (HCAI); 8–14 days post admission = probable HCAI; >14 days post admission = definite HCAI (Public Health England, 2020). We also applied the PHE definition of healthcare-associated COVID-19 outbreaks (Public Health England, 2020) (i.e. ≥2 cases associated with specific ward, with at least one being a probable or definite HCAI) to ward-level data, and for each outbreak evaluated whether there was one or more distinct genetic cluster. This was determined by consecutive linkage of each HOCI into clusters using a two single-nucleotide polymorphism (SNP) threshold (with HOCIs assigned to a genetic cluster if a sequence match to any member). Sequences with <90% genomic coverage were excluded from all analyses.

## Data collection and processing

## Glasgow

During the first wave of SARS-CoV-2, the MRC-University of Glasgow Centre for Virus Research collected residual clinical samples from SARS-CoV-2-infected individuals following diagnosis at the West of Scotland Specialist Virology Centre. Samples were triaged for rapid sequencing using Oxford Nanopore Technologies (ONT) for suspected healthcare-related infections or Illumina sequencing in all other cases (details in Appendix 1).

## Sheffield

Residual clinical samples from SARS-CoV-2-positive cases diagnosed at Sheffield Teaching Hospitals NHS Foundation Trust were sequenced at the University of Sheffield using ARTIC network protocol (ARTIC Network, 2020) and ONT. Throughout the epidemic, members of the IPC team were notified by the laboratory and by clinical teams of positive results and reviewed relevant areas to ensure optimisation of practice and appropriate management of patients. Electronic reports were created contemporaneously, including an assessment as to whether suspected linked cases were present based on ward-level epidemiology. As part of SRT validation, these reports were accessed retrospectively by a study team member blind to the sequencing data and each included HOCI case was defined as being thought unlinked to other cases, a presumed index case in an outbreak or a presumed secondary case.

## HOCI classification algorithm

The sequence matching and probability score algorithm is run separately for each ‘focus sequence’ corresponding to a HOCI. We use associated metadata to assign other previously collected sequences to categories representing where the individual may be part of a SARS-COV-2 transmission network:

It is possible for samples to be members of multiple reference sets. For example, an outpatient may be involved in SARS-CoV-2 transmission at the institution they attended and/or in community transmission.

For each run of the algorithm, pairwise comparisons are conducted between the focus sequence and each sequence within the unit reference set, institution reference set and community reference set. A reference set sequence is considered a close match to the focus sequence if there is a maximum of two SNP differences between them. This choice was based on reported healthcare-associated outbreak events (Meredith et al., 2020; Rockett et al., 2020) and the overall mutation rate of SARS-CoV-2 (details in Appendix 1).

## Probability calculations

We use an expression of Bayes theorem to estimate probabilities for post-admission infection of each focus case divided by exposure on the unit, within the rest of the institution and from visitors (if allowed). An estimate of the prior probability (Pprior) of post-admission infection for each focus case is modified to a posterior probability according to the information provided by the sequence data. The algorithm is based on sound statistical principles, but involves heuristic approximations.

In symptomatic focus cases, we base Pprior on the time interval (t) from admission to date of symptom onset or first positive test (if date of symptom onset not recorded). We calculate Pprior = F(t), where F() is the cumulative distribution function of incubation times (Lauer et al., 2020) (derivation in Appendix 1).

In theory, it would be optimal to use all of the information in the exact sequences observed. However, with the goal of constructing a computationally simple algorithm, we base our calculations on the probability of observing a similar sequence (within two SNPs) to that actually observed for each focus case conditional on each potential infection source/location: infection in the community, current unit/ward or elsewhere in the hospital/institution, or from a visitor. For the unit and hospital, we estimate this probability using the observed sequence match proportion (on pairwise comparison to the focus sequence) in the unit reference set and institution reference set, respectively. For community- or visitor-acquired infection, we use a weighted proportion of matching sequences in the community reference set, with weightings determined by a calibration model that describes geographic clustering of similar sequences among community-acquired infections (described in Appendix 1). The geographic weighting model was fitted separately for each study site using sequences strongly thought to represent community-acquired infection: all community-sampled sequences and patients presenting to the Emergency Department with COVID-19, excluding those recorded as being HCWs.

## Software

The analysis was conducted in R (v. 4.0.2, R Foundation, Vienna) using sequence processing and comparison functions from ape (v. 5.4) and geospatial functions in the PostcodesioR (v. 0.1.1) and gmt packages (v. 2.0). R code to run the algorithm is available (Stirrup, 2021), and it has also been implemented as a standalone SRT for prospective use (HOCI Sequence Reporting Tool working group, 2020) within COV-GLUE (Singer et al., 2020).

## Results

## Study populations

## Glasgow

The Glasgow dataset included 1199 viral sequences (available as of 23 June 2020): 426 were derived from community sampling sites, 351 from patients presenting to Emergency Department or acute medical units, 398 from hospital inpatients and 24 from outpatients. Limited data were available regarding the total number of HCWs testing positive and their identification among community samples, but 15 sequences were recorded as being from HCWs. First positive test dates ranged from 3 March to 27 May 2020. All consensus sequences had genomic coverage >90%.

We applied the SRT algorithm to data from three hospitals with required metadata available, for which 128/246 inpatient cases with sequences were HOCIs. Two of these patients had been transferred from another hospital within 14 days prior to their positive test and were not processed as focus sequences. One inpatient without recorded sampling location was excluded, leaving 125 HOCIs for analysis. Population sequencing coverage was 536/1578 (34.0%) overall for patients at the three hospitals and 128/328 (39.0%) for HOCIs specifically (Appendix 1—figure 1).

## Sheffield

The Sheffield dataset included 1630 viral sequences with accompanying metadata (available as of 10 October 2020): 714 were from inpatients, 117 were from outpatients and 799 were from HCWs. For this retrospective evaluation, 447/714 inpatient samples taken on date of admission were assumed to represent community-onset cases and used to calibrate the model. First positive test dates ranged from 23 February to 30 May 2020. One sequence with genome coverage <90% was dropped from further analysis (an inpatient on date of admission). 201 of the inpatients were HOCIs. Population sequencing coverage was 714/977 (73.1%) overall for inpatients, 201/261 (77.0%) for HOCIs specifically and 799/962 (83.1%) for HCWs.

## Comparison to standard PHE classification

SRT algorithm results in comparison to standard PHE classifications are summarised in Figure 1 and Table 1. The majority of HOCI cases in Glasgow (78/125, 62.4%) and over a third in Sheffield (71/201, 35.3%) met the definition of a definite HCAI and so are known to have acquired the virus post-admission irrespective of sequencing results. The probable HCAI cases formed the next largest group at each site. Overall, the SRT algorithm identified close sequence matches from the same ward for 66.4% of definite and 64.2% of probable HCAIs, indicating likely within-ward transmission (examples in case studies). When one or more close sequence match was identified on the focus sequence’s ward, the SRT probability of infection on the ward was >0.5 in 185/189 cases (Figure 2). For indeterminate HCAIs, the SRT probability of HCAI was >0.5 in 33/82 (40.2%), and in 27/33 (81.8%) a close sequence match on the ward was present. Overall, 14/125 (11.2%) HOCIs in Glasgow and 175/201 (87.1%) in Sheffield had at least one close sequence match to a HCW sample, reflecting the much greater availability of sequences from HCWs in the Sheffield dataset.

![Figure 1.](https://cdn.elifesciences.org/articles/65828/elife-65828-fig1-v2.jpg)

**Figure 1.:** Plot of the posterior probability of healthcare-associated infection (HCAI) for (a) Glasgow and (b) Sheffield hospital onset COVID-19 infection cases from the sequence reporting tool algorithm against the prior probability of HCAI based only on time from admission to diagnosis, grouped by standard infection prevention and control classification recommended by Public Health England. Marginal histograms are displayed with bin-widths of 0.05.

![Figure 2.](https://cdn.elifesciences.org/articles/65828/elife-65828-fig2-v2.jpg)

**Figure 2.:** a) Glasgow and (b) Sheffield hospital onset COVID-19 infection cases grouped by standard Public Health England classification.In cases where there are no close sequence matches in the dataset (including among community cases), the results returned are based solely on the priors and the metadata; this explains the fact that there are some cases with estimated posterior probability of infection on the ward greater than 0.5 for whom there were no sequence matches on the ward.

In 16/244 (6.6%) cases that met the probable or definite HCAI definitions, there was no sequence match within the hospital; this is likely due to incomplete sequence data from SARS-CoV-2 hospitalised cases and staff (with population sequencing coverage <40% patients and very limited for staff from Glasgow and ≈75% of patients and staff in Sheffield) and the presence of asymptomatic and/or undiagnosed carriers. To reflect this the SRT will report ‘This is a probable/definite HCAI based on admission date, but we have not found genetic evidence of transmission within the hospital’ in such situations. There were 26 HOCIs in the Sheffield dataset for whom it was recorded that visitors were allowed on the ward at time of sampling. In three of these, the estimated probability of infection from a visitor was between 0.4 and 0.5 (all had ≥18 days from admission and no ward close sequence matches).

Within the Sheffield dataset, we identified six wards with two genetically distinct outbreak clusters (of two or more patients) and three wards with three distinct outbreaks (see Case study 2). Standard IPC assessment had classified each as a single outbreak. We also identified 10 and 44 HOCIs in the Glasgow and Sheffield datasets, respectively, with no apparent genetic linkage to other HOCI cases on the ward but who met the PHE definition of inclusion within an outbreak event (Table 2).

## Comparison to local IPC conclusions in Sheffield

Contemporaneous notes by IPC teams in Sheffield classified 18/201 HOCIs as the index case in outbreaks. IPC staff defined an index case as the first detected in an environment regardless of prior inpatient stay and, correspondingly, of these 14/18 were the first sequence on their ward and one was the second (the first 1 day earlier from a different bay on the ward was also recorded as an index case, and IPC staff deemed a ward outbreak with unclear index or possibly two index cases). Of the 18 index cases, 11 showed at least one subsequent close sequence match on the same ward (the two index cases on a single ward were not genetically similar, and for 1/18 there were no subsequent sequences from the ward). The median SRT probability of HCAI was 0.70 (IQR 0.22–1.00, range 0.04–1, >0.5 in 12/18).

A further 144/201 HOCIs were classified as being part of local outbreaks, and among these the median SRT probability of HCAI was 0.98 (IQR 0.89–1.00, range 0.02–1.00, >0.5 in 129/144) with one or more close sequence match on the same ward in 104/144. The remaining 39/201 HOCIs, including 10 that were not recorded as HOCIs at the time, were classified by the IPC teams as not being part of local outbreaks. Among these the median SRT probability of HCAI was 0.74 (IQR 0.23–0.99, range 0.02–1.00, >0.5 in 23/39), with one or more close sequence matches on the same ward in 7/39.

## Case study 1

Figure 3 shows a phylogenetic tree of eight HOCIs within a single ward at a Glasgow hospital (Hospital 5, Unit 93), alongside associated metadata and SRT probability outputs. The first HOCI detected (UID0032) was transferred from another hospital within the previous 2 weeks and so SRT output was not generated. All subsequent HOCIs return close sequence matches to at least one prior case on the ward, leading to SRT probability estimates of ward-acquired infection >0.9, even for UID0017 (an indeterminate HCAI). The phylogenetic tree indicates UID0032 has an SNP lacked by most of the cases identified on the ward, and therefore did not seed all of the cases in the outbreak cluster. Also shown is a single HOCI from a different ward in the same hospital (UID0025); this individual was an indeterminate HCAI, but a higher proportion of similar viral sequences within the hospital in comparison to their local community led to a SRT result of probable hospital-acquired infection.

![Figure 3.](https://cdn.elifesciences.org/articles/65828/elife-65828-fig3-v2.jpg)

**Figure 3.:** The black lines represent the time from admission to sampling. The values below the line are the posterior probability for unit infection + the posterior probability of hospital infection from the sequence reporting tool. The tip nodes are coloured according to the local authority area of the community surveillance sequences (circles) or of the patients (crosses).

## Case study 2

Figure 4 shows phylogenetic trees relating to three distinct viral lineages identified on a single ward in the Sheffield dataset (classified by contemporaneous IPC investigation as a single outbreak). Two of these lineages also include sequences from inpatients sampled from other wards within the same hospital. Detailed ward movement data highlighted additional possible links between patients in the B.2.1 cluster. Both UID0149 and UID0157 were present at LOC0111 prior to their sample dates.

![Figure 4.](https://cdn.elifesciences.org/articles/65828/elife-65828-fig4-v2.jpg)

**Figure 4.:** The tree tip nodes are coloured according to ward locations. The black lines represent the time from admission to sampling. The values below the line are the posterior probability for unit infection + the posterior probability of hospital infection from the sequence reporting tool. The circle containing a number represents community sequences that are identical and at the base of this lineage (n = 36).

## Discussion

We have developed a novel approach for identification and investigation of hospital-acquired SARS-CoV-2 infections combining epidemiological and sequencing data, designed to provide rapid and concise feedback to IPC teams working to prevent nosocomial transmission. Through retrospective application to clinical datasets, we have demonstrated that the methodology is able to provide confirmatory evidence for most PHE-defined definite and probable HCAIs and provide further information regarding indeterminate HCAIs. Thus the SRT may allow IPC teams to optimise their use of resources on areas with likely nosocomial acquisition events.

While the SRT is not likely to change IPC conclusions in cases meeting the definition of ‘definite’ or ‘probable’ HCAI based on interval from admission to symptom onset, in 91% of cases it did identify patients in the same ward or elsewhere in the hospital who could plausibly be linked to the HOCI within a single outbreak event. Those definite and probable HOCIs without close sequence matches are likely to reflect transmission from sources within the hospital that have either not been diagnosed or who were diagnosed without viral sequencing. In such cases, it is impossible to calculate a probability of transmission and the SRT will simply state that no sequence matches were found within the hospital.

For cases meeting the definition of ‘indeterminate healthcare associated’, the probability scores returned would be useful for IPC teams. These probabilities are dependent on comparison to sequences from cases of community-acquired infection obtained either from direct community sampling or from patients sampled at admission. The Sheffield dataset was lacking the former data source, but the SRT nonetheless classified a similar proportion of ‘indeterminate healthcare associated’ HOCIs as community-acquired infections to that found in the Glasgow dataset (approximately 60%).

Current PHE guidelines define healthcare-associated COVID-19 outbreaks as two or more cases associated with a specific setting (e.g. ward), with at least one case having illness onset after 8 days of admission (Public Health England, 2020). However, the guidelines note that ‘investigations of healthcare-associated SARS-CoV-2 infection should also take into account COVID-19 cases categorised as "indeterminate healthcare associated"’ (i.e. onset 3–7 days after admission), for which our SRT output would be useful. In most HOCIs meeting this definition of inclusion within an outbreak event, we found evidence of clusters of similar viral sequences located on the ward concerned, and the SRT results were in line with available local IPC classifications in the majority of cases. However, a substantial minority (54/279) of HOCIs, although assumed to be part of a ward outbreak, were, in fact, isolated cases for which the sequencing data refuted genetic linkage to other sequences from the ward. The SRT also provided evidence of wards where IPC-defined outbreak events comprised two or three clearly distinct viral lineages.

The retrospective datasets analysed in this study represent the first few months of the COVID-19 epidemic in the UK, and nosocomial transmission of the virus in the UK during this period has previously been reported at multiple sites (Meredith et al., 2020; Rickman et al., 2021; Carter et al., 2020). HCWs were at increased risk of infection and adverse health outcomes (Kursumovic et al., 2020; Wang et al., 2020; The DELVE Initiative, 2020; Shah et al., 2020; Houlihan et al., 2020) and could have been important drivers of nosocomial transmission (Rivett et al., 2020). Data were limited for Glasgow, but the Sheffield dataset contained a large number of sequences obtained from HCWs, with population sequencing coverage for this group >80%, and there was a close sequence match to at least one HCW observed for 87% of HOCIs. Our analysis has not evaluated direction of transmission to or from HCWs, but they were clearly linked into transmission networks within the hospital. A limitation of the current SRT approach and of the retrospective data available is that they do not include detailed information regarding work locations for HCWs. However, prospective use of the SRT would allow IPC teams to investigate linkage from a HOCI to any HCWs flagged as having a close sequence match.

While a phylogenetic approach is useful in excluding direct transmission between cases, it can be more problematic to confirm transmission source (Volz and Frost, 2013). Phylogenetic models can evaluate the full genetic information provided by viral sequence data, but there are challenges in incorporating and summarising associated patient metadata in a timely fashion (Villabona-Arenas et al., 2020). The challenge of timely collection and standardisation of patient metadata is also relevant for use of the SRT that we have developed, but it is possible to automate such processes through electronic patient record systems. There have been advances in recent years in the computational efficiency and workflow standardisation possible for phylogenetic analyses that have made it easier to use these methods for real-time investigation of outbreaks, for example, through the development of the Nextstrain project (Hadfield et al., 2018; Huddleston et al., 2021). However, there does not currently exist phylogenetic software for SARS-CoV-2 that produces reports or other outputs designed for direct and immediate use by IPC professionals. There will be cases in which phylogenetic analysis would provide information beyond that returned by the SRT, and the two approaches may be complementary to one another for outbreak investigation.

Comparison of SRT output to phylogenetic trees in a number of test cases suggested that some clusters of genetically similar cases identified within a specific ward likely represented more than one transmission event onto the ward from similar viral lineages circulating within the healthcare system. Whilst monophyletic clusters associated with a single location are easier to interpret, we consider the presence of viruses within a ward or hospital that are genetically similar to a HOCI as evidence for nosocomial infection even when they are not plausible transmission sources themselves, given the potential for asymptomatic transmission (He et al., 2020; Rivett et al., 2020; Oran and Topol, 2020; Lucey et al., 2021) and complex transmission networks (Meredith et al., 2020).

The SRT uses a number of heuristic approximations in order to provide an integrated summary of epidemiological and sequence data. However, this choice is associated with the limitation that it does not provide a full probabilistic model of potential transmission networks. Further development of the SRT would also aim to more fully incorporate patient movement data and shift locations for HCWs.

We believe that collaboration between methodologists, virologists, IPC clinicians and software engineers is essential in order to create workflows and reporting systems that will enable the routine use of pathogen sequence data for IPC. The SRT represents such a collaboration, and it has been designed to enable automation of the linkage and processing of viral sequence and patient metadata and subsequent feedback of relevant information to IPC staff. The automated feedback provided by the SRT is nonetheless dependent on timely sequencing of a high proportion of viral samples from cases within the hospital concerned, ideally in combination with sequences also available from community-sampled cases. In the UK this has been possible through the national COG-UK project (COVID-19 Genomics UK (COG-UK), 2020). Denmark has also implemented high population-coverage sequencing of SARS-CoV-2 (Bager et al., 2021), but this is not the case for most countries. The emergence and rapid dominance of lineage B.1.1.7 in the UK (Volz et al., 2021) has provided a case study for the impact of national-level genomic surveillance, but further evidence is required to determine whether rapid sequencing is worth the necessary investment for routine use within IPC practice. This judgement would also be dependent on the available health infrastructure and resources at both the local and national levels.

Prospective evaluation of the SRT is currently underway within a multicentre study in the UK (Blackstone et al., 2021). This study and its accompanying research programme will evaluate the impact of routine viral sequencing and use of the SRT on IPC knowledge, actions and outcomes, and will include quantitative, qualitative (Flowers et al., 2021) and health economic analyses to help guide the future development of pathogen genomics for IPC.

Our novel approach to the investigation of HOCIs has shown promising characteristics on retrospective application to two clinical datasets. The SRT described allows rapid feedback on HOCIs that integrates epidemiological and sequencing data to generate a simplified report at the time that sequence data become available. Prospective evaluation is required in order to recommend use of the SRT in clinical practice, and this work is ongoing. The methodology has been developed for hospital inpatients, but the principles may also be applicable to other settings.
