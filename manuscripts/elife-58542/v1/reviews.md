# Peer review - Round 1

Editors:
- Christina L Stallings, Washington University School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.58542.sa1](https://doi.org/10.7554/eLife.58542.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study is interesting and important because by using PacBio sequencing to conduct SMRT-seq based methylome analyses of 93 M. tuberculosis isolates, the authors were able to uniquely provide a detailed description of DNA methylations of M. tuberculosis genomes associated with the presence or absence of certain MTases.

Decision letter after peer review:

Thank you for submitting your article "Epigenetic mosaicism in the Mycobacterium tuberculosis methylome enables phenotypic plasticity without genetic mutation" for consideration by eLife. Your article has been reviewed by Dominique Soldati-Favre as the Senior Editor, a Reviewing Editor, and three reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Josep Casadesús (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

In this manuscript, the authors used PacBio sequencing to conduct SMRT-seq based methylome analyses of 93 M. tuberculosis isolates. This study is interesting and important because it provides a detailed description of DNA methylations of M. tuberculosis genomes associated with the presence or absence of certain MTases.

However, the reviewers agreed that there were a number of concerns that need to be addressed. In particular, (1) the authors' argument relating the roles of the methylation patterns in physiology and adaptation are too strong and not supported by the data in this manuscript, (2) the details of the methylation analysis were not clearly described in enough detail, and (3) the "mosaic" finding itself is not new or novel, which needs to be acknowledged and addressed. The storyline of the paper needs to be substantially changed to be more descriptive and data-based (instead of speculation-based). The manuscript should also be edited to be clearer and more concise for the reader as well.

Essential revisions:

1) Add detailed method descriptions for the analysis portions of the manuscript.

2) The physiological consequences of mycobacterial gene expression control by DNA methylation remain to be identified. Therefore, the benefits of phenotypic heterogeneity remain hypothetical. This caveat should be emphasized throughout the manuscript. As support, the authors might perhaps cite game theory papers indicating that phenotypic heterogeneity can be an adaptive strategy in bacterial populations. Here are a few examples (among others):

Wolf, Vazirani and Arkin, 2005.

Ficici and Pollack, 2007.

Lambert and Kussell, 2014.

3) Results subsection “Diverse mutations drive DNA methyltransferase activity profiles”. The interpretation that intermediate IPD ratios are due to heterogeneous methylation looks reasonable. However, heterogeneous methylation is naturally found in batch cultures during DNA replication unless the bacterial culture is synchronized, which obviously is not the case here. Because formation of hemimethylated sites occurs at different regions in individual bacteria, the DNA hemimethylation patterns vary from cell to cell. This can introduce noise into SMRT-sequencing, and in this study it might lead to overvaluation of cell-to-cell DNA methylation heterogeneity. The risk of hemimethylation-associated noise decreases in non-dividing cells. The growth stage of the culture used for SMRT-sequencing is not indicated in the manuscript (the authors cite Elghraoui, Modlin and Valafar, 2017, which does not give details). If non-dividing cells were used, it should be clearly indicated. Otherwise, evidence for stochastic DNA methylation would be less compelling.

4) Results subsection “Transcription factor occlusion explains most hypomethylated sites” and thereafter. The statement that transcription factor occlusion explains most hypomethylated sites should be toned down. The data presented are based on bioinformatic analysis only. Proof of transcription factor binding requires biochemical evidence (e. g., gel shift analysis or DNA footprinting). Without proof of this kind, predictions on DNA binding by transcription factors are speculative.

5) Discussion section. Gries et al. (2010) and Saecker et al. (2002) are wrong citations, not appropriate to support the statement that DNA methylation alters biophysical properties that tune promoter strength. These papers do not mention DNA methylation. Papers that address the effects of DNA adenine methylation on DNA structure include Diekmann (1987), Polaczek et al. (1998) and Kimura et al. (1989).

