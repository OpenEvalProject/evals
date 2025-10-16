# Peer review - Round 1

Editors:
- Hang Zhang, Peking University China

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.87197.3.sa0](https://doi.org/10.7554/eLife.87197.3.sa0)

This study provides a valuable contribution to the study of eye-movements in reading, revealing that attention-weights from a deep neural network show a statistically reliable fit to the word-level reading patterns of humans. Its evidence is convincing and strengthens a line of research arguing that attention in reading reflects task optimization. The work would be of interest to psychologists, neuroscientists, and machine learning researchers.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87197.3.sa1](https://doi.org/10.7554/eLife.87197.3.sa1)

This manuscript describes a set of four passage-reading experiments which are paired with computational modeling to evaluate how task-optimization might modulate attention during reading. Broadly, participants show faster reading and modulated eye-movement patterns of short passages when given a preview of a question they will be asked. The attention weights of a Transformer-based neural network (BERT and variants) show a statistically reliable fit to these reading patterns above-and-beyond text- and semantic-similarity baseline metrics, as well as a recurrent-network-based baseline. Reading strategies are modulated when questions are not previewed, and when participants are L1 versus L2 readers, and these patterns are also statistically tracked by the same transformer-based network.

Strengths:

- Task-optimization is a key notion in current models of reading and the current effort provides a computationally rigorous account of how such task effects might be modeled

- Multiple experiments provide reasonable effort towards generalization across readers and different reading scenarios

- Use of RNN-based baseline, text-based features, and semantic features provides a useful baseline for comparing Transformer-based models like BERT

Weaknesses:

- Generalization across neural network models may be limited (models differ in size, training data etc.); it is thus not always clear which specific model characteristics support their fit to human reading patterns.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87197.3.sa2](https://doi.org/10.7554/eLife.87197.3.sa2)

In this study, researchers aim to understand the computational principles behind attention allocation in goal-directed reading tasks. They explore how deep neural networks (DNNs) optimized for reading tasks can predict reading time and attention distribution. The findings show that attention weights in transformer-based DNNs predict reading time for each word. Eye tracking reveals that readers focus on basic text features and question-relevant information during initial reading and rereading, respectively. Attention weights in shallow and deep DNN layers are separately influenced by text features and question relevance. Additionally, when readers read without a specific question in mind, DNNs optimized for word prediction tasks can predict their reading time. Based on these findings, the authors suggests that attention in real-world reading can be understood as a result of task optimization.

Strengths of the Methods and Results:

The present study employed stimuli consisting of paragraphs read by middle and high school students, covering a wide range of diverse topics. This choice ensured that the reading experience for participants remained natural, ultimately enhancing the ecological validity of the findings and conclusions.

In Experiments 1-3, participants were instructed to read questions before the text, while in Experiment 4 participants were instructed to read questions after the text. This deliberate manipulation allowed the paper to assess how different reading task conditions influence reading and eye movements.

Weaknesses of the Methods and Results:

While the study benefits from several strengths, it is important to acknowledge its limitations. Notably, recent months have seen significant advancements in Deep Neural Network (DNN) models, including the development of models such as GPT-3.5 and GPT-4, which have demonstrated remarkable capabilities in tasks resembling human cognition, like Theory of Mind. However, as the code for these cutting-edge models was not publicly accessible, they were unable to evaluate whether the attention mechanisms in the most up-to-date DNN models could provide improved predictions for human eye-movement data. This constraint represents a limitation in the investigation.

The methods and data presented in this study are valuable for gaining insights into the psychological mechanisms of reading. Moreover, the data provided in this paper may prove instrumental in enhancing the performance of future DNN models.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87197.3.sa3](https://doi.org/10.7554/eLife.87197.3.sa3)

This paper presents several eyetracking experiments measuring task-directed reading behavior where subjects read texts and answered questions. It then models the measured reading times using attention patterns derived from deep-neural network models from the natural language processing literature. Results are taken to support the theoretical claim that human reading reflects task-optimized attention allocation.

Strengths:

(1) The paper leverages modern machine learning to model a high-level behavioral task (reading comprehension). While the claim that human attention reflects optimal behavior is not new, the paper considers a substantially more high-level task in comparison to prior work. The paper leverages recent models from the NLP literature which are known to provide strong performance on such question-answering tasks, and is methodologically well grounded in the NLP literature.

(2) The modeling uses text- and question-based features in addition to DNNs, specifically evaluates relevant effects, and compares vanilla pretrained and task-finetuned models. This makes the results more transparent and helps assess the contributions of task optimization. In particular, besides fine-tuned DNNs, the role of the task is further established by directly modeling the question relevance of each word. Specifically, the claim that human reading is predicted better by task-optimized attention distributions rests on (i) a role of question relevance in influencing reading in Expts 1-2 but not 4, and (ii) the fact that fine-tuned DNNs improve prediction of gaze in Expts 1-2 but not 4.

(3) The paper conducts experiments on both L2 and L1 speakers.

Weaknesses:

(1) Under the hypothesis advanced, human reading should adapt rationally to task demands. Indeed, Experiment 1 tests questions from different types in blocks (local and global), and the paper provides evidence that this encourages the development of question-type-specific reading strategies -- indeed, this specifically motivates Experiment 2, and is confirmed indirectly in the comparison of the effects found in the two experiments ("all these results indicated that the readers developed question-type-specific strategies in Experiment 1"). On the other hand, finetuning the model on one of the two types does not seem to reproduce this differential behavior, in the sense that fit to reading data is not improved. In this sense, the model seems to have limited abilities in reproducing the observed task dependence of human reading.

The results support the conclusions well, with the weakness described above a limitation of the modeling approach chosen.

The data are likely to be useful as a benchmark in further modeling of eye-movements, an area of interest to computational research on psycholinguistics.

The modeling results contribute to theoretical understanding of human reading behavior, and strengthens a line of research arguing that it reflects task-adaptive behavior.
