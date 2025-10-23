# Peer review - Round 1

Editors:
- Edward H Egelman, University of Virginia , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.25648.031](https://doi.org/10.7554/eLife.25648.031)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Single-protein detection in crowded molecular environments with high specificity using cryo-EM" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Richard Aldrich as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Steven J Ludtke (Reviewer #2); Robert M Glaeser (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The method proposed allows one to detect characteristic signatures of macromolecular assemblies in crowded cellular environments without labels. This method is complementary to cryo-EM tomography (cryo-ET) in the sense that the size limit of what can be mapped is much lower than that of cryo-ET, but it appears that sample thicknesses has to be much less than what it can be in tomography. It was felt that this method will be taken up by a large community, and it will make a big impact.

The major claims made for this new method, which are well supported by the data, are:

1) Proteins as small as 150 kDa can be reliably detected in vitreous ice.

2) In a crowded environment, like that of the interior of brain tissue, the molecular weight limit should increase to 300 kDa.

3) Identification of macromolecules is highly specific.

This manuscript demonstrates that it is possible to use very fine-grained template matching to identify component molecules in CryoEM images even when obscured by other material. This study focuses on the unique high resolution features present in individual molecules, rather than the low resolution "shape" information often relied upon in single particle picking software. The method is based on the well-known approach of template matching by cross correlation, in which the templates are known, high-resolution structures of macromolecules whose locations and orientations are being sought. The novel result presented in this manuscript is that such template matching works best when low spatial-frequencies are suppressed, leaving mainly the high-frequency components to dominate the cross-correlation search. It is shown, for example, that the method works best when images are taken so close to focus that one cannot see the particles by eye. This result is highly unexpected, since it is known that the SNR is far better at low frequency than at high frequency. Furthermore, there is well-justified concern in the field that the use of a high-resolution template can produce model-dependent bias. This manuscript properly addresses that concern by setting the threshold for identification very high. This is an interesting study, and worthy of publication in eLife.

While it is very nice to see a manuscript on a topic like this really cover the subject in depth and with sufficient technical detail for others to follow in the author's footsteps, the discussion of the various trials and overall discussion seemed at times rather repetitive, covering the same points multiple times. The main manuscript could be considerably streamlined without reducing its scientific content. A bewildering number of points are discussed, and a large number of panels are grouped into just 4 figures. For the sake of clarity, the authors should undertake a major simplification of the manuscript. Even the overall structure of the presentation itself should be reconsidered and improved. For example, it would help if fewer image-panels were used, sufficient to illustrate the concept behind this method and to document that it really works. Further supporting details might then be moved to Supplemental Material.

The method has clearly demonstrated its ability to work on isolated particles and on particles obscured by the bulk of other molecules (the virus substructure example). A key point in this manuscript seems to be the argument that this may be used for molecular localization as an alternative to tomography in cellular material. This study does not make a convincing argument that this will be possible for two reasons:

1) in-situ molecules are likely to undergo substantial structural variations, and will often be complexed with other molecules which will lead to conformational variation. The question of whether the templates being searched for will be sufficiently similar to the actual molecules has not really been addressed. What level of variability would begin to cause failure? This might be addressed very briefly.

2) Their estimate of a 100nm thick layer as being typical for cellular tomograms seems inaccurate. For Cryo studies either very small whole cells are vitrified, which are typically ~500nm thick, or cells are cryo-sectioned or FIB-milled, which are also frequently considerably thicker than 100nm. Perhaps the authors might want to state that while a 100 nm thick sample might be desired for high resolution tomography, this is usually not possible.

For these reasons, it was felt that either the authors need to show some sort of proof of concept on CryoEM of cellular material, or downplay their claims of usefulness for cellular material somewhat. The reviewers are not stating that the method will not work for cells, simply that this manuscript currently provides insufficient evidence to make this claim.

There were some concerns about the use of the term SNR in this manuscript. SNR is widely used in CryoEM for various purposes and the definition here, while somewhat acceptable from a pure image processing perspective, may be confusing to people in CryoEM. Canonically SNR or SSNR are measures of power or intensity ratios. In that "space" coherent averaging scales as amplitude squared and incoherent averaging scales linearly, producing SSNR which scales linearly with "amplitude" whatever that means in a specific situation. In image processing, SNR is sometimes defined as a ratio between a peak and the standard deviation of the background similarly to this manuscript, but this definition produces an amplitude ratio rather than an intensity ratio, giving the SNR here different scaling properties than the SNR and SSNR elsewhere in CryoEM. Very often the SNR in image processing is also squared for this reason. If the authors opt to continue with this definition, it is important that this discrepancy be described in the SNR methods section.
