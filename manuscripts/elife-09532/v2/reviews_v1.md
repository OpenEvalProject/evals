# Peer review - Round 1

Editors:
- John Kuriyan, Howard Hughes Medical Institute, University of California, Berkeley , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.09532.036](https://doi.org/10.7554/eLife.09532.036)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for submitting your work entitled "Residue proximity information and protein model discrimination using saturation-suppressor mutagenesis" for peer review at eLife. Your submission has been favorably evaluated by John Kuriyan (Senior editor) and three reviewers. One of three reviewers has agreed to reveal his identity: Dan Tawfik.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

Review:

The authors present a novel approach to determine 3D contacts in proteins using mutagenesis scans. They demonstrate the value of the inferred 3D contacts by showing their utility in discriminating between inaccurate and accurate 3D models. The experimental methodology involves an initial single mutagenesis scan that is used to identify residue mutations for a secondary mutation scan on that particular background.

In the case of the bacterial toxin CcdB, the single saturation mutagenesis scan was previously published by themselves (Adkar 2012). In this current work, they choose 5 deleterious mutations, based on a "RankScore" identified in their previous work. On each of the 5 backgrounds they did an exhaustive second site scan to find suppressors; i.e. those mutations that rescue the deleterious effect of the single mutation. They find a total of 10 suppressor mutations and then divide these into those likely to be contacts or not (proximal or distal) based on the RankScore of the suppressor mutation in the single saturation scan. Those secondary mutations with low deleteriousness – low RankScore – in the first scan are assumed to be 3D contacts.

The idea of using systematic suppressor-mutagenesis for the determination of protein structures is highly appealing, and constantly in 'the air'. Several groups are engaged in such efforts, and this paper may well be the first actual demonstration of what is likely to become a very powerful methodology. Specifically, the prediction demands a large number of sequences, and in such families, crystal structures are more likely to be available anyway. Membrane proteins comprise a particular challenge that this paper addresses.

Overall, this work is highly valuable, and the mechanisms of suppression are interesting. The manuscript, however, demands some rewriting, and a few critical points need to be addressed or clarified in a satisfactory manner before the paper can be considered acceptable for eLife.

Major concerns that must be addressed:

1) A key idea underlying the method is the discrimination between proximal and distal suppressor mutants, where the proximal ones will indicate physical contacts. The key result is given in Table 1. Based on this Table, 5 positions are mutated and 10 suppressor mutations tested. Thus, the crux of these methods (systematic suppressor mapping) is how to distinguish between distal and proximal suppressors, or global and local suppressors as they are often dubbed. The reviewers are not convinced that the selection criteria applied are objective and generic, namely applicable to any protein. The authors give no justification for the thresholds chosen, and do not show how the results would differ upon changes in these thresholds. The data in Table 1 suggest a very clear cutoff (the distant ones having RankScore 1, the contacting ones having ⩾ 26 scores) but the sample of sequences is so small, and this clearcut separation looks too good to be true.

Also, how do the authors exclude the active site? By checking the structure or blind? If blind the authors need to explain how.

To summarize, the reviewers are concerned that the classification of the residues in distal or proximal positions requires knowledge of the structure, or at least of the surface exposure. This is a limitation that may not make the method useful for structure prediction (or at least less useful). The revised paper must have a clear justification for the steps taken, explained cogently in the Introduction, and also later as necessary.

2) The application of the method to discriminate between different conformations of the DgkA multimers is an interesting one. The authors identify differential contacts between the 2 published conformations and present in Table 2 and Figure 6. However, some of the contacts identified as unique to one structure are really not at all far away in the other structure – even though closer in the example given. For instance, the M66-A99 minimum atom distance is 6.7 Å and 5.5 Å in the crystal structure 3ZE5 (inter monomers as with the NMR structures) and I67-E34 distance is 5.5 Å in the crystal structure 3ZE5 within the monomers (inter monomers in NMR structures) – therefore neither of these contacts is so unique to the NMR structures despite the domain swap, despite the fact they are closer in the crystal. Similarly, though much closer in the crystal, the min atom distance between V62- A41 (between monomers) in one of the NMR structures is 6.3 Å. Therefore, despite the domain swap, many 3D contacts are common to both structures within a looser definition, and therefore it is not clear that one can be sure that the structures are actually discriminated. It would be useful to tabulate the unique contacts with the minimum atom distance in both the structures including the multimeric assemblies.

