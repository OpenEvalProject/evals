# Peer review - Round 1

Editors:
- Anne-Florence Bitbol, Ecole Polytechnique Federale de Lausanne (EPFL) Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.87747.3.sa0](https://doi.org/10.7554/eLife.87747.3.sa0)

In this valuable article, the authors use an existing theoretical framework relying on information theory and maximum entropy inference in order to quantify how much information single cells can carry, taking into account their internal state. They reanalyze experimental data in this light. Despite some limitations of the data, the study convincingly highlights the difference between single-cell and population channel capacities. This result should be of interest to the quantitative biology community as it contributes to explaining why channel capacities are apparently low in cells.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87747.3.sa1](https://doi.org/10.7554/eLife.87747.3.sa1)

In this paper the authors present an existing information theoretic framework to assess the ability of single cells to encode external signals sensed through membrane receptors. The main point is to distinguish actual noise in the signaling pathway from cell-cell variability, which could be due to differences in their phenotypic state, and to formalize this difference using information theory. After correcting for this cellular variability, the authors find that cells may encode more information than one would estimate from ignoring it, which is expected. The authors show this using simple models of different complexities, and also by analyzing an imaging dataset of the IGF/FoxO pathway.

I am only partially satisfied by the authors response. To me, the main question that was unanswered, while being at the core of the claim of the paper, was the magnitude of within-cell variability across repetitions of the stimulus.

This can only be done on the IGF/FoxO system because, as the authors acknowledge, the EGF/EGFR system does not have any data to support any claim about single-cell information that's not heavily informed by models, which assume by construction that this variability is small, naturally leading the desired conclusion.

The authors now measure within-cell, across-repetition variability (delta_0) for IGF/FoxO, but:

- they compare it to cell-to-cell variability, finding that it's smaller. That's good and that supports the main claim of the paper that single cells are more precise than a mean cell. However they don't show it in the paper, but only in the response.

- they also don't compare it to within-cell, within-stimulation variability across time. But this latter variability is what they (wrongly) used to estimate information, and still do in this revision. However I think this is approximated by the blue "simulation" violin plot in Reviewer Figure 2. The true variability is clearly larger than previously assumed. So it's strange that they conclude that "our estimates of cell-to-cell variability signaling fidelity are stable and reliable."

- they don't use this delta_0 variability to revise their estimate of the information accordingly.

- since variability is small compared to the differences between distinct stimulations, of which there are only 4, all information quantities they get are around 2 bits, which is not approaching the information capacity but merely a statement that the number of tested doses is small.

I strongly recommend that the authors actually report the figure they provided as Reviewer Figure 2 in the manuscript. In addition, they should not claim that the within-cell variability (captured by the variability across distinct presentations of the stimulus) is well captured by their initial estimate (based on the variance within a single presentation of the stimulus).


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87747.3.sa2](https://doi.org/10.7554/eLife.87747.3.sa2)

Goetz, Akl and Dixit investigated the heterogeneity in the fidelity of sensing the environment by individual cells in a population using computational modeling and analysis of experimental data for two important and well-studied mammalian signaling pathways: (insulin-like growth factor) IGF/FoxO and (epidermal growth factor) EFG/EFGR mammalian pathways. They quantified this heterogeneity using the conditional mutual information between the input (eg. level of IGF) and output (eg. level of FoxO in the nucleus), conditioned on the "state" variables which characterize the signaling pathway (such as abundances of key proteins, reaction rates, etc.) First, using a toy stochastic model of a receptor-ligand system - which constitutes the first step of both signaling pathways - they constructed the population average of the mutual information conditioned on the number of receptors and maximized over the input distribution and showed that it is always greater than or equal to the usual or "cell state agnostic" channel capacity. They constructed the probability distribution of cell state dependent mutual information for the two pathways, demonstrating agreement with experimental data in the case of the IGF/FoxO pathway using previously published data. Finally, for the IGF/FoxO pathway, they found the joint distribution of the cell state dependent mutual information and two experimentally accessible state variables: the response range of FoxO and total nuclear FoxO level prior to IGF stimulation. In both cases, the data approximately follow the contour lines of the joint distribution. Interestingly, high nuclear FoxO levels, and therefore lower associated noise in the number of output readout molecules, is not correlated with higher cell state dependent mutual information, as one might expect. This paper contributes to the vibrant body of work on information theoretic characterization of biochemical signaling pathways, using the distribution of cell state dependent mutual information as a metric to highlight the importance of heterogeneity in cell populations. The authors suggest that this metric can be used to infer "bottlenecks" in information transfer in signaling networks, where certain cell state variables have a lower joint distribution with the cell state dependent mutual information.

The utility of a metric based on the conditional mutual information to quantify fidelity of sensing and its heterogeneity (distribution) in a cell population is supported in the comparison with data. Some aspects of the analysis and claims in the main body of the paper and SI need to be clarified and extended.

Remaining Comments:

- I think Review Figure 2 which is currently in the SI would improve the main body of the paper if moved there. In that case, the discussion of this figure in the main text would have to address more than it currently does, namely "the same cell's FoxO responses to the same input were found to have significantly less variation compared to the variation within the population".
