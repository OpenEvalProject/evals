# Peer review - Round 1

Editors:
- Gerhard Hummer, The Max Planck Institute of Biophysics , Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.08697.023](https://doi.org/10.7554/eLife.08697.023)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for submitting your work entitled “Regulation of multispanning membrane protein topology via post-translational annealing” for peer review at eLife. Your submission has been favorably evaluated by Randy Schekman (Senior Editor) and three reviewers, one of whom, Gerhard Hummer, is a member of our Board of Reviewing Editors.

he reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Co-translational and post-translational steps in Sec-facilitated insertion of the EmrE integral membrane protein are studied using a coarse-grained simulation model. Consistent with experiment, the simulations produce a mixture of orientations of the protein in the membrane that is sensitive to mutations in the loops connecting the transmembrane helices. Transient topologies are found to anneal by flipping loops across the membrane during post-translational annealing. The resulting orientation distribution thus depends strongly on the electrostatic character of these loops. This work sheds light on the mechanism of membrane protein insertion, its kinetics, and the factors determining the orientation and its variability.

All three referees are overall positive but raise a number of concerns regarding the details of the model, the interpretation of the simulation results, and the presentation in the paper. I find the issues raised by the referees to be relevant. Addressing them in a revision should result in a stronger paper. Following is a brief summary of their reports that emphasizes the main points as seen from my perspective:

Reviewer #1 is concerned that the outcome of the simulations was sensitive to the somewhat arbitrary simulation termination criterion. Other concerns center on the modeling of the peptides, including the assignment of CG sequences, loop length, and the neglect of negative charge (however, the latter may not be particularly relevant for the EmrE sequence).

Reviewer #2 points out a number of relevant connections to the literature, and asks for clarifications/rectifications in the presentation of the model and the simulation results.

Reviewer #3 is concerned that the reported agreement with experiment, while visually strong, may not be quite as convincing in a more quantitative statistical analysis. The reviewer is also concerned about the factors determining the rates of loop flipping in the model and in real systems. The role of degradation (which could affect slowly relaxing EOT structures) should also be discussed in more detail.

In the following, I highlight the points in the reports I consider most relevant.

1) The terms topology, single-topology, and dual-topology should be explained to the general reader. The exact meaning of these technical terms is not immediately obvious and has caused some confusion even among the experts (cf. dual vs. antiparallel topology).

2) The simulations are terminated when a dissociated Ncyto/Ccyto or Nperi/Cperi state with 4 inserted TMDs is reached. The authors should briefly discuss (a) if the results are sensitive to variations in the termination criterion (e.g. by continuing the simulations for an additional set time, by asking for a larger distance from the origin, by running the simulations for a fixed time after initial release etc.) and (b) if there is a justification for this criterion (e.g. that subsequent changes to the topology occur on much longer time scales). It would also be useful to indicate the length of the longest simulation at which 0% of misintegrated proteins is observed.

3) Proteins with mixed orientations in the membrane appear to be the exception. The authors should thus briefly discuss whether by applying the same coarse-graining recipe to other proteins, and using the same simulation protocol, one indeed finds well defined orientations.

4) TMD1 was treated differently from the other 3 TMDs. What happens if one uses the same bead type for all TMDs? (The text states that L-type beads were used, but Supplementary file 1C lists them as V-type beads. The legend of the table also has the assignment of moderate and strong hydrophobicity of L and V beads switched vis-à-vis the text).

5) A discussion of the present results in light of earlier studies should prove insightful. In particular, Cymer et al. in a recent review (J Mol. Biol., 427:999-1022, 2015) raised questions about the simplistic model of release of TM helices in the correct topology. They noted that (a) the assembly process is driven by thermodynamics and (b) at an elongation rate of about 50 ms per amino acid, there is ample time for a chain to sample what could be a very complicated energy landscape. Here the authors indeed find that the insertion pathway and topology of a given EmrE mutant are not immutable. This connection should be discussed.

6) The pathways of insertion should be discussed in more detail. Figure 1 shows the 2D model used by Miller et al. The nascent chain can exit from the translocon either by a gap between translocon and membrane or through the translocon. Although the upper panel of Figure 1B suggests passage through the translocon, the lower panel shows the nascent chain passing from ribosome directly into the membrane. The paper does not address which of these two pathways is preferred. I think the authors should comment on this and, if possible, provide more information on the pathways observed in the simulations. This is important, because Cymer et al. (2015) suggested that the preferred path of the nascent chain might be along the translocon lateral gate rather than through the translocon as suggested by the current cartoons. The lower panel of Figure 1B suggests that the lateral gate pathway may be the preferred path.

7) A more thorough statistical analysis of the data would strengthen the paper. P-values, rank correlations, or other measures of correlation could be calculated for the data presented in Figure 2 so that the reader can understand the correlation and statistical significance of the simulation results compared to the experimental results.

8) What is the role of neighboring protein elements on the flipping frequency of a given loop? How do these correlated motions affect the flipping frequencies presented in Figure 6?

9) A more detailed discussion of the possible role of degradation would be important. Based on experimentally determined timescales of degradation (a brief comment is presented in the last paragraph of the Discussion), and the time scales of insertion and annealing observed here, can one estimate the degraded fraction and the effect on the orientation distribution?

Along the same lines, in the third paragraph of the subsection “Position of slowest-flipping loop in EOT ensemble determines fully integrated topology”, it is not immediately clear how “the fraction of CG trajectories that have reached fully integrated multispanning configurations” (Figure 7B) is related to degradation of sequences as a function of time prior to reaching a fully integrated multispanning topology. This paragraph needs to be edited for greater clarity to reveal the authors' assumptions more clearly.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled “Regulation of multispanning membrane protein topology via post-translational annealing” for further consideration at eLife. Your revised article has been favorably evaluated by Randy Schekman (Senior Editor), a Reviewing Editor, and two reviewers. The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

Please discuss the recent study of Woodall et al. (Nat. Comms, 6:8099; DOI: 10.1038/ncomms9099) on EmrE topologies.

Following are the full reports of the reviewers.

Reviewer #2:

The authors have, in my opinion, responded extremely well to the previous reviews. Critical questions raised have been addressed by the performance of additional simulations and analyses. The conclusions of the paper have been strengthened significantly as a result.

A new issue has arisen, however. Woodall et al. (Nat. Comms 6:8099; DOI: 10.1038/ncomms9099) have just reported (26 August) experiments directed at answering the question of how a cell can generate equal populations of two opposite topologies of EmrE. An important conclusion is that the FtsH protease of E. coli cleans up misfolded or unpaired EmrEs to create equal populations of both EmrE topologies. The authors should address these new findings, particularly in the context of their Figure 7B.

Reviewer #3:

The authors have satisfactorily addressed my concerns. I recommend the manuscript's publication.
