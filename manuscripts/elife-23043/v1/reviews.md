# Peer review - Round 1

Editors:
- Kenton J Swartz, National Institutes of Health , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.23043.021](https://doi.org/10.7554/eLife.23043.021)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Structural insights into the molecular mechanisms of Myasthenia Gravis and therapeutic implications" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Kenton Swartz as the Reviewing Editor and Richard Aldrich as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Jon M Lindstrom (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript from Lin Chen's group describes structural efforts to understand the interactions of an antibody with the nicotinic receptor that can trigger myasthenia gravis (MG). The manuscript presents the first high resolution structure of a soluble extracellular domain of the alpha1 subunit of the nicotinic receptor in complex with a Fab fragment from the standard antibody known to cause experimental myasthenia gravis. The authors use the structure of this complex as a basis for speculation on the relative significance of different atomic interactions at the receptor-Fab interface in determining subunit specificity, and perform sequence comparisons and qualitative binding assays by native PAGE to test binding to the soluble extracellular domain of the alpha1 and alpha9 subunits. The authors then present a speculative mechanism suggesting that cross-linking of pentamers by the whole IgG could trigger membrane deformation, resulting in receptor internalization and eventually myasthenic syndrome.

The strengths of this manuscript and underlying work are in the introductory and structural sections. The authors lay out nicely the physiological background and significance, setting up the structural findings effectively. This piece of the study, alone, is impactful. We have some concerns about the refinement details, described below, but we do not expect those issues to change the overall interpretations or conclusions made in the manuscript. The following are essential revisions that are needed to improve the presentation.

Essential revisions:

1) The crystallographic statistics raise two issues that need to be addressed. First, for both datasets, there is an unacceptably large spread between R and Rfree (8.5-10%). This large spread suggests a high degree of model bias and inappropriate restraints used during refinement. This large spread is surprising given the relatively small spread between R and Rfree in the original alpha1-bungarotoxin complex structure from the same group (2.4% difference, PMID 17643119). Second, the Ramachandran statistics are poor; >90% of the residues should be in the favored region, and good justification should be made for any residues in the outlier region. Strong electron density and/or comparison with higher resolution structures is a requirement for confidence in modeling a residue in an outlier conformation. Thus, regions with poor electron density should have better Ramachandran statistics, not worse, as suggested by footnote b in Supplementary file 1. The authors need to address these two issues either by improving the quality of the refined model or explaining why the statistics, as they currently stand, are justified. One way to improve model quality without too much effort might be using a reference model during refinement (phenix.refine makes this reasonably straightforward).

2) The mechanism suggested for pentamer cross-linking inducing curvature and thereby internalization and pathology is very speculative and needs to be toned down. The reference cited in the Discussion (Drachmann et al., 1978) on cross-linking and curvature does not, as far as we see, actually propose, test or validate a curvature mechanism. As the authors discuss, modeling of cross-linked pentamers is tentative, in part because it relies on the older EM model of the Torpedo receptor, which has a 'funny' alpha1 helix conformation compared to all other structures, and in part because Fabs/IgG's have a great deal of inherent flexibility. We request that you move Figures 6 and 7 to a single supplemental figure and to limit presentation of this hypothetical mechanism to a single paragraph in the Discussion section.

3) The manuscript would have been strengthened by the addition of mutants and binding assays to specifically interrogate the interface seen in the X-ray structure. Although we appreciate that this would require considerable additional work, the authors can and should bring in the literature to help support the interface they see in the structure, as Luo et al., 2009 and others have predicted some of the interactions seen in the present study.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Structural insights into the molecular mechanisms of Myasthenia Gravis and therapeutic implications" for further consideration at eLife. Your revised article has been favorably evaluated by Kenton Swartz as Reviewing Editor and Richard Aldrich as Senior editor, and two reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

1) There is something funny going in paragraph four of the Discussion section. A part of one sentence appears to have been deleted.

2) It would be helpful for the authors to include a few remarks on the following two issues:

Although mAb 35 and mAb 198 are very similar in structure, other EAMG and MG antibodies that bind to this region may not be so similar or bind to identical epitopes. The high frequency of MIR antibodies in MG and EAMG sera was determined by competitive binding between mAbs with serum antibodies. Figure 1 clearly illustrates how large Fab 35 is with respect to the extracellular domain of α 1. Large intact mAb 35 is likely to compete with intact large serum autoantibodies for binding in this region to nearby but somewhat different epitopes than are recognized by mAb 35. mAB 192 is a similar case. The relative size of an antibody and an AChR is nicely illustrated in Figure 6C. The variety of epitopes in the main immunogenic region is an important factor relevant to the Discussion, paragraph two, about trying to treat MG with mimotopes or for developing epitope-specific diagnostics.

In the Results section it is noted that the N terminal α helix of α 1 in Torpedo AChR differs from that in Bellone, Tang, Milius and Conti-Tronconi, 1989. It is worth noting that Morell et al., 2014 shows that variations in MIR structure have large effects on ACh sensitivity. AChR sensitivity involves both ACh binding sites and transmembrane regions. The transmembrane regions are greatly effected by lipid. Solubilization of Torpedo AChRs puts them in an inactive conformation that can be corrected by reconstitution into the proper lipid composition (C daCosta and J Baenziger (2013) Cell Structure 21: 1271-1283). Most crystallized receptors are solubilized and consequently contact lipids partially or completely removed. The 5-HT3 receptor after solubilization was crystallized bound to nano bodies directed at its C loops that function as potent antagonists (Hasssaine et al. (2014) Nature 512: 276-281). This too may have global conformation consequences. Torpedo AChRs are unique in having had their structures determined in their native membrane. Of course, artifacts in their structural determination might also occur.
