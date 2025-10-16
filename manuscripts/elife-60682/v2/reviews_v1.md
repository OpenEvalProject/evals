# Peer review - Round 1

Editors:
- Cynthia M Czajkowski, University of Wisconsin, Madison United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.60682.sa1](https://doi.org/10.7554/eLife.60682.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

How structural motions in pentameric ligand gated ion channels(pLGICs) lead to functional channel gating transitions remains poorly understood. Using the prototypic bacterial proton-gated channel GLIC, fluorescent reporters of protein conformation and kinetic modeling, the authors found a set of mutations that mostly alter pre-gating transitions and others that mainly alter gating (pore opening). Using structural trajectories identified by normal mode analysis to interpret their data in structural terms suggests that pre-activation transitions involve quaternary compaction of the extracellular domain and that activation involves a re-organization of a central gating region. This paper adds new mechanistic information about pLGIC activation.

Decision letter after peer review:

Thank you for submitting your article "Mutational analysis to explore long-range allosteric coupling and decoupling in a pentameric channel receptor" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Olga Boudker as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Andrew J R Plested (Reviewer #1); Grace Brannigan (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

How structural motions in pLGICs lead to functional channel gating transitions is not well understood. In a previous study (eLife 2017), this group used time-resolved fluorescence quenching experiments in a prokaryotic pLGIC, GLIC, and identified motions in the extracellular domain (ECD) that occur prior to channel opening. In this manuscript, the authors extend these studies. To interpret their previous fluorescence quenching data in structural terms, the authors used normal mode analysis to identify structural trajectories underlying GLIC closed to open channel gating transitions. The simulations yielded two pathways leading from closed to open channel end states. To monitor whether motions in the ECD are coupled to motions in the TMD (pore opening), the authors used mutations and the allosteric drug modulator propofol to perturb GLIC gating transitions and compared the effects of these perturbations on proton-induced current responses and steady-state fluorescence quenching data. Based on their data, the authors conclude that they have identified new structural conformations and possible new allosteric pathways during gating, and that GLIC and its mutants have access to a large repertoire of conformational states.

While the data are interesting, the overall concern is with interpretation of the data. The logic of the arguments is not clear enough to support the conclusions. Comparisons between theories are not precise nor quantitative enough to support claim of a new gating model. Simulation description and limitations of this approach are not well described. As written, it is difficult to follow the authors line of reasoning and authors do not discuss alternative mechanisms that can fit their data. Significant re-writing and new analyses to make the arguments clear and focused on what novel contributions the data in this paper are providing are needed. The manuscript would be significantly strengthened by addressing the following major concerns.

Essential revisions:

1) A 1-D, steady state signal (quenching) is used to discern multiple states (meaning, functional conformations, division in space) because it takes multiple values. But the signal is the infinite time average over all states, in different conditions. How do we know that the signal doesn't represent different balances of occupancies of the same small number of states (such as 2 states). There are no apparent reasons why results could not be explained from mutants that change open-closed equilibrium as from new conformational states. The authors need to fully discuss and address this alternative mechanism for explaining the data.

2) What experiments provide direct evidence for intermediates? Can the intermediates states represent abstract transitional milestones, not concrete conformations? That interpretation would be consistent with what has been long established in protein folding, but would entail a major shift in how structures are interpreted, because there would not be a meaningful way to connect conformations to kinetic models.

3) Description of the iMOD fit simulations is unclear and does not provide enough detail. How many simulations were run to yield the two trajectories? It is not clear whether iMod-Fit returns two trajectories from a single calculation or whether multiple simulations were run and the trajectories were clustered. In the methods section (page 25, lines 25-26), trajectory A conformation change is from closed to open whereas trajectory B conformation change is from open to closed. However, in the figures, for both trajectories, frame 1starts at GLIC-pH7 (closed).

4) Since their previous time-resolved fluorescence quenching data (eLife 2017) demonstrated that motions monitored at Bimane-136 (ECD β sandwich compaction) and Bim-250 (M2-M3 loop motion) mainly occur prior to channel opening (activation scheme in Figure 4B), it is unclear why the authors conclude that their Bim-250 data support pathway A identified from their simulations. In pathway A, Bim-250-Y197 unquenching happens in same time frame as the increase in pore radius at the 9' position, whereas in pathway B the unquenching of Bim250-Y97 happens before complete pore radius dilation (Figure 2B, 2D). The experimental data at this position seems compatible with the B trajectory. Moreover, the unquenching of Bim-136-W101 appears consistent with either trajectory (Figure 3B) and occurs before the simulated pore dilation. It is unclear what new information the simulations are providing except that the steady-state fluorescence quenching data show good agreement with the simulated end states.

