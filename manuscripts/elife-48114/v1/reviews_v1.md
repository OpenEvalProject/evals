# Peer review - Round 1

Editors:
- Vatsala Thirumalai, National Centre for Biological Sciences India

Reviewers:
- Vatsala Thirumalai, National Centre for Biological Sciences India

## Review text

DOI: [10.7554/eLife.48114.037](https://doi.org/10.7554/eLife.48114.037)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "A pretectal command system controls hunting behaviour" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Vatsala Thirumalai as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Ronald Calabrese as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this manuscript, the authors uncover the role of a group of pretectal neurons in generating hunting behaviour in larval zebrafish. By using an impressive combination of techniques and detailed functional, anatomical and behavioural analyses the authors have identified a brain region that contains a fraction of cells that can be stimulated to induce hunting-like behaviour and ablated to diminish the same behaviour. This work is technically impressive and the conceptual presentation is excellent. The activation of single neurons to induce hunting-like behaviour is already impressive, and the authors go beyond that by identifying fish that do show behavioural responses on activating a given cell, and image the same cell in that fish in a virtual behavioural assay to functionally characterize it. The reviewers suggest the following essential revisions to improve what is an already strong manuscript.

Essential revisions:

The authors make a strong statement that these neurons constitute a 'command system' for initiating hunting based on their finding that activation of single neurons could elicit hunting routines even in the absence of prey-like stimuli. However, the reviewers felt that such a strong claim was not sufficiently substantiated by the data presented for the following reasons:

1) Each neuron that was able to trigger prey capture did so only in a minority of trials (~18%) and did so with very long latencies (~4s). If they think that the optogenetic stimulation is triggering hunts by direct activation of AF7-pretec neurons, why is it successful only in a small percentage of trials and why does it take several seconds especially in the case of the neurons that project to the nMLF? Previous reports (Thiele et al., 2014; Del Maschio et al., 2017) suggest that direct activation of nMLF generates tail bends in less than a second after photostimulation. Even if AF7-pretec were 1-3 synapses away, delay seems longer than would be predicted for a command system. If this is likely due to low levels of stimulation of ChR2, did the authors test a range of light intensities? A likely alternative interpretation would be that AF7-pretec neurons encode "prey" value – activation of these neurons signal the existence of prey in the visual field, which then increases the probability of downstream generation of the hunting command.

2) The criterion for deciding that the stimulation induced a "hunting routine" is only observing a "period with ocular vergence above threshold". An alternative explanation would be that these neurons are premotor neurons driving eye vergence, and when the animal finds its eyes converged, it responds (with some delay) with a tail movement. Can the authors rule this out?

Given these concerns, the reviewers suggest that the authors reconsider their nomenclature of these neurons as a command system. The results are entirely consistent with the AF7-pretectal neurons playing a 'hunt-promoting' role. Indeed, this study parallels a recently published study (Zhao et al., 2019) identifying GABAergic neurons in zona incerta of mice as 'hunt-promoting' based on similar lines of experimentation. We believe that toning down on the "command system" hypothesis and instead positing this group of neurons as a "hunt-promoting" nucleus will be closer to the results and yet not take away from the importance of these findings.

In addition, reviewers have the following suggestions grouped broadly into experiments, analysis and presentation:

Experiments:

1) The authors stimulate single neurons using the KalTA4u508 reagent. They do not report on the results of stimulating the entire population of AF7-pretectal neurons labeled by the KalTA4u508 stable transgenic line. Is this because the line labels many neurons elsewhere in the brain? If not, it would be important to include this information. It is also essential to provide more information on the expression pattern in the KalTA4u508 line across all regions of the brain and in the spinal cord.

2) Authors ablated these neurons to show effects on hunting. However, the control included no photo-ablation of any cells, and therefore does not control for damage to other nearby cells, or axons of RGCs. The authors should either perform a control with ablation of similar numbers of cells nearby, or justify the current control experiment in the text while acknowledging any shortcomings.

Analysis:

1) There is no 'Eye vergence only' regressor included in the analysis of activity. If the authors claim that eye convergence without tail movement never occurs then this might be important to show explicitly (again making clear what the delays are between the eye and tail movements).

2) Clustering: To obtain their functional clusters, the authors cluster the top 5% responsive neurons then assign the rest of the neurons to these clusters based on distance to cluster centroids. This analysis would need some additional information to make it more transparent. (a) What is the distribution between the cells selected with the two criteria, namely, high visually evoked activity or well modeled in terms of motor variables? (b) What numbers of cells formed the seeds for the 36 clusters (min-max range and median)? It is also recommended to add this criteria (that clustering was done on 5% of cells) in the Results text as well.

3) It was hard to be sure that the description of AF7 neurons scoring high on the "hunting index" (HIx) was a significant result as opposed to falling out of the nature of the regression. HIx measures predominance of activity during hunting as compared to non-response trials. But, in a sense, these are correlated: clustering picks out those cells having motor responses, hence likely to have a high HIx? What is the additional value of the HIx?

4) Figure 1E and F: In Bianco and Engert (2015), using the same moving spot paradigm the authors find that the "distribution of spot locations at time of convergent saccade did not differ for left-right versus right-left stimuli". In contrast this manuscript shows in Figure 1E and F a difference for left to right vs. right to left stimuli. Is this significant? What might account for this difference?

5) Cluster 26 and 28 show lateralized responses and in the fifth paragraph of the subsection “Pretectal neurons are recruited during hunting initiation”, authors state that their distributions are also lateralized but Figure 1—figure supplement 2D shows about equal numbers for cluster 26 on both sides. An explanation seems necessary.

Presentation:

1) The authors need to be clearer about the nature of the visuomotor vector that they use to regress Ca fluorescence. Is it possible to visualize an example VMV or two in the supplementary figures? The figures could be better explicated: for example, in Figure 1G, meaning of terms such as "Conv tail sym" are not immediately obvious until one gets fairly deep into the Materials and methods section.

2) To help the reader, the four tightly packed figures should be broken into perhaps 6 or 7. Currently, each figure is so dense that the font sizes are difficult to read. Further, it is harder to follow the logic when each figure is making multiple, often complex, points. Specifically, Figure 1J-O could become their own figure. The relevant subset of data shown in Figure 1—figure supplement 2A (i.e., the calcium responses during hunting and non-response for the key clusters of 1, 4, and 25-28) could be brought forward into that figure or another new figure. Figure 2 could likewise be split into anatomy of the AF7 neurons and their behavioral responses. The authors make a very nice analysis of the effect of the anterior ventral optic tectum (avOT) and retinal inputs on prey capture behavior. Unfortunately this has been placed in a supplementary figure (Figure 4—figure supplement 1). We would suggest that this be made into a figure on its own.

3) Subsection “Pretectal neurons labelled by KalTA4u508 with hunting-initiation activity”, fourth paragraph: It's notable that the KalTA4u508 neurons don't respond to visual stimuli alone, in marked contrast to the clusters of which they are members (cf. Figure 1N). Presumably this is because these neurons are a small subset of those clusters, but the authors should acknowledge this distinction in the Results and perhaps speculate on the implications – other cluster members must have more significant visual responses.

4) The Introduction and Discussion should be rewritten to position the AF7-pretectal neurons as a hunt-promoting nucleus instead of a command system. The title should also be suitably modified. It is best to avoid poorly defined terms such as 'behavioral epistasis' (in describing the interaction between avOT and AF7-pretec).