6) To improve the manuscript to better convey a clear message, reorganize and revise to highlight the focus on MTase mutants and their effects on methylation:

a) MTases' genotyping from WGS and their activities from IPD ratio-based analysis; as well as their demonstration in population, i.e. phylogeny tree;

b) MTases-based methylation heterogeneity from native IPD value-based analysis, suggesting to move Figure 3E, 3F, and 3G (H37Rv-metA, less important) to supplemental and to move Figure 3—figure supplement 1 (MamB) back to Figure 3 with mention of HsdM in the text;

c) MTases-based comparative methylomics for hypervariable sites and hypomethylated sites, and their potential association with transcription factors;

d) MTases-based comparative methylomics for promoters and SFBSs, including RNAseq re-analysis.

7) The use of knock-down (KD) and knock-out (KO) is usually for change of gene/protein quantity or expression level. It may be more appropriate for the authors to use high- (WT), low- (KD), and in- (KO) active mutants for mutation-caused changes of MTase activity.

8) Epigenetic mosaicism is somewhat associated with MTase activity, high or low, and MTase activity is certainly linked to genetic mutation or genotype. As such, "without genetic mutation" in the title and throughout the manuscript is not accurate, and should be toned down.

9) Results subsection “Virulent M. tuberculosis type strain H37Rv poorly represents methylomes of recent clinical isolates”: while H37Rv was recognized as a poor reference for methylome, a better one from the assembled/analyzed should have been suggested/used. Please specify the reference if used.

10) Since only SNP analysis was considered for phylogeny tree, the effect of insertion/deletion to methylome and methylomics analysis should be mentioned in Discussion section.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Drivers and sites of diversity in the DNA adenine methylomes of 93 Mycobacterium tuberculosis complex clinical isolates" for further consideration by eLife. Your revised article has been evaluated by Dominique Soldati-Favre (Senior Editor), a Reviewing Editor and two peer reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

The reviewers all agree that the revisions have strengthened the original story and the authors' responses to the reviewers look reasonable. Most importantly, problematic data and/or statements have been either clarified or removed in the revised manuscript. There are a few text revisions that the authors should address before formally accepting the manuscript, as detailed here:

1) The name HsdM should not be used for an orphan DNA methyltransferase. The acronym hsdM has been used for decades to designate the DNA methyltransferase subunit of type I restriction-modification systems (see, for instance, Loenen et al., 2014). I perfectly understand that the authors use HsdM in accordance with previous literature, and I am aware that a name change can cause complications and confusion. Despite this inconvenience, the enzyme should be renamed to make it clear that it is not a subunit of a R-M system. How about renaming the enzyme at or near the end of the manuscript and citing Loenen et al., or any another review on restriction enzymes?

2) Introduction. The authors write that recent SMRT-sequencing studies have revealed that DNA methylation has roles beyond restriction-modification. This statement is unfair to the literature. In γ-proteobacteria, Dam methylation has been known to control DNA replication, mismatch repair, transposon activity and regulation of transcription since the 1980's and roles in bacterial pathogenesis were described in the late 1990s. In α-proteobacteria, control of the cell cycle by CcrM methylation was described in the 1990s and roles in pathogenesis in the first years of the century. Please modify the sentence. SMRT has been a fantastic breakthrough but not the beginning of the story!

3) Results section. Please change "inactive mutation" to "loss-of-function mutation". "Inactive" may suggest that the mutation does not do anything while the actual fact is the opposite.

4) Results section. When you mention that hypomethylated sites have been detected in bacteria different from M. tuberculosis, you cite Blow, 2016 (which is fine) and Minch et al., 2015, which does not have anything to do with the subject (DNA methylation is not even mentioned in the paper!). Again, it might be advisable to be fair to the literature citing at least one of the pioneer studies that detected DNA hypomethylation in a bacterial genome. For instance, Ringquist and Smith, 1992 and/or Wang and Church, 1992. Alternatively, you might cite a review.
