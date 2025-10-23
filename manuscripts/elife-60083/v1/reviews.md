# Peer review - Round 1

Editors:
- Christina L Stallings, Washington University School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.60083.sa1](https://doi.org/10.7554/eLife.60083.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript represents important technological and biological advances in our understanding of how different essential pathways in mycobacteria intersect with effects on bacterial morphology, identifying previously unknown functional associations. This study provides a framework for future work that could accelerate our understanding of gene function in mycobacteria.

Decision letter after peer review:

Thank you for submitting your article "Arrayed CRISPRi and quantitative imaging describe the morphotypic landscape of essential mycobacterial genes" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Gisela Storz as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: E Hesper Rego (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

This manuscript combines a CRISPRi library in Mycobacterium smegmatis with high throughput light microscopy and image analysis to investigate the effects of essential gene knockdown on bacterial morphology. The reviewers all agree that there are many technical advances presented in this paper, the experiments are well executed, and the data and its analysis is significant for the field. However, there are some questions regarding the reproducibility of the data and the utility of these data as a predictive tool. The reviewers believe that these questions should be straightforward to address, as described more below.

Revisions for this paper:

1) Questions of reproducibility: The authors state that "Moreover, to verify the reproducibility of the imaging workflow, replicate imaging was performed on separate days for 134 strains."

Does this mean that the authors don't have replicate data for 29 strains? To ensure reproducibility, the authors should perform one or both of the following: 1) Finish collecting the replicate data sets to ensure reproducibility and/or 2) Address reproducibility by comparing the data for the 129 that have been replicated.

The authors should also validate a few genes with a second guide RNA to rule out off-target effects and confirm phenotypes.

2) Questions of utility as a predictive tool:

a) MSMEG_3213 isn't an example of defining the function of an uncharacterized gene instead it simply validates existing database predictions. Further, the data presented here do not demonstrate that MSMEG_3213 is the methylase of an R-M pair. Limitations should be made clear in the discussion of the data.

b) The approach and data falls short of broadly being able to predict the function for any essential gene of interest. The data as presented in Figure 6 do not help this case. While some functionally related genes cluster together, many do not, especially for genes that fall into cluster 2. The disorganization in the UMAP space may stem from the small number of observed phenotypes, whereas published work in other organisms reports much broader ranges of depletion phenotypes. That being said, this isn't a fault of the authors', but it does diminishes their claim to use this method as a predictive tool. The text should be reworded or restructured to clearly represent the utility (or limitations) of these data as a predictive tool.

c) Reshuffling or restructuring some of the sections may help to guide the reader towards understanding the utility of the methods and the data. For example, in addition to describing the methods of their technique, the author's validate or give examples of what their data contain (identification of cryptic putative RM system, histidine auxotroph phenotypes, effects of disrupting mycolic acid biosynthesis). They then discuss the potential to use CRISPRi to confirm compound MOA. This is a lot of information (10 figures with many subpanels), but none of these threads are really taken to completion.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Arrayed CRISPRi and quantitative imaging describe the morphotypic landscape of essential mycobacterial genes" for further consideration by eLife. Your revised article has been evaluated by Gisela Storz (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

1) "An immediate priority is to expand the library to include all 423 predicted essential M. smegmatis genes from our pooled screening data (de Wet et al., 2018) and to perform additional replicate imaging for all mutants to enhance resolution and reproducibility."

While this passage might assuage a reviewer or provide the impetus for a sub-Aim of a proposal, it should possibly be omitted because it implies that the missing data are too important to omit and therefore it is premature to publish the current body of work. A stated immediate priority in a published report is acceptable when it describes the next logical step in a progression identified by conclusions of that publication, but it is less acceptable when it describes a gap in the present step. The wording in the passage sounds like the latter.

The subset of genes selected and currently presented is justified on the basis of conservation with M. tuberculosis, and the degree of reproducibility demonstrated by an independent replicate of more than half of those suggest high value and reliable data.

2) "Although morphological profiling appears to offer a rapid means of preliminary gene function assignment or compound MOA, this approach cannot claim single gene-level sensitivity. Definitive validation is therefore required – via further biochemical and/or functional analysis – to ratify the functional assignments predicted using this tool."

The phrase "gene-level sensitivity" may be misapplied in this context, or at least, confusing. A reviewer points out that the manuscript demonstrates gene-level sensitivity by reducing expression of a gene and the subsequent combination of morphologic effects (phenoprint) places that gene in the Euclidean neighborhood of other genes. The overall passage is aimed at qualifying a limitation of the screen in that it cannot biochemically discern the basis for its inclusion in the neighborhood. Therefore, a clearer and more concise passage would delete "this approach cannot claim single gene-level sensitivity." The resulting single sentence says that phenoprint data does not assign gene function but gene membership to a process or pathway. This can then guide specific experiments of the functional basis for that membership.

3) "Despite lacking single-gene resolution, morphological profiling has the capacity to identify mutants with unexpected phenotypes, providing a preliminary phenotypic characterization which can guide focused downstream investigations towards assigning gene function."

Same comment about the use of "single-gene". Just starting with "Morphological profiling…" could be a clearer statement.
