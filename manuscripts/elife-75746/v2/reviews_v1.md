# Peer review - Round 1

Editors:
- Sonia Sen, https://ror.org/04xf4yw96 Tata Institute for Genetics and Society India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75746.sa0](https://doi.org/10.7554/eLife.75746.sa0)

This study investigates development of the mechanosensory organ on Drosophila notum. It combines live imaging, mathematical modelling, genetics and behavioural analysis to show that, in the peripheral nervous system of Drosophila, entry of progenitor cells into mitosis is spatially and temporally controlled. The authors suggest that this ensures proper targeting of sensory neurons within the ventral nerve cord. This timing is important for axonogenesis and proper spatial arborization, ultimately influencing the animal's behaviour. The study will be of broad interest to those who work on the developmental of sense organs, and in general on the role of timing in development.


---

# Peer review - Round 1

Editors:
- Sonia Sen, https://ror.org/04xf4yw96 Tata Institute for Genetics and Society India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75746.sa1](https://doi.org/10.7554/eLife.75746.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "A neural progenitor mitotic wave is required for asynchronous axon outgrowth and morphology" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Sonia Sen as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Claude Desplan as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Tatsumi Hirata (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

This study investigates development of the mechanosensory organ on Drosophila notum using various genetic techniques. They combine live imaging, mathematical modeling, genetics and behavioral analysis to show that in the peripheral nervous system of Drosophila, entry of progenitor cells into mitosis is spatially and temporally controlled. This, the authors suggest, ensures proper targeting of sensory neurons within the ventral nerve cord. The study will be of broad interest to those who work on developmental processes, and particularly to those interested in sense organ development.

While appreciating the quality of the work and its presentation, we have a few suggestions for the authors that they should be able to address within the time frame of a revision:

1. Related to the model: There are some questions and concerns about the model that have been raised in two of the reviews. They are largely clarification issues. Could the authors please respond to each of them in their revised version? The individual points can be found in the detailed reviews below.

2. All three reviewers raised concerns about possible effect the genetic perturbations might have on bristle development in general. This would have implications for the axogenesis phenotypes that the authors report. So, could the authors check that this is not the case? For example, they could put the directly driven neur-H2B::RFP in their genetic background and look at the characteristic arrangement and size of the bristle lineage nuclei; or stain it with markers such as pros, cut, elav, or any others of their choice that report cell fate identities within an SOP lineage.

3. Finally, there are concerns that in some cases, for example in the of timing of the mitotic wave and its effect on axogenesis, the interpretations of the data are too strongly made. The authors should revisit the text in these sections (Please read the individual reviews for the detailed comments.)

Reviewer #1 (Recommendations for the authors):

We found the study to be interesting, thoroughly executed, well documented, and a pleasure to read. We have a few comments and concerns, which I'm sure the authors should be able to address.

Related to the model

– Is there any interaction between the rows? If SOPs are extending filopodia in all directions, one would expect the wave to move concentrically, and not in the A-P axis.

– One of the predictions from this would be that the level of the inhibitor (Sca) should also follow a wave like progression – start off high in a G2 arrested SOP and drop off as the SOP divides. From the expression patterns shown, this is not possible to see, and the live imaging of Sca:GFP shows only one or two SOPs. Could the authors please comment on this?

– If all SOPs are creating both the activator and the inhibitor, why does self-inhibition not occur?

– The authors mention an acceleration of division with time. We could not see this clearly in the experimental data, but also don't understand what, in the model, might result in it. While section 1 in the Model Description attempts to explain this acceleration with a simpler example, in case of the activator-inhibitor model the "acceleration" behaviour seems to depend on the threshold theta. Specifically, whether theta is below r/(1+2*mu) or between r/(1+2*mu) and r/(1+mu) seems to dictate whether the wave will have an acceleration or an asymptotically constant velocity respectively. Could the authors please verify/comment on this?

– Could the authors also elaborate on how they solved the equations (numerical scheme, initial conditions, boundary conditions) in the model description supplement? Specifically in the activator-inhibitor model, what were the boundary conditions used? The value of theta seems to be unmentioned in the figures both in the main article and the model description. This might be useful for others who want to take a similar approach in other systems.

