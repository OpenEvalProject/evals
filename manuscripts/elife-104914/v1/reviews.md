# Peer review - Round 1

Editors:
- Leopoldo Petreanu, Champalimaud Center for the Unknown Portugal

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.104914.3.sa0](https://doi.org/10.7554/eLife.104914.3.sa0)

This important study conducted experiments to quantify how neural activity independent changes in fluorescence might affect two-photon recordings when using diverse sensors. The researchers found a widespread presence of neural-activity-independent artifacts in two-photon imaging and provide convincing evidence that these artifacts are most likely caused by hemodynamic occlusion. Their findings underscore the importance of accounting for these artifacts when interpreting functional two-photon recordings.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.104914.3.sa1](https://doi.org/10.7554/eLife.104914.3.sa1)

Summary:

Fluorescence imaging has become an increasingly popular technique for monitoring neuronal activity and neurotransmitter concentrations in the living brain. However, factors such as brain motion and changes in blood flow and oxygenation can introduce significant artifacts, particularly when activity-dependent signals are small. Yogesh et al. quantified these effects using GFP, an activity-independent marker, under two-photon and wide-field imaging conditions in awake behaving mice. They report significant GFP responses across various brain regions, layers, and behavioral contexts, with magnitudes comparable to those of commonly used activity sensors. These data highlight the need for robust control strategies and careful interpretation of fluorescence functional imaging data.

Strengths:

The effect of hemodynamic occlusion in two-photon imaging has been previously demonstrated in sparsely labeled neurons in V1 of anesthetized animals (see Shen and Kara et al., Nature Methods, 2012). The present study builds on these findings by imaging a substantially larger population of neurons in awake, behaving mice across multiple cortical regions, layers, and stimulus conditions. The experiments are extensive, the statistical analyses are rigorous, and the results convincingly demonstrate significant GFP responses that must be accounted for in functional imaging experiments.

In the revised version, the authors have provided further methodological details that were lacking in the previous version, expanded discussions regarding alternative explanations of these GFP responses as well as potential mitigation strategies. They also added a quantification of brain motion (Fig. S5) and the fraction of responsive neurons when conducting the same experiment using GCaMP6f (Fig. 3D-3F), among other additional information.

Weaknesses:

(1) The authors have now included a detailed methodology for blood vessel area quantification, where they detect blood vessels as dark holes in GFP images and measure vessel area by counting pixels below a given intensity threshold (line 437-443). However, this approach has a critical caveat: any unspecific decrease in image fluorescence will increase the number of pixels below the threshold, leading to an apparent increase in blood vessel area, even when the actual vessel size remains unchanged. As a result, this method inherently introduces a positive correlation between fluorescence decrease and vessel dilation, regardless of whether such a relationship truly exists.

To address this issue, I recommend labelling blood vessels with an independent marker, such as a red fluorescence dye injected into the bloodstream. This approach would allow vessel dilation to be assessed independently of GFP fluorescence -- dilation would cause opposite fluorescence changes in the green and red channels (i.e., a decrease in green due to hemodynamic occlusion and an increase in red due to the expanding vessel area). In my opinion, only when such ani-correlation is observed can one reliably infer a relationship between GFP signal changes and blood vessel dynamics.

Because this relationship is central to the author's conclusion regarding the nature of the observed GFP signals, including this experiment would greatly strengthen the paper's conclusion.

(2) Regarding mitigation strategy, the authors advocate repeating key functional imaging experiments using GFP, and state that their aim here is to provide a control for their 2012 study (Keller et al., Neuron). Given this goal, I find it important to discuss how these new findings impact the interpretation of their 2012 results, particularly given the large GFP responses observed.

For example, Keller et al. (2012) concluded that visuomotor mismatch strongly drives V1 activity (Fig. 3A in that study). However, in the present study, mismatch fails to produce any hemodynamic/GFP response (Fig. 3A, 3B, rightmost bar), and the corresponding calcium response is also the weakest among the three tested conditions (Fig. 3D). How do these findings affect their 2012 conclusions?

Similarly, the present study shows that GFP reveals twice as many responsive neurons as GCaMP during locomotion (Fig. 3A vs. Fig. 3D, "running"). Does this mean that their 2012 conclusions regarding locomotion-induced calcium activity need reconsideration? Given that more neurons responded with GFP than with GCaMP, the authors should clarify whether they still consider GCaMP a reliable tool for measuring brain activity during locomotion.

(3) More generally, the author should discuss how functional imaging data should be interpreted going forward, given the large GFP responses reported here. Even when key experiments are repeated using GFP, it is not entirely clear how one could reliably estimate underlying neuronal activity from the observed GFP and GCaMP responses.

For example, consider the results in Fig. 3A vs. 3D: how should one assess the relative strength of neuronal activity elicited by running, grating, or visuomotor mismatch? Does mismatch produce the strongest neuronal activity, since it is least affected by the hemodynamic/GFP confounds (Fig. 3A)? Or does mismatch actually produce the weakest neuronal activity, given that both its hemodynamic and calcium responses are the smallest?

In my opinion, such uncertainty makes it difficult to robustly interpret functional imaging results. Simply repeating experiments with GFP does not fully resolve this issue, as it does not provide a clear framework for quantifying the underlying neuronal activity. Does this suggest a need for a better mitigation strategy? What could these strategies be?

In my opinion, addressing these questions is critical not only for the authors' own work but also for the broader field to ensure a robust and reliable interpretation of functional imaging data.

(4) The authors now discuss various alternative sources of the observed GFP signals. However, I feel that they often appear to dismiss these possibilities too quickly, rather than appreciating their true potential impacts (see below).

For example, the authors argue that brain movement cannot explain their data, as movement should only result in a decrease in observed fluorescence. However, while this might hold for x-y motion, movement in the axial (z) direction can easily lead to both fluorescence increase and decrease. Neurons are not always precisely located at the focal plane -- some are slightly above or below. Axial movement in a given direction will bring some cells into focus while moving others out of focus, leading to fluorescence changes in both directions, exactly as observed in the data (see Fig. S2).

Furthermore, the authors state that they discard data with 'visible' z-motion. However, subtle axial movements that escape visual detection could still cause fluorescence fluctuations on the order of a few percent, comparable to the reported signal amplitudes.

Finally, the authors state that "brain movement kinematics are different in shape than the GFP responses we observe". However, this appears to contradict what they show in Fig. 2A. Specifically, the first example neuron exhibits fast GFP transients locked to running onset, with rapid kinematics closely matching the movement speed signals in Fig. S5A. These fast transients are incompatible with slower blood vessel area signals (Fig. 4), suggesting that alternative sources could contribute significantly.

In sum, the possibility that alternative signal sources could significantly contribute should be taken seriously and more thoroughly discussed.

(5) The authors added a quantification of brain movement (Fig. S5) and claim that they "only find detectable brain motion during locomotion onsets and not the other stimuli." However, Fig. S5 presents brain 'velocity' rather than 'displacement'. A constant (non-zero) velocity in Fig. S5 B-D indicates that the brain continues to move over time, potentially leading to significant displacement from its initial position across all conditions. While displacement in the x-y plane are corrected, similar displacement in the z direction likely occurs concurrently and cannot be easily accounted for. To assess this possibility, the authors should present absolute displacement relative to pre-stimulus frames, as displacement -- not velocity -- determines the size of movement-related fluorescence changes.

(6) In line 132-133, the authors draw an analogy between the effect of hemodynamic occlusion and liquid crystal display (LCD) function. However, there are fundamental differences between the two. LCDs modulate light transmission by rotating the polarization of light, which then passes through a crossed polarizer. In contrast, hemodynamic occlusion alters light transmission by changing the number and absorbance properties of hemoglobin. Additionally, LCDs do not involve 'emission' light - back-illumination travels through the liquid crystal layer only once, whereas hemodynamic occlusion affects both incoming excitation light and the emitted fluorescence. Given these fundamental differences, the LCD analogy may not be entirely appropriate.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.104914.3.sa2](https://doi.org/10.7554/eLife.104914.3.sa2)

- Approach

In this study, Yogesh et al. aimed at characterizing hemodynamic occlusion in two photon imaging, where its effects on signal fluctuations are underappreciated compared to that in wide field imaging and fiber photometry. The authors used activity-independent GFP fluorescence, GCaMP and GRAB sensors for various neuromodulators in two-photon and widefield imaging during a visuomotor context to evaluate the extent of hemodynamic occlusion in V1 and ACC. They found that the GFP responses were comparable in amplitude to smaller GCaMP responses, though exhibiting context-, cortical region-, and depth-specific effects. After quantifying blood vessel diameter change and surrounding GFP responses, they argued that GFP responses were highly correlated with changes in local blood vessel size. Furthermore, when imaging with GRAB sensors for different neuromodulators, they found that sensors with lower dynamic ranges such as GRAB-DA1m, GRAB-5HT1.0, and GRAB-NE1m exhibited responses most likely masked by the hemodynamic occlusion, while a sensor with larger SNR, GRAB-ACh3.0, showed much more distinguishable responses from blood vessel change. They thoroughly investigate other factors that could contribute to these signals and demonstrate hemodynamic occlusion is the primary cause.

- Impact of revision

This is an important update to the initial submission, adding much supplemental imaging and population data that provide greater detail to the analyses and increase the confidence in the authors conclusions.

Specifically, inclusion of the supplemental figures 1 and 2 showing GFP expression across multiple regions and the fluorescence changes of thousands of individual neurons provides a clearer picture of how these effects are distributed across the population. Characterization of brain motion across stimulation conditions in supplemental figure 5 provides strong evidence that the fluorescence changes observed in many of the conditions are unlikely to be primarily due to brain motion associated imaging artifacts. The role of vascular area on fluorescence is further supported by addition of new analyses on vasoconstriction leading to increased fluorescence in Figures 4C1-4, complementing the prior analyses of vasodilation.

The expansion of the discussion on other factors that could lead to these changes is thorough and welcome. The arguments against pH playing a factor in fluorescence changes of GFP, due to insensitivity to changes in the expected pH range are reasonable, as are the other discussed potential factors.

With respect to the author's responses to prior critique, we agree that activity dependent hemodynamic occlusion is best investigated under awake conditions. Measurement of these dynamics under anesthesia could lead to an underestimation of their effects. Isoflurane anesthesia causes significant vasodilation and a large reduction in fluorescence intensity in non-functional mutant GRABs. This could saturate or occlude activity dependent effects.

- Strengths

This work is of broad interest to two photon imaging users and GRAB developers and users. It thoroughly quantifies the hemodynamic driven GFP response and compares it to previously published GCaMP data in a similar context, and illustrates the contribution of hemodynamic occlusion to GFP and GRAB responses by characterizing the local blood vessel diameter and fluorescence change. These findings provide important considerations for the imaging community and a sobering look at the utility of these sensors for cortical imaging.

Importantly, they draw clear distinctions between the temporal dynamics and amplitude of hemodynamic artifacts across cortical regions and layers. Moreover, they show context dependent (Dark versus during visual stimuli) effects on locomotion and optogenetic light-triggered hemodynamic signals.

The authors suggest that signal to noise ratio of an indicator likely affects the ability to separate hemodynamic response from the underlying fluorescence signal. With a new analysis (Supplemental Figure 4) They show that the relative degree of background fluorescence does not affect the size of the artifact.

Most of the first generation neuromodulator GRAB sensors showed relatively small responses, comparable to blood vessel changes in two photon imaging, which emphasizes a need for improved the dynamic range and response magnitude for future sensors and encourages the sensor users to consider removing hemodynamic artifacts when analyzing GRAB imaging data.

- Weaknesses

The largest weakness of the paper remains that, while they convincingly quantify hemodynamic artifacts across a range of conditions, they provide limited means of correcting for them. However they now discuss the relative utility of some hemodynamic correction methods (e.g. from Ocana-Santero et al., 2024).

The paper attributes the source of 'hemodynamic occlusion' primarily to blood vessel dilation, but leaves unanswered how much may be due to shifts in blood oxygenation. Figure 4 directly addresses the question of how much of the signal can be attributed to occlusion by measuring the blood vessel dilation, and has been improved by now showing positive fluorescence effects with vasoconstriction. They now also discuss the potential impact of oxygenation.

Along these lines, the authors carefully quantified the correlation between local blood vessel diameter and GFP response (or neuropil fluorescence vs blood vessel fluorescence with GRAB sensors). We are left to wonder to what extent does this effect depend on proximity to the vessels? Do GFP/ GRAB responses decorrelate from blood vessel activity in neurons further from vessels (refer to Figure 5A and B in Neyhart et al., Cell Reports 2024)? The authors argue that the primary impact of occlusion is from blood vessels above the plane of imaging, but without a vascular reconstruction, their evidence for this is anecdotal.

The choice of ACC as the frontal region provides a substantial contrast in location, brain movement, and vascular architecture as compared to V1. As the authors note, ACC is close to the superior sagittal sinus and thus is the region where the largest vascular effects are likely to occur. A less medial portion of M2 may have been a more appropriate comparison. The authors now include example imaging fields for ACC and interesting out-of-plane vascular examples in the supplementary figures that help assess these impacts.

-Overall Assessment

This paper is an important contribution to our understanding of how hemodynamic artifacts may corrupt GRAB and calcium imaging, even in two-photon imaging modes. While it would be wonderful if the authors were able to demonstrate a reliable way to correct for hemodynamic occlusion which did not rely on doing the experiments over with a non-functional sensor or fluorescent protein, the careful measurement and reporting of the effects here is, by itself, a substantial contribution to the field of neural activity imaging. It's results are of importance to anyone conducting two-photon or widefield imaging with calcium and GRAB sensors and deserves the attention of the broader neuroscience and in-vivo imaging community.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.104914.3.sa3](https://doi.org/10.7554/eLife.104914.3.sa3)

Summary:

In this study, the authors aimed to investigate if hemodynamic occlusion contributes to fluorescent signals measured with two-photon microscopy. For this, they image the activity-independent fluorophore GFP in 2 different cortical areas, at different cortical depths and in different behavioral conditions. They compare the evoked fluorescent signals with those obtained with calcium sensors and neuromodulator sensors and evaluate their relationship to vessel diameter as a readout of blood flow.

They find that GFP fluorescence transients are comparable to GCaMP6f stimuli-evoked signals in amplitude, although they are generally smaller. Yet, they are significant even at the single neuronal level. They show that GFP fluorescence transients resemble those measured with the dopamine sensor GRAB-DA1m and the serotonin sensor GRAB-5HT1.0 in amplitude an nature, suggesting that signals with these sensors are dominated by hemodynamic occlusion.Moreover, the authors perform similar experiments with wide-field microscopy which reveals the similarity between the two methods in generating the hemodynamic signals. Together the evidence presented calls for the development and use of high dynamic range sensors to avoid measuring signals that have another origin from the one intended to measure. In the meantime, the evidence highlights the need to control for those artifacts such as with the parallel use of activity independent fluorophores.

Strengths:

- Comprehensive study comparing different cortical regions in diverse behavioral settings in controlled conditions.

- Comparison to the state-of-the-art, i.e. what has been demonstrated with wide-field microscopy.

- Comparison to diverse activity-dependent sensors, including the widely used GCaMP.

Comments on revisions:

The authors have addressed my concerns well. I have no further comments.
