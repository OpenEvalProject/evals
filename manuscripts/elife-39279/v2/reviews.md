# Peer review - Round 1

Editors:
- Upinder Singh Bhalla, Tata Institute of Fundamental Research India

Reviewers:
- David Zwicker, Germany

## Review text

DOI: [10.7554/eLife.39279.024](https://doi.org/10.7554/eLife.39279.024)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Adaptation of olfactory receptor abundances for efficient coding" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: David Zwicker (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this manuscript Tesileanu and colleagues present a theoretical analysis of optimal coding in olfactory systems. They derive analytical results and use simulations to ask how receptor distributions depend on the number of neurons, the tuning width of receptors, and environment, with a core assumption of efficient coding. The study leads to the interesting prediction of strikingly changed receptor distribution following olfactory experience.

Essential revisions:

The current paper lays out a good framework but would be much stronger if some essential ramifications of the core idea were to be addressed.

1) The model must make predictions that can be falsified by experimental or evolutionary data.

2) The authors should incorporate more biological activation functions and receptor sensitivity distributions and examine how these affect the conclusions of the model.

3) The authors should comment on the diversity of olfactory systems across evolution and note how their model does or does not account for this diversity.

4) The authors should address the question of what happens when the number of receptors changes (as opposed to the number of neurons), as this is one of the main variables that seems to differ across evolution.

Reviewer #1:

This study builds its analysis on the idea that olfactory coding lies in a regime where sensor responses are correlated, hence efficient coding leads to divergent receptor abundance.

In addition to the assumption of efficient coding, the manuscript also assumes that olfactory receptor populations adapt to achieve such coding, within the time-frame of receptor turnover. This assumption leads to the interesting prediction of strikingly changed receptor distribution following olfactory experience, a phenomenon that has been observed experimentally.

I find the analysis interesting and potentially insightful, but it misses out on a few key biological points, that I feel really should be taken on board if the analysis is to be biologically relevant. I'll enumerate three of these, in increasing order of concern.

1) The authors explicitly ignore temporal correlations in olfactory cues, with a brief line in the introduction to their model that states that spike timing could be incorporated into the model. I do not see how this will work for respiratory phase tuning of odor responses, and would be interested to see what the authors had in mind for this.

2) The authors choose an operating point where they can apply a linear model for glomerular responses. In the animal, the operating range of different receptors for different odors is rather diverse, with the half-max varying substantially and the slope also varies. Thus a subset of odors will be saturating for some receptors, but linear or even subthreshold for other receptors. I suspect that this will affect the analysis of the responses.

My view is that any coding theory has to account for the very wide range of odor concentrations encountered in nature. One could possibly add this to the analysis reported in Equations 4 to 6, by summing the mutual information over a set of odor ranges, in which different but overlapping subsets of receptors are involved. I would be interested to see if this alters the conclusions.

3) A major point of concern with the whole analysis is of salience. The obvious outlier here is pheromones. Enormous resources are allocated to pheromone detection, and clearly this doesn't seem to fall within the framework presented in the paper. Even with the general olfactory system, the assumption of efficient coding needs to be further mapped to the distribution of odor salience, that is, relevance for animal survival. There seems to be a subtle nod to this point in the third-last paragraph of the Discussion, where 'value of detecting different odorants' is mentioned. I feel that the point is central enough that it needs to be fully addressed.

The constraint is not just to efficiently code the environment, it is to efficiently code those aspects of the environment which matter for survival. This seems to give rise to a fundamental challenge to this model, as follows: Assume a rare predator with a characteristic odor. Even if the predator is absent from the odor scene for long periods, it would be fatal to the prey species to underexpress receptors sensitive to the predator. One can come up with numerous other examples on these lines where selection pressures necessitate receptor expression for reasons other than efficient coding. There may be a couple of ways to go about incorporating this into the model: an evolutionarily determined 'prior' that weights salience of receptors, or a more general rule that tries to ensure a certain degree of broad coverage even at the expense of efficient coding. I suspect both may be relevant.

In summary, I think that the current paper lays out a good framework but would be much stronger if some essential ramifications of the core idea were to be addressed.

Reviewer #2:

