# Peer review - Round 1

Editors:
- Jeremy Nathans, Johns Hopkins University School of Medicine , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.26414.041](https://doi.org/10.7554/eLife.26414.041)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "SynEM: Automated synapse detection for connectomics" for consideration by eLife. Your article has been reviewed by two reviewers and the evaluation has been overseen by Jeremy Nathans as the Reviewing Editor and a Senior Editor..

As you will see, the reviewers were impressed with the importance and novelty of your work, but they also have a number of critiques/comments/suggestions that we think would improve the study and the manuscript.

I am including the unedited reviews at the end of this letter. The comments of reviewer #2 regarding generalizability (point 7) could represent a substantial amount of work. We suggest that you consider consolidating points 6 and 7 in reviewer #2's comments and compare the performance between SynEM, Dorkenwald et al., 2017, Roncal et al., 2014, and Becker et al., 2012 to at least one additional 3D EM dataset (as well as reporting Dorkenwald et al., 2017 and Roncal et al., 2014 performance on the first). The results would help to clarify SynEM's performance and applicability. You should consider reviewer #2's point 8 as optional.

In sum, we appreciate that the reviewers' comments cover a broad range of suggestions for improving the manuscript. Please use your best judgment in deciding which of these can be accommodated in a reasonable period of time.

Reviewer #1:

The manuscript by Staffler et al. describes a method for automatically detecting synapses in electron microscopy images collected using the block face scanning microscope. The authors report a high precision of 97%.

The appearance of this work is timely. An algorithm that is able to accurately detect synapses in electron micrographs with a lower z resolution than focussed ion beam images will be of interest to a number of groups. As the authors state, the method is scalable for larger sets of images, so should have a broad appeal.

This work is well presented and gives a thorough evaluation of the algorithms performance, as well as the comparison with other methods.

I have only a few relatively minor comments about the content of the paper. However, my major reservation concerns its suitability for this type of journal. The method is clearly tested on a very specific set of images, and its performance appears impressive, but beyond this there is little insight about the revealed connectivity. This is clearly a technically important piece of work, but I wonder if it should not be suited to a more specialist journal.

On a more specific note, I was confused about the testing of the performance on the different types of synapses. There is a description of how synapses along inhibitory axons were identified, and the success was high. However, does this mean that it is able to distinguish the contacts, but not classify between excitatory and inhibitory? How does the overall success for identifying synapses in the entire volume account for the two types of synapse? I presume from the description that it is simply identifying a contact, and no distinction is made. This needs to be clarified. It is perhaps a minor point, but nevertheless it is not explicitly given. It is also not clear as to whether the program is able to distinguish those contacts that are found on the dendritic shaft as opposed to those on the spine. Contextual information is being used from these different sites of contact, but are they given in the final result?

Reviewer #2:

Staffler and colleagues present SynEM, a tool for automated chemical synapse inference in volumetric electron microscopy data of cortical neuropil. The authors report SynEM: (1) provides 97% precision and recall of binary cortical connectivity without user interaction, (2) scales to large volumes, and (3) possibly to whole-brain datasets. SynEM is a natural extension of the group's analysis workflow for connectomics. Relying on volumetric neurite segmentation following manual skeletonization with SegEM (Berning et al., Neuron 2015), SynEM performs synapse inference by classifying interfaces between neurites based on spatial, texture, and shape features. The authors apply SynEM to their SBEM dataset from the mouse cortex and present the extracted connectivity as adjacencies for a local connectome in L4 of barrel cortex.

SynEM could be of potential useful to the field, however, there are several important concerns about its potential presented here:

1) Is SBEM + SegEM + SynEM comprehensively detecting structural connectivity? This is a fundamental advantage of EM. Estimating 1 synapse/μm3 (Merchan-Perez et al., 2014), in the authors' 86 x 86 x 52 μm3 volume (Figure 4A), one would expect 384592 synapses. In the reported local cortical connectome (subsection “Local cortical connectome”), SynEM detected 813 synapses over 531 connections. The number of detected synapses are 3 orders of magnitude less than expected. What might explain this? Either A. Only a subset of the data was used; B. The neuropil is not representative of estimates from the literature; C. The SynEM workflow is tuned to detect a subset of synapses, perhaps biased toward "large" synapses, also influencing precision-recall rates; or D. The dataset has insufficient information to detect many cortical synapses.