3) The reviewers feel that global suppressors dominate compensation of highly destabilizing mutations, as applied here (e.g. see PMID: 17122770; PMID: 18495157). So the cases explored here, and especially dgkA, whereby all suppressors were local, may not reflect the difficulty of separating local/global in other proteins (e.g. see PMID: 25455030). Thus, the approach taken here need to be explained and justified with more rigor.

4) Comparison with other methods: The discussion of computational approaches to predict spatially proximal residues seems somewhat biased. It is not clear why EVFOLD, which is now deemed as the most successful method, was not examined. Further, one would like to see a comparison of the structural models offered by EVFOLD and other methods to both the X-ray and NMR structure. Some of these methods will give predictions that unambiguously coincide with the X-ray structure.

The result of the first test, i.e. selection of structures from a fold library may be less convincing than what the authors argue. The field of protein structure prediction went very deep into the use of decoy libraries to test prediction methods in the late 90's and early 2000's. It was later clear that discriminating structures in those conditions was a quite easy exercise and almost any simple method (i.e. surface exposition prediction) was able to perform well in that type of test. In other words, to be convincing these experiments will have to show that the discrimination is substantially better than the one provided by simple prediction methods.

To summarize the reviewers’ concerns, if the authors decide to include comparisons to other methods, then the comparisons should be done on fair basis. Two examples may be sufficient to illustrate the point. The prediction methods based on multiple sequence alignments are not specific for any of the proteins in the alignments and therefore it does not make sense to evaluate them in terms of distances between sidechains (that are specific to each structure), as the authors do. Second, and very important, since the publications of those prediction methods it was very clear that they can be applied only to rich alignments with thousands of sequences. The current application to small alignments does not demonstrate anything but a known principal limitation of the methods ("350 alignments" as reported in the paper).

The authors should decide whether or not to present comparisons to other methods in this paper, and present a judicious discussion of the value of their method.

Other issues to address:

1) While the rationale of detection of proximal suppressors is clear when it comes to protein stability, the effect on function does not follow this rationale. If you disturb a give side-chain-DNA contact, why would a mutation in an adjacent position compensate for that? Unlike the packing-stability that is accounted for (Figure 4), the mechanistic basis of compensation of functional residues remains therefore unclear. Perhaps the authors should not use "function", i.e. ligand binding, to illustrate the method (Figure 1A) but rather, core-packing compensation.

2) Introduction, first sentence – “X-Ray crystallography and NMR…”. Cryo-EM is threatening to shadow both.

3) The Introduction/Discussion overlooks a large body of work that is highly relevant to this one. What the authors dub as systematic suppressor-mutagenesis was done before, often with the aim of unraveling epistatic interactions in proteins in relation to one, or few chosen positions (e.g. PMID: 20975933; 23935519), and sometimes in a systematic manner and in a context that is very similar to the authors (foremost, but not exclusively, PMID: 25455030). We're all prone to cite 'classics' (“Hecht and Sauer, 1985; Machingo et al, 2001; Pakula and Sauer, 1989; Sideraki et al, 2001”) and avoid recent literature that may compromise "novelty" but this does injustice to a lot of very good work, including, eventually, our own. The authors should do a more thorough search and reading, to provide an update picture of experimental explorations of covariance, or epistasis, in individual proteins, and specifically, in support of the claim that: "Though a small number of compensatory mutations were identified, in some cases these were ascertained to be spatially proximal while in others they were distal from the site of the original inactive mutation."

4) "In contrast to proximal suppressors, distal suppressors will typically be on the surface of protein and hence the individual suppressor mutation is expected to show WT like activity." This explanation is very confusing, also because the authors do not use "fitness" terms that would be easier to comprehend. What they mean in effect is that the suppressor mutation is expected to be neutral on its own, and beneficial, or compensatory in combination with the deleterious mutation (PIM in their terminology) – this would be positive sign epistasis in evolutionary terms. The meaning of the next sentence is completely unclear: "Further, unlike proximal suppressors no complementarity relative to the PIM is expected for a distal suppressor."

