# Author response - Round 1

Authors:
- Silvia JH Park
- Evan E Lieberman
- Jiang-Bin Ke
- Nao Rho
- Padideh Ghorbani
- Pouyan Rahmani
- Na Young Jun ([ORCID: 0000-0002-8841-3947](https://orcid.org/0000-0002-8841-3947))
- Hae-Lim Lee
- In-Jung Kim
- Kevin L Briggman ([ORCID: 0000-0003-2946-4661](https://orcid.org/0000-0003-2946-4661))
- Jonathan B Demb ([ORCID: 0000-0003-2227-9041](https://orcid.org/0000-0003-2227-9041))
- Joshua H Singer ([ORCID: 0000-0002-0561-2247](https://orcid.org/0000-0002-0561-2247))

## Response text

DOI: [10.7554/eLife.56077.sa2](https://doi.org/10.7554/eLife.56077.sa2)

Reviewer #1:

[…] I have several questions and suggestions about places the paper could be strengthened:

Subsection “Functional relevance”: Was it not possible to probe the NOS-1 cells at lower light levels? It would be quite interesting to see the contributions of rod and cone input to their responses given the proposed circuitry and functional role.

The main difficulty with this experiment is that we have to identify fluorescent reporter expressing NOS-1 cells by 2PLSM using an IR laser, the light from which alters the responses of rods and shifts their response thresholds, as a number of groups have shown. Therefore, we decided to work at a light level above absolute rod threshold but still within the range where rod bipolar cells are active. This is now explained in the Discussion (subsection “The NOS-1 AC is the dominant inhibitory input to the AII and generates the AII surround”) and the Materials and methods section.

The assumption that all conventional synaptic input to the NOS-1 cell is inhibitory should be qualified given the presence of amacrine cells that release glutamate, and non-ribbon synapses made by bipolar cells.

We added some discussion of glutamatergic amacrine cells, though, as we note, it is unlikely that the well-studied VGLUT3 cell provides synapses to the NOS-1 AC. As well, we make the point that we followed the neurites of putative AC inputs over some short distance to confirm their identities as ACs (subsection “Anatomical assessment of an AC circuit presynaptic to the AII”).

Quantification. Several anatomical observations would be stronger with some quantification. This includes the proximity of the AC-AII synapses and the dendritic branching angle (subsection “Anatomical identification of inhibitory synaptic inputs to AIIs”).

We calculated the distance between each AC–>AII synapse and the nearest RB–>AII synapse (on the same AII). The resulting distribution is illustrated in Figure 3C4. We note that 50% of the AC–>AII synapses are within 2.26 µm of a RB–>AII synapse, indicating that the inhibitory AC input is positioned to modulate the AII response to excitatory input from the RB (subsection “Anatomical identification of inhibitory synaptic inputs to AIIs”). Also, we deleted any mention of branching angle from the revised text because we do not have enough observations to make any quantitative assessment of the significance of the observation.

Subsection “The NOS-1 AC is the predominant NOS-expressing AC in the ganglion cell layer and is distinct from CRH-expressing ACs”: how does the sustained ON response uniquely identify NOS-1 cells? Specifically, could there be another cell type with a sustained ON response that is mixed in? To establish this definitively it seems you would need to fill the recorded cells and see if they share similar morphology. Related, do the brightly labeled cells have NOS-1 morphologies?

We didn’t observe any diversity in the morphology of these cells: all had small field of dendrites in the OFF layer and branching axons in the ON layer. This is mentioned in the revised text (subsection “The NOS-1 AC is a spiking ON cell”).

Subsection “Propagation of the AII surround to downstream ganglion cells”: surrounds inherited from the AII might be expected to be similar across RGC types. This does not appear to be the case, as the surround in the OFF α looks somewhat stronger than the other two cells. It would be helpful to fit the dependence of the response on stimulus diameter to compare parameters of a difference of gaussian model and see if they are consistent.

We are going to decline, respectfully, to take this suggestion. For this purpose, we think the difference-of-Gaussians model to be too poorly constrained (fitting diameter-response curves with four parameters: peak and space constant of center and surround) to be useful. Furthermore, the recorded IPSCs reflect all inhibitory input to the OFF α and δ cell types, not just the AII input, and therefore diversity across ganglion cells is expected: we would not expect identical tuning curves unless the synaptic inputs to the cells were identical, which they are not. We commented on this point (subsection “Propagation of the AII surround to downstream ganglion cells”).

Reviewer #2:

[…]

I do think the authors could make more of an effort to connect to a wider audience in the Abstract and Introduction. The paper is a straightforward read for a retinal neuroscientist, but I'm not sure a neuroscientist outside of that field will understand what is really interesting and important here. For example, the first two sentences of the Abstract build almost zero interest and give little insight to the core problem or why understanding this circuit is interesting. Pitching the paper as “understanding where the surround under scotopic conditions comes from” would at least pull in a broader community of vision scientists who would understand why that problem is important. Similarly, in the Introduction, the authors don't really cue the reader into the question they are tackling until the end of the 4th paragraph. I don't think a full exposition of the rod circuit is necessary before letting the reader know what question the paper is answering, and the current approach seems likely to put off casual readers. That said, leaving the manuscript “as is” would already put it in the top ~5% of manuscripts that I've read.

We thoroughly revised the Abstract and Introduction accordingly.

Reviewer #3:

Specific comments:

1) Surround inhibition of AII amacrine cells in control conditions (Figure 2) is tested only with small stimuli. This is a mismatch to the stimuli used for ganglion cells, nNOS1 amacrine cells, and AII cells after the deletion of nNOS1 amacrine cells. The authors should include larger stimuli in their experiments in Figures 2A-D, to allow for better comparisons between datasets.

While the paper was under review, we had the opportunity to collect additional data from a more suitable control group (Cre-negative animals that had been injected with AAV and tamoxifen; and from the same breeding cage as the Cre-positive/DTA animals). We also used the same range of spot sizes. The new data are presented in Figure 7. The responses at the largest three spot sizes was significantly smaller in the DTA recordings compared to the control recordings. We also updated all of the control cell counting data from these new retinas (n = 6; Figure 7).

2) The authors show that the removal of nNOS1 amacrine cells by viral expression of diphtheria toxin reduces the surround inhibition of AII amacrine cells. To elucidate the significance of nNOS1 amacrine cells to the output signals of the retina, I encourage the authors to test the effects of nNOS1 removal on spike response of ON α, OFF α, and OFF δ cells. This would boost the significance of the study.

We are not able to collect this data. Further, we think that this experiment would be complicated by the fact that the nNOS-CreER retina labels multiple cell types, and so the DTA will necessarily ablate NOS-2 cells, for example, which are the main source of NO release in the retina. The total effect of ablating all NOS+ cells could have effects beyond the elimination of the NOS-1 –> AII synapse. For this reason, we think a full evaluation of the role of NOS-1 cells in retinal function (and behavior) will require more selective genetic targeting of the NOS-1 cell. We now make this point in the Discussion section (subsection “Functional relevance”).

3) I suggest changing the order in which optogenetic and diphtheria toxin experiments are presented. It seems more natural to me to follow the anatomical discovery of connections between nNOS1 and AII amacrine cells with their functional confirmation (i.e., optogenetics) and then to move on to the perturbation that elucidates the functional significance of nNOS1 – AII amacrine cell connections.

We are going to decline, respectfully, to do this. We think that the optogenetic experiments are a better indicator of the function of the circuit than are the DTA experiments.

4) For the synaptic constellations in Figures 4D and 4E, it would be great if the authors could include supplementary videos scrolling through successive planes.

We have created two supplementary videos.

5) I was slightly confused by the inclusion of ON SACs as a laminar marker in Figure 4C and suggest switching to the same gray ON and OFF SAC bands as in Figure 4A.

We revised the figure accordingly.

6) In a supplement for Figure 4, it would be great if the authors could show en face views of the arrays of the different bipolar cell types connected to each nNOS1 amacrine cells (including only bipolar cells with synapses onto the respective target).

We revised the figure accordingly.
