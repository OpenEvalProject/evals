# Peer review - Round 1

Editors:
- Srdjan Ostojic, https://ror.org/05a0dhs15 Ecole Normale Superieure Paris France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67258.sa0](https://doi.org/10.7554/eLife.67258.sa0)

Empirical findings have established that experimental manipulations which increase perceptual accuracy also generally reduce the amount of shared variability between neurons in the visual cortex. To explain this observation, this study combines neurophysiology data and a network model of visual cortex and tests the hypothesis that perception relies on a "general" decoding strategy. The results suggest that the brain seeks to decode arbitrary changes in stimuli that appear in the environment.


---

# Peer review - Round 1

Editors:
- Srdjan Ostojic, https://ror.org/05a0dhs15 Ecole Normale Superieure Paris France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67258.sa1](https://doi.org/10.7554/eLife.67258.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "A general decoding strategy explains the relationship between behavior and correlated variability" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Tirin Moore as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

A highly robust result when investigating how neural population activity is impacted by performance in a task is that the trial to trial correlations (noise correlations) between neurons is reduced as performance increases. However, the theoretical and experimental literature so far has failed to account for this robust link since reduced noise correlations do not systematically contribute to improved availability or transmission of information (often measured using decoding of stimulus identity). This paper sets out to address this discrepancy by proposing that the key to linking noise correlations to decoding and thus bridging the gap with performance is to rethink the decoders we use : instead of decoders optimized to the specific task imposed on the animal on any given trial (A vs B / B vs C / A vs C), they hypothesize that we should favor a decoder optimized for a general readout of stimulus properties (A vs B vs C).

To test this hypothesis, the authors use a combination of quantitative data analysis and mechanistic network modeling. Data were recorded from neuronal populations in area V4 of two monkeys trained to perform an orientation change detection task, where the magnitude of orientation change could vary across trials, and the change could happen at cued (attended) or uncued (unattended) locations in the visual field. The model, which extends previous work by the authors, reproduces many basic features of the data, and both the model and data offer support (with one exception, details below) for the hypothesis.

The reviewers agreed that this is a potentially important contribution, that addresses a widely observed, but puzzling, relation between perceptual performance and noise correlations. The clarity of the hypothesis, and the combination of data analysis and computational modelling are two essential strengths of the paper. Nonetheless, as detailed below, the reviewers believe the manuscript clarity could be further improved in several points, and some additional analysis of the data would provide more straightforward test of the hypothesis.

Essential revisions:

1. it would be important to verify that the model reproduces the correlation between noise and signal correlations since this is really a key argument leading to the author's hypothesis. One possibility would be to make a scatterplot of these two correlations for all neurons for both neural data and the model and for example compare slopes. The slope for the model could be shown for a range of levels of attentional modulation and for the neural data in attended vs unattended as they already do in fig2d of Fig2e. The authors could provide insight into the difference between the specific and general decoder by directly assessing the alignment between the decoders and the noise dimension. This could perhaps (depending on data noise) also be assessed for their physiological decoders of increasing generality (Fig3e).

2. Testing the hypothesis of the general decoder:

2.1 In the data, the authors compare mainly the specific (stimulus) decoder and the monkey's choice decoder. The general stimulus decoder is only considered in Figure 3f, because data across multiple orientations are available only for the cued condition, and therefore the general and specific decoders cannot be compared for changes between cued and uncued. Fair enough, though this could be stated more explicitly around Line 160. However, the hypothesized relation between mean correlations and performance should also be true within a fixed attention condition (cued), comparing sessions with larger vs. smaller correlation. In other words, if the hypothesis is correct, you should find that performance of the "most general" decoder (as in Figure 3f) correlates negatively with average noise correlations, across sessions, more so than the "most specific" decoder. If there is enough data to identify this trend, it could strengthen the conclusions, because Figure 3c per se is not particularly overwhelming, and this reviewer is not sure that the correlation is significant for cued alone or uncued alone data, despite the fact that the range of noise correlation values within each condition is comparable to the range across conditions.

2.2 The analysis in fig3F provides a strong second line of argument in favor of the hypothesis. However, a lot hangs on the two points for "1 ori". This is because the authors restricted analysis to using the 4th orientation as a reference. It seems possible that this analysis could be repeated for other orientations apart from the 3rd on which the monkey data is trained so as to augment the number of points and bring out the relation more clearly.

2.3 In figure 3f, a more straightforward and precise comparison is to use the stimulus decoders to predict the choice, and test whether the more specific or the more general can predict choices more accurately.

3. The main goal of the manuscript is to determine the impact of noise correlations on various decoding schemes. The figures however only show how decoding co-varies with correlations, but a direct, more causal analysis of the effect of correlations on decoding seems to be missing. Such an analysis can be obtained by comparing decoding on simultaneously recorded activity with decoding on trial-shuffled activity, in which noise-correlations are removed. Related to this, the manuscript starts by stating that theoretical studies predict optimal decoding is independent of correlations. Yet, it is apparently never shown (using shuffles) that this prediction actually holds for the "specific" decoder. Conversely, it is not shown that the monkeys' or the general decoder are actually sensitive to removing correlations by shuffling.

