# Peer review - Round 1

Editors:
- Anna Akhmanova, https://ror.org/04pp8hn57 Utrecht University Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82493.sa0](https://doi.org/10.7554/eLife.82493.sa0)

This important paper tackles a core problem in systems biology – how to quantify kinetic parameters from incomplete and noisy experimental data. The study makes a convincing methodological contribution to the field, and its potential usefulness is demonstrated using experimental data in yeast.


---

# Peer review - Round 1

Editors:
- Anna Akhmanova, https://ror.org/04pp8hn57 Utrecht University Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82493.sa1](https://doi.org/10.7554/eLife.82493.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

[Editors' note: this paper was reviewed by Review Commons.]

Thank you for submitting your article "Quantifying how post-transcriptional noise and gene copy number variation bias transcriptional parameter inference from mRNA distributions" for consideration by eLife. Your article has been reviewed by 3 peer reviewers at Review Commons, and the evaluation at eLife has been overseen by Anna Akhmanova as the Senior Editor in consultation with two of the three original reviewers. We apologize for the delay in coming back to you, which was due to the fact that the reviewers have taken some time to respond.

The authors made substantial modifications to the text to accommodate reviewer comments and changed the title to better describe their results. The claims are now easier to assess in the context of the existent literature. Additionally, they also modified figures to more explicitly back their claims. Overall, these changes make the manuscript easier to understand.

However, there are some remaining issues that need to be addressed, as outlined below:

1. A main concern that remains is the discrepancy between nascent and mature mRNAs. The authors argue that this is presumably due to large mRNA turnover rates, which may be expected when the coat protein is not expressed. First, it would be great if the authors could back up this statement with appropriate references. Second, if I take the inferred transcription rates of ~36mRNA/min and the fraction the gene is on ~0.8, this leads to an effective transcription rate of roughly 30mRNA/min (the elongation delay should only lead to a static delay, but not affect the average amount of mature mRNAs that we observe at steady state). Now, in order to obtain an average steady state of mature mRNA around 10 transcripts (e.g., Fig. 3f), I require the mRNA degradation rate to be around 3min^-1. This would give a half-life of roughly log(2)/3=0.2min, which seems to be exceedingly low. According to literature, mRNA half-lives in yeast are typically in the order of 30min and only for very few mRNAs falls below 10mins (see e.g., Geisberg et al., Cell 2014). If we trust this simple calculation above, that would mean that the mRNA half-live is substantially smaller than the lowest reported values that I could find in the literature. I therefore still worry that there might be an issue with the data/spot extraction. At the very least, I would expect such mismatch and its potential origins to be discussed critically in the paper.

2. The second remaining concern relates to the validation against time-series data. I appreciate that the discussion around the calculation of the ACF has been extended. The authors argue that a comparison between statistics obtained from smFISH and live-cell data is not possible due to a potential detection threshold in the former. But why am I then allowed to compare the autocorrelation function (that is derived from calibration against smFISH data) with the autocorrelation of the live-cell data, which also is a statistic of the same transcriptional process? Or conversely, if it was the case that the mRNA mean and variance don't match between experiments, why should we expect the autocorrelation to match? I would be grateful if the authors could clarify these questions. Moreover, I still believe that the term "non-stationary effects" is misleading, since the slowly varying components to the ACF still need to be assumed to be in stationarity in order to capture them by an ACF with just a single time parameter (e.g., the linear fit). Perhaps "slowly-varying" would be a better term.
