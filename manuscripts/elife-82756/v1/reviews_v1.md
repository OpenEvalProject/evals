# Peer review - Round 1

Editors:
- Denise J Cai, https://ror.org/04a9tmd77 Icahn School of Medicine at Mount Sinai United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82756.sa0](https://doi.org/10.7554/eLife.82756.sa0)

This study provides fundamental findings about the developing brain and compelling evidence for how hippocampal physiology evolves during the first few postnatal weeks. Unlike previous in vitro results, which find declining network synchrony after the first postnatal week, the authors find in vivo that synchrony increases and peaks in the second postnatal week, despite emerging GABA-mediated inhibition during this time. They develop a model to explain these findings and suggest an underlying bistable population dynamic, oscillating between silent and active states, that sculpts input discrimination and network synchrony.


---

# Peer review - Round 1

Editors:
- Denise J Cai, https://ror.org/04a9tmd77 Icahn School of Medicine at Mount Sinai United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82756.sa1](https://doi.org/10.7554/eLife.82756.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "Network instability dynamics drive a transient bursting period in the developing hippocampus in vivo" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The reviewers have opted to remain anonymous.

Comments to the Authors:

We are sorry to say that, after consultation with the reviewers, we have decided that this work will not be considered further for publication by eLife. Given the reviewers' enthusiasm of the manuscript, if you feel you can address the reviewers' concerns with additional data collection and analyses, we welcome submission of a revised manuscript, should you choose to decide to collect new data. You can refer to this manuscript number, but we cannot make any guarantees about acceptance because the work would be reconsidered as a new submission.

All reviewers expressed enthusiasm for this manuscript and thought the results were of broad interest to the readership of eLife. While individual reviews are included below, here are a couple of points where reviewers agreed were essential to be included in a revised version before consideration for publication at eLife.

1) Anesthesia has a major effect on neuronal dynamics and therefore, it might seriously impact the findings of the study. The authors should provide experimental data from non-anesthetized animals to confirm their results. This will augment the relevance and validity of the study.

2) A second major aspect that needs to be carefully addressed in a revised version is the data analysis and modelling limitations. All three reviewers raised this aspect. Please see their detailed comments and suggestions below.

Reviewer #1 (Recommendations for the authors):

This interesting manuscript by Graf and colleagues aims to map the developmental trajectories of spontaneous network activity of the developing hippocampus. The authors perform in vivo calcium imaging of CA1 neurons throughout development at P4, P11, and P18. They first develop a computational pipeline to accurately extract neural sources and assign timeseries GCaMP fluorescence values, which is challenging in dense and overlapping cell populations. They then identify that network synchrony (which the authors equate with network burstiness) peaks in the second postnatal week. They found this unexpected because prior in vitro results have identified network synchrony primarily in the first postnatal week, and emerging GABA inhibition is thought to gradually reduce network synchrony thereafter. Using a recurrent neural network model, assuming a simple recurrent architecture within and between excitatory and inhibitory neurons, the authors identify bistable regimes, that amplify input in different and non-linear ways. Silent states were found to amplify input that leads to burstiness, whereas active states did not lead to bursting network behaviors. In sum, the authors propose that bistable network properties in the second week of postnatal life may be important for generating synchronous network activity and performing input discrimination prior to environmental exploration and experience-dependent learning.

The strengths of this study are the systematic characterization of spontaneous CA1 network activity, which was done in vivo, and longitudinally, across the first three postnatal weeks. Rigor was taken to collect high quality data in a challenging prep and the combination of experiments and modeling led to the proposal of an interesting model involving bistable dynamics that may be broadly relevant to developmental physiology. The observation that burstiness is due to single neurons having higher coupling with population activity , not due to increased pairwise correlations, was also quite interesting. Overall the claims of the study are justified by their data.

