# Peer review - Round 1

Editors:
- Saskia Haegens, Columbia University College of Physicians and Surgeons United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69111.sa1](https://doi.org/10.7554/eLife.69111.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper will be of interest to system neuroscientists studying reinforcement learning, as well as neuroscientists in the field of brain rhythms. The work sheds new light on the specialization of individual cell types in the cortex of animals engaged in a challenging task. The authors combine many different techniques (single-cell recordings, clustering of cell types, behavioral modeling, spike-field coherence) in order to understand the differential contributions of subclasses of cell types to cortical computations during a reversal-learning task. The questions asked by the authors in this paper are interesting and their treatment is thorough, with many controls. As a result, this work is a valuable addition to the field.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Interneuron Specific Gamma Synchrony Indexes Cue Uncertainty and Prediction Errors in Prefrontal and Cingulate Cortex" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The reviewers have opted to remain anonymous.

We are sorry to say that, after consultation with the reviewers, we have decided that your work will not be considered further for publication by eLife. While we found the work overall potentially interesting, and the reviewers each found merit in particular elements, several major concerns were raised regarding key components (including the computational model and the focus on the N3 subtype). You will find these detailed in the reviews attached below.

In its current state, the paper tries many things at once (neuron subtype clustering, reward processing, computational modeling), which by itself is laudable, but as it stands it is coming short at tying these aspects together.

We are not inviting a revision because the amount of work we consider required is too extensive. However, given there was considerable interest in elements of the work, we want to point out you are free to decide to rework the current manuscript into a new version and submit this new manuscript to eLife. Note that if you choose to submit a new manuscript it would go through the regular process again (i.e., consideration by editors) and if selected to be sent out for review could potentially go back to the same reviewers and/or new ones.

Reviewer #1:

Boroujeni et al. recorded extracellular spikes from single neurons in brain areas LPFC and ACC in two awake behaving macaques that were performing a reward reversal learning task. They classified the recorded neurons into various subtypes, and investigated how neuronal activity in these different subtypes related to the variables of the behavioural task.

The paper's clear and primary strength is the classification of extracellularly recorded neurons into broad- and narrow-spiking neurons, and even further into subtypes of these two classes. While a split based purely on spike waveform shape into broad- and narrow-spiking is relatively common, the cluster-based classification into subtypes based on various additional parameters like spike variability is novel and potentially illuminating. The authors furthermore convincingly demonstrate that the recorded narrow-spiking neurons (often labelled "putative inhibitory interneurons") are indeed likely inhibitory in nature, by showing that the net effect of a spike in these cells on the surrounding population spike rate is negative. The analysis choices in this part of the paper were clear, well-motivated, and well-presented.

However, the bulk of the paper is taken up by the relationship between neuronal spiking and variables from the behavioural task, specifically choice probability (p(choice)) and reward prediction error (RPE). Here, the conclusions appear not backed up by the data, for several reasons.

First of all, the authors only present results for correlations with RPE in the reward window, and results for correlations with p(choice) in the stimulus windows. One of the main conclusions of the paper is that LPFC neurons code for p(choice) whereas ACC neurons code for RPE. However, correlations with RPE in the stimulus windows and p(choice) in the reward window are never shown. Furthermore, the authors demonstrate that, purely given the task structure, RPE and p(choice) are almost perfectly negatively correlated (r = -0.928, Figure S4). It is therefore very possible that the crucial split is not between p(choice) and RPE as the determinant of neural activity, but simply the time window in which these are analyzed.

Second, the authors present a "circuit architecture" that might account for the observed results. In the Results, this model is presented as though it were a computationally implemented biophysical neural circuit model that makes predictions that are in line with the observed data. I cannot find details of the implementation of such a model in the Methods, which makes the status of the predictions here unclear. It is not explained why two equally-valued objects would lead to gamma synchronization, whereas two objects of unequal value lead to beta synchronization (the key conclusion derived from the model). This appears to depend on total input strength, but it is hard to see why 0.5 + 0.5 (equal value, numbers provided by authors) would result in higher input than 0.8 + 0.2 (unequal value, again numbers from this paper, Figure 9). These choices, and others, appear arbitrary. In general, the description of the model in Results reads more like an interpretation/Discussion section than an outline of model-derived Results.

Third, the presented empirical evidence for narrow-spiking cells (or, more specifically, the N3-subtype) engaging preferentially in gamma-band synchronization, whereas broad-spiking cells engage preferentially in beta-band synchronization, is modest. Interneuron engagement in gamma rhythms is expected from the literature, of course, but in the present dataset this is less clear-cut. In particular, the spectral peaks in Figure 6C are quite similar between broad- and narrow-spiking, and labelling the former "beta" but the latter "gamma" requires a more thorough analysis than is now presented.

Fourth, there are some issues with reporting, where occasionally results are only reported for the narrow-spiking cells and not for the broad-spiking cells, or it is unclear whether a stated result holds for all or just a subset of cells, etc.

Finally, all results are shown aggregated over two animals, while it is important to know how the key results hold in the two animals separately.

I mention some additional recommendations here.

At the very least, correlation analyses for both p(choice) and RPE should be shown for all time windows, to allow a proper assessment. If the authors indeed wish to maintain the hard claim of a dissociation ACC<>RPE and LPFC<>p(choice) this should explicitly be tested by e.g. directly comparing the correlations with the two behavioural variables.

The model should be specified in much more detail. Specifically, the assumptions built into it should be clearly defined, and the quantitative predictions derived from it should be presented.

I understand that the data are not yet publicly released, as others from the same lab are still working on the same data (which is common in the field). However, I would urge the authors to make the source code for all reported analyses publicly available already, to greatly improve transparency and replicability. ("Upon reasonable request" is not sufficient for this goal.)

In general, the narrative could be streamlined a bit, as it currently stands the manuscript is hard to read.

Reviewer #2:

This paper studies the role of lateral prefrontal cortex (LPFC) and anterior cingulate cortex (ACC) in reversal learning. The authors suggest that LPFC plays a role in computing the probability that the animal will make a certain choice (termed choice probability), whereas ACC signals the reward prediction error. Interestingly, narrow spiking cells (putatively inhibitory neurons also known as fast spiking units) had a higher correlation with these task-relevant parameters, compared to broad spiking cells (putatively excitatory neurons also known as regular spiking units).

Next, the authors define electrophysiological cell types (termed e-types), based on spike waveform and firing patterns. The narrow spiking cells are subdivided into 3 subclasses, termed N1, N2 and N3. Notably, the same subclass of narrow spiking cells, N3, had a correlation with choice probability in LPFC and a correlation with reward prediction error in ACC. Neither of the other narrow spiking subtypes had a significant correlation with either parameter in either area.

In the final part of the paper, the authors examine the phase-locking behavior of these N3 cells to the local field potential (LFP). They find that in LPFC, N3 cells phase lock to gamma (35 – 45 Hz) during the initial learning stage shortly after rule reversal, but as learning progresses and performance reaches a new plateau, their phase locking switches to the beta-band (15 – 30 Hz). Perhaps most remarkably, the N3 cells in ACC showed a similar reversal learning stage dependent phase locking behavior; to elaborate, they phase-locked to gamma only when the reward prediction error was high (i.e., shortly after rule reversal).

These results are generally well supported by rigorous statistics and sophisticated analyses. However, there are several weaknesses. First, while the claim that LPFC encoded choice probability is well supported, the claim that ACC encodes reward prediction error is not as well substantiated. As seen in Figure 3, percent neurons showing significantly correlation between their firing rate and reward prediction error is not very different between LPFC and ACC, and quite similar between broad spiking and narrow spiking units within ACC.

Second, the authors build a reinforcement learning model to calculate "Choice Probability", which quantifies the probability that the animal will select the rewarded stimulus. According to this definition, choice probability should dip upon reversal, and rise to a new plateau after several trials. However, this metric is fairly unintuitive, not to mention in conflict with existing nomenclature (e.g., Nienborg, Cohen and Cumming 2012). It would be helpful to have an accompanying plot of how the firing rate and phase locking behavior of each neuronal type changes as a function of trials after reversal.

Third, the extent to which choice probability encoding neurons and reward prediction error encoding neurons in each area falls into a specific e-type is not shown.

Undoubtedly, it is noteworthy and remarkable that N3 is the only e-type that shows a positive correlation with choice probability in lateral prefrontal cortex and a positive correlation with reward prediction error in ACC (Figure 5). But do all choice probability encoding neurons in LPFC and reward prediction error encoding neurons in ACC fall into the N3 e-type?

Further, the task-dependent phase locking behavior of e-types other than N3 are not shown. Given that N3 is the only NS e-type that shows a relationship with task-relevant parameters, I would expect the task learning dependent phase-locking behavior to also be unique to N3, but this result is not presented in this paper.

Finally, the conceptual model in Figure 9 captures the results presented in this paper and gives rise to testable predictions. It seems that some predictions of this model should be testable with the presented data. For example, the prediction that in LPFC, broad spiking cells fall into two functional categories, whereas N3 cells are more functionally homogeneous, would be an interesting prediction to test. Further, the prediction that in ACC, broad spiking cells encode reward whereas N3 cells encode reward prediction error is easily testable and would strengthen the conclusions of this paper.

The main finding of this paper, that a specific electrophysiological subclass of narrow spiking cells serve important roles in a reversal learning by preferentially phase-locking to gamma band LFP, would be of broader significance and impact if this finding could be generalized to other brain regions, behavioral tasks and model species. That said, there are already several papers in the literature that define e-types. Specifically, Markram et al. (2015) define 11 e-types; Gouwens et al. 2019 define 6 e-types that constitute narrow spiking cells (referred to as fast spiking cells in Gouwens et al). For sake of future efforts to study e-types and their functional roles, it would be important to reconcile these disparate definitions of e-types.

Moreover, there are at least two other papers showing that subclasses of narrow spiking neurons have different relationship with gamma (Shin and Moore 2019; Onorato et al., 2020). It would be very interesting and important to know whether the 3 narrow spiking e-types discussed in this paper match up with the subclasses in the two aforementioned papers.

In sum, this paper is a valuable addition to the reinforcement learning literature as well as neuronal cell types and neural oscillations literature. Some additional analyses could strengthen the conclusions of this paper. It is unclear how the e-types defined in this paper will tie into other neuronal categorizations in recent literature. This link to prior work will be important for broader significance.

Comments for the authors:

I. Comments on Figures

1. Figure 2 and Figure S6 shows the PSTH aligned to Feature 1 and Feature 2 based on the cue order (Motion first vs Color first). It would be highly relevant to also show the PSTH aligned to Feature 1, Feature 2 and Reward based on behavioral outcome (correct vs incorrect, and there are at least 3 different types of error outcomes; please see my comment III-2 in Comments on Methods below for elaboration).

In particular, PSTH aligned to reward conditioned on behavioral outcome is crucial for interpreting Figure 3.

2. Figures 2 and 3: The correlation between firing rate and Choice Probability / RPE is interesting, but not very intuitive. It would be helpful to have a plot of Choice Probability and Reward Prediction Error as a function of trials since reversal, as well as the firing rate for each cell type and brain area as a function of trials since reversal. This way we can see whether LPFC NS firing rate after color cue onset tracks Choice Probability, and whether ACC NS firing rate after reward tracks RPE.

3. Figure 4B firing rate unit is missing both the figure and in the main text.

Figure 4C rastergram firing rate seems massively different from the average firing rate in 4B? e.g., for Figure 4C rastergram for N1, there seems to be ~5 spikes per 100ms, which would be ~50Hz, but the average firing rate for N1 is 4Hz?

Also, please discuss why the narrow spiking firing rate is so low (assuming the firing rate unit was Hz, mean firing rate is <2Hz for N2 and N3). Narrow spiking firing rates have typically been reported to be ~10Hz in vivo.

4. Figure 5: It is remarkable that N3 is the only e-type that shows a positive correlation with choice probability in LPFC and a positive correlation with reward prediction error in ACC. To what extent do choice probability encoding neurons and reward prediction error encoding neurons in each area fall into a specific e-type? I would like to know whether a neuron's e-type is predictable from task-dependent functional properties of the neuron.

5. Figure 6C: suggest plotting N3 in the same plot as Broad Spiking and Narrow Spiking units such that the magnitude can be compared more easily.

In addition, please clarify what the y-axis of Figure6c means (Peak densities of spike-LFP synchronization (PPC)). Is this simply the average PPC spectra? Or normalized for each unit in some way? I would recommend plotting the former, such that it is possible to compare which e-types have the best locking properties to which frequency band.

6. Figure 7 and 8: It's very interesting that initially after reversal, N3 locks to gamma but later, as performance reaches a new plateau, N3 locks to beta. If you plot trial since reversal on the x-axis, and plot the peak of PPC spectra (averaged across N3 cells) on the y-axis, do you see a gradual change in peak frequency or is it more of a step function change after each reversal? Relatedly, if you plot the histogram of PPC spectra peak frequency across N3 cells, is it a bimodal distribution (one peak in beta and another peak in gamma) or is it unimodal?

7. It would be interesting to know the behavior-dependent phase locking of other e-types as well. I suggest adding Figure 7 and 8 C and F for all e-types as a supplemental figure.

8. Were LPFC and ACC recorded simultaneously? If so, it would be very interesting to see if inter-area coherence mimics the changes in PPC. For example, does the gamma band coherence go up in the first few trials after reversal, followed by an increase in beta band coherence as behavioral performance plateaus?

9. Figure 9 outlays a really nice hypothesis that gives rise to testable predictions. Some of these predictions are testable within the data presented in this paper. I think it would significantly strengthen this paper if some of these predictions could be tested:

Figure 9 hypothesizes that in LPFC, Broad Spiking neurons should encode Value predictions; e.g., red-selective neurons that, after learning, fire more when red is being rewarded compared to when green is being rewarded. These Value-predictive neurons should fire similarly during learning, and is perhaps even predictive of the animal's choice on a trial-by-trial basis (e.g., on trials that red-selective neurons fired more during learning, the animal saccades according to the red stimulus). In contrast, N3 neurons should show no such Value-predictive behavior. Is there evidence of such prediction in the data?

Relatedly, Figure 9 hypothesizes that in ACC, Broad Spiking neurons encode reward, whereas N3 encode RPE. According to this prediction, N3 activity should be higher for "surprise correct" trials shortly after reversal, and go down as performance plateaus, whereas Broad Spiking neurons should be excited by reward the same amount regardless of whether it is shortly after reversal or after behavioral performance has reached plateau. Is this seen in data? I think this would be made clear if the PSTH aligned to reward were plotted, as suggested in Comment 1.

II. Comments on Main Text

1. "We next asked whether the narrow spiking, putative interneurons that encode p(choice) in LPFC and RPE in ACC are from the same electrophysiological cell type, or e-type (Markram et al., 2015)."

There are ~11 e-types described in Markram et al., 2015. Further, Gouwens…Koch 2019 NN describes ~6 sub-e-types of Fast Spiking cells. I recommend the authors to speculate on how previously reported e-types match up with the e-types described in this paper.

2. "Prior studies have suggested that interneurons have unique relationships to oscillatory activity (Cardin et al., 2009; Vinck et al., 2013; Voloh and Womelsdorf, 2018; Womelsdorf et al., 2014a),"

I suggest adding Chen…Zhang 2017 Neuron to this list of references.

3. Discussion section: There are at least two other papers showing that subclasses of narrow spiking neurons have different relationship with gamma (Shin and Moore 2019 Neuron; Onorato…Vinck 2020 Neuron). It would be an interesting addition to the Discussion section to speculate on whether the 3 narrow spiking e-types discussed in this paper match up with the subclasses in the two aforementioned papers.

III. Comments on Methods

1. In general, the Method section is not consistent about referring to relevant figures for the analyses being described. It would really help the reader if the analyses that went into each figure were clarified: e.g., "Statistical Analysis of time resolved spike-LFP coherence for putative interneurons and broad spiking neurons (Figure 7, 8)"

2. Task design: "Color-reward associations were reversed without cue after 30 trials or until a learning criterion was reached, which makes this task a color-based reversal learning task. "

It seems that a strategy that a monkey might employ would be to count the number of trials after reversal to anticipate when the next reversal would happen, which would rely on a different mental strategy than reversal learning tasks where the reversal points are not predictable. Is there any behavioral evidence that would discount the possibility that the monkeys are counting?

"Hence, a correct response to a given stimulus must match the motion direction of that stimulus as well as the timing of the dimming of that stimulus."

In this task, there appears to be one way to be correct, but several distinct ways of being incorrect. First, the monkey could be incorrect in both the timing and the saccade direction. Second, the monkey could be correct with the timing but incorrect with the direction. Third, the monkey could be correct with the direction but incorrect with the timing. The third outcome could be further subdivided into premature response versus late response. The reason why a monkey might make each mistake is different. Only the first scenario supports the possibility that the monkey thought the other color was being rewarded, e.g., shortly after reversal. It would be interesting to know the proportion of each error type as a function of trials since reversal. Furthermore, I would expect the negative reward prediction error to be most prominent in the first type of error. Hence, it would make sense to me if only the first type of error was considered when calculating choice probability and reward prediction error.

3. "Here, we use this model to estimate the trial-by-trial fluctuations of the expected value (EV) for the rewarded color and the choice probability (CP) of the animal's stimulus selection. EV and CP increase with learning similar to the increase in the probability of the animal to make rewarded choices, causing all three variables to correlate (Figure 4E, F)."

Figure 4 does not have E-F panels.

4. Behavioral analysis: I could not find a formal definition of Choice Probability and Reward Prediction Error anywhere. I assume Equation 4 defines Choice Probability, while Rt-Vt defines RPE? I suggest making these definitions clear in the Methods, as well as the main text and the figure legend.

Choice Probability is abbreviated in at least three different ways throughout the manuscript (e.g., p(choice), CP, CHP). Please be consistent.

Note on terminology: Choice Probability commonly refers to the relationship between the activity of individual sensory neurons and the animal's behavioral choice (see Nienborg, Cohen and Cumming 2012 ARN). The duplicate terminology may be confusing for some readers. I suggest using a different term (e.g., Probability of Choice).

5. "We then quantified the log-likelihood of the independent test dataset given the training datasets optimal parameter values."

Where is this result plotted? What is the model performance in predicting test dataset?

6. Waveform analysis: It would help to add a diagram of T2P, T4R and HR in Figure 4.

Relatedly, trough comes before the peak in extracellular spike waveforms (as apparent in Figure 4C) – T2P should be (tpeak-ttrough) in order to be a positive value?

7. "LV is a measure of regularity/burstiness of spike train and is proportional to the square of the difference divided by sum of two consecutive interspike intervals (Shinomoto et al., 2009)."

This sentence should go in the main text. The reason being; the way LV is described in the main text makes it sound like LV and CV measure the same things: "regular or variable interspike intervals (local variability 'LV'), or more or less variable firing relative to their mean interspike interval (coefficient of variation 'CV')."

8. Given how central the clustering analysis in Figure 4A is to the rest of the paper, the exact parameters that went into this analysis (HR, T4R, LV, CV, FR) should be made clear in the main text.

In addition, this clustering analysis is key to the reproducibility of e-types in other datasets. The authors have stated that "All data and code is available upon reasonable request." However, in my opinion, at least the code for the e-type clustering analysis should be made publicly available.

9. "Correlation of local variation with burst index"

Burst index is defined here, but not plotted in any figures. I suggest adding a plot depicting the relationship between local variation and burst index would be informative.

10. "First, we divided trials into two groups of high and low RPE and CHP values (trials were assigned based on their median value for each neuron)."

I understood RPE and Choice Probability to be values unique to each trial, rather than to each neuron? If so, the median value should be specific to each behavior session, not to each neuron? Please clarify.

11. "We included only neurons with at least 50 spikes per time window."

Does this sentence mean 50 spikes per time window per trial? For a 700ms time window, this would mean that the neuron would have to be firing at ~70Hz in order to be included in this analysis! If this sentence means 50 spike per time window across trials, please clarify. In this case, please also clarify the range of trial number that went into this analysis.

Reviewer #3:

In this work, Boroujeni et al. investigated the role of different cellular subtypes in the lateral prefrontal cortex (LFPC) and anterior cingulate cortex (ACC) of the rhesus macaque as the animals performed an attention demanding reversal-learning task. The authors use an attention-augmented reinforcement learning model to track the trial-by-trial values of key decision-making variables which were then correlated against the neural activity. The cellular population was separated into broad and narrow spiking neurons using features computed from the extracellularly recorded waveforms. The authors find that the activity of the narrow spiking cells in the LFPC is correlated with the choice probability, whereas the activity of narrow spiking cells in the ACC is correlated with reward prediction errors. Interestingly, the authors find that further splitting the population of broad and narrow spiking cells into subtypes revealed that both the choice probability in LPFC and the reward prediction error in the ACC were encoded by a specific subtype of putative interneuron. The authors show that the spike-field phase synchronization of this putative interneuron subgroup is also modulated by choice probability in the LFPC and reward prediction error in the ACC, mirroring the result from their single-unit correlation analysis. The authors use these results to propose a biologically plausible circuit model of how learning in such a task might be implemented through interneuron specific synchronization.

While many of the results in the paper seem robust, some of the conclusions drawn by the authors rest on analyses and methods that require further validation and controls.

1. The clustering of the cell population into 5 broad-spiking and 3 narrow-spiking subtypes is perhaps one of the most critical results that requires further validation since a lot the conclusions in the paper rely on the outcome of this analysis. The validation that the authors include in the paper (Figure S5C, S5D) address concerns regarding the clustering quality, but it's still unclear how meaningful this separation into these 8 clusters actually is. The clustering is also performed on the pooled data across both animals, but the authors should have also shown what the clustering looks like when performed independently on the population from each animal, and if there is a meaningful correspondence between the sets of clusters recovered in the two populations.

2. Most of the follow-up analysis focuses on the comparison between one specific interneuron subtype (N3) and all broad -spiking cells. I imagine that the reason for this is two-fold: (1) the N3 subtype is the only one that showed a significant modulatory effect on the multi-unit activity (Figure 4D), and (2) it seems to be special in the sense that the activity of the N3 cells is significantly correlated with choice probability in LPFC in addition to reward prediction error in ACC. While the reasons for showing key results only for the N3-type can be appreciated, the authors should have included additional control analysis to demonstrate that their results are indeed specific to the N3 subtype. For example, in Figure 7 and 8, the authors show a comparison of the spike-LFP phase synchronization between N3 and broad spiking cells, but no further characterization of subtypes within the broad spike cells or the other narrow spiking types (i.e. N1, N2).

3. The authors show that the spike-field phase synchronization of the N3 subgroup is also modulated by choice probability in the LFPC (Figure 7) and reward prediction error in the ACC (Figure 8), mirroring the result from their single-unit correlation analysis (Figures 2 and 3). Unlike their firing rate analysis however, they do not show anatomical specialization in these analyses, even though the model they propose in Figure 9 clearly shows that they hypothesize this to be the case. It would be very interesting to show the analysis performed in Figure 7 for the ACC N3 population, and likewise, the analysis performed in Figure 8 for the LPFC N3 population.

4. Behavior

a. In Figure 1C, I imagine that the proportion of rewarded choices at reversal (t=0, not shown) is equal to one minus the asymptotic performance? So around 0.1?

b. If the stimulus-reward pairings are fully deterministic, why does the monkey require so many trials (on average 7 I believe it was) to reach asymptotic performance again?

c. Related to the previous question, is there any change in this acquisition time over the course of a session (as they experience more and more reversals)?

d. Can you show some example fits of the reinforcement learning model? For example, the choice probability and expected value as a function of the trial number around a reversal.

5. Single Units

a. The authors correlate the neural activity with model-derived variables, like the probability of choice, and prediction error. The distributions of these variables, however (as indicated in Figure S4b, and S4C) are very skewed, and it seems like most of the variability comes from the few trials (around 10) that it takes to reach asymptotic performance after a reversal. It would be interesting to know what this correlation represents. Are the cells truly tracking small changes in the P(choice) and PE or does this reflect more of a discrete switch? Maybe the authors could show some scatters, firing rate vs. P(choice), of some example cells. How well can p(choice) and PE be decoded from the neural population?

6. Electrophysiology/Clustering

It seems that a lot of the results in the paper rely on clustering analysis. The authors have been cautious in their approach (i.e., validating the results), but given that a lot depends on the reliability of these results, I think it would be wise to add a few more control analyses. I am not sure how feasible these are, but worth considering nonetheless:

a. Another way of validating the clustering is to do it across animals. From what I understood, the clustering (for e-type) is done using data from both animals. How well would a clustering model fit within animals, predict the clustering across animals?

7. Spike field coherence

a. Can the authors comment on the effect of ERPs?

b. Simply controlling for the number of spikes between conditions is not necessarily sufficient. If you have a cell that responds to one condition but does not respond to another condition, the spikes for condition 1 are going to be much more clustered in time than for condition 2. Therefore the underlying LFP is not sampled in the same way between the two conditions.

c. Is it possible to show that the spike-field coherence results are also anatomically specific? Does the synchrony of cells in the ACC and LPFC mirror the single-unit results, i.e. reward prediction error in ACC but not LPFC and choice probability in LPFC but not ACC?

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Interneuron Specific Gamma Synchronization Indexes Cue Uncertainty and Prediction Errors in Lateral Prefrontal and Anterior Cingulate Cortex" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

We believe that the manuscript has improved substantially since the initial submission, and appreciate that you did quite a lot of work to address the concerns raised previously. Reviewers and editors agreed the new analysis makes a much stronger case, and that this work will make a valuable addition to the field. Reviewers raised a few remaining issues, please find these below. We ask you to address these and invite you to submit a revised version of your manuscript at your earliest convenience.

Reviewer #1:

This paper studies the role of lateral prefrontal cortex (LPFC) and anterior cingulate cortex (ACC) in reversal learning. The authors suggest that LPFC plays a role in computing the probability that the animal will make a certain choice (termed choice probability), whereas ACC signals the reward prediction error. Interestingly, narrow spiking cells (putatively inhibitory neurons also known as fast spiking units) had a higher correlation with these task-relevant parameters, compared to broad spiking cells (putatively excitatory neurons also known as regular spiking units).

Next, the authors define electrophysiological cell types (termed e-types), based on spike waveform and firing patterns. The narrow spiking cells are subdivided into 3 subclasses, termed N1, N2 and N3. Notably, the same subclass of narrow spiking cells, N3, had a correlation with choice probability in LPFC and a correlation with reward prediction error in ACC. Neither of the other narrow spiking subtypes had a significant correlation with either parameter in either area.

In the final part of the paper, the authors examine the phase-locking behavior of these N3 cells to the local field potential (LFP). They find that in LPFC, N3 cells phase lock to gamma (35 – 45 Hz) during the initial learning stage shortly after rule reversal, but as learning progresses and performance reaches a new plateau, their phase locking switches to the beta-band (15 – 30 Hz). Perhaps most remarkably, the N3 cells in ACC showed a similar reversal learning stage dependent phase locking behavior; to elaborate, they phase-locked to gamma only when the reward prediction error was high (i.e., shortly after rule reversal).

The main finding of this paper, that a specific electrophysiological subclass of narrow spiking cells serve important roles in a reversal learning by preferentially phase-locking to gamma band LFP, would be of broader significance and impact if this finding could be generalized to other brain regions, behavioral tasks and model species. This paper cites several precedents in the literature that define e-types. Specifically, Markram et al. (2015) define 11 e-types; Gouwens et al. 2019 define 6 e-types that constitute narrow spiking cells (referred to as fast spiking cells in Gouwens et al). For sake of future efforts to study e-types and their functional roles, it would be important to reconcile these disparate definitions of e-types.

Moreover, as mentioned in the Discussion section of this paper, there are several other papers showing that subclasses of narrow spiking neurons have different relationship with gamma (Shin and Moore 2019; Onorato et al., 2020). It would be very interesting and important to know whether the 3 narrow spiking e-types discussed in this paper match up with the subclasses in the aforementioned papers.

In sum, this paper is a valuable addition to the reinforcement learning literature as well as neuronal cell types and neural oscillations literature. However, it is unclear how the e-types defined in this paper will tie into other neuronal categorizations in recent literature. This link to prior work will be important for broader significance.

Comments for the authors:

This paper has made significant improvements from the previous version. Most importantly, the implementation details of the circuit simulation are clarified. The vast majority of my prior concerns have been addressed. I have only a few suggestions remaining.

1. Given that reward prediction error analysis is critical to the thesis of this paper, I am still of the opinion that it would be important to include the PSTH aligned to the reward, for narrow spiking and broad spiking neurons (as in Figure 2) as well as for important e-types (as in Figure S3).

2. The added classifier analysis or predicting cell classes from their correlations with learning variables is very interesting. However, I am not clear on exactly what was used to train the SVM. The way I currently understand this analysis is that in LPFC, correlation between firing rate and p(choice) was calculated for each neuron – and this one-dimensional vector, the size of which is (Number of neurons)X1, was used to train the SVM. Is this the case? Please clarify.

3. Figure S5 E and F: it is hard to see a trend in these plots. I suggest either making the dots transparent; or plotting the data as a 2D-histogram. This way it would be possible to discern where the data is the densest.

4. In Methods, the numbering in the equations are not unique (there's two Equation 2 and two Equation 3). Please correct.

5. The following sentences in Supplementary Online Information needs to be corrected as indicated:

"These circuit motifs are provided to provide a proof-of-concept that the observations can follows from biologically plausible motifs. These circuits motifs also provide predictions which can be tested in future studies."

Reviewer #2:

In this work, Boroujeni et al. investigated the role of different cellular subtypes in the lateral prefrontal cortex (LFPC) and anterior cingulate cortex (ACC) of the rhesus macaque as the animals performed an attention-demanding reversal-learning task. The authors use an attention-augmented reinforcement learning model to track the trial-by-trial values of key decision-making variables which were then correlated against the neural activity. The cellular population was separated into broad and narrow spiking neurons using features computed from the extracellularly recorded waveforms. The authors find that the activity of the narrow spiking cells in the LFPC is correlated with the choice probability, whereas the activity of narrow spiking cells in the ACC is correlated with reward prediction errors. Interestingly, the authors find that further splitting the population of broad and narrow spiking cells into subtypes revealed that both the choice probability in LPFC and the reward prediction error in the ACC were encoded by a specific subtype of putative interneuron. The authors show that the spike-field phase synchronization of this putative interneuron subgroup is also modulated by choice probability in the LFPC and reward prediction error in the ACC, mirroring the result from their single-unit correlation analysis. The authors use these results to propose a biologically plausible circuit model of how learning in such a task might be implemented through interneuron-specific synchronization.

The analysis is thorough and the authors present a nice narrative of the results, even though in some cases my interpretation of the data is a little more mixed than what is written in the paper. For example, the authors are eager to point out that their results are "interneuron specific" and yet the data that they show suggests otherwise. Take the spike-LFP synchronization results shown in Figure S15, where it seems that the modulation of pairwise phase consistency with p(choice) could also be present for the B1 cluster of cells in addition to the N3 group (no stats shown). The same could be true for the B2 type in the ACC, which seems to show differential effects for high and low RPE.

Are these real effects or are these anomalies that are biased by a few outliers? In either case, please clarify.

Thank you for including the new supplementary figures; I can really appreciate the additional amount of work that must have gone into preparing the new controls for the second submission of the paper. The addition of the example model fittings (Figure S5) and the correlation of the firing rate from the two example cells with the RPE and p(choice) (Figure S10) are very nice. I would recommend to the authors to move the two examples in Figure S10 to one of the main figures. In the first submission, the focus of the paper was predominantly on the N3 subtype and its specialized functional properties in ACC and LPFC. The new figures however (specifically Figure S15) show that the story is a little more mixed than originally presented. B1 for example in LPFC shows differential effects for high and low P(choice) and B2 in ACC shows differential effects for high and low RPE. In any case, the new figures provide a much more complete story and I feel made the paper stronger.
