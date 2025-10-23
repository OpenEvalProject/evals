# Peer review - Round 1

Editors:
- John Kuriyan, Howard Hughes Medical Institute, University of California, Berkeley , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.03430.031](https://doi.org/10.7554/eLife.03430.031)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Sequence co-evolution gives 3D contacts and structures of protein complexes”““ for consideration at eLife. Your article has been favorably evaluated by John Kuriyan (Senior editor), working with a member of our Board of Reviewing Editors, and 3 reviewers.

The editors and the other reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

This manuscript describes an approach to predict 3D residue-residue contacts at protein interfaces from an analysis of multiple sequence alignments. The described computational approach (using sequence co-evolution to predict contacts between interacting proteins and to generate three-dimensional models of complex structures) appears to be quite successful and is an important contribution that is of interest to a broad audience. The analyses, results, and conclusions are similar to work conducted during the same period by Baker & coworkers, published recently in eLife. Nevertheless, it is the consensus opinion of the reviewers that the present manuscript is potentially suitable for publication in eLife as well, provided that all of the comments raised by the reviewers can be addressed satisfactorily.

We have appended the comments from the three reviewers below. Although many individual points are raised, you will see that the principal concern of the reviewers is that the manuscript falls short of providing the reader with sufficient analysis to judge the validity of the conclusions. It should be possible for you to revise the manuscript to address these concerns without much in the way of new calculations, so we hope that it should be relatively straightforward to deal with these issues.

In addition, since the Baker paper came out recently, it should be given appropriate credit in a revised version. We recommend removing the word “new” from the manuscript for this reason, and instead simply state what was done.

Reviewer 1:

1) The Abstract claims that the authors' approach can discriminate between interacting and non-interacting proteins. However, as far as I can see, the rest of the paper concerns only calculating the interface residues of proteins which are known to interact. No evidence is presented to support the claim to be able to calculate non-interactors. The authors' claim should be corrected accordingly.

2) The authors claim that the co-evolutionary approach has not previously been applied to prediction of protein-protein interfaces. This is incorrect, as the authors seem to be unaware of the previous work of Raphael Guerois' group, which seems rather surprising. The authors should acknowledge the prior work of Faure et al (2012) and Andreani et al. (2013), and they should modify their claim to novelty accordingly. It would also be appropriate to cite properly the prior work of the Baker group (Ovchinnikov et al., 2014) in the same paragraph (the authors currently mention this work only as a “note added during submission”), and the recent review by Andreani and Guerois (2014).

3) In several places the authors say that their approach exploits the fact that interacting proteins are often coded close to each other in a genome. Why is this assumption necessary? According to the description given in Methods, any pair of sequences which are presumed to interact could be concatenated and then used in the authors method. Please clarify.

4) If I understand the authors’ method correctly, they first concatenate the multiple sequences of the presumed interactors, and they then use their previous approach for detecting interacting pairs of columns in the multiple alignment. In this case, when concatenating the alignments for protein “A” with those of protein “B”, the “intra-EC” pairs would appear as A-A and B-B pairs, while the “inter-EC” pairs would come from A-B or B-A interactions. My question is then, are there any observable differences in the inter and intra scores? One might expect that the conservation scores would be lower for inter interactions than intra interactions, as an interface might show more “plasticity” than the core of a domain. It would be very interesting if the authors could comment on this, preferably supported by numerical results.

5) It is incorrect for the authors to refer to their own data set as a “benchmark”. Suggestion: remove all references to the term “benchmark”. However, if the authors make all their data available in a convenient way on-line, it could be proposed as a new “benchmark”.

6) It is wrong to claim that “Experimental evidence... agrees with EVcomplex predictions” (!). Please rewrite this to say that your predictions agree with the experimental evidence. But, if this is your claim, please also support it in some way. What is the experimental evidence? How to you calculate and quantify “agrees with”?

7) Same point in the main text. “The resulting model is consistent with the topologies from cross-linking”. How do you quantify consistent? RMSD from the earlier models? Please provide supporting details.

Reviewer 2:

My main comments concern the way the data in the current manuscript are analyzed and presented. While the main Figures / Table 1 currently illustrate useful examples, they should also show overall analyses of the results over all cases in the benchmark datasets. In several cases this is essential to support the stated conclusions. It does not seem that this would require a substantial amount of new work or lengthy simulations, as most of the relevant data are in the Supplementary Materials (most data are in raw table format or with a separate Figure for each example, which makes it hard for the reader to gauge overall performance – this could be presented in a more easily digestible format in the main text). Specifically, I feel the paper could be substantially improved if the following points were addressed:

1) Please support the statement “Benchmark calculations here ... indicate that the number of sequences in the alignment is critical...” with a Figure showing overall performance versus # of sequences (Figure 3 shows dependency of accuracy on relative rank for only two examples).

2) Show a main Figure comparing predicted contacts against residue distances in the 30 known crystal structures of complexes that had a sufficient number of sequences (Figure 2 only shows contact plots for two examples, and structural pictures for several more, but no overall quantification). This type of analysis could also help to support the statement “For the top ranked benchmark complexes, the majority of the top 5 ECs is correct to within 8A...” with a more quantitative analysis (Table 1 only shows 7 of the 30 complexes in the dataset; Supplementary file 3 shows all individual contact maps, but no overall quantification).

3) “... these benchmarks show ... and demonstrate the criteria needed for successful prediction of unknown interactions”. To support this statement, it would be useful to have a main Figure / Table for each important criterion, analyzed over an entire benchmark set (as for the number of sequences in point 1).

4) Please add metrics to support statements that ECs are “completely consistent” with crosslinking data, or that a coupling “coincides with experimental evidence”. The comparison Table in Supplementary Figure 6 could be presented in more quantitative terms in the main text (for example, what does “crosslinking neighborhood” mean?).

5) What are the possible reasons for false-positive co-variation that does not correspond to contact?

6) The manuscript deals entirely with pairwise co-evolution, and seems to neglect the possibility of higher-order complexity in the sequence pattern.

Reviewer 3:

The manuscript presents an upbeat and optimistic view of the success of the method, with a relatively small amount of critical discussion and little if any investigation of what one can learn from cases in which it does not perform as expected. (For example, a list of possible reasons for false-positive co-variation that does not correspond to contact is given, but an analysis of actual instances is not.) Likewise, a set of methods is presented that is relatively particular, and the reason why these specific methods were chosen over other possibilities is not provided. Moreover, the manuscript deals entirely with pairwise co-evolution, and seems to neglect the possibility of higher-order complexity in the sequence pattern. The manuscript could be substantially strengthened by adding analyses and insights in these issues.
