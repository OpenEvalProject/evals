# Peer review - Round 1

Editors:
- Inna Slutsky, Tel Aviv University Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55173.sa1](https://doi.org/10.7554/eLife.55173.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

In the present work, the authors examined cellular development and network formation in hippocampal CA1 area under in a mouse model of Lissencephaly, featuring severe cellular heterotopia, with a subpopulation of calbindin-expressing principal cells showing inverted laminar positioning. While the misplace cells retained much of their morphological and intrinsic properties, the authors detected very specific deficits between synapses of later born cholecystokinin-expressing interneurons and ectopic calbindin-expressing principal cells, leading to network hyperexcitability and cross-laminar desynchronization. This work demonstrates that layering may play an instructive role in synaptic specification and identified specific circuit motifs that are more susceptible to disruption.

Decision letter after peer review:

Thank you for sending your article entitled "Aberrant sorting of hippocampal complex pyramidal cells in Type I Lissencephaly alters topological innervation" for peer review at eLife. Your article is being evaluated by two peer reviewers, and the evaluation is being overseen by a Reviewing Editor and John Huguenard as the Senior Editor.

Summary:

The manuscript report a study on the effect of cellular heterotopia on the morphology, connectivity and electrical properties of pyramidal neurons in the pyramidal cell layer of the hippocampus. The authors take advantage of the Lis+/- model of lissencephaly to investigate how mislamination may affect neuronal properties. The Lis+/- mouse reports evidence for impaired migration of hippocampal calbindin expressing pyramidal neurons. The mislamination appears to depend on the time of birth of calbindin neurons during embryonic development. Mislamination does not appear to substantially alter the morphology of the neurons, has subtle effects on electrical properties, but appears to have more substantial effects on inhibitory innervation by CCK expressing inhibitory neurons. Additional differences in oscillatory activity induced by carbachol is reported. The authors conclude that mislamination is not a major driver of functional defects, but a specific circuit motif, the CCK-pyramidal motif, is primarily affected by the Lis+/- mutation.

While the authors find some interesting differences between control and Lis1 mutants, there are no experiments supporting the central claim that the PC neurons analyzed are indeed calbindin cells and unfortunately many of the results suffer from circular inference. The major issues that need to be addressed are detailed below.

Essential revisions:

1) From the Abstract all the way to the Discussion it is rather hard to identify a coherent view of what is the main question the authors are trying to address. It is unclear if their focus is on lamination (as stated initially), or morphological alterations, or circuit connectivity. All these points are addressed, but the rationale guiding the experimental design and description is for the most part understandable only by the intuition of the reader. A clearer and more explicit description of the goals and logic would make the manuscript appealing to a broader audience.

2) Figure 3: The authors start by explaining that "calbindin-expressing principal cells have more complex apical dendritic trees (more branching), than calbindin-negative counterparts". The claim is based on past literature but the authors never experimentally test this claim. In fact, the authors perform supervised clustering (assuming K-means n = 2, due to literature "complex" vs. "simple" trees) and then assume for the remaining manuscript that the "cluster complex" corresponds to "calbindin-cells". This poses several major issues. First, the literature never demonstrated the existence of 2 clusters in Lis1 mice, thus it is not known whether PC with "complex apical trees" correspond to calbindin-cells in these mice, or if there are even 2 clusters, or 3, or 1 cluster in Lis1 mice. Second, the authors cluster cells based on "complexity" and then parameters such as "apical bifurcation" and "sholl complexity" (two parameters inherent to the clustering algorithm) are used to compare cells between the "simple" vs. "complex" cluster, an example of circular inference. Third, the authors show in Figure 1 that calbindin cells represent about 25% of cells in WT and 4% in Lis1, and then according to the algorithm, 54% of cells in WT and 38% in Lis1 are complex, further suggesting that the clustering assumption of "complex cluster of cells" equals "calbindin cluster of cells" is likely incorrect.

3) Figure 4: N numbers are again different across the different panels but are supposed to represent ephys parameters extracted from the same recorded patch cell. In Figure 4C, the algorithm mis-categorized 2 in 8 cells (25%) and 3 in 11 cells (27%), showing unacceptable performance for a clustering algorithm. Another concern is the fact that 8 different parameters were used for physiological clustering analysis (resting membrane potential, sag index, input resistance, spike amplitude, adaptation ratio, firing frequency at 2x threshold, spike threshold, and after hyperpolarization amplitude) but no cross-validation was performed. Risk of possible data overfitting is a major concern.

4a) Figure 6: The major concern is related to the validity of the data. Materials and methods indicate that "Series resistance was monitored throughout experiments using a -5mV pulse at the start of each sweep and ranged from 12-32MOhms". Apart from "12-32MOhms" being a too wide range, what was the average value of series resistance per group? What was the % change of series resistance throughout recordings, namely before and after drug applications? Without that information it is not possible to interpret changes in signal amplitude. Lastly, it is not possible to extract conclusions from n=5 vs. n=13 cells, or from n=3 vs. n=7 cells. How many mice were used for this particular experiment?

4b) The sample traces shown in Figure 6 do not reflect the population data. For experiments in Figure 6, the correct reference is Heft and Jonas, 2005, and not Wilson et al., 2001 (which does not address the cell type specificity of the effects of conotoxin and agatoxin on release, but only heterogeneity of the effect by CB1 expressing or lacking pyramidal neurons).

5) Some of the results appear to be primarily driven by one data point or two. The use of estimation statistics would be helpful in determining which parameters are actually changed in the population data (e.g. Figure 5H, Figure 6D and I or in Figure 7E, or Figure 8D and E).

6) It appears that the size of the hippocampus differs between control and mutant mice (Figure 1A). Nevertheless, without scale bars and clarification of the anteroposterior position at which the slices were cut, it is hard to guess whether the photos were taken from comparable portions of the hippocampus.
