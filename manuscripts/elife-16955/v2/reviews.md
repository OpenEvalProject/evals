# Peer review - Round 1

Editors:
- Elisa Izaurralde, Max Planck Institute for Developmental Biology , Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.16955.025](https://doi.org/10.7554/eLife.16955.025)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "mRNA Poly(A)-tail Changes Specified by Deadenylation Broadly Reshape Translation in Drosophila Oocytes and Early Embryos" for consideration by eLife. Your article has been favorably evaluated by James Manley (Senior editor) and three reviewers, one of whom, Elisa Izaurralde (Reviewer #1), is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

There are several points raised by reviewers 2 and 3 that in fact I prefer not to summarize because this will involve losing some important information and relevant comments provide by experts in the field. Most of the points raised by the reviewers are related to the interpretation of the results and involve reanalysis of the data or the inclusion of additional information. These points can be addressed by the authors without further experimental work.

Reviewer #1:

This is a very interesting manuscript that provides a significant amount of novel information on poly(A) tail changes and translation efficiency in several stages of oogenesis and embryogenesis in Drosophila. This is the first study in which such a comprehensive analysis has been performed and thus provides highly relevant information and unexpected observations, which open new avenues of research. Therefore, the manuscript is ideal for publication in eLife.

Reviewer #2:

This manuscript presents a global analysis of mRNA translation, measured using ribosome profiling, and poly(A) tail length, measured using PAL-seq, during the early stages of Drosophila development, spanning three important developmental transitions: oocyte maturation, egg activation, and the maternal-to-zygotic transition. These data provide interesting insights into the correlation between mRNA translation and poly(A) tail length during various stages of development, and represent a valuable resource. However, a number of issues require clarification, and the manuscript needs to be improved through additional analyses, and made more useful to the reader through the presentation of additional information, as described in the specific comments below:

1) In comparing changes in poly(A) tail length, the authors largely rely on examination of fold change. However, while measurement of fold differences is one approach for quantifying poly(A) tail length changes, this approach is not sensitive and not the most informative when the reference stage gene has a long poly(A) tail. For example, a change in poly(A) length from 10 to 20 yields a 2-fold change; however, a poly(A) tail lengthened from 40 to 80 also yields a 2-fold change, despite the fact that the absolute change is four times greater for the second gene compared to the first gene. This absolute change is not reflected in examining the fold change of the tail length, which may be problematic if one assumes that PABP has a role in linking changes in tail length to changes in translation. The minimum poly(A) length bound by PABP is 12 residues and, on longer tracts, PABP binds approximately every 25 residues (Mol Cell Biol. 1987 Sep;7(9):3268, RNA 2005 Jul;11(7):1131). PABP binding-site length and the additional number of possible PABP copies bound (i.e. change in length as measured by the number of additional PABP that can bind to the transcript) need to be considered when examining changes in poly(A) tail length, and when performing analysis of TE. This analysis would be particularly enlightening in explaining large changes in TE that correspond to apparently small fold-changes in poly(A) tail length.

2) The section discussing the wispy mutant experiments is difficult to follow, and has a number of potential caveats. For instance:

A) The use of poly(A) selection in these experiments complicates the interpretation of the results; why would poly(A) selection in generating samples for RNAseq show biases in wispy mutants but not wild type?

B) If wispy mutants are blocked at the OET, how were TE and tail lengths measured in 0-2 h embryos (this isn't mentioned until the Discussion section)?

C) In Figure 5D, while the changes in TE in wispy mutant and wild type during the OET are correlated, those in the wispy mutant appear decreased in magnitude, implying that wispy does have a role in regulating translational activation during this transition.

Given these issues, the conclusions from this analysis regarding a lack of dependence of translational activation on cytoplasmic polyadenylation are overstated.

3) The authors should provide lists and further analysis (e.g. GO-term enrichment) of specific groups of genes that are mentioned in the manuscript. For example, 300 transcripts underwent little to no decrease in TE despite substantial tail-length reductions during oocyte maturation; mRNAs with tails that were least affected by the absence of Wispy during OET; genes listed in Figure 5D and png-dependent up and down-regulated TE genes list in Figure 6.

4) mRNA targets of SMG have been defined with regard to SMG-associated transcripts, and its regulation of translation and decay (Chen et al., 2014; Genome Biology). How do transcripts up-regulated in smg mutants in this study compare to those previously identified as SMG targets?

5) Quantification of several parameters are needed when making comparative statements. For example, in the second paragraph of the subsection “A conserved switch in the nature of translational control”, the manuscript describes the slope of several relationships and comments on how the slope becomes "strongly diminished," but fails to provide numerical values of the slope, and thus makes it difficult to quantitatively judge these statements.

6) To maximize the usefulness of the manuscript to readers, it will be important to include the TE and poly(A) tail length data at different stages and in different genotypes as supplemental data. Authors should have information tables for different stage samples as in Kronja et al. (2014b), Table S2: showing each gene's mRNA abundance (rpkm), ribosome protected fragments (rpkm), translational efficiency, and mean or median of poly(A) tail length for wild type and each mutant genotype. In addition, links to the data on GEO should be provided.

7) The authors should provide more representative examples of the behaviour of individual transcripts from the datasets they are describing; for instance, in Figure 1C it would be of interest to see traces for additional key genes, such as png, smg, bcd and wisp.

8) Could the authors extend Figure 3A to include time points all the way up to embryo 2-3h? Alternatively, provide a similar analysis for embryonic stages? It would also be beneficial for the reader if each cluster shown in Figure 3A had graphs describing not only TE changes but poly(A) length changes as well, as in Figure 3B. This would help demonstrate the relationship between TE and poly(A) tail length for the different clusters of transcripts.

