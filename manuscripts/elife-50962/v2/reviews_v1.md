# Peer review - Round 1

Editors:
- Kunlin Wei, Peking University China

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.50962.sa1](https://doi.org/10.7554/eLife.50962.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The study investigates how activity in a specific region of the frontal eye field changes when smooth pursuit eye movements switch from preparation to execution. They propose a novel framework based on visuomotor gain to account for the behavioural and neural data collected from monkeys, different from the movement potent framework that has been previously proposed for the skeletomotor system.

Decision letter after peer review:

Thank you for submitting your article entitled "Mechanisms that allow cortical preparatory activity without inappropriate movement" for peer review at eLife. Your article is being evaluated by three peer reviewers, and the evaluation is being overseen by a Reviewing Editor and Joshua Gold as the Senior Editor.

After consultation with each other and with the Reviewing Editor and Senior Editor, the reviewers have identified a list of essential revisions, involving extensive new analyses, which are listed below.

The present study aims to understand whether pseudo-population activity of FEFsem neurons is better explained by a visual-motor gain hypothesis or by the movement-potent/null space framework for the skeletomotor system. Using a brief pulse of visual motion during the preparatory period to produce transient eye motion during fixation, the authors found that the size of eye motion is modulated by factors such as the timing of pulse within the fixation period, direction of pulse motion, and expectation of target speed. This result was interpreted as matching the predictions of the visuomotor gain hypothesis. The authors further found that: 1) an optimal linear model, parameterized by weight estimates from one smooth pursuit task with 8 directions, was used on the same FEFsem neuron population during the preparatory period, and the model predictions appeared to match the actual eye velocity during fixation when there wasn't any; and 2) the principal components (PCs) of the population response measured during preparatory and movement initiation phases were separated by about 65 deg, as opposed to 90 deg as predicted by the movement-null space framework. These results were interpreted as evidence against the movement-null space framework.

All three reviewers (including the reviewing editor) find this paper interesting, well-written, and timely for the field. However, they converged on a common set of concerns about the data analysis.

1) The evidence against the movement-null space frame is indirect. For example, the approach is to find the preparatory subspace in one task and look at what happens in another task. Extensive additional analyses are needed to make the current work comparable to the studies (e.g., Kaufman et al.).

2) Some data analyses are confusing, such as artificially rotating the tuning of some neurons to build a neural space that sometimes includes the same neuron on different axes. These analyses should be either simplified or more clearly explained and justified.

3) The PCA analysis should be improved; e.g., using dPCA.

4) It would be meaningful and necessary to applied subspace analysis to the data from the experiment that provided the behavioral evidence (e.g., Figure 2).

Reviewer #1:

In this manuscript Darlington and Lisberger address the question how preparatory activity in the smooth pursuit eye movement system is prevented from actually driving eye movements. Different solutions have been proposed for different motor systems. The saccadic eye movement system has a gate (omnipause neurons) preventing preparatory activity from activating burst neurons. An analysis of primary motor and premotor activity in the arm movement system has shown that preparatory population activity avoids state space dimensions that result in driving motor output. For the smooth pursuit eye movement system, the authors propose that preparatory activity in the frontal eye field (FEF) controls the gain of a sensorimotor transformation process that is actually driven by visual motion information. An analysis of the FEF population activity indicated that the preparatory activity does not completely avoid the dimensions related to motor output, such that the preparatory activity would be expected to cause eye movements if the neural activity in FEF were responsible for driving smooth pursuit.

1) One of the key elements supporting the authors' claims is a comparison of the time course of preparatory activity in FEF with the time course of the behavioral effect of brief motion pulses. Ideally, these data would have been collected in a combined experiment. For this manuscript they were collected in separate experiments. This is not necessarily problematic as they were collected from the same monkeys. However, both time courses are likely affected by the animals' temporal expectations about upcoming eye movements. The timing of the experiments (distribution of time intervals between fixation onset and onset of the continuous motion cue driving pursuit, not the pulses) should therefore have been identical to be able to make the assumption that the animals' expectation was probably similar. The manuscript is not explicit about whether this was the case. Was it?

Other than that, I don't have any major issues. The data analysis is solid, and the manuscript is very clearly written.

Reviewer #2:

Darlington and Lisberger present a well-written and interesting study that explores how activity in a specific region of the frontal eye field (FEFsem) transitions between preparation and execution of smooth pursuit eye movements. The overall objective is to understand whether pseudo-population activity of FEFsem neurons is better explained by the visual-motor gain hypothesis, originally developed by Lisberger and colleagues, or by the movement-potent/null space framework championed recently by Shenoy and colleagues for the skeletomotor system. The authors provide three results that, in their opinion, support the visual-motor gain hypothesis and refute the movement-null space perspective. I will summarize the three findings and then evaluate the authors' interpretations.

