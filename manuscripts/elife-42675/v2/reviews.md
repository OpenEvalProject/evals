# Peer review - Round 1

Editors:
- Bruce Edgar, University of Utah United States

Reviewers:
- Bart Deplancke, EPFL Switzerland

## Review text

DOI: [10.7554/eLife.42675.033](https://doi.org/10.7554/eLife.42675.033)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The Hox Transcription Factor Ubx stabilizes Lineage Commitment by Suppressing Cellular Plasticity" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Kevin Struhl as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Bart Deplancke (Reviewer #2).

The reviewers have discussed the reviews with one another, at length, and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Overall, the reviewers were enthusiastic about the subject and the approach, and they found the conclusions interesting and noteworthy. But as you can see from the reviews, which are appended in their entirety below, the reviewers also had substantial reservations about technical aspects of data collection and analysis. One simple issue that all the reviewers were concerned about was the lack of replicates for the ChIP experiments (3 replicates are standard), and they agreed that 2 or preferably 3 replicates should be performed and the data re-analyzed. A second general concern was the ChIP-PCR data indicating that Ubx controls H3 K27me3 distributions and Pho binding; in this case the reviewers agreed that the Pho ChIP samples +/- Ubx-deGrad (Figure 6) should be sequenced, to better substantiate your interesting conclusions using whole genome data. (In principle, the H3 K27me3 ChIP samples in Figure 6 should likewise be sequenced, though we leave it up to you to decide how important it is.) Thirdly, we would like to see a few changes to the data analysis, as described in the reviews, to bring into line with standards in the field. Clearly these additional experiments will require some investment, but we feel they are necessary to the bring to paper up to accepted standards in the field. We look forward to seeing your revision.

Reviewer #1:

The Lohmann lab presents an extremely complex analysis of the role of the Hox transcription factor Ubx in lineage commitment/specification in Drosophila. In order to remove Ubx from a given lineage only, they used a protein degradation method recently established and an endogenously tagged version of Ubx. The study is elegant in its design, and many of the discussed findings appear to provide interesting insight into the role of Ubx in the mesoderm, and possibly beyond.

However, for a non-expert in such genome-wide approaches, both the experimental and the analytical part of the work are difficult to analyse and evaluate in detail. In light of this fact, I have to admit that I found the work very interesting, timely and novel, and certainly of excellent quality and relevance to be published in eLife. Even after having read the paper three times, I have not seen any reason to ask for additional experiments.

Reviewer #2:

Using the INTACT nuclei isolation method coupled to comprehensive RNA-seq and ChIP-seq assays, Domsch and colleagues found that a Hox class transcription factor (TF) Ubx binds to both active genes and inactive genes linked to either the mesodermal or neuronal lineages. The authors therefore hypothesized that Ubx may function in tissue development as a repressor of alternative transcriptional programs (i.e. programs steering cells toward a distinct differentiation fate). To investigate this postulate, the authors studied the regulatory function of Ubx in different lineages by depleting this TF in a tissue-specific manner. These experiments revealed that a large proportion of alternate fate genes are upregulated once Ubx is removed, in line with their hypothesis. The authors further profiled the H3K27ac and H3K27me3 chromatin landscapes in Ubx-depleted tissues, which revealed that Ubx likely represses alternate fate genes by controlling their epigenomic status, especially K3K27me3 enrichment. Subsequent motif analysis and downstream experiments thereby showed that this repressive chromatin mark may be directed toward these loci through the regulator Pho, which is stabilized by Ubx at these repressed regions.

Together, this is a very interesting study that should be of broad interest to the gene regulation and developmental biology fields given the formulation of a novel mechanistic model that rationalizes how a broadly expressed TF is able to contribute to cell lineage specification by repressing alternate cell fate genes. The techniques applied, such as tissue-specific nuclei isolation, tissue specific Ubx gene tagging/depletion are elegant and state of the art and the resulting data seems in general solid. There are only a few items that could be clarified better:

1) The authors used 10 RPKM as their threshold to distinguish active from inactive genes. This is a rather high threshold, and so one is left to wonder what the consequence would be on the downstream analyses/results if the more standard threshold of 1 RPKM would be applied?

2) The authors show that Ubx binds to a very large number of genes (roughly 10 K based on Figure 2B, and thus >70% of all Drosophila (10 K / 14 K) can be considered to be Ubx targets). This raises a couple of questions:

a) In Figure 2B, the number of Ubx-bound genes in neuronal tissue at stages 14-17 is much lower than for the other three conditions. What could be the underlying reason?

