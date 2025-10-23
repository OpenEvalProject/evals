# Peer review - Round 1

Editors:
- María Mercedes Zambrano, CorpoGen Colombia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.59726.sa1](https://doi.org/10.7554/eLife.59726.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This work offers an innovative approach that combines computational analysis with experimental studies to explore the production of the antibiotic phenazine by bacteria in natural environments. In addition to detecting microorganisms potentially useful in agricultural applications, this approach can also be extended to study other ecologically relevant microbial genes and properties.

Decision letter after peer review:

Thank you for submitting your article "Global landscape of phenazine biosynthesis reveals species-specific colonization patterns in soils and crop microbiomes" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Gisela Storz as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

Phenazines are natural antibiotics produced by bacteria, found mainly in soils and in the plant rhizosphere, that can also have beneficial effects on crops. However, the complexity of the plant-associated microbiome and the difficulty to culture microorganisms frustrate the identification of phenazine producers that might be relevant to crop health. In this elegant and well-designed work, Dar et al. explore the potential of phenazine production in natural environments using an innovative shotgun-metagenomics approach that is then validated experimentally. They first devised a computational procedure to measure phenazine producing bacteria, which was validated in silico and then used to provide a global view of phenazine biosynthesis and degradation by analyzing >800 soil and plant-associated metagenomes. Based on their biogeographical metagenomic analysis they identified an abundant yet less studied phenazine-producing bacterium and proceeded to characterize its interaction with a plant host of agricultural importance. This study not only increases our appreciation of phenazine biosynthesis and biodegradation in the environment but also provides novel tools for exploring specific genes and plant-microbe associations of agricultural potential.

Essential revisions:

1) The authors make claims about horizontal gene transfer of phenazine biosynthetic operons between phyla. While these seem well-supported overall, there are a number of things unclear about the phylogenetic analysis:

a) which tree reconstruction algorithm was used? The paper refers to MUSCLE, but as far as I know this is a multiple-sequence alignment algorithm, not an algorithm for phylogenetic tree reconstruction.

b) How strong is the bootstrap support for the main branches in the tree?

c) The authors use a concatenated alignment. Have the authors checked whether the individual gene trees are congruent, to exclude e.g. recombination of phenazine operons during evolution?

2) Reference databases are used to map metagenomic reads to and thus assess the frequency of phz producers across the bacterial fraction of microbial communities. The overall approach appears sound, although I wonder how it deals with ambiguous mapping (reads that can map equally well to two or more reference sequences), as this is not explicitly explained in the paper. When mentioning that 'reads that mapped with less than 80% identity', it is also not clear whether this indicates amino acid sequence identity or nucleotide sequence identity. Also, how was this threshold determined to be optimal in terms of specificity vs. sensitivity? Finally, are there any clades of uncultivated microbes with phenazine biosynthetic capabilities that the approach could be missing?

3) For the computational analysis, why were 25 genes used from the ubiquitous single copy gene set? Does the estimate of 'total bacteria' change if you do 10 or 40? Do differences in average genome lengths alter this calculation, and is this something you need to worry about? How does your work compare to other approaches assessing gene abundances per bacteria in metagenomic samples, such as MicrobeCensus?

4) The abundance statistic described in Figure 2A normalizes phz+ genes to total-bacterial score or Reads Per Kilobase levels, a method analogous to the widely used RPKM metric used to measure gene expression which has certain pitfalls (https://rnajournal.cshlp.org/content/early/2020/04/13/rna.074922.120.abstract). The assumption that the RPKM or here, RPK, values are normalized and therefore comparable across multiple samples can be misleading as RPK represents the abundance of the DNA fragment from a population of sequenced DNA fragments. This population represents distinct composition and titer of microbiota that can be unique to different sets of samples (e.g. citrus or maize rhizosphere). I would like the authors to clarify how the RPK statistic proposed here addresses this issue.

5) The validation using simulated metagenomes is set up well but could be explained in more detail. To more clearly show that the approach is able to accurately map frequencies of phenazine operons that are not themselves present in the phz reference database the authors may consider doing a cross-validation analysis by leaving the sequences that are spiked into the simulated metagenome out of the reference dataset. This would allow quantification of how similar a sequence needs to be to one of the reference sequences to still be accurately identified with the mapping procedure. In 2B why is the relationship not linear between estimated and known phz+?

6) For the field validation, can you show a 'predicted' vs. 'experimental' phz plot? You show estimates in 3A, how do these relate to your culture-based approach? This is a key point of your study and needs a figure to demonstrate the validation.

7) Since the vast majority of the metagenome sample are from public data, did the authors consider the impact of DNA quality and variability in sample biomass (https://pubmed.ncbi.nlm.nih.gov/25329041/)? Were any of the public samples from a longitudinal study where the impact of environmental conditions on the distribution of phz+ genes could be explored?

8) Although most of the reads mapped to representative genomes for pseudomonads and Streptomyces, did the authors find any off-target mapping for translated DNA reads to proteins from other gene families? Short reads can represent domains shared by phi+ genes and other gene families and give rise to cross-mapping and over or underestimation. This could possibly bias the mapping counts for phi+ genes.

9) What is the intuition for why phosphate limitation turns on phenazine production?

10) Given that the authors did not include any transcriptomics experiments, there is no direct indication of what proportion of the microbes represented by the sequenced DNA fragments are transcriptionally and metabolically active in each sample. This limitation should be mentioned in the manuscript.
