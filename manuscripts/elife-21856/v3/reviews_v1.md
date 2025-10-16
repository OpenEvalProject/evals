# Peer review - Round 1

Editors:
- Danny Reinberg, Howard Hughes Medical Institute, New York University School of Medicine , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.21856.032](https://doi.org/10.7554/eLife.21856.032)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "CUT&RUN: An efficient alternative strategy for high-resolution mapping of DNA binding sites" for consideration by eLife. Your article has been favorably evaluated by Jessica Tyler (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The method described is interesting and compared with conventional ChIP-seq results in higher resolution, lower background, and greater versatility, where mapping of long range interaction showed near base-pair resolution. A limitation/concern is that the method was used to analyze the binding of CTCF (and the centromeric histone variant CenH3). We request that the authors analyze another factor with limited binding sites in the genome such as a pioneer factor that binds to inaccessible, thus regions resistant to light MNAse treatment. Additionally, an explanation as to how the authors can tell direct from indirect cuts due to topology is necessary.

Reviewer #1:

In the manuscript by Skene and Henikoff, the authors developed Cleavage Under Targets and Release Using Nuclease (CUT & RUN), a chromatin immunocleavage (ChIC) based genome-wide mapping strategy. Compared with conventional ChIP-seq, this new method results in higher resolution, lower background, and greater versatility. In this method, native nuclei were immobilized and incubated with antibody against the protein of interest, and treated with protein A-MNase fusion protein for a very short time at 4o C. DNA released from MNase digestion was subjected to deep-sequencing. The authors tested this method with transcription factors including CTCF and with centromeric histone variant CenH3, and reported data with high resolution and sensitivity. Subsequent long-range interaction mapping by this method showed near base-pair resolution. Overall, the study provided a useful option for genome-wide mapping. There are few points that need to be addressed:

1) It could be problematic to use budding yeast to study insoluble DNA-binding protein complexes. Yeast is a relatively simple model system, and more importantly, most of the yeast genome is actively transcribed, which is very different from the mammalian genome. The mammalian genome is more complex and has large regions of heterochromatin. It is not clear if those regions are accessible to the CUT & RUN methodology. The authors should test the applicability of their methodology to mammalian cells. At the very least, the authors must state in the text the potential limitations of this new methodology.

2) It is unclear if the method can be used to probe chromatin states, including a variety of histone modifications. These features are very topical in the field of chromatin biology. Most current genome-wide profiling approaches can provide useful information on chromatin modifications. It would be useful for the authors to test if CUT & RUN can provide data on genome-wide histone modifications. If not, the authors should discuss this deficiency.

3) In the second paragraph of the subsection CUT&RUN robustly maps yeast TF binding sites in situ at high resolution”, how did the authors define "true positives for both TFs"?

Reviewer #2:

The authors describe a technique for quantitative genome-wide mapping of chromatin-bound factors using antibodies and MNase in nucleo, without requiring fixation or sonication. They show efficient and accurate mapping of two yeast transcription factors at high resolution, precise mapping of the centromeric nucleosome, which is rare in abundance and trapped in an insoluble complex, and mapping of CTCF in human cells, including direct binding sites as well as indirect 3D contact points.

The technique is ingenious and the study is very well presented. I particularly want to applaud the authors for including clear and detailed supplementary protocols, which is rarely seen. If the technology worked as well as claimed and were a true alternative for ChIP-seq, I would highly recommend this manuscript for publication. However, I have a major concern about the ability of CUT&RUN to distinguish direct from indirect contacts and additional worries about specificity and versatility that would need to be addressed experimentally.

A) 3D contacts: the authors present the ability of CUT&RUN to identify distal indirect contacts of CTCF as an asset, but to me it appears to be a major limitation. If I understand correctly, of the ~20k sites identified by CUT&RUN, only those showing native ChIP signal (~10%) are direct binding sites; the others are indirect. That would imply that native ChIP must be performed in parallel to CUT&RUN to identify direct binding sites. That seem a major limitation that disqualifies the technique as a full replacement for ChIP-seq. Is this limited to CTCF or they see evidence of indirect sites also in their yeast data? Are these indirect contacts captured by conventional X-ChIP? Is there any way to distinguish direct from indirect bioinformatically or by modifications to the CUT&RUN protocol?

B) Specificity: the authors show convincingly that CUT&RUN is as sensitive or more sensitive than IP methods. They also show that the background noise is lower (e.g. Figure 1D) than in ChIP-seq. However, this is a relatively innocuous type of background as it is uniformly low. A more important question is if CUT&RUN identifies false positive peaks in accessible chromatin regions, as some of the CTCF data seems to suggest. The authors partially deal with this in Figure 5—figure supplement 1, but I believe that it is crucial to address this more thoroughly. Specifically I suggest that:

