# Peer review - Round 1

Editors:
- Nir Ben-Tal, Tel Aviv University , Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.18715.073](https://doi.org/10.7554/eLife.18715.073)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "A computational interactome and functional annotation for the human proteome" for consideration by eLife. Your article has been favorably evaluated by Naama Barkai as the Senior Editor and three reviewers, one of whom, Nir Ben-Tal (Reviewer #1), is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The Honig lab has been developing the PrePPI methodology and web-server/database for predicting protein-protein interactions at genome-wide scale. PrePPI infers interactions based on known protein-protein complexes, as well as direct and indirect experimental techniques, such as phylogenetic profiles, gene ontology, expression profiles, etc. Here they present a revised PrePPI which is shown to be much superior to the previous version in terms of coverage and accuracy. Improvement is based on data accumulation, which is trivial (but very important!), but also on the addition of novel characteristics of protein-protein interactions, such as information from orthologues, expression profiles, partner redundancy and protein/peptide interactions. PrePPI now covers more than 1.35M interactions in the human proteome, 4 times more than the original version. The paper additionally reports the use of this information for function annotation, gene set enrichment analysis (GSEA), and an analysis of SNPs at interfaces. This is a substantial piece of research that merits publication in eLife if the following points can be addressed.

Essential revisions:

A) The algorithm

1) Features used for scoring the interaction likelihood: How is "5- Orthology" different from "2- Phylogenetic-Profile"?

2) Features used for scoring the interaction likelihood: How is Expression Profile used differently in the new vs. old PrePPI?

3) How specific are the predicted interactions? Considering known interaction pairs of orthologs from two protein families A and B, can PrePPI correctly pair A1 to B1, A2 to B2 and so on?

4) Is it the case that the vast majority of predicted interactions are among paralogous proteins, where missing interactions are inferred based on concrete data for a pair of interacting proteins? It would be helpful to report the fraction of these.

B) Evaluation of coverage and accuracy

5) Training on yeast and testing with human: What is the cross-sets similarity between the proteins in both sets in terms of sequence and structure? Because some of the descriptors are based also on orthologues, how similar are the proteins in the sets in terms of their representations?

6) The authors include in the definition of PPI proteins that are functionally related. This is a very generous interpretation of a PPI which is helpful for function annotation and GSEA. The Abstract should clearly state the definition of PPI and note that there are about 50,000 reliable predictions based on structural evidence alone which is indicative of a direct interaction (see subsection “Prediction Performance”, last paragraph).

7) To get an estimate of the expected accuracy, it could be insightful to compare the new and old PrePPI. The manuscript gives an overall comparison in terms of counts of interactions etc., but comparison of individual interactions would complete the picture. For example, is the difference between the old and new PrePPI only in better coverage? What fraction of the interactions that have been assigned high confidence in the old prePPI are dismissed in the new prePPI? For these (if found), what are the reasons? Changes in the available structural or non-structural data? Or is it the result of smarter data processing?

8) When querying the web site with human trypsin type 1 (P07477), one of the interactors was P35030 (human trypsin type 3). Strangely the structural model for the interaction showed the two trypsin structures were superposed. What does this mean? It clearly is not biologically sensible. This raised the question of whether the website and the entire approach have been stress tested by detailed analysis of specific examples rather than global metrics (ROC curves etc.). The authors should generate a random list of a few Uniprot IDs and input them to the server and then carefully check the answers. This requires work by a researcher with extensive biological expertise – so odd predictions can be identified. The paper could report the set of tested Uniprot IDs.

9) Related to (8) above, please also address the realism of the predicted physical interactions. The original paper acknowledged that the structural models are not refined and are often non-physical. Indeed, often the interacting partners in PrePPI models suffer from major steric clashes. On the other hand, some models are based on non-interacting chains, although they might have high prediction scores.

C) Comparison to other algorithms

10) PrePPI should be compared to other methods. For clear comparison it is essential to clarify the cross-validation since the PrePPI LR-score combines experimental and computational evidence. It is not clear from the paper if experimental data used for training were excluded in testing (Figure 1). This is especially important since PPI databases overlap with each other. How different would the Precision-Recall curves be if only crystal structures with other experimental evidence were used for prediction? In other words, what is the contribution of structural models to the quality of predictions?

11) When compared with the human data from Y2H from Rolland et al., Figure 1C – the authors say that PrePPI compares favorably with Y2H. Please verify and demonstrate this result. Precision-recall curves in addition to ROC are needed in the main text since the sizes of TP and FP datasets are not balanced. What is the size of "N" dataset – millions or hundreds of millions of interactions?

12) The point in (5) is also relevant for the comparison of the third (smaller) set from Vidal to the two other sets.

13) Given the broad definition of a PPI (see 6 above), when PrePPI is compared to the coverage of other databases it would be important to state that these other databases might be using a far more restricted definition of a PPI.

14) The paper describes (subsection “Shared GO annotation”) the number of predictions obtained after removing the GO terms. If it is tractable, it would be interesting to have a table showing the effect of removing each of the terms in turn.

D) Update

15) At present, PrePPI is presumably up-to-date in terms of usage of all experimental data (structure-based or otherwise), and its enhanced performance in comparison to other resources is, in part, related to that. It would be great if PrePPI will be kept up-to-date automatically. It should be possible with the appropriate scripts. Anyway, please indicate in the main text how frequently you plan to update PrePPI.

E) Data availability

16) The web site works for a single sequence input. It is not clear how much global data is available to the community. Can one download a list of all predicted PPIs with the scores? Can one obtain predicted protein-protein structures? This needs to be stated in the paper. According to eLife policy all the data should be made easily accessible to the public. Please take care of that.
