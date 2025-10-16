# Peer review - Round 1

Editors:
- David Ron, University of Cambridge , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.05033.015](https://doi.org/10.7554/eLife.05033.015)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “The Small Molecule ISRIB Reverses eIF2α-phosphorylation-dependent Effects on Translation and Stress Granule Formation” for consideration at eLife. Your article has been evaluated by Randy Schekman (Senior editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors.

The Reviewing editor and the other reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

All three reviewers recognized the significance of your attempt to further characterize the consequences of ISRIB application to stressed cells and the potential for such a study to serve as an important advance. The methodology you chose to evaluate the impact on mRNA translation by ribosome profiling and on stress granule formation, by imaging, was likewise deemed appropriate to the task. However, the individual reviews and the consultative process that followed uncovered important problems concerning the interpretability of the data and the validity of the conclusions drawn. These problems are rather pervasive and it will not be possible for the Reviewing editor to decide alone if a revised version would be suited for publication. Thus, if you decide to revise your paper in accordance with the stipulations below, please bear in mind that it will need to be reviewed again by all three reviewers.

1) Detailed information concerning the Ribo-Seq experiments is missing: How many million mapped reads and how many replicates were done for each sample? The worry that data set may be inadequate is compounded by an impression that the read density for those elements of data that are presented in detail (Figure 1–figure supplement 1, for example) is rather low.

2) Significance figures for RNA transcript abundance are not reported.

3) The full power of single base resolution of the RPF analysis is not harnessed to de-convolute the effects of stress and ISRIB on the translation of uORFs in ATF4 and ATF5. It should be possible to assign reads to either the uORF or the main ORF even when they are overlapping as the reading frame is different.

4) The central conclusions of the paper, that ISRIB eliminated the effects of stress on translational regulation and that ISRIB is equivalent to mutations that abolish the ISR are not supported by the data. Numerous mRNA are differentially engaged by ribosomes in stressed & ISRIB treated sample(s) (Figure 2C) compared to the stressed PERK-/- cells (the benchmark used here for an ISR-inhibited system, Figure 2A). These experiments may be further confounded by a methodological issue in that the cells shown in Figure 2C were apparently treated with tunicamycin for 1 hour, whereas those in Figure 2A for 30 minutes. These issue needs to be dealt with in some detail.

5) The effects of ISRIB on stress granule formation in the images shown seem convincing. But these need to be quantified and analyzed with appropriate statistical tools.

The reviewers’ individual comments are noted below.

Reviewer #1

This manuscript provides new experiments building on those published in a 2013 eLife article concerning the mechanism of action of an ISR inhibitor compounds called ISRIB.

The authors use complimentary techniques to those used in their original study to provide additional support to their model that ISRIB acts to nullify the downstream signalling events following induction of eIF2 phosphorylation. Two experimental strategies are employed here: 1) Ribosome profiling (Ribo-Seq) of cells to examine global translational control responses to ISR and its inhibition and 2) cell imaging via immunofluorescence and also live-cell GFP to examine the appearance of stress granules and P bodies-markers of cellular stress. Both of these analyses appear to confirm and extend the findings reported in the original study, but do not yet identify the mechanism by which the inhibitor ISRIB nullifies the ISR.

My major concerns are with the robustness of the data reported. In its present version this is not possible to fully assess.

1) For RNA and Ribo-Seq experiments, there is no information given concerning the depth of sequencing. How many million mapped reads and how many replicates were done for each sample?

2) The significant changes in ribosome occupancy are reported in supplementary tables, but changes in RNA transcript abundance are not reported. This data should also be added to the manuscript.

3) For the Ribo-Seq fold changes reported, how are reads mapping to overlapping ORFs handled? Eg Figure 1–figure supplement 1, shows reads covering the uORFs (green) and main ORFs (blue) that overlap.

4) Is the read density data in Figure 1–figure supplement 1 reporting a single representative sample, total summed reads from replicates (if done) or mean reads from multiple replicates? The read density is not very high for any of the genes shown, except for ATF4.

5) Can the authors confirm and comment on the presence of RPFs between the annotated uORF and main ORF for CHOP mRNA?

6) One perhaps unexpected finding was an apparent increase in uORF RPFs following stress. The authors have chosen not to elaborate on this point. The usual translational control models depicted often show an all or nothing extreme response, but it is not surprising at all that there are still ribosomes on uORFs that may get skipped more frequently under stress conditions. Perhaps an important measure of control is the proportion of ribosomes that skip uORF2 in ATF4 and 5. This could be quantified as the Ribo-Seq read data for the overlapping ORF regions should be in separate reading frames. It should be possible to assign reads to either the uORF or the main ORF. As a measure of stress mediated translational control, the authors could quantify the number and proportion of RPF within the ORFs key for translational control. For ATF4 and ATF5 ORF/uORF2 reads would give an alternative readout of the relative translational control.

7) Blots showing eIF2 phosphorylation relative to total eIF2 should be in each type of cell used (plus minus) treatment for the time points used in the Ribo Seq study. This could be added to the ATF4 blot which uses different time points.

