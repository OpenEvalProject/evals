# Peer review - Round 1

Editors:
- Nir Ben-Tal, Tel Aviv University , Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.16616.016](https://doi.org/10.7554/eLife.16616.016)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Binding site protonation and self-correcting occlusion control the Na+/K+-pump selectivity" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Erik Lindahl (Reviewer #3) and Nir Ben-Tal (Reviewer #1), who is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Richard Aldrich as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The study examines the physicochemical determinants of binding site selectivity in the Na+/K+-ATPase using molecular dynamics simulations. Various conformation of the ATPase, corresponding to different states along the pump cycle are examined, including the crystal structures of its two main conformations, as well as several models of intermediate states based on the Ca2+ SERCA pump, and models derived from interpolating between well-defined states. Various protonation states of titratable residues in the pump's binding sites are energetically examined using molecular dynamic simulations as different resolutions. The results suggest that the protonation states of three aspartate residues in the binding sites (D804, D808 and D926) alter upon switching between conformations. The results indicate that the different selectivity of the binding sites emerges from the change in the protonation states. Using reduced structural models of the binding sites, this hypothesis is supported by calculating the difference in free energy between the pump bound to Na+ vs. K+ ions along the transport cycle. The authors conclude that initially the binding sites are only weakly selective for either Na+ or K+, and selectivity emerges as collective effect due to the (indirect) interaction of new ions with the ones that are already bound (a knock-on effect); the pump shifts towards K+ selectivity in the outward open state, and towards Na+ selectivity in the inward open state. Binding of the wrong type of ion increases the free energy barrier towards occlusion, preventing the transport cycle to proceed, thereby preventing the pump from operating in the opposite (wrong) direction.

The manuscript addresses an interesting and important question. It proposes a simple mechanism that dictates the shift in the selective properties of the Na+/K+-pump binding sites. However, based on the current draft of the manuscript it is difficult to decide whether the work is novel and solid enough to justify publication in eLife. The summary reflects a long discussion among the reviewers in an effort to resolve this. The author should submit a revised draft only if they are certain that they can address all the issues raised.

Essential revisions:

1) It is difficult to figure out which structures the various steps in Figure 5 are based on. Perhaps:

State 1 and 9 correspond to 3B9B (open SERCA);

State 2 calculated transition to;

State 3 corresponds to 1WPG (occluded SERCA) – but why not 2ZXE (occluded NKA)?

State 4 calculated transition to;

State 5, unclear: called K2E1. Maybe 1VFP with different protonation pattern and K instead of Na?

State 6 corresponds to 1VFP (Ca occluded SERCA) – but with K rather than Na?

State 7 corresponds to 3WGV (occluded NKA);

State 8 calculated transition to 9;

The authors should make perfectly clear which structures are used for which states.

2) The pump cycle should be based on all the relevant structures. Structures have been published of SERCA in E2 (3W5C) and the open ready-to-bind Ca (4H1W) in 2013. These important steps are missing here, or guesses are attempted based on the Ca-occluded 1VFP structure, but that did not predict the structure for H and Ca exchange. The structures are not mentioned. (A nice and recent overview of P-type structures can be found here http://www.ncbi.nlm.nih.gov/pubmed/26695058).

Also, it would be preferable to use 4HYT (ouabain-bound NKA, mentioned as recent but it is from 2013) rather than 3B9B. At least the authors could show an overlay of the ion binding sites from 4HYT and their model.

3) Standard errors estimates should be added to the energy values, and conclusions that have been based on energy values with too large 'error bars' should be reconsidered.

4) If the calculations correctly describe the binding free energy of the pump cycle, they would also need to explain the ion release on the opposite side. Can they show this?

5) The simulations and free energy calculations assume a starting point in which all the pump's binding sites are occupied by a certain set of ions. The authors explicitly claim that selectivity emerges from the increased free energy barrier associate with binding of the wrong ion to a site. However, from a biological point of view to argue that selectivity is governed solely by such mechanism is puzzling, for it is inefficient. The mechanism proposed here beautifully explains the different selective properties of the pump's binding sites in its two conformations, and it is possibly a "last resort mechanism", designed, as the authors claim, to prevent the transport of the wrong kind of ion if it reaches the binding site. However one would expect that for the most part, under physiological conditions, the pump will prevent the wrong ions from reaching the binding site to begin with. The anticipation is that a fast machine, such as this pump, should follow a particularly efficient mechanism, rather than the one proposed here, which figures out that there is issue with selectivity only after binding of several ions of the wrong type. The manuscript does not account for the ions transition into the binding sites and other possible energetic barriers they might encounter on the way. This issue should, at the very least, be discussed.

6) In view of item 5, the authors should revise the title to reflect the fact that selectivity is presumably determined primarily by other mechanisms, and the suggested mechanism here is only a 'safe guard'.
