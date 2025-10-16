# Peer review - Round 1

Editors:
- Constance L Cepko, Harvard Medical School United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.32937.sa1](https://doi.org/10.7554/eLife.32937.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for sending your article entitled "Neurogenic decisions require a cell cycle independent function of the CDC25B phosphatase" for peer review at eLife. Your article is has been evaluated by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Didier Stainier as the Senior Editor.

The major issue to be addressed is the non-cell cycle function of CDC25B. The data presented are intriguing and indicate an alternative role for this protein. Some data regarding the nature of that role would be required for acceptance to eLife.

Reviewer #1:

Bonnet et al. describe a novel function of Cdc25B in promotion of neurogenesis in the developing mouse and chick spinal cord. They first confirmed in mice their previous results obtained with chick embryos showing that Cdc25B ablation prolongs G2 phase of the cell cycle and attenuates neurogenesis. Conditional knockout of Cdc25B reduced the numbers of both Pax2+ GABAergic neurons and Tlx3+ glutamatergic neurons, without significantly affecting that of Pax7+ progenitors. With the use of a cell cycle-dependent cis element, the authors also showed that overexpression of Cdc25B is sufficient to promote neuronal differentiation in the chick spinal cord without affecting orientation of the mitotic spindle or asymmetry of spindle size. Furthermore, Cdc25B depletion and overexpression reduced and increased Tis21+ neurogenic divisions, respectively. Interestingly, this neurogenic function of Cdc25B appears to be independent of its cell cycle-regulating activity, given that overexpression of a Cdc25B mutant that lacks the CDK binding domain still promotes neuronal differentiation. A mathematical model supports the notion that modification of cell cycle duration does not simply account for changes in the rate of neurogenic division under given conditions.

The study was well executed and the manuscript is well written. It would greatly strengthen the study if the authors could show the nature of the cell cycle-independent mechanism by which Cdc25B promotes neurogenic division, but this may be too much to ask.

Reviewer #2:

This manuscript considers the role of CDC25B on neurogenesis, and builds upon previous work (Peco 2012). The experimental results are, in general, sound. Some modelling is included, although this does not add significantly to the paper.

The highlight is genetic evidence that CDC25B has a cell-cycle-independent effect on differentiation. I find this to be an important point, given that there have been many correlative observations between cell cycle length and differentiation rate.

1) How faithfully is division mode measured?

In multiple places in the manuscript, claims are made regarding division mode (i.e. PP vs. NP vs. NN), e.g.

"symmetric neurogenic divisions require CDK interaction [with CDC25B]"

However, I am not 100% convinced with the measurement of division mode, given the present data.

Firstly, there is no direct live imaging/lineage tracing data to corroborate the measurement based on Sox2/tis21. Previous work (Saade et al. 2013) has shown that mitotic Sox2/tis21 expression predicts division mode in wildtype cells (although, as far as I am aware, there is a limited number of live cell tracks which directly back this up). However, it's not guaranteed that Sox2/tis21 remains a reliable division mode marker for the perturbations considered in this paper.

Secondly, this paper measures Sox2/tis21 in all progenitors; the original paper (Saade 2013), only in mitotic cells. Whilst Figure 4B does show that, on average, and at this time point, these measurements are similar, it means that the results quoted in this manuscript are less direct than in (Saade 2013), and there could be confounding effects due to the timing of reporter expression.

Therefore, I would suggest that either:i) the Sox2/tis21 measurements are complemented with a small number of direct lineage tracing experiments to confirm the main findings (e.g. that "symmetric neurogenic divisions require CDK interaction [with CDC25B]"), orii) the writing is changed to de-emphasize "division mode", and instead talk about overall "differentiation rate" (equivalently, the parameter "1 – γ" in the modelling section).

One reason that I think this distinction is important is that recent work in the chick neural tube [1] proposed that division mode statistics follow a binomial distribution i.e. daughter cells differentiate independently of one another. It is important to show whether the perturbations in this paper (e.g. CDC25B∆CDK) affect differentiation rate (γ) generally, or specifically generate a certain type of divisions (e.g. NP).

2) Model

Overall, I am not positive about the use of modelling in this paper. Whilst it is reassuring that the fairly simple model can fit a handful of datapoints on neuron fraction (Figure 6C), this is perhaps not all that interesting or impressive. Similar models have been generated previously [1].

What is interesting, is the claim:

"mathematical modelling reveals that cell cycle duration is not instrumental in controlling the mode of division."

However, I find the model suggested by Table 1 and Supplementary Information 3.2 a rather extreme scenario. To me, a more natural model would be where division modes are still probabilistic (with rates αPP, αPN, αNN), but now these rates are allowed to vary with cell cycle duration. It seems very difficult to rule out this more realistic model given the data presented.

[1] A Branching Process to Characterize the Dynamics of Stem Cell Differentiation, David Miguez, Scientific reports, 2015.
