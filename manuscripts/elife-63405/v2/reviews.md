# Peer review - Round 1

Editors:
- Adrien Peyrache, https://ror.org/01pxwe438 McGill University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63405.sa0](https://doi.org/10.7554/eLife.63405.sa0)

This paper investigates the importance of visual and inertial sensory cues as well as the underlying motion dynamics to the accuracy of spatial navigation. When motion control was artificially manipulated in a virtual environment, subjects could navigate accurately using vision, but not inertial signals alone. Overall, these findings shed new light on how the brain combines sensory information and internal models of control dynamics for self-motion perception and navigation.


---

# Peer review - Round 1

Editors:
- Adrien Peyrache, https://ror.org/01pxwe438 McGill University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63405.sa1](https://doi.org/10.7554/eLife.63405.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Influence of sensory modality and control dynamics on human path integration" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Richard Ivry as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Benjamin Clark (Reviewer #1); Gunnar Blohm (Reviewer #2); Stefan Glasauer (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this manuscript, the authors investigated the importance of visual and vestibular sensory cues and the underlying motion dynamics to the accuracy of spatial navigation by human subjects. A virtual environment coupled with a 6-degrees of motion platform, as described in prior studies, allowed precise control over sensory cues and motion dynamics. To investigate whether control dynamics influence performance, the transfer function between joystick deflection and self-motion velocity was modified at each trial, resulting in subject to rely more on velocity or acceleration to find their way. To explain the main result that navigation error depends on control dynamics, the authors propose a probabilistic model in which an internal estimate of dynamics is biased by a strong prior. Overall, the three reviewers agree this manuscript might be suitable for publication in eLife and that additional data are not necessary. However, the analyses need to be clarified and the conclusion better justified. You will find below a summary of the main concerns. Please refer to the reviewers' comments appended at the end for more details.

Essential revisions:

1. Concerns were raised regarding motion cueing that was used to approximate the vestibular cues that would be present during real motion. The reviewers think that it should be better to refrain from generalizing and to restrict the conclusions to this specific artificial type of vestibular input. It could even by interesting, since motion cueing is used in driving simulators. See reviewer #2, point #3 and reviewer #3, point #3.

2. One possible interpretation of the data is that the subjects rely almost exclusively on sensory feedback, and that no estimate of control dynamics is necessary. One caveat of the current design is that the different trial types were interleaved, possibly resulting in unreliable efferent copies (leading subjects to estimate velocity from sensory inputs only) and a history effect in the estimation of tau (biasing vestibular trials). The authors should provide more evidence that their effect is not the result of feedback control only and that there is no history effect. See reviewer #2 point #2 and reviewer #3, point #1-2.

3. The relationship between tau and performance is unclear and should be clarified. Figure 3A seems to contradict Figure 5A. See reviewer #2, point #1.

4. It is unclear why the authors did not propose a more normative framework, e.g. using a hierarchical Bayesian model, as suggested in the discussion. This would be a very interesting addition to the manuscript. See reviewer #2 point #4.

5. The manuscript lack important information and details: number of trials, maximal velocity, difference between males and females, slope of the dependence between time constant and error. The actual control signal, the joystick command, should be shown and analyzed. See reviewer #1, point #1-2; reviewer #3, point #4-5.

6. It seems that tau was correlated with trial duration and velocity (Supp Figure 4), unlike what is stated in the manuscript (the effect of both factors are said to be "unlikely" p 161-167). The author should clarify this point. See reviewer #3, point #5.

7. Data presentation can be improved. See reviewer #1 point #3-5.

Reviewer #1:

1) The study tested performance by both male and female subjects. Could the authors comment as to whether sex differences were observed across performance measures? Perhaps sex can be indicated in some of the scatter plots.

2) Figure 2A. It would be helpful if the authors identified the start-point of the trajectory and also provided more explanation of the schematic in the caption.

3) Figure 2B-C. It would be helpful if the authors could expand this section to show some example trajectories and the relationship between examples and plotted data points. This could be done by presenting measures (radial distance, angular eccentricity, grain) for each example trajectory.

4) Because the range of sampled time-constants can vary across subjects, it would nice to show plots as in Figure 3B for each subject (i.e., in supplementary material).

5) Discussion. The broader implications of the findings from the models are not sufficiently discussed. In addition, some comparison could also be made to other recent efforts to model path integration error (e.g., PMC7250899).Reviewer #2:

The authors asked how the brain uses different sensory signals to estimate self-motion for path integration in the presence of different movement dynamics. They used a new paradigm to show that path integration based on vision was mostly accurate, but vestibular signals alone led to systematic errors particularly for velocity-based control.

While I really like the general idea and approach, the conclusions of this study hinge on a number of assumptions for which it would be helpful if the authors could provide better justifications. I also have some clarification questions for certain parts of the manuscript.

1) lines 26-7: "performance in all conditions was highly sensitive to the underlying control dynamics". This is hard to really appreciate from the residual error regressions in Figure 3 and seems to be contradicting Figure 5A (for vestibular condition). A more explicit demonstration of how tau affects performance would be helpful.

