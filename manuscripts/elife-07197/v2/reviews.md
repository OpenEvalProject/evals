# Peer review - Round 1

Editors:
- Phillip D Zamore, Howard Hughes Medical Institute, University of Massachusetts Medical School , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.07197.026](https://doi.org/10.7554/eLife.07197.026)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “KRAS-Dependent Sorting of miRNA to Exosomes” for consideration at eLife. Your article has been favorably evaluated by Sean Morrison (Senior editor) and two reviewers, one of whom is a member of our Board of Reviewing Editors.

The Reviewing editor and the other reviewer discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

The function of exosomal miRNAs is a highly controversial area of research, with some studies, such as this manuscript, claiming that miRNAs are not only exported from cells in exosomes, but also taken up by other cells as biologically functional signaling molecules, and others arguing they have no biological function. This manuscript, likely for the first time in the field establishes a well-defined experimental system: three isogenic cells lines that differ solely in KRAS status.

The manuscript makes some progress toward testing the idea that miRNAs can be transferred from cell-to-cell, but given the controversies in the field, a higher standard of proof is required to merit publication in eLife. We recommend the authors be given the opportunity to revise their manuscript, providing the requested new experiments and analyses. Most importantly, I urge the authors to spend less time selling their story and more effort rigorously testing-not proving-their hypotheses.

1) The major paper deficiency is lack of a clear biological model or mechanism explaining the data. While this is also true for most published exosome papers, one expects an eLife paper to propose some explanation for why specific miRNAs are transferred from cell-to-cell according to the exporting cell's KRAS status.

2) Correlation analysis plays a central role in testing the authors' hypothesis. Given the low correlation of the independent biological replicates (deep sequencing replicates typically correlate with R > 0.90 in one of our labs), the authors should apply an appropriate statistical test to determine that R-values of 0.92-0.96 between cells are unlikely to differ from R-values of 0.67-0.89 comparing exosomes to the exporting cells? If the bottom quartile of miRNAs by abundance (i.e., the ones least well measured by convention, rather than digital, sequencing methods) are excluded, do the Pearson correlation values change? Can all the biological replicates be used to make the comparisons, not simply pairwise combinations of individual data sets?

3) Is the degree of reporter repression small because the abundance of exosome-delivered miRNAs is low? The miRNA literature overwhelmingly supports the view that low abundance miRNAs have no biological effects, because the cellular concentration of miRNA-binding sites is much, much greater than the concentration of miRNA. That is, the stoichiometric mechanism of miRNA-mediated repression in mammals requires that miRNAs be highly abundant. When DKs-8 cells obtain a miRNA, such as miR-222, from exosomes, does that new miRNA rank in the top 25% or 50% of miRNAs by abundance? If not, it is difficult to imagine how it could be functional, given the aggregate intracellular concentration of seed-matched target sites. The authors need to report an estimate of how many molecules of a given miRNA sequence are present per exosome and how many are delivered to an individual recipient cell.

4) Why were three perfect sites used? Were controls performed validating the reporter using anti-miRs and miRNA mimics?

5) In the ceramide experiments, the authors interpret the change in exosomal and cellular abundance for miR-100 and miR-320 as evidence that a subset of miRNA sorting is altered by ceramide while a separate, ceramide-independent pathway delivers other miRNAs to exosomes. The data are interesting, but don't seem to contribute to our understanding of the mechanism of putative sorting of miRNAs into exosomes. Perhaps miR-10b is simply less abundant than miR-100 or miR-320, making it harder to reliably detect changes in its abundance?

6A) High-Throughput Sequencing Data. How were the data normalized? How was the normalization procedure validated? Best practice is to select the normalization method that produces the greatest congruence among otherwise identical biologically independent replicates.

6B) Extending miRNA sequences {plus minus} 2 nt “to accommodate inaccurate processing of precursor miRNAs” would be a great idea if miRBase were always right; but miRBase is often wrong. It would be better to use the sequence of the most abundant isoform of the miRNA as the “accurately” processed form and to pool reads for all isoforms with the same 5′ end (i.e., the same seed sequence).

6C) Whenever read data is presented, species data should be presented in parallel. For example, the data in Figure 1 would have a very different meaning if most of the “repeat” sequences were from just a few species, rather than a diverse set of RNAs.
