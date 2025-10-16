# Author response - Round 1

Authors:
- Rafal Donczew ([ORCID: 0000-0001-9729-4153](https://orcid.org/0000-0001-9729-4153))
- Steven Hahn ([ORCID: 0000-0001-7240-2533](https://orcid.org/0000-0001-7240-2533))

## Response text

DOI: [10.7554/eLife.69619.sa2](https://doi.org/10.7554/eLife.69619.sa2)

Essential revisions:

1) The authors should clarify what is meant by "processive elongation" and how their data support this key conclusion. The data in Figure 6B indicate decreasing RNA Pol II occupancy over about the first 300 bp in 3 of the 5 classes of genes, but then the effect plateaus. This observation does not fit well with either a role in release of pausing (expected to be more limited to the region near the TSS) or general processivity (expected to occur across the entire length of the genes). The traveling ratio does not seem well suited to measure this as it only takes account of the initial and final occupancies, but the authors have the data needed to ask about processivity across the genes that could answer this question more completely.

Thank you for the insightful comments. The following answer also relates to point 7:

We agree that the term 'processive elongation' was not a good description of the defects in transcription elongation caused by Bdf depletion. We changed it to 'early elongation' since the detected changes occur in the first 300-400 bp from TSS. As noted by the Reviewers, this observation does not fit with the pause release model observed in metazoans or with general changes in Pol II processivity. Interestingly, the Pugh lab recently reported that acute stress in S. cerevisiae causes Pol II stalling (Badjatia et al., 2021) at the +2 nucleosome, and suggested a regulatory elongation checkpoint. This stalling region overlaps the region where we find elongation defects in the absence of Bdfs. This connection is now discussed on lines 463-466, pg 14.

We performed additional analysis of the data collected for Bur1, Ctk1 and Spt5. We found that the major accumulation of Bur1 and Ctk1 occurs over the first ~400 bp and anti-correlates with changes in Pol II, i.e., most Bdf-dependent genes experience the biggest loss of Pol II and the biggest increase in relative Bur1 and Ctk1 occupancy (Figure 6G). This result is counterintuitive considering the loss of Ser2 phosphorylation. Human BET factors Brd2 and Brd4 were claimed to have kinase activity and Brd4 was directly connected to Ser2 phosphorylation independently of P-TEFb (Denis and Green, 1996; Devaiah et al., 2012). Similarly, Bdf1 was also reported to have an intrinsic kinase activity (Matangkasombut et al., 2000). This possible Bdf1 kinase activity would explain the observed defects and we plan to investigate it in the future work.

At this point, we don't know what drives the increase in Bur1 and Ctk1 occupancy in relation to the Rpb1. We introduced a separate paragraph to the Results section (pg 11) where results related to Bur1, Ctk1 and Spt5 are presented (lines 374-397). Relevant changes were also made in the Discussion (lines 478-487, pg 15).

Finally, we believe that the travelling ratio calculated as the ratio of Pol II at TSS and TES is a useful metric to quantify the observed changes in Pol II distributions at individual genes. To validate our approach, we calculated Pol II signal at other locations along the transcribed regions and related it to signal at TSS. Starting at ~400 bp from TSS the results were very similar and supported our conclusions based on calculation at TES.

2) What is the relative contribution of Bdf1 and Bdf2 to the elongation function?

In the presence of Bdf1, the contribution of Bdf2 to transcription is minimal as shown in Figure 1. Depletion of Bdf1 in the presence of Bdf2 gives a modest defect in transcription and only the simultaneous depletion of Bdf1/2 causes a strong defect. For these reasons all experiments using ChEC-seq and ChIP-seq were based on depletion of both Bdf factors to maximize the observed defects. We expect that, similarly to results measured by 4-thioU RNA-seq, the contribution of Bdf2 to elongation function is small and it would be hard to capture differences in Rpb1 distribution if the Pol II ChIP-seq experiment was based on only Bdf2 depletion.

3) Do Bdf1 and Bdf2 effects on initiation correlate with the effect on elongation at the same genes? This is alluded to in the Discussion but not analyzed in the Results.

To clarify this point, we added Figure 6—figure supplement 2C, which compares the change in TFIIB binding with the change in travelling ratio. The correlation is weak and suggests that, at many genes, the relative contributions of Bdf1/2 to initiation and elongation can be significantly different. Corresponding changes were made in the manuscript (lines 352-353; pg 11).

4) The change in transcription noted upon Brd1/2 depletion in Figure S3C is surprisingly similar for genes with and without scored Bdf1 peaks. While the difference is noted to be statistically significant, the absolute change does not appear to be likely to be physiologically important. Do the authors think this means there are indirect effects of Brd1/2 on all genes, that there is a problem comparing the 4-thioU-seq data with CHEC-seq data, or do they have some other explanation? Perhaps comparing continuous occupancy values (the data in Figure S3D, for example) instead of binary peak calls would resolve this puzzling observation?

Thank you for the comment. Following the suggestion, we replaced Figure S3D with a scatter plot (now Figure 2—figure supplement 1C), which compares the loss of transcription after depleting Bdf1/2 with the Bdf1 promoter signal calculated in a fixed window for all 4883 genes analyzed by RNA-seq. The gene dependence on Bdfs shows a relatively weak correlation with Bdf1 promoter occupancy. Similar findings were reported for the human BET factors. In Winter et al., (2017) BRD4 enhancer occupancy has limited capacity to predict gene response to BET degradation. Similarly, Muhar et al. (2018), found that BRD4 occupancy did not predict gene response to JQ1 treatment. Corresponding changes were made in the manuscript (lines 211-214; p7).

5) Similarly, Figure 2D shows statistical significance for the difference in histone acetylation for genes with and without Bdf1 peak calls, but the absolute difference seems small. The authors should discuss why histone acetylation is less of a driver of occupancy than expected for bromodomain factors.

