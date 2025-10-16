# Peer review - Round 1

Editors:
- Cayetano Gonzalez, Institute for Research in Biomedicine Spain

Reviewers:
- Bart Deplancke, EPFL Switzerland

## Review text

DOI: [10.7554/eLife.50375.034](https://doi.org/10.7554/eLife.50375.034)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "Cooption of antagonistic RNA-binding proteins establishes cell hierarchy in Drosophila neuro-developmental tumors" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Bart Deplancke (Reviewer #1).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife at this point as there are a number of additional experiments needed that would likely take more than two months to complete. However, if you are able to address all the reviewers' concerns and wish to resubmit a revised article in the future, we would be happy to consider this.

The most important revision points are listed first but please address all the other points raised in the reviewers' reports too.

Essential Revisions:

1) The ubiquitous expression of Chinmo and Syp in all identified clusters possess a problem that weakens the model. Resolving the following issues is fundamental. As it is presented now, the model is not supported by the data.

While Chinmo and Syp are key genes to mark the early and late NBs, the scRNA data shows they are rather universally expressed in all clusters This may be under translational control, which is unfortunately not explored further despite being key for the model that they present in the Discussion.

Similarly, the binding of Imp and Syp to chinmo UTRs implies regulation at the RNA level, but chinmo and syp are both ubiquitously expressed. Here, post-transcriptional regulation seems unlikely given the striking mRNA expression overlap between chinmo and syp.

2) The authors indicate that Imp and Chinmo "form a positive feedback loop", which implies a high extent of co-expression, yet the scRNA-seq data shows that imp is expressed in a minor fraction of chinmo positive cells.

3) The concept of stable heterogeneity needs further experimental substantiation by, for instance, determining if the ratio/behaviour of cell types found in adult porsRNAi brain persists in implanted tumours. Linked to clonal analysis with flybow in the transplanted tumour the results from this experiment would be very informative about the validity of the model.

4) The states with high expression of Imp were put at the beginning of the pseudotime using Monocle. However, Monocle cannot be used to determine the root or the base state of the trajectory. Use RNA velocity to provide further substantiation of the pseudotime ordering.

5) Tumour tissue segmentation using Tissue Analyser must be validated by providing high quality images and their corresponding segmented processed images illustrating that (i) the Mira signal is recognised as a "membrane reference",(ii) the images are segmented accurately with respect to nuclei number, and (iii) cell size distribution is accurately generated.

6) Provide evidence showing that mixed clones result from a common precursor (as argued) rather than from cells moving around or from Chinmo+ cells turning down Chinmo protein levels and upregulating Syp.

7) Provide substantiating evidence when referring to asymmetric differentiation divisions.

8) Most of the analyses focuses on Chinmo, Imp, and Syp, which were already previously implicated in this process. Beyond providing a view on tumor heterogeneity, the scRNA-seq data remains underexplored with respect to new insights into tumor development. Related to this, the model prediction of growth being mostly due fast proliferation of Chinmo+ cells appears somewhat trivial. Please, make a clear statement of what we learned from this exercise.

9) Does experimental evidence derived from only one time-point substantiate the claims on "persistence"?

10) There is a long list of critical quality control data that must be provided (i.e. mapping rate of the sequencing reads; percentage of mitochondria and rRNA reads; scRNA-seq data normalization; clusters stability and others).

Reviewer #1:

Genovese et al., present a set of experiments investigating the hierarchical regulation of neural tumours stemming from asymmetrically-dividing neural progenitors (neuroblasts, NB) in Drosophila melanogaster, mainly focusing on a pair of established RNA-binding proteins Imp and Syncrip, whose antagonistic activity regulates self-renewing potential within the studied system.

The presented study encompasses an elegantly designed and executed collection of assays, which in a relatively comprehensive manner address the posed questions. These begin with the single-cell RNA sequencing experiment, and as much as the authors do not seem to explore the abundance and more global relevance of the obtained results to the fullest, they provide a thorough validation of NB tumours (tNB) development and hierarchical regulation- related phenomena. This validation includes refined clonal analysis and stochastic modelling of the hierarchical scheme of tumour development followed by quantitative analysis of tumour growth. This is completed by an in-depth molecular dissection of the dynamics of tNB development and progression upon silencing or overexpression of relevant regulatory actors as well as elegant in situ immunofluorescence assays incorporating analysis of the number, occurrence frequency and size of tNBs at different developmental stages. Finally, they interrogate the metabolic changes within the tumours by integrating their transcriptomic and molecular data sets.

In sum, this is a well-crafted study with a compelling message. However, several concerns need to be addressed prior to publication:

a) The authors started their study with an scRNA-seq analysis on tNBs. The resulting data are potentially a valuable resource, however, the description of the data is rather crude and its integration in the rest of the paper rather shallow (see also below). This is best illustrated by the fact that most downstream analyses focus on Chinmo, Imp, and Syp, genes that were already previously implicated in this process. Beyond providing a view on tumor heterogeneity, the scRNA-seq remain therefore somewhat underexplored with respect to providing novel molecular / regulatory insights regarding tumor development. Below, a few recommendations:

Technical:

• Quality control. Expect for indicating that "we sequenced 5796 cells with median number of 1806 genes/cell", the author did not provide any other QC measures. What is the mapping rate of the sequencing reads? What is the percentage of mitochondria and rRNA reads? <2,000 genes is rather low, what could be the reason for this? How many reads and UMI per cells were acquired?

• How are the scRNA-seq data normalized. Was any filtering performed? If yes, which criteria were used?

• How was the tSNE map plotted? Is it based on the most variable genes? If so, how were the most variable genes determined?

• The authors mention in the figure legend that "unsupervised clustering using the.… of the Cell Ranger". However, detailed parameters were not provided. Additionally, what are the differentially expressed genes in the clusters, especially cluster 7, onto which the entire study is based.

• As a sanity check, the authors should plot the expression level of pros in the scRNA-seq data.

• How stable are the clusters? Was any silhouette analysis performed?

Biological:

• While Chinmo and Syp are key genes to mark the early and late NBs, the scRNA data shows they are rather universally expressed in all identified clusters (Figure 1B, F). As the authors pointed out (e.g. Figure 1G), they may be under translational control, which is unfortunately not explored further despite being key for the model that they present in the Discussion. For example, the authors indicate that Imp and Chinmo "form a positive feedback loop", which implies a high extent of co-expression, yet the scRNA-seq data shows that imp is expressed in a minor fraction of chinmo positive cells. Similarly, the authors show that Imp and Syp both bind chinmo UTRs, implying (because not elaborated further) regulation at the RNA level with perhaps Imp having a stabilizing function and Syp a destabilizing one. But how can the authors then explain that chinmo and syp are both ubiquitously expressed? Again, one can evoke post-transcriptional regulation here, but given the striking mRNA expression overlap between chinmo and syp, such regulation (and thus large disconnect between mRNA and protein levels) would be rather striking. Resolving these questions seems fundamental to this study since, as it is presented now, the model is not supported by the presented data.

• The authors use Monocle to analyze the trajectory of tNBs, and find that "the states with highly expression of Imp were put at the beginning of the pseudotime". However, while Monocle is designed to find the transition trajectory/pseudotime based on transcriptome ordering, it cannot be used to determine the root or the base state of the trajectory. In addition, it is becoming common practice to seek independent analytical validation for such pseudotime analyses and in this regard, the "RNA velocity" tool (https://github.com/velocyto-team/velocyto.R) is a very exciting and intuitive approach. Finally, it would be valuable if staining of Chimo/Imp/Syp/E93 in one microscopy field would be performed to show that Chimo/Imp and Syp/E93 truly represent two different NB stages.

• The authors focus on cluster 7 and functionally validate its biological relevance. While functionally characterizing all clusters are beyond the scope of this manuscript, the author should at least discuss their significance. The cluster at the right side (Figure 1C, maybe cluster 1 or 8) for example is much separated from the other clusters. Which cells belong to this cluster? Any enrichment for specific biological processes? What can we learn here?

Reviewer #2:

The key question this study tries to answer is how cellular heterogeneity comes about in human neural tumors using Drosophila as a model system. Overall there are a lot of interesting observations in the manuscript, but the main weakness is that it is unclear whether the model system used is suitable to address the question. The manuscript suffers further from extensive borrowing of concepts and terminology that are often used in a very confusing and misleading manner and the paper is written in a highly convoluted way, which makes it a rather tough read. Perhaps the story tries to look at the problem from too many angles, many of them remain largely descriptive (e.g. single cell RNA seq, the modeling, the bulk tumor sequencing). Human tumor heterogeneity is apparent in complex factettes. One important idea is the co-existence of genetically divergent tumor cell clones and many concepts are around to explain their origin, aspects of deregulated development certainly contribute. This manuscripts addresses this later aspect. One could look at the data, however, by judging the analysed tissue as a relatively normal tissue in which certain aspects of normal neurogenesis are due to the applied manipulations not functional, which on its own right is interesting, but framing the findings in the context of the above question appears forced. For instance, many of the molecular mechanism already identified can be directly applied. This contrasts with the observation that in other malignant tumors, that can be experimentally induced, genome instability arises rapidly, if that were the case here, which we don't know, doing genetics (flybow) and interpreting the results becomes much more complex. If genetics works predictably, as for instance the clonal analysis suggests, then this casts doubt on the tumor-like state of the tissue analysed. Looking at the data from a developmental biology point of view, the findings may rather represent faulty neurogenesis in which decommissioning of neural stem cells and interfering with the temporal transcription factor cascades has not occur properly, but that it appears that the cells in question can responds to the normal constraints of fly development in as much as it can when a key regulatory factor is removed. Removing more factors alters/worsens of course the situation.

However, there are certainly valuable insights into fly specific developmental biology processes of neurogenesis and decommissioning of neuroblast divisions.
