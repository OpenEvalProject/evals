# Peer review - Round 1

Editors:
- Tatiana Pasternak, University of Rochester United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.35123.024](https://doi.org/10.7554/eLife.35123.024)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Optogenetically induced low-frequency correlations impair perception" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The paper examined whether optogenetically induced increases in spike count correlations in V4 neurons affect the ability of macaque monkeys to detect small orientation changes of Gabor gratings. The authors report that the optogenetic stimulation in the low but not high frequency range affected performance and this effect was limited to the attended location, concluding that the attention induced reduction of low frequency spike count correlations results in improved performance.

The reviewers commented on the ambitious nature of the work and its potential importance, but raised a number of serious reservations that must be addressed for the paper to be further considered for publication in eLife. These are summarized below.

Essential revisions:

1) Anatomical evidence confirming that the neurons were actually transfected should be provided. This includes the information about the affected cell type, their layer locations and variability of the expression.

2) Variable performance on the orientation change task makes it difficult to interpret the effects of optogenetic stimulation. This problem should be addressed.

3) The presence of on- and off- transients in visual stimulation occurring at a frequency of 3-5Hz creates a potential problem in the study aimed at detecting correlations occurring at similarly low frequency. It is important to rule out that optogenetic stimulation may be affecting the detection of the onsets and offsets of visual stimuli. Reviewer 1 suggests a control condition that would eliminate such transients to see whether optogenetic manipulation is still selective for low frequencies.

A related question (reviewer 2) concerns the phase of optical stimulation relative to stimulus presentation whether the presence of the behavioral deficits depended on the phase of optical stimulation. Also, provide information about the phase of optical stimulation used to compute noise correlations

4) Data presentation limited to averages and distributions does not allow the evaluation of significant effects in each experiment. The data suggest that in some cases optogenetic stimulation resulted in elevated thresholds and slopes and in some cases in opposite effects. This is a problem that needs to be addressed and discussed.

5) Please provide a direct comparison between firing rates with and without optical stimulation, showing effects on individual neurons. Rate modulation index does not allow the reader to assess such effects directly.

6) Was orientation tuning affected by optical stimulation? If they were, the disruption of orientation representation in V4 by stimulation could potentially explain the behavioral effects. This should be addressed.

7) Please explain cued and uncued locations vs. "catch trials" and their randomization during the experiment (reviewer 1).

Reviewer #1:

The goal of this paper is to causally test the idea that low-frequency oscillations amongst cortical neurons are a major limiting factor in visual perception and are actively controlled for visual attention. The strategy is a bold one – use optogenetics to introduce low-frequency correlations into the activity of cortical neurons in extrastriate area V4 and document the effects on both visual perception and neuronal activity. If the idea is correct, then the introduction of low-frequency correlations should impair performance. But there are many reasons that performance might be impaired when you alter visual cortical activity. So it is also necessary to show that visual activity has not simply been disrupted by the optogenetic manipulation, and that it is specifically the temporal restructuring of the activity that is crucial. To this end, the paper shows that overall firing rates are not changed, and that the effects are found only with low-frequency and not high-frequency stimulation, among other controls.

This is an ambitious set of experiments to attempt to pack into a short paper, especially given all of the potential pitfalls and controls that need to be considered. In the end, I was not fully convinced that the results as presented support the conclusions. There are several basic issues that need to be addressed to make the case more convincing. I also think that a more detailed unpacking of the data is need in order to understand the results.

The most obvious missing piece is histology. Figure 1C shows a surface view of the cortex illustrating the expression of EYFP. This is not sufficient to answer the questions relevant for interpreting the behavioral and neuronal data. Can you confirm that neurons were transfected? Which types of neurons, and in which layers? How variable was the expression across layers? Can you rule out retrograde transfection from axon terminals? Without histology to verify what was stimulated, I find it difficult to interpret the results.

Performance in the orientation change task seems extremely variable, to the point that it raises concerns about how to interpret changes in task performance. In some cases, the thresholds for detecting orientation changes seem to be in the expected range (a few degrees) – for example, Figure 2B and Figure 2—figure supplement 2A. But in other cases, the thresholds are unusually high, 10 degrees or more (Figure 2—figure supplement 2C). There are also unexpected elevations in% correct for signal values that should be below threshold – for example, 40% correct for the lowest orientation change value in Figure 2—figure supplement 2B. How could the monkey get 40% correct for an undetectable signal? In order to interpret the optogenetic manipulation, I would need to be reassured about the reliability of task performance in the absence of optogenetic manipulation.

