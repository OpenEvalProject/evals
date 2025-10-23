# Peer review - Round 1

Editors:
- Gil McVean, Oxford University , United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.02504.021](https://doi.org/10.7554/eLife.02504.021)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for sending your work entitled “Genome-wide mapping in a natural hybrid zone reveals hybrid male sterility loci and Dobzhansky-Muller interactions” for consideration at eLife. Your article has been favorably evaluated by Detlef Weigel (Senior editor) and 3 reviewers, one of whom is a member of our Board of Reviewing Editors.

The Reviewing editor and the other reviewers discussed their comments before we reached a decision. We all feel that the design and direction of your experiment are important innovations and the work has the potential to be important in the field. However, there are a number of substantive points that need to be addressed. Moreover, the reviewers all felt that there were multiple aspects of analysis, presentation and interpretation that need to be improved.

Below, you will find the full reviews. I should note that it is not standard practice at eLife to return the full reviews in addition to the editor's summary. However, in this case I think the range of comments is a useful reflection of the responses of readers and are likely to be helpful in revision.

In terms of revising, the following major points need to be addressed:

Analysis: Given the large effect of the X chromosome it seems critical to include X variants in the covariance matrix. We also believe that more could be made of analyses of the genetic architecture of the trait (e.g. contribution of individual chromosomes to variance in the trait using GCTA or similar software). Similarly the DMI model makes specific predictions about the direction of epistatic effects (combinations of derived alleles deleterious) which should be easy to address by polarising variants using an outgroup.

Interpretation: The phenotype studied is not hybrid sterility (despite the Title). There is actually no direct evidence for an association between the trait studied and fitness. Indeed the statement that there were no significant results for sperm count is a little worrying. However, there is limited evidence that the phenotypes of the hybrids are typically outside the range of normal variation within the species. It is important to note these caveats.

Presentation: Without fine-mapping or replication, the ability to identify/localise specific genes as being important in the trait is limited. For this reason, we feel the emphasis on long lists of rather weakly-supported candidate genes is misplaced. There are also issues with formatting, clarity of figures and citations. Please concentrate on these above points in your revision. The comments below should help you in understanding details of these issues.

Reviewer #1:

The genetic study of reproductive isolation and speciation has the potential to be transformed by the large-scale study of genetic variation in hybrid zones and mapping experiments. This paper presents the first (at least as far as I know) GWAS of a reproductive isolation phenotype (relative testis weight) between Mus musculus musculus and M. m. domesticus from a hybrid zone. The principle findings are:

1) There are multiple (estimate of 26) regions across the genome contributing to the phenotype.

2) Some of the identified regions overlap with (or are close to) regions identified as affecting reproductive traits from F2 crosses.

3) Many of the regions harbour loci that also affect gene expression in the testis.

4) There is some evidence for interactions between loci, consistent with the DMI model.

These findings are of broad interest to the field and an interesting counterpart to the mapping results, though perhaps not unexpected and I feel not presented in as compelling a way as possible (see below). To be compelling, I think there has to be a more rigorous approach to validating the findings.

Major points:

1) A standard GWAS approach, using linear mixed models to account for relatedness between individuals is used. However, while human GWAS studies typically use 'genome-wide significant' (a somewhat vague term, but implying a conservative threshold for significance of 5e-8) and require replication, the approach taken here is to use an FDR approach with a generous threshold of 10% and no replication. Permutation studies presented show that this threshold is somewhat permissive. More generally, there is no attempt made to either establish how well calibrated the FDR approach is, nor to validate findings through replication. To me this is a serious limitation, and while I understand the authors' desire to maximise the findings from the study, I think a more limited, but well-validated, set of loci would be both more credible and of wider value. In short, I think validation of association signals in a replication set of samples is needed.

2) I would like to know more about the data. For example, how does relative testis weight vary with age (mice were killed across a range of ages), does it differ between the parental species? Likewise, more could be made from chromosome-scale analyses of variance; e.g. using GCTA. Similarly, it would be interesting to attempt to estimate dominance and epistatic variance components. Also, the DMI model makes specific predictions about the direction of interactions. I would like to know what fraction of identified interactions fit with a model in which derived allele (inferred using an outgroup) interactions are deleterious (as opposed to alternative scenarios).

3) Although each is largely minor, there are many comments about the methodology used; justifying methods and parameter choices. I am particularly concerned about the exclusion of the X chromosome from the relatedness matrix, not least because it apparently has such a large estimated effect. This needs to be addressed.

Reviewer #2:

The manuscript by Turner and Harr reports the genome-wide mapping of relative testis-weight loci segregating in a natural hybrid zone of Mus m. musculus and Mus m. domesticus. They combined the high resolution Mouse Diversity Genotyping array for GWAS analysis with microarray-based gene expression analysis of the whole testis to identify the genomic loci potentially involved in reproductive isolation between both species. The logic of the experiments is difficult to follow without first reading their previous paper (Turner et al. Evolution 66:443). Even then, there are three main concerns: First and most important, the phenotype studied is complex and in respect to hybrid sterility rather vague. Testes weight (or relative TW) variation can reflect genetically determined variations without any defect, various defects in haploid phase of meiosis, intrameiotic arrests of various causes and various extent, or even a premeiotic block. If rTW is taken as the only phenotypic trait it is not surprising that the outcome is so complex and its interpretation necessarily difficult. If, at least, histological evaluation and, for example, sperm count were included, the information value would have been much higher.

Second, the use of the term “hybrid sterility loci” seems as a kind of overstatement, because none of the examined males proved to be sterile. In fact, Turner et al. 2011 Evolution paper states 'breeding data do show that hybrids have similar fertility to pure subspecies pairs' (text and Table 2). Moreover, their breeding scheme was designed to maximize the number of hybrid offspring. Thus a significant portion of variation in testes weight could reflect physiological intra- and inter-species QTLs. The argument that variation is much larger in hybrid males than in pure species is weakened by the low number of examined pure species males (See also their Evolution paper).

Third, the Dobrzhansky-Muller incompatibilities, which result in lowering testes weight can favor the involvement of such loci in reproductive isolation. The authors found 149 such chromosomal region pairs but their documentation is missing, perhaps with the exception of Figure 5, which, however, seems to show only expression DMIs (?).

In conclusion, the strength of the paper includes the first attempt to use GWAS on wild mice from a hybrid zone to infer the genetic networks involved in reproductive isolation of a young species pair. The main weak point is the inadequate phenotype selected for quantification and consequent overstatements in the interpretation of the obtained data.

Reviewer #3:

In this study, the authors use crosses among wild mice collected in the hybrid zone between M. m. musculus and M. m. domesticus to map genomic regions associated with reduced relative testis weight in hybrid males. This is a novel approach to identifying regions associated with hybrid male sterility in a system of general interest to the evolutionary genetics community. They found 26 regions across the genome, all of which interacted with at least one partner and most of which interacted with many. They also used GWAS to identify loci associated with variation in expression of testis-expressed genes. The approach seems appropriate and well executed.

My substantive comments are regarding organization, clarity and the interpretation of results. These should be remedied easily with a short round of editing.

The writing could be tighter and clearer, especially in the Abstract and Introduction. Be upfront about the advantages and disadvantages of the approach and clearly summarize the approach and major findings. Hybrid zone analyses reflect current processes in a zone of secondary contact that is relatively recent. Their significance to initial phases of reproductive isolation in allopatry is bolstered when there is overlap between this approach and QTL mapping studies. In addition, even if these specific regions were not critical in early phases, they give insight into the genetic architecture of traits that almost certainly were important.

I was often confused in the manuscript regarding which results were being referred to when e.g. which regions are being referred to in the sentence “All significant regions are involved in”?

Citations are a bit sloppy. For example, in the first paragraph of the Introduction, the authors posit that two approaches have recently substantially advanced understanding. I expected some citations of recent work and instead found only citations from Dobzhansky and Muller. Another example, the citations for “the long-recognized potential for mapping in hybrid zones...” contain only relatively recent papers. This could be easily remedied by adding “for review, see Reiseberg and Buerkle” given that that paper does review some of the older work in the system. There are many additional citations that should be considered for the statement that “islands may not always represent targets of selection...” All in all, I would suggest going through the manuscript more carefully and including citations more consistently and broadly.

More information about the system would also be useful in the Introduction, e.g. what are the three subspecies of house mice, how long have they been diverged, how old is the hybrid zone, etc. What have we learned previously? The Abstract does not actually give the names of the two subspecies.

Explain why there may and may not be overlap between loci uncovered using mapping in hybrid zones and mapping between allopatric populations.

I think this section could be re-organized to make the whole approach clearer. Explain motivation for insight into nature and timing of fertility defects. Why consider testis expression changes in the context of infertility? Give more info on what was actually done. You associated specific loci with variation in what measure of expression? Help the reader more clearly connect your results to specific insight (this refers to paragraph 1 and 2 in this section).

Candidate genes:

First sentence, identified genes from which of the previous analyses? Make the methods for identifying specific genes more explicitly methodical. First, we looked at all genes in the 26 regions with... Then we focused on the genes that were implicated in both this analysis and...

Success of GWAS:

This section seems a bit unclear. Is it GWAS that was very successful or using many different approaches? What is the success here-identification of relatively few locit or better characterization of the architecture? Be upfront about the possible downsides (environmental effects, phenotype characterization).

The entire simulation section needs more explanation and justification. Many tables and figures are devoted to this (many which could be supplemental) but the explanation is very slight. Insight into the importance of which factors in the simulations? There are three criteria for true or false positives-which ones correspond to something you considered true and which ones false? What do the results mean for the interpretation of results?

Genetic Architecture:

This section seems weak. What do you find? How does this compare with previous studies? What does this study in particular add? The reference to the Snowball effect is too slight to be effective.
