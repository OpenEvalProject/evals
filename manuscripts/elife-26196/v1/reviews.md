# Peer review - Round 1

Editors:
- Tatiana Pasternak, University of Rochester , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.26196.018](https://doi.org/10.7554/eLife.26196.018)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "A Hierarchical, Retinotopic Proto-Organization of the Primate Visual System at Birth" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and David Van Essen as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Wim Vanduffel (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The manuscript provides a compelling demonstration of retinotopic functional topographic organization of the visual system in the newborn macaque brain. It shows for the first time that this organization contains adult-like hierarchical structure and does not require visual experience. The reviewers were enthusiastic in supporting the work, emphasizing its high quality, novelty, thorough analysis of the data and excellent writing.

However, the reviewers raised a few issues that should be addressed before the paper is accepted for publication. While these issues are not major, addressing them will undoubtedly improve the manuscript and its accessibility.

Essential revisions:

In response to Reviewer 1:

1) Please clarify Figure 3 and add the actual r-values in Figures 2, 4, and 5.

2) Address the comment about the use of the term "Spatial pattern correlations".

3) Clarify the sentence in the subsection “Retinotopic organization in newborn” starting with "these correlations likely reflect…"

4) If possible, address the question whether the newborn structural connectivity revealed by the functional connectivity analysis is different when performed in adults.

In response to Reviewer 2:

1) Address the lack of visually-driven activity raised by this reviewer.

2) The reviewer questions the validity of scaling the newborn brain without applying non-rigid registration. Please address.

3) Please explain the use of the "novel nomenclature" (PITd/PITv/ OT/aPIT).

4) Please provide more details of the fMRI experiments, with the exact description of each fMRI run, numbers of images acquired. Were all data analyzed? If not what were the exclusion criteria, etc.

Reviewer #1:

Arcaro and Livingstone present here a project investigating the development of retinotopy longitudinally in two infant and adolescent macaques. The authors employ functional connectivity of voxel timeseries to examine the extent to which arealization and retinotopy has emerged in macaques ~10 days old. They demonstrate that interhemispheric functional connectivity is capable of distinguishing different visual areas, and that a voxel's connectivity profile to the contralateral hemisphere well-matches its position in its respective hemisphere. They furthermore demonstrate that the functional connectivity during infancy already contains the hierarchical structure of adulthood and that this retinotopy may serve as a scaffold on which later category-selective regions emerge.

Overall, the study is thorough and very well done. This project is novel in that it extends our understanding of visual cortex organization into a very early developmental timepoint, and across the entire visual cortex. It also makes the important observation that regions of cortex that will later exhibit category-selectivity have a functional connectivity bias to certain eccentricity bands that precedes their category-selectivity. Retinotopy has for some time been a proposed organizational principle of high-level visual cortex and this study nicely offers strong evidence in its favor. I recommend this study for publication.

I have only a few minor comments and questions for the authors to address.

Subsection “Arealization of newborn visual cortex”: what is the t value associated with r values?

For Figures 2, 4, and 5, please put actual r-values and not min max on the colorbars.

It took some effort to understand what was going into Figure 3. A schematic illustrating the procedure might help. Below I describe what I think is going on. If it's wrong then the text might need clarification:

You correlate a voxel with the mean signal from each area in the other hemisphere. This gives you a between-hemisphere connectivity profile (BHCP). Separately, for each area in the other hemisphere you derive the areal correlation profile (ACP), which is an area's correlation with each other area in the ipsilateral hemisphere. You then take the voxel's between-hemisphere connectivity profile and correlate it with the ACP of an area in the other hemisphere, and then you color it according to "how much its profile looked like that area's profile" and you do this in a voxel for each area giving you Figure 3, which is why a voxel can take on different values in each map depending on which area its BHCP is being correlated with. However, a voxel will have a BHCP vector of length N (N=number of areas), however an area with will have an ACP vector of N-1 because you can't correlate it with itself. Did you just exclude that point in the vector when correlating? Or have I misunderstood something?

The phrase "spatial pattern correlations" is misleading: the pattern of activity in V1, for example, is not being correlated with anything. A better term would be something along the lines of profile correlation, since you're correlating profiles of connectivity.

In the subsection “Retinotopic organization in newborn”: what does this mean "these correlations likely reflect the underlying topographic organization within each area, not solely mirror symmetrical point-to-point connections between hemispheres"? Different quadrants don't have point-to-point connections, right? Except for maybe stitching together of the vertical meridian they share, is that what you mean?

