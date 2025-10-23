# Peer review - Round 1

Editors:
- Michel Bagnat, https://ror.org/00py81415 Duke University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69082.sa0](https://doi.org/10.7554/eLife.69082.sa0)

The authors examine the process of mesoderm invagination in the Drosphila embryo and found that while myosin contractility is critical to prevent tissue relaxation during the early phase of the process, it is dispensable for the subsequent folding step. Through modeling and experimental analyses, the authors find that folding is likely mediated by a joint action of active cell shape changes in the mesoderm and apico-basal shrinking in the surrounding ectoderm and suggest that the mesoderm behave as a mechanically bistable tissue during gastrulation.


---

# Peer review - Round 1

Editors:
- Michel Bagnat, https://ror.org/00py81415 Duke University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69082.sa1](https://doi.org/10.7554/eLife.69082.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Mechanical bistability enabled by ectodermal compression facilitates Drosophila mesoderm invagination" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Utpal Banerjee as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Sebastian J Streichan (Reviewer #1); Magali Suzanne (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

The authors address how contractile forces near the apical surface of a cell sheet drive out-of-plane bending of the sheet. To determine whether actomyosin contractility is required throughout the folding process and to identify potential actomyosin independent contributions for invagination, they develop an optogenetic-mediated inhibition of myosin and show that myosin contractility is critical to prevent tissue relaxation during the early stage of folding but is dispensable for the deepening of the invagination. The results shown in the first two figures support the idea that the mesoderm is mechanically bistable during gastrulation.

In the second part of this study, the authors test the role of the coupling between mesoderm and ectoderm by using 2D computational modelling and infrared pulsed laser dissection. They propose that the ectoderm can generate compressive forces on the mesoderm facilitating mesoderm internalization (2nd phase).

They then propose that this mechanical bistability arises from an in-plane compression from the surrounding ectoderm and that mesoderm invagination is achieved through the combination of apical constriction and tissue compression.

While the optogenetic experiments require additional controls, the overall results are compelling and deemed both interesting and significant for the field. By contrast, figure 4,5,6 appear highly speculative, and have substantial issues (e.g. reporting effects orders of magnitude below diffraction limit).

The manuscript presents two different models for data interpretation. The first one is a modified version of an earlier model that provides some predictions that can be tested with relatively simple experiments. On the other hand, the second model is rather complex and should be further analyzed with great care, before considering it for publication. It appears highly overparameterized, oftentimes using ad-hoc modifications for generating a desired effect. Moreover, it is a well-known fact from thin sheet elasticity that contributions of bending to total elastic energy are weighted by thickness cubed. The cell thickness shown are considerably thinner than the equivalent of cells in the embryo. At a thickness comparable to embryonic cells, bending will become orders of magnitude more costly. It further remains unclear how a dynamic variable is obtained. Thus, it is also unclear how the simulations ensure a robust trajectory in a high dimensional phase space with likely multiple minima.

After vigorous discussion with all reviewers, there emerged the possibility to focus the present manuscript on the original optogenetics findings, described in figure 1 and 2, and then quantitative analysis of predictions made by model shown in figure 3. These tests should include lateral edge lengths, across all cells in the ectoderm. Here it will be important to distinguish passive effects in the ectoderm due to pulling from the ventral furrow: If the furrow pulls, cells might actually also shorten laterally. This can be tested using wide-spread twist mutants. Finally, the authors need down their claim of compression. In the discussion, it may be mentioned the possibility of compression. However, the existing data does not support for such a mechanism at all.

Essential revisions:

1. Provide quantitative data of cell shape changes near the ventral furrow. Analysis should include both apical as well as lateral cell surface areas.

2. The authors analyze the effects of RhoDN on MyoII but never on the F-actin network. Rho1 is known to control F-actin organization so this should also be tackled thoroughly.

3. Test actomyosin contractility by measuring network recoil after laser dissection in control (RhoDN non activated) and RhoDN activated embryo.

4. Test the modification of the Polyakov model using available data. Since the lateral rest lengths are modified such that cells shorten over time (by 20 % – in real cells this would be about 8µm), if all 60 ectoderm cells shrink that much, this can result in a considerable in-plane expansion, assuming volume conservation. This could be tested by measuring the time course of average lateral length change of cells in the ectoderm (on the dorsal pole, and in the lateral regions), and explain how this compares to model assumptions.