b) In Figure 2G, the authors show that there is a high correlation in higher order GO terms between the lineage specific transcriptional and Ubx binding profiles. As a control, the authors included the TF Tinman, which revealed a more distinct GO term enrichment profile. However, since Ubx binds to such a large number of genes, is it not entirely expected that the majority of active genes will also be Ubx targets, and thus yield the same GO term enrichment profile? The same holds true for the inactive genes which also fall mostly within the "Ubx target space" and would thus again yield the same profile. That Tin does not yield the same profile is also not surprising given that it binds much fewer genes so the overlap between (in)active genes and Tin gene targets will be much smaller. A better control (if available) would in this regard be a TF that, similar to Ubx, binds to a large number (10 K) of genes. In its current configuration however, this analysis is not very informative. Similar concerns apply to the statements "Strikingly, 85% (1227/1452) of the genes with reduced and 90% (1299/1393) of the genes with increased expression were bound by Ubx in mesodermal nuclei in wild-type embryos, implying that most of the expression changes were a direct consequence of altered Ubx chromatin interactions". Again, since >70% of Drosophila genes are Ubx targets, 85-90% is in fact not very striking and could just be a statistical aberration. This needs to be addressed.

3) The proposed model, while informative, is too simplistic. This is because, in its current form, the model lacks information on what the factors / determinants are that mediate either tissue-specific activation or repression. The identification of these factors is likely beyond the scope of the current study, but perhaps some first layer data analysis on motifs (beyond the listed generic ones) could be performed. In addition, these additional layers need to be incorporated in the model because, as an example, the Ubx-Pho complex is shown to repress neuronal genes in the mesoderm given the enrichment of the Pho motif in these repressed genes. But why then, given that the same motif will obviously be present in the DNA of a neuronal cell, does Pho-Ubx not repress these same genes in a neuronal cell (also since both Pho and Ubx are ubiquitously expressed)? What makes that the Pho motif in a neuronal cell is read differently in a mesodermal cell and vice versa? The same reasoning can be followed for active genes in the respective cell types. At a minimum, such uncertainties should be represented in the model to clearly indicate what type of regulatory information is still missing.

Reviewer #3:

I have mixed responses to the paper by Domsch et al. On the one hand, the experimental design, to analyze Hox regulatory mechanisms in distinct embryonic tissues, seems at first glance important and exciting, I was less impressed with the analysis than I expected to be. My concerns fall in two categories:

1) Data generation and analysis.

For one, although replicates were analyzed for the RNA-seq experiments, it seems that all of the ChIP-seq datasets were only done once, without replicates. Given how noisy these type of data can be (especially when working with a small number of sorted cells and weak ChIP signals as in this case) I think it is imperative to compare at least two experimental replicates and use peak calling algorithms that require two independent datasets to assess statistical relevance. The Venn diagrams in Figure 2—figure supplement 1 for example suggest that there are ~14,000 (!) Ubx peaks in the mesoderm and that more than 7000 of these are mesoderm-specific. These numbers are quite striking but as it stands it is not possible to know how solid they are without replicate datasets and rigorous statistical tests.

I also wonder about the way the authors subtract input ChIP signals from their experimental IPs, as this is an analysis method that is not typically seen in the literature. I would like to see how noisy the input IPs are -- those tracks should be shown.

There is little validation of the ChIP peaks. The only known enhancer that was highlighted was one from Dpp.

The Pho co-IP signal is surprisingly weak given the mechanism of co-recruitment that the authors are proposing.

GAGA-like motifs are often observed by motif discovery algorithms and I am not convinced they are meaningful here given the lack of solid follow up evidence.

One potential strength of the paper is the claim that Pho binding and K27me3 depends on Ubx binding. However, this conclusion is based on a small handful of loci analyzed by qPCR and the differences are small. Further, given that the Pc system can have very specific targets, I think that calculating the ratio of K27me3/K27ac can be misleading. Better to treat these marks independently, since when one is lower it isn't necessarily the case that the other will be higher. It is also the case that Pho binding is not equivalent to K27me3; the latter could simply be a consequence of whether the gene is repressed, which may or may not occur in a Pho-dependent manner.

Many genes lose expression in the Ubx knockdown experiments, suggesting that Ubx also acts as an activator in the mesoderm, but this is not adequately discussed or studied in the paper. It is not clear why the authors choose to focus on the repressed genes.

2) General comments.

Ubx, and Hox genes in general, are well studied transcription factors that are known to be important in multiple cell types including mesoderm, the nervous system, and epithelium. So, seeing lots of genes change their expression when a broadly used transcription factor like Ubx is knocked down. It is also not surprising that the genes differ depending on the tissue (thus the GO analyses done in this paper seems rather trivial). What would take the analyses beyond what is known already is to understand how Ubx carries out differential functions in these two (and other) tissues. Presumably this happens in conjunction with tissue specific factors (e.g. twist for the mesoderm). The role of lineage specific factors, however, is not addressed and only marginally mentioned in the paper.

Terms such as "Cell plasticity" and "lineage restriction" are used rather loosely. The authors show that many up-regulated genes after Ubx knockdown are expressed in other lineages, but this result would have to be the case when a TF that represses genes is removed. There is no hard-evidence of lineage conversion (like loss of mesodermal master-regulatory factors for example), nor is it clear why neuronal (as opposed to endodermal or epithelial genes) genes are the focus here. It seems that the analysis is artificially restricted to repressed neuronal genes, while a more unbiased analysis of the changes that occur would be more valuable.
