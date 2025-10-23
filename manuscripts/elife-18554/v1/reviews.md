# Peer review - Round 1

Editors:
- Sabine Kastner, Princeton University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.18554.033](https://doi.org/10.7554/eLife.18554.033)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "High performance communication by people with ALS using an intracortical brain-computer interface" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Sabine Kastner as the Reviewing Editor and enior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Hagai Lalazar (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary: This study examines spelling performance for two patients with ALS using an intracortical brain computer interface. This is the most comprehensive and elegant study that has been performed on this topic up to this point, and the editors agreed that it merits further consideration for publication at eLife.

Essential revisions:

1) Please discuss why the classification approach (vs. regression underlying cursor control) has not yet been explored.

2) Please provide some evidence that during the sessions when subject T6 was instructed not to use her hand, there was no overt movement. If you don't have EMG or motion capture, even an analysis of the video might satisfy this concern.

3) Please provide additional data (ideally EMG/high resolution eye tracking) to rule out muscle artifacts, or, alternatively, careful documentation of raw LFP traces that were used for control, demonstrating that they appear "naturalistic" rather than "artefactual".

4) Please explain why the HMM was not used with subject T7.

5) Please provide a detailed training history of the subjects (including previous experiments) and obtain as complete as possible training history for the studies they are comparing with. Please explain why the comparison is justified.

Reviewer #1:

Overview: The current study assesses spelling performance for two patients with ALS using an intracortical Brain computer interface (BCI) and a specific algorithm (refit-KF for cursor movement and an HMM for click selection). The main claim of the study is that the exhibited performance is better than previous spelling BCI studies with disabled patients.

General assessment: My main concern is whether the study's approach and result are innovative enough for publication in eLife. The authors previously published a study with the same participants (Gilja et al., 2015) using the same algorithm for cursor movement control. In the current study this is additionally combined with click selection (via an HMM) for spelling, which in the attached IEEE paper is shown to provide a modest but significant improvement on target selection. However, in one of the 2 subjects in the current study, click selection wasn't used. Thus, it is unclear how important is this addition for the exhibited performance. Relatedly, a recent noninvasive BCI spelling study on healthy subjects (Townsend & Platsko, 2016) appear to exhibit similar performance to the current study (1.73 bps in their "free spelling" task, see their table 5). That study should be referred to and the comparison discussed. While the current study appears to exhibit the best spelling accuracy to date as measured on ALS patients using a BCI, another study (McCane et al., 2015) showed that ALS patents and age matched controls exhibit similar performance while using the noninvasive BCI speller used in the Townsend & Platsko study. Thus, that study results arguably apply to ALS patients as well.

Other issues:

1) Intracranial LFP signals can be affected by activity of head muscles, including eye muscles. I'm concerned that such artifacts took place in the higher performing subject (T6), especially given that for that subject LFP frequencies for up to 450 Hz were used, as such high frequencies are more prone to artifacts than low frequencies. If possible, the authors should perform an additional experimental session where EMG signals from head muscles are recorded, or at least eye movements (including micro-saccades) are tracked, and show that the relevant control signals are uncorrelated with the EMG/eye movements.

2) Given that subject T6 has used an eye gaze speller before, it should be feasible to compare the spelling performance of that system vs. the one in the current study. This should be done to substantiate the main conclusion of the study that "intracortical BCIs offer a promising approach to assistive communication systems for people with paralysis."

3) Related to the above, and given that the paper is relatively short, there should be added to the Discussion a section detailing a cost-benefit analysis of invasive methods vs. noninvasive ones. If the authors believe (as I assume they do) that the exhibited performance of their BCI outweighs the risks of invasive surgery and chronic implants then that claim should be made explicit and substantiated.

4) The number of subjects (2) is standard for this type of studies. However, there are significant differences in the procedures involving each of the subjects, particularly regarding: 1 – the calibration procedure of the algorithm, which in one subject (T6) involved performing motor movements with the fingers. 2 – one participant (T6) performed clicks which were decoded using an HMM, the other (T7) did not. Thus, it is unclear if the subjects could actually be pooled together.

5) Related to the above, the best subject in the study seemed to exhibit a capacity for natural motor control not attained by the other subject in the study, and possibly by some subjects in previous studies that are being compared. Thus, this capacity may underlie the exhibited high performance. In order to address this concern the authors performed an additional two sessions with this subject were the movements were required to be suppressed. However, it is unclear if movements were actually suppressed in those sessions, as no data to that effect (such as EMG) is shown. Thus, it is unclear if this control is adequate. The authors should substantiate the claim of this control by showing such data.

6) I couldn't find references for several of the studies that are being compared in the table (Figure 3 – —figure supplement 3).

7) The best performing subject (T6) barely has any spiking signal in the array (Figure 3 – —figure supplement 5.) Thus, it is unclear what type of activity is being extracted and used. The authors should provide traces of the threshold crossings from a small number of channels (e.g. 10) which were most used for control, for example as assessed by off-line, channel dropping analysis. Additionally they should provide traces of the LFP features used for control, assessed in the same way. There should also be an analysis detailing which features were more influential for control (spiking or LFP) for both cursor movement and click selection.

8) There should be a summarized but detailed history of BCI experience for both subjects as this is directly relevant to their capacity to control the BCI. Differences in training can make it hard to compare between studies. Subjects in intracortical BCI studies typically train for much longer periods than in EEG BCI studies. For example, in (Mainsah et al., 2015) which is a study that should be added to the comparison table, subjects trained for 3 days. While subjects in the current study may have well been training for months in different BCI experiments. The authors should (when possible) add that information to the study comparison table and explain, in cases where previous studies had much shorter training periods than the current study, why the comparison is still justified.

