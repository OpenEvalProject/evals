# Peer review - Round 1

Editors:
- Pierre Sens, Institut Curie, PSL Research University, CNRS France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.48646.sa1](https://doi.org/10.7554/eLife.48646.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper reports and interesting modular approach that allow dissecting the molecular feature of the minD-minE biochemical network that allows for the generation of dynamical patterns of membrane composition. Four features of MinE are relevant to pattern formation; activating MinD's ATPase activity, membrane binding, dimerization, and a switch between an active and an inactive conformation. It was known from previous studies that structural switch and membrane binding are dispensable, while ATPase activation is required. This study shows that the ATPase activity is indeed essential, but must be coupled either membrane targeting or dimerization to generate patterns. The in vitro experimental study is nicely complemented with directly relevant modelling, and the modelling makes interesting predictions for how the variants would behave in the confined geometry of real E. coli.

Decision letter after peer review:

Thank you for submitting your article "Design of biochemical pattern forming systems from minimal motifs" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The minD-minE system is a very well study example of a biochemical network that generates dynamical patterns. The goal of this paper is to dissect which features among four – ATPase activity, membrane binding, dimerisation and conformation switch – of the minE protein is necessary for the emergence of patterns. It is known from previous studies that structural switch and membrane binding are dispensable, while ATPase activation is required. The authors show that the ATPase activity is indeed essential, but must be coupled either membrane targeting or dimerization to generate patterns. However, membrane targeting produces patterns of much larger wave-length then wild type, and dimerization lead to less coherent patterns (also with larger wavelength). Conjunction of the three features lead to patterns that are still less robust than wild type. These finding are rationalised within a pre-existing theoretical model via a modification of different reaction rates. The model is then use to predict how patterns produced by the different constructs in an in-vivo geometry.

The reviewers found this study novel and likely to be of general interest. They were particularly positive regarding the modular approach used to dissect the molecular requirement for patterning. The in vitro experimental study is nicely complemented with directly relevant modelling, and the modelling makes interesting predictions for how the variants would behave in the confined geometry of real E. coli.

However, there are several aspects that should be strengthened or clarified.

Essential revisions:

On the experimental side.

1) The reporting of experimental results rather succinct. One would in particular expect a more thorough analysis of the role of concentration. Figure 2—figure supplement 2. show only two titration curves, while three constructs lead to patterns. To what extent does the wave length of the pattern depend on concentration. These are important issues, since they can also be addressed by the model, and hence reinforce the comparison between the two approaches.

2) When studying the minimal, ATPase activating peptide of MinE, it is found that membrane binding by MinD remains dominant. It is surprising that at high peptide to MinD one does not see a lack of membrane binding by MinD as the peptide has been shown to stimulate the ATPase activity of MinD (paper by Goto in PNAS).

3) By adding a dimerization or MTS motif the authors find they can recover pattern formation (albeit different from each other). Does the dimerized peptide result in less coherent pattern than the I24N mutant used in a previous study? If so can the authors guess as to what feature of dimerization leads to this difference?

4) The text states "but the exact outcome depended heavily on the starting conditions of the assay". What exactly is meant by "starting conditions"? Does this refer to different concentrations, or do the authors observe qualitatively different outcomes even for the same nominal initial conditions including concentrations?

5) Given that minE dimerisation is sufficient to produce pattern of similar wavelength than the wild type, and that dimerisation with membrane targeting does not gives the same robustness as wild type (which also present conformation switch), it would seem natural to try a construct that includes a conformation switch but no membrane targeting. Why was this construct not studied?

On the modelling side.

6) Parameters. For the mathematical model, there are many parameters that have to be set. The authors do a good job of explaining the model, the parameters, and their values (except that kE is reported alternately as 5 micron3 s–1 in the legend to Figure 3 and as 10 micron3 s–1 in the Parameters in vitro section). However, the reader is left with little insight into how these parameter values were determined. Even if this is somewhat repetitive with previous works, it would be beneficial to add to the current summary of parameter values in the Materials and methods section an additional presentation of all the parameters in the SI with explanations for the sources of the values.

7) The model depends on a limited number of parameters, including minE recruitment rate by minD and minE membrane binding rate, but also on the concentration of minD and minE. The results of the model are shown in 2D phase diagram, without explaining how the pattern formation depends on concentration. It is claimed that dimerisation increases the recruitment rate and membrane targeting decrease minE unbinding rate. While the latter seems reasonable, the former is more questionable. Recruitment could be diffusion-limited, and dimerisation could rather also decrease the unbinding rate. In addition, a dimer of the MTS should have higher recruitment to the membrane just as a dimer of the peptide has higher recruitment to MinD.

These questions could be addressed addressed by extending the modelling to account for the properties of the different construct on the different reaction rates. They could also be addressed by comparing the concentration-dependence of pattern formation with the theoretical predictions.

8) It is found experimentally that the patterned obtained by the different construct have different length scales than the wild type ones. Is it possible to comment on this from the modelling point of view, while still remaining within the realm of linear stability, by discussing how the most unstable wavelength (as in Figure 3—figure supplement 2) varies for the different constructs.

9) The MinE conformational switch. In addition to the features of MinE explicitly addressed in this study, MinE is known to undergo a conformational switch. Indeed, some of the authors recently published a detailed study of the role of this switch (Denk et al., 2018), and concluded that it increases robustness of oscillations to the MinE/MinD ratio. While the dimerizing constructs of MinE used in the experiments may not be conducive to study of the conformational switch, it should certainly be possible to model the separate role of this switch, for example in the absence of the membrane targeting domain.

A final remark:

The predictions for the in vivo behavior of the various MinE constructs are exciting. The current study would have a much greater impact if these experiments were actually performed. While the current study clearly has novelty and general interest, could the effect of the different construct be studied in vivo?
