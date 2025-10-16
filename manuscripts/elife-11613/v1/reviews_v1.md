# Peer review - Round 1

Editors:
- Constance Cepko, Harvard University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.11613.055](https://doi.org/10.7554/eLife.11613.055)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: this article was originally rejected after discussions between the reviewers, but the authors were invited to resubmit as a Tools and Resources article after an appeal against the decision.]

Thank you for submitting your work entitled "Epigenomic landscapes of retinal rods and cones" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

The work provides an excellent dataset for those in the field, and beyond, as well as provides an example for others who wish to carry out a comprehensive and rigorous assessment of the chromatin of a specific cell type. The data also provide a more in depth view of photoreceptor biology, including the interesting findings concerning the differences between rods and cones, with implications regarding the evolution and function of photoreceptors.

However, I am sorry to say that the paper was not judged as reaching a novel enough conclusion for eLife. The findings regarding rods and cones were not judged significant enough by two of the reviewers. Due to the negative opinion on this point, I did consult another person who is knowledgeable in the field of retinal biology, to see if I could find additional support. Though this individual was not able to perform a full review, he did look it over for the overall conclusions, and again, the opinion was essentially the same. However, the work is beautiful and for a fan of photoreceptors, very interesting.

Reviewer #1: This manuscript details the epigenetic landscape and correlative features of separated retinal rod and cone cells, as distinguished from studies of the whole retina. This appears to be the first study of this kind. The authors perform comprehensive epigenomic profiling separately integrating ATAC-seq, DNA methylation, RNA-seq and histone modifications. A main result is the unusual pattern specific for rods of unmethylated reigons in closed chromatin and without enhancer activity, but with enhancer activity at a prior stage (fetal). This idea is not entirely novel as it has previously been called vestigial enhancers. The computational analyses are standard except for the use of a new Motif tool (MotifSpec) which is to be described elsewhere (though the advantage of the tool relative to what is available is unknown).

The paper is well written and the findings appear solid with conventional computational correlations. The major issue for this reviewer is the cursory attention to function. Figure 4 provides the only functional data which shows that ATAC-seq regions often provide enhancer activity. The extent of enhancer analysis is not up to what can be done to go beyond mere description. In weighing strengths and weaknesses for eLife publication here one has to balance the overall quality of the descriptive data with the relative lack of really new insights into epigenetics and function. Frankly I am on the fence as to whether this manuscript meets criteria for eLife or its more suitable for a genomics journal. The datasets will be useful to workers in the field but probably not more widely.

[Minor comments not shown.]

Reviewer #2:

This research article by Mo et al. continues exploration of cell type-specific epigenomic landscapes, building on their own recently published work in Neuron (NeuroResource: Epigenomic Signatures of Neuronal Diversity in the Mammalian Brain; http://dx.doi.org/10.1016/j.neuron.2015.05.018).

As shown in that earlier publication, combined analysis of DNA methylation and chromatin accessibility is an effective way to characterize cell type-specific regulatory elements. The authors apply this strategy by combining MethylC-Seq and ATAC-Seq analysis to nuclei isolated by FACS sorting or affinity purification (INTACT, a technique they adapted to mammalian cells in their Neuron paper). Unlike that earlier work, this new paper does not introduce a novel, widely applicable technical approach such as INTACT.

The biological observation that the report centers on is that chromatin in rods has hypomethylated regions that correspond to regulatory loci playing important roles in the fetal neuronal development. The authors argue convincingly that these regions are likely shielded from methylation due to the (well-characterized) unusually compact chromatin structure in rod cells. The authors also use comparisons between wildtype and Nr2e3 KO (rd7) rods and between rd7 and Nrl KO (with massive shift to cones) retinas to argue that rd7 rods acquire intermediate epigenetic landscapes between rods and cones.

This is a generally solid descriptive paper which does not happen to yield a new biological insight. It thus appears to fall short of eLife's stated goal of publishing highly significant work. If the editors feel this work belongs in eLife, perhaps it might be a better fit to the Tools and resources section. (Cf. a recent publication in that section: "Cell type-specific transcriptomics of hypothalamic energy-sensing neuron responses to weight-loss"; http://elifesciences.org/content/4/e09800).

Specific comments:

H3K27me3 ChIP-Seq: one of the replicates has very low coverage (3.5M deduplicated aligned reads vs. 16.5M in the other experiment; Supplementary file 1). This is likely indicative of a technical failure. At the very least, combining data from these two replicates should be explained; better, the replicate should be redone or removed.

Electroporation analysis of regulatory regions is not particularly convincing. Shouldn't rod- or cone-specific expression lead to a large number of cells with signal (as in Nr2e3), regardless of signal strength? So it is unclear why native GFP was preferred to AP. The scoring is also confusing. Based on Figure 4, it is unclear why signal from Pde6h(-4.6kb) fragment is called "moderate" while Pde6h(-0.8kb) is called "weak" (in Supplementary file 6). Even if we fully accept the authors' interpretation, there is no particular reason to think that the regions tested by electroporation are representative of all regions used for motif analysis. It might make more sense to first perform the motif finding, and then use the regions with most characteristic motifs to test experimentally.

Authors note that the INTACT analysis was less cell specific in the retina, because after isolation, nuclei typically formed aggregates (possibly with nuclei from cells of different types), rather than stay as singlets. Since cell specificity of the analysis is a major point, it would be important to understand how much of a distortion is introduced by this aggregation. What is the distribution of nuclei per the singlet, doublet, etc. bins? How often doublets and higher order aggregates contain both rod and cone nuclei (perhaps even rough analysis based on the nuclear appearance might suffice)?

[Minor comments not shown.]

Reviewer #3: This is a very novel study which, for the first time, presents a comprehensive analysis of both global as well as specific/local epigenomic states in rods and cones. Although the work is a bit less mechanistic than would be desired, the vast array of data and comprehensive, broad spanning nature of the work makes this a strong manuscript, suitable for publication in eLife. The focus on NR2E3 loss is quite interesting and impactful; it would have been great if they could identify additional combinations of genes which (when lost/modified) promote the cone-like state to a greater extent/achieve more complete conversion. While this (the rod/cone biology component) is slightly removed from my field of expertise, based on the work presented and the conclusions derived, I think this paper should be accepted, pending minor revisions.

This is without question the most comprehensive analysis of the epigenomic features of rods and cones, and the first to generate such data in cones, which are far less abundant than rods in the retina. The authors have the difficult task of bringing forward the key, focused points (i.e. the studies on NR2E3) while showing massive amounts of data that were needed to inform more specific mechanisms.

Are there additional mechanistic insights that have been gained since submission of the manuscript with respect to the loss of NR2E3? Or cooperating genes which would further promote a cone-like state?

Technical comments:

Figure 1.

A) Could the authors extend this to show not only a gene expressed by both but other genes expressed in either rods or cones? The general accessibility patterns would be valuable to see as comparison here.

B) Are there ways to indicate the statistical significance on the figure for B and C? The curves appear very close, and hence, some measurement of significance here would be helpful, if possible. Perhaps a bar graph for site distance next to these graphs?

C) In Figure 1D, is there anything you can generalize about these specific sites in this figure to substantiate the finding? Or show tracks next to the bar graph to indicate what this looks like on key genes?

Figure 2.

Could the authors simplify Figure 2A? Reduce the # tracks? The key point is a bit lost in the number of tracks shown here. Best to separate between this figure and Figure 2—figure supplement 1.

Figure 4.

To complement this, are there quantitative summaries that could be displayed in the figure, i.e.% GFP expression for the key comparisons? Also, to save space/redundancy, perhaps the authors could show just 2 of the 'near cone genes' and place the rest of these in supplemental? I think the point is well illustrated and quite clear.

If possible, as part of Figure 7, a model/summary figure would improve the paper and allow more citations via highlighting the model. I think this would be an important addition.
