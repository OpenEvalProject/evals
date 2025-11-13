# Peer review - Round 1

Editors:
- Assaf Zaritsky, https://ror.org/05tkyf982 Ben-Gurion University of the Negev Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84749.sa0](https://doi.org/10.7554/eLife.84749.sa0)

This important study describes a new mode of collective cell migration during chick embryo development. Quantitative live imaging revealed compelling evidence that cells self-organized into a 3D dynamic meshwork structure while migrating from the epiblast to the endoderm during gastrulation and that this network is associated with N-cadherin-mediated cell-cell adhesion. Agent-based simulations propose that cell-cell adhesions are required for the formation of the meshwork structure and that the cell aspect ratio and cell density may also play a role in the meshwork formation. This manuscript would be of interest to developmental and cell biologists as well as theoreticians studying tissue patterning and collective cell migration.


---

# Peer review - Round 1

Editors:
- Assaf Zaritsky, https://ror.org/05tkyf982 Ben-Gurion University of the Negev Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84749.sa1](https://doi.org/10.7554/eLife.84749.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Migrating mesoderm cells self-organize into a dynamic meshwork structure during chick gastrulation" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Marianne Bronner as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Nicoletta Petridou (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

1) The authors argue that their agent-based model is used to investigate how the meshwork arises and how it contributes to cell movement. This is not supported by the data. The authors can tone down their claims throughout the manuscript, or provide further support as suggested by the reviewers. Specifically (not all suggestions must be followed, but claims must be supported by data):

