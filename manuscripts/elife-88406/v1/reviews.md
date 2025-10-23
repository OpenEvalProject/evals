# Peer review - Round 1

Editors:
- Srdjan Ostojic, École Normale Supérieure - PSL France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.88406.3.sa0](https://doi.org/10.7554/eLife.88406.3.sa0)

This study reports valuable behavioral and computational observations regarding how passive exposure to auditory stimuli can facilitate auditory categorization. The combination of behavioral results in mice with a study of artificial neural network models provides solid evidence for the authors' conclusions. This paper will likely be of broad interest to the general neuroscience community.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88406.3.sa1](https://doi.org/10.7554/eLife.88406.3.sa1)

Schmid et al. investigate the question of how sensory learning in animals and artificial networks is driven both by passive exposure to the environment (unsupervised) and from reinforcing feedback (supervised) and how these two systems interact. They first demonstrate in mice that passive exposure to the same auditory stimuli used in a discrimination task modify learning and performance in the task. Based on this data, they then tested how the interaction of supervised and unsupervised learning in an artificial network could account for the behavioural results.

The clear behavioural impact of the passive exposure to sounds on accelerating learning is a major strength of the paper. Moreover, the observation that passive exposure had a positive impact on learning whether it was prior to the task or interleaved with learning sessions provides interesting constraints for modelling the interaction between supervised and unsupervised learning. A practical fallout for labs performing long training procedures is that the periods of active learning that require water-restriction could be reduced by using passive sessions. This could increase both experimental efficiency and animal well-being.

The modelling section clearly exhibits the differences between models and the step-by-step presentation building to the final model provides the reader with a lot of intuition about how supervised and unsupervised learning interact. In particular the authors highlight situations in which the task-relevant discrimination does not align with the directions of highest variance, thus reinforcing the relevance of their conclusions for the complex structure of sensory stimuli. A great strength of these models is that they generate clear predictions about how neural activity should evolve during the different training regimes that would be exciting to test.

As the authors acknowledge, the experimental design presented cannot clearly show that the effect of passive exposure was due to the specific exposure to task-relevant stimuli since there is no control group exposed to irrelevant stimuli. Studies have shown that exposure to a richer sensory environment, even in the adult, swiftly (ie within days) enhances responses even in the adult and even when the stimuli are different from those present in the task (1-3). Clearly distinguishing between these two options would require further experiments and could be a possible direction for future research.

1. Mandairon, N., Stack, C. & Linster, C. Olfactory enrichment improves the recognition of individual components in mixtures. Physiol. Behav. 89, 379-384 (2006).

2. Alwis, D. S. & Rajan, R. Environmental enrichment and the sensory brain: The role of enrichment in remediating brain injury. Front. Syst. Neurosci. 8, 1-20 (2014).

3. Polley, D. B., Kvašňák, E. & Frostig, R. D. Naturalistic experience transforms sensory maps in the adult cortex of caged animals. Nature 429, 67-71 (2004).


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88406.3.sa2](https://doi.org/10.7554/eLife.88406.3.sa2)

Schmid et al present a lovely study looking at the effect of passive auditory exposure on learning a categorization task.

The authors utilize a two-alternative choice task where mice have to discriminate between upward and downward moving frequency sweeps. Once mice learn to discriminate easy stimuli, the task is made psychometric and additional intermediate stimuli are introduced (as is standard in the literature). The authors introduce an additional two groups of animals, one that was passively exposed to the task stimuli before any behavioral shaping, and one that had passive exposure interleaved with learning. The major behavioral finding is that passive exposure to sounds improves learning speed. The authors show this in a number of ways through linear fits to the learning curves. Additionally, by breaking down performance based on the "extreme" vs "psychometric" stimuli, the authors show that passive exposure can influence responses to sounds that were not present during the initial training period. One limitation here is that the presented analysis is somewhat simplistic, does not include any detailed psychometric analysis (bias, lapse rates etc), and primarily focuses on learning speed. Ultimately though, the behavioral results are interesting and seem supported by the data.

To investigate the neural mechanisms that may underlie their behavioral findings, the authors turn to a family of artificial neural network models and evaluate the consequences of different learning algorithms and schedules, network architectures, and stimulus distributions, on the learning outcomes. The authors work through five different architectures that fail to recapitulate the primary behavior findings before settling on a final model, utilizing a combination of supervised and unsupervised learning, that was capable of reproducing the key aspects of the experiments. Ultimately, the behavioral results presented are consistent with network models that build latent representations of task-relevant features that are determined by statistical properties of the input distribution.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.88406.3.sa3](https://doi.org/10.7554/eLife.88406.3.sa3)

Summary of Author's Results/Intended Achievements

The authors were trying to ascertain the underlying learning mechanisms and network structure that could explain their primary experimental finding: passive exposure to a stimulus (independent of when the exposure occurs) can lead to improvements in active (supervised) learning. They modeled their task with 5 progressively more complex shallow neural networks classifying vectors drawn from multi-variate Gaussian distributions.

Account of Major Strengths:

Overall, the experimental findings were interesting. The modelling was also appropriate, with a solid attempt at matching the experimental condition to simplified network models.
