# Peer review - Round 1

Editors:
- C Daniela Robles-Espinoza, International Laboratory for Human Genome Research Mexico

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.50267.sa1](https://doi.org/10.7554/eLife.50267.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

CNApp is an interactive tool that allows users to visualise whole-genome copy-number profiles from data generated from a number of different platforms, and facilitates performing different analyses such as computation of copy-number alteration scores and sample classification to aid biological interpretation of results. We think it is of utmost importance to provide users with tools for interpreting large amounts of data in an easy manner, and here it is done supplying extensive support for how to use such software. We believe that bench biologists and medical professionals will be interested in this work, as well as bioinformaticians and data analysts.

Decision letter after peer review:

Thank you for submitting your article "CNApp: quantification of copy number alterations in cancer and integrative analysis to unravel clinical implications" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Kathryn Cheah as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this manuscript, Franch-Expósito et al. describe a new app, CNApp, that facilitates the analysis of large datasets of copy number variation. As a proof of principle, they apply it to TCGA SNP-chip datasets and do three different analyses (overall TCGA, hepatocellular carcinoma and colon cancer). Overall, the reviewers find that the app seems to work, and that the analysis performed is reasonable. In broad terms, they show concordance with other published results, with some differences. However, a number of essential revisions must be performed before the work can be accepted for publication.

Essential revisions:

1) Two of the reviewers mentioned problems when using CNApp in different browsers (one mentioned problems with Safari and Firefox, the other one with Chrome and Safari). Please make sure that the app works with all major browsers (preferably), or at the very least indicate the preferred settings for using it.

2) The major advantage that CNApp would offer is the ability to perform large-scale analyses of copy number variation easily for non-bioinformaticians. However, in the current manuscript it is only compared against GISTIC2.0, but even though there seem to be substantial differences between the results of both CN callers, no effort seems to have been made to indicate that CNApp's calls are more accurate, or why users should trust its output. Please compare the results of CNApp not only against GISTIC2.0 but also against other copy number callers, such as CoNVaQ (Larsen et al., 2018) and CNspector (Markham, Sci Rep, 2019), and offer an analysis of the accuracy of CNApp. The use of simulated datasets is suggested for this purpose (For example, see Mermel et al., 2011).

3) Please justify the boundary between focal and broad CNAs, and why that particular boundary was chosen. On the same note, a BCS value of 4 is suggested to be able to distinguish between tumour subtypes in section "Classification of colon cancer according to CNA scores and genomic regions", however no validation in any external datasets is shown to indicate that this is a reliable value. Can the authors please explain if we should expect to see this replicated in other datasets?

4) Please justify the choice of a random forest classification model, and offer a clear explanation of when this analysis is suitable. The ability to "establish associations between the burden of genomic alterations and any clinical or molecular variable" in a user's dataset could lead to spurious correlations and false positive results, given that the tool is aimed at non-experts.

5) Please explain how the CNApp tool deals with whole-genome duplication events.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "CNApp, a tool for the quantification of copy number alterations and integrative analysis revealing clinical implications" for further consideration by eLife. Your revised article has been evaluated by Kathryn Cheah (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

1) In the subsection “, please change the word 'capacity' for 'ability'.

2) Please add labels for the Y-axis in all three plots in Figure 2A.

3) Please be more specific when describing the data shown in supplementary files, adding a description of what columns mean.

4) In legend for Figure 4B, do you mean Wilcoxon rank sum test?

5) In the third paragraph of the subsection “Classification of colon cancer according to CNA scores and genomic regions”, do you mean Figure 4—figure supplement 1E? It is not clear that Figure 4—figure supplement 1F refers to what is specified in the text.
