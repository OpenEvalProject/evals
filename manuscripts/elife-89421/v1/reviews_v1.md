# Peer review - Round 1

Editors:
- Mackenzie W Mathis, École Polytechnique Fédérale de Lausanne Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.89421.3.sa0](https://doi.org/10.7554/eLife.89421.3.sa0)

This paper presents a new method called MINT that is effective at BCI-style decoding tasks. The authors show convincing evidence to support their claims regarding how MINT is a new method that produces excellent decoding performance relative to the state-of-the-art. This work is important and will be of broad interest to neuroscientists and neuroengineers.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.89421.3.sa1](https://doi.org/10.7554/eLife.89421.3.sa1)

Summary:

This paper presents an innovative decoding approach for brain-computer interfaces (BCIs), introducing a new method named MINT. The authors develop a trajectory-centric approach to decode behaviors across several different datasets, including eight empirical datasets from the Neural Latents Benchmark. Overall, the paper is well written and their method shows impressive performance compared to more traditional decoding approaches that use a simpler approach. While there are some concerns (see below), the paper's strengths, particularly its emphasis on a trajectory-centric approach and the simplicity of MINT, provide a compelling contribution to the field.

Strengths:

The adoption of a trajectory-centric approach that utilizes statistical constraints presents a substantial shift in methodology, potentially revolutionizing the way BCIs interpret and predict neural behaviour. This is one of the strongest aspects of the paper.

The thorough evaluation of the method across various datasets serves as an assurance that the superior performance of MINT is not a result of overfitting. The comparative simplicity of the method in contrast to many neural network approaches is refreshing and should facilitate broader applicability.

Weaknesses:

Scope: Despite the impressive performance of MINT across multiple datasets, it seems predominantly applicable to M1/S1 data. Only one of the eight empirical datasets comes from an area outside the motor/somatosensory cortex. It would be beneficial if the authors could expand further on how the method might perform with other brain regions that do not exhibit low tangling or do not have a clear trial structure (e.g. decoding of position or head direction from hippocampus)

When comparing methods, the neural trajectories of MINT are based on averaged trials, while the comparison methods are trained on single trials. An additional analysis might help in disentangling the effect of the trial averaging. For this, the authors could average the input across trials for all decoders, establishing a baseline for averaged trials. Note that inference should still be done on single trials. Performance can then be visualized across different values of N, which denotes the number of averaged trials used for training.

Comments on revisions:

I have looked at the responses and they are thorough and answer all of my questions.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.89421.3.sa2](https://doi.org/10.7554/eLife.89421.3.sa2)

Summary:

The goal of this paper is to present a new method, termed MINT, for decoding behavioral states from neural spiking data. MINT is a statistical method which, in addition to outputting a decoded behavioral state, also provides soft information regarding the likelihood of that behavioral state based on the neural data. The innovation in this approach is neural states are assumed to come from sparsely distributed neural trajectories with low tangling, meaning that neural trajectories (time sequences of neural states) are sparse in the high-dimensional space of neural spiking activity and that two dissimilar neural trajectories tend to correspond to dissimilar behavioral trajectories. The authors support these assumptions through analysis of previously collected data, and then validate the performance of their method by comparing it to a suite of alternative approaches. The authors attribute the typically improved decoding performance by MINT to its assumptions being more faithfully aligned to the properties of neural spiking data relative to assumptions made by the alternatives.

Strengths:

The paper did an excellent job critically evaluating common assumptions made by neural analytical methods, such as neural state being low-dimensional relative to the number of recorded neurons. The authors made strong arguments, supported by evidence and literature, for potentially high-dimensional neural states and thus the need for approaches that do not rely on an assumption of low dimensionality.

The paper was thorough in considering multiple datasets across a variety of behaviors, as well as existing decoding methods, to benchmark the MINT approach. This provided a valuable comparison to validate the method. The authors also provided nice intuition regarding why MINT may offer performance improvement in some cases and in which instances MINT may not perform as well.

In addition to providing a philosophical discussion as to the advantages of MINT and benchmarking against alternatives, the authors also provided a detailed description of practical considerations. This included training time, amount of training data, robustness to data loss or changes in the data, and interpretability. These considerations not only provided objective evaluation of practical aspects but also provided insights to the flexibility and robustness of the method as they relate back to the underlying assumptions and construction of the approach.

Impact:

This work is motivated by brain-computer interfaces applications, which it will surely impact in terms of neural decoder design. However, this work is also broadly impactful for neuroscientific analysis to relate neural spiking activity to observable behavioral features. Thus, MINT will likely impact neuroscience research generally. The methods are made publicly available, and the datasets used are all in public repositories, which facilitates adoption and validation of this method within the greater scientific community.
