# Peer review - Round 1

Editors:
- Eve Marder, Brandeis University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.57443.sa1](https://doi.org/10.7554/eLife.57443.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

We consider this work to be a tour de force achievement on several fronts. Technologically, it ties together nearly a decade of advances in sample preparation, imaging, data management, and image analysis. It also is a very complete automated reconstruction of an EM volume that allows the authors to carefully begin the process of labeling subregions of the neuropil, derive cell types on the basis of both structure and connectivity, and identify circuit motifs, and is a demonstration of what connectomics has always promised to deliver: a reference atlas for biologists and a springboard for theoreticians and modelers working anywhere between the single-cell and whole network levels. We anticipate that this paper and its tools will facilitate the work from numerous laboratories around the world.

Decision letter after peer review:

Thank you for submitting your article "A Connectome and Analysis of the Adult Drosophila Central Brain" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Michael Eisen as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Jason Pipkin (Reviewer #1) and Chris Q Doe (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

This paper is viewed as a landmark contribution to the methodologies of EM connectomics and its use to characterize the Drosophila brain. The manuscript is extensive and well-illustrated, and the reviewers and editors are pleased to help to make this work available to the public. I am taking the unusual (for eLife) action to include the two reviewers in their entirety, as they include constructive comments that were intended by these two careful readers to make the paper more accessible and more useful for the community. I hope that you will take into consideration these comments, and make those editorial changes that will strengthen the paper. In particular, reviewer 2's major request for additional information seems critical for the paper to be maximally useful to the community,

Title: Reviewer 2 suggests a change in the title for your consideration.

Reviewer #1:

The work presented by Scheffer et al. here is a tour de force achievement on several fronts. Technologically, it ties together nearly a decade of advances in sample preparation, imaging, data management, and image analysis. Most impressively, this represents – to my knowledge – the densest and most complete automated reconstruction of an EM volume of this size. While at least one larger volume has been generated from the adult fly brain (Davi Bock's TEMCA work), it has not been segmented (yet) to the level of completion presented here. (Though I am curious to hear the authors' thoughts on to what extent the overall automated segmentation strategy used herein is truly dependent on the isotropic voxels or if a similar set of networks could be retrained on anisotropic data from other existing volumes. One can imagine the value in validating connectivity in another sample that's already been imaged.)

The completeness of the hemibrain connectome enables the authors to carefully begin the process of labeling subregions of the neuropil, derive cell types on the basis of both structure and connectivity, and identify circuit motifs. They also show that the segmented skeletons enable a first pass at building detailed neuronal models at the single-cell level. Therefore this work is not just the presentation of a volume of data (itself impressive) but also a demonstration of what connectomics has always promised to deliver: a reference atlas for biologists and a springboard for theoreticians and modelers working anywhere between the single-cell and whole network levels.

I have no major critiques of this manuscript. Some of the figures could be more striking – or at least not set to Matlab defaults in terms of colors and box ticks (Figures 17, 20, 21 and 25). Others are beautiful (Figures 8 and 10, e.g.).

Finally, I commend the authors for building out the online portal for others to interact with their data. This is an achievement on its own, and probably the most important one for yielding the greatest scientific returns from their efforts.

Reviewer #2:

This massive work describes new methods for generating EM data on large chunks of nervous system – 250 x 250 μm adult central brain – which includes all of one side of the bilateral brain plus all of the central brain midline structures such as the central complex. Thus, it has an n = 1 for most brain neurons. It excludes most of the optic lobe, and all of the ascending/descending neurons, SEZ and VNC. The paper contains comprehensive analyses of the data set, including motif structure, classifying cell types, and adjusting brain neuropil boundaries. The Neuprint software is elegant and intuitive.

Importantly, this data set and associated software provide a method to transition from a light level neuron morphology (e.g. from a FlyLight neuron to a Neuprint neuron). While this needs further development (see comment below), it has the potential to save years of experimental analysis to reach the same point.

This data set will be the gold standard until the full CNS reconstruction is finished in the future. The quality of the EM data are extremely high based on images shown and data in Neuroglancer. As mentioned above, this is a massive work in many regards.

My only required major comment is to expand the section "Matching EM and light microscopy data" as this is an extremely important advance, and perhaps one of the most useful aspects of the entire manuscript. I think the most useful improvement would be to give an example from beginning (FlyLight neuron) to end (matching neuron in Neuprint). This can be another figure, or perhaps better as a numbered text instructions with full URLs for each required step. Or a third option, provide an example workflow on a Janelia page and link to it here. As it stands, I was unable to perform this function with the available information in the paper.
