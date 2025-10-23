# Robust model-based analysis of single-particle tracking experiments with Spot-On

## Authors

- Anders S Hansen<sup>1</sup> †
- Maxime Woringer<sup>1</sup> ([ORCID: 0000-0003-2581-9808](https://orcid.org/0000-0003-2581-9808))
- Jonathan B Grimm<sup>2</sup>
- Luke D Lavis<sup>3</sup>
- Robert Tjian<sup>1</sup> ([ORCID: 0000-0003-0539-8217](https://orcid.org/0000-0003-0539-8217)) †
- Xavier Darzacq<sup>1</sup> ([ORCID: 0000-0003-2537-8395](https://orcid.org/0000-0003-2537-8395)) †

### Affiliations

1. Department of Molecular and Cell Biology University of California, Berkeley Berkeley United States
2. Janelia Research Campus Howard Hughes Medical Institute Ashburn United States
3. Janelia Farm Research Campus Howard Hughes Medical Institute Ashburn United States

† Corresponding author

## Abstract

Single-particle tracking (SPT) has become an important method to bridge biochemistry and cell biology since it allows direct observation of protein binding and diffusion dynamics in live cells. However, accurately inferring information from SPT studies is challenging due to biases in both data analysis and experimental design. To address analysis bias, we introduce 'Spot-On', an intuitive web-interface. Spot-On implements a kinetic modeling framework that accounts for known biases, including molecules moving out-of-focus, and robustly infers diffusion constants and subpopulations from pooled single-molecule trajectories. To minimize inherent experimental biases, we implement and validate stroboscopic photo-activation SPT (spaSPT), which minimizes motion-blur bias and tracking errors. We validate Spot-On using experimentally realistic simulations and show that Spot-On outperforms other methods. We then apply Spot-On to spaSPT data from live mammalian cells spanning a wide range of nuclear dynamics and demonstrate that Spot-On consistently and robustly infers subpopulation fractions and diffusion constants.