If (A), please clarify in the text/methods and let readers know if the synapse density is as expected, or why not. Given that the segmentation with SegEM was volumetric, a comprehensive connectome within the volume should be possible. If not, why did the authors choose only 104 axons and 100 postsynaptic processes?

If (B), please explain why neuropil in this dataset is not representative.

If (C) or (D), this is, of course, would significantly limit the utility of these approaches for the field as the results would not accurately represent the structural connectivity of neuronal networks.

2) Ground truth: synapse numbers were generated by viewing post-segmentation post-border detection volumes. How many synapses were lost during these preprocessing steps? A comparison against ground-truth synapse data generated using an independent method is necessary to judge the overall accuracy of the method in detecting synapses within a volume (see also point 1 above).

3) Are precision and recall rates elevated by large synapses? The distribution of synapse sizes reported in the Supplemental Synapse Gallery (subsection “SynEM workflow and training data”) appears heavily weighted toward larger interfaces (median > 0.1 μm2) compared to previous reports. PSD areas have reported median values of < 0.05 μm2 between hippocampal pyramidal cells (Harris and Stevens, J Neurosci 1989; Bartol et al., eLife 2015) and appear to be even smaller for both putative thalamic and non-thalamic synapses in L4 of mouse barrel cortex (Bopp et al., J Neurosci 2017). Thus, synapses < 0.1 μm2 are unlikely to be a small fraction of the actual population as asserted (Supplemental Synapse Gallery). Rather, it is worrisome that this approach may be missing synapses detectable with other methods (points 1-2), leaving and enriching for synapses easily detected by SynEM.

4) This reader found it difficult to interpret how ground-truth neuron-to-neuron connections were generated. It appears that neuron-to-neuron connectivity precision was calculated using several values taken from the literature (including pairwise connectivity rate and mean number of synapses per connection, subsection “SynEM for connectomes”). An additional assumption in their pairwise connectivity model is that connectivity is random and independent. There is increasing evidence that this assumption is not supported in the rodent cortex (e.g. Song et al., Plos Biol 2005; Lefort et al., Neuron 2009; Ko et al., Nature 2011; Perin et al., PNAS 2011). Is the cost of ground-truthing the reason these numbers were not measured from the dataset used to evaluate SynEM? This is an important value to get correct given the authors' claims.

5) SegEM errors influencing SynEM: SynEM requires a segmented volume (generated here by SegEM). A fuller description of how segmentation errors affect SynEM performance (more than just a few example images) would allow the reader to determine what segmentation results are suitable for application of SynEM (this may also inform point 1 above). Description of how errors in assignment of extracellular space affect SynEM performance would allow the authors support their claim that space-preserving EM preparations would simplify synapse detection.

6) Comparisons and references to relevant and available state-of-the-art tools: To provide evidence that SynEM provides a substantial methodological advance with the new potential to facilitate difficult or intractable experiments, the authors should provide fair comparisons of SynEM to multiple the state-of-the-art approaches. The authors do well to identify a set (Supplementary file 1), but appear to only apply and report their application of Becker et al., 2012 (perhaps to represent it and the family of approaches from the Hamprecht group?) to their data in the main Figures. Several others are missing:

Dorkenwald, S. et al. Automated synaptic connectivity inference for volume electron microscopy. Nat Methods (2017).

Perez, A.J. et al. A workflow for the automatic segmentation of organelles in electron microscopy image stacks. Front. Neuroanat. (2014).

Roncal, W.G. et al. VESICLE: volumetric evaluation of synaptic interfaces using computer vision at large scale. Preprint available at https://arxiv. org/abs/1403.3724 (2014).

Dorkenwald, 2017 was published just recently so its omission is perhaps unsurprising; however, Dorkenwald, 2017 and Roncal, 2014 are particularly important with a similar aims of large-scale synapse inference and may provide competitive or better performance compared to SynEM than the other approaches the authors list.

