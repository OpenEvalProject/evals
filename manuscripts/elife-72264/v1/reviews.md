# Peer review - Round 1

Editors:
- Qiang Cui, Boston University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72264.sa1](https://doi.org/10.7554/eLife.72264.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Proton-mediated gating mechanism of anion channelrhodopsin-1" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Qiang Cui as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by José Faraldo-Gómez as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Several reviewers raised concern in using the HOMO-LUMO gap to model the absorption maximum instead of state-of-the-art QM/MM methods based on, for example, TD-DFT or ab initio methods. This should be possible for the current system considering the modest size of the QM region.

2) Essentially all reviewers are concerned about the statistical errors associated with the reported simulation data. These should be analyzed carefully and reported explicitly.

3) One reviewer highlighted the importance of examining an alternative protonation state of the system [E68(-)/D234(H)].

4) As one reviewer noted, the title of the manuscript implies insight into the "gating mechanism" of GtACR1, but it was actually never simulated like, for example, in the work from Ardevol and Hummer https://www.pnas.org/content/115/14/3557. Instead the conclusions about the gating mechanism are based on simulations of the resting state of the protein. You explained that the actual channel function is correlated with later intermediates of the photocycle (Figure 2 in the manuscript). However, already in the first intermediate the retinal changes the conformation thus the protein conformation might change, which could impact the distance to E68. Therefore, it is important to discuss the mechanistic implication of using the ground state structure in the computational analysis.

Reviewer #1 (Recommendations for the authors):

Overall, the authors did an excellent job in combining different computational methodologies to address the issue of residue titration states in proteins.

Reviewer #2 (Recommendations for the authors):

1) One of the major concerns is that the authors use HOMO-LUMO energy difference to compare them to experimental absorption maxima. A HOMO-LUMO energy gap is not an excitation energy and not the absorption maximum. The main conclusions in this paper are based on these calculations. Therefore, I am concerned about the reliability of the results. To improve it, there is a wide range of methods that can be used instead. I don't mind if the authors use TD-DFT or wave function methods as long as excitation energies are computed.

2) The authors report that 10 geometries were used for HOMO-LUMO gap computation and then averaged. However, the numbers are not shown anywhere. I would like to ask to list it in the SI. It would be for example interesting to see the fluctuation of the values because the differences between the different mutants are rather small.

3) The discussion of the gating mechanism is done on the basis of the dark state structure (Figure 5 and 6), i.e. the retinal is not isomerized and the protein conformation didn't change. So there is some uncertainty in the prediction of the gating mechanism which should be mentioned and discussed.

4) There is very little or no data from the MD trajectories which are used to draw conclusions about the protonation states. For example the RMSD from each trajectory as well as critical distances. This can be also added to the SI.

5) The main conclusion is that Asp234 is deprotonated because the D234E mutant is blue shifted. But this can also be explained by the ability of the protonated D234 to form hydrogen bonds with the Schiff base. Then the closer proximity of E234 would also result in a blue shift.

6) Also the fact that D234E/E68D double mutants is red shifted by only 7 nm can explained by the fact that in D234E the residue E68 is closer to the Schiff base but in the double mutant both are neutral. In addition, the shift is of 7 nm is rather small.

7) In several places the authors mention the similarity between the electrostatic potential in bR and GtACR1. However, bR has a second counter ion (D85) and GtACR1 has a neutral residue in this position. This is close to the Schiff bas region and is therefore important. So I recommend to rethink this phrasing.

8) How can E68 accept a proton in the wild type if it is protonated?

Reviewer #3 (Recommendations for the authors):

This is interesting work and I support its publication following revision. My concerns and suggestions for improvement are:

1) It is clear that one of the acidic residues, E68 or D234, must be deprotonated in order for the Schiff base to be protonated. However, the paper would be improved by a more thorough comparison of the interplay or exchangeability of E68 and D234. In many of the analyses, the authors only compare E68(H)/D234(-) to E68(H)/D234(H). They do not test E68(-)/D234(H)-e.g., MD simulations in Table 1, pKa values in tables 2 and 3, and the calculated spectroscopic shifts in table 4. The mutant results for D234N already suggest that E68 can take D234's role in stabilizing the protonated Schiff base. However, this mutant should not take the place of the wildtype system with E68(-)/D234(H). As emphasized in their concluding paragraph, Asp and Asn can behave differently.

