# Peer review - Round 1

Editors:
- Gene W Yeo, University of California, San Diego United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.69457.sa1](https://doi.org/10.7554/eLife.69457.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

Yang and colleagues report circFL-seq a method for sequencing full length circular RNAs with rolling circle RT and nanopore sequencing. While two other methods have recently been published, this manuscript does add to a growing literature on long read sequencing of circular RNAs.

Decision letter after peer review:

Thank you for submitting your article "circFL-seq reveals full-length circular RNAs with rolling circular reverse transcription and nanopore sequencing" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and James Manley as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Fangqing Zhao (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. Reviewers all agree that a major weakness of the present manuscript is with the comparison to existing methods. The authors should compare circFL-seq to CIRI-long, and reviewers agree that a three way comparison to isoCirc is informative. The authors should accompany their comparisons with a discussion about strengths and weaknesses of each of the methods.

2. The current claims and conclusions that circFL-seq is the superior method is not well supported by their data in this version of the manuscript. The authors should provide fair critiques of the other method (see comments about ligation). The authors need to point out potential limitations. For example, Is CircFL-seq biased to detecting only highly expressed transcripts?

3. In comparison to isoCirc, circFL-seq identified fewer circRNA isoforms with higher read coverage of the detected circRNAs, which may be a PCR artifact. The authors need to address this concern. In addition, in two published studies, isoCirc and CIRI-long have also used nanopore sequencing to characterize circRNA isoforms and alternative splicing events. However, both studies have reported a relatively higher percentage of retained introns (isoCirc: Figure 4b, CIRI-long: Supplementary Figure 13) compared to the number of 3.5% of intron retention events in line 139. The authors should clarify the reason behind this difference.

4. The authors found six f-circ derived from GBF1-MACROD2 fusion and validated their junctions using Sanger sequencing. Besides, the authors also used short-read RNA-seq to validate the linear fusion junctions. What's the ratio of linear and circular transcript derived from these gene fusion loci? Is there any possibility that these f-circRNAs are derived from trans-splicing events? Considering that short-read RNA-seq data cannot effectively distinguish circular and linear transcripts, the authors may try to search for nanopore reads spanning the fusion region, which can provide direct evidence for these gene fusion events.

5. Because of the high error rate of nanopore sequencing, the authors should compare the error rate of CS sequence before and after cRG correction to elucidate the ability to correct sequencing errors with the cRG mode.

6. The authors trained a random forest classifier to predict the strand origin of circular reads. How many CCRs were used as the training set, and how's the performance of the random forest classifier? The authors should provide more data about this step.

General comments:

1. The Figures and Supplemental Figures were not labeled with figure numbers, making it extremely difficult to read (especially some figures span across more than one page). The authors should label the figure number more clearly.

2. Some figures are not clearly labeled. For example, in Figure 2j, what does each lane represent? Also, in Figure 3e, it is not clear what the y-axis is. The authors state that it is read coverage, but how come the value is from 0 to 1? In Figure 3d, the authors state that it is the correlation between HeLa and SKOV3, but it was not clear what axis is HeLa and SKOV3, respectively. Again, what does the shaded area mean in these figures (figure 3c, 3d, 3f, and 3g)? The authors should check through the figure label more carefully and correct them accordingly.

Reviewer #1 (Recommendations for the authors):

Overall, this is a nice piece of work that can be published after revision. Below are my specific comments for the authors:

1. As noted in my public review, the authors should carry out a two-way comparison between circFL-seq and CIRI-long, as well as a three-way comparison between circFL-seq, CIRI-long, and isoCirc. Given that circFL-seq and CIRI-long are both based on RCRT while isoCirc is based on RCA, it would be interesting to see if circFL-seq and CIRI-long produce more concordant results in terms of the discovery and quantitation of full-length circular RNAs, given the similarity in their experimental strategies.

2. In both Introduction and Discussion, the authors noted that the use of ligation in isoCirc may lead to false discoveries of circular RNAs. While this statement is technically correct from an experimental standpoint, such false discoveries can be recognized and removed computationally – therefore this is not a fair critique of isoCirc. In fact, the isoCirc computational pipeline is designed to remove such artifacts, using stringent requirements for alignment quality and presence of canonical splice site motifs in all forward and back splice junctions within full-length circular RNA transcripts.

3. Line 65-67: "Thus, an accurate but affordable method to detect full-length circRNA remains to be developed for wide application in screening functional circRNAs at the omics scale". This statement leaves the impression that such a method currently does not exist, which is not a fair representation of the current literature with the recent publications of isoCirc and CIRI-long.

4. The authors reported that compared to isoCirc, circFL-seq produced more full-length circular RNA reads at the same library depth but identified fewer circular RNA isoforms. The authors appeared to present this finding as a positive feature of circFL-seq. For example, in line 265-267, the authors stated that "as a trade-off, isoCirc produced fewer reads with the same sequencing depth, which raised sequencing costs and weakened its ability to detect and accurately quantify high-quality circRNAs". There are multiple issues with this statement. In terms of the precision of circular RNA quantitation (e.g. as evaluated based on comparison among nanopore replicates as well as comparison to short-read RNA-seq data), the metrics presented for circFL-seq are in fact quite comparable to the metrics presented in the isoCirc paper, so there is no evidence that circFL-seq provides a better quantitation of circular RNAs. Moreover, given that the ground-truth is not known, an alternative interpretation to this observation is that circFL-seq may be biased towards highly expressed circular RNAs, and may lack the ability to discover moderately and lowly expressed circular RNAs. Overall, in comparing different methods, the authors should aim to provide an impartial discussion about the strengths and weaknesses of individual methods, and avoid over-interpreting the data in favor of their own method.

5. The discussion about CDR1as is interesting. Can CIRI-long detect this circular RNA?

6. The authors should also cite the BioRxiv preprint by Rahimi et al., (https://doi.org/10.1101/567164), which is another method for nanopore sequencing of circular RNAs.

7. Overall, the manuscript is easy to read and follow, but it could benefit from a thorough editing by a language editor.

Reviewer #2 (Recommendations for the authors):

1. In comparison to isoCirc, circFL-seq identified fewer circRNA isoforms with higher read coverage of the detected circRNAs. This raises a concern that the outcome may result from that RCRT captures circRNA less efficiently than RCA, resulting in fewer circRNA molecules are captured in circFL-seq. The higher read coverage may simply come from sequencing the same circRNA molecule from the PCR amplification artifacts. This may also explain why circFL-seq cannot detect circRNAs with low read count or lowly expressed circRNAs. In this case, the authors cannot use back splice junction (BSJ) detection saturation as an indicator to compare the required read-depth between isoCirc and circFL-seq. Also, given the concern above, the "high read coverage" does not necessarily mean "high quality" nor "high accuracy" as claimed by the authors. The authors should address this concern before claiming on the benefits of high read coverage.

2. The advantages of circFL-seq over other existing technologies are not well-supported. For example, the authors claim that RCRT has lower residual linear RNA contamination than RCA, but the authors do not provide any data or evidence supporting the claim. Also, the authors claim that the circFL-seq gives higher circRNA read coverage; hence it is beneficial for circRNA quantification. However, the real "benefits" over other technologies (RNA-seq and isoCirc) for circRNA quantification are not clear since the RNA-seq (and isoCirc) quantification is significantly correlated with circFL-seq as demonstrated by the authors.

3. In the manuscript, the results are often comparable with known database and existing technologies when the authors focus on the "high quality" circRNAs only (circFL-seq read counts >= 5) which also have high expression level. The fact suggests that circFL-seq result is trust-worthy on "high quality" only. It also suggests that circFL-seq may fail to detect the lowly expressed circRNAs. The authors should note and discuss these limitations.

General comments:

1. The Figures and Supplemental Figures were not labeled with figure numbers, making it extremely difficult to read (especially some figures span across more than one page). The authors should label the figure number more clearly.

2. Some figures are not clearly labeled. For example, in Figure 2j, what does each lane represent? Also, in Figure 3e, it is not clear what the y-axis is. The authors state that it is read coverage, but how come the value is from 0 to 1? In Figure 3d, the authors state that it is the correlation between HeLa and SKOV3, but it was not clear what axis is HeLa and SKOV3, respectively. Again, what does the shaded area mean in these figures (figure 3c, 3d, 3f, and 3g)? The authors should check through the figure label more carefully and correct them accordingly.

Specific comments:

1. In the Abstract section, the authors claim that "… the detection of cancer-related fusion circRNAs…". However, the authors did not provide any data or literature suggesting that the fusion circRNAs they identified by circFL-seq are really "cancer-related" or biologically meaningful. The claim needs to be revised or proved.

2. In Figure2—figure supplement 1a, the full-length circRNA reads contribute very little percentage of the total clean reads (~2-5%). How come the RCRT method generate so little full-length circRNA reads? The authors should comment on this and discuss it.

3.In Figure 3—figure supplement 3, the author claim that more reads are required for ONT to confidently identify circRNAs. Doesn't this compromise the cost-efficient claim of circFL-seq made by the authors earlier? The authors should comment on this and discuss it.

4. In Figure 3—figure supplement 6a-d, how the saturation curves are calculated? It seems like isoCirc has much lower sequencing depth (~0.3 M) than circFL-seq. How do the authors compare the BSJ saturation in this case?

5. When comparing the validity of circFL-seq and isoCirc, why do the authors focus on top 100 expressed BSJ only? A better comparison should be the total BSJ in circFL-seq and isoCirc.

6. The authors should not use the same absolute circFL-seq BSJ read counts to define high-quality BSJs in isoCirc for the following reasons: (i) the read counts >= 5 in circFL-seq is arbitrary, there is no evidence suggesting that the isoCirc should use the same read counts to define high-quality BSJs. (ii) Since isoCirc captures more circRNAs, a lower BSJ read counts per circRNA is expected given the same sequencing depth. In both cases, lower BSJ read counts in isoCirc does not necessarily mean the BSJ is not "high-quality". Thus, the authors should not use absolute circFL-seq BSJ read counts as an indicator for the BSJ quality in isoCirc.

7. In the PLOD2 circFL-seq and RNA-seq example shown by the authors, the authors suggest that the circPLOD2 has lower exon skipping event than its parent linear RNA in HeLa cells. However, given that the BSJ is exactly the same between exon-skipped and non-exon-skipped circPLOD2, how does the back-splicing mechanism distinguish different parent linear RNA isoforms that selectively back-splices the non-exon-skipped linear RNA to generate specific circPLOD2 isoform in HeLa cells?

8. Are the f-circ detected by circFL-seq generated by RNA fusion or genomic fusion? Although the RNA-seq suggests a genomic fusion, it does not completely eliminate the possibility of a genomic fusion. A genomic PCR followed by Sanger sequencing should be performed to validate the fusion junction of the genome.

Reviewer #3 (Recommendations for the authors):

Considering that there are two recently published circRNA reconstruction tools based on nanopore sequencing, the authors should comprehensively compare their method with these two tools, and carefully discuss the advantages and disadvantages of these methods.

Specific comments:

1. In the Discussion section (line 260-262), the authors compared circFL-seq with the recently published CIRI-long method. Both circFL-seq and CIRI-long use a similar rolling circle reverse transcription strategy to amplify circRNAs. The authors may discuss the difference and (dis)advantages between their method and previous methods (isoCirc and CIRI-long).

2. In section "Comparison with RNA-seq and isoCirc for circRNA detection", the authors compared circFL-seq with the isoCirc method and found that circFL-seq produced more circular reads but identified fewer circRNA isoforms, which is an interesting result. Does it mean that isoCirc has a better sensitivity or higher false discovery rate in detecting lowly expressed circRNAs? The authors should include more comparison (e.g. venn diagram between three sets under different BSJ thresholds) between circFL-seq, isoCirc, and public circRNA database (e.g. circAtlas [PMID: 32345360, PMID: 30893614]) to demonstrate the advantages of their method.

3. The authors found six f-circ derived from GBF1-MACROD2 fusion and validated their junctions using Sanger sequencing. Besides, the authors also used short-read RNA-seq to validate the linear fusion junctions. What's the ratio of linear and circular transcript derived from these gene fusion loci? Is there any possibility that these f-circRNAs are derived from trans-splicing events? Considering that short-read RNA-seq data cannot effectively distinguish circular and linear transcripts, the authors may try to search for nanopore reads spanning the fusion region, which can provide direct evidence for these gene fusion events.

4. Because of the high error rate of nanopore sequencing, the authors should compare the error rate of CS sequence before and after cRG correction to elucidate the ability to correct sequencing errors with the cRG mode.

5. The authors trained a random forest classifier to predict the strand origin of circular reads. How many CCRs were used as the training set, and how's the performance of the random forest classifier? The authors should provide more data about this step.

6. In section "Evaluation of quantification of full-length circRNAs", it would be nice if the authors could compare the quantification results between their method on nanopore reads and previous method (e.g. CIRIquant) on short-read RNA-seq data.

7. The authors used different names (circFL-seq, circfull) to denote their sequencing and data analysis methods. It would be better if they can unify the name, say, circFL-seq, which may avoid misunderstanding.
