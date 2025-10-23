# Peer review - Round 1

Editors:
- Toby W Allen, RMIT University Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.96507.3.sa0](https://doi.org/10.7554/eLife.96507.3.sa0)

This study provides important insight into the mechanisms of proton-coupled oligopeptide transporters. It uses enhanced-sampling molecular dynamics (MD), backed by cell-based assays, revealing the importance of protonation of selected residues for PepT2 function. The simulation approaches are convincing, using long MD simulations, constant-pH MD and free energy calculations. Overall, the work has led to findings that will appeal to structural biologists, biochemists, and biophysicists studying membrane transporters.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.96507.3.sa1](https://doi.org/10.7554/eLife.96507.3.sa1)

The authors have performed all-atom MD simulations to study the working mechanism of hsPepT2. It is widely accepted that conformational transitions of proton-coupled oligopeptide transporters (POTs) are linked with gating hydrogen bonds and salt bridges involving protonatable residues, whose protonation triggers gate openings. Through unbiased MD simulations, the authors identified extra-cellular (H87 and D342) and intra-cellular (E53 and E622) triggers. The authors then validated these triggers using free energy calculations (FECs) and assessed the engagement of the substrate (Ala-Phe dipeptide). The linkage of substrate release with the protonation of the ExxER motif (E53 and E56) was confirmed using constant-pH molecular dynamics (CpHMD) simulations and cell-based transport assays. An alternating-access mechanism was proposed. The study was largely conducted properly, and the paper was well-organized. However, I have a couple of concerns for the authors to consider addressing.

(1) As a proton-coupled membrane protein, the conformational dynamics of hsPepT2 is closely coupled to protonation events of gating residues. Instead of using semi-reactive methods like CpHMD or reactive methods such as reactive MD, where the coupling is accounted for, the authors opted for extensive non-reactive regular MD simulations to explore this coupling. Note that I am not criticizing the choice of methods, and I think those regular MD simulations were well designed and conducted. But I do have two concerns.

(a) Ideally, proton-coupled conformational transitions should be modelled using a free energy landscape with two or more reaction coordinates (or CVs), with one describing the protonation event and the others describing the conformational transitions. The minimum free energy path then illustrates the reaction progress, such as OCC/H87D342- ↔ OCC/H87HD342H ↔ OF/H87HD342H as displayed in Figure 3. Without including the protonation as a CV, the authors tried to model the free energy changes from multiple FECs using different charge states of H87 and D342. This is a practical workaround, and the conclusion drawn (the OCC↔OF transition is downhill with protonated H87 and D342) seems valid. However, I don't think the OF states with different charge states (OF/H87D342-, OF/H87HD342-, OF/H87D342H, and OF/H87HD342H) are equally stable, as plotted in Figure 3b. The concern extends to other cases like Figures 4b, S7, S10, S12, S15, and S16. While it may be appropriate to match all four OF states in the free energy plot for comparison purposes, the authors should clarify this to ensure readers are not misled.

(b) Regarding the substrate impact, it appears that the authors assumed fixed protonation states. I am afraid this is not necessarily the case. Variations in PepT2 stoichiometry suggests that substrates likely participate in proton transport, like the Phe-Ala (2:1) and Phe-Gln (1:1) dipeptides mentioned in the introduction. And it is not rigorous to assume that the N- and C-termini of a peptide do not protonate/deprotonate when transported. I think the authors should explicitly state that the current work and the proposed mechanism (Figure 8) are based on the assumption that the substrates do not uptake/release proton(s).

(2) I have more serious concerns about the CpHMD employed in the study.

(a) The CpHMD in AMBER is not rigorous for membrane simulations. The underlying generalized Born model fails to consider the membrane environment when updating charge states. In other words, the CpHMD places a membrane protein in a water environment to judge if changes in charge states are energetically favorable. While this might not be a big issue for peripheral residues of membrane proteins, it is likely unphysical for internal residues like the ExxER motif. As I recall, the developers have never used the method to study membrane proteins themselves. The only CpHMD variant suitable for membrane proteins is the membrane-enabled hybrid-solvent CpHMD in CHARMM. While I do not expect the authors to redo their CpHMD simulations, I do hope the authors recognize the limitation of their method.

(b) It appears that the authors did not make the substrate (Ala-Phe dipeptide) protonatable in holo-simulations. This oversight prevents a complete representation of ligand-induced protonation events, particularly given that the substrate ion-pairs with hsPepT2 through its N- & C-termini. I believe it would be valuable for the authors to acknowledge this potential limitation.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.96507.3.sa2](https://doi.org/10.7554/eLife.96507.3.sa2)

Summary:

This is an interesting manuscript that describes a series of molecular dynamics studies on the peptide transporter PepT2 (SLC15A2). They examine, in particular, the effect on the transport cycle of protonation of various charged amino acids within the protein. They then validate their conclusions by mutating two of the residues that they predict to be critical for transport in cell-based transport assays. The study suggests a series of protonation steps that are necessary for transport to occur in Petp2. Comparison with bacterial proteins from the same family show that while the overall architecture of the proteins and likely mechanism are similar, the residues involved in the mechanism may differ.

Strengths:

This is an interesting and rigorous study that uses various state of the art molecular dynamics techniques to dissect the transport cycle of PepT2 with nearly 1ms of sampling. It gives insight into the transport mechanism, investigating how protonation of selected residues can alter the energetic barriers between various states of the transport cycle. The authors have, in general, been very careful in their interpretation of the data.

Weaknesses:

Interestingly, they suggest that there is an additional protonation event that may take place as the protein goes from occluded to inward-facing (clear from Figure 8) but as the authors comment they have not identified this residue(s).


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.96507.3.sa3](https://doi.org/10.7554/eLife.96507.3.sa3)

Summary:

Lichtinger et al. have used an extensive set of molecular dynamics (MD) simulations to study the conformational dynamics and transport cycle of an important member of the proton-coupled oligopeptide transporters (POTs), namely SLC15A2 or PepT2. This protein is one of the most well-studied mammalian POT transporters that provides a good model with enough insight and structural information to be studied computationally using advanced enhanced sampling methods employed in this work. The authors have used microsecond-level MD simulations, constant-PH MD, and alchemical binding free energy calculations along with cell-based transport assay measurements; however, the most important part of this work is the use of enhanced sampling techniques to study the conformational dynamics of PepT2 under different conditions.

The study attempts to identify links between conformational dynamics and chemical events such as proton binding, ligand-protein interactions, and intramolecular interactions. The ultimate goal is of course to understand the proton-coupled peptide and drug transport by PepT2 and homologous transporters in the solute carrier family.

Some of the key results include (1) Protonation of H87 and D342 initiate the occluded (Occ) to the outward-facing (OF) state transition; (2) In the OF state, through engaging R57, substrate entry increases the pKa value of E56 and thermodynamically facilitates the movement of protons further down; (3) E622 is not only essential for peptide recognition but also its protonation facilitates substrate release and contributes to the intracellular gate opening. In addition, cell-based transport assays show that mutation of residues such as H87 and

D342 significantly decrease transport activity as expected from simulations.

Strengths:

(1) This is an extensive MD based study of PepT2, which is beyond the typical MD studies both in terms of the sheer volume of simulations as well as the advanced methodology used. The authors have not limited themselves to one approach and have appropriately combined equilibrium MD with alchemical free energy calculations, constant-pH MD and geometry-based free energy calculations. Each of these 4 methods provides a unique insight regarding the transport mechanism of PepT2.

(2) The authors have not limited themselves to computational work and has performed experiments as well. The cell-based transport assays clearly establish the importance of the residues that have been identified as significant contributors to the transport mechanism using simulations.

(3) The conclusions made based on the simulations are mostly convincing and provide useful information regarding the proton pathway and the role of important residues in proton binding, protein-ligand interaction, and conformational changes.

Weaknesses:

There are inherent limitations with the methodology used such as the MEMENTO and constant pH MD that have been briefly noted in the manuscript.
