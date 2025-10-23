# Peer review - Round 1

Editors:
- Juan Valcárcel, Centre de Regulació Genòmica (CRG) Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.59654.sa1](https://doi.org/10.7554/eLife.59654.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This is an elegant and thoroughly performed study on the splicing factor hnRNPM, revealing circuits of post-transcriptional regulation relevant for prostate cancer cell growth. In particular, the study focuses on circular RNAs that are upregulated in HNRNPM deficient cells. Using splice-switching antisense oligonucleotides (SSOs), the authors demonstrate that several HNRPNPM-regulated splicing events can inhibit cell growth in HNRNPM expressing cells.

Decision letter after peer review:

Thank you for submitting your article "HNRNPM controls circRNA biogenesis and splicing fidelity to sustain prostate cancer cell fitness" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Juan Valcárcel as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by James Manley as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

Ho et al. report the results of a targeted pooled shRNA screen to identify splicing factors important for prostate cancer cell growth in vitro and in mouse xenografts. One of the hits corresponds to the gene encoding hnRNP M, an RNA binding protein overexpressed in prostate cancer cells lines compared to untransformed prostate epithelial cells. They further demonstrate that HNRNPM knockdown (KD) reduces cell proliferation, colony formation, anchorage independent growth in vitro, as well as tumor-xenograft size in vivo. eCLIP, RNA-seq and mutational analysis in minigenes identify GU-rich hnRNP M binding sites in (long) introns flanking exons that become included upon hnRNP M knock down as well as flanking exons undergoing circularization by back-splicing. Modulation of three hnRNP M-regulated alternative splicing events using splice switching antisense oligonucleotides leads to inhibition of cell growth and in the case of the EED gene to reduction of H3K27me3 modifications, which might contribute to the anti-proliferative effects observed upon hnRNP M knock down.

This is an elegant and thoroughly performed study on the splicing factor hnRNPM, revealing circuits of post-transcriptional regulation relevant for prostate cancer cell growth. There are however some issues that the reviewers feel that should be addressed before publication.

Essential revisions:

1. One important question is the extent to which these observations connect with prostate cancer biology. In the absence of results with an animal model, questions could still be asked by examining human tumors:

– First, are there alterations in hnRNP M levels/activity in prostate cancer? The results of Figure 1E are consistent with this but the comparison is limited to three cell lines, which is far from conclusive for assessing the impact of hnRNP M levels on real tumor samples. Analysis of public datasets of tumor samples (including TCGA) could be helpful in this regard.

– Second, are there splicing alterations consistent with changes in hnRNP M activity in tumor samples? The result of Figure 7G shows that the levels of EED transcript correlate with disease progression, but it is unclear what is the connection between EED transcript abundance and the ratio between EED isoforms controlled by hnRNP M (both isoforms are in frame and therefore inclusion or skipping of the alternative exon is not predicted to affect mRNA levels). Splicing-focused bioinformatic tools for the analysis of patient prognosis (e.g. Psichomics) may be helpful in this regard for EED, PRKAB2, ZNF548 and other targets of hnRNP M. The results of Figure 5J are potentially interesting but given the difficulty to predict functional effects of circRNAs, it is difficult to conceptualize these observations.

2. Is hnRNPM actually differentially required in prostate cancer versus normal prostate epithelial cells? While the authors suggest that hnRNPM may not simply be an essential protein in prostate epithelial cells, the data to support this are not clear. For example, what is the effect of hnRNPM depletion in PrEC cells (or, alternatively, does hnRNPM expression alter growth of PrEC, LNCAP, or PC3 cells)? The data presented in the manuscript are valuable regardless of the conclusion of these experiments but it would be helpful to clarify this point.

3. Figure 7C: judging from the changes in growth rates (y axis in panels for individual events), it seems that SSOs induce stronger effects on cell proliferation while inducing substantially more limited changes an alternative splicing in these target genes, how can this be explained? Are these results suggesting a potential toxicity issue with the SSO chemistry? Are these results replicated? Are the effects on cell growth recapitulated by combining the effects of SSOs targeting EED, PRKB2 and ZNF548? Finally, please discuss the fact that in Figure 7F, AON1 leads to EED protein decrease, but AON2 does not, and AON1 also leads to increased HNRNPM expression, suggesting a potential feedback loop. Can restoration of normal EED expression/splicing rescue the effects of hnRNPM loss in prostate cancer cells? As with most splicing factors, the protean number of splicing targets makes it difficult to ascertain if the effects of hnRNPM depletion are related to a few or a multitude of mis-spliced targets. Given the nice work presented on EED splicing here, it may be interesting to investigate if restoring correctly spliced EED could rescue the effects of hnRNPM loss.
