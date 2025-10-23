# Author response - Round 1

Authors:
- Kyaw Thu Minn
- Yuheng C Fu ([ORCID: 0000-0001-8037-6398](https://orcid.org/0000-0001-8037-6398))
- Shenghua He
- Sabine Dietmann
- Steven C George
- Mark A Anastasio
- Samantha A Morris ([ORCID: 0000-0001-8561-4340](https://orcid.org/0000-0001-8561-4340))
- Lilianna Solnica-Krezel ([ORCID: 0000-0003-0983-221X](https://orcid.org/0000-0003-0983-221X))

## Response text

DOI: [10.7554/eLife.59445.sa2](https://doi.org/10.7554/eLife.59445.sa2)

Essential revisions:

1) Additional clarification of statistical analysis is needed. Some of the differences in the cell type, interspecies comparisons and interaction between selected receptor-ligand pair are relatively small and so inclusion of confidence intervals (or additional details of analysis) would confirm that these differences are robust.

To test statistical significance in interspecies comparisons, we implemented a randomization test to identify mouse or monkey cell types that map to a gastruloid cell type with statistical significance of p < 0.05. The results of this statistical analyses are incorporated in Figure 3I and J, and the implementation method is explained in the Materials and methods section.

The enrichment of predicted Eph-ephrin pairs (p value) shown in Figure 8—figure supplement 5, is based on the comparison against all receptor-ligand interaction. No statistical test was performed specifically among Eph-ephrin interactions. We rephrased the text to emphasize Eph-ephrin complementary expression in distinct cell types but not enrichment between pairs of cell types.

2) In some cases, it isn't clear whether there are mixed populations of cells or cells with mixed characteristics. The authors should attempt to distinguish between these two possibilities by assessing the scRNAseq data to determine if the cells can be split into two groups or whether markers of the two lineages are co-expressed. This should be carried out for 1) amnion and trophoectoderm , 2) in the ectodermal cluster -neural cells versus surface ectoderm and 3) for primitive and definitive endoderm.

We have carried out additional analyses, but they could not separate sub cell types within the three cell populations. We updated our figures to show expression of additional cell type-specific markers: neural versus surface markers in Ectoderm cluster (Figure 4—figure supplement 2), primitive versus definitive endoderm markers in Endoderm cluster (Figure 4—figure supplement 6), and amnion versus trophectoderm markers (updated Figure 6C). These analyses support the notion that ExE cells co-express markers of trophectoderm and amnion, and cells in Endoderm cluster express markers of definitive endoderm and primitive endoderm. We also discuss that the lack of cells with clear trophectoderm and primitive endoderm identities in the 2D gastruloid culture is consistent with H1 (or H9) conventional/primed hESCs resembling post-implantation epiblast. Indeed, primed hESCs have not been convincingly differentiated into pre-implantation trophoblast or primitive endoderm lineages.

3) The identity of large numbers of cells as ExM in the gastruloid model is confusing. The authors comment on this in the Discussion and note that it may be biased by the large proportion of ExM cells in the monkey dataset. It would be useful to include this caveat where the data is originally discussed to avoid giving misleading impressions.

In agreement, we have included this caveat in the Results. As illustrated in Figure 4—figure supplement 4, top 50 monkey EXMC markers show non-specific (or broad) expression in all gastruloid cell types, suggesting that EXMC is a mis-match in gastruloid.
