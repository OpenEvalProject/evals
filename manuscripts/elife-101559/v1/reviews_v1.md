# Peer review - Round 1

Editors:
- Jie Xiao, Johns Hopkins University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.101559.3.sa0](https://doi.org/10.7554/eLife.101559.3.sa0)

This study presents an important computational framework, FLiSimBA (Fluorescence Lifetime Simulation for Biological Applications), for modeling experimental limitations in Fluorescence Lifetime Imaging Microscopy (FLIM). FLiSimBA is readily available in MATLAB and Python, enables users to simulate effects of noise and varying sensor expression levels, and provides practical guidance for both lifetime imaging experiments and biosensor development. The analyses are robust, and the evidence supporting the tool's utility in distinguishing between multiple lifetime signals is compelling, indicating strong potential for multiplexed dynamic imaging. However, users should also consider that the tool's effectiveness depends on the suitability of a two-component discrete exponential model.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.101559.3.sa1](https://doi.org/10.7554/eLife.101559.3.sa1)

In this study, Ma et al. aimed to determine previously uncharacterized contributions of tissue autofluorescence, detector afterpulse, and background noise on fluorescence lifetime measurement interpretations. They introduce a computational framework they named "Fluorescence Lifetime Simulation for Biological Applications (FLiSimBA)" to model experimental limitations in Fluorescence Lifetime Imaging Microscopy (FLIM) and determine parameters for achieving multiplexed imaging of dynamic biosensors using lifetime and intensity. By quantitatively defining sensor photon effects on signal to noise in either fitting or averaging methods of determining lifetime, the authors contradict any claims of FLIM sensor expression insensitivity to fluorescence lifetime and highlight how these artifacts occur differently depending on analysis method. Finally, the authors quantify how statistically meaningful experiments using multiplexed imaging could be achieved.

A major strength of the study is the effort to present results in a clear and understandable way given that most researcher do not think about these factors on a day-to-day basis. Additionally, the model code is readily available in Matlab and Python, which should allow for open access to a larger community.

Overall, the authors' achieved their aims of demonstrating how common factors (autofluorescence, background, and sensor expression) will affect lifetime measurements and they present a clear strategy for understanding how sensor expression may confound results if not properly considered. This work should bring to awareness an issue that new users of lifetime biosensors may not be aware of and that experts, while aware, have not quantitatively determine the conditions where these issues arise. This work will also point to future directions for improving experiments using fluorescence lifetime biosensors and the development of new sensors with more favorable properties.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.101559.3.sa2](https://doi.org/10.7554/eLife.101559.3.sa2)

Summary:

This study presents a useful computational tool, termed FLiSimBA. The MATLAB-based FLiSimBA simulations allow users to examine the effects of various noise factors (such as autofluorescence, afterpulse of the photomultiplier tube detector, and other background signals) and varying sensor expression levels. Under the conditions explored, the simulations unveiled how these factors affect the observed lifetime measurements, thereby providing useful guidelines for experimental designs. Further simulations with two distinct fluorophores uncovered conditions in which two different lifetime signals could be distinguished, indicating multiplexed dynamic imaging may be possible.

Strengths:

The simulations and their analyses were done systematically and rigorously. FliSimba can be useful for guiding and validating fluorescence lifetime imaging studies. The simulations could define useful parameters such as the minimum number of photons required to detect a specific lifetime, how sensor protein expression level may affect the lifetime data, the conditions under which the lifetime would be insensitive to the sensor expression levels, and whether certain multiplexing could be feasible.

Weaknesses:

The analyses have relied on a key premise that the fluorescence lifetime in the system can be described as a two-component discrete exponential decay. This means that the experimenter should ensure that this is the right model for their fluorophores a priori.
