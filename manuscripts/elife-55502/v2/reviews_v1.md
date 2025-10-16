# Peer review - Round 1

Editors:
- Birte Forstmann, University of Amsterdam Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55502.sa1](https://doi.org/10.7554/eLife.55502.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper develops a new computational imaging approach for label-free imaging that uses polarization to acquire joint measurements of density and anisotropy. The authors provide evidence that this label-free approach can be combined with deep learning to effectively characterize the architecture of different samples across multiple spatial scales. To achieve this, they introduce a relatively computationally efficient deep learning architecture based off of the 3D U-Net that can be used to predict structures from multi-channel images as well as rescue inconsistent labelling.

Overall, the topic is of high interest and the reviewers agree that combining quantitative label-free imaging and deep neural networks of live and postmortem tissue is novel and important. The work is therefore of interest to a broad scientific audience.

Decision letter after peer review:

Thank you for submitting your article "Revealing architectural order with quantitative label-free imaging and deep learning" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Vivek Malhotra as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: David Van Valen (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

This paper develops a new computational imaging approach for label-free imaging that uses polarization to acquire joint measurements of density and anisotropy. The authors provide evidence that this label-free approach can be combined with deep learning to effectively characterize the architecture of different samples across multiple spatial scales. To achieve this, they introduce a relatively computationally efficient deep learning architecture based off of the 3D U-Net that can be used to predict structures from multi-channel images as well as rescue inconsistent labelling.

Overall, the topic is rated very high and the reviewers agree that combining quantitative label-free imaging and deep neural networks of live and postmortem tissue is valued. However, there are several major concerns the authors need to address before this manuscript can be considered for publication in eLife. These are listed below.

Essential revisions:

1) The idea of label-free prediction of a specific tissue structure from density and anisotropy measurements is appealing and well described in the manuscript. However, the selected types of tissue and some of the general conclusions drawn (partially from cross-comparisons) are disputable. What makes mouse kidney, mouse brain and prenatal human brain unique in terms of 'revealing architectural order', but still comparable? There seems to be a lack in knowledge of brain anatomy and morphology, which is important to evaluate the results. Although the GW24 and GW20 measurements are exciting, the shown tiny ROIs are not suitable for highlighting the anatomical differences in a convincing way. The deep learning approaches appear to be correctly implemented and applied, but their scalability does not become obvious (although stated in the Abstract). A critical debate about the efforts needed to address entire large-scale organs is missing. The major add-on to state-of-the-art approaches or to previous own publications does not become clear enough.

2).Ethics: There is no clear statement of the authors concerning ethical approval, origin of samples, etc. The treatment of prenatal human tissue requires other information than the mouse brain and kidney tissue!

3) The key insight offered by this paper is that because deep learning is data-driven, these methods can be improved by improving data rather than making substantial changes to the algorithms. If there is information missing in the images that is needed to make accurate predictions, why not add it in? To me this is an under-appreciated insight, one that the authors cleverly take advantage of, and one that the life science community as a whole sorely needs to hear. Based on the results presented here, there is a good chance that a number of previously ignored imaging modalities will now have higher value because of what can be done with deep learning. Unfortunately, I don't think the paper as written does a good job of relaying this conceptual shift and this is a substantial issue with the paper. Some of my recommendations to address this would include:

3a) Restructuring the Introduction. The prior work of Greg Johnson and others should be presented earlier so it is clear that this work builds on theirs. Doing so would make it easier for readers to appreciate that the novelty lies in combining these methods with the author's approach to quantitative label-free images.

3b) Better describe the novelty and performance gains. On the label-free imaging perspective, it is unclear how much of the work presented here is novel, as opposed to a straightforward application of the author's previous fluorescence based methods. I think this could be better explained. Also, the advantages of their method with respect to archival samples (i.e., obtaining staining information while avoiding potentially damaging stains) should be described earlier. The benefit of these methods for live-cell imaging (obtaining data while avoiding photodamage with respect to fluorescence) should also be mentioned, albeit with the appropriate reference.

4) In addition to this, the second major issue with this paper is how much of a performance boost does the author's label-free imaging approach provide? While the conceptual shift described above is appealing and should be highlighted, the case the authors make that this transforms one's ability to use image-to-image translation models on biological images is less clear. The authors use both the Pearson correlation and the structural similarity index to quantify their reconstruction of fluorescent actin in U2OS cells and in brain slices. However, the differences between standard label-free imaging (brightfield and phase) and the author's approach (brightfield, phase, retardance, and orientation) appear minor. For instance in Table 2, the difference in Pearson correlation is ~0.01-0.02 (the gap does appear to be bigger for FluoroMyelin, but fewer comparisons are presented). On its surface, this appears to be a minor advance (although one could argue whether it is in the realm of statistical significance) and as an experimentalist, it makes one question whether the "juice" of the author's method is worth the "squeeze". However, there are certainly cases where minor boosts in accuracy lead to a big difference in one's ability to use a method. While the ability to measure orientation is certainly useful for following neural fibers, it feels like the case that this architectural information is critical to infer fluorescence patterns hasn't been made.
