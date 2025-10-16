# Peer review - Round 1

Editors:
- Philipp W Messer, https://ror.org/05bnh6r87 Cornell University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81188.sa0](https://doi.org/10.7554/eLife.81188.sa0)

This important study investigates temporal variation in patterns of germline mutation during the evolution of human populations. Using a compelling approach that controls for the effects of selection and biased gene conversion the authors show that changes in generation time alone cannot explain the joint patterns observed for different mutation types, suggesting that other factors such as genetic modifiers or environmental exposures must have played a role as well. This work will be of broad interest to population geneticists and evolutionary biologists.


---

# Peer review - Round 1

Editors:
- Philipp W Messer, https://ror.org/05bnh6r87 Cornell University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.81188.sa1](https://doi.org/10.7554/eLife.81188.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Timing and causes of the evolution of the germline mutation spectrum in humans" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and George Perry as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Laurent Duret (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Both reviewers and the editor agree that this is an interesting piece of work. However, several additional controls are required to strengthen the robustness of the results (in particular regarding the possible impact of polarization errors – notably at CpGs, and regarding the reliability of Relate dating estimates). The specific analyses and revisions we would like to see are laid out in detail in the two reviews.

In addition, we had some concerns about the plausibility of the archaic introgression hypothesis for explaining why the ratio of T>C over T>G differs significantly in African samples compared to non-African samples among mutations that are estimated to be much older than the out-of-Africa migration. We wonder whether it would be possible to actually estimate what amount of introgression was needed to account for this signal. We realize that this might be tricky to answer since we don't know the precise mutational signature of the archaic species. But maybe the authors have some ideas. Alternatively, the authors should provide a more detailed discussion of the introgression hypothesis to make it more clear (and explain why ND10 and ND01 variants could behave differently from ND11 variants).

Reviewer #1 (Recommendations for the authors):

This manuscript reports very interesting observations, but several additional tests have to be done to check whether the African-specific variation in the ratio of T>C/T>G observed among old variants is real or if it might result from methodological artefacts.

Notably, it is not clear to me if the reported pattern is driven by variants that are specific to the African samples, or if it also observed among variants that are shared across populations (which would point to a problem in the dating of mutations). Furthermore, I suspect that polarization errors (notably at CpG sites) might be responsible for the reported pattern. My comments are developed below.

It is possible that I misunderstood something, but in any case, I think these points need to be clarified before this manuscript can be published. There are also several important points of the methodology that need to be explained in more detail. Finally, I included several other suggestions that might be helpful to improve the manuscript.

1. Shared vs private variants

As I understand, the authors first applied Relate to the entire the 1000 Genomes project dataset (N~2,500 individuals?? This should be indicated in the methods). Then, for each population, they inferred the mutation ages by splitting the Relate output genealogies into subtrees for each population and re-estimated the branch lengths to obtain the final mutation ages. Many variants are shared across populations. Thus, if I understood correctly, each shared variant has multiple age estimates (one per population in which the derived allele has been sampled), that can be considered as replicate estimates (in an ideal world, they should be the same, but they may differ because of limited signal in the data and of simplifying assumptions in the methods). What is not clear to me is how these shared variants were considered by the authors. Did they focus their analyses on variants that are private to each pop? Or did they include all shared variants in their analyses?

Given that they do not mention this point, I presume that they took this latter option. I guess that a large fraction of the old variants are shared across populations. For the sake of my demonstration, let us imagine an extreme case, where old variants (say >20,000 generations) would all be shared across human pops. Imagine that the T>C over T>G ratio changed abruptly 50,000 generations ago. In principle, the exact same shift should be detected at this epoch, whatever the present-day population analyzed. However, there is a large uncertainty around age estimates (in particular for old mutations), and if this uncertainty is larger in some populations than in others (e.g. due to pop demographic history), then the signal for this mutational change might differ, both in intensity and in estimated timing, across populations. Thus, this could potentially contribute to the reported differences in 'old' mutational patterns across populations.

To test this, the authors should repeat their analysis of the T>C over T>G ratio (Figure 2A), specifically on variants that are shared across the 3 pops considered [NB: the analysis of non-ND11 sites in Figure 2D suggests that their results are robust to this potential bias; however, I would prefer to see a direct test]. Conversely, the signal for an old shift in mutation pattern should be much stronger if they focus their analyses on variants that are private to each population. I think it would be really useful to present these two analyses so that we can understand the source of the pattern.

Moreover, to be able to evaluate the impact of the different variant filtering criteria that they use, I think it would be helpful to provide information on the number of SNPs analyzed in each panel of Figure 2 (and associated SupFigure 2.xx), and also on the proportion of shared/private SNPs per age bin.

2. Mutation polarization errors

To verify that the peculiar patterns of pop-specific T>C/T>G mutation ratio they observe in old alleles do not stem from inaccuracies in the polarization of ancestral and derived alleles, the authors repeated the analysis by determining the ancestral state on the basis of the chimpanzee reference genome.

Although the results are qualitatively similar (SupFigure 2.7A), I was surprised to see that they are quantitatively quite different: the difference in T>C/T>G ratio between African and non-African samples is much stronger when variants are polarized with the chimpanzee reference genome than when they are polarized with the '6-EPO human ancestral genome' (Figure 2A). Is it simply due to the fact that more SNPs can be polarized with the chimpanzee than with the EPO ancestral genome? (it would be useful to report sample sizes in these figures). If not, then this would imply that polarization errors do have an important impact on the observed pattern (which would weaken the conclusions of the authors).