A main weakness or concern is that 1. it is not clear how functionally important p11 synchrony/burstiness is, and 2. while one network mechanism is proposed there may be other underlying network dynamics that can explain p11 burstiness equally well or better. For instance, it's possible that emerging GABA-ergic inhibition acts on other interneurons or on highly patterned set of principle neurons, or that the sub threshold properties of principle neurons change dramatically during this P11 window, such that any of these alternative mechanisms may drive the observed bursting behavior. Further explorations of the model, to negate alternative explanations, or experimental perturbations during P4 vs P11 vs P18, would clarify and strengthen the main conclusions.

Other Points:

1. Figures 2 and 3 rely heavily on CDFs but a plain display of histograms would be more informative and it would be easier to evaluate heavy tail vs normal distributions, say of firing rates.

2. The enhanced burstiness on P11 seems very sensitive to the definition used for burstiness (ie NB). For instance fraction of time (Figure 2D) suggests similar burstiness on days p11 and p18, whereas burstiness duration (Figure 2E) suggests similar levels on P4 an P11, thus it is not clear how robust or important the p11 bursting behavior is.

3. In Figure 4, coupling to population activity, and all Pearsons analyses, should control for increases in overall firing rates after P4.

4. The model being used seems to be an extension of prior models that are well validated with existing experimentally determined constraints, but such validation data should again be shown for this new extended model.

To strengthen the claim that P11 burstiness is functionally important it would be useful to perform in silico manipulations, or actual experimental manipulations, possibly silencing of these P11 bursts, to show functional consequences later in development.

To strengthen the claim that underlying network bistabiliy leads to this burstiness, it would be useful to provide in silico manipulations that support this, or test alternative models to show they do not lead to burstiness.

The enhanced burstiness on P11 seems very sensitive to how burstiness is defined. It may be important to perform these analyses using a wide range of definitions to show the results are robust to small changes in definition.

In general, data presentation rely heavily on CDFs, but it would be easier to interpret and evaluate if histograms of the raw data were provided (ie for Figures 2 and 3).

All Pearsons analyses, should control for increases in overall firing rates after P4, by shuffling the datasets and providing chance calculations.

More validation data for the model would build confidence in the modeling results.

Overall, the manuscript was difficult to read , possibly because certain terms are used interchangeably (synchrony and burstiness) and possibly because enough of the methods are not described in the main text and possibly because the writing sometimes meanders and loses a consistent message. A tightening up of the text would be very helpful.

Reviewer #2 (Recommendations for the authors):

Strengths:

The paper is very careful to extract single cell signals from the densely populated CA1 region and uses a number of appropriate analysis methods to quantify single cell and population dynamics. Their analysis approaches allowed them to determine differences at distinct developmental stages that could have easily been missed. Their detection methods and barrage of analysis methods will be generally useful to any field that studies functional calcium signals at the network level.

The paper nicely combines experimental findings with computational modeling to gain insight into the development of a functional dorsal CA1. Their experimental findings are on face value difficult to reconcile, but their computational modeling work brings together their experimental findings, along with those from other papers, to put forward a comprehensive framework. This paper is a good example of how experiments should inform computational models to bring insight into brain function.

Weaknesses:

Animals are not awake/alert during imaging. They have just undergone surgery (60 mins prior to imaging) and are in a sedative state during imaging (as far as I can tell). This is a major weakness of the paper as no doubt the CA1 will behave differently in an awake state. This makes it difficult to generalize their findings to the awake state.

The paper contains a lack of causal relationships. For instance, do the NBs setup the hippocampus for learning right before environmental exploration, or do they have some other role? Could they be epiphenomenal? There are no experimental manipulations of NBs, which are needed to further test the authors theories.

A big part of the proposed mechanism for increased NBs at P11 is that GABA has switched from excitatory to inhibitory at all synapses in CA1 by P11, but is this true? The authors refer to literature, but do not show that GABA is inhibitory in their experiments at this time point in CA1.

There is a lack of explanation of why P4 networks have more in common with P18 networks than P11 networks, in many cases. The data clearly demonstrates that there is not a progression of network dynamics as a function of age, and instead P11 is, for many measures, behaving differently than both younger and older developmental stages.

