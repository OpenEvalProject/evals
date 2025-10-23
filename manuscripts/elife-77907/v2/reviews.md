# Peer review - Round 1

Editors:
- Stephanie E Palmer, https://ror.org/024mw5h28 University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77907.sa0](https://doi.org/10.7554/eLife.77907.sa0)

This work builds on rapidly accumulating evidence for the importance of measuring and accounting for behaviour in neural data, and will be of interest to a broad neuroscience audience. Analyses of Allen Brain Atlas datasets show that sensory representations change and match up reliably with behavioural state. The article's main conclusions are supported by the data and analyses, and the work raises important questions about previous accounts of the sources of representational drift in sensory areas of the brain.


---

# Peer review - Round 1

Editors:
- Stephanie E Palmer, https://ror.org/024mw5h28 University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77907.sa1](https://doi.org/10.7554/eLife.77907.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Contribution of behavioural variability to representational drift" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Michael Frank as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Yaniv Ziv (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers all enjoyed the paper and feel that the work is timely and well-executed. However, some common questions and concerns arose in the reviews which were discussed by the group. These are the essential revisions for the manuscript. Please also see the detailed comments from each reviewer below, which should improve the overall impact of the manuscript.

(1) Statistical analyses should not be limited to Pearson correlation and should include more sophisticated metrics, given the clear non-monotonic relationships in the data.

(2) Clarify the terms used that can seem at odds or confounding. Example: "representational drift" and "representational similarity" shouldn't be used interchangeably. For example, it may also be useful to provide working definitions of (and differences between) "drift of behavioral state", "behavioral drift" and "behavior" at the beginning of the manuscript.

(3) Related to point 2, it is crucial to explain the stance taken in the paper on how behavior and elapsed time are to be separated. Please see the relevant major prompts from Reviewers 2 and 3 who have suggested potential new analyses that would make this distinction most clear.

(4) The decoding results as currently reported seem obvious and underdeveloped. To make this have a bit more power, this should be expanded to include a new calculation, perhaps on decoding behavioral state along with the stimulus.

(5) Improve the figure layout to make the work more engaging to a broad readership. A diagram in Figure 1 would be useful.

(6) Show how these results depend on other behavioral parameters measured in these datasets, such as pupil location.

Reviewer #1 (Recommendations for the authors):

Overall the work is careful, and the presentation of the results is thorough. Some questions and suggestions for revision remain, however:

(1) The decoding results seem obvious – if the downstream decoder does not "know" about the behavioral state, then the neurons that are shifted by the behavioral state should be weighted less. Is there anything more meaningful or surprising that can be calculated here? What if the behavioral state is also read out from the population? Does the reliable shift in representation by behavior have any particular illusory effect, meaning does this create errors in a particular direction in visual space that could serve some functional purpose?

(2) What should one expect from this kind of analysis if a sensory task is novel or otherwise engages behavioral states more explicitly? Could the work be extended to comment on how to disentangle slow learning signals from the low-D modes that were found to be engaged by behavioral shifts?

(3) The figures, especially Figure 1, are dense and somewhat unintuitive. It would be nice to see a diagram of the analysis and main results first. This could engage a wider readership. Throughout the figures, it feels like there might be more visually impactful ways of representing the results. Instead, the figures feel repetitive, even though they are highlighting different effects and analyses.

Reviewer #2 (Recommendations for the authors):

1. Contribution of behavior vs. elapsed time: Given that it is already well-established that behavioral variability contributes to variability in neuronal responses (e.g. Niell and Stryker, Neuron 2010; Polack et al., Nat. Neurosci. 2013; Vinck et al., Neuron 2015; Musall et al., Nat. Neurosci. 2019; Stringer et al., Science 2019), it is not clear if the authors try to make the case that drift is an artifact of behavioral variability – i.e. drift is not a genuine phenomenon, it's all behavioral – as the abstract and main text strongly suggests by using the words "mistaken" and "misinterpreted"; or that behavior and time can both contribute to the observed changes in representations. These are two different messages that require a different set of analyses and will likely impact the field very differently, so it is crucial to clarify this point.

