# Peer review - Round 1

Editors:
- Julijana Gjorgjieva, Technical University of Munich Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.90793.3.sa0](https://doi.org/10.7554/eLife.90793.3.sa0)

This fundamental work proposes a novel mechanism for memory consolidation where short-term memory provides a gating signal for memories to be consolidated into long-term storage. The work combines extensive analytical and numerical work applied to three different scenarios and provides a convincing analysis of the benefits of the proposed model, although some of the analyses are limited to the type of memory consolidation the authors consider (and don't consider), which limits the impact. The work will be of interest to neuroscientists and many other researchers interested in the mechanistic underpinnings of memory.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90793.3.sa1](https://doi.org/10.7554/eLife.90793.3.sa1)

Summary:

In the manuscript the authors suggest a computational mechanism called recall-gated consolidation, which prioritizes the storage of previously experienced synaptic updates in memory. The authors investigate the mechanism with different types of learning problems including supervised learning, reinforcement learning, and unsupervised auto-associative memory. They rigorously analyse the general mechanism and provide valuable insights into its benefits.

Strengths:

The authors establish a general theoretical framework, which they translate into three concrete learning problems. For each, they define an individual mathematical formulation. Finally, they extensively analyse the suggested mechanism in terms of memory recall, consolidation dynamics, and learnable timescales.

The presented model of recall-gated consolidation covers various aspects of synaptic plasticity, memory recall, and the influence of gating functions on memory storage and retrieval. The model's predictions align with observed spaced learning effects.

The authors conduct simulations to validate the recall-gated consolidation model's predictions, and their simulated results align with theoretical predictions. These simulations demonstrate the model's advantages over consolidating any memory and showcase its potential application to various learning tasks.

The suggestion of a novel consolidation mechanism provides a good starting point to investigate memory consolidation in diverse neural systems and may inspire artificial learning algorithms.

Weaknesses:

I appreciate that the authors devoted a specific section to the model's predictions, and point out how the model connects to experimental findings in various model organisms. However, the connection is rather weak and the model needs to make more specific predictions to be distinguishable from other theories of memory consolidation (e.g. those that the authors discuss) and verifiable by experimental data.

The model is not compared to other consolidation models in terms of performance and how much it increases the signal-to-noise ratio. It is only compared to a simple STM or a parallel LTM, which I understand to be essentially the same as the STM but with a different timescale (so not really an alternative consolidation model). It would be nice to compare the model to an actual or more sophisticated existing consolidation model to allow for a fairer comparison.

The article is lengthy and dense and it could be clearer. Some sections are highly technical and may be challenging to follow. It could benefit from more concise summaries and visual aids to help convey key points.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.90793.3.sa2](https://doi.org/10.7554/eLife.90793.3.sa2)

Summary:

In their article Jack Lindsey and Ashok Litwin-Kumar describe a new model for systems memory consolidation. Their idea is that a short-term memory acts not as a teacher for a long-term memory - as is common in most complementary learning systems -, but as a selection module that determines which memories are eligible for long term storage. The criterion for the consolidation of a given memory is a sufficient strength of recall in the short term memory.

The authors provide an in-depth analysis of the suggested mechanism. They demonstrate that it allows substantially higher SNRs than previous synaptic consolidation models, provide an extensive mathematical treatment of the suggested mechanism, show that the required recall strength can be computed in a biologically plausible way for three different learning paradigms, and illustrate how the mechanism can explain spaced training effects.

Strengths:

The suggested consolidation mechanism is novel and provides a very interesting alternative to the classical view of complementary learning systems. The analysis is thorough and convincing.

Weaknesses:

The main weakness of the paper is the equation of recall strength with the synaptic changes brought about by the presentation of a stimulus. In most models of learning, synaptic changes are driven by an error signal and hence cease once the task has been learned. The suggested consolidation mechanism would stop at that point, although recall is still fine. The authors should discuss other notions of recall strength that would allow memory consolidation to continue after the initial learning phase. Aside from that, I have only a few technical comments that I'm sure the authors can address with a reasonable amount of work.