1) Injecting a brief pulse of visual motion during the preparatory period produces transient eye motion during fixation. The size of eye motion depends on several factors (when during the fixation period, direction of pulse motion, and expectation of target speed). The authors view the results as consistent with and build logically on the visual-motor gain hypothesis as a mechanism for movement initiation, particularly smooth pursuit. In my view, their interpretation is reasonable.

2) As a test of the movement-potent space hypothesis, the authors estimate the contribution of each neuron/condition to the initiation of smooth pursuit during one task condition (8 directions randomly interleaved). They then use these weights on the preparatory activity of the same population during a different task (repeat trials of same direction) and find that the model predicts changes in eye velocity (during fixation) when there isn't any. This finding is interpreted as evidence against the movement-potent space framework.

In my view, the analysis is not rigorous enough to reach this conclusion. Is it safe to assume, as the authors seem to do, that the population response for movement initiation during the two tasks is the same? How well do the weights for the 8D task predict pursuit initiation for the 1D task? Also, how well do weights obtained from 1D task during pursuit predict eye velocity during preparation in the same 1D task? These factors must be addressed before appreciating the importance of the result emphasized in the manuscript. Also see dPCA comment below.

3) In a related analysis, the authors evaluated the principal components (PCs) of the population response measured during preparatory and movement initiation phases. They found that the 1st PC for each period accounts for ~70% of the variance and that the mean angle between these PCs is about 65 deg, which is not equal to the 90 deg required if preparatory period activity is in a movement-null space. In addition, they identified a subpopulation of neurons that accounts for the observed change in angle between the PCs.

Given that the angle of separation between the primary preparatory and movement PCs is not 90 deg, the authors de-emphasize the potential importance of the movement potent/null space framework and instead view favorably the visual-motor gain hypothesis. However, they do state, "two mechanisms for preventing movements might be better than one". My view on their data is that the population FEFsem definitely resides in different subspaces during preparatory and movement initiation periods. In other words, if we relax a strict interpretation of orthogonality of movement and null subspaces, then these data are very much in line with potent/null space framework. This very much contrasts the take-home message the authors deliver.

Moreover, it is not clear that PC analysis is the best/correct analysis to use for the current data. The authors should consider using demixed principal component analysis (dPCA; https://elifesciences.org/articles/10989; https://www.eneuro.org/content/3/4/ENEURO.0085-16.2016.long). An interesting outcome of previous studies using dPCA is that the primary PCA is generally condition independent and could reflect the large overlap in angle between the PCs. A separation is more appreciable with secondary and tertiary PCs. The authors should pursue this angle of inquiry.

Finally, there is a glaring omission in the analysis. The first part of the paper shows a robust behavioral result, in which a brief visual motion perturbation produces an eye movement during a period typically associated with movement preparation. What subspace is spanned by FEFsem population during the transient eye movement response? Does the activity remain aligned with preparatory PCs (evidence against functional importance of movement-null space) or does it shift to movement PCs (evidence to support the movement-potent hypothesis)? It seems to me that this analysis is crucial to understand population activity control of smooth pursuit by FEFsem.

In summary, a study of how population activity relates to movement preparation and generation is timely. Tests of whether new hypotheses developed in skeletomotor systems generalize to the oculomotor system is very much needed, and this study takes a step in the direction. However, the analysis isn't rigorous enough to reach a reliable conclusion.

Reviewer #3:

Darlington and Lisberger present a previously undescribed "mechanism" by which the smooth eye movement (SEM) region of FEF could prepare pursuit movements without causing them -by dialing up the visuomotor gain. Moreover, they provide evidence in the SEM system against the "null subspace" hypothesis of preparation of arm movements. I find many aspects of the manuscript interesting but I have some concerns about their analytical approach

Comments:

1) Although I think that the potential differences in control of reaching movements and pursuits are interesting, I have concerns about how the authors tested the "null subspace" hypothesis. Overall, I think that the authors should replicate the methods proposed by Kaufman et al., rather than introduce a number of modifications whose implications are hard to grasp -at least for me. In more detail:

1a) All subspace analyses putatively capture activity that reflects some aspect of the underlying circuitry as well as the task (e.g, related to inputs to the neural population or outputs). However, the authors find the null subspace in a lower-dimensional version of the task that they probe (1-targets vs. 8-targets) that is also -I think- cued differently. My suggestion is that they do the analysis using the full 8-target data and considering the preparatory and pursuit epochs as Kaufman et al. did.

