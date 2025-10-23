# Peer review - Round 1

Editors:
- Dominique Bergmann, Stanford University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.01967.027](https://doi.org/10.7554/eLife.01967.027)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Subcellular and supracellular mechanical stress prescribes cytoskeleton behavior in Arabidopsis cotyledon pavement cells” for consideration at eLife. Your article has been favorably evaluated by a Senior editor, Detlef Weigel, and 2 reviewers, one of whom is a member of our Board of Reviewing Editors.

The Reviewing editor and the other reviewer discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

Mechanical influences on developmental and cellular properties are an important topic of broad impact in plants and animals. After having been out of fashion for a few decades, this topic (aided by new tools) is experiencing a renaissance. This manuscript complements recent work on tissue-level dynamics in the plant shoot meristem by examining the relationships between growth, stress patterns and microtubules (MTs) in crenulated pavement cells of the leaf epidermis. New data here provide more convincing experimental support that MTs respond to stress, and novel work with an AFM system shows that MT patterns and cellulose MF patterns match. Exploiting the large size of pavement cells and using mechanical manipulations (ablations), the authors show a correlation between the frequency of katanin-mediated MT severing events and reactions to mechanical stress. Their observation that tissue level stress can override cell level stress was also documented in a recent paper from Jacques et al. (2013). Altogether these experiments and models have the potential to have a broad impact on our thinking about mechanical influences on development.

There are a number of improvements that should be made to the models, and the manuscript could benefit from some clearer writing and some further analysis of data already collected. Specific major issues to be addressed in a revised manuscript are enumerated below.

1) Re-evaluation of models used to represent cells.

Reviewers were concerned about the models used to represent cells in this manuscript, specifically what appears to be a balloon-type model representing only the surface cell wall, whose stresses reported may not be representative of real pavement cells. When looking at the finer details of stress patterns of individual cells, the patterns do not look like what would be expected from a proper 3D model of a cell – the necks should be under compression and the lobes under tension (see for example Dumais and Steele 2000 paper, which the authors cite). In the presented model all stresses are tensional, even after ablation, which may not be realistic. Moreover, the text is misleading in making this appear to be a 3D model when it may be a 2D surface of cells, tethered to a substrate by springs at the anticlinal walls. If it is too difficult or inappropriate to apply the 3D model based on their previous shoot apex work (where cells have a very different shape), please explain. Similarly, the model used (and assumptions) should be much more clearly explained in the main text, as the difference between a 2D model with springs and a full 3D model is potentially very important. It is a bit hard to justify making a fine-grained analysis of stresses in a situation where the geometry of the model itself has not been shown to be representative of the system. For example, in 3D one would expect the neck of a pressurized, isolated pavement cell to be under compression.

Minimal additions to the models include:

Begin by representing the compressional stresses in the model in a different color. If the neck regions are indeed under compression (at least after ablation of neighbor), this would be a satisfactory test of the utility of the model. A hand-drawn model with a few pavement cells in Abaqus would be OK. The cells do not have to be perfect, just qualitatively similar in shape (with lobes and necks). Then apply similar loading conditions as in previous simulations and compare it with the simulation where one cell is removed. Please show both tangential stresses, with a color scheme that also indicates compression.

Correct (or explain) why in Figure panels 4A and B (the model ablation) the cell outlines exactly overlap. Shouldn't the borders move a bit in B next to the cells that are ablated? What exactly does ablation change in the model, if not the boundary next to the ablated cells?

2) Dissect the cell vs. tissue response to stress

A major conceptual advance would come from a deeper analysis of the continuum of cell and tissue responsiveness to stress. The authors propose that “MT behavior depends on stress intensity, which is cell autonomous as long as tissue stresses do not override it”. It would be extremely valuable to calculate or model under what conditions a tissue-level stress would override a cellular stress.

Along these lines, the authors might test whether pavement cell lobes that differ in their orientation relative to the overall growth direction of the leaf and/or relative to the cut sites, have different sensitivities or degrees of MT anisotropies. The answer to this will give a parameter to address the cell autonomy vs. tissue response. Another simple test would be to look at whether guard cell MTs respond to cuts. Given the evidence that GCs created their own local zones of stress and oriented MTs, my guess would be no, but there might be an interesting correlation with “elevated” vs. planar and open vs. closed stomata with respect to responsiveness. This could provide another example of differential “set points” in the cell vs. tissue continuum.

Also, if cutting experiments release tension globally, then wouldn't the MTs be expected to become less oriented?

3) Formulate a compelling argument for how plant cells sense stress and how this generates shape.

