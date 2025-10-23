# Author response - Round 1

Authors:
- Matthew A Heinrich ([ORCID: 0000-0002-9041-5554](https://orcid.org/0000-0002-9041-5554))
- Ricard Alert ([ORCID: 0000-0002-1885-9177](https://orcid.org/0000-0002-1885-9177))
- Julienne M LaChance
- Tom J Zajdel
- Andrej Košmrlj ([ORCID: 0000-0001-6137-9200](https://orcid.org/0000-0001-6137-9200))
- Daniel J Cohen ([ORCID: 0000-0001-5819-1135](https://orcid.org/0000-0001-5819-1135))

## Response text

DOI: [10.7554/eLife.58945.sa2](https://doi.org/10.7554/eLife.58945.sa2)

Revisions:

Together, the reviewers converged on a few points that we felt would not require necessarily any extra experimentation but could be obtained from your current data. These points focus on:

1) Study more systematically the relationship between curvature at the boundary and radial velocity, comparing round and oval shapes. Furthermore, how large does the tissue need to be for the radial velocity to be constant?

We performed new analyses specifically relating curvature to normal expansion velocity including our elliptical tissue data. These data are seen in Figure 1—figure supplement 2. They show normal velocity as a function of curvature and demonstrate that the normal velocity is independent of curvature except in the extreme curvature cases on the highest aspect ratio ellipses. A fuller description can be found in paragraph four of the Results section, and we also provide further context in paragraph two of the Discussion section. With regards to the minimum tissue size needed for constant radial velocity, our analyses suggest tissue diameters of at least 1 mm given that we calculate the stable boundary zone is ~500 µm. This distinction has been added to the Discussion section.

2) Directly compare round tissues that have the same current size but originate from different original sizes to determine if differences derive from original size or current size.

This is an important consideration and insightful question that frequently comes up during presentations of this work, so we devoted an additional figure (Figure 6) to more quantitatively explore this. Our new analyses specifically explore the question of tissues of similar current size but different initial sizes with respect to migration speed, vortex power, cell density, and cell cycle (Figure 6). These new analyses further highlight the importance of history and context in understanding tissue behaviors and make it clear that initial tissue size and mechanical history, rather than current size, drives tissue behavior. A fuller discussion can be found in paragraph three of the Discussion section.

3) Please add more statistical analysis, instead of generalised statements.

Proper statistics are critical, so we have conducted new statistical analyses for all comparative studies. No prior claims have changed, but we now have more quantitative standards to support them. Specific analyses are as follows. Model goodness-of-fit is now evaluated using Chi-squared analysis, which can be seen in Figure 1E, and interpreted as Chi-squared values < 1 representing reasonable fits. Comparison of large and small tissue speeds and radial velocities were assessed by comparing the difference between the datasets compared to their respective standard deviations, as seen in Figure 2D. T-testing via the Mann-Whitney test was performed to compare distributions for vorticity (Figure 3D) and highlight the strongly statistically significant difference between them (p < 0.0001). Further analysis of the spatial correlation between density and vorticity resulted in a new panel (Figure 4—figure supplement 1E, F) displaying the relationships more quantitatively and across the whole dataset. All analyses are discussed in the Materials and methods section.

4) Please add more methods regarding PIV.

We appreciated this common as selection and assessment of PIV parameters is non-trivial and deserves more detailed discussion to aid in reproducibility. To address this, we carefully evaluated the effects of PIV parameters on our results and verified that changing the interrogation box did not appreciably alter the large-scale features or structures of the flow fields. That the larger PIV window is sufficient is especially useful because it can dramatically reduce computation time for large times relative to a smaller window size. These data are now presented in Figure 2—figure supplement 1, and the approach is described in the Materials and methods section.

5) Please add more discussion regarding the limitations of the model.

We discussed the limitations of the model in paragraph four of the Discussion section. We now explain that our model does not account for the cell density field, whereas our data show that vortex formation co-occurs with low-density regions. Again, our model is not intended to be exhaustive, but to capture key mechanistic details with as few parameters as possible. Our data and simulation results therefore call for the development of more detailed models to capture the relationship between vortex formation and cell density.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

1) Regarding the relationship between curvature and edge speed, the authors find that the normal velocity is not constant along the ellipse edge, but they use a constant velocity in their model. They should address this briefly in the Results section and explain why they are able to make the assumption of constant velocity in the model. For example, by measuring if the radius of curvature along the ellipses is mainly greater than 1mm (which I imagine it is) and therefore a constant velocity can be assumed as shown in Figure 1—figure supplement 2B.

This is important to clarify, so we have the following to address it. As noted, high curvature only applies to a small region of the 1:8 ellipses, which will blunt over time as it grows, so our constant velocity model still fits the overall area expansion data well.

“Such high curvatures are concentrated around the major axes of our elliptical tissues. However, most of the tissue edge has a smaller curvature, and therefore advances at a curvature-independent speed. Further, even high curvature regions blunt due to expansion over time (see Figure 1—video 3). As a result, our model with a single edge speed 𝑣𝑛 ≃ 29.5 𝜇m/h is sufficient to capture the area expansion of both circular and elliptical tissues (Figure 1E).”

2) Since a major claim is that the behaviour of the tissues was all due to their original size rather than their current size, it is important to directly compare the behaviour of tissues that were originally large and small at the time point. Is the cell density significantly different for large and small tissues when they are the same size? It is hard to see from the figure.

It is true that the difference in density is less apparent in Figure 6C, and we have added additional discussion specifically exploring this point and emphasizing both the rate of change of density and the fact that the primary density phenotypes occur in the early stages of growth where smaller tissues experience a drop in density while larger tissues experience a monotonic increase. These are summarized below.

“…at equal current sizes, while absolute cell densities in the tissue centers share some overlap, it is notable that the rate of density change at the tissue center is increasing faster in initially-small tissues than in initially-large tissues (Figure 6C). However, the most striking differences in cell density evolution occur not at equal current sizes but during the early stages of tissue expansion: whereas the cell density at the center of large tissues increases at all times, the center of small tissues features a marked density decrease between ∼ 8 and ∼ 24 h (Figure 4A,B).”

Also, Figure 6 is entirely addressed in the Discussion section rather than in the results, despite its importance. Why is it not in the Results section?

We felt strongly that Figure 6 belongs in the Discussion section because it represents a compilation and comparison of data already presented in the prior figures in different forms. In other words, Figure 6 does not show new measurements but rather reanalyzes the data in all the previous figures in a way that showcases history effects. Thus, it is a figure that very much engages with, and emerges from, the points raised in the Discussion section relating to history effects, putting our results into a broader context. Therefore, we feel that moving Figure 6 to the Results section would weaken its impact and the Discussion section overall. That said, we can move it to the Results if necessary.
