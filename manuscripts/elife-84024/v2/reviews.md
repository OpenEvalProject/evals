# Peer review - Round 1

Editors:
- Amy FD Howard, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84024.sa0](https://doi.org/10.7554/eLife.84024.sa0)

This paper presents a valuable cross-validation study of mesoscopic measurements of axonal orientations from three different modalities – small-angle X-ray scattering, scattered light imaging, and diffusion MRI – and is of interest to researchers who want to apply these methods to white matter imaging. The authors show convincing similarities and differences in fiber orientations from all three methods over partial ex vivo brain samples, though the validation of diffusion MRI could be strengthened by considering other fiber reconstruction methods, as only a single diffusion method is investigated.


---

# Peer review - Round 1

Editors:
- Amy FD Howard, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84024.sa1](https://doi.org/10.7554/eLife.84024.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Using light and X-ray scattering to untangle complex neuronal orientations and validate diffusion MRI" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Timothy Behrens as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Anastasia Yendiki (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) One primary concern is regarding the generalisability of the conclusions with respect to the diffusion MRI analysis. First, diffusion MRI provides many different approaches to estimating fibre orientations within the voxel, each of which often has user-defined options that can affect the resulting fibre orientation distribution. Here only a single method is presented. Second, the presence of secondary peaks of small magnitude in single fibre voxels such as a corpus callosum is a known artefact, where subsequent downstream analyses often ignore peaks below some magnitude threshold. A better agreement between SAXS and diffusion MRI may be found if the diffusion FODs were thresholded prior to comparison. Third, the diffusion voxels are larger than the microscopy sections, meaning that the microscopy may not include fibre populations existing in the MRI. Fourth, the analysis considers two postmortem brain samples covering only a small tissue area.

Though the results on diffusion MRI may reflect the data and analysis presented, the conclusions lack generalisability as the diffusion MRI estimates of FOD are very methods dependent (with only one tested here), and potentially lack impact as these additional peaks are often ignored in downstream analyses. These points were somewhat noted in the discussion but do strongly limit the interest of these results to the diffusion MRI community. Given these limitations, the authors should refrain from making unsupported generalised claims about all diffusion MRI analyses, and considerable changes are required to ensure this key concern is properly addressed. This includes but is not limited to textual edits throughout the manuscript and the removal of titles such as "Diffusion MRI tends to overestimate fiber orientations in the human brain" and similar phrases. The title "Identification of false-positive fiber tracts in dMRI", should also be reconsidered given that analysis to identify tracts (e.g. tractography) rather than fibre populations was not performed.

2) The comparison of fibre orientations at the pixel/voxel-wise level is heavily reliant on the accuracy of the data co-registration, including rotation of the fibre orientations. Here only affine registration was used, though the microscopy processing may result in non-linear deformations. Please can the authors provide an evaluation of the quality of the coregistration and a discussion into how this may affect results?

3) Some of the methods were unclear and require additional clarification (please see comments below). In particular, it was unclear a) at what resolution the SLI/SAXS comparisons were made and how data were up/down-sampled to make these comparisons, b) the difference between SLI scatterometry and angular SLI, c) how through plane orientations are computed from SLI, and d) how the correspondence of primary and secondary fibre populations was ensured across modalities.

4) The presentation of the study as a framework for combining SLI/SAXS/dMRI data, rather than a cross-validation study, caused some confusion. There are no clear prescriptions for how researchers interested in the neuroanatomical investigation would combine information from SLI and SAXS, or use the two methods in tandem, rather the information from one modality is used to corroborate/validate that from the other. Further, only SAXS is really compared to the diffusion MRI, presumably due to SLI having unreliable through-plane information. The authors will need to re-consider wording throughout the manuscript (see phrases such as "The combination of scattered light and X-ray imaging …[enable] detailed investigations of complex tract architecture in the animal and human brain", "The high-resolution properties of the former combined with the high-specificity of the latter enables the detailed reconstruction of multiple nerve fiber orientations for each image pixel, which can provide providing unprecedented insights into brain circuitry." or "The presented framework can … deliver more accurate brain connectivity maps of the animal and human brain." for example), or else additional information and example analyses should be provided on how these modalities can be combined for neuroanatomical investigation, particularly in regions where the information from the different modalities does not agree.

5) This may be an issue with the paper submission, but unfortunately the PDF figures were low resolution making the fibre orientations difficult to see. Higher-resolution images would be required in print.

