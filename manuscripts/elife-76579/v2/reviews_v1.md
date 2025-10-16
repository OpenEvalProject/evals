# Peer review - Round 1

Editors:
- Ronald L Calabrese, https://ror.org/03czfpz43 Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76579.sa0](https://doi.org/10.7554/eLife.76579.sa0)

This study applies an unsupervised dimensionality reduction (t-SNE) to characterize neural spiking dynamics in the pyloric circuit in the stomatogastric ganglion of the crab, an important system for mechanistic analysis of rhythmic circuit function. The application of unsupervised methods to characterize qualitatively distinct regimes of spiking neural circuits is interesting and novel. The challenges and lessons learned in this study are of broader interest to those seeking to quantitatively characterize large sets of neural data across many subjects. The method is demonstrated across hundreds of animal subjects and used to investigate circuit responses to a variety of perturbations.


---

# Peer review - Round 1

Editors:
- Ronald L Calabrese, https://ror.org/03czfpz43 Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76579.sa1](https://doi.org/10.7554/eLife.76579.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "Mapping Circuit Dynamics During Function and Dysfunction" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Alex Williams (Reviewer #1).

We are sorry to say that, after consultation with the reviewers, we have decided that this work will not be considered further for publication by eLife.

The reviewers find that paper has intrinsic interest especially to specialists in motor pattern generation by small circuits but requires considerable work and refocusing to make it of broader significance.

The expert reviews are quite compatible and provide rich feedback that could lead to a major overhaul and a new submission to eLife.

1. t-SNR is not in itself a clustering algorithm so its resulting 'clusters' should be validated by application of a true clustering algorithm. t–SNE does often provide a nice 2–D embedding that can simplify subsequent clustering. Here the reviewers suggest that the feature vectors themselves should be subjected to clustering algorithm.

2. The feature vectors are not as well motivated and explained as they should be so that readers in other systems can use the strategy presented here in cases where other features than ISI and spike phase of the activity might be more relevant.

3. There was discussion as to whether the framing of the manuscript as a ML pipeline is appropriate because the pipeline described relies heavily on manual curation. The manual curation should be more explicitly described (with details), and the limitations of this approach – ML followed by manual curation – discussed. Such a pipeline probably can't be as easily downloaded and applied directly to someone else's data, but overall, the community could benefit from more examples/consideration of how to systematically and carefully interleave the use of machine–learning techniques with manual analysis by domain experts but the process should be more explicitly explained.

4. Discussion should be revamped to discuss more fully specific insights into the pyloric circuit and the limitations of the analyses presented, for example the omission of the PY neuron activity means that the map as given is incomplete: potentially there are many more states, and hence transitions, within or beyond those already found that correspond to changes in PY neuron activity.

Reviewer #1:

The authors sought to establish a standardized quantitative approach to categorize the activity patterns in a central pattern generator (specifically, the well–studied pyloric circuit in C. borealis). While it is easy to describe these patterns under "normal" conditions, this circuit displays a wide range of irregular behaviors under experimental perturbations. Characterizing and cataloguing these irregular behaviors is of interest to understand how the network avoids these dysfunctional patterns under "normal" circumstances.

The authors draw upon established machine learning tools to approach this problem. To do so, they must define a set of features that describe circuit activity at a moment in time. They use the distribution of inter–spike–intervals ISIs and spike phases of the LP and PD neuron as these features. As the authors mention in their Discussion section, these features are highly specialized and adapted to this particular circuit. This limits the applicability of their approach to other circuits with neurons that are unidentifiable or very large in number (the number of spike phase statistics grows quadratically with the number of neurons).

