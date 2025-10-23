# Peer review - Round 1

Editors:
- Andrew C Kruse, Harvard Medical School United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62389.sa1](https://doi.org/10.7554/eLife.62389.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper describes the use of time-resolved serial femtosecond crystallography to investigate light-induced changes in the conformation of channelrhodopsin. The authors identified initial conformational changes that occur upon illumination, including a shift in the position of retinal as well as additional changes in the conformation of transmembrane helices 3 and 7. Using these results, the authors propose a model for how initial conformational changes may culminate in channel opening. This work advances our understanding of the molecular mechanisms of channelrhodopsin activation and of light-induced conformational change more generally.

Decision letter after peer review:

Thank you for submitting your article "Time-resolved serial femtosecond crystallography reveals early structural changes in channelrhodopsin" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Kenton Swartz as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Doeke Hekstra (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest but revised data analysis is required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

This manuscript by K. Oda et al. describes the use of time-resolved serial femtosecond crystallography to investigate light-induced changes in the conformation of channelrhodopsin. The manuscript identifies initial conformational changes that occur upon illumination, including a shift in the position of retinal as well as additional changes in the conformation of transmembrane helices 3 and 7. The authors propose a model for how these initial changes may culminate in channel opening.

Essential revisions:

Several technical points were raised during the review process, but the most significant concern centers on the approach to model refinement. The description of the refinement process in the Materials and methods section is very brief, and is missing essential details such as the choice of restraints and the exact details of which difference maps were used. More generally, the use of real-space refinement directly against difference maps is not sufficiently described, and is potentially confounded by a variety of issues. For example, motion of an amino acid side chain into a region that would otherwise be occupied by an ordered water molecule could lead to little change in Fo-Fo density, or changes that are not readily interpretable. Reciprocal space refinement against extrapolated structure factors or reciprocal space refinement of partial occupancy models for each conformational state would be more appropriate (see below). At least one of these approaches should be included in a revised manuscript, along with appropriate statistical benchmarks such as real or reciprocal space correlation coefficients or R-factors. The reviewers also wish to emphasize that it is more appropriate to refine against structure factors corresponding to a conventional electron density (2Fo-Fc type) map than to a difference map. A second significant concern is the mismatch between the timescales of the QM/MM simulations and the experiments, which is not adequately explained. There are a variety of smaller technical points raised, which are discussed in detail below.

1) The authors mentioned low quantum efficiency of the retinal isomerization (~30% in C1C2), and then they built models onto the observed peaks in the difference maps. This can be problematic without validation, and the difference map signals can be misleading. In order to justify the correctness of the refined structures, the difference maps calculated between structures of light and dark states should be presented. Furthermore, more details should be included in structure refinement section, such as restraints, weighting factors, and validation metrics. Alternatively, the extrapolation approach has been adapted by several recent TR-SFX studies, such as the bR or KR2 studies (Science 365, 61-65, 2019); Nature 583, 314-318, 2020). Authors may want to try these approaches. In principle, it may also be possible to refine models of different states with partial occupancy based on the known photoconversion efficiency, which would also provide useful refinement statistics to assess model quality.

2) A vexing complication of the experiments is that the spectroscopic kinetics in crystal form differ markedly from those in solution. Clearly, the crystallographic data show that retinal isomerization is induced in the crystal and leads to conformational change at nearby positions. Spectroscopically, only two states are clearly distinguishable within the time scales of interest (P1/3 versus P2), reflecting the protonation state of the Schiff base. The authors speculate that they see a longer-lived P2 state in the crystal, apparently concurrent with a P1 or P3 state. This is reasonable, but it is not clear whether the authors really see a "P1 to P2 transition" (inclusion of shorter pump-probe delays might have been more convincing). The spectroscopic data likely miss detail of the structural transitions following photoexcitation and do not shed much light on how conformational dynamics may differ between crystal and solution.

3) The comparison between refined structures and the QM/MM simulation model is not convincing. QM/MM calculation results are based on short simulations. The timescales do not match with the ones studied in this TR-SFX. It is hard to make a fair comparison.
