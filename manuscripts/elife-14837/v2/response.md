# Author response - Round 1

Authors:
- Manon Torres
- Denis Becquet
- Marie-Pierre Blanchard
- Séverine Guillen
- Bénédicte Boyer
- Mathias Moreno
- Jean-Louis Franc ([ORCID: 0000-0002-2900-5468](https://orcid.org/0000-0002-2900-5468))
- Anne-Marie François-Bellan ([ORCID: 0000-0002-3278-4642](https://orcid.org/0000-0002-3278-4642))

## Response text

DOI: [10.7554/eLife.14837.027](https://doi.org/10.7554/eLife.14837.027)

Essential revisions:

A loss of function experiment to show that the IRAlu-GFP reporter does not cycle when paraspeckles are disrupted.

As suggested we performed new experiments to show that rhythmic nuclear versus cytoplasmic egfp mRNA in IRAlu-egfp cell line depends upon the presence of paraspeckles. Given the unique Neat1 RNA nuclear localization, RNA knockdown is more convenient than paraspeckle protein depletion for investigating paraspeckle function. Furthermore since there is an essentially perfect relationship between loss of paraspeckles and depletion of Neat1 RNA (Clemson et al., 2009), we addressed this issue by using Neat1 siRNA and Neat1 antisens oligonucleotides (ASO). By RT-qPCR we showed that Neat1 RNA levels were reduced in IRAlu-egfp cell line to around 60% after treatment with specific siRNA compared to negative control siRNA (Figure 5—figure supplement 1). The reduction we obtained in Neat1 RNA levels using siRNA is modest but comparable to that reported in human Hela cells (Clemson et al., 2009; Gagnon et al., 2014) and since in FISH experiments we do not find evidence for Neat1 RNA in the cytoplasm, this is consistent with other findings that RNA inhibition using siRNA can effectively occur in the nucleus (Langlois et al., 2005; Robb et al., 2005; Valgardsdottir et al., 2005; Clemson et al., 2009; Gagnon et al., 2014). Furthermore, the decrease in Neat1 RNA levels was not amplified when we used Neat1 ASO to disrupt paraspeckles siRNA (Figure 5—figure supplement 1). In any case, treatment with Neat1 siRNA and Neat1 ASO disrupts the circadian expression pattern of Neat1 RNA siRNA (Figure 5—figure supplement 1). More importantly, when IRAlu-egfp cells were transfected either by Neat1 siRNA or Neat1 ASO as compared to negative control, the relative ratio of nuclear versus cytoplasmic egfp mRNA levels was significantly decreased (Figure 5B) and the circadian egfp nuclear retention was abolished (Figure 5C). These loss of function experiments showed that the egfp mRNA nuclear retention in IRAlu-egfp cell line does not cycle when paraspeckles are disrupted.

The results are reported in the paragraph 3.5 added in the Results section and discussed in the Discussion section.

A genome wide approach should be used to determine whether known cycling transcripts are associated with paraspeckles.

As suggested, we performed a genome wide approach by deep sequencing the RNA brought down in Neat1 RNA pull-down using anti-sense oligonucleotides. We used the Tophat/Cufflinks pipeline (Trapnell et al., 2012) and only transcripts which exhibited values of fragment per kilobase per million of mapped reads (FPKM) higher than 1 were taken into account. The specificity of Neat 1 RNA pull-down was assessed by crossing the FPKM>1-limited lists obtained with the two specific oligonucleotides. This allowed us to provide a list of genes that were specifically associated to Neat1 RNA (see paragraph 4.1 in Results section and Figure 6—source data 1). All the RNA sequencing data have been registered at Gene Expression Omnibus (GEO) (accession no. GSE81972) and the following link has been created to allow review of record GSE81972 while it remains in private status: http://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?token=ytwjsuuyppgpzmn&acc=GSE81972

We then used publicly available datasets and crossed them with our dataset. This allowed us to determine that near 19% of pituitary circadian transcripts (Hughes et al., 2007) and 27% of post-transcriptional circadian genes in the liver (Menet et al., 2012) are found associated with paraspeckles. Taking into account that rhythmic circadian genes are tissue specific and that it is unfavorable to compare datasets obtained in two different species, the robust overlap we found between our gene list and that of Hughes 2007 and Menet 2012 allows to propose that paraspeckles play a relevant role in circadian gene expression. These results have been described in the paragraph 4.2 of the Results section, illustrated in Figure 6A and discussed in the last paragraph of the Discussion section entitled “Contribution of paraspeckle nuclear retention to circadian gene expression”.

Test a few additional genes in the in vitro system by comparing RNA levels between nucleoplasm and cytoplasm.

We took advantage of our crossing analysis described above to select a few genes common to our dataset and the publicly available datasets cited above. We showed that the nuclear versus cytoplasmic mRNA ratio of these genes displayed a circadian expression pattern that is abolished when paraspeckles were disrupted either by Neat1 siRNA or by Neat1 ASO (see Figure 6B-D, Figure 6—figure supplement 1 and Figure 6—source data 2). These losses of function experiments clearly show that paraspeckle retention of these few genes contributes to their circadian rhythmicity. These results have been described in the paragraph 4.3 of the Results section, illustrated in Figure 6B-D, Figure 6—figure supplement 1 and Figure 6-source data 2) and discussed in the last paragraph of the Discussion section entitled “Contribution of paraspeckle nuclear retention to circadian gene expression.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

In the discussion following their reviews, the reviewers agree that there are serious concerns about the Neat1 pulldown, which lacks controls. They feel that you must include a negative control in their genome-wide analysis. Possibly you have generated the data already, but did not include it in the revised version for whatever reason.

Thus, to summarize, this manuscript describes new important mechanisms that contribute to rhythmic mRNA expression, but has some problems. Addressing them (especially Neat1 pulldown controls) are necessary for publication. This should be feasible without doing any new experiments.

As noted by Reviewer #3, a non-specific oligonucleotide was actually included as negative control in our Neat1 RNA pull-down. This was indicated in the Materials and methods section and in the Results section (Figure 4F and Figure 4—figure supplement 2). This control allows to identify artifacts caused by direct, non-specific binding that are common to all affinity purification techniques. However, when performing RNA sequencing analysis, as already mentioned in our article (Results section, “Libraries were generated from the purified RNAs obtained with the two specific oligonucleotides but no library could be obtained with the non-specific oligonucleotide due to the too small quantity of material recovered”), the amount of RNA obtained with non-specific oligonucleotide was too low to generate a library. This attempt to generate a library after non-specific oligonucleotide was tried out three times without success, attesting that in our experimental conditions, direct non-specific binding of endogenous transcripts to the beads is very low.

One other source of artifacts that is more specific to hybridization capture approach is caused by hybridization events in which the capture-oligonucleotide directly hybridizes to an off-target RNA. As discussed by (Simon, 2015), an alternative method that controls for off-target RNA is to use two independent capture oligonucleotides that bind the target RNA. Specific signals are expected to be found with both oligonucleotides whereas signals that are found with only one oligonucleotide are interpreted as hybridization-induced artifacts. In our paper, we assessed the specificity of Neat 1 RNA pull-down by crossing the FPKM>1-limited lists obtained with two specific oligonucleotides.

Although the very low amounts of RNA obtained with non-specific oligonucleotide did not allow generation of library and RNA sequencing as explained above, they were still measurable by very sensitive qPCR technology in spite of very high Ct values. Thereby to convincingly show that transcripts from Neat1 RNA pull-down sequencing are specific Neat1 RNA targets, we verified by qPCR the specific association of a few of them with Neat1. To this end, we determined for the seven mRNA already selected in our paper, the enrichment obtained after Neat1 RNA pull-down with the two specific biotinylated complementary oligonucleotides that target Neat1 compared to the biotinylated irrelevant probe. As reported in the Results section and shown in a new figure supplement (Figure 6—figure supplement 1), the seven selected genes were significantly enriched after Neat1 RNA pull-down by the two specific probes compared to the non-specific probe.

Reviewer #3:

In this revised version, the authors addressed the reviewer's comments and provided additional data aiming at demonstrating that paraspeckles contribute to rhythmic gene expression at the post-transcriptional level in a pituitary cell line. In particular, the authors now include new results showing that disruption of the paraspeckles in a IRAlu-egfp cell line (using either siRNA or antisense oligonucleotides) decreases the ratio of nuclear vs. cytoplasmic egfp mRNA and impairs the rhythmic nuclear retention of egfp mRNA (Figure 5B, C) in this cell line. The authors also show similar data for several endogenous genes (Canx, Fkbp4 and Calr; Figure 6B-D; 4 other genes in supplementary data). While these data tend to overall support the author's conclusions, they also bring some concerns:

1) Why do six out of the seven genes exhibit in control conditions a rhythm with a period of about 20 hours?

2) Why are the effects on expression different between the siRNA and the antisense oligonucleotide?

3) Why are the phases of the nuclear/cytoplasmic mRNA ratio different between many of the genes (e.g., there is a 8-hr difference between Fkbp4 and Calr, Figure 6B)? The model proposed by the authors would suggest that the nuclear retention is at its lowest for all genes when the number of paraspeckles is at its minimum, i.e., 15-hrs after medium change.

In the experimental design of our study, measures are performed every 4 hours. The reviewer is right to state that this time interval does not allow determining the precise value of the period and phase of the rhythm, but this was not the aim of the experiment. Our purpose was to test whether or not the seven selected genes exhibited a circadian nuclear retention (by definition with a period comprised between 20h and 28h), and whether the minimum value of this rhythm occurred roughly when the levels of paraspeckle protein components and Neat1 RNA were the lowest. We indeed found for the seven selected genes 1/ that the relative mRNA ratio between nucleoplasm and cytoplasm over the time can be fitted by a sine wave curve with a R squared > 0.55 attesting its circadian nature and 2/ that the rhythms were approximately in phase with paraspeckle component rhythms. Furthermore, while having different effects on expression levels, we also found that both siRNA and antisense oligonucleotides were able to disrupt these rhythms attesting that paraspeckles are involved in the circadian nuclear retention of these mRNA.
