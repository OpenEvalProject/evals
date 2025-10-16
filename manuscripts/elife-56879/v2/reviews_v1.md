# Peer review - Round 1

Editors:
- C Daniela Robles-Espinoza, International Laboratory for Human Genome Research Mexico

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.56879.sa1](https://doi.org/10.7554/eLife.56879.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

With larger datasets of single-cell data being made available, there is need in the field for analysis pipelines that can couple these experiments to clinical outcome and other variables in an unsupervised manner, and that can provide functional hypotheses that can be later tested in other cohorts in a simplified manner. Here, the authors have built RAPID, an algorithm that can take single-cell cytometry data as input and have extensively tested it in two cancer datasets, identifying populations of risk-stratifying cells. We envision that in years to come, RAPID will be able to identify markers correlated with important clinical characteristics, and that the functional relationships it finds and are confirmed will be useful for clinical practice.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "High risk glioblastoma cells revealed by machine learning and single cell signaling profiles" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

The reviewers, whose assessments are included below, agreed that RAPID is potentially interesting and useful to the scientific community but the lack of access to the code to test it prevents further assessment. In discussion, they agreed it is necessary for code and data to be accessible before publication for reviewers' perusal. Additionally, they considered the claim that biological findings "could be immediately used to guide clinical design" misguided, as an extensive comparison with existing literature has not been undertaken and extrapolates from results in a very small number of patients. Another suggestion for improving the work include analysing a larger validation cohort to establish the performance of RAPID in different datasets and under different conditions.

Reviewer #1:

In this work, Leelatian and collaborators study a set of 28 resected glioblastoma tissues from as many patients through single-cell technologies assessing 34 phospho-proteins, transcription factors and lineage proteins. They develop 2 technologies: 1) a set of 34 antibodies for single cell mass cytometry and 2) an unsupervised machine learning algorithm called RAPID – which is able to identify phenotypically similar cells ("clusters") and their association to survival variables.

I think the scale of the work is impressive (the study analyses >2 million cells) and the methodology seems very useful. However, there are a few issues that I think would need to be addressed before this manuscript is published.

1) I believe the software to be the main contribution of this manuscript, as the two proteins discovered at the end of the single-cell RAPID analysis have been studied in the context of glioblastoma/glioma and survival before (more of this below, but e.g., PMIDs 9445288, 28693199, 28885661, 27401156, 23719262). The data needs to be made publicly available, the same as the software. It says in the manuscript that it will be done so upon publication, but it absolutely needs to be released by the time the manuscript is published. At the moment it is impossible for me to assess whether RAPID may be easy to use, what variables it needs as input, and how easy it may be to install. Also, I do not know if the authors plan to release a detailed user manual, something that would be essential for publishing a piece of software.

2) I believe that the validation of the software needs to be done on more than one existing single-cell dataset, if possible. The fact that running different iterations of RAPID resulted in highly variable results in the same dataset (18 to 48 clusters identified), and that only one cluster overlapped in the OS vs PFS analyses calls, in my opinion, for more extensive testing. It's interesting that only 7 out of the 43 clusters identified when all cells were put together were considered "universal". Does this mean that this technique is highly susceptible to the number of tumours tested? Hopefully the software is easy to run and answers to these questions can be achieved relatively easily.

3) How do the authors reconcile their results with the observations by other studies that EGFR overexpression is associated with poor prognosis glioblastoma, seemingly contrary to the results in this study? (e.g. PMIDs 29445288, 28693199, 28885661). Linked to this point, I believe that the results are overhyped at times. For example, the phrase "These findings could be used immediately to guide clinical trial design" should be either removed or rewritten in a more measured way. Which population did the authors study, only European-descent (i.e. white) patients? Also, the number of samples is quite small for such a claim. Generalising in this way would be hurtful to global clinical practice.

4) About the classification of tumours into high/low for distinct markers. Two tumours may be highly similar and classified in different groups (in the example given in the text, tumours with 2.68% of cells in the cluster were classified as “low” but those with 2.7% as “high”). Would the conclusions be maintained if the high group was defined as those above the 75th percentile and the low group below the 25th percentile? How important is this definition to the results of the RAPID workflow?

Reviewer #2:

This is a potentially interesting manuscript that seeks to profile glioblastoma samples by mass cytometry to assess intra-tumoral heterogeneity at the protein level. The authors profile a large number of cells in 28 samples using 34 markers (retaining 26 markers in final set). They then use this information (with various filtering steps) to identify modules of variability within tumors and then use some of those modules/signatures to stratify patients’ outcome with a machine learning approach. They suggest that their findings can be "immediately" used to inform clinical trial design.

The study suffers from intrinsic limitations that are hard to overcome and that would be acceptable if the authors had not jumped to conclusions, they do not have the power to support. First, the analysis relies on 26 measured proteins, which is a rather limited set of parameters; any analysis that relies on protein measurement is also only as good as the antibody used and one should keep in mind that some of the clusters inferred might be technical; hence any major statement would require some form of validation by other approaches which is mostly lacking in this manuscript. But all that would be addressable/ok, if the authors had been more reasonable in their conclusions.

