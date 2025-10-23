# Peer review - Round 1

Editors:
- Edith Heard, Institut Curie , France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.23645.025](https://doi.org/10.7554/eLife.23645.025)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Cooperation between a hierarchical set of recruitment sites targets the X chromosome for dosage compensation" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Kevin Struhl as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this manuscript Albritton et al. investigate the targeting mechanisms for the dosage compensation machinery in C. elegans. The nature of the sequences/chromatin features that are required for the targeting of the DCC have been sought, and although rex sequences that are enriched on the X chromosome have indeed been found, unique X-linked sequences do not appear to exist and the question of DCC targeting specificity is still very much open. The authors use ChIP-seq data in embryos, for various DCC components (including SDC-2, SDC-3, DPY-30, DPY-27) and H3K4me3 to identify potential features that can explain X-specificity. The present study analyzed ChIP-seq data for SDC-2, SDC-3, DPY-30, DPY-27 and H3K4me3 in C. elegans embryos to identify the 64 strongest binding sites (for DCC subunits that do not overlap with H3K4me3), all of which are on the X, and then analyzed the features of the 17 strongest binding sites in that set of 64. Their analysis supports the existence of a relatively small number of recruitment sites that share several features which together confer X specificity. Those features include a high-scoring binding sequence, other nearby binding sequences, a HOT domain, and intrinsic DNA-driven nucleosome occupancy. The authors also perform elegant functional studies – deletions and knock-ins of predicted recruitment sites. The emerging model is that SDC-2 and other DCC subunits are initially recruited to relatively few strong recruitment sites, spread to nearby weaker recruitment sites via cooperativity, and can further spread within TADs. The paper is well written and represents a significant advance with novel mechanistic insights into the process of dosage compensation in C. elegans, although some points need to be addressed:

Main Points:

1) Figure 2C shows reduced association of SDC-2 with X recruitment sites in sdc-3 mutants. The authors interpret this as persistent association with the strong sites and loss of association with the intermediate and weak sites and use this as evidence for a hierarchy of recruitment between strong and weak sites. Another interpretation is that SDC-2 association is equivalently reduced at all sites. A possible way to examine this further is via a scatter plot and correlation analysis of SDC-2 binding in wild type versus SDC-2 binding in the sdc-3 mutant. That might help illuminate if in the sdc-3 mutant the level of SDC-2 binding is reduced equivalently or not on strong, intermediate, and weak recruitment sites. It could also be used to address if there are new SDC-2 binding sites in sdc-3 compared to wild type.

2) In Figure 5, how were HOT sites defined i.e. how many TFs bound?

3) The authors should be more cautious regarding the claim that SDC-2 opens chromatin for initial DCC recruitment. They base themselves on the presence of H3 in sdc-2 null mutant at the rex sites (Figure 3A). However, in the absence of SDC-2, this site is not bound by the DCC, which allows it to be chromatinized (hence H3 presence). With the current data, it is difficult to distinguish between chromatin opening and simple occupancy of the site by the DCC (in wild-type animals).

4) Related to the above point, can the authors distinguish if Sdc-2 acts to load the DCC as opposed to trigger focal enrichment (ChIP-seq peaks) at the Sdc-2 binding sites? This could be addressed by analyzing the total number of condensin ChIP-seq tags across the X chromosome (not just peaks) in Sdc-2 (and -3) mutants. If numbers are similar this implies that condensin can still be loaded on the X even without Sdc-2, and that Sdc-2 is therefore likely to be important for concentrating condensin at its binding sites, rather than loading it. Alternatively, if condensin is still present diffusely on the X in Sdc-2 mutants, then the authors might wish to consider a model whereby long range cooperativity arises by pairs of Sdc-2 bound sites blocking the translocation of condensin, leading to focal condensin enrichment, accumulation of chromatin loops and formation of a TAD boundary (see below).

5) The part of the paper dealing with TADs raises some very interesting and important issues but merits some clarification and further analyses:

– In Figure 7A, a horizontal line indicating zero would be helpful. For the rex-41 deletion, the DPY-27 signal appears to be consistently below zero for maybe 5MB, across several strong TAD boundaries. Similarly for rex-40.

– The authors chose a 1MB window to average the DPY-27 signal, and report a "significant decrease in DCC binding across ~1-2 MB regions surrounding each deletion". But with a large 1 MB window the smallest regions that can be detected as DCC depleted seem to be 1-2MB. If DCC depletion were highly localized, for example lost only on one strong DCC site, it is conceivable that it would significantly lower the DPY-27 signal on smoothing windows 1MB in both directions, even though DPY-27 reduction is narrowly localized. It would be helpful to see the data analyzed with significantly smaller smoothing windows in addition to the large-window analysis.

– The authors state that to be able to compare the DPY-27 signal between wild type and each rex deletion strain, they first normalized each to their respective rex-8 locus DPY-27 signal. Are the authors confident that DPY-27 signal at the rex-8 locus is unaffected in the rex site deletions, e.g. that there is not a global reduction of DPY-27?

– In Figure 7B. A horizontal line indicating zero would again be helpful. In addition to the right-most box, 10th from the right box also has an asterisk and is therefore significantly upregulated? The p-values seem not to be very strong. Were they corrected for multiple hypothesis testing? The authors tested >30 boxes, which would make a corrected p-value significantly higher.

– In Figure 7C. This panel addresses an important point. Please explain what this analysis shows.

