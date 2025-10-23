# Peer review - Round 1

Editors:
- Andrew P Morris, University of Liverpool United Kingdom

Reviewers:
- Andrew P Morris, University of Liverpool United Kingdom
- Louise Wain, University of Leicester United Kingdom

## Review text

DOI: [10.7554/eLife.42720.022](https://doi.org/10.7554/eLife.42720.022)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Identification of an emphysema-associated genetic variant near TGFB2 with regulatory effects in lung fibroblasts" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Andrew P Morris as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Mark McCarthy as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Louise Wain (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The reviewers appreciated the work in bringing together the largest GWAS of emphysema to date, and agreed that the integration of GWAS findings with eQTL resources and additional epigenomic data was a good demonstration of how to move from locus to causal variant and effector gene. However, the reviewers were concerned that the association signal at the TGFB2 locus was driven by just COPDGene NHW, with no evidence of association in COPDGene AA or ECLIPSE.

Essential revisions:

1) Independent replication of the emphysema association signal at the TGFB2 locus is essential. Ideally, this would be in an additional study of emphysema, although supporting evidence from related phenotypes (e.g. COPD or lung function) would be an alternative.

2) More details are needed for the colocalization part of the work. As of now, only the reference for the approach is noted. It would be helpful to know the thresholds used and the results they observed. In addition, there are many different colocalization approaches and they tend to not always agree. We ask that the authors assess whether the results are robust to different colocalization methods.

3) The provision of the full results of the eQTL colocalisation analysis is commendable and potentially useful resource for the community. However, the authors should provide the caveat that at P<5x10-5 there are likely to be many false positive emphysema GWAS associations and so replication of the GWAS results should be sought prior to embarking on pursuit of the genes implicated by this analysis.

4) The associations on chromosome 15 (CHRNA3/f locus) and chromosome 19 (CYP2A6) reflect an effect on lung function via smoking behaviour and thus point primarily to addiction pathways. Accepting that it is difficult to entirely adjust for smoking in these analyses, the authors could comment on this and perhaps report (through comparison with published smoking GWAS data) which of the signals might be driven by smoking.

5) The association with the SERPINA1 z-allele is of interest but suggests that there might be individuals with alpha-1 anti-tryspin deficiency amongst the cases. This information should be provided.

6) The authors mentioned that they used PICS to derive "likelihoods" that variants are causal. It would be useful to have a brief description of this approach in the Materials and methods. What is the likelihood of the chosen SNP versus the other six? What is the motivation for the 5% threshold? A more usual approach would be to build a 99% credible set, and then interrogate those variants instead. Posterior probabilities should be provided for variants considered in downstream interrogation

7) For enrichments, the authors use 125 cell types from the Roadmap Epigenomics segmentations (subsection “Overlap of LHE SNPs with Epigenomic Marks in Roadmap Epigenomics Cell Types”) but then state that enhancer were defined by collapsing states 13-18 from Ernst and Kellis, 2015. However, Ernst and Kellis, 2015, does not describe the Roadmap Epigenomics chromatin states, so the reviewers were confused about how the enhancer states were actually generated.

8) The GoShifter approach has been shown to be suboptimal for calculating enrichments (Iotchkova et al., 2019) and we would instead recommend running GARFIELD, which has built-in Roadmap and ENCODE annotations. This would strengthen the enrichment results.

9) In the Discussion the authors note that the underlying regulatory element is called in some but not all fibroblasts data sets and hypothesize that this could represent restricted activity to some subset of fibroblasts, or some subset of conditions. If this is truly the causal variant, then couldn't the element call be a function of sample genotype too? And, thus if the ENCODE/Roadmap/etc. sample did not have the "active" genotype, a peak call might not be observable. We would encourage the authors to add this as a possible interpretation, unless there is justified motivation to report otherwise.
