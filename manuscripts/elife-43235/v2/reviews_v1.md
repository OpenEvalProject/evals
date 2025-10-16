# Peer review - Round 1

Editors:
- Asifa Akhtar, Max Planck Institute for Immunobiology and Epigenetics Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.43235.022](https://doi.org/10.7554/eLife.43235.022)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for sending your article entitled "Acetylation of BMAL1 by TIP60 controls BRD4-P-TEFb recruitment to circadian promoters" for peer review at eLife. Your article is being evaluated by two peer reviewers, and the evaluation is being overseen by a Reviewing Editor and K VijayRaghavan as the Senior Editor.

The points that need to be addressed are given in the reviews below. A very important one to address is the conflict with what was previously known for BMAL1 acetylation of K538 by CLOCK leading to repression (Sassone-Corsi and co-workers) in comparison to the rather unconvincing effect of Tip60 KO on BMAL1 acetylation and interaction with Brd4 (IP-WB). Further, the way the data- analysis is presented, it is not possible to know how the ChIPs were calculated/normalized, unless this information has been missed.To reiterate, the authors would really need to address the weakness of their biochemical data. One supplementary data set arguing that CLOCK does not acetylate BMAL1 is not compelling to revise earlier reports.

Reviewer #1:

This interesting study presents data supporting a role of Tip60-dependant acetylation of BMAL1 to allow expression of circadian regulated genes. The acetylation of a previously identified single lysine on BMAL1 is argued to be at the center of a mechanism controlling Brd4/P-TEFb recruitment, allowing RNAPII pause release and productive transcription elongation. A large amount of data is presented to support the conclusions and endogenous acetylation site mutant of BMAL1 (K538R) is characterized after CRISPR-mediated genome editing.

While the model presented appears well supported by the data, it is very strange that it is not put in the context of known important literature directly linked to what is studied here. For example, BMAL1 acetylation on K537 (mouse, K538 in human) was published in Nature 2007 (Sassone-Corsi lab), shown to be done by CLOCK lysine acetyltransferase activity (BMAL1 heterodimer partner) and oscillates during the circadian cycle, peaking with the repression phase. It was argued that BMAL1 acetylation on K537 leads to repression of circadian regulated genes, through recruitment of CRY1. Ectopic expression of BMAL1 K537R mutant was shown to disrupt circadian rhythm. This is very different to what is proposed here.

Related to that, the authors state that they tested Tip60 as the KAT for BMAL1 because it was previously shown to co-IP with CLOCK/BMAL1 (Sassone-Corsi lab, Cell 2006). Well, that report also showed co-IP with 2 other major KATs, CBP and PCAF, all acetyltransferases previously shown to be present on E-box promoters in vivo… In fact Tip60 and PCAF histone acetyltransferase complexes are well-known co-factors (through their common TRRAP subunit) of Myc transcription factor that binds the same E-box sequences as CLOCK/BMAL1. Interestingly, elevated Myc expression was shown to disrupt the circadian clock (Cell Metabolism 2015).

Tip60/KAT5 is known to prefer the "GGK" sequence as substrate and this is what is found for K538 (BMAL1 sequence "GGKKI"). So modification in vitro with recombinant proteins (or through joint over-expression in transient transfection) makes sense but does not prove per se in vivo physiological relevance (see below).

Specific points about the data:

– Figure 2A:

The effect of K538R on co-IP of CDK9/Brd4 is difficult to judge since there seems to be less BMAL1 signal in the input and the BMAL1 WB signal is saturated. I suspect the effect is, in fact, minor if any.

– Figure 3—figure supplement 1:

This is a key experiment in the context of the literature that showed CLOCK-dependent acetylation of BMAL1. The data presented here raise some questions as there seems to be higher and more constant acBMAL1 signal in the CLOCK KO cells. From the band patterns on the CLOCK KO membrane it seems that the same membrane was used for both total BMAL1 and acBMAL1. Is it possible that the acBMAL1 signal is, in fact, residual total BMAL1 signal after stripping the membrane? Or non-specific acBMAL1 signal because of the high amount of IPed BMAL1 on the membrane?

– Figure 4C:

The effect of Tip60 induced KO on BMAL1 acetylation in vivo is not convincing since the level of total BMAL1 IPed is lower in the KO sample. The graph below based on n=3 shows a decrease after normalization but since the shown WB is not convincing I do not know what to think. Quantification of single point WB signals is known to be misleading as ECL is not linear. The decrease of acBMAL1 seems similar to the one shown for total BMAL1.

– Figure 5A:

The exact same thing can be said here as for Figures 2A and 4C. The effect of Tip60 KO on BMAL1 acetylation/interaction with Brd4 is not convincing as there is less BMAL1 in the input and the IPed signal is saturated but still points to less IPed BMAL1 in Tip60 KO). An identical problem can be noted in 5C as much less Brd4 is IPed, making the conclusion on BMAL1 interaction being dependent on Tip60 not valid.

