# Peer review - Round 1

Editors:
- Leon D Islas, https://ror.org/01tmp8f25 Universidad Nacional Autónoma de México Mexico

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.97696.sa0](https://doi.org/10.7554/eLife.97696.sa0)

This manuscript addresses the molecular mechanism of C-type inactivation observed in a mutant of the Kv2.1-1.2 (Shaker-like) chimeric voltage-gated potassium channel. Previous structural studies using a triple mutant of this channel, which enhance slow inactivation, have demonstrated that inactivation involves a dilation at the outer mouth of the selectivity filter of the channel, leading to a non-conductive state. Here, based on solid molecular dynamics simulations, corroborated by electrophysiological experiments, the authors conclude that the dilated state on its own is conductive, and that an additional conformational change involving occlusion of the pore by I398 is critical to halt conduction. This important conclusion is thought-provoking and motivates further exploration to evaluate pore dilation and I398 in other Kv channels.


---

# Peer review - Round 1

Editors:
- Leon D Islas, https://ror.org/01tmp8f25 Universidad Nacional Autónoma de México Mexico

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.97696.sa1](https://doi.org/10.7554/eLife.97696.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Isoleucine gate blocks K+ conduction in C-type inactivation" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Merritt Maduke as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

During collaborative discussion, three reviewers and the reviewing editor identified the following main concerns that the authors should respond to.

1) It is well established that K-selective channels support potassium permeation through tight coordination by the selectivity filter. It is not clear how a dilated pore might allow selective permeation of this ion. The authors need to clarify possible mechanisms regardless of the MD simulation results.

2) The main conclusion of this manuscript is based on the results of long MD simulations with three force fields. Two of the force fields give inconsistent results and this is fixed by simulations with an ad-hoc correction of the CHARM36 force field. There are no simulations carried out with the corrected CHARMM36m-NBFIX force field that indicate that it continues to reproduce known behavior in WT channels. Authors suggest that the difference in simulation results might be due to the application of harmonic restrains in previous simulations. It should be clarified with simulations if the key differences in results are due to properties of the force fields or the setup of the simulation system.

3) In the AMBER simulation presented in Figure 2, permeation cessation does not seem to be correlated with the movement of the I398 as stated in the text. Please clarify.

4) It is stated that in the AMBER simulations, the distance between β carbons of I398 residues is reduced to 9 angstroms and this leads to a less than 2 angstroms constriction. What are the expected dimensions for the I398N mutant channel? Do simulations of this mutant channel show a WT-like permeation behavior or a dilated selectivity filter.

5) The authors claim that the simulations indicate a similar rate of potassium flow for the kv1.2/2.1-3m channels in the dilated state as for WT Shaker channels. However, it has been known for a while that Shaker W434F channels, which are thought to be permanently c-type inactivated, still allow permeation at the same rate as WT, ~13 pS, just with extremely low open probabilities and very short duration (Yang, Yan and Sigworth, 1997). The simulations presented here, and elsewhere, seem to suggest that the permeability of the slow inactivated state(s) is just significantly reduced. This important discrepancy needs clarification.

6) The 3m channel and the 3m-I398N mutant seem to activate are much more positive voltages than the kv1.2/2.1 channel (Figure 3 E) however in the comparison of time courses (Figure 3d) the I398N mutant activates way faster at the same voltage, this seems to be inconsistent. Also, the voltage pulses employed are too short. Kv1.2 channels slow-inactivate over a time course of seconds. It is possible that the I398N mutant still inactivates over seconds. In fact, Figure 3c shows an indication of slow inactivation as compared with kv1.2/2.1 channels. Given that the I398N mutation activates at more positive voltages, inactivation should be assessed at voltages that saturate the open probability for each channel.

Reviewer #1:

In the present manuscript, Treptow, Liu, Bassetto Jr and colleagues propose a novel mechanism for how C-type inactivation diminishes ion conduction in voltage-gated potassium (Kv) channels. C-type inactivation is a time-dependent mechanism that manifests as a decrease in the ionic current within the second timescale until it reaches a steady-state with minimal conductance. Although the mechanism of C-type inactivation was originally studied in the Shaker Kv channel (Hoshi et al. 1991 Neuron), the structural basis for a related mechanism of slow inactivation was first studied in the KcsA channel (Chakrapani et al. 2007 JGP, Cordero-Morales et al. 2006 NSMB, Imai et al. 2010 PNAS, Kim et al. 2016 JGP, Maffeo et al. 2012 Chem.Rev., Piasta et al. 2011 JGP, Tilegenova et al. 2017 PNAS, Varga et al. 2007 Biochim Biophys Acta, Cuello et al. 2010 Nature). A consensus based on the large amount of experimental data collected on KcsA pointed to the selectivity filter (SF) as the responsible part of the channel for C-type inactivation, which was proposed to collapse during inactivation. This collapse of the filter was the accepted working model prior to recent cryo-EM structures of Kv channels in C-type inactivated states showing that the filter dilates during inactivation (Reddi et al. 2022 Sci.Adv, Tan et al. 2022 Sci Adv, Selvakumar et al. 2022 Nat Comm, Wu Y et al. 2024 pre-print, Stix et al. 2023 Sci Adv,). As the mechanism of selective K+ permeation at high rates has long been established to result from multiple occupancy of the SF (see below), dilation of the filter to remove the outer K+ binding sites would be expected to diminish ion permeation during inactivation, an expectation borne out in Molecular Dynamics simulations (Tan et al. 2022 Sci Adv, Stix et al., 2023Sci Adv). The mechanism proposed by the authors in the present paper, however, challenges our current understanding of the general mechanism for C-type inactivation in Kv1 channels by proposing a new residue, an Ile below the SF as the 'true' gate that impedes ion conduction in C-type inactivated channels. The proposed novel mechanism arises from an MD simulation using the AMBER forcefield and the cryo-EM structure of the Kv1.2-2.1 chimera with 3-point mutations (3m). The 3m mutation (W362F, S367T and V377T) aims to render the channel in a non-conducting C-type inactivated state by speeding its inactivation in a fashion similar to W434F in Shaker (Perozo et al. 1993 Neuron, Yang et al. 1997 JGP) but failing to do so, the Kv1.2/2.1-3m channel is still able to conduct ions; a transient, fast inactivating macroscopic current can be seen upon depolarization. The reason for this is that the chimeric channel contains the sequence of Kv1.2 in the SF, which is known to be particularly resistant to inactivation and requiring more than one mutation to achieve a fast-inactivating phenotype (Suarez-Delgado et al. 2020 JGP, Wu et al. 2022 JGP, Reddi et al. 2022 Sci.Advances).

The fact that the authors chose this particular chimeric channel with the 3 point mutations (Kv1.2/2.1-3m) to study the mechanism of ion permeation during C-type inactivation is an odd choice given that block of ion permeation is incomplete in this mutant (Figure 3B) (Reddi et al. 2022 Sci.Advances). Moreover, the data presented in this manuscript do not support the authors' conclusions.

Strengths:

The new idea presented by the authors is provocative and both MD simulations and electrophysiological techniques are appropriate to explore the mechanism of C-type inactivation.

Weaknesses:

1) The authors seem confused why a dilated filter would be less conductive than one containing 4 ion binding sites. Although details about the mechanism of K+ permeation across the SF remain incompletely understood (including whether there is 'hard' or 'soft knock-on' between ions to promote permeation), it would seem to be established that K+ channels are exquisitely K+ selective because the backbone carbonyls replace waters of hydration and that multiple ions bound within the filter repulse each other to promote rapid throughput (Doyle et al. 1998 and Zhou et al. 2001, Morais-Cabral et al. 2001, Zhou and Mackinnon 2003).

2) The authors proposal that I398 is the gate for C-type inactivation is inconsistent with over multiple structures of KcsA and Kv channels with varying propensities to inactivate because that residue never occludes ion permeation in any of those structures, solved by both X-ray crystallography or cryo-EM. The bar should be high for overturning the weight of evidence that KcsA collapses during inactivation or that Kv channels dilate, and would logically require new structures to support the key conclusions in this study.

3) The MD simulations and the permeation events.

The mechanism proposed by the authors arises from the sole finding of Ile398 twisting during MD simulations produced with the Kv1.2/2.1-3m structure and the AMBER forcefield. The authors propose that the twisting of the Ile creates a gate under the SF that blocks ion permeation during C-type inactivation. This MD result was observed using the unrestrained structure and the AMBER forcefield is the hypothesis generator and the only condition where the authors see this conformational change (Figure 2B). The MD simulations using the CHARMM36 forcefield, on the contrary, show permeation events for half the 10 µs simulation (Figure 2C) and no twisting on the I398. This discrepancy is presented by the authors as a property of the different forcefields used, so they use CHARMM36m-NBFIX to approximate the CHARMM36m force field parameters to AMBER, the permeation events reduce, however, the Ile does not flip in this simulation. These inconsistencies are problematic and not adequately justified by the authors.

In addition, to contextualize these permeation events, it is necessary to see how these simulations, with the exact same conditions and force fields would describe ion permeation for the WT channel in a conducting conformation. The WT MD simulations would likely show many more permeation events without flipping of the I398. This direct comparison will help understand which simulation/force field is more representative of the functional state of the channel and put in context how conductive/nonconductive the Kv1.2/2.1-3m channel is. It seems likely that the present results would be qualitatively consistent with simulations of Shaker performed while constraining the structure and showing that dilation diminishes ion permeation The identity of the I398 as a gate

