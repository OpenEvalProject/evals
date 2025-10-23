# Peer review - Round 1

Editors:
- Demba Ba, https://ror.org/03vek6s52 Harvard University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75769.sa0](https://doi.org/10.7554/eLife.75769.sa0)

This article provides compelling evidence that deep convolutional networks can detect repeating patterns in biological data better than existing methods, in the presence of noise, biological or otherwise. In analyses of data acquired from the brains of primates using various modalities, the authors show that spindles in cortex have a wider spatial distribution that previously thought. Applications of the proposed approach in other settings may lead to novel findings about the distribution of transient oscillatory patterns in the brain.


---

# Peer review - Round 1

Editors:
- Demba Ba, https://ror.org/03vek6s52 Harvard University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75769.sa1](https://doi.org/10.7554/eLife.75769.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "Waveform detection by deep learning reveals multi-area spindles that are selectively modulated by memory load" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Carmen Varela (Reviewer #1).

Comments to the Authors:

We are sorry to say that, after consultation with the reviewers, we have decided that this work will not be considered further for publication by eLife.

Overall, as a group, the reviewers found the application of CNNs to the detection of spindles novel and interesting. More generally, the reviewers thought that a method to detect rhythmic behavior from noisy data could have an important impact on neuroscience research. At the same time, the reviewer expressed some reservations, and felt that the manuscript requires additional work to assess the utility of the CNNs as an addition to sleep biologists' toolkits. Should the authors decide to submit a revised version of the manuscript, we will do our best to have it assessed by the reviewing editor and the reviewers who provided the comments below.

The following represent three main critiques/suggestions from the reviews.

1. The reviewers found the comparisons to existing methods for spindle detection too simplistic and lacking. More specifically, the authors compare their method mainly to the AT method. The reviewers found the lack of details of the authors' implementation of the AT method, and the lack of thorough comparison to spindle-detection algorithms more sophisticated than the AT method, such as the SNR method, surprising. The reviewers suggest that the authors describe their implementation of the AT method in more detail (e.g. threshold selection etc…). The reviewers also suggest that the authors perform thorough comparisons of the CNN to methods/algorithms more sophisticated than the AT method, both in simulations and on the data used in the manuscript. Evidence that the CNN detects substantially more spindles than these methods would motivate its adoption by biologists.

2. The reviewers felt that the analyses do not support the authors' interpretations and their claims of new scientific findings. First, differences in spatial sampling of neural activity by EEG, EcOG and iEEG, together with the fact that volume conduction may contribute to synchronous activity, limits the interpretation of the authors result. Second, a line of work by Dehghani, Cash, Halgren and colleagues investigating the spatial extent of spindles suggest a lack of synchrony: e.g. (1) doi: 10.1152/jn.00198.2010, (2) doi: 10.1002/hbm.21183, (3) doi: 10.1016/j.clinph.2010.06.018. The reviewers suggest that the authors temper their claims significantly, and put them in the context of the above literature.

3. The reviewers thought the manuscript could benefit from an expanded discussion of the motivation for utilizing the CNN for spindle detection, in particular of how, if at all, they tailored the architecture to the spindle-detection setting. The description of the architecture (layers etc…) provided in the manuscript seems to mirror the description of that developed for gravitational wave detection. More generally, the reviewers thought that a discussion of how to tailor the architecture to the detection of brain rhythms other than spindles would benefit the neuroscience community. For instance, variables such as the length of the rhythmic pattern of interest ought to impact architectural choices.

4. The reviewing editor asks that, where applicable, the authors modify the manuscript to address the comments from the detailed reviews shared below.

Reviewer #1:

Mofrad et al. trained a convolutional neural network (CNN) to improve the detection of multi-area spindles and study their regulation by working memory load. They used the CNN algorithm on three different sleep datasets (scalp EEG from humans that had performed a working memory task, intracranial human EEG, and ECoG recorded from macaques). They find that their CNN method identifies more regional and multi-area sleep spindles compared to an amplitude-based spindle detection method. Importantly, they found that the rate of occurrence of regional and multi-site spindles was higher in the sleep after human subjects performed a high-load visual working memory task, compared to after the subjects performed a low-load visual working memory task.

