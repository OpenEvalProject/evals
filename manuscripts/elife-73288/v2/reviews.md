# Peer review - Round 1

Editors:
- Jennifer Grandis, https://ror.org/043mz5j54 University of California, San Francisco United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73288.sa0](https://doi.org/10.7554/eLife.73288.sa0)

While immune checkpoint inhibitors (anti-PD-1 targeted agents) are now FDA-approved for the treatment of locally advanced and recurrent or metastatic head and neck cancer, predictive biomarkers are lacking. In this study, the co-authors have developed an algorithm that they conclude predicts the clinical outcome to multimodality immunotherapy. While this machine learning approach is intriguing, prospective validation of the proposed immune-based signature is essential to begin to incorporate such an approach into the clinic.


---

# Peer review - Round 1

Editors:
- Jennifer Grandis, https://ror.org/043mz5j54 University of California, San Francisco United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73288.sa1](https://doi.org/10.7554/eLife.73288.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Predicting Progression Free Survival after Systemic Therapy in Advanced Head and Neck Cancer: Bayesian regression and Model development" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Wafik El-Deiry as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Reviewer #1 (Recommendations for the authors):

Thinking in terms of what would be clinically tractable, I suggest the authors use ML techniques to reduce the assay panel size to a more parsimonious number of covariates, to train this in their existing dataset, and to then validate this in an independent cohort.

Reviewer #2 (Recommendations for the authors):

Barber et al. present a manuscript discussing predictive factors for chemotherapy efficacy in head and neck squamous cancer (HNSCC). The paper is well written, , and its style/formatting are optimal. The baseline signature moderately predicted outcome, and the data after one cycle further improved the algorithm, though this decreases its utility as a pure predictive tool. It is interesting that a subpopulation of monocytes, a subset of white peripheral cells long suspected to correlate with outcomes in HNSCC was one of the key drivers of the algorithm. However the overall impact in the field of this work seems limited.

Comments:

– The authors focused on immune cell subpopulations and exosomes, which narrows the scope (no cytokines or other biomarkers were included).

– The signatures were not prospectively validated on an independent cohort.

– Unfortunately this algorithm predicts outcome for a first-line therapy that is no longer considered to be the standard of care for HNSCC.

– The outcome measure is PFS, which is appropriate for therapy effect but not the standard in first line therapy (OS would be).

– The conclusions of the manuscript are supported by the data, but some of the caveats (such as the lack of a validation cohort, key in predictive biomarker development), are not addressed.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting the paper entitled "Predicting Progression Free Survival after Systemic Therapy in Advanced Head and Neck Cancer: Bayesian regression and Model development" for further consideration by eLife. Your revised article has been evaluated by a Senior Editor and a Reviewing Editor. We are sorry to say that we have decided that this submission will not be considered further for publication by eLife.

Reviewer #1 (Recommendations for the authors):

Thank you for the opportunity to review this revised manuscript. I feel that the authors have made a good-faith effort to answer all of my prior comments. I, unfortunately, feel that the prior comments have not been very completely addressed.

First is the issue of unmet clinical need. Several reviewers asked whether a predictive biomarker for chemotherapy is relevant, in the era of ICB. I do in fact agree with the authors that there is still clinical value to predicting response to regimens such as EXTREME which do in fact still have a role in the treatment of HNSCC, and are understudied.

However, I did raise the question as to whether this fairly labor-intensive, difficult-to-scale, and expensive assay would add value to the fairly inexpensive and widely available (although admittedly not widely used) biomarkers we already have. I gave the example of NLR but also alluded to simple nomograms that include clinical factors such as age, performance status, tumor stage, etc. It seems important to more convincingly make the case that this model outperforms the widely available, inexpensive data we already have. Looking at the c-indices for this model, I am not sure this is the case. I again would advise this be shown rigorously with direct comparisons, to make the case that this model adds value.

The validation set is very important to the conclusion that this assay has potential clinical use. I fully recognize that a validation set is hard to come by. But this is the "acid test" for such an assay. The validation data here is promising, and again, I understand how hard it is to gather such data, but it is not very convincing. Only 8 patients, with no PFS data (iRECIST is used, with a 50% objective response rate, which seems very high). To support the claim that such an assay has clinical value, a much broader set of validation data are needed.

I raised the question earlier about the large number of patients excluded due to a lack of biospecimens and am concerned that this may limit the results, as this is akin to unequal censoring in a clinical trial. It would be important to compare the patients being studied and those not being studied. This was not addressed.

As with the other reviewers, the lack of OS data is a weakness here. This is a more minor point, as I do understand that the reviewers tried and were unable to obtain this data from the industry sponsor. I want to stress this is a minor weakness compared to some of the above points. However, multiple co-authors have very significant industry COI (co-authors each receiving personal payments from 15-20 companies) and I am concerned that the withholding of OS data (which has already been collected and is in fact a component of PFS) may reflect other motives on the part of the industry sponsor with whom some authors may be conflicted. Nevertheless, if the data are unavailable, a suggestion: if OS data are not available, perhaps the authors could show rigorously that PFS is a very good surrogate marker of OS in this disease.
