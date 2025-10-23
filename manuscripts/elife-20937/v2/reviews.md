# Peer review - Round 1

Editors:
- Clare Blackburn, MRC Centre for Regenerative Medicine, University of Edinburgh , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.20937.038](https://doi.org/10.7554/eLife.20937.038)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Enforcement of developmental lineage specificity by transcription factor Oct1" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Fiona Watt as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this manuscript entitled: "Enforcement of developmental lineage specificity by transcription factor Oct1", Shen et al. have addressed the role of Oct1 in pluripotency and differentiation, by analysing the phenotype of Oct1 null ES cells via both conditional deletion in vitro and after deriving a null ES line. They show that the Oct1 null cells can be propagated under pluripotency conditions with no overt phenotypic differences from the parental line, but cannot undergo normal differentiation when challenged using multiple assays (differentiation to cardiomyocytes and neurons in vitro, and capacity to form teratomas and contribute to chimeras in vivo). Consistent with this, while pluripotency genes are down-regulated normally in the differentiation protocols, differentiation markers are expressed aberrantly. The authors then use RNAseq and ChIPseq (for Oct1, Oct4 and H3K4me3) to address the role of Oct1 during RA-induced ES differentiation. From this, they conclude that part of its effect is to insulate a set of target genes, co-bound by Oct4, from repressive effects of oxidative stress. They also reveal a dynamic interplay between Oct4 and Oct1 binding, where Oct1 takes over from Oct4 as Oct4 levels drop, and suggest this is required to promote lineage-appropriate and suppress lineage-inappropriate expression during differentiation. Overall, the findings are novel and interesting, and the manuscript is well presented. The reviewers have requested the following revisions, which should be addressed in the revised manuscript.

Essential revisions:

1) We request that the authors distinguish between two possible explanations of their data, as detailed below: Oct1/Pou2f1 belongs to the POU family, in which the members share the POU domain as a DNA binding domain. Oct4/Pou5f1 is also a member of the POU family and known as a key transcription factor for establishment and maintenance of pluripotency. The authors have shown that Oct1 and Oct4 bind to mostly different targets in ES cells, although a small proportion of their target sites are shared, indicating their distinct role. Most of the genes occupied by Oct1 do not show differential expression during differentiation, suggesting that these are housekeeping genes. If the regulation of these housekeeping genes by Oct1is required for the survival of a set of differentiated cells, which may happen depending on particular metabolic states, the deficiency of Oct1 would eliminate these cells. Although the authors emphasized that the dysregulation of developmentally-regulated genes is responsible for the defect of differentiation of Oct1-null ES cells, it could alternatively be due to the elimination of the differentiated cells rather than the defect of differentiation event. RA-induced ES cell differentiation is quite a crude system for addressing this point. The authors are encouraged to apply a cleaner system of differentiation and to induce the conditional KO at intermediate states of differentiation event to distinguish these two possibilities.

2) Related to this, the authors are requested to show whether the defects in expression of differentiation marker genes and misexpression of alternative marks shown in Figures 1 and 2 occurs equally across the whole population or only in a subset of cells. These are both possible interpretations of expression data taken from the whole population, but would could lead to different interpretations of the function and mechanism of Oct1 in controlling cell fate. The authors are also requested to clarify whether the defect in the formation of β-tubulin III-expressing neurons in the null versus wild-type cells shown in Figure 2 corresponds to a failure to fully differentiate, or if the null cells are showing slower differentiation kinetics. Was this experiment continued beyond the normal time period of the differentiation protocol, and if so, did the null cells eventually 'catch up' or did they genuinely fail to robustly produce the appropriate neurons?

3) It was previously shown that Oct1-knockdown (~ 50%) in ESCs does not result in any phenotype during neuronal differentiation because of functional redundancy with Oct2 (Theodorou et al. Genes & Dev. 2009. 23: 575-588). To address this inconsistency with their data, the authors are requested to carry out rescue experiments to make sure that Oct1 can rescue the differentiation capacity of Oct1 KO ES cells (e.g. with a constitutively-active Oct1 transgene), in order to confirm the Oct1-dependency of the phenotype.

4) The authors are also requested to deal with the following queries related to data presentation or analysis:i) The authors have generated two germline Oct1 KO lines and littermate WT lines as well as two Oct1 inducible KO lines, however it is not clear whether they have carried out all their qPCR and RNA seq analysis from both lines and pooled together or they have just used one line. It is important to carry out all their experiments in both lines and plot them separately so one can see the variation between the different lines (same genotype) and that between the WT and KO.

