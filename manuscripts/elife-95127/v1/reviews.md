# Peer review - Round 1

Editors:
- Georg B Keller, Friedrich Miescher Institute Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.95127.4.sa0](https://doi.org/10.7554/eLife.95127.4.sa0)

This important study introduces a new cortical circuit model for predictive processing. Simulations effectively illustrate that, with appropriate synaptic plasticity, a canonical layer 2/3 cortical circuit - comprising two classes of interneurons providing subtractive and divisive inhibition - can generate uncertainty-modulated prediction errors by pyramidal neurons. The model is compelling; although it relies on many assumptions and has not yet been compared directly to data, the model does align with empirical observations and yields a range of testable predictions. The study is expected to be of great interest to those involved in cortical and predictive processing research.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.95127.4.sa1](https://doi.org/10.7554/eLife.95127.4.sa1)

Summary:

This computational modeling study addresses the observation that variable observations are interpreted differently depending on how much uncertainty an agent expects from its environment. That is, the same mismatch between a stimulus and an expected stimulus would be less significant, and specifically would represent a smaller prediction error, in an environment with a high degree of variability than in one where observations have historically been similar to each other. The authors show that if two different classes of inhibitory interneurons, the PV and SST cells, (1) encode different aspects of a stimulus distribution and (2) act in different (divisive vs. subtractive) ways, and if (3) synaptic weights evolve in a way that causes the impact of certain inputs to balance the firing rates of the targets of those inputs, then pyramidal neurons in layer 2/3 of canonical cortical circuits can indeed encode uncertainty-modulated prediction errors. To achieve this result, SST neurons learn to represent the mean of a stimulus distribution and PV neurons its variance.

The impact of uncertainty on prediction errors in an understudied topic, and this study provides an intriguing and elegant new framework for how this impact could be achieved and what effects it could produce. The ideas here differ from past proposals about how neuronal firing represents uncertainty. The developed theory is accompanied by several predictions for future experimental testing, including the existence of different forms of coding by different subclasses of PV interneurons, which target different sets of SST interneurons (as well as pyramidal cells). The authors are able to point to some experimental observations that are at least consistent with their computational results. The simulations shown demonstrate that if we accept its assumptions, then the authors' theory works very well: SSTs learn to represent the mean of a stimulus distribution, PVs learn to estimate its variance, firing rates of other model neurons scale as they should, and the level of uncertainty automatically tunes the learning rate, so that variable observations are less impactful in a high uncertainty setting.

Strengths:

The ideas in this work are novel and elegant, and they are instantiated in a progression of simulations that demonstrate the behavior of the circuit. The framework used by the authors is biologically plausible and matches some known biological data. The results attained, as well as the assumptions that go into the theory, provide several predictions for future experimental testing. The authors have taken into account earlier review comments to revise their paper in ways that enhance its clarity.

Weaknesses:

One weakness could be that the proposed theory does rely on a fairly large number of assumptions. However, there is at least some biological support for these. Importantly, the authors do lay out and discuss their key assumptions in the Discussion section, so readers can assess their validity and implications for themselves.

Comments on revisions:

I have no further suggestions for the authors.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.95127.4.sa2](https://doi.org/10.7554/eLife.95127.4.sa2)

Summary:

Wilmes and colleagues develop a model for the computation of uncertainty modulated prediction errors based on an experimentally inspired cortical circuit model for predictive processing. Predictive processing is a promising theory of cortical function. An essential aspect of the model is the idea of precision weighting of prediction errors. There is ample experimental evidence for prediction error responses in cortex. However, a central prediction of the theory is that these prediction error responses are regulated by the uncertainty of the input. Testing this idea experimentally has been difficult due to a lack of concrete models. This work provides one such model and makes experimentally testable predictions.

Strengths:

The model proposed is novel and well-implemented. It has sufficient biological accuracy to make useful and testable predictions.

Weaknesses:

One key idea the model hinges on is that stimulus uncertainty is encoded in the firing rate of parvalbumin positive interneurons. While this assumption is rather speculative, the model also here makes experimentally testable predictions.

Comments on revisions:

Congratulations on a very nice paper.
