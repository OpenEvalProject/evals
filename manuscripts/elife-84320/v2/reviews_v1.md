# Peer review - Round 1

Editors:
- Jessica K Tyler, https://ror.org/02r109517 Weill Cornell Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84320.sa0](https://doi.org/10.7554/eLife.84320.sa0)

The unexpected localization of a cell cycle checkpoint kinase, Rad53, to promoters in response to replication stress suggests that Rad53 may help coordinate transcription in response to disrupted replication. This work will be of interest to those interested in the interplay between genome stability and gene expression.


---

# Peer review - Round 1

Editors:
- Jessica K Tyler, https://ror.org/02r109517 Weill Cornell Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84320.sa1](https://doi.org/10.7554/eLife.84320.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "Prevalent and Dynamic Binding of the Cell Cycle Checkpoint Kinase Rad53 to Gene Promoters" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Miles A Pufall (Reviewer #2).

Comments to the Authors:

We are sorry to say that, after consultation with the reviewers, we have decided that this work will not be considered further for publication by eLife.

After discussing the manuscript, the reviewers and the reviewing editor concluded that while the paper reports a series of interesting observations related to Rad53 binding to gene promoters independent of checkpoint signaling, the reviewers found the main message of the paper to be unclear. The paper starts with an attempt to look at RAD53 binding to replicons, but finds binding of RAD53 to promoter sites in G1 and in the absence of replication stress. Despite this intriguing observation, the results are analyzed with respect to stressed replication. As a result, the paper does not address reasons or consequences of the observed phenotype other than transcription/replication collisions.

From a technical point of view, all reviewers were concerned with the lack of statistics to draw inferences regarding the central question: Does Rad53 coordinate both replication and transcription in response to stress, and do the mutants disrupt this coordination. While it is often useful, to note a trend that is worth exploring, where numbers are available the validity of these inferences must be drawn to strengthen the conclusions.

Reviewer #1:

Strength: Upon first reading of the abstract, there was some concern that the observed Rad53 ChIP-seq at promoters could be related to the "expression bias" previously reported in ChIP-seq data sets, where false peaks were observed at some highly-expressed genes, even for exogeneous non-DNA binding proteins. The authors' analyses, especially lines 229-246, alleviate this concern.

Oftentimes throughout the manuscript the authors mention trends in the data, but without providing actual numbers. E.g. on line 180: "we noticed many Rad53 peaks […] and many of these localized […]"; providing numbers would be helpful for readers to understand the scale of the observed trends. The authors refer to specific figures, but those figures do not contain any numbers either.

As another example, at line 198, the authors say "Additional genes show increased Rad53 binding […], but at other promoters Rad53 binding decreases during the same time course […]. However, at most genes Rad53 remains constant." Numbers would be helpful here. Also, how were the increases and decreases called? What statistical tests and cutoffs were used to make these calls?

Same questions for page 6, lines 216-217. And also line 221, "numerous gene promoters" – could this be expressed as a fraction of all gene promoters in yeast?

The authors used "residual analysis in WT" to identify "the top differentially binding (DB) genes" in each set. Why residual analysis and not an established tool for differential binding, such as DEseq? And how were the different experiments in each set combined? For example, the TP set has 3 transcription factor null mutants and one WT condition. Comparing each mutant to the WT will gives three sets of differentially bound gene promoters; how are these combined? Is the direction of the change always the same across the 3 mutants? If not, what is reported in Figure 4b? What exactly is the y-axis in this figure panel?

The authors continue to say "Many of these genes encode proteins involved in cell cycle progression and cell growth". How was this determined? Was a statistical analysis (like GSEA) performed?

The relevance of the comparison between Rad53 ChIP-seq and Swi6 ChIP-seq is not entire clear. Did the authors mean to illustrate that although Rad53 binds to promoters, its pattern of binding is different from that of transcription factors? I.e. Rad53 binds a large set of promoters, but the range of binding signals is generally narrow, while transcription factors tend to bind strongly but to fewer promoters? If this was the intended purpose of the analysis (presented at lines 221-227), why was Swi6 selected? Would other cell-cycle transcription factors also be relevant for this type of analysis?

