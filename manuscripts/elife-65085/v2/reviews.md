# Peer review - Round 1

Editors:
- Noah J Cowan, Johns Hopkins University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65085.sa1](https://doi.org/10.7554/eLife.65085.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This is an exciting paper and provides new insights into sensorimotor learning for delay, including its time course, limits, and sensory mechanisms.

Decision letter after peer review:

Thank you for submitting your article "Learning to stand with unexpected sensorimotor delays" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Noah J Cowan as Reviewer #1 and Reviewing Editor, and the evaluation has been overseen by Ronald Calabrese as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. All reviewers agree there is the potential for this paper to provide a significant contribution to the literature, but there was strong agreement across the reviewers that there are fundamental gaps in the analysis and, potentially as a result, the interpretation of the results. In addition, each reviewer has read each others' reviews, and all three reviewers agree with the technical points of the other reviewers, and so each of these should be addressed in a revision.

Summary:

This manuscript will be of interest to a wide range of readers interested in motor control, motor adaptation and motor learning. Using an innovative robotic system, artificial time delays from muscle forces to movement were imposed during standing balance. The results clearly show both the difficulties that the imposed delays have on stabilizing movements and the ability of individuals to adapt to the imposed delays to maintain balance. This provides insight into how the nervous system is able to use sensory information to control movements under normal conditions given the time delays inherent in sensory, motor and neural processes.

Essential Revisions:

1. To characterize how strongly soleus EMG (the output) responds to vestibular stimulation (the input), standard measures designed to characterize input-output mappings should be used. Gain in the frequency domain and the unnormalized impulse response function in the time domain are the standard choices. Both measures used do not distinguish between decreases in EMG variability and gain.

1a) Coherence (while important to report) does not provide even an indirect measure of gain: two systems with gains different by an order of magnitude both reach maximum coherence of 1, depending on the amount of noise in the system. In terms of this research result, if an imposed delay increases output variance but does not change gain, then coherence decreases. Presumably soleus EMG variance increases with sway variance, so the decrease in coherence and Figure 6, for example, may simply reflect an increase in soleus EMG variance, not a decrease in the magnitude of vestibular-evoked muscles EMG responses.

2a) The authors use normalized cumulant density in the time domain as a stand in for gain. In principle, an unnormalized version of this should work, as it is related to the impulse response function (but not quite). It would be better to just directly use the standard estimate based on cross spectrum divided by the power spectrum of the input, rather than the normalized IFT of the cross spectrum that the authors used. But, by normalizing by the EMG signal properties (also by electrical stim -- but that would be the same/similar for all subjects), if EMG variance is increased with increasing delay (a plausible result), the cumulant density function amplitude would decrease due to this normalization, even if the vestibular gain remained unchanged.

So, in your revision, we require the use of a standard measure, e.g. cross spectral density between the input and output (as now calculated) divided by the power spectral density of the input. This would give a frequency domain response function. Taking the inverse Fourier transform would put this in the time domain as an estimate of the impulse response function. Other standard measures are possible.

Critically, this change in analysis may provide a new result, and thus require new interpretation. E.g., it may be that the "scalar" gain estimate does not change, but rather there is a change in the variance that explained your previous analysis. In this case, the transfer function estimate could be examined for alternative interpretations. The reviewers all felt that while this would not necessarily be as striking a result, it would still be nevertheless an important paper, and so it is important when re-analyzing this data not to have the forgone conclusion of a change in gain, which is not yet supported by the analysis.

2. We emphasize one of the major concerns of reviewer #2: Rather than report mean-removed RMS sway (in other words, sway standard deviation) it would be better to report percentage of time within specified sway limits

3. The authors should address whether existing models can stabilize an inverted pendulum with long feedback time delays. Sway variance will increase with increasing time delay, so at some point standing balance is not possible due to one's finite base of support (a type of plant nonlinearity). Specifically, the manuscript should be improved with a more nuanced Discussion (near lines 401-421) to consider the other classes of control models (optimal or intermittent control) that possibly could be candidates for controlling a system with long time delays. For example, if optimal control rather than proportional-derivative control is used, then it is possible in principle (perhaps excluding special cases) to stabilize a linear plant with arbitrarily long delays (e.g., Zhou and Wang 2014, DOI 10.1007/s10957-014-0532-8), although for long time delays such control can be quite fragile with respect to disturbances or plant parameters.

4. Bootstrapping should be better justified or not used.

Reviewer #1:

This paper aims to understand how imposed delays between ankle torque and whole-body motion destabilize standing balance, and determine the mechanisms that the nervous system uses to learn to compensate for these imposed delays. Related studies have estimated the critical delay at which upright standing is destabilized, and shown that humans can learn to compensate for increased delay. This study supports these prior results in the literature and delves deeper into human's standing balance. Specifically, they demonstrate that, although initially vestibulomotor responses are attenuated during imposed delays before learning, eventually subjects learn to partially recover their reliance on vestibular feedback, while, at the same time, improving postural control in the face of delay. Furthermore, after learning, subjects' ability to perceive unexpected delays was reduced, leading the authors to speculate that subjects may learn to "internalize" the experimentally added delay, making it hard to identify said delay an external perturbation. So, this study would be of broad interests for researchers who are studying human control of standing balance as well as other models of sensorimotor control across taxa.

Strengths:

1) The manuscript provides a clear and cogent motivation, and the hypotheses are well grounded in the literature.

2) The data, including the tables and graphs in this manuscript, verify the authors' hypotheses in a generally convincing way.

Weaknesses:

1) Clarification of velocity variance with bootstrapping: The estimates of sway velocity variance using bootstrapping was not well described nor justified. In figure 2, it said 'Sway velocity variance ..., and the resulting data were bootstrapped to provide a single estimate per participant and delay'. 'estimate per participant' sounds like simply using bootstrapping to estimate the mean, which is not a standard use of bootstrapping. It can be used to estimate SEM etc, also in line 795-797, it said 'we bootstrapped the participant's data with replication 10,000 times and then averaged across participants for each delay and learning condition.' from which it seems that the authors are computing the SEM across subjects. In sum the statistics associated with variance estimation and bootstrapping is unclear.

2) The use of Cumulant Density: cumulant density as a gain measure is not a standard technique for gain estimation in the motor control literature, and needs further justification.

3) The use of 2s windows for variance estimation in Experiment 1 was unclear. When estimating sway velocity variance in Experiment 1, 2s non-overlapping windows were applied and "if fewer than five 2 s windows were present, the average was taken across the available data (denoted with filled circles in figures)". And in Figure 2A, "Data not included in the velocity variance analysis are grayed out." However, some non-grayed-out regions in Fig 2A are not to be multiples of 2s, which is confusing.

Although the experimental methods, data analysis and writing skills in this paper are detailed, some improvements are needed for figure illustrations and terminology.

