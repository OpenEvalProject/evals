# Peer review - Round 1

Editors:
- María Mercedes Zambrano, CorpoGen Colombia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.61968.sa1](https://doi.org/10.7554/eLife.61968.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Knowledge of the functions and interactions among members of a complex microbial community is crucial to understanding their roles and ecological relevance. This work presents a flexible workflow, M2M, tailored to the metabolic analysis of microbiomes from metagenomics data. It integrates several tools that allow metabolic modelling of large-scale communities, inferring metabolic complementarity and identification of species key to a given community.

Decision letter after peer review:

Thank you for submitting your article "Metage2Metabo: microbiota-scale metabolic complementarity for the identication of keystone species" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Gisela Storz as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Daniel Machado (Reviewer #1); Oliver Ebenhoh (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, when editors judge that a submitted work as a whole belongs in eLife but that some conclusions require a modest amount of additional new data, as they do with your paper, we are asking that the manuscript be revised to either limit claims to those supported by data in hand, or to explicitly state that the relevant conclusions require additional supporting data.

Our expectation is that the authors will eventually carry out the additional experiments and report on how they affect the relevant conclusions either in a preprint on bioRxiv or medRxiv, or if appropriate, as a Research Advance in eLife, either of which would be linked to the original paper.

Summary:

This study presents a pipeline for large-scale metabolic analysis of genomes and metagenomic data. When evaluated on gut microbiome genomes from cultured species and metagenome-assembled genomes, this pipeline was able to reconstruct metabolic networks, identify potential metabolites, and provide information on minimal communities for a given target production and keystone species, defined here as species that are essential for a community to perform a certain metabolic function. The manuscript clearly formulates limitations, explains the software and functionality, and provides source code in a well-structured and clear git repository.

Essential revisions:

The paper could benefit from revisions to improve clarity, and to showcase the tool's versatility and performance. While aspects of the pipeline are novel, such as relying on topological methods and the use of Answer Set Programming to solve the problems of finding minimal sets of reactions or minimal sets of organisms, the authors need to revise some of the novelty claims in light of previous work and existing tools.

Please address the following concerns regarding the novelty of the pipeline and its automation, as well as comparison with existing tools and annotation:

1) There are already some tools that can automate GSMN reconstruction from genomes and MAGs (for example, ModelSEED and CarveMe, this one mentioned), calculate cooperation from GSMNs (SMETANA; Zelezniak et al., 2015), and workflows that automate some tasks such as metaBAGpipes (https://github.com/franciscozorrilla/metaBAGpipes), which assembles MAGs from raw metagenomics data, CarveMe, MEMOTE (model quality control) and SMETANA) and in KBase it is possible to assemble MAGs, run ModelSEED, and merge the single species models into community models for further analysis. These options go from raw metagenomic data (which the m2m software apparently doesn't) to community GSMN analysis and simulation.

2) It seems incorrect to state that their network-expansion algorithm can scale to large communities, unlike other simulation methods based on flux balance analysis. There are LP and MILP implementations of FBA community simulation methods. The LP methods scale linearly with the number of species (Popp and Centler, 2020 recently simulated a 773-species community with FBA). The MILP-based methods are worst-case exponential, but commercial solvers like CPLEX and Gurobi implement very efficient heuristics that allow for fast simulation. To make this claim, the authors should clearly state what is the computational cost (using Big O notation) of their method and show that it is lower than FBA based methods.

3) Different databases are functionally annotated by different tools (Prokka and EGGNOG). Annotation method for the third dataset is unclear. Different methods are employed on different datasets which in turn might hurt the analysis due to lack of standardization of the inputs.

4) Please clarify what is meant when stating that their network expansion algorithm is more robust "in the face of missing reactions". If this means that the algorithm doesn't fail to compute, then it might lead to results that may represent an incorrect metabolic landscape. As such, robustness may not necessarily be correct (or desirable). It could also be that the metabolic end-products obtained with FBA (by performing flux variability analysis of the exchange reactions) would in the end be the same, since in both cases they have to be topologically reachable regardless of the stoichiometry being accounted for or not.

5) While the authors mention reasons for robustness of their algorithms, they do not test these possibilities. Perhaps these could be addressed given that they have all the data required to answer the question.

Please take into account the following points in order to improve the manuscript.

6) The Materials and methods section could benefit from a major revision as it is going back and forth from describing the datasets and the pipeline (the focus is unclear). It'll be useful to have more details on critical steps in the pipeline such as the metabolic objective and community reduction steps and keystone species discovery.

7) The average number of metabolites per model is higher than the average number of reactions (1366 vs 1144 for the gut dataset). GSMNs usually have a lot more reactions than metabolites, hence their underdetermined stoichiometric matrices, and large number of degrees of freedom. Also, the average number of reachable metabolites is only 286, i.e. only about 20% of the metabolic network is reached. How is this possible, and how can one trust such models?

8) There are multiple instances in the Results section where the authors present the p-value for a statistical test without presenting also the effect size and/or test statistic. Knowing the statistical significance is not helpful without knowing the effect size. For instance: "The community diversity varied between disease statuses, with a significantly higher number of MGS observed in T1D individuals forming the initial communities (anova p < 0.01, Tukey HSD test p < 0.01 vs control)."

9) The authors mention that "A classification experiment on the composition of the community scope can, to some extent, (AUC = 0.73 +/- 0.15) decipher between healthy or diabetes statuses." But is this better than a classification based, for instance, on OTU analysis, or functional meta-genome analysis? Although the results are interesting, in the end it is hard to convince the reader that using GSMN reconstruction provides an advantage compared to using the metagenomics data directly.

10) In general, results are not compared to the state of the art and the Results section should contain more specific examples of metabolites/pathways of interest, bacterial species and their known or novel interactions. Additionally, it is mentioned that the datasets are similar – it'll be useful to have a section summarizing the results from all analyses.

11) The utilization of keystone species in this work is not entirely correct. Here the authors use keystone species to mention species that are always present in the set of minimal communities enumerated to produce a given set of metabolites. The definition of keystone species in a community are those whose removal would cause the collapse of the community. Since the simulation method used by the authors doesn't allow to test for community stability, the application of this term does not seem appropriate.

12) Keystone species are also described as the output of the tool and could use a more detailed report and examples in the Results section. These are very interesting and currently get lost between the lines.

13) There are several aspects of the figures that can be improved.

– Figure 1 is confusing could use some reorganization, so the pipeline steps are clear, consider adding numbers to the different steps.

– Figure 2 is very hard to digest. I have difficulties understanding what the figure actually tells me. What is the meaning of the white fields, are the sub-figures connected despite having a different x-axis, and what is the overall message?

– The power graphs are interesting, but it is unclear if they were generated by the tool since this is not clear in the manuscript. In addition, the usefulness of the power graphs in Figure 3 is not fully evident. What do we learn from them and what are the large number of circles? If three subgroups are connected, why are two of them encircled in an extra circle?

– Figure 4 presents an analysis that is downstream of the presented software paper since it illustrates how the output of the software can be further analyzed. In order to appear in the main text of the manuscript, it needs to be better explained since it is hard to understand with the information given. For example, what do the Receiver Operator Curves (ROC) actually represent? More background information is required.

14) The authors should define the essential and non-essential symbionts and add more context on their known interactions in the Introduction and Results sections.

15) The comparison to other platforms such as Kbase and other genome scale models should be discussed in more detail in the Introduction and Discussion sections. It is unclear how this tool can make use of available good quality curated reconstructions as input.
