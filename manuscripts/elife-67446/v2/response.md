# Author response - Round 1

Authors:
- Cassandra L Hays ([ORCID: 0000-0003-4481-3495](https://orcid.org/0000-0003-4481-3495))
- Asia L Sladek
- Greg D Field ([ORCID: 0000-0001-5942-2679](https://orcid.org/0000-0001-5942-2679))
- Wallace B Thoreson ([ORCID: 0000-0001-7104-042X](https://orcid.org/0000-0001-7104-042X))

## Response text

DOI: [10.7554/eLife.67446.sa2](https://doi.org/10.7554/eLife.67446.sa2)

Reviewer #2:

[…] The authors should provide further clarification to the following issues prior to publication:

1. The authors indicate that anionic currents associated with presynaptic glutamate transport vary linearly with glutamate levels in the synaptic cleft. However, a close examination of the cited work (Hasegawa et al., 2006; Otis and Jahr, 1998) reveal several non-linear regions in the glutamate – IA(glu) dose response. Therefore, the authors should provide further evidence for linearity and ensure that their measurements (especially the large multivesicular events) are indeed within the linear region of detection.

We added some additional information for the reader to the introduction, citing data from Hasegawa et al. indicating that glutamate transporters are not saturated during rod release:

“Glutamate reuptake into rods continues even after post-synaptic mGluR6 receptors in rod bipolar cells become saturated suggesting that transporters are not saturated during rod release {Hasegawa, 2006 #1362}. In that range, glutamate anion currents (IA(glu)) vary linearly with glutamate levels in the synaptic cleft and can thus provide a presynaptic measure of glutamate release (Hasegawa et al., 2006; Otis and Jahr, 1998).”

2. In the manuscript, it is not clearly stated whether the resting Ca2+ independent release is independent of the multivesicular release seen at elevated Ca2+. In my reading, the data suggests that the baseline Poisson process persists even at higher membrane potentials while the multivesicular release process emerges independently. Or do the authors think the two forms of release (univesicular and multivesicular) have the same origin? Further clarification of this issue will be useful.

We agree with the reviewer that the two likely emerge independently and now say so explicitly.

Reviewer #3:

[…] I have only one major comment for the authors.

There has been debate on the precise amount of single-photon responses eliminated by the nonlinear thresholding in between rods and rod bipolar cells in the mouse retina. This amount depends on the set point of the thresholding in this synapse and thereby the model parameters used in the analysis presented in Figure 7 in this paper. The authors explore the impact of multiple factors in their simulation model but not this important issue. It would be important to analyze the impact of the setpoint of the nonlinearity in the modeling approach.

The reviewer wonders how the detection performance of the multi-vesicular release model (Figure 7) relates to the thresholding nonlinearity at the rod-to-rod bipolar cells synapse described in several previous studies (Field and Rieke 2002; Bernston, Smith and Taylor 2004; Trexler, Casti and Zhang 2011). The thresholding nonlinearity described in previous work has been related to the (analog) amplitude of the single photon response. Some work argues that the location of the threshold is slightly above the mean single photon response, so that fewer than half of the single photon responses make it past the nonlinearity (e.g. Field and Rieke 2002). Other work has argued that it is slightly below the mean single photon response (e.g. Bernston, Smith and Taylor, 2004) indicating that a bit more than half of the single photon responses traverse the synapse. It is also worth noting, that the locations of the nonlinearity relative to the single-photon response amplitude is almost certainly very species-dependent, as different species have different signal-to-noise ratios for their single-photon responses (Field and Rieke 2002; Trexler Casti and Zhang 2011; Field, Uzzell, Chichilnisky, and Rieke 2019).

Notice, however, that our study indicates that the output of the rod synapse translates the analog photocurrent (or photovoltage) into what is effectively a digital code of multi-vesicular release events. This analog to digital conversion is certainly a part of the ‘nonlinearity’ described in previous studies but determining how much it contributes to the thresholding at this synapse is challenging. This is because it requires understand how small fluctuations in the amplitude of the photocurrent are related to temporal variability in transmitter release. This would effectively require simultaneous photocurrent (or photovoltage) measurements with measurements of the glutamate transporter currents, and/or a full biophysical model of the rod that relates noise in the membrane voltage to variability in multi-vesicular release events. Notice that the model in Figure 7 doesn’t model the photocurrent (or photovoltage); instead, it begins with a model of the dynamics of transmitter release (see Figure 7B) and only models the observed variability in transmitter release dynamics. While understanding precisely how this analog-to-digital conversion contributes to the thresholding nonlinearity between rods and rod-bipolar cells is certainly interesting, we consider this to be beyond the scope of this study. However, we now explicitly acknowledge this issue and limitation in a new paragraph in the Discussion.
