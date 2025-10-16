# Peer review - Round 1

Editors:
- Chris Honey

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.32992.036](https://doi.org/10.7554/eLife.32992.036)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The relationship between spatial configuration and functional connectivity of brain regions" for consideration by eLife. Your article has been reviewed by four peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Sabine Kastner as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Jakob Seidlitz (Reviewer #2); Daniel S Margulies (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

You can see the specific comments from each reviewer below. During our discussion, the reviewers agreed that this was potentially an important result. We felt that the manuscript would be substantially improved if your team could:

i) Provide more information about the location (regions and subnetworks), scale and direction of the spatial variation that is most consistently observed across participants;

ii) Clarify the logic behind the central claim [that spatial variation accounts for the behaviorally-relevant variation in edge-strength] and show that the analytics are not biased to translate non-spatial sources of variability into spatial sources of variability;

iii) Justify the use of low-dimensional decompositions in some analyses and show whether fine-grained parcellations could ameliorate (or exacerbate) the misattribution effects that are reported;

iv) Provide more information about which specific behavioral metrics covary with the spatial/morphological variation.

We also recommend trying to make the manuscript (especially the Introduction and Results) more readable for those who are familiar with fMRI and functional connectivity methods, but who are not experts in the individual differences sub-field and who have not yet read the Materials and methods in detail.

Reviewer #1:

This manuscript presents a potentially interesting study on the spatial arrangement of functional regions and how they interact, and the relationship of this to non-imaging measures. Overall I think I agree with the premise of the paper (anatomy and function are not independent nor completely separable) and find the result of interest to the brain-behaviour community. However, the paper is really hard to read/follow and its unclear to what extent the authors have proven their point.

The difficulty in following this also makes it very difficult to evaluate the significance of the findings. For example in the first simulation topographic information is added to the HCP data and then it is shown that topographic information accounts for some of the variance. It's not clear how this wouldn't be the case since that is what was added. While the simulation may indeed show that topology accounts for a significant fraction of the variance, this doesn't actually show that this is what is happening in real data. In general, the idea that spatial topology matters, while likely true, is poorly supported by an ad-hoc combination of ICA, parcellation, and PFMs.

Besides the intractable writing there are at least two major concerns:

1) The idea that individualized parcellations can reveal information has been shown previously. Comparing networks derived from group-parcellations with individualized spatial maps is not really a fair comparison. While it makes a nice argument for performing individualized functional parcellations the comparison as set up is not that interesting nor informative. To show that the correlation matrices (networks) do not add any unique information, one would need to show that the differences in parcellations (ICA-component definitions) across subjects can predict behavior better than, or comparable to, networks derived from the individualized functional maps. This is not what was done however.

2) It also appears to be the case that the authors derive the truest subject-specific map (Figure 4) from a group-level ICA. This is mentioned briefly in the Materials and methods section and is necessary to preserve the correspondences in ICA components across subjects. It appears that to maintain correspondence ICA was first performed at the group level and then brought to the individual level. It is not clear that this is a fair approach.

The CCA's in Figure 1 are interesting but somewhat unclear. Independent of the concerns with the simulation expressed above, the interpretation of Figure 1 seems to be that the functional data is confounded by the topographic information but this sort of summary does not show that. I think the authors are implying that the high CCA for topography means that this is the source of the functional CCA but these do not have to be from the same source. The summary data needs to be broken down further to prove that argument.

The only functional (nonICA atlas used) is the Yeo atlas, which was somehow extended from 17 regions up to 109, but this is really a low resolution atlas. It has been shown by many groups that functional atlases of this order (such as AAL) are very poor and there are numerous publicaly available atlases with many more nodes such as the Shen atlas (Shen, 2013, which should be mentioned in the Introduction) 268 nodes, the Glasser atlas (360 nodes), which is discussed but not apparently used. This is particularly important given the comment in subsection “Cross-subject information in fMRI-derived measures” that the dimensionality of the decomposition may influence the results.

While ICA 200, is high relative to the low 25 ICA it is still not high relative to many functional parcellation schemes.

There are many other questions and concerns about various steps in the analysis but these are too numerous to catalog with the manuscript in its current form.

Reviewer #2:

This manuscript directly assesses the relationship between underlying spatial topography and functional connectivity. In general, from my knowledge of the literature, this is the first time that such a direct comparison has been performed in the context of brain-behavior comparisons. Overall, I thought the manuscript was well-written and the analyses well-defined and well-executed, and I believe that this topic (and these findings) are of particular relevance to the wider neuroimaging community, especially given the widespread use of this dataset from the Human Connectome Project. Some notable remarks include the use of high-quality publicly available data from a large cohort, and the reproducibility of the findings across parcellations (and thresholding/binarization). Please find below comments for the authors to consider.

1) What was the justification for the use of a dimensionality of 15 for the creation of the ICA basis maps? It would be good to add this to the Materials and methods section "Unique contribution of topography versus coupling" or within the Results (say in subsection “Unique contribution of topography versus coupling”).

2) How consistent were the loadings of the behavior CCA outputs from each of the comparisons with brain (i.e., Figure 1 in this manuscript)? Is it possible to quantify these relationships across the comparisons in this work? It would be good to evaluate this empirically, with reference to the CCA loadings in Smith et al., 2015 as reference in this manuscript. In addition to this quantitative analysis, the manuscript would benefit from more of a discussion (and potentially a supplemental figure) about the resultant behavior axes derived from the CCA (i.e., similar to Figure 1 from Smith et al., 2015).

