# Peer review - Round 1

Editors:
- Ronald L Calabrese, Emory University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.06229.016](https://doi.org/10.7554/eLife.06229.016)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Identification of computations underlying photo-taxis, odor-taxis, and multi-sensory integration” for consideration at eLife. Your article has been favorably evaluated by Eve Marder (Senior editor) and three reviewers, one of whom, Ronald L Calabrese, is a member of our Board of Reviewing Editors.

The Reviewing editor and the other reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

The authors present a very intriguing and thorough behavioral analysis of the navigation of Drosophila larvae to visual and chemical stimuli, separately and combined. For this analysis they use light and optogenetically induced fictive olfactory stimuli whose derivatives were independent identically distributed Gaussian random variables: a Brownian random walk. In an automated system, they monitor large numbers of larvae to a variety of stimuli and a stimulus combination and apply a Linear-Nonlinear-Poisson (LNP) model. Their Results are consistent with a model where visual and chemical inputs are combined early rather than processed in parallel to effect orienting turns. Their Discussion suggests that the methods used can be generally applied in understanding how neuronal networks effect decisions. The writing is very clear and crisp and the figures well designed. The modeling is well conceived and based on established procedures and it appears competently and prudently applied. The Materials and methods section and the Figure legends are very clear and helpful. These results have important implications for behavioral analysis of decision making in animals and serve as an entry point for further mechanistic studies in the important model system. Moreover, the application of the techniques here can be a model for applications in other systems.

There are some concerns which the reviewers share that should be addressed:

1) To be sure that the blue light is not evoking responses in Chrimson expressing ORNs the authors should perform a control experiment in genetically blind larvae with a NorpA mutation while expressing Chrimson in Or42b neurons and presenting blue light. The need for this control is expressed well by one of the expert reviews:

“My biggest concern is that I am not entirely convinced that there is no cross talk between the visual stimuli and the fictive odors. This is because the channelrhodopsin Chrimson is still highly sensitive to blue light despite being red-shifted in its optimal excitation wavelength. Klapoetke et al. 2014 show that blue light is very effective at eliciting spikes in larval neurons even for very brief and dim light levels (Figure 3A). I disagree that simply because the red light is 300 times greater intensity than the blue light, that any blue light response would be 0.3% of the red light responses. This will depend on the light intensities at which the Chrimson saturates. The percentage could be much higher than reported. Additionally, dim blue light was used in the Chrimson experiments to mask out visual responses to the red light. They reference Klapoetke et al. 2014 for this approach. The problem is that Klapoetke et al. 2014 were using adult flies, in which blue light is known not to penetrate the cuticle. Thus blue light likely never reached the Chrimson molecules in their central neurons and thus blue-light masking is appropriate. This manuscript uses this approach in peripheral neurons in a transparent larva. Thus, this blue light is more likely to activate Chrimson.

The authors would ideally use physiology to demonstrate clear separation of their visual and fictive stimuli. At minimum a behavioral approach should be attempted. Could the authors not genetically blind larvae with a NorpA mutation while expressing Chrimson in Or42b neurons and presenting blue light? If the blue light still evokes turning, then there is cause for concern.”

2) The Discussion does not do justice to the Results, probably a holdover from this being originally conceived as a short communication. One of the expert reviewers has some good suggestions for amplifying the Discussion:

“The Discussion was too short and failed to put these new results in a broader perspective. What do these results reveal if anything about the strategy used by larvae to avoid blue light and go towards sources of attractive odorants? I.e., what does it mean about what happens when larvae are navigating “natural” environments where odorant and light have spatial structures with characteristic lengths, rather than being subjected to signals with Gaussian white noise derivative? How do these results fit in with previous studies? I wished the authors had discussed further the interesting differences they identify between decisions in response to ‘CO2 signals’ and those to ‘ethyl acetate’ and light. They mention the role of speed change in response to CO2 but do not discuss whether there is speed modulation in response to the other two signals.”

3) There is a more minor concern that the Chrimson responses might show adaptation over the course of the experiments. In the absence of a direct electrophysiological demonstration, is there any evidence the authors can provide that the adaptation is not a factor in for example the poor fit of the LNP model for the first 10s of the step response in Figure 2C?