B1) the authors perform CUT&RUN experiments in cells lacking the targeted protein.

B2) the authors perform detailed analyses to determine false positive rates, including calling peaks for Abf1 and Reb1 and showing that the majority of the top peaks are within motifs.

B3) the authors analyze enrichment over DNaseI hypersensitive sites for all the CUT&RUN experiments and compare it with enrichment in native ChIP and X-ChIP as a measure of false positive rate.

C) Versatility: to claim that CUT&RUN is a "suitable replacement" (Abstract) or even just "an attractive alternative" (Discussion) to ChIP, the authors should show that it can be applied to a similarly broad array of chromatin-binding proteins. Specifically, my concern is that CUT&RUN works best when the targeted protein resides in a nucleosome free region, and the three proteins targeted here belong to that category. The experiment on Cse4 helps but a more broadly distributed heterochromatic protein would be more convincing.

D) Scales: in several points it is hard to follow the comparisons because scales are omitted or vague (e.g. "low" to "high") in genome browser snapshots and heatmaps. They must be included for all plots and the values represented fully described in the text or legends.

Reviewer #3:

The authors build on their previously developed method to dig deeper into the possibilities offered by ChIP variants to precisely map the genomic location of DNA binding proteins. The technique has the potential to be scalable and transferable and thus impactful.

As the authors point out, the preferred method to analyze genomic occupancy is ChIP-seq because of its relatively simplicity and adaptability to different proteins. Other methods that tag specific enzymes to binding sites are inherently more tedious to apply to multiple proteins because they require the construction of protein fusions. Additionally, they sometimes lack resolution or depth. However, they have the advantage of working in native conditions or even in vivo. The presented method has the advantages of ChIP-seq since it requires only an antibody to the protein of interest without the need of generating a transgenic cell lines. Thus, it can be complemented and compared directly to ChIP-seq. It also gains in resolution over conventional ChIP-seq by relying on an enzymatic digestion of the DNA under native conditions. Additionally, by releasing MNase accessible regions, the method reduced background reads. Finally, it allows the investigation of the local accessibility state. Thus, with minor controls it can be a valuable method for the large community studying how specific proteins interact with the genome.

The described robust performance across digestions time is a very positive attribute of this protocol. Other protocols that require MNase digestion are extremely sensitive to its activity and thus very hard to set up. The overlap on size distribution of Figure 1C demonstrate that fragments are of the same size but it is not conclusive for further applications in terms of identity of these fragments. If the size distribution is similar but globally these fragments map to different locations in the genome, the timing on digestion is an extremely important parameter. Although Figure 2—figure supplement 1 attempts to map it, a global mapping and overlap quantification of the data represented for a region in Figure 1D would benefit the understanding of the digestion time importance or lack of it.

The authors compare Cut&Run with ORGANIC ChIP-seq, a previous generation method from their latest improved method. How does this method compare to their latest method to map TF binding at single base-pair resolution published last year?

Cut&Run relies on MNase digestion. How does Cut&Run perform for pioneer transcription factors that bind to inaccessible, thus resistant regions to light MNAse treatment? Thus, should be discussed and perhaps tested (see below).

Related, and in light of this comment "When aligned to CTCF motifs found within DNaseI hypersensitive 245 sites, CUT&RUN and X-ChIP-seq CTCF heat maps show strong concordance": How does it compare to whole genome ChIP-seq? How does the >150bs run compares to an accessibility experiments? Would a MNase experiment be a better background model for peak calling? If true, then the impact of this method should be reworded.

CTCF is an atypical TFs in terms of its ability to ChIP. Few novel protocols have been established and tested with CTCF but fail when repeated with other TFs. Thus, I highly recommend to perform and report a Cut&Run experiment with another TF such as homeodomain. This to me is an important and the only wet experiment the authors should perform. The rest of my comments could be addressed by re-analysis of the data.

The claim about recovering 3D interactions is weak and to me there is not enough support to include this claim in the manuscript. First, it needs the MNase background model. The MNase is not covalently bound to CTCF, thus some of the release fragments could be released at similar frequencies in both conditions, while CTCF-interacting elements will be resealed at higher frequencies. Secondly, no technique is perfect, but discussion about transient binding and its implications for the digestion of certain regions should be suggested. Finally, the most important information from 3C techniques is that they identify the binding partners. Cut&Run even in the best case scenario will identify regions that could be in contact with one of the many CTCF binding sites in the genome.
