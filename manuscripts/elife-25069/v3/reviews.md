# Peer review - Round 1

Editors:
- Kalanit Grill-Spector, Stanford University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.25069.012](https://doi.org/10.7554/eLife.25069.012)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Altered topology of neural circuits in congenital prosopagnosia" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and David Van Essen as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The paper presents a new network analysis method, to characterize and compare the large scale network topology of brain networks in congenital prosopagnosia (CP) compared to typical controls. By using a new approach (inter-subject functional correlation approach, ISFC), which captures the correlations between nodes of different subjects, the study reports both local and macro scale differences between CP and controls. Locally, there were differences across groups in the anterior temporal (ATL), which served a hub for the control participants, but not CPs. Macroscopically, CPs evinced hyper-connectivity in posterior visual regions compared to controls, especially in the right hemisphere. Moreover, this hyper-connectivity was higher in the right hemisphere, known for its dominance in face processing, compared to the left hemisphere. These results advance understanding of network differences between CPs and controls.

The reviewers agreed that the topic is of great interest, the rationale of the study is straightforward, and the experiments were well designed. They concluded that the study offers new insights into the perturbed cortical topology in CPs.

Essential revisions:

The reviewers raised several major concerns that require your attention before the paper can be considered for publication.

Conceptual

The reviewers raised concerns about overlap with your prior 2014 Cerebral Cortex paper. Please clarify the conceptual advancement made by this study with respect to your prior work.

Another concern raised was that the comparison between normal controls and subgroups of CPs (mild and severe group) is non-independent from the comparison between normal controls and the entire group of CPs. Moreover, the results comparing the entire group of CPs and the different severity levels seems to be at odd with each other. The reviewer commented: "The authors report that compared with controls, CPs showed decreased ISFC in the FFA tagged nodes, as well as increased ISFC in the LOC tagged nodes. However, in the comparison between severe CPs and mild CPs, they report compared with mild CPs, severe CPs showed decreased ISFC in the LOC tagged nodes, as well as increased ISFC in the FFA tagged nodes. The explanations in the discussion pertaining to the inconsistency between these findings is speculative."

Data analysis

Thresholding procedure: The reviewers raised concerns regarding the threshold used, and asked why only positive correlations were considered:

1) Throughout the paper different thresholds are mentioned, but no clear description or quantification of how these thresholds were computed is provided. For example, Figure 1. uses an edge threshold of 0.3 without motivating why such a threshold is used, while the legend of Figure 2 reads on the second line "at minimum threshold", but it's unclear what the minimum is here.

2) Definition of nodes:

Why was a 0.5 threshold used? A better motivation should be provided.

Permutation testing: The permutation test that was used to evaluate the statistical differences of the network structure across the two groups was not properly implemented.

In permutation testing, given a statistic t computed on the difference between two groups, one would randomly assign the group labels, and compute the statistic again, repeat this process multiple times to estimate a null distribution, and compute the empirical p-value of the original statistic. If we apply the same concept to the method developed by the authors, one should first estimate the statistic, that is a correlation matrix for each group. This would be done by performing the split-half procedure for all the possible combinations (10C5 or 252 splits), and averaging across all splits, similar to what Simony et al. did with the leave-one-subject-out scheme. Given these two correlation matrices (one for each group), one would take their difference and obtain the final statistic of interest. Then, to compute the null distribution, one would randomly assign subjects to the groups (while maintaining the same numbers of subjects in each group), and then perform the same procedure to estimate the final statistic. By repeating this process at least 10,000 times (modern computing power can easily allow such number of iterations) one would effectively create a null distribution, that is the sampling distribution under the null hypothesis of no difference between the two groups. FWER correction could be performed in the same way as in Simony et al., 2016, by taking the max of the statistic at each iteration.

Estimation of the null distribution for statistical testing. In the original paper by Simony et al., ISFC was computed in a leave-one-subject-out scheme: time series from one subject were correlated with the average time-series of the other subjects. This process was repeated for all the possible combinations, and an average correlation matrix was computed, imposing symmetry by averaging the correlation matrix with its transpose. Statistical significance was computed through permutation testing, by randomizing the phase of the time series and computing an empirical, FWER corrected p-value. In contrast, Rosenthal et al., 2016 adopt what is known as a split-half scheme: for each group the correlation matrix is computed by correlating the average time series of five subjects with the average time series of the other five subjects. Statistical testing, however, is then mixed with the estimation of the actual correlation matrix from the data, by repeating this process 1,000 times and counting how many times the correlation in one group is greater than the correlation in the other group, to seemingly estimate an empirical p-value. The concern is that this approach might conflate the estimation of the correlation matrix with permutation testing, and might not compute a null distribution.

Comparison between functional connectivity (FC) analysis and ISFC: Comparing ISFC with FC to show the effectiveness of the novel method is very important, However, this comparison should be done while keeping all the statistical analyses comparable, similar to the approach of Simony et al., 2016.

In the present manuscript, the different methods used different statistical tests: t-test to compute significance in FC and a permutation testing in ISFC to evaluate differences between CPs and controls. It is unclear whether the usage of different statistical tests could lead to the differences across the two methods. A permutation testing approach in the analysis of FC could resolve this issue.

Additionally, for ISFC the time series of two runs were averaged and then the correlation matrix computed, whereas for FC correlation matrices were computed within each run, and then averaged. Consistency should be maintained (either averaging time series or computing correlation matrix individually for each run).

