# Peer review - Round 1

Editors:
- Nir Ben-Tal, Tel Aviv University Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.31097.025](https://doi.org/10.7554/eLife.31097.025)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Integrative mapping of enzymatic pathways" for consideration by eLife. Your article has been favorably evaluated by Michael Marletta (Senior Editor) and three reviewers, one of whom, Nir Ben-Tal (Reviewer #1), is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The manuscript introduces a novel approach to enzyme annotation based on analyzing the enzyme within the context of its metabolic pathway. Structural information is utilized to enhance systems models. In particular, predictions of the substrates and products of the enzymes, as well as structural data (from experiment and prediction) are used within the framework of Monte Carlo search to assemble putative metabolic pathways. The most highly ranked pathway is considered as hypothesis, and experiments are designed to examine it.

The strength of this study is that it is an intuitive, well-fleshed out method. Structural prediction data from docking, which is not so strong on its own for functional prediction, is coupled to locations within a pathway, restricting the search space of possible solutions to chemically similar compounds in the pathway proximity of each other. There is also strong experimental evidence for parts of the pathway prediction in H. influenzae.

The weakness of this study is that the initial starting points to build these pathways seems vague, pathway models are not fully experimentally verified (although parts have strong evidence), and application on a larger (genome) scale is not discussed, where this would be incredibly useful. An assumption is made to start with genome organization to select the pathway members which is unexplained and should be backed up.

Opinion:

It is an interesting approach but because of several hype statements the reader ends up somewhat disappointed. The approach is validated on three well known and one novel pathway. This is very impressive both in the scope of work and in the conceptual completeness, but potentially misleading as the computational approaches clearly depend on the amount and quality of already existing information. From experimental structures cocrystallized with correct ligands that would help in virtual screening, to reliance on well understood biochemistry and on homology to already characterized enzymes this approach seems to be aiming for semi-automated reanalysis of already well characterized pathways rather than on annotations of novel, uncharacterized ones – which seems to be the stated motivation for this work. In this context the benchmarks and the "discovery" of L-gulonate catabolic pathway in H. influenzae (which seems to be already well annotated in public databases) are not very convincing. It is also a bit unclear what constitutes actual results of this paper, as significant elements of L-gulonate catabolic pathway discovery in H. influenzae were already published by the same authors in 2015. The authors should either rebrand their approach as aiming at cleaning and solving apparent inconsistencies in existing annotations, or come up with more convincing examples of discovery and annotations of genuinely novel functions/pathways. Such examples would provide more realistic evaluation of the proposed approach. In summary: The main text should make it clearer as to what the immediate application is. Is this method currently limited to filling in parts of a pathway, or is it feasible to now try reconstructing entire cells from "bags" of proteins and metabolites? If the latter, suitable examples should be presented.

Major issues:

1) Assuming that the examples will not change, many statements should be tuned down, starting in the title and Abstract, to reflect the fact that: (a) the proposed approach can, at best, resolve conflicts in existing annotations rather than suggest new annotation, and (b) that even that requires a lot of manual interventions, as opposed to fully automated method.

2) The reasons for the data types chosen to be integrated over other potentially useful sources should be flashed. Reasons could include increasing the computational time, limitations of experimental data, etc.

3) Methods of picking the initial proteins should be explained, since that is a nebulous first step to get around before using this useful method.

4) Selecting based on proximity in genome organization is not backed up (subsection “Problem and approach”, last paragraph). Statistics or citations should be shown on known pathways if this is true. This is an important step to explain because it seems like it may ignore many enzymes which are not in the genome neighborhood. In eukaryotic organisms this does not seem to be nearly as applicable as to prokaryotes.

5) Computational time is unknown, throughout the paper – estimated time to run all docking predictions, chemical similarity, binding site locating, MC sampling, etc. What is the bottleneck? Or main source of human time/input?

6) Is docking done only to one predicted active site in an enzyme? How reliable or comprehensive the binding site estimates used here are? How much does docking add over geometric + biochemical comparisons of active sites? Would it be sufficient to do that and compute similarity analyses of that, rather than running many docking simulations?

7) Discussion, first paragraph. There is additional related work of genome-scale metabolic reconstructions that include structural data:

- http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000938 – structural properties used in predicting drug off target pathways.

- https://bmcsystbiol.biomedcentral.com/articles/10.1186/s12918-016-0271-6 – structural properties used to compare lifestyles and pathway usage.

8) Figure 4E – what is the reason behind higher gene expression increases of UxuB, GulPQM, GulD on a D-mannonate carbon source compared to L-gulonate? Since these proteins are involved in L-gulonate transport and metabolism it would seem like they should be expressed higher on L-gulonate carbon source, not D-mannonate which comes after them in the proposed pathway.

9) What is the author's opinion on applying this method on a genome scale (i.e. entire metabolic network)? Is it feasible in terms of speed and data curation? Is it possible for the authors to generate genome-scale network predictions and compare them to available reconstructed metabolic models? These would be interesting questions to address in the main text.

10) How broadly applicable the approach is? How many new enzymes can be annotated this way?

11) The statement concerning the applicability of the method also to protein-protein interaction (PPI) networks is a bit of a stretch. For now, the essence of the method is docking of the metabolites to their binding/catalytic sites. In PPI this component will have to be replaced, and it is unclear with what. Protein-protein docking, the first possibility that comes to mind, is far less accurate, especially for transient interactions. I would eliminate the statement, or tune is down significantly.

12) Methods:a) The terms in the first equation should be defined.

b) Using the DOCK scores. Usually, in drug discovery campaigns, the docking scores are considered an indication for possible binding, but the actual values or ranks are often inaccurate. It is surprising that here they are taken as a given and nevertheless the pipeline works fine.