4. Figure 3a: Why is the performance of the "monkey's decoder" so low on uncued trials? Is this fully explained by a change in the magnitude of correlations (ie would shuffling single trials in the cued trials lead to such a large decrease)? Or is it due to some other mechanism?

On a related note, how different are the four different decoders (specific/monkey, cued/uncued)? It would be interesting to see how much they overlap. More generally, the authors should discuss the alternative that attention modulates also the readout/decoding weights, rather than or in addition to modulating V4 activity. And also, that the decoder is just suboptimal, not suboptimal locally because optimized for generality. For instance, Figure 3a suggests that in the uncued condition there is lots of information in the neural activity, but the monkeys do not use it. In contrast, the general decoder in the model extracts a large fraction of the information (Figure 3b).

5. Quantifying the link between model and data:

5.1 the text providing motivation for the model could be improved. The motivation used in the manuscript is, essentially, that the model allows to extrapolate beyond the data (more stimuli, more repetitions, more neurons). That sounds weak, as the dangers of extrapolation beyond the range of the data are well known. A model that extrapolates beyond existing data is useful to design new experiments and test predictions, but this is not done here. Because the manuscript is about information and decoding, a better motivation is the fact that this model takes an actual image as input and produces tuning and covariance compatible with each other because they are constrained by an actual network that processes the input (as opposed to parametric models where tuning and covariance can be manipulated independently).

5.2 The ring structure, and the orientation of correlations (Figure 2b) seem to be key ingredients of the model, but are they based on data, or ad-hoc assumptions? L'179-181:"we first mapped the neuronal activity to a 2d space" – how was this done? What are the axes in Figure 2b? The correlation structure appears to be organized in 2d, how can one then understand the 1d changes in Figure 2f?

5.3 In the model, the specific decoder is quite strongly linked to correlated variability and the improvement of the general decoder is clear but incremental (0.66 vs 0.83) whereas in the data there really is no correlation at all (Figure 3c). This is a bit problematic because the authors begin by stating that specific decoders cannot explain the link between noise correlations and accuracy but their specific decoder clearly shows a link.

It may be that the comparison is a bit unfair on the author's hypothesis precisely because of the huge power provided by the model. In order to compare the magnitude of the effect with physiological data, the authors could down sample the results from their model to the range of correlated variability from the monkey data. This may be revealing because the correlation does not seem quite linear and plateaus out close to the monkey's range.

5.4 Quantitative mismatch between model and data: the model is intended to offer only qualitative predictions, and this is fine. But the reviewers did not understand the argument (eg. Line 191 and Line 320) that a quantitative mismatch is a good thing… after all, if the range of changes in noise correlations is small for the data, isn't that the relevant range?

6. General decoder: Some parts of the text (eg. Line 60, Line 413) refer to a decoder that accounts for discrimination along different stimulus dimensions (eg. different values of orientation, or different color of the visual input). But the results of the manuscripts are about a general decoder for multiple values along a single stimulus dimension. The disconnect should be discussed, and the relation between these two scenarios explained.

7. Some statements in the discussion such as l 354 "the relationship between behavior and mean correlated variability is explained by the hypothesis that observers use a general strategy" should be qualified: the authors clearly show that the general decoder amplifies the relationship but in their own data the relationship exists already with a specific decoder.

8. Low-Dimensionality, beginning of Introduction and end of Discussion: experimentally, cortical activity is low-dimensional, and the proposed model captures that. But this reviewer does not understand the argument offered for why this matters for the relation between average correlations and performance. It seems that the dimensionality of the population covariance is not relevant: The point instead is that a change in amplitude of fluctuations along the f'f' direction necessarily impact performance of a "specific" decoder, whereas changes in all other dimensions can be accounted for by the appropriate weights of the "specific" decoder. On the other hand, changes in fluctuation strength along multiple directions may impact the performance of the "general" decoder. Please revise the text to clarify.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A general decoding strategy explains the relationship between behavior and correlated variability" for further consideration by eLife. Your revised article has been evaluated by Tirin Moore (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below.

The authors declined to investigate the impact of shuffling data on their results and the reason given (they are not making claims whether correlations vs no correlation is better) doesn't seem relevant to the point raised. The key issue is that the text suggests a causal, mechanistic link between correlations and the decoder, but this need not to be the case. For instance, in the model, the authors manipulate noise correlations via the modulation of simulated top-down feedback. This may impact other aspects of network activity rather than only correlations, and these other aspects may be responsible for the modified decoding. Similarly, changes in attention levels may indirectly lead to changes in both correlations and decoding, without the two being in a direct causal relation.

It seems like an easy and straight-forward sanity check to see if the accuracy of the two decoders correlates with attention level after shuffling both training and test sets. If shuffling has no effect on the results, the causal statements would need to be amended and/or discussed.
