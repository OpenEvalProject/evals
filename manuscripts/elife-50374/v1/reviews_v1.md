# Peer review - Round 1

Editors:
- Tâm Mignot, CNRS-Aix Marseille University France

Reviewers:
- Lotte Sogaard-Andersen, Max Planck Institute for Terrestrial Microbiology Germany

## Review text

DOI: [10.7554/eLife.50374.033](https://doi.org/10.7554/eLife.50374.033)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration and the revised version was accepted for publication. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "Global transcriptome analysis of the Myxococcus xanthus multicellular developmental program" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Lotte Sogaard-Andersen (Reviewer #1); Patrick Eichenberger (Reviewer #2); Roy Welch (Reviewer #3).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work cannot be considered for publication in eLife. All reviewers agree that the dataset is high quality and will constitute a valuable resource for the field. However, in the present manuscript, the current data are largely used to validate previous results in developmental gene regulation and as such, do not reveal "an integrated regulatory network". New analyses could take the manuscript in this direction and ways to perform them are suggested in each of the individual reviews. Given that the modification will likely take more than the two-months period that eLife grants for revisions, we can only offer to reconsider a deeply modified version that would take these comments into account. Please consider that if you decide to re-submit, the manuscript will have to go through another round of reviews before it can be considered for publication.

Reviewer #1:

This manuscript describes a global analysis of gene expression changes during development in Myxococcus xanthus using RNAseq. During development, M. xanthus cells segregate into three cell types. The data presented here contains the combined changes for all three cell types and no attempts were made to distinguish between cell types. Previously, two transcriptome analyses from developmental samples based on microarrays were published (Diodati et al., Nla18, a key regulatory protein required for normal growth and development of Myxococcus xanthus. J Bacteriol. 188, 1733-1743 (2006) and Shi et al., 2008. Given the technological developments in the past decade to map transcriptomes, the data presented here represent a clear qualitative improvement and represent a rich and important novel resource for the community. Moreover, the data are carefully analyzed and provide a number a testable hypotheses for future studies.

Comments:

1) Introduction third paragraph: Maybe briefly mention that Diodati et al. and Shi et al. previously published transcriptome analyzes of developing cells and how your data represent are different.

2) Subsection “Transcriptome analysis of the developmental program by RNA-Seq” paragraph two: I did not find microarray analyzes in the Bath et al., 2014 reference. Please clarify.

3) In the same paragraph: It is appreciated that the authors validate the quality of the RNAseq data using the two lacZ fusions. Later in the text, when expression profiles are discussed for genes that are important for development, it would be helpful to include a reference to those papers and mention if the listed genes were shown to be up- or down-regulated. Also, many more genes than the ones listed are important for development. To further validate the RNAseq data, I was wondering if it would be worthwhile to prepare a list with genes that are known to be important for development, their expression pattern from qRT-PCR or gene fusions and the expression profile reported here.

4) Subsection “Gene expression profiles organize into 10 developmental groups”: The criteria for including genes in the analysis should be more clearly described: It is my understanding that in order for a gene to be included, it needs to have >50 reads at all seven time points. If this is correct, it seems that this would for instance exclude genes that are not expressed at T=0 or strongly downregulated genes. Please clarify.

5) Throughout the data presentations: It is not clear (to this reviewer) what is meant by "relative expression profiles". If the developmental samples are compared to the T=0 samples, then the T=0 induction ratio for the T=0 samples should be 0.00 but it is not. Please clarify precisely what is shown in the expression profiles.

6) Figure 3, 7, 8 and 9: Standard deviations cannot be derived from n<3; please remove SD from the figures.

7) Figure 8AB: The logic underlying the order in which genes are listed in these two figures is not clear. Maybe it would be a good idea to list them according to function, e.g. in 8B L subunits would be listed together and S-subunits would be listed together.

8) Subsection “A large interconnected regulatory network controls development” paragraph three: DmxB is the response regulator-diguanylate cyclase responsible for the increase in c-di-GMP during development and the dmxB gene was previously shown to be upregulated during development (Skotnicka et al., 2016). Is the dmxB gene among the upregulated response regulators?

Reviewer #2:

This is a comprehensive study of the 96-hour program of fruiting body formation in the bacterium Myxococcus xanthus. Gene expression during the development program was investigated by collecting RNA at 7 successive time points and performing RNA-sequencing on two biological replicates. Based on clustering analyses, genes whose expression varied during development were assigned to 10 developmental groups. The composition of each group was discussed in view of 40 years of research on the model organism. This rich dataset will be invaluable to research groups working on Myxococcus and δ-proteobacteria. It might also hold some value to researchers working on other bacteria with well-characterized developmental programs (B. subtilis, Streptomyces, C. crescentus), but comparison to these systems has not been explored in the current version of this paper. In addition, the following points require clarification.

Subsection “Transcriptome analysis of the developmental program by RNA-Seq”: "two independent biological replicates" and "(R2 correlation>0.98), with the exception of 24-h samples (R2 correlation=0.8)". Why only two and not three? Even though the correlation was high for most samples, the fact that there was lower correlation at one time point might have justified the addition of a third replicate. Also, "high replicate variability between the two replicate datasets (R2 correlation <0.7) were removed". A third replicate would help for that category as well.

"After removing the ribosomal sequences (about 98% of the reads)" This seems like a waste of resources. I wonder why the authors did not use a method to pull down rRNA before sequencing? If the authors had done so, they would have saved money for including a third biological replicate.

Second paragraph of subsection “Transcriptome analysis of the developmental program by RNA-Seq”: "two independent biological replicates". The authors should insist on how the use of RNA-seq extends previous knowledge acquired from microarray experiments. The impact of the present paper is lessened if the data reported are just a confirmation of previous work.

Reviewer #3:

The authors perform a global analysis of the Myxococcus xanthus developmental transcriptome, taking timepoints throughout the biofilm's starvation stress response past the self-organization of fruiting bodies and the differentiation of cells into spores (96 hours). They then compare these data to prior studies, both single gene and high throughput, to determine if the changes in RNA levels for different genes at different time points either match previous data or agree with contemporary functional interaction models. Their comparison serves both as data validation and as the primary source of their conclusions. Because the authors choose to largely limit their manuscript in this way, they miss several opportunities to perform a more varied and compelling set of analyses, and ultimately fails to deliver on their impact statement; the work, as presented, does not "reveal a genetic regulatory network"; with significant modification, it might.

Many interesting questions that could be addressed by these data are left unanswered. There is enough new knowledge to merit publication, but it will require additional analysis and substantial reorganization. Because the changes are significant, there is more than one way to make them, but at least three core problems need to be addressed in one way or another.

Problem 1: Analysis of the primary expression data set is not explained in sufficient detail for the reader to understand and reproduce it. Statistics were sometimes provided in the text with incomplete descriptions of analytical methods. For example, what specific methods were used to make the log2FC comparisons? How were criteria established for determining which genes fell into each DG? Were alternative methods tried before settling on these 10 DG clusters, and could alternative methods produce a different number of clusters and/or parsing of genes within them?

Proposed method to address Problem 1: Additional analyses should be performed on the primary data set to address the following questions: Would application of statistical methods, such as multiple range tests, confirm the stability of the 10 DGs, and are the differences in alternative methods statistically relevant? How much of the transcriptome is involved at each time point (i.e. what percentage of the genome is regulated, and how does that percentage change across the time points)? Are there genes that seem to be unique to each time point (i.e. are there any genes that are significantly up- or down-regulated only at one time point and may therefore be particularly important at that specific time point)? Are there other important expression patterns that can be revealed through different statistical methods, such as a functional PCA (i.e. what is the dimensionality of the time-course data)?

Problem 2: The main focus of the middle part of the manuscript (Figures 3-9) seems to be the confirmation of an existing 'consensus' interaction network, and the authors accomplish this by providing a supporting narrative. Although this narrative is interesting, the choice of genes to focus on and the alternative explanations for inconsistent data make this part of the manuscript subjective. Developmental data already exists for the majority of genes in the 'consensus' interaction network (Figure 1B); sometimes these data are from individual gene studies and sometimes they are from high-throughput studies (also, the authors should carefully qualify their claims of novelty and double check some references). This prior work can be used to generate hypotheses that can be tested using the their data set.

Proposed method to address Problem 2: The hypothesis could be something like "given the consensus functional interaction network and data from prior studies, we expect the expression patterns of this set of genes to follow the interaction network in the following way…". The hypothesis must include genes that do not meet the authors' expression cutoffs. Also, crucial conditional statements and plausible alternative explanations like the one stated in the final sentence of subsection “A‐and S‐motility genes exhibit different developmental expression profiles” can't be left to the end of a section, because they effectively negate everything that comes before it. These statements must be addressed throughout the presentation of relevant results and within the context of prior work, rather than as an afterthought.

