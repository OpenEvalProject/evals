# Peer review - Round 1

Editors:
- Jennifer L Raymond, Stanford University School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55217.sa1](https://doi.org/10.7554/eLife.55217.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Using a series of behavioral experiments and modeling analyses, the authors suggest that cerebellum-dependent motor skill learning is supported by separable "fast" and "slow" learning processes. The manuscript systematically and tightly integrates four functional principles governing this process, consistent with previous experimental evidence and models of the cerebellar anatomy and physiology. Incisive behavioral studies like this one, which provide clear insights/constraints on neural mechanisms, have become all too rare.

Decision letter after peer review:

Thank you for submitting your article "Principles of operation of a learning neural circuit" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Joshua Gold as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Samuel McDougle (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this paper, Herzfeld and colleagues take a computational and psychophysical approach to investigate mechanisms of smooth-pursuit learning behavior in monkeys. Using a series of behavioral experiments and modeling analyses, the authors suggest that learned responses appear to be modulated by the learning environment in a manner that reflects two underlying, separable "fast" and "slow" learning processes, and transfer from the "fast" to the "slow" system. First, the authors show that the relationship between the adaptive response and the size of the experienced error is modulated by the consistency of the environment; that is, the scaling function saturates when the error changes magnitude every trial, but becomes linear if particular errors are experienced repeatedly. These effects are best captured by their dual-process model rather than a single process with a fixed learning algorithm. Next, in a series of speed-based generalization experiments, the authors show that a) generalization functions appear to change with training, suggesting a shift in the relevant inputs to the learning circuit, and b) there are differential changes in generalization patterns over time based on the particular speed of the training stimuli. Finally, the authors formalize their theory in a cerebellum-inspired circuit model of pursuit learning to generate precise predictions about expected neurophysiological instantiations of their behavioral observations.

The manuscript contains a very impressive set of careful, well-designed experiments, and a thought-provoking modeling analysis. The main question is compelling and the reviewers were, for the most part, convinced that the conclusions were largely supported by the data. However, the reviewers identified several points that should be addressed more carefully. Moreover, in its current form, the reviewers found the manuscript difficult to read, even for researchers with considerable relevant modeling and experimental experience. As currently written, it has several logical leaps, making it difficult to follow. It would benefit from restructuring to better guide the reader through the results and justify the modeling.

Essential revisions:

1) The manuscript should be thoroughly edited to improve clarity of the manuscript. As currently written, it has several logical leaps and is quite difficult to follow. The difficulty may arise in part from switching between model and experiment, and an uncertainty about where the results are going. At various points new bells and whistles are added to the model, and it is not always clear why these particular parameterizations are used. Two suggestions for reorganization, which could help with the clarity of the narrative:

– Present the circuit model at the beginning, and then proceed to constrain and test the model. This may be the better option, because dual-site plasticity is already an existing hypothesis for cerebellar function.

or

– Present all the experimental data first, and then build the model.

Additional, more detailed comments about where clarity could be improved are provided below.

2) An expanded, formal model comparison would better in the main text versus the Materials and methods section.

a) Provide a more clear explanation of why an independent fast and slow system can't work.

b) The "dual-process" claim would be strengthened by testing alternative models beyond just the single process model and the non-interaction dual-process model. Is a dual-process model more parsimonious than alternatives that, say, posit a single process with dynamic learning rates (or retention factors) that change systematically over time, as a function of environmental consistency (Castro et al., 2014), or both? Indeed, such models are commonplace in other domains, like reinforcement learning (Iigaya et al., 2018; Behrens et al., 2007; Nassar et al., 2010). Alternative dynamic models (e.g., Kalman filter) might perform significantly worse than the author's dual-process model in explaining the data, but this is an empirical question.

3) Additional explanation is needed regarding the generalization. The learning model does not appear to explain the observed generalization effects (20 vs. 5 deg/s differences, and the gradual shift from linear to gaussian). Although this is addressed in the circuit model's predictions, it would be useful to find a way to validate either the descriptive or circuit model via simulations of the generalization behavior. In addition, the presentation should be improved to more clearly guide the reader through the logic of this section.

a) The first main model conclusion, which is that a slow learning system is required to explain the change in speed generalization to a linear relationship, is not explained well. Intuition is not provided for why the slow system produces a linear relationship when taught by the fast system which does not. When this modification to the model is introduced, multiple features are added (a second system, and feedback control of the error signal), and it isn't clear which of these, or both, are necessary to obtain linearity. Starting in the subsection “Strategy for testing the conceptual model of motor learning”, the authors explain the strategy saying "inputs", which are not illustrated in their conceptual model (Figure 5A). Readers, especially those who are not familiar with the cerebellar circuit, are left to wonder, because this strategy needs imagination based on a real circuit which has an eye velocity related-firing of input, plasticity site, input and plasticity-dependent output for expression of learned behavior. Readers may understand at last when they see Figure 10A, which is the cerebellar learning circuit.

b) The description of the inference of input tuning when describing learning generalization is a bit obtuse. "The changing shape of the generalization function was further accentuated in Monkey RE after 2000 trials when probe trials expressed less behavioral learning (learning expression ratio <1.0) when the pursuit speed was faster in the probe than in the learning trial, suggesting Gaussian generalization." "Gaussian generalization" not defined anywhere. It should be, and the particular form used should be motivated. I assume what the authors mean is that it supports some kind of unimodal tuning of the input. Why can't the form be directly inferred from data, rather than assumed to be Gaussian? In general, the fitting to Equation 6 seems rather arbitrary.

c) Regarding the generalization of learning to different probe speeds: There should be more discussion of this result from an algorithmic perspective and possible/alternative explanations. Can the results be explained by "confidence" about the speed during the learning trial and its relationship to the probe speed that increases over learning and, at the end of learning, results in the learning expression only generalizing to the same speed ("Gaussian" generalization)? Such a discussion could make more intuitive what is otherwise a difficult and technical section that leads to strange conclusion about the model (see next comment).

d) One of the hardest to swallow aspects of the model is the necessity of extremely different speed tuning of the inputs to the fast and slow systems. It is especially hard to swallow because these inputs both ultimately arise presumably from mossy fibers that contact nuclear cells directly or contact granule cells. In such a model, it would seem that either different mossy fibers for each system would be required, or some complicated transformation would need to happen at the granule cell. The authors should expand their discussion of how this might come about, and discuss whether there are other ways that the results might be explained without this strong assumption.

4) Results should be discussed in the context of previous work from other learning and memory systems. This paper highlighted four principles that explain learning of smooth eye responses that predict a change in target direction. Previous work on these principles in other learning and memory systems should be discussed.

5) Several figures show data only from one monkey. Please justify this.
