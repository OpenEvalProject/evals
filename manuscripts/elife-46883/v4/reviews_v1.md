# Peer review - Round 1

Editors:
- Michael B Eisen, HHMI, University of California, Berkeley United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.46883.sa1](https://doi.org/10.7554/eLife.46883.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Proteome-wide signatures of function in highly diverged intrinsically disordered regions" for consideration by eLife. Your article has been reviewed by Michael Eisen as the Senior Editor and Reviewing Editor, and two reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Xavier Darzacq (Reviewer #1) and Jessica Siltberg-Liberles (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. Please aim to submit the revised version within two months.

Summary:

While related protein intrinsically disordered regions (IDRs) usually have little sequence similarity, a growing body of work suggests that general molecular features of these sequences – such as charge or proportions of specific amino acid residues – are conserved. In this manuscript, Zarin et al.et al., find evidence for such conservation by extending a methodology previously applied to an IDR from the S. cerevisiae protein Ste50p to a broader collection of IDRs from the S. cerevisiae proteome. The reviewers consider the manuscript to be a well-executed and timely stud y of interest to a wide range of eLife readers, and suggest only a series of relatively minor revisions.

Essential revisions:

The only major point raised by the reviewers is that the manuscript would be improved with a more in depth description of the methods, which are referred to currently primarily by citation.

For example, it is unclear whether the same power law distribution for gap lengths is used as in past work by Nguyen Ba et al.et al., and how the disordered region substitution matrices are inferred. Additionally, a brief summary of the phylo-HMM(s) (both sequence and gap) used to infer sequence conservation in individual IDRs would be useful given how central this is to the results in the manuscript. Such a discussion could be accomplished simply by extending the existing subsection "Evolutionary analysis of diverged disordered regions".

Minor points:

1) In Figure 6C and Figure 6—figure supplement 2, no fluorescence is visible for Cox15 IDR∆0 and Cox15∆Emp47. This makes it hard to judge whether these constructs fail to localize to mitochondria, as claimed in the manuscript. Are these constructs poorly expressed, or is high thresholding in the fluorescence channel responsible?

2) In Figure 2, three substitutions in the Ste50p IDR are made to demonstrate that similarity in the set of molecular features under selection ("evolutionary signature") implies the ability to perform similar functions. We recommend that the authors indicate how many consensus MAPK phosphorylation sites are present in each of these substituted domains, as this is a core function of the Ste50p IDR.

3) In Figure 2, IDRs are ordered by the Euclidean distance of their vectors of molecular feature Z-scores. This is would be appropriate for linearly independent, orthogonal vector components. Because many of the molecular features are linearly dependent (for instance, (fraction of basic residues) + (fraction of acidic residues) = (fraction of charged residues)), their Z-scores might be suspected to lack independence as well. No evidence to the contrary is provided in the manuscript. Codependence of molecular features could also bias the clustering algorithm so that it is more dependent on features that have a high redundancy (e.g. any of the charge attributes). Zarin et al., use clustering in a qualitative way, so we think this is a minor concern and should not impact the main claims of the paper. However, since this method is likely to be implemented by others, we recommend including a note of caution about using Euclidean distance to interpret differences in evolutionary signatures, especially since Figure 2 implies that this is valid.

4) The authors assert that their IDR cluster-function assignments can be used for functional annotation of 10 previously uncharacterized disordered proteins (Table 2). While this would be useful, the authors provide little validation for these predictions apart from some indirect evidence for one of the proteins (Rnq1p). To make this point more persuasive and to demonstrate the accuracy of the cluster-function assignments, the authors could include predictions for the function of 10 fully disordered proteins of known function, in addition to the existing set of proteins of unknown function.

5) The authors refer to the molecular features as "evolutionary signatures" but wouldn't "functional signatures" be a better term? The title also hints at this…

6) The authors often use the term homology when they mean sequence similarity. They are not equivalent. For example, from subsection “Clustering of proteome-wide evolutionary signatures”:

"For example, the cluster with the highest amount of "homologous" IDRs according to this threshold (top 1% homology) is cluster Q, with 8.9% homologous IDRs. However, the vast majority of the clusters have negligibly homologous IDRs; for example, 17/23 clusters have less than 1% homology between IDRs."

It would be better to write:

"For example, the cluster with the most similar IDRs according to this threshold (top 1% similarity) is cluster Q, with 8.9% sequence identity across the IDRs. However, the vast majority of the clusters have less similar IDRs; for example, 17/23 clusters have less than 1% sequence identity between IDRs."

7) Following up on the entire paragraph from subsection “Clustering of proteome-wide evolutionary signatures” mentioned above, how are the sequences from different IDRs in the clusters compared. It says with Blosum62, but how are they aligned? Gap penalties? What information do pairwise distances between sequences that are this divergent provide?

8) Disorder is predicted using DISOPRED3 on the S.cerevisiae proteome, but if disorder is only predicted for one species, how do you know that disorder is conserved for sequences in each alignment? Disorder is not necessarily conserved across sequences, not even across orthologs, see Montanari et al., 2011 and for further discussion see Ahrens et al.2017.

9) It is stated on numerous occasions that disordered regions are rapidly evolving and they most frequently do, but not always. Some disordered regions that also are predicted to have secondary structure to evolve slow, see Ahrens et al., 2018 and Ahrens et al., 2016.

10) Another recent paper that discusses functional constraint in disordered regions and due to its relevance, it ought to be referred to from the current manuscript, see Afanasyeva et al., 2018.

11) Figure 1—supplementary figure 2 shows nothing. It is supposed to show very little, but really, this shows nothing. If this is correct, can you add what the data looks like for ordered regions as a comparison?
