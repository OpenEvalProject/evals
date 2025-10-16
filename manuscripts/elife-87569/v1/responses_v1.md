# Author response - Round 1

Authors:
- Xiaoxu Li ([ORCID: 0000-0001-5121-9190](https://orcid.org/0000-0001-5121-9190))
- Jean-David Morel
- Giorgia Benegiamo ([ORCID: 0000-0001-7164-6771](https://orcid.org/0000-0001-7164-6771))
- Johanne Poisson ([ORCID: 0000-0002-0183-845X](https://orcid.org/0000-0002-0183-845X))
- Alexis Bachmann
- Alexis Rapin
- Jonathan Sulc
- Evan Williams ([ORCID: 0000-0002-9746-376X](https://orcid.org/0000-0002-9746-376X))
- Alessia Perino
- Kristina Schoonjans ([ORCID: 0000-0003-1247-4265](https://orcid.org/0000-0003-1247-4265))
- Maroun Bou Sleiman
- Johan Auwerx ([ORCID: 0000-0002-5065-5393](https://orcid.org/0000-0002-5065-5393))

## Response text

DOI: [10.7554/eLife.87569.3.sa3](https://doi.org/10.7554/eLife.87569.3.sa3)

The following is the authors’ response to the original reviews.

Reviewer #1 (Recommendations For The Authors):

- There were no mechanistic or causation-focused investigations that could have greatly strengthened the study. The study is ultimately providing two prioritized candidate genes that may be causative, reactive, or independent of the disease.

We thank the reviewer for their positive assessment and agree that our study lacks formal causal analyses. We are aware of this limitation and have made it clear throughout the text. Through triangulation of evidence across tissues and species, we point to very interesting candidates that merit further study, which is the usual scope of such systems genetics investigations. Nevertheless, to introduce some causal inference and reinforce the human relevance of our results, we have performed Mendelian randomization (MR) analysis to investigate the potential associations between MUC4’s gene expression in human colons and the risk of IBD. EPHA6 lacks detectable eQTLs in human colon so we could not include it in this analysis. We found suggestive evidence that increased expression of MUC4 in the sigmoid, but not transverse, colon may increase the risk of IBD (nominal p = 0.033).

The description in the manuscript:

However, it is unclear through what mechanisms the genetic variants in the candidate genes affect IBD susceptibility. One possibility is that genetic variation leads to altered levels of expression of the gene, ultimately affecting disease susceptibility. To test this possibility, we examined the GTEx resource (GTEx Consortium, 2013) and found that MUC4, but not EPHA6, has cis-eQTLs in the sigmoid and transverse colon. To establish likely causal links with IBD incidence, we used these associations as instruments in a two-sample Mendelian randomization (MR) (Hemani, Tilling and Smith, 2017; Hemani et al., 2018) analysis. Using publicly available GWAS summary statistics for IBD, Crohn’s disease, and ulcerative colitis (Liu et al., 2015; Elsworth et al., 2020) as outcomes, we found suggestive evidence that increased expression of MUC4 in the sigmoid, but not transverse, colon may increase the risk of IBD (nominal P value = 0.033, Appendix 1 - Table 6). No eQTLs were reported for EPHA6 in the colon, precluding us from investigating the potential consequences of changes in its expression in these tissues.

- Figures 3 and its supplement Figure 1: Among the 39 modules, the authors have only focused on significantly overlapping up-regulated IBD-related gene modules in both CD (M28 and M32) and HFD (M9 and M28) for their follow up analyses in Figures 4 and 5 to prioritize candidate genes. However, this reviewer thinks there is great value in also focusing on significantly overlapping down-regulated IBD-related gene modules in both CD (M17) and HFD (M15 and M26) for their follow up candidate gene prioritization analyses.

Thank you for your suggestion. We had initially performed overrepresentation analyses in HFD_M15, HFD_M26 and CD_M17, but did not find enrichments related to inflammation (see Author response image 1 below). We did not include this result in the manuscript.

Gene ratios higher than 0.1 are shown and represented by dot size. Dots are colored by -Log10(BH-adjusted P values).

We also checked the module QTL mapping for the significantly overlapping down-regulated IBD-related gene modules in both CD and HFD. We did not find any loci that are significantly associated with these modules, indicating that they are not modulated by genetic variation and hence are less likely to inform on IBD susceptibility.

The description in the manuscript:

The ModQTL analysis was also performed on the modules that are significantly enriched in IBD-downregulated genes (HFD_M15, HFD_M24, and HFD_M26), but no significant or suggestive QTLs were detected. Therefore, we focused on the QTL for IBD-induced genes in HFD_M28 and annotated its candidate genes based on three criteria (Figure 5B).

Reviewer #2 (Recommendations For The Authors):

- One small addition that would be nice would be to indicate if the two candidate genes have cis eQTL in human tissues and/or have any protein-coding variants in humans. This would provide nice additional evidence of causality for these two genes.

Thank you for your positive assessment and suggestion. MUC4 and EPHA6 both have protein-coding variants in humans that were listed in the Appendix – Table 3 and Table 4. In addition, cis-eQTLs have been found for MUC4 in both the sigmoid and transverse colon in humans (GTEx, https://gtexportal.org/home/locusBrowserPage/ENSG00000145113.21). As indicated in our response to the first comment of Reviewer #1, we have now performed mendelian randomization on human eQTL for MUC4. However, no eQTLs were reported for EPHA6 in the colon, preventing us from performing MR analysis on its expression.

- Also, it would be helpful to include the size of the modules in the text of the manuscript. Especially the two modules that were followed up on.

Thank you for your suggestion, we have indicated the size of IBD-related modules in the text of the manuscript.

The description in the manuscript:

Enrichment analyses indicated that modules HFD_M9 (484 genes), HFD_M16 (328 genes), and HFD_M28 (123 genes) were enriched with genes that are upregulated by DSS-induced colitis, while HFD_M15 (368 genes), HFD_M24 (159 genes), and HFD_M26 (135 genes) were significantly enriched with downregulated genes (Figure 3C). Of note, more than 20% of genes involved in HFD_M9 and HFD_M28 were part of the dysregulated genes of the acute phase of mouse UC (day6 and day7) (Figure 3C). Interestingly, genes perturbed during IBD pathogenesis in humans were also enriched in HFD_M9 and HFD_M28 (Figure 3C).

While IBD-related genes were predominantly found in HFD modules, we also found that two modules, CD_M28 (185 genes) and CD_M32 (142 genes), in CD-fed mouse colons were associated with IBD (Figure 3—figure supplement 1A). These two-modules significantly overlapped with the IBD-related HFD_M9 and HFD_M28 modules, respectively (BH-adjusted P value < 0.05) (Figure 3—figure supplement 1B). Moreover, the molecular signatures underlying human UC and Crohn’s disease were also clustered in these two modules (CD_M28 and CD_M32) under CD (Figure 3—figure supplement 1C). Collectively, the co-expression and enrichment analyses identify HFD_M9 and HFD_M28 as IBD-related modules on which we focus our subsequent investigation.
