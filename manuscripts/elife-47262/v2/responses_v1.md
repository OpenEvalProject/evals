# Author response - Round 1

Authors:
- M Florencia Camus ([ORCID: 0000-0003-0626-6865](https://orcid.org/0000-0003-0626-6865))
- Matthew DW Piper ([ORCID: 0000-0003-3245-7219](https://orcid.org/0000-0003-3245-7219))
- Max Reuter ([ORCID: 0000-0001-9554-0795](https://orcid.org/0000-0001-9554-0795))

## Response text

DOI: [10.7554/eLife.47262.029](https://doi.org/10.7554/eLife.47262.029)

Reviewer #1:

[…] My main concern is that the claim that TOR signaling plays a major role needs a bit more substantiation and elaboration.

Our interpretation that diet treatments elicit TOR-dependent responses is based on a combination of our bioinformatic analyses, showing overlap between diet-dependent genes and genes whose expression changes in response to DR, TOR-pathway manipulation, and direct experimental evidence of the diet-dependent effect of rapamycin treatment on male and female reproduction. While we believe that the experimental evidence is compelling, we revised the manuscript in line with this reviewer's comments to substantially bolster the bioinformatic support for the link between our dietary responses and TOR signalling (Introduction). Specifically, we now include an in-depth analysis of the Graze et al. dataset and the relationship between IIS/TOR and diet-dependent gene expression. This shows that the Graze et al. data show patterns of transcription that mirror those described in our data and significant overlap between IIS/TOR and diet responses (subsection “Statistical analyses, identification of DE genes and enrichment analyses”, last paragraph and subsection “Overlap with previously described diet and nutrient-signalling responses”). Furthermore, we show that genes responding to diet manipulation significantly overlap the best-characterised set of TOR-dependent genes currently available (Tiebe et al., 2015, subsection “Diet-specific regulation of male and female reproduction”).

We have edited the manuscript to incorporate these additional findings and clarify evidence for a link between diet responses and TOR signalling (Introduction).

Table 3 shows that there is indeed overlap at the level of transcripts between this study and a previous study using rapamycin. But the reader is given rather little detail and thus a few major questions remain open: what is the overlap between the DR and the rapamycin treatments itself?

The overlap between DR and rapamycin treatment has been previously described in Dobson et al., 2018. The authors found significant overlap between the genes whose expression changes significantly in response to DR and rapamycin treatment across 4 of the 5 female tissues samples. The two tissues that had the highest number of gene overlaps was the brain and the fat body, with 45 and 46 overlapping genes respectively. A summary of these findings can be found in Table 2 of Dobson et al., 2018. We have made the link between DR and rapamycin treatment clearer in the Introduction of our manuscript (fifth paragraph).

Can all genes responding to rapamycin be called (canonical) TOR pathway genes? (i.e., how specific is rapamycin in its molecular action)?

There has been a plethora of work investigating the specificity of rapamycin at inhibiting the TORC1 complex (see e.g. Crespo and Hall, 2002). Rapamycin is very specific in its molecular function, and this specificity is conserved across a wide range of taxa (from yeasts to humans). Accordingly, rapamycin treatment is considered an effective and specific means of manipulating TOR-dependent genes. We have added text to our Materials and methods section to clarify this point.

How strongly significant (actual values / quantification rather < 0.05 threshold) were the overlaps?

We have added p-values for all overlaps in Table 3.

Is there a way to quantify overall how special / exceptional the overlap with rapamycin treatment is (e.g., the overlap with the DR treatment seems to be stronger)?

We agree that the overlap between DR-responsive genes in Dobson et al. and diet-responsive genes in our study appears greater than that of rapamycin-responsive genes. On the other hand, the number of genes in the DR set are larger than those in the rapamycin set for most tissues (meaning that overlap might actually be greater, proportionally, for the latter comparison). Significance, on the other hand, will favour comparisons of larger sets that are more powerful.

On balance, we believe that quantification would not be satisfactory. Yet, we also think that this point is less important in the revised version of our manuscript, that is couched more generally in terms of IIS/TOR signalling. We hope the reviewer will agree with this assessment.

It would also be good to have a list or table or a figure of TOR signaling components that have been identified in the overlap as well as an indication of the directionality and an estimation of the effect sizes of the transcriptional responses ascribed to this pathway.

We have added a supplementary table as requested (Supplementary file 4). The identification of “TOR signalling components” was performed in two different ways. We first compiled a list of genes that can be found under the GO terms “TOR signalling” and “insulin signalling” (N=61 genes in total). We report fold changes in males and females for these genes, irrespectively of significance. This analysis gives an indication of directionality in expression for each sex, and is analogous to some of the analyses performed by Graze et al. [30] (see their Figure 6). We find that while some of the genes are concordant in their expression changes, a number of these genes, including components of TORC1 complex, show opposing expression responses.

For the second approach, we curated data from a study which we believe contains the most well-defined TOR-responsive gene set (Tiebe et al., 2015). These genes are regulated by REPTOR and REPTOR-BP and mediate most of the transcriptional induction caused by TORC1 inhibition in Drosophila. Although this work has only been carried out in males, it is currently the best characterisation of TORC1 effects in flies. We found a significant overlap between our set of genes and TORC1 responsive genes, and this analysis was included in our study (Table 3C, lines 624-631). Furthermore, to examine the directionality of these responses, we provide fold change in both males and females in Supplementary file 4.

Are there also IIS components among the overlapping genes, given that IIS and TOR form a signaling network and given that the study by Graze et al., 2018, found that IIS plays a major role in sex-specific gene expression? What is the overlap with the Graze et al. data?

As mentioned above, we have re-analysed the raw data of Graze et al. using our pipeline (to apply gene- not exon-level transcription levels, consistent with the rest of our analyses). Our re-analysis validates Graze et al.'s overall conclusions, with many genes being differentially expressed when InR is perturbed. However, it also shows that genes fall into classes corresponding to those we define based on diet composition, namely those where InR perturbation has a sexually concordant effect (class 'InR'), those where it has opposing effects in males and females ('InR×Sex'), and those where it elicits sex-biased/-specific effects (InR+'InR×Sex').

Comparing the genes affected by InR perturbation with those responding to diet treatments in our study, we find a significant overlap ate every level, including whether genes show any response in the two datasets, between the significance of individual terms (InR vs. D and InR×Sex vs. D×Sex) and between InR and diet-based gene classifications. We describe these results in the subsection “Overlap with previously described diet and nutrient-signalling responses” and discuss their implications in the subsection “Diet-specific regulation of male and female reproduction”. Furthermore, we have added a supplementary figure where we show the expression of these TORC1 responsive genes, indicating the strength and directionality of response across both sexes (Figure 2—figure supplement 1 and 2).

We have also included text in the Discussion (825-843) to address the important point made by the reviewer about TOR lying within a wider IIS/TOR network. We highlight the fact that while the observed phenotypes are TOR-dependent responses to rapamycin treatment, TOR itself participates in a broader set of (tissue specific) signalling responses and the diet responses observed in our main experiment could be due to regulation via TOR as well as IIS.

Thus, while I believe the overlap with the TOR pathway, and while the rapamycin manipulation experiment (experiment 3) supports the TOR inference, I feel that the major conclusion – i.e. that the sex-specific reverse regulation occurs via the TOR pathway – needs to be backed up better, with some more quantitative analysis (beyond the overlap and experiment 3). To my mind this is a rather important point but also one that should not be too difficult to address with the data already at hand.

We would like to thank the reviewer for their suggestions. We believe that the additional analyses have significantly strengthened our study. While establishing the link between diet responses and IIS/TOR signalling will ultimately require careful experimentation, the additional evidence we now include go, we believe, a long way to corroborating our inferences.
