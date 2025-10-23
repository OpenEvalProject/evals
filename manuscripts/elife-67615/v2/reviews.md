# Peer review - Round 1

Editors:
- George H Perry, Pennsylvania State University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67615.sa1](https://doi.org/10.7554/eLife.67615.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

The technical challenges of identifying and quantifying the frequency of structural variants (SV) on a population scale has been a major limitation to the study of recent human adaptation. This manuscript applies a recent graph-based genotyping method that leverages a library of SVs identified by long-read sequencing to identify SVs in large short-read based cohorts. This is a sensible and powerful approach that highlights several examples of likely adaptive SV evolution in different human populations.

Decision letter after peer review:

Thank you for submitting your article "Local adaptation and archaic introgression shape global diversity at human structural variant loci" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by George Perry as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Clearer connection and contextualization of the contribution of this work given previous studies, both for the SV catalog of results and the highlighted IGH, including analyses of overlap with previous datasets and a clearer set up to enable this paper to serve a larger purpose as a roadmap for future studies that aim to link datasets for SVs. Related to this, the language in a number of sections is unclear or too broad to scientifically interpret, e.g. suggesting analyses are broadly consistent with previous work; specific quantitative comparisons are needed to make or interpret these claims.

2) More depth to the biological interpretation of the study, with specific ideas presented below, including further support/interpretation of the IGH locus and potential tests of SV patterns more broadly.

Reviewer #2 (Recommendations for the authors):

1. The authors do a good job motivating the importance of SVs in human evolution and the previous technical limitations that have limited comprehensive analysis. They also clearly motivate their work using recently generated population-level SV datasets. However, clarification of how this paper's results compare to and expand these previous findings is needed. Previous analyses of SV evolution were not "comprehensive" due to the limitations of short-read approaches. However, as noted by the authors, this and other long-read-based studies also currently cannot "comprehensively" study human SV. I do not see a problem with the "focus on individual variants" obtained in a different way, but more description of how their set of SVs is similar or different from previous work would aid interpretation. A few more supplementary figures describing characteristics of the 92,286 SVs used for downstream analysis (length, type of SV, genome distribution, SV overlap, frequency, etc) are needed. Even though they are already cited, some papers the authors could consider further contextualizing their results in include: Hsieh et al., 2019., Sudmant et al., 2015, Almarri et al., 2020, Ebert et al., 2020, Audano et al., 2019 (there are also others that consider SV with direct reference to introgression events).

2. Related to the above point, the use of the graph genotyping software, Paragraph, is s sensible approach, and I suspect that this paper may provide a template for future analyses merging long-read and short-read SV data. Given this potential contribution, more should be done to discuss the benefits and limitations of this approach. There is brief discussion of "ascertainment bias" based on the 15 individuals with long-read data used from Audano et al., 2019. How does the ancestry of these 15 individuals influence the ability to comprehensively identify SVs in thousands of individuals with different ancestries? A few more details in the main text regarding the sensitivity and specificity of Paragraph would also help to aid result interpretation (rather than just "recent benchmarking…support the accuracy of Paragraph"). Does the Paragraph approach better identify longer SVs, deletions, duplications, inversions, SVs in more repetitive regions of the genome?

3. The authors identify 1121 significant associations between SVs and the expression of nearby genes in LCLs. This analysis is reasonable and clear, but the implications are not clear. Prior to this section, the authors discuss LD with previously investigated SNPs/indels, yet they do not report this information for the eQTL 1121 SVs. How many of these 1121 are in high LD with common SNPs/indels? And how many are not linked to previously investigated variation? Even if most are linked, this is still potentially interesting, but it would be helpful to know if they are identified as eQTL in other datasets (GTEx?). Do these potentially SV mediated eQTL have greater effect sizes than eQTL caused by SNVs? Is there a way to fine map one or two (potentially one related to the subsequently immunoglobulin story or the ones highlighted in Figure 2C) to show that the SV is likely driving the association, rather than other linked variants?

4. The authors use Ohana to test for local adaptation. This method seems appropriate for the challenges of the SV data; the results are interesting; and I appreciate their new individual examples. However, these results are largely descriptive. Testing larger hypotheses about whether SVs are targets of selection more often than SNVs or if these patterns differ between populations or parts of the genome would substantially increase the impact of these results. Figure 4-S1 may be relevant to this kind of comparison; however, it only shows a few loci. While differences in power and ascertainment may make direct comparison challenging, I encourage the authors to think about how to move beyond a list of examples to more general conclusions. Additionally, the y-axis range on Figure 4 across the different ancestries are quite different. It is hard to interpret to the significance and magnitude of the LRS. Can the multiple testing control be integrated here?

5. Finally, the authors explore one example, the immunoglobulin heavy chain locus, in detail. The example and analysis are compelling; however, it is complicated and sometimes hard to follow given the multiple SVs in this region. Readers would benefit from a cartoon schematic of this locus, perhaps expanding on the supplemental figure. I would also appreciate more discussion of why this region might have been filtered out in Browning et al., 2018.

Reviewer #3 (Recommendations for the authors):

The abstract and introduction focus on the size of SVs and the relative "ease" of analysis of SNVs and indels, however, the highlighted variants are indels by the 1000 genomes definition. They also seem to have been discovered in other short-read datasets, (e.g. gnomAD).

Paragraph has been previously shown to work well for genotyping SVs, however it is not clear what the accuracy in the low-coverage 1000 genomes samples is. After filtering, while 92,286 variants remain, 25,201 (27%) of these are absent from any of the 1000 genomes samples. It is unclear how the authors distinguish "true negatives" from "false negatives."

I don't think the LD section adds anything new. This is well reported.

And LD cutoff of 0.5 R2 is used for introgressed haplotypes versus 0.82 for tag haplotypes in the original motivation. Suggest picking one to be consistent throughout.
