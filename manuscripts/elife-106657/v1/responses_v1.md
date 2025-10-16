# Author response - Round 1

Authors:
- Benura Azeroglu ([ORCID: 0000-0001-7243-384X](https://orcid.org/0000-0001-7243-384X))
- Wei Wu
- Raphael Pavani ([ORCID: 0000-0002-7187-2995](https://orcid.org/0000-0002-7187-2995))
- Ranjodh Singh Sandhu ([ORCID: 0009-0008-2340-3423](https://orcid.org/0009-0008-2340-3423))
- Tadahiko Matsumoto
- André Nussenzweig
- Eros Lazzerini-Denchi ([ORCID: 0000-0001-5378-4644](https://orcid.org/0000-0001-5378-4644))

## Response text

DOI: [10.7554/eLife.106657.3.sa4](https://doi.org/10.7554/eLife.106657.3.sa4)

The following is the authors’ response to the original reviews.

Reviewer #1 (Recommendations for the authors):

One minor question would be whether the authors could expand more on the application of END-Seq to examine the processive steps of the ALT mechanism? Can they speculate if the ssDNA detected in ALT cells might be an intermediate generated during BIR (i.e., is the ssDNA displaced strand during BIR) or a lesion? Furthermore, have the authors assessed whether ssDNA lesions are due to the loss of ATRX or DAXX, either of which can be mutated in the ALT setting?

We appreciate the reviewer’s insightful questions regarding the application of our assays to investigate the nature of the ssDNA detected in ALT telomeres. Our primary aim in this study was to establish the utility of END-seq and S1-END-seq in telomere biology and to demonstrate their applicability across both ALT-positive and -negative contexts. We agree that exploring the mechanistic origins of ssDNA would be highly informative, and we anticipate that END-seq–based approaches will be well suited for such future studies. However, it remains unclear whether the resolution of S1-END-seq is sufficient to capture transient intermediates such as those generated during BIR. We have now included a brief speculative statement in the revised discussion addressing the potential nature of ssDNA at telomeres in ALT cells.

Reviewer #2 (Recommendations for the authors):

How can we be sure that all telomeres are equally represented? The authors seem to assume that END-seq captures all chromosome ends equally, but can we be certain of this? While I do not see an obvious way to resolve this experimentally, I recommend discussing this potential bias more extensively in the manuscript.

We thank the reviewer for raising this important point. END-seq and S1-END-seq are unbiased methods designed to capture either double-stranded or single-stranded DNA that can be converted into blunt-ended double-stranded DNA and ligated to a capture oligo. As such, if a subset of telomeres cannot be processed using this approach, it is possible that these telomeres may be underrepresented or lost. However, to our knowledge, there are no proposed telomeric structures that would prevent capture using this method. For example, even if a subset of telomeres possesses a 5′ overhang, it would still be captured by END-seq. Indeed, we observed the consistent presence of the 5′-ATC motif across multiple cell lines and species (human, mouse, and dog). More importantly, we detected predictable and significant changes in sequence composition when telomere ends were experimentally altered, either in vivo (via POT1 depletion) or in vitro (via T7 exonuclease treatment). Together, these findings support the robustness of the method in capturing a representative and dynamic view of telomeres across different systems.

That said, we have now included a brief statement in the revised discussion acknowledging that we cannot fully exclude the possibility that a subset of telomeres may be missed due to unusual or uncharacterized structures

I believe Figures 1 and 2 should be merged.

We appreciate the reviewer’s suggestion to merge Figures 1 and 2. However, we feel that keeping them as separate figures better preserves the logical flow of the manuscript and allows the validation of END-seq and its application to be presented with appropriate clarity and focus. We hope the reviewer agrees that this layout enhances the clarity and interpretability of the data.

Scale bars should be added to all microscopy figures.

We thank the reviewer for pointing this out. We have now added scale bars to all the microscopy panels in the figures and included the scale details in the figure legends.

Reviewer #3 (Recommendations for the authors):

Overall, the discussion section is lacking depth and should be expanded and a few additional experiments should be performed to clarify the results.

We thank the reviewer for the suggestions. Based on this reviewer’s comments and comments for the other reviewers, we incorporated several points into the discussion. As a result, we hope that we provide additional depth to our conclusions.

(1) The finding that the abundance of variant telomeric repeats (VTRs) within the final 30 nucleotides of the telomeric 5' ends is similar in both telomerase-expressing and ALT cells is intriguing, but the authors do not address this result. Could the authors provide more insight into this observation and suggest potential explanations? As the frequency of VTRs does not seem to be upregulated in POT1-depleted cells, what then drives the appearance of VTRs on the C-strand at the very end of telomeres? Is CST-Pola complex responsible?

The reviewer raises a very interesting and relevant point. We are hesitant at this point to speculate on why we do not see a difference in variant repeats in ALT versus non-ALT cells, since additional data would be needed. One possibility is that variant repeats in ALT cells accumulate stochastically within telomeres but are selected against when they are present at the terminal portion of chromosome ends. However, to prove this hypothesis, we would need error-free long-read technology combined with END-seq. We feel that developing this approach would be beyond the scope of this manuscript.

(2) The authors also note that, in ALT cells, the frequency of VTRs in the first 30 nucleotides of the S1-END-SEQ reads is higher compared to END-SEQ, but this finding is not discussed either. Do the authors think that the presence of ssDNA regions is associated with the VTRs? Along this line, what is the frequency of VTRs in the END-SEQ analysis of TRF1-FokI-expressing ALT cells? Is it also increased? Has TRF1-FokI been applied to telomerase-expressing cells to compare VTR frequencies at internal sites between ALT and telomerase-expressing cells?

Similarly to what is discussed above, short reads have the advantage of being very accurate but do not provide sufficient length to establish the relative frequency of VTRs across the whole telomere sequence. The TRF1-FokI experiment is a good suggestion, but it would still be biased toward non-variant repeats due to the TRF1-binding properties. We plan to address these questions in a future study involving long-read sequencing and END-seq capture of telomeres.

Finally, in these experiments (S1-END-SEQ or END-SEQ in TRF1-Fok1), is the frequency of VTRs the same on both the C- and the G-rich strands? It is possible that the sequences are not fully complementary in regions where G4 structures form.

We thank the reviewer for this observation. While we do observe a higher frequency of variant telomeric repeats (VTRs) in the first 30 nucleotides of S1-END-seq reads compared to END-seq in ALT cells, we are currently unable to determine whether this difference is significant, as an appropriate control or matched normalization strategy for this comparison is lacking. Therefore, we refrain from overinterpreting the biological relevance of this observation.

The reviewer is absolutely correct. Our calculation did not exclude the possibility of extrachromosomal DNA as a source of telomeric ssDNA. We have now addressed this point in our discussion.

The reviewer is correct in pointing out that we still do not know what causes ssDNA at telomeres in ALT cells. Replication stress seems the most logical explanation based on the work of many labs in the field. However, our data did not reveal any significant difference in the levels of ssDNA at telomeres in non-ALT cells based on telomere length. We used the HeLa1.2.11 cell line (now clarified in the Materials section), which is the parental line of HeLa1.3 and has similarly long telomeres (~20 kb vs. ~23 kb). Despite their long telomeres and potential for replication-associated challenges such as G-quadruplex formation, HeLa1.2.11 cells did not exhibit the elevated levels of telomeric ssDNA that we observed in ALT cells (Figure 4B). Additional experiments are needed to map the occurrence of ssDNA at telomeres in relation to progression toward ALT.

(3) Based on the ratio of C-rich to G-rich reads in the S1-END-SEQ experiment, the authors estimate that ALT cells contain at least 3-5 ssDNA regions per chromosome end. While the calculation is understandable, this number could be discussed further to consider the possibility that the observed ratios (of roughly 0.5) might result from the presence of extrachromosomal DNA species, such as C-circles. The observed increase in the ratio of C-rich to G-rich reads in BLM-depleted cells supports this hypothesis, as BLM depletion suppresses C-circle formation in U2OS cells. To test this, the authors should examine the impact of POLD3 depletion on the C-rich/G-rich read ratio. Alternatively, they could separate high-molecular-weight (HMW) DNA from low-molecular-weight DNA in ALT cells and repeat the S1-END-SEQ in the HMW fraction.

The reviewer is absolutely correct. Our calculation did not exclude the possibility of extrachromosomal DNA as a source of telomeric ssDNA. We have now addressed this point in our discussion.

(4) What is the authors' perspective on the presence of ssDNA at ALT telomeres? Do they attribute this to replication stress? It would be helpful for the authors to repeat the S1-END-SEQ in telomerase-expressing cells with very long telomeres, such as HeLa1.3 cells, to determine if ssDNA is a specific feature of ALT cells or a result of replication stress. The increased abundance of G4 structures at telomeres in HeLa1.3 cells (as shown in J. Wong's lab) may indicate that replication stress is a factor. Similar to Wong's work, it would be valuable to compare the C-rich/G-rich read ratios in HeLa1.3 cells to those in ALT cells with similar telomeric DNA content.

The reviewer is correct in pointing out that we still do not know what causes ssDNA at telomeres in ALT cells. Replication stress seems the most logical explanation based on the work of many labs in the field. However, our data did not reveal any significant difference in the levels of ssDNA at telomeres in non-ALT cells based on telomere length. We used the HeLa1.2.11 cell line (now clarified in the Materials section), which is the parental line of HeLa1.3 and has similarly long telomeres (~20 kb vs. ~23 kb). Despite their long telomeres and potential for replication-associated challenges such as G-quadruplex formation, HeLa1.2.11 cells did not exhibit the elevated levels of telomeric ssDNA that we observed in ALT cells (Figure 4B). Additional experiments are needed to map the occurrence of ssDNA at telomeres in relation to progression toward ALT.

Finally, Reviewer #3 raises a list of minor points:

(1) The Y-axes of Figure 4 have been relabeled to account for the G-strand reads.

(2) Statistical analyses have been added to the figures where applicable.

(3) The manuscript has been carefully proofread to improve clarity and consistency throughout the text and figure legends

(4) We have revised the text to address issues related to the lack of cross-referencing between the supplementary figures and their corresponding legends.