The authors state that "our results suggest that a significant fraction of what has been described as representational drift in a sensory cortex can be attributed to behavioral variability". However, quantifying the contribution of behavioral variability to representational drift (as the title of the paper claims) requires analysis that controls for the effects of the passage of time, and this was not done in this paper.

It is hard to conclude that both time and behavior modulation contribute differently to representational similarity of different presentations of the same video as the two analyzed video blocks are both well separated by time and differ in terms of the animal's behavior (quantified by pupil width and running speed). This will result in a correlation between time and behavioral changes that preclude the possibility to differentiate between the unique contribution of time and behavior to representational similarity.

One way to quantify the contribution of behavioral variability to representational similarity, is to repeat the analyses of Figure 1 and Figure 4, – i.e. the calculation of the correlation between the absolute change in the behavioral variables and the values of the chosen metric for representational similarity, while holding the interval between video repeats as a constant (subsequent video repeats within the same blocks or video repeats with the same absolute interval between them in general).

Alternatively, the authors can calculate and report the correlation between the change in behavior and representational similarity either between video repeats within or between video repeats across blocks. To control for the effects of time, the authors should separately calculate the linear relationship between the variables using only the light and dark gray data points (within block), and only the orange data points (between blocks), instead of the correlation indicated in red which uses the entire dataset. Additionally, the authors should report the statistics of these correlations (the p-value and the number of samples) in the corresponding figure legend.

The authors are suggesting that changes in representational similarity that were previously attributed to time are in fact only changes in the animal behavior over time. This could be tested using a multivariate regression analysis within each individual animal and quantifying the unique contribution of each variable (e.g., time, pupil size, running speed, etc.) as well as testing the significance of each variable to the fitted model, e.g. using GLM (see Driscroll et al., Cell 2017; Musall et al., Nat. Neurosci. 2019 for a similar approach).

Furthermore, if the authors are suggesting that representational drift merely reflects gradual changes in behavior, then it would be convincing to show that when the same analyses (e.g. multiple regression) are performed on a different set of stimuli with less abrupt changes in the behavioral state of the animals then there is no significant decrease in representational similarity. To do that, the authors can try to compare the similarity between the representations (for both population-vector correlations and setpoint similarity) across blocks in which the behavior didn't change significantly, and show there is no significant decrease in representational similarity. For example, the authors report in Figure 6 that there is less variability in behavior across blocks of drifting gratings and that there is no consistent and significant change in the behavior across the population of mice. Therefore, one way to test if there is higher representational similarity within blocks compared with across blocks (i.e., representational drift) without changes in behavior is to select mice that didn't exhibit behavioral changes across blocks and perform the analyses on them. This should also be done on the two blocks of 'Natural video 3', which are more proximal in time and therefore are likely to be more similar in behavior.

2. Cases of non-linear/monotonic relationship between behavioral changes and representational similarity and inappropriate use of correlation: In three of the main figures (specifically: Figure 1B, C, F, G, Figure 3C, I, and Figure 4C, D, G, H) the authors are using Pearson's correlation to quantify the relationship between the absolute change in pupil width between two video repeats and the representational similarity between the same repeats. In many of the plots, the data should not be fitted using Pearson's correlation since some of the assumptions of this model are not met. The most concerning issue is that the relationship between the two variables (change in behavior and representational similarity) does not always follow a linear or even a monotonic trend. This suggests that the relationship between the changes in pupil width and representational similarity are not correctly captured using a univariate linear model (e.g., Pearson's or Spearman's correlations). Additionally, in many of the plots, the data points fall into two or more dense clusters. This can lead to the false impression that there is a strong monotonic relationship between the two variables, even though there is a weak (or even opposite) relationship within each cluster (e.g., as in Figure 3 C, I and Figure 4G) (see an example in Aggarwal and Ranganathan, Perspect Clin Res 2016). This is a crucial point since the clusters of data points most likely represent different blocks that occurred at different times. Likewise, in Figure 5A, C, D, F right panels (and Extended Data Figure 10B, F), excluding the middle-range data points – which are the majority of data points – is unjustified and the use of Pearson's correlation in this case is inappropriate and misleading.

