# Peer review - Round 1

Editors:
- Randy B Stockbridge, https://ror.org/00jmfr291 University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84805.sa0](https://doi.org/10.7554/eLife.84805.sa0)

This important work proposes a novel approach, based on co-evolution analysis, machine-learning protocols, and molecular dynamics simulations, to predict structures and energetics of the main states of the alternating access cycle of a family of membrane transporters, the sugar porters. The approach is compelling, especially the application of co-evolution and Alphafold to generate accurate models in different conformational states of a given protein, and will be of interest to the membrane transport and computational modeling communities.


---

# Peer review - Round 1

Editors:
- Randy B Stockbridge, https://ror.org/00jmfr291 University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84805.sa1](https://doi.org/10.7554/eLife.84805.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Reconstructing the transport cycle in the sugar porter superfamily using coevolution-powered machine learning" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Randy B Stockbridge as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Kenton Swartz as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Krishna D Reddy (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers were very positive about the approach, and thought this was a potentially very valuable contribution to the field. They were especially enthusiastic about the application of co-evolution and Alphafold to generate highly accurate models in different conformational states, and the reviewers appreciated the extensive amount of modeling work. However, the reviewers also thought that the first point listed here was a considerable issue that could undermine important conclusions and would need to be fixed.

1. The most critical issue is that the procedure to calculate the free energy profile in Figure 5D appears to be fundamentally flawed. A properly calculated one-dimensional (1D) free energy profile must reflect the probability distribution of a single, well-defined collective variable and cannot generally be derived by stitching together 1D profiles from different variables. As the free energy landscape is an essential part of the manuscript, this will need to be corrected with extra analysis, providing the necessary information has been stored in the trajectories (see Kumar et al. J Comp Chem, 1992).

In addition, the reviewers identified several other "essential revisions" that they believe can be addressed in a revision:

2. The authors should soften their claims that this method is superior to homology modeling (without having done a quantitative analysis) and that this method is an order of magnitude faster than comparable methods (which has not been shown, and might be difficult to demonstrate).

3. The free energy landscapes in Figure 5A and Figure 5B do not seem consistent with each other, and the authors do not discuss whether errors in the calculations that may contribute to this. Upon discussion, the reviewers thought this might be in part due to confusing labeling of the minima. In order to clarify this point, it would be useful for the authors to quantitatively assess the differences by showing the relative probability (or free energy difference) between outward-occluded and occluded states from each of the two landscapes.

4. The reviewers also noted that the free energy landscapes in the companion paper also (eLife-84808) appeared significantly different. For example, the occluded state is a barrier in Figure 2E of the other work while looks essentially the most stable state in Figure 5A of this work and is again a barrier in Figure 5B. Also, the inward open state seems unstable in Figure 2E of the other work while there is a clear stable minimum in Figure 5C of this work. The authors should justify/discuss this.

5. Simulations started from predicted models tend to drift away from the native structure in the multi microseconds time domain, unless restraints are applied. the authors should show compelling evidence that the predicted models used in the simulation are of sufficiently high quality (Proteins 2012; 80:2071-2079). Therefore, the authors should show evidence that the predicted models used in the simulation are of sufficiently high quality, especially if the backbone RMSD deviates over 1 Å from the experimental structure.

6. As the free energy calculations are based on simulations started from different structures it would be useful to show free energy estimates from these individual simulations.

7. Since the quality of co-evolution analysis is largely dependent on the quality of the BLAST and sequence alignment, more detail regarding the methodology (trimming, manual editing, program parameters, sequence exclusion, etc.) is important to include. The actual sequence alignment and the list of proteins as a supplement should also be provided.

8. It is hard to fully conceptualize the extent of structural differences with 2D representations of aligned structures. A per-residue RMSD of various structure comparisons, mapped onto the experimentally solved structure, would help further illustrate the specific structural similarities and differences between the models and structures. This type of figure would be more helpful than the current Figures 4B and 4C.

Reviewer #1 (Recommendations for the authors):

Can you expand on the thought on page 15/line 22 that "even the rocker-switch bundle movement might utilize asymmetric rearrangements." I don't understand what the expectation for symmetry is.

Reviewer #2 (Recommendations for the authors):

– As the authors mention, most people use homology models to model specific conformations. Though I agree that the presented analysis is likely superior to such techniques, it is essential to demonstrate this quantitatively, both before and after MD simulations. Given the improvements post MD simulation, it would be interesting to see if the superior starting point (biased AlphaFold2 models) leads to a more improved final model, or if MD simulations are sufficient to approach the free energy minimum. This would further demonstrate the necessity of the described methodology and argue for its wider adoption.