2) For example, focusing on the measured shifts in absorption wavelengths (Table 4), mutating either residue to the opposite acidic residue (i.e., E68D and D234E) results in a decrease in wavelength. Similarly, mutating either to neutral (E68Q and D234N) results in very little shift (+2 and -3, respectively). Is this difference significant or within error of being equivalent? If the latter, why is it that the authors conclude only E68(H)/D234(-) is present in the room temperature wild type system? Couldn't E68(-)/D234(H) be a contributing species? Similarly, the authors could have calculated the shifts for E68Q in both the protonated and deprotonated forms of D234 (Table 4).

3) Focusing on pKa calculations, which will clearly hold their trends for the crystal structure, the pKa of E68 should also be measured post simulation and relaxation of the E68(-)/D234(H) state.

4) An additional concern is the lack of reported error bars. The magnitude of error should be reported for each quantitative calculated and measured result. This is essential to discern which conclusions are statistically supported and outside of their measured or calculated error bars.

5) It would help the reader to clearly delineate what is new in this work and what has been previously reported. It seems only the absorption of E68Q/D234N is new? What conclusions are new?

6) The final concluding paragraph about the influence of Asp to Asn mutations does not seem well supported by these findings. In this presented case there is a functional change due to the D234N mutation, even though there is little change in absorption due to compensating D68 deprotonation. This conclusion should perhaps be reconsidered/reframed. If kept as is, the motivation based on the reported findings needs to be more clearly explained.

7) The DFT used in the QM/MM was fairly basic (B3LYP with 6-31G* basis sets). How was this choice justified for the given system? I.e., to what higher level theory and larger basis sets was this compared to in order to verify it works well enough for these calculations?

8) Line 311 on page 17 replace ', which are caused by…asparagine,.…' with 'that are caused by.… asparagine.…' removing the commas since the clause specifies the subject-it is not additional information about the subject.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Proton transfer pathway in anion channelrhodopsin-1" for further consideration by eLife. Your revised article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by José Faraldo-Gómez as the Senior Editor.

Editors and reviewers concur that the manuscript has been improved; however, there are some remaining issues that must be addressed or clarified before the manuscript can be accepted for publication, especially about the TD-DFT calculations and MD simulations for the pKa evaluations. We urge you to provide a compelling resolution to these issues.

Reviewer #1:

The authors included additional TD-DFT calculations, and also sampled more configurations as well as protonation patterns. They have also clarified a few questions raised in the last round of review. In my opinion, the revision is acceptable for publication in eLife.

Reviewer #2:

1) The authors have provided TD-DFT results, following the suggestion from all three reviewers. The results are qualitatively similar to the HOMO-LUMO energy gaps. But there is one important difference. The structure with Cl- is blue shifted with respect to the parent state at the TD-DFT level, while it is red shifted when the HOMO-LUMO energy gap is used for the calculation of excitation energies.

A comparison of the differences in orbital energies to absorption maxima is physically incorrect (also pointed out by other reviewers). Therefore, I recommend the authors to add the TD-DFT results to the table 4 in the manuscript.

2) I appreciate adding the excitation energies from the 10 snapshots of each GtACR1 variant. It shows that the wide distribution for E68D agrees with the wide band from experiment. Maybe this is due to some heterogeneity in the structure. It would be interesting to check this.

3) It is not clear how the authors know that the M intermediate is the conducting intermediate in GtACR1. As far as I know the structure of the M intermediate is also not known for C1C2, the artificial chimaera of channelrhodopsin 1 and 2. More importantly, it is not just the isomerization but also a conformational change in the protein which allows the pore formation. It is not clear how this is taken into account in the simulation. I'm not asking the author to redo the simulations, but simply inform the reader about this important differences.

4) The proton transfer is outside of my expertise. I thought the Grotthuss mechanism is proposed for a network of water molecules.

In addition to these replies, the use of a 0.01 fs time step for the numerical integration of the equations of motions in MD makes no sense. This is at least 50 times too small.

Reviewer #3:

My one remaining concern is that the length of the MD simulations in each protonation state should be stated and the method for selecting conformations from those simulations should be described. The reason for this is that the pKa calculations will be most dependent on conformation. Their conclusions hinge on (1) having run simulations long enough to stabilize each charge state, and (2) selecting a reasonable number of conformations that were representative of the stablilized ensemble. Ideally they would report the number of conformations they chose, how probable those structures were in the simulations (cluster and count based on positions of the important residues), and show a representative figure of the structures in the SI.

Other than this, I am happy with the author's revisions.
