# Peer review - Round 1

Editors:
- Martin Vinck, Ernst Strüngmann Institute (ESI) for Neuroscience in Cooperation with Max Planck Society Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63163.sa1](https://doi.org/10.7554/eLife.63163.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Perceptual decisions are often associated with widespread changes in neural activity, encompassing sensory signals, choice signals and signals relating to motor behavior. However, what is the causal relevance of these neuronal changes? Here, Zatka-Haas disentangle different components of a behavioral task, namely action selection, action initiation and sensory encoding, and characterize their unique and distributed correlates using large-scale imaging and Neuropixel recordings. Subsequently, large-scale and targeted optogenetic inactivation was used to determine which cortical regions have a direct causal relevance for behavior. Specific regions in sensory and frontal cortex made direct causal contributions to behavior in a way that can be predicted precisely from their sensory correlates. By contrast, regions with action initiation correlates were not directly causally relevant for the task, despite the fact that these regions distinguished between hits and misses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "A perceptual decision requires sensory but not action coding in mouse cortex" for consideration by eLife. Your article has been reviewed by 3 external peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Karel Svoboda (Reviewer #2).

Our decision has been reached after careful consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be further considered for publication in eLife. Reviewers made several positive comments about the ambitious nature of the study as well as the quality of the dataset. However, major concerns were raised about the interpretation of the neurometric model, the interpretation of the task correlates, and the general conceptual advance made by the study.

Reviewer #2:

The authors used widefield imaging, Neuropixels recording, optogenetic inactivation, and modeling to study the coding and causal roles of dorsal cortex in a two-alternative unforce-choice task. Consistent with the ephys data reported previously by the same lab (Steinmetz et al. 2019), widefield imaging revealed distinct patterns of cortical activity related to vision, action, and choice. Interestingly, whereas the vision correlates match their causal roles both spatially and temporally, the widespread action correlates appear to be non-causal. Based on these observations, the authors constructed a neurometric model that linearly combines population activity in visual and frontal cortex. This simple model captured the animal's behavior and predicted the difference in the inactivation effects of the two regions.

Overall, this is an interesting study that puts together a variety of experimental and computational techniques to build quantitative links among different measurements of the same task. However, the data are not completely self-consistent, and the interpretations of the results are not fully satisfying. In addition, the key findings of this study (pre-movement cortical choice coding is weak; cortical action coding is non-causal) are more likely to be task-specific rather than generalizable (as already implied by the authors).

1. Although it is nice to use multiple methods, widefield imaging and ephys record very different things. This comparson should be explored better. Where do the widefield signals come from? How does it compare to the depth distribution sampled from Neuropixels recordings? Is there any laminar signature in the ephys data? For example, in Figure 2n, the SSp trace does not rise until -50 ms, but in the imaging data (Figure 2g), significant action signal already appears in SSp at -100 ms. Could this be explained by a sampling bias towards superficial layers in widefield imaging?

2. Encoding versus decoding:

(1) In the encoding model, 20.1% of SSp neurons had significant pre-movement action encoding (Line 141), which was stronger than MOp (15.3%), whereas in Figure 2n, the action decoding of SSp is clearly weaker than MOp, with a proportion of significant pre-movement decoding far less than 20%. How csn this discrepancy be explained?

(2) Line 56 "correlates of action.… strongest in primary motor and somatosensory cortex" and Line 390 "What then might be the function of the strong MOp/SSp activity observed prior to action execution?" Given the above discrepancy, how to define the strength of "action correlates"? By encoding or decoding? For example, based on decoding (Figure 2n), one would conclude that the strongest action correlates prior to movement is in MOp/MOs, or even VISal, but not in SSp.

3. The main conclusion of this study, as manifested in the title, is that the widespread cortical action coding is not causal. But some concerns in data analysis and result interpretation may weaken this conclusion.

(1) The conclusion is based on the negative results in Figure 3d-f, which averaged over equal non-zero contrast trials. Are these the best stimulus conditions to look at? It is reasonable to use these conditions in Figure 3a-c since the balanced left and right choices on control trials may maximize any Δ Contraversive effect of inactivation. However, following the same logic, it is more likely to observe significant ΔNoGo, if any, when the Go and NoGo choices are balanced, i.e., on trials with zero contrast on both sides (~50% NoGo in Figure 1f). In other words, using non-zero contrast trials, Figure 3d-f could have substantially underestimated the inactivation effect on Action.

(2) Also related to point (1), Figure 4d suggests that VIS or MOs inactivation does increase the NoGo choices for at least unilateral stimulus conditions. Although these two areas were assumed to be only sensory-related in the context of Figure 4, they also encode action (Figure 2). In particular, the pre-movement action coding in MOs is comparable with MOp (Figure 2n). Therefore, how to reconcile the observation in Figure 4d with the conclusion that cortical action coding is not causal?

(3) One argument weakening the conclusion is that the localized unilateral inactivation could be too weak to perturb distributed action coding. The authors point this out (Line 381), but it is hard to tell whether the current interpretation is "most parsimonious" (Line 385). Without bilateral and multi-regional inactivation data, the overall conclusion of this study should be more conservative. Instead of saying "do not play a causal role", descriptions like "not locally causal" (Line 415) may be more appropriate.

4. The neurometric model seems oversimplified. It uses one scalar variable to represent the population activity of each area, with an underlying assumption that all the areas are homogeneous. But this is not the case for MOs, where contra- and ipsi-lateral visual coding are mixed (Figure 2j and m). This may explain the strange result that the weights of MOs are additive (Figure 4b), which should be discussed. Is it possible to fit a similar neurometric model using the ephys data that at least takes this level of heterogeneity into account?

5. Many different protocols have been used throughout the paper, but the motivations are not always clear, making the results sometimes difficult to compare. For example:

(1) The open-loop period was used in imaging and ephys sessions, but not in the inactivation experiments. Did the animals behave differently with and without the open-loop period?

(2) In the pulse inactivation experiment, 15 mW 25 ms photostimuli were used, but in Figure 3 Sup. 3c and f, the simultaneous ephys recordings were done with 4 mW, 10 ms. It is unclear how different these two protocols could be in terms of the long-lasting suppression effect, which is important for interpreting Figure 3h and i. Moreover, the rebound after 100 ms seems to be strong in Figure 3 Sup. 3c and f. Could it be even stronger in 15 mW 25 ms case? Rebound activity can greatly confound interpretation of inactivation experiments.

(3) In Figure 4, multiple laser powers were used, but the data were pooled together to compare with the neurometric model. Is this valid given that the effect of MOs inactivation depends on the laser power Figure 3 Sup.1f? This also raises a concern related to major point 3(3): what if higher powers are used in Figure 3d-f? It seems unfair to include 2.9 and 4.25 mW in Figure 4 while drawing conclusion from Figure 3d-f using only 1.5 mW.

Reviewer #3:

This is a very ambitious study using an impressive set of cutting-edge techniques. The authors' goal is to address the timely and interesting question "where in the cortex does neural activity code for sensation, choice, and action?" They present data from wide-field imaging, single-unit recordings, and targeted optogenetic inactivation, along with a model. They ultimately find neural representations of sensation and motor action, but very little encoding of choice, across the cortical mantle, and this is reinforced by the results of cortical inactivation. Overall, the lack of truly novel results and the incomplete nature of the findings reduce the potential impact.

The study falls short for two reasons. First, this may simply be the wrong task in which to examine choice representation in the cortex. As the authors nicely show, mice begin turning the wheel immediately after the stimulus presentation, and no delay is enforced. To deeply examine the question posed by the authors, the task would need to have stimulus, delay, and response periods separated to allow the experimenter to observe and perturb uncontaminated patterns of neural activity.

Second, the authors may not be using the right approach to detect key populations of cortical neurons. They suggest that the sparseness of neurons that encode choice indicates that the cortex simply does not generally function in this aspect of the behavior. They further point to the idea that subcortical areas such as the colliculus and the striatum have been implicated in visual detection tasks. However, the authors do not include data showing that choice is in fact encoded by neurons in those regions. Recent studies (Lee at al, Cell Reports 2020; Tang et al. Neuron 2020; Puscian et al. Cell Reports 2020, etc) have in fact shown that neurons in primary visual cortex robustly encode choice in visual detection tasks. However, several of these papers highlighted that this encoding is a feature of neural populations with projection targets specific to the type of task. Thus, Neuropixels recordings of unidentified neurons may give the mistaken impression that choice encoding is extremely sparse or not present in the cortex, but targeted recordings or imaging of specific populations may reveal that such encoding is robust. Such a finding would be entirely in keeping with the growing realization in the field that each cortical area may represent physically intermingled but functionally separable components of large-scale circuits.

Reviewer #4:

Understanding the relationships between neural activity and function continues to be a major undertaking. This study uses widefield calcium imaging and Neuropixel recording data to interpret causal impacts of optogenetic suppression sampled across dorsal cortex. The authors present the novel findings that (1) effects of optogenetic suppression are specifically correlated with the magnitude of sensory encoding within each region and (2) frontal and occipital cortices make different contributions to choice formation (substrative vs additive).

The experiments and analyses are performed at high quality. The insights are novel, interesting, and relevant to a general neuroscience audience. The points below attempt to clarify some of the major findings.

– I encourage the authors to carefully acknowledge what is novel in this study as opposed to published work from recent studies (eg, Steinmetz et al., 2019). For example, the presentation of single unit choice probability in the Results and Discussion do not appropriately acknowledge which analyses and assessments are novel.

– I am concerned with the central of the logic of the study as presented. If we consider the framework that decision-making occurs before action/response, then of course we would not expect action coding to impact 'a perceptual decision'. And yet, given the title, the authors appear to consider this a core finding of their study.

– (Related to above) I would expect action coding to causally impact motor performance. Indeed, the authors report that MOp suppression reduced peak wheel velocity by 20%. It seems odd that this important finding is minimized in the Results and Discussion. This finding argues strongly that the action signals in MOp do not solely reflect a corollary discharge. Did suppression in other 'action coding' regions also alter motor performance (wheel velocity, reaction time, other measures)?

– What is the reason for the additional optogenetic suppression experiments presented in in Figure 4 (how are they different from the experiments presented in Figure 3)? Are the lack of effects on NoGo probability in Figure 3D inconsistent with the increased Misses in Figure 4D? Is the lack of increased incorrect responses in MOs in Figure 4D inconsistent with the increased rightward choices in MOs in Figure 3A?

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for choosing to send your work entitled "A perceptual decision requires sensory but not action coding in mouse cortex" for consideration at eLife. Your article has been considered by a Senior Editor and a Reviewing editor, and we are prepared to consider a revised submission.

Please take note of the following points when preparing your revised submission:

Reviewers made several positive comments about the ambitious nature of the study as well as the quality of the dataset, which combines many different techniques in a technically impressive manner. Reviewers generally commented positively on the identification of causally related task correlates related to sensory perception, which is based on a combination of optogenetics, recordings and modelling. However, they still had major concerns about the interpretation and analysis of the choice and action correlates, including about issues covered in the action plan that should be considered further, as follows:

1) Explain conceptual advance