3. Stimulus dependent representational drift: A key statement of the current manuscript is that slow and gradual changes in behavior may change the setpoints (activity rates) of different neurons over time, leading to the appearance of a gradual decrease in representational similarity metrics such as 'population vector correlation' even in brain areas that do not, (literary) represent (or encode) the presented stimuli. This point was raised both as a critical evaluation of the representational similarity metrics chosen in the past to characterize the stability of visual representations or as a criticism of the use of the term 'representational drift'.

The fact that there are changes that are not purely related to the tuning of cells is not new and was demonstrated in several previous studies on coding stability. For instance, Ziv et al., Nature Neurosci. 2013 and Gonzales et al., Science 2019, have shown that place cells in the mouse hippocampal CA1 can drop in and out of the ensemble during different visits to the same familiar environment over weeks, leading to a gradual change in the population of place cells that encode the location of the animal during the task. These changes, which reflect changes in activity rates, were independent of the position the neurons encode and were found in place cells and non-place cells alike. Likewise, Driscoll et al., Cell 2017 and Aschauer et al., Cell Reports 2022, showed a similar turnover of the active cells in the cortex. Notably, Rubin et al., eLife 2015, showed that hippocampal representations of two distinct environments (which had very distinct place-cell representations) co-evolve over timescales of days-weeks. This shared component of the drift stems from gradual context-independent changes in activity rates. In fact, the prevalent use of the term representational drift (coined by Rule et al., Curr Op in Neurobiol 2019) is based on these above-mentioned studies and served to capture the entire range of gradual changes in neuronal activity over time. More recently, Schoonover et al., Nature 2021, and Deitch et al., Current Biology 2021 separately analyzed changes in activity rates and changes in tuning, and showed gradual changes in the cells' activity rates during periods of spontaneous activity, explicitly stating that these changes can occur independently of the presented stimulus.

Crucially, cells' activity rates are very relevant to stimulus encoding, as cells exhibit 'rate remapping' between environments or stimuli. Thus, equating stimulus-independent changes and changes in activity rates (setpoint similarity) is problematic because part of the changes in activity rates can be stimulus-dependent. This can be seen even in the visual cortex by calculating the setpoint similarity between different stimuli (e.g. Deitch et al., 2021 Figure S3H): the average activity rates of blocks of the same stimuli are more similar than between blocks of different stimuli. Thus, code stability is a function of two key factors: (1) stability in tuning and (2) stability in activity rates. Deitch et al., 2021 showed that the gradual changes over time that occur with respect to these factors are nearly independent of each other.

Furthermore, the fact that there are changes in setpoint similarity in CA1, although this area doesn't reliably encode visual stimuli, cannot, in itself, be used as an argument for the role of behavioral changes in representational drift since these changes can also be associated with elapsed time (see our point #1 above).

Overall, we agree that it is important to carefully dissociate between the effects of behavior on changes in neuronal activity that are stimulus-dependent or independent, but we feel that the criticism raised by the authors ignores the findings of the relevant literature, which (1) did not purely attribute the observed changes to the sensory component, and (2) did dissociate between stimulus-dependent changes (in tuning) and off-context/stimulus-independent changes (in activity rates).

We propose that the authors tone down their interpretations throughout the paper, and especially in the discussion: e.g., "changes in representational similarity (i.e. representational drift) can arise from changes in both sources, and hence attributing it purely to the drift of the sensory component might be inaccurate" and "Drawing further conclusions about stimulus-dependences of representational drift in visual cortex – and other sensory cortices – thus needs a critical evaluation by teasing apart the contribution of different components (stimulus-induced and stimulus-independent)".

