# Peer review - Round 1

Editors:
- Nick Proudfoot, University of Oxford , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.00808.041](https://doi.org/10.7554/eLife.00808.041)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Condensin controls recruitment of RNA Polymerase II to achieve nematode X-chromosome dosage compensation” for consideration at eLife. Your article has been favorably evaluated by a Senior editor and 3 reviewers, one of whom is a member of our Board of Reviewing Editors.

The Reviewing editor and the other reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

This study describes the development of a new technique for mapping nascent TSS;GRO-cap. This powerful new technique has been applied to two aspects of C. elegans transcriptional regulation: mapping the nascent TSS of outrons and transcriptional regulation of X-chromosome inactivation. Both of these applications are important and publishable. However the first application needs further work/clarification.

1) Our main concern is the authors’ claim that a combination of GRO-seq and GRO-cap allows unequivocal assignment of new upstream TSS for C. elegans outrons (5’ end of mature mRNA is formed by SL1 trans-splicing and so doesn’t define gene TSS). For example, in the Discussion section, the authors state that they assign upstream TSS “by requiring that TSS calls be supported by uninterrupted GRO-seq signal for transcriptionally engaged Pol II between the GRO-cap TSS and the previously annotated 5’ end”. GRO-seq shows the presence of active polymerases, and hence, uninterrupted signal does not rule out the possibility of signal arising from multiple, partially overlapping transcripts. For example, if two tandem transcriptional units were located in close proximity, GRO-seq signal could appear continuous (especially as run-on can proceed after the TTS). This could explain the differences with the Chen et al (2013) data, which proposes that separate transcription units may exist upstream of outrons that could be enhancer derived transcripts (eRNAs).

Since this is a key issue we recommend further analysis on this point. To distinguish between these two possibilities, it would be necessary to analyse secondary promoters detected by GRO-cap and confirm that there are no 3’ ends at these positions (PMID: 20522740 or 21085120) that would break these very long outrons into two independent units.

Specific comments related to point 1: A) In Figure 1G, one can observe a secondary TSS in the position of the annotated WB start, in addition to the one described by the authors. Specifically, in the right panel (where the reads are centered on the GRO-cap determined TSS), a clear white line moving towards the right is apparent. To be able to appreciate how important this secondary TSS (located in the WB defined position) is with respect to the new ones defined by the authors, it would be useful make the same plot but using the GRO-cap data.

B) Figure 1–figure supplement 11: the fact that GRO-seq signal increases as it passes GRO-cap spikes does not prove that they are continuous transcripts with different 5’ UTRs. Partially overlapping tandem eRNA with lower expression level than the main transcript could produce the same pattern.

C) It seems to us that there is one limitation for the GRO-cap method that the authors did not discuss. Only elongating polymerases in the proximity of the TSS (e.g., <500bp?) will have a nascent RNA short enough to produce a sequencing library compatible with Illumina technology. Although that does not alter the discussed results in this case, this limitation should be stated for future users of the technique.

2) A way to further strengthen the argument that authentic TSS of outrons in many cases is distant to the mature mRNA 5’ end would be ChIP based analysis using Pol II CTD ser5 and ser2 specific antibodies. Thus could be performed on a few selected transcription units with amplicons covering the outron and 5’ half of the coding region.

3) Regarding the accumulation of Pol II at the 3’ end of genes. The authors suggest that extensive pausing at the 3’ end of genes may be linked to trans-splicing. In this context, it would be beneficial if the “not in operon genes” in the analysis presented in Figure 4B were further subdivided into monocistronic trans-spliced genes and non-trans-sliced genes. It would be interesting to see if non-trans-spliced genes also show Pol II accumulation at the 3’ end. In addition they should comment on the possibility that the high U content in the intergenic regions within operons (ur element that direct trans-splicing) and perhaps also at the 3’ end of genes could create a partial bias during GRO-seq and so skew the results for these regions.

4) The effect of scd2 mutant on dosage compensation and consequent effects on transcription uncovers that dosage compensation also affects small non-coding RNAs (miRNAs). Are there more miRNA affected by dosage compensation? What do they have in common? Do they regulate a group of genes with similar function?
