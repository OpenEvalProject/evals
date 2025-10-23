# Peer review - Round 1

Editors:
- Jonathan Erik Peelle, https://ror.org/01yc7t268 Washington University in St. Louis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77468.sa0](https://doi.org/10.7554/eLife.77468.sa0)

This MEG study elegantly assesses human brain responses to spoken language at the syllable, word, and sentence level. Although prior studies have shown significant cortical tracking of the speech signal, the current work uses clever task manipulation to direct attention to different timescales of speech, thus demonstrating tracking mechanisms that are both automatic and task-dependent operate in tandem during spoken language comprehension.


---

# Peer review - Round 1

Editors:
- Jonathan Erik Peelle, https://ror.org/01yc7t268 Washington University in St. Louis United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77468.sa1](https://doi.org/10.7554/eLife.77468.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Task-dependent and automatic tracking of hierarchical linguistic structure" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Barbara Shinn-Cunningham as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Johanna Rimmele (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. The relationship of participants' behavior to the observed MEG responses. One clear concern is the degree to which the accuracy differences between word lists and sentences (Figure 1) explain MI differences.

2. A number of important details regarding analysis choices were missing and should be added, including: justification of the frequency bands used for the MI analysis, task order (were sentences always first, and word lists second), whether ROIs were defined across hemispheres, details on signal filtering, and details regarding the PCA analysis.

3. The use of "hierarchical linguistic structure" should be clarified or tempered in the context of the current results. Although the attention was directed to syllables, words, and phrases through instructions, the significant MEG results were in the phrasal band (Figure 3) and not the others (supplemental figures).

Reviewer #1 (Recommendations for the authors):

The participants ranged in age from 18-59, which is a rather broad range. Given age-related changes in both hearing (not assessed) and language processing, it was surprising to not at least see age included in the models (though perhaps there were not enough participants?). Some comment would be useful here.

Figures: The y axis label seems frequently oddly positioned at the top – maybe consider just centering it on the axis?

I liked the inset panels for the main effects, but they are rather small. If you can make them any larger that would improve readability.

In general, I really like showing individual subjects in addition to means. However, it also can make the plots a bit busy. I imagine you've tried other ways of plotting but might be worth exploring ways to highlight the means a bit more (or simplify the main paper figures, and keep these more detailed figures for supplemental)? Totally up to you, but I had a hard time seeing the trends as the plots currently stand.

On my copy of the PDF, Figures 6 and 4 (p. 14) were overlapping and so really impossible to see.

Figure 1: In the text, the condition is referred to as "word list", but in the figure "wordlist". Having these match isn't strictly necessary but would be a nice touch.

Regarding accuracy differences: including accuracy in the models are good, but alternately, restricting analyses to only correct responses might also help with this?

Reviewer #2 (Recommendations for the authors):

– l. 122: does that mean the sentence was always presented first and the word-list second? The word-list did not contain the same words as the sentence, right? This might have affected differences in tracking and power.

– l. 197: why were the linear mixed-models for the MEG data performed separately per ROI? Also, were ROIs computed across hemispheres?

– l. 198: was the procedure described by Ince et al., 2017 using gaussian copula used for the MI analysis, if yes could you cite the reference?

– l. 191: could you give the details of the filter, what kind of filter etc?

– l. 191/l. 206: why were the frequency bands for the power analysis (δ: 0.5-3.0 Hz; theta: 3.0-8.0 Hz; α: 8.0-15.0 Hz; β: 15.0-25.0 Hz) different than for the mutual information analysis (l. 191: phrase (0.8-1.1 Hz), word (1.9-2.8 Hz), and syllable (3.5- 5.0 Hz)), could you explain the choice of frequency band? Particularly, if the authors want to check signal-to-noise differences in the mutual information analysis by using the power analysis, it seems relevant to match frequency bands.

– l. 207: why was the data averaged across trials and not the single-trial data fed into the mixed-models, such an analysis might strengthen the findings?

– l. 213: averaged across hemispheres or across trials?

– l. 216: all previous analyses were conducted across the hemispheres?

– l. 217: "for the four different frequency bands" this is referring to the frequency bands chosen for the power analysis, not those in the MI analysis?

– Figure 1: were only correct trials analyzed in the MEG analysis? If not, this might be a problem as there were more correct trials in the sentence compared to the word-list condition at the phrasal scale task. Could you add a control analysis on the correct trials only, to make sure that this was not a confound?

– l. 252 ff./Figure 2: As no power peak is observed in the δ (and α) band, this might result in spurious connectivity findings.

– l. 304: with higher connectivity in the phrasal compared to the passive task? Could you add this info?

– Something went wrong with figure 6.

– l. 403: alignment of neural oscillations with acoustics at phrasal scale, this reference seems relevant here: Rimmele, Poeppel, Ghitza, 2021.

– Wording: l. 387 "in STG".

Reviewer #3 (Recommendations for the authors):

1. In procedure settings, I am not sure whether the sentence condition is always presented before the word list condition (the misunderstanding comes from lines 126-128). Please add the necessary details and avoid this misunderstanding.

2. In the MEG analysis, PCA was performed to reduce computational load and increase the data relevance. However, the PCA procedure is not clear. For example, the authors extracted top *20 PCA components per region. Why 20 components? And why not 10 or 30 components? The details should be clarified.
