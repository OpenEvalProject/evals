# Peer review - Round 1

Editors:
- Peter Latham, University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.44516.sa1](https://doi.org/10.7554/eLife.44516.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

In the real world, the acoustic environment changes continuously -- background noise can be loud or quiet, and even at a particular volume the spectrum can change dramatically (both on relatively short timescales). This work addresses the question of how speech perception adapts to such changes. The authors propose a model that is successful in explaining empirical data, including very recent data describing perceptual adaptation at multiple time scales. This should make an important contribution to our understanding of multi-scale speech processing.

Decision letter after peer review:

Thank you for submitting your article "Integrating prediction errors at two time scales permits rapid recalibration of speech sound categories" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Timothy Behrens as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Olasagasti and Giraud constructed probabilistic models to study speech recalibration -- how speech perception adapts to changes in the acoustic environment of the perceiver. Unlike previous work, the current work addresses a volatile environment. The resulting model is successful in explaining empirical data, including very recent data describing perceptual adaptation at multiple time scales; in particular, an updating rule at two timescales outperformed models with an updating rule at a single scale. The work is important, the paper is well-written and the results will be of great value to the field of speech perception, and likely also to the field of perception in general.

Essential revisions:

1) The authors highlighted that updating rules at multiple timescales are beneficial, but it is probably the process implemented at each timescale that matters. I would like to ask the authors to further illustrate what is the nature of cognitive processes at each timescale, besides highlighting “two timescales”.

2) The sentence in the Abstract –“sound categories are represented at different time scales” – is not clear. Is it the information about sound category represented at different timescales? I would like the authors to clarify. The probabilistic models here represent a decision/inference process in my opinion, which is inconsistent with this claim. The frame-by-frame procedure of combining the visual/audio cues in the models are unrelated to the experimental evidence that humans can tolerate a large temporal lag between audio and visual cues of speech. I would like the authors to discuss the difference between the experimental evidence and their model procedures. If possible, could the authors jitter the lag between audio and visual cues to check the model performance. Could it be possible that the large timescale biased the model estimate in the beginning of each trial, even before perceptual information comes in. If possible, could the authors illustrate dynamics of the two- timescale model estimates as in Figure 2A.

3) The way in which the model is evaluated is not clear. Please be more specific about it – describe the relevant dataset, the evaluation of the model against the dataset and its comparison with other models in this respect.

4) Please elaborate on the principle of assigning different time scales to different levels in a hierarchical Bayesian inference framework; specifically, please describe how were specific time scales selected for specific Bayesian levels.

5) The advantages to speech perception are evident from this work, but the potential theoretical and computational consequences (difficulties, limitations and advantages) are not clear enough. Please devote a Discussion section to the broader aspect of evaluating time scales of adaptation.
