# Peer review - Round 1

Editors:
- Alfonso Valencia, Barcelona Supercomputing Center - BSC Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.44941.sa1](https://doi.org/10.7554/eLife.44941.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The paper describes the stratification of a diabetes cohort based on characteristics extracted from the medical records of a rather homogenous population. These characteristics include other diagnoses and lifestyle factors. The clusters of patients, obtained with an unsupervised Markov clustering method, represent characteristic longitudinal glycemic dysregulation patterns that include the temporal order of comorbidities, as well as genetic features, i.e. SNPs close to some of the known diabetes related genes.

The work opens the doors to the study of the molecular basis of the classical etiological subtypes of diabetes at the light of their relations with the clusters based on comorbidity relationships and symptoms.

Decision letter after peer review:

Thank you for submitting your article "Linking glycemic dysregulation in diabetes to symptoms, comorbidities and genetics through EHR data mining" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The biomedical goal of the paper is to identify subgroups of diabetes patients. The study is based on a large set of medical records from patients with T1D or T2D. The methodology produces 6 large clusters (MCL) combining structure information (ICD-10 level 3 codes) and symptoms extracted from the free text. The analysis shows enrichment in clinically relevant groups and relations with other diseases. The paper includes the specific analysis of glycemic deregulation, its relation with comorbidities and with previously identified genes/SNPs.

Essential revisions:

The topic is relevant and timely. The technical contribution is at the leading front of the analysis of medical records analysing structured and free text information.

On the critical side there are limitations in clustering analysis, as well as in the use of limited ICD third level data. These serious criticisms have to be addressed completely in a revised version. There are also a number of other issues related with the origin of the data (temporal coverage of the cases) that need to be addressed in detail in the text.

Finally, it is not completely clear what are new results and what is validated (and how). Even, if these are common problems in many large scale studies, it is important to address them clearly in the paper. This point is related with the criticisms on the unclear goal of the paper: technical or medical? The comments of the reviewers reflect that given the situation, you will have to think if you want to prioritise the novelty of the approach instead of making medical claims that might be difficult to sustain.

We ask you to address the following;

More details on the key points above:

1) Circularity

The analysis strategy and reasoning appears to be circular and there are not provided measures of independence between codes, factors, elements, etc. that are introduced or measured at each step. In particular, there are used two vocabularies (which obviously expand the number of "codes" assigned to patients, as it should be; first section Results is not novel) that gave approximately 940,000 codes as explained in Materials and methods. However, it is expected that many of these codes are in fact correlated, non-independent, but instead they are all used to generate patient clusters; for example, in several instances it is emphasized that codes from primary diabetes diagnoses are not used in clustering/analyses, but it is well known a priori that many other codes are significantly correlated with the diagnoses (it is therefore not unexpected that patient clusters differentiate diabetes subtypes). Therefore, it would also not be unexpected that clusters differentiate glycemic levels. In fact, the 71 clusters are defined using distances from ICD-10 chapter XVIII symptoms (subsection “Enriched comorbidity and symptom patterns in diabetes patient clusters”, first paragraph), which includes examination of blood parameters. Again, latter the clusters are defined based on comorbidities, which presumably many are linked to the original codes. Another example of this point is the identification of a "schizophrenia" cluster (subsection “Glycemic dysregulation”, last paragraph), which is expected if the corresponding codes are included. I agree that an observation of differential glycemic levels in this clusters may be interesting, but then first it should be evaluated the overall correlation among the thousands of codes used in the study, and also then the study is limited to assess co-occurrences of terms/codes.

One possible way out could be the comparison results of structured vs. structured+unstructured features.

2) Clustering

As overall conclusion, Discussion section includes the statement that the results show "many different and homogenous groups of patients", but it has to be formally demonstrated that the groups are independent, that they are many more than randomly expected by permuting the same cohort, and that they are more homogenous that some value.

Additionally, questioning the clusters stability, would be necessary to provide a sensitivity analysis on the clusters to illustrate the stability.

3) ICD codes

Truncating the codes to three digits is akin to adding noise by losing information. Please justify your rationale behind truncating the codes. It'll be good if this issue could be addressed in the Discussion or one of the limitations of the work.

4) Data limitations and temporal series

First, there might be problems with the time-dependent comorbidities in a given cluster. There are multiple reasons: (1) the length of the observational window before and after considered in a given cluster is not talked about/defined. This can impact the enrichment of symptoms and hence all the downstream analysis; (2) length observational windows is bound to be different in different clusters, which may introduce the bias in computing comorbidities; (3) it is not clear from the analysis if there exist any relation between the observational window and cluster size.

