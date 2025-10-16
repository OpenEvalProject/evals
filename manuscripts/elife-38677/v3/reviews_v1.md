# Peer review - Round 1

Editors:
- Floris de Lange, Donders Institute for Brain, Cognition and Behaviour Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.38677.025](https://doi.org/10.7554/eLife.38677.025)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Current and future goals are represented in opposite patterns in object-selective cortex" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Floris P de Lange as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Sabine Kastner as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Brad Postle (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

van Loon et al. examine working memory representations of information that is either currently relevant (current) or will be relevant later (prospective). Using fMRI, they find that both types of working memory can be decoded from activity patterns in mid-level visual activity patterns. Strikingly, activity patterns were opposite for these two types of memory, with information that will be needed to accomplish a future goal, but not the most proximal one, represented in a format that is anticorrelated with format in which it will be represented when it is of highest relevance.

All three reviewers were enthusiastic about the aims of the study. There was however considerable debate about whether the results could indeed be interpreted as 'coding prospectively relevant information', or whether they could be equally well represent BOLD undershoot (reviewer 1) or attentional suppression (adaptation) of the unattended working memory (WM) item and/or class (reviewer 3).

Essential revisions:

It will be essential to satisfactorily rule out the alternative interpretations of the data put forward by reviewer 1 (point 1 and 2) and reviewer 3.

Reviewer #1:

van Loon et al. examine working memory representations of information that is either currently relevant (current) or will be relevant later (prospective). Using fMRI, they find that both types of working memory can be decoded from activity patterns in mid-level visual activity patterns. Strikingly, activity patterns were opposite for these two types of memory.

This is an interesting study, on the currently 'hot topic' of where and how visual information is maintained in working memory in the human brain. The paper is well written and coherent, and the analyses are expertly done and clear. I am however worried about some alternative explanations for the results that may ultimately render them rather hard to interpret.

1) Can the results be explained by BOLD undershoot?

During the prospective trials, the participants see an exemplar of the category of interest (e.g., a cow) and the flower, and then they see a cue that tells them to first focus on the flower. The null hypothesis (i.e., no sensory activity pattern for items that only become relevant later) would dictate that activity in the 'cow area' would simply decline, and become active again only during search display 2. Under this null hypothesis, cow voxels would have negative values during search display 1, which would explain why cross-classification results in below-chance performance.

The authors swiftly dismiss this possibility, because, as Figure 2—figure supplement 1 shows, overall BOLD signal in the prospective condition actually goes up. However, what is plotted here is mean BOLD signal of the entire pFS area. Naturally, the flower search display will generate a large BOLD signal (in e.g. flower voxels). I think it is quite plausible that the results are explained by a BOLD undershoot of the relevant voxels, which is masked by a BOLD activation by a concomitant activation of other visually response voxels.

2) Can the results be explained by systematic differences in search display 1 between current and prospective trials?

Another alternative explanation (of which I'm less sure it holds water, but I thought it may be good to mention it anyway) of the anti-decoding during search 1, is that prospective trials are trials in which the search 1 display is always the 'flower search display'. Current trials are trials in which something else than flowers is presented. Is it possible that the below chance decoding means that flowers don't resemble the other categories? In other words, is it possible that below chance decoding has nothing to do with the memorized target, but with the presented search display? (which is systematically different between conditions?)

3) Design choice