5. Some degree of lateral cell shrinking is expected from ventral furrow pull. To distinguish possible contributions from ventral furrow vs active processes shortening the cell edges as proposed in the model, the authors should repeat the lateral cell surface analysis from (5) in twist or snail mutants.

6. To address to some extent the role of the mesoderm the authors could perform an early optogenetic RhoDN of the ventral side. If the ectoderm is pushing, then one could predict that the ventral cells should reduce their size along DV but not along AP because of the DV pushing from left and right ectoderms.

These experiments and the contrast of data with the modified Polyakov model may allow the authors to arrive at a soft conclusion implicating other forces, e.g. ectoderm compression, in the discussion.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Mechanical bistability of the mesoderm epithelium facilitates mesoderm invagination during Drosophila gastrulation" for further consideration by eLife. Your revised article has been reviewed by 3 peer reviewers and the evaluation has been overseen by Utpal Banerjee as the Senior Editor, and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Essential revisions:

The reviewers have found the manuscript much impproved and have praised the extensive work performed to address their criticism. This has resulted in a greatly improved manuscript that needs no further experimental work and is almost ready for publication pending some editorial changes. Specifically, they have pointed out one analysis that needs attention and several discussion points that should be addressed with text changes as follows:

1. For Figure 9f the authors have opted to track an ectoderm cell over time to demonstrate ectoderm displacement. This is fine, nevertheless the author should be consistent and perform again the analysis for Figure 9f by using the same analysis procedure they implemented for Figure 9a. More precisely the authors should follow a cell that is located 20 cells away from the midline (not just 10 cell away).

Discussion points:

2. The model should be described as a theory. In its current form it is hard to distinguish from the descriptions of experiments. It should be clearly labeled that it is purely elastic, and that it neglects the well-known viscous properties of tissues that dominate on the scale of at least 4 minutes and beyond.

3. On page 19 and eventually in the discussion the discrepancy between the model and the in vivo measurements should be discussed. More precisely, along a cross-section in the model the minimum necessary ectoderm cell shortening is 5-10% for 60 cells while in the real embryo the cell-shortening measured is 4-8% for a much smaller number of ectoderm cells closer to the mesoderm (20 cells?). Please consider these potential discrepancies and if they are indeed present discuss its possible origin and/or speculate in the discussion what might account for them.

4. In the new version of the paper, it is pointed out that F-actin in ectoderm cells is not affected by RhoDN optogenetic activation. This is quite puzzling and therefore merits at least further discussion.

5. In Figure 4A and in many other experiments, RhoDN is activated both in the mesoderm and in the ectoderm. Therefore, by following the logic of the model, ectoderm pushing is not dependent on Rho signaling. In other words, while mesoderm cell shortening depends on Rho, ectoderm cell shortening is Rho independent. This also is quite surprising thus merits further discussion.

6. The manuscript has valuable data on cell behaviors in the lateral ectoderm. But, the presentation is entirely focused around the idea of 'compression', and no alternatives discussed. One such alternative, could be the impact of germband extension on deepening the already formed furrow. The cellular flow of germband has a component directed towards the ventral pole, possibly allowing cells to flow into furrow, that has already formed. This extension will lead to the observed apicobasal shortening of lateral ectoderm cells, and deepening of the fold, but requires no mechanical bistablity. It would further be consistent with lack of fold and the described cell shapes at the apical surface in Snail and opto RhoDN experiment.

7. Stress is needed to build up for the proposed buckling by compression. However, the Snail experiments clearly demonstrate that no buckling of mesoderm occurs when cell behaviors in the mesoderm are perturbed. Stating mesoderm buckles due to compression from the ectoderm is, therefore, misleading and has not been demonstrated with an experiment. Any mention of this interpretation should be confined to the discussion.

8. In the discussion, the statement "Using computer modeling, we further demonstrated that mechanical bistablity in the mesoderm can arise from an apicobasal shrinkage of the ectoderm, which generates in-plane compression as the cell volume remains conserved" is misleading. This needs to be clarified, if the authors wish to raise the idea of bistability in the Discussion section.