9) Figure 6 and Figure 7 should be consistent (especially regarding the x- and y-axes) so that the reader can more easily compare the changes in png-dependent mRNAs in the png mutant to the changes in the smg mutant.

10) This manuscript includes both newly acquired and previously published data (Kronja et al., 2014a,b). The authors should more clearly indicate which data have been previously published and which are new. For example, a table should be provided outlining the source of the datasets used for each portion of this study: the table should indicate where new datasets or previously published datasets are used, and the type of sequence analysis performed (RNA-seq, ribosome-profile, and/or PAL-seq).

11) When describing the data in Figure 3, the authors discuss how a vast majority of the mRNAs that have >2-fold increase in TE are observed to undergo increases in poly(A) tail length. However, without the reciprocal analysis, this approach appears biased towards confirming their current model. The authors should perform the reciprocal analysis and examine the TE behavior of the mRNAs that undergo poly(A) tail lengthening, and show what proportion of the lengthened mRNAs also have a >2-fold increase in TE.

12) More information should be provided in the Methods and/or main text with regard to the number of replicates carried out for different experiments and statistical analyses performed on the data.

Reviewer #3:

The work by Eichhorn et al. characterizes the correlation between poly(A) tail length changes and ribosome-footprinting/mRNAs-seq (Translation Eficiency; TE) in Drosophila oocytes and embryos. Thus, the authors describe the correlation, or lack of correlation, between both events at different developmental stages and in mutant flies for wispy, png and smg (all previously implicated in translation regulation and/or poly(A) tail length dynamics). This study is a direct follow-up on previous works by the authors studying changes in mRNA translation during early Drosophila development (Kronja et al., 2014, ribosome-footprinting and proteomics) and poly(A) tail length profiling, together with TE measurements, in zebrafish and frog early development (Subtelny, 2014). Conclusions of the current study confirm those of previous works, showing a strong correlation between poly(A) tail length changes and TE until gastrulation, when the coupling is dampened.

Now, the authors further extend these approaches by using mutant embryos for known regulators of embryonic mRNA translation. However, genome-wide correlations allow for a limited set of conclusions as to the mechanism of maternal mRNA translation regulation, being the added value more as "valuable resources for future studies".

1) The "aggregation" of data from different mRNA variants in PAL-Seq and TE complicates interpretation of results. Thus, in oocytes, where there is no transcription and where there is a good correlation between poly(A) tail length and TE, it is safe to assume that the same mRNA is being compared. However, after MZT, newly transcribed mRNAs (for any given ORF) can be different than the maternal ones. This is indeed the case for alternative cleavage and polyadenylation during embryonic development (Hoque, 2013).

2) This work assumes a linear relationship between poly(A) tail length and translation. However, this has not been demonstrated. For example, while previous works show that (for maternal mRNAs) elongation of the poly(A) tail from 20-30 to 80-100 As causes translational activation (presumably by allowing the formation of the close-loop eIF4E-eIF4G-PABP), there is no evidence showing that further elongation has any impact. Thus, more than a linear correlation, poly(A) tail length may have a bimodal regulatory effect. This is supported by recent evidence (Park et al., 2016) indicating that a single PABP (binding 30-40 As) may be sufficient to support full translational activation. Therefore, ΔP(A) does not have the same meaning when it goes from 20 to 40 As than from 100 to 200 As.

3) Even for "unimodal" poly(A) tail length distribution (i.e., cyclin B, Figure 4B) the peak is broad ranging from 0 to 100, with about 40% of the transcripts having a poly(A) tail above 50 nt. Based on the above argument, it is difficult to interpret the meaning of an average at 40 nt. On the other hand, for toll (4D), most of the mRNAs are below 50 nt in stage 14 and the majority above 50 in activated eggs.

4) Normalization of the ribosome-footprinting by mRNA levels (mRNA-seq) using oligo-dT capture generates a strong bias that overestimates TE for short polyadenylated mRNAS (Park et al., 2016).

5) Being mRNA translation initiation a "competitive event" in which, not only mRNA-intrinsic features, but also competition with other mRNAs for the translational machinery dictates its efficiency, the large level changes in specific mRNAs after MZT (with maternal mRNA degradation and new transcription) can severely affect the normalization to obtain the TE ratio. This would not be an issue before MZT, as individual mRNA levels do not change.

6) Other level at which the interpretation of the results is difficult is derived from the origin of changes in poly(A) tail length, nuclear vs. cytoplasmic. Thus, in oocytes (with no transcription and no mRNA degradation), poly(A) tail length changes are presumably originated in the cytoplasm and for the same mRNA populations. After MZT (when mRNA transcription and degradation are reestablished), most of the poly(A) tail elongation events presumably correspond to newly transcribed mRNAs and most of the deadenylation events will result in mRNA degradation.

7) Probably, the most relevant contribution of this work over previous analyses is the use of mutants to correlate changes in poly(A) tail length with changes in TE. Although some potential correlations are found for wispy, png and smg, the main problem of this approach is that it does not differentiate between direct and indirect effects and all three genes have a profound impact in early embryonic development. This is clearly shown in the global deadenylation in wispy-mut oocytes and embryos. Obviously, this phenotype cannot be ascribed to the direct role of wispy in cytoplasmic polyadenylation, which should only affect a reduced number of mRNAs. In turn, the fact that these global changes do not impact the TE/poly(A) distribution over WT, can be due to the competitive nature of the poly(A) tail effect.
