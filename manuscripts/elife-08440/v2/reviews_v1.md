# Peer review - Round 1

Editors:
- David C Van Essen, Washington University in St Louis , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.08440.021](https://doi.org/10.7554/eLife.08440.021)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for submitting your work entitled “Parkinson's disease targets an intrinsic brain network” for peer review at eLife. Your submission has been favorably evaluated by Timothy Behrens (Senior Editor), a Reviewing Editor, and two reviewers.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

This study is a very interesting and well thought out multimodal analysis of brain atrophy and functional connectivity in a multi-site cohort of de novo PD patients. It benefits from a (multi-centric) large cohort of rare de novo PD patients and from the methodological approaches used for the analysis of local atrophy (namely DBM+ICA). The fact that the authors also looked for a spread of the disease via structural and functional networks (using both diffusion imaging and [resting-state] fMRI) is another strength of this study. It provides intriguing evidence in support of the hypothesis that atrophy initiated in or near the substantia nigra may spread to other subcortical and cortical regions in a pattern that at least to some degree reflects network connectivity as revealed by resting-state fMRI.

Both reviewers were enthusiastic about many aspects of the study, but both raised substantial concerns that are largely complementary to one another. Hence, we consider the manuscript to be potentially acceptable, but only after a major revision that addresses the key points raised by the reviewers.

Some of the recommendations would entail significant additional analysis, and we do not insist that all of them necessarily be carried out. For example, suggestion #8 is to carry out the rsfMRI analysis of functional connectivity using the freely available HCP dataset. We encourage you to consider this, but it is not essential for the revised manuscript. For the other recommended re-analyses, including #1 (seed-based analysis), #11 (higher-dimensional ICA decomposition) and #13 (FLICA analysis) it is important that you either follow the recommendation or provide a cogent response as to why this was not done.

Essential revisions:

1) A strength of this paper is that multiple different methods were used to measure connectivity patterns in normal subjects (resting state seed based, resting state ICA, DTI). A relative weakness is that only one method was used to define the atrophy pattern in PD, the central finding in the paper. There are numerous techniques for detecting and quantifying atrophy, so why did the authors choose the one they did (DBS). Do they get similar results using an alternative technique? Similarly, they only used one method to identify the atrophy pattern (ICA). Why not use a seed based approach to identify regions whose atrophy correlates with atrophy in the SN? The authors do not need to perform every methodological possibility, but the reasons for their choices need to be more clearly justified. Further, they should make it clear when and why their methods deviate from prior work with similar goals (e.g. Bill Seeley's work).

2) Results are a bit overstated at times which could detract from the importance of the findings. The authors convincingly show that a specific pattern of atrophy is related to PD, aging, dopamine binding in the striatum, and UPDRS score. This alone is very worthy of publication. Whether this atrophy network is an “intrinsic brain network”, as defined by resting state fcMRI, or validates the “network spread model” of PD, this is indeed an important question, but it is weakly supported by the present data. The authors may be better served to focus on their strongest findings and relegate the others to the Discussion.

3) The authors put great emphasis on the fact that their atrophy pattern matches an “intrinsic connectivity network”, including making this the title, but the data supporting this claim are weak. Specifically, the criteria for a “match” are arbitrary. The authors chose a threshold of r = 0.25. If they had chosen a threshold of 0.35 instead, we would conclude that the atrophy pattern fails to match any intrinsic connectivity networks. Rather than concluding that the atrophy matches or fails to match an intrinsic connectivity pattern, the authors could make better claims on comparative matching. In other words, they can claim that their atrophy pattern matches a specific network better than other atrophy patterns and they can conclude that their atrophy pattern matches a specific network better than other networks.

4) It is a bit unclear whether the PD-ICA network (Figure 1) shows the full ICA component identified combining PD and controls or if only those voxels within the component that showed significant differences between PD and controls. I believe it's the former, but this should be made a bit clearer and it would be helpful to also show that latter. What part of this network shows the greatest difference between PD and controls?

5) There are concerns regarding the correlations across the 135 ROIs. The authors already have atrophy and connectivity measures at the voxel level so why not do the analysis across voxels? By combining different pieces of various brain atlases with their own hand-drawn atlas of brainstem structures, the authors introduce the possibility of bias into their ROI analysis. Is there no suitable existing atlas such as the WFU-Pickatlas? If the authors must use a custom atlas, some criteria regarding which brainstem structures were included versus excluded are needed.

6) Atrophy in the PD-ICA, SBR, UPDRS, and age all appear to be somewhat correlated. It would be interesting to know which are independently correlated after accounting for the others using a multivariate analysis.

7) In testing whether the PD-ICA overlaps with an intrinsic connectivity network, the authors include comparison to a meta-analysis of regions responding to stimulus value. Although potentially interesting, this map should not be referred to as an “intrinsic connectivity network”.

8) The resolution used for the rsfMRI connectivity analyses in healthy young subjects (both seed-based and “propagation model”) is of 3.5 mm isotropic, which makes it impossible to distinguish (a seed in) the substantia nigra from the subthalamic nucleus, and probably also the red nucleus. This might explain why the authors found that the latter two structures were as likely to be propagators as the substantia nigra.

To alleviate these major concerns, the authors should probably re-do these analyses with an improved resolution dataset, which is for instance readily available in the HCP in a young and healthy population (∼500 subjects at 2 mm isotropic).

9) The authors should explain clearly how they manually defined their ROI in the substantia nigra and other small structures (only names of anatomical atlases are specified in the Methods), and extensively discuss the inherent limitations coming with such a resolution for both their seed-based analysis and propagation model.

10) Similarly, in the subsection “Spatial Analysis of PD-ICA network”, it is not clear that the location of the T1 weighted results obtained from DBM can be so precisely identified (substantia nigra vs. subthalamic nucleus, PPN, bed nucleus of the stria terminalis, etc.), so the authors should make this point clear in their manuscript.

11) The spatial cross-correlation between the 3 different networks seems to some extent arbitrarily set up at |r|>0.25. The authors should possibly report whether other significant cross-correlations were found for |r|<=0.25. The authors might also want to use the higher dimension ICA decomposition (d=70 instead of d=20) provided in Smith et al., 2009, as their high dimension ICA yields more specific basal ganglia networks.

12) Regarding the DBM analysis, the use of ICA is quite ingenious, especially considering the multi-centric aspect (16 sites, 3 different scanners) of this imaging cohort. Could the authors please specify whether they found site-specific or scanner-specific artefactual ICs in their results? What about a direct comparison of their DBM maps between the 2 populations? Presumably, this provided no significant result, which therefore sends a strong methodological message about an optimised approach for multi-centric T1 weighted volumetric studies.

13) There is concern about the specific use of MELODIC on structural data. The reason is that MELODIC is “tuned” to identifying sparse data and is inherently more suited for fMRI rather than structural data. It can therefore be the case that some more “global” components explaining the largest variance across the subjects can be missed sometimes. It seems unlikely here as the inputs used for TICA were DBM maps and not GM maps, and the main IC is reassuringly highly relevant to the pathology studied. It might be worth however for the authors to run FLICA (another data-driven ICA tool available in FSL) on their data to make sure results are similar.

14) Regarding their correlations with clinical measures, could the authors maybe justify in the manuscript why they have not used the MoCA and other parts of the UPDRS than part III, or alternatively carry out these correlation analyses?

15) Could the authors please provide the list of best propagators using diffusion imaging (similar to Table 3)? It would also be interesting to discuss the strong negative correlations reported in Table 3.
