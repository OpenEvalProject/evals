# Peer review - Round 1

Editors:
- Inna Slutsky, Tel Aviv University Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62373.sa1](https://doi.org/10.7554/eLife.62373.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper examines the properties of GABAergic interneurons in a mouse model of type I lissencephaly, a neurodevelopmental disorder. Utilizing electrophysiology, immunocytochemistry and RNA sequencing, the authors found that the lissencephaly mutation reduces the abundance of fast-spiking PV+ interneurons, while increasing the proportion of neurons with intermediate spiking phenotype. The mutation changes morphological development, intrinsic excitability, and inhibitory output of PV+ interneurons. Single-cell RNA sequencing reveals several dysregulated genes related to morphogenesis, cell excitability and synapse formation. These results suggest that impaired development and function of PV+ interneurons contributes to the spontaneous seizures observed in type I lissencephaly.

Decision letter after peer review:

Thank you for submitting your article "Emergence of Non-Canonical Parvalbumin-Containing Interneurons in Hippocampus of a Murine Model of Type I Lissencephaly" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and John Huguenard as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Gordon Fishell.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

The paper by Ekins et al. examines the properties of GABAergic interneurons in a mouse model of type I lissencephaly, a neurodevelopmental disorder. To address this question, the authors use electrophysiology, immunocytochemistry, and molecular techniques including RNA seq. The main findings are:

– The lissencephaly mutation reduces the abundance of fast-spiking PV+ interneurons, and increases the proportion of neurons with intermediate spiking phenotype.

– Global and cell-specific mutations in GABAergic interneurons have comparable effects, suggesting cell-autonomous mechanisms.

– The mutation changes morphological development, intrinsic excitability, and inhibitory output of PV+ interneurons.

– Single-cell RNA sequencing reveals several dysregulated genes, related to morphogenesis, cell excitability, and synapse formation.

Based on these results, the authors conclude that impaired development and function of PV+ interneurons contributes to the spontaneous seizures observed in type I lissencephaly. Overall, the reviewers found this a quite nice paper. The key findings are exciting, the experiments are systematically planned and well performed, and the manuscript is carefully written. However, the reviewers have a couple of points that need to be addressed before the manuscript can be published.

Major points:

1) The authors demonstrate that the macroscopic morphological properties of axons and dendrites of PV+ neurons differ between wild type and mutant. However, the microscopic morphological properties are largely ignored. Parameters of interest include dendritic and axonal diameters, number of presynaptic terminals, and "aspinyness" versus "spinyness" of interneuron dendrites.

2) A different clustering analysis must be applied to validate the main conclusions.

The Materials and methods section, regarding clustering analysis, states that: "To identify potential subclusters of PV+INTs, we performed principal components analysis (PCA) and hierarchical clustering based on Euclidean distance of normalized (log transformed) intrinsic electrophysiological parameters using R-studio version 0.99.451 and R version 3.4.2." So the question is, how many clusters exist in the sample? What value should be considered for k? Figure legends seem to provide the answer: "The dendrogram inset indicates 2 optimal clusters" and "The dendrogram inset indicates 3 optimal clusters".

Unfortunately, dendrograms cannot (usually) tell you how many clusters you should have, unless the ultrametric tree inequality holds, which is very rare for any real-world data. In other words, it is a common mistake (and misinterpretation) to use dendrograms as a tool for determining the number of clusters in a dataset. As a result of that premise, one of the central arguments is that "WT PV+INTs consist of two physiological subtypes: FS and NFS cells" whereas "GlobalLis PV+INTs consist of three physiological subtypes: FS, IS and NFS cells". But let us look at the data. Figure 3E and Figure 4E show cell intrinsic properties for these groups. Shouldn't the FS group be similar among these Figures? In fact, the FS groups seems indeed similar if we combine the FS+IS groups in Figure 4. This is because k=2 was assumed in Figure 3 and k=3 was assume in Figure 4, so the FS group suffered further splitting into a new IS subgroup.

3) The authors claim that connectivity of PV+ interneurons and pyramidal neurons differs between wild-type and mutant. To understand the network relevance, it would be nice to know whether this not only holds for inhibitory output, but also for excitatory synaptic input of PV+ interneurons. Mutual connectivity between interneurons might be also important. At the very least, these points need to be better discussed.

4) The conclusions stand and fall with the assumption that recording conditions are the same for wild-type and mutant mice. Controls should be provided to reassure that this is the case, and differences are not dependent on systematic differences in age of the animals, slice quality, etc.

5) The statistics of the paper requires improvement. A Fisher exact test should be used to test the statistical significance of the different proportions between wild-type and mutant mice. "nonparametric t-test" replaced by more specific information, such as Wilcoxon signed rank test or Mann-Whitney U test. Finally, the authors should revise the estimation of the number of classes in the cluster analysis. Based on the shape of the frequency distribution, the authors suggest that two classes in wild-type and three classes in mutant describe the experimental observations. However, the differences in the distributions are quite small, and the significance is unclear.

6) The authors demonstrate several structural and functional differences between PV+ interneurons in wild-type and mutant brains, but what this means for the activity of interneurons in vivo remains unclear. Ideally, the authors should record from PV+ interneurons in wild-type and mutant mice under in vivo conditions (some tetrode recordings might be affordable). At the very least, the results should be better discussed in the context of in vivo activity.

7) The mechanisms underlying the differences in excitability and synaptic output between fast and intermediate spikers remains unclear. Changes in in excitability are likely to be related to changes in Na+ or K+ channel density or subtype. Similarly, changes in inhibitory output will be due to changes in q, N, or pR. Both are only tangentially related to the RNAseq data reported in the paper. More work seems needed to work out the mechanisms.

8) A bit more emphasis on whether there were any indications in the non-autonomous Emx1-cre mutant would have a made a nice complement (might have missed this if it was there).

9) Another concern is with confusing IS cells with the SST populations, as they are both more or less IS and they apparently had no specific marker to identify the PV cells other than the physiology that was sufficiently perturbed to confound proper identification of this population. That they were discernible seemed evident from the scRNA-seq analysis but some attention to the SST interneurons (which clearly would be affected in the nkx2.1-cre KO) would have been a nice addition. Are they still facilitating, is their morphology normal, Are they properly dendritically targeting. Both distinguishing these for the IS population and describing this population at least a bit more thoroughly would have been very nice additions to what is clearly a wonderful paper.

10) The presentation of the manuscript requires improvement. The amount of description of wild type PV interneurons is surprising, as it has already been thoroughly described, in particular in Pelkey et al., 2017. This is necessary for the comparison of wt and mutant cells but perhaps could be parred down rather than spending the first third of the paper describing things are already well documented in the literature. In the present form, the Discussion is rudimentary and focused on side-issues. Several other aspects need to be included (see other major points).
