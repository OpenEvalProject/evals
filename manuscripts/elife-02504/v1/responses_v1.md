# Author response - Round 1

Authors:
- Leslie M Turner
- Bettina Harr

## Response text

DOI: [10.7554/eLife.02504.022](https://doi.org/10.7554/eLife.02504.022)

Analysis: Given the large effect of the X chromosome it seems critical to include X variants in the covariance matrix. We also believe that more could be made of analyses of the genetic architecture of the trait (e.g. contribution of individual chromosomes to variance in the trait using GCTA or similar software). Similarly the DMI model makes specific predictions about the direction of epistatic effects (combinations of derived alleles deleterious) which should be easy to address by polarising variants using an outgroup.

Inclusion of X genotypes:

We repeated the mapping analysis, including X genotypes in the covariance matrix. The main effect of this change was a slightly more stringent P value cutoff to identify significant SNPs, which resulted in the identification of fewer genomic regions (26 regions excluding the X-chromosomal markers, 12 regions including the X-chromosomal markers). The positions of the regions stayed essentially the same.

Variance explained by individual chromosomes:

As suggested by reviewer 1, we used the software gcta to try and estimate the contribution of individual chromosomes to phenotypic variance (i.e. relative testis weight). This analysis has been pioneered on large GWAS datasets on human quantitative traits, such as height. We faced several problems with this analysis. The first problem is a conceptual one, the second a technical.

The model that gcta is fitting assumes that SNPs have additive effects on the trait. While this is very likely a good approximation for traits such as human height, it is not appropriate for hybrid sterility traits, because the Dobzhansky-Muller model predicts epistatic interactions between loci are necessary to observe hybrid defects. The additive genetic model would be adequate if we would map quantitative variation in testis weight within a subspecies, but not for the transgressive phenotypes in the hybrids between subspecies.

The technical problem arises when one deals with a highly structured population, such as our population from the hybrid zone. If there is an effect of population structure, SNPs on one chromosome will be correlated with the SNPs on the other chromosomes, hence estimates of variance explained individual chromosomes are overestimates. To correct for this, Yang et al. (2011) introduced a model where the genetic relatedness matrices of all the chromosomes are fitted jointly (the –mgrm flag in gcta) to estimate the variance explained by each of the chromosomes. When we applied this version of the model, the likelihoods did not converge, even after running the maximum number of iterations allowed by the software (10,000). The most likely explanation for this problem is that our sample size is too small (185 individuals). The recommended minimum sample size for genome-partitioning analysis is 5,000 (http://gcta.freeforums.net/thread/27/partioning-autosomes).

The results presented below were obtained by running the REML procedure on each chromosome separately, incorporating the first 10 principle components (Eigenvectors) calculated over the whole autosomal dataset to correct for population structure. Similar results were obtained when Eigenvectors were calculated from the respective chromosome to correct for population structure.chromosomeV(G)/VpSEP valuechr10.5413090.1156481.66E-05chr20.6981860.091513.09E-06chr30.3710460.1399060.006895chr40.5786850.1134676.23E-05chr50.2797610.1435280.02633chr60.5466150.1095883.64E-07chr70.5477680.105442.16E-06chr80.3473580.1338620.001698chr90.4168490.1433850.005933chr100.3112710.1646130.05873chr110.4577160.1312590.002731chr120.4465140.117824.18E-07chr130.3062720.1341670.004079chr140.5211040.1166298.90E-08chr150.3575160.1218790.0002658chr160.543880.1122186.10E-06chr170.6444970.0918078.874E-09chr180.2089510.1459250.1124chr190.0567780.1094880.2996chrX0.7522310.0719999.09E-10

The heritability estimates (i.e. the proportion of phenotypic variation due to additive genetic factors, V(G)/Vp) are not reliable due to the complications stated above. However, in both sets of analyses, chromosomes 2, 17 and X explained most of the variation. These results are consistent with our mapping analysis, which identified significant GWAS regions located on those chromosomes.

Ancestral vs. derived sterility alleles:

We agree that determining if sterility alleles are ancestral or derived would be of great interest. However, significant SNPs identified by GWAS are unlikely to include the causal mutations for mapped phenotypes. Without knowing the causal variant, it is not straightforward to categorize sterility alleles as ancestral or derived. Nevertheless, we compared genotypes in significant regions from M. m. musculus and M. m. domesticus populations to M. spretus, M. spicilegus and M. mattheyii. Each region comprises numerous SNPs that can be polarized and additional sites with shared polymorphisms between musculus and domesticus. Thus, it will not be possible to determine which alleles are ancestral vs. derived until future studies identify causal genes/mutations.

Interpretation: The phenotype studied is not hybrid sterility (despite the Title). There is actually no direct evidence for an association between the trait studied and fitness. Indeed the statement that there were no significant results for sperm count is a little worrying. However, there is limited evidence that the phenotypes of the hybrids are typically outside the range of normal variation within the species. It is important to note these caveats.

We agree that that there was a need for additional explanation of links between the mapped phenotype and hybrid sterility. We discuss this issue in detail now and note caveats in the “phenotyping” section of Methods, and the “sterility-associated phenotypes” and “effect size” sections of Results. In addition, we mapped another sterility-associated phenotype: testis expression PC1.

Presentation: Without fine-mapping or replication, the ability to identify/localise specific genes as being important in the trait is limited. For this reason, we feel the emphasis on long lists of rather weakly-supported candidate genes is misplaced. There are also issues with formatting, clarity of figures and citations.

We agree. We simplified annotation of the GWAS regions, reporting only genes with strong evidence for roles in reproduction (Tables 1-2) and removed most of the discussion of candidate genes from the text.

We made several major changes to the organization of the manuscript to improve clarity. First, we edited the Introduction, incorporating suggestions from reviewers to better explain the motivation and logic of the study. Second, we separated Results and Discussion and added more subheadings. Third, we reduced the number of figures in the main text to four.

Additional changes:

We made several changes in response to concerns of individual reviewers, notable examples include:

Significance thresholds: We clarified the motivation for reporting results using a permissive (FDR <0.1) threshold and using multiple lines of evidence to identify loci likely to be true positives. We report estimates of the false positive rate using stringent and permissive thresholds from simulations.

Tests for interactions:

Instead of testing for interactions with MCMCglmm, we used a mixed model approach similar to the GEMMA framework used to identify single-SNP associations.

Overlap between GWAS regions and sterility QTL:

We performed permutation tests to determine if associations between GWAS regions and previously reported candidate sterility regions were non-random. It was not possible to test for non-random concordance between genetic interactions identified in this study and those reported in F2 hybrids by permutation because individual GWAS regions have multiple partners and the number of possible pairwise interactions between SNPs varies widely across region pairs. In the absence of statistical support for the overlapping pattern, we decreased emphasis on this result by including the figure showing overlap as a supplemental figure.

Yang, J., et al. 2011. Genome partitioning of genetic variation for complex traits using common SNPs. Nat. Genet. 43:519–525.
