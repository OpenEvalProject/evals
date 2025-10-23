# Reproducible diagnostic metabolites in plasma from typhoid fever patients in Asia and Africa

## Authors

- Elin Näsström<sup>1</sup>
- Christopher M Parry<sup>2</sup>
- Nga Tran Vu Thieu<sup>4</sup>
- Rapeephan R Maude<sup>6</sup>
- Hanna K de Jong<sup>7</sup>
- Masako Fukushima<sup>2</sup>
- Olena Rzhepishevska<sup>1</sup>
- Florian Marks<sup>9</sup>
- Ursula Panzner<sup>9</sup>
- Justin Im<sup>9</sup>
- Hyonjin Jeon<sup>9</sup>
- Seeun Park<sup>9</sup>
- Zabeen Chaudhury<sup>9</sup>
- Aniruddha Ghose<sup>10</sup>
- Rasheda Samad<sup>10</sup>
- Tan Trinh Van<sup>4</sup>
- Anders Johansson<sup>11</sup>
- Arjen M Dondorp<sup>6</sup>
- Guy E Thwaites<sup>4</sup>
- Abul Faiz<sup>13</sup>
- Henrik Antti<sup>1</sup> †
- Stephen Baker<sup>4</sup> ([ORCID: 0000-0003-1308-5755](https://orcid.org/0000-0003-1308-5755)) †

### Affiliations

1. Department of Chemistry, Computational Life Science Cluster Umeå University Umeå Sweden
2. Clinical Sciences Liverpool School of Tropical Medicine Liverpool United Kingdom
3. School of Tropical Medicine and Global Health Nagasaki University Nagasaki Japan
4. The Hospital for Tropical Diseases, Wellcome Trust Major Overseas Programme Oxford University Oxford United Kingdom
5. Clinical Research Unit Ho Chi Minh City Vietnam
6. Mahidol-Oxford Tropical Medicine Research Unit (MORU), Faculty of Tropical Medicine Mahidol University Bangkok Thailand
7. Department of Internal Medicine, Division of Infectious Diseases and Center for Infection and Immunity Amsterdam (CINIMA) University of Amsterdam Amsterdam the Netherlands
8. Center for Experimental Molecular Medicine (CEMM), Academic Medical Center University of Amsterdam Amsterdam The Netherlands
9. The International Vaccine Institute Seoul South Korea
10. Chittagong Medical College Hospital Chittagong Bangladesh
11. Department of Clinical Microbiology Umeå University Umeå Sweden
12. Centre for Tropical Medicine Oxford University Oxford United Kingdom
13. Malaria Research Group and Dev Care Foundation Dhaka Bangladesh
14. Department of Medicine The University of Cambridge Cambridge United Kingdom

† Corresponding author

## Abstract

10.7554/eLife.15651.001 Salmonella Typhi is the causative agent of typhoid. Typhoid is diagnosed by blood culture, a method that lacks sensitivity, portability and speed. We have previously shown that specific metabolomic profiles can be detected in the blood of typhoid patients from Nepal (Näsström et al., 2014). Here, we performed mass spectrometry on plasma from Bangladeshi and Senegalese patients with culture confirmed typhoid fever, clinically suspected typhoid, and other febrile diseases including malaria. After applying supervised pattern recognition modelling, we could significantly distinguish metabolite profiles in plasma from the culture confirmed typhoid patients. After comparing the direction of change and degree of multivariate significance, we identified 24 metabolites that were consistently up- or down regulated in a further Bangladeshi/Senegalese validation cohort, and the Nepali cohort from our previous work. We have identified and validated a metabolite panel that can distinguish typhoid from other febrile diseases, providing a new approach for typhoid diagnostics. DOI: http://dx.doi.org/10.7554/eLife.15651.001

## Introduction

Typhoid is a systemic infection caused by the bacterium Salmonella Typhi (S. Typhi) (Parry et al., 2002; Dougan and Baker, 2014). With an estimated 21 million cases annually, typhoid remains a persistent global health issue (Buckle et al., 2012; Ochiai et al., 2008). The symptoms of typhoid arise after the organism invades the gastrointestinal wall and enters the bloodstream (Everest et al., 2001). Isolating the organism from the bloodstream is the mainstay of typhoid diagnostics (Gilman et al., 1975; Parry et al., 2011), but this method lacks sensitivity and researchers are aiming to discover biomarkers that may become a more reliable and rapid approach to diagnosing disease (Baker et al., 2010). One approach for discovering biomarkers is metabolomics, a method detecting low-molecular-weight metabolites in biological materials by mass spectrometry (Madsen et al., 2010). Our previous work demonstrated that significant and reproducible metabolite profiles could segregate S. Typhi cases, Salmonella Paratyphi A cases, and asymptomatic controls in a Nepali patient cohort (Näsström et al., 2014). Further, we found that a combination of six metabolites could define the infecting pathogen in the blood of febrile patients. These data represented a major step forward in the discovery of biomarkers with the potential to be future typhoid diagnostics. We have applied a similar approach with plasma samples collected from febrile patients in Bangladesh and Senegal to further investigate and validate our previous findings.

## Results

## Plasma metabolites in Bangladeshi typhoid fever patients

By hierarchical multivariate curve resolution, we resolved 394 peaks from the GCxGC-TOFMS data (Materials and methods) in 30 plasma samples from febrile patients in Bangladesh (

![Figure 1.](https://cdn.elifesciences.org/articles/15651/elife-15651-fig1-v1.jpg)

**Figure 1.:** (A) OPLS-DA model generated from GCxGC-TOFMS data from the plasma of 10 patients with culture-positive typhoid and 10 fever controls using 236 metabolites. Regular (circles) and cross-validated (squares) scores for the first predictive component (t[1] and tcv[1], respectively, linked by broken line) showing a separation between culture-positive typhoid (red) and fever control samples (grey) (p=0.006). (B) Column plot of the predicted scores for the first predictive component (tPS[1]) where clinically suspected typhoid samples (n = 9) (blue columns) have been predicted into the model distinguishing between culture-positive typhoid (red) and fever control samples (grey). Plot shows five samples were more similar to the culture-positive typhoid samples and three more similar to the controls; one sample remained marginal. The blue stars identify PCR-amplification-positive samples.DOI: http://dx.doi.org/10.7554/eLife.15651.002

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/15651/elife-15651-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (A) OPLS-DA model generated from UHPLC-Q-TOFMS data from the urine of 10 patients with culture-positive typhoid and 10 fever controls using 941 metabolites (positive ionization mode). Regular (circles) and cross-validated (squares) scores for the first predictive component (t[1] and tcv[1], respectively, linked by broken line) showing a separation between culture-positive typhoid (red) and fever control samples (grey) (p=0.025). (B) Column plot of the predicted scores for the first predictive component (tPS[1]) where culture-negative/suspected typhoid typhoid samples (n = 9) (blue columns) have been predicted into the model distinguishing between culture-positive typhoid (red) and fever control samples (grey); PCR-amplification-positive samples are identified by the blue stars.DOI: http://dx.doi.org/10.7554/eLife.15651.003

## Prediction of culture-negative/clinically suspected typhoid fever

A major challenge in diagnosing typhoid is identifying true typhoid patients but have a negative blood culture result (Moore et al., 2014). We observed a significant overlap between the culture-negative/clinically suspected typhoid metabolite profiles with both the culture-positive group and the fever control group (Figure 1B). We used the OPLS-DA model that distinguished between the culture-positive typhoid patients and the fever controls to predict the clinically suspected typhoid samples. We found that 5/9 plasma samples had a metabolite profile indicative of culture-positive typhoid and three exhibited a greater degree of resemblance to fever controls (one indifferent) (Figure 1B). Notably, 3/5 clinically suspected typhoid samples with a metabolite profile indicative of typhoid were additionally PCR amplification positive for S. Typhi in blood (Table 1 and Figure 1B). We also investigated potential diagnostic typhoid signatures in urine samples from the same patients using UPLC-Q-TOFMS (Materials and methods). Examination of 941 putative metabolite peaks obtained from urine using positive ionization an OPLS-DA model resulted in significantly different metabolite profiles between the S. Typhiculture-positive patients and the fever controls (p=0.025) (Figure 1—figure supplement 1 and Supplementary file 1B).

## Reproducible typhoid metabolite patterns in Bangladeshi and Nepali cohorts

We next compared informative plasma metabolites of Bangladeshi

![Figure 2.](https://cdn.elifesciences.org/articles/15651/elife-15651-fig2-v1.jpg)

**Figure 2.:** OPLS-DA models generated from GCxGC-TOFMS data using 15 informative metabolites from the current study (Bangladeshi cohort) and the previous study in Nepali cohort that were consistently up- or downregulated and significantly different in a multivariate model separating culture-positive S. Typhi patients from controls. (A) Regular (circles) and cross-validated (squares) scores for the first predictive component (t[1] and tcv[1], respectively, linked by broken line) showing a separation between culture-positive typhoid (red; n = 10) and fever control samples (grey; n = 10) (p=0.016) in the Bangladeshi cohort. (B) Column plot of model covariance loadings (w*[1]) for the first predictive component for the 15 common named metabolites in the Bangladeshi cohort, showing metabolites with a higher relative concentration in the culture-positive typhoid group in red and metabolites with a higher relative concentration in the fever control group in grey. (C) Regular (circles) and cross-validated (squares) scores for the first predictive component (t[1] and tcv[1], respectively, linked by broken line) showing a separation between culture-positive typhoid (red; n = 33 including eight analytical replicates) and afebrile control samples (grey; n = 32 including seven analytical replicates) (p<0.0001) from the Nepali cohort. (D) Column plot of model covariance loadings (w*[1]) for the first predictive component for the 15 common named metabolites in the Nepali cohort, showing metabolites with a higher relative concentration in the typhoid group in red and metabolites with a higher relative concentration in the afebrile control group in grey.DOI: http://dx.doi.org/10.7554/eLife.15651.005

## Typhoid fever metabolites in Bangladeshi and Senegalese validation cohorts

For further validation, we analyzed an additional 54 plasma samples from febrile patients from Bangladesh and Senegal using a different analytical technique (GC-TOFMS, methods). This validation cohort included samples from patients with confirmed typhoid and samples from patients with malaria or infections caused by other pathogens. Through an independent targeted processing approach, we detected 247 putative metabolites; after manual filtering, 104 metabolites were suitable for modeling (

![Figure 3.](https://cdn.elifesciences.org/articles/15651/elife-15651-fig3-v1.jpg)

**Figure 3.:** OPLS-DA models generated from GC-TOFMS using 104 metabolites. (A) Column plot of the first predictive component scores, t[1] showing a separation of typhoid infection samples (red; n = 14) from the two control groups; malaria (light grey; n = 15) and infections caused by other bacteria/pathogens (grey; n = 25) (p<0.0001). For the Bangladeshi samples, there is a clear separation except for one control sample behaving as a typhoid sample, there is more overlap for the Senegalese samples. (B) Column plot of the first predictive component scores, t[1] showing a separation of typhoid infection samples (red; n = 14) from malaria samples (light grey; n = 15) (p<0.001). There is a clear separation for the Bangladeshi samples and for the Senegalese samples except two typhoid samples behaving as malaria.DOI: http://dx.doi.org/10.7554/eLife.15651.006

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/15651/elife-15651-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** Score plot with the scores of the two first predictive component, t[1] (x-axis) and t[2] (y-axis) showing a separation of typhoid infection samples, shown in red, from the two control groups (malaria, shown in light grey, and infections caused by other bacteria/pathogens, shown in dark grey) along the first component (with some overlap) and a separation of the malaria control group from the other infections control group along the second component (with some overlap) (p=0.0035).DOI: http://dx.doi.org/10.7554/eLife.15651.007

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/15651/elife-15651-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** The metabolite pattern separating typhoid samples from controls in the Bangladeshi/Senegalese validation cohort was compared to the corresponding metabolite patterns in the Bangladeshi cohort in the current study and the Nepali cohort in the previous study to find metabolites that were consistently up- or downregulated and multivariate significant in the three cohorts. Column plots of first predictive component scores (t[1]) for OPLS-DA models separating typhoid samples (red) from controls (dark grey, including a malaria group in light grey in A) for (A) GC-TOFMS data of plasma samples from the Bangladeshi/Senegalese validation cohort based on 24 significant metabolites consistently up- or downregulated in the Bangladeshi/Senegalese cohort and the Bangladeshi cohort and/or the Nepali cohort (p<0.0001), (B) GCxGC-TOFMS data of plasma samples from the Bangladeshi cohort based on 13 significant metabolites consistently up- or downregulated in the Bangladeshi/Senegalese cohort and the Bangladeshi cohort (p=0.39) and (C) GCxGC-TOFMS data of plasma samples from the Nepali cohort based on 14 significant metabolites consistently up or downregulated in the Bangladeshi/Senegalese cohort and the Nepali cohort (p<0.0001). Five metabolites were consistently up or downregulated in all three cohorts.DOI: http://dx.doi.org/10.7554/eLife.15651.008

The informative plasma metabolites from the Bangladeshi/Senegalese validation cohort were compared to the primary Bangladeshi and Nepali cohorts. We identified 49 common metabolites across all datasets. After comparing the direction of change and degree of multivariate significance, we found 24 metabolites that were consistently up- or downregulated in the Bangladeshi/Senegalese validation cohort and the Bangladeshi cohort and/or the Nepali cohort (Supplementary file 1D). OPLS-DA models of the consistently up- or downregulated metabolites resulted in significant separations between those with typhoid and the control samples for the Bangladeshi/Senegalese validation cohort (p<0.0001) (Figure 3—figure supplement 2A) and for the Nepali cohort (p<0.0001) (Figure 3—figure supplement 2C), the model was weaker for the primary Bangladeshi cohort (p=0.39) (Figure 3—figure supplement 2B) (Supplementary file 1B).

## Discussion

This study augments our previous findings and provides additional insight into next generation typhoid diagnostics (Näsström et al., 2014). Previously, we aimed to identify metabolite profiles that could distinguish between patients with S. Typhi and S. Paratyphi A infections. We hypothesized that metabolite profiles might differentiate clinically indistinguishable infections caused by these genetically related pathogens (Didelot et al., 2007; Maskey et al., 2006); asymptomatic individuals constituted the control group. Here, we aimed to identify S. Typhi metabolite profiles in different settings without S. Paratyphi A disease (Maude et al., 2015). This approach was a greater challenge given a heterogeneous fever control group and a group of patients with suspected typhoid fever. We suggest this study more closely reflects a real situation given the non-specific presentation of febrile diseases. We also assessed the diagnostic potential of urine using this methodology as it is a convenient specimen (Gilman et al., 1975).

Using a validation cohort from Asia and Africa we were able to identify significant, reproducible metabolite profiles in the blood of patients with typhoid. The identified metabolites significantly discriminated S. Typhi-culture-positive individuals from patients with alternative febrile diseases, including malaria. Among patients with clinically suspected typhoid but a negative blood culture, we identified metabolite profiles consistent with the confirmed typhoid patient profiles (Nga et al., 2010). The metabolite profiles in urine also significantly segregated the typhoid patients from the febrile controls, but did not provide the same predictions as the plasma samples for the culture-negative patients. The culturenegative clinically suspected typhoid group is challenging because of the lack of a satisfactory reference standard diagnostic test, but this innovative method allows a new approach to investigate this problematic patient group using plasma samples.

The most important finding from this study was the identification and validation of significantly variable metabolites that can identify blood culture confirmed typhoid fever patients in distinct patient cohorts (Asia and Africa) with differing control populations. At least 24 metabolites have the potential to identify typhoid fever patients in these patients. These included glycerol-3-phosphate (carbon source and precursor for phospholipid biosynthesis) (Austin and Larson, 1991), stearic acid (component of liposome)(Galdiero et al., 1994), and linoleic acid (bactericidal activity) (Yang et al., 2010), pyruvic acid, and creatinine. Furthermore, leucine and phenylalanine were consistently up- or downregulated between all collections.

New approaches are needed for the diagnosis of tropical febrile diseases. We have identified and validated a panel of metabolites that can identify febrile patients with typhoid. The next challenges are to corroborate these targets in larger patient numbers and incorporate into simple diagnostic test formats. This approach could be potentially expanded into other tropical febrile diseases.

## Materials and methods

To measure the systemic metabolite profiles associated with typhoid, we selected plasma and urine samples from 30 patients in a febrile disease study conducted in Chittagong, Bangladesh (Maude et al., 2015): Ten patients had blood culture S. Typhi confirmed typhoid; nine patients had a clinical diagnosis of typhoid (blood culture negative ± PCR positive for S. Typhi); and 11 matched individuals had a febrile disease other than typhoid (fever controls) (Table 1 and Supplementary file 2). The study sites, population and study design are described in detail in the supplementary information and are published elsewhere (Maude et al., 2015). Validation samples included plasma samples from 54 patients from Bangladesh and Senegal with 14 patients having confirmed S. Typhi infection, 15 patients having malaria and 25 having an infection caused by other bacteria/pathogens (Supplementary file 2) (von Kalckreuth et al., 2016; Marks et al., 2017). Chromatograms and mass spectra of the Bangladeshi plasma samples were generated and analysed as previously described by blinded operator in a random order using comprehensive two-dimensional gas chromatography with time-of-Flight Mass Spectrometry (GCxGC-TOFMS) (Näsström et al., 2014). Chromatograms and mass spectra of urine samples were generated using high-throughput ultra-performance liquid chromatography/quadrupole-time-of-flight mass spectrometry (UPLC-Q-TOFMS). Chromatograms and mass spectra of the Bangladeshi/Senegalese validation plasma samples were generated using one-dimensional gas chromatography with time-of-flight mass spectrometry (GC-TOFMS). Acquired and processed data was analyzed using chemometrics based pattern recognition. All methods are described in detail in Supplementary file 3.