The authors should better explain the novelty of their findings and the relationship to previous work (in particular Steinmetz et al. 2019). For example it needs to be clarified which aspects of findings using the same dataset are novel, e.g. the presentation of single unit choice probability.

2) Improve overall conceptual interpretation of task correlates and lack of choice correlates

(i) The study should explain better how to understand the concept of choice in light of their task and findings. The authors should discuss why this is an appropriate task to study choice representation in the cortex, and how the interpretations of the authors might be constrained by not having separate stimulus, delay and response periods. The authors should improve their explanation of the difference between choice vs. no/go correlates.

(ii) The authors should clarify the central of the logic of the study. If we consider the framework that decision-making occurs before action/response, then one would not expect action coding to impact 'a perceptual decision'. And yet, given the title, the authors appear to consider this a core finding of their study.

(iii) One argument weakening the conclusion about the finding that widespread action coding is not causal, is that the localized unilateral inactivation could be too weak to perturb distributed action coding. The authors point this out (Line 381), but it is hard to tell whether the current interpretation is "most parsimonious" (Line 385). Without bilateral and multi-regional inactivation data, the overall conclusion of this study should be more conservative. Instead of saying "do not play a causal role", descriptions like "not locally causal" (Line 415) may be more appropriate.

(iv) The authors should address the apparent discrepancy with studies (e.g. Lee at al, Cell Reports 2020; Tang et al. Neuron 2020; Puscian et al. Cell Reports 2020, etc) that show that neurons in primary visual cortex robustly encode choice in visual detection tasks.

