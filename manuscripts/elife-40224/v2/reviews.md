# Peer review - Round 1

Editors:
- Mark Schira, University of Wollongong Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.40224.023](https://doi.org/10.7554/eLife.40224.023)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Bayesian Analysis of Retinotopic Maps" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Mark Schira as the Reviewing Editor and Reviewer #3, and the evaluation has been overseen by Joshua Gold as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: D. Samuel Schwarzkopf (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision combining the comments from all three reviewers to help you prepare a revised submission.

Summary:

The manuscript by Benson and Winaver introduces a very sophisticated toolbox that combines a prior with fMRI scanning to estimate the retinotopic layout of a large set of visual areas for an individual subject. This work is an extension of previous work from the first author. The authors previous work has proven very successful and useful, and there is little doubt that the current work will be very useful, too. These techniques could theoretically be very beneficial in situations where only minimal data can be collected (elderly, children, patients). Since these Bayesian maps also contain automatic delineation, they could be very useful for reducing experimenter biases in manual delineation, which is still the standard to the field. Of course, this comes with the caveat of reduced flexibility, a potential systematic bias and that the delineation of many areas beyond V3 remains controversial. The auto-delineation is only as good as the atlas used as prior – but even then, the atlas procedure would enhance the reproducibility of findings. In general, this method is solid, cutting edge, and provides a significant improvement over previous procedures.

Essential revisions:

The overall assessment of the manuscript from all three reviewers is quite positive, but they raise a set of concerns, as follows.

1) There were questions about how well the methods can deal with extreme individual variability. As it stands, the manuscript presents a detailed and informative analysis of variability in the anatomical and functional features of visual field maps. The ability to characterize the extent to which variations in retinotopic organization are due to anatomical differences versus differences in the structure-function relationship is remarkable. However, the discussion on how this method would allow the quantification of more extreme and unexpected departures from expected topographical organization should be expanded. There exist several reports showing how clinical conditions (for example: achiasma, hemi-hydranencephaly and albinism) can affect the topographic organization of areas in early visual cortex. It should be discussed what results the method would provide if presented with such anomalies, expected or unexpected. At the present time there is a brief suggestion in the introduction about clinical applications, but we believe it should be expanded in the Discussion.

2) On a related note, the Bayesian inference maps do a good job at revealing individual differences in the functional architecture of visual cortex. However, while the deviations from a validation data set are small for these Bayesian maps, it would be informative to understand under what situations this technique fails. It is unsurprising that the noisy “Data alone” or the “Anatomy alone” maps contain errors – but could the authors elaborate on any systematic errors the Bayesian method has? Do most errors originate in the prior or the empirical retinotopic maps?

3) In a proper Bayesian formulation, the effect of the evidence on the posterior should depend on both the strength of the evidence but also on the certainty of the prior, which would presumably vary with the visual area. Our understanding of the methods was that the prior was essentially weighted equally at all locations. However, the certainty of the prior maps is arguably better for V1 than the higher areas (this is more of a problem for the higher regions beyond V3 and the authors already acknowledge that this aspect is still experimental).

Moreover, there was some concern that, as more data are introduced the estimated maps do not seem to improve much further. We understand and appreciate the comments from the authors that they believe this as a strength rather than a bug, because even excessive amount of data might not hold the ground truth. However, it still is a concern: under Bayesian optimization, the uncertainty of the data estimate should continue to get smaller with increasing repetition. This does not seem to be the case, instead after a small amount of data the model 'refuses' to make any further compromises. Further discussion of this point might be useful.

4) The authors should be much clearer and more upfront what the novel contribution of this work is, as opposed to previous work. From our judgment the improvements are substantial, but the reader has to piece together what is based on previous work and what novel, hence a succinct rapport early on would be much appreciated. Along a similar line, we believe the manuscript would benefit from being made more concise.

5) The authors already discuss this to some degree, but of course there is no proper ground truth in these analyses. They used a large retinotopic data set as validation data, which seems entirely reasonable. But this has some implications for the individual differences in functional architecture that this analysis reveals: offsets between cortical folding structure and retinotopic organisation could be because of errors in alignment between the functional scans and the cortical sampling. Even a small offset could masquerade as a shift in visual field borders. Thus, some differences may reveal not individual differences in maps but in the idiosyncrasies in image alignment.

6) We were a bit confused about the pRF size data. Both the pattern and magnitude of results in the Bayesian inference map don't match the empirical pRF data very well. pRF sizes in the actual data are much greater and differ systematically between V1, V2, and V3. The Bayesian data have smaller pRFs (intercept at 0) and V1 and V2 are essentially indistinguishable. The authors should discuss those discrepancies and other issues that might affect pRF size, such as fixation stability and the size of the centre-surround configuration.

Moreover, the model predicts visual field positions not included in the training data and returns an estimate of pRF size. While the fit between the inferred and the validated eccentricity is remarkable, the plot on the wide-field data is based on a single participant. This limitation should be stressed in the text as a cautionary note. Extrapolation is a notoriously hard problem. The quality of the data plays a major role. A naïve participant, with not-so-stable fixation, and maybe moving in the scanner could result in a different extrapolation trend.

7) Inter-individual differences that remain after the first anatomical alignment step are characterised as variability in the structure vs. function relation, and they may or may not largely be that. However, no alignment process is optimal and some of the remaining variance is undoubtedly due to insufficiencies of the anatomical alignment process. The alignment process used is based on the nice work from Hinds et al., but one does wonder if the large dataset used may not allow improvements to this process – and if only through fine tuning of some parameters.

8) Figure 9 is very hard to decipher, it needs more space and thinner lines and different rendering of the error range. It also seems to suggest that the magnification curves of V2 and V3 cross that of V1 at around 1.5-3 degrees. Crossing of magnification curved was first shown by Schira et al. (2009) and explained by Schira et al. (2010). Your data seems to suggest the crossing is at higher eccentricities than the 0.7-1 degree reported by Schira et al., which is possible but deserves some discussion. Specifically, since measured and inferred maps disagree on this value.
