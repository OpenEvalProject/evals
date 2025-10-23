# Peer review - Round 1

Editors:
- Karel Svoboda, Janelia Research Campus, Howard Hughes Medical Institute , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.24364.019](https://doi.org/10.7554/eLife.24364.019)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "EM connectomics reveals axonal target variation in a sequence generating network" for consideration by eLife. Your article has been favorably evaluated by a Senior Editor and three reviewers, one of whom, Karel Svoboda (Reviewer #1), is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

This is an interesting paper on the detailed connectivity in HVC, a nucleus in the zebrafish brain that is critical for production of stereotyped song. A subclass of HVC neurons (those that project to RA) produce precise sequences (sequential neural activity patterns) of activity. However, the circuit and network properties underlying sequential activity patterns are not understood. Computational models have focused on local excitation to produce this activity. However, excitatory connections between RA-projecting HVC neurons have been difficult to find in brain slice recordings, arguing against the models. Kornfeld et al. show that proximal axons of RA-projecting HVC neurons synapse onto inhibitory interneurons; in contrast, more distal axonal segments synapse onto excitatory neurons, consistent with chain models.

This is the first serial EM reconstruction study of songbird brain, and therefore this manuscript could be an important resource for songbird researchers. The paper contains a wealth of anatomical data that will be useful for unraveling the circuit mechanisms underlying sequence generation in this circuit.

Please revise the paper in response to the points below. Three major points need addressing:

1) Data resource.

2) Conceptual issues. Mainly, the reviewers feel that this report has little to say about chain models and alternatives.

3) Technical issues. Mainly, the classification of symmetric and asymmetric synapses is not well supported.

Data resource issues:

The underlying EM data should be shared upon publication. This would be consistent with recent trends in sharing of volume EM data accompanying publication of biological results (Kasthuri et al., 2015; Bock et al., 2011; Takemura et al., 2013; https://www.janelia.org/project-team/flyem/data-and-software-release; and many others at http://www.openconnectomeproject.org/). Traced skeletons should also be provided.

Approach: the authors confirmed the morphology of HVC(RA) cells by using single-cell labeling and light microscopy (LM). Most (95%) of the dendrites of HVC(RA) cells are sufficiently compact to be covered by the image size of the serial block-face electron microscopy (SBEM) (166 x 166 x 77 μm3).

From a postsynaptic perspective, SBEM revealed that the synapses onto an HVC(RA) cell are dominated by inhibitory (symmetric) synapses rather than excitatory (asymmetric) synapses (60%: 40%, main text, sixth paragraph). This fraction is surprising because it is different from results described in the mammalian literature (but see point 1 below). After taking into account the ratio of BDA-labelled (retrogradely labelled) HVC(RA) cells relative to the total number of HVC(RA) cells, HVC(RA) – HVC(RA) connections are estimated to be ~15% of all the excitatory inputs (main text, eighth paragraph) to a single HVC(RA) cell.

From a presynaptic perspective, the authors also found that the probability of making a connection to another HVC(RA) neuron depends on the distance between the presynaptic axon and its cell body of origin. At a short distance (<100μm) from the cell body, most (95%) of the synapses that an HVC(RA) axon makes are on inhibitory neurons, whereas few (3%) are made on other HVC(RA) cells. At greater distances from the soma, the axon tends to make more synapses on other HVC(RA) cells (36.7% of its presynaptic axon terminals, main text, eleventh paragraph). On average, the authors estimated that about a quarter (24%) of all incoming excitatory synapses are homotypic (HVC(RA) -HVC(RA) synapses. The discrepancy between this number and the estimate from post-synaptic side could be due to the difficulty of defining the presynaptic terminal compared to postsynaptic structure.

Although it was already known that HVC(RA) cells make connection to other HVC(RA) cells, the distance dependent connectivity is a novel finding. This is of interest to those who are interested in the network architecture of HVC.

The core analysis for the distance dependent connectivity is that orphaned axons are further from their parent somata and make a higher proportion of excitatory synapses. This is a one bit analysis, which is ok. Beyond that, the attempts at quantitative analysis using Baysian approaches is not convincing.

Major conceptual issue 1:

Although the HVC(RA) – HVC(RA) interaction is the major focus of this paper, the results here show that only a quarter of excitatory inputs onto an HVC(RA) cell are from other HVC(RA) cells. The majority of excitatory inputs to HVC(RA) cells remain to be described. Can the authors provide more information about the remaining ~75% of excitatory inputs? For example, major afferents of HVC are NIf and Uva. In addition to HVC(X) cell type, it is reasonable to assume they (NIf, Uva, HVC(X)) would comprise the remaining excitatory inputs to HVC(RA) cell. Since some of these other inputs are likely to be important for singing (especially those from Uva), it seems important to know their identity. As it stands, this paper failed to provide the majority of input to HVC(RA).

Major conceptual issue 2:

These results do not serve to support a chain model. The authors acknowledge this limitation (main text, fifteenth paragraph), but it seems that much of the significance of this study rests on knowing whether the interconnected HVC(RA) neurons are actually parts of functional chains that display sequential activity, as introduced in this manuscript. Testing this idea would require a combination of functional imaging and SBEM methods. This is a high bar. But as it stands, the interconnected neurons could be a cluster of somewhat distributed cells that fire together.

Out another way. The network structure presented here may be consistent with, but not indicative of, a role in sequence generation. This network structure is also consistent with winner-take-all dynamics and with synchrony detection. Is there an argument the authors can make that this network structure is specifically supportive of a role in sequence generation?

Re: "Both observations support the notion that the neural sequences that pace the song are generated by global synaptic chains embedded within local inhibitory networks."

"Are consistent with the notion" would be more accurate. (see also main text, sixteenth paragraph).

Major technical issues

1) Identification of symmetric vs. asymmetric synapses is questionable. The data and methods presented are insufficient. Figure 1F is too small; Figure 1—figure supplement 1 shows only one reasonably clear asymmetric contact (panel D). Since there is no post-staining with this imaging method, post-synaptic densities are unamplified by a mordant. Misclassification biased toward symmetric contacts is therefore possible. Since this is a potential bias in the underlying data, it would not be detected by the verification method, i.e. to have a second expert independently classify synapses to obtain consistent results. Misclassification would be consistent with the surprising finding that these dendrites have unusually high fraction of inhibitory input (~60%). Although it is likely the authors have developed expertise to classify these synapses, despite the above issues, the data presented in the paper are not sufficient to convince the reader. At a minimum, more raw data and examples of classification will need to be shown. If this does not suffice, an independent verification of classification correctness should be devised. For example, axons could be traced from identified excitatory and inhibitory somata in the volume, and the synapses these axons make could be randomly presented for classification to a blinded party. If classification in this data set is correct and unbiased, all synapses arising from excitatory axons should be classified as asymmetric, and all axons arising from inhibitory neurons should be symmetric etc.

2) Re: "Although ~70% (174 out of 248) of dendritic branches reached the boundary of the EM data set and were thus incomplete, many reconstructions included some of the most distal inputs (median ± SD of maximum soma distances: 90.9 ± 8.6 μm and 116.7 ± 29.4 for EM and LM, respectively) and should therefore sample the full gamut of input types."

This assertion is poorly motivated. The LM data had a mean dendritic path length of 3187 μm (main text, fifth paragraph), whereas the EM data had a maximum path length of 1956 μm. The maximum intact dendritic path length discovered in the EM volume therefore failed to reach the observed mean dendritic path length observed at the light level. The authors find that the distribution of synapses changes proximally; what data are available to suggest that this is not also the case distally? If none, it would be better to acknowledge this limitation, and leave the question open for future study.
