# Peer review - Round 1

Editors:
- Sebastian Deindl, Uppsala University Sweden

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69387.sa1](https://doi.org/10.7554/eLife.69387.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

In this study, Kim and co-workers track the dynamics of a large set of different ATP-dependent chromatin remodelers in living cells by utilizing state-of-the-art single-molecule imaging. They report that the remodelers exhibit very high turnover rates at target loci/nucleosomes, find evidence for cooperativity among the remodelers, and reveal the role of ATP hydrolysis in those interactions. These observations allow the authors to put forward a model for tug-of-war activities that modulate the accessibility of promoter regions for transcriptional activity. This manuscript brings important new information to the remodeler and chromatin dynamics field.

Decision letter after peer review:

Thank you for submitting your article "Single-molecule imaging of chromatin remodelers reveals role of ATPase in promoting fast kinetics of target search and dissociation from chromatin" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Sebastian Deindl as the Reviewing Editor and Kevin Struhl as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Xiaojun Ren (Reviewer #1); Bradley R Cairns (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The impact of the paper would be increased if the model presented in Figure 8 could be extended to include all six remodelers studied, thereby highlighting their kinetics similarities and the resulting tug-of-war at promoters.

2) The authors should comment on the perceived discrepancy in the relative abundance of the remodelers. The authors should consider adding the proposed quantification via Western Blot if feasible.

3) The authors should comment on several important technical points raised by the reviewers, in particular in terms of the imaging conditions (single remodelers rather than clusters, potential effect of exposure to laser light, media flow during data acquisition) and data analysis (decomposition of histograms in Figures 1 and 2. The authors should also comment on the cell cycle phase and explicitly describe if/how it was taken into account.

Appropriate textual changes to the manuscript would improve clarity on these points.

Reviewer #1 (Recommendations for the authors):

1) It appears to this reviewer that the Log D and jump distance histograms in Figures 1 and 2 should be decomposed into three components: chromatin-bound, intermediate diffusive, and free diffusive, since the authors have identified an intermediate diffusive population that can transition between bound and free states, which are shown in Figure 3.

2) The authors use the number of molecules of remodelers from published results (Ho, 2018) to calculate target-search kinetics. It appears to this reviewer that the published data does not match the data in Figure S1A. For instance, Figure 7A shows that INO80 is more abundance than ISW2; however, Figure S1A shows the opposite results. Given that these remodelers have been endogenously tagged, it would be possible to quantify the number of molecules of remodelers through western blotting by comparing to known concentrations of HaloTag.

3) P27L603: It should be 10 ms exposure time.

4) P27L605: Please explain why each video lasts 1.5 min.

5) P27L607: It should be 250 ms exposure time.

6) P27L612: Please explain again why each video lasts 7-9 min.

7) P28L638: Please check the equation.

8) P32L716: Please check the reference.

Reviewer #2 (Recommendations for the authors):

The model presented in figure 8 restricts itself to two of the remodelers (RSC and INO80) addressed, and does not reflect the full scope of the results obtained in this work. It would be helpful if changes could be made to the model figure in order to embrace all six remodelers studied, highlighting their kinetics similarities, and the resulting tug-of-war at promoters. Notably, it would be helpful to consolidate and clarify the ATPase state, as ATP and ADP+Pi are written concomitantly at all stages of each remodeler presented. Moreover, the model would benefit from a more clear depiction of ATP binding in the enhancement of nucleosome browsing, and of ATP hydrolysis in the enhancement of dissociation.

Reviewer #3 (Recommendations for the authors):

The paper is a technical tour-de-force, but I have a number of technical questions that need clarification. These arise partially from my ignorance, but also from the fact that there seem to be details missing in the methods section. Given that the paper should be read by a maximal number of chromatin biologists, I think it would greatly enhance the impact of the paper to include explanations concerning the following points, either in the methods section or in the text itself.

