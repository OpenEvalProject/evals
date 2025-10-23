# Peer review - Round 1

Editors:
- Aleksandra M Walczak, École Normale Supérieure France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.60381.sa1](https://doi.org/10.7554/eLife.60381.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The manuscript combines an impressive array of experimental and modeling approaches to study cell morphological changes due to stiffness heterogeneities and contractility. The article is an interesting, well-written contribution to the field, with the discussion and conclusion well supported by the experimental data.

Decision letter after peer review:

Thank you for submitting your article "Condensation tendency of connected contractile tissue with planar isotropic actin network" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

This article reports the radial alignment of rat embryonic fibroblasts at the periphery of circular confinement patterns. It combines a large array of experimental and modeling approaches to study the origin of this phenomenon and find that contractility, adhesion and stiffness gradient are necessary to obtain this alignment.

Summary:

The authors study the effect of confinement on the alignment of REF cells confined within circular micropatterned islands. They observed that the cells are aligned perpendicularly to the boundary after 48h, contrary to other elongated cells such as NIH-3T3. After testing several subclones of that cell line, they identified cell contractility and cell-cell adhesion affect the organization of the cells in the circular patterns. They confirmed this finding using drugs that affect contractility and disrupt cell adhesion. Then they compared their results to a continuum model and to a Voronoi model.

Enthusiasm for the work is diminished by the limited experimental support for key assumptions of the conceptual and math models (e.g. existence of stiffness gradient, assumption of uniform contractility, use of calcium chelator to show importance of adhesion). Further, integration of model and experiment could be improved, and some of the narrower assumptions of the models (e.g. omitting cell proliferation, remodeling of cell-cell contacts, and cell-substrate interactions, assuming uniform contractility) need better justification. Also, a clear correlate to specific events in development, physiology, or disease would highlight the broader impact of the work beyond a very specific event in a carefully engineered system. Finally, 3 similar papers came out on arxiv from the Roux group. They should be discussed in the manuscript and cited.

Essential revisions:

1. Several assumptions underlying the models need substantiation.

a) The assumption of a purely elastic process: Figure 1A show a dramatic increase in the number of REF2c cells from 24 to 48 hours, suggesting that cells are proliferating. This, together with continuous remodeling of cell-cell contacts, would result in deformations that dissipate elastic energy. Neither modeling approach accounts for this. It would be important for authors incorporate these behaviors, or to provide evidence that cell proliferation and remodeling are unimportant, and similar between the three cell populations being compared.

b) The assumption that contractility is uniform: Work cited (Tambe et al) shows on the contrary that collective cell behaviors exhibit highly heterogeneous active stresses. Experimentally, there are a few potential ways to clarify this point. The authors could use the stiffer (1 MPa) micro post cultures, which recreate radial alignment seen on micropatterned PDMS islands, and compute force variations from post deflection. Alternatively, the authors could perform short time lapse experiments to measure deformations following treatment with blebbistatin or Y27632. Yet another option would be to perform staining for contractile proteins such as phospho-myosin light chain, GTP-bound RhoA, or others, to confirm they are uniformly distributed despite the heterogeneity of F-actin (although such experiments might not reveal uniform contractility when F-actin is nonuniform). Finally, if no experimental support is possible, then authors could turn to model simulations to test whether spatial heterogeneities in contractility alter the overall behavior of the system. In addition to either modeling or experimental support for the assumption that contractility is uniform, authors should provide examples from the literature on related systems that support this assumption.

c) The importance of a stiffness gradient in the cell population, which is one of the key aspects of this work: evidence for the existence of such a gradient is provided only by staining for F-actin, which is insufficient. While F-actin is indeed a key cytoskeletal component in defining the stiffness of cells, the link between intensity of staining and stiffness needs to be proven. Only a single reference is provided, which focused on one specific cancer cell line and the role of stress fibers in stiffening the cell. Moreover, given that F-actin interacts with nonmuscle myosin to form the key contractile machinery of most cell types, heterogeneity in F-actin likely implies heterogeneity in contractility as well. There are also concerns with the measurement of F-actin abundance, including need for statistics on the spatial distribution, and to normalize per cell to reflect variations in F-actin as opposed to simply variations in cell density, which are also present (Figure 1A). Finally, the F-actin gradient is only shown and quantified when intensities are summed over many samples. It would be important to demonstrate a significant gradient within individual samples, and how it varies across samples.

