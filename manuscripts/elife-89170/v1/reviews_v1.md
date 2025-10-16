# Peer review - Round 1

Editors:
- Mariana Gómez-Schiavon, Universidad Nacional Autónoma de México Mexico

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.89170.3.sa0](https://doi.org/10.7554/eLife.89170.3.sa0)

The paper presents valuable computational findings on how growth feedback affects the performance of synthetic gene circuits designed for adaptive responses. By systematically analyzing over four hundred circuit topologies, the authors provide solid evidence for their conclusions on failure mechanisms and design features that enhance robustness against growth dynamics. While the study's significance and rigor are somewhat constrained by its reliance on previously published network topologies, these results are highly relevant for advancing the engineering of gene circuits in various applications.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.89170.3.sa1](https://doi.org/10.7554/eLife.89170.3.sa1)

Engineered artificial gene regulatory networks ("circuits") have a wide range of applications, but their design is often hindered by unforeseen interactions between the host and circuit processes. This manuscript employs computational modeling to investigate how growth feedback influences the performance of synthetic gene circuits capable of adaptation. By analyzing 425 hypothetical circuits previously identified as achieving nearly perfect adaptation (Ma et al., 2009; Shi et al., 2017), the authors introduce growth feedback into their models using additional terms in ordinary differential equations. Their simulations reveal that growth feedback can disrupt adaptation dynamics in diverse ways but also identify core motifs that ensure robust performance under such conditions. Additionally, they establish a scaling law linking circuit robustness to the strength of growth feedback. The findings have important implications for synthetic biology, where host-circuit interactions frequently compromise desired behaviors, and for systems biology, by advancing the understanding of network motif dynamics. The authors' classification schemes will be highly valuable to the community, offering a framework for addressing growth-related challenges in circuit design.

Strengths

- A detailed investigation into the reasons for adaptation failure upon the introduction of cell growth was conducted, distinguishing this work from other studies of functional screening in gene regulatory network topologies. The comprehensiveness of the analysis is particularly noteworthy.

- Approaches for assessing robustness, such as the survival ratio Q, were employed, providing tools that may be applicable to a broad range of network topologies beyond adaptation. The scaling law derived from these approaches is both novel and insightful.

- A thorough numerical analysis of three gene regulatory networks exhibiting adaptation was performed. For each of the 425 topologies analyzed, approximately 2e5 circuits were sampled using Latin hypercube sampling, ensuring robust coverage of the parameter space. Among these, 1.5e5 circuits were identified as showing adaptation and subsequently subjected to further analysis, yielding approximately 350 parametric designs per topology for deeper investigation.

- The systematic approach and depth of the analysis position this study as a significant contribution to the understanding of gene regulatory networks and their response to growth feedback. The combination of detailed investigation, novel robustness metrics, and rigorous computational techniques enhances the impact of this work within the field.

Weaknesses

- The study focuses exclusively on a preselected set of 425 topologies previously shown to achieve adaptation, limiting the exploration of whether growth feedback could enable adaptation in circuits not inherently adaptive. While the authors have discussed and justified this choice, the focus restricts the generality of the conclusions, as the potential for growth feedback to induce adaptation in non-adaptive circuits remains unaddressed. The analysis includes scenarios where higher growth feedback restores adaptation in circuits that lose it at intermediate levels, but further elaboration on the implications for circuit design would strengthen the impact. The numerical framework and parameter choices align well with established methods, and an overview of the selected topologies has been provided. However, offering detailed information in supplementary materials or a public repository would further enhance the paper's accessibility and reproducibility.

- The model fails to capture the influence of protein levels on growth. To ensure accurate modeling of protein-level effects on growth, the b(t) term should be scaled appropriately, similar to Tan et al. Nature Chemical Biology 5:842-848 (2009).

- The authors propose bistability or multistability as the primary mechanisms behind different types of adaptation failure, explaining why the failures do not occur precisely at bifurcation points. They argue that their ODE simulations provide evidence for oscillation-related bifurcations, and an included appendix explores this phenomenon further, detailing how it can be observed in their results. While the authors choose not to apply semi-analytic methods, such as numerical continuation and eigenvalue analysis, to validate the existence of bifurcations, their approach offers valuable insights into the underlying dynamics of adaptation failures.

- The analysis in this work is carried out exclusively in a deterministic regime, as the focus is on scenarios where the effects of noise are assumed to be minimal. This approach is justified, and the authors acknowledge the complexity of extending their analysis to include stochasticity, which they suggest as an avenue for future research. The discussion has been expanded to address the potential impact of noise, its handling, and the assumptions underlying its exclusion. It is important to note, however, that noise can significantly alter system behavior-for instance, stabilizing trajectories and removing oscillations, as shown in prior studies (e.g., 10.1016/j.cels.2016.01.004). Additionally, variability in experimental implementations may influence the dynamics beyond what is predicted in deterministic models. These factors should be considered when interpreting the results.
