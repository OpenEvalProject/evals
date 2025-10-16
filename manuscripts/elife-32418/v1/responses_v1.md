# Author response - Round 1

Authors:
- Aussie Suzuki ([ORCID: 0000-0001-7390-5116](https://orcid.org/0000-0001-7390-5116))
- Sarah K Long
- Edward D Salmon

## Response text

DOI: [10.7554/eLife.32418.037](https://doi.org/10.7554/eLife.32418.037)

[Editors’ note: the author responses to the first round of peer review follow.]

All this said, however, the three reviewers and the Reviewing Editor share the view that the current form of the manuscript lacks the clarity required to be accepted by the community as a generally useful technical resource. All three reviewers advocate an almost complete re-writing of the manuscript. As we realise that this will require considerable time and effort, we feel forced to return the manuscript to you and leave you an opportunity to decide on further moves. We will be happy to consider a revised form of the manuscript that fully meets the indications provided by the reviewers. This, however, will have to be considered a new submission.

We appreciate that all reviewers found our study important and with considerable merit. We also thank the reviewers for their constructive comments and suggestions. As requested by the reviewers and the editor, both the text and figures have been reorganized and edited to “improve clarity of the manuscript to the level required by the community as a general useful technical resource.”

Significant modifications in the revised manuscript to improve clarity are as follows:

1) Addition of a “Principles of the Method” section to the beginning of the Results with a corresponding Figure containing schematic and numerical information of the analytical method to provide the requested “pipeline for obtaining accurate 3D measurements”, and Figure 1—source data 1 providing details of each step and potential error sources.

2) Re-organization of all figures to put key findings in the main Figures and supporting data in corresponding Figure supplement in a logical way to comply with their presentation in eLife.

3) Unified the names of variables used in both the experimental data analysis and the computer simulation of the method to make the fundamental principles clearer for the reader to follow.

4) Provided new data in the Materials and methods to address the question from the reviewers about missing data: the efficiency of endogenous protein depletion by siRNA for the EGFP labeled protein components of the Ndc80 complex.

5) Made modifications or additions to the text in response to the specific reviewer’s concerns as listed below.

Reviewer #1:

[…]

On a less positive tone, as written the paper is a true heavy weight, and I rather strongly feel that the authors have to work very seriously to streamline their descriptions, simplify the figures, and shorten the text to make the paper more accessible. For instance, the mathematical analysis currently in Figure 3 could be summarized and presented in a separate box. Each figure comes with approximately 15 panels, and it would be preferable to present most of these data in form of a table in the main text and as plots in Supplementary. Also, the authors may want to harmonize font size throughout their figures, as the figures look very heterogeneous.

We addressed this issue as summarized in “Significant modifications in the revised manuscript to improve clarity”.

Reviewer #2:

[…]

General assessment:

While the shear amount of data here is impressive, it unfortunately is not presented in an accessible way. Without a much clearer presentation, I do not feel the manuscript in its current form can serve as a useful technical resource. In many instances, it is extremely difficult to understand what is being plotted, and what are the primary important messages that the authors wish to draw from each piece of data. Some interesting and potentially valuable technical concepts are considered, such as the likelihood that variation in coverslip thickness causes large chromatic shifts in the z-direction, and the possibility that kinetochore tilting seen by other groups could be an artifact due to the inherent uncertainty in localizing dim fluorescence spots. However, it is extremely difficult to discern whether either of these potentially interesting points can be supported by the data. In my view, this paper is not ready for publication. Below I have listed specific comments which I hope can help the authors improve their presentation.

We addressed the general “clarity” issue as summarized in “Significant modifications in revised manuscript to improve clarity”.

Substantive concerns:

Results section: "Because other Δ measurements had smaller SDs, we settled on values of Sxsd=Sysd = 4 and Szsd = 8, since there could have been some unexpected CA contribution to Δ variance from unknown local changes in refractive index." This seems arbitrary. The sentences just prior to this one suggested that larger values were needed to explain the data. Why go through the trouble to estimate carefully what is needed to explain the data, only to then impose an ad hoc reduction?

To clarify this issue, we edited the relevant paragraph in the results to read (Note Ssd is now named SDc for variance in centroid determination):

“To obtain an estimate of the error contributed from the SDc, we used results from Δ analysis which in principle have local CA correction. […] This result indicates that the variance in our centroid measurement is very small and only slightly enhances the 3D measurements from the true value.”