This study presents a valuable comparison of fibre orientation estimates from three different modalities: diffusion MRI, scattered light imaging, and x-ray scattering. The comparison is interesting as each modality is sensitive to different aspects of tissue microstructure – water anisotropy, micron-scale structural coherence, and myelin lamella respectively. Where scattered light and x-ray imaging can be only applied ex vivo, diffusion MRI has in vivo applications but suffers from being an indirect estimate of the microstructure of interest. By acquiring all modalities in both a vervet monkey and human brain sample, the authors provide quantitative, pixel/voxel-wise comparisons of fibre orientation estimates within the same tissue samples. The authors show convincing agreement in fibre orientations from all three methods, giving confidence in the fidelity of the methods for neuroanatomical investigations. Differences are also observed: SLI is shown to have less reliable estimates of fibre inclination, and the CSD analysis presented overestimates the number of crossing fibre populations when compared to the microscopy methods, particularly in single fibre regions such as the corpus callosum, a known artefact in some diffusion analyses.

In the current PDF, it is very difficult to see fibre orientations in figures due to low resolution, limiting the reader's ability to assess the results. Higher-resolution images would provide more information and easier comparisons.

The methods are generally clear though some additional information is needed: 1) to specify the resolution that the orientations are compared in each figure and how data was up-/down-sampled for these comparisons respectively. For example, each SAXS pixel contains many SLI pixels. It is currently unclear whether the mean SLI orientation from a neighbourhood is equivalent to the SLI compared, or whether a comparison was made for each SLI pixel. Similarly, for the dMRI-microscopy comparisons. 2) I also could not follow why two SLI methods are presented in the methods: SLI scatterometry relating to Figure 2, and angular SLI relating to all other results. Further clarification is needed. 3) Since the quality of the data co-registration can strongly impact pixel/voxel-wise comparisons, quantification of the registration accuracy or overlays demonstrating the quality of the co-registration would be valuable.

A primary weakness of the work as a diffusion MRI validation study is that though diffusion MRI supports many different models to extract fibre orientations with different outputs, here only a single model is compared to the microscopy data, which may affect the generalisability of the results. Further, it only compares the primary orientations from the diffusion MRI and does not consider each fibre population's magnitude (density of fibres) or the orientation dispersion, both of which can influence downstream analyses.

The paper could be strengthened by a more detailed discussion on the differences between the imaging modalities – e.g. in terms of imaging resolution, signal-generating mechanisms, and sensitivity to specific aspects of the tissue microstructure – and how these differences may limit their application to specific neuroanatomical investigations, or ability to validate one another. For example, the microscopy sections are 80 microns thick whilst the diffusion voxel is 200 microns. I expect this could contribute to the difference in the number of fibre populations per voxel.

The hypothesis that dMRI signal contributions from extra-axonal water result in additional fibre populations could be investigated by running CSD on both low and high-b-value data (for example using the openly available MGH dataset, Fan 2016) where fewer secondary fibre populations should be observed at high b-value.

Thanks to the authors for providing links to the code and data relevant to the manuscript.

It would be very interesting to have the authors comment on the ability of SLI/SAXS to validate dMRI estimates of fibre density of dispersion or demonstrate a comparison of these.

Some suggestions on the manuscript:

– Abstract: "we find a reduction of peak distance with increasing out-of-plane fiber angles" – Without additional context from the paper, I found this statement unclear. Some further explanation or rephrasing would help.

– Line 58 – Please can you give the resolutions of SLI/SAXS

– Line 123 "Figure 4A shows very small angular differences that appear to be uniformly distributed" – I'm not sure what is meant here the distribution doesn't appear to be shown.

– Figure 4 – please can you clarify why some regions do not appear to be included in the analysis? i.e. the top right-hand side of the slide is missing in A/B and parts of the cingulum appear to be missing in part C. What is the rationale for this? By excluding many pixels from the cingulum in the histogram in 4d, would this not lead to an underestimation of the angular difference?

– Figure 4a – I would recommend using a colour bar where colours have a unique meaning. White or light red currently can mean more than one thing in the image.

– Figure 5 – The 3D colour wheel is atypical for dMRI community which usually uses blue for IS and green for AP. Though the current version is acceptable as the meaning of the colours is clearly indexed, it may be worth considering changing to avoid any confusion.

– Line 173 onwards – Please can you provide the maps of single/crossing fibre voxels for both dMRI and SAXS? It would be interesting to see the clustering of the single/crossing fibre populations.

– Line 203 – I find it very hard to interpret or see the 3D arrows in Figure 6A

– Line 413 – "The high-resolution properties of the former combined with the high-specificity of the latter enables the detailed reconstruction of multiple nerve fiber orientations for each image pixel, which can provide providing unprecedented insights into brain circuitry." This conclusion seems out of place given the work presented, as details have not been provided on how to combine information from these modalities.

– Line 414 – Typo "provide providing"

– Line 429 – I assume the tissue was immersion fixed?

Reviewer #2 (Recommendations for the authors):

