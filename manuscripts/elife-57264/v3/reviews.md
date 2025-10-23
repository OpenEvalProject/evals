# Peer review - Round 1

Editors:
- Sebastian Deindl, Uppsala University Sweden

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.57264.sa1](https://doi.org/10.7554/eLife.57264.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Given the ubiquitous nature of binding measurements in the literature, including newly emerging high-throughput approaches, this manuscript addresses an important and timely topic. This manuscript is particularly compelling in providing an easy-to-follow set of practical guidelines exemplified with relevant binding data. The authors' approach to this important topic is highly pedagogical and should be a must-read for anyone with the ambition to quantitatively characterize binding equilibria.

Decision letter after peer review:

Thank you for submitting your article "How to measure and evaluate binding affinities" for consideration by eLife. Your article has been favorably reviewed by two peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by John Kuriyan as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

In this manuscript, a review of 100 studies reporting on binding measurements is presented, allowing the authors to identify and illustrate a number of pitfalls and issues that often adversely affect the reliability and meaningful biological interpretation of binding equilibrium measurements. Using example binding measurements to illustrate the most relevant points, the authors provide a straightforward, practical set of guidelines in terms of a step-by-step “checklist” that can be followed to ensure acquisition of high-quality data best suited to quantitatively describe simple binding equilibria. Given the ubiquitous nature of binding measurements in the literature, including newly emerging high-throughput approaches, this manuscript addresses an important and timely topic. While there may be at least partial overlap with previously published literature on this topic, this manuscript is particularly compelling in providing an easy-to-follow set of practical guidelines exemplified with relevant binding data. The manuscript is well written and accompanied with a number of high-quality and clear illustrations. As such, the authors' approach to this important topic is highly pedagogical and should be a must-read for anyone with the ambition to quantitatively characterize binding equilibria.

Revisions:

The authors should address the following points to further improve clarity of the manuscript:

1) While the need for the equilibration time control is clear, the requirement for changing the concentration of the second species to probe whether ligand depletion could affect Kd measurements seems to be less universal. If a Kd value, as obtained via binding experiment, is substantially larger than the concentration of the labeled species, it would not be strictly necessary to test for potential ligand depletion. It would be important to take this notion into account in the literature survey so as to indicate those cases where a titration regime could indeed be plausible. It would be useful to provide examples from the literature of Kd values that were underestimated due to ligand depletion. The authors should consider emphasizing the specific conditions where ligand depletion might be overlooked (e.g. high-affinity interactions requiring the use of particularly low concentrations of the labeled binding partner, where concentration uncertainty could play a significant role, and a very low active concentration of the protein). That said, varying the equilibration time is an extremely useful control that should be recommended, but perhaps the authors could be more specific as described above. The authors should also consider emphasizing that the inability to obtain a good fit with a hyperbolic function should be considered a serious warning sign that could indicate insufficient equilibration or ligand depletion. The requirement to rigorously report binding curves and fits could be an important part of a binding data reporting standard. In particular for indirect methods such as EMSAs, binding curves and fits are often omitted.

2) Cpf1 is discussed as an example where affinity is substantially underestimated. However, this particular example appears more complicated and likely requires factors other than insufficient incubation time to be considered: First, in one of the studies reporting a 1000-fold lower affinity, a koff of 1/(several seconds) was directly measured using a smFRET assay; Second, the experimental conditions that are known to affect binding were different in all three studies being compared, including temperature, buffer composition (specifically, divalent ions), as well as RNA and DNA sequences; Moreover, in some cases, the Cpf1 proteins were from different species (Strohkendl et al., 2018, and the study reporting the lowest affinity).

Indeed, this illustrates another common mistake when reporting or using binding affinities: treating them as constant values rather than functions of many variables, and ignoring experimental conditions and other important details when comparing the values. It would be important (and educational) to emphasize this in the manuscript, see also minor points for more details. This all being said, Cpf1 still makes a good case for the authors' main point regarding the need to prove that binding is at equilibrium, since the lack of this proof in the study reporting the lowest affinity creates a lot of confusion.

3) In Appendix 3, Weeks and Crothers, 1992 is cited for a precise competitive binding equation for the case of Kd,comp close to total concentration of P, but the solution to the quadratic equation in Weeks and Crothers does not represent a general equation for competitive binding. Instead, the same approximation as in Lin and Riggs (Kd,comp>>total concentration of P) is assumed and the equation is solved for theta to obtain a binding curve rather than a single point for theta=0.5. This approach should still be considered superior when compared to determining Kd,comp from a single data point since it takes all the other data of the curve into account. However, this approach still cannot be used in case of comparable affinities for competitor and labeled ligand. Instead, a general competitive binding curve should be used that represents a correct solution to the cubic equation (see, for example, PMID: 7875313).
