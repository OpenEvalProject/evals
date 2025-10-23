# Peer review - Round 1

Editors:
- Johanna Ivaska, University of Turku , Finland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.11384.036](https://doi.org/10.7554/eLife.11384.036)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for submitting your work entitled "Heterogeneity in mesenchymal motility reflects adaptive switching between two distinct migration modes" for peer review at eLife. Your submission has been evaluated by Fiona Watt (Senior Editor) and three reviewers, one of whom, Johanna Ivaska, is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

Summary:

As you will see from the individual reviews included below, all the reviewers found that the paper is important and potentially suitable for publication in eLife as it describes fantastic analysis, with a level of detail and complexity that hasn't been attempted before. However, there was a consensus that the cell biological concepts put forward are somewhat overlapping with already published definitions regarding migration modes. Therefore, this article appears to be better suited to be published in eLife as a Tools and Resources article.

Essential revisions:

In case this would be something you would be happy with, please consider resubmitting the article formatted according to this category. This would mainly involve some re-writing to integrate your work better with the existing literature (please see the detailed comments below).

It would also benefit the cell motility field if you would be able to state explicitly how you think the discontinuous and continuous migration modes are related mechanistically to the other modes of carcinoma and fibroblast 2D and 3D migration. In addition, please consider possibly shortening the text in some parts (the Introduction for example is rather extensive), streamlining supplemental data and depositing the custom Matlab code appropriately.

Reviewer #1:

Much of the attention in the cell migration field has been in the mechanisms dictating the two main modes of cell migration, in particularly in 3D, namely amoeboid and mesenchymal migration modes. However, it is clear that not all mesenchymal cells migrate with the same morphological features. In this elegant, unbiased study Loch and co-workers describe two distinct modes on mesenchymal migration: continuous and discontinuous. The distinction is based on their high-though put microscopy and cutting edge image and statistical analyses of different migratory features. They define distinct features like cell adhesion number, localization and duration and their association with one of the two different migration modes. Furthermore, the dependency of the migration modes to perturbations of integrin activity, ECM ligand density and cell contractility are assessed in detail.

This is a carefully written manuscript putting forward an exciting new distinction of sub-modalities of mesenchymal migration.

Reviewer #2:

This manuscript characterises modes of migration on 2 dimensional surfaces which are relevant to mesenchymal cell motility. Using impressive multi-parametric analyses the authors determine interchangeable 'continuous' and 'discontinuous' migratory behaviours, which exhibit different requirements for specific features, for example continuous migration speed is closely correlated with cell matrix adhesion complex lifetime.

This study is elegantly designed and executed, and the characteristic properties of migrating mesenchymal cells are analysed in exquisite detail. Perturbation analysis is performed to analyse how specific properties might influence migratory mode. One major limitation of the study is the focus on a single cell line for the bulk of the analysis. Although other cells are more superficially investigated, in my opinion some extension is necessary to confirm the generalisability. For example, showing that manipulations can change the mode of migration in continuous-only (Hs578T) or discontinuous-only (Hep-3) cell lines would be particularly compelling.

My other concern with this manuscript in its current form is that it is not clear what has been determined that gives fresh insight and that it therefore may not constitute a significant advance of the highest novelty. This may be a harsh criticism, as it does constitute an excellent description of in depth analytical methodology.

Reviewer #3:

An important goal for the motility field is to understand how many different ways a single cell can migrate. This manuscript seeks to address this challenging question by using a combination of imaging and computational approaches to carefully characterize two types of mesenchymal cell migration defined here as continuous and discontinuous. Following a series of very careful comparisons of speed, persistence, protrusion dynamics, adhesion size, and F-actin intensity, for example, as well as comprehensive pairwise correlations between all of the parameters measured, they conclude that mesenchymal cells migrating on a two-dimensional tissue culture surface switch stochastically between distinct modes of migration (defined by an ensemble of cell-intrinsic parameters) in response to perturbations in cell-matrix adhesion and ROCK signaling, rather than using a continuous spectrum of migration mechanisms where each cell-intrinsic parameter can change independently. This conclusion is supported by the data presented and their discussion point that the presence of distinct migration mechanisms within population of cells need to be accounted for remains timely. It is difficult, however, to identify a clear conceptual advance resulting from this work or new information regarding the molecular mechanisms of cell movement.

Importantly, the authors have overlooked several recent papers where it was clearly shown that fibroblasts and other mesenchymal cells can use distinct migration mechanisms depending on the structure of the external environment, the degree of cell-matrix adhesion, as well as cell-intrinsic properties such as the level of RhoA/ROCK activity and actomyosin contractility (Liu et al, Cell, 2015, 160:659-672, Ruprecht et al, Cell, 2015, 160: 673-685, and Petrie et al, Science, 2014, 345:1062-1065). These publications each dilute the suggestion made by the authors here that it is unclear whether distinct sub-modalities of mesenchymal motility exist. Additionally, these papers and others (notably earlier publications from the labs of Peter Friedl, Erik Sahai, Ken Yamada, and Chris Marshall) clearly demonstrate the strong affect that matrix dimensionality has on the plasticity of cell migration mechanisms. How dimensionality could affect the migration of the cells used in this work is not addressed. Critically, the possibility that the continuous and discontinuous modes of migration characterized here only arise on an artificial tissue culture surfaces is not eliminated. It is also not clear why these cells need more than one mechanism to move.

Despite the lack of novelty in the conclusions of the work overall, the automated approach used to analyze cell motility is remarkable. This comprehensive and potentially unbiased approach has the clear potential to help identify new mechanisms of cell movement. For example, Figure 4C shows that the correlation between only a small subset of cell parameters changes significantly between the continuous and discontinuous modes. Identifying what those parameters are and if they actually caused the motility differences could be a way to leverage this data set to make new discoveries about the mechanisms regulating cell migration plasticity. Without this type of new mechanistic information I suggest the work might be more suited to be presented as a methods type paper.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Heterogeneity in mesenchymal motility reflects adaptive switching between two distinct migration modes" for further consideration at eLife. Your revised article has been favorably evaluated by Fiona Watt (Senior Editor) and the Reviewing Editor. The manuscript has been improved and modified to some extent but there are some remaining issues that need to be addressed before acceptance, as outlined below:

1) Novelty and main point of the paper: Although novelty is not highly important for the "Tool and Resources" category, the resubmitted title and Abstract both continue to emphasise the two modes of mesenchymal migration that are described and not on the automated and very complete analysis that they are able to perform. Very important is to highlight that the authors themselves accept in the Discussion that the existence of these two modes is not new and not even the co-existence of them. Please highlight more the quantitative information that you can extract and how this information can be correlated with responses to perturbation and the plasticity of cells to adapt to new conditions.

2) Repository of files: The manuscript mentions a "Cell adhesion and migration analysis toolbox" for Matlab with a detailed description of its functions and operation but it does not mention where is this placed. The rebuttal letter says that this "will be attached to the Data Dryad link" but still the location is not yet available. The scope of eLife and in particular of the "Tools and Resources" article type specifies that these articles should "highlight new experimental techniques, datasets, software tools and other resources" and also that "Tools and Resources articles should fully describe the biological material, data and methods so that prospective users have all the information needed to deploy them within their own work". At the moment the article does not fully describe the methods in the manuscript, maybe only in the detailed description coming with the Matlab toolbox but this is not accessible now. This needs to be revised.
