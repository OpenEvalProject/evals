# Peer review - Round 1

Editors:
- Merritt Maduke, https://ror.org/00f54p054 Stanford University School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73124.sa0](https://doi.org/10.7554/eLife.73124.sa0)

This paper presents crystal structures of sCoaT, a heavy metal transporting P-type ATPase. These structures and complementary functional data define the overall fold of this protein and provide insight into several mechanistic features, including a conserved histidine proposed to act as a novel counter-ion during transport. This work will be of interest to biochemists and microbiologists interested in the transport of transition metals, structural biology of membrane proteins and drug development.


---

# Peer review - Round 1

Editors:
- Merritt Maduke, https://ror.org/00f54p054 Stanford University School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73124.sa1](https://doi.org/10.7554/eLife.73124.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Structure and ion-release mechanism of PIB-4-type ATPases" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Olga Boudker as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Kazuhiro Abe (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this letter to help you prepare a revised submission. Overall, the reviewers find your manuscript to reflect an interesting and significant study. There are several revisions, however, necessary to strengthen and clarify points, particularly around interpretation of the structures, metal selectivity, and use of MD simulations.

Essential revisions:

Metal selectivity:

1) The characterization of sCoaT activities was carefully done. However, it is unclear why results obtained in this study regarding metal affinity (especially Co2+ and Zn+) is largely different from the previous report (ref 18). Authors just wrote the observed discrepancy is due to the different experimental conditions. Although previous study employed the ATP regenerating coupling assay to determine π release instead of Pi-Mo endpoint assay used in this study, these difference unlikely affect to the determined metal affinity. Are these differences due to the different detergent used (DDM vs C12E8), soybean phospholipids? or different protein sequence? It is helpful for this field to show what is important for measuring ATPase activity of sCoaT. Therefore, please describe possible reason for these discrepancies if authors aware it. Related, XY scattered plot with sigmoidal curve fitting is better than the current version of bar graph format in Suppl Figure 2b. The current form is somewhat misleading for Zn and Co affinity.

2) While discussing the N-terminus, which contains metal-coordinating residues), the authors conclude that “the residues upstream of MA are not essential for catalytic activity” The data shown in Figure 2 support this statement. However, it would be important to determine whether the deletion of the N-terminus affects metal selectivity. If the N-terminus helps to discriminate between Zn and other metals (for example by binding and increasing local concentration of Zn over Co), then the conclusion that “ this level of regulation is absent in PIB-4-ATPases” would not be correct. Thus, it would be helpful and informative to perform the metal titration/activity experiment for the N-terminally truncated construct and compare Zn and Co.

3) Both SsZntA and sCoat transport zinc. As written, it is unclear how structural differences between these transporters affect zinc transport. It would be helpful to state more clearly whether the rates and metal affinity are similar or different for these two pumps.

Interpretation of Structures:

4) To strengthen the presentation of the science, the authors should show electron density associated with the BeF3- and AlF4- ligands and describe how they differentiated the bound ligands from other potential bound substrates (phosphate). The authors should also soften their conclusions regarding the conformational states of the two structures, as they seem to be the same state trapped in the same crystal form.

5) X-ray structures were well modeled as seen in the impressive Rw/Rf values regardless of relatively low-resolution data. However, due to the absence of crystal packing at TM region, TM helices and extracellular side of the protein portion showed poor densities. Although authors overcame this problem of TM modelling by employing ISOLDE, these parts (TM helices and extracellular loops) may be less reliable compared to other well-resolved regions such as cytoplasmic domains. Especially, the extracellular portion of TM6 is important as this portion is directly related to the conclusion of this paper, and hence the electron density map and atomic model should be displayed. In Suppl Figure 4a, TM6 is only shown around H657, and its extracellular side were not shown. In Suppl Figure 4 b, electron density at lower part of TM6 looks sparse, and seems difficult to construct reliable model at this contour level. Related to this issue and also described later, MD trajectories show that the displacement of either E120-E658 or W118-P652 occurs very early stage in all the simulation. This seems to be a consequence of the initial model (crystal structure) being deformed by the MD force field, rather than a conformational change of the enzyme occurring during the transport cycle.

