# Peer review - Round 1

Editors:
- Toby W Allen, https://ror.org/04ttjf776 RMIT University Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80303.sa0](https://doi.org/10.7554/eLife.80303.sa0)

In this study the authors aim to describe the electromechanical coupling responsible for activation of a Hyperpolarised-activated and Cyclic Nucleotide-gated (HCN) channel. HCN channels are the only mammalian channels to open under hyperpolarisation, being important for their roles in cardiac and neuronal cells. The authors use enhanced-sampling atomistic simulations to enforce sampling between open and closed states of the channel. The simulations suggest state-dependent interactions involving pore and voltage sensor helices, as well as with lipids, leading the authors to propose a domino-like mechanism of activation. These findings will be of considerable interest to the ion channel community.


---

# Peer review - Round 1

Editors:
- Toby W Allen, https://ror.org/04ttjf776 RMIT University Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80303.sa1](https://doi.org/10.7554/eLife.80303.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Interplay between VSD, pore and membrane lipids in electromechanical coupling in HCN channels" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Richard Aldrich as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers were supportive of the work and appreciated the mechanistic insights. The main concerns needing to be addressed are listed below, with full details available in the reviews themselves.

1. The decision to model the open pore of HCN1 using homology with hERG has been questioned. Because the simulations depend critically on this open-state model, it requires validation. It has been suggested that a better choice would have been the available HCN4 open state cryoEM structure. It has also been stated that hERG could be problematic because it does not have a gating hinge in common with HCN and has other sequence differences (such as V390) that may impact the structure of the HCN1 model. The authors should try the HCN4 pore domain to see how such a homology model would compare to the one used.

2. Provide experimental evidence in the form of existing or new experimental data to demonstrate the accuracy of the current open-state HCN1 model that has been used to set the interaction distances to guide simulations. In particular, data is requested that can confirm the relevance of those interaction distances. Also, for D290 – K412, the validation is missing a control (effect of Cd2+ on wildtype).

3. Provide any available mutagenesis or other data that supports the importance of residues proposed to interact with lipids.

4. Provide analysis or additional simulation that can address concerns about the reproducibility of simulation results, given only 1 simulation that enforces the chosen simulation distances has been performed. Also, please provide statistical tests to demonstrate an increase vs decrease in key interactions.

5. Better explain and visualise the proposed mechanism referred to as a "domino effect".

Reviewer #1 (Recommendations for the authors):

I note that the low-resolution blurry pdf figures provided for review made the reading of details very difficult.

I must say the figures have not done a good job of explaining the so-called "domino" effect, and perhaps data can be presented alongside a cartoon to explain this, with the domino nature clearly explained, just as the "domino effect" has been explained clearly in pentameric ligand-gated channels, for example.

Additional comment/question regarding the D290-K412 salt bridge cysteine cross-bridging: Is it possible that this approach might capture rare conformations, where those cysteines may briefly come to within 8 Å and then bind for a long time, despite not being relevant to the wildtype functional state? Irreversible binding (on the experimental timescale) may trap unphysical conformations, reminiscent of what has been previously argued in relation to biotin-avidin experiments examining VSD movements (e.g. Jogini and Roux Biophys J 2007 93:3070), for example. It is not clear to me that the cross-link proves that a wildtype salt bridge is important for the activated state, and why in the main review I ask about possible other experiments to back it up.

Figure 3c shows some data for D290-K412. I note that supporting timeseries and violin plots like Figure 3C would be useful for all relevant distances, including N300-W281, V390-I302 and others noted.

Reviewer #2 (Recommendations for the authors):

This is a well-written manuscript on a hot topic. The study would attract many readers. But the figures are extremely unclear, the colors are not helpful, and the text in the figures is too small. There are also some other concerns that need to be addressed.

1. It is not clear why W281 was indicated as a very interesting residue. Is there something different about this residue compared to other residues in the channel? It seems to come out of the blue that this residue is especially interesting to study. Or figure 2 is maybe the true reason of the focus?

2. Figure 1. W281 interactions with 277-286: are these interactions intersubunit or intrasubunit? If intrasubunit, is it really interesting if neighboring sidechains on an α helix are interacting? Do they stabilize some conformation?