This work is a cross-validation of an x-ray tomography technique (SAXS) and an optical microscopy technique (SLI) for imaging axonal orientations ex vivo. These innovative methods were introduced in recent papers by the authors, who have teamed up here to compare them side-by-side on the same tissue samples for the first time. The two methods are both label-free (do not require staining) and they are quite complementary. SAXS can provide full 3D orientation measurements on intact tissue, but it operates at a mesoscopic resolution and requires access to a synchrotron. SLI can measure the orientations of multiple fascicles per voxel at a microscopic resolution and relies on more widely accessible equipment, but its accuracy suffers for fiber orientations perpendicular to the imaging plane and it requires tissue to be sectioned before it is imaged. Therefore it makes a lot of sense to explore the complementary strengths of these two techniques, and to use one to "fill in the blanks" of the other. The paper also compares the orientation measurements obtained with SAXS and SLI to those obtained with diffusion MRI. The latter provides only indirect measurements based on water diffusion, at a mesoscopic resolution somewhat lower than that of SAXS, but has the benefit of being feasible in vivo.

A limitation of this study is that conclusions on the comparison between SAXS and SLI are drawn from only 2 sections of a partial monkey brain sample and 2 sections of a partial human brain sample. Conclusions on diffusion MRI are drawn only on the 2 human sample sections. This is particularly an issue for the comparison to diffusion MRI, as the diffusion MRI voxels are wider than the section thickness, hence one cannot preclude that any orientations detected with diffusion MRI but not with SAXS and SLI come from the portion of the voxel that is missing from the corresponding SAXS/SLI section.

The stated aim of the paper is to provide a framework for combining the complementary benefits of SAXS and SLI, rather than simply presenting the results of a cross-validation study. This is a significant and ambitious aim. However, in order for this to serve as a framework, there would have to be clear prescriptions for how researchers interested in obtaining ground-truth measurements of axonal orientations would do so by using these two methods in tandem. This is not adequately developed in the paper in its present form. For example, the results show reasonable agreement between SAXS and SLI orientations when fibers lie within the SLI imaging plane and decreasing agreement for fibers with increasing through-plane inclination. How would the two methods be combined in voxels where they disagree? Would one use SLI orientations in voxels with fewer through-plane fibers and SAXS orientations in voxels with more through-plane fibers? How would voxels be assigned to each category? How would the orientation vectors from the two modalities be composed and how would the resolution difference between the two be handled? When the through-plane measurement of SLI is unreliable, is its in-plane measurement still reliable? That is if there were one mainly in-plane and one mainly through-plane fiber population, would the orientation of the former still be measured correctly by SLI? There is also considerable agreement reported here between through-plane orientations obtained with SAXS and diffusion MRI. Would this mean that diffusion MRI itself could be used to supplement SLI with through-plane orientations? Any clear set of prescriptions along these lines would represent a framework for imaging orientations by combining modalities. This, however, would require detailed steps for how to perform the combination and use the multi- vs. uni-modal framework to reconstruct connectional anatomy.

A key advantage of SAXS is that it can be performed on intact samples, i.e., before any nonlinear distortions of the tissue are introduced by sectioning. Thus it can provide an undistorted reference, with contrast on axonal orientations that would be absent in, say, a structural MRI of comparable resolution. This contrast could be used to drive registration of the distorted SLI sections to an undistorted SAXS volume, and therefore is a key way in which the two techniques can complement each other. Here, however, this is not explored, as SAXS is performed after sectioning. It is not clear if this is the authors' prescription for how a combined SAXS/SLI framework would be implemented, or if it was done specifically for this study. First, it would seem that SAXS on the intact sample would be lower maintenance, requiring less setup time and hence potentially less overall beamtime than performing SAXS on each section separately. This would make it more practical for routine deployment beyond a few sections. Second, because the SAXS data are now nonlinearly distorted, they cannot be affinely aligned to the MRI volumes. While, in principle, performing both SAXS and SLI on the sections may facilitate the comparison between the two, having to unmount, rehydrate, and remount the sections in between may negate this advantage, as now there is no guarantee that SAXS and SLI can be affinely registered to each other. Here all these registration steps are performed affinely, so it is unclear to which extent the computed errors between modalities are characterizing the inherent limitations of the respective contrasts, or limitations of the registration technique. Some of the alignment is performed manually, for example, specific regions of the images are realigned by hand, and the slice of the diffusion MRI volume that is aligned to the SAXS/SLI sections is chosen by hand. Again, for this to serve as a framework that can be deployed on whole samples, there would have to be clear prescriptions for how to perform these steps robustly, how to ensure that the MRI can be acquired in a coordinate frame parallel to the sections, etc.

