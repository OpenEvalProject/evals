# Peer review - Round 1

Editors:
- Jean-Jacques Orban de Xivry, KU Leuven Belgium

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.94608.3.sa0](https://doi.org/10.7554/eLife.94608.3.sa0)

This study presents an important finding on the influence of visual uncertainty and Bayesian cue combination on implicit motor adaptation in young healthy participants, hereby linking perception and action during implicit adaptation. The evidence supporting the claims of the authors is convincing. The normative approach of the proposed PEA model, which combines ideas from separate lines of research, including vision research and motor learning, opens avenues for future developments. This work will be of interest to researchers in sensory cue integration and motor learning.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.94608.3.sa1](https://doi.org/10.7554/eLife.94608.3.sa1)

I appreciate the normative approach of the PEA model and am eager to examine this model in the future. However, two minor issues remain:

(1) Clarification on the PReMo Model:

The authors state, "The PReMo model proposes that this drift comprises two phases: initial proprioceptive recalibration and subsequent visual recalibration." This description could misinterpret the intent of PReMo. According to PReMo, the time course of the reported hand position is merely a read-out of the *perceived hand position* (x_hat in your paper). Early in adaptation, the perceived hand position is biased by the visual cursor (x_hat in the direction of the cursor); towards the end, due to implicit adaptation, x_hat reduces to zero. This is the same as PEA. I recommend that the authors clarify PReMo's intent to avoid confusion.

Note, however, the observed overshoot of 1 degree in the reported hand position. In the PReMo paper, we hypothesized that this effect is due to the recalibration of the perceived visual target location (inspired by studies showing that vision is also recalibrated by proprioception, but in the opposite direction). If the goal of implicit adaptation is to align the perceived hand position (x_hat) with the perceived target position (t_hat), then there would be an overshoot of x_hat over the actual target position.

PEA posits a different account for the overshoot. It currently suggests that the reported hand position combines x_hat (which takes x_p as input) with x_p itself. What is reasoning underlying the *double occurrence* of x_p?

There seem to be three alternatives that seem more plausible (and could lead to the same overshooting): (1) increasing x_p's contribution (assuming visual uncertainty increases when the visual cursor is absent during the hand report phase), (2) decreasing sigma_p (assuming that participants pay more attention to the hand during the report phase), (3) it could be that the perceived target position undergoes recalibration in the opposite direction to proprioceptive recalibration. All these options, at least to me, seem equally plausible and testable in the future.

(2) Effect of Visual Uncertainty on Error Size:

I appreciate the authors' response about methodological differences between the cursor cloud used in previous studies and the Gaussian blob used in the current study. However, it is still not clear to me how the authors reconcile previous studies showing that visual uncertainty reduced implicit adaptation for small but not large errors (Tsay et al, 2021; Makino, et al 2023) with the current findings, where visual uncertainty reduced implicit adaptation for large but not small errors.

Could the authors connect the dots here: I could see that the cursor cloud increases potential overlap with the visual target when the visual error is small, resulting in intrinsic reward-like mechanisms (Kim et al, 2019), which could potentially explain attenuated implicit adaptation for small visual errors. However, why would implicit adaptation in response to large visual errors remain unaffected by the cursor cloud? Note that we did verify that sigma_v is increased in (Tsay et al. 2021), so it is unlikely due to the cloud simply failing as a manipulation of visual uncertainty.

In addition, we also reasoned that testing individuals with low vision could offer a different test of visual uncertainty (Tsay et al, 2023). The advantage here is that both control and patients with low vision are provided with the same visual input-a single cursor. Our findings suggest that uncertainty due to low vision also shows reduced implicit adaptation in response to small but not large errors, contrary to the findings in the current paper. Missing in the manuscript is a discussion related to why the authors' current findings contradict those of previous results.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.94608.3.sa2](https://doi.org/10.7554/eLife.94608.3.sa2)

Summary:

The authors present the Perceptual Error Adaptation (PEA) model, a computational approach offering a unified explanation for behavioral results that are inconsistent with standard state-space models. Beginning with the conventional state-space framework, the paper introduces two innovative concepts. Firstly, errors are calculated based on the perceived hand position, determined through Bayesian integration of visual, proprioceptive, and predictive cues. Secondly, the model accounts for the eccentricity of vision, proposing that the uncertainty of cursor position increases with distance from the fixation point. This elegantly simple model, with minimal free parameters, effectively explains the observed plateau in motor adaptation under the implicit motor adaptation paradigm using the error-clamp method. Furthermore, the authors experimentally manipulate visual cursor uncertainty, a method established in visuomotor studies, to provide causal evidence. Their results show that the adaptation rate correlates with perturbation sizes and visual noise, uniquely explained by the PEA model and not by previous models. Therefore, the study convincingly demonstrates that implicit motor adaptation is a process of Bayesian cue integration

Strengths:

In the past decade, numerous perplexing results in visuomotor rotation tasks have questioned their underlying mechanisms. Prior models have individually addressed aspects like aiming strategies, motor adaptation plateaus, and sensory recalibration effects. However, a unified model encapsulating these phenomena with a simple computational principle was lacking. This paper addresses this gap with a robust Bayesian integration-based model. Its strength lies in two fundamental assumptions: motor adaptation's influence by visual eccentricity, a well-established vision science concept, and sensory estimation through Bayesian integration. By merging these well-founded principles, the authors elucidate previously incongruent and diverse results with an error-based update model. The incorporation of cursor feedback noise manipulation provides causal evidence for their model. The use of eye-tracking in their experimental design, and the analysis of adaptation studies based on estimated eccentricity, are particularly elegant. This paper makes a significant contribution to visuomotor learning research.

The authors discussed in the revised version that the proposed model can capture the general implicit motor learning process in addition to the visuomotor rotation task. In the discussion, they emphasize two main principles: the automatic tracking of effector position and the combination of movement cues using Bayesian integration. These principles are suggested as key to understanding and modeling various motor adaptations and skill learning. The proposed model could potentially become a basis for creating new computational models for skill acquisition, especially where current models fall short.

Weaknesses:

The proposed model is described as elegant. In this paper, the authors test the model within a limited example condition, demonstrating its relevance to the sensorimotor adaptation mechanisms of the human brain. However, the scope of the model's applicability remains unclear. It has shown the capacity to explain prior data, thereby surpassing previous models that rely on elementary mathematics. To solidify its credibility in the field, the authors must gather more supporting evidence.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.94608.3.sa3](https://doi.org/10.7554/eLife.94608.3.sa3)

(2.1) Summary

In this paper, the authors model motor adaptation as a Bayesian process that combines visual uncertainty about the error feedback, uncertainty about proprioceptive sense of hand position, and uncertainty of predicted (=planned) hand movement with a learning and retention rate as used in state space models. The model is built with results from several experiments presented in the paper and is compared with the PReMo model (Tsay, Kim et al., 2022) as well as a cue combination model (Wei & Körding, 2009). The model and experiments demonstrate the role of visual uncertainty about error feedback in implicit adaptation.

In the introduction, the authors notice that implicit adaptation (as measured in error-clamp based paradigms) does not saturate at larger perturbations, but decreases again (e.g. Moorehead et al., 2017 shows no adaptation at 135{degree sign} and 175{degree sign} perturbations). They hypothesized that visual uncertainty about cursor position increases with larger perturbations since the cursor is further from the fixated target. This could decrease importance assigned to visual feedback which could explain lower asymptotes.

The authors characterize visual uncertainty for 3 rotation sizes in a first experiment, and while this experiment could be improved, it is probably sufficient for the current purposes. Then the authors present a second experiment where adaptation to 7 clamped errors are tested in different groups of participants. The models' visual uncertainty is set using a linear fit to the results from experiment 1, and the remaining 4 parameters are then fit to this second data set. The 4 parameters are (1) proprioceptive uncertainty, (2) uncertainty about the predicted hand position, (3) a learning rate and (4) a retention rate. The authors' Perceptual Error Adaptation model ("PEA") predicts asymptotic levels of implicit adaptation much better than both the PReMo model (Tsay, Kim et al., 2022), which predicts saturated asymptotes, or a causal inference model (Wei & Körding, 2007) which predicts no adaptation for larger rotations. In a third experiment, the authors test their model's predictions about proprioceptive recalibration, but unfortunately compare their data with an unsuitable other data set (Tsay et al. 2020, instead of Tsay et al. 2021). Finally, the authors conduct a fourth experiment where they put their model to the test. They measure implicit adaptation with increased visual uncertainty, by adding blur to the cursor, and the results are again better in line with their model (predicting overall lower adaptation), than with the PReMo model (predicting equal saturation but at larger perturbations) or a causal inference model (predicting equal peak adaptation, but shifted to larger rotations). In particular the model fits for experiment 2 and the results from experiment 4 show that the core idea of the model has merit: increased visual uncertainty about errors dampens implicit adaptation.

(2.2) Strengths

In this study the authors propose a Perceptual Error Adaptation model ("PEA") and the work combines various ideas from the field of cue combination, Bayesian methods and new data sets, collected in four experiments using various techniques that test very different components of the model. The central component of visual uncertainty is assessed in a first experiment. The model uses 4 other parameters to explain implicit adaptation. These parameters are: (1) a learning and (2) a retention rate, as used in popular state space models and the uncertainty (variance) of (3) predicted and (4) proprioceptive hand position. In particular, the authors observe that asymptotes for implicit learning do not saturate, as claimed before, but decrease again when rotations are very large and that this may have to do with visual uncertainty (e.g. Tsay et al., 2021, J Neurophysiol 125, 12-22). The final experiment confirms predictions of the fitted model about what happens when visual uncertainty is increased (overall decrease of adaptation). By incorporating visual uncertainty depending on retinal eccentricity, the predictions of the PEA model for very large perturbations are notably different from, and better than, the predictions of the two other models it is compared to. That is, the paper provides strong support for the idea that visual uncertainty of errors matters for implicit adaptation.

(2.3) Weaknesses

Although the authors don't say this, the "concave" function that shows that adaptation does not saturate for larger rotations has been shown before, including in papers cited in this manuscript.

The first experiment, measuring visual uncertainty for several rotation sizes in error-clamped paradigms has several shortcomings, but these might not be so large as to invalidate the model or the findings in the rest of the manuscript. There are two main issues we highlight here. First, the data is not presented in units that allow comparison with vision science literature. Second, the 1 second delay between movement endpoint and disappearance of the cursor, and the presentation of the reference marker, may have led to substantial degradation of the visual memory of the cursor endpoint. That is, the experiment could be overestimating the visual uncertainty during implicit adaptation.

The paper's third experiment relies to a large degree on reproducing patterns found in one particular paper, where the reported hand positions - as a measure of proprioceptive sense of hand position - are given and plotted relative to an ever present visual target, rather than relative to the actual hand position. That is, (1) since participants actively move to a visual target, the reported hand positions do not reflect proprioception, but mostly the remembered position of the target participants were trying to move to, and (2) if the reports are converted to a difference between the real and reported hand position (rather than the difference between the target and the report), those would be on the order of ~20{degree sign} which is roughly two times larger than any previously reported proprioceptive recalibration, and an order of magnitude larger than what the authors themselves find (1-2{degree sign}) and what their model predicts. Experiment 3 is perhaps not crucial to the paper, but it nicely provides support for the idea that proprioceptive recalibration can occur with error-clamped feedback.

Perhaps the largest caveat to the study is that it assumes that people do not look at the only error feedback available to them (and can explicitly suppress learning from it). This was probably true in the experiments used in the manuscript, but unlikely to be the case in most of the cited literature. Ignoring errors and suppressing adaptation would also be a disastrous strategy to use in the real world, such that our brains may not be very good at this. So the question remains to what degree - if any - the ideas behind the model generalize to experiments without fixation control, and more importantly, to real life situations.
