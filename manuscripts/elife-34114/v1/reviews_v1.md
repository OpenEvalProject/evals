# Peer review - Round 1

Editors:
- Joseph S Takahashi, Howard Hughes Medical Institute, University of Texas Southwestern Medical Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.34114.036](https://doi.org/10.7554/eLife.34114.036)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Transcriptomic analyses reveal rhythmic and CLOCK–driven pathways in human skeletal muscle" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Fiona Watt as the Senior Editor. The following individuals involved in review of your submission has agreed to reveal his identity: Joseph Bass (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission

Summary:

In this manuscript titled 'Transcriptomic analyses reveal rhythmic and CLOCK–driven pathways in human skeletal muscle', the authors performed RNA–seq analysis in muscle tissue biopsies (in vivo) and cultures of synchronized primary differentiated myofibers (in vitro) from human subjects, allowing them to compare cell autonomous and non–cell autonomous rhythms of transcription. Of note, the authors found that rhythmic transcription of genes involved in glucose transport (i.e. GLUT4 regulation), lipid metabolism and immune response were present in both the in vivo and in vitro samples. However, many other genes which were rhythmic in vivo did not appear rhythmic in vitro, suggesting that there are non–cell autonomous factors controlling rhythmic transcription in human muscle. In addition, since total RNA was used, both pre–mRNA and mature mRNAs were quantified. Indeed, the authors identified genes which oscillate at both the transcriptional and post–transcriptional levels. Finally, the dependence of rhythmic transcripts on the core molecular clock was determined using siRNA–mediated knock down of CLOCK in the primary myotube cultures. siCLOCK myotubes displayed reduced expression of many genes which were found to be rhythmic in vitro. The authors also determined that siCLOCK myotubes display reduced insulin–dependent and –independent glucose uptake, suggesting reduced activity of the GLUT4–transport mechanism. Overall, the finding that the circadian clock controls glucose and lipid metabolic gene expression in primary human myofibers is important and provides further evidence of the role of the molecular clock in the regulation of muscle function and glucose homeostasis.

The daily transcriptome analysis of the human muscle biopsies taken at 4 h intervals across 24 h from 10 healthy individuals serve as a valuable and important resource, especially in view of the current attempts to map circadian rhythmicity in humans. In this regard, a more rigorous comparison between available detests of mouse muscle transcriptome (e.g. McCarthy et al., 2007; Miller et al., 2007; Dyar et al., 2014; Zhang et al., 2014; Hodge et al., 2015) with this new data would provide interesting insight regarding the difference in muscle rhythmic gene expression between mice and humans, and likely between nocturnal and diurnal species, respectively.

The major strength of this study lies on the expression data obtained from human healthy individuals in a well–controlled manner, this section by itself is an important resource.

The in vitro experiments primarily corroborate previous studies done with cultured cells (e.g. Krishnaiah et al., 2017) that show dramatic reduction in rhythmic gene expression in culture compared to organs in vivo.

Essential revisions:

1) The in vivo biopsy samples were taken from the vastus lateralis muscle whereas the in vitro samples were from gluteus maximus. Therefore, is it possible that the observed gene expression differences observed between the in vitro and in vivo sample sets are explained by the fact that they are derived from different muscles? One option to address this would be to compare gene expression profiles from biopsies of VL and GM muscles – do they differ in a similar way to the in vitro versus in vivo gene sets? This may beyond the scope here.

2) The authors observed gene expression changes with siCLOCK that support increased mitochondrial oxidative/type I muscle remodeling. This result is consistent with what was observed in RNA–sequencing studies in Bmal1KO mouse muscle (Hodge et al., 2015). However, others have provided evidence for reduced mitochondrial oxidative metabolism in Bmal1KO muscle cells. Therefore, it is possible that the gene signature does not equate with the metabolic phenotype. For instance, gene expression changes may be compensatory rather than causal? In the absence of such analysis, discussion should acknowledge the interest in future functional bioenergetic profiling (e.g., respirometry with mitochondrial fuel substrates).

3) The mathematical model used to detect rhythmicity should be validated on an existing dataset or a demo dataset in order to compare their results with established and widely used algorithms that detect rhythmic profiles, such as JTK_CYCLE (Hughes et al., 2010) and Meta Cycle (Wu et al., 2016) that incorporates ARSER, JTK_CYCLE and Lomb–Scargle.

4) It would be interesting to compare the genes identified as rhythmic in cultured U2OS cells (Krishnaiah et al., 2017) with the ones identified in the current study, even though these are completely different cells. It might shed light on genes, aside from the core clock, that globally maintain rhythmicity in culture.

5) The authors conclusion that the cell–autonomous circadian clock has an essential role in coordinating muscle glucose homeostasis and lipid metabolism in humans should be revised as it is not supported by their results. Their finding that knockdown of clock in vitro affected the overall expression of ~8% of all genes with genes related to glucose and lipid metabolism suggests that the CLOCK protein itself modulate their expression and not necessarily the oscillator. Furthermore, the result that only few genes maintain rhythmicity both in vivo and in vitro, most of them are core clock components, does not support it either.
