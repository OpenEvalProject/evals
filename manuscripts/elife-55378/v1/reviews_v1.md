# Peer review - Round 1

Editors:
- Tobias Reichenbach, Imperial College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55378.sa1](https://doi.org/10.7554/eLife.55378.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The mechanosensitive inner hair cells of the inner ear convey their electrical signals to the auditory nerve through synapses at their base. This article shows that important biophysical properties of the auditory-nerve fibres vary systematically with the spatial location of the synapses. It thereby casts light on the organisation of subgroups within the auditory-nerve fibres, and will aid a better understand of the coding of sound in the auditory nerve.

Decision letter after peer review:

Thank you for submitting your article "Loudness sensitivity in the spiral ganglion emerges from a maturational gradient in morphology and biophysics" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Tobias Reichenbach as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Barbara Shinn-Cunningham as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Elisabeth Glowatzki (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The study investigates how biophysical parameters of auditory-nerve fibers vary with the location of the corresponding synapses on the inner hair cells. The authors find that some of these parameters – such as conductances, voltage threshold for spiking and time constants – vary systematically with the spatial location of the synapses. Moreover, they show that a multiple linear regression model that takes these biophysical parameters into account can predict the spatial location to a significant extent. This work is very timely, as the current research in the field focusses on dissecting the underlying properties of auditory-nerve fibre subgroups, an important step in understanding how the sound signal is coded.

Essential revisions:

1) The title and Abstract appear partly misleading. First, the term "loudness sensitivity" in the title leads the reader to expect a direct investigation of the SGNs' dependency of spontaneous rate and threshold on the location. In addition, is "intensity sensitivity" the best descriptor? After all, high spontaneous afferents that respond to low intensity sound do respond to high intensity sound as well. Perhaps "intensity selectivity", "dynamic range" or even "intensity tuning" better captures the difference. Second, the finding of the maturational gradient takes major space in the title and manuscript. This ignores the probably more important finding regarding the pillar/modiolar differences that are found regardless of age. In particular, it is impressive that pillar/modiolar differences already exist at young postnatal ages, which may be worth highlighting. In addition, the authors might want to emphasize their important conclusion that the developmental gradient is not the determinant of the final differentiation of type I cochlear afferents.

2) It is unclear how the authors have dealt with the multiple comparisons that frequently arise. – In “Statistical Analysis”, they write that, when encountering multiple conditions, they have conducted ANOVA followed by post-hoc tests. Did they adjust for multiple comparisons in these post hoc tests? If so, which method did they chose? These issues arise, for instance, on – subsections “Diversity of firing patterns in current clamp”, and – “ Model 1: Spiking neurons only (P3-P10)”.

3) Additional statistical tests are required in some instances:

– Subsection “Current-clamp features of non-spiking neurons are also correlated with normalized basal position” third paragraph: Do the response latencies also vary significantly with position when spiking and non-spiking neutrons are considered separately?

– Subsection “D. Spatial gradients in biophysical properties may be maturational gradients” paragraph one: Please perform a significance test to determine whether the variation in the currents with age is significant.

– In paragraph two: Please perform a significance test for the dependency of the average latencies on age.

– In paragraph three: Please add a significance test for the divergence of the current threshold and the maximal conductance of fibres at the different locations with age.

4) Regarding the linear regression model, the authors determine the variance inflation factor (VIF), and subsequently eliminate variables with a VIF larger than 4. But this is a somewhat arbitrary threshold. The standard and more rigorous way to prevent overfitting is through cross-validation: determine the model parameters from one part of the data (training set) and determine the obtained correlation from the remaining data (test data). Variables can then be eliminated if they improve the model performance (assessed on the test data!). There is also an issue with the model description. Why is the fourth parameter called xn and not x4? This is particularly confusing (and inconsistent) when the text later refers to any variable as xn ( – “Statistical Analysis”). Please clean this up. It should also be stated which variables x1, x2 and so forth represent.

5) The authors say relatively little about how the observed differences in membrane properties contribute to known functional diversity of cochlear afferents. Yes, modiolar afferents have higher current thresholds, but they also have more negative voltage thresholds. Which is more important?

6) In the Discussion, the authors seem to suggest that neurons with "graded firing" may be those that suffered greater damage. Was that the intent?