To check that, the authors should repeat the analyses with a common set of SNPs (for which the ancestral state was inferred by both methods), and test to what extent the patterns differ according to the polarization method.

The authors should also provide information on how the '6-EPO human ancestral genome' was inferred (indicate the species included in the EPO alignment, and the principle of the method that was used to infer ancestral states), and how they used it. Notably, the EPO ancestral genome makes the distinction between sites for which the ancestral state is considered of 'high-confidence' (reported in upper case) or 'low-confidence' (lower case). Did the author use all sites, or only the high-confidence ones (this should be indicated in the Methods)? Does this make a difference if the analysis is restricted to low-confidence or high-confidence sites?

3. Mutations in CpG or non-CpG context

CpG sites are mutational hotspots and are therefore particularly prone to recurrent mutations and hence to polarization errors. The way the authors handled CpG mutation is not very well detailed. They wrote (line 141): 'we divided C>T SNPs into sub-types occurring in CpG and non-CpG contexts by considering the flanking base pair on either side of the variant'.

If I understand correctly, for the reverse mutation type (T>C), they did not distinguish CpG vs. non-CpG contexts. This implies that mis-polarized C>T CpG mutations are included in the dataset of T>C variants. I imagine that polarization errors may have an important impact on the inference of mutation age. If mis-polarized recent C>T CpG mutations tend to be inferred as old T>C mutations, then the difference in T>C/T>G old mutations observed between African and non-African might simply be due to differences in the total number of variants (and hence in the number of mis-polarized variants) across pops. NB: this would explain why the signal disappears when ND11 sites (which potentially correspond to polarization errors) are excluded – but not ND10 or ND01 (which are more likely to correspond to bona fide old mutations).

To check that, the authors should repeat their analyses of T>C/T>G ratio, after having excluded all variants that potentially arose in a CpG context (i.e. for which either the REF or the ALT allele is in a CpG context – whatever the inferred ancestral state).

4. gBGC

The authors carefully accounted for the possible confounding effects of gBGC. However, the way they explain this point in the results (lines 187 to 202) is unclear. They wrote (line 194 p. 5): "Assuming no systematic evolution in the relative rates of S>W mutations and W>S mutations and unbiased estimation of allele age under gBGC, we would expect similar fractions of S>W and W>S mutations across age bins". This statement is incorrect: if the genome is subject to gBGC, then the ratio W>S/S>W is expected to increase with alleles age; and if the genome is not subject to gBGC, then it does not make sense to refer to an 'unbiased estimation of allele age under gBGC'.

I would recommend the authors to reorganize this section :

1. State that because of gBGC, the relative proportion of W>S vs S>W variants is expected to increase with the age of alleles.

2. Accordingly, they observe an enrichment of W>S variants relative to S>W variants in older age bins (SupFigure 1.6). According to the gBGC model, this enrichment should be positively correlated with recombination rate. The authors have not performed this latter analysis, but I suggest they should; this would be a useful positive control of the signature of gBGC, that they can contrast with what they see in SupFigure 2.3 (where they checked that the patterns they observed are robust to variation in recombination rate, so that to exclude any bias that could be caused by gBGC).

3. Conclude that it is important to take gBGC into account.

To avoid biases that might be caused by gBGC, the authors computed ratios of mutation rates, for pairs of mutation types that are a priori expected to be either not affected by gBGC (C>G/T>A) or equally affected by gBGC (e.g. T>C/T>G). It should be noted however that the mismatch repair mechanisms underlying gBGC (which are not known yet) might act differently on different types of mismatches. For instance, in bacteria, the MutY Adenine DNA-glycosylase of the BER is more efficient on transversion than on transition mismatches (Tsai-Wu et al., 1992 doi: 10.1073/pnas.89.18.8779). In humans, gBGC is stronger on W:S heterozygous sites that are in a CpG context compared to non-CpGs (Halldorsson et al., 2019). It is therefore in principle possible that gBGC contributes to variation in the ratios T>C/T>G or C>T/C>A across age bins. The authors mention this point in their discussion (line 675), but I think it would be useful to mention it also in the result section.

To assess such possible effects, the authors checked that the patterns they observed are robust to variation in recombination rate (SupFigure 2.3). This control is essential, and this is the reason why I think it would be important to demonstrate the efficiency of this test by showing the signature of gBGC on W>S vs S>W variants (see above).

Reviewer #2 (Recommendations for the authors):

1. Line 595 says that the TCC signal "may not be specific to Europeans." It's probably worth strengthening this to note that we know it's also in South Asians and has been localized to the descendants of an ancient Anatolian population.

2. It's very interesting that the East Asian T>A enrichment appears as a robust signal given that the prior association of the Japanese T>A enrichment with the Anderson-Trocmé, et al. cell line artifact. Can the authors comment on whether they find evidence of an authentic enrichment in any of the sequence contexts previously associated with the cell line artifact?

3. In line 646, the authors mention that the deeply diverged Khoe-San lineage is a place where we might find ancient mutation spectrum differences. I believe Do, et al. Nature Genetics 2015 in fact did find a mutation spectrum difference between the San and other Africans.

4. I like the "implications" paragraph (lines 690-701) and agree that much more needs to be done to jointly model mutation spectrum evolution with demographic history. It'd be good to note that some work along these lines has already been reported in the original Relate paper as well as DeWitt, et al. 2021 and Speidel, et al. 2021, including evidence of the type of confounding the authors discuss.
