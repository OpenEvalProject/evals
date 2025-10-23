# Peer review - Round 1

Editors:
- Arup K Chakraborty, Massachusetts Institute of Technology United States

Reviewers:
- Elena Papaleo, Danish Cancer Society Research Center Denmark

## Review text

DOI: [10.7554/eLife.48491.sa1](https://doi.org/10.7554/eLife.48491.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

In this paper, the authors provide a very nice description of how non-equilibrium effects can drive a particular biological phenomenon.

Decision letter after peer review:

Thank you for submitting your article "Efficient conversion of chemical energy into mechanical work by Hsp70 chaperones" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Arup Chakraborty as the Senior and Reviewing Editor. The following individual involved in review of your submission has agreed to reveal their identity: Elena Papaleo (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Your paper, which builds on a previous publication, provides new insights into a non-equilibrium biological problem, and also represents a nice use of MD calculations coupled to Jarzinsky's relation. There are two major comments that need to be addressed.

Essential revisions:

1) The kinetic rate model is very simple, however with many parameters. The innovation seems to be that you incorporate the free energies ∆∆G (calculated from MD) into the kinetic rate model, and obtain the probabilities of n. If we understood correctly, the end result that higher the concentration of ATP, higher the occupation number n seems simple enough, because you choose konATP≫konADP in the table of parameters, and therefore one should naturally expect it. So, it is unclear what is non-trivial in this interpretation given the choice konATP≫konADP.

2) The paper is not written very clearly, especially for a general biological audience, which constitutes the readership of eLife.

We have appended the two reviews below, so you can directly address other points that need to be addressed.

Reviewer #1:

The authors study the probability of binding of chaperones to protein substrates. The article utilizes (i) MD simulations towards calculating free energy differences (∆∆G) of incremental binding of chaperon complexes onto the substrate, (ii) uses a simple polymer model to predict the "free energy differences" (∆G), and (iii) implement a multi-parameter kinetic rate model to predict the probability of number of occupied chaperones as a function of ratio of ATP and ADP concentrations. These studies seem to be extensions of some of the authors' previous studies on chaperones, as they utilize some parameters from their earlier studies.

1) The article utilizes Jarzynski's equality for calculating the free energy differences. The free energy calculations are very expensive in nature due to the possibility of many conformations and number of states. The calculations appear fine. The agreement between polymer theory and the MD calculations is nice. The calculations by taking the stretched end state as a reference is clever. This work provides another example for the utility of non-equilibrium work calculations in obtaining the free energies for biological systems. I liked this aspect of the work.

2) Here is my main comment: The kinetic rate model is very simple, however with many parameters. The innovation seems to be that they incorporate the free energies ∆∆G (calculated from MD) into the kinetic rate model, and obtain the probabilities of n. If I did not misunderstand, the end result that higher the concentration of ATP, higher the occupation number n seems simple enough, because they choose konATP≫konADP in the table of parameters, and therefore one should naturally expect it. So, I would like to know what is non-trivial in this interpretation given the choice konATP≫konADP.

A far more interesting study would have been to understand the mechanisms that help us understand konATP≫konADP depending on the protein and chaperon configurations and allostery, but this is beyond the scope of the current article. So, the authors may take this as a suggestion for future works.

3) Also, the authors arguments on energy efficiencies in converting the chemical energy to mechanical energy are not motivated properly, as the choice for the definition of efficiency is not clear. Why is Equation 2 a good definition for efficiency? It’s just that the system is not in thermal equilibrium and because of the rates chosen, one will expect to see increased probabilities of occupation of chaperones with increased concentration ratio of ATP to ADP?

Decision: I am inclined to consider the article for publication in eLife when I see the response for point 2.

Reviewer #2:

The work by Barducci's group and collaborators illustrates an elegant computational study, validated against experimental data, to unveil thermodynamics and kinetic details of the mechanism of substrate expansion induced by the Hsp70 chaperone.

The work is technically sound and well designed, the agreement with the FRET data are encouraging in the direction that this kind of models can provide important insight into the mechanistic aspects of the process and the critical role played by ATP.

Despite the impressive work, the presentation of the data in the manuscript can be improved and guides the reader better in conveying some of the main messages. I thus encourage the authors to revise the writing and data presentation in figures and supplementary information carefully. Sometimes the writing sounds rather technical. A revision could be done to make it more accessible to a broader readership, especially more biology-oriented so that the outcome of this nice work can be better appreciated not only by specialists and does not risk to get lost.

Subsection “Structural and thermodynamic characterisation of chaperone-substrate complexes” – the authors say that they used a coarse-grained force field tailored to disordered proteins and it works appropriately for the unfolded state of the substrate of interest, but are they using the same model also for the chaperone protein? How did they ensure that this model is a good compromise to simulate at the same time the unfolded substrate and the folded chaperone? Could the authors discuss more in details about this?

Discussion – how much it is expected to be a specific mechanism for Hsp70 or could be common to other chaperones? Perhaps the authors could consider having a more general discussion and future perspective.

Another concern that I have is about data availability to reproduce the calculations/simulations and comparisons with experimental data. There are different options that the authors can consider and widely used by the molecular modeling and computational community. For example, they could use a GitHub repository to release the input files for the simulations, scripts to reproduce them, along with scripts to reproduce the analyses. GitHub, of course, has limitation to raw data if the authors want to make accessible the trajectories, they should probably look for repositories that provide more space than GitHub. Otherwise, they could add a statement in the manuscript that the trajectories will be available upon request, as it has been done in other similar publications. I believe that the input files and scripts would already be a significant advantage in the direction of accessibility and reproducibility.

The corresponding author is one of the members of the recently established PLUMED consortium, and I would encourage to deposit the input files also in the PLUMED-NEST repository.
