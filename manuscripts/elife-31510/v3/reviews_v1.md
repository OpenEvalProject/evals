# Peer review - Round 1

Editors:
- Richard M Berry, University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.31510.032](https://doi.org/10.7554/eLife.31510.032)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Spatial structure of disordered proteins dictates conductance and selectivity in Nuclear Pore Complex mimics" for consideration by eLife. Your article has been favorably evaluated by Richard Aldrich (Senior Editor) and three reviewers, one of whom, Richard M Berry (Reviewer #1), is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal their identity: Jan T Liphardt (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors directly probe the transport of ions, and indirectly the transport of inert molecules and transport receptors through a pore in a membrane designed to mimic key aspects of the nuclear pore complex. Three types of pore-in-membrane configurations were explored: (i) un-derivatized (i.e., bare) (ii) derivatized with the WT FG domain of the nucleoporin Nsp1 (FG-nanopores), and (iii) derivatized with this same FG domain of Nsp1, wherein the hydrophobic residues F,I, L and V were replaced by S (SG-nanopores). The authors deduced that "FG-nanopores showed a clear selectivity as transport receptors can translocate across the pore whereas other proteins cannot. SG mutant pores lack such selectivity." They then present coarse-grained molecular dynamics simulations that they assert "reveal that FG-pores exhibit a high-density, nonuniform protein distribution, in contrast to a uniform and significantly less-dense protein distribution in the SG-mutant." They finally "conclude that the sequence-dependent density distribution of disordered proteins inside the NPC plays a key role for its conductivity and selective permeability."

Essential revisions:

1) Better evidence is required than is currently presented in the paper that the grafting densities are similar for Nsp1-FG versus Nsp1-SG. Without this assurance, the control represented by Nsp1-SG is not useful. The grafting experiments in guanidinium HCl do not convincingly demonstrate that the grafting densities of the Nsp1-FG and Nsp1-SG entities were similar.

Ideally a direct measure of these densities is needed since their physical properties, even in the presence of guanidium HCl, may be quite distinct and may yield different grafting densities. If this is not possible, further discussion and justification is required.

1b) The closest the manuscript comes to this is the coating density estimate in the pore, estimated from conductance blockade. However this is badly explained and therefore does not inspire confidence. Is it simply given by the simulated fit to conductivity data or are there independent measures? Subsection “Estimate of the surface grafting density of the FG-Nups based on conductance” states: "The average conductance blockade can be used to estimate the number of Nsp1 proteins that are blocking the ion flow through a nanopore of e.g. 48 nm where the conductance dropped from 70 nS to 12 nS. This yields an estimate of 107 for the number of Nsp1 proteins for this 48 nm pore." An explanation is needed of how this estimate is made. The implication seems to be that it is not via the MD simulations, which would make this a circular argument. It needs to be clear what model was used and what if any the free parameters were and how they were estimated. Or better still, provide an independent experimental measure.

2) The described transport experiments are performed with Kap95 and with tCherry separately rather than with them mixed together. Real transport works with both transport receptors and proteins that are not destined to be transported present at the same time. Indeed Lim and co-workers (PMID: 28864541) has again just shown how important Kap95 likely is for establishing the barrier function. This is an important factor not tested in the present mimics. Please state whether the authors attempted to make measurements on mixtures, and if not why not ? If so, can they differentiate Kap95 transit from tCherry transit in such mixtures by their very different transit times?

3) InFigure 5—figure supplement 2 and other measurements, state whether the multiple measurements were made on a single pore or on different pores, and report on the reproducibility of measurements made on separately fabricated pores with the same grafting material (e.g. FG domain of Nsp1)?

4) Please either present information on the transit event rate and behavior as a function of Kap95 and mCherry concentration in solution, or explain why there is none. Again, real transport in the NPC has been shown to involve the binding of many transport receptors to a single NPC at any one time, which makes this an important question.
