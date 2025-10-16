# Peer review - Round 1

Editors:
- Philipp W Messer, Cornell University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70242.sa0](https://doi.org/10.7554/eLife.70242.sa0)

This paper studies the evolution of herbicide resistance in Amaranthus tuberculatus, a widespread agricultural weed. By illuminating how adaptive mutations arose and spread in this remarkable example of rapid human-induced adaptation, the study will be of interest to a broad audience, ranging from plant biologists interested in herbicide resistance to evolutionary biologists and population geneticists studying the fundamental factors and processes that govern rapid adaptation. The paper applies innovative population genetic methodology to support its primary finding that resistance mutations have evolved multiple times in parallel.


---

# Peer review - Round 1

Editors:
- Philipp W Messer, Cornell University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70242.sa1](https://doi.org/10.7554/eLife.70242.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Repeated origins, gene flow, and allelic interactions of herbicide resistance mutations in a widespread agricultural weed" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, including Philipp W Messer as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Molly Przeworski as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Pleuni S Pennings (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Both reviewers agree that this paper is interesting and should warrant publication in eLife, assuming that the authors can perform the following essential revisions. These points are laid out in more detail in the "recommendations for the authors" sections below.

1) Please add a discussion of what the results mean for preventing resistance in weeds, as pointed out by reviewer 2.

2) Reviewer 1 had some concerns about the robustness of ARG inferences to potential phasing errors. This should be discussed in more detail. Similarly, it should be tested whether results are robust to potential misspecification of the recombination rate at the resistance loci.

3) Please follow the suggestions provided by reviewer 2 regarding the analyses shown in Figure 2. It might be helpful to show the actual haplotypes.

4) Given that the finding of the recent population expansion is critical for the interpretation of allele ages, and therefore the question of whether adaptation occurred from SGV or de novo mutations, it would be reassuring if this result could be confirmed with a different inference method such as DaDi, stairway plot, or SMC++. If not possible, or if results are inconsistent, the claims about allele ages and sweep origins would need to be qualified accordingly.

5) Both reviewers were not entirely convinced by the finding of possible haplotype competition. Please clarify more precisely what you mean by interference / competition / etc. It should also be made more clear what the null expectation here is; for example, how often would ALS574 and ALS 653 be expected to occur together on the same haplotype in a model of free recombination?

Reviewer #1 (Recommendations for the authors):

The need for phased data for all RELATE, ARGweaver, and selection scan analyses raises some concerns about how potential phasing errors could affect the results. I feel the authors should at least discuss this. Ideally, additional analyses would be performed to test for such effects explicitly, although it is not clear to this reviewer what the most appropriate model would be. Maybe respective analyses were already performed in the papers that introduced the methods, in which case those results could simply be discussed here.

The recombination rate inference with LDhat could also be problematic at the resistance loci due to the presumably strong selection these loci have experienced, which may have affected LD patterns significantly. If, for example, sweeps have led to substantially elevated levels of linkage disequilibrium at these loci, LDhat would presumably interpret this as a lower recombination rate. My suggestion would be to run potentially affected analyses at the sweep loci not only with the recombination map inferred by LDhat, but also scenarios with a constant recombination rate set to a range of values, in order to test how robust the results would be to potential recombination rate misspecification.

The results from the demographic inference are intriguing and also play an important role for the interpretation of the results, as they provide the basis for the rescaling used to estimate both the population-level adaptive mutation rate and allele ages. If there would be a substantial error in the estimate of the recent effective population size, interpretations about adaptation from de novo mutation versus standing genetic variation could change quite dramatically. The demographic inference is currently based on the RELATE method. I wonder whether the authors have considered confirming these results with alternative methods to check how robust they are between different methods. For example, it would be interesting to compare this with SFS-based methods such as stairway plot and DaDi, or hybrid approaches such as SMC++. If the results from different methods agree, this would greatly increase trust in their accuracy. By contrast, if there are large discrepancies, possible reasons for this and potential implications for the interpretation of results would need to be discussed.