1b) Studies like Kaufman's assume that the relevant "neural information" is captured by activity patterns shared across the neural population; these patterns are probed by analyzing a state space in which axis is the activity of one recorded neuron. The authors adopted an approach that puzzled me: having multiple axes that reflect the same neuron after rotating its activity. I'd again suggest them to adopt the simpler approach of defining one axes per neuron, discarding neurons that were recorded multiple times during different conditions (at least I have trouble foreseeing all potential implications of their manipulations)

1c) I am again a bit confused about the potential effect of the authors rotating the tuning curves of each neuron in the analysis. Although I agree that there may be FEF neurons with these properties, I would avoid it because it implies assuming that the absolute coordinates of the target doesn't matter, or at least show that it doesn't influence the main result.

1d) Did the authors include all the recorded neurons in this analysis or only neurons that were significantly tuned to the task? Although studies in the motor cortices suggest that the population dynamics sampled from sufficiently large neural populations are the same irrespective of the sampled neurons (Trautman et al., 2018), I worry this may bias their results.

1e) Because of these concerns, I believe that the authors should repeat Figure 8 after calculating the preparatory and pursuit PCs as in Kaufman et al., 2014.

1f) Minor: I assume that the authors only compare the first pursuit PC and the first preparatory PC because they each capture a large fraction of the total neural variance. For a full assessment, I'd suggest an analysis like the one in Figure 4 of Elsayed et al., 2016, or the principal angle analysis used in Gallego et al., 2018.

2) The central idea of "gain control" is interesting, but I think the authors should pursue it further. For example, can single trial eye speed be predicted from neural activity? (I'd do this analysis for the data in Figure 2 and 3). Also, how do the authors think this gain leads to a transition from preparation to movement, by exceeding a threshold? I think some analyses and discussion in this regard are missing.

3) In the Results section the authors make the proposal that there may be "non-specific preparatory enhancement of visuomotor gain". I think they could address this directly by using demixed principal component analysis (dPCA) (Kobak et al., 2016). dPCA effectively performs semi-supervised dimensionality reduction and can be used to isolate population activity patterns that only depend on time (these would be the component the authors refer to) and components that depend on the direction of the movement (see, e.g., Kaufman et al., 2016, Gallego et al., 2018 for examples in motor cortex). Examining both the dynamics of these components (e.g., when do putative time-related and target-related components start ramping up?) and the weights (e.g., are there subpopulations of neurons?) could be interesting. Note that there's freely available code by Kobak et al.

4) Figure 2 shows strong effects, but it would be nice to see the data distributions, or at least box plot versions of (b) and (c). As to (d), would the authors see the same trend if they plotted single trial values or a 2D histogram? This figure focuses in neurons that had "positive preparatory firing rate modulation". What was their percentage among all recorded neurons? And among all modulated neurons? And what happens with these neurons? Same for the increase and decrease cells in Figure 3.

References:

GF Elsayed, AH Lara, MT Kaufman, MM Churchland and JP Cunningham. Reorganization between preparatory and movement population responses in motor cortex. Nature Communications 2016

JA. Gallego, MG. Perich, SN. Naufel, C Ethier, SA Solla and LE Miller. Cortical population activity within a preserved neural manifold underlies multiple motor behaviors. Nature Communications 2018

MT Kaufman, JS Seely, D Sussillo, SI Ryu, KV Shenoy and MM Churchland. The Largest Response Component in the Motor Cortex Reflects Movement Timing but Not Movement Type. eNeuro 2016

D Kobak, W Brendel, C Constantinidis, CE Feierstein, A Kepecs, ZF Mainen, X-L Qi, R Romo, N Uchida, C Machens. Demixed principal component analysis of neural population data. eLife 2016

MG Perich, JA Gallego, LE Miller. A Neural Population Mechanism for Rapid Learning. Neuron 2018

EM Trautmann, SD Stavisky, S Lahiri, KC Ames, MT Kaufman, DJ O'Shea, S Vyas, X Sun, SI Ryu, S Ganguli, KV Shenoy. Accurate estimation of neural population dynamics without spike sorting. Neuron 2018

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Mechanisms that allow cortical preparatory activity without inappropriate movement" for further consideration by eLife. Your revised article has been evaluated by Joshua Gold (Senior Editor), a Reviewing Editor, and two of the original reviewers.

The manuscript has been improved substantially. The addition of new analyses as well as the justification for why other requested analyses are not needed were satisfactory. Overall, the revised version is well written and of strong impact. It pushes back a bit against the increasingly dogmatic view of movement-potent and movement-null subspaces.

We have one remaining major concern that should be addressed:

1) It would be interesting to a) recompute weights relating FEFsem activity to eye velocity separately for subpopulations 1 and 2, and (b) predict eye velocities for each. Is there a difference in the predictive power for the two subpopulations? And how well do the results align with the proposed role of each subset (including for different directions)? A new figure can probably be committed to the results.
