# Peer review - Round 1

Editors:
- Frank Jülicher, Max-Planck-Institute for the Physics of Complex Systems Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.27454.023](https://doi.org/10.7554/eLife.27454.023)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Global morphogenetic flow is accurately predicted by the spatial distribution of myosin motors" for consideration by eLife. Your article has been reviewed by three peer reviewers, including a member of our Board of Reviewing Editors, and the evaluation has been overseen by the Reviewing Editor and Anna Akhmanova as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors perform a careful and thorough analysis of the collective cell movements during early development of the Drosophila embryo. Using light sheet microscopy and a quantitative image analysis the observed patterns of fluorescence intensity are mapped on a closed two-dimensional surface representing the epithelial surface. In the case of fluorescently labelled myosin, patterns of myosin on the apical and on the basal side of the tissue have been quantified separately on the 2d surface. The work uses an elegant and original approach to quantify anisotropies of apical myosin using a Radon transform. In addition, flow fields are determined using PIV. The authors use the 2d distribution and anisotropies of apical and basal myosin to estimate patterns of active stress in the tissue. Using a continuum theory of an active gel, velocity fields are calculated and compared to the observed cell flow patterns. Strikingly, the authors show that the most important features of the cell flow can be accounted for from the knowledge of myosin distributions. Furthermore, the authors show that altered flow patterns in twi mutants can be explained by changed patterns of myosin distributions under mutant conditions. These are important results that provide a significant advance of the understanding of morphogenetic movements in the early fly embryo. The quantitative methods used are powerful and sophisticated. While this work is interesting and strong, there are several points that need to be addressed in a revision of the manuscript and several points need clarification.

Essential revisions:

1) A major concern as detailed below is that a lot of information is missing in the manuscript.

2) The authors do not show what the actual myosin distribution looks like, and there is little detail in how the 'coarse-grained' or 'smoothened' myosin distributions in Figure 1F-K are obtained. The corresponding supplemental figure did not really help in this regard. If the data has been smoothened to produce these plots, the original data should also be shown. Scale bars should also be added to the figures. What is the 'contrast' in the myosin signals? What is the level of intensity between dorsal and ventral in relation to the average? What are the units in Figure 1F–K, Figure 2C, etc.?

3) The model used to calculate the flow fields is shown in Figure 3A. It is unclear why the isotropic basal and the anisotropic apical signals are used only. The apical myosin also has an isotropic signal. Is this not used and why not? Maybe the notation, which is not fully explained, leads to confusion here. Is the tensor mapical traceless or does it contain an isotropic signal? This should be clarified. Presumably the isotropic and anisotropic contributions of apical myosin are contributing with two different factors. These factors should be defined and their values reported.

4) The quantification of anisotropies of the myosin distribution represents an interesting methodological advance. The presentation of the quantification of this anisotropy on the surface of the embryo is not very clear. Figure 2C and Figure 2D do not provide a full picture of the quantified anisotropy patterns. The authors should show a complete map of myosin anisotropy at different times.

5) Information about the anisotropy of the basal signal evaluated with the same method is missing. Why is the basal myosin anisotropy not contributing to the stress equation? Is it because basal myosin anisotropy is low?

6) In the appendix the anisotropy quantification using a Radon transform is explained. However, I did not see a clear definition of how the Radon transform information is used to determine the myosin tensor mapical in Figure 3A.

7) If m(r) denotes a factor positively correlated to myosin concentration, the sign of the righthand side of Equation 6 may be wrong. With the current sign, a positive accumulation of myosin would drive an outward flow. It is essential that the authors clarify this.

8) In Figure 2D it is not clear what is plotted. The caption states "Eigenvectors of myosin tensor are plotted in cyan". It is not clear if the myosin tensor is a field defined on a regular grid, of only selected vectors are shown. Shown are bars that are hardly visible to the bare eye. They do not look like vectors and it is unclear to which points they are attached.

9) The authors should provide more information on the 2D shear and bulk viscosities ν and ν' and they ratio B. If one considers the height of the tissue layer as an explicit variable and treats the tissue as isotropic and incompressible in 3D, divergences in the 2D flow field couple to height changes and the ratio of the 2D bulk to the 2D shear viscosity would be 3 (see e.g. Batchelor, 2000). How does this compare to the values that are fitted here? Can the model be simplified to 2 parameters? Can B be constant in time (I assume not, Figure 1C–E)?

10) Related comment: Please provide the values of the parameters B, α, β in a table/plot in the main text together with confidence bounds. Are α and β constant in time? The 'true' number of model parameters remains unclear. Is this really just one parameter as stated in the abstract, or is it three as stated in the main text? It remains unclear whether the viscosity ratio B was different for each time point which would correspond to effectively many fit parameters. In the main text it is mentioned that B changes with time however this is unclear and needs to be clarified. The main text refers to Figure 1C–E about this but in the figure there is no information about B.

11) It seems the authors use a single value of B that is space-independent at each time point, but then allow B to instantaneously change everywhere and synchronously in space. The motivation for this remains unclear. How could that be achieved in the embryo?

12) In Figure 1C–E it is not stated in the caption (and not even in the supplement) which fluorescence signal (apical, basal myosin, combined?) is used to calculate the velocity field. This important information that should be found easily.

13) In Figure 3C, it is unclear whether the shown flow profiles are obtained with or without the "cut" in mesoderm? We would suggest adding a figure or schematic actually showing what the "cut in mesoderm" perturbation is doing.

14) One sentence states that the comparison between theoretical and experimental plots is done using normalised velocity fields rather than real velocity fields (caption of Figure 3B: "Fit residual, comparing predicted flow field with measured flow field normalized for magnitude"). The precise way the velocities were normalized remained unclear to the referees. Was the velocity normalized at each position separately or was only the overall magnitude of the velocity field normalized? The former case would be a problem because real velocity fields should be compared including velocity amplitude patters.

15) An important result is that "the model achieves about 90% accurate description of the flow pattern before and after VF invagination". It is quite unclear how this percentage of agreement is defined and determined. Also, in the caption of Figure 3 the residual is not defined. The definition of the residual given in the methods remains a bit unclear because the notation is not well explained (which quantities depend on position and which do not, how is <[…]>embryo defined etc.).

16) The flow and myosin profiles in twist embryos are not reported. They should absolutely be shown.

17) It is not clear what information the theoretical analysis of mutants is bringing. Are the parameters used to fit the data the same as in WT?

18) It is misleading to refer to the model used in the calculations as viscoelastic. This is a description in the fluid limit and it should be referred to as such. Viscoelasticity does not enter; the corresponding viscoelastic relaxation time is not a parameter that is considered. Please correct corresponding references in the Abstract and main text, for example the language in the Results section (please add page and maybe line numbers in the revision) is confusing and the statement in the Abstract is misleading (surprisingly simple effective visco-elasticity model -> viscous model). Of course, one can arrive at a fluid-like description by considering the long-time behavior of a viscoelastic material as the authors also show, and it is certainly ok to provide this derivation. But the theory that is used in the end is fluid and not being clear here can put the reader on a wrong track.

19) In Figure 3A a coordinate independent, covariant expression of the dynamic equations is presented. The equations given in the appendix are not covariant but depend on a coordinate system. It is therefore unclear whether the continuum theory applied to the problem is covariant or not. This should be clarified. Furthermore, the finite element method used is also not clear with respect to this point and not sufficiently explained. Do the results depend on the choice of the finite element discretization used or not? If not, has this been checked? If yes, what does this mean? We understand that the authors do not want to go into notational complexities here but the conceptual approach used should be clear.
