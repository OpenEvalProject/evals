# Peer review - Round 1

Editors:
- Patrick Cramer, Max Planck Institute for Biophysical Chemistry , Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.09945.017](https://doi.org/10.7554/eLife.09945.017)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for submitting your work entitled "RNA polymerase errors cause splicing defects and can be regulated by differential expression of RNA polymerase subunits" for peer review at eLife. Your submission has been evaluated by James Manley (Senior Editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

In this manuscript, Carey describes a computational method called MORPhEUS that allows measuring RNA polymerase error rates using published RNA-seq data. By counting the number of matches and mismatches to the reference genome after technical errors are minimized, MORPhEUS enables the author to estimate the error rate at each position of the genome. Using chromatin-associated RNA from RNA-seq data in K562 cells, the author calculates error rates at splice site junctions and demonstrates that these are higher at 5` splice sites, suggesting that this could affect intron retention. Using ENCODE RNA-seq data, the author further investigates if the expression level of the Pol II subunit Rpb9, known to be required in Pol II fidelity, affects RNA polymerase error rates in different cell lines. Furthermore, the author measures RNA-seq error rates using two yeast strains in which it is possible to modulate the expression of Rpb9 or Dst1, finding that cells with low expression of Rpb9 or Dst1 possess higher error rates, consistent with known biochemical and genetic data. The idea is intriguing and the explanations for observations in terms of Pol II error rates make sense. The proposed method MORPhEUS is appropriate to perform comparative analysis of RNApol induced transcription errors between two or more samples or to identify RNApol errors leading to intron retention. Other than currently available methods this approach is able to identify errors transcriptome-wide and does not "require specialised organism-specific genetic constructs", therefore it seems to be highly useful. The method presented here is interesting and it is a valuable tool for estimating RNA Pol II error rates from RNA-seq data, although several points need to be addressed before publication can be considered.

Essential revisions:

1) Possible alternative explanations for the observations

A main issue with this manuscript is that alternative explanations could also make sense. The author has to show that his explanations are the only or at least most plausible ones. Figure 2b is central to the proposed method. It shows an elevated rate of errors at the uracil in the 5' splice site of the canonical GU-AG introns selected by the author. The explanation given is that Pol II errors in the U lead to intron retention. Why then is the error rate of the guanine not similarly elevated? One would then also expect to see elevated error rates for the conserved AG motif of the 3' splice site and in the well conserved branch point motif. The analysis of these motifs should confirm the interpretation by the author. Because this data is not shown, does that mean no elevated signal has been observed? How can this be explained in the light of the author's interpretation of Pol II errors at splicing motifs leading to retained introns? Since the only position with elevated error rate seems to be the U at the 5' SS, an alternative explanation (probably not the only possible one) could be that some factor strongly binds to the uracil in such a way that the reverse transcription in the RNA-seq protocol causes the uracil to be misread. Note that U->C mutations are also observed in PAR-CLIP and are known to originate during reverse transcription of the RNA.

2) Choice of null model

Figure 2b shows relative error rates on the y-axis. The error rates observed around 5' splice sites are normalized by the error rates seen for the same dinucleotides, GT, at other places in the transcriptome. The 4-fold elevated error rate therefore depends on the null model. It would be important to compute the relative error rate at the uracil with more refined trimer null models to see if the 4-fold increase holds up. Two versions, one with the mutated nucleotide at the first position and another model with the mutated nucleotide at the last of the three trimer positions, should be used. The latter version could model sequence-dependent effects during reverse transcription. For each trimer in the transcriptome one can compute the error rate at the first and third nucleotide. Then, the total mutations for each position around the 5' splice site (and the 3' splice site and branch point) are divided by expected numbers of mutations, which is simply the sum of error rates for each of the trimer contexts for the position.

3) Effects of Rpb9

The author demonstrates that expression of Rpb9 negatively correlates with error rates in human cell lines, suggesting that the differential expression of Rpb9 affects RNA polymerase fidelity in vivo. The level of mRNA expression does not necessarily correlate with protein level and, more importantly, the author should normalize the expression of Rpb9 with another subunit of Pol II (e.g. Rpb3) in each cell line used for the analysis (Figure 2c). An alternative explanation for Figure 2c and Figure 3b would be that changing Rpb9 and TFIIS concentration from its finely regulated value impairs elongation, which in turn can influence splicing rates and splicing efficiency. (See e.g., Lacadie et al., In vivo commitment to yeast cotranscriptional splicing is sensitive to transcription elongation mutants, Genes Dev. 2006.) Can such alternative explanations be excluded? Further, in Figure 3b the author shows that intron retention is higher under conditions of low Rpb9/Dst1 induction. Is the low induction of Rpb9 or Dst1 affecting the same introns? Does the author find a higher error rate in GT 5´ donor site in the mRNAs that show intron retention?

4) Possible bias resulting from conservation

To measure the error rates at splicing junctions, the author counts errors at each position relative to 5´ donor sites, using reads spanning intron-exon junctions centered on GT donor sites. As a result, the errors at the T nucleotide are more enriched compared to other positions. It is not clear if the analysis is performed measuring the average GT error rate comparing all the reads at intron-exon junctions or single mRNAs (Figure 2a, 2b). If the analysis is made using all genes, since GT at intron-exon is a conserved sequence and the flanking regions are not, this could lead to a bias. This must be clarified.

5) Suggestions for additional controls

A positive control would be to analyse RNA-seq data of an organism with a mutated polymerase known to have an elevated mutation rate and to show that this mutation rate leads to higher relative error rates at conserved splicing motifs. A negative control would be to analyse RNA-seq data of a mutant organism with a known transcription elongation defect and to show that the elongation defect does not affect the putative Pol II error rate in a similar way as Rbp9 and TFIIs overexpression. If possible we encourage the author to conduct these controls.

6) Repetitive reads

In paragraph four the alignment quality filter procedure is explained. However it is not mentioned how repetitive reads (or potentially repetitive reads in e.g. unknown duplications of genes) are handled and might affect the result. This must be clarified.

7) Possible bias from coverage

Not counting identical mismatches occurring twice or more at the same position (paragraph four) is problematic, because:

– This needs to be adjusted by depth-of-coverage at each position. Positions with high coverage are much more likely to have the same 'real' RNApol error twice, than positions with low coverage. (This seems to be so obvious that we might have overlooked the explanation of the normalization procedure)

– RNA polymerase errors seem to be biased to e.g. C->T (see Figure 3c), making it quite a bit more likely to see exactly the same RNApol error twice at a position for C->T/G->A.

In general the uncertainty of RNApol error estimates at low coverage positions (i.e. lowly expressed genes) should be much worse than for high coverage (highly expressed genes). Is this addressed in the algorithm? (Maybe this problem has been discussed but missed by reviewers.) If not it needs some clarification, how different depth-of-coverage and mutation bias is considered when estimating the errors or removing mismatches of the same type.
