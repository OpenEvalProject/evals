# Peer review - Round 1

Editors:
- Edward H Egelman, https://ror.org/0153tk833 University of Virginia United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80980.sa0](https://doi.org/10.7554/eLife.80980.sa0)

The work details a valuable method of defocus corrected large area cryo-EM (DeCo-LACE). The data-acquisition approach is highly complementary to the research group's previous work of using high-resolution 2D template-matching (2DTM) to identify macromolecular complexes in dense and heterogeneous cellular specimens. Overall, the data presented shows that DeCo-LACE is a solid approach to locating large ribosomal subunits in FIB-lamella at scale.


---

# Peer review - Round 1

Editors:
- Edward H Egelman, https://ror.org/0153tk833 University of Virginia United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80980.sa1](https://doi.org/10.7554/eLife.80980.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Defocus Corrected Large Area Cryo-EM (DeCo-LACE) for Label-Free Detection of Molecules across Entire Cell Sections" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Richard Aldrich as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Thomas G Laughlin (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

The authors have developed a method aimed at characterizing particles found in wide-view image montages from cellular sections. While it might be seen as an incremental advance over their previous publication on template-matching, enabling users to be able to examine wide fields of view has importance and significance for addressing cell biological questions. There are several limitations to the present study, however, that should be addressed in a revised paper:

(1) They have only used the large ribosomal subunit for this study. They should discuss the MW of this object and the fact that it has a significant fraction of nucleic acid, increasing the contrast. They might speculate how the method would work for objects with lower MW and no nucleic acid content.

(2) While the method is proposed as a faster alternative to cryo-ET, the computational demands seem prohibitive. Can they speculate on how the method could be accelerated (and not just by adding more processors)? Given the computational bottleneck, can they provide recommendations to readers on when the presented approach is appropriate?

(3) The manuscript could potentially be improved by a more thorough explanation of the resolution regime to which the 2DTM signal-to-noise ratio (SNR) values are most sensitive. When would one anticipate aberrations like a coma to become problematic?

(4) Fitting of particle defocus allows detection of the Z-height for each large ribosomal subunit. Could the authors estimate what is the precision of the detection of Z-height in their experiment and how it depends on the thickness of the lamella (˜150…250 nm in this case).

(5) How close to the top or the bottom end of the lamella can a ribosome subunit be detected? Can it be detected when it is partially milled away? Do the molecules in the "middle" of the lamella correspond to higher SNR?

Reviewer #1 (Recommendations for the authors):

The manuscript could potentially be improved by a more thorough explanation of the resolution regime to which the 2DTM signal-to-noise ratio (SNR) values are most sensitive. When would one anticipate aberrations like a coma to become problematic?

Lines 156-158: How does the inclusion of the non-illuminated areas, even when filled with Gaussian noise, impact the estimate of the false-positive rate? Could this be the source of the apparent overestimation of the false-positive rate?

Ln 189: "exclusively".

Lines 220-224: Are the authors able to incorporate the effect of coma in the 2DTM routine to see its effect on results or perform simulations on the effect coma has on the SNR values? When would one expect a coma to become limiting/negatively affect the SNR? Is it near/beyond the Nyquist of this data set anyway?

Lines 267-269:

Reference 27 (Cash et al., 2020) detailed a case of substantial beam image shift which resulted in |0-6| mrad of beam tilt (up to 20 μm image shift) and limited the reconstruction to 4.9 Å. In Cheng et al., JSB, 2018 the authors could obtain ~3-3.5 Å reconstructions in light of |1.3| mrad beam tilt (~5-8 μm image shift), which is likely closer to the maximum amount of beam tilt being applied in the presented study.

Lines 270-272:

Can the authors elaborate their explanation on the impact of coma on SPA vs 2DTM? I would have thought that a coma would have less of an impact on SPA data through averaging compensatory directions and more of an impact on 2DTM by making the reference project less similar to the experimental image.

Line 342:

Why were images resampled to 1.5 Å? Was this to include information beyond the physical Nyquist? If so, has this been shown to improve the 2DTM results?

Figure-4 supplement-1:

Panels D and E are not described in the legend. Are micrographs cropped to the illuminated area inscribed before 2DTM or is the entirety of the unilluminated area, filled with Guassian noise, included?

Figure 7:

Remove/replace "electron" in the first box.

Reviewer #2 (Recommendations for the authors):

The manuscript is technically excellent and well written. I have several important questions that are still not addressed in the current version of the manuscript.

1. Fitting of particle defocus allows detection of the Z-height for each large ribosomal subunit. Could the authors estimate what is the precision of the detection of Z-height in their experiment and how it depends on the thickness of the lamella (˜150…250 nm in this case).

2. How close to the top or the bottom end of the lamella can a ribosome subunit be detected? Can it be detected when it is partially milled away? Do the molecules in the "middle" of the lamella correspond to higher SNR?

3. As all the research using this approach is performed on ribosomal subunits, in order to make the method more general – it should also work on other macromolecules. Could the authors discuss the potential lower limits for detection in FIB lamella?
