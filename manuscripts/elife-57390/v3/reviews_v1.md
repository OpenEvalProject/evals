# Peer review - Round 1

Editors:
- Stephen CJ Parker, University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.57390.sa1](https://doi.org/10.7554/eLife.57390.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This exciting study quantifies the genetic architecture of gene expression (eQTL) and protein abundance (pQTL) regulation in iPSCs and will server is an important benchmark for the community. The rigorous comparison of these e/pQTL maps reveals differences that represent expected biological diversity, with a notable example in Figure 3B. Further, this work will serve as a foundation for many novel future studies, including GWAS colocalization and additional omics layers.

Decision letter after peer review:

Thank you for submitting your article "Population-scale proteome variation in human induced pluripotent stem cells" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Stephen CJ Parker as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Patricia Wittkopp as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Arushi Varshney (Reviewer #3); Roderic Guigó (Reviewer #4).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

Here the authors report pQTL results on 202 iPSC lines from 151 donors which already had RNA-seq data, enabling direct population-scale comparisons of eQTL and pQTL. This manuscript is well-written, clear, and has impactful results. We think it would be a great resource for the field. This is excellent work, and the authors are to be commended on an exciting study. We have a few items of feedback:

Revisions:

1) It is unclear how the acquisition of RNA and proteomics data were related. For example, were the same batches prepped, split, and material frozen for later profiling. Or, were the lines grown up at separate times for each of the different profiling modalities? If the latter, how could this potentially RNA-protein confounding batch effect influence the results?

2) In subsection “pQTL arising from protein-altering variants”, paragraph three, the authors advocate using protein abundance instead of RNA to interpret pathogenic mechanisms of rare variants. However, QTL studies generally have low power to detect effects for SNPs with low MAF. In fact, in this study, the authors used MAF 5% or higher. So, how does one reconcile this assertion to use protein abundance to interpret rare variant effects with the massive sample size it would take to do so. Addressing this idea in the text would be helpful.

3) The authors should make the full summary scan results available so that the rest of the community can use them as a resource.

4) Discussion paragraph three, the word "significant" is missing a "ly" and we'd advise removing that word altogether. In general, it should be used when making a statistical comparison and the associated test and p-value should be provided. This is not mentioned anywhere in the sentence. So, either those results should be disclosed, or a different word without a statistical connotation should be used. The same issue is present in paragraph three of subsection “pQTL arising from protein-altering variants”.

5) The variance component analysis showed effects of culture medium, sex, age etc. Were these taken as covariates in the QTL analysis? Looking at effects of the culture medium, were the culture passage numbers comparable across lines and does that have an effect?

6) For the X chromosome inactivation (XCI) section, it is unclear how exactly the XCI status was quantified. Subsection “RNA and proteome variability” paragraph two and the legend to Figure 1 reference the Materials and methods section but a description of this analysis is missing there. These results are hard to interpret without methodological clarity.

7) Figure 1D – While the random forest model analysis is interesting, the authors should elaborate on their selection of these specific variables. Some other factors that would be informative to include would be MAF and RNA expression level.

8) Figure 2B and 3C – is the grey bar/shaded region in these plots the genomic location of the respective gene? If so, this should be specified in the legend.

9) Figure 3C and the corresponding text briefly describe a pQTL for the VRK2 gene where the pQTL SNP is also a GWAS SNP for schizophrenia risk. The authors should elaborate on the pQTL direction of effect with respect to GWAS risk. Is the variant the lead SNP for GWAS or what is the LD r2 with the lead SNP and do these signals colocalize in that case? Is there some evidence of this protein being relevant in schizophrenia related cellular mechanisms?

10) Figure 4E – This is an interesting example. What is the eQTL/pQTL and trans pQTL direction of effect with respect to the Alzheimer's GWAS risk allele? In this example, the SNP rs1129187 is associated with PEX6 mRNA expression and protein abundance, and also associated with PEX1 and PEX26 abundance. To directly test if the trans-association of the SNP with PEX1 and PEX26 is through the association with PEX6 (complex stability) and not through other mechanisms, have the authors tried to regress out the PEX6 abundance from the association between the SNP and PEX1 or PEX26 and check if the association disappears?

11) Wrong figures are referenced in some places in the manuscript. Figure 3D is referenced before 3B etc.

12) Were there genes for which significant eQTL and also pQTL associations were identified but the variants were independent (low LD r2?)

13) It was confusing that the authors do not clearly distinguish between the variant affecting the phenotype of the gene (transcript or protein expression) and the affected gene. They write "we report 654 genes with a cis pQTL and 3487 genes with a cis eQTL. I assume that will in general find multiple p/eQTLs for a given gene (althought these number do not appear to be reported). These are thus the numbers of p/eGenes, but not of p/eQTLs. However, when they set to investigate replication of p/eQTLs, the numbers correspond to p/eGenes. The authors equate the numbers of QTLs with the number of affected genes. This part could be more clear.

14) Figure 1B. It looks to me that the fraction of the total variance explained by the factors the authors use in their model is much larger for transcriptomics than for proteomics data. I suggest the authors to report this number. If I am correct, this would mean that proteomics data behaves "somehow" more stochastically than transcriptomics data, maybe reflecting technical issues. It maybe also linked to the lack of replication of eQLTs at the protein level.

15) I understand the rationale of using 250Kb for eQTL analysis, since much of the regulation of gene expression is likely to reside in the promoter region. However, I do not see a biological rationale for using the same window for pQTL analysis. I understand that using the same window maybe the only way of making meaningful comparisons between eQTLs and pQTLs, and I think that this is ok. By using the same window the authors are implicitly assessing to what extent variation affecting gene expression also affects protein expression, that is the genetic variation in which the impact on protein expression is mediated by the impact on gene expression. Maybe the authors should acknowledge this.

16) Related to the above. eQTLs tend to cluster around the TSS. Do they observe the same clustering for pQTLs? What is the comparative distribution of p/eQTLs along the tested region?
