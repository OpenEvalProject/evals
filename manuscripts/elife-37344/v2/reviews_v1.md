# Peer review - Round 1

Editors:
- Siu Sylvia Lee, Cornell University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.37344.038](https://doi.org/10.7554/eLife.37344.038)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Chromatin accessibility dynamics across C. elegans development and ageing" for consideration by eLife. Your article has been reviewed Jessica Tyler as the Senior Editor, a Reviewing Editor, and three reviewers. The following individual involved in review of your submission has agreed to reveal her identity: Bérénice A Benayoun (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The reviewers appreciated the high impact of the work, particularly as an important resource for the community. The reviewers generally agreed that the experimental designs and data analyses were rigorous and the results were well described.

Essential revisions:

1) A major point that needs to be addressed is the potential caveats relate to changes in cell numbers as pointed out by reviewer 2. This can be addressed textually, however the corresponding conclusions will need to modified accordingly.

2) The reviewers suggested a number of clarifications, including additional quality control analyses, and clear discussion of differences in methods. These include all specific comments from reviewers 1 and 3 below.

Reviewer #1:

This manuscript by Janes et al., described a novel dataset resource mapping chromatin elements throughout C. elegans lifespan, from development to adulthood, and, for the first time in worm, throughout several stages of adulthood. The authors identify > 40K elements with accessible chromatin in at least one of the assayed time points, with highly dynamic landscape of accessibility throughout worm lifespan. Using nuclear transcription profiling, to bypass the C. elegans specific trans-splicing phenomenon, the authors refine annotations of >15K promoter and > 19K enhancers. Both classes of elements seem to be able to drive bidirectional transcription based on follow-up reporter experiments in 2 lines.

The article does describe the resource dataset well, and the raw data is already readily available. This resource will be of broad interest to the aging and chromatin fields. A couple of points need to be further clarified, and some complementary analyses need to be performed for reproducibility and statistical soundness.

1) The young adult stage profiling is performed in 2 distinct contexts: WT N2 and the glp-1 mutant, serving as an anchor point between the developmental and adult datasets. The rationale for the switch is reasonable, but it would be important to discuss how similar/dissimilar the YA ATAC-seq data is between the two strains (N2 and glp-1 mutant).

2) In the Discussion section of similarity vs. dissimilarity with previous developmental datasets, it would also be important to include the state of culture: liquid vs. solid, as this may have broad consequences on gene activation patterns, notably in the muscle tissue. The Daugherty et al., paper used solid cultures, whereas this study had liquid cultures (according to subsection “Collection of developmental time series samples”). It would be important to include a significance of correlation test.

3) In the CV analysis (subsection “Patterns of histone marks at promoters and enhancers”/Figure 3), it may be useful to include a statistical analysis, for instance in the form of a significance of correlation test, and maybe a scatter plot.

4) In the Materials and methods section, the authors mention the use of "the Illumina TruSeq kit or a homemade equivalent". For the sake of reproducibility, it is important to include (i) a table listing which dataset was generated which each kit/method and (ii) a description of the "homemade equivalent (steps, enzymes, used suppliers).

5) For the tissue-specific enrichment analysis (Materials and methods section), the use of a background and how it was selected needs to be included. This choice can greatly affect observed enrichment results.

6) Metagene analysis are convenient representation tools but (i) they smooth away variations in the data, potentially masking heterogeneity, and (ii) have no statistical support for changes described. To fully support conclusions, the authors need to include a complementary statistical analysis for the data reported in Figure 3B, Figure 1—figure supplement 1C/D, Figure 2—figure supplement 1B/C, Figure 3—figure supplement 1B. This can be done by either including the 95% confidence interval on the metagene plots or performing a quantitative analysis using a boxplot and a non-parametric Wilcoxon rank-sum test.

Reviewer #2:

The authors present whole animal ATAC-seq data for six developmental stages of C. elegans along with five stages of aging adults to define accessible sites. They also collect long nuclear RNA-seq data for each time point in both time series to help classify the accessible sites into promoter and enhancer types. To further augment the developmental series in particular, the authors collected chromatin ChIP-seq data and short, capped nuclear RNA to assess chromatin state and transcription initiation, respectively. After assigning a type to the accessible regions, they cluster the promoter sites based on their accessibility over the developmental time course and the aging time course. Using single cell data from Cao et al., (2017) they find that some site clusters are associated with target genes with tissue-specific expression. They also use the single cell data in conjunction with ChIP-seq TF data to show that some TFs are preferentially associated with genes expressed in certain tissues.

Overall, the paper is well-written and the data sets seem of high quality. The chromatin accessibility data should be of considerable interest to the C. elegans community, and their evaluation of chromatin marks relative to promoters, enhancers, and the patterns of expression of the target genes should be of interest to the wider chromatin community. The fact that most sites change over time is not surprising, given that the expression of most genes changes considerably over time. This conclusion and the cluster analysis is complicated by the fact that the fraction of cells from any given tissue changes over time, and thus the fraction of reads from a peak associated with that tissue will change, even if accessibility at that site within that cell does not change over time. The clearest example is the gonad, where cells from this tissue go from being less than 1% of the total cell (genome) number to more than half over the course of larval development. An accessible site in gonad cells that was constant throughout this expansion would be expected to show a large increase over time, simply from the increasing cell number. Similarly, intestinal cells double their genomes with each larval molt. Neurons and muscle increase in L1 but not thereafter, so proportionally the signal from their accessible sites would be expected to diminish over time, even if accessibility remained constant. Indeed, the patterns of most of the assigned clusters for the developmental time course follow the expectation from cell numbers. Finally, the analysis of TF ChIP-seq data seems quite similar to that of Cao et al., except that the authors condition their analysis on overlap of ChIP-seq sites with accessible sites. However, since the overlap of accessible sites with ChIP-seq sites is very high, it is not clear what is new here.

In sum, the paper presents data sets that will provide an important resource for the worm community. The biological insights are modest in the present paper, but its utility to the community should produce valuable insights over time.

Reviewer #3:

The Janes et al., manuscript reports ATAC seq profiling along a developmental and aging time course in whole worm C. elegans. In general, the experimental design and the data processing all appear rigorous and well done. By comparing the ATAC data with RNA-seq of nuclear RNAs, the authors define many promoters and putative enhancers. Moreover, the authors found that many of the accessible sites show dynamic developmental regulation, and the sites are often associated with tissue-specific gene expression. Overall, the data reported represent an important resource for the community.

1) It will be important to show quality control analyses to assess the reproducibility of the data / between replicates.

2) Similarly, MDA or PCA to show the overall relatedness of the data from the different time points will be helpful.

3) For the ATAC data comparison with previously published data, the authors indicated that different peak calling parameters likely account for the differences. It will be helpful for the authors to examine their data using the previously published analysis pipelines (or vice versa) and provide some quantification of the differences / similarities between the datasets.
