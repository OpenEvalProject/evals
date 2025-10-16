# Peer review - Round 1

Editors:
- Sandeep Krishna, National Centre for Biological Sciences­‐Tata Institute of Fundamental Research India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.97754.3.sa0](https://doi.org/10.7554/eLife.97754.3.sa0)

This study presents a light-entrainable synthetic oscillator in bacteria, the optorepressilator. The authors develop a toolbox using optogenetics that makes the cellular oscillator easily controllable. This toolbox is valuable, contributing both to bioengineering and to the understanding of biological dynamical systems. The comparison with a mathematical model, population, and single-cell measurements demonstrate convincingly that the planned system was achieved and is suitable to control and study biological oscillators.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97754.3.sa1](https://doi.org/10.7554/eLife.97754.3.sa1)

Summary:

The "optorepressilator", an optically controllable genetic oscillator based on the famous E. coli 3-repressor (LacI, TetR, CI) oscillator "repressilator", was developed. An individual repressilator shows a stable oscillation of the protein levels with a relatively long period that extends a few doubling times of E. coli, but when many cells oscillate, their phases tend to desynchronize. The authors introduced an additional optically controllable promoter through a conformal change of CcaS protein and let it control how much additional CI is produced. By tightly controlling the leak from the added promoter, the authors successfully kept the original repressilator oscillation when the added promoter was not activated. In contrast, the oscillation was stopped by expressing the additional CI. Using this system, the authors showed that it is possible to synchronise the phase of the oscillation, especially when the activation happens as a short pulse at the right phase of the repressilator oscillation. The authors further show that, by changing the frequency of the short pulses, the repressilator was entrained to various ratios to the pulse period, and the author could reconstruct the so-called "Arnold tongues", the signature of entrainment of the nonlinear oscillator to externally added periodic perturbation. The behaviour is consistent with the simplified mathematical model that simulates the protein concentration using ordinary differential equations.

Strengths:

Optical control of the oscillation of the protein clock is a powerful and clean tool for studying the synthetic oscillator's response to perturbation in a well-controlled and tunable manner. The article utilizes the plate reader setup for population average measurements and the mother machine setup for single-cell measurements, and they complement nicely to acquire necessary information.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97754.3.sa2](https://doi.org/10.7554/eLife.97754.3.sa2)

Summary:

In this manuscript by Cannarsa et. al., the authors describe the engineering of a light-entrainable synthetic biological oscillator in bacteria. It is based on an upgraded version of one of the first synthetic circuits to be constructed, the repressilator. The authors sought to make this oscillator entrainable by an external forcing signal, analogous to the way natural biological oscillators (like the circadian clock) are synchronized. They reasoned that an optogenetic system would provide a convenient and flexible means of manipulation. To this end, the authors exploited the CcaS-CcaA light-switchable system, which allows activation and deactivation of transcription by green and red light, respectively. They used this system to make the expression of one of the repressilator's transcription factors (lacI) light-controlled, from a construct separated from the main repressilator plasmid. This way, under red light the oscillator runs freely, but exposure to green light causes overexpression of the lacI, pushing the system into a specific state. Consequently, returning to red light will restore the oscillations from the same phase in all cells, effectively synchronizing the cell population.

After demonstrating the functionality of the basic concept, the authors combined modeling and experiments to show how periodic exposure to green light enables efficient entrainment, and how the frequency of the forcing signal affects the oscillatory behavior (detuning).

This work provides an important demonstration of engineering tunability into a foundational genetic circuit, expands the synthetic biology toolbox, and provides a platform to address critical questions about synchronization in biological oscillators. Due to the flexibility of the experimental system, it is also expected to provide a fertile ground for future testing of theoretical predictions regarding non-linear oscillators.

Strengths:

* The study provides a simple and elegant mechanism for the entertainment of a synthetic oscillator. The design relies on optogenetic proteins, which enable efficient experimentation compared to alternative approaches (like using chemical inducers). This way, a static culture (without microfluidics or change of growth media) can be easily exposed to flexible temporal sequences of the zeitgeber, and continuously measured through time.

* The study makes use of both plate-reader-based population-level readout and mother-machine single-cell measurements. Synchronization through entrainment is a single cell level phenomenon, but with a clear population-level manifestation. Thus, this experimental approach combination provides a strong validation to their system. At the same time, differences between the readout from the two systems have emerged, and provided a further opportunity for model refinement and testing.

* The authors correctly identified the main optimization goal, namely the effective leakiness of their construct even under red light. Then, they successfully overcame this issue using synthetic biology approaches.

* The work is supported by a simplified model of the repressilator, which provides a convenient analytical and numerical means to draw testable predictions. The model predictions are well aligned with the experimental evidence.

Weaknesses:

* Even after optimizing the expression level of the light-sensitive gene, the system is very sensitive, i.e., a very short exposure is sufficient to elicit the strongest entertainment. This limited dynamic range might hamper some model testing and future usage.

* As a result of the previous point, the system is entrained by transiently "breaking" the oscillator: each pulse of green light represents a Hopf bifurcation into a single attractor. it means that the system cannot oscillate in constant green light. In comparison, this is generally not the case for natural zeitgebers like light and temperature for the circadian rhythms. Extreme values might prevent oscillations (not necessarily due to breaking the core oscillator), but usually, free running is possible in a wide range of constant conditions. In some cases, the free-running period length will vary as a function of the constant value.

While the approach presented in this manuscript is valid, a comprehensive analysis of more subtle modes of repressilator entrainment could also be of value.

* The entire work makes use of a single intensity and single duration of the green pulse to force entrainment. While the model has clear predictions for how different modalities should affect entrainment, more experiments are needed to validate those predictions.
