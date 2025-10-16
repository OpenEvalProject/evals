# Peer review - Round 1

Reviewers:
- Daniel Zilberman, University of California, Berkeley , United States

## Review text

DOI: [10.7554/eLife.20777.055](https://doi.org/10.7554/eLife.20777.055)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Population scale mapping of transposable element diversity reveals links to gene regulation and epigenomic variation" for consideration by eLife. Your article has been favorably evaluated by Detlef Weigel (Senior Editor) and two reviewers, one of whom is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal his identity: Jeffrey Ross-Ibarra (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Stuart et al. present a compelling and comprehensive description of TE variation in Arabidopsis thaliana, highlighting the influence of TE polymorphism on expression of nearby genes and methylation of nearby regions. This paper persuasively argues that TE variation is the genetic basis for most DNA methylation polymorphisms and makes an important contribution to our understanding of the genomic impacts of TEs. However, the reviewers raised several points that should be addressed before publication. Most generally, this manuscript focuses a bit too much on the process and not enough on the biology. Dense statistical descriptions that will be difficult to understand for most readers are common, yet some results are explained either very broadly or not at all, and some important biological issues are ignored. A greater emphasis on biological meaning would substantially improve this paper.

Essential revisions:

1) The authors report that TEPID identified 300-500 insertions and 1000-1500 deletions per ecotype relative to Col. However, the overall number of insertions identified was 15,007 vs. 8,088 deletions. The reason that more deletions than insertions were identified per ecotype but fewer overall is that some of the deletions are present in nearly all or all tested ecotypes. Because this analysis is relative – insertions are both insertions in other ecotypes and deletions in Col, whereas deletions are deletions in other ecotypes and insertions in Col, such 'fixed deletions' are just insertion in Col. The authors get to this issue later in the analysis, but they don't explain the asymmetry. Why aren't there 'fixed insertions' relative to Col – meaning deletion in Col? Is TEPID unable to identify such events, or is there a biological meaning to this? An explanation would be very helpful.

2) The authors mention that TE insertions and deletions are both biased for pericentric regions, without discussing the observation that deletions are far more biased and what this likely means for actual TE insertion biases. The data strongly suggest that TE insertions are largely random, but are eliminated by selection from the chromosome arms. However, reading this paper, one could easily get the impression that TE insertion and deletion location biases are similar (which is stated in the Results), when they are actually not similar at all except in the most general sense.

3) C-DMRs and CG-DMRs are introduced without any description of the underlying biology (gene body vs. TE methylation; C-methylation mostly in TEs, CG mostly in genes) that would help to make sense of the different correlations of these DMRs with TE insertions. Gene body methylation doesn't even come up until the next-to-last Results section, and it's not explained there either. A keen reader might notice that CG-DMR distribution tracks genes, but to most the biological meaning of the presented analyses with respect to the two types of DMRs will be very obscure.

4) There is some concern about the inferences made about gene expression, as it seems that TE genes are not removed from the gene models used in the differential expression calls. Separating the impact of TEs inserting into TEs from the effect of TEs inserting into host genes would strengthen the argument that TEs are associated with extreme expression changes.

5) It may be useful to including some information about expectations of TE allele frequency in Arabidopsis, for example based on Helitron measurements by Hollister and Gaut (2007) (http://mbe.oxfordjournals.org/content/24/11/2515.long) and Gypsy measurements by Lockton and Gaut (2010) (http://bmcevolbiol.biomedcentral.com/articles/10.1186/1471-2148-10-10).

6) As any definition of a rare allele is somewhat arbitrary, the paper should be clearer about how TE variants are categorized into rare and common. Probably due to additions in the text, the definition of common (>3% MAF) comes in the subsection “Relationship between TE variants and single nucleotide polymorphisms”, long after Figure 2 is introduced. Can the common/rare definition either be added to the Figure 2 legend, or introduced when polarization is described? Similarly, it seems that the translation of MAF cutoffs to numbers of individuals are not consistent throughout the paper. While the definition of MAF cutoff states this is in >7 accessions, this doesn't obviously make sense with 217 accessions (shouldn't it be >=7?). Also, it seems that filtering reduces the number of accessions to 184, where 3% would be >5. Since there are so many low frequency TEs (Figure 2—figure supplement 2), small shifts in this definition might change conclusions qualitatively.

