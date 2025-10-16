# Peer review - Round 1

Editors:
- Craig T Miller, University of California, Berkeley United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.29510.015](https://doi.org/10.7554/eLife.29510.015)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Genomic regions controlling shape variation in the first upper molar of the house mouse" for consideration by eLife. Your article has been favorably evaluated by Patricia Wittkopp (Senior Editor) and three reviewers, one of whom, Craig T Miller (Reviewer #1), is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal their identity: Alistair R. Evans (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Pallares and colleagues study mouse molar shape variation in two subspecies of house mice. Using a GWAS and 3D surface morphometric approach in hybrid mice, the authors identify five genomic regions associated with molar shape. One genomic region contains the candidate gene Mitf, and the authors show in lab mice with different mutant alleles of Mitf a role for Mitf in regulating molar shape. Overall this study presents the first GWAS for molar shape in natural populations, identifies the first genomic regions found to underlie quantitative variation in molar shape in nature, and identifies a specific gene (Mitf) regulating quantitative aspects of molar shape in the lab that appears to also regulate natural variation in tooth shape.

Essential revisions:

1) One potential concern is many of the Mitf mutant comparisons are done between mutant mice and a panel of non-sibling B6 mice. It seems possible that differences in genetic background in these mouse lines contribute to the differences in tooth shape. One nice argument against this is the authors observe differences in tooth shape between mice heterozygous and homozygous for the mi-vga9 allele. It would strengthen the authors' conclusions if in Table 1 they compared the mi-vga9/mi-vga9 mice not just to wild-type mice, but to the mi-vga9/+ mice. In Figure 5, these genotypes look quite different, but it would be better to also formally test the differences. Along these lines, can the authors comment on whether the mi-vga9/mi-vga9 and mi-vga9/+ mice were full siblings? If so, that would further strengthen the argument that Mitf, not genetic background differences are responsible.

2) Although finding actual mutations underlying the Mitf-associated QTL is beyond the scope of this study, can the authors at least comment on whether coding changes are found between the domesticus and musculus mice used in their study, or whether Mitf coding changes are present in the reference genome assemblies available for domesticus and musculus derived strains or populations?

3) Subsection “Association mapping”, third paragraph: Can the authors further justify the decision to pick arbitrary 500 kb intervals for most QTL? It seems they have data that would speak to patterns of LD in this sample, including genome-wide averages and within these QTL, so not sure whether 500 kb is an overly conservative estimate or not.

4) Subsection “Association mapping”, second paragraph: I was surprised that no genomic regions were significantly associated with size variation, given how polygenic and strong the signal appears for tooth shape. Was mouse size corrected for in mapping centroid size?

5) "The other mutant alleles do not exhibit osteopetrosis in homozygotes." Can the authors clarify for this statement, whether they mean osteopetrosis has not been reported in homozygotes for these alleles, or whether they (or other groups) looked for osteopetrosis in homozygotes? If the latter, the authors should provide references or data to back up this claim. If the former, the sentence should be edited. Same comment for “The evidence presented here for effect of Mitf on molar shape comes from mutations in a mouse laboratory strain, and it is therefore not equivalent to comparing the effect of naturally occurring alleles”.

6) Materials and methods: Only the first upper molar is analyzed. Why not, but the rational for this choice is never explained through the manuscript.

7) Geometric morphometrics: You used 10 landmarks to anchor the template. They are very important features to know because they impose some constrains, but there is no way for the readers to get this information.

For the full template, 1588 semi-landmarks are used and for the "wear-free" 1532. This is much denser in the second case than in the first given that all tips of cusps are removed. I don't understand why you increase the sampling.

8) Subsection “Tooth shape, mouse age and wear”. Your idea is that age is related to wear, as once erupted tooth shape doesn't change except by the effect of wear. In my opinion you should explain it to readers.

9) Wear is expected to be on PC1. People have used Burnaby-like procedure to get rid of such artifacts (many examples with fish) based on PC1 or expected shape changes. You decide to use a very different alternative approach (quite a disappointing one) by cutting cusp tips. Why not, but why? Because age impacts a lot of PCs and thus you consider that the effect of wear is spread all over the shape space? If so, I think you should explain your rational. Interestingly, age explain the same amount of variance with the 'wear-free' template but is less significant.

