# Peer review - Round 1

Editors:
- Marina V Rodnina, https://ror.org/03e76ya46 Max Planck Institute for Biophysical Chemistry Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76562.sa0](https://doi.org/10.7554/eLife.76562.sa0)

The paper describes a method for single-molecule profiling of RNA modifications. The results not only solve many urgent questions in understanding rRNA modification, ribosome heterogeneity and ribosome biogenesis, they also provide a major step in developing technologies to probe the RNA epitranscriptome. The results are expected to be of broad interest for specialists in the RNA field.


---

# Peer review - Round 1

Editors:
- Marina V Rodnina, https://ror.org/03e76ya46 Max Planck Institute for Biophysical Chemistry Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76562.sa1](https://doi.org/10.7554/eLife.76562.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Concerted modification of nucleotides at functional centers of the ribosome revealed by single-molecule RNA modification profiling" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Marina V Rodnina as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by James Manley as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Katrin Karbstein (Reviewer #2); Guillaume F Chanfreau (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. The experiments with the helicase mutants may need additional controls. The modification pattern obtained with the cold-sensitive prp44 should be compared to that with the wt after a shift to the same non-permissive temperature. It would be necessary to perform a control experiment with a wild-type strain shifted to a similar temperature. Also, the dbp knockout analysis is performed at steady state while prp43-cs is a cold shift so it is quite difficult to compared the result directly.

2. The conclusion concerning the resilience of modification to stress should be supported by some considerations concerning the potential time frame of stress response vs. the time of synthesis of new ribosomes that could potentially have a different modification level. Regarding splicing perturbations, and with the exception of the dbr1 knockout, the mutants used in the study do not result in a major depletion of intron encoded snoRNAs so it is quite expected that there is no loss of modification at these positions. Similarly, the environmental stresses used are short, and are not expected to affect modification patterns in a major way considering the stability of ribosomes. Unless the authors perform sequencing on rRNAs synthesized after a shift into stress conditions, it is misleading to state that rRNA modification profiles are unaffected by environmental treatments.

3. Another issue that may need to be considered is the level of depletion of individual snoRNAs after depletion of the snoRNP proteins. It is possible that some snoRNAs are depleted more rapidly than others, and that this may affect the modification patterns. The authors should perform RNA sequencing of RNA samples used after depletion of Cbf5 or Nop58 such that they can directly correlate snoRNA levels to modification levels. Unless the authors provide these data, it is difficult to conclude whether specific sites are more or less resilient to genetic depletion of snoRNP proteins.

4. On p.10, the authors benchmark their method in challenging, hypermodified regions. More generally, modifications close to each other should be contained in some conventional datasets. As these are mostly correlated (or anticorrelated) some attempts to identify that in the existing data should be made.

5. The authors should analyze the correlated and anticorrelated sites in more depth and in particular consider the RNA secondary structure, as the base pairing to snoRNAs disrupts that (as well as RP binding). In fact, in a first look, it seems to me that the anticorrelated changes could be explained by competing binding of two distinct snoRNAs.

6. Why there are so few ribosomes reads in each sample. A typical Oxford Nanopore flow cell will typically yield ~1 million reads and yet it seems like only a few hundred make it into the figure.

7. There are definitely some hot spots for miscalled modifications in the IVT samples. Would be interesting to hear the author's thoughts on why these sights are miscalled. They mention a few examples later in the text, but a more thorough discussion is needed.

8. Non-full-length ribosomes are discarded. It's possible that 2'O-met may increase the stability of ribosomes by preventing inline hydrolytic cleavage. This may bias the presented data to 2'O-met modifications. This could be discussed.

9. The heatmaps are somewhat difficult to interpret. In all figures, the heatmaps could be enlarged and the cluster matrix and UMAP projections could be deleted or made smaller.

10. Figure 2D snR80 target should be 25S – Ψ766.

11. P5 – Line 112 "which either" needs rewording.

12. – Resistant of Um2921 of GM2922 to depletion of Nop58. The authors conclude this paragraph by saying that the "low number of ribosomes unmodified at these positions suggest that their modification may be essential for rRNA stability". This conclusion is incorrect, considering that Spb1 can methylate both Gm2922 and Um2921 when snR52 is depleted. So, the absence of unmodified rRNA upon depletion of Nop58 (or Cbf5) can be fully explained by the functional redundancy with Spb1.