By far the main limitation and major caveat this reviewer sees is that the authors draw major conclusions on stratifying GBM patients for their outcome based on a cohort of 28 patients. This is massively underpowered to address patient stratification. The markers they home on are nothing very new (EGFR, SOX2, S100 etc) that have been interrogated in much larger cohorts (TCGA has >400 samples) and have not yielded as valuable information as claimed by the authors.

This study would only be useful if the 28 samples were a discovery cohort and their findings were validated in hundreds of patients’ samples. If EGFR was that good at predicting outcome of GBM, we would know by now. So unfortunately, underpowered study for the claims on outcome. The mass cytometry profile/data would be of interest if followed-up, but not for survival analysis given limited dataset.

Reviewer #3:

Leelatian, Sinnaeve et al. describes a single-cell mass cytometry data-set measuring 34 proteins and phospho-proteins across 28 glioblastoma patients. This represents a rich data-set which the authors take advantage to develop a novel computational tool, RAPID, to identify cell type clusters that inform on patient survival. This approach identified 9 cell clusters that stratified patients according to their overall survival, and these can be classified into negative and positive prognostic using S100B and EGFR protein abundance.

Although further work would be required to confirm the robustness and utility of these findings to the clinic, this study presents novel insights, tools and data-sets that will be of interest to the scientific community.

1) The separation and classification of the 43 cell clusters (Figure 1B) is not very clear. Consistently, these varied extensively across the 10 down-sample analyses with 18-48 optimal clusters. Have the authors tried multiple configurations of the tSNE parameters (e.g. perplexity, learning rate)? Clustering could also be compared to current state-of-the-art pipelines (PMID: 31217225), for example running Principal Component Analysis (PCA) as a pre-processing step before the non-linear tSNE.

2) Several clusters of glioblastoma cell types exist (Figure 2A), in particular a subset (lower left) seems to have a heterogeneous expression of Nestin and strong phosphorylation of AKT. Is this a common observation across other patient samples? If so, what is the percentage of cells this represents and could there be an impact on the analysis if this population, like the other cell types, were removed? Additionally, p-AKT is enriched in GNP cluster 37 and GPP cluster 41. Specifically, GPP cluster 41 is the only cluster enriched in 2 patients (LC03 and LC09) which are classified as GNP. To me this is counterintuitive, and might indicate some unique variation, either true biological or artefact, of this cell type.

3) The potential translation into the clinic seems to be one of the main messages of the manuscript and is indeed particularly interesting. Specifically, the fact that only S100B and EGFR expression is enough to stratify patient overall survival. Could the observations gained from the single-cell experiments be used to re-analyse bulk patient genomic and proteomic data-sets to support further the clinical relevance of these findings? For example, what is the percentage of glioblastoma IDH1 wild type patients with S100B and EGFR high or low?

4) The availability of RAPID as a tool to the community is important and a positive aspect of this work. Thus, I believe the source should have been made accessible prior to publication.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Unsupervised machine learning reveals risk stratifying glioblastoma tumor cells" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Philip Cole as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Julie Laffy (Reviewer #4).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus, the revisions requested below only address clarity and presentation.

Summary:

In this revised manuscript, Leelatian, Sinnaeve and collaborators introduce the RAPID algorithm for identifying clusters of cells relevant for stratification of patient survival in single-cell datasets, especially mass cytometry datasets including more than 25 patients. In this new version, they have tested RAPID with two datasets from different cancer types, one generated by them and another one already published, and have performed extensive statistical validation both technical and biological.

Revisions:

Please address the following points raised by the reviewers:

1) Clustering is performed across all tumours combined, so the authors should distinguish inter-tumour effects from the intra-tumour effects that they describe. Could they show for example that the cluster phenotypes are derivable from a significant number of individual tumours? Inter-tumour effects would imply some different conclusions to the ones the authors draw, depending on the patient specificities of these effects. Assuming no patient specificity, one potentially interesting and even complementary conclusion would be that basal levels of certain proteins in a tumour are indicative of patient outcome (indiscriminately of any particular cellular subpopulation). Do the authors see that EGFR, S100B and other enriched proteins vary primarily within, or between, tumours? To check for patient specificity, the authors should state in the text i) which, if any, clusters were largely tumour-specific and ii) how many tumours contributed to each of the clusters. Without these figures, the biological relevance of each of the clusters (namely the NP and PP subsets) is difficult to assess. It might also be useful to add tSNE plots coloured by patient alongside the existing plots (Figures 1B, 2A, 4A). If there are indeed clusters dominated by individual tumours, I would think that they should be removed early on in the RAPID pipeline. If there are many such cases, then perhaps the authors would have to consider an alternative clustering approach.

2) Do any of the cell subsets identified (Figure 1B, C) reflect a proneural population? This is a known component of glioblastomas and has moreover been postulated to be associated with better prognosis because it is the dominant component in lower-grade gliomas (e.g. Verhaak et al., 2010). How do the authors reconcile this with their own findings? Or, if a proneural phenotype is lacking, could the authors comment on why that might be? One reason could be technical: simply that proneural markers were not sufficiently represented in the panel. If that is the case, the authors should acknowledge this in the text and take care not to overstate their results pertaining to the phenotypes of NP and PP subsets in GBM.
