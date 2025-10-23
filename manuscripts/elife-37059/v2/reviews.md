# Peer review - Round 1

Editors:
- Alfonso Valencia, Barcelona Supercomputing Center - BSC Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.37059.sa1](https://doi.org/10.7554/eLife.37059.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Context-enriched interactome powered by proteomics helps the identification of novel regulators of macrophage activation" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aviv Regev as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The paper proposes a combination of -OMICS data using a molecular network framework. The goal is to identify new regulators of macrophage activation related with cardiovascular disease (CVD). The assessment of the results is carried out by an enrichment analysis strategy, i.e. quantifying the position in the ranking of known cardio disease related drugs (from iCTNet) and pathways. A small scale loss of function experiment is performed for two newly proposed targets.

Essential revisions:

The critical questions that have to be clarified are the following:

1) Possible biases in the network construction and associated calculations.

(1a) The inclusion of small scale experiments in the network might end up biasing the results, since these experiments target well known proteins. Similarly, the network might contain other biases, e.g. smaller distances between druggable proteins.

(1b) Other related question would be if the definition of druggable proteins, obtained from a network based method, will influence their distribution in the network?

(1c) Use of the Pearson correlation instead of the partial correlation coefficient, and the possible bias towards indirect associations.

(2) Insufficient information and doubts on the procedures.

(2a) The comparison of the combined network with its two components, i.e.

PPI and co-abundance, seems to be incomplete and the specific methodological details not sufficiently clear. What is the prediction performance of the co-abundance network alone?

(2b) It is reasonable to question if the direct union of both types of networks is the best strategy. This issue should be discussed.

(2c) The reasons of additional filtering of the results obtained with the network based approach by requesting an additional level of expression – fold changes – is unclear. How and why the resulting candidates were selected requires additional clarification.

(3) The use of shortest path distances seems too simple as a measure of associations, while other alternatives, including network kernel distances,connectivity-based association measures, assortativity, and others, are commonly used in the field.

Reviewer #1:

The authors use an integrative analysis of proteomics, transcriptomics and molecular network data in order to identify new regulators of macrophage activation, which may be of interest as candidate therapeutic targets for cardiovascular disease (CVD). The proposed methodology, which combines omics-derived co-abundance networks with literature-derived molecular interaction networks, is evaluated by assessing the enrichment of the resulting top-ranked proteins in known CVD drugs as compared to a prioritization that uses only literature-derived network information, as well as by the enrichment of the top-ranked proteins in inflammation-related pathways and signatures. Moreover, for two new top-ranked proteins, in-vitro loss-of-function experiments are used to show that these proteins have a regulatory role in pro-inflammatory signaling.

Overall, the authors' approach is logical, and although the method is very similar to previous contextualized network distance based target prioritization approaches, the obtained results in the context of macrophage activation and CVD are new and interesting. However, major comments have to be addressed regarding potential biases in the network construction resulting from the inclusion of data from targeted low-throughput experiments, the comparative evaluation of network prioritization approaches (no cross-validation is performed), and the discussion of limitations regarding false positives and negatives in the combined networks and in the experimental evaluation of candidate drug targets.

(1) In the subsection “Construction of the literature-based protein-protein interaction (PPI) network”, the authors mention that the literature-based PPI network they constructed does not only include high-quality binary interactions from high-throughput Y2H screens, but also interactions from low-throughput experiments, protein 3D structures, as well as protein complexes derived from experiments that cannot confirm direct physical interactions (e.g. Co-IP). As the authors correctly mention in the third paragraph of the Introduction, such networks are often biased towards highly studied proteins. The addition of context-specific co-abundance edges may to a certain extent address limitations of the PPI network with regard to cell-type specificity, but since the authors combine the PPI network with the co-abundance network, rather than using the co-abundance information to filter the PPI network, biases and false-positives in the original PPI network will not be removed and still influence the final analyses. Moreover, as opposed to the partial correlation coefficient, the Pearson correlation used to construct the co-abundance network will identify many indirect associations and spurious associations between two variables resulting from shared dependencies on a third confounding factor variable. For these reasons, the authors should check how the results of their approach change if low-throughput experiments and sources of evidence limited to indirect associations (rather than physical interactions) are filtered out from the PPI construction. Similarly, the influence of the correlation measure used for the construction of the co-abundance network on the final results should be investigated, e.g. by testing alternative measures like the partial correlation coefficient or the biweight midcorrelation, which is more robust against outliers, and discussing limitations arising from potential confounding variables. Finally, the authors should consider and discuss whether using the co-abundance information to filter the PPI network, rather than combining the two networks (and their erroneous edges), would provide a more reliable final network.

