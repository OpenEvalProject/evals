# Peer review - Round 1

Editors:
- Roberto Bonasio, University of Pennsylvania United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63274.sa1](https://doi.org/10.7554/eLife.63274.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Efficient transcription-coupled chromatin accessibility mapping in situ" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jessica Tyler as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Charles G Danko (Reviewer #1); Junyue Cao (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Essential revisions

1) Reviewers #1 and #3 raise questions regarding the possibility of some accessible regions not being profiled by CUTAC and reviewer #1 suggests to analyze regions bound by CTCF to explore this possibility. Please include these or other analyses to address this point.

2) Reviewers #1 and #3 wonder about the quantitative correlation in addition to the spatial overlap shown. Please include these analyses.

3) While the experiments presented indicate a correlation between transcription and chromatin accessibility, the term "transcription-coupled" in the title implies that a causal link has been demonstrated, but this would require manipulations. We advise you to change the title to better reflect the content of the manuscript.

Additional points

We also think that several of the other points made by the reviewers might help you strengthen this manuscript and encourage you to consider addressing them if possible. The full reviews are included below.

Reviewer #1:

This paper by the Henikoff lab introduces CUTAC, a molecular tool that allows users to sequence DNA inside nucleosome depleted regions accessible to transposition by a protein A (pA)-Tn5 fusion protein. CUTAC builds on the Henikoff lab's exciting new CUT&TAG method. Unlike the CUT&TAG protocol published recently, however, this new work uses low-salt conditions during tagmentation, which appears to promote Tn5 transposition in nucleosome depleted regions adjacent to the primary antibody. The data demonstrating that CUTAC favors transposition inside of nucleosome depleted regions is compelling and clearly shown. Moreover, the new method affords a substantial improvement in the resolution for active regulatory regions compared with CUT&TAG for histone modifications, comparable to that of high-quality ATAC-seq data. Compared with ATAC-seq, there are potentially several compelling advantages of CUTAC, including reproducibility, side-by-side library prep with CUT&TAG, and the possibility of being selective about which open chromatin regions are sequenced (see below). Between these advantages and the authors' past success and broad community interest in the CUT&RUN and CUT&TAG family of methods, I am in favor of publication. I have several comments for the authors:

1) The authors' model is that the primary antibody recruits pA-Tn5 fusion, which then transposes DNA in adjacent accessible regions. However, not all nuclease accessible chromatin is marked by H3K4me2/3. Several lines of evidence suggest that, at least CTCF binding sites have a high level of DNase-I accessibility, but many lack histone modifications indicative of active enhancers/ promoters. Most of the previous work on this subject was done using DNase-I-seq, however presumably the same signal is true for ATAC-seq?! Assuming ATAC-seq shows the same signal, I am curious to know whether CUTAC data collected using K4me2/3 antibodies shows accessibility near CTCF binding sites. An easy way to get at this would be to center on CTCF sites, and break them into classes which do/ do not contain evidence of either K4me2/3 or transcription using ENCODE data. If a heatmap shows similar signal between ATAC and CUTAC at CTCF sites associated with K3me2/3, but only ATAC shows signal at CTCF sites not associated with these marks, then it implies a degree of specificity for open chromatin near the primary antibody as would be expected from the author's model.

2) Selecting which open chromatin regions to measure could be an additional, compelling advantage of CUTAC over ATAC-seq. One could imagine, for instance, using CUTAC to find open chromatin near specific kinds of transcriptional co-activators or co-repressors, Pol II, or (possibly) transcription factors. I would imagine there are a range of applications that would benefit from something like this. Is it worth saying more about this? Or do the authors think that more exploration would be required before this could be stated with any certainty (perhaps the analysis suggested in point #1, above, will help)?

3) To what extent does CUTAC recover the quantitative amount of chromatin accessibility measured by ATAC-seq? Heatmaps suggest the two are highly correlated, as would be expected. It might be useful for readers to see scatterplots that show the correlation in integrated signal near peaks. Note that I would not necessarily expect the correlation to be perfect if there is some specificity for accessible chromatin near H3K4me2/3.

