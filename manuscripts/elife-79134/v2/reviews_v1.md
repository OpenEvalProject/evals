# Peer review - Round 1

Editors:
- Katelyn Gostic, https://ror.org/024mw5h28 University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79134.sa0](https://doi.org/10.7554/eLife.79134.sa0)

By analyzing a carefully curated dataset of cases observed early, and adjusting for multiple forms of bias, this study provides convincing evidence that in the absence of public health interventions, the duration of infectiousness of COVID-19 (original variant) is longer than previously estimated. These important findings improve our ability to model counterfactual intervention-free scenarios, add to evidence that interventions have reduced the duration of infectiousness, and provide an example of how to navigate the biases and pitfalls inevitably present in outbreak data.


---

# Peer review - Round 1

Editors:
- Katelyn Gostic, https://ror.org/024mw5h28 University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79134.sa1](https://doi.org/10.7554/eLife.79134.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "The unmitigated profile of COVID-19 infectiousness" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Aleksandra Walczak as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: James A Hay (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

(1) All three reviewers raised questions about the potential impact of ascertainment bias and small sample size in the unmitigated transmission pair data. Please address potential impacts on the results, and qualify the conclusions if appropriate.

(2) Address questions from two reviewers about the accuracy of fixed incubation period estimates obtained from a meta-analysis. Should these be corrected for the same biases that affect generation interval estimates?

(3) Please provide more detail about the methods used to estimate R0 and the generation interval of variants of concern. Please also consider editing the methods for clarity and readability by a general audience.

(4) In order to make the manuscript more accessible to a general audience, please provide a clearer explanation of why short forward intervals are overrepresented in a growing epidemic. Consider including a diagram or simulation, as suggested by Reviewer 3.

(5) Please address the impact of uncertainty in viral load trajectories on individual generation times, on the residual fraction, and on our ability to infer generation intervals for variants of concern using viral load trajectories. On a related note, please consider modifications to Figure 6a so that it is easier to visualize whether the viral load trajectory aligns well with the claim that 18% of transmission occurs >14d after infection.

Reviewer #1 (Recommendations for the authors):

1. The methods section is complete, but it might be easier to follow with more attention to organization, transitions, and maybe with additional subheadings. In particular, it would be helpful if key details like which parameters are being estimated, and which data you're fitting to, were easier to locate in this section.

2. The Introduction and Methods cover a lot of ground summarizing all the forms of bias and adjustment that go into producing an accurate unmitigated estimate, and it is currently a bit hard to keep track of all these details. It could be helpful to provide some sort of list, table, or summary paragraph to help readers keep track of all the forms of bias and adjustment that this analysis deals with, including references where appropriate. It would also be helpful to more clearly state that the main contribution of this study is to collect and apply all these statistical corrections to a carefully curated dataset.

3. I got tripped up by this statement on page 12:

"We find that our framework is able to properly reproduce the realized serial interval distribution given the growth rate in the early stages of the outbreak in Wuhan, China (Figure 3b)."

Aren't the models fit to the SI data-meaning that we expect this result and should be alarmed by anything else? I think that this is just a wording issue and that what you're trying to say here is something like, "With or without the growth-rate adjustment, the model was able to fit the observed serial interval data well (Figure 3b)". But with the current phrasing, it sounds (at least to me) like this is being presented as some sort of independent validation of the model. For the same reason, I'd consider changing "estimated SI" to "fitted SI' in the Figure 3b legend.

Reviewer #2 (Recommendations for the authors):

As well as the broad comments made in the public review, I had the following comments:

– "This dataset includes a total of 77 transmission pairs with a mean serial interval of 9.1 days (7.9-10.2 95% CIs) and a standard deviation of 5.2 days. This is substantially longer than the mean of 7.8 days suggested by Ali et al" – is it possible to quantify this difference statistically (e.g. with a test for difference in means between the samples)? Given a mean of 9.1 days and SD=5.2, it wouldn't seem implausible for a random subsample from this dataset to have a mean of 7.8?

– Could the authors clarify which formula they used from Wallinga and Lipsitch (2007) to calculate R0 from generation time, as the exact calculation will depend on assumptions about the distribution of generations etc? I presume the authors used an appropriate formulation but would be useful to state explicitly. The finding that the early R0 is similar despite a longer generation time seems a bit counter-intuitive, so it would be helpful to have some more discussion about what's happening here.

– It would be useful to give some intuition about why changing the baseline incubation period had a limited effect on the results. Is this because the epidemic phase adjustment dominates in the calculation?

– The methods for scaling the generation interval for other VOCs are described briefly in the caption to Figure 6, but it would be helpful to have the calculation given explicitly in the methods, so there is no ambiguity in terms like "ratio of the clearance's durations". Also in this figure, it's unclear where Α line is in B and C, so worth mentioning in the caption. Finally, I didn't follow this sentence: "The inset shows a zoom-in on the period of 12-24 days after exposure, a period in which there is a substantial difference between the current estimate and those from previous studies." Are the presented estimates not all new ones derived from the current study and viral shedding data.

– I appreciate that not all of these studies were available at the time of submission, but it could be helpful to update the discussion to also place the results in the context of more recent viral culture duration from serial swabbing data (Chu et al., JAMA Int Med 2022) and/or shedding profiles in human challenge data (Killingley et al., Nature Med 2022).
