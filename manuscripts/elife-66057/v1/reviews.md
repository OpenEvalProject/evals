# Peer review - Round 1

Editors:
- Andreas Horn, Charité - Universitätsmedizin Berlin Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66057.sa1](https://doi.org/10.7554/eLife.66057.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

In this manuscript, Sharma et al., investigated the effect of dopamine administration on oscillatory whole-brain networks by means of simultaneous local field potential recordings from the subthalamic nucleus and whole-brain magnetoencephalography recordings in seventeen patients with Parkinson's disease. A key feature is the combined use of invasive and noninvasive recordings and to investigate network changes by employing a hidden markov model. They identified three physiologically interpretable spectral connectivity patterns and found that cortico-cortical, cortico-STN, and STN-STN networks were differentially modulated by dopaminergic medication. These findings provide new insights regarding the mechanisms by which dopamine and medications alter cortico-basal ganglia dynamics, and open up new directions for studying their functions.

Decision letter after peer review:

Thank you for submitting your article "Differential dopaminergic modulation of spontaneous cortico-subthalamic activity in Parkinson's disease" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Kelly Bijanki (Reviewer #1); Muthuraman Muthuraman (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

1. I believe one strong concern is the first one raised by reviewer #1 in that it is important to differentiate neural activity differences in the ON medication state in whether they may originate from the effects of dopamine on the brain or the fact that the patients are moving more. Is there any possibility to address this issue? E.g. were motion parameters analysed to some degree? Does archival data exist that could be used to differentiate states at rest vs. states with movement (e.g. finger tapping)? If not this limitation should be prominently discussed.

2. While I personally think the concern of rev. 3 with contamination of STN signals by EEG is not of major concern (and the method has been established with reproducible results e.g. based on the Litvak / Hirschmann / Neumann works). Still, electrode localization could help to at least assure all leads were properly placed (or if not results would remain stable if the ones outside STN would be discarded)

3. I agree with rev. #2 that presentation can be improved. While circular connection plots are informative, it could be helpful to see to results in Figures 2-4 mapped to a brain (or sensor space). In general, I think the Results section could be stratified and presentation optimized.

Reviewer #1 (Recommendations for the authors):

Below is a list of concerns upon reviewing the manuscript, with suggestions for improvement.

1. The style of writing in the introduction is a little light on examination of the prior literature and motivation for the study. Starting at line 79, it transitions into a preview of the methods section listing of the analyses the researchers undertook and less like a true introduction setting the scene for the experiments.

2. This reviewer was surprised by the use of the word "communication", communication state, comms, etc. Perhaps this is a term of art in MEG (not this reviewer's area of expertise) but defining an MEG feature as indicative of communication seems presumptuous and merits at least brief discussion in the manuscript. Please add more background on MEG analysis and interpretation, especially in PD, in the introduction section.

3. This reviewer was unclear on why increased "communication" in the medial OFC in δ and theta was interpreted as a pathological state indicating deteriorated frontal executive function. Given that the authors provide no evidence of poor executive function in the patients studied, the authors must at least provide evidence from other studies linking this feature with impaired executive function.

4. Authors further reported that increased DA (L-DOPA administration) caused β activity to switch from STN-mediated motor network to a frontoparietal mediated one. The authors provide somewhat impoverished anatomical detail about the differences between the observed STN-mediated motor network and the known pathological β activity in STN in PD.

5. Last, authors report that DA didn't modify locally-originating STN oscillations in PD, but the detail on how they define locally-originating is unclear.

6. On line 86 the authors identify prior research limited by its investigation of specific connectivity pairs, whereas on line 104 the authors report on connectivity pairs in the current study.

7. The authors use the term "oscillations" without properly defining it in terms of neural activity and they have not addressed the analytical approach they use to confirm the activity measured on LFP or MEG reflects oscillatory activity vs. bursting activity or other neural activity types.

8. Authors need to acknowledge the role of DBS in PD therapy earlier in the study and identify that as the means by which they have access to simultaneous LFP recording. They don't even define the acronym "DBS" at its first use.

9. Authors could be more clear in lines 90-97 to define what they mean by "disruptive, "physiologically restorative", and "limited".

10. Authors repeatedly state their method allows them to delineate between pathological and physiological connectivity, but they don't explain how dynamical systems and discrete-state stochasticity support that goal. Lines 106 and 111.

11. Authors must address differences in neural activity other than DA-mediated changes in the on and off medication state. For example, when patients are off med, their UPDRS scores are elevated – do they not have movements that would pick up extra activations in MEG during "rest"? Is it possible to do a true "resting state" in active PD? At minimum, this concern must be discussed in the manuscript.

12. Figure 1: this reviewer would like to see the Y axis indicating amplitude or power, rather than arbitrary units from NNMF output. This figure also begs the question why the NMMF categorized 10-20hz oscillations as δ/theta (bump in blue line in "ON medication" and above 30Hz as α (red line, same plot)). To this reviewer, it appears as though the NMMF factorization worked effectively in the "OFF medication" data set but failed in the "ON medication" data set.

13. Patient sample appears to under-represent female patients. Is there a relationship between sex and DA metabolism/uptake/MEG markers? Perhaps simply acknowledge the imbalance in the manuscript.

14. LFP recordings were sampled from externalized DBS leads using the St. Jude directional 6172 lead except in one patient who had the Boston Scientific leads (which I think is fine to include in analysis together provided surface areas of contacts are identical). The geometry of the segmented leads needs to be addressed relative to sensitivity for various frequencies of oscillatory activity. Segmented leads have very low surface area and may require ultra-high sampling rates (30 kHz and higher) to resolve oscillatory activity.

Reviewer #2 (Recommendations for the authors):

General remarks:

1. A visualization of the state time series would be a nice addition to see the dynamics of the network. Including the probabilities would further give an impression of "how clear the states are", i.e. were they exclusive or were there some intervals where 2 states were rather active at the same time.

2. The color coding in table 1 (4x orange) does not correspond to the ring figures (2x orange/hemisphere). Both areas 17 and 18 are termed "medial orbitofrontal".

Results

As stated in the public review, there are several points concerning the presentation of the results:

3. Line 180 Supporting the dopamine overdose hypothesis in PD, we identified a δ/theta oscillatory network involving lateral and medial orbitofrontal cortical regions.

– Figure 2 also shows the inter-hemispheric connectivity of the pars orbitalis. What is the reason to not mention this in the main text?

4. Line 259: Furthermore, ON medication in the α band only the connectivity between temporal and parietal cortical regions and the STN was preserved (Figure 3C α; p < 0.05), consistent with previous findings (Litvak et al. 2011). In contrast, in the β band only STN-medial orbitofrontal connectivity remained intact (p < 0.05, Figure 3C β).

– Similar to the comment on line 180, the figure also shows α connectivity between the STN and medial orbitofrontal cortex.

5. Line 269: Finally, ON medication, a sensorimotor-frontoparietal network emerged (p < 0.05, Figure 3C β) where sensorimotor, frontal, and parietal regions were no longer connected to the STN, but instead directly communicated with each other in the β band.

– Similar to the comment on line 180: is there a reason to exclude the connection from the somatomotor cortex to the caudal middle frontal (e.g. figure 3c, β: 13r-16r)?

6. 256: Importantly, coherence OFF medication was significantly larger than ON medication between STN and sensorimotor, STN and temporal and STN and frontal cortices (p < 0.05 for all connections, Figure 3B α and β).

– The figure does not these results for STN and sensorimotor cortex

7. 263: Most previous PD studies report a decrease in the motor-STN coherence ON medication in the β band (Hammond, Bergman, and Brown 2007; Litvak et al. 2011; Hirschmann et al. 2013; Little et al. 2013; Marinelli et al. 2017) but do not indicate any changes that the sensorimotor regions might experience at the whole-brain level. In the communication state, OFF medication, STN-pre-motor (sensory), STN-frontal, and STN-parietal connectivity was present (p < 0.05, Figure 3A α and β). STN-cortical coherence was then significantly reduced ON compared to OFF medication (p < 0.05, Figure 3B α and β).

– The first sentence introduces cortico-cortical connections, which is then, however, followed by STN-cortical results. This is then followed by results on the sensorimotor-frontoparietal network, which indeed is cortico-cortical. However, later in the manuscript, the following statement suggests that the cortico-cortical network differs from the sensorimotor-frontoparietal network: "Still, significant connectivity was selectively preserved in a spectrally-specific manner ON medication both at the corticocortical level and the cortical-STN level. Furthermore, a sensorimotor-frontoparietal network emerged ON medication" (line282). It is not clear what exactly resembles the cortico-cortical network, and where the results are presented.

On the results of temporal properties:

8. Line 324: Previous research has shown that ON medication, spectrally-specific cortico-STN connectivity remains preserved in PD compared to OFF medication (Litvak et al. 2011; Hirschmann et al. 2013). This indicates the existence of functionally relevant cortico-STN loops. A decrease in coherence between the cortex and the STN has also been observed ON medication (George et al. 2013), which was correlated with improved motor functions in PD. All the connectivity effects were observed in our results for the communication state. Furthermore, in the communication state, we showed the existence of a frontoparietal sensorimotor 331 network in the β band ON medication. Recent evidence indicates that with the loss of dopamine and the start of PD symptoms, δ/theta oscillations emerge within the basal ganglia (Whalen et al. 2020). In line with these findings, STN-STN δ/theta oscillations in the local state were reduced ON medication.

– I have the impression that this paragraph is not in the right position. It repeats and even discusses the previously mentioned results and jumps from "frontoparietal sensorimotor networks" to "STN-STN δ/theta" findings.

Further, it is not clear if "All the connectivity effects were observed in our results for the communication state" relates to the citations above, especially since other states are shown to have effects on connectivity as well.

9. Additionally, the main text should provide t-scores and degrees of freedom, not only p-values. The comprehension of the results could be improved by displaying significantly different comparisons in a clear way in Figure 5 (e.g. provide * for p<0.05). However, what was the rationale for testing the medication condition and states with different t-tests? Would a 2way- repeated measures ANOVA not be more appropriate?

10. Line 353: The lifetimes for both the local and communication state were significantly increased by medication (ON > OFF: local, p < 0.01; comms, p {less than or equal to} 0.01).

and line 360: Both the local and communication state tended to last longer ON medication.

– This seems to be a repetition. Also, it is not clear what "tended to last longer" means? Is there a significant difference or a trend?

Methods

11. Line 676: Since NNMF does not guarantee a unique solution, we performed multiple instances of the factorization.

– The authors should state the exact number of repetitions. How was this number decided?Reviewer #3 (Recommendations for the authors):

1. The Authors could examine the effect of the dopaminergic medication (ON and OFF) on the recurrent oscillatory patterns of transient network connectivity within and between the cortex and the STN, as a function of the duration of the disease and/or the DRT history.

2. Re the contamination of the STN signal by volume conducted signals from the cortex. Page 20 (lines 584-586) "To correct for volume conduction in the signal, symmetric orthogonalisation (Colclough et al., 2015) was applied to each subject's resulting cortical time series matrix".

Have the authors applied this correction to the STN LFPs? If the authors cannot rule out the possibility of a contamination of STN LFPs by volume conducted signals from the cortex and cannot guarantee that the signal recorded in the STN only reflected local STN activity they should at least interpret their results with caution and discuss this limitation in their discussion.

3. The authors could make the paper more reader-friendly. In particular, could classical spectral and coherence analyses be performed to visualize the characteristics of the oscillatory activity and neural synchronization of the EMG and LFP signals in the recurrent oscillatory patterns of transient network connectivity both ON and OFF medication?

4. In this study, the authors could reconstruct the trajectories of the DBS leads within the STN (using for example the open source LeadDBS program?).
