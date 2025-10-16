# Peer review - Round 1

Editors:
- Mark T Nelson, University of Vermont United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.60208.sa1](https://doi.org/10.7554/eLife.60208.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript aims to quantify the local impact of a single capillary occlusion on blood flow using in silico approaches based on realistic models of mouse microvascular networks. The authors noted four different possible arrangements of flow into and out of a capillary segment and showed that there were differing impacts on flow in up and downstream vessels for capillary occlusions with these four different arrangements.

Decision letter after peer review:

Thank you for submitting your article "The severity of microstrokes depends on local vascular topology and baseline perfusion" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Laura Colgin as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Marilyn Cipolla (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

This manuscript aims to quantify the local impact of a single capillary occlusion on blood flow using in silico approaches based on realistic models of mouse microvascular networks. The authors noted four different possible arrangements of flow into and out of a capillary segment and showed that there were differing impacts on flow in up and downstream vessels for capillary occlusions with these four different arrangements. The authors then calculated the prevalence of these different arrangements in the capillary network, and later interpret these arrangements as having functionally distinct roles of blood flow redistribution vs. oxygen/nutrient exchange. The authors further calculated perfusion changes in tissue volumes due to single capillary occlusions for these different arrangements. They then examined the impact of the baseline flow rate, the depth into the cortex, and the distance from large penetrating vessels for the topological arrangement where an occlusion had the most severe impact on perfusion. The authors concluded that obstruction of capillaries that had two vessels flowing in and two flowing out had the largest impact on perfusion and that only baseline flow rate was predictive of the volume that saw reduced perfusion after occlusion of a single capillary with this two in and two out arrangement. The degree of perfusion impact suggest that single capillary occlusions do not likely lead to significant local tissue hypoxia. Finally, the authors examine how the location of a single capillary occlusion impacts the number of arteriole to venule paths through the capillary network.

Essential revisions:

General: There was a general consensus that to broaden the manuscripts appeal the authors should include a section on multiple micro-infarcts and transient stalls. The results, are somewhat narrow in scope, focusing on details of local flow rearrangements after single capillary occlusions and lacking a broader biological context or analysis of the impact of multiple occlusions (which is more relevant for disease states) that could make these findings of value to a broader scientific readership.

1. The number of cases tested for each condition is surprisingly small (eg 8 capillaries/type) and the variance in the results are calling for a much larger survey. This is similar across all the results presented. One would expect to see tens if not hundreds of cases tested for each type, across all simulations. Clearly, the data limits the amount of AD-to-AV cases but there are certainly enough capillaries to test for all the other experiments.

2a. Given the proximity of other vessels in the vicinity of the occluded capillary (some unaffected as shown by the authors, "Distant" class, Figure 2) what is the net impact of a capillary occlusion on tissue pO2? It is possible that the flow rearrangement observed by the authors (lines 231-233) counterbalance the loos of flow at the MSC keeping tissue pO2 constant (or close to) thus rendering MSC insignificant from this key physiological point of view. Therefore, this is the most crucial metric to compute as it will determine whether or not the MSC of different types do indeed lead to local ischemia; at least this should be shown for the "worst-case" scenario of 2-in-2-out. Further, it is plausible that the flow reduction in the vicinity of the MSC can allow for a larger fraction of oxygen to diffuse out of the nearby capillaries given the increased negative tissue-vessel gradient that will be generated. Combined with flow reorganization in non-affected vessels, this can lead to a net stable tissue pO2. Under such scenario, the statement in line 181-182 can be substantiated. Moreover, the relevance of MSCs is down-tuned by the reported 5% median inflow in the larger volume factor (lines 205-206).

2b. Related to the above, it is clear that this manuscript will be a cornerstone when it comes to interpreting future in vivo results. As such, the computation of tissue p02 will be extremely useful to guide such experiments.

3. With respect to the shortest distance used, the euclidean distance is of interest but the analysis should be done in terms of a "weighted" graph where resistance along the path is used. A comparison between the two is of much interest and might likely shed some interesting insight. Nevertheless, If opting for presenting one case, then the weighted one is the more relevant one.

4a. The authors have here the unique opportunity to increase the appeal of their work by including multiple-MSCs or multiple "stalls" scenarios. It is very intriguing to see in this manuscript how the presence of single MSC (and the subsequent reduction in flow in several other capillaries) increases the chances of subsequent MSC occurrence given the postulated link between initial decrease in flow (postulated as a potential mechanism for increasing the chances of MSC formation). The authors could titrate the concentration of such events based on recently published works that estimated "stall" occurrence in vivo.

4b. Is it possible for the authors to use published in vivo data to investigate what types of capillary topologies are reported with more "stalls"? Having such a comparison in this paper would be also very useful (on the same line as 2b comment).

5. There is a very interesting point made by the authors about the role of each topology (lines 544-547). This view calls for a balanced organization of the different topologies along the DA-AV flow paths. Is this indeed the case? The authors should plot the relative frequency of each type along flow paths; naively expected to be kept conserved. The opposite will weaken this view and likely point to a developmental epiphenomenon that results in a more or less random distribution of the different topologies.

6. The introduction to this manuscript is far too broad and sets up a larger problem to solve (with a focus on lack of ability to detect microstrokes in humans) for what was actually accomplished by the performed experiments. While it is good to introduce the larger picture, it is a bit misleading in terms of what the reader comes to expect after such an introduction. We recommend not only shortening it in length but also focusing it more on issues the study of flow networks are specifically able to speak to or help clarify in the field, rather than discussing uncertain implications for Alzheimer's disease pathology, for example. Perhaps emphasize the importance of investigating a single occlusion and the finding that a single occlusion is not enough to generate hypoxia likely to trigger pathology.

7. In terms of presentation of results, there was a general lack of statistical validation of trends or differences. There are several cases with large variability in simulation outcomes (e.g. the dark blue points in Figure 2f) that are not addressed. This variability and lack of statistical analysis of the results also calls into question whether the number of simulations used to generate this data was sufficient (a power analysis could prove useful here).

8. From a visual standpoint, we felt that while the results were clearly written for Figure 1, the figure itself (e to h) does not clearly show that there is a decrease in flow due to it being expressed as a relative change in flow. Figure 2 may benefit from showing a schematic representation of the volume factor, and removing the excessive horizontal gridlines (f to h). Figure 3 averages together two networks with quite different topological arrangements. It would make more sense to show the properties of these two networks independently (as in Supplementary Figure 7) in the main text. Figure 4 panel D is confusing: How can a flow path still go through the part of the vessel where a microstroke has been induced? The relevance of the decreased number of arteriole to venule flow paths after a capillary occlusion, as described in Figure 4, is also unclear. It would seem that the more biologically meaningful assay would be to explore how multiple occlusions impacted the number of flow paths and thus impacted regional perfusion. Finally, in section 3.5 a figure may be helpful to represent the finding about the geometric mixing of capillaries with different topological distances to arterioles and venules (defined as the AV-factor). It seems that this analysis could also be extended to explore how the variability of the average AV-factor of capillaries in a tissue volume varied with the size of the volume – a kind of 'smallest homogenous unit' analysis for the cortical capillary network.

9. The simulated area is small and the flow rates used also quite low. It's not clear why this was.

10. The information/data on the frequency and distribution of the different MSC-types in a realistic microvascular network is used on page 7. Where were these data obtained from?

11. The speculation that different capillary network configurations might confer distribution of blood flow and another to deliver oxygen and nutrients is interesting but not supported, yet, by data. Are there additional configurations that might be considered?

12. The authors appropriately used pressure values from Schmid that took them from published studies, however, some of those studies (Bohlen for example) used hypertensive rats. Did the authors consider normotensive or hypertensive conditions?
