# Peer review - Round 1

Editors:
- Christina L Stallings, Washington University School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.61885.sa1](https://doi.org/10.7554/eLife.61885.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This manuscript provides a global view of transcription factor interactions in Pseudomonasaeruginosa and represents an important resource for the research community. With the use of novel assays, the work has uncovered transcription factor binding specificities for nearly half of the annotated transcription factors and forms a good foundation for future studies. The study will be of interest to microbiologists and those interested in bacterial metabolism.

Decision letter after peer review:

Thank you for submitting your article "The Binding Specificity Atlas of Pseudomonasaeruginosa Transcription Factors Reveals Novel Regulators in Virulence" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Bavesh Kana as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Yu Zhang (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

This manuscript analyzes the DNA binding sequence specificity of transcription factors (TFs) in the human pathogen Pseudomonasaeruginosa using a high-throughput DNA enrichment method. The consensus binding motifs of 182 (out of 371 in total) TFs were obtained and genomic loci were predicted to be targets of these TFs, some of which were experimentally validated. The work provides a useful resource for studying the transcription regulation network in Pseudomonasaeruginosa, and also provides DNA motif information for TFs in other bacteria. The reviewers all agree the work performed is generally of good quality, however, specific concerns raised by the reviewers regarding how the data are obtained, classified, and validated, need to be addressed.

Essential revisions:

1. One of the major conclusions is that most TFs bind as homodimers because their PWMs contain 'head-to-head' duplications of the same sequence. However, it could also be that two monomers bind a single double stranded DNA molecule in the HT-SELEX assays. It would be helpful if the authors could investigate whether homodimeric protein-protein interactions are known to occur for relevant TFs, or whether homodimers have been observed in structural studies.

2. The comparison of their HT-SELEX-derived PWMs with those obtained by ChIP should be expanded. After predicting binding events based on their PWM data, precision/recall analysis should be done with the ChIP data that compares individual binding events rather than the overall composite PWM binding motif. This will address the question of how many predicted binding events were also reported by ChIP and how many binding events detected by ChIP were also predicted. This is a key point.

3. The computational scanning for TF binding sites in the Pseudomonas genome is not sufficiently described: how was thresholding determined to call binding sites for each TF?

4. How a TF is associated with a biological pathway is not well described. How many binding events are required to call an association? Is this done one TF at a time, or one pathway at a time? How is a pathway defined?

5. The biological validation experiments appear ad hoc. It is not clear what this says about the entire dataset. For instance, only one new TF was validated experimentally out of 57 biofilm-associated TFs. The crystal violet assay can be easily performed in a 96-well plate format to validate 57 TFs that affect biofilm formation. PAO1 mutants can be obtained from Manoil lab (PAO1 transposon insertion library (https://www.gs.washington.edu/labs/manoil/libraryindex.htm)

6. It should be noted that the gel shift assays are similar to SELEX.

7. How many (predicted) binding events are functional? Analysis of (available) RNA-seq data would be key for this. For instance, Figure 1B. shows that the well-studied GacA and AmrZ have similar DNA binding specificity. Transcriptomic data are available for both these TFs (PMID: 31270321) and should be compared to the physical binding predictions.

8. Page 11. Lines 266-268, also Figure 5A. The authors state that ShpR shares six targets with PA4008 implying a cooperative (or redundant?) function in regulating T6SS. From the figure 5A, these 6 targets are: tagJ1, tssE1, tssF1, tssG1, clpV1, vgrG1. However these six genes are in the same operon and share a single promoter (https://Pseudomonas.com/feature/show/?id=102905&view=operons). The figure and the text imply that there are 6 independent TF binding sites located in 6 different promoters. However, there is a single promoter, and ShpR and PA4008 share only one target. Operon genes that share a single promoter are represented in the figures as independent genes. This is a major problem throughout the paper and figures and needs to be resolved.

9. Page 12. This paragraph is speculative as no functional motility assays were performed and no target genes were functionally validated. Thus the statement "in sum, 37 TFs were found involved (..) in regulating motility-related genes" is an overstatement.

10. Throughout the manuscript, the authors should be careful not to overstate their findings and be precise when biological function is predicted vs demonstrated experimentally.

11. The manuscript would benefit from thorough proofreading and editing.

12. Overall, 371 TFs entered in the pipeline and a result could be generated for 182 TFs (app. 50%). From an experimental design point of view, only 3 TFs have been used to benchmark the reproducibility of the binding site motifs which represents <1% of the input. This should be improved to provide a resource for the field. Since it is an in vitro assay, I would have expected to see the results validated systematically in duplicate. The author claim that the three replicates obtained "virtually identical binding specificity": but what does this mean statistically?

13. How did the authors select 182 TFs out of 371 TFs? Were there issues with protein purification for the others?

14. Line 167/Figure 2E: using the binding motifs, the authors predicted the involvement of 365 TFs in Pseudomonas virulence pathways. How is it possible to predict the role of 365 TFs while they obtained PWM for only 182 TFs?

15. Figure 3B/C: AmrZ binding site: it is not clear for the link between Figure 3B and 3C. Where is the motif in the psl operon?

16. The authors have already published a TF regulatory network paper (https://doi.org/10.1038/s41467-019-10778-w) covering 20 TFs : a supplementary figure that compares side-by-side the motifs found in the both papers could be interesting.

17. The author should explain why 201 sequence motifs (PWMs) were obtained for 182 TFs in the main text. For example, in the Data S1, the Module 37 of PA1241 has two sequence motifs containing almost the same consensus sequence. Why have two consensus sequence motifs have to be assigned?

18. The sequence motif for sig54 (rpoN) is conserved across bacteria and the core consensus sequence of GGN(10)GC has been confirmed in various studies. The sequence motif for sig54 by SELEX (Figure 1C) is inconsistent with previous literatures and should be reanalyzed and discussed.

19. The manuscript also describes interesting monomeric sequence motifs for 19 TFs. The discussion of these 19 TFs should be expanded.

20. The location of TF-binding sites relative to transcription start site (TSS) on the promoter DNA could help predict the activity of the corresponding TFs. For example, TF binding sites overlapping with the core promoter region (-35 to +1) and the proximal downstream region of a TSS may suggest transcriptional repression. As TSS profiles in Pseudomonasaeruginosa are published, it would strengthen the report to integrate the TSS information into the analysis herein.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "The Binding Specificity Atlas of Pseudomonasaeruginosa Transcription Factors Reveals Novel Regulators in Virulence" for further consideration by eLife. Your revised article has been evaluated by Bavesh Kana (Senior Editor) and a Reviewing Editor.

Summary:

This manuscript provides a global view of transcription factor interactions in Pseudomonasaeruginosa and represents an important resource for the research community. With the use of novel assays, the work has uncovered transcription factor binding specificities for nearly half of the annotated transcription factors and forms a good foundation for future studies. The study will be of interest to microbiologists and those interested in bacterial metabolism.

Although the manuscript has been improved, there are some remaining issues that need to be addressed, as outlined below:

1. There are still concerns about the interpretations of RpoN binding data. It is well established that RpoN doesn't function as a dimer to facilitate transcription initiation. It binds RNAP core enzyme in a 1:1 molar ratio to form an RNAP holoenzyme. Second, the sequence motif itself is not a direct repeat of two half-sites. The 5' 'GG' and 3' 'GC' consensuses of the GGN(10)GC motif are representative sequences of the '-24' and '-12' elements of a typical sigma 54 (encoded by rpoN)-initiated promoter. The two elements are recognized by two separate domains of RpoN, both in the presence and absence of RNAP holoenzyme. This issue of data interpretation and representation needs to be addressed. It is also recommended that the authors use a different example of head to tail binding.

2. The authors associate a TF with a pathway when a single predicted binding event occurs with any gene in that pathway. However, statistical analysis must be performed to determine the false discovery rate and whether their findings could occur via chance.

3. There are still points that the authors equate binding with function in the manuscript, please revise throughout to not make this overstatement.