The comparisons between Rad53 binding and gene expression (line 248-284) show a clear positive correlation, especially in certain gene subsets/clusters. Further analyses, focused on targets of SBF, MBF, Msn4 and Ste12, confirm these correlations on subsets of genes targeted by these transcription factors. But it is unclear, to this reviewer, whether the authors conclusion that "regulation by SBF appears to be responsible for the correlation between increased Rad53 binding at the promoter and up-regulation of these target genes" is truly supported by the data. The correlations and overlaps are compelling, this is true, but are these significant and do they point to causality?

In Figure 8b, the authors highlight a few SBF targets that show "significant deviation" from the global trend. (How what the significance assessed?) But these are just the SBF targets in the "Top DB" set, i.e. in differentially bound gene promoters. Since this is how they were selected, shouldn't we expect them to deviate from the global trend? It is not clear how this finding shows that "Rad53 signal changes at these genes depends on SBF". This section (lines 364-283) continues with some examples of specific genes and their Rad53 promoter binding chances. But it is not clear what the general conclusion is according to these data.

One aspect that makes the manuscript difficult to read is that there are many observations reported throughout the paper, but it is not always clear how they relate to the main message of the paper. E.g. line 132: "the replication fork collapse was more severe in the absence of Rad53 kinase compared to the absence of checkpoint signaling in the mrcD mutant". This is an interesting observation, but what is the relevance for the main message of the paper?

As another example, in the paragraph at line 60 (Introduction), the authors talk about Rfx1 and Ixr1 transcription factors, and the RNR genes. But the relevance of this is unclear at this point.

As another example, the section at pages 7-8, lines 286-327, discusses Rad53 binding at gene bodies, rather than promoters. This is an interesting finding, but it distracts from the main message of the paper.

Page 5: The authors separate their ChIP-seq experiments into two groups, or sets: the CP set (WT, Rad53 mutant, and mrc1D) and the TP set (ixr1D, swi4D, swi6D and WT). While the conditions in the CP set are the ones used throughout the paper, the motivation behind the TP set in unclear. How were these particular factors selected? And are the "WT" assays the same in the two groups? For the transcription factors, the authors say they are selected "based on the types of genes that bind Rad53", but no other details are provided.

How was differential gene expression performed? (Figure 5)

Line 343: what does "enrichment score" refer to here? For this analysis, Fisher's exact test seems to be the most appropriate test for assessing enrichment of the Swi4/Swi6 targets among the differentially expressed genes.

For scatterplot analyses, e.g. Figure 8, there is no statistical analysis of the observed correlations. What are the R2 values and the corresponding p-values for these correlations?

