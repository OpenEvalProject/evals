# Peer review - Round 1

Editors:
- Baron Chanda, University of Wisconsin-Madison United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.41653.045](https://doi.org/10.7554/eLife.41653.045)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The hydrophobic nature of a novel membrane interface regulates the enzyme activity in voltage-sensing phosphatase" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Richard Aldrich as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors show data in support of the role of two hydrophobic residues in VSP for regulating the phosphates activity of VSD. MD simulations show that two hydrophobic residues allow better contact with the membrane and that nearby hydrophilic residues prevent the insertion of the hydrophobic residues in the hydrophobic core of the membrane, so that there is some flexibility of the PD. Experimental results show that the hydrophobic nature of these residues promotes the phosphatase activity and also affects the VSD motion. The data and the story are convincing and complete.

Essential revisions:

1) Subsection “Retrograde effects of mutations in the hydrophobic spine on VSD motion”, second paragraph, "The normalized F-V relationship of L284F/G214C-TMRM shows that the fluorescence reached the -1 level over 100 mV as in WT/G214C-TMRM, whereas it did not reach the -1 level at greater than 100 mV in L284Q/G214C-TMRM and F285Q/G214C-TMRM": I don't understand this sentence. You mean that the FV didn't saturate at voltage >100 mV for the mutants, but it saturated for WT?

2) Subsection “Retrograde effects of mutations in the hydrophobic spine on VSD motion”, fourth paragraph: Insert "for WT", because you are not measuring at the peak for mutants. It is not clear what you are quantifying by measuring at this time and why? Just to show it is different at this particular time point?

3) Subsection “Retrograde effects of mutations in the hydrophobic spine on VSD motion”, fourth paragraph: You are mixing phases in time and voltage. What do you really mean at > 100 mV? Along the voltage axis the first two phases have already occurred at <100mV.

4) Subsection “Retrograde effects of mutations in the hydrophobic spine on VSD motion”, fourth paragraph: Is the third component the only one connected to coupling? If so, why is the first and second altered at V >100mV also?

5) Subsection “Analysis of the fluorescence of an unnatural amino acid, Anap, suggests two-step activation of the CCR”, second paragraph: This is not a clear description of what happens. A relative larger fluorescence signal at higher voltages (meaning that the F saturates at a less positive voltage) should give a leftward shift. As written right now, it sounds like there are two effects.

6) Discussion section, first paragraph, "provide high movability": It seems like it is the hydrophilic residues that provides mobility, not the hydrophobic residues which would anchor it more to the membrane.

7) Subsection “The hydrophobic spine controls the later transition of enzyme activation”, fourth paragraph: It is not clear how you distinguish between effect directly on VSD of mutations and retrograde coupling.

8) Subsection “Mechanistic insights into coupling between the VSD and CCR”, end of first paragraph: This sentence is not clear, tell what was found earlier and describe why or why not consistent with present data.

9) Subsection “Mechanistic insights into coupling between the VSD and CCR”, second paragraph, "membrane-tethered β2 subunit suggested that CaV binds": What are β2 and CaV? This is not explained.

10) Figure 11. What happens in VSD between middle and right panel? Should voltage do anything here? If so, shouldn't S4 move further out then?

11) No evidence for two different catalytic rates were observed. Multiple VSP states have been reported by other scientists, including a report from these authors (Sakata and Okamura, 2014), revealing two VSD states when testing VSD mutants but that publication does not show a difference in the catalytic activity. Experimental evidence for two catalytic states, low and high activity is needed.

(Below is the alternative suggested by the other reviewer:

I think to measure the catalytic activity with such precision as to be able to detect the low activity state is hard. This is because there will be a monotonic increase in the amount of VSP in the high activity state with increasing voltage and the voltage range for this increase and the voltage range for the proposed low activity is partly overlapping. One possibility is to have them remove the low activity of the intermediate state and just claim that the hydrophobic spine increases the catalytic activity by just altering the population in the high activity state. I don't think to explain their data, that it is necessary for their model to have the low activity in the intermediate state (it could just be no activity in the intermediate state). So my recommendation is to remove this if they don't have more data for the low activity. Removing this will not detract from the rest of their findings or conclusions.)

12) Both the Abstract and the Discussion emphasize a two state active model for VSP based on this data. While the Anap data clearly shows two states that go to one state with the Q mutations, the TMRM data is much less clear. Previous publications have all fit the G214C-TMRM data with a single Boltzmann. I would like to see residuals or other analysis that a double Boltzmann is required to accurately fit the data. I'm also concerned that two states in a fluorescence trace (whether TMRM or Anap) is interpreted as low and high activity state.

13) Regarding the interpretation of the electrophysiology and fluorescence, one of the conclusions the authors state is that there is a preference for aromaticity in the 284 position. Many of the comparisons between WT and L284F show that they are barely or only slightly different from each other. The hydrophobicity interpretation is a much stronger conclusion.

14) I have one concern regarding how the MD data is presented. Overall, description of the MD simulations was difficult to follow. I bounced back and forth between all of the supplementary figures to be able to understand how the experiments were done and how they were being interpreted. The low resolution of the supplementary figures made this more challenging as well. One aspect that confused me was the units. The MD simulations are in nm and the text in the Results section states binding was observed in Figure 2—figure supplement 2H for example. The "position from lower monolayer P atoms" for panel H range from -4 to -2 nm or -40 to -20 angstroms. The Materials and methods state that the binding is defined as -2 and -12 Å in the CG set. This range does not agree with the what is written in the Results section or the data. Is one of these units or values typos? Further explanation is needed to understand why the authors chose 0 and -4 Å for the AT simulations and another set of numbers for the CG set as well.
