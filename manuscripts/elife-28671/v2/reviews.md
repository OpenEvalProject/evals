# Peer review - Round 1

Editors:
- Nir Ben-Tal, Tel Aviv University Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.28671.034](https://doi.org/10.7554/eLife.28671.034)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Lipids and ions traverse the membrane by the same physical pathway in the nhTMEM16 scramblase" for consideration by eLife. Your article has been favorably evaluated by Gary Westbrook (Senior Editor) and three reviewers, one of whom, Nir Ben-Tal (Reviewer #1), is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal their identity: Raimund Dutzler (Reviewer #2). The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Based on our discussion of your manuscript we agree that the study provides an interesting molecular perspective of the mechanisms of lipid and ion transport in the TMEM16 family. While there have been both experimental and simulation studies performed on this system before, the combined approach is a strong point of the work. The manuscript provides a detailed and stimulating view on different aspects of the function and regulation of a Ca2+-activated lipid scramblase. In general, we feel that it captured the essence of how a lipid scramblase catalyzes the bidirectional diffusion of lipids between both leaflets of the bilayer. Other proposals made in the manuscript, such as the activation of the protein by Ca2+, the permeation of ions and the conversion of the channel TMEM16A into a scramblase by point mutations are at this stage speculative, but they put forward testable hypotheses that will stimulate further studies. However, there are also a number of potential pitfalls both with simulations and experiments (not to mention models) that we feel should be addressed better.

We do not think that new simulations or experiments are necessary, but the reviewers and editors would like to see a much more critical distinction between solid and speculative aspects taking potential ambiguities in the results into account, as well as addressing the issues below e.g. with new analysis of existing data.

Essential revisions:

General:

The manuscript is rather long and a bit tedious to read. Please edit to make more concise so it is easier to read for non nhTMEM16 scramblase fascinados.

The results on point mutants of TMEM16A that confer scrambling activity to the protein and that changes the apparent selectivity of currents over time from anion selective to non-selective is puzzling, particularly in light of a recent structural investigation that showed a different organization of the ion conduction path compared to scramblases. Please address this in the Discussion.

The region the authors refer to as aqueduct is equivalent to the region that in the manuscript describing the structure was termed 'subunit cavity'. Please clarify in the manuscript.

MD simulations:

Some of the MD simulations rely on very limited data (sometimes only single events) from statistical mechanics, and as the authors cite this system has previously been studied with simulations by other groups. The authors should clearly stress where they agree with previous simulations, what results are new/different, and analyze/comment on the statistical certainty of new results. In light of the high complexity of the system and the extended length of trajectories, it would also be interesting for the reader to know more about the convergence of the system during the simulation and the structural relationships between the observed conformations in the simulated systems compared to the initial crystal structure. This might be particularly relevant for simulations with applied external potential.

When combined with experimental data, an obvious critical test is to perform additional simulations that include the mutations identified to switch the activity on/off, and show that they have the expected effects. Although we do not require the authors to perform such additional studies, it would be valuable to outline specific predictions about other experimental/simulation results that are expected if this model is correct. Is it possible to confirm other data (such as ion conductance) with experimental results, e.g., by extrapolating the applied voltages to physiologically relevant potentials?

Although it is common to use higher potentials in simulations, the authors should justify their choice of going up to 500mV, explain to the reader that it is significantly higher than physiological potentials. Are there other potential problems than distortion of the structure?

The flipping rates observed in the simulations appear to be orders of magnitude higher than the experiments by Malvezzi et al. [Nat Commun 4, 2367] that suggests rates of ~10,000 lipids per minute. This casts some doubt on the qualitative accuracy of simulations; The authors should explain or acknowledge this discrepancy. Are there other features where the simulations are in better quantitative agreement with experimental kinetics?

Although phospholipids are the most important substrates, there are indications e.g. ceramides (without the phosphate group) can be flipped by these proteins [Suzuki et al., J Biol Chem 288, 13305]. Given that the model reported here appears to rely heavily on electrostatic interactions, how would it explain the activity for these other types of lipids?

One of the main arguments of the work is that the ion conductance pathway should be identical to the scramblase pathway. However, at least for TMEM16A there is now a recent (low-resolution) structure available [Paulino, eLife 2017;6:e26232] where the structure is found to be rearranged compared to nhTMEM16, which creates a mostly occluded ion permeation pathway. There is no question the authors' V543S mutant is interesting, but given the complex interplay with changes in ion selectivity after phospholipid scrambling is initiated, would this not rather suggest potential structural transitions that open/close the ion pore vs. creating the surface necessary for scrambling? Obviously, this structure was not available when the authors performed their work, but even with limited resolution it appears to be in partial conflict with the present statement that there is no difference in ion permeation pathways from that taken by phospholipids. For the readers' sake, the model should be compared to these results and the differences discussed.

What is the connection between the absence of bound Ca2+ and the conformational change closing the lipid pathway?

Why did the authors observe permeation of Na+ but not Cl- ions? This is in conflict with the poor current selectivity observed in experiment.

Cellular assays:

It would be interesting to learn more about the technical limitations of the cellular assay used in this study. The authors apply Ca2+ present in their patch pipette to the cytoplasm after establishing a whole-cell patch. It is expected that the equilibration of the Ca2+ concentration with cytosol would proceed within a minute. The cellular response indicating lipid scrambling was obtained after 6 minutes and the measurement lasted 14 minutes. It would be interesting to learn more about any non-specific cellular response to high (200 µM) Ca2+ from mock-transfected cells. How long would it take before cellular artifacts become apparent and how would these look like with respect to AnnexinV-binding and patch-clamp experiments.

The accumulation of phosphatidyl-serine on the outside of the plasma membrane, which is a prerequisite for the detection by AnnexinV, takes time, but what is the underlying cause for the delay in the activation of currents? The anticipation is instantaneous activation of the scramblase, and currents.

Have the authors considered an increase of the intracellular Ca2+ concentration by Ca2+ ionophores instead of a patch pipette? If so, did these experiments show a similar result with respect to scrambling?

Why was the codon optimized, N-terminally-tagged construct of nhTMEM16 used for experiments in Figure 5 not used for experiments shown in Figure 4C?

In vitro assays have previously indicated a basal activity of nhTMEM16 in the absence of Ca2+. Do the authors have evidence for such activity in their assays?

The results describing the behavior of TMEM16A mutants are puzzling. Why do 20% of cells expressing WT show scrambling? What is the evidence that the currents measured from cells transfected with the TMEM16A mutant V543S after 15 min are still mediated by this protein? How would WT currents measured under the same conditions look like?

Why does the mutant K588N but not K588Q confer scrambling activity to TMEM16A given that, according to a recent structure at low resolution, the residue might not be exposed to the membrane?
