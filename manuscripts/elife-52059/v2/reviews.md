# Peer review - Round 1

Editors:
- Dorothea Hämmerer, University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.52059.sa1](https://doi.org/10.7554/eLife.52059.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper presents a rich study investigating Locus Coeruleus (LC) function with a variety of MR and physiological measures. The study of LC function has recently gained more interest due to the LCs early decline in dementia. The authors show that structural and functional measures of the LC can be used to gain insight in its role in memory encoding and retrieval as well as related physiological processes.

Decision letter after peer review:

Thank you for submitting your article "Dynamic behavior of the locus coeruleus during arousal-related memory processing: a multi-modal 7T fMRI study" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Timothy Behrens as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Mara Mather (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper reports on an impressive study which presents the state of the art in the type and quality of measures needed for investigating Locus Coeruleus (LC) function, also including MR measures developed by the authors themselves. A shortcoming of the paper is that the analysis methods used are not always sufficiently documented to enable an assessment of their precision, usefulness and validity. Especially with a structure so rarely investigated in fMRI, a study with such a nice state-of-the-art set-up should help us understand what aspects of the LC are possible to investigate with fMRI and which aren't. In this light, I would also think that already a convincing report on basic task-related fMRI responses in the LC can present a sufficient scientific advance. More advanced additional analyses might not be needed if their physiological plausibility proves unsatisfying.

Essential revisions:

Specifically, the following revision requirements are suggested, also based on the comments by the external reviewers:

Introduction:

1) The authors should be clearer in the Introduction as to how LC/NE effects might differ between different stages of memory processing.

Behavioral analyses on memory measures:

2) The bias measure hasn't been sufficiently described to be understandable. Also given difficulties in the task design for the name recognition memory part, it is suggested to just focus on Hits-FAs of the emotional face recognition task (not the name recognition task).

Preprocessing of fMRI data:

3) The authors mention comparing different preprocessing pipelines but (to my knowledge) don't show statistics on how these result in differences in the GLM results or SNR measures in their regions of interest. These should be added and are in particular critical as the authors chose to proceed with a denoising approach that does not include respiration and pulse regressors (maybe outline to what extent these might be captured even without explicit regressors in the chosen ICA denoising approach).

4) Precision in the spatial coregistration/normalisation is paramount for group analyses on such a small structure. The authors should provide supplementary information that allows to evaluate the precision of the spatial transformations for every individual fMRI dataset.

Physiological/functional measures:

5) it isn't clear why a relationship between a change in sAA across subtasks and task-specific measures of rMSSD is more relevant than a relationship between task-specific sAA levels and rMSSD measures.

6) the significance of the coherence analyses linking LC BOLD variability and HRV/sAA are unclear (what does a higher coherence between HRV and BOLD variability mean? Why does this have to be related to a change in sAA?). Please only leave this in /a subset of analyses in) if the analyses can be reasonably physiologically motivated. Also, for these analyses, exclusively pulse-corrected fMRI data should be used.

7) Please scrutinize the GLM results for circularity in the ROI selection.

8) It is not clear what variability in the coherence measures between e.g. LC and MTL indicates functionally. It might be cautioned against interpreting these for areas/task conditions where the task-related GLMs did not show significant activations?

Discussion:

9) The Discussion should be scrutinized for claims that exceed the physiological significance of the results.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Dynamic behavior of the locus coeruleus during arousal-related memory processing in a multi-modal 7T fMRI paradigm" for further consideration by eLife. Your revised article has been evaluated by Timothy Behrens (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

We thank the authors for their work in revising this manuscript which has clarified several issues. There are still some concerns with the paper which we ask the authors to address:

1) As a general rule, we would like to ask the authors to go through the methods again and make sure that all analyses can be retraced by the reader. This concerns in particular the behavioral analyses. It is still not clear how the bias memory score was calculated. Please indicate which data were used for this (Hits-FAs of names related to which faces, old or new?) and give the precise formulas of all the calculations applied to these data.

2) Related to this, to add a more accessible measure of emotional memory effects (of names associated with faces), please add a table giving Hits, FAs, and Hits-FAs for names separately for old emotional and old neutral faces and separately for new emotional and new neutral new faces (incorrectly indicated as old (FA)), as well as statistics on the difference in Hit-FAs measures for names only on correct as old identified emotional versus neutral faces.

3) We ask the authors to consider limiting the analyses exploring links between LC resting state variability and (indirect) physiological indicators of NA (sAA and HRV) to correlations across task stages and analyses with HRF-convolved low and high HRV events, which are very interesting. By contrast, the coherence analyses in particular frequencies of resting state fMRI data with HRV seem not well motivated by the cited literature (which physiological processes do these high-frequency-specific fMRI data likely represent?). Alternatively, to taking these results out, the authors can revise their motivation for these analyses and make the interpretation of the results clearer. The reviewers found these hard to understand in an already complicated paper.

4) The significance of the exploratory coherence analyses, which report changes in the variability in coherence as their outcome measure seems to be also less clear in its physiological meaning (which processes that we can measure in fMRI are changing in coherence here and why should this be related to sAA?). Again, we invite the authors to remove these analyses. However, If the authors feel that this is adding valuable information, they are invited to leave these analyses in and make the interpretation of the results more accessible to the reader.

5) The results from the analyses on changes in coherence across task stages are not yet clear. I am wondering whether such analyses are prone to spurious results: if HIP-AMY coherence is higher in consolidation > baseline and in baseline > encoding, shouldn't it also be higher in consolidation > encoding? What does it mean if this effect is not picked up by the analyses? If the authors have easy access to the data, they may consider adding an analysis in a control area that shouldn't be implemented in consolidation or retrieval to provide cut-offs for avoiding spurious results or suggest alternative approaches to control for spurious results. Again, however, an alternative is to discuss this issue.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Dynamic behavior of the locus coeruleus during arousal-related memory processing in a multi-modal 7T fMRI paradigm" for further consideration by eLife. Your revised article has been evaluated by Timothy Behrens (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

We thank the authors for implementing most of the requested changes. However, in their responses to Comment 1 and 2, they misunderstood or overlooked important aspects of the question. We would like to ask them to adjust their responses and changes in the paper as follows:

Re Comment 1: Please also indicate whether the names used for the calculation of the bias score were paired with new or old faces or whether this was collapsed across both old and new faces.

Re Comment 2: There was a misunderstanding in the response to comment 2. The statistics required in the table were the hit and false alarm rate for names, not for faces. Please report the Hit rate, FA rate and Hit-FA rate separately for the names paired in the memory tests with old emotional and old neutral faces and for those paired with new emotional and new neutral new faces.
