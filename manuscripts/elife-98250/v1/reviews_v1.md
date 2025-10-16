# Peer review - Round 1

Editors:
- Stephen D Liberles, Howard Hughes Medical Institute, Harvard Medical School United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.98250.3.sa0](https://doi.org/10.7554/eLife.98250.3.sa0)

This is a valuable manuscript analyzing single-cell RNA-sequencing data from the mouse vomeronasal organ. Convincing evidence in this manuscript allows the authors to identify and verify the differential expression of genes that distinguish apical and basal vomeronasal neurons. The authors also show that Gnao1 neurons exhibit enriched expression of ER-related genes, which they verify with in situ hybridizations and immunostaining and also explore via electron microscopy.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.98250.3.sa1](https://doi.org/10.7554/eLife.98250.3.sa1)

Devakinandan et al. present a revised version of their manuscript. Their scRNA-seq data is a valuable resource to the community, and they further validate their findings via in situ hybridizations and electron microscopy. Overall, they have addressed my major concerns. I only have two minor comments.

(1) The authors note in Figure 4I, and K that because the number of C2 V2Rs or H2-Mv receptors increased while the normalized expression of Gnao1 remained constant (and likewise for V1Rs and Gnai2 in Figure 4-S4C) that their results are unlikely to be capturing doublets. I'm not sure that this is the case. If the authors added together two V2R cells the total count of every gene might double, but the normalized expression of Gnao1 would remain the same. To address this concern, the authors should also show the raw counts for Gnao1 as well as the total number of UMIs for these cells.

(2) As requested, the authors have now added a colorbar to the pseudocolored images in Figures 7. However, this colorbar still doesn't have any units. Can the authors add some units, or clarify in the methods how the raw data relates to the colors (e.g. is it mapped linearly, at a logscale, with gamma or other adjustments, etc.)? Moreover, it's also unclear what the dots in the backgrounds of plots like Figure 7E mean. Are they pixels? Showing the individual lines, the average for each animal, or omitting them entirely, might make more sense.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.98250.3.sa2](https://doi.org/10.7554/eLife.98250.3.sa2)

Summary:

The study focuses on the vomeronasal organ, the peripheral chemosensory organ of the accessory olfactory system, by employing single-cell transcriptomics. The author analyzed the mouse vomeronasal organ, identifying diverse cell types through their unique gene expression patterns. Developmental gene expression analysis revealed that two classes of sensory neurons diverge in their maturation from common progenitors, marked by specific transient and persistent transcription factors. A comparative study between major neuronal subtypes, which differ in their G-protein sensory receptor families and G-protein subunits (Gnai2 and Gnao1, respectively), highlighted a higher expression of endoplasmic reticulum (ER) associated genes in Gnao1 neurons. Moreover, distinct differences in ER content and ultrastructure suggest some intriguing roles of ER in Gnao1-positive vomeronasal neurons. This work is likely to provide useful data for the community and is conceptually novel with the unique role of ER in a subset of vomeronasal neurons.

Strengths:

(1) The study identified diverse cell types based on unique gene expression patterns, using single-cell transcriptomic.

(2) The analysis suggest that two classes of sensory neurons diverge during maturation from common progenitors, characterized by specific transient and persistent transcription factors.

(3) A comparative study highlighted differences in Gnai2- and Gnao1-positive sensory neurons.

(4) Higher expression of endoplasmic reticulum (ER) associated genes in Gnao1 neurons.

(5) Distinct differences in ER content and ultrastructure suggest unique roles of ER in Gnao1-positive vomeronasal neurons.

(6) The research provides conceptually novel on the unique role of ER in a subset of vomeronasal neurons, offering valuable insights to the community.

Comments on latest version:

In the revised manuscript, the authors have thoroughly addressed all of this reviewer's concerns.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.98250.3.sa3](https://doi.org/10.7554/eLife.98250.3.sa3)

Summary:

In this manuscript, Devakinandan and colleagues have undertaken a thorough characterization of the cell types of the mouse vomeronasal organ, focusing on the vomeronasal sensory neurons (VSNs). VSNs are known to arise from a common pool of progenitors that differentiate into two distinct populations characterized by the expression of either the G protein subunit Gnao1 or Gnai2. Using single-cell RNA sequencing followed by unsupervised clustering of the transcriptome data, the authors identified three Gnai2+ VSN subtypes and a single Gnao1+ VSN type. To study VSN developmental trajectories, Devakinandan and colleagues took advantage of the constant renewal of the neuronal VSN pool, which allowed them to harvest all maturation states. All neurons were re-clustered and a pseudotime analysis was performed. The analysis revealed the emergence of two pools of Gap43+ clusters from a common lineage, which differentiate into many subclusters of mature Gnao1+ and Gnai2+ VSNs. By comparing the transcriptomes of these two pools of immature VSNs, the authors identified a number of differentially expressed transcription factors in addition to known markers. Next, by comparing the transcriptomes of mature Gnao1+ and Gnai2+ VSNs, the authors report an enrichment of ER-related genes in Gnao1+ VSNs. Using electron microscopy, they found that this enrichment was associated with specific ER morphology in Gnao1+ neurons. Finally, the authors characterized chemosensory receptor expression and co-expression (as well as H2-Mv proteins) in mature VSNs, which recapitulated known patterns.

Strengths:

The data presented here provide new and interesting perspectives on the distinguishing features between Gnao1+ and Gnai2+ VSNs. These features include newly identified markers, such as transcription factors, as well as an unsuspected ER-related peculiarity in Gnao1+ neurons, consisting in a hypertrophic ER and an enrichment in ER-related genes. In addition, the authors provide a comprehensive picture of specific co-expression patterns of V2R chemoreceptors and H2-Mv genes.

Importantly, the authors provide a browser (scVNOexplorer) for anyone to explore the data, including gene expression and co-expression, number and proportion of cells, with a variety of graphical tools (violin plots, feature plots, dot plots, ...).
