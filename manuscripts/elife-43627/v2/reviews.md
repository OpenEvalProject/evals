# Peer review - Round 1

Editors:
- Matthew G Vander Heiden, Massachusetts Institute of Technology United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.43627.036](https://doi.org/10.7554/eLife.43627.036)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Flura-seq identifies organ-specific metabolic adaptations during early metastatic colonization" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Sean Morrison as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The paper is interesting, though both reviewers commented that the uniqueness of the technique was overstated and raised technical questions that should be addressed in a revised manuscript. I have summarized the specific points from the reviewers that should be addressed.

Summary:

The study presents a new technique called Flura-seq for transcriptomic analysis of rare cell populations in tissues. This approach is based on 5-FU labeling of nascent RNAs in cytosine deaminase-expressing cells. After validating the approach in cell lines it was used to characterize the transcriptome of rare metastatic cells in vivo. They describe organ specific gene expression signatures and focus on the fact that lung micrometastatic cells have higher expression levels of electron transport chain as well as antioxidant genes, and confirm these findings in human breast cancer metastases.

Essential revisions:

1) With recent advances in single cell RNA sequencing, please discuss how this technique differs and, if possible, comment on how it performs in comparison to the more widely used single cell RNA sequencing approaches. A discussion of where Flura-Seq should be used instead of scRNA-seq would increase the impact of the paper.

2) Given that Flura-seq requires the overexpression of cytosine deaminase and uracil phosphoribosyl transferase, the administration of 5FU and thymine and a relatively short-term assay, these limitations should be more fully discussed. Also, the authors should not completely discount existing approaches that are relevant to these questions including laser capture microdissection/RNA-seq and SLAM-ITseq.

3) In Figure 3C, it was noted that only 53 to 74% of the aligned reads were mapped to the human genome after IP in 5-FC treated mice. Does it mean that 26 to 47% of the reads are derived from contaminating mouse reads? What does this mean for the efficacy of the staining and IP purification? Can one then trust that all the human reads correspond to stained RNA of actively transcribed genes with such a noisy technique? How good is the qPCR to assess the signal-to-noise ratio of the technique (for example Figure 3B) and why is there such a discrepancy between Figure 3B and 3C results?

4) In Figure 4D, it was claimed that lung micrometastases have the highest content of unique transcriptional activity. However, what is lacking is an objective quantification of this uniqueness. This result is the reason why the remainder of the paper focuses on the specificity of the lung versus brain metastases and electron transport chain (ETC)/antioxidant gene expression levels, so this should be more convincing.

5) Please comment on whether the main findings could be explained by the higher oxygen levels in the lung tissue compared to the brain and mammary fat pad. It is well known that high oxygen can lead to high levels of oxidative stress. This seems to be confirmed by the basal 4-HNE, GPX1 and NRF2 stainings in normal lung tissue, which are equally high as in the lung metastases and higher than in normal brain tissue (Figure 5C, E, F). Finally, in the comparison of in vitro cultures for example, the high oxygen levels could also be responsible for the loss of differences in the transcriptional profiles of ex vivo cultures from different organs (Figure 4B).

6) In co-culture experiments to assess the sensitivity of Flura-seq (Figure 1F), could the authors comment on why there isn't higher signal of human housekeeping genes in the samples when there are 10-fold more human cells?

7) Many of the RNAs downregulated in TGFb control samples are also reduced in the Flura-seq samples, which seems surprising given the short 30 minute 5-FC labeling period. Was the signal for these genes low relative to the control samples, as expected? To assess this, it would be helpful to see the normalized count values for each condition in the supplemental tables (not just fold-change). Also, are there differentially expressed transcripts identified by Flura-seq that are not found in the control samples? Are they known TGF-b targets? Potential false-positives?

8) Please clarify or reference how the 24 genes for the NRF2 signature were selected.

9) Please ensure that statistical significance of the results is addressed throughout, including in Figure 1F (where the SD is large), 2C, and 3B-C.
