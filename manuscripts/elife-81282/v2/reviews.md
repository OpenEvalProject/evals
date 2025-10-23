# Peer review - Round 1

Editors:
- Jörn Diedrichsen, https://ror.org/02grkyz14 Western University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81282.sa0](https://doi.org/10.7554/eLife.81282.sa0)

This valuable study examines a largely ignored brain structure (the thalamus) in functional brain imaging studies. The study shows that localized thalamic regions show hub properties in terms of their activation properties and connectivity to cortical regions. While some open questions regarding the robustness and validity of measure that defines the hub properties may remain, the evidence in the paper is generally convincing, especially as converging evidence across two large datasets is presented.


---

# Peer review - Round 1

Editors:
- Jörn Diedrichsen, https://ror.org/02grkyz14 Western University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81282.sa1](https://doi.org/10.7554/eLife.81282.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Thalamocortical contribution to cognitive task activity" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, including Jörn Diedrichsen as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Timothy Behrens as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Moataz Assem (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. The measure of "task hub" properties that is central to the paper would need to be much better explained and justified. You motivate the measure to be designed to find voxels that are "more flexibly recruited by multiple thalamic activity components", but it is not clear to me at this point that the measure defined on line 634 does this. First, sum_n w_i2 is constrained to be the variance of the voxel across tasks, correct? Would sum_n abs(w) be higher when the weights are distributed across components? Given that each w is weighted by the variance (eigenvalue) of the component across the thalamus, would the score not be maximal if the voxel only loaded on the most important eigenvector, rather than being involved in a number of components? Also, the measure is clearly not rotational invariant – so would this result change after some rotation PCA solution? Some toy examples and further demonstrations that show why this measure makes sense (and what it really captures) would be essential. The same holds for the participation index for the resting state analysis.

2. The least compelling set of results (though not necessarily wrong) is the thalamic prediction of cortical activations. This is because the functional connectivity (FC) matrix used to link the thalamus and cortex was derived from the same data after regressing out task-related variance. However, this process might not be clean enough. The authors do not provide enough details on how task-evoked responses were regressed and how the residuals were assessed to be clean. A stronger test would utilize an FC matrix derived from independent data. Alternatively, I suggest using the FC matrix from dataset 2 to examine cortical projections of dataset 1 (and vice versa).

3. Throughout the manuscript, there is a general dependence on qualitative comparisons instead of quantifying similarities between findings. For example, (a) the spatial similarity of task hubs across the two datasets was not assessed (Figure 1d) (b) similarities between thalamic task hub projections to the cortex (Figure 2b). The comparison between the two datasets should be better quantified.

4. For the activity flow analysis, the null models (which need to be explained better) appear weak (i.e. no differences across tasks?), and it is no small wonder that the thalamus does significantly better. The Pearson correlations are not overwhelmingly impressive either. To give the reader a feel for how good/bad the prediction actually is, it would be essential that the authors would report noise ceilings – i.e. based on the reliability of the cortical activity patterns and thalamic activity patterns, what correlation would the best model achieve (see King et al., 2022, BioRxiv, as an example).

Reviewer #2 (Recommendations for the authors):

The findings presented here are important. The following recommendations would make the conclusions stronger:

1. The study would benefit from linking the thalamic task hubs to canonical resting-state networks defined in the thalamus (e.g. Ji et al. 2019 NeuroImage). Do task hubs mainly overlap with one functional network [e.g. the frontoparietal network (FPN)] or do they cross multiple functionally distinct networks? The latter would suggest some fractionation of the identified hubs (which is alluded to in the current results, due to the non-replication of the posterior thalamic task hub across datasets). It would be most interesting if task hubs ended up occupying voxels at the intersection of multiple RSNs (similar to how Power et al. 2013 Neuron defined hubs).

2. Could fractionating the thalamic task hubs reveal different cortical contributions? The cortical results in Figure 2B are actually not that similar across the datasets (e.g. ventro-medial frontal and posterior cingulate areas). Further, the cortical areas identified occupy much of the association cortices, which is inconsistent with more localized cortical hubs that the authors reference (Bertolero et al. as well as other studies). The posterior portion of the thalamic task hubs is already one potential contributing factor to these differences. There is also evidence that anterior thalamic regions are the most connected to a localized core subset of the FPN (Assem et al. 2020 Cerebral Cortex). Similarly, would simulating fractionated lesions to the thalamic task hubs show different contributions in Figure 5?

3. The least compelling set of results (though not necessarily wrong) is the thalamic prediction of cortical activations. This is because the functional connectivity (FC) matrix used to link the thalamus and cortex was derived from the same data after regressing out task-related variance. However, this process might not be clean enough. The authors do not provide enough details on how task-evoked responses were regressed and how the residuals were assessed to be clean. Perhaps these details could quell my concerns. That said, if available, a stronger test would utilize an FC matrix derived from independent data. Alternatively, I suggest using the FC matrix from dataset 2 to examine cortical projections of dataset 1 (and vice versa).

4. Throughout the manuscript, there is a general dependence on qualitative comparisons instead of quantifying similarities between findings. For example, (a) the spatial similarity of task hubs across the two datasets was not assessed (Figure 1d) (b) similarities between thalamic task hub projections to the cortex (Figure 2b). Please quantify any comparison between the two datasets.

5. This is optional but I believe it would serve the study well if they link their thalamic task hubs to underlying thalamic nuclei using one of the many existing atlases (e.g. Najdenovska et al. nature scientific data 2018 https://www.nature.com/articles/sdata2018270). Even if the links with nuclei is at a coarse level, it could serve as a nice anatomical foundation for future explorations.
