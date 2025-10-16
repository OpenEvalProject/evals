# Peer review - Round 1

Editors:
- Sandeep Krishna, National Centre for Biological Sciences‐Tata Institute of Fundamental Research India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64348.sa1](https://doi.org/10.7554/eLife.64348.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper applies a combination of experimental and theoretical approaches to study the circadian clock of Anabaena, a cyanobacterium which exists as multicellular filaments. The system offers a rare natural example of a one dimensional system of coupled oscillators which have been the subject of much theoretical investigation. The authors demonstrate an interesting role of rpaA as a regulator of the clock and cell-cell communication to synchronize oscillations across cells in the same filament. They also show that inherent demographic noise can expand the parameter range over which oscillations with circadian periods occur, possibly enhancing the robustness of the clock.

Decision letter after peer review:

Thank you for submitting your article "Robust, coherent and synchronized circadian clock-controlled oscillations along Anabaena filaments" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Mogens H Jensen (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

All three reviewers found the Anabaena system interesting and the analysis of a circadian clock that depends on cell-cell communication to be of general interest. However, they had a series of concerns about the claims made in the paper.

Essential revisions:

1. On the experimental front, please pay particular attention to address points 1a-d raised by Reviewer 1.

2. On the theoretical front, please give a clearer explanation of Figures 5 and 6 (see comments by Reviewers 2 and 3) and provide analyses to show that the claims about the model are robust to parameter choices (points 1 and 2 of Reviewer 3).

Please go through all three reviews appended below and try to address all the comments in a revised manuscript.

We would like to draw your attention to changes in our policy on revisions we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Reviewer #1:

Arbel-Goren et al., apply a combination of experimental and theoretical approaches to study the circadian clock of Anabaena sp. Unlike Synechococcus which is unicellular, Anabaena exists as multicellular filaments. The authors follow the expression dynamics of gfp expressed from a clock-controlled promoter (PpecB) and show that expression follows an oscillatory pattern. They find that cells within the same filament (up to 10 cells apart) are synchronous, but cells across unrelated filaments are not. Synchrony is inherited upon division. The oscillatory patten is not consistent with the expression pattern of kai genes. Instead, the authors show that expression is in phase with rpaA expression, but dependent on Kai. To strengthen the idea that cell-cell communication is essential for the oscillations, the authors delete septal proteins, which breaks the pattern observed. Theoretical model of coupled clocks fits the experimental observations. The authors conclude that this clock might provide robustness in case of fluctuating or stressful conditions.

I have focused my comments on the experimental aspects of this manuscript.

1. The main conclusion of the present work is the importance of cell-cell communication in establishing the circadian clock of Anabaena, which is in contrast to that observed for the unicellular Synechococcus. This is an interesting observation. However, I think the authors must provide more compelling evidence to strengthen this conclusion. For example:

a. The effects of filament lengths are unclear to me. In Figure 2, the authors compare the gene expression profiles for cells up to 10 cells apart in the same filament and state that these are comparable. However, according to their model, there seems to be a length-dependent effect. To test the same, the authors can compare profiles of cells in increasing intervals and provide plots as shown in Figure 2A for the same. In general, while the authors use synchronization index to characterize degree of synchronization in various conditions, the representation of expression profiles as in Figure 2A is better to follow. This analysis for cells deleted for sepJ/ fraCD must be included.

b. In addition to the analysis above, the authors can block cell division (using drug treatment such as cephalexin) to assess how division affects the oscillatory patterns observed.

c. The authors make an argument in the Discussion section that levels of Kai proteins may not be limiting to trigger the coupled clock behaviour they observe. In order to support this conclusion, they must perturb expression of these genes (overexpress the kai operon).

d. The authors propose that this cell-cell communication must involve transport of small molecules. Could the authors please elaborate on how these molecules feed directly into regulation of gene expression patterns? Are they produced in the cell or freely diffusing in the growth media? The current Discussion section does not explain this idea with clarity. It would be nice to include the influence of such a molecule in their theoretical framework as well.

2. The physiological relevance of the mechanism described in this study is unclear to me. How do the authors envision such clock coupling provides robustness and a biological advantage under stress conditions? Could such robustness be assessed under various sugar availabilities or under starvation for example?

Reviewer #2:

This is a nice paper on measurements on circadian oscillations in Anabaena filaments. There has been a lot of investigations on circadian rhythms in various systems. I am not an experimentalist and I do not work on circadian systems so it is hard for me to judge whether this paper presents fundamental new measurements on the circadian clock and its relations to the cell cycle. However, the paper appears very comprehensive and presents to the best of my knowledge new nice results.

Let me concentrate on the model presented in Figure 5A. This is defined by different interactions between various phosphorylated states of KaiC gene. I should like the authors to explain in more details the different links in this diagram. It probably makes sense that there are transitions between the phosphorylated states but please explain in more details. It is well know that oscillations are generated from negative feed-back loops.

In the diagram there are two negative links, from S state to Kai A and back again. This by itself defines a positive feed-back loop which will give rise to a switch not to oscillations. Therefore the only negative loop I can identify is the one S -> KaiA -> D(ST) -> S. Is that the loop that is responsible for all the oscillations? I might doubt it but please explain.

The authors have 'exported' all equations to the supporting information but I would have liked whether it is possible to include the equations for this basic loop as a diagram in the figure?

From the underlying deterministic model of this diagram the authors obtain the phase diagram in Figure 5C. I presume the line to the colored region is defined through a Hopf bifurcation, am I right? As the authors mention, there is 'only' a circadian time scale at the lower right boundary. But is that not surprising?

Next, the authors presents a model for an array of coupled circadian clocks which is supposed to model Anabaena through cell-cell communications via septul proteins. The full structure of the model is nicely presented in the supporting information. Well, it is not a simple model that is developed and I cannot claim I understand all the involved steps. Some of the results are presented in Figure 6. Figure 6B shows results from Gillespie on how the cells are correlated. Bit I am missing a little more explanation. What is the noise level (volume/number of molecules in Gillespie?), max/min of what. And in the text there is an error where Figure 6B says it is the power spectrum. Altogether, I find it a nice paper.

Reviewer #3:

The system is very interesting and offers a rare natural example of a system of coupled oscillators which have been the subject of much theoretical investigation.

I think the results certainly merit consideration in eLife. However, I think some of the theoretical claims made are not sufficiently supported in the paper in its current version.

1. A central argument that the system does not display deterministic oscillations seems to rely heavily on Figure 5C. However, it is a little difficult to see how much that conclusion is robust to the very specific model and parameters used. For example, it would seem that a factor of 2 in [Kai C] and a factor of 10% in [KaiA] would completely change that conclusion. Surely, this is possible given that there is evidence that Anabaena differs from Synechococcus as the authors themselves claim. Perhaps there is no parameter combination (including parameters other than the two the authors chose to vary) which would show deterministic oscillations without making the Figure 5B fit significantly worse but this is a little unclear from the current text.

2. Following on that point, the authors do not seem to sufficiently discuss the applicability of Rust et al. model and parameters to Anabaena. I think the paper would be considerably strengthened by a clear discussion on how robust the conclusion is to different parameter variations and the applicability of this choice, as well as the possibility of deterministic vs noise driven oscillations.

3. There are three different Kernels used for the cell-to-cell communication, about which little is known experimentally. Of these, the exponential seems most plausible in the absence of other knowledge. The caption of Figure 6D says the complex coherence function is fit using an exponential kernel but the sharp cutoff in the fit seems to suggest a constant Kernel with a sharp cutoff. The SI suggests a power law Kernel fits well but it is unclear what the justification of such a Kernel would be. As an aside, is it possible to simplify the equations in a mean-field kind of way?

4. It is a little unclear in Table 1 why R is so high even for different filaments particularly since it was originally introduced in Garcia-Ojalvo as an order parameter that sharply distinguishes between synchronization and lack of.

I think the paper is not suitable for eLife in its current form but a clearer and stronger discussion of model choice and fitting could remedy that.
