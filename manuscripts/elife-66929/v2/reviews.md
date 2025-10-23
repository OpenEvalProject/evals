# Peer review - Round 1

Editors:
- Karsten Kruse, University of Geneva Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66929.sa1](https://doi.org/10.7554/eLife.66929.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript presents computer simulations that demonstrate how smooth boundaries can be created between a zone of active expansion and a second zone of active constriction that surrounds it. This work is of interest to scientists working in the field of cytoskeletal organization, mechanobiology, and self-organizing active matter.

Decision letter after peer review:

Thank you for submitting your article "Emergence of a smooth interface from growth of a dendritic network against a mechanosensitive contractile material" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Anna Akhmanova as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Provide a physical (or mechanistic) explanation for the observed smoothening behavior.

2) Test how sensitive the main results are to initial conditions, and to different parameter values by performing a sensitivity analysis (especially on the wild-type like cases).

3) Describe the model a bit more specifically at the beginning of the result section so the reader has a general sense of how it was implemented.

4) Using physically relevant units in the text and the table would make it easier to follow and potentially more impactful. Or the authors should explain if there is a good reason to keep those non-physical units.

5) Please provide Matlab files at resubmission.

Reviewer #1:

The authors attempt to understand the basis of smoothing interfaces between Arp2/3-based actin networks and actomyosin networks in the syncytial Drosophila embryo during pseudo-cleavage. This is an interesting question in the context of how actin networks are organized. To understand interface smoothing, the authors perform "node-based" simulations of the two actin networks. The simulation methods of the two networks follows previously published methods and are validated through comparisons with previous work. For the interface between these networks, the authors invoke some ad hoc rules that are poorly justified form a physical point of view. It is not clear, how much their results depend on this choice of interfacial dynamics. Whereas the simulation results are quantitatively analyzed, there is essentially no quantification of the experiments, and the comparison between experiment and theory remains qualitative. Eventually, the authors propose a set of ingredients that are sufficient to yield smooth interfaces in their simulations. However, a thorough understanding in terms of the physical mechanism underlying the simulation results remains elusive. For these reasons, in its current state, this works seems of limited use for the community.

Reviewer #2:

In this manuscript, Sharma et al., aim to better understand the mechanical mechanisms underlying the organization of the syncytium, the cortical meshworks of actin and myosin under the surface of the fly embryo during early embryo development. This meshwork is composed of two networks that self-organize into circular caps containing branched actin filaments and surrounded by an acto-myosin constrictive network. Using a model based on nodes that follow simple mechanical rules, the authors demonstrate that one can start with roughly defined zones where each meshwork is defined, and only in certain conditions these zones will become clearly defined with a smooth border as seen in the fly embryo. They show that clear and smooth boundaries appear only when a branched actin meshwork expands in the caps and when there the surrounding acto-myosin network exerts enough contractile forces especially at the interface between both meshworks.

Strengths:

The modeling of the actin and myosin meshworks is performed using phenomelogical rules at a meso-scale, which allow the authors to focus on general mechanical properties of the meshworks and limit the number of free parameters.

The authors nicely demonstrate what mechanisms cannot lead to smooth boundaries and which one can.

The authors systematically compare their simulations with experimental data in wild-type and in knock-down flies that have been published before or that they generate for this study.

Weaknesses:

The parameters are discussed in the text in arbitrary non-physical units (e.g. pixels, steps, etc.). It is sometimes difficult to follow whether the values used are realistic or not. That said the parameter table gives some equivalence but this prevents a smooth read.

Some of the parameters used in all the simulations are set to certain values but those values are often not discussed, and it is unclear to which extent the results of the simulations are sensitive to those parameters.

The code is provided only as a pdf file which prevents the reader to run the simulations themselves.

The authors could test how sensitive their main results are to initial conditions, and to different parameter values by performing a sensitivity analysis (especially on the wild-type like cases).

Please provide Matlab files at resubmission.

Things that could be clarified:

The authors could explain a bit more how the initial rough patterns of Arp2/3 and acto-myosin zones are generated in the embryo. Is it signaling? Could it be self-organized from a random initial organization by the mechanics too?

They could describe the model a bit more specifically at the beginning of the result section so the reader has a general sense of how it was implemented.

Using physically relevant units in the text and the table would make it easier to follow and potentially more impactful. Or the authors should explain if there is a good reason to keep those non-physical units.