For example, Figure 1B is confusing. There is a circle with δ t inside which represents the imposed delay but it is not good to put both the "Whole body sway" and "Delayed whole-body sway" out of that circle. This is a confusing (and nonstandard!) way of schematizing a closed-loop system such as this. See many examples from the literature, including but not limited to papers by Lena Ting, Michael Dickinson, Daniel Robinson, my lab, and many others for standard ways of writing control system block diagrams that would be more easiliy interpretable. Lena Ting's lab (Lockhart and Ting 2007, expressed in time domain) and Simon Sponberg's lab (https://science.sciencemag.org/content/348/6240/1245.abstract, expressed as a general block diagram) both have nice papers that explicitly include delay in the feedback loop. My lab has three review papers with numerous examples that can be found here: https://limbs.lcsr.jhu.edu/publications/#Reviews.

Some figures in this paper are not straightforward for the readers to understand. Especially in Figure 1, the descriptions are complete, but figures themselves are not informative enough. For instance, in Figure 1 C, the descriptions of the experiment 3 whose trials ("of similar design to Experiment 2B, except that the robot only transitioned between baseline (20 ms) and 200 ms delays (not illustrated)") is unclear. This figure is significant to the paper's results in order to show the procedure of three experiments. Thus, it should be better clarified, or supplemental figures should be used to further explicate such issues.

More details about the load in Figure 1B is needed. We can only learn from line 541 that "For all experiments, participants stood on a custom-designed robotic balance simulator programmed with the mechanics of an inverted pendulum to replicate the load of the body during standing (Figure 1A)". However, the authors need to show in specific equations that were simulated, and the parameters they set in their design, to enable reproducibility of the results.

Moreover, important data points should be marked on the figure. On Figure 1E, the y axis "imposed delay" has only 20 ms and 300 ms marked, but authors later mentioned that "Data from a representative participant (see Figure 1E) show missed 299 detections of the 100 and 150 ms imposed delays", so it would be clearer if they can also mark 150 ms and 100 ms on the graph, because those are critical points.

RE: Cumulant Density: It is indeed critical to have a gain estimate in the vestibulomotor analysis, since coherence alone does not indicate the strength of response to a stimulus: nonlinearities and noise can decrease coherence, even if the gain to stimulus remains unchanged. The authors perform such a gain analysis (see e.g. Figure 4A) using "Cumulant density". This is an interesting technique for identifying the sensorimotor gain but does not seem to be in widespread use, and I could not find a theoretical justification in the system ID textbooks I have. That said, it appears possible that under the right conditions, the appropriately normalized Inverse Fourier Transform of the cross spectral density (i.e. the so-called Cumulant Density) should amount to the impulse response function, but I'm not sure of this. It would be helpful if the authors could better justify this approach or use a more standard analysis, such as impulse response recovery.

The authors call the Vestibular-Evoked Muscle Responses assays an "Experiment" (Experiment 2A), but the experiment is actually much broader, and covers all everything in the gray box in Figure 1C. Likewise for the perception assay ("Experiment 2B"). This terminology is confusing and I recommend dropping that nomenclature and just saying "Vestibular Testing" and "Perceptual Testing". Also, Figure 1C is laid out to look like a table, with two rows, and the first "column" appears to be labeling the rows, but it is not. Please rework this panel to be less confusing.

Reviewer #2:

Using a robotic system, the manuscript demonstrates that imposing time delays from ankle torques to movement causes postural sway to increase, as one would expect based on stochastic models of postural control. What is more surprising is the extent to which participants can adapt to imposed delays and decrease postural sway over multiple days. The evidence of adaptation is exceptionally clear. Another strength of the manuscript is that it relates these decreases in postural sway to a decrease in how often participants perceive unexpected balance movements, suggesting that over time participants learn that their ankles torques are causing the movements even though the movements are artificially delayed. These perceptual measures were obtained in real time during standing balance and carefully characterized, sometime that is not typically done in postural adaptation experiments.

The manuscript also characterizes the relationship between vestibular stimulation and surface electromyography EMG signals from the soleus muscle, using coherence in the frequency domain and the normalized cumulant density function in the time domain. Often gain, which has units of (output units)/(input units), is used to measure how responses to a perturbation change. A common example is using gain to quantify sensory re-weighting during standing balance. (It would be helpful if the authors discussed whether their hypothesized changes in vestibular-evoked muscle responses can be thought of as sensory re-weighting.)

One concern is whether the measures used in this study conflate changes in output magnitude with changes in output variance. For example, if an imposed delay increases output variance but does not change gain, then coherence decreases. For this reason, gain seems a better choice than coherence given the questions the authors are addressing. Similarly, in the time domain, an unnormalized impulse response function seems a better choice than the normalized cumulant density function. Similar comments apply to the time-frequency analysis of Experiment 3, which the manuscript uses to track changes in the relationship between vestibular stimulation and soleus EMG.

One important implication of the reported results that is discussed is that models that predict the maximal sensorimotor delay that allows standing balance are probably underestimating the maximal delay because they assume proportional-derivative (PD) or proportional-integral-derivative (PID) controllers, which are not optimal controllers when there are time delays. The predictions are also based a linear analysis of stability. In reality, due to a person's limited base of support, the person may fall or take a step even though a linear analysis shows that they are stable. It might be helpful to discuss this in relation to the study's imposition of specified limits of body sway.

One other issue that would be helpful to discuss in more detail would the exact sensory consequences of the imposed delays used in this study. The researchers imposed delays from the forces participants produce (forces applied to the support surface) to body movements. This delays sensory feedback related to body movements, but other sensory feedback, such as proprioceptive feedback about muscle forces and cutaneous feedback about the center of pressure (COP) have normal sensory delays. The component of COP dependent on center-of-mass position is delayed but the component dependent on ankle torque is not. Even the way proprioceptive information about muscle length is altered is more complex than a simple time delay, since length changes in tendons allow changes in muscles lengths without joint rotations. It would be helpful to discuss whether the resulting sensory conflicts contribute to the difficulty of balancing with an imposed delay and the implications for adaptation.

Abstract: It would be helpful to mention that sway was restricted to rotation about the ankles.

Figure 1 caption: Why was it necessary to use 3D googles to provide a visual scene to participants? Since the participants are actually moving, would it not be easier just to have participants look at an actual fixed visual scene?

Lines 171-174: Does "both p < 0.001" refer to overall tests for dependence on imposed delay? If so, it would be helpful to indicate which statements in this sentence are supported by statistical tests.

Lines 212-217: The comparing the retention test to sway attenuation corresponding to the time constant seems arbitrary and apparently does not take into account uncertainty in the estimated time constant. To support the statment that "balance improvements were partially maintained" it seems more relevant to compare the retention test to sway variance at the beginning of training to test whether improvements are at least partially maintained and to sway variance at the end of training to test whether improvements are only partially maintained.

Line 521: What was the range of participant ages?

Line 554: The delay from specified to measured motor position was estimated to be 20 ms. Is this with the inertial load of the backboard and participant? Should this be thought of a pure time delay or some other type of frequency response function (transfer function)?

Line 558: The linear least squares predictor algorithm used to synchronize the visual motion with the motors is not described in sufficient detail in the cited reference (Shepherd 2014) to permit others to reproduce this aspect of the experimental setup. It would be helpful to do so here.

Line 569: It would be helpful to specify the functional form and parameters of the stiffness that "caught" the backboard when it exceeded the specified limits.

Line 590: Does "reaching a limit" mean crossing from outside to inside the specified limits?

Lines 674-754: The text describing the protocols for Experiments 2A and 2B refer to pre-learning and post-learning testing, consistent with Figure 1C, but I cannot find where the details of these testing procedures are described. It would be helpful to explicitly refer to pre- and post-learning testing when describing these testing procedures in this section of the manuscript.

Line 697: Please clarify what it means that "Participants then completed Experiment 2A or 2B testing" during the retention testing.

Line 718: Was the range of root-mean-square amplitudes of the electrical vestibular stimulation due to stochastic variation or was amplitude systematically varied?

Line 712: Were conditions tested in order from small to large delays, as in Experiment 1?

Line 719: Does "pseudo-random order" refer to the order of trials within each condition?

Line 746: Was the transition from the 20-ms delay to the experimental delay instantaneous?

Line 746-750: It would be clearer to only use the term "transition" to refer to a change in imposed delay and use a different term to refer to the period of time during which the experimental delay is imposed.

Line 750: Please explain the reason a "catch" 20-ms delay was included in the experimental protocol, since this seems to be the same as the baseline delay. Did anything actually change in how the robotic system was controlled when the "catch" 20-ms delay was imposed? In other words, was the failure to find an effect preordained?

Line 776: Does the term "window" here mean the same thing as term "inter-transition delay" on Line 747? If so, it would be helpful to use the same term in both places.

Line 785: It is implied that the 2-s windows excluded periods of time when body angle was outside the specified limits, but it would be helpful to explicity state this restriction up front.

Line 795: What was bootstrapping used to estimate, the average variance for that participant? Why not just use the actual average variance, as was done when there were fewer than five 2-s windows? Bootstrapping is typically done to test a null hypthosis or construct a confidence interval and assumes independent samples, which would not be the case for data from the same participant.

Line 812: Did the 2-s window have to start after the delay was imposed AND end before the button press?

Line 821: Does concatenating the trials mean that the jumps in signal values from the end of one trial to the beginning of the next are affecting the results?

Reviewer #3:

The study describes three experiments that investigated the influence of increased feedback time delay in the ability of human subjects to maintain stable upright balance and their ability to learn/adapt to control balance at time delays values that are greater than those predicted to be possible based on existing simple feedback control models of balance. The studies made use of a unique robot balance device that allowed the generation of continuous body motion as a function of a time-delayed version of the corrective ankle torque generated by the subject as they swayed.

The experiments quantified changes in body sway behaviors as a function of added time delay and characterized the time course of improvements in balance control as subjects learned to stand with a long delay value imposed by the robotic device. The learning was acquired over multiple training sessions and was demonstrated both by a reduction over time in sway measures and by changes in psychophysical measures that demonstrated a reduction in a subject's indication of the occurrence of unexpected body motions. Additionally, the learned ability to control balance with an added time delay was very well retained at 3 months post training.

A final experiment used electrical vestibular stimulation (EVS) to demonstrate the changing contribution of vestibular information to balance control following a transient increase in time delay. This experiment demonstrated a marked reduction in activity in the soleus muscle that was correlated with the EVS following the onset of an added feedback time delay indicating that the added delay caused a reduction in the vestibular contribution to balance.

In general, the experiments were appropriately designed and analyzed. Although the number of participants in each experiment were not large, they were sufficient given the rather robust effects observed when time delays were added to be feedback.

The robotic balance device not only permitted manipulation of the time delay, but also guarded against subjects actually falling when they swayed beyond the normal range of sways compatible with stable balance. This artificial stabilization of balance beyond the normal range permitted subjects to recover from what would otherwise have been a fall and to immediately continue their attempts to learn a balance strategy that was able to overcome the detrimental effects of increased feedback delay. Thus the training procedure was likely much more effective than if trials had been stopped when sway moved beyond the normal range. One imagines such a training device could have important uses in rehabilitation of balance deficits.

But this artificial stabilization also interfered with one of the balance measures used to quantify the influence of added time delay. Specifically, the RMS sway measure used by the authors did not distinguish between time periods when the subject was being artificially stabilized and the time periods when sway was within the normal sway range. Thus the results that were based on the RMS sway measure were not convincing. But fortunately a sway velocity variance measure was also used to quantify sway behavior as a function of time delay and this measure only used data that was within the normal range of sway.

Overall results are an important addition to knowledge related to how humans control standing balance and demonstrate an ability to learn, with training, to balance with unexpectedly long delays between control action and the resulting body motion.

Overall results are clearly presented but this reviewer has some suggestions for improvement.

1. Experiment 1 quantifies changes in balance control as a function of added time delay by measuring RMS sway amplitude and sway velocity variance. It seems incorrect to use the entire 60 seconds of data in the calculation of RMS sway when there are periods of sway beyond the 3 deg backward and 6 deg forward sway balance limits since the backboard motion is artificially stabilized in the region outside the balance limits. It is only with detailed reading of the methods that the reader understands that the backboard motion is artificially stabilized at extremes of sway so this makes a complete understanding of the RMS sway results presented in Figure 2 difficult. But the problem is not fixed by just making the artificial stabilization methods more evident when presenting the Figure 2 results. The problem is that this RMS sway calculation is not representative of the overall subject-controlled sway behavior when there are periods in the trails when the sway was not controlled by the subject (which occurred frequently with longer delays). This reviewer suggests that a much more useful measure would be to calculate and display the percentage of time that subjects were maintaining control within the balance limits. It would be similarly informative to see this type of percentage measure used to track the Experiment 2 learning results in addition to the velocity variance measures shown in Figure 3.

2. In Experiment 3, group data results show changes in muscle activation evoked by electrical vestibular stimulation based on the 489 of 588 trials on which subjects signaled that they detected an unexpected balance motion. But what about the other 99 trials when subjects did not signal unexpected balance motion? Since the authors suggest there is a possible linkage between the time course of vestibular decline and the detection of unexpected motion, it may be that there was a slower (longer time constant) or reduced amplitude of vestibular decline on the 99 trials where unexpected motion was not detected. Such a finding would strengthen the notion of a linkage between vestibular inhibition and motion detection. Alternatively, if the vestibular declines were indistinguishable between trials with and without unexpected motion this would suggest that the linkage was not tight and something else may be involved. In either case this comparison would be useful. Additionally, it seems that 99 trials should be enough data since Figure 6 shows good results from a single subject based on 77 trials.

3. The section on pages 23 and 24 discusses alternative models that might be able to explain how subjects can learn to tolerate long time delays. I believe that all of the references to alternative models are to models that would be classified as continuous control models as opposed to intermittent control schemes that have been proposed as an alternative (e.g. Ian Loram references such as Loram et al., J Physiol 589.2:307-324, 2011, Gawthrop, Loram, Lakie, Biol Cybern 101:131-146, 2009, and the Morasso reference in the authors manuscript). It seems that Loram's work has shown that it is possible to visually control an unstable load with properties similar to those of a human body using an intermittent control scheme. This intermittent control scheme should be referenced. But beyond just mentioning these alternative control structures as possibilities, do the authors know of actual simulations of these models that can demonstrate that an inverted pendulum system can be made stable with the extremely long time delays that the authors investigated?

4. Several places in the manuscript the authors refer to estimates of maximal time delays based on simpler feedback control models. Specifically, the Bingham et al. 2011 and the van der Kooij and Peterka, 2011 references are given. But the values of the maximal time delays are not consistent across the various mentions of these two references. Here is a listing of those mentions:

- Line 78: ~300 ms

- Line 406: 340-430 ms

- Line 667: ~400 ms

- Line 678: ~400 ms

This reviewer could find mention of 340 ms in the van der Kooij and Peterka paper, but it seems that the Bingham paper did not really investigate time delay in detail and that paper also was investigating body motion in the frontal plane that has considerably different lower body dynamics compared to a single segment inverted pendulum.

5. The authors indicated that analysis programs and data will be made publicly available upon acceptance for publication.
