# Author response - Round 1

Authors:
- Andrew John Knappenberger ([ORCID: 0000-0003-2659-4305](https://orcid.org/0000-0003-2659-4305))
- Caroline Wetherington Reiss ([ORCID: 0000-0002-6385-1879](https://orcid.org/0000-0002-6385-1879))
- Scott A Strobel ([ORCID: 0000-0001-8402-4226](https://orcid.org/0000-0001-8402-4226))

## Response text

DOI: [10.7554/eLife.36381.030](https://doi.org/10.7554/eLife.36381.030)

Reviewer #1:

[…] Overall, the work is very interesting and should be of broad interest to the journal audience. However, there are some technical details regarding the assignment of the ions and orientation of the PPRP effector that should be addressed to provide greater confidence in the crystallographic model. Another point of concern is citing unpublished or "in press" work, which may not agree with the journal policy.

1) Introduction, second paragraph and throughout the manuscript, the authors make reference to Sherlock et al. in press as two separate manuscripts. Please provide the "Sherlock et al. in press" manuscripts with more complete information (i.e., all authors, title, journal). Since there are two manuscripts, they need to be distinguished as 2018a or 2018b, or by the appropriate journal style.

2) Introduction, fourth and fifth paragraphs, and elsewhere. The authors refer to "Sherlock et al., unpublished." This may not conform the journal guidelines for citations. The reviewer objects to citing unpublished work because it is not a rigorous source of information that is transparent for the journal readership.

One significant issue raised by the reviewers and the editors was the status of the work cited from the Breaker lab. We are happy to report that the two Sherlock et al. papers referenced in our work have been accepted by eLife and PNAS. This enables us to properly cite their work in this revised manuscript. Sherlock, Sudarsan, and Breaker 2018 is not yet available online as of our re-submission, but it is expected to appear in the very near future.

3) Supplementary file 1. The reviewer has a number of suggestions to improve the table.

First, the unit cell cannot be known to an accuracy of 1/1000th Å based on the mode of data collection. HKL2000 will report the errors and these could be indicated or the cell should be reported to 1/10th of an Ångstrom. The same is true of the angles.

Corrected.

Second, the reviewer recommends using Rp.i.m. instead of Rmerge. The former accounts for redundancy in the data collection and should replace the latter (see Karplus and Diedrichs (Curr Opin Struct Biol 34, 60) and Weiss (J. Appl. Cryst. 34, 130-135). This metric is also provided by HKL2000.

Rp.i.m. is now included in Supplementary file 1 in addition to Rmerge.

4) Figure 2. The mode of metal ion coordination is unclear based on the drawing. To clarify the scheme, please provide the name of the nucleotide atom in panel B that forms an interaction with PRPP. The underlying reason for this request is that the ligand could be modeled in a different manner in the electron density.

New supplemental figure (Figure 1—figure supplement 2) shows coordination distances to the three metals and the text now describes the ambiguities inherent in metal assignment at this resolution.

5) One aspect of the presentation that could be improved is to provide greater evidence for the orientation of modeled PRPP. Rotation of PRPP by 180° about the y-axis would place the pyrophosphate into M2. The reviewer noted this possibility prior to reading the 180° rotation of ppGpp in the ensuing section. In this respect, more should be done to explore this possibility as a supplemental figure. For example, compare the SA omit electron density for both orientations (or use averaged kicked maps or composite omit rebuild maps, which are likely the best – but slowest to run; use 2Fo-Fc coefficients). How do the Rfree values compare for each orientation? How do the real space correlation coefficients compare?

We modeled PRPP in the alternative orientation suggested by the reviewer. In this orientation, the Rfree rises from 0.2523 to 0.2537. It results in a short (2 Å) hydrogen bond between PRPP and the N1 atom of G6, and forces two non-bridging oxygens in the pyrophosphate into implausibly close proximity (1.8 Å) with one another. All indications are that this is not the correct orientation of the molecule within the RNA.

6) It is unclear what metal ions are present in sites M1, M2 and M3. These are stated to be consistent with Ba2+ (subsection “The structure of the wild-type PRPP aptamer and a single point mutant ppGpp aptamer”, seventh paragraph) but actual distance information and geometry should be provided. Why? It seems unusual that Ba2+ would bind in place of Mg2+ since the latter has significantly shorter coordination distances and distinct octahedral geometry. Mg2+ is the expected intracellular ion of course. Anomalous scattering from Ba2+ might help to more definitively model the ions, which is still difficult to define at this resolution. In these respects, the coordination distances between the ions and the ligands should be mentioned. (the aforementioned paragraph notes the coordination of M2 is consistent within inner sphere coordination. Please be more specific). What are the B-factors of the Ba2+ ions? If they are modeled as Mg2+, are they unreasonably low? If another contour level is add to the maps, is the s-to-n consistent with Ba2+ (e.g., 10 σ or greater peaks).

7) The observation of Ba2+ in the complex with PRPP suggests that the ion should be sufficient for binding in equilibrium dialysis experiments. The experimental methods describe the use of Mg2+ (subsection “Determination of dissociation constants by equilibrium dialysis”, first paragraph) Was Ba2+ tried? If Ba2+ showed binding, this could be a stronger case for the observation of the assignment of Ba2+ in the electron density maps. The reviewer realizes that these are not easy experiments, so analysis with Ba2+ may not be feasible. Why not use isothermal titration calorimetry?

We thank the reviewer for raising this important point. We have carefully reviewed the metal assignments for M1, M2, and M3 within the PRPP structure. Because there is a mixture of divalent metals in the crystal condition (both Mg2+ and Ba2+ are present), partial occupancy is a potential complicating factor. Both Mg2+ and Ba2+ support PRPP binding and do so at similar affinities (see above). The data support the assignment of M1 and M3 as having significant occupancy by Ba2+. Assignment of M1 or M3 as magnesium result in very large positive peaks occur in the Fo-Fc map. Upon closer inspection, there is reasonable case to be made for assigning M2 as Mg2+. Although coordination distances (~2.8 Å to 3.0 Å) are longer than expected for Mg2+, the B factor (64 Å2) and difference map are reasonable. All three sites are likely to be partially occupied by both Mg2+ and Ba2+ which complicates the assignments. A sentence to this effect has been added to the text.

Reviewer #2:

[…] 1) The I/sigmaI values reported for each structure are on the low side (1.27 for PRPP and 0.67 for ppGpp) and the difference between Rfree and Rwork for each structure is on the high side. Perhaps the structures have been refined to an artificially high resolution.

