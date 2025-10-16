# Peer review - Round 1

Editors:
- Maureen E Murphy, The Wistar Institute United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69843.sa0](https://doi.org/10.7554/eLife.69843.sa0)

The authors present an interesting genomics approach to understanding the role of heat shock factor 1 (HSF1) in breast cancer cells. They show that HSF1 indirectly interacts with estrogen receptor α (ERα) by regulating the transcription of HSP90, which is essential for normal folding and function of the receptor. They also show that HSF1 and ERα tether within the genome to enhance the transcription of a subset of genes associated with disease progression. Finally, they show the relevance to the breast tumors through comparing their data to publicly available data.


---

# Peer review - Round 1

Editors:
- Maureen E Murphy, The Wistar Institute United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69843.sa1](https://doi.org/10.7554/eLife.69843.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for sending your article entitled "Heat Shock Factor 1 (HSF1) as a new tethering factor for ESR1 supporting its action in breast cancer" for peer review at eLife. Your article is being evaluated by 3 peer reviewers, and the evaluation is being overseen by a Reviewing Editor and Maureen Murphy as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Mary Allen (Reviewer #2); Sean Fanning (Reviewer #3).

Heat Shock Factor 1 (HSF1) as a new tethering factor for ESR1 supporting its action in breast cancer.

The authors present an interesting genomics approach to understanding the role of heat shock factor-1 (HSF1) in breast cancer cells. Namely, they show that HSF-1 indirectly interacts with estrogen receptor α (ERα) by regulating the transcription of HSP90, which is essential for normal folding and function of the receptor. They also show that HSF-1 and ERα tether within the genome to enhance the transcription of a subset of genes associated with disease progression. They show relevance to the breast cancer patient through comparing their data to publicly available data. However there are concerns about some of the conclusions reached in the manuscript, and how some of the statistical analyses have been performed.

Major Concerns:

1. The RNA-seq comparisons were done by counting the number of genes that were different. They note that the basal level of several of the genes targeted by ESR1 is higher in HSF1 deficient cells. If that is true then my expectation is fold-change will be lower after ligand addition. Mathematically, fold change is a ratio, and increasing the denominator decreases the ratio value. It is unclear if they removed the ER target genes with higher basal levels in HSF1 deficient cells that the higher induction they note would still be present. To clarify my confusion, I would like to know if the difference in the presence of ligand due to the difference before the ligand was added or due to what happens after the ligand is added. Also, Figure 4 seems to imply that the level of ESR1 is lower in the HSF1- cells. Is that a factor in the RNA-seq response to E2?

2. The authors show that HSF1 deficient cells have a higher number of ESR1 peaks with more tags in the absence of E2. However, a spike-in was not used, so the change seen in the ChIP-seq could be a technical artifact. For example, formaldehyde crosslinking varies from plate to plate regardless of the sample type. Sequencing depth of the ChIP-seq samples was not discussed and unless the depth is comparable, graphs should be on normalized tags, not tags.

3. All figures that compare chip regions should be randomizing one of the two data sets and asking what is the expectation for overlap. For instance, they talk about how often HSF1 bound sites are also ESR1 bound. Knowing if that amount of interaction is expected by random chance is only possible if they shuffle the positions of one of the datasets and ask for overlap rate. (Or using an equivalent statical test like bedtools jaccard or reldist).

4. When comparing the HSF1 ChIP-seq the ESR1 ChIP-seq to the ChIA-pet their intersections, and overlap statics should be used to determine if the interactions in 5D are just random overlaps or are seen more than one would expect by chance. (See comment above on shuffling and bedtools tests.)

5. The relationship is not clear between their results regarding the sequencing of HSF1 deficient cells and the human tumor data. The molecular data implies HSF1 regulates ESR1 in wild-type cells. The authors should add to the discussion potential reasons why are ESR1+/HSF1low and ER-/HSFhigh are the most divergent groups.

6. Title: In contrast to the classical DNA-binding mode, where ER binds directly to EREs, tethering factors such as AP-1 family transcription factors (PMIDs: 11162939, 21964465) and Sp1 (PMID: 16651265), have been shown to recruit ER to their target genes, which lack canonical EREs. The proposed model suggests that HSF1 acts as a cooperative factor for ER, where both transcription factors bind DNA independently (Figure 8). The authors also stated that "co-binding of both factors in the same DNA region is not critical in the regulation of the ESR1 transcriptional activity" (pg 12, ln 286-287). Thus, the mechanism of HSF1 action does not meet the basic requirements of a tethering factor as suggested in the title.

7. Analysis of data: A strength of this manuscript is the use of RNA-seq to examine the effect of HSF1 loss on the estrogen-regulated transcriptional program in MCF7 cells. However, the data presentation is unnecessarily complicated (Figure 1A). Moreover, data presented as fold change E2/Ctr (Figure 2B, 2C and 2E) can be misleading and should be avoided in this case, because HSF1 KO appears to have gene-specific effects on estrogen-deprived cells.

8. The MGAT3/FOS/CYP24A1 expression profile, where HSF1 loss reduces gene expression with and without estrogen stimulation (Figure 2F), supports a role of HSF1 as an ER collaborator or cooperative factor. In contrast, the predominant expression profile, which is exhibited by GREB1/PGR/KDM4B, where HSF1 loss enhances gene expression in estrogen-deprived cells (Figure 2F), supports an inhibitory role for HSF1 under estrogen-deprived conditions, which undermines the role of HSF1 as a cooperative tethering factor for ER at these estrogen-induced genes. Together, these findings are interesting, but do not show conclusively that the efficacy or potency of E2 is reduced in HSF1-deficient cells.

9. The authors examined the effect of HSF1 KO on the ER-HSP90 interaction using PLA. The authors show conclusively that HSF1 loss enhanced the ER-HSP90 interaction (Figure 4). This finding is novel and compelling, but evidence that HSP90 contributes to the HSF1 KO phenotypes was not presented, which is a major weakness in the paper.

10. The authors used ChIP-seq to compare ER and HSF1 binding sites across the MCF7 cell genome. ER and HSF1 binding sites show < 3% overlap in estrogen-deprived cells, with about 4-fold more overlapping binding sites observed upon E2-stimulation (Figure 5A, 5B), which indicates that both factors generally bind DNA independently, with some cooperative binding where ER recruitment was increased. Comparing ChIP-seq recruitment data with ChIA-PET interaction data, suggests interaction between some distinct overlapping and non-overlapping HSF1 and ER binding sites (Figure 5D). It is not clear exactly how prevalent these long-range interactions are across the genome. Using PLA, the authors showed that E2 enhanced the ER-HSF1 interaction (Figure 5F), suggesting that ER can drive chromatin organization that enables these long interactions or chromatin looping. However, chromatin conformation capture (3C) showed that some of these long-range interactions occur in HSF1 KO cells (Figure 5E), suggesting that ER does not require HSF1 to drive chromatin looping. Can the authors clarify these findings into a cogent model?

11. In breast cancer, ER+ status is an independent and mostly favorable prognostic marker (PMIDs: 6488142, 28601929). High HSF1 expression is associated with mortality in ER+ breast cancer (PMID: 22042860, 27713164). Prognostic impact of HSF1 expression on ER- cases was not obvious (PMID: 27713164). Here, the authors analyzed the TCGA database for prognostic value of ER and HSF1 mRNA and suggest that ER- cases with high HSF1 mRNA levels have the poorest outcome (Figure 6D), suggesting an ER-independent role for HSF1 in breast cancer. However, this conclusion is probably a biased reflection of the prognostic difference between basal and luminal breast cancer subtypes (Figure 6C) (PMID: 26693050). Moreover, how this finding supports a HSF1 role as a cooperative or tethering factor for ER is not clear, and the prognostic value of HSF1 mRNA levels in ER+ breast cancer was not obvious from the data presented.

12. With regard to their conclusion that HSF1 increases the diversity of the transcriptome in ER-positive breast cancers, the rationale for this analysis is unclear, and the idea that HSF1 affects ER-target genes has already been demonstrated in the KO model using RNA-seq (Figure 2).

13. Stylistic changes are needed: Much of the text in the figures are too small to read. It was hard to tell the differences between the A, B, C, D groups and the a, b, c, d groups in figure 7.

14. In figure 5, they authors should be subsampling the "all" groups to the same number as the smaller groups to see if the distributions are the same.

15. Figures 5A and 5B are trying to show information for the HSF1 and ESR1 overlapping peaks. However, for that data to be useful we need to understand non-overlapping peak data. Also, is the figure showing tags from ESR1 ChIP-seq or HSF1 ChIP-seq?

16. Important concern: The authors should be using statistical tests to see if overlap in data sets are above random chance.

17. The authors generated HSF-1 knockouts for MCF7 and T47D breast cancer cells. However, the vast majority of their work was performed with only the T47D cells. These cell lines show different dependencies on ERα and antiestrogen differently affect receptor stability between them. More work should have been done outside of one knockdown and proliferation experiment to show that HSF-1 is important in both cell lines. It would give credence to its role in breast cancer cells beyond MCF7 cells.

18. The authors used an aldefluor assay to show that HSF-1 affects stem-progenitor populations. They did not show any additional data for this line of inquiry. If this phenotype is affected by HSF-1 they should examine EMT signatures along with cellular invasion, and migration.

19. Therapeutic approaches to targeting ERα were not discussed in this manuscript. However, the role of HSF-1 in the therapeutic response to antiestrogens would be of great importance to the field. Showing the impact of HSF-1 knockdown to ERα transcriptional activity and cellular proliferation in the presence of clinically important hormone therapies fulvestrant and 4-hydroxytamoxifen as well as CDK4/6 inhibitors like palbociclib would greatly enhance the impact of this paper.
