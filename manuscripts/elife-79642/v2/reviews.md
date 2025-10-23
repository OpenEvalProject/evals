# Peer review - Round 1

Editors:
- Birte U Forstmann, https://ror.org/04dkp9463 University of Amsterdam Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79642.sa0](https://doi.org/10.7554/eLife.79642.sa0)

This paper presents valuable data from 18 patients treated with GPi DBS for dystonia using a standard RL task. Their compelling main observation is that DBS reduced the impact of value on evidence accumulation leading to more exploratory choices which was supported by fitting a dynamic decision model to the data. This work will be interesting for scientists working in fundamental and clinical neurosciences.


---

# Peer review - Round 1

Editors:
- Birte U Forstmann, https://ror.org/04dkp9463 University of Amsterdam Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79642.sa1](https://doi.org/10.7554/eLife.79642.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Pallidal neuromodulation of the explore/exploit trade-off in decision-making" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Frank as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Generalizability:

Studying dystonia patients gives the unique opportunity to study the effects of electrical pallidal stimulation on decision-making in humans and given that dystonia primarily affects movements rather than cognition/decision-making this might also well be representative of healthy people. This (i.e. the similarity between task performance of patients and healthy people) is, however, not demonstrated in this study. In the introduction, the authors state that reward prediction error is intact in dystonic patients, but the paper that they cite for this (ref 34) is titled '… abnormal reward learning in cervical dystonia'. Furthermore, albeit clearly less pronounced than movement symptoms cognitive problems are present in dystonia patients (see Jahanshahi 2017 Movement Disorders). I would therefore recommend enrolling a healthy control group allowing to compare DBS ON and DBS OFF to healthy people.

2) Statistics:

I understand that Bayesian statistics cannot always directly be compared to non-Bayesian frequentist statistics. However, to me, the frequentist and Bayesian statistics are not consistent in this study. ANOVAs, etc are applied on subject-averages data using a p-value of 0.05 to distinguish between significant vs. non-significant results. In the Bayesian modelling analysis, the 95% HDI is computed. While this number is arbitrary (just as a p-value of 0.05) it still has a rationale to it given that in the scientific community 95% is also used for frequentist confidence intervals. Therefore, I think that 95% would be the most consistent choice here. However, none of the model parameters differ between ON vs. OFF regarding the 95% HDIs, since they overlap with 0 (see 'Contrast' in table 1). Especially the decision threshold and drift rate scaling parameter HDIs have a large overlap with 0, but they are still interpreted as significant based on the Bayes factor. The Bayes factor, however, is not used for the behavioral analyses. For example, there are no effects of DBS on decision times, but at the computational level, several parameters (which predict the decision time) are affected. I think for the sake of consistency of analyses within the paper the statistics of the Bayesian analyses should rely on the 95% HDI.

3) Connectome correlation analysis:

If I understand it correctly, the connectome analysis relates behavioral effects of stimulation to whole-brain networks rather than just local effects in the pallidum by testing whether patients who showed stronger effects of stimulation have electrodes that are closer to connections with different brain areas. In the abstract, the results of this analysis are reported as "… was predicted by the degree of functional connectivity between the stimulating electrode and prefrontal and sensorimotor cortices". In the discussion, it is stated that "…DBS-induced enhanced exploration correlated with the functional connectivity of the stimulation volume in the GPI to frontal cortical regions identified previously in functional imaging studies of explore-exploit decision making … The exploration-enhancing effects of GPI-DBS in our study were predicted by functional connectivity to brain regions whose neurons encode uncertainty [27] and predict behavioural switching[430 29, 30]". However, figure 4 essentially shows that almost the whole brain correlates with inter-individual differences in behavior reaching correlation coefficients as strong as -0.7 e.g. lower brain stem, cerebellum, and occipital cortex, none of which are mentioned in the paper. To me, it seems that there are correlations with very large and very distributed cortical areas rather than with specific areas in the prefrontal and sensorimotor cortex as stated in the paper.

Related to this point: The variable used for the connectomic correlation analysis is not the same variable that was affected by DBS in the statistical analysis. The statistical analysis found that P(explore) differed between DBS ON vs OFF irrespective of the session. Instead the "maximum within-session increase in P(Explore) DBS-ON – P(Explore ) DBS-OFF" was used.

