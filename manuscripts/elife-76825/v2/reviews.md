# Peer review - Round 1

Editors:
- Arvind Murugan, https://ror.org/024mw5h28 University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76825.sa0](https://doi.org/10.7554/eLife.76825.sa0)

This paper addresses how cells can robustly maintain direction during movement by ignoring noise in concentration gradients while also being able to adapt to new signals in those gradients. The authors study this tension in EGFR signaling by postulating a form of cellular memory in a theoretical framework based on dynamical systems and bifurcation theory. The authors also carry out experiments that raise further interesting questions. This paper will be of interest to scientists of all stripes working on cell motility and for theorists who take a dynamical systems view of biological phenomena.


---

# Peer review - Round 1

Editors:
- Arvind Murugan, https://ror.org/024mw5h28 University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76825.sa1](https://doi.org/10.7554/eLife.76825.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Cells use molecular working memory to navigate in changing chemoattractant fields" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Elizabeth R Jerison (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers broadly appreciate the theoretical framework here and the new experimental data gathered. However, a few critical changes are required before publication.

1) The most critical change suggested by the reviewers is tempering and clarifying the relationship between experimental results and theory here. The theoretical work here is already sufficiently interesting, and the experimental results add to it, but the current statements imply a consistency between theory and experiments that is not fully supported.

