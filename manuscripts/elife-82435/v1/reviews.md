# Peer review - Round 1

Editors:
- Pierre Sens, https://ror.org/02feahw73 Institut Curie, CNRS UMR168 France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82435.sa0](https://doi.org/10.7554/eLife.82435.sa0)

In this work, Monfared et al. construct a valuable three-dimensional phase-field model for cell monolayers and use this to investigate the relationship between single-cell extrusion events and topological defects in cellular arrangement. The extension of existing 2D phase field models to three dimensions is an important contribution of this paper, which will be of general interest to the theoretical modelling of epithelial monolayers. Here the model is used to study the importance of cell-cell and cell-substrate interaction in extrusion from cell monolayers, which will be of practical interest to biologists and physicists working on this process. This paper presents convincing evidence that extrusion events are distinctly linked to defects in nematic and hexatic orders in the cell monolayer.


---

# Peer review - Round 1

Editors:
- Pierre Sens, https://ror.org/02feahw73 Institut Curie, CNRS UMR168 France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.82435.sa1](https://doi.org/10.7554/eLife.82435.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Mechanical Basis and Topological Routes to Cell Elimination" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jonathan Cooper as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers found that the 3D phase field model you developed is a very valuable improvement over existing 2D models, but that your claims of how extrusion is linked to topological parameters was insufficiently justified.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Substantiate the claim that the three-dimensional phase field model is crucial for understanding cell extrusion as compared to 2D models. This should include in depth analysis of necessarily 3D parameters, such as basal and apical cell surfaces.

2) Provide a better statistics of the topological parameters and their fluctuations in normal (non extruding) cells to better assess their change during extrusion.

3) Improve the characterisation of the extrusion points, e.g. by improving the representation and discussion of the stress (Figure 4).

4) Provide a point-by-point answer to the criticism of all three reviewers and appropriately amend the paper.

Reviewer #1 (Recommendations for the authors):

1. The authors say "The similarities between cellular systems and liquid crystals featuring both nematic order (Saw et al., 2017; Kawaguchi et al., 2017; Duclos et al., 2018; Blanch-Mercader et al., 2018; Tan et al., 2020; Zhang et al., 2021) and hexatic order (Pasupalak et al., 2020; Maitra et al., 2020; Hoffmann et al., 2022) with the two phases potentially coexisting (Armengol-Collado et al., 2022) and interacting provide a fresh perspective for understanding cellular processes." Do the authors also find that the two phases coexist? I find this rather difficult to understand.

2. The 1/2 defects are defined using a nematic order parameter (I guess the positions of the defects are identified as the positions of zeros in this order parameter and the sign is assigned by looking at the orientation field around that). However, I think it will make the work more self-contained and easier to understand if the authors explicitly explain how they obtain a nematic order parameter field from a map of projected 2d cell shapes.

3. I am guessing that the 1/6 defects are defined purely using the co-ordination number of the cells (or do the authors construct a hexatic field and use the zeros of that to identify the hexatic disclinations?). But the probability density of average coordination number from Figure 2e seems to be peaked at 5 rather than 6. Therefore, I don't understand the rationale for considering hexatic defects (or hexatic order). Also, would it be possible to define a hexatic order parameter the same way the authors (presumably) defined a nematic order parameter (and director field) and obtain the defects explicitly as singularities in this field?

4. The authors say "Figure 4(c) shows the evolution of spatially averaged normalized isotropic stress for extruding cell…. demonstrating a clear stress build up, followed by a drop near t~−t~e=0". Maybe I am missing something, but I do not see this drop. Instead, the mean (red line) increases monotonically.5. The authors say that the out-of-plane shear stress "prior to extrusion exhibits oscillations with large magnitudes relative to the mean field." However, since they don't present any data on the usual fluctuation of the out-of-plane shear stress (i.e. for non-extruding cells), the reader has no way to judge whether this is atypical. Surprisingly, the standard deviation seems to be larger at earlier times (i.e., away from the extrusion event). Could the authors compare the standard deviation of the shear stress fluctuations of extruding and non-extruding cells?

6. If the earlier point is not clarified, it is not really clear to me what new information is obtained from a 3d model of the cell layer that couldn't be obtained from a 2d phase field model. (I do understand that their criteria for identifying extrusion is only available in the 3d model, but in a 2d model, one could choose a different criterion -- shrinkage of the (2d projected) area of a cell below a critical value or cell overlap for instance -- which would probably lead to similar results).

