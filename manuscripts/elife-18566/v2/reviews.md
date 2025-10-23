# Peer review - Round 1

Editors:
- Frances K Skinner, University Health Network , Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.18566.171](https://doi.org/10.7554/eLife.18566.171)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Interneuronal mechanisms of hippocampal theta oscillation in full-scale and rationally reduced models of the CA1 circuit" for consideration by eLife. Your article has been favorably evaluated by Eve Marder (Senior Editor) and three reviewers, one of whom, Frances K Skinner (Reviewer #1), is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors have developed a large-scale model of CA1 microcircuitry, with conductance-based models of nine distinct cell types. It is a treasure trove of highly intertwined model and experimental details, an impressive tour de force of bringing together much experimental detail in a cohesive, carefully constructed model that is open and accessible with available. The authors propose this as a first full-scale CA1 model capable of generating theta. Perturbation experiments show that some, but not all, of the neuron types are necessary to generate the theta rhythm, and conclude that the diversity of interneuron types is necessary to generate theta.

All reviewers recognized that putting this together was a herculean task and the commitment to open access was appreciated. However, there were also various concerns raised by all the reviewers. We truly understand the difficulty of writing and preparing these papers, with all of the concomitant decisions about what to include, so we hope that the following comments will give you a sense of how well the decisions you have made are "working" for the reader.

Essential revisions:

1) Coordination with companion paper and network clamp contribution to present paper

All the reviewers have had a chance to view the companion paper and it was felt that inclusion of the 'network clamp' in the present form in this manuscript was not a good fit as the present paper is a research article type. Rather, it was felt that the authors should focus on the scientific results of the work in the present paper. The authors should consider what important things have been demonstrated about the network by using the NetworkClamp tool. And even though it requires more full-scale simulations, they could make those changes to the full network model itself for the present paper.

i) For example, Panel 7E seems to be the essential one: show how theta is affected by reducing separately PV+ or SOM+ input by 90% – do these simulations for the full model here, and state them here. Then in the companion paper, they could show the current Figures 7 and 8 whereby the NetworkClamp tool achieves analogous results, but much more quickly. Also, then here they could make a reference to the SimTracker paper as a place where readers could learn more.

ii) As it stands, the description and proposed use of 'Network Clamp' is somewhat confusing. Comparison is made with being similar to in vivo (from perspective of a single pyramidal cell) – but the spontaneous theta is presented in reference to a whole hippocampus preparation (Goutagny et al. 2009, Amilhon et al.). Also, it is the case that one needs the full-scale simulation in the first place (to have the appropriate inputs), before using networkclamp, right? – Thus, the advantage in the present paper is not quite clear. Also, the CA3 and EC afferent inputs are still there – so that inhibitory sculpting and cross-validation comments unclear. Could they expand and explain use intentions more specifically?

iii) Subsection “Interneuronal contributions to theta oscillations in simplified models derived from the full-scale virtual CA1 network”, first paragraph: implies that Methods would provide greater detail on the implementation of the Network Clamp, but there is not any mention of it there. Was a section in Methods omitted by mistake? Is the "network clamp" just a theoretical concept that the authors implemented entirely by hand, or is it a mechanism that NEURON users could just add to their own network simulations? Unclear. Also, it sounds like presynaptic spike trains that are inputs to the pyramidal cell are entrained to theta, but that could be better articulated in a Methods subsection.

2) Clarity about overall goal/theta generation mechanism/experimental comparisons

i) Subsection “An accessible approach to modeling that balances detail, scale, flexibility and performance”, second paragraph: In commenting on the overall approach/strategy, the authors mention answering particular questions. The question presumably is about how theta is generated in CA1 microcircuitry (such as a whole hippocampus preparation of Goutagny et al.). If this is the case, the authors should state this explicitly.

Along these same lines, are the authors concerned about rat and mouse differences? (Goutagny et al. is rat, but Amilhon et al. is mouse, and model is rat, and both experimental papers are referred to and compared).

Model details are from rat CA1 (Bezaire and Soltesz), and in consideration with whole hippocampus prep of Goutagny et al. However, model comparisons are done with in vivo (e.g., subsection “Emergence of spontaneous theta and γ oscillations in the full-scale model in the absence of rhythmic external inputs”, fourth paragraph) with inhibition aspects, and the higher firing pyramidal cells to in vivo (rather than in whole hippocampus prep). Please be clear about what is used and being compared to and why, i.e., rationales given.

ii) If possible, the authors should provide a clear summary of the theta generation mechanism (assuming this is the question being asked). 'Factors' of diversity, etc. are given, but not really a generation mechanism it seems although it clearly seems to revolve around the 0.65Hz-based inputs. In essence, the authors should edit their paper to be clear about intentions and interpretation.

