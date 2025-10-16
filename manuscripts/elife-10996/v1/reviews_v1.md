# Peer review - Round 1

Editors:
- Duncan T Odom, University of Cambridge / Cancer Research UK , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.10996.017](https://doi.org/10.7554/eLife.10996.017)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "No evidence of widespread dosage compensation in wild S. cerevisiae strains" for consideration by eLife. Your article has been reviewed by four peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Randy Schekman as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

Summary:

All the reviewers, as well as the Reviewing Editor, were entirely convinced that a revised and carefully re-written version of your manuscript should be publicly released in eLife. Major concerns centered around the overall tone being too aggressive, many analyses possibly being too stringent, and an unbalanced consideration of all possible explanations, particularly given how nascent our understanding as a field is of dosage compensation. It was also discussed that the authors need to describe the methods used in a more detailed manner.

All four reviewers brought up a highly compelling set of additional analysis and interpretation concerns to be addressed, and are therefore appended to this letter. A revision suitable for acceptance will not require any additional experimental data; however, to publish will require new analyses, corrected figures, a balanced Discussion, and substantial reworking of the text and argument structure.

Essential revisions:

1) Methods: Every analysis should be described in a detailed Methods section, with subsections clearly annotated and referenced in the main text by occurrence in the figures and in the Results section.

2) Soften tone: As one reviewer eloquently said: "The tone throughout the article is rather strident and bordering on confrontational. It would be wise for the sake of rational open discussion to soften some of the more forceful statements." The overly confident or aggressive text must be adjusted before acceptance. In some sections of the manuscript, the authors’ interpretations were simplified or inappropriate, and exceptionally strict analysis cut offs may bias Torres' interpretations. Additional tonal comments found in the reviews below should not be neglected. Importantly, the title and section headers will have to be toned down as well.

3) Restructure: A careful introduction to what is meant by 'dosage compensation' must be laid out clearly in the Introduction. Sections should start with a paragraph laying out the reasoning that leads to why each analysis was performed (see for instance Reviewer 3 point 5). See also the Reviewing Editor’s comments below.

4) Aneuploidy versus instability: Many reviewers noted that Torres' equating aneuploidy and instability was not appropriate; this must be corrected throughout.

Reviewer #1:

The Torres et al. manuscript re-examines the Hose et al. (eLife 2015) data to evaluate dosage compensation in wild yeast strains. At the heart of the Torres manuscript is whether the data of Hose et al. truly support dosage compensation. Their analysis is thorough, careful, and convincing, but the methods need to be better described.

1) They argue that the presence of non-integer DNA copy number states implies the strains are highly heterogeneous and unstable. But this is methodologically poorly described. The methods argue that chromosome copy number is calculated by taking the average number of all genes within each chromosome. So one assumes that non-integer is an average substantially different from an integer, but what variance is acceptable? The copy number plots (Figures 1, 2, 4) show considerable variability from point to point, depending on strain; for example Figure 1 NCYC110 is tightly distributed around 2 DNA copies whereas YPS1009 seems more variable. Is this variability taken into account? Is it influenced by depth? Means are more sensitive to outliers than the median – would you see a similar result using the median, or (in the case of numerous aneuploid chromosomes) is the median too skewed upward?

Furthermore, it is unclear that they can infer instability rather than simply heterogeneity, the exception being the one obvious case (K1) where the DNA and RNA copy numbers vary. That said, a devil's advocate argument is that K1 shows differences between DNA and RNA assays (specifically on chromosome VI) because of "dosage compensation". While highly unlikely (seeing how there are other aneuploid chromosomes that are not compensated), it seems an important point given the final overall findings of the paper.

2) The methodologies for assessing false positives are poorly described. Both the randomization and the error/noise distribution approach are only vaguely described. When the ratios were permuted relative to the gene list, what was then done to assess dosage compensation – they say "the method of Hose et al. (see Methods)” but in the Methods it is not described. (The false discovery rate analysis is described but that is used later in the paper). What does "not reported independently" (in this same section) mean? How does using the "lowest average chromosome-wide DNA error" bias your result? How exactly were errors combined?

