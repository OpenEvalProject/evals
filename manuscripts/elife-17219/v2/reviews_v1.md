# Peer review - Round 1

Editors:
- Axel T Brunger, Howard Hughes Medical Institute, Stanford University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.17219.028](https://doi.org/10.7554/eLife.17219.028)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Automated structure refinement of macromolecular assemblies from cryo-EM maps using Rosetta" for consideration by eLife. Your article has been favorably evaluated by John Kuriyan (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors and another is Sjors HW Scheres (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript concerns atomic model refinement against maps obtained from single particle electron microscopy data at near atomic resolution (for EM structures determined in the ~ 4.5 to 3 Å range). This is an important topic in modern structural biology, as the recent surge in resolution of cryo-EM structures calls for improvements in the methods to position and refine atoms in these maps.

Here the authors use the Rosetta package which takes into account prior knowledge about protein structure. Although Rosetta has been previously applied to EM map refinement, the authors describe a number of improvements of the method. The authors implemented (1) procedures to detect regions where the fit of manually built models produced strain in the local geometry as a consequence of misfitting the map or as a consequence of inaccuracy of the magnification parameter. Other improvements include (2) voxel size refinement, which may resolve the magnification inaccuracy of cryoEM maps; (3) side chain down-weighting during refinement, which may be proper for cryoEM maps since the molecules are not packed and therefore side chains less well defined compared to backbone; (4) refinement against the full map at the final stage.

Although none of these approaches are individually entirely new, it is the combination of these methods that may become a useful tool for the structural biologist working with EM maps. However, the reviewers have identified a number of issues that need to be addressed before a final decision can be made.

Essential revisions:

1) The improved refinement methods should be compared to standard refinement approaches, since otherwise it is difficult to judge the improvement of the presented over existing methods. They should for example compare with standard phenix.refine real-space simulated-annealing refinement. The amount of computational time for both approaches should also be provided. Finally, the comparison should systematically assess the quality of the model fit throughout the model, not just by subjectively showing particular regions.

2) There is clearly a need to find a better estimate of the voxel size. It is tempting to optimize the voxel in the way described here and it has been done in the same way before as published by other groups (these references to previous work should be provided). However, if the model has errors (which it always has), the best modelmap correlation is not always obtained for the correct voxel size. One of the reviewers performed a simple test using a PDB structure (PDB ID 4AKE) and simulated a density with voxel size 1.0 Å. Errors were introduced to the model by adding Gaussian noise to the atomic coordinates, here with a σ of 3 Å. 50 of such randomized models were generated. The modelmap correlation was then plotted for different voxel sizes, showing mean and standard deviation for these 50 models. It turns out that the error of the voxel size optimization is of the same order of magnitude as the typical error of the estimate from the microscope (~1%). Thus, the proposed voxel size estimation method may not produce the true voxel size. This issue needs to be addressed in the manuscript.

3) Figure 4A is supposed to show the mismatch of the deposited model and density. One of the reviewers downloaded the deposited model (PDB 4CI0) and EM map (EMD-2513) and could not reproduce this figure. The deposited model actually fits well into the deposited map. Images are attached to this decision letter of a similar view with the same contour level given in the figure caption (0.065). The authors need to clarify this issue.

4) The authors may wish to further elaborate on two limitations that are briefly mentioned in the final paragraph of the Discussion:

A) How to handle maps that have dramatic differences in local resolution. For example, in the TrpV1 channel case, the authors had to refine part of the model in two steps against two parts of the map (which is only mentioned in the Methods).

B) How to determine the sharpening B-factor objectively before real-space refinement. The authors appear to have determined the sharpening B-factor subjectively (as mentioned in the first paragraph of the Methods section). But what criterion was used? This issue may become more difficult when the map has heterogeneous local resolutions.

5) How does the method handle missing residues in loops or disordered region that are very difficult to place manually? This would be a very useful tool.

6) Figure 3B, right panel. How are these different models of the ensemble selected? By using some map correlation criterion to get the "best" fitted models?

7) The original and optimized voxel sizes for the F420 example is given in the manuscript as 1.320 and 1.326 Å. The changes in voxel sizes should also be given for the other examples.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Automated structure refinement of macromolecular assemblies from cryo-EM maps using Rosetta" for further consideration at eLife. Your article has been favorably evaluated by John Kiriyan (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors.

The manuscript has been improved but there is a remaining issue that needs to be addressed before acceptance, as outlined in the following.

The reviewers found the explanation on the issue previously raised about Figure 5 not satisfactory. The shift shown in Figure 5 is not a result of voxel size error, but is likely due to the fact that the authors of the F420 structure (PDBID 4ci0) did not carefully generate the biological assembly structure. Maybe there was a slight mismatch in the symmetry operators used to generate the entire assembly. If one fits each subunit rigidly into the density (e.g. in Chimera) then all subunits fit very well (also with the original voxel size of 1.320). Figure 5A and the "deposited" items in panels B and C should therefore be removed. The effect of changing the voxel size from 1.320 to 1.326 Ang is much smaller than the current figure suggests.
