# Peer review - Round 1

Editors:
- Frances K Skinner, University Health Network , Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.06444.043](https://doi.org/10.7554/eLife.06444.043)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

[Editors’ note: this article was originally rejected after discussions between the reviewers, but the authors were invited to resubmit after an appeal against the decision.]

Thank you for choosing to send your work entitled “Noise promotes independent control of gamma oscillations and grid firing within a recurrent attractor network” for consideration at eLife. Your full submission has been evaluated by Eve Marder (Senior editor) and three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the decision was reached after discussions between the reviewers. Based on our discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife at this time.

While all the reviewers felt that the work was intriguing and could be of interest to the gamma oscillation, noise and grid cell community, there was concern that the present model was not consistent with existing experimental data. Specifically, discrepancies regarding inhibitory cell connectivity and recent experimental work (Buetfering et al., 2014) need to be addressed. It was felt that this would require re-doing and/or performing additional simulations to determine whether results remained the same. Further detailed comments for consideration are provided below. While you may choose to resubmit a revised manuscript, please note that substantial progress to address the reviewers' concerns is required for a subsequent review to be considered.

Reviewer #1:

The authors study the noise-sensitivity of a model previously introduced in a Neuron paper. The connectivity is different from other models for grid cells because there is no recurrent excitation; rather the stellate cells interact via inhibitory cells. To obtain nice oscillations it is helpful that cells have similar firing rates, however to encode information in the level of activity it is necessary that cells have different firing rates. The authors determine under what conditions both can be achieved simultaneously and find that there is an optimal noise level. The mechanism described bears some resemblance to study of an interneuron network by Tiesinga and Jose (2000) wherein noise reduces the effects of heterogeneity in firing rate on the level of gamma synchronization and increases the range of conductances for which oscillations are obtained, but at the price of neurons not firing on each cycle, similar to the results shown in the manuscript. The results are nice and I found the paper interesting.

In Figures 2 and 4 place fields are shown. I presume they are from E cells. What do the place fields for I cells look like? Does this conform to experimental data?

From the Neuron paper I gather that there is no recurrent excitation, but what is the evidence for the absence of mutual inhibition?

The neurons are connected all to all. Would an actual stochastic connectivity according to a probability that is scaled to the conductance pattern shown in Figure 1B, also work and provide the appropriate noise level?

The authors focus on varying synaptic strength gI and gE, which shows the robustness of oscillations/attractor states, but I would expect that synaptic strength of the network in vivo would not vary that much over time, or could that happen through synaptic plasticity effects? It would be nice to discuss the relevance of the conductance range investigated.

Reviewer #2:

I have only one major comment. This work is largely based on this lab's prior finding that layer II stellate cells do not show recurrent connectivity. This was a problem for standard attractor model connectivity, so the authors conceived the E-I-E attractor model. I think this is great. But, it remains possible that layer II pyramidal cells do show recurrent connectivity, which would support the standard attractor models. There is now controversy which cell types correspond to grid cells, and thus far the published (recent Neuron paper from Brecht's lab) and unpublished (David Roland's poster at SfN from the Moser lab) data suggest that both cell types in layer II are grid cells. Since pyramidal cells might/probably show recurrent connectivity, I would like to know if the same principles about noise emphasized by this paper would also apply to more standard E–E attractor models. I wouldn't ask the authors to explicitly model this, but do the authors have any insight about this that they could add to the Discussion? This is especially relevant to their very broad discussion about the beneficial role of noise in neural computation in general and the protective role of noise against seizures. Most cortical circuits have recurrent excitatory connectivity. Perhaps the authors could address more standard E–E attracter that contains global inhibition in their discussion.

Reviewer #3:

The authors created a recurrent attractor network, and investigated how noise affected synaptic activity at gamma frequencies and grid firing. Their recurrent attractor network incorporates E-I-E connectivity to produce grid firing through a velocity-dependent update of network attractor states, and also produce theta-nested gamma frequencies. They found that noise can increase the range of synaptic strengths with which gamma activity and grid computations are produced, and that synaptic gamma frequency and amplitude can be modulated independently from the grid firing.

In general, the manuscript was well-written, and the results logically follow from their model. However, fundamental questions about the model itself are important to consider. Recently, Buetfering and colleagues found that parvalbumin-positive (PV+) interneurons in the medial entorhinal cortex (MEC) integrate input form grid cells with various phases, and exhibited low spatial sparsity and no spatial periodicity (Buetfering et al., 2014. Nat Neurosci 17(5):710–718.). This argues against a scenario in which fast-spiking interneurons mediate grid cell phase-dependent recurrent inhibition in the MEC – a necessary component of the authors' recurrent attractor network model, where the activity bump in the E-cell population is reflected by an inverted bump in I-cell population activity. This discrepancy needs to be addressed.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for resubmitting your work entitled “Noise promotes independent control of gamma oscillations and grid firing within recurrent attractor networks” for further consideration at eLife. Your revised article has been favorably evaluated by Eve Marder (Senior editor), a Reviewing editor, and two additional reviewers.

The manuscript has been significantly improved and only minor revisions are required. Once you have addressed these trailing issues, the manuscript should be acceptable without further review.

Reviewer #1 Minor Comments:

I have one minor question, in their new Figure 2, they show unimodal spatial autocorrelation images of the I cells. This does occur in the Buetfering paper Figure 4A, but there are also a few with a weak periodic pattern (lower right panel of Figure 4A, grid score 0.18). Can this be found in the simulations as well?

Reviewer #2 (General assessment and major comments (Required)):

The authors responded to my comments adequately. In addition to the initial goal of exploring conductance parameters from E-I and I-E, the manuscript now provides substantially additional simulations to support E-I-E attractor models in general.

In their rebuttal the authors defend against the criticism that experimental data has not shown grid firing fields in inhibitory neurons. This criticism manifests from Buettfering et al., 2014 who report that PV interneurons do not show grid firing patterns. The authors have completed additional analyses and expanded their discussion to argue that these experimental data are no inconsistent with E-I models. (1) I cells in their model are weakly tuned grid cells (often below the gridness threshold used by Buettfering). (2) New simulations show that I cells show less grid-like activity when they are connected to uncorrelated grid cells. (3) The authors point out that Buetfering et al., 2014 only examine PV interneurons, and thus, other interneurons could exhibit grid firing fields. Overall I find these arguments convincing (especially #2), which fuel the debate about the structure of plausible E-I models and lead to new predictions (non-spatially correlated input to I cells, and/or other interneuron classes show grid properties). Close examination of experimental data show clear grids and not-so-clear grids (Krupic, Burgess, and O'Keefe, 2012) which may to correspond to firing on different theta phases (Newman and Hasselmo, 2014), similar to many interneuron classes in CA1 of the hippocampus.

The authors add I–I connectivity, consistent with their experimental data, and the model is robust. This suggestion and implementation has strengthened the manuscript.

My concern about E–E models has been addressed. While I do believe E–E models are still possible the authors correctly argue that this issue is far from settled. We do not yet have a clear understanding of MEC microcircuits, especially intralaminar connections that may or may not be needed for grid cell generation. However, the authors add additional simulations of E-E-I models, which provide similar results to the E-I models.

Reviewer #3:

Overall, we think that the authors have addressed our concerns. In particular, the additional simulations and discussions about how their findings relate to Buetfering et al. (2014), examining the effect of recurrent inhibition (I–I) has made the paper much stronger, and tying their results into some experimentally testable predictions.

The general results showing how different mechanisms could control grid activity and gamma oscillations are interesting, although a bit more of an explanation of the precise mechanisms of their gamma oscillation is needed (i.e., first paragraph of Discussion).
