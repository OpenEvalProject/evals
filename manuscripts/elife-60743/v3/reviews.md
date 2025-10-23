# Peer review - Round 1

Editors:
- Timothy W Nilsen, Case Western Reserve University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.60743.sa1](https://doi.org/10.7554/eLife.60743.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

In this paper the authors use a thermostable reverse transcriptase encoded by a so-called group II intron to sequence RNAs present in blood. This reverse transcriptase differs from retroviral reverse transcriptases in that it can read through structured regions of RNA. Results presented indicate that the population of RNAs in blood is more complex than previously thought.

Decision letter after peer review:

Thank you for submitting your article "Identification of protein-protected mRNA fragments and structured intron RNAs in human plasma by TGIRT-seq peak calling" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Timothy Nilsen as Reviewing Editor and James Manley as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Mariano A Garcia-Blanco (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The reviewers agreed that the work was, in principle, suitable for eLife. Nevertheless, each raised significant concerns that need to be addressed via revision. Specifically, the reviewers felt that the bioinformatic analysis needs to be strengthened. They also requested that you provide some practical application of the work. Please address all of the points raised by the reviewers as thoroughly as possible.

Reviewer #1:

The Lambowitz group has developed thermostable group II intron reverse transcriptases (TGIRTs) that strand switch and also have trans-lesion activity to provide a much wider view of RNA species analyzed by massively parallel RNA sequencing. In this manuscript they use several improvements to their methodology to identify RNA biotypes in human plasma pooled from several healthy individuals. Additionally, they implicate binding by proteins (RBPs) and nuclease-resistant structures to explain a fraction of the RNAs observed in plasma. Generally, I find the study fascinating and argue that the collection of plasma RNAs described is an important tool for those interested in extracellular RNAs. I think the possibility that RNPs are protecting RNA fragments in circulation is exciting and fits with elegant studies of insects and plants where RNAs are protected by this mechanism and are transmitted between species.

I have one major comment for the authors to consider. In my view the use of pooled plasma samples prevented the important opportunity to provide a glimpse on human variation in plasma RNA biotypes. This significantly limits the use of this information to begin addressing RNA biotypes as biomarkers. While I realize that data from multiple individuals represents a significant undertaking and may be beyond the scope of this manuscript, I urge the authors to do two things: (1) downplay the significance of the current study on the development of biomarkers in the current manuscript (e.g., in the Abstract and Discussion – e.g., "The ability of TGIRT-seq to simultaneously profile a wide variety of RNA biotypes in human plasma, including structured RNAs that are intractable to retroviral RTs, may be advantageous for identifying optimal combinations of coding and non-coding RNA biomarkers for human diseases."). (2) Carry out an analysis in multiple individuals – including racially diverse individuals – very important information will come of this – similar to C. Burge's important study in Nature 2008 where it was clear that there is important individual variation in alternative splicing decisions – very likely genetically determined. This second suggestion could be added here or constitute a future manuscript.

Reviewer #2:

Yao et al. used thermostable group II intron reverse transcriptase sequencing (TGIRT-seq) to study apheresis plasma samples. The first interesting discovery is that they had identified a number of mRNA reads with putative binding sites of RNA-binding proteins. A second interesting discovery from this work is the detection of full-length excised intron RNAs.

I have the following comments.

1) One doubt that I have is how representative is apheresis plasma when compared with plasma that one obtains through routine centrifugation of blood. The authors have reported the comparison of apheresis plasma versus a single male plasma in a previous publication. I think that to address this important question, a much-increased number of samples would be necessary.

2) For the important conclusion of the presence of binding sites of RNA-binding proteins in a proportion of apheresis plasma mRNA molecules, the authors need to explore whether there is any systemic difference in terms of mapping quality (i.e. mapping quality scores in alignment results) between RBP binding sites and non-RBP binding sites, so that any artifacts of peaks caused by the alignment issues occurring in RNA-seq analysis could be revealed and solved subsequently. Furthermore, it would be prudent to perform immunoprecipitation experiments to confirm this conclusion in at least a proportion of the mRNA.

3) In Figure 2D, one can observe that there are clearly more RNA reads in TGIRT-seq located in the 1st exon of ACTB, compared with SMART-seq. Is there any explanation? Will this signal be called as a peak (a potential RBP binding site) in the peak calling analysis (MACS2)? Is ACTB supposed to be bound by a certain RBP?

