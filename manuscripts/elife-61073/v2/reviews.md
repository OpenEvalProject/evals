# Peer review - Round 1

Editors:
- Sara Hägg, Karolinska Institutet Sweden

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.61073.sa1](https://doi.org/10.7554/eLife.61073.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The work highlights the importance of proteomic biomarkers in aging and its association across other data types.

Decision letter after peer review:

Thank you for submitting your article "Plasma proteomic biomarker signature of age predicts health and life span" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Anna Akhmanova as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional analyses are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

This is a well-written article that analyzes a proteomics data set of a large number of individuals and conduct several analyses to identify protein biomarkers of aging, mortality and aging related diseases. They also integrate the result with genetic and other data. The work adds to the growing field of biomarkers of aging and related diseases. There are, however, some concerns about statistical methods used that need attention before the manuscript can be accepted for publication in eLife.

Essential revisions:

1) A general concern is that it is not clear what the authors controlled in various hypothesis tests. Different names and possibly different methods were presented for statistical significances as "FDR", "FDR-q", "p", "P", "pfdr", "FDR_P", and so on. Multiple testing correction was not likely applied in some analyses, for examples, mediation analysis and Mendelian randomization. It would be much easier to understand the results if only one method, e.g. B-H FDR, and label was used for all analyses.

2) The authors report an analysis of sex specific aging proteins. It would be important to replicate the results in an independent population. The interval study should have data to replicate the sex-specific aging signature.

3) Mediation by methylation. This analysis is interesting but there are some points that need clarification. Specifically, how did the author test for the enrichment of the age-associated CpG within 10 kb of aging proteins? Also, was the mediation tested only for CpG sites near genes, so only "cis" relations were tested but not "trans" relations? Finally, the claim about ENNP7 would be more believable if the authors show the relation between protein data versus the methylation data for this gene.

4) Association of age-related proteins with multimorbidity. A clean analysis would model the number of diseases using a Poisson regression and there is no need to run a two steps analysis, the authors could model the number of diseases over time using mixed effect models, or more easily GEE.

5) Cox proportional hazards models. The time variable of the models was not clarified. A crucial assumption of the Cox models, proportional hazards, was not checked by a test such as Schoenfeld residuals.

6) Differential protein expression across age. The plots show that the distribution of their population is not uniform over age. Their plots in Figure 6 shows a very suspicious correlation between the peak of the number of significant proteins and the larger concentration of individuals in their samples. The number of expressed proteins in a set is a function of the sample size, and the claim of the authors about the age pattern of significant proteins is not valid. The effects of the non-linear correlation were not taken into account in other analyses. Because of the effects, the adjustment for age was likely not enough for the Cox models, assuming follow-up time was the time variable. In Figure 8A, PROaccel cannot be independent from chronological age. Possibly this explains why the authors observed a significant mortality association in the older group only. At least quadratic effects of age, possibly higher orders, should be considered.

7) Proteomic signature of age. First, the authors have a proteomic score of age, not a signature, which is essentially a set with patterns. In addition, the analysis of negative and positive residuals is not valid statistically. The authors should use an interval about the predicted chronological age, and then define the groups of slower and faster age based on their statistically significant difference from the predicted age.

8) Pathway enrichment analysis. Some pathways were presented to be overrepresented in the set without any detailed information of the analysis. Background set and annotated sets for each pathway should be described possibly in a table.

9) It is not apparent which part of the findings or observations were new. It seems some parts e.g. aging signatures with 76 proteins, were supportive replications of previous findings of the authors or others. Any discussion about novel findings would be helpful to understand the significance of this paper.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your article "Plasma proteomic biomarker signature of age predicts health and life span" for consideration by eLife. Your article has been reviewed and discussed among the reviewers and the Reviewing Editor and Anna Akhmanova as the Senior Editor.

We believe the manuscript has improved but some concerns were still raised that are listed below. These needs to be taken into consideration before the paper can be accepted for publication in eLife.

Revisions:

1) It seems the authors simply replaced those various labels with "B-H FDR". Hence, some values in the columns "B-H FDR" cannot be correct. For example, the values of "B-H FDR" are identical to "p" in Supplementary file 1B.

2) No violation of the proportional hazards assumption should be clearly stated in the manuscript. As only the global p-value was given in the response, it is not clear whether the authors had checked the significance of every variable in their Cox model or not.

3) The text "did not affect the results" is too vague. It should be clearly stated with more explanation about the model and results.

4) All genes should not be used as the background reference because those included the genes for the proteins the authors didn't measure at all. When all genes were used as the reference set, such enrichment analysis likely identifies the enrichment among the 1301 measured proteins, which were proteins in plasma, comparing to all proteins. This explains why the authors found strong enrichments of inflammatory pathways.
