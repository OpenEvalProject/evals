# Peer review - Round 1

Editors:
- Tony Ng, https://ror.org/0220mzb33 King's College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80150.sa0](https://doi.org/10.7554/eLife.80150.sa0)

This work sets out to develop a better machine learning-based predictor of survival/prognosis for patients diagnosed with pancreatic cancer. To achieve this, the authors developed a large combinatorial family of machine learning methods based on a high-dimensional set of -omics and other patient data features; using ten publicly available data sets. By finding the combined ML method(s) that performed best on the task, the authors were able to identify a reduced set of features (giving rise to a signature called AIDPS that involves 9 genes) which, when measured in the patient, allow for fairly accurate prediction of patient survival and prognosis. Importantly, three new external data sets GSE21501, GSE57495, GSE71729 were used in the validation.


---

# Peer review - Round 1

Editors:
- Tony Ng, https://ror.org/0220mzb33 King's College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80150.sa1](https://doi.org/10.7554/eLife.80150.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Comprehensive machine-learning survival framework develop a consensus model in large scale multi-center cohorts for pancreatic cancer" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Caigang Liu as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Anthony C C Coolen (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. The authors should repeat their complete pipeline after randomizing within each of their ten data sets the clinical outcomes (i.e. shuffle the time-to-event outcomes). If one would obtain again a signature with comparable prognostic features, then one can be sure that what is reported here is largely a manifestation of overfitting due to dimension mismatch, and hence of no interest.

2. The authors should provide a better understanding of why agreement/optimization amongst a large number of combined ML methods was chosen as a way to drive feature selection. Comparing to existing methods is one thing, currently, there isn't really a clear comparison here to other feature selection approaches.

3. The authors should provide a thorough explanation of the biological relevance of the 9 genes in relation to the mutational load/copy number changes/ immunological infiltration found in low AIDPS patients.

Reviewer #1 (Recommendations for the authors):

Things I think would strengthen the paper:

1. A better understanding of why agreement/optimization amongst a large number of combined ML methods was chosen as a way to drive feature selection. Comparing to existing methods is one thing, but there isn't really a clear comparison here to other feature selection approaches, nor much discussion of why this one was chosen. Is this meant to be a reproducible approach, for other problems, or is the point just to get the AIDPS features? Why is this approach to feature selection preferred/superior.

2. Right now the current pipeline seems highly unwieldy because of all the models considered. Is this meant to be a general and reproducible approach? if so, the authors need to demonstrate more clearly that this same approach can be done by others with ease.

3. Everything in the subsequent analyses comparing high and low AIDPS groups hinges on the assumed accuracy and generality of the model. Once you have 9 genes, though, you should be able to study those features using a range of methods, some of which are picked to have high interpretability. I am sorry if I missed this, but at the moment it is not clear to me what best an ML method can do is using the 9 genes, and whether there is an interpretable method that works well but might imply a non-trivial relationship amongst the genes that matters to the outcome. This seems more informative than studying the statistics of high and low AIDPS groups

Reviewer #2 (Recommendations for the authors):

To rescue their claims one could suggest to the authors the following simple but clean and fair test. The authors could repeat their complete pipeline after randomizing within each of their ten data sets the clinical outcomes (i.e. shuffle the time-to-event outcomes). If that exercise is found to make the signal disappear (i.e. the separation of KM curves, and the nontrivial AUROC values), then their present results should be studied further as possibly relevant. If, on the contrary, one would obtain again a signature with comparable prognostic features, then one can be sure that what is reported here is largely a manifestation of overfitting due to dimension mismatch, and hence of no interest.

Reviewer #3 (Recommendation for the authors):

From the biological point of view, currently, there was little explanation of the biological relevance of the 9 genes in relation to the mutational load/copy number changes/ immunological infiltration found in low AIDPS patients. Please discuss these in sufficient detail.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Comprehensive machine-learning survival framework develop a consensus model in large scale multi-center cohorts for pancreatic cancer" for further consideration by eLife. Your revised article has been evaluated by Caigang Liu (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

1. The improvements to figure 7 (in the supplementary figures linked to Figure 7) meant to address Reviewer #1's request seem to all focus on treating the aidps features separately. Please show the accuracy when these aidps features are considered together as a nine dimensional feature vector in one model.

