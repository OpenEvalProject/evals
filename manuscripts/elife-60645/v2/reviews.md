# Peer review - Round 1

Editors:
- Patricia J Wittkopp, University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.60645.sa1](https://doi.org/10.7554/eLife.60645.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

We are excited to publish this work because it presents a novel, creative strategy for studying variation in RNA and protein expression in parallel. It then uses this strategy to simultaneously quantify RNA and protein expression in genetically variable cells and examines the genetic basis for this expression variation. Consistent with prior work, they find different loci contributing to variation in RNA and protein expression, but this work greatly strengthens this observation because the new methodology removes many other possible sources of differences between the two.

Decision letter after peer review:

Thank you for submitting your article "Simultaneous quantification of mRNA and protein in single cells reveals post-transcriptional effects of genetic variation" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Patricia Wittkopp as the Senior and Reviewing Editor. The following individual involved in review of your submission has agreed to reveal their identity: David Gresham (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

This paper presents a creative, novel strategy for quantifying expression of RNA and protein of the same genes in the same cells. While some concerns were raised about the mRNA level plateau that will need to be addressed, the methods and analyses were generally felt to be sound. Using this clever method, levels of mRNA and protein were used to simultaneously map QTL affecting mRNA and protein expression levels. The primary finding was that different QTL are affecting these two levels of gene expression, which is consistent with prior work. This consistency lead to a range of opinions about the novelty of the work.

In a revision, it will be critical to make more clear the new biological insight provided by the work, beyond the experimental design. Specifically, you should more clearly state what was learned about eQTLs and pQTLs with these new approaches that goes beyond what was already known. Clarifying expectations would also help: Do you expect to simultaneously have the same eQTLs and pQTLs? What are the molecular mechanisms responsible for different mRNA and pQTLs? Authors claim that is not statistical, however large effect trans-QTLs are conserved across e-pQTLs. Either way, how different trans-factors can interact with target genes and be responsible for expression and protein differences?

We have left the full set of reviewer comments below in this case because they contain detailed, specific, and complementary comments and reflect this range of opinions.

Reviewer #1:

In this paper, Brion et al. performed expression QTL mapping in a budding yeast cross using two methods for quantifying gene expression at the level of transcript abundance and protein abundance. Previous eQTL studies have been performed separately for transcript abundance and protein abundance using separate experimental procedures. These studies have found that there is a largely unique set of trans QTL that underlie interindividual variation in mRNA and protein abundance. However, these comparative analyses have a number of limitations that the authors outline. To rigorously address the extent to which these loci overlap the authors developed a method that enables simultaneous detection of protein and mRNA levels in single cells. Protein expression is detected using GFP fusions. mRNA expression is quantified using a novel, and clever, CRISPR-based system that uses self-cleaving ribozymes to generate a guide RNA that directs a dCas9 to drive expression of mCherry. Using this approach the authors performed bulk segregant mapping in a cross between two yeast strains to map loci that underlie differences in expression of mRNA and protein. Consistent with prior studies, they find little overlap between eQTL affecting the two levels of expression. They follow up on one locus, YAK1, in detail using RNAseq and mass spec.

This is an interesting study that presents a very clever method of quantifying mRNA and protein expression simultaneously. The experiments and analysis are well-performed. Although the result is consistent with previous studies, it greatly strengthens those observations and thus is an important addition to the field. Prior to publication the authors should address the following:

– The authors state that "most genetic variation in gene expression arises from trans-acting variants…" and cite several studies from model organisms that support this. However, my understanding is that this is not the case in human studies. The authors should expand on their explanation as to why they haven't been found in humans, beyond the fact that they can occur anywhere in the genome.

– The authors refer to the poor correlation between mRNA and protein levels, but should mention the issues identified with this comparison in Csardi et al., 2015 https://pubmed.ncbi.nlm.nih.gov/25950722/

– Figure 1 states the cells were grown in YNB + glutamate. Why was this media used for the study?

– Figure 3—figure supplement 3 aims to show the heritability of the phenotype of sorted cells. This would be more convincing if scatter plots were presented that show that after the sorting there is no correlation between the green and red signal, or if there is, an explanation as to why.

– It would be easier to read the paper if after the method has been introduced the text referred to mRNA and protein expression rather than the color of the reporter.

– The authors refer to the protein QTL as "post-transcriptional", but I think that term makes one think of mRNA stability, which is not what is measured. Perhaps "translational control" would be more correct and clearer.

– What is the rationale for showing δ-allele frequencies in Figure 4A? Showing LOD scores in this figure would make more sense to me for reporting QTL.

– It is not intuitive to me that δ-allele frequencies correspond to effect sizes and this should be more clearly explained.

– It is not clear to me if there is any compensation used in the FACS analysis. Is there any correlation between the green and red channels when controls containing only green or only red are used?

– Why is a loess regression used to correct for cell size? Wouldn't dividing by FSC be simpler and have the desired effect of normalizing for cell size?

Reviewer #2:

In this work, the authors used a novel approach to simultaneously measure mRNA and protein levels and identify trans-acting genetic variants affecting both or either of both. The authors present a fast and accurate novel strategy, taking advantage of a CRISPR strategy, and FACS analysis in a highly used yeast cross. Unfortunately, this work does not provide novel genetic, neither biological insights and conclusions are similar to previous findings. I would recommend the authors try to extend their work to a higher number of genes/environments and obtained novel biological insights that could explain how trans-acting factors, including post-transcriptional and post-translation modifications, impact mRNA, protein and traits. Furthermore, a time course would be interesting to analyse and determine how trans-acting variants affect mRNA and protein levels over time and whether they correlate or not.

Reviewer #3:

In this manuscript, Brion Lutz and Albert detail the simultaneous mapping of trans-acting QTLs influencing mRNA production and steady-state protein level differences between yeast strains BY4741 and RM-11 for ten genes. While much work has previously been done evaluating mRNA-QTLs in this system and others, the simultaneous comparison of transcription and protein QTLs, even for a relatively small set of genes, is significant and timely. The authors used a clever experimental system that converts transcription rates of test genes into mCherry expression by CRISPR activation. Notably, the authors find most QTLs affect protein levels, but not mRNA levels, and that mRNA-QTLs do not always have the same effects on protein levels. They also report genome-wide comparisons of a YAK1 kinase allele-swap on steady-state protein and mRNA levels. Overall, the manuscript describes important results that suggest more study of pQTLs is needed to better model the impact of transcription regulatory variation. While generally solid, the authors should further evaluate the effects of the mCherry plateau and examine protein-protein interactions for each of the ten genes to evaluate how these might contribute to the disparities between RNA-QTLs and protein-QTLs. They are also missing important citations that should be included for scholarly accuracy. Numbered issues (chronological):

1) Introduction: the authors should include Emerson et al., 2010 for yeast, and references of similar work in Drosophila, including McManus et al., 2010; Coolon et al., 2014 and Huang et al., 2015 and potentially others.

2) Introduction paragraph three: Cenik et al., 2015 also used ribosome profiling and mass spectrometry to examine post-transcriptional variation amont human LCLs and should be cited.

