# Author response - Round 1

Authors:
- Anna M Scarborough ([ORCID: 0000-0003-3621-234X](https://orcid.org/0000-0003-3621-234X))
- Juliana N Flaherty ([ORCID: 0000-0002-9745-6762](https://orcid.org/0000-0002-9745-6762))
- Olga V Hunter
- Kuanqing Liu
- Ashwani Kumar
- Chao Xing ([ORCID: 0000-0002-1838-0502](https://orcid.org/0000-0002-1838-0502))
- Benjamin P Tu ([ORCID: 0000-0001-5545-9183](https://orcid.org/0000-0001-5545-9183))
- Nicholas K Conrad ([ORCID: 0000-0002-8562-0895](https://orcid.org/0000-0002-8562-0895))

## Response text

DOI: [10.7554/eLife.64930.sa2](https://doi.org/10.7554/eLife.64930.sa2)

Essential revisions:

Two main themes emerged from the discussion among the reviewers: 1) concern about the reporter as displaying a readout that is splicing dependent; 2) the desire for additional experimental support and discussion of the model presented in Figure 7. As such, the reviewers suggest the following be addressed:

1. Provide additional controls to convince the reader that the GFP reporter expression is truly dependent on its splicing efficiency. Both Reviewers 1 and 2 provide more granular suggestions on how to potentially do this below.

The reviewer’s fairly point out that several shortcomings of our GFP reporter obscured whether the regulation by CFIm25 is due to splicing activity or to changes in RNA stability. These concerns were based primarily on three results: 1) We did not observe the detained intron isoform (GFP-DI) in our northern blots, so it was questionable whether it was even regulated by intron detention, 2) the reporter spliced in an unexpected pattern (Figure 1—figure supplement 1), and 3) we did not exclude potential roles of CFIm25 in hp2-6 regulation of mRNA stability. We have developed two new reagents that we think rigorously address these concerns and strongly support the conclusion that the GFP reporters (and MAT2A) are regulated by CFIm25 at the level of splicing of the detained intron.

First, we have improved the quality of our northern blot GFP probe. In the previous version of the manuscript, we mentioned that we could not visualize the isoform of GFP containing the detained intron (GFP-DI). In fact, we did not even observe the mRNA except under inducing (-methionine) conditions (see Figure 1D and Figure 1E). Since then, we designed a significantly improved GFP probe that detects both isoforms of our reporter (revised Figure 2B and Figure 2—figure supplement 1). To improve the signal-to-noise in the assay even more, we also added a poly(A)-selection step to our northern blot validation experiments in Figure 2B-2E and Figure 2—figure supplement 1. To address Reviewer #1’s concern regarding quantification, we included quantification of these data not only as %DI, but also as relative levels of each of the isoforms (Figure 2C-2E). Using the original reporter, we see concomitant decreases of mRNA with increases in the GFP-DI isoform upon knockdown of METTL16 or CFIm25. These observations support the proposed roles of CFIm25 and METTL16 in the regulation of splicing of the detained intron of the reporter used in the CRISPR screen.

We have kept the data with the old probe in Figures 1D and 1E. We could repeat those experiments with the new GFP probe to produce a cleaner result, but that seems misleading since our screen was rationalized based on those data.

Second, we have included data from a modified reporter recently developed in the lab (revised Figure 2A, bottom diagram). The reporter is effectively the same as the one used previously except for two changes. This reporter includes a T2A “self-cleaving” peptide between the GFP and the β-globin MAT2A fusions for better protein stability. (The stability issue was described in the original version and remains in the revised Results section and Figure 1—figure supplement 1.) However, the relevant change for the current paper is that the new reporter has hp2-6 mutated, so it is not subject to regulation by hp2-6-mediated RNA stability. Using this reporter (T2A, hp2-6m9), we observed diminished GFP mRNA levels and increased GFP-DI accumulation upon depletion of METTL16 or CFIm25 (Figure 2A-E; Figure 2—figure supplement 1). A similar response was observed with two independently derived integrated clonal cell lines (Figure 2B-E and Figure 2—figure supplement 1). This observation excludes the possibility that the CFIm25 regulation is hp2-6 dependent and is consistent with a role for these factors in splicing of the MAT2A detained intron in the GFP reporter.

As a side note, careful inspection of the northern blots in revised Figure 2B show that the new T2A, hp2-6m9 reporter mRNA is slightly longer and the detained intron isoform is slightly shorter than the original “Reporter” counterparts. These patterns are consistent with the fact that the new reporter lines’ splicing patterns reflect the “predicted” pattern discussed in Figure 1—figure supplement 1, while the original reporter is distinct as previously reported. Thus, the effects of CFIm25 on the reporter is not specific to the unique splicing pattern in the original reporter.

With these new data, we have specifically demonstrated that CFIm25-mediated regulation of our MAT2A reporter does not require hp2-6. Conversely, both the initial submission and the revised version of the paper include data from the 116-ΔDI line that demonstrates that CFIm25 regulation of the endogenous MAT2A requires the detained intron (Figure 3A-3C; Figure 3—figure supplement 1A). Since hp2-6 are not required for CFIm25 regulation but the detained intron is, these data strongly support the conclusion that the effect of CFIm25 on GFP mRNA accumulation is due to a novel role for CFIm25 in splicing of the MAT2A detained intron.

2. Figure 7A makes two predictions: (1) the UGUU and UGUA reporters in Figure 4G, but not the UGCU, should be responsive to CFIm25 knockdown and (2) co-depletion of CFIm25 and METTL16 should not have a bigger impact on the splicing of the endogenous MAT2A than depletion of CFIm25 alone. Both of these predictions are readily tested with the reagents at hand and therefore should be done.

These are excellent suggestions, and we have included both of these experiments in the revised manuscript. To address the second point first, we have now included METTL16/CFIm25 co-depletion experiments in revised Figure 2H. As predicted by the model, there is no synergistic/additive effect after co-depletion of both CFIm25 and METTL16 on endogenous MAT2A RNA isoforms.

We also include the requested experiment with the mutant reporters in revised Figure 4—figure supplement 1. As predicted by the reviewer, the UGUA reporter responds similarly to wild-type upon either CFIm25 or METTL16 knockdown, but the UGCU is unaffected. However, there is an important technical caveat regarding the behavior of the UGCU mutant. In our hands, siRNA knockdowns are considerably more efficient in the 293A derivative line 293A-TOA than in HEK293 cells. The latter were used for the reporter experiments in Figure 4, but since the requested experiments required knockdown, we used 293A-TOA cells for the requested experiments. However, 293A-TOA cells show a much higher baseline intron detention than HEK293 cells. As with many alternative splicing events, we find considerable variability in intron retention patterns with both endogenous and reporter RNAs in different cell lines (e.g. Park et al. Cell Reports 2017). In the case that the counter-hypothesis were true (i.e. siCFIm25 has additive effects with UGCU), we would not be able to see this change because there is little dynamic range to increase intron retention. Therefore, these data remain largely inconclusive on this issue. These caveats are included in the legend to Figure 4—figure supplement 1.

3. Modify language in the discussion as described by Reviewer 3.

We have updated the Discussion to include the points raised by Reviewer #3.
