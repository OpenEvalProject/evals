# Peer review - Round 1

Editors:
- Moritz Helmstaedter, Max Planck Institute for Brain Research Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.45696.027](https://doi.org/10.7554/eLife.45696.027)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "MagC, magnetic collection of ultrathin sections for volumetric correlative light and electron microscopy" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Eve Marder as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As you can see below, both reviewers value the innovative approach of the method. However, both reviewers request a more elaborate discussion of the limitations of the approach. At the same time, reviewer 2 lists a series of insufficiencies of the manuscript's presentation, which we expect to be addressed in a revised version.

In particular, the raw data should be available for the reviewers before the manuscript can be accepted. Similarly, the data should be made available (and stay available) for the readers after eventual publication.

Finally, we ask you to resubmit the paper as a Tools and Resources paper, as it is a Methods paper.

Reviewer #1:

In the manuscript "MagC, magnetic collection of ultrathin sections for volumetric correlative light and electron microscopy" Templier details a novel solution to a historically vexing problem -how to reliably collect hundreds of ultrathin sections for serial electron microscopic 3D reconstruction.

Traditionally electron microscopists will carefully trim and prepare the sample block so that the resulting ultrathin sections stick together in long trains in the order they were cut while floating in the diamond knife boat (e.g. Harris et al., 2006). These trains of sections can be collected on a silicon wafer by carefully nudging them with an eyelash while water is drained from beneath them (e.g. Burel et al., 2018). Templier's method avoids the complications involved in ensuring trains of sections reliably form while cutting. It also avoids complications involved in ensuring that these trains stay in position above the silicon wafer as the water is drained. He does this by eschewing train formation altogether, instead trimming the block to a point and positioning an air current source to ensure that sections do not stick together to form trains. Crucially, Templier describes how to augment the sample block with superparamagnetic nanoparticles (along with fluorescent beads) prior to ultrathin sectioning so that each individual ultrathin section will be attracted by a permanent magnet which, following completion of sectioning, is positioned 1 mm above the water's surface and swept over the boat to collect and concentrate all sections directly above a submerged silicon wafer. The water is then withdrawn, and heating pads are engaged, causing the ultrathin sections to adhere to the silicon wafer supposedly without wrinkle formation. Templier describes how section ordering can be restored computationally by imaging the fluorescent beads in LM and calculating the correlation matrix of all collected sections. Templier proceeds to demonstrate his method with two correlative LM and EM datasets.

Importance: Dense cellular connectomics is important to neuroscience research and multibeam scanning electron microscopes are being used by an increasing number of labs to push to larger volumes. Since these multibeam SEM perform best when sections are collected directly onto silicon wafers, Templier's MagC method provides a much needed solution for such section collection.

Novelty: Other solutions exist to the problem of collecting ultrathin sections on silicon wafers (e.g. Burel et al., 2018) but Templier's MagC method has the potential to be easier and more repeatable as it avoids many of the manual steps.

Effectiveness: Templier provides two datasets (507 and 203 sections, 50 nm section thickness) as evidence of the effectiveness of the MagC technique. Aside from minor artifacts, these datasets show that neurites can be traced throughout and large immunolabeled processes can be identified in LM and correlated with the EM.

Concerns: A more comprehensive discussion of problems that can occur and steps to avoid them would be helpful.

Minor comment:

A few more details about Figure 1—figure supplement 5 would be helpful. This is supposedly a single multibeam SEM montage from a larger MagC collected run. How many sections were collected in this run? Is this image representative of the overall quality? Was multibeam SEM imaging also compatible with the LM immuolabeling shown in the other datasets?

Reviewer #2:

Templier describes a method to automate the collection of serial sections by embedding magnetic nanoparticles in a sample block and collecting cut sections with a moveable permanent magnet. This is a clever idea and addresses some of the issues with the competing ATUM technology. However, since the manuscript is meant to describe a new methodology, there are several limitations with the manuscript in its current form.

1) The description of the preparation of the magnetic resin is missing. Since this is a key component to the method, it should be explicitly described instead of only citing Puig et al. Details such as the instrumentation used, dispersion method, why a different resin was chosen for the iron nanoparticles, and any optimization of particle concentration that would allow a reader to replicate the procedure are conspicuously missing from the manuscript.

2) The format of the article text reads more like a hastily prepared lab report than a scientific manuscript. The supplementary figure legends contain oddly placed methodological details such as subsections “Metric for order retrieval and order retrieval for data set 1”, “Immunostaining protocol” and “Text 1: conversion of correlative LM-EM imagery for neuroglancer” interspersed with supplementary figures. These details should be in the main Materials and methods section I think, or at least less confusingly organized.

3) Critical issues are not addressed such as a) exploring whether block face size effects the ability of the magnet to collect sections, b) whether the magnetic particles degrade the cutting properties of the knife for thousands of sections, c) can sections less than 50nm thick be collected with the magnet at the nanoparticle density described?

4) A benefit of ATUM is that the collection of thousands of sections can be collected without user intervention. The articles does not address how this process works for MagC. Can sectioning be continued after mounting one batch of sections on a wafer without losing a section? What is the error rate associated with restarting the section collection process?

5) Were the sections that needed to be manually detached from the wall of the boat damaged?

6) The logic behind attaching the dummy piece is not sufficiently described. What happens if the dummy piece is not attached?

7) A downloadable image stack is preferable to a youtube video (Video 1) for assessing data quality. I'm not sure what is the scientific content of Video 2, it seems more like a PR video.

8) I have tried to open the location of the datasets with multiple browsers, but have only received ‘site not’ found errors.

9) When trying to visualize the link showing traced neurites I could not see the raw data and received an error.

10) I couldn't find details in the Materials and methods about what type of LM and SEM was used to perform the imaging and under what imaging conditions.

11) Details about how cutting was performed are missing, such as cutting speed, knife angle, clearance angle, etc…

12) A video of the process of collection (demonstrating the snake path of the magnet and dropping the water level) would be very helpful.

13) The main text describes the LM imaging procedure briefly but the Materials and methods do not expand on this. Does the immersion oil on top of the sections simply wash off? Are there any other cleaning steps before heavy metal post-staining?

14) The 'Data analysis' portion of the main text is more focused on data visualization. Some detail is needed regarding the length of traced neurites, etc…

15) Were any sections distorted during the collection process (e.g. folds, tears, warping), particularly during the mounting step down onto the wafer? Was this assayed?

16) Typo subsection “Section collection, last paragraph”, should be 45 mm.

17) The description of 'asymmetrically stacked microscopy coverslips' (subsection “Section collection, last paragraph”) is unclear. A diagram would help to show how the wafer is actually situated in the boat.

18) Figure 1—figure supplement 3 references a panel 'H' that is not in the actual figure.

19) Figure 1—figure supplement 1: The sections are of different intensities and contrast. What is the source of this variability?

20) Figure 2—figure supplement 1 references 6 panels, there are only 4 in the figure.

21) What is the actual contamination in Figure 1—figure supplement 2D. Is this an aggregation of iron nanoparticles?

22) Figure 1—figure supplement 2, there appear to be slivers detached form the sections in panel A. What are these? I don't see the dummy piece in these sections. Is the attachment of the iron in this example the same as presented in Figure 1?
