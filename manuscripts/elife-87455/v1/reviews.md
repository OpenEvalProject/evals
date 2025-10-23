# Peer review - Round 1

Editors:
- Wenfeng Qian, Chinese Academy of Sciences China

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.87455.3.sa0](https://doi.org/10.7554/eLife.87455.3.sa0)

This study offers important insights into the generation and maintenance of monosomic yeast lines and is, to our knowledge, the first to evaluate gene expression in yeast monosomies. The research introduces an innovative method to assess epistasis between genes on the same chromosome, providing solid evidence for positive epistatic interactions affecting fitness. Although the authors have substantially improved the methodology and interpretation during revision, questions regarding the interpretation of the transcriptome data have not been completely addressed.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87455.3.sa1](https://doi.org/10.7554/eLife.87455.3.sa1)

The study by Korona and colleagues presents a rigorous experimental strategy for generating and maintaining a nearly complete set of monosomic yeast lines, thereby establishing a new standard for studying monosomes. Their careful approach in generating and handling monosome yeast lines, coupled with their use of high-throughput DNA sequencing and RNA sequencing, addresses concerns related to genomic instability and is commendable. However, I would like to express my concerns regarding the second part of the study, particularly the calculation of epistasis and the conclusion that vast positive epistatic effects have been observed. I believe that the conclusion of positive epistasis for fitness might be premature due to potential errors in estimating the expected fitness.

The method used to calculate fitness expectation (1 + sum(di), where di = rDRi - 1) may be inappropriate. The logarithm transformation mentioned by the authors is designed to transform the exponential growth curve into a linear relation for estimating doubling rate, and thus the fitness expectation should be calculated as the product of rDRi values. As an illustration, if gene A exhibits a 20% reduction in fitness when halved (A/-) and gene B exhibits a 30% reduction (B/-), the expected fitness of A/- B/- should be 56%, rather than the 50% estimated in the study. In other words, the formula used by the authors could underestimate the fitness expectation.

This issue is evident in Figure 2b, where negative values were obtained due to the use of an incorrect formula for estimating fitness expectations. It is worth noting that Figure 2a shows rDR values around one, indicating that no further logarithmic transformation was applied.

While widespread positive epistasis in yeast has been reported by other studies (e.g., doi: 10.1038/ng.524, but not to the extent reported in this study), the conclusion of the current study might not be sufficiently supported. I recommend that the authors revisit their calculation methods to provide a more convincing conclusion on the presence of positive epistasis for fitness in their dataset. Overall, I appreciate the authors' efforts in this study but believe that addressing these concerns is essential for strengthening the validity of their findings.

Comments on revised version:

The authors have adequately addressed all my previous concerns during revision.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87455.3.sa2](https://doi.org/10.7554/eLife.87455.3.sa2)

This study examines monosomies in yeast in comparison to synthetic lethals resulting from combinations of heterozygous gene deletions that individually have a detrimental effect. The survival of monosomies, albeit with detrimental growth defects, is interpreted as positive epistasis for fitness. Gene expression was examined in monosomies in an attempt to gain insight into why monosomies can survive when multiple heterozygous deletions on the respective chromosome do not. In the RNAseq experiments, many genes were interpreted to be increased in expression and some were interpreted as reduced. Those with the apparent strongest increase were the subunits of the ribosome and those with the apparent strongest decreases were subunits of the proteasome.

The initiation and interpretation of the results were apparently performed in a vacuum of a century of work on genomic balance. Classical work in the flowering plant Datura and in Drosophila found that changes in chromosomal dosage would modulate phenotypes in a dosage sensitive manner (for references see Birchler and Veitia, 2021, Cytogenetics and Genome Research 161: 529-550). In terms of molecular studies, the most common modulation across the genome for monosomies is an upregulation (Guo and Birchler, Science 266: 1999-2002; Shi et al. 2021, The Plant Cell 33: 917-939).

It was also apparently performed in a vacuum of results of evolutionary genomics that indicate the classes of genes for which dosage causes fitness consequences. It was from yeast genomics that it was realized that there is a difference in the fate of duplicate genes that are members of molecular complexes following whole genome duplications (WGD) versus small segmental duplications (SSD) with longer retention times from WGD than other genes and an underrepresentation in small scale duplications (e.g. Papp et al. 2003, Nature 424: 194-197; Hakes et al 2007, Genome Biol 8: R209). This pattern arises from negative fitness consequences of deletion of some but not all members of a complex after WGD or the overexpression of individual subunits after SSD (Defoort et al., 2019 Genome Biol Evol 11: 2292-2305; Shi et al., 2020, Mol Biol Evol 37: 2394-2413). In order for this pattern to occur, there must be a reasonably close relationship between mRNA and the respective protein levels. This pattern of retention and underrepresentation has been found throughout eukaryotes (e.g. Tasdighian et al 2017, Plant Cell 29: 2766-2785) indicating that yeast is not an outlier in its behavior.

In the present yeast study, not only are there apparent increases for ribosomal subunits but also for many genes in the GAAC pathway, the NCR pathway, and Msn2p. The word "apparent" is used because RNAseq studies can only determine relative changes in gene expression (Loven et al., 2012, Cell 151: 476-482). Because aneuploidy can change the transcriptome size in general (Yang et al., 2021, The Plant Cell 33: 1016-1041), it is possible and maybe probable that this occurs in yeast monosomies as well. If there is an increase in the general transcriptome size, then there might not be as much reduction of the proteosome subunits as claimed and the increases might be somewhat less than indicated.

Indeed, the authors claim that there is an increased cell volume in the monosomies. Given that cell volume correlates very well with the total transcriptome size (Loven et al., 2012, Cell 151: 476-482; Sun et al 2020, Current Biol 30: 1217-1230; Swaffer et al., 2023, Cell 186: 5254-5268), it could well be that there is an increased transcriptome size in the monosomies. Thus, the interpretation of the relative changes from RNAseq is compromised.

It should be noted that contrary to the claims of the cited paper of Torres et al 2007 (Science 317: 916-924), a reanalysis of the data indicated that yeast disomies have many modulated genes in trans with downregulated genes being more common (Hou et al, 2018, PNAS 115: E11321-E11330). The claim of Torres et al that there are no global modulations in trans is counter to the knowledge that transcription factors are typically dosage sensitive and have multiple targets across the genome. The inverse effect trend is also true of maize disomies (Yang et al., 2021, The Plant Cell 33: 1016-1041), maize trisomies (Shi et al., 2021), Arabidopsis trisomies (Hou et al. 2018), Drosophila trisomies (Sun et al. 2013, PNAS 110: 7383-7388; Sun et al., 2013, PNAS 110: 16514-16519; Zhang et al., 2021, Scientific Reports 11: 19679; Zhang et al., genes 12: 1606) and human trisomies (Zhang et al., 2024, genes 15: 637). Taken as a whole it would seem to suggest that there are many inverse relationships of global gene expression with chromosomal dosage in both yeast disomies and monosomies.

In a similar vein, the authors cite Muenzner et al 2024, Nature 630 149-157 that there is an attenuation of protein levels from aneuploid chromosomes while the mRNA levels correlate with gene dosage. This interpretation also seems to have been made in a vacuum of the evolutionary genomics data noted above and there was no consideration of transcriptome size change in the aneuploids. Also, Muenzner et al make the remarkable suggestion that there is degradation of overproduced proteins from hyperploidy, but for monosomies there is greater degradation of the proteins from the remainder of the genome.

To clarify the claims of this study, it would be informative to produce distributions of the various ratios of individual gene expression in monosomy versus diploid as performed by Hou et al. 2018. This will better express the trends of up and down regulation across the genome and whether there are any genes on the varied chromosome that are dosage compensated. The authors claim in the Abstract that "There is no evidence of increased (compensatory) gene expression on the monosomic chromosomes", but then note after describing the increased cell volume of monosomies that this observation likely signals an increased transcriptome size: "Indeed, one explanation for the observed epistasis for viability could be an ample overproduction of all transcripts, so that even those halved by monosomy are sufficiently abundant". It is not clear to this reviewer what conclusions can be made from this work other than the empirical observation that monosomy does not reflect the cumulative effect of multiple haplo-insufficiencies of individual heterozygous deletions and that there are some RELATIVE changes in gene expression, but it is unclear what the ABSOLUTE PER CELL expression is across the whole genome. Clarifying this issue would be important for understanding the nature of any epistasis and fitness consequences.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87455.3.sa3](https://doi.org/10.7554/eLife.87455.3.sa3)

The current study examined 13 monosomic yeast strains that lost different individual chromosomes. By comparing the fitness of monosomic strains and several heterozygous deletion strains, the authors observed strong positive epistasis for fitness. The transcriptomes of monosomic strains indicated that general gene-dose compensation is not the reason for fitness gains. On the other hand, gene expression of ribosomal proteins was up-regulated and proteasome subunit expression was down-regulated in all tested monosomic strains. The authors speculated that overexpression in combination with decreased degradation of the insufficient proteins might explain the positive epistasis observed in monosomic strains. This study investigates an important biological question and has some interesting results. However, I have some reservations about the data interpretations listed below.

(1) In Figure 3b (and line 179), the authors stated that those haploinsufficient genes were not transcribed at elevated rates, but almost half of them are in reddish colors (indicating that the expression is higher than 1-fold). Obviously, many haploinsufficient genes are up-regulated in monosomic strains. What the data really show is that the level of overexpression is not correlated with the fitness effect of the deletion (since all the p values are not significant). The authors need to correct their conclusions.

(2) Why are some monosomic strains removed from the transcriptomics analysis, especially when the chromosome IV and XV strains show very strong positive epistasis? The authors need to provide an explanation here.

(3) The authors stated that diploidy observed in chromosome VII and XIII strains were due to endoreplication after losing the marked chromosomes (lines 97 and 117). Isn't chromosome missegregation an equally possible explanation? Since monosomic cells are generated by chromosome missegregation during mitosis, another chromosome missegregation event may occur to rescue the fitness (or viability) of monosomic cells in these strains.

Comments for the revised version:

The authors have addressed all my previous concerns and I have no further questions.
