# Peer review - Round 1

Editors:
- Alex Sigal, https://ror.org/04qzfn040 Africa Health Research Institute, University of KwaZulu-Natal South Africa

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69949.sa0](https://doi.org/10.7554/eLife.69949.sa0)

Surveillance screening can help us estimate the prevalence of SARS-CoV-2 infection and co-infection with other respiratory pathogens. This work offers a high-throughput and cost-effective method to do such surveillance based on RT-LAMP combined with deep sequencing. This method can be applied to clinical samples for an accurate reading of the fraction of infections where the SARS-CoV-2 titer is moderate or high.


---

# Peer review - Round 1

Editors:
- Alex Sigal, https://ror.org/04qzfn040 Africa Health Research Institute, University of KwaZulu-Natal South Africa

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69949.sa1](https://doi.org/10.7554/eLife.69949.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "COV-ID: A LAMP sequencing approach for high-throughput co-detection of SARS-CoV-2 and influenza virus in human saliva" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Dominique Soldati-Favre as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers assessment was that, while the approach may make an important contribution to genomic surveillance of SARS-CoV-2, it was unclear if it would deliver the benefits of decreased cost, time, and labor in a real-world situation.

The main weakness pointed out by both reviewers was that much of the work was done on spiked samples. High throughput on clinical samples was not demonstrated, as only 8 were used.

The reviewers agree that the type of clinical sample tested, whether saliva or swab, is less important. What the proof of concept would require is at least a "superpool" of several pooled wells, with each well containing the maximum number of samples (or close to it). This way, both pooling steps are tested.

Reviewer #1 (Recommendations for the authors):

I do not have specific technical concerns, but the methodology is difficult to evaluate with results from only 8 clinical samples. Factors such as differing Ct values, sample quality, and others should be evaluated to see if the approach could be used with high throughput, and this would require at a minimum a "superpool" of several pooled wells with each well containing the maximum number of samples. Participant Ct values should be presented and be correlated to detection. Swab transport media can substitute if saliva is not available. Negative samples should be combined with qPCR confirmed positive samples and false negative and false positive rates determined.

Given that a fast turnaround time is key to success, the approach proposed by the authors is unlikely to be used except in very large studies with ready access to deep sequencing, in which case they would also have access to a PCR. Where the approach may fill an unmet need is genomic surveillance of the virus in the population which would likely involve reconfiguring the system to sequence spike.

Reviewer #2 (Recommendations for the authors):

I enjoyed reading this manuscript and was impressed with its potential to make a significant contribution to population-level testing of infectious disease, e.g. during the COVID-19 pandemic. Assuming that you are able to able to address the points in the Public Review, I would be pleased to recommend this manuscript for publication in eLife. In particular, I think it would be very helpful to perform more testing of your method from clinical samples. I realise that these may be difficult to acquire and so I do not want to be too demanding in the exact source of these samples, just something a bit more realistic than the spike-ins used extensively here.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your article "A LAMP sequencing approach for high-throughput co-detection of SARS-CoV-2 and influenza virus in human saliva" for consideration by eLife. Your revised article has been reviewed by 2 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Dominique Soldati-Favre as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

The main comment of the Reviewers was to show feasibility with more than 8 clinical samples, given that the reason for the approach was to do high-throughput analysis of clinical samples.

The authors therefore used 120 clinical samples in an experiment to show that the approach can be scaled up. The results are presented in Figure 2—figure supplement 2.

While the reviewer comments were addressed, the results seem to show that the sensitivity of the approach (rate of false negatives) is considerably inferior to that of qPCR: By counting on panel A of the figure, there are 17 qPCR-positive samples. Thresholding by the highest values of SARS/Spike+1 in the qPCR negative samples (about 0.1), 8 samples out of 17 are above threshold by the authors' approach. Therefore, 9 out of 17 (53%) are false negative.

Because the sample is imbalanced – many more qPCR negatives relative to positives – the false-positive rate (1-specificity) is not sensitive to false positives and the ROC curves are overly optimistic in describing the result.

The reviewers agreed that those intending to implement the approach can decide for themselves whether it is right for them, but that these limitations should be clearly stated. The authors can use a Precision-Recall curve which does not consider the false positive rate to quantify the performance of their approach.

Also, the strategy of an artificial N2 spike-in is not described until later in the MS. It should be described for the figure to explain the SARS/Spike+1 ratio.

Reviewer #1 (Recommendations for the authors):

The main comment of the Reviewers was to show feasibility with more than 8 clinical samples, given that the reason for the approach was to do high-throughput analysis of clinical samples.

The authors therefore used 120 clinical samples in an experiment to show that the approach can be scaled up. The results are presented in Figure 2—figure supplement 2.

Using qPCR as the gold standard, there are 17 samples (estimated, from counting the points) out of 120 (14%) that had a detectable Ct value. Using the presented approach without thresholding, there were 86 samples out of 120 (72%) where viral sequences were detected.

Thresholding by the highest values of SARS/Spike+1 in the qPCR negative samples (about 0.1), 8 samples out of 120 (7%) were above threshold, with 9 out of 17 (53%) being false negative.

If this is a misinterpretation of the results, then I would suggest clarifying it. If not, the method presented has low sensitivity, unless indeed the majority of people in the cohort had SARS-CoV-2 infections not detected by qPCR.

Also, the strategy of an artificial N2 spike-in is not described until later in the MS. It should be described for the figure to explain the SARS/Spike+1 ratio. The name of the denominator should perhaps be changed to avoid confusion with the SARS-CoV-2 spike gene. The horizontal line at 0.2 which appears to be a threshold in Figure 2—figure supplement 2B should be explained and the scale changed to log to make all the values visible and not have a scale interruption.

Reviewer #2 (Recommendations for the authors):

I thank the authors for their efforts in revising this manuscript and particularly for performing another round of sample collection/analysis. The results presented in Figure 2 - Figure Supplement Figure 2 significantly improve the statistical confidence in the ability of this method to identify positive clinical samples and the ROC plots will allow readers to make their own quantitative judgements of the performance of this method for their own purposes. I also thank the authors for making all the minor edits I suggested in my previous review.

I now fully support publication of this article in eLife as is.