Analysis of FOVs is performed on separate animals at the different ages. The findings would be further strengthened if the same neurons were tracked over time. This can be done in adult mice. However, given the developmental changes that occur between P4 and P18, this type of experiment may not be feasible with current methods. Still, it would be insightful to observe how the same network develops throughout this period. An experiment for the future, perhaps.

It is not explicitly clear whether the mice are awake during the experiments or under anesthesia. It is stated that head-fixed animals are "spontaneously breathing" in the Results section, and in the Methods they state "Isoflurane was discontinued after completion of the surgical preparation and gradually substituted with the analgesic sedative nitrous oxide". So, what is the general state of the animals during in vivo imaging? This is important as it will certainly affect network activity in CA1 and should be discussed.

The data is interpreted that NBs are more prevalent at P11 than P4 and P18. However, given the overall increase in CAT frequency at P18 (Figure 3A, right) it might make it more difficult to detect isolated NBs from those riding on top of (or very close in time to) other NBs (especially given that calcium transients have relatively slow decay kinetics). The authors should be careful to make sure their NB detection method is not biasing them to detect more NBs in FOVs with generally lower activity, i.e. at P11 versus P18.

I do wonder if CAT kinetics differ in PCs at the different age groups. They should show that expression levels are similar, rise times/decay times are similar, noise levels are similar…to rule out these as confounds to the other forms of analysis.

Reviewer #3 (Recommendations for the authors):

The manuscript addresses an important topic. The data and modeling results provide new insights into the developmental trajectories of network activity in hippocampal CA1 area. However, several major aspects, especially concerning (i) the solidity of data from a rather low number of mice, (ii) the lack of experimental data uncovering the underlying mechanisms of described processes and (iii) the interpretation of results in the context of existing literature, dampen my enthusiasm and need to be addressed as part of a major revision before further consideration of the study.

1. The in vivo dataset is too small to enable reliable conclusions. In the manuscript, the number of mice used for each analysis is not specified. In general, n numbers should be stated more clearly and be included in the figure legends. For each mouse 3-5 FOVs and in average 14 FOVs/group were acquired, implying that only around 3-4 mice were used for group analysis. Furthermore, the applied stats use FOVs as statistical unit and covers not for single datapoint independency, i.e. FOVs that are coming from the same mouse. The authors might think about the use of mixed-effect models for statistical analysis after increasing the size of the dataset. Given the small size of the recording area, the authors should state how overlapping FOVs and thus, cell populations, between imaging sessions were avoided. Moreover, what was the rationale for focusing the investigation on P4, P11, and P18? Are these time points of particular relevance? In the absence of more time points, it is unclear how the dynamics of described processes evolve.

2. Besides modeling, additional experimental evidence of the cellular interactions underlying the developmental dynamics of bursts should be added. Direct targeting of distinct neuronal populations, their acute or chronic manipulation, possible combination with electrophysiological recordings, are just few suggestions, how the insights from modeling should be complemented. Moreover, the RNN model provides insights into the mechanisms governing the elevated burstiness constrained to the P11 age group. However, it remains unclear, which mechanisms potentially contribute to the developmental emergence of a bi-stable network as well as its potential disappearance. The authors might include this developmental aspect in the model as well and discuss age-dependent features in synaptic strength and timing that account for observed changes in network synchrony and burstiness in more detail.

3. line 371-374: the authors conclude the presence of a lower synchrony in the developing CA1 area compared to sensory cortices as the result of the identification of lower correlation values. The reference cited for visual cortex (Rochefort at al., 2009) uses no pairwise correlation analysis and should be removed. The other references for somatosensory cortices quantify pairwise correlation but use different analytical strategies and not STTC as used in the present manuscript. Thus, the comparison of absolute correlation values might be inappropriate and further depend on the chosen timescale. Another important factor impacting correlation values is the use of anesthesia. Mice were anesthetized with nitrous oxide, known to alter neurotransmission and consequently affecting physiological activity. While anesthesia increases correlation in sensory areas (Goltstein et al., 2015), it decreases STTC values in the CA1 area (Yang et al., 2021). The studies cited in line 371-374 are done in non-anesthetized or in urethane/isoflurane anesthetized mice. Consequently, the identified lower correlation values could thus be an artifact of differential actions of anesthesia in sensory areas versus CA1 area. Moreover, anesthesia has been identified to impact brain activity in an age- and dose-dependent manner (Chini et al., 2019) and might therefore impact the selected age groups differently. Accordingly, the authors should refrain from the statement of a developmental lower correlation in CA1 area than in sensory areas. To support this statement additional recordings in non-anesthetized mice in CA1 area and compared to equally analyzed open-access datasets of sensory cortices would be required. In line with this, PSD analysis of frequencies below 1 Hz as used in Figure 3B are in particular sensitive to anesthesia and should be interpreted with caution.

