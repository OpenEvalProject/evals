# Peer review - Round 1

Editors:
- Karsten Weis, ETH Zurich Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.49708.sa1](https://doi.org/10.7554/eLife.49708.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Courel et al. use a variety of genomic datasets to examine the impact of nucleotide content (AU versus GC content) of human mRNAs upon their post-transcriptional fates. The results suggest that translational regulation applies predominantly to AU-rich transcripts, whereas high GC content correlates with mRNA decay as the major mode of regulation for such transcripts. While the cellular mechanism of how the nucleotide content of an mRNA is recognized remains unclear, all three reviewers found the results that are described in this paper interesting and important. The authors have addressed the key concerns during the revision, and the manuscript is now ready for publication.

Decision letter after peer review:

Thank you for submitting your article "GC content shapes mRNA storage and decay in human cells" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and James Manley as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

All three reviewers found the results described in this paper interesting and felt that the reported findings are in principle appropriate for publication in eLife. However, there were important concerns regarding the statistical methods that must be addressed. We note that the results are mainly correlative and causation was not established. As described below, the authors should test their model with specific reporter mRNAs with varying GC content.

Essential revisions:

1) There is a general issue of how the data are analyzed; almost every result is supported by correlation analysis (Spearman). First and foremost, the authors compare two different correlations many times, and attribute meaning to differences in the Spearman values – this is not appropriate, a statistical test is needed to establish whether two correlations are meaningfully different. Second, the authors use a wide range of adjectives (weak, strong, moderately etc) to describe and interpret correlations, the selection of these adjectives seems rhetorical rather than rigorous. Third, it would be helpful to justify (in the Materials and methods, perhaps) why Spearman rather than Pearson correlations are employed. Fourth, there are statements (e.g., subsections “PBs only accumulate AU‐rich mRNAs”; “The GC content of mRNAs shapes post‐transcriptional regulation”) that require associated statistical tests.

2) Relying on the GC content as the main basis for the conclusion could be problematic for the following reasons: a) There is a clear technical bias that connects GC content to observed transcript abundance as observed through RNAseq. This has been extensively documented (Benjamini et al., NAR 2012, for example), and has to do with the PCR amplification step at the end of almost every library construction protocol. This might not be problem with regards to the data produced by the authors, but they do use data, including CLIP data, from other sources. It can be difficult to be certain that such data is free of such biases. CLIP data may be particularly sensitive to this bias since due to the low amount of input material, a large number of PCR cycles are often required to make a library. b) GC content is not a standalone variable in the transcriptome. It is significantly correlated with a range of other variables, including transcript length (Marin et al. 2003, Yeast), expression (Kudla et al. 2006, PLOS Biology), and conservation (Litterman et al. 2019, Genome Res). Accordingly, all of these variables are correlated with each other. This makes it difficult to assign observed effects to just one of these variables. This is not to say that GC content is not playing a role, perhaps even a dominant one. However, it could be problematic to draw mechanistic conclusions from groups of correlations of metrics (GC, length) that are themselves prone to spurious correlations.

This could be disentangled through the use of reporter transcripts. For example, one could look at the P body localization, DDX6 sensitivity, etc. of long but GC-rich transcripts, short but GC-poor transcripts, and so on. This strategy could also be used to look at the relative contributions of CDS and 3' UTR sequences, since the GC content of the two in endogenous transcripts are correlated and thus also hard to disentangle.

3) The authors should speculate as to how they feel the GC-ness of an mRNA is 'measured' by the cell. Do they feel RNA secondary structure plays a role – in which case the authors could cross-compare with global assessments of RNA structure (e.g. Luu et al. 2016 Cell v165, p1267) Or could it be that the levels of specific amino-acylated tRNAs are critical? In which case the authors could compare to aa-tRNA levels (e.g. Evans et al., Cell v165 p1267). Or is there some other mechanism that the authors feel could be speculated upon?

4) The terminology used throughout the paper needs to more accurately reflect the experiments and data that have been evaluated. For instance- the authors use the terms mRNA stabilization and mRNA decay when describing analyses where steady state mRNA levels have been measured. They silence specific factors and measure steady state mRNA levels and talk about factor-dependent mRNA decay. They haven't at any point in the paper directly measured the rate of mRNA decay or the stability of an mRNA. In fact, the only experiment that touches upon this is the metaplot of reads across RNAs showing accumulations of 5' and 3' reads. Again, though this is not a direct measure. Another example of this is the assumption that polysome enrichment equates to translation rates. Once again translation or the rate of translation has never been measured in the paper. Instead the steady state levels of mRNA in polysome fractions has been measured and is used as a proxy for translation rates. While this is quite common in the general literature, at the very least the authors needs to explain the assumption and the potential for polysome enrichment due to inhibited translation elongation should be raised as a potential caveat.

5) Elements in the Discussion and the legend titles to individual parts of figures are often overstated and need to be looked at carefully – several examples are found throughout the text.
