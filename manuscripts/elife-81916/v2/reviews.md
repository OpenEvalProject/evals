# Peer review - Round 1

Editors:
- Amy Wesolowski, Johns Hopkins Bloomberg School of Public Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81916.sa0](https://doi.org/10.7554/eLife.81916.sa0)

This large-scale collaborative study is a timely contribution that will be of interest to researchers working in the fields of infectious disease forecasting and epidemic control. This paper provides a comprehensive evaluation of the predictive skills of real-time COVID-19 forecasting models in Europe. The conclusions of the paper are well supported by the data and are consistent with findings from studies in other countries.


---

# Peer review - Round 1

Editors:
- Amy Wesolowski, Johns Hopkins Bloomberg School of Public Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81916.sa1](https://doi.org/10.7554/eLife.81916.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Predictive performance of multi-model ensemble forecasts of COVID-19 across European nations" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Neil Ferguson as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Jeffrey L Shaman (Reviewer #1); Sen Pei (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The primary comment was regarding the novelty and additional insights gained from this work. While both reviewers noted that the methodology was sound, there are other papers reporting very similar findings/work in this setting (and others) but the added value of this work, in particular, was not clear. The authors are encouraged to better articulate the added value of the work.

Reviewer #1 (Recommendations for the authors):

I guess my main question is: do we need another report on multi-model 'ensembling'? I'm not sure. This work is more substantive and validated than multi-model scenario efforts (i.e. it is forecasting not scenario play), which are often wildly speculative and in many instances shouldn't be published in high-profile journals (and I've been on a few of those papers).

I will let the editor decide.

A few other comments.

The authors use a flexible submission structure that does not appear to be strictly regularized. They write: 'Teams could express their uncertainty around any single forecast target by submitting predictions for up to 23 quantiles (from 0.01 to 0.99) of the predictive probability distribution. Teams could also submit a single-point forecast.' Were there any issues arising from this? For instance, given that there was flexibility in what was submitted-some only submitting some quantiles or a point prediction, leading to variable missingness across quantiles-are there instances where the average mean or median value does not increase monotonically with quantile?

'Coverage' is an evocative term; in weather, they more typically use 'reliability', defined as the correspondence between the forecast probability of an event and the observed frequency of that event. Consider at least noting that coverage, as defined here, is reliability. Calibration is used to describe reliability, and I note this is used in the text.

The use of relative WIS is nice.

I believe your definition of F^(-1) (α), which is confusing as I reflexively read this as a matrix inverse (perhaps use G(α) instead), is for the supremum (least upper bound), not the infimum (greatest lower bound), i.e. G(α)=sup{t:F_i (t){greater than or equal to}α}. If not, I think the {greater than or equal to} should be {less than or equal to}.

Note that in US flu forecasting, there is an expectation of observation revisions. Forecasts are validated against final revised observations, despite what was available in real time.

Reviewer #2 (Recommendations for the authors):

This is a solid and well-written work summarizing the efforts of the European COVID-19 Forecast Hub.
