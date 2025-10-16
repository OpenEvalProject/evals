# Peer review - Round 1

Editors:
- Karsten Kruse, University of Geneva Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.61011.sa1](https://doi.org/10.7554/eLife.61011.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The authors study cell competition using simulations and experiments. The simulations quantitatively reproduce experiments and show that mechanical competition is determined by differences between the homeostatic densities of winners and losers, whereas tissue organization is key for biochemical competition. By linking cell-scale mechanisms to tissue-scale organization, the study provides fundamental insights into mechanisms underlying cell competition and is of broad interest for developmental biologists

Decision letter after peer review:

Thank you for submitting your article "Cell-scale biophysical determinants of cell competition in epithelia" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Naama Barkai as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Romain Levayer (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

In this manuscript, Gradeci et al. use a theoretical approach together with experiments to investigate biophysical determinants of cell competition in epithelia. Employing a cellular Potts model, which is fitted to rich experimental data, they determine values of parameters quantifying mechanical and biochemical processes involved in cell competition. The major finding of this work is that the difference between the homeostatic density of the winner and loser cell populations is a key mechanical parameter affecting competition. However, it is poorly affected by growth rate or tissue architecture. While, for example, Basan et al. 2009 already suggested that differences in growth rate will poorly affected the outcome of competition based on differences in homeostatic pressure, this is the first time that it is clearly demonstrated that they are sufficient to reproduce quantitatively experimental data. The authors also provide evidence that biochemical competition strongly depends on tissue organization. It is one of the most realistic modeling of cell competition which has been performed so far.

Essential revisions:

1. The manuscript seems to be poorly written. There is not a nice logical flow and the figure panels are referred to in an almost random manner, which makes it very hard to understand this work. Also, Figure 1A,B,E and Figure 2 are not very helpful. Several assumptions are not clearly explained. Please, improve the text.

2. The Potts model should be related more closely to cellular properties. What do the parameters represent? Can you give us information about how sensitive your results are to variations in the parameter values?

Previously, the authors have shown that WT cell proliferation increases in the vicinity of Scribble mutant cells (Bove et al. MBOC 2017). Using a continuous model, they also proposed that this boost of proliferation is required to recapitulate the dynamics of the two populations. It is somehow surprising that the authors did not describe or implement this process in their cellular Potts model (which now can includes information about cellular neighbourhood). Indeed, while the difference in homeostatic density is sufficient to recapitulate the cell population dynamics, it does not prove that this is the actual mechanism at play, and does not exclude alternative mechanisms. Could the authors test whether this alternative mechanism could – or could not – be sufficient to recapitulate Scribble competition dynamics? More generally, the point raised by the authors could be much stronger if they could compare the accuracy of their current model (purely based on differences in homeostatic density) with alternative models (e.g.: non cell autonomous process) to reproduce the Scribble competition scenario.

Also, alternatively, could this boost of proliferation be an emerging feature of differences in stiffness and local increase of Scribble elimination (hence increasing locally WT cell area and their proliferation )? Do the authors observe such local boost of proliferation in their model without implementing additional rules ?

3. So far, the main outputs of the model compared with the experiment are the evolution of cell density and number of cells. However, the authors do have experimental data about the rate of death and rate of division (Bove et al. 2017, Figure 2G). Actually the cumulative rate of apoptosis obtained in the simulation (Figure S4D of this study) seems to be different from the experimental curves (cell death of Scribble cells raised later in experiments, and the difference with WT cells is not as strong). Could the author comment on that or try to find an explanation ?

4. Most of the time, the authors mention the disappearance of the loser cells in the text, however most of the simulations finish before full disappearance of the loser cells (e.g. Figure 6C, k=0.1 and 1). Is this a matter of time (longer simulation would lead to full disappearance) or is there a steady state with loser cells maintained at low number ?

5. As stated and shown by the authors, the size of the cluster of loser cells strongly influence the outcome of biochemical competition. It is striking that for the fully sorted conditions, the losers survive irrespective of J-heterotipic. Intuitively this might be related to a perimeter other area ratio which reaches a critical value where apoptosis rate / cell splitting rate (both scaling with perimeter) are always lower than proliferation (scaling with area). Do you also observe such critical cluster size appearing in the partially sorted conditions ? This may be reflected by the final distribution of loser cell-clusters in the partially sorted condition (all clusters being larger than this critical value).