– If inhibition stops upon losing contact, then the inhibition from cell k to its neighbours, and the inhibition from the neighbours to cell k, should all go to zero. This effect is better captured by a multiplication of Heaviside theta functions i.e. H(A_{K+1} – theta) * H(A_{k} – theta) + H(A_{k-1} – theta) * H(A_{k} – theta). Making this change allowed us to reproduce the figures in the article while the original equations did not yield the same results. Could the authors please comment on this?

Related to axon targeting and behaviour

– We were concerned that some of the phenotypes might be due to inappropriate cell fate specification in the SOP due to the manipulation of the notch pathway. Can the authors show that this is not affected?

General

– In the introduction, could the authors please talk about SOP cell division and fates, and the role of the notch pathway in it? This will help the reader interpret their results in the context of the entire process.

Reviewer #2 (Recommendations for the authors):

1) This is a hypothesis-driven paper. Individual phenotypes caused by gene manipulations look coherent only based on several hypotheses provided by the authors, but each hypothesis is not well supported by previous or present studies. Even though this reviewer generally agrees that original speculation and interpretation should be more highly appreciated and included in papers, and also that the hypotheses in this manuscript serve as a good guide for readers to digest the contents, some parts of the manuscript are just too assertive. Hypothetical arguments should be addressed as hypothetical. A few details are explained below.

2) The live analysis of mitosis timing is the strength of this study. Although the mitotic wave is not very clear in the heat-mapped pictures, the quantified data and the simple mathematical model help convincing understanding of the wave. The model intuitively explains the difference of characters in the wave propagation from the origin to second cells and that among other further SOPs. Although the authors discuss that the mitotic origin is determined by other mechanism, I still do not understand why the second origin does not appear upon suppression of the inhibitory signal. Or does it in fact appear? Notch-signaling mutants generally have more bristles in the thorax. Does this phenotype actually influence the analysis of scabrous mutants? The authors should discuss them in the paper.

3) In scabrous mutants, the mitotic wave is disrupted, but is not abandoned or synchronized. The word choice should be more careful. The critical caveat of the scabrous mutants is that positions of mitotic origin are not the same as those in the wild-type (Figure S2). This means that the mutation somehow affected cell-intrinsic characters of SOP cells themselves. Therefore, the mutant phenotypes described later cannot be attributed solely to changes of mitotic timing. Does the RNAi mutant show a similar distribution of the origins?

4) The cytoplasmic protrusions may be a candidate of cell-cell-communication, but this hypothesis still lacks experimental support in the SOP system. Because Rac1 is pleiotropic, it is similarly possible that the dominant negative form affected other aspects of the cells. The authors should be clearer about the limitations. Rephrase the conclusive subtitle of this paragraph.

5) The association between neuron generation timing and axon patterns has no supportive evidence at this moment. It is a pure speculation with no ground. The paper by Usui-Ishihara and Simoson referred in this manuscript examines inter-raw but not intra-raw differences. They used the length of bristles as an indirect scale of differentiation timing but did not examine the birth timing of the cells per se. Top of that, these authors only discussed the rough correlation in a few sentences in the paper. In this regard, this manuscript's claim that axonal patterning is altered because of the change of mitotic timing is obviously overstatement and misleading to readers.

Reviewer #3 (Recommendations for the authors):

There are a number of points where the clarity and presentation of the manuscript could be improved:

1. In Figure 1C, the authors use a linear regression to fit the data from individual SOP row, while in 1D the combined data from all three row is fitted with their model. However, no explanation is given for the difference in fit (linear vs non-linear) in the individual versus combined data. This should briefly be clarified in the text and/or theory supplement.

2. The data motivating the assumptions used to build the model should be better introduced. On line 02-to-06, the authors state these assumptions, but without further explanations the choice of model seems rather arbitrary. In order not to break the flow of the manuscript, the authors could refer in the results to a more detailed section in the methods where they explain the thinking behind their model and cite the relevant literature.

3. In general, it would be helpful to the reader to write the GAL4 driver used for the experiments in the actual Figures (e.g. 2A, 5B…).

4. Figure 4C, D: what developmental stage is this? It should be clearly indicated in the legend or main text.

5. For the experiments where tubG80ts is used to temporally control sca-RNAi and dominant-negative Rac, it would be useful to state the timings in the Figure legends or indicate it on the figures themselves. These details are important to exclude confounding effects due to interference with other aspects of bristle development than the mitotic wave.
