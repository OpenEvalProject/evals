# Peer review - Round 1

Editors:
- Moussa Zouache, https://ror.org/03r0ha626 University of Utah United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.97982.sa0](https://doi.org/10.7554/eLife.97982.sa0)

This important work advances our understanding of elements influencing neurodevelopment in children. The data presented is convincing and offers insights into the effect of demographic and environmental factors, particularly nutrition, on the functioning of the gut-brain axis and the risk for developmental delays.


---

# Peer review - Round 1

Editors:
- Moussa Zouache, https://ror.org/03r0ha626 University of Utah United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.97982.sa1](https://doi.org/10.7554/eLife.97982.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Serum metabolome indicators of early childhood development in the Brazilian National Survey on Child Nutrition (ENANI-2019)" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor.

As is customary in eLife, the reviewers have discussed their critiques with one another and with the Reviewing and Senior Editors. The decision was reached by consensus. What follows below is the Reviewing Editor's edited compilation of the essential and ancillary points provided by reviewers in their critiques and in their interaction post-review. Please submit a revised version that addresses these concerns directly. Although we expect that you will address these comments in your response letter, we also need to see the corresponding revision clearly marked in the text of the manuscript. Some of the reviewers' comments may seem to be simple queries or challenges that do not prompt revisions to the text. Please keep in mind, however, that readers may have the same perspective as the reviewers. Therefore, it is essential that you amend or expand the text to clarify the narrative accordingly.

The Authors are invited to address the reviewer's comments, giving particular attention to data presentation/analyses, handling of confounding variables and additional support for aspects of the methodologies employed. Specifically, the Authors should consider the following points in their revision:

1) Inclusion of microbiome and factors affecting microbiome composition in the study as possible confounders

2) Possible shortcomings associated with the directed acyclic graph approach (clarifications as to the methodology employed; inclusion of the microbiome and additional factors affecting microbiome composition) and more broadly confounding variable selection

3) Lack of power calculations and sensitivity analyses to validate some of the strong assumptions made in subject selection, stratifications and covariate identifications

4) Relevance/appropriate use of PLSR

5) Discuss the use of DQ as a viable outcome

6) Biases in subject selection (towards higher socio-economic status) and generalizability of the study

Reviewer #1 (Recommendations for the authors):

I would recommend that the authors include all study covariates in Table 1, Supplementary Table 1 and the Methods section Covariates to prevent confusion. In addition to the mean and 95% CI, the p-values for DQ should also be included in Supplementary Table 1. All covariates that are statistically significantly associated with DQ in your study cohort should be included in the statistical models, and additionally studied via either interaction analysis or mediation analysis depending on which analysis is most appropriate. The directed acrylic graph (DAG) can be discarded completely. Following these suggestions should help prevent biasing the current analysis by the authors' perceived relevance and relationships of the covariates with the dependent and independent variables.

All significant results from the initial correlation analysis should be stated and considered, although the most striking ones on the volcano plot can be emphasized. Of benefit to the authors is that in the search for biomarkers, it matters less what causes the change in metabolite (e.g., diet, obesity) nor even if the metabolite has a direct effect on the neurodevelopmental outcome and is rather just a side effect of the true causative factor(s). If the concentration of a serum metabolite can reliably indicate the neurodevelopmental outcome, it has value as a biomarker regardless, and exploring the relationship with covariates and mechanism can be initially explored in this manuscript as you have done (i.e., interaction analysis and mediation analysis) and investigated in future work.

As part of the fuller description of the initial correlation analysis, a supplementary table should be included that provides more information on the unknown compounds, including the mass, confidence level of any identifications, likely chemical classes and/or chemical formulas.

If including all the significant covariates in the regression models is non-trivial (e.g., issues of multi-collinearity), the better use of PLSR may be done at this step to see if the variable importance of the metabolites exceeds the confounders, rather than its current use in metabolite selection which did not yield any findings beyond what was already found by the initial correlation analysis. Another option would be to use machine learning, such as random forest where false discovery rates can be estimated for importance metrics (R package pRF).

All abbreviations included in the manuscript should be defined at their first instance.

Although the DQ is an invaluable metric, it would also be of interest to explore the relationship between serum metabolite biomarkers and the different neurodevelopmental domains (e.g., motor, cognitive, language, socio-emotional) if possible.

Reviewer #3 (Recommendations for the authors):

1. Why was sensitivity analysis not done? Why was mediation analysis done and stopped? Shouldn't other testing have been done?

2. Though it is a large sample size, the sampling technique was convenience sampling. In resource-poor settings this may be the methodology that is followed but has funding been applied for? What are the plans for further study?

3. What was the time period of the data collection? Which year? Is it relevant in the world of 2024?

4. Can the data be compared with data from Brazil where the children were from lower socioeconomic strata or where mothers or caregivers education was lower or higher than what is mentioned in the study?
