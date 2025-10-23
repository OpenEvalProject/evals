# Peer review - Round 1

Editors:
- Jonathan Erik Peelle, https://ror.org/04t5xt781 Northeastern University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82386.sa0](https://doi.org/10.7554/eLife.82386.sa0)

This study addresses a fundamental aspect of human speech processing: namely, how acoustic and linguistic features interact during comprehension. The authors present convincing evidence that helps elucidate the role of language experience on neural processing, re-weighting processing of speech based on whether a listener understands the language being spoken.


---

# Peer review - Round 1

Editors:
- Jonathan Erik Peelle, https://ror.org/04t5xt781 Northeastern University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82386.sa1](https://doi.org/10.7554/eLife.82386.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "A tradeoff between acoustic and linguistic feature encoding in spoken language comprehension" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Andrew King as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The aspects of the current results that are consistent with vs. different to prior arguments should be better clarified. As it stands, the theoretical advance of the current paper relative to much current thinking in the field is not always clear.

2) The treatment of the high-entropy vs. low-entropy contexts in the models was unclear; in particular, if separate TRFs were constructed for these groups of contexts (line 260), a single model (in which entropy was included as a factor) would seem preferable (this was suggested by the model in line 275). Please clarify the model construction and results that were obtained and which underlie the main conclusions (including how words were divided into high vs. low entropy).

3) The conclusions about listener responses to understood (Dutch) vs. not-understood (French) speech need to be tempered to account for the acoustic differences across language (and possibly across speaker – it was unclear whether the same talker was used for both languages). These points should be explicitly considered and clarified.

Reviewer #1 (Recommendations for the authors):

Figure 4 was very useful and I thought should appear earlier in the paper – I would put this first, so that readers see it as that.

I could not find data or analysis scripts, which would be useful to share. There is a promise that it will be available through an institutional repository but it should be available as part of the review process, no?

Reviewer #2 (Recommendations for the authors):

TRF analysis. As the authors mention, the TRFs will be highly correlated for different features, which makes it problematic to infer the spatiotemporal distribution of each speech feature. Can the authors take this analysis further by assessing model accuracies as before, but this time changing the lags over which the regression is computed (e.g. in sliding time windows 0-50 ms, 25-75 ms, etc.)? This would give information on processing latencies unique to a particular speech feature, going beyond what is currently presented.

Could the authors discuss what might explain their finding of specific phoneme tracking independent of acoustics, which is contra the findings of Daube et al.

I am unclear about linear mixed models presented for the 'Tracking performance of linguistic features' section (some of the issues described here apply elsewhere too). The text states that forward difference coding was used to assess the difference between consecutive models. Which p-values correspond to these contrasts? Are they reported in the tables? But these look like the coefficients of a model, not model comparisons. Significance braces are shown in the figures but the captions do not indicate what these represent exactly. Then in line 224 there is a single p-value attributed to the effect of model, which again I am unsure how to interpret (is the combined effect of the forward difference contrasts?). Finally source plots in Figure 1D, do they show the forward difference contrasts or do they show pairwise comparisons between e.g. acoustic model vs phoneme onsets, phoneme onsets vs phoneme entropy etc. To make this section clearer, in addition to providing additional detail (e.g. in the figure captions), I would consider using more familiar pairwise comparisons instead of forward difference contrasts.

Figure 2, please fully label all plots. e.g. 2A the dark vs light green bars are not distinguished (same issue for TRF plots). Do they represent the left vs right hemispheres? If so, where are the data for the high vs low entropy comparison? There is an inset panel but I think it would be clearer to show all the 'conditions' in the main graphs i.e. high low entropy, left right hemisphere. As with Figure 1, caption needs more detail e.g. what are the significance braces indicating?

Please specify how words were grouped into high and low entropy. Median split?

Reviewer #3 (Recommendations for the authors):

Regarding point (2) of the public review, my suggestion would be to analyze the distinction by including both low and high entropy predictor sets in a single TRF model. This way, all words' responses would be accounted for, and overlapping responses from different words would be properly controlled for. Contributions from specific sets of predictors could still be assessed by estimating models without those predictors.

Regarding point (3), a stronger case could be made, for example, with a group of French speakers listening to the same stimuli – to make comprehension orthogonal to acoustic properties.

Errors/inconsistencies

Line 531 implies that acoustic edges were modeled in 8 bands ("8-band acoustic onset spectrogram") but Figure 4 only shows a single time series.

In Figure 4A, it looks to me like the spectrogram is shifted relative to the sound wave.

In Figure 4A, the third word has lower Word Entropy than the fourth, but is assigned to the high entropy condition, while the fourth is in the low entropy condition.

The Discussion says about the initial model (before adding entropy) "Phoneme surprisal, phoneme entropy, and word frequency reconstruction accuracies were left-lateralized" (348), but I don't think I saw a statistical test of lateralization. In fact, in the model with entropy the effect of Hemisphere for phoneme features was n.s. (281).

"To isolate the effect of sentence and discourse context and control for the frequency effect we also added word frequencies in our full model" (374): I don't believe this is doing what is intended (/described). The main question asked statistically is whether word entropy modulates other predictors' TRFs. Adding a word frequency predictor will control for responses correlated with word frequency, but it will not control for other predictors' TRF shapes being modulated by word frequency.