(v) The authors should discuss the possibility that targeted recordings or imaging of specific populations according to projection patterns may reveal that choice encoding is robust, following the idea that there could be functionally separable components of large-scale circuits, and that choice encoding might a feature of neural populations with projection targets specific to the type of task.

3) Interpretation and analysis of action correlates

The main conclusion of this study, as manifested in the title, is that the widespread cortical action coding is not causal. The authors should address several concerns in data analysis and result interpretation that may weaken this conclusion.

(i) The conclusion is based on the negative results in Figure 3d-f, which averaged over equal non-zero contrast trials. Are these the best stimulus conditions to look at? It is reasonable to use these conditions in Figure 3a-c since the balanced left and right choices on control trials may maximize any Δ Contraversive effect of inactivation. However, following the same logic, it is more likely to observe significant ΔNoGo, if any, when the Go and NoGo choices are balanced, i.e., on trials with zero contrast on both sides (~50% NoGo in Figure 1f). In other words, using non-zero contrast trials, Figure 3d-f could have substantially underestimated the inactivation effect on Action.

(ii) Also related to point (3-i), Figure 4d suggests that VIS or MOs inactivation does increase the NoGo choices for at least unilateral stimulus conditions. Although these two areas were assumed to be only sensory-related in the context of Figure 4, they also encode action (Figure 2). In particular, the pre-movement action coding in MOs is comparable with MOp (Figure 2n). Therefore, how to reconcile the observation in Figure 4d with the conclusion that cortical action coding is not causal?

