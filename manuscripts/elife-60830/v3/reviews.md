# Peer review - Round 1

Editors:
- Thomas Serre, Brown University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.60830.sa1](https://doi.org/10.7554/eLife.60830.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript addresses a major unknown in the literature. Previous empirical studies on the potential role of unsupervised temporal contiguity learning have observed behavioral effects in relatively difficult object discriminations and changes in neural selectivity for very easy object discriminations at the level of single neurons. Linking these two observations is not trivial, and the current manuscript is a very important step towards filling this gap.

Decision letter after peer review:

Thank you for submitting your article "Unsupervised changes in core object recognition behavior are predicted by neural plasticity in inferior temporal cortex" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Takeo Watanabe (Reviewer #2); Hans Op de Beeck (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

This paper raised the very interesting and fundamental question of how unsupervised exposure to objects makes the ventral system learn to better recognize objects in a temporally tolerant way. To address this question, an overall unsupervised computational model was built. The model had three core aspects such as a generative model of a baseline monkey IT population, an IT population and behavior linking model, and an IT plasticity rule that predicts response development of temporally associated object images. Sophisticated human psychophysical experiments were also conducted to examine how the model predicts human object recognition performance. The model with empirically-based monkey IT neural parameters remarkably well predicted the human behavioral results. These results suggest that the unsupervised learning processing successfully linked empirical and theoretical learning results based on monkey IT population to human learning of object recognition.

The reviewers agreed that the manuscript would make a welcome addition to a relatively sparse literature – trying to bridge the behavioral and neurophysiological literature. The general approach was deemed elegant, and the psychophysics results for experiments conducted at this scale on AMT to be surprisingly clean (for the extensive subject training it required). These are arguments that the paper has both the novelty and the quality to be a good fit for the journal.

However, there was also a general sense that the story was somewhat oversold – seemingly providing an almost definitive answer to the questions asked, and in particular on the ability to bridge the two levels. The authors did not convince yet the reviewers that this is an appropriate conclusion. First the model fit does appear to be solid enough, in particular in the high-sensitive range in which most of the neural data were obtained. Furthermore, the conditions between the neurophysiological and the psychophysical experiments were not sufficiently matched, and for too many of the differences we do not know to what extent they matter. There were also substantial issues brought up by reviewers on the modeling side with a reviewer even attempting a crude implementation of the model to understand how parameter free it truly is.

Overall, this is a manuscript with great promises but important caveats were found and controls will need to be done.

Essential revisions:

The manuscript can improve substantially in the message it gives about the level of understanding that has been reached with this work.

1. The results confirm that for large image differences there is a smaller behavioral effect of exposure than needed to really say that the missing link has been resolved. Even a model with a relatively large lapse rate does not explain this. There is very little learning for initial d'>>2, despite that the model with lapse rate 9% still expects so. Also, the lapse rate is a handy solution, but not a very convincing argument. This is a problem, because all the neural findings were obtained with large image differences. The authors do not emphasize this enough, but it should almost be with red letters over the manuscript because it totally changes the interpretation of the findings. As we understand the manuscript, α is estimated in Figure 4 using image pairs with a very high d', and then the prediction of learning effect in Figure 6B fails for such image pairs. Isn't this a major problem? Please comment.

2. The authors made the behavioral task artificially difficult by introducing changes to the test paradigm for which it has not been shown how they might affect the learning effect induced by temporal contiguity exposure at the neural level. This might again affect whether the obtained α can be relied upon. Here are some of the differences. First, in the behavioral experiments, the test phase showed the stimuli on a background. This was not done at the neural level -- do the neural effects of temporal contiguity survive adding a background? Second, in the behavioral experiments, cover trials were interleaved to 'disguise' the simplicity of the testing. How would these cover trials impact neural recordings? Third, the behavioral experiment asks not only for invariance across size, but also in position (at least in screen coordinates), and apparently also pose (p. 3). The neural findings are not necessarily generalizable to this more complicated situation. Fourth, the image discriminability is not matched between the new behavioral experiments and the old electrophysiology. Most of the data here are obtained with faces, which is similar to previous behavioral experiments in this domain, but not representative for the very large image differences in electrophysiology. We encourage the authors to think themselves for ways to address these concerns. The ideal way to address these issues would be to re-do the neural data collection. That is obviously out of scope for a revision given that the current manuscript does not present new neural data. New psychophysical data would not help because the changes with respect to neural recordings are necessary to bring performance below ceiling. Maybe this could be done by switching to another dependent variable that remains relevant at ceiling, such as reaction time data? However, this would add an additional layer of complexity and assumptions about how RT relates to neural selectivity. Maybe the authors can consider this. If not, then we would be amenable to the authors (i) acknowledging this discrepancy and toning down their conclusions accordingly, (ii) indicating which differences might be most important (or speculate on why they might not be important, and (iii) mentioning explicitly that further neural recordings are necessary to decide the issue.

3. The authors should also be more complete about the discrepancies in the literature that put further doubt on how accurate our estimate is of the actual effect size and the boundary conditions under which effects of temporal contiguity exposure occur. There are null results in the literature. For example, Crijns et al., 2019 found no effect in rat V1. Nor did a recent human fMRI study (Van Meel et al., 2020, NeuroImage), which used an exposure paradigm with objects and size changes that is very similar to what is used in the current manuscript. This literature is not mentioned, or even cited wrongly (Crijns et al.,). I have a difficulty with bringing all these null results in agreement with the current set of findings. We might overestimate the effect of temporal contiguity based upon how the authors have summarized the literature. In terms of future directions, there is clearly also a need for further neural investigation of the boundary conditions of temporal contiguity effects.

4. There was a level of skepticism regarding how truly parameter free the model actually is. A model that goes from single cell responses to behavior necessarily has quite a few moving parts and associated design choices. For some of these choices it would be comforting to see what happens when they are dropped or altered. To what extent is the apparent zero-parameter match of the learning rates subject to an implicit model fitting by means of design choices? Specifically, the authors use the same size tuning template for all neurons in the population, combined with multiplicative noise. It feels as if this is not a random choice. The reviewers suspect that it will – at least on average – preserve the performance of the classifier across different object scales, because the classifier computes correlation coefficients and hence normalizes responses. It also means that the update during learning for the non-swapped exposure is – again on average – in the same direction for all neurons (either increasing or decreasing the rate, depending on the size tuning template). Is the improvement of discrimination performance in the model independent of the specific size tuning template that is used? Or does it depend on whether the firing rate at the large size is higher or lower than at the medium size? An independent sampling of size tuning for the different neurons would have been the more natural choice. It would be comforting to see the results hold up.

Please note that one of the reviewers actually went through the trouble to actually quickly code up a toy variant of the model. They reported that it appeared as if the learning rate in the model could be controlled by means of setting noise levels, and the consistent size tuning altered how much the model's classification performance improves for the non-swap exposure scenario. It was also noted that the improvement for non-swap and the deterioration for swap is actually even more pronounced without the consistency in size tuning, which maybe speaks in favor of at least the qualitative aspect of the model. The question thus remains whether it is possible to get both learning rates to match the data without the tuning consistency. This is an important point raised and we expect additional comments and controls.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Unsupervised changes in core object recognition behavior are predicted by neural plasticity in inferior temporal cortex" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Takeo Watanabe (Reviewer #2); Hans Op de Beeck (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

As requested by Reviewer #2, please:

1) Add a brief discussion regarding differences in how objects/faces are encoded in the visual cortex and possible implications (or lack thereof) for the interpretation of results.

2) Confirm that corrections for multiple comparisons were implemented.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Unsupervised changes in core object recognition behavior are predicted by neural plasticity in inferior temporal cortex" for further consideration by eLife. Your revised article has been evaluated by Michael Frank (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

The argument that you are making regarding the absence of correction for multiple comparisons sounds reasonable, but it is open to debate. While we are sympathetic to your point about letting "the reader [to] decide on what inferences to draw from the data, confidence intervals and associated statistical test", we also feel that in the current manuscript form, the reader might not realize the absence of corrections. As a compromise, we suggest that you add a paragraph in the methods including your justification to make this clear.
