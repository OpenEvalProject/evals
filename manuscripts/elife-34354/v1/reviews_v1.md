# Peer review - Round 1

Editors:
- Lila Davachi, New York University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.34354.017](https://doi.org/10.7554/eLife.34354.017)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Macro-connectomics and microstructure predict dynamic plasticity patterns in the non-human primate brain" for consideration by eLife. Your article has been reviewed by David Van Essen as the Senior Editor, a Reviewing Editor, and three reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Mikail Rubinov (Reviewer #1); Rosanna Olsen (Reviewer #2); Katherine Duncan (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The reviewers all felt that the dataset is exciting and unique and that the analyses conducted and presented in the paper provide a comprehensive investigation into neural reorganization following a brain injury.

However, they all agreed that there are improvements to be made to the statistical approach and presentation of the results. First, and foremost, it was noted that the analyses do not capitalize on the longitudinal nature of the dataset. Instead, analyses of the data are treated as if they are all independent even though the 3-month period data is included in both dependent measures and differences across animals not properly accounted for. Thus, it would be important to adopt mixed linear models to account for variance across animals (notably, these models can deal with missing data and allow a repeated measures approach).

The reviewers also agreed that the description of the results was very hard to follow. Reviewer 1 pointed out that the authors have taken a 'kitchen-sink' approach without building a logical flow of data presentation. I won't go into detail here but instead am choosing to append the specific reviews in this case because I think they will be very helpful in your revision.

Reviewer #1:

The study presents analyses of a unique dataset; the effects in my view are novel and interesting. Having said this, I find the main network analyses of this data to be quite clunky. The authors have taken a "kitchen-sink" approach by applying a large group of analysis tools to their data, without carefully considering which of these tools may describe the primary or most important effects and which may describe redundant secondary correlations or byproducts. More specifically, the study describes reductions and increases in individual connections, changes in within-module and between-module connectivity, changes of node strength, participation coefficient, coreness, rich clubness and modularity. Many of these measures undoubtedly correlate with each other which paradoxically seeks not to clarify but to obfuscate the general picture. I discuss my main concerns below in more detail.

1) It would be most useful to first ascertain if the authors have observed any simple changes in the signal which may drive the downstream effects. For example, I couldn't find if the authors have examined changes in functional connectivity distributions (as well as the mean overall connectivity) before and after lesioning.

2) A complementary analysis could also consider the presence of a specific subnetwork affected after lesions (presumably this subnetwork would focus on the hippocampus). An objective and data-driven way to achieve this would be to employ the Network-Based Statistic (Zalesky, 2010). Together analyses 1 and 2 would allow us to gain a basic picture of changes in the localized pattern of network organization.

3) Much of the authors' analyses (modularity, participation coefficient, within and between module connectivity) relies on an accurate clustering of the network into modules or communities. However, running Louvain community detection with default parameters often results in issues with the resolution limit (Fortunato, 2007), which may underestimate the total number of modules. The authors should consider the extent to which their observed effects are robust to the number of modules chosen in the algorithm. Can they estimate in a principled way if the number of modules changes before and after lesioning? Again, the default Louvain algorithm produces a fairly arbitrary resolution of module partitioning. See e.g. Newman, 2016 and Fortunato, 2016 for details.

4) It is quite confusing to refer to within-module connectivity and strength as local connectivity and to between-module connectivity and participation coefficient as long-range connectivity. These are distinct concepts which are studied separately and do not necessarily coincide (e.g. individual within-module connections can also be long-range). If the authors truly wish to consider local and long-range connectivity, they should define these concepts directly based on connection length criteria (e.g. Sepulcre, 2010). Alternatively, they should describe the effects in more direct terms (namely, within and between module connectivity).

5)Several other studies have considered the relationship between centrality and cytoarchitectural density, I wonder if the authors are familiar with these results – they should be mentioned and discussed in the paper. See for example Beul, 2015/2017 Scholtens and van den Heuvel, 2014/2015 and Rubinov, 2015.

6) Hubs and modules, rich-club and core-periphery all describe essentially the same properties. See Rubinov (2016) for details. As mentioned above, running many redundant analyses seems not to clarify but conversely to obfuscate the primary effects.

Reviewer #2:

This was a novel, comprehensive investigation into neural reorganization following a brain injury. The authors should be commended for undertaking this rigorous and ambitious study. Below I will list some of the limitations as well as some clarification questions.

The paper nicely outlines the motivation to study neural reorganization, both acutely and after recovery, due to local brain lesions. While this question is indeed important, the current data only speak to the nature of brain organization due to lesions to a single region of the brain (the hippocampus). While, in my mind, this focus is well-motivated due to the dramatic effect of hippocampal lesions on memory function, I felt there was a bit of a disconnect between how the investigation was framed at the outset and the specific methods used here. A justification in the Introduction about why the hippocampus was the target of the current investigation is warranted, given the broad readership of eLife.

Similarly, the authors speculate that neural plasticity following lesions is highly dependent on the cellular makeup of different brain regions. It seems that the cellular makeup of the lesioned region itself could also drastically determine the nature of the neural reorganization following injury. Thus, the conclusions about how the brain is transformed due to local injury are somewhat limited.

The authors speculate that the patterns of plasticity during the chronic stage could relate to recovery of function. It is also stated in the Materials and methods section that behavioural data on a memory task was reported in Browning, 2012 (Note: I could not find this report as the reference was incomplete). A critical next question is whether these neuroplastic changes reflect cognitive recovery. Could the authors refer to existing studies that have examined the recovery of function in either non-human animals or humans to tie the brain changes observed here to cognitive changes following brain injury?

