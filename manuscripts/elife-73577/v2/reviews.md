# Peer review - Round 1

Editors:
- Virginie Courtier-Orgogozo, Université Paris-Diderot CNRS France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73577.sa0](https://doi.org/10.7554/eLife.73577.sa0)

Bergeron et al. show that mutation rate independently estimated by several teams with the same pedigree dataset can be different due to the methods and approaches used to identify de novo mutations. This result is of primary importance because it shows the necessity to have standard mutation identification methods and the difficulties to compare mutation rates from different studies.


---

# Peer review - Round 1

Editors:
- Virginie Courtier-Orgogozo, Université Paris-Diderot CNRS France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73577.sa1](https://doi.org/10.7554/eLife.73577.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Mutationathon: towards standardization in estimates of pedigree-based germline mutation rates" for consideration by eLife. We are sorry for the long review process. Given the long list of authors, it was difficult for us to find reviewers with no conflict of interest. Your article has now been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and George Perry as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Aaron R. Quinlan (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The authors should address issues or add discussion on de novo mutations calling in multi-sibling families, based on multi-generational pedigrees or on multiple tissues, the cellular processes causing germline de novo mutations which can vary between species, and the effect of the tissue on somatic mutation contamination, that could require adjustments in the method. Furthermore, the authors should discuss the fact that there is no sampling error at play in the mutationathon, since all teams used the same input data.

Since a gold standard approach is not achievable, the authors may want to revise the title.

Finally, the text should be made more accessible to a broad audience.

Reviewer #1 (Recommendations for the authors):

Page 16 line 428-429:

According to the authors, the multiple nucleotide mutations (MNM) are removed from most of studies because believed to be false. But some elements also seem to show that this type of MNM are possible, in example when replication-transcription machineries overlap. Do the authors have any example of MNM tested by PCR in any cited study? This could help to choose between keep or discard. If necessary, see for example CurrBiol. 2011 Jun 21;21(12):1051-4. doi: 10.1016/j.cub.2011.05.013.

Page 23 lines 611-630.

The exact value of µ is provided only for two teams (TT and RW). Can the authors also add the exact values of µ from other teams somewhere?

Page 25:

The table 2 looks uncomplete to me, is there MQ different threshold between the teams that need to be mentioned?

Page 30 line 754:

1) The authors should add a table (even in supplementary) with all mutation candidates, indicating

Chromosome position ref alt team true/false (and other relevant information at their discretion). Maybe the low complexity region led to higher rate of mutation identification candidates, where the 5 teams have so many different mutation candidates, with only 7 true shared. Complexity around mutation candidate positions may be addressed by several methods (see https://doi.org/10.1093/molbev/msab140). This point can be to the benchmarks at the end of page 30 if relevant.

2) For me, an important implication of this study is the mutation spectrum. The 5 mutations rates estimates are of the same order (one is still high), but the mutation candidates between the teams differ. This means that an analysis of the mutation spectrum and intragenomic mutation rate variation between the teams can be different, more significantly than the difference in mutation rate itself: AT bias, insertion/deletion, chromosome mutation rate, and so one. I highly encourage the authors to realize a later study exploring in detail the benchmarks proposed at the end of page 30.

Reviewer #2 (Recommendations for the authors):

I had couple of suggestions:

It would be very useful to introduce a site-specific error rate parameter at least for the human data.

Also it would be interesting if the authors can use some of their suggested parameters: alignment, variant calling and post-filtering on some of the available data to show how their guidelines may improve the mutation rate estimate.

Reviewer #3 (Recommendations for the authors):

Assessing the variability of germline mutation rates predicted from each pipeline via application to more (e.g.) pedigrees would be informative.

LCRs on line 434 refer to low-complexity regions identified by Heng Li as drivers of false-positive variant predictions.

The color scheme in Figure 3B will be difficult for the color blind.

Figure 3C is difficult to parse. Perhaps consider an "Upset" plot.

Do the GQ filters discussed on lines 670-674 apply to each member of the pedigree? That is, is GQ>=20 applied to the genotype for each macaque at each site?

Figure 5 is very difficult to read. Please make the axis labels larger. You may be able to also make the figure more legible by packing the bars more tightly so as to waste less whitespace.

The manuscript is often difficult to read with all of the VCF acronyms used to describe the filtering logic applied. While decipherable for those familiar with the "joys" of VCF, you might consider a more accessible approach for a broader audience.