We used a combination of the CC1/2 and the point at which the slope of the Wilson plot approaches zero to assign cutoff points. We used the widely accepted CC1/2 value of 0.15 to cut the data.

Furthermore, both structures appear to be missing portions of the chain.

These nucleotides are disordered in the structure so we did not model them.

2) The authors should cite the paper by Battaglia et al. describing the structure of guanidine-I.

We particularly thank the reviewers for catching this omission. The citation has been added.

Reviewer #3:

[…] 1) Compound identity for synthesized PRPP and ppGpp. This is not a chemistry journal, but how did authors validate compound identity? Because "riboswitch binds synthesized compound, therefore compound identity is X" would be circular reasoning. Is the resolution high enough to serve as validation of ligand identity? Also was wondering if resolution was high enough to show that ligands were not hydrolyzed in the structure, e.g. GMP+PPi instead of GTP is common.

PRPP was purchased from Σ Aldrich and validated by the company. ppGpp was made using previously established methods and verified by comparison of anion-exchange retention time with a ppGpp standard (purchased from TriLink BioTechnologies). A supplemental figure has been added to show this validation (Figure 6—figure supplement 3).

2) "A common ancestral RNA likely diverged to recognize guanidine, PRPP, and ppGpp in spite of the chemical and structural diversity among these ligands" This line is too speculative. What evidence do you have that one became three, vs. first was guanidine, then branched to two new, or vice versa?

We did not intend to suggest an order of divergence between these RNA classes. The text has been revised to clarify this point.

3) Figure 1—figure supplement 1 – "PRPP" control sample, how was this sample treated? It is unclear if it was treated under same reaction conditions, although text suggests PRPP would be totally degraded under those conditions (but not shown?)

Explanatory text has been added to the legend of Figure 1—figure supplement 1.

4) Figure 2 – Results text state that M3 "forms a water-mediated coordination to the 5-phosphate" but this is not shown in B?

Added.

5) Figure 6C – does resolution allow for assignment that there is no ion or water bound in the guanidine/metal pocket shown?

We do see ions and water molecules in this area, but they are too distant to be true coordination or hydrogen bonding contacts. Positioning of these species varies among chains in the asymmetric unit.

6) Discussion: It should be made clear that this study does not demonstrate that the G96A mutation is sufficient to alter gene regulation in vivo, although the aptamer selectivity is altered. See Mandal and Breaker 2004 for precedence. Along these lines, what is the range of% identity for natural PRPP and ppGPP riboswitches? This would be helpful to know.

Done.