2. For reviewer #2, please remove the newly added material called `performance of AIDPS in randomly split cohorts', as this adds nothing relevant (as it s again testing on discovery data). Please take out all mentioning of `validation' or `validated' from the manuscript, other than when discussing the tests on the three new data sets GSE21501, GSE57495, GSE71729; only the latter can be called validation sets. Please compare the performance of existing signatures to that of the authors' own signature on the three new data sets GSE21501, GSE57495, GSE71729.

The main reason for this suggestion is that the revised manuscript still tests their own signature on discovery data but that of the competitors on unseen data, which is not a fair comparison. Unless the authors remedy this they should (i) remove all mentioning of superior performance of their signature (since the comparison did not involve a level paying field) and (ii) remove all mentioning of `validation' other than in relation to the three new data sets.

3. Please include (4. Current research progress on these nine AIDPS genes) in the rebuttal, which is a summary of what is known about the biological function of the nine genes, as an Appendix or Supplementary information in the manuscript.

Reviewer #1 (Recommendations for the authors):

The authors have largely addressed the concerns raised in my previous review. As best I can tell, they have not yet shown how a simple ML model (such as linear regression or xgboost) performs on the same task when only fed with the 9 aidps features simultaneously. The improvements to figure 7 meant to address my request seem to all focus on treating the aidps features separately, so it useful to know they perform poorly when separate… what about when they are considered together as a nine dimensional feature vector in one model?

Reviewer #2 (Recommendations for the authors):

In my first report I put forward two points. First, that the authors used the same data sets both in the discovery stage and the validation stage. Second, that they compared the performance of competitor signatures to theirs by using these same data. This has the following consequences: 1. They could not claim that their signature had been validated, because what they called validation data were in fact the discovery data (the potential impact of overfitting is hence unclear). 2. The comparison between their signature and the existing ones was not fair (their own signature was tested on its corresponding discovery data, but the competitors' signatures on what for those signatures would be independent validation data). Therefore, all claims on their signature having been validated and on it being superior to existing signatures were not supported by the available evidence. I also suggested that they could test for overfitting impact by repeating their previous analyses step by step with outcome-randomized versions of the original data. This should make all true signals disappear and is hence a clean and fair test.

In the revised version of their manuscript the authors did not carry out the requested re-analysis with outcome-randomized data. Instead they (a) sampled several new data sets from their original data (without outcome randomization), and (b) tested their signature on three independent new data sets. Exercise (a) seems pointless; of course the signature would again be able to predict, since one is testing it once more on samples from the discovery set. Exercise (b), although not what was requested by this referee, is more useful. Here the authors report again significant performance of their signature, with AUC values in the range 0.68-0.70, lending weight to the suggestion that their signature makes sense.

I conclude from the authors' reply and from the new version of the paper that point 1. above has been partly addressed, but not point 2. If the authors, as it seems, do not wish to carry out the requested analysis with outcome randomization, then they have the following options:

Option A;

– Remove the newly added material called `performance of AIDPS in randomly split cohorts', this adds nothing relevant (see my notes above, it is again testing performance on discovery data).

– Take out all mentioning of `validation' or `validated' from the manuscript, other than when discussing the tests on the three new data sets GSE21501, GSE57495, GSE71729; only the latter can be called validation sets.

– Remove all performance comparisons between the new signature and the existing ones (since this comparison is presently not fair) and all conclusions based on these comparisons.

Option B:

– Remove the newly added material called `performance of AIDPS in randomly split cohorts', this adds nothing relevant (see my notes above, it is again testing on discovery data).

– Take out all mentioning of `validation' or `validated' from the manuscript, other than when discussing the tests on the three new data sets GSE21501, GSE57495, GSE71729; only the latter can be called validation sets.

– Compare the performance of existing signatures to that of their own signature on the three new data sets GSE21501, GSE57495, GSE71729; this comparison would be fair.

I would personally strongly suggest option B, since otherwise the paper would in my view be too weak in terms of the amount of justified conclusions to warrant publication (but that is a decision for the editor to make). In addition, I would still hope that the authors choose to comply with my original request for application of the full pipeline to outcome-randomized discovery data. This would clarify objectively, for the authors' own benefit, the extent to which their original tests and conclusions may have been affected by overfitting.

Reviewer #3 (Recommendations for the authors):

The authors have addressed my comments. I find the following v useful as a summary of what is known about the biological function of the nine genes and wonder if it can be incorporated as an Appendix or Supplementary information:

