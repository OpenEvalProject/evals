# Peer review - Round 1

Editors:
- Lauren Childs, United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63537.sa1](https://doi.org/10.7554/eLife.63537.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This work assesses the role of within-host viral shedding dynamics and contact heterogeneity on distribution of transmission events in SARS-CoV-2 and influenza. Using multi-scale modeling, predictions are made on the manner and contribution of super spreading to transmission. This model has the potential to provide insight into transmission dynamics of SARS-CoV-2, which could help inform policy.

Decision letter after peer review:

Thank you for submitting your article "Viral load and contact network predict SARS-CoV-2 transmission and super-spreading events" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Aleksandra Walczak as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Jonathan Forde (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

This work assesses the role of within-host viral shedding dynamics and contact heterogeneity on distribution of transmission events in SARS-CoV-2 and influenza. Using multi-scale modeling, with similar resulting generation time and serial interval distributions to published work, predictions are made on the manner and contribution of super spreading to transmission. Distinctions are seen when comparing to applying a similar modeling framework to influenza.

Essential revisions:

1) Statistical analysis:

The model parameters are estimated using an exhaustive grid search, which yields good fits for the best-fit values, but there is no assessment of statistical certainty in the parameter values. The authors essentially adopted a strategy in the spirit of approximate Bayesian computation (ABC), by proposing parameter values, simulating from a model, and comparing summary statistics of the simulated output to known values from the literature. The analysis would be helped by doing a more formal ABC analysis, as this would provide a better sense of how narrowly constrained the parameter values are given the available data. At minimum, it would be more convincing to consider additional parameter sets grided across a narrowed region of parameter space before selecting an optimal fit.

2) Model validation

The state of our knowledge about these infections is limited, both by the short time during with this research has been conducted, and the paper's need to rely on data taken from before the introduction of confounding factors such as social distancing and widespread mask usage. For this reason, in addition to the included sensitivity analysis for the model parameters, a sense of the sensitivity of the model's conclusions to the data set to which it is being fitted is needed. How much would these results change if there are errors in our understanding of the distribution of individual R0 values, or serial intervals?

3) Distinction in assumptions for flu and covid

The populations on which the histograms for the two diseases are based are quite different. For SARS-CoV-2, the studies are from China (Shenzhen, Tianjin and Hong Kong), while those for influenza are from Switzerland. Could cultural differences be relevant? What about seasonal differences, as the time during which the early SARS-CoV-2 studies occurred was necessarily restricted?

Furthermore, the explanation for the difference between influenza and COVID is based primarily on differences in contact patterns. While the Discussion clarifies this to be based on the efficiency with which exposures lead to infections (and pre-symptomatic transmission), which does sound like a viral parameter, rather than a social one. These viral factors do seem more believable than having to explain why the patterns of social contact exhibited by influenza patients would differ from those of SARS-CoV-2 patients. More focus on possible mechanistic explanations is warranted.

Title: "Contact heterogeneity" rather than "contact network" is more appropriate for the title as no network is considered.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Viral load and contact heterogeneity predict SARS-CoV-2 transmission and super-spreading events" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Aleksandra Walczak as the Senior Editor. The Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Revisions:

A key definition in the work (as stated in the Discussion) is the exposure contact. However, apart from the parenthetical definition in the Discussion, exposure contact is not clearly defined. This is particularly important as estimates on the exposure contact seem to impact the estimates on the viral load to infectiousness functional relationship. In particular, infectiousness is defined "… as the viral load dependent probability of transmission given direct airway exposure to virus in an exposure contact." Why does the parameterization for this change so significantly pre and post lockdown when the main difference appears to be in exposure contacts? The explanation given refers to "… more prolonged and intense exposure contacts…" This seems to imply an unequal reflection of what an "exposure contact" truly means. Furthermore, how does the "exposed contact rate" compare with exposure contacts.

Figure 10. This new figure is confusing. In the text, viral shedding kinetics are referred to as panel (A) and kinetics of infectivity as panel (B), but they are both part of panel (A) in the figure. What is different between the SARS-CoV-2 and Influenza schematics in panel (B). Panel (C) is referred to in the text but is not in the figure.
