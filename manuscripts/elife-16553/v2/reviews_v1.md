# Peer review - Round 1

Editors:
- Michael Häusser, University College London , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.16553.017](https://doi.org/10.7554/eLife.16553.017)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Unique Membrane Properties and Enhanced Signal Processing in Human Neocortical Neurons" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Michael Häusser as the Reviewing Editor and Eve Marder as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Nelson Spruston (Reviewer).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript examines the cable and specific membrane properties of human neocortical neurons in slices dissected from patients. To address this question, the authors use electrophysiological recording, cable modelling, and simulations. The main finding is that the specific capacitance in human cells is lower than previously reported in rodents, as convergently shown by two different approaches (cable modeling and nucleated patch recording). Furthermore, they show that a low Cm is advantageous for both efficacy and speed of signal propagation in pyramidal cells. If the difference in Cm is indeed true, this would clearly be an important and interesting finding that surely deserves publication in eLife. However, several issues need to be addressed before the conclusions can be considered secure. Most importantly, alternative interpretations of the data are not carefully considered. Furthermore, the case for a difference in Cm rests on only four recordings from mouse neurons.

Essential revisions:

1) Short current pulses in current clamp: why were these performed only in human neurons and not in mouse neurons? The decay of voltage transients in response to current injection is a highly indirect measure of Cm. Thus, it would be valuable to identify the fundamental difference in the voltage responses observed in human and mouse neurons, thus providing a direct indication of the feature of the data that is indicative of a different Cm. If the authors have short current pulse data from mouse neurons, they should therefore provide it, particularly since this would offer two parallel lines of evidence that illustrates the difference between human and mouse neurons, which would be more convincing than just the result from nucleated patches.

2) Nucleated patch experiments: the number of recordings is very low. In particular, n=4 for mouse neurons is very low by the standards of the field, especially since obtaining recordings from mouse neurons is easier than for human neurons. We strongly encourage the authors to add additional datapoints to the mouse nucleated patch dataset.

3) Modeling of human neurons: were these the same neurons from which the recordings were obtained? If not, it is possible that the morphologies used were different enough to introduce significant error in the estimation of Cm. (Note: this is an example of a general problem with the paper, which is that it is not well written.).

4) Modeling of human neurons: Fits of the voltage transients are based on estimates of Ra, Rm, and Cm. To make a more convincing case that low values of Cm are necessary to achieve good fits, please provide a plot (or plots) of RMS error for different combinations of these three values. See also additional comments below about series-resistance and capacitance compensation.

5) The Ra obtained in the present study seems unrealistically high. Two-electrode recording (separating voltage-recording from current-feeding electrode) has revealed Ra values of 115 – 190 Ohm cm (Roth and Häusser, 2001; Schmidt-Hieber et al., 2007; Nörenberg et al., 2010). Clearly, the best way to address this discrepancy would be to use the two-electrode approach for human neurons. If this is not possible, the limitations of the present study should be clearly stated. Additionally, the value of Ra will depend on the intracellular solution. However, the composition of the internal solution for the whole-cell recordings is not even mentioned in the paper (it is most likely different from the Cs+ solution used for nucleated patch recording).

6) There is evidence for non-uniformity of Rm in the literature (Stuart and Spruston, 1998; Nörenberg et al., 2010). The authors should test non-uniform models to corroborate the conclusion of low Cm under these conditions.

7) The authors need to obtain confidence intervals of the parameter estimates. One possibility might be to use bootstrap analysis, as previously suggested by Roth and Häusser, 2001.

8) Cable modeling is well known to be sensitive to even subtle nonlinearities. A particular problem is Ih. Is Ih expressed in the human neurons? Is there a sag during hyperpolarizing currents mediated by Ih? Did the authors make any attempt to block Ih?

9) The accuracy of the Cm estimate stands and falls with the reliability of the spine correction. However, the spine correction factors are not convincing. Wouldn't it be the best to directly count spines in the recorded cells rather than in postmortem tissue? How did the authors correct for hidden spines (branching out in z direction) or for spines below the LM resolution limit? Finally, without being pedantic, the mean F from the given data is 2.0, rather than 1.9. We agree that a change will make the Cm even smaller, but in any case, this highlights potential systematic errors.

10) The estimation of the surface area of the nucleated patches is not convincing. The shape of the nucleated patches is probably best approximated by an ellipsoid. The exact formula for the surface area of spheroids or triaxial ellipsoids is quite complicated, so the simple equation 4 of Gentet et al., 2000 (which the authors apparently used; see subsection “Nucleated Patches”) is an approximation of an approximation. Also, the authors don't state which of the "formulas" of the Gentet paper they used. Finally, numbers for the surface area of the nucleated patches need to be given in the present paper.

11) Unfortunately, the authors fail to address the mechanisms underlying the low Cm in human pyramidal cells. Is it a difference in the relative dielectric constants or the geometric properties of the lipids (i.e. the length of acyl side chains)? Or does the protein content influence the relative dielectric constant of the membrane (and thereby Cm)? At the very least, these aspects have to be better discussed.
