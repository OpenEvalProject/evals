# Peer review - Round 1

Editors:
- Axel T Brunger, Stanford University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.08419.043](https://doi.org/10.7554/eLife.08419.043)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for submitting your work entitled "CryoEM and Computer Simulations Reveal a Novel Kinase Conformational Switch in Bacterial Chemotaxis Signaling" for peer review at eLife. Your submission has been evaluated by Michael Marletta (Senior editor), a Reviewing editor, and three reviewers. There are several major issues that need to be addressed before a final decision can be made.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

Summary:

The manuscript describes the use of subtomogram averaging to determine the structure of a reconstituted chemotactic signaling array at intermediate-resolution.

A complex has been assembled on lipid monolayers between (1) the cytoplasmic domain of Tar chemotaxis receptor, (2) CheA, and (3) CheW. A cryo-tomography density map of the resulting crystalline patches has been obtained, and sub-tomogram averaging has been used to an estimated resolution of the core-signalling unit around 1.3 nm. Flexible-fitting molecular dynamics has been used to dock known crystal structures of these components into the density map. This model and the molecular dynamics simulations suggest a new conformational switch.

Overall, this study defines the reconstituted arrays at an unprecedented resolution and thereby confirms key features of the assembly that have been proposed in the past, but not previously visualized – such as the CheW rings and the P3 and P4 domain positioning. These are important contributions to the understanding of the array structure. However, there are major concerns about the anisotropic character of the EM data and the possible impact on the accuracy of the model. Moreover, the reliability and uniqueness of the fit of the model to the EM data must be assessed in order to judge the quality of the model.

The all-atom MD simulations, which are impressive in their size and duration, suggest a provocative dynamical model of kinase regulation, although the accompanying biochemical data are not highly supportive of the "dipping" mechanism, and further control experiments should be performed. Moreover, it is not entirely clear how these conformational changes are to be interpreted in terms of CheA activation and whether there are other relevant changes.

Reviewer #1:

Essential revisions:

1) The elegant combination of an in vitro reconstitution together with sub-tomogram averaging and molecular modeling is very impressive, but this reviewer has two substantial technical concerns: the data has been obtained by performing tomography on a monolayer sample. All of the unit-cells are equivalently oriented relative to the electron beam and during tomography are tilted through a limited angular range. As is also the case in 2D electron-crystallography experiments, this results in a missing cone of information in the final structure. The resolution of the structure is therefore lower in Z than in X, Y. This situation cannot be avoided for a monolayer sample. This anisotropic resolution has multiple implications: it will lead to apparent smearing of the structure in Z; it will influence the ability to place the subunits into the map, and especially to determine their Z-position; it will affect the MDFF. The authors only quote a single resolution suggesting this effect may not be considered. What is the resolution in Z? Does this allow reliable positioning of the structural models in Z? How reliable is this positioning? How was the anisotropic resolution taken into account in MDFF?

2) Knowing how the available structures have been placed into the EM map, and with what confidence the positions are determined, is essential for assessing the reliability of the final model. It is not clear to me how reliable these positions are. For example, the authors state that the four-helix bundle of the CheA-P3 bundle is clearly discerned to run parallel to the receptor. How clearly? Judging from the available supplementary movie, there is some room for varying this position, as there is for the position of the P5 domain, in particular in the Z direction. What is currently missing is an assessment of how reliable the subunit models are and how accurately the EM map determines their position and arrangement. Are any alternative arrangements possible? With what confidence can this arrangement be selected? How accurately can the domain positions and orientations be determined using an EM map of this resolution and these structural subunit models? How accurate do these initial positions need to be to interpret details after MDFF? One can imagine that with a 30 Å resolution structure, subsequent MDFF would not give a structure reliable to side-chain resolution, while with a 5 Å structure it would – what about at the resolution in this manuscript? In the end the authors go on to determine specific amino acid interactions and conformational changes, so it is important to clearly justify/demonstrate that this level of interpretation is reliable and unique given the input data.

3) Example data should be deposited in the EMDB.

Reviewer #2:

Minor revisions:

1) Various CheA domains are first referred to in the subsection “3D density maps of CheA2-timer and CheA2-hexamer”. It would be helpful if there had been a sentence or two first to introduce the structure of CheA, identifying the domains P1 to P5.

