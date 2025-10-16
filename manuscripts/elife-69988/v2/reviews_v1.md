# Peer review - Round 1

Editors:
- Stephen C Ekker, Mayo Clinic United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69988.sa0](https://doi.org/10.7554/eLife.69988.sa0)

The issue of building a high-quality brain atlas for vertebrates has been a long-standing challenge in the field. Your work has nicely hit this mark using zebrafish, and using a method that should be applicable to many different stages and other organisms.


---

# Peer review - Round 1

Editors:
- Stephen C Ekker, Mayo Clinic United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69988.sa1](https://doi.org/10.7554/eLife.69988.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "AZBA: A 3D Adult Zebrafish Brain Atlas for the Digital Age" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Stephen C Ekker as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Marianne Bronner as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Harold Burgess (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The following issues need to be addressed, and should not cause much of a delay:

1) Non-annotated areas should not be "0" like areas outside (use of black in both cases).

2) There should be one table containing colors, abbreviations and full names of anatomical structures (which will make the data much more and easier accessible). Assigning all anatomical entities to larger brain structures (telencephalon etc) may not be possible for all structures due to anatomical disputes, but also very helpful where possible.

3) Think they should do an analysis to at least show the differences are not so huge that mixing the sexes is reasonable.

Reviewer #1 (Recommendations for the authors):

This paper uses cutting-edge imaging to develop a new 3D map of the zebrafish brain. The use of fixed imaging plus antibody staining with Lightsheet microscopy has developed an excellent high-resolution dataset. The regional imaging data is convincing. The data is well-presented, and the text easy to read. This is an ideal manuscript within the broad scope of eLife.

A few questions remain to better understand the outcomes they describe:

1) For smaller brain regions, how do they validate their annotation? This was not clear.

2) What is the true estimate of error of their imaging approach? 8 microns is pretty large, and might lead to errors in tagging individual cells. How do they sort this out? This is not well presented in this current version of the manuscript.

3) How many different fish did they image? We now know there are a LOT of differences even between siblings of wild-type lines. This would provide another form of error they would need to address, if nothing else for users to explore their resource.

Reviewer #2 (Recommendations for the authors):

My comments below should be interpreted only as efforts to make this atlas as user-friendly as possible.

Understandably, due to the incomplete knowledge of the zebrafish brain, some parts of the brain have not been segmented. At present, these areas are indexed as 0 (zero), which is the same as the area outside the brain. I would strongly encourage the authors to distinguish unannotated voxels from space outside of the brain, as this will be essential to facilitate computational analyses of brain imaging data.

I suspect that the annotation file "2021-05-02_AZBA_Label_descriptions.txt" is formatted for ITK-SNAP. However, it could be more useful for other computational studies:

(1) At present, the file contains only region abbreviations, making it necessary to constantly consult Table S2 of the manuscript. I would like this file to additionally include the full name of the region.

(2) Each region should be associated with a major brain division (telencephalon, diencephalon etc) and where possible, given any other useful annotations (ventricle, tract, nucleus). These labels provide valuable grist for computational methods.

(3) For people not using ITK-SNAP it would be helpful to provide the coordinates of a voxel within each region. For example I tried in vain to hunt for the voxels corresponding to MAC.

(4) I understand the first column (index) and last column (abbreviation). What are the other columns?

After light-sheet imaging, what actually happens during the step referred to as "3D volume generation", or "Three-dimensional volumes were created from individual image sets", or "Image stacks from individual fish brains were converted to 3D volumes”? Does this simply refer to the stitching plus resampling procedure?

If I understand correctly, the ultimate step in generating a template brain was to mirror the first average, then register the previously linearly aligned TOPRO samples to to it. Although I appreciate from the data I retrieved from Dryad that the result is a symmetric brain, I can't quite understand why this procedure yielded a symmetric template, rather than just a more precise template with left/right reversal, so please describe what happened in this step more clearly.

More importantly, while in general a symmetric template is desirable (especially for computational approaches), this procedure obscures important biological asymmetries present in the habenula, a major focus of neurobiological studies in zebrafish. Could you somehow exclude the habenula from the symmetrization step?

No information is provided on the precision of the registration procedure. It would be helpful to assess precision so that subsequent users can evaluate whether their own procedures provide sufficiently close alignments.

I expect that autofluorescence is more variable than TOPRO and carries less information. However there is no information provided for evaluating the quality of the registration achieved using autofluorescence as a bridging channel. Figure 4D (which is small and hard to see) purports to illustrate the accuracy of autofluorescence bridging registration using the example of the Locus Coeruleus. However, because one can not reliably ascertain the LC in either the HuC or TOPRO stain, there is nothing to usefully compare the TH stain to. Precise registration is important because the IHC channels used for segmentation were registered using autofluorescence. Please provide a measurement of registration accuracy using autofluorescence. Why was TOPRO not used with IHC for this step, to provide the strongest alignment?

The Methods are generally appropriately detailed, and specify the age of the fish. However, 3-4 month old fish can vary widely in size, and therefore presumably in brain volume. It may be helpful to add details on the size of the fish, and how sensitive the accuracy of the registration procedure is to size.

Much of the segmentation was performed on coronal sections, for which region boundaries are generally smooth. However, when viewed in other planes, boundaries are jagged resulting in artificial discontinuities within regions. It would be desirable to implement at least a simple procedure to smooth region boundaries in 3D space.

Reviewer #3 (Recommendations for the authors):

In the intro page 4 the authors claim the adult zebrafish brain would be "several orders of magnitude larger" than the larval brain. "Several" to me means more than two, but I would think that the adult zebrafish brain is just one order of magnitude larger (larva 500 micrometer, adult 5-15 mm).

Some images, e.g. in Figure 4, especially 4d, but also parts of Figure 7, are provided with too low resolution in the PDF to judge detail.

Figure 7B middle panels "0,10"

Prox1 appears to be an example that a major expression domain maps to a non-annotated anatomical domain – or the prethalamus is so dark here that it cannot be distinguished from black. In the text where Prox1 is presented, this domain appears to be not mentioned.

For some panels it may be better to present cutouts at higher magnification, with anatomical regions outlined in fine white lines and labelled (rather than using the color code only).

D GFAP: I cannot identify in the figure the GFAP pattern described in the text:

"we found GFAP most concentrated near the midline and ventricles (Figure 7D)."

Why is there no GFAP signal in the midsagital section 7D 0.00?

Materials:

Given sex differences in the fish brain (see papers cited by authors), the authors should report whether male or female brains or a mix of brains from both sexes were used.

Limitations

Given that relatively few antibodies are available for specific zebrafish neuronal markers, it would be very informative to know if the technique used by the authors would in principle be applicable to fluorescent whole mount hybridization stained brains.