Problem 3: Comparison of starvation-induced to glycerol-induced sporulation expression is a very interesting idea; an analysis might provide meaningful insight regarding the similarities and differences between these seemingly related events. The authors only begin to perform this analysis.

Proposed method to address Problem 3: The extent and nature of differences in gene expression between starvation-induced and glycerol-induced sporulation must be characterized and quantified. A superficial scan of Figure 2B reveals whole regions of different expression patterns. For example, what are all of the additional repressed genes in DG 9 during glycerol-induced sporulation? Could some of these genes provide insight into the differences between the two kinds of sporulation? Could some of these data be used to address the 'spore versus peripheral rod' alternative hypothesis proposed in subsection “A‐and S‐motility genes exhibit different developmental expression profiles”? Could some of these data be used to support the 'consensus' functional interaction network?

There are more minor issues involving the consistent use of abbreviations and nomenclature, claims of novelty, appropriate references, and the accuracy of concluding statements, but these can wait for the next round of revisions.

Major Points: Text

The text should be divided into three main sections: a comprehensive analysis of the gene expression data generated for this study (see point 1 above), a detailed comparison of these data to a 'consensus' functional interaction network (see point 2 above), and a detailed comparison of these data to the glycerol-induced sporulation time course (see point 3 above). All validation work (i.e. B-gal) should be put in supplementary materials, including figures that parse the expression data to support the narrative.

Major Points: Figures

The figures should be reorganized to better help the reader navigate the manuscript; at present, their structure and sequence do not match the text in a linear sequence. In the following discussion, the current figures are referred to as 'old Figure X' and proposed figures are referred to as 'new Figure X'.

New Figure 1A should be real images of M. xanthus development rather than a cartoon. It should include images that represent each of the time points taken so that the reader can see what development looks like under a microscope.

Old Figure 1B should be moved later in the manuscript because that is when it is discussed in the text.

New Figure 2 should have the cartoon of M. xanthus development running vertically on the left side of the heatmap accurately spaced to represent events, along with representative times. A timeline is also represented horizontally, but the authors use developmental stages and times interchangeably throughout the text, and so it would be helpful to have one diagram that runs along one axis showing clearly which times refer to which DGs and which developmental stages. The times should also match new Figure 1, so that the reader can easily go back and see what each stage actually looks like. Old Figure 2B should be moved later in the manuscript because the comparison to sporulation data is not yet discussed in the text.

New Figure 3 should include at least some set of analyses (see above).

Old Figures 3 through 9 should be moved to supplementary figures.

New Figure 4 should have a diagram showing the interaction of genes like one in Figure 1B. The Results section must be clear regarding which genes have transcription profiles that support the authors' hypotheses and which ones don't, and the figure should also include any genes that didn't make the expression cutoff to be included in the analysis. The interaction network diagram in old Figure 1B is designed to horizontally match to the cartoon showing development in old Figure 1A – this is a good idea for new Figure 4, but the matching should be more obvious, and should include developmental stages and DG groupings as in new Figure 2.

New Figure 5 should be the comparison between starvation induced development/sporulation vs glycerol-induced sporulation transcription profiles. Emphasis should be focused on genes whose expression profiles are similar between the two data sets, and genes whose expression profiles are different. Perhaps some of the genes from new Figure 4 could be identified as involved in development, sporulation, or both. There may also need to be a new Figure 6 providing additional statistical analysis, similar to new Figure 3.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for submitting your article "Transcriptome dynamics of the Myxococcus xanthus multicellular developmental program" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Gisela Storz as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Lotte Sogaard-Andersen (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors have made considerable changes in the latest revision. Most importantly, the statistical analyses involved in the parsing and evaluation of expression data are now described clearly and early in the manuscript. Of course the authors' data are not perfect but, for these kinds of large data sets, variations between experimental replicates must be expected. For example, the relatively weak correlation between replicates of the 24 hour time point does not diminish the overall impact of the manuscript, even though the authors can only speculate about an explanation. The inclusion in supplementary materials of alternate heatmaps for different numbers of Developmental Groups (Figure 2A—figure supplement 1) is also very helpful to a reader who may well use these data for the authors' primary stated purpose – as "important tools and resources for future studies." The comparison between starvation and glycerol induced spores is particularly interesting.
