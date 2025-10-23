# Peer review - Round 1

Editors:
- Frances K Skinner, Krembil Research Institute, University Health Network Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.44320.031](https://doi.org/10.7554/eLife.44320.031)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for sending your article entitled "Sub-second dynamics of theta-gamma coupling in Hippocampal CA1" for peer review at eLife. Your article is being evaluated by three peer reviewers, and the evaluation is being overseen by a Reviewing Editor and Laura Colgin as the Senior Editor. A consensus was reached based on the original reviews and subsequent discussions between reviewers and editors.

Given the list of essential revisions, the editors and reviewers invite you to respond within the next two weeks with an action plan and timetable for the completion of the additional work. We plan to share your responses with the reviewers and then issue a binding recommendation. The action plan only needs to address the "Essential Revisions" listed below and should contain a similar level of detail as a traditional rebuttal letter.

Summary:

This manuscript investigates cross-frequency coupling of theta and different gamma bands in rodent CA1 using open access data from CRCNS.org. The authors present a novel method for categorizing individual theta cycles and demonstrate that such a categorization can reveal distinct processing states in the CA1 region of the hippocampus. They use a clustering procedure based on the frequency and phase of gamma activity on individual theta cycles, and they identify four distinct theta states (including two "fast gamma" states) during awake behavior and REM sleep. Analyzing transitions between states along with coherence between regions, they find that the network transitions between states depending on behavior and show that subfield coherence occurs during corresponding states. The authors also assess firing rates and spike field coherence of different cell types during different states, finding that slow gamma states have lower firing overall, less spatial information, and less phase precession. Phase precession was most pronounced during medium and "late fast" gamma states.

Examining relationships between rhythms is notoriously hard to characterize at small timescales, and this method could prove useful for determining possible processing state transitions at the hundreds of milliseconds scale.

Essential revisions:

While all the reviewers found the work interesting, several issues arose regarding method details, application of method, and clarity/analyses of their claims.

Specifically, the authors need to address the following:

i) Are the cycle-by-cycle labels reliable/robust/"real"? In other words, can we confidently speak of individual cycles as being in one of the four categories? OR is this just another way of describing theta-gamma coupling that reveals 4 centers in a continuum of possibilities? If this is another way of finding theta-gamma coupling types, the authors need to highlight how their method adds value to the existing literature.

ii) If a potential user of this data applies k-means to data that they've recorded, e.g., with a single tetrode in the pyramidal layer, can they assume with confidence that they will find the same 4 clusters and be able to label theta-cycles? Or do they need the laminar probes?

iii) More analyses need to be done to support some of their claims. In particular, they should verify that clustering is similar during sleep and wakefulness by attempting to identify clusters during those states in isolation (rather than pooling them together). They will need to do this in order to support their claims about the four distinct states in this region.

iv) A concern was raised that the analysis of place cell activity did not adequately control for the location on the track or the animal's speed (subsection “Spiking during S-gamma has lower spatial information and phase precession”, second paragraph) or other potentially important behavioral factors.

v) There is something a little strange about the consistency of LFP and CSD findings across electrodes (and by extension, layers of the hippocampus) as there should be changes across input and cell body layers. Concerns were raised that the authors are potentially not sampling both input and cell body layers or averaging across electrodes that are not from the same location. This needs to be clarified, tightened up, or claims about consistency across layers need to be removed.

vi) Clarification and justification of their clustering, a cleaned up Figure 2, and an exploration of other measures of coherence which are insensitive to power effects are needed.

vii) Particularly given the fact that they've used open data, it would be appropriate for the authors to share their code.

viii) The authors do a good job cataloging how many animals/sessions are used for different comparisons, but it would have been very valuable to really understand how one animal's data differed from another. Authors, for instance, could classify theta cycles using the cluster centers from other animals and compare cluster assignments with what happens when the same animal is used for clustering. Related to this, was any cross-validation done?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Sub-second dynamics of theta-gamma coupling in Hippocampal CA1" for further consideration at eLife. Your revised article has been favorably evaluated by Laura Colgin as the Senior Editor, a Reviewing Editor, and three reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed and clarified before acceptance, as detailed below.

Overall, the main concern regards whether the new analyses have been properly cross-validated.

Questions arising regarding novelty and/or robustness of results.

