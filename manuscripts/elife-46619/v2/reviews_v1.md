# Peer review - Round 1

Editors:
- Thomas Yeo, National University of Singapore Singapore

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.46619.sa1](https://doi.org/10.7554/eLife.46619.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The authors provide evidence that humans possess a constellation of brain regions involved in encoding the mass of viewed objects (which they refer to as physical inference), and show that this encoding of mass generalizes across objects and various material and physical properties. The reviewers and editors felt that the study was interesting and novel. The experiments and analyses appear to be expertly conducted, and the authors provide considerable evidence in support of their claims. Of the few studies that have investigated the neural coding of object properties such as mass and other physical object properties, few if any have demonstrated that physical inferences of this nature arise in tasks that do not require actions. Therefore, we believe this work will be of great interest to the scientific community.

Decision letter after peer review:

Thank you for submitting your article "Invariant representations of mass in the human brain" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Michael Frank as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Jacqueline Snow (Reviewer #2); Jason Gallivan (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors provide evidence that humans possess a constellation of brain regions involved in encoding the mass of viewed objects (which they refer to as physical inference), and show that this encoding of mass generalizes across objects and various material and physical properties. The reviewers and editors felt that the study was interesting and novel. That said, there are significant concerns about several technical and interpretation issues that need to be addressed before the paper can be published. The following comments highlight the "essential revisions" (which the authors must address in the revised manuscript and response letter).

Essential revisions:

1) In general, the description of the decoding analyses did not contain sufficient details for the study to be replicated. The following points should be clarified in the revised manuscript.

A) What cross-validation procedure was used for the analyses: leave-one-run-out or something else? One gets the sense that trial types were reserved for classifier testing, but that these trials would have also appeared in the same experimental run as the testing trials (e.g., In the Experiment 1 decoding). This could inflate the decoding results.

B) It was also not fully clear how decoding was setup for Experiment 1, and how trials were grouped for leave-one-trial-out classification analysis. Were trials labelled as heavy vs. light in the splash and blow conditions and then tested on pillow trials? This should be clarified.

C) Also, in the Materials and methods, the authors mention that beta values were used on trials 'classified' as… – do you mean based on the subject's behavioral responses or the actual trial identity? For example, in Experiment 1 (and other experiments), what were the regressors used? Was the whole 3 seconds modeled as a box? What about the 1s response period? Was reaction time, etc taken into account? Which betas were then used for classification? Was beta estimated for each trial, so classification was done per trial (that would make sense, but just clarifying). We assume a canonical HRF response was assumed? What HRF parameters? Since this is event related design, the hemodynamic response might leak across trials, which might inflate accuracies (e.g., two adjacent trials might be in the training and test sets respectively resulting in information leak). How was this handled in the decoding?

D) We are not sure what's the dimensionality of the input to the SVM. Were the input beta coefficients from all voxels (which would be thousands of voxels) or was it an 11-dimensional vector, corresponding to the beta coefficients of the 11 functional ROIs? If the latter, was the GLM performed for average time courses within each of 11 ROIs? Or GLM was performed for all vertices and then the betas were averaged within each ROI?

E) What regularization parameter was used for the SVM? How was this hyperparameter selected?

F) In Experiment 3, it was unclear when exactly (in time) authors were decoding mass from the videos (was an HRF aligned to the onset of the video?), and was this conflated at all with the requirement that subjects respond as quickly as possible during the video whether the object will cross the line? Also, how did subjects report this?

G) Please provide more details on how LO/pF/OTC texture areas were defined.

2) Why not perform the analysis in each functional ROI separately? This would provide greater specificity about the effects and allow specific claims to be made about regions rather than a massive frontoparietaltemporal network. On that note, to demonstrate the specificity of the effects, we would also like to see a whole-brain searchlight decoding analysis. This would also allow some greater specificity of where in the brain they see effects of the color task (presumably V4), or where in the brain they see effects of object material (e.g., aluminum vs. cork, more on this below). The inclusion of a searchlight analysis would significantly bolster observations.

3) Based on the Experiment 2 design, we are not sure you can make any claims about the automaticity of mass encoding. The study interspersed color and mass blocks, and it is difficult to rule out that the context effect on mass blocks carried over to (and created biases on) color blocks. Moreover, we think it would have strengthened their observations to show that a classifier trained on mass blocks can cross-decode mass on color blocks, rather than just decode mass from the color blocks independently (as was done).

4) The authors said that "A power analysis was used to calculate the appropriate number of subjects for each experiment." We assumed this meant that the authors determine a sample size of 20 was necessary for Experiment 3. Why then did the authors examine mass decoding in the LO/pF/OTC texture areas in only 6 subjects? A fair comparison, to demonstrate equivalent power, would be to demonstrate that object material (e.g., aluminum vs. cork) can be decoded using the same regions (LO/pF/OTC).

5) Eye Movement Control analysis. This analysis was completely unclear. How are the different measures computed, what time windows were used for analysis (specific events in a trial?), how were the trials collapsed for analysis? No details were provided making it difficult to interpret the authors' claims.

6) "A pattern recognition approach to physical reasoning might predict that the neural representations in these regions would hold information about low-level visual features or situation-specific representations of physical variables. In contrast, if these regions support a generalized engine for physical simulation, we would expect to find that they hold representations of abstract physical dimensions that generalize across scenario and other physical dimensions." – We are a bit unconvinced about the logic. Isn't it possible for a pattern recognition technique to implicitly encode these abstract physical dimensions, which are then detected by your decoding approach? For example, suppose we train a reinforcement learning (RL) algorithm in a virtual environment to perform certain tasks. Isn't it possible that physical dimensions are implicitly encoded by the RL algorithm even though the RL algorithm does not utilize an explicit physical generative model? In fact, one might argue that the use of MVPA (linear SVM) in Experiment 1 suggests that the physical representation is implicit, so the authors might simply be decoding the pattern recognition approach's implicit representation of mass (or some other physical attribute) in the brain?

7) I understand that the authors relied on a network of brain areas that had been identified in a previous study by Fischer et al., 2016, which were shown to be engaged in a physical reasoning paradigm. It does seem, however, from the description of the localizer task, that the contrast of falling direction (i.e., the 'physics' task) vs. color task, would identify a number of different brain areas, not all of which would have similar functions. As one example, intuitively, it seems that the physics task that involved estimating where the leaning tower of blocks would fall would preferentially activate motion-selective areas (i.e., hV5/MT+) – which have been shown in previous fMRI studies to be activated when observers anticipate motion. The group maps illustrated in Figure 3A do indeed suggest an involvement of such motion-selective cortex, especially in the RH. As such, I wondered how meaningful the results are given that there is such a broad network of areas that is being sampled in the analyses. Is the claim that the network as a whole is operating as a 'physics engine', or are more localized regions within the network accounting for this function more so than others? It is also possible that different regions within the network may be more or less likely to show invariance – for example in real-world scenarios when, presumably, more specific rather than invariant representations would be beneficial to support possible actions? Perhaps identifying the areas that were part of this 'network' (either in the figure or a new table) would help readers to make their own assessment.