There is a very basic aspect of the experimental design that seems like a problem, but perhaps the authors have a very well-reasoned explanation for this approach. The hypothesis is that low-frequency (4-5 Hz) correlations play a central role in cortical processing, and this guides the choice of sinusoidal optogenetic stimulation. But the stimulus itself is flashed on for 200 ms and then left off for 200-400 ms, which means that there were visual transients (on or off) also occurring at a frequency of 3-5 Hz. If the goal is to test the importance of intrinsic low-frequency correlations, why use a stimulus that includes transients in this same frequency range? It seems that an alternative explanation for the perturbations in performance might be that the optogenetic stimulation masks the ability to detect the onsets and offsets of the visual stimulus. Can this be ruled out? If the stimulus were simply left on for an extended period of time (seconds), and then changed orientation, would the optogenetic manipulation still be effective and still selective for low frequencies?

The data were compressed for presentation in ways that made it difficult to understand what additional significant effects might be present in each experiment. Figure 2C is a good example of this. The histogram illustrates that, overall, both the threshold and slope increased in trials with low-frequency optical stimulation, by showing that the population-level ratio of stimulation relative to baseline is significantly greater than 1. First, please clarify the stats (here and elsewhere). This is reported as a t-test in the fourth paragraph of the Results and Discussion. Which type – paired sample? Is the distribution normal, or should a non-parametric test be used? Second, please report the data in a way that allows us to appreciate what happened on individual experiments. Given the scale on the x-axis, it looks like optical stimulation may have caused significant increases in threshold or slope in some experiments and significant decreases in others. If so, it would be misleading to base the conclusion on the average effect. This point is especially relevant for the attend away condition (Figure 2D), in which the average threshold is not different, but the spread in the histogram suggests that many individual experiments were significant but roughly equally split between increases and decreases.

I had similar concerns about the neuronal data in Figure 4. In addition to plotting the rate modulation index, please directly compare the firing rates with and without optical stimulation. Was the firing rate significantly changed for individual neurons? The effects of attend-in and attend-away should be similarly documented across the population of neurons. Did optical stimulation significantly change this modulation for individual neurons? The concern here is that there may be no difference on average, but a more or less balanced combination of significant increases and significant decreases.

Beyond changes in firing rate, it is also possible that the optical stimulation disrupted the tuning properties of the neurons. Do you have data to confirm that the orientation tuning and receptive field properties of the neurons was not changed during optical stimulation? If the claim is specifically about the role of low-frequency correlations, it is important to rule out the possibility that behavioral effects were due simply to disrupting the representation of orientation information in V4.

Reviewer #2:

Nandy and colleagues investigate whether optogenetically induced increases in spike count correlations in V4 neurons affect the ability of macaque monkeys to detect small orientation changes of Gabor gratings. The find that this is indeed the case, but only if the optogenetic stimulation is in the low frequency range (4-5Hz, sinusoidal modulation), not when it occurs at higher frequencies (tested were 20 Hz). This only occurred when the neurons stimulated represented the attended (instructed) location, not when the represented the non-instructed location. The authors conclude that the attention induced reduction of low frequency spike count correlations indeed convey behavioural benefits.

This is an interesting study, but I have a few questions:

I was unable to determine whether the phase of stimulation was fixed relative to stimulus presentation. Probably not as stimulus presentation varied within a trial. This means that orientation changes would occur at variable phases of optogenetic stimulation. If so, it will be important to know whether behavioural deficits occurred equally across different phases, or whether they were co-modulated.

The histograms show and the noise correlations also seem to be calculated over different optogenetic phases (if my assumption from above is correct). It will be important to determine whether there were changes in either when calculated for different optogenetic phases. If so, these need to be documented in detail.

The authors state that no effect was seen in the attend away condition. Was that even true on catch trials (i.e. attend away, but change occurs at RF)? If so, it needs to be explained why.

