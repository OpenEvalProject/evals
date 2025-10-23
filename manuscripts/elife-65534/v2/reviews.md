# Peer review - Round 1

Editors:
- Jennifer Flegg, The University of Melbourne Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65534.sa1](https://doi.org/10.7554/eLife.65534.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

The manuscript uses a new approach to model the infectiousness profile of COVID-19 infected individuals. The key finding from this work is that contact tracing prevents a large proportion of onward transmissions, even if contacts within a short window (2 days) are traced. The evidence from this work emphasises the importance of contact tracing and isolation in containing the spread of COVID-19. This finding is of great interest to public health policy makers. The methodology is of general interest to modellers working on COVID-19.

Decision letter after peer review:

Thank you for submitting your article "High infectiousness immediately before COVID-19 symptom onset highlights the importance of continued contact tracing" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Rowland Raymond Kao (Reviewer #2); Elizabeth Lee (Reviewer #3).

As is customary in eLife, the reviewers have discussed their critiques with one another. What follows below is the Reviewing Editor's edited compilation of the essential and ancillary points provided by reviewers in their critiques and in their interaction post-review. Please submit a revised version that addresses these concerns directly. Although we expect that you will address these comments in your response letter, we also need to see the corresponding revision in the text of the manuscript. Some of the reviewers' comments may seem to be simple queries or challenges that do not prompt revisions to the text. Please keep in mind, however, that readers may have the same perspective as the reviewers. Therefore, it is essential that you attempt to amend or expand the text to clarify the narrative accordingly.

Essential revisions:

1. Is it possible to use more recent data? If so, the results should be updated. If not, the discussion should be expanded to highlight this caveat, otherwise the conclusion on the effectiveness of contact tracing could be overly optimistic.

2. The model code and compiled data should be made available for public use.

3. The fundamental problem is already well known, and the application to COVID-19, while useful, is better than poorer models, but only marginally better performing than the Ferretti model. The serial interval estimates are only slightly better (figure 2), there are 84% of contacts when considering tracing two days prior to symptoms, compared to what looks like about 80% for the alternative in figure 4 and by the looks of the violin plots from figure 3, quite a bit of overlap if one considers credible intervals. As such, while the analysis is a solid, useful addition to the literature, the authors should provide a better exposition on how it advances scientific insight (the fundamental issues regarding exponential distributions having been identified previously), methodologically (given the thorough analysis by Fraser et al. in 2004) or in terms of impact (given the limited improvement over the Ferretti model).

4. The framing of the paper seems very focused on improving fits to the transmission pair data, however, and I think it would be more impactful to consider the implications of poor estimation of pre-symptomatic transmission and the generation time. I think this shift in focus could also help strengthen the narrative of the paper, which wavers between focusing on model fitting and the importance of implications for contact tracing. Can the authors comment?

5. I was a bit lost in the application of the models to the contact tracing example. The definition of the contact elicitation window (lines 142-144), where identification of contacts would occur up to x days prior to contact symptom onset, makes sense theoretically in this model comparison setting, but it is hard to translate these findings to real-world application. Are there any implications that could be useful for informing contact elicitation strategy (e.g., for how many days after time of infection or symptom onset could contact tracing have a measurable benefit in preventing onward transmissions?)

6. Lines 147-151: Given that the impact on onward transmission events is so dependent on the contact tracing assumptions, I would recommend stating the assumptions explicitly here, reporting the results in relative terms as compared to a single model, or both.

7. How different are the variable infectiousness model results from parameter estimates from the original studies that reported the transmission pairs data?

8. Can the authors comment on the plausibility of the infectiousness distribution in their new proposed models? While better model fitting certainly provides a measurable improvement to leveraging existing data, I'm not aware of studies that support the discontinuous assumptions about infectiousness made here.

9. Assuming alpha means the same thing across the models, why is the 95% credible interval so large for the Feretti model? In general, the model parameters should be more clearly explained for this model. Can the authors comment?
