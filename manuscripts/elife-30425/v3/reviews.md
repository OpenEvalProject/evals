# Peer review - Round 1

Editors:
- Richard S Lewis, Stanford University School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.30425.026](https://doi.org/10.7554/eLife.30425.026)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Fusion of Cardiology and Astronomy Empowers Characterization and Functional 3D Mapping of Individual Excitation Contraction Coupling Sites" for consideration by eLife. Your article has been favorably evaluated by Anna Akhmanova (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal their identity: Michael Stern (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The study by Tian and colleagues introduces and evaluates an interesting new approach to reconstruct the spatial and temporal distribution of Ca2+ release sites in living cells. The approach (CaCLEAN) uses the CLEAN algorithm of radio astronomy convolved with a Ca2+ diffusion model to localize and characterize Ca2+ release events in cardiac myocytes under normal excitation-contraction coupling (ECC) conditions.

The significance of the new technique is that it makes possible for the first time, analysis of triggered calcium signaling events at thousands of closely spaced ECC couplons in intact muscle, thus providing a new window on mechanisms of physiological ECC. The authors describe a variety of tests to validate the technique, and apply it to study the bases for the negative Ca2+ amplitude-frequency effect and the effects of β-adrenergic stimulation. By revealing the behavior of individual Ca2+ release units under different conditions, the technique has the potential to distinguish changes in local Ca2+ flux amplitude and the probability and reliability of localized Ca2+ release events. The technique provides a powerful new tool to study mechanisms underlying physiological and pathophysiological behavior of the heart, and may have broader application to a wide variety of calcium signaling events in other cell types as well.

Essential revisions:

All three reviewers agreed that the CaCLEAN technique is innovative and potentially powerful, and will interest a broad community of researchers in the area of calcium signaling. However, the reviewers found the current description and validation of CaCLEAN inadequate. As described the technique is semi-empirical, choices of key parameters are not experimentally constrained, and there are not enough data to evaluate the technique's accuracy in identifying the true locations of Ca2+ release events. To address these issues, the following essential concerns must be adequately addressed before the paper can be accepted.

1) CaCLEAN needs additional validation before it can be accepted as ground truth about calcium release events. The performance of the algorithm depends highly on underlying assumptions of parameters and the choice of diffusion coefficients. More confidence is needed that the location of release sites is an unbiased estimate of their true location, and that the presence or absence of a spark at a given location is not influenced by variations in dye loading, light intensity etc.

a) The resolution limits of the CaCLEAN technique and implications for interpretation of results need to be discussed more quantitatively. What proportion of the CaCLEAN sites are individual as opposed to overlapping couplons? Thresholding is used in the CLEAN iterations to avoid false positives, but how does the choice of threshold affect the number of missed events (i.e., couplons)?

One approach to give a more complete description of the accuracy and limits of the technique would be to simulate dye images of large numbers of closely localized simultaneous sparks at known locations, and determine how precisely and accurately those locations are recovered by the CaCLEAN process. Ideally this would involve a 3D reaction-diffusion model, but this may not be practical for a variety of reasons, including the time required, and the lack of consensus on a single calcium model with buffering for the myocyte.

As a reasonable compromise, one could generate a single spark image using existing spark models, and linearly superimpose a large number of copies with various centers to see if CaCLEAN can recover the centers. This would address the major question of whether clustering and overlapping of the fluorescence patterns cause any systematic bias in CaCLEAN, even though it would not take into account all the nonlinear buffering interactions among sources. This should be do-able, preferably with the sparks placed in 3 dimensions and then "imaged" with the confocal PSF.

In this way one could specify a range of critical conditions (couplon spacing, S/N ratio, assumed values for CLEAN thresholding and diffusion coefficients) required for the algorithm to generate an accurate map, and to place quantitative limits on its accuracy. Such information will be essential to validate the technique and to enable others to use it properly.

b) As a further consistency check, it would be useful to use the algorithm to reconstruct release sites in quiescent myocytes that exhibit spontaneous sparks. Raw frame data for that analysis should be readily available (perhaps from frames between stimulations). This test should allow a visual comparison between observed sparks and ECC release sites which would provide a consistency check as well as demonstrate the small subset of couplons that are engaged in spontaneous activity.

c) The algorithm assumes symmetrical diffusion, raising the question of how the reconstruction would be affected by diffusion barriers closed to couplons, e.g., mitochondria. Ideally this would be addressed by using appropriate simulated data, but if this is beyond the scope of the current study, a brief discussion of such potential effects should be included.

2) Better quantification in several places is needed.

a) Regarding the proximity of Ca2+ release sites to the plasma membrane in Figure 1D, the text refers only to a "very good correlation." A quantitative measure should be included.

b) In Figure 2A, the masks show a "very good match" while in Figure 2B the pattern of couplons is "rather different." Important information could be gleaned by measuring the probability of firing for each couplon over multiple stimuli, revealing the location of couplons that are highly reliable vs. those that are not. Are the most reliable couplons the first to fire? The number of cells analyzed should also be stated.

c) In Figure 1D-E, Ca2+ signals are measured at different distances from entry sites, but they are not strictly comparable because they are recorded in the vicinity of different entry sites. It would be more informative to compare responses at variable distances from the same entry site, and to average several examples if possible.

3) The algorithm, and in particular the ACO, needs to be more clearly described. How is the ACO generated, what is the equation for it, and how are the particular choices of ACO parameters justified? Is the ACO amplitude or size the more important variable? How does the choice of ACO parameters (amplitude, diffusion coefficient) affect the lateral spatial resolution?

4) The application of CaCLEAN to understand the negative amplitude-frequency relationship is a potential strength of the paper. Early on the authors mention decreased SR Ca2+ content and a decreased number of participating couplons as possible causes, but their respective contributions are not fully resolved here. A decreased number of couplons certainly contributes (Figure 3Cb), but are the Ca2+ transient amplitudes of active couplons constant or do they decline with frequency? One way to address this would be to calculate the mean and s.d. of Ca2+ signal time course from the entire ensemble of couplons at low and high driving frequencies, and plot the average F vs. time to illustrate any changes. Multiplying this waveform by the number of active couplons may then demonstrate whether these changes are sufficient to account for the observed Ca-frequency relationship.

In the Abstract, the negative amplitude-frequency relationship is attributed to decreased firing reliability at higher frequencies. However, it is not clear whether release reliability (as defined by the temporal and spatial CV) tells us anything more than the decline in the total number of active couplons. This should be clarified.
