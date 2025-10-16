# Peer review - Round 1

Editors:
- Jalees Rehman, https://ror.org/02mpq6x41 University of Illinois at Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80900.sa0](https://doi.org/10.7554/eLife.80900.sa0)

The manuscript by Godoy and colleagues is an important contribution to the understanding of how lung endothelial regeneration progresses following endothelial ablation. The novelty and elegance of this study are rooted in the regional and specific ablation of lung endothelial cells using diphtheria toxin without the massive inflammatory activation that is seen with lung injury induced by bacterial infections, viral infections, or lipopolysaccharide. The data convincingly demonstrate that there is an emergence of a highly proliferative lung endothelial subpopulation with specific molecular signatures that facilitate regeneration.


---

# Peer review - Round 1

Editors:
- Jalees Rehman, https://ror.org/02mpq6x41 University of Illinois at Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80900.sa1](https://doi.org/10.7554/eLife.80900.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Single Cell Transcriptomic Atlas of Lung Microvascular Regeneration after Targeted Endothelial Cell Ablation" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Jalees Rehman as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Paul Noble as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Vinicio de Jesus Perez (Reviewer #2); Wolfgang M. Kuebler (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Compare scRNA-seq on lung ECs with other recent lung injury endothelial scRNA-seq datasets to identify commonalities and differences in the signatures of clusters related to injury and proliferation responses.

2) Analyze the scRNA-seq changes in non-endothelial cells and identify potential cell-cell interactions between endothelial and non-endothelial cells

3) Perform a more in-depth analysis of changes in endothelial cell states using trajectory building and RNA velocity analyses as well as infer potential transcription factors driving the changes to assess whether there are additional factors beyond FoxM1 that are activated in the proliferative cluster

4) Characterize the apelin signaling pathway and its role in driving the shift of endothelial cells to stem-like states

5) Define the stem-like endothelial cells by isolation or in vitro induction, as well as the cues that result in their formation after the loss of adjacent endothelial cells post DT – is it the apoptosis of neighboring endothelial cells or is it the lack of signaling input from neighbors such as junctional cues, or a different mechanism.

Reviewer #1 (Recommendations for the authors):

The study could be strengthened by addressing the following points:

1. Clarify the "stem-like" nature of the cells. Is Procr just a marker of the stem-like cells endothelial cells or is it involved in the stem-like nature. "stem-like" really refers to multipotency – can these cells become non-endothelial cells? Or are they merely progenitors of endothelial cells and can only mature into endothelial cells? Providing experimental evidence for the "stem-like" nature by performing differentiation assays or replacing "stem-like" with a more appropriate term may be helpful.

2. Mechanistic studies: Apelin and Procr are repeatedly mentioned as two key markers of the new transition process that the endothelial cells undergo but the studies remain mostly descriptive except for the apelin inhibitor study which only measures mortality but does not track actual endothelial regeneration. Overexpression of apelin or Procr in vivo using lung endothelial-specific gene delivery (or shRNA delivery to block) and measurement of lung EC regeneration would help define their mechanistic roles. Alternatively, one could consider ex vivo studies on lung ECs to demonstrate potential mechanistic roles for the gCap transition process.

3. Bioinformatic analysis of ECs: One key claim is the transition of gCap ECs into the proliferative EC subpopulation. How does this observation relate to the emergence of proliferative lung EC populations following lung injury described by others in the field? Can one model the trajectory of the transient "stem-like" and proliferative EC populations using Monocle3 or other trajectory-building algorithms?

4. FoxM1: An unbiased analysis of the potential transcription factors involved in cell transition and proliferation activation would be helpful. This could be performed by algorithms that infer transcription factor activities in single-cell data (so that one does not have to rely on mRNA levels of transcription factors). it would be very compelling if FoxM1 was one of the top inferred transcription factors by such an unbiased analysis.

