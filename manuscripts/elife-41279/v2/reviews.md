# Peer review - Round 1

Editors:
- Patricia J Wittkopp, University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.41279.sa1](https://doi.org/10.7554/eLife.41279.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

We are excited to have this impressive study of cis-regulatory grammar published in eLife. Figuring out how cis-regulatory sequences determine gene expression has been a long-standing challenge for the field, and this study makes an important contribution by revealing the relative roles of transcription factor binding affinity and surrounding sequence context with a rigorous and deep set of experiments.

Decision letter after peer review:

Thank you for submitting your article "Synthetic and genomic regulatory elements reveal aspects of cis-regulatory grammar in Mouse Embryonic Stem Cells" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Patricia Wittkopp as both Reviewing and Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: David N Arnosti (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The conversion of DNA sequence information to transcriptional output relies on the context-specific interactions of transcription factors and cofactors, which influence each other and the transcription process in multiple ways. Thus, it has been difficult to identify general principles allowing predictive models of cis regulatory element outputs, even with precise information about TF concentrations and DNA sequences acted upon. In this manuscript, King et al. use plasmid-borne massively parallel reporter assays to identify cis regulatory considerations that influence the activities of Oct4, Klf4, Sox2, and ESRRB transcription factors in embryonic stem cells, which have been well characterized for gene expression and genome-wide chromatin features. They take a two-pronged approach for this study, testing hundreds of elements in plasmid libraries. They create synthetic elements carrying binding motifs for the four proteins in varying numbers (2-4 sites), and they select genomic sequences that resemble these elements in that they are known to have some level of protein occupancy, and bear motifs of the OSKE factors. Using high-throughput sequencing, the activities of the libraries are assessed in transfected cells, and relative expression compared to certain mutant constructs in which the motifs are removed.

The presence of a large number of inactive elements is a valuable finding that allows the authors to assess the importance of specific features for activity vs. inactivity.

The authors determined that the activities of the generally active synthetic elements can be predicted by random forest machine learning models, employing the number of bound elements as well as the binding site arrangements. However, the insights gained from these constructs appear not to contain predictive power on the genomic sequences, where a smaller fraction of candidate elements are active. A gapped kmer approach indicates that differentiating the active from inactive genomic sequences involves the identification of additional binding sites. A more nuanced RF modeling approach involving factor spacing, primary sites, and ChIP signals measured on these elements is able to provide a better level of accuracy than any of these elements alone; interestingly, these are factors that were specifically left out of the synthetic library, where spacing is held constant, and motif quality is not varied. Consequently, when using synthetic elements, an enhanceosome model described their data better, while with genomic elements, the billboard model worked better.

Overall, this study points to possible avenues for progress, as well as very specific reasons for pessimism. The synthetic elements tested include certain features that may not apply to endogenous elements (placement of an element directly next to a basal promoter, plasmid rather than integrated location), as well as consciously avoid variables that may be key (differences in spacing, affinities). Since we already have much evidence for the roles of spacing and motif affinity, it makes sense that the authors deliberately set up a testing situation which can assess other factors for possible use in wider modeling efforts, namely order of elements on the enhancer, and number of factors present. The answer appears to be that any informative synthetic approaches must incorporate the factors pursued in the analysis of their endogenous data elements. Overall, this study makes an important contribution to identification of pathways that must be pursued to subsequently create deeper understanding of the DNA-to-transcriptional output function.

Essential revisions:

1) Differing enthusiasm for the modeling component was reflected in the reviewers' comments. One thought that the emphasis on the models was an over-reach, especially because the data neither supports one or the other model, nor is there enough of it to make a definitive claim. The other was not bothered by the data not fitting neatly into either model nor what was perceived as an oversimplification of the models. However, even this latter reviewer agreed that the authors should more clearly spell out how their tests do or do not sample the many variables. Revision to the modeling section to make these points more clear to readers is needed.

2) There was also a difference in opinion about how much this work advances the field, with one reviewer pointing out that it doesn't identify new physical principles or factors affecting transcriptional regulation, and the other agreeing but arguing that this work is part of the necessary path that our fields must explore to make real progress on predictive approaches. I agree that the large size of the set of active/inactive endogenous elements characterized is a very important contribution to the field; one that will help us better recognize and understand enhancer sequences. Revision to the text to more explicitly articulate the contribution to the field of this work is needed to address this concern.

Below are specific comments from reviewers that elaborate on the concerns expressed more generally in the two points above:

1) Even though I like the logo-like presentation of the preferred order of the TF on the synthetic promoters, to claim that this result fits an enhanceosome model is a stretch at best. An enhanceosome model requires positioning of every TF in a particular conserved structure. Here there is a certain preference for some positioning. To my understanding the authors only used identical/constant non-binding site sequence in all of the synthetic constructs. How do they know that these sequences do not influence the order? Can the authors choose two variants (one strong and one weak), and introduce 5 different flanking sequences and check whether the ratio in expression between both arrangements is conserved?

2) For the genomic elements the results are not surprising, as we expect to get interference from unknown or cryptic regulatory elements. The analysis they provide in Figure 5 shows a nice correlation between ChIP-seq data and strength of expression supporting the notion that the more elements bind the promoter the higher the expression. From my perspective this result supports neither the billboard nor the enhanceosome model, but rather a more dynamic model where the cumulative occupancy keeps the promoter open for longer supporting a higher expression. The dynamic or "occupancy" model is further also supported by the data in Figure 4, where there is a correlation between higher expression and stronger sites. I would like to see a discussion of a more dynamical model as another option for explaining their data.

3) The claim that optimal spacing leads to better expression is also not supported but the data. First of all – what is optimal spacing? The author don't say. Is it constant for all the TFs used, or different for each TF pair? Do they have data which supports one type of spacing over another? Finally, how do they know that next-nearest neighbor effects do alter "optimal spacing" of nearest neighbors? To answer this question will require another much larger OL, which is clearly outside of the scope. Nevertheless, I would like the authors to clarify their claim.

4) The authors implicitly factor out a number of elements in their synthetic library, either to make the task manageable, or because they suspect certain features are more important. These include the design of having up to just one binding motif for each of the factors, the placement of the factors adjacent to the basal promoter, ensuring that certain proteins will have privileged access to the basal machinery, and the decision to not test spacing. The logic of the paper would be easier to follow if the authors would explain why they made these choices e.g. perhaps certain features are already well enough known.

5) The finding that chromatin accessibility is not at all predictive is quite fascinating – many studies have relied on such data to infer where relevant enhancers are, and in which cell types. The authors should place this finding in context – does it have something to do with their use of plasmid-borne genes, rather than integrated reporters?

6) The RF modeling of genomic sequences with the most complex set of features (58 in all) sorts enhancers into active and inactive elements (if I understood their approach). Would the predictions be different, more informative, if they were attempting to predict relative activity? IF this is a misunderstanding, it would be helpful to clarify.