If the I398 residue is a gate and the residue responsible for diminishing ionic flow in the C-type inactivated state, it is rather curious that it has never been seen before given how many simulations have been run on KcsA and Kv channels. Can the authors provide a rationale for supporting their conclusions in light of what has already been done? How many times did the authors observe the conformational change of this residue relative to the amount of MD runs? If the authors constrain the structure as in previous simulations on Shaker, would I398 no longer adopt a conformation that blocks ion permeation? Also, the results in Figure 2 and FigS2 using the AMBER forcefield, seem to disagree. When the authors repeat the MD simulations using the AMBER forcefield restricting the I398 movement and making it 'permeable' the permeation stops after 2 µs with a long residency of K+ ions in the pore. This result alone would seem to challenge the authors hypothesis and clearly suggests that the twist of the I398 is not required to stop ion permeation events because the dilated structure alone seems to be doing that. The CHARMM36m-NBFIX simulations show only 3 permeation events during the whole simulation. How do the authors reconcile these results with their conclusions?

4) Functional consequences of the I398N mutation

It is known that mutations at I398 have a strong functional effect in other channels like Shaker (I470) or KcsA (F103), where previous studies have provided support for a key role of this residue in coupling opening of the inner gate with conformational changes in the SF during inactivation. Those studies are considerably more detailed than the present functional studies and would seem to be inconsistent with I398 functioning as a gate. Val substitutes well for Ile, both Cys and Phe are slower and Leu is faster, and no mutations completely disrupt C-type inactivation (Holmgren et al. 1997, Peter CJ et al. Sci Reports 2013, Cuello et al. 2010 Nature 466 203-8, Cuello et al.2010 Nature 466 272-5). How can the authors reconcile their new ideas with these earlier studies and mechanistic ideas about the role of I398? In addition, introducing an Asn, introduces a polar side chain in a hydrophobic region, a radical change that can affect more than just the C-type inactivation of the channel. In order to understand the effect of I398N it is necessary to study the effect of that mutant in isolation without the 3m mutations since it is a new mutation in the context of Kv1.2/2.1. For instance, does it also impair C-type inactivation in the absence of the 3m mutations? Does it affect the permeation of potassium? Does it shift the G-V curve? Without this information it's not possible to fully understand the results presented in Figure 3. Might introducing a polar residue in this region impact ion binding within the SF? Might the mutation alter inactivation by increasing the affinity of K+ for the filter? Finally, the MD simulation results with an Asn at position 398 disagree with the proposed mechanisms and the functional data. The electrophysiological experiments show a channel that conducts ions (Figure 3C) however the MD simulations using the AMBER forcefield do not, and the CHARMM36m only shows permeation events for 3 µs out of 10. How do the authors explain these results?

5) Toxin binding to the outer pore

The results presented with AgTxII seem quite preliminary and it's hard to understand how they support the proposal of I398 functioning as a gate. Only a few traces are shown at one toxin concentration rather than time courses to demonstrate that equilibrium has been achieved. It seems that the 3m mutations are somehow altering toxin binding regardless of whether the I398N mutations rescue ion conduction, but how this supports I398 functioning as a gate is unclear. How do the AgTxII results relate to the model proposed for CTX in Fig3F? Are the authors proposing that the outer pore of the SF changes its architecture when the I398N mutation is introduced?

Recommendations for the authors

1) The statement "These simulations strongly suggest that the filter in the dilated conformation can conduct K+ ions, and that the conformational motion of I398 is necessary to truly block conduction." As well as "Despite intrinsic force-field differences with respect to channel conductivity, all three atomistic models support that the dilated conformation of the selectivity filter is, by itself, conductive and the isoleucine gate is required to effectively block K+ current across the channel." are not fully supported by the MD results since restricting the conformational motion of I398 also blocks conductions as shown in S2, please review these statements.

2) "Gating fluctuations of I398 are, however, clearly observed in the late stages of the simulation and, correlate well with the reduction of ions in the central cavity of the channel and with the conduction across the selectivity filter. Particularly important, the CHARMM36m simulation adds support to the assumption that the dilated conformation of the selectivity filter is conductive, and that closure of the isoleucine gate is required to shut down ion transport across the channel." Please reference these results in the figure, the CHARMM36m forcefield did not show the Ile changing its conformation in the Figures presented.

3) In observance of the result "the estimate of ~0.2pA is still orders of magnitude larger than the measured current in the triple-mutant channel upon C-type inactivation (vide infra), and, therefore, the conductivity properties of the "dilated" conformation of the selectivity filter cannot explain alone the inactivation of kv1.2-kv2.1-3m under membrane depolarization." There is another possible explanation for this discrepancy related to the configuration of the MD simulations. Taken together the variability of the results restraining vs non-restraining the I398, there is a possibility that the calculations obtained from the MD simulations are not representing the C-type inactivated state of the Kv1.2/2.1-3m triple mutant.

