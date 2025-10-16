# Peer review - Round 1

Editors:
- Alison Goate, Icahn School of Medicine at Mount Sinai , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.22978.011](https://doi.org/10.7554/eLife.22978.011)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Hippocampal activation is associated with longitudinal amyloid accumulation and cognitive decline" for consideration by eLife. Your article has been favorably evaluated by Gary Westbrook (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal their identity: Michela Gallagher (Reviewer #3). The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Leal and colleagues investigated the connection between neuronal activity and amyloid-β (Aβ) in the brain of cognitively normal humans. Specifically, they assessed hippocampal activity using fMRI during a memory task which included encoding and recall of visual images, and determined how this baseline hippocampal activity was associated with amyloid deposition over time, which was measured by 11C-Pittsburgh Compound-B (PIB) PET neuroimaging. Long-term memory changes were also measured by a verbal learning long-delay free recall test (CVLT). The authors report a significant, positive association between baseline hippocampal activation and longitudinal PIB changes. This association appeared to be specific to the hippocampus, as occipital cortex and bilateral inferior frontal gyrus did not show any association with PIB change over time. There was also no association between hippocampal activity and longitudinal memory changes, but longitudinal amyloid accumulation mediated the relationship between these two variables. There was also an association between Aβ accumulation and CVLT decline over time. The authors point out that they have previously found baseline alterations in brain activity due to the presence of amyloid plaques, but they did not see a connection between PIB levels and hippocampal activity at baseline suggesting that hippocampal activity was influencing Aβ deposition independent of amyloid levels at baseline.

Essential revisions:

1) The authors point out that due to their smaller sample size, they were unable to examine the specific effects of ApoE4 carriers. This is understandable, but of the 6-7 participants who were PIB +, how many of those were ApoE4 carriers? This information should be reported. If all of the PIB + individuals were ApoE4 carriers, the effects of hippocampal activity on amyloid accumulation could be mediated by ApoE4 and it would be unclear what the relationship between hippocampal activity and amyloid accumulation is in non-ApoE4 individuals. Second, because we know APOE4 is associated with increased Aß deposition it should be included as a covariate in all of the analyses including PIB measures.

2) PIB distribution volume ratios were calculated from reactivity in cortical regions: frontal, parietal, temporal, and cingulate cortex. This allowed the effects of hippocampal activity on global amyloid deposition to be assessed. However, results from mouse studies would suggest that Aβ levels would also be increased locally, in the hippocampus, with higher baseline hippocampal activity (e.g. Cirrito et al., 2005). Was there any amyloid accumulation in the hippocampus of these subjects that was detectable and if so, does longitudinal hippocampal PIB also associate with baseline hippocampal activity?

3) Subsection “Increased Aβ accumulation associated with a longitudinal decline in memory performance”: The choice of the model here could be of some concern. The authors might consider that both PIB and CVLT are time-varying outcomes. They have summarized the changes in PIB over time and used this slope as a predictor of changes in CVLT over time. So in essence this approach uses data from PIB that occurs after a CVLT measurement to inform what will happen to CVLT at that time. Isn't this logic a bit circular?

The authors might consider an alternative modeling approach and see whether it yields the same results. Consider:

CVLT _ij = b0 + b1 PIB_i0 + b2 (PIB_ij – PIB_i0) + b3 time_ij + b4 (PIB_ij – PIB_i0) x time_ij

Basically, consider how changes from baseline in PIB are associated with changes at CVLT BUT only up to the particular time point. They can add in their random intercept and random slope for time as they did in the models they fit.

4) There is a similar concern with the analysis for amyloid accumulation mediating the influence of hippocampal activation on memory decline, where they have done the analysis on the summary measures of slope (subsection “Longitudinal amyloid accumulation mediates the influence of hippocampal activation on memory decline”).

Step 1 tested the effect of X on Y, not including M. -> Likely this is fine.

Step 2 tested X predicting M -> this is basically the model they report in the subsection “Hippocampal activation at baseline associated with longitudinal Aβ accumulation”.

Steps 3 and 4 tested M|X significant predictor of Y and X|M not a significant predictor of Y -> Here they could also adapt the model suggested above to include X.
