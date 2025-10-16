# Peer review - Round 1

Editors:
- Samantha R Santacruz, The University of Texas at Austin United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.58848.sa1](https://doi.org/10.7554/eLife.58848.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The authors present a short report demonstrating the difference in neural dynamics between grasping and reaching behaviors. This work is broadly interesting to those in the field of motor control and leverages cutting-edge techniques to elucidate neural dynamics associated with the two aforementioned motor behaviors. We are enthusiastic about the suitability of this publication in eLife.

Decision letter after peer review:

Thank you for submitting your article "Neural population dynamics in motor cortex are different for reach and grasp" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Samantha R Santacruz as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Richard Ivry as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Marco Capogrosso (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

The authors present a cohesive and elegant short report demonstrating the difference in neural dynamics between grasping and reaching behaviors. The reviewers are enthusiastic about this work and agree that this study is of great interest to the field since increasingly the motor cortex is modelled as a system with strong dynamical properties. However, they find that the manuscript would be greatly strengthened by clarifications in the analyses, statistics, and animals utilized. The manuscript is suitable for publication in eLife subject to the revisions detailed below.

Essential revisions:

1) Analysis to convince the reader that motor cortical neural activity analyzed is as grasp-modulated as much as it is reach-modulated, which would control for the possibility that neural activity is just more reach-modulated so looks like reach conditions have stronger dynamics. Are the percentage of neurons modulated by the task same in grasp vs. reach (in the PSTH that you analyze)? Since these dynamics questions reflect how well changes (modulation) in firing rate are predicted, it would be important to know that the amount of modulation is comparable. Further, please clarify the point articulated in paragraph three of subsection “Control comparisons between arm and hand data”. Since firing rates are normalized before jPCA, why is analyzing the peak firing rates without normalization a valid way to "directly contrast the inputs to the jPCA analysis"?

2) Analysis to show that reach and grasp PSTHs are equally representative of individual trials, which would control for the possibility that grasp activity is just more variable trial-to-trial so analyzing the PSTH isn't representative of true dynamics. How reliable is the trial-to-trial neural activity for reach vs. grasp? Ensuring that the PSTH is equally reflective of trial activity is important for fairly comparing these two conditions.

3) Please report R2 for the neural reconstruction with LFADS for reach vs. grasp in Figure 2. This value would indicate whether using a non-linear dynamics model (LFADS) can accurately predict neural activity even in the case of grasp, which is important to do prior to any of the kinematic decoding.

4) Clarify the number of animals used for each analysis. It is difficult to understand from the results and reported figures how many animals were used and for which analysis. We suggest using a table to report this information in an accessible format. When performing statistics with data combined across animals, we also suggest using a linear mixed effect model with "animal" as a random effect.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your article "Neural population dynamics in motor cortex are different for reach and grasp" for consideration by eLife. Your revised article has been reviewed by two of the original peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Richard Ivry as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

The authors present a short report demonstrating the difference in neural dynamics between grasping and reaching behaviors. The reviewers remain enthusiastic about this work and the overall interest that it will have to the field, but there remain outstanding concerns regarding the statistics and interpretation of results. Below you will find more detailed comments. The manuscript is suitable for publication in eLifeeLife if the points detailed below can be addressed.

Revisions for this paper:

– Pertaining to Essential Revisions #3: The authors now report an R2 for the NEURAL reconstruction using LFADS for reaching and grasping. The authors have placed this result in the Materials and methods section, rather than in the Results section. Secondly and more importantly, this result is: "The average correlation between measured and reconstructed firing rates was 0.44 +/- 0.022 and 0.48 +/- 0.021 for single trials and 0.73 +/- 0.03 and 0.76 +/- 0.011 when averaged within condition, for reach and grasp respectively". This suggests that both reach and grasp NEURAL activity are equally explained by LFADS. This result appears to go against the main message of their paper (which to this point has been that there are no discernible dynamics in grasping, but there are in reaching). We would like to see this result reported in the Results section before Figure 2, and would like to see the message of the paper reflect this result (maybe something along the lines of "Grasping dynamics are high dimensional, non-linear, and can't be used for decoding with a linear decoder whereas reaching dynamics are low dimensional, linear, and can be used for decoding").

– The R2 result from above also seems to contradict the tangling results in Figure 3 (that Q-M1/Q-kinematics is higher for grasping than reaching). However upon further inspection of Figure 3, it seems like the reaching and grasping Q-kinematics are quite different (mean Q-kinematics seems to be about ~1x104 for reaching, ~0.3x104 for grasping), whereas it looks like the Q-motor cortex may be similar for both reaching and grasping. Perhaps the kinematics themselves may be driving the significant differences in the Q-ratio while the Q-motor cortex values may be comparable (which would be more consistent with the above result for approx equal R2 from LFADS)? This should be addresses in the revision.

– Pertaining to essential revisions #2: We appreciate the inclusion of panel I in Figure 1—figure supplement 2 to address this point. The main point of this question was to assess whether trial-to-trial variability affected the estimate of the PSTH and thus the ability of a linear model to capture dynamics from the PSTH. Displaying the coefficient of variation as a bar graph collapses over all temporal differences in trial-to-trial variability. For example, it is consistent within this bar plot that trial-to-trial activity is approx. uniform across the reaching behavior epoch, but for grasp is low at the beginning of the trial then high at the end of the trial for example. This hypothetical difference would make it so that the grasping PSTH is consistent at the beginning and noisy at the end, and could explain why it is harder to estimate grasping PSTH with linear dynamics. If this is the case, it may be that reach and grasp neural dynamics are not very different, just that grasp behavior tends to be more variable so the PSTH is not reflective of the true dynamics that may be ongoing during grasp. Another way to address this concern would be to report R2 of neural activity estimated from fitting dynamics on single trials and showing the same differences as in Figure 1. This gets around the issue of trial-averaging and potential trial-to-trial variability differences. We ask that the authors report this R2 value.

– There remain some overall concerns with the statistics performed. When performing statistics, data points from different subjects cannot be pooled together. This is because performing tests on pooled data violates the assumption of iid samples because part of the variance in the samples is explained by the fact that data some of the samples are from one animal and some from the other (intra-animal vs inter-animal). In this case manuscript, the authors are comparing 2 monkeys against 2 different monkeys, and everything is pooled together. We ask the authors to clarify and justify their methodology.
