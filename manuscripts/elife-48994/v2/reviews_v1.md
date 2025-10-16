# Peer review - Round 1

Editors:
- Alex K Shalek, Broad Institute of MIT and Harvard United States

Reviewers:
- Itai Yanai, United States

## Review text

DOI: [10.7554/eLife.48994.125](https://doi.org/10.7554/eLife.48994.125)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Self-assembling manifolds in single-cell RNA sequencing data" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Alex K. Shalek as the Reviewing Editor and Naama Barkai as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Itai Yanai (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Tarashansky et al. detail a computational algorithm called SAM (Self-Assembling Manifold) that helps to identify meaningful clusters within single-cell RNA-Seq data. SAM iteratively re-weights gene expression by importance (as determined by variation across neighborhoods rather than individual cells) until convergence; the resulting nearest neighbor graph is then used for clustering, and gene weights can be used to indicate biological significance. The authors benchmark SAM using previously published data as well as a self-generated Schistosoma dataset that had proven difficult to cluster using existing methods. Overall, the manuscript is well written and the algorithm has the potential to be impactful.

Essential revisions:

• The authors should provide better documentation on SAM to make the scripts more understandable to a general audience and aid in its application to new datasets. Specific guidelines on the selection of variable parameters (e.g., SAM weight cutoffs; illustrated through the presented examples) are particularly important, as is examination of the extent to which SAM is confounded by integrating data across batches and methods. More example applications should be included in the documentation, as well as in-depth function descriptions.

• A more comprehensive analysis of the parameter space for some of the existing methods (e.g., Seurat) should be performed to properly benchmark SAM. Utilizing data for which ground truth is known could be particularly illuminating. The authors should also discuss under what conditions SAM performs well to help guide its implementation.