Why was the higher frequency in the beta range, not in the gamma range, where some people might expect to see behavioural benefits to occur?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for submitting your article "Optogenetically induced low-frequency correlations impair perception" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Eve Marder as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The reviewers acknowledged your efforts to address the comment raised in their initial review. However, a number of issues remain and those undermine their confidence in the main conclusions of the paper. These must be addressed for the manuscript to be considered for publication in eLife. The points listed below are based not only on the reviews attached below, but also on the discussion among the reviewers that followed.

Essential revisions:

1) Lack of histology

The reviewers felt that the lack of histology seriously complicates the interpretation of the results but are willing to accept a possibility that the expression patterns of the viral vector in V4 are the same as those shown for V1 in the previous publication from the lab. However, you should add appropriate disclaimers about the assumptions about transfected neurons (based on the published V1 data), and discuss how your interpretation would be affected if these assumptions turn out to be incorrect.

2) Variability in orientation thresholds

The reviewers felt that the explanation attributing variability to the difference in thresholds for oblique and cardinal orientation, needs stronger documentation. To that end, rather than providing 8 example psychometric functions, the relationship between base orientation and performance should be documented by plotting thresholds for each of the sessions as a function of orientation.

3) Potential confound of visual and optogenetic stimulation delivered at similar low frequencies

Reviewers did not feel that the phase analysis included in the revision adequately addressed the problem. Reviewer 2 commented that while the overall effect may not be phase-specific, it may be specific "to cases where the optogenetic frequency is similar to the stimulus onset/offset frequency". Please provide additional information, to address this.

Please address the absence of label for the x-axis in Figure 4—figure supplement 3B and different sign of effects on threshold and sensitivity. One of the reviewers suggests sorting the experiments into subsets based on how the psychometric curves change (for example, based on where the experiments fall in Figure 2—figure supplement 5).

4) Changes in thresholds and slopes

The summary plot (Figure 2—figure supplement 5) reveals not only increases in threshold (22/42 cases) but also decreases in threshold (~14 cases). Please address the apparently opposite effects produced by stimulation.

In addition, it appears that stimulation increased the slope more often than decrease it. Since the increase in slope is likely to be associated with an increase in sensitivity, the proposed role of decreased correlations in improving the separability of neuronal activity is puzzling. This effect appears inconsistent with the proposed interpretation of the changes in spike-count correlations with stimulation. The reviewers suggest that you link the measured changes in correlations with the observed changes in psychometric functions by using a decoding scheme similar to that used by Cohen and Maunsell, 2009. This approach would allow you to predict the changes in psychometric curves given the changes in spike-count correlations.

5) Orientation tuning

Please provide additional information concerning the Figure 4—figure supplement 4 scaling on the x-axis and pooling data across neurons. How were the neurons used for this analysis selected? (see comment from reviewer 1).

6) Please provide documentation of false alarm rates from catch trials with and without optogenetic stimulation (see comment from reviewer 1).

7) The phase locking of spikes to the phase of stimulation should also be shown during the stimulus, in addition in the absence of stimulation.

8) The effect of optogenetic phase on behavior should be aligned with the preferential population activity, which seems to peak/trough at 240° and 60° respectively.

9) Please clarify what statistical test was used to determine that the phase of optical stimulation did not affect behavior or orientation tuning

Reviewer #1:

In my comments below, for clarity I repeat the original comments in quotes, with my new comments inserted after each item.

Overall, the authors have made efforts to address each major comment, but have been prevented from fully settling several of the points due to technical limitations. Some of these are substantial points that affect my confidence in the main conclusions.

"The most obvious missing piece is histology. Figure 1C shows a surface view of the cortex illustrating the expression of EYFP. This is not sufficient to answer the questions relevant for interpreting the behavioral and neuronal data. Can you confirm that neurons were transfected? Which types of neurons, and in which layers? How variable was the expression across layers? Can you rule out retrograde transfection from axon terminals? Without histology to verify what was stimulated, I find it difficult to interpret the results."

The authors do not have histology for the two monkeys used in the study but they show a figure from a previously published study using the same viral vector injected into cortical area V1.

Will the expression patterns be the same in V4, the area targeted in this study? I don't know, and I don't know of any published work using this vector in macaque V4. Apparently, there is tissue from one of the monkeys (that was sacrificed) from this study; even if the tissue is damaged due to penetrations it should be possible to identify transfected cells, and the approximate size and layer distribution. It is not clear what steps were taken along these lines, or if that tissue was unfortunately discarded.

