# Author response - Round 1

Authors:
- Annika Boldt ([ORCID: 0000-0002-6913-5099](https://orcid.org/0000-0002-6913-5099))
- Celine Ann Fox ([ORCID: 0000-0003-1740-3765](https://orcid.org/0000-0003-1740-3765))
- Claire M Gillan ([ORCID: 0000-0001-9065-403X](https://orcid.org/0000-0001-9065-403X))
- Sam Gilbert ([ORCID: 0000-0002-3839-7045](https://orcid.org/0000-0002-3839-7045))

## Response text

DOI: [10.7554/eLife.98114.4.sa2](https://doi.org/10.7554/eLife.98114.4.sa2)

The following is the authors’ response to the current reviews.

Reviewer #1:

(1) To improve the clarity of the work, I suggest a final note to the authors to say more explicitly that objective accuracy has a finer resolution *due to the number of "special circles" per trial* in their task. This task detail got lost in my read of the manuscript, and confused me with respect to the resolution of each accuracy measure.

We agree with the reviewer that this would be a useful clarification and have therefore added the following statement to the Methods section on p. 20:

“It should be noted that the OIP has a slightly finer resolution due to the number of special circles per trial.”

(2) Similarly for clarification, they could point out that their exclusion criteria removes subjects that have lower OIP than their AIP analysis allows (which is good for comparison between OIP and AIP). Thus, it removes the possibility that very poor performing subjects (OIP) are forced to have a higher than actual AIP due to the range.

We agree this would be a useful statement to add and have included the following sentence in the Supplement on p. 8:

“Such a restriction of the threshold parameter was intended to increase the comparability between AIP and OIP, and hence improved the calculation of the reminder bias.”

The following is the authors’ response to the previous reviews.

Reviewer #1:

(1) Upon reading their response to the question I had regarding AIP and OIP, a few more questions came up regarding OIP, AIP, how they're calculations differ, and how the latter was computed in R. I hope these help readers to clarify how to interpret these key measures, and the hypotheses that rely upon them.

Regarding fitting, and in relation to power, is16 queries adequate to estimate an AIP using the R's quickpsy? That is, assuming some noise in the choice process, how recoverable is a true indifference points from 16 trials? If there's a parameter recovery analysis (ie generating choice via the fitting parameters, which will have built-in stochasticity, and seeing how well you recover the parameter) of interest would be helpful. It may help to characterize why the present study might differ from prior studies (maybe a power issue here).

The reviewer is absolutely correct that we should have provided more detail when describing our fitting procedure for the psychometric curves. We have now addressed this by adding the following statements to the Methods section and Supplement:

Page 20 in the main manuscript: “Fitting was done using the quickpsy package in R and more detail is given in the Supplement.”

Pages 8 and 9 in the Supplement:

“Psychometric curve fitting

We used the quickpsy package in R to fit psychometric curves to each participant’s choice data to derive their actual indifference point (AIP), which was operationalised as the threshold parameter when predicting reminder choices from target values. We restricted the possible parameter ranges from 2 to 9 for the threshold parameter and from 1 to 500 for the slope parameter, based on the task’s properties and pilot data. Apart from those parameter ranges, we used only default settings of the quickpsy() function.

Each participant has only 16 trials (2 for each target value) contribute to the curve fitting. To understand the robustness of the AIP based on such limited data, we conducted a parameter recovery analysis. We simulated 16 trials based on each psychometric function and re-ran the curve fitting based on those simulated choices. There was close correspondence between the actual and recovered threshold parameters (or AIPs) with a correlation of r = 0.97, p < 0.001 (see also Figure S1). In contrast, the slope parameter—which was not central to any of our analyses—exhibited greater variability during the initial fitting. This increased uncertainty likely contributed to its poor recovery in the simulation, as evidenced by a near-zero correlation (r = −0.01, p = 0.82).”

(2) Along these lines, it would be helpful for the reader to actually see the individual psychometric curve, now how quickpsy was used (did you fit left and right asymptotes), etc, to understand how that fitting procedure works and how the assumptions of the fitting procedure compare to what can be gleaned through seeing the choice curves plotted.

As stated above, we used default settings of the quickpsy() function and hence assumed symmetric asymptotes at 0 and 1. However, the reviewer mentions “left and right asymptotes”, so maybe this question is about restricting the possible parameter range for the threshold, which we restricted to values from 2 to 9, as described above.

Regarding the individual curves, we have now include the following statement on page 9 in the Supplement: “Figures S2 to S31 show the individual psychometric curves that were estimated for each participant.” Please refer to the Supplement for the added figures.

(3) A more full explanation of quickpsy, its parameters, and how choice curves look might also generate interesting further questions to think about with respect to biases and compulsivity. Two individuals might have similar indifference points, but an asymptote might reflect a bias to always have some percent chance of for example to take the reminders even at the lowest offer available for them.

We agree that this is an interesting focus which we will keep in mind for future studies.

(4) Regarding comparing OIP to AIP:

For OIP, as far as I can understand, the resolution of it is decreased compared to AIP. Accuracies for OIP can only be 0/4,1/4,2/4,3/4, or 4/4. Yet, the resolution for AIP is the full range of offers (2 to 9) with respect to the parameter of interest (the indifference point). Could this bias the estimation of OIP for instance, someone who scored 25% might actually be much closer to either 50 or 0, but we can't tell due to resolution?

As mentioned in response to comment (1), we restricted the parameter range for the thresholds to 2 to 9 to increase comparability. The reviewer is right to point out that the OIP still has lower resolution than the AIP, which is one of the downsides of having a shortened paradigm (cf. the longer version in Gilbert et al., 2019), which is optimised for online testing, especially if used in combination with additional questionnaires. We have no reason to believe though that this could have led to any bias, especially none that would contribute to the individual differences which are the main focus of our study.

Gilbert, S. J., Bird, A., Carpenter, J. M., Fleming, S. M., Sachdeva, C., & Tsai, P.-C. (2020). Optimal use of reminders: Metacognition, effort, and cognitive offloading. Journal of Experimental Psychology: General, 149(3), 501–517. https://doi.org/10.1037/xge0000652

(5) Additionally, it seems like the upper and lower bounds of OIP (0 and 10) differ from AIP (2 and 9). Could this also introduce bias (for example, if someone terrible performance, the mean would artificially be higher under AIP than OIP because the smallest indifference point is 2 under AIP, but could be 0 under OIP).

See our response to comment (1), we fixed the range to 2 to 9 (which was the range of target values used in our study).

(6) Finally seeing how CIT actually corresponds to accuracy overall (not a relative measure like AIP compared to OIP) I think would also be helpful as this is related to most points noted above.

We included the suggested test as an exploratory analysis on pages 42-43 in the Supplement: “Third, we were interested in how the transdiagnostic phenotypes would correspond to performance. We therefore fitted a model which predicted internal accuracy (that is, unaided task performance on trials where no reminders could be used) from AD, CIT, and the other covariates (age, education and gender). We found that neither AD, β = -0.02, SE = 0.05, t = 0.44, p = 0.658, nor CIT, β = -0.03, SE = 0.05, t = -0.66, p = 0.510, predicted internal accuracy.

The full results can be found in Table S13 as well as in Figure S32.”