References:

Townsend, G. & Platsko, V. Pushing the P300-based brain-computer interface beyond 100 bpm: extending performance guided constraints into the temporal domain. J Neural Eng., 13(2):026024. (2016).

McCane, L.M., Heckman, S.M., McFarland, D.J., Townsend. G., Mak, J.N., Sellers, E.W., Zeitlin, D., et al. P300-based brain-computer interface (BCI) event-related potentials (ERPs): People with amyotrophic lateral sclerosis (ALS) vs. age-matched controls. Clinical neurophysiology 126 (11): 2124-31. (2015).

Mainsah, B.O., Collins, L.M., Colwell, K.A., Sellers, E.W., Ryan, D.B., Caves, K. & Throckmorton, C.S. Increasing BCI communication rates with dynamic stopping towards more practical use: an ALS study. J Neural Eng., 12(1): 016013. (2015).

Reviewer #3:

A closed-loop BMI for typing was tested with 2 ALS patients. Performance showed substantial improvement compared to previous studies, on both realistic and quantitative tests. This study is thorough, its details are, for the most part, explained well, and has important clinical implications. I have made suggestions to improve the clarity and presentation of the manuscript.

1) Improving typing speeds can be evaluated both on an absolute scale (relative to the typing speeds of able-bodied typers), as well as, the improvement relative to previous studies. This study makes a substantial improvement in both regards, however both points can be made more clearly and earlier in the paper.

The comparison to able-bodied typers (main text, twelfth paragraph) should be stated in the Abstract (perhaps just comparing to texting, which is the most comparable to cursor control) and mentioned earlier in the manuscript (e.g. after the fourth paragraph of the main text). This is critical for a non-expert reader to be able to assess this work in the general context of the state-of-the-art of assistive communication devices.

Additionally, the table in Figure 3—figure supplement 3, should be made a full figure. This comparison gives a broad picture of the improved performance achieved in the current study (i.e. the variance across many other studies and the 1-2 orders of magnitude improvement over EEG based approaches). This table should have an additional column, describing in a few words the algorithm and type of user-interface used in each study (e.g. "p300-speller", "ReFIT-KF & HMM", etc.). Also, all the papers cited in the table should appear in the references.

2) Typing is inherently a (multi-class) classification problem, and not the regression problem underlying 2D cursor control. BCI typing speeds will eventually be limited only by the mean time of each cursor trajectory (between each letter selected), and any time used for the selection itself (dwell times, or "click"). This difference explains why the texting speeds of able-bodied subjects (which usually use only one finger) are lower that their keyboard typing speeds (which have discretized the alphabet into the 10 fingers). This issue has not been explored in the current paper, and to my knowledge, in the series of studies on "typing" with humans or monkeys (except for Andersen, et al. (2004)). If the authors have done any offline data-analysis to test this idea, it would be very helpful to describe it briefly. Otherwise, why this approach has not yet been explored should be explained.

3) Figure 3—figure supplement 1, discusses that performance (in both the copy-typing and grid tasks) was not significantly different when the subject was asked to suppress any overt movements. However, there is no measurement of the movement and its ensuing reduction after the instruction. The main text should be more forthcoming about this, and mention that this is only what the subject was trying to do, however was not measured and quantified. Moreover, as EMG from the arm was not measured, it should be mentioned that an effect of nascent muscle commands (that did not elicit observable movements) on the performance cannot be ruled out. This is especially important, as subject T6 had better results, and her remaining finger movements were used to train her initial decoders. As different patients may or may not have specific residual movements, this makes performance comparisons between them less precise. This point should also be mentioned, in the paragraph hypothesizing about the reasons for the performance differences between the subjects (main text, fifteenth paragraph).

4) The analysis in Figure 3—figure supplement 4 suffers from all the weaknesses of analyzing the tuning of M1 neurons by fitting them to a cosine-tuning function for movement direction, reported in many studies (some even by authors of the current study). For example, (i) the percent of neurons that show a change in preferred direction depends on the goodness-of-fit of the cosine model across the population (which the authors don't report), (ii) preferred directions have been shown to change as a function of time during the movement (Churchland & Shenoy (2007), Figure 13), (iii) there are high frequency deviations from cosine tuning, which, in addition to the cosine tuning component, may be expected from random connectivity (Lalazar, Abbott, Vaadia (2016)), etc. This figure and the associated sentence in the main text (main text, eighth paragraph; and Methods subsection) do not contribute to the manuscript and only diminish from its otherwise compelling level of rigor. I suggest removing them.

5) Why was the HMM decoder not used for subject T7? This should be explained.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "High performance communication by people with paralysis using an intracortical brain-computer interface" for further consideration at eLife. Your revised article has been favorably evaluated by Sabine Kastner (Senior Editor) and one of the previous reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

1) The paragraph discussing the costs and benefits of invasive vs. noninvasive bci strategies should be more balanced. The potential risk of brain surgery (e.g. infection, tissue damage, brain swelling, seizures) needs to be explicitly stated, especially the risk of infection given that there is an implant providing a physical connection from the brain to outside the scalp.

2) – On several instances, the authors stress the benefits of a fully self-calibrating, fully wireless implantable system. They need to make clear that theirs is not such a system.
