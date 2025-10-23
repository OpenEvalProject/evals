# Peer review - Round 1

Editors:
- Kristin Scott, University of California, Berkeley, Berkeley , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.25690.035](https://doi.org/10.7554/eLife.25690.035)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Fast two-photon imaging of subcellular voltage dynamics in neuronal tissue with genetically encoded indicators" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Eve Marder as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper presents a novel GEVI, ASAP2s and its application in a variety of contexts: cultured neurons, human iPSC-derived cardiomyocytes, Drosophila visual system, and organotypic slice culture. The authors apply random-access point-scanning 2P microscopy to achieve high time resolution and decent SNR in the Drosophila and organotypic slice culture systems. The technical quality of the work and the presentation are high. Overall, this is a well-executed study, showing the utility of ASAP2s in a variety of systems. Importantly, they show modest, but real improvements to enable 2P functional imaging.

Essential revisions:

1) One main concern is that it is not at all clear what the relationship is between this report, featuring ASAP2s, and the 2016 study by a similar group of authors (Cell, 2016, 166, p245) that discloses ASAP2f. Clearly the mutations are different, but there is no comparison between 2s and 2f. Since this is largely the same group of authors, they should have access to the appropriate DNA constructs and even the required genetically-modified organisms. At the very least, some discussion of the relative benefits of 2s vs. 2f should be discussed. One does not need to be the clear "winner" – it's good to have a variety of methodologies to employ, but this paper does not clear up the confusion over which plasmid a prospective user would request. These considerations should be addressed: ideally with experiments and at the very least with a discussion. There should also be comparisons to the other "state of the art" indicator, mAce-Neon, out of the Schnitzer efforts. Since there is a shared co-author on these studies, this should be feasible.

2) The new GEVI is somewhat more sensitive and somewhat slower than ASAP1. This tradeoff leads to improved spike detection abilities under the conditions tested, though at the expense of spike waveform fidelity. What is the upper limit on spiking rate that can be detected by this new, slower ASAP2? For a long time the problem in genetically encoded voltage indicators (aside from poor membrane trafficking) was prohibitively slow kinetics. Now it appears to have shifted the other direction. The slower off rate of ASAP2s makes for brighter signals, but is it still fast enough for fast spikes? What is the upper limit (i.e. when should one turn to ASAP1 orASAP2f?) Selling the decrease in GEVI speed as a positive attribute of the new GEVI is rather misleading.

3) Does ASAP2s work better in 2P purely because of the change in time constant + improved sensitivity, or has there been a change to the photophysics of the FP itself? (i.e. is the FP brighter, either in quantum yield or 2P absorption?)

How was the membrane capacitance and other items in Figure 3—figure supplement 2A-C calculated? The capacitance would be the value I would expect to rise, upon insertion of voltage-sensing domains in a plasma membrane. It looks like the numerical value of ASAP2s's capacitance is higher than that of untransfected cells (spread of data on untransfected bar is larger).

4) A more nuanced discussion of the photobleaching under 2P illumination would be helpful. For a given illumination intensity, NA, pulse duration, and wavelength, one would expect the photobleaching rate to be proportional to the duty cycle of illumination at each pixel, i.e. the fraction of the time the laser resides on the pixel. For the photobleaching measurements in Figure 1—figure supplement 3, the duty cycle is ~10^-6 (0.4 us per pixel x 2.23 Hz). For the applications in slice culture, the duty cycle is ~0.04 (50 us per voxel x 925 Hz). This is a 40,000-fold difference in illumination dose per voxel. The authors should discuss the importance of illumination duty cycle in determining the photobleaching rate.

Surprisingly, the fast photobleaching time-constants only differed by a factor of ~100 (5 s in the table in Figure 1—figure supplement 3D vs. 0.04 s in Figure 3—figure supplement 2J). This discrepancy deserves comment.

The presence of multiple time-scales in the photobleaching deserves some comment and analysis. One suspects the fast timescale represents photobleaching of the molecules directly under the laser focus, while the slower timescale represent depletion of surrounding molecules as they diffuse into the focus. If this guess is correct, then the authors could partially 'restore' the higher fluorescence of the cell either by briefly shutting the laser (so that GEVI concentration gradients can disperse), or by shifting the illumination spots to new locations. A demonstration that one can partially counteract photobleaching by these approaches would help allay some of the concerns about 2P voltage imaging.

It is not a foregone conclusion that 2P imaging is the best approach to voltage imaging in tissue. The number of points that can be multiplexed at high time resolution is limited, and photobleaching is a serious concern. A more detailed discussion of the photobleaching issues could help advance this discussion substantively.

5) The paper should also be more specific in the Abstract and throughout that the rodent "brain tissue" experiments are in organotypic slice cultures. Don't bury this fact. In many places the manuscript simply refers to "brain slice" or "intact brain tissue". The authors should exclusively refer to "organotypic slice culture." From the perspective of neuroscience applications, there is a world of difference between an acute slice and a cultured slice. These are also different from an optics perspective: cultured slices are thinner and sparser, offering much better imaging quality than acute slices. The impact of the work would have been greater had the authors looked in acute slice and e.g. characterized how deep they could image.

There have been many applications of GEVIs in organotypic slice culture with 1P imaging. It is not obvious that 2P imaging in organotypic slice cultures enables applications that could not have been achieved with more widely available 1P techniques.