In any case, it is clear that BMAL1 still gets acetylated in the absence of Tip60? As the TIP60 coactivator complex is present on the enhancers and promoters of a large number of transcribed genes, the effect of its induced KO can lead to indirect effects on gene transcription.

– Figure 5D:

To distinguish effects on txn initiation vs elongation the authors perform ChIP-qPCR with RNAPII-Ser2ph and TFIIE Abs. To really argue about initiation vs elongation, or pause release, the real readout should be RNAPII-Ser5ph vs Ser2ph?

Overall, all ChIP-qPCR experiments are difficult to efficiently judge as it is not clear from the Materials and methods/Figure legends how these values were calculated. 6B acBMAL1 oscillation not convincing with load. The graphs indicate "relative enrichment" and the Materials and methods state "to unbound regions". But since the values are 1 and below this would mean no enrichment vs the control unbound regions? The ChIP-qPCR methods also state n=3, is this biological independent triplicate experiments? Or technical replicates (same chromatin, 3 IPs)? Or PCR replicates?

Reviewer #2:

This is an interesting paper that explores mechanisms that contribute to circadian regulation of clock gene transcription, using experiments performed in cultured cells and mutant mice

In the first section of the paper, the authors show that periodic expression of a BMAL1-driven luciferase reporter and of several endogenous clock-regulated genes is inhibited by the Cdk9 inhibitor flavopiridol and by JQ1, a BET inhibitor that preferentially targets BRD4, which contributes to P-TEFb recruitment to genes. Consistent with these observations, JQ1 treatment also leads to loss of BRD4 and Cdk9 at the clock gene Dbp and to a decreased in phosphorylation of the Pol II CTD on Ser2. Based on these observations, the authors propose that BRD4-dependent P-TEFb recruitment is a rate limiting step in Dbp regulation. In further experiments, they present evidence that (i) BRD4 (and Cdk9) bind BMAL1 acetylated at lysine 538; (ii) Tip60 acetylates BMAL1 at K538; (iii) occupancy of BRD4, Cdk9, and Ser2P-phosphorylated Pol II at clock genes is reduced in cells expressing BMAL K538R, as is expression of Dbp mRNA and a BMAL1 luciferase reporter; (iv) Tip60 deficiency gives rise to a circadian phenotype in mice, dampening or disruption of cyclic clock gene expression in SCN and in fibroblasts, (v) Tip60 deficiency also leads to decreased BMAL1 acetylation, BRD4, Cdk9, and Ser2P-phosphorylated Pol II at clock genes.

Overall, the data are consistent with the authors' model that the histone acetyl transferase TIP60 contributes to circadian gene regulation by acetylating BMAL1, which in turn leads to recruitment of BRD4 and Cdk9/P-TEFb and release of promoter proximally paused Pol II into productive elongation of several circadian transcripts. I do, however, have a number of minor comments.

Comments:

1) Relevant to Figure 1 and supplemental figures: It would perhaps be more surprising if blocking P-TEFb/Cdk9 or BRD4 activity didn't interfere with clock gene regulation than that it does since they have very widespread roles in gene regulation.

2) The authors used the ratio of Ser2P Pol II/total Pol II as a measure of release from promoter-proximal pausing into productive elongation, but they don't show effects of drug treatments or BMAL1 / Tip60 mutations on total Pol II distribution. I think it would be better to show not only the ratio of these two ChIP signals but also each of them individually so the reader can assess the degree to which the mutations alter Pol II distribution vs Pol II CTD phosphorylation.

3) The authors conclude that BMAL or Tip60 mutation doesn't affect initiation based on evidence that the mutations don't lead to changes in TFIIE occupancy measured by ChIP. Strictly speaking, this is consistent with idea that PIC assembly is unlikely to be affected but doesn't rule out changes in initiation rate.