iii) The authors show that some interneuron diversity is necessary to generate theta. In particular, perturbing all interneurons to behave/look progressively more like one type of interneuron (PV+B) did not allow for generation of theta. Presumably in these simulations, all interneurons had identical passive/conductance/kinetic parameters? How much variance is there in firing patterns among PV+B cells characterized empirically? Might this variance in physiological firing properties be sufficient to generate the theta rhythm you observe within your CA1 model? This could be tested with one more round of simulations, similar to the network configuration in Figure 6D except the one constant set of intrinsic PV+B-like model parameters applied to all interneurons could be varied randomly within some set range.

iv) Subsection “Phase-preferential firing of interneurons in the full-scale model of the isolated CA1”, last paragraph and Figure 5A-B: Model vs. experiment differences occur in PV+B – which you then perturb to show how it related to the generation of theta. How do you explain that your model PV+B cells fire at the trough of theta, while experiments show them nearly in phase with the peaks? Is that what is meant by the "note" about the recording site in Ferguson et al. in these lines? (Similar question for the Ivy cells – though that is less important here Ivy's were not essential to the model's theta generation.) Otherwise – isn't this problematic since your exploration of PV+B was so essential to the Figure 6 content?

Subsection “Stimulation”, last paragraph: Figure 5—figure supplement 1 indicates large discrepancies between model and empirical data. Authors comment very little on this, but shouldn't this be a big deal?

v) Even though the network models were constrained by biological data, the models still failed to reproduce the experimentally observed theta modulated neuronal firing phases of principal and inhibitory neurons (e.g. see Figure 5). For instance, according to the Klausberger data the basket cell profile is that of a neural accumulator, that is it linearly rises till a max value and abruptly ends. However, the model BC response is gaussian/Bell shape! Can the authors comment as why this is case even though their circuit models are faithful representations of the real CA1 circuit in terms of cell numbers, connectivities, etc.? Are they still missing important components which were not included in their models? Can they comment (even speculate) which are these components?

vi) Subsection “Perturbation experiments indicate a key role for interneuronal diversity in the emergence of spontaneous theta”, second paragraph: – Data not shown for what happens when pyramidal cell connectivity removed – this is quite interesting as it is not many connections as authors point out, and may help the authors and others understand the mechanistic essence. Could more specifics be provided (or relevant Figure 6 and supplement be expanded?) when it is said theta rhythm collapses – does that mean no rhythm or higher frequency or unclear output or what?

vii) Subsection “Perturbation experiments indicate a key role for interneuronal diversity in the emergence of spontaneous theta”, last paragraph: It is said that goes from silent to hyperactive, but this does not seem to be the case in Figure 6E or supplement where the non-theta all seems to be around 3 Hz?

viii) Subsection “Emergence of theta oscillations from a biological data-driven, full-scale model of the CA1 network”, third paragraph: 33,500 spikes obtained in model – how was that determined, and presumably, with the 0.65 Hz input, how different is the number of spikes with larger or smaller frequency inputs (where they have shown the theta rhythm collapses)? This could be helpful in getting at the theta rhythm essence.

3) Model details

i) The description of intrinsic properties of individual neurons (passive and active parameters of the conductance-based models) is entirely missing from the paper, and inadequate on the model website. These model details need to be accessible forever, directly from the paper (or as supplementary information), not from an external website that could be discontinued. Yet even on the website, the information about individual neurons is incomplete/inconvenient to access. For example, a row of graphs about each channel in the model is included on the website (http://mariannebezaire.com/ca1_graphic/mymodel.html), but the axes of the graphs are not labeled. Do these show voltage activation curves? Distributions throughout the somato-dendritic axis? Are all ion channels included in each neuron type? Also, I found out by accident (website had no instructions) that manually clicking on each morphology sends you to a page with a set of tables and images with drop-down menus. It would have been helpful to provide text/tables summarizing channels included in each neuron type, with graphs of model vs. experimental traces and references to the exact equations for channel. It is essential for such information to be accessible from supplemental information, not an external site, unless it is a well-monitored, maintained, and curated site such as model DB.

ii) Such detailed models suffer from too much detail, which translates mathematically into thousands of parameters that need to be tweaked to simulate accurately and quantitatively the responses of cells in the networks. Did the authors use any optimization technique to constrain their model's responses other than calculated guises of biological detail?

The network models contained 1 excitatory principal cell type and 8 types inhibitory interneurons. These interneurons targeted specific compartments of the principal cells. But what about other types of excitatory cells? Also, what about inhibitory cells that targeted CA1 inhibitory cells (e.g. Chamberland, S., and Topolnik, L. (2012))?
