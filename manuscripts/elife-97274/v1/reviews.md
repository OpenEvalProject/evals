# Peer review - Round 1

Editors:
- Jun Ding, Stanford University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.97274.4.sa0](https://doi.org/10.7554/eLife.97274.4.sa0)

This computational modeling study builds on multiple previous lines of experimental and theoretical research to investigate how a single neuron can solve a nonlinear pattern classification task. The revised manuscript presents convincing evidence that the location of synapses on dendritic branches, as well as synaptic plasticity of excitatory and inhibitory synapses, influences the ability of a neuron to discriminate combinations of sensory stimuli. The ideas in this work are very interesting, presenting an important direction in the computational neuroscience field about how to harness the computational power of "active dendrites" for solving learning tasks.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97274.4.sa1](https://doi.org/10.7554/eLife.97274.4.sa1)

Summary:

This computational modeling study builds on multiple previous lines of experimental and theoretical research to investigate how a single neuron can solve a nonlinear pattern classification task. The authors construct a detailed biophysical and morphological model of a single striatal medium spiny neuron, and endow excitatory and inhibitory synapses with dynamic synaptic plasticity mechanisms that are sensitive to (1) the presence or absence of a dopamine reward signal, and (2) spatiotemporal coincidence of synaptic activity in single dendritic branches. The latter coincidence is detected by voltage-dependent NMDA-type glutamate receptors, which can generate a type of dendritic spike referred to as a "plateau potential." In the absence of inhibitory plasticity, the proposed mechanisms result in good performance on a nonlinear classification task when specific input features are segregated and clustered onto individual branches, but reduced performance when input features are randomly distributed across branches. Interestingly, adding inhibitory plasticity improves classification performance even when input features are randomly distributed.

Strengths:

The integrative aspect of this study is its major strength. It is challenging to relate low-level details such as electrical spine compartmentalization, extrasynaptic neurotransmitter concentrations, dendritic nonlinearities, spatial clustering of correlated inputs, and plasticity of excitatory and inhibitory synapses to high-level computations such as nonlinear feature classification. Due to high simulation costs, it is rare to see highly biophysical and morphological models used for learning studies that require repeated stimulus presentations over the course of a training procedure. The study aspires to prove the principle that experimentally-supported biological mechanisms can explain complex learning.

Weaknesses:

The high level of complexity of each component of the model makes it difficult to gain an intuition for which aspects of the model are essential for its performance, or responsible for its poor performance under certain conditions. Stripping down some of the biophysical detail and comparing it to a simpler model may help better understand each component in isolation.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97274.4.sa2](https://doi.org/10.7554/eLife.97274.4.sa2)

Summary:

The study explores how single striatal projection neurons (SPNs) utilize dendritic nonlinearities to solve complex integration tasks. It introduces a calcium-based synaptic learning rule that incorporates local calcium dynamics and dopaminergic signals, along with metaplasticity to ensure stability for synaptic weights. Results show SPNs can solve the nonlinear feature binding problem and enhance computational efficiency through inhibitory plasticity in dendrites, emphasizing the significant computational potential of individual neurons. In summary, the study provides a more biologically plausible solution to single-neuron learning and gives further mechanical insights into complex computations at the single-neuron level.

Strengths:

The paper introduces a novel learning rule for training a single multicompartmental neuron model to perform nonlinear feature binding tasks (NFBP), highlighting two main strengths: the learning rule is local, calcium-based, and requires only sparse reward signals, making it highly biologically plausible, and it applies to detailed neuron models that effectively preserve dendritic nonlinearities, contrasting with many previous studies that use simplified models.