3) Given the focus/topic of this manuscript, and as briefly touched on in the discussion (and Figure 1—figure supplement 1) about the relationship between fractional surface area and subject CCA weights, it would be of great interest to the audience of this manuscript to quantify and report the relationship between basic morphological features (for example, cortical thickness, surface area, volume, myelin maps, and/or curvature) and the spatial rfMRI maps/networks. Clearly spatial variability explains a great deal of variance in rfMRI-derived network matrices, but it would be good to compare these maps to classical morphological metrics, which are derivable from these data.

4) I would highly recommend the authors include a section (in the Materials and methods) about the data quality assessment and quality control that was performed, as well as elaborate on the preprocessing procedures. This would be of particular interest to those that would like to try to reproduce these findings or replicate them in an independent dataset.

Reviewer #3:

The study by Bijsterbosch and colleagues addresses the important question of what aspect of functional connectivity varies across individuals. Prior work has largely investigated variance in the strength or amplitude of functional connectivity, however, the current findings demonstrate that much of that variance is better explained by differences in spatial topography. The analyses are conducted on data made available by the Human Connectome Project, and include validation using several network decomposition and parcellation approaches.

The topic of this study is of high relevance to the field, and my primary recommendation to the authors would be to provide more extensive illustration of the topographic variance in the main manuscript. Specifically, Figure 2 is an excellent example of the type of spatial variance underlying individual differences in functional connectivity measures. Further figures depicting the spectrum of spatial variance (based on the maps shown in the supplementary videos, for example) would further help the reader understand the nature of these patterns of interindividual difference. In addition, an additional figure that summarizes the topographic variance across the cortex, along the lines of Figure 1—figure supplement 1, would be a helpful addition to the current manuscript.

Reviewer #4:

Main Issues

It is important to show that the PROFUMO decomposition is not biased to ascribe variance to the spatial mode when that variance arises elsewhere (e.g. from changes in inter-regional correlation). Please include a simulation which explicitly tests this idea (or explicitly describe for the reader the simulations from the prior PROFUMO papers that have demonstrated this fact). It is particularly important to demonstrate this for the case of overlapping generator ROIs. For, example, one could run a simulation on a 40 by 40 voxel grid, with Gaussian sources A, B, C, D located with centers as (10,10), (10,30), (30,10) and (30,30) respectively. The sources are expressed in space as Gaussians with s.d.s of (say) 10 units so that the signals from different sources do overlap. Now, we suppose that the four source signals are generated as a coupled linear system with some coupling matrix. We then ask whether changing the coupling matrix (without changing the spatial profile of the sources) leads PROFUMO to change its inferred spatial modes.For example, in condition 1, the B source is correlated with the C source, and the A source is correlated with the D source. In condition 2, the B source is additionally correlated with the A source. Are the _shapes_ of the sources recovered by Profumo different in Condition 1 and Condition 2? This is important to show, because otherwise the spatial variation inferred by PROFUMO may actually arise from changes in the true coupling matrix. Are the spatial maps the same even under conditions where the true coupling strengths fluctuate around their means over time?

The prediction of behavioral properties using fMRI is a central aspect of this manuscript, and yet there is almost no description of what aspects of human behaviors are being predicted. Which aspects of task performance are being well-captured? In subsection “Cross-subject information in fMRI-derived measures” there is reference to the in "positive-negative mode of covariation" but there is no description of what this means concretely.

Some of the writing in the Results section seems to assume that the readers have already read the Materials and methods, and yet the Materials and methods appear after the results. I suggest providing the readers with a bit more methodological context in the following subsections, to help them understand what was done:

In the Introduction section, when introducing the PROFUMO method, please elaborate a little more on what it does and how it works;

Relatedly, when comparing PROFUMO with dual regression approach, please provide readers with a brief description of the dual regression method, so that they can understand why it may not succeed in accurately recovering subject-specific networks;

Introduction section: "simulations that manipulate aspects of the data" – please be more precise about what is manipulated in the simulations;

Figure 1 – this Figure could be more effective if there was a graphical depiction of how the predictions are made from each of these fMRI-derived measures; as it is now, the reader arrives at this point in the manuscript with little idea of what is meant by any of the row-labels in this Figure;

Results section, paragraph three – once again the reader will have difficulty understanding what is being described because the relevant methods have not yet been laid;

Subsection “Spatiotemporal simulations demonstrating potential sources of variability in edges”; "thereby allowing each aspect to be fixed to the group average prior to generating simulated data using the outer product" – at this point in the manuscripts readers do not have any understanding why an outer product is relevant, or which matrix equation is being referenced;

The authors have quite convincingly shown that spatial variation in fMRI sources across subjects is an important challenge and widespread confound. Please provide some elaboration on your comments in the penultimate paragraph of the Discussion and provide the reader with some specific suggestions on how this problem might be overcome, and in what contexts it is more or less perilous. Is PROFUMO the answer? Is functional co-registration using localizers the answer? Could brain-wide functional hyper-alignment / shared response modeling provide another solution to the spatial variation problem? e.g. Chen et al., 2015.
