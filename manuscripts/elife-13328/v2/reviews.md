# Peer review - Round 1

Editors:
- Nicholas T Ingolia, University of California, Berkeley , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.13328.036](https://doi.org/10.7554/eLife.13328.036)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "Thousands of novel translated open reading frames in humans inferred by ribosome footprint profiling" for consideration by eLife. Your article has been favorably evaluated by Naama Barkai (Senior editor) and two reviewers, one of whom served as guest Reviewing Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Ribosome profiling seems to promise data that will allow empirical and unbiased detection of translated reading frames. In this manuscript, the authors apply a novel algorithm based on hidden markov models to analyze ribosome profiling data for a panel of human lymphoblastoid cell lines which they generated as part of this study. The new dataset is interesting, the computational approach is sensible and seems sound.

The end product of the analysis is a collection over 7,000 coding sequences (CDS) that are predicted to be translated to protein by the cell. They identify a wide variety of novel coding sequences, reflecting alternate reading frames on known mRNAs as well as translation of unannotated transcripts and pseudogenes. The authors try to demonstrate the validity of these predictions in various ways. The first comparison uses data generated in the presence of a drug that arrests the ribosome, which allows that start position and reading frame of the predicted CDS to be assessed. The p-values reported for the statistical significance in aggregate are impressive, but the underlying data in Figure 4 suggest that the false positive rate is high. The second approach to validation considers the rate of non-synonymous vs synonymous substitutions inside the predicted CDS. Again, only for a small fraction (roughly 5%) of the CDS predictions there is statistical evidence that evolutionary pressure keeps the corresponding protein sequence constant, and the size of the effect for novel CDS in Figure 5A is tiny. A third comparison, with mass spec data for protein sequences, again reveals a confirmation rate (5%) that falls far short of what would be expected for matching annotated CDS.

Conceptually, the present work offers a statistically well-grounded approach for identifying translated reading frames. The results include a few interesting biological insights: alternative non-AUG start codons occur much more often than expected, a significant fraction of CDS have upstream alternatives whose level is mutually anti-correlated, and cis-QTLs can be mapped for the relative preference between the two alternatives. Empirically, the authors are able to ground their novel peptide predictions in direct detection of translated protein products, albeit at a rather low detection efficiency. These advances distinguish the present work from other recent studies addressing the same question, and on these grounds merit publication in eLife.

This is an excellent study, and the authors have done the best they can to analyze the data. It is perhaps disappointing that such a small fraction of the novel CDS predictions seem to hold up in validation. The authors speculate that these peptides may turn over more rapidly than for annotated CDS (perhaps by analogy with antisense transcription). This is indeed a possible explanation, but it would require further substantiation, which is beyond the scope of this study.

Essential revisions:

1) There is a risk that the larger community will use these new annotations as a resource without being aware of the low validation rate at the level of individual CDS. I therefore feel strongly that the authors should address the ~5% validation rate explicitly in the Abstract. That said, the validation rate in terms of transcriptional initiation may be much more favorable than that in terms of steady-state protein abundance. Future studies will need to address this further, but this is still an important work that sets a significant step towards a more comprehensive understanding of translational control on a genome-wide scale.

2) The authors estimate model parameters, including start codon usage psi_c, from five thousand well-expressed, annotated CDSes. However, annotated mCDSes, cryptic/novel mCDSes, and uaCDSes may differ – and in particular annotated mCDSes likely show a particularly strong bias towards the use of AUG codons, and a near-complete absence of most others besides CUG, which occurs in a few specific genes such as c-Myc. Does this effect in the estimated psi_c values bias the discovery of new reading frames in order to produce the trend shown in Figure 3B?

3) The authors report that 310 / 7,801 GENCODE-analyzed genes showed an "entirely distinct" mCDS. However, they estimate their per-transcript Type I error rate as 4.5%, which seems roughly consistent with all 310 instances of distinct CDSes reflecting annotation errors.

4) Identification of the precise translation initiation site has a higher false discovery rate than overall CDS identification. Other recent work (e.g. Fields et al.) incorporates harringtonine start site profiling directly into CDS predictions. Could the authors take a similar approach to improve detection of the correct initiation site (and perhaps thereby improve overall CDS accuracy too)?

5) As a related point, is there a general trend to identify CDSes that are longer, or CDSes that are shorter, when identifying the correct reading frame but not the annotated start site?

6) In the second paragraph of the subsection “Translation of short alternate coding sequences in addition to the mCDS”, the authors report 46 uaCDSes with detected peptides and 317 uaCDSes with evidence for selective constraint – are these two groups correlated?
