# Peer review - Round 1

Editors:
- Marcelo Nobrega, University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.31977.046](https://doi.org/10.7554/eLife.31977.046)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Integration of human pancreatic islet genomic data refines regulatory mechanisms at Type 2 Diabetes susceptibility loci" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aviv Regev as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The reviewers of your manuscript found that the publication of a comprehensive epigenomic map of human islets is of broad interest and a timely resource for the community. The study has significant strengths, including the important observation of the far superior performance of WGBS compared to even the more recent, expanded 800K methylation array in comprehensively annotating methylation sites across the genome. Another significant strength highlighted by all reviewers is the integration of this dataset with other functional annotations and genetic fine mapping for T2D-associted loci, readily identifying a subset of variants that are putatively causal of the associations, and laying out a general analytical strategy that can be used by others, beyond those with immediate interest in T2D genetics. Overall, the reviewers found that this study significantly contributes to the effort of generating comprehensive functional annotations of a tissue of great medical and biological importance and thus far not properly characterized yet.

Below is a summary of essential points to be addressed:

1) The data presented starting in Figure 2B and shown throughout the manuscript suggest that virtually all enrichments are significant using FDR (masked by reporting only "FDR < 0.05" in main text). A more appropriate representation would either be quantitative (size proportional to log10p) or using a more stringent (Bonferroni) correction. The enrichments shown could be depicted in a more quantitative manner.

2) Causal GWAS variants can be enriched in regions with other functional annotations, such as coding regions or regions with strong evolutionary conservation. Such regions have not been considered here. The authors chose to reweight their PPAs solely using chromatin data, but this would down-weight causal variants with other functional annotations in the same region.

3) How much have the segmentations from the HMM improved with the additional data generated (without using GWAS enrichment as the benchmark)? It appears as though FGWAS enrichments for the actual annotations themselves (shown in Figure 3—figure supplement 1 and Figure 3—figure supplement 2) are just as good, if not better, than the HMM analysis (could also look at simple non-HMM two-annotation enrichments). Another way to look at this in the authors' framework would be to compare the median # of credible set SNPs (and top PPA) using only these annotations for FGWAS.

4) Both the Bayes Factor and FGWAS approaches rely on the assumption that at most one SNP in each region is causal, which may not always be true. This limitation should be discussed.

5) The addition of the Capture-C data in Figure 5C does not appear to help resolve rs11708067 as the likely causal variant as a several LD variants are similarly (by eye) overlapping fragments of high Capture-C density. Could this be quantified?

6) Given the known advantages of Stratified LD Score Regression (Finucane et al., 2015) over FGWAS to uncover true enrichments, have the authors considered using this approach?

7) What proportion of the narrow sense heritability is captured by the PPA variants?

8) The nomenclature used to define individual loci emerging from GWAS has followed the historical approach of using the closest gene to the associated SNPs. It has recently been recognized that this is often an imprecise approximation, as pointed out by reviewer 1. While there is no expectation that the authors would come up with a solution to this nomenclature conundrum, it was felt that the authors might address this issue on the paper, highlighting that the gene names associated with each locus may not accurately reflect the gene target of the association.

9) It was also noted that, despite the depth and complexity of the analysis carried out in this work, key data are missing which would greatly enhance the value of this report. An example is provided by Figure 4D: why not present a table giving the identified variants at each of the loci (or at least the top half?) with their causal probability? Presumably TCF7L2 refers to rs7903146? This should be clarified (as for the other loci included). It would also be nice to provide eQTL data for this and a few other chosen loci.

10) Finally, we would suggest that the authors consider bringing up the possibility that the association signal of several of the GWAS loci analyzed, including the ones highlighted in this work (see comment 5, above), might result not from the phenotypic impact of a single causal variant, but rather by the combined effects of multiple variants within the associated haplotype. This is certainly a topic that will become more obvious as we perform more detailed and high throughput computational and experimental analysis of GWAS loci, and it would be important for this work to come out already pondering about this possibility.
