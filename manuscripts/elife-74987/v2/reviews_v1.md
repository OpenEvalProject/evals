# Peer review - Round 1

Editors:
- Detlef Weigel, https://ror.org/0243gzr89 Max Planck Institute for Biology Tübingen Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74987.sa0](https://doi.org/10.7554/eLife.74987.sa0)

How easily is one species replaced by another system in an ecosystem, and what does it take so that two species are no longer equivalent? This is a central issue of ecology, which has been addressed in this elegant study. The rule of thumb the authors come up with, that genetic differences between two bacterial strains greater than about 100 bp are a good predictor of these strains being no longer ecologically equivalent, is likely to be one that will be highly cited in future.


---

# Peer review - Round 1

Editors:
- Detlef Weigel, https://ror.org/0243gzr89 Max Planck Institute for Biology Tübingen Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74987.sa1](https://doi.org/10.7554/eLife.74987.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Interactions between strains govern the eco-evolutionary dynamics of microbial communities" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by me as Senior and Reviewing Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

A central question in ecology is to what extent individual species can be replaced by other species with similar functional attributes. This study addresses this question using an innovative approach that begins with natural microbial communities harvested from similar niches in nature, bringing these communities to the lab and then letting them evolve under identical conditions. The conclusion is that even seemingly minor genetic differences can have outsized effects. Importantly, the authors come up with a rule of thumb, that genetic differences between two strains greater than about 100 bp are a good predictor of these strains being no longer ecologically equivalent. Because this number is easy to remember, it will likely be broadly cited, and it is therefore important to ensure that this estimate is not too far off the mark.

Essential revisions:

I would like you to address all the comments of the reviewers, but please pay particular attention to the following items:

1. There needs to be a better understanding of what "strain" means. Please explore the data more fully to estimate how many different lineages correspond to single "strains". If you have good arguments that strains are the equivalent of isolates, please state so.

2. Determine whether different strains are likely to have diverged within the host, or whether they constitute different colonization events.

3. State effect sizes when discussing inter-specific versus intra-specific correlations.

4. State how well the statistical approach used can detect positively or negatively coupled oscillations with or without a time-lag between strains, and explore how robust the conclusions are if these patterns remain undetected.

5. State if the correlational analysis would allow the identification of higher-order interactions.

Reviewer #1 (Recommendations for the authors):

Species were defined as having identical 16S rRNA (l. 97-98), a practice known as amplicon sequence variants (ASVs). Normally, V4 region sequencing is usually resolved to operational taxonomic units (OTUs) of 97% similarity representing something between the species and general level. There are benefits for either method, and ASVs may be problematic due to dissimilarities between different copies of the 16S rRNA V4 region in the same microbe. Also, different species in certain genera may have similar V4 regions. Since much of the accuracy of their method depends on this species inference, the authors should detail how they resolve species and possibly compare it to alternative methods.

Strains were resolved from SNPs that were highly correlated (mean R=0.8 according to line 144-145). What if this threshold changed? Would there be additional strains? How would that affect the cross correlation between strains within a species? Does the number of reads mapped to a certain genome affect this figure? Figure S5 shows a clear separation between strains (although in both panels one could spot 3 and not 2 strains), but how does this look in other species? If it's not as clear, this requires some benchmarking of clustering thresholds to see if the conclusion still holds.

Some of the results depend on the steady-state of the microbial community. The authors state there is a 31% temporal coefficient of variation (l. 106). Is that a little? A lot? How does it affect the relevant results? Figure S1 shows communities that are more stable than others: while M01 and M08 seem very stable, M02, M04, M06 and M10 seem quite variable. How do the results differ between stable and unstable communities?

All strain-strain correlation histograms and plots show a range of [0,1], but the range of coefficients for the Pearson correlation is [-1,1]. How do the authors explain this discrepancy? I could not understand it from the Methods section. In the case that only the magnitude of correlation (its absolute value) was considered, this is probably wrong, as two strains that have a negative correlation should probably not be considered coupled.

Question:

Does the distribution across genes of the SNPs separating two across genes determine strain dynamics? I.e., do you see clearer separation between strains if the SNPs fall within a certain functional group?

