# Peer review - Round 1

Editors:
- Diethard Tautz, Max Planck Institute for Evolutionary Biology , Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.03523.026](https://doi.org/10.7554/eLife.03523.026)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Long non-coding RNAs as a source of new peptides” for consideration at eLife. Your article has been favorably evaluated by Aviv Regev (Senior editor) and 3 reviewers, one of whom is a member of our Board of Reviewing Editors.

The Reviewing editor and the other reviewers discussed their comments extensively before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

This paper adds to the current active discussion on the coding potential of lncRNAs, the role of short open reading frames and the emergence of new genes. The authors use published ribosome association datasets, but use several analysis pipelines that go beyond the analysis that has previously been done with these data. However, there are two comparable published papers that do similar analysis, namely Ingolia et al. 2011 and Guttman et al. 2013. While the former had suggested much translation of lncRNAs, the latter denies this, although there is some overlap of authors.

Major comments that need to be addressed by additional analyses and/clarification:

The crucial point is in how far ribosome associations are partly artifacts. The fraction of lncRNAs that the authors find to be associated with ribosomes is very large. Is this because the vast majority of transcripts actually are scanned by ribosomes, or could this observation be an artifact of the way the ribosome profiling data was analyzed? Pseudo-genes, and bona-fide human lncRNAs with known non-coding functions, were investigated, but the authors found evidence of ribosome binding in these putative negative controls, i.e. possible evidence for artifacts. This issue needs to be resolved more clearly, since the current paper should go beyond the Guttmann et al. 2013 line of arguments. It is necessary to provide a convincing demonstration that the analysis of ribosome profiling data is based on signal, not on noise. This could be done by different means, for instance by deriving null models describing what fraction of transcripts would be expected to be found associated with ribosomes if all of the ribosome profiling data was random, or by calculating otherwise a False Positive Rate or False Discovery Rate in the calling of “ribosome association” per transcript. You can also try something like the Bazzini 2014 or the Carvunis 2012 method. Another possibility is to choose a class of sequences with very low ribosomal association (maybe 3'UTRs are best) and use that as an upper bound on the false positive rate. The lower bound on the false positive rate is zero, and likely to remain there, but calculating an upper bound is something that should be added.

The claim is also made that these short and hard-to-annotate protein-coding genes look young according to protein-coding metrics and PN/PS. While plausible, it is also possible that they represent a mixture of genes of all ages combined with sequences that, while perhaps translated at some level, are not really genes in the functional sense of the word (at least not yet), and whose existence is therefore highly transient in evolutionary time. Contamination with these sequences could create the same statistical effect as having young genes. The presence of such contamination is also a critical piece of evidence in theories of how de novo protein birth occurs. This basically means that there are two interpretations of the data, both interesting, and not mutually exclusive. This needs to be better clarified. For instance the results of the BlastP search against codRNAs (supplementary file 8) and the results of the BlastX search against nr could be merged into one table or bar graph counting the number of BlastP and BlastX hits in lncRNA-noribo, lncRNA-ribo, and codRNA, separately, for each species.

It is unclear why the starved conditions (Table 1) were used in the yeast riboprofiling data. Starvation represses translation and therefore makes the data unreliable as a marker of translation. This should therefore be redone, perhaps with the rich media conditions of Ingolia et al. 2009, but if this needs to be redone anyway, ideally with the much higher coverage data of Artieri & Fraser.
