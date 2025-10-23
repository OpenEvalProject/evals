# Peer review - Round 1

Editors:
- Irene Giardina, https://ror.org/02be6w209 Università Sapienza Italy

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72707.sa0](https://doi.org/10.7554/eLife.72707.sa0)

This work uncovers a simple but far-reaching statistical principle that describes the geometry of cell packing in snowflake yeast and green algae. It draws on ideas from granular physics to offer new insight into universal rules of multicellular geometry that are otherwise easily obscured by the cell-scale idiosyncrasies of the different biological systems.


---

# Peer review - Round 1

Editors:
- Irene Giardina, https://ror.org/02be6w209 Università Sapienza Italy

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72707.sa1](https://doi.org/10.7554/eLife.72707.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Cellular organization in lab-evolved and extant multicellular species obeys a maximum entropy law" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Both reviewers praise the quality of the paper and the relevance of the results. There are not, in their opinion, critical aspects in the manuscript to be further addressed. However, they suggest a number of revisions, which would improve the clarity and presentation of the work. In particular, both reviewers think that more discussion is needed of the maximum entropy model, e.g. whether additional information on higher order structures or morphology related correlations might lead to more effective statistical models. Referee 2 also advises for more contextualization of the results, and a wider discussion about their generality.

Below the full reports, the authors are kindly invited to take into account the referees' comments in a revised version.

Reviewer #1:

The manuscript by Day and colleagues investigates the geometry of cell packing in two multicellular eukaryotes (snowflake yeast and green algae). Using a combination of experiments and models drawn from statistical physics, they show that the distribution of cellular neighborhood volumes follows a simple universal form – a modified gamma function – that arises from a maximum entropy argument. Using simulations of different growth processes, they then show that these universal distributions are ubiquitous-arising, for example, even in correlated systems as long as there is a minimal level of noise. Finally, they show how these principles contribute to emergent evolutionary features (specifically group size distributions) in snowflake yeast, and use simple theoretical models to argue that fluctuations, while inherently stochastic, give rise to robust structures that do not depend sensitively on the microscopic and biological features of the system.

This paper is a beautiful example of how simple biophysical models can provide fundamental and unifying insight into complex biological systems. It is well written, addresses an important and timely topic, and raises intriguing questions about the balance between "regulated" biology and simple statistical physics as selective forces for evolution.

I have several comments for the authors to consider, at their discretion. Overall, I really enjoyed this paper and learned a great deal from it.

– The manuscript offers an interesting guiding principle that describes two considerably different biological systems. As the authors show in simulations, the principle is expected to hold over a broad range of conditions, but of course not universally (though even small levels of stochasticity broaden the range of applicability). I think the paper could be improved by expanding on the discussion of these limitations. In particular, it is not clear to me exactly how surprising it is to see "good" fits to a 2-parameter distribution of this sort (or more generally, what level of "good" we should expect of the fits in finite data sets like these). The authors address this issue in part by showing fits to other distributions, which is nice. But I wonder if it would be helpful to also include (or at least discuss) more systematic model selection. To be clear, I find the analysis quite convincing as is. But I am trying to get my head around the limitations, and in particular, to get a feel for how likely one is to see similar "goodness of fit" results using other distributions with a relatively small number of parameters.

– Related to the previous point: one approach might be to construct a type of "null" model from the data, perhaps by systematically shuffling the data in some way and then bootstrapping to evaluate the likelihood of achieving fits of similar quality.

– Have the authors considered trying to systematically quantify the impact of including higher-order structures in the max ent model? For example, one could perhaps use multi-information metrics (https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.91.238701) to evaluate the extent to which higher-order features of the data are relevant / necessary; the idea is essentially to construct maximum entropy models with various levels of data complexity "built in" and then evaluate (perhaps with an info-theoretic style metric) the extent to which that complexity improved the model. Perhaps something similar has been done for granular materials to capture higher-order statistics of packing? I ask this primarily out of curiosity, not as a serious criticism of the current approach. A discussion of this point might add to the paper.

Reviewer #2:

Day, Thomas C. et al. investigate the geometrical statistic of cell packing in multicellular organisms. Using a maximum entropy prediction originally developed in the study of granular materials, the authors show that the statistics of cell packing imposes a robust physical, entropic constraint on the geometrical arrangement of cells. Strikingly, the authors show that both snowflake yeast evolved under lab conditions and wild-type Volvox, which develop according to very different processes and have disparate overall morphology, both exhibit cell packing statistics consistent with the maximum entropy predictions. They then use simulations to show that entropic cellular packing can arise from various modes of multicellular development due to randomness in cell positions and that substantial deviations from entropic packing arise only in the case of low developmental noise (randomness) and strong correlations in cell positions. Finally, the authors use theory and measurements from experiments with yeast to show how maximum entropy statistics dictate size heritability in simple multicellular systems. Together, their results support the perhaps counterintuitive result that developmental randomness can actually underpin developmental reproducibility, in this case reproducibility in the geometry of cell packing in terms of the free space associated with individual cells within a multicellular structure. This work contributes the identification and new consideration of a fundamental physical constraint of particular relevance to the evolutionary origins of multicellularity and to multicellular morphogenesis in general.

The conclusions of this paper are well supported by the rigorous analysis of data and simulations.

Work on the evolution of multicellularity has traditionally focused on molecular and genetic mechanisms, but because multicellular morphogenesis is an inherently physical process, biophysical studies provide an important complementary perspective. A particular strength of this paper is that insights are derived from theory that requires few, but specific, conditions be met in order to be satisfied, and therefore stands to apply generally to diverse multicellular systems, irrespective of many differences between them. The combination of empirical results from disparate multicellular systems in conjunction with simulations encompassing an expanded set of multicellular morphologies and growth processes compellingly support the generality of the insights. Beyond simply speculating about the implications of entropic packing on the function of multicellular systems, the authors demonstrate impact or lack thereof on aspects of form and function in multicellular yeast and Volvox. Importantly, simulations allowed the authors to investigate in detail the robustness of theoretical predictions in terms of deviations from theory arising from developmental processes. In addition to providing new insight, this work lays the foundation for the exciting possibility of inferring aspects of developmental dynamics and regulation simply by observing the statistics of cell packing in an organism, which could be of great use in comparative evo-devo studies where developmental processes are difficult or impossible to observe.

While the work is very strong overall, there are a few caveats to consider, primarily concerning the simulations. Multicellularity takes many forms by many different processes among eukaryotes. While simulations do cover a range of different morphologies and developmental processes found in nature, factors not explicitly addressed such as constraint or patterning by secreted extracellular matrix, differences in cell shape, cell migration, and others can lead to different kinds of multicellular form. The extent to which potential correlations imposed by diverse morphologies might lead to deviations from theoretical maximum entropy predictions, and how robust those deviations might be to noise is not entirely clear. Additionally, the randomness strength in simulations from high to low, while reasonable, does not appear to be grounded in empirical characterization of randomness strength in developmental processes across biological systems. Ultimately, although they leave some uncertainty as to the generality of the results, these limitations do not contradict or significantly diminish the key claims of the paper.

Comments for the authors:

1) The simulation results are compelling but left me with some questions. To what extent do the morphologies and processes investigated by simulations address the diverse forms of multicellularity encountered across eukaryotes? To what extent does the overall shape of the multicellular structure affect the cell packing distribution (e.g. multi-lobed structure as in Zoothamnium niveum, dichotomous branching as in Dinobryon, something with an undulating boundary)? Are there any examples of simple multicellular eukaryotes that might exhibit very strongly correlated cell positions? What is known about randomness strength or precision in developmental processes in biological systems, and if anything is known, how does this compare to values in simulations? Providing a bit more contextualization or motivation for specific choices in simulations could help address these questions and would support the generality of conclusions drawn from the simulations. Although I am convinced that the results hold for a broad range of multicellular architectures and do not think that the possible existence of a few edge cases contradicts the main conclusions of the work, it is not entirely clear to me that the effects of growth morphology, connection topology, and dimensionality have been accounted for.

