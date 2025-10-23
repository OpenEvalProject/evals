# Peer review - Round 1

Editors:
- Amy L Williams, Cornell University United States

Reviewers:
- Amy L Williams, Cornell University United States

## Review text

DOI: [10.7554/eLife.46922.026](https://doi.org/10.7554/eLife.46922.026)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Large, three-generation CEPH families reveal post-zygotic mosaicism and variability in germline mutation accumulation" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Amy Williams as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Mark McCarthy as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Sasani et al. present a study of 40 large multi-sibling, three-generation CEPH/Utah pedigrees with the aim of estimating the rate of de novo mutations (DNMs), analyzing variation in paternal age effects, and identifying germline mosaic DNMs with their associated mutational spectra. The number of families and the fact that the CEPH/Utah pedigrees are enriched with large numbers of children in the third generation enable a more detailed study of the paternal age effect and of germline mosaic DNMs than prior studies, which have primarily analyzed trios. The finding that the paternal age effect varies by more than an order of magnitude adds to the already complex picture of mutational dynamics and provides strong evidence in support of a prior finding of a two-fold difference based on three families (Rahbari et al.). The study design enables the division of germline mosaic variants into those that seem to have arisen very early in development – gonosomal variants – and those that arise after primordial germ cell specification (post-PGCS). The mutational spectra associated with post-PGCS DNMs differ from those of other DNMs, with some possible biological explanations proposed in the text.

Essential revisions:

Overall this paper is a solid contribution to the DNM literature, but there are a few additional analyses that will help ensure the findings are robust and enhance the information already presented, as outlined below.

1) Since this manuscript's main advance regarding variation in paternal age effect over the Rahbari et al. result is greater statistical power, more robust statistical analyses of this pattern would strengthen the paper. Figure 3 presents a commendable amount of raw data in a fairly clear way, yet the authors use only a simple ANOVA to test whether different families have different dependencies on paternal age. The supplement claims that this result cannot be an artifact of low sequencing coverage because regions covered by <12 reads are excluded from the denominator, but there still might be subtle differences in variant discovery power between e.g. regions covered by 12 reads and regions covered by 30 reads. To hedge against this, the authors can define the "callable genome" continuously (point 1 under "other questions and suggestions") or they can check whether mean read coverage appears to covary with mutation rates across individuals after filtering away the regions covered by <12 reads.

2) Another concern about paternal age effects is the extent to which outlier offspring may be driving the apparent rate variation across families. If the authors were to randomly sample half of the children from each family and run the analysis again, how much is the paternal age effect rank preserved? Alternatively, how much is the family rank ordering preserved if mutations are only called from a subset of the chromosomes?

3) A factor regarding paternal age effects that is only mentioned briefly alluded to late in the paper are the differences in the intercept between families (Figure 3C). Do either the intercept or slope vary with the number of F2 children? Is there any (anti-)correlation between slope and intercept? It would seem odd if the intercept strongly impacts the slope since a low per-year rate probably should not correlate with a high initial rate at younger ages.

4) Another analysis that is informative about the cellular stage at which mutations occurred is to examine, for mutations found in F1, what fraction of these are transmitted to F2s. Putative DNMs could in fact be present in blood but not in the germline, and the study design here makes it easy to identify the fraction of such DNMs. A complexity of this is the use of multi-sample genotype calling. Perhaps dividing the genotype calling into a set called using the P0 and F1 generations only and comparing the resulting DNMs to those found in F2s (with calling in everyone) would ensure that the set of DNMs aren't biased towards those also present in the germline of F1s.

5) In the additional data files, I could not find the age of all the individuals. It would be informative if the age information can be provided on the pedigree diagrams or as a separate files with identifiers.

6) Will the sequencing data generated here be posted to the SRA or dbGaP?

7) The authors state that "a gamete sampled from a younger father is more likely to possess a DNM that will recur in a future child." This doesn't seem correct as stated – every gamete should be equally likely to possess a DNM that will recur in a future child, independent of parental age. I believe what is meant is that a particular DNM sampled from the child of a young parent is more likely to be shared with a sibling than a DNM sampled from the child of an older parent.

Other questions and suggestions:

1) One concern is in defining a site as "callable", which is of course not strictly binary. It would be good to take sequencing depth into consideration when deciding callability. Ideally this would also factor into both the FPR and MHR values. Given the three-generation study design, there is a greater opportunity to perform these analyses in a more detailed manner than in trio studies and thus to better estimate/model these rates.

2) Another factor to analyze is the use of multi-sample genotype calling and its potential to bias against the identification of non-mosaic (singleton) DNMs. Perhaps the 60x vs. 30x analysis can help estimate the rates of missing singletons in a way that is distinct from the MHR analysis.

3) What is the range of the MHR? Is there significant variation with respect to MHR among families (in cases where P0 were genotyped)? Moreover, is there any enrichment or biases in mutational spectra seen using the MHR?

4) The authors mentioned that they have removed DNMs with likely "DNM carriers" in the cohort. Does this remove DNMs where the alternate alleles are observed in only the unrelated individuals or does it also include the related individuals?

5) Other things to explore further related to parental age effects are: how do the conclusions change and/or can you detect similar variability in maternal age when analyzing phased DNMs? This may be underpowered, but for those families that share grandparents, if two brothers are in the F1 generation, do their paternal age effects differ?

6) For the parental age effect model the authors have correctly included "family-id", but for the rest of their analysis they have defined a "family" as the unique group of two F1 parents and their F2 offspring (e.g., Figure 3—figure supplement 1). Can the authors comment whether this might introduce biases in their analysis and filtering strategies, as some families are more related to each other than the rest?

7) Figure 4 shows that the number of DNMs shared with siblings does not appear to correlate with paternal age. Although it is seems unlikely to affect the result, it seems odd to report these as raw counts without correcting for the number of siblings the child has. It would be good to report the strength of the correlation between family size and shared DNM count and correct the shared counts for family size before testing for a correlation with paternal age.

8) Why, from Figure 4B, are the differences in mutational spectra found in the post-PGCS mosaic analysis only based on 289/721 of these DNMs (presumably the phased ones)?

9) A minor but important consideration here is as a term, "post-PGCS", seems to include any mutations that arise following the establishment of the germ cells, but what seems to be the intended meaning is those mutations that arise during germ cell proliferation (or related). Rewording would aid understanding here.

10) For the mutational spectra analysis of gonosomal mosaic DNMs, this and other similar analyses consider each allelic class independently. Would power increase by analyzing the data as a whole using, say, a Chi-squared six degree of freedom test?

11) The authors have applied the same filters as DNMs for identifying post-PGCS mosaic variants. They seem to have filtered candidates based on VAF > 0.2. Might this filter may be too stringent for identifying the post-PGCS events?

12) To identify gonosomal mutations the authors have applied hard VAF cut off < 0.2, considering the number of cell divisions before PGC, would this threshold be a bit too low? Would their observation change significantly if they change the threshold to <0.3?

13) What is the VAF distribution of candidate gonosomal mutations in F2? One of the filters they have used have VAF >=0.3 in F2. Might this threshold be too lax? For the gonosomal mutations that occur in F1, an expectation of a higher VAF of almost 0.5 in the F2 set seems reasonable.

14) In mosaic post-PGCS analysis: the authors have identified 32 events with supporting alleles in F1. Among these 32 mutations, do any occur in families were F1s are related? For example, do F1 19_A mom and 19_B dad share some of these mosaic mutations? If so is there any correlation in mutational burden in F1 with the age of P0?
