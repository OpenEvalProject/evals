# Peer review - Round 1

Editors:
- Shozeb Haider, https://ror.org/02jx3x895 University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81850.sa0](https://doi.org/10.7554/eLife.81850.sa0)

The manuscript reports on a useful tool to study protein allosteric regulation function. The work is based on inadequate experimental validation of the predicted residues implicated in mediating allosteric signaling. The study highlights the significance of the weak pairwise term for the prediction of the allosteric function.


---

# Peer review - Round 1

Editors:
- Shozeb Haider, https://ror.org/02jx3x895 University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81850.sa1](https://doi.org/10.7554/eLife.81850.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Coevolution-based prediction of key allosteric residues for protein function regulation" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Volker Dötsch as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Sarath Dantu (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

There seems to be a consensus between the reviewers that:

1) There is a lack of comparison of the proposed method against existing ones that do pretty much the same. This is the main weakness of the manuscript.

2) The authors should also provide a better metric of the true positives of their method – and of course report the false positives they have for the cases they've tested. AlloSite seems to predict several residues as key, some of which happen to be oncogenic (Table 1). It's not clear how many of the top 10, let's say, residues that it predicts have an allosteric effect.

3) In addition to the comparison, the authors need to establish that the signal coming from comparison of allosteric vs. orthosteric is different from comparing any two random patches with same number of residue pairs.

4) A complete picture of the predictive power with both strengths and weakness of the tool should be presented.

Reviewer #1 (Public Review):

Allostery refers to processes whereby a change at one site of a biological macromolecule affects the structure and dynamics at another distinct functional site, enabling the regulation of the corresponding function. Xie et al. developed an in-silico method to predict residues involved in allosteric regulation using a coevolution-based method. A fast and accurate method of identifying key residues responsible for allosteric signalling is important for drug design purposes and protein engineering.

Strengths:

1) The authors applied their method to multiple targets from different protein families to test their method.

2) The method is able to predict in a retrospective analysis certain residues involved in allosteric communication between orthosteric and allosteric binding sites.

Weaknesses:

1) There are several tools used in statistical genomics to predict allosteric communication pathways. Even though the paper tries to demonstrate the ability to predict residues that are involved in allosteric communication, KeyAllosite is not compared with any other state-of-the-art tool that does the same (1-3), which would highlight the strengths of this method with respect to existing ones.

2) The authors mention that the number of effective homologue sequences affects the probability of finding an allosteric site in the top 3 scored sites, however, Cdc4 and AR2 have also a low number of effective homologue sequences (Figure 1.A) yet a high Z-score. No sufficient explanation is given regarding this discrepancy. This also demonstrates that a threshold in the Neff under which KeyAlloSite becomes unreliable should be defined.

3) From the low Z-score of CYP3A4, the authors claim that the conservation of residues in the orthosteric site is important for getting an accurate prediction of the coupling strength. It is not clear though if and how is this aspect encoded in the KeyAlloSite. From the description of the method, it seems like the algorithm does not check for the level of conservation of the orthosteric residues. An explanation as to why has it not been incorporated into the algorithm is necessary. The conservation at a given site in an MSA defined as the overall deviance of amino acid frequencies at that site from their mean values, in combination with the statistical coupling of two sites has been shown to be important in the development of allosteric models (4).

4) In the case of AuroraA, the authors do not explain why other Ser/Thr/Tyr residues scored higher than T287 and T288, or if their higher scores are an artefact. However, in many cases, post-translational modifications take place by secondary partners and, therefore, the coupling of a post-translational modification site with the orthosteric site cannot be used to predict such sites. Post-translational modification sites are expected to have a strong coupling with residues of the upstream/downstream effector that is responsible for the modification, rather than with residues of the orthosteric site of the protein.

5) The authors defined allo-residues as the residues whose Z-score is >0.8, but there is no strong argument regarding the choice of this threshold. In the case of the allosteric pockets, for example, the authors use a threshold of 0 to identify pockets with strong coupling strength.

6) In the case of the Tar, it would be good if the authors reported the results starting from an apo structure as well and see if the method is able to find Y149 and Q152. That way, they could test how sensitive/biased the method is to the chosen conformation. If no apo structure is available, maybe another protein where both an apo and a holo structure exist could be used for this purpose.

7) The data in Table 1 is not sufficiently convincing. It would be helpful to also report how many of the identified residues by KeyAlloSite are indeed involved in oncogenic mutations or find another metric to quantify the success rate of KeyAlloSite.

8) The success rate of the method to predict key residues of the function of CALB (38% success rate based on the reported residues in the literature) and CMS (20%), should be interpreted with caution. It may be the case that the rest of the predicted residues have not been tested for their functional role, or that the method has indeed a low success rate in predicting key residues for allosteric communication.

