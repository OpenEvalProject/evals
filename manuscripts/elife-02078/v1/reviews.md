# Peer review - Round 1

Editors:
- Ronald L Calabrese, Emory University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.02078.013](https://doi.org/10.7554/eLife.02078.013)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Cell-intrinsic mechanisms of temperature compensation in a sensory receptor neuron” for consideration at eLife. Your article has been favorably evaluated by a Senior editor and 3 reviewers, one of whom, Ronald L Calabrese, is a member of our Board of Reviewing Editors.

The Reviewing editor and the other reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

The authors describe experiments showing temperature insensitivity in locust auditory receptor neurons (Q10< 1.5) and then pursue a modeling approach to explain these results. They concentrate on the spiking mechanisms itself and use an ensemble modeling approach to identify model neurons that will show comparable temperature insensitivity while expressing membrane currents with normal Q10s. These modeling experiments identify key processes (parameters) that give rise to the temperature 'compensation' and show that well-compensated models show a shift in threshold that partially cancels the shift in F-I slope that all models show. They also address the issues of information transfer and metabolic cost as temperature increases and find no restrictions for compensated models. They then use a reverse engineering method to address temperature compensation in the transduction mechanisms (receptor potential). The finding are of general interest because many neurons, including peripheral mammalian neurons, experience temperature changes and these studies show that such changes are easily accommodated/compensated by systems of membrane currents with normal Q10s.

The three reviewers are from different backgrounds and have different overlapping expertise; their reviews reflect their different backgrounds and expertise, but they all agree that four major revisions are needed.

1) While conciseness is a virtue it should not sacrifice clarity and completeness. We encourage the authors to expand their style in Introduction, Results, and even Methods to add more rationale and fuller explanations of what they did and how the models were constructed and used. In particular the section “Model-based inference of the auditory transduction function” was very difficult to follow. We suggest that the authors expand this section and fully explain what they did, how they did it, and why they did it.

2) Like prior studies by Laughlin and others on the metabolic cost of neuronal signaling, the authors use Na flux as a proxy for ion pump activity and as their measure of metabolic cost during spiking and at rest. The authors should provide clear rationale for why the cost of other ions were excluded. This seems particularly relevant in light of the authors' finding that the properties of Na channels, more than those of other channels, influence energy efficiency in these model neurons. The model used only includes Na and K currents and so other ions cannot be considered and the cost of K is tied to the cost of Na by the Na/K pump but this and the inherent limitations it imposes on the conclusion should be made explicit.

3) One reviewer crystallized concerns about the experimental component of the work: “My concerns are with the acquisition of the biological data, particularly with respect to temperature control and measurement…” The authors should make their experimental procedures crystal clear (in both Results and in Methods) and should address each of the questions posed by this reviewer. They should also make arguments about how much error there would have to be to affect their conclusion.

4) The authors should apply appropriate statistical tests to the biological data in all cases where temperature appears to affect a characteristic, e.g., spike width, so that the reader is confident that the temperature change is large enough to measure valid Q10s.

Other issues to address:

Reviewer #1:

The section “Model-based inference of the auditory transduction function” was very difficult to follow. This reviewer is a computational neuroscientist but I am unfamiliar with reverse engineering techniques, and I was not given enough help in reasoning through the experiments and data as would be necessary for the general reader in neuroscience. I suggest that the authors expand this section and fully explain what they did, how they did it, and why they did it. The Methods section helps a bit but only very marginally and is very technically written. Think of the general reader here.

Reviewer #2:

Like prior studies by Laughlin and others on the metabolic cost of neuronal signaling, the authors use Na flux as a proxy for ion pump activity and as their measure of metabolic cost during spiking and at rest. I have always been puzzled by this choice – why exclude the cost of other ions? I assume there are good reasons for this choice that I am simply not aware of, so I suggest that the authors include a comment on this question. This seems particularly relevant in light of the authors' finding that the properties of Na channels, more than those of other channels, influence energy efficiency in these model neurons. This result makes me wonder if the outcome would have been different (with other ion channels playing a bigger role in energy efficiency) if metabolic cost had been defined in a less Na-centric way.

Another comment concerns the tests for robustness of their findings to the particular choice of model neuron that the authors describe in the paper. In the Results section we learn that the authors tested for robustness of their results by checking whether a relatively modest (20%) variation of parameters of the Connors-Stevens model used here changes the overall conclusions, and are assured that it does not. While this test for robustness is laudable, I was much more convinced that the findings are robust by a very short comment, hidden in the Methods section, in which the authors state that they also found temperature compensation of firing properties despite temperature dependence of ion channels in a structurally different Traub-Miles model neuron. I recommend that the authors consider giving this latter result a more prominent place in the paper, because it could potentially (since I don't know the details) make the case for generality of the results much stronger.

Reviewer #3:

The work is novel, interesting and well presented. Though the linkage between the biological neurons and the models is quite tenuous, I have no problems with the computational aspects of the paper. My concerns are with the acquisition of the biological data, particularly with respect to temperature control and measurement. This is important because if the temperature change at the receptor ending is over-estimated then the Q10s will be under-estimated and there may not be an interesting biological phenomenon (the surprisingly low Q10) in need of explanation. The preparation was heated by placing it on a Peltier element i.e. a localized heat source underneath the locust. Heat conduction from that source will vary through the various tissues, cuticle and saline and I would expect that the preparation was not at a uniform temperature throughout. The GTF 300 thermal probe has, according to the manufacturer's website, a diameter of 1mm (assuming that it hadn't been modified) which is relatively large with respect to distances inside the thoracic/abdominal cavity. I wonder if the authors could provide more information in the Methods that might increase confidence that the temperature range reported and used to calculate Q10 was the range that the receptor ending actually experienced. For example, how was the temperature at the attachment site of the receptor neurons measured using the GTF 300 probe? How variable was the temperature at different sites in the preparation (tympanum, saline, ganglion)? What did the calibration curve look like and was a calibration curve generated for every preparation that provided data or from other preparations; how consistent was it between preparations?

Action potential width was measured at the recording site in the metathoracic ganglion but it is being associated with firing frequency generated at the tympanum. Did these two sites experience the same temperature changes? Given that the density and diversity of conductances can be quite different at different locations of a neuron, do we know whether action potential parameters at these two sites are the same?

The sample size of 9 neurons in 8 preparations is relatively small. I assume that each preparation provided at least one neuronal recording and one provided two, but this is not explicitly stated. According to Figure 1C, one or more of the neurons had a Q10 for spike rate at half max greater than 2.5 suggesting that these measures were quite variable. Did the authors perform any statistical comparisons to test significance?

It is unsurprising to me that metabolic cost was defined as Na load and then the computational analysis revealed that parameters of the Na conductance had the greatest effect on Q10 of metabolic cost. The authors might comment on this.
