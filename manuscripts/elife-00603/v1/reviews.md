# Peer review - Round 1

Editors:
- Diethard Tautz, Max Planck Institute for Evolutionary Biology , Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.00603.030](https://doi.org/10.7554/eLife.00603.030)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for submitting your work entitled “Evolutionary principles of modular gene regulation in yeasts” for further consideration at eLife. Your article has been favorably evaluated by a Senior editor and two reviewers, one of whom is a member of the Board of Reviewing Editors.

The paper presents an excellent and carefully analyzed dataset dealing with principles of the evolution of transcriptional regulation. The paper has already been through one round of revision and has certainly been improved. [Editors’ note: the authors were encouraged to resubmit once the manuscript describing the Arboretum algorithm had been accepted, as it serves as a basis for the analysis in the current submission.] The data look very nice, with physiology-aligned sampling points based on growth phase and nutrient availability. They apply a recently developed algorithm called Arboretum to infer co-regulated gene modules and changes in gene module membership across the phylogenetic tree. An important aspect of the approach is the ability to infer ancestral states at internal nodes across the tree, allowing comparison of module composition in extant and ancestral species.

However, both reviewers felt that the interpretation of the results based on the Arboretum algorithm needs to be revisited. This may not require additional analysis, but a more self-critical discussion seems warranted that specifies the limitations of the current approach. The major points of the referees are:

1) The Arboretum algorithm requires that “…every gene (if present in that species) must be assigned to exactly one module”. This seems to be a very crucial point for much of the analysis. One would canonically expect that most genes have pleiotropic functions, i.e., could easily be part of more than one module. We understand that it is necessary to artificially restrict this to the best-supported module, but this can at the same time lead to problems in the conclusions. For example, changes of genes from one module to another could potentially be due to small probability shifts of assignment within the algorithm. It would therefore be important to know the second best assignments for these genes and how much the assignment probabilities differ from each other. Ideally a statistical test would need to be developed that would assess whether a shift was significant. It seems that adding more analysis and discussion of this point is a prerequisite for interpreting the observed shifts between modules.

2) A major drawback is that the Arboretum approach does not exploit the interesting temporal details. Only five modules are inferred, whereas by eye it is clear from Figures 3 and 4 that there are more than five expression patterns in each species, due to subtle (but likely important) temporal differences. Simply defining modules based on “strong” versus “mild” induction or repression, without subdividing modules by temporal patterns, does not provide a lot of resolution. Furthermore, the method “over-fits” the data by classifying genes into discrete bins without saying anything quantitative about the divergence in expression. For example, genes in Figure 7C look mildly induced to similar levels in Smik and Sbay, but the middle panel shows that the genes are classified into different modules in the two species. In the end, the module classification is discrete but doesn’t really quantify the divergence in expression very well. All this leaves the biological interpretation of these modules murky – surely there must be more than five regulatory systems across the life cycle of these species, and if so then what do these module groupings really reflect?

The Discussion is currently rather short and should be expanded to deal with the above points.