The arguably most speculative part of this study are the results on negative LD between common resistance mutations, which is interpreted by the authors as being caused by either haplotype competition, negative epistasis, or selective interference. Again, phasing could be somewhat problematic here. Maybe there are enough homozygotes in the data set that the authors could at least confirm that some of the findings hold even for unphased data? Also, I'm concerned that unknown population structure could potentially play into these results. This would be difficult to test, obviously, given that it's unclear what models one should test specifically. However, one question that I think could be more easily answered is how likely it is to find such negative LD at other genomic loci. Are the resistance loci truly genomic outliers in this regard? I hope the authors can add some discussion about whether they think population structure may or may not provide a potential alternative explanation for the observed negative LD.

Reviewer #2 (Recommendations for the authors):

I think this is a super interesting paper. It shows evidence for multiple origins (9) of drug resistance and also widespread migration (transmission) of resistance alleles between local populations. That in and of itself is worth publishing for me.

I feel like what is missing from the paper is a discussion of what these results mean for preventing resistance in weeds. I think that it means that when we want to prevent resistance, we need to be concerned with preventing mutation (control pop size / selection locally) and we need to be concerned with gene flow between populations (do not share equipment and staff?). I think the paper could benefit from more translation of the results to a non-evolutionary genetics audience. I also would love to see more easy-to-digest information about the relevant herbicides and the weed itself. This way, you can make the paper more interesting for evolutionary geneticists who have never thought about herbicide resistance and you can introduce those who are interested in plants and agriculture to evolutionary genetics.

In my opinion, some major improvements could be made to the presentation. Part of that is eye for detail in figures (e.g., use same colors and same notation throughout) and text (e.g., line 118 why mention psbA here, but nowhere else? Line 126 why mention glyphosate here? These things make the text hard to follow.…).

Some of the analysis on allele ages / evidence of recent selection should be presented differently before I am convinced.

The same is true for the analysis on clonal interference. This should start with clarifying what is meant by interference / competition / etc.

Instead of TSR I would write "resistance allele" – I think that will help other readers.

Figure 1: could Figure 1 be remade using the origins from Figure 2? Once you know that there are multiple origins, doing an analysis that ignores these origins doesn't make too much sense, I think. Can you use the same nomenclature as Table 1 and Figure 2?

Figure 2:

1. First, use ARG to find origins. Conclusion: there are multiple origins!

2. Then plot origins and fractions on a map. Conclusion: there is migration as well, though not panmixia (would it make sense to test that?).

3. Finally test for recent selection. Here I would love to see some kind of strength of selection statistic rather than just p-value.

For one allele there is evidence for recent selection, but not selection since origin (right?) – ALS 574#4. Could you show a zoom in for the tree with the 0.02% cut-off for that allele?

Conclusion of figure 2: multiple origins and gene flow are both important. For some alleles evidence that there has been selection since origin – suggests de novo evolution of resistance. But for some possibly standing genetic variation? I am not so convinced of that part of the analysis. Maybe it'd help to show haplotypes?

Suggestion: can you show haplotypes (like Harpak et al. on rats or Garud et al. on Drosophila or Williams and Pennings on HIV?)

Please label MidWest and Ontario. Could the pies have the same scale in the two regions?

Suggestion: Use the same color and nomenclature scheme throughout. For example, the 653_7 origin should have that name and color throughout the figure and other figures.

Figure 3:

The increase in pop size is clear and not surprising.

The allele ages are interesting. Could they be plotted?

I am not convinced that there is evidence for SGV for 653#7, because its age is only about 30 years according to the figure. 3B and 2C are hard to reconcile in my head.

Figure 4:

This is about interactions between ALS574 and ALS 653. These are 300-ish bp apart.

The resistance mutations never occur on the same haplotype which is surprising (how surprising? Could we get a prediction for how common this should have been if there was free recombination given the age of the alleles?).

Now, I'd say the next question is: how often do they occur in the same individual, given their commonality in each population. Like a HW-test. Is there selection against carrying two resistance alleles?

I am not entirely convinced that there is evidence for competition. Or maybe it is not clear to me what the authors mean exactly by competition / interference.

I am not sure my brain can follow Figure 4A – what would be the expectation here given multiple origins at both loci?
