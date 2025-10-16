# Peer review - Round 1

Editors:
- Michael J Frank, Brown University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.30150.020](https://doi.org/10.7554/eLife.30150.020)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Associability-modulated loss learning is increased in posttraumatic stress disorder" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Richard Ivry as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This study addresses the question of how the hypervigilance in PTSD patients can be accounted for from a computational psychiatric perspective. The authors provided both behavioral modeling and neuroimaging data to support the hypothesis that allocation of attention (associability weight) is higher in the PTSD compared to the control subjects; neural markers associated with associability but not prediction error, such as amygdala and insula showed elevated activity in PTSD during loss learning. This is a well-written and timely research article with interesting results. The quantitative approach to a specific clinical population should be of interest to a wide audience of basic research and translational studies.

Essential revisions:

1) Both reviewers noted that the modeling part was potentially more complex than needed. For example, the paper specified reward sensitivity and learning rate. However, these two parameters might covariate in parameter estimation. They also separated the chosen and unchosen option learning rates yet did not run a nested model comparison to test whether these additional parameters are necessary. From an empirical perspective, the authors might want to restrict their model to a simpler one or provide enough evidence to support a more complicated one. Also, Equation 3 does not seem to make sense as currently written.

2) Please add some additional detail regarding the task to the main text. It is difficult to understand the model without understanding the task. Within the task description in the supplemental materials, several aspects of the task remain unclear:

- What was the probability of better/worse outcomes for the less rewarded stimulus?

- What was the probability distribution of payoffs within the specified ranges, i.e. within 20-30 or 70-80 (uniform, Gaussian, etc.)?

- Were outcomes shown for both chosen and unchosen stimuli? If not, how did subjects learn from the unchosen stimulus?

3) The authors might want to clarify the logic behind titrating the length of the task to achieve certain level of better choice selection rates. Different performance in the task itself is a behavioral marker between the control and PTSD groups. In fact, Figure 2A suggests that there is a difference in performance between the groups. Also, given the design of the task, gain and loss blocks alternated. Within the gain block, associability in general shows a declining trend. Thus, it is important to disentangle a non-specific adaptation signal from the associability signal that the paper focuses on.

4) There are significant problems with the conceptual interpretation of the results:

-Based on the equations, associability value is expected (unsigned) prediction error:

Equation 6 can be rewritten as 𝛋A(t + 1) = 𝛋A(t) +η(|𝛅 t | – 𝛋A(t))

Associability weight is the learning rate in learning this associability value (i.e. in learning expected unsigned prediction error). Presumably, this learning rate should be high if the prediction errors themselves are expected to be more likely to change over time.

If this interpretation is correct, many descriptions of associability weight in the text are misleading. For example, "behavioral parameter estimates of associability…increased with PTSD" (Abstract), "[Associability weight] indicates the extent to which the magnitude of previous prediction errors is used to update trial-by-trial associability values", "associability weights, reflecting the degree to which stimulus values are modulated or not by associability during loss learning for each participant". Associability weight is actually a learning rate and so reflects the extent to which recent prediction errors (as opposed to older prediction errors) are weighted in updating associability values. This is different from stating associability weight is a measure of associability or that it reflects the extent to which associability is used to make decisions. This distinction is crucially important to understanding the results conceptually.

5) It seems that associability does not play a stronger role in subjects with PTSD. It also does not appear to be the case that PTSD subjects are systematically overestimating associability values. Rather, subjects with PTSD more heavily weight recent prediction errors (as opposed to older prediction errors) when estimating associability values; this may be due to a higher prior belief in the likelihood that prediction errors will change over time.

6) Simulations revealed that associability weight did not affect performance. Is higher associability weight adaptive, maladaptive, or neither?

7) Regarding neural data: Was the associability value that was used as a regressor the updated value for the current trial (i.e. incorporating prediction error on the current trial)? If so, it would reflect the unsigned prediction error on the current trial, especially if the associability weight is high. Is it possible that the neural results simply reflect a stronger response to unsigned prediction error, as opposed to signed prediction error, in PTSD? Even if the updated value was not used, it seems that the associability value should be correlated with unsigned predication error on current trial.

8) Was there a brain-behavior relationship independent of PTSD. It is also not clear whether adding PTSD symptoms to the brain-behavior relationship model improved model fit because the brain-behavior interaction was stronger in PTSD or whether the brain-behavior interaction was weaker in PTSD.

9) In the Introduction, the correspondence between the model and clinical constructs related to PTSD could be further clarified conceptually. Are unexpected events, reminders of negative events, and threats all being equated? Is associability the same as attention to threat?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Associability-modulated loss learning is increased in posttraumatic stress disorder" for further consideration at eLife. Your revised article has been favorably evaluated by a Senior Editor, Michael Frank as the Reviewing Editor, and two reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed. Given their specificity and brevity, I've decided to simply append the reviewers’ requests here:

Reviewer 1:

1) If the previous version was lacking certain details, this version gave me an impression that they might have overdone it. The authors might want to tighten the Materials and methods (for example, the MCMC part can be placed into supplementary materials).

2) In the response to the reviewers, the authors justified their modeling approach and pointed to previous literatures in terms of including a decay factor in their model. I'm curious whether removing this parameter would significantly changes the results reported in the paper since it seems irrelevant to the scientific question the authors were interested in.

3) In Figure 2B, the plotted associability value and prediction error seems to be inversely correlated (albeit these values were generated using a moving average method). But in their model, as the authors stated in their response to the reviewers, current associability was generated using PEs from previous trial. And if they indeed correlate with each other, then how did they look for the neural correlates of PE and associability values at the same time? Also, the y-axis in Figure 2B was labeled as "parameter value", which should be "variable value".

4) I'm confused with Figure 3D and 4B, are they both neural correlates of associability values? And the difference is 3D refers to the associability neural correlates independent of PTSD diagnosis but 4B does?

5) The model free logistic regression mentioned that "the outcome history for stimulus A would be (2+1)/5 = 0.6". I have a hard time understanding why it should be defined this way.

Reviewer 2:

6) My primary remaining concern is that I am still having difficulty understanding the three-way interaction between neural encoding of associability value, prior trial outcomes, and PTSD symptoms to predict switching behavior (subsection “Neural substrates of associative learning in PTSD and relationship to behavioral choices”, last paragraph). It is difficult for me to understand what it means that the interaction is "positive" in PTSD subjects and "negative" in non-PTSD subjects, and how to interpret this. Since a small loss was coded as 1 and a large loss as 0, does this mean that in PTSD, small losses were associated with a stronger relationship between neural activity and switching, while in non-PTSD, large losses were associated with a stronger relationship between neural activity and switching? If so, how do the authors interpret this? I do not find the figure showing chi-squared values (Figure 5B) illuminating on this point.