(iii) Related to the question whether action coding causally impact motor performance: Indeed, the authors report that MOp suppression reduced peak wheel velocity by 20%. The authors should discuss this finding more prominently in the Results and Discussion. This finding argue that the action signals in MOp do not solely reflect a corollary discharge. Did suppression in other 'action coding' regions also alter motor performance (wheel velocity, reaction time, other measures)?

4) Comparison between encoding vs. decoding results

(i) In the encoding model, 20.1% of SSp neurons had significant pre-movement action encoding (Line 141), which was stronger than MOp (15.3%), whereas in Figure 2n, the action decoding of SSp is clearly weaker than MOp, with a proportion of significant pre-movement decoding far less than 20%. How can this discrepancy be explained?

(ii) Line 56 "correlates of action.… strongest in primary motor and somatosensory cortex" and Line 390 "What then might be the function of the strong MOp/SSp activity observed prior to action execution?" Given the above discrepancy, how to define the strength of "action correlates"? By encoding or decoding? For example, based on decoding (Figure 2n), one would conclude that the strongest action correlates prior to movement is in MOp/MOs, or even VISal, but not in SSp.

5) Comparison between modalities

The comparison between different methods, in particular widefield imaging and ephys recordings, should be explored better. Where do the widefield signals come from? How does it compare to the depth distribution sampled from Neuropixels recordings? Is there any laminar signature in the ephys data? For example, in Figure 2n, the SSp trace does not rise until -50 ms, but in the imaging data (Figure 2g), significant action signal already appears in SSp at -100 ms. Could this be explained by a sampling bias towards superficial layers in widefield imaging?

6) Use of CCCP

CCCP, as a measure of choice probability, appears to be misleading when used to describe analyses to quantify sensory and action coding. One possibility is to introduce the general method of Combined Conditions Probability, and apply this analysis to Stimulus, Choice, or Action. (sCCP, cCCP, aCCP).

7) Comparison between protocols

Many different protocols have been used throughout the paper, but the motivations are not always clear, making the results sometimes difficult to compare. For example:

(i) The open-loop period was used in imaging and ephys sessions, but not in the inactivation experiments. Did the animals behave differently with and without the open-loop period?

(ii) In the pulse inactivation experiment, 15 mW 25 ms photostimuli were used, but in Figure 3 Sup. 3c and f, the simultaneous ephys recordings were done with 4 mW, 10 ms. It is unclear how different these two protocols could be in terms of the long-lasting suppression effect, which is important for interpreting Figure 3h and i. Moreover, the rebound after 100 ms seems to be strong in Figure 3 Sup. 3c and f. Could it be even stronger in 15 mW 25 ms case? Rebound activity can greatly confound interpretation of inactivation experiments.

(iii) In Figure 4, multiple laser powers were used, but the data were pooled together to compare with the neurometric model. Is this valid given that the effect of MOs inactivation depends on the laser power Figure 3 Sup.1f? This also raises a concern related to major point 3(3): what if higher powers are used in Figure 3d-f? It seems unfair to include 2.9 and 4.25 mW in Figure 4 while drawing conclusion from Figure 3d-f using only 1.5 mW.

(iv) What is the reason for the additional optogenetic suppression experiments presented in in Figure 4 (how are they different from the experiments presented in Figure 3)? Are the lack of effects on NoGo probability in Figure 3D inconsistent with the increased Misses in Figure 4D? Is the lack of increased incorrect responses in MOs in Figure 4D inconsistent with the increased rightward choices in MOs in Figure 3A?

8) Neurometric model related to sensory correlates:

The authors should discuss why the relatively simple neurometric model is appropriate. It uses one scalar variable to represent the population activity of each area, with an underlying assumption that all the areas are homogeneous. But this is not the case for MOs, where contra- and ipsi-lateral visual coding are mixed (Figure 2j and m). This may explain the strange result that the weights of MOs are additive (Figure 4b), which should be discussed. Is it possible to fit a similar neurometric model using the ephys data that at least takes this level of heterogeneity into account? The authors should address why a model with additive weights for MO and visual cortex is appropriate given that one might expect MO activity to depend on activity in the visual cortex.