The authors designed their task such that one target was 'of interest' (could be of three categories) whereas the other was always exactly the same item (the flower). I am wondering whether this is a good design choice. One of the potential problems of this design choice is already mentioned in point 2. But it seems to create other forms of imbalance. For example, a 'prospective trial' may be more difficult than a 'current' trial. In prospective trials, there is a longer WM load, in current trials there is a reduced WM load (because the flower doesn't really require holding in WM, as behavioral results also show).

I don't really understand what advantage the current design has, over a design in which e.g. two exemplars would be shown from the three categories employed by the authors. This would be a more balanced design, and it would allow the authors to truly compare current vs. prospectively relevant items, in a design in which these trials are of equal difficulty.

Reviewer #2:

"Current and future goals are represented in opposite patterns in object-selective cortex," van Loon, Fahrenfort, Olivers. This manuscript introduces what may well come to be accepted as an important principle in the representational dynamics of information held in versus out of the focus of attention in visual working memory, with information that will be needed to accomplish a future goal, but not the most proximal one, represented in a format that is anticorrelated with format in which it will be represented when it is of highest relevance. The approach taken by the authors represents an important advance, in that it addresses how information is maintained in different states of priority, rather than "just" where. (Questions of 'where' can be interesting, but only if they give insight into/constrain models of mechanism, and this field has matured to the point where questions of 'where in the brain' no longer offer much of an advance.) Overall, the manuscript is very clearly written and argued, and my comments will mostly highlight points where clarity could be improved.

Figure 2A: It appears that, by TR4 following the cue, the prospective category is at baseline – if so, this could be consistent with a stimulus encoding response that then returns to baseline (as opposed to the prospective category being "actively" (my term, but the authors' implication) sustained across the initial delay).

Figure 3B: This is a nice visualization. It could provide more information if the individual exemplars were identified (as, e.g., 1, 2, 3, 4 rather than four undifferentiated green dots). What's not clear to me, however, is whether any quantitative and/or inferential information is conveyed by the lines that cross in the middle of each MDS plot for Search 1 and Search 2.

"Next we wanted to investigate what turns a currently relevant into a prospectively relevant representation." This misrepresents what was accomplished in the analyses that follow, which were more along the lines of 'tracking what transformation a representation undergoes when transitioning from currently to prospectively relevant." Indeed, it is noted in the Discussion that "A crucial question that our data does not answer is what the exact mechanism is behind this transformation."

For the analyses illustrated in Figure 4, more information is needed. First, what condition labels are used for the three sets of t-values in each plot? E.g., for "cow," are the betas from the cow regressor from the GLM used for all three plots (Current Same, Prospective Same, Prospective different)? If this is true, it's not surprising that there's very limited variance across voxels in the latter two conditions. Would the regression be more interesting if it was "fair" to the Different category by using its regressors? Also, how does this analysis reconcile with the idea of an opposite representation? E.g., why isn't the slope of Prospective Same of the same value as Current Same, but opposite in sign? A separate question is how interpretable the classifier weights are. With logistic regression, the importance of any given voxel can vary markedly depending on the level of sparsity that is imposed (i.e., depending on the lambda term in the regression model). Haynes's group has described a way to get unequivocal importance values from SVM, but I'm not familiar with a comparable metric for logistic regression. If such a diagnostic can be extracted from logistic regression it would be of considerable interest, and so should be detailed.

"We found that object category information was stronger for pFs, visual cortex and IPS than for RMF, whereas the impact of relevance (Current vs. Prospective) was apparent in all ROIs throughout the trial." This is an important point, and addresses a question of considerable current theoretical interest (and controversy), and so more information should be included – enough to support critical evaluation of this statement.

Reviewer #3:

van Loon and colleagues present the results of an elegant fMRI study designed to test for representational differences/similarities in coding scheme for items in working memory with different priority status (immediately relevant vs. prospectively relevant). The study is well-conceived, well conducted and well-motivated to tackle an important problem. The analyses are clear and appropriate, however the results are somewhat surprising. The authors report a literal reversal in pattern during search in the irrelevant display. Even more surprising, this occurred in both the first and second search position (i.e., even after the non-relevant item could be forgotten). The authors present these results very clearly, and provide at least two interpretations: top-down control (attention suppression?) or neural adaptation, favouring the latter.

A major question left unresolved is whether this adaptation (or top-down suppression) is item specific or general to the whole class of stimuli (category specific). Obviously this is a trickier analysis, but theoretically tractable and worth reporting whether or not it is possible. The results would be very informative, especially interpreting the effects within a working memory framework.

In general, the authors do a good job handling what feels like unexpected results; however, I think there is room to be a bit more upfront with the initial hypotheses. They are relatively clear that they did not expect a pattern reversal, and especially not during the second search. For clarity, I think it would be worth explicitly stating the initial hypotheses regarding the first delay period (presumably there is a case for qualitative different formats in preparation for search).
