# Peer review - Round 1

Editors:
- Agnese Seminara, Université Côte d'Azur France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.57524.sa1](https://doi.org/10.7554/eLife.57524.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

In this manuscript, the authors present the first dataset that simultaneously monitors behavior and odor in real time for freely walking flies navigating toward an intermittent odor. Flies were visualised as they navigated toward the source of a turbulent plume of smoke, that the flies were naturally attracted to. A quantitative statistical analysis of behavior in relation to odor unveiled novel algorithms underlying navigation toward intermittent odor cues.

These results pave the way for further research on the neural and computational basis of olfactory navigation strategies in the fly and introduce an attractive odor that can be imaged simultaneously with behavior, with impact for a broad swathe of the scientific community.

Decision letter after peer review:

Thank you for submitting your article "Walking Drosophila navigate complex plumes using stochastic decisions biased by the timing of odor encounters" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Ronald Calabrese as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Venkatesh N Murthy (Reviewer #2); Antonio Celani (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

In this manuscript, the authors present the first dataset that simultaneously monitors behavior and odor in real time for freely walking flies navigating toward an intermittent odor. Flies were visualised as they navigated toward the source of a turbulent plume of smoke, that the flies were naturally attracted to. Intermittency was quantified by visualisation of the smoke in real time while following the animals. A quantitative statistical analysis of behavior in relation to odor unveiled novel algorithms underlying navigation toward intermittent odor cues. Turning and stopping was a semi-random process whereas anemotactic responses depended on odor encounter. The authors tested mutants to ensure that behavior was driven by olfaction.

These results pave the way for further research on the neural and the computational basis of olfactory navigation strategies in the fly and introduce an attractive odor that can be imaged simultaneously with behavior, with impact for a broad swathe of the scientific community.

Essential revisions:

A) Because smoke is a complex signal, the behavior it elicits may be caused by a combination of effects caused by the single compounds contained in the plume, including potential repellents (e.g. CO and toluene are toxic at high concentration). Hence aspects of this behavior may be odor-dependent, and not be generally applicable to other odors. The authors should make this caveat clear to the audience, and we expect this will stimulate further work.

B) The distribution for the simulated fly (Figure 7C) is quite different from the one of true flies. One notable feature is that the simulated agent's distribution is less "peaky" along the y axis (compare with Figure 1K). True flies, it would seem, remain closer to the central axis than simulated ones. Perhaps a couple of slight changes in the model could influence/improve the fit:

• From Figure 4D, it seems like turn angle distribution could be tetra-modal, with an encounter independent part centered on 50 and an encounter-dependent part centered on 25. Could a model with this added level of granularity improve the fits to behavior? It would make odor driven changes in direction sharper and potentially improve tracking.

• The generating function for P(upwind|turn) is not very satisfactory. It is a linear fit offset by 0.5 and truncated at 1. Why did the authors not use a standard choice model with a bias term and inverse temperature controlling the slope? This could potentially handle better the extreme of the encounter frequency axis which are those that have the worst fit with the current model (Figure 4G).

C) We expect the combined behavior-odor dataset to prove extremely valuable for further research, is it possible to make it publicly available?