2) The sections titled "Multicellular motility is robust to cellular area heterogeneity" starting on p. 11 is slightly perplexing. It is certainly interested, and I see that it addresses a question that may arise from analysis of Volvox cell packing, but in its current form, I do not believe it contributes substantially to the key points of the paper. The introduction section seemed to imply that the results would demonstrate that fluctuations in cell packing may play a role in the evolution of multicellular systems, but as I understood them, the results suggest that fluctuations do not affect motility, at least implying that there should be little to no effect on any aspect of fitness related to motility. It is possible that there could be other aspects of organismal fitness related to cell packing, so while these results are consistent with cell packing fluctuations not necessarily impeding or constraining the evolution of multicellularity, they do not strongly support that conclusion. Perhaps contextualizing the results a bit more in terms of key points of the paper while reporting them and referring to them in the Discussion section might help the reader better appreciate their significance within the context of the paper overall.

3) I might suggest removing or otherwise modifying the phrase "highly-evolved" (p.14) as its meaning is unclear, has connotations of evolutionary teleology, and clashes with the fact that all extant organisms share an evolutionary history of equal length. Maybe something such as "organisms with highly-regulated development" may be more appropriate.

4) Is anything known about the source of correlated subregions of cells in Volvox? Do the authors have any ideas about this? Either way, it would be interesting to know and may warrant at least a small comment in the text.

5) In the author list, SSH is missing an asterisk to denote corresponding authorship.

6) An "e" is missing in "surface" in the caption for Figure 2B.

7) I believe the dotted red line in Figure 4B should be a solid line to match those in panels A and C.
