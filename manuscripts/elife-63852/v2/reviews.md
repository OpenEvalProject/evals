# Peer review - Round 1

Editors:
- Patricia W Finn, University of Illinois at Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63852.sa1](https://doi.org/10.7554/eLife.63852.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper identifies transcriptional signatures of 19 variables including psychosocial factors, blood cell composition and asthma symptoms through RNA-sequencing and a new machine learning strategy. The results show that immune gene expression mediates the link to negative psychosocial experiences.

Decision letter after peer review:

Thank you for submitting your article "Psychosocial experiences modulate asthma-associated genes through gene-environment interactions" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Mone Zaidi as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary

This paper studies the interaction between genetics and psychosocial environment. RNA-seq in PBMCs is performed to assess associations between transcription, questionnaire response data, PBMC cytokine production, and pulmonary function tests. Additionally, the investigators utilized genetic data to assess gene by environment interactions. This work would be of interest to a wide viewership. However, significant issues with underlying methodology detract from interpretation of the data and make it difficult to draw any definitive conclusions. Given these underlying concerns, this paper's conclusions are not supported by the data presented and significant changes in methodology are necessary.

Essential revisions:

1. The greatest concern with this manuscript is that instead of using observed variables the use generalized linear models with elastic net regularization was employed to develop surrogate markers for observed variables within transcriptional data. This in itself is not inherently problematic if the authors were able to identify transcriptional signatures that explained a significant amount of variance in the observed variable. Unfortunately, the data suggests that transcriptional signatures only predict differences in peripheral leukocyte population. The % variance explained for neutrophils, lymphocytes, and eosinophils was >30% (not suggested as a cutoff). Notably, these three variables had significant and strong correlations at follow-up time points. This suggests that the authors indeed did identify transcriptional signatures that might reasonably serve as surrogates to these observed variables. However, the main focus of this manuscript is the psychosocial environmental exposure. The % variance explained for each these transcriptional signatures is < 5%. Further, these transcriptional signatures showed weak rho values when assessed at follow-up. These are not reasonable surrogates for observed values as these signatures could not within a reasonable margin of error predict many of these psychosocial measures. Due to this issue the interpretation of figures 2 and 3 becomes obscured. It remains usure what it means to have self-disclosure signature correlated with a FEV1 percent predicted signature when these signatures are not predictive of observed data. Do the observed values correlate? If so this might lend credence to authors proposed transcriptional signatures. Further the same issue plagues to the findings in figure 3 where these transcriptional signatures are used for the regression to test if known eQTLs have interaction with psychosocial measures. Since Figures 2 and 3 represent the major findings of the paper. Unfortunately, definitive conclusion cannot be drawn until the authors rectify this issue.

2. With regard to the mediation analysis presented in Figure 2, two issues arise. First, the authors present the mediation as if the three leukocyte populations were assessed simultaneously as mediators which does not appear to be the case from the description in the methods. Second, a sensitivity analysis should be performed with the mediation to assess if there is an observed confounder.

3. There is concern if the sequencing genomes at 0.1x coverage is sufficient. This leaves a significant amount data that is imputed. How many of the significant findings were derived from imputed values? Does the pair-wise error rate reported for genotype call between 0.03 and 0.12 refer to percent of base pairs where there is a discrepancy? Units are important, is this 3-12% or 0.03-0.12%.

4. It is unclear whether the interpretation of the eQTLs associated with asthma/atopy risk in population where 100% subjects have asthma. In these populations changes in gene expression can't correspond to risk because no individual is at risk; they already have the disease.

5. One lingering question is the clinical implication(s) of this extremely elegant work. In the big picture, how could we employ these results to tailor treatments for kids with asthma?

6. The effect of sex differences. While the authors recruited a similar number of male and females, it is not indicated their proportion in the 119. Additionally, asthma severity in females is exacerbated due to menstruation (Also, asthma is worsened during hormonal changes in females (e.g., menstruation, see Zein, J.G., Erzurum, S.C. Asthma is Different in Women. Curr Allergy Asthma Rep 15, 28 (2015). https://doi.org/10.1007/s11882-015-0528-y). According to the provided data, the authors do not correct for this effect and based on the current text, it is not address whether it is was taken into account. Additionally, what is the justification for dropping all the gene chromosomes? Would the results change if they were not removed?

7. One of the main difficulties while reading the text for me was that some of the topics are not clearly introduced and explained in the main text, while they were super easy to follow the same concepts and ideas in the supplementary information and in the appendix. Could the author modify the text to make it a little bit clearer, please?

8. The authors indicate that SES transcriptional signature "strong overlap with each other". Regarding this sentence: (a) SES is a very complex item to define and measure. Could the author specify how did they calculate it, e.g., income, education, a conglomerated index? (b) Is it a correlation between which variables, e.g., normalized RNA-seq counts, outputs from the model? Or you are talking about common present/absent transcripts? (c) Based on the heatmap, there are a total of 4 SES-houses unoccupied, subjective SES, parental income and houses rated >=fair, and only houses unoccupied and houses rated >= fair have a strong negative correlation, which one would have expected. Also, only parental income and houses rated >=fair are in the same cluster. (d) "For example, subjective SES was significantly correlated with objective parental responsiveness, family conflict, and self-reported self-disclosure, which is the extent to which the youths talk about their thoughts and feelings (r=-0.26, p=0.004, r=0.25, p=0.006, r=0.53, p=6.8*10-10, respectively)". Are those correlations between the transcriptional signatures associated with each variable? Or between the variables themselves. Could you clarify it, please?Sometimes the authors employed the term transcriptional signatures of subjective SES while other times they just referred to subjective SES. Finally, were those correlations models corrected by age? Did you look at associations with race/ethnicity? Did you correct from age, sex, race, ethnicity, SES?

9 "Using mediation analysis, we found significant (p<0.05) paths through all three blood composition signatures, such that, at the molecular level, self-disclosure association with higher pulmonary function could be partially explained by an increase in the proportions of monocytes and neutrophils and reduced proportions of lymphocytes (Figure 2b)". Were other physiological inputs (e.g., subjected SES), mediators (e.g., IL13 GC resistance) and/or outputs (e.g., asthma severity) modeled for the mediation analysis? If not, may the authors explain the reasoning of selecting the chosen variables, please?

10. "To examine the genotype-by-environmental effects… entire cohort of 251 individuals" I am concerned whether the subjects that were employed to identify the transcriptional signatures include representative of those individuals not included in the models in terms of socio-demographic characteristics. Also, the models were validated with only in a subset of psychological measurements-note that psychological measurements were indeed the worst predicted in the validation set. Therefore, I am not sure that the predicted psychological values are adequate. Is there any manner that we can verify their accuracy?

11. For the physiological analysis, why anxiety measurements were not incorporated, e.g., GAD-7 or similar, as they can trigger asthma symptoms?
