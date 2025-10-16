# Peer review - Round 1

Editors:
- Stephen C Kowalczykowski, University of California, Davis , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.03273.012](https://doi.org/10.7554/eLife.03273.012)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “DNA binding polarity, dimerization, and ATPase ring remodeling in the Cdc45-MCM-GINS replicative helicase” for consideration at eLife. Your article has been favorably evaluated by James Manley (Senior editor) and 2 reviewers, one of whom is a member of our Board of Reviewing Editors.

The Reviewing editor and the other reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

Overall, the experiments are well executed the data are sound and the main conclusions are justified. However, neither the inference regarding the ssDNA path (on Cdc45) nor the final model (in terms of conformational changes during the loading and translocation) are fully supported by the data. These issues can be addressed provided that the authors can address the following major points; additional experimentation is likely not required:

1) Relationship of ssDNA binding to Mcm subunits. Figure 2A shows a very specific structure in which DNA is uniquely in contact with the Mcm5 subunit. The basis for this figure is EM reconstructions of the CMG complex with bound DNA that contains a streptavidin tag. As ssDNA is poorly visualized under EM, the streptavidin marks the location of the DNA in the complex. However, 1) the class averages in Figure 2B show the streptavidin at a considerable distance from the CMG complex, making assignment of a specific DNA-binding MCM subunit difficult, and 2) as nearly as this reviewer can tell, there is nothing in the text that specifically identifies Mcm5 as the sole DNA binding subunit. Explain: is Figure 2A a structural summary or artistic license?

2) Thresholding/filtering issues. A major point in the paper is the physical interaction between CDC45 and Mcm5, in which the N terminus of CDC45 is proposed to essentially pry apart the N and C-terminal domains of Mcm5 (Figure 1D). There are several technical problems with this conclusion. Although varying the thresholding (presumably through Chimera) is a useful way to emphasize various features, in Figure 1D it is so extensive that the N and C-terminal domains of Mcm5 are completely separated from one another, a feature not demonstrated by other CMG structures presented in this paper. In general, the thresholding level should generate an enclosed volume consistent with the calculated molecular weight of the component proteins: was this done? When 2 structures are being compared, the levels of thresholding and filtering should be the same in each structure.

3) In addition, the interpretation that CDC45 pries apart the N and C-terminus of Mcm5 largely depends upon how the various masses within the structure were segmented – what part of the density belongs to Mcm5 and what part actually belongs to CDC45? This question has an additional problem insofar as the region of CDC45 that likely interacts with Mcm5 is not highly conserved and the authors were unable to generate a homology model for it. Moreover, the software used for segmentation that sets the subunit boundaries (likely the Segger tool in Chimera) requires a very high-resolution structure to give reliable results without computational validation (< 10 angstroms). Although for transmission EM the structures in this manuscript are excellent, it seems a little optimistic that the authors have enough resolution to accurately validate these boundaries visually. There are computational methods available to provide proper validation of their results (http://ncmi.bcm.edu/ncmi/software/segger/docs_fitting_scores).

4) The figures are confusing and should be improved. Specifically:

A) In all the figures, top and side views should be kept in similar orientations whenever possible for clarity.

B) Figure 3 and Figure 6 are inconsistent in terms of leading strand and lagging strand positions relative to Mcm subunits.

C) Figure 3D suggests a rocking motion (rotation) between the CMG and the duplex DNA. This is not supported by data here. It is quite possible that the leading strand could slip out to the outer channel formed by GINS and Cdc45 without altering the relative orientation between duplex DNA and the CMG. Furthermore, the conformation when the leading strand is captured by Cdc45 is different from that shown here. This figure should be altered to reflect this.

D) Figure 5 suggests the exact register of the CMG dimer based on 2D class averages. Although it is plausible, there are no experimental data to confirm this and Models 3 or 5 cannot be completely dismissed. Furthermore, Figure 5A suggest there might be some flexibility in the dimer arrangement as not all the class averages display the same tight packing. This part of the Results/discussions should be tuned down.

E) Figure 6. Translocation step. The interactions of GINS and Cdc45 with Mcm are different in the two complexes. Please check polarity! The earlier steps neither are unclear nor supported by data here so should be omitted. Furthermore, since Mcm2-7 likely act sequentially, different subunits will have different nucleotide bound states at a given time. ATP-gS state presented here therefore might not reflect the functional state during translocation. It is also unclear what triggers gate open/close. How does the Cdt1-Orc complex (which induces the gate being blocked) enable dsDNA loading? What is the defining factor that leads to DNA melting and gate opening/strand separation? These are not addressed here and therefore Figure 6 should be modified to only reflect major conclusions here. The leading strand and lacking strand as well as their directionality should be labelled.

5) Methods: how many particles contributed to the final reconstruction? How were the streptavidin-labelled data processed? Is a 3D reconstruction obtained (since 436 micrographs were collected)?

6) Significance: the author argued that the need for GINS/Cdc45 in preventing DNA from escaping Mcm2-7 would likely to be minimal. This raises the question of the significance of the additional roles proposed in this paper (to capture the “escaped” leading strand). Please reconcile.
