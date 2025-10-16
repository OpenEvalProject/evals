# Peer review - Round 1

Editors:
- Tâm Mignot, Aix Marseille University-CNRS UMR7283 France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.40472.023](https://doi.org/10.7554/eLife.40472.023)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Mechanics and dynamics of translocating MreB filaments on curved membranes" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Gisela Storz as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The manuscript by Wong et al. seeks to link the molecular details of polymer binding and motion on curved surfaces to phenomena observed in the localization and motion of MreB in rod-shaped bacteria. This is timely work and focuses on a multi-scale process that is both fundamental to the way bacteria grow and firmly grounded in molecular biophysics. The authors present a very large number of analytical and numerical results and make a good effort to link these to experimental observations. Of particular note, Gaussian curvature localization (which seems to be somewhat controversial) is linked in this model not to an energetic preference of the proteins for these parts of the cell but rather to a consequence of the motion and the geometry via kinetics.

A series of important changes is requested before the manuscript could be considered for publication in eLife.

1) The authors need to do a better and more even-handed job addressing the current theoretical literature that has attempted to explain MreB localization, and comparing their results to previous theoretical works. Specifically, the authors make very different assumptions/focus on different details of the polymers than several previous papers. For example, Quint, Gopinathan and Grason et al., 2016, show that ribbon-like polymers (of which MreB is likely to be one example due to its protofilament architecture) can have both intrinsic curvature and twist which can give rise to localization at specific mean and Gaussian curvatures. Wang and Wingreen, 2013, (which is barely discussed despite being likely the most relevant previous theoretical work on this subject) discuss curvature localization in detail and show that the specific pattern of polymer deformation (e.g. where most of the deformation is focused at the polymer tips) is highly important. Why did the authors of the manuscript under review choose the details of their model and how would it be different if they had added the details considered by others and shown to affect geometric localization? What if the localization or motion did depend on Gaussian curvature or if the filaments were slightly twisted ribbons? The authors specifically state in Appendix 1 "we have assumed the filament to be bent uniformly, but the case of a curvature which varies with position along the filament length can be considered similarly." But would it have made a difference (as suggested by Wang and Wingreen)? Would this fit the data better? Worse? The same but with more parameters? The manuscript is written as if there is no other theoretical work out there and that is just not true. The authors need to both motivate their decisions and compare their results quantitatively to those of previous models in the literature. Otherwise, the reader cannot put the work into context and it is unclear which model is more likely correct given available experimental data.

2) As shown in Figure 2C the model has broader implications in terms of filament proteins and membrane binding than MreB bound to cylindrical membranes and discussion of how it could apply to other biological systems should be included. In particular, the detailed mathematical model and all its generality must be explained in a context that fits the scope of eLife. The paper contains notation commonly used in mathematics (but not that common in biophysics). For example, after Equation 3, the angular noise is denoted by N(0, σ^2) where neither N or its arguments are defined nor given biophysical significance. This trend towards a formal mathematical approach is even more prevalent in the supplementary information. Another example, is the discussion in the main text of the processivity parameters λ and k in the subsection “Dynamics of translocation”. While they are used in some of the detailed calculations in the supplementary information, the main text with the application to MreB proteins shows results for either zero processivity for which the proteins cannot attain their minimal free energy configuration in regions of high membrane curvature or for infinite processivity, in which case the proteins can move to reside in the high curvature regions of the membrane – with some fluctuations about those positions. Thus, it was not clear why the dynamic calculation was performed in such detail since the main text only showed the results for the two limiting cases of kinetic restrictions and no kinetic restrictions.

3) The kinetic equation (Equation 3) seems to coarse grain over the protein-membrane interactions and intrinsic noise to result in a Langevin equation with an effective noise that depends on the curvatures. It is not at all clear how this is obtained from the standard physical treatment of particle motion where the Langevin equation contains a term corresponding to the physical forces (in this case, due to the curvature energies of the membrane and protein) and another corresponding to white noise (which could also model cell activity if so desired). Had the standard treatment been used, the authors might have been able to predict the steady-state position and orientation as well as the fluctuations about that steady-state using a Boltzmann factor (with an effective noise) which would have provided more intuition than the kinetic simulations that eventually attain such a steady-state.

Specific points:

- The authors state that MreB motion is processive "in contrast to spontaneous or diffusive motion," but then state "we may model the trajectories of filaments as random walks." This seems contradictory.

- "translocates along the largest principal direction." Why was this chosen? Can the authors motivate this with a molecular mechanism via which enzymes/the polymers might know which direction has the largest principle curvature? This to me is the least well motivated part of the model in terms of linking realistic molecular biophysics to the global behavior.

- The supplement is already quite lengthy and detailed, but there remain statements in the text that either state something can be shown, that some parameter/choice is rather unimportant, or simply make an assertion and state "(not shown)". I find this extremely problematic. The authors should back up all of these statements (e.g. with a derivation, calculation, simulation, etc.). This reminded me of the professor who states, "it is trivial to show…". If it is obvious, then it should be easy to show. If it is hard to show, then the off-handed remark seems incorrect.

- "filaments are increasingly misaligned in wider B. subtilis cells". Define misaligned so the reader does not have to go to the referenced paper and figure out what this means.

- Figure 3: The '0' and '\infty' designations were confusing for B and D, particularly after reading the fifth paragraph of the subsection “Dynamics of translocation”. I think this is the most confusing part of the text and after reading the text, supplement, and figures/supplementary figures I admit to not fully grasping all of it. Perhaps it could be made more clear.

- Figure 4 inset: Why is this not compared to the experimental data (e.g. from Bratton et al., 2018) as the Mean curvature plot is? This would make this result (a key one for the paper) much stronger.

- Supplementary file 1, 2: Is it possible to put confidence intervals on these estimates from different papers? I understand the authors need to make choices for their modeling, but it would be useful to know how well the field agrees on these numbers.

- Figure 3—figure supplement 1: In the fluorescence image, it is not clear where the cell/bulge are, especially compared to the rest of the figure. Maybe add a schematic?

- Figure 3—figure supplement 2 and Appendix subsection “Cylinder with small wavelength undulations”: The authors state that since Ursell et al. showed a high degree of correlation between mean and Gaussian curvature, that the small wavelength undulating model is better. But in Ursell, this was done for the channel-curved sinusoidal cells and not normal rod cells. Could this make a difference such that the long wavelength model might be better? If it was, would this make a difference?

- Figure 3—figure supplement 3: Unless I missed it, this figure is not used in the text or supplement. Does it matter that the data clearly does not resemble the assumption?
