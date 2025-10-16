# Peer review - Round 1

Editors:
- Richard A Neher, University of Basel Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73250.sa0](https://doi.org/10.7554/eLife.73250.sa0)

When selecting for one particular trait, it is not uncommon for other traits to change. This is due to pleiotropic mutations that affect multiple characters. Ardell and Kryazhimskiy develop a theoretical framework to predict adaptive trajectories observed in environments other than the one selection is operating in. The effects of adaptation across environments have important implication to antibiotic treatments, where resistance evolution to one antibiotic can alter the susceptibility to other antibiotics.


---

# Peer review - Round 1

Editors:
- Richard A Neher, University of Basel Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73250.sa1](https://doi.org/10.7554/eLife.73250.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "The population genetics of pleiotropy, and the evolution of collateral resistance and sensitivity in bacteria" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Richard A Neher as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Joachim Krug (Reviewer #2).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife. However, if you feel you can address the comments as outlined below, we encourage you to resubmit.

The reviewers agreed that pleiotropy of mutations and the resulting adaptive trajectories across different environment are important topics that are both of theoretical and applied interest. Your theoretical framework predicts fitness trajectories observed in environments other than the one selection is operating in (home env). These trajectories in non-home environments are calculated via integrals over the joint fitness effect distribution weighted by the fixation probability in the home environment. However, your framework assumes strong selection and weak mutation (SSWM) and deviations from this assumption seem to have strong effects. We think that these effects need to be at least partially understood. Furthermore, application to the KO library is a useful proof-of-concept, but the practical relevance of these patterns for understanding collateral sensitivity/resistance is far from obvious.

In summary, we felt that the manuscript needs to make a more substantiative theoretical advances and/or provide more robust actionable insights into drug resistance evolution to justify publication in eLife. We would be happy to reconsider this manuscript should you be able to make substantive progress towards these issues.

Reviewer #1:

Ardell and Kryazhimskiy use bacterial KO data in multiple conditions to study the structure of pleiotropy, that is the degree to which a genetic perturbation affects multiple phenotypes, and present a theoretical framework to predict and assess fitness trajectories observed in environments other than the one selection is operating in. The work is thoroughly done and has potentially interesting implications for sequential drug therapy.

The central object of their framework is the joint distribution of fitness effects of mutations in multiple environments where the distribution is over all mutations in the genome. The dynamics in the space of fitness in multiple environments is then modeled as a random walk (described by a diffusion equation) assuming that mutations sweep separated in time (SSWM). The model and the calculations necessary to arrive at the predictions are simple and transparent. The results quantitatively predict simulation results with the range of validity of SSWM. Outside this range, the model predicts the qualitative behavior, but is quantitatively wrong.

1) My main disappointment with the paper is the inability to quantitatively describe the dynamics outside the SSWM regime. I would expect that the effects of competing mutations or weak selection could be accounted for at least perturbatively. Alternative, one could determine the distribution of the effects of fixed mutations in the "home" environment in simulations and use this distribution to predict the dynamics in other environments.

2) My other substantial concern is the question whether anything can be learned about drug resistance evolution or collateral sensitivity/resistance from KO experiments. While some drug resistance evolution involves loss-of-function mutations (e.g. porin losses), it often proceeds via point mutations, up-regulation, or horizontal acquisition. Furthermore, the statistical treatment here requires many mutations to sample the joint effect distribution to give reliable answers. In clinical resistance evolution, the number of mutations observed is often quite small and their effect distributions are wide. The practical relevance of this is therefore far from clear.

3) While the similarity of this work to similar questions in quantitative genetics is discussed in the introduction, I would like to see an extended discussion whether some limits of the model at hand can be described by the quantitative genetics approach.

Reviewer #2:

The authors present a theoretical framework for analysing pleiotropic effects in populations evolving in different environments based on the concept of a joint distribution of fitness effects (JDFE). Simple correlation measures are derived from the JDFE that allow one to predict the evolutionary outcome in the non-home environment. Analytic theory is derived in the SSWM regime and complemented by simulations covering the regime of large mutation supply. A proof-of-concept application to collateral antibiotic resistance and sensitivity in bacteria based on a published data set for knockout strains is presented. Overall, this is an important, systematic contribution to very timely subject that is well suited for publication in eLife.

1. I do not quite share the authors' surprise at the outcomes shown in Figure 1. In fact, there is a simple heuristic that allows one to predict the direction of the fitness change in the non-home environment in all cases: Simply look at the y-coordinate of the tail of the JDFE corresponding to the largest beneficial effects along the x-axis.

2. Along the three rows of panels in Figure 2, there appears to be a systematic but in two cases non-monotonic variation of the slope with the mutation supply NU_b. Do the authors have a (tentative) explanation for this behavior?

Reviewer #3:

The goal of this manuscript--to develop predictive tools for inferring fitness trajectories in new environments--is an important goal and I appreciate the synthesis of theoretical modeling with parameter estimation from empirical mutation studies.