4) In some parts of the text and Abstract, I came away with the impression that CUTAC involves both H3K4me2 and H3K4me3 primary antibodies in the same sample. Based on the main text, however, I think the authors are only using one of these two marks at a time. Please clarify.

5) In Figure 5, please clarify aspects of the CUTAC experiment that were explored in earlier figures were used. Was it me2 or me3? With or without hexanediol or dimethylformamide?

Reviewer #2:

In this manuscript Henikoff et al. present a modification of CUT&Tag, a method that they developed previously to profile chromatin epitopes genome-wide. Here, they show that CUT&Tag can be applied to profile transcription-couple chromatin accessibility sites by simply altering the salt concentration during tagmentation that changes the biochemical binding preferences of the pA-Tn5 transposase. The authors have creatively shown that this method can be performed at home to yield the same results as when performed in the lab, an interesting feature given the current restrictions on laboratory occupancy. The authors claim that while CUTAC takes longer to perform that ATAC-Seq, it gives better quality data than ATAC-seq based on the variation of ATAC-seq data quality between laboratories. The authors assume that all laboratories that perform ATAC-Seq are equally proficient in the technique and that variation is simply due to the technique itself and not the experimentalist. Therefore, it is unclear if CUTAC is indeed superior to ATAC-Seq. Together with the fact that CUTAC is a very minor modification of CUT&Tag, I am not convinced that it is a sufficient advance to warrant publication as a research tool in eLife.

Reviewer #3:

In this manuscript, Henikoff et al. developed a novel approach for in-situ mapping of transcription-coupled chromatin accessibility. Compared with conventional ATAC-seq, this method displays several unique advantages, including high sensitivity and compatibility with parallel Cut&tag profiling. I am rather enthusiastic about the release of this work. Also it is highly appreciated that the authors already uploaded the detailed protocol to protocol.io. For publication in eLife, this work only has several points to be clarified as shown below:

1) In Figure 1AB, CUT&Tag-direct with different starting nuclei numbers gave very different fragment size distributions. Is there a specific reason for this? How does the input nuclei/cell number affect the genome-wide signals?

2) For the divergent outputs from CUT&Tag and CUTAC, the manuscript implies that this is due to different Tn5-DNA binding affinities between low and high salt conditions. Is it also possibly due to that the high salt simply broad the space between nearby nucleosomes for more efficient tagmentation?

3) My major concern for using this approach as a substitution of ATAC-seq is that this method may introduce bias with the use of antibody linked Tn5. Are there enriched H3K4me2 signals in the peaks detected only by H3K4me2 CUTAC compared with peaks detected only by Omni-ATACseq?

4) Figure 5 is helpful for evaluating technique efficiency and qualities. However, the number of peaks per mapped fragments is affected by the input cell/nuclei number and the library's complexity. It would be great if these comparisons are made based on the same number of input nuclei. This is also helpful for comparing the efficiencies of different approaches. Also, how similar is the CUTAC dataset compared with all other ATAC-seq datasets by correlation analysis?

5) For the broad application of the technique, it would be great if the authors can compare the library preparation cost per sample between this technique and conventional ATAC-seq.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Efficient chromatin accessibility mapping in situ by nucleosome-tethered tagmentation " for further consideration by eLife. Your revised article has been evaluated by Jessica Tyler (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

1) Regarding H3K4me2 and ATAC-seq, your response and the revised text state "Using an interval equal to average peak width at half-height, 51.3% of CUTAC and 50.0% of Omni-ATAC sites overlap ATAC_ENCODE peaks." As this was one of the three key requests of the reviewers, the analysis supporting these numbers should be shown, perhaps as additional panel to Figure 4 (ATAC encode peaks) or as a supplementary figure.

2) In Figure 4F, the estimate of 90% coverage of these sites with CUTAC seems generous based on the heatmap. Could you add a horizontal line to clearly indicate where you believe the cutoff is? Also your response mention that you aligned Omni-seq to these sites but it's not shown in the new figure. The reviewer had specifically asked to compare H3K4me2 positive and negative in Omni-seq and CUT&tag.

3) Did you submit Table 1? I could not find it.
