# Peer review - Round 1

Editors:
- Mia T Levine, https://ror.org/00b30xv10 University of Pennsylvania United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82617.sa0](https://doi.org/10.7554/eLife.82617.sa0)

This important paper will be of interest to scientists studying evolutionary divergence of immune responses and those studying how transposable elements rewire transcriptional regulatory networks. Using a combination of computational and experimental approaches, this work describes a new class of rodent-specific transposons that can act as enhancers of immune genes in mice.


---

# Peer review - Round 1

Editors:
- Mia T Levine, https://ror.org/00b30xv10 University of Pennsylvania United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82617.sa1](https://doi.org/10.7554/eLife.82617.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Mouse B2 SINE elements function as IFN-inducible enhancers" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Molly Przeworski as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Kenji Ichiyanagi (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

There was consensus among the reviewers that the topic is of broad interest and the data were rigorously generated. The reviewers, however, also felt that some of the claims require additional support. A request for new analyses of the current dataset in hand could potentially blunt these concerns. Depending on the results of these additional analyses, a single new experiment would be required to support the inference that the focal B2 element acts as a Dicer1 enhancer. Please see below for specific revisions requested.

Essential revisions:

1) It is not clear whether the Dicer1 locus is unique. Are there other loci that have both a nearby B2_Mm2 element and a binary difference between inducibility in mouse versus human cells? It would be helpful to understand whether there other B2_Mm2 insertions that could contribute to a mouse-specific IFGN-sensitivity. Adding DEseq values from human RNAseq data the authors already use (current references 10 and/or 37) for identifiable human orthologs to Table S7 would thus strengthen their conclusions. If there are many potential candidates, the authors should discuss the rationale for selecting Dicer1 in particular.

2) The results of Serpina3g and Serpina3F gene expression in the authors' knockout cells are very interesting. However, the authors focus almost exclusively on Serpina3g and Serpina3F, which makes it difficult to understand what is happening genome wide. Are other IFNΓ-induced genes (including those not on chromosome 12) similarly affected at the level of basal or induced transcription? How many genes are different in WT versus KO cells, both at basal and induced states? Does this correlate with their CUT&TAG data shown in Figure 5? By focusing only on nearby genes (Serpina3g and Serpina3F), the authors hint that this may be a long-range regulatory effect, "potentially mediated by the CTCF binding activity of the element" that they removed. But by only focusing on two nearby IFNΓ-induced genes, their data do not rule out the (also potentially quite interesting) possibility that there may be a more indirect role for this TE site or Dicer1 in basal transcription of IFNΓ-induced genes or IFNΓ-mediated gene expression.

3) The specificity of the KO effect on the Dicer1-Serpina region of chromosome 12 is not clear. Without analysis of the complete RNA-seq and CUT&RUN datasets, it is difficult to rule out a more global effect (i.e., beyond chromosome 12). If these new analyses yield evidence of specificity of the KO lines, the reviewers will be satisfied. If not, the reviewers request an additional manipulation: KO of an intron element of equivalent size to the original deletion, KO of a different B2 element – apparently there is one 2kb away, or even better, replacement of the B2 element with one that lacks cGAS motifs (though the final suggestion is likely too technically challenging). Determining whether there are changes in the basal or induced levels of Dicer1/Serpina genes in this additional line would serve as an important control for the KO experiment. Providing more data on other genes throughout the genome in WT and KO cells, which the authors have generated but do not include in the manuscript, would help distinguish between these models.

4) There are high levels of POLR2A occupancy at the B2_Mm2.Dicer1 element in induced WT cells. Could this be a Pol2 pause site? Could deletion of this element lead to a change in Pol2 occupancy and change Dicer1 expression independent of enhancer activity? To probe such questions, the reviewers requested that the authors directly test the possibility that the intronic B2 element actually acts as a regulator of splicing or transcriptional elongation. Careful analysis of the Dicer1-mapping reads from the RNA-seq data – or RT-qPCR – could resolve this concern.

5) Figure 4F – The authors claim that "deletion of B2_Mm2.Dicer1 also has a significant repressive effect on the IFNΓ-inducible expression of Serpina genes." However, the basal levels of Serpina3f/Serpina3g are significantly reduced upon this deletion compared to WT. Furthermore, expression of Serpina genes in the KO cell lines significantly increase upon IFNΓ stimulation, suggesting that they still show inducible expression despite the B2_Mm2.Dicer1 deletion. The authors should compare the magnitude of induction before and after stimulation between the WT and KO cell lines to determine if there is indeed a repressive effect on inducible expression of Serpina genes.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Mouse B2 SINE elements function as IFN-inducible enhancers" for further consideration by eLife. Your revised article has been evaluated by Molly Przeworski (Senior Editor) and a Reviewing Editor.

The reviewers appreciated your many additional experiments/analyses as well as the edits to the text. The manuscript has been improved substantially but there are some remaining issues that need to be addressed.

1. All three reviewers felt that the response to Critique#1 was insufficient. There are several places in the manuscript referring to the significance of the Mouse B2 SINE elements contributing to lineage-specific immune response. For example, the introduction highlights that "a key open question is whether the co-option of TEs as immune regulatory elements is evolutionarily widespread as a mechanism driving divergence of innate immune responses."

The reviewers (or at least two of them) did not expect to see additional KO experiments but did expect the authors to highlight a handful of other examples where STAT1 binding to a proximal B2 SINE element is found in a mouse-specific ISG only. If no other such examples are available to highlight, then it's currently difficult to discern how generalizable this relationship is between rodent-specific B2 SINE elements and mouse-specific ISGs.

Furthermore, the authors highlight a limitation of the current human cell dataset – specifically the limitation of sampling gene expression only 24 hours after interferon treatment (new paragraph starting line 310) in human cells. However, in line 232, the same dataset is used to support the earlier statement that "the human ortholog DICER1 does not show IFNΓ-inducible expression in human primary macrophages (Qiao et al. 2016)…mouse DICER1 shows a significant 50% upregulation in response to IFNΓ in primary mouse BMDMs…."

This earlier statement is substantially weakened by the final Results paragraph. This issue needs to be resolved to support the major claim of the paper that a lineage-specific TE is responsible for a lineage-specific immune response, echoed in the abstract: "B2 elements…exemplifies how lineage-specific TEs can facilitate evolutionary divergence of innate immune regulatory networks."

2. In the response to reviewer comments under critique#2, it was stated that "…the other differentially expressed genes in the KOs most likely represent off-target/stochastic changes, that are commonly seen across separate clonal isolations." And as communicated in the manuscript: Line 288: "The other dysregulated genes showed no discernable physical or functional pattern and also showed high variability between individual clones…consistent with intrinsic clonal transcriptional variation…" Whether this is true for all 101 genes should be clarified. It seems surprising given that at least some genes should be indirect targets of Dicer1. Finally, does Dicer1 show less variability than these other genes? If so, that should be stated.

3. Finally, one reviewer was concerned that the intronic location of B2 SINE means that the authors cannot delineate whether the element acts as an enhancer or instead a regulator of transcriptional elongation.
