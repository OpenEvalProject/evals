# Peer review - Round 1

Editors:
- Björn Herrmann, Baycrest Hospital Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.91605.3.sa0](https://doi.org/10.7554/eLife.91605.3.sa0)

Building on previous toolboxes to distinguish 1/f noise from oscillatory activity, this study introduces an important advancement in neural signal analysis to identify oscillatory activity in electrophysiological data that refines the accuracy of identifying non-sinusoidal neural oscillations. Extensive validation, using synthetic and various empirical data, provides convincing evidence for the accuracy of the method and outlines practical implications for relevant scientific problems in the field.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91605.3.sa1](https://doi.org/10.7554/eLife.91605.3.sa1)

Summary:

The study introduces and validates the Cyclic Homogeneous Oscillation (CHO) detection method to precisely determine the duration, location, and fundamental frequency of non-sinusoidal neural oscillations. Traditional spectral analysis methods face challenges in distinguishing the fundamental frequency of non-sinusoidal oscillations from their harmonics, leading to potential inaccuracies. The authors implement an underexplored approach, using the auto-correlation structure to identify the characteristic frequency of an oscillation. By combining this strategy with existing time-frequency tools to identify when oscillations occur, the authors strive to solve outstanding challenges involving spurious harmonic peaks detected in time-frequency representations. Empirical tests using electrocorticographic (ECoG) and electroencephalographic (EEG) signals further support the efficacy of CHO in detecting neural oscillations.

Strengths:

The paper puts important emphasis on the 'identity' question of oscillatory identification. The field primarily identifies oscillations through frequency, space (brain region), and time (length, and relative to task or rest). However, more tools that claim to further characterize oscillations by their defining/identifying traits are needed, in addition to data-driven studies about what the identifiable traits of neural oscillations are beyond frequency, location, and time. Such tools are useful for potentially distinguishing between circuit mechanistic generators underlying signals that may not otherwise be distinguished. This paper states this problem well and puts forth a new type of objective for neural signal processing methods.

The paper uses synthetic data and multimodal recordings at multiple scales to validate the tool, suggesting CHO's robustness and applicability in various real-data scenarios. The figures illustratively demonstrate how CHO works on such synthetic and real examples, depicting in both time and frequency domains. The synthetic data are well-designed, and capable of producing transient oscillatory bursts with non-sinusoidal characteristics within 1/f noise. Using both non-invasive and invasive signals exposes CHO to conditions which may differ in the extent and quality of harmonic signal structure. An interesting follow-up question is whether the utility demonstrated here holds for MEG signals, as well as source-reconstructed signals from non-invasive recordings.

This study is accompanied by open-source code and data for use by the community.

Weaknesses:

The criteria that the authors use for neural oscillations embody some operating assumptions underlying their characteristics, perhaps informed by immediate use cases intended by the authors (e.g., hippocampal bursts). The extent to which these assumptions hold in all circumstances should be investigated. For instance, the notion of consistent auto-correlation breaks down in scenarios where instantaneous frequency fluctuates significantly at the scale of a few cycles. Imagine an alpha-beta complex without harmonics (Jones 2009). If oscillations change phase position within a timeframe of a few cycles, it would be difficult for a single peak in the auto-correlation structure to elucidate the complex time-varying peak frequency in a dynamic fashion. Likewise, it is unclear whether bounding boxes with a pre-specified overlap can capture complexes that manoeuvre across peak frequencies.

This method appears to lack the implementation of statistical inferential techniques for estimating and interpreting auto-correlation and spectral structure. In standard practice, auto-correlation functions and spectral measures can be subjected to statistical inference to establish confidence intervals, often helping to determine the significance of the estimates. Doing so would be useful for expressing the likelihood that an oscillation and its harmonic has the same auto-correlation structure and fundamental frequency, or more robustly identifying harmonic peaks in the presence of spectral noise. Here, the authors appear to use auto-correlation and time-frequency decomposition more as a deterministic tool rather than an inferential one. Overall, an inferential approach would help differentiate between true effects and those that might spuriously occur due to the nature of the data. Ultimately, a more statistically principled approach might estimate harmonic structure in the presence of noise in a unified manner transmitted throughout the methodological steps.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91605.3.sa2](https://doi.org/10.7554/eLife.91605.3.sa2)

Summary:

A new toolbox is presented that builds on previous toolboxes to distinguish between real and spurious oscillatory activity, which can be induced by non-sinusoidal waveshapes. Whilst there are many toolboxes that help to distinguish between 1/f noise and oscillations, not many tools are available that help to distinguish true oscillatory activity from spurious oscillatory activity induced in harmonics of the fundamental frequency by non-sinusoidal waveshapes. The authors present a new algorithm which is based on autocorrelation to separate real from spurious oscillatory activity. The algorithm is extensively validated using synthetic (simulated) data, and various empirical datasets from EEG, and intracranial EEG in various locations and domains (i.e. auditory cortex, hippocampus, etc.).

Strengths:

Distinguishing real from spurious oscillatory activity due to non-sinusoidal waveshapes is an issue that has plagued the field for quite a long time. The presented toolbox addresses this fundamental problem which will be of great use for the community. The paper is written in a very accessible and clear way so that readers less familiar with the intricacies of Fourier transform and signal processing will also be able to follow it. A particular strength is the broad validation of the toolbox, using synthetic, scalp EEG, EcoG, and stereotactic EEG in various locations and paradigms.

Weaknesses:

A weakness is that the algorithm seems to be quite conservative in identifying oscillatory activity which may render it only useful for analyzing very strong oscillatory signals (i.e. alpha), but less suitable for weaker oscillatory signals (i.e. gamma).
