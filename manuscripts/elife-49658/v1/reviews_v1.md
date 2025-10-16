# Peer review - Round 1

Editors:
- Yue Wan, A*STAR Singapore

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.49658.sa1](https://doi.org/10.7554/eLife.49658.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Studying the full transcriptome complexity and processing is key to understanding the biology of any organism. While the advent of RNA sequencing using short-read sequencing has greatly enriched our understanding of the transcriptome, challenges due to short-read sequencing include difficulties in mapping uniquely to individual isoforms, and assembling full transcripts, especially in repeat regions. In addition, the need to convert RNA into cDNA libraries for sequencing can result in artifacts in transcript annotation due to template switching of reverse transcriptase enzymes, and cDNA sequencing limited in its ability to detect RNA modifications. Using nanopore direct RNA sequencing, the authors updated the annotation of the Arabidopsis transcriptome by identifying new antisense transcripts, new splicing patterns, 3' end usage, polyA tail lengths and full length transcripts using 5'cap capture. In addition, using a mutant of the m6A writer in Arabidopsis (vir-1 mutant), and vir-1 mutant reconstituted with vir-1, the authors used increased error rates in direct RNA sequencing to detect m6A modifications transcriptome-wide. The authors showed that m6A modifications impact RNA stability and circadian cycles are associated with 3' end formation in arabidopsis. The paper is very informative in the utility and limitations of using direct RNA sequencing to interrogate transcriptomes and the strategies described in the manuscript is widely applicable to not only Arabidopsis but also to any biologist interested in their transcriptome of choice.

Decision letter after peer review:

Thank you for submitting your article "Nanopore direct RNA sequencing maps an Arabidopsis N6 methyladenosine epitranscriptome" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Christian Hardtke as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This is a timely manuscript to demonstrate the utility of direct RNA sequencing in discovering transcriptomic features in the model organism Arabidopsis thaliana. In addition to studying the primary sequences of the transcriptome, including 5' ends, splicing and polyA+ tail length, the authors also utilized direct RNA sequencing to identify m6A modifications in vir-1 mutants and in vir-1 mutants with restored VIR activity. They found that m6A modifications is associated with 3' end processing in Arabidopsis thaliana. Overall the manuscript is well written and interesting.

We have suggestions to improve the manuscript to increase the impact of the novelty and utility of using direct RNA sequencing, as well as the technical strength of the manuscript by adding controls and performing validations to determine the accuracy of the new signals that they find.

Essential revisions:

1) For polyA tail length determination- could the authors show accuracy of their polyA tail determination on a set of standards with known poly(A) tail lengths?

2) 75% of the author's adapter ligated library failed to align to the transcriptome. The authors should look into the failed reads to explain why this is so.

3) For transcripts with new 5' ends identified by 5'end capture, the authors should validate of the new 5'ends using 5'end RACE.

4) A set of RNAs with known m6A sites should be generated to determine the accuracy and sensitivity of the author's method in detecting m6A to other available softwares, such as Tombo from Nanopore, as well as other published methods including (https://www.biorxiv.org/content/10.1101/525741v1). The authors should also comment on the robustness of their method with regards to new software changes.

5) The authors should show data on the correlation between sequencing depth and the ability to detect m6A modifications. They should also do deeper analysis to look at the nucleotide composition of the called m6A modifications that they capture, as well as whether there is potential bias towards capturing modifications on specific transcripts.

6) Direct RNA sequencing benefits from the aspect that it is long read, single molecule sequencing. As such, there is the possibility of "phasing" modifications that cannot be performed using short-read sequencing. The authors should show some examples of RNAs with more or less modifications than expected and attempt to associate that with RNA processing to demonstrate the utility of direct RNA sequencing.

Reviewer #1:

The possibility to perform RNA sequencing in its native form, without the requirement of cDNA synthesis, represents a major significant advance in RNA biology. Within this context, in this manuscript Matthew Parker and colleagues applied the Oxford Nanopore direct RNA sequencing to characterize the profiling of RNA transcripts in the model plant Arabidopsis thaliana. In the first part of the manuscript, the aim of this research is to: 1) prove that the Nanopore direct RNA sequencing has the ability to detect long, complex mRNAs under an acceptable error rate and to resolve a great complexity of splicing events; 2) prove that the over-splitting and spurious antisense reads generally occurs at low frequency in Nanopore direct RNA sequencing; 3) prove that Nanopore direct RNA sequencing can be used in estimation of poly-A tail length; 4) prove that Nanopore direct RNA sequencing using Cap-dependent capturing is effective in detecting authentic mRNA 5′ ends by using a convolutional neural network classifier of raw signals. In the second part, the authors present a direct RNA sequencing-based approach to detection of m6A methylation in data produced from both the vir-1 mutants defective in m6A and the vir-1 mutants restoring VIR activity. Furthermore, taking advantage of long read sequencing, the authors found that VIR activity is associated with the maintenance of 3' end formation of mRNAs. Overall, this manuscript describes a scientifically sound investigation of an important scientific area, that of epitranscriptomics. This manuscript will no doubt be a valuable resource to the growing field of direct RNA sequencing. I recommend this manuscript for publication in eLife.

I have some specific points detailed below.

1) In the supplementary Table 1, only 25% and 27% of sequencings reads in the 5' adapter ligation library could be mapped to the TAIR10 genome. The authors should check the sequencing reads to explain in detail the reason for the failed alignment in a large majority of sequencing reads.

2) Subsection “Differential error site analysis reveals the m6A epitranscriptome”, 17,491 sites with a more than two-fold higher error rate in the VIR-complemented line with restored m6A. Are these error sites exclusively located in adenine positions? A nucleotide composition summary is required to improve clarity.

3) Subsection “Spurious antisense reads are rare or absent in nanopore DRS”, the absence of reads mapping to antisense to RCA suggests that spurious antisense is rare or absent from Nanopore direct RNA sequencing data. Is it a generally accepted that the genomic loci of RCA do not generate antisense transcripts? If so, this information should be included.

4) The webpage (https://github.com/bartongroup/Simpson_Barton_Nanopore_1) which is used to deposit scripts and pipelines on GitHub is not accessible. The code availability will represent a valuable addition to the Nanopore RNA sequencing community and can be used a guide for direct RNA methylation analysis.

5) This is a technical paper to assess the performance of Nanopore direct RNA sequencing in a pioneer manner. Since m6A RNA modification detection and full-length RNA transcript sequencing using Cap-dependent capturing constitutes the major contribution of this paper, the recent advances relating to these topics should be included in the Introduction section.

Liu H, et al. Accurate detection of m6A RNA modifications in native RNA sequences. bioRxiv 2019:525741.

Jiang F, et al. Long-read direct RNA sequencing by 5'-Cap capturing reveals the impact of Piwi on the widespread exonization of transposable elements in locusts. RNA Biol 2019:1-10.

Reviewer #2:

In this manuscript, Parker et al. demonstrated several interesting applications of nanopore direct RNA sequencing (DRS) to advance the current understanding of Arabidopsis transcriptome. They have assessed the primary performance factors of DRS that are related to the basecalling error profile, poly(A) length distribution, full-length splicing profile, and the reliability of antisense reads. Also, they have developed two new techniques for DRS to find the 5′-end positions of capped RNAs and the m6A -modified positions in mRNAs. Finally, they applied an error-based m6A -detection method to find the association between the m6A modifications of 3′ UTR and RNA 3′-end processing in Arabidopsis thaliana.

This manuscript lists many different types of RNA processing and modification that can be detected by DRS. This is a nice demonstration of the potential applications and strengths of DRS. But most parts do not connect to each other, and the conceptual novelty is limited. I have some concerns that will need to be addressed before publication.

1) This technique is conceptually similar to the work by Liu et al. (https://www.biorxiv.org/content/10.1101/525741v1). Please clarify the similarities/differences between Liu et al. and the method described in this manuscript.

2) Base-calling error profiles can vary depending on the basecaller version, the model in the basecaller, the processing/filtering parameters used for running the basecaller, the pore protein version, and the motor protein version. Recently, there was a huge upgrade for the basecalling model (high-accuracy model, a.k.a. flip-flop basecaller) introduced in Guppy 3.2. Moreover, according to the Oxford Nanopore Technologies (ONT), a faster motor protein and the new R10 pore will be introduced to their DRS kits very soon. The authors need to clarify and inform the readers that the error profile presented here may change depending on the basecaller software, a model, a pore, and a motor protein.

The method described in this manuscript can work in the specific combinations that the authors used, but it does not guarantee its performance in the other settings. Considering the change in the flagship basecaller, Guppy, with higher accuracy after the version used in the manuscript, the authors need to check if this method works with comparable accuracy with the newer Guppy.

