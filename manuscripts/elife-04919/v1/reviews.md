# Peer review - Round 1

Editors:
- Howard Eichenbaum, Boston University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.04919.015](https://doi.org/10.7554/eLife.04919.015)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Temporal structure in the retrieval of associations” for consideration at eLife. Your article has been favorably evaluated by a Senior editor, a Reviewing editor, and 3 reviewers.

The following individuals responsible for the peer review of your submission have agreed to reveal their identity: Howard Eichenbaum (Reviewing editor), Nikolaus Kriegeskorte (peer reviewer), and Kenneth Norman (peer reviewer). A further reviewer remains anonymous.

The Reviewing editor and the reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

The reviewers were consensual in their enthusiasm for the question under study and for the sophisticated design and analyses, for the novel findings on temporal dynamics of memory reactivation, and the inclusion of negative findings. There were, however, major concerns about the strength of some of the findings, and there were other specific concerns by individual reviewers about some of the statistical tests, the exposition, and the interpretation of specific findings. These concerns are provided below.

Reviewer 1:

Reinstatement is only significant at the level of category-average representations, not individual exemplars of each face, body, and scene. This is a pity because each category was equally often associated with positive and neutral reward. This makes it difficult to assess whether the specific reward-predictive stimuli were reinstated at the point of reward and whether the strength of such reinstatement predicted the propagation of value updates. The authors speculate that category-level reinstatement might explain the absence of significant value updating suggested by their behavioural post-test. They do show that stronger reinstatement of the early component of the category representation just before reward onset predicts subjects' value-based choices in the behavioural post-test. However, although reasonably corrected for multiple testing across latencies, this effect is barely significant and is one of several analyses attempting to establish a relationship between reinstatement of reward-predictive stimuli and value updating. [Reviewing editor: This comment clarifies the reviewers' concern about this issue, but it may not be possible to improve on the comments provided by the authors in the discussion of their findings.]

Reviewer 2:

1) The Introduction does a nice job of identifying a gap in the literature, though I believe it overstates this gap in some ways. I would suggest additional discussion of the findings of Manning et al. (2011; 2013, Journal of Neuroscience), which identify the spatial and spectral signatures of reinstatement. Perhaps the authors could emphasize the temporal aspects of associative retrieval more thoroughly in this section.

2) The authors should more clearly identify the cognitive constructs they are assessing. Throughout the manuscript, the authors seem to alternate between focusing on a paradigm designed for associative retrieval, sensory preconditioning, and value updating. Given that the task design allows for investigating each of these, the authors should state this upfront and additionally discuss the prior literature linking these constructs in the Introduction.

3) The rationale for using univariate vs. multivariate feature sets should be stated earlier in the text. Is the rationale only to verify that more information is captured using multivariate techniques compared to univariate techniques? If so, I think simply citing the prior literature demonstrating this should be sufficient and it is unnecessary and a bit tangential to focus on this point as a primary finding. As the text stands now, it takes a while to get to the point of the primary research findings.

4) Pattern classification performance was calculated within subject and then averaged across subjects, revealing peaks around 200ms and 400ms. To what extent are these peaks evident in individual subjects? The authors partially raise this issue themselves in the Discussion section, but may wish to provide quantitative results regarding this issue.

5) Although the data generally supports the claim that they are primarily measuring “evoked” activity, the authors should be cautious to not imply that it is only evoked activity.

6) In the Discussion section: Several EEG and fMRI studies of temporal order memory (some using an RSA approach) are excluded but should be cited and/or discussed (Hsieh, 2011, Journal of Neuroscience; Hsieh et al., 2014, Neuron; Ezzyat and Davachi, 2014, Neuron).

7) Overall, the data support the claim of two temporally distinct representational periods. However, such an interpretation is complicated by a highly significant (double the chance rate) classification performance during the two windows. The authors should discuss this more thoroughly. Additional analyses described above may also clarify this interpretational discrepancy.

Reviewer 3:

1) What kinds of multiple comparisons corrections are the authors using for the analyses shown in Figure 4A and 4B? Elsewhere in the paper, the investigators appear to be using an approach of controlling for familywise error at p < .05, but it is not clear what is going on here (the paper only says p = 0.05 “peak-level significance thresholds”). Whatever correction the authors use will need to correct for the use of classifiers trained on different time points and also their exploration of multiple time points during the reward learning phase. For what it's worth, I thought that the approach taken in Figure 6 (controlling for all time points, but only two classifiers: the 200ms-trained classifier and the 400ms-trained classifier) was acceptable; a similar approach could be applied here, if it isn't being used already.

2) For the RSA analysis, it was not clear if the authors obtained a meaningful measure of “self-similarity” values (i.e., how similar is the pattern for a particular item to the pattern evoked by other instances of that same item). If they did not measure this, it would be useful to re-do the analysis in a way that obtains self-similarity measurements. Having this information would allow the authors to get separate readouts of item-specific information (e.g., by contrasting the diagonal cells to the off-diagonal cells from the same category) and category information. In particular, it would be useful to get these measures (along with some statistical assessment of their reliability, e.g., through bootstrapping) for both the 200ms and 400ms time points. While it is clear that category structure is not strongly represented at the 200ms time point, the RSA analysis in its current form does not speak to how strongly item-specific information is represented at the two time points (the text, as it is currently written, seems to be implying that there is less information about individual items at 400ms than 200ms, but we don't know that).

3) As shown in Figure 1, about half of the participants showed P(Si+) that was below .5, and some of these participants showed P(Si+) values that were well below .5. While I can understand how variance in the level of reactivation (during the reward learning phase) could lead to variance in participants' preference, ranging from no preference to strong preference in favor of the associated item, but it is not clear how variance in reactivation could lead to the opposite preference. The only other interpretation of the below-chance performance is that it is noise, but in that case, how can it be explained using classifier evidence? It would be useful if the authors commented on this.

4) A suggestion: to the extent that classification performance is suffering due to a lack of training data, we have sometimes found in my lab that we can improve classification by using a “leave one subject out” approach (i.e., train on all but one subject, test on the left-out subject). This approach assumes that brain patterns are relatively consistent across participants. If that assumption is generally true, then the 25-fold increase in the number of training patterns can improve classification accuracy by a substantial margin (conversely: if there is extensive between-subject variability in the patterns, then moving to a leave-one-subject out approach can hurt classification accuracy). Anything that improves classification accuracy has the potential to greatly boost the interpretability of these results.
