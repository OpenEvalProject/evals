# Peer review - Round 1

Editors:
- Detlef Weigel, Max Planck Institute for Biology Tübingen Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.101197.3.sa0](https://doi.org/10.7554/eLife.101197.3.sa0)

This valuable study addresses the potential roles of the master regulator of X chromosome inactivation, the Xist long non-coding RNA, in the regulation of autosomal genes. Using data from mouse cells, the authors propose that Xist can coat specific autosomal promoters, which in turn leads to the attenuation of their transcriptional activity. The evidence from individual genes is interesting, and the model aligns with recently published results from humans. However, despite some improvements during revision, the data and statistical analyses in the current study are not yet strong enough to allow for conclusive inferences, leaving the evidence for mouse cells behaving like human cells incomplete. The topic of the work is of broad interest, in particular to colleagues studying gene regulation and noncoding RNAs.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.101197.3.sa1](https://doi.org/10.7554/eLife.101197.3.sa1)

Summary:

The manuscript by Yao S. and colleagues aims to monitor the potential autosomal regulatory role of the master regulator of X chromosome inactivation, the Xist long non-coding RNA. It has recently become apparent that in the human system, Xist RNA can not only spread in cis on the future inactive X chromosome but also reach some autosomal regions where it recruits transcriptional repression and Polycomb marking. Previous work has also reported that Xist RNA can show a diffused signal in some biological contexts in FISH experiments.

In this study, the authors investigate whether Xist represses autosomal loci in differentiating female mouse embryonic stem cells (ESCs) and somatic mouse embryonic fibroblasts (MEFs). They perform a time course of ESC differentiation followed by Capture Hybridization of Associated RNA Targets (CHART) on both female and male ESCs, as well as pulldowns with sense oligos for Xist. The authors also examine transcriptional activity through RNA-seq and integrate this data with prior ChIP-seq experiments. Additional experiments were conducted in MEFs and Xist-ΔB repeat mutants, the latter fails to recruit Polycomb repressors.

Based on this experimental design, the authors make several bold claims:

(1) Xist binds to about a hundred specific autosomal regions.

(2) This binding is specific to promoter regions rather than broad spreading.

(3) Xist autosomal signal is inversely correlated with PRC1/2 marks but positively correlated with transcription.

(4) Xist targeting results in the attenuation of transcription at autosomal regions.

(5) The B-repeat region is important for autosomal Xist binding and gene repression.

(6) Xist binding to autosomal regions also occurs in somatic cells but does not lead to gene repression.

Together, these claims suggest that Xist might play a role in modulating the expression of autosomal genes in specific developmental and cellular contexts in mice.

Strengths:

This paper deals with an interesting hypothesis that Xist ncRNA can also function at autosomal loci.

Weaknesses:

The revised manuscript now includes many additional bioinformatic analyses to support the premise that Xist RNA targets a specific set of about 100 promoters and attenuates their expression in the early stages of differentiation. I have previously raised significant concerns about the bioinformatic analyses and the robustness of the data, especially those linked to CHART-seq datasets. Despite some improvements, fundamental problems with the analysis remain, precluding a conclusion on whether Xist RNA binds specific autosomal promoters. The main concerns include:

(1) The authors nicely explain the use of biological replicates; however, they still fail to provide the sufficient analysis I requested on d0 and sense probes. While some quantification is presented in Figures 1E and 1F, the peak calling I asked for has still not been performed. In the response document, the authors report that about 600 peaks were identified in d0 female ESCs compared to about 100 in differentiated conditions. They explain this by the well-known phenomenon of having a background of differentiated cells in d0. In my opinion, this reasoning is flawed. With 98% of cells not inducing Xist in the culture, it is unimaginable why 600 peaks would be detected in the peak calling analysis. Rather, this demonstrates a high background in the CHART peak calling. To assess this further, I have reanalyzed d7 CHART datasets and found robust enrichment of the sense probe on promoters of genes, even stronger than the antisense probe. MACS peak calling also identifies a robust number of peaks on the sense probe. Indeed, even though Figure 1F shows low sense probe enrichment, this is because it focuses on the anti-sense peaks only. An opposite effect is observed when focusing on all genes or on sense peaks. Thefore it is tough to decide which of the signal is truelly due to Xist binding and what is an inherent problem with the CHART signal. These results cast serious doubts on the biological conclusions of this work and point to a very high background level of promoter signal in both sense and antisense samples.

(2) The authors do not address the conundrum of their results: how is it possible to have a genome-wide autosomal accumulation of Xist signal at promoters (see Figures 1A and 1B), while simultaneously specifically affecting only 100 promoters in the genome? The signal is either general (as Figures 1A and 1B suggest) or specific (as implied by the peak calling), but it cannot be both. Current data points to the fact that CHART has a bias for the most open parts of the chromatin.

(3) The text is still very confusing when it comes to Polycomb. Some experiments point to the fact that there are few PRC1/2 marks at putative Xist autosomal binding sites (Figure 3C), while the use of X1 induces the loss of PRC2 marks. I still find this internally contradictory. The authors sadly do not address my concerns with additional analysis. Their current data indicate that upon Xist upregulation, Xist-RNA binds to autosomal regions that are highly expressed and devoid of Polycomb. These loci then become transcriptionally attenuated and gain some (but low) level of PRC2 in a Xist-dependent fashion. If this model is true, then all these regions should not have Xist in d0 of differentiation and should also have slightly lower levels of PRC2. The argument that there is a low level of Xist in 2-5% of cells should not be a problem because most of the signal will come from the 98% of cells not expressing Xist (as seen in Figure 1A). Without timepoint 0, the whole premise of the paper is difficult to interpret. Either the d0 samples are good enough, or the system is so leaky that it is nearly impossible to identify Xist-specific effects. Males are a useful control but are obviously a genetically very different line with distinct epigenetic and signaling statuses. It is crucial to compare the timing of repression/PRC accumulation to conclude if and how Xist is functional on these loci.

(4) The authors did not address my concerns about the transcriptional analysis. I belive that the control genes are not selected properly. This analysis should not have been performed on just 100 randomly selected regions/genes. Instead, bootstrapping of 100 randomly selected regions/genes should be done, e.g., 1000 times. Additionally, one should only sample from expressed genes to have a comparable control gene set. For example, in Figures 4D and 4E, the distribution of control regions is entirely different. To stress again, relying on a set of 100 randomly selected genes/regions is not statistically robust; controls have to be matched, and bootstrapping has to be performed. Finally, each timepoint uses a different set of autosomal targets. There is a need to visualize the same set of genes across all timepoints (including d0). For example, are genes bound by Xist at d7 highly expressed at d0 and then attenuated only at d7? What happens to them at d14 (see points from 3)? The arguments about d0 heterogeneity are again not convincing (nor is Figure 3H, which shows a different set of genes).

(5) Transcriptional analysis is often shown only as tracks however the reads for key example genes have to be quantified properly and not just visualized or amalgamated in a violin plot.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.101197.3.sa2](https://doi.org/10.7554/eLife.101197.3.sa2)

Summary:

To follow-up on recent reports of Xist-autosome interaction the authors examine female (and male transgenic) mESCs and MEFs by CHARTseq. Upon finding that only 10% of reads map to X, they sought to identify reproducible alternative sites of Xist-binding, and identify ~100 autosomal Xist-binding sites in active chromatin regions. They demonstrate a transient down-regulation of autosomal expression. They utilize published male transgenic inducible Xist mESC data to support their findings. In their system, inhibition of Xist reduces autosomal impact.

Strengths:

The authors address a topical and interesting question with a series of models including developmental timepoints and utilize unbiased approaches (CHARTseq, RNAseq). For the CHARTseq they have controls of both sense probes and male cells; and indeed do detect considerable background with their controls. The use of 'metagene' plots provides a visual summation of genic impact. They compare with published data.

Weaknesses:

The revised text and rebuttal clarified my confusion of the 'follow-up' analyses (Figure 4) compared to published datasets. Further, the figure legends have been improved.

While the controls were a strength, it appears that when focussed on bound regions, the background (from sense probes) is now also substantially higher than global background (compare 1E to 1A/B). Thus, why do these autosomal targets enrich for the sense probes, and how to distinguish from such background for the ∆B experiments? If male and sense are both controls, then why is sense lower for males than females, doesn't this suggest Xist impact? While authors note d0 might detect Tsix, the signal is only slightly reduced by d14 and never equivalent. Indeed, the new PCA (S1C) does show as noted that female Xist interactions are distinct from sense and male, but the male signal is even more distinct from sense probes.

It would have been preferable to see the dispersion of the Xist RNA cloud in these ∆B cells, rather than a reference.

Only 2 replicates were used, but there were multiple time-points: D0, D4, d7, d14; further, the correlation analysis showed good reproducibility, and in response to reviews they note that 2 replicates are standard of practice.

The conclusion that RepB is "required for localization to the ~100 genes" is based on density (panel 2E); however, these autosomal targets retain enrichment at TSSs (panel 2A) and indeed the text suggests they are the same sites, suggesting that in fact the choice of autosomal region binding is not RepB dependent. Thus, this remains unresolved for me.

The introduction is clear, and the senior author is a leader in the field; however, by this reviewer's count 19 of the 52 references include the senior author.

Better descriptors for the supplemental Excel files would be helpful.

Aim achievement: The authors do identify autosomal sites with enrichment of chromatin marks and evidence of silencing. Their revised text clarifies many issues, although this reviewer still remains unconvinced that the autosomal targeting is repB-dependent.

The impact of Xist on autosomes is important for consideration of impact of changes in Xist expression with disease (notably cancers). Knowing the targets (if consistent) would enable assessment of such impact.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.101197.3.sa3](https://doi.org/10.7554/eLife.101197.3.sa3)

Summary:

Yao et al use CHART to identify chromatin associated with Xist in female mouse ESCs, and, as control, male ESCs at various timepoints of differentiation. Besides binding of Xist to X chromosome regions they found significant binding to autosomes, concentrating mostly on promoter regions of around 100 autosomal genes, as elucidated by MACS. The authors went on to show that the RepB repeat is mostly responsible for these autosomal interactions using a female ESC line in which RepB is deleted. Evidence is provided that Xist interacts with active autosomal genes containing lower coverage of repressive marks H3K27me3 and H2AK119ub and that RepB dependent Xist binding leads to dampening of expression, but not silencing of autosomal genes. These results were confirmed by overexpression studies using transgenic ESCs with doxycycline-inducible Xist as well as via a small molecule inhibitor of Xist (X1), inducing/inhibiting the dampening of autosomal genes, respectively. Finally, using MEFs and Xist mutants RepB or RepE the authors provide evidence that Xist is bound to autosomal genes in cells after the XCI process but appears not to affect gene expression. The data presented appear generally clear and consistent and indicate some differences between human and mouse autosomal regulation by Xist. Thus, these results are timely and should be published.

Strengths:

Regulation of autosomal gene expression by Xist is a "big deal" as misregulation of this lncRNA causes developmental defects and human disease. Moreover, this finding may explain sex-specific developmental differences between the sexes. The results in this manuscript identify specific mouse autosomal genes bound by Xist and decipher critical Xist regions that mediate this binding and gene dampening. The methods used in this study are appropriate, and the overall data presented appear convincing and are consistent, indicating some differences between human and mouse autosomal regulation by Xist.

Comments on revisions:

In the revised manuscript, the authors have addressed my previous criticisms satisfactorily. Moreover, the manuscript has been much improved with new confirmatory results and additional control experiments. This, combined with more detailed descriptions/explanations facilitates data interpretation, making the paper more transparent and easier to read.
