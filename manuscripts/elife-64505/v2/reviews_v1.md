# Peer review - Round 1

Editors:
- Adrien Peyrache, McGill University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64505.sa1](https://doi.org/10.7554/eLife.64505.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper presents a new framework to decode neuronal activity in the hippocampus during ripple events. This method reveals that most ripple events contain spatially interpretable content that often progresses at timescales slower than previously reported and that appears to better match previous wake activity at real time. These findings challenge the classical view of replay as primarily time-compressed representation of previous wake activity and provide a fuller picture of the repertoire of possible content for ripple events during rest.

Decision letter after peer review:

Thank you for submitting your article "Hippocampal replay of experience at real-world speeds" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Timothy Behrens as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Yunzhe Liu (Reviewer #1); H Freyja Ólafsdóttir (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In the present study, the authors report that the proportion of candidate replay events in the hippocampus showing spatially interpretable content is much higher than previously described. In addition, these events often progress at slow ("real-world") timescales while it is generally assumed that hippocampal replay is compressed in time. Specifically, the authors have used a state space model that captures the spatial content and temporal evolution of replay. This model is based on few assumptions and is aimed to be unbiased – as it is based on "clusterless" extracellular spikes. While the three reviewers are generally enthusiastic about the work and agree that this study is potentially suitable for eLife, they have raised several concerns that should be addressed to warrant publication. The main concerns are summarized below, please refer to the detailed reviewer's comments for more information.

Essential revisions:

1. The authors should further test their method on exploration data to validate the approach, especially since non place cells may potentially bias the decoding of animal's speed in clusterless data (see reviewer #3 point #1). This analysis of hippocampal activity during run can be used to identify the encoded speed in within theta sequences (reviewer #1, point #2).

2. The authors have to improve controls, especially their shuffling procedures. Shuffling the spike-location relationship is too permissive. See reviewer #2, point #1 and reviewer #3, point #9.

3. The authors should use more stringent thresholds on speed and theta power to rule out the possibility that some of the events are not replays but represent current position. See reviewer #2, points #2-3.

4. The classification of candidate replay events should be improved (especially events that may be partially "unclassified") and the authors should provide a more detailed comparison of the replay events detected with their method and with previously described methods (reviewer #3, points #2-3)

5. The authors should provide descriptive statistics demonstrating that spiking properties during candidate replay events (e.g. average rate per tetrode) are similar between sorted and clusterless data (reviewer #3 point #6-7). Only events in which spikes are detected on multiple tetrodes should be included, to prevent decoding from the firing of a single cell. Finally, spikes of putative inhibitory neurons should be discarded (reviewer #3, point #7).

6. The authors have used neuronal data collected from the different subcircuits of the hippocampus (CA1-3). It should be demonstrated that the main results hold if the analysis is restricted to CA1, on which most of previously published studies are based, especially since it can affect the nature of replay events. Is there a relationship between the category (e.g. continuous or stationary) of a given replay event and the proportion of neurons from the different substructures that fired during that event? Also, discussing the seemingly low proportion of continuous events (if the same proportion is observed when only including CA1 neurons). See reviewer #2, point #4 and reviewer #3, points #4-5.

7. The title of the manuscript is a bit misleading as the reported replayed speeds are often even slower than "real-world speed" and should therefore be changed. See reviewer #1, point #1 and reviewer #3, point #8.

8. The authors should further discuss the implication of their findings. See reviewer #1, point #3 and reviewer #2, point #4.

9. Please note that reviewer #3 has also raised a couple of minor concerns that should be addressed.

Reviewer #1:

Denovellis et al. have developed a state space model approach for unbiased replay detection. As a result, they are able to demonstrate that most of the candidate replay events (i.e., sharp wave ripple events) contains spatial coherent (stationary or continuous) content, and they progress at a relative lower speed (< 1m/s) than previously believed.

I like this paper a lot. The writing is very clear, and the analysis is thorough. The proposed method is likely to be very impactful and widely adopted in the replay community.

Reviewer #2:

Denovel and colleagues develop and apply a state space model to decode position representation during hippocampal SWR events. The main advantage of this model is that is makes fewer assumptions of the dynamics of SWR events allowing it capturing varying and mixed movement dynamics. Through the application of this model the authors are able to decode coherent spatial content from the vast majority (~90%) of SWR events – a much, much higher proportion than previous papers on the topic have reported – and they show that, contrary to previous work, the most common type of movement dynamic during SWR events is one that's characterised by a stationary/slow movement speeds.

I believe the work by Denove and colleagues represents a significant advance in our understanding of SWR events. Moreover, the state space method Denove et al. described also represents useful analytical tool which could potentially be useful to many neuroscientists in the field. I would also like to commend the authors for their clear and detailed explanation of the model.

I do however have some concerns about the robustness of their SWR event method and some of their control analyses. Below I explain these in more details and suggest ways to address these concerns. All suggestions are implementable and would, I believe, significantly strengthen the authors' conclusions.

1. To control for spurious SWR events (containing spatially coherent content), the authors shuffle the position-spike relationship. Although this type of control analysis is commonly used, it can be overly permissive, particularly if researchers are working with small-to-medium samples sizes. This is because for smaller samples sizes it is unlikely that all positions are represented equally by the cell population (which is an assumption of the control analysis). However, given the authors are using clusterless decoding, a cell ID shuffle is not possible. Thus to address this potential caveat, it would be useful if the authors show position representation in their cell population on the W-maze? Moreover, if the position representation is not equal throughout the environment the authors need to account for this in their position resampling with replacement control analysis.

2. The authors use a speed threshold of 4cm/s to exclude SWR events that may occur during movement periods. Could the authors use a more stringent threshold – e.g. 1cm/sec or 0cm/sec? Although 4cm/sec is low I believe it is important to rule out the possibility that some of their detected spatially coherent SWR events don't merely reflect the movement of the animal during the event. This is particularly important given their finding that the most common type of replay event is one that is characterised by slow movement speeds – akin to those seen during actual behaviour.

3. Related to this, the authors could also use low theta power as an additional quality criteria to weed out events that may reflect (slow) movement periods.

4. One of the main findings of the paper is that SWR events can consist of different types of movement dynamics (stationary, continuous, fragmented) or a mixture of dynamics. This is indeed an interesting and novel finding, but it would be useful if the authors could elaborate on the theoretical implications of different type of replay events. For example, do the authors think SWR events belonging to different movement dynamic categories are supported by different sub-circuits within the hippocampus? For example, some work has shown SWR events preceded by EC activity are longer in duration Oliva et al. (2016).

Reviewer #3:

The authors of this study investigated the prevalence and range of representational dynamics associated with replay activity in the rat hippocampus during periods of rest following a spatial alternation task in a W-shape maze. Using a state space model that captures the spatial content and temporal evolution of replay during sharp-wave ripple activity, the authors report that most ripple events contain spatially interpretable content that often progresses at timescales slower than previously reported and that appears to better match previous wake activity at real time. The reported findings challenge the classical view of replay as primarily time-compressed representation of previous wake activity and build on previous work on stationary events and reduced proportion of significant trajectory replay events to provide a fuller picture of the repertoire of possible content for ripple events during rest. While the results are intriguing, a number of conceptual and technical shortcomings prevent a more enthusiastic appreciation of this work in its current state, as detailed below.

1. The main Bayesian model needs to be tested first during run on track, where the prior is being built. The authors need to compute the error of the model during run in terms of the difference between the decoded position during run and the actual animal trajectory. If, for any reason, the model appears stationary during run at any trial/lap, then the authors will need to take that into account when claiming stationarity during rest. In particular, clusterless decoding may make use of spikes that are not spatially well modulated and that would appear to support the stationary events during rest.

2. Please use more stringent classification of the events. As the current relaxed criterion for classifying events only requires a portion of the event to exhibit that behavior, what proportion of events classified as 'stationary' or 'continuous' significantly pass traditional, rigorous event-matched shuffles? What proportion of extended stationary events, >100 ms for instance, have a line-fit replay score above the 95th percentile of event-matched shuffles (circular shifting of posterior decoded probabilities) and a trajectory length shorter than a certain value, e.g. 6 cm? Similarly, what proportion of continuous trajectories pass their respective event-matched shuffles? What proportion of stationary events are entirely stationary? The authors need to quantify all of the above and present them in the Results.

3. One significant conclusion of this paper is that most population events during awake rest are stationary-continuous mixtures or stationary as opposed to continuous (replay) events. However, given that an event is classified as stationary if part of the event is stationary (probability >0.8), there is a possibility that the rest of the event is unclassified (no clear structure). In plots 3G, 5A-F it is important to include details about the unclassified ripples and the unclassified parts of the ripple which is otherwise classified. For instance, in 5A, the proportion of ripples with parts that are unclassified needs to be mentioned. This is important because parts of the event might be stationary, and parts might be noise/unclassified. Previous studies have characterized events as stationary only if they were stationary throughout the event and had excess stationarity than the 95th percentile of an event-based shuffle. How many of the events classified as stationary pass this significance criterion? This relaxed classification might otherwise lead to over-classification of certain event types.

4. The reported results are based on combined recordings from 3 hippocampal areas: CA1, CA2, and CA3 (conform Methods). These areas have different cell types, some of which respond to animal stationarity rather than movement. This makes classification and comparison of all event types between this study and the previous studies reporting on CA1 place cells only which were active on simpler tasks on linear tracks difficult. The authors should restrict their analysis to tetrodes located exclusively in CA1 when computing proportions of event types and only then compare their results to previous studies reporting on significant replay and stationary events. To make this comparison even more interpretable, similar significance tests against shuffles and use of clustered data (available for 9 out of the 10 animals that were previously published) should be performed. If the presented proportions of events persist under these conditions, the impact of the findings will be significantly increased.

5. There is discrepancy in proportion of replay events reported here compared to previous studies. Continuous events are most similar to traditionally detected replay sequences, however, those sequences are unidirectional (move from one side of the track to the other to be significant), while these events can move in both directions (model of movement dynamic is symmetric for continuous). The authors should investigate and explain why the proportions of continuous events are less than those of traditionally detected replay sequence events with event-matched shuffles (10-50% in other studies as stated by the authors versus ~5% only continuous).

6. The properties of each event type need to be compared to rule out other reasons for their distinct spatial and temporal dynamics. These properties to be compared between classes of event types (e.g. stationary, continuous, etc.) include: number of tetrodes active in the event, ripple power, total number of spikes in the event, spikes per bin, event duration, proportion of spikes under 6 ms ISI for each tetrode in each event type, proportion of the event duration it lies in that classification. Could you also confirm that population events included for clusterless decoding are similar in properties to those obtained from clustered data by comparing their properties (duration and z-scored population firing rates across the event)?

7. There is a possibility that one neuron dominates a population event and, therefore, stationary events are simply single units firing continuously. For instance, Figure 1A for the simulation shows just that, one simulated neuron fires and a stationary event is predicted by the algorithm. As clusterless decoding is used for the main analyses, can only events consisting of multiunit activity from at least 5 tetrodes be included in the analysis? Will the main classes of events be replicated under these conditions? Related to this, interneurons (putative inhibitory neurons) should be removed from the clusterless decoding based on waveform shape as there is a possibility that inclusion of interneurons in the clustering decoding analysis biases results towards detection of stationary events (there might be a hint of this from examples presented in Figure S4 where good stationary events seem to have higher spiking per tetrode compared to continuous events). The event classes should be recomputed and compared with the original classes.

8. The current title is misleading. There does not appear to be clear evidence of replay at real-world speeds. First, during each run lap, the animal trajectory changes unidirectionally at an estimated speed of 25-35 cm/s. For replay to occur at real time speed, the trajectory decoded during rest should fully unfold at the same speed over 3-4 s for a 1m-long track. This is never reported here, partly because the events are shorter. The stationary events decode individual locations, but there is no indication that they evolve in succession (successive locations at successive times) to represent trajectories at real time speeds. Second, neurons fire in time-compressed theta sequences during run, so neuronal activity is naturally compressed even before replay. Compressed replay essentially already represents space at roughly the same speed as during run (theta sequences).

9. Bursting of neurons or other individual neuronal properties might lead to classification of successive bins as spatially coherent and/or stationary. In order to control for that possibility, in clustered decoding researchers typically generate shuffled datasets with conserved place map properties by circularly shifting individual place maps. The shuffles generated in this paper randomize the position to spike relationship destroying all single-cell properties. Can shuffles with conserved tetrode multiunit activity properties be generated instead to test this hypothesis? E.g. circularly shift by the same value all spikes from the same tetrode.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Hippocampal replay of experience at real-world speeds" for further consideration by eLife. Your revised article has been evaluated by Timothy Behrens (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

The most critical aspect is about the decoding. During wake, theta sequences should strongly impact the accuracy of the decoding with 2m time bins, but it is unclear why this is not the case. The study should also provide some comparison of decoding accuracy with 2ms and 20ms and provide further details regarding how exactly events are eventually classified (see reviewer #2, points 9-11).

The study should also include examples showing the differences and similarities in decoding with the clusterless and more classical approaches (see reviewer #2, point #1).

Some other concerns were raised, mostly requesting clarification in the methods and the discussion of the results. Please see detailed review below (reviewer #2, points #2-8).

Reviewer #2:

I am satisfied with the changes the authors have made in their manuscript and the updated manuscript addresses all of my concerns.

I think the findings are exciting and will contribute to theoretical development in the field. I particularly like that the authors have made the code for their state space model available – this may prove useful for promoting methodological consistency and transparency in the replay field.

Reviewer #3:

In the revised manuscript, the authors have partially addressed the previous concerns. The manuscript has improved, and the findings remain potentially interesting. Below, please find additional comments aimed at improving the accuracy and readability of the manuscript:

1. Due to the various differences from earlier methods (clusterless decoding, state space encoding model, bin size, event detection criteria and quantification of dynamic type: radon transform vs current method), it is difficult to pinpoint which of these differences is leading to the authors' main conclusions. For the general readership, it will be extremely useful to show actual examples of the same decoded spike trains using standard Bayesian decoding (with clustered units) and using state space models. This could reveal any significant differences in the decoded locations which the authors claim are revealed by this method (pages 3 and 4). Since the authors claim there is a substantial difference between the two methods, differences in the inferred dynamics from the two methods should be visible by eye and many such examples should be available.

2. Is the higher preponderance of stationary/slow events caused by the authors setting of the beginning and ends of events as the start and ends of ripples, rather than using the multiunit population activity (which can span multiple ripples). Can the authors rerun the analysis with multiunit population activity to ensure that the results are not different from previous studies mostly due to how events are detected? Even if the results are due to that, it will be useful to report that to the reader as it will not diminish the impact of these findings (the authors already allude to the fact that the cut off is arbitrary) but will help them understand the reason for the differences between the studies.

3. Can the authors include a histogram of event duration versus proportion of such events for each of the dynamic so that the reader can better judge what is the likelihood of each event type by duration?

4. Although the fragmented dynamic would indeed identify discontinuities in decoded locations, how exactly is it better than a non-parametric shuffle? What if the fragmented dynamic has more false-positives or false-negatives?

5. Are the discovered dynamics restricted to the replay of the animal experience or can they be present before the experience? The authors should discuss this possibility.

6. How is stationarity a real-world 'speed'? Isn't it a lack of movement? Were only the spikes emitted while the animal was moving used for the encoding model and not those while it was resting? How are then the stationary events replays of that movement? What was the average velocity of the animal during movement? And of the stationary dynamic?

7. References cited and conclusions drawn from papers are not accurate in some instances, please verify and correct. Several cases are listed below, but the list is larger. Louie and Wilson, Neuron 2001 showed that replay of experience can occur at real-time speed during REM sleep, which should be cited. On lines 67-68 the authors say: "events that represent a single location are only seen in young animals (Stella et al., 2019)". That study did not investigate young animals, the authors probably meant to refer to (Farooq and Dragoi, 2019), which should be cited. There is a difference between what previous studies have claimed, and what the authors attribute to those studies. For instance, previous studies observed low proportions of sequential trajectories, but they did not observe low proportions of spatially coherent time-bins/cofiring, which are otherwise well-reported and have been observed many times.

8. How do the authors know that a probability of 0.8 or above can be inferred from downstream neurons as opposed to 0.95? Unless recordings are performed from downstream neurons that cannot really be determined. Both 0.8 and 0.95 face the problem of ambiguity of whether it is interpretable by a downstream neuron, however, a probability of 0.95 will enable readers to judge what happens when events are statistically significant. Can the authors discuss this in the main text?

9. Very low decoding errors (3-6 cm) during the run at the small timescale employed here (2 ms) may indicate that this method is incapable of capturing theta sequences (which should give a higher decoding error). Instead, they capture stationary dynamics like they do during rest. Larger bins for decoding during run are typically used to study position representation at larger timescales (at bigger timescales than theta sequences) which are likely to have low error. This could be problematic since the current method might be biased toward over-representing the stationary dynamic. The authors should address this in the manuscript.

10. What happens when a 20 ms time bin is used for state space modelling? Does it reduce the proportion of spatially-coherent events?

11. Figure 5. When whole ripples are classified as stationary, stationary-continuous mixture and so on, how is this classification done for the whole ripple? The classification of dynamics is done for each 2 ms bin, but what criteria are used to classify the whole ripple? Please provide more details on the intermediate steps. For instance, if an event is stationary, but only has one 2 ms bin which deviates, is it considered stationary-continuous?