6) It is unclear what does a unique arrangement of the A domain in sCoaT mean (Line212-216), 14 degrees and 3.5A displacement compared to the SsZntA in the same E2.Pi state (Suppl Figure 7). Is it due to the A-domain extension found in sCoaT (L216)? Alternatively, even though TGE motif is superimposable, this 15 degrees tilted A domain conformation in sCoaT is rather similar to E2BeF ground state of SsZntA? If so, comparison with ZntA E2-BeF state is missing and this comparison should be added in the figure (as in Suppl Figure 7), otherwise readers cannot judge whether observed conformation of sCoaT A domain is close to E2P or E2.Pi state of ZntA.

MD Simulations:

7) Structure analysis defined that the BeF-bound form represents a late E2P state (L211, and also concluded in the paragraph starting L280), and AlF-bound form corresponds to E2.Pi transition state (L200). In both states, the relationship between phosphate analog and TGE motif indicates that these are clearly outward-occluded E2.Pi type rather than outward-open E2P ground state. Given that the extracellular gate closure occurred in TM region is coupled to the cytoplasmic domain arrangement, gate opening cannot be expected for both states. Following this logic, the evaluation of gate opening based on the gate-closing crystal structures itself does not make sense. Even though the gate opening is observed in the MD simulation, it is unlikely to occur, at least, does not represent meaningful conformational change in the transport cycle.

Based on this point of logic (for example, one would not expect the outward gate opening in the K-occluded E2-Pi state of NaKATPase), there was a strong suggestion that removing the MD simulation would improve the quality of the manuscript. Doing so would not lessen the conclusions, because you can reach the same conclusion with the simple structural comparison between previously published gate-open SsZntA and present gate-closed sCoaT, to show the metal exit pathway, as these heavy metal pump belongs the same P1B group and possess very similar topology and helix arrangement.

The reviewers discussed whether there could be any usefulness in retaining MD simulations in the manuscript. It was pointed out that you had difficulty modeling the transmembrane domains of the structures, so MD could be an interesting way to look at the stability of the model. It could be that the extracellular gate is not tightly closed in your MODEL, which is what allowed the MD to reveal a plausible ion pathway. This point would be need be strongly clarified in the manuscript

8) Figure 2 and Suppl Figure 8 is confusing. Figure 2d shows E2-BeF (MD) in which E658 does not reach to the E120, but in Figure 2g author showed E2-AlF (MD) result and try to indicate E658-E120 interaction, a 4.5A distance is too far to form sufficiently strong hydrogen bond though. Authors described that gate opening in MD simulation is occurred like showing in Figure 2e, in which lower portion of TM6 is unwound (E2-BeF,MD). However, in Figure 2g and Suppl Figure 8a (E2-AlF, MD) shows different conformational change (probably entire TM6 shift outwardly?).

Other:

9) It is evident that E658 is important for the sCoaT function from the mutagenesis study. However, it is unclear the argument of why E658 is expected to be facing to the metal-binding site in E1 state without having E1 structure.

10) As a correction, E568 in L250 should be E658.

11) The presence of CxxC motif in the MA is an interesting and important finding, as it is generally assumed to be the past of HMBD. To assist the readers and increase clarity, it would be helpful to illustrate the location of this motif in the structure using a cartoon similar to those shown in Suppl Figure 1. Such supplementary cartoon can also show the sequence of the N-terminus. Current illustration of the metal binding residues in the alignment figure using dark green shading obscures rather than highlights these residues.

12) The question about the role of the "platform" is intriguing but simply raising it without offering alternative seems unsatisfactory. Given the flexibility of GlyGly one wonders whether during the transport cycle the "platform" helix straightens and whether the MB'-M1 loop interacts with the N-terminal metal-binding residues to position the N-terminus in the vicinity of the transmembrane domain. Can the platform be a part of the cytosolic gate? The authors may decline to speculate, but would appreciate hearing their thoughts about the possible role of the "platform" helix.

13) In the sentence (lane 314) “uncover several leads that abrogate function…” replace word ‘leads” with “compounds”.

14) It is unclear whether the identified inhibitors specifically abrogate the zinc transport activity of sCoat or equally affect transport of other metals. The authors imply that the broad metal specificity of P1B-4 ATPases is important for virulence. Therefore, it would be of value to perform experiments to show that the inhibitors block the metal-dependent ATPase activity or transport of metals other than zinc. However, such experiments are not essential for this manuscript.