2) One of the main potential caviats I see in the study design is the fact that trial types (vest, visual, combined) were randomly interleaved. In the combined condition, this could potentially result in a form of calibration of the vestibular signal and/or a better estimate of tau that then is used for a subsequent vestibular-only trial. As such, you'd espect a history effect based on trial type more so (or in addition to) simple sequence effects. This is particularly true since you have a random walk design for across-trial changes of tau. In other words, my question is whether in the vestibular condition participants simple use their previous estimate of tau, since that would be on average close enough to the real tau?

3) I thought the experimental design was very clever, but I was missing some crucial information regarding the design choices and their consequences. First, has there been a psychophysical validation of GIA vs pure inertial acceleration? Second, were GIAs always well above the vestibular motion detection threshold? In other words could the worse performance in the vestibular condition be simply related to signal detection limitations? Third, how often did the motion platform enter the platform motion range limit regime (non-linear portion of sigmoid)?

4) lines 331-345: it's unclear to me why you did not propose a more normative framework as outlined here. Especially, a model that would "contrain the hypothesized brain computationa dn their neurophysiological correlates" would be highly desirable and really strengthen the future impact of this study.

5) I would highly recommend all data to be made available online in the same way as the analysis code has been made available.Reviewer #3:

The manuscript describes interesting experimental and modelling results of a novel study of human navigation in virtual space, where participants had to move towards a briefly flashed target using optic flow and/or vestibular cues to infer their trajectory via path integration. To investigate whether control dynamics influence performance, the transfer function between joystick deflection and self-motion velocity was modified trial-by-trial in a clever way. To explain the main result that navigation error depends on control dynamics, the authors propose a probabilistic model in which an internal estimate of dynamics is biased by a strong prior. Even though the paper is clearly written and contains most of the necessary information, the study has several shortcomings, as outlined below, and an important alternative hypothesis has not been considered, so that some of the conclusions are not fully supported by results and modelling.

Substantive concerns

1) The main idea of the paper for explaining the influence of control dynamics is that for accurate path integration performance participants have to estimate dynamics. This idea is apparently inspired by studies on limb motor control. However, tasks in these studies are often ballistic, because durations are short compared to feedback delays. In navigation, this is not the case and participants can therefore rely on feedback control (for another reason, why reliance on sensory feedback in the present study is a good idea, see point 2 below). This means that the task can be solved, even though not perfectly, without actually knowing the control dynamics. Thus, an alternative hypothesis for explaining the results that has not been considered is that the error dependence of control dynamics is a direct consequence of feedback control. Feedback control models have previously been suggested for goal-directed path integration (e.g., Grasso et al., 1999; Glasauer et al., 2007).

To test this assumption, I modelled the experiment assuming a simple bang-bang feedback control that switches at a predefined and constant perceived distance from the target from +1 to -1 and stops when perceived velocity is smaller than an epsilon. Sensory feedback is perceived position, which is assumed to be computed via integration of optic flow. This model predicts a response gain of unity, a strong dependence of error on time constant (slope similar to Figure 3) or of response gain on time constant (Equation 4.1) with regression coefficients of 0.8 and 0.05 (cf. Figure 3D), and a modest correlation between movement duration and time constant (r approximately 0.2, similar to Figure 3A). Thus, a feedback model uninformed about actual motion dynamics and without any attempt to estimate them can explain most features of the data. Modifications (velocity uncertainty, delayed perception, noise on the stopping criterion, etc.) do not change the main features of the simulation results.

Accordingly, since simple feedback control seems to be an alternative to estimating control dynamics in this experiment, the authors’ conclusion in the abstract “that people need an accurate internal model of control dynamics when navigating in volatile environments” is not supported by the current results.

2) Modelling: the main rationale of the model (line 173 ff: “From a normative standpoint, …”) is correct, but an accurate estimate of the dynamics is only required if the uncertainty of the velocity estimate based on the efference copy is not too large. Otherwise, velocity estimation should rely predominantly on sensory input. In my opinion that’s what happens here: due to the trial-by-trial variation in dynamics, estimates based on efference copy are very unreliable (the same command generates a different sensory feedback in each trial), and participants resort to sensory input for velocity estimation. This results in feedback control, which, as mentioned above, seems to be compatible with the results.

3) Motion cueing: Motion cueing can, in the best case, approximate the vestibular cues that would be present during real motion. Furthermore, it is not clear whether the applied tilt is really perceived as linear acceleration, or whether the induced semi-circular canal stimulus is too strong so that subjects experience tilt. Participants might have used the tilt has indicator for onset or offset of translational motion, specifically because it is self-generated, but the contribution of the vestibular cues found in the present experiment might be completely different from what would happen during real movement. Therefore, conclusions about vestibular contributions are not warranted here and cannot solve the questions around “conflicting findings” mentioned in the introduction.

