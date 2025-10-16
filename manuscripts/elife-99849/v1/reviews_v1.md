# Peer review - Round 1

Editors:
- Rachel Evans, https://ror.org/0220mzb33 King's College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.99849.3.sa0](https://doi.org/10.7554/eLife.99849.3.sa0)

The authors have developed a robust machine learning approach to predict radio sensitivity in patients with NPC based on a defined gene signature. Some key aspects of this signature have been validated in vitro using relevant cell lines which strengthens the conclusions of this important and convincing study. The publication will be of interest to clinicians working on this indication as well as a more broader readership made up of scientists working on radiation biology and those with a bioinformatics/machine learning background.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.99849.3.sa1](https://doi.org/10.7554/eLife.99849.3.sa1)

Summary:

In this study, the authors developed a novel radiotherapy sensitivity score (NPC-RSS) for nasopharyngeal carcinoma patients using machine learning algorithms. They identified 18 key genes associated with radiosensitivity and demonstrated that NPC-RSS could effectively predict radiotherapy response in both public and in-house datasets. Furthermore, they found that the key genes of NPC-RSS were closely related to immune characteristics, the expression of radiosensitivity-related genes, and signaling pathways involved in disease progression. The authors validated the consistency of expression of two key genes, SMARCA2 and CD9, with NPC-RSS in their own cell lines. They also showed that the radiosensitive group, classified by NPC-RSS, exhibited a more enriched and activated state of immune infiltration compared to the radioresistant group.

Strengths:

(1) The study employed a comprehensive approach by integrating multiple machine learning algorithms to develop a robust predictive model for radiotherapy sensitivity in nasopharyngeal carcinoma patients.

(2) The predictive performance of NPC-RSS was validated using both public and in-house datasets, demonstrating its potential clinical applicability.

(3) The authors conducted extensive analyses to investigate the biological mechanisms underlying the association between NPC-RSS and radiotherapy response, including immune characteristics, radiosensitivity-related gene expression, and relevant signaling pathways.

(4) The consistency of key gene expression with NPC-RSS was validated in the authors' own cell lines, providing additional experimental evidence.

Weaknesses:

(1) The sample size of the in-house dataset used for training the model was relatively small (34 patients), which might limit the generalizability of the findings.

(2) The authors did not perform functional experiments to directly validate the roles of the identified key genes in radiotherapy sensitivity, relying instead on associations with immune features and signaling pathways.

(3) The study did not discuss the potential limitations of using machine learning algorithms, such as the risk of overfitting and the need for larger, diverse datasets for more robust model development and validation.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.99849.3.sa2](https://doi.org/10.7554/eLife.99849.3.sa2)

Summary:

This article utilizes machine learning methods and transcriptomic data from nasopharyngeal carcinoma (NPC) patients to construct a biomarker called NPC-RSS that can predict the radiosensitivity of NPC patients. The authors further explore the biological mechanisms underlying the relationship between NPC-RSS and radiotherapy response in NPC patients. The main objective of this study is to guide the selection of radiotherapy strategies for NPC patients, thereby improving their clinical outcomes and prognosis.

Strengths:

(1) The combination of multiple machine learning algorithms and cross-validation was used to select the best predictive model for radiotherapy sensitivity from 71 differentially expressed genes, enhancing the robustness and reliability of the predictions.

(2) Functional enrichment analysis revealed close associations between NPC-RSS key genes and immune characteristics, expression of radiotherapy sensitivity-related genes, and signaling pathways related to disease progression, providing a biological basis for NPC-RSS in predicting radiotherapy sensitivity.

(3) Grouping NPC samples according to NPC-RSS showed that the radiotherapy-sensitive group exhibited a more enriched and activated state of immune infiltration compared to the radioresistant group. In single-cell samples, NPC-RSS was higher in the radiotherapy-sensitive group, with immune cells playing a dominant role. These results clarify the mechanism of NPC-RSS in predicting radiotherapy sensitivity from an immunological perspective.

(4) The study used public datasets and in-house cohort data for validation, confirming the good predictive performance of NPC-RSS and increasing the credibility of the results.

Limitation:

(1) The study focuses on a specific type of nasopharyngeal carcinoma (NPC) and may not be generalizable to other subtypes or related head and neck cancers. The applicability of NPC-RSS to a broader range of patients and tumor types remains to be determined.

(2) The study does not account for potential differences in radiotherapy protocols, doses, and techniques between the training and validation cohorts, which could influence the performance of the predictive model. Standardization of treatment parameters would be important for future validation studies.

(3) The binary classification of patients into radiotherapy-sensitive and resistant groups may oversimplify the complex spectrum of treatment responses. A more granular stratification system that captures intermediate responses could provide more nuanced predictions and better guide personalized treatment decisions.

(4) The study does not address the potential impact of other relevant factors, such as tumor stage, histological subtype, and concurrent chemotherapy, on the predictive performance of NPC-RSS. Incorporating these clinical variables into the model could enhance its accuracy and clinical utility.
