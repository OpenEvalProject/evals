# Peer review - Round 1

Editors:
- Magnus Nordborg, https://ror.org/05twjp994 Gregor Mendel Institute Austria

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79238.sa0](https://doi.org/10.7554/eLife.79238.sa0)

This is an important paper that presents compelling arguments (based on simulation and comprehensively reviewed background theory) that Linear Mixed Models generally should perform better at correcting for genetic and environmental confounding in GWAS than more commonly used Principal Components methods.


---

# Peer review - Round 1

Editors:
- Magnus Nordborg, https://ror.org/05twjp994 Gregor Mendel Institute Austria

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79238.sa1](https://doi.org/10.7554/eLife.79238.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Limitations of principal components in quantitative genetic association models for human studies" for consideration by eLife. Your article has been reviewed by 4 peer reviewers, including Magnus Nordborg as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Detlef Weigel as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission. Individual reviews are also included as they are generally helpful. As you will see, there is strong support for your work, but it is clear that improvements are in order to justify your general claims.

Essential revisions:

1) You must at least discuss that the scenarios you test are in a sense as unrealistic as the (much more limited) simulations previously run, both in terms of sample size and population structure. Actual human GWAS are run "within populations" to minimize environmental confounding (more on this below) as much long-range LD and involve much larger sample sizes. Does this affect your conclusions? Related to this, the historical context for several methods you cite is not given.

2) Practical considerations for why PCs were/are used are not discussed either. Unbalanced designs, meta-studies, sample sizes.

3) You are not discussing environmental confounding, which is not only likely more of a problem in human GWAS than any of the other things discussed here, but could potentially justify a combination of LMM and PCs. Selection could have a similar effect, as discussed in the original LMM paper by Yu et al. (2006). Ideally, this should be simulated, but it certainly must be discussed, and the conclusions must take this into account.

4) You are similarly not addressing the issue of rare alleles and heterogeneity, which is a major preoccupation in human genetics. How does genetic architecture affect your conclusions? If you could address this, it would be a very nice (and timely) contribution (whereas the manuscript as currently written feels like it's fighting a 10-year old battle).

5) Finally, the description of the theory is often hard to follow, relies heavily on a particular model (ancient allele frequencies), and appears to be wrong in a few specific cases (see comments below). The results table is likewise inscrutable, and it is difficult to relate your simulations to real-life scenarios.

Reviewer #1 (Recommendations for the authors):

At the very least you need to comment on the practicability and relevance issues noted above.

I would also recommend adjusting the writing to make your (otherwise lucid) review of the theory more accessible to a broader audience. Not only do you assume considerable knowledge of mathematical statistics, but you are also deeply rooted in a classical quantitative genetics framework. Terms like "inbreeding edges" are likely to befuddle all but a tiny fraction of humanity!

Reviewer #2 (Recommendations for the authors):

1. Environmental effects are known to correlate with population structure. A silly example of this is chop-stick skills, which obviously correlate with broad levels of East-Asian ancestry, e.g. in a global population sample it would likely correlate with the first two top PCs, and additional PCs would not explain more. Hence, for such a trait the generative model could really just be the top PCs, in which case including top PCs as covariates would be optimal. An LMM would in this example probably try to account for a much more complicated structure in addition to the top PCs. Hence, in summary, I would appreciate some simulations where you have environmental contributions that are perhaps strongly correlated with individual PCs, as I believe such scenarios may exist in real data analyses.

2. I really appreciate the detailed simulations in this study, but perhaps it would make sense to simulate traits given UKB genotypes? Also, and perhaps more importantly, how about also evaluating the two approaches on UKB data, to see if you really find more hits using LMMs? (similar to Loh et al., NG 2018)

3. You note that PCs are the top eigenvectors of the kinship matrix. This is usually true, but not always as when deriving PCs one should ideally apply some LD adjustment to avoid PCs capturing long-range LD regions, which can otherwise reduce power to detect variants in long-range regions. See e.g. Patterson et al. (PLoS Genet 2006) or Privé et al. (Bioinformatics 2020).

4. Following up on the previous comment, I wonder if the conclusions in this paper change if PCs are derived the way they often are, i.e. excluding long-range LD regions and/or using some LD adjustments.

5. Some of the LMMs cited are not classical LMMs, in the sense that they do not assume an infinitesimal genetic architecture. E.g. BOLT-LMM (Loh et al., Nat Genet 2015) assumes a mixture of two Gaussians as a prior for the effects, which they show can improve power further. Mbatchou et al. (Nat Genet 2021) also use blockwise ridge regression (infinitesimal model), which is effectively a more flexible prior. Using these, the relationship between the PCs and the model becomes yet more complicated. Similarly, the GCTA mixed model GWAS uses a LOCO approach to improve power, which I believe means that a slightly different kinship is used for each chromosome.