"The nine AIDPS genes were rarely studied in tumors, most of which focused on their roles in biological phenotypes such as tumorigenesis and progression, and few studies investigated their roles and guiding significance in PACA immune microenvironment and treatment. Specifically, we found that SELENBP1 owned lower expression in the low AIDPS group with poor prognosis was associated with better tumor prognosis, and its decreased expression resulted in poor prognosis of many tumors such as lung adenocarcinoma. Meanwhile, DCBLD2, PRR11, EREG, ADM and TGM2, which were overexpressed in the low AIDPS group, played an essential role in the proliferation, invasion and metastasis of many tumors such as PACA, hepatocellular carcinoma and colorectal cancer, and lead to their chemotherapy resistance and were potential targets for enhanced efficacy. However, the functional roles and mechanisms of UNC13D and CDCA4 in tumors are not well understood, and more high-quality studies are needed in the future. These findings are consistent with our study, and the specific functional characteristics are summarized as follows:

1. SELENBP1, encoding a novel human methanethiol oxidase, whose expression is significantly decreased in the progression of Barrett's esophagus to adenocarcinoma and can affect chemotherapy sensitivity (PMID: 20332323). This is consistent with our results that SELENBP1 expression was decreased in the low AIDPS group with worse prognosis (Figure 7—figure supplement 3).

2. PLCB4 encodes a phospholipase, and activating PLCB4 mutation was recently identified in primary leptomeningeal melanocytic tumors (PMID: 28499758).

3. DCBLD2 is upregulated in glioblastoma and head and neck cancer, and phosphorylation of DCBLD2 Y750 activates AKT pathway which in turn enhances EGFR-driven tumorigenesis (PMID: 25061874). DCBLD2 has also been found to play a crucial role in the invasion, progression, and metastasis of neuroendocrine tumors (PMID: 18827820). These results are consistent with an increased expression of DCBLD2 in the low AIDPS group with a dismal prognosis.

4. Proline-rich protein 11 (PRR11) is a novel tumor-related gene, which has been found can promote breast cancer growth and anti-estrogen resistance through the PI3K pathway (PMID: 33127913). In addition, it has also been demonstrated that PRR11 affects autophagy and promotes proliferation in non-small cell lung cancer (NSCLC) through the Akt/mTOR pathway (PMID: 30258945; 35005120), and recent studies have also found that PRR11 can promote the tumorigenesis and progression of renal clear cell carcinoma (ccRCC) by regulating E2F1 stability (PMID: 34499617). Overall, these results are consistent with higher expression of PRR11 in the low AIDPS group with a worse prognosis.

5. UNC13D mutation play an essential role in familial hemophagocytic lymphohistiocytosis (FHL), but its role in tumors remains unknown and needs to be further explored (PMID: 21931115; 24842371; 25564401; 24882743).

6. EREG, as an EGFR ligand epithelial regulatory protein, plays a fundamental role in the growth and proliferation of breast and colorectal cancers (PMID: 26215578; 23549083) and is associated with tamoxifen resistance in breast cancer (PMID: 30967627) and efficacy of panitumumab and adjuvant chemotherapy in colorectal cancer (PMID: 26869404; 25272957).

7. Adrenomedullin (ADM) encodes a pre-prohormone that is cleaved into two bioactive peptides, which can dilate blood vessels, regulate hormone secretion, and promoting angiogenesis. Many studies have confirmed that ADM plays a major role in the proliferation, invasion, angiogenesis, and metastasis of PACA, hepatocellular carcinoma, prostate cancer, melanoma, ovarian cancer, and endometrial cancer and may become a novel therapeutic target (PMID: 22960655; 17363587; 18657357; 24100627; 21994414; 22400488; 11420706).

8. In addition, currently one of the few studies support the oncogenic role of cell division cycle associated protein 4 (CDCA4) in tumors and nuclear factors induced as E2F transcription factor families that regulate E2F-dependent transcriptional activation and cell proliferation, but their potential mechanism, especially effect on PACA tumorigenesis and progression require further investigation (PMID: 35251007; 16984923).

9. Transglutaminase 2 (TGM2), a promoter of stemness and radiotherapy resistance in glioma (PMID: 33483373), has been confirmed in many studies to promote colorectal cancer progression via P53 and Wnt/β-catenin signaling pathways (PMID: 34103685; 31570702), as well as is associated with tumor-promoting inflammation in gastric cancer (PMID: 32467608). These results are consistent with the TGM2 expression dramatically increased in the low AIDPS group with worse prognosis, suggesting that TGM2 may play an important role in the development and progression of PACA."
