# Peer review - Round 1

Editors:
- Ewa Paluch, University College London , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.03282.022](https://doi.org/10.7554/eLife.03282.022)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Mechanical stress homeostasis in active epithelial cell clusters by dynamic cell-cell force transduction” for consideration at eLife. Your article has been favorably evaluated by Tony Hunter (Senior Editor), a Reviewing editor, and 3 reviewers.

The Reviewing editor and the reviewers discussed their comments before we reached this decision, and the Reviewing Editor has assembled the following comments to help you prepare a revised submission.

The reviewers all agree that the new method presented is cutting edge, timely and important. The method uses the principle of force balance to estimate cell-cell forces from cell-matrix forces and combines it with a thin plate modeling approach to extract a spatially resolved map of cell-cell forces in epithelial monolayers. This allows 1) sub cellular measurements at a higher resolution than could previously be achieved, and 2) spatially-resolved dynamic measurements for small clusters of any topology. The method is first validated for “tree-like” clusters, in which case it can be compared to the already established force imbalance method. The method is then applied to the generic case of “loop” clusters, in which case this is the only method that up to now can give results. An interesting variant of this experiment is the use of “mosaic clusters”, where a molecular player of monolayer mechanics is depleted in a subset of cells within the cluster.

The general comment from all reviewers is that this is primarily a methodological paper. The biological applications presented do not provide real mechanistic insight and are proof-of-principle investigations showing that the method can be useful to address important biological questions. eLife is interested in publishing cutting-edge methods papers; therefore we would like to encourage the submission of a revised version. However, the reviewers found that for the method to be useful and of interest to a broad community, the presentation needs to be substantially revised and the assumptions and limitations of the method clearly discussed. We would also like to encourage you to make the code allowing the implementation of the method available to the public.

Specifically, two main points need to be addressed:

1) Presentation of the method and its limitations:

A key assumption is that the cell monolayer behaves like a thin elastic sheet with only two elastic moduli (linear and isotropic elasticity). In classical monolayer stress microscopy, this might be a better assumption because in this case large sheets of cells are observed without cellular resolution. Here however, the authors focus on small clusters of cells where cell contractility, stiffness, ECM adhesion, etc., vary from cell to cell, as it is also evident from the supplementary movies. In the Materials and Methods section, the authors suggest that this assumption might not be as severe as one might think; eventually the method reconstructs (cell-cell) forces from (cell-matrix) forces, thus the details of the material model might somehow drop out because they are used twice, once in the forward and once in the backward direction. However, this is a rather vague argument, could it be backed up by more explicit theoretical considerations?

Also, two of the experiments presented, cell division and mosaic clusters, definitely describe a very heterogeneous situation. In the movie showing a cell division event, it is clear that the dividing cell even partially detaches from the cluster (a large gap between the membranes can be observed). Thus there are intermittent new external boundaries, which are not taken into account in the analysis. Could the authors comment on this?

Another strong assumption is that there is no dissipation of forces by cortical elements, due to shear forces for example. Could the authors discuss this assumption?

Limitations: it is clearly the only method currently allowing one to estimate forces in four-cell cluster in “loop” configuration. But how reliable would the estimation be in a ten-cell or hundred-cell group?

One of the strongest advantages of the method presented is that it makes subcellular measurements possible. However, the resolution (10 um) is not very high. The authors suggest that this length scale could be a cellular feature and “not necessarily a resolution limit of the FEM analysis”. Would the method allow for measurements with a higher resolutions for epithelia with shorter junctions than these displayed by the MCF cells used here?

Reviewer #2 provided a detailed list of points that would make the presentation of the method more accessible. These points are listed in the minor comments pasted below.

2) Implications and limitations of the experiments presented:

The authors observe that intercellular forces are relaxed around mitotic cells although the total intercellular force in the cluster is kept constant, suggesting that the local relaxation is compensated by intercellular force increase between neighboring cells. This leads the authors to propose that such stress homeostasis might be the ”basis of mechanical integrity in a proliferating and deforming epithelium“. However, the conclusions are based on a single example with two dividing cells; the experiment does not appear strong enough to justify such strong conclusions. Could the authors either expand the experimental investigation of force homeostasis or tone down the conclusions? Could they also discuss what kind of mechanisms could lead to the proposed stress homeostasis?

One of the most striking findings of the paper is that intercellular forces are transmitted along cluster peripheral cell on a stiff substrate (on which traction forces are high), and through the center of the cluster on a soft substrate (on which traction forces are low). Why are cells and stress not shown here? Here again, could the authors discuss a potential mechanistic basis for this behavior?

