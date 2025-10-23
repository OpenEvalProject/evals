# Peer review - Round 1

Editors:
- Mariana Gómez-Schiavon, https://ror.org/01tmp8f25 Universidad Nacional Autónoma de México Mexico City Mexico

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.96421.3.sa0](https://doi.org/10.7554/eLife.96421.3.sa0)

This manuscript makes important contributions to our understanding of cell polarization dynamics by demonstrating how compensatory regulatory and spatial mechanisms enhance the robustness of polarization patterns. By integrating a computational pipeline with comparisons to experimental data, the authors provide convincing evidence that stability and asymmetry in reaction-diffusion networks are crucial for polarization in C. elegans zygotes. Their findings offer novel insights into essential biological processes such as cell migration, division, and symmetry breaking. Future theoretical and experimental work could refine the model by addressing its acknowledged limitations.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.96421.3.sa1](https://doi.org/10.7554/eLife.96421.3.sa1)

In this manuscript, the authors aim to evaluate the robustness of stable asymmetric polarization patterns by analyzing both a minimal 2-node network and a more biologically realistic 5-node network based on the C. elegans polarization system. They introduce a computational pipeline for systematically exploring reaction-diffusion network dynamics. Their study highlights the limitations of the widely used 2-node antagonistic network, demonstrating its susceptibility to simple modifications that disrupt polarization. However, they show that polarization stability can be restored by combining multiple regulatory mechanisms, and that spatially varying kinetic parameters can fine-tune the interface position. The authors further investigate the 5-node network of C. elegans, identifying key parameters that enhance its robustness against perturbations. Their findings provide novel insights into the mechanisms that ensure stable polarization in biological systems.

The major strengths of this work lie in its rigorous computational approach and the clarity of its findings. The authors demonstrate that the widely used 2-node antagonistic network is highly sensitive to parameter changes, requiring precise fine-tuning to maintain stable polarization. However, they show that stability can be restored through compensatory modifications, which expand the range of parameter sets supporting polarization. By further exploring spatial parameter variations, the authors reveal how compensatory adjustments can stabilize polarization patterns, offering insights into potential biological mechanisms regulating interface localization.

Extending their analysis to the C. elegans polarization network, the authors construct a 5-node model grounded in an extensive literature review. Their computational pipeline identifies key parameters that enhance robustness, and their model successfully replicates experimental observations, even in mutant conditions. Notably, among 34 possible network structures, only the naturally evolved 5-node network with mutual inhibition between specific components maintains stable polarization, highlighting its evolutionary optimization. This work significantly advances our understanding of polarization maintenance and provides a valuable framework for future in silico experiments.

Despite its strengths, the study has some limitations related to simplifying assumptions. The model neglects cortical flows and the role of actomyosin dynamics, which are known to be crucial during the establishment phase of polarization in the C. elegans zygote. While the authors focus on the maintenance phase, the absence of these biomechanical effects may limit the model's applicability to the full polarization process. Additionally, the assumption of infinitely fast cytoplasmic diffusion disregards potential effects of cytoplasmic flows on the stability of molecular distributions. Experimental measurements suggest that cytoplasmic diffusion coefficients are only an order of magnitude higher than membrane diffusion coefficients, meaning that finite diffusion combined with cytoplasmic flows could influence polarization stability. Although the authors acknowledge and discuss these limitations, incorporating these effects in future models could provide a more complete picture of the polarization dynamics in C. elegans embryos.