The authors should also show the precision-recall curves for the other methods (perhaps the 3 best performers from Supplementary file 1; Dorkenwald, 2017; Perez, 2014; and Roncal, 2014) tuned to their dataset. This would be an appropriate supplement to Figure 2.

7) Generalizability: A major impediment to the EM connectomics field has been that analysis workflows have been highly specific to particular dataset types. It would be of substantially more value if SynEM's utility is demonstrated across different 3D EM dataset types. The abstract states: "we report SynEM, a method for automated detection of synapses from conventionally en-bloc stained 3D electron microscopy image stacks"

As the authors are aware, there are multiple approaches to generate 3D EM datasets. To provide evidence for the utility across 3D EM image stacks, the authors should apply SynEM to other EM datasets. Ideally, datasets from 3D EM methods (Briggman and Bock, 2012) other than SBEM. This approach (1) would demonstrate generalizability; (2) could provide a better understanding of dataset parameters influencing SynEM and automated segmentation performance more broadly (it is the lower resolution of their dataset that benefits most from SynEM, on the other hand the authors may discover that SynEM is an overall outperformer?); and (3) benefits from the authors' knowledge on how to best tune the SynEM pipeline as compared to others' workflows (a potential problem with comparing others' approaches on one's own data). This should be straightforward. Several public datasets exist of ATUM-SEM (e.g. https://neurodata.io/data/kasthuri15), ssTEM (eg. https://neurodata.io/data/bock11), FIB-SEM (e.g. http://cvlab.epfl.ch/data/em), and other SBEM data. Alternatively, the authors could modify their description of scope, narrowing the utility of their approach to SBEM. In this case, one would, still want to see the workflow evaluated on at least one other independent dataset.

8) Directly test the claim of lower resolution performance: The authors propose that better segmentation tools are needed for higher-imaging throughput, lower-resolution datasets and that SynEM's performance is particularly useful for such data. In addition to testing performance on other dataset types (point 7), it should be straightforward for the authors to compare performance on their 6 nm data (Figure 1F). The authors should demonstrate the difference in performance on 6 compared to 12 nm data. If the authors are interested in imaging fast at lowest resolution possible to accurately extract connectomes, they should also decimate their 12 nm data to lower resolutions and examine where SynEM performance falls off in as a function of resolution.

9) Scalability: The authors strongly pitch that to analyze a 1 mm3 of cortex, approaches must be developed to accurately detect billions of synapses. In the abstract, the authors also assert that SynEM may plausibly scale to whole-brain datasets. It is unclear synEM the tool up to this task. As alluded to in (point 1) above, the synapse detection rates are surprisingly low. Moreover, there is little detail about how the approach scales to much larger volumes in terms of compute time and resources or other aspects of effort in the pipeline. Thus, it is difficult for this reviewer to estimate the cost and effort of implementing this workflow at such scales.

10) Terminology: binary vs. binary and undirected. To this reviewer, the use of 'binary' should be clarified and made consistent throughout the text. At the synapse level, the authors use binary to classify appositions as synapses or not, irrespective of direction.

Subsection “SynEM workflow and training data”. The SynEM score was then thresholded to obtain an automated binary classification of interfaces into synaptic / non-synaptic (θ in Figure 2A).

Subsection “SynEM workflow and training data” and Figure 2 legend Initially, we interpreted the annotator's labels in a binary fashion: irrespective of synapse direction, the label was interpreted as synaptic (and non-synaptic otherwise, Figure 2C, "Binary")

Whereas, at the connection level (all synapses making up the connectivity between a neuron pair) binary is used for whether or not there is at least γ synapses. These are, however, are directed connections.

Subsection “SynEM for connectomes”.We assume that the goal is a binary connectome containing the information whether pairs of neurons are connected or not.

Subsection “SynEM for connectomes”. “binary connectomes by considering all neuron pairs with at least γnn synapses as connected”

Convention in the field is for 'binary' to be used for unweighted connectivity, not to describe an undirected synapse. In descriptions of connectivity this reviewer would suggest using 'undirected-binary', 'directed-binary', 'undirected-weighted', or 'directed-weighted' not just 'binary' across the text.
