# Peer review - Round 1

Editors:
- Tobias H Donner, University Medical Center Hamburg-Eppendorf Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.33334.029](https://doi.org/10.7554/eLife.33334.029)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Post-decision biases reveal a self-consistency constraint in perceptual inference" for consideration by eLife. Your article has been favorably evaluated by Timothy Behrens (Senior Editor) and three reviewers, one of whom, Tobias H Donner (Reviewer #1), is a member of our Board of Reviewing Editors. The following individuals involved in review of your submission have agreed to reveal their identity: Mehrdad Jazayeri (Reviewer #2); Bruce G Cumming (Reviewer #3); Valentin Wyart (Reviewer #4).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Your paper reproduces influential previous findings on how combining a discrimination task with an estimation task produces systematic biases in estimation (Jazayeri and Movshon, 2007). The previous study had explained the estimation bias as the result of an optimal readout of sensory evidence for the discrimination task (henceforth referred to as 'readout model'). You provide a different explanation in terms of a self-consistent Bayesian observer. You perform two additional experiments (cueing the stimulus range, and providing the answer to a discrimination task), and show that the results follow the predictions of your model well.

All reviewers thought that your paper makes a compelling case that your self-consistent Bayesian observer provides an excellent account of all the data, including variation between individual observers. The reviewers also appreciated your discussion of the potential adaptive function of this self-consistency bias and its relation to 'cognitive dissonance' phenomena described in the social psychology literature.

One issue contentious among reviewers was whether the conceptual advance provided by your paper is sufficient to warrant publication in eLife. The reviewers converged on the conclusion that (with the revisions requested below) the paper would be borderline for eLife, but that the case could be made for it being above threshold. Another issue was whether or not it was necessary that you report a formal head-to-head comparison between your self-consistent observer and the readout model by Jazayeri and Movshon. The reviewers eventually agreed that it would be unreasonable to ask you for truly defensible head-to-head comparison. Doing so would require that you develop a complete algorithmic model, which would demand making many assumptions about how a prior is encoded and how it would interact with readout weights. It would also require you to make another set of assumptions about how factors such as prior knowledge ought to be included in the old readout model, which would weaken your argument and blur the distinction between the two models.

Essential revisions:

1) The paper is written in a way that makes it difficult for the reader to appreciate which part is replication and which part is truly novel. Please revise the Abstract and Introduction to clarify this, focusing on the following points.

The original observation of self-consistent behavior was made several decades ago. Jazayeri and Movshon reported this phenomenon in perception, and since then, several studies have replicated the finding (e.g., Szpiro et al., 2014; Zamboni et al., 2017). Stocker and Simoncelli developed and published the self-consistent observer model in NIPS in 2008. The current model is almost an exact replica of that previously published one. Experiment 1 is a replica of the original Jazayeri and Movshon experiment, with the exception of using orientation rather than motion direction. The main novel contribution of your present paper are the empirical tests (Experiments 2 and 3).

2) Please add a discussion of whether the original readout model (Jazayeri and Movshon, 2007) cannot account for your data. The reviewers felt that changes in the prior on orientation width (caused by cuing) might produce similar effects in their model, without having to invoke self-consistency; or that providing the observer with veridical information about the stimulus category might naturally change the percept in the traditional Bayesian way. The reviewers thought it would be important to make clear to what extent we now have two equally good explanations of the phenomenon. Specifically, the reviewers would like you to rework the paper to clarify the following three things in the Discussion:

- Explain that the two models are tackling the question at different levels. This would help the paper highlight an important conceptual point that the previous work failed to convey.

- Explain that Experiments 2 and 3 may not be decisive for arbitrating between the two models. Even without this, the two experiments highlight an important and complementary point that when other sources of information are available (prior information and/or other cues), these sources could influence the decoding strategy (in both models). This is particularly relevant because if one subsumes the effects of prior into the readout weights, then the difference in the two models become a matter of semantics and would diminish the intuitive interpretation that makes the paper appealing.

- Explain that to properly compare the two models, future research has to (1) develop an algorithmic version of their model, and (2) consider how prior information could be worked into the old readout model. This would allow the paper to inform the path forward for meaningful head-to-head comparisons. In this context, it would be useful to discuss what it means to suddenly abolish a portion of the posterior. This can be done conveniently in a model but how does it fit with what we know about how these computations are carried out by the brain?

3) Two recent studies investigated the same estimation bias and arrived at conclusions that are different from yours. Those should be addressed in more detail. Specifically:

- Zamboni et al. (2017) established an important role of the presence and orientation of the reference in inducing estimation biases. The reference can induce the bias even without any categorical choice. This seems to at odds with your claim that choices cause the estimation bias. You briefly touch on this study in Discussion, claiming that the current self-consistent observer model can account for this. Given that this issue is critical for your conclusion, you should fit your model to the Zamboni et al. data (which are available).

- Results from Szpiro et al. (2014) suggest that the phenomenon is learned through practice. This suggests that it cannot be straightforwardly attributed to a conditionalization. Additionally, in the same study, it was found that the bias manifests itself differently in the perceptual and motor domains. If we have to come up with a different model for each domain, then the exercise of using a Bayesian approach seem less revealing. It is disappointing that this study is not cited given that the empirical observations are directly against the proposed hypothesis.

4) A key component of your model is conditionalization of the posterior according to prior choice. You motivate this by noting that this allows subjects to be self-consistent. However, in most realistic conditions, the behavior would remain consistent even without this component – the conditionalization just moves the estimate away from the boundary, it does change sides. Since the model doesn't actually increase self-consistency, please describe more carefully what motivates it.

5) Please provide quantitative measures about the quality of fits. Your model fits look compelling, but the assessment is only qualitative at present.
