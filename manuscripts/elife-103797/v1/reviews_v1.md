# Peer review - Round 1

Editors:
- Martin Graña, https://ror.org/04dpm2z73 Institut Pasteur de Montevideo Uruguay

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.103797.3.sa0](https://doi.org/10.7554/eLife.103797.3.sa0)

The work presents a valuable extension of qFit-ligand, a computational method for modeling conformational heterogeneity of ligands in X-ray crystallography and cryo-EM density maps. The authors provide solid evidence of improved capabilities through careful validation against the previous version, particularly in expanding ligand sampling within conformational space. Such improvements suggest practical utility for challenging applications, including macrocyclic compound modeling and crystallographic drug fragment screening.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.103797.3.sa1](https://doi.org/10.7554/eLife.103797.3.sa1)

Summary:

Flowers et al describe an improved version of qFit-ligand, an extension of qFit. qFit and qFit-ligand seek to model conformational heterogeneity of proteins and ligands, respectively, cryo-EM and X-ray (electron) density maps using multiconformer models-essentially extensions of the traditional alternate conformer approach in which substantial parts of the protein or ligand are kept in place. By contrast, ensemble approaches represent conformational heterogeneity through a superposition of independent molecular conformations.

The authors provide a clear and systematic description of the improvements made to the code, most notably the implementation of a different conformer generator algorithm centered around RDKit. This approach yields modest improvements in the strain of the proposed conformers (meaning that more physically reasonable conformations are generated than with the "old" qFit-ligand) and real space correlation of the model with the experimental electron density maps, indicating that the generated conformers also better explain the experimental data then before. In addition, the authors expand the scope of ligands that can be treated, most notably allowing for multi conformer modeling of macrocyclic compounds.

Strengths:

The manuscript is well written, provides a thorough analysis, and represents a needed improvement of our collective ability to model small-molecule binding to macromolecules based on cryo-EM and X-ray crystallography, and can therefore has a positive impact on both drug discovery and general biological research.

Weaknesses:

Weaknesses were addressed during review. Overall, the demonstrated performance gains are modest.

Specific comments:

(1) The accuracy of initial placement may be critical. At the same time, in my experience ambiguous cases are quite common, for example with flat ligands with a few substituents sticking out or with ligands with highly mobile tails. There remain some questions regarding sensitivity to initial ligand placement, which individual users should check for.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.103797.3.sa2](https://doi.org/10.7554/eLife.103797.3.sa2)

Summary:

The manuscript by Flowers et al. aimed to enhance the accuracy of automated ligand model building by refining the qFit-ligand algorithm. Recognizing that ligands can exhibit conformational flexibility even when bound to receptors, the authors developed a bioinformatic pipeline to model alternate ligand conformations while improving fitting and more energetically favorable conformations.

Strengths:

The authors present a computational pipeline designed to automatically model and fit ligands into electron density maps, identifying potential alternative conformations within the structures.

Weaknesses:

Ligand modeling, particularly in cases of poorly defined electron density, remains a challenging task. The procedure presented in this manuscript exhibits limitations in low-resolution electron density maps (lower than 2.0 Å) and low-occupancy scenarios. Considering that the maps used to establish the operational bounds of qFit-ligand were synthetically generated, it's likely that the resolution cutoff will be even stricter when applied to real-world data.
