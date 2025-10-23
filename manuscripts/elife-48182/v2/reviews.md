# Peer review - Round 1

Editors:
- Huan Luo, Peking University China

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.48182.026](https://doi.org/10.7554/eLife.48182.026)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "A neural mechanism for contextualizing fragmented inputs during naturalistic vision" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Joshua Gold as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

This work combined fMRI, EEG and deep neural network model to investigate the neural basis of encoding of fragment location information (e.g., vertical, horizontal positions) across different scene categories. It addresses an important question about how the 'abstract' spatial layout that is not explicitly presented in the stimulus itself is represented in neural activities. The paper is clearly written and the approach and results are interesting and novel. However, there are some major issues brought up by the reviewers that need the authors to address and do additional analysis.

For a revision to be successful, you must address the following major issues:

Essential revisions:

1) The thirty-six figure segments come from only six natural images (3 indoor and 3 outdoor), which means the figure fragments would be repeatedly presented and be learned or memorized gradually. It is therefore hard to distinguish two interpretations – do the results reflect a true representation of spatial layout knowledge that would be automatically formed and could generalize to any natural images or do they derive from a learning and familiarization process after repeated exposure? A possible way to assess this is to divide the data into various stages and compare the early- and late-stage results. If the spatial layout knowledge is automatically represented regardless of learning, we would expect to see the same results in the early part. On the other hand, if it is indeed learning or memory process that induces the results, we would expect to see the pattern only in the late part but not in the early part.

2) Each scene picture was split into two halves horizontally and three parts vertically. Thus, there are confounding factors with regards to why the effect only occurred for vertical locations but not for horizontal locations. The authors should either collect new data or perform new analysis to address the issue.

3) The authors used DNN regression to confirm that the vertical position effect is not due to category-related information. However, the involvement of low-level features in discriminating vertical locations is still quite possible and could not be completely ruled out from the current analysis. For example, image segments at different vertical locations of natural scenes (upper, middle, lower) seem to be also associated with different low-level features (e.g., low spatial frequency for upper part, such as sky or ceiling, etc.). The authors could add additional analysis to clarify the confounds, for example, by creating a low-level dissimilarity design matrix, which would then predict involvement of V1 for the low-level features but not for vertical location, while the reverse for OPA.

4) It is hard to understand what exactly DNN features were removed. ResNet50 and AlexNet were used widely but these DNN models were trained by a very large set of images, whereas the present study only compares 6 specific images. The specific features to differentiate the 6 specific images may not be the same as the removed DNN features. The authors could show reconstructed images with DNN features removed and it is quite possible that human observes would still differentiate the 6 reconstructed images even when the DNN features are removed.

5) It is difficult to figure out what the authors were arguing was the mechanism or the consequence: Does knowledge/schema help sort incomplete information, or does the brain sort incomplete information so that we can extract knowledge? The paper is motivated by the former ("…the brain uses prior knowledge about where information typically appears in a scene to meaningfully sort incoming information") but then ends by stating the latter ("This mechanism empowers the visual brain to efficiently extract meaning from dynamic real-world environments, where it is confronted with sequences of incomplete visual snapshots"). Please add clarifications.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A neural mechanism for contextualizing fragmented inputs during naturalistic vision" for further consideration at eLife.

The manuscript has been improved but there was still one issue that was misunderstood or not clearly addressed.

In the original third comment, the reviewer pointed out that the DNN regression analysis cannot convincingly rule out the involvement of low-level properties in vertical position effect and suggested to directly test the DNN features in V1 ("The authors could add additional analysis to clarify the confounds, for example, by creating a low-level dissimilarity design matrix, which would then predict involvement of V1 for the low-level features but not for vertical location, while the reverse for OPA."). The authors have performed additional analysis by using 3 low-level control models, but again just examined whether the vertical position effect existed after regression using these models. The results indeed are not quite convincing and it seems that the regression even could not disrupt category representations as the previous DNN model showed. To explicitly address the concern, as the reviewer originally suggested, the authors should perform a new analysis to show that the DNN model does account for low-level property representation in V1, which would then support the claim that DNN regression could remove the low-level features.
