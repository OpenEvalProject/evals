# Peer review - Round 1

Editors:
- Alex Fornito, https://ror.org/02bfwt286 Monash University Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79418.sa0](https://doi.org/10.7554/eLife.79418.sa0)

This important work develops new methods for aligning measures of brain-wide gene expression in the mouse and human brains. It presents compelling evidence in support of both conserved and species-specific transcriptional patterns. The work will be of interest to neuroscientists and geneticists interested in the molecular correlates of brain evolution.


---

# Peer review - Round 1

Editors:
- Alex Fornito, https://ror.org/02bfwt286 Monash University Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79418.sa1](https://doi.org/10.7554/eLife.79418.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Whole-brain comparison of rodent and human brains using spatial transcriptomics" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Kate Wassum as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Bratislav Misic (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Each of the Reviewers has raised some specific points that require further attention or analysis in their public review and recommendations for authors. Please provide a point-by-point response to each of these. We especially ask that you well address Reviewer 1 recommendations to authors points 2 and 3.

In your revision, If you have not already done so, please ensure your manuscript complies with the eLife policies for statistical reporting: https://reviewer.elifesciences.org/author-guide/full "Report exact p-values wherever possible alongside the summary statistics and 95% confidence intervals. These should be reported for all key questions and not only when the p-value is less than 0.05."

Reviewer #1 (Recommendations for the authors):

From the methodological point of view, this study is well-executed and the specific questions/suggestions are presented below.

1. Expression patterns across broad anatomical divisions such as the human cortex, subcortex, brainstem, and cerebellum demonstrate substantial differences. Similar tendencies are also observed in the mouse brain, where differences between neocortical and other brain areas tend to be much stronger compared to the differences within these divisions. The analyses presented in this work are performed on the combined datasets covering the whole brain and the resulting similarity metrics appear to be significantly skewed to the right with values broadly ranging from 0.7-1. Could the authors please comment if these transcriptional differences between broad anatomical divisions may attenuate/diminish the potential differences within these structures, e.g. within cortex/neocortex/subcortex/cerebellum? It might be interesting to expand the analyses by analyzing each anatomical division independently in order to disentangle more subtle transcriptional similarities/differences between species.

2. Currently, in the description of the processing of AHBA data there is no mention of within-donor normalization prior to data aggregation. It has been previously shown that samples acquired from the same donor tend to cluster together rather than reflecting anatomical divisions of the brain when samples across 6 brains are combined. Based on the current documentation, samples from all 6 brains are first aggregated into a sample x gene matrix and only then normalized for every gene across samples. This type of normalization retains expression differences between different donor brains and can bias the resulting sample x gene and region x gene datasets as well as subsequent analyses. Markello et al., (2021) have recently shown that within-donor data normalization is the most influential step in AHBA data processing, therefore, I suggest revisiting this data processing step. Also, could the authors comment on the choice of mean expression level subtraction for within-sample/region normalization rather than the standard z-score normalization?

3. Does the latent gene space method allows the identification of genes that are most informative in region identification? Could the authors provide some comments in the manuscript?

4. Some formal statistical evaluations should be presented when performing comparisons. For example, but not limited to, comparing maximal correlational values between sensimotor and supramodal areas (lines 277-280, Figure 5B).

References

Markello, R. D., Arnatkeviciute, A., Poline, J.-B., Fulcher, B. D., Fornito, A., and Misic, B. (2021). Standardizing workflows in imaging transcriptomics with the abagen toolbox. eLife, 10, e72129. https://doi.org/10.7554/eLife.72129

Reviewer #2 (Recommendations for the authors):

I think the manuscript is very polished as-is. I have a number of questions/suggestions that should be considered optional:

1) Line 61: "the connections of a brain region tend to be unique". I know exactly what the authors mean (each brain region has a unique/specific connectivity profile), but the sentence could perhaps be clearer.

2) Why use a multi-layer perceptron to map homologues, as opposed to a more interpretable, SVD-based method, such as PLS or CCA?

3) It is still not entirely clear to me how well the perceptron performs in the more conventional, global sense – is there a final, cross-validated accuracy? Is this accuracy significantly greater than what would be expected by chance?

4) In most of the analyses, there is a clear distinction between the cortex and cerebellum, which should then be expected to drive the configuration of the latent spaces. Have the authors attempted to perform the analysis using cortex only?

5) Do the authors have a sense of what biological pathways the homologous genes are involved in?
