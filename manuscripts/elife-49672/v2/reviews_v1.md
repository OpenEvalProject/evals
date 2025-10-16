# Peer review - Round 1

Editors:
- László Csanády, Semmelweis University Hungary

Reviewers:
- László Csanády, Semmelweis University Hungary
- John Bankston, University of Colorado Anschutz Medical Campus
- Marcel P Goldschen-Ohm, University of Texas at Austin United States

## Review text

DOI: [10.7554/eLife.49672.sa1](https://doi.org/10.7554/eLife.49672.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

In this paper Porro and colleagues address the molecular mechanism by which binding of cAMP modulates the voltage sensitivity of hyperpolarization-activated cyclic nucleotide-gated (HCN) channels. They examine the role of the N-terminal HCN domain (HCND), which was identified in recent cryo-EM structures as a structural segment wedged in between the channel's voltage sensor domain (VSD) and its C-terminal cytosolic domains (C-linker ring and cyclic nucleotide-binding domain (CNBD)). The authors find that perturbing hydrophobic interactions between the HCND and the VSD impairs correct folding and trafficking. Moreover, disrupting interactions either between HCND and VSD or between HCND and C-linker ring abolishes the stimulatory effect of cAMP on channel activation. These observations identically apply to three different HCN isoforms, human HCN1, mouse HCN2, and rabbit HCN4. The authors conclude that the HCND serves to transmit the conformational change induced by cAMP binding to the transmembrane VSD. These findings provide a mechanistic explanation for the link between voltage- and cAMP-induced activation, which is an important step forward in understanding structure-function relationships of HCN channels.

Decision letter after peer review:

Thank you for submitting your article "The HCN domain couples voltage gating and cAMP response in Hyperpolarization-activated cyclic nucleotide-gated channels" for consideration by eLife. Your article has been reviewed by three peer reviewers, including László Csanády as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Olga Boudker as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: John Bankston (Reviewer #2); Marcel P. Goldschen-Ohm (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

All three reviewers have found the work interesting and the data of high quality, but some concerns were raised which will need to be addressed before publication. Specifically, interpretation of single-mutant data in terms of disruption of one specific interaction needs further experimental support (see sections 1 and 2) below).

Essential revisions:

1) In the HCN2 background, the authors pinpoint interacting residue pairs I176-L250 and F151-Y180, R154-E478, and M155-K464. For each of the above four pairs the authors mutate only one of the two involved side chains, and interpret the resulting phenotypes to reflect the consequence of loss of interaction between the target pair. While this interpretation might be correct, interpreting the effect of a single mutation in terms of loss of a specific interaction is questionable. The conclusions would be strengthened by performing conventional mutant cycles, i.e., by mutating both interacting residues individually and in combination. Non-additivity of mutation-induced functional effects in the double mutant would support (and energetically quantify) the functional relevance of the proposed interaction.

E.g., in addition to the already characterized WT and E478A constructs, the authors should also characterize R154A and R154A/E478A. These four constructs form a thermodynamic mutant cycle. The free energy difference between the open and the closed state at zero mV (deltaGo-c) can be expressed as deltaGo-c = -z*F*V1/2 (or deltaGo-c = -(R*T/k)*V1/2, using the authors' terminology). Energetic effects of the two single mutations and of the double mutation should be quantitated as deltadeltaGo-c = -(R*T/k)*deltaV1/2. Non-additive effects of the two mutations in the double mutant would support the authors' hypothesis and at the same time quantify the energetic contribution of the R154-E478 salt bridge to the stabilization of the open state. Alternatively, a charge-swap between positions 154 and 478 (R154E, E478R, R154E/E478R) could be attempted, but this would require characterizing three novel constructs. We leave it to the authors' discretion to try one of those approaches.

2) F151E was the only mutation shown to alter cAMP regulation of V1/2 at the HCND-VSD interface. To support the idea that this results from a charged substitution perturbing a hydrophobic pocket, the authors should test whether other charged substitutions (D,K,R) have a similar effect.

3) Most of the mutations in the first interaction site (Figure 2) result in channels that don't make it to the membrane, however, the I176A and L250A mutants both do something interesting to gating. Is the voltage dependence of these channels lost or just shifted? What do the IVs look like? Did you try to hold more depolarized to close the channels?

4) In the second hydrophobic interaction site (Figure 3, Figure 4), you use MD to look at how the local structure changes when the central PHE is mutated and show a disruption of the structure. This is reported as a change in distance between the mutated residue and a nearby TYR. Some clarification about the relationship between the simulation and the data are needed. The three largest changes in the simulation are caused by the mutations to VAL, ALA, and GLU which all perturb the measured distance by the same amount. However, the functional data reports a dramatically different voltage dependence between these three mutants and in the last case no sensitivity to cAMP. It is unclear how the MD simulation relates and enhances these data.

5) In a number of places in the hydrophobic site (I134A versus I176A or F109 versus F151) there is a substantial difference between your results in HCN1 versus HCN2, whereas the C-linker HCND interaction results are quite consistent. Some comment on the ubiquity of this mechanism in the HCN family might be warranted.

6) A little more discussion of linear response theory and what the modeling can tell you and its limitations might be helpful. We are unfamiliar with this approach and a broad audience might be as well. If you break the putative bonds/salt bridges does the model tell you that the force is not transmitted as well?