The authors should temper their claims and clearly delineate the ways in which the experimental results agree and disagree with the theoretical model here. (`All models are wrong, but some are useful.') Such a clear statement would allow future work to build on the results here.

2) The authors should discuss other predictions of their model for future experiments (e.g., see reviewer #2's and #3's comments).

3) Simplify/reduce technical jargon – e.g., see reviewer #1's comments.

Reviewer #1 (Recommendations for the authors):

Appraisal of results supporting Figure #1 and theoretical background:

The theoretical background is sound and detailed. However, much of it rests on the choice of parameters as identified by the authors. It would be beneficial to see the dependence of the existence of saddle-node pitchfork bifurcations (and similarly the stable polarisation state, and homogeneous symmetric steady states) on key parameters (especially the total EGFR on the plasma membrane, and the total amount of the membrane-localized PTPRG and the ER-bound PTPN2).

Also, the authors claim that in their model, "The cell polarity is sustained even when the EGF signal is briefly disrupted, but also, the cell is able to rapidly reverse the direction of polarization when the signal direction is inverted". It would be helpful if the authors indicated (either by a numerical plot, or analytical calculations if possible) the time scales of such responses in their model. Chiefly, it would help to know how long the signal would need to be disrupted before the polarity is no longer sustained, how long the signal direction needs to be inverted before the cell reverses polarity, and how long it takes for the cell to either reverse or lose polarity.

Appraisal of results supporting conclusion #1:

The authors claim that MCF7 cells maintain a memory of the direction of previously encountered signals through prolonged EGFR phosphorylation polarisation and temporal evolution of the cell protrusion that emerges from a saddle-node pitchfork bifurcation which maintains the system away from the steady states. The key pieces of evidence present claim that after subjecting the cells to a stable gradient of EGF for one hour, the cells remain polarised for ~40 minutes. While the experimental evidence shows that the cells are partially polarised for ~40 minutes after gradient washout, the polarisation is less than it is in the presence of the signal and steadily approaches the unpolarised state (this is most clearly seen in the single-cell trajectories supplied in Supp. Figure 2-1F). This is unlike the distinct persistence of polarisation shown in the numerical results (Figure 1F and G). To me, the experimental data suggest that the timescale of relaxation from the polarized state to the unpolarized state due to slow dephosphorylation kinetics is ~40 minutes. The authors should describe what the characteristic chemical timescales of the system are, and if persistence of ~40 minutes is uncharacteristically large. How do the experimental results reflect the existence of a metastable "ghost" state as in saddle-node bifurcations, rather than two steady states that take ~40 minutes to move between them as in a subcritical pitchfork bifurcation without a saddle-node? The authors attempt to answer this by using Lapatinib later on (which should be brought into this section), but the difference due to Lapatinib isn't established as data is shown only for one cell, and further, the unintended effects of Lapatinib on the cells hasn't been shown (a possible way to demonstrate this would be a control experiment with cells treated with Lapatinib for a short amount of time and then exposed to a gradient of EGF to show that there is a memory in such a case).

Appraisal of results supporting conclusion #2:

The authors claim that the transient memory encoded in the EGFR phosphorylation polarisation and cell protrusion translates to memory in directional migration up a linear EGF gradient that persisted after the gradient washout. The authors demonstrate that there is a transient memory in directional migration after subjecting the cells to 5 hours of a linear gradient (however, they do not initially identify the period of this memory in Figure 3A and 3B. They later suggest that it is 50 minutes after gradient washout); however, it is difficult to see if the memory encoded in the EGFR phosphorylation polarisation and cell protrusion is accurately reflected in the memory in directional migration due to the vast differences in the timescales of the experimental evidence for the two (the former is in a constant exposure for 1 hour, while the latter is for a constantly decreasing exposure for 5 hours). Further, the evidence using Lapatinib is not conclusive, as even if we believe that there is a difference between the directionality with and without Lapatinib (Figure 3J), this does not establish the link between transient molecular states and transient directionality. The evidence in Figure 3G is inconclusive as it is not sufficiently different from the case without Lapatinib and Takens's delay-embedding trajectory is based on just one cell.

A key piece whose repercussions were not discussed much by the authors is that the gradient steepness was progressively decreased. The authors treated the entire period before the gradient washout as being the same, and I am still unclear as to what the effect of decreasing the gradient was.

Appraisal of results supporting conclusion #3:

The authors claim that MCF10A cells can sense dynamic gradients while maintaining robust directional migration even when the signal was disrupted. This is seen very clearly in silico in Figure 4B, but the experimental results in Figure 4C clearly differ in that the cells do not seem to have any significant memory following the gradient washout. Further, the ability of the cells to respond to changes in the environment should be contrasted to the case of slow dephosphorylation kinetics to highlight the role of the transient memory state. In general, it would be helpful to understand what the effect of a shorter time scale of the transition from a polarised to unpolarised state would be on the robustness of the system, and what the effect of a longer time scale would be on the adaptation of the system.

Note regarding the Discussion:

The authors do not distinguish their contributions from those made by other research groups that are addressing similar questions. For example, in line 310, the authors cited a set of papers as relevant experimentally but dismissed them as not providing a mechanism even though some of them did. For instance, Skoge et al. (PNAS, 2014), discussed a possible mechanism by which cells exhibit memory and maintain directed motion in the classical back-of-the-wave problem for Dictyostelium, and Prentice-Mott et al. did so for chemotactic neutrophil-like cells. Similarly, in lines 28-30 and lines 148-149 they cite a host of different papers that also model directional sensing in eukaryotic chemotaxis that they dismiss but should address. They state that these models cannot capture memory in polarization along with continuous adaptation or require fine-tuning. But it is not apparent that this is the case. The work by the authors is sufficiently different from many of these other papers and their contribution is significant that it merits dissemination (even if as a different framework for the same problem). But they should acknowledge clearly what their specific contribution is, or how it performs better than other models. If possible, they should cite experimental evidence that distinguishes their predictions from those of other models.

Detailed notes regarding figures and text:

The figures and the captions are very unclear, and the text can be bigger. The captions do not properly explain what is happening (please use complete sentences for captions). A few (but not exhaustive) notes:

Figure 1: Please label the color notation for the bars indicating the direction of the gradient (red, green, and orange) or indicate it somewhere in the caption. A plot similar to Figure 2B would be very helpful.

Figure 1A: This figure is highly confusing without the text. As such it served no purpose for me, and even after reading the text and understanding what it was trying to say, I didn’t understand the figure itself. The caption labels are inconsistent with the coloring in the plot, and there’s a notion of time that was not conveyed in the figure. It might serve the reader to split this into two figures and make the figure captions more explanatory.

1B: Not all the different elements are not explained in the caption (basically everything inside the cell is unlabelled).

1C: The circuit is too small to see.

Supp Figure 1-1: Please label the figures in the correct order (the panels labeled E should alphabetically appear after F and G). Also, it might be beneficial to keep the same scale for Ep (or switch to Ep/Et while identifying Et in the figure itself).

It was difficult to find the parameters used for the IHSS. I would recommend a table of parameters with columns for the different sets of simulations performed, with descriptions of each of the parameters/variables.

1-1B The current description gives the impression that Et is titratable (but as I understand it, the total protein concentration was conserved in the mass-action kinetics) especially as it is placed along with Ep which does change in the simulations. Please elaborate on the description in the figure caption and distinguish Ep and Et as a variable and parameter respectively.

Figure 2A: Please indicate a color bar for EGF just as was provided for EGFRp.

2C: During what time was the spatial projection generated?

D, E, H: Please spell out that n and N refer to the sample size and the number of replicates for the general readership.

2F: The figure is barely legible. Please magnify, and consider normalizing E-Ep.

2G: What are the units for the area? Is it a fraction of the total area?

2H: What does the horizontal line at the solidity of 0.65 represent? Also, how is the "end of memory" determined?

Figure 3A: Please identify the memory phase and label it in blue.

Figure 4D Please add a horizontal line for cos\theta = 0.

4E This figure was very difficult to read. Please consider breaking it into multiple 2D plots as one of the dimensions in the plot currently serves no purpose

Note for Section 1:

This section is fairly heavy on jargon and technical language. While I appreciate the transparency, it might benefit the general reader to reduce the number of terms used. For example, stable inhomogeneous state regime, stable polarization, and inhomogenous steady-state are used interchangeably in the text and the figures. Sticking to a small set of terminology would be beneficial to the reader.

Notes for Section 2:

I would define solidity early on (as of now, the first definition appears in line 557, but solidity appears as a quantity as early as Figure 2). In line 168, I would clarify if it is the polarisation that is shallow or the gradient of EGF. Also, a key piece of evidence that is currently buried is the timescale of gradient washout. It would serve the reader to highlight it in the text.

Please also clarify the relevance of the Takens delay-embedding trajectory. Currently, I found it misleading since it merely states that is a period of transition between two distinguishable states: the polarised state and the unpolarised state, which is already captured in the time plot of the EGFR dynamics.

Notes for Section 3:

It is currently stated that "directed migration persisted for a transient period of time after the gradient wash-out". This doesn't seem to be quantified, and what constitutes a "transient" period is unclear. Thus, the statement ,"The directionality estimated in the 9h time-frame after the gradient removal was greater than the one in continuous stimulus absence" seems to contradict the statement that "After the memory phase, the cells transitioned to a migration pattern equivalent to that in the absence of a stimulus" as the duration of the transient period of transition is unspecified. Also, this statement is not adequately reflected in the statistics of the directionality (Figure 3B).

Notes for Section 4:

This section was well-written, with the exception of describing what the KDE distributions reveal. This is a key piece of statistical evidence that must be more clearly shown and its relevance discussed.

Reviewer #2 (Recommendations for the authors):

– In general, the experiments conducted support the key features of the dynamical model. It would strengthen the authors' conclusions if the effects of perturbations (e.g., by Lapatinib) could be clarified in the main text within the context of the model. For instance, is only the memory lost, or is the cell's ability to polarize in the presence of a gradient also disrupted?

– It would be helpful if one did not have to refer to the caption to read several of the figure panels. (An example: the color-coding in 3A, D).

Reviewer #3 (Recommendations for the authors):

Timescale of memory

In my understanding, the lifetime of a 'ghost' state near a saddle-node bifurcation goes as 1/r^(1/2), where r is the distance to the critical point. This suggests that the timescale associated with the memory state is sensitive to how close the system is to the critical point, and, at least formally, diverges as the system actually approaches this point. This would seem to present a fine-tuning problem: not only does the system need to have parameters tuned to be near criticality, but in fact they have to be exactly the right distance away to achieve a physiologically reasonable intermediate memory timescale. It would be useful for the authors to discuss this: how is the memory timescale controlled? How sensitive is it to parameter changes? Is this somehow a feature, in that the cell can potentially physiologically change its memory timescale?

Suggestions regarding the theoretical exposition:

1. The authors should clarify the dimensional reduction that led to the bifurcation diagrams in Figure 1A and Figure 1—figure supplement 1B. Absent additional justification of this reduction, it would also be clearer to describe this as an approximate treatment of the system (whose behavior is born out by the reaction-diffusion simulations), rather than a proof (line 100).

2. It would be useful to readers to include a more concrete discussion of the EGFR model in the main text, including which features of it drive the behavior of the system and which biochemical parameters control location in the phase space. Additionally, how does the magnitude of the external gradient affect the cell? As a suggestion, the authors could consider moving Methods 5.15, Equation 17, to the main text, with a description of what the important variables are, and what features are important to the presence of the pitchfork bifurcation.

Suggestions regarding the presentation of the measurements:

1. Related to the public review, the authors could strengthen the paper by explicitly discussing the discrepancies between the measurements and the expectations from the model, and potential explanations. Does experimental noise interfere with the EGFR phosphorylation profile measurements? Do the authors believe that some of the cells are not at criticality?

2. The fact that the model depends on cells being biochemically poised near a critical point suggests a variety of stronger experimental tests of the framework. As one example, the authors' analysis suggests that overexpressing EGFR should push the cells away from the critical point, into the inhomogeneous steady-state regime, where they would break symmetry according to the first-encountered gradient and no longer be capable of adapting to a new gradient. This would be quite surprising, as it would correspond to breaking a sensing system by increasing the number of sensors. While performing this experiment is likely beyond the scope of this paper, the authors could strengthen the presentation by discussing this and/or other more counterintuitive predictions of their model in light of existing empirical data and/or future experiments.

3. Figure 2—figure supplement 1C: given that the direction of the polarization relative to the gradient is important, it would be interesting to see all the polarization profiles (and the variability from cell to cell with respect to the direction relative to the gradient).