5) RankScore: 'residue depth' – define please, and also 'mutational tolerance'.

6) Subsection “Application of suppressor methodology to identify the functional conformation of the membrane protein DgkA in-vivo“: V62Q, M66S, M66L, I67V, V68G and W112V were identified as PIMs from screening of SSM – is this from previous work, or this one? If the latter, data need to be provided, and also the criteria for selecting these mutations for the suppressors screen.

7) The Abstract is somewhat misleading as one gets the impression that all possible compensatory pairs in the target proteins were identified. Upon reading further, it becomes clear that half a dozen deleterious mutations were chosen, and suppressors were identified for this small set. This does not make this work less valuable, on the contrary, it demonstrates its power to obtain structural information by exploring a relatively small number of positions. But it would be best to clarify this point.

8) One 'trick' of identifying global suppressors is that they in most cases comprise 'consensus/ancestral' mutations (see PMID: 18495157). The authors may wish to consider this as another parameter in their algorithm.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Residue proximity information and protein model discrimination using saturation-suppressor mutagenesis" for further consideration at eLife. Your revised article has been favorably evaluated by John Kuriyan (Senior editor) and three reviewers. The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

Your manuscript has been read and discussed by three reviewers and the editor, and the decision is the work is, in principle, acceptable for publication in eLife. There are, however, a number of issues with the manuscript, as written, that can be improved by judicious editing. These issues are outlined below, and we ask that they be addressed in a revised manuscript. The revised manuscript will be handled by the editor, without further external review.

1) One of the reviewers is still not convinced that the method you use to distinguish between proximal/distal pairs, and to identify active site residues, is robust. You have provided a manuscript that has been submitted elsewhere that addresses the underlying concepts. Please provide a more complete justification for these points in the present manuscript, so that a non-specialist reader can fully understand the logic behind the method. Cite the submitted manuscript as appropriate. Refer to standard methods of analysis where appropriate, rather than to methods developed in your lab.

2) This reviewer is also not convinced that the superiority of this method is clearly demonstrated by the limited set of decoy calculations done and by the one EV-fold comparison that is provided. On the whole, though, we feel that these comparisons are useful, but you could make it more clear in the manuscript that these are illustrative differences rather than definitive demonstrations of superiority. Please point out limitations of the comparisons.

3) The manuscript is quite difficult for a non-specialist to follow, and in this way it obscures the innovation and depth of the work. It is essential that the manuscript be edited so that it is accessible to a generally knowledgeable structural biologist or biochemist. Some of the points to note are listed below, but it is recommended that the revised manuscript be read by a seasoned non-specialist colleague, and their advice taken, before being resubmitted to eLife.

A) The manuscript is heavy on long run-on paragraphs that introduce multiple ideas, making it difficult for the reader to follow. Break up the flow into separate paragraphs for each idea, concept or result.

B) Ideas are introduced out of order, often with highly specific and cryptic information provided before a more general explanation. For example, CcdB is used without explanation first. Later, concerning CcdB, the incomprehensible statement (to a non-specialist) that "This is <5L" is made. Only later is the biological function explained, and the "<5L" statement is never explained. This is but one of several such instances that make the paper difficult for a general audience.

C) Please avoid the use of inessential abbreviations – we are not under page limits in an online publication. For example, it is highly recommended that "parent inactivating mutation" be spelt out everywhere – the editor sees no reason why this should not be done, and the use of PIM is felt to add to the incomprehensibility of the manuscript. Likewise, why use SSM when it can be spelt out? Why abbreviate yeast surface display with the incomprehensible YSD? The editor asks that you retain only standard abbreviations or gene names.

D) Please ensure that all metrics are clearly explained to the non-specialist reader. For example, in the subsection “Discrimination between proximal and distal suppressors “"RankScore" is used with no explanation.
