# Peer review - Round 1

Editors:
- Edoardo M Airoldi, Harvard University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.04640.030](https://doi.org/10.7554/eLife.04640.030)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Perturbation biology models predict c-Myc as an effective co-target in RAF inhibitor resistant melanoma cells” for consideration at eLife. Your article has been favorably evaluated by Aviv Regev (Senior editor), a Reviewing Editor, and two additional reviewers.

The Reviewing editor and the reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

The editorial team has identified two areas of major concern: (1) novelty of the approach and (2) biological significance.

Regarding novelty of the approach, a portion of the most interesting methodological innovations has been already published by a subset of the authors. The pre-processing PERA step is new, and so are a number of other technical advances. In this paper, the authors extended the scope of the analysis substantially (phosphoprotein antibodies from 16 to 138, perturbation conditions from 44 to 89, and phenotypes from 1 to 5), and we appreciate that this extension is critical for biologists to adopt such approaches. However, the authors fail to clearly present the innovations over previous work. The authors should make an effort, perhaps in a dedicated subsection under Methods, to offer a nuanced discussion of the approach stating how it supports scientific discovery, what is novel relative to the earlier studies, and what are the open challenges. Overall the approach is technically solid and well motivated, and eLife readers will benefit from such a discussion in the context of the new and extensive data set.

Regarding biological significance, the reviewers all agree that the authors do not clearly address how their results advance our understanding of the biology, nor provide any novel biological insights. It is very important that any conceptual novelty is highlighted in the revised manuscript.

Other serious concerns include limitations of the approach with respect to predictions (reviewer 2, please address this in the response and in the manuscript), and lack of a convincing statistical validation (e.g., frequentist coverage of the predictions in a realistic simulation study – where data are generated using parameters estimated from the real data). We would like to see these addressed in the revision as well.

Overall, this is a solid piece of work, and we look forward to receiving a revision.

Reviewer #1:

The authors applied belief propagation to data from systematic pharmacological perturbations and generated network models of signaling in melanoma cells. The authors used these models to predict cellular responses to untested drug perturbations. Simulating the models, the authors made predictions for effective combinations of perturbation. The authors argue that one of these predictions, that co-targeting c-Myc with MEK or RAF is synergistic, is non trivial and go on to demonstrate experimentally a synergistic effect of co-treating.

Conceptual and high-level feedback:

In my opinion, the most significant and general result of this work is showing the promise of genomically-informed preclinical trials and providing a concrete example of a synergistic pharmacological treatment inhibiting the cell division of melanoma cells. The experimental design and the network inference methodology seem careful and well executed. The results appear convincing. On the down-side, I do not see much conceptual novelty or results contributing to our understanding of the biology. It is also not clear to me that the initial synergistic effect of co-targeting, which is interesting and explored in details, will actually prevent the development of drug-resistance over the long term in a clinical application. I invite the authors to emphasize any conceptual advances in their work and new biological conclusions that I may be missing. I think that conceptual advances would contribute the most to elevating the significance and general interest in this work.

[Minor comments not shown.]

Reviewer #2:

In this study, the authors use a belief propagation (BP) algorithm to construct a network model of nearly 100 (phospho)proteins and several phenotypes in response to single and paired drug treatments. The network models use a differential equation framework, so they can be simulated to predict the response of the observed variables (proteins, phenotypes, etc.) to new perturbations and arbitrary combinations of perturbations. Simulations nominate c-Myc, which was not perturbed in the original drug screen, due to its in silico effect on G1 arrest. c-Myc is targeted indirectly with JQ1, and JQ1 in combination with predicted complementary inhibitors (MEKi and RAFi) induce strong changes in viability and G1 arrest.

The modeling approach is inherently limited to make predictions about proteins on the protein array in the perturbation screen and edges represent indirect effects, but the experimental/computational technique – in particular the focus on quantitative, predictive instead of descriptive networks – is powerful when there is sufficient coverage on the protein array. The algorithmic innovations have already been published (BP algorithm and preliminary SkMel-133 analysis in Molinelli 2013; including prior knowledge in Miller 2013). This manuscript expands the (phospho)protein antibodies (16 to 138), perturbation conditions (44 to 89), and phenotypes (1 to 5) modeled in RAFi-resistant SkMel-133 cells and evaluates new predicted pairs of inhibitors. It also introduces the pre-processing PERA step, which improves the inclusion of prior pathway knowledge by making it more systematic. The prior implementation – using soft constraints and rewarding edges with prior support instead of penalizing those without – is well-motivated given that interactions in pathway databases are derived from different cell types.

1) The criteria used to select c-Myc and G1 arrest instead of other phenotypes and top-ranked in silico perturbations are not made explicit, making it difficult to assess how well the method could predict additional novel perturbations. Figure 5–figure supplement 2 shows that the top perturbation for all phenotypes is not novel but rather one of the activity nodes for the originally screened drugs. c-Myc does cause a substantial change to G1 arrest in silico, but so do other novel perturbations like p38 on viability, STAT3pY705 on S arrest, etc. Furthermore, it appears that there was no preference given to combinations of drugs that are predicted to be synergistic (similar to Miller 2013) or take effect at the lowest possible doses. Indeed, the top viability perturbations – PKCi and CDK4i – only reduced viability at high doses.

2) Is the RAFi-resistance phenotype of the SkMel-133 cell line recapitulated in the computational model? bRAF or aBRAF are top 10 predicted perturbations for all phenotypes except G2 arrest.

3) Are the observed changes in G1 arrest under inhibitor treatment statistically significant?

4) What was done to verify the identity of the SkMel-133 cell line?

5) Edge frequencies are one way to assess BP stability, and Figure 4–figure supplement 2 shows that there are few stable edges. How much do the phenotype predictions vary across the 4000 simulations?

[Minor comments not shown.]
