# Structurally distributed surface sites tune allosteric regulation

## Authors

- James W McCormick<sup>1</sup> ([ORCID: 0000-0001-7573-2300](https://orcid.org/0000-0001-7573-2300))
- Marielle AX Russo<sup>1</sup>
- Samuel Thompson<sup>3</sup>
- Aubrie Blevins<sup>1</sup>
- Kimberly A Reynolds<sup>1</sup> ([ORCID: 0000-0003-4805-0317](https://orcid.org/0000-0003-4805-0317)) †

### Affiliations

1. The Green Center for Systems Biology, University of Texas Southwestern Medical Center Dallas United States
2. Department of Biophysics, University of Texas Southwestern Medical Center Dallas United States
3. Department of Bioengineering, Stanford University Stanford United States

† Corresponding author

## Abstract

Our ability to rationally optimize allosteric regulation is limited by incomplete knowledge of the mutations that tune allostery. Are these mutations few or abundant, structurally localized or distributed? To examine this, we conducted saturation mutagenesis of a synthetic allosteric switch in which Dihydrofolate reductase (DHFR) is regulated by a blue-light sensitive LOV2 domain. Using a high-throughput assay wherein DHFR catalytic activity is coupled to E. coli growth, we assessed the impact of 1548 viable DHFR single mutations on allostery. Despite most mutations being deleterious to activity, fewer than 5% of mutations had a statistically significant influence on allostery. Most allostery disrupting mutations were proximal to the LOV2 insertion site. In contrast, allostery enhancing mutations were structurally distributed and enriched on the protein surface. Combining several allostery enhancing mutations yielded near-additive improvements to dynamic range. Our results indicate a path toward optimizing allosteric function through variation at surface sites.

## Introduction

In allosteric regulation, protein activity is modulated by an input effector signal spatially removed from the active site. Allostery is a desirable engineering target because it can yield sensitive, reversible, and rapid control of protein activity in response to diverse inputs (Dagliyan et al., 2019; Pincus et al., 2017; Raman et al., 2014). One common approach for achieving allosteric regulation in both engineered and evolved systems is through domain insertion: the transposition, recombination, or otherwise fusion of an ‘input’ domain into an ‘output’ domain of interest (Aroul-Selvam et al., 2004; Dagliyan et al., 2016; Ostermeier and Benkovic, 2000; Nadler et al., 2016). In natural proteins, domain insertions and rearrangements play a key role in generating regulatory diversity, with kinases serving as a prototypical example (Fan et al., 2018; Huse and Kuriyan, 2002; Peisajovich et al., 2010; Shah et al., 2018). In engineered proteins, domain insertions have been used to generate fluorescent metabolite biosensors (Nadler et al., 2016), sugar-regulated TEM-1 β-lactamase variants (Guntas et al., 2005), and a myriad of light-controlled proteins including kinases, ion channels, guanosine triphosphatases, guanine exchange factors, and Cas9 variants (Dagliyan et al., 2016; Wang et al., 2016; Karginov et al., 2011; Toettcher et al., 2013; Shaaya et al., 2020; Coyote-Maestas et al., 2019; Richter et al., 2016). In all cases, domain insertion provides a powerful means to confer new regulation in a modular fashion.

However, naively created domain insertion chimeras sometimes exhibit relatively modest allosteric dynamic range, with small observed differences in activity between the constitutive and activated states (Lee et al., 2008). These fusions then require further optimization by either evolution or empirical mutagenesis, but general principles to guide this process are largely absent. Which mutations tune or improve an allosteric system? Because we lack comprehensive studies of allosteric mutational effects in either engineered or natural systems, it remains unclear whether such mutations are common or rare, and what magnitude of allosteric effect we might typically expect for single mutations. Additionally, it is not obvious if such mutations are structurally distributed or localized (for example, to the insertion site). Answers to these questions would inform practical strategies for optimizing engineered systems and provide insight into the evolution of natural multi-domain regulation in proteins.

To address these questions, we performed a deep mutational scan of a synthetic allosteric switch: a fusion between the E. coli metabolic enzyme Dihydrofolate Reductase (DHFR) and the blue-light sensing LOV2 domain from A. sativa (Lee et al., 2008; Reynolds et al., 2011). This modestly allosteric chimera shows a 30% increase in DHFR velocity in response to light. Focusing on mutations to the DHFR residues, we found that only a small fraction (4.4%) of the mutations that retained DHFR activity had a statistically significant impact on allostery. Individual mutations exhibited generally modest effect sizes; the most allosteric single mutant characterized (H124Q) yielded a twofold increase in velocity in response to light relative to the starting construct. Structurally, allostery disrupting mutations tended to cluster near the LOV2 insertion site and were modestly enriched at both conserved and co-evolving amino acid positions. In contrast, allostery enhancing mutations were distributed across the protein, and strongly associated with the protein surface. We observed that combining a few of these mutations yielded near-additive enhancements to allosteric dynamic range. Collectively, our data elucidates practical strategies for optimizing engineered systems, and shows that weakly conserved, structurally distributed surface sites can contribute to allosteric tuning.

## Results

### Characterization of an unoptimized allosteric fusion of DHFR-LOV2

To begin our study of allostery tuning mutations, we selected a previously characterized synthetic allosteric fusion between DHFR and LOV2 generated in earlier work (Lee et al., 2008; Reynolds et al., 2011). In this fusion, the LOV2 domain of A. sativa is inserted between residues 120 and 121 of the E. coli DHFR βF-βG loop; we refer to this construct as DL121 (Figure 1A,B). The choice of LOV2 insertion site was guided by Statistical Coupling Analysis (SCA), an approach for analyzing coevolution between pairs of amino acids across a homologous protein family (Rivoire et al., 2016; Lockless and Ranganathan, 1999; Halabi et al., 2009). A central finding of SCA is that co-evolving groups of amino acids, termed sectors, often form physically contiguous networks in the tertiary structure that link allosteric sites to active sites (Halabi et al., 2009; Süel et al., 2003; Pincus et al., 2018). To create the DL121 fusion, Lee et al. followed the guiding principle that sector connected surface sites in DHFR might serve as preferred sites (or ‘hot spots’) for the introduction of allosteric regulation (Lee et al., 2008). The resulting DL121 fusion covalently attaches the N- and C-termini of LOV2 into a sector connected surface on DHFR, and displays a twofold increase in DHFR hydride transfer rate (khyd) in response to blue light (Lee et al., 2008). Under steady-state conditions, we measured a 28% increase in the turnover number (kcat) in response to light and a statistically insignificant change in the Michaelis constant (Km) (Figure 1C). Thus, the DL121 fusion is modestly allosteric in vitro. As DHFR has no known natural allosteric regulation, the LOV2 insertion confers a new, evolutionarily unoptimized regulatory input.

![Figure 1.](https://cdn.elifesciences.org/articles/68346/elife-68346-fig1-v2.jpg)

**Figure 1.:** (A) Composite structures of the individual DHFR and LOV2 domains (PDB ID: 1R × 2 and 2V0U), indicating the LOV2 insertion site between positions 120 and 121 of DHFR (Sawaya and Kraut, 1997; Halavaty and Moffat, 2007). DHFR is in gray cartoon, NADP co-factor in green sticks, and folate substrate in yellow sticks. In LOV2 signaling, blue light triggers the formation of a covalent adduct between a cysteine residue (C450) and a flavin mononucleotide (FMN, yellow sticks) (Salomon et al., 2001; Crosson and Moffat, 2002; Swartz et al., 2002) and associated unfolding of the C-terminal Jα-helix (red cartoon); this order-to-disorder transition is used for regulation in several synthetic and natural systems (Pudasaini et al., 2015; Glantz et al., 2016). (B) DHFR loop conformational changes near the LOV2 insertion site. While the mechanism of DHFR regulation by LOV2 is currently unknown, inspecting the native DHFR structure provides some insight. The substrate-bound Michaelis complex of native DHFR is in the ‘closed’ conformation (gray cartoon), while the product ternary complex is in the ‘occluded’ state (purple cartoon). The βF-βG loop, where LOV2 is inserted, is highlighted in cyan. In native DHFR, hydrogen bonds between this loop (Asp122) and the Met20 loop (Gly15, Glu17) are thought to stabilize the closed conformation (Sawaya and Kraut, 1997; Schnell et al., 2004). Mutations to positions 121 and 122 reduce activity and cause the enzyme to prefer the occluded conformation (Cameron and Benkovic, 1997; Mhashal et al., 2018; Miller and Benkovic, 1998). (C) Steady state Michaelis Menten kinetics for the DL121 fusion under lit (blue) and dark (gray) conditions. The kcat of DHFR increases 28% in response to light; the difference in Km is statistically insignificant (Supplementary file 1a). Error bars represent standard deviation for three replicates. (D) Quantifying the allosteric effect of mutation. Allostery for the DL121 fusion is reported as the ratio between lit and dark velocity. The effect of a mutation on allostery is then computed as the ratio of mutant allostery to wt-DL121 allostery (bottom blue box).

But can this relatively small allosteric effect generate measurable physiological differences that could provide the basis for evolutionary selection? DHFR catalyzes the reduction of 7,8-dihydrofolate (DHF) to 5,6,7,8-tetrahydrofolate (THF) using NADPH as a co-factor. THF then serves as a one-carbon donor and acceptor in the synthesis of thymidine, purine nucleotides, serine, glycine, and methionine. Because of these critical metabolic functions, DHFR activity is strongly linked to growth rate, and under appropriate conditions, E. coli growth rate can be used as a proxy for DHFR activity (Reynolds et al., 2011; Thompson et al., 2020). Prior work found that the modest in vitro allosteric effect of DL121 conferred a selectable growth rate advantage in vivo: when an E. coli DHFR deletion strain (ER2566 ΔfolAΔthyA) was complemented with DL121, the resulting strain grew 17% faster in the light than in the dark (Reynolds et al., 2011). Thus, DL121 is a system where: (1) allosteric control is rapidly and reversibly applied, (2) the allosteric effects on activity can be readily quantified both in vitro and in vivo, and (3) there remains potential for large improvements in regulatory dynamic range through mutation.

### A high-throughput assay to resolve small changes in DHFR catalytic activity

Our goal was to measure the effect of every single amino acid mutation in DHFR on the allosteric regulation of DL121. To do this, we aimed to follow a strategy loosely akin to a double mutant cycle (Figure 1D). The starting DL121 construct shows so-called V-type allostery, in which the effector (light) regulates the catalytic turnover number (kcat) (Carlson and Fenton, 2016). Thus, allostery can be quantified as the ratio of kcat between lit and dark states. More generally, allostery might be considered as a ratio of velocities (v = kcat [S]/(Km + [S])) between the lit and dark states, as the allosteric effector could regulate turnover, substrate affinity, or both. In either case, we defined the allosteric effect of mutation as the fold change in allosteric regulation upon mutation (Figure 1D, blue box). We sought to infer this quantity for every mutation in a saturation mutagenesis library of DHFR by using growth rate as a proxy for catalytic activity.

As in prior work, we measured the growth rate of many E. coli strains in parallel by using next generation sequencing (NGS) to monitor the frequency of individual DHFR mutants over time in a mixed culture (Figure 2; Reynolds et al., 2011; Thompson et al., 2020). Allele frequencies $(f_{a})$ at each time point (t) were normalized as follows: $f_{a}=ln⁡\frac{N_{a}}{N_{WT}}_{t}-ln\frac{N_{a}}{N_{WT}}_{t=0}$ where $N_{a}$ and $N_{WT}$ are the number of mutant and wildtype (WT) counts at a given time point. By performing a linear fit of the log normalized allele frequencies vs. time we calculated a slope corresponding to relative growth rate: this value is the difference in growth rate for the mutant relative to a reference ('WT') construct.

![Figure 2.](https://cdn.elifesciences.org/articles/68346/elife-68346-fig2-v2.jpg)

**Figure 2.:** (A) The turbidostat. The instrument has 15 individual growth chambers (vials), positioned on a stir plate inside an incubator. Illumination was provided by blue LEDs in each vial holder. (B) Log-normalized relative allele frequency over time for 11 DHFR point mutations of known catalytic activity and the DL121 fusion. Allele frequency (colored circles) was determined by next-generation sequencing of mixed-population culture samples at each time point. All frequencies were normalized to t = 0 and WT DHFR (no LOV2 insertion). Error bars reflect standard error across four measurements, they are sometimes obscured by the marker. The slope for each line of best fit provides the growth rate of each mutant allele relative to WT DHFR. (C) Relative growth rate vs. log10(velocity) for the 11 DHFR mutants and DL121 as characterized in panel B. Color coding of mutations is matched to panel B. Error bars reflect standard error of the mean over four replicates. The dashed line was fit by linear regression to all mutants in the linear regime (M42F excluded).

As individual mutations tend to exhibit modest effects on allosteric regulation, we optimized the linear regime and resolution of the growth rate assay in two ways (Reynolds et al., 2011). First, we grew the E. coli populations in a turbidostat outfitted with blue LEDs to activate LOV2 (Figure 2A). The turbidostat maintains each culture in exponential growth by dynamically sensing optical density and adjusting media dilution rate accordingly Toprak et al., 2013; this ensures near-constant media conditions and eliminates the need for manual serial dilutions. Second, we selected media conditions – M9 minimal media with 0.4% glucose and 1 µg/ml thymidine supplementation – in which growth rate can resolve subtle differences in catalytic activity near the DL121 fusion. We evaluated the resolution of our assay using a ‘standard curve’ of 11 point mutations of known catalytic activity in non-chimeric DHFR (Figure 2B). Under these conditions, we observed a log-linear relationship between relative growth rate and DHFR velocity over nearly four orders of magnitude; this relationship saturates (plateaus) for the most active mutants (WT and M42F, Figure 2C). Importantly, the relative growth rate and velocity of DL121 were near the center of the linear regime of our assay.

In using velocity to describe our data, we have incorporated two assumptions: (1) we presume minimal variation in protein abundance between mutants (enzyme concentration is equal to one) and (2) we fix the substrate concentration at 25 µM, which was previously reported as the endogenous concentration for WT E. coli (Kwon et al., 2008). Individual mutations may cause variation in protein abundance, but because allostery concerns a relative change in activity, light-independent differences in abundance can be removed by appropriate normalization (as discussed further below).

As previously observed, the exponential divergence of mutants with different growth rates in a population makes it possible to detect even small biochemical effects (Breslow et al., 2008). More specifically, we can discriminate a change of ±0.02 µM−1 s-1 in catalytic power (kcat/Km) under these conditions. This level of precision is on par with – and in some cases better than – literature-reported errors for in vitro steady state kinetics measurements of DHFR (Reynolds et al., 2011; Wagner et al., 1992; Huang et al., 1994). Consequently, we can resolve small catalytic and allosteric effects of mutations on DL121 through this high-throughput growth-based assay.

### Deleterious mutations are enriched at conserved, coevolving positions in DHFR

In order to map the coupling of individual DHFR positions to light, we constructed a deep mutational scanning library over all DHFR positions in the DL121 fusion (Figure 3—figure supplements 1–2). Then, we measured the growth rate effect of each mutation in triplicate under both lit and dark conditions using the above-described assay (Figure 3A–C, Figure 3—figure supplements 3–4, Figure 3—source data 1). In this experiment, all growth rates were calculated relative to the unmutated DL121 fusion, which itself exhibits reduced activity (and growth rate) compared to WT DHFR. Mutations fell into four broad categories in terms of growth rate effects: neutral, uniformly deleterious (Figure 3A), uniformly beneficial (Figure 3B), or light dependent (and thus allosteric, Figure 3C). We were unable to measure growth rate for 891 of the 3021 possible missense mutations (19 substitutions over 159 positions): 226 (7.5%) were missing at the start of the experiment (t = 0) for one or more replicates (referred to as ‘no data’), and an additional 665 (22%) were depleted from the library before reaching the minimum of three time points required for growth rate estimation (we refer to these as null mutants, see also Materials and methods, Figure 3—figure supplement 4). We interpreted these 665 rapidly depleting null mutants as highly deleterious to growth rate and thus DHFR activity. The relative growth rates for the remaining 2130 mutations (70.5%) were highly reproducible, with a correlation coefficient between replicate pairs above 0.9 (Figure 3—figure supplement 3).

![Figure 3.](https://cdn.elifesciences.org/articles/68346/elife-68346-fig3-v2.jpg)

**Figure 3.:** (A-C) Representative relative growth rate trajectories for three mutations. (A) DL121 D27N was deleterious in both lit and dark conditions. (B) DL121 D122W was advantageous under both lit and dark conditions. (C) DL121 E154R was deleterious in the dark, and near neutral in the light. Solid lines were obtained by linear regression; the slope of these provides the difference in growth rate relative to the unmutated DL121 construct. Relative growth rates were measured in triplicate for each mutant under lit (blue) and dark (gray) conditions. (D) Distribution of relative growth rates under dark conditions. The distribution for all mutations with measurable growth rate effects is in gray (‘null data’ and ‘no data’ excluded); the distribution for sector mutations is in navy. The relative growth rate of DL121 D27N, a mutation that severely disrupts catalytic activity, is indicated with a cyan dashed line. (E) The fraction of DL121 mutations with measurable growth rates that can be categorized as: DHFR surface, core, sector, and evolutionarily conserved (see Materials and methods for definitions). The fraction is shown for both the complete library (gray bars), and the library after removing mutations with low growth (growth rate <= DL121 D27N). The absolute number of mutations is shown above each bar. A contingency table summarizes the overlap between mutations in the sector (at a p-value cutoff of 0.010), and the mutations that yield low growth (growth rate <= DL121 D27N). (F) Structural distribution of positions enriched for mutations with growth rates as low as or lower than DL121 D27N (red spheres). The DHFR backbone is in gray cartoon, the folate substrate in yellow sticks, and the NADP co-factor in green sticks. (G) Relationship of the sector (navy blue surface) to positions enriched for growth-rate disrupting mutations (red spheres, same as in F).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/68346/elife-68346-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Log10(counts) of all possible mutations in DHFR domain of DL121 chimeric protein library at time point zero. The y axis corresponds to positions on E. coli DHFR domain as numbered in PDB ID: 1R × 2. A red star indicates the location of the LOV2 domain insertion. The x axis corresponds to possible mutations. Wild-type residues are shown in gray; positions with no counts are shown in white.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/68346/elife-68346-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** A histogram of the number of counts per mutant at time point zero. The median and mean number of counts is shown as a dashed and solid red line, respectively.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/68346/elife-68346-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** The relative growth rate (see Materials and methods) for each mutant is compared across all three lit (A-C) and dark (D-F) replicates. The line of best fit is indicated with a blue dashed line. The teal dashed lines represent the growth rate of DL121-D27N; mutants with a relative growth rate below this cutoff were considered near catalytically inactive and excluded from analysis of allostery.

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/68346/elife-68346-fig3-figsupp4-v2.jpg)

**Figure 3—figure supplement 4.:** (A) Relative growth rate in the dark. (B) Relative growth rate in the light. Blue and red indicate mutations with deleterious and beneficial effects on growth rate respectively. White squares with black outlines mark the WT residue at each position. Mutations missing from the library (‘no data’) are colored gray, and mutations that did not have sufficient counts for at least three time points (‘null data’, no relative growth rate could be fit) are colored navy.

![Figure 3—figure supplement 5.](https://cdn.elifesciences.org/articles/68346/elife-68346-fig3-figsupp5-v2.jpg)

**Figure 3—figure supplement 5.:** Comparison of growth rates as doublings per hour for three enzymes: nonchimeric E. coli DHFR with a D27N mutation (rendering it catalytically inactive), the unmutated fusion protein, DL121, and DL121 combined with the D27N mutation. All three mutants were grown in a 96-well plate in M9 media supplemented with either no thymidine, 1 μg/ml thymidine (the same media conditions as the experiments in this work), or 50 μg/ml thymidine at 30°C. Error bars represent standard deviation across six replicates.

![Figure 3—figure supplement 6.](https://cdn.elifesciences.org/articles/68346/elife-68346-fig3-figsupp6-v2.jpg)

**Figure 3—figure supplement 6.:** (A) Structural distribution of positions enriched for mutations with growth rates as low as or lower than DL121 D27N (indicated with red spheres). The DHFR backbone is in gray cartoon, the folate substrate in yellow sticks, and the NADP co-factor in green sticks. (B) Relationship of evolutionarily conserved positions (light blue surface) to positions enriched for growth-rate disrupting mutations (red spheres, same as in A). (C) A contingency table summarizes the overlap between conserved positions, and the mutations that yield low growth (growth rate <= DL121 D27N).

Before examining the allosteric effects of mutations, we first considered the effects of mutations on growth rate (and thus DHFR activity) in a single growth condition (dark). Prior work has found that deleterious mutations are enriched at evolutionarily conserved positions and within the protein sector (McLaughlin et al., 2012). The DHFR sector was defined by analyzing coevolution in a multiple sequence alignment of native DHFR domains, so we wished to examine if sector positions were indeed critical to function in the chimeric DL121 fusion. Good correspondence between the DHFR sector, evolutionary conservation, and deleterious mutations in DL121 would provide confidence that the core functional elements of native DHFR remain intact in the chimera. The vast majority of mutations were at least modestly deleterious to growth, with a median relative growth rate of −0.084 in the dark and −0.083 in the light (Figure 3D). A cluster of beneficial mutations was observed just before the LOV2 insertion site at position 121 in both conditions, suggesting some potential to compensate for the inserted LOV2 (Figure 3—figure supplement 4). The overall distribution of fitness effects shows some differences relative to prior DMS studies of natural proteins including native E. coli DHFR (Thompson et al., 2020; Garst et al., 2017). First, the distribution of fitness effects for mutations in natural proteins is often centered around neutral, implying a certain degree of mutational robustness (McLaughlin et al., 2012; Stiffler et al., 2015). Secondly, DMS of native DHFR – under experimental conditions designed to resolve mutational effects near WT – revealed many beneficial (activating) mutations (Thompson et al., 2020). There are two explanations for the relative paucity of beneficial and neutral mutations in the present dataset. First, the DL121 fusion is comparably less robust because the unoptimized LOV2 insertion introduces an initial compromise to DHFR function. Secondly, the conditions of our assay (both expression and media) differ from prior work (Thompson et al., 2020) and were selected to resolve mutational effects near DL121; consequently, mutations with native-like (or better) activity are in the saturating, non-linear regime of our assay.

To identify the slowest growing – and presumably near, or entirely, inactivating – mutations, we applied an empirical growth rate cutoff of −0.13 to the lit and dark growth rates. This corresponds to the growth rate for DL121 D27N; D27N is an active site mutation that strongly reduces the activity of WT DHFR (Figure 2B,C). The DL121 D27N mutant grows very slowly in the conditions of our assay and is inviable in the absence of thymidine supplementation (Figure 3—figure supplement 5). We found that mutations with growth rates at or below this cutoff (including the null mutants) were significantly enriched in both the sector (p=7.9×10−8, Figure 3E, Supplementary file 1b) and at evolutionarily conserved positions (p=8.7×10−20, Figure 3—figure supplement 6, Supplementary file 1c). When mapped to the WT DHFR structure, positions enriched for deleterious mutations surround the active site and co-factor binding pocket (Figure 3F), structurally overlap with the sector (Figure 3G), and include a number of positions known to play a critical role in WT DHFR catalysis (e.g. W22, D27, M42, and L54) (Howell et al., 1986; Fierke et al., 1987). These data are consistent with the view that sector positions continue to play a key role in conferring DHFR catalytic activity in the DL121 fusion.

Following the thinking that (near) inactive DHFR variants are both inherently non-allosteric and associated with the least reproducible growth rate measurements (Figure 3—figure supplement 3), we removed the set of 1247 slow-growing (growth rate <−0.13) and null mutations prior to the analysis of allostery. The retained 1548 mutations – representing 51% of the growth assay data – remain well-distributed between the DL121 surface, core, sector, and evolutionarily conserved positions (Figure 3E). These present a high-confidence and representative subset of the data for evaluating mutational effects on DL121 allosteric regulation.

### Allostery tuning mutations are sparse

To compute the allosteric effect of mutation, we considered the triplicate measurements of lit and dark relative growth rate for each mutant (Figure 3A–C). Given the log-linear relationship between growth rate and DHFR velocity (Figure 2C), subtracting growth rates approximates log-ratios of velocities. Thus, we estimated the allosteric effect of mutation by taking the difference in the average relative growth rates between lit and dark conditions:

In the above equations, rgr is relative growth rate (which is directly measured in our sequencing-based assay) and gr refers to absolute growth rate. Accordingly, positive values indicate allostery enhancing mutations and negative values indicate allostery disrupting mutations (Figures 1D and 4A). Of the 1548 mutations evaluated, the allosteric effect is normally distributed with a mean near zero (µ = 0.0017, Figure 4—figure supplement 1). To assess the statistical significance of allosteric effects, we computed a p-value for each mutation by unequal variance t-test under the null hypothesis that the lit and dark replicate measurements have equal means. These p-values were compared to a multiple-hypothesis testing adjusted p-value of p=0.016 determined by Sequential Goodness of Fit (SGoF, Figure 4B; Carvajal-Rodriguez and de Uña-Alvarez, 2011). Under these criteria, only 69 mutations (4.5% of all viable mutants) significantly influenced allostery: 56 mutations enhanced allostery while 13 disrupted allostery. We did not observe a strong association between the magnitude of growth rate effect and the allosteric effect size. Allostery-influencing mutations spanned a wide range of growth rates and exhibited comparatively modest effects on light regulation (Figure 4C).

![Figure 4.](https://cdn.elifesciences.org/articles/68346/elife-68346-fig4-v2.jpg)

**Figure 4.:** (A) Heatmap of mutational effects on allostery. Blue indicates allostery disrupting mutations, and red indicates allostery enhancing mutations. White squares with black outlines mark the WT residue at each position. Mutations missing from the library (‘no data’) are colored gray, and mutations that did not have sufficient sequencing counts for at least three time points (‘null data’) are colored navy. The LOV2 domain insertion site is indicated with a red star. (B) Volcano plot indicating the statistical significance of the light-dark growth rate difference (y-axis) as a function of relative growth rate difference (x-axis). p-Values were computed using a t-test across triplicate light and dark measurements. Individual points correspond to mutations; mutations on the left (yellow) side of the graph are allostery disrupting, while mutations on the right (blue) are allostery enhancing. Two cutoffs for statistical significance are indicated with dashed gray lines – both a standard value of p=0.05, and an adjusted p-value of 0.016, obtained by using Sequential Goodness of Fit (SGoF) to account for multiple hypothesis testing. Mutations selected for further in vitro experimental characterization are colored red and labeled. S148C and E154R did not yield sufficient quantities of active protein for further in vitro characterization. (C) Triplicate relative growth rate measurements under lit (blue) and dark (gray) conditions for all mutations with statistically significant allostery at the adjusted p-value (p<=0.016). The mutations are sorted by dark growth rate; mutations selected for in vitro characterization are marked with red asterisks. (D) Relationship between the allosteric effect as measured in vivo and in vitro. As we expect a log-linear relationship, we compare the ratio of velocity at 25 µM DHF (along x) to the exponent of the relative growth rate difference (along y). The relative growth rate difference under lit and dark conditions is the mean of triplicate measurements, error bars indicate SEM. All mutant effects on growth rate were measured in the same experiment (corresponding to a subset of the data in panel B) with the exception of DL121 C450S. The relative growth rate for this light-insensitive LOV2 mutant was measured in the ‘calibration curve’ experiment shown in Figure 2 (see also Materials and methods). The ratio between velocity in the light and velocity in the dark reflects the mean of triplicate measurements; error bars indicate SEM. The green line was fit by linear regression.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/68346/elife-68346-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** The allosteric effect of all viable mutants is shown in gray with the mean allosteric effect of 0.0017 shown as a red dotted line. The allosteric effect of viable mutants in the sector is shown overlaid in blue. The mean allosteric effect of sector positions is −0.0005. The cutoff for sector identity used is a p-value of 0.01 as calculated in Reynolds et al., 2011 (Rivoire et al., 2016).

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/68346/elife-68346-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** Initial velocity vs. substrate (dihydrofolate) concentration for the purified DL121 chimeric protein, allosterically inactivated DL121-C450S and eight point mutations to the DHFR domain of DL121. Lit (blue) and dark (gray) conditions are shown with error bars representing standard deviation across three replicates. The kcat, KM, catalytic efficiency and associated error are reported in Supplementary file 1a.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/68346/elife-68346-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** The absorbance of purified DL121 chimeric protein, allosterically inactivated DL121-C450S and eight point mutations to the DHFR domain of DL121. Lit state absorbance spectra (red line) were measured after illumination for at least 2 min by full spectrum 125 watt 6400K fluorescent lamp (Hydrofarm Inc). Dark conditions are taken under the same conditions but using opaque tubes when the sample was placed under the lamp. With the exception of the DL121-C450S mutant, all show a characteristic spectral shift upon light stimulation consistent with an active LOV2 domain. Formation of a covalent FMN-thiol adduct in the LOV2 domain upon light exposure causes the 447 nm peak in the dark state to shift to 390 nm in the light.

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/68346/elife-68346-fig4-figsupp4-v2.jpg)

**Figure 4—figure supplement 4.:** The relaxation of the chromophore at 447 nm was observed for 5 min following illumination for at least 2 min by full spectrum 125 watt 6400K fluorescent lamp (Hydrofarm Inc). With the exception of the allosterically inactivated DL121-C450S all of the assayed LOV2 domains had exponential and reversible relaxation to the dark state near that of the unmutated DL121 (kFMN = 0.017 s−1), indicating an active light response in the protein.

![Figure 4—figure supplement 5.](https://cdn.elifesciences.org/articles/68346/elife-68346-fig4-figsupp5-v2.jpg)

**Figure 4—figure supplement 5.:** (A) The KM values (B) enzyme velocity and (C) kcat values are shown for both lit (blue bar) and dark (gray bar) conditions, error bars represent standard error across three replicates. Above each pair of bars the lit:dark ratio of the relevant catalytic parameter is shown. The Michaelis-Menten kinetics values are reported in Supplementary file 1a.

![Figure 4—figure supplement 6.](https://cdn.elifesciences.org/articles/68346/elife-68346-fig4-figsupp6-v2.jpg)

**Figure 4—figure supplement 6.:** The relationship between the relative growth rate difference (in vivo) and the ratio of (A) catalytic turnover (kcat) (B) catalytic efficiency (kcat/KM) or (C) the Michaelis constant (KM). As we expect a log-linear relationship, we compare the ratio of catalytic constants to the exponent of the relative growth rate difference. The green dashed line is the linear regression with the coefficient of correlation (R2) shown. The low coefficient of correlation in comparisons (B-C) indicates that there is little relationship between the allosteric growth rate difference and both catalytic efficiency and the Michaelis constant ratios. The error bars represent standard error.

To further examine the ability of the growth-based sequencing assay to quantitatively resolve mutation-associated changes in allosteric regulation, we selected 10 mutations spanning a range of allosteric and growth rate effects for in vitro characterization (Figure 4B red dots, Figure 4—figure supplements 2–4). As a control, we included the light insensitive variant DL121-C450S: the C450S mutation of LOV2 abrogates light-based signaling by blocking formation of a light-induced covalent bond between position 450 and the FMN chromophore (Christie et al., 2002). We expressed and purified the selected DL121 mutants to near homogeneity; S148C and E154R did not yield sufficient quantities of active protein for in vitro studies. We find it noteworthy that E154R—one of the strongest allostery-enhancing mutations in vivo—was unstable in multiple purification strategies. For the remaining eight mutations we measured the kcat and Km of DHFR under lit and dark conditions (Figure 4—figure supplement 2). To confirm function of the fused LOV2 domain, we also measured relaxation of the FMN chromophore following light stimulation and collected absorbance spectra before and after the application of light (Figure 4—figure supplements 3–4). As expected, all the characterized DL121 mutations (with the exception of DL121-C450S) retained LOV2 domains with light-responsive absorbance spectra and chromophore relaxation constants similar to the unmutated DL121 construct. Evaluating the light dependence of DHFR activity, the change in Km value between lit and dark conditions was neither significant for any point mutation nor correlated to allosteric effect size (R2 = 0.003) (Supplementary file 1a, Figure 4—figure supplements 5–6). The Km values for all characterized mutants (0.15–1.9 µM) were similar to that of unmutated DL121 (~1 µM). Instead, we observed that light predominantly modulated catalytic turnover (kcat).The ratio of kcat in the light relative to the dark ranged from 1.1 (for the non-allosteric DL121-C450S construct) to 2.0 (for the most allosteric point mutation, H124Q) (Supplementary file 1a, Figure 4—figure supplements 5–6). For reference, the starting DL121 construct has a lit:dark kcat ratio of 1.3. So why might the characterized allosteric mutations predominantly effect kcat? One plausible explanation is that the conditions of our in vivo experiments fall within a pseudo-zero-order kinetics regime ([DHF]>>Km). In this scenario, light-associated changes in Km would have little impact on enzyme velocity (and accordingly growth rate) and go undetected in our assay. Consistent with this, the in vivo concentration of DHF for wildtype E. coli (25 µM) is well above the Km for all the characterized DL121 mutations. Alternatively, it could be that the biophysical mechanism of the DL121 fusion somehow makes it more energetically feasible for light to modulate kcat than Km. In any case, the 1.3- to 2-fold changes in kcat translate to similar fold changes in enzyme velocity. A comparison of the in vitro allosteric effect on velocity to the in vivo growth rate effect yields a near-linear relationship with a correlation coefficient of 0.83 (Figure 4D). Taken together, these data show that our growth-based assay is quantitatively reporting on changes in allostery, and that the allosteric mutations identified here modulate DHFR activity through changes in catalytic turnover number.

### The structural pattern of allostery tuning mutations

Next, we examined the distribution of allostery-tuning mutations on the WT DHFR tertiary structure. The 13 allostery disrupting mutations localized to six DHFR positions concentrated near the LOV2 insertion site (Figure 5A). More specifically, 90% of the allostery disrupting mutations occurred within 10 Å of the DHFR 121 cα atom (Figure 5B). These mutations were modestly enriched in the protein sector (Supplementary file 1d). Overall, the observed spatial distribution suggests these mutations may disrupt allostery by altering local structural contacts needed to ensure communication between DHFR and LOV2.

![Figure 5.](https://cdn.elifesciences.org/articles/68346/elife-68346-fig5-v2.jpg)

**Figure 5.:** (A) Sites of allostery disrupting mutations (orange spheres). DHFR backbone is in gray cartoon, folate substrate in yellow sticks, and NADP co-factor in green sticks. (B) Fraction of mutations that enhance (blue), disrupt (orange), or do not significantly influence allostery (gray) as a function of distance to the LOV2 insertion site at DHFR position 121. Solid and dashed lines indicate mutations at either the p=0.016 and p=0.05 significance cutoffs for allostery, respectively. (C) Sites of allostery enhancing mutations (light blue spheres). (D) Contingency table summarizing the overlap between allostery enhancing mutations and mutations on the DHFR solvent accessible surface (considered as >25% relative solvent accessibility in the 1R × 2 PDB). (E) Sites of allostery enhancing (light blue spheres) and disrupting mutations (orange spheres) in the context of the sector (dark blue surface). (F) Contingency table summarizing the relationship between allostery enhancing mutations and sector mutations (sector defined at a p-value cutoff of 0.010). No allostery enhancing mutations occur within the sector.

In contrast to this localized pattern, the 56 allostery enhancing mutations were observed at 25 positions distributed across the DHFR structure (Figure 5C) and enriched on the protein surface (Figure 5D, Supplementary file 1e). These enhancing mutations were never found in the protein sector and were thus statistically significantly depleted from the protein sector (Figure 5E,F). This relationship – wherein allostery disrupting mutations were modestly enriched and allostery enhancing mutations were strongly depleted from the sector – also holds when defining the set of allosteric mutations at a relaxed cutoff of p=0.05 (Supplementary file 1d). Given the prior finding that sector connected surface sites were hotspots for introducing allostery in DHFR (Reynolds et al., 2011), we also examined the association between allostery-influencing mutations and two other groups of DHFR positions: (1) surface sites that are either within or contacting the sector and (2) surface sites that are only contacting the sector (but not within-sector). As for the analysis of sector positions only, we observed a statistically significant depletion of allostery enhancing mutations and enrichment of allostery disrupting mutations when considering the set of surface sites within or contacting the sector. This finding holds true over a range of significance thresholds for defining sector and allosteric mutations (Supplementary file 1f). When considering the set of positions that contact (but are not within) the sector, we did not observe a statistically significant association at nearly all cutoffs (Supplementary file 1g). Indeed, a number of allostery enhancing mutations do not contact the sector at all and occur in surface exposed loops (e.g. from residues 84 to 89, and from 116 to 119). So, counter to our expectations, the optimization of allostery did not occur at sector connected sites or even proximal to the LOV2 insertion site. Instead, structurally distributed and weakly conserved surface sites provided a basis for tuning and enhancing allosteric regulation regardless of sector connectivity.

Taken together, our data show that many distributed surface sites can make modest contributions to allosteric regulation. Can these mutants be combined to further improve allosteric dynamic range? To test this, we created two mutant constructs by combining the most potent allostery enhancing mutations as characterized in vitro: the double mutant DL121-M16A,H124Q, and the triple mutant DL121-M16A,D87A,H124Q (Figure 6A). For both constructs, we measured steady-state catalytic parameters (Supplementary file 1a) and verified LOV2 function through absorbance spectra and chromophore relaxation kinetics experiments (Figure 6—figure supplement 1). Interestingly, all three mutations exhibited near-log-additive improvements in allostery (Figure 6B). The DL121-M16A,H124Q fusion exhibits a 2.74 fold increase in velocity upon light activation while the triple mutant shows a 3.87-fold increase in velocity. For both mutant combinations, the improvement in allostery is realized by reducing the dark state (constitutive) activity (Figure 6—figure supplement 1, Supplementary file 1a). The serial addition of allostery enhancing mutations also reduced the overall catalytic activity of DHFR, suggesting that further improvement could be obtained by combining these mutations with a non-allosteric but activity-enhancing mutation. Overall, these data suggest that a naïve sector connected fusion can be gradually evolved toward increased allosteric dynamic range through the stepwise accumulation of single mutations at structurally distributed surface sites (Figure 6C).

![Figure 6.](https://cdn.elifesciences.org/articles/68346/elife-68346-fig6-v2.jpg)

**Figure 6.:** (A) Location of M16, D87, and H124 (blue spheres). The LOV2 insertion site, G121, is shown in red spheres. The DHFR backbone is in gray cartoon, the folate substrate in yellow sticks, and the NADP co-factor in green sticks. (B) The in vitro allosteric effect of the single, double and triple mutants. Included are the log-additive expectations (Expected) for the double and triple mutants given only the single mutation effects, and the experimentally measured effects (Observed). The ratio between velocity in the light and dark reflects the mean of triplicate measurements; error bars indicate SEM. There is not a statistically significant difference between the expected and observed allosteric effects (p=0.07 for M16A,H124Q, p=0.48 for M16A,D87A,H124Q; as computed by unpaired t-test). (C) Schematic whereby a novel domain insertion is iteratively optimized by surface residue variation.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/68346/elife-68346-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (A-B) Steady state kinetics measurements in the light and dark. Initial velocity vs. substrate (dihydrofolate) concentration is plotted, Lit (blue) and dark (gray) conditions are shown with error bars representing standard deviation across three replicates. For both the double and triple mutant, the lit states were better fit by a substrate inhibition model than a standard Michaelis-Menten model (p<0.05). The kcat, KM, catalytic efficiency and associated error are reported in Supplementary file 1a. (C-D) Relaxation rate of the LOV2 chromophore. The relaxation of the chromophore at 447 nm was observed for 5 min following illumination for at least 2 min by full spectrum 125 watt 6400K fluorescent lamp (Hydrofarm Inc). (E-F) Spectroscopic characterization of LOV2 activation. Lit state absorbance spectra (red line) were measured after illumination for at least 2 min by full spectrum 125 watt 6400K fluorescent lamp (Hydrofarm Inc). Dark conditions are taken under the same conditions but using opaque tubes when the sample was placed under the lamp. Both mutants show a characteristic spectral shift upon light stimulation consistent with an active LOV2 domain.

## Discussion

We used deep mutational scanning to study the frequency and structural pattern of allostery tuning mutations in a synthetic allosteric system, with the goal of understanding how regulation between domains can be optimized. Overall, allostery-influencing mutations were rare – just under 5% of viable mutations had statistically distinguishable effects on the lit and dark states of the DL121 fusion. We found that mutations at conserved and co-evolving (sector) positions were often deleterious to DHFR function and infrequently influenced allosteric regulation. In a few cases, sector mutations served to disrupt allostery; nearly all allostery disrupting mutations were localized to the LOV2 insertion site on DHFR. Counter to our expectations, allostery enhancing mutations were distributed across the DHFR structure, depleted from the sector, and enriched on the protein surface. When considered individually, the allostery-enhancing mutations had modest effects (up to twofold) on regulation, but (at least in some cases) they can be combined to yield near-additive improvements in dynamic range. A triple mutant (DL121-M16A,D87A,H124Q) rationally designed using our point mutant data produces a 3.87-fold increase in velocity upon light stimulation, up from the 1.3-fold allosteric effect of our starting construct.

These results should be considered in the context of our experiment: the DL121 fusion begins with sharply reduced DHFR activity, and our experiment intentionally used relatively stringent DHFR selection conditions to better resolve small differences in kinetic parameters. Thus, it is unsurprising that a large fraction of DHFR mutations in our library were deleterious, with an appreciable fraction near-inactive. This result echoes prior studies showing that the fraction of deleterious mutations (and mutational robustness) is strongly modulated by a variety of factors, including purifying selection strength and expression level (Stiffler et al., 2015; Jiang et al., 2013; Lundin et al., 2018). Given the finding that stabilizing mutations can often improve protein evolvability (Lundin et al., 2018; Bloom et al., 2006; Zheng et al., 2020), it would be interesting to examine how the distribution of mutational effects on both DL121 function and allostery would change in the background of a stability (and/or activity) enhancing mutation to DL121. While we observed that the number of allosteric mutations is few and the effect sizes are generally small in our model system, a previous study of allostery tuning mutations in pyruvate kinase indicated that up to 30% of mutations can tune allostery, with the maximum observed effect size approaching 22-fold (Tang and Fenton, 2017). Nevertheless, our data serve to illuminate the pattern of mutational effects on a newly established (and unoptimized) domain fusion – the presumptive first step toward regulation in a number of both natural and synthetic systems.

Interestingly, we observe a seeming disparity between the sites where we were able to introduce new allosteric regulation by domain fusion (in our earlier work), and the sites where allosteric tuning takes place (in this work). Previously, Reynolds et al. found that sector connected surface sites served as hotspots for the introduction of new light-based regulation in DHFR (Reynolds et al., 2011). Indeed, allosteric regulation was never obtained when the LOV2 domain was inserted at a non-sector connected site. In contrast, in this work, we observed that allostery enhancing mutations were depleted both within the sector and at sector connected sites. For example, we observed a number of allostery enhancing mutations at positions 83–89 of the DHFR αD-βE loop, while LOV2 insertions in this region location did not initiate allostery as quantified either in vitro or in vivo (Lee et al., 2008; Reynolds et al., 2011). This suggests different structural requirements for establishing and tuning allostery in this system (and possibly others): here allostery seems to be more easily introduced at evolutionarily conserved and co-evolving sites, but once established, can be optimized through less conserved sector-peripheral residues.

Although our work focuses on a synthetic allosteric fusion, our results are broadly consistent with an emerging body of work characterizing allostery-influencing mutations in natural proteins. Together, these data point to a model in which mutations at evolutionarily conserved positions exert large (and often disruptive) effects on function while allostery is tuned at less conserved surface sites. For example, Leander et al. recently used deep mutational scanning to map the pattern of compensatory mutations that rescued allosteric function for non-allosteric tetracycline repressor (TetR) variants (Leander et al., 2020). In that study a ‘disrupt-and-restore’ strategy was used: an already-allosteric system was inactivated and deep mutational scanning was then used to identify compensatory mutations. While there are significant differences between rescuing a deficient variant and the optimization of a novel allosteric construct, they likewise found that the mutations at highly conserved sites were often disruptive to stability and function, while allostery-rescuing mutations occurred at weakly conserved and structurally distributed sites (Leander et al., 2020). Similarly, mutations at ‘rheostat’ sites – weakly conserved positions distal to the site of regulation – were found to modulate allosteric control in human liver pyruvate kinase and the lactose repressor protein (lacI) (Campitelli et al., 2020; Wu et al., 2019). Intriguingly, the association of allostery enhancing mutations with the protein surface hints at a possible role for solvent – and more specifically the protein hydration layer – in tuning regulation.

The finding that the allostery initiated upon naïve fusion of the DHFR and LOV2 domains can be further enhanced by single mutations implies a path to improved allosteric dynamic range by stepwise mutagenesis and selection. Three of the most allostery enhancing mutations could be combined to yield a near-additive improvement in regulatory dynamic range. This has interesting implications for both evolved and engineered allosteric systems. In evolved systems, standing mutational variation is more likely at weakly conserved surface sites (particularly under less stringent selection conditions), and this could provide a means for generating variation in allosteric regulation upon a domain fusion event. Moreover, while engineering studies sometimes use mutations near the domain insertion site to optimize regulation, our results suggest that diffuse surface site mutations could present an effective alternative. Whether by engineering or evolution, it seems that mutations at weakly conserved and structurally distributed residues can provide a path to the optimization of regulation.

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
      <td>Gene (Escherichia coli)</td>
      <td>DHFR-LOV2 121</td>
      <td>Reynolds et al. Cell 2011 [20]</td>
      <td>Fusion of Escherichia coli DHFR and Avena sativa LOV2</td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>BL21(DE3)</td>
      <td>New England Biolabs</td>
      <td>NEB #: C2527H</td>
      <td>Competent cells</td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>ER2566 ΔfolA ΔthyA</td>
      <td>Dr. Steven Benkovic, described in [20, 26]</td>
      <td>Competent cells</td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>XL1-Blue</td>
      <td>Agilent Technologies</td>
      <td>Cat. #: 200249</td>
      <td>Competent cells</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pACYC-Duet_DL121_WTTS(plasmid)</td>
      <td>Reynolds et al. Cell 2011 [20]</td>
      <td>Addgene ID 171954</td>
      <td>Contains chimeric DL121 with TYMS (selection vector)</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pHIS8-3_DL121(plasmid)</td>
      <td>Reynolds et al. Cell 2011 [20]</td>
      <td>Addgene ID 171953</td>
      <td>Contains chimeric DL121 (expression vector)</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos1_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSATCAGTCTGATTGCGGCG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos2_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSAGTCTGATTGCGGCGTTAG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos3_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSCTGATTGCGGCGTTAGCG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos4_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSATTGCGGCGTTAGCGGTA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos5_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGCGGCGTTAGCGGTAGAT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos6_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGCGTTAGCGGTAGATCGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos7_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSTTAGCGGTAGATCGCGTTATC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos8_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGCGGTAGATCGCGTTATCG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos9_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGTAGATCGCGTTATCGGCATG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos10_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGATCGCGTTATCGGCATGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos11_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSCGCGTTATCGGCATGGAAAA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos12_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGTTATCGGCATGGAAAACGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos13_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSATCGGCATGGAAAACGCC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos14_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGGCATGGAAAACGCCATG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos15_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSATGGAAAACGCCATGCCG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos16_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGAAAACGCCATGCCGTGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos17_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSAACGCCATGCCGTGGAAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos18_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGCCATGCCGTGGAACCTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos19_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSATGCCGTGGAACCTGCCT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos20_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSCCGTGGAACCTGCCTGCC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos21_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSTGGAACCTGCCTGCCGAT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos22_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSAACCTGCCTGCCGATCTC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos23_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSCTGCCTGCCGATCTCGCC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos24_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSCCTGCCGATCTCGCCTGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos25_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGCCGATCTCGCCTGGTTT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos26_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGATCTCGCCTGGTTTAAACGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos27_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSCTCGCCTGGTTTAAACGCAACA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos28_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGCCTGGTTTAAACGCAACAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos29_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSTGGTTTAAACGCAACACCTTAAATAAAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos30_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSTTTAAACGCAACACCTTAAATAAACCCG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos31_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSAAACGCAACACCTTAAATAAACCCGTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos32_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSCGCAACACCTTAAATAAACCCGT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos33_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSAACACCTTAAATAAACCCGTGATTATGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos34_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSACCTTAAATAAACCCGTGATTATGGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos35_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSTTAAATAAACCCGTGATTATGGGCC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos36_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSAATAAACCCGTGATTATGGGCC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos37_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSAAACCCGTGATTATGGGCC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos38_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSCCCGTGATTATGGGCCGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos39_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGTGATTATGGGCCGCCATAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos40_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSATTATGGGCCGCCATACCT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos41_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSATGGGCCGCCATACCTGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos42_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGGCCGCCATACCTGGGAA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos43_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSCGCCATACCTGGGAATCG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos44_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSCATACCTGGGAATCGATCGGT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos45_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSACCTGGGAATCGATCGGT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos46_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSTGGGAATCGATCGGTCGT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos47_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGAATCGATCGGTCGTCCG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos48_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSTCGATCGGTCGTCCGTTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos49_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSATCGGTCGTCCGTTGCCA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos50_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGGTCGTCCGTTGCCAGGA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos51_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSCGTCCGTTGCCAGGACGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos52_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSCCGTTGCCAGGACGCAAA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos53_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSTTGCCAGGACGCAAAAATATTATCC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos54_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSCCAGGACGCAAAAATATTATCCTGAG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos55_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGGACGCAAAAATATTATCCTGAGCTC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos56_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSCGCAAAAATATTATCCTGAGCTCACAA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos57_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSAAAAATATTATCCTGAGCTCACAACCGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos58_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSAATATTATCCTGAGCTCACAACCGGGTA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos59_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSATTATCCTGAGCTCACAACCG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos60_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSATCCTGAGCTCACAACCG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos61_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSCTGAGCTCACAACCGGGT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos62_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSAGCTCACAACCGGGTACG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos63_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSTCACAACCGGGTACGGAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos64_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSCAACCGGGTACGGACGAT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos65_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSCCGGGTACGGACGATCGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos66_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGGTACGGACGATCGCGTA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos67_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSACGGACGATCGCGTAACG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos68_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGACGATCGCGTAACGTGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos69_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGATCGCGTAACGTGGGTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos70_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSCGCGTAACGTGGGTGAAG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos71_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGTAACGTGGGTGAAGTCGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos72_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSACGTGGGTGAAGTCGGTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos73_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSTGGGTGAAGTCGGTGGAT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos74_fwd2</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGTGAAGTCGGTGGATGAAG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos75_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSAAGTCGGTGGATGAAGCAATTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos76_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSTCGGTGGATGAAGCAATTGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos77_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGTGGATGAAGCAATTGCGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos78_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGATGAAGCAATTGCGGCG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos79_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGAAGCAATTGCGGCGTGT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos80_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGCAATTGCGGCGTGTGGT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos81_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSATTGCGGCGTGTGGTGAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos82_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGCGGCGTGTGGTGACGTAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos83_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGCGTGTGGTGACGTACCA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos84_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSTGTGGTGACGTACCAGAAATCAT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos85_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGGTGACGTACCAGAAATCATGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos86_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGACGTACCAGAAATCATGGTGATTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos87_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGTACCAGAAATCATGGTGATTGGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos88_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSCCAGAAATCATGGTGATTGGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos89_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGAAATCATGGTGATTGGCGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos90_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSATCATGGTGATTGGCGGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos91_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSATGGTGATTGGCGGCGGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos92_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGTGATTGGCGGCGGCCGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos93_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSATTGGCGGCGGCCGCGTT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos94_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGGCGGCGGCCGCGTTTAT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos95_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGGCGGCCGCGTTTATGAA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos96_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGGCCGCGTTTATGAACAGTT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos97_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSCGCGTTTATGAACAGTTCTTGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos98_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGTTTATGAACAGTTCTTGCCAAAAGCGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos99_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSTATGAACAGTTCTTGCCAAAAGCGCAAA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos100_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGAACAGTTCTTGCCAAAAGCGCAAAAGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos101_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSCAGTTCTTGCCAAAAGCGCAAAAGCTTT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos102_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSTTCTTGCCAAAAGCGCAAAAG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos103_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSTTGCCAAAAGCGCAAAAGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos104_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSCCAAAAGCGCAAAAGCTTTATCTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos105_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSAAAGCGCAAAAGCTTTATCTGACG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos106_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGCGCAAAAGCTTTATCTGACG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos107_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSCAAAAGCTTTATCTGACGCATATCGAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos108_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSAAGCTTTATCTGACGCATATCGAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos109_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSCTTTATCTGACGCATATCGACGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos110_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSTATCTGACGCATATCGACGCA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos111_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSCTGACGCATATCGACGCAG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos112_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSACGCATATCGACGCAGAAGT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos113_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSCATATCGACGCAGAAGTGGAAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos114_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSATCGACGCAGAAGTGGAACT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos115_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGACGCAGAAGTGGAACTGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos116_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGCAGAAGTGGAACTGGCC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos117_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGAAGTGGAACTGGCCACC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos118_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGTGGAACTGGCCACCACT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos119_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGAACTGGCCACCACTCTAGA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos120_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSCTGGCCACCACTCTAGAG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos121_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGACACCCATTTCCCGGATTAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos122_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSACCCATTTCCCGGATTACGA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos123_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSCATTTCCCGGATTACGAGCC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos124_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSTTCCCGGATTACGAGCCG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos125_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSCCGGATTACGAGCCGGAT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos126_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGATTACGAGCCGGATGACTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos127_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSTACGAGCCGGATGACTGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos128_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGAGCCGGATGACTGGGAA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos129_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSCCGGATGACTGGGAATCG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos130_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGATGACTGGGAATCGGTATTCAG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos131_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGACTGGGAATCGGTATTCAGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos132_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSTGGGAATCGGTATTCAGCGAATT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos133_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGAATCGGTATTCAGCGAATTCCAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos134_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSTCGGTATTCAGCGAATTCCAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos135_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGTATTCAGCGAATTCCACGATG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos136_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSTTCAGCGAATTCCACGATGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos137_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSAGCGAATTCCACGATGCTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos138_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGAATTCCACGATGCTGATGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos139_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSTTCCACGATGCTGATGCG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos140_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSCACGATGCTGATGCGCAG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos141_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGATGCTGATGCGCAGAACT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos142_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGCTGATGCGCAGAACTCTC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos143_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGATGCGCAGAACTCTCACAG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos144_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGCGCAGAACTCTCACAGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos145_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSCAGAACTCTCACAGCTATTGCTTTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos146_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSAACTCTCACAGCTATTGCTTTGAGATT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos147_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSTCTCACAGCTATTGCTTTGAGATTCT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos148_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSCACAGCTATTGCTTTGAGATTCTGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos149_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSAGCTATTGCTTTGAGATTCTGGAG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos150_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSTATTGCTTTGAGATTCTGGAGCG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos151_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSTGCTTTGAGATTCTGGAGCG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos152_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSTTTGAGATTCTGGAGCGGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos153_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGAGATTCTGGAGCGGCGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos154_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSATTCTGGAGCGGCGGTAA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos155_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSCTGGAGCGGCGGTAACAT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos156_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSGAGCGGCGGTAACATCCG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos157_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSCGGCGGTAACATCCGTCG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos158_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSCGGTAACATCCGTCGACAAG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos159_fwd</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>NNSTAACATCCGTCGACAAGCTTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos1_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CGGATCCTGGCTGTGGTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos2_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CATCGGATCCTGGCTGTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos3_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GATCATCGGATCCTGGCTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos4_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>ACTGATCATCGGATCCTGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos5_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CAGACTGATCATCGGATCCTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos6_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>AATCAGACTGATCATCGGATCCTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos7_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CGCAATCAGACTGATCATCGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos8_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CGCCGCAATCAGACTGATC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos9_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>TAACGCCGCAATCAGACTGA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos10_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CGCTAACGCCGCAATCAG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos11_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>TACCGCTAACGCCGCAAT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos12_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>ATCTACCGCTAACGCCGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos13_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GCGATCTACCGCTAACGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos14_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>AACGCGATCTACCGCTAAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos15_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GATAACGCGATCTACCGCTAAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos16_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GCCGATAACGCGATCTACC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos17_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CATGCCGATAACGCGATCTAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos18_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>TTCCATGCCGATAACGCG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos19_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GTTTTCCATGCCGATAACGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos20_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GGCGTTTTCCATGCCGATAACG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos21_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CATGGCGTTTTCCATGCC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos22_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CGGCATGGCGTTTTCCAT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos23_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CCACGGCATGGCGTTTTC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos24_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GTTCCACGGCATGGCGTT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos25_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CAGGTTCCACGGCATGGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos26_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>AGGCAGGTTCCACGGCAT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos27_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GGCAGGCAGGTTCCACGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos28_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>ATCGGCAGGCAGGTTCCA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos29_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GAGATCGGCAGGCAGGTT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos30_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GGCGAGATCGGCAGGCAG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos31_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CCAGGCGAGATCGGCAGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos32_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>AAACCAGGCGAGATCGGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos33_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>TTTAAACCAGGCGAGATCGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos34_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GCGTTTAAACCAGGCGAGAT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos35_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GTTGCGTTTAAACCAGGCGA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos36_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GGTGTTGCGTTTAAACCAGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos37_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>TAAGGTGTTGCGTTTAAACCAGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos38_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>ATTTAAGGTGTTGCGTTTAAACCAGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos39_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>TTTATTTAAGGTGTTGCGTTTAAACCAG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos40_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GGGTTTATTTAAGGTGTTGCGTTTAAAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos41_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CACGGGTTTATTTAAGGTGTTGCGT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos42_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>AATCACGGGTTTATTTAAGGTGTTGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos43_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CATAATCACGGGTTTATTTAAGGTGTTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos44_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GCCCATAATCACGGGTTTATTTAAGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos45_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GCGGCCCATAATCACGGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos46_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>ATGGCGGCCCATAATCAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos47_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GGTATGGCGGCCCATAATC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos48_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CCAGGTATGGCGGCCCATA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos49_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>TTCCCAGGTATGGCGGCC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos50_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CGATTCCCAGGTATGGCG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos51_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GATCGATTCCCAGGTATGGCG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos52_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>ACCGATCGATTCCCAGGTATG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos53_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>ACGACCGATCGATTCCCA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos54_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CGGACGACCGATCGATTC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos55_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CAACGGACGACCGATCGA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos56_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>TGGCAACGGACGACCGAT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos57_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>TCCTGGCAACGGACGACC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos58_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GCGTCCTGGCAACGGACG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos59_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>TTTGCGTCCTGGCAACGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos60_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>ATTTTTGCGTCCTGGCAAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos61_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>AATATTTTTGCGTCCTGGCAAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos62_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GATAATATTTTTGCGTCCTGGCAAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos63_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CAGGATAATATTTTTGCGTCCTGGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos64_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GCTCAGGATAATATTTTTGCGTCCTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos65_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>TGAGCTCAGGATAATATTTTTGCGTCCT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos66_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>TTGTGAGCTCAGGATAATATTTTTGCG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos67_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CGGTTGTGAGCTCAGGATAATATTTTTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos68_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>ACCCGGTTGTGAGCTCAG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos69_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CGTACCCGGTTGTGAGCT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos70_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GTCCGTACCCGGTTGTGA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos71_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>ATCGTCCGTACCCGGTTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos72_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GCGATCGTCCGTACCCGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos73_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>TACGCGATCGTCCGTACC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos74_rev2</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CGTTACGCGATCGTCC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos75_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CCACGTTACGCGATCGTC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos76_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CACCCACGTTACGCGATC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos77_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CTTCACCCACGTTACGCG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos78_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CGACTTCACCCACGTTACG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos79_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CACCGACTTCACCCACGT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos80_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>ATCCACCGACTTCACCCA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos81_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>TTCATCCACCGACTTCACC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos82_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>TGCTTCATCCACCGACTTCACC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos83_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>AATTGCTTCATCCACCGACTTC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos84_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CGCAATTGCTTCATCCACC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos85_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CGCCGCAATTGCTTCATC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos86_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>ACACGCCGCAATTGCTTC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos87_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>ACCACACGCCGCAATTGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos88_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GTCACCACACGCCGCAAT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos89_rev2</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>TACGTCACCACACGCC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos90_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>TGGTACGTCACCACACGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos91_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>TTCTGGTACGTCACCACACGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos92_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GATTTCTGGTACGTCACCACACGCC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos93_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CATGATTTCTGGTACGTCACCACACGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos94_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CACCATGATTTCTGGTACGTCACCACA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos95_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>AATCACCATGATTTCTGGTACGTCA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos96_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GCCAATCACCATGATTTCTGGTAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos97_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GCCGCCAATCACCATGATTT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos98_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GCCGCCGCCAATCACCATG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos99_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GCGGCCGCCGCCAATCAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos100_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>AACGCGGCCGCCGCCAAT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos101_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>ATAAACGCGGCCGCCGCC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos102_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>TTCATAAACGCGGCCGCC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos103_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CTGTTCATAAACGCGGCC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos104_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GAACTGTTCATAAACGCGGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos105_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CAAGAACTGTTCATAAACGCGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos106_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>TGGCAAGAACTGTTCATAAACGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos107_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>TTTTGGCAAGAACTGTTCATAAACG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos108_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CGCTTTTGGCAAGAACTGTTCATAAA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos109_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>TTGCGCTTTTGGCAAGAACT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos110_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CTTTTGCGCTTTTGGCAAGAAC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos111_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>AAGCTTTTGCGCTTTTGGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos112_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>ATAAAGCTTTTGCGCTTTTGGCA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos113_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CAGATAAAGCTTTTGCGCTTTTGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos114_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CGTCAGATAAAGCTTTTGCGCTTT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos115_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>ATGCGTCAGATAAAGCTTTTGCG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos116_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GATATGCGTCAGATAAAGCTTTTGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos117_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GTCGATATGCGTCAGATAAAGCTTTTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos118_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>TGCGTCGATATGCGTCAGATAAA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos119_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>TTCTGCGTCGATATGCGTCA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos120_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CACTTCTGCGTCGATATGCG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos121_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GTCGATGTTCTCGGCGGT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos122_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GCCGTCGATGTTCTCGGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos123_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GTCGCCGTCGATGTTCTC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos124_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GGTGTCGCCGTCGATGTT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos125_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>ATGGGTGTCGCCGTCGAT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos126_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GAAATGGGTGTCGCCGTC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos127_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CGGGAAATGGGTGTCGCC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos128_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>ATCCGGGAAATGGGTGTC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos129_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GTAATCCGGGAAATGGGTGTC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos130_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CTCGTAATCCGGGAAATGGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos131_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CGGCTCGTAATCCGGGAA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos132_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>ATCCGGCTCGTAATCCGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos133_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GTCATCCGGCTCGTAATCC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos134_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CCAGTCATCCGGCTCGTA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos135_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>TTCCCAGTCATCCGGCTC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos136_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CGATTCCCAGTCATCCGG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos137_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>TACCGATTCCCAGTCATCCG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos138_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GAATACCGATTCCCAGTCATCC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos139_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GCTGAATACCGATTCCCAGTC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos140_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>TTCGCTGAATACCGATTCCCA</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos141_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GAATTCGCTGAATACCGATTCCC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos142_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GTGGAATTCGCTGAATACCGATTC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos143_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>ATCGTGGAATTCGCTGAATACC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos144_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>AGCATCGTGGAATTCGCTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos145_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>ATCAGCATCGTGGAATTCGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos146_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CGCATCAGCATCGTGGAATT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos147_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CTGCGCATCAGCATCGTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos148_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GTTCTGCGCATCAGCATC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos149_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>AGAGTTCTGCGCATCAGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos150_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GTGAGAGTTCTGCGCATCAG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos151_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GCTGTGAGAGTTCTGCGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos152_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>ATAGCTGTGAGAGTTCTGCG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos153_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>GCAATAGCTGTGAGAGTTCTGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos154_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>AAAGCAATAGCTGTGAGAGTTCTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos155_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CTCAAAGCAATAGCTGTGAGAGTTC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos156_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>AATCTCAAAGCAATAGCTGTGAGAGTT</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos157_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CAGAATCTCAAAGCAATAGCTGTGAG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos158_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CTCCAGAATCTCAAAGCAATAGCTG</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_pos159_rev</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>CCGCTCCAGAATCTCAAAGC</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_E154R_F</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>ctctcacagctattgctttaggattctggagcggcggtaa</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_E154R_R</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>ttaccgccgctccagaatcctaaagcaatagctgtgagag</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_D122W_F</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>gtaatccgggaaatgggtccagccgtcgatgttctcggc</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_D122W_R</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>gccgagaacatcgacggctggacccatttcccggattac</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_D127W_F</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>cagtcatccggctcgtaccacgggaaatgggtgtcgc</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_D127W_R</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>gcgacacccatttcccgtggtacgagccggatgactg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_M16A_F</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>cggcatggcgttttccgcgccgataacgcgatct</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_M16A_R</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>agatcgcgttatcggcgcggaaaacgccatgccg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_A9N_F</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>catgccgataacgcgatctacatttaacgccgcaatcagactgatc</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_A9N_R</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>gatcagtctgattgcggcgttaaatgtagatcgcgttatcggcatg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_R52K_F</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>tcctggcaacggcttaccgatcgattcccaggtatggc</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_R52K_R</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>gccatacctgggaatcgatcggtaagccgttgccagga</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_E120P_F</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>ctagagtggtggccagtggcacttctgcgtcgatat</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_E120P_R</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>atatcgacgcagaagtgccactggccaccactctag</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_S148C_F</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>aagcaatagctgtgacagttctgcgcatcagcatc</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_S148C_R</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>gatgctgatgcgcagaactgtcacagctattgctt</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_H124Q_F</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>tcgtaatccgggaactgggtgtcgccgtc</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_H12RQ_R</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>gacggcgacacccagttcccggattacga</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_D27N_F</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>aaaccaggcgagattggcaggcaggttcc</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_D27N_R</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>ggaacctgcctgccaatctcgcctggttt</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_D87A_F</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>catgatttctggtacggcaccacacgccgcaat</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_D87A_R</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>attgcggcgtgtggtgccgtaccagaaatcatg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Thrombin_to_TEV_F</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>cttccagggtcatgggatgatgatcagtctgattgc</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Thrombin_to_TEV_R</td>
      <td>This Paper</td>
      <td>Mutagenic PCR primer</td>
      <td>tacaggttctcaccaccgtggtggtggtg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_SL1V2_F</td>
      <td>This Paper</td>
      <td>Round one Amplicon PCR primer</td>
      <td>cactctttccctacacgacgctcttccgatctnnnnatcaccatcatcaccacagc</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_SL1V2_R</td>
      <td>This Paper</td>
      <td>Round one Amplicon PCR primer</td>
      <td>tgactggagttcagacgtgtgctcttccgatctnnnnaccgatcgattcccaggta</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_SL2V2_F</td>
      <td>This Paper</td>
      <td>Round one Amplicon PCR primer</td>
      <td>cactctttccctacacgacgctcttccgatctnnnngcaacaccttaaataaacccg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_SL2V2_R</td>
      <td>This Paper</td>
      <td>Round one Amplicon PCR primer</td>
      <td>tgactggagttcagacgtgtgctcttccgatctnnnngatttctggtacgtcaccaca</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_SL3V2_F</td>
      <td>This Paper</td>
      <td>Round one Amplicon PCR primer</td>
      <td>cactctttccctacacgacgctcttccgatctnnnngtaacgtgggtgaagtcg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_SL3V2_R</td>
      <td>This Paper</td>
      <td>Round one Amplicon PCR primer</td>
      <td>tgactggagttcagacgtgtgctcttccgatctnnnnctcgatgcgctctagagtg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_SL4V2_F</td>
      <td>This Paper</td>
      <td>Round one Amplicon PCR primer</td>
      <td>cactctttccctacacgacgctcttccgatctnnnnaagaagaccgccgagaacat</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_SL4V2_R</td>
      <td>This Paper</td>
      <td>Round one Amplicon PCR primer</td>
      <td>tgactggagttcagacgtgtgctcttccgatctnnnncttaagcattatgcggccg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL121_CLV3_F</td>
      <td>This Paper</td>
      <td>Round one Amplicon PCR primer</td>
      <td>cactctttccctacacgacgctcttccgatctnnnngacacccatttcccggattacgagc</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>DL_WTTS_R3</td>
      <td>This Paper</td>
      <td>Round one Amplicon PCR primer</td>
      <td>tgactggagttcagacgtgtgctcttccgatctnnnngccgtgtacaatacgattactttctg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>D501</td>
      <td>Illumina/Reynolds et al. Cell 2011 [20]</td>
      <td>Round two Amplicon PCR primer</td>
      <td>aatgatacggcgaccaccgagatctacactatagcctacactctttccctacacgac</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>D502</td>
      <td>Illumina/Reynolds et al. Cell 2011 [20]</td>
      <td>Round two Amplicon PCR primer</td>
      <td>aatgatacggcgaccaccgagatctacacatagaggcacactctttccctacacgac</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>D503</td>
      <td>Illumina/Reynolds et al. Cell 2011 [20]</td>
      <td>Round two Amplicon PCR primer</td>
      <td>aatgatacggcgaccaccgagatctacaccctatcctacactctttccctacacgac</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>D504</td>
      <td>Illumina/Reynolds et al. Cell 2011 [20]</td>
      <td>Round two Amplicon PCR primer</td>
      <td>aatgatacggcgaccaccgagatctacacggctctgaacactctttccctacacgac</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>D505</td>
      <td>Illumina/Reynolds et al. Cell 2011 [20]</td>
      <td>Round two Amplicon PCR primer</td>
      <td>aatgatacggcgaccaccgagatctacacaggcgaagacactctttccctacacgac</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>D506</td>
      <td>Illumina/Reynolds et al. Cell 2011 [20]</td>
      <td>Round two Amplicon PCR primer</td>
      <td>aatgatacggcgaccaccgagatctacactaatcttaacactctttccctacacgac</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>D507</td>
      <td>Illumina/Reynolds et al. Cell 2011 [20]</td>
      <td>Round two Amplicon PCR primer</td>
      <td>aatgatacggcgaccaccgagatctacaccaggacgtacactctttccctacacgac</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>D508</td>
      <td>Illumina/Reynolds et al. Cell 2011 [20]</td>
      <td>Round two Amplicon PCR primer</td>
      <td>aatgatacggcgaccaccgagatctacacgtactgacacactctttccctacacgac</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>D701</td>
      <td>Illumina/Reynolds et al. Cell 2011 [20]</td>
      <td>Round two Amplicon PCR primer</td>
      <td>caagcagaagacggcatacgagatcgagtaatgtgactggagttcagacgtg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>D702</td>
      <td>Illumina/Reynolds et al. Cell 2011 [20]</td>
      <td>Round two Amplicon PCR primer</td>
      <td>caagcagaagacggcatacgagattctccggagtgactggagttcagacgtg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>D703</td>
      <td>Illumina/Reynolds et al. Cell 2011 [20]</td>
      <td>Round two Amplicon PCR primer</td>
      <td>caagcagaagacggcatacgagataatgagcggtgactggagttcagacgtg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>D704</td>
      <td>Illumina/Reynolds et al. Cell 2011 [20]</td>
      <td>Round two Amplicon PCR primer</td>
      <td>caagcagaagacggcatacgagatggaatctcgtgactggagttcagacgtg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>D705</td>
      <td>Illumina/Reynolds et al. Cell 2011 [20]</td>
      <td>Round two Amplicon PCR primer</td>
      <td>caagcagaagacggcatacgagatttctgaatgtgactggagttcagacgtg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>D706</td>
      <td>Illumina/Reynolds et al. Cell 2011 [20]</td>
      <td>Round two Amplicon PCR primer</td>
      <td>caagcagaagacggcatacgagatacgaattcgtgactggagttcagacgtg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>D707</td>
      <td>Illumina/Reynolds et al. Cell 2011 [20]</td>
      <td>Round two Amplicon PCR primer</td>
      <td>caagcagaagacggcatacgagatagcttcaggtgactggagttcagacgtg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>D708</td>
      <td>Illumina/Reynolds et al. Cell 2011 [20]</td>
      <td>Round two Amplicon PCR primer</td>
      <td>caagcagaagacggcatacgagatgcgcattagtgactggagttcagacgtg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>D709</td>
      <td>Illumina/Reynolds et al. Cell 2011 [20]</td>
      <td>Round two Amplicon PCR primer</td>
      <td>caagcagaagacggcatacgagatcatagccggtgactggagttcagacgtg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>D710</td>
      <td>Illumina/Reynolds et al. Cell 2011 [20]</td>
      <td>Round two Amplicon PCR primer</td>
      <td>caagcagaagacggcatacgagatttcgcggagtgactggagttcagacgtg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>D711</td>
      <td>Illumina/Reynolds et al. Cell 2011 [20]</td>
      <td>Round two Amplicon PCR primer</td>
      <td>caagcagaagacggcatacgagatgcgcgagagtgactggagttcagacgtg</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>D712</td>
      <td>Illumina/Reynolds et al. Cell 2011 [20]</td>
      <td>Round two Amplicon PCR primer</td>
      <td>caagcagaagacggcatacgagatctatcgctgtgactggagttcagacgtg</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>QuikChange II site-directed mutagenesis kit</td>
      <td>Agilent</td>
      <td>Cat. #: 200523</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>usearch v11.0.667</td>
      <td>Edgar Bioinformatics 2010 (PMID:20709691)</td>
      <td>Merge read pairs</td>
      <td>https://www.drive5.com/usearch/</td>
    </tr>
  </tbody>
</table>

### Experimental model and subject details

#### Escherichia coli expression and selection strains

ER2566 ΔfolA ΔthyA E. coli were used for all growth in vivo growth rate measurements; this strain was a kind gift from Dr. Steven Benkovic and is the same used in Reynolds et al., 2011 and Thompson et al., 2020 (Reynolds et al., 2011; Thompson et al., 2020). XL1-Blue E. coli (genotype: recA1 endA1 gyrA96 thi-1 hsdR17 supE44 relA1 lac [F’ proAB lacIqZΔM15 Tn10(Tetr)]) from Agilent Technologies were used for cloning, mutagenesis, and plasmid propagation. BL21(DE3) E. coli (genotype: fhuA2 [lon] ompT gal (λ DE3) [dcm] ∆hsdS. λ DE3 = λ sBamHIo ∆EcoRI-B int::(lacI::PlacUV5::T7 gene1) i21 ∆nin5) from New England Biolabs were used for protein expression.

### Method details

#### DHFR saturation mutagenesis library construction

The construction of the DHFR-LOV2 saturation mutagenesis library was done as described in Thompson et al., 2020 (Thompson et al., 2020). Four sublibraries were generated to cover the entire mutational space of E. coli DHFR: positions 1–40 (sublibrary1, SL1), positions 41–80 (sublibrary2, SL2), positions 81–120 (sublibrary3, SL3), and positions 121–159 (sublibrary4, SL4) Inverse PCR with NNS mutagenic primers (N = A/T/G/C, S = G/C) was done at every position in DHFR to produce all amino acid substitution. The vector with DHFR-LOV2 121 and TYMS in a pACYC-Duet vector was described in Reynolds et al., 2011 (Reynolds et al., 2011).

The NNS primers were phosphorylated with T4 polynucleotide kinase (NEB, cat#M0201S). 20 µL phosphorylations was prepared according to the following recipe: 16.5 µL sterile water, 2 µL T4 ligase buffer, 0.5 µL T4 PNK enzyme, and 1 µL 100 µM NNS primers. The reactions were then heated at 37°C for 1 hr and 65°C for 20 min.

PCR reactions were set up using 2x Q5 mastermix (NEB, cat#M0492), 10 ng of plasmid template, and 500 nM forward and reverse primers. PCR was performed in the following steps: (1) 98°C for 30 s, (2) 98°C for 10 s, (3) 55°C for 30 s, (4) 72°C for 2 min, (5) return to step 2 for 22 cycles, (6) 72°C for 5 min. 25 µL of PCR reaction was mixed with 1 µL of DpnI (NEB, cat#R0176) at 37°C for 4 hr. The samples were then purified by gel extraction and a DNA Clean and Concentrator −5 kit (Zymo Research, cat#D4014). PCR product solution were then phosphorylated with a second round of T4 PNK: 100 µL of gel-extracted PCR product,12 µL of 10x T4 ligase buffer, 5 µL of T4 PNK, 5 µL of sterile water and were incubated at 37°C for 1 hr with 90°C for 30 s. The reactions were ligated with 100 µL PNK phosphorylated PCR product, 15 µL T4 ligase (NEB, cat#M0202S), 30 µL T4 ligase buffer and, 155 µL sterile water. The reaction was incubated at room temperature for 24 hr.

The concentration of each reaction was quantified by gel densitometry (ImageJ) and combined in equimolar ratios to form sublibraries. The library was divided up into four sublibraries with sublibrary 1 covering positions 1–40, sublibrary 2 covering positions 41–80, sublibrary 3 covering positions 81–120, and sublibrary 4 covering positions 121–150. Sublibraries were transformed into electrocompetent XL1-Blue E. coli using a MicroPulser Electroporator (Bio Rad) and gene pulser cuvettes (Bio Rad, cat#165–2089). Cultures were miniprepped using a GeneJET plasmid miniprep kit (Thermo Scientific, cat#K05053). Library completeness was verified by deep sequencing on a MiSeq (Illumina).

### Growth rate measurements in the turbidostat for DHFR DL121 mutant library

DHFR DL121 sublibraries were transformed into ER2566 ∆folA ∆thyA E. coli by electroporation using a MicroPulser Electroporator (Bio Rad) and gene pulser cuvettes (Bio Rad, cat#165–2089). Cultures were grown overnight at 37°C in GM9 minimal media (93.0 mM Sodium (Na+), 22.1 mM Potassium (K+), 18.7 mM Ammonium (NH4), 1.0 mM Calcium (Ca2+), 0.1 mM Magnesium (Mg2+), 29.2 mM Chloride (Cl-), 0.1 mM Sulfate (SO42-), and 42.2 mM Phosphate (PO43-), 0.4% glucose) pH 6.50, containing 50 µg/mL thymidine and 30 µg/mL chloramphenicol (Sigma, cat#C0378-5G) as well as folA mix which contains 38 µg/mL glycine (Sigma, cat#50046), 75.5 µg/mL L-methionine (Sigma, cat#M9625) 1 µg/mL calcium pantothenate (Sigma, cat#C8731), and 20 µg/mL adenosine (Sigma, cat#A9251). Four hours before the start of the experiment, the overnight culture was diluted to an optical density of 0.1 at 600 nm in GM9 minimal media containing 50 µg/mL thymidine and 30 µg/mL chloramphenicol and incubated for four hours at 30°C. The cultures were centrifuged at 2000 RCF for 10 min and resuspended in the experimental conditions of GM9 minimal media containing 1 µg/mL thymidine and 30 µg/mL chloramphenicol. This was repeated two more times. The cultures were then back-diluted to an OD600 of 0.1 in 16 mL/vial of media. The turbidostat described in Toprak et al., 2013 was used in continuous culture (turbidostat) mode with a clamp OD600 of 0.15 and a temperature of 30°C. Each vial had a stir bar. Vials designated as ‘lit’ had one 5V blue LED active. The optical density was continuously monitored throughout the experiment. 1 mL samples were taken at the beginning of selection (0 hr) and at 4, 8, 12, 16, 20, and 24 hr into selection and were centrifuged at 21,130 RCF for 5 min at room temperature with the pellet being stored at −20°C for sequencing sample preparation.

### Growth rate measurements in the turbidostat for DHFR control library

Wild-type DHFR, 12 DHFR point mutants (D27N, F31V, F31Y, F31Y-L54I, G121V, G121V-F31Y, G121V-M42F, L54I, L54I-G121V, M42F, and W22H), and three chimeric DHFR-LOV2 fusion constructs (DL116, DL121, and DL121-C450S) each in a pACYC-Duet vector with TYMS as described in Reynolds et al., 2011 were transformed into ER2566 ∆folA ∆thyA E. coli by electroporation using a MicroPulser Electroporator (Bio Rad) and gene pulser cuvettes (Bio Rad, cat#165–2089) (Reynolds et al., 2011). Cultures were grown overnight at 37°C in GM9 minimal media (93.0 mM Sodium (Na+), 22.1 mM Potassium (K+), 18.7 mM Ammonium (NH4), 1.0 mM Calcium (Ca2+), 0.1 mM Magnesium (Mg2+), 29.2 mM Chloride (Cl-), 0.1 mM Sulfate (SO42-), and 42.2 mM Phosphate (PO43-), 0.4% glucose) pH 6.50, containing 50 µg/mL thymidine and 30 µg/mL chloramphenicol (Sigma, cat#C0378-5G) as well as folA mix which contains 38 µg/mL glycine (Sigma, cat#50046), 75.5 µg/mL L-methionine (Sigma, cat#M9625) 1 µg/mL calcium pantothenate (Sigma, cat#C8731), and 20 µg/mL adenosine (Sigma, cat#A9251). Four hours before the start of the experiment the overnight culture was diluted to an optical density of 0.1 at 600 nm in GM9 minimal media containing 50 µg/mL thymidine and 30 µg/mL chloramphenicol and incubated for four hours at 30°C. The cultures were centrifuged at 2000 RCF for 10 min and resuspended in the experimental conditions of GM9 minimal media containing 1 µg/mL thymidine and 30 µg/mL chloramphenicol. This was repeated two more times. The cultures were then back-diluted to an OD600 of 0.1 and pooled at equal (1/16th) ratios and aliquoted into four ‘dark’ and four ‘lit’ vials with 16 ml culture. The turbidostat described in Toprak et al., 2013 was used in continuous culture (turbidostat) mode with a clamp OD600 of 0.15 and a temperature of 30°C. Each vial had a stir bar. Vials designated as ‘lit’ had one 5V blue LED active. The optical density was continuously monitored throughout the experiment. One mL samples were taken at the beginning of selection (0 hr) and at 4, 8, 12, 16, 20, and 24 hr into selection and were centrifuged at 21,130 RCF for 5 min at room temperature with the pellet being stored at −20°C for sequencing sample preparation.

### Plate reader assay for E. coli growth

Single point mutant DHFR-D27N, DL121 chimeric protein, and DL121 with a point mutant D27N each in a pACYC-Duet vector with TYMS as described in Reynolds et al., 2011 were transformed into ER2566 ∆folA ∆thyA E. coli by electroporation using a MicroPulser Electroporator (Bio Rad) and gene pulser cuvettes (Bio Rad, cat#165–2089) (Reynolds et al., 2011). Cultures were grown overnight at 37°C in GM9 minimal media (93.0 mM Sodium (Na+), 22.1 mM Potassium (K+), 18.7 mM Ammonium (NH4), 1.0 mM Calcium (Ca2+), 0.1 mM Magnesium (Mg2+), 29.2 mM Chloride (Cl-), 0.1 mM Sulfate (SO42-), and 42.2 mM Phosphate (PO43-), 0.4% glucose) pH 6.50, containing 50 µg/mL thymidine and 30 µg/mL chloramphenicol (Sigma, cat#C0378-5G) as well as folA mix which contains 38 µg/mL glycine (Sigma, cat#50046), 75.5 µg/mL L-methionine (Sigma, cat#M9625) 1 µg/mL calcium pantothenate (Sigma, cat#C8731), and 20 µg/mL adenosine (Sigma, cat#A9251). Four hours before the start of the experiment, the overnight culture was diluted to an optical density of 0.1 at 600 nm in GM9 minimal media containing 50 µg/mL thymidine and 30 µg/mL chloramphenicol and incubated for four hours at 30°C. The cultures were centrifuged at 2000 RCF for 10 min and resuspended in the experimental conditions of GM9 minimal media containing either 0, 1, or 50 µg/mL thymidine and 30 µg/mL chloramphenicol. The cells were centrifuged and resuspended two more times. The cultures were then back-diluted to an OD600 of 0.005 into 96-well plates with six replicates each.

### Next-generation sequencing Amplicon sample preparation

Cell pellets were lysed by the addition of 10 µL sterile water, mixed by pipetting, and incubated at 98°C for 5 min. One µL of this was then combined with 5 µL Q5 buffer (NEB, cat#M0491S), 0.5 µL 10 mM DNTP (Thermo Scientific, cat#R0192), 2.5 µL of 10 mM forward and reverse primers specific to the sublibrary and containing the TruSeq adapter sequence (Appendix 1: SL1V2, SL2V2, SL3V2, SL4V2, DL121CLV3F, and DL_WTTS_R3), 0.25 µL of Q5 enzyme (NEB, cat#M0491S) and 13.25 µL of sterile water. These samples were then heated at 98°C for 90 s and then cycled through 98°C for 10 s 63–65°C (sublibrary 1: 66°C, sublibrary 2: 63°C, sublibrary 3: 64°C, and sublibrary 4: 65°C) for 15 s and then 72°C for 15 s, repeating 20 times with a final 72°C heating for 120 s in a Veriti 96-well thermocycler (Applied Biosystems). These samples were then amplified using TruSeq PCR reactions with a unique combination of i5/i7 indexing primers for each timepoint. 1 µL of this PCR reaction was then combined with 5 µL Q5 buffer (NEB, cat#M0491S), 0.5 µL 10 mM DNTP (Thermo Scientific, cat#R0192), 2.5 µL of 10 mM forward and reverse primers, 0.25 µL of Q5 enzyme (NEB, cat#M0491S) and 13.25 µL of sterile water. These samples were then heated at 98°C for 30 s and then cycled through 98°C for 10 s 55°C for 10 s and then 72°C for 15 s, repeating 20 times with a final 72°C heating for 60 s in a Veriti 96 well thermocycler (Applied Biosystems). Amplified DNA from i5/i7 PCR reaction was quantified using the picogreen assay (Thermo Scientific, cat#P7589) on a Victor X3 multimode plate reader (Perkin Elmer) and the samples were mixed in an equimolar ratio. The DNA was then purified by gel extraction and a DNA Clean and Concentrator −5 kit (Zymo Research, cat#D4014). DNA quality was determined by 260 nm/230 nm and 260 nm/280 nm ratios on a DS-11 +spectrophotometer (DeNovix) and concentration was determined using the Qubit 3 (Thermo Scientific). Pooled samples were sent to GeneWiz where they were analyzed by TapeStation (Agilent Technologies) and sequenced on a HiSeq 4000 sequencer (Illumina) with 2 × 150 bp dual index run with 30% PhiX spike-in yielding 1.13 billion reads. The control library was sequenced in-house using a MiSeq sequencer (Illumina) with 2 × 150 bp dual index 300 cycle MiSeq Nano Kit V2 (Illumina cat#15036522) with 20% PhiX (Illumina cat#FC-110–3001) spike-in yielding 903,488 reads.

### DHFR chimeric expression constructs

The E. coli DHFR LOV2 fusion was cloned as an NcoI/XhoI fragment into the expression vector pHIS8-3 (Lee et al., 2008; Reynolds et al., 2011). Point mutants were engineered into the DHFR gene using QuikChange II site-directed mutagenesis kits (Agilent cat#200523) using primers specified in Appendix 1. All DHFR/LOV2 fusions for purification were expressed under control of a T7 promoter, with an N-terminal 8X His-tag for nickel affinity purification. The existing thrombin cleavage site (LVPRGS) following the His-tag in pHIS8-3 was changed to a TEV cleavage site using restriction-free PCR to improve the specificity of tag removal (Bond and Naus, 2012). All constructs were verified by Sanger DNA sequencing.

### Protein expression and purification

DHFR-LOV2 chimeric proteins were expressed in BL21(DE3) E. coli grown at 30°C in Terrific Broth (12 g/L Tryptone, 24 g/L yeast extract, 4 mL/L glycerol, 17 mM KH2PO4, and 72 mM K2HPO4). Protein expression was induced when the cells reached an absorbance at 600 nm of 0.7 with 0.25 mM IPTG, and cells were grown at 18°C overnight. Cell pellets were lysed by sonication in binding buffer (500 mM NaCl, 10 mM imidazole, 50 mM Tris-HCL, pH 8.0) added at a volume of 5 ml/g cell pellet. Next the lysate was clarified by centrifugation and the soluble fraction was incubated with equilibrated Ni-NTA resin (Qiagen cat#4561) for 1 hr at 4°C. After washing with one column volume of wash buffer (300 mM NaCl, 20 mM imidazole, 50 mM Tris-HCL, pH 8.0) the DHFR-LOV2 protein was eluted with elution buffer (1M NaCl, 250 mM imidazole, 50 mM Tris-HCL, pH 8.0) at 4°C. Eluted protein was dialyzed into dialysis buffer (300 mM NaCl, 1% glycerol, 50 mM Tris-HCl, pH 8.0) at 4°C overnight in 10,000 MWCO Thermo protein Slide A Lyzer (Fisher Scientific cat#PI87730). Following dialysis, the protein was then purified by size exclusion chromatography (HiLoad 16/600 Superdex 75 pg column, GE Life Sciences cat#28989333). Purified protein was concentrated using Amicon Ulta 10 k M.W. cutoff concentrator (Sigma cat#UFC801024) and flash frozen using liquid N2 prior to enzymatic assays.

### Steady state Michaelis Menten measurements

The protein was spun down at 21,130 RCF at 4°C for 10 min and the supernatant was moved to a new tube with any pellet being discarded. The concentration of the protein was quantitated by A280 using a DS-11 +spectrophotometer (DeNovix) with an extinction coefficient of 44920 mM−1 cm−1. The parameters kcat and Km under Michaelis-Menten conditions were determined by measuring the initial velocity for the depletion of NADPH as measured in absorbance at 340 nm, with an extinction coefficient of 13.2 mM−1 cm−1. This is done in a range of substrate concentrations with a minimum of 8 data points around 4 Km, 2 Km, 1.5 Km, Km, 0.8 Km, 0.5 Km, 0.25 Km and 0. The initial velocities (slope of the first 15 s) were plotted vs. the concentration of Dihydrofolate and fit to a Michaelis Menten model using non-linear regression in GraphPad Prism 7. The reactions are run in MTEN buffer (50 mM 2-(N-morpholino)ethanesulfonic acid, 25 mM tris base, 25 mM ethanolamine, 100 mM NaCl) pH 7.00, 5 mM Dithiothreitol, 90 µM NADPH (Sigma-Aldrich cat#N7505) quantitated by A340. Dihydrofolate (Sigma-Aldrich cat#D7006) is suspended in MTEN buffer pH 7.00 with 0.35% β-mercaptoethanol and quantitated by A282 with an extinction coefficient of 28 mM−1 cm−1. Depletion of NADPH is observed in 1 mL cuvettes with a path length of 1 cm in a Lambda 650 UV/VIS spectrometer (Perkin Elmer) with attached water Peltier system set to 17°C. Lit samples are illuminated for at least 2 min by full spectrum 125 watt 6400K compact fluorescent bulb (Hydrofarm Inc cat#FLC125D). Dark samples were also exposed to the light in the same way as the lit samples but were in opaque tubs. Velocity, $V=k_{cat}[P]\frac{[S]}{K_{M}+[S]}$, was calculated using the concentration of DHF found in wild-type E. coli (~25 µM Kwon et al., 2008).

### Spectrophotometry of the LOV2 chromophore

The spectra of the LOV2 chromophore is determined with a Lambda 650 UV/VIS spectrometer (Perkin Elmer) at 350–550 nm using paired 100 μL Hellma ultra micro cuvettes (Sigma cat#Z600350-1EA) with a path length of 1 cm. Purified protein in was diluted (when possible) to 20 μM in MTEN buffer pH 7.00 with 0.35% β-mercaptoethanol The lit samples are illuminated for at least 2 min by full spectrum 125 watt 6400K compact fluorescent bulb (hydrofarm Inc). Relaxation of the lit state chromophore is observed in the Lambda 650 UV/VIS spectrometer (Perkin Elmer) at 447 nm (dark peak) using paired 100 μL Hellma ultra micro cuvettes (Sigma cat#Z600350-1EA) with a path length of 1 cm.

### Quantification and statistical analysis

#### Next-generation sequencing

The sequencing data analysis can be divided into two portions: (1) Read Joining, Filtering and Counting, followed by (2) Calculating Relative Fitness and Final Filtering. We describe each step below; all code was implemented in Bash shell scripting or Python 3.6.4. All analysis codes have been made available as a series of python 3 Jupyter Notebooks on github (https://github.com/reynoldsk/allostery-in-dhfr; McCormick et al., 2021; copy archived at swh:1:rev:dd8ee13f775f8b08548d64868f15e46583cbf543).

#### Read joining, filtering, and counting

The data analysis began with unjoined illumina fastq.gz files separated by index (generated by GeneWiz). The forward and reverse reads were combined using usearch v11.0.667 using the i86linux32 package. The commands given to usearch are contained in the script UCOMBINER.bsh.

Reads of each paired fastq file are identified and quality checked using the script DL121_fastq_analysis.py. Mutant nucleotide counts and number of wild-type reads are stored in a dictionary where the read count is separated by file name (vial and timepoint eg: T2V3) and sublibrary. If any nucleotide in the coding region is below a qscore cutoff of 30, that read is discarded. Counts of every nucleotide are saved in a text file by timepoint and vial.

Converting nucleotide variation to amino acid count as well as probabilistic sequencer error correction is done by the Hamming_analysis.ipynb script. Given the probabilistic nature of base calling on the Illumina platform, one can expect a number of reads that were errantly called. For each codon, the expected number of reads due to sequencing noise was calculated with the formula:

$$
NErrant_{t}^{Mut}=N_{t}^{WT}10^{\frac{\muQ}{-10}}^{HD}
$$

The number of errant mutants ($NErrant_{t}^{Mut}$) can be calculated from the number of observed wild type ($N_{t}^{WT}$), the average Q score of the sequencing run $\muQ$, and the hamming distance ($HD)$ or number of mutations away from. The number of errant mutants then subtracted from the actual mutant count. In addition to the number of observed wild type, this is calculated for every possible mutation observed, up to the 31 other nucleotide codons, (NNK codons are discarded due to the nature of library construction). Once the total number of errant reads are calculated and subtracted from the mutant and wild-type counts, they are then converted into the amino acid sequence and are saved into text files. These files are then used to load information for calculation of growth rate and allostery.

### Calculating relative fitness and final filtering

#### Growth_Rate_and_Allostery.ipynb

was the python script used for this analysis. Relative frequency was calculated as follows:

$$
ft=ln⁡\frac{N_{t}^{Mut}/N_{t}^{Wt}}{N_{t=0}^{Mut}/N_{t=0}^{Wt}}
$$

Variant frequencies ($N_{t}^{Mut}$) were determined relative to WT ($N_{t}^{Wt}$) and normalized to the initial frequency distribution at t=0. The relative growth rate then calculated by linear regression of these normalized frequencies. Light dependence was calculated as the difference between lit vs. dark growth rates. Variant frequency was only calculated if there were more than 50 mutant reads at time zero. Definitions for sector identity, conservation values, and surface identity used in SectorSurfaceDefinitions.ipynb are the same as those from Reynolds et al., 2011. Accessible surface area was calculated using MSMS, using a probe size of 1.4Å and excluding water as well as heteroatoms (Sanner et al., 1996). Values for total surface areas were taken from Chothia, 1976. Together these were used to calculate relative solvent accessible surface area, and 25% was used as a cutoff for 'surface'. A surface site is considered to contact the sector if the atoms comprising the peptide bond contact *any* sector atoms. Contact is defined as the sum of the atom's Pauling radii + 20%.

To determine significant allosteric mutations, a p-value for each mutation was computed by unequal variance t-test under the null hypothesis that the lit and dark replicate measurements have equal means. Two cutoffs were used, a standard cutoff of p=0.05, and a more stringent cutoff that is adjusted to consider multiple hypothesis testing. A multiple-hypothesis testing adjusted p-value of p=0.016 was determined by Sequential Goodness of Fit (Carvajal-Rodriguez and de Uña-Alvarez, 2011). General analysis and figures made from this data are performed in allostery_analysis.ipynb.
