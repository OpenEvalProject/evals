# Peer review - Round 1

Editors:
- Cheryl Ackert-Bicknell, University of Colorado United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68623.sa0](https://doi.org/10.7554/eLife.68623.sa0)

This paper offers a new take on multivariate genotype-phenotype mapping that identifies the joint phenotypic effect of genes involved in known biological processes that impact craniofacial variation. More specifically, the work expands on the traditional idea of candidate gene investigations into candidate biological process investigations, grouping multiple genes into a single analysis. In doing so, the authors show the joint effects of three strong candidate processes, chondrocyte differentiation, determination of left/right symmetry, and palate development on multidimensional craniofacial shape in the heterogenous Diversity Outbred mouse population.


---

# Peer review - Round 1

Editors:
- Cheryl Ackert-Bicknell, University of Colorado United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68623.sa1](https://doi.org/10.7554/eLife.68623.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Shapes and genescapes: Mapping multivariate phenotype-biological process associations for craniofacial shape" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and George Perry as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Laura Saba (Reviewer #1); Peter Claes (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions

All three reviewers emphatically stated they found the discussion and conclusions of this paper to be overstated, and not completely supported by the data. That said, they unanimously felt that a substantial revision of this work could deal with this problem and hence a revision opportunity was suggested over an outright rejection. Overall, the requested revisions do not require new data, but do require some reanalysis of the data. These issues are presented in greater detail in the point by point revisions listed below. In addition, when the reviewers tried to use the web app on the browsers Chrome and Firefox, just when the results appeared, they received an error that it disconnected from the server. Please check the web app stability and where necessary provide guidance on browser use for both Mac and PCs.

1. The use of the word 'process' throughout was not initially clear. It would help if it were clearly defined early on.

2. There is some inconsistency between the results, Figure 2A, and the discussion about how Nov/Ccn3 is annotated.

3. For the likelihood ratio test for differences in the distribution of cell sizes between Bmpr1b mutants and controls, it is important that all the interaction effects that included genotype were eliminated as well.

4. The matric used for judging the stability of the cluster results is often referred to as the cophenetic correlation coefficient. This common terminology may help to clarify the first sentence of the paragraph that starts on line 287. It isn't clear why a t-statistics was used to determine if the correlation coefficient was significantly different from zero. Perhaps a reference is needed.

5. In the 'Process effects in mutant morphospace', the authors point out similarities in the direction of the process vector to some of the mutants. It would be impressive if those process/mutant pairs annotated and if those genes had high weights in the MGP genetic vector. Similar comment for the gene/process pairs in the heatmap.

6. The conclusions starting on line 462 and ending on line 466 were not tested rigorously.

7. More detail about how the mutant MANOVA coefficients were calculated is needed.

8. It is not clear how the regularization parameter was chosen.

9. The paper is presented as the development of a new approach; however, it is not written in that way. The methods section "Regularized PLS analysis" is not accessible for a general public. If the reader is not already familiar with multivariate PLS, they will have no chance of understanding what this paper is all about. The results don't mention the actual genotype-phenotype approach, a description of the process-based MGP mapping should be done first thing in the results. Accordingly, the first figure should be current figure 10. And hopefully the legend will include more details.

10. The approach provides the phenotypic effect of genetic variation in already known pathways but it does not result in new genotype-phenotype associations; this is acknowledged in the text. However, the manuscript suggest that the results generate testable hypothesis which is just not supported by the provided data. The predictions of phenotypic effects are done on genes that are previously known to be involved in pathways that result in such phenotypes. For example, the Bmpr1b gene is annotated in the 'Chondrocyte Differentiation' biological process and genetic variation in such gene is therefore used for the genotype-phenotype analysis, but then, the authors suggest that given the results of the mapping, Bmpr1b should show chondrocyte development phenotypes, which is a circular argument. This example is also true for the other two predictions described in the manuscript. A way of showing that the approach results in testable hypothesis will be to run the genotype-phenotype mapping on pathways that are not previously known to affect craniofacial shape, and then test whether the high loading genes indeed affect the phenotype in the expected way. Until that is shown, the claim that this approach results in new testable hypothesis should be taking with caution and this paper must be revised to reflect this reality.

11. The approach is not new. Multiple other methods perform versions of multivariate genotype-phenotype mapping (this is discussed in the manuscript), but more importantly, the authors state to be using a method previously published by Mitteroecker et al. 2016 with the twist of restricting the analysis to known biological processes. It is not clear in the manuscript how much of their approach is actually new and how much is Mitteroecker's applied to a subset of markers. To highlight some lines where it sounds as if the authors did develop the method are found on lines 390-392 and lines 423-425, but rereading of Mitteroecker et al. 2016 suggests this is not the case. This is a crucial point that is not explained nor discussed at all.

12. One of the challenges with multivariate analyses of this type is how to measure success of the model. In this case, the authors compared their genotype-phenotype results to phenotype results from genetically manipulated mice. As written, it is not clear where the information from the mutant mice came from. Although not explicitly stated, it appears that the mutant data is assigned to a process simply based on the inclusion of the mutated gene in the process being tested. There was no consideration of the genetic loadings of that particular gene in the original MPG model. If the mutated gene is in the process but has very weak genetic loadings, the assumption that the mutant phenotype should be similar to the phenotype associated with the process genetic loading is suspect. Theoretically, the MPG predicted phenotype in the mutated rodent would be more accurate if the mutated gene had a stronger genetic loading. Furthermore, if the mutant data was derived from the literature than it likely includes some publication bias. All genes included likely have some effect on cranial morphology or their results likely would not have been published.

13. Within the manuscript, there is an emphasis on the concordant direction of association between the process MGP axis and the axis of shape variation of a relevant mutant phenotype. However, some ambiguity remains about the relevance of the direction of association between the direction of the process MGP axis and the axis of shape variation of a relevant mutant phenotype. The loadings per gene are presented as negative/positive values in all figures, but it is never explained in the methods what does the sign mean. From the description in the methods, the direction of the correlation between the process PLS1 phenotypic loadings and the mutant MANOVA coefficients cannot be predicted unless you knew that the mutation of the gene was similar to one or more of the 8 founder haplotypes. This would require functional knowledge about the markers/haplotype included in the genetic loadings. Explain this in the methods and figure legends to help the reader actually understand what the PLS is doing.

14. There was also some confusion surrounding the rationale and methodology for estimating the null distribution of the R2 values. More detail is needed on how random marker selection for permutation was constrained to follow similar patterns of linkage disequilibrium to the observed marker set. Also, it is unclear what the rationale for randomly selecting markers rather than randomly selecting genes to generate the null distribution.

15. In general, the section 'Comparison of processes to principal component' lacks statistical rigor and conclusions are supported by the data. It is not relevant to compare all 1000 processes with the principal components without first filtering based on R2 values from the MPG analysis. The overall value of the analysis in this section is unclear.

16. In the discussion, the authors do not make a compelling case for how these types of analyses could be used to generate hypotheses for further studies.

17. As stated in the introduction this is a study of complex relationships between genotypes and phenotypes, and it is important to keep in mind that the technique used here as many others in similar endeavors, remain linear in nature, and therefore limited in exposing potentially non-linear relationships.

18. While the three example processes are interesting and easy to understand or follow in terms of, how this is of interest. I do struggle with the interpretation of the follow-up analyses, including correlating effects of processes, comparing of processes to principal component directions and process effects in mutant morpho-space. It is unclear if all these analyses make sense, and more importantly, the dimensionality into which these explorations are being made is rather low. First, any process effect is modelled by the first PLS-component only. Therefore, is the process and its effect on craniofacial shape modelled completely? Probably not. Second, the morpho-space in the last two mentioned analyses here above, is restricted to the first two principal components only. Therefore, is craniofacial variability modelled completely? Probably not. As a result, Figure 7 A, especially, represents only a sub-dimensional view of process effects versus mutant phenotypes. Discrepancies observed, e.g., none of the Bmp mutants align with the bmp signaling pathway, can be due to the limited linear dimensionality, or because of other underlying genuine biological explanations. However, it is hard to tell.

19. It is suggested by one of the reviewer that a better overlap between PLS and CCA and the use of both in genotype-phenotype associations is welcome. E.g., the discussion simply states, "Our approach also differs from methods that associate single locus effects with a multivariate phenotype (Claes et al., 2018)" without any explanation or insight how and what is different. In fact, the difference is not that great, besides the difference in underlying paradigm (GWAS versus candidate selection) and looking across multiple genes instead, which is the forte of this work. The incorporation of gene-based or haplotype-based MV GWAS into the discussion or introduction is also encouraged.

20. The reviewers need to make a stronger case about the benefit of groups of genes, because of the regularization and the selection of a 1-dimensional latent variable. I.e., It is of interest, for at least the three examples given, to run a gene-by-gene based analysis alongside, and to verify the benefit of the process-based analysis.

21. It is suggest that the authors investigate the effect of the user-defined regularization on their results. Additional cross-validation based results to see how good the first PLS component generalizes is needed. It is recognized that collecting a completely independent replication cohort is outside the scope or typical research resources. However, a more elaborated investigation using cross-validations might help.

22. Somewhat related to the point above, the authors need to provide more information on the dimensionality reductions performed, e.g., please present CV results using multiple PLS components, and provide insights on how many components are expected to be relevant in describing a process and its effect on craniofacial variation. The same applies for the 2-PC morphospace, of interest is to provide insight into choosing only 2PCs and no more?

23. The reviewers found the assessment cluster stability to be circular. Please include some references illustrating this approach or to investigate alternative measures for clustering techniques in machine learning, e.g., the silhouette score.

24. The Comparison of processes to principal component directions, ends with listing processes correlated to PCs. It was hard finding out if these groups listed made sense to be grouped as such. Additional and more explicit information for the reader in those directions is welcome here and in other places where such listing of processes (e.g., the clustering) is done.

25. How are the authors estimating % total phenotypic variance explained by the PLS genotype vector (lines 193, 226)? Is this the R2 they talk about in the methods? If so, please use the same terminology in results and methods sections.

26. The authors show that the %var explained in the first three examples (chondrocytes, palate, and symmetry) is higher than randomly chosen set of genes. But maybe, an additional biologically important point to test is whether pathways that are known to be involved in craniofacial development explain significantly higher phenotypic variance than pathways that are expected not to contribute to such phenotypes. This, besides being a testable hypothesis, will shed light into our understanding of the GO terms annotated to affect craniofacial development, and probably highlight pathways previously not associated with such processes that could be followed up in future work.

27. It is highlighted as a main finding that the phenotypic effect of different biological processes correlate with each other and with single mutants, however it is not discussed how much of that correlation is driven by different processes sharing genes. Could you elaborate on that aspect of the analysis? How many genes are shared and whether that correlates with the correlation of vector directions? I wouldn't be sure about how solid the main finding is unless it is clearly shown that it is not coming from shared genetic effects.

28. Supp Figure 4 shows several covariates for the data, however the methods only described how 'generation' was accounted for. What about sex? Mouse source? I don't have a way of knowing whether you are using them as covariates in your model, or whether you can actually add covariates to the model, because the model is not described in the methods.

29. The Results section is dry and doesn't provide any conclusion for the different sections. This could be improved if the conclusions of the analyses that are currently described in the Discussion section be moved to the relevant Results sections. This will also benefit the discussion that is currently very long and most of it is an actual description of results.

30. The information necessary to understand the figures should be in the corresponding figure legend not in the main text (e.g. l 327-329, l 331-333, l346-349). And, all figures showing results of the MGP analysis will benefit from ranking the genes according to variance of the loadings instead of alphabetical order – so it becomes easier to asses which genes are more important.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Relating Multivariate Shapes to Genescapes Using Phenotype-Biological Process Associations for Craniofacial Shape" for further consideration by eLife. Your revised article has been reviewed by 3 peer reviewers and the evaluation has been overseen by George Perry as the Senior Editor, and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below. The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. It is recognized that this is the second request for revisions on this paper.

Essential revisions:

A lengthy discussion was had among the reviewers about clarifying what is meant by new hypothesis. It was agreed that this issue must be addressed, but not does not necessarily need new data or experiments. Two of the three points below directly center on this issue.

1) In line 327-329 (of the tracked changes version) the authors write" "The majority of process MGP analyses demonstrate a similar importance to many alleles, highlighting the main strength process-level analyses over individual marker tests". This is an interesting claim, but what data supports this statement exactly? It would be great if this is supported by some density plot with for example # of genes ranking high (whatever threshold you choose) for each process. The authors have tested ~30 or so processes for some of the analyses. Please clarify if this claim coming from there?

