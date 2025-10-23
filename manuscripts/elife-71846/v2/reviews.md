# Peer review - Round 1

Editors:
- Shella Keilholz, Emory University and Georgia Institute of Technology United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71846.sa0](https://doi.org/10.7554/eLife.71846.sa0)

The authors make a convincing argument that they have found an MRI-based biomarker for dopaminergic input into the striatum. Because the dopaminergic system is involved in neurodegenerative disorders such as Parkinson's disease and also in processing reward signals, the biomarker is likely to become widely adopted and enable new types of experiments in related fields. In this revision, the authors further demonstrate the specificity of the potential biomarker and its lack of sensitivity to head motion.


---

# Peer review - Round 1

Editors:
- Shella Keilholz, Emory University and Georgia Institute of Technology United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.71846.sa1](https://doi.org/10.7554/eLife.71846.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Mapping dopaminergic projections in the human brain with resting-state fMRI" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Shella Keilholz as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Michael Frank as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Georg Northoff MD, PhD (Reviewer #2); Finnegan J Calabro (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) A key assertion of the manuscript is that the biomarker is specific to the dopaminergic system. This assertion needs stronger support. Studies that show that the biomarker disambiguates between different neuromodulatory systems (e.g., serotonergic) are needed to address this issue. For example, existing data could be examined by putting the seed in the subcortical regions like Raphe nucleus and VTA/SN and then investigating their upstream functional connectivity (see Martino et al., 2020, Conio et al., 2020, and others). The results could be compared to the present DA-driven results including conjunction and exclusive masking.

2) Common confounds for resting state fMRI analysis (e.g., head motion) need to be better addressed in terms of how they affect the mode that serves as a biomarker. It is essential to be certain that the biomarker is not picking up motion differences between groups.

Reviewer #1 (Recommendations for the authors):

It was not clear to me how the modes for different parts of the striatum were combined. A brief explanation would be useful.

Have the authors looked at functional connectivity between areas that exhibit differences in the 2nd mode and their hypothesized targets? For example, if the area that exhibits differences as a function of alcohol use also show differences in functional connectivity to a target area that replicates previous studies, it would further strengthen the manuscript.

It would be informative to see if other modes are altered in PD. If they are not, it would suggest great specificity for the 2nd mode.

There’s an interesting difference between the overall correlation of DaT and the 2nd order mode in the putamen as compared to the caudate that should be discussed.

Any overlap between the tobacco and alcohol use group should be described.

Reviewer #2 (Recommendations for the authors):

– The connectopic mapping is based on functional connectivity and correlating time series. May be analysis of dynamic functional connectivity could enhance the validity of the data: if cortical regions show similar dynamic pattern int heir variability, it could be used to further specify the specificity of the cortical connectivity pattern of the striatum.

– May be a figure of the differential cortical connectivity patterns of the three modes (zero-first-, and second-order) (Figure 1) could be shown as that would reveal the cortical specificity of the striatal subregions which is biochemically relevant…

– As I understand the DaT SPECT subjects are different from the HCP subjects so you correlate different healthy subjects with each other…correct? If so, I would recommend at least some healthy subjects to have both SPECT and fMRI (beyond the PD subjects)…..even if a low number, it would increase the validity of the marker….this is important given that, as far as I can see in the tables, there is considerable inter-subject variability in the striatal data both SPECT and fMRI.

– Figure 3: where are the cortical connections in the three fMRI striatal modes? Do they correlate with the DaT SPECT striatal data?

– Also: the HCP sequences and scanning measures are not ideal to capture subcortical regions like the striatum including their subregions as they do not, as far as I recall, contain axial slices….. this could be mentioned as limitation…

– Statistically: the main results on this paper rely on correlation mostly Pearson. It would be nice to have that further solidified by using more robust regression analyses….

Reviewer #3 (Recommendations for the authors):

It is unclear to me how the topographic maps shown in Figure 1 are derived, and specifically how these relate to the spatial fits being performed separately for each region. I would have expected discontinuities in these maps at the regional boundaries, but the maps appear to vary continuously across the striatum, so some clarification on what these maps are representing relative to the per-ROI statistical surface odelling being performed would be helpful.

The resulting second order mode seems qualitatively similar to maps found in previous connectivity mapping approaches (e.g., Tziortzi et al., 2014). Some discussion about either consistency with previous approaches, or description of differences in what this method identifies, would be helpful. In particular, if the patterns are sufficiently similar, this would open the possibility of associating analyses performed using these other atlases for interpretations related to DA distribution. If there are differences, it would be interesting to discuss how these methods differ in the patterns they identify.

I’m confused by the description of a “lossless” SVD for dimensionality reduction (l 543). Presumably to attain a reduction in the matrix size, some proportion of eigenvalues are retained with the rest removed, rendering it lossy. Some clarification here, or information about what proportion is retained, would be helpful.

What is the rationale for using a scree test to choose the best TSM, rather than a less subjective AIC/BIC or similar? The selection of such complex models, in relatively small spatial regions (e.g., quartic model for caudate-Nacc) raises questions about how effectively extra coefficients are being penalized in this approach.

A citation is needed for this assertion: “as PD is known to affect the putamen region of the striatum before the caudate-Nacc region” (l. 215)