a. Analyze how the network structure affects the collective migration of cells (Reviewer #2, point #1).

b. Verify the model prediction regarding the increased rate of mesoderm cells at the primitive streak with a current experimental framework (Reviewer #1).

c. Is the cell's aspect ratio an essential factor for network formation? Reviewer #2 proposes to perform simulations with higher attraction values. (Reviewer #2, point #6)

d. Milder perturbations (e.g., less concentration of N-cad-M so the cells do not lose adhesion completely) or the combination with complementary approaches (e.g., use of blebbistatin, ROCK inhibitor, etc) to understand the contribution of shape, cell-cell adhesion, and density to meshwork formation (Reviewer #3 – point #3)

2) Several clarifications and further quantitative support are required regarding the interpretation of the experimental data. Again, the authors can choose to remove unsupported claims or clarify and provide better support.

a. The argument that mutated cells are excluded from the meshwork is not supported by Figure 4C-D and should be properly quantified (Reviewer #1, Reviewer #2 – point #2).

b. Figure 4J should include the data of all five embryos and the statistical test should take them into consideration (Reviewer #2 – point #4). It is not clear what statistical tests are used throughout the manuscript (e.g., 3/5 embryos usually lead to a p-value > 0.08).

c. There is insufficient data to draw conclusions on the dynamics of the mutant-control cell-cell interactions, this can be resolved with more extensive analysis (Reviewer #2 – point #5).

d. The authors claim that mutated cells are more rounded. This should be quantified (Reviewer #1, Reviewer #2 – point #3)

3) Depleting the intracellular domain of N-cadherin can have effects on intracellular signaling that can lead to changes in cell migration and morphology (cell rounding, de-attachment) which is very much expected to affect the network structure. This is quite a harsh experiment to conclude how N-cadherin contributes to the meshwork, since many parameters change at the same time, and thus these experiments alone do offer much understanding of how the meshwork is formed and functions. In general, the manuscript would benefit a lot from more targeted experiments on either adhesion/shape (different N-cadherin mutants or combinations with other manipulations), and specifically, Reviewer #3 proposes a control experiment of overexpressing N-cad lacking the intracellular domain (Reviewer #3 – point #2). Another possibility is tuning down relevant claims and addressing these issues in the Discussion.

4) Experimental confirmation that the cells being labeled by electroporation (Figure 1) are indeed (mostly) mesodermal and that the meshwork structure is only present in the mesoderm (Figure 2). Reviewer #3 proposes immunostaining or HCR with a mesodermal marker (Reviewer #3 – point #1).

5) The description of the topological data analysis should be elaborated and self-contained. This point was raised by all reviewers. Specifically:

a. Persistent homology analysis: the technical terminology that is inconsistent with the context and very hard to follow. A minimal explanation of the terminology, namely of what is meant by birth-, death rates, and lifetimes, how/why they relate to particular structural properties, and how one should understand the persistence diagrams must be included briefly in the Results and extensively in the Methods section. As a recommendation, Reviewer #2 suggests translating the terminology to be consistent with the context of spatial data (instead of using quantities with temporal terminology).

b. Illustration and a better description of agent-based simulations. The authors should explain how they solved their equations and why they chose a particular potential energy and their set of parameters (Reviewer #2).

6) Regarding the theoretical model, it is not clear to me if the size ratio of hole vs. particles/agents is comparable to the ratio measured experimentally. It seems that in the microscopy images, there are clearly fewer cells surrounding one hole than agents around a hole in the model. A brief quantitative description/analysis would be beneficial to clarify this (Reviewer #3 – point #4).

Reviewer #1 (Recommendations for the authors):

Nakaya et al. investigate the cellular mechanisms underlying mesoderm cell migration in chick embryos. Through the use of live and fixed high-resolution imaging and so-called topological data analysis (TDA), they uncover the existence of a dynamic, cell-cell adhesion-dependent meshwork pattern in the mesoderm. By tracking wildtype vs. dominant negative N-cadherin expressing cells, they uncover a dependency of directed collective cell migration but not individual cell migration on cell-cell adhesions. Combining experimental observations with theoretical modeling, the authors demonstrate that elongated shape, attractive interaction, and specific cell densities can sufficiently explain the formation of dynamic meshworks during mesoderm formation.

The key findings in this work are compelling and the integration of theoretical modeling to ask questions that are not experimentally tractable is well-done, done, and well-integrated with experiments. While the author's claims and conclusions are largely justified by their data, a few key observations in the imaging data are described only anecdotally and could be better characterized. Clarifications of some of the methods and motivations would also strengthen the work.

The authors apply topological data analysis (TDA), which is an innovative approach to quantifying tissue topology and provides clear quantitative measures for holes within the meshwork. I appreciate the value of this approach and its application both to experimental and modeling data. However, the authors did not explain this method adequately, and visualization of the results could be improved for clarity.

The use of theoretical modeling and its juxtaposition to experimental data to explain the formation of the meshwork through adhesions, cell shape, and density alone is very strong and compelling, and the data align well with the theoretical model. Since there are numerical predictions that come out of the theoretical models, there are some potential opportunities for experimental measurements that are missed. In fact, while certain elements are quantified very well, some key elements of the model are demonstrated only anecdotal and glossed over – cell shape (shown in supplemental Figure 5 but should be shown earlier), exclusion of dom. Neg. cadherin cells from holes, and time of contact. It would have strengthened the work to better characterize these key observations.

The experiments and modeling of the change in the meshwork structure over time in Figure 6 are compelling. The model predicts an increased rate of appearance of mesoderm cells at the primitive streak. The authors have the opportunity to make an experimental observation of this using their current experimental framework.

Overall, the methods described in this work are likely to have a broad impact in the field of developmental biology in terms of quantitative analysis of imaging data, and a well-designed combination of modeling and experimental results. The biological insights of this work in terms of how the developing mesoderm migrates as a meshwork will likely also open the door for the discovery of such modes of collective migration in other developmental systems.

The use of the classic chick model is not adequately presented. The authors should elaborate in the introduction on the advantages and limitations of the chick model, and how this model has been used historically for such cell migration assays, and how it compares to other experimental models.

Figure 1 does not strongly contribute to the narrative- the anterior/middle/posterior aspect of the mesoderm is not mentioned again, and sometimes taken into consideration and sometimes ignored, even within figure 1. In this reviewer's view, All information in Figure 1 is already contained in Figure 4 in direct contrast to the dom. Neg. cadherin cells, illustrating the desired points much more clearly. Figure 1 panels are also out of order and not referenced in order in the main text, making reading confusing.

For all electroporation experiments- how do the authors know that they are observing mostly mesodermal cells? Are there markers the authors could use to demonstrate this?

Line 135: "The directionality of trajectories was smaller than unity"- what does that mean?

For PD diagrams- for clarity, could the authors create a threshold that indicates a hole and pseudocolor data points in that color?

The authors' claim that the length scale of collective migration is similar to the diameter of the hole is not substantiated.

Clearer control examples of N and p-cadherin endogenous stainings would be useful.

Figure 3: measurements i 3D are not very informative, but if the authors can measure the directionality of the meshwork and how it changes over time (all the inverse xy area for example), or come up with other measures that could indicate dynamics of the network, that would add value.

Last sentence of page 15: "Since the length scales of the polar order of the collective migration and the size of the holes of the meshwork are comparable, we speculate that the frequent rearrangement of the cell-cell contact is a reason why the collective order of the mesoderm cells decays in the long length scale." This reviewer did not follow the logic. If collective order was similar in cells that are near each other if they are constantly rearranging why would that explain this phenomenon?

Reviewer #2 (Recommendations for the authors):

The authors provide a detailed experimental and computational investigation of the collective migration of chick mesoderm cells during early gastrulation. Using live imaging and quantitative analysis they characterize the motility of individual cells as they migrate from the primitive streak. From measurements of individual cell directionality, MSD, and cell-speed autocorrelation function they conclude that individual cells migrate in a directed manner but their motion fluctuates in three dimensions and generally appears as a biased random walk. Quantifications of a motility order parameter and measurements of MSRD revealed that the motility of neighboring cells is correlated within a radius of a few tens of microns. Consistent with these findings they also discover that during cell migration a 3D meshwork is formed in between the epiblast and the endoderm. Using persistent homology analysis they characterize the meshwork structure and its dynamics. They find that the meshwork holes are tens of microns in size, consistent with the length scale found in the migration analysis. To investigate the role of cell-cell adhesion in this process they overexpressed an N-cadherin mutant in the mesoderm cells and analyzed cell motility and network formation. Mutated cells were less persistent, the tissue progression speed was lower and their directional coordination was weaker. They, therefore, conclude that cell-cell adhesion is important for the coordinated movement of the cells. To investigate how the meshwork is formed they developed agent-based stochastic simulations of rod-shaped cells interacting via short-range attraction and core repulsion. The simulations showed that meshwork structures form with strong inter-cell attraction and that a threshold cell aspect ratio is required to form the meshwork. In addition, for the networks to form, cell density needed to be sufficiently low since otherwise, they would fill the space with no holes, as they find in later stages of development. The work presented in this manuscript is comprehensive and interesting but I nevertheless have a few important comments.

Strengths: The work provides a detailed characterization of the individual and collective motility of mesoderm cells during gastrulation. The authors discover a novel structure that is formed in the process and present computer simulations that reproduce the structures formed and suggest key factors that may drive and influence their formation.

Weaknesses: Major one: The authors present their analysis of the network structure using persistent homology analysis and use technical terminology that is inconsistent with the context; they describe the structural properties of the meshwork in terms of birth-, death rates, and lifetimes. This makes it very hard to understand their findings. The authors should translate the expressions to the current context, namely use expressions that have concrete structural rather than temporal meaning, and explain in more detail how the points in the persistent diagrams relate to the structural properties of the network.

1. The authors should consider examining their network structure using more direct metrics as done in the analysis of fluid phase transitions in the references mentioned above.

2. The authors could use the simulations described in the section "Dynamic meshwork formation with the supply of agents" to also measure the motility characteristics of the cells in these simulations. This might shed light on how the network structure affects the collective motility of the cells.

Other comments:

1. Abstract line 30-31: The authors say: "To investigate how this meshwork arise and how it contributes to the cell movement we utilized an agent-based theoretical model …". While the authors could use their simulations to explicitly analyze how the network structure affects the collective migration of cells, in the current version of the manuscript this is not done.

2. Line 308 and caption of Figure 4: It isn't clear why the authors say that mutated cells are excluded from the meshwork. They do appear to line a hole. It isn't clear that the images in 4C and 4D shed light on the propensity of the mutated cells to form a network.

3. Line 309-311, 356-358, and 388: Based on 4C and 4D, the authors reach the conclusion that mutated cells are more rounded. This is hard to tell and needs to be quantified.

4. Line 330-334: The graph in 4J should include the data on the two embryos that did not show the effect on Phi(t) and only then the p-value needs to be calculated. It currently is not compelling that there is an effect on the polar order parameter.

5. Line 342-352: The few shown images in Figure 4 supplement 2 are insufficient to draw conclusions on the dynamics of the cell-cell interactions between the mutated and control cells; this requires more extensive analysis.

6. The simulations results appear to resemble a one-component spinodal decomposition of unstable fluids where condensation occurs globally throughout the system (for relevance in biological systems see reviews by Cats and Tailleur, Annu. Rev. Condens. Matter Phys. 2015. 6:219-44 and Joel Berry et al. 2018 Rep. Prog. Phys. 81 046601) It is driven by the attractive van der Waals interactions between particles and does not require them to be anisotropic; for a 2D simulation with Lennard- Jones potential see for instance, Koch et al., Phys Rev A, 1983. I.e., simpler simulations of round particles in attractive interaction (Lennard Jones potential) reveal similar structures in a so-called spinodal decomposition process. Moreover, in the experiments, the cells appear to be quite round. The aspect ratio is close to 1. It is therefore not clear that the rather small cells' aspect ratio is indeed an essential factor for network formation. The authors show in Figure 5C that for a specific choice of cell density and interaction strength, the aspect ratio is important for network formation. I suggest testing stronger attraction strengths (would it not phase separate?) and lower densities.

7. The description of the topological structure analysis in the methods section needs to be self-contained and not be based on the readers' knowledge of the original reference by Obayashi 2018. In addition, as mentioned above, the terminology should also be modified and adapted to the current context of the manuscript and more detailed explanations should be given on how to understand the persistence diagrams (which are a major tool used in the manuscript).

8. Theoretical model section: It would be useful if the authors included an illustration of how their agents and their interaction potential look like. They should add a few sentences explaining how Eq. 1 (and/or 8) was solved, and a few sentences motivating the choice of parameters and of the interaction potential.

Reviewer #3 (Recommendations for the authors):

In their manuscript, Nakaya et al. investigate the migration of mesoderm cells in the gastrulating chick embryo to understand how they coordinate as a collective despite the lack of tight confinement and lasting cell contacts. By means of confocal imaging and thorough quantitative analyses for cell tracking, they show that, while individual mesoderm cell motion displays some randomness, the cells move collectively toward the anterior-lateral or lateral direction. Moreover, the mesoderm forms a dynamic 3D meshwork structure, which the authors characterise applying persistent homology analysis. Immunostainings and a knockdown assay hint towards a role of N-cadherin-based cell adhesion in controlling collective cell migration and meshwork structure. Furthermore, Nakaya et al. develop an agent-based theoretical model to recapitulate the experimental observations and test additional parameters, such as cell-cell adhesion, cell elongation, and cell density. This model confirms the importance of adhesion for meshwork formation and supports cell shape and density as further parameters influencing it.

One major strength of this work is the detailed analysis of cellular motion, providing a compelling characterisation of mesoderm cell migration. Moreover, the theoretical model notably complements the experimental observations, while also adding to them. It provides further parameters influencing meshwork formation that could be tested experimentally in the future. Generally, the analysis methods employed in this manuscript constitute a good basis for future work on similar structures and processes. A point of improvement for this study is to understand the differential contribution of N-cadherin in cell adhesion, elongation, and density and through which of these parameters it influences meshwork formation.

All in all, the authors describe a novel mode of collective cell migration of the mesenchymal cells forming the chick mesoderm. This work also contributes to our understanding of cell migration in environments that are not physically restricted and highlights the importance of keeping tissue structure in mind when investigating cellular behaviour. In addition, the methods employed for analysis may be of interest to an audience beyond the field of developmental biology.

Here, I provide some suggestions for experiments that could contribute to strengthening the author's claims, as well as some considerations that in my opinion should be taken into account when coming to conclusions about the experiments:

1. Experiments to confirm that the cells being labelled by electroporation (Figure 1) are indeed (mostly) mesodermal, especially since the authors also suggest other cells may have been labelled, but do not quantify this ("there might have been a few endodermal and epiblast cells", p. 7). This could be done e.g. by immunostaining or HCR with a mesodermal marker. Similarly, in Figure 2, labelling of the epiblast/mesoderm/endoderm via immunostaining or HCR would show in a convincing way that the meshwork structure is only present in the mesoderm.

2. In Figure 4, the authors conclude that intercellular adhesion controls collective mesoderm cell migration based on the effects of overexpression of N-cad-M (lacking the extracellular domain). However, this experimental setup does not take into account that overexpressing the intracellular domain of N-cadherin can have effects on intracellular signalling. Changes in signalling could also account for changes in cell migration, instead of or in addition to the effect of cell adhesion and the associated outcomes of cell elongation. A control experiment would be to overexpress N-cad that lacks the intracellular domain instead and compare the effects between the two manipulations.

3. The theoretical model predicts that shape, cell-cell adhesion, and density contribute to meshwork formation. The authors test these predictions via the N-cad loss of function experiments, where cells naturally round up since they lose cell-cell adhesion to their neighbours. This experimental approach makes it hard to evaluate which of the model parameters are indeed physiologically relevant in vivo. I understand that finding experimental strategies that influence more than one parameter over the other is difficult, however more mild approaches (e.g. less concentration of N-cad-M so the cells do not lose adhesion completely) or the combination with complementary approaches (e.g. use of blebbistatin, ROCK inhibitor, etc) may help understand more the cellular basis of the meshwork formation.

4. Regarding the theoretical model, it is not clear to me if the size ratio of hole vs. particles/agents is comparable to the ratio measured experimentally. It seems that in the microscopy images, there are clearly fewer cells surrounding one hole than agents around a hole in the model. A brief quantitative description/analysis would be beneficial to clarify this.

5. An additional point regarding the theoretical model is if the emergence of the nematic order is also observed in the experimental data, and how this is disrupted in N-cad loss of function.

6. Overall, the manuscript is clearly written, with only some minor typos ("chamotaxis" in Table S6, "transvers" in Figure 2 S1A). Additionally, the sentence "… five embryos, each of which contains a lot of cells" (p. 18) could be rephrased to be more specific regarding the approximate number of cells.

7. The figures are clear and well-structured, with some sketches greatly contributing to the understanding of the experimental setups and imaging regions. However, in some cases, displaying the fluorescent images in different colours could make them clearer (e.g. green and cyan together do not provide much contrast; green and red in the same image is not accessible to people with red-green colour blindness, as in Figure 3, Figure 3 S1, Figure 4, Figure 4 S2). Additionally, in Figure 1C it may be helpful to clarify that the dot marks the initial position of the cells (as is done in Figure 4E). In Figure 4, Figure 4 S1 and S2, as well as in the main text, more consistency in the naming of the mutant N-cadherin construct would add cohesion to the work ("N-Cad M", "Ncad DN", "N-cad mutant", "N-cad-M", "N-Cad-M").

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Migrating mesoderm cells self-organize into a dynamic meshwork structure during chick gastrulation" for further consideration by eLife. Your revised article has been evaluated by Marianne Bronner (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, namely toning down claims that are not fully supported by the data (or providing the data to support these claims). Please refer carefully and fully to the comments by reviewers 2 and 3.

Reviewer #1 (Recommendations for the authors):

The authors have addressed all concerns to this reviewer's satisfaction. This reviewer has no further suggestions.

Reviewer #2 (Recommendations for the authors):

The authors adequately responded to all my major comments. Nevertheless, with one point I think the authors need to tone done their conclusion. Although with their theoretical model the authors did not observe network formation with round cells, this does not yet mean that cell elongation is an essential factor for network formation in the experimental system. Indeed, as mentioned in my previous report, the network structures found in their experiments resemble the patterns formed with unstable fluids undergoing a one-component spinodal decomposition. This process is driven by the attractive van der Waals interactions between particles and does not require them to be anisotropic in shape. See references in my previous report. This implies that network formation of the type that the authors find could indeed form with interacting round cells under appropriate conditions.

Reviewer #3 (Recommendations for the authors):

The authors have not addressed most of the essential revisions asked.

Even if some of the experiments did not work, it is recommended that the authors provide those data for the reviewers to be able to access the results. If this is not possible, the abstract should substantially change, because the necessary data to fully support the conclusions are missing.

Some examples:

(1) Confirm that the cells being labelled by electroporation are mesodermal cells. The new figures make it easier to understand but there is no quantification and if the authors conclude that is not possible to know if these are mesodermal cells, then they cannot fully support their conclusion that this is a mechanism of mesoderm-specific cell migration.

(2) N-cadherin manipulations / rhok inhibitors. Since no other alternative experiments were possible by the authors, the conclusions should change. Especially in the abstract and not only briefly in the discussion
