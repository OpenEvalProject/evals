# Peer review - Round 1

Editors:
- Emilio Salinas, Wake Forest University School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.94961.2.sa0](https://doi.org/10.7554/eLife.94961.2.sa0)

This work provides a valuable analysis of the effect of two commonly used hyperparameters, noise amplitude and firing rate regularization, on the representations of relevant and irrelevant stimuli in trained recurrent neural networks (RNNs). The results suggest an interesting interpretation of prefrontal cortex (PFC) dynamics, based on comparisons to previously published data from the same lab, in terms of decreasing metabolic cost during learning. The evidence indicating that the mechanisms identified in the RNNs are the same ones operating in PFC was considered incomplete, but could potentially be bolstered by additional analyses and appropriate revisions.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.94961.2.sa1](https://doi.org/10.7554/eLife.94961.2.sa1)

Summary:

This study compares experimental data recorded from the PFC of monkeys to the activity of recurrent neural networks trained to perform the same `task' as the monkeys, namely, to predict the delivery of reward following the presentation of visual stimuli. The visual information varied along 3 dimensions, color, shape, and width. Shape was always relevant for reward prediction, width was always irrelevant, and color was irrelevant at the beginning of the trial but became relevant later on, once it could be assessed together with shape. The neural data showed systematic changes in the representations of these features and of the expected reward as the learning progressed, and the objective of this study was to try to understand what principles could underlie these changes. The simulations and theoretical calculations indicated that the changes in PFC activity (throughout learning and throughout a trial) can be understood as an attempt by the circuitry to use an efficient representational strategy, i.e., one that uses as few spikes as possible, given that the resulting representation should be accurate enough for task performance.

Strengths:

- The paper is concise and clearly written.

- The paper shows that, in a neural circuit, the information that is decodable and the information that is task-relevant may relate in very different ways. Decodable information may be very relevant or very irrelevant. This fact is critical for interpreting the results of pure decoding studies, which often assume an equivalence. This take-home message is not emphasized by the authors, but I think is quite important.

- The results provide insight as to how neural representations may be transformed as a task is learned, which often results in subtle changes in selectivity and overall activity levels whose impact or reason is not entirely clear just by looking at the data.

Weaknesses:

The match between the real PFC and the model networks is highly qualitative, and as noted by the authors, comparisons only make sense in terms of *changes* between early and late learning. The time scales, activity levels, and decoding accuracies involved are all different between the model and recording data. This is not to disregard what the authors have done, but simply to point out an important limitation.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.94961.2.sa2](https://doi.org/10.7554/eLife.94961.2.sa2)

Summary:

The study investigates the representation of irrelevant stimuli in neural circuits using neural recordings from the primate prefrontal cortex during a passive object association task. They find a significant decrease in the linear decodability of irrelevant stimuli over the course of learning (in the time window in which the stimuli are irrelevant). They then compare these trends to RNNs trained with varying levels of noise and firing rate regularization and find agreement when these levels are at an intermediate value. In a complementary analysis, they found (in both RNNs and PFC) that the magnitude of relevant and irrelevant stimuli increased and decreased, respectively, during learning. These findings were interpreted in terms of a minimization of metabolic cost in the cortex.

To understand how stimuli can be dynamically suppressed at times when they are irrelevant, the authors constructed and analyzed a reduced two-neuron model of the task. They found a mechanism in which firing rate regularization increased the probability of negative weights in the input, pushing the neural activities below the threshold. A similar mechanism was observed in RNNs.

Strengths:

The article is well-written and the figures are easily understood. The analyses are well explained and motivated. The article provides a valuable analysis of the effect of two parameters on representations of irrelevant stimuli in trained RNNs.

Weaknesses:

(1) The mechanism for suppressing dynamically relevant stimuli appears to be incomplete and does not explain clearly enough how representations of 'color' which are suppressed through negative input weights become un-suppressed in the presence of the second variable 'shape'.

(2) Interpretation of results in terms of the effect of metabolic cost on cortical dynamics is not backed up by the presented data/analyses. The change in dynamics of 'color' representations in the prefrontal cortex only qualitatively matches RNN dynamics and may arise from other causes.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.94961.2.sa3](https://doi.org/10.7554/eLife.94961.2.sa3)

Summary:

In order to study the factors and neural dynamics that lead to the suppression of irrelevant information in the brain, the authors trained artificial neural networks in the execution of a task that involved the discrimination of complex stimuli with three main features: color, shape, and width. Specific combinations of color and shape led to a reward, but the temporal structure made color dynamically irrelevant at the beginning of the trial, and then it became relevant once the shape was presented. On the other hand, the width of the stimulus was always irrelevant. Importantly, non-human primates were also trained to execute this task (in a previous study by the authors) and the activity from neural populations from the dorsolateral Prefrontal Cortex (dlPFC) was recorded, allowing to compare the coding of information by the artificial neural network model with what happens in biological neural populations.

The authors changed systematically the amount of noise present in the neural network model, as well as limiting the firing rate of the artificial neurons to simulate the limitations imposed by high metabolic costs in biological neurons. They found that models with medium and low noise, as well as medium and low metabolic cost, developed information encoding patterns that resembled the patterns observed throughout learning in the dlPFC, as follows: early in the learning process, color information was strongly represented during the whole trial, as well as shape and width, whereas the color/shape combination significance (XOR operation) was weakly encoded. Late in learning, color information was initially suppressed (while it was deemed irrelevant) and became more prominent during the shape presentation. Width information coding decreased, and the XOR operation result became more strongly encoded.

Subthreshold activity dynamics were studied by training artificial networks consisting of 2 neurons, with the aim of understanding how dynamically irrelevant information is suppressed and then encoded more strongly at a different time during the trial. Under medium noise and medium metabolic cost, color information is suppressed by the divergence of the activity away from the level that triggers spikes. The authors claim that this subthreshold dynamic explains the suppression of irrelevant information in biological neural networks.

Strengths:

The study leverages the power of computational models to simulate biological networks and do manipulations that are difficult (if not impossible) to perform in vivo. The analyses of the activity of the network model are neat and thorough and provide a clear demonstration of how noise and metabolic costs may affect the information coding in the brain. The mathematical analyses are rigorous and nicely documented.

Weaknesses:

The study does not leverage the fact that they have access to the activity of individual neurons both on a neural network model and in neural recordings. The model/brain comparison results are limited to the decodability of different pieces of information during the execution of the task at different stages of learning. It would have been useful if the authors had shown response profiles of individual neurons, both biological and artificial, to strengthen the claim that the activity patterns are similar. Perhaps showing that the firing rates vary in a similar way in the large models (like they do for the 2-neuron model) would have been informative. For instance, it is possible that suppression is not occurring in the dlPFC, but that the PFC receives input with this information already suppressed. If suppression indeed happens in the PFC, response profiles associated with this process may be observed.

There is no way to say that the 2-neuron models are in any way informative of what happens in brain neurons, or even larger artificial networks since the sources of sensory input, noise, and inhibition will differ between biological and artificial networks. And because the firing patterns are not shown for large networks, it is not clear if some non-coding artificial neurons will become broadly inhibitory but maintain a relatively high firing rate (to mention only one possibility).
