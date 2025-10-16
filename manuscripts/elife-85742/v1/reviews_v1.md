# Peer review - Round 1

Editors:
- Emilio Kropff, https://ror.org/0431v7h69 Fundación Instituto Leloir Argentina

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85742.sa0](https://doi.org/10.7554/eLife.85742.sa0)

This computational work represents a valuable and long overdue assessment of the potential mechanisms associating patterns of activity of entorhinal grid cells, recorded mostly in rodents, with the population property of hexasymmetry detected in non-invasive human studies. The methodic comparison of alternative hypotheses is compelling, and the conclusions are important for the future design of experiments assessing the neural correlates of human navigation across physical, virtual, or conceptual spaces.


---

# Peer review - Round 1

Editors:
- Emilio Kropff, https://ror.org/0431v7h69 Fundación Instituto Leloir Argentina

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85742.sa1](https://doi.org/10.7554/eLife.85742.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Quantitative modeling of the emergence of macroscopic grid-like representations" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Laura Colgin as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Alessandro Treves (Reviewer #1); Daniel Bush (Reviewer #2); Matthew F Nolan (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions (for the authors):

1) Strengthen the link between the simulations presented here and the known biophysical properties of rodent entorhinal grid cells. Revise the ranges used in the analyses in comparison with those reported in the literature (see details for each scenario below) and provide a graphical representation of the values in each case. Provide an idea of how values of H are related to results obtained with other methods in previous experimental studies.

2) Extend the study to null-hypothesis scenarios, such as the standard grid cell model or head-direction clustering that is independent of grid cell firing.

Reviewer #1 (Recommendations for the authors):

Suggestions for improvement to the authors:

Is there quantitative evidence independent of the Doeller (2010) paper that head direction selectivity is clustered along the grid axes?

Similarly, is there quantitative evidence independent of the Heys (2014) and Gu (2018) papers for the clustering of spatial phases?

The most important panels of the whole paper, Figure 2E, and Figure 3B are impossible to read. Could you replace them with level contours or proper color-coded ones?

Also, the gray curves in subplots Figure 2B-D and F-H are difficult to see.

Some statements seem to be overkill, such as that the adaptation weight should be restricted to the range 0 < w < 1.

Also, the detailed analysis of the third hypothesis seems like overkill.

For the navigation model, real rat trajectories are available; maybe human VR ones as well?

Are all grid units in the model on the same scale? The presence in rodent mEC of 4-5 "modules" with different grid scales should be discussed.

Can effective firing rate adaptation parameters be somehow gauged from studies of the real biophysical properties of grid cells, as in the early Giocomo and Hasselmo studies? Obtaining "realistic" parameters just by dividing by 2 ideal parameters seems a bit arbitrary.

Congratulations on the nice study, especially the valuable analytical components!

Reviewer #2 (Recommendations for the authors):

My main suggestion for improving this manuscript is to strengthen the link between the simulations presented here and the known properties of rodent entorhinal grid cells by: [1] clarifying exactly what each set of 'biologically plausible parameters' are and how they were obtained; and [2] providing graphical illustrations of these parameter values, to compare with the 'ideal conditions' that are displayed in most figures. Specifically:

In the conjunctive cell hypothesis section, could the authors describe how the 'biologically plausible' tuning width parameter was extracted from the data presented by Doeller et al. (Nature, 2010)? Towards the end of page 12, for example, the authors state that they "…derived the more realistic [tuning width] parameters from a previous study", but do not provide any details of these parameter values (I eventually found them in the caption of Figure 5) or how they were derived. Could they also add an illustration of the head direction tuning generated by all three tuning width parameters (i.e. those shown in panels F, G, and H) to Figure 2A, overlaid in dashed or dotted lines, to give an intuition of how each tuning width compares to empirical data?

In Figure 3, could the authors show the firing pattern of a simulated grid cell with the adaptation weight of 1 that is used to generate the results shown in panels C, D, and E? Does this introduce significant variability in firing rate between different firing fields, as observed experimentally (Ismakov et al., Current Biology, 2017)? What value of the adaptation weight was used to generate the data shown in dashed grey and pink lines on the right-hand side of panel A? Can this be related to estimates of the strength of firing rate adaptation in entorhinal pyramidal and stellate cells, for example as described by Alonso and Klink (Journal of Neurophysiology, 1993)? This might also lead the authors to modify their claim that they are "not aware of empirical investigations regarding repetition suppression effects in single grid cells", made at the top of page 13 and again in the Discussion

With regards to the structure-function hypothesis, and following the comments above, the authors should also state how the 'realistic' values of the clustering parameter that they refer to in Sections 2.2.3 and 2.3 were derived from data presented by Gu et al. (2018), and what those parameter values are

Reviewer #3 (Recommendations for the authors):

1. Could the null hypothesis of trajectory-dependent hexasymmetry be mapped out more clearly? For example:

- It's implicit that a 'standard' grid cell model wouldn't generate hexadirectional modulation. It could help the reader to make this clear early in the introduction.

- The Methods and Supplemental Data illustrate the possibility that hexadirectional modulation could arise simply from the trajectory followed – called path hexasymmetry here. The very nice modelling approach used provides an opportunity to quantify the size of this effect relative to effects in previous human studies and to verify that previous attempts to mitigate this through binning were successful. Adding this analysis would be a valuable control for the interpretation of human data.

- For the conjunctive grid model, is there anything special about the neurons being grid cells? In other words, would head direction cells with similar tuning profiles generate the same hexadirectional modulation? I expect they would but clarity here would be helpful for future mechanistic work.

2. For the evaluation of the grid by head direction hypothesis, the range of parameter values considered seems quite narrow compared to the likely properties of grid cells (see e.g. Sargolini et al. 2006). It could be helpful to add a null case where the head direction is not aligned to the grid axes and to consider a greater range of alignment jitter.

It could also help the reader to illustrate the head direction parameters for each simulation, alongside the results. E.g. With plots of the head direction tunings for the models presented.

3. The math behind the definition of H is clearly laid out in the methods section. I think it would help the reader to also give some intuition for the design and behaviour of H when it's introduced in the Results section. It would also be helpful to indicate here the range of possible values, and within that range to indicate values that could arise from noisy activity given finite sampling duration, etc.

4. Related to the above, some intuition for the expected values of H given previous fMRI/EEG studies could also be helpful. For example, to facilitate comparisons could the numerical simulation results also be analysed with previous methods and the scores reported? This way a reader could better appreciate the extent to which the effect sizes in the simulations are comparable with the human fMRI/EEG data.
