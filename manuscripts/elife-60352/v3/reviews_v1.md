# Peer review - Round 1

Editors:
- Joseph Lehár, Boyce Thompson Institute for Plant Research United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.60352.sa1](https://doi.org/10.7554/eLife.60352.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript presents two statistical approaches to evaluating for drug effect measurements and associations between biomarkers, for dose curve data. Measurements of these kinds are made in many contexts, and frequently reported without accounting well for measurement uncertainties. A statistical framework of this kind will be widely useful and should be frequently applied.

Decision letter after peer review:

Thank you for submitting your article "A statistical framework for assessing pharmacological response and biomarkers using uncertainty estimates" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Detlef Weigel as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Alexander W Blocker (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

This manuscript presents two statistical approaches to evaluating for drug effect measurements and associations between biomarkers, for dose curve data. Measurements of these kinds are made in many contexts, and frequently reported without accounting well for measurement uncertainties. A statistical framework of this kind will be widely useful and should be frequently applied.

The reviewers noted some issues with in the manuscript, which should be addressed before final acceptance to eLife.

Essential revisions:

1) While this work presents a clear statistical framework, the Discussion and Abstract should explain more clearly how this framework improves drug potency or biomarker discovery efforts. That will help communicate the relevance of this work.

2) The authors should clarify of how measurement errors in the curves relate to fitted parameter uncertainties, to explain the superiority of particular fitting approaches.

3) A more thorough discussion of fitting performance is recommended. In particular, accounting for how fitting parameter selection and degrees of freedom. It would also be helpful to explore robust estimators to assess the reliability of fitted parameters. A more thorough analysis is also recommended for edge cases where the IC50 falls outside the measured range.

4) Additional model checking and comparisons would be useful. For example, Comparing the presented models to a more standard sigmoid, and additional comparisons highlighted in the comments. It would also help to clarify the relationship between Bayesian posterior probabilities, and ANOVA q-values for the GP approach.

5) The authors should revise Figure 3C and D. Grouping response curves by mechanism can be misleading since different drugs or biomarkers may intrinsically have discordant potencies due to differing on-target binding efficiency or off-target effects.
