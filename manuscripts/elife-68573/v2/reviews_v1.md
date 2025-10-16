# Peer review - Round 1

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68573.sa1](https://doi.org/10.7554/eLife.68573.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript is of broad interest to readers in the fields of RNA biology, epigenetics, and early development. The authors provide an exceptionally comprehensive description of the temporal dynamics of mobile element RNA, host defense protein, and epigenetic mark abundance across fruit fly early embryo development. Pairing this descriptive work with the first application of a rapid protein degradation system to maternal proteins in the model fruit fly embryo, the authors reject a previously accepted model that the maternally-deposited protein Piwi establishes gene silencing transmitted epigenetically to later stages of development.

Decision letter after peer review:

Thank you for submitting your article "Maternally inherited piRNAs silence transposons during Drosophila embryogenesis" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Kevin Struhl as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. The three reviewers applauded this exceptionally comprehensive description of the temporal dynamics of transposable element RNA, of piRNA pathway proteins and of H3K9me3 across embryogenesis. The reviewers also agreed that the novel application of the auxin-degron system to maternally deposited proteins in the early embryo opens new avenues of research for the community. Finally, the inference that maternal Piwi may actually not set up epigenetic silencing in later life stages represents an important course correction for the field. You will see below, however, that the reviewers were unconvinced that the current data support the major claim of the paper articulated in title, abstract, and final model, namely, that maternal Piwi is required for transposon suppression. We welcome a revised version of the manuscript that stays closer to the data, guided by the list of essential revisions below.

Essential revisions:

New experiments/analyses

1) The reviewers were unconvinced that the data support the major claim of the paper- namely, that maternally-deposited Piwi silences roo. In wildtype embryos, the dramatic increase in roo by 4hr and especially the sharp increase between 2hr-4hr – compared to the comparatively subtle 2-fold increase upon Piwi degradation – makes careful developmental staging hugely important for inferences from the latter experimental data. An internal control to carefully calibrate the RNA-seq with progression of development is necessary. Moreover, the 297 transposon curiously shows just over 2-fold increase versus control. How can we reconcile this change with log10 mean expression is >3 on the Figure 5D but in Figure 1C, the 297 transposon RPMs are barely registering any RPMs throughout embryogenesis.

2) Related to point 1), the reviewers requested additional timepoints for the auxin-induced degradation experiment. Specifically, RNA-seq or even just qPCR well-after the timepoints reported for both roo and 297. These timeports are important for determining if these two elements still drop to original low levels by 12hr or 17hr despite Piwi degradation at the beginning of embryogenesis. If so, the major claim of the paper would be yet further undermined.

3) The reviewers appreciated the compelling loss of H3K9me3 across the genome and at roo insertions upon Piwi degradation. However, the reviewers were less convinced of the significance of H3K9me3 depletion for gene regulation. For example, in Figure 5-SuppFig-1D, the roo insertion with H3K9me3 is overlapping Hid promoter, it seems surprising that there is little change in Hid mRNA levels after auxin induced degradation and loss of H3K9me3 signal. Related, for Figure 3B, the authors should overlay their RNAseq data with the ChIP-seq tracks for lbm and Tsp42El (which are both normally expressed in the embryo). If the pattern is like what is shown on Flybase, lbm and Tsp42El expression may actually increase during embryogenesis in the same degree of H3K9me3 accumulation around the roo insertion. This pattern could oppose the model of direct or meaningful silencing by piRNAs. While there is clearly a piRNA-chromatin response at roo insertions, the effect on roo silencing may actually be quite modest, and the modesty of this effect may contribute to the perplexing lack of any later developmental phenotypes from the auxin-induced Piwi degradation.

4) The reviewers agreed that one of the most impactful contributions made by this report is the rejection of the model put forward by Gu and Elgin. To further probe what may account for the differences between the two studies, the authors could take advantage of their own data. Specifically, in Gu and Elgin, they found different TE families responded differently to the depletion of maternal Piwi – authors could pull these TE families from their genome-wide data to investigate the dynamics (expression and K9 enrichment in response to maternal piwi depletion), further addressing this discrepancy.

Language modification/softening claims/key clarifications

5) Even if the 2-fold increase in roo holds up after more rigorously controlled developmental staging, the reviewers remained unconvinced that such a subtle change (compared to the dramatic spike in roo expression WT embryos) warrants the current title (and the model in figure 5). Unless, for example, the 2-fold increase triggers additional roo transposition (as assayed by WGS), then the title/model appears overstated. Modification of this claim in the title, abstract, and discussion is required.

6) In the ovary, roo is the transposon family with the highest density of antisense piRNAs present and roo mRNA is strongly upregulated upon combined Aub/Ago3 knock-down (Senti et al., 2015). By contrast the authors state that roo is not regulated by the ovarian piRNA pathway (lines 760-763). Their statement, however, is based only on nxf2 KO flies, which inhibit specifically coTGS and not PTGS, in line with previous findings of roo being insensitive to Piwi-mediated regulation in the ovary (Théron, NAR 2018). A revision of this interpretation and referencing the papers showing potent piRNA-mediated regulation of ovarian roo transcripts by PTGS is necessary.

