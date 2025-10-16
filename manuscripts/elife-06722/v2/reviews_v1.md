# Peer review - Round 1

Editors:
- Torben Heick Jensen, Aarhus University , Denmark

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.06722.028](https://doi.org/10.7554/eLife.06722.028)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Quality control of transcription start site selection by nonsense-mediated-mRNA decay” for consideration at eLife. Your article has been favorably evaluated by James Manley (Senior editor) and two reviewers, one of whom is a member of our Board of Reviewing Editors.

The Reviewing editor and the other reviewer discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

Overall the study by the Jacquier laboratory is timely and contains very interesting information adding to our knowledge of how pervasive transcription is suppressed post-transcriptionally by RNA turnover.

Before acceptance the following points should be addressed:

Major points:

1) A technical concern relates to the TSS sequencing method, which relies on the treatment of poly(A)+ RNA with phosphatase to prevent degradation intermediates with a 5' phosphate from ligating to the biotinylated adaptor oligo. Since transcripts with 5'ends originating downstream of their annotated TSSs (B-TSSC, iTSS) are identified, it seems crucial to control for the efficiency of the phosphatase treatment, as many of these transcripts may otherwise represent degradation intermediates rather than transcripts with alternative 5'ends. Finding the same consensus sequence motif as at canonical TSSs helps, but do the authors have any direct means to control for the effective exclusion of such species from the libraries?

2) Differential expression analysis should be done according to today's best practice, which includes normalization of the data that accounts for differences in sequencing depths between samples (i.e. size factor normalization [see DESeq2] rather than rpkm).

Minor points:

1) The authors' seem somewhat biased towards the idea that every transcript that is repressed by some factor constitutes noise. Is this really always clear?

2) The authors identify a consensus sequence, which basically is identical for all types of RNAPII transcripts: A(N)6PyPu, where the Pu is the TSS. Is it possible to investigate/estimate what fraction of such sites in the genome is functioning as TSSs based on the TSS sequencing data?

3) The term “synergistic”, used in the subsection “Identification of additional pervasive transcripts” (“it had a synergistic effect on some ‘intergenic’…”): could this synergism simply be an additive effect that is hidden by the generally low expression of these RNAs?

4) What is the reason for the overall rather low mapping rate of the sequencing data (sometimes as low as 30%)?

5) Throughout the manuscript only few statistical tests are applied. While in many cases the displayed effects appear convincing, it would be useful to, e.g., evaluate whether the small difference in Figure. 7B is statistically significant.