9. While the authors consistently claim precise agreement between the model and data, it remains unclear to what extend this is the case. Visuals of simulations are provided. But there are no quantitative comparisons found that directly compare a model result with a corresponding measurement. Therefore, such claims (e.g. page 14 "In particular, the transitional state of the tissue revealed in the simulation is nearly identical to that identified in our ontogenetic experiments") have to be toned down (e.g. looks visually similar).

10. The quantitative analysis shown in figure 8 appears inconsistent with the descriptions. First, the authors refer to a rate of volume reduction, but show volume. Moreover, rate of volume reduction in WT appears consistently different from snail, yet is described as very similar. Such strong claims should either be toned down or backed up with a statistical significance test.

11. In the text page 20, the authors describe "In the wild type embryos, the compression promotes ventral furrow invagination, which in turn functions as a 'sink' to facilitate the movement of the ectoderm in the ventral direction". There is no experimental evidence provided for compression, and therefore this statement is speculation. Please rephrase.

Reviewer #1 (Recommendations for the authors):

The revised manuscript by Guo et al. has been revised, addressing some but not all of my concerns. In fact, the manuscript provides additional data, that argues strongly against the proposed mechanical bistability mechanism. The manuscript reads like two separate works.

The authors raise an interesting question in the abstract: Is myosin contractility at the apical surface required throughout folding? In the current version, characterization of the opto tool is much improved. It allows the authors to demonstrate apical myosin activity is not needed in a late phase of furrowing. The results presented in the first five figures are very interesting on their own, and provide a valuable contribution to the field. In my opinion, this would be an excellent point to stop the manuscript and enter the Discussion section. Such a work would be a great addition to eLife.

Instead, the authors enter a new direction, and propose mechanical bistablity of the mesoderm, to explain these ideas. This is somewhat unclear, as there are many possibly simpler explanations consistent with this very interesting observation that are not discussed (see more below). Instead, in figures six to nine, the manuscript hinges on speculation, and a purely elasticity-based model in combination with analysis of cell geometry along the apicobasal surface in support of their hypothesis. The conclusion, that invagination requires mechanical bistabilty of the mesoderm cannot be supported with the data presented. These claims should be toned down before publication, as already suggested in the first round of revisions. It seems this problem can be fixed by clarifications, and moving speculative data interpretation from the Results section to the Discussion sections.

(1) The manuscript offers no support for mechanical bistablity assumption. That purely elastic materials can buckle under compression is well established. But, the authors supply data that argues against mechanical bistablity in this system.

– Experimental data does not go beyond correlation, and yet the mechanism presented claims a causal role of ectoderm compression for ventral furrow folding. The original manuscript attempted to provide experimental data in support of the mechanical instability model. The current figures describe cell shapes in 3D, but there is no test of causality offered. This is somewhat puzzling, as the optogenetic tool should also function in the lateral ectoderm.

– The model should be described as a theory. In its current form it is hard to distinguish from the descriptions of experiments. It should be clearly labeled that it is purely elastic, and that it neglects the well-known viscous properties of tissues that dominate on the scale of at least 4 minutes and beyond.

– It is not clear to what extend the material in figure 8 supports the main argument. Instead, it seems to show the opposite. Lateral ectoderm shorting happens wether or not ventral furrow forms. This is a clear demonstration that the proposed mechanical bistability assumption is not able to drive tissue folding. Instead, these results suggest that folding needs to occur through an independent mechanism. Deepening of the fold could be generated by another mechanism (see below).

– Compression, as indicated by the authors, implies reduction in apical surface area of compressed cells, which is not shown in Snail or early opto RhoDN experiment. Early opto RhoDN experiments are described as heterogeneous cell morphology, but not further analyzed because of technical challenges. It is not clear how this is a technical problem, and not an issue of data interpretation. Heterogeneous apical cell area is consistent with cell shear, but not with external compression.

2) Discussion of model limitations and alternative scenarios.

– I congratulate the authors on their observation in figure 4b. It seems reasonable to further analyze this interesting phenomenon, and study the possible impact of tissue tissue interactions. In doing so, the manuscript would benefit from an open approach.