6) An analysis of rex site orientation would be very informative. Current models of TAD formation suggested by the Mirny and the Liebermann-Aiden laboratories (PMIDs 27210764, 27224481, 26499245), based on an early model from Kim Nasmyth suggest a loop extrusion model involving complexes (e.g. SMC) that are stopped by proteins bound at oriented boundaries (CTCF sites in mammalian cells). The parallel for rex sites with the mammalian Cohesin / CTCF system is striking. The authors could explore the orientation of the motifs presented in Figure 4 at recruitment sites (cf. Rao et al. Cell 2014) to see whether pairs of neighboring strong / weak sites tend to be in a specific configuration (convergent, divergent or tandem). In particular they could assess whether orientation of sites inside clusters correlates with DCC recruitment strength and could potentially explain some results presented in Figure 6 (the orientation is not described in these experiments). This could also be investigated for the TAD boundaries that are found to interact. In this regard, the Crane paper suggests that the strongest rex sites are associated with TAD boundaries, while the model in this paper suggests that strong sites are located inside TADs. A line-up of the relative positions of TAD boundaries and strong/weak recruitment sites will shed light on this. And Figure 8 should be accordingly modified. It would also be informative to show condensin enrichment over oriented strong / weak sites.

7) More detailed information on the bioinformatics approaches – normalization procedures – for the different data sets should be provided. The use of the mixtools package should be better described. Ideally the authors could provide scripts as part of the paper, or even the entire analysis as in some recent cases (PMID 27919068).

8) The authors should correct/modify several statements:i) In Abstract: "SDC-2 is required to open chromatin" – please moderate this statement.ii) The second paragraph of the Introduction – the authors introduce dosage compensation and focus only on male / female differences – they should also discuss X:A ratio dosage compensation.iii) In the same paragraph the authors state that in each case of dosage compensation a protein complex is specifically targeted to the X in only the sex where is regulates transcription: this is not true in mammals, Xist RNA is expressed from the X only when there are 2 or more X chromosomes, regardless of whether there is a Y present or not: thus in XO females, as in XY males, there is no targeting of Xist and its protein partners to the X.iv) The authors state in this paragraph that the targeting of the DCC involves a 2-step strategy – recruitment and spreading – again this is a proposal – it should not be stated as a fact.v) At the end of their introduction the authors mention TADs – they do not describe what these correspond to at all – and it is not clear that TADs are universal entities (for example, see review by Dekker and Heard 2015), particularly in C. elegans (Crane et al., 2015) where they only appear to exist on the dosage compensated X. The authors should explain and cite appropriate references.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Cooperation between a hierarchical set of recruitment sites targets the X chromosome for dosage compensation" for further consideration at eLife. Your revised article has been favorably evaluated by Kevin Struhl (Senior editor), and three reviewers, one of whom is a member of our Board of Reviewing Editors.

The manuscript has been improved but there are a few remaining issues that need to be addressed before acceptance, as outlined in the reviewers comments.

One particular point concerns the new H3 data provided in Figure 3—figure supplement 1. This data is not strong and the H3 plots should probably be left out. Also, in Figure 7C, it is important to explain if the vertical pink line represents 1 or all 3 deletion-affected regions. In Figure 7—figure supplement 5, the TAD boundaries as defined by Crane et al. should also be shown on the same graph. Once these changes and the other minor points outlined below are taken into account your paper will be ready for acceptance.

Reviewer #1:

The authors have addressed most of the issues raised and have improved their manuscript according to many of the suggestions from the reviewers.

There are just a couple of points that are discussed in the response to reviewers points but that merit inclusion in the revised text:

Point 4 "While we cannot exclude the possibility that, prior to sdc-2 expression, some DPY-27 is loosely associated with all chromosomes, the current data suggest that SDC-2 is required for X-specific loading of condensin DC."

Reviewer #2:

This revised submission is certainly improved and almost ready for publication.

The new analysis shown in Figure 2—figure supplement 1 is nice. We are a bit surprised that in panel B all of the intermediate sites and some of the strong sites display more loss of SDC-2 in the sdc-3 mutant than the average across the X. Is the X average of -1.280 in panel B driven by many regions of the X having low levels of SDC-2 in both N2 and sdc-3 (the leftward cloud of gray spots in panel A)? In the main text, I suggest changing "To eliminate the possibility" to "To test the possibility" to avoid having a bias toward certain expected results.

Are the authors convinced by Figure 3—figure supplement 1 that H3 is enriched at the strong sites in EE? The EE profiles look noisy and would need error bars. Most of the EE samples generated by modENCODE were not that early (not necessarily skewed for <40-cell stage as mentioned in subsection “SDC-2 is required to maintain open chromatin at strong recruitment sites, which display intrinsic DNA-encoded nucleosome occupancy”, and later-stage embryos containing more nuclei might dominate ChIP patterns), so using them as representative of pre-DC seems risky. Finally, why are the scales different in Figure 3A and Figure 3—figure supplement 1?

In the legend to Figure 7C, please explain the pink vertical line. Does it represent 1 or all 3 deletion-affected regions?

In the legend to Figure 7—figure supplement 5A, please explain that the numbers in parentheses in panel A are the ranks. In the legend, the sentence "Recent HiC data" needs to be fixed.

Reviewer #3:

This revised version of the manuscript by Albritton et al. integrates all major modifications which we requested on the first review round. Technically, the paper is currently very good and the interpretations of the data careful.

I was however a little frustrated by the analysis of the TAD boundary/rex site orientation and the subsequent discussion, which is limited to the old loading-spreading model.
