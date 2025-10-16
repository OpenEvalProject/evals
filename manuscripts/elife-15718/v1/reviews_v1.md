# Peer review - Round 1

Editors:
- Eduardo A Groisman, Yale School of Medicine , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.15718.025](https://doi.org/10.7554/eLife.15718.025)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: this article was originally rejected after discussions between the reviewers, but the authors were invited to resubmit after an appeal against the decision.]

Thank you for submitting your work entitled "Bile Salt Receptor Complex Activates a Pathogenic Type III Secretion System" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Richard Losick as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Alejandro Buschiazzo (Reviewer #2).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

The reviewers and editor found the work intriguing. However, there was unanimity in the feeling that the manuscript did not provide an understanding of bile recognition in the investigated signal transduction pathway. Moreover, there were several technical and conceptual issues that are detailed in the comments presented below.

Reviewer #1:

Li P et al. report the discovery of a new protein (VtrC) as an essential element to regulate type three secretion system 2 in Vibrio. VtrC is shown to form a complex with VtrA, which is responsive to bile (a known inductor of T3SS2, ultimately modulating virulence). VtrA and VtrB had already been identified as essential T3SS2 regulators, but the mechanism of bile sensing and signal transduction remains unknown, and this is the main question the authors want to address.

After identifying VtrC, the authors demonstrate that vtrA and vtrC belong to a single operon and, elegantly, that deletion of vtrC specifically affects T3SS2 and bile sensitivity.

VtrC is further characterized as a bitopic membrane protein, which led to uncovering periplasmic interaction with VtrA in vivo (co-IP). Not affecting vtrA transcription, VtrC appears to be critical for VtrA protein stability.

1) Why didn't the authors raise an antibody against the whole periplasmic (or intracellular) domain of VtrA? (VtrA might be expressed in the absence of VtrC, but that last short segment is being degraded, or that epitope is conformational and sensitive to VtrC binding?)

2) The crystal structure of the VtrA/VtrC complex represents an important contribution, confirming the association between both proteins.

Some concerns about the crystallographic data (the authors' feedback is important):

• for a 2-wavelength MAD phasing, 0.25 seems a suspiciously low FOM figure (what can you say about the three Se sites that were not found with direct methods, on the final refined model?)

• Rfree in principle seems high (almost 30%) for a 2.7Å resolution structure. No electron density is shown. Were there any difficulties throughout refinement? Is electron density good throughout the asymmetric unit? (please include a supplementary figure with best and worst ED map regions)

• Stereochemical rmsd figures for bond lengths and angles are extremely low. Why? Were extra-tight restraints used during refinement? if yes, why?

Please briefly address these points in the Materials and methods.

3) Are there other, alternative, heterodimer architectures (or yet, tetrameric organizations etc) in the cubic packing? Please cite the next best inter-protomer buried interface surface, ruling out otherwise ambiguous oligomeric choices.

4) The structural data don't seem to contribute all that much into a mechanistic understanding. Particularly, the ligand-binding site cannot be pinpointed as the authors admit. Did the authors attempt crystallizing the complex in the presence of TDC or other potential ligands? Make this explicit. Structurally assessing how VtrA-VtrC recognizes bile would be a major mechanistic insight (see next).

5) TDC is used as the sole ligand assayed by ITC, based on a previous report, but bile is really heterogeneous. The authors would benefit of incubating the complex with bile, then purifying and crystallizing (also MS can be helpful), attempting to see and/or identify ligands, which may not be TDC. Actually, the authors claim that TDC binds with nM affinity, which is somewhat misleading. KD is actually on the low microM range (i.e. nearer microM than nM, in contrast to most FABPs used as reference in Richieri et al. 2000 Biochemistry). "Nanomolar" should thus be changed to "low μM" in the Abstract and Discussion. Maybe other bile components bind tighter and are relevant physiologically?

6) Structural data would also be valuable to understand the critical role of interacting residues in the VtrA/VtrC interface. Structure-based mutants of vtrC can be analyzed on the vtrC-knockout background by the kind of functional assays that the authors have performed.

7) The major concern overall for the paper is indeed the mechanistic insight, which was the main question the authors sought to answer in the first place. Figure 9 is too vague: which bile component(s) binds physiologically? If it were TDC, where does it bind on the VtrA/VtrC complex? What are the characteristics of the signal-triggered rearrangement of VtrA (and/or VtrC)?

Alternative hypothesis: VtrC stabilizes (somehow) VtrA, but it is VtrA on its own that binds bile components and transduces the signal. Given that recombinant VtrA's periplasmic domain is available, it would be important to assess its own capacity to bind TDC (using ITC). And, if really no binding is detectable, did the authors attempt crystallizing the VtrA periplasmic domain on its own? This structure could well inform about VtrC-triggered rearrangements.

Reviewer #2:

