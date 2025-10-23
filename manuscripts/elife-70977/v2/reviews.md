# Peer review - Round 1

Editors:
- Naama Barkai, Weizmann Institute of Science Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70977.sa1](https://doi.org/10.7554/eLife.70977.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Supracellular organization confers directionality and mechanical potency to migrating pairs of cardiopharyngeal progenitor cells" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Ajay Chitnis (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

As you will see, the reviewers found your paper interesting but raised some concerns. Please address them in full before resubmitting.

Reviewer #1:

In this manuscript, authors develop a computational model of migrating pairs of cardiopharyngeal progenitors in Ciona model to describe their properties during migration. Most of the predictions drawn from the simulations are corroborated experimentally in vivo. The polarized migrating pair of progenitors represent a minimum unit of collective migration showing essentially that "two cells are better than one".

The simulation of the migrating cell pair is based on Cellular Potts Model and uses cell morphology as a proxy to model different mechanical and cellular forces that generate specific cell shapes during migration. The model seems to faithfully reproduce the in vivo observations. The arguments describing the model are well explained. The model thus provides a number of predictions pertaining the migrating cell collectives that can be tested in vivo using genetic and molecular tools. The authors then test some of the predictions prompting them to conclude that the migrating progenitor pair present the simplest model of collective migration, in which the two cells are intercellularly coupled and their polarization occurs across the two-cell continuum, thus forming a supracellular collective. This cell collective displays hierarchy, which favors linear arrangement conferring directionality and persistence in migratory behavior. While some conclusions are well justified and the experimental evidence corroborates the simulations, at few points the conclusions are more speculative; the figure panels not always match the manuscript text. The concept that the migrating pair can deform the overlaying endoderm is the least developed and not probed in vivo. In summary, the computational model represents a powerful tool to examine directional migration of polarized cell collectives with similar characteristics allowing for studying how biomechanical cues integrate with molecular signals across group of cell collectives to coordinate their behavior.

In Figure1: The manuscript text does not follow the arrangements of figure panels. First data corresponding to 1A, C, D are described and only then to 1B. Then 1F is described before 1E. Also in the Figure 1F is mislabeled as 1G. This is all quite confusing to follow.

The shape measurements should be described in a schematic. The L/T sphericity label in y-axis of graph in C suggests it is a ratio, but the overall shape was measured. In D, the bounding box with the length and width should be indicated. Were all measurements performed on dorsal views?

In Figure 1E, the non-muscle myosin distribution has to be better quantified. While the line plots suggest the depletion from the leader-trailer cell membrane junction, myosin appears to be accumulating at the front of cell periphery in both leader and trailer. The claim that it is relatively depleted is not entirely true when looking at the example presented. What is the myosin distribution in the sagittal sections? What is the distribution of actin? The more detailed actomyosin distribution would further support the model in 1B. On what data are the conclusions about absence of "contractility organized in supracellular fashion" based on? It seems that leader overall may have less non-muscle myosin then trailer, suggesting that maybe there is a polarized distribution of myosin.

In Figure 2: In the first paragraph, the concept of supracellular polarity between leader and trailer should be introduced as a hypothesis. At the current state it seems that just the change in their shape justifies the claim that the pair is supracellularly polarized.

In 2A, graph at right, when is the sphericity measured, only when DdrDN is expressed in trailer or leader? This needs to be clarified.

Because the authors in these sets of experiment also point out that increased protrusive behavior is more likely adopted in the leader cell, the conclusions drawn here in this section about the polarization at the supracellular level have to be taken this data into account. In similar way as presented in the introduction to Figure 3.

Figure 3:

Similar to Figure 1, the figure panels do not completely follow the manuscript text. Please revise.

The fact that the simulation predicts the hierarchy in the linear arrangements is one of the key findings. The presentation of the in vivo data in Figure 3E are however not so easy to follow. The confusing part is to follow the numbers (in %) between the manuscript text and the graphs in 3E. If the alignment occurs only at 57%, isn't it then random?

What is the unit of displacement of y-axis in 3H bottom graph.

Figure 5:

The concept of endoderm deformation has to be clarified. The readers that are not directly from the field of TCV migration may not necessarily understand it. Do the authors mean the little pocket that endoderm forms around TCVs shown in merge of 5A? If that is the case, please add arrowheads or similar to highlight this better. The deformation is then happening locally at the cellular level. The term “deforming endoderm” implies the deformation at the tissue-scale. This needs clarification.

What is the evidence for differing stiffness of endoderm and epidermis?

What are the values and units for “varying endoderm stiffness”? At the minimum some relative value should be added here to understand the difference in the odelling parameters. Are the assumptions about the stiffness based on physiological values?

If the endoderm is soft, to what extent it is important to consider its mechanical resistance? Afterall, the 2-cell equivalent significantly outperformed the supracellular arrangements with soft endoderm. This should be commented.

While interesting to use the modelling to understand the forces from the surrounding tissue exerted on the migrating cell pair, the concept here is the least developed and not tested experimentally. The sentence in the abstract referring to this data is somewhat misleading and needs revising.

Statistics: in some experiments the N number of biological replicates is indicated, but not in all experiments. This should be corrected. In the methods section, Mann-Whitney test is described as used to compare two experimental groups, but in some panels t-test with Welch’s correction is used. It should be clarified and corrected. What software/tool was used to perform statistical tests? The in vivo data should be presented with S.D. not S.E.M.

Overall, it is very interesting study, and the power of the computational simulation is very well reflected in the in vivo experiments. My main recommendation for improving the manuscript (in addition to above points) is to re-write the flow, to simplify the motivations for the experiments, and conclusions drawn from it, and leave the speculations and assumptions for the discussion.

Reviewer #2:

In this study, the authors develop a model to understand the collective migration of migrating pairs of cardiopharyngeal progenitor cells. This represents an simplest form of collective migration with two cells. They propose that the collective migrates as a “supracell”, with leader cells assuming a greater protrusive capability and trailer cells assuming greater retractive capability. They meticulously study the effects of leader-trailer and cell-matrix adhesivity, intracellular force distributions and noise on robustness of cell migration. They corroborate their simulation results with experiments. Overall, this study comprehensively demonstrates that migrating as a collective leads to more mechanically efficient and persistent migration than as a single motile cell. A particular strength of the paper is that the authors have done an excellent job of explaining how the Cellular Potts Model works and how they chose to represent specific biological details using this modelling environment. The model is also likely to provide a useful framework for development of models of more complex examples of collective migration.

Specific comments questions:

1. Page 3, para 1 – "TVCs maintain polarized and bulky shapes as they invade…". It would be helpful if the authors could clarify what they mean by polarized and bulky.

2. Quantification and Statistical Analysis, Page 14 – What was the size of Gaussian filter chosen by the authors to preprocess their images?

3. How would the authors biophysically justify their choice of protrusive force strength being a function of (α – φ), while retractive force strength is a constant value? Would simulation results differ significantly if retractive force strength in trailer or single cells is a function of (β – φ) or (90⁰ – φ)?
