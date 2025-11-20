# Removal of developmentally regulated microexons has a minimal impact on larval zebrafish brain morphology and function

## Authors

- Caleb CS Calhoun<sup>1</sup>
- Mary ES Capps<sup>1</sup>
- Kristie Muya<sup>1</sup>
- William C Gannaway<sup>1</sup>
- Verdion Martina<sup>1</sup>
- Claire L Conklin<sup>1</sup>
- Morgan C Klein<sup>1</sup>
- Jhodi M Webster<sup>1</sup>
- Emma G Torija-Olson<sup>1</sup> ([ORCID: 0000-0001-5003-7395](https://orcid.org/0000-0001-5003-7395))
- Summer B Thyme<sup>1</sup> ([ORCID: 0000-0003-3593-4148](https://orcid.org/0000-0003-3593-4148)) †

### Affiliations

1. Department of Neurobiology, The University of Alabama at Birmingham Heersink School of Medicine Birmingham United States ([ROR:008s83205](https://ror.org/008s83205))

† Corresponding author

## Abstract

Microexon splicing is a vertebrate-conserved process through which small, often in-frame, exons are differentially included during brain development and across neuron types. Although the protein sequences encoded by these exons are highly conserved and can mediate interactions, the neurobiological functions of only a small number have been characterized. To establish a more generalized understanding of their roles in brain development, we used CRISPR/Cas9 to remove 45 microexons in zebrafish and assessed larval brain activity, morphology, and behavior. Most mutants had minimal or no phenotypes at this developmental stage. Among previously studied microexons, we uncovered baseline and stimulus-driven phenotypes for two microexons (meA and meB) in ptprd and reduced activity in the telencephalon in the tenm3 B0 isoform. Although mild neural phenotypes were discovered for several microexons that have not been previously characterized, including in ppp6r3, sptan1, dop1a, rapgef2, dctn4, vti1a, and meaf6. This study establishes a general approach for investigating conserved alternative splicing events and prioritizes microexons for downstream analysis.

## Introduction

Alternative splicing greatly expands proteome diversity and can impact brain development and disease (Vuong et al., 2016). As most metazoan proteins are represented by multiple isoforms, defining the functional significance of individual splicing events is a vast challenge. Mouse studies do not have the throughput to assess the neural role of 10 or 100 s of isoforms, and cell culture does not recapitulate the complex development of an animal brain.

One class of particularly conserved and developmentally regulated spliced exons is microexons or mini-exons. These small exons, defined here as 3–30 nucleotides or 1–10 amino acids in length, are either gained or lost in transcripts in the brain compared to other tissues. While most are in-frame, this pathway can also trigger nonsense-mediated decay to influence protein levels (Lin et al., 2020). Although these neuron-specific exons were recognized almost 40 years ago (Brugge et al., 1985; Martinez et al., 1987), their discovery and annotation have continued into recent years (Parada et al., 2021). Thus far, hundreds have been identified. Although more than one splicing regulator has been implicated in the alternative inclusion of microexons in neurons (Ciampi et al., 2022; Li et al., 2015a), many are controlled by the vertebrate-specific protein SRRM4 (Irimia et al., 2014; Quesnel-Vallières et al., 2015). Srrm4 interacts with Srsf11 and Rnps1 at polypyrimidine sequences upstream of microexons to regulate their inclusion (Gonatopoulos-Pournatzis et al., 2020).

Proteins that regulate and contain microexons are involved in neurodevelopmental disorders. In the brains of individuals with autism spectrum disorder (ASD), the level of SRRM4 is reduced, leading to the misregulated splicing of multiple microexons (Irimia et al., 2014). Mice haploinsufficient for Srrm4 display reduced social interaction, sensory hypersensitivity, and impaired synaptic transmission (Quesnel-Vallières et al., 2015). Furthermore, Srrm4 is involved in regulating the ASD-relevant KCC2-dependent GABAergic excitatory to inhibitory switch (Nakano et al., 2019), and a mouse model of ASD with disrupted Pten has decreased Srrm4 expression and microexon inclusion (Thacker et al., 2020). Loss-of-function variants in its interacting partner SRSF11 have been implicated in ASD in humans (Yuen et al., 2017). While the behavioral roles of only a few microexons have been studied in detail (Gonatopoulos-Pournatzis and Blencowe, 2020), the elimination of one from Eif4g1 altered synaptic plasticity and social behavior in mice (Gonatopoulos-Pournatzis et al., 2020). Many genes containing microexons also lead to neurodevelopmental disorders when mutated in humans. Examples include CASK-mediated microcephaly and cerebellar hypoplasia, SPTAN1-mediated childhood-onset epilepsy, and MAPK8IP3-mediated intellectual disability (Giacomini et al., 2021; Platzer et al., 2019; Syrbe et al., 2017). Taken together, this splicing program, the genes with microexons, and microexons themselves are important to enable proper neural development.

Although most microexons are unstudied, detailed structural and functional characterization of a small subset has revealed involvement in synapse development. The most well studied are found in the receptor-type tyrosine phosphatase (e.g., ptprf) and teneurin (e.g., tenm4) gene families. Recognized in the 1990s (O’Grady et al., 1994; Pulido et al., 1995), two microexons in presynaptic PTPδ (Ptprd), PTPσ (Ptprs), and LAR (Ptprf) modulate trans-synaptic interfaces and determine selective interaction with postsynaptic partners (Lin et al., 2018; Li et al., 2015b; Park et al., 2020; Um et al., 2014; Yamagata et al., 2015; Yim et al., 2013). Similarly, differential inclusion of two conserved microexons in teneurins can modulate trans-synaptic homophilic or heterophilic interactions through splicing-dependent, large conformational changes (Berns et al., 2018; Gogou et al., 2024; Li et al., 2020). While studying these cell adhesion molecules has highlighted how microexons can trigger differential protein–protein interactions, little is known about the developmental consequences of these biochemical switches in other protein classes.

Identifying the neurobiological roles of many individual microexons is a challenge. Studies of splicing regulators such as srrm4 impact the entire splicing program, making it impossible to determine the importance of individual microexons to protein function. Furthermore, microexons could still be differentially included in a srrm4 regulatory mutant via compensation by other splicing factors, such as its paralogue srrm3, which is responsible for microexon inclusion in photoreceptor transcripts in zebrafish (Ciampi et al., 2022). A vertebrate model is necessary for these studies; although there is a similar splicing mechanism in Drosophila melanogaster, there is no overlap of the individual microexons (Torres-Méndez et al., 2021). Thus, we used larval zebrafish, a vertebrate that supports more high-throughput studies than mammalian models (Thyme et al., 2019), to assess the brain activity, brain structure, and behavior of zebrafish larvae mutant for 45 microexons (Figure 1A).

![Figure 1.](https://cdn.elifesciences.org/articles/101790/elife-101790-fig1-v1.jpg)

**Figure 1.:** (A) Pipeline of the screen. Mutant lines with alternatively spliced microexons removed were generated with CRISPR/Cas9, crossed together, and sibling larvae were assessed for changes to brain morphology, brain activity, and behavioral profiling. (B) The amino acid sequence identity of 95 zebrafish microexons compared to mouse. (C) The amino acid sequence identity of 95 zebrafish microexons compared to mouse and divided by the sequence identity of the entire protein. (D) Gene Ontology analysis of biological processes associated with the 95 mouse microexons that are conserved in zebrafish. The analysis was completed using the PANTHER classification system. (E) Quantification of reverse transcription PCR (RT-PCR) for microexon-containing regions over zebrafish development. These data were clustered using the default seaborn clustermap settings (method = ‘average’). Panels A and E were created in BioRender.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/101790/elife-101790-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** Diagrams were generated with DNA Features Viewer (https://edinburgh-genome-foundry.github.io/DnaFeaturesViewer/). The first and third columns show the microexons and neighboring exons, with a unique scale bar included for each mutant. The second and fourth columns show the zoomed area around each microexon with the start position for putative regulatory elements and gRNA sites. When the microexon neighbored either the first or last exon, the UTR is included in the labeled exon (e.g., csnk1g1 and synj1-1). When determining possible UC-repeat elements, a distance of 100 base pairs from the microexon was considered, although <50 base pairs is canonical. The label for the UC repeat represents the beginning of possible repeat sequences and not the span; thus, there may be closer elements.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/101790/elife-101790-fig1-figsupp2-v1.jpg)

**Figure 1—figure supplement 2.:** (A) Reverse transcription PCR (RT-PCR) validations of microexon removal at 6 dpf for wild-type (+/+), heterozygous (+/−), and homozygous (−/−) siblings. The expected length of the product with and without the microexon is shown above each sample, and the ladder is shown on the left side. The upper band in the vav2 wild-type and heterozygous samples is a heterodimer of the two products, an outcome we often see when genotyping smaller deletions. (B) Quantification of the gels in panel A. (C) Nanopore sequencing (Plasmidsaurus) of the heterozygous nrxn1a sample with corresponding read counts (right). The second read (R2) represents the intermediate band on the nrxn1a gel above. This sequence corresponds to an extension of the upstream exon (gray), indicating that there are two isoforms of nrxn1a in addition to the developmentally regulated inclusion of the microexon. (D) Nanopore sequencing (Plasmidsaurus) of the heterozygous vav2 sample with corresponding read counts. The R2 sequencing missing the microexon was additionally confirmed with Sanger sequencing of the homozygous sample. (E) qRT-PCR for selected microexon lines. The expression of each gene was normalized to rpl13a. Statistical significance was calculated with the Brown–Forsythe and Welch ANOVA corrected for multiple comparisons.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/101790/elife-101790-fig1-figsupp3-v1.jpg)

**Figure 1—figure supplement 3.:** (A) Developmental phenotypes observed in homozygous larvae for three genes with truncating mutations. Chi-square analysis p < 0.01 from 12/12 animals with and without a phenotype. Additionally, healthy homozygous animals were never recovered from multiple heterozygous incrosses assessed at 4–6 dpf. (B) Brain activity maps for heterozygous incrosses. The comparisons are shown above the sum-of-slices intensity projection with a 6 dpf brain outline, where the genotype before the | is being compared to the one after. All N are in Supplementary file 2. (C) Brain structure maps for heterozygous incrosses. All N are in Supplementary file 2. (D) Brain activity maps for heterozygous outcrosses for those mutants with lethal developmental phenotypes that prohibit homozygous imaging. The comparisons are shown above the sum-of-slices intensity projection with a 6 dpf brain outline, where the genotype before the | is being compared to the one after. All N are in Supplementary file 2. (E) Brain structure maps for heterozygous outcrosses for those mutants with lethal developmental phenotypes that prohibit homozygous imaging. The comparisons are shown above the sum-of-slices intensity projection with a 6 dpf brain outline, where the genotype before the | is being compared to the one after. All N are in Supplementary file 2.

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/101790/elife-101790-fig1-figsupp4-v1.jpg)

**Figure 1—figure supplement 4.:** (A) Baseline and stimulus-driven behavior dot plots for heterozygous incrosses. Dot size corresponds to the percent of significant assays in the category (e.g., Magnitude). Replicate experiments using different parental pairs are shown side-by-side. All N are in Supplementary file 2. (B) Baseline and stimulus-driven behavior dot plots for heterozygous outcrosses. Dot size corresponds to the percent of significant assays in the category (e.g., Magnitude). (C) The caska truncating mutant has repeatable phenotypes in motion frequency and dark flash response. Example frequency of motion plot for caska mutants. The nighttime movement frequency is increased. The wild-type siblings (black) are compared to the homozygous (red). (D) Graph demonstrating the reduced dark flash responsivity of caska mutants. The latency is increased in this line (see panel H), which can be visualized by this response plot. (E) Increased daytime movement frequency and increased dark flash response frequency in ckap5 heterozygous mutants (red) compared to wild-type siblings (black). This phenotype represents the strongest behavioral outcome for heterozygous compared to wild-type. (F) The ppp6r3sa16892 has an increased response to acoustic stimuli. These three plots are response traces (shown from left to right) induced by strong taps that occur after tap habituation block 2 (day5dpfhab2post), after tap habituation block 3 (day5dpfhab3post), and during the night (a0f1000d5pD300a1f1000d5p).

## Results

A recently developed computational tool identified microexons that are differentially spliced during mouse brain development and conserved in zebrafish (Parada et al., 2021). Based on the intersection of these two sets, 95 microexons fulfilled both parameters (Supplementary file 1). Of these 95 microexons, 42 exist in a canonical layout in the zebrafish genome, with both a UGC and UC repeat – or similar polypyrimidine tract – directly upstream of the alternatively spliced exon (Gonatopoulos-Pournatzis et al., 2018; Supplementary file 1, Figure 1—figure supplement 1), indicating that Srrm4 likely controls their inclusion. Of the remaining microexons, 44 are organized similarly to the canonical layout, typically with either a UGC or UC repeat. Thus, they may also be regulated by Srrm4. The protein sequences of the 95 microexons are highly conserved between mouse and zebrafish (Figure 1B), more so than the full-length protein sequences (Figure 1C). The genes containing microexons are enriched for those involved in neuronal development as well as the cytoskeleton (Figure 1D). The majority of these microexons are included in transcripts as the brain develops, rather than lost, in both mouse and zebrafish (Figure 1E), making CRISPR/Cas9 removal of the microexon an ideal approach for studying the function of the added amino acids.

Using CRISPR/Cas9, we generated lines that removed 45 conserved microexons (Supplementary file 2) and assayed larval brain activity, brain structure, and behavior (Figure 1A). Four guide RNAs were used, two on each side of the microexon (Supplementary file 2, Figure 1—figure supplement 1). For microexons with upstream regulatory elements that are likely important for splicing, these elements were also removed (Figure 1—figure supplement 1). While we were most interested in those microexons only present after 24 hr post-fertilization (Figure 1E), as this is when the brain is forming, we also removed microexons from several genes with an earlier expression of the isoform. For eight mutant lines, we confirmed that the microexon was eliminated from the transcripts as expected (Figure 1—figure supplement 2). Although our genomic deletion did not yield unexpected isoforms, qRT-PCR on these eight lines revealed significant downregulation for the homozygous vav2 mutant (Figure 1—figure supplement 2), indicating possibly complex genetic regulation. Protein-truncating mutations in eleven additional genes that contain microexons revealed developmental and neural phenotypes in zebrafish (Figure 1—figure supplement 3, Figure 1—figure supplement 4), indicating that the genes themselves are involved in biologically relevant pathways. Three of these genes – tenm4, sptan1, and ppp6r3 – are also in our microexon line collection.

To uncover neural phenotypes, we assessed baseline and stimulus-driven movement. Homozygous mutant and control sibling larvae were subjected to a behavioral pipeline in 96-well plates from 4 to 7 days post-fertilization (dpf) (Figure 2A). Only a small number of strong, repeatable phenotypes were observed either at baseline or in response to acoustic or visual stimuli (Figure 2B, C, Figure 2—figure supplement 1, Figure 2—figure supplement 2, Figure 2—figure supplement 3). Baseline behavioral differences were observed in multiple movement categories. For example, rapgef2 mutants showed an increased movement frequency (Figure 2B, D) but no changes to the characteristics of these movements (magnitude) or location in the well. In contrast, dop1a mutants had reduced daytime movement and an increased well-edge preference specifically at night (Figure 2—figure supplement 2, Figure 2—figure supplement 4, Figure 2B, D). Other baseline movement phenotypes included a well-center preference for vav2 mutants, a decreased movement magnitude for ptprd-2 (also referred to in the literature as meA) mutants (Figure 2—figure supplement 4), and an increased movement magnitude for ptprd-1 (also referred to in the literature as meB) mutants (Figure 2D). Dark flash response phenotypes included a reduced latency for eif4g3b mutants and a reduced response frequency for ptprd-1 (meB) and dop1a mutants (Figure 2C, D, Figure 2—figure supplement 4). Acoustic response phenotypes included an increased frequency of response to strong stimuli for ppp6r3 mutants and a reduced frequency of response to strong acoustic stimuli for ptprd-2.

![Figure 2.](https://cdn.elifesciences.org/articles/101790/elife-101790-fig2-v1.jpg)

**Figure 2.:** (A) Summary of behavioral pipeline. (B) Baseline behavioral phenotypes for microexon mutants. The labels ‘1’ and ‘2’ indicate biological replicates. The data shown is for homozygous mutant larvae compared to wild-type siblings. Comparisons to the heterozygous larvae are removed for clarity and available in the Supplementary Materials, as they often have even milder phenotypes than homozygous. The size of the bubble represents the percent of significant measurements in the summarized category, and the color represents the mean of the strictly standardized mean difference (SSMD) of the significant assays in that category. (C) Stimulus-driven behavioral phenotypes for microexon mutants. The labels ‘1’ and ‘2’ indicate biological replicates. The bubble size and color are calculated the same as in panel B. (D) Examples of behavioral phenotypes. The black boxes in panels B and C correspond to the selected plots. Wild-type siblings (black) are compared to the homozygous (red), and the plots show mean ± SEM. All N are in Supplementary file 2. Kruskal–Wallis ANOVA p-values for the selected plots are as follows: dop1a center preference during the first night (day0night_boutcenterfraction_3600) = 0.00006/0.0008, N +/+ = 15 (run 1) and 14 (run 2), N −/− = 17 (run 1) and 15 (run 2); eif4g3b p-values are not calculated for response traces (shown is all dark flashes in block 1), p-values for the latency for the first 10 dark flashes in block 1 (day6dpfdf1a_responselatency) = 0.026/0.0008, N +/+ = 16 (run 1) and 15 (run 2), N −/− = 15 (run 1) and 21 (run 2); ppp6r3 frequency of response to strong acoustic stimuli with a sound frequency of 1000 Hz that precede the habituation block (day5dpfhab1pre_responsefrequency_1_a1f1000d5p) = 0.002/0.016, N +/+ = 19 (run 1) and 20 (run 2), N −/− = 21 (run 1) and 29 (run 2); ptprd-1 pixels moved in each bout for the duration of the experiment (combo_boutcumulativemovement_3600) = 0.001/0.00002, N +/+ = 22 (run 1) and 21 (run 2), N −/− = 26 (run 1) and 18 (run 2); rapgef2 number of bouts for the duration of the experiment calculated using the delta pixel data in each frame (dpix_numberofbouts_3600) = 0.002/0.001, N +/+ = 21 (run 1) and 23 (run 2), N −/− = 21 (run 1) and 20 (run 2).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/101790/elife-101790-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** Baseline behavior dot plots for all sibling comparisons. Dot size corresponds to the percent of significant assays in the category (e.g., Magnitude). Replicate experiments using different parental pairs are shown side-by-side. All N are in Supplementary file 2.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/101790/elife-101790-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** Frequency of motion measured as number of bouts/hour over the entire duration of the experiment. The biological replicates are shown side-by-side. All N are in Supplementary file 2. The wild-type siblings (black) are compared to the homozygous (red).

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/101790/elife-101790-fig2-figsupp3-v1.jpg)

**Figure 2—figure supplement 3.:** Stimulus-driven behavior dot plots for all sibling comparisons from a heterozygous parental in-cross.

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/101790/elife-101790-fig2-figsupp4-v1.jpg)

**Figure 2—figure supplement 4.:** All N are in Supplementary file 2. (A) Frequency phenotype of dop1a mutants. Shown is the day3msdf_dpix_numberofbouts_60 graph for run 1/run 2. p-values: 0.033/0.038 (linear mixed model) and 0.036/0.11 (Kruskal–Wallis ANOVA, which performs poorly on data with a large range). (B) Reduced dark flash response frequency phenotype of dop1a mutants. Shown is the response frequency for dark flash block 3 (day6dpfdf3_responsefrequency). p-values: 0.047/0.036 (Kruskal–Wallis ANOVA). (C) Reduced dark flash response of nrg2b mutants. p-values are not calculated for response graphs. (D) Reduced dark flash response frequency phenotype of ptprd-1 mutants. Shown is the response frequency for dark flashes from all three blocks (day6dpfdfall_responsefrequency). p-values: 0.0056/0.0018 (Kruskal–Wallis ANOVA). (E) Reduced nighttime sleep bout frequency phenotype of ptprd-1 mutants. Shown is the plot for the entire 3-night/day experiment (combo plot). p-values: 0.001/0.013 (linear mixed model). The same measure from a subsection of the data, the entire second night (day2nightall_dpix_numberofboutsSLEEP, not shown), has Kruskal–Wallis ANOVA p-values of 0.001/0.003. (F) Altered number of bouts frequency phenotype of ptprd-1 mutants. Shown is the entire 3-night/day experiment (combo plot). p-values are not significant for the entire duration, but a subsection (day1morn_dpix_numberofbouts_60, not shown) has Kruskal–Wallis ANOVA p-values of 0.003/0.012. (G) Reduced daytime bout total pixels magnitude (dpix_boutcumulativemovement) phenotype of ptprd-2 mutants. Shown is the entire 3-night/day experiment (combo plot). p-values are not significant for this duration. The same measure from a subsection of the data, the evening of day 1 of the experiment (day1evening_dpix_boutcumulativemovement, not shown), has Kruskal–Wallis ANOVA p-values of 0.002/0.019. (H) Increased sleep bout (stronger in daytime) frequency phenotype of ptprd-2 mutants. Shown is the entire 3-night/day experiment (combo plot). p-values: 0.001/0.013 (Kruskal–Wallis ANOVA). The same measure from a subsection of the data, the entire second night (day2nightall_dpix_numberofboutsSLEEP_60, not shown), has Kruskal–Wallis ANOVA p-values of 0.001/0.01. (I) Reduced number of bouts (stronger in daytime) frequency phenotype of ptprd-2 mutants. Shown is the entire 3-night/day experiment (combo plot). p-values: 0.001/0.04 (linear mixed model) and 0.003/0.08 (Kruskal–Wallis ANOVA). (J) Reduced acoustic response frequency phenotype of ptprd-2 mutants. Shown are the escape responses for the strong stimuli occurring following acoustic habituation (habituation_day5dpfhab1post_responsefrequency). The responses are filtered for those that are true escapes, and the phenotype emerges for only the true, short-latency C-bends. p-value: 0.03/0.006 (Kruskal–Wallis ANOVA). (K) Reduced strong acoustic responses of ptprd-2 mutants. This response plot goes along with the frequency data, but this plot is not filtered for only the true C-bends. p-values are not calculated for response graphs. (L) Increased daytime location center preference for vav2 mutants. Shown is the evening of the second day (day2evening_boutcenterfraction), but multiple subsections show significant increase in center dwelling preference. p-value: 0.006/0.013 (Kruskal–Wallis ANOVA).

To detect changes to brain development and function, we collected phospho-Erk (pErk) brain activity maps under unstimulated conditions at 6 dpf. Large morphological differences were identified using the Jacobian matrix derived from the image registration process (Jefferis et al., 2007; Rohlfing and Maurer, 2003). Similar to the behavioral findings, few phenotypes were observed in brain activity (Figure 3, Figure 3—figure supplement 1A, Figure 3—figure supplement 2) or brain structure (Figure 3B, Figure 3—figure supplement 3, Figure 3—figure supplement 4) in homozygous mutants compared to wild-type control siblings when quantified by region (Figure 3C). Repeatable phenotypes were mild (Figure 3D) compared to a mutant with a moderate phenotype and both increased and decreased activity and structure (see control-tcf7l2) (Capps et al., 2024). Only one mutant, ppp6r3, displayed substantial and repeatable differences in brain morphology (Figure 3B, E), with reduced size observed mainly in the thalamus and neighboring pretectum. While the loss of both copies of microexons was required for most phenotypes, brain activity differences were observed in vti1a and sptan1 heterozygotes (Figure 3F) as well as vav2 and mapk8ip3 (Figure 3—figure supplement 1, Figure 3—figure supplement 2). While repeatable phenotypes in brain activity and structure were observed in a small subset of mutants, other zebrafish studies using identical methods have typically uncovered brain activity phenotypes for approximately half of the lines that are stronger than any we observed (Figure 3G; Capps et al., 2024; Thyme et al., 2019; Weinschutz Mendes et al., 2023).

![Figure 3.](https://cdn.elifesciences.org/articles/101790/elife-101790-fig3-v1.jpg)

**Figure 3.:** (A) Clustered summary of pErk comparisons between homozygous mutants and wild-type control siblings, where magenta represents decreased activity and green represents increased. The signal in each region was summed and divided by the region size. The N for all experiments is available in Supplementary file 2. (B) Clustered summary of structure comparisons between homozygous mutants and wild-type control siblings, where magenta represents decreased size and green represents increased. (C) Location of major regions in the zebrafish brain based on masks from the Z-Brain atlas (Randlett et al., 2015). (D) Brain imaging for microexon mutants with repeatable brain activity phenotypes. The brain images represent the significant signal difference between homozygous and wild-type control siblings. They are shown as sum-of-slices projections (Z- and X-axes) with the white outline representing the zebrafish brain. (E) Structural phenotype of the ppp6r3 mutant, with replicates shown side-by-side. The magenta indicates decreased size. (F) Brain imaging for two microexon mutants with brain activity phenotypes that are similar for both the heterozygous and homozygous mutants. (G) Comparison of the total brain activity signal between homozygous microexon mutants from this work and mutants for autism risk genes from Capps et al., 2024. Both increased and decreased activity are considered a single comparison rather than the average of the repeats.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/101790/elife-101790-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** The comparisons are shown above the sum-of-slices intensity projection with a 6 dpf brain outline, where the genotype before the | is being compared to the one after. All N are in Supplementary file 2.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/101790/elife-101790-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** The comparisons are shown above the sum-of-slices intensity projection with a 6 dpf brain outline, where the genotype before the | is being compared to the one after. All N are in Supplementary file 2.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/101790/elife-101790-fig3-figsupp3-v1.jpg)

**Figure 3—figure supplement 3.:** The comparisons are shown above the sum-of-slices intensity projection with a 6 dpf brain outline, where the genotype before the | is being compared to the one after. All N are in Supplementary file 2.

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/101790/elife-101790-fig3-figsupp4-v1.jpg)

**Figure 3—figure supplement 4.:** The comparisons are shown above the sum-of-slices intensity projection with a 6 dpf brain outline, where the genotype before the | is being compared to the one after. All N are in Supplementary file 2.

## Discussion

Our study provides a broad overview of the larval zebrafish neural phenotypes resulting from removing developmentally regulated microexons. Here, we leveraged our previously successful brain activity mapping and behavioral profiling strategy, which has high sensitivity and has uncovered phenotypes for dozens of mutants (Thyme et al., 2019). While only a few zebrafish lines had neural phenotypes, most of the microexons with behavioral or brain activity differences were previously unstudied and found in diverse protein classes.

The small number of observed phenotypes was unexpected based on conservation of the microexons (Figure 1B, C) and the discovery rates of previous screens using similar methods (Capps et al., 2024; Thyme et al., 2019; Weinschutz Mendes et al., 2023). Although most of these studies focused on protein-truncating alleles, we have found phenotypes in lines with missense mutations (Capps et al., 2024). However, this outcome is consistent with a recent, similar study of microexons in zebrafish (Lopez-Blanch et al., 2024). Although only three of the 18 microexons this group studied are in the same genes as our set (ap1g1, vav2, and vti1a), the phenotypes for individual mutants are similar, and this work shares the same overall finding of minimal phenotypes in zebrafish larvae. Importantly, the pErk brain activity mapping method we used is highly sensitive, significantly minimizing the likelihood that substantial zebrafish larval phenotypes from individual microexon removal are being missed. In our published work (Capps et al., 2024; Thyme et al., 2019), we showed that brain activity can be drastically impacted without manifesting in differences in those behaviors assessed in a typical larval screen such as was completed by Lopez-Blanch et al. Furthermore, the genes that contain microexons are developmentally important (Figure 1—figure supplement 3, Figure 1—figure supplement 4). For instance, the caska loss-of-function mutant displayed substantial changes to brain activity, a smaller brain size, and multiple behavioral phenotypes. Loss-of-function mutants for sptan1 and ppp6r3 are stronger than lines that only remove the microexon (Figure 1—figure supplement 3, Figure 1—figure supplement 4).

The limited effects of individual microexon deletions suggest that stronger phenotypes may require disrupting multiple microexons or examining later stages of development. It is possible that perturbation of multiple microexons simultaneously, as was observed in the brains of autistic individuals (Irimia et al., 2014), is necessary to produce pronounced effects on early neurodevelopment. Zebrafish homozygous for srrm4 deletion did not display any overt developmental phenotypes (Ciampi et al., 2022), in contrast to a previous morpholino study (Calarco et al., 2009). More recently, it was revealed that loss of srrm4 has minimal impacts on behavior (Lopez-Blanch et al., 2024) and brain structure (Gupta et al., 2025), while srrm3 mutants have significant neural phenotypes and early mortality (Ciampi et al., 2022; Lopez-Blanch et al., 2024). This finding indicates that Srrm3 loss is necessary for complete elimination of these microexons, but studying microexons in the context of this line is also complicated by possible downstream consequences of severe vision loss. Alternatively, although the microexons are present at larval stages, they may only become important during later stages of neuronal maturation that support more complex behaviors. Mouse models were studied as adults and for disruptions to social interaction, learning, and memory (Gonatopoulos-Pournatzis et al., 2020; Han et al., 2024), which larvae are not yet capable of Dreosti et al., 2015; Valente et al., 2012.

Our study extends on findings for previously studied genes containing microexons. We discovered increased brain activity (Figure 3D) and an altered dark flash response in mutants for the eif4g3b (Figure 2D), whereas a mouse model with the microexon removed was described as having no behavior phenotypes (Gonatopoulos-Pournatzis et al., 2020). That study, however, focused on social behavior, learning, and memory and may not have included stimuli analogous to dark flashes. Alternatively, microexon removal in zebrafish could have differential behavioral impacts than in rodents. Mice mutant for the ptprd-2 (meA) microexon have increased movement and interrupted sleep (Park et al., 2020). Both zebrafish mutants in ptprd demonstrate the opposite, with reduced daytime movement and increased sleep during the day for ptprd-2 (Figure 2—figure supplement 4). While the underlying disrupted circuitry could differ between the species, the daytime sleep increase raises the possibility of a rebound response to undetected nighttime sleep disruptions. In other cases, the gene that contains the microexon has been extensively studied, but research on the microexon itself is absent. For example, the function of SNARE protein Vti1a in neural development and dense core vesicle biogenesis has been studied in great depth (Bollmann et al., 2022; Emperador-Melero et al., 2018; 
Kunwar et al., 2011; 
Sokpor et al., 2021; Walter et al., 2014). Its brain-specific microexon, however, was recognized over 20 years ago (Antonin et al., 2000), and its specific importance has been largely ignored. We discovered reduced brain activity mainly in the telencephalon in both homozygous and heterozygous lines compared to wild-type siblings (Figure 3F), highlighting the relevance of considering multiple conserved isoforms when characterizing protein function in the brain.

Mutants for unstudied microexons with the strongest phenotypes come from diverse protein classes (Gonatopoulos-Pournatzis and Blencowe, 2020), indicating this splicing program impacts neurodevelopmental processes beyond trans-synaptic partner selection. The only mutant with a substantial brain size difference was ppp6r3, which encodes a regulator of protein phosphatase 6 (PP6), and this reduced size was present and more severe in the predicted protein-truncating ppp6r3sa16892 line (Figure 1—figure supplement 3). Although little is known about this protein, it has been linked to cell cycle (Heo et al., 2020) and cell death (Wu et al., 2022), nominating hypotheses for determining future research on the source of the reduced size. Dctn4 is part of the dynactin complex, Mapk8ip3 is involved in Kinesin-1-Dependent axonal trafficking (Platzer et al., 2019; Watt et al., 2015), and Sptan1 is a cytoskeleton scaffold protein (Huang et al., 2017). The number of microexon-containing genes related to the cytoskeleton (Figure 1D) and also trafficking (e.g., vti1a) suggests that microexons may be important to the specialized cytoskeletal needs of developing neurons. The functions of microexons in cytoskeletal proteins are beginning to be discovered (Poliński et al., 2023). Transcriptional regulation is represented by the meaf6 mutant, while Rapgef2, which has the strongest behavioral phenotypes upon microexon removal (Figure 3D), is a signaling protein.

Although our list is not comprehensive, as many microexons remain unstudied, we have prioritized several microexons for future study from the 45 tested. For seven mutants, we confirmed that the microexon was cleanly removed without unanticipated effects on isoforms or transcript levels (Figure 1—figure supplement 2), including for some of the most interesting that are entirely unstudied (ppp6r3, sptan1, meaf6). For those with phenotypes that are not yet confirmed by qRT-PCR (rapgef2, dctn4, dop1a, mapk8ip3), studies of gene loss-of-function in zebrafish and mice reveal far stronger phenotypes and lethality, suggesting that our lines impact only the microexon (Abeler-Dörner et al., 2020; 

Drerup and Nechiporuk, 2013; 
Satyanarayana et al., 2010; Tuttle et al., 2019). In future work, proximity-dependent ligation in zebrafish lines with and without the microexon could reveal differential binding partners in vivo (Rosenthal et al., 2021), as microexons are often found in surface-accessible protein domains and can regulate protein–protein interactions (Dergai et al., 2010; Irimia et al., 2014). The discovery of microexon mutants with neural phenotypes lays the groundwork for future investigation of impacted neurodevelopmental pathways and how interactomes differ between isoforms.

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
      <td>Genetic reagent (D. rerio)</td>
      <td>Microexon mutants</td>
      <td>This paper</td>
      <td>Supplementary file 2</td>
      <td></td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Mouse monoclonal anti-Erk</td>
      <td>Cell Signaling</td>
      <td>#4696</td>
      <td>IF(3:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Rabbit monoclonal anti-phospho-Erk</td>
      <td>Cell Signaling</td>
      <td>#4370</td>
      <td>IF(1:500)</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>E.Z.N.A. MicroElute Total RNA Kit</td>
      <td>Omega Bio-Tek</td>
      <td>R6834-02</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>iScript Reverse Transcription Supermix</td>
      <td>Bio-Rad</td>
      <td>#1708840</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>GoTaq 2x master mix</td>
      <td>Promega</td>
      <td>M7123</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>SsoAdvanced Universal SYBR Green Supermix</td>
      <td>Bio-Rad</td>
      <td>#1725270EDU</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Oligonucleotide primers for genotyping and cDNA amplification</td>
      <td>Life technologies, this paper</td>
      <td>Supplementary files 1 and 2</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Fiji/ImageJ</td>
      <td>https://imagej.net/software/fiji/downloads; Schindelin et al., 2012</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Image registration with CMTK</td>
      <td>https://www.nitrc.org/projects/cmtk; Jefferis et al., 2007</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Zebrafish brain mapping and Z-Brain atlas</td>
      <td>Randlett et al., 2015</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Zebrafish behavior analysis</td>
      <td>https://github.com/thymelab/ZebrafishBehavior; Joo et al., 2020</td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

### Zebrafish husbandry

Zebrafish experiments were approved by the UAB Institutional Animal Care and Use Committee (IACUC protocols 22155 and 21744) and UMass Chan Institutional Animal Care and Use Committee (IACUC protocol 202300000053). Mutants were generated in an Ekkwill-based strain using CRISPR/Cas9 as previously described (Capps et al., 2024; Thyme et al., 2019; Supplementary file 2). Both adults and larvae were maintained on a 14/10 hr light/dark cycle at 28°C. Experimental larvae were maintained at a density of less than 160 per dish in 150 mm Petri dishes in fish water with methylene blue, and debris was removed at least twice prior to experimentation. Visibly unhealthy larvae and those without inflated swim bladders were excluded from experiments. Control animals were always siblings from the same clutch and derived from a single parental pair, and all larvae were genotyped after experimentation. Even with using sibling controls and collecting multiple biological replicates from individual parents, the possibility remains that linked genetic variation may have contributed to the mild phenotypes we observed, as only a single line was generated.

### Brain activity and morphology

Phosphorylated-ERK (pErk) antibody staining was conducted as previously described (Capps et al., 2024; Thyme et al., 2019). The total ERK antibody (Cell Signaling, #4696) was used at 3:1000 and pErk antibody was used at 1:500 (Cell Signaling, #4370). Typically, the primary antibody exposure was for 2–3 days and secondary for 1 day. Image stacks were collected with a Zeiss LSM 900 upright confocal microscope using a 20x/1.0 NA water-dipping objective. These stacks were registered to the standard zebrafish Z-Brain reference using Computational Morphometry Toolkit (CMTK) (Jefferis et al., 2007; Randlett et al., 2015; Rohlfing and Maurer, 2003; Thyme et al., 2019). The significance threshold for MapMAPPING (Randlett et al., 2015; Thyme et al., 2019) was set based on a false discovery rate where 0.05% of control pixels would be called as significant for both the brain activity and structural measurements.

### Larval behavior

Larval behavior assays were conducted and analyzed as previously described (Capps et al., 2024; Joo et al., 2020; Thyme et al., 2019). The pipeline begins on the evening of larval stage 4 dpf and includes the following stimuli: 5 dpf light flashes (9:11 to 9:25), mixed acoustic stimuli (prepulse, strong, and weak, from 9:38 to 2:59), and three blocks of acoustic habituation (3:35 to 6:35); the night between 5 and 6 dpf mixed acoustic stimuli (1:02 to 5:00) and light flashes (6:01 to 6:20); 6 dpf three blocks of dark flashes with an hour between them (10:00 to 3:00) and mixed acoustic stimuli and light flashes (4:02 to 6:00). Stimulus responses were quantified from high-speed (285 fps) 1-s-long movies. All code for behavior analysis is available at https://github.com/thymelab/ZebrafishBehavior (copy archived at Thyme, 2024a). Frequency of movement, magnitude of movement, and location preferences were calculated for the baseline data. An example of a ‘frequency’ measure would be the active seconds/hour. An example of the ‘magnitude’ measure would be the movement velocity of a bout. An example of a ‘location’ measure would be the fraction of the bout time spent in the center of the well. Frequency, response magnitude parameters, and latency to response are also calculated for each stimulus response from the high-speed movies. The stimulus responses are also broken up into subsets, such as the dark flashes that occur at the beginning of the dark flash block and those that occur at the end. Multiple measures are calculated for the experiment, and both summarized and raw measures are shown in Figure 2 and the Supplementary Material. The summarized data is generated by merging related terms (e.g., all the ‘frequency’ measures) together. The size of the bubble represents the percent of significant measurements in the summarized category, and the color represents the mean of the strictly standardized mean difference of the significant assays in that category. It is possible for some measures in the merged group to be increased (purple) and some decreased (orange), such as if a behavioral change occurs between 4 and 6 dpf, which is why it is possible to have two offset bubbles in each square. The scripts for merging these measurements and generating the summarized bubble plot graphs are available at https://github.com/thymelab/DownstreamAnalysis (copy archived at Thyme, 2024b).

### Reverse transcription PCR (RT-PCR and qRT-PCR)

RNA was extracted from zebrafish embryos using the E.Z.N.A. MicroElute Total RNA Kit (Omega Bio-Tek R6834-02), and cDNA synthesis was performed with iScript Reverse Transcription Supermix (Bio-Rad #1708840). Following PCR with GoTaq polymerase (Promega M7123) and primers (Supplementary file 1), samples were run on a 4% agarose gel and the band intensities were quantified using Fiji (Schindelin et al., 2012). For qRT-PCR, we combined three to four zebrafish heads at 6 dpf for each biological replicate. For RT-PCR, these separate biological samples were combined into one per genotype. We homogenized the heads and performed RNA extraction and cDNA synthesis as described above. We then performed qRT-PCR with SsoAdvanced Universal SYBR Green Supermix (Bio-Rad #1725270EDU) according to the manufacturer’s protocol and using primers in Supplementary file 1.