4. The threshold for burst detection was quantified individually for each FOV. Consequently, the proportion of silent periods in each FOV affects the threshold calculation and might affect the P11 age group, where activity is almost but not completely continuous, differently. Analysis of bursts detected with a threshold quantified only on "active" periods by excluding silent periods could further support the presence of burst activity during events without be affected by the changing discontinuity over age.

5. The authors describe in the Introduction that in the neonatal hippocampus activity is triggered by myoclonic twitches. Did the authors monitor the animal's movement? If yes, the occurrence of bursts and presence of network motifs could be correlated to the movement. This would enable a better understanding of how age-dependent dissociation of CA1 activity from twitches relates to the emergence and stabilization of self-organized hippocampal motifs during recurring activation patterns (line 258, 259) and changes in neuronal synchrony.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Network instability dynamics drive a transient bursting period in the developing hippocampus in vivo" for further consideration by eLife. Your revised article has been evaluated by Laura Colgin (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

While all the reviewers remain enthusiastic about this work, Reviewer 3 points out some major concerns that need to be addressed before this manuscript can be recommended for publication.

I appreciate the work that was done to investigate the influence that N20 anesthesia has on hippocampal network activity, but I find that the conclusions that the authors draw from these experiments is not rooted in the data. Furthermore, and perhaps more concerning, the network activity of P11 "anesthetized" mice in this dataset seemingly contradict the main results that are presented in the remainder of the manuscript.

1) The activity of anesthetized P11 mice displayed in figure 6 greatly differs from anesthetized age-matched mice in the rest of the manuscript.

2) The average theta bandpower of N20 mice in figure S3D is less than half of those of age-matched mice in figure 3E (~3.7x10-4 vs 8.9x10-4). These values would be much more similar to P4 (2.9x10-4) and P18 (3.4x10-4) mice than to the P11 ones (8.9x10-4) that are plotted in figure 3E.

3) The peak in the Φ PSD of figure 6F for both anesthetized and unanesthetized mice is virtually indistinguishable to that of P18 mice in figure 3D (and roughly half the size of that of P11 mice).

4) The N20 mice in figure S3G have a % of cells with a significant STTC that is less than half than age-matched mice in figure 4E. The values in figure S3G are actually much closer to the P18 group than the P4 one. How can that be?

5) Could the authors verify whether anesthesia affects other parameters that are central to the thesis of the manuscript such as the Gini coefficient of CaT etc.?

6) I find the provided data does not corroborate the statement that neuronal network activity under nitrous oxide closely resembles that recorded in unanesthetized mice. Several parameters that are important to the thesis of the manuscript such as STTC, population coupling etc. are affected by anesthesia. As a general concern, providing a comparison between anesthetized and unanesthetized mice at one single developmental timepoint does not give much insight into whether the developmental processes that are described in the paper are biased by anesthesia. While experimentally addressing this concern is time consuming, it should be discussed.

7) Line 125: what is this event detection routine based on analyzing mean ∆F(t) that you compared CATHARSIS to? Overall, the information provided to assess the quality of the calcium transient extraction pipeline is scarce, and its validity has to be taken at face value. It would be comparable to an electrophysiology paper using its unique spike sorting algorithm. While I can understand that extracting calcium transients from a densely packed brain area such as the rodent CA1 has its own unique challenges, this is now routinely done using established pipelines. For instance, a recent paper (Dard et al., 2022, also published in eLife) used suite2p to extract calcium transients from the developing CA1 network (same developmental phase). I would suggest the authors to attempt at replicating their results using this more established calcium transient pipeline.