The results from this study advance the methods used to detect sleep events. As discussed by the authors, most algorithms to detect sleep oscillations in EEG and LFP data are based on amplitude thresholds; this approach is inadequate when studying regional and global spindles, in which the amplitude may not always remain above threshold in all recording sites. The authors overcome this limitation with a ML approach that detects significantly higher numbers of regional and multi-site spindles. The results presented here demonstrate how ML detection algorithms can offer novel insights on the function of spindles; similar approaches could be helpful with other sleep oscillations. Specifically, the results presented by Mofrad et al. suggest that, compared to amplitude-based detection methods, CNNs improve the detection of spindles that occur temporally correlated across cortical regions. In addition, the authors used the CNN spindle detection method on human sleep data after subjects performed a working memory task. The results are consistent with the hypothesis that cross-regional spindle synchronization is regulated by working memory load prior to sleep, providing insight into how specific cognitive processes influence sleep spindles.

An additional strength of this study is the demonstration that the CNN method yields similar results in ECoG, EEG, and iEEG, and in data from macaques and from humans, suggesting that the detection method is applicable across species and across electrophysiological recording methods.

A few points should be considered when interpreting the results. The definition of local, regional, and multi-site spindles used in this manuscript is based on the absolute number of electrode sites in which a spindle was detected. Since the ECoG, EEG, and iEEG have different spatial sampling, the definition could overestimate regional and multi-site spindles in iEEG recordings, particularly in the subjects that had large number of electrode contacts in one brain region. This could contribute to the much higher ratio of global spindles observed in the iEEG data compared to ECoG and EEG. Nonetheless, the analyses that support a correlation between widespread spindles and memory load were based on 64-channel scalp EEG and are not expected to be biased by differences in electrode spatial sampling.

Lastly, the results are interpreted in the context of the systems memory consolidation hypothesis, which proposes that new memories become integrated into neocortical networks in a process that is facilitated by sleep oscillations. The results from the sleep EEG analyses after subjects performed a low- or high- load visual working memory task are indeed consistent with the idea that multi-site spindles contribute to the consolidation of memories formed before the subjects went to sleep. Likewise, the results are also consistent with the synaptic homeostasis hypothesis, which states that sleep oscillations are important in scaling synaptic plasticity of networks that may have been particularly active during wakefulness. The results of this study are therefore congruent with the possibility of multi-site spindles coordinating the homeostatic regulation of synaptic strength across multiple cortical regions in relation to the cognitive load experienced by the subjects during wakefulness prior to sleep.

Recommendations for the authors

The work presented in this manuscript is highly relevant to advance the methods used to detect sleep oscillations, and to understand the functional significance of sleep spindle coordination across cortical areas. The manuscript text and figures are clear and well-organized. Below are suggestions that may help further improve the quality of this work.

The distinction of three spindle types (local, regional, multi-area) based on the co-occurrence across recording sites should be discussed with regard to the different spatial sampling of EEG, ECoG and, specially, iEEG electrodes. For example, spindles detected in multiple recording sites in subjects such as B and C which have multiple contacts in one brain region (Suppl. Table 1), might be incorrectly labelled as regional or multi-area. Although sampling biases are not expected to affect the results regarding memory, it will be helpful for readers to explain how these potential biases were addressed in the analyses of iEEG data. Could the much higher ratio of multi-area spindles in iEEG data (Figure 2c, right panel) be explained by electrode sampling bias? Along the same lines, it may be more appropriate to refer to 'multi-area' spindles as 'multi-site' spindles if they do not necessarily imply occurrence in distinct cortical areas.

It would also be helpful to expand the justification for the choice of CNN algorithms; the text refers to their previous use detecting earthquakes or gravitational waves but is not immediately clear why noise in these applications would be similar to noise in sleep signals.

Line 35: remove 'stage 2': the references provided are mostly from rodents, in which separate NREM sleep stages are less defined; and spindles are not necessarily exclusive of N2 even in humans.

Lines 61,62: Long-range connections are one potential link to temporarily coordinate spindles across cortical areas. Another important set of connections that could coordinate spindles are the thalamocortical projections, mainly those thalamic pathways with widespread projections to superficial layers of cortex (references such as Clasca et al., 2012, Eur J Neurosci 35(10):1524-32. doi: 10.1111/j.1460-9568.2012.08033.x.).

