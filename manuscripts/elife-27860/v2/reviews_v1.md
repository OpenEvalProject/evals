# Peer review - Round 1

Editors:
- Nir Ben-Tal, Tel Aviv University Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.27860.082](https://doi.org/10.7554/eLife.27860.082)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Deep transcriptome annotation suggests that small and large proteins encoded in the same genes often cooperate" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Diethard Tautz as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Chen Xie (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper describes an analysis of Eukaryotic genomes to identify alternative open reading frames (altORFs). The paper posits the existence of a large number of altORFs. Evidence that these are indeed protein coding includes there existence as orthologs across several species and the apparent constraint on their evolution between species. The authors also describe how the proteins encoded within the same gene may participate in similar functions.

This interesting and important study should be suitable for publication in eLife after addressing the major issues outlined below. Because this is the first systematical work about altORF, and the altORF list in the paper may play an important role in future research, the results have to be very solid and strict.

Essential revisions:

1) In the generation of the altORF database the authors remove all sequences that share more than 80% identity with the reference proteome. Nevertheless, there are still questions related to the similarity between altORF and reference proteins originating from the same genes. The authors should examine whether there is any association between the% overlap and the functional similarity (in terms of protein domains, localization, function etc.). Even if the overlap is lower than 80%, protein pair may still share multiple features.

2) Previous proteogenomic studies that find novel protein sequences based on genomic data (including point mutations) show lower score distribution of the new sequences, compared to the reference proteome (Menschaert and Fenyo, and related papers). Together with the larger size of the alternative sequences, analyses normally results in high false discovery rate of alternative sequences. The authors should present the score distributions and examine whether such different distribution occurs also in their altORF. Based on these, they may require separating between the FDR filtrations of these databases (as done with genomic data).

3) The overlap between ribo-seq and MS-based proteomics is surprisingly low. The authors explain that limitation of ribo-seq mapping probably underestimates the identified ORFs. It should be explained why the MS data does not cover larger proportions of the Ribo-seq IDs. Deeper analysis of this comparison should determine whether these missing ORFs are expected to be more lowly expressed, or are these specific to the examined systems in each discipline. Importantly, in case that the examined systems are markedly different, the comparison might be meaningless. The authors should try to analyze similar systems to enable meaningful assessment of these approaches.

4) The authors studied the conservation of each human altORF or annotated CDS by checking whether it existed in other species, and found many conserved altORFs. They should consider the possibility that even a neutral ORF may stay intact until a disabling mutation is fixated. A short ORF has much lower probability to be disabled than a long ORF and stays intact for much longer time, and most of altORFs are very short. It will be better if the authors use a statistical model to estimate the disabling probability of an ORF with a specific length in a specific time. Then they may estimate how many altORFs are really under functional constraint.

5) The authors used PhyloP values representing 100 vertebrates basewise conservation of the third positions of altORF overlapping and non-overlapping regions in annotated CDS to study the selection pattern of altORF CDS, but they should only use altORF-annotated CDS pairs conserved in vertebrates instead of all of them. In addition, they can also compare the PhyloP values of the first and second positions with the third positions of altORF5', altORF3', and altORFnc conserved in vertebrates to investigate their selection pattern.

6) In their analyses of ribosome profiling data, the authors believed that a TIS with 10 or 5 reads is active. It may be an artifact because there are always reads in the 5' UTR of mRNA even there is no upstream ORF; and reads supporting the TIS of an altORFCDS may be just due to the translation of annotated CDS. That may explain why much more altORF5' and altORFCDS are supported than altORF3' and altORFnc. A more strict way is to check the periodicity of the reads, and there are already tools, such as RiboTaper or RibORF. The authors should use at least one of the tools to analyze and check whether they get the same pattern. In addition, the authors should also analyze the altORFs supported by proteomics data in the same way as Figure 5A.

7) In their analyses of proteomics data, is it possible that the peptides of altORFs may also come from the microbe in human samples, such as parasites or infectious microbe? For example, randomly picking up a peptide "MKHIPSR" (supplementary file 2, table "RAW MS OUTPUT", row 9), and running NCBI BLASTP against the nr database, found four perfect matches, including one from a protein in Pseudomonas, which is an infectious bacteria. This phenomena may be highly likely for short peptides. Unless this scenario is highly improbable, the authors could filter out the peptides, which can also be from the microbe in human in order to make the evidence more reliable.

