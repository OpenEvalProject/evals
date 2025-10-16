# Peer review - Round 1

Editors:
- Inez Rogatsky, https://ror.org/03zjqec80 Hospital for Special Surgery United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66034.sa0](https://doi.org/10.7554/eLife.66034.sa0)

This study modeling the actions of estrogen and progesterone receptors (ER and PR) in endometrial cancer cells through a panel of genomic approaches reveals a potentially interesting collaboration between the two, further facilitated by the non-receptor transcription factor PAX2. The identification of so-called chromatin 'progestin control regions' inside TADs, where the three factors cooperate and which appear to be the feature setting endometrial cancer cells apart from breast cancer cells, is of potential interest for future investigation.


---

# Peer review - Round 1

Editors:
- Inez Rogatsky, https://ror.org/03zjqec80 Hospital for Special Surgery United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.66034.sa1](https://doi.org/10.7554/eLife.66034.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Chromatin topology defines estradiol-primed Progesterone Receptor and PAX2 binding in endometrial cancer gene expression" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Jessica Tyler as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Carol Lange (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The study is devoid of any functional data linking PAX2 to ER/PR signaling. Co-localization data is purely correlative and circumstantial. PAX2 binding enrichment near ER/PR sites over its binding at randomly selected open enhancers needs to be statistically established. Critically, the authors should demonstrate that depleting PAX2 affects ER/PR-driven gene expression or their genomic localization. As a related point, the authors should specify how they arrived at picking PAX2 is a candidate regulator among other members of the Pax family.

2) Although Ishikawa cells are a well-studied commonly used model system for endometrial cancer cells, they are a unique cell line and it is critical to establish that authors' findings are not a feature specific to Ishikawa cells. The authors need to recapitulate at least some of their observations in a different endometrial ER+/PR+ model cell lines, or human tissue organoids, or in cohorts of clinical samples. If no other models exist, the authors should acknowledge and discuss the limitations of their findings.

3) Based on the GEO dataset uploaded, there appears to be a single replicate for the ChIP-seq experiments. If so, this does not meet the minimum ENCODE requirement and cannot be analyzed or serve as basis for any conclusions. For example, many of the differential peaks (i.e. the 307 lost peaks) are likely to be false positives that result from only one replicate.

4) Many of the conclusions are based on small subsets of genes in TADs that correlate with outcome. The authors need to provide evidence that the Hi-C and genomic analyses revealed a statistically enriched gene signature of clinical and prognostic potential in endometrial cancer, rather than pick a handful of genes that happen to correlate with clinical outcome (which would likely be achieved by any random large enough starting set of genes).

Additional specific revisions:

1. Based on motif enrichment analysis, the authors claim that PR monomers could bind at 30 min and dimers at 60 min. There is no real evidence that this is the case. Unless the authors plan to pursue this functionally and show dimeric vs. monomeric binding, this statement needs to be removed.

2. Please clarify what 'shuffling the coordinates' for PgCRs means (lines 362-363)

3. On page 13, the term 'hormone-regulated' is used frequently. Please state whether you are referring to R5020 or E2.

3. In line 398, please clarify what list of genes you are referring to.

4. Some of the text is confusing. For example, the authors talk about the 'proliferative response' to R5020, which implies a proliferation in response to treatment, rather than an anti-proliferative response. Similarly, the sentence starting 'The signature of genes regulated in conjunction with loss….' is unnecessarily confusing and doesn't make obvious sense.

Reviewer #1 (Recommendations for the authors):

1. Some functional data linking PAX2 to the PR (and/or) ER pathway.

2. Some confidence that more than one replicate of ChIP-seq was conducted and if not, I am unwilling to support pursuing this manuscript.

3. Evidence that the Hi-C and broad genomic analysis revealed a gene signature of clinical value, rather than a handful of genes that happen to correlate with clinical outcome (which would likely be achieved any random set of genes).

