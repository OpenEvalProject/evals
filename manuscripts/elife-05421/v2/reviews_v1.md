# Peer review - Round 1

Editors:
- Stephen C Harrison, Harvard Medical School, Howard Hughes Medical Institute , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.05421.021](https://doi.org/10.7554/eLife.05421.021)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Enabling X-ray Free Electron Laser Crystallography for Challenging Biological Systems from a Limited Number of Crystals” for consideration at eLife. Your article has been favorably evaluated by John Kuriyan (Senior editor) and three reviewers, one of whom, Stephen Harrison, is a member of our Board of Reviewing Editors.

The Reviewing editor and the other reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

The manuscript represents a substantial advance in the processing of XFEL diffraction data, through the introduction of postrefinement methods. Although it provides no direct comparison with other procedures (from Kabsch or White), data for the three test cases considered show considerably improved statistics. Moreover, the total number of frames required to compile a data set is very much smaller than with the so-called “Monte Carlo” method. The manuscript is well written and thorough (especially in the provision of equations in the Methods section). A possible, but forgivable, omission was the inclusion of a more challenging test case that could demonstrate a genuine increase in the effective resolution of a dataset from the new procedures.

The reviewers had the following modest concerns, questions and requests:

A. Theory:1) Sphere model for Eoch. The basic idea of postrefinement is that the ratio of the intensity of a partially recorded reflection to its value in a properly corrected and scaled reference data set is a very sensitive measure of the orientation and unit-cell parameters of the crystal and of diffracting-range parameters such as mosaic spread, energy dispersion, and range of unit-cell parameters within the diffracting volume. Equations (1) and (2) summarize the application to XFEL stills, with Eoch as the critical function requiring definition and evaluation. The authors choose a sphere model for Eoc, which is reasonable for cases in which the diffracting range is dominated by energy dispersion and unit-cell variation. For a mosaic crystal with no variation in unit cell across the diffracting volume and mosaicity higher than the energy dispersion, the reciprocal-space shape of the diffraction spot will not be spherical; it will intersect the Ewald sphere as an arc, since the Bragg angle and hence the distance of any component of the spot from the origin of reciprocal space will be (ex hypothesi) invariant, while the range of azimuthal angles of the spot on the detector will depend on the mosaic spread (assumed to be non-zero). With cryopreserved crystals, the assumption that a combination of unit-cell variation and energy dispersion dominates is almost certainly a good one, but it may not hold for tiny crystals at ambient temperature in an injected beam. Anisotropy of some of the parameters may also make other shapes a better fit. The approach in the paper is, of course, generalizable to other shapes (with much “hairier” expressions for Eoch and its derivatives). In any case, the authors should discuss the assumptions that go into the sphere approximation.

2) Lorentz factor. A clear discussion of Lorentz factor is important, to give the paper full archival value as a complete treatment of the intensity correction problem. Formally, there is no Lorentz factor for a still. This statement is easy to prove using the “sinc” formula given in Equation 1 of the cited article by Kirian et al. (2010). If two different relps lie precisely on the Ewald sphere, then the value of the sinc function is simply equal to the square of the number of unit cells, regardless of resolution or any other geometric factor. All that remains is the polarization (which is not a Lorentz factor) and the incident intensity, which is the same for every spot. The only terms that remain hkl-dependent are the structure factor F, and the solid angle subtended by a pixel. The latter has some semblance to a Lorentz factor, but disappears upon pixel integration if the detector is corrected to be spherical. The spreading out of the spot due to mosaic spread and spectral dispersion in reciprocal space could be considered a Lorentz factor, but in the context of the present work, this should be part of the “partiality”.

B. Questions:

1) In the test cases, the data quality for the subset of images (e.g. 2,000 for thermolysin) is clearly lower than using the entire dataset. Is there any indication of convergence when considering data quality metrics vs the number of images included, or does inclusion of all images always give the best data?

2) The Discussion section is relatively brief. Even with the improved processing, the data quality falls significantly short of what would be expected for conventional SR rotation data collection. Does the analysis provide any pointers to the remaining major sources of error?

3) Figure 6 (myoglobin data): For the high resolution terms, post-refinement appears to make the data worse as judged by the R and Rfree metrics. Why?

4) There are many fewer spots per image for thermolysin than for the other two datasets. What is the definition of a “spot” in this context?

5) It is not clear if a separate resolution limit is applied to each image during the final merging step. Can this be clarified?

6) Figure 9: What is the second peak that is clearly visible when all images are used? Perhaps it would be useful to quote the largest “noise” peak as well as that for the Zn.

7) Table 3: The hydrogenase data were collected with a seeded beam, and yet the term representing the energy dispersion γe is larger than that for thermolysin and almost as large as for the myoglobin data. Why?

C. Request:

The paper should have a complete list of all the parameters and symbols in the equations and their definitions (as Acta Cryst may still do and certainly used to do). Many of the parameters (such as theta(x) and theta(y)) were defined only in the figures, and it might indeed clutter the text to define each of them immediately after their first appearance in equation (1).
