# Peer review - Round 1

Editors:
- Jessica K Tyler, Weill Cornell Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70878.sa0](https://doi.org/10.7554/eLife.70878.sa0)

Transcription factors (TFs) bind to the DNA in a sequence-specific manner at TF binding sites (TFBSs) to control gene transcription. Hence, characterizing how TFs interact with DNA is key to uncover how gene regulation occurs and how this process can be disrupted in diseases. While the binding properties of a large portion of human TFs are well characterized, a remaining challenge lies in our knowledge of how TFs interact cooperatively at regulatory elements, either forming dimers or co-binding the same regions. In this manuscript, Shen et al. explored spacing patterns between TFBSs using previously published data sets and revealed that the dominant pattern is a relaxed range of spacing between collaborative factors and tolerance for InDels that change the TFBS spacing.


---

# Peer review - Round 1

Editors:
- Jessica K Tyler, Weill Cornell Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70878.sa1](https://doi.org/10.7554/eLife.70878.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Natural genetic variation affecting transcription factor spacing at regulatory regions is generally well tolerated" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, including Chris P Ponting as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

The question under study without doubt is important and the natural experiment approach has several strengths. Nevertheless, both reviewers would have been more persuaded of its conclusions if large-scale experimental validations could have been reported and if these conclusions were generalized to other TFs and systems. A large number of methodological and statistical questions were also raised that together reduced the enthusiasm of the reviewers for publication. We hope that the comments provided below are helpful to you when you consider how and when to submit this work for publication.

Reviewer #1:

This manuscript by Shen et al. exploits pre-existing data (Link et al., 2018a; Keane et al., 2011) to explore whether InDels observed among 5 diverse mouse strains alter transcription factor binding affinity, using the PU.1 and C/EBPβ LDTFs as paradigm.

These wholly computational analyses provide evidence that affinities of "co-binding sites" correlate poorly with their spacing. Variants lying in PWMs alter affinity for their cognate factor, but also the co-binding factor, but the authors propose that there is little change in affinity resulting from spacing changes between them. This conclusion is drawn from indirect observations: (a) "co-binding" is never demonstrated, rather inferred from close proximity of ChIP-seq peaks, (b) changes in effect sizes (Table 1) following filtering with collaborative or unrelated factors, although whether these results are statistically robust requires further clarity.

The study would have benefited from the results drawn from the "natural experiments" being then validated experimentally, for example using reporter assays in cells whose TF spacing has been changed. Overall, its results were highly correlative, and provided little in the way of substantive novel observations.

Issues:

(i) line 201 "The remaining sites with InDels between PU.1 and C/EBPβ motifs, which should represent a clean set of spacing alterations, showed a diminished effect on TF binding (Table 1 "filtered by collabor. factors"; Figure 3D)." I'm unsure whether this is true, or else whether the change in significance (p-value Table 1) reflects the change in number of binding regions being considered. Similarly, the H3K27ac analysis referred to on line 232. Please comment on whether these effect size differences are significant.

(ii) Figure 5 does not provide new findings that are sufficient to merit having a Main Figure. Figure 5A. This analysis should be repeated with a more sensitive local aligner, e.g. LASTZ. Panel A simply reflects a technical effect (that of altered gap penalties) rather than any biological phenomenon (similarly Figure Supplements) and panels 5B,C illustrate one example, rather than a generalizable phenomenon.

Reviewer #3:

In this study, Shen et al. perform a meta-analysis of previously published data to unravel the effects of SNPs and InDels in the binding of CEBPB and PU.1 in macrophages. The authors find/confirm that alterations in the TF motif have an important impact on TF binding, while alterations on the spacing between the motifs does not have an effect on their binding. While this is an intriguing question, the study is rather straightforward, mostly confirms previous observations of the impact of PU.1 binding site alterations (although the presented analysis techniques are state-of-the-art and inspiring; and InDels are often not included, while here they are carefully assessed). The study could be enhanced with experimental validation (e.g. enhancer reporter assays); comparison with other computational techniques (e.g., deep learning); inclusion of additional data layers (e.g., gene expression); and expanding it to other TFs and systems to investigate whether these findings are generally true for other cell types. As it currently stands, the conclusions in the paper are a bit too general from the (biased) analyses performed.

1. Are LDTFs pioneer TFs and SDTFs non-pioneer TFs? We have only found this terminology in papers from this group.

2. The basis of the study are ChIP-seq peaks, but ChIP-seq peaks without the TF motif exist (sometimes a large fraction), can this be discussed? Particularly how false positive (i.e., indirect binding sites, or phantom peaks) impact the results.

3. Calculating spacing between motifs is a big challenge, because often a CRM contains multiple matches to the same TF. If TF1 has 3 matches, and TF2 has 4 matches, then there are a lot of distances between TF1 and TF2 motifs possible. The authors calculate only the distance between the two best scoring matches. Can this decision be justified by a thorough analysis? (e.g., do other distances between the best match of PU.1 and the 2nd best match of CEBP destroy or maintain the correlations?). In conclusion, a landscape overview of possible distances vis-a-vis genomic variation would be more informative than only using the distance between the two best matches.

4. Related – in Figure 1c. How is the distance between CEBPB and PU.1 motifs calculated on the singly PU.1 binding sites, do they also have CEBPB binding sites (and vice versa)? If yes, what are the differences between these regions and regions bound by CEBPB (e.g. is it because CEBPB motifs are weaker in these regions compared to regions bound by CEBPB)?

5. Also related – how much does spacing change with indels (e.g. from ~12bp, what is the final size distribution with indels)?

6. Figure Suppl 4 (Figure 2). In regards to the effect of the spacing, it seems that when the initial spacing between the motifs is around 60 bp, effects are weaker compared to when the initial size is between 20-40 and 80-100 bp; what could be the reason?

7. Figure 1d. Have sites with log reads CEBPB/PU.1 < 4 been filtered out?

8. Line 115 – the negative correlation between PU.1 and CEBP motifs 'implicates' synergistic binding and degenerative motifs, but this is speculation (it is not known which ChIP-seq events reflect true enhancers).

9. If CEBPB ChIP-seq signal is negatively correlated with the PU.1 motif score (Figure 1d), mutation of the PU.1 motif should increase CEBPB binding (Figure 2). Based on panel D, it seems that mutation of the PU.1 motif actually decreases CEBPB binding.

10. The quality of the SNPs and InDels are not discussed. InDels are more prone to false positives, this was not taken into account?

11. The quality of the ChIP-seq peaks is also not taken into account. Can a FRIP analysis be provided, for example plot FRIP versus the number of peaks across the samples.

12. PU.1 and CEBP were somehow chosen. An unbiased analysis starting from a larger motif collection would have been more interesting, to see if the properties of PU.1, CEBP, and their distance, emerges from the background of other motifs. Later on there is a JASPAR analysis – what were other high-scoring hits?

13. For the twelve collaborative factors predicted, some kind of (computational) validation would be useful.

14. For identifying cofactors exploiting other ChIP-seq data (Figure 3A), which ChIP-seq tracks were used and in which tissue? In general, data/code availability sections are missing.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Systematic analysis of naturally occurring insertions and deletions that alter transcription factor spacing identifies tolerant and sensitive transcription factor pairs" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jessica Tyler as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Jeff Vierstra (Reviewer #2).

The reviewers are in agreement that this paper is of potential interest for readers studying transcription factor (TF) binding site grammar/enhancer regulation. The work provides insight into the role of motif spacing alterations in TF binding/co-binding in the context of naturally occurring genetic variation. Overall, the data are properly analyzed and validated, although aspects of data analysis and presentation should be improved as outlined below, in a revised manuscript.

Reviewer #1:

Shen and colleagues investigated the role of motif spacing in regulating transcription factor (TF) binding or co-binding, specifically in the context of naturally occurring InDels in both human individuals and mouse strains, using previously published data (Hu et al., 2019; Link, Duttke, et al., 2018; Stolze et al., 2020).

The authors classified 75 TFs in K562 cells into constrained and relaxed spacing relationships with respect to their co-binding TFs, and found most of the TF pairs fall in the relaxed category. To illustrate whether spacing alterations affect TF binding and promoter-enhancer function, the authors analyzed the previously published data in mouse macrophages and human endothelial cells. They find that relaxed TF binding is highly tolerant to naturally occurring spacing alterations, which was further supported by CRISPR/Cas9 induced InDels in mouse macrophages.

The study would benefit from including other types of data available (i.e. gene expression and 3D interactions), to better examine the effects of spacing alterations and whether they are indeed related to promoter-enhancer functions.

1. The authors defined constrained and relaxed spacing relationships using public dataset including 75 TF ChIP-seq in K562 cells. K562 and HepG2 (analyzed in this study) are cancer cell lines. The karyotype of cancer cell lines, their own genetic variations and specific TF networks need to be carefully examined/ruled out before applying this to other data from healthy individuals.

2. Some TFs, especially the ones belong to the same families, share core motif sequences, and usually these TFs can co-localize to regulate gene expression. It is not clear how this case was handled in the pipeline.

3. (Figure 2A and 2B) The number of TF pairs considered/affected, the number of InDels at motifs/between motifs/in backgrounds, and the number of high-frequency/rare variants/singletons, need to be listed, which could further help illustrate the significance of any enrichment.

4. Line 165 – 168, "Since common variants are associated with less deleteriousness and rare variants with more deleteriousness (Lek et al., 2016), our data suggest that InDels between motifs of TFs with constrained spacing could be just as damaging as those at motifs whereas InDels between motifs of TFs with relaxed spacing might have a much weaker effect". This is speculation, and it would be better supported by at least some examples if not analysis/statistics, to show the deleterious effects. Probably this could be validated using CRISPR experiments as for relaxed ones.

5. The authors attempted to explore if these InDels eventually affect enhancer-promoter activity/function, but it's not clear whether enhancers and promoters were considered and whether they were considered separately in the analysis. Also, it would be great if the authors could assess whether spacing alterations investigated here in mouse macrophages affect gene expression, since RNA-seq/GRO-seq and PLAC-seq data are available from the published research. This information may help clarify the analysis, strengthen the conclusion and would be useful for readers interested in enhancer regulation.

Reviewer #2:

This paper attempts to address a long-standing question of how TFs collaborate to instantiate and maintain accessible and functional regulatory DNA. The authors make use of ENCODE data the investigate the extent TF spacing constraints in the genome and then integrate both human genetics data (gnomAD) and a compendium of ChIP-seq experiments performed in diverse mouse genetic backgrounds to test whether motif spacing has a significant effect on TF binding. While I appreciated the authors utilization of many datasets to test for spacing effects (large ENCODE data to identify motif pairs with spacing constraints, human genetic to look for signals of negative selection of natural variation effecting spacing and mouse TF binding data to 'test' for spacing effects), I find that computational analysis within this paper is quite shallow, leading to mostly obvious conclusion that variation within the TF-DNA interaction interface are critical for TF binding. Furthermore, While the editing experiments are a nice addition in the revision, I am not sure that they provide much in the way of validating or generalizing their claims. Finally, the authors should more thoroughly place their work in the context of previous studies.

1. The constrained vs. relaxed spacing analysis has a high likelihood to be confounded by latent genome architecture. Specific class of retrotransposable elements are known to 'template' regulatory DNA (see Bourque, G. et al. 2008 Genome Res. (10.1101/gr.139105.112), Kunarso et al. 2010 Nat. Genetics (10.1038/ng.600), and an analysis of co-binding/spacing constraints from ENCODE data: Wang et al., 2012 Genome Res.(10.1101/gr.139105.112)). The authors should perform an analysis that accounts for repetitive DNA that encode competent cis-regulatory DNA elements that have been templated across the genome. At a minimum these previous works should be cited.

2. The authors should comment on how rigid DNA-encoded TF spacing is not supported by evolutionary studies, which have shown an excess of TF motif turnover within regulatory DNA (see work from Duncan Odom's group, Vierstra el., 2014 Science for a direct mouse-human comparison).

3. While Leveraging CRISR/Cas9 editing to generate a broad spectrum of 'spacing' alleles is a clever approach to tackle the experimentally test the effect of motif spacing on TF (co-)binding, the experiment is very underpowered to test the generalizability of the authors claims. Did the authors select single cell clones from the editing experiment or just look at bulk edited populations? If the former, it is unclear how any conclusions can be made from a mixture of edited cells that have a spectrum of indels (also likely carrying two different alleles).

Reviewer #3:

Transcription factors (TFs) bind to the DNA in a sequence-specific manner at TF binding sites (TFBSs) to control gene transcription. Hence, characterizing how TFs interact with DNA is key to uncover how gene regulation occurs and how this process can be disrupted in diseases. While the binding properties of a large portion of human TFs are well characterized, a remaining challenge lies in our knowledge of how TFs interact cooperatively at regulatory elements, either forming dimers or co-binding the same regions. In this manuscript, Shen et al. explored spacing patterns between TFBSs. Relying on ChIP-seq data, they developed a new methodology to predict TF pairs harbouring constrained or relaxed spacing patterns between their TFBSs. The authors made their code available, which allows reproducibility and exploration; this should be a requirement in the field but is not always complied with so we thank the authors for this. When applied to a limited set of TFs with ChIP-seq data in K562 cells, the authors predicted that TF pairs primarily bind to DNA with relaxed spacing between their TFBSs. Nevertheless, they were able to highlight already known as well as novel specific pairs of TF harboring constrained spacing. Next, the authors leveraged naturally occurring small insertions and deletions in the human population and mouse strains to confirm that altering spacing between TFBSs of TF pairs with relaxed spacing patterns has limited effect. This observation was further supported by synthetic spacing alterations induced by CRISPR-Cas9 experiments. The study is overall well designed and addresses an important challenge in our understanding of TF-DNA interactions and TF cooperation.

Nevertheless, we believe that there are some methodological limitations that favor the identification of relaxed spacing patterns, which should be better outlined in the manuscript to allow the reader to fully comprehend the results. From the title and first sections of the manuscript the readers are given the impression that relaxed and constrained spacing instances are about to be described and analysed with an equal importance. However, more focus is given to the relaxed spacing with both the mouse and CRISPR analyses exclusively dedicated to this with no clear explanation why. It would be useful to the readers to have this explicitly outlined by the authors. Finally, the terminology associated with TF-DNA interactions is very often incorrect, which confuses the readers and should be addressed. Please see below for our detailed comments.

1. The terminology associated with TF binding events is inappropriate. The authors use "ChIP-seq peaks", "TFBSs", and "motifs" almost interchangeably, which is not correct. The inconsistency in the terminology makes it difficult to fully comprehend what the authors meant/did.

An example is one of the first sentences in the Introduction: "TFs bind to short, degenerate sequences at promoters and enhancers, often referred to as TF binding motifs." The sequences bound by TFs in promoters and enhancers are TFBSs while TF binding motifs are computational representations of TFBS sets, which can be represented in many ways such as consensus motifs, PFMs, etc.

The next sentence claims that "TFs bind in an inter-dependent manner to closely spaced motifs." Motifs cannot be closely spaced but TFBSs are. Another example is the subsection "Motif identification" in the Methods section while the authors describe the prediction of TFBSs (using motifs).

2. More details should be provided to the Methods section. We acknowledge that the authors provide their code for inspection but outlining all methodological details in the manuscript would help in the clear understanding of the methods used. For instance:

a. The authors do not describe how they selected de novo motifs using HOMER (only best motif?, any p-value threshold?, any specific background used?)

b. For the TFBS predictions, the authors used a FPR threshold of 0.1%, but which was the specific tool that they used for that? FPR computation depends on background expectation, what was used (e.g. 25% A, C, G, or T or nucleotide composition of the genome)?

c. P. 23, lines 466-470. The authors described that they conducted a permutation test but then described that the null distribution was obtained using random spacing values between 0 and 100. If the null distribution is obtained by randomly selecting values between 0 and 100, it does not correspond to a permutation. A permutation test would imply permuting the observed spacing values.

d. P. 25, lines 513-516. It is not clear to us why the authors considered subsets of mutations when overlapping TFBSs predicted for the ChIP'ed TFs (only if 2-bit difference in motif score) but not for mutations overlapping TFBSs predicted by MAGGIE (all mutations). Why not consider all mutations in all cases?

3. The methodology used has several limitations that are not described by the authors. We encourage the authors to clearly outline them to the readers. Furthermore, we believe that these limitations favor the identification of relaxed spacing, which should be acknowledged, especially since the majority of the work focuses on alterations of spacing for TF pairs with relaxed spacing patterns.

a. It is well documented that TF binding preferences for TFs binding in close proximity (e.g. as dimers) can be altered. For instance, Jolma et al. (https://www.nature.com/articles/nature15518) used CAP-SELEX to reveal that "Most TF pair sites identified involved a large overlap between individual TF recognition motifs, and resulted in recognition of composite sites that were markedly different from the individual TF's motifs." As the authors relied on TF binding profiles (or motifs) corresponding to the binding preferences of TFs binding as monomers, it is possible that they will miss cooperative binding inducing a change in binding preferences. Furthermore, the authors did not consider overlapping motifs, which is again precluding the identification of constrained spacing.

b. The authors rely on ChIP-seq data to identify TF cooperation. While this is fine overall, this data does not allow the authors to know whether two identified TFs bind to their TFBSs on the same molecules. Indeed, ChIP-seq being a bulk experiment, it does not allow to discriminate between true co-occupancy on the same molecule or not. This should be discussed to put the work in a larger context to the readers. See https://www.cell.com/molecular-cell/pdf/S1097-2765(20)30793-0.pdf for a reference.

c. The de novo motif enrichment does not ensure that the motif found is actually the one bound by the ChIP'ed TF. Indeed, the motifs found for ARID1B and ARID2 correspond to GATA motifs while ARID TFs bind to more general A+T rich motifs. It is unclear whether the signal observed for these TFs is due to their direct interaction with DNA.

4. It would have been nice to perform similar experiments as the mouse and CRISPR ones but considering TF pairs with fixed spacing of their TFBSs. If the authors decide not to, they should at least clearly state to the readers that they more specifically focused on relaxed spacing and why.

5. It would have been interesting to provide information about the prevalence of cobinding events in the different ChIP-seq datasets. For instance, what is the percentage of ChIP-seq peaks that contain a predicted TFBS for each TF? What is the percentage of such peaks that contain cobinding events? Is there a difference in numbers b/w constrained or relaxed spacing. Providing this information would help the readers to put these observations into a more general context of TF binding regions.

6. It would be nice to have similar plots as in Figure 3B for pairs of TFs with constrained spacing to show how it contrasts.

7. In all analyses, it seems that more deletions than insertions were observed (see Figure 2A for instance). It would be interesting to see if the results recapitulate when considering insertions and deletions independently.

8. It is unclear to us what is the analysis of MAGGIE-predicted TFBSs adding to the story. Moreover, the authors claim that MAGGIE identifies "functional" TFBSs but the authors do not provide any specific evidence of function (and which function?) in our opinion.

9. It seems that there is a periodic pattern in Figure 5E with log-odds ratio periodically equal to 0 (at least with indel sizes < -45). Could this correspond to the minor groove width periodicity of ~10bp (see for instance https://www.cell.com/cell/pdf/S0092-8674(18)31312-6.pdf for periodicity of mutations)? Could the authors comment on that?

10. In several figures, the authors should provide all points instead of summarizing with boxplots, which are frowned upon as they hide data distribution.

11. P. 9 line 178: the authors mentioned 50 millions SNPs but we do not find where this data is used as observing SNPs would not alter spacing.

12. P. 2 line 46: "implicating their effect…" we would rather write "suggesting their effect…".

13. The authors seem to have ignored homodimers. Maybe their methodology could be extended to consider spacing b/w TFBSs for the same TF.

14. TF naming is sometimes inconsistent in the text and figures. For example, SPI1 and PU.1 are both used in Figure 3. Similarly, we recommend revisiting the text for p65 and RELA, as well as C/EBPβ and CEBPB.

15. It is not clear where the authors retrieved HepG2 cell line data from (used in the Figure 1 —figure supplement 4). Was this data processed in the same way as K562 cell line data?

16. P. 8 line 152: we suggest replacing "we overlaid" with "we mapped".

17. P. 1 line 30: "ChIP-sequencing" should be replaced with "ChIP-seq" for consistency.

18. Figure 3D,F,H : instead of motif score this should be TFBS score.
