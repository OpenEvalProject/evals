# Peer review - Round 1

Editors:
- Thorsten Kahnt, Northwestern University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.56938.sa1](https://doi.org/10.7554/eLife.56938.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Drift diffusion models are widely used in psychology and neuroscience research. However, diffusion model applications are often constraint by the available software rather than the scientific question that ought to be asked. Thus, having a model and associated software package that provides more flexible model fits will be of great value for the scientific community.

Decision letter after peer review:

Thank you for submitting your article "A flexible framework for simulating and fitting generalized drift-diffusion models" for consideration by eLife. Your article has been reviewed by Joshua Gold as the Senior Editor, a Reviewing Editor, and three reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Long Ding (Reviewer #1); Eric-Jan Wagenmakers (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus, the revisions requested below only address clarity and presentation.

Summary:

Reviewers were generally impressed with this work as it presents a substantial step forward, providing a much-needed, flexible, and efficient way to fit choice and reaction time data common to many decision behaviors. Reviewers mostly made a number of suggestions for how to improve the manuscript. However, they also identified two essential issues that would need to be adequately addressed in a revised version. Specifically, it would be important to apply the models to a different data set and to consider additional criteria for model evaluation.

Essential revisions:

1) As explained in reviewer #2's major comment 2, the RT distribution in the Roitman and Shadlen data set is not very representative. Reviewers agree that the authors should include an addition, more representative data set for the current paper. In particular, reviewers suggested the following data set: Wagenmakers et al., (2008). These data are available at http://www.ejwagenmakers.com/Code/2008/LexDecData.zip

2) As detailed in reviewer #2's major comment 3, and reviewer #3 major comment 3, given the flexibility of the model, it is unclear whether goodness-of-fit is the only or even the most appropriate criteria to evaluate different models.

Reviewer #1:

This work provides a much-needed, flexible, and efficient way to fit choice and reaction time data common to many decision behaviors.

The detailed methods in the section "Fokker-Plank formalism of the GDDM" are outside my expertise. But the superior performance of the GDDM compared to other packages, both in accuracy and execution time, is very convincing and rigorously demonstrated. The writing is also very clear. I expect that the software package will be widely used in the field. This is a rare instance when I support publication as is.

Reviewer #2:

In general I am truly impressed with this work. It present a substantial step forward, and I strongly believe a revision should be published. At the same time, I also believe the manuscript can be greatly strengthened along the lines provided below.

Essential revisions:

1) "Fifth, single trial parameter variability is supported within the GDDM framework for both starting point and non-decision time."

Initially, I was not sure what the authors mean with "single trial parameter variability". Do they mean "across-trial variability"? And if so, does their methodology not allow for across-trial variability in drift rate, as the full DDM does? If the GDDM indeed does not allow such variability, this warrants explicit mention and an extensive discussion.

Then when I read the Discussion section the cat comes out of the bag: "While the GDDM framework supports individual trial variability in non-decision time and starting position according to any arbitrary distribution, it does not support drift rate variability. As a result, the GDDM framework does not support the entire "full DDM"."

But this is a severe limitation, one that needs to be acknowledged and emphasized from the start. Variability in drift rate is a highly plausible mechanism that has been an integral part of the DDM since 1978. Without this mechanism to account for (fairly ubiquitous) slow errors, the model will have to turn to other mechanism to accomplish this, such as moving-in bounds. The authors mention "However, the GDDM framework is broad enough to support an infinite number of extensions which create the same RT features which originally motivated inclusion of drift rate variability." But the goal of the modeling is not to fit the data well; the actual goal is to decompose the observed data into meaningful psychological processes, and a process of moving-in bounds is fundamentally different from drift-rate variability. I assume that the drift rate variability frustrates the mathematical work? The reader needs to know the reason why the model cannot handle drift rate variability.

Staying on the same point, the authors then point out that "Indeed, in Figure 2, our 5-parameter GDDM provided a better fit to the asymmetry between correct and error RT distributions than the 11-parameter "full DDM"." True, but since these data are highly unrepresentative (see the next point below), this can just as well be used as an argument *against* the GDDM: apparently it is able to fit just about any pattern of data, even patterns that are highly unrepresentative.

