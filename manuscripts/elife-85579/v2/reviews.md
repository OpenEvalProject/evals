# Peer review - Round 1

Editors:
- Jie Xiao, https://ror.org/00za53h95 Johns Hopkins University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85579.sa0](https://doi.org/10.7554/eLife.85579.sa0)

This valuable work reports a unique N-terminal motif of Staphylococcus aureus GpsB, the co-crystal structure of GpsB with the C-terminus of PBP4, and the direct interaction between GpsB and the C-terminus of FtsZ. The evidence supporting these discoveries is convincing, with biochemical and structural characterizations. This study sheds light on the role of GpsB in the cell division of this important pathogen.


---

# Peer review - Round 1

Editors:
- Jie Xiao, https://ror.org/00za53h95 Johns Hopkins University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85579.sa1](https://doi.org/10.7554/eLife.85579.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Staphylococcus aureus FtsZ and PBP4 bind to the conformationally dynamic N-terminal domain of GpsB" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Bavesh Kana as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Tobias Doerr (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions (for the authors):

The reviewers identified that the study of S. aurues GpsB and its interactions with FtsZ and PBP4 is important for understanding the essential role of GpsB in the cell division of S. aureus. However, the structure of GpsB and PBPs has been reported before in B. subtilis and S. pneumoniae, and the functional characterization of GpsB's new motif and the structural characterization of GpsB and FtsZ's interaction is incomplete. The manuscript requires extensive revisions to address two essential points raised by the reviewers.

1) Please address the functionality of the 3-aa insertion/kinked structure motif in S. aureus GpsB by providing new experiments as requested by Reviewer #1, points 1 and 2, and Reviewer #3, point 1 (first paragraph of recommendations to authors).

2) Please provide a structural characterization of GpsB in complex with the C-terminus of FtsZ. If a co-structure is not possible, please provide justifications and/or a discussion on a predicated model using Alphafold2/RosettaFold.

Reviewer #1 (Recommendations for the authors):

1. The crystal structure revealed similarities and differences between Sa GpsB and GpsB from other species. Sa GpsB contained a hinge in the helix that results in bending of the protomer. This feature was not observed in other species. The authors provided strong evidence showing that the hinge was not a crystallization artifact but a novel motif through stability measurements, NMR, and MD simulations (Figures 1 and 2). The authors further tested the effects of deletion of two 3-residue insertions uniquely present in Sa GpsB (∆MAD and ∆MNN) using the lethality of Sa GpsB overexpression in B. subtilis (Figure 2). While these experiments are important, the overexpression of ∆MAD or ∆MNN in S. aureus appeared to have a modest effect (Figure S4), thus it may be difficult to argue that the hinge is important for Sa GpsB function. The authors hypothesized that this modest effect is due to the differential affinity of ∆MNN to itself than Sa GpsB, but it is unclear how it would explain the modest effect. Furthermore, these mutational investigations may be better/easier to interpret if mutants are expressed in wt gpsB depletion background.

2. To complement these experiments, perhaps the authors could insert MAD or MNN into Bs GpsB and monitor the mutants' thermostability, localization, and lethality in B. subtilis subsequently. Additionally, overexpressed WT Sa-GpsB mislocalized in B. subtilis and was lethal, while overexpressed ∆MAD and ∆MNN localized to the mid cell and cells were normal. Do these results indicate that the lethality of SaGpsB in B. subtilis is a nonspecific protein aggregation effect and that the two regions are responsible for the aggregation? What protein-protein interactions contribute to the mid-cell localization of SaGpsB in B. subtilis? If the toxicity of Sa GpsB in Bs is caused by the hinge structure one would expect mutating the Bs GpsB to include it would also have a similar toxic effect.

3. The discovery that the CTV of Sa FtsZ has a repeat match of the consensus GpsB binding motif is interesting. The binding affinities at ~ 20 to 70 μM, however, do not appear to be strong. The authors suggested that cellular affinities may be higher and a regulatory point. Could the authors provide a negative control using Sa FtsZ∆6, or a peptide from another species that does not have the motif to rule out sequence-independent binding? These controls may be important because the FtsZ (320-390) terminus includes the two negatively charged E but binds tighter than FtsZ (379-390), which also contains the two E residues. Additionally, if we assume that the crystallographic work between the FtsZ terminus with Sa GpasB is not successful, can a structure be deduced from the NMR study?

4. As the FtsZ CTV's binding motif is similar to that of PBP4, do they compete with each other, or can they both bind to two monomers of GpsB simultaneously? How important is this binding? The authors reported that ∆MAD has lost the binding to PBP4 and FtsZ CTV, but it is hard to imagine how the structure that is different from the binding site causes a significant reduction in binding. To demonstrate the importance of binding, the authors may wish to design some mutations at the binding surface and exam the consequences in cell physiology.