I found the final part confusing and not convincing. Ultimately the key message is: 1. PR is a prognostic gene; 2. A small number of the genes from the TAD analysis correlate with outcome. This would be expected if enough genes are used as a starting point. Is there any statistical enrichment in the genes derived from the Hi-C (assuming they are also regulated in the authors RNA-seq data) that correlate with outcome in endometrial cancer? If not, then any list of genes would inevitably have a handful that correlate with outcome, but the key question is whether the Hi-C compartmentalization allows the discovery of genes that are enriched for clinical prognostic potential? If not, I'm not sure the last part adds anything to the story.

Reviewer #2 (Recommendations for the authors):

The authors use Ishikawa cells as a representative cell line model of PR+ endometrial cancer. Are there additional ER+/PR+ models than can be included to support their salient findings around the role of PAX2 as a required co-factor with PR or ER/PR at hormone regulated target genes? The major concern for readers centers on how we dissociate cell line differences from tissue-specific ones with the use of only one cell line to represent the tissue? Can the authors demonstrate a role for PAX2 in human tissue organoids for example? If no other models exist, the authors should discuss the limitations of their findings that are limited to a single cell line herein.

How does PAX2 expression change during endometrial cancer development and progression (i.e. in the public data)? Loss of PAX2 (i.e. early in cancer development) may explain the loss of responsiveness to progesterone or loss of protection from progesterone as an inhibitor of estrogen-induced proliferation. Furthermore, the authors should demonstrate that PAX2 is actually required for progestin-dependent regulation of known target genes in these cells by performing PAX2 knock-down or knock-out studies (and by individual target gene readouts of mRNA levels and promoter recruitment/ChIP).

Reviewer #3 (Recommendations for the authors):

1) The author claims that ER alpha is the predominant isoform present in Ishikawa cells (Supplementary Figure 1G). This relies on a Western blot comparing abundance of ER alpha to ER beta. However, this Western has no positive control for the ER beta antibody, and given different sensitivities of the antibodies, abundance between the two isoforms cannot really be compared in this manner. Has this been looked at previously? Is ER beta not expressed at all in this cell line?

2) There needs to be more rationale for the use of the Ishikawa cell line. As per the authors' data, there is very low PR expression in these cells, and the luciferase activity of the endogenous PR / number of PR chromatin binding sites is overall low throughout the ChIP-seq studies. The authors also state on line 262 that the hormone-dependent gene regulation is very cell type specific. Why not look at common themes across cell lines instead of looking very specifically at a cell line for which the data likely will not apply to other cell lines?

3) Figure 4 shows many other enriched TF binding motifs other than PAX family TFs. It would be useful to discuss why the authors chose to focus on PAX family/PAX2 specifically.

4) On lines 297-307, the authors state that PAX2 ChIP-seq data shows overlap with ER and PR binding sites. However, do the PAX2 binding sites specific ally correspond to new PR binding sites which appear in the presence of E2 pre-treatment?

5) Can the authors be more clear on what they mean by shuffling the coordinates for PgCRs in lines 362-363?

6) On page 13, the authors use the term "hormone-regulated" frequently. Please clarify this language to express whether you are referring to progestin or E2 regulated genes.

7) In lines 398, it is unclear what list of genes the authors are referring to. The data generated in this study have been submitted to the NCBI Gene Expression Omnibus (GEO); accession number GSE139398.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Chromatin topology defines estradiol-primed Progesterone Receptor and PAX2 binding in endometrial cancer" for further consideration by eLife. Your revised article has been evaluated by Jessica Tyler (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

1. The statistical analysis for some of the new figure panels is lacking. Specifically, Figure 5H, 5I, Figure 5—figure supplement 2B (siRNA KD of PAX2) display error bars, and up/down changes are described in Results, however, it is not indicated which tests were used to compare the values and which of the changes are, in fact, significant.

2. Wording in the abstract describing these results could be streamlined to "…. in PAX2 knockdown cells suggests a role for PAX2 in fine-tuning ERalpha and PR interplay in transcriptional regulation".
