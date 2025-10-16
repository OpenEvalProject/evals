# Peer review - Round 1

Editors:
- Mark Lescroart, University of Nevada at Reno United States

Reviewers:
- Mark Lescroart, University of Nevada at Reno United States
- Alon Hafri, University of Pennsylvania United States

## Review text

DOI: [10.7554/eLife.47686.sa1](https://doi.org/10.7554/eLife.47686.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Many regions in the human brain have been implicated in the representation of observed actions, but the literature on action recognition has focused largely on a few classes of actions. Here, the authors seek to understand the representation of actions by studying how the common underlying aspects of many different actions are reflected in brain responses. Perhaps the best aspect of this paper is the large number of actions used as stimuli. The realistic visual variation in these actions grants the work an important increment in external validity compared to much past work. The authors also cope well with the complexity of their stimuli by considering multiple models of the underlying components (or features) of actions, which capture multiple ways that actions can be similar. These models do not exactly rule out alternative explanations for the results in the paper. Rather, the authors show how different aspects of observed actions (or visual features correlated with actions) are represented in partly overlapping regions of human lateral occipito-temporal cortex. The comparison with the other models makes the finding that semantic aspects of actions best capture responses in a particular parcel of left lateral occipito-temporal cortex interestingly specific and compelling.

Decision letter after peer review:

Thank you for submitting your article "The representational space of observed actions" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Mark Lescroart as the Reviewing Editor, and the evaluation has been overseen by Richard Ivry as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Alon Hafri.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The goal of the present study was to find which areas of the brain contain a representational space that reflects the semantic similarity space of actions. Using a set of photographic images of 28 everyday actions, inverse MDS, and multiple regression RSA of fMRI data, the authors found that semantic similarity ratings were best matched to representations in LOTC and left pIPS, over and above other models related to body parts, objects, movement, and scene contexts. The authors propose that these regions may act as the input for how humans represent the meaning of actions.

This work is significant in that it is the first to show that a punctate and limited set of regions (LOTC and pIPS) may be the substrate for human representation of action meanings from visual content. The broad stimulus set also provides an important generalization and expansion of past work on action representation. Consequently, the reviewers were unanimous in their enthusiasm for the impact and general quality of the study. However, the reviewers also raised concerns that must be addressed before the paper can be accepted.

Major comments:

1) The authors acknowledge some confounds in their experiment: some actions were photographed nearer than others, and some actions included two bodies where most included only one. The reviewers support the inclusion of these stimuli in the interest of broad sampling. However, the authors should create models to assess the severity of these potential confounds. Specifically, the authors should include a one- vs. two-person model and a near vs. far model as sixth and seventh models in the multiple regression RSA analysis.

2) The authors should also consider at least one image-derived model to assure that any differences they measure in the brain are not due to low-level differences between their conditions. The authors should choose a model that provides a better proxy for V1 processing than does the pixel energy model they currently use (e.g. a Gist model, Gabor model, HMax, or the first layer of nearly any convolutional neural network). Use of a better low-level model is necessary both to assess correlations with the other models and to be included in the multiple regression RSA analysis. Particularly if the RDM-RDM correlations are small (see below), there is the potential that only one or two outlying conditions in low-level similarity space could affect the results.

3) The authors should provide more information about the subjects' instructions in their behavioral rating sessions. Specifically, the authors should clarify whether "meaning" was defined for participants, and whether (and which) examples were given. These instructions strongly influence the interpretation of the models used in the study.

4) The authors should indicate whether some or all of the subjects were naive to the purpose of the study. This is necessary because the models of interest are all based on subjective ratings that might be influenced by knowledge of the purpose of the experiment.

5) Probabilistic regions, or at least probabilistic centroids of regions, for hMT+, EBA, and V3A/B should be labeled on the flatmaps. Such labels are available from published atlases and other work and would require no additional data collection. Currently, anatomical details are only reported for maxima of activation in Supplementary file 3. Labels on the flatmaps will make it clearer how the extent of activation in each condition relates to hMT+, EBA, and V3A/B (and by extension, to OPA/TOS). This is important given the extent to which anatomy figures in the Discussion.

6) The authors should report how large the model-RDM-to-brain-RDM correlations are in individual subjects, or at least an average and range of these correlations across subjects. The authors should also include some visualization of the brain-derived RDM(s) for an area or areas of interest to facilitate qualitative comparison with the model RDMs in Figure 2. One of the hazards of RSA is that correlation can be strongly influenced by a few outlying data points, so if a given model only captures one or two cells of the RDM well, small but above-chance correlation values can still result. If the overall correlation between the model RDMs and the brain RDMs is high (say, over 0.4), this is not a concern. However, in many RSA studies, the correlations between model- and brain-derived RDMs is quite low (r < 0.05), which is in the range that a few outlying values could affect results. If this were true here, it would have consequences for the interpretation of the models, so some assurance is necessary that this is not the case.

7) The authors should report the searchlight radius.

8) Instead of correlation distance, the authors should use squared Euclidean distance as their RDM distance metric, as in (Bonner and Epstein, 2018; Khaligh-Razavi and Kriegeskorte, 2014). Since the distances from one brain RDM are modeled as linear combinations of the distances from a set of predictor RDMs, a distance metric that sums linearly is more in line with the modeling assumptions.

9) The reviewers do not object to use of static images. However, the authors should more explicitly justify the use of static images instead of videos, and discuss the consequences of not using moving stimuli. (This topic merits than the one sentence currently present around the third paragraph of the Discussion.)

10) A substantial portion of the Discussion is dedicated to the results in pIPS. This section is fairly long and strays from the data reported in the paper somewhat more than the other sections. Since the analysis is performed at a group level and there are no functional localizers reported, and since the location of OPA in particular can vary across individuals and is not tightly localized to the Temporal Occipital Sulcus (Dilks et al., 2013), it is difficult to say what the relation of the IPS result is as compared to OPA or other regions. This section should be re-written to more clearly indicate which parts are speculative, and potentially reduced in length.

11) Currently, discussion of the relationship between the recovered action similarity space and other work on this topic is confined to a few lines in the Discussion. The authors' point that their space depends on the actions they chose to include is well taken, but nonetheless the authors should discuss whether and how the dimensions of their similarity space relate to other hypotheses about the semantic structure of action representation. Work in language has thought at length on this issue (e.g. Pinker, 1989; Talmy, 1985; Kemmerer).
