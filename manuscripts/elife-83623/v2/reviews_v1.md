# Peer review - Round 1

Editors:
- Giulia Zanetti, https://ror.org/02mb95055 Birkbeck, University of London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83623.sa0](https://doi.org/10.7554/eLife.83623.sa0)

This important work is of interest to the electron microscopy and cell biology communities. The field has long searched for a suitable method to combine the pristine preservation of vitrified samples with a volumetric imaging modality that reveals subcellular architecture at sufficient contrast for ultrastructural analyses. The authors describe here the use of novel ion beams for imaging cellular samples in three dimensions, concluding that one of the four plasma sources tested produces the highest quality images, allowing them to provide several recommendations for imaging conditions along with software for improving collected images. This approach should be very useful for addressing many biological questions.


---

# Peer review - Round 1

Editors:
- Giulia Zanetti, https://ror.org/02mb95055 Birkbeck, University of London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83623.sa1](https://doi.org/10.7554/eLife.83623.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Cryo-plasma FIB/SEM volume imaging of biological specimens" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Anna Akhmanova as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Alex de Marco (Reviewer #1); Alex J Noble (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) In its current form the paper does not show or discuss how plasma beams can mitigate charging artifacts (or not). The authors should add a comparison of charging artifacts with different sources (including Gallium) before computational correction. If this is not possible, they should remove the claim that they 'address these challenges using a cryogenic plasma FIB/SEM' (including charging). Similarly, the resolution measurements presented in the last supplementary figures do not relate to the use of plasma FIB/SEM in comparison with other beams.

2) Add a description of curtaining over time, in response to the following point from reviewer 1: "curtains appear over time when milling, and it would be useful to understand how different sources behave over time in FIB/SEM tomography sessions. The score is currently done from individual windows milled, which gives a good indication of the performance. However, it would make sense to check that the behaviour remains identical in an imaging setting and with the moving milling windows (or lines). This will show the counteracting effect to the redeposition and etching effect reported when imaging with the E-beam the milled face. "

3) Add data on milling resolution and beam cross-section in response to the following point from reviewer 1: "No detail about the milling resolution has been reported. Since different currents and beams have different cross-sections, it is expected to affect the z-resolution achievable during an imaging session. It would be useful to have a description of the beam cross-sections at the various conditions used and how or whether these interfere with the preparation."

4) Comment on the effects of imaging tilt angle on collection efficiency.

5) Explain the loss in resolution upon tilting the imaging angle, and the effect on contrast on the curtain edges (refer to reviewer 1 comment: "the generation of secondary electrons is known to increase with the increased tilt and to consider that the curtains (that are the prominent feature on the surface) are running along the tilt direction, it would be expected to see no contrast difference between the background and the edge of each curtain as the generation of secondary electrons will increase with tilt for both the edges and the background. Therefore, the contrast should be invariant, at least on the curtains").

6) Comment on reviewer 1 claim of suboptimal astigmatism correction, and on how this might affect the comparison between the different imaging tilt angles.

7) Discuss whether and how the contrast gained from the optimised approach using plasma FIB will allow interpretation and segmentation of biological features.

Can automated segmentation approaches be applied to the FIB/SEM volumes in similar ways to cryo-ET reconstructions?

Could the authors demonstrate that the features detected in the SEM can be used to target areas of interest for cryo-ET? If so, can they show structural preservation in the cryo-ET reconstructions?

Alternatively, the manuscript should more explicitly state that downstream correlative approaches are a potential application to be developed and tested in future work, and this is currently not possible.

Reviewer #2 (Recommendations for the authors):

Suggestions for Improvement:

The results presented in this manuscript are substantial on their own, and merit publication. However, as written, I worry that most readers will have a similar experience as me, reading excitedly, on the edge of our seats, waiting for the proof-of-concept that this approach is effective (and perhaps more effective than CLEM) for targeting and downstream cryo-ET imaging, and will come up somewhat disappointed that this is not demonstrated.

I propose that the authors choose one of two possible paths to address the weakness above. The first, more extensive albeit thorough option, would be to address this by collecting tilt series data and reconstructing tomograms of the same lamella imaged by plasma cryo-FIB/SEM, and demonstrate that cross-correlation between volumetric cryo-FIB/SEM and cryo-ET acquisition is possible without affecting image/reconstruction quality. This could be evaluated either qualitatively (e.g. integrity of membranes/filaments) or structurally (e.g., by solving the subtomogram average of the cellular ribosome). Ideally, the authors would select a target and demonstrate an advantage of cryo-FIB/SEM targeting over the more standardized cryo-fluorescence/CLEM approaches.

The second option would be to revise the manuscript text to more explicitly state upfront that this work is solely focused on evaluating the performance of cryo-FIB/SEM for volumetric imaging and ultrastructural analyses, and that future work will determine whether these are of sufficient quality to the image by cryo-ET. The authors sort of dance around the possibility that this approach could be used for downstream applications without sufficiently testing this, and therefore, I believe the intent of the article needs to be more explicitly addressed in the manuscript text. This would strengthen the merits of the article by allowing the reader to focus on the substantial improvements to contrast/imaging without feeling like something is "missing" at the end.

Finally, I suggest that the authors apply an automated segmentation algorithm to their volumetric data as a more unbiased and practical metric to evaluate the degree to which cryo-FIB/SEM imaging increases resolution, contrast, and interpretability of subcellular features at scale that would enable biological insight.

Reviewer #3 (Recommendations for the authors):

The authors present a method for using the exceptional SEM imaging capabilities of the Helios Hydra and new cryo-plasma FIB milling functionality on vitrified biological specimens to obtain contextual information on cells and tissues while potentially localizing areas of interest for subsequent lamellae generation. Significant results are presented where analyses of the cryo-pFIB performance are qualitatively and quantitatively displayed and exemplified, which is particularly useful for the field as pFIBs begin to be used worldwide. The authors show SEM optimization examples from bacterial cells, mammalian cells, and tissue along with features that may be expected in the resolution range of the instrument (10 nm – 10 µm). The authors clearly compare the four plasma sources, proceed with the best source partly based on a proposed curtaining score, then optimize imaging quality by tilting to 90 degrees relative to the SEM, analyze several samples, and introduce a U-net algorithm for cleaning up charging streaks.

I have experience with cryo-FIB/SEM and cryo-ET/EM. Overall, I think this manuscript is timely and practical, given that cryo-pFIB/SEMs are anticipated to be adopted widely beginning in 2023, and should be published.
