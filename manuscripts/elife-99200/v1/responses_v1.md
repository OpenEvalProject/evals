# Author response - Round 1

Authors:
- Dayna Adrienne Croock ([ORCID: 0000-0002-5107-8006](https://orcid.org/0000-0002-5107-8006))
- Yolandi Swart
- Haiko Schurz ([ORCID: 0000-0002-0009-3409](https://orcid.org/0000-0002-0009-3409))
- Desiree C Petersen ([ORCID: 0000-0002-0817-2574](https://orcid.org/0000-0002-0817-2574))
- Marlo Möller ([ORCID: 0000-0002-0805-6741](https://orcid.org/0000-0002-0805-6741))
- Caitlin Uren ([ORCID: 0000-0003-2358-0135](https://orcid.org/0000-0003-2358-0135))

## Response text

DOI: [10.7554/eLife.99200.4.sa2](https://doi.org/10.7554/eLife.99200.4.sa2)

The following is the authors’ response to the previous reviews

Recommendations for the authors:

Reviewer #1:

First, I thank the authors for clarifying some of the confusion I had in the previous comment and I appreciate the efforts the authors put into improving the quality of the manuscript. However, my concerns about the lack of novelty of the key findings are not perfectly addressed and there is no additional analysis done in this revision. Currently in this version of the manuscript, asserting that a p-value of 10-6 is close to genome-wide significance may be considered an overstatement. Further analysis focusing on finding novel and additional discovery is very necessary.

We thank the reviewer for their comments. Reviewer #2 also made a comment regarding the genomewide threshold, “However, it remains unclear why the authors found it appropriate to apply STEAM to the LAAA model, a joint test for both allele and ancestry effects, which does not benefit from the same reduction in testing burden.” The reviewers’ have correctly identified our oversight - we have amended the manuscript as follows:

(1) The abstract, “We identified a suggestive association peak (rs3117230, p-value = 5.292 x10-6, OR = 0.437, SE = 0.182) in the HLA-DPB1 gene originating from KhoeSan ancestry.”

(2) From line 233 to 239: “The R package STEAM (Significance Threshold Estimation for Admixture Mapping) (Grinde et al., 2019) was used to determine the admixture mapping significance threshold given the global ancestral proportions of each individual and the number of generations since admixture (g = 15). For the LA model, a genome-wide significance threshold of pvalue < 2.5 x 10-6 was deemed significant by STEAM. The traditional genome-wide significance threshold of 5 x 10-8 was used for the GA, APA and LAAA models, as recommended by the authors of the LAAA model (Duan et al., 2018).”

(3) We excluded the results for the signal on chromosome 20, since this also did not reach the LAAA model genome-wide significance threshold.

(4) From line 296 to 308: “LAAA models were successfully applied for all five contributing ancestries (KhoeSan, Bantu-speaking African, European, East Asian and Southeast Asian). However, no variants passed the threshold for statistical significance. Although no variants reached genome-wide significance, a suggestive peak was identified in the HLA-II region of chromosome 6 when using the LAAA model and adjusting for KhoeSan ancestry (Figure 3). The QQ-plot suggested minimal genomic inflation, which was verified by calculating the genomic inflation factor (= 1.05289) (Supplementary Figure 1). The lead variants identified using the LAAA model whilst adjusting for KhoeSan ancestry in this region on chromosome 6 are summarised in Table 3. The suggestive peak encompasses the HLA-DPA1/B1 (major histocompatibility complex, class II, DP alpha 1/beta 1) genes (Figure 4). It is noteworthy that without the LAAA model, this suggestive peak would not have been observed for this cohort. This highlights the importance of utilising the LAAA model in future association studies when investigating disease susceptibility loci in admixed individuals, such as the SAC population.”

We acknowledge that our results are not statistically significant. However, our study advances this area of research by identifying suggestive African-specific ancestry associations with TB in the HLA-II region. These findings build upon the work of the ITHGC, which did not identify any significant associations or suggestive peaks in their African-specific analyses. We have included this argument in our manuscript (from lines 425 to 432):

“The ITHGC did not identify any significant associations or suggestive peaks in their African ancestryspecific analyses. Notably, the suggestive peak in the HLA-DPB1 region was only captured in our cohort using the LAAA model whilst adjusting for KhoeSan local ancestry. This underscores the importance of incorporating global and local ancestry in association studies investigating complex multi-way admixed individuals, as the genetic heterogeneity present in admixed individuals (produced as a result of admixtureinduced and ancestral LD patterns) may cause association signals to be missed when using traditional association models (Duan et al., 2018; Swart, van Eeden, et al., 2022).”

We appreciate the comment regarding additional analyses. We acknowledge that we did not validate our SNP peak in the HLA-II region through fine-mapping due to the lack of a suitable reference panel (see lines 490 to 500). Our long-term goal is to develop a HLA-imputation reference panel incorporating KhoeSan ancestry; however, this is beyond the scope and funding allowances of this study.

Reviewer #2 (Recommendations for the authors):

The authors we think have done an excellent job with their responses and the manuscript has been substantially improved.

Thank you for taking the time to help us improve our manuscript.
