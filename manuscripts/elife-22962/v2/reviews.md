# Peer review - Round 1

Editors:
- John Huguenard, Stanford University School of Medicine , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.22962.021](https://doi.org/10.7554/eLife.22962.021)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Computational models of O-LM cells are recruited by low or high theta inputs depending on h-channel distributions" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Eve Marder as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Ivan Soltesz (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Overall, this is an important and carefully performed study, which examines the role of H-currents in rhythmic firing of virtual OLM interneurons during imposed synaptic activity patterns designed to simulate in vivo activity. The study leverages multicompartmental OLM cell models developed from reconstructed neurons with distinct somatic and dendritic compartments. The strength of the approach is in using models in which different combinations of channel distributions were all selected to fit the OLM firing properties, as is likely to occur in biology. Using this powerful approach the authors show that, in contrast to a previous study that modeled an in-vivo like synaptic conductance state with exclusively somatic synaptic inputs and somatic h-conductance, explicit modeling of dendritic compartments that receive excitatory and inhibitory synaptic inputs and express h-channels enabled O-LM interneurons in CA1 to synchronize their spike frequency to the modulation frequency of a population of inhibitory synaptic inputs.

Essential revisions:

1) The role of H-currents and (M-type) potassium channels has been explored in detail in previous work in pyramidal cells (Narayanan and Johnston, J. Neurosci 2008) and the current study expands the work to OLM cells and in the context of in vivo-like synaptic inputs. Thus, the role of H-currents in regulating theta frequency firing is not entirely novel and the above study needs to be cited. Also, as detailed in Narayanan and Johnston, H-channel kinetics would be expected to contribute to resonance in the theta range.

2) In Figure 2, the more appropriate test for the -H condition would be to replace H with a leak conductance rather than adjusting the synaptic conductance levels. Especially since this was done on a per model basis and only to excitatory synapses, each model would receive a very different input. The authors need to consider replacing H with leak conductances and/or by bias currents rather than modifying synaptic conductances. How -H condition impacts membrane time constants also needs to be considered as this can impact intrinsic resonance of the model neuron. The same issue concerns the analysis of Kdr and KA effects as well, as again the membrane conductance is altered by channel closure and instead of changing leak conductance the authors re-tune synaptic conductance.

3) Comparison of models with somatic versus dendritic H-channel distributions in table 2 shows a systematically higher membrane resistance and capacitance in models with somato-dendritic H-channels. This would be expected to change membrane time constants and could contribute to differences in the frequency preference among the 2 model classes. Controls are needed to exclude this possibility and confirm that H channel distribution underlies the differences between the models.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Computational models of O-LM cells are recruited by low or high theta frequency inputs depending on h-channel distributions" for further consideration at eLife. Your revised article has been favorably evaluated by Eve Marder (Senior Editor), a Reviewing Editor and two reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

Please include the response figure as a supplemental figure, as it is an important control.

Reviewer #1:

The authors has addressed essential revision 1 in the manuscript. They have provided convincing explanations and additional simulations to address essential revisions 2 and 3 in the response letter but choose not to include the control simulations in the manuscript. I would recommend including a statement in the text related to Figure 2 that "control simulations in which an "artificial leak conductance" was introduced to maintain baseline firing without manipulating synaptic conductance yielded similar results" and all further simulation s were performed by scaling the excitatory synaptic conductance. They could refer reader to the response letter or add the Figure Author response image 1 as a Supplement to Figure 2. In its current state, the issue of conductance raised by both reviewers is not addressed in the main manuscript.

Reviewer #2:

The authors addressed my points. I do not have any additional concerns.
