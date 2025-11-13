# Allele-specific gene expression can underlie altered transcript abundance in zebrafish mutants

## Authors

- Richard J White<sup>1</sup> ([ORCID: 0000-0003-1842-412X](https://orcid.org/0000-0003-1842-412X))
- Eirinn Mackay<sup>2</sup> ([ORCID: 0000-0003-1436-2259](https://orcid.org/0000-0003-1436-2259))
- Stephen W Wilson<sup>2</sup> ([ORCID: 0000-0002-8557-5940](https://orcid.org/0000-0002-8557-5940))
- Elisabeth M Busch-Nentwich<sup>1</sup> ([ORCID: 0000-0001-6450-744X](https://orcid.org/0000-0001-6450-744X)) †

### Affiliations

1. Cambridge Institute of Therapeutic Immunology & Infectious Disease (CITIID), Department of Medicine, University of Cambridge Cambridge United Kingdom ([ROR:013meh722](https://ror.org/013meh722))
2. Department of Cell and Developmental Biology, University College London London United Kingdom ([ROR:02jx3x895](https://ror.org/02jx3x895))
3. School of Biological and Behavioural Sciences, Faculty of Science and Engineering, Queen Mary University of London London United Kingdom ([ROR:026zzn846](https://ror.org/026zzn846))

† Corresponding author

## Abstract

In model organisms, RNA-sequencing (RNA-seq) is frequently used to assess the effect of genetic mutations on cellular and developmental processes. Typically, animals heterozygous for a mutation are crossed to produce offspring with different genotypes. Resultant embryos are grouped by genotype to compare homozygous mutant embryos to heterozygous and wild-type siblings. Genes that are differentially expressed between the groups are assumed to reveal insights into the pathways affected by the mutation. Here we show that in zebrafish, differentially expressed genes are often over-represented on the same chromosome as the mutation due to different levels of expression of alleles from different genetic backgrounds. Using an incross of haplotype-resolved wild-type fish, we found evidence of widespread allele-specific expression, which appears as differential expression when comparing embryos homozygous for a region of the genome to their siblings. When analysing mutant transcriptomes, this means that the differential expression of genes on the same chromosome as a mutation of interest may not be caused by that mutation. Typically, the genomic location of a differentially expressed gene is not considered when interpreting its importance with respect to the phenotype. This could lead to pathways being erroneously implicated or overlooked due to the noise of spurious differentially expressed genes on the same chromosome as the mutation. These observations have implications for the interpretation of RNA-seq experiments involving outbred animals and non-inbred model organisms.

## Introduction

Large-scale genetic screens to identify gene function by randomly introducing mutations have been a staple of zebrafish genetics for several decades (Driever et al., 1996; Haffter et al., 1996; Kettleborough et al., 2013). The advent of RNA-sequencing (RNA-seq) has enabled investigators to estimate the location of such mutations in the genome, while also providing information regarding gene expression levels and affected cellular pathways in the mutants. The bioinformatics pipelines which process RNA-seq data to generate gene expression information focus on transcript abundance, differential splicing, and gene set enrichments, and, in general, genomic location is not considered when assessing genes that are differentially expressed (DE) in a mutant context. Here, we report that physical location can impact a gene’s likelihood of being DE in mutant zebrafish.

In the typical protocol for introducing random point mutations, male zebrafish from a laboratory wild-type strain are treated with N-ethyl-N-nitrosourea (ENU) to mutagenise sperm (Kettleborough et al., 2011; Mullins et al., 1994). The mutagenised fish (G0) are mated with wild-type females to produce F1 offspring, each heterozygous at random novel mutation sites. F1 fish are outcrossed with wild types to produce clutches of F2 offspring, which are subsequently incrossed to produce F3 embryos. The F3 clutches contain the novel mutations in Mendelian ratios, and in a forward genetics approach are screened for recessive phenotypes of interest which appear in approximately 25% of embryos (Mullins et al., 1994). These embryos are referred to as ‘mutants’ whereas those without phenotypes are ‘siblings’.

Mutant embryos are homozygous for a novel allele (the ‘causative mutation’) and due to genetic linkage, they are likely to be homozygous for alleles physically nearby on the chromosome. The location encompassing the causative mutation therefore lies in a region which is highly homozygous in mutants, yet heterozygous in siblings. This is referred to as linkage disequilibrium (LD). The region of high LD can be mapped using high-throughput sequencing and bioinformatics pipelines (Mackay and Schulte-Merker, 2014; Minevich et al., 2012; Obholzer et al., 2012) whereas prior efforts involved painstaking genotyping of simple sequence length polymorphisms and genome walks using bacterial or P1 artificial chromosome libraries or subsequently, microarrays (Stickney et al., 2002; Zhang et al., 1998).

All mapping processes rely on identification of polymorphic loci throughout the genome. Laboratory zebrafish strains have a high degree of intra-strain polymorphism (Guryev et al., 2006), but mapping is aided by the introduction of alleles from other strains. Thus, mutagenised males are often paired with females from a different strain. As a result, in a mapping cross, alleles in the mutants and siblings are inherited from two different strains. This remains true throughout the multiple generations that a mutant line is maintained in a laboratory.

In this study, we report that the highly polymorphic nature of zebrafish strains can lead to gene expression differences between mutant and sibling embryos through allele-specific expression (ASE). The effect of ASE is well documented across many species, and can be tissue- and condition-specific (Ayroles et al., 2009; Doss et al., 2005; Fu et al., 2009; Battle et al., 2017; Huang et al., 2015; Kim-Hellmuth et al., 2020; Storey et al., 2005). Here, this phenomenon manifests as a cluster of DE genes located near to the causative mutation site in many different unrelated mutant lines. The differential transcript levels of these local genes are likely due to expression differences between wild-type strains rather than altered transcription due to the mutation. We confirm the high prevalence of ASE in zebrafish in the SAT line which is derived from only two haplotypes. This observation has implications for researchers attempting to use differential expression to explain phenotypes of interest, not only in zebrafish, but also in other outbred model organisms, as these local genes may simply be a red herring.

## Results

### Differentially expressed genes are often enriched on the mutant chromosome

To map the causal mutations for a number of different mutants from forward genetic screens, we used RNA-seq and LD mapping, based on Cloudmap (Minevich et al., 2012). A representative LD mapping plot (taken from the mutant line u426) is shown in Figure 1. We observed a high degree of LD on chromosome 7 at approximately 22 Mbp, suggesting the phenotype-causing mutation is near this position. DESeq2 reported 209 genes as DE (adjusted p-value < 0.05) between mutants and siblings. Annotating the LD mapping plot with the position of these genes showed a cluster of DE genes near the LD mapping peak on chromosome 7. Indeed, we found 15 DE genes in an arbitrarily sized 20 Mbp window centred on the mapping peak at 22 Mbp, representing 7% of all DE genes. For comparison, a 20 Mbp window randomly sampled (1000 iterations) from the zebrafish genome contains approximately 1.4% of known genes.

![Figure 1.](https://cdn.elifesciences.org/articles/72825/elife-72825-fig1-v2.jpg)

**Figure 1.:** The plots for each of the 25 chromosomes shows the allele balance (proportion of reads containing the alternative allele) of each single nucleotide polymorphism (SNP) locus along with its physical position. The blue and orange lines are LOESS-smoothed averages of the data. The green line is the absolute difference of the mutant and sibling samples and is used to identify the region of highest LD. Vertical lines indicate the position of differentially expressed genes.

We then used a logistic regression model to examine the effect of LD on the probability of an individual gene being DE. A summary of each line and the regression results are presented in Table 1. Of nine mutant lines analysed (Supplementary file 1), seven samples showed a significant, positive effect of LD (Benjamini/Hochberg adjusted p-value < 0.05). To help visualise the effect of LD on DE probability, we calculated an odds ratio for each sample by comparing the DE probability at the site of maximum LD with the probability at a site of median LD. In the most extreme case (the sample nl14), the likelihood of finding a DE gene near to the mutation site was over 100-fold higher than the likelihood of finding one at a random other location in the genome.

**Table 1.**
 Summary of logistic regression results for RNA-sequencing (RNA-seq) analysed mutant lines.Causative mutation shows the gene and location of the mutation site in lines where this has been confirmed empirically, otherwise the location is estimated from linkage disequilibrium (LD) data. Significance column indicates adjusted p-value (***: < 0.001, **: < 0.01; *: < 0.05). Odds ratio compares DE likelihood at maximum LD versus site of median LD. The nearby genes column shows the number of DE genes lying within a 20 Mbp window centred on the mutation site, and the percentage of these genes out of the total DE genes. In-table citations: 1(Barlow et al., 2020), 2(Miesfeld et al., 2015), 3(Armant et al., 2016). nl14 line kindly provided by Alex Nechiporuk.


<table>
  <thead>
    <tr>
      <th>Allele</th>
      <th>Causative mutation</th>
      <th>DE genes/total</th>
      <th>Coefficient ± SEM</th>
      <th>Sig.</th>
      <th>Odds ratio</th>
      <th>Nearby genes (%)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>nl14</td>
      <td>lama1 unpublished(chr24, 41.6Mbp)</td>
      <td>12/31,664</td>
      <td>9.09 ± 1.56</td>
      <td>***</td>
      <td>118.5</td>
      <td>3 (25%)</td>
    </tr>
    <tr>
      <td>la0155771</td>
      <td>dmist (chr5, 19.9 Mbp)</td>
      <td>157/31,199</td>
      <td>6.84 ± 0.46</td>
      <td>***</td>
      <td>55.8</td>
      <td>23 (15%)</td>
    </tr>
    <tr>
      <td>u5051</td>
      <td>dmist (chr5, 19.9 Mbp)</td>
      <td>71/31,199</td>
      <td>8.72 ± 0.72</td>
      <td>***</td>
      <td>44.0</td>
      <td>13 (18%)</td>
    </tr>
    <tr>
      <td>u757</td>
      <td>Unpublished (chr23, 22 Mbp)</td>
      <td>33/31,199</td>
      <td>6.31 ± 2.13</td>
      <td>**</td>
      <td>7.8</td>
      <td>1 (3%)</td>
    </tr>
    <tr>
      <td>u534</td>
      <td>Not known (chr1, ~25 Mbp)</td>
      <td>87/31,664</td>
      <td>4.83 ± 1.05</td>
      <td>***</td>
      <td>5.4</td>
      <td>4 (5%)</td>
    </tr>
    <tr>
      <td>u426</td>
      <td>Not known (chr7, ~22 Mbp)</td>
      <td>209/31,664</td>
      <td>2.67 ± 0.48</td>
      <td>***</td>
      <td>5.3</td>
      <td>15 (7%)</td>
    </tr>
    <tr>
      <td>nl132</td>
      <td>yap1 (chr18, 37.2 Mbp)</td>
      <td>140/31,199</td>
      <td>2.58 ± 1.57</td>
      <td>–</td>
      <td>2.3</td>
      <td>4 (3%)</td>
    </tr>
    <tr>
      <td>sb553</td>
      <td>ache (chr 7, 26.0 Mbp)</td>
      <td>348/24,558</td>
      <td>3.77 ± 1.67</td>
      <td>*</td>
      <td>2.0</td>
      <td>14 (4%)</td>
    </tr>
    <tr>
      <td>u535</td>
      <td>Not known (chr13, ~25 Mbp)</td>
      <td>294/31,663</td>
      <td>0.35 ± 1.04</td>
      <td>–</td>
      <td>1.1</td>
      <td>4 (1%)</td>
    </tr>
  </tbody>
</table>

In parallel, we were analysing a separate catalogue of 3’ tag sequencing experiments of zebrafish mutant lines (115 experiments), most of which were generated and made available as part of the Zebrafish Mutation Project (Collins et al., 2015; Dooley et al., 2019; Kettleborough et al., 2013). These were analysed for differential expression, producing a large collection of DE gene lists. We noticed that, often, the mutant chromosome had a large proportion of the total number of DE genes in the experiment. For example, comparing mitfaw2/w2 embryos to siblings produces 116 DE genes, 48 of which are present on chromosome 6, which is the chromosome where mitfa is located (Figure 2A).

![Figure 2.](https://cdn.elifesciences.org/articles/72825/elife-72825-fig2-v2.jpg)

**Figure 2.:** (A) Ideogram showing the locations of the DE genes in a mitfaw2 incross. Circles represent DE genes and are coloured red if the gene is upregulated in the mutant embryos and blue if it is downregulated. (B) Distribution of the total number of DE genes in experiments according to whether there is an enrichment on the mutant chromosome (orange) or not (blue), plotted on a log10 scale. (C) Plot of normalised counts according to genotype in an intercross of two different sox10 alleles. Yellow = wild type (+/+), orange = sox10 t3 heterozygotes (t3/+), blue = sox10 baz1 heterozygotes (+/baz1), purple = sox10 t3, baz1 compound heterozygotes (t3/baz1). The schematic below the plot shows the chromosomes contributing to each genotype. Embryos that share the wild-type allele inherited from the baz1/+ parent (yellow chromosome) show higher expression levels.

To investigate this, we tested for chromosomes that had an enrichment of DE genes under the null hypothesis that they are randomly distributed across the genome. In all, 60 chromosomes from 37 lines had a statistically significant enrichment of the DE genes (binomial test, Bonferroni adjusted p < 0.05). Of these, 44 were on the chromosome carrying the mutation being investigated in the experiment (Supplementary file 2). Of the other 16, 7 had an enrichment on chromosome 9. This was driven by expression of γ-crystallin genes (Supplementary file 3), which are expressed in the lens and present in a cluster on chromosome 9 (Greiling et al., 2009) that we have previously observed as being co-regulated (White et al., 2017). This suggests that the eyes are affected in some of the analysed mutants. Whether there was an enrichment of DE genes on the mutant chromosome did not depend on the total number of DE genes found in the experiment, although experiments with very high numbers of DE genes tended not to show an enrichment (Figure 2B).

In one experiment, we noticed that the differential expression of some genes was linked to one of the wild-type chromosomes in the experiment. This experiment was an intercross of two different sox10 alleles, t3 (Dutton et al., 2001) and baz1 (Carney et al., 2006) sampled at 24 hr post-fertilisation (hpf). Embryos were genotyped for both sox10 alleles, which allowed us to also track the wild-type chromosomes in the cross. We noticed that two of the genotypes had expression levels for some genes on the same chromosome as sox10 that were different from the other two genotypes (Figure 2C). The groups with higher expression shared the wild-type chromosome from the baz1/+ parent (Figure 2C, yellow chromosome) whereas the others shared the chromosome carrying the baz1 allele (Figure 2C, blue chromosome). One explanation for this is that there is higher expression from the si:ch73–308m11.1 allele on the wild-type chromosome (Figure 2C, yellow chromosome), which led us to hypothesise that the enrichment of DE genes on the mutant chromosome is not necessarily dependent on the mutant gene.

Our hypothesis is that ASE, that is, polymorphism-driven variation in expression levels of genes, is common across the genome. This would manifest as differential expression when a genomic locus is driven to homozygosity in some individuals and the expression levels of genes in this locus are compared to those in individuals that are heterozygous, or homozygous for the other allele.

### ASE is common in a wild-type cross

To test the hypothesis that the over-representation of DE genes on the mutant chromosome can be driven by ASE independently of the mutated gene, we investigated gene expression in wild-type fish with defined haplotypes to enable easy identification of the different alleles in the cross. We used the SAT line, which was generated from an intercross of one fully sequenced double haploid AB fish and one fully sequenced double haploid Tübingen fish (Howe et al., 2013). This means that for any position in the genome there are up to two possible alleles. The original haplotypes have recombined through the generations that the SAT line has been maintained by incrossing.

We incrossed two SAT fish, fin-clipped them to isolate DNA for exome sequencing, collected 96 morphologically normal embryos at 5 days post-fertilisation (dpf), extracted RNA from the individual embryos, and did RNA-seq on the 96 samples. We used the exome sequence of the SAT parent fish for this cross to call SNPs and identify regions that are either homozygous for the AB haplotype, homozygous for the Tübingen haplotype, or heterozygous. Using the RNA-seq reads and SNPs identified in the parental exome data, we genotyped the embryos at locations that distinguish the AB and Tübingen haplotypes. Aggregating these data in 1 Mbp regions allowed us to determine the haplotypes of each individual embryo. We identified regions of the parental genomes where at least two genotypes, and thus potentially ASE, are possible in the offspring (informative regions) and where we had sufficient read depth to unambiguously identify the haplotypes in the offspring. We grouped the 96 RNA-seq samples according to their haplotype in that region (Figure 3A–B). Across the genome, this resulted in 82 different groupings of embryos according to local genotype. Embryos that had evidence of a recombination event within the informative region were assigned to a genotype group according to the largest contiguous section of the region.

![Figure 3.](https://cdn.elifesciences.org/articles/72825/elife-72825-fig3-v2.jpg)

**Figure 3.:** (A) Experimental design. Two wild-type SAT fish were incrossed and 96 embryos were collected for RNA-sequencing (RNA-seq) at 5 days post-fertilisation (dpf). Depending on the haplotypes of the parents, different combinations of genotype are possible in specific regions in the offspring. (B) The haplotypes of the collected embryos were determined in 1 Mbp bins using the RNA-seq reads and the embryos were grouped according to the haplotypes in specific regions. Chromosome 5 is shown with chromosomal position along the x-axis and samples on the y-axis. 1 Mbp bins are coloured according to the haplotype in that region. Blue = homozygous Tübingen (Tu/Tu), green = heterozygous AB/Tübingen (AB/Tu), orange = homozygous AB (AB/AB), dark grey = not consistent with parental haplotypes (NC), light grey = no haplotype call (NA), due to, for example, low coverage. Examples of regions used to group the embryos are boxed. Red ovals indicate regions containing recombination breakpoints in the samples labelled in (C). (C–D) Examples of differentially expressed genes from two different groupings. (C) Counts for the myhc4 gene, grouped according to the haplotypes in the region 5:31–37 Mbp (region 1 in B). The Tübingen allele is expressed at very low levels, with much higher expression in the heterozygotes. There are two examples of embryos with recombinations within the region. Compare to red ovals in the haplotype plot in (B). (D) Example of a differentially expressed gene (slc4a4a) in a region where all three genotypes are present (5:44–53 Mbp, region 2 in B). As in (C), the Tübingen allele has lower expression, with the heterozygotes showing intermediate levels. (E) Distribution of absolute log2(fold change) values found between wild-type alleles. Differences when comparing homozygous embryos (blue) are generally larger than when comparing heterozygotes to homozygotes (yellow).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/72825/elife-72825-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Representation of the parental haplotypes of the SAT cross across all 25 chromosomes (blue = Tu/Tu, green = AB/Tu, orange = AB/AB). The black box shows the region (Chr5:44–53 Mb) that was used to define the groups of embryos compared using DESeq2. The red triangles show the positions of the genes that are differentially expressed when using this sample grouping, most of which are in or close to the region. (B) Expanded plot of chromosome 5 from 40 to 60 Mb. The differentially expressed genes are labelled.

Differential gene expression analysis on each different embryo grouping revealed DE genes located in or close to the region of the genome that was used to define the embryo groups (Figure 3 and Figure 3—figure supplement 1, Supplementary file 4). The log2(fold changes) of affected genes varied widely but had an absolute mean of 0.5 for the homozygous versus homozygous comparison (Figure 3E). This demonstrates that genes can show ASE in a wild-type context (Figure 3C–E).

Through these analyses, it was also possible to see the consequences of meiotic recombination in individual embryos (Figure 3B–C). For example, two samples (C7 and E5) showed recombination in the 31–37 Mbp region of chromosome 5 (red ovals in Figure 3B). The genotypes near the myhc4 gene were the opposite of that called for the whole region and this is evident in the count plot – C7 has expression comparable with the Tu/Tu haplotype, despite being assigned AB/Tu, and E5 has expression similar to the AB/Tu samples despite being assigned Tu/Tu based on the entire 31–37 Mbp region (Figure 3C).

### ASE can alter interpretation of experiments

To assess what impact ASE might have on the interpretation of RNA-seq experiments, we looked at the effect on Gene Ontology (GO) enrichments if DE genes on the same chromosome as the mutation were removed from the DE gene list. To do this, we ran GO enrichment on two different gene lists for each experiment. The first list comprised all the DE genes and the second excluded genes on the same chromosome as the mutation. The gene harbouring the mutation was not removed if it was DE. It is important to note that removing all the genes on the same chromosome potentially removes genes that are misregulated due to the mutation as well as those caused by mutation-independent ASE; for almost all experiments it is not possible to distinguish between the two without further experimental analyses (see next section). The enrichment of GO terms from the two lists was compared using the Jaccard similarity coefficient (Jaccard, 1912).

These analyses showed that ASE could affect enriched GO terms, but that this effect was very variable (Figure 4A). This is not unexpected and will depend on how many of the DE genes are on the same chromosome as the mutation and whether the genes on the same chromosome contribute to any of the enriched GO terms using the full list. Experiments where there wasn't an enrichment of DE genes on the mutant chromosome generally did not show as large an effect, which again makes sense as the DE genes linked to the mutation were a smaller fraction of the gene list.

![Figure 4.](https://cdn.elifesciences.org/articles/72825/elife-72825-fig4-v2.jpg)

**Figure 4.:** (A) Distribution of the overlap between the Gene Ontology (GO) terms enriched when DE genes linked to the mutation are removed. GO term enrichment was done on both the DE gene list and the list with the genes on the same chromosome as the mutation removed (excluding the mutated gene itself). The lists of enriched GO terms were then compared and the Jaccard similarity coefficient (number of GO terms enriched in both sets/total number of enriched GO terms) calculated. Each point represents one experiment. Experiments are split according to whether the chromosome with the mutated gene has an enrichment of DE genes or not. Points are coloured by the number of DE genes identified in the experiment (log10 scale). (B) Plot showing the changes in GO term enrichment for a single experiment (sox10t3/baz1 incross at 36 hr post-fertilisation). Each point is an enriched GO term ranked by p-value (highest ranked terms at the top) and the lines connect the same terms if they are enriched using both gene lists (all genes or genes linked to the mutation removed). Unconnected points are terms that are only enriched for either the ‘all genes’ list (open circles) or for the ‘linked genes removed list’ (open squares). (C) Network diagram representation of the same GO enrichments as in (B). Each node represents a GO term, and the nodes are connected by an edge if the genes annotated to the term overlap sufficiently (Cohen’s kappa > 0.4). GO term nodes are coloured by whether they are enriched in both lists (orange) or just one (blue = all genes only, green = linked genes removed only). The shape of the nodes represents the GO term domain of the term (circle = biological process, square = cellular component, hexagon = molecular function).

Overall, experiments with fewer DE genes showed larger effects. However, there were experiments with hundreds to thousands of DE genes where only 50% of GO terms were shared between both sets. For example, in a sox10 t3/baz1 intercross at 36 hpf, 302 genes were DE, 32 of which were on chromosome 3 (the same chromosome as sox10). GO term enrichment using the full list of genes produced 92 enriched GO terms, only 49 of which were also enriched if the genes on chromosome 3 had been removed from the list (Figure 4B–C). In addition, 28 extra GO terms were enriched using the shorter gene list.

### Distinguishing response genes from ASE

Having established that ASE is widespread and can significantly alter the transcriptional profiles of mutant zebrafish, we wondered whether there is a way to distinguish potential ‘true’ response genes located on the same chromosome as the mutation, that is, those that change expression due to the altered function of the mutated gene, from those DE genes that arise through ASE. We went back to the expression data from the compound heterozygous sox10t3;sox10baz1 cross and found that the genes that were DE between sox10t3/baz1 individuals and their siblings and located on chromosome 3 fell into different groups with respect to their expression levels across the four different genotypes (Figure 5). Ten genes showed expression patterns as shown in Figure 2C, where increased expression was linked to the presence of a specific allele (Figure 5A and C). Only one gene (ENSDARG00000110416) located on another chromosome, encoding an miRNA, showed a similar pattern (Figure 5—figure supplement 1). By contrast, the other 15 DE genes (excluding sox10 itself) on chromosome 3 showed genotype-dependent transcript levels that were consistent with (though do not prove) a response to loss of sox10 function, that is, the wild types and the compound heterozygous individuals had opposing expression levels whereas both heterozygous genotypes had intermediate levels or the same as wild types (Figure 5B and C). Sox10 is a key regulator of neural crest development, so we looked for published spatial expression data at 24 hpf on ZFIN (zfin.org). Of the genes we speculated to be downstream of sox10, all four with data on ZFIN are expressed in neural (kctd13 and cygb1) and neural crest (syngr1a and vasnb) derivatives, whereas the three ASE candidates with available data are not spatially restricted (traf7, polr3h, and polr2f). Consequently, for genes showing single allele-linked expression patterns, it is likely that ASE is the primary driver of their differential expression and that they are probably red herrings.

![Figure 5.](https://cdn.elifesciences.org/articles/72825/elife-72825-fig5-v2.jpg)

**Figure 5.:** (A) Plot of normalised counts consistent with ASE. This shows either reduced expression from the allele on one of the wild-type chromosomes (white chromosome in the diagram under the plot) or increased expression from the allele on the t3 chromosome (red chromosome). Yellow = wild-types (+/+), orange = t3 heterozygotes (t3/+), blue = baz1 heterozygotes (+/baz1), purple = compound heterozygotes (t3/baz1). (B) Normalised counts consistent with a response to the sox10 mutations. The compound heterozygotes have reduced expression and the other two groups of heterozygotes are intermediate between the compound heterozygotes and the wild types. (C). Boxplots of the expression of all the differentially expressed (DE) genes on chromosome 3. These are split into two groups, those that are consistent with being downstream of sox10 (sox10-DE) and those that appear to be driven by allele-specific expression unrelated to sox10 (ASE-DE).

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/72825/elife-72825-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** The expression of this gene according to genotype is not consistent with a response to a recessive mutation. Yellow = wild types (+/+), orange = t3 heterozygotes (t3/+), blue = baz1 heterozygotes (+/baz1), purple = compound heterozygotes (t3/baz1).

## Discussion

Transcriptional profiling is a powerful and popular technique to investigate the gene expression changes resulting from organismal insults such as drug treatments, infections, or altered gene function. To gain mechanistic insight into gene regulatory events affected by a particular mutation, it is paramount to distinguish specific responses due to altered function of the mutated genes from other causes that change transcript abundance, such as developmental delay or technical artefacts such as batch effects. In this work, we describe a previously under-appreciated effect of ASE on the transcriptomes of zebrafish mutants. In 51 out of 124 transcriptional profiling experiments comparing zebrafish mutants and siblings at different stages of development, we found a statistically significant enrichment of DE genes on the same chromosome as the mutated gene. In a previous study using RNA-seq to map ENU mutations (Miller et al., 2013), it was noted that very few genes were detected as being DE in regions linked to the mutation. This difference is likely the result of methodological differences between the two studies, the most significant of which is the sample size. Miller et al. used one mutant and one wild-type sample, whereas our study has a median sample size of 10 per condition.

The physical arrangement of genes in an organism’s genome is not random. Co-expression of functionally related genes using shared regulatory elements and/or transcription factors provides an evolutionary pressure to keep these genes clustered in physical proximity within a chromosome (Thévenin et al., 2014). Consequently, it is possible that a mutation affecting one gene could alter expression levels of nearby genes if they form a functionally related cluster. However, the neighbouring DE genes in the tested mutant lines showed no obvious functional connections. Of note, 7/16 chromosomal enrichments that were not linked to the mutated genes affected a chromosome 9 cluster of crystallin genes that are expressed in the eye. Instead we found that the enrichments were driven by ASE, which has been widely demonstrated across different tissues and organisms (Battle et al., 2017; Huang et al., 2015; Kim-Hellmuth et al., 2020) and can play a role in developmental and disease processes (Libioulle et al., 2007; Moffatt et al., 2007; Nicolae et al., 2010).

ASE is often tissue-dependent and the average log2(fold change) between alleles in human ASE is about 0.6 as measured in different tissues (Battle et al., 2017). Here, we have observed ASE at similar magnitudes even when averaged across all tissues through whole embryo RNA-seq. This suggests that the expression differences between alleles would be even larger when looking at individual tissues.

Zebrafish wild-type ‘strains’ are not strains in the same sense as the well-characterised inbred lines in mouse or medaka, for example. Zebrafish are highly polymorphic, such that ASE is evident even in lines that were not outcrossed to another genetic background before the experiment. Consequently, ASE could potentially impact the penetrance or expressivity of phenotypes caused by the same mutation in different genetic backgrounds (Sanders and Whitlock, 2003; Sheehan-Rooney et al., 2013; Young et al., 2019). Indeed, Sheehan-Rooney et al., 2013, showed that the expression of ahsa1a differed by more than threefold in two different backgrounds (WIK and EkkWill) and was responsible for a difference in severity of the phenotype caused by a mutation in gata3. The effect of ASE is expected to be much less pronounced in RNA-seq data from inbred mouse strains in which allelic polymorphism is much less common. Indeed, in our work on RNA-seq data from mouse knockouts (Collins et al., 2019), we did not observe enrichment of DE genes on the mutant chromosome. However, ASE should be considered when working with wild mouse strains, crosses between different genetic backgrounds, or indeed with any organism that isn’t fully inbred.

Given that ASE can lead to differential expression between mutants and siblings, can we correct for it in transcript profiling experiments? The solution is not as simple as removing any DE genes in the same region of the chromosome as the mutation being studied. This is because the DE genes on the same chromosome as the mutation are likely to be a mix of genuine responses to the mutation and linkage of ASE unrelated to the mutation. One way to resolve this would be to use two different mutant alleles of the same gene to generate compound heterozygotes and enable tracking of parental alleles. This would allow genotyping for both alleles and the ability therefore to also identify the different wild-type chromosomes in the cross. As shown in Figure 5, this makes it possible to distinguish between potential genuine responses to the mutation and spurious ones. Another possibility would be to identify an informative SNP in the wild-type alleles of the mutant gene being studied to allow genotyping of both the mutation and the wild-type alleles. There are also complementary approaches to investigate gene function that avoid the confounding effects of ASE. Transgenic overexpression of the gene of interest could validate true target gene responses and should leave ASE genes unaffected. Alternatively, analysing morpholino- or CRISPR/Cas9-injected G0 embryos (Eisen and Smith, 2008; Kroll et al., 2021; Wu et al., 2018) should avoid the ASE effect as the injected embryos will have a mix of background alleles. Note that although using G0 CRISPR/Cas9 mutants avoids the effect of ASE, F2 fish carrying stable CRISPR/Cas9-induced mutations will again show the effects of ASE when comparing homozygous mutants to siblings.

All these methods involve extra effort and expense, as well as having their own specific caveats and drawbacks (such as off-targets effects and mosaicism), and so would need careful consideration with respect to the need to validate specific gene expression changes for the conclusions of the study. As a first step, we recommend that, whatever analysis pipeline is used, the output of DE genes contains the locations of the genes, making it possible to easily see which genes are on the same chromosome as the mutation and therefore candidates for ASE.

## Materials and methods

**Key resources table**


<table>
  <thead>
    <tr>
      <th>Reagent type (species) or resource</th>
      <th>Designation</th>
      <th>Source or reference</th>
      <th>Identifiers</th>
      <th>Additional information</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Gene (zebrafish, Danio rerio)</td>
      <td>mitfa</td>
      <td>Ensembl</td>
      <td>ENSDARG00000003732</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (zebrafish, Danio rerio)</td>
      <td>sox10</td>
      <td>Ensembl</td>
      <td>ENSDARG00000077467</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (zebrafish, Danio rerio)</td>
      <td>si:ch73-308m11.1</td>
      <td>Ensembl</td>
      <td>ENSDARG00000039752</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (zebrafish, Danio rerio)</td>
      <td>myhc4</td>
      <td>Ensembl</td>
      <td>ENSDARG00000035438</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (zebrafish, Danio rerio)</td>
      <td>slc4a4a</td>
      <td>Ensembl</td>
      <td>ENSDARG00000013730</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (zebrafish, Danio rerio)</td>
      <td>polr3h</td>
      <td>Ensembl</td>
      <td>ENSDARG00000102590</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (zebrafish, Danio rerio)</td>
      <td>vasnb</td>
      <td>Ensembl</td>
      <td>ENSDARG00000102565</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (zebrafish, Danio rerio)</td>
      <td>gata3</td>
      <td>Ensembl</td>
      <td>ENSDARG00000016526</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (zebrafish, Danio rerio)</td>
      <td>ahsa1a</td>
      <td>Ensembl</td>
      <td>ENSDARG00000028664</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (zebrafish, Danio rerio)</td>
      <td>BX537296.1</td>
      <td>Ensembl</td>
      <td>ENSDARG00000110416</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (zebrafish, Danio rerio)</td>
      <td>cygb1</td>
      <td>Ensembl</td>
      <td>ENSDARG00000099371</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (zebrafish, Danio rerio)</td>
      <td>BX000701.1</td>
      <td>Ensembl</td>
      <td>ENSDARG00000099172</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (zebrafish, Danio rerio)</td>
      <td>syngr1a</td>
      <td>Ensembl</td>
      <td>ENSDARG00000002564</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (zebrafish, Danio rerio)</td>
      <td>hlfa</td>
      <td>Ensembl</td>
      <td>ENSDARG00000074752</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (zebrafish, Danio rerio)</td>
      <td>coro7</td>
      <td>Ensembl</td>
      <td>ENSDARG00000089616</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (zebrafish, Danio rerio)</td>
      <td>kctd13</td>
      <td>Ensembl</td>
      <td>ENSDARG00000044769</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (zebrafish, Danio rerio)</td>
      <td>RF00091</td>
      <td>Ensembl</td>
      <td>ENSDARG00000084991</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (zebrafish, Danio rerio)</td>
      <td>trir</td>
      <td>Ensembl</td>
      <td>ENSDARG00000104178</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (zebrafish, Danio rerio)</td>
      <td>tfap4</td>
      <td>Ensembl</td>
      <td>ENSDARG00000103923</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (zebrafish, Danio rerio)</td>
      <td>CU138547.1</td>
      <td>Ensembl</td>
      <td>ENSDARG00000074231</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (zebrafish, Danio rerio)</td>
      <td>CABZ01019904.1</td>
      <td>Ensembl</td>
      <td>ENSDARG00000104193</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (zebrafish, Danio rerio)</td>
      <td>traf7</td>
      <td>Ensembl</td>
      <td>ENSDARG00000060207</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (zebrafish, Danio rerio)</td>
      <td>polr2f</td>
      <td>Ensembl</td>
      <td>ENSDARG00000036625</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (zebrafish, Danio rerio)</td>
      <td>CR394546.5</td>
      <td>Ensembl</td>
      <td>ENSDARG00000112755</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (zebrafish, Danio rerio)</td>
      <td>FP326649.1</td>
      <td>Ensembl</td>
      <td>ENSDARG00000088820</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (zebrafish, Danio rerio)</td>
      <td>AL953907.2</td>
      <td>Ensembl</td>
      <td>ENSDARG00000113960</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (zebrafish, Danio rerio)</td>
      <td>CR388047.2</td>
      <td>Ensembl</td>
      <td>ENSDARG00000109888</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (zebrafish, Danio rerio)</td>
      <td>CABZ01040998.1</td>
      <td>Ensembl</td>
      <td>ENSDARG00000111638</td>
      <td></td>
    </tr>
    <tr>
      <td>Gene (zebrafish, Danio rerio)</td>
      <td>si:dkey-175d9.2</td>
      <td>Ensembl</td>
      <td>ENSDARG00000093476</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (zebrafish, Danio rerio)</td>
      <td>AB</td>
      <td>ZIRC</td>
      <td>ZDB-GENO-960809–7</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (zebrafish, Danio rerio)</td>
      <td>Tübingen</td>
      <td>ZIRC</td>
      <td>ZDB-GENO-990623–3</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (zebrafish, Danio rerio)</td>
      <td>SAT</td>
      <td>ZIRC</td>
      <td>ZDB-GENO-100413–1</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>ENSDARG00000089358sa19600</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-190501–298</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>bace2hu3332</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-100723–4</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>bmp7asa1343</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-120411–112</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>cacna1csa6050</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-161003–17955</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>capza1bta253a</td>
      <td>PMID:23594742</td>
      <td></td>
      <td>Allele not cryopreserved</td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>capzbhi1858bTg</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-040907–2</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>cax1sa10712</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-130411–634</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>cdan1sa5902</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-161003–17833</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>cep192sa875</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-120411–491</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>clp1sa6358</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-161003–18184</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>copb1sa3636</td>
      <td>PMID:23594742</td>
      <td></td>
      <td>Allele not cryopreserved</td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>cyfip2sa1556</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-120411–193</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>cyldasa21010</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-161003–11078</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>dag1hu3072</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-070315–1</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>dhx15sa7108</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-161003–18741</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>dmdta222a</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-980413–693</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>dnmt3aasa3105</td>
      <td>PMID:23594742</td>
      <td></td>
      <td>Allele not cryopreserved</td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>dnmt3aasa617</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-120411–432</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>dnmt3basa14480</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-130411–3189</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>dnmt3bb.1sa15458</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-130411–4030</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>frem2asa21742</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-161003–11257</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>glra1sa3896</td>
      <td>PMID:23594742</td>
      <td></td>
      <td>Allele not cryopreserved</td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>gmdsp31erb</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-051012–8</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>gpaa1sa2042</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-161003–10931</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>greb1sa1260</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-120411–60</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>grin2b (2 of 2)sa19927</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-190501–603</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>hsp90aa1.1u45</td>
      <td>PMID:18256191</td>
      <td>ZDB-ALT-080401–1</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>jak2bsa20578</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-161003–10984</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>kdm2aasa898</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-120727–213</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>kdm2aasa9360</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-161003–20015</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>kitlgatc244b</td>
      <td>PMID:23364329</td>
      <td>ZDB-ALT-980203–1317</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>lamb2tm272a</td>
      <td>PMID:19736328</td>
      <td>ZDB-ALT-980203–1438</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>lamc1sa379</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-120411–351</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>las1lsa674</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-120727–150</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>ldlrsa16375</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-130411–4850</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>maptasa22009</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-161003–11315</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>mdn1sa1349</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-120411–117</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>megf10sa6166</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-161003–18049</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>meis1sa9839</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-130411–5422</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>mitfaw2</td>
      <td>PMID:10433906</td>
      <td>ZDB-ALT-990423–22</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>nebhu2849</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-070730–10</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>bufti209</td>
      <td>PMID:9007258</td>
      <td>ZDB-ALT-980203–1049</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>nod2sa18880</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-161003–10423</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>nol9sa1022</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-120411–10</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>nol9sa1029</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-160721–33</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>nup88sa2206</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-120727–92</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>pax2asa24936</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-161003–12106</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>pcnasa8962</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-161003–19656</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>pla2g12bsa659</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-161003–18374</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>pld1sa1311</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-120411–91</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>polr1asa1376</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-120411–135</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>ptf1asa126</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-100506–17</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>rpl13sa638</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-161003–18201</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>rps24sa2681</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-161003–12995</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>ryr1sa23341</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-161003–11675</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>ryr1sa6529</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-161003–18326</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>sh3gl2sa19508</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-161003–10694</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>si:ch211-168k14.2sa6115</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-161003–18015</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>slc22a7bsa365</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-120411–342</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>slc2a11bsa1577</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-120411–200</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>smarce1sa18758</td>
      <td>PMID:23594742</td>
      <td>Allele not cryopreserved</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>sox10baz1</td>
      <td>PMID:17065232</td>
      <td>ZDB-ALT-070131–1</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>sox10t3</td>
      <td>PMID:11684650</td>
      <td>ZDB-ALT-980203–1827</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>srpk3sa18907</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-161003–10436</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>sucla2sa20646</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-161003–11003</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>tcf7l1am881</td>
      <td>PMID:11057671</td>
      <td>ZDB-ALT-001107–2</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>tfap2asa24445</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-131217–17748</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>tfap2csa18857</td>
      <td>PMID:23594742</td>
      <td>Allele not cryopreserved</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>tfip11sa3219</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-120727–140</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>tmod4hu3530</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-070914–1</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>top1lsa2597</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-161003–12704</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>ttnasa1029</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-160721–33</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>ttnasa787</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-120411–459</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>ttnbsa5562</td>
      <td>PMID:23594742</td>
      <td>Allele not cryopreserved</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>vps16sa7027</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-161003–18689</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>vps16sa7028</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-161003–18690</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>vps51p9emcf</td>
      <td>PMID:16581006</td>
      <td>ZDB-ALT-060602–2</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>wu:fj82b07sa24599</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-161003–20235</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>yap1sa25458</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-200207–2</td>
      <td></td>
    </tr>
    <tr>
      <td>Genetic reagent (zebrafish, Danio rerio)</td>
      <td>zgc:171,763sa22031</td>
      <td>PMID:23594742</td>
      <td>ZDB-ALT-161003–11320</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>HISAT2</td>
      <td>PMID:31375807</td>
      <td>RRID:SCR_015530version 2.1.0</td>
      <td>https://github.com/DaehwanKimLab/hisat2</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>featureCounts</td>
      <td>PMID:24227677</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>DESeq2</td>
      <td>PMID:25516281</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>BCFTools</td>
      <td>PMID:33590861</td>
      <td>RRID:SCR_002105version 1.4</td>
      <td>https://samtools.github.io/bcftools/bcftools.html</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>statsmodels</td>
      <td>http://conference.scipy.org/proceedings/scipy2010/pdfs/seabold.pdf</td>
      <td></td>
      <td>https://www.statsmodels.org/stable/index.html</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>DeTCT</td>
      <td>PMID:26238335</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>BWA</td>
      <td>https://arxiv.org/abs/1303.3997</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>biobambam</td>
      <td>https://gitlab.com/german.tischler/biobambam2</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>mpileup</td>
      <td>PMID:21903627</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>QCALL</td>
      <td>PMID:20980557</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GATK</td>
      <td>PMID:21478889</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Tophat</td>
      <td>PMID:23618408</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>QoRTs</td>
      <td>PMID:26187896</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

### RNA-seq and LD mapping

Eight independent mutant fish lines under study by groups at UCL (zebrafishucl.org) were analysed by RNA-seq in order to simultaneously gain gene expression data and to measure alleles across the genome in order to help map the causative mutation. Seven of these lines were the product of ENU random mutagenesis, one was created by a random viral insertion, and one by a targeted CRISPR insertion. An additional sample was taken from the literature (Armant et al., 2016) at random by searching Pubmed for papers where RNA-seq data had been uploaded to the European Nucleotide Archive.

In preparation for RNA-seq, embryos or larvae were sorted into two groups based on their phenotypes (mutant and sibling), each comprising three pools of at least 15 individuals. RNA was extracted from these six samples and sequenced using the IIlumina NextSeq platform (2 × 75 bp reads, approximately 75 million reads per sample). Reads were aligned to the GRCz10 genome using HISAT2 (Kim et al., 2019). To measure differential expression, transcripts were counted from the aligned RNA-seq reads using featureCounts (Liao et al., 2014) and compared using DESeq2 (Love et al., 2014). A gene was considered DE if the adjusted p-value from DESeq2 was below 0.05.

To perform LD mapping, the three samples in each group were analysed as a single pooled sample for single nucleotide polymorphisms (SNPs) by BCFtools (Li, 2011), calculating the allele ratio at each SNP location. SNPs which appeared in only one of the two genotype pools were filtered out, as were those with a quality score below 100. The absolute difference between a given SNP’s mutant and sibling allele ratio indicates the degree of segregation of that allele (Mackay and Schulte-Merker, 2014). These values can be smoothed using LOESS, producing maps of the genome showing regions of high LD (Minevich et al., 2012). The physical location of each gene’s start codon in the GRCz10 genome assembly was downloaded from Ensembl BioMart and appended to the DESeq2 table. The LD value was estimated at each gene’s position based on interpolation of the LOESS-smoothed SNP data. Finally, a logistic regression model was used to test the effect of LD on a gene’s probability of being DE. This was performed using the Logit function of the Python module statsmodels.

### DeTCT sequencing

DeTCT libraries were generated, sequenced, and analysed as described previously (Collins et al., 2015). The resulting genomic regions and putative 3′ ends were filtered using DeTCT’s filter_output (v0.2.0)script (https://github.com/iansealy/DETCT/blob/master/script/filter_output.pl, Sealy, 2020) in its --strict mode. --strict mode removes 3’ ends in coding sequence, transposons, if nearby sequence is enriched for As or if not near a primary hexamer. Regions not associated with 3′ ends are also removed. Differential expression analysis was done using DeTCT’s run_pipeline (v0.2.0)script (https://github.com/iansealy/DETCT/blob/master/script/run_pipeline.pl) using DESeq2 (Love et al., 2014) with an adjusted p-value cut-off of 0.05. Sequence data were deposited in the European Nucleotide Archive (ENA) under accessions ERP001656, ERP004581, ERP006132, ERP003802, ERP004579, ERP005517, ERP008771, ERP005564, ERP009868, ERP006133, ERP009078, and ERP013835. Details on the experiments are in Supplementary file 5.

### DNA sequencing

Double haploid AB and Tübingen fish were produced and sequenced as described in Howe et al., 2013. Whole genome sequencing data (SRA Study: ERP000232) was downloaded from the European Nucleotide Archive. Exome sequencing on parents for the wild-type SAT cross was done as described (Kettleborough et al., 2013). Reads were mapped to the GRCz11 genome assembly using BWA (Li and Durbin, 2010, v0.5.10) and duplicates were marked with biobambam (Tischler and Leonard, 2014). SNPs were called using a modified version of the 1000 Genomes Project variant calling pipeline (Abecasis et al., 2010). Initial calls were done by SAMtools mpileup (Li, 2011), QCALL (Le and Durbin, 2011), and the GATK Unified Genotyper (DePristo et al., 2011). SNPs not called by all three callers were removed from the analysis, along with any SNP that did not pass a caller’s standard filters. Additionally, SNPs were removed where the genotype quality was lower than 100 for GATK and lower than 50 for QCALL and SAMtools mpileup and where the mean read depth per sample was less than 10. These SNP calls were then filtered for positions that are informative of the parental background in the SAT cross, that is, ones that are homozygous reference in one double haploid fish and homozygous alternate in the other.

### RNA-seq of wild-type SAT embryos

RNA was extracted from 5 dpf larvae as described previously (Wali et al., 2022). Briefly, RNA was extracted from individual embryos by mechanical lysis in RLT buffer (Qiagen) containing 1 μl of 14.3 M β-mercaptoethanol (Sigma). The lysate was combined with 1.8 volumes of Agencourt RNAClean XP (Beckman Coulter) beads and allowed to bind for 10 min. The plate was applied to a plate magnet (Invitrogen) until the solution cleared and the supernatant was removed without disturbing the beads. This was followed by washing the beads three times with 70% ethanol. After the last wash, the pellet was allowed to air-dry for 10 min and then resuspended in 50 μl of RNAse-free water. RNA was eluted from the beads by applying the plate to the magnetic rack. Samples were DNase-I treated to remove genomic DNA. RNA was quantified using Quant-IT RNA assay (Invitrogen). Stranded RNA-seq libraries were constructed using the Illumina TruSeq Stranded RNA protocol after treatment with Ribozero. Libraries were pooled and sequenced on six Illumina HiSeq 2500 lanes in 75 bp paired-end mode. Sequence data were deposited in ENA under accession ERP011556. Reads for each sample were aggregated across lanes (median reads per embryo = 18.1 M) and mapped to the GRCz11 zebrafish genome assembly using TopHat (Kim et al., 2013, v2.0.13, options: --library-type fr-firststrand). The data were assessed for technical quality (GC-content, insert size, proper pairs, etc.) using QoRTs (Hartley and Mullikin, 2015). Counts for genes were produced using htseq-count (Anders et al., 2015, v0.6.0 options: --stranded = reverse) with the Ensembl v97 annotation as a reference. Differential expression analysis was done in R (R Development Core Team, 2019) with DESeq2 (Love et al., 2014) using a cut-off for adjusted p-values of 0.05.

The samples were genotyped at the positions that were determined to be informative using the double haploid sequence using GATK’s SplitNCigarReads tool followed by the HaplotypeCaller (Poplin et al., 2017) on the RNA-seq data. The genotype calls were converted to their strain of origin (either DHAB or DHTu) and haplotypes were called by taking the most frequent genotype call in 1 Mbp windows. Any haplotypes that were not consistent with the parental haplotypes were removed.
