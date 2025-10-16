# Peer review - Round 1

Editors:
- Andrea Musacchio, Max Planck Institute of Molecular Physiology Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.31149.031](https://doi.org/10.7554/eLife.31149.031)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Autocatalytic microtubule nucleation determines the size and mass of spindles" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Andrea Musacchio as the Senior and Reviewing Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this paper, the authors use mono polar spindles (obtained for instance by Eg5 knockdown) to evaluate the position of minus-ends in Xenopus egg extract spindles, and thus to evaluate the mechanism of microtubule nucleation, and its effect on spindle size. The authors show that the monopolar spindle density profile can be understood as an autocatalytic mechanism that is regulated by a gradient of active nucleators. This is achieved by laser ablation experiments triggering a wave of depolymerisation. Measurements of the properties of the depolymerisation wave profile allow to access quantitative information on the nucleation profiles and length distribution of the microtubules. Comparison between control spindles and spindles with MCAK inhibition, which have longer and longer-lived microtubules, is consistent with the regulated autocatalytic mechanism. The paper concludes with a computational model to account for the control and MCAK inhibition conditions. The model is well explained and nicely done, and makes a strong contribution to the paper. In conclusion, the reviewers consider this an interesting and elegant study. However, they also identify the following important points that should be addressed in a revised version of the manuscript.

Essential revisions:

1) A table of parameters, together with values that are determined in the study, should be added. For instance, it is unclear what parameters are obtained from the model fit in Figure 4B.

2) While the theoretical modelling seems generally reasonable, some aspects remain unclear. Before Equation 7 the authors argue that since a nucleator can bind anywhere on microtubules with average length l, they bind on average at distance l from the end of the mother microtubule – why is it not l/2 then? They then argue that the center of mass velocity is given by v=l theta with theta the turn-over rate. Can the authors explain in more details where this relation comes from? In particular, one reviewer is surprised that the branching rate does not enter this formula; is it the case that there is still a velocity at 0 branching rate for instance?

3) In Figure 3C, it is unclear from the legend what exactly is being plotted. The authors should clarify this point.

4) Since only bound nucleators are nucleating new microtubules, it seems that the whole process would not start without the formation of initial microtubules by a process distinct from the autocatalytic mechanism described in the paper. Can the authors discuss what may control the density at x=0? Is it different in the control and MCAK-inhibited conditions?

5) After Equation 1, the sentence "this rate has a very well peak that moves as a function of time, Figure 1C" is confusing. The rate Ã(t, r) is already integrated with respect to distance away from the cut, so presumably Figure 1C does not directly inform about the shape of the function as a function of r. Is this correct? If not, please explain.

6) In Figure 2B, the x-axis says "distance from the central"; do the authors actually mean "microtubule length L"?

7) After Equation 6, the authors mention that P(y, l) does not depend on y. Is that something that can be verified from experimental measurements?

8) In Figure 1D, the two nucleation profiles for control and a-MACK conditions are plotted in arbitrary units. Are these arbitrary units defined in a consistent way, such that the difference in magnitude of the two plots is meaningful? If so, it would be helpful to clarify this in the manuscript.

9) Throughout the paper, the authors generalize the results to "mitotic spindles" or in some cases "large spindles". However, the mechanisms described here may be particular to Xenopus egg extract spindles, in which branched microtubule nucleation has been observed. The authors should be careful either to limit conclusions to the system described here, rather than to all mitotic spindles in general, or to explain how the results may apply in other mitotic spindles, which may not show branched microtubule nucleation, and/or where microtubule nucleation may occur exclusively at spindle poles or centrosomes.

10) The authors state that the location of minus ends in the monopolar spindles exactly corresponds to the location of microtubule nucleation, because microtubule transport is completely eliminated in the absence of Eg5. This is a major assumption in the paper, and experimental verification that no microtubule transport occurs in the absence of Eg5, and that the minus ends are exact readouts for the location of microtubule nucleation, is important.

11) The authors state that their method of laser cutting and analysis resolves the minus end locations with a single laser cut, allowing the authors to measure the "microtubule nucleation profile" (units a.u./length2). It would be helpful to provide a bit more detail regarding the method in the main text and so that the reader can follow the experiment, and, in addition, a better definition and description of "microtubule nucleation profile" would allow the reader to better understand the results in Figure 1D. Right now, these key results are too briefly explained in the main text, and not understandable.

12) The authors measured microtubule nucleation under conditions in which MCAK was inhibited, and found that the number and spatial spread of nucleated microtubules was increased. From these experiments, it was concluded that microtubule nucleation depended upon the presence and dynamics of microtubules. However, can the authors exclude that the nucleation process itself is not altered by MCAK inhibition, such that stabilization of microtubule nuclei by inhibition of MCAK would lead to increased nucleation, similar to but not dependent on the presence of additional microtubule density in the presence of MCAK?

13) The description of the experiments in Figure 2D, in which an "inert obstacle" was added to block microtubule polymerization, should be better detailed in the main text. Further, while the one sample image is convincing, there was no quantification of this result, nor detail on how the location of the obstacle relative to the center of the monopole would alter these results. This needs to be addressed.

14) From the RanQ69L experiments, in which new microtubules were nucleated at the edge of pre-existing structures (one experiment shown, no quantification), the authors conclude that the amount of active nucleators limit the size of monopolar spindles. This conclusion would be greatly strengthened by measuring the size of the monopoles as a function of the concentration of active nucleators.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Autocatalytic microtubule nucleation determines the size and mass of spindles" for further consideration at eLife. Your revised article has been favorably evaluated by Andrea Musacchio as the Senior and Reviewing Editor, and two reviewers.

The reviewers praised your effort in revising the manuscript, but there are two remaining issues that need to be addressed before acceptance, as outlined below. The required changes are textual and do not require re-review, but I kindly ask you to consider the reviewers' points very carefully:

1) One thing that remains unclear is the definition of the velocity v. The explanations given by the authors seem confusing, and the authors should clarify this in the manuscript, maybe with the help of a schematic. What is not clear is that (i) in their reply to the referees, the authors state that v is the velocity due to the branching process, but end by saying that in the absence of branching there is still a non-zero velocity. This sounds contradictory and needs to be clarified. (ii) It is unclear if this velocity is different or equal to the velocity of polymerisation of individual filaments. (iii) If the velocity is indeed associated to the microtubule mass flow as stated by the authors, it is not clear how this velocity can be independent from the branching rate. It sounds natural to think that a moving filament decorated with many branches will not create the same mass flow as an undecorated filament. These points should be clarified in the text, possibly with the aid of a schematic.

2) While the authors generalize the results to "mitotic spindles" or in some cases "large spindles", the mechanisms described here rely on branched microtubule nucleation, which, to the reviewer's knowledge, has only been observed in Xenopus egg extract spindles. Thus, the reviewer thinks that it is important to limit the conclusions and paper title to systems in which branched microtubule nucleation has actually been observed, since the model relies specifically on this assumption, rather than to all mitotic spindles in general. It appears that the authors address this concern by hypothesizing that branched microtubule nucleation could potentially also happen in mitotic spindles from other organisms, without supporting data. In the absence of new data to demonstrate that branching microtubule nucleation is a general mechanism across multiple organisms, this argument is not convincing, and the paper and title should be rewritten with more exact language to limit the conclusions specifically to spindles, such as the Xenopus egg extract spindle, in which branched microtubule nucleation has been observed.
