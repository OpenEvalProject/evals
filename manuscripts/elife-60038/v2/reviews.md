# Peer review - Round 1

Editors:
- Ivan Topisirovic, Jewish General Hospital Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.60038.sa1](https://doi.org/10.7554/eLife.60038.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This article suggests a hitherto elusive mechanism implicated in resolving ribosome collisions that appears to be distinct from the previously described quality control mechanism wherein aborted translation is sensed by ZNF598. To this end, the authors provide evidence that recruitment of EDF1 to collided ribosomes triggers inhibition of translation initiation in cooperation with GIGYF2 and 4EHP. Future studies are warranted to establish the potential physiological role(s) of this EDF1-driven response to ribosome stalling.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Ribosome collisions trigger cis-acting feedback inhibition of translation initiation" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Ivan Topisirovic as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Senior Editor.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife at this stage.

There was general enthusiasm pertinent to the potential role of the EDF1-GIGYF2-4EHP axis in sensing and resolving ribosome collisions. Unfortunately, however, the reviewers felt that the ribosome profiling studies suffered from insufficient statistical rigor due to the lack of biological replicates. In addition, it was found that the mechanistic data corroborating the latter model were somewhat preliminary and/or open to alternative explanations. Specifically, it was thought that the analysis of ribosome profiling data should be improved by including independent biological replicates and statistically rigorous methodology. This should be complemented by orthogonal validation of ribosome profiling data and ZNF598-dependent stalls. In addition, experiments corroborating the proposed model would also benefit from sufficient replication. Important controls outlined in each of the reviewer's comments should also be included. Addressing issues raised regarding eS10 ubiqutination as well as the potential competition between GIGYF2-4EHP binding to EDF1 vs. ZNF598 would also be appreciated. The latter experiments should be carried out using more direct approaches (e.g. co-IP). Finally, excluding and/or considering alternative explanations pertinent to studies employing emetine was also thought to be warranted.

We realize that this news will be disappointing. If you plan to address these issues and resubmit this study to eLife as a new submission, we will try to expedite the review process by sending the manuscript to the same reviewers that reviewed the initial submission and include your responses to the reviewer comments from this round of evaluation. We hope you will find these comments constructive in planning your next steps.

Reviewer #1

In this study, Juszkiewicz et al. provide evidence suggesting a previously unappreciated mechanism of resolving ribosome collisions centred on EDF1. This mechanism appears to be distinct form the quality control mechanism wherein aborted translation is sensed by ZNF598. To this end, the authors provide evidence that recruitment of EDF1 to collided ribosomes may inhibit translation initiation via recruitment of GIGYF2 and 4EHP. Based on these data, it is proposed that EDF1 examines mRNAs for increased ribosome density, followed by the recruitment of GIGYF2 to block initiation and facilitate resolving of ribosome collisions. Failure of this mechanism is suggested to be followed by induction of ZNF598-directed mechanism. Overall, it was found that this study is of broad potential interest as it describes a hitherto underexplored mechanism of resolution of ribosomal stalling and collisions. Notwithstanding general enthusiasm for the model, it was found that this study falls short when it comes to including a number of important controls as well as biological replicates to support authors' conclusions. Specific comments are outlined below:

Major comments:

– Several major issues were observed concerning inadequate scientific rigor, including insufficient number of replicates. It is stated in the legend of Figure 1—figure supplement 1 that ribosome profiling experiments were done in 2 technical replicates, which, if not a typo, suggest a single biological replicate. This precludes any meaningful statistical analysis. It is also expected that high reproducibility will be obtained from technical replicates, and it is thus not clear why technical replicates were used en lieu of biological replicates.

– A number of additional issues were noted pertinent to ribosome profiling analysis:

"To determine whether a subset of mRNAs are more dependent on ZNF598 than others, we tabulated the KO/WT ratio of CFr for each ORF. This value was plotted relative to that ORF's total dRPFs as an indicator of sampling depth, and hence reliability of the measurement (Figure 1C). 339 ORFs were higher (defined as ZNF598-dependent ORFs) and 159 ORFs lower than a significance interval defined by two standard deviations flanking a rolling mean".

This is lacking any statistical rigor as there is no adjustment for multiple testing. It would be more appropriate to perform biological replicates and to statistics on these.

"When normalized to the number of background rRNA reads as an internal control..."

Using rRNA to normalize is highly inadvisable as rRNA typically varies for a number of reasons. It also seems that the way rRNA reads are used to normalize the data, does not affect dRPFs to mRPFs ratio.

Figure 1—figure supplement 2: My opinion is that the correct approach here is to establish whether there are more dRPFs when TE adjusted for mRNA length. To this end, Y axis should represent dRPFs, while X axis should represent translational efficiencies calculated as residuals from a regression between mRPFs and mRNA levels (reads only from the coding region should be used). This will adjust for both length of the mRNA and the expression level.

"One explanation for the absence of a correlation is if collisions on highly translated mRNAs are efficiently resolved by ZNF598-triggered disassembly. However, a matched ribosome profiling dataset from ZNF598 knockout (KO) cells showed a similar range of CFr and no correlation with TE (Figure 1—figure supplement 2A, orange dots). This indicates that highly translated mRNAs (as defined by high TE) neither show a higher than average basal collision frequency nor are they preferentially affected in ZNF598 KO cells"

This seems as over-interpretation given how these effects were calculated, and the inherent noisiness of the assay. To make this claims RUST analysis should also be performed.

"…would be more likely to occur on mRNAs with high ribosome density."

It seems equally plausible that local features of the CDS may explain this phenomenon.

"Due to normalization, the above analysis cannot inform about any uniform and wholesale differences in collision frequency between WT versus KO cell"

The authors should corroborate this statement as their data indicate largely uniform effects.

"As exemplified by HNRNPU and RPS4X, some ORFs that did not score as hits when averaging CFr across the ORF nevertheless showed individual collision site(s) that are strongly dependent on ZNF598 (Figure 2C)."

How were these identified? Do they occur more than by chance?

"Such examples indicate that disome profiling is capable of identifying highly specific and strongly ZNF598-dependent stall sites with codon precision".

Seems overstated without any systematic analysis and validation that these indeed represent true events.

"Third, the collision frequency is remarkably similar across a wide range of translation efficiencies"

Data to support this statement were found to be insufficient.

Several other weaknesses were observed:

– "In addition to ZNF598 as the most collision-specific interaction partner, we identified eight other candidate collision-specific proteins."

Can authors explain how were these proteins identified as candidates?

– "Only two of the candidates, EDF1 and GIGYF2, were collision-specific interactors in both WT and ZNF598 KO cells"

How was this calculated/determined?

– Figure 3D – Western blot indicating the extent of ZNF598 depletion is missing.

Reviewer #2

Ribosome stalling and collisions, as well ribosome-associated quality control have drawn considerable attention over the last several years. It was postulated that major substrate for this ribosome rescue pathway are ribosomes stalled on damaged and prematurely polyadenylated mRNAs. The stalls are resolved by no-go decay factors, Pelota-Hbs1, and ZNF598(Hel 2), however there are still gaps in the mechanism of this process. In this manuscript, Juszkiewicz and colleagues, demonstrate an interesting observation that the ribosome collisions may initiate translation initiation inhibition in cis independently of ZNF598 pathway.

Unfortunately, despite the clear support that EDF1 is involved in ribosome collisions and resolution of this process, most of the claims are not clearly or fully supported by the presented data.

1) The complete analyses of ribosome profiling data and dRPF/mRPF ratio has multiple limitations. It is not clear whether these data are analyzed for the sequencing bias and normalization by dividing both sets with same rRNA background reads is problematic. The three conclusions drawn from these data are as such not supported.

