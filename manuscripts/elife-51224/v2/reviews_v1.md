# Peer review - Round 1

Editors:
- Leon D Islas, Universidad Nacional Autónoma de México Mexico

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.51224.sa1](https://doi.org/10.7554/eLife.51224.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Chloride-hydrogen exchangers of the CLC family are important targets for known human disorders. Unraveling their molecular mechanisms is important for understanding their role in physiology. In this manuscript the authors show a novel mechanism for the simultaneous occupancy of chloride and protons in the transport pathway. These results should open new avenues of research to understand CLC transporters and channels.

Decision letter after peer review:

Thank you for submitting your article "Divergent Cl- and H+ pathways underlie transport coupling and gating in CLC exchangers and channels" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Leon D Islas as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Reviewing Editor and Richard Aldrich as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Michael Pusch (Reviewer #2); Merritt Maduke (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. A fourth expert on MD simulations was also consulted.

Summary:

This manuscript by the Accardi group proposes a new molecular mechanism to explain chloride and proton transport in CLC-class transporters and channels.

Using a combination of molecular dynamics, electrophysiology and non-canonical aminoacid substitutions, the authors find two phenylalanine residues that facilitate the movement of a protonated external glutamate involved both in gating and chloride permeation. This conformational change is different from the previously proposed one where the external glutamate occupies a chloride binding site and competes with the ion. This is an original and exciting paper and it constitutes an important contribution to understanding CLC channels/transporters.

Essential revisions:

1) In Figure 2—figure supplement 1F, the authors report PMF calculations that show that the preferred state of Phe357 for the Scen-Sext configuration is the 'up' rotamer. This is the rotamer observed in multiple crystal structures, e.g. ion-bound WT, E148Q, E148A EcCLC, WT apo EcCLC and WT CmCLC. Accordingly, one can see in Figure 2—figure supplement 1AB that the umbrella-sampling simulations that underlie the PMF in Figure 2A probe this 'up' rotamer when Z1 ~ 0 and Z2 ~ 5 A, i.e. the Scen-Sext configuration.

The reason why the Scen-Sext configuration is not a metastable state in the PMF in Figure 2A cannot be, therefore, that Phe357 is in the 'wrong' rotamer; to the contrary, the PMF in Figure 2A samples the 'correct' rotamer for Scen-Sext, according to the data provided in Figure 2—figure supplement 1AB. The reason must be instead that other configurations, and in particular those with Z1 < 0 and Phe357 'down', are more favored energetically when examined in simulation. Consistent with this, when Phe357 is artificially fixed in place in the 'up' rotamer (Figure 2D), the states with Z1 < 0 are strongly penalized.

It would seem that the central and clear prediction from this simulation data is that Scen-Sext with Phe357 up is an energy barrier for the mechanism of ion motion through EcClC, at 4-6 kcal/mol, and is strongly disfavored relative to e.g. Sint-Sext with Phe357 down (Figure 2-figure supplement 1B). Yet, the latter state is not included in the mechanistic diagram shown in Figure 8, which instead depicts the former as an intermediate (states V and VI), despite the PMF in Figure 2A. This is not internally consistent. More importantly, isn't this result/prediction counter to the E148Q structure (Phe357 up) and the analysis of relative ion occupancies therein (as well as in WT and E148A) by Lobet and Dutzler 2005? Also, isn't it at odds with the interpretation of the ITC experiments in Picollo et al., 2012 ("Our data suggest that protonation of Glu148 is unfavorable with no ions in the transport pathway, that protonation of the gating glutamate is favored by binding of a Cl− ion to Scen and is greatly stabilized by a second Cl− in Sex"). The authors should clarify if Scen-Sext with Phe357 up is a true free-energy minimum. The PMF in Figure 2A shows that Sint-Scen is not a metastable state either. Like Scen-Sext, it falls in the 4-6 kcal range, and is in a downhill gradient in free energy, which seems to suggest the ion in Sint isn't stable. This could be explained by the lower affinity of this site, but at 150 mM KCl, the simulation is well above saturating conditions.

A PMF calculation analogous to Figure 2A for E148Q with ions occupying Sext and Scen would help to alleviate these concerns – assuming it shows that the experimentally determined structure is a stable configuration.

2) The authors should provide an explanation of what factors cause Phe357 to favor a different rotamer when the ion configuration changes from Scen-Sext to Sint-Sext (Figure 2—figure supplement 1B) and from Scen-Sext to Sext only (Figure 2—figure supplement 1D), but somehow not from Scen-Sext to Scen only (Figure 2—figure supplement 1E). It is difficult to envisage how the sidechain of Phe357, which projects away from the chloride pathway and does not directly interact with the ions, nevertheless responds to the occupancy of the binding sites. Is this due to changes in the conformation of the structure?

