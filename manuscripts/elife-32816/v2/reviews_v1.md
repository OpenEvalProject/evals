# Peer review - Round 1

Editors:
- Jody C Culham, University of Western Ontario Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.32816.021](https://doi.org/10.7554/eLife.32816.021)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The representational dynamics of task and object category processing in humans" for consideration by eLife. Your article has been favorably evaluated by David Van Essen (Senior Editor) and two reviewers, one of whom, Jody C Culham (Reviewer #1), is a member of our Board of Reviewing Editors and the other is Stefania Bracci (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Both reviewers were positive about the manuscript, particularly the novel combination of MEG and fMRI to address the influence of task goals upon object recognition unfolds over time. Results complement previous work and provide novel results by characterising how task and object representations evolve and interact throughout the visual hierarchy.

Essential revisions:

1) Key methods in the main text should be clarified.

Specifically, the exact inputs into the classifiers should be explained briefly in the main text (and perhaps also more explicitly in the detailed methods). In the Cichy et al. (2014, Nat Neurosci) paper, it looks like the data put into RSMs was signal strength at each spatial channel. In the present paper, some sort of PCA was done to extract seemingly spatiotemporal components. Are the features being decoded purely spatial or is there any component of rates of temporal change? Some explanation in the main text, not just the Materials and methods, perhaps along with a schematic in the figures (as in Figures 1B and 4A of Cichy) would help readers understand key elements needed to understand this as-yet-not-that-common combination of fMRI and MEG RSA.

The commonality analysis (subsection “Model-based MEG-fMRI Fusion for Spatiotemporally-Resolved Neural Dynamics of Task and Object Category”, first paragraph) could have also been summarized more clearly.

2) Some additional discussion of the interpretation of MEG-fMRI correlations is warranted.

If the MEG features are purely spatial, then what does it mean to say that the voxelwise pattern of activation in a region measured with fMRI is correlated with a sensorwise pattern of activation in MEG. If there are univariate as well as multivariate activation changes in the region, then is this relationship somewhat trivial? As the spatial features (voxels) in fMRI that contribute to successful classification can be plotted (voxel weight maps), can the sensors in MEG that contribute to classification be plotted and compared with the fMRI maps.

3) The reviewers have some concerns about the degree to which object decoding representations reflect specific object categories (e.g., cow), or object-specific visual properties. This should be addressed in the Discussion and/or the strength of the claim for category specificity should be toned down. The authors may wish to consider an additional analysis suggested by one reviewer.

Reviewer 1 notes:

In Figure 1B, labels under the categories or more information in the figure legend would help (I had to look at the detailed methods to learn that the categories shown were specific categories not the general categories typically studied in ventral-stream processing (e.g., cows not animals). After seeing reviewer 2's comments, I too wonder how strong the category-specific arguments can be when the stimuli would have been even more visually similar than in most studies of category-selective processing.

Reviewer 2 notes:

In Figure 2, the authors show significant object decoding (regardless of task) during the object stimulus period. I wonder to what extent these object – presumably, objects within the same category share very similar visual properties (e.g., shape, texture, luminance etc.). Some of the results shown make me think that the latter interpretation might be possible. In particularly, the highest decoding accuracy is found immediately after image onset. Subsequently, decoding accuracy smoothly and constantly decreases (Figure 2). A similar pattern is also visible in Figure 4A. After object onset, during the period of highest decoding accuracy, there was no decoding difference between conceptual and perceptual tasks (this difference emerges later on), thus suggesting that this effect might be related to objects' visual attributes. To address this point the authors could run an additional temporal generalisation analysis (Figure 3A) to test pattern similarities across time for object categories. If during object onsets the results show two different clusters, results would point to different cognitive processes across time. In my view, it would be a nice addition the current analyses.

I also wonder whether the authors found similar patterns of object decoding for all 8 conditions? Based on evidence from the literature, I would expect some conditions (e.g., animals) to show better decoding than others (e.g., plants).

Related to the first comment, regarding the model-based MEG-fMRI fusion analysis shown in Figure 5, the authors state: "…EVC, LO and pFS exhibited a mixture of task and category-related information during the Object Stimulus Period, with relative increases in the size of task-related effects when moving up the visual cortical hierarchy". Wouldn't you expect the same hierarchical increasing pattern for object representations? Instead, looking at the figure, it seems that the object category model explains more variance in EVC than pFS. I wonder whether a visual model (e.g., shape – such as the geometric blur descriptor (Belongie et al., 2002), which captures object shape similarities irrespective of orientation) would do a better work – especially in EVC and LO. Maybe the authors could discuss this possibility in the Discussion section.