In lines 38-41, the authors refer to SARs of allosteric drugs as "flat", which is not clear what they refer to.

It is not clear if the so-called, "allo-residues", that the authors define in lines 49-52 refer to residues that affect the binding or the signalling.

It would be helpful for the reader if the authors included a section where they describe the method itself and the key steps of developing their model before presenting the results. That way, the reader could follow the results easier.

The authors classified L359 of BCR-ABL1 as an allo-residue and justified the importance of this residue based on the fact that a weaker ligand does interact with this residue. For transparency, it would be good for the authors to report the allosteric scores of all 44 residues in the allosteric site to show that this residue was not cherry-picked and that the method can pick up all the residues that are important for the binding.

The manuscript has several typos and language mistakes (e.g. "screening" instead of "screen" in the Abstract, missing articles, etc.) that should be corrected prior to a resubmission.

Reviewer #2 (Public Review):

The authors designed a statistical approach to analyse coevolution scores from a protein and predict allosteric residues. This approach relies on comparison of residues from the two sites (allosteric vs. orthosteric) and omits the rest of the protein.

While the approach is logical, the predictive power has not been clearly established. To demonstrate the effectiveness of the approach a confusion matrix should be provided as it will show the predictive power of the method in the different scenarios presented in the manuscript (PTM's, enzymes, pathogenic mutations, etc.).

An effective method, along these lines, will have significant impact on protein and drug design.

It would be helpful if statistics on the distribution of significant scores from E row comparison after the t-test are provided. Further, you have so far compared allosteric with orthosteric, it would be interesting to compare the same distribution/statistics with allosteric vs. non-orthosteric residues. It may serve as a very good benchmark. The idea would be to see if the events of significance from allosteric vs. orthosteric are different/unique if we pick and compare any two random patches in the protein.

A boxplot of Zscores for All, top200, top300, top400 pairs from Figure 1—figure supplement 2 would be very informative.

As you have been using top zscore residues (>0.5 or >0.9 for enzymes), direct or indirect evidence for the statement in lines 306-307 is not very apparent from the provided data. This has to be flushed out further.

Please annotate residues for which experimental data is available to compare with keyallosite predictions for example in Supplementary files 4 and 5. In the main text (line 284) you only mention one residue out of 52 to demonstrate the effectiveness of the prediction. Again a confusion matrix would help here.

Can you please clarify if in Figure 2, number of residues refers to the number of residues from allosteric+orthosteric site?

Figure 6 may be ideal as Figure 1 to inform the readers about the protocol of this work.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Coevolution-based prediction of key allosteric residues for protein function regulation" for further consideration by eLife. Your revised article has been evaluated by Volker Dötsch (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

1. Can you please provide a detailed description and expand the discussion on the predicted amino acids and why the predicted residues are not the top ranking ones?

2. The theoretical formulation to extract the coupling score and a compare/contrast to Hopf et al. approach would be highly beneficial to the readers.

Reviewer #1 (Recommendations for the authors):

The authors did extensive work trying to address the revision comments, and their effort is much appreciated.

Nevertheless, in the absence of further experimental validation of the importance of the predicted so-called key "allo-residues" in mediating the signal between the orthosteric and allosteric binding site, it is still hard to assess the predictive power of the presented method. There are still residues for example that score higher than known functional residues (see for example residues T235, S245 and S249 in the case of Aurora A) whose implication in signal transduction is not confirmed, or residues whose importance depends on the conformation chosen for analysis despite the coevolutionary conservation metric used to score the residues (Q152 of Tar whose score is way below the 0.8 threshold when an apo structure is considered, which shouldn't be the case given that AlloSite uses only MSA and coevolutionary information for the scoring – it seems like other residues are predicted to be way more important based on the allosteric pocket definition given by CAVITY to decrease the score of Q152 to <0.8 after normalisation).

I fully understand that such experimental validation goes beyond the capacities of a computational group, however, as a reader, I might be hesitant to try this method.

Reviewer #2 (Recommendations for the authors):

The authors have carefully addressed all the comments from the previous review.

Few additional comments for authors to consider:

The Discussion section can be enriched further. At present it only discusses two points, i.e., ability of the method to predict key allosteric residues and requirement of sequence depth. For example: the last two paragraphs 565-580 are repetitive as they both highlight the need for depth in sequence alignments which is a known issue for MSA dependent methods, as again discussed by Hopf et al. Nature Biotechnology volume 35, pages 128-135 (2017). Further, the theoretical formulation to extract the coupling score is identical to Hopf et al. and a compare/contrast of the two approaches would be highly beneficial to the audience. Even Hopf et al. highlight the significance of the pairwise term, as done in this article.