7) Gene At2G01360 used as an example in Figure 5 is highlighted in Figure 2 of Freeling et al. (2008) (http://genome.cshlp.org/content/18/12/1924.full) as transposing to this position in Arabidopsis by an unknown mechanism. Please comment about the possible relationship between this observation and the presence of a polymorphic TE within Arabidopsis.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "Population scale mapping of transposable element diversity reveals links to gene regulation and epigenomic variation" for consideration by eLife. Your article has been favorably evaluated by Detlef Weigel (Senior Editor) and four reviewers, one of whom is a member of our Board of Reviewing Editors. The following individual involved in review of your submission has agreed to reveal their identity: Magnus Nordborg (Reviewer #2).

Our decision has been reached after extensive consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife in its present form. We would, however, welcome a resubmission that substantively addresses reviewer concerns. Senior Editor Detlef Weigel suggests that you contact him directly if you have questions regarding the decision and recommendations. Magnus Nordborg is also happy to discuss his comments.

Although the reviewers found the subject of the manuscript interesting and clearly presented, three major deficiencies were identified:

1) The paper appears to conflate transposition with TE content variation, which are different things. TE variation – the actually measured feature – can occur through new insertions, but also through deletion of old copies. Given the large number of ecotype genomes and an understanding of the underlying phylogeny, new insertions could be distinguished from deletions of ancestral TEs in most cases. This would allow new insertion evens to be considered separately from deletions.

2) As explained by Magnus Nordborg in his review, the use of LD to measure TE insertion age is questionable and likely produces inaccurate measurements. This might explain why the conclusion reached in this manuscript that even recent TE insertions are biased for pericentric heterochromatin is inconsistent with studies of individual plant TEs that do not show such a bias. A more appropriate estimate of TE insertion age may be through measurement of allele frequency. Because estimated TE age is used in analyses throughout the manuscript, a robust measure is essential.

3) The section on seed and gamete methylation contains numerous questionable statements and analyses. Statements linking demethylation in pollen to imprinting are very confusing, because imprinting is associated with demethylation in the female gametophyte. The correlations with TEs demethylated (more accurately hypomethylated) in the CHH context in sperm ignore the global nature of this phenomenon, which affects most heterochromatic TEs. The small RNA analysis rests on the unwarranted assumption that the small RNAs are produced in the endosperm. The paper from which the small RNA data are derived makes a strong case that the small RNAs are derived from the maternal seed coat, which would provide a trivial explanation for the observation that TEs absent in the maternal genome have lower levels of small RNA in hybrid seeds. The most promising result – the correlation between TE content and methylation in Col x Cvi hybrids – didn't hold up in Col x Ler hybrids.