2) The reviews all agreed that there was some level of circularity in the examples shown by the authors. The reviewers strongly felt that the response to comment #10 was not convincing, and the main text was not sufficiently modified to clarify this point. The reviewers agreed that if they remained confused on this point, readers of this manuscript likely would be too. The following is a second attempt at explaining the reviewers point again: all three mutants tested (Bmpr1, Fgf10, and Ankrd11) have previous published data showing their effects on craniofacial shape, sometimes even directly related to the biological process the authors are testing. So, given a) they are functionally annotated to be part of that process, b) there are previous publications -possibly the annotation is derived from those studies, although not necessarily- showing their phenotype effect on craniofacial shape, it does not sound as the authors are generating new hypothesis with their method. This would sound more convincing for the readers if the authors explained better for each example what is their rational for calling each of them a new hypothesis generated by the method. Explicitly list what is previously known or not known about those genes and their effect on craniofacial shape (they reference previous studies, but not in the context of framing how this is different from what they are doing), and be emphatically clear about what is the new "thing" they are trying to show. The reviewers are not saying it is not great to see those genes highly ranked within the process MPG vector, but they are just saying that strong claims of this being a new hypothesis are being made when working with genes for which an effect on craniofacial shape has been shown before. This exact point was also raised in query #16 but there was no new text in the Discussion addressing this point.

3. Related to the point above, there were several comments in by the reviewer previously on how, with the current data, the authors could approach more directly the 'testable new hypotheses' that this method generates, but they were not really implemented. This of course does not diminish the value of the paper, but the opposite would have increased its ability to prove that new hypotheses are indeed generated and proven true (not related to genes obviously related to craniofacial shape). For example, point #26 suggests to-test effects on processes that are not related/or expected to be related to craniofacial shape. The authors reply that is difficult to delineate such processes. The reviewers wondered about considering or at least mentioning 'gonad /sperm / egg development'? Social / mating behavior? Circadian rhythm? Etc.
