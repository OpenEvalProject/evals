# Peer review - Round 1

Editors:
- Frances K Skinner, Krembil Research Institute, University Health Network Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.29384.024](https://doi.org/10.7554/eLife.29384.024)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Revealing the Distribution of Transmembrane Currents along the Dendritic Tree of a Neuron from Extracellular Recordings" for consideration by eLife. Your article has been favorably evaluated by Richard Aldrich (Senior Editor) and three reviewers, one of whom, Frances Skinner, is a member of our Board of Reviewing Editors. The following individuals involved in review of your submission have agreed to reveal their identity: Alexandra Chatzikalymniou (Reviewer #1), Joshua Goldwyn (Reviewer #2); Michiel Remme (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

This paper introduces a novel method to estimate current sources underlying extracellular recorded voltages. The method relies on a combination of kernel CSD analysis of the extracellular potential recordings and knowledge of the morphology of a neuron close to the recording electrodes. Assuming one is able to isolate the contribution of this one cell to the extracellular potentials, this method can map the current sources onto this cell. The method was validated against arbitrary morphologies and electrode configurations simulating biologically relevant scenarios from simple (ball and stick and Y shape neuron) to more complicated (ganglion cell model). It is thought that this method has great potential and should be interesting to many neurophysiologists as it allows for significantly improved reconstructions of the current source density distribution along a cell morphology.

However, the reviewers noted various aspects that need to be addressed.

Essential revisions:

1) The code needs to be included and not just upon request.

Please see the information on eLife website regarding Tools and Resources papers: https://submit.elifesciences.org/html/eLife_author_instructions.html#types

"…relevant code must conform to the Open Source Definition and be deposited in an appropriate public repository; and methodological advances need to be comprehensibly described…"

2) The authors need to edit their paper in the following ways:

a) Overall editing of the paper is needed.

There are numerous spelling errors and especially the articles before many nouns are missing. Much more proofreading of the text is recommended as part of the overall revisions.

b) Bring forth the significance/importance/need for their work earlier. For example, the last section of the Discussion ('importance of this work') could be moved to the beginning of the paper.

c) Edit and expand writing to be more accessible, to be more understandable to the general reader, and to avoid confusion in what is meant.

Specifically: i) Since this paper introduces a new methodology, and most readers will not have a e.g. machine learning background, I believe the paper needs to improve the explanation of the methodology, and not just in the Materials and methods, but throughout the paper. Clearly the authors have already attempted to make it readable to non-experts, but I would specifically recommend the following:

- At the beginning of the results, a summary of the method should be included. That is, present the method in a "self-contained" way so that the reader does not need to 'walk through' several methods (kCSD, sCSD, skCSD) and remarks on the innovations in each "iteration" as given in the Materials and methods at end of the paper.

- It should be possible to read the paper from beginning to end without running into terms that have not been defined yet (e.g. subsection “Dependence of reconstruction on noise level”: 'regularization'; subsection “Dependence of reconstruction on the number and arrangement of Recording Electrodes”, third paragraph: 'the width of the basis functions'; 'the cross-validation error').

- In the Materials and methods: some intuition for the kernel method should be given (and not by referring to another paper). Why would one 'avoid direct estimation of coefficients a_j'?. What is gained with the kernel trick? One will have to estimate fewer parameters, but how does that come about? Does this rely on specific assumptions?

ii) Is it meaningful to make comparisons to interpolated voltage method or kCSD method? These methods are not, to my knowledge, designed or expected to have resolution at the single cell (or subcellular level) – well, I suppose the resolution is determined by the electrode grid, but in any case it is not clear to me that readers would assume that these methods "should" be able to resolve branch points or other information local to a dendritic tree. Edit/expand the manuscript to make clear what is meant.

iii) “Proof of concept experiment”. I am confused by this section. The authors go into detail describing the spatial and dynamical features of the inferred transmembrane currents. But then they seem to nullify their observations and the usefulness of their method when they write "From an experimental setup consisting of only 14 electrodes on a linear probe a detailed distribution of current sources along a complex morphology cannot be expected". Then, they write "but the firing activity is well observable" – but this point is not novel or contested. Indeed, spike identification from multi-electrode recordings is a common data analysis task, and not the (apparent) point of the method presented here.

See also paragraph in Discussion beginning: "The skCSD method performed adequately for the proof of concept experimental data". I don't feel this is justified, without further clarification of the message in the subsection “Proof of Concept experiment: Spatial Current Source Distribution of Spike-triggered Averages”. Edit/expand the manuscript to make clear what is meant.

iv)“To test the effect of branching on the results, a simple Y-shaped morphology was used (Figure 11B). […] The first was stimulated at 5, 45, 60 ms, the other at 5, 25, 60 ms after the onset of the simulation.” Why choose these arbitrary stimulation times? Why are the synapses activated in this specific temporal sequence? It would be interesting to know what the temporal resolution of the technique is. Also, how would the performance of the technique change for different degrees of correlation of synaptic inputs? Edit/expand the manuscript to address reasoning/rationale of these questions.

v)“As a realistic example, we used a mouse retinal ganglion cell morphology Kong et al. (2005) from NeuroMorpho.Org Ascoli (2006). […] The cell was also driven with an oscillatory current. In the dendrites, only passive ion channels were used.” What is the frequency of the oscillatory input and its effect? They do say approximately 6.5Hz (line 175), but it would to helpful to know about different frequencies (say higher γ frequencies) and/or discuss it. How does the separation sensitivity of current sources depend on the frequency of the oscillatory input used? The validity of the technique should be tested for different oscillatory frequencies so that potential users keep in mind how the performance of current sources separation may vary as a function of input frequency. Is the separation of synaptic inputs equally successful for lower and higher synaptic input frequencies? As users will likely need to reveal current sources of different oscillatory input frequencies this information would be important to present. Edit/expand the manuscript to do and/or discuss these aspects.

vi) The Introduction (third paragraph) suggested to me that the current injection to the cell is exploited in this new method. However, this idea does not seem to be very central throughout the paper. Perhaps this could be stated more clearly.

3) Estimating parameters in real experiments.

The authors suggest using a modeling approach to generate data and optimize the parameters and then use these parameters for the actual data.

- First of all, from the Figure 8 results it seems the CV error is pretty good (though what is the CV error for case H?). Why not just use that? It would be informative if the authors illustrate how different the CSD estimates are when using the CV error instead of the L1 error in Figure 9.

- My main concern with using the modeling approach (L1 error) is that the active properties of the neuron are not known sufficiently well. But I would expect that the presence of active currents (e.g. sodium, calcium, NMDA spikes, but also subthreshold active currents) would have a significant impact on the parameter estimates (R, λ etc.), compared to the parameters for a passive model (see suggestion in the subsection “Experimental Recommendations”). The authors should explore this, i.e. show how parameter estimates vary when considering a passive versus some variations of active models. There are various detailed hippocampal pyramidal cell models in modelDB from which the authors could use the active properties for their cell reconstruction and compare the obtained skCSD parameters with those obtained from a passive model.

- In general, the effects of the parameters λ, R and M are not properly discussed. How strongly do they affect the CSD estimates?