Reviewer #2 (Recommendations for the authors):

While I appreciate the efforts in providing a solid base for the characterization of the interactions between GspB and FtsZ or PBP4; I consider the novelty is not enough to publish in eLife considering the previously published works.

– Results. When describing the 3D structure of the GspB N-term domain; Did authors run AlphaFold2 (AF2) to see the prediction of the hexameric full-length structure? Is this configuration compatible with interaction with other partners? How the discovered hinge could affect the oligomeric arrangement of the full-length protein? How these results could compare with GspB from other bacterial species for which this region has been also solved?

– Results. Line 201. Also, as there is no 3D structure for the complex between the N-term domain of GspB and the C-term domain of FtsZ, AF2 prediction could be important to identify if the same pattern of interactions observed for PBP4 are observed here, and maybe to identify key residues in this interaction. Mutagenesis experiments could then validate this interaction.

– Results. When describing the interactions between GspB and PBP4, authors should directly compare with previous interactions observed for GspB in B. subtilis and S. pneumoniae (Cleverley et al. Nat Comms 2019). Now, this information is only partially presented when comparing crystal packing in S. aureus GspB with the complex GspB:PBP1a in B. subtilis.

Two Arg residues seem to be critical in the interaction with PBPs, is this interaction lost if you mutated both of them?

– Figure 5. Please indicate how this model was generated. Is this just an artistic representation of the partners? is based on previous structures? or on predictions by AF2?

Reviewer #3 (Recommendations for the authors):

This is a nice study overall, and very well-written and well-organized. My main issue is with the overexpression experiments. Overexpression toxicity of divisome components can be highly pleiotropic and is difficult to interpret. I don't follow the conclusion that the insertion sequence is important for function since an assessment of functionality is only based on overexpression toxicity. Can you replace native GpsB with the ∆MAD and ∆MNN mutants? This would be the ultimate test of functionality. If not possible, you could conduct depletion experiments of the wild-type copy in a background expressing the mutants.

It is unclear to me why the ∆MAD/MNN mutants are less toxic than the WT (see my minor comment below as well). I don't find the bacterial two-hybrid data very convincing. BACTH is not necessarily quantitative, so more precise experiments (ELISA?) would be necessary to conclude something about the affinity of heterocomplexes. Since the exact mechanism of toxicity is not important for their conclusions, maybe tread a little more lightly here. The statement in line 185 is a bit too strong.

Figure 3C needs a negative control. Not knowing if a value of ~1.5 in their GTPase assay is significantly above the background, it is possible that the ∆C6 mutant is simply catalytically dead, and thus cannot be activated by GpsB. A GTPase point mutant in FtsZ would be a great control here to establish whether FtsZ without GpsB has activity significantly above background, and would consequently demonstrate that the ∆C6 mutant is specifically deficient in GpsB-mediated activation.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Staphylococcus aureus FtsZ and PBP4 bind to the conformationally dynamic N-terminal domain of GpsB" for further consideration by eLife. Your revised article has been evaluated by Bavesh Kana (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Please add discussions regarding the putative arrangement between FtsZ and GpsB in Figure 5, either by Alpah-fold2 predication as Rev #2 suggested, or textual justifications.

Reviewer #2 (Recommendations for the authors):

The authors have partially responded to my previous review.

It seems that more detailed information on the C-term FstZ and GpsB interaction is ongoing for future work.

The predicted model by AF multimer of the N-term GpsB dimer and the C-term of FtsZ is straightforward to do, and this model could reinforce, at this moment, the experimental results provided in the manuscript. If the AF multimer fails, thus it can be just mentioned in the manuscript.

Other potential implications of this in silico experiment, could be to know if the GpsB dimer interacts with one or two FtsZ chains.

Also, as a proof of concept, the same AF multimer run can be done with PBP4 and GspB to see if a more extended picture of the PBP4-GspB complex can be reached.

Reviewer #3 (Recommendations for the authors):

The authors have adequately responded to the first round of reviews. I still believe that an FtsZ GTPase mutant would be the better control for the biochemical assay showing stimulation of GTPase activity by GpsB, but BSA is adequate.

I also still believe that a true examination of the functional importance of the hinge domain residues would require replacement of the native GpsB with these variants, followed by phenotypic characterization (though my understanding is that ∆gpsB phenotypes are subtile, but measurable nonetheless via e.g. morphology). The current reliance on overexpression toxicity (which was pointed out during the first round of reviews) makes interpretation of these data more difficult. That said, using a gpsB mutant for overexpression experiments is certainly an improvement over the first version of the manuscript.
