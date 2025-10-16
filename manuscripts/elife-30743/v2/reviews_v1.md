# Peer review - Round 1

Editors:
- Sean R Eddy, Howard Hughes Medical Institute, Harvard University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.30743.027](https://doi.org/10.7554/eLife.30743.027)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Gene free methodology for cell fate dynamics during development" for consideration by eLife. Your article has been favorably evaluated by Arup Chakraborty (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The authors previously introduced a "geometric" dynamical model for C. elegans vulval development (Corson and Siggia 2012). A subsequent paper (Barkoulas et al. 2013) provided quantitative data for mutants perturbing the EGF and Notch pathways. In this manuscript, Corson and Siggia update their model, show that it accounts quantitatively for almost all observed phenotypes, and that it makes additional testable, non-obvious predictions.

The reviewers feel that this is strong and interesting work that merits publication in eLife, but we do have several issues and questions that we would ask you to address in a revised manuscript, listed in the following 9 points:

1) A main assertion is that this "geometric model with no coupling between the two signaling pathways (EGF and Notch) [is used] to explain epistasis in a variety of experiments". However, the model does couple EGF and Notch signaling pathways in several ways, including:

◦ While it is true that the two signals are parameterized by two vectors m→1and m→2, which are combined in a linear manner in Equation 4, the linear combination (vector m) is an argument to non-linear functions, including the hyperbolic tangent and the norm (Equation 3). This non-linear mapping will, in effect, introduce interaction terms involving products of m→1 and m→2. For example, consider the second-order term of the Taylor series expansion of the function tanh, or expand out the norm of l1m→1 + l2m→2, and one sees that there are products of components of vectors m→1 and m→2 in numerous places in the model equations.

◦ Making the above more complex to interpret, the interaction terms have no basis in mechanism.

◦ Next, the weighting factor (l2) for Notch signaling in Equation 4 depends on the level of EGF and Notch signaling, according to Equation 7 (note the dependence on the vector r, which depends on EGF and Notch signaling). Thus, the magnitude of Notch signaling depends on EGF signaling – a form of coupling.

◦ Finally, the threshold line for Notch expression (dotted line in Figure 1D) cuts diagonally through the fate plane. This line represents yet another form of coupling, since the level of Notch ligand (l2) depends on passing this threshold line (which depends on EGF and Notch signaling).

2) It is asserted that this model framework is the "most parsimonious parameterization of how two signals can control three fates". This statement is debatable, and readily disproven by drawing examples from literature. Based on Table 2, there appears to be 12 parameters in the model. The footnote to the table indicates an additional one that was not fit (norm of vector 1→1), but is a parameter. In total, we have at least 13. There are many examples of developmental patterning models, including but not limited to this C. elegans system, with fewer parameters. Some of these other models even include molecular mechanism (coarse-grained), and are capable of predicting phase diagrams of multicellular phenotype. Therefore, parsimonious parameterization is probably not a major feature of the approach presented here. Rather, it seems more accurate to describe the model as taking a complex fate plane structure (Equations 1-11) and using numerous parameters to fit the dynamically-evolving landscape to experimentally-observed VPC fate choices. In this respect, the approach opens itself to a classical critique of phenomenological modeling in biology: given a sufficiently complex model structure, one can fit observed behavior to it.

3) There are a number of predictions about the dynamical behavior of the system (Figures 5–6, subsection “Dynamical perturbations are sensitive tests of the model”). However, it is unclear what confidence to have in these predictions because there is so little temporal data for this system with which to parameterize dynamics (as pointed out in the manuscript). For example, the dataset in [Barkoulas et al., 2012] is extensive, but appears to be only endpoint measurements. According to Table 1, it seems that the only data for intermediate time points came from anchor cell ablations in the wild-type worm ([S12]). While this data provides VPC fate choices (as shown in the table), there is no data on the level of Notch signal. Additional detail is needed on what temporal data is used to parameterize the model, how, and what degree of confidence one can have on the parameterization of dynamics.

4) This modeling approach provides a quantitative framework for predicting phenotypes, but is largely phenomenological. One may be left wondering what new things we learned about mechanisms involved in C. elegans vulval development. We are left with a black-box(*) of modulating EGF/Notch signal on one end, and post- or predicting phenotypes on the other end. Whether this is the most insightful avenue for modeling and drawing mechanistic insight into developmental systems is unclear. (*) perhaps a grey-box since the mathematical construction is precisely known to us. But, the construction is phenomenological and has no mechanistic basis.

5) Related #4, the notion that "geometric models should be the method of choice when confronted with sparse in-vivo data" seems an overstatement. Even in light of sparse in-vivo data and nascent mechanistic knowledge, significant progress has been made in many developmental model systems by using mechanistic models to predict phenotypes, and revising these models accordingly when experiments disprove model predictions.

