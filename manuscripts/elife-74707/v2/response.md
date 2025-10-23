# Author response - Round 1

Authors:
- Juan Feng
- Xianchi Dong
- Adam DeCosta
- Yang Su
- Fiona Angrisano
- Katarzyna A Sala
- Andrew M Blagborough ([ORCID: 0000-0002-5257-8475](https://orcid.org/0000-0002-5257-8475))
- Chafen Lu ([ORCID: 0000-0002-3954-4836](https://orcid.org/0000-0002-3954-4836))
- Timothy A Springer ([ORCID: 0000-0001-6627-2904](https://orcid.org/0000-0001-6627-2904))

## Response text

DOI: [10.7554/eLife.74707.sa2](https://doi.org/10.7554/eLife.74707.sa2)

Essential revisions:

All three reviewers agree that this is an interesting and important study, and that the work is very well conducted and presented. They also identified a number of points, as detailed below in the recommendations to the authors, which could be addressed in the text to strengthen and/or clarify the manuscript, without the need for additional experiments. Specifically, the reasons for discrepancy between binding to the recombinant ectodomain versus the native protein on gametes for the non-neutralizing mAbs could be discussed in more details. It could be due either to how the parasites are treated or due to the state of the ectodomain, as suggested by the observation that a fraction of the protein binds with good affinity, while a larger fraction doesn't.

We have banged our collective heads against the wall trying to come up with a clear explanation (the PI's head is the most damaged) and cannot. All we can do is speculate. We do two things in Discussion. Instead of asking the question about why the discrepancy is present at the end of one paragraph, which may lead readers to expect an answer in the next paragraph, we delete that question and start the next paragraph by saying that we all we can do is speculate and offer one possibility at the end of that paragraph.

Reviewer #2:

[…]

In the introduction, where the authors write "To mediate fusion, D3 of HAP2 folds over an inner trimeric core composed of D1 and D2 (Figure 1).", is this a proposal or model? If it has been proved, please cite the paper. If not, please indicate that this is a proposal.

The whole conformational change was cited (a review) in the previous sentence.

In Figure 4A there is no structure shown for the two complexes – only opened up structures. This seemed strange and not intuitive. Could the structures of the complexes also be shown? Without this, it is very hard to understand how the two epitopes relate to each other from what is shown.

Thanks for pointing that out, we have added the two complex structures in the Figure 4A.

The authors also do not show the sulphate ions which they see in one of the structures. These ions appear to link the epitope and the antibody. How do they know that these are sulphate ions and are they likely to be physiologically relevant?

"The Fab 2/1.12 complex (4.5 mg/ml) was crystallized with 0.2 M ammonium sulfate, 25% PEG 3350, 0.1 M Bis-Tris pH5.5." These ions are highly unlikely to be physiologically relevant.

It would be good to move Figure S6 into the main manuscript as it helps explain develop a model for how the antibody works.

We do not know how the antibody works- It could work through blocking conformational change or it could simply opsonize the gametes for phagocytosis or it could agglutinate them.

The number of clashes and RSRZ outliers are high for a 2.1Å structure for 7LR4. For 7LR3 the number of RSRZ outliers and Ramachandran outliers are both high. These structures appear to require more work in refinement.

My groups prides itself in refinement. We are one of the few groups that reports MolProbity statistics in our crystal statistics tables. These show that our structures are in the 97-99th percentiles of all structures in the pdb of similar resolutions for clashes and geometry (which includes Ramachandran outliers). Thus the quality of our refinement is outstanding. Our style of refinement (and we usually push resolution more than others, because we do not throw out useful data, as recommended by Diedrichs and Karplus) tends to give high RSRZ outliers. We tend to build the mainchain through weak but continuous density and we do not truncate sidechains. This takes more care in refinement, provides a more useful model for biologists, but also gives higher RSRZ outliers. Additionally, the 7LR3 complex was difficult to refine as explained in Methods:

"During model building and refinement of the 2/6.14 Fab complex, the Fab constant domains of one complex had good density, but the variable domains and D3 had broad but continuous density that was difficult to trace. In contrast, all domains of the other complex were easily traced. Furthermore, refinement remained stuck. Alternative space groups including those with lower symmetry or use of twin rules provided no improvement. We then realized that in the troublesome D3-Fab complex in the asymmetric unit, two alternative conformations were present for D3, VH, and VL, whereas CH1 and CL had a single conformation. The transition between dual and single conformations occurred at the elbows between VH and CH1 and between VL and CL; i.e. the two conformations differed in elbow angle. In further refinement, the resolution cutoff was changed from 2.4 to 2.8 Å, and we largely treated each of the dual conformations of D3, VH1, and VL as rigid bodies based on their structure in the single conformation of the other D3-Fab complex."
