# Peer review - Round 1

Editors:
- Fred Rieke, Howard Hughes Medical Institute, University of Washington United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.34238.054](https://doi.org/10.7554/eLife.34238.054)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Biophysics of object segmentation in a collision-detecting neuron" for consideration by eLife. Your article has been favorably evaluated by Eve Marder (Senior Editor) and three reviewers, one of whom, Fred Rieke (Reviewer #1), is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

All three reviewers agreed that the paper described a very interesting result and were enthusiastic about the approach. We also agreed that the paper could be strengthened in several ways. Four specific points follow; these and other points are detailed in the individual reviews.

1) Utility of the model. The model presented is quite complex and does not lead to a clear intuitive insight into how the interaction between HCN and KD type channels gives rise to looming sensitivity. The paper would benefit from more intuition about what the key properties are (time course, voltage dependence, etc.) that control interactions between these channels and give rise to looming sensitivity.

2) Inclusion of "standard" looming stimuli in analysis. It was unclear whether the standard looming stimuli were included in the fits in Figure 2J and 4C. This point would appear to impact the fits considerably.

3) Statistical tests. The paper is lacking statistical tests in several places. This includes analysis of significance for key results (a partial list includes the cAMP results and the slopes of lines in Figure 2E – but generally this should be addressed throughout the paper).

4) Division between main and supplementary figures. Some key pieces of data show up only in the supplementary figures (e.g., the pharmacology in Supplementary Figure 1). Supplementary Figure 4 is also quite central to the paper. The paper would benefit from inclusion of any key results in the main figures.

Reviewer #1:

This paper describes the basis of sensitivity of looming sensitivity in grasshopper LGMD neurons. The breadth of the paper – from single cell conductances to behavior – is impressive and the paper provides a rare link between the mechanistic basis of dendritic computation, neural responses and behavior. The general significance of the work is set up nicely in the Introduction. There are several issues that should be strengthened.

Abstract: The Abstract creates the simple expectation that HCN channels are going to explain looming sensitivity. Only later in the paper is it clear that it is the interaction of HCN channels and a depolarization-activated K channel. It would help to make this clear from the start.

HCN channel block. The pharmacology in Supplementary Figure 1 is quite central to the paper. I think it should also be included as a main figure. It also at present is restricted to example cells, and needs some population analysis. Further it is not clear why some experiments were in current clamp and others in voltage clamp.

Statistical tests. There are a number of effects for which significance should be evaluated. Some examples are: (1) the cAMP results in Figure 2F; (2) the slopes of the black lines in Supplementary Figure 4; (3) the slope in Figure 2E.

Figure 4 relies heavily on Supplementary Figure 4. Further, Supplementary Figure 4 is quite confusing. I think this entire analysis needs to be described more clearly and more of it needs to be included in the main text.

Reviewer #2:

In this manuscript, Dewell and Gabbiani examine molecular mechanisms underlying loom detection in the LGMD neuron in locust. The use a clever stimulus in which they can continuously modulate the coherence of a loom-like stimulus to investigate how different channels affect the coherence tuning of the LGMD response. First, they show that LGMD neurons show a sag under hyperpolarization that is cAMP-modulated and is eliminated by an antagonist to HCN channels. Using this antagonist, they show various properties of LGMD responses that depend on HCN channels, but show that these properties alone do not account for the coherence tuning of the neurons. This antagonist also reduces the jump rate for fully coherent stimuli. They use a second antagonist to show that potassium channels are also involved in coherence tuning, but show somewhat opposing effects to the HCN channels. Finally, the authors conclude with a realistic model of LGMD firing, including many channels and compartments, and show that after tuning parameters, they reproduce some of their data with this model, importantly reproducing the primary effects of the HCN and potassium channels on the loom coherence tuning curves.

