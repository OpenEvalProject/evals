# Peer review - Round 1

Editors:
- Lucy Forrest, NINDS United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.29880.029](https://doi.org/10.7554/eLife.29880.029)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Inferring joint sequence-structural determinants of protein functional specificity" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Richard Aldrich as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: David T Jones (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors present an approach to identify functionally specific residues that distinguish functional subgroups in a protein evolutionary superfamily. The method is based on identifying clusters of residues through sequence analysis (Bayesian Partitioning With Pattern Selection, BPPS) that are distinctive of individual subfamilies of a larger family/superfamily. This is followed by a second step identifying clusters of residues using an approach based on protein structure (Structurally Interacting Pattern Residues' Inferred Significance, SIPRIS) and calculating a statistical significance for the overlap of the structure-based cluster with the sequence-based cluster. This combination is a potentially very robust, insightful, and valuable approach, with widespread applications in uncovering the mechanisms of allostery.

Essential revisions:

The reviewers were enthusiastic about the potential impact of the method, as well as the writing and presentation of the manuscript, and agreed that benchmarking of allosteric residues is limited by the available experimental literature, justifying the use of specific examples. However, other aspects of the approach require more quantification and benchmarking. Specifically, confidence in the method would be greatly improved by the inclusion of:

1) A benchmark of the ability of the BPPS/SIPRIS strategy to identify functional binding site residues, such as specificity-determining residues that distinguish protein subgroups binding different ligands. These predictions should be easy to assess by using known substrate binding sites in e.g. the IBIS resource.

2) Benchmarking of the partitioning into sub-families given by the BPPS method. The authors could compare the subgrouping achieved by the MCMC method of BPPS with groupings identified by experimental characterisation of relatives, e.g. in the SFLD resource that provides curated hierarchical groupings for superfamily sequence relatives. See for example the benchmarking of subfamily grouping in Brown, D.P., Krishnamurthy, N. and Sjölander, K., 2007. Automated protein subfamily identification and classification. PLoS computational biology, 3(8), p.e160.

3) An analysis or discussion of the dependence of the BPPS method on the quality of the input multiple sequence alignment (MSA). Although a sequence search is used to expand the datasets, presumably it is necessary to have key representatives in the starting cluster. This suggests that some knowledge of the subgroups is necessary before starting the BPPS analysis. How dependent is the method on having informative sets of sequences for each subgroup in the starting cluster? What is the range of RMSD between relatives in the MSA used to analyse the example superfamilies? How applicable will this method be to structurally very divergent superfamilies?

4) Per journal policy, the BPPS and SIPRIS software must be made maximally available. The code must conform to the Open Source Definition (https://opensource.org/docs/osd), and should be deposited in an appropriate public repository. To ensure that software can be reproduced without restrictions and that authors are properly acknowledged for their work, authors should license their code using an open source license. Authors are encouraged to use version control services such as GitHub, GitLab, and SourceForge. eLife maintains a GitHub account to archive code accompanying eLife publications that has been deposited on GitHub or another version control service.