4) In general, could you please explain this analysis in more detail? If I understand it correctly each voxel had a value for 'connectivity' to the stimulation field and a value for 'behavioral effect' and across patients, this then gave an R-map. How was figure 4 thresholded (only the maximum positive and negative Rs are given in the color bar)? Then p-values are listed. One is 0.04 and another one is 0.009. What is the difference between the two? These values seem to reflect the correlation of similarity between the individual map with the group map and the behavioral variable, but was the correlation with the behavioral variable not already used for creating the R-map? Describing the analysis in more detail might help make it more understandable to the audience not familiar with the analysis (including me).

5) It is my understanding that high exploration (e.g. P(Explore) of 0.2) should be related to poorer task performance since the optimal strategy would always use the high-value option and only switch rarely to identify the reversal(s). Why is it then that DBS can affect exploration but not the sum of rewards if the two are related? Should DBS not affect the sum of rewards if it for example was more pronounced in its effect on P(explore)?

6) Would the authors have predicted different effects for subthalamic deep brain stimulation? The DBS effects on the GPi are mainly interpreted in terms of reduced firing rate/activity. Since the STN exerts glutamatergic innervation of the GPi, should STN suppression lead to similar results? Conversely, GPe exerts GABAergic innervation of the STN. Should GPe suppression lead to the opposite behavioral effect? Were some of the electrodes localized within or close to the GPe rather than GPi and if so, did these patients show different behavioral effects?

7) Was the OFF vs ON DBS order counterbalanced? 3 patients did not complete the task OFF, and the ON dataset was not available in another patient. Did the authors check if the DBS order was relevant for the DBS effect on P(explore)?

8) The fact that a decrease in exploration behaviour isn't correlated with a modification of reward pay-off is at odds with the original theory of exploration/exploitation balance. This should at least have been discussed in order to convince the reader of the robustness of the effect observed on the P(Explore).

9) Alternative hypotheses concerning the role of the BG on the exploration/exploitation trade-off can be proposed (habits vs goal-directed behaviour, reward-driven vs automatism, etc.). They are not ruled out by the experimental results (even if we take them for granted despite (i).

10) It seems the decrease in exploration did not lead to a decrease in overall reward-but was the learning slower in the OFF condition? Figure 5 red and blue learning curves look similar, but the model fits in Figure 6 suggest a difference in positive learning rate.

If there truly is no difference in the acquisition, I'm surprised a significant reduction in exploration didn't slow learning at all either at the beginning or post-reversal… Does this imply exploration is not necessary to perform this task accurately?

11) The authors touch briefly on the differences between directed exploration (e.g. info-seeking) and random decision noise in the Discussion section; however, it might be worth mentioning earlier that current existing work on GPi (as far as I'm aware) largely links it to overall decision noise rather than information-seeking. (Whereas potentially other areas of the pallidum, e.g. GPe, have been implicated in explicit information-seeking exploration, as per White et al., 2019 Nature Comm). Clarifying this random/directed exploration difference early in the manuscript rather than later might be helpful.

12) P.3, l.108-109 ("Previously, studies of the explore-exploit dilemma have utilised bandit tasks with high pay-out volatility and/or multiple-choice options…") implies the use of the reversal learning task is novel in the context of explore-exploit. However, two-choice, simple-reversal tasks + RL models have been used before in this context: see Zhukovsky et al. 2019 Nature, Barnes et al. 2022 BP for rodent work, Oberwelland Weiss et al. 2020 FiNs for human work. None of those studies explicitly examine the role of GPi or use RLDDM, so the novelty of the present work remains, but the implication that previous studies haven't used reversal learning is perhaps misleading and might be best rephrased.

Similarly, the claim in the introduction (p2, l45) that the neural bases of the explore/exploit tradeoff remain poorly understood is perhaps outdated. The reference is from 15 years ago, and much work has been dedicated in the interim to the neural underpinnings of explore/exploit. While certainly there is not one clear, complete circuit agreed upon for calibrating the trade-off and not one single model that's more right than all others, it could be argued that the neural mechanisms behind explore-exploit are not more poorly understood than those behind most cognitive processes.

13) Would help to briefly explain and contextualize dystonia, for a broader audience who may be unfamiliar with it.

