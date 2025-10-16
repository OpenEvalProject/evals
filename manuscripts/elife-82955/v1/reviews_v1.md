# Peer review - Round 1

Editors:
- László Csanády, https://ror.org/01g9ty582 Semmelweis University Hungary

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82955.sa0](https://doi.org/10.7554/eLife.82955.sa0)

This important study addresses the molecular mechanisms of the proton-activated chloride channel (PAC), a widely expressed ion channel involved in organelle pH homeostasis and acid-induced cell death. Convincing data based on structure-guided mutagenesis and molecular dynamics simulations provides new insight into the mechanism underlying channel desensitization under sustained acidic stimulation. The results are of interest to ion channel physiologists.


---

# Peer review - Round 1

Editors:
- László Csanády, https://ror.org/01g9ty582 Semmelweis University Hungary

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82955.sa1](https://doi.org/10.7554/eLife.82955.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Molecular mechanism underlying desensitization of the proton-activated chloride channel PAC" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including László Csanády as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Richard Aldrich as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. The model would be much more complete if specific protonation events involved were identified or at least clearly hypothesized. Can one say definitively that additional protonation events after opening are required as indicated in the model figure? Are they on residues implicated here? In addition to the charge reversal mutations presented, charge neutralizing mutations could be evaluated to address this: (1) E107Q, (2) D109N, and (3) E107Q/D109N to explore protonation of the acidic pocket and (4) E249Q, (5) E250Q, and (6) D251N to explore protonation of the beta10-11 linker.

Related to the above, the model figure 7 would benefit greatly if protonation states of residues (or groups of residues) were indicated, especially as previous work has implicated residues in different processes. In addition, predicted pKas in wild-type and mutant structures for the relevant acidic residues could be presented to guide possible protonation mechanisms and explain mutant effects.

2. The MD simulations raise several technical concerns, and are often inconsistent with the functional results. These issues should be addressed or at least acknowledged:

2.1. The MD analysis critically depends on assumptions on the protonation states of multiple residues, that are often located in close proximity to each other. In the methods, the authors state they use PropKa to estimate the pKa of residues and assigned the protonation states based on this. What pH was considered in the simulations? Was the propKa analysis run considering how choices in the protonation state of neighboring residues affect the pKa of the other residues? This is critical because the interaction energies will greatly depend on the protonation state chosen. Was the pKa for the mutant constructs re-evaluated? For example, does having a Gln or Arg in place of a His affect the pKa of nearby acidic residues? (Altered desensitization in H98R could be explained by perturbed pKa of nearby E107/D109 in addition to (or instead of) reduced interaction strength between the 98-109 side chains.)

2.2. The experimental data suggests that H98, E107, and D109 play analogous roles in PAC desensitization. However, the MD simulations suggest that the H98-D109 interaction energy is ~4 times larger than that of H98-E107. This should lead to a much greater effect of the D109 mutation. How is this rationalized?

2.3. The experimental data shows that E94 plays a key role in desensitization and the authors argue that this is due to the interactions of this residue with the β10-11 linker. However, the MD simulations show that these interactions happen for a small fraction, ~10%, of the time and with interaction energies comparable to those of the H98-E107-D109 cluster. It is not clear how these sparse and transient interactions can play such a critical role in desensitization. Also, if the interaction energies are of the same sign, how come one set of mutants favors desensitization and one does not?

2.4. Are 600 ns sufficient to evaluate sampling of the different conformations? The MD simulations should be extended beyond the 600 ns to increase sampling, ideally, multiple independent repeats should be carried out and analyzed at different pHs.

3. The underlying assumption in the interpretation of all the data is that the mutations stabilize or destabilize the desensitized conformation of the channel. However, none of the functional measurements provide direct evidence supporting this key assumption. The conclusions would be greatly strengthened if the authors could directly show that the mutations speed up or slow down the rate of recovery from the desensitized state. This should be feasible for most constructs as activation and desensitization happen at different pHs.

4. The reliability of the reported time constants of inactivation is questionable. For the reliable fitting of an exponential function, a time course at least 2-3x longer than the time constant itself must be fitted. In many cases, the presented time courses are too short to afford an exponential fit. E.g.: Figure 2B (H98R, E107R); Figure 3B (WT at pH 4.6 or 5.0, E94Q at pH 4.6 or 5.0); Figure 4E (H98R, E94R/H98R); Figure 5 (WT at pH 4.6 or 5.0, D91N at pH 4.6 or 5.0); Figure 6B (E250R).

Reviewer #1 (Recommendations for the authors):

1. I am concerned about the reliability of the reported time constants of inactivation. For the reliable fitting of an exponential function, a time course at least 2-3x longer than the time constant itself must be fitted. In many cases, the presented time courses are too short to afford an exponential fit. E.g.: Figure 2B (H98R, E107R); Figure 3B (WT at pH 4.6 or 5.0, E94Q at pH 4.6 or 5.0); Figure 4E (H98R, E94R/H98R); Figure 5 (WT at pH 4.6 or 5.0, D91N at pH 4.6 or 5.0); Figure 6B (E250R). The normalized surviving current fraction after 30 s is a simpler and more reliable parameter – maybe it would suffice for supporting the authors' conclusions, even if reliable time constants cannot always be extracted from the data.

Reviewer #2 (Recommendations for the authors):

Overall, this is a nice study with well-done experiments. Interpretations of the data seem largely reasonable, though some questions remain about exactly how to reconcile structural and functional data and the precise molecular mechanisms underlying desensitization. I have several comments that could improve the interpretability and accessibility of the study for a general audience.

1. The major issue is that important regions for desensitization are implicated when the model would be much more complete if specific protonation events involved were identified or at least clearly hypothesized. Can one say definitively that additional protonation events after opening are required as indicated in the model figure? Are they on residues implicated here? Several additional mutants could be evaluated to address this: (1) E107Q, (2) D109N, and (3) E107Q/D109N to explore protonation of the acidic pocket and (4) E249Q, (5) E250Q, and (6) D251N to explore protonation of the beta10-11 linker (in addition to charge reversal mutations presented). In addition, predicted pKas in wild-type and mutant structures for the relevant acidic residues could be presented to guide possible protonation mechanisms and explain mutant effects. For example, altered desensitization in H98R could be explained by perturbed pKa of nearby E107/D109 in addition to (or instead of) reduced interaction strength between the 98-109 side chains.

2. Related to 1, the model figure 7 would benefit greatly if protonation states of residues (or groups of residues) are indicated, especially as previous work has implicated residues in different processes.

3. I do not understand the explanation provided for the difference between the properties of endogenous PAC and overexpressed PAC in a PAC -/- cell line, which is substantial. Why should overexpression (resulting in ~4x current density) results in a higher degree and faster rate of desensitization? This is an interesting difference to point out even if the reason for the difference is unclear.

4. A brief discussion further connecting the structure papers with this work would help with context. How do the proportions of open, closed, and desensitized structural states at high and low pH values (refs 17,18, Deng et al. Sci. Adv. 2021) match the expected distribution based on the recordings here? Can the authors explain discrepancies in different conditions (e.g. detergent vs nanodisc)?

5. Line 212 appears to include a typo. Residue107-249 intersubunit and 250-297 intrasubunit interactions are observed in PDB 7SQH.

6. This sentence may be misworded. "Specifically, mutations predicted to stabilize the low-pH non-conducting structure (H98R, E107R, D109R, and E250R) greatly reduced channel desensitization; on the other hand, those predicted to destabilize it (E94R and D91R) produced the opposite effect (Figure 7)." H98R, E107R, D109R, and E250R should destabilize the desensitized state to reduce desensitization.

7. Figure 7 legend: does the model depict one or two subunits?

Reviewer #3 (Recommendations for the authors):

Suggestions:

I think it is critical to directly show that the mutations speed up or slow down the recovery from desensitization. This should be feasible for most constructs as activation and desensitization happen at different pHs.

The MD simulations should be extended beyond the 600 ns to increase sampling, ideally, multiple independent repeats should be carried out and analyzed at different pHs.

The effects of protonation choices on different should be evaluated.

The inconsistencies between electrophysiological results and MD simulations should be addressed and, if it is not possible to resolve them, then they should be acknowledged.

- I do not see a reduction of interaction energy and of distance with E107 in H98 vs 98R (Figure 2), as claimed in the text (pg. 7).
