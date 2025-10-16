# Peer review - Round 1

Editors:
- Sjors HW Scheres, MRC Laboratory of Molecular Biology United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.97227.3.sa0](https://doi.org/10.7554/eLife.97227.3.sa0)

This valuable work presents the latest version of CTFFIND, which is the most popular software for determination of the contrast transfer function (CTF) in cryo-electron microscopy. CTFFIND5 estimates and considers acquisition geometry and sample thickness, which leads to improved CTF determination. The paper describes compelling evidence that CTFFIND5 finds better CTF parameters than previous methods, in particular for tilted samples (e.g. for cryo-electron tomography) or where thickness is an issue (e.g. cellular samples, or electron microscopy at low voltages).


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97227.3.sa1](https://doi.org/10.7554/eLife.97227.3.sa1)

This work presents CTFFIND5, a new version of the software for determination of the Contrast Transfer Function (CTF) that models the distortions introduced by the microscope in cryoEM images. CTFFIND5 can take acquisition geometry and sample thickness into consideration to improve CTF estimation.

To estimate tilt (tilt angle and tilt axis), the input image is split into tiles and correlation coefficients are computed between their power spectra and a local CTF model that includes the defocus variation according to a tilted plane. As a final step, by applying a rescaling factor to the power spectra of the tiles, an average tilt-corrected power spectrum is obtained used for diagnostic purposes and estimate the goodness of fit. This global procedure and the rescaling factor resemble those used in Bsoft, Warp, etc, with determination of the tilt parameters being a feature specific of CTFFIND5 (and formerly CTFTILT). The performance of the algorithm is evaluated with tilted 2D crystals and tilt-series, demonstrating accurate tilt estimation in general.

CTFFIND5 represents the first CTF determination tool that considers the thickness-related modulation envelope of the CTF firstly described by McMullan et al. (2015) and experimentally confirmed by Tichelaar et al. (2020). To this end, CTFFIND5 uses a new CTF model that takes the sample thickness into account. CTFFIND5 thus provides more accurate CTF estimation and, furthermore, gives an estimation of the sample thickness, which may be a valuable resource to judge the potential for high resolution. To evaluate the accuracy of thickness estimation in CTFFIND5, the authors use the Lambert-Beer law on energy-filtered data and also tomographic data, thus demonstrating that the estimates are reasonable for images with exposure around 30 e/A2. While consideration of sample thickness in CTF determination sounds ideally suited for cryoET, practical application under the standard acquisition protocols in cryoET (exposure of 3-5 e/A2 per image) is still limited. In this regard, the authors are precise in the conclusions and clearly identify the areas where thickness-aware CTF determination will be valuable at present: in situ single particle analysis and in vitro single particle cryoEM of large specimens (e.g. viral particles).

In conclusion, the manuscript introduces novel methods inside CTFFIND5 that improve CTF estimation, namely acquisition geometry and sample thickness. The evaluation demonstrates the performance of the new tool, with fairly accurate estimates of tilt axis, tilt angle and sample thickness and improved CTF estimation. The manuscript critically defines the current range of application of the new methods in cryoEM.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.97227.3.sa2](https://doi.org/10.7554/eLife.97227.3.sa2)

This paper describes the latest version of the most popular program for CTF estimation for cryo-EM images: CTFFIND5. New features in CTFFIND5 are the estimation of tilt geometry, including for samples, like FIB-milled lamellae, that are pre-tilted along a different axis than the tilt axis of the tomographic experiment, plus the estimation of sample thickness from the expanded CTF model described by McMullan et al (2015). The results convincingly show the added value of the program for thicker and tilted images, such as are common in modern cryo-ET experiments. The program will therefore have a considerable impact on the field.

Comments on revised version:

My comments have been addressed adequately.
