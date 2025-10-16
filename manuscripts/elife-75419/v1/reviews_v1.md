# Peer review - Round 1

Editors:
- Jenny Tung, https://ror.org/00py81415 Duke University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75419.sa0](https://doi.org/10.7554/eLife.75419.sa0)

This paper uses inbred hybrid mouse lines to estimate the heritability of the mucosa-associated microbiome and map variants in the mouse genome that are associated with the composition of the microbiome. The findings are of broad interest to microbiome researchers and improve on knowledge in the field, as the mapping design facilitates the identification of narrow association intervals and points to a novel correlation between heritability and cospeciation rates. The manuscript provides useful information about the approach to heritability estimation, allowing the results to be more readily placed in context. Congratulations on this important contribution to the literature.


---

# Peer review - Round 1

Editors:
- Jenny Tung, https://ror.org/00py81415 Duke University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75419.sa1](https://doi.org/10.7554/eLife.75419.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Key features of the genetic architecture and evolution of host-microbe interactions revealed by high-resolution genetic mapping of the mucosa-associated gut microbiome in hybrid mice" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Wendy Garrett as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. Demonstrate the robustness of the heritability analyses, including consideration of potential technical and biological confounding variables and ideally using complementary analyses (e.g., distinct methods for estimating heritability).

2. Demonstrate the robustness of the phylosymbiosis (heritability-cospeciation rate correlation) to controlling for taxon abundance.

3. Control for population structure are well as relatedness in the trait mapping analysis.

Reviewer #1 (Recommendations for the authors):

1. Heritability estimates in the study are quite high, including traits that are more highly heritable than even canonical high heritability traits in humans, like height. This could be accurate, particularly in a lab-controlled environment where genetic variation is ramped up by the crossing design and hybrid origins of the founder, but I think requires closer examination. In particular, I was surprised that there does not appear to be any adjustment for covariates in the heritability analysis: in my experience, batch and technical effects are omnipresent in genomic studies, including microbiome analysis, and can affect heritability estimates in unpredictable ways. Although sex and age are controlled for in the study design, are there differences in housing, diet, sample processing, library prep, or sequencing quality/read yield/lane/batch that account for measurable variance and need to be taken into account?

2. Related, part of the benefit of estimating heritability in a mixed effects models framework is the ability to flexibly control for other covariates. I don't see a benefit in using Mantel tests to correlate genetic relatedness and microbiome structure overall-as heritability is much more directly supported by direct estimation-and suggest removing this part of the analysis. I realize that the genetic relatedness-microbiome structure analysis might provide a "holistic" picture, but that could also be done by analyzing the top PCs of the microbiome data in a formal h2 analysis.

3. For the individual trait mapping analysis, I have some concerns that the models might not adequately control for background population structure. It's a good step to control for genetic structure with the K matrix, but I would like to see that the results are robust to including the top PCs of the genotype data in the model as additional fixed effects. Where possible, you could also consider using LD score regression to check that there is no unexpected inflation of test statistics.