"Performance in the orientation change task seems extremely variable, to the point that it raises concerns about how to interpret changes in task performance. In some cases, the thresholds for detecting orientation changes seem to be in the expected range (a few degrees) – for example, Figure 2B and Figure 2—figure supplement 2A. But in other cases, the thresholds are unusually high, 10 degrees or more (Figure 2—figure supplement 2C). There are also unexpected elevations in% correct for signal values that should be below threshold – for example, 40% correct for the lowest orientation change value in Figure 2—figure supplement 2B. How could the monkey get 40% correct for an undetectable signal? In order to interpret the optogenetic manipulation, I would need to be reassured about the reliability of task performance in the absence of optogenetic manipulation."

The authors explain that this is probably due to differences in detection performance – in particular, thresholds were lower for baseline orientations near the cardinal (i.e., horizontal and vertical) orientations. They show 8 sample psychometric curves that are consistent with this explanation.

This seems plausible, but the author should show it holds true for the other 34 sessions as well. If you simply plot threshold for each session as a function of the baseline orientation, this would show whether the variance was indeed systematically related to the baseline orientation.

"There is a very basic aspect of the experimental design that seems like a problem, but perhaps the authors have a very well-reasoned explanation for this approach. The hypothesis is that low-frequency (4-5 Hz) correlations play a central role in cortical processing, and this guides the choice of sinusoidal optogenetic stimulation. But the stimulus itself is flashed on for 200 ms and then left off for 200-400 ms, which means that there were visual transients (on or off) also occurring at a frequency of 3-5 Hz. If the goal is to test the importance of intrinsic low-frequency correlations, why use a stimulus that includes transients in this same frequency range? It seems that an alternative explanation for the perturbations in performance might be that the optogenetic stimulation masks the ability to detect the onsets and offsets of the visual stimulus. Can this be ruled out? If the stimulus were simply left on for an extended period of time (seconds), and then changed orientation, would the optogenetic manipulation still be effective and still selective for low frequencies?"

The authors agree these are important potential confounds but for technical reasons, they are not able to do the control experiment in which the stimulus is simply left on, to test whether the optogenetic stimulus might be masking the visual onset and offsets that occur in the same frequency range.

The phase analysis is interesting, but does not address the same point exactly. I wouldn't necessarily expect the effect to be phase-specific, but I do suspect it might be specific to cases where the opto frequency is similar to the stimulus onset/offset frequency. This question remains open.

Some comments about Figure 4—figure supplement 3B: What is the x-axis and why is it unlabeled? There seem to be some interesting possible mixed effects at low delta orientations. If you pool across all sessions (with different sign of effects on threshold and sensitivity) perhaps some effects are getting averaged out. Have you tried sorting the experiments into subsets based on how the psychometric curves change (for example, based on where the experiments fall in Figure 2—figure supplement 5)?

"The data were compressed for presentation in ways that made it difficult to understand what additional significant effects might be present in each experiment. Figure 2C is a good example of this. The histogram illustrates that, overall, both the threshold and slope increased in trials with low-frequency optical stimulation, by showing that the population-level ratio of stimulation relative to baseline is significantly greater than 1. First, please clarify the stats (here and elsewhere). This is reported as a t-test in the fourth paragraph of the Results and Discussion. Which type – paired sample? Is the distribution normal, or should a non-parametric test be used? Second, please report the data in a way that allows us to appreciate what happened on individual experiments. Given the scale on the x-axis, it looks like optical stimulation may have caused significant increases in threshold or slope in some experiments and significant decreases in others. If so, it would be misleading to base the conclusion on the average effect. This point is especially relevant for the attend away condition (Figure 2D), in which the average threshold is not different, but the spread in the histogram suggests that many individual experiments were significant but roughly equally split between increases and decreases."

The authors now provide a summary plot (Figure 2—figure supplement 5) that summarizes the changes in threshold and slope. This is helpful. It shows that in addition to the main effect reported in the paper – the increase in threshold seen in 22/42 cases – there is also sometimes a significant decrease in threshold (~14 cases). Any ideas about why the effect flips sign in these cases?

More curiously, and harder to understand, the stimulation also tends to increase the slopes more often than it significantly decreases the slopes. An increase in slope would imply that the sensitivity of the monkey during the stimulation had increased. Given the proposed role of decreased correlations in improving the separability of neuronal activity, shouldn't the main effect have been a decrease in slope?

