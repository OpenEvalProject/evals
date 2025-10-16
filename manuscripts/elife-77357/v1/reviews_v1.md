# Peer review - Round 1

Editors:
- Erica A Golemis, https://ror.org/0567t7073 Fox Chase Cancer Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77357.sa0](https://doi.org/10.7554/eLife.77357.sa0)

This manuscript makes a valuable contribution to the common understanding of the function of lncRNAs in cancer formation and progression. Besides developing and applying a robust analysis framework of large-scale pan-cancer omics datasets to discover the roles of 30 long non-coding RNAs (lncRNAs) in cancer proliferation and growth, the authors performed direct function-testing experiments to validate the predicted biological mechanisms of two lncRNAs. The analysis framework developed here can serve as a resource to study the functions of lncRNA in cancer, and the computational framework can also be further extended to study cancer-relevant transcriptional and post-transcriptional regulation.


---

# Peer review - Round 1

Editors:
- Erica A Golemis, https://ror.org/0567t7073 Fox Chase Cancer Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77357.sa1](https://doi.org/10.7554/eLife.77357.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Systematic lncRNA mapping to genome-wide co-essential pathways uncovers cancer dependency on uncharacterized lncRNAs" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Erica Golemis as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Xi Steven Chen (Reviewer #1); Xingyi Guo (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. The modeling work described on Page 5 lines 108-114, and Page 6 is a bit confusing. Were those two analyses the same or independent? On page 5, 540 positives and 500 negative lncRNAs were discovered, but 1027 lncRNAs were identified on Page 6. It's important to clarify the analysis workflow here. It's also necessary to mention the total number of annotated lncRNAs used in the analysis.

2. On page 8, the top 200 negatively and 200 positively associated genes for each lncRNA were used for downstream analysis, which was an arbitrary cutoff. Instead, the Kolmogorov-Smirnov test implemented in GSEA could be considered to use the whole gene list to test enrichment.

3. Could the authors clarify the reason 50 Hallmark gene signatures were used in TCGA analysis instead of using the same co-essential modules in CCLE analysis?

4. Could the authors clarify the number of TCGA samples used in the analysis? For example, we know there are more than 1000 BRCA samples, but only 526 samples were used in the analysis. In 7B, why were only a few cancer types listed instead of all ten cancer types?

5. In the multivariate regression, the authors should include a covariant, 'cancer type' if they used all data combined from different cancer types, to adjust potential cancer heterogeneity. Alternatively, they can perform such analysis for each cancer.

6. In lines 530-532: "The BH adjusted regression P<0.001was used as the cut-off to select significantly associated lncRNA-mRNA pairs in CCLE or a specific TCGA cancer type." To identify significantly correlated lncRNA-mRNA pairs, the authors need to justify why they would not just use results from TCGA to replicate the associations.

7. In lines 547-549: "We finally selected the modules that show significant enrichment of proliferation/growth-regulating genesets/pathways." -The authors need to provide a detailed number here.

8. In lines 555-557: "0.05. The average regression coefficient scores, measured from the lncRNA and module members, were used to predict the lncRNA-mediated co-essential module regulation direction." The authors need to discuss the limitation of this strategy to predict the regulation direction, as the statistical approach is not well justified.

9. In the Methods section, "Meta-analysis of lncRNA and gene expression", the authors need to discuss the limitation of this approach, as the different sample sizes could lead to a significant bias. The authors should consider that the results could be more reliable from the largest sample size of RNA-seq dataset.

10. The authors may wish to include additional analyses using data for lung squamous cell carcinomas, as they are available in TCGA.

Reviewer #2 (Recommendations for the authors):

I hope my comments below could help authors improve their work in their revision.

Well-established cancer-driver genes/cancer gene consensus may need to be considered for their annotations.
