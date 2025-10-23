# Peer review - Round 1

Editors:
- Gaël Varoquaux, Inria Saclay France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.53588.sa1](https://doi.org/10.7554/eLife.53588.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Dijkstra et al. provide empirical evidence for reversal of perceptual inference by analyzing the electrophysiological signature of brain responses to visual stimuli. It reveals a feedback loop from higher-level regions that appear as an oscillation in the delay of the brain response. This empirical evidence is useful to refine theories of perception.

Decision letter after peer review:

Thank you for submitting your article "Neural dynamics of perceptual inference and its reversal during imagery" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Timothy Behrens as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript uses MEG during a working memory/imagery task to investigate the flow of information between low and high level areas during perception and imagery respectively. The authors provide empirical evidence consistent with the notion that high level regions are first during imagery, and last during perception. In addition, they show that recall leads to several oscillations (around 11Hz), interpreted as bottom-up and top-down processes. This evidence is extracted via several methodological innovations. A multivariate classification methods, namely Linear Discriminant Analysis (LDA) is applied to various time points following stimulus presentation and the resulting trained classifiers (one by time-point) are used, to time-align the imagery trials via their ability to discriminate better than others. This time alignment is central to claim that “information” is processed bottom-up or top-down along the ventral visual pathway. Here the distance to the discriminating hyperplane is used as a proxy for the evidence that the signal is present, analyzed at the group level.

The findings were deemed of high interest by the reviewers. The evidence for oscillations is expected to stimulate greatly neurosciences, in particular predictive coding theory. Indeed, the phenomena revealed are insufficiently known (e.g. the oscillation between feedforward and feedback activity during imagery). The reviewers also appreciated the creative use of classifiers to extract signal as well as the fact that the data from the study are publicly available.

The discussions however mostly focused on trying to decide whether or not the evidence was conclusive. Given the amount of non-classic data transformations that lead to the evidence, how to assert that the results, in particular the multiple oscillations, are specific to visual recall, and not low-level properties of the neural signal, Indeed, the neural signal has a complex time-frequency structure. Our understanding of the permutations used is that they will create unstructured patterns, which will lead to a random and unstructured ordering of the most-similar pattern. In other terms, the permutations do not capture the temporal structure of the neural signal. A better null procedure is needed to provide solid evidence that the oscillation revealed is indeed related to imagery dynamics.

Essential revisions:

1) A first point to clarify are what aspects of the stimuli that drives variations in the perception time. The manuscript is very light on details in terms of the psychological dimensions varied to create the variations in the perception time that are related to variations in the imagery time. The theories invoked (predictive processing theories) relate to ambiguity in the sensory signal, hence they suggest that the variations the perception time should be related to the stimuli. Yet, the manuscript does not offer an explanation on the causes the variation in perception time. Some of the differences between the two classes of stimuli likely reflect "unspecific" mechanisms: i.e. electrophysiological signatures that are not specific to particular neural representations, but to overall differences in e.g. attentional capture. For example, if faces trigger a stronger visual response than houses, then, what is considered to be the reactivation of a face in this study, would simply reflect an overall modulation of visual/IT activity. Such non-specific activation would be expected to trigger feedforward and feedback traveling waves in the ventral and dorsal visual pathways, as extensively described in monkey electrophysiology as well as with MEG (e.g. Michalareas et al., 2016). For these reasons, we feel that the revised manuscript should discuss in detail what aspects of the stimuli drive the variations in time.

2) A second wider point relates to establishing whether or not the sophisticated analysis enhances oscillations that are specific to mental imagery, or rather general to neural signals. Indeed, neural signals have a complex autocorrelation structure. To address the possible confound that alpha modulation could affect the SNR and explain the corresponding findings the authors perform a coherence analysis on individual sensors. The fact that no significant effect is obtained with this analysis motivates the authors to rule out this hypothesis. However, statistics on single sensors are known to be less statistically powerful techniques, so the result could be explained by the poor statistical power of this supplementary analysis. Overall, all the reviewers found it hard to assess the methods, and hence feel that the whole pipeline should be experimentally shown not to create the signatures that are interpreted. A small number of specific analyses can help establishing this evidence without resorting to fine theoretical analysis of the data-processing pipeline:

A) Applying the same exact analysis to neural signal where one would not expect such conclusion to arise. A specific instance of such signals can be found using time windows located in the inter-stimuli intervals (for instance before the trial).

B) Using a complementary analysis based on second-level statistics: i.e. fit a distinct model on each subject separately, and test the reactivation signatures across subjects. Indeed, the authors use mixed-model/first-level statistics with trials and subjects as random variables. Such approach is unusual in decoding-based analyses, because of the cross-validation – i.e. the training of the decoder introduces dependencies across decoders' predictions, and thus breaks the independence assumption of first-order statistical tests.

C) Using the non low-pass filtered data. Indeed, there is the suspicion that the oscillatory effect observed during perception could be due to a low pass filtering effect. This doubt is suggested by the supplementary analysis using non-low pass filtered data. Figure S2 in supplementary material is however not comparable to the corresponding figure in the main text. If the non-low pass filtered data actually confirm the findings these data should be used in the main text without the need for added analysis.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Neural dynamics of perceptual inference and its reversal during imagery" for further consideration by eLife. Your revised article has been evaluated by Timothy Behrens (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

The reviewers find that the evidence is not rock solid, but the work is stimulating and the findings do not stem from an apparent methodological flaw. They feel that publishing these is beneficial for the field, but would like the potential limitations to be more explicit. No additional analysis is mandatory for resubmitting, but work on the wording is important.

Reviewer #1:

The authors answered thoroughly most of the comments raised by the reviewers. Importantly, they performed complementary analyses to make the evidence stronger, for instance the analysis without low-pass filtering. Also, the trial-level data show a weak effect, but one that is present, which is an important piece of evidence to confirm that the effect is not created by the analysis. They unfortunately did not follow our suggestion of analyzing data outside the stimuli, which would have made a strong null hypothesis. Rather, they used an elaborate simulation.

Overall, I feel comforted that the evidence is not created by the data analysis, and I am in favor of publication.

Reviewer #2:

Thanks to the authors for this response.

Generally speaking, I am not amazed by responses based on simulations – which is the source of a significant set of the new results and analyses in the present revision. Simulations remain soft controls, because, unlike real data, they may be blind to a wide variety of issues. Responses systematically based on novel analyses of the MEG signals would have been more convincing, like we originally proposed (e.g. applying the same analyses on different time windows such as the inter-stimulus interval, in order to ensure that no effect were found there).

In addition, if I understand correctly, the p-values derived from the mix models may be invalid (reviewing comment 2B): i.e. we cannot easily estimate p-values when the independence hypotheses between samples is not met – which is the case with a CV, because the training models are fitted on partially similar datasets – consequently their predictions are not independent: c.f. e.g. Noirhomme et al., 2014 (NeuroImage: Clinical).

This arguably minor concern is reinforced by the fact that single-trial-based statistics can dramatically increase the degrees of freedom, and can thus lead to unreasonably confident p-values. Second-level stats across subjects only would be a more conservative approach. Again, the authors did not follow that recommended route.

That being said, these statistical issues should not undermine the methodological and neuroscientific work. While I am relatively unhappy with the current answer, the paper remains interesting and potentially important.

Consequently, I will not oppose its acceptation for publication, but would strongly recommend the authors to provide a clear code of their analyses and simulations to facilitate future replications.

Reviewer #3:

I would like to thank the authors for the convincing and thorough revision.

I just have two remaining comments.

– Related to your answer "We acknowledge that this breaks the independence assumption but we still believe that this is the most valid test for our data, since testing across subjects ignores the large between-trial variability." Can you add a sentence somewhere in the text about this?

Just as a comment here, using non-parametric methods like in the EEGLAB LIMO toolbox would address this issue: e.g. Pernet et al., 2011 (Computational Intelligence and Neuroscience).

– The proper URL for MNE software is https://mne.tools/ and the related

publication is:

A. Gramfort, M. Luessi, E. Larson, D. Engemann, D. Strohmeier, C. Brodbeck, L. Parkkonen, M. Hämäläinen, MNE software for processing MEG and EEG data, NeuroImage, Volume 86, 1 February 2014, Pages 446-460, ISSN 1053-8119
