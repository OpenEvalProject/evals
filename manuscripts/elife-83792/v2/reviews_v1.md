# Peer review - Round 1

Editors:
- Stacey D Finley, https://ror.org/03taz7m60 University of Southern California United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83792.sa0](https://doi.org/10.7554/eLife.83792.sa0)

This important study presents predictions from a computational model demonstrating the impact of the extracellular matrix on collective cell migration in the neural crest. The evidence supporting the claims of the authors is solid, and the study is interesting to cell biologists exploring cell migration in different contexts.


---

# Peer review - Round 1

Editors:
- Stacey D Finley, https://ror.org/03taz7m60 University of Southern California United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83792.sa1](https://doi.org/10.7554/eLife.83792.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Dynamic fibronectin assembly and remodeling by leader neural crest cells prevents jamming in collective cell migration" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Jonathan Cooper as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Expand the model to include the ability of cells to switch phenotypes.

2) Include contact-induced repulsion.

Reviewer #1 (Recommendations for the authors):

The goal of this work is to investigate the mechanisms that mediate the collective migration of neural crest cells (NCCs). The authors first perform experimental studies to visualize and quantify NCC migration in chick embryos. Through knockdown or increased density of the extracellular matrix component fibronectin, the authors confirm the importance of this protein in promoting proper migration of NCCs. These data motivate the development of an agent-based model of NCC migration to quantitatively study factors that influence migration, including interactions between leader and follower cells, contact guidance, haptotaxis, secretion of fibronectin, and distribution of fibronectin in the extracellular matrix.

The experimental data are clearly presented and provide a strong basis for model development. Modeling and experiments are complementary, as the model enables a more in-depth analysis of the mechanisms driving NCC migration. The model itself is described well, including assumptions and parameters. Many modeling results are presented; though some data are left out, presumably to keep the paper focused. Some consideration of additional simulation results that can be presented to further support the conclusions is warranted.

The authors achieved the goal of delineating specific mechanisms that influence proper NCC migration. Impact on the field is likely modest; however, such predictive, mechanistic analyses are important to drive future experimental studies.

This is a well-written and interesting study. I am excited to see how experimental data motivates the development of a mechanistic ABM to explore mechanisms of cell migration. Both the data and model are clearly presented, and I applaud the authors for managing this, as it is no small feat.

I suggest some edits to refine and improve the paper.

1. Figure 2 and associated text: it is not clear how representative the two ABM realizations are. First, how many simulations were done here? Second, how many times does each realization occur? This is important to describe to provide some context for the simulation results.

2. In general, "data not shown" is present several times. This does not give the sense that the conclusions are justified. And in my opinion, some of the omitted data is critical to the study. For example, the orientation of the ECM fibers and statistics for the orientation of cells. The orientation of ECM fibers and cells are important aspects of migration; thus, results related to these points should be presented.

3. Leaving experimental testing of some model predictions somewhat reduces the impact of this paper. While it is not necessary to validate every model simulation, a careful examination of the most prominent conclusions would reveal the results that are important to test.

4. A description of the model limitations is missing. It is essential to state the limitations of the model to provide context for the readers and acknowledge the ways in which model assumptions may affect the results.

Reviewer #2 (Recommendations for the authors):

This theoretical work explores, by developing an agent-based model, the idea that remodelling of the extracellular matrix plays a role in collective cell migration.

Strengths:

Well-written theoretical paper that deals with the important problem of how groups of cells migrate collectively in a directional manner. The main hypothesis that extracellular matrix remodelling could play a role, not only in cell motility but, in collective cell migration is novel and the results are important, as it allows us to make predictions that could be eventually tested with future experiments. In addition, this theoretical paper is based on the migration of neural crest cells, a highly migratory cell population whose migratory behaviour has been likened to cancer invasion during metastasis. Thus, the conclusion of this paper could have implications for understanding different cells that migrate collectively, such as during embryo development, cancer invasion, or wound healing, to name a few.

Weakness:

As this is a theoretical paper, I would have considered it desirable that the authors move away from the restrictions of developing their model on a particular animal model, as they could be free of incorporating all the cellular principles discovered in a multitude of different animal models that have analysed neural crest migration (chick, zebrafish, Xenopus, etc). Unfortunately, the biological assumptions of the model are based only on the migration of chick neural crest, with particular emphasis on the biological findings of the experimentalist collaborator of this paper. For example, although the authors consider a cell-cell repulsion behaviour in their model, they claim that "chick cranial NCCs do not typically repel each other upon contact (Kulesa et al., 1998; Kulesa et al., 210 2004)", avoiding this behaviour in their simulations. However, a more recent paper has shown a typical cell-cell repulsion behaviour in chick neural crest (see: Li et al. (2019). in vivo Quantitative Imaging Provides Insights into Trunk Neural Crest Migration. Cell Rep. 26, 1489-1500), and this behaviour is widely documented in other species. So, instead of restricting their model to the questionable evidence that neural crest cells do not repel each other, why not make a more general model where cell repulsion could be another parameter to be explored?

An important aspect of the model is based on the clear distinction between leaders and trailing cells during neural crest collective migration. Again, this assumption in the model seems to ignore two excellent papers that unequivocally show that there are no fixed or distinct leader and trailing neural crest cells (Richardson et al., (2016). Cell Rep. 15, 2076-88; Alhashem et al. (2022). eLife. 11:e73550), which has been shown in chicken cephalic neural crest (Richardson et al., (2016). Cell Rep. 15, 2076-88) as well as in all other species in which high resolution of migrating neural crest has been performed. In all these species the leader and trailing cells are defined by their position within the cluster, and not by a predefined cellular state. So, leaders become leaders as soon as they reach the front of the cluster, while they become trailers when they lose this position. This more realistic dynamic behaviour of mesenchymal cells could be incorporated into their model, making it more general and not only restricted to situations in which leader and trailing cells are predefined. For example, they could make that each time a cell reaches the front position they start secreting fibronectin, and they stop it when they lose this position.

– Make the model more general, so that its assumptions are not based only on one animal model (or on the experiments of a particular group)

Reviewer #3 (Recommendations for the authors):

The authors use an agent-based (biological cells are modeled as computational agents) approach to explore the observed phenomenon of neural crest cell migration (NCC) in embryonic development, which is poorly understood mechanistically. Developing and implementing a 2 phenotype model off NCC population interacting with a remodelable extracellular matrix, they recapitulate many observed behaviors (specifically collective streaming of cells), finding, with compelling support, several key factors (contact guidance, etc) needed (and likewise not needed) to produce collective migration. Their modeling effort was greatly aided by in vivo experiments, detailed sensitivity analysis, and in silico experimental manipulation.

The authors' conclusions are well supported by their computational experiments as well as in vivo data and experiments. This is a well-communicated work that adds to the literature on modeling collective cell migration as well as introduces a new way to model ECM in an agent-based framework.

Strengths of this work include:

– Cross-disciplinary collaboration between computational and bench scientists.

– Selection of appropriate techniques to model phenomena of interest.

– Use of computational techniques to simulate knockdown, upregulation, and synthetic rescue of phenomena under study much of which also ties to either novel or previously published in vivo findings.

– Appropriate use of sensitivity analysis in stochastic simulations to support conclusions and guide computational experiments.

– Well-commented open-sourced software, enabling stochastic reproducibility of results as well as distribution of knowledge to the community.

– Publication of data in well-organized download, enabling community review of evidence.

The work cannot include everything and as such, the following items are not addressed in this work but may be relevant:

– As stated by the authors, there are several possibilities not excluded or explored by the presented simulations, including behavioral switching of cells or other possible methods of communication (such as a diffusing substrate).

– Likewise, as stated by the authors, not all findings supported by the modeling and simulations are currently supported by bench-side findings, leaving open the possibility that they may not be observed in in vivo studies.