2) The demonstration where the models are fit to the data is (deeply) problematic, because the monkey data are simply not representative. As can be seen from the grey histograms in Figure 2, the "regular" DDMs predict a long-tailed RT distribution, which is however not apparent from the data. This then creates ambiguity: yes, one can show that the existing models do not fit well, but they are fit to unrepresentative data. If these data patterns were regularly observed, the DDM would never have been proposed in the first place. It would be much more compelling to fit the models to any of the large benchmark data sets that are publicly available – these data sets all show a pronounced right skew.

3) As the progenitor of the much-maligned "EZ" model, I guess I am obliged to protest a little. Yes, of course EZ is not flexible, and does not have all the bells and whistles. But that is kind of the point of a simple model. There are some demonstrations that (contrary to my own expectations even) EZ actually does better than the full diffusion model when applied to sparse data. I am not talking about goodness-of-fit, but about recovering the ground truth in a simulation study (e.g., figuring out which parameters are the same and which differ). For sparse data, a simple model may work better. One reference:

van Ravenzwaaij, Donkin and Vandekerckhove, (2017).

Reviewer #3:

The manuscript introduces a generalized drift-diffusion model, together with the modular software package PyDDM to fit it. The generalized drift-diffusion model is a set of accumulation-to-bound models that feature highly flexible components, such as time- and location-varying drifts, variable starting points, time-varying decision boundaries, etc. The manuscript describes how to compute first-passage time distributions for this set of models by numerically and efficiently solving the Fokker-Plank Equation (FPE), of which PyDDM provides an implementation, together with a set of optimizers that can be used to adjust the model's parameters to behavioral data.

Having a model and associated software package that provides more flexible model fits is very welcome and timely, as diffusion model applications are frequently constraint by the available software rather than the scientific question that ought to be asked. PyDDM promises to provide such a package, and appears to be sufficiently well document to ease uptake by the community. Thus, it would be a welcome addition to the currently available diffusion model fitting packages.

Some concerns should be addressed before the manuscript can be published:

1) The manuscript frequently describes the numerical solution of the FPE a "simulation", starting with the title, the introduction, the main text, etc. Commonly, solving the FPE is not considered a simulation, such that describing it as such is potentially confusing misnomer – in particular as there exist simulation-based "likelihood-free" methods to fit models solely based on simulating them. First, I urge the authors to not call solving FPEs a "simulation", but instead describe their approach as numerically propagating the probability mass, which can intuitively be thought of as performing an infinite number of simulations. Second, the authors should acknowledge likelihood-free fitting methods, like ABC (see, for example, Holmes and Trueblood, 2018 and related) to fit diffusion models – subsection “Methods for simulating the DDM and GDDM” would be a good starting point.

2) The precision and the clarity of the manuscript can be improved in many instances:

- It should be made clear that GDDMs only support Markovian processes + some additional post-processing of the computed first-passage time distributions. This is, for example, the reason why they don't support continuously varying drift rates, but this isn't at all clear from the manuscript. An additional (current) limitation is that the implementation currently only supports boundaries that vary symmetrically around zero, even though this appears to be a limitation of the provided implementation rather than a fundamental limit to the chosen approach.

- The manuscript frequently claims that the solution is "continuous" (e.g., subsection “Methods for simulating the DDM and GDDM”, subsection “Software package for GDDM fitting”) in time, even though they only provide time-discretized numerical results.

- It isn't sufficiently clear from the manuscript that all provided FPE solutions are approximate, as they discretize time and space. Currently, the manuscript only highlights the approximate nature of the forward Euler scheme (subsection “Execution time vs error tradeoff”). Indeed, it has worse numerical properties, but that doesn't make the implicit schemes non-approximate.

3) The manuscript highlights a better fit (i.e., higher likelihood, better BIC, etc.) of a DDM with time-varying boundaries and a leak, and uses this fit (of a single dataset) to re-iterate throughout the manuscript that a better model fit with fewer parameters is always more desirable (e.g., subsection “Software package for GDDM fitting”). This mis-characterizes the modeling exercise, in which the structure and presence of different components of DDMs might be as important as the quality of the fit.

4) The authors highlight three approaches to "simulate" DDMs and GDDMs, but seem to be missing a fourth based on solving Volterra integral equation, as described by Smith, (2000) and implemented by the 'dm' package by Drugowitsch et al., – which is fairly flexible, but unfortunately only provides computing the first-passage times, but no model fitting code.