We would welcome a resubmission that clearly identifies TE insertions, provides a robust measure of the false positive and false negative rates (please see Magnus Nordborg's review below), provides a robust measure of TE age, and ideally deepens the analysis of the correlations between TE variation, DNA methylation polymorphism, and gene expression as suggested by the reviewers.

Reviewer #2 (Magnus Nordborg):

This is a very clear and interesting paper. It is one of the first genome-wide descriptions of TE polymorphism (there will be more…), and, although the conclusions are a bit limited, it should be of broad interest. Most importantly, it really suggests strongly that methylation variation is mostly genetic.

I do have a few substantive concerns, however. The first concerns data quality, which has been a major reason these types of studies have not done before. Calling TE polymorphisms from short-read data is not trivial. What is done here is sensible, but I would still like to have some idea of error rates and biases. Using simulations (subsection “Computational identification of TE presence/absence variation”) is not QC – it is at best debugging of software. What is needed is comparison with real data, preferably a "gold standard". The obvious choice is the PacBio Ler assembly, and it is used here, but it seems to me it is used in the wrong direction. The TE polymorphisms identified in the short-read data are confirmed in the PacBio data, rather than the other way around. It is the usual false-positive / false-negative issue that plagues all these data. What is done shows that the identified polymorphism are reliable, but it tells us nothing about what we don't see. Which leads to biases of all kinds. Why not do the right thing? And if there is a good reason for not doing the right thing, please justify this, and say a few words about how why the inevitable biases do not affect your results.

My second concern is the entire missing heritability section (Figure 2), which I think is based on two misunderstandings, one of linkage disequilibrium (LD), one of the nature of "missing heritability". Take LD first. It is theoretically impossible for TEs variants to show a different LD behavior than SNPs unless they are due to repeat mutations (which have to be very frequent indeed to affect LD). As long as identity in state = identity by descent, it doesn't matter how mutations arise. Of course it is possible that some of the TE indels could be non-unique, but there is no evidence for this in this paper (you could look for it: does the same insertion occur on unrelated haplotypes?). I'm fairly convinced that the difference is r2 distributions you see are largely due to differences in the allele frequency. To confirm this, compare r2 between TEs and flanking SNPs to r2 between a SNP and flanking SNPs after making sure that the polymorphism being tested has the same derived allele frequency. This can be done by binning. I think you will see that there is no difference. And if you do see a difference, it is probably due to some other artifact (genotyping error?), because, as I said, it is theoretically impossible for there to be a difference (unless repeat mutations are very different, selection is strong, etc.).

Don't say things like "this variant was classified as a young TE insertion, as it is not in linkage disequilibrium with surrounding SNP" – the younger a mutation is, the stronger the LD (because there has been no time for recombination). Sure, r2 will be low, but this is a trivial consequence of the definition of r2.

As I see it, the relevance of TEs in the "missing heritability" debate is simply that they could be an important source of rare deleterious alleles. Such alleles, regardless of whether they are TEs, SNPs, or CNVs, will have the property that they can be mapped in pedigrees in which they segregate, but will individually explain very little of the population variation and thus cannot be mapped using GWAS. This has nothing to do with LD: it is a simple consequence of their frequency. LD is a red herring in this context. I would get rid of Figure 2. and simply mention this in the Discussion.

But speaking of rare variants, you seem to argue against TEs having an effect, at least on transcript abundance, although you note that perhaps the rare variants are the ones that matter (subsection “TE variants affect gene expression”, first paragraph). Did you try testing this in aggregate (analogously to what human geneticists do to establish that rare alleles matter)? Rather than carrying out a SNP-by-SNP test, which clearly doesn't work when frequencies are less than 3% (is that 2 alleles?), ask whether these rare TEs are, in aggregate, more likely to show extreme phenotypes than two (or three, or whatever the right number is) randomly chosen individuals? You could calculate some kind of two-tailed rank statistic, and simply ask whether they are more likely to be extreme (feel free to contact me if this is not clear).

As I said from the outset, the strength of this paper is confirming that a large fraction of DMRs are due to TEs. This could be made even stronger:

A) When estimating the fraction based on published DMR data (subsection “TE variants drive DNA methylation differences between accessions”, end of first paragraph), why not distinguish between types of DMRs?

B) When looking for DMR around identified TEs (subsection “TE variants drive DNA methylation differences between accessions”, first paragraph), why not using random regions as control?

C) The correlations between TE and methylation are nice, but is there any clear example of strong methylation without a TE? This would be of obvious interest.

D) have you considered trans-acting TEs? Even if there is no TE variant in cis, there could be one in trans. How many more DMRs can you explain if you consider nearby TEs, variable or not?

Trans-acting TEs could also be important when interpreting the crosses, but I'm guessing other reviewers will comment more extensively on that.

Reviewer #3:

This is a very nice analysis of transposon activity in Arabidopsis accessions and will serve as a platform for similar analyses in more complex genomes.

Reviewer #4:

The manuscript by Stuart and colleagues describes the development of a software pipeline for detection of variations in transposons insertions (TEPID). The authors applied this pipeline to the available genomic sequences of over 200 Arabidopsis accessions. They verified efficiency and accuracy of the TEPID and estimated ages of transposons based on linkage disequilibrium between transposon and flanking sequences. In addition, they assessed the degree of transposon derived regulation of transcription of the neighbouring genes, which turned out to be surprisingly limited and only two experimentally verified examples could illustrate TE derived transcriptional suppression or activation. Interestingly, suppression of transcription of a gene encoding a LRR protein seems to cause a change in the level of resistance to a bacterial pathogen when accessions with or without the transposon insertion were compared. The authors also studied the influence of transposon insertions on the local variation in DNA methylation claiming that especially old insertions affect variation in DNA methylation. Finally, in reciprocal inter-accession crosses they examined the epigenetic interaction between accessions differing in the distribution of particular transposable elements, comparing loci with presence of corresponding transposons in one or both accessions.

This is an interesting manuscript.