Indeed, it is not clear how temporality is defined. The heatmap presented in Figure 2B does not help either. Specifically, what is the index date, relative to which pre and postcodes were identified? It is quite likely that the index date would vary for patients, therefore, how does that variability was accounted? Please explain this paragraph in more detail and if possible, then provide a schematic diagram representing temporality and how it was considered in this analysis. In addition, in the fourth paragraph of the subsection “Comorbidity pairs and patterns within symptom related clusters”, it appears the time window before and after is likely to bias the estimation of T2D and elevated blood glucose level. More clarity on this will be helpful.

In any case, a better explanation is needed about the length of the observational window before and after used to compute comorbidities. The length of the observational window (before and after in a given cluster) is bound to confound the disease association. Was this length kept similar for all the clusters? If not, then it is very much possible that certain cultures are (just based on cluster size) are likely to be enriched in certain symptoms. Please provide an in-depth analysis on this.

5) Additional data

Please briefly explain the type of genetic data is included and at what level of omics.

The candidate genetic and biochemical markers of glucose regulation could be of interest if replicated. However, could these have been discovered without the clustering e.g. using simpler regression methods?

It is unclear how the clusters segregate in their genetic basis, which could then support the identification of disease subtypes. The question is not as much which genetic variants are associated with a given cluster, but if the effect estimations are statistically different between clusters, which would then favor the existence of subtypes. It is also unclear if the association signals are genome-wide significant in any case.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Linking glycemic dysregulation in diabetes to symptoms, comorbidities and genetics through EHR data mining" for further consideration at eLife. Your revised article has been favorably evaluated by Naama Barkai as the Senior Editor, a Reviewing Editor, and two reviewers.

The manuscript has been improved but there is still some confusion about the significance of the resulting clusters, significance of the selected thresholds and the subsequent biological interpretation, as outlined below by the first reviewer. The final version should clarify the exploratory nature of the work and the limits of the statistical reliability, as pointed out by the second reviewer.

Reviewer #1:

The authors have done a perceptible effort trying to answer the major concerns initially raised, and I personally appreciate the clarifications and additional data provided.

However, I am still not convinced that the main results are robust enough to support the overall message, in particular regarding the title: "Linking glycemic dysregulation.…to symptoms, comorbidities and genetics…".

First, the issue of "circularity". I might have over-looked the original Discussion that mentioned that primary and secondary diabetes diagnoses were excluded, or my initial comment might have been unclear, but I was referring to the expectation that clusters should obviously identify major known diabetes types; in particular if dozens of diagnosis codes (some of them correlated) and extensive text vocabulary is analyzed. The point is not if the clusters identify what it is already known, but if they identify new etiology/subtypes. Of note, the following example is somewhat inaccurate: "… triple negative breast cancer patients share many features with ER-positive patients for example." Indeed TNBC and ER+ cases do not share cell-of-origin, prognosis, tissue-metastasis preference, neither therapeutic approaches.

My reasoning above is then linked to the title issue: the study of glycemic perturbation is presented in one section (“Glycemic dysregulation”) and remains unclear which clusters, symptoms, are robust regarding statistical differences for "glycemic perturbation" from the others. The thresholds of 0-2, 3-5 parameters, and then the clusters (21 with 50% patients 3 parameters…) appear to be arbitrary. The use of sentences with the following grammatical constructions may not help to understand the analyses: "distinct differentiation…dysregulation parameters". Next, glycemic perturbation is linked to genetic risk in the last Results section, but as initially raised, it is unclear what means "top association signals"; are these significant genome-wide, are they statistically different between the clusters/symptoms? Are cluster-risk interactions significant? Honestly, this remains unclear to me and I hope I am not overlooking to any data. I agree with the authors on their final response to the question of "circularity": 1) To which extent does it reproduce the classification made by doctors? 2) Does it allow us to make a more specific subgrouping of patients?

I believe that the lack of specific subgroups with statistically defined differences across the three features included in the title is evident from the Abstract, which does not detail any result: it just includes a general message of what the study has found as a last sentence.

Reviewer #2:

I am satisfied with the revision of the article. I feel that the questions I raised have been addressed. Limitation in the use of 3-digit ICD9 codes remains, but the response from authors and subsequent changes made in the manuscript are appropriate.

This study may serve as a starting point for more in-depth analysis in subsequent analysis.
