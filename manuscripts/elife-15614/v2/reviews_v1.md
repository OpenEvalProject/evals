# Peer review - Round 1

Editors:
- Joel K Elmquist, University of Texas Southwestern Medical Center , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.15614.023](https://doi.org/10.7554/eLife.15614.023)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: this article was originally rejected after discussions between the reviewers, but the authors were invited to resubmit after an appeal against the decision.]

Thank you for submitting your work entitled "Hypothalamic transcriptomes of 99 mouse strains reveal trans eQTL hotspots, splicing QTLs and novel non-coding genes" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Mark McCarthy as the Senior Editor. One of the three reviewers has agreed to reveal her identity: Penelope Bonnen (Reviewer #1).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

While all of the reviewers found your data to be of potential interest, they all raised substantive concerns regarding both study design and data presentation. The consensus was that addressing all of these issues would entail substantial work. As you may know, one of the goals of eLife is to avoid protracted cycles of "long-loop" revision, and this means that we try to avoid any recommendations for revision that are likely to take longer than a few weeks.

Reviewer #1:

1) Trans eQTL hotspots analysis is nicely done and the authors relate two well-supported and interesting examples of trans eQTLs. Two comments for this section. Firstly, the method used to identify regions of trans eQTLs was blind to LD; a simple distance (100 kb) based bin was used and the number of trans acting SNPs counted. The authors relate that a 'hotspot' of trans acting SNPs contained several SNPs in LD with each other. This approach is valid, but may skew results to identify regions with a larger number of trans acting SNPs because of the underlying LD structure. In this case LD helps to identify these regions. However, there may be regions with less LD but still strong trans acting SNPs; using the method these regions will be de-emphasized, not due to the strength of trans acting elements but rather due to LD architecture of the genome. The authors may wish to mention this. Second, poorly annotated regions of the genome are not devoid of functional elements and it may be a bit of an overstatement to say the eQTL SNPs in these regions are unlikely to be causative.

2) Which lincRNAs were included in the association testing between lincRNAs and HMDP phenotypes? Were both the 381 plus 129 novel tested? In particular it would be interesting to clarify if any of the 129 newly identified lincRNAs associate with HMDP phenotypes. This reviewer found this sentence a little confusing 'none of these lincRNA were previously reported in the hypothalmus'; does this mean they all belonged to the group of 129 novel lincRNAs? Were these 129 totally novel or simply not previously known to be expressed in the hypothalamus? Some clarification would be helpful and would emphasize the findings that are particular to this study.

Reviewer #1 (Additional data files and statistical comments):

Please include the top 500 transcripts that associate with a phenotype in supplemental materials listed along with transcript ID, phenotype, and p-value. These are referred to in the first paragraph of the subsection “Association of hypothalamic expression and phenotypes” and are a valuable work product of this study. As such readers may benefit from this information.

Reviewer #2:

This manuscript focuses on a detailed analysis of hypothalamic transcriptomes from 99 mouse strains to among many things identify eQTL, spicing eQTL and novel non-coding genes and their relationship to metabolic and cardiovascular traits. Many of the aspects of the relevance or tissue-specific findings pertaining to hypothalamus were not well clarified leading to a concern with the overall study design. Many of the analyses suffer from potential interpretation or technical flaws limiting my enthusiasm.

A key feature of the manuscript is the identification of numerous novel isoforms and genes. It is an exceptional feature that the authors are able to confirm their data using peptide data. However, most of these are pseudogenes when manual characterized against NCBI and UCSC. Is this simply a deficiency in the GENCODE M2 annotation? Further, can the authors discount mismapped reads from highly homologous sequences to these pseudogenes. Key aspects of this pipeline are not well presented and I am very skeptical of the "novelty" of the set of genes they have found or even their relevance to the hypothalamus in specific let alone any hypothalamus specific function. Criteria for tissue-specificity should further be better described.

The distal eQTL information provides no extra information. Indeed, the authors themselves describe it as most likely a local signal.

The correlation of ASE and eQTL is a technical feature that has been reported in several other papers. It shouldn't be listed as a major feature of the manuscript and would be better as supplemental information.

The authors derive their own ASE approach using DEseq. This is not a conventional approach for this tool. Other published ASE-specific software exists. Can the authors explain why they did it this way?

How correlated are ASE sites within a gene? Does this support site aggregation for a gene-centric approach?

Trans-eQTLs can be spurious due to the chance correlation of a genetic marker with technical factors such as batch or biological factors such as sex or BMI. The authors do not provide enough detail/experimentation as to make these effects believable as true trans-eQTLs compared to spurious correlations.

Furthermore, for RNA-seq data many 1-1 trans-eQTLs can be the product of mismapping and are clearly identified when looking at the distribution of reads across a gene model in a tool like IGV.

