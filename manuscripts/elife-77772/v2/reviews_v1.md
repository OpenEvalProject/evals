# Peer review - Round 1

Editors:
- Adrien Peyrache, https://ror.org/01pxwe438 McGill University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77772.sa0](https://doi.org/10.7554/eLife.77772.sa0)

This paper will be of interest to the neuroscience community studying brain oscillations. It presents a new method to detect sharp wave-ripples in the hippocampus with deep learning techniques, instead of the more traditional signal processing approach. The overall detection performance improves and this technique may help in identifying and characterizing previously undetected physiological events.


---

# Peer review - Round 1

Editors:
- Adrien Peyrache, https://ror.org/01pxwe438 McGill University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77772.sa1](https://doi.org/10.7554/eLife.77772.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Deep learning based feature extraction for prediction and interpretation of sharp-wave ripples" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and John Huguenard as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

In the present study, Navas-Olive et al., introduce a novel method to detect and characterize sharp-wave ripples (SWRs) in the hippocampus. Specifically, the study presents how a convolutional neural net (CNN) may achieve better performance than more traditional signal processing techniques. While each reviewer has raised a number of specific concerns about the present study, there was an agreement that the following essential revisions needed to be addressed to warrant publication of the manuscript.

1. The study compares the performance of SWR detection with a CNN and with more classic signal processing methods (i.e. filters). However, several aspects of this comparison are unclear, if not misleading. First, while the CNN has obviously been optimized to detect SWRs, the study should clarify how the filter parameters were chosen. The study should demonstrate that fine-tuned filters still underperform the CNNS. Moreover, the study should present a fair comparison of the performance of each method, based on the same ground truth data, using the same number of channels, etc.

2. It is unclear what types of events are detected by the CNN and missed by the traditional approach, how can one be sure these are more physiologically relevant. Isn't it possible that some of these events result for example from an increase in spiking without clear underlying SWR? The study should provide more information regarding the nature of the events that are detected by the CNN and not the traditional approach.

3. The study should also convincingly demonstrate that the CNN can be applied to a new dataset and still outperform the spectral approach without (or at least little) re-training. This is key to validating the method.

4. The higher performance of the CNN should be demonstrated with, for example, manual scoring of false positive/negative rates. In summary, there should be no d.ubt that the CNN outperforms the spectral approach across conditions and datasets.

Please see the reviewers' comments below for more details.

Reviewer #1 (Recommendations for the authors):

– Several times throughout the paper the authors claim that "spectral methods fail to capture the mechanistic complexity of SWRs". I understand that they want to make the point that spectral methods are based mainly on the spectrum, and therefore constrain the variability of the events to be detected. However, this sentence is misleading as spectral methods could also be used to detect variability of events if properly tuned, even in separate runs throughout one dataset if that is what is wanted. This is a rather important point as it can be misinterpreted by the fact that those methods cannot be used to detect a variety of SWRs, which is not true if they are used properly.

– Several times the authors also claim that they are able to detect "physiologically relevant processes" with their new method, but as it is, the manuscript just shows that they can detect new events, and remain to be shown whether they are "physiologically relevant".

– In "Figure S1. Network definition and parameters" do the authors mean "Figure 1"? In Figure 1 the authors show how they tune the parameters that work best for their CNN method and from there they compare it with a filter method. Presumably, the filter method has also been passed through a parameter tuning process to be used to its best performance but this is not stated and not shown anywhere in the paper. If "relatively arbitrary" parameters are used, then this could be the explanation of why the performance of the filter method is worst compared to CNN.

– In Figure 2. What do the authors mean by absolute ground truth? I could not find a clear explanation in the text and it seems to me that the authors refer to "absolute ground truth" as the events detected by CNN? If this is the case I am not sure is the best approach to use this as a fair comparison of "absolute ground truth". Similarly, I don't think is the best approach to use the "mean reference of performance" the score of a second research (nGT) of that of the previous researcher (oGT) as the second score will inherit the fails of the first score. Instead, maybe compare the two of these metrics separately or take the average of the two of them?

– The authors should show at least one manual score of the performance of their CNN method detection, showing examples of what they might consider false positives and missed scores. In figure 2D they did it for an external dataset and they re-scored it in order to "correct" the original ground truth. They show a "false positive" that they corrected but as I understand it, if that event was not part of the ground truth is a "missed" or "false negative" event instead of a "false positive" right?

– In Figure 2E the authors show the differences between CNN with different precision and the filter method, while the performance is better the trends are extremely similar and the numbers are very close for all comparisons (except for the recall where the filter clearly performs worse than CNN) and the significance might be an effect of sample size.

– The authors claim that "some predictions not consistent with the current definition of SWR may identify different forms of population firing and oscillatory activities associated with sharp-wave", while this is true, it is the fact that by the nature of the LFP and spiking activity, typical noise of the network at low (LFP) and high (spikes) frequencies could be capture in the CNN and misinterpreted as a "relevant event".

– In Figure 5 the authors claim that they find "striking differences in firing rates and timings of SWRs detected at SO, SR and SLM", however, from the example plots in Figure 5H it is clear that except SO, all other strata follow a similar timing, with bot SO and to some extent SLM showing some misalignment in time. How confident are the authors about this variability which turn out to be significant in Figure 5H is not related to the fact that at the two sides of the dipole of the pyramidal cell layer (SO and SLM) more noise can be detected due to larger events fluctuations that not necessarily are ripple events? In other words, the events detected at SO and SLM could contain a higher percentage of false positives? Alternatively, could the variability be related to the occurrence (and detection) of similar events in neighboring spectral bands (i.e., γ events)? The authors should discuss this point in the text.

Overall, I think the method is interesting and could be very useful to detect more nuance within hippocampal LFPs and offer new insights into the underlying mechanisms of hippocampal firing and how they organize in various forms of network events related to memory. Nonetheless, I suggest clarifying the above points for better interpretability as it will also clarify the context of how the method is being validated and where it could be applied in the future.

Reviewer #2 (Recommendations for the authors):

The key points that are required to convincingly support the claims of the paper are:

1. Comparing the CNN to a filter approach that has access to the same number of channels and can also learn the relative weight of each.

2. Showing that the CNN significantly outperforms such a model in detecting SWRs.

3. Convincingly demonstrating that the model can be applied to new datasets with good performance and reasonable overhead.

4. Showing that the CNN can identify real, biologically relevant aspects of SWRs that a filter cannot.
