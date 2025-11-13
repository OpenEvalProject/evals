# Copy number variation and population-specific immune genes in the model vertebrate zebrafish

## Authors

- Yannick Schäfer<sup>1</sup> ([ORCID: 0000-0002-5264-8816](https://orcid.org/0000-0002-5264-8816))
- Katja Palitzsch<sup>1</sup> ([ORCID: 0000-0002-6292-4925](https://orcid.org/0000-0002-6292-4925))
- Maria Leptin<sup>1</sup> ([ORCID: 0000-0001-7097-348X](https://orcid.org/0000-0001-7097-348X))
- Andrew R Whiteley<sup>2</sup> ([ORCID: 0000-0002-8159-6381](https://orcid.org/0000-0002-8159-6381))
- Thomas Wiehe<sup>1</sup> ([ORCID: 0000-0002-8932-2772](https://orcid.org/0000-0002-8932-2772)) †
- Jaanus Suurväli<sup>1</sup> ([ORCID: 0000-0003-0133-7011](https://orcid.org/0000-0003-0133-7011)) †

### Affiliations

1. Institute for Genetics, University of Cologne Cologne Germany ([ROR:00rcxh774](https://ror.org/00rcxh774))
2. WA Franke College of Forestry and Conservation, University of Montana Missoula United States ([ROR:0078xmk34](https://ror.org/0078xmk34))
3. Department of Biological Sciences, University of Manitoba Winnipeg Canada ([ROR:02gfys938](https://ror.org/02gfys938))

† Corresponding author

## Abstract

Copy number variation in large gene families is well characterized for plant resistance genes, but similar studies are rare in animals. The zebrafish (Danio rerio) has hundreds of NLR immune genes, making this species ideal for studying this phenomenon. By sequencing 93 zebrafish from multiple wild and laboratory populations, we identified a total of 1513 NLRs, many more than the previously known 400. Approximately half of those are present in all wild populations, but only 4% were found in 80% or more of the individual fish. Wild fish have up to two times as many NLRs per individual and up to four times as many NLRs per population than laboratory strains. In contrast to the massive variability of gene copies, nucleotide diversity in zebrafish NLR genes is very low: around half of the copies are monomorphic and the remaining ones have very few polymorphisms, likely a signature of purifying selection.

## Introduction

The innate immune system of an organism provides the first defense line against pathogens. Immune genes tend to evolve quickly and are often associated with a high degree of genetic variability. Many genes and proteins of the immune system are lineage-specific (limited to specific groups of animals, plants, or other taxa), while others have defense roles in a wide range of species. In particular, proteins containing a large nucleotide-binding domain followed by smaller repeats have an immune function in animals, plants, fungi, and bacteria alike (Ting et al., 2008; Jones and Dangl, 2006; Uehling et al., 2017; Gao et al., 2022). In animals, these repeats are usually leucine-rich repeats (LRRs) and the proteins themselves are classified as NLRs (nucleotide binding domain leucine-rich repeat containing, also known as NOD-like receptors). They have a multitude of functions: some act as pathogen sensors or transcription factors (Almeida-da-Silva et al., 2023), others are components or modulators of inflammasomes, large protein complexes that are assembled within cells as part of the response to biological or chemical danger (Almeida-da-Silva et al., 2023).

Plants have their own NLRs that are structurally similar to the ones from animals and also carry out central functions in the immune response (Urbach and Ausubel, 2017; Yue et al., 2012). Their diversity has been extensively characterized in several species, including the thale cress (Arabidopsis thaliana), and vastly different repertoires have been found from different strains or individuals (Van de Weyer et al., 2019b). NLR repertoires can also be referred to as NLRomes, and a species-wide repertoire is called the ‘pan-NLRome’.

Most knowledge about NLRs in animals comes from studies of humans and rodents, but their NLR repertoires (20–30 genes) are smaller than those of many other species such as the purple sea urchin, the sponge Amphimedon queenslandica, and many fish (Hibino et al., 2006; Yuen et al., 2014; Suurväli et al., 2022). However, even in mice one NLR (Nlrp1) has different copy numbers in different laboratory strains, ranging from 2 to 5 (Lilue et al., 2018). In many fishes, studies have reported NLR repertoires in the range of 10–50 genes (e.g., Rajendran et al., 2012; Li et al., 2016). In others, hundreds of NLRs are present, including in the model species zebrafish (Danio rerio) (Stein et al., 2007; Laing et al., 2008; Tørresen et al., 2018; Adrian-Kalchhauser et al., 2020; Suurväli et al., 2022). The zebrafish reference genome contains nearly 400 NLR genes, two-thirds of which are located on the putative sex chromosome (chromosome 4), in a genomic region associated with extensive haplotypic variation (Howe et al., 2013; Howe et al., 2016; McConnell et al., 2023; Anderson et al., 2012).

The majority of fish NLRs represent a fish-specific subtype that was originally labeled NLR-C (Laing et al., 2008), although they can be further divided into at least six groups based on structural similarities and sequence of conserved exons (Howe et al., 2016; Adrian-Kalchhauser et al., 2020). A schematic structure of proteins encoded by zebrafish NLR-C genes is presented in Figure 1A. All of them possess a FISNA domain (fish-specific NACHT-associated domain), which precedes the nucleotide-binding domain NACHT and is encoded by the same large exon near the N-terminus of the protein (Howe et al., 2016). FISNA-NACHT is in some cases preceded by the effector domain PYD, but this is encoded by a separate exon (Howe et al., 2016). Additionally, many NLR-C proteins have a B30.2 domain (also known as PRY/SPRY) at the C-terminal end, separated from FISNA-NACHT by multiple introns and exons containing the LRRs (Figure 1A; Howe et al., 2016). The B30.2 domain functions through protein–protein interaction (Woo et al., 2006) and is also found in a variety of other genes such as the large family of TRIM ubiquitin ligases (van der Aa et al., 2009; Howe et al., 2016; Suurväli et al., 2022) that are often also involved in immunity.

![Figure 1.](https://cdn.elifesciences.org/articles/98058/elife-98058-fig1-v2.jpg)

**Figure 1.:** (A) Generalized, schematic representation of the domain architecture of an NLR-C protein. Each box represents a translated exon. The N-terminal repeats, the death-fold domain, as well as the B30.2 domain only occur in subsets of NLR-C genes. The number of N-terminal repeats and leucine-rich repeats can vary. Domains that can be either present or absent in different NLRs are surrounded by square brackets. (B) Sampling sites for wild zebrafish. All sites are located near the Bay of Bengal. Final sequenced sample sizes are indicated in parentheses. The map is based on geographic data collected and published by AQUASTAT from the Food and Agriculture Organization of the United Nations (FAO, 2021). The population DP is marked with an asterisk because its analysis and results are presented only in figure supplements.

It is not known why fishes possess so many NLRs, how they evolve, and how much within-species genetic variability they have. The previously observed repeated expansions and contractions of this family suggest it to have a high rate of gene birth and death (Suurväli et al., 2022). Studies have shown that viral and bacterial infections can induce the expression of specific fish NLRs (reviewed in Chuphal et al., 2022). Some of these have PYD or CARD domains and can even form inflammasomes similar to mammalian NLRs (Kuri et al., 2017; Li et al., 2018b). A species-wide inventory of major NLR exons in a model species such as zebrafish would provide valuable insights into the evolution and diversity of this large immune gene family.

## Results

By adapting and modifying a protocol that combines bait-based exon capture with PacBio SMRT technology (Witek et al., 2016), we successfully generated circular consensus sequence (CCS) data for targeted parts of the immune repertoire from 93 zebrafish (of initial 96), representing four wild populations (Figure 1B) and two laboratory strains. With this approach, we aimed to sequence all exons in zebrafish that encode the nucleotide-binding FISNA-NACHT domains and all exons that encode B30.2 domains. Samples of one wild population (DP) suffered from poor sequence coverage and had to be excluded from downstream analyses in order to avoid bias in interpretation. Results involving this population are only shown in figure supplements and not in the main figures.

Our protocol used PCR with primers targeting ligated adapters to amplify the below-nanogram amounts of genomic DNA obtained from exon capture. This limited our fragment sizes to the lengths of what the polymerase was able to amplify. Zebrafish NLRs can have their exons spread out across tens of kilobases, so that we cannot know which exons belong to the same gene. However, we were able to use captured sequence surrounding the targeted exons to distinguish among near-identical coding sequences and separate NLR-associated B30.2 domains from B30.2 elsewhere in the genome.

### The zebrafish pan-NLRome

We used an orthology clustering approach on NLR sequences assembled from all populations to create a reference set of NLRs (a pan-NLRome). This resulted in the identification of 1513 unique FISNA-NACHT containing sequences and 567 for NLR-associated B30.2 (NLR-B30.2). Nearly 10% of the sequences (145 FISNA-NACHT and 64 NLR-B30.2) contained pre-mature stop codons that were at least 10 amino acids from the end and led to early truncation of the protein. In total, 101 of the 1513 FISNA-NACHT were preceded by an exon containing the N-terminal effector domain PYD. Nearly all of those (97 out of 101) were found in group 1 NLR-C genes identified by the presence of the characteristic sequence motif GIAGVGKT (Howe et al., 2016). Since the combination of FISNA and NACHT is only present in NLR-C, its count of 1513 can be considered equal to the total number of NLR-C genes in the data. We found each individual zebrafish to have 100–550 NLR genes from the pan-NLRome in at least one copy (Figures 2 and 3), and only 50–75% of these have a high-quality match in the GRCz11 reference genome (Figure 2—figure supplement 2). In general, laboratory zebrafish had less NLRs than wild samples (Figure 2). The number and length of CCS reads and assembled contigs (both prior to orthology clustering) are presented in Figure 2—figure supplement 1.

![Figure 2.](https://cdn.elifesciences.org/articles/98058/elife-98058-fig2-v2.jpg)

**Figure 2.:** Black diamonds on the box plots denote means, horizontal lines denote medians. Left side: two laboratory strains; right side: three wild populations.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/98058/elife-98058-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A1) Absolute numbers of CCS reads from NLR exons per sequenced individual. (A2) Lengths of the CCS reads that map to NLR genes. (B1) Absolute numbers of assembled contigs containing an NLR exon per sequenced individual. Triangles above TU mark the numbers of NLR exons found in the reference genome. (B2) Lengths of the individual assembled contigs that contain an NLR exon. Outliers not shown in the boxplots. The black diamonds on boxplots denote means, horizontal black lines denote medians.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/98058/elife-98058-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (A) Proportions of unique FISNA-NACHT and NLR-B30.2 sequences that were successfully mapped to the reference genome GRCz11 with a mapping quality of 60, by population. (B) Distribution of mapping qualities for all unique NLR sequences that aligned to GRCz11, showing that most map either with very high (60) or very low quality.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/98058/elife-98058-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** (A) Nucleotide sequence logo (on top, continued on bottom left) and amino acid logo (on bottom right) for a small, highly conserved 47 bp exon that precedes B30.2 in zebrafish NLRs and not in other genes. The first nucleotide of the exon was removed to generate the correct amino acid translation. Logos were created with Weblogo, the height of each base represents its information content in bits (Crooks et al., 2004). (B) Absolute numbers of contigs containing a B30.2 exon per sequenced individual, split by presence/absence of the NLR-specific exon. The black diamonds on boxplots mark the means. (C) Genomic distribution of FISNA-NACHT domains in the GRCz11 reference genome. (D) Genomic distribution of B30.2 domains in the GRCz11 reference genome.

![Figure 3.](https://cdn.elifesciences.org/articles/98058/elife-98058-fig3-v2.jpg)

**Figure 3.:** (A) Sequence data from each individual zebrafish (vertical axis) was aligned to FISNA-NACHT exon sequences of the pan-NLRome (horizontal axis). Grayscale intensity shows, for each NLR, the proportion of NLR-aligning data in each given fish that matches this specific gene. Darker gray indicates a higher likelihood of this NLR being represented in multiple copies in the particular individual. Light gray indicates a single copy, white indicates absence. For clarity, only the 1235 FISNA-NACHT exons for which at least one fish had a minimum of 10 reads mapped to it are shown. (B) Numbers of pan-NLRome sequences (based on FISNACHT diagnosis) found in all three, two, or only one wild population. (C) Relative numbers of fish in which pan-NLRome sequences were found in wild populations. ’Core’ pan-NLRome: genes which are found in at least 80% of the sample (from a total of 57 wild fish); ’shell’: genes in at least 20%; ’cloud’: rare genes found in less than 20% of the sample. (D) Observed and estimated sizes of population-specific pan-NLRomes. Data points (filled circles and squares) show the average number of totally discovered NLR genes (as identified via their FISNA-NACHT domain) when investigating $x$ fish. The dashed line is obtained by non-linear fit of the data to the function given in Equation 2. For all populations, the hypothetical pan-NLRome size – when extrapolating $x→∞$ – is finite (see Table 1).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/98058/elife-98058-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A1, A2) Numbers of private and shared NLR sequences in wild populations. (B1, B2) Numbers of unique NLR sequences (each with one or more copies per individual) found in fish of the sequenced strains. Black diamonds on the box plots denote means, horizontal lines denote medians. (C1, C2) Population-specific pan-NLRomes and sets of NLR-B30.2 domains. Data points (filled circles and squares) show the average number of totally discovered NLR genes (as identified via their FISNA-NACHT domain) in $x$ individuals. The dotted lines represent the result of non-linear curve fitting (detailed in ‘Materials and methods’).

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/98058/elife-98058-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** (A) Sequence data from each individual zebrafish (x-axis) was aligned to FISNA-NACHT exon sequences of the pan-NLRome (y-axis). Grayscale intensity shows, for each NLR, the proportion of NLR-aligning data in each given fish that matches this specific gene. Darker colors can be interpreted as potentially having multiple copies. Lighter colors indicate a single copy, white color means that the sequence was not present. For clarity, only the 1235 FISNA-NACHT for which at least one fish had 10 reads mapped to it are shown. (B) Relative numbers of fish in which the pan-NLRome sequences were found in wild populations. Some belong to the core pan-NLRome (in at least 80% of fish), while others are classified as shell (in at least 20% of fish) or cloud (less than 20%). (C) Numbers of unique NLR sequences (each with one or more copies per individual) found in fish of the sequenced strains. Black diamonds on the box plot denote means, horizontal lines denote medians. (D, E) Principal component analysis of scaled-per-individual NLR (FISNA-NACHT) copy numbers. The first two components appear to separate data based on differences between wild and laboratory zebrafish (PC1), and based on geographic distance (PC2).

Whereas FISNA-NACHT is only found in NLRs, B30.2 domains are also found in other gene families. In addition to the 567 NLR-B30.2 domains, we also found 732 B30.2 domains not associated with NLRs. We were able to distinguish between them by utilizing the sequence of a short highly conserved 47 bp exon that appears to precede B30.2 in NLRs, but not in other genes (Figure 2—figure supplement 3). Each individual zebrafish possesses 20–180 NLR-B30.2s n at least one copy (Figure 3—figure supplement 1).

### Copy number variation in the pan-NLRome

Aligning CCS reads to the pan-NLRome revealed a considerable amount of variability in the proportion of reads mapping to them, both between and within populations (Figure 3A). This can be interpreted as the gene being present in different copy numbers. Furthermore, each NLR had its own distinct pattern of copy number variation, although generally the highest copy numbers were observed for the wild populations KG, SN, and CHT (Figure 3A). We also observed some sequencing batch-related differences, but the copy numbers differed even between individuals sequenced in the same batch.

Of the 1513 unique FISNA-NACHT and 567 NLR-B30.2 sequences, 880 FISNA-NACHT and 346 NLR-B30.2 (59 and 57%, respectively) were detected in at least one individual from all wild populations (Figure 3B, Figure 3—figure supplement 1).

There were also NLR sequences shared between just two wild populations, and some were restricted to a single population (Figure 3B). Moreover, we observed a lot of variability in the distributions of gene copies among fish within populations (Figure 3C). Only around 4% of the genes in the pan-NLRome were found in 80%, or more, of the wild fish. They constitute the core NLRome (Van de Weyer et al., 2019a). Most genes (51%) were found in the so-called shell of the pan-NLRome (20–80% of fish). Almost as many (45%) are found in a few fish (less than 20% of the sample) only. Although 60% of NLR genes occur in all wild populations, only 4% are omnipresent, that is, are in the core pan-NLRome. Thus, there is considerable variation in the NLR repertoires of individuals from the same population.

The total number of NLRs identified in a number $x$ of individual fish can be fitted to a harmonic function (Medini et al., 2020). Using this function (see ‘Materials and methods’), we estimated the sizes of the NLRomes of the populations (Figure 3D) and found a total of 520 and 570 NLRs in the laboratory strains TU and CGN, respectively (Table 1). For the wild populations, we estimated four times as many: 2283 in KG, ,896 in SN, and 2452 in CHT.

**Table 1.**
 Values of fitted parameters and saturation limits for FISNA-NACHT and NLR-B30.2 exons, by population.


<table>
  <thead>
    <tr>
      <th>Population</th>
      <th colspan="4">FISNA-NACHT</th>
      <th colspan="4">NLR-B30.2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>-</td>
      <td>α</td>
      <td>β</td>
      <td>Limit</td>
      <td>Quantile*</td>
      <td>α</td>
      <td>β</td>
      <td>Limit</td>
      <td>Quantile*</td>
    </tr>
    <tr>
      <td>TU</td>
      <td>178.274</td>
      <td>1.43356</td>
      <td>519.548</td>
      <td>118</td>
      <td>53.8579</td>
      <td>1.40774</td>
      <td>164.73</td>
      <td>164</td>
    </tr>
    <tr>
      <td>CGN</td>
      <td>257.207</td>
      <td>1.62786</td>
      <td>569.367</td>
      <td>23</td>
      <td>78.7156</td>
      <td>1.61283</td>
      <td>177.246</td>
      <td>25</td>
    </tr>
    <tr>
      <td>DP</td>
      <td>309.14</td>
      <td>1.01231</td>
      <td>25284</td>
      <td>2930†</td>
      <td>69.3609</td>
      <td>0.87454</td>
      <td>∞</td>
      <td>na</td>
    </tr>
    <tr>
      <td>KG</td>
      <td>436.761</td>
      <td>1.2152</td>
      <td>2288.41</td>
      <td>2060</td>
      <td>145.715</td>
      <td>1.1418</td>
      <td>1113.23</td>
      <td>6.41e6</td>
    </tr>
    <tr>
      <td>SN</td>
      <td>479.892</td>
      <td>1.26093</td>
      <td>2152.12</td>
      <td>3907</td>
      <td>145.548</td>
      <td>1.10183</td>
      <td>1514.35</td>
      <td>3.75e9</td>
    </tr>
    <tr>
      <td>CHT</td>
      <td>416.712</td>
      <td>1.18893</td>
      <td>2451.81</td>
      <td>1.12e5</td>
      <td>135.677</td>
      <td>1.11911</td>
      <td>1218.54</td>
      <td>1.41e8</td>
    </tr>
  </tbody>
</table>

_*Sample size required to capture 90% of the population’s pan-NLRome.†DP required sample size refers to only 10% (instead of 90%) of its hypothetical pan-NLRome size._

### Differences from the reference genome

NLRs sequenced in this study were often different from those present in the reference genome GRCz11. Even NLRs sequenced from the strain that the reference genome itself is based on (TU) did not always align well to it. When the exon itself did align, the intronic sequences surrounding it could often be very different from the reference. In numbers, only around 75% of NLRs occurring in TU fish aligned to the reference genome GRCz11 with high mapping qualities (Figure 2—figure supplement 2A). This number dropped even lower elsewhere – from 60–65% of NLRs in CGN which aligned well to the reference, down to only around 50% for the wild populations. The majority of NLRs that did not map well had a very poor mapping quality of 1 (Figure 2—figure supplement 2B). Moreover, there were 9 FISNA-NACHT and 10 NLR-associated B30.2 in the pan-NLRome which did not map anywhere in the reference genome.

### Purifying selection on single-nucleotide variants

We used the pan-NLRome as a reference for identifying single-nucleotide polymorphisms in the data. NLR sequence diversity was rare, with a large fraction of exons not having any variants in any of the populations. If variants were present, nucleotide diversity ($\theta_{\pi}$) was up to 0.016 and Watterson’s estimator ($\theta_{w}$) up to 0.021 (Figure 4A and B). In laboratory strains, genetic variability of FISNA-NACHT exceeded that of B30.2, but no such pattern was observed for wild populations. B30.2 exons of laboratory strains were also less variable than B30.2 from wild zebrafish (Figure 4B). The proportion of exons without any polymorphisms was much higher among FISNA-NACHT than among B30.2 (Figure 4C). The majority of variable NLR exons had $\theta_{\pi}/\theta_{w}$ ratios of less than 1 (Figure 4D), indicating an excess of rare alleles.

![Figure 4.](https://cdn.elifesciences.org/articles/98058/elife-98058-fig4-v2.jpg)

**Figure 4.:** Pairwise nucleotide diversity ($\theta_{\pi}$) and Watterson’s estimator of the scaled mutation rate ($\theta_{w}$) for FISNA-NACHT (A) and NLR-associated B30.2 (B) exons. (C) Proportion of exons without any single nucleotide polymorphisms. (D) Ratio of $\theta_{\pi}/\theta_{w}$. Only exons with at least one single-nucleotide polymorphism are shown. The dotted, horizontal line marks a ratio of 1, the expected value under neutrality and constant population size. The black diamonds on box plots denote means, horizontal lines denote medians.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/98058/elife-98058-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Nucleotide diversity ($\theta_{\pi}$) and Watterson estimator ($\theta_{w}$) for FISNA-NACHT exons. (B) Nucleotide diversity ($\theta_{\pi}$) and Watterson estimator ($\theta_{w}$) for NLR-associated B30.2 exons. (C) Proportion of exons which are completely monomorphic. (D) Ratio of $\theta_{\pi}/\theta_{w}$. Only exons with at least one variant are shown. The black, dotted line marks a ratio of 1. The black diamonds on box plots denote means, horizontal lines denote medians.

## Discussion

We sequenced and assembled the FISNA-NACHT and B30.2 exons of hundreds of NLRs from 93 zebrafish. We were able to capture the diversity of this gene family in three wild populations and two laboratory strains, and produced lower coverage NLR data for an additional wild population (DP). Analyzing the 73 zebrafish from populations other than DP, we found evidence that each genome from a wild individual contains only a fraction of more than 1500 identified NLR copies. The number of NLRs found per individual, each with one or more copies, ranged from around 100–550. Some of the lower counts were likely underestimated due to low sequencing depths in specific samples. Since all samples from population DP suffered from low read depth, their analysis is only shown in figure supplements. As targeted sequencing based on bait-capture requires sufficient homology between bait and target, diverged NLR exons may have been missed in our approach. This affects B30.2 exons even more than FISNA-NACHT exons because they are much shorter. However, the observed slow increase in newfound NLR gene copies per sequenced individual after the first few individuals indicates that not many NLRs were missed. The sizes of NLR repertoires differ between zebrafish individuals in the three wild populations.

Nonlinear fitting of NLR counts to Equation 2 suggested that the investigated populations all possess closed pan-NLRomes with roughly 500–600 NLRs in the laboratory strains and around 2000 NLRs in the wild populations. The total numbers of NLRs with a B30.2 exon are about 170 in the laboratory strains and between 1100 and 1500 for the wild populations (Table 1). To explore the entire NLRome of wild populations, large samples are needed: based on the curve-fitting results, we estimate that capturing 90% of the NLRome may require up to several hundred thousand fish (Table 1). Orthogroup clustering with the data from DP resulted in 47 FISNA-NACHT exons which did not occur in any other population. Our results suggest that the pan-NLRome of the entire species must be vastly larger than what we have been able to detect with our limited sample sizes from a limited number of populations. Geographically distant populations – for example, in Nepal or the Western Ghats (Whiteley et al., 2011) – likely harbor many more NLRs which are not present in the populations we sequenced.

Although a few zebrafish assemblies are available in addition to the reference genome, for instance, the fDanRer4.1 assembly from the Tree of Life Initiative (GCA_944039275.1), none of those provide a suitable framework for mapping and analyzing NLRs on their own. One of the hindrances is the fact that the majority of NLR genes are located on the notoriously difficult to assemble long arm of chromosome 4, which harbors plenty of structural variation (McConnell et al., 2023). Furthermore, large multi-copy gene families are difficult to analyze. Read mapping and counting of copies in a particular genome is not trivial. Any downstream analysis which relies on clearly distinguishing paralogous and orthologous comparisons becomes fuzzy, if not impossible. Still, improving sequencing technology and the rising interest in pan-genomic studies Bayer et al., 2020; Sherman and Salzberg, 2020; Liao et al., 2023 have already started to transform the data structures in which genomes are stored, away from a single-reference genome-based view, toward graph-based genome networks. Whether the promise of a thereby improved inventory of structural variation of a species holds up remains still to be seen. Anyway, as shown for the zebrafish NLRs, the availability of a single high-quality reference genome is certainly not sufficient neither to identify nor to understand the diversity of large gene families.

### Properties of the zebrafish NLRome

We have previously demonstrated a substantial reduction in single-nucleotide variation in zebrafish laboratory strains compared to wild populations (Suurväli et al., 2020). Here, we showed that the copy numbers of the NLRome and their variation are also heavily reduced. The most obvious explanation for this observation is the recent population bottleneck which marks the establishment of laboratory strains. The reduction in copy number variation in the major histocompatibility complex (MHC) locus in a population of greater prairie-chicken was attributed to a recent bottleneck as well (Eimes et al., 2011). Additionally, the reduced amount of pathogenic challenges in a laboratory environment could lead to a steady loss of expendable genes. For these reasons, one has to exercise caution when extending conclusions from immune-related studies on laboratory zebrafish to wild zebrafish. The same caution should also be exercised when extending results from laboratory organisms to other species, including human.

Studies have shown that even mammals have hundreds of genes with diverse molecular functions that are affected by copy number variation, even though it rarely involves full genes (Kooverjee et al., 2023; Zarrei et al., 2015). One example of the latter is the MHC locus, which harbors varying numbers of gene copies between closely related species of ruminants (He et al., 2024) and has haplotype-specific copies in mice (Lilue et al., 2018). However, the vast number of NLRs in zebrafish combined with presence/absence variation (McConnell et al., 2023) and high rates of duplication exceeds what has been found in other animals so far. A comparable situation can be found in the NLR genes of the thale cress (A. thaliana). Our predicted number of NLRs in a zebrafish population is on the same scale as the 2127 NLRs found in the thale cress NLRome (Van de Weyer et al., 2019b). Moreover, copy numbers also vary greatly between A. thaliana accessions (Lee and Chae, 2020). A total of 464 conserved, high-confidence orthogroups were identified in A. thaliana, 106–143 of which were defined as the core NLRome because they were found in a subset comprising at least 80% of the accessions (Van de Weyer et al., 2019b). In wild zebrafish, we found a set of 880 NLR genes which were detected in at least one individual from three wild populations, but only 58 NLRs were found in the vast majority (more than 80%) of wild individuals. Although structural similarities of NLRs in plants and animals are thought to be the result of convergent evolution (Yue et al., 2012), it appears that the similarities extend to their evolutionary trajectories. However, the overall number of gene copies as well as the variation in copy numbers within populations and in individual gene repertoires are more extreme in zebrafish than in A. thaliana.

We postulate that as immune genes, many NLR genes are likely shared between populations because they provide a fitness advantage in the defense against common pathogens. The additional NLRs shared among only some of the wild populations and the population-specific NLRs may represent local adaptations to ecological niches. Additionally, there could be functional redundancy within the NLRome, so that different individuals have different NLRs with the same functional role. In general, the fact that hundreds of NLR gene copies are maintained in zebrafish, together with a signature of purifying selection, suggests that the evolution of these genes is far from neutral. Although the expression of fish NLRs is often induced by pathogen exposure (reviewed in Chuphal et al., 2022), the exact function of most zebrafish NLR-C genes remains unclear. It is possible that some of them participate in the formation and activity of inflammasomes (Li, 2018a; Valera-Pérez et al., 2019; Lozano-Gil et al., 2022, Kuri et al., 2017), but we only found the N-terminal effector domains (CARD or PYD) that are typically involved in this function (Petrilli et al., 2005) in a small subset of NLR-C genes.

Although we mainly used the counts of FISNA-NACHT orthogroups to estimate total numbers of NLRs, we also analyzed the B30.2 exons of NLR-C genes. In general, NLR-associated B30.2 exons exhibit patterns of copy number variation that are similar to those seen for FISNA-NACHT. For example, about half of the B30.2 sequences are found in all wild populations, similar to the set of 880 FISNA-NACHT exon sequences conserved among populations.

### What drives the copy number differences?

There are at least two mechanisms which could contribute to the extensive copy number variation seen among zebrafish populations: first, it could be attributed to a high degree of haplotypic variation. Large DNA fragments contain different sets of genes and gene copies, similar to the zebrafish MHC loci (McConnell et al., 2014). Extensive haplotypic variation occurs on the long arm of chromosome 4, the location containing over two-thirds of all NLRs in zebrafish (McConnell et al., 2023). Such segregating haplotype blocks would explain the existence of the core NLRome, but not the frequent presence of genes that occur only in a single individual.

Alternatively or additionally, the evolution of NLR-C genes could be driven by duplication events (Cannon et al., 2004) and gene conversion (Laing et al., 2008). Gene duplications can be caused by unequal recombination, transposon activity, or whole genome/chromosome duplications (Magadum et al., 2013; Kapitonov and Jurka, 2007). The arrangement of NLR-B30.2 genes in clusters on the long arm of chromosome 4 suggests that tandem duplication via unequal crossing-over (Otto et al., 2022) played the most important role in the expansion. Since there are many transposable elements on the long arm of chromosome 4 (Howe et al., 2013), it would be reasonable to assume that at least some of them have assisted in the local expansion and transfer of NLR exons and genes to chromosomes other than chromosome 4. Since our targeted sequencing approach does not elucidate the genomic arrangement of the NLR gene copies and many of them do not have recognizable orthologs in the reference genome, we cannot draw further conclusions about the role of tandem arrays in their evolutionary trajectory.

It is tempting to speculate that chromosome 4 could be a source of NLRs which continuously generates new copies. However, gene gains must be balanced by gene loss to maintain a stable genome size. NLR-C genes may be lost via accumulation of random mutations due to a lack of selective pressure and loss-of-function mutations, but they may also be lost through unequal recombination. This mechanism would allow only NLR genes contributing to the functionality of the immune system to be kept, while others would disappear.

In the similarly evolving plant NLRs, tandem duplication is thought to be the primary driver of NLR gene expansion (Cannon et al., 2004), but they are also often associated with transposable elements. If the diversity of unrelated NLR genes in such distantly related species is driven by common molecular mechanisms, then the same mechanisms might also act on NLRs of other phylogenetic clades and even on unrelated large gene families, such as odorant receptors (Mombaerts, 1999).

### Conclusion

This study showcases an example of the evolutionary dynamics affecting very large gene families. The sheer amount of copy number variation that appears to be present in a single gene family of zebrafish is staggering, with different individuals each having numerous genes that are not present in all others. This can only be caused by diversity-generating mechanisms that are active even now. In this study, we have laid the groundwork for future studies investigating the molecular basis and evolutionary mechanisms contributing to the diversity of large, vertebrate gene families.

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
      <td>Strain (Danio rerio)</td>
      <td>Cologne zebrafish; CGN; KOLN</td>
      <td>Other</td>
      <td></td>
      <td>8 Cologne fish, AG Hammerschmidt, University of Cologne</td>
    </tr>
    <tr>
      <td>Strain (D. rerio)</td>
      <td>Tübingen zebrafish; TU</td>
      <td>Other</td>
      <td></td>
      <td>8 Tübingen fish, AG Hammerschmidt, University of Cologne</td>
    </tr>
    <tr>
      <td>Biological sample (D. rerio)</td>
      <td>DP</td>
      <td>Other</td>
      <td></td>
      <td>20 wild fish, Dandiapalli, India (22.22155, 84.79430)</td>
    </tr>
    <tr>
      <td>Biological sample (D. rerio)</td>
      <td>CHT</td>
      <td>Other</td>
      <td></td>
      <td>20 wild fish, Chittagong, Bangladesh (22.47400, 91.78300)</td>
    </tr>
    <tr>
      <td>Biological sample (D. rerio)</td>
      <td>KG</td>
      <td>Other</td>
      <td></td>
      <td>20 wild fish, Leturakhal, India (22.26189 87.27881)</td>
    </tr>
    <tr>
      <td>Biological sample (D. rerio)</td>
      <td>SN</td>
      <td>Other</td>
      <td></td>
      <td>20 wild fish, Santoshpur, India (22.93765 88.55311)</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Baits; RNA baits; hybridization baits</td>
      <td>Daicel Arbor Biosciences</td>
      <td>Cat# Mybaits-1-24</td>
      <td>Sequences available in Figure 2—source data 2</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>MagAttract HMW DNA Kit</td>
      <td>QIAGEN</td>
      <td>Cat# 67563</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>NucleoSpin Tissue Kit</td>
      <td>MACHEREY-NAGEL</td>
      <td>Cat# 740952.50</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>NEBNext Ultra II DNA Library Prep Kit</td>
      <td>New England Biolabs</td>
      <td>Cat# E7645L</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>NEBNext Multiplex Oligos for Illumina</td>
      <td>New England Biolabs</td>
      <td>Cat# E7335L</td>
      <td>Index Primers Set 1</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Kapa HiFi Hotstart Readymix</td>
      <td>Kapa Biosystems</td>
      <td>Cat# 07958935001</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>PreCR Repair Mix</td>
      <td>New England Biolabs</td>
      <td>Cat# M0309L</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>SMRTbell Template Prep Kit 1.0-SPv3</td>
      <td>Pacific Biosciences</td>
      <td>Cat# 100-991-900</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>GRCz11</td>
      <td>NCBI RefSeq</td>
      <td>RefSeq:GCF_000002035.6</td>
      <td>Zebrafish reference genome</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>M220 miniTUBE, Red</td>
      <td>Covaris</td>
      <td>Cat# 4482266</td>
      <td>Used to shear DNA on Covaris ultrasonicator</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>DB MyOne Streptavidin C1</td>
      <td>Thermo Fisher Scientific</td>
      <td>Cat# 65001</td>
      <td>Used to retrieve bait-bound DNA fragments</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>AMPure XP</td>
      <td>Beckman Coulter</td>
      <td>Cat# A63881</td>
      <td>Size selection beads</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Ampure PB</td>
      <td>Pacific Biosciences</td>
      <td>Cat# 100-265-900</td>
      <td>PacBio-compatible size selection beads</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>lima</td>
      <td>Pacific Biosciences</td>
      <td>lima:v1.0.0; lima:v1.8.0; lima:v1.9.0; lima:v1.11.0</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>ccs</td>
      <td>Pacific Biosciences</td>
      <td>ccs:v4.2.0</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>pbmarkdup</td>
      <td>Pacific Biosciences</td>
      <td>pbmarkdup:v1.0.0</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>pbmm2</td>
      <td>Pacific Biosciences</td>
      <td>pbmm2:v1.3.0</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>samtools</td>
      <td>https://doi.org/10.1093/bioinformatics/btp352</td>
      <td>samtools:v1.7</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>EMBOSS</td>
      <td>https://doi.org/10.1016/s0168-9525(00)02024-2</td>
      <td>EMBOSS:v6.6.0.0</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>HMMER</td>
      <td>https://doi.org/10.1093/bioinformatics/btt403</td>
      <td>HMMER:v3.2.1</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>blastn</td>
      <td>https://doi.org/10.1186/1471-2105-10-421</td>
      <td>blastn:v2.11.0+</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>hifiasm</td>
      <td>https://doi.org/10.1038/s41592-020-01056-5</td>
      <td>hifiasm:v0.15.4-r347</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>get_homologues</td>
      <td>https://doi.org/10.1128/AEM.02411-13</td>
      <td>get_homologues:x86_64–20220516</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>deepvariant</td>
      <td>https://doi.org/10.1038/nbt.4235</td>
      <td>deepvariant:r1.0</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GLnexus</td>
      <td>https://doi.org/10.1101/343970</td>
      <td>Glnexus:v1.2.7–0-g0e74fc4</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>vcftools</td>
      <td>https://doi.org/10.1093/bioinformatics/btr330</td>
      <td>vcftools:v0.1.16</td>
      <td></td>
    </tr>
  </tbody>
</table>

### Samples

Wild zebrafish from four sites in India and Bangladesh (Figure 1B) had been collected in the frame of other projects (e.g., Whiteley et al., 2011; Shelton et al., 2020). Laboratory zebrafish from the Tübingen (TU) and Cologne (CGN) strains were provided by Dr. Cornelia Stein from the Hammerschmidt laboratory (Institute for Zoology, University of Cologne). All samples were stored in 95% ethanol until use. Tail fins from 20 fish per wild population and 8 fish per laboratory strain were used as starting material for the subsequent steps.

### DNA extraction, exon capture, and sequencing

Genomic DNA was extracted with kits from QIAGEN (MagAttract HMW kit) and MACHEREY-NAGEL (Nucleospin Tissue Kit), followed by shearing with red miniTUBEs on the Covaris M220 ultrasonicator. Nicks in the DNA were repaired with PreCR Repair Mix (New England Biolabs). Samples were barcoded with the NEBNext Ultra II DNA Library Prep Kit, then pooled together in batches of four or eight (details provided in Appendix 1). RNA baits for the exon capture (Daicel Arbor Biosciences) were custom-designed to target immune genes of interest (mainly NLRs, but also some others) based on version GRCz10 of the reference genome. Bait sequences and target locations are available in Figure 2—source data 2. Exon capture and PacBio library preparation were both done according to a protocol adapted from Witek et al., 2016. Libraries were sequenced at the Max Planck-Genome-Centre Cologne, with PacBio Sequel and Sequel II. Additional details are provided in Appendix 1.

### Read processing, mapping, and clustering

Raw sequences were de-multiplexed with lima. Consensus sequences of DNA fragments with at least three passes (CCS reads) were inferred with ccs, followed by PCR duplicate removal with pbmarkdup. All read mapping was done with pbmm2 (v.1.3.0), a PacBio wrapper for minimap2 (Li, 2018a). lima, ccs, pbmarkdup, and pbmm2 were all provided by Pacific Biosciences. Mapped files were processed and filtered with samtools (v1.7) (Li et al., 2009). De novo assemblies were generated with hifiasm (v0.15.4-r347) (Cheng et al., 2021). Tools from the HMMER suite (v3.2.1) (Wheeler and Eddy, 2013) were used to detect the presence of NLR-associated sequences. Contigs containing FISNA-NACHT or B30.2 were sorted into orthoclusters using get_homologues (build x86 64–20220516) (Contreras-Moreira and Vinuesa, 2013) and blastn (v2.11.0+) (Altschul et al., 1990). Orthoclusters for which pbmm2 did not align any CCS reads to the representative sequence with at least 95% identity were excluded from further analyses. Further details are provided in Appendix 1.

### Modeling

To estimate the full size of each population’s NLR repertoire, we calculated the increment in the total number of identified NLR exon sequences when adding sequence data from one additional individual of a population to a set of already surveyed individuals. As noted earlier (Medini et al., 2020), these increments are well approximated by a power-law decay.

Briefly, given a sample of $n$ individuals, there are

$$
w_{n}(x)=(\frac{n}{x−1})(n−(x−1))=(\frac{n}{x})x
$$

ways to choose $x−1$ individuals from the entire sample and add another – not yet chosen – one. For each $x$, we calculated the increment in the number of identified exon sequences and averaged over all possible choices of individuals. Summation of the average increments yields the total number of exons identified with $x$ individuals, as plotted in Figure 3D. Then, we fitted the nonlinear function

$$
y=\alphaH(x,\beta)
$$

where $H(x,\beta)$ is the generalized harmonic number with parameter $\beta$, that is,

$$
H(x,\beta)=\sumk=1x\frac{1}{k^{\beta}}
$$

It represents the sum of increments, decaying according to a power-law, with parameters $\alpha$ (intercept) and $\beta$ (decay rate). Importantly, if $\beta>1$, the series in Equation 3 converges and its limit may be interpreted as the size of a closed NLRome. The NLRome is open, if $\beta\leq1$. Values of the fitted parameters and saturation limits are presented in Table 1.

### Genetic diversity

Single-nucleotide genotypes in each fish were identified from the.bam output of pbmm2 by using deepvariant (r1.0) (Poplin et al., 2018) with the PacBio model. Joint genotyping of the individual samples was done with glnexus (v1.2.7–0-g0e74fc4) (Yun et al., 2021) with its deepvariant-specific setting. Per-site $\theta_{\pi}$ of the NLR exons was calculated with vcftools (v0.1.16) (Danecek et al., 2011). Watterson’s estimator of the scaled mutation rate is

$$
\theta_{w}=\frac{S}{H(n−1,1)l}
$$

where $S$ is the number of segregating sides seen in a sample of $n$ aligned sequences, each of size $l$ (here, 1761 bp for the FISNA-NACHT exons and 540 bp for the B30.2 exons).

Under neutrality (all alleles confer the same fitness to an individual) and constant population size over time, one expects equality $\theta_{\pi}=\theta_{w}$.

### Data visualization

Plots and heat maps were created in RStudio (v2022.07.2) with R (v4.2.1) using ggplot2 (v3.3.6) or xmgrace (v5.1.25; https://plasma-gate.weizmann.ac.il/Grace/). Venn diagrams were created via BioVenn (Hulsen et al., 2008; Figure 3B) and ggvenn (v0.1.9) (Figure 1A). Final processing of the images was done in Inkscape (v1.1.2; https://inkscape.org/).
