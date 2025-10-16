# Peer review - Round 1

Editors:
- Thomas Serre, Brown University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.53445.sa1](https://doi.org/10.7554/eLife.53445.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript provides a novel take on modeling cortical responses using general, nonlinear neural network models while maintaining a high and desirable level of interpretability. The quantitative results demonstrate the success of the method, in comparison to more classic approaches, and the subsequent analysis provides an accessible and insightful interpretation of the “strategies” used by the neural network models to achieve this improved performance.

Decision letter after peer review:

Thank you for submitting your article "Estimating and interpreting nonlinear receptive fields of sensory responses with deep neural network models" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Bernhard Englitz (Reviewer #1); Nicholas A Lesica (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The reviewers found that the manuscript provides a novel take on modeling cortical responses using general, nonlinear models while maintaining a high and desirable level of interpretability. In particular, the study demonstrates the potential of deep networks for the analysis of intracranial recordings from the human auditory cortex during the presentation of speech. The approach involves fitting deep networks and then analyzing linear equivalents of the fits to provide insights into nonlinear sensory processing. The reported quantitative results demonstrate the potential of the method, in comparison to simpler / classic models such as STRFs, and the subsequent analysis provides an accessible and insightful interpretation of the computational strategies used by the deep network models to achieve this improved performance.

As a general comment, the reviewers (and the reviewing editor) would like to encourage the authors to make software for their model publicly available.

Essential revisions:

The reviewers raised a number of concerns that must be adequately addressed before the paper can be accepted. Some of the required revisions will likely require further experimentation within the framework of the presented studies and techniques.

– Response evaluation with noise-adjusted correlation: The authors account for the possibility of noise in the responses by computing the noise-adjusted correlation, detailed in the Materials and methods. It was not clear to the reviewers where this method was referenced from since they could not find it mentioned in Dean, Harper and McApline, 2005 (though they could have easily missed it). The description in the Materials and methods is mathematically clear, but does not clarify the properties of this measure, e.g. under which circumstances would a 1 value be achieved? Please comment.

While this adjustment does something potentially related, one reviewer's suggestion is to use instead, the principled approach of predictive power (Sahani and Linden 2003, NeurIPS), which gives a good sense of absolute performance in the context of noise. Otherwise, the authors should explain/introduce the noise-adjusted correlation more fully.

– As presented, there is uncertainty about how much of what is being fitted is actually truly reflective of sensory processing vs. variability in the (linearized) fits due to the limited amount of data used for training. Since these networks are universal function approximators, they could in principle capture 100% of the explainable variance in the data if they are given enough training samples. In that perfectly predictive regime, we could be very confident that differences between fits reflect true differences in sensory processing. But if we are not in this regime, then we cannot know what fraction of the differences between fits is “real” without further investigation. The authors describe something along these lines in the section “Linearized function robustness”. But this only assesses robustness against different initial conditions for the fits, not the number of training samples. A more detailed evaluation of the robustness of the estimates as a function of the amount of available training data would help address this concern. Specifically, the reviewers would like to see some type of analysis that assesses the degree to which adding more data would increase performance and/or change the fits. Perhaps something along the lines of bootstrap resampling to at least put confidence intervals on a statistic would help.

– On a related note: since performance is measured as explainable variance (rather than just variance) the implicit goal is to capture only the stimulus-driven portion of the response. But the training is performed on single-trial data. With enough training samples the models will learn to ignore non-stimulus driven fluctuations even if they are trained on single-trial data, but how do we know that we have enough training samples to be in this regime? If we are not, then isn't there a worry that the fluctuations the time-point-by-time-point linearized fits reflect attempts to capture non-stimulus driven variance? In short, it is critical to quantify how much the (differences between) (linearized) fits would be expected to change if more training samples were used. Ideally, they wouldn't change at all. But given the reality of limited experimental data, we need a principled approach to derive confidence intervals just as we would for any other statistics, especially if this general approach is to be used meaningfully by non-experts.

– Comparison with more advanced neural models: While the currently presented method has the clear advantage of time-to-time interpretability of the kernel, the reviewers were not fully convinced that the absolute level of predictability was necessarily best-in-class (which is also not claimed in the text, but it is hard to assess where it falls within the set of existing models). It would thus be important to compare the DNN fit against two more general models, i.e. an STRF with a static nonlinearity and a model including adaptation (e.g., as proposed by Stephen David at OHSU). In particular, relating the extracted three properties to the adaptation parameter of the latter model could provide some unification between modeling approaches.

– Temporal hold: The identification of the temporal hold property was seen as one of the most exciting results from the manuscript. Hence, the reviewers request that it be analyzed more thoroughly. The criterion for the lag duration was just given as “significantly correlated”, without specification of a test, p-threshold, or a correction for multiple testing. In particular, it is not clear what happens if it drops briefly below the threshold but is significantly correlated afterward (e.g. oscillations?). Given the novelty of this result, it would be important to devote more detailed analysis to these questions (e.g., using permutation tests a la Koenig and Melie-Garcia, Brain Topography (2010), which is fast to implement and includes the corresponding options.)

– Method limitation: If one wants to measure the degree of nonlinearity in a given brain area, isn't it sufficient to simply look at how much of the explainable variance is or is not captured by a linear model? What else is learned by looking at the performance of a particular nonlinear model in this context? In fact, it would seem that using the linear model alone would be the only way to make a general statement in this context. Just because one particular nonlinear model fits one area better than another (or improves predictions in one area more than another) doesn't necessarily show that one or the other area is, in general, more nonlinear. It only suggests the nonlinearity in one area is more readily fit by that particular network given limited training samples. Please comment.

– Statistical testing: The statistical testing performed needs to be detailed more to include effect sizes.
