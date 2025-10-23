# Author response - Round 1

Authors:
- Carl J Hodgetts ([ORCID: 0000-0002-0339-2447](https://orcid.org/0000-0002-0339-2447))
- Mark Postans
- Jonathan P Shine
- Derek K Jones
- Andrew D Lawrence ([ORCID: 0000-0001-6705-2110](https://orcid.org/0000-0001-6705-2110))
- Kim S Graham ([ORCID: 0000-0002-1512-7667](https://orcid.org/0000-0002-1512-7667))

## Response text

DOI: [10.7554/eLife.07902.019](https://doi.org/10.7554/eLife.07902.019)

1) The authors should reconsider the treatment of the surprising correlation between hippocampal deactivation and both fornix FA and task accuracy. In their reviews, Reviewer #1 suggested more explanation, while Reviewer #2 suggested that the results should just be presented as “surprising” without too much handwaving. Upon post-review discussion amongst reviewers, the consensus was that the discussion of should be retained but revised. Reviewer #3 suggested acknowledging the broader literature, noting that baselines are difficult to define for the hippocampus.

To address these points, the relevant section in the manuscript has been rewritten as follows:

“The reported association between fornix microstructure (FA and to a lesser extent MD) and scene-related BOLD activity in HC was in the opposite direction to that observed between ILF microstructure and face selectivity in PrC/FFA, with fornix microstructure positively correlating with HC scene deactivations. […] One possibility, therefore, is that sparser blood supply in the HC (e.g., lower capillary density; Borowsky and Collins, 1989) leads to a decoupling between neuronal activity and BOLD, that is, where oxygen metabolism exceeds local blood flow.”

2) More discussion of the anatomical inputs to the hippocampus should be added (Reviewer #2, point 4).

In response to Reviewer 2, we have revised the manuscript as follows:

“[…] the reciprocal interplay between HC and surrounding neocortical and subcortical regions (Aggleton et al., 2015; Saunders and Aggleton, 2007) – that is afforded partly by fornical connections – appears critical for the formation of flexible spatial representations in the HC (i.e., those that maintain the coherent layout of a spatial environment across multiple viewpoints). […] Interestingly, this may also account for the moderate, though non-significant, association between size oddity and fornix microstructure (see Results).”

3) A direct statistical test should be performed to test whether the brain-behavior correlations are significantly greater for the fine-grained perceptual tasks vs. the simple featural task (Reviewer #2, point 4).

Direct statistical tests (Steiger z-tests) comparing the brain-behaviour correlations for (1) scene vs. size, and (2) face vs. size, were initially presented in Supplementary file 1. These are still reported and have now been moved into the main manuscript:

“While none of the microstructural measures obtained, in either pathway, were significantly associated with performance in the difficulty-matched size oddity condition, there were, as reported above, small-to-moderate one-tailed trends between fornix/ILF MD and size oddity (Figure 1—figure supplement 1). A Steiger Z-test comparing these coefficients revealed a significant difference between the face and size oddity correlation for ILF MD (z (26) = 2.05, p = 0.02). The difference between the size and scene oddity correlations for fornix MD did not differ significantly (z (26) = 0.94, p = 0.17).”

Based on the suggestion by Reviewer 2 (point 4), we conducted partial correlations to see whether the significant relationship between face/scene oddity and fornix/ILF MD remains when size oddity is controlled for – i.e. to show that white matter microstructure is predictive of face/scene oddity over and above its contribution to lower-level visual discriminations. When size oddity is controlled for, we still observe significant associations (one-tailed) between scene oddity and fornix MD (r = -0.38, p = 0.02, 95% CI [-0.61, -0.08]), and face oddity and ILF MD (r = -0.53, p = 0.00, 95% CI [-0.61, -0.08]). This additional analysis is now reported in the Results section.

4) Further justification is needed for the choice of regions based on probabilistic atlases rather than direct contrasts between faces and scenes (Reviewer #3, point 2). In addition, the authors should acknowledge that connectivity only correlates with the contrast of scenes vs. rest (not scenes vs. faces).

The reason for this is three-fold: firstly, probabilistically defined ROIs were used to ensure consistency in the analyses conducted between regions. Defining functional ROIs (while preferable in certain contexts) would have inevitably led to variability in the contrasts and thresholds used to identify clusters in individual subjects, particularly given variation in signal-to-noise across medial temporal lobe and temporo-occipital fusiform regions. This leads us to the second reason, namely that an anatomical ROI approach avoids the loss of individuals from our analysis (see also Lee et al., 2008; Barense et al., 2010; Mundy et al., 2013), which would reduce the overall power of the experiment, and would also lead to potential bias in the analysis by only including those participants that, for example, show significant BOLD increases for faces versus scenes. Finally, this method was chosen to ensure non-circularity in our BOLD-behaviour and mediation analyses – i.e. we wanted to ensure that ROIs were independent of the BOLD signal change data that were analysed as part of the mediation analyses (Kriegeskorte et al., 2009).

The finding that fornix connectivity only correlates with scenes vs. rest (not scenes vs. faces) is now acknowledged in the Discussion section.

5) The reviewers wondered what happened in other areas including PPA (Reviewer #2, points 2 and 3) and other nodes of the scene network (RSC, TOS). Some suspected that these areas may have been analyzed but didn't show interesting patterns and thus weren't included. If so, a brief mention would be helpful along with an acknowledgment that the data for scenes and the fornix have less specificity than those for faces and the ILF. If not, the authors should consider including these analyses. They are not strictly required as eLife avoids asking for extensive additional analyses unless they are necessary for the conclusions. However, since all three reviewers agreed in discussion that this analysis would be beneficial, the authors should consider including them.

We did not look at this initially as our focus was on characterising the association between category-selective BOLD and microstructure in only those medial temporal ROIs that are directly connected to our tracts of interest. Based on the reviewers’ suggestion – that fornix microstructure may be associated with BOLD in other scene-selective cortical regions (RSC, PPA, and TOS) – we conducted an additional voxel-wise analysis within ROIs of the RSC, TOS and PPA. To be consistent with analyses presented in the manuscript, we used anatomically-defined, independent ROIs for the PPA (posterior parahippocampal gyrus from the Harvard-Oxford Cortical Atlas), RSC (Brodmann Area 29 dilated by a single voxel; see Bluhm et al., 2009) and TOS (a probabilistic mask from the ICBM Sulcal atlas; Mazziotta et al., 1995). Using the same statistical thresholds presented in the paper, no significant clusters were found that showed a significant positive association between scene-selective BOLD (S > F, S > rest) and fornix microstructure (MD or FA) in any of the additional scene-selective ROIs.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

You've addressed almost all the points well. There's just one small revision the Reviewing Editor would like to request. Regarding effects in RSC, PPA, and TOS, the previous decision stated: “Some [reviewers] suspected that these areas may have been analyzed but didn't show interesting patterns and thus weren't included. If so, a brief mention would be helpful along with an acknowledgment that the data for scenes and the fornix have less specificity than those for faces and the ILF.” You've now done the analysis and found no significant effects but it doesn't seem to be mentioned in the manuscript. Because it was a common question from multiple reviewers and you did the work of the analysis, please add a brief mention it in the manuscript.

A brief mention of this analysis has now been added to the Results and Methods sections of the manuscript. These results are described as follows:

“To test whether fornix microstructure is associated with scene-selective BOLD in other scene-selective cortical regions (Epstein, 2014), we conducted an additional voxel-wise analysis within anatomically-defined, independent ROIs sampling the posterior parahippocampal gyrus (PHG), retrosplenial cortex (RSC) and transverse occipital sulcus (TOS; see Methods). No significant clusters were found that showed a significant positive or negative association between scene-selective BOLD (S > F, S > rest) and fornix microstructure (MD or FA) in any of the additional scene-selective ROIs.”