10) Finally you analyzed something very close to what is captured with 2D outline. The amount of 3D information you have in your sampling depend on the cusp height kept in the template. You didn't say anything about that. How did you decide the height at which you cut the tips?

11) I don't understand why you run separate Procrustes superimpositions (subsection “Functional evaluation of the candidate gene Mitf”, second paragraph). It adds a very complex way of comparing shape changes. I can understand that you were afraid that weird mutant twists your Procrustean space for GWAS but in my opinion, you could have added the mutant as supplementary observations into the hybrid GPA (i.e. superimposing each mutant to the hybrid mean shape). It will have allowed the comparison of shape changes using more classical tools of geometric morphometrics (angles between shape vectors, vector correlation etc.). In your approach, I don't get how the two can be centered and aligned to ensure that trivial variation are removed.

12) One additional remark on this method of comparing shape changes is that in order to get a threshold you consider the values obtained between PCs. PCs are orthogonal but not independent (subsection “Functional evaluation of the candidate gene Mitf”, last paragraph). The math ensures that they are orthogonal but nothing ensure that they are independent given the underlying generative processes (for ex genetics).

13) GWAS: The family structure in your sample is very strong and you correctly use linear mixed model to handle it but, as in your previous papers, running multiple univariate LMM on PCs is not the most powerful approach, but I understand that running multivariate LMM is challenging, but the cost is evident here as you don't have a very powerful design with 183 mice.

"To facilitate association mapping" but it is at the price of some power lost because PCs are not aligned to the underlying genetics.

Nonetheless, you correctly want to assess the effect size of best SNPs simultaneously on the full shape space (on all tangent coordinates), but why using only the first 18 PCs? Why estimating these effect sizes only on 86% variance? Did you consider that 14% are just analytical errors?

14) About that (subsection “Association mapping”, last paragraph) you say that you used the coefficient of determination but with multivariate data I guess you used an analogue based on distances (a ratio of sums of sum-of-squares) but there are other analogue based on classical multivariate statistics (Pillai etc.). It may be better to precise that it is procrustes distances based R2.

15) It is unclear that you used leave-one chromosome out approach to handle the pop structure in your LMM (subsection “Association mapping”, second paragraph).

16) SNP heritability: subsection “SNP heritability”, first paragraph: In my opinion, the way you present your computation of the "total heritability" is right in calculus but is little weird in term of genetics. In my opinion, you assess the sum of the additive genetic variances and do the ratio with the total variance to get a quite poor proxy of h2, and indeed means not much in term of heritability (see discussions of Monteiro and Klingenberg between 2002 and 2010).

17) Functional evaluation: subsection “Samples used to functionally evaluate Mitf”: I don't agree with this statement about sexual dimorphism. There are plenty of phenotypes with SD in mammals and more specifically in the house mouse (see for example Kart et al. 2016 Nat Comms). The fact that SD is low on bone shape doesn't insure that it is the case in tooth.

18) Results, first paragraph: The most parsimonious hypothesis is simply it is within species variation and that the inter-subspecific variance is smaller than the within, species-specific loci have small effects on this character and are not distinguishable from within-species loci. I don't think we need to ask for transgressive variation or hybrid instability.

19) Discussion: subsection “Genetic architecture”, first paragraph: Actually this conclusion is based on the huge amount of missing heritability (difference between the SNP heritability and the actual loci you catch-up). However, as your GWAS doesn't properly handle the multivariate nature of the shape space, you don't know anything about that because for instance a locus, orthogonal to all PCs, and explaining 1% of variance on each, will finally explained a lot of variance but will never be captured with your approach.

20) You have a very small sample size to run Hotelling T2. Will you do a t-test with N = 5 samples? Same conditions apply to Hotelling. Moreover you have twice more additional parameters plus correlation between the two variables to estimate. Maybe doing something non-parametric based on distances will be more reliable.

21) Some p-values for statistical tests were not reported in the manuscript.
