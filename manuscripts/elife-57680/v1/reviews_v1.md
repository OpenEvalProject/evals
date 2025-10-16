# Peer review - Round 1

Editors:
- Lucie Delemotte, KTH Royal Institute of Technology Sweden

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.57680.sa1](https://doi.org/10.7554/eLife.57680.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper presents an experimentally validated model of the IKs channel, KCNQ1+E1 in two states, Activated/Open and Resting /Closed, based in large part on an extensive review of experimentally-derived constraints. The models reported, deposited in PDB-dev will be of great value to the community. By comparing to the cryo-EM structure of KCNQ1+E3, the structural origin of profound functional differences with important physiological consequences is revealed.

Decision letter after peer review:

Thank you for submitting your article "Allosteric Mechanism for KCNE1 Modulation of KCNQ1 Potassium Channel Activation" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Lucie Delemotte as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Kenton Swartz as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Leon D Islas (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

KCNQ1 channels are a principal component of the slow-activating repolarization current in the heart. The slow activation character is produced by an interaction with the KCNE1 regulatory subunit. Although a well-characterized interaction, the molecular details of this are still controversial. The paper by Kuenze et al. investigates the molecular details of the association between the KCNQ1 channel and its regulatory subunit, KCNE1. Through molecular modeling and protein-protein docking, the authors arrive at a proposed mode of interaction between KCNE1 and models of the closed and open KCNQ1 channel. These detailed molecular interactions then are validated via a varied number of experiments, including mutagenesis, electrophysiological analysis of the effects of mutations and cysteine-cysteine crosslinking. Contrary to previous belief, the FTL motif in KCNE1 is not directly interacting with S6. Instead, the authors propose that FTL affects S6 via a allosteric network via S5. Comparing their KCNQ1/KCNE1 models with the KCNQ1/KCNE3 structure, they found that KCNE1 and KCNE3 share a very similar binding site. But different interactions of FTL in KCNE1 and TVD in KCNE3 with KCNQ1 are proposed to account for the different functional modulation of KCNQ1 by different KCNE subunits.

The reviewers agreed that the models deposited in PDB-dev would be of great value to the community, and that the review of experimental restraints used to build the models are in and of itself of great value. They also judged that the experimental validation of the proposed models was thorough and increased the confidence in the proposed modes of interaction between the two proteins. The data were thus convincing, but the conclusions about interactions were sometimes overstated and a more extensive discussion about the mechanism of KCNE1 was needed. Additionally there were some concerns about the way the cross-linking experiments were carried out. A detailed review is included below.

Experiments:

1) Related to Figure 2 and all other experiments using crosslinking: the authors show that under control, reducing or oxidizing conditions the magnitude of the currents are different. The way the data are presented and described led us to understand that each treatment, control, DTT or Cu-Phenantroline was applied to different groups of cells. If this is the case, this is a major experimental problem. Since there is variability in expression level and possibly changes in open probability and/or single channel conductance in each of the mutants that the authors are not accounting for, a simple comparison of the current density magnitude between different treatments is meaningless. These experiments should be carried out in the same cell. Typically disulfide bond formation (crosslinking) is induced by Cu-Phe after basal current recording and then reversed by DTT. There is a vast literature making use of this technique and this is the accepted way of performing this experiment. The authors should clarify if this is indeed what they did and show an example of such an experiment.

Conversely, if each treatment was applied to different groups of cells, the authors should show that the introduced cysteine residue produces no changes in open probability and single-channel conductance.

2) The recordings shown by the authors were obtained in a limited voltage range, up to 60 mV. The tail currents show that the activation is far from saturation at this voltage and in consequence the estimation of the V1/2 from these curves incurs in an error, which could be very large. The authors should comment on these limitations or alternatively estimate this parameter from currents obtained at a wider range of voltages.

Modeling:

1) To strengthen confidence in the modeling procedure, the following controls should be carried out: the docking of E1 should be done on the recent human structures of the activated/open state hKCNQ1 instead of only on the author's previous model. Conversely, docking of E3 to their AO model (and to the experimental structure mentioned above) should be performed to demonstrate that the procedure allows to recapitulate the experimental binding pose.

2) Figure 3—figure supplement 1 shows a comparison of the models obtained in this work with the cryo-EM structure. The authors show that the backbone RMSD is fairly low between models and structure, but it would be more informative to show the degree of deviation of the position of side chains, especially in the regions in the models that were used for docking the KCNE1.

3) Another aspect that is not even mentioned by the authors is the fact that the stoichiometry of KCNQ1-KCNE1 complexes appears to be variable. There is no experimental consensus on how many KCNE1 subunits are present per tetrameric KCNQ1 and the evidence seems to support the view that the number of KCNE1 subunits associated with a KCNQ1 tetramer depends on the expression level of the former. The authors seem to have chosen a 2:1 KCNE1:tetramer assembly for their simulations. Although a different stoichiometry might or might not alter the details of the interaction, it has been show that the variable stoichiometry can alter the biophysical effect (degree of voltage shift among others) of KCNE1, indeed suggesting that the mode of interaction might also not be unique. Did you try docking four KCNE1s per tetramer? Would this different stoichiometry alter the mode of interaction between KCNE1s and KCNQ1? At the very least, the authors should discuss this variable affects and their choice of stoichiometry.