Brain-behavioral correlations: It would be interesting to link the topological changes to the severity of CP by conducting a correlation analysis between behavioral performance with topological measures, in which each point in the correlation is an individual subject. This approach could evaluate if the topological changes could predict behavioral performance in individual CPs. A similar analysis could also be conducted in normal groups.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Altered topology of neural circuits in congenital prosopagnosia" for further consideration at eLife. Your revised article has been favorably evaluated by David Van Essen (Senior editor), a Reviewing editor, and three reviewers.

The manuscript has been improved but there are some remaining issues listed by reviewers 2 and 3 that need to be addressed before acceptance, as outlined below. It is important to address these concerns incisively in the revised manuscript and in a point-by-point response in your cover letter.

Reviewer #1:

The authors have addressed my previous suggestions.

Reviewer #2:

I'm glad to see my comments have been appropriately addressed, and the quality of the paper has been significantly improved. Importantly, the new correlation analysis between the ISFC edges and behavioral performance really provide us new insights on the neural mechanism of the CP. But on second thought I still have several concerns that the authors may want to address.

1) I do agree that ISFC is a powerful approach to detect the stimulus-locked inter-regional correlation patterns. But as the visual experiment in the current study is a blocked design rather than the continuous natural (or real life) stimulus design as that in Simony et al., 2016, I'm wondering if the ISFC were mainly driven by the 'box car' effect rather than stimulus-locked response. If so, maybe the authors need to remove the data from the rest periods before running ISFC.

2) The data from an independent localizer was used to define the nodes. It elegantly avoids the double dipping. But I'm still wondering if there are some biases because only the data from the controls were taken into account in defining the nodes. Will this choice bias some results (e.g., the face-specific dominance in controls' nodes)?

3) In the definition of edges using the standard FC, why the author normalized all correlation coefficients for each subject to remove the subject level global effects? Aren't the global effects our interests in comparing controls and CPs? And, why the authors didn't use the same strategy to normalize all correlation coefficients in the definition of edges using the ISFC?

4) As I pointed out in the last round of review that the top schematic in Figure 1 and Figure 4 is somewhat misleading. The dash lines which connect the corresponding nodes in a pair of brains may mislead the readers into thinking that ISFC only calculates the functional correlation between corresponding nods across brain as inter-subject correlation (ISC) does. Nor do I catch what the top schematic in Figure 2 exactly does express.

Reviewer #3:

The authors addressed most of the comments in the first round of the review, however I believe that the manuscript can be improved further in clarity and in methodological rigor.

Definition of node strength. The authors abandoned the use of node degree in favor of weighted node degree, or node strength, by creating an undirected weighted graph, where the weights are t-values of correlations between pairs of ROIs. However, they used both negative and positive t-values at the same time to compute the strength of each node. As reported in the Appendix of the paper the authors cite (Rubinov and Sporns, 2010), the assumption of this metric is that all the weights are positive and normalized between 0 and 1. In this manuscript, weights are not all positive, and not normalized (although I believe this is less problematic). I'm not sure that it makes sense to consider both negative and positive weights at the same time. Imagine a node with only two incident edges, one with positive weight (say +10), and one with negative weight (-10). The strength of this node will be 0, but this doesn't correctly represent that the node is strongly correlated with another node only in the Control > CP contrast, and strongly correlated with a different node only in CP > Control. It is my understanding that in networks with negative weights one should analyze both sets of weights (positive and negative) separately.

Correlation between ISFC and behavior. I find that this analysis has several issues that need to be addressed. First, the authors used a one-tailed t-test, but this is generally considered too liberal without a clear a priori hypothesis on the directionality of the effect. It is even more problematic considering that with a two-tailed t-test, none of the results would be significant. In addition, even with a one-tailed t-test, the correlation between CFMT and ISFC values is not significant (even though the authors claim that it is: p = 0.053). Second, I find even more problematic the fact that the authors computed two different correlations and regressions, one for each group; looking at Figure 2 it is evident that if the two groups were considered together, the regression line would be flat or perhaps negative. This should be addressed by running a single multiple regression with a regressor variable indicating the group. Also, using z-scores as the x-axis in Figure 2 is confusing: there's no need to z-score the values prior to correlating them, and showing the actual questionnaire score will allow the reader to understand better how the participants score in those questionnaires. Lastly, what do the authors mean with "raw ISFC value"? Given the node by node ISFC matrix, does it refer to the average across one row of this matrix (perhaps taking only the upper triangular matrix if the ISFC matrix is symmetric)? And is the diagonal considered or removed prior to averaging, if the average is being computed?

Comparison between FC and ISFC. The authors improved the permutation testing approach for the ISFC, however they used an FDR corrected t-test with FC. The authors should consider implementing the permutation approach used in Simony et al., 2016, to make the two methods really comparable (i.e., differing only in the way correlations are computed), or justify why they chose these different statistical tests. In addition, ISFC correlations are still computed by averaging the time-series in the two runs first, whereas in FC first correlation matrices are computed, and then averaged. This should be made consistent in both analyses to make the comparison clearer.

In addition, it seems now that results from FC and ISFC converge. Then, why is ISFC needed at all? The authors should expand their discussion on this point. Also, correlations between edges and behavioral results should be performed also using FC-if not in the main text, they should be inserted in the supplementary materials to let readers understand the benefits/drawbacks of either methods when investigating similar questions.

Comparison between node strength and node location. Please provide more information on the stability of this result using different number of bins/bin sizes. How many bins had only one node? Also, for each bin, was the node strength computed as the sum of all the nodes belonging to that bin, or the average/median? The values in the y-axis in Figure 3 seem too high to be averages, and this analysis suffers from the problem described above of putting together negative and positive weights: a better approach would be to divide negative and positive edges, and perform the same analysis.

Please provide units for both axes in Figure 3.

The legend of Figure 3 refers to controls as "matched", but throughout the paper "controls" is used.
