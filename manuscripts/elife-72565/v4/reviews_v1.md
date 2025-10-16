# Peer review - Round 1

Editors:
- Gordon J Berman, Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72565.sa0](https://doi.org/10.7554/eLife.72565.sa0)

In this manuscript, the authors describe a generative model-based framework to better analyze stochastic growth data, including bacterial cell growth. They show how this framework can be applied to gain insight into the processes underlying these phenomena. This work is well-supported by simulations and data analysis and will likely be of interest to those trying to understand the processes governing bacterial growth, as well as those studying stochastic growth processes in biology more broadly.


---

# Peer review - Round 1

Editors:
- Gordon J Berman, Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72565.sa1](https://doi.org/10.7554/eLife.72565.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "To bin or not to bin: analyzing single-cell growth data" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Aleksandra Walczak as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Benjamin P Bratton (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The final result (Figure 4) is somewhat disconnected from the majority of the paper that precedes it. Specifically, the authors' procedure that resolves exponential vs. non-exponential growth results in E. coli in alanine being deemed exponential (Figure 2B) only to later be revealed as non-exponential (Figure 4A), albeit weakly. Furthermore, the procedure advertised as distinguishing exponential from linear growth (Figure 3B), when applied to the data, reveals neither (Figure 4). This makes the main point of the paper (the demonstration and resolution of pitfalls) feel disconnected from its application to a particular case, which is more nuanced and likely leaves many questions unanswered.

2) The title ("To bin or not to bin…") implies that binning is the main culprit behind potentially misleading analyses, but one of the reviewers argued that in the end, it is linear regression. Each of the two main pitfalls and their resolution would be unchanged if the data were never binned. Binning affects the apparent curvature of the y vs x relationship, but this reads as a more minor point. Therefore, the title may be a bit misleading in service of its poeticism.

3) The authors look at different choices of binning dimensions but do not sufficiently explore the power of their generative model to perform (un)weighted regression or parameter estimation from the not-binned data. They do explore the unbinned data from an analytical statistics approach in sections 5.4.1 and 5.5 but this is not yet extensively explored in the figures and/or discussion.

4) This manuscript could be improved by including a discussion on binning single-cell length trajectories, those taken on a single cell within one division cycle, either based on the length or on time. Experimentally, my understanding is that most growth measurements are done on a fixed \Δ t basis, and therefore measurements are averaged using length as a function of time. Another option, one that I have not seen used, is to use a \Δ L basis and measure the time to grow either a specific amount or a specific fractional amount. Of course, these are different ways to slice the same cake, and such an extension may be useful to expand the authors' argument that one needs to utilize a generative model to be able to assess their choice in statistical analysis.

5) As the formulation of this approach borrows from and is built heavily on previous data and previous statistical frameworks, it would be helpful to have more discussion on what is new to this particular manuscript. This is always a difficult balance as one needs the context of the previous work to understand the symbology used, but just reiterating what is already in the literature can lead to a dilution of the new/novel/important discoveries of the manuscript.

6) The authors should resolve the use of the term "cell size" to mean both "cell length" and "cell volume" (line 107, line 431/432). The authors briefly touch on a related concept of length growth vs biomass growth in 343-357. As a first, naively simple model of cell growth, it is possible to come up with a simple model for linear vs volumetric growth by imagining that a cell grows exponentially in length from birth to death. In this simple model, at the appropriate time, it switches from growing a cylinder to growing hemispherically endcaps, as it needs to perfectly duplicate its shape. In this simple model, one can easily see that the instantaneous, relative volumetric and length growth rates are not identical; vary throughout the cell cycle; and even their average over the whole cell cycle is not 1. While the authors mention that the average diameter is quite robust between growth conditions, only in the limit that the cell is very long and not a spherocylinder does the approximation that shape does not matter come in to play. Granted, this naïve model does not incorporate the wealth of information known about division timing or geometric changes during growth, and underscores the authors' main point that a specific model of the dynamical process should be included.Reviewer #1:

In this manuscript, the authors describe a generative model-based framework to better analyze stochastic growth data, including bacterial cell growth. They show how this framework can be applied to gain insight into the processes underlying these phenomena. More specifically, they start by showing how binning along different axes in the

This work is well-supported by simulations and data analysis and will likely be of interest to those trying to understand the processes governing bacterial growth, as well as those studying stochastic growth processes in biology more broadly.

Strengths:

– The choice and execution of the simulations were sensible and well-done, respectively, and they provided clarity as to the overall message of the manuscript.

– The conclusions are well-supported by the data.

– I found the writing to be clear throughout.

Weaknesses:

– It would be good to have a more extensive discussion about what is specifically new here. This is not my particular field, so having a bit more of an introduction about methods beyond binning (if any) that have emerged to understand these data.Reviewer #2:

The manuscript by Kar et al., uses single-cell experiments, simulations, and theory to investigate a common method of determining whether cell size grows exponentially. Specifically, they show that a relationship that should adhere to y = x for exponential growth on average (where x is the product of the division time and mean growth rate, and y is the log of the ratio of the birth and division size), in fact deviates from y = x with noise, because x contains noise that y does not (growth rate noise). This makes exponential growth seem non-exponential. The resolution, they show, is to plot x vs. y instead. Additionally, they show that when plotting x vs. y for linear growth, the relationship is coincidentally very close to x = y. This makes linear growth seem exponential. The resolution, they show, is to plot the instantaneous growth rate vs. the normalized cell age, which will decrease for linear growth and will be constant for exponential growth. Applying this protocol to E. coli size data, they find that the growth rate actually increases weakly with age, indicating somewhat superexponential growth.

Strengths

The insights in this manuscript are highly important for the field to know. The fact that exponential growth can masquerade as non-exponential growth and vice versa means that much confusion likely exists in a field that is already surprisingly complex given how simple its questions are to state. The fact that the authors offer resolutions to these pitfalls means that this work should add clarity to the field and move it forward in a meaningful way.

The conclusions are well supported by the data. For example, in the case of seemingly non-exponential growth, the problem is presented by the experimental data, reproduced by the simulations, and explained by the theory, while the resolution is inspired by the theory, proven by the simulations, and demonstrated by the experimental data.

The manuscript is well written. While it is rooted in careful analysis, it remains understandable to a largely non-quantitative audience.

Weaknesses

The final result (Figure 4) is somewhat disconnected from the majority of the paper that precedes it. Specifically, the authors' procedure that resolves exponential vs. non-exponential growth results in E. coli in alanine being deemed exponential (Figure 2B) only to later be revealed as non-exponential (Figure 4A), albeit weakly. Furthermore, the procedure advertised as distinguishing exponential from linear growth (Figure 3B), when applied to the data, reveals neither (Figure 4). This makes the main point of the paper (the demonstration and resolution of pitfalls) feel disconnected from its application to a particular case, which is more nuanced and likely leaves many questions unanswered.

The title ("To bin or not to bin…") implies that binning is the main culprit behind potentially misleading analysis, but I would argue that in the end, it is linear regression. Each of the two main pitfalls and their resolution would be unchanged if the data were never binned, I believe. Binning affects the apparent curvature of the y vs x relationship, but this reads as a more minor point. Therefore, the title may be a bit misleading in service of its poeticism.Reviewer #3:

Kar et al., examine an interesting and important question of how to make sense of large sets of observational data, specifically cell length data, which may or may not be consistent with various underlying biological mechanisms. As datasets improve in their technical quality (increasing spatiotemporal resolution, increasing numbers of observations), there is hope that the community will be able to resolve differences between underlying cell biological mechanisms of cell size homeostasis. As the authors point out, these interpretations and analyses require statistical analysis that can accurately perform the model selection or parameter estimation task of interest.

1) The authors succeed in bringing attention to the issue of appropriate binning when analyzing large datasets. The authors focus their figures and discussion on an important, and practical issue, as many researchers perform linear regression on binned data. The title and framing of the manuscript imply that it will provide a comparison with statistical methods that do not involve binning. The authors look at different choices of binning dimensions, but do not sufficiently explore the power of their generative model to perform (un)weighted regression or parameter estimation from the not-binned data. They do explore the unbinned data from an analytical statistics approach in section 5.4.1 and 5.5 but this not yet extensively explored in the figures and/or discussion.

2) The authors succeed in walking the reader through the power of examining a specific mechanism/model and the statistical properties of that model. In this case, the authors do this with both a model of cell length homeostasis that comes from exponential growth or linear growth with homeostatic feedback. This approach rests heavily on previous work from the same group including a reframing of the statistical correlations between different observables that was explored in the included references [13] and [16]. This reframing is complemented by additional experiments and reanalysis of various published experimental datasets.