5) To monitor how motions in the ECD are coupled to motions in the TMD (pore opening), the authors used mutations and the allosteric drug modulator propofol to perturb GLIC gating transitions and compared the effects of these perturbations on proton-induced current responses and steady-state fluorescence quenching data. Since the fluorescence data are steady-state, whether a mutation causes an effect on the timing of the structural change in the gating pathway or an effect on the percentages of different conformational states in the ensemble at steady-state is not known and confounds data interpretation. The authors need to discuss this point.

5) Data supporting the statement that mutations of H235, L157 and L246 lead to new global conformations are limited. One could argue that these mutations have dramatic functional effects (eliminate current) and thus, it is not all that surprising that alternative conformations might be adopted that normally would not be visited.

6) Data to support the claim that propofol specifically affects the pre-activation step are limited. Propofol could affect open-closed equilibrium.

7) It is striking that the fluorescence quenching profile for the Q235 mutant with propofol closely mirrors that of H235 without propofol (Black vs light/dashed green lines in Figure 8D). The addition of propofol reverses the effect of the H235Q mutation on structure, not just qualitatively, but close-to-quantitatively, for both the Bim136-Q101W and Bim135-W72 sensors. This is remarkable, especially for the latter sensor where the curve is complex. Yet the discussion treated the two sensors differently despite a similar reversal of the effect of the H235Q mutation, and the authors say the data for Bim135-W72-H235Q cannot be interpreted in structural terms. This explanation is confusing, especially since the corresponding figure is given equal weight in the paper. The authors need to revisit this section to improve clarity or move the mutant results and discussion of explicit technical limitations to supplementary information.

8) The authors claim that their results "challenges the conventional concept that receptor activation involves a single conformational pathway." Do the authors believe their results are inconsistent with the 4 state Heidemann and Changeux models from the 1980s?

9) TMD motions were not measured. Monitoring motion of the M2-M3 loop does not monitor changes in the TMD or pore opening. In previous work, authors used Bimane243 to monitor M2 motions. Additional reporters of TMD motions would be helpful.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Mutational analysis to explore long-range allosteric coupling and decoupling in a pentameric channel receptor" for further consideration by eLife. Your revised article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Olga Boudker as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Andrew J R Plested (Reviewer #1); Grace Brannigan (Reviewer #2).

We appreciate the authors efforts in responding to the previous critiques and in revising the original paper. The revised paper is improved and the reviewers feel that no additional experiments are required. The paper has changed considerably. The biggest concern is that the revised manuscript, as written, is still difficult to follow, even for experts in the field, making it difficult to evaluate and appreciate its impact. The manuscript requires considerable editorial work to improve clarity. The specific points are:

1. The interpretation of the data with propofol is still a weak point. For instance, the manuscript says that "Our data thus shows that propofol does not act locally by altering the conformation of the TMD, but rather acts on the global allosteric transitions by displacing the equilibria and preserving ECD-TMD coupling" However, the preceding discussion is minimal. I spent a while trying to piece together how the data show that propofol's mechanism of action is not local. It is clear that the binding of propofol does affect the conformation far from the TMD, but this sentence implies that the authors have shown that TMD conformational change is insufficient for action. In other words, I could not figure out how the authors showed that ECD conformational shifts were necessary for propofol to act. If I am missing something, a few more sentences spelling out the logic here would be helpful or rewording of conclusions is needed.

2. The new Figure 9 is so full of important information that it gets hard to follow. I request that all the isomerization constants be compiled in a table for ease of comparison. The caption for that table can then refer to the equations and methods from which they were derived and differentiate between normalization schemes. While it may be useful to keep them in Figure 9 as well, Figure 9 is already overwhelmingly complex. I suggest either having fewer plots or fewer elements per plot. The arrows from one plot to the next were also not intuitive. Mainly, I request that the authors look at this figure with fresh eyes and consider breaking it up or streamlining it somehow.

3. Line 37 "Seminal work in the 80s showed that a minimal four-state model describes the main allosteric properties of the muscle-type nAChR (Heidmann and Changeux, 1980; Sakmann et al., 1980)."

First, the word seminal is best avoided; it is rather outdated. I would not take these similarly out-of-date works as a benchmark, rather use them as a counterpoint – perhaps you can say: "although xxx work in the 1980s, …" and then introduce the updates?