Reading through the manuscript, however, I found myself repeatedly wondering whether the stated application of the methods developed here doesn't constitute something of a tautology. This could be a misreading on my end, but I'll explain: the authors state that they have the central goal of predicting whether a population adapting to one environment will lose fitness in another "non-home" environment. Yet the parameter estimation they develop and propose for estimating fitness trajectories requires fitness measurements in both the home and non-home environments. If one already has fitness measurements for both home and non-home, how much more information is added by estimating the JDFE? I understand that the authors are estimating the fitness trajectories over time, with the incorporation of population genetic parameters, but again, I was unsure of how much information was added with the JDFE particularly given large discrepancies in the Wright-Fisher models and the decreasing predictive capacity with time. The bottom row of Figure 1 provided perhaps the most convincing evidence of the usefulness of the JDFE, but the unintuitive result was not adequately explored nor explained (see comment below). Also, perhaps an exploration of how the predictions could be extended to unmeasured environments is possible (as in Kinsler et al. 2020)?

Further specific conceptual comments and suggestions:

1) The authors demonstrate in Figure 1 that JDFEs even with similar shapes produce markedly different fitness trajectories. They argue that the correlation coefficient of the JDFE is not a reliable predictor of fitness trajectories in the home environment. I was struck by this counterintuitive result, and found myself searching for further explanation. Are the authors arguing that the practice of simply looking at the correlation coefficient in tradeoff studies in general is insufficient for predicting the fates of pleiotropic mutations? Either way, it would be helpful to the reader to elaborate on why and under which conditions the discrepancy with the correlation coefficient and fitness trajectories arises.

2) The modeling results throughout the manuscript reveal poor predictive capabilities in Wright-Fisher simulations. For example, the results in figure 2 show substantial discrepancy between the theoretical predictions and the results of the Wright-Fisher simulations. The authors address this only briefly stating that outside of the strong selection, weak mutation model (SSWM) the pleiotropy statistics are only "statistical predictors". But the discrepancy was systematic and wide, suggesting rather little insight from the pleiotropy statistics in sequential adaptation scenarios. I could not find discussion of this discrepancy between the SSWM and Wright-Fisher modeling predictions.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "The Population Genetics of Collateral Resistance and Sensitivity" for further consideration by eLife. Your revised article has been evaluated by Meredith Schuman (Senior Editor) and a Reviewing Editor.

The manuscript has been improved considerably. The reviewers particularly appreciated the more general theoretical results. However, we would like to see a more thorough discussion of previous literature. In particular, the study by Nichol et al. is important prior work that needs to be discussed in greater depth.

In addition to a more extensive discussion of the literature, we would also like to see, if at all possible, some level of empirical validation of the results beyond the KO data presented so far. The data by Stiffler et al. and Nichol et al. characterize point mutations. Using these data beyond what is currently shown in Figure S1 could be very valuable.

Reviewer #2:

The manuscript has been largely restructured and rewritten, and has improved considerably. The issues that I raised in my previous report have been adequately addressed. As requested in the previous round of reviews, the theory has been generalized beyond the SSWM regime. Moreover, a second data set on resistance mutations in β-lactamase has been added, and the discussion of the practical applicability of the approach has been extended significantly. As far as I am concerned, the paper can be accepted in its present form.

Reviewer #3:

The authors thoroughly responded to the reviewers' comments and I found the resubmission to be both clearer and to demonstrate greater prediction accuracy in the Wright Fisher simulations. The addition of the section on estimating JDFE parameters from experimental data was a positive addition to the manuscript in that it provides a bridge for experimentalists to implement the methods developed by the authors.

That being said, as an experimentalist who could potentially implement the proposed modeling in my own work for predicting tradeoffs, I am not yet convinced of the significant advance of the proposed modeling framework for making predictions. Specifically, I found the following two points to present the most significant drawbacks to the manuscript at present:

i) I found the manuscript to lack sufficient discussion of what has been shown before in the field of modeling collateral resistances and how the present manuscript presents a clear advance in light of this work. To the first point, a brief perusal of recent literature on collateral resistance brought me to Nichol et al. 2019 Nature Comm. Ardell et al. reference the Nichol manuscript on line 37 when stating that previous work observes wide variation in collateral outcomes. But Nichol et al. did more than demonstrate variation in collateral outcomes, and instead conducted 60 parallel experimental evolution assays in one antibiotic, measured the probability of collateral resistance/susceptibility and then modeled through SSWM simulations the predicted collateral resistance outcomes for dozens of drug pairs. The present manuscript should explain how its methods/goals/results differ from those of Nichol et al.

My second point is (ii) the manuscript would be significantly strengthened if it could provide proof-of-concept validations beyond the KO work and the β-lactamase work. If I understand correctly, the authors perform the drug-ranking experiments with simulated data. I am surprised that the authors cannot find a dataset in which to validate any part of the drug-ranking predictions. This type of validation would be helpful in convincing the reader of the strength of the proposed methods. As a relevant aside, Beyond Figure S1 I couldn't find where the Β-lactamase data was used and the basic conclusion stated in the text for S1 regarding variable resistance pleiotropy is already well-established in previous work.