2) The authors rightly point out that the model agrees with previous structural studies, and they go on to validate, in cells, the conformational change that they propose for CheA. This should all be balanced by some discussion of what might be added by further improving the resolution. While docking known structures into EM maps at a resolution of ~1.2 nm is generally accepted as giving useful biological information, it generally is not accepted as giving a definitive final structure.

Reviewer #3:

Essential revisions:

1) The authors should provide more detail with respect to the uniqueness of the P4 positioning in the density maps. This is an important issue because the EM data here alone determines the P4 position and it does not draw on crystal structures, such as most of the other interfaces. The conformation of P4 is also critical to the dynamics simulations that follow. The domain fitting was done reasonably, however; on viewing the density, one wonders if other positions are also nearly as compatible. For example, do the fits converge if different starting conformations are used? Could some metric be given with respect to the goodness of fit? Also on this point, it appears that the nucleotide-free form on the P4 domain was taken, both for the modeling and the dynamics. ATP binding substantially affects the conformation of a large loop on the P4 domain surface. Does ATP-bound P4 give a similar fit as the nucleotide-free form?

2) There is cryoEM data that suggests the P1 and P2 associate quite strongly with the kinase core in the inhibited state (Briegel et al. 2013). If these regions indeed contact P4, they could alter its positioning and dynamics. This point should be noted.

3) This reviewer is concerned that the significance of the R297 salt bridge to stabilizing the dipped conformation is overstated. In the simulations, is 4 versus 2 instances of dipping significant for 27 copies? Also, although 3 of the 4 dwell times for the dipped conformation are indeed longer in the wt, the other one is similar to that seen in the mutant. Is the principle component associated with this motion the only one that shows a difference in occurrence between the wt and mutant trajectories? A more thorough assessment of this data would bring more confidence to the dipping result.

4) The use of "asymmetry" might be misleading to differentiate the conformational states. The term certainly describes the dipped state, however; the asymmetry may simply be a consequence of this being a rare event. The reader gets the impression that there are two states: one symmetric and one asymmetric; however, a dipped symmetric state may also be possible, just unlikely to be seen in the same dimer under the simulation conditions.

5) Little information is given with respect to the PCA in the dynamics trajectories (and there is no mention of it in the Methods section). Also, for a general biological scientist, the significance of Figure 5C will be lost without a better description of what is being represented. It would be useful to know what percent of the eigenvalues are represented by the first component and how many vectors represent a majority of the total motion. Also, the authors focus on this one dipping transition; are there no other significant conformational changes? The arrays are of great interest in part due to their cooperative behavior; one might expect such simulations to reveal recoupling across core particles. There is also data that changes in the P5-receptor interfaces are associated with activation (Piasta et al. 2013). Are any such motions observed? This should be commented on.

6) The cross-linking data supports proximity of the CheA receptor residues, but it does not provide much support for the dipping motion. Control sites would have to be investigated and relative rates of cross-linking determined, ideally for multiple positions. For example, the R394 self cross-link seems to form as readily as CheA-receptor cross-links. R394 self cross-links are not surprising given the symmetry in the trimers-of-dimers, nonetheless, these sites are ~15 Å apart. Furthermore, it is not clear why the N405 self cross-links also do not form, given that these residues are closer to each other than are copies of R394. The statement near the end of the second paragraph of the subsection “Biochemical validation of CheA conformational change in E. coli cells” is not accurate, given that the yields of the 394 self cross-links are quite different in the two experiments. Normalizing to this band, there is not much change between the 394/361 and 394/316 pairs. Even if the cross-linking is less for 316/394, it could mean that those resides are simply further apart in a dominant conformation or show reactivity differences (e.g. 405 vs. 394). There is also the question of what state the cells are in during cross-linking. The attractant serine is present during the experiment, but depending on the timing of the washes, the cells are likely adapted. How much of CheA is activated and how much is inhibited in these experiments? For only a few sites, as investigated here, it would be more powerful to detect an attractant depend effect on relative cross-linking of the reporters. As it stands, the cross-linking data primarily supports the general architecture, but does not make the dipping mechanism more compelling.

7) The cell swimming assays need more description and from Figure 6 alone, it is not clear what parameter is being graphed. "Swimming ability" itself is a misnomer, as the cells can likely swim fine, but can't alternate tumbling properly to migrate in soft agar. This should be explained in the text or figure legend. Do all the mutants form attractant rings at the migration fronts indicative of chemotaxis? Or do some just show spreading, a consequence of some CheA activation, but no regulation (pseudotaxis). Photographs of the swarm plates for key mutants (or those that show differences should be provided as figure supplements). Furthermore, simply measuring the swarm radius does not distinguish a mechanistic defect from an assembly defect. Can an assessment be made (perhaps using the reconstitution system) if the mutants form arrays like wt?

