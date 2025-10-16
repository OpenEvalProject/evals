# Learning cortical representations through perturbed and adversarial dreaming

## Authors

- Nicolas Deperrois<sup>1</sup> ([ORCID: 0000-0001-7178-1818](https://orcid.org/0000-0001-7178-1818)) †
- Mihai A Petrovici<sup>1</sup> ([ORCID: 0000-0003-2632-0427](https://orcid.org/0000-0003-2632-0427))
- Walter Senn<sup>1</sup> ([ORCID: 0000-0003-3622-0497](https://orcid.org/0000-0003-3622-0497))
- Jakob Jordan<sup>1</sup> ([ORCID: 0000-0003-3438-5001](https://orcid.org/0000-0003-3438-5001))

### Affiliations

1. Department of Physiology University of Bern Bern Switzerland

† Corresponding author

## Abstract

Humans and other animals learn to extract general concepts from sensory experience without extensive teaching. This ability is thought to be facilitated by offline states like sleep where previous experiences are systemically replayed. However, the characteristic creative nature of dreams suggests that learning semantic representations may go beyond merely replaying previous experiences. We support this hypothesis by implementing a cortical architecture inspired by generative adversarial networks (GANs). Learning in our model is organized across three different global brain states mimicking wakefulness, NREM and REM sleep, optimizing different, but complementary objective functions. We train the model on standard datasets of natural images and evaluate the quality of the learned representations. Our results suggest that generating new, virtual sensory inputs via adversarial dreaming during REM sleep is essential for extracting semantic concepts, while replaying episodic memories via perturbed dreaming during NREM sleep improves the robustness of latent representations. The model provides a new computational perspective on sleep states, memory replay and dreams and suggests a cortical implementation of GANs.
