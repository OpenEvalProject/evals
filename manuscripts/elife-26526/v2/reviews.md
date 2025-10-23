# Peer review - Round 1

Editors:
- Gerhard Hummer, Max Planck Institute of Biophysics Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.26526.027](https://doi.org/10.7554/eLife.26526.027)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The Liquid Structure of Elastin" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Arup Chakraborty as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Robert Best (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The paper uses molecular simulations to study the properties of elastin. In extensive simulations of elastin fragments with a simple repeat sequence, the authors find that the peptides are disordered and self-associate to form a dense protein-rich phase. This appears to be the first study that uses all-atom simulations to tackle the formation of liquid-like protein aggregates. The results support many of the features of elastin determined experimentally such as formation of local turn structure, but do not support an overall ordered aggregate which had been proposed in the past. Instead, individual peptides are still able to diffuse, albeit slowly.

In their reports, the three reviewers raise a number of serious concerns. The main criticisms are that (1) the simulation systems are highly simplified and may not adequately capture all relevant properties of real elastin, (2) the significance of the results is not clear because important negative controls and reference simulations are missing, (3) possible force field issues are not assessed, and (4) the comparison to experiment is weak. A detailed list of the criticisms follows below. These points would have to be addressed in a revision.

Essential revisions:

1) The simulation systems are highly simplified and may not adequately capture all relevant properties of real elastin. Peptides with a simple repeat sequence (VPGVG)7 are studied. Whereas the pentapeptide and related polypentapeptides have been accepted as suitable mimics for the extensive hydrophobic regions of elastin, it is important to discuss the advantages and possible drawbacks and limitations stemming from the choice of sequence. Of particular concern is the fact that the native protein is largely characterized by alternating hydrophobic and crosslinking domains. Although the hydrophobic domains have sequences similar to the model of this study, they are usually flanked by crosslinking domains that have at least partial α-helical character. As such, it would appear rather unlikely that 27 hydrophobic domains in the native protein would form an aggregate like the one used here.

2) The significance of the results is not clear because important negative controls are missing. Wouldn't any concentrated solution of peptides with a roughly similar sequence composition behave in the same way, i.e., form a solvated blob? It would help to contrast the elastin results to simulations of IDP peptide fragments that do not aggregate and of IDPs that form "solid" aggregates in simulations using a similar protocol. In particular, is the extent of hydration in the core of the elastin bundle significantly higher than for other aggregating peptides? The authors mention silk and amyloid as two extremes of hydrated and solid aggregates. There are even reports in the literature that show a tendency to fibrillize (Fred W. Keeley, Catherine M. Bellingham and Kimberley A. Woodhouse, Philosophical Transactions: Biological Sciences, Vol. 357, No. 1418, Elastomeric Proteins: Structures, Biomechanical Properties and Biological Roles (Feb. 28, 2002), pp. 185- 189).

3) The choice of force field seems problematic, because it has been reported to favor overly compact structures in other systems. See e.g. Figure 1 in Piana et al., Curr. Opin. Struct. Biol. v24, p98, 2014, where the scaling of Rg with number of residues comes close to the one-third power, whereas most protein chains in water are closer to ideal chain scaling. Now elastin is quite hydrophobic, so it is possible that all is fine and it should be collapsed anyway, but it would be good to have some discussion of this issue and maybe a comparison with experiments which show that the elastin monomer behavior is reasonable.

4) The comparison to experiment is rather weak and qualitative at best, and therefore should be strengthened. For instance, can the simulations be related quantitatively to the neutron scattering experiments in Perticaroli et al., 2015? In light of the considerable force field issues in IDP simulations (well documented by work also of the authors!), it is very important to have experimental support. Comparisons to specific experiments should be performed in a way that could, at least in principle rule out, this and/or other models.
