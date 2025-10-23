# Peer review - Round 1

Editors:
- Wesley I Sundquist, University of Utah School of Medicine , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.06980.014](https://doi.org/10.7554/eLife.06980.014)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Measuring the optimal exposure for single particle cryo-EM using a 2.6 Å reconstruction of rotavirus VP6” for consideration at eLife. Your Tools and Resources article has been favorably evaluated by John Kuriyan (Senior editor), a Reviewing editor, and three reviewers.

The following individuals responsible for the peer review of your submission have agreed to reveal their identity: Wes Sundquist (Reviewing editor); Janet Vonck (peer reviewer) and John Rubinstein (peer reviewer). A further reviewer remains anonymous.

The Reviewing editor and the reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

Grant and Grigorieff describe an exciting next step in the recent spectacular series of cryo-EM maps from direct electron detector data, with a reconstruction of the rotavirus VP6 protein at a resolution of 2.6 Å from 4000 virus particles, using both the icosahedral symmetry and the 13-fold non-icosahedral symmetry (more than three million asymmetric units). The large size of the particles made it possible to analyse individual movie frames, and a 130-frame, 100 e-/Å2 data set was used to assess the effects of radiation damage. The authors conclude that optimal doses for EM maps at low and intermediate resolutions are much higher than the 10-20 e-/Å2 determined previously using crystalline samples, for example with a pre-exposure of 50 e-/Å2 a map at better than 6 Å resolution could be obtained. The authors speculate that the loss of long-range order in the crystalline samples may have played a role. Making use of the fact that the rotavirus particles can be aligned well from very short exposures (they use the average of 3 frames) they devise a filtering scheme for the data based on the resolution-dependent SNR fall-off as a function of exposure, and show that using this scheme a 2.6 Å reconstruction can be done from the full 130-frame dataset that is indistinguishable from the best reconstruction using unweighted frames 4-21 only. The dose filtering scheme has been integrated in a new program for frame alignment.

The presented data are beautiful, the paper is clear and well-written, the work provides welcome additions to the growing toolbox available to the still young field of cryo-EM by direct electron detectors. Overall, this is an excellent paper of high value and high interest to the scientific community.

Significant issue that the authors must address

1) The dose optimized weighting scheme applied to the entire movies (frames 4-130) produces exactly the same resolution as when using a much smaller subset of the data (frames 4-21) determined by manually searching for the ideal dose fractionation set of frames. While it is convenient to be able to avoid the tedious manual search, it is a harder sell to justify acquiring 5x the number of frames (all needing storage and processing etc.) to get to the same resolution. The authors are no doubt aware of this—but ought to address it directly in the paper—and thus base the justification for the high dose acquisition and weighting scheme on the proposition that this will have a much more important impact on smaller particles. This could then justify the pain of acquiring many more frames but this remains to be proved. Can the authors use one of the publicly available datasets to prove this proposition (e.g. the raw movie frames and other metadata of the proteasome dataset, which goes to 2.8A resolution, are available on EMPIAR)? If the authors decide this is too much work then the emphasis on this point should be reduced, and the authors should modify the statement that the major impact of the paper is enabling SPEM on smaller particles (as this is not yet shown). Instead, the authors could choose to place more emphasis on the extraordinarily high resolution of the reconstruction that has been achieved here. This might involve including some discussion on how the data was obtained and what methods were used to reach the exceptionally higher resolution.

Other issues that the authors should address:

1) The authors base their analysis of radiation damage on SNR values calculated from the FSC. Is this really equivalent to the critical exposure (Ne) values measured by following the fading of the calculated diffraction spots from 2D crystals? (The answer may indeed be yes, but a little justification is needed).

2) The authors convert from critical exposures to optimal exposures using the Nopt=∼2.5Ne relationship from Hayward and Glaeser (1979). This ratio is based on a rather complex derivation and several assumptions. The authors should justify its use here, showing or explaining how it still applies to the Ne values measured from SNRs and the FSC.

3) The dose filtering was tested on the same data that was used to derive the critical dose curve. However, the authors speculate that the rotavirus with 780 copies of VP6 may to some extent be affected by some loss of long-range order as a function of dose like the 2D crystal samples. If this is the case, their dose curve would overestimate the radiation sensitivity of smaller complexes. This issue should be discussed.

4) The details of the new program Unblur are vague. Is it available? Is it stand-alone or part of a package? Is the dose filtering optional and (in light of the previous comment) are the values hard-wired? It is important to add this information so the new program can be tested by the community.