Lines 102-103: please specify how descriptive statistics are reported; are the values reported in parenthesis the mean and standard deviations? Clarify in the methods section how duration was calculated. The methods state that 'The CNN model takes a window of sleep recording (500 ms which is bandpass…)' (Line 303), is that a 500ms moving window? With what step size? What determines the start and end of a spindle in the CNN and AT methods?

Line 161: include p value for local spindles (as done in the figure legend).

Given the unique dataset and methods, and the focus of this work on the locality and globality of spindles, the authors may want to report on potential changes in the density of local spindles specifically over visual and frontal cortical areas. Is it possible that increases in local spindle density are not significant when all regions are considered together but may be significant in certain regions engaged by the visual working memory task? In that sense, it is interesting that the SNR approach detects a (smaller) increase in local spindles with high memory load (Supp. Figure 4a). A more precise analysis of local spindles over relevant cortical areas will not diminish the author's main result on multi-area spindles, but it will provide additional cues on the role of spindle spatial synchronization in sleep and will enhance the value of this interesting work.

Lines 241-242 say that 'the quality of sleep was studied by the degree of spatial synchronization'; it will be helpful to clarify this statement because if the degree of spatial synchronization was used to select the sleep data used for this work, the dataset may include more synchronized activity compared to other datasets. This does not nullify the results, but clarification will be important to ensure replicability. Likewise, the methods used for sleep detection should be described in more detail, was sleep detected in the same way in all datasets?

Line 250: only visual inspection was used to detect stage 2 in the EEG data? clarify if only NREM sleep was used in all datasets used for analysis? (same for the iEEG recordings)

Not clear what is added by the paragraph between Lines 283-288 unless more details are provided. If the model simulates spiking activity in the awake state, is this helpful as a ground truth control for sleep LFP? What type of spiking model? What network architecture?

Paragraph starting in line 290. Was the CNN model trained and optimized for each dataset?

Lines 296-297: 'best' based on what?

Line 350 states that the overall threshold for the AT method was based on the average root mean squared. Was the AT approach developed and applied independently for each data set (EEG, ECoG, iEEG)? It is not clear from the text if the different signal amplitudes in the datasets were considered for AT detection (were the data and RMS normalized?).

Figure Supp. 5: correct typo in the figure legends (spindle)

Reviewer #2:

The primary goal of this paper is to provide evidence that sleep rhythms are more spatially extended than previously known, using a deep learning convolutional neural network (CNN) model specifically designed to characterized rhythmic activity that has not previously been applied to sleep data.

Strengths

1. The authors establish that the CNN method proposed can detect spatially extended sleep rhythms and that difference occur when measuring spindles after a low vs high load memory tasks in multiple data sets.

2. The CNN method presented may provide a powerful technique to characterize a range of brain rhythms and difference across tasks or patient populations.

3. The results and figures are clearly presented.

4. The methods are sound, with the exception that more detail on the method and how it uniquely accounts for rhythmic activity is warranted and should be discussed in the Results section of the paper, rather than in the methods.

Weaknesses

1. The results of the paper do not establish that this CNN method is better than prior methods at detecting spatially extend sleep rhythms, or that the methods is better able to distinguish sleep spindles after a low vs high load memory task. As such, while a new method for detecting spindles is clearly presented, there do not appear to be any new scientific findings in this paper. The authors compare the CNN with only the AT methods for the main result of the paper (Figure 3, Supplementary Figure 3), and not the SNR method. Why not compare directly to the SNR also to see if CNN is actually better? The SNR method is used to generate the data set that the CNN is trained on, as such is it possible for the CNN to do better? Would the AT method be able to pick up more multi-area spindles with a lower threshold?

The CNN and SNR methods are directly compared only for the low vs high memory load task in Supplementary Figure 4. A visual comparison of the low vs high memory load results from the CNN (Figure 3c) and SNR methods (Supplementary Figure 4 top) suggests that the SNR method is equally able to distinguish these conditions. Overall, the advantage of the CNN is not clear.

2. There are several high-level strong claims in the paper that are not directly investigated or supported by the evidence in this paper. For example, "These results thus provide specific neural mechanisms by which memories can be stored in distributed neocortical networks during sleep". "Taken together, these results provide substantial evidence of a specific role for spindles in linking neuron groups distributed widely across cortex during memory consolidation". "The key missing piece is to understand how spindles can guide specific long-range excitatory connections to strengthen during sleep-dependent memory consolidation. We hypothesized that widespread, multi-area spindles might provide this mechansism". At best, the results in this paper provide supportive evidence that spindles could do these things by they do not investigate or establish causality in any way.