The analysis and result in Figure 6 is striking. However, I'm curious to know what is the outcome of functional connectivity analysis done during infancy when repeated in adulthood. Is the connectivity structure unchanged, or is there a refinement of the connectivity structure? Either way the result is will be informative. If the adult functional connectivity looks closer to the retinotopic mapping data, then that suggests that inherent connectivity is refined with development, which is interesting. However, it functional connectivity remains the same as it was in infancy, it suggests that the connectivity provides a scaffold on which later retinotopic maps develop.

Figure 8 is very nice! I'm satisfied with it as is. A future analysis might be to make a model relating cycles-per-degree (CPD) tuning in the infant data to the population receptive field (pRF) size of a voxel in the adult data. That will enable using independent data in infancy to determine if one can predict the pRF size in adulthood within each voxel. This could provide strong evidence supporting the hypothesis that CPD is related to pRF size.

While I recognize this is beyond the scope of the current paper, it would be interesting in the future to try and estimate the population receptive field of each voxel as a weighted sum of timecourses from voxels in V1 or prior visual areas. Using the known transformation of the visual field to V1, one then could use this weighting to derive the pRF of every voxel in subsequent areas and estimate the pRF size and eccentricity and then compare it to adult data. Might be a nice future direction.

Reviewer #2:

Based on monkey fMRI data, Arcaro and Livingstone showed that the newborn visual system contains a topographic organization reflecting that observed in adult macaques. This proto-organization emerges before the development of face selectivity and they propose that it provides a scaffold for the development of the fully-developed visual system, including category selective patches.

This is a very well written manuscript based on a data set that is exceedingly challenging to obtain. I truly commend the authors for this achievement. The analyses are state-of-the-art and well-done. I truly enjoyed reading this manuscript that conveys a very important result which is difficult/impossible to obtain without whole-brain imaging. This message should be of interest to a broad readership not restricted to vision scientists – as the authors may have discovered a general developmental principle. I only have a few comments that should be taken into account before I can formally recommend publication for eLife.

1) An important (though not critical) result is the lack of visually-driven activity in cortex in newborns while rest correlations between V1 and extrastriate cortex are already profoundly present. Visually-driven activity becomes strong at an age of >30 days. I've several questions with regard to this finding:

A) The two measures are fundamentally different (regression versus correlation), which required quite different pre-processing steps. Did the authors consider age-dependent differences in the hemodynamic response that may explain this result? This could affect the regression analysis but not the correlation analysis -and it could explain the difference in visual responses between day 10 and 30. This strange GLM finding also conflicts with studies showing that many neurons show already stimulus selectivity around the time of natural eye opening, although weaker than in adults.

B) A mutually non-exclusive explanation may be that the newborns simply closed their eyes inside the scanner (due to anxiety?) – as it must have been their first time in a rather obnoxious environment for them. Were eye-movement recordings analyzed in these very young infants?

2) The authors scaled the newborn brain by 130% relative to match it with the older brain and non-rigid registration was not applied, as far as I can see. How confident are the authors that this procedure is valid? Most results hinge on the back-mapping of maps acquired at an older age to the newborn cortex, so this is an important analytical step that requires validation. Why not adding non-rigid registration procedures?

3) I'm puzzled why the authors decided to use a novel nomenclature for areas that have been described previously. Apparently, previously described OTd (Janssens et al. and Kolster et al. 2014) corresponds to the new PITd (present manuscript) and previous PITd with aPIT (present manuscript). There is no obvious reason to confuse the readership. New areas PITd/PITv/ OT/aPIT is supposed to form a cluster with a shared foveal representation, but the same holds true for V4A, PITd, PITv, and OTd as described in Janssens et al. The data presented in the present manuscript are not detailed enough to defend a new nomenclature.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A Hierarchical, Retinotopic Proto-Organization of the Primate Visual System at Birth" for further consideration at eLife. Your revised article has been favorably evaluated by David Van Essen (Senior Editor), a Reviewing Editor, and two reviewers.

The manuscript has been improved but there is a remaining issue that needs to be addressed before acceptance, as outlined below:

1) Please address the request from reviewer 1 to provide functional connectivity analysis in the older monkeys to enable the comparison with baby monkeys. This request was supported by reviewer 2, who in response to this request commented as follows: "Although the interpretation of the current data set does not depend on the additional analysis, it will considerably strengthen the paper".

