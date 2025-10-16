# Peer review - Round 1

Editors:
- Dori Derdikman, Technion - Israel Institute of Technology Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.33503.022](https://doi.org/10.7554/eLife.33503.022)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Inferring circuit mechanisms from sparse neural recording and global perturbation in grid cells" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Omri Barak (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In the article "Inferring circuit mechanisms from sparse neural recording and global perturbation in grid cells" the authors propose a way to show how different models of grid cell activity can be distinguished/falsified through experiments both in silico and in vivo. A wide variety of models explaining the grid cell pattern and network have been put forward since the discovery of grid cells in 2005. According to the authors existing data cannot distinguish between recurrent and feedforward models. The paper especially emphasizes velocity-based, continuous attractor models of grid cells using recordings from a small selection of neurons and methods to perturb the system. The authors claim that their suggested perturbation (cooling) combined with their novel measure (DRPS) could in part solve the "inverse problem" of inferring circuitry. The authors make the distinction between models that assume 1) a connectivity profile where the connectivity depends on the phase relationship between the neurons, termed the "fully connected", and those where the connectivity is determined by a distance between the neurons either 2) on a torus, "partially periodic", or 3) on a plane with tweaks on the edges, "aperiodic". By manipulating the network (e.g. changing the strength of the inhibition), the authors demonstrate that there can be a detectable change in the phase relationship between neurons in the partially periodic and aperiodic models. The manuscript offers quite an interesting and unusual perspective by giving direct suggestions on an experiment that could distinguish which of the models are correct. The last figure of the paper (Figure 5) is actually a very pedagogical decision tree for experimentally discriminating the underlying circuit mechanisms.

The paper is on one hand of great appeal, but on the other hand has major flaws: On one hand it is of great interest to the community, due to its nice link between a whole set of theories and potential experiments. Beyond the clear appeal to people working on grid cells, the systematic treatment of perturbation-based predictions could be relevant to other realms as well. However, all the reviewers have pointed to serious flaws in the paper, which should be addressed in order for the paper to be reconsidered for publication in eLife.

Given our concerns, we ask that you respond soon with a detailed plan to address the essential points below and provide an estimate of the time it may take to do so. The reviewing editor and referees will then consider your proposed work and issue a binding recommendation

Essential revisions:

1) Connection to real data: The paper would have been much stronger if it would have been more connected to real experiments. We note that an experiment including recordings of grid cells during a perturbation has already been published (Kanter et al., 2017). The authors in that paper used chemogenetic manipulations to determine the effects of hyperpolarization and depolarization on spatial coding in grid cells and how that is later read out by hippocampal place cells. Both manipulations resulted in reliable changes to the spatial tuning amplitudes but without a change in the placement of the fields in the environment or in the phase relationship between cells. We believe that the article here would suggest that this is the result of a feedforward mechanism and that the DRPS method would not be applicable. It seems appropriate that the authors mention this work and discuss under what conditions they might expect a different result.

2) Accounting for additional phenomena in grid cells: The method described here is designed to discriminate mostly between variants of the purely velocity-driven continuous attractor models of single modules. While these models have been useful in demonstrating how a network could integrate velocity, it is well known that any deviations from the assumed connectivity will cause the network to drift (Tsodyks and Sejnowski, 1995; Zhang, 1996), resulting in significant errors over time. Of course, this is easily remedied by additional spatial inputs (e.g. Pastoll et al., 2013) that could come from cues in the environment, such as encounters with a wall, or other mechanisms such as a very appealing interaction of grid modules of different spacing and the place cell system, as suggested by Sreenivasan and Fiete, 2011.

Furthermore, there is additional experimental work that single module velocity-driven networks would likely be insufficient to replicate, such as the field placements in a trapezoid (Krupic et al., 2015), the distortions (Stensola et al., 2015) and field-to-field variability in boxes (Dunn et al., 2017; Ismakov et al., 2017; Kanter et al., 2017).

The authors have to think whether the DRPS method would still be effective if drift or any of these experimentally-observed details are accounted for.

3) Scaling of velocity inputs: The model described here is a variant of the model described in Widloski and Fiete, 2014. This model multiplies the velocity input (Equation 7) by the synaptic input (see Equations 5 and 6). This is in contrast to the additive velocity input in Burak and Fiete, 2009 as well as many other models. This is an important detail since scaling the velocity input by the synaptic input partially mitigates the issue of the balance between the velocity and non-velocity input. It might be that if the velocity input was included additively, the network would much sooner result in extremely large or small periods than any detectable differences in phase relationships. Thus, the authors should check this more plausible variant of the model.

4) The scope of the models: The results of the paper are only valid within a limited set of models, that is not as inclusive as the authors describe. The authors present their analysis as a complete survey of all plausible candidate models. However, there are many other options. For instance, a feed forward model that also has strong lateral connections in the grid layer is one example of a hybrid model. We don't think the authors should cover every conceivable model, but the scope of the study could be stated more clearly.

Furthermore, Figure 5 suggests that, after perturbation, if the grid period has not changed then it should be a feedforward network. It would be more correct to say that it would rule out a purely velocity-driven, single-module continuous attractor model. One example of a non-feedforward mechanism that includes continuous attractor dynamics and might be able to handle (to some degree) such a perturbation would be Sreenivasan and Fiete, 2011. According to Figure 5, the experiment does not work if no change is observed, but maybe it is rather the model that were incorrect?

Related to the above points are the results presented in Figure 5—figure supplement 1. Does this indicate that not all the leaves in Figure 5 are expected to exist? In general, how robust are the different model classes?

We understand that the authors have to limit their investigation to a limited number of grid cell models, but it should be more clearly stated that the suggested experiment can only discriminate between these attractor dynamic models. Furthermore, a short discussion of grid cell models based on other principles should be mentioned in the manuscript.

5) Biological complexity: The authors suggest another experiment, manipulating the gain of inhibitory synaptic conductances, for example by infusion of benzodiazepines. Furthermore, they state that this manipulation has "unambiguous interpretation in terms of grid cell models". This statement is too strong, as we assume that the authors are not ignorant to the complexity of biological systems and cortical networks. None of the models considered in the paper takes into account the different cell types or different connectivity among the neurons in the different layers of entorhinal cortex (e.g. Fuchs et al., 2016). Without speculating on the effects of infusing a drug, it is likely not as clean as adjusting all the synaptic weights to the same amount in a model.

Furthermore, while the method described in the manuscript are able to infer circuitry and mechanism from a sparse population of "recorded" neurons, it does not seem to us that the authors consider that the model neurons are very homogeneous, in contrast to all in vivo recordings, that contain a lot of neurons that vary in tuning curves, regularity, firing rates, grid scores etc. Since the aim of the paper is to infer connectivity, there should be a discussion related to the different cell types and connections in the entorhinal network. We do not expect the authors to build a model representing all the biological complexity of different cell types, connections etc., but we think the paper would have improved if the authors discussed to what extent their model is robust to biological complexity.

[Editors' note: the authors’ plan for revisions was approved and the authors made a formal revised submission.]