Finally, the paper puts forth a general conclusion that diffusion MRI overestimates the number of fiber populations per voxel, on the basis of small ODF peaks appearing perpendicular to the main ODF peaks. Of all conclusions in the paper, this is the least convincingly supported by evidence. First, these small perpendicular peaks are a known artifact, which would be typically eliminated by ignoring ODF peaks below a certain amplitude, a common practice in diffusion tractography algorithms. The authors refrain from using an amplitude threshold, with the rationale that it may also remove true diffusion orientations. However, they apply a threshold when they detect SLI peaks (a rather stringent 8% of the maximum). Second, the explanation that these artifactual peaks may appear due to vessel walls is not convincing. Vasculature is sparse. A single vessel wall will not impact the diffusion signal in the same way as a bundle of parallel axons. In an axon bundle, water molecule displacements are restricted in all directions except parallel to the axons. A single vessel wall in a voxel will not have the same effect on displacements (which are much smaller than the size of the voxel). From Figure 5, it looks like there would be at most 1-2 of these vessels in a diffusion MRI voxel, and they would not be in all voxels. This cannot explain the widespread appearance of these small artifactual peaks. Third, many ODF reconstruction methods have parameters that can be adjusted to make these artifactual peaks more or less prominent. The default parameters may be optimal for in vivo but not ex vivo data, due to the effects of fixation. In light of these concerns, I would caution against making such a general statement about all diffusion MRI in the human brain, especially on the basis of a single diffusion reconstruction method applied to a single location in one brain.

– The term "neuronal orientations" (or "trajectories") is used throughout but "axonal orientations" would be more suitable, as neurons are not imaged here.

– "… the signal is affected by all brain structures, not axons". It is true that the diffusion signal is affected by all tissue components, but that is not the main issue. What we use to extract orientations is not the signal itself, but the anisotropy (orientational dependence) of this signal. Not all tissue components contribute to this anisotropy the same way that myelin sheaths and axon membranes do, even if they contribute to the signal itself.

– There are several mentions of false positives as the problem with diffusion tractography methods. However no method has a fixed false positive rate, all methods have thresholds that can be adjusted to make their false positive rate as low or as high as one wants. It's the trade-off between the false positive rate and true positive rate that is difficult to improve, not the false positives themselves. You can always remove false positives, but the challenge is that you cannot do it without an excessive loss of true positives.

– In Methods: the in-plane resolution of the SAXS and SLI scans is provided, but what is the through-plane resolution? Is it the same as the section thickness (80 microns)?

– In Methods: there is a description of how the in-plane and through-plane orientations are computed in SAXS, but only how the in-plane orientations are computed in SLI.

– In Methods: it is unclear at what scale the angular errors are computed. Is it at the highest resolution among the modalities that are being compared, i.e., do you obtain as many values of the error as SLI-sized voxels?

– The use of the word "peak" without further qualifiers is likely to confuse the diffusion MRI audience. Here 2 peaks (in the SLI profile) = 1 fiber population, but in usual diffusion terminology 1 peak (in the diffusion/fiber ODF) = 1 fiber population.

– How are the "primary" and "secondary" orientations in a voxel determined for each modality? Are any steps taken to ensure that they match across modalities? Otherwise, you can imagine a scenario where the same fiber population ends up being the primary orientation in one modality but the secondary one in the other, and vice versa. This would overestimate the angular error between modalities. If the goal is to measure error as a difference between orientation angles, not amplitudes (as amplitudes mean different things in each modality anyway), then care must be taken to establish the correspondence of fiber populations between modalities.

– Registration with 12 degrees of freedom is affine. Linear and affine are not quite synonyms.

– It would be helpful to report the angular resolution of each technique as a function of through-plane inclination, e.g., what is the smallest angle between crossing fibers that can be accurately resolved by SLI when the fibers are in-plane or inclined?

– In Discussion: the paragraph on clearing and fluorescence microscopy should be updated to reflect the latest developments in that field. It is not "only feasible for smaller sample sizes", as clearing has now been demonstrated in samples as large as a whole slab of a human hemisphere. Also, the statement "it fails to disentangle densely packed nerve fibers" is not generally true, as this depends on the imaging resolution. The resolution of fluorescence microscopy can in principle be increased to the sub-micron level. It is true that the few studies that compared fluorescence microscopy of cleared tissue to diffusion MRI so far did not use state-of-the-art of these methods, but this is not due to an inherent limitation of the methods.

– In Discussion: while a single PS-OCT measurement gives only the in-plane orientation, the use of multiple measurements at multiple incidence angles to infer the through-plane orientation has been demonstrated in the literature.

– In Discussion: the statement that SAXS and SLI yield orientations with "a higher precision and smaller crossing angles" should be clarified. Higher/smaller than what? Which modality here is used as the reference that SAXS, SLI, and diffusion MRI are being compared to, in order to determine that the error is lower in one than the other?
