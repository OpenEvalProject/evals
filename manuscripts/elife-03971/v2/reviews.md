# Peer review - Round 1

Editors:
- Nahum Sonenberg, McGill University , Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.03971.020](https://doi.org/10.7554/eLife.03971.020)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “mRNAs with efficiently translated uORFs resist stress-induced translation suppression inflicted by eIF2 phosphorylation” for consideration at eLife. Your article has been favorably evaluated by James Manley (Senior editor) and three reviewers, one of whom is a member of our Board of Reviewing Editors.

The Reviewing editor and the other reviewers discussed their comments before we reached this decision, and the Reviewing editor has assembled the following comments to help you prepare a revised submission.

In this study, you identify mRNAs that continue to be translated in the presence of sodium arsenite. Ribosome profiling of HEK293T under normal and stress conditions, identified a small number of mRNA whose translation is resistant to eIF2-alpha phosphorylation. Interestingly, the majority of these mRNAs contain uORFs that are efficiently translated under normal conditions. Experiments done with wild type and mutant mRNA reporters demonstrated the importance of uORF for translational resistance.

The reviewers thought that in general the work is interesting. It incorporates an important technology to assess translational control genome wide. The genome-wide analysis is the most important contribution of the manuscript and there are several new genes identified whose translational regulation could be important for cellular adaptation to arsenite stress. Also, besides identifying several new stress-resistant mRNAs, you describe a specific characteristic that is associated with these mRNAs, an efficiently translated uORF.

Two of the reviewers noted that a mechanistic explanation of how uORFs provide translational resistance to stress is lacking, however.

In addition, the work does not break new ground in our understanding of translational control during stress and eIF2 phosphorylation. No new mechanisms of translational control were described, but rather the study provides a broader picture supporting the idea that certain uORFs are central to mechanisms facilitating translation during stress.

Because the results are novel and important we are prepared to consider a revised version that will address some important questions raised by the reviewers as follows:

1) Given the small number of eIF2-alpha phosphorylation resistant transcripts, it is important to validate them by RT-qPCR/polysome profiling. In addition, it is rather surprising that the list of stress-resistant mRNAs does not include mRNAs that were reported to possess IRESs. This should be discussed.

2) The manuscript should be more precise in explaining the calculation that was used to classify gene transcripts that are resistant to arsenite stress. Classification of resistant mRNAs could be based on either the change in RNAseq reads or the Z score. This clarification is important because mRNAs that have a positive Z score may still experience a reduction in translation during arsenite treatment, in which case the Z score may not be an the best measure of mRNA resistance. Explain and justify which calculation was used to classify mRNAs as being resistant and provide a full description of what delineates translation resistance from repression during arsenite stress.

3) The manuscript should delineate preferential translation from translation resistance (sometimes called tolerance). In preferential translation there is poor mRNA translation during non-stressed conditions and high levels of translation in response to stress and eIF2 phosphorylation. The literature indicates that ATF4 is an example of preferential translation in response to eIF2 phosphorylation as supported by Figure 1A. Curiously in this manuscript, arsenite stress did not induce the expression of the luciferase reporter with the 5'-leader of the ATF4 transcript (Figure 4A) and there was perhaps only a modest enhancement of ribosome occupancy in the mRNA CDS during arsenite stress as judged by ribosome profiling. Perhaps arsenite differs from other stress conditions that were reported to induce preferential translation of ATF4 mRNA (e.g. pharmacological inducers of ER stress).

4) SLC35A4 appears to be the only gene that showed strong enhanced translation in response to arsenite translation (i.e. preferential translation). Does the 5'-leader of the SLC35A4 gene transcript confer enhanced expression in a reporter assay during arsenite stress?

5) Do the uORFs in the resistant gene transcripts display any differences from those whose translation was repressed during arsenite stress?

6) The manuscript refers to eIF2 phosphorylation and translational control, as highlighted in the title, but there were no experiments establishing cause/effect between eIF2 phosphorylation and the translation expression of a gene. Rather, it was only inferred based on translational control mechanisms previously described in the literature for ATF4 and the related ISR genes.

7) Could you include analysis of mRNAs either for the context around the AUG in the uORF or whether non-AUG codons might be used (if in a good context)? This would require additional data mining but no additional experiments. This might also allow for an explanation of the 11 AUGs in the SLC35A4 mRNA that do not seem to serve as initiation codons.

8) A major concern is the sampling time. From Figure 1A it appears that the hyper-phosphorylation of 4E–BP1 disappears at 1 hour (although the gel is not of high enough quality to tell; there is the possibility of smiling of the gel bands). The GAPDH loading control is overexposed and, therefore, inadequate. The phosphorylation of eIF2alpha is up at 0.5 hours but maximal at 2 hours. The concern is the possible crossover of 4E–BP1 activation (loss of phosphorylation) and the onset of eIF2alpha phosphorylation. The authors should more rigorously exclude indirect targeting of mTORC1–4EBP and mTORC1–S6K pathways of protein synthesis regulation by arsenite treatment. The 4EBP1 blot on Figure 1A should be less exposed to make the bands more discernible. The blots showing no change in p-4EBP1 and p-S6K levels under their conditions of arsenite treatment should also be shown. Do the authors have an independent control for determining the level of cap-dependent translation vs. the level of eIF2-dependent translation?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled “Translation of leaders is pervasive in genes resistant to eIF2 repression” for further consideration at eLife. Your revised article has been evaluated by James Manley (Senior editor), a member of the Board of Reviewing Editors, and two reviewers. The manuscript has been improved but there are some significant remaining issues that need to be addressed before proceeding, as outlined below.

