# Peer review - Round 1

Editors:
- Agnese Seminara, University of Genoa Italy

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67495.sa1](https://doi.org/10.7554/eLife.67495.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

How the bacterium E. coli decides when to divide is an interesting, important, unsolved and highly controversial topic of interest to readers across disciplines, including microbiology, cell biology and statistical physics. Popular "single process" models invoke regulation at the step of replication initiation or at the step of cell division per se, whereas these authors have previously proposed a "concurrent cycles" model in which both processes are relevant, with different prominences in different situations. Consistent with the authors' motivating hypothesis, in the particular perturbed condition investigated in this work, a process different from DNA replication becomes increasingly important for division control as the degree of perturbation increases, which provides a new challenge to models for cell division control.

Decision letter after peer review:

Thank you for submitting your article "Two different cell-cycle processes determine the timing of cell division in Escherichia coli" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Nancy Kleckner (Reviewer #2); Chenli Liu (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

(1) Please include a discussion to address the possibility that DNA replication and cell division may not be entirely independent.

You could additionally perform experiments to strengthen your conclusions, now or at a later time – but this is not a requirement, it is entirely up to you. Suggestions: perturb specific cell division processes by titrating components involved in Z-ring assembly (e.g., titrating FtsZ as in Zheng et al. PNAS 2016). Alternatively, following the authors' reasoning, perturbation to DNA replication should exaggerate the effect of the replication-dependent processes on division timing. One possible approach is to slow down the speed of replication fork as done in Zhu et al. mBio 2017 or Si et al. Curr. Biol. 2017. It is important to see if the single-cell correlations can be restored when replication is perturbed in A22 treated cells.

2) Please edit the manuscript to address all points raised in the "Recommendation for authors" sections below.

Reviewer #2 (Recommendations for the authors):

Overall, this paper is well and clearly written.

Figure 2.

A. Are the two cells outlined below the same as the ones in the image series above? Does not seem so. There are too many "time points" in the below cartoon vs the above images and the positions of the spots don't correspond. This is hard to understand.

B. It seems that cell lengths are greater in liquid culture than in mother machine at all A22 concentrations; the same might or might not be true of width. Why? Does this matter? Is it completely clear that the cells are in steady state after 6 hours (see discussion in Zheng et al., 2020)?

C. (i) Can the authors explain why, in the unperturbed case, the DnaN signal seems to "split" into two parts and then become single again? This does not happen in the A22 samples. Does this matter?

(ii) Also, it is noted that the times defined by these images do not "strictly agree" with average replication/termination times…Please explain? Are we supposed to see these as illustrating the general pattern of the change in replication initiation time, vs division, and the fact that C period is the same in all conditions, without worrying about the exact length of the C-period? Or…how are the average replication/termination times actually determined (vs these images)?

(iii) Also – it might be useful to indicate the "C" and "D" periods explicitly, eg in the unperturbed case? C period is time between red and yellow dotted lines and D period is time between yellow dotted line and next cell division, right? But in the A22 case, C period spans a division and D-period is again between yellow line and next division… This is obvious to people used to C+D but is something to keep in mind in terms of the biology.

Figure 3.

– Legend has typo: B,D,F: Slopes of the added sizes corresponding to A, C, D should be "E", respectively

– In Panel E

(i) There is an assumption involved in plotting the "average length added PER ORIGIN in C+D" versus the "initiation length PER ORIGIN". (i.e. in normalizing "per origin").

The rationale for this approach should be made explicit. It is presumably derived from the Witz-type analysis in (C) which considers that everything scales with the number of origins. Perhaps this is in the SI/Methods, but it needs to be explained in the text.

(ii) Does it matter that in A22-treated cells, the C-period is spread over two division cycles? Probably not, since the C period is constant in all conditions, but this might be mentioned?

Figure 4.

Panel AB. This is confusing (at least to this reviewer). In Panel A, the cartoon and legend say: "Two independent inter-division and timer-like replication/segregation processes with control parameters ζH and ζCD¨ = 1, respectively, must be completed before division occurs. The adder-like inter-initiation processes with control parameter ζI = 0 determines size at initiation." But in Panel B: "Model-fitting to experimental data reveals the probability pH of the inter-division process to control cell division as a function of increasing D period (with increasing A22 concentration), assuming constant control parameters ζH = 0, ζC+D¨ = 0, ζI = 0."

Why does the model in (A) use different values for ζH and ζCD¨ than those used for the model fitting?

Reviewer #3 (Recommendations for the authors):

1. It has been reported that MreB affected chromosome segregation (see Ram Madabhushi and Kenneth J. Marians, Molecular Cell, 2009, and Thomas Kruse et al., EMBO J, 2003 for details). The authors need to put this issue into discussion and/or analysis.

2. In the model, if QC+D' keeps constant, it is natural to conclude that 'inter-division process' would become more limiting (i.e., pH would increase), in the case of increased C+D periods. Since C+D' is unmeasurable, more discussion are need to explain the contribution of the experimental data to the conclusion of the model.

3. In Figure 3F, it would be helpful to show a line indicating 'always depends on DNA replication'.

4. Line 33, should be Figure 1BC.

5. Line 109-111, YPet-DnaN is used to measure periods of DNA replication. Since DnaN is reported to be associated with DNA for some time after replication is done (M. Charl Moolman et al. Nature Communications, 2014), one may overestimate the C-period in this manner.

6. There are three control parameters (𝜁H, 𝜁I and 𝜁CD′) in the model. The first two were assigned to 0 with explanation in Line 200-210. It needs more explanation of 𝜁CD′ in the main text.

7. In Figure 2B and 2C, standard deviations for each gray rectangle are missing.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Two different cell-cycle processes determine the timing of cell division in Escherichia coli" for further consideration by eLife. Your revised article has been reviewed by 3 peer reviewers and the evaluation has been overseen by Naama Barkai as the Senior Editor, and a Reviewing Editor.

The manuscript is essentially ready for publication. Please address the two remaining comments from referee 3 as you see fit, for example by editing the two figures as suggested by the referee.

Reviewer #1 (Recommendations for the authors):

Revisions are satisfactory. I have no further comment.

Reviewer #2 (Recommendations for the authors):

All concerns of this reviewer have been fully addressed in the revised manuscript.

Reviewer #3 (Recommendations for the authors):

The revision makes the manuscript much more comprehensible. I have two remaining comments:

1. Since most cell size-related models emphasize steady-state, providing further evidence that the single-cell data here were acquired during steady-state is important, as also commented by Reviewer 1. Similar to Figure 2-Supplement 2, I would recommend plotting the 'inter-division time' vs. 'Time of birth' as well, because growth rate is likely to be constant with continuous medium supply but 'inter-division time' may not, whereas steady-state requires a similar rate for both cell growth and division. Furthermore, showing these two plots for the highest A22 dosage (1 ug/mL) data or even all dosages used in the work would be a very strong evidence that the cells were in steady-state.

2. 'Initiation mass' (or initiation volume) is commonly used to refer cell size upon initiation. With altered cell width in this work, cell length is no longer a good proxy for cell mass, especially in important figures like Figure 3E. therefore, I strongly recommend to use cell volume in both axis in Figure 3E (or entire Figure 3) to precisely convey the message that the added mass becomes negatively correlated with initiation mass. The dots in Figure 3E (right panel) may also be less clustered and the trend line could be more significant, if volume is used there.
