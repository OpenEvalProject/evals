# Peer review - Round 1

Editors:
- Naama Barkai, Weizmann Institute of Science , Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.18981.031](https://doi.org/10.7554/eLife.18981.031)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Transcriptional rewiring over evolutionary timescales changes quantitative and qualitative properties of gene expression" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Naama Barkai as the Senior Editor and Reviewing Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Judith Berman (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As you will see below, the reviewers found your results highly interesting. The question of how transcription networks are rewired in evolution is fundamental, and your comprehensive analysis of the GAL system in Candida gives fascinating new insights into this model system. The reviewers therefore agreed that the manuscript provides an important contribution. Before publication, however, please revise the paper to account for the main comments:

1) Revisit the Cph1 findings more directly to explain previous findings.

2) Report growth phenotype of the Y. lipolytica rtg1 mutant.

3) Test whether GAL1/7/10 facilitate growth on GlcNAc.

4) Discuss possible implications of your study to Candida biology.

Reviewer #1:

Understanding how transcriptional networks evolve over time is a fundamentally important problem in biology. The authors provide a compelling and detailed example of how the GALactose utilization network of the pathogenic yeast Candida albicans differs from the well-characterized eukaryotic model network in the baker's yeast S. cerevisiae. Although differences between the regulation of these two networks were first characterized in 2007 by another lab (PMID: 17540568), it appears that the original paper may have only correctly identified half of the events. Specifically, the original study and the present study make it clear that the transcriptional activator Gal4 (and here also the co-repressor Gal80) do not regulate the GAL genes in C. albicans. In addition to showing that Gal4 regulated non-GAL targets in C. albicans, the original study identified Cph1 (the ortholog of Ste12) as the transcriptional activator of the GAL genes. In contrast, the present study identified Rtg1 and Rtg3 as GAL regulators by screening a library of transcription factor knockouts for genes whose removal eliminated galactose catabolism (in the presence of the respiration inhibitor Antimycin A). Both rtg1 and rtg3 deletions had strong phenotypic effects in this condition, while cph1 and gal4 deletions did not. Induction of a GAL1 reporter construct and a synthetic promoter containing Rtg1 and Rtg3 binding sites were shown to depend on functional RTG1 and/or RTG3. The present study also provides a much more thorough, precise, and quantitative characterization of the induction parameters of the C. albicans network than previous semi-quantitative studies published in 2007-2010 (which are properly cited here). Finally, by creating a rtg1 knockout in the early-diverging Saccharomycotina Yarrowia lipolytica, they provide evidence that Rtg1-mediated regulation of the GAL network is ancestral (although the quantitative effect of deletion is only 3-fold).

In general, this is study is a rigorous and exceptionally interesting contribution to our understanding of the evolution of transcriptional networks. Its reach will be extended because of the iconic status of the GAL network in molecular biology and because of previous evolutionary studies on this network. I found the inference (based on reporter gene expression in knockouts) that Gal1 may still play a signaling role that does not involve Gal4 and Gal80 particularly surprising. It may have interesting implications for how the downstream regulators switched, nicely setting the stage for future studies. Similarly, the result that GlcNAc may regulate galactose metabolism is thought provoking and will likely to be extended in future work. For this study, the most pertinent issues that should still be addressed are:

1) I think they owe it to the authors of the original study and the community to revisit some of the Cph1 findings more directly. The original study did not test growth of the cph1 knockout (as done here), but they did test its impact on a GAL10 reporter gene (here GAL1 was the reporter). The original study also deleted the putative Cph1 binding site and showed an effect. Did they actually unknowingly delete a Rtg1/Rtg3 binding site? Is it possible that Cph1 plays a quantitative but non-essential role in regulating GAL gene expression?

2) GEO and SRA accession numbers need to be provided.

