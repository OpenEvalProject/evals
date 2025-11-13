# Multiplexed measurement of variant abundance and activity reveals VKOR topology, active site and human variant impact

## Authors

- Melissa A Chiasson<sup>1</sup> ([ORCID: 0000-0002-1880-3181](https://orcid.org/0000-0002-1880-3181))
- Nathan J Rollins<sup>2</sup>
- Jason J Stephany<sup>1</sup>
- Katherine A Sitko<sup>1</sup>
- Kenneth A Matreyek<sup>1</sup>
- Marta Verby<sup>3</sup>
- Song Sun<sup>3</sup>
- Frederick P Roth<sup>3</sup>
- Daniel DeSloover<sup>4</sup>
- Debora S Marks<sup>2</sup> ([ORCID: 0000-0001-9388-2281](https://orcid.org/0000-0001-9388-2281))
- Allan E Rettie<sup>5</sup>
- Douglas M Fowler<sup>1</sup> ([ORCID: 0000-0001-7614-1713](https://orcid.org/0000-0001-7614-1713)) †

### Affiliations

1. Department of Genome Sciences, University of Washington Seattle United States
2. Department of Systems Biology, Harvard Medical School Boston United States
3. Donnelly Centre and Departments of Molecular Genetics and Computer Science, University of Toronto, and Lunenfeld-Tanenbaum Research Institute, Sinai Health System Toronto Canada
4. Color Genomics Burlingame United States
5. Department of Medicinal Chemistry, University of Washington Seattle United States
6. Department of Bioengineering, University of Washington Seattle United States

† Corresponding author

## Abstract

Vitamin K epoxide reductase (VKOR) drives the vitamin K cycle, activating vitamin K-dependent blood clotting factors. VKOR is also the target of the widely used anticoagulant drug, warfarin. Despite VKOR’s pivotal role in coagulation, its structure and active site remain poorly understood. In addition, VKOR variants can cause vitamin K-dependent clotting factor deficiency or alter warfarin response. Here, we used multiplexed, sequencing-based assays to measure the effects of 2,695 VKOR missense variants on abundance and 697 variants on activity in cultured human cells. The large-scale functional data, along with an evolutionary coupling analysis, supports a four transmembrane domain topology, with variants in transmembrane domains exhibiting strongly deleterious effects on abundance and activity. Functionally constrained regions of the protein define the active site, and we find that, of four conserved cysteines putatively critical for function, only three are absolutely required. Finally, 25% of human VKOR missense variants show reduced abundance or activity, possibly conferring warfarin sensitivity or causing disease.

## Introduction

The enzyme vitamin K epoxide reductase (VKOR) drives the vitamin K cycle, which activates blood coagulation factors. VKOR, an endoplasmic reticulum (ER) localized transmembrane protein encoded by the gene VKORC1, reduces vitamin K quinone and vitamin K epoxide to vitamin K hydroquinone (Li et al., 2004; Rost et al., 2004). Vitamin K hydroquinone is required to enable gamma-glutamyl carboxylase (GGCX) to carboxylate Gla domains on vitamin K-dependent blood clotting factors. VKOR is inhibited by the anticoagulant drug warfarin (Czogalla et al., 2017; Zimmermann and Matschiner, 1974), and VKORC1 polymorphisms contribute to an estimated ~25% of warfarin dosing variability (Owen et al., 2010). For example, variation in VKORC1 noncoding and coding sequence can cause warfarin resistance (weekly warfarin dose >105 mg) or warfarin sensitivity (weekly warfarin dose <~10 mg) (Osinbowale et al., 2009; Yuan et al., 2005).

Though 15 million prescriptions are written for warfarin each year (https://www.clincalc.com), fundamental questions remain regarding its target, VKOR. For example, the structure of human VKOR is unsolved, though a bacterial homolog has been crystallized (Li et al., 2010). A homology model based on bacterial VKOR has four transmembrane domains, but the quality of the homology model is unclear, as human VKOR has only 12% sequence identity to bacterial VKOR. Moreover, experimental validation of VKOR topology yielded mixed results: similar biochemical assays suggested either three- or four- transmembrane- domain topologies (Schulman et al., 2010; Tie et al., 2012; Shen et al., 2017; Wu et al., 2018).

Topology informs basic aspects of VKOR function including where vitamin K and warfarin bind, so determining the correct topology and validating the homology model is critical. In particular, VKOR has four functionally important, absolutely conserved cysteines at positions 43, 51, 132, and 135, the orientation of which differs between the two proposed topologies. In the four transmembrane domain topology, all four cysteines are located on the ER lumenal side of the enzyme. In this topology, cysteines 43 and 51 are hypothesized to be ‘loop cysteines’ that pass electrons from an ER-anchored reductase, possibly transmembrane thioredoxin-related protein (Schulman et al., 2010), to the active site (Rishavy et al., 2011). However, in the three transmembrane domain topology, these cysteines are located in the cytoplasm and other pathways would be required to convey electrons to the redox center. Even for non-catalytic residues, topology plays an important role. For example, vitamin K presumably binds near the redox center, and topology dictates which residues make up the substrate binding site.

To understand the effect of human variants and to define the vitamin K and warfarin binding sites, VKOR variant activity has been extensively studied in cell-based assays (Czogalla et al., 2017; Shen et al., 2017; Tie et al., 2013). In addition to activity, VKOR protein abundance has also been studied because abundance is an important driver of disease and warfarin response. For example, VKOR R98W is a decreased- abundance variant that, in homozygous carriers, causes vitamin K-dependent clotting factor deficiency 2 (Rost et al., 2004). A 5’ UTR polymorphism reduces VKOR abundance and can be used to predict warfarin sensitivity (Gong et al., 2011). However, so far, the activity and abundance of only a handful of VKOR variants has been tested.

Here, we used multiplexed, sequencing-based assays (Gasperini et al., 2016) to measure the effects of 2,695 VKOR missense variants on abundance and 697 variants on activity. Our analysis of the large-scale functional data supports a four transmembrane domain topology, which an orthogonal evolutionary coupling analysis confirmed. Next, we identified distinct mutational tolerance groups, which are concordant with a four transmembrane homology model. Combining this homology model with variant abundance and activity effects, we identified an active site that contains the catalytic residues C132 and C135 and shares six positions with a previously proposed vitamin K binding site (Czogalla et al., 2017). We found that of four conserved cysteines putatively critical for function, only three are absolutely required, and analyzed the mutational signatures of two putative ER retention motifs. Human VKORC1 variants present in genetic databases and contributed by a commercial genetic testing laboratory were each classified based on abundance and activity. While most variants show wild type-like activity, 25% show low abundance or activity, which could confer warfarin sensitivity or cause disease in a homozygous context. Finally, we analyzed warfarin resistance variants and found that they span a range of abundances, indicating that increased abundance is an uncommon mechanism of warfarin resistance.

## Results

### Multiplexed measurement of VKOR variant abundance using VAMP-seq

To measure the abundance of VKOR variants, we applied Variant Abundance by Massively Parallel sequencing (VAMP-seq), an assay we recently developed (Matreyek et al., 2018). In VAMP-seq, a protein variant is fused to eGFP with a short amino acid linker. If the variant is stable and properly folded, then the eGFP fusion will not be degraded, and cells will have high eGFP fluorescence. In contrast, if the variant causes the protein to misfold, protein quality control machinery will detect and degrade the eGFP fusion, leading to a decrease in eGFP signal (Figure 1a). mCherry is also expressed from an internal ribosomal entry site (IRES) to control for expression. Differences in abundance are measured on a flow cytometer using the ratio of eGFP to mCherry signal. To determine whether VAMP-seq could be applied to VKOR, we fused eGFP to VKOR N- or C-terminally and found that both orientations had high eGFP signal (Figure 1—figure supplement 1). We compared N-terminally tagged wild type (WT) VKOR to R98W, a variant that ablates a putative ER retention motif and reduces abundance (Czogalla et al., 2014), and to TMD1Δ, a deletion of residues 10–30 which comprise the putative first transmembrane domain (TMD1; Figure 1b). Both reduced abundance variants exhibited much lower eGFP:mCherry ratios than WT, demonstrating that VAMP-seq could be applied to VKOR.

![Figure 1.](https://cdn.elifesciences.org/articles/58026/elife-58026-fig1-v1.jpg)

**Figure 1.:** (a) To measure abundance, an eGFP reporter is fused to VKOR. eGFP-tagged WT VKOR is folded correctly, leading to high eGFP fluorescence. However, a destabilized variant is degraded by protein quality control machinery, leading to low eGFP fluorescence. (b) Flow cytometry is used to bin cells based on their eGFP:mCherry fluorescence intensity. Density plots of VKOR library expressing cells (grey, n = 12,109) relative to three controls: WT VKOR (red, n = 4,756), VKOR 98W (blue, n = 2,453), and VKOR TMD1Δ (orange, n = 2,204) are shown. Quartile bins for FACS of the library are marked. (c) Abundance score density plots of nonsense variants (dashed blue line, n = 88), synonymous variants (dashed red line, n = 127), and missense variants (filled, solid line, n = 2,695). The missense variant density is colored as a gradient between the lowest 10% of abundance scores (blue), the WT abundance score (white) and abundance scores above WT (red). (d) Heatmap showing abundance scores for each substitution at every position within VKOR. Heatmap color indicates abundance scores scaled as a gradient between the lowest 10% of abundance scores (blue), the WT abundance score (white), and abundance scores above WT (red). Grey bars indicate missing variants. Black dots indicate WT amino acids. (e) Number of substitutions scored at each position for abundance. (f) Scatterplot comparing VAMP-seq derived abundance scores to mean eGFP:mCherry (n = 1 replicate) ratios measured individually by flow cytometry. Variants were selected at random to span the abundance score range. Error bars show standard error for abundance scores and standard error for eGFP:mCherry ratio.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/58026/elife-58026-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (a) Scatterplot of eGFP vs. mCherry fluorescence for cells expressing either C-terminally eGFP-tagged VKOR (VKOR-eGFP, blue) or N-terminally eGFP-tagged VKOR (eGFP-VKOR, red). (b) Pairwise abundance score correlations between replicate sorting experiments. Seven VAMP-seq replicates were performed. Pearson’s correlation coefficients are shown. Score numbers in this figure correspond to replicate numbers shown in Supplementary file 1.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/58026/elife-58026-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** (a) Ten variants that spanned the range of abundance scores were assayed individually via Western blot. Protein abundance was measured using a GFP-specific antibody, resulting in a band at ~42 kDa, the predicted size of an eGFP-VKOR fusion. A cofilin-specific antibody was used as the loading control. (b) Ratios of eGFP band intensity to cofilin band intensity from the Western blot were plotted versus the variant’s abundance score (Pearson’s R = 0.87).

We constructed a barcoded site-saturation mutagenesis VKOR library that covered 92.5% of all 3240 possible missense variants. To express this library in HEK293T cells we used a Bxb1 recombinase landing pad system we previously developed (Matreyek et al., 2017). In this system, each cell expresses a single VKOR variant. Recombined, VKOR variant-expressing cells were then sorted into quartile bins based on their eGFP:mCherry ratios. Each bin was deeply sequenced, and abundance scores were calculated based on each variant’s distribution across bins. Raw abundance scores were normalized such that WT-like variants had a score of one and total loss of abundance variants had a score of zero (Figure 1c). We performed seven replicates, which were well correlated (Figure 1—figure supplement 1, mean Pearson’s r = 0.73; mean Spearman’s ρ = 0.7, Supplementary file 1). Abundance score means and confidence intervals for each variant were calculated from the replicates.

The final dataset describes the effect of 2695 of the 3240 possible missense VKOR variants on abundance (Figure 1d and e). Validation of 10 randomly selected variants spanning the abundance score range showed high concordance between individual eGFP:mCherry ratios assessed by flow cytometry and VAMP-seq derived abundance scores (Figure 1f, Pearson’s r = 0.96, Spearman’s ρ = 0.97). Western blots of these variants also showed high concordance with abundance scores (Figure 1—figure supplement 2).

### Multiplexed measurement of VKOR variant activity using a gamma-glutamyl carboxylation reporter

We also measured VKOR variant activity, adapting a HEK293 cell assay based on vitamin K- dependent gamma-glutamyl carboxylation of a cell-surface reporter protein (Haque et al., 2014). In this assay, if VKOR is active, a Factor IX domain reporter is carboxylated, secreted and retained on the cell surface where it is detected with a carboxylation-specific, fluorophore-labeled antibody. However, if VKOR is inactive, the reporter is not carboxylated and the antibody cannot bind (Figure 2a). We modified the HEK293 activity reporter cell line to eliminate endogenous VKOR activity by knocking out both VKORC1 and its paralog, VKORC1-like 1 (VKORC1L1) (Tie et al., 2013; Figure 2—figure supplement 1). We also installed a Bxb1 landing pad to facilitate expression of individual VKOR variants or libraries (Figure 2—figure supplement 1). Recombination of WT VKORC1 into the landing pad of the HEK293 VKOR activity reporter cell line yielded robust reporter activation, demonstrating that the reporter line could be used to assess the activity of a library of VKOR variants (Figure 2b).

![Figure 2.](https://cdn.elifesciences.org/articles/58026/elife-58026-fig2-v1.jpg)

**Figure 2.:** (a) Left panel, A Factor IX Gla domain reporter is expressed inHEK293 cells and consists of a prothrombin pre-pro-peptide which allows for processing and secretion, a Factor IX Gla domain, and Proline rich Gla protein 2 (PRGP2) transmembrane and cytoplasmic domains. Middle panel, Cells expressing WT VKOR carboxylate the reporter Gla domain, which, upon trafficking to the cell surface, can be stained using a carboxylation-specific antibody conjugated to the fluorophore APC. Right panel, VKOR knockout cells do not carboxylate the reporter, so the fluorescent antibody does not bind. (b) Density plots of HEK293 activity reporter cells stained with APC-labeled carboxylation-specific antibody expressing no VKOR (blue, n = 7,188), WT VKOR (red, n = 4,107), or the VKOR variant library (grey, n = 41,418). Quartile bins for FACS of the library are marked. (c) Activity score density plots of nonsense variants (dashed blue line, n = 14), synonymous variants (dashed red line, n = 35), and missense variants (filled, solid line, n = 697). The missense variant density is colored as a gradient between the lowest 10% of activity scores (blue), the WT activity score (white) and activity scores above WT (red).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/58026/elife-58026-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (a) Western blot of parental cell line vs. HEK293 activity reporter cell line. Loading control is actin (42 kDa). VKOR was probed using an antibody generated against a peptide from the C-terminal of VKOR (FRKVQEPQGKAKRH) (Hallgren et al., 2006). The band for VKOR at 17 kDA is visible in the parental cell line but is not present in the HEK293 activity reporter cell line. (b) Scatterplot showing mTagBFP2 vs. eGFP mean fluorescence intensities for HEK293 activity reporter cells recombined with a construct encoding WT VKOR followed by internal ribosomal entry sequence and eGFP. The emergence of a distinct recombined population that is eGFP positive and mTagBFP2 negative (black outline, n = 768 cells) supports the presence of a single landing pad into the cell genome, and not multiple insertions. (c) A chromatogram showing the barcode sequence of the landing pad inserted at the AAVS1 locus in the HEK293 activity reporter cell line. The presence of a single barcode, highlighted in red, instead of mixed peaks, supports insertion of one landing pad rather than multiple landing pads.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/58026/elife-58026-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** Pairwise score correlations between replicate sorting experiments of VKOR activity. Six replicates of the activity assay were performed. Pearson’s correlation coefficients are shown. Score numbers in this panel correspond to replicate numbers shown in Supplementary file 2.

We recombined a library of VKORC1 variants into the HEK293 activity reporter cell line and sorted recombinant cells into quartile bins based on carboxylation-specific antibody binding. Each bin was deeply sequenced and, as for VAMP-seq, an activity score was computed for each variant. Final activity scores and confidence intervals were computed from six replicates for a total of 697 missense variants, 21.5% of those possible (Figure 2—figure supplement 2, mean Pearson’s r = 0.62 and mean Spearman’s ρ = 0.56, Supplementary file 2). Our activity score density plot showed that most variants had WT-like activity scores (Figure 2c).

### Human VKOR has four transmembrane domains

Two different domain models, one with three transmembrane domains and another with four, have been proposed for human VKOR (Li et al., 2010; Tie et al., 2012; Figure 3a). Because charged amino acids occur infrequently in transmembrane domains and should be less tolerated, we reasoned we could discriminate between these two models using a sliding window average of the effect of charged substitutions on VKOR abundance (Elazar et al., 2016a; Sharpe et al., 2010). We found four clearly demarcated regions where charged substitutions profoundly reduced VKOR abundance, relative to aliphatic substitutions (Figure 3b). To exclude the possibility that the eGFP tag used in our VAMP-seq assay somehow affected topology, we also analyzed the activity score data. The activity data, derived using native, untagged VKOR, revealed the same four minima as the abundance data (Figure 3c). In addition to these four minima, we also observed an activity score minimum at position 57, corresponding to a conserved serine at this position. This serine occurs at the end of the lumenal half-helix hypothesized to shield the active site from non-specific oxidation, so it is likely this signal is the result of disruption of that half helix. Together, these results strongly support the hypothesis that, like its distant bacterial homolog, human VKOR has four transmembrane domains.

![Figure 3.](https://cdn.elifesciences.org/articles/58026/elife-58026-fig3-v1.jpg)

**Figure 3.:** (a) Three and four transmembrane domain (TMD) models of VKOR, with TMDs in dark grey (Li et al., 2010; Tie et al., 2012). (b) Windowed abundance score means (width = 10 positions) for charged substitutions (green) and aliphatic substitutions (gold). Dark grey boxes correspond to TMDs proposed in the four-domain model. Dashed lines show median synonymous and the nonsense abundance scores. (c) Windowed activity score means (width = 10 positions) for charged substitutions (green) and aliphatic substitutions (gold). Boxes and dashed lines as described in b. (d) Secondary structure classification from local evolutionary couplings shown as alpha scores calculated for alpha helices (red) and beta sheets (blue). Dashed lines show significance cut-offs for alpha helices (1.5, red) and beta sheets (0.75, blue) (Toth-Petroczy et al., 2016). (e) A contact map derived from evolutionary couplings. Black points show pairs of positions with significant coupling. Light green points show predicted contacts between TMD1 and TMD2. Dark green points show predicted contacts between TMD1 and TMD4. (f) Predicted tertiary contacts between TMD1-TMD2 (shown in light green in e) and g, TMD1-TMD4 (shown in dark green in e) shown on the evolutionary couplings-derived hVKOR structural model. (h) Scatterplot comparing change in free energy for membrane insertion (Elazar et al., 2016a) (∆∆Gapp) to median abundance score for each amino acid substitution. Cytoplasmic and lumenal positions shown in black, TMD2 in light green, and TMDs 1, 3, and four in dark green. Charged substitutions shown as circles, all other substitutions as triangles.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/58026/elife-58026-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (a) Pymol graphic showing overlap between EVcouplings-folded model of VKOR (shown as a cartoon in green) compared to the bacterial structure (PDB: 4NV5, shown as a cartoon in grey). RMSD is 3.915903 Å over 120 residues. (b) Shows the same two structures, rotated 120°C.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/58026/elife-58026-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** Evolutionary couplings (black) from alignment of 1118 eukaryote sequences show an overall topology consistent with the bacterial 4-TM VKOR, and include contacts (green and dark-green) between helices in contact in 4-TM but not in a 3-TM topology. Based on fewer sequences, contact predictions are noisier than those from the full alignment. To best show the topology signal, we plot couplings beyond the top L strongest (gray).

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/58026/elife-58026-fig3-figsupp3-v1.jpg)

**Figure 3—figure supplement 3.:** (a) Histograms of abundance scores for missense variants, grouped by domain and colored by cytoplasmic, ER lumenal, or transmembrane localization. b, Hydrophobicity index of a bacterial MSA (red) and a mammalian MSA (blue), calculated using Hessa et al. scale (Hessa et al., 2005) and AlignMe server (Stamm et al., 2014).

To validate these findings, we performed evolutionary coupling analysis to infer the three-dimensional structure suggested by co-evolution. We aligned 6910 VKOR sequences from both eukaryotes and prokaryotes (1118 sequences from eukaryotes, 5731 from bacteria, and 61 from environmental samples and viruses) and identified coupled residues using the EVcouplings software (Hopf et al., 2012; Marks et al., 2011). Local patterns of evolutionary couplings (i.e. between nearby positions, i to i+4) supported a four-helix topology. The helices predicted by these local evolutionary couplings overlapped 70 of the 82 residues in alpha-helices of the bacterial structure (PDB 4NV5) (Shen et al., 2017) and included in our alignment (hyper-geometric test p-value=3.26−23, Figure 3d).

We identified non-local evolutionary coupling patterns characteristic of three-dimensional contacts, which also strongly supported the four transmembrane domain model. Using these contacts, we computationally folded human VKOR, yielding a modeled structure similar to the bacterial structure (RMSD = 2.58 Å over 97/143 Calpha, Figure 3—figure supplement 1, Supplementary file 3). The predicted tertiary structure had a four-helix topology, with antiparallel contacts between the full lengths of transmembrane domains 1 and 2 (Figure 3e, Figure 3f) and between the full lengths of transmembrane domains 1 and 4 (Figure 3e, Figure 3g). These antiparallel contacts would not be present in a three-helix topology and are only possible in a four-helix topology. This topology is also supported when we restricted our analysis to 1118 eukaryotic sequences exclusively (Figure 3—figure supplement 2).

Comparison of our abundance data to the energy required to insert different amino acids into the membrane yielded additional evidence for the four transmembrane domain model. The apparent change in free energy (ΔΔGapp) of insertion relative to wild type for every amino acid has been determined experimentally using deep mutational scanning of bacterial membrane proteins (Elazar et al., 2016a). Median abundance score and ΔΔGapp for each amino acid are correlated (Figure 3h). In particular, the large energetic cost of insertion of transmembrane domains with charged amino acids is apparent, including within the second transmembrane domain TMD2. Beyond insertion energies of individual amino acids, the overall hydrophobicity of transmembrane helices contributes to membrane protein insertion (Elazar et al., 2016a), as well as topology (Elazar et al., 2016b) and degradation (Guerriero et al., 2017). To determine whether overall helix hydrophobicity was a large factor contributing to abundance scores, we calculated the free energy for insertion (ΔGhelix) of each helix in the four transmembrane domain model using the ΔG prediction server v1.0 (Hessa et al., 2007) and TopGraph (Elazar et al., 2016b). Both predicted that transmembrane domain three had the most favorable ΔGhelix for insertion (ΔG prediction server: TMD1: 0.435, TMD2: 1.551, TMD3: −1.749, and TMD4: 1.734; Topgraph: TMD1: −6.3, TMD2: −5.5, TMD3: −12.6, TMD4: −4.3). Interestingly, we observed that TMD3 has a high density of substitutions with WT-like scores (Figure 3—figure supplement 3a), suggesting that TMD3’s favorable insertion energy might explain its mutational tolerance. In addition, the high concordance of hydrophobicity indices from bacterial and mammalian multiple sequence alignments further supports the conservation of a four transmembrane domain topology between bacteria and mammals (Figure 3—figure supplement 3b).

### Detailed structural context of VKOR variant abundance effects

Having confirmed that human VKOR has four transmembrane domains, we next explored the detailed pattern of mutational effects we observed in the context of a four transmembrane domain homology model. We generated a homology model of human VKOR with I-TASSER using the bacterial VKOR structure (Shen et al., 2017; Yang et al., 2015, Supplementary file 4). We performed hierarchical clustering of positions based on abundance scores, which yielded four groups of positions with characteristic mutational patterns (Figure 4a). In Group 1, most substitutions were neutral or increased abundance; in Group 2, charged amino acid and proline substitutions decreased abundance; in Group 3, all substitutions decreased abundance; and in Group 4, all substitutions decreased abundance profoundly. Each group corresponded to a spatially distinct region of the homology model structure (Figure 4b).

![Figure 4.](https://cdn.elifesciences.org/articles/58026/elife-58026-fig4-v1.jpg)

**Figure 4.:** (a) A heatmap showing hierarchical clustering of positions based on abundance score vectors, with the dendrogram above. Groups of positions, chosen based on the dendrogram, are numbered and colored. Heatmap color indicates abundance scores scaled as a gradient between the lowest 10% of abundance scores (blue), the WT abundance score (white) and abundance scores above WT (red). Grey bars indicate missing variants. Black dots indicate WT amino acids. (b) Positions in groups 1–4 shown on the VKOR homology model, with numbers and colors corresponding to panel a. (c) Boxplot showing relative solvent accessibility of positions in each cluster determined using DSSP (Kabsch and Sander, 1983; Touw et al., 2015) and colored as in b. Bold black line shows median, box shows 25th and 75th percentile. Line shows 1.5 interquartile range above and below percentiles, and outliers are shown as black points. (d) Histograms of abundance scores for missense variants in the cytoplasmic, ER lumenal, or transmembrane domains. (e) Histograms of activity scores for missense variants in the cytoplasmic, ER lumenal, or transmembrane domains.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/58026/elife-58026-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** Heatmap of abundance scores for all arginines and lysines in VKOR. First four positions (K30, K33, K35, K37) are in or proximal to transmembrane domain 1. Heatmap color indicates abundance scores scaled as a gradient between the lowest 10% of abundance scores (blue), the WT abundance score (white) and abundance scores above WT (red). Grey bars indicate missing variants. Black dots indicate WT amino acids.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/58026/elife-58026-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** Histograms of abundance scores for missense variants for three proteins: PTEN, TPMT, and VKOR.

Group one positions were located in or adjacent to cytoplasmic and ER lumenal loops, which were more tolerant of substitutions than the transmembrane domains. At four Group one positions, K30, R33, R35, and R37, almost every substitution increased abundance. These positively charged positions are positioned either at the edge of TMD1 (K30) or in the ER lumen directly abutting the top of TMD1 (R33, R35, and R37). The ‘positive inside rule’ (von Heijne, 1989), suggests that positive charges in membrane proteins generally reside in the cytoplasm, and this phenomenon is important for driving topology and membrane insertion (Elazar et al., 2016b; Nilsson and von Heijne, 1990; von Heijne, 1989). K30, R33, R35, and R37 violate the positive inside rule, and substitutions at these positions may increase abundance by reducing charge inside the ER, reducing topological frustration or increasing membrane insertion efficiency. Compared to the other 12 arginine and lysine positions in WT VKOR, K30, R33, R35, and R37 are the only ones where substitutions generally increased abundance (Figure 4—figure supplement 1). Our observations are consistent with a screen of rat VKOR variants intended to improve protein expression in E. coli where deletion of positions 31 to 33 increased protein levels (Hatahet et al., 2015).

In Group two, charged amino acids or proline substitutions generally decreased abundance. Group two consisted mostly of transmembrane positions that had side chains projecting into the lipid bilayer. Such transmembrane positions usually have hydrophobic, nonpolar side chains (Ulmschneider and Sansom, 2001). Proline has poor helix forming propensity, explaining why proline substitutions decreased abundance at these positions. Group 3 consisted of a mixture of cytoplasmic, ER lumenal and transmembrane positions where most substitutions decreased abundance. The cytoplasmic positions in this group included the putative dilysine ER localization motif at positions 159 and 161. Also in this group were R98, part of another putative ER retention motif at positions 98 and 100, and a glycine adjacent to TMD1 at position nine. The transmembrane positions had side chains projecting towards neighboring transmembrane helices, suggesting that, as for other membrane proteins (Fleming and Engelman, 2001; Mravic et al., 2019), intramolecular sidechain packing is important for abundance.

Finally, substitutions in Group 4, consisting of positions G19, Y88, I141, and L145, resulted in catastrophic loss of abundance. These positions are all in transmembrane domains with side chains projecting into the interior of the protein. On the basis of strict mutational intolerance of these positions, we hypothesized that their coordinated side chain packing comprises the core of the VKOR four helix bundle. Indeed, Group four residues had dramatically lower relative solvent accessibility than Groups 1–3 (Figure 4c).

The four transmembrane domain homology models also allowed us to explain VKOR’s unusual trimodal distribution of variant abundance scores. Previous VAMP-seq derived abundance score distributions for the cytosolic proteins TPMT and PTEN were bimodal (Figure 4—figure supplement 2; Matreyek et al., 2018), and 15 of 16 deep mutational scans of other soluble proteins using a variety of other assays also exhibited bimodal functional score distributions (Gray et al., 2017). Because VKOR is an ER resident, transmembrane protein, we hypothesized that its unusual trimodal abundance score distribution resulted from transmembrane domain substitutions. Indeed, the lowest mode of the distribution was composed almost exclusively of deleterious transmembrane domain substitutions (Figure 4d). In contrast, the intermediate mode consisted of substitutions in the ER lumen, cytoplasm, and transmembrane domains. Similarly, substitutions that profoundly decreased activity occurred in transmembrane domains (Figure 4e).

### Variant activity and abundance identify functionally constrained regions of VKOR

We reasoned that our activity and abundance data could reveal the location of functionally important positions in VKOR, including the active site, since functionally important positions should have many loss-of-activity but few loss-of-abundance variants. Thus, we calculated the specific activity for each variant by taking the ratio of its rescaled activity score and abundance score (see Methods). We computed the median specific activity for each position; substitutions at positions with low median specific activity generally have low activity relative to their abundance. We set a specific activity threshold based on two absolutely conserved cysteines that form VKOR’s redox center, C132 and C135. Using this threshold, positions with the lowest 12.5% of specific activity scores and with at least four variants scored for activity were deemed functionally constrained and mapped on the homology model of VKOR (Figure 5a, Figure 5—figure supplement 1). These 11 functionally constrained positions are organized around C132 and C135 and define, at least in part, the VKOR active site (Figure 5b,c, Figure 5—figure supplement 1). Among the functionally constrained positions are six positions previously identified in vitamin K docking simulations (Czogalla et al., 2017; Figure 5—figure supplement 1), including F55, which is hypothesized to bind vitamin K. Three functionally constrained positions, G60, R61, and A121, did not match any position in the predicted active site, but were immediate neighbors of W59 and L120, positions that are present in the predicted active site.

![Figure 5.](https://cdn.elifesciences.org/articles/58026/elife-58026-fig5-v1.jpg)

**Figure 5.:** (a) Positions with the lowest 12.5% of median specific activity scores and at least four variants scored for activity are shown as magenta spheres on the VKOR homology model. Cysteines C132, and C135, also in the bottom 12.5% of median specific activity scores, are shown in green spheres. (b) Magnified view of the redox center cysteines (positions 132, and 135, green spheres) and surrounding residues that define the active site (magenta spheres). Residues shown in transparent spheres, with side chains also shown in sticks. (c) Panel b rotated 120°.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/58026/elife-58026-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** (a) Histogram of specific activity, with catalytic cysteines C132 and C135 labeled in blue. Dashed line demarcates bottom 12.5%. (b) Active site positions as defined by computational docking, shown on the homology model as yellow spheres (Czogalla et al., 2017). (c) Heatmap of activity scores for residues with lowest 12.5% of specific activity scores, collapsed by amino acid class. Color indicates activity scores scaled as a gradient between the lowest 10% of activity scores (blue), the WT activity score (white) and activity scores above WT (red). Grey indicates missing data. (d) Heatmap of abundance scores for residues with lowest 12.5% of specific activity scores. Color legend same as described in c, applied to abundance scores. (e) Specific activity scores of a subset of variants, with error bars showing standard deviation. (f) Histogram of coefficient of variation for the specific activity value.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/58026/elife-58026-fig5-figsupp2-v1.jpg)

**Figure 5—figure supplement 2.:** (a) Heatmap of activity scores for cysteines. Catalytic cysteines C132 and C135 labeled in green. Color indicates activity scores scaled as a gradient between the lowest 10% of activity scores (blue), the WT activity score (white) and activity scores above WT (red). Grey indicates missing data. (b) Heatmap of abundance scores for cysteines. Catalytic cysteines C132 and C135 labeled in green. Color legend same as described in a, applied to abundance scores.

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/58026/elife-58026-fig5-figsupp3-v1.jpg)

**Figure 5—figure supplement 3.:** (a) Heatmap of abundance scores for diarginine ER retention motif. X-axis shows residues and position. Color indicates abundance scores scaled as a gradient between the lowest 10% of abundance scores (blue), the WT abundance score (white) and abundance scores above WT (red). Grey indicates missing data. (b) Heatmap of abundance score for dilysine ER retention motif. X-axis shows residues and position.

Besides C132 and C135, VKOR has two additional absolutely conserved cysteines, C43 and C51. In the four transmembrane domain model, C43 and C51 are postulated to be loop cysteines that relay electrons to the C132/C135 redox center (Liu et al., 2014). We classified C43 as having low specific activity, but we only observed one variant at this position, so it was not included in our set of functionally constrained positions (Figure 5—figure supplement 2). In contrast, substitutions at C51 resulted in only modest activity loss, a phenomenon that has been observed previously (Shen et al., 2017). Interestingly, every substitution at C51 and 15 of 19 at C132 decreased VKOR abundance (Figure 5—figure supplement 2). Inside cells, the majority of VKOR molecules have a C51-C132 disulfide bond, and warfarin binds to this redox state of VKOR (Shen et al., 2017). Since disruption of this disulfide bond apparently impacts abundance as well as activity, this bond may be important for VKOR folding and stability.

VKOR is thought to contain two sequences important for ER localization. The first is a diarginine motif (RxR) at positions 98–100, and the second is a dilysine motif (KXKXX) at positions 159–163. While we did not directly measure localization, we found that only six of 19 R98 variants and seven of 14 R100 variants resulted in low abundance (Figure 5—figure supplement 3). In contrast, nearly all variants at K159 (14 of 18) and K161 (17 of 19) resulted in low abundance (Figure 5—figure supplement 3). A histidine substitution was tolerated at position 161, which mimics the KXHXX motif commonly found in coronaviruses and a small number of human proteins (Ma and Goldberg, 2013). Because protein localization and degradation are coupled (Hessa et al., 2011), we suggest that the reductions in abundance we observe are the result of degradation caused by mislocalization, and that the dilysine motif at positions 159–163 is essential for VKOR ER localization. Overall, comparison of VKOR variant activity and abundance revealed functionally important regions, refining our understanding of the active site, redox-active cysteines, and ER retention motifs.

### Functional consequences of VKOR variants observed in humans

Variation in VKOR is linked to both disease and warfarin response, but the overwhelming majority of VKOR variants found in humans so far have unknown effects. Thus, we curated a total of 215 variants that had either been previously reported in the literature as affecting warfarin response (Supplementary file 5), were in ClinVar (Landrum et al., 2014), were in gnomAD v2 or v3 (Karczewski et al., 2019), or were present in individuals whose healthcare provider had ordered a multi-gene panel test from a commercial testing laboratory (Color Genomics) (Supplementary file 6). Of eight variants present in ClinVar, we included only one (D36Y) in our analysis as it was the only variant reviewed by an expert panel (Kurnik et al., 2012). 159 variants were present in gnomAD, and all but one missense variant (D36Y) had population frequencies less than 0.2%. 28 variants were literature-curated warfarin response variants, only 12 of which were in one of the databases surveyed. D36Y was the only warfarin response variant present in all databases, ClinVar, gnomAD, and Color (Figure 6—figure supplement 1).

We classified 193 of the 215 variants we curated according to their abundance (Supplementary file 6). All synonymous variants with the exception of two were WT-like or possibly WT-like, while the three nonsense variants were scored as low abundance (Figure 6a). Missense variants spanned all abundance categories, with 129 (60%) having WT-like or possibly WT-like abundance. 30 missense variants were low abundance, and 12 were high abundance. The single known pathogenic variant R98W was low abundance (Figure 6b). We also classified 54 variants according to their activity (Supplementary file 6). Only one variant, A115V, exhibited low activity. It had WT-like abundance, indicating that the loss of activity is not due to loss of abundance.

![Figure 6.](https://cdn.elifesciences.org/articles/58026/elife-58026-fig6-v1.jpg)

**Figure 6.:** (a) Histogram of abundance classifications for variants from gnomAD, ClinVar, and Color Genomics. Nonsense variants colored in blue, synonymous in red, and missense in grey. (b) Histogram of abundance classifications for same variants in a, colored by pathogenicity. The only variant known to cause disease, R98W, is colored in blue. All other variants shown in yellow. (c) Scatterplot showing abundance scores for literature-curated warfarin resistance variants. Bars show standard error and are colored by abundance class. Variants are arranged in order of abundance score.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/58026/elife-58026-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** Venn diagram of VKOR missense variants present in gnomAD v2 and v3, ClinVar, Color Genomics, a commercial genetic testing company, and literature-reported warfarin resistant variants.

We examined warfarin response variants including W5X, the only variant observed so far linked to human warfarin sensitivity (Oldenburg et al., 2004). As expected, W5X was low abundance, reinforcing that heterozygous loss of VKOR is the cause of warfarin sensitivity in carriers of this variant. Warfarin resistance variants, on the other hand, are predicted to abrogate warfarin binding (Li et al., 2010), but it is unclear whether these variants have appreciable effects on abundance or activity. We found that warfarin resistance variants span a range of abundances and that the distribution of warfarin resistant variant abundance was not different from missense variants generally (Figure 6c, two-sided Kolmogorov-Smirnov test p=0.438). Five warfarin-resistance variants had low abundance, suggesting that these variants must block drug binding or increase activity to confer resistance. One variant, A26T, had high abundance, a possible mechanism of warfarin resistance. The five warfarin resistance variants, R58G, W59L, V66M, G71A, and N77S, whose activity we scored, were all WT-like. Thus, our abundance and activity data are consistent with warfarin resistance arising largely from variants that block warfarin binding.

## Discussion

We conducted multiplexed assays to measure the effects of 2,695 VKOR variants on abundance and 697 variants on activity. Both abundance and activity data provided evidence for a four transmembrane topology, which was further supported by evolutionary couplings analysis. We evaluated a VKOR homology model in the context of the patterns of variant effects on abundance we measured and found that the homology model could explain these patterns. Low specific activity residues mapped onto this homology model identify, at least in part, the active site, which largely overlaps with the results of a vitamin K docking simulation (Czogalla et al., 2017). Our active site is shallower than what the docking simulation predicts; this is the result of low abundance scores at some of the deeper, transmembrane positions predicted by docking to bind the isoprenoid chain of vitamin K (F87, Y88), and poor coverage of activity scores for other positions (V112, S113). In light of the fact that substitutions at F87 and Y88 resulted in low abundance, we note that the modeled vitamin K binding mode would disrupt packing of VKOR core residues and require repacking of helices to maintain protein stability (Merkle et al., 2018). In addition to the active site, substitutions at the dilysine and, to a lesser extent, the diarginine ER localization motifs caused abundance loss.

We also used our large-scale functional data to analyze 215 VKOR variants found in humans. 16% of these variants affect neither activity nor abundance; we identified 54 previously uncharacterized low abundance or low activity variants that could be pathogenic or alter warfarin response. We found that only one warfarin resistance variant had increased abundance, indicating that increased abundance is not a pervasive warfarin resistance mechanism. Many of the other warfarin resistant variants have warfarin IC50s that are 10- to 100-fold higher than wildtype VKOR in cell assays (Shen et al., 2018), and this high level of resistance probably cannot be gained through increased protein abundance alone. All five of the warfarin resistance variants whose activity we scored were WT-like. Taken together these data support the notion that warfarin resistance generally involves alterations to warfarin binding rather than abundance or activity. We analyzed one known warfarin sensitivity variant, W5X, and found that it is low abundance, suggesting the possibility that any of the 53 other low abundance variants, if found in a person, might also confer warfarin sensitivity.

While our VKOR variant abundance and activity data illuminates various aspects of VKOR’s structure and function, the data have limitations. For example, neither assay captures variant effects on mRNA splicing, which means we cannot determine the effect of human splice site variants on VKOR activity or abundance. In addition, as a result of how these assays were engineered, both have limited dynamic ranges. Thus, subtle effects on abundance or activity cannot be discerned, and it is difficult to translate the scores these assays generated to a more precise biochemical measure, like absolute VKOR molecules present or enzymatic kinetics. In addition, both assays have inherent noise, largely arising from the limited number of cells we can sample due to the bottleneck of cell sorting. We account for this noise by filtering each dataset based on variant frequency and presenting a confidence interval for each abundance and activity score. Reengineering the assay to be growth-based, instead of flow cytometry-based, would increase the number of cells sampled and would most likely improve library coverage and score estimation.

In the future, we envision that the assays we used could be employed to better understand VKOR’s interaction with warfarin. Here, we could measure warfarin’s effect on both variant abundance and activity, mapping the warfarin binding site more finely. In addition, we could identify warfarin resistance mutations that have not yet been observed in the clinic and group variants by their putative resistance mechanism. Overall, our work highlights the value of multiplexed assays of variant effect for better understanding protein structure, function and human variant effects.

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
      <td>Antibody</td>
      <td>Murine anti-Factor IX carboxylated Gla domain (mouse monoclonal)</td>
      <td>Green Mountain Antibodies</td>
      <td>Cat#GMA-001</td>
      <td>(1:100)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>HRP Anti-beta-actin antibody (mouse monoclonal)</td>
      <td>Abcam</td>
      <td>Cat#ab20272; RRID:AB_445482</td>
      <td>(1:10,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Amersham ECL Mouse IgG, HRP-linked whole Ab (sheep polyclonal)</td>
      <td>GE Healthcare</td>
      <td>Cat#NA931; RRID:AB_772210</td>
      <td>(1:10,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Goat anti-Mouse IgG (H+L) Highly Cross-Adsorbed Secondary Antibody, Alexa Fluor Plus 488 (goat polyclonal)</td>
      <td>ThermoFisher</td>
      <td>Cat#:A32723; RRID:AB_2633275</td>
      <td>(1:10,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Goat anti-Rabbit IgG (H+L) Cross-Adsorbed Secondary Antibody, Alexa Fluor 647 (goat polyclonal)</td>
      <td>ThermoFisher</td>
      <td>Cat#:A-21244; RRID:AB_2535812</td>
      <td>(1:10,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>anti-Cofilin (D3F9) XP Rabbit mAb (rabbit monoclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>Cat#:5175; RRID:AB_10622000</td>
      <td>(1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-GFP from mouse IgG1κ (clones 7.1 and 13.1) (mouse monoclonal)</td>
      <td>Roche</td>
      <td>Cat#:11814460001; RRID:AB_390913</td>
      <td>(1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-VKOR (rabbit monoclonal)</td>
      <td>PMID:16634640</td>
      <td></td>
      <td>(1:1000)</td>
    </tr>
    <tr>
      <td>Strain, strain background (Escherichia coli)</td>
      <td>E. coli electrocompetent</td>
      <td>NEB</td>
      <td>Cat#C3020K</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>LYNX Rapid APC conjugation kit</td>
      <td>BioRad</td>
      <td>Cat#LNK033APC</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>SuperSignal West Dura Extended Duration Substrate</td>
      <td>ThermoFisher</td>
      <td>Cat#34076</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Library Quantification Kit (Illumina)</td>
      <td>KAPA Biosystems</td>
      <td>Cat#KK4854</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>MiSeq Reagent Kit v3 (600 cycles)</td>
      <td>Illumina</td>
      <td>Cat#MS-102–3003; RRID:SCR_016379</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>NextSeq 500/550 High Output v2 kit (75 cycles)</td>
      <td>Illumina</td>
      <td>Cat#TG-160–2005; RRID:SCR_016381</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>Qiagen miniprep kit</td>
      <td>Qiagen</td>
      <td>Cat#27106</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>GenElute HP Plasmid midiprep kit</td>
      <td>Sigma</td>
      <td>Cat#NA0200</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>DNA clean and concentrator kit</td>
      <td>Zymo</td>
      <td>Cat#D4031</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algortihm</td>
      <td>PyMOL</td>
      <td>Schrodinger</td>
      <td></td>
      <td>https://pymol.org</td>
    </tr>
    <tr>
      <td>Software, algortihm</td>
      <td>Enrich2</td>
      <td>PMID:28784151</td>
      <td></td>
      <td>https://github.com/FowlerLab/Enrich2</td>
    </tr>
    <tr>
      <td>Software, algortihm</td>
      <td>R</td>
      <td>R</td>
      <td></td>
      <td>https://cran.r-project.org/</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Fugene 6</td>
      <td>Promega</td>
      <td>Cat#E2691</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Lipofectamine 3000</td>
      <td>ThermoFisher</td>
      <td>L3000015</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Atomic coordinates, bacterial VKOR structure</td>
      <td>Protein Data Bank</td>
      <td>PDB: 4NV5</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Raw and analyzed data</td>
      <td>This paper</td>
      <td>GSE149922</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (human)</td>
      <td>293T AAVS1 tetbxb1 clone 4</td>
      <td>PMID:28335006</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (human)</td>
      <td>HEK293 VKOR activity reporter</td>
      <td>PMID:24297869</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>PX458</td>
      <td>Addgene</td>
      <td>Cat#48138; RRID:Addgene_48138</td>
      <td></td>
    </tr>
  </tbody>
</table>

### General reagents, DNA oligonucleotides, and plasmids

Details on general reagents can be found in the Key Resources table above. Unless otherwise noted, all chemicals were obtained from Sigma and all enzymes were obtained from New England Biolabs. E. coli were cultured at 37°C in Luria broth. All cell culture reagents were purchased from ThermoFisher Scientific unless otherwise noted. HEK 293 T cells (ATCC CRL-3216) and derivatives thereof were cultured in Dulbecco’s modified Eagle’s medium supplemented with 10% fetal bovine serum, 100 U ml−1 penicillin, and 0.1 mg ml−1 streptomycin. Cells were induced with 2.5 ug mL−1 doxycycline. Cells were passaged by detachment with trypsin-EDTA 0.25%, and cells were prepared for sorting by detachment with versene. All cell lines tested negative for mycoplasma. Cell line identity was not authenticated. Because our activity assay is vitamin-K dependent, all activity assays were done with the same lot of FBS to ensure similar concentrations of vitamin K in each replicate.

All synthetic oligonucleotides were obtained from IDT and can be found in Supplementary file 7. All non-library-related plasmid modifications were performed with Gibson assembly (Gibson et al., 2009).

### Library construction

A gBLOCK with a codon-optimized sequence for human VKOR was ordered from IDT. It was then cloned into the vector pHSG298 (Clontech). Saturation mutagenesis primers were designed for each codon in VKOR from positions 2 to 163 (Jain and Varadarajan, 2014) and ordered resuspended from IDT. Forward and reverse primers for each position were mixed at 2.5 mM, and used in a PCR reaction with 125 pg of pHSG298-VKOR, 5% DMSO, and 5 µL of KAPA Hifi Hotstart 2X ReadyMix. PCR products were visualized on a 0.7% agarose gel to confirm amplification of the correct product.

PCR products were then quantified using the Quant-iT PicoGreen dsDNA Assay kit (Invitrogen) using DNA control curves done in triplicate. To pool positions, a total amount of DNA for each reaction was calculated that maximized the volume to be drawn from the lowest concentration PCR product. Pooled PCR products were cleaned and concentrated using Zymogen Clean and Concentrate kit and then gel extracted. The pooled library was phosphorylated with T4 PNK (NEB), incubated at 37°C for 30 min, 65°C for 20 min, and then 4° indefinitely. 8.5 µL of this phosphorylated product was combined with 1 µL of 10X T4 ligase buffer (NEB) and 0.5 µL of T4 DNA ligase (NEB) to make a 10 µL overnight ligation reaction. This reaction was incubated at 16°C overnight.

The overnight ligation was then cleaned and concentrated (Zymogen) and eluted in 6 µL of ddH2O. 1 µL of this ligation was then transformed into high efficiency E. coli using electroporation at 2 kV. Each reaction contained 1 µL of ligation (or ligation control or pUC19 10 pg/uL) and 25 µL of E. coli 975 µL of pre-warmed SOC medium was added to each cuvette after electroporation, transferred to a culture tube, and recovered at 37°C, shaking for 1 hr. At 1 hr, 1 and 10 µL samples from all cultures were taken and plated on appropriate medium (LB + kanamycin for ligation and ligation control; LB + ampicillin for pUC19), the remaining 989 µL was used to inoculate a 50 mL culture (+ kanamycin). Plates and 50 mL culture were incubated at 37°C overnight (shaking for 50 mL culture). Colonies on plates were then counted, and counts were used to calculate how many unique molecules were transformed to gauge coverage of the library. 50 mL culture was spun down and midiprepped.

To transfer the library from pHSG298 to the recombination vector, the pHSG298 library and recombination vector were digested with XbaI and AflII for 1 hr at 65°C. The library and cut vector were then gel extracted. The library was then ligated with the cut vector at 5:1 using T4 ligase, overnight at 16°C. The ligation was heat inactivated the next morning, clean and concentrated. Another high efficiency transformation was performed the same as described above, except this ligation was plated on LB + ampicillin (antibiotic switching strategy). Plates and 50 mL culture were incubated at 37°C overnight (shaking for 50 mL culture). Colonies on plates were then counted, and counts were used to calculate how many unique molecules had been transformed to gauge coverage of the library. A 50 mL culture was spun down and midiprepped.

To barcode individual variants, plasmid library harvested from midiprep was digested with EcoRI-HF and NdeI at 37°C for 1 hr, 65°C for 20 min. Barcode oligos were ordered from IDT, resuspended at 100 uM, and then annealed by combining 1 µL each of primer with 4 µL CutSmart Buffer and 34 µL ddH2O and running at 98°C for 3 min followed by ramping down to 25°C at −0.1 °C/second. After annealing, 0.8 µL of Klenow polymerase (exonuclease negative, NEB) and 1.35 µL of 1 mM dNTPS was then combined with the 40 µL of product to fill in the barcode oligo (cycling conditions: 25°C for 15:00, 70°C for 20:00, ramp down to 37°C at −0.1 °C/s). Digested vector and barcode oligo were then ligated overnight at 16°C.

The overnight ligation was then cleaned and concentrated and eluted in 6 µL of ddH2O. 1 µL of this ligation was then transformed into high efficiency E. coli using electroporation at 2 kV. Each reaction contained 1 µL of ligation (or ligation control or pUC19 10 pg/uL) and 25 µL of E. coli. 975 µL of pre-warmed SOC medium was added to each cuvette after electroporation, transferred to a culture tube, and recovered at 37°C, shaking for 1 hr. At 1 hr, 1 and 10 µL samples from water and pUC19 cultures were taken and plated on LB supplemented with ampicillin. For ligation and ligation control, four flasks were prepared with 50 mLs of LB and ampicillin, and then 500 µL, 250 µL, 125 µL, 62.5 µL was sample from the 1 mL of recovery and transferred into a corresponding flask. From those flasks, 1 µL, 10 µL, and 100 µL, were sampled and plated onto LB ampicillin plates. Plates and 50 mL culture were incubated at 37°C overnight. Colonies on plates were then counted, and counts were used to calculate how many unique molecules were transformed to gauge number of barcodes. Flask with the target number of barcodes was then spun down and midiprepped.

### Cell line description

#### VAMP-seq assay cell line

HEK293T cells with a serine integrase landing pad integrated at the AAVS1 locus were used (Matreyek et al., 2017).

#### Activity assay cell line

We used a previously published reporter cell line (Haque et al., 2014) and inserted a recombinase-based landing pad at the AAVS1 safe harbor locus using a previously published strategy (Matreyek et al., 2017). Single cell clones were transfected with TALENs for AAVS1 and the landing pad plasmid, and single cell clones were sorted. Presence of one landing pad was confirmed by 1) barcode sequencing of the landing pad and 2) co-transfection experiment with GFP and mCherry. From this, we moved forward with one clone demonstrated to have only one landing pad present (clone 45).

gRNAs to delete portions of the first exon of both VKORC1 and VKORC1L1 were ordered and cloned into pSpCas9(BB)−2A-GFP (PX458), which was a gift from Feng Zhang (Addgene plasmid #48138; http://n2t.net/addgene:48138; RRID:Addgene_48138). Clone 45 was then transfected with these four plasmids, and single cells were sorted based on GFP positivity. Disruption of VKORC1 and VKORC1L1 was confirmed by performing nested PCR, TA cloning, and then sequencing of products. We detected three alleles for both VKORC1 and VKORC1L1, indicating that these loci are triploid in HEK293 cells.

A Western blot was also used to confirm absence of VKOR protein product in our activity reporter cell line. Protein lysates were harvested from ~1 million cells using 100 µL NP40 lysis buffer with freshly prepared protease inhibitor cocktail and 1 mM PMSF. Protein lysates were Qubited for concentration, and 20 ug of each protein lysate was loaded. 4–12% BisTris NuPage gel (Thermo Fisher) was used with MES buffer + 500 µl of antioxidant added to the inner chamber. The gel ran at 150V for 90 min. Gel was then transferred to Nitrocellulose using 1X transfer buffer 20% EtOH at 24V for 1 hr on ice. The blot was washed for 5 min with 1X TBS-T 0.1% Tween three times. Blot was then blocked for overnight 1X TBS-T 0.1% Tween + 5% Milk. Blot was then washed for 5 min with 1X TBS-T 0.1% Tween three times. Blot was then cut in half at the between the 25 kDa and 35 kDa molecular weight markers. The bottom blot was incubated with: αVKOR 1:1000 + 1X TBS-T 0.1% Tween + 5% Milk. The top blot was incubated with αbeta-actin dHRP 1:1000+ 1X TBS-T 0.1% Tween + 5% Milk. Both blots were incubated with their primary antibodies overnight at 4°C. The αVKOR blot was washed for 5 min with 1X TBS-T 0.1% Tween three times. The αVKOR blot was then incubated with 1:10,000 secondary anti-mouse-HRP (GE Healthcare NA931V) + 1X TBS-T 0.1% Tween + 5% Milk for one hour. The αbeta-actin dHRP blot remained in primary antibody during this time, as no secondary antibody is needed for a direct HRP conjugate. Both blots were then washed for 5 min with 1X TBS-T 0.1% Tween three times. Blots were then incubated with Supersignal West Dura Extended Duration Substrate (Thermo Fisher). 500 µl of both substrates incubated on blot for 5 min. Blots were then dried by kimwipe and exposed using the colorimetric and chemiluminescence functions on the BioRad ChemiDoc MP (Biorad).

#### Recombination of variants in cell lines: abundance assay

Cells were transfected in six well plates, 250,000 cells per well (12–24 wells transfected total for each experiment). Sequential transfections were performed. On day 1, 3 ug of pCAG-NLS-Bxb1 was diluted in 250 µL of OptiMEM and 6 µL of Fugene (Promega). On day 2, 3 ug of barcoded library was diluted in 250 µL of OptiMEM and 6 µL of Fugene6 and transfected. 48 hr after this second transfection, cells were induced with doxycycline at a final concentration of 2.5 ug/mL.

#### Recombination of variants in cell lines: activity assay

Cells were transfected in six- well plates, 500,000 cells per well (18–24 wells transfected total for each experiment). 272 ng of pCAG-NLS-Bxb1 was diluted in 125 uL of OptiMEM with 2.7 ug of barcoded library. 2.25 uL of Lipofectamine 3000 (Thermo Fisher) was diluted in 125 uL of OptiMEM in a separate tube. The DNA mixture was then added to the Lipofectamine 3000 mixture and incubated at room temperature for 15 min. Transfection mixture was then added dropwise to one six-well plate. Cells were induced with doxycycline 48 hr after transfection, with a final concentration of 2.5 ug/mL doxycycline.

#### Enrichment sorting for recombined cells

Cells were washed once with PBS, then dissociated with versene. Medium was added to dilute EDTA, and cells transferred to 15 mL conical and spun down at 300 x g for 4 min. Medium was aspirated off, and cells were resuspended in PBS, then filtered through a 35 um nylon mesh filter. Cells were sorted on a BD Aria III FACS machine. mTagBFP2, expressed from the unrecombined landing pad, was excited with a 405 nM laser. Recombined cells either expressed mCherry (abundance) or eGFP (activity), and these were excited by a 561 nm laser and a 488 nm laser, respectively. Samples were gated for live cells using FSC-A and SSC-A, then singlets using SSC-H vs. SSC-W, FSC-H vs. FSC-W. For activity assay reporter cell line, cells were then sorted for DsRed positivity to ensure robust expression of reporter. Cells that had successfully recombined a single VKOR variant were gated on recombinant mTagBFP2 negativity and either mCherry positivity (abundance) or eGFP positivity (activity) (see Figure 2—figure supplement 1b for gating example). Recombined cells were sorted on ‘Yield’ mode in the BD Diva software and grown out for 3–5 days.

#### Abundance assay quartile sorting

Recombined cells were run on a BD Aria III FACS machine. Cells were prepared for sorting as described above, and were then gated for live, recombined singlets. A ratio of eGFP/mCherry was created using the BD Diva software as a unique parameter, and the histogram of this ratio was divided into four equal bins. Each quartile was sorted into a 5 mL tube on ‘4-Way Purity’ mode. Sorted cells were grown out for 2–4 days post sorting to ensure enough DNA for sequencing. The details of replicate sorts for activity assay are in Supplementary file 1.

#### Antibody conjugation

Factor IX Gla domain antibody specific for carboxylation was conjugated to APC following LYNX Rapid APC Antibody Conjugation Kit instructions. Antibody was resuspended at 1 mg/mL in nuclease-free water. 1 µL of Modifier reagent was then added for every 10 µL of antibody and mixed by pipetting. That mixture was then pipetted directly onto the LYNX lyophilized mix and gently mixed by pipetting up and down twice. The conjugation mixture was then capped and incubated in the dark at room temperature overnight. After overnight incubation, 1 uL of Quencher reagent was added for every 10 uL of antibody used and left to incubate for 30 min. At that point, antibody was divided into 20 uL aliquots to be used for replicate experiments and stored at −20°C.

#### Activity assay antibody staining and quartile sorting

Cells were plated in six-well plates at 500,000 cells per well with D10 medium with no doxycycline. All replicates were performed with 18–24 wells of cells total. After 24 hr, doxycycline was added to cells to induce expression of reporter and VKOR variant. Cells were then incubated with doxycycline for 48 hr. On day of cell sorting, each six well was washed with cold PBS, dissociated with 200 µL of versene, and then resuspended in 1 mL of phenol red-free DMEM + 1% FBS and transferred to a 5 mL FACS tube. Cells were spun at 300 x g, then washed once with 1 mL of phenol red-free DMEM + 1% FBS. Cells were spun at 300 x g, and after aspirating supernatant, cell pellet was resuspended in 100 uL of antibody diluted 1:100 in phenol red-free DMEM + 1% FBS. Cells were incubated in antibody for 20 min at 4°C in the dark, with vortexing at five minute intervals to ensure staining. After 20 min, 1 mL of staining buffer was added to each tube to dilute out antibody. Cells were spun at 300 x g, washed twice more similarly with staining buffer, then resuspended in 200 uL. At this point, all tubes were pooled and filtered to remove clumps. Cells were then sorted using a FACSAria III (BD Biosciences) into bins based on their APC intensity. First, live, single, recombinant cells were selected as described above. A histogram of APC was created and gates dividing the library into four equally populated bins based on APC fluorescence intensity were drawn. The details of replicate sorts for activity assay are in Supplementary file 2.

### Western blotting for abundance score validation

Nine variants that spanned the abundance score range were chosen to validate abundance scores. Cells were recombined using a selectable serine integrase landing pad (Matreyek et al., 2020) using the transfection method described above for abundance experiments. Recombinants were then selected with a small molecule, AP1903, at a concentration of 10 nM. Protein lysates were harvested from ~1 million cells using 100 µL NP40 lysis buffer with freshly prepared protease inhibitor cocktail. 15 µL of each protein lysate was loaded onto a 4–12% BisTris NuPage gel (Thermo Fisher) with MES buffer + 500 µl of antioxidant added to the inner chamber. The gel ran at 200V for 35 min. Gel was then transferred to nitrocellulose using 1X transfer buffer 10% MetOH at 24V for 1 hr on ice. The blot was washed for 5 min with 1X TBS three times. Blot was then blocked for one hour with 1X TBS-T + 5% milk and then washed for 5 min with 1X TBS-T 0.1% Tween three times. The blot was incubated with αVKOR 1:1000 and αcofilin 1:1000+ 1X TBS-T 0.1% Tween + 5% milk overnight at 4°C. The blot was washed for 5 min with 1X TBS-T 0.1% Tween three times. The blot was then incubated with 1:10,000 Goat anti-Mouse IgG (H+L) Highly Cross-Adsorbed Secondary Antibody, Alexa Fluor Plus 488 (ThermoFisher) and 1:10,000 Goat anti-Rabbit IgG (H+L) Cross-Adsorbed Secondary Antibody, Alexa Fluor 647 (ThermoFisher)+ 1X TBS-T 0.1% Tween + 5% milk for one hour. The blot was then washed for 5 min with 1X TBS-T 0.1% Tween three times. The blot was then imaged using the AlexaFluor488 and AlexaFluor647 fluorescent channels on the ChemiDoc MP (Biorad).

### gDNA prep, barcode amplification, and sequencing

Cells were then collected, pelleted by centrifugation and stored at −20 °C. Genomic DNA was prepared using a DNEasy kit, according to the manufacturer’s instructions (Qiagen), with the addition of a 30 min incubation at 37 °C with RNAse in the re-suspension step. Eight 50 μl first-round PCR reactions were each prepared with a final concentration of ~50 ng μl−one input genomic DNA, 1 × Q5 High-Fidelity Master Mix and 0.25 μM of the KAM499/VKORampR 1.1 primers. The reaction conditions were 98°C for 30 s, 98°C for 10 s, 65°C for 20 s, 72°C for 60 s, repeat five times, 72°C for 2 min, 4°C hold. Eight 50 μl reactions were combined, bound to AMPure XP (Beckman Coulter), cleaned and eluted with 21 μl water. Forty percent of the eluted volume was mixed with Q5 High-Fidelity Master Mix; VKOR_indexF_1.1 and one of the indexed reverse primers, PTEN_seq_R1a through PTEN_seq_R2a, were added at 0.25 μM each. These reactions were run with Sybr Green I on a BioRad MiniOpticon; reactions were denatured for 3 min at 95°C and cycled 20 times at 95°C for 15 s, 60°C for 15 s, 72°C for 15 s with a final 3 min extension at 72°C. The indexed amplicons were mixed based in relative fluorescence units and run on a 1% agarose gel with Sybr Safe and gel extracted using a freeze and squeeze column (Bio-Rad). The product was quantified using Kapa Illumina Quant kit.

### Subassembly

Barcoded VKOR library was subassembled using a MiSeq 600 kit (Illumina). Two amplicons were generated, one forward, one reverse. PCR reactions were each prepared with ~500 ng input plasmid DNA, 1 × KAPA High-Fidelity Master Mix and 0.25 μM of the VKOR_SA_amp_F/VKOR_SA_amp_R or VKOR_SA_for_amp_R2.0/VKOR_SA_rev_amp_F2.0 primers. PCR reactions were run at 95°C for five minutes, then cycled 15 times at 98°C for 0:20, 60°C for 0:15, 72°C for 0:30, with a final extension at 72°C for 2:00. Amplicons (741 bp) were gel extracted on a 1.0% gel run at 130V for 35 mins. The product was quantified using Qubit and Kapa Illumina quant kit. Read lengths were as follows: 289 bp forward read, 18 bp index1, 18 bp index 2 (index = barcode forward and reverse). All reads sharing a common barcode sequence were collapsed to form the consensus variant sequence, resulting in 175,052 barcodes after filtering.

### Barcode counting and variant calling

Enrich2 was used to quantify barcodes from bin sequencing, using a minimum quality filter of 20 (Rubin et al., 2017). FASTQ files containing barcodes and the barcode map for VKOR were used as input for Enrich2. Enrich2 configuration files for each experiment are available on the GitHub repository. Barcodes assigned to variants containing insertion, deletions, or multiple amino-acid alterations were removed from the analysis.

### Calculating scores and classifications

Scores and classifications were assigned using previously published analysis pipeline (Matreyek et al., 2018). Briefly, for each protein variant, frequencies in each bin were calculated by dividing counts by total counts. From there, we filtered variants based on the number of experiments in which it was observed (Fexpt = 2) and their frequency (Ffreq = 10−4), after noticing that low frequency variants introduced noise to the analysis. These frequencies were then each weighted by multiplying by 0.25, 0.5, 0.75, and one in a bin-wise fashion. We generated a replicate score for each variant by using min-max normalization: normalizing to the median weighted average of the nonsense distribution set at 0 and the median weighted average of the synonymous distribution set at 1. We then averaged those scores for a final, experiment-wide variant score. Standard deviation and standard error were also calculated for each variant, and 95% confidence intervals were estimated using standard error, assuming a normal distribution. Abundance and activity classifications were assigned by assessing variant score and confidence intervals in relation to synonymous variant distribution. To do this, we established a cut-off that separated the 5% of synonymous variants with the lowest abundance (or activity) scores from the 95% of synonymous variants with higher abundance (or activity) scores. Variants with both scores and upper confidence intervals below this threshold were classified as ‘low,’ while those with scores below but upper confidence above were classified as ‘possibly low.’ Variants with scores and lower confidence intervals above the threshold were classified as ‘WT-like’, while those with scores above lower confidence intervals below the threshold were classified as ‘possibly WT-like.’ Finally, another threshold was set that separated the 5% of synonymous variants with the highest scores from the rest of the synonymous distribution. Variants that had scores above this threshold, with lower confidence intervals above the lower threshold were classified as ‘high'.

### Windowed abundance and activity analysis

Windowed averages of abundance and activity scores were calculated using a window length of 10 positions with center alignment. Scores were calculated for both charged amino acids (R, K, H, D, E,) and aliphatic amino acids (G, A, V, I, L).

### Evolutionary couplings analysis

EVcouplings extracts the constraints between pairs of residues, as evidenced in alignments of homologous sequences: first homologous sequences must be collected and aligned, and then a model of statistical energy costs and benefits between residues is fit to explain the sequence variation in the alignment. We collected an alignment of 2770 sequences using jackhammer (http://hmmer.org/) to query the human VKOR sequence against UniRef100 (https://www.uniprot.org/uniref/), with a bitscore per residue cutoffs of 0.4 and 7 search iterations. We predicted secondary structures where the summed strength of couplings at would-be alpha helix and beta strand contacts scored above 1.5 for alpha helices and 0.75 respectively, for two or more consecutive residues. We extended the called helices and strands by one residue on each side for a minimum structure size of four residues. All methods used for building alignments, training the model, folding, and predicting secondary structure are part of the EVcouplings software (https://evcouplings.org/) (Hopf et al., 2019).

### Homology modeling

A homology model of human VKOR was made by accessing I-TASSER (Yang et al., 2015) and using PDB structure 4NV5 as a template for threading. Model1 from results was used for all figures in this paper.

### Hierarchical clustering

Hierarchical clustering was performed on abundance score vectors for each position using the hclust function in R. Dendrogram for hierarchically clustered heatmap was drawn using dendextend package (version 1.12.0).

### Active site residue analysis

Activity and abundance scores were rescaled so that the lowest score present in the dataset was set at 0, and the highest score at 1. A ratio of rescaled activity to rescaled abundance (specific activity) was then calculated for every variant. Using variant specific activity scores, median specific activity was calculated for each position. Threshold for classification as an active site position was drawn based on scores of known redox cysteines at positions 132 and 135, resulting in lowest 12.5% of median specific activity scores being classified as active site residues. We additionally required that any position within this group had been scored for at least four variants to eliminate noise from poor sampling.

### Code availability

Code for analysis is available at http://github.com/FowlerLab/VKOR (Chiasson, 2020a; copy archived at https://github.com/elifesciences-publications/VKOR).

The code used to train the evolutionary couplings model is available at the EVcouplings GitHub repository (Chiasson, 2020b; https://github.com/debbiemarkslab/EVcouplings; copy archived at https://github.com/elifesciences-publications/EVcouplings). The data used to train the model is publically available at uniprot (https://uniprot.org).
