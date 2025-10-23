# Peer review - Round 1

Editors:
- YM Dennis Lo, https://ror.org/02zhqgq86 The Chinese University of Hong Kong Hong Kong

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75181.sa0](https://doi.org/10.7554/eLife.75181.sa0)

This study provides an interesting clinical relevance of human and microbe cell free RNAs derived from plasma that can be used as biomarkers for cancer detection and cancer type classification, and thereby having potential in clinical application.


---

# Peer review - Round 1

Editors:
- YM Dennis Lo, https://ror.org/02zhqgq86 The Chinese University of Hong Kong Hong Kong

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75181.sa1](https://doi.org/10.7554/eLife.75181.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Cancer Type Classification Using Plasma Cell Free RNAs Derived from Human and Microbes" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by YM Dennis Lo as the Senior Editor and Reviewing Editor. The following individual involved in review of your submission has agreed to reveal their identity: Cuncong Zhong (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. There have been many genome-wide association studies published in the field for cancer detection and cancer type classification using other technical strategies. What are the main advantages of using cfRNAs as biomarkers to distinguish cancer patients versus healthy donors, comparing with, for example, regular RNA-seq? There are already panels of genes that can be used as biomarkers for cancer patient detection and cancer type classification, based on their expression or other chemical modifications.

2. One of the main challenges in cancer detection is the ability of a technique to identify (or predict) patients at an early stage. The authors profiled samples from a cohort of ~300 patients. What percentage of the patients are at the early stage of the disease, i.e. stage I or II? What is the performance of using the featured cfRNAs as biomarkers to identify cancer patients at early stage? The author should also provide detailed clinical information of the cohort used as a supplementary.

3. In Figure 4, the authors identified cfRNAs in plasma which can be used as "biomarkers" to classify different cancer types, however most of them are circular RNAs. How about the expression of these "biomarkers" in the primary cells from the corresponding tumor types?

4. Microbial contaminations may be introduced during sample preparation. How could one be sure that the microbes detected from this study are actually from patients rather than experimental contaminations?

5. In Figure 5, the authors tried to build a predictive model of cancer detection based on cfRNAs, however, the performance of the predictive model seems very unstable, according to the AUROC, which varies from 0.4-1.0. This result greatly reduces the reliability of the machine learning model. Could they author explain why?

6. The panel of cfRNAs (both human and microbes) itself is more valuable in clinical application than the performance score of the model, if the performance is indeed as good as the authors claimed. Therefore, it will be good if the authors can present this result in more detail.

7. The language of the manuscript can be further improved. The word "some" is overused in many places, which is not scientific.

8. The authors need to redo the classification analysis with bootstrapping.

9. The authors need to correct their errors relating to "validation" and "test" datasets.

10. The authors need to add the patient inclusion criteria.

Reviewer #1 (Recommendations for the authors):

Chen et. al studied the use of cfRNA data for the diagnosis of five types of cancer. The authors claim that cfRNA reads from both human and microbial sources can both contribute to the cancer diagnosis. Overall, I find the hypothesis and design of the experiment reasonable. If successful, the results of this work can be used to detect major cancer types in early stages, significantly improving the survival rate of the cancer patients.

The authors need to redo the classification analysis with boosting.

The authors need to correct their errors relating to "validation" and "test" datasets.

The authors need to add the patient inclusion criteria.

Reviewer #2 (Recommendations for the authors):

In this manuscript, Chen et al. presents clinical relevance of human and microbe cfRNAs derived from plasma, which can be used as biomarkers for cancer detection and cancer type classification. The authors profiled cfRNAs in a cohort of ~300 plasma samples of five cancer types (colorectal cancer, stomach cancer, liver cancer, lung cancer, esophageal cancer) and healthy donors with RNA-seq. They claimed a prediction rate over 0.9 for distinguishing cancer patients from healthy donors and an improvements of predictive power in cancer type classification by combining human and microbial features together. Overall, I found this study interesting and potentials in clinical application. The experiment is well designed and data properly analyzed. The presented results also support the conclusions. The motivation and potential impacts of the this study would need to be further addressed the Introduction and Discussion sections.

My main concerns are as follows:

1. There have been many genome-wide association studies published in the field for cancer detection and cancer type classification using other technical strategies. What are the main advantages of using cfRNAs as biomarkers to distinguish cancer patients versus healthy donors, comparing with, for example, regular RNA-seq? I believe there are panels of regular genes that can be used as biomarkers for cancer patient detection and cancer type classification, based on their expression or other chemical modifications.

2. One of the main challenges in cancer detection is the ability of a technique to identify (or predict) patients at an early stage. The authors profiled samples from a cohort of ~300 patients, and I am wondering what percentage of the patients are at the early stage of the disease, i.e. stage I or II? What is the performance of using the featured cfRNAs as biomarkers to identify cancer patients at early stage? The author should also provide detailed clinical information of the cohort used as a supplementary.

3. In Figure 4, the authors identified cfRNAs in plasma which can be used as "biomarkers" to classify different cancer types, however most of them are circular RNAs. How about the expression of these "biomarkers" in the primary cells from the corresponding tumor types?

4. Microbial contaminations may be introduced during sample preparation. I am not convinced whether the microbes detected from this study are actually from patients rather than experimental contaminations.

5. In Figure 5, the authors tried to build a predictive model of cancer detection based on cfRNAs, however, the performance of the predictive model seems very unstable, according to the AUROC, which varies from 0.4-1.0. This result greatly reduces the reliability of the machine learning model. Could they author explain why?

6. The panel of cfRNAs (both human and microbes) itself is more valuable in clinical application than the performance score of the model, if the performance is indeed as good as the authors claimed. Therefore, it will be good if the authors can present this result in more detail.

7. The language of the manuscript can be further improved. The word "some" is overused in many places, which is not scientific.
