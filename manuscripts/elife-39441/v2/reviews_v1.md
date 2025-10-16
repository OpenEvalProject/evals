# Peer review - Round 1

Editors:
- Michael M Kozlov, Tel Aviv University Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.39441.033](https://doi.org/10.7554/eLife.39441.033)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The role of scaffold reshaping and disassembly in dynamin driven membrane fission" for consideration by eLife. Your article has been reviewed by Vivek Malhotra as the Senior Editor, a Reviewing Editor, and three reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Vadim Frolov (Reviewer #1); Aurélien Roux (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The article describes the results of state-of-the-art CG simulations of membrane fission by dynamin, which, potentially, represent a considerable advance in understanding the mechanism of this phenomenon. The simulations allowed the authors to check, within the framework of their computational model, the feasibility of the previously suggested two-stage and constrictase scenarios of the process, to test whether the early suggested modes of the conformational changes of the dynamin helix can drive membrane fission, and to conclude that (i) the Darboux torque applied by the dynamin helix to the membrane is necessary for fission, (ii) the precursor of the hemi-fission stage is formation of a membrane nano-pore; (iii) the transition from the hemi-fission to the complete fission happens spontaneously after disintegration of the dynamin scaffold.

The reviewers found the results interesting and, potentially, suitable for publication in eLife provided that their comments are addressed.

Essential revisions:

1) One of the major concerns of the reviewers is a lack of the statistical validation of the results. In the current manuscript only one fission scenario is presented without any indication of the probability of its realization in the computational experiments.

Further, the statement that other scenarios, which include different combinations of the dynamin spiral constriction, elongation and rotation, are ineffective in terms of driving fission, needs a statistical substantiation.

A quantitative comparison of fission probability in all possible scenarios is necessary to validate the major conclusion of the study.

More specific questions would be: How variable is the fission pathway? How many hemi-fissions (in all cases? All with pores? Do pores ever go to complete fission directly?)? All of them are stable cylindrical micelles? All micelles shrink spontaneously to 0 length and then break upon the protein filament disassembly?

2) The quantitative characterization of the structural details of the suggested and alternative pathways has to be strengthened. Specifically,

- It is claimed that pores nucleating before hemi-fission are few nm wide and live for few microseconds, too small to be detected in real life. Of note, few nm pores are huge, not small (typical transient pores in electroporation are close/below 1 nm). Even if a pore opens for few microseconds, the integral charge transferred through it under a typical voltage bias of 100mV would be within detection limits. To substantiate the claim that the pores predicted by the proposed pathway are too small to be detected experimentally, determination of the size/open time distributions would be necessary.

In this context, the authors should comment on the validity of their strategy to simulate pores. In the case the computational method used is known to cause difficulties to simulate pore formation, it is requested that the authors perform simulations to estimate the pore formation at different tensions and compare the results to the experimental data (for example, Evans et al., 2003).

- It is claimed that pure constriction produces fission only upon complete closure of the lumen. What are the criteria for "no lumen"? How big is the difference (quantitatively, e.g. in nm) between "no lumen" and "visible" lumen seen in fissions caused by rotation+constriction? What are the variations in Rc? How Rc/its variations depend of the rotation angle/effective torque?

3) The agreement between the suggested mechanism and the existing structural data has to be further elaborated. Specifically:

- The Darboux torque is suggested to be produced when the dynamin adhesion line moves along a fixed/stable filament, e.g. via asymmetric displacement of the PH domains. This movement assumes synchronous tilting of many domains to produce the torque, yet such cooperative actions were seemingly ruled out. Then how does the torque build up? Further, can the PH domains support the torque providing that their connections to the protein stalk are rather flexible? More broadly, the torque creates stresses in the protein filament itself – is it realistic (can it be estimated) that the helical filament sustains the stress without changing shape?

Along the same lines, the authors state that tilting of the PH domain upon GTP hydrolysis could create a Darboux torque only if an asymmetric tilt occurs. In currently available cryo-EM maps (Sundborger et al., 2014), only 1 of the 2 PH domains of dimers is tilted, ensuring the required asymmetry. However, when looking at the tetrameric level, the titled PH domains are on each side of the tetramers, restoring symmetry. The authors should carefully check these points and explain how the data are compatible with their findings about the importance of the Darboux torque.

Finally, the tilting of the PH domains has been discussed in detail by biochemists, in particular, in the context of its effect on the molecular interactions between the membrane and the dynamin helix. Two levels of changes have been proposed: (i) tilting helps insertion of an amphipathic helix that helps to promote membrane curvature and thus constriction; (ii) titling breaks the specific lipid (PIP2)-dynamin bond or pulls the lipid out of the membrane. While the first change is unlikely because the amphipathic helix is located on the side of dynamin that is not in interaction with the membrane when titled (Harvey McMahon, private communication), the latter is essential for transmission of the Darboux torque to the membrane. It is thus required that the authors propose an estimate of the energy put on the dynamin/membrane bond when PH domains are tilting and compare it to the affinity values of dynamin PH domain for PIP2, and to forces required to pull off lipids from membrane.

4) The relationship with the results of other simulation models has to be thoroughly discussed. Specifically:

The conclusion that the scission of the stalk/micelle, may not be physiological relevant sounds problematic. Other simulation works show that a stalk formed between fusing vesicles is highly long living even for symmetric, membrane forming lipids such as POPC (Risselada, 2014). Those systems essentially do not differ from the ones simulated here after dynamin disassembly. In support of those results, it was recently found by one of the reviewers (using a string method) that a 'dimple' stalk formed between POPC membranes is thermodynamically stable and that scission would require a ~20 kBT barrier, quite in contrast to the here-envisaged fast rupture after Dynamin assembly. The question is whether the Crooks model underestimates the stalk stability and thereby falsely advocates the conclusion that the coined "second barrier" may not be physiological relevant. In flat membranes POPC stalks can become metastable and even stable under membrane dehydration (stabilization of the stalk is hydration repulsion driven in that case). The solvent free Crooks model cannot reveal such a behavior since it has a strong inherent tendency to form lamellar structures. Furthermore, the stalk may equally well expand after Dynanim disassembly, i.e., progression of fusion, since progression of fission and fusion are competitive pathways at this stage (they share the shame intermediate). The statement that small hemifused vesicles - which is essentially the structure one obtains after Dynamin disassembly - are poised to undergo fission is the exact opposite of the widely accepted observation that highly curved vesicles are fusogenic (even when being protein-free). In fact, there is evidence that completion of fission relies on feedback mechanisms and may involve several constriction cycles. This could suggest that scission attempts may fail, and that the mechanism perhaps relies on a dynamically imposed stress.

A related issue is the lack of movement of the (centers of mass of) daughter vesicles in Video 5 and Video 6 (comparable in size "protein pieces" move)? Is there a constraint? If so, does it affect the hemifission stability? Breakage of the cylindrical micelle upon shortening (Video 6) looks puzzling, one would rather expect formation of a stable stalk-like structure.
