# Peer review - Round 1

Editors:
- Felix Campelo, https://ror.org/03g5ew477 Institute of Photonic Sciences Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79903.sa0](https://doi.org/10.7554/eLife.79903.sa0)

Chemically fixing cells for fluorescence microscopy is a common practice in cell biology. However, fixation artifacts can lead the incorrect interpretations of experimental results. This article presents compelling evidence showing that in the context of liquid condensates formed by liquid–liquid phase separation (LLPS), paraformaldehyde (PFA) fixation creates a number of artifacts – such as changes in the number, appearance, or disappearance of liquid condensates. These important findings will be of great interest not only for those in the LLPS field but for any cell biologists using fixed samples for microscopy.


---

# Peer review - Round 1

Editors:
- Felix Campelo, https://ror.org/03g5ew477 Institute of Photonic Sciences Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79903.sa1](https://doi.org/10.7554/eLife.79903.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Fixation Can Change the Appearance of Phase Separation in Living Cells" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Felix Campelo as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Vivek Malhotra as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Judith Miné-Hattab (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

In the discussion amongst the reviewers, we all agreed that this is a very interesting and important paper. But the paper needs some clarifications and extra work. Specifically, the major points that should be addressed follow.

1) Compare different fixation methods/concentrations, etc. The authors only report on the artifacts caused by PFA at 4% (with 10' incubation time). They should test other concentrations and other fixatives. In particular, work from the Eggeling lab showed a similar fixation artifact on cell surface receptor clustering (https://journals.biologists.com/bio/article/5/9/1343/1227/Critical-importance-of-appropriate-fixation), which was somehow minimized by adding glutaraldehyde to the fixation buffer. The authors should also test this.

2) Better relate the experimental observations with the dynamic model. As suggested (see detailed reports below), this could be by measuring diffusion coefficients (e.g. FRAP) and see if that matches with the model's predictions.

3) Improve the description of LLPS in the introduction (see details below).

4) Finally, although we do not require the authors to test how other cellular structures are affected by fixation, the authors should add a short section in the introduction to mention some examples of other kinds of structures that are not well conserved by the fixation. Otherwise, it gives the impression that fixation artifacts exist only for LLPS, unfortunately, the preservation of structures by fixation is not limited to LLPS. They should also discuss the fact that some fixation protocols can destroy some structures while another protocol will preserve them. It is the case for some filament structures such as actin filament which are preserved by methanol fixation but seem altered by PFA fixation. This part would help the reader to understand that the quality of a fixation protocol strongly depends on the type of structure studied.

Reviewer #1 (Recommendations for the authors):

I think this is an important paper that presents an important observation that will be important for the community. My main concern/question is whether the two parts of the paper (experimental observations and computational model) are connected causally or not. I think that the glycine experiments point in that direction, but I fail to see concluding evidence on whether the observed changes in the LLPS structures after fixation are indeed caused by slower/faster fixation rates in/out of the condensates. Along these lines:

– Line 111: "The fact that different phase-separating proteins can have bifurcating behaviors upon fixation is interesting.": I fully agree with this. Have the authors considered coexpressing in the same cells the same protein with two different tags (that behave differently after fixation), such as GFP-TAF15 and dsRed-TAF15; or probably even better, dsRED and Halo TAF15? If the kinetic model represents the experimental situation, wouldn't you expect that fixation leads still to the appearance of small droplets in the dsRED but not in the Halo protein?

– Figure 4: glycine also seems to cause a change in the fraction of droplet protein in live cells (compare left panels in A and B). Could the authors discuss that?

Related to the model:

– Line 154: k2 in the model appears as a volumetric rate (that is, all particles in the droplet have the same escape probability). Would a surface escape rate (only particles at the surface are able to escape) change the results of the model?

– Can the authors provide analytical expressions (I believe that is relatively simple) for the plots in 5C, D as a function of the relative in puncta fix. rate and the relative overall fix. rate?

Reviewer #2 (Recommendations for the authors):

To strengthen the manuscript, the authors should try more protocols of fixation. In the simulation part, they could try to incorporate the diffusion coefficient of the protein of interest and see if it is possible to predict the effect of fixation as a function of the diffusion coefficient.

The manuscript focuses on LLPS but it would be interesting to discuss other artefacts of fixation outside of the LLPS: have they tested the artefacts on structures like filaments, chromatin organization, or other types of structures than LLPS? Or do fixation artefacts only concern LLPS?

Reviewer #3 (Recommendations for the authors):

Proteins that undergo LLPS in living cells show a very dynamic behavior and rapidly move from the biomolecular condensates to the surrounding environment (e.g. cytoplasm or nucleoplasm), as demonstrated using FRAP. This dynamic behavior could explain why when comparing fluorescently tagged IDR proteins in living cells and in fixed cells, one could detect only the "larger" condensates in living cells, while detecting also smaller condensates in the fixed cells. Comparison of the number and size of condensates detected in living cells using conventional confocal microscopy and super-resolution microscopy will help understand whether this is sufficient to increase the number of smaller condensates detected in living cells. If not, this would support the idea proposed by the authors that "when the overall fixation rate is fast compared with the dynamics of targeted interactions, fixation artifacts can be minimized even with unequal fixation rates in and out of puncta."

Not all proteins analyzed showed a different distribution in living versus fixed cells (as shown in Figure 3 for GFP-FUS). The differences in the number and size of condensates observed in living and fixed cells should be correlated with the dynamic of the protein analyzed by FRAP. Are proteins with the highest mobility measured by FRAP corresponding to those that show an increased number/size of puncta upon fixation? Are FUS protein-protein interactions stable and less dynamic compared with the overall fixation rate?

Recommendations for improving the writing and presentation: Defining whether a protein undergoes LLPS is based on different assays in vitro, using recombinant proteins and in cells. The observation that a given protein forms "puncta" inside the cells is generally not accepted as a criterion to establish whether it undergoes LLPS. The measure of the number, size, sphericity, liquid-like dynamic behavior (e.g. by FRAP), and sensitivity to agents such as e.g. hexanediol are all assays required to establish and characterize whether a given protein undergoes LLPS. These aspects should be described in the introduction of the paper. It is a bit simplistic to only focus on the calculation of the number and size of puncta before/after fixation.
