# Peer review - Round 1

Editors:
- Sarah E Cobey, University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68917.sa1](https://doi.org/10.7554/eLife.68917.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This paper provides important observations and insights on the within-host evolution of seasonal influenza, particularly H3N2 in children. As in adults, H3N2 appears to evolve largely by purifying selection during the initial stages of infection when transmission is likely to occur, and nonsynonymous mutations accumulate later. The authors propose a model of mutation-selection balance that might explain diversity in young children with longer infections.

Decision letter after peer review:

Thank you for submitting your article "Within-host evolutionary dynamics of seasonal and pandemic human influenza A viruses in young children" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Miles Davenport as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

This study adds to our knowledge of the evolutionary dynamics of influenza within hosts. The longitudinal data – from likely primary H3N2 infections in children and infections with emerging H1N1pdm09 – are interesting, and the evolutionary analysis has laudably broad scope. That said, the reviewers agreed that limitations in both the data and analysis cast doubt on the conclusions. More analysis could strengthen the study. After consultation, our major concerns are that:

1. Not enough attention is given to potential errors affecting the sequences. Reviewers discussed both systematic sequencing and random PCR errors. Ideally plasmid controls would have been used, but under the circumstances, we suggest the authors instead perform sensitivity analysis and other checks recommended by Reviewers 2 and 3.

2. The temporal trends are not analyzed in a statistically careful way. Reviewers 1 and 3 raised concerns about the trends reported in Figure 2. (Are they really there?) This affects the general conclusions about H1N1pdm09 v. H3N2.

3. The simulations assume an odd distribution of fitness effects, which might skew the conclusions about the evolutionary regimes of the two subtypes. (It is not unclear why they should have contrasting evolutionary dynamics.) More thorough sensitivity analysis could help here.

The essential revisions would address these concerns. The reviewers were also in agreement on their more specific comments, which I hope you can use to strengthen the work.

Reviewer #1 (Recommendations for the authors):

My primary suggestion is effectively to clarify the statistics for the temporal trends. For instance, in Figure 2, do the p-values test for NS and S being significantly distinct from each other within a time point or gene or between time points/genes? I initially thought the latter given the claims in the text about temporal dynamics. I believe more tests are needed for these claims, not only for H1N1pdm09 (ll. 180-182). This will influence the comparison with simulation output. The Discussion might then also need updating (ll. 474-477).

Reviewer #2 (Recommendations for the authors):

Figure 1 figure supplement 2 appears to show variants present at reported frequencies that where not in all overlapping amplicons. These could be PCR artifacts or potentially real variants that were missed in one of the amplicons. Are the evolutionary rate dynamics driven by variants in this frequency range? Is there enough signal to filter out similar variants and validate the robustness of the findings?

Line 205: It is not clear how the frequency of synonymous mutations, by themselves indicates negative selection in the antigenic sites. What is the importance of the higher frequency of synonymous mutations found in antigenic sites?

Line 663: How were overlapping reading frames accounted for in the evolutionary rate calculation?

The qualitative similarity between the simulated and observed rates is nice addition to the manuscript. Is it possible to use the frequencies of mutations in longitudinal pairs to further support the hypothesis of mutational-selection balance?

Reviewer #3 (Recommendations for the authors):

1. The authors identify and analyze several recurrent mutations in the H3N2 M2 and NP genes, which were found in anywhere from 16 to 27 unlinked individuals. They argue that the recurrent NP mutation is a stabilizing mutation and is epistatically linked to several co-variants that may have destabilizing effects (Figure 5). I am concerned that these mutations may result from technical artifacts and may not represent genuine within-host variants, particularly since amino-acid variants that are known to be associated with oseltamivir resistance were only identified in two patients despite the administration of oseltamivir in many patients. In data from McCrone et al., 2018, for example, several sites appear to harbor low-frequency variants in unrelated individuals, much like the authors describe here, but those variants are also present in the plasmid controls, suggesting that they represent common, site-specific polymerase errors rather than recurrent mutations.

To try to determine whether these variants are technical errors, the authors would ideally sequence plasmid controls using the same protocols that were used to sequence the original samples. Since this is likely infeasible, the authors should also check their data to see if variation is present at M2-77, NP-G384R, and other apparent sites of recurrent mutation at frequencies below the variant-calling threshold. If variation is present at these sites in most samples at a frequency much higher than in neighboring sites, then this variation may reflect technical errors in sequencing. The authors called variants after mapping reads to a reference genome, but they might also try remapping to the sample consensus sequence to reduce the risk that mapping artifacts are causing these recurrent variant calls.

2. The authors write that non-synonymous mutations accumulate later in patient infections, but it's not clear to me how strongly the data in Figure 2A supports that argument, particularly given the limited number of samples collected at any given day following symptom onset. Does nonsynonymous diversity tend to increase over time in successive timepoints collected from the same individual? Does noise in variant frequencies account for the apparent fluctuations in synonymous diversity over time, and if so, how does noise affect the interpretation of nonsynonymous diversity?

3. In the simulations of A/H1N1pdm09 in Figure 6A and 6B, the authors simulate a distribution of fitness effects in which 1% of nonsynonymous mutations are neutral and the remaining mutations are weakly (s=0.01) or strongly (s=0.1) beneficial (lines 785-6). This distribution of fitness effects seems unrealistic to me – even for an emerging virus that may be adapting to a new host, most nonsynonymous mutations will still be deleterious because they affect basic protein functions. It's not clear to me that the large increase in nonsynonymous diversity that the authors observe from these simulations would be observed if deleterious mutations were adequately accounted for; the distribution would probably look much more similar to Figures 6D and 6E.