3. It is stated that in the ECoG and iEEG data, the AT method detected a subset of spindles that are significantly higher-amplitude than those detected by the CNN methods, using a one-sided Wilcoxon sign rank test. Does this mean that CNN does not detect some of the high amplitude spindles? Is this advantageous? There is something confusing about the way this is stated. A Figure of the distribution in number and amplitude of spindles detected with the 3 methods (CCN, AT, SRN) would be useful.

4. The 3 different recording methods sample activity across different spatial scales, and depth electrodes (iEEG) are sampling vastly different areas (i.e. deeper sources) than ECoG and EEG. As such, it is difficult to relate findings related to "simultaneous spindle detection" in local, regional, multi-area electrodes across these three different measures. A primary concern is that the finding that there are more multi-area spindles (e.g. Figure 2b for iEEG – similar results for EEG and ECoG are not quantified) could be due to volume spread of the spindle source. Is there a way to rule this out? There are ways to minimize the influence of volume conduction with EEG and ECoG source analysis, however, to my knowledge, these methods currently don't exist for iEEG.

Recommendations for the authors:

In Figure 1d, there appear to be other spindle in each of these example traces. Were these not picked up by the algorithm, or simple not highlighted in red? Clarification would be helpful.

Why are the randomly sampled red dashed line in Supplementary Figure 1 not flat? Is the 1Hz filter somehow biasing the amplitude at the center?

It would be helpful to see the results shown in Figure 2b for iEEG for ECoG and EEG data as well.

There is are claims about SNR and CNN being independent of spindle amplitude. Clarification of how the SNR power calculations are independent of amplitude would be useful.

The methods state "We first tested CNN models with different architectures and selected one of the best architectures across sleep recording data sets". What does "one of the best" mean? Quantification would be helpful. Overall, clarification of advantages of this CNN method in identifying rhythmic activity, other than training on rhythmic activity (?), would be helpful.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Waveform detection by deep learning reveals multi-area spindles that are selectively modulated by memory load" for further consideration by eLife. Your revised article has been evaluated by Timothy Behrens (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

We thank the authors for carefully considering the feedback they received during the first round of reviews, and for performing additional analyses and modifying their manuscript with the feedback in mind. We also thank the authors for patiently waiting for these reviews. The reviewers found the new version of the manuscript a substantial improvement compared to the first submission. The reviewers feel that additional changes and clarifications can put the authors' contribution in its proper context, and broaden the reach of their contribution in the community. The reviewers think the authors ought to

1. Make their comparisons of the CNN and AT methods in the presence of noise more realistic than currently. Experimentalists would care, for instance, about robustness of the CNN, compared to the AT method, to biological forms of noise (e.g. confounding oscillations such as a brief period of REM theta synched across channels, does the CNN offer an advantage to the AT in that case?). Moreover, the authors seem to have made the comparisons with a fixed noise level/SNR (not to confuse with the 'SNR' method). Does the choice of noise amount have a biological basis? The authors will find text in the reviews unpacking this comment

2. Clarify apparent inconsistencies in certain statistics reported (e.g. spindle rates), as well as conduct statistical tests for some of their data more appropriate than ones currently used. The authors will find text in the reviews unpacking this comment

3. Tone down claims of generality of the CNN, and provide clear explanations for what makes the choice of architecture suitable to the current application to spindle detection. The reviewing editor finds this the most important piece of feedback from the reviews. As written, the reviewing editor feels that the manuscript may promote a culture of using deep learning in neuroscience without understanding how deep learning works. The authors have a unique opportunity of not only presenting an application of deep learning that leads to new scientific findings/hypotheses but also of doing so in a manner that promotes a culture of looking inside the black box and trying to understand it. The authors will find text in the reviews unpacking this comment

Reviewer #1:

The manuscript has improved substantially and many of my concerns have been addressed. The deep-learning spindle detection method is more fully reported and the new controls with simulated data (varying noise and amplitude) are an improved approach to compare the CNN and AT methods (Figure S1, new Supplementary Table 1). The new analyses investigating the rotating spindle waves provide a framework for understanding the differences with prior reports of low synchrony.

However, there are several important concerns that should be addressed.

