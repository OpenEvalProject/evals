# Peer review - Round 1

Editors:
- Arvind Murugan, University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.107524.3.sa0](https://doi.org/10.7554/eLife.107524.3.sa0)

This study presents a valuable finding about how receptor–ligand binding pathways with multi-site phosphorylation can show non-monotonic responses to increasing ligand affinity and to kinase activity. The authors provide compelling evidence through a simple ordinary differential equation model of such signaling networks with the key new ingredient of ligand-induced receptor degradation. The work will be of interest to physicists and biologists working on signal transduction and biological information processing.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.107524.3.sa1](https://doi.org/10.7554/eLife.107524.3.sa1)

Summary:

The authors study the steady-state solutions of ODE models for molecular signaling involving ligand binding coupled to multi-site phosphorylation at saturating ligand concentrations. Although the results are in principle general, the work highlights the receptor tyrosine kinases (RTK) as model systems. After presenting previous ODE model solutions, the authors present their own "kinetic sorting" model, which is distinguished by ligand-induced phosphorylation-dependent receptor degradation and the property that every phosphorylation state is signaling competent. The authors show that this model recovers the two types of non-monotonicity experimentally reported for RTKs: maximum activity for intermediate ligand affinity and maximum activity for intermediate kinase activity.

The main contribution of the work is in demonstrating that their model can capture both types of non-monotonicity, whereas previous models could at most capture non-monotonicity of ligand binding.

Strengths:

The question of how energy dissipating, and thus non-equilibrium, molecular systems can achieve steady-state solutions not accessible to equilibrium systems is of fundamental importance in biomolecular information processing and self-organization. Although the authors do not address the energy requirements of their non-equilibrium model, their comparative analysis of different alternative non-equilibrium models provides insight into the design choices necessary to achieve non-monotonic control, a property that is inaccessible at equilibrium.

The paper is succinctly written and easy to follow, and the authors achieve their aims by providing convincing numerical solutions demonstrating non-monotonicity over the range of parameter values encompassing the biologically relevant regime.

Weaknesses:

(1) A key motivating framework for this work is the argument that the ability to tune to recognize intermediate ligand affinities provides a control knob for signal selection that is available to non-equilibrium systems. As such, this seems like a compelling type of ligand selectivity, which is a question of broad interest. However, as the authors note in the results, the previously published "limited signaling model" already achieves such non-monotonicity to ligand binding affinity. The introduction and abstract do not clearly delineate the new contributions of the model.

The novel benefit of the model introduced by the authors is that it also achieves non-monotonic response to kinase activity. Because such non-monotonicity is observed for RTK, this would make the authors' model a better fit for capturing RTK behavior. However, the broad significance of achieving non-monotonicity to kinase activity is not motivated or supported by empirical evidence in the paper. As such, the conceptual significance of the modified model presented by the authors is not clear.

UPDATE: The authors have now clarified the significance of the model in elucidating how known motifs (multisite phosphorylation and active receptor degradation) could explain the behavior, including non-monotonicity. The authors have also provided compelling arguments for the biological significance of achieving non-monotonic kinase activity response.

(2) Whereas previous models used in the literature are schematized in Figure 1, the model proposed by the author is missing (See line 97 of page 3). Without the schematic, the text description of the model is incomplete.

UPDATE: this issue has been resolved.

(3) The authors use the activity of the first phosphorylation site as the default measure of activity. This choice needs to be justified. Why not use the sum of the activities at all sites?

UPDATE: This was a non-issue. The potential misunderstanding has been mitigated by clarifications in the text.

Comments on revisions:

All issues previously identified were convincingly addressed. I have no additional suggestions.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.107524.3.sa2](https://doi.org/10.7554/eLife.107524.3.sa2)

Summary:

In classical models of signaling network, the signaling activity increases monotonically with the ligand affinity. However, certain receptors prefer ligands of intermediate affinity. In the paper, the authors present a new minimal model to derive generic conditions for ligand specificity. In brief, this requires multi-site phosphorylation and that high-aﬃnity complexes be more prone to degrade. This particular type of kinetic discrimination allows to overcome equilibrium constraints.

Strengths:

The model is simple, and it adds only a few parameters to classical generic models. They moreover vary these additional parameters in ranges based on experimental observations. They explain how the introduction of these new parameters is essential to ligand specificity. Their model quantitatively reproduces the ligand specificity of a certain receptor. They finally provide testable prediction.

Weaknesses:

The naming of multiple variables as activity without precise definitions may be confusing to readers.

Comments on revisions:

I thank the authors for addressing my comments. One point remains regarding the naming of multiple variables as activity. Besides using other words, the authors may consider giving precise definitions of terms, e.g. by writing "We define kinase activity as the phosphorylation rate $\omega=k_p\tau$." A connection that appears only at line 204 in the present manuscript.
