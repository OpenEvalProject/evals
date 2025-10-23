# Peer review - Round 1

Reviewers:
- Alexander Borst, Max Planck Institute of Neurobiology , Germany

## Review text

DOI: [10.7554/eLife.22431.014](https://doi.org/10.7554/eLife.22431.014)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Sensitivity to image recurrence across eye-movement-like image transitions through local serial inhibition in the retina" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom, Alexander Borst (Reviewer #1), is a member of our Board of Reviewing Editors, and the evaluation has been overseen by David Van Essen as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Kevin L Briggman (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

In this manuscript, Krishnamoorthy and colleagues examine RGC responses to eye-movement like visual stimuli in the mouse retina. They find that 5-10% of RGCs are "image-recurrence sensitive," meaning that their spiking is generally suppressed after a transition from one spatial pattern to the next, unless the same pattern reappears. IRS cells correspond to transient Off α RGCs. Through a series of clever manipulations of a shifting grating stimulus, pharmacology, intracellular recordings and computational modeling, they convincingly show that the IRS response is mediated by a serial inhibition circuit in the inner retina. The authors argue that this type of feature sensitivity may be useful in guiding micro saccades to correct for fixational drift. The mechanistic explanation of this unexpected IRS response is very solid, and it stands as an unusually convincing example of attributing some feature of retinal computation to a serial inhibition circuit. This is achieved mostly through the authors' clever stimulus design and willingness / ability to use whole cell recordings from identified OFF α cells. The effort to firmly identify these IRS cells as the transient OFF α RGCs is very nice.

Major points to address in revision:

1) Function of IRS cells for natural eye movements in mice: do mice show saccadic eye movements, with saccadic intrusions, that would help to stabilize and fixate the image, as the authors speculate in the discussion? The references given in this context by the authors appear to mainly address humans. What about saccades along contours, as in the Discussion? Relatedly, the IRS responses seen using natural images are much less consistent than those elicited by gratings stimuli. From a population perspective this suggests that for a given transition, some subset of cells will show IRS-like responses and others will not. Some discussion of encoding by this heterogeneous population would be useful to include.

2) IRS brain target region: Given the fact that the ganglion cell type is identified, the authors could discuss to which target region in the mouse brain this ganglion cell is sending its axon to.

3) Sources of response variability: From the data it is difficult to get a sense of the sources of variability in the responses. The proposed mechanism behind IRS seems to depend on the appropriate amount of negative contrast within the RF. Similarly, if the variable transition response (e.g Figure 1C) is an offset response, then it would rely on there being sufficient positive contrast in the starting position. Can you explain any of the variability in these responses based on the portion of the grating that is within each cell's RF? This sort of analysis would be especially useful in the context of the natural image experiments (Figure 4C), which show much less robust IRS responses. Can you use the computational model to predict which natural images will or will not show an IRS response?

4) Illustrating the model: The computational model is a bit hard to follow and ultimately is not used as much as it could have been. It would help the reader to understand the underlying mechanism to show the responses of various model components during some of these stimuli (Figure 8). For example, you could highlight two regions of the stimulus in Figure 8A, one that changes and one that doesn't, and illustrate the responses of some of the key model components during and after the transition. Adding a panel between 8B and 8C showing the time series responses of each of the cell types in the model in responses to different transition types would I think make it far easier to grasp. Also, adding a cartoon of the actual anatomy to complement 8A would be a nice addition.

5) Model parameter sensitivity: Some statement about parameter sensitivity in the model would be appreciated. Also a concise statement of the total number of free parameters in the model would help.

6) Evidence for AII: The evidence that the slow ON amacrine cell in this circuit is the AII amacrine is largely circumstantial and based on past work under different conditions. I would suggest softening the focus on this specific amacrine cell and instead highlight the proposed general circuit organization.