– Since the quality of co-evolution analysis is largely dependent on the quality of the BLAST and sequence alignment, I would like some more detail regarding the methodology (trimming, manual editing, program parameters, sequence exclusion, etc.). The actual sequence alignment and the list of proteins as a supplement should also be provided. I was unable to find this in the provided OSF link; therefore, as it stands, I am not able to assess this data.

– It is hard to fully conceptualize the extent of structural differences with 2D representations of aligned structures. A per-residue RMSD of various structure comparisons, mapped onto the experimentally solved structure, would help further illustrate the specific structural similarities and differences between the models and structures. This type of figure would be more helpful than the current Figures 4B and 4C, as the improvements are hard to get a sense of as currently presented. Furthermore, this would answer the related question regarding if MD simulations improve RosettaMP models in specific ways, or is it a more global improvement.

– The proposed model of proton-coupling suggests conformation-specific pKa's of the aspartate residue, so that the transporter can bind protons in the outward-facing state, yet release protons in the inward-facing state. If this is the case, the co-evolution analysis should reveal residues adjacent (or perhaps even more allosteric) to the aspartate that could regulate the pKa in a conformation-dependent manner. This would be interesting to describe.

Reviewer #3 (Recommendations for the authors):

A critical issue of this work is that the procedure to calculate the free energy profile in Figure 5D is fundamentally flawed. A properly calculated one-dimensional (1D) free energy profile must reflect the probability distribution of a single, well-defined collective variable and cannot generally be derived by stitching together 1D profiles from different variables. Namely the orthogonal space of one variable, is generally not the same of that of another variable (and there are overlap regions between different variables). To do this correctly the authors should first define a single, mathematically well-defined variable describing the gradual structural variation from outward-open to inward-open conformations. A possibility for example is to use a path variable (J Chem Phys 2007 Feb 7;126(5):054103) derived from consecutive configurations from the three different paths. The authors could then use a reweighting approach to properly calculate the free energy along this path from the sampling of all simulations. To do this rigorously, the authors could use the weighted histogram analysis or the multistate Bennett acceptance ratio method, so that biases on different variables and overlap regions are properly accounted for.

The free energy landscapes in Figure 5A and Figure 5B do not seem consistent with each other. Namely while the occluded state is a main free energy minimum in the landscape of Figure 5A, it seems to be a barrier region in Figure 5B. To quantitatively assess this, it would be useful that the authors show the relative probability (or free energy difference) between outward-occluded and occluded states from each of the two landscapes. To do this the authors could define a unique descriptor to discriminate outward-occluded and occluded states (using the same descriptor for each landscape) and evaluate their probability. A simple way to do this, assuming the overall bias potential is only a function of CV1 and CV2, is to calculate the cumulative weight of each state. Where the weight of a simulation frame can be calculated as exp{-F(i)/kT}/N(i), where F(i) is the free energy as a function of CV1 and CV2 in a small bin of those variables assigned to that frame and N(i) is the number of simulation frames in that bin. This simple scheme could be also used to project the 2D landscape on a single variable, but weighted histogram analysis or the multistate Bennett acceptance are generally more rigorous methods in this regard.

As the free energy calculations are based on simulations (walkers) started from different (endpoints) structures it would be useful to show free energy estimates from these individual simulations. If this is not possible because they cover different portions of the space, the authors should show a metric of overlap, to make sure that individual simulations do not explore completely separated regions of the configurational space, thus leading to unreliable free energies.

Based also on the previous considerations, there is no evidence that the methodology proposed leads to one order of magnitude speed up compared to other methods and it would be generally difficult to demonstrate for these types of systems.

Another important point is that the simulations are based on the predicted models rather than on experimental structures. Previous systematic studies (see for example Proteins 2012; 80:2071-2079) underline how simulations started from predicted models tend to drift away from the native structure in the multi microseconds time domain, unless restraints are applied, which could help structural improvements (see also Protein Science 2015 25:19-29). Therefore, the authors should show compelling evidence that the predicted models used in the simulation are of sufficiently high quality, especially if the backbone RMSD deviates over 1 Å from the experimental structure. For example, by showing that convectional MD simulations started either from the models or from the X-ray structures are both stable and sample similar conformations (e.g. based on pairwise RMSD of both side chains and backbone).

The results of the modeling part of the work seem encouraging, nonetheless a suggestion for the authors is that, besides the RMSD distribution in Figure 4A they show analogous data for a descriptor that can better differentiate structural differences between states, as for example based on state-specific contacts. In particular, is not uncommon that the backbone RMSD between different states of a transporter is 3 Å or smaller.