2) Authors never report that experiments shown in Figure 3C and Figure 5B are from the same set of data, but they clearly use the same blots in these two figures. Have authors did replicates of these experiments?

3) It is not completely clear how eS10 gets ubiquitinated by ZNF598 in cells missing GIGYF2 (Figure 6). The supplement Figure 6 shows no recruitment of ZNF598 to poly-ribosomes in those same conditions with a rather massive recruitment in case of the WT cells. Authors argue that this could be due to transient interaction of ZNF598 in cells missing either EDF1 or GIGYF2. Is es10 ubiquitinated in HEK293 cells missing ZNF598, or Caco-2 and MCF-7 cells?

4) Original report by Morita et al., 2012. has 4EHP-GIGYF2-ZNF598 complex as translational repressor with direct co-IPs between all components and especially between 4EHP and ZNF598 as well as GIGYF2 and ZNF598. Is EDF1 binding to GIGYF2-4EHP and competing with ZNF598? There is no co-IP studies shown on any components so the reader is left to believe on interactions through the polysome profiles or functional assays.

Reviewer #3

The authors present a study on the dynamics of ribosome collisions and how modulations of the RQC pathway aim to resolve such aberrant events. By using a combination of disome-seq to identify collisions, clever reporter constructs and unbiased proteomics they shed light on different branching of the RQC pathway. Despite some important shortcomings pointed out in the following comments, the methods and conclusions are sound, the paper is well written, and it represent a strong contribution to the field.

