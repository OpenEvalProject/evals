# Peer review - Round 1

Editors:
- Chris P Ponting, University of Edinburgh United Kingdom

Reviewers:
- Nenad Sestan

## Review text

DOI: [10.7554/eLife.38619.047](https://doi.org/10.7554/eLife.38619.047)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The Transcriptional Logic of Mammalian Neuronal Diversity" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Nenad Sestan (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

The reviewers described the broad survey of gene expression in nearly 200 mouse neuronal subpopulations as being a powerful and useful resource for the neuroscience community. A major strength was the use of transgenic labelled neuronal subpopulations with some anatomical information. Nevertheless, this Editor and some of the reviewers were not convinced by the analysis of "long genes" that gene length is an appropriate explanatory metric of regulatory complexity, particularly given that the density of regulatory elements across mammalian genomes is known to be relatively uniform. We consider the authors' hypothesis not to have been proved. Consequently, either this analysis needs to be removed or replaced or further substantiated. Additionally, we request that the comparison with single cell data is updated, and its presentation revised. Finally, it will be important to report findings using conventional statistical metrics rather than those currently used, unless the authors can justify that these are superior.

The following are the revisions that are required:

1) Currently only gene bodies, and not intergenic sequences, are considered in the analysis. Unless this subjective choice is further justified the authors will need to consider (e.g. for the ATAC-Seq analysis) all intergenic and intragenic regulatory elements. This could be done by considering a gene territory in its vicinity and ATAC-Seq peaks that connect to the gene via HiC peaks, for example. If a regulatory complexity metric is best explained by a gene's full (rather than intragenic) regulatory landscape then the associated speculation in the manuscript needs to be removed. Additionally, reviewers were not convinced: that the frequency of insertion mutations is uniform in the genome, as assumed; that sequence-similar, more cell/tissue-specific, paralogs could modulate this frequency; and, that there are specific population genetic studies that could test the authors' hypothesis.

2) The authors' attempt to reinvent the wheel, statistically, was considered unnecessary. Reporting results using conventional statistics should be sufficient. Attempts to develop novel test statistics should be removed unless with compelling justification. This is easily done since one of the statistics is close to "fraction of comparisons DE" and the other is close to a fold change. The NNLS method is itself not validated and also not essential for the analysis.

3) An important analysis is the comparison with single cell RNA-seq datasets (Figure 2). The problem with the current analysis is that the Ziesel, 2015 and Tasic, 2016 studies are already somewhat out of date, because they are pilot studies to the most recent Tasic et al., 2018 paper in bioRxiv which is already accepted. We understand that the dataset should be available soon, and thus that the timeline should be compatible with this revision. If the data set unexpectedly is not available please do let us know. Another high resolution dataset is from Paul et al., 2017, whose data should also be compared.

4) The use of "cell type" is misleading, even with "operational cell types" defined in the Materials and methods section. Even with known anatomic locations, it is quite likely that the labelled population comprises multiple "atomic types". "Subpopulation" is a more appropriate description and is no less significant. In this discussion, the authors must discuss the extent to which their analysis might be confounded by interregional or interindividual variation.

5) Figures. These could be further streamlined and shuffled to help the reader more. Figure 2 jumps straight into what may seem like an esoteric debate to those not currently diving into or weary of single cell RNA sequencing. A schematic of single cell vs. pooled cell analysis that illustrates shallow and deep RNA capture plus questions of cell purity might help introduce these heatmaps. Also, the Figure 2B panels could be placed in the supplement, and in Figure 2A, it might help to highlight examples of possible low purity cell types to highlight the overall very high purity of the data. Figure 3 – DI and SC will not be intuitive to all readers, even after the schematic in 2A. As a bridge, it might help to label individual genes with high SC and high DI from the scatterplot in B and show the expression of these genes across cell types. Figure 4A dives into this a level deeper by focusing on OFF noise, but Lhx1 and Calb2 could be labeled as examples in 3. Figure 5B: label how many long and short genes were considered.

6) The authors should supplement the use of PANTHER gene families to avoid, to the extent possible, biases in the specific datasets included in this database; it is possible that some gene families, including synaptic and signaling genes or homeobox transcription factors, are over-represented in this dataset. In Figure 4D, the PANTHER gene category "receptor" seems overly broad. What types of receptors? Certainly not all receptor genes are long – olfactory receptors are very short. Also, signaling proteins are on this list but are not discussed in the text along with ion channels and cell adhesion molecules. Why this selective avoidance?

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for sending your article entitled "Mapping the transcriptional diversity of genetically and anatomically defined cell populations in the mouse brain" for peer review at eLife. Your article is being overseen by Chris Ponting, as Reviewing Editor, and Catherine Dulac as the Senior Editor.

Given the issue regarding "long genes" that we describe below, the editors and reviewers invite you to respond within the next two weeks with an action plan and timetable for the completion of additional work. We plan to discuss your response and then issue a binding recommendation.

You have placed considerable emphasis in your two versions of this manuscript on correlations with "long genes". With respect to these aspects (in many places, e.g. subsection “Long genes shape neuronal diversity”, fourth paragraph) it is our view that this argument cannot be retained unless you can satisfactorily refute the results of Raman et al., 2018. These indicate that the length dependencies that you, and others, have seen are likely a PCR artefact.

"Long genes shape neuronal diversity". This returns to our previous issue whether "long gene" expression is correlated with neuronal diversity or whether it causes neuronal diversity. The word "shape" implies causality, yet without evidence: their expression could be a consequence of diverse neuronal cell populations. You also have not shown whether these mRNA expression trends persist with proteins and this will need to be stated explicitly. "rich in transposons and other retroelements". This implies that these introns contain active elements whereas they contain the inactive debris of retrotransposons. The last paragraph of the Discussion is not warranted and should be excluded because it implies (without evidence) that long genes arise because of "exaptations".