5. Non-endothelial cells: The authors have very valuable non-endothelial single-cell data which shows changes in cell numbers but there is no analysis of the transcriptome change in those cells. if the authors can show how endothelial ablation itself affects the gene expression in alveolar macs, epithelial cells, and other immune cells, then it would have broad implications for our understanding of how endothelial cells regulate lung homeostasis.

Reviewer #2 (Recommendations for the authors):

The manuscript titled "Single Cell Transcriptomic Atlas of Lung Microvascular Regeneration after Targeted Endothelial Cell Ablation" by Soares Godoy et al. underlines the importance of single-cell RNA seq in the discovery of mechanisms in lung microvascular repair. Overall, the study is well-designed, and the experiments are concise and relevant. However, there are certain areas where further explanation is required to greatly improve the quality of the manuscript and make it suitable for publication.

1. One of the major points referenced in the introduction is the role of ALI/ARDS in Sars-Cov-2 infection. I wonder if it would be possible to compare the datasets obtained from the DT-mouse study and the recently published scRNA-seq analysis of COVID lungs (doi.org/10.1038/s41586-021-03569-1) to identify whether there are similar cellular/genetic/molecular changes. This will greatly strengthen the implications of this animal study's findings and help mitigate the weaknesses associated with the model.

2. Could the authors obtain access to lung tissue from ALI/ARDS patients (+/- COVID) and stain for aCap/gCap and apelin molecules? It would be interesting to see whether these cell types exhibit patterns similar to animal ones.

3. The scRNA-seq dataset is incredibly rich and will be a major resource for the community. While the focus is understandably on ECs, I think attention should be given to cell-cell interactions across the lung. Could the authors carry out ligand-receptor analysis to further emphasize how other cell types react to the injury? Please see doi.org/10.1038/s41576-020-00292-x for details regarding the methodology that can be used to carry out this analysis.

Reviewer #3 (Recommendations for the authors):

1. The authors propose apelin-apelin-receptor signaling between "stem-like cells" (Cluster 1, zone 2) and "progenitor-like cells" (cluster 1, zone 3, and cluster 7) as a driver of endothelial regeneration, yet these cells seem to exist at different time points (in fact, the authors propose that the latter emerge from the former). So, how can cell A signal to cell B if at the same time cell A already transitions into cell B by way of this signaling?

2. For cluster 1, I am surprised that the authors did not use RNA velocity analyses to validate the time-dependent transition of cells across the different zones in this cluster. Such analyses would clearly strengthen the conclusion that this is a single cell type that is undergoing different cell states during this process.

3. What is the signal that activates these "stem-like cells" and makes them transition from basal gCap into cluster 1, zone 2 cells? Is it the apoptosis of adjacent endothelial cells, or the concomitant inflammation? While it may be difficult to answer this question, some discussion may be warranted as identification of such a signal would allow replicating – e.g., for in-depth studies but also for therapeutic purposes as suggested by the authors – this transition in vitro.

4. The mortality data comparing young vs. old mice and the effects of the apelin receptor antibody are interesting, but more insight at the cellular level would help to further validate (or refute) the proposed concept. Specifically, one may ask whether age or apelin receptor inhibition can prevent the formation of Cluster 1 zone 3 cells at Day 5 post-DT? I realize that, unfortunately, such an experiment is prevented by the fact that most of these mice die on day 4, and the residual mice may present a survival bias. But how do the authors reconcile the fact that these mice die at D4, while the actual apelin-receptor positive population (cluster 1 zone 3) which supposedly is targeted by the apelin receptor antibody only emerges on D5?

5. In Figure 1C, it would be helpful to show that the apoptotic cells are indeed endothelial cells by counterstaining with CD144, CD31, etc. rather than DAPI alone.

6. In their section on Speculations and Ideas, the authors propose isolating stem-like and progenitor-type gCap cells at different time points after DT treatment. Indeed, such isolation would go a long way to validate the proposed non-proliferative nature of the former vs. the high-proliferative nature of the letter by actual functional assays rather than transcriptomic profiles alone. This opportunity should at least be discussed.