4. The use of the term "Representational similarity" versus "Representational drift":

It is important that the authors explicitly define the term representational drift and edit the paper in a way that uses the terms "representational similarity" and "representational drift" in a consistent way throughout the manuscript. Most studies have demonstrated drift (even if not using the term 'drift') as a decreasing similarity between neuronal responses to the same stimulus/task as a function of the time interval between experiences/stimulus presentations under the same experimental conditions (Ziv et al., Nat. Neurosci. 2013; Lee et al., Cell 2020, Driscoll et al., Cell 2017; Rule et al., 2019; Schoonover et al., 2021; Deitch et al., 2021; Marks and Goard et al., Nat. Comm. 2021; Jensen et al., BioRxiv 2021 and Aschauer et al., Cell Reports 2022). This point regarding the differences between drift and variability in neuronal responses is nicely illustrated and discussed in a recent review paper (Clopath et al., Philos Trans, 2017). However, throughout the current manuscript, the authors refer to any change in representational similarity as representational drift and use these terms interchangeably regardless of the interval between the compared timepoints. For example:

"…Importantly, changes in representational similarity (i.e. representational drift)…"

In most of the above-mentioned studies about drift, the behavior or performance of the animal was at a steady state throughout the examined time intervals, suggesting that the observed changes in neuronal activity are not due to gradual changes in the behavior (e.g., due to learning, habituation, or changes in arousal). Thus, while the behavior itself may vary across different time points, as long as it is not changing gradually throughout the experiment, it should not lead to the appearance of drift.

To determine whether neuronal representations are gradually changing, there must be at least three (not necessarily equally spaced) different compared time points (see Clopath et al; 2017). We suggest adding a paragraph that explicitly explains the difference between neuronal variability and drift, how to differentiate between the two cases, and including an additional time point in the illustration presented in Extended Data Figure 1A (which now only includes two times points).

5. Focusing on reliable units improves time-lapse decoding: The analysis presented in Figure 7 shows that using reliable units (i.e., units that don't show changes in their tuning over time) results in higher decoding accuracy (i.e. more stable population code). Given that stability at the single-cell level should directly contribute to stability at the population level, this analysis is circular and therefore the conclusion that "Decoding generalizability of natural images improves by focusing on reliable units" is trivial.

Irrespective of this issue, we agree that it is a reasonable idea that reliable units could serve as a stable core for the brain to rely on for coping with changing neuronal responses. However, the distribution of stimulus reliability is not bi-modal (as shown in Figure 2H), but actually skewed towards lower reliability values. Thus, it is unclear how focusing on a small, unrepresentative subset of reliable units informs us how the brain copes with changing representations.

Reviewer #3 (Recommendations for the authors):

– In the introduction it may be useful to provide working definitions of (and differences between) "drift of behavioural state", "behavioural drift" and "behaviour".

– To rule out any potential artifact resulting from bin width choice being correlated with behavioral timescale, it would be useful to see the effect of varying bin width in computing population vectors.

– The Siegle et al. dataset methods imply that pupil position is available as well; thus do the same results apply if using position in addition to diameter? It would be nice to mention if any other behavioural measures are available that were not analyzed, as ignoring these seemed to lead previous accounts of drift astray.

– Pg. 5 bottom paragraph: "Inclusion of multiple cell types…to control for this…" – this control actually seems to be for possible strain differences; it is not clear in the Siegle at al. dataset how many cell types were presented (i.e. which cells were opto-tagged), so this information should be present if discussed.

– In the discussion of Figure 6, there is a nod to the expected results if pupil diameter correlation was used as a separate measure of behavioural tuning, which references Figure 6 b,e (pg. 13..should be Figure 5b,e?).

– Pg.19 "in line with previous reports" should be "in line with a previous report" unless more citations are provided.

– Pg. 20 "with a more decrease in pupil size" should be "with larger decreases in pupil size" or similar.
