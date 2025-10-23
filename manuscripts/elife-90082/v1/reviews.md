# Peer review - Round 1

Editors:
- Joshua I Gold, University of Pennsylvania United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.90082.3.sa0](https://doi.org/10.7554/eLife.90082.3.sa0)

In this study, Ger and colleagues present a valuable new technique that uses recurrent neural networks to distinguish between model misspecification and behavioral stochasticity when interpreting cognitive-behavioral model fits. Simulations provide solid evidence for the validity of this technique and broadly support the claims of the article, although more work is needed to understand its applicability to real behavioral experiments. This technique addresses a long-standing problem that is likely to be of interest to researchers pushing the limits of cognitive computational modeling.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90082.3.sa1](https://doi.org/10.7554/eLife.90082.3.sa1)

Summary:

Ger and colleagues address an issue that often impedes computational modeling: the inherent ambiguity between stochasticity in behavior and structural mismatch between the assumed and true model. They propose a solution to use RNNs to estimate the ceiling on explainable variation within a behavioral dataset. With this information in hand, it is possible to determine the extent to which "worse fits" result from behavioral stochasticity versus failures of the cognitive model to capture nuances in behavior (model misspecification). The authors demonstrate the efficacy of the approach in a synthetic toy problem and then use the method to show that poorer model fits to 2-step data in participants with low IQ are actually due to an increase in inherent stochasticity, rather than systemic mismatch between model and behavior.

Strengths:

Overall I found the ideas conveyed in the paper interesting and the paper to be extremely clear. The method itself is clever and intuitive and I believe it could potentially be useful in certain circumstances, particularly ones where the sources of structure in behavioral data are unknown. Support for the method from synthetic data is clear and compelling. The flexibility of the method means that it could potentially be applied to different types of behavioral data - without any hypotheses about the exact behavioral features that might be present in a given task.

Weaknesses:

That said, I have some concerns with the manuscript in its current form, largely related to the applicability of the proposed methods for problems of importance in computational cognitive neuroscience. This concern stems from the fact that the toy problem explored in the manuscript is somewhat simple, and the theoretical problem addressed in it could have been identified through other means (for example through use of posterior predictive checking for model validation), and the actual behavioral data analyzed were interpreted as a null result (failure to reject that the behavioral stochasticity hypothesis), rather than actual identification of model misspecification. Thus, in my opinion, the jury is still out on whether this method could be used to identify a case of model misspecification that actually affects how individual differences are interpreted in a real cognitive task. Furthermore, the method requires considerable data for pretraining, well beyond what would be collected in a typical behavioral study, raising further questions about its applicability in problems of practical relevance. I expand on these primary concerns and raise several smaller points below.

A primary concern I have about this work is that it is unclear whether the method described could provide any advantage for real cognitive modeling problems beyond what is typically done to minimize the chance of model misspecification (in particular, posterior predictive checking). The toy problem examined in the manuscript is pretty extreme (two of the three synthetic agents are very far from what a human would do on the task, and the models deviate from one another to a degree that detecting the difference should not be difficult for any method). The issue posed in the toy data would easily be identified by following good modeling practices, which include using posterior predictive checking over summary measures to identify model insufficiencies, which in turn would call for the need for a broader set of models (See Wilson & Collins 2019). In this manuscript descriptive analyses are not performed (which, to me, feels a bit problematic for a paper that aims to improve cognitive modeling practices), however I think it is almost certain that the differences between the toy models would be evident by eye in standard summary measures of two-step task data. The primary question posed in the analysis of the empirical data is as to whether fit differences related IQ might reflect systematic differences in the model across individuals, but in this case application of the newly developed method provides little evidence for structural (model) differences. Thus, it remains unclear whether the method could identify model misspecification in real world data, and even more so whether it could reveal misspecification in situations where standard posterior predictive checking techniques would fall short. The rebuttal highlighted the better fit of the RNN on the empirical data as providing positive evidence for the ability of the method to identify model insufficiency, but I see this result as having limited epistemological value, given that there is no follow up to explore what the insufficiency actually was, or why accounting for it might be important. The authors list many of the points above as limitations in their discussion section, but in my opinion, they are relatively major ones.

The manuscript now mentions in the discussion that the newly developed methods should be seen as being just one tool in the larger toolkit of the computational cognitive modeler. However, one practical consideration here is that, since other existing tools such as simulation and descriptive analyses can be combined to (1) identify model insufficiency, (2) motivate specific model changes that can fix the problem, it is not exactly clear what the value added from the proposed method is.

One final practical limitation of the method is that it requires extensive pretraining (on >500 participants) in existing study, limiting its applicability for most use cases.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90082.3.sa2](https://doi.org/10.7554/eLife.90082.3.sa2)

SUMMARY:

In this manuscript, Ger and colleagues propose two complementary analytical methods aimed at quantifying the model misspecification and irreducible stochasticity in human choice behavior. The first method involves fitting recurrent neural networks (RNNs) and theoretical models to human choices and interpreting the better performance of RNNs as providing evidence of the misspecifications of theoretical models. The second method involves estimating the number of training iterations for which the fitted RNN achieves the best prediction of human choice behavior in a separate, validation data set, following an approach known as "early stopping". This number is then interpreted as a proxy for the amount of explainable variability in behavior, such that fewer iterations (earlier stopping) correspond to a higher amount of irreducible stochasticity in the data. The authors validate the two methods using simulations of choice behavior in a two-stage task, where the simulated behavior is generated by different known models. Finally, the authors use their approach in a real data set of human choices in the two-stage task, concluding that low-IQ subjects exhibit greater levels of stochasticity than high-IQ subjects.

STRENGTHS:

The manuscript explores an extremely important topic to scientists interested in characterizing human decision-making. While it is generally acknowledged that any computational model of behavior will be limited in its ability to describe a particular data set, one should hope to understand whether these limitations arise due to model misspecification or due to irreducible stochasticity in the data. Evidence for the former suggests that better models ought to exist; evidence for the latter suggests they might not.

To address this important topic, the authors elaborate carefully on the rationale of their proposed approach. They describe a variety of simulations -- for which the ground truth models and the amount of behavioral stochasticity are known -- to validate their approaches. This enables the reader to understand the benefits (and limitations) of these approaches when applied to the two-stage task, a task paradigm commonly used in the field. Through a set of convincing analyses, the authors demonstrate that their approach is capable of identifying situations where an alternative, untested computational model can outperform the set of tested models, before applying these techniques to a realistic data set.

WEAKNESSES:

The most significant weakness is that the paper rests on the implicit assumption that the fitted RNNs explain as much variance as possible, an assumption that is likely incorrect and which can result in incorrect conclusions. While in low-dimensional tasks RNNs can predict behavior as well as the data-generating models, this is not always the case, and the paper itself illustrates (in Figure 3) several cases where the fitted RNNs fall short of the ground-truth model. In such cases, we cannot conclude that a subject exhibiting a relatively poor RNN fit necessarily has a relatively high degree of behavioral stochasticity. Instead, it is at least conceivable that this subject's behavior is generated precisely (i.e., with low noise) by an alternative model that is pooly fit by an RNN -- e.g., a model with long-term sequential dependencies, which RNNs are known to have difficulties in capturing.

These situations could lead to incorrect conclusions for both of the proposed methods. First, the model mis-specification analysis might show equal predictive performance for a particular theoretical model and for the RNN. While a scientist might be inclined to conclude that the theoretical model explains the maximum amount of explainable variance and therefore that no better model should exist, the scenario in the previous paragraph suggests that a superior model might nonetheless exist. Second, in the early-stopping analysis, a particular subject may achieve optimal validation performance with fewer epochs than another, leading the scientist to conclude that this subject exhibits higher behavioral noise. However, as before, this could again result from the fact that this subject's behavior is produced with little noise by a different model. The possibility of such scenarios does not mean that such scenarios are common, and the conclusions drawn in the paper are likely appropriate for the particular examples analyzed. However, it is much less obvious that the RNNs will provide optimal fits in other types of tasks, particularly those with more complex rules and long-term sequential dependencies, and in such scenarios, an ill-advised scientist might end up drawing incorrect conclusions from the application of the proposed approaches. The authors acknowledge this limitation in their discussion, but it remains a significant caveat that readers should be aware of when using the technique proposed.

In addition to this general limitation, the relationship between the number of optimal epochs and behavioral stochasticity may not hold for every task and every subject. For example, Figure 4 highlights the relationship between the optimal epochs and agent noise. Yet, it is nonetheless possible that the optimal epoch is influenced by model parameters other than inverse temperature (e.g., hyperparameters such as learning rate, etc). This could again lead to invalid conclusions, such as concluding that low-IQ is associated with optimal epoch when an alternative account might be that low-IQ is associated with low learning rate, which in turn is associated with optimal epoch. Additional factors such as the deep double-descent (Nakkiran et al., ICLR 2020) can also influence the optimal epoch value as computed by the authors. These concerns are partially addressed by the authors in the revised manuscript, where they show that the number of optimal epochs is primarily sensitive to the amount of true underlying noise, assuming the number of trials and network size are constant. The authors also acknowledge, in the discussion section, that many factors can affect the number of optimal epochs, and that inferring behavioral stochasticity from this number should be done with caution.

APPRAISAL AND DISCUSSION:

Overall, the authors propose a novel method that aims to solve an important problem, but since the evidence provided refers to a single task and to a single dataset, it is not clear that the method would be appropriate in general settings. In the future, it would be beneficial to test the proposed approach in a broader setting, including simulations of different tasks, different model classes, and different model parameters. Nonetheless, even without such additional work, the proposed methods are likely to be used by cognitive scientists and neuroscientists interested in assessing the quality and limits of their behavioral models.