8) For the immunofluorescence experiments and for the GFP experiments in Figures 3 and 4 and Figure 4–figure supplement 1, each experiment requires quantification of a larger number of cells than are shown in each representative image. For example in 100 cells in each of three separate experiments what proportion of cells (plus minus) error contain stress granules or P bodies as appropriate. Such an analysis would enable statistical treatment of the significance of the observations made.

9) What is the effect of the ISR and ISRIB on the other arms of the UPR at the times used here. Are sampling times too early to observe XBP1 splicing and changes in ribosome binding? If they are this should be stated, if they are not it would helpful to show XBP1 reads.

Reviewer #2

In this manuscript, the authors study the role of ISRIB, a small molecule targeting the integrated stress response (ISR) in two experimental systems: Ribosome profiling and stress-granules formation. The study of the ISR by ribosome profiling essentially confirms earlier studies. The effect of ISRIB and stress granules is surprising and novel, but the underlying mechanisms remain unknown. While the study is potentially interesting, there are some important issues to address.

Major issues:

Throughout the manuscript, there is a disconnection between the data and the conclusions. I will only highlight the major ones here:

1) One of the central conclusions of the paper is that ISRIB eliminated the effects of eIF2α phosphorylation. The authors wrote: “The translational output of ISRIB-treated cells to ER stress was remarkably similar to that of cells with a genetically ablated ISR”. This contradicts the data. In fact, there are major differences between the two data sets (Figure 2A and 2C). I recommend providing a complete list of genes that change after ISRIB treatment and to study these changes, as it may shed light on ISRIB's function and/or target.

Supporting the idea that the changes caused by ISRIB (Figure 2) are actually tractable, ISRIB caused more changes (Figure 2) than Tm (Figure 1A). The secret of ISRIB's function may be hidden in this dataset. This needs to be documented and exploited.

A related issue: The authors conclude that “ISRIB does not have general off-targets effects on translation, transcription or mRNA stability.”

Again, this contradicts the data. Beside, “off-target” is a not suitable here, since we don't know what is the target of ISRIB.

2) Figure 3B: What are the vertical lines on PERK blots? Between first and second lane in the top blot and between the 9th and 10th lane in the bottom blot.

3) Figure 3A: It would be good to see images with better resolution to appreciate the localization of eIF3α, which looks very interesting. I still see some stress-granules on Ars+ISRIB in some cells but in most cells, the signal is too strong to be analyzed. It would be good to see images of better resolution and some quantitative assessment of the effects.

4) The disappearance of stress-granules is the impressive finding of the manuscript but how does this all happen? It is difficult to follow what might be going on because of the lack of consistency in the conditions used and because adequate controls are not presented. From this paper and the previous one, it would appear that ISRIB acts upstream of ATF4 translation and is dependent upon eIF2α-P (but without affecting the latter)? This needs to be explored further to get some understanding of what is happening.

Figure 4C: It would be good to present gels to show the effects, as the authors have the images already. It would be interesting to appreciate the qualitative changes in translation. Does this match, what is seen by ribosome profiling?

5) The Discussion is very broad and not connected to the current dataset. The first sentence of the Discussion is incorrect, as there are other antagonists of the ISR. I suggest two options for a revised discussion: Either to focus the discussion on the current dataset or to provide additional data inline with the discussion (mTOR signaling and the ISR, memory and stress granules, memory and ribosome profiling data).

6) Figure 1B: I didn't understand this panel. It needs to be clarified.

Reviewer #3

This study provides an important extension validating the compound ISRIB as a highly specific inhibitor of the canonical eIF2α-phosphorylation-dependent Integrated Stress Response. Given that original report was published in eLife, this present paper is most suitable as a linked research advance.

The most important finding is that the effects of ISRIB on mRNA translation, revealed by the unbiased tool of ribosome foot-print profiling and mRNA sequencing, are limited to effacement of the translational induction of a small set (five in total) of mRNAs that are translationally upregulated by the ISR. In this regard, ISRIB discretely mimics the effects of mutations that block eIF2α phosphorylation, either by interfering with the action of the upstream kinase (PERK-KO) or by precluding substrate phosphorylation in cis (eIF2αS51A).

Further support for a comprehensive defect in the ISR, introduced by ISRIB, is provided by evidence that stress granules (these are mysterious collections of mRNA binding proteins and translation factors that assemble in cells experiencing high levels of phosphorylated eIF2α) are rapidly disassembled by ISRIB.

In passing, this paper makes an important contribution to the study of the ISR: By confirming that its known positively regulated targets, cobbled together from biased searches (ATF4, ATF5, CHOP, GADD34), comprise a nearly complete list; the single newcomer being SLC35A. And by drawing attention to the fact that their translational induction by the ISR does not entail the loss of footprints on the short repressive uORFs (as predicted by the regulated translation re-initiation model).

An important caveat to these complementary comments is that this reviewer lacks the expertise to judge the technical validity of the RNA seq and ribosome footprinting and defers to other reviewers' expertise in this regard.

The lack of any measureable effect of ISRIB on baseline translation is surprising as there is evidence for basal activity of the ISR: For example PERK_KO, eIF2a_S51A and ATF4_KO cells all share a strong baseline requirement for amino acid supplementation (likely indicating that the ISR contributes to baseline ATF4-mediated gene expression). The authors may wish to comment on this point.
