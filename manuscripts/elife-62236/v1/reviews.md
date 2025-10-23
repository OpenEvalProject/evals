# Peer review - Round 1

Editors:
- Arduino A Mangoni, Flinders Medical Centre Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62236.sa1](https://doi.org/10.7554/eLife.62236.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The authors have identified candidate markers of glucocorticoid action that can now be investigated in larger cohorts. This work has generated a vast amount of data, including transcriptomics data from both adipose tissue and peripheral blood mononuclear cells, plasma micro RNA data and serum metabolomics data.

Decision letter after peer review:

Thank you for submitting your article "Identification of human glucocorticoid response markers using integrated multi-omic analysis" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Clifford Rosen as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Natalie Bordag (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

The research focuses on the identification of markers of glucocorticoid action both at the transcriptomics level and the metabolite level. The availability of robust markers would be valuable in allowing the optimisation of glucocorticoid dosage. Ten subjects with primary adrenal insufficiency were used to enable biomarker discovery following treatment with hydrocortisone. While the cohort was small many of the markers observed had a high level of significance making this a useful preliminary study. A micro RNA (MiR-122-5p) was identified as being strongly correlated with glucocorticoid exposure and this finding was replicated in independent studies.

Essential revisions:

– Molecular data are often very noisy and require extensive cleaning. Which pre-processing approaches were applied? PCA is normally used to explore the sample structure and identify possible abnormalities while normalisation is needed to rescale the expression values to reduce noise. More explanations are needed on how PCA was used and whether any array normalisation was conducted.

– Certain results are not well explained. For example, those reported in the subsection “PBMC and adipose tissue transcriptomes have limited overlap in response to GC but are enriched for shared pathways” for PBMCs (the same applies to adipose tissue), how many differentially expressed genes (DEGs) did you find? This number is important to know before using those genes in pathway analysis. Did you use FDR or other forms of multiple testing correction to determine significance? It is unclear if you then used those DEGs to test pathway enrichment and you found a connectivity of n=4426 which is 3.7-fold stronger than using random genes. I am not sure what this means, or maybe 4426 is the list of DEGs? If so what is 3.7 connectivity? Please explain. Again, for pathways or GO terms enrichment, FDR should be used to correct for multiple testing. Overall, this analysis (Figure 2) does not appear to add much to the manuscript. Without multiple testing correction, relevant analyses seem to be those based on further gene filtering (i.e. retaining only genes confirmed across tissues and platforms such as those in Figures 4-8).

– Another example of low clarity is Figure 3. What is shared correlation? Heatmaps have no contrast and are uninformative. The dichotomisation by 0.5 is inappropriate, a higher cut-off (e.g. 0.8) might increase the contrast. Maybe the Venn diagram alone (Figure 3E) would be enough to convey your message if better explained?

– Discussion. miR-122-5p is not a novel circulating miRNA, it has been widely monitored as a diagnostic marker. Rephrase.

– There is a very extensive literature on miR-122-5p as diagnostic marker which I don't think has been thoroughly covered in the Discussion. For elevated miR-122-5p has been proposed as predictor on myocardial infarction which in turn has been associated with depressed hydrocortisone levels. Some additional discussion in this direction might be useful.

– Given that many conditions seem to affect miR-122-5p it would be important differentiate the effect of GC exposure from other conditions that affect its levels.

– In the metabolomics data the fold changes are quite small to confident on their robustness in such a small data set. Were the values of the metabolomic markers normally distributed?
