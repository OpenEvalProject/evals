# Author response - Round 1

Authors:
- Jan Drugowitsch
- Gregory C DeAngelis
- Eliana M Klier
- Dora E Angelaki
- Alexandre Pouget

## Response text

DOI: [10.7554/eLife.03005.018](https://doi.org/10.7554/eLife.03005.018)

1) How were the degrees of freedom calculated for the BIC? Was the model probability calculated by computing a BIC for each subject, and then summing these across subjects? Another approach that is used in functional imaging is to compute exceedance probabilities. Model evidence across multiple subjects inflates degrees of freedom, and exceedance probabilities have been developed to deal with that problem. This is similar to fixed effects vs. mixed effects (or hierarchical) models for analyzing behavioral data across multiple subjects.

As we fitted the model parameters for each subject separately, the BIC was computed for each subject separately and then summed. The details of this procedure are described in the Data Analysis subsection in Methods. All but one model discussed in the main text have the same number of parameters, such that other approaches to taking the number of model parameters into account would have led to the same result.

As suggested by the reviewers, we have additionally added a random-effects Bayesian model comparison, which was added to Figure 7–figure supplement 1 (panels b and c). The results of this analysis are consistent with our previous BIC analysis, adding strength to the conclusions. We thank the reviewers for this good suggestion.

2) Within the Results section there is a paragraph about how to set the noise terms in the model, but the reader finds that out several lines ahead. This would be easier to follow if an introductory sentence were added along the lines of 'The noise terms eta_vis and eta_vest play crucial roles in the model, as they relate to the reliability of the momentary sensory evidence. To specify the manner in which such noise may depend on motion coherence, we relied on fundamental assumptions about how optic flow stimuli are represented by the brain...”

Thank you for this suggestion. We have modified the beginning of this paragraph as suggested.
