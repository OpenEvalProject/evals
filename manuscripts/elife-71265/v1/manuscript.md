# Extent, impact, and mitigation of batch effects in tumor biomarker studies using tissue microarrays

## Authors

- Konrad H Stopsack<sup>1</sup> ([ORCID: 0000-0002-0722-1311](https://orcid.org/0000-0002-0722-1311)) †
- Svitlana Tyekucheva<sup>2</sup>
- Molin Wang<sup>1</sup>
- Travis A Gerke<sup>3</sup>
- J Bailey Vaselkiv<sup>1</sup> ([ORCID: 0000-0001-7702-9504](https://orcid.org/0000-0001-7702-9504))
- Kathryn L.# Penney<sup>1</sup>
- Philip W Kantoff<sup>4</sup>
- Stephen P Finn<sup>5</sup>
- Michelangelo Fiorentino<sup>6</sup>
- Massimo Loda<sup>7</sup>
- Tamara L Lotan<sup>8</sup>
- Giovanni Parmigiani<sup>2</sup>
- Lorelei A Mucci<sup>1</sup>

### Affiliations

1. Department of Epidemiology Harvard T.H. Chan School of Public Health Boston United States
2. Department of Data Science Dana-Farber Cancer Institute Boston United States
3. Department of Cancer Epidemiology Moffitt Cancer Center Tampa United States
4. Department of Medicine Memorial Sloan Kettering Cancer Center New York United States
5. Trinity College Dublin Ireland
6. Pathology Unit, Addarii Institute University of Bologna Bologna Italy
7. Department of Pathology Weill Cornell Medical Center New York United States
8. Department of Pathology Johns Hopkins University Baltimore United States

† Corresponding author

## Abstract

Tissue microarrays (TMAs) have been used in thousands of cancer biomarker studies. To what extent batch effects, measurement error in biomarker levels between slides, affects TMA-based studies has not been assessed systematically. We evaluated 20 protein biomarkers on 14 TMAs with prospectively collected tumor tissue from 1,448 primary prostate cancers. In half of the biomarkers, more than 10% of biomarker variance was attributable to between-TMA differences (range, 1-48%). We implemented different methods to mitigate batch effects (R package batchtma ), tested in plasmode simulation. Biomarker levels were more similar between mitigation approaches compared to uncorrected values. For some biomarkers, associations with clinical features changed substantially after addressing batch effects. Batch effects and resulting bias are not an error of an individual study but an inherent feature of TMA-based protein biomarker studies. They always need to be considered during study design and addressed analytically in studies using more than one TMA.