The main results of the paper provide evidence that ISIs and spike phase statistics provide a reasonable descriptive starting point for understanding the diversity of pyloric circuit patterns. The authors rely heavily on t–distributed stochastic neighbor embedding (tSNE), a well–known nonlinear dimensionality reduction method, to visualize activity patterns in a low–dimensional, 2D space. While effective, the outputs of tSNE have to be interpreted with great care (Wattenberg, et al., "How to Use t–SNE Effectively", Distill, 2016. http://doi.org/10.23915/distill.00002). I think the conclusions of this paper would be strengthened if additional machine learning models were applied to the ISI and spike phase features, and if those additional models validated the qualitative results shown by tSNE. For example, tSNE itself is not a clustering method, so applying clustering methods directly to the high–dimensional data features would be a useful validation of the apparent low–dimensional clusters shown in the figures.

The authors do show that the algorithmically defined clusters agree with expert–defined clusters. (Or, at least, they show that one can come up with reasonable post–hoc explanations and interpretations of each cluster). The very large cluster of "regular" patterns – shown typically in a shade of blue – actually looks like an archipelago of smaller clusters that the authors have reasoned should be lumped together. Thus, while the approach is still a useful data–driven tool, a non–trivial amount of expert knowledge is baked into the results. A central challenge in this line of research is to understand how sensitive the outcomes are to these modeling choices, and there is unlikely to be a definitive answer.

Nonetheless, the authors show results which suggest that this analysis framework may be useful for the community of researchers studying central pattern generators. They use their method to qualitatively characterize a variety of network perturbations – temperature changes, pH changes, decentralization, etc.

In some cases it is difficult to understand the level of certainty in these qualitative observations. A first look at Figure 5a suggests that three different kinds of perturbations push the circuit activity into different dysfunctional cluster regions. However, the apparent spatial differences between these three groups of perturbations might be due to animal–level differences (i.e. each preparation produces multiple points in the low–D plot, so the number of effective statistical replicates is smaller than it appears at first glance). Similarly, in Figure 9, it is somewhat hard to understand how much the state occupancy plots would change if more animals were collected –– with the exception of proctolin, there are ~25 animals and 12 circuit activity clusters which may not be a favorable ratio. It would be useful if a principled method for computing "error bars" on these occupancy diagrams could be developed. Similar "error bars" on the state transition diagrams (e.g. Figure 6a) would also be useful.

Finally, one nagging concern that I have is that the ISIs and spike phase statistics aren't the ideal features one would use to classify pyloric circuit behaviors. Sub–threshold dynamics are incredibly important for this circuit (e.g. due to electrical coupling of many neurons). A deeper discussion about what is potentially lost by only having access to the spikes would be useful.

Overall, I think this work provides a useful starting point for large–scale quantitative analysis of CPG circuit behaviors, but there are many additional hurdles to be overcome.

Reviewer #2:

This manuscript uses the t–SNE dimensionality reduction technique to capture the rich dynamics of the pyloric circuit of the crab.

Strengths:

– The integration of a rich data–set of spiking data from the pyloric circuit.

– Use of nonlinear dimension reduction (t–SNE) to visualise that data.

– Use of clusters from that t–SNE visualisation to create subsets of data that are amenable to consistent analyses (such as using the "regular" cluster as a basis for surveying the types of dynamics possible in baseline conditions).

– Innovative use of the cluster types to describe transitions between dynamics within the baseline state and within perturbed states (whether by changes to exogenous variables, cutting nerves, or applying neuromodulators).

Some interesting main results:

– Baseline variability in the spiking patterns of the pyloric circuit is greater within than between animals.

– Transitions to silent states often (always?) pass through the same intermediate state of the LP neuron skipping spikes.

Weaknesses:

– t-SNE is not, in isolation, a clustering algorithm, yet here it is treated as such. How the clusters were identified is unclear: the manuscript mentions manual curation of randomly sampled points, implying that the clusters were extrapolations from these. This would seem to rather defeat the point of using unsupervised techniques to obtain an unbiased survey of the spiking dynamics and raises the issue of how robust the clusters are.

– The main purpose and contribution of the paper is unclear, as the results are descriptive, and mostly state that dynamics in some vary between different states of the circuit; while the collated dataset is a wonderful resource, and the map is no doubt useful for the lab to place in context what they are looking at, it is not clear what we learn about the pyloric circuit, or more widely about the dynamical repertoire of neural circuits.

– In some places the contribution is noted as being the pipeline of analysis: unfortunately as the pipeline used here seems to rely in manual curation, it is of limited general use; moreover, there are already a number of previous works that use unsupervised machine–learning pipelines to characterise the complexity of spiking activity across a large data–set of neurons, using the same general approach here (quantify properties of spiking as a vector; map/cluster using dimension reduction), including Baden et al. (2016, Nature), Bruno et al. (2015, Neuron), Frady et al. (2016, Neural Computation).

Some key limitations are not considered:

– The omission of the PY neuron activity means that the map as given is incomplete: potentially there are many more states, and hence transitions, within or beyond those already found that correspond to changes in PY neuron activity.

– The use of long, non–overlapping time segments (20s) – this means, for example, that the transitions are slow and discrete, whereas in reality they may be abrupt, or continuous.

– tSNE cannot capture hierarchical structure, nor has a null model to demonstrate that the underlying data contains some clustering structure. So, for example, distances measured on the map may not be strictly meaningful if the data is hierarchical.

– The Discussion does not include enough insight and contextualisation of the results.

Recommendations:

Explain and validate the clusters:

– The paper explains only that the clusters were assigned by manual curation of randomly sampled points. How then were all points assigned to clusters given that sample? What metric was used?

– We would suggest validating the clusters by using a clustering algorithm to recover them (approximately) from the vectors

Clarify the paper's goals and contributions:

– As noted above, the use of an unsupervised pipeline to map spiking activity is not novel; the survey of data is interesting, but purely descriptive. The key contributions were then not obvious to this reader – please clarify. To give some suggestions, while reading 3 possible contributions came to mind, but none quite fit: if the paper is an announcement of the dataset, then the datasets need a detailed explanation; if the paper is the introduction of a pipeline, then the pipeline ought to be fully unsupervised, else it is of little use outside the hands of the present lab; if the paper is about insights into the pyloric circuit, then conclusions and insights ought to be drawn from the descriptive results

Improve the Discussion:

– Explicitly link the results to insights into the pyloric circuit. The abstract states "strong mechanistically interpretable links between complex changes in the collective behavior of a neural circuit and specific experimental manipulations" – but only the short section on "Diversity and stereotypy in trajectories from functional to crash states" touches on this.

– Long section on other clustering methods is a survey of some alternatives and draws no conclusions about why tSNE was chosen here: either use to justify tSNE, or omit.

– Lines 678–716 are not based on any results in the paper.

Discuss limitations:

– The omission of the PY neuron activity means that the map as given is incomplete – what might it look like with it (new states, new transitions etc)?

– The transitions are slow and discrete by design (20 s long segments), whereas in reality they may be abrupt, or continuous.

– tSNE's limitations and their implications e.g. it cannot capture hierarchical structure, nor has a null model to demonstrate that the underlying data contains some clustering structure.

– Why those features of the spike–trains, and how would the map change if features were omitted or added? (e.g. the regularity of spiking).

Reviewer #3:

Gorur–Shandilya et al. apply an unsupervised dimensionality reduction (t–SNE) to characterize neural spiking dynamics in the pyloric circuit in the stomatogastric ganglion of the crab. The application of unsupervised methods to characterize qualitatively distinct regimes of spiking neural circuits is very interesting and novel, and the manuscript provides a comprehensive demonstration of its utility by analyzing dynamical variability in function and dysfunction in an important rhythm–generating circuit. The system is highly tractable with small numbers of neurons, and the study here provides an important new characterization of the system that can be used to further understand the mapping between gene expression, circuit activity, and functional regimes. The explicit note about the importance of visualization and manual labeling was also nice, since this is often brushed under the rug in other studies.

While the specific analysis pipeline clearly identifies qualitatively distinct regimes of spike patterns in the LP/PD neurons, it is not clear how much of this is due to t–SNE itself vs the initial pre–processing and feature definition (ISI and spike phase percentiles). Analyses that would help clarify this would be to check whether the same clusters emerge after (1) applying ordinary PCA to the feature vectors and plotting the projections of the data along the first two PCs, or (2) defining input features as the concatenated binned spike rates over time of the LP & PD neurons (which would also yield a fixed–length vector per 20 s trial), and then passing these inputs to PCA or t–SNE. As the significance of this work is largely motivated by using unsupervised vs ad hoc descriptors of circuit dynamics, it will be important to clarify how much of the results derive from the use of ISI and phase representation percentiles, etc. as input features, vs how much emerge from the dimensionality reduction.

Please define all acronyms when they are introduced.

Why is 20 seconds chosen as the time window to compute ISIs/phase representations before feeding the data into t–SNE? Is this roughly the window one needs to look at to visually identify differences across dynamical regimes and can the authors explain why?

It would be useful to note in the manuscript that t–SNE is tuned to preserve local over global similarities, which gives it its utility in clustering. It would also be useful to discuss the relationship of t–SNE to UMAP (McInnes, Healy, Melville 2018 arXiv: https://arxiv.org/abs/1802.03426), another popular dimensionality reduction technique in neuroscience.

Most uses of t–SNE in biology in the past have been in the context of classifying behavior (e.g. Berman et al. 2014 J R Soc Interface: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4233753/ or Clemens et al. Current Biology 2018: https://www.sciencedirect.com/science/article/pii/S0960982218307735). Including these references would be helpful as a point of comparison and to emphasize the novelty of applying t–SNE to neural spiking data.

Can the authors comment on how much pyloric rhythms can deviate from the standard triphasic pattern before behavior (or digestion?) is significantly disrupted?

In Figure 6 it would be helpful to show example time–series going into the transition matrix analysis, with identified state labels at the different timepoints. It wasn't clear whether timepoints were e.g. moment–to–moment, 20 sec chunks, a 20 sec sliding window, etc.

In Figure 8 it would be helpful to show examples of what bursts look like with and without decentralization, in order to contextualize the quantitative metrics.

It would also be useful to connect this work in the discussion to modern approaches for identifying model parameter regimes underlying distinct neural activity patterns (see e.g. Bittner et al. 2021 bioRxiv https://www.biorxiv.org/content/10.1101/837567v3)

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Mapping circuit dynamics during function and dysfunction" for further consideration by eLife. Your revised article has been evaluated by Ronald Calabrese (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Two reviewer concerns remain, which are explained more fully in the reviews below.

1. The analysis pipeline outlined in this paper is rather ad hoc. This isn't a general "tool" as it has only been demonstrated in one particular biological system.

2. It is acceptable for the authors to call the core method (tSNE) unsupervised. The "manual curation" is part of any exploratory data analysis, though it is generally preferable to for this manual curation / interpretation step to be as objective and reproducible as possible (which is arguably not entirely achieved in this paper). The paper can be seen as an investigation into how to apply an existing tool (tSNE) to a very well-studied and simple neural system.

In revision, we ask the authors to take a final pass through the Introduction and Discussion and to tone down any comments about this being a general, off-the-shelf tool and to note that while the core algorithmic method (tSNE) is unsupervised, there is still the need for expert interpretation of the output.

Reviewer #1:

The manuscript has been revised along the lines suggested in both the consensus suggestions and the individual reports. The rewritten Discussion is considerably improved. There is a lot of hard work here, and I've no doubt the results are useful to the PI's lab, and presumably other workers on this CPG.

To my mind the authors did not really address two of the main concerns of the reviewers: (1) what the purpose of this paper is and (2) the validity of the manual clustering of tSNE. In more detail:

Purpose of the paper: the paper prominently refers to it introducing an "unsupervised" method/approach (e.g. lines 69-70) and a "tool" (lines 537-541, 711-714). Neither are true: the approach here is by definition not unsupervised as it uses manual curation to identify the clusters upon which all further analyses are based; such manual curation means that the only "tool" parts are using tSNE on a feature vector, which doesn't merit the term. Rather, it seems that the purpose of the paper is instead to provide a cohesive overview of the dynamics of this specific CPG system, by finding a way to systematically combine a large number of separate recordings from baseline and perturbed preparations, thus allowing knowledge discovery (e.g. the types of transitions; the changes in the regular state that precede transitions) on those combined data.

tSNE and validating the clustering: the authors did considerable work related to this issue, by using their approach on synthetic data, replacing tSNE with UMAP, and by testing simple hierarchical and k-means clustering of their feature vectors. But none of these spoke directly to the validity of the clustering: the synthetic data and UMAP were still manually clustered, so could be made to conform to the desired results; the unsupervised clustering approach used shows the well-known problem that directly clustering a high-dimensional dataset (a 48-dimensional feature vector) is often impossible using classical techniques simply due to the curse of dimensionality. The normal approach here would be to use dimension reduction then unsupervised clustering (e.g. in the classic combination of PCA then k-means), matching the way the two steps are done in the present paper.

As the paper shows, the clusters found in tSNE by manual curation are arbitrary. For example, changing the perplexity parameter changes the fragmentation of the tSNE map, so would likely lead to different manual clusterings. In another example, the clusters found by manual curation are not all contiguous in the 2D space e.g. the LP-silent cluster is in 3 groups, one of which is on the opposite side of the 2D space to the others – so distance in this space is not interpreted as meaningful for all clusters. In another example, the dividing line between some "clusters" is arbitrarily put in a contiguous run of points – e.g. the LP-weak-skipped (pink) and irregular-bursting (brown).

So to me it seems we're still left with the original main issues raised, and consequently am still unclear who this paper is aimed at – this is a useful way for the lab who owns that data to organise it, but how useful is it in revealing the structure of dynamics in the CPG, and hence to others? Moreover, though the Discussion is much improved, the paper is still rather descriptive throughout.

These are clearly subjective concerns, not issues with the quality of the analyses done based on the clustering, which are solid, nor with their interpretation, which has been considerably improved. Nonetheless, I think the paper would still be considerably improved by a concerted redraft, and perhaps reorganisation, to deal with these issues.

Reviewer #2:

I appreciate that the authors carefully considered my review and tried new analyses (e.g. hierarchical clustering and UMAP) and have expanded the Discussion section to comment on the issues raised during review. I also agree that "a rigorous error analysis would be useful but is not trivially done" -- and since I do not have a concrete suggestion here, I think the manuscript should be published without one. Overall, I feel that my concerns have been satisfactorily addressed.

Reviewer #3:

One small remaining edit that would be helpful is to show the projection of the data onto the first two PCs (re: the PCA analysis referenced in Figure 2-Figure supp 2), so that the reader can visualize what structure there is prior to computing the triadic difference statistics. If not too computationally intensive, it would also be useful to show what emerges from applying a naive clustering or visualization algorithm directly on the spike-train time-series [see (2) in Reviewer #3 major concern], even if only to show that it is quite messy.
