# Peer review - Round 1

Editors:
- Claude Desplan, New York University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.90505.3.sa0](https://doi.org/10.7554/eLife.90505.3.sa0)

Using continuum theory of elastic solids the authors present evidence that periodic muscle contraction leads to elongation of C. elegans embryos by storing elastic energy that is subsequently released by extending the embryo's long axis. This important finding could apply to other developmental processes and be exploited in soft robotics. The presented evidence is convincing on the phenomenological level adopted in the work. How bending energy is converted into elongation on a more microscopic level remains to be worked out.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90505.3.sa1](https://doi.org/10.7554/eLife.90505.3.sa1)

The authors have made a novel and important effort to distinguish and include different sources of active deformations for fitting C elegans embryo development: cyclic muscle contractions and actomyosion circumferential stresses. The combination and synchronisation of both contributions are, according to the model, responsible for different elongation rates, and can induce bending and torsion deformations, which are a priori not expected from purely contractile forces. The model can be applied to other growth processes in initially cylindrical shapes.

The tilt of the fibers is an important assumption of the model. However, fiber direction in Figure 3B is not fully clear for explaining the tilting. The fiber in 3B has not very much in common with the fibers in the color part of the figure. Also, is vector m supposed to be tangent to the fiber? In the figure does not seem to be so. It should be expected that alpha is a consequence of the deformation, not as an input parameter, as it seems in the tests of Figure 6A. How is the value of alpha chosen? According to Figure 6, torsion is expected for alpha>0, but for beta=pi/2 and alpha>0 no torsion may be obtained. In fact, it seems that torsion should appear when cos(beta)*sin(alpha)>0. As a consequence, value of beta should be given in Figure 6. Can the amount of torsion be tested as a function of alpha and beta?

The transfer of energy and deformation is a very interesting aspect of the paper, and also crucial for the model and predicting elongation. However, the modelling of this transfer remains very obscure and only explained in the Appendix. Some more details on how the transfer is selected should be given in the main text. Can the transfer of energy interpreted as a change of the relaxed reference configuration? Once a ratio of the energy transferred is fixed, the assumption on elongation distribution should be stated. (Uniformly? ) The authors should also define in the main text the factor g_a1, and explain how this value is computed from condition W_c=W_r .

Given the convoluted shape of the embryo in the egg, contact may be a crucial mechanism for determining growth and torsion. The model does not include this contact, and this limitation should be reflected in the article.

Minor comment:

-Line 300: "we determine the optimal values for the activation parameters". the optimal with respect to which objective? Norm of difference between experimental and computational displacements? How this is quantified needs to be specified.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90505.3.sa2](https://doi.org/10.7554/eLife.90505.3.sa2)

Summary:

During C. elegans development, embryos undergo elongation of their body axis in absence of cell proliferation or growth. This process relies in an essential way on periodic contractions of two pairs muscles that extend along the embryo's main axis. How contraction can lead to extension along the same direction is unknown.

To address this question, the authors use a continuum description of a multicomponent elastic solid. The various components are the interior of the animal, the muscles, and the epidermis. The different components form separate compartments and are described as hyperelastic solids with different shear moduli. For simplicity, a cylindrical geometry is adopted. The authors consider first the early elongation phase, which is driven by contraction of the epidermis, and then late elongation, where contraction of the muscles injects elastic energy into the system, which is then transferred into elongation. The authors get elongation that can be successfully fitted to the elongation dynamics of wild type worms and two mutant strains.

Strengths:

The work proposes a physical mechanism underlying a puzzling biological phenomenon. The framework developed by the authors could be used to explain phenomena in other organisms and could be exploited in the design of soft robots.

Weaknesses:

(1) The manuscript is hard to read without being very familiar with continuum descriptions of elastic media. This might make the work difficult to access for biologists. This is a real pity because the findings are potentially of great interest to developmental biologists and engineers alike.

(2) The discussion of the worm's mechanical properties could go deeper. The authors hardly justify their assumptions.