Thank you for the comment. We modified the manuscript in lines 269 – 274 (pg 9) where we discuss possible alternative targeting mechanism for Bdfs including interactions of Bdf1 with acetyl lysines on histone H3 and reference examples of human BET factors interacting with other transcription factors in a bromodomain-independent manner. For example, the conserved ET domain seems to be a frequent point of contact with protein partners. It is possible that the Bdf1 ET domain is similarly involved in interactions with non-histones proteins and such interactions can provide alternative means of recruitment of Bdf1 to chromatin.

6) The conclusion that Bdf1/2 have roles independent of TFIID relies on similar kinetics and extents of depletion of the Bdfs and Taf1/Taf13 but this is not shown here.

Thank you for the suggestion. We compared the kinetics of Bdf1 and Taf1/Taf13 degradation by Western blot. The results shown in Figure 1—figure supplement 2A validate that the degradation of Bdf1 (both alone or in combination with bdf2 deletion) is comparable to Taf1 and Taf13 degradation at time points before, during and after the 30 minute depletion time used for our RNA analysis. Corresponding change was made in the manuscript (line 142-143; pg 5).

7) The authors interpret Ser2 phosphorylation as a marker for release of pausing, but the roles of P-TEFb on DSIF, NELF, and other factors seem more firmly established, so this interpretation needs to be explained more completely. Perhaps related to this and to point 1, the authors should also discuss the increased occupancy by Ctk1 and Bur1, as this might indicate failure to perform a transition between initiation and elongation, leading to elevated accumulation of the enzymes that participate in promoting it. Does the primary data suggest accumulation of Ctk1 and Bur1 over the promoter as seen with RNA Pol II, or is it found throughout the gene bodies?

Thank you for the comments. We changed the manuscript to include information about phosphorylation of NELF and DSIF. Our answer to the question regarding Bur1 and Ctk1 is included in the response to the point 1 above and includes additional data analysis now shown in Figure 6G and in Figure 6—figure supplement 3.
