# Peer review - Round 1

Editors:
- Saskia Haegens, https://ror.org/00hj8s172 Columbia University College of Physicians and Surgeons United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67684.sa0](https://doi.org/10.7554/eLife.67684.sa0)

This valuable work introduces a detailed computational model to elucidate the underpinnings of experimentally observed coordinated rhythmic dynamics across brain regions. It provides a solid step towards understanding rhythmic attention. The work will be of interest to neuroscientists working on brain rhythms and attention from a cognitive, systems or computational perspective.


---

# Peer review - Round 1

Editors:
- Saskia Haegens, https://ror.org/00hj8s172 Columbia University College of Physicians and Surgeons United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.67684.sa1](https://doi.org/10.7554/eLife.67684.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Interacting rhythms enhance sensitivity of target detection in a fronto-parietal computational model of visual attention" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Floris de Lange as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

After discussion, the reviewers and editors agreed that the work has potential but is currently missing some key aspects. In terms of generalizability, a clear explanation of the key mechanisms of the model is missing. The work focuses more on reproducing the data rather than introducing mechanisms that might be used by the brain for other tasks. Main concerns, as detailed in the reviews below, include lack of justification of parameter choices (which often are given without explanation), and regarding spatial structure in the model reflecting the spatial structure of the task and physiology, which currently is very limited.

Reviewer #1 (Recommendations for the authors):

1) The authors should provide more detailed explanations for the choice of the model architecture. In this way, the reader can understand if the selected model features correspond to assumptions based on experimental literature or, instead, model predictions. Several features of the model are based on rodent data (e.g. Karnani et al., 2016 and Zhang et al. 2014 at lines 278). Consistently with this choice, the authors should then explain the justification for the self-inhibition of the SOM population in the visuo-motor module of FEF (Figure 2) given that these connections are virtually absent in the mouse visual cortex (Pfeffer et al., 2013 Nat. Neurosci.). Other key architectural choices which differ from the results in Pfeffer et al. (2013) and need to be clarified are: FS cells being absent and SOM not inhibiting VIP in the visuo-motor FEF module. Additionally, In mice, there is a high density of VIP cells in the superficial layers (Kim et al., 2017 Cell) so the authors should justify the absence of VIP cells in the superficial layers of LIP. Also, the authors should justify why the RS cells in the superficial layers of LIP are not self-exciting given the existence of strong recurrent excitatory connections (e.g. Cossell et al., 2015 Nature). Finally, the author should explain how the different parameters described in tables 1-10 were chosen (including whether they originate from measurements in the rodent or in the primate brain). More specifically, the authors should explain which of these parameters are based on the experimental literature and which of them are chosen to reproduce the oscillatory dynamics presented in the paper.

2) It seems that the model is not taking into consideration the spatial structure of the task, except for the FEF visual cells. As the author mention in line 38, the experimental literature shows that the rhythm of hit rates depends on whether the target is at the cued (8 Hz) or uncued (4 Hz) location. I would have expected the model to have working memory neurons to encode the position of the cue and then decision cells to use this information and produce hit rates that depend on the position of the target relative to the cue. Instead, the authors limit their discussion regarding changes in hit rate rhythms to a possible change in LIP to FEF connectivity without any mention of the spatial structure of the network. If possible, the authors should include a more clear spatial structure to the model. Otherwise, the authors should provide a more clear explanation of their choice.

3) The model is fairly complex and it will benefit the paper to increase the explanatory power of most of the figures. In particular, the authors should add spectrograms of the RS cells described in Figure 3B to show how the different bands wax and wane as a function of the theta phase (this is shown only for the FEF visuomotor cells in Figure 5 at the moment). For example, it is not clear from Figure 3B that during the poor θ phase, LIP produces a β1 rhythm. Also, the authors should label all the cell types in the model outlines of Figure 3A, 4A, 5A and 6A, 10 and 11 and, possibly, mention in these panels which rhythm is present in each external input. Finally, I recommend moving Figure 2 to Figure 1 to facilitate a comprehensive understanding of the relationship between the model and the empirical findings.

Reviewer #2 (Recommendations for the authors):

1, Apparently, from the model setting, gap junctions play an essential role in getting the results. However, is there any experimental evidence showing that such widespread and strong gap junctional coupling (the modeling used in this paper) exists between LIP and FEF neurons? To me, there is very few reports of gap junction between these two brain areas. Although, generally speaking, gap junction has higher probability to appear between cortical interneurons, but the coupling coefficients (cc) of such gap junctional coupling is very small, compared to what used in this study. So, please justify why consider gap junctions between excitatory neurons, and why with such strong strengths? It appears that the gap junction used in the present paper is too strong, such that the spikings of LIP and FEF neurons are too synchronized, making the rhythms generated in these two areas appear to be rather "artificial" (see more questions see below). BTW, what does the "LIP superficial SI cells" refer to in line 711? This kind of cell is not reported above.

2, The synapse types (inhibitory / excitatory) between neurons are unclear in the model diagram of Figure 2, Figure 3A, Figure 4A, Figure 5(a) and Figure 6(a).

3, The authors stated their model is capable of producing the γ,β_1,β_2 rhythms in LIP and FEF modules, and explained the excitation and inhibition relationship within each module during the rhythm activity. However, it remains unclear why each module produces the oscillation activities at such specific oscillation bands, which should be the key issue of the working mechanism from the computational aspect. I doubt that by using too strong gap junctions and highly synchronized spiking inputs (from mdPul and V4), neuron activities are too easy to be synchronized, preventing us to inspect the true underlying mechanism for the rhythm generation. With such over-synchronized activities, the oscillation band produced in the model becomes trivially relying on the oscillation of the external input.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Interacting rhythms enhance sensitivity of target detection in a fronto-parietal computational model of visual attention" for further consideration by eLife. Your revised article has been evaluated by Floris de Lange (Senior Editor), a Reviewing Editor, and one of the original reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below.

Reviewer #1 (Recommendations for the authors):

I am glad to receive this revised version of the manuscript. Its clarity has greatly improved, particularly that of the model's scope and choices. The authors addressed thoroughly my comments. I believe the current manuscript is stronger and more compelling. However, there are some remaining points listed below that I believe must be addressed.

1) Excluding biological elements that are deemed not necessary is a parsimonious and helpful approach. However, there are cases in which the manuscript is not sufficiently convincing that these elements are not necessary. For example, the different cell types form a complex microcircuit. Removing an element from this microcircuit could break down its normal functioning. The reverse of this concept is the following: the authors show that modules, where specific cell types have been removed, mimic the neural dynamics observed experimentally. However, they often do not prove that putting back this cell type, which likely exists in this area, will not generate dynamics inconsistent with the data. This question is addressed at least once by the authors in line 771:

"in our hands, placing a target-detection circuit in LIP superficial layers -like the one modeled in the FEF module-did not alter LIP rhythms or improve detection of low contrast targets."

It is great that the author did this analysis but then they should add a reference here to the related figure (it is not clear which one). Similarly, the authors should test, not necessarily in the full model, but at least in the independent modules, what would happen if they add the FS neurons to the visuomotor FEF module or the recurrent RS connections in the LIP module and the visual FEF module. I can imagine two possibilities: (i) nothing changes qualitatively, in which case the authors' approach is justified because it uses a more parsimonious model without unnecessary elements; (ii) the behavior is very different for the conditions tested, in which case the authors should comment on that.
