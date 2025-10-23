# Peer review - Round 1

Editors:
- Barbara G Shinn-Cunningham, Boston University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.16747.014](https://doi.org/10.7554/eLife.16747.014)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Individual differences in selective attention predict speech identification at a cocktail party" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Barbara G Shinn-Cunningham (Reviewing editor and Reviewer #1) and Hari Bharadwaj (Reviewer #2), and the evaluation has been overseen by Eve Marder as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. We hope you will be able to submit the revised version within two months, so please let us know if you have any questions first.

Summary:

This investigation tests the hypothesis that individual differences in the ability to identify target speech in the presence of spatially separated speech distractors is related to cross-subject differences in both supra-threshold auditory temporal processing abilities and cognitive function. More specifically, the authors assess binaural sensitivity to temporal-fine-structure (TFS) information and the ability to focus attention in a large group of young audiometrically normal-hearing listeners, thereby extending and complementing previous work. Overall, this is a nice study in distinguishing between sensory and central contributions to individual differences that may affect everyday communication. The study is clear, well written, and of interest to the hearing-research community. We have three major issues that need to be addressed, along with some suggestions that might strengthen your presentation.

Essential revisions:

1) The statistical tests you performed do not disprove a sensory contribution to the observed individual differences that you argue reflect top-down attention.

You have shown that the intensity difference limen (DL) measured using backward masking correlates strongly with DL in quiet (Table 2). Given that DLmasked and DLquiet are strongly correlated, using them both as predictors in the multiple regression analysis makes the assignment of coefficients (and subsequent t-scores) dependent on the exact algorithm used for fitting, and essentially arbitrary.

If DLmasked was not included, was DLquiet a significant predictor? Is DLmasked a significant predictor when DLquiet has already been partialed out?

The Lasso fitting procedure penalizes the L1-norm of the set of coefficients, thereby favoring sparse solutions. Thus, it would pick the better of the two predictors: that is, DLmasked might be picked over DLquiet or over both together. However, the fact that the procedure does not pick DLquiet is not in itself evidence that DLmasked does not include differences from sensory factors. All this proves is that the DLmasked is the better of the two predictors overall and effectively encompasses the other.

Also, you use an eigenvalue ratio criterion (First paragraph of Regression analysis section) to say that there isn't a multicollinearity problem here. This index is of limited utility when many noisy predictors are used. Indeed the correlation between DLmasked and DLquiet is already evidence for some multi collinearity.

The language you use to describe your results needs to reflect these subtleties, and/or you need to include more extensive statistical testing to rule out sensory contributions that are correlated with/included in DLmasked. All you can currently conclude is that the perceptual weight given to the masker accounts for the behavior, not that this factor reflects only top-down selection.

2) Isn't a differential measure of auditory masking effects more in line with your other metrics?

If the differences in DL under masking reflect top-down selection, it seems to make more sense to quantify the differential effect of masker on DL as a correlate rather than the overall threshold under masking (e.g., DLmasked minus DLquiet). This would better parallel the visual measure you use (the differential effect of the flanker on the reaction time) as a measure of top-down selection (as opposed to the overall RT with an incongruent flanker).

3) The "cognitive" component you measure seems more specific than your discussion/presentation concedes.

The backward masking task you used to isolate auditory "attention" requires listeners to attend to a signal and ignore a later event that draws attention exogenously. This task no doubt indexes the ability to suppress an exogenous draw of attention, and your results show that this ability differs across listeners in a way that is reflected in "cocktail party" listening. However, this may be very different from the ability to sustain focused attention. Indeed, different attentional control subnetworks are thought to control exogenous vs. endogenous attention; a whole host of processes (e.g., precise sensory coding, scene analysis, top-down selection, exogenous attention.) allow us to selectively understand a target and ignore maskers.

In the first paragraph of discussion, you claim that "the ability to direct auditory selective attention" differs in consistent ways across listeners; however, it seems more appropriate to argue that there are differences in "the ability to suppress exogenously salient, but task-irrelevant auditory events." See also the second paragraph, and eighth paragraph of Discussion section where you write, "future experiments on attentional factors influencing cocktail-party listening could include tasks measuring both the endogenous and exogenous orienting of attention." We agree; but we suspect you have just isolated one particular aspect of attention, already.

This does not diminish the importance of your study, but changes the language you might use to discuss your results. Please consider integrating this idea into the way you describe your study. Rather than arguing that you are measuring "attention" (and leaving it at that), taking a more sophisticated, nuanced view that distinguishes amongst different aspects of attention, and that doesn't over-simplify, would enhance the impact of your work.