There are two remaining major concerns:

The first concern was the bioinformatics and reluctance to incorporate fold-change into the core statistics of the manuscript. This is a shortcoming and confuses interpretation of the identification of genes whose translation is induced upon arsenite stress. This is the potential novelty of the manuscript.

The other major concern was the experimental validation of the ribosome profiling. The reporter assays do not fully support the profiling data, and the controls, e.g. ATF4, did not follow the expected induced translation with increased eIF2 phosphorylation. In the rebuttal letter (the Methods of the manuscript were not detailed on this point), the reporter mRNA was stated to be transfected in cultured cells for 1 hour prior to arsenite treatment for an additional 2 hours (the Methods section stated the later treatment time). There is a concern that the non-stressed cells are not truly non-stressed as there is likely to be insufficient recovery from the transfection using lipofectamin 2000. This could explain why there were virtually no genes that were preferentially translated in the reporter assay, just different degrees of repression. The non-stressed conditions were not without the underlying membrane stress of the transfection agent. Also 40 micromolar is a large amount of arsenite to stress the cells.

Below is the description of the concerns in more detail:

The first is centered on reviewer concern number 3 that indicated that there should be clear delineation between the levels of translational control, e.g. preferential translation and translation resistance (or tolerance). In the first paragraph of the response to reviewer concern 3 the authors provide a definition of preferential translation as an increase of translation with a high Z-score and a fold-change >1 and tolerant with a high Z-score and fold change as <1. This was a straightforward conceptual framework involving Z-score and fold-change that should be incorporated into the manuscript analysis and ranking.

The second concern is how the results from ribosomal profiling analysis compare to other approaches previously used in the literature. This is the heart of the manuscript. In Reviewer concern 1, the response stated that qPCR and polysome analysis would not be appropriate for this analysis despite its utility in the literature. As a consequence, the manuscript elected to rely on reporter assays involving transfections of mRNAs featuring 5'-leaders of targeted gene transcripts upstream of the firefly luciferase coding sequence. ATF4, a well-characterized preferentially translated gene transcript was used as a positive control, and the artificial gene transcript pGL3 was an example of a gene that is repressed by eIF2 phosphorylation and stress. Curiously, ATF4 translation was not preferentially translated, but displayed a partial resistance to arsenite stress. The authors’ argument for why ATF4 ribosome profiling data and reporter data are in agreement (even though the ATF4 reporter is not induced) is based on “technical limits of methods accuracy”. The details of the reporter assay were not fully clear in the original or present manuscript, but the response letter provided additional details in the response to reviewer concern number 3. The mRNAs were transfected into HEK293T cells and 1 hour after transfection the cells were treated with arsenite for 2 hours prior to harvesting and analysis. There are some concerns about the timing in this protocol, such as would 1 hour be sufficient time for the resolution of the membrane stress triggered by the transfection protocol? Furthermore, it is suggested that even though the SLC35A4 reporter was not inducible during arsenite stress, that this is not in disagreement with the ribosome profiling dataset because SLC35A4 mRNA levels are low in the profiling dataset. As the purpose of using the Z-score was to eliminate variability and error in the assessment of the ribosome profiling dataset, is this sufficient justification for why the two assay results do not appear to be consistent? In a related point in concern number 6, it was suggested that the manuscript should focus on “establishing cause/effect between eIF2 phosphorylation and translation expression of a gene.” This could be directly addressed in the reporter assay, and the explanation involving an alternative stress (DTT) and mTOR did not appear to adequately address this basic concern.

Other comments:

1) The English is still a bit rough, but not to the point where the reader cannot understand what is intended.

2) Although in the position of being a “break out” paper, it would be nice if there was some effort expended at a possible explanation although it would be obviously speculative (see below). To just leave the paper to end on “there a black box that allows for this resistance to eIF2 repression” is unsatisfying (although accurate).

3) The authors stress the resistance to eIF2 repression, but do not stress as well that most of the proteins are poorly expressed. Using the number of reads scale in Figure 2 where ATF4 is 43, the other proteins fall mostly into the 0 to 2-8 range. This inefficiency is also reflected in the reporter assays in Figure 4 where pGL3 is 100%, the remaining normal configuration for most constructs yields expression levels in the 5 to 10% of pGL3 range.

4) That said, the low level of expression may be entirely appropriate for phosphatases, kinases, transcription factors, etc. that are not required in large amounts.
