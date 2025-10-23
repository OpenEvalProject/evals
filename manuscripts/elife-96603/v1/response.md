# Author response - Round 1

Authors:
- Yiting Li ([ORCID: 0009-0003-5104-5516](https://orcid.org/0009-0003-5104-5516))
- Wenqu Yin
- Xin Wang
- Jiawen Li
- Shanglin Zhou
- Chaolin Ma
- Peng Yuan ([ORCID: 0000-0003-4051-4447](https://orcid.org/0000-0003-4051-4447))
- Baoming Li ([ORCID: 0009-0006-1554-9700](https://orcid.org/0009-0006-1554-9700))

## Response text

DOI: [10.7554/eLife.96603.3.sa3](https://doi.org/10.7554/eLife.96603.3.sa3)

The following is the authors’ response to the original reviews.

eLife Assessment

This useful study reports how neuronal activity in the prefrontal cortex maps time intervals during which animals have to wait until reaching a reward and how this mapping is preserved across days. However, the evidence supporting the claims is incomplete as these sequential neuronal patterns do not necessarily represent time but instead may be correlated with stereotypical behavior and restraint from impulsive decision, which would require further controls (e.g. behavioral analysis) to clarify the main message. The study will be of interest to neuroscientists interested in decision making and motor control.

We thank the editors and reviewers for the constructive comments. In light of the questions mentioned by the reviewers, we have performed additional analyses in our revision, particularly aiming to address issues related to single-cell scalability, and effects of motivation and movement. We believe these additional data will greatly improve the rigor and clarity of our study. We are grateful for the review process of eLife.

Public Reviews:

Reviewer #1 (Public Review):

Summary:

This paper investigates the neural population activity patterns of the medial frontal cortex in rats performing a nose poking timing task using in vivo calcium imaging. The results showed neurons that were active at the beginning and end of the nose poking and neurons that formed sequential patterns of activation that covaried with the timed interval during nose poking on a trial-by-trial basis. The former were not stable across sessions, while the latter tended to remain stable over weeks. The analysis on incorrect trials suggests the shorter non-rewarded intervals were due to errors in the scaling of the sequential pattern of activity.

Strengths:

This study measured stable signals using in vivo calcium imaging during experimental sessions that were separated by many days in animals performing a nose poking timing task. The correlation analysis on the activation profile to separate the cells in the three groups was effective and the functional dissociation between beginning and end, and duration cells was revealing. The analysis on the stability of decoding of both the nose poking state and poking time was very informative. Hence, this study dissected a neural population that formed sequential patterns of activation that encoded timed intervals.

We thank the reviewer for the positive comments.

Weaknesses:

It is not clear whether animals had enough simultaneously recorded cells to perform the analyzes of Figures 2-4. In fact, rat 3 had 18 responsive neurons which probably is not enough to get robust neural sequences for the trial-by-trial analysis and the correct and incorrect trial analysis.

We thank the reviewer for the comment. Our imaging data generally yielded 50-150 cells in each session. The 18 neurons mentioned by the reviewer are from the duration cell category. We have now provided the number of imaged cells from each rat in the new Supplementary figure 1D. In addition, we have plotted the duration cells’ sequential activity of individual trials for each rat in new Supplementary figure 1B and 1C. These data demonstrate robust sequential activities from the duration cells.

In addition, the analysis of behavioral errors could be improved. The analysis in Figure 4A could be replaced by a detailed analysis on the speed, and the geometry of neural population trajectories for correct and incorrect trials.

We thank the reviewer for the suggestions. We have now performed analyses of the neural population trajectories as the reviewer suggested. We have calculated the neural population trajectories using the first two principal components of the neural activities during nose poke events. While both correct and incorrect trials show similar shapes of the trajectories, correct trials show more expanded paths, with longer lengths on average. These new results are now updated in Figure 4. Since type I or type II errors would likely generate trajectories not following the general direction which is different from our observations, these results are consistent with our conclusion that scaling errors contribute to the incorrect behavior timing in these rats.

In the case of Figure 4G is not clear why the density of errors formed two clusters instead of having a linear relation with the produce duration. I would be recommendable to compute the scaling factor on neuronal population trajectories and single cell activity or the computation of the center of mass to test the type III errors.

To clarify the original Figure 4G, the correct trials tended to show positive time estimation errors while the incorrect trials showed negative time estimation errors. We believe that the polarity switch between these two types suggests a possible use of this neural mechanism to time the action of the rats.

In addition, we have performed the analysis suggested by the reviewer in our revision. We calculated two types of scaling factors. On individual cell level, we computed the peak position of individual trials to the expected positions from averaged template. And on neural population level, we searched for a scaling multiplier to resample the calcium activity data and minimized the differences between scaled activity and the expected template. Using these two factors, we found that correct trials show significantly larger scaling compared to incorrect trials, consistent with our original interpretation that behavior errors are primarily correlated with scaling errors in the neural activities (type III error). These new results are now incorporated in Figure 4 and we have also updated the main text for the descriptions.

Due to the slow time resolution of calcium imaging, it is difficult to perform robust analysis on ramping activity. Therefore, I recommend downplaying the conclusion that: "Together, our data suggest that sequential activity might be a more relevant coding regime than the ramping activity in representing time under physiological conditions."

We agree with the reviewer, and have now modified this sentence in the abstract.

Reviewer #2 (Public Review):

In this manuscript, Li and collaborators set out to investigate the neuronal mechanisms underlying "subjective time estimation" in rats. For this purpose, they conducted calcium imaging in the prefrontal cortex of water-restricted rats that were required to perform an action (nosepoking) for a short duration to obtain drops of water. The authors provided evidence that animals progressively improved in performing their task. They subsequently analyzed the calcium imaging activity of neurons and identify start, duration, and stop cells associated with the nose poke. Specifically, they focused on duration cells and demonstrated that these cells served as a good proxy for timing on a trial-by-trial basis, scaling their pattern of actvity in accordance with changes in behavioral performance. In summary, as stated in the title, the authors claim to provide mechanistic insights into subjective time estimation in rats, a function they deem important for various cognitive conditions.

This study aligns with a wide range of studies in system neuroscience that presume that rodents solve timing tasks through an explicit internal estimation of duration, underpinned by neuronal representations of time. Within this framework, the authors performed complex and challenging experiments, along with advanced data analysis, which undoubtedly merits acknowledgement. However, the question of time perception is a challenging one, and caution should be exercised when applying abstract ideas derived from human cognition to animals. Studying so-called time perception in rats has significant shortcomings because, whether acknowledged or not, rats do not passively estimate time in their heads. They are constantly in motion. Moreover, rats do not perform the task for the sake of estimating time but to obtain their rewards are they water restricted. Their behavior will therefore reflects their motivation and urgency to obtain rewards. Unfortunately, it appears that the authors are not aware of these shortcomings. These alternative processes (motivation, sensorimotor dynamics) that occur during task performance are likely to influence neuronal activity. Consequently, my review will be rather critical. It is not however intended to be dismissive. I acknowledge that the authors may have been influenced by numerous published studies that already draw similar conclusions. Unfortunately, all the data presented in this study can be explained without invoking the concept of time estimation. Therefore, I hope the authors will find my comments constructive and understand that as scientists, we cannot ignore alternative interpretations, even if they conflict with our a priori philosophical stance (e.g., duration can be explicitly estimated by reading neuronal representation of time) and anthropomorphic assumptions (e.g., rats estimate time as humans do). While space is limited in a review, if the authors are interested, they can refer to a lengthy review I recently published on this topic, which demonstrates that my criticism is supported by a wide range of timing experiments across species (Robbe, 2023). In addition to this major conceptual issue that cast doubt on most of the conclusions of the study, there are also several major statistical issues.

Main Concerns

(1) The authors used a task in which rats must poke for a minimal amount of time (300 ms and then 1500 ms) to be able to obtain a drop of water delivered a few centimeters right below the nosepoke. They claim that their task is a time estimation task. However, they forget that they work with thirsty rats that are eager to get water sooner than later (there is a reason why they start by a short duration!). This task is mainly probing the animals ability to wait (that is impulse control) rather than time estimation per se. Second, the task does not require to estimate precisely time because there appear to be no penalties when the nosepokes are too short or when they exceed. So it will be unclear if the variation in nosepoke reflects motivational changes rather than time estimation changes. The fact that this behavioral task is a poor assay for time estimation and rather reflects impulse control is shown by the tendency of animals to perform nose-pokes that are too short, the very slow improvement in their performance (Figure 1, with most of the mice making short responses), and the huge variability. Not only do the behavioral data not support the claim of the authors in terms of what the animals are actually doing (estimating time), but this also completely annhilates the interpretation of the Ca++ imaging data, which can be explained by motivational factors (changes in neuronal activity occurring while the animals nose poke may reflect a growing sens of urgency to check if water is available).

We would like to respond to the reviewer’s comments 1, 2 and 4 together, since they all focus on the same issue. We thank the reviewer for the very thoughtful comments and for sharing his detailed reasoning from a recently published review (Robbe, 2023). A lot of discussions go beyond the scope of this study, and we agree that whether there is an explicit representation of time (an internal clock) in the brain is a difficult question to be answer, particularly by using animal behaviors. In fact, even with fully conscious humans and elaborated task design, we think it is still questionable to clearly dissociate the neural substrate of “timing” from “motor”. In the end, it may as well be that as the reviewer cited from Bergson’sarticle, the experience of time cannot be measured.

Studying the neural representation of any internal state may suffer from the same ambiguity. With all due respect, however, we would like to limit our response to the scope of our results. According to the reviewer, two alternative interpretations of the task-related sequential activity exist: 1, duration cells may represent fidgeting or orofacial movements and 2, duration cells may represent motivation or motion plan of the rats. To test the first alternative interpretation, we have now performed a more comprehensive analysis of the behavior data at all the limbs and visible body parts of the experimental rats during nose poke and analyzed its periodicity among different trials. We found that the coding cells (including duration, start and end cells) activities were not modulated by these motions, arguing against this possibility. These data are now included in the new Supp. Figure 2, and we have added corresponding texts in the manuscript.

Regarding the second alternative interpretation, we think our data in the original Figure 4G argues against it. In this graph, we plotted the decoding error of time using the duration cells’ activity against the actual duration of the trials. If the sequential activity of durations cells only represents motivation, then the errors should be linearly modulated by trial durations. The unimodal distribution we observed (Figure 4G and see graph below for a re-plot without signs) suggests that the scaling factor of the sequential activity represents information related to time. And the fact that this unimodal distribution centered at the time threshold of the task provides strong evidence for the active use of scaling factor for time estimation.

In order to further test the relationship to motivation, we have measured the time interval between exiting nose poke to the start of licking water reward as an independent measurement of motivation for each trial. We found that this reward-seeking time was positively correlated with the trial durations, suggesting that the durations were correlated with motivation to some degree. And when we scaled the activities of the duration cells by this reward-seeking time, we found that the patterns of the sequential activities were largely diminished, and showed a significantly lower peak entropy compared to the same activities scaled by trial durations. The remaining sequential pattern may be due to the correlation between trial durations and motivation (Supp. Figure 2), and the sequential pattern reflects timing more prominently. These analyses provide further evidence that the sequential activities were not coding motivations. These data are included in Figure 2F, 2K and supp. Figure 3 in revised manuscript.

Regarding whether the scaling sequential activity we report represents behavioral timing or true time estimation, we did not have evidence on this point. However, a previous study has shown that PFC silencing led to disruption of the mouse’s timing behavior without affecting the execution of the task (PMID: 24367075), arguing against the behavior timing interpretation. The main surprising finding of our present study is that these duration cells are different from the start and end cells

in terms of their coding stability. Thus, future studies dissecting the anatomical microcircuit of these duration cells may provide further clues regarding whether they are connected with reward-related or motion-related brain regions. This may help partially resolve the “time” vs.

“motor” debate the reviewer mentioned.

(2) A second issue is that the authors seem to assume that rats are perfectly immobile and perform like some kind of robots that would initiate nose pokes, maintain them, and remove them in a very discretized manner. However, in this kind of task, rats are constantly moving from the reward magazine to the nose poke. They also move while nose-poking (either their body or their mouth), and when they come out of the nose poke, they immediately move toward the reward spout. Thus, there is a continuous stream of movements, including fidgeting, that will covary with timing. Numerous studies have shown that sensorimotor dynamics influence neural activity, even in the prefrontal cortex. Therefore, the authors cannot rule out that what the records reflect are movements (and the scaling of movement) rather than underlying processes of time estimation (some kind of timer). Concretely, start cells could represent the ending of the movement going from the water spout to the nosepoke, and end cells could be neurons that initiate (if one can really isolate any initiation, which I doubt) the movement from the nosepoke to the water spout. Duration cells could reflect fidgeting or orofacial movements combined with an increasing urgency to leave the nose pokes.

(3) The statistics should be rethought for both the behavioral and neuronal data. They should be conducted separately for all the rats, as there is likely interindividual variability in the impulsivity of the animals.

We thank the reviewer for the comment, yet we are not quite sure what specifically was asked by the reviewer. It appears that the reviewer requires we conduct our analysis using each rat individually. In our revised manuscript, we have conducted and reported analyses with individual rat in the original Figure 1C, Figure 2C, G, K, Figure 4F.

(4) The fact that neuronal activity reflects an integration of movement and motivational factors rather than some abstract timing appears to be well compatible with the analysis conducted on the error trials (Figure 4), considering that the sensorimotor and motivational dynamics will rescale with the durations of the nose poke.

(5) The authors should mention upfront in the main text (result section) the temporal resolution allowed by their Ca+ probe and discuss whether it is fast enough in regard of behavioral dynamics occurring in the task.

We thank the reviewer for the suggestion. We have originally mentioned the caveat of calcium imaging in the interpretation of our results. We have now incorporated more texts for this purpose during our revision. In terms of behavioral dynamics (start and end of nose poke in this case), we think calcium imaging could provide sufficient kinetics. However, the more refined dynamics related to the reproducibility of the sequential activity or the precise representation of individual cells on the scaled duration may be benefited from improved time resolution.

Recommendations for the authors:

Reviewer #1 (Recommendations For The Authors):

(1) Please refer explicitly to the three types of cells in the abstract.

We have now modified the abstract as suggested during revision.

(2) Please refer to the work of Betancourt et al., 2023 Cell Reports, where a trial-by-trail analysis on the correlation between neural trajectory dynamics in MPC and timing behavior is reported. In that same paper the stability of neural sequences across task parameters is reported.

We have now cited and discussed the study in the discussion section of the revised manuscript.

(3) Please state the number of studied animals at the beginning of the results section.

We have now provided this information as requested. The numbers of rats are also plotted in Figure 1D for each analysis.

(4) Why do the middle and right panels of Figure 2E show duration cells.

Figure 2E was intended to show examples of duration cells’ activity. We included different examples of cells that peak at different points in the scaled duration. We believe these multiple examples would give the readers a straight forward impression of these cells’ activity patterns.

(5) Which behavioral sessions of Figure 1B were analyzed further.

We have now labeled the analyzed sessions in Figure 1B with red color in the revised manuscript.

(6) In Figure 3A-C please increase the time before the beginning of the trial in order to visualize properly the activation patterns of the start cells.

We thank the reviewer for the suggestion and have now modified the figure accordingly in the revised manuscript.

(7) Please state what could be the behavioral and functional effect of the ablation of the cortical tissue on top of mPFC.

We thank the reviewer for the question. In our experience, mice with lens implanted in the mPFC did not show observable difference with mice without surgery in the acquisition of the task and the distribution of the nose-poke durations. In our dataset, rats with the lens implantation showed similar nose-poking behavior as those without lens implantation (Figure 1B). Thus, it seems that the effect of ablation, if any, was quite limited, in the scope of our task.
