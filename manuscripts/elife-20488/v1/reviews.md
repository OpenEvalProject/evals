# Peer review - Round 1

Editors:
- Nir Yosef, University of California , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.20488.033](https://doi.org/10.7554/eLife.20488.033)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Discovering sparse transcription factor codes for cell states and state transitions during development" for consideration by eLife. Your article has been favorably evaluated by Arup Chakraborty (Senior Editor) and three reviewers, one of whom, Nir Yosef (Reviewer #1), is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper presents an interesting framework for identification of lineage/ developmental relationships based on whole transcriptome profiles. The basic notion is that differentially expressed genes among triplets of samples (representing either a developmental fork or a linear developmental progression) should largely exhibit a prototypical pattern that reflects the lineage relationship. The authors successfully apply this to infer lineage relationship in hematopoiesis, using bulk- level RNA-seq. They then turn to apply their method to single cell data of early neuronal development, and concomitantly infer clusters of cells (each representing a developmental state), and their organization into a lineage structure. A subset of these results is followed up in another, yet unpublished manuscript. The algorithm was also used and followed up on in a companion manuscript of ESC differentiation.

Essential revisions:

Overall, this study is innovative and provides new insights into cell-type detection and lineage relationship. The method developed here is complementary to existing pseudotime inference methods in single-cell analysis and the paper is clearly written. Nonetheless, the paper may benefit from additional valuation of the method's performance, specifically – by applications to additional data sets and by systematic comparison with existing methods. More detailed descriptions of their methods is also merited, as described below.

1) "Lineage progression" triplets: In the case of cell type B that gives rise to cell type A that gives rise to cell type C the middle node (A) is chosen as the "root"

1.1) The terminology "root cell type" and "terminal leaf cell types" seems inappropriate and confusing in this case and should be revised.

1.2) The minimum-in-leaf model makes sense in the "Lineage progression" case as it captures the common scenario of genes that get turned on or off in a lineage path, with some persistence of this state. However, in such triplets that are distant enough along the path this may contradict the single "pulse" model (i.e., transient change) proposed in other studies. To explore this, Figure 1 should be revised. Currently it only shows the majority statistics. It would be important to see the fraction of genes that conform to the minimum-in-leaf model (which can be anywhere between 51% and 100%) while contrasting:

1.2.1) "Lineage progression" vs. "cell fate decision" triplets.

1.2.2) Triplets with leaves vs. triplets that only include internal nodes.

1.2.3) Triplets with different distance in the tree.

2) The Clear-minimum-in-leaf model.

2.1) To further support the validity of the minimum-in-leaf model, the latter extension to Figure 1 (comment 1.2) should also include comparison between all related triplets vs. all unrelated triplets (i.e., representatives from three different branches).

2.2) Subsection “Discovering sparse patterns correlated with lineage transitions”, third paragraph: There are more than 2 possible patterns for differentially expressed genes between 3 cell types. In addition to the clear minimum A<B=C and clear maximum A=B<C there is also A<B<C, which is actually what is expected for lateral inhibition, discussed in the text several times. This pattern of three clearly distinct expression levels is not discussed at all in the text (in fact, it is excluded from the model, as described in subsection “1. Notation; Bayes’ Rule”, first paragraph). A clear example is HLF, mentioned in the text as higher in MPP compared to CMP, but it is much higher in the third member of the discussed triplet, ST (according to ImmGen skyline browser).

2.3) The B&T subtree used for the observation has a very simple topology of only two branches. That might limit the generality of the conclusion. Indeed, the reconstructed lineage tree of the progenitors include a loop, which is not supported by the literature. Authors should discuss this difference from known tree topology. Also, why did they use their approach to reconstruct only hematopoietic progenitors and not all ~250 ImmGen populations?

3) First algorithm.

3.1) For the formula in the third paragraph of the subsection “Using patterns to infer lineages”, but I wonder how to draw a cutoff for a tree to be 'correct'. If the method is applied to unrelated cell-types, what is distribution of the p-values?

3.2) How robust is the lineage prediction model to the initialization procedure and parameter choices? For example, how sensitive is the resulting tree on the number of initial clusters? how sensitive are the results for the algorithm's parameters (e.g., probability cutoffs) or for sub-sampling of samples or genes? A similar stability analysis should also be included for the second algorithm (extension to single cells), which can be even more sensitive due to its iterative nature.

4) Application to hematopoiesis:

4.1) It is not clear how well the algorithm can separate related from unrelated triplets? (i.e., representatives from three different branches). While this is mentioned anecdotally in Figure 2, it should be evaluated systematically, e.g., with AUROC.

4.2) Given the constraints of the algorithm, the aggregated lineage tree is undirected. While this is mentioned briefly, this key point should be better clarified in the main text.

5) Algorithm's extension to single cells.

5.1) Comparison to other methods.

Recently a number of papers have been published to infer cell lineages from single-cell gene expression data, such as Monocole (Trapnell et al. NBT, 2014), Treutlein et al. (Nature 2014), Wishbone (Setty, Nature Biotech, 2016), tSCAN (Ji, NAR, 2016), StemID (Grun, Cell Stem Cell 2016), and diffusion map (Haghverdi, Nature Methods, 2016). It will be useful to compare with these methods at least to get a sense to what degree this method provides new information (note: it looks like Figure 4B comes from Monocole, but we could not find a mention for it in the Results section).

5.2) Differential expression in single cells.

The t-test used to identify clear minimum and clear maximum patterns is appropriate for microarray analysis, but one limitation of t-test is it assumes the underlying distribution is normal, which is not true for RNAseq, and especially single-cell RNA-seq data. Specifically, single-cell RNA-seq can be severely under-powered because many genes (especially transcription factors) have low or even zero expression values due to dropout. Please discuss ways to incorporate more sophisticated tests that addresses this challenge (e.g., as in scDE), or demonstrate why this is not needed.

5.3) Related to that – the threshold used for definition of a pattern is p<0.005 in a two sample t-test. Though not specified by the authors, it seems that as there are 1500 transcription factors tested, and 3 tests performed per gene (to test the separation of each of the 3 triplet members from the other two), 4500 tests were performed per triplet. Thus, one would expect to find 22 transcription factors (4500*0.005) with a pattern that pass this threshold for each triplet in the absence of a signal. The authors have to address the multiple comparisons issue.

6) Application on Single cell data

6.1) While the single-cell data comes from another manuscript that is under review elsewhere; the information provided on this data is insufficient.

6.1.1) Please provide a compete "census" of the data – how many cells from each condition; how many reads per library, which read lengths were used?

6.1.2) How was the data processed? Should we worry about potential confounders of library quality (which have been presented and discussed time and again in the recent scRNA-seq literature)?

6.2) The algorithm should have been demonstrated first on a single cell RNA-seq datasets where the true cell type transitions tree is known, such as one of the publicly available hematopoietic progenitors single cell RNA-seq datasets.

6.3) There is no estimate of how sparse is the resulting code – how many genes can be used to decipher the topology? Can they be identified ahead? Is it possible that any group of genes of similar size (~1500) can code for cell states and cell transitions with the same success as the transcription factors?

6.4) It is not clear how the tree was generated. Was it using the generic algorithm from the previous section, or by enforcing the temporal order of the samples? If it is the latter – please describe the procedure and explain why the generic algorithm does not work.