6) There is little, if any, comparison to other models that predict phase diagrams for this system. Does this modeling approach match experimentally observed phenotypes better than other models? Do other models predict "sensitization" by quantitatively modulating specific signaling mechanisms? What are the pros and cons of the approach presented here relative to other methods?

7) Figure 1D and 1E show a dashed line in the fate plane, with an explanation in the legend that "cells positioned below the dashed line express Notch ligands." The dashed line appears invariable across the different panels. Does this mean that cells express Notch ligands regardless of their fate types (t=0.5 for P5/7.p for secondary fate, and several panels for tertiary fate)? If so, it will be good to cite experimental evidence for this.

8) In Figure 4C2, where authors predicts a transient primary fate for the green cloud (P5/7.p), the path is above the dashed line. How would these cells produce Notch ligands to transiently signal P4/8.p to induce secondary fate? I'm assuming that the paths are simulated results and not schematic drawings. If the latter, one may argue that the ectopic Notch is epistatic to the EGF, in which case one does not need to invoke a transition through the primary fate.

9) P6/P7/P8 are supposed to be an equivalence group, but Figure 1D shows P6.p with a different fate plane from P7.p/P8.p. Doesn't this beg the question? The model needs to explain how P6 becomes different from P7/P8. Figure 1D appears to be trying to illustrate the notion of competence windows (that P6.p has an early competence window to respond the EGF signal, and P7.p has a middle competence window to receive the Notch signal from P6.p). But it's unclear how the model treats competence windows. It seems the authors are trying to say that P6.p sees the highest/earliest EGF signaling from the AC, so P6.p starts "moving" in its fate plane first; and when P6.p starts expressing Notch, that starts moving P7.p. But it's not clear why the fate planes themselves change. If the EGF signal causes the fate plane of P6.p to change to an all-1* fate plane, doesn't this become tautological? (That is: the geometric model explains how P6.p adopts 1* fate by saying that P6.p moves toward 1* fate.)

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Gene free methodology for cell fate dynamics during development" for further consideration at eLife. We apologize for the delay in examining your revised manuscript. Your revised article has been favorably evaluated by Arup Chakraborty (Senior Editor), and a Reviewing Editor.

The manuscript has been greatly improved, and the referees agree that most concerns have been satisfactorily addressed. However, there is one aspect (1a, b below) that needs to be addressed before a decision to accept the paper can be made, because a central claim of the manuscript remains unclear. There is also one other aspect (2 below) that the referees note for you to consider at your discretion.

1a) Regarding whether the model includes coupling between EGF and Notch, your response acknowledges "couplings induced between the N and EGF pathways by the non-linear functions that are used". However, the manuscript still states in several places that E and N are not coupled in the model, including:

"Our model has no overt coupling between the EGF and Notch pathways, implying that if we fit two alleles,[…]".

"Until this point, we have used a geometric model with no coupling between the two signaling pathways[…]"

"Our model with no pathway interactions then fits the genetic data in…"

You are trying to make a distinction between "overt" versus implicit coupling. Whether the coupling is overt or implicit, however, the end result is that the signals are coupled with each other, and the manuscript should not claim that they are not.

1b) In addition to coupling introduced by nonlinear functions, the model includes coupling in its geometric construction. This point was in the original review (see final bullet under point 1) but left unaddressed. Consider Figure 7 and subsection “Fate correlations and multistability”, where it says "a simple way to incorporate one such coupling in the model, with no additional parameters, is to down-regulate Notch signaling in 1º fated cells along the same threshold [the dotted line in Figure 1D] that defines the production of Notch ligands". If downregulating Notch signaling along a line in the fate plane is a way to introduce EGF-Notch coupling, would not upregulating/increasing the production of Notch ligands as cells cross the same line also be a form of coupling? The latter is part of the model from the start.

This coupling has nothing to do with the shape/steepness/non-linearity of the threshold – it is a coupling introduced by a demarcation in the fate plane at which Notch ligands are unregulated. To cross that demarcation, cells must possess a combination of EGF and Notch signaling that lands them in that place in the phase plane. Thus, the level of EGF and Notch signaling affects expression of Notch ligand, which in turn affects EGF and Notch signaling: geometric coupling.

This is a second reason to question the manuscript's central claim to predict epistasis without invoking coupling; please clarify.

2) The comparisons to other models were useful. Regarding model complexity as quantified by numbers of parameters – the manuscript still speaks of a vague "plethora of parameters", but you provided useful parameter numbers for the other models in your response (over 40 parameters (Hoyos) and 13 parameters (Giurumescu)). It would clarify the scale of the disparity if you included these numbers in the manuscript.
