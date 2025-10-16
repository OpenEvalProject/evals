# A state space modeling approach to real-time phase estimation

## Authors

- Anirudh Wodeyar<sup>1</sup> ([ORCID: 0000-0003-2577-5139](https://orcid.org/0000-0003-2577-5139)) †
- Mark Schatza<sup>2</sup>
- Alik S Widge<sup>2</sup> ([ORCID: 0000-0001-8510-341X](https://orcid.org/0000-0001-8510-341X))
- Uri T Eden<sup>3</sup>
- Mark A Kramer<sup>3</sup>

### Affiliations

1. Mathematics and Statistics Boston University Boston United States
2. Department of Psychiatry University of Minnesota Minneapolis United States
3. Department of Mathematics and Statistics Boston University Boston United States

† Corresponding author

## Abstract

Brain rhythms have been proposed to facilitate brain function, with an especially important role attributed to the phase of low frequency rhythms. Understanding the role of phase in neural function requires interventions that perturb neural activity at a target phase, necessitating estimation of phase in real-time. Current methods for real-time phase estimation rely on bandpass filtering, which assumes narrowband signals and couples the signal and noise in the phase estimate, adding noise to the phase and impairing detections of relationships between phase and behavior. To address this, we propose a state space phase estimator for real-time tracking of phase. By tracking the analytic signal as a latent state, this framework avoids the requirement of bandpass filtering, separately models the signal and the noise, accounts for rhythmic confounds, and provides credible intervals for the phase estimate. We demonstrate in simulations that the state space phase estimator outperforms current state-of-the-art real-time methods in the contexts of common confounds such as broadband rhythms, phase resets and co-occurring rhythms. Finally, we show applications of this approach to in vivo data. The method is available as a ready-to-use plug-in for the OpenEphys acquisition system, making it widely available for use in experiments.
