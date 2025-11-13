# Immune genes are hotspots of shared positive selection across birds and mammals

## Authors

- Allison J Shultz<sup>1</sup> ([ORCID: 0000-0002-2089-4086](https://orcid.org/0000-0002-2089-4086)) †
- Timothy B Sackton<sup>1</sup> ([ORCID: 0000-0003-1673-9216](https://orcid.org/0000-0003-1673-9216)) †

### Affiliations

1. Informatics Group Harvard University Cambridge United States
2. Department of Organismic and Evolutionary Biology Harvard University Cambridge United States
3. Museum of Comparative Zoology Harvard University Cambridge United States

† Corresponding author

## Abstract

Consistent patterns of positive selection in functionally similar genes can suggest a common selective pressure across a group of species. We use alignments of orthologous protein-coding genes from 39 species of birds to estimate parameters related to positive selection for 11,000 genes conserved across birds. We show that functional pathways related to the immune system, recombination, lipid metabolism, and phototransduction are enriched for positively selected genes. By comparing our results with mammalian data, we find a significant enrichment for positively selected genes shared between taxa, and that these shared selected genes are enriched for viral immune pathways. Using pathogen-challenge transcriptome data, we show that genes up-regulated in response to pathogens are also enriched for positively selected genes. Together, our results suggest that pathogens, particularly viruses, consistently target the same genes across divergent clades, and that these genes are hotspots of host-pathogen conflict over deep evolutionary time.

## Introduction

Central to the study of evolutionary biology is the desire to understand how natural selection operates across a diverse set of populations and species. While many selective pressures vary across taxa, some common selective pressures may result in consistent patterns of natural selection across a set of species. By taking an unbiased approach and scanning as many identifiable orthologous genes as possible across a set of species for signatures of positive selection, it may be possible to identify functional patterns that indicate shared selective pressures.

Early comparative genomic studies on primates, mammals, bees, ants, Drosophila and other organisms (Schlenke and Begun, 2003; Sackton et al., 2007; Kosiol et al., 2008; Barreiro and Quintana-Murci, 2010; Roux et al., 2014) that included unbiased selection scans identified immune system pathways as common targets of natural selection. This implies that pathogens, which elicit the immune response, may be strong and consistent selective forces across species. Furthermore, in several clades of invertebrates, receptor genes, or the genes interacting directly with pathogens are most often the target of positive selection (Sackton et al., 2007; Waterhouse et al., 2007; Ellis et al., 2012). Finally, recent studies of mammals show that proteins that interact with viruses experience about twice as many amino acid changes compared to proteins that do not (Enard et al., 2016) and proteins that interact with Plasmodium experience elevated rates of adaptation (Ebel et al., 2017). While this evidence clearly implicates pathogens as a major selective force driving rapid evolution across a wide range of species, it is still unknown if pathogens tend to target a small, conserved set of host proteins (predicting repeated selection on the same genes), or whether pathogens tend to interact with hosts in lineage or clade-specific ways (predicting selection on different genes). Previous genome-wide studies have focused on single taxonomic lineages (e.g. mammals), or limited subsets of candidate genes across clades, but the availability of many new genomes now allows detailed comparisons across deeply divergent clades to test the degree to which the specific genes represent shared hotspots of positive selection across long evolutionary timescales.

Birds (class Aves) are a natural genomic model to study shared selection pressures with mammals. Birds share a number of convergent features with mammals, including traits (e.g. homeothermy), and common pathogens (e.g. Influenza A). Furthermore, the number of bird genomes has increased dramatically in recent years (e.g. Zhang et al., 2014a). However to our knowledge, there have been no studies of genome-wide signatures of positive selection in this ecologically important group. Birds are a radiation of approximately 10,000 species (Clements et al., 2016) that possess diverse morphologies and behaviors (Gill, 2007). They have a global distribution and diverse range of habitats (Jetz et al., 2012), and many species migrate thousands of miles annually (Gill, 2007), making them excellent models for studies of disease ecology. From a genomic perspective, they have small genomes, generally stable chromosomes, a low number of repetitive elements relative to other vertebrates, and low rates of gene loss and gain (Organ et al., 2007; Organ and Edwards, 2011; Zhang and Edwards, 2012; Ellegren, 2013; Zhang et al., 2014b). Birds have the same general blueprint of immune pathways as mammals, but with a slimmed down gene repertoire and some small differences in the functions of specific genes (Kaiser, 2010; Chen et al., 2013; Juul-Madsen et al., 2014). Studies of the evolutionary dynamics of avian immune genes have almost exclusively focused on the major histocompatibility complex genes (MHC) or toll-like receptors (TLRs), with evidence of positive selection across species in MHC class I genes (Alcaide et al., 2013), MHC class II genes (Edwards et al., 1995; Edwards et al., 2000; Hess and Edwards, 2002; Burri et al., 2008; Burri et al., 2010) and TLRs (Alcaide and Edwards, 2011; Grueber et al., 2014; Velová et al., 2018). From a broader perspective, the conclusions drawn from more general studies of positive selection across birds have been limited by including only a few species (e.g. Nam et al., 2010), or using low-power analysis methods (e.g. comparing overall dN/dS values across GO-terms (Zhang et al., 2014b)).

We use comparative genomics in birds to study genome-wide signatures of positive selection without any a priori assumptions of gene functions. We find that the strongest signatures of selection are concentrated in four general categories: immune system genes, genes involved in recombination and replication, genes involved in lipid metabolism, and phototransduction genes. By comparing avian and mammalian datasets, we show that genes under positive selection in birds are likely to be under positive selection in mammals, and that this signal is the strongest in viral defense immune pathways. Finally, we reanalyzed 26 independent studies of gene expression after infectious challenge in birds and mammals as an unbiased, alternative approach to characterizing genes with potential immune function. We show that genes up-regulated following a pathogen challenge are more likely to be under positive selection in birds compared to those not differentially expressed, that there is also an overlap in birds and mammals in genes up-regulated in response to pathogens, particularly viruses, and that some of the classic genes studied as targets of host-pathogen co-evolution (PKR, MX1) are under selection and up-regulated following pathogen challenge in both clades. Together, all of our results support the hypothesis that adaptation against pathogens consistently involves the same genes across deep evolutionary timescales.

## Results

### Strong signatures of positive selection throughout the avian genome

We used PAML and HyPhy site models to test genes for evidence of positive selection across 39 species of birds (Figure 1; Supplementary file 1 Table 1). We ran all models for 11,231 genes using the gene tree as the input tree and for 8669 genes using the species tree as the input tree. The 8669 genes used in the species tree analysis had a maximum of one sequence per species in the alignment, while the gene tree analysis included some alignments with up to three paralogs per species. To test for positive selection for each gene, we conducted likelihood ratio tests between models that include an extra ω parameter for some proportion of sites and models that do not include the extra ω parameter. An FDR-corrected p-value from that likelihood ratio test less than 0.05 is considered evidence of positive selection for that gene. For all model comparisons (PAML models described in Table 1), we found that between 17% and 73% of genes are under positive selection (Table 2). About 20% of genes are positively selected with the more conservative M1a vs. M2a tests or M2a vs M2a_fixed tests, with large overlaps among the genes identified. The less conservative M7 vs. M8 tests show much greater proportions of positively selected genes (~70%), although this is reduced to about 35% with the M8 vs. M8a test, indicating that the M8 model may often improve fit by adding a class of sites with ω very close to 1. HyPhy’s BUSTED identified ~ 50% of genes as positively selected (FDR-corrected p-value less than 0.05). Fewer than half of these genes are also identified as being positively selected by all PAML tests - 1562 genes with the gene tree as input and 1203 genes with species tree as input. In total, 14% of analyzed genes are found to be under positive selection in all tests (Table 2, Supplementary file 1 Table 2 (raw gene tree results), Supplementary file 1 Table 3 (raw species tree results)). We consider these 1562 genes to be a high-confidence positive selection gene set for downstream functional analyses. Compared to all other genes, the high-confidence positive selection gene set has overall higher distributions of M0 model ω values, which assumes a single ω for all sites in a gene (Figure 2A; Mann-Whitney U-test: gene trees: not-significant median ω = 0.084, significant median ω = 0.344, p<0.0001; species trees: not-significant ω = 0.084, significant ω = 0.332, p<0.0001).

![Figure 1.](https://cdn.elifesciences.org/articles/41815/elife-41815-fig1-v2.jpg)

**Figure 1.:** Photo credit from Wikimedia Commons (top to bottom): Elegant Crested Tinamou: DickDaniels, Greater Rhea: Quartl, Southern Cassowary: Summerdrought, Mallard: Dcoetzee, Red Junglefowl: Francesco Veronesi, Common Cuckoo: Mike McKenzie, Anna’s Hummingbird: Becky Matsubara, Little Egret: GDW.45, Adelie Penguin: Stan Shebs, Downy Woodpecker: Wolfgang Wander, American Crow: DickDaniels, Zebra Finch: Jim Bendon.

**Table 1.**
 PAML Model descriptions.


<table>
  <thead>
    <tr>
      <th>Model</th>
      <th>Model description</th>
      <th>Parameters</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>M0</td>
      <td>one ratio</td>
      <td>ω</td>
    </tr>
    <tr>
      <td rowspan="2">M1a</td>
      <td rowspan="2">neutral</td>
      <td>p0 (p1 = 1 p0)</td>
    </tr>
    <tr>
      <td>ω0 &lt; 1, ω1 = 1</td>
    </tr>
    <tr>
      <td rowspan="2">M2a_fixed</td>
      <td rowspan="2">neutral</td>
      <td>p0,p1 (p1 = 1 p0 - p1)</td>
    </tr>
    <tr>
      <td>ω0 &lt; 1, ω1 = 1, ω2 = 1</td>
    </tr>
    <tr>
      <td rowspan="2">M2a</td>
      <td rowspan="2">selection</td>
      <td>p0,p1 (p1 = 1 p0 - p1)</td>
    </tr>
    <tr>
      <td>ω0 &lt; 1, ω1 = 1, ω2 &gt; 1</td>
    </tr>
    <tr>
      <td>M7</td>
      <td>neutral (beta distribution)</td>
      <td>p, q</td>
    </tr>
    <tr>
      <td rowspan="2">M8a</td>
      <td rowspan="2">neutral (beta distribution)</td>
      <td>p0 (p1 = 1 p0)</td>
    </tr>
    <tr>
      <td>p, q, ωs = 1</td>
    </tr>
    <tr>
      <td rowspan="2">M8</td>
      <td rowspan="2">selection (beta distribution)</td>
      <td>p0 (p1 = 1 p0)</td>
    </tr>
    <tr>
      <td>p, q, ωs&gt; 1</td>
    </tr>
  </tbody>
</table>

**Table 2.**
 Counts (above) and proportions (below) for all tests of individual, and combined tests of selection for gene trees and species trees.


<table>
  <thead>
    <tr>
      <th>Dataset</th>
      <th>N genes</th>
      <th>m1a vs m2a</th>
      <th>m2a vs m2a_fixed</th>
      <th>m7 vs m8</th>
      <th>m8 vs m8a</th>
      <th>All PAML</th>
      <th>Busted</th>
      <th>All PAML + BUSTED</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Gene trees</td>
      <td>11231</td>
      <td>1925 0.17</td>
      <td>2197 0.20</td>
      <td>7504 0.67</td>
      <td>3679 0.33</td>
      <td>1901 0.17</td>
      <td>6244 0.56</td>
      <td>1562 0.14</td>
    </tr>
    <tr>
      <td>Species trees</td>
      <td>8669</td>
      <td>1783 0.21</td>
      <td>2026 0.23</td>
      <td>6293 0.73</td>
      <td>3395 0.39</td>
      <td>1752 0.20</td>
      <td>3870 0.45</td>
      <td>1203 0.14</td>
    </tr>
  </tbody>
</table>

Gene trees and species trees also had similar distributions of overall ω values with the M0 model (K-S test: D = 0.006, p=1, Figure 2B). The mean ω value is 0.15, the median ω is 0.10 and standard deviation is 0.14 using either the gene or species tree as the input tree. Because of the similarity between gene tree and species tree results, and to minimize issues associated with hemiplasy in species trees (Hahn and Nakhleh, 2016; Mendes and Hahn, 2016), for all bird-specific analyses below, we use focus on gene tree results to maximize the number of genes tested. However, all results are qualitatively similar with the species tree results as input.

![Figure 2.](https://cdn.elifesciences.org/articles/41815/elife-41815-fig2-v2.jpg)

**Figure 2.:** (A) Comparison of M0 model ω values between genes under selection for all site tests, and those not under selection, for both gene trees and species trees. The mean ω values were significantly higher for genes under selection for both gene trees and species trees (Mann-Whitney U-test: gene trees: W = 1201387, p < 0.0001; species trees: W = 938934, p < 0.0001). (B) Violin plot of ω values from the PAML M0 model using either gene trees or species trees as the input phylogeny. (C) Violin plot of alignment lengths for genes significant in all tests of selection, or not significant in all tests of selection using either gene trees or species trees as input phylogenies. (D) Distribution of the proportion of significant lineages for HOGs identified as not significant (FDR-corrected p-value ≥ 0.05), or significant (FDR-corrected p-values < 0.05) with BUSTED. The means of the two distributions are significantly different (Mann-Whitney U-test: W= 6205530, p<10-16).

We also explored whether alignment length had an effect on our ability to detect selection in a gene. We compared alignment lengths between our high-confidence genes detected as being under selection by all tests, and those that were not (Figure 2C). We assessed significance for this relationship using logistic regression, with selection status (under selection or not) as the dependent variable and alignment length as the independent variable. The model was significant for both gene trees (median length under selection = 1,818; median length not under selection = 1,089; coefficient = 3.49e-4, p-value<0.0001) and species trees (median length under selection = 1,893; median length not under selection = 1,158; coefficient = 3.46e-4, p-value<0.0001), likely indicating that power to detect selection increases with alignment length.

### Immune, recombination, lipid metabolism, and phototransduction pathways are enriched for positive selection in birds

For an unbiased perspective on whether or not positively selected genes are concentrated in particular functional pathways, we performed a pathway enrichment test of positively selected genes against a background of all genes tested. With chicken as the reference organism, 351 genes of the high-confidence positive selection gene set and 3347 of all genes tested could be mapped to KEGG pathways for use as the test set and gene universe respectively. Out of the 166 KEGG pathways available for chicken, or any other bird species, 119 had at least one gene with evidence of positive selection (Supplementary file 1 Table 4). We found 18 KEGG pathways that were significantly enriched with positively selected genes (q-value less than 0.1; Figure 3A; Supplementary file 1 Table 4). These 18 pathways belong to seven KEGG functional categories: infectious disease, immune system, signaling molecules and interaction, replication and repair, lipid metabolism, and sensory system. Some genes are shared by multiple enriched pathways, particularly among those with immune or recombination-related functions. However, many genes are uniquely enriched in a single pathway as well (Figure 3B), suggesting that these enrichment results are not driven by a few core genes present in many pathways. While we focus on the gene tree results due to the larger number of genes available for enrichment tests, species tree results show the same overall trends of significant immune and recombination-related pathways (Figure 3—figure supplement 1).

![Figure 3.](https://cdn.elifesciences.org/articles/41815/elife-41815-fig3-v2.jpg)

**Figure 3.:** (A) The 18 pathways significant at q-value < 0.1 ordered by enrichment values, calculated as the proportion of genes under selection in the pathway over the proportion of genes significant in all KEGG pathways. Points are filled by q-value, and each pathway is colored by the broader KEGG functional category. Edge lengths do not contain meaningful values, but are chosen to maximize viewability. Pathways with more genes under selection than expected based on median gene length are highlighted with an asterisk. (B) Map depicting the relationships of all significant genes among pathways. Each gene (small, light circle) is connected by a line to each pathway it belongs to (large, dark circle). Each point is shaded according to the broader KEGG functional category. See Figure 3—figure supplement 1 for pathways identified using species trees.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/41815/elife-41815-fig3-figsupp1-v2.jpg)

To test whether our pathway enrichment results were robust to reference organism, we also conducted pathway enrichment tests using zebra finch and human as the reference organism. Pathway enrichment results using zebra finch showed similar results as those presented above using chicken, particularly for immune-related pathways and recombination and repair pathways (Supplementary file 1 Table 5). Pathway enrichment results using human, which has additional annotated pathways, resulted in 37 pathways significantly enriched with positively selected genes (q-value less than 0.1; Supplementary file 1 Table 6) out of 269 pathways with at least one homologous gene in our dataset. Compared to the enrichment results using chicken, the human pathways primarily added many disease or immune pathways not available for birds, suggesting that the overall functional results are robust to reference organism.

Finally, to test whether gene length variance among KEGG pathways influenced our results, we estimated the expected number of genes under selection among genes annotated to a given pathway using the parameters from our logistic regression model conducted for all genes (see previous section), and compared these values to our observed results. We used a conservative Fisher’s exact test to test for significance, and find that while all of the pathways we observed have more genes under selection than expected based on median gene length alone (Figure 3; Supplementary file 1 Table 7), not all are statistically significant.

### Lineages clustered by genes under selection in birds are most strongly related to body size and lifespan

Codon-based site models typically can only detect positive selection when the same sites in the protein are under selection in numerous lineages. In order to detect selection limited to particular lineages, we relaxed this assumption, and used aBS-REL to estimate of the probability of selection independently at each branch of the phylogeny. To test consistency with our site-model results, we calculated the number of lineages with evidence for positive selection from the branch-site (aBS-REL) for each gene. We found that genes identified by BUSTED as having sites with evidence of positive selection across avian lineages also had significantly more lineages under selection using aBS-REL (Mann-Whitney U-test: median proportion significant lineages under selection given significant BUSTED result: 0.16, median proportion significant lineages under selection given non-significant BUSTED result: 0.05, p<10−16, Figure 2D). While branch-site tests can be subject to false inferences of positive selection due to multinucleotide mutations (Venkat et al., 2018), the similar patterns between our site-model results, and the aBS-REL results suggests that the overall patterns we observe hold true with this alternative analysis.

To identify additional functional classes of genes that may be selected in only a subset of lineages, we used a principle components analysis (PCA) to summarize the variance of parameter estimates (proportion of sites under selection, ω) across genes for each species, and then used phylogenetic comparative methods to identify species traits associated with PC loadings for each gene. We find three PCs that together explain 16.8% to 17.2% of the variance in aBS-REL parameter estimates across species, while the remaining PCs explain about 3% of the variance (Figure 4—figure supplement 4). PC1 (Figure 4) identifies a diverse set of species from different lineages sharing similar PC scores, while PC2 and PC3 appear to primarily identify lineage or clade-specific selection with variation depending on parameter and underlying tree used (gene or species trees). We conducted subsequent analyses using gene trees as input, given the similarity in results when using gene trees or species trees as the baseline phylogeny, so that we could maximize the number of genes available for analysis. We focused on PC1, the only principle component with similar values in unrelated lineages that varied consistently between parameters (Figure 4) to test whether it might be associated with life history. We found a significant correlation between log-transformed body mass, a proxy for many life history characteristics, and PC1 scores for each species using phylogenetic generalized least squares (Figure 5, proportion of sites under selection: β = −1.04, SE = 0.24, t-value = −4.26, p-value=0.0001; ω: β = −10.24, SE = 3.01, t-value = −3.40, p-value=0.0016).

![Figure 4.](https://cdn.elifesciences.org/articles/41815/elife-41815-fig4-v2.jpg)

**Figure 4.:** The PC1 scores indicate species in different clades that have similar parameter estimates from aBS-REL tests for positive selection and explain 7.2% of the variance across all genes tested. See Figure 4 supplement 1 for a visualization of PC1 estimated using ω values and gene trees, Figure 4 supplement 2 for a visualization of PC1 estimated using the proportion of sites under selection using species trees, Figure 4 supplement 3 for a visualization of PC1 estimated using ω using species trees, and Figure 4 supplement 4 for a visualization of eigenvalues for all PCAs.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/41815/elife-41815-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** The PC1 scores explain 7.6% of the variance across all genes tested.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/41815/elife-41815-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** The PC1 scores explain 7.6% of the variance across all genes tested.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/41815/elife-41815-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** The PC1 scores explain 7.6% of the variance across all genes tested.

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/41815/elife-41815-fig4-figsupp4-v2.jpg)

**Figure 4—figure supplement 4.:** PCA of the (A) proportion of sites under selection using gene trees, (B) log-transformed ω values using gene trees, (C) proportion of sites under selection using species trees, and D) ω values using species trees across genes for each species.

![Figure 5.](https://cdn.elifesciences.org/articles/41815/elife-41815-fig5-v2.jpg)

**Figure 5.:** Species values and reconstructed node values are connected by phylogeny. A PGLS analysis of these two traits showed a significant correlation (p=0.0001). See Figure 5—figure supplement 1 for a phylomorphospace plot depicting PC1 estimated using ω estimates.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/41815/elife-41815-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** Species values and reconstructed node values are connected by phylogeny. A PGLS analysis of these two traits showed a significant correlation (p=0.0016).

To understand any functional signal in the genes most strongly correlated with body size, we calculated a Spearman’s rank correlation for each gene using the proportion of sites under selection or log-transformed aBS-REL ω values for each lineage compared to log-transformed body mass. We performed KEGG pathway gene set enrichment using the ρ value for each gene. For the proportion of sites under selection, the most significant pathway was the cellular senescence pathway, which had a q-value of 0.61 and a normalized enrichment score of −1.52. For ω, the most significant pathway was the FoxO signaling pathway, which had a q-value of 0.09 and a normalized enrichment score of −0.62 (Supplementary file 1 Table 8).

### Shared signatures of selection in birds and mammals are enriched for viral-interacting pathways

We investigated whether we could detect signatures of pathogen-mediated selection at deeper time scales by testing whether the same genes are repeatedly under selection in both birds and mammals, and whether those genes are clustered in functional pathways. We combined our results with those from Enard et al., 2016, a study that used HyPhy’s BUSTED program to test for positive selection in 9681 orthologous genes from 24 mammal genomes. To best match the experimental procedures used by Enard et al., 2016, for bird-mammal comparisons we used only our BUSTED results with the species tree as the input phylogeny. The combined dataset consisted of 4931 orthologous genes with results in both clades.

We first tested for significant overlap in positively selected genes in both clades with a Fisher’s exact test. To understand whether these results were driven by genes with different levels of evidence for positive selection, we used four different FDR-corrected p-value cutoffs for significance, 0.1, 0.01, 0.001, and 0.0001. We found evidence for a significant overall overlap in positively-selected genes at all four different FDR-corrected p-value cutoffs, with stronger signal at smaller FDR-corrected p-values (Figure 6A, Supplementary file 1 Table 9). To ensure that these results were not driven by greater power to detect selection in more constrained genes, or longer genes, we conducted two additional analyses. First, we performed the Fisher’s exact test after removing the 20% most constrained genes, defined as the 20% of genes with the smallest m0 ω values. The results of this test were extremely similar to the previous test (Figure 6—figure supplement 1). Second, we conducted logistic regressions at each FDR-corrected p-value cutoff with the selection status in mammals as the response variable, and the selection status in birds, alignment length, and their interaction as the independent variables. At all FDR-corrected p-value cutoffs, both alignment length and selection status in birds are significant predictors of selection status in mammals (Supplementary file 1 Table 10), but their interaction is not. These results suggest that the overlap we observe between birds and mammals cannot be explained by either constraint bias or alignment length, and is instead likely related to the biology of the shared selected genes.

![Figure 6.](https://cdn.elifesciences.org/articles/41815/elife-41815-fig6-v2.jpg)

**Figure 6.:** For all analyses, we considered four different FDR-corrected p-value cutoffs for significance (to identify genes under positive selection) A. Odds ratio of overlap in genes under selection in both bird and mammal datasets. We indicate the number of observed genes under selection in both clades (n obs) and the number of expected genes under selection in both clades (n exp). B. Pathway enrichment scores from KEGG pathway enrichment tests with genes under selection in both birds and mammals as the test set, and genes under selection in birds as the background set. Ten pathways significantly enriched in birds with at least one gene under selection in both birds and mammals are color-coded. All other pathways are shown in grey. Significant enrichment values are outlined in black (q-value < 0.1) or grey (q-value < 0.2). C. Null distribution of enrichment scores generated from 1,000 randomization tests compared to empirical enrichment scores (vertical bars). Null distributions were generated by randomly selecting gene sets from the background set of genes (bird significant genes) for use as the test set. The randomized test set contained the same number of genes as empirical test set for each FDR-corrected p-value cutoff for significance. Empirical enrichment scores are depicted by a vertical bar, and with significant q-value scores outlined in black (q-value < 0.1) or grey (q-value < 0.2). See Figure 6 Supplement 1 for the odds ratio overlap in genes under selection in both bird and mammal datasets with the 20% most constrained genes removed.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/41815/elife-41815-fig6-figsupp1-v2.jpg)

We tested for functional enrichment in shared selected genes compared to all genes under selection in birds. KEGG enrichment with a test set of genes under selection in both clades and gene universe of genes under selection in birds, showed that pathways with immune function, particularly viral-interacting pathways, are significantly enriched for shared signatures of selection. These results are particularly significant at the lowest FDR-corrected p-value significance cutoffs (Figure 6B). As pathways enriched for positively selected genes in birds have higher enrichment values than other pathways (Figure 6B), we also conducted 1000 randomized enrichment tests to make sure pathways with more genes under selection in birds are not more likely to show more positively selected genes in both lineages by chance. We calculated multiple test corrected p-values for the empirical enrichment scores compared to the randomly generated null distribution within each of the four FDR-corrected p-value cutoffs for significance. These results corroborate those of KEGG enrichment tests, with Influenza A and Herpes simplex infection pathways showing significantly higher enrichment values, particularly at lower FDR-corrected p-value cutoffs for significance (Figure 6C). We observe four genes under selection in the Influenza A pathway out of 12 genes annotated to the pathway, compared to an expectation of 0.7 using an FDR-corrected p-value cutoff of 0.0001, and four genes under selection in both Influenza A and Herpes simplex pathways compared to expectations of 1 and 0.7, respectively, out of 14 and 10 pathway genes using an FDR-corrected p-value cutoff of 0.001.

### Genes up regulated in response to pathogens are more likely to be under positive selection in birds

We used gene expression data as an alternative test of whether pathogens are likely driving immune-related patterns of positive selection. First, for birds, we tested whether genes that were significantly differentially expressed following a pathogen challenge are more likely to be under positive selection. We used avian transcriptome data from 12 different studies representing seven different types of pathogens, including four viruses, two bacteria, and one species of protist (Supplementary file 1 Table 11). We compared both the proportions of positively-selected genes (using the high-confidence positive selection gene set) that were up-regulated following a pathogen challenge compared to those not differentially expressed, and the proportions of positively selected genes that were down-regulated following a pathogen challenge compared to those not differentially expressed. We found that for all pathogens, up-regulated genes are significantly more likely to be positively selected (Figure 7; Supplementary file 1 Table 12). The pattern was less consistent for down-regulated genes, with overall smaller numbers of down-regulated genes, weak evidence for a greater proportion of positively selected genes for West Nile Virus and Plasmodium, and weak evidence for a smaller proportion of positively selected genes for E. coli (Figure 7; Supplementary file 1 Table 12). Note that we did not test whether our positively selected genes were under selection in the specific lineages where the transcriptome data were collected. Therefore, we cannot say for sure that there is a direct link between selection and expression in each specific dataset. However, the observed correlation between gene expression and selection status only strengthens our hypothesis that these genes are under long-term co-evolutionary relationships between pathogens and hosts.

![Figure 7.](https://cdn.elifesciences.org/articles/41815/elife-41815-fig7-v2.jpg)

**Figure 7.:** For different pathogens, we show the proportion of genes under positive selection in birds (defined as significant with FDR corrected p-value < 0.05 for all PAML and BUSTED model comparisons) for genes down significantly down regulated, significantly up regulated, or not significantly differentially regulated. The number above each bar indicates the number of genes in a given transcriptional response class. The significance of enrichment for positively-selected genes in up- or down-regulated expression classes, as calculated by logistic regression, is indicated by asterisks above the “down” and “up” bars.

We tested for shared pathogen-mediated selection in birds and mammals by comparing bird and mammal gene expression patterns when challenged with the same, or a closely-related pathogen. There were five pathogens with publicly available data for at least one bird and mammal species – two viruses: Influenza A and West Nile virus, two bacteria: E. coli and mycoplasma, and one protist: Plasmodium (Supplementary file 1 Table 11). All comparisons between bird and mammal datasets for viral and bacterial pathogens showed that there was significant overlap in up-regulated genes, but no significant overlap in down-regulated genes (Table 3). Genes differentially expressed in response to Plasmodium showed the opposite pattern, with significant overlap in down-regulated genes, but no significant overlap in up-regulated genes (Table 3).

**Table 3.**
 Fisher’s exact test results from bird and mammal transcriptome studies.


<table>
  <thead>
    <tr>
      <th>Pathogen</th>
      <th>Transcriptional response</th>
      <th>N genes diff. expressed in both lineages</th>
      <th>N genes expected by chance</th>
      <th>p-value</th>
      <th>Odds ratio (95% conf. intervals)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Influenza</td>
      <td>up</td>
      <td>30</td>
      <td>14.8</td>
      <td>&lt;0.0001</td>
      <td>2.48 (1.56,3.84)</td>
    </tr>
    <tr>
      <td>Influenza</td>
      <td>down</td>
      <td>7</td>
      <td>7.2</td>
      <td>1.000</td>
      <td>0.96 (0.35,2.29)</td>
    </tr>
    <tr>
      <td>West Nile Virus</td>
      <td>up</td>
      <td>6</td>
      <td>0.9</td>
      <td>&lt;0.0001</td>
      <td>25.06 (4.46,253.47)</td>
    </tr>
    <tr>
      <td>West Nile Virus</td>
      <td>down</td>
      <td>0</td>
      <td>0</td>
      <td>1.000</td>
      <td>0 (0, 884.62)</td>
    </tr>
    <tr>
      <td>E. coli</td>
      <td>up</td>
      <td>84</td>
      <td>52.4</td>
      <td>&lt;0.0001</td>
      <td>1.9 (1.45, 2.47)</td>
    </tr>
    <tr>
      <td>E. coli</td>
      <td>down</td>
      <td>24</td>
      <td>20.7</td>
      <td>0.397</td>
      <td>1.2 (0.73, 1.90)</td>
    </tr>
    <tr>
      <td>Mycoplasma</td>
      <td>up</td>
      <td>16</td>
      <td>8.4</td>
      <td>0.010</td>
      <td>2.1 (1.14, 3.62)</td>
    </tr>
    <tr>
      <td>Mycoplasma</td>
      <td>down</td>
      <td>0</td>
      <td>0.1</td>
      <td>1.000</td>
      <td>0 (0, 47.56)</td>
    </tr>
    <tr>
      <td>Plasmodium</td>
      <td>up</td>
      <td>14</td>
      <td>9.8</td>
      <td>0.166</td>
      <td>1.53 (0.79, 2.77)</td>
    </tr>
    <tr>
      <td>Plasmodium</td>
      <td>down</td>
      <td>9</td>
      <td>3.2</td>
      <td>0.004</td>
      <td>3.44 (1.42, 7.57)</td>
    </tr>
  </tbody>
</table>

Logistic regressions with genes under selection in birds as the response variable and genes under selection in mammals, genes up or down-regulated in birds, and their interaction as predictor variables showed that for all categories, the selection status in mammals is the strongest predictor, followed by the transcriptional response in birds for some pathogens, but no significant interaction between the two (Table 4). Very few genes were under selection in birds and mammals and also differentially expressed in both clades at all FDR-

**Table 4.**
 Logistic regression results testing whether genes under selection in birds could be predicted by selection status in mammals (sig_mammals), transcriptional regulation in birds, or their interaction.


<table>
  <thead>
    <tr>
      <th>Pathogen</th>
      <th>Transcriptional response</th>
      <th>N genes</th>
      <th>Predictor variable</th>
      <th>Estimate</th>
      <th>Standard error</th>
      <th>Z score</th>
      <th>p-value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Influenza</td>
      <td>down</td>
      <td>4488</td>
      <td>sig_mammals</td>
      <td>0.76</td>
      <td>0.09</td>
      <td>8.45</td>
      <td>&lt;0.0001</td>
    </tr>
    <tr>
      <td>Influenza</td>
      <td>down</td>
      <td>4488</td>
      <td>down_reg_birds</td>
      <td>−0.12</td>
      <td>0.42</td>
      <td>−0.29</td>
      <td>0.771</td>
    </tr>
    <tr>
      <td>Influenza</td>
      <td>down</td>
      <td>4488</td>
      <td>sig_mammals: down_reg_birds</td>
      <td>−0.76</td>
      <td>0.85</td>
      <td>−0.89</td>
      <td>0.372</td>
    </tr>
    <tr>
      <td>Influenza</td>
      <td>up</td>
      <td>4488</td>
      <td>sig_mammals</td>
      <td>0.77</td>
      <td>0.09</td>
      <td>8.52</td>
      <td>&lt;0.0001</td>
    </tr>
    <tr>
      <td>Influenza</td>
      <td>up</td>
      <td>4488</td>
      <td>up_reg_birds</td>
      <td>0.79</td>
      <td>0.22</td>
      <td>3.69</td>
      <td>0.0002</td>
    </tr>
    <tr>
      <td>Influenza</td>
      <td>up</td>
      <td>4488</td>
      <td>sig_mammals: up_reg_birds</td>
      <td>−0.88</td>
      <td>0.5</td>
      <td>−1.77</td>
      <td>0.077</td>
    </tr>
    <tr>
      <td>West nile virus</td>
      <td>down</td>
      <td>3774</td>
      <td>sig_mammals</td>
      <td>0.77</td>
      <td>0.1</td>
      <td>7.76</td>
      <td>&lt;0.0001</td>
    </tr>
    <tr>
      <td>West nile virus</td>
      <td>down</td>
      <td>3774</td>
      <td>down_reg_birds</td>
      <td>11.98</td>
      <td>196.97</td>
      <td>0.06</td>
      <td>0.952</td>
    </tr>
    <tr>
      <td>West nile virus</td>
      <td>down</td>
      <td>3774</td>
      <td>sig_mammals: down_reg_birds</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
      <td>-</td>
    </tr>
    <tr>
      <td>West nile virus</td>
      <td>up</td>
      <td>3774</td>
      <td>sig_mammals</td>
      <td>0.77</td>
      <td>0.1</td>
      <td>7.76</td>
      <td>&lt;0.0001</td>
    </tr>
    <tr>
      <td>West nile virus</td>
      <td>up</td>
      <td>3774</td>
      <td>up_reg_birds</td>
      <td>1.1</td>
      <td>0.87</td>
      <td>1.27</td>
      <td>0.203</td>
    </tr>
    <tr>
      <td>West nile virus</td>
      <td>up</td>
      <td>3774</td>
      <td>sig_mammals: up_reg_birds</td>
      <td>−1.46</td>
      <td>1.66</td>
      <td>−0.88</td>
      <td>0.378</td>
    </tr>
    <tr>
      <td>E. coli</td>
      <td>down</td>
      <td>4225</td>
      <td>sig_mammals</td>
      <td>0.74</td>
      <td>0.09</td>
      <td>7.95</td>
      <td>&lt;0.0001</td>
    </tr>
    <tr>
      <td>E. coli</td>
      <td>down</td>
      <td>4225</td>
      <td>down_reg_birds</td>
      <td>−0.16</td>
      <td>0.19</td>
      <td>−0.83</td>
      <td>0.409</td>
    </tr>
    <tr>
      <td>E. coli</td>
      <td>down</td>
      <td>4225</td>
      <td>sig_mammals: down_reg_birds</td>
      <td>0.18</td>
      <td>0.5</td>
      <td>0.36</td>
      <td>0.717</td>
    </tr>
    <tr>
      <td>E. coli</td>
      <td>up</td>
      <td>4225</td>
      <td>sig_mammals</td>
      <td>0.72</td>
      <td>0.1</td>
      <td>7.2</td>
      <td>&lt;0.0001</td>
    </tr>
    <tr>
      <td>E. coli</td>
      <td>up</td>
      <td>4225</td>
      <td>up_reg_birds</td>
      <td>0.24</td>
      <td>0.1</td>
      <td>2.39</td>
      <td>0.017</td>
    </tr>
    <tr>
      <td>E. coli</td>
      <td>up</td>
      <td>4225</td>
      <td>sig_mammals: up_reg_birds</td>
      <td>−0.03</td>
      <td>0.26</td>
      <td>−0.13</td>
      <td>0.895</td>
    </tr>
    <tr>
      <td>Mycoplasma</td>
      <td>down</td>
      <td>4059</td>
      <td>sig_mammals</td>
      <td>0.73</td>
      <td>0.09</td>
      <td>7.74</td>
      <td>&lt;0.0001</td>
    </tr>
    <tr>
      <td>Mycoplasma</td>
      <td>down</td>
      <td>4059</td>
      <td>down_reg_birds</td>
      <td>−0.59</td>
      <td>0.53</td>
      <td>−1.11</td>
      <td>0.266</td>
    </tr>
    <tr>
      <td>Mycoplasma</td>
      <td>down</td>
      <td>4059</td>
      <td>sig_mammals: down_reg_birds</td>
      <td>−0.06</td>
      <td>0.93</td>
      <td>−0.06</td>
      <td>0.948</td>
    </tr>
    <tr>
      <td>Mycoplasma</td>
      <td>up</td>
      <td>4059</td>
      <td>sig_mammals</td>
      <td>0.75</td>
      <td>0.1</td>
      <td>7.77</td>
      <td>&lt;0.0001</td>
    </tr>
    <tr>
      <td>Mycoplasma</td>
      <td>up</td>
      <td>4059</td>
      <td>up_reg_birds</td>
      <td>0.51</td>
      <td>0.21</td>
      <td>2.42</td>
      <td>0.016</td>
    </tr>
    <tr>
      <td>Mycoplasma</td>
      <td>up</td>
      <td>4059</td>
      <td>sig_mammals: up_reg_birds</td>
      <td>−0.71</td>
      <td>0.41</td>
      <td>−1.73</td>
      <td>0.084</td>
    </tr>
    <tr>
      <td>Plasmodium</td>
      <td>down</td>
      <td>3222</td>
      <td>sig_mammals</td>
      <td>0.74</td>
      <td>0.11</td>
      <td>6.86</td>
      <td>&lt;0.0001</td>
    </tr>
    <tr>
      <td>Plasmodium</td>
      <td>down</td>
      <td>3222</td>
      <td>down_reg_birds</td>
      <td>−0.02</td>
      <td>0.37</td>
      <td>−0.05</td>
      <td>0.961</td>
    </tr>
    <tr>
      <td>Plasmodium</td>
      <td>down</td>
      <td>3222</td>
      <td>sig_mammals: down_reg_birds</td>
      <td>0.01</td>
      <td>0.85</td>
      <td>0.01</td>
      <td>0.992</td>
    </tr>
    <tr>
      <td>Plasmodium</td>
      <td>up</td>
      <td>3222</td>
      <td>sig_mammals</td>
      <td>0.73</td>
      <td>0.11</td>
      <td>6.71</td>
      <td>&lt;0.0001</td>
    </tr>
    <tr>
      <td>Plasmodium</td>
      <td>up</td>
      <td>3222</td>
      <td>up_reg_birds</td>
      <td>0.19</td>
      <td>0.23</td>
      <td>0.85</td>
      <td>0.396</td>
    </tr>
    <tr>
      <td>Plasmodium</td>
      <td>up</td>
      <td>3222</td>
      <td>sig_mammals: up_reg_birds</td>
      <td>0.44</td>
      <td>0.87</td>
      <td>0.5</td>
      <td>0.614</td>
    </tr>
  </tbody>
</table>

corrected p-value cutoffs for significance, reducing power to detect signals of enrichment. However, a few genes with low FDR-corrected p-values selection cutoffs in both datasets (p<0.0001) were also up-regulated in response to influenza (PKR, PARP9, and MX1), up-regulated in response to West Nile virus (PKR), up-regulated in response to E. coli (F5), or down-regulated in response to E. coli (RAD9A).

Due to the small number of genes under selection and differentially expressed in both lineages, we also sought to test whether there was any difference in differential expression effect size (β values) between genes under selection in both lineages, genes under selection in birds, and genes not under positive selection. A difference in overall differential expression effect size might suggest the existence of general differences in gene expression patterns that might not be strong enough to produce significant signal at individual genes. For each gene, we calculated the harmonic mean of bird and mammal absolute, standardized β values in response to infection with each pathogen and compared the mean of each β distribution in the three selection categories with pairwise Mann-Whitney U-tests. We found that genes under selection in both lineages have larger β values than both other classes, particularly in response to viruses (Figure 8, Supplementary file 1 Table 13). Genes under selection in birds also have larger β values compared to genes not under selection in response to viruses, but not other pathogens.

![Figure 8.](https://cdn.elifesciences.org/articles/41815/elife-41815-fig8-v2.jpg)

**Figure 8.:** Groups of genes are defined as being under positive selection in both birds and mammals, in birds only, or neither birds nor mammals (not significant). Differential expression effect values for each gene are calculated as the harmonic mean of the absolute β values of birds and mammals. We compared the mean of each category to that of the other two categories within each pathogen with Mann-Whitney U-tests, and the significance-level for each test is indicated by asterisks. Comparisons with p>0.10 are left blank. Note that boxplot outliers are not depicted.

## Discussion

Here, we show that shared signatures of positive selection are consistent with pathogen-mediated selection. First, across birds, genes involved in immune system function, DNA replication and repair, lipid metabolism, and phototransduction are targets of positive selection. Most of these pathways can be directly or indirectly linked to immune response. Functional transcriptomic data independently validate these results, showing that gene up-regulated in response to pathogens contain a higher proportion of genes under positive selection than those not regulated by infection. These results hold true at a broader taxonomic scale. We not only show that genes under selection in birds are more likely to be under selection in mammals, but that these shared selected genes are enriched for immune system processes, and in particular those related to viral response. We find few genes differentially regulated and under positive selection in both birds and mammals, but those we found are known to interact directly with pathogens. We also find that genes under positive selection in both lineages have significantly larger overall differential expression effect values compared to those only under positive selection in birds or those not under positive selection. Our results point to pathogens, and in particular viruses, being the most consistent selective pressure across tetrapods.

### Pathogens drive shared signatures of selection across birds and mammals

The strong overlap in genes under positive selection in mammals and birds (Figure 6A), together with the functional enrichment and expression results, support the hypothesis that pathogens consistently target the same genes across deeper evolutionary timescales. Although there are some differences in the fine details between avian and mammalian immune systems (e.g. different TLRs are functionally similar in the types of pathogens they recognize (Kaiser, 2010; Chen et al., 2013), the overall immune responses are conserved between the clades (Kaiser, 2010). Schrom et al., 2018 theoretically demonstrated that there are a limited number of network architecture configurations that are both inducible and robust, and our results here further suggest that pathogens are constrained in how they can interact with these networks to suppress an immune response. Further work on signatures of selection in other tetrapod clades would help to distinguish whether the shared patterns of selection we observe are due to convergence or ancient shared tetrapod selection.

We also show that the same genes are likely to be up-regulated in response to pathogen infection (Table 3), despite significant differences in the overall transcriptomic study designs (Supplementary file 1 Table 11). We found few genes both differentially expressed and under positive selection in both lineages, although we did find a significant, but small tendency for genes under selection in both clades to be differentially expressed (Figure 8). Those genes we did find are either classic examples of well-documented host-pathogen arms races (PKR (Samuel et al., 2006; Rothenburg et al., 2009; Elde et al., 2009; Enard et al., 2016) and MX1 (Ferris et al., 2013)), or genes known to interact directly with pathogens or the immune response (PARP9 (Zhang et al., 2015), RAD9 (An et al., 2010), F5 (Brunder et al., 1997)), which are new candidates for genes that may be involved in host-pathogen arms races across tetrapods.

### Viruses produce the strongest signatures of pathogen-mediated selection

Our results highlight that shared signatures of selection are enriched for pathways annotated to interact with viruses compared to those that interact with other pathogens. We show similar findings with our differential expression results - the differences in shared levels of differential expression in birds and mammals are strongly significant for the viral infectious agents, and only marginally significant for the other infectious agents (Figure 8). There was also a stronger overlap in expressed genes for the viruses compared to the other two classes of pathogens (Table 3). Finally, the Influenza A and Herpes simplex pathways were significantly enriched for shared genes under selection (Figure 6B,C). There is a near universal tendency to switch hosts in viruses (Geoghegan et al., 2017; Shi et al., 2018) and retroviruses (Henzy et al., 2014), although there is some variation in the prevalence of host-switching in different viral families (Geoghegan et al., 2017). This tendency may drive shared selection pressures if viruses target common host genes across divergent species. Examples of host-switching will only increase as more viruses are sequenced. Across populations of Drosophila melanogaster, a recent study observed higher rates of adaptation in viral genes only, not immune genes in general, bacterial genes, or fungal genes (Early et al., 2017), suggesting that these results may be more general across broader organisms as well.

### Pathogens are a strong selective pressure in birds

Our pathway enrichment results and differential expression results imply that pathogens are one of the strongest selective pressures on amino acid sequence of protein coding genes in birds. Our site test results, which require the same sites to be under selection across species, suggest that host-pathogen interactions are constrained to target specific sites in the same genes in different species. Without these site constraints, genes may be under selection in many different lineages of birds, but there may also be much greater variation in molecular pathways under selection at more recent evolutionary timescales. Our PCAs of parameters of positive selection for each gene for each species support this hypothesis. Following PC1, axes of variation either separate clades of species (e.g. ratites, song birds), or specific lineages. Three previous studies that performed genome-wide scans for positive selection in specific bird lineages further support this hypothesis. First, Nam et al., 2010 compared positive selection acting on three avian lineages, and while 1751 genes were evolving more rapidly than average in one of these three lineages, only 208 were common to all. Backström et al., 2013 compared signatures of positive selection in two species of galliformes and two species of passerines, and found that only the passerine lineages showed GO enrichment with terms related to fat metabolism, neurodevelopment and ion binding. Finally, Zhang et al., 2014bfound evidence for positive selection in the three vocal-learning bird lineages enriched for neural-related GO terms.

Previous studies of immune gene evolution in birds focus on receptor genes known to be hotspots of host-pathogen co-evolution, the Toll-like Receptors (TLRs) and Major Histocompatibility Complex (MHC). Five of the 10 avian TLRs are present in our dataset, with TLRs 1A, 1B, 2A, and 2B likely filtered out due to their recent duplication and TLR21 likely filtered out due to missing data caused by sequencing difficulty (Alcaide and Edwards, 2011; Grueber et al., 2014). For the five TLRs in our dataset we observe that the M0 ω values are similar to those observed by a previous study (Alcaide and Edwards, 2011). In addition, our results confirm those of Alcaide and Edwards, 2011; Grueber et al., 2014, and Velová et al. (2018), which showed TLR5 as having the highest proportion of selected sites, and the endosomal TLRs (TLR3, TLR7) as having the smallest proportion of selected sites. These similarities from independent studies focusing on just a few genes give us additional confidence in the results of our larger dataset. Unfortunately, the complexity of the MHC genes means that they were not included in our dataset. However, a recent survey of selection across birds found selection for both classes of MHC loci (Minias et al., 2018), indicating that our overall patterns of selection likely hold true.

Receptor genes clearly have signatures of pathogen-mediated selection but signaling pathways (e.g. ECM-receptor interaction and cytokine-cytokine receptor interaction) and downstream genes in immune pathway are also under selection in our dataset. Pathogens have evolved many ways to avoid the host immune response, sometimes at receptors, but sometimes at signaling molecules or genes involved in other cellular processes (Finlay and McFadden, 2006; Randall and Goodbourn, 2008; Pichlmair et al., 2012; Quintana-Murci and Clark, 2013; Sironi et al., 2015). The strong signatures of positive selection we observe in these alternative pathways and locations suggest that pathogens not only consistently target the same sites in receptor genes, but also the same sites within genes with other functions. The gene with the highest proportion of significant lineages in birds as estimated by aBS-REL in the Influenza A pathway is not for a receptor gene, but a signaling gene – the gene TRIF, also known as TICAM1. TRIF is recruited by TLR3, a viral sensing TLR in birds, and activates a set of molecules that culminates in the activate of IRF7 or NF-κB (Santhakumar et al., 2017). This gene is under selection in 61% of avian lineages, one of the highest proportions in our dataset, and highlights that genes beyond the classically studied MHC loci and TLRs may be interesting candidates for future studies on the ecology and evolution of host-pathogen co-evolution.

### Non-immune functional pathways under positive selection in birds

In addition to pathways directly related to immune function, pathways related to DNA replication and repair were also significantly enriched for positively selected genes (Figure 3). However, positive selection in these pathways may also be indirectly related to immune functions. First, viruses frequently subvert these pathways (e.g. mismatch repair, non-homologous end-joining) to promote their own replication cycle (Chaurushiya and Weitzman, 2009; Luftig, 2014). Long-term antagonistic selection between hosts and viruses to control these pathways could produce long-term signatures of positive selection, as in immune pathways. In addition, these pathways promote chromosomal stability and remove damaged DNA bases. Birds are known for their compact genomes that show greater than average chromosomal stability (Zhang et al., 2014b), and a surprising paucity of transposable elements (TEs) (Cui et al., 2014; Zhang et al., 2014b; Kapusta and Suh, 2017). One effect on genome structure during the insertion of transposable elements is genome rearrangement due to homologous recombination (Kazazian, 2004). Cui et al. (2014) hypothesized that homologous recombination may be responsible for purging transposable elements from the genome, and even observed a galliform hepadnavirus in the process of being removed via homologous recombination. Current host-pathogen evolutionary arms races between birds and TEs are also observed in woodpeckers and allies (Piciformes). There is evidence of different CR1 families expanding at least three different times within the order, and purifying selection for polymorphic TEs in three closely related woodpecker species (Manthey et al., 2018). Finally, the Kapusta et al. (2017) observation that the non-recombining W chromosome and regions near centromeres had the highest TE richness also suggest that homologous recombination may allow natural selection to more efficiently remove insertions that are deleterious in the population. Our pathway enrichment results support this hypothesis, and the similar dynamics of positive selection at specific sites as those observed with immune gene pathways suggest that birds may experience a form of host-pathogen co-evolution with TEs.

Two other groups of pathways were enriched for positively selected genes, although these pathways did not have significantly more genes under selection than expected based on median gene lengths, suggesting some caution in interpretation is warranted. The first category, lipid metabolism, includes the steroid hormone biosynthesis pathway and linoleic acid metabolism pathway. Steroid hormone biosynthesis is known to be related to diverse life history strategies in birds (Hau et al., 2010), and linoleic acid, more common in seed-rich diets, is related to thermoregulation and can vary across habitats (Ben-Hamo et al., 2013; Andersson et al., 2015). These pathways could be under selection in the diverse set of species included in our dataset. However, these are also known to be factors modulating the immune system (Koutsos and Klasing, 2014), and pathogens are known to target cellular processes beyond the immune system (Pichlmair et al., 2012). Further study including additional life history characteristics may help distinguish between these two selective forces.

The second category, phototransduction, likely relates to different avian life histories and the visual needs associated with those life histories. The genetics of the avian visual system has traditionally focused on the evolution of the cone receptor genes, and specifically variation in the short wave sensitivity type one pigment, which has shifted multiple times between ultraviolet and short wavelengths throughout birds with a single amino acid change (Odeen and Hastad, 2003; Ödeen and Håstad, 2013). However, a comparison of retinal transcriptomes from owls, falcons, and hawks, groups that have visual systems adapted to low-light environments (e.g. nocturnal or crepuscular species) or with visual systems tuned for high visual acuity, found evidence for positive selection on phototransduction genes (Wu et al., 2016). The strong signal of positive selection across the broad array of species chosen for our dataset suggests that these genes may be broadly important across many species, and an in-depth analysis of species associated with specific visual needs may uncover additional information on the evolution of this important avian sensory system.

Finally, our PCA to identify groups of species that have the same genes under selection identified one principle component that separates species across the avian phylogeny (Figure 4), which is significantly correlated with body mass (Figure 5). By correlating the parameter estimates for each gene with body mass to identify the genes driving this correlation, we find that the FoxO signaling pathway and weakly, the cellular senescence pathway were associated using gene set enrichment (Supplementary file 1 Table 8). Lifespan is one trait that is highly correlated with body mass (Furness and Speakman, 2008), FoxO proteins are linked to the aging process (Martins et al., 2016), and cellular senescence may be linked to lifespan through telomere dynamics (Monaghan and Haussmann, 2006; de Magalhães and Passos, 2018). Within a species, telomeres typically degrade as an organism ages, but few interspecific studies have found a correlation between telomere length and lifespan (Monaghan and Haussmann, 2006). However, a recent comparative study in birds showed that telomeres shortened more slowly in species with longer lifespans, and that these results are conserved within families (Tricola et al., 2018). A study of genes associated with telomeres in mammals did not find any correlation between the strength of positive selection at these loci and body mass (Morgan et al., 2013). Our results, and the unique pattern of telomere lengthening observed in birds may be an ideal system to study the evolution of telomere dynamics, and the molecular underpinnings of these processes. Finally, telomere length mediates lifespan and lifetime fitness, both of which are reduced due to chronic malaria infection (Asghar et al., 2015), and suggests that this lineage-specific signature of selection may also be related to pathogen-mediated selection.

### Conclusions and implications

Across birds, and more generally across tetrapods, there is a clear signal of positive selection acting on immune genes, whether against pathogens or transposable elements. Our results demonstrate that the same genes and potentially even the same codons may be shared targets of pathogens to subvert the immune response across not just species but also tetrapod Classes (mammals, birds). Genes with particularly strong evidence of selection may be good candidates for further study from a functional and ecological perspective, and could broaden perspectives on the ecology and evolution of immunity beyond MHC loci and TLRs typically examined. From an applied perspective, there is a great need to understand which proteins or genes in immune gene networks are important in pathogen resistance to improve breeding strategies in economically important species (e.g. poultry; (Kaiser, 2010). Our work is a first step in this direction, and we provide a rich resource for the examination of specific genes and pathways.

Here we have only considered positive selection at a broad scale. Combining these results with those from populations or specific clades within birds and mammals may provide new insights on similarities or differences in long and short-term selection. Pathogen load is the strongest driver of local adaptation in humans (Fumagalli et al., 2011) and viruses are important drivers of population adaptation in flies (Early et al., 2017). From a network perspective, functional gene pathways under strong selection in humans are directly or indirectly involved in immunity (Daub et al., 2013). Given the signatures of host-pathogen co-evolution we observe across birds, we expect that pathogens are an important driver of recent adaptation in bird populations as well.

## Materials and methods

### Identification, alignment and filtering of avian orthologs

Avian orthologs were identified, aligned, and filtered by Sackton et al. (2018). We provide a brief outline of the methodology here, but full details and computer code can be found in Sackton et al. (2018). The program OMA v.1.0.0 (Roth et al., 2008; Altenhoff et al., 2013) was used to infer patterns of homology among protein-coding genes across 39 sequenced bird (Figure 1) and three non-avian reptile (Alligator mississippiensis, Anolis carolinensis, and Chrysemys picta) genomes. For each gene set, the longest transcript was selected to represent that protein in the homology search.

Once OMA had completed, alignments were built for each OMA-defined homologous group using MAFFT v.7.221 (Katoh and Standley, 2013), RRID:SCR_011811), and a HMM was built for each protein alignment using HMMER v. 3.1b hmmbuild (Johnson et al., 2010), RRID:SCR_005305). Each HMM was then used to search the full set of OMA input both to verify that the same proteins were recovered as belonging to a homologous group, and to assign unassigned proteins if possible. Finally, a graph-based algorithm was used to add gene models not assigned to any OMA group to the best match if possible. This produced a new set of homologous groups, which we use in the following analyses.

These 45,367 hierarchical orthologous groups, or HOGs, were filtered to retain 16,151 HOGs with sequences for at least four species. Protein sequences were aligned with MAFFT v. 7.245 (Katoh and Standley, 2013), and filtered in three steps. First, entire columns were excluded if missing in more than 30% of species, had sequence in fewer than 10 taxa, or was missing in two of the three of the main taxonomic groups (paleognaths, neognaths, or non-avian outgroups). Second, poorly aligned regions were masked according to Jarvis et al. (2014) using a sliding-window similarity approach. Third, columns were removed using the same criteria as the first round. Next, entire sequences were removed from each alignment if they were over 50% shorter than their pre-filtered length or contained excess gaps. Finally, entire HOGs were removed if they contained more than three sequences for any species, did not have more than 1.5x sequences for the given number of species present in the alignment, or were less than 100 base pairs long. Nucleotide sequences for all remaining HOGs were aligned with the codon model in Prank v. 150803 (Löytynoja and Goldman, 2008). In total, 11,247 HOGs remained after all alignment and filtering steps.

Guide trees for use in the tests of selection were constructed for each alignment with RAxML v. 8.1.4 (Stamatakis, 2014), RRID:SCR_006086) under a GTR + GAMMA substitution model, partitioned into codon positions 1 + 2 and 3, with 200 rapid bootstrap replicates and a maximum likelihood tree search. In cases where species had more than one sequence in the alignment, we included all copies to produce a gene tree for that HOG.

### Tests of selection

Once HOGs had been identified and filtered, we considered them as representatives for genes, and so will refer to them as genes. To identify positively selected genes, we compared models of nearly neutral evolution to those that included signatures of positive selection at a proportion of sites across lineages in the avian phylogeny. Sites under positive selection are defined as those with elevated nonsynonymous/synonymous substitution ratios (ω = dN/dS) compared to the expectation under neutral evolution, ω = 1. We used two different programs to identify genes with evidence for elevated ω values at specific sites across avian lineages. First, we used the site models (Nielsen and Yang, 1998; Yang et al., 2000) implemented in the program Phylogenetic Analysis by Maximum Likelihood v4.8 (PAML, RRID:SCR_014932; (Yang, 2007)) to calculate likelihood scores and parameter estimates for seven models of evolution (Table 1). Because some genes contained gene duplicates, we ran all analyses of selection on gene trees from all 11,247 genes, and separately on the species tree for 8,699 genes that had a maximum of one sequence per species. We used the species tree generated by OMA from Sackton et al. (2018) as the phylogenetic hypothesis. First, we fit the M0 model, which estimates a single ω for all sites in the alignment. We used the branch lengths estimated with the M0 model as fixed branch lengths for subsequent models to decrease computational time. To identify genes with evidence of positive selection, we conducted likelihood ratio tests between neutral models and selection models (models with ω > 1). We compared likelihood scores from the M1a vs. M2a, M2a vs. M2a_fixed, M7 vs. M8, and M8 vs. M8a models (Supplementary file 1 Tables 2,3) (Nielsen and Yang, 1998; Yang et al., 2000; Wong et al., 2004b). We computed p-values according to a χ2 distribution with two, one, two, and one degree of freedom respectively.

In addition to the site tests implemented in PAML, we used BUSTED (Murrell et al., 2015), a modeling framework implemented in the program HyPhy (Pond et al., 2005), RRID:SCR_016162), to identify genes with evidence of positive selection at a fraction of sites. BUSTED uses a model that allows branch-to-branch variation across the entire tree (Murrell et al., 2015). Similar to the PAML models, BUSTED uses a likelihood ratio test to compare a model including selection (ω >1 at a proportion of sites) with one that does not. We parsed all PAML and HyPhy results with computer code (Shultz and Sackton, 2019; copy archieved at https://github.com/elifesciences-publications/avian-immunity) and ran all downstream analyses in R. For both sets of tests, we used the Benjamini-Hochberg approach to correct for multiple testing (Benjamini and Hochberg, 1995) with the p.adjust function in the stats packages in R v.3.5 (R Core Development Team, 2008). We considered an FDR-corrected p-value less than 0.05 as evidence for positive selection in that gene for a given model comparison.

Finally, in addition to testing for selection at particular sites across bird lineages, we used the aBS-REL method in HyPhy with default parameters (Kosakovsky Pond et al., 2011) to detect which specific lineages showed evidence of selection for each gene. For each lineage, including both tip species and internal branches, aBS-REL estimates a p-value for the presence of positive selection. We considered both the raw p-value as well as a p-value corrected for multiple testing within each gene. Fewer lineages showed evidence of selection with an FDR-corrected p-value, but all subsequent results were qualitatively consistent with both sets of tests. For simplicity and because the stringent correction may remove biologically-interesting lineages with weak to moderate selection, we present the results using the number of lineages considered nominally significant without multiple-test correction. We also used a script to parse all aBS-REL results and run all downstream analyses in R (Shultz and Sackton, 2019).

Previous work has found that alignment errors can result in substantial false positives (Markova-Raina and Petrov, 2011). However, our strict alignment filtering strategy and use of the evolution-aware PRANK aligner minimizes the possibility that our results are solely false positives (Markova-Raina and Petrov, 2011). Recombination also can elevate ω estimates, but the M7 vs M8 model has been shown to be robust to recombination (Anisimova et al., 2003), and these results give us the highest proportions of positively selected genes we observe in our dataset (Table 2). Finally, despite observing high proportions of selected genes, the overall trend of gene-wide estimates of ω <<1 is consistent with patterns of purifying selection on coding regions of the genome (Figure 2B). Furthermore the similarity in estimated ω values between this study and previous studies in birds with different sets of genome sequences or the use of pairwise estimates between chicken and zebra finch (Nam et al., 2010; Zhang et al., 2014a) give us confidence that our results are robust.

### Gene annotation

We annotated genes for downstream enrichment analyses using chicken (Gallus gallus assembly version 4.0; G.K.-S. Wong et al., 2004a) and zebra finch (Taeniopygia guttata assembly version 3.2.4; Warren et al., 2010) NCBI gene IDs from sequences of those species included in the alignment of each gene. Of the 11,247 HOGs, 10,889 could be assigned to a chicken NCBI gene id, 10,364 could be assigned to a zebra finch NCBI gene id, 10,142 could be assigned to both, and 136 could not be assigned to a chicken or zebra finch NCBI gene ID. In order to test additional pathways available for mammalian species (see below), we converted chicken and zebra finch NCBI gene IDs to human (Homo sapien; GRCh38.p10) NCBI gene IDs using the R biomaRt package version 2.36.1 (Durinck et al., 2005; Durinck et al., 2009). For both avian species, we downloaded the ENSEMBL gene IDs, NCBI gene IDs, and human homolog ENSEMBL gene IDs for each gene using the ggallus_gene_ensembl (chicken genes, Gallus-gallus-5.0) and tguttata_gene_ensembl (zebra finch genes, TaeGut3.2.4) datasets. For humans, we downloaded the ENSEMBL gene IDs and NCBI gene IDs from the human hsapien_gene_ensembl (human genes, GRCh38.p10) dataset. We assigned each gene by first identifying all human ENSEMBL gene IDs and NCBI gene IDs that were chicken orthologs, and filled in missing IDs with zebra finch annotations. In total, 9,461 out of 11,247 genes could be annotated with human NCBI gene IDs.

### Functional gene pathway enrichment for lineages under positive selection in birds

We looked for patterns of positive selection among groups of genes with similar functions using KEGG pathway enrichment tests (Kanehisa and Goto, 2000; Kanehisa et al., 2012), RRID:SCR_012773). We used our most conservative set of genes as our test set – those with FDR-corrected p-values less than 0.05 for all site tests (N = 1,521), including the m1a vs. m2a PAML model comparison, m2a vs. m2a_fixed PAML model comparison, m7 vs. m8a PAML model comparison, m8 vs. m8a PAML model comparison, and BUSTED analysis (see Table 1 for PAML model descriptions). Because of the similarity between the model results using gene trees and species trees (see Results), we use the gene tree results as input to maximize the number of genes that could be included in a functional analysis. Preliminary analyses using the species tree results are qualitatively similar to those presented here.

To conduct KEGG pathway enrichment analyses, we used the ‘enrichKEGG’ command from clusterProfiler v. 3.8.1 (Yu et al., 2012), RRID:SCR_016884) from Bioconductor v. 3.7 (Gentleman et al., 2004), RRID:SCR_006442) with chicken as the reference organism. We used the genes included in both PAML and HyPhy analyses with NCBI gene IDs (N = 10,874) as the gene universe for enrichment tests. To ensure genes not present in the chicken genome, but present in other bird species were not biasing our results, we also performed the functional enrichment test using zebra finch as the reference organism. Finally, we performed a final enrichment test using human as the reference organism to test whether the expanded KEGG pathways of humans could provide insights beyond those available for chicken and zebra finch. We visualized the results using modified versions of the ‘dotplot’ and ‘cnetplot’ commands in clusterProfiler.

We also tested whether median gene length for each pathway could explain our observed enrichment results. We used alignment length as a proxy for gene length, and first conducted a logistic regression with the selection status for each gene (under selection in all tests or not) as the dependent variable and alignment length as the independent variable. We then used the resulting model to estimate the probability of a gene identified as being under selection for each pathway based on median alignment length. We multiplied that probability by the number of genes in a pathway to calculate the expected number of genes under selection based on length alone, and compared that number to our observed value using a Fisher’s exact test.

### Clustering genes under selection among bird lineages

We used aBS-REL results to understand how groups of species that experience similar selective pressures might show evidence for positive selection for the same genes. To do this, we created matrices of the parameter estimates (proportion of sites under selection, ω) at each gene for each species. Because some ω estimates were at the boundary value, we set all ω estimates greater than 10,000 to 10,000. We also replaced any non-significant (p-value>0.05) parameter estimates with an ω value of 1, and proportion of sites under selection value of 0. We used these matrices to conduct principle components analyses (PCA) to cluster species by either the proportion of sites under selection or the log-transformed ω value of each species for each gene. We replaced any missing values with the mean parameter estimates for that gene, log-transformed ω values, and performed the PCA with the prcomp function in R.

Only the first principle component grouped unrelated species consistently among parameters and gene trees or species trees (see Results), so we tested whether PC1 might be related to body mass, a measurement correlated with many life history characteristics (Pienaar et al., 2013). We extracted body mass measurements from each species using the CRC Handbook of Avian Body Masses (Dunning, 2009) and used phylogenetic generalized least squares (PGLS) (Martins and Hansen, 1997) to test for a correlation between the PC1 scores and log-transformed body mass. To obtain branch lengths for our species tree topology, we randomly selected one gene with one sequence for all species and used the branch lengths as calculated by the M0 model in PAML. Our results were robust to tests with alternative genes. We ran the PGLS analysis in R with the gls function from the nlme package 3.1–137 (Pinheiro et al., 2013), RRID:SCR_015655), with a both a Brownian motion (Felsenstein, 1985) and an Ornstein-Uhlenbeck (Hansen and Martins, 1996) model of evolution. A Brownian motion fit better than the Ornstein-Uhlenbeck model (AIC > 2), so we report those results. However, the results are qualitatively similar. We visualized the two traits and the phylogeny using the ‘phylomorphospace’ function and the evolution of PC1 on the phylogeny using the a modified version of the ‘plotBranchbyTrait’ function from phytools v. 0.6–44 (Revell, 2012), RRID:SCR_015502).

To better understand which genes and molecular functions were contributing to the correlation between PC1 and body mass (see Results), we calculated a p-value for the association between the proportion of sites under selection and log-transformed body mass, and log-transformed ω values and log-transformed body mass for each gene separately. Due to the non-normal distribution of parameter estimates, we used Spearman’s rank correlation with the cor.test function from the stats package in R (R Core Development Team, 2008). Although Spearman’s rank correlation does not include phylogenetic correction, the aBS-REL p-values are estimated independently for each branch, and so should not be biased by phylogeny. We used the Benjamini-Hochberg approach to correct for multiple testing (Benjamini and Hochberg, 1995).

We tested whether there might be any functional signal in these genes using gene set enrichment with the Spearman’s rank correlation values (ρ) as the input for each gene. To avoid biases in genes with only one or a few lineages under selection, we only tested genes with at least five lineages under selection (preliminary results with alternative cutoff suggest that results are robust to the specific cutoff used). We tested for gene set enrichment with the chicken KEGG pathways using the ‘gseKEGG’ command from clusterProfiler (Yu et al., 2012).

### Comparisons of avian and mammalian selection datasets

In order to identify shared signatures of selection in both birds and mammals, we compared our results to those of Enard et al., 2016. We used our BUSTED results as calculated using the species tree to ensure our results were comparable to their BUSTED tests of positive selection. We combined our datasets using the human ENSEMBL gene ID annotations (conversion methods described above). In total, we could identify 4,931 orthologous genes with results from both datasets. With the set of genes included in both studies, we re-calculated FDR-corrected p-values, and compared the proportion of genes significant in both birds and mammals with a p-value cutoff of 0.1, 0.01, 0.001 and 0.0001 to understand whether genes under weak or strong selection might produce different signals. We calculated significance of an increased overlap in genes under selection in both birds and mammals with a Fisher’s exact test. We repeated this analysis after removing the 20% most constrained genes, defined here as the 20% of genes with the lowest m0 model ω values, to ensure that results were not driven by the reduced power to detect selection in constrained genes. We also tested whether an overlap in genes significant in both clades could be explained by gene length. To do this, for each p-value cutoff, we conducted a logistic regression with the selection status in mammals (significantly under selection or not according to the p-value cutoff) as the response variable, and the selection status in birds, alignment length, and their interaction as independent variables.

We tested whether pathogen-mediated selection might be an important factor in driving the overlap of these genes using KEGG pathway enrichment. We ran these tests as described above, with the genes under positive selection in both birds and mammals as the test set of genes, and the set of genes under selection in birds as the background set of genes. We used the four different FDR-corrected p-value cutoffs (p<0.1, 0.01, 0.001, or 0.0001) to identify genes under selection in each clade. Finally, we used permutation tests to ensure that our pathway enrichment results were not biased toward genes commonly under selection in birds. We randomly created test sets the same size as those empirically defined from the set of genes significant in birds and performed KEGG pathway enrichment. We calculated the enrichment score (proportion of selected genes in the pathway compared to the proportion of selected genes in the dataset) for each pathway significant in our bird-only results (described in above section) and included in our test of empirical data. That is, the pathway had to be significant in birds, and contain at least one gene under selection in both birds and mammals. We performed each permutation for each p-value cutoff 1000 times to generate a null distribution of enrichment values to compare to our empirical results.

### Association of genes under positive selection to pathogen-mediated transcriptional responses in birds

We independently tested whether genes under positive selection throughout birds were associated with pathogen-mediated immune responses using publicly-available transcriptome data. We tested whether genes that were differentially expressed in response to a pathogen challenge were more likely to be under positive selection. We identified 12 studies of birds that compared the transcriptomes of control individuals and individuals experimentally infected with a virus, bacterium or protist (Supplementary file 1 Table 11; (Smith et al., 2015a; Smith et al., 2015b; Sun et al., 2015a; Sun et al., 2015b; Videvall et al., 2015; Sun et al., 2016; Beaudet et al., 2017; Deist et al., 2017a; Deist et al., 2017b; Newhouse et al., 2017; Zhang et al., 2018). We downloaded all available SRA files for each bioproject and extracted the fastq files with fastq-dump from SRA-Tools v. 2.8.2.1 (Leinonen et al., 2011). We used kallisto v. 0.43.1 (Bray et al., 2016), RRID:SCR_016582) to quantify transcript abundance with 100 bootstrap replicates. We used paired-end or single-end mode (assuming average fragment lengths of 250 base pairs with a standard deviation of 50 base pairs) as appropriate for each bioproject, using the ENSEMBL transcriptome reference for each species (Supplementary file 1 Table 11). One species did not have an ENSEMBL reference available (Spinus spinus), so we mapped to the transcriptome reference of the closest available reference, Serinus canaria, downloaded from NCBI.

We tested for differential expression between experimentally infected individuals and control individuals with sleuth v0.30 (Pimentel et al., 2017), RRID:SCR_016883). In cases where individuals were available at different timepoints, had different phenotypes (e.g. resistant or susceptible), used different pathogen strains, or sequenced transcriptomes from different organs, we tested each condition separately. We considered a gene to be significantly differentially expressed if it had a q-value less than 0.05 and an effect size, quantified as the absolute value of β, greater than 1. We then combined results for each condition of each bioproject. We considered a gene to be differentially expressed for that study if it was significant in half of conditions defined as different time points and phenotypes for each organ (Supplementary file 1 Table 11). For three studies, only a single condition had any appreciable signal, we use used a relaxed our cutoff to count a gene as significant if it was significantly differentially expressed in any condition (Supplementary file 1 Table 11).

To compare genes across species, we translated all ENSEMBL gene IDs to homologous chicken ENSEMBL gene IDs from the R biomaRt package version 2.36.1 (Durinck et al., 2005; Durinck et al., 2009), RRID:SCR_002987), except for S. canaria, which we translated to chicken gene IDs by mapping genes IDs to sequences in the same gene alignments in our dataset. Some pathogens were represented by more than one study in our dataset. To combine the results for each pathogen, we considered each gene to be significant for that pathogen if it was significant in at least one study. We used logistic regression to test whether genes that were up-regulated (compared to no difference in transcription) were more likely to be under selection in birds (defined in above section), and to test whether genes that were down-regulated were more likely to be under selection in birds.

