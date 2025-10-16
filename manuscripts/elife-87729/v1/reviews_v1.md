# Peer review - Round 1

Editors:
- Huan Luo, Peking University China

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.87729.3.sa0](https://doi.org/10.7554/eLife.87729.3.sa0)

This study presents a valuable finding on developing a state-of-the-art generative model of brain electrophysiological signals to explain temporal decoding matrices widely used in cognitive neuroscience. The evidence supporting the authors' claims is convincing. The results will be strengthened by providing more clear mappings between neurobiological mechanisms and signal generators in the model. The work will be of interest to cognitive neuroscientists using electrophysiological recordings.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87729.3.sa1](https://doi.org/10.7554/eLife.87729.3.sa1)

With genephys, the author provides a generative model of brain responses to stimulation. This generative model allows to mimic specific parameters of a brain response at the sensor level, to test the impact of those parameters on critical analytic methods utilized on real M/EEG data. Specifically, they compare the decoding output for differently set parameters to the decoding pattern observed in a classical passive viewing study in terms of the resulting temporal generalization matrix (TGM). They identify that the correspondence between the mimicked and the experimental TGM to depend on an oscillatory component that spans multiple channels, frequencies, and latencies of response; and an additive, slower response with a specific (cross-frequency) relation to the phase of the oscillatory, faster component.

A strength of the article is that it considers the complexity of neural data that contribute to the findings obtained in stimulation experiments. An additional strength is the provision of a Python package that allows scientists to explore the potential contribution of different aspects of neural signals to obtained experimental data and thereby to potentially test their theoretical assumptions critical parameters that contribute to their experimental data.

A weakness of the paper is that the power of the model is illustrated for only one specific set of parameters, added in a stepwise manner and the comparison to on specific empirical TGM, assumed to be prototypical; And that this comparison remains descriptive. (That is could a different selection of parameters lead to similar results and is there TGM data which matches these settings less well.) It further remained unclear to me, which implications may be drawn from the generative model, following from the capacities to mimic this specific TGM (i) for more complex cases, such as the comparison between experimental conditions, and (ii) about the complex nature of neural processes involved.

Towards this end I would appreciate (i) a more profound explanation of the conclusions that can be drawn from this specific showcase, including potential limitations, as well as wider considerations of how scientists may empower the generative model to (ii) understand their experimental data better and (iii) which added value the model may have in understanding the nature of underlaying brain mechanism (rather than a mere technical characterization of sensor data).


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87729.3.sa2](https://doi.org/10.7554/eLife.87729.3.sa2)

This paper introduces a new model that aims to explain the generators of temporal decoding matrices (TGMs) in terms of underlying signal properties. This is important because TGMs are regularly used to investigate neural mechanisms underlying cognitive processes, but their interpretation in terms of underlying signals often remains unclear. Furthermore, neural signals are often variant over different instances of stimulation despite behaviour being relatively stable. The author aims to tackle these concerns by developing a generative model of electrophysiological data and then showing how different parameterizations can explain different features of TGMs. The developed technique is able to capture empirical observations in terms of fundamental signal properties. Specifically, the model shows that complexity is necessary in terms of spatial configuration, frequencies and latencies to obtain a TGM that is comparable to empirical data.

The major strength of the paper is that the novel technique has the potential to further our understanding of the generators of electrophysiological signals which are an important way to understand brain function. The paper clearly outlines how the method can be used to capture empirical data. Furthermore, the used techniques are state-of-the-art and the developed model is publicly shared in open source code.

On the other hand, there is no unambiguous mapping between neurobiological mechanisms and different signal generators, making it hard to draw firm conclusions about neural underpinnings based on this analysis.