3) In addition, Tombo from the ONT has a mode called "level_sample_compare" that enables the modified base detection by comparing control and experiment groups. Can you discuss a bit about the benefits and drawbacks of your method in comparison with Tombo?

4) Subsection “Nanopore DRS confirms sites of RNA 3′ end formation and estimates poly(A) tail length”: The standard nanopore DRS library preparation uses the double-stranded RNA-DNA ligation assisted by an oligo(dT) splint. It inevitably introduces a substantial underrepresentation of short poly(A) tails. Even 10 nt oligo(dT) splint often results in a strong bias for > 20 nt poly(A) tails against the shorter tails. Moreover, short poly(A) tails often carry additional U tails which interfere with the ligation to the adapter. In addition, the means of the single-read "poly(A) length measurements" may not be a suitable summarization to estimate the means of "poly(A) lengths." Nanopolish gives the best approximations of poly(A) lengths at a single-read level. However, as the poly(A) dwell time roughly follows a gamma distribution with a long tail, the mean of the best approximations at a single-read level systematically overestimates the mean of poly(A) length.

5) Subsection “Cap-dependent 5′ RNA detection by nanopore DRS”: The authors used RNA ligase 1 to mark the 5′ ends of RNAs. Due to the substrate specificity of this enzyme, circularized mRNAs and mRNA-mRNA concatamers might have been produced. Supplementary Table 1 shows that the libraries using the standard protocol yielded ~90% of mappable reads while the libraries with cap-dependent ligation yielded only ~25%. Please describe what the other 75% are. Also, it would be helpful if the sequence information of the 5′ adapter were presented in the manuscript.

6) Subsection “Differential error site analysis reveals the m6A epitranscriptome”: How many of the miCLIP peaks could be detected with nanopore DRS? The authors only show the analyses using the population-level detection of m6A -modified sites. A real benefit of nanopore DRS lies in the associative analyses at a single-read level. Is it possible to use the DRS method to call m6A -modified sites within single molecules and analyze to see if a modified RNA has different polyadenylation status or 3′ end position from those in an unmodified RNA?

I feel that the current discoveries related to m6A modification in this manuscript can be better done using miCLIP than nanopore DRS.

Reviewer #3:

In this manuscript, "Nanopore direct RNA sequencing maps an Arabidopsis N6 methyladenosine epitranscriptome" the authors use Nanopore direct-read RNA sequencing (DRS) to characterize the Arabidopsis transcriptome, including features that can't easily be determined by short read sequencing, such as cap-associated transcription start sites, splicing events, poly(A) site choice and poly(A) tail length. The authors also use this approach to map sites of m6A modification and use a vir-1 mutant strain to validate m6A sites. The identification of modified transcripts allowed the authors to identify a role of m6A in regulating length of circadian period. Overall the paper is well written and is easy to follow.

The authors use cap-dependent ligation to enrich for capped mRNAs, reducing the 3' end bias observed in DRS. It would be of interest to discuss if the transcripts with early 5' ends result from technical artifacts (for example, degradation during RNA preparation) or represent transcripts present in the cell that lack a cap structure that is compatible with the ligation protocol. For example, the authors demonstrate that nanopore DRS can identify rare anti-sense transcripts. Could transcripts with early 5' ends, which are selected against in the cap dependent libraries, represent rare transcripts or degradation intermediary products?

Additionally, the authors leverage DRS to expand the set of annotated transcripts and splicing isoforms. Can the authors use this data to describe new endogenous targets of NMD, poison exons, or find examples of proteins with new functional domains?

One feature of the transcriptome the authors focus on is the localization and effect of m6A modification on RNA metabolism. It would be informative if in addition to the ERCC controls, a set of RNAs with known m6A sites were also included.

One aspect of m6A biology that can't easily be studied with current methodologies is the stoichiometry of the modification at each position in each transcript. Can the authors comment at all on stoichiometry of m6A from DRS? Furthermore, can the authors comment on how many reads per transcript are necessary to detect a modification? Is there a bias towards more abundant transcripts? In mammalian cells it has been shown that modified RNAs tend to have shorter 3' UTRs (Molinie et al., 2016)(PMID: 27376769). Can this observation be tested in DRS, and if so, does the same phenomena occur in Arabidopsis? Information on stoichiometry can be validated for ACA sites with transcript specific assays using the MazF nuclease.

Lastly, can the authors comment on the ability of detecting modifications other than m6A through DRS?
