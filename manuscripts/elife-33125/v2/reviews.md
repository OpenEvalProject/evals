# Peer review - Round 1

Editors:
- David Sherratt, University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.33125.041](https://doi.org/10.7554/eLife.33125.041)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Spot-On: robust model-based analysis of single-particle tracking experiments" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Kevin Struhl as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Lothar Schermelleh (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

This 'Resource' manuscript describes an integrated approach for single-particle tracking (SPT) microscopy using stroboscopic photoactivation (spaSPT) and present "Spot-On", an open-access software analysis tool for SPT data. The latter can be applied to any kind of SPT data and uses model fitting to calculate diffusion rates and bound and mobile population sizes. The authors convincingly validate and compare their approach with other available tools using ground-truth simulations and analysing a number of Halo-tagged nuclear proteins with differential dynamic properties in U2OS cells and labelled with photoactivatable JF dyes.

Both reviewers are enthusiastically supportive of this being published, although a small number of minor comments and corrections are appended below.

1) A practical issue – could some of the information on the website also be loaded as a supplemental tutorial file (some helpful screenshots?)?

2) The software in its current form is restricted to 2D-SPT analyses. Why is 3D-tracking not implemented, and is there a planned route for a future upgrade? With many imaging systems offering astigmatism-based 3D localisation option, would this not offer potential benefits? We understand that a package for 3D analysis may be out of the scope of the present article, but whether there is a prospect for such a package in the future might be indicated/commented on.

3) Along with the software, the authors describe spaSPT as a beneficial approach to minimize motion-blur and tracking errors. What would be the difference between spaSPT and SPT with very low concentration of non-photoactivatable JF dyes? The authors may want to discuss application of Spot-On with alternative imaging approaches in cases where photoactivation is either not possible (e.g. due to lack of laser lines or suitable dyes) or not desired (potential damage, blue channel is already used).

4) It would be desirable to have a function for visualising tracks with the option to differentially select and display subsets of tracks that fall into different categories (immobile/mobile or other criteria). This would enable the user to directly see spatial patterns of differential dynamics.

5) i) Figure 4K and subsection “Effect of motion-blur bias on parameter estimates”, first paragraph: Why is there is a small but significant difference between PA-JF549 and PA-JF646?

ii) Subsection “Validation of Spot-On using spaSPT data at different frame rates”: The axial detection range should be specified (around 700 nm?).

iii) Abbreviations CDF and PDF may need to be introduced in the main text as well, not only the figure legend.

iv) Figure 4—figure – supplement 3 legend – last paragraph: Does the "total bound fraction of ~60-65%" refer to Halo-Sox2? Please specify.