3) The heart of the paper is the issue of how to assess dosage compensation. They miss an opportunity in the Discussion to discuss both the key points of "dosage compensation" as a concept (distinct from what they refer to as "transcriptional response to aneuploidy”). Likewise there are issues when assessing aneuploidy numbers – the constant need for a frame of reference and this issue of expectation (i.e. RNA copy numbers will vary relative to DNA simply because of expression levels being variable). This would help the reader to understand why skew is expected in the distribution if dosage compensation is present.

Reviewer #2:

Amon and coworkers re-analyze data previously obtained by Hose et al. (2015). This re-evaluation identifies several flaws in the original analysis and yields a completely opposite conclusion; namely that there is no sign of widespread dosage compensation in (aneuploid/polyploid) feral S. cerevisiae strains. As far as I can see, the re-analysis is technically sound and I especially commend the authors for the permutation test applied to the RNA/DNA ratio for each gene.

I therefore recommend publication of this paper in eLife, even though I do have a few suggestions (below).

1) Most importantly, I would suggest giving A. Gash and her team the opportunity to co-publish their response to this new paper together with the publication of the new paper. I think it would be interesting to know what the original authors think about this re-evaluation, and it also seems courteous to offer this possibility to Dr. Gash. I also feel that it is important to give the opportunity to have the response published together (at the same time) with this new paper.

2) It would be interesting to expand the short Discussion section to further highlight that non-laboratory S. cerevisiae strains harbour natural copy number variants. The sentence "The fact that strains YJM428, Y2189, K1, UC5, Y3, Y6 and CBS7960 are unstable also means that these strains are less fit than euploid strains" might benefit from a more elaborate discussion to help the reader understand the rationale behind this argument, and to discuss literature showing that several experimental evolution experiments have identified transient aneuploidies as a common but potentially suboptimal solution to overcome harsh conditions.

3) The authors use non-integer changes in DNA read depth as evidence that a given strain is unstable. I see the logic behind this reasoning, but since this result directly contradicts previously published results, and since it is of great importance to the broad community working with (industrial and feral) S. cerevisiae yeasts, one has to be sure that there are no (cryptic) technical reasons for the non-integer changes, even if this scenario appears unlikely. If the strains are indeed so unstable, one would expect that analyses (whole-genome-sequencing) of different single colonies yield (very) different outcomes. Is this the case? Another, more elegant approach would be to investigate CNVs in single cells in a population, but this might be technically more challenging…

Reviewer #3:

This manuscript is a report that is a rebuttal directed at a prior eLife paper by Gasch and her group (Hose et al, 2015). The paper by Gasch reports dosage compensation at the transcriptional level in aneuploid wild yeast. The main focus of the reviewed manuscript is to demonstrate that the observed dosage compensation reflects shortcomings of the analysis. Science should foster open disputation of controversial topics. As the field of aneuploidy is rather new and evolving, it is essential to address the disagreements early on and thoroughly. Torres et al. specifically mention the following issues: the used strains may be unstable, the normalization is suboptimal there is no test for significance of the number of dosage compensated genes and its correction for multiple testing the standard deviation of the DNA sequencing data is used as a cut off for determining dosage compensated genes on RNA sequencing data and the three-point analysis to identify dosage compensated genes is too limited and therefore prone to noise-related errors. Since the analysis by Hose et al. has some flaws, this referee feels that the manuscript by Torres et al. should be made public. However, there are several important points that should be addressed.

1) First, the authors make the point that the wild aneuploid yeast might be chromosomally unstable. Although this is probably true, it is not possible to conclude based on the presented data – the authors say as an example that the RNA and DNA levels are very different for K1 strain in figure 1A in Hose et al.; however, this reviewer can see only DNA levels in 1A. The fact that there are non-integer DNA copy numbers means strictly speaking only that the strain is heterogeneous.

2) In the second paragraph of "Evaluation of the analysis methods employed by Hose et al.", the authors state: "Most normalization protocols do not take into account that aneuploid strains harbor a different total number of genes than euploid strains". This statement by Torres et al. is incorrect. If something, they contain more copies of genes. Also, Torres et al. mention that the data has to be manually corrected, however, there is no description how they envision to do this nor is it obvious whether they performed it on the data from Hose et al. or not. Here, a description should be added at least in the Methods description. Next, Torres et al. state that "the data used for analysis by Hose et al. (2015) deviate from the actual expression values..."; here the "actual expression values" should be those that Torres et al. calculated. In fact, there is no way to know the "actual expression values"; the approach is to just try to normalize the data and hope that it reflects the reality.

