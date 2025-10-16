# Peer review - Round 1

Editors:
- Richard M Berry, University of Oxford , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.22140.011](https://doi.org/10.7554/eLife.22140.011)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Length-dependent flagellar growth of Vibrio alginolyticus revealed by real time fluorescent imaging" for consideration by eLife. Your article has been reviewed by four peer reviewers, one of whom, Richard M. Berry, is a member of our Board of Reviewing Editors and the process has been overseen by Richard Losick as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The authors have measured the rate of growth of the polar flagellum and sheath of Vibrio alginolyticus, using a vital dye, NanoOrange, whose fluorescence is low until it binds to the flagellar sheath (to a non-polar substrate). Thus, they can monitor changes in length without manipulating cells (e.g., washing and staining). This is a notable improvement. They show that the sheath is closely opposed to the filament. Presumably the sheath grows at its base where it is contiguous with the cell's outer membrane, but this is not known.

The experimental method and results add substantially to our understanding of flagellar filament growth, making the paper suitable in principle for publication in eLife. However, substantial improvements are needed in the data fitting and modelling, and in the discussion of how the results and model relate to existing models of flagellar-type export.

Substantial comments:

1) Data fitting: The 3-part piecewise linear fit to the speed vs. length data (Figure 2C) is not very convincing. In fact, Figure 4E (Discussion, first paragraph) shows a different fit to the data than 3 piecewise linear segments. More care is needed to discuss what can and cannot be determined by fitting the data and comparing it to the results of modelling.

2) Further to comment 1): the model appears to be over-specified. It needs to be demonstrated that (or discussed whether) the data can equally well be explained by single-file diffusion (Stern and Berg, 2013) or a chain model (Evans et al., 2013) without invoking the pushing mechanism. It is not realistic to assume that a flagellin subunit that has diffused away from the base of the filament is not allowed to diffuse back. Nor is it necessary to assume that the subunits are completely unfolded, since an α-helical chain is only about 1 nm in diameter, and therefore smaller than the 2nm pore.

Preferably the modelling should be improved substantially. At least the discussion of other models in the literature (particularly Evans et al., 2013 and Stern and Berg, 2013) should be much improved and the need for the new model features (driven by data), and their plausibility, discussed carefully and quantitatively.

Further details on this point:

Discussion, third paragraph: All that is needed to explain these data is that there is a length dependence of the transit rate, which becomes rate-limiting (= slower than injection) as filaments grow longer. The length dependence of the chain model (Evans et al., 2013) is not discussed, so nothing can be said for or against it.

Subsection “Simulating flagellar growth by a one-dimensional single-file diffusion model”, point 1: "SI appendix" – I could not find. Presumably this justifies the use of 56 nm as the length of the flagellin in the channel. Discuss this in the text. In particular, how can you have LS >1 (best fit is LS=12)? This requires the apparatus to push filaments further than their length! If there is an extended length and a semi-coiled length, this needs to be said. Subsection “Estimation of V. alginolyticus flagellin length”, last paragraph: a simple estimate of the contour length based on the dimensions of a peptide bond (~0.35 nm per a.a.) gives about twice this contour length. Is 56 nm really a good estimate? How does the model and fit depend upon this?

Subsection “Simulating flagellar growth by a one-dimensional single-file diffusion model”, point 1: LS as described is really equivalent to a loading length in units of 56 nm – better to quote this length directly so that it can easily be compared to the filament length in Figure 4. Naively I'd expect that the occupancy saturates and the rate slows when the filament is longer than the loading length. But it seems that this happens at filament lengths longer than the loading length. Discuss/explain.

Subsection “Simulating flagellar growth by a one-dimensional single-file diffusion model”, point 3: Is it realistic that (both?) touching units stop? Rather than diffusing more slowly as a larger object?

Subsection “Model parameter space search and the best fit”, last sentence: Figures do not show that there is a dependence of growth rate in the limit of long filaments upon "secretion force" (LS?). If this has been demonstrated, it should be shown. It's not clear that the model is expected to predict this, especially in the light of the previous comment which seems to preclude monomers pushing each other. But perhaps in fact stopping upon contact DOES provide a mechanism for pushing, as hitting injected monomers will ratchet the Brownian Motion of those further in.

3) Subsection “Fluorescent labeling of flagellar sheath for real time monitoring of flagellar growth”, third paragraph: discuss/explain/fix the conflict between statements that flagella are anchored to the surface and the assumption that they are 3D helices. Are they helices anchored at lowest points? Is there any evidence for this, e.g. 3D imaging? The 2D-3D correction is minor to the point of being unnecessary, but also it is wrong if filaments are fully anchored to the surface and thus in fact 2D.
