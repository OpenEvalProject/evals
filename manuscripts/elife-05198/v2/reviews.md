# Peer review - Round 1

Editors:
- Roderic Guigó, Center for Genomic Regulation , Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.05198.017](https://doi.org/10.7554/eLife.05198.017)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “The majority of transcripts in the squid nervous system are extensively recoded by A-to-I RNA editing” for consideration at eLife. Your article has been favorably evaluated by Chris Ponting (Senior editor) and 2 reviewers, one of whom is a member of our Board of Reviewing Editors.

The Reviewing editor and the other reviewer discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

The paper by Alon et al. is a well-performed, concise study that shows extensive RNA editing in the squid genome. Since the extent of editing is several orders of magnitude larger than that reported in the human genome, and actually in any other metazoan species, the results are obviously of biological relevance, and therefore appropriate for eLife. The manuscript also describes a novel bioinformatic method to identify editing sites. Overall, the manuscript is well written and both Methods and Results are clearly explained.

Despite being unexpected, the results appear to be quite robust: the control in primates shows that they are not an artifact from novel pipeline employed to predict editing sites in absence of assembled genome sequences. The strong bias to AG mismatches, the clustering pattern in genes, the neighbor preferences, the tissue specificity (irrespective of biological origin), the resulting recoding events towards the common amino-acid, etc., all these strongly support the editing sites found by the authors.

1) The de novo transcriptome assembly is a very trivial computational issue. Many false positives are expected at least in complex mammalian transcriptomes. Paralogs could affect the reconstruction of real isoforms leading to a sort of chimeric transcripts. In addition, alternative splicing may complicate transcript reconstruction. Are there estimations about the impact of alternative splicing and paralogs in squid? Any impact of this on the results should be discussed in the text. Also, the text should clarify that this is not a completely de novo method since genomic sequences are generated.

2) The strategy is biased towards the RNA editing prediction in protein coding regions (CDS). Can RNA editing events be detected also in non-CDS regions by the method? If not, this should be clarified in the text. Related to this, evidence of RNA editing in repetitive regions in squid could potentially be interesting, probably revealing an opposite trend than mammals.

3) Regarding methodology, can the statistical binomial test detect any significant change in the non-AG positions? If yes, how do you explain this finding?

The average RNA and DNA coverage is high but regarding RNA editing candidates, are there filters to exclude low covered sites? What is the minimal coverage for RNA and DNA?

Did you apply filters to RNA and DNA reads? I mean reads with low quality and positions at read ends.

4) Have the authors considered the possibility that their results arise from somatic genomic editing, rather than RNA editing? While for the human and macaque control, the RNA and DNA samples are from the same tissues, in the case of squid, RNA samples are from the tissues from the nervous system, while DNA is from the sperm sack. To unequivocally conclude that the observations are indeed from RNA editing, I guess that DNA and RNA need to be from the same biological source. Maybe the investigation of the distribution of the relative proportion of reads supporting and not supporting the edit could help here.

5) Related to the above, the authors used RNA only from tissues from the nervous system. Therefore, it is not possible to assess whether the phenomenon observed is characteristic of this system, or it is actually systemic in the entire organism. I think that sequencing RNA from some other non-nervous tissue could help to distinguish between the two hypotheses.

6) Regarding the characterization of RNA editing events, events tend to be tissue specific. Are there events showing tissue specific levels? That is, cases in which the gene locus in expressed at the same level in all tissues but editing levels are different.

7) It is a little bit disappointing that there is limited investigation in the potential mechanisms behind the extensive editing observed. The authors could have at least investigated ADAR with some additional detail. The RNA (and DNA sequence) helps to delineate the ADAR sequence, and the RNA reads to estimate expression levels. Are there multiple copies of ADAR in the squid genome? Is ADAR expressed at comparatively higher expression levels than in organism with low editing levels (they can use the mouse and human samples to make this comparison? Has the ADAR sequence in squid diverged faster than expected? In specific domains? All these questions are quite simple to answer.

8) The authors also provide an adaptive explanation to the high levels of editing observed in the squid genome, and hypothesize that, in contrast to current assumptions, that extensive editing is common as a way to cope with temperature adaption, except in mammals that, as homeotherms, would not require such a process. This is, by the way, reminiscent of the isochore theory by Bernardi that would separate homeotherm vertebrates from “cold-blooded” (poikilotherm) vertebrates (to which, by the way, the authors may want to cite). If the authors were correct that would indeed be a quite relevant result. They could easily employ their pipeline in available vertebrate RNAseq data (for instance, http://www.sciencemag.org/content/338/6114/1587.full) to test this hypothesis.
