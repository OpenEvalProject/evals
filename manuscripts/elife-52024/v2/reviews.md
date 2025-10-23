# Peer review - Round 1

Editors:
- Philippe Herbomel, Institut Pasteur, CNRS UMR3738 France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.52024.sa1](https://doi.org/10.7554/eLife.52024.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

To understand the extent and role of cell fate heterogeneity in development and homeostasis, a highly desired goal has been to be able to follow the short- and long-term fate of single cells and their progeny, depending on their precise location and cell type identity within the developing organism at any given time. To this aim, various methods have been developed that used the optical transparency of model organisms such as zebrafish or C. elegans to trigger a genetic recombination leading to a switch in fluorescent reporter gene expression via a laser-mediated optical stimulation of the cells of interest. However, none of these methods was yet able to warrant truly single-cell labeling at high efficiency without compromising cell viability. This critical step has now been achieved by the authors of the present paper, via key improvements of a previous method using infrared laser mediated controlled cell heating. They have applied their improved single-cell labelling method with high success to three different cell types in the developing zebrafish, so it will likely be widely applicable to any tissue of transparent animal models.

Decision letter after peer review:

Thank you for submitting your article "in vivo single-cell lineage tracing in zebrafish using high-resolution infrared laser-mediated gene induction microscopy" for consideration by eLife. Your article has been reviewed by two peer reviewers, including Philippe Herbomel as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Didier Stainier as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

He et al. present a significant improvement of the IR-LEGO method originally introduced by the Kamei lab in 2006 to induce heat shock promoter driven gene expression in specific cells of a live organism by briefly illuminating them with an infrared laser. They manage to obtain a high efficiency of single-cell labeling well above the spontaneous activation of the HS promoter, while preserving cell viability – which was an issue of this method. The optimal conditions of illumination are fine-tuned by using a new method of real-time, high spatial resolution thermometry based on the fluorescence ratio of two fluorophores, one of which is temperature sensitive.

Essential revisions:

1) The narrow margin between labelling efficiency and cell damage was a major limitation in the various studies that used the original IR-LEGO method in various tissues and organisms. Therefore it should be added to the three other "fundamental challenges" listed in the Introduction.

Then in Figure 2—figure supplement 2, we learn that the authors' own set-up, if applied as single-point heating, kills a muscle cell in 2 sec. of illumination! Should we understand that in their previous papers using similar wavelength and power, but 2 min of presumably single-point illumination (Xu, 2015, Tian, 2017, He, 2018) the rate of cell death was actually very high, even though this was not mentioned? In the present work, the authors should devote more than just one sentence to this essential point in the Results section. It deserves at least a whole paragraph, in which they will notably document e.g. the frequency of cell death/damage following point vs. 8 x 8 µm scanning illumination in the various tissues examined, including for the HE cells which are the main target of this and their previous work (Tian, 2017). Also, how was such a long illumination chosen – i.e. how did it influence labeling efficiency vs. cell viability?

Then for the Discussion section, a question remains: molecules diffuse rapidly within the scanned targeted cell, so how can the 8 x 8 µm scanning make such a difference – i.e. less damage to the cell? The authors should discuss this and propose explanations.

2) The simulations of heat diffusion in Appendix 2 and Figure 1—figure supplement 1 are for a 2D diffusion field. But at steady state the diffusion equation reads ∇2T = 0; a 3D solution does exist: δT(r) ~1/r (as fohe potential away from a point charge). It would be interesting to compare that solution to the data.

3) The temperature gradient obtained in the z axis is less steep than in the xy plane, implying that more than one cell will often be labeled along the z axis (unless the targeted cells belong to a structure like the hemogenic endothelium studied here, which is basically 1 cell thick). Thus, in Figure 2—figure supplement 4B, the histograms should also be done in the z direction, and we suggest that for a dense tissue such as the muscle, the authors indicate whether the 45% of non-single-cell labeling is due to additional labeling in the z axis vs. x/y plane.

On the same issue: using a 2-photon laser excitation at 670 or 740 nm might yield a large absorption at the focal point and a much more local heating in the z axis. Why not choose that strategy? This could be discussed.

4) A steep temperature gradient is obtained with 3% agarose, and even more so in zebrafish tissue, but none in water. The authors invoke the higher thermal conductivity of water, but the latter is actually only slightly higher than that measured in the literature for 3% agarose or live tissues (0.6 vs. ~ 0.5). (Similarly, I guess their simulation of Appendix 2 would have also produced a gradient with a thermal conductivity of 0.6 instead of 0.5.…?) So some other factor must be invoked: e.g. convection occurring in water?

5) In the Discussion (3rd paragraph), the authors write "However the efficiency of single HE labeling is relatively low (29.3%)". But in the referred Supplementary file 1B and Figure 2—figure supplement 4C, that is not what we see: it is 55.6% – hence higher than for the myocytes! Which value is correct? (If it is the latter, then the rest of the paragraph becomes irrelevant).
