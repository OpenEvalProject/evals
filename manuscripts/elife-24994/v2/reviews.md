# Peer review - Round 1

Editors:
- Patrick Nolan, Medical Research Council Harwell United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.24994.027](https://doi.org/10.7554/eLife.24994.027)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The genomic landscape of human cellular circadian variation points to a novel role for the human signalosome" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom, Patrick Nolan (Reviewer #1), served as Guest Reviewing Editor, and the evaluation has been overseen by Mark McCarthy as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Yoshitaka Fukada (Reviewer #2) and Michael McCarthy (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Gaspar et al. present their findings on circadian variation in human umbilical cord fibroblasts. They used a GWAS study and identified SNPs associated with a number of molecular circadian phenotypes. The authors claim the genetic variants they identified show greater than expected differences in allele frequency in a group of subjects with extreme chronotypes. Based on GWAS data, they focused on COPS7B, a subunit of the COP9 signalosome, for a number of mechanistic investigations into period determination. The authors use a number of approaches, including RNAi, Co-IP of FLAG-tagged proteins and SILAC, to validate their initial findings and propose some interesting and novel molecular mechanisms. Specifically, they argue that COPS7B may promote the stability of the circadian transcriptional regulator, BMAL1. Based on these observations, they posit that clock protein half-life is determined by contributions both from destabilising factors via the ubiquitin proteasome and stabilising factors via the signalosome. The latter would represent a significant addition to our understanding of the molecular basis of circadian period determination.

Essential revisions:

GWAS:

Conducting a GWAS study with such a small number of samples (140-147) is ambitious and this probably underlies the high p-values for the data described throughout the manuscript. Although such datasets usually require higher power, the reviewers understand the limitations here. It is not reasonable to expect numbers in a cell-based experiment to go much larger, or equal to those seen in GWAS (N>10,000). Both points should be discussed and justified.

Please justify multiple testing using a threshold of FDR 0.1. Why choose this threshold? An FDR of q<0.05 is reasonable for a GWAS study, even a cell based study. An FDR of 0.1 seems unusually high. If not justifiable, then perhaps gene list should be modified.

In subsequent text, the authors quote the p value for the two most significant SNPs affecting PER2 expression, not the q value. Why?

It would be helpful to know the degree of phenotypic correlation across the 5 rhythm parameters, and to estimate their genetic overlap. Do any of the markers associate with more than one parameter (as expected)? Or if not, why? For example, in comparing Manhattan plots, PER2 expression is the only variable where the Chr2 SNPs show anything near a threshold. Given the eventual mechanistic validation (BMAL1 stability), shouldn't we expect a similar pattern in the Manhattan plot for PER1 expression? Please provide this information and justify.

In Figure 1, the statistical method is not well described, nor is a citation provided that validates the approach. The reviewers have concerns that simply calculating the difference in allele frequency between groups may not be valid across the entire range of allele frequencies. Why wasn't a more standard approach employed (e.g. chi square analysis, or for selected SNPs, trait morningness vs. genotype association)? If possible, these analyses should be included. Also in Figure 1, is it appropriate to study all association with chronotype equally? For instance, SNP associations with phase may be predicted to have stronger contribution to chronotype than amplitude. This approach should be justified, especially in light of the small sample size and the multiple comparisons problem.

RNAi:

Aspects of the RNAi experiments are hard to interpret. Of the 28 genes affecting period and 29 affecting amplitude, is there overlap (i.e. genes that affect both)? Of the control RNAis, the results should more clearly state how many control RNAis were used, and what proportion affected period or amplitude. Does a chi-square test indicate this proportion is significantly different?

In subsection “Genes associated with positive SNPs affect circadian clock function”, when assessing the probability that the genes affect the circadian clock when compared to random genesets, it is unclear why the authors have used one test to assess the reduced & increased period/amplitude and a different test for the combined cumulative distribution. Presumably this is from analysis of the same data so the same tests should be used, please change or justify.

Gene enrichment analysis, Figure 3:

The authors state that they 'applied gene ontology enrichment analysis to the list that we obtained'. There is a bit of confusion here. Was this applied to the 59 genes from 3C or the 76 genes from the original eQTL? What threshold was used for the GSEA? Figure 3A and 3B should be amalgamated into a graph with clear p-values added to the graph. As written in subsection “Positive SNPs highlight protein catabolism as essential to human circadian variation”, paragraph 2, authors then go on to pick the genes from 5 of the top 6 pathways for further analysis shown in Figure 3D-F. Is this somehow relevant to what is shown in Figure 3C? Only some of the pathways shown in Figure 3C are significant and included in the top 6 pathways. For example, oxidoreductase activity (included) is not in the top 6 pathways in Figure 3—figure supplement 1 while macromolecule catabolic process (not included) is? Finally, given that the resulting genes are not significant in the GWAS and are not from a random sample, please provide evidence that the significant increase/decrease in period (Figure 3E) is not by chance.

Figure 4 and associated text:

Is the rs920400 AA genotype associated with long or short period in fibroblasts? How can this be reconciled with 'average PER2 expression' being higher? Is it justifiable to use a single timepoint here to look at PER2 expression? Do the genetic association findings of COPS7B share any association with the BMAL-Luc parameters? As the main result, the COPS7B association should be reported for all of the 5 parameters selected. If the genetic association does not match the RNAi experiment, the discrepancy should be discussed. It is difficult to accept that COPS4 knockdown lengthens period (by 9.9 hrs!) as it appears to completely obliterate the bioluminescence rhythm. What is the condition of the cells after knockdown? Labelling in Figure (COP4) is incorrect.

Figure 5 and associated text:

The authors claim direct binding of COP9 signalosome with several clock proteins, but the data need to be polished in order to fully support this conclusion. The immunoprecipitation analysis (Figure 5A, B, D) lacks essential experimental controls: in the FLAG-IP experiment, COPS7b signal should be no longer be detected in the absence of co-expression of FLAG-proteins in the same gel. These controls should be included in Western Blots. In the FLAG IP (a) the COPS7B antibody appears to cross-react with both PER2-FLAG and CRY1-FLAG. This confound should be addressed and justified. Both panels seem to show that interaction of COPS7B with PER2-FLAG and CRY1-FLAG is greater than with BMAL1-FLAG, yet the authors are proposing a direct interaction with BMAL1, how is this so? Authors should address this as it affects their arguments in the paper. Figure 5C. What does the * signify and how was it measured? Presumably this should be a repeated measures ANOVA determination. Statistical methods should be included. How does this translate into 'the half-life of BMAL1 was reduced twofold'? Figure 5—figure supplement 1. Shouldn't you be seeing some protein degradation in these graphs, there is nothing evident here, particularly so in the CRY1 experiment. Some explanation is required in the text. How is this related to 'The half lives of CRY1 and PER2 remained unchanged'? Neither levels approach anything near 50% of the time-0 timepoint. What does 'even if their absolute abundance varied' mean?

Subsection “COPS7B and the COP9 signalosome are rhythmically imported into the nucleus”:

The argument the authors make about the conflicting phases of expression of PER/CRY with COPS7B in U2OS cells might hold for native protein interactions but this should not hold when constitutively ovexpressing recombinant PER-FLAG and CRY-FLAG proteins. There must be some other cause for the discrepancy seen in protein interactions in the two cell lines. Please address these issues in Results and Discussion.

Presentation and style:

There are numerous instances of errors in cross-referencing of Figures, referencing citations and overall flow of text in Results section.

Abstract:

Given that the Abstract is the first port-of-call for many readers, it should be a realistic reflection of the main findings and conclusions in the manuscript. Some text such as 'Overwhelmingly gene set enrichment points to differences in protein catabolism as the major source of clock variation in humans' is rather strong. The reviewers request that this be toned down appropriately.