This manuscript by Li et al. describes research that increases understanding of how bile induces Type Three Secretion in Vibrio parahaemolyticus. It had previously been shown that the proteins VtrA and VtrB were necessary for bile-mediated induction of the T3SS2 system, and VtrA activated VtrB in response to bile. This paper identifies a new component of this system, VtrC, that is in the membrane associated with VtrA. The authors crystalize the periplasmic interacting domains of VtrA and VtrC, in the absence of bile, and show the complex binds bile. This is a nice manuscript that definitely increases our understanding of this process, but I feel the authors overstep a bit in terms of the novelty of this work and their conclusions that they provide mechanistic insight into this process. Therefore, my enthusiasm is somewhat tempered.

1) The authors state that "the mechanism of bile sensing by these bacteria remains elusive". From the introduction, it would seem that not bile responsive proteins have been identified, or the impact of bile on these proteins elucidated. However, in Vibrio cholerae ToxT binding to bile inhibits its ability to bind target promoters, and as the authors state in the discussion bile has been shown to induce disulfide bonds in ToxR.

2) The authors don't really uncover the mechanism of VtrAC bile sensing, but just another important component of the system. For instance, I was surprised that the authors did not use the crystal structure to engineer mutations that would be predicted to disrupt the interaction or disrupt the binding to bile. Moreover, no structures are determined with bile, and they only identify the structure of the periplasmic domains, so how bile binding is transduced to changes in DNA binding affinity is not understood. They clearly make important advances, but this manuscript does not provide the mechanism of bile sensing.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for resubmitting your work entitled "Bile Salt Receptor Complex Activates a Pathogenic Type III Secretion System" for further consideration at eLife. Your revised article has been favorably evaluated by Richard Losick (Senior editor), a Reviewing editor, and two reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below.

There some questions about the processing of the diffraction data, which should be addressed before the manuscript can be accepted for publication. These questions are as follows:

The authors should be aware that the F432 cubic space group is extremely rare in protein crystal structures (~200 entries belonging to it, among the >105 structures in the PDB). So, although possible to encounter, as with any unusual discovery, one should be extra cautious to avoid mistakes.

For the next few comments, you might want to check whether your space group assignment was correct (or could there be a form of pseudo-symmetry?). Pseudo-symmetry often results in regions of the alleged ASU with weak electron density and greater difficulty in model building. This is why I had asked previously about how good the electron density is, not only in the good parts, but also in the bad ones (the authors misunderstood replying only with the obvious: that density is better in the core and worse in the flexible solvent-exposed regions). A mistake in the space group could end up being worrisome in giving parts of the model wrong (even on top of parts that are right). The new structure in complex with TDC, is in part reassuring (a confirmation with different packing), but some figures of its own, also raise questions.

Issues that have remained unanswered:

1) Phasing FOM too low: 0.25 is suspicious for a MAD experiment. Could be explained because of too little anomalous signal (e.g. only two methionines for approx. 200 residues – probably a quite tough phasing scenario). Again, my point was to think (and test!) whether there is a lower symmetry possibility to integrate the data in, and then see if shelxd works better. Straightforward tests that you can also perform to scrutinize this SG assignment: a) use ccp4 program zanuda to analyze your cubic data, it will systematically test for lower compatible space group choices (and also perform some initial refinement for each, to have comparative figures); b) reintegrate the cubic data in P1, and perform mol replacement now that you have a solution (which is maybe completely right, or at least partially right for sure), searching for as many hetero-dimers as you calculate according to the triclinic unit cell volume: if a solution is found, than you can analyze if the packing indeed conforms to a such highly symmetric space group as F432.

2) Maybe it is cubic, end of story.

3) But, if alternative choices do appear, not only shelxd might give better FOM, but actually maps may turn out better (in the bad parts, if there were); final refined average B factors closer to Wilson B (this is a definitely strange behavior reported in your table); better Rmerge statistics (also high, not only in the high resolution shell, but also in the low res – I know high multiplicity is here at play, so I do not want to say this is necessarily wrong: just look closely and critically at it, to avoid mistakes).

4) I would strongly advise against including hydrogen atoms in the refinements. Else, explain really well why you think it's OK to include them. This goes also for the orthorhombic form with TDC. The validation reports seem clear in that you have included them: to support a refinement strategy with independent H atoms you would need ultra-high resolution (i.e. better than 1.2Å) or a neutron light source for the diffraction experiment.

5) The nominal resolution for the new orthorhombic structure is probably not 2.1Å: very low completeness of the data (57% high res shell). Please reconsider this. Actually, please elaborate as to why completeness drops significantly comparing the processed data vs those used for refinement.

It is suggested to reduce/simplify subsection “The VtrA/VtrC complex is an obligate heterodimer”; it's enough there to indicate that only 2 Se-Met out of the 5 present in the protein complex, were ultimately seen to be ordered in the refined model, hence contributing proportionally little to the measured anomalous signal in the first place (likely explaining the low FOM figure at the phasing step, previous to density modification).

In this context it is rather misleading to state that the 2 Se-Met "were used for refinement", actually you are probably talking here about their use to solve the substructure of anomalous scatterers for subsequent protein phasing purposes.
