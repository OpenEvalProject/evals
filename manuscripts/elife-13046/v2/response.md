# Author response - Round 1

Authors:
- Radostin Danev ([ORCID: 0000-0001-6406-8993](https://orcid.org/0000-0001-6406-8993))
- Wolfgang Baumeister

## Response text

DOI: [10.7554/eLife.13046.020](https://doi.org/10.7554/eLife.13046.020)

Essential revisions: 1) The 2015 PNAS paper of Danev et al. provide hard data for beam-induced phase shift of a function of dose (nC) for a specific VPP. In the Results and Discussion section the authors write that the "phase plate versus number of images has to be calibrated in advance", like they did in the PNAS paper. Assuming that this calibration is solely a function of dose and not of time (e.g., is there any decay of the phase shift during the time the data acquisition of the next hole is being setup?), such calibration could have been done with very little effort. Such data are important for the reproducibility of their own experiments as well as for future work done in other labs: could they still be added?

We measured and added phase shift versus image number/total dose data as Figure 3 in the revised manuscript.

2) Figure 5: one should plot the (natural) logarithm of the number of particles against 1/d2, the inverse of the square of the resolution. That way, one can fit straight lines through the red and blue curves to obtain B-factors, which can then be compared directly. 3) The smaller subsets in Figure 5 were obtained based on a sorting (in RELION) of the particle images. This should be replaced by random subsets of varying size, as sorting the best particles into the smallest subsets may have the undesired effect that the resolution for the smaller subsets is relatively better.

We recalculated the resolution versus particle number data using random subsets of particles and replaces the original data. The results are plotted in Figure 6A in the revised manuscript. We also plotted the ln(N) vs 1/d2 in Figure 6B and fitted linear regions of the data to measure the B-factor. As described in the text we observed two regions with approximately twofold change in the B-factor. Unfortunately we could not provide a plausible explanation for the variation of the B-factor.