8) Line 189: figure 3C and the manner in which the term "continuous activity" is used in this paragraph is perplexing. Brain activity is discontinuous (alternation of low-activity (silent) state and high activity periods) in early development, but it should already be continuous and adult-like at P18 if not already at P11. It is therefore perplexing that several P18 mice have a time in continuous activity (Figure 2C) that is well below 50% and a few even below 20%. If this is an effect of anesthesia, it is concerning and a datapoint that goes in the direction of N2O having a major impact on hippocampal activity (anesthesia seems indeed to reduce CaT frequency also in the data presented here, see Figure S3C). If this depends on the manner in which "continuous activity" is defined/computed, perhaps a different term should be used.

9) The authors write that a statistical mixed-effect model is not applicable in their opinion due to low numbers of FOVs/mouse. However, the data are not independent and a mouse with 4 FOVs biases the data distributions much stronger than a mouse with only 1 FOV. This is especially important since an overlap of FOVs cannot be ruled out as they write in their methods. If the authors don't want to use mixed-effect models, they should take mice as statistical unit by taking the average of each mouse, as it's also done in many of their cited studies. A minor point here, in Figure 4 D the number of neurons is written in the legends. For P11 mice 11 FOVs and for P18 mice 12 FOVs were recorded, resulting in 161 neurons for P11 and 100 neurons for P18, respectively. How do the authors explain the substantially higher yield in P11 mice? Might differential effects of anesthesia play a role?

10) I appreciate that, in the revised manuscript, the authors considered the concerns regarding the unwanted effects of anesthesia and performed additional experiments in unanesthetized P11 mice. However, as they write, anesthesia has age-dependent effects on network activity. Especially, the emergence of an active sleep-wake cycle (at ~P14) is suggested to co-occur with frequency-specific (i.e. altered network dynamics) effects of anesthesia (Ackman et al., 2014; Chini et al., 2019; Cirelli and Tononi, 2015; Shen and Colonnese, 2016). Thus, their anesthetic strategy might affect their comparisons between P18 and younger mice.

Reviewer #1 (Recommendations for the authors):

The authors addressed all my concerns.

Reviewer #2 (Recommendations for the authors):

The authors have added new experiments in non-anesthetized mice, and substantial new analysis, modeling, and interpretation. Through this revision they have addressed all of my previous concerns.

Reviewer #3 (Recommendations for the authors):

The manuscript by Graf et al., investigates the population dynamics of the mouse CA1 hippocampal area across the first two weeks of extra-uterine life. The manuscript leverages the combination of experimental data and modeling to identify P11 as a developmental stage in which network burstiness peaks due to network bi-stability. An increase in synaptic inhibition is suggested as being the reason behind this transient network characteristic.

The revised manuscript employs a series of innovative and state-of-the-art analytical techniques and the modeling work is elegantly used to try to get mechanistic insight into the processes underlying the network properties and how they evolve throughout development. The modeling section of the paper is very high quality, yet it is not always clear how it relates (or how it explains) the experimental data that is presented in the first part of the manuscript (see below for comments). The authors try to explain the link between experimental and modelling work by discussing published data from in vitro, electrophysiological and imaging studies in CA1 but also in sensory areas. Due to the methodological variability as well as diverse selected age ranges in these studies, it is unclear how they relate to the ones included in the manuscript. Although the authors might refrain from doing manipulation experiments, they could image GABAergic neurons to better understand their contributions to NBs.

In line with the concerns listed below, the manuscript does provide solid experimental and theoretical evidence for its conclusions.

I appreciate the work that was done to investigate the influence that N20 anesthesia has on hippocampal network activity, but I find that the conclusions that the authors draw from these experiments is not rooted in the data. Furthermore, and perhaps more concerning, the network activity of P11 "anesthetized" mice in this dataset seemingly contradict the main results that are presented in the remainder of the manuscript.

– The activity of anesthetized P11 mice displayed in figure 6 greatly differs from anesthetized age-matched mice in the rest of the manuscript.