3) What ion configuration was equilibrated for 100 ns before the PMF in Figure 2A was calculated? Were other starting conditions tested? How were the PMF calculations shown in Figure 2—figure supplement 1C-F initiated?

4) In regard to the proposed dipole-pi interaction between protonated Glu148 and the aromatic rings of Phe190 and Phe357: what is the magnitude of this interaction, as represented by the simulation forcefield, compared with e.g. a hydrogen-bond, all other factors being equal? Are the snapshots in Figure 3 anecdotal observations, or do they reflect statistically representative states? If the latter, how were they selected?

5) Mutants of Fext in CLC-5 (F255A) and CLC-7 (F301A) show rather voltage-independent currents, including steady state inward currents. There is a suspicion that they may be contaminated significantly by endogenous leak currents. Therefore, the authors have to provide positive evidence that these (inward) currents are real. Otherwise these data should be removed.

6) The fact that Gluex in CLC-1 structures seems to be in a position out of the Cl permeation pathway could be due to radiation damage in cryoEM data acquisition, to which glutamate residues are particularly sensitive. This should be discussed.

7) In a paper from 2003 (in which one of the lead authors of this manuscript is a co-author as well), Fcen of CLC-1 has been quite extensively characterized. For example, in addition to dramatic effects on gating, the F484A mutant showed a reduced single channel conductance. Also, in more recent papers from the Desaphy group, mutants of Fcen that cause myotonia have been characterized. This work should be discussed.

8) In the same 2003 paper (Estevez et al., 2003), Fcen was proposed to be part of an inhibitor binding site. This, together with recent structural data on the CLC-1 channel, should be discussed (e.g. could binding of these inhibitors impede the movement of Gluex?).

9) The outward movement of the protonated Gluex without interference somehow reminds me of a kinetic mechanism proposed for CLC antiporters (Jentsch and Pusch, 2018), in which a hypothetical "swap" between protonated Gluex and a Cl ion was proposed. This might be discussed.

10) Regarding the Sext Cl site, the recent paper from Park et al., from the Lim group should be discussed.

11) The experimental tests of the role of F190 and F357 in the CLC mechanism are not convincing. In CLC-ec1, the authors show that mutations at these positions decrease turnover rates and increase Cl-/H+ coupling stoichiometry. While this result can be called "consistent" with the MD simulations, it would also be consistent with any number of other mechanisms. Moreover, it is likely that mutating any other similarly conserved residue (for example F199) would cause similar changes in function. So, it is not clear that these results validate predictions of the MD simulations. Similarly, mutations on CLC-7 and CLC-0 could have many different interpretations. Unfortunately, it is not obvious what experimental tests could be done to specifically test predictions of the MD simulations. One experiment that would help would be to put F190 and F357 mutations into the CLC transporters in an uncoupled (E148A in CLC-ec1) background. Since the Phe residues are predicted to predominantly affect the H+-transport branch of the mechanism, they should have little or no effect (on Cl- transport) in such a background. Ideally, it would be best if the authors could think of additional specific tests of predictions. If that is not feasible, it is important to remove a lot of overstatements that have been made with respect to interpretations of the experimental results. For example, most of the effects of the mutants are not "drastic" or "extreme" but are actually rather modest effects on function and much smaller than effects of other known CLC mutations. Also, the concluding sentence (…"our results show that the aromatic slide forms an evolutionarily conserved structural motif that is…") would need to be toned down.

12) The reduced current levels for the F301A and F514A mutants cannot be distinctly ascribed to the reduced transport rate observed in CLC-ec1. The effect of the mutant could also be a reduced expression level. The voltage-clamp experiments do not distinguish between these possibilities. The authors should provide evidence for similar expression levels or tone down this assertion.

13) The effects of the alanine substitutions in both external and central phenylalanines seem to be an enhancement of gating (current measurable at every voltage), without too drastic changes in voltage-dependence (z for WT and F514A is the same). Alternatively, could the inward current in the mutants be carried by protons? This would be a similar behavior to omega currents in the voltage sensor domain proteins. This distinction is important because the effects of atomic mutagenesis are divergent with those of alanine substitution. Substitutions of the central phenylalanine make gating more difficult, while alanine substitutions seem to enhance gating.

14) It would have been nice if non- canonical aminoacid incorporation experiments were carried out in the CLC-ec1 transporter, for which the MD simulations were performed. Is there a reason for this? Although it seems that the effects are conserved, it seems also that gating and permeation effects of mutagenesis are mixed in the CLC channels, while transport could be better characterized in CLC-ec1.