13. "to a large extent, 2´O-methylation is independent of pseudouridylation in yeast rRNA (Figure 1D and 1E).": I would suggest changing the wording to " 2´O-methylation and pseudouridylation in yeast rRNA are independent of each other".

14. Figure 4 is incredibly hard to understand. I just could not grasp the information presented. I suggest that the authors find an alternative way to present the information.

15. P20 line 368. I do not think that the reference Piekna-Przybylska 2007 is correctly cited here. This paper is about "new bioinformatics package for research on rRNA nucleotide modifications in the ribosome" and it does not provide information related to the fact that synthesis of intron encoded snoRNAs is compromise d by mutations that affect splicing.

16. P21 – line 390. Alternative snoRNA maturation pathways independent of splicing. The reference Grzechnick et al. 2018 is not correct here, as this paper deals with independently transcribed snoRNAs that are not encoded within introns. Correct reference should be Ooi et al. 1998 or papers from the Bozzoni group that showed splicing independent processing of intron encoded snoRNAs in yeast.

Reviewer #1 (Recommendations for the authors):

1. The experiments with the helicase mutants may need additional controls. For example, the modification pattern obtained with the cold-sensitive prp44 should be compared to that with the wt after a shift to the same non-permissive temperature.

2. The conclusion concerning the resilience of modification to stress should be supported by some considerations concerning the potential time frame of stress response vs. the time of synthesis of new ribosomes that could potentially have a different modification level.

Reviewer #2 (Recommendations for the authors):

There are some ways the manuscript could be improved:

1. On p.10, the authors benchmark their method in challenging, hypermodified regions. More generally, modifications close to each other should be contained in some conventional datasets. As these are mostly correlated (or anticorrelated) some attempts to identify that in the existing data should be made.

2. I would suggest that the authors analyze the correlated and anticorrelated sites in more depth and in particular consider the RNA secondary structure, as the base pairing to snoRNAs disrupts that (as well as RP binding). In fact, in a first look, it seems to me that the anticorrelated changes could be explained by competing binding of two distinct snoRNAs…

Reviewer #3 (Recommendations for the authors):

I'm confused about why there are so few ribosomes reads in each sample. A typical Oxford Nanopore flow cell will typically yield ~1 million reads and yet it seems like only a few hundred make it into the figure.

There are definitely some hot spots for miscalled modifications in the IVT samples. Would be interesting to hear the author's thoughts on why these sights are miscalled. They mention a few examples later in the text, but a more thorough discussion is needed.

Non-full-length ribosomes are discarded. It's possible that 2'O-met may increase the stability of ribosomes by preventing inline hydrolytic cleavage. This may bias the presented data to 2'O-met modifications. This could be discussed.

The heatmaps are somewhat difficult to interpret. In all figures, the heatmaps could be enlarged and the cluster matrix and UMAP projections could be deleted or made smaller.

Figure 2D snR80 target should be 25S – Ψ766.

P5 – Line 112 "which either" needs rewording.

– Resistant of Um2921 of GM2922 to depletion of Nop58. The authors conclude this paragraph by saying that the "low number of ribosomes unmodified at these positions suggest that their modification may be essential for rRNA stability". This conclusion is incorrect, considering that Spb1 can methylate both Gm2922 and Um2921 when snR52 is depleted. So the absence of unmodified rRNA upon depletion of Nop58 (or Cbf5) can be fully explained by the functional redundancy with Spb1.

"…to a large extent, 2´O-methylation is independent of pseudouridylation in yeast rRNA (Figure 1D and 1E).": I would suggest changing the wording to " 2´O-methylation and pseudouridylation in yeast rRNA are independent of each other".

Figure 4 is incredibly hard to understand. I just could not grasp the information presented. I suggest that the authors find an alternative way to present the information.

P20 line 368. I do not think that the reference Piekna-Przybylska 2007 is correctly cited here. This paper is about "new bioinformatics package for research on rRNA nucleotide modifications in the ribosome" and it does not provide information related to the fact that synthesis of intron encoded snoRNAs is compromise d by mutations that affect splicing.

P21 – line 390. Alternative snoRNA maturation pathways independent of splicing. The reference Grzechnick et al. 2018 is not correct here, as this paper deals with independently transcribed snoRNAs that are not encoded within introns. Correct reference should be Ooi et al. 1998 or papers from the Bozzoni group that showed splicing independent processing of intron encoded snoRNAs in yeast.
