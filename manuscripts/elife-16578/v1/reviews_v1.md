# Peer review - Round 1

Editors:
- Richard A Neher, Max Planck Institute for Developmental Biology , Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.16578.045](https://doi.org/10.7554/eLife.16578.045)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Lineage Tracing of Human B Cells Reveals the in vivo Landscape of Human Antibody Class Switching" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Arup Chakraborty as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The manuscript uses sequencing reads of the variable region and parts of the surrounding constant region of immunoglobulin heavy chains to investigate the dynamics of class switch recombination (CSR) in humans. The data are used to infer the relative rates of all possible class switch events. The authors further demonstrate that class switch recombination is correlated within clonal B cell lineages and that this correlation decreases with increasing distance of the variable part of the sequence. All reviewers agreed that these are interesting results addressing an important question. However, we identified various points that require further discussion or additional analysis.

Essential revisions:

1) It is not clear how errors were corrected using the molecular barcodes. You state that you obtained ~261k reads per sample which typically represented 170k distinct molecules (subsection “Antibody Repertoire Sequencing with Subclass Resolution”, first paragraph). This would suggest that most barcodes are represented only once and no consensus sequence of (>=3 sequences) can be computed. Did you use singleton and doubleton barcodes as Figure 1—figure supplement 1A suggests? If so, sequencing errors likely contribute to diversity in many of the clonal clusters (the inserts are quite long and the end of the 2nd read often has low sequencing quality, hence sequencing errors are a concern).

While it seems plausible that errors rarely produce sequences that have different classes, sequencing errors can produce additional sequences that are more similar to a sequence of a different class and hence inflate CSR rate estimates. This should be clarified and the analysis should be carefully controlled for the influence of sequencing errors. Ideally, only proper consensus variants should be used.

2) The authors have opted for a custom analysis pipeline using minimal spanning trees instead of phylogenetic reconstruction and probabilistic models of class switching. The analysis doesn't account for the possibility of unsampled ancestors and it is not clear how the assumption that all ancestors are sampled influences the inference of CSR events. The problem of unsampled ancestors is well known when reconstructing transmission histories of viruses (e.g. http://dx.doi.org/10.1371/journal.pcbi.1003397). The authors performed a number of analysis to validate the CSR inference (presented in Figure 2—figure supplement 1: restriction to identical VDJs, rarefaction analysis), but some concerns remain. A combination of a Z -> X and a Z -> Y transition with an unsampled Z will be misinterpreted as an X -> Y transition, regardless of whether X and Y are separated by somatic mutations or not. For transitions with a small number of counts, a few such instances could contribute substantially. The rarefaction analysis is not informative for transitions with small rates and few counts.

The authors should either provide additional analyses that address these concerns, or state the limitations of their rate inference explicitly.

3) You claim that class switching landscapes of identical twins are not identical, but are they significantly more different than those inferred from biological replicates? If not, the section heading "Identical Twins Do Not Share Identical Class Switching Landscapes" is misleading.

4) The analysis of concordant class switch events on subtrees of two parents with a common ancestor in the same state which go on to produce progeny of different classes is elegant, but we would like to see an additional control: Is the distance between children to parents correlated with that of parents to the common progenitor? Such correlations could arise due to differential sampling of lineages. In this case, similarities in switching might be due to similar distances of parents to children. In other words: Are the length of branches associated with particular switching events? And if so, are branch length of sisters correlated? This can be readily checked.

We would also like you to clarify whether you can conclude that there is a cell specific state that favors specific CSR events, or whether the observed correlation between closely related cells can be explained by an overall variation of in the switching rate, which will mostly result in switches to the same state. An analysis of the conditional probabilities of switching, given the switch of the sister (as mentioned in the subsection “Analysis of Correlations in Class Switch Fates among Related Cells”) could address this. More detail on how Yule's Q is calculated should be given and its meaning briefly explained in the main text.

5) Analysis scripts, code, and data need to be made publicly available. Ideally, documented scripts (the authors used python, iPython notebooks might be an option) along with preprocessed data should be provided. In particular, in the light of possible improvements of the analysis, preprocessed data sets that facilitate analysis by others would be welcome. Raw data needs to be deposited in short read archives.

6) The caption of Figure 2—figure supplement 1B refers to Figure 2A, but Figure 2A doesn't contain similar matrices. The caption of Figure 2—figure supplement 2A refers to pies and colored slices, but all pies are mono-chrome. eLife has no limit on the number of figures. We suggest reorganizing the supplementary figures into smaller more coherent units. The current multi-panel figures with very small print and long captions are not helpful.