4) Methods: I was not able to find an important piece of information: how many trials were performed in each condition? Without this information, the statistical results are incomplete. It was also not possible to compute the maximal velocity allowed by joystick control, since for Equation 1.9 not just the displacement x and the time constant is required, but also the trial duration T, which is not reported. One can only guess from Figure 1D that vmax is about 50 cm/s for tau=0.6 s and therefore the average T is assumed to be around 8.5 s.

5) Results: information that would useful is not reported. On page 6 it is mentioned that the “effect of control dynamics must be due to either differences in travel duration or velocity profiles”, it is then stated that both is “unlikely”, but no results are given. It turns out that in the supplementary Figure 4A the correlation between time constant and duration/velocity is shown, and apparently the correlation with duration is significant (but small) in the majority of cases. Why is that not discussed in the Results section? Other results are also not reported, for example, what was the slope of the dependence between time constant and error? Why is the actual control signal, the joystick command, not shown and analyzed?

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled “Influence of sensory modality and control dynamics on human path integration” for further consideration by eLife. Your revised article has been evaluated by Richard Ivry (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but reviewer #3 has raised several issues that need to be addressed, as outlined below:

Reviewer #3:

The present version of the manuscript has clearly improved, and the authors responded adequately to the comments, and a link to the data was also provided. Some very helpful additional analysis was added, such as shown in Figure 3E. There are, however, some critical points left which are outlined below.

Introduction, line 83f: “These findings suggest that inertial cues alone lack the reliability to support accurate path integration …” Even though in general I’d agree with this statement, the findings in the current paper do not support this claim. Since the inertial cues were generated by motion cueing rather than being natural, it could be that natural inertial cues would yield much better path integration performance. Please change accordingly. See also next comments.

Figure 1 suppl. 2: I agree that the initial tilt cannot contribute to linear path integration, but if it is processed by the central estimator (see, for example, your co-author Jean Laurens’ models), it would change the perceived orientation of the participant to a tilted position. Consequently, the GIA after the tilt would be correctly perceived as being due to tilt, this means it would not be interpreted as resulting from linear displacement, and vestibular input would not at all, or only to a very little part, be used as input to the path integration system. This could be an explanation for the findings of inferior performance in the vestibular condition (see comment above). It would mean that motion cueing as applied here is not appropriate for simulating linear travel, which would be an important finding for designing driving simulators. Please discuss …

Results, page 4: it seems that the fit for the combined condition, specifically for distance (both in terms of R2 and of response gain), was worse than for the visual condition. This would be surprising, since adding a second sensory input should not have that effect. However, if the vestibular stimulus, specifically for distance, is not appropriate, then this is exactly what should happen. A conflicting vestibular stimulus could decrease response gain (and the fit).

Results, page 6, line 164ff: “A partial correlation analyses revealed..” A summary statistical result should be shown here as well to support the result of time constant dependence.

Line 165: “…albeit only by modulating the distance dependence” I first misunderstood this and thought it would only modulate radial distance dependence. After looking at Figure 3 suppl 2: maybe better write “…albeit only by modulating both angular and radial distance dependence.”

Figure 5: text in figure caption is missing (probably due to clipping of the text box).

Results page 12-13, Bayesian model: I’m surprised that both SD of likelihood and prior were free parameters. For a Bayes model with Gaussian distributions and fixed prior, only the quotient of both standard deviations is a free parameter (the model is basically equivalent to a weighted sum of the mean of prior and the measurement, with the weight being determined by the quotient of the variances). So, either I misunderstand your model, or there’s a mistake. If the latter is the case, then Figure 6 and the corresponding results are also partly wrong, since likelihood σ and prior σ cannot be determined on their own, but only their quotient. See next comment, I suppose there is really a mistake.

Results page 14, dynamic prior model: here you can easily see from equation 7 (page 25) that there are in fact only 2 free parameters, not three (as you state), if you re-express the weight k: the weight k is given as k=varp/(varp+varm)=1/(1+varm/varp). So only varm/varp is free, not both, you cannot determine both from the fit. Note: in this model, it is usually sufficient to take the first measurement as mean of the first prior (corresponding to a maximum likelihood estimate on the first trial, or uninformative prior). This reduces the model to one free parameter.

Discussion, line 343-344: “In contrast, inertial (vestibular/somatosensory cues) alone lacked the reliability to support accurate path integration …” this is the case for the motion cueing inertial cues, so please make clear here and at other points that your data only refer to this type of inertial cues.

Discussion: I miss a general discussion of the limits of the study due to using motion cueing. As mentioned several times, the results concerning the vestibular and combined conditions of this study cannot be generalized to vestibular stimuli under natural conditions.

Along these lines I’m also very puzzled to read in the authors’ responses the following statement: “Therefore, there is no need to ensure that these accelerations are perceived identically: they are identical.”

(This reminds me of an astronaut who once stated that there is no need to study perception of up and down in space, because in weightlessness there is no up and down.)

Two identical linear accelerations can very well be perceived completely differently depending on the rotational history and context. That’s the reason why we perceive a tilt of the head as what it is, and not as rapid linear displacement. Please ask your coauthors Dora Angelaki and Jean Laurens, who are long enough in the field to know this. And this is extremely relevant in the present context.
