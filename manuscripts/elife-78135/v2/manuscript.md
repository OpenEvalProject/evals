# Admixture of evolutionary rates across a butterfly hybrid zone

## Authors

- Tianzhu Xiong<sup>1</sup> ([ORCID: 0000-0002-4576-8764](https://orcid.org/0000-0002-4576-8764)) †
- Xueyan Li<sup>2</sup>
- Masaya Yago<sup>3</sup>
- James Mallet<sup>1</sup> ([ORCID: 0000-0002-3370-0367](https://orcid.org/0000-0002-3370-0367))

### Affiliations

1. Department of Organismic and Evolutionary Biology, Harvard University Cambridge United States ([ROR:03vek6s52](https://ror.org/03vek6s52))
2. Kunming Institute of Zoology, Chinese Academy of Sciences Kunming China ([ROR:03m0vk445](https://ror.org/03m0vk445))
3. The University Museum, The University of Tokyo Tokyo Japan ([ROR:057zh3y96](https://ror.org/057zh3y96))

† Corresponding author

## Abstract

Hybridization is a major evolutionary force that can erode genetic differentiation between species, whereas reproductive isolation maintains such differentiation. In studying a hybrid zone between the swallowtail butterflies Papilio syfanius and Papilio maackii (Lepidoptera: Papilionidae), we made the unexpected discovery that genomic substitution rates are unequal between the parental species. This phenomenon creates a novel process in hybridization, where genomic regions most affected by gene flow evolve at similar rates between species, while genomic regions with strong reproductive isolation evolve at species-specific rates. Thus, hybridization mixes evolutionary rates in a way similar to its effect on genetic ancestry. Using coalescent theory, we show that the rate-mixing process provides distinct information about levels of gene flow across different parts of genomes, and the degree of rate-mixing can be predicted quantitatively from relative sequence divergence (FST) between the hybridizing species at equilibrium. Overall, we demonstrate that reproductive isolation maintains not only genomic differentiation, but also the rate at which differentiation accumulates. Thus, asymmetric rates of evolution provide an additional signature of loci involved in reproductive isolation.

## Introduction

DNA substitution, the process whereby single-nucleotide mutations accumulate over time, is a critical process in molecular evolution. Both molecular phylogenetics and coalescent theory rely on observed mutations (Yang and Rannala, 2012; Wakeley, 2016), and so the rate of substitution/mutation is the predominant link from molecular data to information about the timing of past events (Bromham and Penny, 2003). Substitution rates often vary among lineages: generation time, spontaneous mutation rate, and fixation probabilities of new mutations could all contribute to the variation of substitution rates (Ohta, 1993; Lynch, 2010). Recent evidence suggests mutation rates are even variable among human populations (Harris, 2015; DeWitt et al., 2021). As such variation affects how fast the molecular clock ticks, reconstructing gene genealogies among different species sometimes accounts for species-specific rates of evolution (Lepage et al., 2007). However, under the standard coalescent framework, empirical studies of within- and between-species variation tend to ignore rate variation among populations (Costa and Wilkinson-Herbots, 2017; Wolf and Ellegren, 2017; Kautt et al., 2020). The latter is partly based on a popular assumption in coalescent theory that neutral mutation rate is constant for a given locus across the whole genealogy (Hudson, 1990). Hybridization and speciation lie in the gray zone of these extremes, and have their own problem: molecular clocks from different lineages could be mixed by cross-species gene flow — a gene could evolve under one clock before it flows into another species and switches to evolve according to a different clock (Figure 1). This mixing process is largely outside the scope of existing theories and has received little attention from empirical studies.

![Figure 1.](https://cdn.elifesciences.org/articles/78135/elife-78135-fig1-v2.jpg)

**Figure 1.:** Each gray block represents a species with its species-specific substitution rate. Solid lines represent gene genealogies prior to coalescence, and horizontal jumps between species represent inter-specific gene flow. Dots are substitutions. When a gene sequence inherits mutations derived under multiple rates, the number of substitutions it carries will reflect a mixture of substitution rates among different species. If gene flow is strong, each lineage carries a similar number of substitutions; If gene flow is weak, genes evolve independently with species-specific rates, and the distribution of substitutions in each lineage will likely be skewed towards the distribution of species-specific substitution rates.

However, if mixing between molecular clocks exists and can be measured, its strength could carry information about gene flow, which is important for studying reproductive isolation between incipient species. Genomic regions responsible for reproductive isolation lead to locally elevated genomic divergence (“genomic islands”), often caused by linked genomic regions experiencing less gene flow (“barrier loci”; Nosil et al., 2009; Michel et al., 2010; Renaut et al., 2013; Payseur and Rieseberg, 2016). In studying a hybrid zone between two butterfly species, Papilio syfanius and Papilio maackii, we discovered evidence for unequal genome-wide substitution rates between the two species. Using this system, we investigate the interaction between unequal substitution rates and gene flow, and whether this interaction reveals new information on reproductive isolation.

As these butterflies are rare species, occurring in a remote region of China, and are hard to collect, we employed methods based on analysis of whole-genome sequences of a few specimens. We hope that these methods may prove of use in studying other rare or perhaps endangered species where few individuals can be sacrificed. Results will follow two parallel lines: first, we provide evidence that genomic islands are associated with barrier loci. Then we infer the existence of unequal substitution rates. Finally, using a coalescent model, we calculate the relationship between the magnitude of genomic islands and the degree of mixing between substitution rates in linked regions. Throughout the analysis, we assume reverse mutations are rare, so that higher substitution rates always lead to higher numbers of observed substitutions.

## Results

### Divergent sister species with ongoing hybridization

We sampled 11 males of P. syfanius and P. maackii across a geographic transect (Figure 2A, dashed lines) covering both pure populations (in the sense of being geographically far from the hybrid zone) and hybrid populations. We also include four outgroup species, two of which have chromosome-level genome assemblies (P. bianor, P. xuthus; Lu et al., 2019; Li et al., 2015), while the other two (P. arcturus, P. dialis) are new to this study. All samples were re-sequenced to at least 20× coverage across the genome and mapped to the genome assembly of P. bianor. Among sampled local populations, P. syfanius inhabits the highlands of Southwest China (Figure 2A, red region), whereas P. maackii dominates at lower elevations (Figure 2A, blue region) (see Figure 2—figure supplement 3 and Figure 2—source data 4 for the complete distribution). The two lineages form a spatially contiguous hybrid zone at the edge of the Hengduan Mountains (Figure 2B) with individuals exhibiting intermediate wing patterns (Figure 2A: purple dot, corresponding to population WN in Figure 2B). Consistent with previous results (Condamine et al., 2013), assembled whole mitochondrial genomes are not distinct between the two lineages (Figure 2C, Figure 2—source data 3), suggesting either that divergence was recent, or that gene flow has homogenized the mitochondrial genomes. However, the two species are likely adapted to different environments associated with altitude, as several ecological traits are strongly divergent (Kashiwabara, 1991; Figure 2—figure supplement 1). Similarly, between pure populations (KM and XY in Figure 2B), relative divergence ($F_{S⁢T}$) is also high across the entire nuclear genome (Figure 2D, Figure 2—source data 1). The $F_{S⁢T}$ on autosomes averages between 0.2–0.4, and on the sex chromosome (Z-chromosome) it reaches 0.78. A highly heterogeneous landscape of $F_{S⁢T}$ is accompanied by numerous islands of elevated sequence divergence ($D_{X⁢Y}$) and reduced genetic diversity ($\pi$) scattered across the genome (Figure 2—figure supplement 4, Figure 2—source data 2). Since animal mitochondrial DNA generally has higher mutation rates than the nuclear genome (Haag-Liautard et al., 2008), its low divergence between the two species are likely the result of gene flow. Overall, despite ongoing hybridization, genomes of the pure populations of P. syfanius and P. maackii are strongly differentiated.

![Figure 2.](https://cdn.elifesciences.org/articles/78135/elife-78135-fig2-v2.jpg)

**Figure 2.:** (A) The geographic distribution of P. syfanius (red) and P. maackii (blue). Scale-bar: 100 km. Dashed line is the sampling transect covering five populations (colored circles). (B) Elevation, climate, and sample sizes along the transect. (C) Mitochondrial tree with four outgroups. (D)$F_{S⁢T}$ across chromosomes (50 kb windows with 10 kb increments). The inset shows the estimated density of $F_{S⁢T}$ on each chromosome.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/78135/elife-78135-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** The mimicry polymorphism in P. syfanius. The occurrence of spotted and spotless forms matches local forms of poisonous swallowtails in the genus Byasa.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/78135/elife-78135-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Seasonal distributions of adults. Records with verifiable time information were used (must have months, but we also kept records with missing days or years). Records explicitly mentioning larvae, pupae or eggs were removed, and records from December to February were also removed since adults do not occur in winter. Together, there were 62 P. syfanius records and 3138 P. maackii records passing all filters. Then we estimated kernel density of variable (month +day/30). If day is missing, it was randomly picked among 1–30. Results show the average kernel density from 1000 repeated estimations.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/78135/elife-78135-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** Estimated geographic distribution of P. syfanius (red) and P. maackii ssp. han (blue) predicted by MaxEnt. Scale-bar represents 800 km.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/78135/elife-78135-fig2-figsupp4-v2.jpg)

**Figure 2—figure supplement 4.:** Window-based $D_{X⁢Y}$ and $\pi$ estimated for populations KM and XY.$D_{X⁢Y}$ and $\pi$ on chromosomes. This series of plots include genetic diversity $\pi$ (red: population KM; blue: population XY) and absolute sequence divergence $D_{X⁢Y}$ (gray: between populations XY and KM). $D_{X⁢Y}$ and $\pi$ are calculated on 10 kb non-overlapping windows. The horizontal axis has range (0 bp, $18\times10^{6}$ bp), and the vertial axis has range (0, 0.03). Empty regions are masked due to abnormal coverage.

### Genomic islands are associated with barrier loci

A natural question is whether genomic differentiation is associated with barrier loci and reproductive isolation. In other words, can $F_{S⁢T}$ variation be attributed to gene flow variation between sister species? We suspect that barrier loci likely exist, because sequence variation between pure populations suggests that elevated $F_{S⁢T}$ is associated with reduced $\pi$ and elevated $D_{X⁢Y}$ across autosomes (Figure 3A), as expected for hybridizing species (Irwin et al., 2018). The Z chromosome (sex chromosome) has the highest $D_{X⁢Y}$ and the lowest $\pi$ among all chromosomes (Figure 2—figure supplement 4), another characteristic of hybridizing species with barriers to gene flow (Kronforst et al., 2013).

![Figure 3.](https://cdn.elifesciences.org/articles/78135/elife-78135-fig3-v2.jpg)

**Figure 3.:** For all plots, pure populations refer to XY & KM, and hybrid population refers to WN. (A) Between pure populations, reduced diversity ($\pi$, showing values averaged between pure populations) is associated with increased divergence ($D_{X⁢Y}$) across autosomes (30 segments per chromosome). Error bars are standard errors. (B) The conceptual picture of entropy metrics on diploid, unphased ancestry signals. In a genomic window, between-individual entropy ($S_{b}$) measures local ancestry randomness among individuals, while within-individual entropy ($S_{w}$) measures ancestry randomness along a chromosomal interval. (C) Simulated behaviors of entropy in a simplified model of biparental local ancestry. Chromosomes are assumed to be spatially homogeneous, thus recombination rate is uniform among 1000 equally spaced SNPs, and adjacent SNPs have a single probability of ancestry disassociation. For each haplotype block with linked ancestry, its ancestry is randomly assigned according to the average contribution from each species. Each pair of haploid chromosomes are combined into an unphased ancestry signal before calculating entropy. The top plot assumes equal contribution from both species, and the bottom plot assumes ancestry disassociation probability = 0.001. Solid lines are average entropies across 1000 repeated simulations, and shaded areas represent averaged upper and lower deviations from the mean. (D) The joint range among entropy, $\pi$, and $D_{X⁢Y}$ across autosomes (20 segments per chromosome). Color range is normalized by the range of entropy in each plot. Gray represents higher entropy, and colored regions are associated with lower entropy. Heatmaps represent linear fits to the ensembles of points. (E) The correlation $ρ$ on autosomes between entropy in hybrid populations and {$\pi$, $D_{X⁢Y}$, $F_{S⁢T}$} within and between pure populations. $ρ$ is shown above each regression line. Error bars are standard errors of entropy from 50 repeated estimates of local ancestry using software ELAI (parameters are in Materials and methods). The significance of $ρ$ is estimated using block-jackknifing among all segments: $Z$-scores are shown in parentheses.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/78135/elife-78135-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** An example run of the local ancestry estimation software ELAI on chromosomes 1–30 of four diploid individuals from the hybrid population WN (generation parameter: 5000). Gray represents the ancestry contribution from P. maackii.

To test for the presence of barrier loci, we augment the analysis with the sequences of four individuals from the population closest to the center of the hybrid zone (Population WN). We investigate whether differences in ancestry variation provide additional evidence for barrier loci in this hybrid zone. The underlying logic is that barrier loci will simultaneously:

Effects 3 and 4 can be bundled together as “reduced ancestry randomness” around barrier loci because both are expected if intermixing of segments of different ancestries within a genomic interval is prevented. For effects 3 and 4, because of small sample sizes, estimating site-specific statistics such as pairwise linkage disequilibrium is untenable. However, our high-quality chromosome-level reference genome enabled accurate estimation of local ancestry. As a remedy for small sample sizes, we employ two entropy metrics borrowed from signal-processing theory to quantify ancestry randomness in local regions along chromosomes (see Materials and methods). By dividing chromosomes into segments, we can extract indirect information about effects 3 and 4 at the expense of reduced genomic resolution. The proposed metrics, $S_{b}$ and $S_{w}$, correspond to the randomness of ancestry between and within individual diploid genomes from a local population (Figure 3B). For a cohort of ideal chromosomes with uniform recombination and marker density, if ancestry is independent between homologous chromosomes, both $S_{b}$ and $S_{w}$ increase with reduced local ancestry correlation and more balanced parental contribution (Figure 3C).

For a given autosomal segment, we then calculate $\pi$, $D_{X⁢Y}$, and $F_{S⁢T}$ between pure populations, as well as entropy metrics $S_{b}$ and $S_{w}$ in hybrid individuals for the same segment. To investigate whether effects 1–4 are all present in our system, the joint range among entropy, $\pi$, and $D_{X⁢Y}$ is shown in Figure 3D, which suggests that low ancestry randomness (low entropy) is likely associated with reduced $\pi$ within species and elevated $D_{X⁢Y}$ between species. To further quantify such association, we estimated Pearson’s correlation coefficients ($ρ$) between entropy and the latter statistics (Figure 3E). These associations are strongly significant ($Z$-scores > 3). Consequently, reduced ancestry randomness in hybrids (effects 3 & 4) coincides with classical patterns of barrier loci between pure populations (effects 1 and 2). This analysis is not sufficient to exclude all alternative hypotheses. For instance, we cannot entirely exclude the possibility that patterns are driven by low-recombination regions ($S_{w},S_{b}↓$) that experience linked selection ($\pi↓$) also have elevated mutation rates ($D_{X⁢Y}↑$). Nonetheless, this alternative seems most unlikely, as low-recombination regions should typically be less rather than more mutable (Lercher and Hurst, 2002; Jensen-Seaman et al., 2004; Yang et al., 2015; Arbeithuber et al., 2015; Liu et al., 2017). Overall, adding information from hybrid populations strengthens the evidence for barrier loci acting across autosomes.

The Z chromosome was excluded from this analysis as it likely differs in mutation rate or effective population size (Presgraves, 2018), but its ancestry in hybrid individuals either retains purity or resembles very recent hybridization (long blocks of heterozygous ancestry, Figure 3—figure supplement 1). The Z chromosome has low ancestry randomness, and it also has the highest level of divergence (Figure 2D), both of which suggest strong barriers to gene flow between P. syfanius and P. maackii on this chromosome.

### Asymmetric site patterns

A hint that substitution rates differ between the two species comes from site-pattern asymmetry (but this asymmetry alone is insufficient to establish the existence of divergent rates). We focus on two kinds of biallelic site patterns. In the first kind, choose three taxa (P1,P2,O1), with P1=syfanius, P2=maackii, while O1 is an outgroup. Assuming no other factors, if substitution rates are equal between P1 and P2, then site patterns (P1,P2,O1)=(A,B,B) and (B,A,B) occur with equal frequencies, where “A” and “B” represent distinct alleles. This leads to a $D$ statistic describing the asymmetry between three-taxon site patterns:

$$
D_{3}=D_{P_{1},P_{2},O_{1}}=\frac{n_{ABB}−n_{BAB}}{n_{ABB}+n_{BAB}},
$$

where $n$ is the count of a particular site pattern across designated genomic regions. A significantly non-zero $D_{3}$ indicates strongly asymmetric distributions of alleles between P1 and P2.

In a second kind of site pattern test, we compare four taxa (P1,P2,O1,O2) and calculate a similar statistic between site patterns (A,B,B,A) vs (B,A,B,A):

$$
D_{4}=D_{P_{1},P_{2},O_{1},O_{2}}=\frac{n_{ABBA}−n_{BABA}}{n_{ABBA}+n_{BABA}}
$$

Classically, a significantly non-zero $D_{4}$ suggests that gene flow occurs between an outgroup and either P1 or P2, thus it is widely used to detect hybridization (the ABBA-BABA test) (Durand et al., 2011; Hibbins and Hahn, 2022). Here, $D_{4}$ is used more generally as an additional metric of site pattern asymmetry.

We compute both $D_{3}$ and $D_{4}$ on synonymous, nonsynonymous, and intronic sites, with P. syfanius and P. maackii samples taken from pure populations (KM and XY). For each type of site, we progressively exclude regions with local $F_{S⁢T}$ below a certain threshold, and report $D$ statistics on the remaining sites in order to show the increasing site-pattern asymmetry in more divergent regions (Figure 4). $D_{3}$ is significantly negative regardless of outgroup or site type for most $F_{S⁢T}$ thresholds, and $D_{4}$ is also significantly negative for most outgroup combinations when computed across the entire genome ($Z$-scores are shown in Figure 4—figure supplement 1), proving that site-patterns are strongly asymmetric between P. syfanius and P. maackii. Importantly, the direction of asymmetry is nearly identical across all outgroup comparisons. This asymmetry cannot be attributed to batch-specific variation as all samples were processed and sequenced in a single run, and variants were always called on all individuals of P. syfanius and P. maackii. Sequencing coverage is normal for most annotated genes used in the analysis (Table 1), suggesting that asymmetry is not due to systematic copy-number variation that could affect variant calls. Nonetheless, two independent processes of evolution could explain observed asymmetric site patterns. In hypothesis I (Figure 5A, left), asymmetry is generated via stronger gene flow between P. syfanius and outgroups, leading to biased allele-sharing. In hypothesis II, site pattern asymmetry is due to unequal substitution rates between P. syfanius and P. maackii, which is further modified by recurrent mutations in all four outgroups (Figure 5A, right). We test each hypothesis below.

![Figure 4.](https://cdn.elifesciences.org/articles/78135/elife-78135-fig4-v2.jpg)

**Figure 4.:** $D$ statistics are unanimously negative.For each data point, we choose an $F_{S⁢T}$ threshold (x-axis) and report $D$ statistics on SNPs with a background $F_{S⁢T}$ (50 kb windows and 10 kb increments) no less than the given threshold. Error bars are standard errors estimated using block-jackknife with 1 Mb blocks. The aberrant behavior for the highest $F_{S⁢T}$ bins is we believe mostly due to low sample sizes for these bins.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/78135/elife-78135-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** $D_{3}$, $D_{4}$ statistics plotted with their $Z$-scores.

**Table 1.**
 Coverage abnormality in SNPs from coding sequences (CDSs).Abnormal coverage is inferred if the average coverage of a CDS exceeds twice of the median coverage of all CDSs in the genome.


<table>
  <tbody>
    <tr>
      <td>Number of SNPs from CDSs with abnormal coverage</td>
      <td>1993</td>
    </tr>
    <tr>
      <td>Total number of SNPs from all CDSs</td>
      <td>1060525</td>
    </tr>
  </tbody>
</table>

![Figure 5.](https://cdn.elifesciences.org/articles/78135/elife-78135-fig5-v2.jpg)

**Figure 5.:** (A) Two hypotheses to explain negative $D$ statistics. (B) The percentage of local gene trees (50 kb non-overlapping windows) where P. syfanius and P. maackii are together monophyletic. For each level of support, we filter out windows with Support(monophyly) and Support(paraphyly) below a given level, and report both the percentage of windows passing the filter (informative windows) and the percentage of monophyletic windows. (C) The distribution of P. syfanius branch lengths ($L_{s}$) relative to those of P. maackii ($L_{m}$) among highly supported monophyletic trees (Support ≥95). Each curve corresponds to a pairwise comparison between a syfanius individual and a maackii individual. Branch lengths are distances from tips to the most-recent common ancestor of all syfanius +maackii individuals. (D) Behavior of $D_{3}$ under divergent substitution rates and recurrent mutations in outgroups (O1). (E) Behavior of $D_{4}$ under divergent substitution rates and recurrent mutations in outgroups (O1 & O2). (F) Left: Median $D_{3}$ is positively correlated with node height; Right: Median $D_{4}$ is negatively correlated with $(ΔNode height)/(ΣNode height)$. Node height is used as a proxy for the probability of recurrent mutation ($p_{i}$).

### Hybridization with outgroups does not explain site-pattern asymmetry

We first test hypothesis I by phylogenetic reconstruction using SNPs in annotated regions. We construct local gene trees for each 50 kb non-overlapping window for all samples, including the four outgroup species. As biased gene flow with outgroups should rupture the monophyletic relationship among all P. syfanius +P. maackii individuals, the fraction of windows producing paraphyletic gene trees can be used to assess the potential impact of gene flow. However, almost all gene trees show the expected monophyletic relationship (Figure 5B). This conclusion is independent of the level of support used to filter out genomic windows with ambiguous topologies (see Materials and methods). Consequently, hardly any window shows a phylogenetic signal of hybridization with outgroups. Nonetheless, branch lengths in reconstructed gene trees suggest possible substitution rate divergence between the two species: Among highly supported monophyletic trees (bootstrap support ≥ 95), P. maackii (in populations YA, BJ, XY) is always significantly more distant than P. syfanius from the most recent common ancestor of P. maackii +P. syfanius (Figure 5C, significance levels reported via a Wilcoxon signed-rank test for each pair of individuals, see Figure 5—source data 2). Second, the direction of allele sharing in the $D$ statistics is unanimously biased towards P. syfanius. If hypothesis I were true, hybridization with outgroups is required to take place mainly in the highland lineage. There is no evidence to support why the highland lineage should receive more gene flow based on current geographic distributions, as outgroups P. xuthus and P. bianor overlap broadly with both P. maackii and P. syfanius, while outgroup P. dialis is sympatric only with P. maackii (Condamine et al., 2013). Although it is possible that historical and modern geographic distributions differ, and archaic gene flow might have occurred preferentially with P. syfanius, it should still leave some phylogenetic signal of introgression. Overall, we find little evidence for biased hybridization required by hypothesis I.

One might worry that by rejecting hypothesis I, we also throw doubt on widely accepted conclusions of the ABBA-BABA test for gene flow in other systems (that a significantly nonzero $D_{4}$ implies hybridization with outgroups) (Durand et al., 2011). However, in the next section, we show why $D_{3}$ and $D_{4}$ are fully consistent with hypothesis II, and so this is just a special case where the ABBA-BABA test produces a false positive for gene flow.

### Evidence for divergent substitution rates

In hypothesis II, divergent substitution rates between P. maackii and P. syfanius interact with recurrent mutations in outgroups to produce asymmetric site patterns. To understand its effect on $D$ statistics, consider a simplified model of recurrent mutation (Figure 5D,E), where a site in outgroup $i$ mutates with probability $p_{i}$, producing the same derived allele with probability $c$. When averaged across the genome, $c$ can be treated as a constant, and $p_{i}$ increases with distance to the outgroup. In the absence of gene flow, for three-taxon patterns, recurrent mutations modify $D_{3}$ by a factor of approximately $(1-2⁢c⁢p_{1})$ (Figure 5D, see Materials and methods), and observed $D_{3}$ will thus be positively correlated with $p_{1}$. For four-taxon patterns, it can be shown that observed $D_{4}$ is always negative due to larger probabilities of recurrent mutation in more distant outgroups (Figure 5E, see Materials and methods). Assuming no significant contribution of incomplete lineage sorting (Maddison and Knowles, 2006), the value of $D_{4}$ becomes more negative with increasing $Δp_{i}/Σp_{i}=(p_{2}−p_{1})/(p_{2}+p_{1})$.

To test these signatures, we employ estimated node heights of outgroups in the mitochondrial tree (Figure 2C) as proxies for outgroup distance, and hence for the relative probability of recurrent mutation ($ρ_{i}$). In line with expected signatures, we find that observed $D_{3}$ indeed increases with node height (Figure 5F, left), and observed $D_{4}$ decreases with (Δ Node height/∑ Node height; Figure 5F, right). Thus, the directions and magnitudes of both $D$ statistics are congruent with hypothesis II. As hypothesis II naturally predicts unanimously negative $D_{3}$ and $D_{4}$ as well as their relative magnitudes among different outgroup combinations, it is more parsimonious than hypothesis I. Hence, divergent substitution rates likely exist between P. syfanius and P. maackii.

### Rate-mixing at migration-drift equilibrium

Having tested for the existence of divergent substitution rates, we now explore how they become mixed by gene flow using a coalescent framework. In particular, we will assess whether the conceptual picture in Figure 1 can be recovered quantitatively in the butterfly system. As gene flow is ongoing between the two lineages, consider two haploid populations of size $N$ exchanging genes at rate $m$ (Figure 6A). This simple isolation-with-migration (IM) model at equilibrium has relative divergence (Notohara, 1990)

$$
F_{ST}=\frac{1}{1+4Nm}
$$

![Figure 6.](https://cdn.elifesciences.org/articles/78135/elife-78135-fig6-v2.jpg)

**Figure 6.:** (A) Behavior of the equilibrium isolation-with-migration model with divergent substitution rates. If coalescence is weaker than gene flow, each lineage has a similar number of derived alleles. If coalescence is stronger than gene flow, lineages sampled from the population with a faster substitution rate will also inherit more derived alleles. (B) Theoretical relationship between observed rate ratio ($r$) and relative divergence ($F_{S⁢T}$), parameterized by the true ratio r0) of substitution rates. (C) Observed rate ratios between P. maackii (population XY) and P. syfanius (Population KM), partitioned by ten $F_{S⁢T}$ intervals. Error bars are standard errors calculated using 1 Mb block-jackknifing. (D) The theoretical relationship between $r$ and $F_{S⁢T}$ is a good fit to observation.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/78135/elife-78135-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** Symmetric migration models. Parameters: $N_{1}=10^{4}/6$, $\mu_{1}=3\times10^{-5}$ (substitution rate in the red species), $m=(0.1)^{Array(1.4:0.25:5.4)}$. Substitution rate in the blue species is determined by $r_{0}$. Theoretical curves appear to be exact. (106 repetitions).

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/78135/elife-78135-fig6-figsupp2-v2.jpg)

**Figure 6—figure supplement 2.:** Conservative migration models. Parameters: $N_{1}=10^{4}/6$, $\mu_{1}=3\times10^{-5}$ (substitution rate in the red species), $m=(0.1)^{Array(1.4:0.25:5.4)}$. Substitution rate in the blue species is determined by $r_{0}$. Theoretical curves are still robust, although less accurate (106 repetitions).

![Figure 6—figure supplement 3.](https://cdn.elifesciences.org/articles/78135/elife-78135-fig6-figsupp3-v2.jpg)

**Figure 6—figure supplement 3.:** Stepping-stone models. Parameters: $N=10^{4}/6$, $\mu_{1}=3\times10^{-5}$ (substitution rate in the red species), $m=(0.1)^{Array(1.4:0.25:5.4)}$. The blue species is three times slower in substitution. Within-species population structure dampens observed relationship below the theoretical curve (104 repetitions).

To quantify the signature of mixed rates, consider the asymmetry in observed numbers of substitutions (circles in Figure 6A). Take a pair of sequences from two populations. Let $⟨n_{1}⟩$ be the expected number of derived alleles exclusive to the sequence in population 1, and let $⟨n_{2}⟩$ be the same expected number in population 2. Their ratio is defined as observed rate ratio:

$$
r=\frac{⟨n_{2}⟩}{⟨n_{1}⟩}
$$

Evidently, $r=1$ is the symmetric point where both sequences have the same number of derived alleles. Further, let the actual substitution rate in population 1 be $\mu_{1}$, and the actual substitution rate in population 2 be $\mu_{2}$. The ratio between the two actual rates are defined as the true rate ratio:

$$
r_{0}=\frac{\mu_{2}}{\mu_{1}}
$$

At migration-drift equilibrium, observed rate ratio ($r$) and observed divergence ($F_{S⁢T}$) are related by the following formula parameterized singly by $r_{0}$ (Figure 6B, see Materials and methods):

$$
r=\frac{1+r_{0}+F_{ST}(r_{0}−1)}{1+r_{0}−F_{ST}(r_{0}−1)},
$$

which translates into

$$
F_{ST}≈\frac{r−1}{r_{0}−1}ifr_{0}≈1
$$

These formulae indicate that unequal substitution rates are more mixed in regions with lower genomic divergence. Equation 7 is surprising, because it reveals that the remaining fraction of substitution rate divergence ($(r-1)/(r_{0}-1)$) is almost the same as $F_{S⁢T}$, which corresponds to the fraction of genetic variance explained by population structure (Wright, 1949). In Figure 6B, the relationship between $r$ and $F_{S⁢T}$ is still largely linear when one species evolves three times as fast as its sister species ($r_{0}=3$), and so Equation 7 might be robust under biologically realistic rates of substitutions between incipient species. Using extensive simulations (Figure 6—figure supplement 1 to Figure 6—figure supplement 3), we show that the full formula (Equation 6) is also robust in a number of equilibrium population structures.

To test whether such predictions are met, we calculate $r$ on synonymous, nonsynonymous, and intronic sites partitioned by their local $F_{S⁢T}$ values between pure populations (KM & XY), and recover a similar monotonic relationship across most $F_{S⁢T}$ partitions (Figure 6C). For introns, the observed relationship between $r$ and $F_{S⁢T}$ is a near perfect fit to Equation 6 (Figure 6D, squares), with an estimated $r_{0}$ = 1.837. For synonymous (Figure 6D, circles) and nonsynonymous sites (Figure 6D, triangles), Equation 6 also provides an excellent fit in regions with low to intermediate $F_{S⁢T}$. Estimated $r_{0}$ for synonymous sites is 1.813, close to that of introns, while nonsynonymous sites have a considerably lower $r_{0}$ of 1.633. If introns and synonymous substitutions are approximately neutral, we infer that neutral substitution rates are about 80% greater in the lowland species.

## Discussion

### Entropy as a useful measure of ancestry randomness

A critical step in our analysis is to associate genomic islands with barrier loci. Conventionally, information on increased association between barrier sites in hybrid populations comes from two-locus linkage disequilibrium (Slatkin, 1975). Empirical studies on hybrid populations frequently use such statistics to strengthen the evidence for barriers to gene flow (Knief et al., 2019; Wang et al., 2022). Alternatively, if phased haplotypes can be sequenced, the length of ancestry tracts (Sedghifar et al., 2016) or the density of ancestry junctions (Janzen et al., 2018; Wang et al., 2022) also carry information on barrier loci. All these methods break down with small numbers of unphased samples, as forced phasing can produce a large number of false ancestry junctions. However, conventional notions such as “ancestry tract length” are not definable for unphased local ancestry. The dilemma forces us to consider more robust statistics that carry information on ancestry association even in unphased data.

The development of both entropy metrics follows three intuitions:

Since entropy carries information about the degree of ancestry correlation, it will decrease in regions of low recombination and high genetic relatedness. If genetic relatedness is produced by inbreeding, it should affect the entire genome in a similar way, and between-individual entropy ($S_{b}$) will be similar across different parts of the genome. However, if inbreeding is so severe that $S_{b}$ is globally zero, it will not be an informative metric. It is worth noting that within-individual entropy $S_{w}$ shares a conceptual similarity to the wavelet transform of ancestry signals (Pugach et al., 2011; Sanderson et al., 2015). These entropy metrics will be particularly useful for window-based genomic analysis of ancestry correlation with limited sampling, and they are also compatible with larger sample sizes and more than two parental species. (The formulae of entropy with two parental species are presented in Materials and methods, and mathematical details are discussed in Appendix 1.) Nonetheless, this entropy approach assumes local ancestry can be accurately inferred, which will be challenging for studies with low-coverage sequencing, non-chromosomal genome assembly, or lacking reference populations.

### Potential mechanisms of divergent substitution rates

Interestingly, a higher substitution rate in the lowland lineage P. maackii is congruent with the evolutionary speed hypothesis (Rensch, 1959), where evolution accelerates in warmer climates. Our finding echoes the results of many previous studies (Gillooly et al., 2005; Wright et al., 2006; Lin et al., 2019; Ivan et al., 2022). Without measuring the per-generation mutation rates in both species, it is unclear what mechanisms cause increased substitution rates, but the lowland lineage typically has an additional autumn brood that is absent in P. syfanius (Takasaki et al., 2007; Figure 2—figure supplement 2). Warmer temperatures in lowland habitats might also increase spontaneous mutation rates in ectothermic insects (Waldvogel and Pfenninger, 2021). Both mechanisms could produce increased substitution rates in the lowland species. It is surprising that estimated $r_{0}$ between synonymous sites and introns agree with each other under such a coarse framework, and estimated $r_{0}$ for nonsynonymous sites is considerably lower. Less asymmetric rates for nonsynonymous substitutions could perhaps be explained by the nearly neutral theory (Ohta, 1993), which argues that many nonsynonymous mutations are mildly deleterious, and selection is more efficient in suppressing them in larger populations and slowing down substitutions. In the field, the lowland species often appears in larger numbers with well-connected habitats, while the highland species faces a highly heterogeneous landscape of the Hengduan Mountains, which could lead to differences in effective population sizes required by our expectation under the nearly neutral theory.

### Are introgression tests robust to substitution rate variation?

An additional result from our study is that divergent substitution rates might produce spuriously non-zero $D_{4}$ statistics when combined with recurrent mutations, which could increase the false positive rate of the ABBA-BABA test (Durand et al., 2011). This phenomenon has been suspected in humans (Amos, 2020), and is certainly a theoretical possibility (Hibbins and Hahn, 2022), but has not been tested in most empirical studies.

A wide class of introgression tests targeting gene flow between outgroups and a pair of taxa are based on site pattern information. Hahn’s $D_{3}$ computes absolute sequence divergence between groups in a triplet of species (Hahn and Hibbins, 2019), and will be affected by unequal substitution rates in a similar way to our $D_{3}$. Martin’s $f_{d}$ computes the same numerator as our $D_{4}$ (Martin et al., 2015), so it could also produce false positives under similar situations. Related statistics include $D_{p}$ (Hamlin et al., 2020), $D_{f}$ (Pfeifer and Kapan, 2019). A general guideline for site-pattern based statistics is that the focal pair of taxa are closely related such that substitution rates do not differ, while outgroups should not be too distant to minimize recurrent mutations (Hibbins and Hahn, 2022). However, whether these assumptions are met in empirical studies is worthy of investigation, and our system provides a counterexample even between sister species with ongoing hybridization.

A separate pitfall might occur if introgression tests based on site-patterns are applied to genomic windows to locate regions introgressed from outgroups. In our case, $F_{S⁢T}$ peaks have the most asymmetric substitution rates between P. maackii and P. syfanius, thus they will most likely be associated with false-positive $D$ statistics. This could lead to the incorrect interpretation that some barrier loci (“speciation genes”) are introgressed from outgroups – a popular hypothesis in adaptive introgression and hybrid speciation, see Edelman and Mallet, 2021.

To this end, we speculate that using appropriate substitution models to infer gene tree topology will perform better in assessing the impact of introgression with outgroups.

### The conceptual picture of rate-mixing

In the gray zone of incomplete speciation, interspecific hybrids bridge between gene pools of divergent lineages (Mallet, 2005). We here demonstrate a similar role of hybridization in coupling and mixing differing substitution rates. Divergent rates of substitution carry information about outgroups, while divergence based on allele frequency differences does not. Preserving divergent substitution rates is a stronger effect than maintenance of allele frequency differences, because divergence of allele frequencies is a prerequisite for rate preservation. This dependency can be coarsely quantified across the genome by the relationship between observed rate ratio $r$ and relative divergence $F_{S⁢T}$ in an equilibrium system of hybridizing populations (Equation 6). At migration-drift equilibrium, it is not surprising that divergent substitution rates are associated with relative divergence. In Figure 6A, when coalescence occurs rapidly compared to gene flow, most substitutions separating individuals are species-specific. However, when gene flow is faster than coalescence, individuals will carry substitutions that occurred in both species. This could have important implications, because preserving lineage-specific substitution rates as measured by $r$ might not require low absolute rates of gene flow. Instead, reducing effective population sizes via recurrent linked selection might achieve a similar result in populations at equilibrium ($N↓⇒F_{S⁢T}↑⇒r↑$).

The theory in its present form has several limitations. First, mutations follow the infinite-site model (Kimura, 1969), so that reverse mutations, double mutations, and substitution types are not accurately reflected in the estimated ratio between species-specific substitution rates. Second, population structure is assumed at equilibrium, whereas real data could carry footprints from non-equilibrium demographic processes (e.g. secondary contact) (Hey, 2010). Third, there could be considerable population structure within each species contributing to elevated $F_{S⁢T}$ but not necessarily to rate-divergence. This effect could be seen in simulated stepping-stone models (Figure 6—figure supplement 3) and will underestimate the level of rate divergence. Fourth, substitution is stochastic across the genome, and accurately estimating observed rate ratio $r$ relies on averaging substitution numbers across a large number of sites. This poses a problem if sites linked to high $F_{S⁢T}$ regions are rare (i.e. few genomic islands). Lastly, as the theory is built upon the neutral coalescent, it is best suited for studying behaviors of neutral sites.

Nonetheless, the monotonic relationship between $r$ and $F_{S⁢T}$ (i.e. larger sequence divergence is associated with more asymmetric substitution rates) might be qualitatively robust regardless of the aforementioned caveats. For instance, even for hybrid zones formed by recent secondary contact, reducing the absolute rate of gene flow by barrier loci in principle also keeps divergent rates from mixing, simply because it prevents substitutions accumulated in the allopatric phase from flowing between species.

In conclusion, our study characterizes several genomic consequences of the rate-mixing process when molecular clocks tick at different speeds between hybridizing lineages. This process provides new information on reproductive isolation but also leads to pitfalls in interpreting results of popular introgression tests. As this phenomenon is neglected in most studies of hybridization and speciation, its full scope awaits further investigation in both theories and empirical systems.

## Materials and methods

### Museum specimens and climate data

Museum specimens with verifiable locality data of all species were gathered from The University Museum of The University of Tokyo (Harada et al., 2012; Yago et al., 2021), Global Biodiversity Information Facility (The Global Biodiversity Information Facility, 2021b; The Global Biodiversity Information Facility, 2021a), and individual collectors (Figure 2—source data 5). Records of P. maackii from Japan, Korea and NE China were excluded from the analysis, so that most P. maackii individuals correspond to ssp. han, the subspecies that hybridizes with P. syfanius. Spatial principal component analysis was performed on elevation, maximum temperature of warmest month, minimum temperature of coldest month, and annual precipitation, all with 30s resolution from WorldClim-2 (Fick and Hijmans, 2017). The first two PCAs, combined with tree cover (Hansen et al., 2013), were used in MaxEnt-3.4.1 to produce species distribution models that use known localities to predict occurrence probabilities across the entire landscape (Phillips et al., 2017). Outputs were trimmed near known boundaries of each species. See Figure 2—figure supplement 3 for the final result.

### Sampling, re-sequencing, and mitochondrial phylogeny

Eleven males of P. syfanius and P. maackii, with one male of P. arcturus and one male of P. dialis were collected in the field between July and August in 2018 (Figure 2—source data 5), and were stored in RNAlater at –20 °C prior to DNA extraction. E.Z.N.A Tissue DNA kit was used to extract genomic DNA, and KAPA DNA HyperPlus 1/4 was used for library preparation, with an insert size of 350 bp and 2 PCR cycles. The library is sequenced on a Illumina NovaSeq machine with paired-end reads of 150 bp. Adaptors were trimmed using Cutadapt-1.8.1, and subsequently the reads were mapped to the reference genome of P. bianor with BWA-0.7.15, then deduplicated and sorted via PicardTools-2.9.0. The average coverage among 13 individuals in non-repetitive regions varies between 20× and 30×. Variants were called twice using BCFtools-1.9 – the first including all samples, used in analyses involving outgroups, and the second excluding P. arcturus and P. dialis, used in all other analyses. The following thresholds were used to filter variants: $10N<$ DP $<50N$, where $N$ is the sample size; QUAL > 30; MQ > 40; MQ0F < 0.2. As a comparison, we also called variants with GATK4 and followed its best practices, and 93% of post-filtered SNPs called by GATK4 overlapped with those called by BCFtools. We used SNPs called by BCFtools throughout the analysis. Mitochondrial genomes were assembled from trimmed reads with NOVOPlasty-4.3.1 (Dierckxsens et al., 2017), using a published mitochondrial ND5 gene sequence of P. maackii as a bait (NCBI accession number: AB239823.1). We also used the following published mitochondrial genomes (NCBI accession numbers): KR822739.1 (Papilio glaucus), NC_029244.1 (Papilio xuthus), JN019809.1 (Papilio bianor). The neighbor-joining mitochondrial phylogeny was built with Geneious Prime-2021.2.2 (genetic distance model: Tamura-Nei), and we used 104 replicates for bootstrapping. The reference genome of P. xuthus was previously aligned to the genome of P. bianor and we used this alignment directly in all analysis (Lu et al., 2019).

### Calculating site-pattern asymmetry

Given a species tree {{P1,P2},O}, where P1 and P2 are sister species and O is an outgroup, if mutation rates are equal between {P1,P2}, and no gene flow with O, then on average the number of derived alleles in P1 should equal the number of derived alleles in P2. Let $S$ be a collection of sites, $f_{s}$ be the frequency of a particular site pattern at site $s\inS$. “ABB” be the pattern where only P2 and O share the same allele, and “BAB” be the pattern where only P1 and O share the same allele, then the three-species $D_{3}$ statistic is calculated as

$$
D_{P_{1},P_{2},O}=\frac{\sums\inS(f_{s,ABB}−f_{s,BAB})}{\sums\inS(f_{s,ABB}+f_{s,BAB})},
$$

where $S$ is always limited to sites without polymorphism in the outgroup O. This statistic is in principle capturing the same source of asymmetry as the statistic proposed by Hahn and Hibbins, 2019, although their version uses divergence to the outgroup instead of frequencies of site-counts. Similarly, the four-species $D_{4}$ statistic, which considers species tree {{{P1,P2},O1},O2} and site patterns ABBA versus BABA (Durand et al., 2011) is calculated as

$$
D_{P_{1},P_{2},O_{1},O_{2}}=\frac{\sums\inS(f_{s,ABBA}−f_{s,BABA})}{\sums\inS(f_{s,ABBA}+f_{s,BABA})},
$$

where $S$ is always limited to sites without polymorphism in the second outgroup O2. The significance of both tests was computed using block-jackknife over 1 Mb blocks across the genome. Additionally, we estimated rate ratio as follows. First we restricted to sites where all outgroups are fixed for the same ancestral allele to dampen the influence of recurrent mutation. Then, for each site, sample one allele at random from each focal lineage. Calculate the probability of observing a derived allele in P1 but not in P2, and the probability of observing a derived allele in P2 but not in P1. The rate ratio is computed as the ratio between the two probabilities. Explicitly, let $I⁢(⋅)$ be the identity function, and $f_{s}$ be the frequency of the derived allele, then:

$$
Rate ratio r=\frac{\sums\inSf_{s,P_{1}}(1−f_{s,P_{2}})Π_{i\inoutgroups}I(f_{s,i}=0)}{\sums\inS(1−f_{s,P_{1}})f_{s,P_{2}}Π_{i\inoutgroups}I(f_{s,i}=0)}
$$

Its standard error was estimated using 1 Mb block-jackknifing. We excluded P. xuthus from the outgroups to increase the number of informative sites when using this formula.

### D3 and D4 under unequal substitution rates and recurrent mutations

In this section, we calculate observed $D_{3}$ and $D_{4}$ assuming that incomplete lineage sorting contributes insignificantly to both statistics. If incomplete lineage sorting is present, it will not create new bias (numerators are on average unchanged), but will likely dampen existing bias (inflating denominators).

As substitutions are independent along each lineage, we can mute recurrent mutations in outgroups and generate them afterwards. For three taxa with gene tree {{P1,P2},O1}, before recurrent mutations, there are $n_{1}$ sites with pattern (B,A,A), and $n_{2}$ sites with pattern (A,B,A). If substitution rate is higher in P2, we have $n_{2}>n_{1}$, so the true value of $D_{3}$, written as $D^_{3}$, is always negative:

$$
D^_{3}=\frac{n_{1}−n_{2}}{n_{1}+n_{2}}<0
$$

Next, recurrent mutations in O1 occur at each site with an average probability $p_{1}$, and with an average probability $c$, ancestral alleles from affected sites in O1 are converted to the same derived allele in {P1,P2}. $c$ will be independent of $n_{1}$ and $n_{2}$, as long as substitutions between {P1,P2} are only different in rates, but not mutation types. Hence, two possible mutation paths exist:

$$
(A,B,B)→p_{1}(A,B,⋅)→c(A,B,A)≡(B,A,B)(B,A,B)→p_{1}(B,A,⋅)→c(B,A,A)≡(A,B,B)
$$

The expected site counts, after recurrent mutations, become

$$
⟨n_{ABB}⟩=(1−p_{1})n_{1}+cp_{1}n_{2}⟨n_{BAB}⟩=(1−p_{1})n_{2}+cp_{1}n_{1}
$$

Using the new expected site counts in $D_{3}$ statistics produce the following value:

$$
D_{3}=\frac{1−(c+1)p_{1}}{1+(c−1)p_{1}}D^_{3}≈(1−2cp_{1})D^_{3}
$$

Since $D^_{3}$ is negative, it grows approximately linearly near small values of $p_{1}$. (The full equation is still monotonic in $p_{1}$.)

Similarly, for four-taxon statistics, before recurrent mutation, there are two types of sites: (A,B,B,B)- $n_{1}$; (B,A,B,B)- $n_{2}$. Suppose the average probability of recurrent mutation is $p_{1}$ in O1, and $p_{2}$ in O2, and the conversion probability of each recurrent mutation into derived alleles of {P1, P2} is $c$ for both outgroups. Using the same procedure, one can show that

$$
D_{4}=\frac{p_{2}−p_{1}}{p_{2}+p_{1}}D^_{3}
$$

Since recurrent mutations occur more frequently in distant outgroups, $p_{2}>p_{1}$. Because $D^_{3}$ is negative, we have $D_{4}<0$.

### Local gene trees

Local gene trees were estimated using iqtree-2.0 (Minh et al., 2020) on 50 kb non-overlapping genomic windows with options -m MFP -B 5000. Only SNPs from annotated regions (synonymous sites +nonsynonymous sites +introns) across all individuals were used. For diploid individuals, heterozygous sites were assigned IUPAC ambiguity codes and iqtree assigned equal likelihood for each underlying character, thus information from heterozygous sites is largely retained. This is crucial as we are interested in the branch length of inferred trees. Option -m MFP implements iqtree’s ModelFinder that tests the FreeRate model to accommodate maximum flexibility with rate-variation among sites (Kalyaanamoorthy et al., 2017). We also used UltraFast Bootstrap to calculate the support for different types of splits in each window (the -B 5000 option; Hoang et al., 2018). In each window, we extracted the support for monophyly among P. maackii +P.syfanius directly from the output of UltraFast Bootstrap, and we define the support for paraphyly among P. maackii +P.syfanius as (100 - the support for monophyly). For each level of support, we filtered out genomic windows where both the support for monophyly and the support for paraphyly drop below the given level. The remaining windows were considered informative.

### Rate-mixing under the equilibrium IM model

We construct a continuous-time coalescent model as follows. Both populations have $N$ haploid individuals, gene flow rate is $m$, and coalescent rate is $N^{-1}$ in each population. In the equilibrium system, as we track both haploid individuals backward in time, there are six distinct states: $(1|2),(2|1),(1,2|),(|1,2),(0|),(|0)$, where 1 and 2 represent two individuals prior to coalescent, 0 is the state of coalescent, and $(⋅|⋅)$ shows the location of each lineage. Its transition density $B⁢(t)$ satisfies $\partial_{t}⁡B=AB$, where $A$ is given as

$$
(-2⁢m0mm000-2⁢mmm00mm-2⁢m-\frac{1}{N}000mm0-2⁢m-\frac{1}{N}0000\frac{1}{N}0-mm000\frac{1}{N}m-m)
$$

Let $S_{i|j}⁢(T)$ be the mean sojourn time of an uncoalesced individual inside population $i$ during $0\leqt\leqT$, conditioning on the individual being taken from population $j$ at $t=0$. Assuming the infinite-site mutation model, let $\mu_{i}$ be the substitution rate in population $i$, observed rate ratio $r$ is thus

$$
r=\frac{\mu_{2}S_{2|2}(∞)+\mu_{1}S_{1|2}(∞)}{\mu_{1}S_{1|1}(∞)+\mu_{2}S_{2|1}(∞)}
$$

where (due to symmetry)

$$
S_{1|1}(∞)=S_{2|2}(∞)=\int_{0}^{+∞}(1,0,0,1,0,0)e^{At}(1,0,0,0,0,0)^{T}dt=\frac{1+2Nm}{2m}S_{2|1}(∞)=S_{1|2}(∞)=\int_{0}^{+∞}(0,1,1,0,0,0)e^{At}(1,0,0,0,0,0)^{T}dt=N
$$

Let $r_{0}=\mu_{2}/\mu_{1}$, and since $F_{S⁢T}=(1+4⁢N⁢m)^{-1}$, we have

$$
r=\frac{1+r_{0}+F_{ST}(r_{0}−1)}{1+r_{0}−F_{ST}(r_{0}−1)}
$$

### Local ancestry estimation

Software ELAI (Guan, 2014) with a double-layer HMM model was used to estimate diploid local ancestries across chromosomes. An example command is as follows: elai-lin -g genotype.maackii.txt -p 10 -g genotype.syfanius.txt -p 11 -g genotype.admixed.txt -p 1 -pos position.txt -s 30 -C 2 -c 10 -mg 5000 --exclude-nopos.

Note that -mg specifies the resolution of ancestry blocks, thus increasing its value will increase the stochastic error of incorrectly inferring very short blocks of ancestry. To control for uncertainty, we estimated repeatedly for 50 times. All replicates were used simultaneously in finding the correlation coefficients between entropy and other variables. Results from an example run is in Figure 3—figure supplement 1.

### Ancestry and entropy

Here we introduce concisely the data transformation framework for calculating the entropy of local ancestry. The mathematical detail of this approach is presented in the appendix.

#### Ancestry representation

The space of all ancestry signals is high-dimensional, and directly calculating the entropy in this space is not feasible with just a few individuals. So we propose to measure only the pairwise correlation of ancestries among sites, which captures only the second-order randomness, but is sufficient for practical purposes. Consider a hybrid individual with two parental populations indexed by $k=1,2$. Assuming a continuous genome, let $p_{k}⁢(l)=0,\frac{1}{2},1$ be the diploid ancestry of locus $l$ within genomic interval $[0,L]$. By definition, we have $p_{1}⁢(l)+p_{2}⁢(l)=1$, that is the total ancestry is conserved everywhere in the genome. The bi-ancestry signal at locus $l$ is defined as the following complex variable

$$
z⁢(l)=\sqrt{p_{1}⁢(l)}+i⁢\sqrt{p_{2}⁢(l)}=e^{i⁢arccos⁡\sqrt{p_{1}⁢(l)}},
$$

where $i=\sqrt{-1}$ is the imaginary number. An advantage of using a complex representation for the bi-ancestry signal is that we can model different ancestries along the genome as different phases of a complex unit phasor ($e^{i⁢\theta}$), such that the power of the signal at any given locus is simply the sum of both ancestries, which is conserved ($|z⁢(l)|^{2}=1$). It ensures that we do not bias the analysis to any particular region or any particular individual when decomposing the signal into its spectral components.

### Within-individual spectral entropy (Sw)

To characterize the average autocorrelation along an ancestry signal at a given scale $l$, define the following scale-dependent autocorrelation function

$$
A⁢(l)=Re⁢[\frac{1}{L}⁢\int_{0}^{L}z⁢(ξ)⁢z⁢(ξ+l)¯⁢dξ],
$$

where $z⁢(l)$ is understood as a periodic function such that $z⁢(ξ+l)=z⁢(ξ+l-L)$ whenever the position goes outside of $[0,L]$. The Wiener-Khinchin theorem guarantees that $z⁢(l)$’s power spectrum $ζ⁢(f)$, which is discrete, and the autocorrelation function $A⁢(l)$ form a Fourier-transform pair. Due to the uncertainty principle of Fourier transform, $A⁢(l)$ that vanishes quickly at short distances (small-scale autocorrelation) will produce a wide $ζ⁢(f)$, and vice versa. So the entropy $S_{w}$ of $ζ⁢(f)$, which measures the spread of the total ancestry into each spectral component, also measures the scale of autocorrelation. In practice, $ζ⁢(f)$ is the square modulus of the Fourier series coefficients of $z⁢(l)$, and we fold the spectrum around $f=0$ before calculating the within-individual entropy $S_{w}$. The formula used in the manuscript is

$$
S_{w}=−\sumn=0+∞ζ_{n}ln⁡ζ_{n}ζ_{n}={|Z_{n}|^{2}+|Z_{−n}|^{2}(n>0)|Z_{0}|^{2}(n=0)
$$

where $Z_{n}$ are the Fourier coefficients from the expansion $z⁢(l)=\sum_{n=-∞}^{+∞}Z_{n}⁢e^{i⁢2⁢\pi⁢n⁢l/L}$. To speed up the Fourier expansion, we could densely pack equally-spaced markers that sample a continuous ancestry signal into a discrete signal, which then undergoes Fast Fourier Transform (FFT). The spectrum of FFT (discrete and finite) approximates the continuous-time Fourier spectrum (discrete and infinite), and entropy also converges as marker density increases.

### Between-individual spectral entropy (Sb)

As ancestry configuration is far from random around barrier loci, it will also influence the correlation of ancestry between different individuals at the same locus. For a genomic region experiencing strong barrier effects, two individuals could either be very similar in ancestry, or very different. This effect can be quantified by first calculating the cross-correlation $C_{j,j^{′}}⁢(l)=z_{j}⁢(l)⁢z_{j^{′}}⁢(l)¯$ at position $l$ between individuals $j$ and $j^{′}$, and then averaging across a genome interval: $c_{j,j^{′}}=\frac{1}{L}⁢\int_{0}^{L}C_{j,j^{′}}⁢(l)⁢dl$. The $J\timesJ$ dimensional matrix $C$ with entries $c_{j,j^{′}}$ describes the pairwise cross-correlation within the cohort of $J$ individuals. We also have $c_{j,j}≡1$ as each individual is perfectly correlated with itself. The matrix $C$ is Hermitian, so it has a real spectral decomposition with eigenvalues $\lambda_{j}$ that satisfy $\sum_{j}\lambda_{j}/J=1$. This process is very similar to performing a principal component analysis on the entire cohort of individuals, and $\lambda_{j}/J$ describes the fraction of the total ancestry projected onto principal component $j$. If many loci co-vary in ancestry, the spectrum ${\lambda_{j}}$ will be concentrated near the first few components. Similarly, we use entropy to measure the spread of the spectrum, and hence the between-individual spectral entropy is defined as

$$
S_{b}=-\sumj\frac{\lambda_{j}}{J}⁢ln⁡\frac{\lambda_{j}}{J}
$$
