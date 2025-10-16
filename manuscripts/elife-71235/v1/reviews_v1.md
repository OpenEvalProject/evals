# Peer review - Round 1

Editors:
- Mashaal Sohail, https://ror.org/01tmp8f25 National Autonomous University of Mexico Mexico

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71235.sa0](https://doi.org/10.7554/eLife.71235.sa0)

A genetic haplotype on chromosome 3 that entered the human lineage from mating with Neanderthals has previously been implicated as a strong genetic risk factor for severe COVID-19 outcomes. This study uses population genetics and functional genomics tools along with experimental assays to assess the genetic variants in these regions for their likelihood of driving the severe COVID-19 phenotype. They ultimately identify 4 (out of about 600) variants as strong functional candidates. This study is a valuable contribution to the interaction between host genomics and COVID-19 outcomes and provides compelling evidence allowing for more targeted future functional investigations.


---

# Peer review - Round 1

Editors:
- Mashaal Sohail, https://ror.org/01tmp8f25 National Autonomous University of Mexico Mexico

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71235.sa1](https://doi.org/10.7554/eLife.71235.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Regulatory dissection of the severe COVID-19 risk locus introgressed by Neanderthals" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Molly Przeworski as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

All reviewers agree that the topic of the paper, identifying genetic features that contribute to covid-19 severity in a neanderthal introgressed region, is of general interest and the authors impressively combine various annotation and functional assessments of the variants. However, there are a range of concerns about the experimental and functional genomics evidence presented, leading to the conclusion that whether chemokine receptor expression is linked to the clinical phenotype remains unaddressed by the study. The majors concerns are:

(1) The first concern is the assumption that regulation of GFP expression under a minimal promoter correlates perfectly with regulation of CCR1 and CCR5 under their native promoter. The authors could simply address this in the text, but this will not address the underlying issue. Preferably, having narrowed their regions of interest down to 4 emVars, they would place these on a reporter construct with GFP under control of the CCR1 or CCR5 promoters (or a minimal section of these specific promoters) and repeat either their quantitative PCR analysis or, in this case, a fluorescence-based assay may suffice. This would greatly strengthen the argument that CCR1 and CCR5 are specifically regulated by these emVars. If they believe that an infectious context might change these results, they could conduct this reporter assay during viral infection using viruses that do not require BSL3 containment, or collaborate with a lab able to use SARS-CoV-2.

(2) The second issue is, as acknowledged by the authors, that the emVars they identify using computational approaches are downregulatory whereas CCR1 and CCR5 are upregulated during severe COVID-19. The authors included some speculation about how these regulatory regions might still be linked to upregulation of the chemokine receptors in a clinical context, but this closing section of the manuscript isn't very strong. The assay described above would be informative as to whether these emVars do in fact downregulate CCR1 and CCR5, and whether they do so during infection. As a further suggestion to address the discrepancy between clinical gene expression data and their MPRA data, the authors could perform the conventional reporter assay (such as luciferase assay) in epithelial or macrophage cell lines (not K562). At least they might want to test the four variants they highlighted in the manuscript.

(3) Enhancer activity should be defined in a relative manner, by comparing to the background activity of negative control sequences.

(4) The authors should propose the molecular mechanisms of the SNPs' function that underlie COVID19 severity. For example, the authors could perform TF motif search around the potential causative SNPs they found, see if the SNPs alter the TF motifs, and see if the alteration of the TF motifs can explain the eQTL effect direction.

Reviewer #1 (Recommendations for the authors):

There are, in my opinion, two primary weaknesses of the paper. The first is the assumption that regulation of GFP expression under a minimal promoter correlates perfectly with regulation of CCR1 and CCR5 under their native promoter. The authors could simply address this in the text, but this will not address the underlying issue. Preferably, having narrowed their regions of interest down to 4 emVars, they would place these on a reporter construct with GFP under control of the CCR1 or CCR5 promoters (or a minimal section of these specific promoters) and repeat either their quantitative PCR analysis or, in this case, a fluorescence-based assay may suffice. This would greatly strengthen the argument that CCR1 and CCR5 are specifically regulated by these emVars.

If they believe that an infectious context might change these results, they could conduct this reporter assay during viral infection using viruses that do not require BSL3 containment, or collaborate with a lab able to use SARS-CoV-2.

The second issues is, as acknowledged by the authors, that the emVars they identify using computational approaches are downregulatory whereas CCR1 and CCR5 are upregulated during severe COVID-19. The authors included some speculation about how these regulatory regions might still be linked to upregulation of the chemokine receptors in a clinical context, but this closing section of the manuscript isn't very strong. The assay described above would be informative as to whether these emVars do in fact downregulate CCR1 and CCR5, and whether they do so during infection. Depending on the results the authors may not need the very speculative hypothesis at the end of the paper.

Reviewer #2 (Recommendations for the authors):

1. The authors defined the activity of enhancers based on the log fold change (LFC) between barcode counts in cDNA comparing to those in plasmid library (p<0.01). With this definition, they claimed that 53% of the tested sequences had enhancer activity (Figure 2D). However, I do not think such absolute values (i.e. LFC cDNA count/pDNA count, p>0.01) can be considered as "activity" of enhancers. Rather, enhancer activity should be defied in a relative manner, by comparing to the background activity of negative control sequences. For example, Inoue et al. (Cell Stem Cell, 2019) identified active enhancers whose activity significantly deviated from that of the negative control sequences. Moreover, in the most case of traditional luciferase assays, researchers specify the activity of enhancers relative to that of a negative control (e.g. empty vectors etc.). Hence, I would like the authors to provide and visualize the following information:

(1) How many sequences (or what fraction) show significantly higher barcode expression (LFC cDNA/pDNA) than negative controls? These should be considered as "active enhancers", and the distribution of these relative activities can be visualized with a violin (or box) plot, comparing to the activity of negative and positive controls.

(2) Do these "active enhancers" significantly overlap with enhancer epigenetic marks (chromHMM enhancers, DHS, and worth including H3K27ac). It is similar to Figure 3B, but I expect the result will be improved.

(3) How many emVars fall into the "active enhancers"? Do the four eQTLs that are linked with CCR1/5 overlap with "active enhancers"? emVars that are not overlap with "active enhancers" should be less important, because the differential expression between the two alleles should be within the range of background noise.

2. The authors systematically identified potential candidates of causative SNPs associated with COVID19 severity, while previous GWAS only found a tag SNP. These findings could be much strengthened and warranted if the authors propose the molecular mechanisms of the SNPs' function that underlie COVID19 severity. For example, the authors could perform TF motif search around the potential causative SNPs they found, see if the SNPs alter the TF motifs, and see if the alteration of the TF motifs can explain the eQTL effect direction. They could further test if overexpression/knockdown of the candidate TFs affect CCR1/5 expression.

Reviewer #3 (Recommendations for the authors):

1. Schematic representation of computational analysis overview (like Vosa et al. 2018 Figure 1) would be helpful to understand the analysis flow and MPRA experiment design.

Computational analysis parts in the manuscript are descriptive and hard to follow up. Also, some important SNPs (rs13063635 and rs13098911) are not indicated in figure 1.

If rs13063635 and rs13098911 are in the same region shown in Figure 1, the author should indicate the position.

2. Now author narrowed down the four critical variants. To filling the gap of the discrepancy between clinical gene expression data and their MPRA data, this reviewer suggests the conventional reporter assay (such as luciferase assay) in epithelial or macrophage cell lines (not K562).

At least they might want to test the four variants they highlighted in the manuscript.

3. Hypothesis described in the discussion page #2 line 15~ is obscure and not great for the conclusion. Please make it clear.

4. This reviewer is curious if there are any common transcription factor binding sites around the 20 critical variants. If the author has any data of TF motif analysis would be nice as an additional figure.
