# Peer review - Round 1

Editors:
- Lucy Forrest, NINDS United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.26985.024](https://doi.org/10.7554/eLife.26985.024)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Allosteric control of an asymmetric transduction in a GPCR heterodimer" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors and the evaluation has been overseen by Richard Aldrich as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Dmitry Veprintsev (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript reports an investigation of the allosteric control between subunits in a heterodimer of metabotropic glutamate receptor 2 and 4, using an elegant and ingenious quality control system that assures surface expression of only the intended dimers. The study reports asymmetric activation of dimeric metabotropic glutamate receptors, such that if a mGlu2 subunit is present, mGlu4 is responsible for the G protein activation in the heterodimer. By using subtype specific agonists, as well as swapping the extracellular domains between the subtypes, the authors were also able to show that it is possible to activate signaling by the heterodimer via activation of the mGlu2 extracellular domain. Using constitutively-active cross-linked extracellular domains the authors also demonstrate that no matter how the extracellular domains are activated, it is the mGlu4 that is responsible for signaling.

Essential revisions:

The reviewers are enthusiastic about the manuscript. However, they raise a number of concerns that must be adequately addressed before the paper can be accepted.

1) Two of the reviewers raise serious doubts about the interpretation of the molecular dynamics simulations. These concerns can be summarized as: (1) the fluctuations of loop regions in a homology model during a simulation could have many origins unrelated to the activation mechanism, and since appropriate methodological details were not provided [the sequence identity of the template; the final alignment and curations of the alignment; the loop lengths and templates; structural reliability measures for those segments; providing the model as supplementary material], it is not clear that the models are sufficiently reliable in these regions to avoid such artifacts; (2) even if the models were reliable, it is entirely possible that differences in fluctuations of ~1 Å would not be robust to repeated, parallel simulations (n>1); and (3) critically, the underlying assumption that asymmetric dynamics in a dimer should be detectable as fluctuations on the timescale of microseconds in the monomer is speculative. For these reasons, this section of the manuscript should be removed before resubmission, and the conclusions adjusted accordingly.

2) The overall message of the manuscript should be communicated more consistently throughout the manuscript. In particular, from the data and from the discussion it is clear that some conformational change, but maybe not the full activation of mGlu2, is required for the allosteric activation of the mGlu4. In other places (abstract, end of introduction) this effect is described too simplistically as 'negative cooperativity'.

In addition, the statement in the abstract: 'revealed a dynamics "winner-take-all" mechanism in mGlu heterodimers, providing new insight on the allosteric control between subunits in a GPCR dimer’ implies some kinetic aspects and time-resolution of the measurements while no kinetic measurements were presented. Rewording this statement could help avoid confusion.

3) Cell-surface expression levels are not always clearly reported. Statistical analysis of the expression levels would aid in interpretation of the results, specifically in Figure 1—figure supplement 2 and Figure 2—figure supplement 2 and 3. Similarly, in Figure 1B, cell surface expression is only statistically compared with mock and not among the different heteromers. In this case, the data look similar, but this does not seem to be the case for several of the supplemental figures (see below).

4) Figures 1, 2, 4 and 5 show the same type of data but use different Y axes (Fluorescence units or fold change over Mock, or normalised to the highest value). This makes it difficult to compare the experiments. It would be better to use the same Y axis – whichever is the most informative.

5) Figure 1C and F – the signal amplitude for the 2-4 heterodimer seem to be inconsistent on these two panels while it is consistent on others.

6) Figure 4A and B – The data presented are inconsistent with the previously presented data (compounded by the use of a different normalization along Y) and with the statement that the signaling is mediated via mGlu4. In the presence of NAM and a deactivating mutations signaling was observed. Panel D: are the differences in Ca2+ release between the two different 2-4 heteromers statistically significantly different? And if so: what could be an explanation for this (it seems that the inhibition of Ca2+ release is less profound when CRD is also from mGlu2)?

7) A more in-depth discussion of the following results is required:a) While it is concluded that the allosteric control of signaling is mediated via the 7TM domains, it is also worth discussing the possibility that some allosteric control could be mediated via the 7TM-VFT1-VFT2-7TM path, and only via the direct 7TM-7TM path. Three must be bi-directional allosteric connections between the 7TM and the VFT domains, and the allosteric coupling between the individual VFT domain has also been shown by the authors themselves.

b) In Figure 1C: glutamate has a lower efficacy at mGlu4-4 compared to 2-2, 2-4, 4-2. Is that because 2 positively affects 4? This matter is not discussed. The high efficacy (Ca2+ release) of 2-4 and 4-2 in Figure 1C is not seen in Figure 1F.

c) In Figure 1D: why does mutation of one of the two monomers in mGlu2-2 lead to a larger decrease in glutamate efficacy than in mGlu4 dimers? Does mGlu2-2 couple to 2 G-proteins to reach highest activity, in contrast to mGlu4-4, 4-2 or 2-4 for which coupling to 1 G-protein is sufficient? Again, the use of different y-axes complicates ready comparison.

d) In Figure 1—figure supplement 3 C: why are there differences between 2x-4 and 4-2x? Could this be due to differences in expression level?

e) In Figure 2: the receptors consisting of VFT and CRD derived from mGlu2 consistently show a higher Ca2+ release. This fact is not discussed.

f) In Figure 3, it is not clear why IP accumulation is monitored in this particular experiment as opposed to Ca2+ release in the others.

g) In Figure 3—figure supplement 1, there are differences in expression levels: do they correlate with efficacy?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for submitting your revised work entitled "Allosteric control of an asymmetric transduction in a G protein-coupled receptor heterodimer" for consideration by eLife. Your revisions and responses have been reviewed by a Reviewing Editor, and the evaluation has been overseen by a Senior Editor.

We are willing to accept the manuscript for publication, provided that the molecular simulations are excluded. Although the nominal accuracy of the models on which the simulations are based appears to be reasonable (50% identity, high coverage), thereby addressing one of our previous concerns, it remains questionable whether the conclusions extracted from these simulations are sufficiently robust and convincing. The fundamental claim that microsecond-scale fluctuations of these two intracellular loops relate to the activation of a ligand-bound dimer is speculation – particularly for an apo, monomeric receptor. Critically, this claim is also not convincingly supported by the simulation data provided, based on the information added to the revision. Only one MD trajectory was calculated for the mGlu2 model, and although the trajectories are 5 microseconds-long, analysis of RMSD versus time shows the models continue to drift away from the starting structure throughout the simulation; therefore, it is unclear whether the observed fluctuations reflect functional dynamics or inaccuracies of the models. Indeed, no molecular explanation is given as to why one protein is "more dynamic" than another, leaving open the strong possibility that this difference owes to the differences in the quality of the models or how the simulations were set up or conducted. On top of this, the simulations include an apo monomer, rather than a ligand-bound dimer whose actions are being monitored in the experiments. In summary, the molecular simulations are insufficient to support the hypothesis put forward, and the relevance of the observations is too tenuous. It is our opinion that the speculation of the underlying mechanism for activation of mGlu4 vs mGlu2 is equally plausible without the simulations.

– There is a typo in the revised abstract: "their role in receptor remains elusive" (insert signaling)

– There is no reference to rat mGlu2 being used in the abstract, as indicated in the response regarding the title.

– In the Discussion section: The phrase: "the consequence of the mGlu4 ECD dimer", is confusing and possibly incomplete, since it refers also to data relating to mGlu2.