– The manuscript has valuable data on cell behaviors in the lateral ectoderm. But, the presentation is entirely focused around the idea of 'compression', and no alternatives discussed.

– One such alternative, could be the impact of germband extension on deepening the already formed furrow. The cellular flow of germband has a component directed towards the ventral pole, possibly allowing cells to flow into furrow, that has already formed. This extension will lead to the observed apicobasal shortening of lateral ectoderm cells, and deepening of the fold, but requires no mechanical bistablity. It would further be consistent with lack of fold and the described cell shapes at the apical surface in Snail and opto RhoDN experiment.

– The timescale of elasticity is very short compared to the 20 minutes of ventral furrow. As pointed out by the authors, the cited paper by Doubrovinsky provides an estimate for the transition to viscosity within 4 minutes. It is one of the longest currently published timescales for this process. As the authors clearly demonstrated turnover of the actomyosin cytoskeleton is very fast, further indicating the four minutes estimate is an upper bound of what is to be expected for these cells.

But, even if it is as long as four minutes, viscosity means, stresses will dissipate. Stress however is needed to build up for the proposed buckling by compression. Snail experiments clearly demonstrate that no buckling of mesoderm occurs when cell behaviors in the mesoderm are perturbed. Stating mesoderm buckles due to compression from the ectoderm is misleading, and has not been demonstrated with an experiment. Any mention of this interpretation should be confined to the discussion.

– In the discussion, the statement "Using computer modeling, we further demonstrated that mechanical bistablity in the mesoderm can arise from an apicobasal shrinkage of the ectoderm, which generates in-plane compression as the cell volume remains conserved" is misleading. The authors neither showed that ectoderm compresses mesoderm, nor is it a novel result that elastic systems can buckle under compression. This needs to be clarified, if the authors wish to raise the idea of bistability in the Discussion section.

– While the authors consistently claim precise agreement between the model and data, it remains unclear to what extend this is the case. Visuals of simulations are provided. But there are no quantitative comparisons found that directly compare a model result with a corresponding measurement. Therefore, such claims (e.g. page 14 "In particular, the transitional state of the tissue revealed in the simulation is nearly identical to that identified in our ontogenetic experiments") have to be toned down (e.g. looks visually similar).

Reviewer #2 (Recommendations for the authors):

Guo et al. have revised their paper by following the reviewer's suggestion.

The science presented is now more solid and merits publications after addressing the following 4 points:

1) In the new version of the paper, Guo and colleagues point out the fact that F-actin in ectoderm cells is not affected by RhoDN optogenetic activation. This is quite puzzling and therefore merits at least further discussion.

2) In Figure 4A and in many other experiments, RhoDN is activated both in the mesoderm and in the ectoderm. Therefore, by following the logic of the authors model, ectoderm pushing is not dependent on Rho signaling. In other terms, while mesoderm cell shortening depends on Rho, ectoderm cell shortening is Rho independent. This also is quite surprising thus merits further discussion.

3) For Figure 9f the authors have opted to track an ectoderm cell over time to demonstrate ectoderm displacement. This is fine, nevertheless the authors should be consistent and perform again the analysis for Figure 9f by using the same analysis protocol implemented for Figure 9a. More precisely the authors should follow a cell that is located 20 cells away from the midline (not just 10 cells away).

4) At page 19 and eventually in the discussion the authors should emphasize the discrepancy between the model and the in vivo measurements. More precisely they should make clear that along a cross-section in the model the minimum necessary ectoderm cell shortening is 5-10% for 60 cells while in the real embryo the cell-shortening measured is 4-8% for a much smaller number of ectoderm cells closer to the mesoderm (20 cells?).

Reviewer #3 (Recommendations for the authors):

The authors have done a great job responding to the concerns raised by the 3 referees with the quantitative analysis of cell shape after Rho1 inhibition, the analysis of the impact of Rho1 inhibition on F-actin, new laser ablation experiments to confirm the inactivation of myosin with their opto-Rho1DN construct, the analysis of the extend of endodermal shortening both on control and snail mutant embryos, the addition of active lateral contraction in the mesoderm in the model. They have added new data and analysis that strengthen the overall impact of the paper. They further discuss their findings in a more general context regarding previous works. I strongly support publication.
