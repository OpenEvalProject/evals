# Peer review - Round 1

Editors:
- Rishidev Chaudhuri, UC Davis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.56894.sa1](https://doi.org/10.7554/eLife.56894.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Grid cells and place cells are populations of neurons that are thought to work together to represent an animal's spatial position using complementary encodings of space. This paper provides a simple but compelling mechanistic model of how they might interact and, in doing so, suggests explanations for a variety of experimental findings.

Decision letter after peer review:

Thank you for submitting your article "Bidirectional coupling of hippocampus and MEC accounts for grid field variability and artificial place cell remapping" for consideration by eLife. Your article has been reviewed by Laura Colgin as the Senior Editor, a Reviewing Editor, and three reviewers. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below primarily address clarity and presentation and require only minor additional numerical simulations.

Summary:

Agmon and Burak present a novel integrated model of grid cell and place cell networks, with bidirectional coupling between grid cells in the medial entorhinal cortex and place cells in the hippocampus. The model combines attractor dynamics in the hippocampus and in multiple grid modules in an interesting and consistent manner. Despite its relative simplicity, the joint place cell-grid cell network can explain a wide range of experimental findings, including that hippocampal place cells and hippocampal remapping can persist without MEC, the variability of firing rates across grid fields, and the intriguing observation that artificial hippocampal remapping is induced by depolarization but not hyperpolarization of MEC inputs to the hippocampus.

Overall, the model surpasses previous feedforward models, is implemented at an appropriate level, is presented in language that is accessible to experimentalists and is quite timely given recent puzzling observations on the relation between grid cells and place cells.

Essential revisions:

1) The operation of the network should be presented more thoroughly. The development of this combined network is a major result, but it is a bit unclear how the network produces the reported results. In particular:

a) Illustrating bump dynamics. The only dynamical data presented in the paper relates to path-integration and drift. When a bump develops from random initial conditions, does it do so steadily or in spurts? Similarly, how does bump score across different maps evolve when the bump develops into a mixed state?

b) How many maps can be stored by the network? In the Supplementary Material, the authors calculate that this number scales with the number of neurons. Do simulations support this result, and what is the scaling prefactor?

c) What range of parameters, especially the relative strength of connections within and across subnetworks, produce desired results?

2) How does the place cell network operate without grid cell input, and how does this compare to MEC lesion experiments? What activity patterns appear? I presume that it would not path-integrate-is this true? Also, it seems that place cell remapping arises from grid cell inputs, namely, map-dependent shifts in grid cell phase – is this true?

3) All the modeling presented in the paper is done in 1-d. It would be useful to confirm that it indeed also works in 2-d (and use the grid scales consistent with the experimental data). This would facilitate the comparison to (future) experimental results.

4) In addition to artificial remapping, where the firing rate distribution across grid fields is experimentally manipulated, a reorganization of the firing rate among grid fields can also be naturally observed in rate remapping paradigms (Diehl et al., 2017). Although the authors may have omitted this experimental finding because it does not fit into their framework of the place cell network mimicking global remapping, some of their analysis of artificial remapping shows that their network can in principle generate persistent mixed states. More in depth analysis should be added which describes to what extent the findings by Diehl et al. can be reproduced by the current network architecture or whether major modifications would be necessary. The Introduction, Results and Discussion sections should be expanded to include these analyses and their interpretation.

5) Correction of drifts: It is interesting that the network can correct the drift of the grid module. There has now been a literature on this issue (Hardcastle, Ganguli and Giocomo, 2015; Mulas, Waniek and Conradt, 2016; Pollock et al., 2018). In particular these studies have shown that error correction can happen between the boundary cell or landmark cells to grid cells. It is unclear if/how the current error-correction mechanism fundamentally differs from the previous studies. It would be useful to clarify these issues. Also, how is "incompatible drift" defined in subsection “Coordination of the grid cell representation: suppression of incompatible drifts”?

6) Robustness with respect to the selection of the grid modules: The authors used [38.4,48, 64]cm for the 3 grid modules. Are the predictions robust with respect to the selection of the modules? For example, the form of decoding error using ML estimate would depend on the how the scales of the module are organized. With a hierarchical grid code (Mathis et al., 2012; Wei et al., eLife 2015), it is much less prone to non-local errors, unlike the residual number system studied by Fiete et al., (2008).

7) One highlight of the current work is that the model could account for the seemingly paradoxical finding in Kanter et al., (2017). However, as the authors pointed out that there is also the issue regarding the generality of the finding in Kanter et al., (2017). Is there a regime that the proposed model can also account for Miao et al., (2015)? The authors wrote: "while in Ref (Kanter et al., 2017) chemogenetic receptors were targeted almost exclusively to layer II stellate cells of the MEC in transgenic animals, a broader population has been likely affected using viral injection in Ref (Miao et al., 2015)." The argument may not address the problem, because both stellate cells and pyramidal cells in EC2 can be grid cells. These points need to be more carefully discussed, as it is critical to the test of the proposed model.

8) The rationale behind the variability in individual grid firing here bears some similarity to Dunn et al. (Dunn et al., 2017). This relationship needs to be clarified.

9) Quantification of the model predictions: Regarding the variability of individual grid firing fields, is it possible to quantify the effect and compare it to the publicly available grid cell dataset? Similarly, is it possible to quantify the model prediction on artificial mapping and put it into a format which would be more directly comparable to the data at the neural population level?
