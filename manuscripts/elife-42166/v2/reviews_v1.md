# Peer review - Round 1

Editors:
- Edward H Egelman, University of Virginia United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.42166.029](https://doi.org/10.7554/eLife.42166.029)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "RELION-3: new tools for automated high-resolution cryo-EM structure determination" for consideration by eLife. Your article has been favorably reviewed by three peer reviewers, including Edward H Egelman as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by John Kuriyan as the Senior Editor. The following individuals involved in review of your submission have also agreed to reveal their identity: John L Rubinstein (Reviewer #2); Eva Nogales (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

All reviewers agreed that this paper would be an excellent contribution to the Tools or Resources category in eLife, and would be helpful to many people currently using cryo-EM as well as those hoping to use cryo-EM. The new algorithms described in the paper, including CTF/Defocus refinement of individual particles, Ewald sphere correction and beam-tilt correction, appear promising, and it is clear that Relion 3.0 will be an important software package for many people. No major concerns were raised, only minor points that can be easily addressed.

Minor points:

1) The authors estimate the resolution in some instances to a hundredth of an Å. This level of precision makes no sense in cryo-EM, where the FSC curve is never monotonic, and results are easily influenced by masking. In addition, Sjors recently wrote in a CCPEM forum that "we have seen artificially high FSC curves in cases of strong 'rotational smearing' of the particles due to extremely broad posterior probability functions of the orientations." So simply smearing the map can improve the FSC, as previously noted by Grigorieff. Thus, defining the FSC resolution, which can be easily altered by tenths of an Å by masking and smearing, to a precision of a hundredth of an Å defies common sense. Therefore, 3.49 should be 3.5, and 3.11 should be 3.1.

2) Figure 1 needs the y-axes to be labelled in both parts. Without knowing precisely what is being plotted, it is confusing that the function oscillates about zero (I had guessed correlation, but that would be positive everywhere there is correlation).

3) CTF refinement: It might be useful to add a few statements regarding the performance of the per-particle CTF refinement algorithm when dealing with i) particles of different size (e.g. are smaller particles less reliably fit), ii) reconstructions of different resolution (e.g. will using a low-resolution reference structure lead to degraded defocus estimates; if so, at which resolutions has this been observed?), and iii) micrographs with different numbers of particles. Regarding the last point, it appears that the algorithm does not use the particle population of a micrograph to improve the accuracy of CTF fitting, e.g. by fitting a plane or to avoid outliers (e.g. Figure 4, supplement 1). This would imply that the number of particles per micrograph does not play a role in the per-particle use case – is this correct?

Also, since the refined map is needed for CTF refinement, how reliable is the procedure with reconstructions at medium resolution (in the 5-7Å regime)? Finally, have the authors compared their method with the local CTF estimation method done using Gctf, where no input map is needed?

4) Ewald sphere correction: Could the authors give the radius of the test specimen used, and the resolutions at which Ewald sphere curvature becomes limiting for this radius, according to previous estimates in the literature (e.g. by DeRosier, Grigorieff, and others)?

5) Automated data exploration: The script failed to select the correct structure because it used, at equal resolution, the largest class. Did any of the other refinement parameters point to the correct structure (e.g. translation or rotation accuracies from the alignment)?

6) Β-galactosidase: The comparison to previous reconstructions from the same and other groups is insightful and the emphasis on using proper validation statistics is important.
