# Peer review - Round 1

Editors:
- Michael L Dustin, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64709.sa0](https://doi.org/10.7554/eLife.64709.sa0)

You have developed and validated a new method for measurement of nanoscale height of macromolecules that can be non-uniformly distributed on irregular surfaces. Such samples are common in biology, which will make this a valuable approach to achieve super-resolution results for samples where this would have not been possible previously.


---

# Peer review - Round 1

Editors:
- Michael L Dustin, https://ror.org/052gg0110 University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64709.sa1](https://doi.org/10.7554/eLife.64709.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Binding site localization on non-homogeneous cell surfaces using topological image averaging" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Michael L Dustin as the Reviewing Editor and Reviewer #1 and Erdinc Sezgin as Reviewer #2, and the evaluation has been overseen by Olga Boudker as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

You describe a method to measure nanoscale height of fluorophors above a surface that can be rendered with a distinct fluorophore, but doesn't need to be radially symmetric, as for recently published CSOP method. This was applied to measurement of S. pyogenes M protein.

There were a number of technical concerns about the calibration and validation of the method and the comparison to CSOP.

Essential revisions:

1. Since the major focus of this work is applying the method of spatially averaging of two fluorescent signals to non-spherical surfaces, it is critical that the image analysis method (using Hough transforms, edge detection, filtering, etc) be validated with known non-spherical objects to confirm that it is working as expected. Currently, it is unclear for what range of sizes and shapes the approach is accurate and what potential sources of error might be. Both experiments and simulated data could be used to evaluate performance of the analysis algorithm.

2. The authors indicate they use 100nm beads to correct for chromatic aberration, but chromatic aberrations can increase as the imaging plane moves away from the glass surface. Do the dual-labeling experiments shown in Figure 3 – Supplementary Figure 1 include correction of chromatic aberration based on the 100nm beads? Is so, then it appears that chromatic aberration needs to be corrected at the image plane rather than the glass surface. How is this difference observed in the dual labeling experiment accounted for in the image analysis procedure?

3. How does the reported accuracy depend on the number of cells averaged and the amount of fluorescent antibody on each cell? It would be interesting to see a plot of the height uncertainty per cell as a function of the antibody fluorescence intensity (as a proxy for amount of antibody). Since the reported ~5nm resolution is for averages across 37-55 independent cells, would averaging more cells give higher precision (and does averaging fewer cells give lower precision)?

4. How does fixation affect the measurements? Can the method be used on unfixed cells, and what is the localization uncertainty for unfixed samples? Also, is the uncertainty in localization of the ligand signal due to antibody fluctuations and labeling location included in the analysis?

5. In the comparison with CSOP (Son, PNAS, 2020), it would be helpful to first demonstrate both techniques on spherical objects, in order to confirm that the use of CSOP is consistent with published results and to evaluate how the new method compares for spherical objects (presumably it should be equivalent). There is also not a calibration test in the study. There should be a very well controlled calibration samples to evaluate the accuracy as well as dynamics range. The authors could use swelled spherical RBC with the same DNA based height standards examined in Son et al. in GUV. CSOP and the new method could then be fairly compared, calibrated and then applied to the same height standards on a biconcave RBC, which would test the new method on a non-spherical object.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your revised article "Nanoscale binding site localization by molecular distance estimation on native cell surfaces using topological image averaging" for consideration by eLife. Your article has been re-reviewed by the same 3 peer reviewers as in the initial review, including Michael L Dustin as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Olga Boudker as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Erdinc Sezgin (Reviewer #2).

The reviewers all felt that the efforts you have made are helpful, but still were not clear on the height accuracy of the experimental data needed to be useful for relevant measurements on biological molecules at surfaces,. These revisions may not require new experiments, but will require clarification of the data sets, some revisions to the simulated data shown, and additional analysis of the signal requirements and sources of error. The Reviewing Editor has drafted this to help you prepare a second revised submission.

Essential revisions:

You have provided additional simulations and experimental data in the revised manuscript, but you have not fully addressed the essential revisions as the most significant issue for any new method, the experimental validation, is not complete. Showing that an algorithm can obtain height measurements on simulated data demonstrates the performance of the algorithm but is not true experimental validation of the technique. Specifically, the authors need to confirm that molecules of known heights can be correctly measured with the claimed precision. Furthermore, the reported experimental height uncertainties are significantly different from the simulated uncertainties for variable shapes, which raises fundamental questions about other sources of error.

1. You have not shown that experimental measurements and the analysis algorithm can correctly capture the height of a known molecule (e.g. DNA) on a known surface (e.g. a sphere). The measurement of DNA height on the non-spherical surface of an RBC is not meaningful until you can show that you can accurately measure the height of that DNA on a known surface geometry. It is the equivalence of those two height measurements – one on a known surface and one on a variable surface – that would give confidence that you have a new methodology for obtaining accurate height measurements on non-spherical and non-uniform surfaces. One suggestion was to use a swelled erythrocyte in a 50% isotonic solution as a spherical object, but a more standard spherical object would be a GUV or uniform glass bead. But you need experimental data on spherical object comparing CSOP and Site Localization.

2. The simulations in Figure 2 are a useful addition to the manuscript and provide a quantitative characterization of the algorithm for idealized images, but the results in Figure 2 show uncertainties much less than that of most experimental measurements in the manuscript. For example, when you say the largest deviation from true distance was 10%, its not obvious what data this claim is based on. The worst case seems to be a 5 nm deviation from true distance, does this mean that the simulated structure was 50 nm in height? Percentage of deviations should be clearly shown and explained. Furthermore, what are the dominant sources of localization uncertainty if the contribution from patchy and non-spherical surfaces is normally much smaller than 5nm? The precision of fluorescence localization methods typically depends on the number of photons collected. Is that true for this method?

3. To report uncertainty in your height measurements, you use standard error of the mean rather than standard deviation, which is the more appropriate measure in our collective view. Since uncertainty in height measurement is based on molecular averages on an individual particle basis (affected by, e.g., number of photons collected for molecules on that particle, how thoroughly chromatic aberration is corrected, etc), measuring more particles does not correct those issues for non-random sources of error (e.g. chromatic aberration). It is also unclear to us how removing negative height values from the population of measurements is justified when calculating means if there is no independent reason to reject those measurements as invalid, wouldn't removing only the negative outliers skew the result and to larger errors in the absolute height? Regardless, were you to use standard deviation, rather than standard error of the mean, the reported uncertainty would be significantly larger, which would necessitate a effort to find sources of error and to reduce these as much as possible to make the method useable.

4. While the motivation to measure heights of molecules on patchy, non-spherical surfaces is a good one it should be made clear that CSOP is only valid for spherical objects and it should not be applied to non-spherical objects. There is no reason to show simulated data that CSOP fails on non-spherical objects as applying CSOP to a non-spherical object, even in a simulation, is not appropriate. The important comparison between CSOP and Site Location is that they should both achieve 1 nm measurement accuracy for height measurements on a spherical object, with Site Localization striving to preserve this accuracy on on non-spherical surfaces.
