# Peer review - Round 1

Editors:
- Todd C Mockler, Donald Danforth Plant Science Center , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.00011.025](https://doi.org/10.7554/eLife.00011.025)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for choosing to send your work entitled “Nascent-Seq Reveals Novel Features of Mouse Circadian Transcriptional Regulation” for consideration at eLife. Your article has been evaluated by a Senior Editor and 3 reviewers, one of whom is a member of eLife's Board of Reviewing Editors.

The Senior Editor (Detlef Weigel), the Reviewing Editor (Todd Mockler) and the other reviewers discussed their comments before we reached this decision, and the Reviewing Editor has assembled the following comments based on the reviewers' reports. Our goal is to provide the essential revision requirements as a single set of instructions, so that you have a clear view of the revisions that are necessary for us to publish your work.

General assessment:

Your data suggest that the circadian oscillation of mRNA transcription is only partly controlled by the transcriptional regulatory machinery, which is in contrast to what is currently accepted in the field. Your manuscript therefore addresses an important problem in circadian biology: what is the correlation between transcription and the mRNA levels measured by high-throughput techniques? In various organisms and tissues the cycling transcripts have been identified, however, the link between these stable mRNA measures, transcriptional activity, and post-transcriptional regulation has not been addressed on a global scale. The reviewers agreed that the principles behind the experiments are generally sound, that the manuscript is well written, and that with a few exceptions the experimental protocols and analysis methods are clear. This paper provides several key advancements in the field and provides a solid foundation upon which to build a better understanding of the transcriptional regulatory mechanisms and the contribution of post-transcriptional mechanisms to clock regulated gene expression.

Major concerns:

Several concerns relate to establishing whether the findings arising from the Nascent-Seq and mRNA-seq comparisons reflect genuine biological differences or are a technical artifact from comparing two different methods:

It is difficult to evaluate the conclusions drawn from the nascent Seq, mRNA-seq, and ChIP-seq experiments without knowing how much Illumina read data was acquired for each sample, and what the read mapping statistics were for each sample. Carefully describing the amount and types of sequence data is essential for interpretation and needs to be presented in the manuscript so that the reader can confirm that the conclusions are based on genuine biological phenomena. Also, you used strand-specific libraries for some of the experiments, but it is not clear in which ones, and if this could affect the analysis. Please provide this information, which can be presented in an additional table. How many genes were expressed in each sample (i.e. detected in the sequence data given some threshold of minimal expression) in the nascent Seq and mRNA-seq experiments needs to be given as well, as this will be a further measure of whether the depth of sequencing achieved for each sample was adequate.

A second question is whether the quantification method affect the variance. Is the read per base pair value adjusted for the total number of reads? If not, differences in sequencing depth could contribute to differences in variance. Further, the number of introns and extended regions in the nascent RNA data could affect the proportion of exonic sequence being sampled, biasing the sensitivity of the read per base pair measure. Appropriate normalization would contribute to ensuring the comparisons are as even as possible.

The comparison of mRNA levels in the same tissue from different labs has also resulted in non-overlapping sets of rhythmic transcripts. Is any of the difference in nascent RNA and mRNA levels from intrinsic biological variation or from the limitations of quantifying these molecules? How consistent are the mRNA and nascent RNA timecourses compared to themselves (e.g. the 6 samples of mRNA to the other 6 samples of mRNA). Since this will not provide sufficient resolution, other techniques to establish the similarity of the data sets can be used. What is the overlap with rhythmic data from other labs (using the same algorithms)?

There are several new comparisons and analysis methods described in this paper. It is essential that the approaches and analysis methods employed on this novel data are clearly explained and accessible to the community so that the experiments can be applied to other systems and comparisons with this work made. The description of the analysis methods provided in the materials and methods need to be detailed and where “custom scripts” are used, these scripts need to be made available.

Cycling nascent RNA and mRNA was compared with a time course from the livers of mice housed in 12:12 LD. Interpretation is hindered by use of a cycling light/dark cycle as it is impossible to distinguish which rhythms are truly circadian and which are light driven; collections in constant darkness would have been preferable. While the data presented is still compelling, this potential confounding factor needs to be addressed in a revised manuscript.

Comparison of rhythmic nascent RNA and mRNA (R-R) showed a weak overlap between the two data sets (only 41.6% of na-RNAs were also rhythmic at the mRNA level). However, it is unclear how this percentage was reached as the ratio of 342 (strong rhythmic nascent RNA) to 822 (total rhythmic nascent RNA) was used, but the authors indicate that 342 is representative of “rhythmically transcribed genes” (and suggest all cycling nascent RNA) whereas 842 represents “rhythmic RNA expression” (lines 114-116). Based on the figures provided, it is unclear how these numbers were obtained and further clarification is needed. A 28.4% overlap of oscillating Na-RNA and total mRNA (342/1204) was shown, which suggests a high amount of cycling mRNAs undergo post-transcriptional regulation that is critical for rhythmicity. However, it is unclear why only the strongly rhythmic nascent RNAs were used (342) instead of all cycling Na-RNAs (842) and this should be explained more clearly.

Summary:

The major issues the review team would like to see addressed relate to read depth, normalization and comparison methods, and improved descriptions of the methods to better explain how the data was processed and analyzed (for example, better explanations of key ratios used in data interpretation). The results of this study are very exciting, but it is important for the authors to convince the reader that the results reflect a genuine biological difference and do not reflect a technical artifact from comparing two different methods. The review team hopes your manuscript will be able to move forward with improved analysis and better explanation of this analysis, without the need for new data.