– While addressed by the authors, citing the evidence that the planes of travel of these cells are narrow, 3-D simulations were not conducted. Noting that the authors discussed the jamming of cells and its impacts on invasion, developing 3-D simulations may yield different results in the context of cell jamming. It is something that could be explored, noting that having not included 3-D simulations does not take away from the conclusions in this work.

Lines 104-115 – The authors could consider (I truly mean consider) adding a late-breaking pre-print that is related to the authors' area of study to their already excellent literature review – https://www.biorxiv.org/content/10.1101/2022.11.21.514608v1. I mention it only because it is late breaking, attempting to enable the authors to include should they wish to.

Line 150 – The figure "title" does not match the majority of the area dedicated to the figure. Perhaps there could be two figures? Or a different title? "in vivo experiments and results"?

Line 152 – Developmental stage in the caption doesn't match the stage identified in Line 141. Should it?

Figure 2 and Caption (Lines 192-200)

Figure 2a and b: I found it difficult to distinguish between velocity vectors and fiber orientation vectors. Could a different color or symbol be considered to more easily distinguish them? Also, I am not seeing the additional puncta laid down by secretory cells. I have assumed that all puncta in the simulation are being visualized in the simulation stills but see only the original grid. Finally, I assume that the extra column of puncta on the right-hand side is just an artifact of visualization or something, but it may be appropriate to address why it is there. Of course, regardless it won't affect the simulations as the cells don't make it that far.

Caption – There appears to be a statistical test indicated in Figure 2C, but the caption does not identify it. The abbreviation "VE" appears in 2D but is not defined in the caption. I think it may not be defined in the manuscript at all, but of course, I may have missed it.

Figure 3 and Caption

VE isn't defined. If it's defined before, this should be fine – I point it out only in case for whatever reason the abbreviation changes in Figure 2, leaving Figure 3 as possibly the first time it's used.

Lines 469-473 – It's not clear which of these new experimental observations are from this work and which are from previous works. I may have misunderstood, but I think they are not all new in this work. Would the authors consider citing the other works here (no doubt there were previously cited but the reader may not recall all of this), enabling the reader to know which was added to this work? Or use some other indicator to identify their most recent findings being presented as a novel in this work?

Line 570 – I believe there may be a typo – I think the computational domain has an area of 250,000 um^2 (500 by 500).

Line 574 – If FN diffused or decayed at a shorter timescale than NCC migration, I feel like those phenomena would have to be accounted for. I may be misreading, but would it be that the FN processes are on a "longer" time scale than NCC migration, thus the FN can be considered unchanged during the 720 minutes of simulated time?

General comment on overview – I think it would be reasonable to highlight here how many agents become part of a simulation typically as well as the amount of simulated time to provide readers with an idea of those scales of the simulations. On a similar note, it would be reasonable to note a typical walltime as well as roughly what hardware was used to run the simulations, giving the community a chance to understand how long it might take to run similar simulations.

Table 1 – R_cell parameter – I didn't see a McLennan et al. 2020 in the citations. I may have missed it.

Reviewing the code, I see that there seem to be puncta agents in addition to the fibronectin field. How are the puncta agents used in the simulations? How do they interact with the non-diffusing substrate field? How, if at all, do their properties (their non-coding/PhysiCell-related properties) differ from the original puncta field?

In PhysiCell, there is a default value for the radius of interaction that determines where an agent looks for its neighbors. The default value is 30 um. Roughly, how did the authors address this as they did interaction testing over the longer than 30-um distances for interaction testing that would have occurred during the sensitivity analysis?

In the equations for the gradients (Del S_FN and Del S_cell), I see the motivation – cell center i is compared to all the puncta and cell centers in its vicinity. However, when viewing the expression under the summation, it seems like one would eventually calculate one single scalar, versus a field of scalars over which a gradient could be calculated. I certainly assume that I am not seeing the obvious, but could the authors please provide this reviewer with additional explanation for how or what the gradient is calculated over?
