# Peer review - Round 1

Editors:
- Timothy Verstynen, Carnegie Mellon University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.36395.019](https://doi.org/10.7554/eLife.36395.019)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Model-based fMRI reveals dissimilarity processes underlying base rate neglect" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Timothy Verstynen as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Michael Frank as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Carol Seger (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The reviewers all agreed that this was an important and creative study. The use of MVPA to test explicit psychological models of a cognitive phenomenon was innovative. However, all of the reviewers found the presentation of the theoretical and methodological aspects of the study to be opaque. This resulted in substantial difficulty in being able to accurately judge whether the key findings were veridical or not (or in some cases what the key findings are). Given the overall positive opinion on the scope and aims of the study, the article will require substantial revisions in order to be able to adequately evaluate the conclusions and interpretations put forth.

Below is a consolidated review of the comments from all reviewers. The major points are organized by topic.

Essential revisions:

1) Inferential concerns:

The authors are often imprecise when writing about the cognitive functions that might underlie the differences in neural activation in the MVPA analyses. They often refer to the subjects "thinking about" the common or rare category, but this is unclear. The subjects could consciously be thinking about the category. The representations could be activated implicitly, and indirectly and unconsciously bias the subjects' responses. The subjects could simply be paying more attention to the certain features, and this attention could precede (attending to a feature associated with a rare disease could bias the decision) or even follow the decision (deciding it is the rare disease heightens attention to features of the rare disease). The authors do briefly discuss alternatives in the Discussion section, but a more systematic analysis of the different options and which are ruled out by the present results versus which are still open questions would be helpful.

2) Ambiguity in the MVPA models:

What parameters from the dissGCM model were used?

It is unclear how the pattern similarity measures during trials when the low base rate outcome is selected is consistent with the authors' theory. However, it seems that the increased similarity to rare features on trials when the high base rate outcome is selected (for objects only) would be counter to the authors' dissGCM model.

Finally, the authors have a clear model-based definition of similarity and dissimilarity in the Model description section, similarity as the summed similarity to the winning category exemplars, and dissimilarity as the summed similarity to other categories, so that the two measures are relative to different sets of stimuli. They didn't clearly establish this difference in the Introduction and didn't always clearly interpret results clearly. Many readers will come to the paper assuming that dissimilarity is just the opposite of similarity and need to clearly understand when and how each term is being used. Perhaps using terms like Dissimilarity-Other Category and Similarity-Same category would make it clearer. Some of the most exciting results of the paper are the different neural correlates of similarity and dissimilarity (Figure 5), but it is easy to get confused as to why the negative similarity regressor (blue in Figure 5) differs from the dissimilarity regressor.

3) Logical Flow:

The authors rely heavily on assuming that the reader will not read the paper in a linear order, instead assuming the reader will be familiar with much of the Materials and methods when reading the Results. For example, information regarding the regions that the representational distance scores are drawn from is buried at the end of the Materials and methods. In addition, there are not clear details in the Materials and methods regarding the calculation of the similarity score itself. Thus, it is almost impossible for the reader to know how to interpret the key findings (Figures 3-5) without going back and forth or making some assumptions about the approach. This needs to be overhauled given the format of eLife.

The one place this isn't a concern is the presentation of the dissGCM model. While the details are appreciated, they are also out of place. This needs to be in the Results and Materials and methods, not the Introduction, and disambiguated so that conceptual information necessary for understanding the model and its fit to behavior is provided in Results, while the model itself is formally defined in the Materials and methods.

4) Neural Similarity analysis:

In many cases, it's not clear that the correct statistics were used. For example, in Figure 3, the interaction and main effects are reported as post-hoc t-tests. How was the interaction actually calculated (i.e., can't assess an interaction with a t-test)? What linear model was used? There is also a concern that the key analysis reported in Figure 3 may be based on very few trials. How many trials were actually included for each subject? Was there sufficient statistical power for the analysis?

5) Parameterization of behavior for brain-behavior correlations:

It is not immediately clear what the value is in showing the brain-behavior predictions based on the probability of selecting the low base rate outcome and the pattern similarity scores in Figure 5. This needs to be motivated and explained in more detail.

There is a specific model parameter, (s in Equation 3), that defines the degree to which a subject relies on similarity vs. dissimilarity. Wouldn't correlating individual differences in pattern similarities with this variable be a much more direct measure of the dissGCM hypothesis?

6) Value and clarity of univariate BOLD analysis:

The description of how these results are obtained is a bit opaque in the Materials and methods.

This analysis is asking a tangential question than the primary hypothesis of the paper (i.e., it's not supporting or adding nuance to the key findings from the multivariate analysis).

The interpretations from these maps is subjective and somewhat vague.

7) Analysis of face regions with face stimuli:

Why didn't the authors look at face activation in a face region (e.g., FFA) at all? Faces are the imperfect predictor here, which means they are the stimulus with the most flexibility in terms of associating with the outcome. Wouldn't a key prediction of the dissGCM model be that faces be more similar to object and scene area activity on trials when the common outcome is selected and vice versa for trials where the rare outcome is selected? It seems odd that the analysis is restricted to objects and scenes given the unique position face stimuli are given in the task.

8) Behavioral analysis:

For the behavioral analysis (Figure 2), was the interaction formally decomposed? Please report the relevant statistics in detail. It is also puzzling why reaction time was not reported. Reaction time could shed light on the mechanisms underlying choices. For example, if replying based on similarity is due to habitual responding, one would predict faster RTs in that case. One would also expect longer RTs for more deliberative choices.

9) Presentation of consecutive rare stimuli:

Are there any trials where the authors present two consecutive rare stimuli? Carvalho and Goldstone (2015) suggest that participants make decision by comparing the stimulus at time t with the stimulus at time t-1. In the current article, the stimulus at time t-1 is more likely to be from the same category as the stimulus at time t for common categories than for rare categories. Same category stimuli focus on within-category information (similarity) while different category stimuli focus on between-category information (dissimilarity). This alternative explanation does not rely on base rate and should be discussed.
