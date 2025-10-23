# Peer review - Round 1

Editors:
- Alexander Shackman, University of Maryland United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64812.sa0](https://doi.org/10.7554/eLife.64812.sa0)

Hofmann et al., investigate the link between two phenomena, emotional arousal and cortical α activity. Although α activity is tightly linked to the first reports of electric activity in the brain nearly 100 years ago, a comprehensive characterization of this phenomenon is elusive. One of the reasons is that EEG, the major method to investigate electric activity in the human brain, is susceptible to motion artifacts and, thus, mostly used in laboratory settings. Here, the authors combine EEG with virtual reality (VR) to give experimental participants a roller coaster ride with high immersion. The ride, literally, leads to large ups and downs in emotional arousal, which is quantified by the subjects during a later rerun. Several different decoding methods were evaluated, and each showed above-chance levels of performance, substantiating a link between lower levels of parietal/occipital α and subjective arousal in a quasi-naturalistic setting.


---

# Peer review - Round 1

Editors:
- Alexander Shackman, University of Maryland United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64812.sa1](https://doi.org/10.7554/eLife.64812.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Decoding subjective emotional arousal from EEG during an immersive Virtual Reality experience" for consideration by eLife. Your manuscript has been reviewed by 2 peer reviewers, and the evaluation has been overseen by Drs. Shackman (Reviewing Editor) and Baker (Senior Editor). The following individual involved in review of your submission has agreed to reveal their identity: Peter König (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Summary:

Hofmann et al., investigate the link between two phenomena, emotional arousal and cortical α activity. Although α activity is tightly linked to the first reports of electric activity in the brain nearly 100 years ago, a comprehensive characterization of this phenomenon is elusive. One of the reasons is that EEG, the major method to investigate electric activity in the human brain, is susceptible to motion artifacts and, thus, mostly used in laboratory settings. Here, the authors combine EEG with virtual reality (VR) to give experimental participants a roller-coaster ride with high immersion. The ride, literally, leads to large ups and downs in emotional arousal, which is quantified by the subjects during a later rerun. Three different decoding methods were evaluated (Source Power Comodulation, Common Spatial Patterns, and Long Short-Term Memory Recurrent Neural Networks), each of which demonstrated above-chance levels of performance, substantiating a link between lower levels of parietal/occipital α and subjective arousal in a quasi-naturalistic setting.

The reviewers both expressed some enthusiasm for the manuscript:

– The study is timely and makes an important contribution to our understanding of the relation of emotions and sensory processing.

– Of potentially great interest to a broad audience.

– The embedding in historic literature is excellent. I like it a lot.

– This work is notable because the roller-coaster simulation is a well-controlled, yet dynamic manipulation of arousal, and in its comparison of multiple decoding approaches (that can model the dynamics of affective responses). Indeed, this is an interesting proof of concept that shows it is possible to decode affective experience from brain activity measured during immersive virtual reality.

Major revisions:

Nevertheless, both reviewers expressed some significant concerns.

1. The result section is written as if there would be a preceding method section. But there is not. As a consequence, a large part of the results is incomprehensible without scrutinizing the method section further down. I'd suggest integrating about 2-3 pages worth of the total 17 pages method section into the result section proper. For example, you can safely assume that the majority of readers are not familiar with SPoC and CSP, might have heard of LSTM, but do not know the details relevant for the present context. Nonmov and mov conditions, well, might be guessed, but it is better to just state it. Similarly, Space coaster and Andes coaster, yeah, I just assumed that these are two different sections in the lab-amusement park. Still, make a short comment and reduce guessing.

2. Potential perceptual confounds: Decoding the emotional arousal vs. decoding break vs. ride. The emotional arousal drops drastically during the break. Ok, that's the nature of the break. However, the visual input also changes a lot during the break. This raises the possibility that the decoding emotional arousal largely rests on segmenting break vs. non-break periods by differentiating high motion visual input during the ride vs. static stimulation during the break. Figure 2 suggests some power differentiating different levels of emotional arousal within the ride intervals, but it is not really obvious. To address this issue, can you either better document and visualize the data or supply an analysis, not including the break, and just decoding variations of emotional arousal during the ride sections.

3. Temper the framing and claims to better align with the actual data and approach. The authors advocate that naturalistic experiments are needed to study emotional arousal, because "static" manipulations are not well-suited to capture the continuity and dynamics of arousal. This point is well-taken, but no comparisons were made between static and dynamic methods. Thus, although the work succeeds in showing it is possible to use machine learning to decode the subjective experience of arousal during virtual reality, it is not clear what new insights naturalistic manipulations and the machine learning approaches employed have to offer. Here are some suggestions for empirically evaluating the importance of dynamics in characterizing arousal:

a. Compare the effectiveness of the models developed in the present study against more conventional measures of arousal. Does a standard measure of occipital/parietal α predict subjective ratings as well as more complex models?

b. Experimentally compare correlates of arousal in static vs naturalistic manipulations. Do models trained to predict the arousal of participants during VR generalize to standard tasks and vice versa?

c. Investigate the importance of temporal dynamics in modeling arousal. LSTM models can model temporal dynamics through recurrent connections. Does disrupting this aspect of LSTM models reduce performance? Are dynamic models necessary to explain these naturalistic data?

4. The methods used to assess model performance are also a concern. Decoding models were evaluated separately for each subject using 10-fold cross-validation, and inference on performance was made using group-level statistics. Because time-series data are being decoded, if standard cross-validation was performed the results could be overly optimistic. Additionally, hyperparameters were selected to maximize model performance which can also lead to biased estimates. This is particularly problematic because overall decoding performance is not very high. Here are some suggestions for evaluating model performance:

a. Use rolling cross-validation or larger blocks to confirm that autocorrelation in EEG data and arousal ratings does not bias results.

b. Perform inference using block permutation (e.g., by iteratively scrambling consecutive blocks of subjective arousal ratings and refitting models).

c. Use nested cross-validation to optimize hyperparameters to provide a less biased estimate of performance.