The new comparisons between CNN and AT models using surrogate data with systematically varied noise are useful. However, what was the rationale to compare the specific types of noise presented in Supplementary Table 1? Both the CNN and the AT have similar sensitivities and specificities for all noises, which may suggest that the different noise conditions do not constitute substantially different challenges for the detectors (also suggested by the example in Supplementary Figure 1, in which the spindle has a high signal to noise ratio with all types of noise). I think the readers will be more convinced of the value of the CNN method it can offer an advantage under a 'noise' condition in which the traditional AT methods are likely to struggle. For example, a more interesting source of noise may be the presence of non-spindle oscillations due to brief state changes (e.g., REM or α), or noise artifacts (e.g., examples in Supplementary Figure 12). The sensitivity of traditional methods is likely to go down in examples like these, how does the CNN compare?

Line 92: "co-occurrence"; please clarify the time window or time overlap used to determine co-occurrence. Did any amount of time overlap between spindles count as co-occurrence? Likewise, in Line 150: "simultaneously detected spindles", line 151: "based on co-occurrence". I think it's worth emphasizing in this paragraph that 'co-occurrence' and 'simultaneous' detection do not imply 0-lag synchrony (as discussed in the 'rotating waves' sections).

Lines 102 and 104: "low and high visual memory task" should be "low and high-load…" (also in the Figure 3 legend, and in lines 261-262, 263: 'high-load' visual memory tasks).

There are some inconsistencies in the reported rates (spindles/min) across analyses and figures: Suppl. Figure 4a indicates average spindles/min around 4-5/min in all data types, including EEG data used in the visual memory task. However, the average from the distributions shown in Figure 3b seems much lower, even when combining all spindles across each memory condition, e.g. for the H-VM is about 1/min in local and regional and about 0.5/min for multi-area. In other words, could you clarify how the averages of the distributions in Figure 3b add up to 4 spindles/min in Figure 4a? In addition, in Figure 3b, within the low-VM condition the rate of multi-area spindles is substantially lower (< 0.5/min) than local and regional (about 1/min on average); and within high-VM the rate also appears much lower (<1/min) for multi-area compared to the distributions for local and regional spindles (up to ~2/min). The text indicates p-values for what seems to be a comparison of relative rates (between H-VM and L-VM), which is interesting but is this result due to a significantly lower multi-area spindle rate with low memory? Based on the figure it looks like multi-area spindles occur at lower rates regardless of memory load? It will be helpful to provide statistical comparisons of spindle rates (among all spindle types) within each condition (L-VM, H-VM) so that the relative changes with memory can be interpreted in the context of the absolute spindle rates in each memory condition. Based on the distributions it seems that non-parametric tests would be more appropriate than t-tests.

Suppl. Figure 4: missing (a),(b) labels. Supplementary Figure 4a is not described in the text?

Line 725: 12? sites

Line 154: it'd be useful to reference the Supplementary Table 2 (with the list of the cortical regions).

Lines 170, 171: I believe the verb should be in past tense.

Line 179: The interpretations regarding the association between the visual memory load and subsequent sleep spindles is limited to memory consolidation processes. However, memory performance after sleep was not studied in this work, therefore "the impact on memory consolidation" cannot directly be assessed. Sentences such as these (lines 179-180): "If this is the case, what is the impact of the distribution on sleep-dependent memory consolidation? To answer this question…" could be rephrased to state the key question that the data can address. Other sentences in the manuscript are more accurate and valuable in this respect, e.g., Lines 289-290 "(2) this spatial extent can be modulated by the specific memory conditions prior to sleep (Figure 3)". Indeed, memory consolidation is one of several mechanisms that determine how wakefulness influences sleep oscillations. The authors correctly cover literature on the association between memory and spindles "An increase in spindle density after memory tasks and its relationship with memory consolidation is well established (Clemens et al., 2005; Dang-Vu et al., 2008; Gais et al., 2002; Schabus et al., 2007, 2004)", but the impact of the authors' findings would be enhanced by discussing other hypotheses in the sleep field that are also consistent with the presented results; for example, the high-load working memory condition may increase firing rates and entrain downscaling processes during subsequent sleep (Tononi and Cirelli, 2014; Crunelli et al., 2018; Klinzing et al.,2019).

Paragraph starting 215: is this only with the EEG data?

Figure 4a: missing (a),(b) labels for the plots. Indicate the x,y value of the removed outlier point in parenthesis (in 'a' and 'c') since it's not in the plot but still used in quantifications.