4) For Figure 2A, it would be informative for the comparison of RNA yield and RNA size profile among different protocols if the author also added the results of TGIRT-seq.

5) As shown in Figure 4C (the track of RBP binding sites), it seems quite pervasive in some gene regions. How many RBP binding sites from public eCLIP-seq results are used for overlapping peaks present in TGIRT-seq of plasma RNA? What percentage of plasma RNA reads are fallen within RBP binding sites? Are those peaks present in TGRIT-seq significantly enriched in RBPs binding regions?

6) Since there is a considerable portion of TGIRT-seq reads related to simple repeat, one possible reason is likely the high abundance of endogenous repeat-related RNA species in plasma. Nonetheless, have authors studied whether the ligation steps in TGIRT-seq have any biases (e.g. GC content) when analyzing human reference RNAs and spike ins (Introduction paragraph three)?

7) As described in Figure 2 legend, there are 0.25 million deduplicated reads for TGIRT-seq reads assigned to protein-coding genes transcripts which are far less than 2.18 million reads for SMART-seq. The authors need to discuss whether the current protocol of TGIRT-seq would cause potential dropouts in mRNA analysis, compared with SMART-seq?

8) While scientific thought-provoking, the practical implication of the current work is still unclear. The authors have suggested that their work might have applications for biomarker development. Is it possible to provide one experimental example in the manuscript?

Reviewer #3:

In this work, Yao and colleagues described transcriptome profiling of human plasma from healthy individuals by TGIRT-seq. TGIRT is a thermostable group II intron reverse transcriptase that offers improved fidelity, processivity and strand-displacement activity, as compared to standard retroviral RT, so that it can read through highly structured regions. Similar analysis was performed previously (Qin et al., 2016), but this study incorporated several improvements in library preparation including optimization of template switching condition and modified adapters to reduce primer dimer and introduce UMI. In their analysis, the authors detected a variety of structural RNA biotypes, as well as reads from protein-coding mRNAs, although the latter is in low abundance. Compared to SMART-Seq, TGIRT-seq also achieved more uniform read coverage across gene bodies. One novel aspect of this study is the peak analysis of TGIRT-seq reads, which revealed ~900 peaks over background. The authors found that these peaks frequently overlap with RBP binding sites, while others tend to have stable predicted secondary structures, which explains why these regions are protected from degradation in plasma. Overall, this study provided a robust dataset and expanded picture of RNA biotypes one can detect in human plasma. This is valuable because the findings may have implications in biomarker identification in disease contexts. On the other hand, the manuscript, in the current form, is relatively descriptive, and can be improved with a clearer message of specific knowledge that can be extracted from the data.

Specific points:

1) Several aspects of bioinformatics analysis can be clarified in more detail. For example, it is unclear how sequencing errors in UMI affect their de-duplication procedure. This is important for their peak analysis, so it should be explained clearly. Also, it is not described how exon junction reads (when mapped to the genome) are handled in peak calling, although the authors did perform complementary analysis by mapping reads to the reference transcriptome.

2) Overall, the authors provided convincing data that TGIRT-seq has advantages in detecting a wide range of RNA biotypes, especially structured RNAs, compared to other protocols, but these data are more confirmatory, rather than completely new findings (e.g., compared to Qin et al., 2016).

3) The peak analysis is more novel. The authors observed that 50% of peaks in long RNAs overlap with eCLIP peaks. However, there is no statistical analysis to show whether this overlap is significant or simply due to the pervasive distribution of eCLIP peaks. In fact, it was reported by the original authors that eCLIP peaks cover 20% of the transcriptome. Similarly, the authors found that a high proportion of remaining peaks can fold into stable secondary structures, but this claim is not backed up by statistics either.

4) Ranking of RBPs depends on the total number of RBP binding sites detected by eCLIP, which is determined by CLIP library complexity and sequencing depth. This issue should be at least discussed.

5) Enrichment of RBP binding sites and structured RNA in TGIRT-seq data is certainly consistent with one's expectation. However, the paper can be greatly improved if the authors can make a clearer case what is new that can be learned, as compared to eCLIP data or other related techniques that purify and sequence RNA fragments crosslinked to proteins. What is the additional, independent evidence to show the predicted secondary structures are real?

6) The authors should probably discuss how alignment errors can potentially affect detection of repetitive regions.

7) Many figures are IGV screenshots, which can be difficult to follow. Some of them can probably be summarized to deliver the message better.