Contextualization and Interpretation of data:

1) Abstract: "FTL… affects the channel gate via an allosteric network." This is not shown, but only a proposed mechanism. Please state as suggestion, not fact.

2) “ Likewise, mutation of FTL to TVG renders the KCNQ1-KCNE1 channel constitutively active, similar to KCNQ1-KCNE3” and other similar statements. Previous studies have shown that KCNQ1/KCNE1-TVG is not a constitutively open KCNQ1/KCNE3-like channel (Panaghie et al., 2006; Barro-Soria et al., 2017), in contrast to the work by Melman. Maybe good to tone down this conclusion? Or more evidence showing that TVG converts KCNQ1-KCNE1 into constitutively conductive KCNQ1-KCNE3 would be good.

3) In Figure 2, why was the focus of the experiments on the extracellular portion of the (TM) region of E1? From the SI tables, there seems to be fewer constraints from interactions of the intracellular portion.

4) “ Both mutations resulted in smaller peak current amplitudes and significantly depolarized activation V1/2 (ΔV1/2,K362A = 14.7 mV, ΔV1/2,N365A = 14.7 mV) (Figure 5D+E, Supplementary file 1—table 5), indicating that these mutant channels required more energy to open, possibly due to a loss of stabilizing interactions with KCNE1.”. The conclusion is a little too strong. The fact that mutations at K362 and N365 make the channel activate at more depolarized voltages doesn't mean they affect the interaction with KCNE1, even though they seem close to KCNE1 in the model. K362 and N365 are in S6 and maybe just important for pore opening. Crosslinking or double mutant cycle analysis for the C ends of S6 and E1 (say K362 and S68), or KCNE1-dependent effects of K362 and N365 mutations would be needed to claim interactions.

5) Subsection “Experimental validation of KCNE1 residues interacting with KCNQ1” paragraph four. Mutations at W323 and Y46 share similar phenotypes of GV relations, but authors didn't show any experimental evidence to confirm that they are in direct contact (In the model they seem to be close together). Also, Y46 mutant had faster activation kinetics while W323 had wt-like activation kinetics, why is that if they are indeed functionally interacting?

6) Discussion paragraph two. "FTL can affect the nearly PAG motif through the mediation of S5", what residues in S5 is responsible for the mediation? From Figure 9 the authors labeled 263, 266, 267 and 270 and mentioned that mutations of them change the channel activation. Please clarify these mutational effects and discuss how they would differ for the FTL motif and the TVG motif.

7) Discussion paragraph three. This whole paragraph provides some experimental studies to support the model that FTL motif affects PAG motif via S5 involvement. But how this model induces the slower activation gating of KCNQ1 is not clear. To answer this question that the authors mentioned in the beginning of discussion, we would like more evidence and discussion concerning how FTL motif makes the KCNQ1 channel slow to open.

8) Discussion paragraph five. In Barro-Soria et al., 2017, they concluded that FTL also affects the S4 movement.

9) “ This mechanism may account for at least some of the gating differences between KCNE1 and KCNE3” and “ This proposed mechanism can account for the different effects of KCNE1 and KCNE3 on KCNQ1 gating”. This is too strong a statement. Similar to comment 7 above, how does the FTL motif makes Q1 channel open slowly while TVG motif makes Q1 constitutively leaky using this proposed model. It seems like the authors have more ideas about how KCNE1 affects KCNQ1 than how KCNE3 affects KCNQ1? Maybe stick to the more obvious effects seen/proposed?

10) Figure 5. Why does the amplitude go down for mutants? Is this really a good parameter to measure interactions? What is the rationale behind this conclusion?

11) Figure 8. Y267-T58 interaction seems very important for the proposed mechanism, but very little data is shown for this interaction (just simulations, except Y267F reducing expression, but consider concern above). Any more data for this interactions?

12) Figure 7. Y65A looks as good as Y65 or Y65F. So is the aromatic ring at Y65 really important?

13) In several places, data that is used to impose constraints in the model is then used to corroborate the relevance of the model. That should be avoided, or at least clarified.

14) The role of the interaction between Y267 and residues on S4 (M238 and D242) is intriguing, and its disruption when E1 is bound but not E3. Are those state-dependent and can they be related to the stabilization of the specific VSD state?

15) The 274-45 pair that are suggested to crosslink are not that close in either model (15A) and seem to point in different directions.

Presentation of results:

1) In Figure 5, the authors focus on residue W323, Y267 and K362/N365 because they had the largest number of contacts with E1 in a specific segment. Where is the data supporting this claim? The way the contacts are presented in this figure was confusing to several reviewers.

2) Figure 2—figure supplement 2. This is not the correct figure. wt KCNE1 should be shown, not as now with mutant KCNE1. This is a crucial control experiment. Also, the very important controls for wt KCNQ1 coexpressed with KCNE1 cys mutants are missing.

3) Figure 7 B-C. What are the authors trying to convey with these data? The reviewers did not see any obvious pattern. Is the correlation they propose really significant?
