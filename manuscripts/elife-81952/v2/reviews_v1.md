# Peer review - Round 1

Editors:
- Kellie N Smith, https://ror.org/00za53h95 The Johns Hopkins University School of Medicine Baltimore United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81952.sa0](https://doi.org/10.7554/eLife.81952.sa0)

In this valuable and important study, the authors use cancer immunology datasets to study and discover a new biomarker for immune checkpoint blockade response. Not only does this work have the potential to be clinically impactful, but it also provides a deeper understanding of basic biology that can be applied to many different disease settings, and is supported by solid evidence.


---

# Peer review - Round 1

Editors:
- Kellie N Smith, https://ror.org/00za53h95 The Johns Hopkins University School of Medicine Baltimore United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81952.sa1](https://doi.org/10.7554/eLife.81952.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "T cell receptor convergence is an indicator of antigen-specific T cell response in cancer immunotherapies" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Tadatsugu Taniguchi as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) In Figure 1D, use true healthy controls rather than COVID-19 subjects (I.e. the CMV dataset from Adaptive) unless there is good and substantial reason not to

2) Make all suggested changes regarding clarity (including confirming cluster IDs), and better contextualize the findings in relation to prior work.

Reviewer #1 (Recommendations for the authors):

The analysis is straightforward, yet generated really interesting results. I would recommend minor revisions before accepting it.

I have several questions that need the authors to clarify or provide more explanation.

1. In Figure 1 —figure supplement 1A, why after reaching 17 amino acids, did the degeneracy remain constant? The authors should discuss this in the Discussion section.

2. The scRNA-seq-based analysis is interesting. However, in Figure 3B, the recluster of CD8 T cells is not that different from Figure 3A. However, the convergent cells are in a totally different cluster. Are there any mislabeled clusters?

3. Why do CD4 T cells have very few degenerative clones? The authors should discuss this in the Discussion section.

Reviewer #2 (Recommendations for the authors):

Given the authors' track record of predicting cancer vs non-cancer using TCR repertoire, it will be interesting to investigate if and how TCR convergence can be used as an early-stage cancer biomarker.

There are a few suggestions to improve the scientific rigor and accessibility of this work:

1. In figure 1D, the author used COVID-19 patients' samples to represent non-Cancer patients. However, the inflammatory responses between COVID-19 patients and healthy individuals are expectedly different. It will be necessary to have true healthy donors as control.

2. In figure 3D, the author used a human dataset derived from multiple previous study cohorts. Convergent T cells were also sparsely distributed in cluster 01 and cluster 05. Since the cited dataset was a meta-analysis, it might be possible that some of these T cells may exhibit a 'tighter' distribution in a single cohort. It will be worthwhile to explore if the non-cluster-04 convergent T cells are enriched for other T cell phenotypes.

3. This study will benefit from more human datasets with neoantigen-specific T cells, both to verify the antigen-specificity of the convergent TCRs and to find out the types of antigens (viral or tumor antigens) that convergent TCR can recognize.

4. In the analysis of ICB response prediction (Figure 4), it will be interesting to investigate if there are similar or shared convergent TCRs across the responders. If so, these TCRs could be more direct predictors of immunotherapy outcome, although, given the large diversity of the antigen repertoire, this commonality might not be seen.

5. The authors should distribute an open-source package or script for users to easily analyze convergent TCRs.

Reviewer #3 (Recommendations for the authors):

Figure 1 typo: "covergence".

I think this may be a typo: "As antigen-specific T cells play a crucial role in defending tumor cells".

The definition of public TCRs needs to be justified: "Each of these cohorts was mixed with the 666 samples from the Emerson cohort(37) to form new cohorts with sample sizes of 716, 685, 711, 719, 716, and 695. The TCR sequences shared by at least 5% of different individuals within a cohort were defined as the public TCRs of that cohort." Assuming the "cohort" at the end of this sentence is the merged cohort, this seems like it could create artifacts due to the sizes/depths of the different cohorts, and therefore their contribution to their respective "merged" cohorts.

"starting with cysteine and ending with phenylalanine" Note that there is a common allelic variant (TRBJ2-7*02) that ends with a V.

The zenodo dataset file is in.rar format. It would be nice if a more standard format like.zip or.tgz could be used, given that there doesn't seem to be a public compression utility that understands rar files.

When contrasting convergent TCRs with sequence clustering approaches, the authors state "Nevertheless, the fact that T cells within each TCR convergent cluster share the same TCR amino acid sequence guarantees perfect antigen-specificity". For single-chain data, this isn't the case, since the paired chains could be different. So similarity and identity at the amino acid level are not really all that different.