4. In Figure 3 and lines 251 – 258, the results report PVE levels that are impossible (since more than 100% of variance can't be explained). While this is noted in the text, and some potential explanations are provided (lines 256 – 258), the current presentation isn't very useful because it's unclear how much trait variance is really being explained. A better alternative might be to construct the equivalent of polygenic scores for each trait and ask how much variance in each associated phenotype these composite scores explain (this approach would provide one value per mapped trait, upper-bounded by the overall trait heritability).

5. Finally, I lost the thread a bit when reading the second half of the results. All of these sections focus on one type of enrichment/annotation analysis or another. However, the hypotheses or models being tested in several of the analyses were not clear to me. E.g., why should we expect microbiome-associated genes to encode proteins that are networked to one another? Is the relationship to the GF versus conventional comparison based on the idea that if genes affect the microbiome, then changes in the microbiome should also affect the proteins those genes encode (not obvious to me)? Ultimately, what does it mean to be a "promising" candidate gene (promising for what kind of application), and how is that defined by these enrichment analyses?

Rather than having readers try to fill in the rationale for these analyses, it would be helpful to clarify the motivation in the paper itself-or even shorten these sections to focus on those where there is the clearest underlying model or hypothesis. This might also avoid diluting the more interesting, less speculative findings presented earlier.

Reviewer #2 (Recommendations for the authors):

Overall, this was an excellent study and I have few comments for improvement. A couple of points:

The association between heritability of taxa and their co-speciation rates is interesting, but I wonder whether this could be explained by an association between abundance and statistical power to detect heritability/co-speciation. Have the authors considered modeling heritability as a function of co-speciation rate and relative abundance? Such an analysis would be important to determine whether heritability and co-speciation rate are associated independently of abundance.

Relative abundances of microbes were used for all analyses (as opposed to absolute abundance quantification). Because findings based on relative abundances can be difficult to interpret, more discussion on this limitation would be helpful.

My understanding is that heritability estimates were generated only for ASV relative abundances. However, previous heritability studies have examined taxonomic levels from ASV to phylum. It would be interesting to extend the analyses presented to higher taxonomic levels beyond ASVs (eg species to phylum).

Reviewer #3 (Recommendations for the authors):

The main point of concern for me are the heritability estimates. The paper reports heritability results that may be a bit surprising considering the current knowledge and literature: the heritability values are very high, with several values around 90% or higher. This is unexpected, and I am not sure how this is reconciled with the expectation that most variation in the microbiome is environmental rather than genetic. Although some potential reasons are given in the Discussion (mice raised in a controlled environment, using cecal content, etc), it still makes me a bit uneasy to see such high heritability estimates. One potential way to approach this is to try a different statistical approach for calculating heritability. Another would be to compare heritability estimates from this study with estimates from other studies – by now there are quite a few studies that report microbiome-wide heritability estimates from humans, mice, and other host species. It could be useful to correlate the heritability estimates in the current study with those from these studies. Lastly, it would be good to compare microbiome heritability estimates from this study to heritability’s of other complex traits in the same system – are there other known phenotypes that have heritability estimates that are this high?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Key features of the genetic architecture and evolution of host-microbe interactions revealed by high-resolution genetic mapping of the mucosa-associated gut microbiome in hybrid mice" for further consideration by eLife. Your revised article has been evaluated by Wendy Garrett (Senior Editor) and a Reviewing Editor.

All reviewers appreciate the thorough revisions and re-analyses, which have resulted in a much improved manuscript. However, there are a few remaining issues that need to be addressed, as outlined below (the first item is the most essential):

1) Address the concern of Reviewer 3 below, which concern inflated heritability values in the main text. While the correlations in h2 estimates between methods are reassuringly high, Figure 8 in the response to reviewers also shows that the h2 reported in the paper (from lme4QTL) are typically several-fold (and sometimes an order of magnitude) higher than obtained from three alternative methods. This information would not be available to readers in the manuscript's current form. The response to reviewers indicates that lme4qtl was chosen because it had a high R2 with the PVE explained by the additive effects of significant SNPs (Figure 4 in the response to reviewers). However, both GEMMA and sommer produce similar R2 values (and in one case, a higher R2 value) but much lower heritability estimates. Do these lower estimates also correlate with co-speciation rates?

2) Consider the polishing revisions to the code repository suggested by Reviewer 3.

3) Consider integrating the useful explanation in the response to reviewers about experimental design controls for technical and batch effects in the main manuscript, as future readers may have similar questions.

Reviewer #2 (Recommendations for the authors):

The authors addressed all of my comments from the previous round of review. The inclusion of multiple alternative calculations of heritability have improved the manuscript substantially.

All 16S rRNA gene sequence data have been deposited to NCBI.

Reviewer #3 (Recommendations for the authors):

I thank the authors for a comprehensive revision that addressed many of my concerns. It was good to see that the heritability values are correlated across different methods, and that several other methods produced heritability values smaller than those generated by lme4QTL. This, together with the fact that heritability values for some bacteria are higher than those for traits like length and weight, supports my notion that lme4QTL heritability values are overestimated. I am not sure what the reason is -- it's hard to know without spending time digging into the data, and I might not have the statistics background to advise on this -- but I am not confident that these values are robust. I would encourage the authors to investigate these analyses very thoroughly, making sure that all potential confounders are accounted for, the models are reasonable, and there are no artifacts in the data. I would suggest the text includes the results of heritability analysis with other approaches (in addition to lme4QTL) more prominently: Figure 1 should report and visualize heritability values from all methods used, and visualize the correlations between them. The text should describe these results, the methods used, the heritability values reported and their correlation. There should be a clear discussion about the possible reasons for the high heritability values (and why they are lower using other methods). I would also suggest including the analysis comparing heritability values across studies in the text, and include a visualization of these correlations, rather than just reporting the p-value.

Regarding code availability, I want to thank the authors for enhancing the README file on the github repository, which now provides a nice description of the pipeline and analysis steps. However, I am not sure if this is sufficient for readers who want to reproduce the results: looking at the code itself, it seems like there are commands to load scripts that are not included in the repository (e.g. the snp_heritability_lme4qtl.R script loads the script function_for_gemma.r that I couldn't find anywhere), and these scripts might not be able to be run on other machines. I recommend amending the github repository and scripts so that anyone who wishes to do so is able to run the analysis and reproduce the results.
