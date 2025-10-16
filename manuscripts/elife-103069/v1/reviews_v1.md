# Peer review - Round 1

Editors:
- Juan Alvaro Gallego, Imperial College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.103069.3.sa0](https://doi.org/10.7554/eLife.103069.3.sa0)

This study provides important insights as to how interacting brain areas produce movement during the execution of a skilled multi-directional reaching task. Using a combination of single neuron and neural population analysis, optogenetic stimulation, and computational models, the authors provide convincing evidence of an asymmetrical influence between mouse premotor and motor cortex during the execution of a well-practiced behaviour. This asymmetry can only be captured by some but not all population analysis methods, which is a key lesson to the field in and of itself. Analyzing how activity that is shared and private to these areas relates to different aspects of movements, and why different methods provide different outcomes regarding the nature of inter-area interactions would further strengthen this work.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.103069.3.sa1](https://doi.org/10.7554/eLife.103069.3.sa1)

This study examined the interaction between two key cortical regions in the mouse brain involved in goal-directed movements, the rostral forelimb area (RFA) - considered a premotor region involved in movement planning, and the caudal forelimb area (CFA) - considered a primary motor region that more directly influences movement execution. The authors ask whether there exists a hierarchical interaction between these regions, as previously hypothesized, and focus on a specific definition of hierarchy - examining whether the neural activity in the premotor region exerts a larger functional influence on the activity in the primary motor area, than vice versa. They examine this question using advanced experimental and analytical methods, including localized optogenetic manipulation of neural activity in either region while measuring both the neural activity in the other region and EMG signals from several muscles involved in the reaching movement, as well as simultaneous electrophysiology recordings from both regions in a separate cohort of animals.

The findings presented show that localized optogenetic manipulation of neural activity in either RFA or CFA resulted in similarly short-latency changes of the muscle output and in firing rate changes in the other region. However, perturbation of RFA led to a larger absolute change in the neural activity of CFA neurons. The authors interpret these findings as evidence for reciprocal, but asymmetrical, influence between the regions, suggesting some degree of hierarchy in which RFA has a greater effect on the neural activity in CFA. They go on to examine whether this asymmetry can also be observed in simultaneously recorded neural activity patterns from both regions. They use multiple advanced analysis methods that either identify latent components in the population level or measure the predictability of firing rates of single neurons in one region using firing rates of single neurons in the other region. Interestingly, the main finding across these analyses seems to be that both regions share highly similar components that capture a high degree of the variability of the neural activity patterns in each region. Single units' activity from either region could be predicted to a similar degree from the activity of single units in the other region, without a clear division into a leading area and a lagging area, as one might expect to find in a simple hierarchical interaction. However, the authors find some evidence showing a slight bias towards leading activity in RFA. Using a two-region neural network model that is fit to the summed neural activity recorded in the different experiments and to the summed muscle output, the authors show that a network with constrained (balanced) weights between the regions can still output the observed measured activities and the observed asymmetrical effects of the optogenetic manipulations, by having different within-region local weights. These results emphasize the challenges in studying interactions between brain regions with reciprocal interactions, multiple external inputs, and recurrent within-region connections.

Strengths:

The experiments and analyses performed in this study are comprehensive and provide a detailed examination and comparison of neural activity recorded simultaneously using dense electrophysiology probes from two main motor regions that have been the focus of studies examining goal-directed movements. The findings showing reciprocal effects from each region to the other, similar short-latency modulation of muscle output by both regions, and similarity of neural activity patterns, are convincing and add to the growing body of evidence that highlight the complexity of the interactions between multiple regions in the motor system and go against a simple feedforward-like hierarchy.

The neural network model complements these findings and adds an important demonstration that the observed asymmetry can, in theory, also arise from differences in local recurrent connections and not necessarily from different input projections from one region to the other. This sheds an important light on the multiple factors that should be considered when studying the interaction between any two brain regions, with a specific emphasis on the role of local recurrent connections, that should be of interest to the general neuroscience community.

Weaknesses:

While the reciprocal interaction and similarity in neural activity across RFA and CFA is an important observation that is supported by the authors' findings, the evidence for a hierarchical interaction between the two regions appears to be weaker. The primary evidence for a hierarchical interaction comes from a causal optogenetic manipulation, carried out at the onset of the reaching movement and conducted with n = 3 in each experimental group, which shows an effect in both regions, yet the effect is greater when silencing the activity in RFA and examining the resulting change in CFA, than vice versa. Analysis of the simultaneously recorded neural activity, on the other hand, reveals mostly no clear hierarchy with leading or lagging dynamics between the regions. The findings of the optogenetic manipulation might be more compelling if similar effects were observed when the same manipulation was applied at different stages of movement preparation and execution, indicating a consistent interaction that is independent from the movement phase.

The methods used to investigate hierarchical interactions through analysis of simultaneously recorded activity yielded inconsistent results. For instance, CCA and PLS showed no clear lead-lag relationship, while DLAG provided some evidence suggesting RFA leads CFA. Overall, these methods largely failed to demonstrate a clear hierarchical interaction. Assuming a partial hierarchy exists, this inconsistency may indicate that the hierarchy is not reflected in the activity patterns or that these analytical methods are inadequate for detecting such interactions within complex neural networks that are influenced by multiple external inputs, reciprocal inter-regional connections, and dominant intra-regional recurrent activity.

As is also argued by the authors, these inconsistent findings underscore the need for caution when interpreting results from similar analyses used to infer inter-regional interactions from neural activity patterns alone. However, the study lacks sufficient explanation for why different methods yielded different results and more elaborate clarification is needed for the findings presented. For example, in the population-level analyses using CCA and PLS, the authors show that both techniques reveal components that are highly similar across regions and explain a substantial portion of each region's variance. Yet, shifting the activity of one region relative to the other to explore potential lead-lag relationships does not alter the results of these analyses. If the regions' activities were better aligned at some unknown true lead-lag time (or aligned at zero), one would expect a peak in alignment within the tested range, as is observed when these same analyses are applied to activity within a single region. It is thus unclear why shifting one region's activity relative to the other does not change the outcome. The interpretation of these results therefore, remains ambiguous and would benefit from further clarification.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.103069.3.sa2](https://doi.org/10.7554/eLife.103069.3.sa2)

Summary:

While technical advances have enabled large-scale, multi-site neural recordings, characterizing inter-regional communication and its behavioral relevance remains challenging due to intrinsic properties of the brain such as shared inputs, network complexity, and external noise. This work by Saiki-Ishkawa et al. examines the functional hierarchy between premotor (PM) and primary motor (M1) cortices in mice during a directional reaching task. The authors find some evidence consistent with an asymmetric reciprocal influence between the regions, but overall, activity patterns were highly similar and equally predictive of one another. These results suggest that motor cortical hierarchy, though present, is not fully reflected in firing patterns alone.

Strengths:

Inferring functional hierarchies between brain regions, given the complexity of reciprocal and local connectivity, dynamic interactions, and the influence of both shared and independent external inputs, is a challenging task. It requires careful analysis of simultaneous recording data, combined with cross-validation across multiple metrics, to accurately assess the functional relationships between regions. The authors have generated a valuable dataset simultaneously recording from both regions at scale from mice performing a cortex-dependent directional reaching task.

Using electrophysiological and silencing data, the authors found evidence supporting the traditionally assumed asymmetric influence from PM to M1. While earlier studies inferred a functional hierarchy based on partial temporal relationships in firing patterns, the authors applied a series of complementary analyses to rigorously test this hierarchy at both individual neuron and population levels, with robust statistical validation of significance.

In addition, recording combined with brief optogenetic silencing of the other region allowed authors to infer the asymmetric functional influence in a more causal manner. This experiment is well designed to focus on the effect of inactivation manifesting through oligosynaptic connections to support the existence of a premotor to primary motor functional hierarchy.

Subsequent analyses revealed a more complex picture. CCA, PLS, and three measures of predictivity (Granger causality, transfer entropy, and convergent cross mapping) emphasized similarities in firing patterns and cross-region predictability. However, DLAG suggested an imbalance, with RFA capturing CFA variance at a negative time lag, indicating that RFA 'leads' CFA. Taken together these results provide useful insights for current studies of functional hierarchy about potential limitations in inferring hierarchy solely based on firing rates.

While I would detail some questions and issues on specifics of data analyses and modeling below, I appreciate the authors' effort in training RNNs that match some behavioral and recorded neural activity patterns including the inactivation result. The authors point out two components that can determine the across-region influence - (1) the amount of inputs received and (2) the dependence on across-region input, i.e., relative importance of local dynamics, providing useful insights in inferring functional relationships across regions.

Weaknesses:

(1) Trial-averaging was applied in CCA and PLS analyses. While trial-averaging can be appropriate in certain cases, it leads to the loss of trial-to-trial variance, potentially inflating the perceived similarities between the activity in the two regions (Figure 4). Do authors observe comparable degrees of similarity, e.g., variance explained by canonical variables? Also, the authors report conflicting findings regarding the temporal relationship between RFA and CFA when using CCA/PLS versus DLAG. Could this discrepancy be due to the use of trial-averaging in former analyses but not in the latter?

(2) A key strength of the current study is the precise tracking of forelimb muscle activity during a complex motor task involving reaching for four different targets. This rich behavioral data is rarely collected in mice and offers a valuable opportunity to investigate the behavioral relevance of the PM-M1 functional interaction, yet little has been done to explore this aspect in depth. For example, single-trial time courses of inter-regional latent variables acquired from DLAG analysis can be correlated with single-trial muscle activity and/or reach trajectories to examine the behavioral relevance of inter-regional dynamics. Namely, can trial-by-trial change in inter-regional dynamics explain behavioral variability across trials and/or targets? Does the inter-areal interaction change in error trials? Furthermore, the authors could quantify the relative contribution of across-area versus within area dynamics to behavioral variability. It would also be interesting to assess the degree to which across-area and within-area dynamics are correlated. Specifically, can across-area dynamics vary independently from within-area dynamics across trials, potentially operating through a distinct communication subspace?

(3) While network modeling of RFA and CFA activity captured some aspects of behavioral and neural data, I wonder if certain findings such as the connection weight distribution (Figure 7C), across-region input (Figure 7F), and the within-region weights (Figure 7G), primarily resulted from fitting the different overall firing rates between the two regions with CFA exhibiting higher average firing rates. Did the authors account for this firing rate disparity when training the RNNs?

(4) Another way to assess the functional hierarchy is by comparing the time courses of movement representation between the two regions. For example, a linear decoder could be used to compare the amount of information about muscle activity and/or target location as well as time courses thereof between the two regions. This approach is advantageous because it incorporates behavior rather than focusing solely on neural activity. Since one of the main claims of this study is the limitation of inferring functional hierarchy from firing rate data alone, the authors should use the behavior as a lens for examining inter-areal interactions.

Comments on revisions:

I appreciate the authors' thoughtful revisions in response to prior reviews, which I believe have substantially improved the manuscript. In particular, I found the addition of the new section "Manifestations of hierarchy in firing patterns" to be valuable, as it begins to address some of the more complex and potentially conflicting observations


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.103069.3.sa3](https://doi.org/10.7554/eLife.103069.3.sa3)

This study investigates how two cortical regions which are central to the study of rodent motor control (rostral forelimb area, RFA, and caudal forelimb area, CFA) interact during directional forelimb reaching in mice. The authors investigate this interaction using (1) optogenetic manipulations in one area while recording extracellularly from the other, (2) statistical analyses of simultaneous CFA/RFA extracellular recordings, and (3) network modeling. The authors provide solid evidence that asymmetry between RFA and CFA can be observed, although such asymmetry is only observed in certain experimental and analytical contexts.

The authors find asymmetry when applying optogenetic perturbations, reporting a greater impact of RFA inactivation on CFA activity than vice-versa. The authors then investigate asymmetry in endogenous activity during forelimb movements and find asymmetry with some analytical methods but not others. Asymmetry was observed in the onset timing of movement-related deviations of local latent components with RFA leading CFA (computed with PCA) and in a relatively higher proportion and importance of cross-area latent components with RFA leading than CFA leading (computed with DLAG). However, no asymmetry was observed using several other methods that compute cross-area latent dynamics, nor with methods computed on individual neuron pairs across regions. The authors follow up this experimental work by developing a two-area model with asymmetric dependence on cross-area input. This model is used to show that differences in local connectivity can drive asymmetry between two areas with equal amounts of across-region input.

Overall, this work provides a useful demonstration that different cross-area analysis methods result in different conclusions regarding asymmetric interactions between brain areas and suggests careful consideration of methods when analyzing such networks is critical. A deeper examination of why different analytical methods result in observed asymmetry or no asymmetry, analyses that specifically examine neural dynamics informative about details of the movement, or a biological investigation of the hypothesis provided by the model would provide greater clarity regarding the interaction between RFA and CFA.

Strengths:

The authors are rigorous in their experimental and analytical methods, carefully monitoring the impact of their perturbations with simultaneous recordings and providing valid controls for their analytical methods. They cite relevant previous literature that largely agrees with the current work, highlighting the continued ambiguity regarding the extent to which there exists an asymmetry in endogenous activity between RFA and CFA.

A strength of the paper is the evidence for asymmetry provided by optogenetic manipulation. They show that RFA inactivation causes a greater absolute difference in muscle activity than CFA interaction (deviations begin 25-50 ms after laser onset, Figure 1) and that RFA inactivation causes a relatively larger decrease in CFA firing rate than CFA inactivation causes in RFA (deviations begin <25ms after laser onset, Figure 3). The timescales of these changes provide solid evidence for an asymmetry in impact of inactivating RFA/CFA on the other region that could not be driven by differences in feedback from disrupted movement (which would appear with a ~50ms delay).

The authors also utilize a range of different analytical methods, showing an interesting difference between some population-based methods (PCA, DLAG) that observe asymmetry, and single neuron pair methods (granger causality, transfer entropy, and convergent cross mapping) that do not. Moreover, the modeling work presents an interesting potential cause of "hierarchy" or "asymmetry" between brain areas: local connectivity that impacts dependence on across-region input, rather than the amount of across-region input actually present.

Weaknesses:

There is no attempt to examine neural dynamics that are specifically relevant/informative about the details of the ongoing forelimb movement (e.g., kinematics, reach direction). Thus, it may be preemptive to claim that firing patterns alone do not reflect functional influence between RFA/CFA. For example, given evidence that the largest component of motor cortical activity doesn't reflect details of ongoing movement (reach direction or path; Kaufman, et al. PMID: 27761519) and that the analytical tools the authors use likely include this component (PCA, CCA), it may not be surprising that CFA and RFA do not show asymmetry if such asymmetry is related to control of movement details. An asymmetry may still exist in the components of neural activity that encode information about movement details, and thus it may be necessary to isolate and examine the interaction of behaviorally-relevant dynamics (e.g., Sani, et al. PMID: 33169030).

The idea that local circuit dynamics play a central role in determining the asymmetry between RFA and CFA is not supported by experimental data in this paper. The plausibility of this hypothesis is supported by the model but is not explored in any analyses of the experimental data collected. Further experimental investigation is needed to separate this hypothesis from other possibilities.

Comments on revisions:

The authors have improved the manuscript by reviewing several aspects of the text and the addition of supplemental materials. I believe these revisions have clarified some important aspects of the results.
