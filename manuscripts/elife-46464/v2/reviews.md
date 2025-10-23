# Peer review - Round 1

Editors:
- Julie A Kauer, Stanford University United States

Reviewers:
- Tibor Harkany, Karolinska Institute Sweden
- Idoia Quintana-Urzainqui, University of Edinburgh United Kingdom

## Review text

DOI: [10.7554/eLife.46464.031](https://doi.org/10.7554/eLife.46464.031)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Molecular and anatomical organization of the dorsal raphe nucleus" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Eve Marder as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Tibor Harkany (Reviewer #1); Idoia Quintana-Urzainqui (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This is a comprehensive, well executed and interesting study addressing a timely and important question. The raphe nuclei are implicated in many neuropsychiatric and neurological disorders and they hold one third of all serotonergic neurons of the brain. However, the structure and function of the region has been difficult to study given its extraordinary heterogeneity in neurochemical composition and anatomical organization. We are in need, therefore, of single cell datasets and studies like this one. In their manuscript "Molecular and anatomical organization of the dorsal raphe nucleus", Huang and colleagues shed light on the complex anatomy and organization of the dorsal raphe nucleus (DRN) in the adult mouse. By performing single cell RNA-seq in dissected DRN region they produced an interesting dataset which encompasses neural and non-neural cell types present in and around DRN. Based on this transcriptomic data they identify 5 subtypes of 5-HT neurons and comprehensively study their anatomical and molecular characteristics. By analyzing the distribution of genes identified as differentially expressed on each of the putative subtypes they develop a map of their anatomical localization within the DRN. Then, they perform a series of experiments to explore whether 5-HT raphe neurons projecting to known targets (basal ganglia, cortex or thalamus) correspond to any of the subtypes identified. They show that the DR is composed of at least 5 distinct 5-HT neuronal types. In addition, the authors demonstrate that at least 2 distinct 5-HT neuronal types project to the striatum. Finally, they validate that a Pdyn-expressing 5-HT neurons (likely belonging to subtype III) strongly and specifically innervate various basal ganglia structures.

Essential revisions:

The reviewers have very positive comments about the study, but especially because this paper will be relied upon as a critical reference in the field, more validation is required for the existence of the 5 subtypes, particularly given the relatively low percentage of genes identified per cell with the single-cell RNA-seq. To achieve this, two approaches are indicated.

1) Additional FISH will be required to prove that the 5 claimed subtypes are correct and separate (in particular, the two very similar cell types 5-HT-I and II). Adding a reasonable quantitative would be adequate (e.g. 5-HT-IV x% out of all serotonergic neurons in a particular DRN subregion), and would be a good fit to Figure 4B. Preferably the authors will use at least one or two more specific markers for each cell subtype, showing similar anatomical distribution throughout the DRN and/or co-localization if possible.

2) Sten Linnarsson has recently published a scRNA-seq paper in Cell (Zeisel et al., 2018) in which they find TPH2+ neurons. Those data were produced with deeper sequencing. It would elevate the importance of the findings in this manuscript considerably if the authors could use a bioinformatic comparison of their own cells with this publicly available database. First, they should mix together their own cells and those from the Linnarsson database and see if iterative machine learning splits them into the two original clusters; if so, this may then require further sequencing. If not, they then might go deeper with a larger number of cells to justify the existence of the 5 subgroups. The above pipeline could also be informative in retaining the "peptidergic" cluster. There is concern that the authors may be losing low-level expressed neurotransmitter synthesis genes.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for submitting your article "Molecular and anatomical organization of the dorsal raphe nucleus" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Eve Marder as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Idoia Quintana-Urzainqui (Reviewer #3); Martin Häring (Reviewer #4).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This is a comprehensive, well executed and interesting study addressing a timely and important question. By performing single cell RNA-seq in dissected DRN region they produced an interesting dataset which encompasses neural and non-neural cell types present in and around DRN. Based on this transcriptomic data they identify 5 subtypes of 5-HT neurons and comprehensively study their anatomical and molecular characteristics. By analyzing the distribution of genes identified as differentially expressed on each of the putative subtypes they develop a map of their anatomical localization within the DRN. Then, they perform a series of experiments to explore whether 5-HT raphe neurons projecting to known targets (basal ganglia, cortex or thalamus) correspond to any of the subtypes identified. The work is expected to be widely used as a reference for this important brain region.

The reviewers are generally enthusiastic about this paper, and the substantial revisions to the original manuscript. They do, however, have some remaining concerns that we feel can be easily addressed.

We suggest a change in the Figure 4—figure supplement 2. The Z-Score has the disadvantage that it only shows relative expression levels (colour code). In respect to expression differences this can be misleading. Thus, if you compare several different cell types (Figure 3B) the expression (here Tph2 and Slc22a3) are quite uniform among the serotonergic neurons. If, however, the observed number of clusters is smaller (focus on serotonergic cells; Figure 4A), than the small expression differences suddenly appear huge for these two genes. Moreover, the authors state in the figure legend for Figure 4—figure supplement 2 that "…Prkcq+;Trh- 5-HT neurons are putative 5-HT-II neurons.". This might be correct but has to be shown in another mean beside Z-score as both genes are shown to be expressed also in Cluster 2 (slightly lower compared to Cluster 1) in Figure 3B and even in 4A.

The reviewers agree that the paper would be stronger if the authors would add staining for Nfix or Slc6a1 (Cluster 1; Figure 4) and Mkl2 (Cluster 2 enriched), although we will leave this up to the authors. If no new stainings are added, however, the presentation of Z-scores should be changed to dotblot (or maybe barblot) format, as seen in other publications (e.g. Kupari et al., 2019, Cell Rep.). Dotblots allow the visualization of the percentage of cells expressing the gene in the separate clusters in addition to relative expression levels (colour code), while the bar blot approach shows the expression level of a gene for each single cell directly.

This presentation will allow the reader to determine whether expression differences are due to generally lower levels in the two clusters or to higher percentage of cells lacking the gene in Cluster 2. The Z-score does not allow this, and the TPH2 and Slc22a3 results are examples of how the Z-Score can be misleading (Figure 3B and 4A).