1) “They use community clustering and then switch to k-means clustering.” The reasons for this revolve around robustness to electrode location, but in their revised manuscript, they emphasize the use of the pyramidal layer LFP for analysis. Thus, it seems that the community clustering is superfluous and could be pushed to a comment and/or supplementary figure.

2) “They claim that there are four clusters, but it is unclear to what extent these lie on a continuum or are very distinct.” The authors in response compare model likelihoods for 1 and 4 component models, but they don't carefully describe this in the Materials and methods. Thus, a critical question is whether they have properly cross-validated this result. If they have, this is a valid result. Additionally, they compared inter- and intra-cluster distances, and referred to the "maximum inter-cluster correlation" without defining it. Is it simply the smallest of the largest correlation with any other cluster for that data point? Or somehow for all data points? Furthermore, it is also critical that this analysis be done with cross-validation (i.e., assessing theta-cycles not used to define the model parameters), but this is not specified in the Materials and methods.

3) “They did not assess whether the resulting spectro-temporal descriptions of theta-gamma states were robust across animals.” The authors in response have compared across animals and find that the slow gamma state is quite robust, but the others are not. This reviewer hypothesizes that this may be because the theta oscillation is not consistently phased across different electrodes. If a single theta was used across shanks, would the states be more similar? Additionally, why not just add a tetrode data set from CRCNS to their analysis to ensure that the result is not recording-style dependent?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Sub-second dynamics of theta-gamma coupling in Hippocampal CA1" for further consideration at eLife. Your revised article has been favorably evaluated by Laura Colgin as the Senior Editor, Frances Skinner as the Reviewing Editor, and additional reviewer Caleb Kemere, who has chosen to reveal his identity.

The manuscript has been improved and will likely be accepted once the remaining issues outlined below are addressed.

1) A question is whether theta phase estimation is less accurate for different gamma bands. If it was, then the quality of the individual cycle estimates might be different, which might affect clustering. The point about medium and fast gamma bands overlapping for certain electrode depths raised this question in a reviewer's mind. If theta power was equivalent across states, then it would suggest that it was equally easy to estimate theta phase, but I suspect that theta power may be different.

Unless the authors have ideas of how to assess the quality of theta phase estimation, the authors are requested to point out in the Discussion that their results depend on accurate theta phase estimates. (I think it may just be the two faster gamma bands.).

The authors should also tone down their claims of four (vs. three) a bit.

Further, the paper emphasizes that it is the first to identify 4 TG states. Authors should at least make sure to also mention that Lopes-dos-Santos et al. reports the potential for 4 TG states and tone down their assertions in this regard.

2) One thing that probably needs to be removed is the 1 vs. 4 Gaussians test. It turns out that for unsupervised learning (which K-means is an example of, but also probabilistic latent-variable models), the log-likelihood, even with cross-validation, does not always reflect the best model in model-selection questions. In particular, it will favor models with more components. The reviewer struggled to find a good reference for the authors on this question – both Machine Learning, A Probabilistic Perspective by Murphy, and The Elements of Statistical Learning by Hastie, Tibshirani, and Friedman mention it in passing but don't give much detail. Unfortunately, however, it means that the approach the authors take is not guaranteed to work (particularly, as is described in Murphy, when the underlying data are not actually Gaussian).

3) Several times, the authors assert that they are the first to analyze TG states on a cycle by cycle basis. I believe that Dvorak et al., 2018 do this, as well as Zheng et al., 2016. The authors should definitely at least discuss the Dvorak paper and tone down their assertions in this regard.

4) The authors find that TG states are not affected by novelty. This seems to contradict the findings of Kemere, Carr, Karlsson, and Frank, 2013, and this should be discussed.

5) The authors continue to use the phrase "gravity center". I believe this concept is nearly universally referred to as "center of gravity".

6) In the first paragraph of the subsection “Changes in CA1 PPC with CA3 and EC during different theta-gamma states”, it says "we next coupling". Something is missing.

7) In the second paragraph of the subsection “Spiking during S-gamma has lower spatial information and phase precession”, it says that there was "no spatial preference" of TG states. If there is a speed preference, and a difference in speed across the track (as there must be), how is this possible?

8) The use of Morlet rather than (the better) Morse wavelets may result in suboptimal frequency/phase estimates. The authors should be aware of this.
