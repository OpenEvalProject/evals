# Peer review - Round 1

Editors:
- Eduardo Eyras, https://ror.org/019wvm592 Australian National University Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73520.sa0](https://doi.org/10.7554/eLife.73520.sa0)

This paper presents a new method to study known and novel alternative splicing events at the single-cell level and perform differential analysis across cell types. The method addresses current challenges in the analysis of splicing in single cells related to technical variation and experimental biases. Performing one of the most comprehensive studies to date with data from different mice, this work expands the body of splicing events that potentially define individual cell types.


---

# Peer review - Round 1

Editors:
- Eduardo Eyras, https://ror.org/019wvm592 Australian National University Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73520.sa1](https://doi.org/10.7554/eLife.73520.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Robust and annotation-free analysis of alternative splicing across diverse cell types in mice" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and it was agreed that a resubmission that fully addresses all of the concerns raised would be suitable for further consideration for publication in eLife. The Reviewing Editor has drafted the following to help you prepare a revised submission.

Essential revisions:

The reviewers have indicated that although the work might be of interest to researchers working in alternative splicing, the method requires significant additional testing and benchmarking, and the novelty of the findings must be made more clear. The reviewers have provided multiple suggestions to improve this and other aspects of the manuscript.

Reviewer #1 (Recommendations for the authors):

Authors have applied their method to two big scRNA-Seq datasets and have reported multiple biological discoveries from their computational analysis. However, the presentation and validation of the results should be improved. I elaborate on my comments below:

One of my major concerns is about the evaluation and benchmarking analysis of scQuint. Authors have particularly reviewed some of the existing methods in the appendix, but they provided no comparison between the performance of scQuint and those methods. Particularly authors have mentioned on page 18 that they have previously analyzed these datasets with prior methods, but they did not provide any comparison between their findings and those by other methods. In its current form, it is extremely difficult to judge the sensitivity and specificity of scQuint or whether it is a new contribution to the field. Thus, the paper's contribution is to run a standard, published analysis on a single cell dataset. There is no functional or experimental validation to support or refute the findings. Further, there is no computational validation, in terms of testing whether the predictions in this dataset hold in other data.

One limitation of the current method is more statistical tests which could lower the statistical power due to multiple hypothesis testing issue, as it needs to perform a separate test for each pair of gene/cell type compared to a test for each gene that some other methods need for finding "genes" with cell-type-specific splicing.

Authors have used the same model as in leafcutter for their analysis. However, they claim that they are getting better p-value and clustering results compared to leafcutter. It is not clear why their method should perform better than leafcutter.

One of the major advantages of the tabula muris dataset is that it contains data from multiple mouse individuals (i.e., biological replicates), which can be leveraged to show the reproducibility of the biological findings across biological replicates. However, authors did not take advantage of this in presenting their results. I highly recommend that authors show that their results can be replicated across mouse individuals, by visualizing their results as stratified by donor ID. Reproducibility is important for distinguishing between a real reproducible biological signal and a biological/technical noise particularly for the unannotated splicing events as they might be a product of splicing noise.

Authors have applied their method to only SS2 and not to any 10x data. I believe that the tabula muris dataset contains 10x data as well. While I agree that 10x is more challenging than SS2 for splicing analysis, it is still a valuable resource for splicing analysis as it has higher throughput compared to SS2 and can better capture rare cell types. I recommend that authors comment on the applicability of their method to 10x in the paper and, if their method is applicable, show how their current results compare to the results based on 10x data.

Since the paper is about analyzing splicing in single cells, I think it is extremely valuable to show the variation at the "single-cell level" (rather than pseudobulked cell-type level) via box or violin plots. This is extremely important as it is not clear from the current plots (e.g., figure 5 c,d,e or figure 8c,d) that the splicing event was observed in how many cells in each cell type and what is the range of read counts per single cell in each cell type. As I mentioned earlier it is extremely difficult to judge the reproducibility and single-cell variation of the visualized splicing events in figures as the data is aggregated across all cells within the cell type from separate donors.

Authors mention that there is little overlap between differentially expressed and differentially spliced genes but on the other hand they say that the clusters based on splicing and expression latent space are highly consistent with each other. I think they should comment on why this is possible, is it because the same cluster has different markers in each space. If so, is it possible to highlight a few clusters and show their marker genes based on splicing and expression changes?

On page 9, authors say that they detected thousands of cell-type-specific events; however, they do not provide more specifics about these events? How many events exactly? Across how many distinct genes (also what fraction of genes, and is this fraction with previous studies?)? And distinct cell types? Also, it is not clear how the examples in figure 5 were chosen? Are they among the top genes? What are the top genes? Are they genes known to have cell-type-specific splicing?

The paper lacks any experimental validation on the discovered splicing events. It is extremely important to show through experimental/FISH validations that these events are not computational artifacts and can be detected in the cell types.

It is not clear how (and how many?) splicing events in B cell trajectory were identified. Do you report any event that is differential in any of the B cell states as a cell with alternative splicing in B cell trajectory? And again, how these examples were chosen are they among the top genes in B cell trajectory?

Authors say that they detected many more events in cortex and also higher fraction of unannotated events in cortex, is this because cortex has been more deeply sampled compared to other tissues (Table 2)? Authors should account for sampling depth differences between cell types to see which one is really more enriched in alternative splicing events.

For Figure 9C, what is the AUC if the model is trained on one individual and used for prediction on another mouse?

Is not the higher fraction of events in 5' UTRs vs 3' UTR a result of the bias in your method? As you only consider events with shared 3' SS and not events with shared 5' sites in your analysis?

How did authors account for the coverage-dependent bias (as reported in https://elifesciences.org/articles/54603) which could cause spurious splicing bimodality in scRNA-Seq?

Reviewer #2 (Recommendations for the authors):

To demonstrate the significance of the approach a more completed performance evaluation, for example, using synthetic data, is recommended, as well as a comparison to alternative methods regarding biological significance.
