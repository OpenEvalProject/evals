# Peer review - Round 1

Editors:
- Arianna Maffei, Stony Brook University United States

Reviewers:
- Arianna Maffei, Stony Brook University United States
- Asif A Ghazanfar, Princeton University United States
- Justus Verhagen, The John B Pierce Laboratory/Yale United States
- Luca Mazzucato, University of Oregon United States

## Review text

DOI: [10.7554/eLife.45968.011](https://doi.org/10.7554/eLife.45968.011)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Dynamical structure of cortical taste responses revealed by precisely-timed optogenetic perturbation" for consideration by eLife. Your article has been reviewed by four peer reviewers, including Arianna Maffei as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Laura Colgin as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Asif A Ghazanfar (Reviewer #2); Justus Verhagen (Reviewer #3); Luca Mazzucato (Reviewer #4).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

There is general consensus that the manuscript by Mukherjee et al. provides a significant contribution to our understanding of how sensory perception drives action. Overall, the reviewers agreed that the experimental methods and the overall framework of the study are strong and that the results support the authors' conclusions. There are a few concerns regarding the description of the data and controls as well as a few suggestions to strengthen the paper's conclusions further by additional analyses.

Essential revisions:

A more descriptive title would be beneficial. The current title is pretty generic.

The description and justification of control conditions should be expanded. In a number of places in the manuscript there is lack of clarity as to which control is being referred: no opto, short opto, long opto. Moreover in Figure 5 there are a 2.5s control and a 0.5 control. A better way to refer to controls across the manuscript would be helpful, as would be a better description and justification for the choices of controls. An additional justification for why the authors chose to use light off control conditions instead of reporter-only viral injections should be provided.

Figure 3A would be more compelling if the regression coefficient analysis was reported also for 0.5s inactivation.

Figure 4 needs clarification as it is not clear what panel B1 and B2 are reporting. In addition, a description of Figure 6 is lacking in the Results.

Regarding the statistical methods used for the study, the authors spend a long portion of the methods describing and discussing Bayesian methods, but their analysis does not fully apply them to determine change points intervals. This would certainly strengthen the quantification of the transitions between epochs and provide a stronger quantification of the data. For example, one can assign a prior distribution on the intervals where change points CI and CP are concentrated according to the authors' definition in the first paragraph of the subsection “Modeling and change-point identification in ensemble firing data” (and Figure 6). These change points, if estimated for each session, would change the M-step, leaving the hard E-step unchanged. For clarity, it would also be useful to write down the full E-M equations and what modification of standard EM procedures lead to the "hard assignment" case used here.

The authors should perform the same CP analysis in Figure 7 to the other 2 conditions where laser ON occurred during 0-0.5s and 1.4-1.9s intervals. This is a necessary control to support the claim that only perturbations occurring at 0.7-1.2s affect gaping. Finally, in Figure 4 change point analysis would allow to better estimate when the cumulative sum of the KL divergence changes abruptly, under the hypothesis that the cumsum is piecewise linear.