(2) In their comparison of network prioritization methods based on known CVD drugs from iCTNet the authors relate the predictive performance for the combined networks (PPI + co-abundance networks) to the performance for using only the PPI network via ROC curve analyses. However, they do not compare the combined networks to using the co-abundance networks only, i.e. it is not clear whether the co-abundance networks alone as data source would already outperform the purely PPI-based analysis for drug prioritization, or whether only the combination of PPI + co-abundance networks provides a superior performance. Thus, ROC curves and statistical tests for evaluating the co-abundance networks only as compared to the combined networks should be added. The statistical test used for performance comparison should also be explained in more detail: The authors mention that they use a Mann-Whitney U-Test to compare the AUROC values; however, given that only one AUROC is available for each network (the PPI and the combined network), it is not clear how the Mann-Whitney U-Test is applied in this context, since this test requires more than one value per group: Do the authors use a cross-validated AUROC computation? This would be an appropriate and more robust approach than computing a single AUROC, and would enable a statistical performance comparison, but also needs to be explained in detail in the manuscript.

Especially if the authors optimize their model (e.g. by modulating the ratio of weights, as described in the second paragraph of the subsection “Addition of macrophage derived co-abundance edges increases CVD drug target prediction performance”), a cross-validation is needed in order to prevent that the same outcome data used to optimize the prediction approach is also used to evaluate it (i.e. preventing a circular analysis with misleading performance estimates).

(3) In the Abstract, the authors write that their approach revealed "top candidates for CVD therapeutic targets"; however, in the manuscript, the authors do not investigate the druggability of these candidate proteins (GBP1 and WARS), neither experimentally nor in-silico, but only experimentally asses their regulatory role using pro-inflammatory readouts. Thus, the authors should either limit the claimed discovery to have identified/confirmed the regulatory role of the candidate proteins, or alternatively, add analyses that confirm the druggability and/or show preliminary evidence confirming that CVD-specific disease phenotypes (rather than generic inflammation readouts) in a model system can be modulated specifically via GBP1 and WARS. The authors should also mention whether existing disease gene prioritization approaches would predict the same or different candidate proteins (currently no comparison is shown).

(4) The authors should explain why they use shortest path distances for quantifying network associations rather than network kernel distances or connectivity-based association measures. The multiplicity and density of interactions that interconnect proteins may provide more evidence for a functional association than the shortest path distances alone, and it is unclear whether considering longer-range shortest path distances in the analysis still provides a significant added informative value or rather spurious associations as compared to an association measure purely based on direct connectivity. These points and potential limitations of the used association measure should be discussed.

Reviewer #2:

The authors have demonstrated an interesting approach that starts with large scale data mining and end up with validation of potential target of CVD and in particular the macrophage activities in CVD.

The experimental design and workflow of the publication is clearly laid out, and it is didactic enough to walk through the manuscript without too many hurdles.

I see no major issue with the manuscript as is and found it actually quite good examplar of systems oriented study and target prioritization excercise.

Reviewer #3:

The article is well written but the Introduction and Discussion are too lengthy. My general concerns relate to:

(1) The authors have not carefully tested for confounding factors that might underlie some if not most of the observed correlations and prediction performances. Do the drug targets show some preferential presence in the co-abundance network versus PPI network and are there any degree differences between drug targets and other proteins in the co-abundance network and/or PPI network? Do co-abundance edges preferentially connect to hubs in the PPI network? If there are biases of these kinds then a random addition of edges to the network as empirical control might not capture this and modifications like adding random edges involving proteins in the co-abundance network would represent a more relevant negative control? To which extent is the definition of your drug targets influenced by network information because a network tool, iCTNet was used? Can this lead to circularity when using these drug targets as seeds in the network proximity approach?

(2) The authors state that the drug targets are not significantly close to each other in the network, yet, when used in the benchmark of the network proximity algorithm, the performance is good. Don't they have to be close in the network for the algorithm to work? Why use the LCC sometimes and the average shortest path at other times to determine closeness? What is the negative dataset used in the benchmark and can authors plot precision-recall curves as well to provide a better overview on the precision of the predictions? What is the prediction performance of the co-abundance network alone?

(3) The reasoning for why the candidate lists need to be further improved by using expression fold change data are not clear. Is the candidate list based on the network prediction not good enough? Then this can be clearly stated. Why were the candidates GBP1 and WARS picked? Because they show the highest expression fold change among the candidates? How many other proteins show as high or higher fold change justifying that the network prediction "helped" selecting among the differentially expressed genes those that are more close to known drug targets? To my non-expert understanding of the immune system, the experiments validate the function of the candidate genes in inflammation/immune response but that was an obvious hypothesis given their up-regulation in expression? How do these experiments validate the concept of using network proximity to drug targets to find new candidates? It remains unclear how the modulation of inflammation biomarkers by the candidates relates to CVD. Contrary to statements in the discussion, I cannot find experimental validation of mechanisms.