Changes to the extended hippocampal system have been reported in cases of developmental amnesia (Rosenbaum, Gao et al., 2015; Dziecol et al., 2017). These individuals have alterations to the fornix, mammillary bodies, and thalamus, similar to the grey matter changes reported in the current work.

The authors characterize grey matter changes due to injury, but do not comment on which white matter tracts were also affected. Can the authors determine whether the alveus, fimbria, and fornix were damaged by the lesions (or altered post-injury)?

The authors state that "statistically significant grey matter loss was restricted to subcortical areas that were monosynaptically connected to the hippocampus." However, there seems to be more regions affected than those listed in the results listed in the text. For example, in Figure 1C, LGN also seems to be affected.

It is stated that the hippocampus was the fourth best predictor of acute changes in long-range connectivity, which leads me to wonder what were the top 3 regions? Is it surprising that there are regions that predict connectivity to a greater extent than the region that was directly lesioned?

Reviewer #3:

Strengths:

This manuscript contains a detailed analysis of an exciting and rare dataset - a longitudinal record of functional connectivity and grey matter volume changes resulting from circumscribed lesions to the hippocampus. The findings from this well-controlled animal study have clear and important implications for both clinical and basic research questions in humans.

Concerns:

1) Defining the chronic phase as changes between 3 months and 12 months can lead to interpretative challenges. Can the authors provide clear criteria for which changes can be interpreted as recovery and which as further disruption? It seems as though both the pre-lesion and 3-month points would be required to constrain the interpretation. Relatedly, including the 3-month estimates in both dependent measures (0-3month and 3month-12mount) means that these measurements are not independent. E.g., is the relationship between hippocampal connectivity and increases in chronic long-range connectivity evidence that pre-lesion hippocampal connectivity predicts greater recovery or that it predicts greater acute disruption (as was separately reported).

2) The longitudinal repeated measurements could be a real strength of this paper, but the analyses do not capitalize on the design. Instead, all measurements are treated as "independent." I would strongly recommend using mixed linear models to account for, what I anticipate to be, significant differences across animals given the variable population and lesion extent. These models can accommodate missing data, addressing the authors' reasons for not accounting for the repeated measures. Alternatively, the authors could report the key findings in each animal to qualitatively document how reliable the observed relationships are across animals. At a minimum, more detail needs to be added to current analyses descriptions. E.g., are the results across animals averaged to create a signal estimates prior to entry into the GLM? I assume this was done based on the graphs, but it should be stated. I would also encourage authors to consider analyses that track changes across time within animals. The finding that chronic changes in GM volume are related to acute changes in connectivity is very interesting but raises other questions about the temporal dependence of plasticity changes.

3) I found the presentation of results hard to follow. For example, the GM volume results were split into two distant sections. Additionally, partial models were presented in various forms before the full models, despite the full model often being required to accurately interpret the relationships. I would recommend organizing the Results section according to the three dependent measures, beginning each section with the full models and only reporting partial models when necessary. It would also be helpful to include a correlation matrix for the independent variables to address the independence of these metrics before entering them into a model. The table at the end of the Results section did help to pull the sections together, but some reorganization could add clarity throughout.

4) There should be some discussion of how the excitotoxic lesions compare to common causes of brain damage in humans and the degree to which these results could be expected to generalize given these differences.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for submitting your article "Macro-connectomics and microstructure predict dynamic plasticity patterns in the non-human primate brain" for consideration by eLife. Your article has been reviewed by Eve Marder as the Senior Editor, a Reviewing Editor, and three reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Mikail Rubinov (Reviewer #1); Rosanna Olsen (Reviewer #2); Katherine Duncan (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

This revision was very responsive to many of the concerns noted and the reviewers are still supportive of the paper. However, they also agreed that further statistical analyses of existing data are needed to build confidence that the reported effects are not driven simply by the use of different monkeys at different timepoints. This is absolutely critical to address. Furthermore, a few additional discussion points should also be added.

Essential revisions:

In the original round of revisions, it was requested that the authors adopt some way to account for repeated measures or to assure that there was evidence that the reported effects are not simply driven by the fact that different monkeys are used at the different timepoints.

In the response, it was claimed that mixed models could not be constructed for their primary analyses. The logic presented however is not clear. For example, a mixed model could be constructed by predicting each observation (e.g. acute change in network participation for region 1, region 2, and so on; N.regions x N.monkey rows) by the four factors of interest as fixed effects along with a random intercept (and ideally random slopes corresponding to each fixed effect) grouped by monkey. The results from this approach would indicate how reliable the observed relationships are across monkeys and, thus, how generalizable they may be.

It would be also be important to demonstrate in some way that major conclusions are driven by patterns that can be consistently observed across monkeys. Given the large amount of missing data, it's possible that some of the differences between acute and chronic time points merely reflect differences in the monkey populations with data at those times. Even qualitatively replicating the reported patterns in the two monkeys with full datasets could alleviate this concern.

In response to reviewer 1, you now briefly report very strong changes to the overall connectivity across the brain but these results are not well integrated with the other dependent measures. How do the four predictors relate to overall functional connectivity? One specific question that arises is with respect to hubness, the most reliable factor, similarly predicted within module connectivity and network participation; would it be more parsimonious to interpret this relationship as being with overall connectivity?

Finally, it is challenging for the reader to understand the relationship between the continuous hubness predictor used in the first half of the results and the three categories of hubs presented in the second half. Specifically, do non-hubs, provincial hubs, and connector hubs systematically map onto different levels of 'hubness', and does the categorical partitioning of hubness into these levels explain changes in network participation above and beyond what hubness can? This may be a remnant of your original very comprehensive, but dense, reporting. We recommend adopting one well-motivated representation of centrality, unless there is a good reason to do otherwise?
