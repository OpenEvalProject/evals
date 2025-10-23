# Peer review - Round 1

Editors:
- Asifa Akhtar, Max Planck Institute for Immunobiology and Epigenetics , Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.09571.047](https://doi.org/10.7554/eLife.09571.047)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for submitting your work entitled "Chromatin dynamics and the role of G9a in gene regulation and enhancer silencing during early mouse development" for peer review at eLife. Your submission has been favorably evaluated by Fiona Watt (Senior editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

Essential revisions:

The three reviewers found your manuscript very interesting. However, there was consensus that currently the manuscript lacks coherence and would greatly benefit from removing parts of the data and strengthening other aspects.

Below, I summarize the main discussion points raised during the review process that we would like you to address upon revision.

In particular, we suggest that you could consider removing parts from the early embryo due to lack of functional relevance.

The reviewers were excited by the ChIP-seq data from epiblast, but felt that additional validations (see comments from Reviewer 2) and analyses (point 4 of Reviewer 3) would maximize the impact of the study.

There was also a suggestion to remove the p53 where indirect effects cannot be ruled out. However, it was also discussed that one value of the p53 ChIP result from G9a KO is demonstration that G9a loss enhances p53 binding at select enhancers, without appreciably affecting H3K27ac (Figure 6D). The reviewers suspect that this may be an indirect consequence of either increased accessibility at enhancers associated with loss of H3K9me2 (which would be an interesting phenotype supporting role of G9a in enhancer repression) or simply of an increased cellular stress resulting in increase in p53 stability (perhaps less interesting). If combined with some accessibility data and eRNA expression analysis at matching enhancers (none of the enhancers at which eRNAs were analysed corresponds to the p53-bound enhancers from Figure 6D), the p53 ChIP result could be used to strengthen the conclusions on the role of G9a in regulating enhancer function – which currently needs further work.

We also highly encourage you to further strengthen the computational analysis and specificities required. This should help in addressing a number of points raised by the three reviewers.

Reviewer #1:

In the current study, Zylicz and colleagues explore the role of G9a and EZH2 during early embryonic development encompassing the 2-cell stage and early blastocysts. The quantity and technical aspects of this study are very impressive. Each of the experiments provides important insights into the function of G9a and EZH2 in priming gene regulatory networks in epiblast cells. However, the experiments are disjointed and do not flow together well to make one coherent story. There is sufficient data here to produce two or more coherent stories exploring individual early findings reported by the authors. For instance, data from the 2-cell study and the transposons experiments can be removed to improve the flow of the paper as they detract from the main message of the study.

1) The H3K9me2 expression levels in Figure 1C, compared to GLP and G9a expression levels in Figure 1–figure supplement 1 are standardized to different time points. In addition, different time points are presented (i.e. E3.5 versus E4.5; E5.5 versus E6.5). Is this the reason that expression of H3K9me2 and G9a/GLP does not directly correlate? The authors should standardize the expression to the same stage if they wish to draw comparisons.

2) It is not clear why the samples from the G9a M/Z and M/+ are pooled in the analysis presented in Figure 1E and Figure 1-figure supplement 2E? In other panels the data is separated. Transcription of some genes from the zygotic genome has been reported as early as the 2 cell stage and hence, these data should be separated. This may also reduce the large variation seen in Figure 1E and Figure 1–figure supplement 2E.

3) During the RNA seq. analysis, why was a fold change cut-off of log2(1.6) used? Furthermore, was a false discovery rate, which is more commonly used, applied to the data? How can the authors rule out that all direct targets of G9a are changed by at least log2(1.6)?

4) In the G9a-/- versus control RNA seq., G9a mRNA does not appear to be reduced (Figure 2–source data 1). Is there a reason for this discrepancy?

5) What was the cut-off for significance in the Ezh2-/- RNA Seq. dataset? It is not clear in the paper. Is it the same as the G9a-/- RNA Seq? The authors need to make this information clear.

6) Figure 3E shows only a small number of transcriptional changes despite H3K27me3 and H3K9me2 being wide spread. Does the correlation change if the arbitrary log2 cut-off of 1.6 is changed? Deletion of chromatin modifying proteins does not always result in very large changes in the expression of target genes.

7) The authors need to further address the discrepancy in OCT4 level between their study and Yamamizu et al., 2012. It seems odd that there is such a large incongruity between the two studies. Only one line is provided in the Discussion on this topic and it does not sufficiently propose any reasons for such discrepancy. Given that lack of changes in pluripotency is central to the conclusions of this paper, the authors should undertake staining for OCT4 in G9a-/-embryos and controls.