8) Subsection "Evidence of functional coupling between reference and alternative proteins coded by the same genes", the authors claimed that "If there is functional cooperation or shared function, one would expect orthologous alternative-reference protein pairs to be co-conserved". However, functional cooperated proteins are not necessarily co-conserved. For example, a newly originated altORF can also interact with its annotated CDS; many co-conserved proteins do not interact with each other, e.g., there are tens of thousands of proteins co-conserved in human and chimpanzee and most of them do not cooperate. The co-conservation analysis may be informative for multiple gene birth and death events in a large phylogenic tree of dozens or hundreds of species, but not in this case.

9) Paragraph two of the same subsection, the authors claimed "Another mechanism that could functionally associate alternative and reference proteins from the same transcripts would be that they share protein domains". Proteins that share similar domains do not necessarily cooperate, and in contrast many proteins that do not share similar domains do interact nevertheless. The results about the zinc finger proteins and the two altORFs that are experimentally studied are interesting. However, it is better to remove the part about relation between co-conservation / domain sharing and functional cooperation.

10) Discussion first paragraph, the authors claimed that "underrepresentation of altORFs in repeat sequences" supported the functional role of altORFs. However, their altORFs were predicted from the transcriptional annotation that was probably underrepresented in repeat regions, and this observation may be simply caused by the biased locations of transcripts. They should also perform the same analysis of repeat regions with annotated CDS, and compare the results with those of altORFs. Combining this with the above two points, the statement of three lines of evidence: (6), (7), (8) should be removed.

11) Finally, the data at "https://roucoulab.com/p/downloads" only include simple information of altORFs. Considering that this altORF list may be important for further studies, as much information as possible should be provided in order to let others follow the work easier. We encourage the authors to include freely accessible and well-organized tables containing information about the 183,191 human altORFs and 51,818 annotated CDSs at their website. For each ORF/CDS, the authors should provide: ORF accession, ORF type (5', CDS, 3', nc), chromosome, start position, end position, sequence, transcript accession, conservation (chimpanzee, mouse,.[...], yeast), ribosome profiling evidence (each data set separately), proteomics evidence (each data set separately), predicted functional signatures. Perhaps more data? It should not require too much effort since the data are already stored in MySQL database.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Deep transcriptome annotation suggests that small and large proteins encoded in the same genes often cooperate" for further consideration at eLife. Your revised article has been favorably evaluated by Diethard Tautz (Senior editor), a Reviewing editor, and three reviewers.

Overall, the authors dealt very well with the points that have been raised about the original manuscript. The few that remain (detailed below) can be addressed without a second round of external review.

Reviewer #2:

Overall the authors properly addressed all my comments and edited the manuscript accordingly. In some cases they decided not to include the analyses in the revised manuscript.

Comment #1: Regarding the protein sequence overlap and association with function, I suggest to add a short description of the Results section (1-2 sentences) and the figure in the supplementary material.

Comment #2: The authors properly addressed the issue and edited the manuscript accordingly.

Comment #3: I think the authors did not fully understand the question. I referred to predicted proteins based on ribo-seq which are not identified by proteomics (and not vice versa). I accept their claim that this is not a major aim in the paper, but it could be still interesting to discuss the underlying causes for discrepancies. Nevertheless, I don't think it is absolutely required for the paper.

Minor comment #8: Since the quantitative aspect of the result is indeed not critical here, I accept their compromise which results from the availability of appropriate analytical software.

Altogether, in terms of the proteomic aspects, I find the manuscript improved compared to the previous version (mainly due to the FDR correction), and the rest has been addressed in the authors' reply.

Reviewer #3:

The authors addressed most of the comments well, besides they showed important results, including a large number of altORFs existing in the genome, and many of them probably encoding functional proteins due to that they were under functional constraint, or were expressed, or had functional domains, therefore, I think this paper could be accepted if the authors solve all remaining comments as follows well.

As I mentioned in essential revision point 8 and 9, which the authors also agreed, co-conservation or domain sharing does not mean functional interaction/cooperation. The co-conservation or domain sharing evidence in this paper was very weak and did not support the conclusion, functional cooperation. In the other way, even the few cases mentioned in the paper, which altORFs and annotated ORFs did functionally interact with each other do not show co-conservation or domain sharing. Simply changing "functional cooperation" to "functional relationship" makes no difference. The relevant parts in the manuscript should be removed, and the Title and Abstract should also be edited accordingly. Actually, the rest of the work is already very significant and solid.
