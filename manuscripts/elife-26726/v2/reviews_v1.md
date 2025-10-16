# Peer review - Round 1

Editors:
- Alfonso Valencia, Barcelona Supercomputing Center (BSC) Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.26726.016](https://doi.org/10.7554/eLife.26726.016)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Systematic integration of biomedical knowledge prioritizes drugs for repurposing" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aviv Regev as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Jason Moore (Reviewer #1); Amitabh Sharma (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

This paper describes a very large resource of information on potential drug target interaction and its use for the prediction of drug repositioning opportunities The large network ensembles 47k nodes (11 kinds) and 2.25M edges (24 kinds) from 29 public databases. The network provides new relations that could lead to interesting discoveries. The algorithmic proposal is simple and reasonable, the testing makes sense and it is based on independent data sets. The examples provided are interesting as illustration of the best results, i.e., insights into epilepsy and nicotine dependence treatment.

There are a few points that require careful attention:

Justifications for the cutoffs used to define edges. Edges have a different level of reliability ranging very differently depending on the considered domain (ex. gene expression level). It is not clear how this has been taken into account/normalised. How edge reliability has been made comparable across resources and data types? Additionally, the authors have used different discretization threshold for different information domains. It is not clear how these thresholds have been determined and how/if they could potentially impact the predictive ability of the presented approach. This should be explained and each choice on this regard numerically justified.

The test sets used to validate the predictive ability of the Rephetio approach look strongly unbalanced toward negative cases (in 3 cases out of 4 the number of negatives is 3 orders of magnitude larger than the positives). It is necessary to assess the impact performance evaluation comparing with balanced sets of negatives and positives.

Other comments below are related with areas that require better explanations, clarification and editing:

- It was a bit confusing to map the nodes mentioned in the Introduction and Results to the Materials and methods. For example, anatomy is not mentioned in the nodes section of the Materials and methods. Making this more consistent might help the reader.

- It might be useful to expand some of your text on graph databases since they are very new and not many people know what they are or why they are useful.

- Edges of Hetionet are directed/undirected or a mixture of both. This inherently affects the definition of a path.

- The analysis of pathways of at most length 4 should be justified. What is the average length of a path between any node-pairs? And how loops are managed in this regard?

- The selection of the cases (e.g. methapaths Figure 3) should make clear how many good cases are there by for example providing a table with the best performing ones.

- The labels in Figure 2 are annoyingly all abbreviated. To improve readability I would suggest explicitly indicating the meta edge type.

- Even if referencing their relevant previous publication the "degree-weighted path count" should be briefly explained. Particularly, how this algorithm penalizes the paths involving high degree nodes?

- The multiple sclerosis example mentioned in the third paragraph of the subsection “Hetionet v1.0”: are the results shown anywhere? I believe the 4 nodes mentioned gene, disease, BP and anatomy? What exactly are the 5 types of interactions (guess: GpBP, DaG, DdG, DuG, AuG)? I understand that the authors have to contend with only a few examples to demonstrate the functionalities of their tools but still, it would help the reader to visualize this example if these details were presented.

- Related to the above: It would help the reader to show the four lines of Cypher code in the MS example to demonstrate the ease of use claimed by the authors. Or alternatively, to refer the reader to the part of the website where the syntax is introduced. Without this, the sentence "Furthermore, the portion of the query to identify paths meeting the above specification required only four lines of Cypher code" is left up in the air a little bit.

- In the second paragraph of the subsection “Systematic mechanisms of efficacy”, could the authors elaborate on the DWPC delta AUROC? The concept has been introduced in a previous publication, but it would be helpful to recap the definition so as to induce more biological insight in the reader.

- In Figure 2A, it took me a while to figure out that the dot sizes are not continuous but instead there are only two dot sizes with small dots corresponding to non-significant (FDR>0.05) and larger dots corresponding to significant (FDR<0.05) metapaths. It would help to put a small legend clarifying this.

- The selected metapaths in Table 3. We see that good (all of the 11 positive covariates of the following section) as well as poor predictors are both shown. According to what criteria were they selected? Is it just a random selection intended to show the range of parameters and what they signify? If so, this should be noted.

- "29,044 non-treatments": If non-treatments are any disease-compound pairs that are not the 755 known treatments, then the number should be much higher. It would be helpful if the authors refer the reader to the Materials and methods section "Prior probability of treatment" here.

- The permutation test has to be more clearly explained and potentially combined or compared with some previously published approaches (BiRewire for example.

- The baseline performances of their network the authors assembled 5 randomized versions of it. This number seems to be very small and this section requires clarification.

- Did the Thinklab contributors – pre-reviewing the paper – consent to having their names appear in a publication?

- The analysis described in the first Results section (Systematic mechanisms of efficacy) leads to the authors' conclusion that the frequency of the information types in the metapaths for selected existing drug-disease pairs is higher for those traditionally considered by pharmacology and it is particularly low for metaedges involving gene expression and transcriptional data. In the eye of the authors this should tune down the recent excitement surrounding this type of data. This argument looks a bit circular. The authors have used a set of established drug-disease possibly involving many approved drugs. Drug discovery pipelines have been typically guided so far by knowledge of disease mechanisms, chemical structures of drug candidates and targets. Should not be obvious that for approved drugs what lead to their development is reflected by the enriched meta edges found by the authors?

- Additionally, most of the recent excitement around the use of transcriptional data for drug repurposing comes from the development of signature matching tools exploiting drug-drug similarities and drug-disease anti-similarity at the level of transcriptional signatures (respectively elicited by the drugs under consideration upon treatment of in vitro models, and from contrasting diseased vs. normal state). Would this be worthy the inclusion of other two type of edges (transcriptional signature similarity/anti-similarity at the whole signature level)? This possibility should be at least discussed.

Finally, Heterogeneous network presented in this study unambiguously refers to "aggregated" networks consisting of the sum of multiple types of nodes and edges. While heterogeneous networks present perhaps the most viable way of integrating multiple and diverse types of biomedical data and are therefore very valuable to gaining integrated biological insights through machine learning approaches, it is important to distinguish them from multilayer networks, whose theory and mathematical framework has been established in the reviews mentioned. The current diversity of nomenclature in the filed stems from the fact that, at least for now, these slightly different types of multilayer networks have to distinguished for their mathematical treatment. On the other hand, no such mathematical framework exists for generic heterogeneous networks such as HetNet, but rather, an exhaustive survey of node/edge combinations (metapaths) is needed, such as the one presented in this paper. The authors should note the fundamental difference between multilayer and aggregated network approaches when making this comparison.