Line 552: "We simulated 60-minutes recording containing" should it be "60-minutes of recording…"?

Reviewer #2:

The authors suggest that the lack of algorithms for reliably identifying spindles in neural recordings has led to the under reporting/underestimation of the spatial extent to which spindles occur in the brain. The authors propose an approach based on CNNs that they claim can detect spindles more reliably than existing ones, lead to new insights as to how cross-region spindles may contribute to the integration of 'information' across brain areas.

Strengths

1. The applicability of the proposed methods to neural data from multiple modalities, i.e. EEG, EcOG and iEEG.

2. The framework the authors lay out for constructing high-quality data sets to train the CNNs.

3. The combination of computational methods and new suggested insights into how spindles can facilitate the integration of 'information' across brain areas.

Weaknesses

1. The authors could improve the explanations as to why the CNN seems to do better than legacy methods such as the AT. The explanation surrounding the CNN's ability to detect spindles of different amplitudes does not seem satisfactory enough.

2. The authors claim the applicability of the CNN to data from different modalities, and its generality, as a strength. Given the black-box nature of CNNs, and the lack of an attempt in the manuscript to explain the CNN, its success/failure modes, which aspects of the data it focuses on to detect spindles (e.g. saliency maps), these claims do not feel justified to the reviewer and may contribute to the proliferation of black-box CNNs in neuroscience

Recommendations for the authors:

The reviewing editor found the manuscript a much improved version of the initial submission.

1. The reviewing editor found that the analyses currently in the manuscript do not support the authors' claims of generality of the CNN (e.g. lines 376-377), and that the language surrounding these claims may contribute to supporting an already-widespread tendency to utilize black-box neural networks for analyzing neural data.

a) One feedback from the first round of reviews had to do with the lack of details surrounding the CNN. The reviewing editor appreciates the authors' attempt to improve this. The authors seem to want to emphasize the generality of the architecture. Such claims of generality do not give insight to the reader on how to pick an architecture for detecting oscillatory patterns in a different context (e.g. ripples). The success of the architecture for gravitational wave detection, its use in the current manuscript, do not give license to use it w/o changes in any application.

A practitioner would appreciate guidance on architecture design. Given the length of pattern of interest and a sampling rate, a user would want to know how to pick filter sizes. For instance, for a patter of length 0.5 seconds, a 256 Hz sampling rate, the effective filter (explained below) associated with an architecture ought to have size on order of 100 samples (0.5*256 = 128 samples), not 10 or 1000. The reviewing editor thinks this manuscript could have a much stronger impact if the authors took such questions into considerations. Have authors visualized the filters they learn? Have they considered generating saliency maps to determine which parts of inputs the network focuses on to detect spindles? At present, the emphasis on the generality of the CNN, w/o considerations for what about the authors' specific context makes the choice of architecture suitable (other than the fact that it works for gravitational-way detection) feels a bit disappointing.

More details on guidance on how to design architecture/why current architecture works: For any conv net, the choice of filter size at each layers, together with number of layers relates to size of features one would like to detect. Each layer a conv. Composition of conv equals a conv with a filter size roughly proportional to the sum of filter sizes at each layers. 7x7 filters not uncommon in image proc. Cascading 3-4 such layers (ignoring nonlinearities) gives a filter with an effective 30x30 size.

Concrete suggestions: (a) adding text to the manuscript explaining what what about the authors' specific context makes the choice of architecture suitable (other than the fact that it works for gravitational-way detection), (b) visualizing filters learned by the architecture, (c) consider generating saliency maps.

(b) The reviewing editor feels that the authors can improve the section detailing the training of the CNN. The editor suggests the authors consider using a table to summarize different aspects (number of layers, filter sizes etc….). The editor also suggests that, very early on, the authors mention the subject-dependence of the training.

2. Misc questions

(a) In supplementary figure 4b, the scatter plot for EEG (green) suggests a similar max PSD for the CNN and AT. I would expect a similar rate of spindle detection. Supplementary figure 4a suggests otherwise. Can the authors explain?

(b) In Figure 2c, EcOG the fact that the CNN detects fewer local and regional spindles per minute than the AT method requires explanation. Does this figure refer to correctly detected spindles? Should the editor interpret the lower ratio as the AT method having more false alarms than the CNN?
