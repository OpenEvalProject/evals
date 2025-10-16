# Peer review - Round 1

Editors:
- Hang Zhang, https://ror.org/02v51f717 Peking University China

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.97894.3.sa0](https://doi.org/10.7554/eLife.97894.3.sa0)

This important work proposes a neural network model of interactions between the prefrontal cortex and basal ganglia to implement adaptive resource allocation in working memory, where the gating strategies for storage are adjusted by reinforcement learning. Numerical simulations provide convincing evidence for the superiority of the model in improving effective capacity, optimizing resource management, and reducing error rates, as well as for its human-like performance. This work will be of broad interest to computational and cognitive neuroscientists, and may also interest machine-learning researchers who seek to develop brain-inspired machine-learning algorithms for memory.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97894.3.sa1](https://doi.org/10.7554/eLife.97894.3.sa1)

Summary:

In this research, Soni and Frank investigate the network mechanisms underlying capacity limitations in working memory from a new perspective, with a focus on Visual Working Memory (VWM). The authors have advanced beyond the classical neural network model, which incorporates the prefrontal cortex and basal ganglia (PBWM), by introducing an adaptive chunking variant. This model is trained using a biologically-plausible, dopaminergic reinforcement learning framework. The adaptive chunking mechanism is particularly well-suited to the VWM tasks involving continuous stimuli and elegantly integrates the 'slot' and 'resource' theories of working memory constraints. The chunk-augmented PBWM operates as a slot-like system with resource-like limitations.

Through numerical simulations under various conditions, Soni and Frank demonstrate the performance of the chunk-augmented PBWM model surpass the no-chunk control model. The improvements are evident in enhanced effective capacity, optimized resource management, and reduced error rates. The retention of these benefits, even with increased capacity allocation, suggests that working memory limitations are due to a combination of factors, including the efficient credit assignment that are learned flexibly through reinforcement learning. In essence, this work addresses fundamental questions related to a computational working memory limitation using a biologically-inspired neural network, thus has implications for conditions such as Parkinson's disease, ADHD and schizophrenia.

Strengths:

The integration of mechanistic flexibility, reconciling two theories for WM capacity into a single unified model, results in a neural network that is both more adaptive and human-like. Building on the PBWM framework ensures the robustness of the findings. The addition of the chunking mechanism tailors the original model for continuous visual stimuli. Chunk-stripe mechanisms contribute to the 'resource' aspect, while input-stripes contribute to the 'slot' aspect. This combined network architecture enables flexible and diverse computational functions, enhancing performance beyond that of the classical model.

Moreover, unlike previous studies that design networks for specific task demands, the proposed network model can dynamically adapt to varying task demands by optimizing the chunking gating policy through RL.

The implementation of a dopaminergic reinforcement learning protocol, as opposed to a hard-wired design, leads to the emergence of strategic gating mechanisms that enhance the network's computational flexibility and adaptability. These gating strategies are vital for VWM tasks and are developed in a manner consistent with ecological and evolutionary learning held by human. Further examination of how reward prediction error signals, both positive and negative, collaborate to refine gating strategies reveals the crucial role of reward feedback in fine-tuning the working memory computations and the model's behavior, aligning with the current neuroscientific understanding that reward matters.

Assessing the impact of a healthy balance of dopaminergic RPE signals on information manipulation holds implications for patients with altered striatal dopaminergic signaling.

Comments on revisions:

In the revised version, the authors have thoroughly addressed all the questions raised in my previous review. They have clarified the model architecture, provided detailed explanations of the training process, and elaborated on the convergence of the optimization.

Additionally, Reviewer 2 made a very constructive suggestion: Can related cognitive functions or phenomena emerge from the model? The newly added analysis and results highlighting the recency effect directly address this question and significantly strengthen the paper.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97894.3.sa2](https://doi.org/10.7554/eLife.97894.3.sa2)

Summary:

This paper utilizes a neural network model to investigate how the brain employs an adaptive chunking strategy to effectively enhance working memory capacity, which is a classical and significant question in cognitive neuroscience. By integrating perspectives from both the 'slot model' and 'limited resource models,' the authors adopted a neural network model encompassing the prefrontal cortex and basal ganglia, introduced an adaptive chunking strategy, and proposed a novel hybrid model. The study demonstrates that the brain can adaptively bind various visual stimuli into a single chunk based on the similarity of color features (a continuous variable) among items in visual working memory, thereby improving working memory efficiency. Additionally, it suggests that the limited capacity of working memory arises from the computational characteristics of the neural system, rather than anatomical constraints.

Strengths:

The neural network model utilized in this paper effectively integrates perspectives from both slot models and resource models (i.e., resource-like constraints within a slot-like system). This methodological innovation provides a better explanation for the limited capacity of working memory. By simulating the neural networks of the prefrontal cortex and basal ganglia, the model demonstrates how to optimize working memory storage and retrieval strategies through reinforcement learning (i.e., the efficient management of access to and from working memory). This biological simulation offers a novel perspective on human working memory and provides new explanations for the working memory difficulties observed in patients with Parkinson's disease and other disorders. Furthermore, the effectiveness of the model has been validated through computational simulation experiments, yielding reliable and robust predictions.

Comments on revisions:

The authors have already answered all my questions.