7. The cells in the authors' model move in the direction of the cell polarisation. It would be useful if the authors could comment how this cell polarisation is determined.

8. In the same vein, the cell polarisation doesn't directly affect the cellular structure (i.e., there is no term involving the polarisation in the free energy in Eq. 1). Is that assumption correct?

9. The authors say "Interestingly, the association of cell extrusion events with regions of high out-of-plane shear stress has parallels with the phenomenon of plithotaxis, where it was shown that cells collectively migrate along the orientation of the minimal in-plane intercellular shear stress (Tambe et al., 2011). In this context, based on the association of cell extrusion events with regions of high out-of-plane shear stress, we conjecture that high shear stress concentration hinders collective cell migration with cell extrusion providing a mechanism to re-establish the status-quo." I don't see clear evidence of high out-of-plane shear stress in 4b. Figure 4b has two extrusion sites, one of which certainly displays high out-of-plane shear stress, but the other, not so much. Could the authors quantify their claim that extrusion events are statistically associated with high out-of-plane shear stress?

10. The authors claim that the probability of extrusion at "nematic and hexatic disclinations " changes depending on cell-cell and cell-substrate adhesion. Is this a secondary consequence of the structure of the cell layer changing depending on those parameters (i.e., going from a predominantly nematic-like organisation to a more hexatic organsiation)?

11. If I understand correctly, the cells are extruded at -1/2 disclinations as well, which I find puzzling.

Reviewer #2 (Recommendations for the authors):

I would like to point out:

– The identification of defects, as shown in Figure 2, sensitively depends on various thresholds. The cell with 4 neighbors in Figure 2b could easily be also considered as a cell with 8 neighbors. How sensitive are the results with respect to the thresholds used?

– Why is the approach to find correlations between defects and extruding cells different for positional and orientational defects? I would find it more natural to also average over various runs and time intervals to identify such correlations for the positional defects.

– In the conclusion it is argued that negative Gaussian curvature cannot form due to the rigid substrate. This somehow indicates that the basal side is considered, for which I understand this argument. For the apical side I don't! As I assume that the experimental data in Saw et al. show the apical side, I wonder what the relation is?

Reviewer #3 (Recommendations for the authors):

This work explores the linkage between extrusion and topological defects in cell monolayers. To better understand this linkage, the authors used cutting-edge numerical simulations that were developed by some of the authors in Mueller et al. 2019. I have some major concerns regarding some theoretical analyses and interpretations of results (see major point 1 and minor points). I cannot recommend the publication of the present manuscript before these concerns are addressed.

1. Linkage between topological defects and extrusion events.

1.1. In line 104 to 108, it is suggested that the state in Figure 1a is an active nematic turbulent state based on the nucleation and dynamics of nematic defects. However, an active turbulent state is also characterized by specific statistical features of flows. Are the flows in simulation compatible with an active nematic turbulent state?

1.2. In line 117-124, it is suggested that extrusions in Saw et.al. 2017 correlate with the position of + and -1/2 defects. Unless I am mistaken, their observations showed spatiotemporal correlations only for +1/2 defects. Can the authors comment on this point? If this is the case, how do the authors interpret the fact that -1/2 defects also correlate with cell extrusion in their simulations? Is the mechanism for cell extrusion in -1/2 defects of mechanical origin? Adding the average isotropic stress near -1/2 defects would help to clarify this point.

1.3. In lines 124-128, the authors define a time interval around an extrusion event, but I could not understand the reason for the choice of the lower and upper values (5.625 and 0.625). How did the authors choose these values? In the Figure 4, the stress build-up occurs within a time interval of less 1 unit of time, and in Figure 8, the change in the coordination number and the area seem to occur over time intervals of 10-100 units of time. Can the authors discuss the separation of these time scales? Another relevant time scale is the mean life-time of nematic topological defects in their simulations, can discuss show the distribution of life-times of nematic defects and discuss how this is related to the other time scales?

1.4. The authors observed that extrusion preferentially occur near + and -1/2 defects. However, in Figure 2a, there are two extrusion events and tens of defects, which seems to indicate that many defects are non-functional because they do not generate an extrusion event. Is it the case? Can the authors provide an estimate of the fraction of defects that are non-functional? Along these lines, a question that remains unaddressed is whether an extrusion event can favor the nucleation of a pair of nematic defects. Can the authors comment on this?