3. Pg. 6. "the Y289D mutant retains many characteristics of the VSD-pore interactions of the activated state". At this point you have only stated that W281 only interacts with lipids in the activated state, so what VSD-pore interactions are you referring to here?

4. "The wider distribution of bending angles in S4 for the system lacking the HCN domain indicates that the HCN domain may also contribute to stabilizing the activated state of S4 (Figure 2 —figure supplement 1B and 2F)." This is not clear in Figure 2 supp 1B or 2F.

5. Do you have any experimental data to support your proposed stabilization of the open state by the W281-N300 interaction? Or could it be validated in the MD by mutating them?

6. Figure 2 Suppl 2. Do you have any statistical test for the increase vs decrease of the interactions? Not clear to me of any consistent changes in some cases.

7. Pg. 15. "However, this distance decreases rapidly in the first few picoseconds of simulations" What simulation? Starting from what state?

8. Figure 3 Suppl 1. The channels should really be more closed by the C-C mutation if D-K stabilizes the open state, i.e. the voltage dependence should be shifted to more negative voltages and channels should be less open. Right now, the cys-cys mutation does the opposite, shifts the voltage dependence to more depolarized voltages and the channels are less closed (more leak currents). So, it is not really clear that a D-K interaction really stabilizes the open state. Could it be that cyc-cys +Cd2+ stabilizes the open state (because these residues are close in space), but D-K does not stabilize the open state even if they are nearby each other?

9. Figure 4 Suppl 3. I cannot see the proposed increases and decreases in S6-S5 and S6-S6 interactions, respectively. Is there some statistics or number to bolster these claims? Should not the ABMD curve go from resting towards the open state during the simulations? This is not always the case?

10. Figure 5A. I cannot see the proposed increase in lipid contacts on S5 and S6? Can you quantify something? Why not use the ABMD state instead of the activated state, since the activated state is not open?

11. The Domino effect is not very well explained. What is happening in the different steps during the domino effect, i.e. what step is first and why does this step cause the second step, etc…? Figure 6 is not clearly showing in a figure what you think is happening. Also, some residues and symbols are shown without any explanations: what do the arrows under "int" represent, and what are F and E?

12. The role of lipids in hyperpolarization-dependent gating is not well documented or described. How is this supposed to happen and how can it be tested? Not clear what H392-R297 and their lipid interaction are doing?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Interplay between VSD, pore and membrane lipids in electromechanical coupling in HCN channels" for further consideration by eLife. Your revised article has been evaluated by Kenton Swartz (Senior Editor) and a Reviewing Editor.

We do note, however, that the revised manuscript was seen by the past reviewers and they strongly recommend making a couple of changes summarised below.

Recommended changes:

1. The authors refer to the effect of a lipid on the salt bridge R297 and D401, recently identified in HCN2, as a general feature of all HCN (Schmidpeter et al. 2022. Nat. Struct. Mol. Biol. 29, 1092-11009). This evidence is questionable, as the salt bridge is not present and plays no role in other HCN subtypes, for instance in HCN4. Examination of the 4 structures of HCN in the closed state in databank, 2 from hHCN1 and 2 from hHCN4, there is no clear evidence of the salt bridge between R297 and D401 (HCN2 numbering). First of all, there is NO density for the side chain of D, so it cannot be modelled. Note that the absence of density is by itself a strong indication that it does not form a salt bridge. Aspartates are subjected to radiation damage and it is known that when their sidechains form a salt bridge they are preserved, otherwise they are damaged by the electrons during image collections. If, nonetheless, one wanted to model the side chain of D, in any case, the distance from R side chain is in all 4 cases >4 A, above the cut-off distance for a salt bridge. It is therefore recommended that the authors add a statement admitting the lack of evidence for the conservation of a salt bridge pair in HCN1 and HCN4.

2. Dai and Zagotta 2017 do not say anything about HCN channels, so this reference should be removed in most places.

3. Page 22. Yellen did not show H462-Q468C, but H462-L466C Cd2+ crosslinking. So this data does not support the bond equivalent to H392-Q398 that the authors propose.
