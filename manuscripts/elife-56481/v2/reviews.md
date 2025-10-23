# Peer review - Round 1

Editors:
- Barbara G Shinn-Cunningham, Carnegie Mellon University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.56481.sa1](https://doi.org/10.7554/eLife.56481.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper aims to assess how well attention to a speaker can be decoded from EEG using convolutional neural networks (CNNs). In particular, the authors train a CNN on EEG data from a "cocktail party" attention experiment and demonstrate impressive decoding performance, better than many prior related efforts. Though effects of eye gaze cannot be completely ruled out, the authors acknowledge this potential confound and do a diligent job of addressing this concern. These provocative results are likely to impact future research in the use of EEG to decode the focus of attention in auditory tasks.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "EEG-based detection of the attended speaker and the locus of auditory attention with convolutional neural networks" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Barbara G Shinn-Cunningham as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Andrew Dimitrijevic (Reviewer #2).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

All of the reviewers felt that the work has the potential to appear in eLife. However, there were substantial concerns about some of the technical details. Without some significant additional work to address potential limitations of the findings and confounds of the experiments that were conducted, we felt the manuscript was not ready for publication in eLife. The standard for asking for a revision (rather than a rejection) for eLife is that if any additional work is likely to take two months or more. Given this, we must reject the manuscript: we believe that the additional work required will take more than two months.

Reviewer #1:

This is an interesting paper that addresses a very timely and interesting question. Given the attention (pun intended) to real-time decoding of attention in the field today, the approach described is likely to be influential.

However, as written, I am not sure how general the findings are, based on the experiments described. Reviewer 3 does an excellent job of articulating the concerns I had, as well, so I am not reiterating them here. With additional controls that demonstrate the robustness of the findings, this work will be of high impact.

Overall, the paper is very clearly written. However, there are a few phrasings that are grammatically proper, but that sound awkward to a native English speaker's ear. (For instance, "Especially the elderly and people suffering from hearing loss have difficulties attending to one person in a noisy environment." is more natural when written as "Both the elderly and people suffering from hearing loss have particular difficulty attending to one person in a noisy environment." ) If the paper were being revised at this point, I would offer a more complete list of such sentences and suggested edits-- but don't believe it makes sense to do so at this juncture.

Reviewer #2:

The manuscript "EEG-based detection of the attended speaker and the locus of auditory attention with convolutional neural networks" describes a study where the authors used a convolutional neural network (CNN) to identify auditory attend locations while the EEG was recorded. The data indicated that CNNs can classify attend locations and accuracy and speed of detection increases when the stimulus envelope is included in the CNN.

As written, the manuscript may appeal to engineering or computer science audiences, however, I feel that more needs to be incorporated to appeal to a broader scope/readership of eLife. Although this may deter from the practical or real-world application of the CNN, including and relating more physiological/neuroscience aspects of the CNN may make the manuscript more palatable to a general audience. It may also demonstrate that this technique can also be used to inform how the brain operates. Two current theories relating to auditory selective attention, as the authors mention, is enhancement of envelope encoding schemes and α lateralization. What features is the CNN using? The use of filtered EEG (low frequency for envelope and band-pass 8-12 Hz, for α) may provide some indication. Some detail on the inferred neural generators, perhaps a topography of the feature weights (similar to de Taillez) would be informative. Also, more detail on the filters used for the spatial-temporal feature map would be helpful. The authors may also consider using a "control" condition to estimate false positive rates. This might be implemented as random EEG shuffling (left and right) for the final testing phase, which would have an accuracy of 50%. Some discussion on the behavioral aspect of the subject performance would also be desirable. Where there content questions about the attend speakers, did the subjects indeed listen to the appropriate target? In cases where CNN performance was not 100% was the subject "peaking a listen" to the other side?

Overall, the CCN is a novel application in this domain and determining attend location within 1-2 sec is a remarkable feat.

Reviewer #3:

This is a very nice study, and well written. The applications are very relevant, and the work is timely. However, I have a number of concerns which need to be addressed before I can believe these very impressive results.

The classification performance for the CNN:D model is very high, with accuracy using 1 second of data almost as high as that at 10 seconds. One potential downfall of CNNs (and DNNs in general) is that they might be hyper-sensitive to the particular EEG setup that they're trained on. I.e., if you tested the same subject on another day, would the performance be the same? Or are they learning to optimize performance with a particular setup of electrode locations and noise conditions? I understand that the data set was collected a few years ago, but is it possible to run the experiment again on a small subset of subjects, and use the CNN that was trained on the previous experiment to classify the data from the new experiment? This would address the concern of the CNN overfitting to the precise experimental setup of the day.

The benefit of the linear stimulus reconstruction approach is that we know how it works, and it can generalize to unseen speakers. The authors state that they tried training a DNN to perform stimulus reconstruction, but its performance was not as impressive as the CNN:S+D approach. However, the CNN:S+D specifically requires a binary decision between 2 speakers. Is it possible that the network is over-fitting to the specific speakers in the training set? If 2 new speakers were introduced, could it handle that? Is it possible for the authors to test this with the current data-set? If not, an additional experiment would be required.

In addition, the linear stimulus reconstruction approach allows for a generic subject-independent model that can decode the attention of an unseen subject. The authors do show results from a generic CNN, but this was trained on all subjects. Can the authors perform an additional analysis using a generic decoder but ensure that the test subject has been completely unseen by the network?

On a similar note, the training, cross-validation, and test data were all obtained from the same trials. I.e., in a single 6 minute trial, the first part was chosen as the training set, followed by cross-validation and test sets. This could lead to overly optimistic results. Can the authors perform an additional analysis where the training, validation, and test sets are all taken from different trials?

Can the authors provide any insight into what the network is learning, and how it can perform so well? As the authors mention in the introduction, perhaps it is α power. They could test this hypothesis by providing the CNN with different frequency bands of the neural data.

In summary, I would require to see a lot more proof that the CNN is not just overfitting to the particular subject, EEG setup, and day of recording, and that these results are generalizable.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "EEG-based detection of the locus of auditory attention with convolutional neural networks" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Barbara Shinn-Cunningham as the Senior and Reviewing Editor. The following individuals involved in review of your submission have agreed to reveal their identity: James O'Sullivan (Reviewer #1); Andrew Dimitrijevic (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

This manuscript presents research aimed at assessing how well attention to a speaker can be decoded from EEG using convolutional neural networks. In particular, the authors train a convolutional neural network directly on EEG data during a "cocktail party" attention experiment and compare it to an approach based on based on reconstructing an estimate of the speech envelope from the EEG using linear regression. The authors demonstrate decoding performance n with accuracies of ~80% using just 1-2 s of data, which is much better than the state of the art.

The reviewers all believe that this work may be appropriate for a Tools and Methods paper in eLife. However, there remain a few critical questions and concerns that need to be addressed for the paper to make its contribution to the field clear.

There are some potential strengths of this technical report comparing the CNNs and linear models for decoding auditory spatial attention using EEG. This research opens new avenues of exploration of auditory attention methods that can be used for real-time decoding applications such as neurally steered hearing aids. The authors claim that it is possible to decode the locus of attention with accuracies of ~80% using just 1-2 s of data is much better than the state of the art.

Because we could not obtain assessments from all of the original reviewers, one of the reviewers is new to the paper. This reviewer read the paper and wrote their own comments before going back and looking at the earlier reviews. They noted that some of the points that concerned them had been raised before. Still, the reviewers who saw your earlier submission do appreciate the changes you made.

Revisions for this paper:

The remaining critical issues that must be addressed for the paper to be published are:

1. Comparing current results to those obtained using envelope reconstruction is useful, but it is somewhat unfair. That is something that you should acknowledge. Specifically, the envelope reconstruction approach is not just a linear approach, it is a linear approach that is constrained to relating EEG responses to the envelopes of the two speech streams. No such constraint is placed on the CNN; it trains on the EEG and settles on whatever features are best for solving the question. Related to this, even the EEG preprocessing (filtering) is different for the CNN and the envelope reconstruction approaches. While this makes sense (the filters chosen for the envelope reconstruction seemed reasonable based on the literature), it also means that the information in the EEG differs in the two analyses. These issues should be acknowledged.

2. Some explanations of what features drive the CNN performance would greatly increase the impact of the paper. As a Tools and Methods paper, there are not significant expectations for demonstration of important neuroscience findings. Still, without some information about what is happening in the neural responses, readers cannot judge the likely usefulness and replicability of this "tool." Is there any way to know this? For example, some of the cited literature (e.g., Bednar; Wostmann) show that α power is important for decoding spatial attention. Α frequencies are included in your CNN analysis and might be responsible for the results you describe. You could check this by seeing how the CNN performance drops if you exclude α frequencies, for instance.

Relatedly, it is almost worrying how good the performance gets when you train on the other examples from the same story and speaker (Figure 5). Why would this be? Is the CNN picking up on some weird features in the EEG that are very specific to these speakers? Without having a sense of what drives the exceptional performance, it makes one wonder what the CNN relies on.

3. The results presented in the manuscript show no effect of window size on performance. This must, in the limit, not be true. More data must be shown to show this dependence and determine the limits of the method.

4. For 3 subjects, with a 10s window, the performance of the CNN was lower than the linear model (Figure 2). How is it possible then, that every subject had a better MESD when using the CNN (Figure 3)? I know you've excluded 1 subject from the figure, but what about the other 2 subjects?

5. You talk about the idea that future work can address some unanswered questions, like whether or not performance will drop with fewer EEG channels. However, related to the idea that the results might be driven be decoding of spatial attention, it would be interesting to know if spatial patterns are driving the CNN decoding.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your article "EEG-based detection of the locus of auditory attention with convolutional neural networks" for consideration by eLife. Your revised article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Barbara Shinn-Cunningham as the Senior and Reviewing Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Andrew Dimitrijevic (Reviewer #2); Behtash Babadi (Reviewer #4).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary

This is a very interesting and provocative paper, which demonstrates decoding from EEG of the directional focus of auditory attention in a dichotic or HTRF-emulated competing-speaker setting. Using a CNN-based decoder to jointly extract the relevant features and classify the locus of attention, you show significant decoding improvements compared to the common linear decoding techniques; moreover, the decoding is rapid, and is thus able to track attentional switches. Analyses implicate the β band as well as frontal EEG channels in decoding. The paper is well-written and clear, the methods are described carefully and transparently, the results are impressive, and the discussion is thorough and inspiring. Your cross-validation scheme for training the CNN to avoid overfitting is admirable; this is very often overlooked.

In addition, we would like to note how thoughtfully you revised your original submission. Two of the three original reviewers read this revision, along with one new reviewer. It was clear to all that your revision and your reply to the previous criticisms were responsive and thorough. We want to thank and commend you for the work you put in on this revision. That said, the revision raised a new concern, discussed below.

Essential revision

1. The reviewers are not convinced that eye movements are not a substantial contributor to decoding accuracy. Specifically, the frontal topography of the convolution filters in Figure 6 looks suspiciously like an EOG signature. We think it is critical for you to clarify what features of the EEG are being used for classification. One way to test this would be look at the raw data (attend left vs right) and look the time-frequency profile.

1a. Saccade-related ERP profiles tend to have a positive peak near 0 ms followed by a negative peak around 20 ms. The attention-related ERPs using EEG, however, have key peaks at in the 100-200 ms range. Given this, the temporal profile of the filters may inform the arguments for and against eye movements contributing.

1b. Relatedly, if you found that the filters were tuned to γ band activity, this would suggest that small saccades are influencing performance. The fact that the network weights the β band as much as it does suggests that it may even like γ band more. On the other hand, if the filters are tuned to α or high δ, that would argue against saccades being the cause.

1c. Your MWF algorithm should remove large gaze artifacts. However, even very small (but consistent) gaze changes could be responsible for some of the effects you see. You should also consider the literature on micro saccades and γ, and about whether small but consistent drifts of gaze during long trials contribute.

1d. We are aware of your recent arXiv paper (Geirnaert et al) in which the CNN fails on another data set. Were subjects asked to fixate in that study, but not this? A better description of how subjects were instructed in the current study should be included, no matter what. Given the Geirnaert results, we think it is especially critical to figure out whether the results in the current paper really are attention effects in neural responses, rather than due to eye movement. It would be unfortunate to have to publish a correction if the results in the current study are attributed to attentional effects when they are actually due to gaze differences.

Given these issues, we would like you to undertake some of the above analyses to address the concerns, and consider in the Discussion the evidence for and against eye gaze contributing to the exceptional performance of your algorithm.