As mentioned above, the choice of transcription factor null mutants for the Rad53 ChIP-seq experiments is not clearly motivated. SBF (Swi6+Swi4) is definitely a relevant choice, but would this be the top choice in an unbiased analysis of transcription factor proteins? Data on transcription factor gene targets is available for many factors in yeast. An unbiased analysis across all transcription factors could be performed to determine which factor shows the most significant (Fisher's test?) overlap with gene promoters bound by Rad53. In such an analysis, would SBF be the top candidate? If so, this kind of analysis would significantly strengthen the manuscript. Similarly, how was Ixr1 chosen? Was it meant as a control?

Reviewer #2:

In the manuscript entitled "Prevalent and Dynamic Binding of the Cell Cycle Checkpoint Kinase Rad53 to Gene Promoters" the authors explore the possibility that occupancy by the replication machinery influences regulation of genes. To do this, the authors measure the occupancy of Rad53, a key signaling kinase for the DNA replication checkpoint (DRC) that binds to replication origins. The authors measure occupancy after putting cells under stress with hydroxyurea in both wild-type cells and in cells in which the DRC is impaired through a mutation in Rad53 and by deletion of Mrc1. With an intact DRC, early origins of replication are activated and are occupied by Rad53. When the DRC is impaired early origins of replication are also activated and are occupied by Rad53, but late origins of replication are activated and occupied as well, indicating a bypass of the DRC. In a key finding, it is also noted that Rad53 occupies regions that are upstream and downstream of a large number of genes, and that the expression of thousands of genes is altered when the DRC is impaired. A difference in Rad53 occupancy near genes often correlates with changes in the expression of these genes. In particular, it appears that an increase in Rad53 binding close to the transcription start site of genes, both upstream and downstream, is correlated with the reduced expression of these genes. A deeper analysis of SBF target genes related to cell cycle and mating-type switching shows a correlation between Rad53 occupancy and gene expression. This appears to show two roles for Rad53 occupancy: inhibition of transcription at some genes when checkpoints are impaired, but also potentially as a transcriptional activator at others. With these roles, the authors assert that Rad53 coordinates both replication and gene expression under replication stress.

There are two major strengths to this manuscript. The first is that transcription-replication conflicts are increasingly being realized as occurring in eukaryotes, and this manuscript provides an excellent example of when such conflicts might occur. The carefully chosen mutants that bypass DRC even under stress show the aberrant firing of late origins in the proximity of genes whose expression is impaired. This provides a relevant and useful system to study conflicts when replication and transcription are not coordinated. The second major strength of this manuscript is the thorough collection of rich data sets in this system. The correlation of origin activity, Rad53 occupancy, and gene expression in WT and mutant backgrounds before and after administration of HU to induce replication allows probing of correlations between aberrant responses to stress and gene expression. The authors provide useful analyses of these data and demonstrate that bypass-induced binding of Rad53 correlates with reduced gene expression at numerous genes. Thus, their main assertions are supported by the data.

The main overall weaknesses of the paper are that it is difficult to read with little effort spent to make the work accessible outside the field of replication stress, the findings are not always well connected to provide a convincing argument, the figure resolution often makes them unreadable and impossible to interpret, and some statistical analyses are either missing or inappropriate. The weaknesses are detailed below:

There is a widespread use of indefinite quantifiers (some, many, several) to make quantitative inferences. Such as:

Line 200: "most genes" remain constant. How may genes go up, down, and remain constant?

Line 221: "Visual inspection of the ChIP-seq peaks suggested that Rad53 bound to numerous gene promoters and TSSs throughout the genome." How many is numerous? What fraction of TSSs?

Line 305: "Overall, most of the down regulated genes in cluster 1 of this group are situated very close to active origins". Reporting numbers make this more convincing.

Line 316: "More down regulated genes are found when the nearby origins are active." Reporting numbers make this more convincing.

Virtually all of the SBF target analysis.

Without quantification and statistics these amount to anecdotal observations. A quantitative inference requires the exact counting of groups followed by a statistical test.

Comment 1: The introduction is confusing. Line 47: After describing DRC and DDC along with four different kinases, the final sentence states that "the signaling" promotes widespread gene expression changes. All signaling? Rad53 specifically? Line 50 says that Mac1 and Rad53 are essential for cell viability, but Line 52 states that kinase null mutants (presumably either kinase?) are extremely sick. Which is it, sick or dead (essential)? The next sentence states that under bypass conditions (not defined) that sml1- and rad53- cells exhibit a "more severe defect" than mec1- cells, and that implies a role for Rad53 beyond DRC. This is either contradictory to Rad53 being essential, or too much background is left out to understand this pathway under different conditions. In addition, the authors already state that Rad53 has a role in DDC, which is beyond its function in DRC. Later the authors do not do a good job connecting RNR to "upregulating dNTP pools". This introduction may be clear to those familiar with Rad53 already, but not for others including those interested in transcription regulation or other aspects of signaling.

As a smaller point, the authors claim in the last paragraph that Rad53 is localized to 20% of promoters suggesting a "global" role in coordinating the response. 20% is not global – it may indicate a multifaceted role in response but global is a very high bar.

Comment 2: Most of the intro talks about the central role of Mec1 in sensing stress – yet the authors chose to first explore mrc1- cells and their stress response. What's the rationale for choosing that and not mec1-?

Comment 3, Line 84. The title doesn't help the reader understand the result. Having more heading that emphasized the results might help the reader more.

Comment 4: Line 101. The accounting for early, late, and inactive origins is confusing in the text but explained better in the methods. In this accounting early is defined as active in WT and late is defined as active in the mutants but not wild type. However, in Figure 2 origins are ranked according to replication timing define elsewhere (Yabuki 2002). Why the difference in the categorization? Do the classifications match perfectly? If so, why not use the Yabuki classification for both and avoid confusion?

Comment 5, Line 105. The assertion is that rad53_K227A favors late origins over early. Figure 1b shows a scatter plot with signal as the y-axis. It appears that a statistical test has been done to presumably show a significant difference between E (early) and L (late). What test was done (not described in body or figure)? Is the test for the difference in signal? If for signal, it could be that there are strong late ORCs, but more early ORCs – which would be a different test. My reading of "favor" late ORCs would be that there is a greater number of late than early, and that signal is how active the favored ORCs are.

Comment 6, line 138. The meaning of "the status of replisomes" is not defined and potentially broad. Something more specific would be helpful.

Comment 7, Line 146. The evidence of "slower progression" of Cdc45 away from the origin in mrc1- mutants is not clear to me. Could the authors describe what they are seeing to help the reader? The heat maps in Figure 2 Supplement 1 are duplicated in Figure 2 b,d, and f. This is not necessary and could be (was) confusing. Further, the Replication TIme scales in Figures 2b,d, and f seem to overlap between early and late – which is odd.

Comment 8, Line 163 "In contrast, the Mrc1 is not strictly required to induce or maintain -H2A." is a conclusion that is drawn without describing the result. The result appears to be that gammaH2A deposition is strong in the mutant and persists even at late time points.

Comment 9: The speculation in paragraph lines 166-169 would fit better in the discussion.

Comment 10, line 173. "dispersed in late times" – there is only one late time, HU90.

Comment 11, line 183. The claim that Rad53 signal increases from HU45 to HU90 is not 100% clear from the plots, and requires some type of test. Diffbind is great for this. Also – "A similar pattern occurs at the RNR3 promoter" I don't see this labeled in Figure 3.

Comment 12, line 190. How is "upstream" of the promoter defined? 1kb? 10kb? I don't see it in the results or methods.

Comment 13, paragraph 190-200. This is a discussion of Rad53 binding near TSSs. The fractions reported are the fraction of Rad53 peaks near genes. This is interesting, but the abstract reports that Rad53 "coordinates…genome-wide transcription" and binds "20%" of promoters. The number of promoters occupied by Rad53 is not reported here and should be accounted for to make these claims.

Comment 14: Paragraph lines 202-210. I found this paragraph confusing. First, the description of residual analysis in the methods was confusing. Summing in 25bp windows over 500bp upstream of TSS seems an odd way to calculate enrichment within a region, corrected for counts. R packages such as DiffBind do this quite rigorously, handle replicates well, and report differentially enriched regions with p-values. Also, reporting the difference in enrichment in regions between conditions is confusing – why not just enriched or depleted occupancy? I also could not quite follow what was meant by "435 genes identified in both". Please clarify, as much of the manuscript relies on this classification.

Comment 15. Figure 3d is not described in the legend, nor how it was calculated in the methods. This could be a useful plot but needs to be described.

Comment 16. The clustering conclusions in paragraph lines 250-256 draw distinctions that are not evident. The paragraph states that there is little difference in samples in G1, yet rad53-mutant and mrc1- samples cluster together. The paragraph also states that different from G1, rad53-mutant, and mrc1- samples cluster together in HU45 and HU90. The repeats of each mutant cluster together, but are not even always in the same clade (HU90). This interpretation is a stretch.

Comment 17. Lines 267-273. I had to read up on co-expression analysis and clustering. It is not clear to me why co-expression analysis is more useful than simple k-means clustering to identify sets of similarly differentially expressed genes. Perhaps a few words on why this method was chosen.

Comment 18. Line 321: "Furthermore, the bias toward the down regulation is even stronger (>80%) when the nearby origin is in a head-on orientation towards the gene." What is the percent when co-directional? Is the difference significant? It looks close enough that discerning a difference might require a statistical test (Fisher's Exact).

Comment 19. I had a hard time following the analysis of SBF and MBF target genes (page 8). First, an "Enrichment Score" is reported for the inclusion of SBF genes in the DEG set. I don't know what an enrichment score is. A more useful score is whether the number of potential SBF target genes is more likely to be differentially regulated than another random transcriptional complex. This can be calculated using Fisher's exact test. Otherwise, reporting that 36 out of 81 is anecdotal (unless the enrichment score is explained better). Second, Figures 8a bottom were impossible to read, and it was not clear what conclusions were to be drawn from them. Lastly, in paragraph lines 367-382, an analysis of the enrichment near genes in SBF mutants was performed. It is asserted that there is a "significant" difference in the enrichment of SBF targets among Top DBs – how was significance calculated? Then, in a series of pictures (Figure 8b insets) that the position of some enrichment is collapsed in mutants. Is this just visual? Calculating the Z-scores for these points and showing that the Z-scores reduce significantly would be a straightforward way to determine that the occupancy collapses toward the average.

Comment 20, lines 439-440. "Our data is consistent with the possibility that the Rad53 kinase contributes to the transcription regulation as a structural component" I don't know what this means. The manuscript asserts that the activity of Rad53 matters – so what is meant by the assertion that it is a "structural component"?

Comment 21. For rigor and reproducibility, the processing code should be included, preferably with raw data, in a manner that can be validated by the reviewer with one or few commands.

Reviewer #3:

In this study the authors find that unexpectedly RAD53 is bound to promotor regions of 20% of all yeast genes. The authors use genome wide ChIP-seq and correlative analysis to gene expression. Because of its known function during replication stress, experiments were designed with replication stress perturbation. However, the authors found RAD53 is bound to the promotor regions in G1 and without stress, and independent of canonical checkpoint signaling, making an analysis of experiments with replication stress somewhat illogical in the context of the specific discovery. Moreover, it introduces multiple additional variables directly affecting gene expression. This challenges the strength of interpretations of the correlations made.

Generally the correlations between RAD53 promotor biding and gene expression (some genes are some not) appear to be low. It is also unclear from the manuscript what matrix the authors use to claim significance of a given correlation.

Moreover, alternative interpretations are not considered. The authors solely investigate RAD53 promotor binding for its correlative effects on gene expression. While the finding that RAD53 is bound to promotor sites in the absence of stress is very interesting and promises for a potential greater implication of repair proteins in the conservation of transcription, promotor site binding of repair proteins have been previously reported Specifically, NEIL1 is preloaded at promotor sites of evolutionary critical genes and shown to promote rapid and efficient repair of promotor sites for conversation of critical genes. Such alternatives interpretation are not considered.

The authors may want to consider discussing (Nucleic Acids Research, Volume 49, Issue 1, 11 January 2021, Pages 221-243,) in the context of their discovery.

The authors use a kinase dead RAD53 mutant and a checkpoint dead mutant strain to suggest that RAD53 promotor binding is independent of a stress response. Recruitment to chromatin has been shown to involve acetylation rather than phosphorylation, as seen for Neil1, thus could be considered as an alternative to phosphorylation as stress signals, and alternative RAD53 mutant strains could be considered.
