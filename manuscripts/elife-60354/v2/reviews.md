# Peer review - Round 1

Editors:
- Tatiana Sandoval-Guzman, Center for Regenerative Therapies TU Dresden Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.60354.sa1](https://doi.org/10.7554/eLife.60354.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This study presents a combination of techniques to examine macromolecule synthesis in a complex and rapidly changing structure such as the regenerating limb of an axolotl. A pipeline for 3D visualization and quantification reveals the heterogenous cellular response within a complex tissue. Of interest, is the compatibility to use in other organs and tissues or at the organismal level.

Decision letter after peer review:

Thank you for submitting your article "3D Visualization of Macromolecule Synthesis" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Tatiana Sandoval-Guzman as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Didier Stainier as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. This decision includes a summary redacted from the three reviews.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

Duerr and colleagues present a combination of click-it, tissue clearing and light sheet technologies to examine macromolecule synthesis (namely DNA synthesis, transcription, translation, and glycosylation). This pipeline allows the visualization and quantification of cellular processes in growing 3-dimensional tissue. The authors use axolotl limb regeneration, a challenging system to tackle given its complex tissue types and large volume. Upon amputation, the remaining tissue in the limb will produce proliferating progenitors that accumulate forming a structure called the blastema, which the authors use to test macromolecule synthesis simultaneously. The authors demonstrate that administration of macromolecule analogs can be visualized simultaneously in a single sample. Furthermore, the authors create an image analysis pipeline that allows the analysis of individual elements or segments within the limb; they use the regenerating humerus to demonstrate the multiscale quantitative analysis capabilities of their method.

While the technologies used in this manuscript are not novel, the combination of these techniques together provide a compelling foundation to answer questions in this and other similar systems, while decreasing labor-intensive techniques such as tissue sectioning. The ability to look into these processes while preserving structure, helps understand the underlying biological function of a cell and its intricate relation to other tissues. This method opens up the possibility to analyze complex heterogeneous changes across heterogeneous tissues.

Overall, this manuscript has a potential broad scope and by using already commercial and open source tools, it can facilitate a broader applicability.

We have the following suggestions to improve the validation of the methods described in this manuscript.

Essential revisions:

1) One of the strengths of this methods is the diminution of a labor-intensive sectioning/staining/imaging track. One concern is that a more persuasive effort could be presented to validate the number of cells identified by both methods. Using the EdU+ quantification as a point of reference between the imaging protocols, the authors could provide a direct comparison with the standard methodology. One possibility is a randomized quantification of single planes from the wholemount volume and tissue sections. This would demonstrate side by side the detection sensitivity of the whole mount/LSFM visualization. Additionally, there is no information related to imaging parameters such as magnification, pixel size and its comparison between wholemount light sheet and confocal imaging. Many of the figures would be greatly enhanced by zoom insets to show the level of resolution and a comparison of resolution between the two methods. Can the same conclusion be reached using two-dimensional section imaging as it can using 3-dimensional imaging?

2) Given the complex nature of a regenerating limb, we consider of importance the biology behind the methods, more information is needed describing the rationale for the given experimental choices. In general, there is very little information shown for the methods. For example, macromolecule analogs were injected three hours before tissue harvesting. Why was this timepoint chosen? Is this time choice relevant for the additional analogs AHA or GlyNAz? Is there an optimization that the authors didn't mentioned? Similarly, the authors do not explain the use of TDE as a clearing agent versus other clearing strategies that they highlight in the manuscript. Is there an advantage or reason for this choice? The authors should clearly state if there is.

3) A key point of the paper is the simultaneous visualization and quantification of macromolecules. While the authors demonstrate that co-administration of macromolecule analogs is possible for simultaneous visualization, the further analysis doesn't exploit this important feature. We wonder if this method allows for identification of cells through immunofluorescence/immunohistochemistry together with the click-it macromolecule labeling. Did the authors attempt to immunolocalize a particular cell population? One particular question that we would like to see addressed is the quantification of RNA or protein synthesis in double labelled tissue (in volume). The authors may already have tissue that is double labeled.

4) How applicable can this method be for other tissues/organisms, or is it limited to more dense tissue (bone)? Have the authors attempted this technique on other organs? If it is envisioned to replace tissue sectioning, the authors should address whether the technique is adaptable to other tissues and model organisms. If generalizable, the associated supplementary tools and tutorial should also reflect this (e.g., the ImageJ macro currently prompts for a "blastema file").

5) The methods and rationale for the limb denervation experiments should be better explained. Specifically, why was a mock denervation not needed? In the absence of this control, could the change in DNA synthesis be due to the injury of the denervation, rather than an absence of nerves? Please also include more details on the time point chosen to denervate the limb, how the time point analyzed (24 hrs post denervation) relates to the timing of nerve degeneration and why such a small volume was analyzed. One possibility is that a small volume could bias the final histogram measurement. Did the authors consider analyzing two volumes in the blastema, for example, one proximal and one distal?

6) Figure 6 can show the power of the method, however, there is no statistical test to quantify the difference between the two experimental groups. This computational pipeline is giving numerical values to a biological process, it is worth then to analyse them. The graph in Figure 6 shows only the histograms of the 3 time points that the authors considered affected. It would be informative to know how the time points that show no change look in comparison. In general, it is challenging to interpret Figure 6, we suggest separating the histograms, or using violin plots for better visualization.