Reviewer #1:

In this revision, the authors addressed most of the comments raised in the original review. Overall, the paper is strong and of interest for the readership of eLife. However, there is one remaining major concern.

In the prior review, one of the main concerns read: "The analysis and result in Figure 6 is striking. However, I'm curious to know what is the outcome of functional connectivity analysis done during infancy when repeated in adulthood. Is the connectivity structure unchanged, or is there a refinement of the connectivity structure? Either way the result is will be informative. If the adult functional connectivity looks closer to the retinotopic mapping data, then that suggests that inherent connectivity is refined with development, which is interesting. However, if functional connectivity remains the same as it was in infancy, it suggests that the connectivity provides a scaffold on which later retinotopic maps develop".

The authors replied "We are presently working on tracking the retinotopic organization of older/juvenile (2-3 years of age) monkeys. So far, the organization appears to be similar, though it is difficult to make direct comparisons with the correlation approach. To match these early neonate data to the 2-3 year old data, we needed to scale the brains by ~130%, which means our effective sampling resolution was coarser for the neonate data."

While the authors did not address this concern, we believe it is important to show the functional connectivity analyses in the older monkeys (>1.5 years) and compare it to the baby monkeys because the neonate monkeys cannot fixate and therefore all the analyses in the neonates are done with functional connectivity rather than retinotopy. As such, the authors compare one map (functional connectivity in the baby monkeys) to another map of eccentricity from retinotopic mapping (in the >1.5 year old monkeys). Given that the authors transformed the older monkeys' ROIs to the baby monkey brains, it seems a straightforward analysis to do the same functional correlation analysis on the older monkeys (on which these ROIs were defined in the first place). That the brain changes size across areas is a potential concern for all analyses, not just this one. Therefore, their argument against doing this analysis undermines the other analyses they are performing. The reason that measuring the functional connectivity in the older monkeys (e.g. Figure 2A, Figure 5A) is important is that this analysis will enable estimating what aspects of functional connectivity stay the same with age and what components develop, as described in the initial comment. Thus, the outcome of this analysis will flesh out what the authors mean by proto-retinotopic organization.

Reviewer #2:

The authors addressed all my concerns. This is a very neat and important paper, which will be of interest to many. I would like to commend the authors for addressing this challenging question!

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A Hierarchical, Retinotopic Proto-Organization of the Primate Visual System at Birth" for further consideration at eLife. Your revised article has been favorably evaluated by David Van Essen (Senior Editor), a Reviewing Editor, and two reviewers.

The manuscript has been improved but there is one remaining issue that need to be addressed before acceptance, as outlined below:

Reviewer 1 points out that "Figure 6 only shows the resting state correlations in the neonates". Please address the comment that the updated Figure 6 should include the correlations in the juveniles.

Reviewer #1:

The authors had addressed my major remaining comment asking whether it is retinotopy that is developing, or that the relationship between retinotopy and resting state correlation that is developing. To address this concern I suggested comparing the resting state correlations in the juveniles compared to neonates.

They did a slightly different analysis than I suggested, which is fine with me. In their revision, they compared the correlations between retinotopic correlations and resting state functional correlations within the juveniles to the retinotopic correlations in juveniles vs. resting state correlations in the neonates.

They report the results in the subsection “Retinotopic organization in newborn”:

“Excluding V1, the mean absolute deviation between eccentricity correlations at newborn and juvenile ages was 2.0° across retinotopic areas, in both hemispheres, in both monkeys. Juvenile eccentricity correlations were more similar to the eccentricity mapping (mean deviation = 1.4°) than to the neonate eccentricity correlations, potentially indicating refinement of retinotopic maps over development. However, these differences might reflect non-biological variance (e.g., the precision of anatomical registration and proximity of coil placement due to brain size differences across ages). These data indicate that extensive retinotopic organization across both early and higher visual cortex was already present within the first weeks of life.”

What is still missing is a figure illustrating these results. In the response letter they write: "We include these new data in a revised Figure 6." However, I did not see these new data in Figure 6. Figure 6 only shows the resting state correlations in the neonates. Please update Figure 6 to include the correlations in the juveniles.

Reviewer #2:

The authors addressed the remaining issues raised by the other reviewer. I've no further comments.