4) "Recently, high-resolution structures of Kv channels revealed a novel conformation of the selectivity filter that is partially dilated at its outer end and constricted near its internal face (8-10)". The internal face of the SF architecture of all the cited structures (S3 and S4) can still solve densities for coordinated K ions in their internal face and as stated in the legend of Figure 1 resembles that on the conductive state, arguing against the constricted conformation stated by the authors please review.

5) This statement in the Abstract could be misleading for the reader, if I understand it correctly, it reads as if the electrophysiology measurements demonstrate that the Kv1.2-2.1-3m mutant is conducting, but then is stated that functional experiments show inactivation, please review: "While the experimental structure was interpreted as the elusive non-conductive state, molecular dynamics simulations and electrophysiology measurements demonstrate that the dilated filter of kv1.2-kv2.1-3m, however, is conductive and, as such, cannot completely account for the inactivation of the channel observed in functional experiments".

Reviewer #2:

Based on computational analysis of structures of the conductive WT Shaker B and Kv1.2-2.1 chimera and the pore-dilated Shaker-W434F and triple-mutant Kv1.2-2.1 chimera channels, the authors hypothesize that pore-dilation alone cannot account for the non-conductive tendency of these channels in the C-type inactivated state. The authors then go on to analyze the Kv1.2-2.1 triple mutant (kv1.2-kv2.1-3m) by simulation with AMBER and CHARMM36m force fields, and find that under conditions where the pore-lining residue I398 is allowed to relax, the I398 side chains from all four subunits rapidly twist to occlude K+ conduction, whereas K+ conduction is maintained under conditions where I398 does not occlude the pore, as in the kv1.2-kv2.1-3m crystal structure.

To validate the role of I398 in controlling conduction in pore-dilated channels, the authors introduce the mutation I398N in kv1.2-kv2.1-3m channels and find that the substitution with the hydrophilic asparagine residue effectively abrogates C-type inactivation behavior. The addition of I398N does not appear to act by preventing the pore-dilated conformation, as Agitoxin-II, which strongly blocks the open-conducting but not pore-dilated channels, does not block the kv1.2-kv2.1-3m-I398N channels.

The manuscript follows a logical series of experiments and thoughtful, rigorous analysis. The mechanism presented is supported by computational and electrophysiological data, and underscores a potential role for conformational changes in pore-lining residues in inactivation that may occur in other K+ channels.

Results presented in the manuscript make the strong prediction that an asparagine at position 398 should not occlude the pore in the triple-mutant background, and should stabilize conduction even when the pore is "dilated". It should be possible to show this directly with a simulation, and I think such a demonstration would greatly strengthen the manuscript.

Reviewer #3:

This manuscript reports on an investigation by Treptow et al. of C-type inactivation in voltage-gated potassium (Kv) channels, a process whereby prolonged voltage activation leads to a nonconductive state. They examined a triple-mutant Kv1.2-Kv2.1 channel to provide a detailed characterization of the dilated conformation of the selectivity filter. This structure was initially thought to represent the nonconductive state. However, molecular dynamics simulations and electrophysiology showed that this dilated state is actually conductive. The study found that effective inactivation involves an additional conformational change at isoleucine residues (I398) in the pore-lining segment S6, which acts as a hydrophobic gate just below the selectivity filter. This mechanism is critical for C-type inactivation and presents new targets for drug development to modulate Kv channel gating states. This work constitutes a significantly novel contribution to our understanding of the mechanism of conduction of potassium ions. As such, I strongly recommend publication.

I have a few comments that the authors could consider for improving the presentation of their results:

1) The conformational free energy landscape is a crucial piece of the story, which gives quantitative substance to the hypotheses tested throughout the work. However, the description of these results appears surprisingly only in the Discussion section as an afterthought. The authors should make an effort to incorporate these results in the body of the results.

2) Related to the previous point is a general lack of details concerning these calculations. For instance, it is imperative to have an idea of the error associated to the estimated free energies.

3) The differential affinity of the toxin for the two selectivity filter conformations is another crucial piece of the puzzle as it enables to unambiguously interpret the effect of the mutation of isoleucine into asparagine. However, the docking and binding affinity calculations are buried in the supplementary information. The authors should consider giving greater space and emphasis to these results in the main text

4) I am intrigued by the massively different behavior shown by the charmm force-field. What is the reason for this? I wonder if the greater stability of the hydrated configuration of the isoleucine side chain is an artifact due to the water model (tip3p does not reproduce water's surface tension, so wetting/dewetting transitions are not expected to be correctly described).
