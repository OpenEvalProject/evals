# Peer review - Round 1

Editors:
- Felix Campelo, Institute of Photonic Sciences Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.101885.3.sa0](https://doi.org/10.7554/eLife.101885.3.sa0)

This is a valuable report of a spatially-extended model to study the complex interactions between immune cells, fibroblasts, and cancer cells, providing insights into how fibroblast activation can influence tumor progression. The model opens up new possibilities for studying fibroblast-driven effects in diverse settings, which is crucial for understanding potential tumor microenvironment manipulations that could enhance immunotherapy efficacy. While the results presented are convincing and follow logically from the model's assumptions, some of these assumptions, as acknowledged by the authors, may oversimplify certain aspects in light of complex experimental findings, system geometry, and general principles of active matter research. Nonetheless, the authors provide justification for their work as a meaningful step towards more comprehensive modeling approaches.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.101885.3.sa1](https://doi.org/10.7554/eLife.101885.3.sa1)

The authors present an important work where they model some of the complex interactions between immune cells, fibroblasts and cancer cells. The model takes into account the increased ECM production of cancer-associated fibroblasts. These fibres trap the cancer but also protect it from immune system cells. In this way, these fibroblasts' actions both promote and hinder cancer growth. By exploring different scenarios, the authors can model different cancer fates depending on the parameters regulating cancer cells, immune system cells and fibroblasts. In this way, the model explores non-trivial scenarios. An important weakness of this study is that, though it is inspired by NSCLC tumors, it is still far from modelling tumor lesions with morphologies similar to NSCLC tumors and does not explore the formation of ramified tumors. In this way, is a general model and it is challenging how it can be adapted to simulate more realistic tumor morphologies.

Comments on revisions:

The authors have improved the manuscript and addressed my concerns.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.101885.3.sa2](https://doi.org/10.7554/eLife.101885.3.sa2)

Summary:

The authors develop a computational model (and a simplified version thereof) to treat an extremely important issue regarding tumor growth. Specifically, it has been argued that fibroblasts have the ability to support tumor growth by creating physical conditions in the tumor microenvironment that prevent the relevant immune cells from entering into contact with, and ultimately killing, the cancer cells. This inhibition is referred to as immune exclusion. The computational approach follows standard procedures in the formulation of models for mixtures of different material species, adapted to the problem at hand by making a variety of assumptions as to the activity of different types of fibroblasts, namely "normal" versus "cancer-associated". The model itself is relatively complex, but the authors do a convincing job of analyzing possible behaviors and attempting to relate these to experimental observations.

Strengths:

As mentioned, the authors do an excellent job of analyzing the behavior of their model both in its full form (which includes spatial variation of the concentrations of the different cellular species) and in its simplified mean field form. The model itself is formulated based on established physical principles, although the extent to which some of these principles apply to active biological systems is perhaps debatable (see Weaknesses). The results of the model do indeed offer some significant insights into the critical factors which determine how fibroblasts might affect tumor growth; these insights could lead to new experimental ways of unraveling these complex sets of issues and enhancing immunotherapy. In this revised version, the authors have properly placed this work within the general context of other research on modeling the tumor-immune ecology.

Weaknesses:

Models of the form being studied here rely on a large number of assumptions regarding cellular behavior. One major issue is the degree to which close-to-equilibrium assumptions (such as the dynamics being driven by free energy minimization) can be taken as reliable predictors of the obviously active dynamics of biological cells. The authors have recognized this conceptual issue and have argued that these assumptions provide a reasonable first step for understanding the full complexity of dynamics in the tumor microenvironment.

The problem of T cell infiltration as well as the patterning of the extracellular matrix (ECM) by fibroblasts necessarily involve understanding cell proliferation, cell motion and cell interactions due e.g. to cell signaling. There is evidence that inherently non-equilibrium interactions between the fibroblasts and the extracellular matrix can lead to patterning of the fiber network and trapping of potentially infiltrating T-cells. it is not clear the extent to which this type of interaction can be captured by the approach being used here, although the authors propose that they can be mimicked by proper terms in their formulation. This to me is the primary concern that I had with this paper.

The authors have now addressed what used to be a separate weakness concerning the assumption that fibroblasts affect T cell behavior primarily by just making a more dense ECM. Instead, the organization of the ECM (for example, its anisotropy) could be playing a much more essential role than is given credit for here. This possibility is now discussed in some detail and the authors have suggested that the introduction of a nematic order parameter field would be a useful way to treat this effect.