It is not clear what the advantage of studying E-cadherin dynamics in such large clusters is. The method provides a relatively rough estimate of the force (14% precision as documented by the authors in a four-cell case, but probably less in larger clusters) whereas the correlation between force and E-cadherin concentration is a highly debated issue that requires exact force measurement. To be fully convincing, the positive correlation between force and E-cadherin and the increased correlation in growing and shrinking junctions, should be confirmed in cell doublets or linear triplets with exact intercellular force measurements. The time correlations displayed in Figure 7 are particularly inconclusive. Could the authors either substantiate these findings with more convincing experiments or remove these experiments? It does not seem correct to discuss a trend that is not substantiated by statistics (particularly compared to the statistics of the other experiments presented in the paper).

Furthermore, the movies show strong protrusive activity, with contacts between cells in the plane of imaging, in contrast with the 'standard' geometry of adherens junctions. Yet, the determination of cell-cell transmission uses in plane traction force measurements and assumes traction forces perpendicular to the interface.

The observed correlation between changes in E-cadherin intensity and stresses might reflect this stronger protrusive activity. How do the authors cope with this?

Minor comments:

The title does not seem to reflect the message of the paper; it suggests that the paper is about stress homeostasis, which is only one of the applications presented and which is not investigated in detail. We would suggest modifying the title to make clear that this is primarily a methods paper.

Could the authors provide details on how the force extraction is exactly done? What is the code used? What are the required inputs? Can the calculation be performed with a normal computer and how long does it take?

Reviewer #1:

The magnitude of the total intercellular force per cell depends on the numbers of neighboring cells, whereas the magnitude of the traction force on the ECM does not. Why are cells and stress not shown here? How reliable are cell-cell force measurements by FEM in clusters containing more than 20 cells?

Reviewer #2:

This manuscript is written in a very technical manner and the methods part at the beginning of the Results section but also later parts of the Results section are not easy to follow. Figure 1 is over-crowded, it is not clear to me why the mathematical equations and the references are required here. In order to demonstrate the way the method works, it seems more helpful to proceed to Figure 3 and to place Figure 2 later or in the supplement. The quantities analyzed in Figure 2 are not defined well and it is not clear how the numbers for N and n correspond to each other. In Figure 3 it should be explained why the sign inverted traction forces are shown. I also note that the network representation is rather dense and maybe even redundant, because the connectivity information on the edges can also be read off from the nodes (I understand that this information is used later to analyze force distribution and I do not mind leaving it in if the authors find this essential, but it shows again that the presentation is very crowded). What seems to be missing from this representation, though, seems to be information if a given node has resulted from a cell division. In Figure 4, the authors use a very special definition of strain energy (using only the displacement resulting from a single cell) without discussing alternatives or limitations. Regarding the length scale analysed in Figure 6, I wonder if the authors effectively extract the persistence length of the cell-cell contour; the explanations of the meaning of these length scales are rather hard to follow. In general, the authors should rethink how to make the presentation of their results more accessible to the general reader. I also note that Title and Abstract might be further sharpened. The used of the word “active” is not clear on first reading.

Although some details of the model are explained in large detail, the core of the method, namely the FEM-work, is not described in sufficient detail in the Materials and methods. Is the method implemented in the MATLAB PDE toolbox an optimization technique and if so, with which target function? What is the difference to the approach in monolayer stress microscopy, where one integrates the partial derivatives? Another issue is the use of an exponentially decaying Young's modulus between tight cluster mask and footprint boundary. Why is this complicated ad hoc procedure necessary? Can it happen that the Young's modulus has already decayed to a very small value at the cero stress boundary of the footprint and would this not lead to artifacts?

Regarding the cell-matrix force reconstruction, the authors use standard approaches and there is no real concern here, except that the method used (regularized FTTC) should be mentioned in the main text (at least when showing the traction maps in Figure 3, which obviously use a cubic lattice) and that a number should be given for the spatial resolution (actually the bead density seems to be quite low). What is the maximal bead displacement used in these experiments? How could the spatial resolution be improved in the future (leading to a smaller footprint region and to better results regarding the adhesions)? Such a discussion is important to understand the limitations of this approach and would also be helpful to understand the complicated procedure used to extract the sub-cellular length scale.

Why do global patterns of force distribution arise when at the same time the authors argue that force transmission is locally scrambled by cell-matrix contacts and actomyosin contractility? In fact these results seem to be contradictory, because stress localization to the rim is exactly what one expects from thin plate theory with long-ranged forces; because the authors use this assumption in their method, it is not clear how consistent their conclusions are in regard to the method used.
