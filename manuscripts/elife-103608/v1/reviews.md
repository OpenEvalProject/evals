# Peer review - Round 1

Editors:
- Detlef Weigel, Max Planck Institute for Biology Tübingen Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.103608.3.sa0](https://doi.org/10.7554/eLife.103608.3.sa0)

The authors present a software (TEKRABber) to analyze how expression of transposable elements (TEs) and TE silencing factors KRAB zinc finger (KRAB-ZNF) genes are correlated in experimentally validated datasets. TEKRABber is used to reconstruct regulatory networks of KRAB-ZNFs and TEs during human brain evolution and in Alzheimer's disease. The direction of the work is important, with potentially significant interest from others looking for a tool for correlative gene expression analysis across individual genomes and species. However, the reviews identified biases and shortcomings in the pipeline that could lead to an unacceptable number of false positive and negative signals and thus impact the conclusions, leaving the work in its current form incomplete.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.103608.3.sa1](https://doi.org/10.7554/eLife.103608.3.sa1)

The authors present their new bioinformatic tool called TEKRABber, and use it to correlate expression between KRAB ZNFs and TEs across different brain tissues, and across species. While the aims of the authors are clear and there would be significant interest from other researchers in the field for a program that can do such correlative gene expression analysis across individual genomes and species, the presented approach and work display significant shortcomings. In the current state of the analysis pipeline, the biases and shortcomings mentioned below, for which I have seen no proof of that they are accounted for by the authors, are severely impacting the presented results and conclusions. It is therefore essential that the points below are addressed, involving significant changes in the TEKRABber progamm as well as the analysis pipeline, to prevent the identification of false positive and negative signals, that would severely affect the conclusions one can raise about the analysis.

My main concerns are provided below:

One important shortcoming of the biocomputational approach is that most TEs are not actually expressed, and others (Alus) are not a proxy of the activity of the TE class at all. I will explain: While specific TE classes can act as (species-specific) promoters for genes (such as LTRs) or are expressed as TE derived transcripts (LINEs, SVAs), the majority of other older TE classes do not have such behavior and are either neutral to the genome or may have some enhancer activity as mapped in the program they refer to 'TEffectR'. A big focus is on Alus, but Alus contribute to a transcriptome in a different way too: They often become part of transcripts due to alternative splicing. As such, the presence of Alu derived transcripts is not a proxy for the expression/activity of the Alu class, but rather a result of some Alus being part of gene transcripts (see also next point). Bottom line is that the TEKRABber software/approach is heavily prone to picking up both false positives (TEs being part of transcribed loci) and false negatives (TEs not producing any transcripts at all) , which has a big implication for how reads from TEs as done in this study should be interpreted: The TE expression used to correlate the KRAB ZNF expression is simply not representing the species-specific influences of TEs where the authors are after.

With the strategy as described, a lot of TE expression is misinterpreted: TEs can be part of gene-derived transcripts due to alternative splicing (often happens for Alus) or as a result of the TE being present in an inefficiently spliced out intron (happens a lot) which leads to TE-derived reads as a result of that TE being part of that intron, rather than that TE being actively expressed. As a result, the data as analysed is not reliably indicating the expression of TEs (as the authors intend too) and should be filtered for any reads that are coming from the above scenarios: These reads have nothing to do with KRAB ZNF control, and are not representing actively expressed TEs and therefore should be removed. Given that from my lab's experience in brain (and other) tissues, the proportion of RNA sequencing reads that are actually derived from active TEs is a stark minority compared to reads derived from TEs that happen to be in any of the many transcribed loci, applying this filtering is expected to have a huge impact on the results and conclusions of this study.

Another potential problem that I don't see addressed is that due to the high level of similarity of the many hundreds of KRAB ZNF genes in primates and the reads derived from them, and the inaccurate annotations of many KZNFs in non-human genomes, the expression data derived from RNA-seq datasets cannot be simply used to plot KZNF expression values, without significant work and manual curation to safeguard proper cross species ortholog-annotation: The work of Thomas and Schneider (2011) has studied this in great detail but genome-assemblies of non-human primates tend to be highly inaccurate in appointing the right ortholog of human ZNF genes. The problem becomes even bigger when RNA-sequencing reads are analyzed: RNA-sequencing reads from a human ZNF that emerged in great apes by duplication from an older parental gene (we have a decent number of those in the human genome) may be mapped to that older parental gene in Macaque genome: So, the expression of human-specific ZNF-B, that derived from the parental ZNF-A, is likely to be compared in their DESeq to the expression of ZNF-A in Macaque RNA-seq data. In other words, without a significant amount of manual curation, the DE-seq analysis is prone to lead to false comparisons which make the stategy and KRABber software approach described highly biased and unreliable.

There is no doubt that there are differences in expression and activity of KRAB-ZNFs and TEs repspectively that may have had important evolutionary consequences. However, because all of the network analyses in this paper rely on the analyses of RNA-seq data and the processing through the TE-KRABber software with the shortcomings and potential biases that I mentioned above, I need to emphasize that the results and conclusions are likely to be significantly different if the appropriate measures are taken to get more accurate and curated TE and KRAB ZNF expression data.

Finally, there are some minor but important notes I want to share:

The association with certain variations in ZNF genes with neurological disorders such as AD, as reported in the introduction is not entirely convincing without further functional support. Such associations could be merely happen by chance, given the high number of ZNF genes in the human genome and the high chance that variations in these loci happen associate with certatin disease associated traits. So using these associations as an argument that changes in TEs and KRAB ZNF networks are important for diseases like AD should be used with much more caution.

There is a number of papers where KRAB ZNF and TE expression are analysed in parallel in human brain tissues. So the novelty of that aspect of the presented study may be limited.

Additional note after reviewing the revised version of the manuscript:

After reviewing the revised version of the manuscript, my criticism and concerns with this study are still evenly high and unchanged. To clarify, the revised version did not differ in essence from the original version; it seems that unfortunately, no efforts were taken to address the concerns raised on the original version of the manuscript, the results section as well as the discussion section are virtually unchanged.
