# Peer review - Round 1

Editors:
- Paschalis Kratsios, University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.89050.4.sa0](https://doi.org/10.7554/eLife.89050.4.sa0)

This Research Advance describes a valuable image analysis method to identify individual neurons within a ‎population of fluorescently labeled cells in the nematode C. elegans. The findings are solid and the method succeeds to identify cells with high precision. The method will be be of interest to the C. elegans research community.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.89050.4.sa1](https://doi.org/10.7554/eLife.89050.4.sa1)

In this paper, the authors developed an image analysis pipeline to automatically identify individual ‎‎neurons within a population of fluorescently tagged neurons. This application is optimized to deal with ‎‎multi-cell analysis and builds on a previous software version, developed by the same team, to resolve ‎‎individual neurons from whole-brain imaging stacks. Using advanced statistical approaches and ‎‎several heuristics tailored for C. elegans anatomy, the method successfully identifies individual ‎‎neurons with a fairly high accuracy. Thus, while specific to C. elegans, this method can ‎become ‎instrumental for a variety of research directions such as in-vivo single-cell gene expression ‎analysis ‎and calcium-based neural activity studies.‎


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.89050.4.sa2](https://doi.org/10.7554/eLife.89050.4.sa2)

The authors succeed in generalizing the pre-alignment procedure for their cell identification method to allow it to work effectively on data with only small subsets of cells labeled. They convincingly show that their extension accurately identifies head angle, based on finding auto florescent tissue and looking for a symmetric l/r axis. Their demonstrated method works to allow the identification of a particular subset of neurons. Their approach should be a useful one for researchers wishing to identify subsets of head neurons in C. elegans, and the ideas might be useful elsewhere.

The authors also assess the relative usefulness of several atlases for making identity predictions. They attempt to give some additional general insights on what makes a good atlas, and clearly demonstrate the value of more data. Some insights seem less clear as available data do not allow for experiments that cleanly decouple: (1) the number of examples in the atlas; (2) the completeness of the atlas; and (3) the match in strain and imaging modality discussed. In the presented experiments the custom atlas, besides the strain and imaging modality congruence discussed is also the only complete atlas with more than one example. The main neuroPAL atlas is an imperfect stand-in since a significant fraction of cells could not be identified in these data sets, making it a 60/40 mix of Openworm and a hypothetical perfect neuroPAL comparison. The alternate neuroPal atlases shown in supplemental figure 4 are complete but provide only one point cloud.

It is striking that in the best available apples to apples match the single data set glr-1 atlas produces qualitatively better results than the single (complete) neuroPAL atlas. This is a clear performance advantage given the ground truth. This is as good an evaluation as is possible given current data however given the inexact nature of assigning ground truth identities I think it is difficult from results to tease out if this is due to strain, imaging conditions or systematically different identifications of cells from different sources.

The experiments do usefully explore the volume of data needed. Though generalization to other arbitrary cell subsets remains to be shown the insight is useful for future atlas building that for the specific (small) set of cells labeled in the experiments 5-10 examples is sufficient to build an accurate atlas.
