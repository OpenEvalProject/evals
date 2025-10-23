# Peer review - Round 1

Editors:
- SP Arun, Indian Institute of Science Bangalore India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.87719.3.sa0](https://doi.org/10.7554/eLife.87719.3.sa0)

Schnell et al. report important differences between the strategies used by rodents and humans when discriminating different visual objects. The evidence supporting these findings is convincing, showing that rat performance was influenced far more by low-level cues compared to humans. It is, however, unclear to what extent these differences can be explained by the lower visual acuity of rats. This work will be of general interest to vision and cognition researchers, particularly those studying object vision.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87719.3.sa1](https://doi.org/10.7554/eLife.87719.3.sa1)

Schnell et al. performed two extensive behavioral experiments concerning the processing of objects in rats and humans. To this aim, they designed a set of objects parametrically varying along alignment and concavity and then they used activations from a pretrained deep convolutional neural network to select stimuli that would require one of two different discrimination strategies, i.e. relying on either low- or high-level processing exclusively. The results show that rodents rely more on low-level processing than humans.

Strengths:

1. The results are challenging and call for a different interpretation of previous evidence. Indeed, this work shows that common assumptions about task complexity and visual processing are probably biased by our personal intuitions and are not equivalent in rodents, which instead tend to rely more on low-level properties.

2. This is an innovative (and assumption-free) approach that will prove useful to many visual neuroscientists. Personally, I second the authors' excitement about the proposed approach, and its potential to overcome the limits of experimenters' creativity and intuitions. In general, the claims seem well supported and the effects sufficiently clear.

3. This work provides an insightful link between rodent and human literature on object processing. Given the increasing number of studies on visual perception involving rodents, these kinds of comparisons are becoming crucial.

4. The paper raises several novel questions that will prompt more research in this direction.

Weaknesses:

1. The choice of alignment and concavity as baseline properties of the stimuli is not properly discussed.

2. From the low-correlations I got the feeling that AlexNet is not the best baseline model for rat visual processing.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87719.3.sa2](https://doi.org/10.7554/eLife.87719.3.sa2)

Schnell and colleagues trained rats on a two-alternative forced choice visual discrimination task. They used object pairs that differed in their concavity and the alignment of features. They found that rats could discriminate objects across various image transformations. Rat performance correlated best with late convolutional layers of an artificial neural network and was partially explained by factors of brightness and pixel-level similarity. In contrast, human performance showed the strongest correlation with higher, fully connected layers, indicating that rats employed simpler strategies to accomplish this task as compared to humans.

Strengths:

1. This is a methodologically rigorous study. The authors tested a substantial number of rats across a large variety of stimuli.

2. The innovative use of neural networks to generate stimuli with varying levels of complexity is a compelling approach that motivates principled experimental design.

3. The study provides important data points for cross-species comparisons of object discrimination behavior

4. The data strongly support the authors' conclusion that rats and humans rely on different visual features for discrimination tasks.

5. This is a valuable study that provides novel, important insights into the visual capabilities of rats.

Weaknesses:

1. The impact of rat visual acuity (~1cycle/degree) on the discriminability of stimuli could be more directly modeled and taken into consideration when comparing rat behavior to humans, who possess substantially higher acuity.

2. The distinction between low- and high-level visual behavior is coarse, and it remains uncertain which specific features rats utilized for discrimination. The correlations with brightness and pixel-level similarity do provide some insight.

3. The relatively weak correspondence between rat behavior and AlexNet raises the question of which network architecture, whether computational or biological, might better capture rat behavior, particularly to the level of cross-rat consistency.