Results section: "The simulation data also shows that the combination of variances in centroid measurement and CA correction can account for a large fraction of the variance in tilt angles[…]This suggests that the majority of proteins linking the inner to outer kinetochore are aligned along the kMT axis." This is one of the key conclusions of the paper but it is not well supported. A thorough analysis would state explicitly how much of the variability is explained by the uncertainties in localization and chromatic shift, and also how much real kinetochore tilting would be consistent with the data.

We deleted this conclusion from the simulation section of the revised manuscript and inserted the following sentence at the end of the section of the Results entitled: “The Mean Human Kinetochore Protein Architecture at Metaphase Measured by the Δ Method and Our 3D Method are Similar.” to read:

“In Figure 5, the Ndc80 complex and protein linkage to the inner kinetochore are shown aligned with the axis of kMTs because the ML3D mean separation values are only slightly greater than their corresponding Δ values and the Δ value is a projection of the ML3D value along the K-K axis.”

In addition, we have added the potential errors in angle measurements in the result section of kinetochore tilt and simulation in revised manuscript to read:

“Unlike 3D separation, the mean tilt angle β was sensitive to unequal numbers of kinetochores above and below the spindle equator. The mean angle β is near zero in the middle of the spindle and reaches mean values of about 20-25 degrees at the bottom and top of the spindle (Figure 6 —figure supplement 2C).”

and

“To see how the SDc and CAsd of our measurement method effect the variances in the angles α and β, we entered into the simulation constant values for S between zero and 100 nm (Figure 8B). The variance in the angles α and β are largest for small separations (Figure 8B). Our SDc and CAsd caused about half to two-thirds of the variance measured in cells for separations of 60 nm (CENP-T-Hec1-9G3 in Figure 3C) or 90 nm (CENP-A-Hec1-9G3 in Figure 6—figure supplement 2).”

Results section: "after depletion of the endogenous protein by RNAi" How effective was the depletion?

We have added the efficiency of protein depletion in Materials and methods of the revised manuscript. The new sentences read:

“siRNA was performed with 100 nM of siRNA duplex and siRNA sequences of CENP-T, CENP-C, Ndc80, and Nuf2 were described previously (DeLuca et al., 2002; Suzuki et al., 2015). […]Although we performed siRNA for endogenous proteins when we used cell lines expressing EGFP tagged protein, there was no significant differences for Δ, 2D, and 3D separation measurements in Ndc80-EGFP stable cells with or without siRNA for Ndc80.”

Results section: "This result indicates that most of the Z-offset in the original Sz data is not produced by unequal numbers of kinetochores from above and below the spindle axis, but likely from somewhat thinner coverslips than the standard 0.17 mm thickness (Figure 7C)." This potentially interesting point is not rigorously supported without a demonstration that coverslips of known thickness but deviating from the standard 0.17 mm produce predictable changes in Z-offset. It seems that it would be a straightforward experiment to measure coverslips thicknesses and then prepare and analyze cells on those coverslips that happen to deviate from the standard.

To address this issue, we added a new Graph and the following sentence:

“The plot in Figure 6—figure supplement 1 illustrates the sensitivity of Z-offset to coverslip thickness. A steep slope is seen when measured Z-offset values in Figure 6C are plotted as a function of the mean thickness we measured for #1, #1.5 and #2 coverslips.”

Discussion section: "[…]we found that measurements of individual kinetochores (not sister pairs) within a single cell yielded the identical value at metaphase as the mean obtained from kinetochores within several cells. Thus, variations between cells or selected kinetochore measurements like Δ analysis is not an issue." This is overstated. The data in Figure 4E show only that mean values for populations of hundreds of kinetochores are consistent. But they say nothing about kinetochore-to-kinetochore variability. And "several cells" is unclear. How many cells? If the number is very small then the data cannot strongly support the conclusion that cell-to-cell variability is negligible.

The above sentence was miss-worded. The corrected sentences read:

“Sister kinetochore pairs were used for majority of measurements in this study to directly compare separations obtained by Δ and 2D/3D fluorescent co-localization methods using the same data sets. To test if selection of sister pairs influenced our measurements, we measured 120 kinetochores selected randomly in a single cell. This produced a mean separation value nearly identical to the mean value for single kinetochore measurements of sister pairs obtained from 6 metaphase cells (Figure 4C).”