The coherence knob on the loom stimuli is clever and a useful way to interrogate these mechanisms, and I found the pharmacology and measurements all mostly convincing and well-presented, with a few small points enumerated below. My major concern was with the modeling. I've read through these sections three or four times now, and it's still not clear to me what is going on. Some of this speaks to presentation, and I think this could be improved. But one question is: what is the purpose of the model? A detailed model with thousands of compartments and many fitted parameters can be used to determine whether you're missing any crucial components in principle, by asking whether the sophisticated model can reproduce results with verisimilitude? But such models typically won't give an intuition for what's going on. I want a model that gives me intuition about the biophysical processes involved. In the supplement, the authors say that this is the simplest model that reproduces the results, but surely there must be a toy model with fewer and more simply arranged spatial compartments that would give intuition for some specific coherence results, even if it didn't reproduce things exactly. In part, Figure 7 gave me pause because this coherence/incoherence is necessarily a spatiotemporal integration issue, as the authors emphasize in the introduction, but the schematic has a single spatial compartment. To really get what's going on, we need at least two compartments. Or a one-dimensional chain of compartments with an edge sweeping across, which could show currents/activations/voltages at different time-points during the coherent vs. incoherent edge? I'd really like to have a better intuition for what is happening, and what timescales matter for the HCN activity and its inactivation of the KD-like channels.

Reviewer #3:

Dewell and Gabbiani use a novel visual 'looming' stimuli of varying spatial coherence. With the aid of pharmacological intervention, the authors explore mechanisms underlying response characteristics of looming neurons (and escape behaviors) in the grasshopper. Here they provide evidence that spatiotemporal patterning on the LGMD neuron's dendrites induced by looming stimuli, elicit responses via HCN and other channel dynamics. Whether and how neurons use broad spatial components of the dendritic input statistics to compute information (rather than via presynaptic mechanisms) is an important question in the neurosciences of interest to a general audience.

1) I have an important question with respect to data analysis. In the critical Figure 2J, the authors chose to include a standard loom in addition to a 100% coherence loom (effectively two data points at 100%), though the reasoning for this is not provided. Does the line of best fit (red) include the standard loom ('star') data point at 100% coherence? If so, why would this 'standard loom' stimulus composed of very different frequency components be added to this analysis? The primary hypothesis of this manuscript depends on the slope of this line to increasing coherence (coherence preference) and this selectivity looks to be largely affected by the presence of this additional, confounding data (standard vs. 100% coarse).

What is the coherence preference for ZD7288 with this point removed and is it still significantly different than control (Figure 2K)? If not, why not? If the slopes of these lines are not significantly different, then the parsimonious explanation for the data set is that the ZD7288 is causing something akin to the hyperpolarizing injection of current (Supplementary Figure 3D). Testing for a significant difference between the coherence preference for ZDZ7288 (without standard loom) with that obtained for the.-2.5nA current injection would make the author's point more convincing. In fact for ease of comparison, coherence preferences for all conditions (control, ZD7288, 4AP, Cs+, -2.5dc) could be presented in a single figure (with error bars and tests for significance). The authors may then like to develop hypotheses with respect to response differences in standard loom compared to 100% coherence coarse loom induced by HCN blockade.

Note that a similar 'extra' data point seems to also be having a very large impact on the 4AP result (Figure 4C).

Additionally, as the primary interpretation is from the slope rather than the overall strength of these lines of best fit (Figure 2J), the reader should be provided (a) the analysis window used for spike count (b) the y-intercept (0% coherence) relationship to any spontaneous activity and (c) why a single control data point was used as the normalization (% max). To further complicate matters, the individual data underlying Figure 2J presented in Supplementary Figure 3A strangely shows a weighted line (with data points) for one single example, rather than the average. It is in fact this Supplementary Figure 3A (the non-highly derived) that makes the authors point much more convincing, with most red lines looking flat – however the authors should again separate standard vs. 100% coarse loom to be fully validated.

For their main hypothesis to be supported, I believe the authors should start again with Figure 2J and 2K. Calculating the mean, spike counts (from Supplementary Figure 3A), without including the standard zoom. If a normalizing factor must be used, one less dependent on a single value would be better (e.g. mean across all coherences).

Following, the rest of the manuscript flows very well, delving further into proposed mechanisms underlying this preference. This includes solid proposals of interactions between HCN and voltage-gated K+ channels, and robust modeling efforts.

