# Peer review - Round 1

Editors:
- Lilianna Solnica-Krezel, Washington University School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55913.sa1](https://doi.org/10.7554/eLife.55913.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This work develops an image analysis pipeline for extracting and analyzing cell-based data using unsupervised machine learning to find correlations between cell shape, orientation, position, and gene expression. Timelapse imaging of the developing zebrafish lateral line organ is used as an example of this approach. The authors develop an approach to statistically represent cell shape in both a cell-based and tissue-based reference frame to construct a feature space for machine learning. This representation is used to build an atlas integrating multiple cellular markers and linking them to cell type archetypes. This tour de force pioneering study is expected to open an avenue to a more effective analysis of "data-rich" microscopy data, which provides one of the most important yet challenging windows on unfolding of the embryogenesis and organogenesis.

Decision letter after peer review:

Thank you for submitting your article "An image-based data-driven analysis of cellular architecture in a developing tissue" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Marianne Bronner as the Senior Editor The following individual involved in review of your submission has agreed to reveal their identity: Ajay B. Chitnis (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor, who also read the manuscript and has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

This work develops an image analysis pipeline for extracting and analyzing cell-based data using unsupervised machine learning to find correlations between cell shape, orientation, position, and gene expression. Timelapse imaging of the zebrafish lateral line is used as an example of this approach. The authors develop an approach to statistically represent cell shape in both a cell-based and tissue-based reference frame to construct a feature space for machine learning. This representation is used to build an atlas integrating multiple cellular markers, such as F-actin or Golgi organelle, predict smFISH data and, is linked to cell type archetypes. This tour de force pioneering study is expected to open an avenue to very effective analysis of "data-rich" microscopy data, which provides one of the most important yet challenging windows on unfolding of the embryogenesis and organogenesis.

Essential revisions:

Whereas the two reviewers and the managing editor were in agreement about the significance and broader applicability of the methods you developed, they differed in their view on the manuscript presentation.

One reviewer thought that the paper is well laid out, and despite its complexity, the logic and significance of each step in the analysis made fairly accessible to a diverse reader audience. The authors describe the challenges of data extraction, data integration and data interpretation. They address these challenges by describing how high-resolution 3D images collected with AiryScan fast mode confocal microscopy were first segmented with automation. Then a four-step process was implemented to extract and integrate information from these images.

However, the second reviewer thought that this paper is a bit of a "diamond in the rough". It was not easy to understand what the authors were doing after reading the title, Abstract, Introduction, or first section of the Results. And it was not until the reviewer read the remaining results that they got excited that this was a novel, general, and up-and-coming approach. Having read the manuscript, the reviewing editor agrees with this reviewer that revising the manuscript with the goal of increasing its clarity and accessibility would significantly improve its impact.

Therefore, we recommend that you should re-work the first half of the paper considering the following points with the goal of better communicating your approach to a biology audience. Be 1) more specific, 2) less jargony, and 3) describe goals with multiple words. Moreover, more detail about the patio-temporal details of what was imaged should be added in the Results section. The methodological approach is described as a tool for studying organogenesis, a highly dynamic process. Yet, only from the Materials and methods section one can learn that embryos at 30-34 hpf (and thus practically a single time point) have been imaged. Please, indicate whether a primordium at a specific position in the embryo was imaged. Also, the authors could more clearly describe the feature integration experimental setup, especially whether integration of signals like F-actin, or Golgi apparatus requires simultaneous imaging of the membrane signal. Consulting the manuscript with non-specialists would be also advised during the revision process.

In addition, as reviewers point out, one is a little disappointed that despite the elegant analysis, what the authors discovered, with some minor exceptions, for the most part confirmed what we knew to a large extent about morphogenesis in the pLLP. Therefore, perhaps more exploration of differences between cells along the inside out axis rather than along the longitudinal or DV axis might have provided some additional important distinctions between cells in terms of how they might correlate with Nuclei, Actin or golgi distribution. Such new insight would underscore the power of the approach and its impact in the field.