"I had similar concerns about the neuronal data in Figure 4. In addition to plotting the rate modulation index, please directly compare the firing rates with and without optical stimulation. Was the firing rate significantly changed for individual neurons? The effects of attend-in and attend-away should be similarly documented across the population of neurons. Did optical stimulation significantly change this modulation for individual neurons? The concern here is that there may be no difference on average, but a more or less balanced combination of significant increases and significant decreases."

The authors have added a Figure 4—figure supplement 1 that compares the spike rates for all neurons with and without optogenetic stimulation, and report no significant change in firing rate due to stimulation. I find this set of figures very convincing.

"Beyond changes in firing rate, it is also possible that the optical stimulation disrupted the tuning properties of the neurons. Do you have data to confirm that the orientation tuning and receptive field properties of the neurons was not changed during optical stimulation? If the claim is specifically about the role of low-frequency correlations, it is important to rule out the possibility that behavioral effects were due simply to disrupting the representation of orientation information in V4."

The authors respond that they did not measure tuning curves. However, they do have data from the non-target orientation and some target orientations, which they report in Figure 4—figure supplement 4. I find it difficult to evaluate this plot because I don't understand the scaling on the x-axis or how data were pooled across neurons. It is also not clear that data from all neurons should be included in this analysis, unless their activity was strongly modulated across the range of orientations used (i.e., the data indicate direction tuning over the domain tested). And then the data might be aligned on the x-axis so that 1 value corresponded to the "best" direction.

The issue of possible changes in neuronal tuning is critical for interpreting the results. Perhaps the authors can do more to address this.

"There was some ambiguity in the description of how the orientation change in the stimulus was managed. The paper describes a 95% probability at the cued location and 5% at the uncued location. But then there were also "catch trials" without any change. It's not clear how these add up. Were the 95% and 5% independent? What was the probability of a catch trial? Were these truly randomized, or were they presented in as a fixed fraction of the trials?"

The authors now explain their definition of 'catch' trials.

Are the FA rates on from catch trials documented somewhere in the paper? I did not see it except for Figure 2—Figure supplement 2A, which curiously appears to show a false alarm rate on catch trials of about 50% Is this correct? How can the FA rate be that high when the hit rate drops well below that for small orientation changes? I would expect the FA rate to be the floor for the curve.

Aside from trying to understand the plots, the other reason for asking about FAs is to know whether the FAs also changed with optogenetic stimulation. This would be important for assessing possible changes in response criterion, which would also be important to nail down, since changes in criterion could also shift the psychometric curves

Reviewer #2:

The authors have addressed some of my previous points, but I have a few issues remaining:

They describe the phase locking of spikes to the phase of stimulation when no stimulus was present. However, it would be important to see this also for the stimulus period.

The authors use 4 bins to calculate the effect of optogenetic phase on behaviour, but these are not aligned with the preferential population activity alignment, which seems to peak/trough at 240° and 60° respectively. This needs to be done.

It is unclear what statistical test was used to determine whether behaviour was unaffected by the phase of optical stimulation?

The same is true for the effect on orientation tuning.

In general, statistical reporting should be checked and adequately improved.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for submitting your article "Optogenetically induced low-frequency correlations impair perception" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Eve Marder as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The revised manuscript has addressed most of the reservations raised by the two reviewers. There remain only a few issues that need the authors attention. These are listed below.

Essential revisions:

1) Please substitute multiple t-tests with ANOVA to reveal potential interactions.

2) Please address the point concerning correction analysis, raised by reviewer 2.

3) Please include the figure from Essential Revisions #3 as a supplementary figure. Also include: a) the average firing rate traces for each of the 4 flashes, and b) confirm the behavioral effects for the low-frequency but not high-frequency stimulation.

Reviewer #2:

The authors have also performed the analysis relating to the NDMI and PDMI. They report a significant negative correlation, between the two. Looking at Figure 5 this seems to be driven by 5/42 experiments. They do not report what type of correlation was calculated (Pearson? Spearman? Robust correlation to control for outliers?). I think a robust correlation would be appropriate, while given the distribution of data I assume Pearson is inappropriate. They also present a line, which I assume is a slope of a linear regression? Given that NDMI and PDMI are dependent variables, slopes need to be calculated of x vs. y and y vs. x, and then the average slope needs to be taken.
