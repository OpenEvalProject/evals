# Peer review - Round 1

Editors:
- Marcel P Goldschen-Ohm, https://ror.org/00hj54h04 University of Texas at Austin United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.92418.4.sa0](https://doi.org/10.7554/eLife.92418.4.sa0)

This useful work provides insight into agonist binding to nicotinic acetylcholine receptors, which is the stimulus for channel activation that regulates muscle contraction at the neuromuscular junction. The authors use in silico methods to explore the transient conformational change from a low to high affinity agonist-bound conformation as occurs during channel opening, but for which structural information is lacking owing to its transient nature. The simulations indicating that ligands flip ~180 degrees in the binding site as it transitions from a low to high affinity bound conformation are solid. A limitation is the approximation of binding energies using Poisson-Boltzmann Surface Area and mismatch between calculated and experimental binding energies for two of the four ligands tested. Nonetheless, this work presents an intriguing picture for the nature of a transient conformational change at the agonist binding site correlated with channel opening.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.92418.4.sa1](https://doi.org/10.7554/eLife.92418.4.sa1)

Summary:

The authors want to understand fundamental steps in ligand binding to muscle nicotinic receptors using computational methods. Overall, although the work provides new information and support for existing models of ligand activation of this receptor type, some limitations in the methods and approach mean that the findings are not as conclusive as hoped.

Strengths:

The strengths include the number of ligands tried, and the comparison to the existing mature analysis of receptor function from the senior author's lab.

Weaknesses:

The weakness are the brevity of the simulations, the concomitant lack of scope of the simulations, the lack of depth in the analysis and the incomplete relation to other relevant work. The free energy methods used seem to lack accuracy - they are only correct for 2 out of 4 ligands.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.92418.4.sa2](https://doi.org/10.7554/eLife.92418.4.sa2)

Summary:

The aim of this manuscript is to use molecular dynamics (MD) simulations to describe the conformational changes of the neurotransmitter binding site of a nicotinic receptor. The study uses a simplified model including the alpha-delta subunit interface of the extracellular domain of the channel and describes the binding of four agonists to observe conformational changes during the weak to strong affinity transition.

Strength:

The 200 ns-long simulations of this model suggest that the agonist rotates about its centre in a 'flip' motion, while loop C 'flops' to restructure the site. The changes appear to be reproduced across simulations and different ligands and are thus a strong point of the study.

Weaknesses:

After carrying out all-atom molecular dynamics, the authors revert to a model of binding using continuum Poisson-Boltzmann, surface area and vibrational entropy. The motivations for and limitations associated with this approximate model for the thermodynamics of binding, rather than using modern atomistic MD free energy methods (that would fully incorporate configurational sampling of the protein, ligand and solvent) could be provided. Despite this, the authors report correlation between their free energy estimates and those inferred from the experiment. This did, however, reveal shortcomings for two of the agonists. The authors mention their trouble getting correlation to experiment for Ebt and Ebx and refer to up to 130% errors in free energy. But this is far worse than a simple proportional error, because -24 Vs -10 kcal/mol is a massive overestimation of free energy, as would be evident if it the authors were to instead to express results in terms of KD values (which would have error exceeding a billion fold). The MD analysis could be improved with better measures of convergence, as well as a more careful discussion of free energy maps as function of identified principal components, as described below. Overall, however, the study has provided useful observations and interpretations of agonist binding that will help understand pentameric ligand-gated ion channel activation.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.92418.4.sa3](https://doi.org/10.7554/eLife.92418.4.sa3)

Summary:

The authors use docking and molecular dynamics (MD) simulations to investigate transient conformations that are otherwise difficult to resolve experimentally. The docking and simulations suggest an interesting series of events whereby agonists initially bind to the low affinity site and then flip 180 degrees as the site contracts to its high affinity conformation. This work will be of interest to the ion channel community and to biophysical studies of pentameric ligand-gated channels.

Strengths:

I find the premise for the simulations to be good, starting with an antagonist bound structure as an estimate of the low affinity binding site conformation, then docking agonists into the site and using MD to allow the site to relax to a higher affinity conformation that is similar to structures in complex with agonists. The predictions are interesting and provide a view into what a transient conformation that is difficult to observe experimentally might be like.

Weaknesses:

A weakness is that the relevance of the initial docked low affinity orientations depend solely on in silco results, for which simulated vs experimental binding energies deviate substantially for two of the four ligands tested. This raises some doubt as to the validity of the simulations. I acknowledge that the calculated binding energies for two of the ligands were closer to experiment, and simulated efficiencies were a good representation of experimental measures, which gives some support to the relevance of the in silico observations. Regardless, some of the reviewers comments regarding the simulation methodology were not seriously addressed.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.92418.4.sa4](https://doi.org/10.7554/eLife.92418.4.sa4)

Summary:

In their revised manuscript "Conformational dynamics of a nicotinic receptor neurotransmitter binding site," Singh and colleagues present molecular docking and dynamics simulations to explore the initial conformational changes associated with agonist binding in the muscle nicotinic acetylcholine receptor, in context with the extensive experimental literature on this system. Their central findings are of a consistently preferred pose for agonists upon initial association with a resting channel, followed by a dramatic rotation of the ligand and contraction of a critical loop over the binding site. Principal component analysis also suggests the formation of an intermediate complex, not yet captured in structural studies. Binding free energy estimates are consistent with the evolution of a higher-affinity complex following agonist binding, with a ligand efficiency notably similar to experimental values. Snapshot comparisons provide a structural rationale for these changes on the basis of pocket volume, hydration, and rearrangement of key residues at the subunit interface.

Strengths:

Docking results are clearly presented and remarkably consistent. Simulations are produced in triplicate with each of four different agonists, providing an informative basis for internal validation. They identify an intriguing transition in ligand pose, not well documented in experimental structures, and potentially applicable to mechanistic or even pharmacological modeling of this and related receptor systems. The paper seems a notable example of integrating quantitative structure-function analysis with systematic computational modeling and simulations, likely applicable to the wider journal audience.

Weaknesses:

The response to the initial review is somewhat disappointing, declining in some places to implement suggested clarifications, and propagating apparent errors in at least one table (Fig 2-source data 1). Some legends (e.g. Fig 2-supplement 4, Fig 3, Fig 4) and figure shadings (e.g. Fig 2-supplement 2, Fig 6-supplement 2) remain unclear. Apparent convergence of agonist-docked simulations towards a desensitized state (l 184) is difficult to interpret in absence of comparative values with other states, systems, etc. In more general concerns, aside from the limited timescales (200 ns) that do not capture global rearrangements, it is not obvious that landscapes constructed on two principal components to identify endpoint and intermediate states (Fig 3) are highly robust or reproducible, nor whether they relate consistently to experimental structures.