ii) The authors have not indicated how many biological replicates they have carried out for their ChIP-seq data. They are requested to clearly indicate the variation between the replicate libraries, which can then be pooled for later analysis.

iii) The authors have only used one algorithm to carry out motif analysis, this analysis should be repeated using a different algorithm (such MEME-ChIP).

iv). Similarly, the authors should examine whether Oct2 can functionally compensate the loss Oct1 and rescue the differentiation phenotype of Oct1 KO ES cells.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Enforcement of developmental lineage specificity by transcription factor Oct1" for further consideration at eLife. Your revised article has been favorably evaluated by Fiona Watt (Senior Editor), a Reviewing Editor, and two reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

As you will see from the reviewers’ comments, there was a remaining concern regarding the interpretation of some of your data. In particular, the data presented in Figure 4G-J do not unequivocally demonstrate that switching from Oct4 to Oct1 is required for differentiation (as noted in the comments from reviewer 1). Therefore, we ask that you add Oct1 staining to the YFP staining presented and, in addition, that you address in the text the possible alternative explanations for these results (you might also consider changing the title in this light). If you do not feel able to make these changes, we would require the rescue experiment outlined by reviewer 1 to be included before the manuscript could be accepted for publication. We also request that you attend to both of the issues raised by reviewer 3, which can be dealt with by textual changes.

Reviewer #1:

In the revised manuscript, the authors made several changes to address the points mentioned by the reviewers. The most important point the authors should confirm was the functional confirmation of the switching from Oct4 to Oct1 on induction of differentiation-associated genes to undergo proper differentiation event. Neuronal differentiation was well-established system and the combination of the inducible KO of Oct1 would allow them to give a clear answer to this question as the reviewers expected. However, the experiment performed by the authors was not well organized and the result was equivocal. If the switch from Oct4 to Oct1 at the beginning of differentiation event is functionally important, the constitutive KO ES cells will fail to give rise to terminally differentiated cells whereas the conditional KO induced after switching will differentiate, even in lower efficiency than WT ES cells. However, induction of KO event at day 4 of differentiation culture, the time point when Oct1 was already replace Oct4 at several target sites as shown in Figure 8F, completely abolished differentiation to mature neurons. This result suggested that Oct1 function is required for the late period of differentiation event or maintenance of the mature differentiated phenotype in cell-type-dependent manner. The assessment of KO event at cellular level was incomplete in this experiment. Why did the authors detect YFP expression, an indirect marker of inducible KO, rather than the loss of Oct1 protein with anti-Oct1 Ab?

An alternative way to address this point precisely is the rescue by the inducible Oct1 expression in Oct1-null ES cells after induction of differentiation. According to the answers to the reviewers' comments, the authors tried to rescue Oct1-null ES cells by transfection of constitutively-active Oct1 transgene at different time point, and failed. Why not using the inducible expression system such as Tet-on system to drive Oct1 transgene? It is well-established system and commercially available.

The strict confirmation of this point is very important to support the hypothesis the authors proposed. Without such confirmation, the other data is insufficient to support the hypothesis. The role of Oct1 for normal proliferation, protection against stress, and maintenance of certain metabolic state in differentiated cell types would explain the defect of Oct1-null ES cells in chimera assay, teratoma assay and slower growth of EBs rather than the defect in differentiation event.

Reviewer #3:

I think Tantin and colleagues have addressed most of the major concerns raised by the reviewers in the first round. After fixing few minor issues (see below), I would recommend the publication of this manuscript in eLife.

Issue 1: Figure 6A and B. The authors compare RNA-seq data of parental vs. KO in both undifferentiated and differentiated conditions. The authors conclude that the KO show more gene expression differences during differentiation. However, it is important to show variability across parental and KO samples separately in both conditions. i.e. one would expect that cells are more heterogeneous during RA-differentiation compared to pluripotency state. So, it is expected to see more difference in RA-differentiation state.

Issue 2: Figure 7B (bottom). the known Oct4-Sox2 motif was enriched in 22.9% of Oct4 unique peaks as compared to Oct4 motif which was enriched 15.3%. This does not make sense as Oct4 motif is the exact first half of the Oct4-Sox2 composite motif. One would expect Oct4 motif to be present in all Oct4-Sox2 (22.9%) sites plus few more sites that only contain Oct4 motif. The authors need to clarify what those percentages mean in the legend.
