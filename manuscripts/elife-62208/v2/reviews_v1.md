# Peer review - Round 1

Editors:
- Detlef Weigel, Max Planck Institute for Developmental Biology Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62208.sa1](https://doi.org/10.7554/eLife.62208.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The genome of the fungal pathogen Verticillium dahliae can be partitioned into evolutionary stable core regions and evolutionarily dynamic regions that are repeat-rich, gene-poor, devoid of house-keeping genes, and instead encode genes important for host-pathogen interactions; identifying such "adaptive", lineage-specific portions of pathogen genomes is both interesting in its own right and has implications for agricultural practices. The current study reports a large amount of genetic and epigenetic data that are used to train a model to distinguish core and adaptive regions of the genome, which in turn allows a larger fraction of the genome to be identified as potentially adaptive. The model is validated with a diversity dataset, which confirms that the regions classified as adaptive are more likely to contain lineage-specific sequences. Future work will reveal whether different epigenetic marks contribute to different modes of evolution, or whether they are merely a consequence of different selective forces acting on the different regions.

Decision letter after peer review:

Thank you for submitting your article "A unique chromatin profile defines adaptive genomic regions in a fungal plant pathogen" for consideration by eLife. Your article has been overseen by Detlef Weigel as the Reviewing and Senior Editor, and three peer reviewers. The following individual involved in review of your submission has agreed to reveal their identity: Brett M Tyler (Reviewer #1).

The reviewers have discussed the reviews with one another and have drafted this decision to help you prepare a revised submission.

As we have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

The fungus Verticillium dahliae is a broad host-range plant pathogen. As in other filamentous plant pathogens, its genome can be partitioned into evolutionary stable core regions and evolutionarily dynamic regions that are repeat-rich, gene-poor, devoid of house-keeping genes, and instead encode genes important for host-pathogen interactions. Identifying such "adaptive", lineage-specific (LS) portions of pathogen genomes is both interesting in its own right and has implications for agricultural practices.

It has been shown before that these regions (or even entire chromosomes) can exhibit particular epigenetic marks and sequence composition (for example in Fusarium, Zymoseptorira, Leptospheria, Botrytis and others). The current study builds on these observations. It reports an impressive amount of data including whole-genome bisulfite, histone modification, DNA accessibility and RNA-seq data for V. dahliae, and these data are used to train a model to distinguish core and adaptive regions of the genome, which in turn allows a larger fraction of the genome to be identified as potentially adaptive. The model is validated with a diversity dataset, which confirms that the regions classified as adaptive are more likely to contain lineage-specific sequences.

What remains to be demonstrated is how the expanded set of "adaptive" regions reported here can be used to advance our understanding of the processes that underlie genome compartmentalization in filamentous plant pathogens, and how different epigenetic marks contribute to different modes of evolution, or whether they are merely a consequence of different selective forces acting on the different regions.

Essential revisions:

1) Too little attention is paid to chromosome organization such as centromeres and pericentromeres, which are linked to differences in epigenetic states.

2) A mutant strain impaired in DNA methylation (Δhp1) is used to show a role of HP1 in DNA methylation in V. dahliae. This functional aspect could greatly enhance the study, but is currently poorly integrated in the remainder of the work. It is not clear if the Δhp1 mutant has an overt phenotype or is altered in its gene expression pattern. The Δhp1 mutant must be more fully characterized as to changes in gene expression between core and LS regions.

3) Throughout the manuscript there is reference to repeat induced point mutations (RIP) without comments on the paradox that V. dahliae is asexual and that the RIP mechanism is associated with meiosis. Could the signatures of RIP reflect mutations that accumulated in an ancestral sexual population of V. dahliae? The absence of RIP mutations from LS regions would seem to be in agreement with these regions having evolved only after the transition to an asexual lifestyle. Also, in agreement, it has previously been shown that TEs associated with LS regions tend to be younger. We ask you to follow up on these previous conclusions.

4) You divide all TEs into four classes (subsection “Transposable element classes have distinct genomic and epigenomic profiles”). Could some patterns be obscured with this broad classification? It appears that the bimodal distributions in Figure 2B reflect different dynamics of different TE (sub)families. Please provide a more fine-scale analysis of properties associated with specific TE (sub)families. Group3 elements are associated with genes that show stronger in planta induction. You should elaborate more on this observation, for example, by describing where in the genome these Group3 elements are located.

5) The machine learning section suffers from a confusion of purpose. You begin by training four algorithms to predict core and lineage-specific (LS) regions from the chromatin data, attempting to minimize false positive and false negatives. Then you pivot, and hypothesize that the remaining false positives may in fact be true positives (previously unclassified LS regions). Validation with new Presence/Absence Variation (PAV) and RNA-seq data supports this proposal. While this approach works, it is not ideal. If you had intended from the beginning to identify new LS regions, you should have created a training data set of high quality core regions (e.g. BUSCO genes and their surrounding regions) as well as high quality LS regions (e.g. genes that encode secreted proteins and that show either PAV or are induced in planta). Furthermore, this curated training data set should contain equal numbers of positive (LS) and negative (core) examples.

6) Following on from the above, in none of the predictions (e.g. in Table 2, Table 3, Figure 6, subsection “Machine learning predicts more lineage-specific genomic regions than previously considered”) do you seem to document which parameter settings were used for each algorithm. As demonstrated in Figure 5, the actual precision and recall vary according to the threshold used to make the binary core/LS call. These threshold parameters should be shown in each case, for example in a diagram similar to Figure 5B or else by showing the optimization curves in the supplement.

Similarly, in the Materials and methods, you state that the optimal parameters for prediction were chosen by maximizing "accuracy". You fail to define "accuracy" but let us assume that you mean [(true positives + true negatives)/all predictions]. This means that, given the heavily skewed distribution of positives and negatives, the optimization will be heavily biased towards minimizing false negatives. In fact, you state "The Matthews correlation coefficient (MCC) [is] an analogous measure to accuracy but more appropriate for unbalanced binary classification". You do not inform us why you used accuracy for the optimizations rather than the MCC, or whether by "accuracy" you intended to convey that you did actually use the MCC.

Here again is confusion of purpose. If you indeed used [(true positives + true negatives)/all predictions], and therefore biased the optimization towards true negatives (core genes) you would inadvertently have liberalized the prediction of false positives. In the absence of a high quality training set, liberalizing the prediction of false positives is actually a good way to improve the search for undetected true positives (LS regions). If this were your intent (which is not discussed), then there would be no need to introduce the MCC except perhaps to explain why it was not used.

7) With this paper, you have substantially expanded the way that LS regions are identified, introducing a much wider range of metrics. Thus, the term "lineage-specific" no longer accurately defines such regions, because it refers only to the use of PAV to define the regions. As you state, you are actually interested in regions responsible for host colonization and adaptation. Continuing to use the term "LS regions" will cause confusion as to whether you refer to regions that exhibit PAV, or regions identified with the new algorithms. This confusion is exemplified by you reference to "old and new LS regions" (subsection “Machine learning predicts more lineage-specific genomic regions than previously considered”). We assume that going forward you do not intend to continue to use the terms "old LS" and "new LS". We strongly recommend you choose a new name for the new, expanded "LS" regions.