8) The authors show in Figure 2E that p21 is upregulated in a subset of G9a-/-samples, which is consistent with increased H3K9me2 at the p21 locus during ESC differentiation. The authors claim that these observations support their view that the delayed development of G9a-/- embryos is related to increased apoptosis and/or reduced proliferation, and not retainment of pluripotency. The authors have provided little evidence for this. The authors should validate their proposal in vivo by undertaking BrdU incorporation studies and phospho-H3 staining for proliferation, as well as TUNEL or active caspase-3 staining to analyse cell death.

9) In addition, can the authors exclude that the expressions of important developmental genes are normal at E6.5? For instance, a very high level of Bmp4 is observed in G9a-/- E6.25 epiblasts (Figure 2D), which could be one explanation for developmental defects. In situ hybridizations for developmentally important genes including Bmp4 need be carried out.

10) In the E6.25 RNA Seq. data (Figure 2–source data 1), p21 mRNA is not reduced in G9a-/- epiblasts. Can the authors explain its absence?

11) Since the authors state that a significant proportion of genes affected by G9a deletion are involved in germ line specification, the authors need to show whether germ cells are affected. Are PRDM14 and Blimp1 expression patterns normal in G9a-/- embryos? If pluripotency is indeed unaffected, while germ line specification is presumably impaired, can the authors show normal alkaline phosphatase staining in G9a-/- embryos and not in germ cells?

12) The authors claim that 2i ESCs as primitive ectoderm (PrE). In contrast, the works from Austin Smith's lab and others (Van Oosten et al., 2012 for example) have shown that the ESC state in 2i resembles the naïve state of the epiblast. Why do the authors consider the 2i state to be similar to the PrE? Rather, ESCs in standard ESC medium (with serum) are considered to be more like E4.5 PrE.

Reviewer #2:

Please note that I cannot judge the stringency of the bioinformatics pipelines used in depth, and therefore my comments are focused mostly on the biology of the questions addressed and the conclusions drawn, rather than in the stringency of the computational side. I do find, in general, that the computational data is not always presented in a manner for a broad readership, and some points below suggest improvements towards this direction.

Although a few of the observations documented are not particularly new, the manuscript by Zylics and colleagues builds on former data on Ezh2 and G9a in regulating development around implantation. The strongest point in, my view, is the analysis of epiblast cells in vivo at the transcriptional level and at the chromatin level (K9me2 and K27me3) genome wide. The experiments are carefully executed and in most instances the conclusions drawn are supported by the data presented.

I have, however, mixed feelings about the presentation and the flow of the manuscript. It does not come out as a single, solid message, and is diluted with many pieces of data, some of which I find irrelevant for the main conclusions and I would therefore suggest to remove these parts, which encompass all the pre-implantation data (which is not strong enough), as well as the p53 data at the end, which in the end are not very strong. This would allow the authors to concentrate in a less dense manner, on the main messages of the paper based on the transitions between naïve/primed and epics states.

I have some comments on the ChIP protocol validation that require in my view, additional experimental work, and some comments to draw to the phrasing and statistics throughout the manuscript, as well as clarification or additional computational analysis.

The 'pregastrulation conclusion’ (paragraph four of the Discussion) is reasonable, but the preimplantation work is confusing, and poorly documented in comparison with the peri-implantation and in vitro data (e.g. statement of 2C specific gene regulation by G9a is based on only 3 genes) and does not add much to the manuscript and instead deviates the focus of attention from the pre-gastrulation cell fate transitions.

All figures lack description of quantification of fluorescence intensities, as well as the N numbers for IF and quantifications. The only description is 'fluorescence intensity was normalised to DAPI', but the authors state that they used 'quantitative immunofluroescence' to analyse levels. Please add a better description and/or controls for this.

In Figure 3B and C: Why is ChIP enrichment mostly negative – it suggests rather a depletion of mark? Is there any enrichment at all e.g. for K9me2 in Figure 3B? The same applies for Figure 3–figure supplement 2 C, in which H3k9me2 'enrichment' is again below 0.

From Figure 3B and 3D, the authors conclude that K9me2 and K27me3 are on different regions. However, the data presented do not fully support these conclusions, both from analysis in 3B and from the self-organising maps: while there are some regions that are not overlapping, there are clearly other regions that do show overlap. The shape of the line in the fitting in 3B also suggests this interpretation. Since this analysis was not presented with statistics, nor with a comparison of e.g. active promoters or full genome data for 3B, I believe that the authors are not in the position to conclude what they conclude, so this part needs reinterpretation.