3) To straighten their point, the authors should show at least one volcano plot of the 838 compensated genes (identified by Hose et al.) and their calculated FDRs.

4) It would be useful for the reader if the authors would add the 2SD RNA and 2SD DNA to Table 1 for comparison of the variance and further substantiate the incorrect use of the 2SD DNA as a cutoff in Hose et al.

5) For the understanding of the discussed issues it might be useful to restructure the manuscript in a way that each of the three paragraphs showing that there is no dosage compensation includes the corresponding critical points of the analysis by Hose et al. For each of the three subchapters first the criticism should be raised, followed by their re-analysis and their own analysis. It feels much more logical to explain first the criticism and then show the new results than to list first everything that is wrong and only then show the reasons.

Reviewer #4:

This manuscript is a very thorough reanalysis of a recent paper on aneuploidy and wild strains recently published in eLife (Hose et al.). This paper reaches quite different conclusions than Hose et al. and instead shows a lack of evidence for what Hose et al. call dosage compensation. I found the Torres et al. analysis pretty compelling, and I was rather surprised that the original paper did not include similar analyses. Some of the identified mistakes include errors in normalization, apparent copy number variants in the strains used as euploid controls, and discrepancies between RNA and DNA for some strains. Overall I was convinced that there are significant issues with the Hose paper that were masked by the data presentation and analysis methods used.

I was particularly convinced by the demonstration that the distribution of gene expression of genes on euploid and amplified chromosomes was identical. One could argue whether the distributions of DNA and RNA should be compared (even given the vastly different dynamic ranges), or whether the exact cutoffs employed are too stringent or not stringent enough, but any model of "dosage compensation" seems like it should have genes behaving differently when they are at elevated dosage. This does not appear to be the case.

That said, I did find some of the reanalysis a little too demanding: buffering could still be present but below the 2 SD thresholds used throughout. That's one difficulty of working with single increment dosage effects, particularly in diploids: the fold changes expected are far less than the cutoffs generally employed for expression analysis. While in bulk it's clear that the average expression change scales with copy number, individual genes may not. The MLR analysis from the dosage series strains seems like the best way to detect these potentially subtle effects, though the false positive analysis was fairly convincing that even this analysis fell short in Hose et al.

To make the paper even more compelling, I would like to see some positive controls. That is, what would genes look like that truly do have some buffering against dosage? Can they ever be detected using the methods of either this paper or the Hose et al. one? The Introduction mentions ribosomal genes and histones, for example, so it would be interesting to see how they behave. It could be that detecting such subtle effects is currently beyond the abilities of current RNA measurement technologies.

In addition, the main argument of the Hose paper seems to be a difference between lab strains and natural isolates. A more direct comparison between the data from different strains in this paper would help compare these directly and demonstrate whether they are in fact showing identical patterns.

Reviewing Editor's comments:

The following editorial revisions are single examples of the type that must be made to the manuscript's tone, listed in order of occurrence in the manuscript. Re-review will focus on a detailed list of revisions, if edits are still needed.

Title

New title: “No current evidence for widespread dosage compensation in yeast”.

Abstract alterations:

“mostly lead to an according change in gene expression.” This is a nonsensical sentence, likely a typo.

“gene expression is not observed in wild…” to "gene expression can be violated in wild…".

“dosage compensation occurs neither in laboratory strains nor natural…” to "dosage compensation remains unproven in laboratory strains and natural variants."

Results headers:

All these should be re-worded to report results, not conclusions. For instance:

"Many wild yeast strains have unstable karyotypes." As the reviewers indicated, this is just one of the potential interpretations of the CNV data.

"No dosage compensation in…" (all sections). These are extrapolative and interpretive statements that should be toned down considerably.

Section titled "No dosage compensation in wild isolated YJM428…" should probably be split into two sections, based on the fact that the six yeast lines listed are explored as falling under two different explanations.
