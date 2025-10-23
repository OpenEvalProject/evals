# Peer review - Round 1

Editors:
- Andrea E Martin, Max Planck Institute for Psycholinguistics Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.96217.3.sa0](https://doi.org/10.7554/eLife.96217.3.sa0)

van Vliet and colleagues show a useful correlation between internal states of a convolutional neural network (CNN) trained on visual word stimuli with three specific components of evoked MEG potentials during reading in humans. The findings are solid, though quantitative evidence that model can produce any of the phenomena that the human visual system is known to have (e.g., feedback connections, sensitivity to word frequency), or that it has comparable performance to human behaviour (i.e., similar task accuracy with a comparable pattern of mistakes) would make the conclusions much stronger.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.96217.3.sa1](https://doi.org/10.7554/eLife.96217.3.sa1)

van Vliet and colleagues present results of a study correlating internal states of a convolutional neural network trained on visual word stimuli with evoked MEG potentials during reading.

In this study, a standard deep learning image recognition model (VGG-11) trained on a large natural image set (ImageNet) that begins illiterate but is then further trained on visual word stimuli, is used on a set of predefined stimulus images to extract strings of characters from "noisy" words, pseudowords and real words. This methodology is used in hopes of creating a model which learns to apply the same nonlinear transforms that could be happening in different regions of the brain - which would be validated by studying the correlations between the weights of this model and neural responses. Specifically, the aim is that the model learns some vector embedding space, as quantified by the spread of activations across a layer's weights (L2 Norm prior to ReLu Activation Function), for the different kinds of stimuli, that creates a parameterized decision boundary that is similar to amplitude changes at different times for a MEG signal. More importantly, the way that the stimuli are ordered or ranked in that space should be separable to the degree we see separation in neural activity. This study does show that the layer weights corresponding to five different broad classes of stimuli do statistically correlate with three specific components in the ERP. However, I believe there are fundamental theoretical issues that limit the implications of the results of this study.

As has been shown over many decades, there are many potential computational algorithms, with varied model architectures, that can perform the task of text recognition from an image. However, there is no evidence presented here that this particular algorithm has comparable performance to human behavior (i.e. similar accuracy with a comparable pattern of mistakes). This is a fundamental prerequisite before attempting to meaningfully correlate these layer activations to human neural activations. Therefore, it is unlikely that correlating these derived layer weights to neural activity provides meaningful novel insights into neural computation beyond what is seen using traditional experimental methods.

One example of a substantial discrepancy between this model and neural activations is that, while incorporating frequency weighting into the training data is shown to slightly increase neural correlation with the model, Figure 7 shows that no layer of the model appears directly sensitive to word frequency. This is in stark contrast to the strong neural sensitivity to word frequency seen in EEG (e.g. Dambacher et al 2006 Brain Research), fMRI (e.g. Kronbichler et al 2004 NeuroImage), MEG (e.g. Huizeling et al 2021 Neurobio. Lang.), and intracranial (e.g. Woolnough et al 2022 J. Neurosci.) recordings. Figure 7 also demonstrates that late stages of the model show a strong negative correlation with font size, whereas later stages of neural visual word processing are typically insensitive to differences in visual features, instead showing sensitivity to lexical factors.

Another example of the mismatch between this model and visual cortex is the lack of feedback connections in the model. Within visual cortex there are extensive feedback connections, with later processing stages providing recursive feedback to earlier stages. This is especially evident in reading, where feedback from lexical level processes feeds back to letter level processes (e.g. Heilbron et al 2020 Nature Comms.). This feedback is especially relevant for reading of words in noisy conditions, as tested in the current manuscript, as lexical knowledge enhances letter representation in visual cortex (the word superiority effect). This results in neural activity in multiple cortical areas varying over time, changing selectivity within a region at different measured time points (e.g. Woolnough et al 2021 Nature Human Behav.), which in the current study is simplified down to three discrete time windows, each attributed to different spatial locations.

The presented model needs substantial further development to be able to replicate, both behaviorally and neurally, many of the well-characterized phenomena seen in human behavior and neural recordings that are fundamental hallmarks of human visual word processing. Until that point it is unclear what novel contributions can be gleaned from correlating low dimensional model weights from these computational models with human neural data.

The revised version of this manuscript has not addressed these concerns.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.96217.3.sa2](https://doi.org/10.7554/eLife.96217.3.sa2)

Summary:

The authors investigate the extent to which the responses of different layers of a vision model (VGG-11) can be linked to the cascade of responses (namely, type-I, type-II and N400) in the human brain when reading words. To achieve maximal consistency between, they add noisy-activations to VGG and finetune it on a character recognition task. In this setup, they observe various similarities between the behavior of VGG and the brain when presented with various transformations of the words (added noise, font modification etc).

Strengths:

- The paper is well written and well presented

- The topic studied is interesting.

- The fact that the response of the CNN on unseen experimental contrasts such as adding noise correlated with previous results on the brain is compelling.

Weaknesses:

- The paper is rather qualitative in nature. In particular, the authors show that some resemblance exists between the behavior of some layers and some parts of the brain, but it is hard to quantitively understand how strong the resemblences are in each layer, and the exact impact of experimental settings such as the frequency balancing (which seems to only have a very moderate effect according to figure 5)

- The experiments only consider a rather outdated vision model (VGG)

Comments on revisions:

After rebuttal, the authors significantly strengthened their results. I now find the paper much more convincing, and thank the author for their careful consideration of the reviewers' suggestions.
