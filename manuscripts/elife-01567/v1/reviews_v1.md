# Peer review - Round 1

Editors:
- Jan Traas, Ecole normale supérieure de Lyon , France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.01567.016](https://doi.org/10.7554/eLife.01567.016)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Automated quantitative histology reveals vascular morphodynamics during Arabidopsis hypocotyl secondary growth” for consideration at eLife. Your article has been favorably evaluated by a Senior editor, Detlef Weigel, and 3 reviewers, one of whom served as the guest Reviewing editor for this article.

All three reviewers agree that this study describes a robust tool that represents a broadly useful addition to existing methods.

Nevertheless a number of issues have been identified that need to be addressed before the article is acceptable for publication:

1) While the method is well adapted to the biological system analysed here, it would be important to have an idea of the applicability to other organs and/or species. Would, for example, the pipeline function as well in the case of cambium formation in poplar or root cell differentiation in maize? Since this article is mainly technically oriented and the data presented here only provide limited further biological insight, it will be important to underline and fully explain the methodological significance of the work described here. While this does not necessarily imply that extra experiments are required, it should be made clear what the wider applications are. This would largely compensate for the lack of clear conclusions on the biological system.

2) The cell type detection has an accuracy of 88%, which seems relatively low. The key criteria used by the classifier to distinguish between the cell types are not very clear. If for example the main observable used to make the distinction between the cell types turns out to be cell size, then having a 12% miss-classification could have quite some effect on the conclusions drawn in the paper.

3) Two remarks concern the PCA analysis:

- One of the reviewers performed a PCA on the data from Table 2 (using R software ade4 package) and could not reproduce the results presented in Figure 3. The authors should clarify what data they used for this PCA. If the PCA was indeed done on Table 2B, they should double check this part of their analysis. The reviewer suggested also to include intermediate steps of the PCA (correlation matrix, eigenvectors) as supplementary material.

- There is no discussion in the paper as to how the different observables contribute to the first principle component, which represents almost 94% of the variation. What is actually explaining almost all of this variation? Such a discussion would make it much more insightful what is actually changing over time and what makes Col-0 different from Ler.

4) In the part on “Visualization of vascular morphodynamics through combined plots of cell size and incline angle” there seems to be an issue with the incline angle: what happens when a cell is round? One would expect a highly randomized distribution of incline angles in that case. Please indicate how this problem was addressed.

5) Several points concern the more biological implications of the work described:

- The paper contains a long description regarding the differences between the two genetic backgrounds in terms of total cross-sectional area, size variations and so forth, but no context is given how this information can be useful for understanding Arabidopsis development.

- In principle it should be possible to derive the relative contribution of cell expansion and cell proliferation from the data (see for example the Supporting Online Material of Bosveld et al., Science 2012). This would show how without having the availability of explicit time series, the cell dynamics underlying secondary growth can still be derived through statistical measures. Although such an analysis might be beyond the scope of this paper, it would help the paper to go beyond methodology.

- In general, the papers suffers from giving many precise measurements without inserting them in a proper context, such that it becomes unclear why these specifics are insightful and important for understanding plant development.

You might try to be clearer about these biological implications in both the Results and the Discussion.