3) The documentation of the statistical analyses and number of replicates is inadequate for a journal that prides itself on transparent reporting in this area. Generally speaking, statistical tests were reported, and the number of replicates appears "at least" two or three. In many cases, this may be because the authors feel the result is clear enough to trust, but in others (e.g. Figure 3C results with rtg3, see below), that is far from obvious. Even if there are limited numbers of replicates on the same day, there are ways to combine results across experiments done on different days. Non-parametric tests, such as Wilcoxon rank sum tests, may be particularly well suited since they do not make assumptions that are often violated in molecular biology studies.

Reviewer #1 (Additional data files and statistical comments):

See major comment #3 above.

Reviewer #2:

This is a very nice manuscript from the Johnson group that addresses the rewiring of the GAL1/7/10 genes in C. albicans. This issue has been addressed in prior studies almost a decade ago, but this paper extends the prior work with a comprehensive analysis of the transcription factors involved. Here, the C. albicans GAL1/7/10 genes are shown to be necessary for growth on galactose and to be important for formation of robust biofilms in a rat catheter model. They then identify two transcription factors Rtg1 and Rtg3 as the only two TFs that are required for growth on Galactose. They also show that the GAL promoter region and the RTG binding sites are required for the majority of GAL gene induction using GFP reporter assays.

An elegant competition experiment is performed with a high throughput flow cytometry assay that can measure GAL-GFP expression levels in S. cerevisiae and C. albicans with the C. albicans cells distinguished by an mCherry reporter. They detect the classic bimodal population of S. cerevisiae cells (in low Galactose with little or no glucose). In contrast, C. albicans expresses GAL genes earlier, and in a continuous manner. In addition, GAL gene transcription induction is higher as determined by RNA seq analysis. Two genes other than GAL1,7,10 are induced in both C. albicans and S. cerevisiae but we are not told which genes these are and it was not readily extracted from the supplementary tables.

They then show that the GAL1 control region is induced by GlcNAc and that the two Rtg1/3 binding sites are sufficient to drive most or all of this induction. GlcNAc was previously shown to activate GAL genes (Gunasekera et al), but this study adds the Rtg binding sites to the story. Nonetheless, it begs an important, unanswered question: Do GAL1/7/10 facilitate growth on GlcNAc? It seems that this experiment (growing Gal∆ strains on GlcNAc) would be simple to do and that it would allow consolidation of Figure 3C/D and Figure 6.

What is the source of galactose that cells must sense and metabolize or do these GAL genes also metabolize something else?

Along these lines, it would be useful to discuss why galactose metabolism is critical for growth as a biofilm? Is there a lot of GlcNAc in biofilms?

It also would be interesting to know if the three C. albicans GAL genes can function in S. cerevisiae. (This would be quite straightforward to do, as there are no CUG codons in any of the three genes.)

Finally, the authors connect the rewiring theme to Yarowia lipolytica – a very distant relative of C. albicans and S. cerevisiae and show that the only Rtg1-like gene in this organism is required for expression of GAL1. Here again, it would be interesting to know if the Y. lipolytica rtg1 mutant is also defective for growth on Galactose and on GlcNAc or other carbon sources.

Prior studies suggested the involvement of Cph1 or Rgt1 while these factors did not come out of the deletion library screens here. Why do the authors think that this is the case? Were very different alleles or assays used? Did the Cph1 and Rgt1 fall into the 104 colonies bin in figure 3B? Given that the experiments clearly show that Rtg1/Rtg3 are major, but not exclusive, regulators of the GAL1/7/10 genes, it would be useful to discuss the possible other mechanisms that regulate expression of these genes.

Reviewer #2 (Additional data files and statistical comments):

I think providing information about the other two genes that overlap between S. cerevisiae and C. albicans is essential. Determining if gal mutant cells have growth defects, other than not growing on galactose medium, would also provide biological context for the evolutionary results. Given that this rewiring of gal genes in general has been discussed in several other papers, this paper should extend the implications of the rewiring to the biology of the organisms.
