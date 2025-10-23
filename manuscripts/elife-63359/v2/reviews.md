# Peer review - Round 1

Editors:
- Inna Slutsky, Tel Aviv University Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63359.sa1](https://doi.org/10.7554/eLife.63359.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

In this manuscript, the authors developed a soma-targeted variant of an existing blue-light sensitive opsin for efficient optogenetic stimulation. It allows neuronal stimulation with ten-fold lower power and low spectral crosstalk with red calcium indicator. This newly developed opsin presents a new powerful tool for a large-scale all-optical control of neuronal activity in vivo.

Decision letter after peer review:

Thank you for submitting your article "Optogenetic strategies for high-efficiency crosstalk-free all-optical interrogation using blue light-sensitive opsins" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and John Huguenard as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Shai Berlin (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

In this manuscript, the authors developed a soma-targeted variant of an existing blue-light sensitive opsin, CoChR, for efficient optogenetic stimulation and combined it with red calcium indicator aiming to achieve low crosstalk in all-optical control of neuronal activity. Compared to a previous soma-restricted version of CoChR, the new stCoChR achieves soma restriction without compromising photocurrent, thus enabling efficient two-photon neuronal excitation in vivo. The optimal laser power and repetition rate for driving spikes in stCoChR positive neurons were carefully calibrated with juxtasomal recordings in vivo. The authors tested the crosstalk between two-photon raster scanning at a wavelength typically used for imaging red functional indicators and photoactivation of stCoChR-expressing neurons. They also demonstrated simultaneous two-photon imaging and holographic photostimulation of L2/3 neurons in mice.

While the reviewers are impressed by the efficiency of the new opsin variant, which will be useful for the growing community of experimenters performing "all-optical experiments", the claim of 'crosstalk-free' all-optical interrogation – stated in the title! – is not fully convincing. Therefore, the advance presented here is being oversold, unless the authors provide further evidence as detailed below.

Essential revisions:

1. The experiments in Figure 5 and Figure S5 aim to quantify the crosstalk between imaging and photostimulation, which is the key advantage of the proposed method over previous all-optical approaches. However, these experiments were performed in neurons expressing stCoChR without RCaMP.

The concern is whether the imaging conditions used here can provide sufficient RCaMP signal, if RCaMP is co-expressed. Imaging quality is particularly important here given that jRCaMP1a is not as bright as GCaMP6s as adopted in many other all-optical studies. The authors argued they used 'imaging conditions commonly used to monitor red-shifted functional indicators', but the expression of stCoChR may affect the expression of RCaMP, and therefore requires more power for imaging the same neurons.

Ideally these cross-talk experiments should be done in neurons co-expressing stCoChR and RCaMP, with simultaneous imaging and juxtasomal recording to confirm that the imaging conditions used here is sufficient to report spikes in the jRCaMP1 signal while insufficient to activate the opsin.

2. What is the success rate of all-optical manipulation? Specifically, what is the percentage of targeted cells that showed fluorescence transients with adequate signal-to-noise? How does this percentage vary with different photostimulation laser repetition rates and power? Are the traces in Figure 6C showing all targeted neurons in one experiment?

3. Will increasing imaging power assist the detection of photostimulation-evoked RCaMP events? As one increases the imaging laser power, at what point does it stop improving detection of RCaMP events immediately following photostimulation, and at what point does it start to increase the baseline RCaMP events in the opsin-positive neurons in the field-of-view? Answers to these questions will also assist the evaluation of crosstalk between RCaMP imaging and stCoChR activation.

4. The authors show that reducing the repetition rate of the laser allows holographic activation of stCoChR at low average power. A biophysical explanation for this observation is not given. The results are clearly presented and the new tool is certainly of interest for in-vivo optogenetics labs, as there is no detectable interference between calcium imaging and photostimulation. A caveat is the relatively poor control of spike timing: The method requires 20 ms of 2p excitation to reliably generate an action potential, while blue light pulses of 1 ms are usually sufficient. Given that the closing of stCoChR is also relatively slow, it would be of interest to know the maximum frequency at which single spike control is possible with this approach. Also, the z-resolution is poor (>80 µm), which could be a problem for dense cell layers. In a methods paper, these limitations should be discussed.

5. Because of the quadratic dependence of excitation events on pulse intensity, 2p imaging/photoactivation at lower pulse repetition rates can be performed at lower average power – this is not a miracle. Whether a low rep rate/high pulse energy regime confers any real advantage depends on the nature of the expected photodamage: If thermal effects dominate, low average power is a good thing. The advantage of reduced repetition rates (and very short pulses!) for two-photon imaging of retinal has recently been published (Palczewska et al., PNAS, https://doi.org/10.1073/pnas.2007527117), this paper should be cited. If, on the other hand, triplet states and solvated electrons are produced and lead to the destruction of biomolecules, high peak powers are to be avoided. For 2p imaging, it has been shown that higher rep rates (with lower pulse power) strongly reduce the amount of photobleaching (Fuzeng Niu et al. 2019 Laser Phys. 29 046001). Will ever higher peak powers at some point be a problem for CoChR, do they bleach the retinal? A discussion along these lines would leave the reader less mystified (as the authors do not show a lower limit/optimum for the rep rate).

6. The authors do not provide a single micrograph showing the localization of stCoChR. As this is one of their main contributions here, they should provide high resolution micrographs showing the localization of the stCoChR in neurons. This could be done by immunolabelling or by simply removing the P2A sequence, and trying to see whether these are really soma targeted (and to what extent in comparison to dendrites, for instance).

7. What is missing throughout the paper are control experiments showing that without opsins, these different illumination schemes do not evoke firing. This is really missing in the all-optical interrogation of neurons in Figure 6. The authors need to show that under identical imaging settings, neurons that do not express stCoChR (but that positively express jRCaMP1a) do not fire! This experiment (Figure 6) also requires recording of electrical activity along the optical responses and this is because in the example they show (Figure 6C), the responses do not look like APs, rather small increases in fluorescence due to low Ca2+ elevations. The authors should also show longer recordings (as they do in Figure 5B for instance) and then compare between the optical responses (DF/F) of jRCAMP to spontaneous APs versus those obtained by the optical stimulation of stCoChR. Are they different (DF/F, kinetics, etc).?