– The average theta bandpower of N20 mice in figure S3D is less than half of those of age-matched mice in figure 3E (~3.7x10-4 vs 8.9x10-4). These values would be much more similar to P4 (2.9x10-4) and P18 (3.4x10-4) mice than to the P11 ones (8.9x10-4) that are plotted in figure 3E.

– The peak in the Φ PSD of figure 6F for both anesthetized and unanesthetized mice is virtually indistinguishable to that of P18 mice in figure 3D (and roughly half the size of that of P11 mice).

– The N20 mice in figure S3G have a % of cells with a significant STTC that is less than half than age-matched mice in figure 4E. The values in figure S3G are actually much closer to the P18 group than the P4 one. How can that be?

– Could the authors verify whether anesthesia affects other parameters that are central to the thesis of the manuscript such as the Gini coefficient of CaT etc.?

– I find the provided data does not corroborate the statement that neuronal network activity under nitrous oxide closely resembles that recorded in unanesthetized mice. Several parameters that are important to the thesis of the manuscript such as STTC, population coupling etc. are affected by anesthesia.

As a general concern, providing a comparison between anesthetized and unanesthetized mice at one single developmental timepoint does not give much insight into whether the developmental processes that are described in the paper are biased by anesthesia. While experimentally addressing this concern is time consuming, it should be discussed.

Line 125: what is this event detection routine based on analyzing mean ∆F(t) that you compared CATHARSIS to? Overall, the information provided to assess the quality of the calcium transient extraction pipeline is scarce, and its validity has to be taken at face value. It would be comparable to an electrophysiology paper using its unique spike sorting algorithm. While I can understand that extracting calcium transients from a densely packed brain area such as the rodent CA1 has its own unique challenges, this is now routinely done using established pipelines. For instance, a recent paper (Dard et al., 2022, also published in eLife) used suite2p to extract calcium transients from the developing CA1 network (same developmental phase). I would suggest the authors to attempt at replicating their results using this more established calcium transient pipeline.

Line 189: figure 3C and the manner in which the term "continuous activity" is used in this paragraph is perplexing. Brain activity is discontinuous (alternation of low-activity (silent) state and high activity periods) in early development, but it should already be continuous and adult-like at P18 if not already at P11. It is therefore perplexing that several P18 mice have a time in continuous activity (Figure 2C) that is well below 50% and a few even below 20%. If this is an effect of anesthesia, it is concerning and a datapoint that goes in the direction of N2O having a major impact on hippocampal activity (anesthesia seems indeed to reduce CaT frequency also in the data presented here, see Figure S3C). If this depends on the manner in which "continuous activity" is defined/computed, perhaps a different term should be used.

The authors write that a statistical mixed-effect model is not applicable in their opinion due to low numbers of FOVs/mouse. However, the data are not independent and a mouse with 4 FOVs biases the data distributions much stronger than a mouse with only 1 FOV. This is especially important since an overlap of FOVs cannot be ruled out as they write in their methods. If the authors don't want to use mixed-effect models, they should take mice as statistical unit by taking the average of each mouse, as it's also done in many of their cited studies. A minor point here, in Figure 4 D the number of neurons is written in the legends. For P11 mice 11 FOVs and for P18 mice 12 FOVs were recorded, resulting in 161 neurons for P11 and 100 neurons for P18, respectively. How do the authors explain the substantially higher yield in P11 mice? Might differential effects of anesthesia play a role?

I appreciate that, in the revised manuscript, the authors considered the concerns regarding the unwanted effects of anesthesia and performed additional experiments in unanesthetized P11 mice. However, as they write, anesthesia has age-dependent effects on network activity. Especially, the emergence of an active sleep-wake cycle (at ~P14) is suggested to co-occur with frequency-specific (i.e. altered network dynamics) effects of anesthesia (Ackman et al., 2014; Chini et al., 2019; Cirelli and Tononi, 2015; Shen and Colonnese, 2016). Thus, their anesthetic strategy might affect their comparisons between P18 and younger mice.
