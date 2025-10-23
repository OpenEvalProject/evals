# Peer review - Round 1

Editors:
- Yibing Shan, DE Shaw Research , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.25850.018](https://doi.org/10.7554/eLife.25850.018)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: this article was originally rejected after discussions between the reviewers, but accepted after the authors appealed against the decision.]

Thank you for submitting your work entitled "Substrate transport and anion permeation proceed through distinct pathways in glutamate transporters" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors and the evaluation has been overseen by a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Christof Grewer (Reviewer #2).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

Using molecular dynamics simulations combined with biochemical and functional assays, this study explores the structure and mechanism of the chloride permeation channel of secondary-active glutamate transporters. While the findings are largely consistent with the earlier findings, they fall short of providing significant new insights. It appears that, in a close look, the identified transporter conformation and the channel for chloride permeation do not differ substantially from that identified and characterized by Machtens et al., 2015.

Reviewer #1:

Cheng et al. report an investigation of the mechanism by chloride ions permeate across secondary-active glutamate transporters, through passive diffusion. To this end, the authors combine molecular dynamics simulations and biochemical and functional studies. The former are primarily focused on GltPh, a prokaryotic transporter, while the experimental assays are carried out for human EAAT1, expressed in oocytes.

The most apparent shortcoming of this study is that it is unclear how it adds to the published body of work on this subject – particularly recent work, e.g. Machtens et al., 2015. The principal conclusion in that study is essentially the same as that proposed here, namely that an intermediate conformation between the OF and IF states is such that an anion-selective conducting pore opens up at the interface between the transport and trimerization domains; as far as I can discern by comparing the figures in these two articles, even the proposed pathway for chloride is highly similar.

It could be argued that independent verification of that result would be of interest. For example, a reader of Machtens et al. might be concerned by the fact that the conducting intermediates hypothesized that study originate from computer simulations in which the transporter is subject to transmembrane voltages of up 1.6 V. Thus, a re-evaluation of those results with more sophisticated or systematic approaches would be well justified. This is not the case here, however. The computational work in Cheng. et al. is of subpar quality, from a methodological standpoint, and appears to follow a design that is largely arbitrary. For example, the authors use so-called targeted MD simulations to generate conformational intermediates between the so-called iOFS and IF states. In this approach, the RMSD of the protein backbone structure, relative to a target, is gradually reduced to a value close to zero. This approach might seem reasonable, except these TMD trajectories are 10 ns long – i.e. clearly out of equilibrium. In that timescale, there simply is no chance that the side-chain structure, which is, after all, what controls the backbone conformation, will be minimally realistic. In my opinion, therefore, it is improbable that the resulting structural intermediates fall close to a minimum free-energy pathway between the two states considered – except in a purely qualitative sense. This issue aside, why exactly are the authors assuming here that the Cl- conducting state is an intermediate between iOF and IF conformations? As mentioned, the work seems to examine the same concepts put forward elsewhere. The authors should also clarify why they reportedly carry out 6 of these non-equilibrium trajectories, but apparently consider only one configuration of run #1 for further analysis. Why this precise configuration? What is the significance of these multiple calculations?

The subsequent steps of the computational protocol are equally confusing and seemingly ad hoc. Why are multiple simulations of the selected intermediate carried out with and without voltage applied? In which way does this procedure lead to the "refinement" of the structure of this intermediate? What is the metric that enables the authors to consider this structural intermediate is "refined"? And why, again, is the endpoint of only one of these multiple simulations considered for the analysis of ion permeation through PMF calculations? Are the authors using two different methods to compute these PMF profiles (Metadynamics and ABF), as the supplementary information seems to suggest? Why would that be necessary? What is the statistical error in the calculated PMF profiles? And importantly, what is the Cl- conductance associated with the calculated PMF profile, and does it resemble the experimental value? Finally, why are these PMF profiles (for Cl- and Na+) computed in the absence of one of the 3 Na+ ions bound to the structure?

I don't have major concerns in regard to the experimental data. However, I fail to recognize in which way this data specifically supports or confirms the computational work presented here, except on a very qualitative sense. As far as the question of Cl- channeling is concerned, the main experimental result is that MTS modifications of Cys substitutions at EAAT1 positions equivalent to Val51 and Leu212 GltPh reduce the rate of ion permeation, but not transport. The structure of GltPh shows these residues cluster together at the above mentioned interface, and clearly exposed to the solvent on the extracellular side. This data therefore helps to confirm the previously proposed notion that Cl- diffuses across this interface – it also confirms the data for V51 mutants in Machtens et al., 2015. What I fail to recognize is (a) what is distinct about the computational predictions put forward here, and (b) in which way the experimental data obtained in this study specifically validates those predictions.

Reviewer #2:

This is very nice and comprehensive work that reveals novel information on the mechanims of the anion conductance associated with glutamate transporters. The combination evidence from molecular dynamics simulations supported by experimental data is compelling. I have no general concerns, but would like to ask the authors to include citations of the work of Tao and Grewer regarding the location of the Na3 binding site, which is used in this manuscript for the MD simulations.

[Editors’ note: the author responses to the first round of peer review follow.]