4. Line 66 "However, the physiological relevance of these structures or their assignment to particular intermediates or end-states in putative gating pathways remains ambiguous and poorly studied."

This is a very important point and underlines the importance of the work at hand.

5. Line 69 "Conversely, it is likely that key conformations, unfavored by crystal packing lattice or under-represented in receptor populations on cryo-EM grids, are missing in the current structural galleries."

On the other hand, this is overstated. I would say "possible", not likely. Intermediates might be missing, but are they "key"?

6. Line 86 "much faster than ionic current measurement that occurs in the 30-150 millisecond range "

Much faster than the rise time of population or ensemble currents.

7. Line 116 "Two independent trajectories, A and B, were computed starting from each of the two end-state structures and divided into 12 and 11 frames respectively. "

I appreciate that the authors tried to explain better now, but this is still somewhat opaque. Please just say one trajectory goes from rest to active, and the other from active to rest. The use of "end-state structures" is confusing. They are both end and start, depends on which trajectory it is. Or are there really four structures – two crystals and two end states? Some of the figures suggest that each trajectory does not conclude in really the right place. I can't say which one because I have no idea what figure is which (figures not numbered and some do not correspond to figure legend order).

8. With iModFit, I think it is important to discuss how plausible it is that the transitions are not ergodic. This is mentioned in the discussion. In one way, we should not take these trajectories too seriously. But it is also important to consider the possibility that they are pulling out important information from the structures. Are the authors suggesting that the isomerisations are, preferentially, not reversible? I mention below that it would be a great future insight to have non-equilibrium data that could report the non-reversible motion at some of these sites.

9. Later in the paper, the text again makes me feel like I don't understand what iModFit does.

Line 176 "For the ECD quenching pair Bim136-Q101W, the simulations show that Bim136 and the Trp101 indole ring are separated in the resting-like state, and are in close contact in the active-like state (Figure 3A). "

The simulations? Are you referring to the docking results? The resting and active-like states are from structures, aren't they, not from iModfit? If the states used are from structures, there is little predictive power from the docking to these structures that couldn't be deduced by eye, is there? Or are you comparing the state at the end of the iModFit run, which isn't the other crystal state?

Surely iModFit (simulations?) only tells you about the trajectories of the fluorophores? This time-order of transitions between distances is interesting. But why is it mixed up with end state information (surely known from PDB)?

At the very least, a better description is needed. Overall, I still do not understand how the iModFit trajectories help to understand the steady state fluorescence.

10. Line 155 "In conclusion, using iMODfit we could generate two distinct trajectories that are in principle equally plausible to describe a gating transition of GLIC activation. "

But a really key point that doesn't really come up, but I think it should, is that the different trajectories really consist of at least two steps, Twist and the central gating motion, but they occur in different orders. This is a clear appeal to the intermediate states like flip and prime, and motivates the rest of the paper. The role of the compaction is less clear. If there were not distinct movements, the hysteresis in the motions would be much harder to understand. Still, the connection of the iModFit to the steady-state data is less convincing than any non-equilibrium data would be. This is the distinction between a plausible model (as the authors present) and evidence. The change of fluorescence at given sites should have different orders for activation and deactivation, shouldn't it? This would be worth mentioning. It is something for the future of course. And this is not to diminish the insight from the steady-state measurements.

11. Additionally, the flipped state, where the conformational change of the orthosteric site is predicted to be rather complete, but where the channel is closed, would fit the functional requirement of a pre-active state (Lape et al., 2008).

This is trivial because the flip state is just the name of a non-open agonist bound state. Also, flip is not the only type of state that fits, they might all be the same, from different perspectives. I wrote a comment about this once: "Don't flip out: AChRs are primed to catch and hold your attention"

12 The quantitative details of the fitting and the agreement or otherwise seem reasonable but I cannot claim to check in detail, I'm afraid. The individual conformations have various proton bound states and equilibria, so the 3-state model is quite a bit more complicated than at first sight. It might be nice to include the full model (to indicate the assumptions) in a supplementary figure. If, as the authors say, a relatively complicated proton binding scheme is needed to describe even equilibrium data, this is something of a find and needn't be buried. I don't think we have many ideas about how may protons are needed to gate.

13. I did notice that the Y28F mutant has the biggest change in the Pre-open constant. This selective effect was the case for the nearby A52S mutant in the glycine receptor – a big change in flip, no change in the main gating constants (Plested et al., 2007). Quite different at the K276E below that (Lape et al., 2012). But there are tons of mutants on these positions, maybe there are better ones to compare.