The widespread, inconsistent, and redundant use of variables in this paper is extremely confusing. Figure 3 alone introduces at least 25 different variables: X1p, Y1p, Z1p, Sxsd, Sysd, Szsd, CAxp, CAyp, CAzp, CAxsd, CAysd, CAzsd, randn, Sxp, Syp, Szp, Sxyp, Sxyzp, CAxe, CAxs, CAye, CAys, CAze, CAzs. Sometimes two different variables seem to denote the same quantities, for example in Figure 1C, where both CAx and Xg – Xr are used, whereas in Figure 1—figure supplement 1, only Xg – Xr is used. Conversely, two different calculations are sometimes represented by the same variable, such as S(3D), which does not include the correction for chromatic shift in Figure 1, but does include the correction in later figures. When the variables x and y are used in the equations for regression lines, they are often contradictory with respect to the plotted quantities, such as in Figure 1—figure supplement 1, where the regression variable x sometimes denotes Y (y-axis position in pixels) and the regression variable y sometimes denotes Xg-Xr (chromatic shift along x-axis in nanometers). When used sparingly and consistently, variables can make difficult mathematical concepts easier to follow. But here the use of variables seems to obfuscate things. It might help to adopt vector notation, to allow more compact expressions that capture the important conceptual relationships without explicitly showing all three cardinal directions.

We significantly unified variable names between those used for experimental analysis and those used in the computer simulations.

The paper includes a huge number of scatterplots (I count ~59) and histograms (~32). Most of the scatterplots lack clear trends with respect to changes in the x-, y-, or z-position. In general, these plots seem to provide lots of clutter without adding much insight.

We have significantly modified Figure construction to put key data in the major figures and supporting data in Supplemental Figures using the eLife format.

Reviewer #3:

Major concerns:

The paper as written is challenging to read and needs significant changes to both the text and figures to become an accessible and used resource.

1) While it is clear that the authors achieve more accurate centroid localization than previous works, the text does not clearly synthesize which practices together made this possible, and what experimental and analysis pipeline people should use to achieve such accuracy (what's good enough, and what isn't?). As one example to help guide changes, Figure 7 illustrates how Sz varies with imaging depth and kinetochore tilt, but the text describing this figure does not explain how this data relates to the rest of the work nor makes a concrete suggestion about best practices. Making a clear connection between the data and actionable outcomes is critical for this work to be a useful tool, and will help create a constructive, positive tone towards improving future measurements. On this note, it would be helpful to integrate in a single new figure the final suggested pipeline for obtaining accurate 3D measurements – unless the authors have a better idea for how to do that.

We have significantly modified the manuscript and figures to address these concerns as outlined in the first page in “Significant modifications in revised manuscript to improve clarity.”

2) The figures are unnecessarily complicated and often very hard to read. The authors should take the time to think about which figures are essential for the main text and which are not, and should take the time to make their figures clear enough to stand alone. Figures should be significantly simplified. As examples, Figure 1D could be moved to the supplement and Figures 5 and 6 could be moved or condensed. (In addition, it is critical that plots in all figures have clearly labeled axes in readable font sizes, and there must be no confusion about what is measured).

Again, we have significantly modified the manuscript and figures to address these concerns as outlined in the first page in “Significant modifications in revised manuscript to improve clarity.”