3) One caveat to the experimental approach is the plateau in mCherry measurements at high transcription rates. The authors argue that this plateau does not affect most genes, by comparing qPCR signal from inducible GFP and ACT1. However, this seems problematic because the PCR efficiency of GFP and ACT1 may not be identical. Thus it's possible the mRNA plateau occurs at a lower level. If this were the case, one would expect to see fewer mRNA-QTLs for highly expressed genes than for low-expression genes. Is there any relationship between expression levels (RNA-seq) and number of mRNA-QTLs among the 10 genes tested? If high mRNA genes are artifactually missing mRNA-QTLs, it's possible more pQTLs also affect mRNA levels.

4) A related complication of the assay system is that the tested genes do not have native 3' UTRs or cleavage and polyadenylation sites (CPS). The "strength" of CPS, has an important impact on mRNA levels and may influence both mRNA stability and transcription (See Shalem et al. PMID: 25875337). The 3' UTR issue should be discussed.

5) "A majority of the loci corresponded to protein-QTLs that did not overlap an mRNA-QTL". Were these non-matching QTLs more common in genes with high mRNA levels (i.e. could this reflect the mCherry plateau)?

6) Figure 5 shows variation among the number of pQTLs and mRNA-QTLs for the 10 studied genes. In the Discussion, the authors note that some p-QTLs could result by changes in protein complex members. Is there any relationship between the number of pQTLs for genes and the number of protein-protein interactions each gene has?

7) The YAK1 mutation was identified as altering protein (but not mRNA) levels of ARO8, BMH2 and GPD1. The genome-wide RNA-seq and Mass-spec comparison of YAK1 alleles appears to only show this affect for GPD1. Were the other genes also significantly altered in mRNA or protein levels in this orthogonal experiment?

8) The paper ends with the suggestion that protein abundance is under more complex genetic control than mRNA abundance. While this seems very likely in general (before the results presented in this paper) due to protein turnover and post-translational modifications, I think the authors should reiterate at the end of the paper that this is for trans-QTLs specifically. I expect that cis-QTLs have more consistent influences on mRNA and protein levels.