14. Table 1 statistics. Multiple mutants are being compared to the same reference value. Unpaired t test is not the correct test to use for these data. Investigators should use an ANOVA with a posthoc test such as a Dunnett or Bonferroni.

15. MWC fitting of the fluorescent and current data is used to conclude that mutations at the ECD alter the pre-activation step while those at the ECD-TMD interface and TMD alter the activation step (gating). Due to the assumption that the mutations do not effect proton affinity to the sites, the authors need to be careful about overinterpreting the data. The modeling provides support but is not conclusive.

16. How the fluorescence quenching data relate to motions identified by iMODfit is not obvious. On page 10, lines 315-318, the authors state "the fluorescence and electrophysiological pH-dependent curves presented in this paper underlie two major allosteric steps, pre-activation (a fast process causing the changes in fluorescence as previously identified in stopped flow experiments and activation (a slower phase). Based on their 2017 eLife paper, the bim136 fluorescence reports early pre-gating motions, and bim250 reports early pre-gating motions and some later motions. In the revised manuscript, based on iMOD fit/normal mode analyses, the authors state that bim136 is monitoring a quaternary compaction of the ECD that is occurring throughout the gating cycle and that bim250 is monitoring motion of m2-m3 loop which is part of the 'central gating reorganization' including opening of pore (see page 14, lines 452-455). Later in the paper (page 16, lines 528-529) they state 'ECD compaction is critically involved in pre-activation". This is confusing and requires additional explanation and discussion. If the fluorescent reporters at these positions are monitoring fast, early pre-gating motions then why is the quaternary compaction and m2-m3 loop motion part of the central gating reorganization? Am I missing something?

17. In the abstract, the authors state that 'preactivation involves major asymmetric quaternary motions of the extracellular domain'. It is unclear to me what experimental data support this conclusion. Is this based on the starting pH7.0 crystal structure? The authors need to clarify if the asymmetry that they are describing is at the subunit level or is based on two different motions in the ECD (twisting and compaction). Without strong experimental evidence for asymmetric motions, this conclusion should be removed from the abstract.

18. They use iModFit and NMA as synonyms in some parts of the paper, which causes confusion. iMODfit/Normal mode analysis treats the protein like a 3D elastic network. It doesn't capture interactions with solvent or specific residue-residue interactions. It superimposes multiple local low-energy fluctuations to find likely larger scale conformational fluctuations. You would get asymmetry when it costs less total energy to move a few chains by a lot, than to move all of them by a little. The more chains the protein has, the more likely it is that imodFit will find asymmetry. I'm not sure the imodfit simulations add much regarding asymmetry, but the expected behavior of these macromolecules at room temperature makes it an uncontroversial claim, albeit one without significant new evidence.

19. In revised manuscript (page 5, lines 155-157), authors state 'using iMODfit we could generate two distinct trajectories that are in principle equally plausible to describe a gating transition of GLIC activation'. Additional discussion spelling out the logic here is essential.

It is important for the reader to understand the limitations of iModFit, and for a non-computational reader to know what iModFit is not. The authors need to add further discussion in methods or result sections. It is not a physics-based simulation technique like molecular dynamics – I'd call it a numerical approach for generating hypothetical pathways, and then experiments or simulations need to distinguish between them. They have used it here as a conceptual framework. The software itself is not designed to generate trajectories, but to generate structures. Motions or trajectories generated by Normal Mode Analysis are always reversible. Then imodfit applies a bias on top of that, based on the structure, to get a directional trajectory. They applied two different biases (based on two different structures) so they ended up with two different hypothetical and reversible trajectories.

In their response letter, the authors state "one simulation is starting from the closed conformation to reach the open conformation, and the other from the closed to the open. Both trajectories represent plausible pathways for activation and deactivation." It is unclear whether the authors think that simulation A describes activation (closed channel to open channel) pathway and simulation B describes deactivation pathway (open channel to closed channel) or if they think that both trajectories can describe activation (closed channel to open channel)? Please clarify.

20. The authors should discuss and compare their results from iMODfit/NMA analyses to results from Toby Allen lab (PNAS 2017) using all-atom molecular dynamics with a string method to solve for GLIC gating pathways. What new information has been gained from the iMODfit/NMA?

21. Figures 3 supplementary 1 and 2 and 3 are in in different order compared to figure legends and text on page 6 lines 174-175. Authors need to check the order of the supplementary figures. It would be helpful if figures were labeled for review purposes.

22. Abstract should state which experimental results support their conclusions and describe the novel contributions that the data are providing.
