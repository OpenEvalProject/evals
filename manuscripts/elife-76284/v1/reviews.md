# Peer review - Round 1

Editors:
- George H Perry, https://ror.org/04p491231 Pennsylvania State University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76284.sa0](https://doi.org/10.7554/eLife.76284.sa0)

Zhang et al. use evolution-guided mathematical models to guide the timing and dosing of abiraterone treatment in castrate-resistant prostate cancer. While the sample size is limited, the implications of the study outcome are broad and compelling, and the article importantly highlights the transformative potential of deeply interdisciplinary research.


---

# Peer review - Round 1

Editors:
- George H Perry, https://ror.org/04p491231 Pennsylvania State University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76284.sa1](https://doi.org/10.7554/eLife.76284.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Evolution-based mathematical models significantly prolong response to Abiraterone in metastatic castrate resistant prostate cancer and identify strategies to further improve outcomes" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by George Perry as the Reviewing and Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers are positive about your paper but requesting several points of clarification in their below reviews. Please address these points in your revision.

Reviewer #1 (Recommendations for the authors):

I suggest the authors clearly describe what has been published and what the difference is in the current model. It seems the mathematical model described 204-227 is the same as the original model in Zhang J et al. 2017, however, many details were missing (e.g. what are the cell types, why some parameters are set in a certain way) and just reading this part alone without reading Zhang J et al. 2017 is confusing.

Many mathematical details are missing: Line 427 says "The full details of the mathematical model are presented in Supplementary Mathematics section below." While there is nothing under the Supplementary Mathematics section on the last page. Line 246-249 only vaguely say there are patient-specific parameters and there are shared ones. However, there are important assumptions about the model that should be introduced more clearly. I found out from the supplement that competitive coefficients are set as the same across all patients, while the authors also showed that these are critical to determining outcomes. The authors should provide more explanations or analysis about why is alright to set the same if infer in ADT more successful patients and not successful patients if their values are similar.

The authors should give more explanations about how to understand the figures. The figure 3a is for a patient with an initial resistant fraction of 0.03 but based on the density value for the red line and blue line in the bottom panel of figure 3a, it doesn't seem like the fraction is 0.03. I have the same question for all such figures in the paper. And figure legend doesn't really match the plot for the top panel of figure 3a, does the red color indicate treatment? And line style indicates real/modeled?

I also suggest the authors illustrate more of how the clinical guidance can be derived from the current analysis. Eg. "include more rapid withdrawal of therapy when PSA crosses the 50% threshold". Some simulations showing the impact of withdrawal at the different thresholds will be useful.

The manuscript has not talked about Figure 4 (I didn't find where it is referenced).

Analysis code should be available for review.

Reviewer #2 (Recommendations for the authors):

There is a significantly longer median time to progression, 33 months in the patients that received adaptive therapy group compared to 14.3 months in the SOC cohort, and OS was 58.5 months compared to 31.3 months. It would be very informative to highlight what percentage of mCRPC patients could benefit from evolution-informed treatments, considering those that have <50% PSA decline after the first arbiterone therapy (statistically), those that progress while on arbiterone treatment, and those that have evolutionary dynamics that violate the assumptions of the model.

The mathematical model is clearly described. As it takes a significant portion of the Results section, it would be helpful for the reader to highlight the changes and advantages compared to the previously published model in 2017, Nat Comms.

In addition, while the manuscript is clearly written, it would help a lot for the reader if the abbreviations such as TTP in the abstract, TP, T+, and T- are described in their first use (Line 206 or Abstract), without the need to read previous work from the authors.

I couldn't find the information on how many patients didn't undergo castration or a table with a summary of the clinical features for each patient, ideally along with PSA levels, duration of arbiterone treatment, and the number of arbiterone treatments.

The results show no statistically significant difference between the two patient groups (SOC and adaptive therapy group) in terms of tumour stage, Gleason score, and pretreatment PSA.

Unfortunately, the sample size wouldn't allow for multivariate analysis. What about based on whether patients underwent castration-resistant therapy?

The SOC cohort had prior therapy history (Line 407), but it is not clear from the text whether patients from the adaptive therapy cohort also had prior therapy history.

Some figures in the supplementary would need a higher resolution

Is there a difference in the competition coefficient ratios between SOC and adaptive therapy cohorts, at the start of treatment and at progression?