Regarding my validation point above, the only validation presented for the lcChip-seq is a comparison of Pearson figures (Figure 3–figure supplement 1) based on clustering of independent replicates – what if replicates are all poor showing similar background enrichment? The protocol would need validation to assess a comparison in magnitude of enrichment to standard protocol. I assume the authors have some material left to run a couple of PCR reactions, can they estimate by ChIP-PCR the differences in order of magnitude with the lcChIP in EpiSC versus the 'normal' EpiSC ChIP protocol?

I do not see much significance/added value on the p53 data (in the subsection “G9a Mediates Efficient Enhancer Inactivation”), and it only adds more 'density' in the manuscript, which is quite dense. Specially, how relevant (biologically and statistically) is the "15%" of H3K9me2 and H3K27ac enhancers being bound by p53?

The analysis of 'proximity' of eRNA is not presented adequately, nor it is known what 'proximity' is? In kb? This cannot be inferred from the graphs presented. Can the authors do an enrichment analysis of eRNA expression (on the y axis) relative to specific distances of genes (on the x axis, in kb). The conclusion on page 15 on H3K9me2 domains 'extend to active enhancers targeted for silencing, which accounts for coenrichment with H3K27ac' implies a causal relationship for which there is no data.

Reviewer #3:

In this study Zylicz et al. set out to explore the deposition and function of repressive histone marks such as H3K27me3 and H3K9me2 during early embryonic development. The authors generated embryos deficient for G9a or Ezh2 methyltransferases and examined their gene expression profile using single epiblast RNA-seq at day E6.25, prior to the overt phenotypic manifestations. To determine which genomic loci are marked by repressive histone methylation marks in vivo, the authors performed low cell number ChIP-seq assays for H3K27me3 and H3K9me2 in E6.25 epiblasts. Strikingly, for either mark, an exceedingly small subset of marked genes is perturbed upon loss of respective enzyme, suggesting either existence of multiple redundant silencing mechanisms or these methylation events being a secondary consequence of repression. Furthermore, the set of genes that are aberrantly upregulated are non-overlapping between the two different knock outs and show therefore that in the epiblast H3K27me3 and H3K9me2 are involved in repression of different set of genes. The authors note that many intergenic enhancer regions are marked by H3K9me2 in the epiblast, and they follow up upon these observations using the in vitro cellular models. They conclude that G9a mediates efficient inactivation of a subset of enhancers, particularly those bound by p53.

This study contains many interesting observations, tackles an important biological question and is generally well-executed. However, it also suffers from weaknesses that dampen my overall enthusiasm, but which could be fairly easily addressed.

1) The authors claim that a subset of enhancers gains H3K9me2 in epiblast, and that this is associated with their inactivation during transition to primed pluripotency. Several issues need to be clarified here:

In Figure 4E, heatmaps of H3K9me2 from ESC (to show that these loci indeed gain H3K9me2 during differentiation) and 6.5 epiblasts (to show that similar findings can be observed in vivo) should be included. Furthermore, how would these heatmaps look if authors chose as their analysed regions enhancers that are active in EpiLC/EpiSC, but not in ESC? What would be the corresponding profiles (if any) of H3k9me2 status at these regions?

2) A substantial weakness of the study is that despite the authors having all the necessary reagents in hand, the data pertaining to the functional impact of G9a on enhancer activity is limited to just a few examples, and not coherent ones either (e.g. enhancers shown in Figure 6D don't overlap those shown in Figure 6G-F). Given that the role of G9a in enhancer inactivation is one of the central novel claims of the paper, at the very least the eRNA expression analysis from the G9aF/–CreER EpiLCs treated with EtOH or TAM should be done systematically, across all H3K9me2 marked enhancers, and in comparison to enhancers unmarked by H3K9me2, but containing similar enrichment levels of H3K27ac. The relationship between enhancers with G9a-dependent eRNA expression and transcriptional changes at neighboring genes should be determined. To what extent transcriptional changes observed in G9a KO cells can be explained by H3K9me2/eRNA changes at nearby enhancers?

3) Increased p53 binding upon loss of G9a may be an indirect consequence of the defect in enhancer repression, perhaps resulting in the increased enhancer accessibility- did the authors consider looking at chromatin accessibility measurements such as ATAC, DNase or FAIRE? Such data could in fact strengthen the conclusions on the functional impact of G9a on enhancer activity, regardless of the specific impact on p53.

4) The authors generate valuable H3K9me2 and H3K27me3 ChIP-seq datasets from epiblast cells of E6.25 embryos, but I feel they missed the opportunity to provide a deeper comparison of their results with the H3K9me2 and H3K27me3 patterns reported from the in vitro cellular models such as EpiLC or EpiSC. What are the major similarities and differences in patterns? A systematic (and to whatever extent possible, quantitative) comparison of H3K9me2 patterns across the genome in different cellular states would not only be broadly interesting for the community, but also relevant for the authors' own conclusions.
