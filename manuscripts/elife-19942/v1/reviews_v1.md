# Peer review - Round 1

Editors:
- Hugo J Bellen, Baylor College of Medicine , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.19942.039](https://doi.org/10.7554/eLife.19942.039)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Genome-wide Identification of Neuronal Activity-regulated Genes in Drosophila" for consideration by eLife. Your article has been favorably evaluated by a Senior Editor and two reviewers, one of whom, Hugo Bellen, is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Chen et al. used three different neuronal stimulation methods and RNAseq to systematically identify Activity-Regulated Genes (ARGs) in Drosophila. The study identified 12 ARGs (including previously known ARGs, hr38 and striped) that overlap in the three paradigms but also revealed a large number of stimuli-specific ARGs, suggesting that neurons may respond differently to different stimuli. The authors further performed RNAseq on small groups of neurons isolated by cell sorting (Dopaminergic and Pdf neurons, stimulated by the dTrpA1-strategy) and found that although there were some overlaps, many genes were cell type specific. In addition, the authors investigated the chromatin accessibility of the ARGs pre- and post-stimulation and found that in contrast to mammalian IEGs that show some changes in chromatin structure upon stimulation, the fly ARGs are in an open chromatin state to begin with. Together with the findings that fly ARGs are not enriched for transcription factors and small genes, the authors find an interesting difference between mammalian IEGs and Drosophila ARGs, and conclude that fly ARGs are more similar to mammalian secondary response genes (SRGs) or delayed response genes (DRGs). Finally, using the information from these experiments, the authors generated five Luciferase-based reporters and show that three of them show some stimulation induced activation in vivo.

Overall, we feel that the manuscript is well conceived and well written. Identification of new ARGs and showing a proof-of-principal that this information can be used to generate new tools is valuable. In addition, pan-neuronal and subtype specific transcriptomic profiles of neurons treated with different stimulations are also unique and interesting datasets that can be further mined to extract interesting biological information. The finding that, in Drosophila, activity-induced transcription happens downstream of the level of chromatin accessibility will also allow researchers to begin to study the similarities and differences in the mechanism of activity-dependent gene activation between different model organisms. Finally, although not optimized yet, construction of several luciferase based neuronal activity reporter further adds value to this paper. As such, it is likely to be of broad interest and appropriate for publication in eLife; however, there are a few issues that must first be addressed:

Essential revisions (requiring experimental studies):

1) In all of the figures regarding expression profiling, there are no data confirming that the primary findings in RNAseq can be verified by other methods such as qPCR. We assume that the RNAseq was performed on biological replicates (although we cannot find such info in the Materials and methods). Even so we feel that having independent sets of data to backup these primary findings are critical. The authors should take several genes (top candidates from each of the stimulation paradigms that are shared and are unique) and perform qPCR or other assays to detect RNA transcripts (or protein if there is a change) to demonstrate that their findings are reproducible and can be verified by independent methods.

2) The authors find that although there are overlapping genes, ARGs found in different stimulation paradigms are significantly different. The authors speculate this could be reflecting some gene expression changes in non-neuronal cells (glia etc.), global changes that happen independent of neuronal activation (light-response, heat-shock response) or the difference in in-vivo versus ex-vivo experiments. One possibility that the authors do not discuss is the strength and duration of the stimulation. Based on the Methods section, the ChR2 paradigm stimulates the flies only for 30 seconds at the beginning and follow transcriptional changes, while dTrpA1 and high K+ paradigms continuously activate the neurons for the entire duration (up to 60/90min). If the authors perform a longer stimulation in ChR2 flies, they may see more genes that overlap with the other 2 paradigms. Also, in order to determine if the difference between high-K+ stimulation and the other two paradigms are simply due to differences in-vivo and ex-vivo sample preparation, the authors can perform an ex-vivo experiment for the ChR2 and dTRPA1 flies as well and see how that may affect the list of ARGs. Considering that additional RNAseq may require significant time, effort, and cost, the authors can select several high-confident hits from each of the paradigms (see major point 1) and test them via qPCRs or other methods.

3) In Figure 7, the authors show that 3 reporters they generated respond to ChR2-mediated neuronal activation. However, they do not show how these reporters behave in the other two stimulation paradigms (dTrp1A, high K+). Was there a reason the author only focused on ChR2-ARGs? Is the binding site of Lola, Eip78 and Relish enriched in ARG genes activated by the other two paradigms? How do these reporters (and the two that didn't respond to ChR2-activation) behave when stimulated with dTrp1A and high-K+? Since a key conclusion that the authors draw from their RNAseq data is that stimulation paradigms make a big difference, the authors should test their reporter under different stimulation conditions. In addition, the authors should comment on whether their reporter signal is strong enough that they can be used to visualize neuronal activity in all (e.g. elav-GAL4) or subpopulation (e.g. TH-GAL4, Pdf-GAL4) of neurons.

Additional revisions (Textural changes/clarification):

1) Do any of the ARG genes the authors identified have known roles in neuronal plasticity? If so, what portion? This should be included in the Discussion.

2) We cannot find the information of how many flies or brains were used for each experiment. Also, were all of the flies of the same sex or a mix? How old were the flies when these experiments were performed? The authors should provide enough information so that others can replicate the findings.

3) For ChR2-flies, the authors state "A 30-second 10 Hz LED exposure was sufficient to induce a uniform seizure within seconds, and all flies were able to recover within 15 min." For the dTrpA1 experiments, however, no phenotypic descriptions are provided. Did the dTrpA1 flies also show a similar seizure phenotype? If the flies do not show seizures or show a different behavioral defect during the stimulation, the two stimuli maybe acting on different neuronal populations (despite the two proteins being expressed pan-neuronally with elav-GAL4) leading to a difference in the ARG list.

4) The authors should state the amount/concentration of ATR that was fed to theChR2 flies.

5) In Figure 2D, Is the 'weak anti-correlation' between change in gene expression and relative gene length significant? What is the R value?

6) In Figure 7B, there appears to be a second peak of luciferase activity at the end of recording with the eip78C reporter. Is this typical? Background? Non-specific activation? Is the signal observed significantly different from the control (looks very similar)? Additionally, in Figure 7—figure supplement 1, both of these 'control' reporters seem to have less of a response compared to controls. Is there any possible explanation for that phenomenon? Is the difference significant?

7) Many of the experiments used a control with CyO in the background. While we understand that there are advantages to using siblings for comparison, balancer chromosomes often incur unpredictable phenotypes. Therefore, were any steps taken to ensure that the CyO chromosome was not significantly different from WT?

8) In the second paragraph of the subsection “Promoter Regions of ARGs are at Permissive State Prior to Stimulation”, what do you mean when you refer to "all annotated genes"? This phrasing is used several times throughout the manuscript, but is not adequately explained. Does this mean all fly genes, all ARGs or something else?

9) Figure 3: Misalignment of "Dissecte d Brains" in A.

10) In Figure 3, were the 8 genes shown in E selected at random or was there a reason to leave out the other 4?

11) Figure 4: The axes for A and B are not internally consistent; I believe that all coordinates should range from -5 to 5.

12) Formatting of Tables 9 and 10 needs to be adjusted. Also, since only 3 of the columns in both of these tables have different values, the tables could be shrunk down with the rest of the information (which is the same for all columns) described in a legend.