14) I am not sure why, in the connectivity analysis, DBS stimulation volume was linked to the maximum within-session ON-OFF p(Explore) difference … why separate by session in this analysis, when p(Explore) in panel A of the same figure, and in several of the other analyses + model fits, is calculated over all three sessions? Why is the within-session difference relevant here and nowhere else?

Relatedly, I'm not sure I understand what it means for the spatial similarity measure in Figure 4A to have a value less than 0… I'm not familiar with this type of analysis so I might just not be understanding it, but if the R-Map is built from an (?) average of individual patients' connectivity maps (as per l.224-226), how is it possible that 11/14 individuals have negative spatial similarity to the R-Map?

15) To my understanding, previous neural models and accounts of the GPi activity modulating exploration were within-task (e.g. in early trials all options are available for exploration, in later trials once one option emerged as best, GPi suppressed others); whereas in the present data, the manipulation happens across tasks. Thus we're seeing differences in an overall level of exploration rather than GPi-driven fluctuations in within-task behavior-which, while still in line with previous findings, warrants some additional questions. For instance:

– Does the within-task modulation of exploration differ in the OFF and ON states? Visual inspection of Figure 3D suggests no, but hard to tell visually.

– Would a finer p(Explore) window (say, per every 10 trials rather than every 40) indicate some interesting differences in the patterns of exploratory choices between the OFF and ON states, that might not be visible with averaging?

16) It might be worth clarifying explicitly in the text that the m parameter for scaling takes the place, in some sense, of the softmax function for RL in terms of calibrating explore/exploit behavior. This is not immediately obvious to readers unfamiliar with the RLDDM, but it's a relevant detail for interpreting modelling results in terms of exploration behavior.

17) In a similar vein, perhaps also state explicitly that the m parameter and the learning rate were previously found to be negatively correlated, and what that means. This will give the reader a bit of extra context to interpret and understand figure 7.

18) It might also help to explain why the learning rates can go outside of the usual [0; 1] interval (and they're on quite a larger scale as seen in the original RLDDM paper, though I suspect that's just a consequence of using a different dataset).

19) The present model can't capture potential fluctuations m across the session. (For instance, corresponding to increased exploration tendencies in the beginning, or right after the reversal.) Pedersen et al. present an alternative to the stable-scaling model, in which parameter m, rather than remain fixed, changes through the session; this does not fit as well with the data they used, but the difference in fit was small. When comparing the best RLDDM models to use, was a non-constant scaling model also tested? (The proposed power-law function might not necessarily reflect the intuitive exploration fluctuations in a reversal-learning task, which we might expect to differ from the PST in the original RLDDM paper, so the function might require some tweaks).

20) I am not certain this is feasible within the number of trials, but would fitting the RLDDM separately to each task version to pre- and post-reversal find any differences in how parameters change in the OFF and ON states?

Not sure we would expect any differences or what they would be under the present hypothesis on GPi function; however, having a finer measure for fluctuations in exploration (either through a model-free moving window of p-Explore, as suggested earlier, or through a dynamic scaling model, or by fitting pre- and post-reversal) could provide extra insight into how exploration is affected by the DBS manipulation.

Reviewer #2 (Recommendations for the authors):

The robustness of the effect observed on P(explore) should be discussed.

Alternative hypotheses should be discussed also.

Reviewer #3 (Recommendations for the authors):

Conceptual Comments

1) It seems the decrease in exploration did not lead to a decrease in overall reward-but was the learning slower in the OFF condition? Figure 5 red and blue learning curves look similar, but the model fits in Figure 6 suggest a difference in positive learning rate.

If there truly is no difference in acquisition, I'm surprised a significant reduction in exploration didn't slow learning at all either at the beginning or post-reversal… Does this imply exploration is not necessary to perform this task accurately?

2) The authors touch briefly on the differences between directed exploration (e.g. info-seeking) and random decision noise in the Discussion section; however, it might be worth mentioning earlier that current existing work on GPi (as far as I'm aware) largely links it to overall decision noise rather than information-seeking. (Whereas potentially other areas of the pallidum, e.g. GPe, have been implicated in explicit information-seeking exploration, as per White et al., 2019 Nature Comm). Clarifying this random/directed exploration difference early in the manuscript rather than later might be helpful.

3) P.3, l.108-109 ("Previously, studies of the explore-exploit dilemma have utilised bandit tasks with high pay-out volatility and/or multiple-choice options…") implies the use of the reversal learning task is novel in the context of explore-exploit. However, two-choice, simple-reversal tasks + RL models have been used before in this context: see Zhukovsky et al. 2019 Nature, Barnes et al. 2022 BP for rodent work, Oberwelland Weiss et al. 2020 FiNs for human work. None of those studies explicitly examine the role of GPi or use RLDDM, so the novelty of the present work remains, but the implication that previous studies haven't used reversal learning is perhaps misleading and might be best rephrased.

