# Peer review - Round 1

Editors:
- Sara Hägg, https://ror.org/056d84691 Karolinska Institutet Sweden

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64329.sa0](https://doi.org/10.7554/eLife.64329.sa0)

This is an outstanding dissection of the genetic architecture of body weight at the genome-wide level across time and across environments. The use of a multiparental mouse population permits high-resolution mapping. The statistical analyses are advanced, leveraging new models, as well as tools developed specifically for this mouse population. The corresponding results are presented in nice and informative figures.


---

# Peer review - Round 1

Editors:
- Sara Hägg, https://ror.org/056d84691 Karolinska Institutet Sweden

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64329.sa1](https://doi.org/10.7554/eLife.64329.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Age and diet shape the genetic architecture of body weight in Diversity Outbred mice" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Matt Kaeberlein as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Andrew Dahl (Reviewer #2); Amelie Baud (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Wright et al., have empirically studied the subtleties of the genetic architecture of a classic quantitative trait, body weight, providing evidence of gene-by-age and gene-by-diet effects, both at the level of the entire genome and at the level of individual genetic loci. The authors also identified likely causal variants at individual loci. To do so, they used a mouse population descended from multiple, known founders and reconstructed the founder haplotypes at each locus, and also used genomic annotations. Finally, the authors also explored pleiotropy, allelic heterogeneity and locus heterogeneity at the associated loci.

This is an outstanding dissection of the genetic architecture of a complex trait at the genome-wide level, at the locus level, across time and across environments. The experimental design is excellent, with the use of a multiparental mouse population that also permits high-resolution mapping. The statistical analyses are good and advanced, leveraging the GxEMM model recently published by Dahl et al., as well as tools developed specifically for this mouse population to trace back the origin of each QTL to the progenitors of the population; the corresponding results are presented in very informative figures. Finally, the paper is well structured and written, however, additional clarifications, justifications and possibly small additional analyses are requested to make the paper a better fit to the eLife community.

Major Comments:

1. Please justify the p-value thresholds:

– Lines 306-7 say that a 10fold weaker threshold is used for the interaction test--why? Also, where do these thresholds come from?

– Is it sound to take this two-step approach of first finding loci and then 'fine mapping' variants nearby? It is definitely fine if the thresholds are valid genome-wide--but then why not test genome-wide?

2. Please eliminate nonnegativity constraints on VCs in software:

– Are you truncating estimates to be nonnegative? If so, this will cause bias, which I believe is visible in your simulations. This is essential to fix for testing, and also for unbiased VC estimates.

– Users will test random effects, so it is necessary to validate (or remove) this part of your software.

– I don't see an assessment of tests or ses for the VCs. A quick supp figure corresponding to the current simulations would suffice, I think.

3. Please assess standard errors/false positive rates/power for testing VCs:

– Are there evidence that GxEMM improves power for fixed effect interaction tests? I think just commenting on this is enough, but it does seem important if you want others to use your approach. Comparing power (or some measure of false positives) for EMMA vs GxEMM in real data and/or simulation would work.

4. Mouse phenotyping:

– the text needs to say upfront that the mice included in this study were subject to a battery of phenotyping beyond weighing, including metabolic cage phenotyping, blood drwas, and "challenge-based phenotyping procedures". Currently this information comes late in the text (L287), and the title of Figure 1 Supplement 1 reads "Raw phenotype measurements", which does not alert the reader to these additional phenotypes. Some details about this phenotyping are needed, in particular how many blood draws were taken and which specific procedures are included under "challenge-based phenotyping".

This extra phenotyping means that the body weight results presented in this study could be study-specific. In particular, the decrease in PVE observed with age in this study, which contrasts with increased heritability with age observed in previous studies (see Introduction), could be the result of increased noise due to extra phenotyping. The implications of this extra phenotyping need to be discussed.

Importantly, it does not mean that this study is any less relevant than mouse studies without challenging life events, humans also experience challenging life events

5. Clarifications on Figure 4:

– What do PVE_tot and PVE_e represent (more on this below)? In particular, L291 "total genetic variance for the 40% CR group" is non-sensical to me because I thought PVE_tot was across all mice – as suggested by the fact that there is a single dark grey line in Figure 4 showing PVE_tot. Also, I was expecting PVE_tot (dark grey line in Figure 4) to be the sum of non diet-dependent genetic effects + all 5 PVE_e (colored lines). Yet the dark grey line is below the coloured lines. Hence I don't have the right intuition for what PVE_tot and PVE_e are. Looking at the equations didn't help: shouldn't it be PVE_e in Equation (7) and PVE_tot in Equation (13)?

Clarifications are needed.

– Figure 4: I love this figure, but worry a bit about the role of GxGeneration:

– The legend gave me a strong (and wrong) sense that the GxE was all about diet. If possible, disentangling the two GxE contributions visually would be helpful.

– I don't understand why generation is included (eg you could instead include cage effects, or neither).

– Why not have an apples-to-apples comparison using GxGeneration as the baseline for questions about GxDiet?

– What is dark grey? The hom estimate from GxEMM? The hom+GxGeneration (but then shouldn't there be one estimate for each generation)?

– More generally, I don't follow how generation is being used in this paper. Is it just always in the background as a random effect, and if so, why? Why don't you test for locus-x-generation effects--if they're not expected to be interesting, why do they explain so much variance? If they are absorbing confounding, why not also adjust for cage (perhaps with the GxEMM 'IID' model to save degrees of freedom)? I suspect whatever you're doing is reasonable, but maybe just explain a bit more clearly.

Figure 4—figure supplement 2, (b), right – isn't it concerning that the permuted phenotypes are heritable? How can this be? I recognize you don't use this kinship in your real analyses (though believe you do use the genotypes from which the kinship is built), but some explanation here would increase confidence in the overall approach.

I'd like to see versions of Figure 4 that: overlay the interventions, as in supplement Figure 1; only show the E-specific genetic variances (ie substracting the sig2g_hom terms); and show the heritabilities (ie normalize by total variance at each time point). These would make nice supplement Figures if easy to generate.

6. GWAS-related comments:

– The GWAS section and the corresponding figures are overwhelming. I think it would benefit from shortening and using sub-headings. I think it would be good to show first how likely causal variants can be identified (including FAP groups, functional annotations etc. and have one figure for that), with the chr6 and chr 12 loci as examples, and THEN show these loci across age and diets to discuss pleiotropy and heterogeneity.

– except if we consider triallelic SNPs, the distinction between allelic heterogeneity ("a single locus harboring multiple functional alleles each with distinct phenotypic effects") and (what I call locus heterogeneity) "a single genomic region contains multiple functional body weight loci that are only revealed with sufficient fine-mapping resolution" (L346-349) is difficult to make because noise can blur genetic associations, making it impossible to know the exact position of the causal variant(s). Consistent with the difficulty I just mentioned, in the section L419-443 and corresponding Supplementary Figures, I find that the assignments of the loci to either allelic or locus heterogeneity not obvious/robust.

I think it would be best to focus on distinguishing between pleiotropy (same causal variant(s) affecting body weight at different ages or in different diets) and non-pleiotropy (be it allelic or locus heterogeneity), rather than trying to distinguish between allelic and locus heterogeneity.

Statistical tests exist to test the null hypothesis {same locus affects both traits} in multiparental populations (doi.org/10.1534/g3.119.400098). In addition, looking at the FAPs of the lead variants, as the authors do here, would be a great way to complement this statistical test. Statistical evidence of different loci + differing top FAPS would provide strong evidence for some form of heterogeneity.

If you are going to focus on pleiotropy yes/no, it would be good to show a locus with likely pleiotropic effects (with the caveat that this would be the null hypothesis so not really evidence, rather suggestive).

An idea now, not a request: It would be interesting to know whether the loci for which different causal variants are predicted to affect different traits (e.g. different ages) are also loci for which multiple causal variants are predicted to affect either trait (see doi:10.1038/ng.2644).

7. Gene enrichment:

– is there a significant enrichment in genes affecting neurological behavior in this study, to support the claim that the fine-mapped genes implicate neurological and metabolic processes? If not, probably best to move the corresponding section of the text to the discussion. Also discuss whether the associations between neurological genes and body weight could arise due to the stressful extra phenotyping of the mice (are those associations mostly for ages after the challenge-based phenotyping for example, or are they seen even for ages before that stressful phenotyping?)

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting a revised version of your article "Age and diet shape the genetic architecture of body weight in Diversity Outbred mice" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Matt Kaeberlein as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Andrew Dahl (Reviewer #2); Amelie Baud (Reviewer #3).

The manuscript has improved since last submission, however, few comments many for clarity need to be addressed before the manuscript can be accepted for publication.

Essential Revisions:

1) The methods used to calculate the genome-wide significance threshold for the GWAS are now explained with sufficient detail but I believe the thresholds used are much less stringent than commonly accepted (commonly accepted = some estimate of a genome-wide threshold of 0.05). Two lines of evidence for this:

– The authors "used the number of top singular values that explain at least 90% of variation across markers (500), as a proxy for the number of independent QTL signals,", from which they calculated the Bonferroni corrected threshold. They mention in their response to the reviewers that this approach is similar to what is used in human GWAS. However, based on the results presented in Table 1 of https://onlinelibrary.wiley.com/doi/epdf/10.1002/gepi.20430 for example, I believe a value much greater than 90% of variation needs is used when applying this approach to human GWAS data to get close to the commonly accepted threshold of 5.10-8. SimpleM (presented in Table 1 of the paper above) uses a cutoff of 99.5% and still yields a more lenient threshold than 5.10-8.

– Other GWAS in DO mice have used much more stringent thresholds than p-value of 10-4: for example, https://link.springer.com/article/10.1007/s00335-018-9745-8#Sec11 used a P value threshold of 7.3.10-7 to claim genome-wide significance at 0.05; https://reader.elsevier.com/reader/sd/pii/S0168952519300654?token=DEFE149F2C71C5E4EA274AB6AE3638597EEACA678E9451C00AEE8CCD806BDA0E20ACE4BAA8DEF5D6BE37F274132E9F61&originRegion=eu-west-1&originCreation=20210602135101 used an even more stringent threshold – see Figure 3C.

As a consequence of the likely very lenient significance thresholds used in GWAS, all the claims from GWAS and subsequent analyses are supported by limited statistical evidence. In particular, it is difficult to be confident that the apparent lack of pleiotropic signals observed across loci is a real feature of the architecture of body weight: the different FAPs observed etc. could be the result of noise. The genes identified in Table 1 are also supported by limited statistical evidence.

2) I find the GWAS-related text still poorly organised and overwhelming. For example, effects as a function of age are discussed in three different sections (L404, L454, and L483). Similarly pleiotropy is discussed in three different sections, and functional variants are discussed in different sections too. Perhaps group everything related to pleiotropy in one section, effects as a function of age in another, and candidate variants/genes in a third?

The non-linearity in diet is hard to understand and appreciate in the current manuscript. It is quite interesting (surprising), if true. Perhaps give it its own section?

3) Using a diagonal omega matrix is problematic not only for pairs of diets but also for pairs of generations I think, as interaction effect sizes could well be correlated in pairs of generations. The response from the authors to this issue is not entirely satisfactory to me, as they acknowledge that biases are possible but suggest biases will be small without really explaining why they will be small.

– Lines 291-5 – I don't understand why permutations don't fully break the correspondence between both sources of relatedness and phenotype? The kinship is just a matrix, and I don't see how substructures in this matrix could be invariant to random permutation. (You are mean centering such that row/column sums are 0, right? this is required for REML). In other words, what null are you testing if the permutations are also significant? Why doesn't your claim imply that a pure noise phenotype would have significant GxE?

4) For negative VC estimates -- the new supp Figure is great, as is the new flag, but don't see these mentioned in the text? I suggest you acknowledge your constrained approach causes bias (cf your simulations), but that you address it in principle with the new flag and also there is no reason to worry about your real data analyses (because you have such strong signals). I think it's important to have unbiased inference for GxE h2 (much more than for additive h2).