1. How do they know that they are actually imaging SINGLE chromatin remodelers in every case, and not clusters of a given remodeler, for example, bound at multiple nucleosomes at a promoter (or cluster of promoters) ? I understand that they use a pulsed laser to activate the Halo tag fluorochrome, but it seems to me that they need to quantify the number of molecules each signal might represent. Hansen and Darzacq have worked out means to do this. The authors could also estimate the number of total molecules of each remodeler this way, which would be useful to know, especially to see if this influences occupancy rates.

2. The pixel size (over 100 nm) is quite large – certainly large enough to contain multiple protein complexes. How large are the signals they monitor ? Did the try to reduce pixel size (it is possible with the LSM 710 and 100x objective)?

3. The authors use an imaging scheme worked out by Hansen et al. for "rapid" and "slower" movements. In one they image at 10ms intervals for 1.5 min, but for the slower one they image at 250ms intervals for 7-9 minutes. This latter scheme implies a lot of exposure to laser light. Did they check that there was no impact on cell division rate after the slower, longer imaging protocol ? It is a massive dose, and the time needed for cell division should be monitored under these conditions.

4. The authors say that they image for 2 h after the immobilization of cells on a cover slide. Are the cells continually bathed in medium during imaging ? this should be stated, if so. During 2 hours without glucose yeast rapidly deplete their ATP levels and this strongly influences chromatin mobility and remodeler activity (as shown 20 years ago, but also in this paper by walker motif mutation). It leads one to wonder if the slower moving remodeler tracks were taken at the end of the 2h period and the faster ones at the early time points ? Or did they keep a flow of fresh media onto the cells ? This is a very important technical point that should be explained in the methods.

5. For the longer (but not shorter) tracking and subsequent calculation of diffusion coefficients the authors should be conscious that nuclear movement (or cellular and instrumental drift) can alter the track, if not normalized out. I guess the fact that they subtract H2B movement does normalize for cellular or instrumental drift, but perhaps they should state that. Other means exist, e.g. to track the center of the nucleus interpolated from a ring of nuclear pores or background nuclear fluorescence – and subtract that movement from the movement of the SPT. Some discussion of removal of such background drift should be mentioned in methods, or if this has already been ruled out elsewhere, the reference should be cited.

6. Finally, the authors assume that the nucleosome remodelers are almost exclusively involved in transcription, and based on this they make the tug-of-war argument that INO80 and ISWI2 are counteracting RSC and Swi/SNF action. However, the two remodelers that have slightly different diffusion histograms (INO80 and ISWI2) are both implicated in DNA replication (and also in DNA repair), as well as transcription. The Tsukiyama lab has clearly demonstrated their roles in replication, and various authors provided convincing evidence that INO80 is important for paused fork restart and other repair events. DNA repair may be too rare an event (compared to transcription) to bias the movement observed, but replication could definitely bias the mobility/diffusion or Spot-on profiles, if a fraction of the cells imaged were in S phase.

This raises a number of questions:

a) Were the cells imaged exclusively in G1 phase ? That is, were only cells without buds monitored ? This should be stated if so.

b) If not, did they monitor INO80 or ISWi2 diffusion specifically in S phase cells and did this lead to the same or a different profile of chromatin-bound/-free fractions and diffusion co-efficients?

c) The diffusion histograms are fit to two Gaussian curves, but they would also be compatible with the superposition of multiple populations. Given that INO80 (and probably ISWI2) respond to phosphorylation, and may be regulated by cell cycle phase – it might be that there are more than simply a "bound" and an "unbound" population. This should – at the very least be discussed.

I think it should be mentioned that these specific two remodelers are involved in replication – and what that might imply – unless all cells imaged were in G1 phase. If they were all G1 phase cells, then it should have been mentioned (sorry if I missed it).

d) There could also be multiple variant complexes, containing additional subunits or being post-translationally modified, that might account for the complexity of Diffusion coefficients. This should at least be mentioned somewhere in the discussion.

With clarity on these issues, I think this paper definitely brings important new information to the remodeler and chromatin dynamics field.