7) The authors' finding of 297 is interesting but needs more elaboration. Based on previous functional studies of piRNA coTGS mutants (e.g., piwi, mael, arx, mael), 297's response is categorized with TE families that are classified as "opposite categories" by authors' data and interpretation – 412 and mdg1 families. In these previous studies, similar to 412 and mdg1, 297 has burst transcription and reduced K9 in these mutants in ovarian somatic cells. I am puzzled by how to reconcile the authors' interpretation of Roo and 297 with these previous findings. Based on Figure1 – SfigF, the expression dynamics of 297 differs from that of roo. Can this be attributed to the absence of normalization by copy number?

8) Since roo is known to be potently regulated through PTGS in the ovary and Aub is maternally inherited, conclusions about somatic piRNA-mediated regulation of roo (and other PTGS-targeted transposons) requires depleting Aub in addition to Piwi. If this experiment is not feasible, a description of the limitations of Piwi depletion specifically regarding likely redundancy between embryonic coTGS and PTGS by Piwi- and Aub-piRNA complexes, respectively, is essential.

9) Images requires quantification. In Figure 2-supplement 1, for example, by only glancing at the images for piwi, panx, and nxf2 vs H2Av localization, I would not have drawn the same conclusion as the authors. Authors should quantify the co-localization of GFP and RFP foci to support their conclusion.

10) The reviewers found omissions in the methods section that require attention.

a. Given the challenges of diffusing small molecules across dechorionated embryos, additional detail about the development of the auxin systems is warranted.

b. Transposon-calling method in the w1118 genotype and the strain with the AID-tagged Piwi should be reported. In the auxin-degron study, the sequenced strain would be heterozygous, complicating TE calling with short reads. Might the uncertainty associated with calling TEs in heterozygotes have led to the confusing results in Figure 5D and E? (For Figure 5 – SFigure C-E, the H3K9me3 enrichment is not right at the boundary of 297 insertions, but a short distance from it). This is a sharp contrast to Figure 3A-B, which is more typical -are the 297 boundaries inappropriately shifted?

c. It appears that only euchromatic TEs were incorporated into the analysis – if so, please clearly state this.

d. The y-axes should be the same for Figure 2A (for piwi) and Figure 2-SFigE (for panx) and 2-SFigG (for Nxf2) to help with comparison across these factors. Same for Figure 2B and Figure 2-SF and H.

e. Details of the ChIP-seq analyses are missing. For some, the authors used rpm (e.g., Figure 3A) while at other places, authors used fold enrichment (e.g., Figure 5E-was the former not normalized to input while the latter was?)

11) What prompts the massive clearance of the H3K9me across the 177 roo insertions after 10h AEL and does this have a real link to Piwi/piRNA binding to the roo nascent transcripts? Maybe speculate on this more in the discussion?

12) Pg 9 Line 236 To determine whether roo might be competent for retrotransposition in embryos, the authors mined quantitative proteomic data for roo peptides of gag, pol and env, but this just establishes ORF expression, not the act of retrotransposition, which actually requires WGS analysis for new copies of roo TE insertions. I suggest changing to more accurate statement like "To determine whether roo mRNAs are effectively being translated during the pulse of embryonic expression, we mined quantitative proteomic data…"

13) What is the consequence of lower viability of dechorionated embryos in regard to RNA-seq and ChIP-seq analyses. When do the embryos die off and how would this affect the dynamic range of the analyses?

14) Calling the orientation of TEs from short read data is tricky. How were these data validated?

Reviewer #1:

This study provides the most solid characterization of Drosophila Piwi mRNA and protein levels throughout embryogenesis to date, with insightful data on Drosophila embryonic TE expression and H3K9m3 marks, and useful creation of a GFP-AID-Piwi fly strain that enables testing whether maternally contributed Piwi has a direct role in responding to TE expression and H3K9me3 levels in the embryos after auxin-induced Piwi degradation. I applaud the thorough analysis, well written prose, beautiful figures and movies, and well-designed experiments. All the data and reagents from this study need to be shared with the public in a revision of the manuscript that I would welcome to see.

But I have one major contention with the hard push of authors to fit the data to a desired hypothesis and mechanism which proposes that maternally-deposited Piwi/piRNAs have a direct role in "silencing" the roo transposon. This issue begins with the paper's title of "Maternally inherited piRNAs silence transposons during Drosophila embryogenesis". My critiques and interpretation of the data suggest to me that Maternal Piwi and piRNAs are 'Responding' to the major roo transposon expression burst during Drosophila embryogenesis, but the importance of a silencing role is debatable.Reviewer #2:

In this study, Fabry and co-authors combined elegant and novel genetic experiments, live imaging, and functional genomics to investigate the role of maternally deposit piRNA machinery, in particular piwi, in silencing transposable elements (TEs) in developing embryos. Surprisingly, they found that maternally deposited piwi, but not zygotically expressed piwi, plays a dominant role in silencing TE families that are predominantly active in the embryos, especially for Roo and 297. Their developmental time course analysis provides a detailed investigation for the sequential events during embryogenesis, namely the nuclear localization of piwi, the burst of TE transcription, and transcriptional silencing of TEs. While the authors' findings are exciting and seem well supported, there are some incongruencies with previous studies, and these need to be further addressed. This includes that piwi's role in maintaining, in addition to initiating, TE epigenetic silencing in somatic tissues and whether TE family 297's activities and host-directed silencing are predominantly embryonic. The varying dynamics among different TE families may worth further investigation (by performing analyses that are normalized by TE copy number) to gain a full picture of the role of piwi in suppressing not only Roo, but also other TE families. Some technical details also need further clarification. Overall, this is an important study that will further our understanding of how hosts suppress selfish genetic parasites.

Reviewer #3:

Argonaute proteins of the Piwi-clade are best known for their role in germline silencing of transposons, but both Piwi and Aub have been shown to also be highly expressed in somatic cells during early Drosophila embryogenesis raising the question of putative somatic regulatory functions. Fabry et al. address this important question by first performing a detailed characterization of endogenous expression of transposons and the transposon silencing piRNA pathway during Drosophila embryogenesis (Figures 1-3) and then an experimental test of the embryonic functions of maternally inherited Piwi/piRNA molecules using a new protocol for degron-mediated protein depletion in dechorionated embryos (Figures 4-5).

In the first part of the paper the authors describe strong embryonic expression of the roo transposon as well as embryonic expression of maternally inherited Piwi. Although this to a certain extent validates previous observations, the authors' comprehensive analyses of transposons and piRNA pathway genes in both transcriptome and proteome data adds a very valuable and novel overview of this gene regulation. In addition, the authors extend on the current knowledge in several places, for example by characterizing Piwi expression from maternal vs zygotic origin (Figure 2E-F).

In the second part of the paper the authors present an elegant implementation of auxin-mediated depletion of degron-tagged Piwi. By auxin administration to dechorionated embryos, the authors are able to deplete maternally inherited Piwi-piRNA protein complexes within 25 minutes. This is an important advance compared to previous RNAi-based methods. In the following analyses the authors describe Piwi-dependent embryonic heterochromatin formation at roo and 297 transposon insertions.

The experiments are in general well designed and controlled and the analyses are broad and comprehensive. As the authors highlight in the last paragraph of the paper, the presented data largely disproves the tested hypothesis of Piwi-piRNA-mediated somatic epigenetic gene regulation in the Drosophila embryo. This finding is important and will be of broad interest for the field.

My main reservation with the current manuscript is that I find the conclusions on embryonic transposon regulation to be unnecessarily overstated. I find that this overstatement somewhat overshadows the important findings that resolve the question of maternal Piwi-piRNA functions in embryo gene regulation.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Maternally inherited piRNAs direct transient heterochromatin formation at active transposons during early Drosophila embryogenesis" for consideration by eLife.

We found the revised language much more in line with the data and were satisfied with virtually all additional analyses, particularly the new data on embryo staging. A few hanging concerns remain that I trust can be quickly addressed. Note that the absence of tracked changes in the revision document made it difficult, at least in two instances, to track stated adjustments to the text. Please point to these changes with line numbers.

Essential Revisions:

1. The referees requested that panel C from the figure for reviewers be included in the main text along with A and B (maybe as part of the supplement to figure 5? (rebuttal point 1)).

2. Please include language justifying the use of different approaches to analyzing the RNA-seq data presented in Figures 1C and 5D (rebuttal point 1).

3. Please add to the main text, possibly in the legend, that the different strains (w1118 and the degron strain) had different 297 insertion numbers/mean expression (rebuttal point 1).

4. Please point to where language referring to "further highlighted the different normalization strategies in…the text" (rebuttal point 1) is found.

5. Please point to where language referring to "Appropriate adjustments have been made to the text underlining the limitations of whole embryo approaches…" is found.

6. Given that the only major publication addressing maternal Piwi impacts on epigenetic silencing uncovered a very different result, additional language in the main text reconciling the current dataset with Gu and Elgin is still warranted. The few sentences added to the revision are not sufficient to help the reader understand the discrepancy. The cited more modest depletion of Piwi in Gu and Elgin should have more modest effects on the Piwi-regulated TEs- the absence of overlap with your more complete Piwi depletion remains to be explained. More, the discovery of no overlap between upregulated TEs in the two datasets lacks reference to the new figure (or at least a parenthetical "data not shown").
