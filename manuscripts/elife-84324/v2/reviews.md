# Peer review - Round 1

Editors:
- Laura L Colgin, https://ror.org/00hj54h04 University of Texas at Austin United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84324.sa0](https://doi.org/10.7554/eLife.84324.sa0)

This valuable work in human subjects reports that sounds that were associated with specific memories during waking behaviors can trigger the reactivation of these memory representations during REM sleep. Convincing evidence is provided to support the conclusions. The work expands our understanding of memory processing during sleep.


---

# Peer review - Round 1

Editors:
- Laura L Colgin, https://ror.org/00hj54h04 University of Texas at Austin United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84324.sa1](https://doi.org/10.7554/eLife.84324.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Targeted memory reactivation in human REM sleep elicits detectable reactivation" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Laura Colgin as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Kenneth A Norman (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Reviewers agreed that there is a lack of clarity in the Methods as currently written which make it difficult to evaluate the results (as one example, what features go into the classifier?). The Methods will need to be revised to provide clarification before a decision can be made about whether the claims in this manuscript are rigorously supported by the results. Please see individual reviews below for details.

2) Some claims are not well supported by the presented results. Additional analyses are suggested that may strengthen the evidence for some of the claims. Claims with insufficient support (e.g., claims related to theta, claims related to dilation/compression, etc.) should be removed from the paper unless additional analyses/results can be included to provide sufficient support. Please see individual reviews below for details.

3) The justification for excluding trials (e.g., discarding low variance trials and discarding trials to match the number of clear trials across participants) is unsatisfactory. Please see individual reviews below for details.

Reviewer #1 (Recommendations for the authors):

My specific suggestions are as follows:

I suggest including a section in the methods explaining how TMR sounds were presented during REM sleep.

Please describe the methods for the searchlight analysis used to select channels of interest and a region of interest.

It would be helpful to have more details about how the LDA classifier was trained on the sleep data. It is my understanding that each sleep trial began with a TMR cue (a sequence of tones), and that both the cued and uncued sequences were associated with both left and right-handed button presses (each sequence contains 1,2,3, and 4). It is unclear to me how the classifier is then trained to discriminate between left vs. right hand.

It would also be helpful to have more details about testing on the imagery data, including more details about how the imagery data were prepared and preprocessed. Was the classifier tested on the imagery data from both pre- and post-sleep, from both cued and uncued sequence trials?

Regarding the procedure of rejecting trials with low variance ('Because TMR will not be effective with all trials, we also rejected trials with a low variance that do not differ from their mean across time since they are unlikely to contain a response.') – my reading of this is that "a response" refers to reactivation. If that is the case, then trials from the adaptation night would not contain "a response". Or perhaps a response more broadly refers to any event-related response to the sound cue. To alleviate any concerns related to this, it might be helpful to include some more descriptive information about how many trials are included in various conditions/analyses.

Reviewer #3 (Recommendations for the authors):

One recommendation is for the authors to clarify the methods. In particular:

The description of the "searchlight" procedure that was used for feature selection lacked detail. I couldn't figure out what the authors did from what was written in the paper. What features were included in each searchlight? Did the searchlights encompass multiple electrodes? What frequencies were included for each electrode? or did the authors use raw power? Also, I don't understand the statement on line 354 that "this was done on different participants who performed the same task to avoid circularity". Does this mean that feature selection was done separately for each participant, using a nested cross-validation procedure? or by "different participants" do you mean "participants who were not included in the main sample for this study"? Much more detail is needed here.

Is the main classification analysis done within participants (i.e., train on one participant's sleep data, test on the same participant's wake data) or across participants? I am assuming the former, but I tried looking this up and I could not find it (apologies if I missed it). Relatedly, for the statistics, is AUC first computed within each subject and then averaged across subjects, or is it computed differently?

Line 375 mentions a PCA step in the time dilation analysis, but it is unclear what the features are that are being fed into the PCA (are the feature vectors of dimensionality n_frequencies x n_electrodes x n_timepoints, or are they something else, and is the PCA looking at variance across trials, or across time points within a trial, or something else).

More information on the cluster-based permutation (i.e., what was permuted?) would be useful.

My second recommendation is for the authors to revisit the issues mentioned in the public review regarding theta-mediation, time dilation/compression, and sequence-specificity of the classification-behavior relationship. If the authors can not strengthen their claims, they should step back from making these claims.

Regarding the analyses looking at theta: The authors' median split approach is not the most statistically powerful way to address this question (see, e.g., papers by Gary McClelland about median splits). Using a more continuous regression approach might yield better results.

Regarding the analyses looking at dilation/compression: Here, the authors' main task is to show that their results necessitate a dilation/compression explanation, as opposed to simply being due to autocorrelation in feature patterns over time.

Regarding the analyses looking at the "sequence-specificity" of the classifier-behavior relationship: To assess sequence-specificity, the authors could run a bootstrap where, for each resampling of subjects, they compute the difference between the fisher z of the cued sequence and the fisher z of the uncued sequence.

I was intrigued by the authors' use of training on sleep data and testing on wake data. The justification for this (that features that are reactivated during sleep may be a subset of features that are reactivated during wake) is a sensible hypothesis but conjectural. If this hypothesis is correct, it implies that results should be worse if classifiers are trained on wake and tested during sleep. I don't think it's necessary to do this, but if the authors tried the reverse approach it would be useful to see the results (if wake-trained classifiers are indeed worse than sleep-trained classifiers, this would provide some converging support for the authors' claim that reactivated features during sleep are a subset of features activated during wake). It might also be useful to see the results if the authors train on sleep and test on sleep.

For the analyses looking at whether theta power is used for classification, the authors perform a "negative control" where they include theta-band oscillations (but filter out other bands) and show that reactivation goes away. They may also want to include a "positive control" where they filter out theta-band oscillations and show that reactivation persists.

The fact that objects and faces were associated with the motor responses (crossed with the left and right responses) suggests to me that the authors may have considered looking at object/face classification in addition to the left/right classification. If the authors did in fact perform other analyses (that yielded null results) I think it would add to the value of the paper to report them here.

The authors match the number of "clean trials" across participants, using the smallest number that was obtained across all participants (366) – this seems like it is unnecessarily discarding useful data. If the AUC is computed within each subject and then averaged across subjects, then each subject will "count the same" regardless of how many trials are included.

Lines 300-302: why did you include these four blocks that contained random sequences?

How do the authors reconcile the overall lack of benefit from REM TMR with the finding that, across participants, the degree of reactivation evoked by REM TMR cues correlates with behavioural change? The explanation on lines 244-246 ("This absence of behavioural improvement could be due to individual differences in the way REM processes the task, potentially relating to an interaction between the extent or style of learning and REM processes") was not helpful to me in reconciling these two points – the authors might want to further unpack their argument here to make it clearer.

Phrase: "wake-like memory reactivation" – I am not sure what this phrase means.
