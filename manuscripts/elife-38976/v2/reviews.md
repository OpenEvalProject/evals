# Peer review - Round 1

Editors:
- Jeremy Nathans, Johns Hopkins University School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.38976.034](https://doi.org/10.7554/eLife.38976.034)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "FluoEM, Virtual labeling of axons in 3-dimensional electron microscopy data for long-range connectomics" for consideration by eLife. Your article has been reviewed by Eve Marder as the Senior Editor, a Reviewing Editor, and three reviewers. The following individual involved in review of your submission has agreed to reveal his identity: Harald F Hess (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

All of the reviewers were impressed with the importance and novelty of your work, and the high quality of the data. The full three reviews are included at the end of this letter, as there are a variety of specific and useful suggestions in them.

Reviewer #1:

This paper by Drawitsch et al., describes how fluorescently labeled axons imaged with light microscopy can be identified in EM image stacks using a process of computational matching of their trajectories. The paper is well presented, and the figures are appropriate.

This is an interesting paper and represents a small but significant step forward in the connectomics field. Identifying neurites belonging to different cells types in serial EM images has been achieved using a number of different methods over many years beginning with the work of Ed White in the 1970s. However, as the techniques for ultrastructural imaging have developed and vast volumes of brain tissue can now be visualized, tools for labeling different cell types in the EM are still very limited. Combining EM with LM is the obvious way forward but finding neurites in EM image stacks that were previously seen with LM is not straightforward. To date, this has been achieved with careful targeting of small regions using fiducial marks, and as the authors state, this is not relevant for connectomics' analysis. The current paper provides a detailed description of axon trajectories, giving some measurement of their uniqueness of length to allow a sorting process and selection of possible candidates. The final conclusion is that axon lengths of only less than 40 microns are needed for the method to work.

The authors provide all the datasets, which are exceptional, and it’s clear that very few laboratories could achieve imaging on such a scale. I am more enthusiastic about the results rather than the tools themselves as few groups have the resources for this approach.

I only have one question about the method. I fully appreciate that the authors describe a systematic computational approach for matching axons but while reading the paper and understanding how long this takes I wonder how quickly axons can be found by a human observer using the same datasets. Or is this even possible? In the methods part, the authors explain how they use the blood vessels to locate the region in the tissue from which the EM image stack was taken. Therefore, the region in which the axon can be found has been narrowed down considerably. If single axons are evident in the LM dataset, can these be found in the EM once it's clear where in the volume they should be located? As the authors describe how boutons are used to confirm the identity of the axons, could human observers achieve the same task more rapidly without having to make such large reconstructions of many axons?

Reviewer #2:

In this manuscript Drawitsch et al., present a workflow – FluoEM – for faithfully identifying correlated axon segments in sequentially imaged light microscopic and EM datasets. The approach is a significant advance in 3D connectomics as it allows labeled long-range axonal inputs to be mapped onto dense EM neuropil reconstructions. This approach has advantages over other correlative LM-EM approaches as it does not require any chemical label conversion and can potentially be used to study long-range axonal targets of genetically identifiable neurons from selected brain areas at nanometer resolutions afforded by EM. The results presented, especially the matching of varicosities to synapses is very satisfying and convincing. The experimental, computational methods described are sound and well documented. Together the approaches and tools described in this manuscript are likely to be impactful for the connectomics field and this paper merits publication in eLife.

1) In subsection “Comparison of axon and synapse detection in LM and EM” the authors compare axon and synapse detection in both LM and EM. While it is indisputable that the unambiguous assignment of synapses would require EM data the nearly 30% error rate in the assignment of axonal trajectories and branches in the LM data reported in this study appears unusually high. Is this likely due to high density of viral labeling. It would be useful to understand in more detail the effects of labeling sparsity in LM accuracy. Was the sparsity consistent across the 3 samples studied? Are the sparser regions of the neuropil associated with more accurate tracings?

2) The presentation of timing in various parts of the manuscript (Results section, Discussion section and the extrapolation in the Materials and methods section) is a bit confusing and could be better. For instance, what is the relative work load of completion needed for matching versus the time for reconstructing complete axons in the EM volume? It is also not clear if there are other bottleneck steps in scaling to larger volumes and if a linear extrapolation of axon segment matching times is relevant.

3) The current approach of correlative LM-EM is designed for looking at EM level connectivity of relatively dense axonal projections from different labeled 'source' brain areas. A complementary use case would be to look at input-output relationships of entire axonal arbors of single labeled neurons – the scales of such arbors could be much larger than the EM volume imaged in this study. Could the authors speculate on the feasibility of an approach wherein the acquisition of a high resolution EM dataset would be guided by the LM imaging of a very sparse labeled sample?

Reviewer #3:

The manuscript addresses a very important factor in extending the relevance of connectomics for mammalian brains, namely how to assign the source or destination of long-range projections associated with a target neuropil. Presently, the imaging and reconstruction of neural tissue volumes approaching 1 mm3 are becoming possible, yet a complete mammalian brain is out of range by 2-3 orders of magnitude. So, the identification of long-range input and output connections of a 1 mm3 region is clearly a major component to understanding the circuitry a reconstructed local region.

The research and manuscript are high quality and comprehensive. As just mentioned the motivation is well justified, the methodology for CLEM is well documented, as well as exemplary data sets and analysis software. The criteria for establishing positive or most likely neuron identification is described thoroughly in both a general level and in the fine detail of source code. The major concerns of error, e.g. error rates from light microscopy reconstruction are presented explicitly and shown how they can still be corrected to give very convincing correlative identification. Several different identification strategies e.g. path length, varicosities, etc. are compared as multiple cross confirming and extending options. Demonstrations in several locations in different layers of the cortex also prove the general applicability of this methodology.

One important parameter seems to be the axon labeling density. It seems that this must be controlled to get both as many as possible axons and yet sparse enough that they are separable in LM with the exemplary value of ~71% faithful reconstruction number. It would be helpful to have a rough number here and discussion of how that might be controlled or how that limits or expands the fraction of I/O projections into the EM volume.

There is without doubt a highly relevant, timely, and useful contribution to the field.
