# Peer review - Round 1

Editors:
- Werner Kühlbrandt, Max Planck Institute for Biophysics , Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.00461.010](https://doi.org/10.7554/eLife.00461.010)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for choosing to send your work entitled “Ribosome structures to near-atomic resolution from thirty thousand cryo-EM particles” for consideration at eLife. Your article has been evaluated by a Senior editor and 3 reviewers, one of whom is a member of our Board of Reviewing Editors.

The following individuals responsible for the peer review of your submission want to reveal their identity: Werner Kühlbrandt (Reviewing editor); Niko Grigorieff (peer reviewer). The Reviewing editor and the other reviewers discussed their comments, and the Reviewing editor has assembled the following summary to help you prepare a revised submission.

Bai et al report the cryo-EM structure of the yeast 80S ribosome at close to 4 Å resolution, determined from images recorded with the new direct electron detection Falcon camera. An essential modification of the camera readout that is not yet commercially available enabled the recording of dose-fractionation movies. By aligning and averaging individual subframes from these movies, the authors were able to overcome the effects of beam-induced specimen movement, which has been the most serious limitation in high-resolution data acquisition by cryo-EM until now. Remarkably, movies of 35,000 particles or less recorded in a single session were sufficient to achieve this impressive result.

Similar cameras have been developed by Gatan and the Direct Electron company. The high detective quantum efficiency of these innovative devices makes them far superior to the widely used scintillator-based CCD cameras and even to film, which has been the medium of choice for high-resolution cryo-EM data recording. The new direct electron detection cameras are set to revolutionize cryo-EM, and the present study is the first to take advantage of their full power to determine the structure of an important macromolecular complex at high resolution.

An important factor contributing to this success is new software. Scheres' powerful Bayesian approach already proved in the RELION program to excel in the job of sorting projections from heterogeneous samples. This frame-by-frame particle alignment had already been studied by Brilot et al (2012) and Campbell et al. (2012) but with limited improvement in resolution. Scheres and coworkers prove the superiority of their statistical framework over more traditional methods, bringing the resolution of single-particle methods into a new territory. The paper requires only minor modifications, as below.

1. The concept of a “probabilistic prior” will be unfamiliar to most readers and requires a brief explanation. How were the widths of the priors for the statistical movie processing chosen? Did the authors perform some kind of optimization, maybe by observing improvements in the gold-standard FSC? How did the authors take into account the observation that the beam-induced movement per dose unit is larger at the beginning of an exposure and smaller towards the end?

2. Comments on image processing:

* What was the beam tilt in the centre of the illuminated area, and how was it measured or estimated? How much beam tilt would be acceptable at 4 Å resolution? Can you exclude that the resolution was limited by beam tilt?

* Please provide details on the classification (window size, number of classes, regularization factor, how many cycles?).

* Code for this novel alignment procedure should be provided.

* It would be desirable, and a great asset for the community, if the data would be deposited as a benchmark that allowed the testing of other algorithms. EMDB now allows for such depositions.

3. Comments on figures:

* Figure 1: The red and green dots reinforce the (false) notion that the particle moves by this amount. The underlying vector with exaggerated length is okay.

* Figure 2G: there should be a panel 2G (or a separate figure) showing complete density maps of the 80S ribosome for the three modes of frame integration. Many readers are familiar with the appearance of the ribosome in various reconstructions and reproduction of the full maps would provide a good qualitative appreciation of the results.