Similarly, the claim in the introduction (p2, l45) that the neural bases of the explore/exploit tradeoff remain poorly understood is perhaps outdated. The reference is from 15 years ago, and much work has been dedicated in the interim to the neural underpinnings of explore/exploit. While certainly there is not one clear, complete circuit agreed upon for calibrating the trade-off and not one single model that's more right than all others, it could be argued that the neural mechanisms behind explore-exploit are not more poorly understood than those behind most cognitive processes.

4) Would help to briefly explain and contextualize dystonia, for a broader audience who may be unfamiliar with it.

Analysis Comments

5) I am not sure why, in the connectivity analysis, DBS stimulation volume was linked to the maximum within-session ON-OFF p(Explore) difference … why separate by session in this analysis, when p(Explore) in panel A of the same figure, and in several of the other analyses + model fits, is calculated over all three sessions? Why is the within-session difference relevant here and nowhere else?

Relatedly, I'm not sure I understand what it means for the spatial similarity measure in Figure 4A to have a value less than 0… I'm not familiar with this type of analysis so I might just not be understanding it, but if the R-Map is built from an (?) average of individual patients' connectivity maps (as per l.224-226), how is it possible that 11/14 individuals have negative spatial similarity to the R-Map?

6) To my understanding, previous neural models and accounts of the GPi activity modulating exploration were within-task (e.g. in early trials all options are available for exploration, in later trials once one option emerged as best, GPi suppressed others); whereas in the present data, the manipulation happens across tasks. Thus we're seeing differences in an overall level of exploration rather than GPi-driven fluctuations in within-task behavior-which, while still in line with previous findings, warrants some additional questions. For instance:

– Does the within-task modulation of exploration differ in the OFF and ON states? Visual inspection of Figure 3D suggests no, but hard to tell visually.

– Would a finer p(Explore) window (say, per every 10 trials rather than every 40) indicate some interesting differences in the patterns of exploratory choices between the OFF and ON states, that might not be visible with averaging?

Modelling Comments

1) It might be worth clarifying explicitly in the text that the m parameter for scaling takes the place, in some sense, of the softmax function for RL in terms of calibrating explore/exploit behavior. This is not immediately obvious to readers unfamiliar with the RLDDM, but it's a relevant detail for interpreting modelling results in terms of exploration behavior.

2) In a similar vein, perhaps also state explicitly that the m parameter and the learning rate were previously found to be negatively correlated, and what that means. This will give the reader a bit of extra context to interpret and understand figure 7.

3) It might also help to explain why the learning rates can go outside of the usual [0; 1] interval (and they're on quite a larger scale as seen in the original RLDDM paper, though I suspect that's just a consequence of using a different dataset).

4) The present model can't capture potential fluctuations m across the session. (For instance, corresponding to increased exploration tendencies in the beginning, or right after the reversal.) Pedersen et al. present an alternative to the stable-scaling model, in which parameter m, rather than remain fixed, changes through the session; this does not fit as well with the data they used, but the difference in fit was small. When comparing the best RLDDM models to use, was a non-constant scaling model also tested? (The proposed power-law function might not necessarily reflect the intuitive exploration fluctuations in a reversal-learning task, which we might expect to differ from the PST in the original RLDDM paper, so the function might require some tweaks).

5) I am not certain this is feasible within the number of trials, but would fitting the RLDDM separately to each task version to pre- and post-reversal find any differences in how parameters change in the OFF and ON states?

Not sure we would expect any differences or what they would be under the present hypothesis on GPi function; however, having a finer measure for fluctuations in exploration (either through a model-free moving window of p-Explore, as suggested earlier, or through a dynamic scaling model, or by fitting pre- and post-reversal) could provide extra insight into how exploration is affected by the DBS manipulation.