1) Steady-state RNA abundance in the different tested conditions has not been measured, making it impossible to appreciate possible changes in translation efficiency for the transcripts displaying collision events. The authors should show that such concern is not valid (the plot in Figure 2B does not represent a sufficient assessment), by experimental methods or analysis of other datasets. If not possible, the Authors should acknowledge this significant shortcoming, and revisit some of their conclusions where necessary.

2) The authors should compare their findings with recent work outlining the crosstalk between translation initiation and the RQC: https://www.biorxiv.org/content/10.1101/792994v1

3) The authors might want to explore the potential sequence/structure features underlying pausing collisions events and their potential in discriminating between ZNF598-dependent and other pausing events. Results from recent work on detecting pausing events should be considered (e.g. https://www.biorxiv.org/content/10.1101/746875v2 , https://www.biorxiv.org/content/10.1101/710061v1 , https://www.biorxiv.org/content/10.1101/710491v1).

4) In the emetine treated samples, the percentage of dRPF reads mapping to the ORF greatly increases. Do the authors observe robust pausing/collisions outside coding regions in the different conditions, or do they represent possible contaminants?

5) Figure 3C shows how both EDF1 and GIGYF2 migrate to the polysome fraction under emetine treatment. However, this might represent a more general phenomenon where many more protein complexes migrate to the polysome fraction. Can the author comment on this possibility?

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Ribosome collisions trigger cis-acting feedback inhibition of translation initiation" for further consideration by eLife. Your revised article has been evaluated by Suzanne Pfeffer (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining textual issues that need to be addressed before acceptance, as outlined below:

1) It was thought that the authors should either tone down some statements or discuss alternative explanations of observed phenomena. In particular, the interpretation that EDF1 recruits GIGYF2 complex at collided ribosomes was found to be insufficiently supported by data. To this end, it was found that although the IP experiments support the role of EDF1 in stabilization of GIGYF2 complex binding to collided ribosomes, their role in its recruitment remains unclear. This should be clearly stated throughout the manuscript and depicted in the model shown in Figure 5. It was also thought that Figure 7 should be removed as this model would require further kinetic studies that, as we agree, are out of the scope of this study.

2) Although highly appreciated, several issues were raised regarding frame-shifting studies. For instance, it appears that EDF1 depletion favours -1 frameshifting which cannot be fully explained by the collision model. Moreover, the authors cite studies that indicate that frameshifting should be in +1 direction. Discussion of these apparent discrepancies appears to be warranted. Potential effects of frameshifting on NMD activation should also be discussed. Finally, RFP signal and RFP/GFP ratios should be presented along with GFP for EDF1 knockdown and KO cells (Figure 4 and Figure 4—figure supplement 1) to further facilitate interpretation of results in Figure 6 and Figure 6—figure supplement 3.

3) It was also thought that the authors should specify number of replicates and precise criteria for some statistical tests. For example, 1.6 fold threshold was found to be quite arbitrary, and the authors should clearly elaborate on criteria to use such cutoff. MS data should be made publicly available and identified factors that are enriched/depleted on collided ribosomes should be at least briefly discussed. The authors are are also encouraged to add all appropriate controls (e.g. showing that ZNF598 is indeed knocked out in the experiment in question rather than referring to previous publications where these lines were established)

4) At times, interpretation of data was thought to require some clarification. Particularly, Figure 2—figure supplement 1A shows apparent increase in mRNA levels, albeit in the text the authors state that there is a lack of the potential mRNA abundance changes. To this end, it was thought that appropriate significance testing is required to corroborate the authors' conclusions, and if it turns out that the changes in mRNA abundance are significant, this should be commented on. Moreover, it is argued that 4EHP, but not GIGYF2 depletion increases translation. However, considering the scale in Figures 2C vs. 2D, it appears that the changes are of comparable amplitude but in the opposite directions. Based on this, significance testing appears warranted.

5) The authors are advised to verify some of the references. For instance in Mills et al., 2016 study does not appear to demonstrate ZNF598 loss during maturation of reticulocytes.