6. Your derivation assumes that there are some ancestral allele frequencies underlying the true model, but that seems perhaps unnecessary to me because these allele frequencies only represent the "correct" weights for the variants, and we know that they are probably wrong anyway. Indeed alternative and likely better weightings can be used, see Speed and Balding (AJHG 2012, NGR 2015, NG 2019). If you instead assume the sample frequencies are the right frequencies, then all the math becomes simple by standardizing the variants.

7. Another publication that also provides some similar theory on the relationship between PCA and mixed models is Janss et al., (Genetics 2012). (Interestingly, although their work is very nice their PCs did however have major long-range LD issues.)

8. The authors mention that LMMs are not well suited for unbalanced samples, e.g. where the case-control ratio in the sample is <5%, and cite Zhou et al., Nat Genet 2018 as a solution. However, before Zhou et al. there were no computationally efficient generalized mixed models capable of being able to be applied to UKB sample sizes, which could help explain why LMMs haven't been adopted as quickly as one might have expected.

9. I believe there is some concern regarding meta-analyzing LMM GWAS summary statistics, e.g. whether one should use the actual effective sample sizes or the effective sample sizes (which I believe is the best approach). I believe this is probably the main reason why LMMs are not as widely used as we would like. I would appreciate some discussion or reflection on this.

Reviewer #3 (Recommendations for the authors):

The presentation of the results in Table 3 is nearly incomprehensible.

The authors are incorrect about no other troublesome cases on line 48. The differential variance between populations can induce bias (see papers from Xihong Lin).

The author's discussion of the benefits of including sample PCs in LMM (eg 468-472 on p28) is misinformed. In particular, it is a critical step for methods like BOLT.

The authors say "low-dimensional" when they mean "low-rank".

The Sul and Eskin paper does not result in a tie. It states that creating a second kinship matrix from the PCs can address the issue presented in Price et al. entirely with LMMs.

It would also be interesting to know to what extent the singular value distribution matters versus the rank? The authors have some discussion of this in 5b but it is not well developed.

Reviewer #4 (Recommendations for the authors):

I have the following comments for consideration:

Historical context: The overall reasoning for controlling population stratification and relative kinship for different types of populations was given in [26]. It would be helpful to revise the introduction part to focus more on the original research papers and their reasonings: [5] (PCA), [9] (Q), [26] (LMM, Q in MM), and [16] (PC in LMM and actual association study). The later studies with LMM from the groups behind GCTA should be mentioned as the (emerging/emerged) trend, in addition to those comparison studies.

A couple of relevant research may be examined and discussed, in terms of different types of populations, determining the number of PCs to be included in the LMM, model comparison, and modeling fitting (redundancy). https://doi.org/10.1534/genetics.108.098863 https://doi.org/10.1038/hdy.2010.11

One question is the justification for examining a single heritability of 0.8. This level is generally regarded very high. It would be more convincing to see the results when h2 = 0.3-0.6, particularly if this is set for a large population with different subgroups.

The choice of m1=n/10 is not adequately justified. Even though we typically assume that there are many loci and the detection power increases with larger sample sizes, the actual detected numbers of loci in empirical studies are lower than that. With the current set m1 (Table 2), what were the power values, and are they close to the empirical studies?

"The largest limitation of our work is that we only considered quantitative traits". This may be expanded to include that with the overall simulation scheme, you assume the causal variants are functioning across different groups of a large population (2.2.5 Trait Simulation)? Real data with measured traits may be different. This can also be different for different types of complex diseases. Some clear context information should be given at the beginning too.

Among these simulated population and real data, have you examined whether a small number of PCs are indeed significant to explain some trait variation? I think this was the original thinking of applying PCs to correct the population stratification.

L46 and L487. Assume the low-dimension part of the relatedness matters in terms of trait differences among groups, which need to be adjusted.

L53-57. This is not an accurate summary of the relevant papers. Earlier papers set up the general LMM framework with different components that may be included or included and individual components that can have varied forms or reported the first actual association study with the LMM framework. These two are earlier papers that (re-)introduce LMM to the association studies, and markers were used for kinship, structure, and PCA.

L64-70. Redundancy is not an issue since the objective is to control false positives using two types of covariates.

L166. Large "and"(?) Family.

L282. Theoretical and empirical evidence of these two needs to be provided.

Table 3. Not clear about the asterisk.
