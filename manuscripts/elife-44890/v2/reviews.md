# Peer review - Round 1

Editors:
- Chris Honey

Reviewers:
- Daniel S Margulies, Max Planck Institute for Human Cognitive and Brain Sciences Germany
- Jakob Seidlitz

## Review text

DOI: [10.7554/eLife.44890.020](https://doi.org/10.7554/eLife.44890.020)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The relationship between spatial configuration and functional connectivity of brain regions revisited" for consideration by eLife as a Research Advance. Your article has been reviewed by Daniel S Margulies (Reviewer #1) and Jakob Seidlitz (Reviewer #2), and the evaluation has been overseen by Chris Honey, the Reviewing Editor, and Richard Ivry as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary

This manuscript by Bijsterbosch and colleagues extends their prior work describing the impact of spatial confounds on the variation in functional connectivity across individuals, and its connection to variation in behavior. Here, the authors test several specific hypotheses to account for their prior findings. They do this by examining two axes of potential bias: i) algorithms to derive spatial and temporal functional connectivity domains, and ii) methods for generating "soft" (data-driven) and "hard" (a priori) parcellations. Furthermore, they provide both empirical evidence and quantitative support via simulations in support of these investigations. Ultimately, the authors conclude that inter-individual behavioral variability is best explained by the spatial overlap between networks, which affects the extraction of soft parcellations. The manuscript is clearly written, and the analyses and results are presented in a manner that makes the logic of the study straightforward.

Overall, the reviewers were impressed by the rigor and logical progression of the manuscript, and the effort to include results from different surface alignment algorithms as well as a comparison with volumetric registration. The reviewers also appreciated the discussion and comparison of dual regression methodologies versus PROFUMO, and the clear differences in assumptions that are made with each.

Essential revisions

1A) The maps of network overlap, presented in Figure 4A, appear spatially consistent with prior findings of the relative degree of cortical folding (Toro et al., 2008). As cortical morphology may impact on functional connectivity (for example, differences between adjacent sulci and gyri), is it possible that the network overlap results are driven in part by cortical morphology? This issue is distinct from the point raised in the discussion regarding network interdigitation, but the impact of morphology on the results could be the same. A post hoc test of whether measures of cortical surface area and volume account for the brain-behavior relationship observed in the CCA analysis might be sufficient to assess whether this concern is relevant.

1B) Another possible interpretation of the topography in Figure 4: the areas of most overlap appear to be in areas that have been shown to be prone to problems in cortical reconstruction (mostly due to excess head motion). In light of the lack of influence of surface registration method (as discussed above and in the manuscript), can the authors speculate/discuss this pattern of overlap?

2) The Discussion mentions 'primary visual cortex' (V1) as being an area of high overlap (Figure 4). However the regions appear to be located predominantly within higher visual areas along the lateral wall (rather than within the calcarine sulcus). Please justify or correct this claim.

3) As the core brain-behavior finding from the CCA analysis is from Snet PFM, would there be any way to visualize the pattern of spatial overlap associated with the components (along the lines of the figures shown in Figure 4A)? This might help in interpreting the results in the context of prior findings.

4) The Discussion mentions that ongoing work explores why the brain-behavior relationships are also observed when hard parcellations are used (e.g. the Yeo et al. and Glasser et al. parcellations). The authors speculated that: "it is possible that [hard] parcellation methods are therefore unable to isolate overlap into a distinct parcel (which would allow results to be unbiased, particularly at a sufficiently high dimensionality), and instead parcel boundaries in regions of overlap are determined by the network with the strongest amplitude (or lowest cross-subject variance), leading to mixing of extracted timeseries". Are the authors now able to confirm this speculation? More generally, can the authors explain why the brain-behavior variance explained is so similar when using hard parcellations and when using dual regression approaches (Figure 1A of Bijsterbosch et al., 2018)? Should this be the case if the dual regression methods are subject to these spatial overlap / spatial independence effects, while hard parcellations are not?