2. The importance of cell-cell adhesion is another crux of the story, pointing to differences underlying the various polarization phenotypes. However, the only experimental support for this is via treatment with a calcium chelator, EGTA. Only one reference is provided for this method (#35, Chen et al), yet Chen et al. appear not to have used EGTA at all, and instead disrupted E-Cadherin using neutralizing antibodies. This is a much more specific and direct approach that the authors of the present study should consider in place of EGTA. In the absence of this or similarly targeted approaches (RNAi, etc), author should include control experiments that demonstrate this rather broad perturbation does not alter contractility or cell-substrate interactions. This could be done at least in part, by using the traction force measurement system the authors have devised. It is particularly important to do so given the importance of calcium for cytoskeletal contraction via calmodulin. A second experiment authors could supplement this with is pharmacologic inhibition of calcium-depdendent contractility, with the hope/expectation that calmodulin-mediated contractility does not predominate this system. Even with these experiments, however, the authors need to provide support from published work that this method of disrupting cell-cell adhesion is well established.

3. The relationship between the in vitro system used by the authors and in vivo phenomena is weak. This is particularly true for the continuum model, where it is nontrivial to relate strain and stress to cell shape changes, given that cell shape is not simply an affine elastic deformation owing to stresses acting on it, but instead a response to stresses integrated with cell autonomous behaviors. There is a large body of literature on the alignment of cells relative to the direction of applied static or dynamic stretch. This mechano-responsivity that dictates cell shape is not considered in the present study. Even without considering these complicating cell behaviors, it is not clear how the magnitude of stress or strain relate to the change in cell shape. In addition, authors would ideally make use of the models to pinpoint what underlies the distinct polarization phenotypes between REF2c, REF11, and 3T3 cell types. The in vitro system should be used to measure directly the cell generated forces.

4. Some terms are either not properly defined or misused and the writing is sometimes unclear. What is the "condensation" process the authors are referring to and how this is related to the boundary alignment of the REF cells. It is the first word in the title of the manuscript, still it appears for the first time in the text only on page 18, where it is poorly defined. Please, read the work of Trepat et al. on active dewetting published in 2018. What do the authors mean by "tendency" (sometimes there is condensation, sometime there isn't?). A different wording to explain their results might be better. Furthermore, terms like nematic, or symmetry are misused.

5. There is a lot of data, analysis and model, but their presentation is not well organized, such that serious rewriting and re-organizing seems in order. The authors chose to show all the analysis they could do in the figures, and therefore there is no clear take-home message. Are all those plots necessary? What is the main result? We suggest to focus on the essential findings. Also, plot the 2 cells types in the same graph instead of showing one graph/cell type.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Condensation tendency and planar isotropic actin gradient induce radial alignment in confined monolayers" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Aleksandra Walczak as the Senior and Reviewing Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Please answer the Reviewers comments. They are mainly discussion points (you do not need to do new experiments), but please do so carefully.

Reviewer #1:

The authors were extremely responsive to reviewer critiques, including text changes, new experiments, and modeling simulation. There are some key places where concerns remain, and these should be addressed via text changes, explicitly describing limitations in the Discussion. Specifically:

1) The modeling of cell responses as purely elastic in the continuum model remains problematic. While new data indicates that cell alignment does not require proliferation, authors do not address the extent to which energy is dissipated via remodeling of cell-cell junctions. This is accounted for in the Voronoi model, as author's point out, but it's absence from the continuum model is a strong limitation that should be noted.

2) Most critically, there remains only indirect support for two key assumptions of the work. One that there is a stiffness gradient, inferred from actin staining, and the other that contractility is uniform and/or unimportant. Given that contraction is produced by interaction of myosin and actin, homogeneous myosin and graded actin can still produce heterogeneous contractile forces. The authors have performed some simulations to test a role for contractility but this is within a modeling framework built on the interpretation of authors, so to some extent you get out what you put in. It would have been ideal to see inhibitor experiments that block myosin activity along with model predictions of the resulting phenotype. I'm the absence of this, some concession on these assumptions needs to be articulated in the Discussion.

Reviewer #2:

This submission is a revised manuscript on the radial alignment of REF cells at the periphery of circular confinement patterns. The revisions are significant, and address the comments raised by the reviewers with a number of new experiments and analyses. I recommend publication in eLife.

Reviewer #3:

I'd like to thank the authors for their corrections. I think the manuscript has improved in clarity significantly. Still, some of the main comments remain unaddressed.

I am summarizing below the main concerns from the last round of reviews and whether they were addressed or not.

1. Justification of the model assumptions:

– Existence of stiffness gradient: ok (thanks to more citations);

– Calcium chelation: ok (thanks to more citations);

– No cell proliferation: ok (thanks to new experiments);

– Uniform contractility: NOT ok (not enough evidence, details below).

2. Integration of model and experiment: No changes.

3. Connection to development, physiology, or disease: No changes.

4. Discussion of the Roux papers: not ok.

I am now giving more details on some of the main points that were not adequately addressed:

1. Uniform contractility: The authors performed new immunostaining and new simulations. They showed that the density of myosin motors was uniform on most of the tissue, with a slight increase on the boundary cells. they then performed simulations to show that this slight increase of contractility at the edge does not lead to radial alignment. However, this is not enough experimental evidence to conclude that contractility is uniform. indeed, uniform myosin + non-uniform Factin does not necessarily mean uniform contractility as both proteins are required for contraction.

The authors show in simulations that an increase of contractility at the edge leads to smaller boundary cells. What would happen if contractility follows the actin gradient? Could that be enough to reproduce the radial alignment of the cells, even in the absence of cell contractility differential or condensation?

2. Integration of model and experiments. there is no quantitative comparison between theory and experiments. The simulation results are summarized in the new panel Figure 4B. Instead, why not showing the same radial profiles as for the experiments? It will make the comparison between experiments and theory easier.

It would be neat to see how sensitive the cell alignment is to rho, g and their gradients.

Along those lines, can the authors comment on how steep the stiffness gradient has to be in order to re-align the cells radially? Can this be quantitatively compared to the actin gradients measured in Figure S3-1? Not all the patches seem to display the gradient (see images in the 3rd column). Can the authors show if the steepness of the actin gradient correlates with the radial alignment of the cells or their size for each pattern instead of showing that the average gradient value and the average alignment are correlated?

3. Discussion of the 3 papers from Aurelien Roux's lab: The papers are cited in the bulk of the introduction, but not properly discussed. It seems to me that the transition from parallel to perpendicular anchoring is particularly important to mention in this manuscript. The authors claim in their response that they discussed the papers in the discussion. I could not find this section (none of the 3 papers are cited in the Discussion section). I think comparing and contrasting the results of those papers with this manuscript would greatly improve our understanding of how contractility and circular confinement impact the organization of dense layers of elongated cells.