In this manuscript Tesileanu and colleagues present a theoretical analysis of optimal coding in olfactory systems. The goal is to find the distribution of olfactory receptor abundances that maximizes the information an olfactory system can gain about odors in its environment, and to predict how receptor abundances should change when the environment changes. Given a set of assumptions about how odors are encoded by a population of receptors, they derive an expression for the mutual information between the response of a receptor population and a vector of environmental odors. They then evaluate this expression and show that the information depends on an overlap matrix, related to the covariance of the environmental odor vector. Based on these analytical results, they use simulations to ask how receptor distributions depend on the number of neurons, and the tuning width of receptors. They then ask how receptor abundances should change when the environment changes. They report a number of findings: (1) Receptor abundances are more sensitive to environmental perturbations when the number of neurons is small or intermediate, (2) Receptor abundances are more sensitive to environmental perturbations when they are narrowly tuned, (3) changes in optimal receptor abundances cannot be simply predicted from changes in odor abundances or variances.

At an abstract level, olfactory systems can be thought of as arrays of receptors, which have evolved from distinct receptor families many times over the course of evolution. Olfactory receptor genes are among the largest and most rapidly evolving gene families. Therefore I highly support the goals of this study to provide a theoretical understanding of how receptor arrays should change in response to changes in odor environment. In general, the level of abstraction adopted in this study is appropriate, and some of the findings are interesting. However, I have a number of questions about the analyses performed and conclusions reached, particularly concerning how the results might be related to biologically testable phenomena.

1) The conclusions concerning how receptor abundances should change following a change in environment are disappointing. While their model recapitulates Ibarra-Soira's result which predicts that the distribution of high abundance receptors is likely to remain unchanged, they do not provide any concrete predictions on the receptors which change their abundance in either direction of change or magnitude. As currently stated, the central predictions of the model – that optimal receptor abundances can increase or decrease or stay the same following a change in environment – seems to be unfalsifiable.

The manuscript could be strengthened by making more concrete predictions about how receptor abundances should change, at least in particular regimes. For example, the authors note that for intermediate numbers of neurons, optimal receptor distributions are anti-correlated with the inverse of the overlap matrix Q-1. They expand on this to say that receptors with high Q-1 can be uninformative because they do not fluctuate or because they provide redundant information. Although I did not fully follow the arguments here, it seemed like this was saying that abundance is inversely related to information, and there are two ways to be uninformative, one by having low variance, and two by being highly correlated with other receptors. Could this be used to make more concrete predictions about predicted changes in receptor abundance, at least for a given number of neurons? In addition, the authors also provide model evidence for predicting the magnitude of the change based on the change in olfactory environment, but it is unclear the characteristics which group types of changes together.

2) Some of the conclusions seem odd when considered in the context of olfactory evolution. For example, the authors conclude that if the number of neurons is large, then the optimal receptor distribution is approximately uniform. Olfactory systems differ greatly in magnitude across organisms. In particular, two of the most-studied models, fly and mouse, differ by an order of magnitude in the number of receptors (~60 for fly, ~1000 for mouse), as well as the total number of neurons. The finding that total neuron number determines receptor distribution should be tied numerically to the olfactory systems of flies and mice, if not also for other organisms. It is unclear, for example, whether the olfactory receptor number of mice is considered large, or whether it would fall in the intermediate signal to noise regime. Does the model predict that mouse receptor distributions are uniform while fly distributions are highly skewed? Why then is any adaptation observed in mouse receptor abundances as has been observed experimentally?

Given the results presented here one might imagine that the optimal strategy would be to make a very large number of broadly tuned receptors. Instead, what we observe across evolution are olfactory systems of various sizes, with various widths of odor tuning, all constantly evolving. The number of receptors in particular seems to be under strong evolutionary pressure, with new gene families expanding (as in ant ORs) or collapsing (as in humans). This discrepancy, or the other constraints that might lead to the biological situation, should be commented on.

The authors state that receptor abundances do not change in insects and therefore focus on a mammalian example to test their hypothesis. However, insect olfactory systems evolve quite rapidly between closely related species, and there is a large literature on this, especially from the Hansson group (e.g. Dekker…Hansson, 2006). Can these studies be used to test any of the hypotheses here? Or can the authors propose comparative studies that would test their hypotheses?

3) Several concepts used in the text are a bit unclear, at least to a biological reader:

Could the authors provide some intuition for what is meant (biologically) by the inverse of the overlap matrix?

Could the authors please unpack the following sentence:

The quantity KQ thus behaves as a signal-to-noise ratio (SNR), so that Equation 4 is essentially a generalization to multiple, correlated channels of the standard result for a single Gaussian channel, I = 1 log(1 + SNR2).

Could the authors please clarify in the discussion of Equation 7 whether Ktot represents the total number of neurons, the number of receptors, or the number of receptor types? Is the total number of neurons the most sensible thing to vary or would it be interesting to look at olfactory systems with different numbers of receptor types? This seems related to the question of where noise arises in the system, and what other constraints, besides information as quantified here, an animal might have on the design of its olfactory system.

4) The investigation of how optimal coding changes with broad versus narrow tuned receptors was interesting. However, real receptor arrays, at least as seen in the Hallem data, contain a mix of broadly and narrowly-tuned receptors, and receptor tuning width depends on odor intensity, with many receptor showing narrowly tuned response at low concentrations and wider tuning at high concentrations. Could the authors explore what happens in this regime, and provide any explanation for why animals might have both broad and narrowly tuned receptors? This finding could be further explored by making predictions for olfactory systems with receptors of mixed tuning widths, as is generally accepted to be the case in most organisms. This would provide a more concrete prediction for future experiments.

5) The authors claim that their model is robust to non-linearities and as well as their choice to represent the olfactory environment as a vector of concentrations. These ideas should be tested and demonstrated within the paper. For example, the nonlinearities involved in receptor encoding are well known: receptor responses can be expressed as a Hill function of odor concentration:

r = (c^n)/(c^n+Kd)

In many olfactory systems n=1, further simplifying this equation. The authors should explicitly show that the model generalizes when this nonlinearity is included. In addition, the main sources of noise in receptor encoding are likely to be (1) difference in receptor abundance across neurons that express the same receptor, (2) stochasticity in receptor binding and activation. The authors might consider incorporating these sources noise and showing that the model extends in this case.

The first section of the Results is difficult to read because it contained a number of statements justifying elements of the model and claiming that these do not affect the conclusions. This section would be easier to read if these points were saved for later in the manuscript where they could be explicitly demonstrated.

6) The section on dynamical optimization at the end seemed least well-constrained by data, and also (as noted) somewhat preliminary. The authors might consider reserving this material for a future manuscript that explores dynamics and tests them more thoroughly, and instead using this space to show that the model still holds when certain assumptions in the first version of the model are relaxed.

7) The authors should consider including graphical representations, similar to those provided in Figure 1, for concepts such as the mutual information measure, the covariance matrix, the overlap matrix, and the inverse overlap matrix. This would help provide insight for readers with less mathematical background, who may nonetheless be interested in the predictions of the models.

Reviewer #3:

The paper investigates theoretically how changing copy numbers of olfactory sensory neurons affects the coding properties of the olfactory system. The authors introduce a simple model based on the maximization of mutual information, which they analyze analytically and numerically using both artificial and measured values for the receptor sensitivities. Their analysis reveals a complex dependence of the optimal copy numbers of expressed receptors on the correlation structure of the receptor sensitivities and the odor environment. Since qualitatively similar dependencies have been observed in experiments, the model is very valuable for understanding the dynamics of copy number adaptation in the olfactory system. More generally, the presented model of the olfactory system is helpful for discussing how sensory systems adapt to changes in the environment and whether the aim for efficient coding is the driving mechanism.

The manuscript is well written and the arguments are clearly presented for the most part. My main concerns with the manuscript are that some limitations are not spelled out explicitly and that the theoretical analysis could have been more comprehensive. In particular, the authors do not investigate how their model would fair in the realistic case where odors are sparse and they do not discuss how the results depend on the number of different receptor types and the number of different odor molecules. The latter might be important to assess how relevant the results would be for realistic situations, since the current analysis is necessarily restricted to smaller numbers for the lack of adequate experimental data.

Taken together, I believe that the manuscript provides a substantial advance of our understanding of the olfactory system and of the adaptation of sensory systems to changing environments in general. I can therefore recommend publication of the manuscript in eLife once my comments have been taken into account.