The Abstract states “Force patterns in plant tissues control cell shapes...”. In support, the authors point to their (very nice) previous work that suggests that MT orientation is controlled by stresses in the tissue, which can be deduced from organ shape (Introduction, paragraph 2). However, this is difficult to reconcile even in the shoot apex. If cells start out with a random orientation creating isotropic growth, why doesn't the plant just create a globular structure? How can MTs be responsible for both tissue shape and cell shape if their orientation is primarily controlled by stress? Another interpretation would be that MT orientation is specified by a mechanism other than stress. Genetically defined organizing centers could control tissue and cell polarity, controlling the orientation of MTs. The shape change induced by the MT orientation would then direct the cellulose orientation, and thus cell wall anisotropy, and create non-trivial shapes. The resulting shape would then have a stress pattern that correlates with the MT orientation, which the authors observe. What is the mechanism for sensing stress? It is relatively easy to sense strains, but how can you sense stress, without invoking strain at some point?

4) Reword section on cell-wall anisotropy to reflect indirect measure of this property.

The claim that pavement cell shape relies on oriented MTs affecting cell wall anisotropy has not actually been clearly demonstrated. The AFM results that show the technique can see the CMF bundles in walls. The results are very nice and convincing, and it is believable that you are indeed making a map of the CMF network with the AFM. However this are not measuring cell wall anisotropy in-plane with these experiments as the text seems to claim. However I see nothing wrong with using this data as a proxy for cell wall anisotropy. One should also note that this still does not show a causal relationship between MT and CMF orientation in this system, but it is convincing correlative data given what is already know about the interaction there.

5) Separate the effects of material properties from those that arise from cellular geometry.

The authors propose that lack of movement of the necks after ablation proves that they are stiffer in this region (second paragraph of the Results section entitled “Pavement cell wall shape correlates with microtubule organization…”). However, intuitively, effects of geometry would dominate stiffness here. I would be surprised if the ablation of a neighbor cell in a model with uniform material properties would show an equal displacement in necks and lobes, and this should be tested.

6) Revisit cell-pressing experiments with better images and proper citations of previous literature.

It is difficult to see the differences in the experiments were cells are pressed by slides (Figure 3). In the text the differences are reported to be 0.37 vs 0.57 by their anisotropy measure. They report the same amount of difference (0.2) for necks vs lobes where the orientation is obvious. Why is it so much harder to see here? Also it is claimed that the effect is reversible, and that the value goes to 0.24 a day after the slide is removed. But this is quite a bit less than the starting point of 0.37, unless 0.13 of the difference appears instantly. If this is the case, the “before” condition needs to be quantified and presented for comparison. Jacques et al. (2013) have done similar experiments pressing on leaf epidermal cells; these previous results need to be mentioned and evaluated more extensively in this manuscript.

7) A devil's advocate position would be that the stress sensing mechanism the authors observe is just a secondary role for MTs in case of damage, etc. and that their orientation is primarily determined by other factors (i.e., geometry, genes, gradients, etc.). The authors should point to data to rule out this hypothesis, or an explicit statement that this position cannot be ruled out should be made.

[Editors' note: further clarifications were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled “Subcellular and supracellular mechanical stress prescribes cytoskeleton behavior in Arabidopsis cotyledon pavement cells” for further consideration at eLife.

Your revised article has been favorably evaluated by a Senior editor, Detlef Weigel, and two reviewers, one of whom is a member of the Board of Reviewing Editors. We appreciate the careful consideration of review comments and the new models included in the rebuttal letter. Some of the data provided only in the rebuttal letter we felt would be useful to the readers of the manuscript and so we ask you to make a few minor revisions before acceptance, as outlined below:

1) There is one point regarding the modeling that should be addressed more directly in the paper, and not just the rebuttal, and that is the choice of low turgor pressure (2 bar) in the models. This was used to explain why there wasn't more movement in the model after ablation, and why this level was necessitated by their model (if it is higher they get larger deformations and the models do not converge).

A more realistic model seems simply not to be possible with the technology available and our expert reviewer agrees that that a more realistic model would probably behave in a qualitatively similar way, and thus would not change their results. However, it is important for the reader to be aware why the low turgor choice was made, the difficulties in model convergence in such a system, and the issue with anticlinal walls. This information should be in the paper in either the main text or as supplemental material, not just in the rebuttal letter.

2) The experiments in which single cells were ablated (Author response image 6 and in revised text) and in which guard cell MTs were monitored after ablation (Author response image 7) were quite informative and the latter should also be included in the manuscript in either the main text or as supplemental material.