Reviewer #2 (Recommendations for the authors):

1. The authors have performed a number of interesting analyses of the genetic basis of strain coexistence. Looking at Figure 2C, it is clear that when there are O(104), strains are nearly always decoupled, whereas strains with <O(102) SNVs between them are nearly always coupled (a fact which the authors comment on). Interestingly, recent studies on the human gut microbiome (Garud, Good et al., 2019 and Zhao, Lieberman et al., 2019) estimated the number of SNVs which segregate between strains of a species found in unrelated human hosts is also O(104), while much smaller numbers of segregating sites (O(102)) accumulate due to clonal diversification within the host. This opens the interesting possibility, which the authors might consider exploring, that “coupled” strains are lineages which diversified within the host plant at some point prior to transplantation to the lab, while “decoupled” strains are strains which independently colonized the host. If the authors are able to confidently reconstruct haplotypes using the strai“ phasin” scheme employed, it should be straightforward to estimate the time to the most recent common ancestor (TMRCA) between coexisting strains, and then compare this number with the lifespan of the plant host species. This analysis would be highly interesting, as it might clarify the timescales over which evolutionary modifications accumulate into meaningful ecological differences between strains.

2. The authors outline an elegant model to determine if strain interactions are stronger than expected under an ecological null model in their Methods section (lines 652 – 686) and then actually use the significance test developed there to show that strains have a denser network of interactions than species in one community (M07), a result which is only shown in Supplementary Figure 15. Why is this analysis relegated to the Supplement? So far as I can tell, this network of interactions analysis is in fact not referenced in the main text, which seems a pity as it is an interesting analysis. Additionally, what do the results of this network of interactions analysis look like in the other 9 communities? If strains typically have a denser network of interactions across communities – if not, does this impact the conclusions of the paper?

3. I personally feel this test of interaction significance is in fact stronger than the relabeling scheme outlined in the main text as it tests for the significance of interactions relative to a well-defined model.

4. To build off the previous point, it strikes me as necessary to actually establish that inter-specific strain correlations are actually meaningfully stronger than species correlations, rather than just stronger. Are 76% of strain couplings significantly stronger than the corresponding species abundance trajectories, or marginally so? It would be helpful if the authors could mention the effect sizes at play here

5. Additionally, I am confused as to why the correlation between species abundance trajectories is not simply a weighted average of the respective strain abundance correlations.

6. I would argue that the model outlined in the Methods, which is used to build the interaction network is not a “neutral” model (line 664), as the authors state. Rather, it is an ecological null model.

7. Could the reason that strain abundances appear more “dynamic” have something to do with the relatively greater strength of sampling noise within vs. between species? I would imagine that there could be greater variance in strain abundances/differences in correlations due to the fact that species abundances/correlations were measured using 16S and strain dynamics were measured with shotgun reads. Why not standardize everything with shotgun reads? Species abundances can be estimated using shotgun reads, as well. This strikes me as a potentially important source of technical noise.

Reviewer #3 (Recommendations for the authors):

– Please explain in the main manuscript (i) how sensitive the statistical approach used is to also detect positively or negatively coupled oscillations with or without a time-lag between strains, (ii) how robust the conclusion are if these patterns remain undetected, and (iii) if the correlational analysis would allow to identify also higher-order interactions (i.e. beyond pairwise, including dynamics resulting from >3 way interactions).

– I do not fully understand the importance of pseudogenization for this study. The statement in Line 386 about deactivation of genes that do not contribute to fitness is very general and I would expect this phenomenon to be independent of strain-level differentiation. Therefore, also the conclusion in Line 388, that non-functional pseudogenization contributes to strain-specific interactions is not fully clear. Please clarify.

– I would like to suggest the following (new) title to better reflect the main finding of the study: „Strain-level rather than species-level differences govern eco-evolutionary dynamics in microbial communities”.

– The authors ask what SNPs lead to a decoupling of strains. However, would it also be possible to define a set of genes that lead to coupling? For example, can some metabolic interactions (cross-feeding, competition, etc.) be inferred from strains that showed coupling? This would significantly enhance the manuscript, because it would provide a mechanistic explanation for the observed pattern.