8) In the subsection “3D density maps of CheA2-timer and CheA2-hexamer“, second paragraph, the electron density is less in the CheW/P5 contacts between neighboring core signaling particles than within the core complex, but this does not necessarily mean that the interfaces are weaker; they may instead be more structurally variable, and, hence, averaged out. Consider a change of wording. It is also difficult to see in Figure 3A and 3C that there is less density in the P5/W contacts between core particles. In Figure 3, color P5 and W differently, and demark the interfaces 1 and 2 that are being referred to in the text.

9) This reviewer appreciates that the authors are being cautious with the interpretation of their data, but the reader is largely left to summarize what the findings mean for CheA activation. The mechanistic take home message should be more explicit.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for submitting your work entitled "CryoEM and Computer Simulations Reveal a Novel Kinase Conformational Switch in Bacterial Chemotaxis Signaling" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Marletta as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission. The following comments need to be addressed before a final decision can be made.

Reviewer #1:

1) Anisotropic resolution of the map.

The authors present the angular distribution of the contributing subunits and argue that because is a good coverage of the tomography tilt range this concern can be disregarded. This is not a valid argument for two reasons. Firstly because the angular coverage is not good – high tilt angles are clearly underrepresented relative to low tilt angles, and this will cause a resolution anisotropy (it is not completeness of coverage, but uniformity of coverage that determines resolution anisotropy). Secondly, at high tilt the monolayer sample is much thicker and the projections have lower signal to noise. High and low tilts do not contribute equivalently to the final structure. This will also cause resolution anisotropy. I reiterate my initial concern – that the resolution of the structure is expected to be lower in Z than in X and Y. In the response to reviewers the authors show some isosurfaces with simulated wedges. It is not possible to sensibly assess the extent of anisotropic resolution from such images, and anyway, fitting is not based on isosurfaces, but on density. I am not persuaded that resolution anisotropy can be largely disregarded as the authors suggest.

This is not an unusual problem and it should not be difficult for the authors to address this issue better. They should be clear in the manuscript that there is resolution anisotropy and make an attempt to measure its extent (previous publications have used for example FSC within cones or 3DSSR to assess anisotropic resolution). The potential effect of this on fitting and MDFF should then be considered. Ideally, this would be taken into account during simulation, but the authors will probably consider this too much work. In that case they should write that this was not taken into account, and discuss what the potential influence might be on the reliability of domain positioning or on the simulations.

2) Reliability and uniqueness of fit.

This question was also asked by reviewer 3. How well does the EM density determine the position of the domains, in particular P4? From the authors response to reviewers it sounds like the position is not well defined, but that different positions still undergo dipping motions. I am still concerned that the orientation of P4 is not well defined by the EM map, that the starting orientation is critical to the MDFF analysis, and that this influences the interpretation of the dipping motion. The authors have access to the raw data and do not seem to be concerned by this. In that case they need to help the reader to assess the reliability of the model. Ideally by providing a metric for the goodness of fit, but minimally by an honest appraisal of the caveats, clearly and openly discussing the reliability of the fit, where alternative positions are possible, and how this might influence the interpretation. This should be in the main text of the manuscript.

Reviewer #2:

The revisions made in response to my comments are fully satisfactory.

Reviewer #3:

In their revised version of the manuscript, the authors have done a nice job of improving the paper and they have largely addressed my concerns. The one exception is the cross-linking studies. I still do not agree with the statement that "Taken together, our cross-linking experiments suggest that the CheA-P4 "dipped" conformation observed in silico is indeed sampled within the native chemosensory complex of E. coli." The inference here is that the cross-linking data supports the dipped conformation as a relevant state of the arrays. It may well be, but, the cross-linking data does not provide strong support for this supposition. Again, the only band to report on the dipped conformation (361/394) is quite weak, much weaker than the self 394-394 band. It's not uncommon to see some cross-linking between residues that are in proximity. In fact, I would be surprised if no cross-linking was observed, even if only the undipped conformation was represented. The authors can lean more on their mutagenesis data to support the dipped conformation, but I don't think the cross-linking makes the case.