1.5. In Figure 2a it seems that the typical separation between nematic defects is approximately 6 cell sizes. In the case that extrusion events occur randomly, I would have expected d_min to be below 3. However, in Figure 3a, d_min can reach 25 cell sizes. Can the author comment on these differences? Can the authors include the distributions of density of nematic defects in their simulation?

Besides, can the authors add numerical details in Methods on how were the extrusion events generated in the hypothesis-testing approach? For example, were cells pulled upwards with a constant force or at a constant speed?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Mechanical Basis and Topological Routes to Cell Elimination" for further consideration by eLife. Your revised article has been evaluated by Jonathan Cooper (Senior Editor) and a Reviewing Editor. The referees did acknowledge that the manuscript has been significantly improved, but there remain a number of serious criticism that must be answered.

Model assumptions: Many possible 3D features that could be responsible for complex 3D cell shapes are not included in the model. This needs to be explicitly discussed in the manuscript. These include:

1) You present a 3D model and claim that it is essential to understand cell extrusion, but most of the analysis is done on 2D quantities. The results regarding the isotropic and out-of-plane shear stress are certainly interesting but do not constitute such an explanation for the extrusion process. Furthermore, a number of assumptions of the model relate to 2D features. For instance, the polarity appears to be a 2D quantity defined by an angle (probably in the x-y plane, this should be specified). This seems to exclude active out-of-plane relative movement between cells which could participate in the extrusion process in real systems. Is there any reason for the RHS of Eq. 3. to be a two-dimensional vector or is the cell velocity not strictly in the plane? This should be clarified, and the limitations of the model clearly discussed

2) Furthermore, the magnitude of the polarity vector is set to unity, which precludes fluctuations of activity among cells, a feature that is often associated with local rearrangement processes such as extrusion. This is a strong assumption that is not discussed.

2) Extrusion has often been described as the result of different mechanical properties in the basal and apical sides on the epithelia. You say in your rebuttal that this is just one element of the 3D complexity on which you choose not to focus. It is acceptable not to include this in a model in order to focus on other effects, however, this possibility should be mentioned as a relevant process in the manuscript.

3) Scutoids. It does not appear to be clearly demonstrated that scutoids are a feature of curved epithelia only, and it is quite possible that such arrangement might be relevant to the extrusion process even in flat epithelia. While a model such as the present one that does not include this possibility is certainly valuable, the text should not give the impression that they are irrelevant.

Analysis:

4) Most of the analysis is done on projected quantities, but how the projection is obtained is not clearly explained. What does the 2D representation (such as Figure 2 for instance) exactly show? Is it a cut through the epithelia at fixed z, or some kind of maximum intensity projection? This must be specified.

5) in Figure 2a, it seems that the director field (red bars) around blue +1/2 defects correspond to -1/2 defects, and vice-versa the director field around green -1/2 defects correspond to +1/2 defects. This feature is clearer for defects that are far from others. If this is indeed the case, it should be corrected.

6) In the new Figure 12, the probability density of pairwise distance between defects is presented. It is unclear whether this distance corresponds to the minimal distance between pairs of +1/2 defects or rather the distance between half-integer defects. To compare with the results from Figure 2 the former seems more appropriate. Please comment on this point and include the former distribution if necessary.

7) Some new results presented in the revised version are confusing, or insufficiently discussed. For instance the new Figure 6 in the rebuttal. If one holds cell-substrate adhesion fixed, the mean number of extrusions has a clear maximum at a particular cell-cell adhesion. However, no other quantity that the authors present seems to show a similar maximum. Maybe the origin of this is hiding in the plot of nematic defect density for different adhesions (Figure 5 of the rebuttal). If so, that plot should be improved and both that and the Figure 6 of the rebuttal should be brought to the main text, as this seems an important feature of the problem

Discussion:

8) Threshold: In your response and in the manuscript (l.192), you seem to suggest that your method does not suffer from the arbitrariness of setting a threshold to defined extrusion events, but it appears (l.99) that extrusion also involves thresholding (of the cell vertical displacement – l.99) in your case. How would this threshold influence the results?
