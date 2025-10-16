# Peer review - Round 1

Editors:
- Silke Hauf, https://ror.org/02smfhw86 Virginia Tech United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.106525.3.sa0](https://doi.org/10.7554/eLife.106525.3.sa0)

This important study addresses the role of non-genetic factors in individual differences in phenotype. Using C. elegans, the study finds that non-genetic differences in gene expression, partly influenced by the environment, correlate with individual differences in two reproductive traits. This supports the use of gene expression data as a key intermediate for understanding complex traits. The clever study design makes for compelling evidence.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.106525.3.sa1](https://doi.org/10.7554/eLife.106525.3.sa1)

Summary:

Genome-wide association studies have been an important approach to identifying the genetic basis of human traits and diseases. Despite their successes, for many traits, a substantial amount of variation cannot be explained by genetic factors, indicating that environmental variation and individual 'noise' (stochastic differences as well as unaccounted for environmental variation) also play important roles. The authors' goal was to address how gene expression variation in genetically identical individuals, driven by historical environmental differences and 'noise', could be used to predict reproductive trait differences.

Strengths:

To address this question, the authors took advantage of genetically identical C. elegans individuals to transcriptionally profile 180 adult hermaphrodite individuals that were also measured for two reproductive traits. A major strength of the paper is in its experimental design. While experimenters aim to control the environment that each worm experiences, it is known that there are small differences even when worms are grown together on the same agar plate - e.g., the age of their mother, their temperature, the amount of food they eat, and the oxygen and carbon dioxide levels depending on where they roam on the plate. Instead of neglecting this unknown variation, the authors design the experiment up front to create two differences in the historical environment experienced by each worm: (1) the age of its mother and (2) 8 8-hour temperature difference, either 20 or 25 C. This helped the authors interpret the gene expression differences and trait expression differences that they observed.

Using two statistical models, the authors measured the association of gene expression for 8824 genes with the two reproductive traits, considering both the level of expression and the historical environment experienced by each worm. Their data supports several conclusions. They convincingly show that gene expression differences are useful for predicting reproductive trait differences, predicting ~25-50% of the trait differences depending on the trait. Using RNAi, they also show that the genes they identify play a causal role in trait differences. Finally, they demonstrate an association with trait variation and the H3K27 trimethylation mark, suggesting that chromatin structure can be an important causal determinant of gene expression and trait variation.

Overall, this work supports the use of gene expression data as an important intermediate for understanding complex traits. This approach is also useful as a starting point for other labs in studying their trait of interest.

Weaknesses:

There are no major weaknesses that I have noted. Some important limitations of their work are worth highlighting, though (and I believe the authors would agree with these points):

(1) A large remaining question in the field of complex traits remains in splitting the role of non-genetic factors between environmental variation and stochastic noise. It is still an open question which role each of these factors plays in controlling the gene expression differences they measured between the individual worms.

(2) The ability of the authors to use gene expression to predict trait variation was strikingly different between the two traits they measured. For the early brood trait, 448 genes were statistically linked to the trait difference, while for egg-laying onset, only 11 genes were found. Similarly, the total R2 in the test set was ~50% vs. 25%. It is unclear why the differences occur, but this somewhat limits the generalizability of this approach to other traits.

(3) For technical reasons, this approach was limited to whole worm transcription. The role of tissue and cell-type expression differences is important to the field, so this limitation is relevant.

Comments on revisions: The authors have addressed my previous comments to my satisfaction.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.106525.3.sa2](https://doi.org/10.7554/eLife.106525.3.sa2)

This paper measures associations between RNA transcript levels and important reproductive traits in the model organism C. elegans. The authors go beyond determining which gene expression differences underlie reproductive traits, but also (1) build a model that predicts these traits based on gene expression and (2) perform experiments to confirm that some transcript levels indeed affect reproductive traits. The clever study design allows the authors to determine which transcript levels impact reproductive traits, and also which transcriptional differences are driven by stochastic vs environmental differences. In sum, this is a comprehensive study that highlights the power of gene expression as a driver of phenotype, and also teases apart the various factors that affect the expression levels of important genes.

Overall, this study has many strengths, is very clearly communicated, and has no substantial weaknesses that I can point to.

One question that emerges for me is whether these findings apply broadly. In other words, I wonder whether gene expression levels are predictive of other phenotypes in other organisms. I think this question has largely been explored in microbes, where some studies (PMID: 17959824) but not others (PMID: 38895328) found that differences in gene expression were predictive of phenotypes like growth rate. Microbes are not the focus here, and instead, the discussion is mainly focused on using gene expression to predict health and disease phenotypes in humans. This feels a little complicated since humans have so many different tissues. Perhaps an area where this approach might be useful is in examining infectious single-cell populations (bacteria, tumors, fungi). But I suppose this idea might still work in humans, assuming the authors are thinking about targeting specific tissues for RNAseq.

In sum, this is a great paper that really got me thinking about the predictive power of gene expression and where/when it could inform about (health-related) phenotypes.

Comments on revisions: No additional comments


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.106525.3.sa3](https://doi.org/10.7554/eLife.106525.3.sa3)

Summary:

Webster et al. sought to understand if phenotypic variation in the absence of genetic variation can be predicted by variation in gene expression. To this end they quantified two reproductive traits, the onset of egg laying and early brood size in cohorts of genetically identical nematodes exposed to alternative ancestral (two maternal ages) and same generation life histories (either constant 20 ºC temperature or 8-hour temperature shift to 25 ºC upon hatching) in a two-factor design; then, they profiled genome-wide gene expression in each individual.

Using multiple statistical and machine learning approaches, they showed that, at least for early brood size, phenotypic variation can be quite well predicted by molecular variation, beyond what can be predicted by life history alone.

Moreover, they provide some evidence that expression variation in some genes might be causally linked to phenotypic variation.

Strengths:

Cleverly designed and carefully performed experiments that provide high-quality datasets useful for the community.

Good evidence that phenotypic variation can be predicted by molecular variation.

Weaknesses:

What drives the molecular variation that impacts phenotypic variation remains unknown. While the authors show that variation in expression of some genes might indeed be causal, it is still not clear how much of the molecular variation is a cause rather than a consequence of phenotypic variation.

Comments on revisions: I have no more comments for the authors
