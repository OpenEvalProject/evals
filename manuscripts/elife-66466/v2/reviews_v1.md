# Peer review - Round 1

Editors:
- Alex Fornito, Monash University Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66466.sa1](https://doi.org/10.7554/eLife.66466.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper makes an important contribution to understanding human brain development and will be of note to readers with a particular interest in subcortical anatomy. The work sheds new light on principles of subcortical maturation and its genetic mechanisms.

Decision letter after peer review:

Thank you for submitting your article "The genetic organization of longitudinal subcortical volumetric change is stable throughout the lifespan" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Tamar Makin as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

The Reviewers were all enthusiastic about the potential of the paper, but had a number of methodological concerns that will be important to address. We would be happy to consider a revision provided that you are able to comprehensively address all the points raised.

Essential revisions:

1. The analysis includes data from a wide age range spanning 4 to 88 years. T1 signal characteristics, particularly those affecting tissue contrast, can change significantly over this time. This will have an impact on the accuracy of any automated segmentation algorithm. How can we be sure that age-related differences are not simply due to variations in tissue contrast? This problem is compounded by the reliance on the Freesurfer aseg algorithm, which parcellates the brain using an adult training set. Thus, not only will there be a problem of age-related differences in tissue contrast, but also in the accuracy with which individual T1s can be spatially aligned to the template, which is likely to decline as a function of age difference from the young adults used to generate the templates/training set. The authors should demonstrate that such effects cannot explain their findings.

2. The authors conclude that "at a general level, change in the structures tended to cluster according to trends from embryonic development and placement along the cranial vertical axis, but with notable exceptions.". This is based on the unsupervised clustering solution from correlating inter individual variation in change for each structure (which they argue is reproduced in development aging and genetic analyses – see point 2 below). Looking at their clustering solution though, a more superficial explanation could easily explain the 3 main clusters they observe: Cluster 1 = fluid-filled ventricles, Cluster 2 = White matter (or white matter rich for thalamus, hippocampus and cerebellar cortex) ROIs, Cluster 3 = Most other ROIs, which are general non-white matter rich cortical or subcortical nuclei. I understand that linkage to embryological patterning is more profound – but there must be some effort to address the more concrete possibility that the clustering is basically saying CSF goes with CSF, white with white, and gray with gray (put crudely). Although thalamus, hippocampus and cerebellar cortex are classed as gray by tissue classification algorithms – it is well recognized that these structures also contain substantial white matter components. We suggest comparing mean MT or FA for Clusters 1 and 2 to get at this empirically. Evidence for the "tissue composition" hypothesis for clustering is not incompatible with the "embryological origins" hypothesis – but focusing on the latter to the extent that the authors do would be more justified if there were not evidence of the former.

3. The authors conclude that their findings show "substantial coherence in the pattern of change between development and the rest of the life". This major finding is based mainly on the cross-cell correlations and Mantel tests for compare different correlation matrices: (i) correlated intra-individual changes in development, (ii) correlated changes in adult/aging, (iii) genetic correlation in change, and (iv) SNP-based estimated of co-heritability. The dominant signal by far within any one of these matrices, and the main signal that appears to be recovered across matrices is the contrast between ventricular measures and non-ventricular measures. The reproducibility of this contrast is less meaningful than the reproducibility e.g. based on correlation across all non-ventricle edges between matrices. First and foremost, a fundamental issue with giving equal weight to ventricular vs. non-ventricular measures in their contribution to statements of similarity between matrices is that the ventricles are a single continuous fluid filled cavity, so that saying – eg lateral and lateral inf ventricles are correlated is considerably different from saying amygdala and thalamus are. Compounding this concern is that the weight given the ventricle-related edges in driving cross-matrix correspondences is somewhat arbitrarily defined by how many parts you want to chop the ventricles into. This level of arbitrariness does not apply for example for the distinction between the other main ROIs included. To address these issues, the cross-edge correlation between matrices should be presented and probed through scatterplots. Scatterplots for these edge-wise correlations between matrices should lay out the issue (using edge here to mean cell in the matrix). The ~0.8 value is likely to be inflated by dense point of edges to the top right and bottom left of the plot relating to inter ventricular edges and ventricle-nonCSF edges respectively. These scatterplots between matrices should be visualized with all edges, then with just the edges that do not include ventricles. The correlation should be recalculated for the latter, and a fit line shown to help readers identify those edges that show weakest correspondence between matrices. A v efficient way of looking at the sensitivity tests above is constructing a symmetric 5*5 matrix – each column/row is a matrix from Figures 2 and 4. The cells show inter-matrix correlations. Show this one with ventricles in, and once with them out. The core issue here is showing that the signals being discussed and interpreted aren't overly dependent in the simple contrast between tissue and non-tissue compartments.

4. The Mantel test is likely biased in the case of spatially autocorrelated data (Guillot and Rousset, 2013, Methods in Ecol and Evol). The authors should consider generating spatially constrained null models (e.g., Alexander-Bloch et al. NeuroImage, 2018; Burt et al. NeuroImage, 2020) for inference on the Mantel test.

5. It may be, in part, due to how you phrase some points but you seem to suggest that volumetric correlation is analogous to volumetric change correlation, which is not supported by the analyses you perform. The fact that the matrices of correlations between volume and volume change resemble each other does not prove they are driven by similar (genetic) factors. You would need to evaluate correlation between volume and volumetric change, in particular at a genetic level to support this claim. Here is a selection of the sentences I found misleading or problematic:

This was confirmed by single nucleotide polymorphisms-based analyses of 38127 cross-sectional MRIs.

Importantly, both the structure and the coordinated change of each cluster tended to be governed by common sets of genes

This means that regions that develop and change together through life tend to be governed by the same sets of genes

Rather, genetic influence on change rates and baseline volume overlapped for most structures. This finding allowed us to use cross-sectional data from UKB to further explore the genetic contribution to subcortical organization.

The similarity of the developmental change matrix and the SNP genetic correlation matrix obtained from middle-aged adults thus yielded further support for the hypotheses that genetically governed neurodevelopmental processes can be traced in subcortical structures through life.

6. You also seem to assume that the clusters defined from pairwise correlations would consist in homogeneous regions (e.g. with common genetics or determinants). I would argue that this is not necessarily the case, and it could be investigated at a genetic level using multivariate twin models (e.g. common pathway model).

7. I would find useful that you highlight the significant phenotypic and genetic correlations (e.g. in Figure 2 and 4). For example, I would find a cluster consisting of significant correlations more convincing. On the other hand, a significant positive correlation between clusters would suggest that the clusters are not independent, which is also interesting.

8. In my opinion, the description of age trajectories, albeit extremely interesting, are not central to the scientific question you are trying to tackle. I think it would improve readability to present them after the main results in the same section as the cluster trajectories. In particular, reading the result section led me to think that GAMM were central to your analysis, while they are only used for a visualisation of the age trajectories, which only serves a descriptive purpose.

9. More generally, the result section would benefit from being more linear (starting from the main results) and/or would benefit from a better correspondence between the figures and the text. At the moment, it feels like the figures and text have different progressions all together, which is confusing. For example, the results presented in Figure 2 are spread in different sections of the text that are not even following each other. Figure 4 would make sense near Figure 2, or even as an additional panel of Figure 2. An example of what I think would be a more linear progression of the results.

o E.g. Phenotypic correlations/clusters.

o Replication in adults.

o Sensitivity analysis.

o Genetic correlations clusters.

o Relationship with embryonic development.

o Visualisation of age trajectories of regions and clusters.

o Additional analyses (e.g. cognition).

10. Modularity analysis – There does not appear to be any assessment of the statistical significance of the cluster solution. This could be done by shuffling the correlation matrix using appropriate algorithms, depending on the degree to which the authors want to consider spatial effects in the data (e.g., Roberts et al. 2015, NeuroImage; Rubinov and Sporns, NeuroImage, 2011).

11. Modularity analysis – it appears the authors used a standard implementation of the Louvain algorithm. The default definition of Q defines a null expectation for within-cluster connectivity that is not appropriate for correlation matrices. With such data, the mean correlation can be appropriate.

12. Modularity analysis – the evaluation of different levels of γ is commendable. It is unclear why this is left to the end of the Results. This should either be placed at the beginning, as a way of justifying the 5-cluster solution, or the beginning should indicate what value of γ was used initially and contain a reference to subsequent analyses that investigate the issue of γ in more detail.

13. The similarity between the clusters and developmental origins is qualitative. Given that this is a core aim of the analysis, perhaps the authors could perform some inference by shuffling the labels and using a measure of partition similarity such as their normalized mutual information?

14. Please explain why the cortex is treated as a single structure? Cortical development is regionally heterogeneous.

15. Sex is known to modify trajectory shape for cortical and subcortical structures. It would be good to show that the observed clustering holds for male and female subsamples. This would provide an important sensitivity analysis and also potential evidence for a sort of split half reliability.

16. It would also be important to show how ROIs cluster when you use the first derivatives from the gam fits in Figure 1. That would provide a complimentary approach to the inter-individual change method on which current work is built, and also help unpack some of the potential concerns re "fluid vs. tissue" and "white right vs. other" as two big potential drivers for findings. I would add plots for the ventricular components in Figure 1 too, as well as dendrograms for the primary heat map clustering used to order other matrices. My guess would be split one is CSF vs. tissue, and split 2 is white/white-rich tissue vs. other tissue.

17. In estimating APCs – how did the authors deal with were people with more than 2 scans, and the potential for including mid-scan age as a factor before correlating given the non-linear volume changes in development?

18. I may have missed it but I did not expect the analysis of cognitive function. What purpose it is serving and does it really integrate in the theory of neurodevelopment? In addition, only one association seems significant after multiple testing and the difference seems to be localised in the 25-60 years old group for which you have the fewest observations (from Figure 1). Could this be due to a handful of outliers? Could you also add precision about which test was used? Maybe reporting several curves for difference quantiles of the distribution (instead of above/below average) would help visualise the effect?

19. Figures 4 and 5 need a color scale.

20. Figure 2 is the main figure of result and I strongly suggest you expand the caption to improve self-readability. For example, the fact that the first row are results obtained on the LCBC sample. Clarify that the clustering was not recalculated for each matrix but is that of the first panel. In addition, the titles of the correlation plots could be clearer (e.g. clearly stating phenotypic and genetic correlations). Also the 4th panel is not a volumetric change-change relationship, which is the title of the figure.

21. Abstract and introduction should announce that the focus is about volume of subcortical structures.

22. The discussion reads well but contains many statements that do not seem supported by the results or that sounded too definitive considering the analysis only focused on 16 volumetric measurements. It also lacks a limitation section.

23. Some aspects of the text could be clearer. For example:

Line 44 – it is unclear what the hypothesis is precisely.

Line 59 – what does a topographic organization correspond to in this context? regionally specific?

Line 61 – it is unclear what it means to follow the "genetic organization of the cortex".

Line 79 – it is very hard to understand what this hypothesis refers to and what it predicts.

Line 88 – it is unclear what a genetic anatomical architecture is.

Line 105 – please clarify: was the correlation across subjects?

Line 121 – it is unclear what "common factors" refers to here.

Line 217 – only a correlation rather than prediction has been shown.

Line 256 – please clarify: was consensus clustering run over 1000 runs at each γ?

“Although the lifespan trajectories of subcortical structures are much more divergent than those for cortical regions.”

Unclear to me how this is supported by results from the article, could you expand on how you conclude this?

“Mapping the developmental clusters to the adult part of the sample yielded highly different change trajectories.”

Here it may help to cite figures and tables in Discussion – also is this the case for all clusters?

“Clusters 1, 3 and to a lesser extent 4 were related to general cognitive function in a mostly age-invariant manner, which implies that the relationship between cognitive function and subcortical volumes is established early in life.”

This sounds like a huge overstatement. You studied only volume change of 16 regions – and the associations with cognition scores are not the most convincing.

“This means that regions that develop and change together through life tend to be governed by the same sets of genes.”

Beyond my previous criticism, this reads as a rather large generality.

“…and are governed by distinct sets of genes.”

What is this conclusion based on?

“It has also been argued that genes expressed in the subcortex generally are more region-specific and tend to evolve more rapidly than genes expressed in cortical regions”.

I am not sure what you mean by "evolve more rapidly" is it that it is under greater selection pressure?

The SNP genetic correlation matrix was highly similar to the developmental change matrix, as demonstrated by the Mantel test (r = 0.57, p <.0005, see Figure 2).”

I am not a big fan of qualitative judgments (e.g. highly). Especially that I assume r can vary between 0 and 1 so "highly" can be seen as an overstatement.

As much as the Mantel test statistics are different from 0, are they also different from 1?

Generalized

“Additive Mixed Models (GAMM)”

Could you add some details about the maximal order of the splines you considered? How was the best model – best order selected?

“This revealed a close to perfect match between the adult genetic clusters and their embryonic origins.”

24. You say grouping is extremely similar, but compared to the clusters presented in Figure 2, I feel that this is an overstatement. E.g. caudate, accumbens, putament, pallidum – two of those were in separate clusters previously. Also positive rG between cerebellum cortex and WM while this was negative before.

25. “In all cases yielded the slope function the lowest IC values”. This is not true – see caudate and cortex.

What to make from small AIC/BIC differences i.e. a marginally better fit? I wonder whether Table 3 is really adding anything, especially that the age trajectories are mostly descriptive?

26. “We fitted the developmental trajectory of each cluster…”.

I assume you took the total volume of each cluster? What is this analysis really adding? First it assumes the cluster is somewhat homogenous (see my second comment) and another problem is that the different volumes can have extremely different scales which makes interpreting the sum difficult.

27. “Using multivariate latent change score models, we calculated…”.

Why did you not also use the annual symmetrized percent change you used previously? Especially that you want to compare rG to the phenotypic correlations you previously studied.

28. rGs from twin models are corrected for ICV, which does not seem to be the case for the GREML approach. Is this simply missing in the text?

“…pair of the 16 brain sub-cortical structures, including the first ten principal components, sex and age as covariates.”

29. “log likelihood test”. I am more used to it being referred to as the likelihood ratio test.

30. “restricted maximum likelihood methods” – (very) minor detail but REML is the optimisation approach used to estimate the parameters of what is a bivariate mixed model. A compromise may be to talk about GREML, which is not more correct but quite commonly used to refer to the LMM implemented in GCTA. For an analogy, it is as if you referred to the GAMM as a Restricted Marginal Likelihood method.

31. “…due to heuristics in the algorithm…”. What are the heuristics here, is it random starting values?

32. “Also, all reconstructed surfaces were inspected, and discarded if they did not pass internal quality control.” Surely, this does not apply to the UKB analyses. Did you perform any QC on them beyond the UKB provided screening?

33. “In addition, we removed participants suggested to be removed for genetic analysis by the UK Biobank team.” Could you add a precision about why this exclusion is recommended?
