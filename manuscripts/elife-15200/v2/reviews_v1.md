# Peer review - Round 1

Editors:
- Johannes Krause, University of Tübingen , Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.15200.022](https://doi.org/10.7554/eLife.15200.022)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Rewiring MAP kinases in Saccharomyces cerevisiae to regulate novel targets through ubiquitination" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Ivan Dikic as the Senior and Reviewing Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The ability to rationally engineer post-translational circuits utilizing processes like phosphorylation and ubiquitylation is critical for expanding synthetic biology beyond transcriptional circuitry. Here, the authors developed a new technique based on target phosphorylation motifs and protein interaction domains to engineer post-translational interactions between MAPK kinases and protein substrates. Using engineered pathways in yeast where a MAP kinase (Fus3 or Erk2) is targeted to artificial substrate protein through fusion of both the kinase and substrate to compatible interaction domains, they determine that this mode of interaction and the presence of the cognate phosphorylation motif (in this case a phosphodegron) is sufficient to confer MAPK regulation of the substrate (in this case leading to degradation). They used this technique to control ubiquitin-dependent degradation of fluorescent reporters (such as YFP) and to rewire signaling circuits in yeast both transcriptionally and post-translationally. The key findings include: 1) substrate phosphorylation by a MAPK kinase can be engineered in a highly modular fashion by combining two distinct modules (protein-protein interaction and phosphorylation motif); 2) the engineered phosphorylation can enable new signaling capabilities through feedback/feedforward loops. The technique is novel and is useful for dissecting natural signaling pathways as well as for synthesizing new signaling behaviors. In particular, it represents an exciting example of engineering a fully post-translational feedback loop in a signaling system, which makes this a major step forward from a synthetic biology point of view. The manuscript could be strengthened by consideration (and integration) of known mechanisms for docking interactions involving Fus3, and their role in regulating signal output (Remenyi et al. Mol Cell 2005).

Essential revisions:

1) Protein-protein interaction domains. The paper focused on exploring both natural and synthetic interaction domains, including PDZ, SH3, SYNZIP. In their approach, two interaction domains are fused separately to the MAPK kinase and the non-native protein substrate. Thus, both proteins need to be engineered to enable the phosphorylation interaction. In contrast to this approach (and as the authors citied), an alternative approach is to only engineer the protein substrate by utilizing native docking interactions between MAPK kinase and its substrate. Regot et al. and Durandau et al. used this alternative strategy to control fluorescent reporter localization. Can the authors comment on the relative capabilities of these different design strategies?

2) Related to point 1. In the current design, the ligand is fused to the kinase and the corresponding binding domain is fused to the substrate. What if the locations of the two domains are swapped? If the response is not sensitive to where the domain is fused, then it will provide stronger support to the claim that the design is highly modular. If the authors have data on this already, it would be helpful to report it because, even if the result is negative, it would be useful for other researchers seeking to design similar systems.

3) Additional controls, some biochemical in nature, should be provided to confirm that regulation is via the proposed mechanism. Kinase dead Fus3 should be included in certain key experiments (e.g. Figure 1) to confirm that phosphorylation of the substrate is actually mediated by the Fus3 kinase fusion. The authors should also confirm that degradation of the YFP-degron construct is mediated via the SCF complex and ubiquitin-mediated proteasomal degradation. The experiments describing implementation of negative feedback and feedforward topologies require the inclusion of dynamic, time-course data. Temporal regulation of signal output could be markedly different when MAPK is targeted to phosphorylate alternative network components.

4) Scalability of the design. In Figure 2D-E, the authors used different interaction domains to control the phosphorylation of two different substrates by Fus3. However, the response of the YFP substrate is much weaker than that of the mCherry substrate. First, what about the response in individual cells? Is the response of YFP always weaker than mCherry in all individual cells, or only in subpopulations? Second, is this due to the saturation of the system? If so, it would be helpful to identify the source of limitation that can be improved in the future.