[Editors' note: the author responses to the re-review follow.]

Reviewer #2:

This paper is very significantly improved. I commend the authors for their very careful reworking. I think the result is a paper that can serve as a very important resource, not only to the community of scientists interested in kinetochore architecture, but also more broadly, to microscopists studying the architectures of other large molecular assemblies inside cells. I hope the following relatively minor comments will help the authors further improve their manuscript in preparation for publication. In particular, I feel the impact of the paper could be boosted by a more quantitative analysis of the amount of true, kinetochore-to-kinetochore variability that would be compatible with the measurements, as explained in the last two comments below.

Results section: "Unexpectedly, in vivo, the C-terminus of Ndc80 locates much closer to the globular domains of Spc24/Spc25 (Figure 4B). This difference might be caused by structural restrictions on the position of the EGFP tag, which was tethered to the protein end by a 9 amino acid linker." A structure for the tetramerization domain within the Ndc80 complex is available (Valverde et al., 2016). Can the apparent arrangement in vivo of the C-termini of Ndc80 and Nuf2 and the N-termini of Spc24 and Spc25 be reconciled with this published structure? Or does one need to further invoke "restrictions" on the epitopes/antibodies to reconcile these different views of the Ndc80 complex? More generally, the published structures for the Ndc80 complex can provide predictions for the distances between many of the antibody pairs used in this study. Why not include a comprehensive, graphical comparison of predicted versus measured distances? If the correlation is good, then such a comparison would provide very compelling additional support for the accuracy of the fluorescence colocalization technique. It would also help clarify what is the in vivo structure of the Ndc80 complex.

We have added a detailed comparison between our measurements and previous studies in vitro (Huis In 't Veld et al., 2016; Valverde et al., 2016; Wei et al., 2005) in Figure 4—figure supplement 1.

Discussion section: "Note that their higher SDc values explains why their Δ measurements are significantly larger than ours (Figure 9—figure supplement 1)." This statement seems a bit overstated to me considering that the authors can only estimate the SDc values of their competitor's work – they do not know the SDc values from that work with 100% certainty. In my view, it would be more correct, and would not undercut the impact of the present paper at all, to qualify the sentence very slightly as follows: "Such high SDc values could explain[…]" or "Such high SDc values probably explain[…]"

Thank you for an important suggestion. We have modified this and subsequent sentences to read;

“Such high CDsd values could explain why their Δ measurements are significantly larger than ours (Figure 9—source data 1). […]In our measurements, large values of Zoffset were rare (Figure 5—source data 1); we have no information to judge how much other sources of error like Z-offset, contributed to the Smith, McAinsh and Burroughs, 2016 measurements.”

Discussion section; "A previous study has shown that the accuracy of separation measurements is sensitive to the spatial staggering of the labeled molecules along the kinetochore inner to outer axis only for stagger greater than 150 nm, which produces two fluorescent peaks instead of a single peak (Joglekar et al., 2009)." This statement seems over-simplified to me, and potentially confusing. The production of two peaks is not a general consequence of staggering of the labeled molecules. It occurred in a highly idealized simulation in the cited paper, where the simulated positions of six red spots were shifted by fixed distances in the x-direction relative to a corresponding set of six green spots. More random staggered arrangements could retain a single fluorescent peak, but with a larger width compared to a case without staggering.

Our writing was not clear. This paragraph now reads:

“Human kinetochores are built from multiple copies of core-kinetochore proteins (Suzuki et al., 2016). […] This indicates that our centroid measurements correspond to the mean position of the fluorescently labeled protein epitopes within human kinetochores.”

Discussion section: "Second, the SD of our 2D/3D measurements are small, typically less than 10 nm, and a significant part of this SD must be from the SDc and CAsd (see above discussion) and not from differences between kinetochores." This is interesting, but it only weakly supports the "uniform architecture" hypothesis. A key question is, how much true, kinetochore-to-kinetochore variability in distance is compatible with the measured SDs? Based on the data and analyses presented in this paper, it should be possible to make a quantitative statement about how wide the underlying distribution of true distances is likely to be. The purely qualitative statement, that the architecture is "very" uniform, seems a bit hollow.

Discussion section: "Surprisingly, only 10~15 kinetochores needed to be averaged to achieve the mean and SD typical of > 150 kinetochores (Figure 9—figure supplement 2)." This observation merely indicates that 10 to 15 kinetochores are sufficient to estimate the mean and width of the distribution. It does not by itself indicate anything about the width, i.e. about the level of kinetochore-to-kinetochore variability.

We asked how much kinetochore-to-kinetochore variability can be involved in our experimental measurements using simulations in Figure 9—source data 2. Based on these results, we have modified sentences to read: “Second, as expected for the Gaussian distribution measured for separation values (e.g. Figure 3B), we found that only 10~15 kinetochores were needed to be averaged to achieve the mean and SD typical of > 150 kinetochores (Figure 9—figure supplement 1). Third, the SD of our 2D/3D measurements are small, typically less than 12 nm, and a significant part of this SD must be from the CDsd and CAsd (Table 6A and see above discussion) and not from differences between kinetochores. To see this more clearly, we used the same simulations in Figures 8–9 with mean kinetochore-to-kinetochore variability (Ksd = ± 0, ± 5, ± 10, or ± 15 nm) (Figure 9—source data 2). Simulation results showed that Ksd of about ± 5 nm or less plus measurement CDsd and CAsd yielded the experimental mean SD value of 12.5 nm (Figure 9—source data 2). These results imply that the vast majority of kinetochores at metaphase have a similar protein architecture”