The comment on rs31703733 is very speculative. The authors should prove that this is the case otherwise, I am not sure there is anything that can be definitely said about trans-eQTLs in this manuscript.

Some of the statements in the manuscript could benefit from more formally described multiple testing correction or an FDR. For instance "35% of lincRNA.… significantly (p<1e-3) correlate to at least one phenotype in the HMDP". If I do some rudimentary correction assuming 150 traits, I am not sure this is a significant finding. This is an issue for the trait analysis of the novel transcripts too.

How believable are the non A-to-G modification? Is 30% an expected number?

Reviewer #3:

In this manuscript, Hasin-Brumshtein and coauthors provide a systems-level analysis of hypothalamic gene expression, its regulation by genetic elements, and its association with metabolic phenotypes. The hypothalamus is composed of diverse and distributed neuronal subpopulations that control multiple aspects of metabolic homeostasis. Here, the authors test the hypothesis that differences in hypothalamic gene expression in a hybrid mouse diversity panel (HMDP) may influence the sensitivity of particular strains to phenotypes associated with diet-induced obesity. The authors provide two specific examples from their data of transcripts (1 annotated and 1 lincRNA) whose expression correlates with a specific metabolic endpoint (Figures 4E and 5D). To increase confidence in the analysis, the authors should validate the hypothalamic expression differences between strains for a handful of these transcripts by in situ hybridization.

Overall, the lack of functional validation of candidate genes with phenotypic outcomes severely limits this as a resource, and greatly diminishes the impact of this study. Nonetheless, this study does begin offering a detailed mapping of genomic regions underlying differential gene expression and RNA processing events in the hypothalamus, which with additional work could enhance our functional understanding of the hypothalamus. However, in its present form, it is not accessible to the research community working in the hypothalamus.

Hasin-Brumshtein et al. characterize the expression of both annotated and novel genes, transcript variants, and lincRNAs from the hypothalamus of mice representing 99 strains from the HMDP. The effort invested in obtaining and analyzing both genomic and proteomic data at this scale is impressive. However, profiling data presented would benefit from a more thorough description of mouse husbandry conditions prior to tissue collection. Were the mice raised on the same chow diet used by Parks et al. (2013) to establish the phenotypic responses of mice in the HMDP to high fat, high sucrose diet? In fact, the authors' description in the Introduction suggests that RNA-Seq was performed on "mice… fed a high fat high sugar diet." If so, it is unclear if the observed expression differences across the mouse strains drive their unique phenotypic responses to dietary challenge or if these differences are a response to such a challenge. Similarly, since RNA-Seq was performed on as few as 1 subject per strain, the authors should elaborate on steps taken to mitigate other environmental factors that might have influenced gene expression in the mice. Why not increase the power of this study by increasing the numbers on the most commonly used strains with the greatest divergence in metabolic outcomes?

The authors do acknowledge one major weakness which is the pan-hypothalamic approach, thus reducing their ability to identify genotype/phenotype associations with transcripts (Discussion, sixth paragraph). However, the statement at the end of that paragraph: "transcription… was shown to be largely shared among tissues and cell types" is confusing. If this is true, would not the small differences in expression between subpopulations of neurons be the most important in determining their functional specificity and in turn contribute to phenotypic differences? Such small differences are the least likely to be identified by analyzing the whole hypothalamus. Alternatively, the differences could arise from altered synaptic connectivity, which would also be difficult to resolve by expression profiling. This is an important point that is never discussed.

In addition, given that the hypothalamus is a critical region for many important sex-dependent metabolic and behavioral outcomes due to signaling from sexually dimorphic subsets of neurons, one wants to know how these data compare between male and females.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for resubmitting your work entitled "Hypothalamic transcriptomes of 99 mouse strains reveal trans eQTL hotspots, splicing QTLs and novel non-coding genes" for further consideration at eLife. We were receptive to the basis of your appeal, and the revised article has been favorably evaluated by Mark McCarthy (Senior editor), the original Reviewing editor, and by the more critical of the previous sets of reviewers.

All of us are positive about your revision. However, there are a couple of issues that remain to be addressed before acceptance, as outlined below:

1) The caveat the authors have added to the text is acceptable but the authors should look at Gencode M4 and see if there are overlaps with their genes. This annotation has been available for 2.5 years and is the most current mouse annotation file. M2 dates back to 2013. The rationale that annotation changes too rapidly ("month-to-month") is not supported by the Gencode release dates and since the novelty of these transcripts is a major feature, it should be put in line with the latest (2.5y old) annotation. One could simply overlap novel locations with bed files of latest annotations at a minimum.

2) Another issue that remains is the trans-eQTL results as any SNP correlated with a batch effect can appear as a trans-eQTL hotspot. The trans-eqtl on chr15 relevant to ion transport might be reflecting circadian rhythm. http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2819050/

The authors should explore this issue in more detail or properly caveat it too.
