# Peer review - Round 1

Editors:
- Saad Jbabdi, University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70119.sa1](https://doi.org/10.7554/eLife.70119.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

The manuscript introduces a new tool – BigBrainWarp – which consolidates several of the tools used to analyse BigBrain into a single, easy to use and well-documented tool. The BigBrain project produced the first open, high-resolution cell-scale histological atlas of a whole human brain. The tool presented here should make it easy for any researcher to use the wealth of information available in the BigBrain for the annotation of their own neuroimaging data. This is an important resource, with diverse tutorials demonstrating broad application.

Decision letter after peer review:

Thank you for submitting your article "BigBrainWarp: Toolbox for integration of BigBrain 3D histology with multimodal neuroimaging" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Saad Jbabdi as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Tamar Makin as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Emma C Robinson, PhD (Reviewer #2); Roberto Toro (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions: (see reviewer comments for details)

1) More in depth discussion of the limitations of having a single brain and the implications this has in utilising BigBrainWarp.

2) More details/clarifications on the registration approaches

Reviewer #2 (Recommendations for the authors):

I think this is a great resource and so I spent some time looking into the installation and running of the pipeline and in general I find the instructions very clear. This was even after having to install the pipeline from source as docker isn't working for me on MacOs Big Sur currently.

In terms of the paper specifically I had some initial trouble following the motivations, past research and tutorial experiments. As said previously the goals specific to this paper could be clearer in the abstract and Figure 1G is not clearly explained. For the Introduction, first paragraph, what is meant by ' the mergence of histology with computational neuroscience supports more observer independent principles?'

On 'staining profiles and derived features' I didn't follow the section on optimising smoothing and number of surfaces. What is meant by 'evaluated […] number of profile peaks for each combination' and comparing at 'various distances along the Bigbrain surface mesh' in terms of steps? I don't really find the supplemental figure on this helpful either – I can't interpret the grey bars in A.

In terms of the results, I think the examples used for the tutorials show broad applications and the detailed resource for running them (on the website) is great. I did have some trouble at first understanding what was done, however. So I recommend going back and writing in a more lay way. For example, tutorial (1) Figure 3C -its not immediately apparent whether this is from one subject or a combination. It took me some time to understand that the cortical surface colour map represents the trend from the plots of functional connectivity across the iso-to-allocortex axis. For tutorial 2 the text just says '(i) and (ii) are computed with BigBrainwarp' without stating what they are. The matrix in (ii) could have its dimensions labelled (i.e. regions x regions); and it isn't made clear (iii) is the eigenvalues and in the figure caption these are called 'principle components' but the decomposition is not PCA.

For tutorial 3 I think it would be wise to stress more carefully the impact of subject-specific topographic variation and the possible effect it has on the results – as mentioned in the public summary I think it may relate or interact with the findings of higher variation of the frontal parietal networks. Where topographic or cortical variation is mentioned it may be worth citing some papers with evidence for it e.g. HCP parcellation paper (Glasser Nature 2016) or Ruby Kong's 2021 Cerebral cortex paper, or Evan Gordon's parcellation papers.

Reviewer #3 (Recommendations for the authors):

The manuscript presents BigBrainWarp, a tool for facilitating the integration of BigBrain data for the analysis of neuroimaging data. The rationale for this is well described and the manuscript provides compelling illustrative applications.
