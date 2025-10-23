# Peer review - Round 1

Editors:
- Indira M Raman, Northwestern University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.15202.017](https://doi.org/10.7554/eLife.15202.017)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Optical electrophysiology for probing ion channel function and pharmacology" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Richard Aldrich as the Senior Editor. One of the two reviewers has agreed to reveal his identity: Brian Salzberg.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript describes the development of an all-optical electrophysiology technique for studying activity-dependent modulation of ion channels (in this case, NaV1.7), in a format compatible with high throughput screening. The authors employ expressed CheRiff as an optical activator, and QuasAr2 as an optical voltage reporter, in genetically engineered HEK cells. Their work demonstrates that optical electrophysiology provides, as they put it, "a favorable tradeoff between accuracy and throughput."

Essential revisions:

While the reviewers were favorable about the idea and many elements of the approach, they shared some concerns about the manuscript, which fall in to two categories: first, scientifically, no major new discoveries are clearly evident and second, technologically, some issues that are inadequately addressed. With respect to the first category, if the focus is indeed on the tool aspect, it might be possible to consider the manuscript for the Tools and Resources section of eLife, where the technique is more relevant than the discovery. But, in that case, the points in the second category become all the more important. The essential points to address therefore become the following:

The very high intensity light necessary to activate the optogenetic reporter and consequent questions of tissue damage and value over existing methods, expanded upon by the reviewers in point 1a and 1b below; 2) The apparent dependence of the technique on the regenerative capacities of V-gated Na channels, which might limit its general applicability, expanded upon by the reviewers in point 2 below, and 3) The issue of interference with other pharmacological agents, expanded upon by the reviewers in point 3 below.

1) The major criticism is over the use of QuasAr2 as the optical reporter. The light intensity used to excite QuasAr2 is about two orders of magnitude higher than (already high) intensities used normally for optogenetics. One wonders whether fluorescence excitation at an intensity of 400 W/cm2 is truly useful, or, for that matter, necessary. This illumination intensity is provided by not one, but two lasers, exciting the cells in parallel, because the quantum yield of the fluorescent protein is relatively low.

A) The bleaching and phototoxicity produced by such high illumination should be quantified. The authors should also provide some data on the heating effects of illuminating the preparation for extended times with 400 W/cm2 in the near infrared.

B) Also, why can't an organic voltage sensitive dye, applied in the bath, and requiring orders of magnitude lower illumination intensity be used as the optical reporter? There exist dozens of voltage sensitive dyes that can provide the speed (greater than that of QuasAr2), and the sensitivity to circumvent the illumination problem.

2) The authors claim their capacity to probe in a semi-quantitative way the activation, inactivation and state-dependent pharmacological blockade of voltage-gated sodium channels. However, the quantitative aspect of the measurements is questionable. The whole study is based on the occurrence of sodium-dependent regenerative depolarizations (spikes) produced by NaV channels. The figures displaying single-cell recordings of these spikes (Figure 2E and Figure 2—figure supplement 1) show that they occur in an all-or-none fashion, as expected from a dynamical system with NaV channels. Therefore, the appearance of partial blockade reported in the figures are obtained by averaging many cell, some of which are still able to generate spikes and others not. As a consequence, the range of modulation over which the technique is sensitive will depend heavily on the variability of NaV expression. If all the cells were expressing the same density of NaV, one would expect response curves being step functions, as all the cells would cross the threshold for regenerative spiking at the same level of channel modulation. This aspect must be quantified extensively by monitoring the dependence of the spike on channel density and by measuring the distribution of NaV channel expression in the polyclonal cell mixture, relative to the density threshold for regenerative spiking. Finally, the maximal plateau potential evoked by optogenetic stimulation looks dangerously close to spike threshold in Figure 2—figure supplement 1A. This aspect must be quantified extensively. Additionally, while establishing a proof of principle for all-optical screening using this new optogenetic toolset, the paper falls short of comparing quantitatively all-optical measurements with electrophysiological measurements. Furthermore, the applicability to a wide range of voltage-gated channels, other than sodium channels, is not clearly demonstrated, given the dependence of the current assay on regenerative spiking.

3) The authors point rightly (Discussion, fourth paragraph) that interference of tested pharmacological compounds with the optogenetic reporters and actuators may produce false positive and false negative results, but that it is unlikely to happen. The burden of proof should not be left on potential users of their technique. The interference with the optogenetic tools of a wide subsets of the compounds used in this study, from different chemical families, should be tested using systematic patch-clamp recordings.