2) Figure 2I reveals interesting time courses of control and ZD7288 that are not discussed in further depth. With intracellular application of ZD7288 the spiking activity (red dashed line) ends earlier than control. This is not simply a gain scaling, as response onset initially builds with the same time course as the control. These waveforms are also different with the extracellular applications.

How do these differences in time course affect further analysis? That is, what is the time window considered for calculating spike count? Do the model simulations explain any of these interesting temporal dynamics? Furthermore, if peak spike rates were used instead, would the calculated coherence preference across conditions exhibit similar traits?

3) It is not clear in the main text when individual trials (across animals) are considered as independent samples for the statistical tests. Or if and when such replicates are averaged into a single sample.

4) Although data in Figure 2K is presented as median and the authors applied a paired t-test (similarly in other tests). However, there is not a solid description of the ordering of these paired interventions. I presume the solutions could not be washed out, therefore all these results are with controls first, followed by treatments. Although the authors cannot get around this difficulty, it should be described clearly so that readers can consider confounding factors such as animal fatigue and neuronal habituation on such responses.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Biophysics of object segmentation in a collision-detecting neuron" for further consideration at eLife. Your revised article has been favorably evaluated by Eve Marder as the Senior Editor, and Fred Rieke as the Reviewing Editor. The original reviewers were consulted but were not asked for formal reviews.

This is a revision of an interesting paper on dendritic computation in a visually-sensitive neuron in grasshopper. The paper has improved in revision, but a few issues remain. These all center around making the paper maximally accessible to a broad audience. Most generally, the model is still difficult, and I would encourage the authors to take another pass through that section to see if it can be clarified further (some specific suggestions are below).

Abstract, penultimate sentence: This sentence could get broken into two for clarity.

Subsection HCN channels in dendritic field A are implicated in coherence tuning”, end of first paragraph: This is where you first introduce HCN channels as a possible mechanism for selective responses to coherent motion. You could expand the proposal here a bit, as it is not immediately clear how HCN channels would serve this function (and it later becomes clear that they do not by themselves). An interested reader will be trying to develop a conceptual framework at this point in the paper, and likely will be confused about the proposal. A similar issue comes up in the last paragraph of the aforementioned subsection and in the first paragraph of the subsection “HCN channels mediate coherence tuning of escape behaviors”. In all these cases a reader thinking about how HCN would mediate the observed effects will likely be confused. The intuition for the role of HCN comes in the subsection “HCN channels affect membrane properties and synaptic summation” – I think this should come earlier.

"A similar result held[…]" – not sure you mean similar here, as that most naturally would mean larger and faster from previous sentence.

Subsection “HCN channels in dendritic field A are implicated in coherence tuning” (and thereafter): I think an implicit assumption is that the current you measure is dominated by gH. It would be good to state this assumption explicitly.

Subsection “Compartmental modeling highlights role of K+ and Ca2+ channel inactivation in coherence tuning”, fourth paragraph: this paragraph is tough because of the back and forth between activation and inactivation. Is there a simple way to illustrate the interplay between voltage, HCN channel activity and KD inactivation? Maybe with activation and inactivation curves for KD and the range of voltages explored with and without HCN channels?

Figure 7D: it would be helpful to describe more fully here why full inactivation is important, as opposed for example to modulation of the level inactivation (which looks larger with HCN channels blocked).

Figure 6D/E: Some statistics are needed here.

Subsection “Compartmental modeling highlights role of K+ and Ca2+ channel inactivation in coherence tuning”, fourth paragraph: reference to Figure 7C seems out of place here.

Figure 7G: Can you do these same calculations with HCN blocked?

Subsection “Compartmental modeling highlights role of K+ and Ca2+ channel inactivation in coherence tuning”, last paragraph: I think ending the results with the transient calcium channel part weakens the paper a bit since that is the last thing a reader walks away with, and that is the least established part of the paper.

Discussion, second paragraph: I think sodium or calcium channels could provide spatial selectivity – if you agree this sentence should get modified.

"increases in bursting.[…] " is awkward.

Discussion: there is a good deal of text in the Discussion that goes back over the model and how multiple channel types act together. I think this could get consolidated in the Results, and made briefer in the Discussion.