### Comparisons of gene expression patterns and positively selected genes in birds and mammals

Finally, we compared the pathogen-mediated transcriptional responses in birds to those in mammals. We used 14 previously published studies that generated transcriptomes for control individuals and pathogen-challenged individuals to identify differentially expressed genes in response to pathogen infection for a species of mammal (Supplementary file 1 Table 11; (Qian et al., 2013; Langley et al., 2014; Ogorevc et al., 2015; Rojas-Peña et al., 2015; DeBerg et al., 2016; Lee et al., 2016; Tran et al., 2016; Chopra-Dewasthaly et al., 2017; de Jong et al., 2018). We chose studies that used similar pathogens as those used in the avian experiments to compare the expression profiles of the two clades as closely as possible, while acknowledging that such matching will necessarily be somewhat imprecise. We used the same preprocessing steps as described in the above avian transcriptomic section. In two studies, seven and nine different timepoints were used, with a large number of individuals giving increased power to detect differentially expressed genes. For these two studies, we required genes to be significant in half of all timepoints as well as overall (all infected individuals compared to control individuals). We translated all non-human ENSEMBL gene IDs to human ENSEMBL gene IDs using biomaRt to compare results across all bird and mammal species. Finally, for birds and for mammals, we summarized results for each gene for each infectious agent, considering a gene to be differentially expressed if it was differentially expressed in any study. Despite the smaller number of genes identified in the joint bird and mammal datasets, results comparing the enrichment in bird-only studies as described above were robust (results not shown), so we have confidence that our combined bird and mammal dataset captured the signal observed with birds alone.

With our combined bird and mammal dataset, we first tested whether genes up-regulated in infected birds were also likely to be up-regulated in infected mammals, or whether genes down-regulated in infected birds were also likely to be down-regulated in infected mammals. We used a Fisher’s exact test to test whether the proportions of up- or down- regulated genes in both clades deviated from null expectations. Then, we combined the gene expression results with the significance results across birds and mammals. We sought to test whether genes that were under positive selection in birds were likely to be under positive selection in mammals and differentially expressed (either up- or down-regulated in both clades). To do this, for each pathogen, we used logistic regression with genes under selection in birds as the response variable (under selection or not), and the mammalian selection status (under selection or not), the differential expression status in birds (up- or down-regulated), and their interaction as predictor variables. Finally, due to the variety of experimental setups and small number of genes up- or down-regulated in both birds and mammals, we used a more sensitive test to test whether the absolute value of mammal and bird β values were significantly higher in genes under selection in both lineages, or genes under selection in birds, compared to genes not detected as being under selection with our BUSTED site tests. A larger absolute value of β implies larger magnitudes of differential expression, regardless of the direction of selection or q-value significance. To ensure the β values were as comparable as possible among studies, we first standardized the β values to have a mean of 0 and standard deviation of 1 for each study. Then, for pathogen replicates within birds and mammals, we used the maximum β value observed as the bird or mammal β value for that gene (results were robust if the mean β value was used instead). For each gene, we calculated the harmonic mean of bird and mammal β values, and used a Mann-Whitney U-test to test whether mean β values were significantly different between genes under selection (q-value < 0.05) in birds and mammals and genes under selection in birds only, between genes under selection in birds and mammals and genes not under selection in either lineage, and between genes under selection in birds only and genes not under selection in either lineage.
