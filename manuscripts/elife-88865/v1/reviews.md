# Peer review - Round 1

Editors:
- David J Paterson, University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.88865.3.sa0](https://doi.org/10.7554/eLife.88865.3.sa0)

This important study brings together a clear application of the digital twin approach to make predictions using patient specific models with different genotypes. The data are compelling and go beyond the current state-of-the-art to support proof-of-principle evidence. Given the low subject numbers, further studies will be required going forward to support the veracity of the data and its translational utility.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88865.3.sa1](https://doi.org/10.7554/eLife.88865.3.sa1)

The authors have employed a digital twin approach to show that depending on the underlying disease mechanism, a digital replica constructed from human data can both recapitulate clinical findings, but also provide important insights into the fundamental disease state by revealing underlying contributing mechanisms. Moreover, the authors are able to show that a disease state caused by two different underlying genetic anomalies exhibit different electrical and morphological profiles.

This is important information as it allows for potential stratification of treatment approaches in future cases based on underlying phenotype by linking it to specific genotype properties. One of the most innovative aspects of the study is the mismatch switching between personalized structure, remodeling and genotype specific electrophysiological properties. The approach is elegant and allows for further exposure of the key mechanisms that contribute to the development of ventricular tachycardia circuits. One addition that could add more insight is to predict the effect of structural remodeling alone well, considering only normal electrophysiological models. Another interesting approach would be a sensitivity analysis, to determine how sensitive the VT circuits are to the specific geometry of the patient and remodeling that occurs during the disease, such an approach could also be used to determine how sensitive the outputs are to electrophysiological model inputs.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88865.3.sa2](https://doi.org/10.7554/eLife.88865.3.sa2)

The authors of this paper use a "digital twin" computational model of electrophysiology to investigate the pathology of Arrhythmogenic Right Ventricular Cardiomyopathy (ARVC) in several patients undergoing Electro-Physiological Studies (EPS) to treat Ventricular Tachycardias (VTs). The digital twin computational models are customised to the individual patient in two ways. Firstly, information on the patient's heart geometry and muscle/fibrous structure is extracted from Late Gadolium-Enhanced Magnetic Resonance Image (LGE-MRI) scans. Secondly, information from the patient's genotype is used to decide the particular electrophysiological cell model to use in the computational model. The two patient genotypes investigated include a Gene Ellusive (GE) group characterised by abnormal fibrous but normal cell electrical physiology and a palakophilin-2 (PKP2) group in which patients have abnormal fibrotic remodelling and distorted electrical conduction. The computational model predicts the locations and pathways of re-entrant circuits that cause VT. The model results are compared to previous recordings of induced VTs obtained from EPS studies.

The paper is very well written, and the modelling study is well thought out and thorough and represents an exemplar in the field. The major strengths of the paper are the use of a personalised patient model (geometry, fibrous structure and genotype) in a clinically relevant setting. Such a comprehensive personal model puts this paper at the forefront of such models in the field. The main weaknesses of the paper are more of a reflection on what is required for creating such models than on the study itself. As the authors acknowledge, the number of patients in each group is small. Additional patients would allow for statistical significance to be investigated.

The paper's authors set out to demonstrate the use of a "digital twin" computational model in the clinical setting of ARVC. The main findings of the paper were threefold. Firstly, the locations of VTs could be accurately predicted. There was a difference in the abnormal fibrous structure between the two genotype groups. Finally, there was an interplay between the fibrous structure of the heart and the cellular electrophysiology in that the fibrous remodelling was responsible for VTs in the GE group, but in the PKP2 group VTs were caused by slowed electrical conduction and altered restitution. The study successfully met the aims of the paper.

The major impact of the paper will be in demonstrating that a personalised computational model can (a) be developed from available measurements (albeit at the high end of what would normally be measured clinically) and (b) generate accurate results that may prove helpful in a clinical setting. Another impact is the finding in the paper that the cause of VTs may be different for the two genotypes investigated. The different interplay between fibrous and electrophysiology suggested by the modelling results may provide insights into different treatments for the different genotypes of the pathology. The authors use open-source software and have deposited all non-confidential data in publically available repositories.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88865.3.sa3](https://doi.org/10.7554/eLife.88865.3.sa3)

Overview

The authors propose a personalized ventricular computational model (Geno-DT) that incorporates the patient's structural remodeling (fibrosis and scar locations based on LGE-CMR scans) as well as genotyping (cell membrane kinetics based on genetic testing results) to predict VT locations and morphologies in ARVC setting.

To test the model, the authors conducted a retrospective study using 16 ARVC patient data with two genotypes (PKP2, GE) and reported high degree of sensitivity, specificity, and accuracy. In addition, the authors determined that in GE patients, VT was driven by fibrotic remodeling, whereas, in PKP2 patients, VT was associated with a combination of structural and electrical remodeling (slowed conduction and altered restitution).

Based on the findings, the authors recommend using Geno-DT approach to augment therapeutic accuracy in treatment of ARVC patients.

Critiques

1. The small sample size is a limitation but has already been acknowledge and documented by the authors.

2. Another limitation is the consideration of only two of the possible genotypes in developing the cell membrane kinetics, but again has acknowledged by the authors.

Final Thoughts

The authors have done a commendable job in targeting a disease phenotype that is relatively rare, which constrains the type of data that can be collected for research. Their personalized computational model approach makes a valuable contribution in furthering our understanding of ARVC mechanisms.
