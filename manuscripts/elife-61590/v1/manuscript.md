# Genetic disruption of WASHC4 drives endo-lysosomal dysfunction and cognitive-movement impairments in mice and humans

## Authors

- Jamie L Courtland<sup>1</sup> ([ORCID: 0000-0001-6846-3552](https://orcid.org/0000-0001-6846-3552))
- Tyler WA Bradshaw<sup>1</sup> ([ORCID: 0000-0003-4480-1187](https://orcid.org/0000-0003-4480-1187))
- Greg Waitt<sup>2</sup>
- Erik J Soderblom<sup>2</sup>
- Tricia Ho<sup>2</sup>
- Anna Rajab<sup>4</sup>
- Ricardo Vancini<sup>5</sup>
- Il Hwan Kim<sup>3</sup> †
- Scott H Soderling<sup>1</sup> ([ORCID: 0000-0001-7808-197X](https://orcid.org/0000-0001-7808-197X)) †

### Affiliations

1. Department of Neurobiology, Duke University School of Medicine Durham United States
2. Proteomics and Metabolomics Shared Resource, Duke University School of Medicine Durham United States
3. Department of Cell Biology, Duke University School of Medicine Durham United States
4. Burjeel Hospital, VPS Healthcare Muscat Oman
5. Department of Pathology, Duke University School of Medicine Durham United States
6. Department of Anatomy and Neurobiology, University of Tennessee Heath Science Center Memphis United States

† Corresponding author

## Abstract

Mutation of the Wiskott–Aldrich syndrome protein and SCAR homology (WASH) complex subunit, SWIP, is implicated in human intellectual disability, but the cellular etiology of this association is unknown. We identify the neuronal WASH complex proteome, revealing a network of endosomal proteins. To uncover how dysfunction of endosomal SWIP leads to disease, we generate a mouse model of the human WASHC4c.3056C>G mutation. Quantitative spatial proteomics analysis of SWIPP1019R mouse brain reveals that this mutation destabilizes the WASH complex and uncovers significant perturbations in both endosomal and lysosomal pathways. Cellular and histological analyses confirm that SWIPP1019R results in endo-lysosomal disruption and uncover indicators of neurodegeneration. We find that SWIPP1019R not only impacts cognition, but also causes significant progressive motor deficits in mice. A retrospective analysis of SWIPP1019R patients reveals similar movement deficits in humans. Combined, these findings support the model that WASH complex destabilization, resulting from SWIPP1019R, drives cognitive and motor impairments via endo-lysosomal dysfunction in the brain.

## Introduction

Neurons maintain precise control of their subcellular proteome using a sophisticated network of vesicular trafficking pathways that shuttle cargo throughout the cell. Endosomes function as a central hub in this vesicular relay system by coordinating protein sorting between multiple cellular compartments, including surface receptor endocytosis and recycling, as well as degradative shunting to the lysosome (Chiu et al., 2017; Cullen and Steinberg, 2018; Raiborg et al., 2015; Simonetti et al., 2019). How endosomal trafficking is modulated in neurons remains a vital area of research due to the unique degree of spatial segregation between organelles in neurons, and its strong implication in neurodevelopmental and neurodegenerative diseases (Follett et al., 2014; Lane et al., 2012; Mukherjee et al., 2019; Poët et al., 2006; Zimprich et al., 2011).

In non-neuronal cells, an evolutionarily conserved complex, the Wiskott–Aldrich syndrome protein and SCAR homology (WASH) complex, coordinates endosomal trafficking (Derivery and Gautreau, 2010; Linardopoulou et al., 2007). WASH is composed of five core protein components: WASHC1 (aka WASH1), WASHC2 (aka FAM21), WASHC3 (aka CCDC53), WASHC4 (aka SWIP), and WASHC5 (aka Strumpellin) (encoded by genes Washc1-Washc5, respectively), which are broadly expressed in multiple organ systems (Alekhina et al., 2017; Kustermann et al., 2018; McNally et al., 2017; Simonetti and Cullen, 2019; Thul et al., 2017). The WASH complex plays a central role in non-neuronal endosomal trafficking by activating Arp2/3-dependent actin branching at the outer surface of endosomes to influence cargo sorting and vesicular scission (Gomez and Billadeau, 2009; Lee et al., 2016; Phillips-Krawczak et al., 2015; Piotrowski et al., 2013; Simonetti and Cullen, 2019). WASH also interacts with at least three main cargo adaptor complexes – the Retromer, Retriever, and COMMD/CCDC22/CCDC93 (CCC) complexes – all of which associate with distinct sorting nexins to select specific cargo and enable their trafficking to other cellular locations (Binda et al., 2019; Farfán et al., 2013; McNally et al., 2017; Phillips-Krawczak et al., 2015; Seaman and Freeman, 2014; Singla et al., 2019). Loss of the WASH complex in non-neuronal cells has detrimental effects on endosomal structure and function, as its loss results in aberrant endosomal tubule elongation and cargo mislocalization (Bartuzi et al., 2016; Derivery et al., 2009; Gomez et al., 2012; Gomez and Billadeau, 2009; Phillips-Krawczak et al., 2015; Piotrowski et al., 2013). However, whether the WASH complex performs an endosomal trafficking role in neurons remains an open question, as no studies have addressed neuronal WASH function to date.

Consistent with the association between the endosomal trafficking system and pathology, dominant missense mutations in WASHC5 (protein: Strumpellin) are associated with hereditary spastic paraplegia (SPG8) (de Bot et al., 2013; Valdmanis et al., 2007), and autosomal recessive point mutations in WASHC4 (protein: SWIP) and WASHC5 are associated with syndromic and non-syndromic intellectual disabilities (Assoum et al., 2020; Elliott et al., 2013; Ropers et al., 2011). In particular, an autosomal recessive mutation in WASHC4 (c.3056C>G; p.Pro1019Arg) was identified in a cohort of children with non-syndromic intellectual disability (Ropers et al., 2011). Cell lines derived from these patients exhibited decreased abundance of WASH proteins, leading the authors to hypothesize that the observed cognitive deficits in SWIPP1019R patients resulted from disruption of neuronal WASH signaling (Ropers et al., 2011). However, whether this mutation leads to perturbations in neuronal endosomal integrity, or how this might result in cellular changes associated with disease, are unknown.

Here we report the analysis of neuronal WASH and its molecular role in disease pathogenesis. We use in vivo proximity proteomics (iBioID) to uncover the neuronal WASH proteome and demonstrate that it is highly enriched for components of endosomal trafficking. We then generate a mouse model of the human WASHC4c.3056c>g mutation (SWIPP1019R) (Ropers et al., 2011) to discover how this mutation may alter neuronal trafficking pathways and test whether it leads to phenotypes congruent with human patients. Using an adapted spatial proteomics approach (Davies et al., 2018; Geladaki et al., 2019; Hirst et al., 2018; Shin et al., 2019), coupled with a system-level analysis of protein covariation networks, we find strong evidence for substantial disruption of neuronal endosomal and lysosomal pathways in vivo. Cellular analyses confirm a significant impact on neuronal endo-lysosomal trafficking in vitro and in vivo, with evidence of lipofuscin accumulation and progressive apoptosis activation, molecular phenotypes that are indicative of neurodegenerative pathology. Behavioral analyses of SWIPP1019R mice at adolescence and adulthood confirm a role of WASH in cognitive processes and reveal profound, progressive motor dysfunction. Importantly, retrospective examination of SWIPP1019R patient data highlights parallel clinical phenotypes of motor dysfunction coincident with cognitive impairments in humans. Our results establish that loss of WASH complex function leads to alterations in the neuronal endo-lysosomal axis, which manifest behaviorally as cognitive and movement impairments in mice.

## Results

### Identification of the WASH complex proteome in vivo confirms a neuronal role in endosomal trafficking

While multiple mutations within the WASH complex have been identified in humans (Assoum et al., 2020; Elliott et al., 2013; Ropers et al., 2011; Valdmanis et al., 2007), how these mutations lead to neurological dysfunction remains unknown (Figure 1A). Given that previous work in non-neuronal cultured cells and non-mammalian organisms have established that the WASH complex functions in endosomal trafficking, we first aimed to determine whether this role was conserved in the mouse nervous system (Alekhina et al., 2017; Jia et al., 2010; Derivery et al., 2009; Gomez et al., 2012; Gomez and Billadeau, 2009). To discover the likely molecular functions of the neuronal WASH complex, we utilized an in vivo BioID (iBioID) paradigm developed in our laboratory to identify the WASH complex proteome from brain tissue (Uezu et al., 2016). BioID probes were generated by fusing a component of the WASH complex, WASH1 (gene: Washc1), with the promiscuous biotin ligase, BioID2 (WASH1-BioID2, Figure 1B), or by expressing BioID2 alone (negative control, solubleBioID2) under the neuron-specific, human Synapsin-1 promoter (Kim et al., 2016). We injected adenoviruses (AAV) expressing these constructs into the cortex of wild-type postnatal day zero (P0) mice (Figure 1B). Two weeks post-injection, we administered daily subcutaneous biotin for 7 days to biotinylate in vivo substrates. The viruses displayed efficient expression and activity in brain tissue, as evidenced by colocalization of the WASH1-BioID2 viral epitope (HA) and biotinylated proteins (Streptavidin) (Figure 1C–F). For label-free quantitative LC-MS/MS analyses, whole-brain samples were collected at P22, snap frozen, and processed as previously described (Uezu et al., 2016). A total of 2102 proteins were identified across all three experimental replicates, which were further analyzed for those with significant enrichment in WASH1-BioID2 samples over solubleBioID2 negative controls (Figure 1—figure supplement 1D, Supplementary file 1).

![Figure 1.](https://cdn.elifesciences.org/articles/61590/elife-61590-fig1-v1.jpg)

**Figure 1.:** (A) The WASH complex is composed of five subunits: Washc1 (WASH1), Washc2 (FAM21), Washc3 (CCDC53), Washc4 (SWIP), and Washc5 (Strumpellin). Human mutations in these components are associated with spastic paraplegia (de Bot et al., 2013; Jahic et al., 2015; Valdmanis et al., 2007), Ritscher–Schinzel syndrome (Elliott et al., 2013), and intellectual disability (Assoum et al., 2020; Ropers et al., 2011). (B) A BioID2 probe was attached to the c-terminus of WASH1 and expressed under the human synapsin-1 (hSyn1) promoter in an AAV construct for in vivo BioID (iBioID). iBioID probes (WASH1-BioID2-HA or negative control solubleBioID2-HA) were injected into wild-type mouse brain at P0 and allowed to express for 2 weeks. Subcutaneous biotin injections (24 mg/kg) were administered over 7 days for biotinylation, and then brains were harvested for isolation and purification of biotinylated proteins. LC–MS/MS identified proteins significantly enriched in all three replicates of WASH1-BioID2 samples over soluble-BioID2 controls. (C) Representative image of WASH1-BioID2-HA expression in a mouse coronal brain section (Cx=cortex, Hipp=hippocampus, Thal=thalamus). Scale bar, 1 mm. (D) Representative image of WASH1-BioID2-HA expression in mouse cortex (inset from C). Individual panels show nuclei (DAPI, blue), AAV construct HA epitope (green), and biotinylated proteins (Streptavidin, red). Merged image shows colocalization of HA and Streptavidin (yellow). Scale bar, 50 µm. (E) Representative image of WASH1-BioID2-HA expression in mouse hippocampus (inset from C). Scale bar, 50 µm. (F) Representative image of WASH1-BioID2-HA expression in mouse thalamus (inset from C). Scale bar, 50 µm. (G) iBioID identified 175 proteins in the WASH interactome (fold-enrichment>4; FDR<0.05). Node size represents protein abundance fold-enrichment over negative control (range: 4–7.5), solid gray edges delineate iBioID interactions between the WASHC1 probe (seen in yellow at the center) and identified proteins, and dashed edges indicate known protein–protein interactions from HitPredict database (López et al., 2015). (H,I) Clustergrams of (H) all five WASH complex proteins identified by iBioID. (I) Previously reported WASH interactors (13/175), including the CCC and Retriever complexes. (J) Endosomal trafficking proteins (23/175 proteins). (K) Endocytic proteins (24/175). (L) Proteins involved in cytoskeletal regulation (31/175), including Arp2/3 subunit, ARPC5. (M) Synaptic proteins (27/175). Clustergrams were annotated by hand and cross-referenced with Metascape GO enrichment (Zhou et al., 2019) of WASH1 proteome constituents over all proteins identified in the BioID experiment.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/61590/elife-61590-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (A) After normalization, protein intensity is not different between SolubleBioID2 Control and WASHC1-BioID2 samples. Control samples are depicted in teal, WASH1 samples are depicted in purple. Data reported as mean ± SD, error bars are SD, n=3 independent experiments. (B) Protein-level missingness is inferred to be missing not-at-random due to the left shifted distribution of the density distributions of proteins with missing values. Top: Density distribution. Bottom: Cumulative distribution. (C) Principal component analysis (PCA) of Control and WASHC1 samples reveals clear separation of experimental conditions. (D) Volcano plot of proteins identified in in vivo BioID experiment illustrates the thresholds used to consider proteins significantly enriched in WASHC1 samples over Control: Fold-change≥4.0, Benjamini–Hochberg FDR<0.05, p<0.05. All five WASH complex proteins were significantly enriched.

The resulting neuronal WASH proteome included 175 proteins that were significantly enriched (fold-change≥4.0, Benjamini–Hochberg FDR<0.05, Figure 1G; Benjamini and Hochberg, 1995). Of these proteins, we identified all five WASH complex components (Figure 1H), as well as 13 previously reported WASH complex interactors (Figure 1I; McNally et al., 2017; Phillips-Krawczak et al., 2015; Simonetti and Cullen, 2019; Singla et al., 2019), which provided strong validity for our proteomic approach and analyses. Additional bioinformatic analyses of the neuronal WASH proteome identified a network of proteins implicated in vesicular trafficking, including 23 proteins enriched for endosomal functions (Figure 1J) and 24 proteins enriched for endocytic functions (Figure 1K). Among these endosomal and endocytic proteins were components of the recently identified endosomal sorting complexes, CCC (CCDC93 and COMMD9) and Retriever (VPS35L) (Phillips-Krawczak et al., 2015; Singla et al., 2019), as well as multiple sorting nexins important for recruitment of trafficking regulators to the endosome and cargo selection, such as SNX1-3 and SNX16 (Kvainickas et al., 2017; Maruzs et al., 2015; Shin et al., 2019; Simonetti et al., 2017). These data demonstrated that the WASH complex interacts with many of the same proteins in neurons as it does in yeast, amoebae, flies, and mammalian cell lines. Furthermore, there were 31 proteins enriched for cytoskeletal regulatory functions (Figure 1L), including actin-modulatory molecules such as the Arp2/3 complex subunit ARPC5, which is consistent with WASH’s role in activating this complex to stimulate actin polymerization at endosomes for vesicular scission (Jia et al., 2010; Derivery et al., 2009). The WASH1-BioID2 isolated complex also contained 27 proteins known to localize to the excitatory post-synapse (Figure 1M). This included many core synaptic scaffolding proteins, such as SHANK2-3 and DLGAP2-4 (Chen et al., 2011; Mao et al., 2015; Monteiro and Feng, 2017; Wan et al., 2011), as well as modulators of synaptic receptors such as SYNGAP1 and SHISA6 (Barnett et al., 2006; Clement et al., 2012; Kim et al., 2003; Klaassen et al., 2016), which was consistent with the idea that vesicular trafficking plays an important part in synaptic function and regulation. Taken together, these results support a major endosomal trafficking role of the WASH complex in mouse brain.

### SWIPP1019R does not incorporate into the WASH complex, reducing its stability and levels in vivo

To determine how disruption of the WASH complex may lead to disease, we generated a mouse model of a human missense mutation found in children with intellectual disability, WASHC4c.3056c>g (protein: SWIPP1019R) (Ropers et al., 2011). Due to the sequence homology of human and mouse Washc4 genes, we were able to introduce the same point mutation in exon 29 of murine Washc4 using CRISPR (Derivery and Gautreau, 2010; Ropers et al., 2011). This C>G point mutation results in a Proline>Arginine substitution at position 1019 of SWIP’s amino acid sequence (Figure 2A), a region thought to be critical for its binding to the WASH component, Strumpellin (Jia et al., 2010; Ropers et al., 2011). Western blot analysis of brain lysate from adult homozygous SWIPP1019R mutant mice (referred to from here on as MUT mice) displayed significantly decreased abundance of two WASH complex members, Strumpellin and WASH1 (Figure 2B). These results phenocopied data from the human patients (Ropers et al., 2011) and suggested that the WASH complex is unstable in the presence of this SWIP point mutation in vivo. To test whether this mutation disrupted interactions between WASH complex subunits, we compared the ability of wild-type SWIP (WT) and SWIPP1019R (MUT) to co-immunoprecipitate with Strumpellin and WASH1 in HEK cells. Compared to WT, MUT SWIP co-immunoprecipitated significantly less Strumpellin and WASH1 (IP: 54.8% and 41.4% of WT SWIP, respectively), suggesting that the SWIPP1019R mutation hinders WASH complex formation (Figure 2—figure supplement 1). Together these data support the notion that SWIPP1019R is a damaging mutation that not only impairs its function, but also results in significant reductions of the WASH complex as a whole.

![Figure 2.](https://cdn.elifesciences.org/articles/61590/elife-61590-fig2-v1.jpg)

**Figure 2.:** (A) Mouse model of the human SWIPP1019R missense mutation created using CRISPR. A C>G point mutation was introduced into exon29 of murine Washc4, leading to a P1019R amino acid substitution. We hypothesize (H1) that this mutation causes instability of the WASH complex. (B) Representative western blot and quantification of WASH components, Strumpellin and WASH1 (predicted sizes in kDa: 134 and 72, respectively), as well as loading control β-tubulin (55 kDa) from adult whole-brain lysate prepared from SWIP WT (Washc4C/C) and SWIP homozygous MUT (Washc4G/G) mice. Bar plots show quantification of band intensities normalized to β-tubulin, expressed as a % of WT (n=3 mice per genotype). Strumpellin (WT 100.0±5.1%, MUT 3.8±0.9%, t2.14=18.60, p=0.0021) and WASH1 (WT 100.0±4.3%, MUT 1.1±0.4%, t2.1=22.77, p=0.0018) were significantly decreased. Equivalent amounts of protein were analyzed in each condition (β-tubulin: WT 100.0±8.2%, MUT 94.1±4.1%, U=4, p>0.99). (C) Schematic of experimental techniques used to interrogate the effect of the SWIPP1019R mutation in subsequent figures: spatial proteomics (top), confocal and electron microscopy (middle), and mouse behavioral tasks (bottom).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/61590/elife-61590-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** (A) Schematic showing overexpression of WT or MUT SWIPP1019R in HEK293T cells followed by immunoprecipitation. (B) Western blots of input (5%, left) and immunoprecipitated (IP, right) protein. Two samples per condition were run on two separate gels, n=4 separate experiments. (C) Quantification of B normalized to WT. Strumpellin (WT 100.0±6.8%, MUT 54.8±8.0%, t5.9=4.290, p=0.0054), WASH1 (WT 100.0±7.3%, MUT 41.4±4.4%, t4.9=6.902, p=0.0011), HA (WT 100.0±4.1%, MUT 107.8±4.1%, t6.0=1.344, p=0.2275). Data reported as mean ± SEM, error bars are SEM. **p<0.01, two-tailed t-tests.

### Unbiased spatial proteomics analysis of SWIPP1019R mutant mouse brain reveals significant disruptions in endo-lysosomal pathways

Next, we aimed to understand the impact of the SWIPP1019R mutation on the subcellular organization of the mouse brain proteome using spatial proteomics. Conceptually, spatial proteomics encompasses a variety of methodological and analytical approaches, which share a common goal: predicting the subcellular localization of proteins. Most often this is done by combining subcellular fractionation of a biological sample with proteomic profiling of the resultant fractions (Breckels et al., 2016; Crook et al., 2019; Crook et al., 2018; Geladaki et al., 2019; Itzhak et al., 2017; Itzhak et al., 2016; Jean Beltran et al., 2016). We performed spatial proteomics by subcellular fractionation, MS profiling, and subsequent clustering analysis. Clusters (modules) in the spatial proteomics network represent predicted subcellular compartments composed of proteins whose abundance covaries together in subcellular space (Geladaki et al., 2019; Mulvey et al., 2017). We analyzed differential abundance of individual proteins, as well as of protein groups (modules) identified in the spatial proteomics network to evaluate how the pathogenic SWIPP1019R mutation may perturb the organization of the neuronal subcellular proteome. This approach enabled us to study protein changes at a network level, which provided more biologically relevant insight than would be possible by assessing only protein-level differences.

Brains from 10-month-old mice were gently homogenized to release intact organelles, followed by successive centrifugation steps to enrich subcellular compartments into different biological fractions (BioFractions) based on their density (Figure 3A; Geladaki et al., 2019). Seven WT and seven MUT fractions (each prepared from one brain, 14 samples total) were labeled with unique isobaric tandem-mass tags and concatenated. We also included two sample pooled quality controls (SPQCs), which allowed us to assess experimental variability and perform normalization between experiments. By performing this experiment in triplicate, deep coverage of the mouse brain proteome was obtained – across all 48 samples we quantified 86,551 peptides, corresponding to 7488 proteins. After data pre-processing, normalization, and filtering, we retained 6919 reproducibly quantified proteins in the final dataset (Supplementary file 2).

![Figure 3.](https://cdn.elifesciences.org/articles/61590/elife-61590-fig3-v1.jpg)

**Figure 3.:** (A) Tandem-mass-tag (TMT) spatial proteomics experimental design. Seven subcellular fractions were prepared from one WT and one MUT mouse (10mo). These samples, as well as two pooled quality control (QC) samples, were labeled with unique TMT tags and concatenated for simultaneous 16-plex LC–MS/MS analysis. This experiment was repeated three times (three WT and three MUT brains total). To detect network-level changes, proteins were clustered into modules, and linear mixed models (LMMs) were used to identify differences in module abundance between WT and MUT conditions. The network shows an overview of the spatial proteomics graph in which 49 different modules are indicated by colored nodes. (B) Protein module 38 (M38) contains subunits of the WASH, CCC, Retriever, and CORVET/HOPS complexes. Node size denotes its weighted degree centrality (~importance in module); purple node color indicates proteins with altered abundance in MUT brain relative to WT; red, yellow, orange, and green node borders highlight protein components of the CCC, Retriever, CORVET/HOPS, and WASH complexes obtained from the CORUM database; dashed black edges indicate experimentally determined protein-protein interactions; and gray-red edges denote the relative strength of protein covariation within a module (gray=weak, dark red=strong). (C) M38 displays decreased overall abundance in MUT brain. The aligned profiles of all M38 proteins are plotted together after sum normalization, and rescaling such that the maximum intensity is 1. Each solid line represents a single protein, measured in WT (teal) and MUT (purple) conditions. The estimated WT and MUT means are displayed in dashed teal and purple lines, respectively (WT-MUT Contrast log2Fold-Change=−0.12, T=−11.14, DF=2324, p-adjust=2.078×10−26; n=3 independent experiments). (D) Protein profile of WASHC4 (aka SWIP) plotted as relative (sum-normalized) protein intensity, rescaled to be in the range of 0–1 (WT-MUT Contrast log2Fold-Change=−1.517, DF=26, p-adjust=1.72×10−16; n=3 independent experiments). WT levels are depicted in teal, and MUT levels are depicted in purple. Shaded error bar represents the min-to-max values of all three experimental replicates. Significant differences in individual BioFraction WASHC4 levels are indicated with stars. ***p<0.001, MSstatsTMT p-value for intra-BioFraction comparisons with FDR correction.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/61590/elife-61590-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (A) Line graph depicting LAMP1 signal abundance normalized to total protein across subcellular biological fractions. LAMP1 pattern reveals no difference between MUT and WT in LAMP1 pelleting, but a significant difference in the abundance of LAMP1 in BioFraction 8 (two-way ANOVA genotype effect, F4,44=7.68, p<0.0001; Sidak’s multiple comparisons test, p=0.0006). Shaded region highlights subcellular fractions used in 16-plex TMT mass spectrometry experiments. Fractions 4–10 from one WT and one MUT mouse were analyzed for each TMT experiment. Data reported as mean ± SEM, error bars are SEM. (B) Western blots depicting LAMP1 abundance from three separate WT animals (Experiments 1–3). (C) Western blots depicting LAMP1 abundance from three separate MUT animals (Experiments 1–3).

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/61590/elife-61590-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** (A) Line graph depicting EEA1 signal abundance normalized to total protein across subcellular biological fractions. EEA1 pattern reveals no difference between MUT and WT in EEA1 pelleting (two-way ANOVA genotype effect, F1,4=0.290, p=0.6184). Shaded region highlights subcellular fractions used in 16-plex TMT mass spectrometry experiments. Fractions 4–10 from one WT and one MUT mouse were analyzed for each TMT experiment. Data reported as mean ± SEM, error bars are SEM. (B) Western blots depicting EEA1 abundance from three separate WT animals (Experiments 1–3). (C) Western blots depicting EEA1 abundance from three separate MUT animals (Experiments 1–3).

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/61590/elife-61590-fig3-figsupp3-v1.jpg)

**Figure 3—figure supplement 3.:** (A) Line graph depicting total protein abundance across subcellular biological fractions. There is no difference between MUT and WT samples (two-way ANOVA genotype effect, F1,4=0.0094, p=0.9274), measured by mean fluorescence units (M.F.U.) per lane. Shaded region highlights subcellular fractions used in 16-plex TMT mass spectrometry experiments. Fractions 4–10 from one WT and one MUT mouse were analyzed for each TMT experiment. Data reported as mean ± SEM, error bars are SEM. (B) Western blots of total protein abundance across subcellular fractions from three separate WT animals (Experiments 1–3). (C) Western blots of total protein abundance across subcellular fractions from three separate MUT animals (Experiments 1–3). Total protein abundance per lane was used for normalizing endosomal and lysosomal markers.

![Figure 3—figure supplement 4.](https://cdn.elifesciences.org/articles/61590/elife-61590-fig3-figsupp4-v1.jpg)

**Figure 3—figure supplement 4.:** (A) Experimental design used for tandem-mass-tag (TMT) spatial proteomics. Each experiment was designated as a mixture (Mix 1–3), with seven BioFractions prepared from one WT and one MUT animal (TMT channels: C1–7=WT; C9–15=MUT). The g-force pelleting speed used to obtain each BioFraction is indicated in the corresponding square (i.e. 5K=5000xg). Two sample-pooled quality control samples were used for normalization between experiments in channels 8 and 16 (QC1 and QC2). (B) Boxplot of protein intensity for all proteins in each sample showing no large differences within or between batches after normalization. (C) Principal component analysis of each sample reveals separation of all 7 BioFractions. (D) The variance attributable to the experiments’ major covariates for every protein. After normalization, the major source of variation for most proteins is BioFraction. After normalization, the variation attributable to differences between mixtures is negligible. (E) Principal component analysis of proteins showing the 49 modules identified by clustering the spatial proteomics network. (F) Matrix of comparisons used by MSstatsTMT to assess intra-BioFraction and overall protein differences between Control and Mutant conditions.

![Figure 3—figure supplement 5.](https://cdn.elifesciences.org/articles/61590/elife-61590-fig3-figsupp5-v1.jpg)

**Figure 3—figure supplement 5.:** (A) Module 4 is 5.6-fold enriched for plasma membrane proteins (p-adjust=1.39×10−38) and displays no significant change in module-level intensity between WT and MUT conditions (p-adjust=0.323). (B) Module 5 is 2.4-fold enriched for nuclear proteins (p-adjust=3.48×10−22) and displays no significant change in module-level intensity between WT and MUT conditions (p-adjust=0.270). (C) Module 1 is 6.7-fold enriched for cytosolic proteins (p-adjust=1.06×10−89) and displays a slight change in module-level intensity between WT and MUT conditions (p-adjust=6.5×10−20). (D) Module 13 is 6.1-fold enriched for ribosomal proteins (p-adjust=2.0×10−10) and displays no significant change in module-level intensity between WT and MUT conditions (p-adjust=1). (E) Module 7 is 4.7-fold enriched for endoplasmic reticulum proteins (p-adjust=8.43×10−16) and displays no significant change in module-level intensity between WT and MUT conditions (p-adjust=1). (F) Module 40 is 6.8-fold enriched for mitochondrial proteins (p-adjust=5.40×10−15) and displays a slight change in module-level intensity between WT and MUT conditions (p-adjust=8.18×10−6). (G) Module 9 is 18.5-fold enriched for peroxisomal proteins (p-adjust=1.39×10−20) and displays no significant change in module-level intensity between WT and MUT conditions (p-adjust=0.474). (H) Module 8 is 27.6-fold enriched for proteasomal proteins (p-adjust=7.91×10−41) and displays no significant change in module-level intensity between WT and MUT conditions (p-adjust=1). For all modules, light purple nodes represent proteins with decreased abundance in MUT samples, dark purple nodes represent proteins with increased abundance in MUT samples, blue node borders highlight proteins with sample organelle designation as (Geladaki et al., 2019), experimentally determined protein–protein interactions (HitPredict), and gray-red edges denote the relative strength of protein covariation within a module (gray=weak, dark red=strong). Corresponding profile plots for each module depict individual scaled protein intensities in light teal (WT) and purple (MUT) lines, with the estimated value of WT and MUT conditions shown as dashed lines.

We used MSstatsTMT to assess differential protein abundance for intra-fraction comparisons between WT and MUT genotypes and for overall comparisons between WT and MUT groups across all BioFractions (Figure 3—figure supplement 4F; Huang et al., 2020). In the first analysis, there were 65 proteins with significantly altered abundance in at least one of the seven subcellular fractions (Benjamini–Hochberg FDR<0.05, Supplementary file 2). Five proteins were differentially abundant between WT and MUT in all seven fractions, including four WASH proteins (WASHC1, WASHC2, WASHC4, WASHC5) and RAB21A – a known WASH interactor that functions in early endosomal trafficking ( Figure 3D; Del Olmo et al., 2019; Simpson et al., 2004). The abundance of the remaining WASH complex protein, WASHC3, was found to be very low and was only significantly reduced in BioFraction 10 (F10) and the overall (‘Mutant-Control’) comparison. These data affirm that the SWIPP1019R mutation destabilizes the WASH complex. Next, to evaluate global differences between WT and MUT brain, we analyzed the average effect of genotype on protein abundance across all fractions using MSstatsTMT (Huang et al., 2020). At this level, there were 728 differentially abundant proteins between WT and MUT brain (Benjamini–Hochberg FDR<0.05) (Supplementary file 2). We then aimed to place these differentially abundant proteins into a more meaningful biological context using a spatial proteomics approach.

Network-level analyses of spatial proteomic datasets can generally be performed in one of two ways: a top-down approach where proteins are grouped into organellar compartments learned from a predefined set of marker proteins, or a bottom-up approach where proteins are first clustered together based on covariation across biological fractions, and then analyzed for organellar enrichment (Breckels et al., 2016; Crook et al., 2019; Crook et al., 2018; Itzhak et al., 2019; Itzhak et al., 2017; Jean Beltran et al., 2016; Orre et al., 2019). For our network-based analyses, we chose to use a bottom-up approach, where we clustered the protein covariation network defined by the pairwise Pearson correlations between all proteins (Freedman et al., 2007). Our data-driven, quality-based approach used Network Enhancement (Wang et al., 2018) to remove biological noise from the covariation network and optimized partitions of the graph by maximizing the Surprise quality statistic (Aldecoa and Marín, 2013; Traag et al., 2015). Clustering of the protein covariation graph identified 49 modules of proteins that strongly covaried together (see Materials and methods for complete description of clustering approach).

To test for module-level differences between WT and MUT brain, we extended the LMM framework provided by MSstatsTMT to perform statistical inference at the level of protein groups (Huang et al., 2020). To identify systematic differences in the abundance of protein groups (modules), we fit the protein-level data for each module with a linear mixed-model expressing the mixed effect term, Protein, representing variation among a module’s constituent proteins. We then performed a contrast of condition means given the fitted model, as described by Huang et al., 2020. Twenty-three of the 49 modules exhibited significant differences in WT versus MUT brain (Bonferroni p-adjust < 0.05; Supplementary file 3; Benjamini and Hochberg, 1995; Hochberg, 1988). Of note, the module containing the WASH complex, M38, was predicted to have endosomal function by annotation of protein function (UniProt: ‘Early Endosome’, hypergeometric test p-adjust < 0.05, Supplementary file 4). Similar to the WASH iBioID proteome (Figure 1), M38 contained many endosomal proteins, including components of the CCC (CCDC22, CCDC93, COMMD1-3, and COMMD6-7) and Retriever sorting complexes (VPS26C and VPS35L) (Figure 3B). It also contained core subunits of the CORVET and HOPS vesicular tethering complexes, which enable fusion of vesicles within the endo-lysosomal system (VPS11, VPS16, VPS18, and VPS33A) (van der Beek et al., 2019). Across all fractions, the abundance of M38 was significantly lower in MUT brain compared to WT, providing evidence that the SWIPP1019R mutation reduces the stability of this protein subnetwork and impairs its function (Figure 3C).

We also observed another module, M36, that was enriched for lysosomal protein components (hypergeometric test p-adjust <0.05) (Geladaki et al., 2019) and contained all eight subunits of the exocyst complex (CORUM), a vesicular trafficking complex involved in lysosomal secretion (Giurgiu et al., 2019; Sáez et al., 2019). In contrast to the decreased abundance of the WASH complex/endosome module (M38), M36 exhibited increased abundance in MUT brain (Figure 4C). M36 (Figure 4B) contained several lysosomal cathepsin proteases (CTSA, CTSB, CTSS, and CTSL) as well as key lysosomal hydrolases (HEXA, GBA, GLB1, MAN2B1, and MAN2B2) (Eng and Desnick, 1994; Mayor et al., 1993; Mok et al., 2003; Moon et al., 2016; Patel et al., 2018; Regier and Tifft, 1993; Rosenbaum et al., 2014). Notably, M36 also contained the lysosomal glycoprotein progranulin (GRN), which is integral to proper lysosome function and whose loss is widely linked with neurodegenerative pathologies (Baker et al., 2006; Pottier et al., 2016; Tanaka et al., 2017; Zhou et al., 2018). The overall increase in abundance of module 36, and these key lysosomal proteins (Figure 4C–E), may therefore reflect an increase in flux through degradative lysosomal pathways in SWIPP1019R brain.

![Figure 4.](https://cdn.elifesciences.org/articles/61590/elife-61590-fig4-v1.jpg)

**Figure 4.:** (A) Simplified schematic of the endo-lysosomal pathway in neurons. Inset depicts representative lysosomal enzymes, such as proteases (CTSL), glycosidases (MAN2B1, MAN2B2, GLB1, HEXA), and key lysosomal regulators (GRN). (B) Network graph of module 36 (M36). M36 proteins that exhibit altered abundance in MUT brain include lysosomal proteins, HEXA, GLB1, MAN2B1, MAN2B2, GRN, and CTSL. Network attributes: Node size denotes its weighted degree centrality (~importance in module), node color indicates proteins with altered abundance in MUT brain relative to WT, yellow outlines highlight proteins identified as lysosomal in Geladaki et al., 2019, green outlines indicate members of the exocyst complex (CORUM), dashed black edges indicate experimentally determined protein-protein interactions (HitPredict), and gray-red edges denote the relative strength of protein covariation within a module (gray=weak, dark red=strong). (C) The scaled protein intensity of all M36 proteins plotted together as a module. Overall, there is a significant increase in the estimated mean of M36 relative to WT (WT-MUT log2Fold-Change=0.086, T=8.25, DF=2488, p-adjust=1.29×10−14; n=3 independent experiments). Light teal and purple lines denote scaled protein profiles for individual WT and MUT proteins, respectively. Dashed green and purple lines indicate mean scaled protein intensities for WT and MUT, respectively. (D) Protein profile of lysosomal protein progranulin, GRN (WT-MUT Contrast log2Fold-Change=0.637, DF=28, p-adjust=1.58×10−5; n=3 independent experiments). (E) Protein profile of lysosomal enzyme, MAN2B1 (WT-MUT Contrast log2Fold-Change=0.319, DF=26, p-adjust=2.75×10−4; n=3 independent experiments). For (D) and (E), WT levels are depicted in teal, and MUT levels are depicted in purple. Shaded error bar represents the min-to-max values of all three experimental replicates. Significant differences in individual BioFraction levels are indicated with stars. *p<0.05, MSstatsTMT p-value for intra-BioFraction comparisons with FDR correction (D,E).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/61590/elife-61590-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** (A) Network graph of Module 22 (M22) containing endosomal proteins from UniProt. Three retromer sorting complex subunits (CORUM) are highlighted with teal borders and endosomal proteins are highlighted with orange borders. For all networks, light purple nodes denote proteins whose abundance is decreased in MUT samples, dark purple nodes denote proteins whose abundance is increased in MUT samples, node size reflects weighted degree centrality (~importance in network), dashed black lines denote protein–protein interactions, and gray-red lines indicate covariation strength (gray=weak, dark red=strong). (B) Module-level profile of scaled M22 protein intensity reveals decreased abundance in MUT samples compared to WT (WT-MUT log2Fold-Change=−0.095, T=−11.5, DF=4128, p-adjust=2.42×10−28; n=3 independent experiments). For all profile plots, light teal lines denote individual WT protein levels, light purple lines denote individual MUT protein levels, dashed green lines represent estimated WT scaled intensity, and dashed purple lines represent estimated MUT scaled intensity. (C) Network graph of Module 6 (M6) containing endoplasmic reticulum proteins. Inset highlights multiple proteins involved in the ER stress response. Proteins which were also designated as ER localized in the dataset by Geladaki et al., 2019 are highlighted with blue borders. (D) Profile of M6. Overall, there is a significant increase in MUT conditions compared to WT (WT-MUT log2Fold-Change=0.059, T=12.2, DF=10934, p-adjust=3.68×10−32; n=3 independent experiments). (E) Network graph of Module 27 (M27) containing synaptic proteins. Synaptic proteins are highlighted with pink node borders, and proteins that were also identified as enriched in the WASH1-BioID2 proteome (Figure 1) are highlighted with yellow node borders. (F) Module-level profile plotting scaled protein intensities of M27 constituents. Overall, there is a significant decrease in MUT conditions compared to WT (WT-MUT log2Fold-Change=−0.059, T=−6.89, DF=3718, p-adjust=3.19×10−10; n=3 independent experiments).

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/61590/elife-61590-fig4-figsupp2-v1.jpg)

**Figure 4—figure supplement 2.:** (A) Schematic representation of brain region analyzed, motor cortex, adapted from Allen Brain Atlas (Oh et al., 2014). (B,C) Representative images of excitatory synaptic staining in adolescent WT (B) and MUT (C) brain. Excitatory pre-synaptic marker, bassoon, is depicted in magenta and excitatory post-synaptic marker, homer1, is depicted in green. Their colocalization is visualized as white puncta. (D) Graph of the average number of synaptic puncta per 250×250 µm region of interest, normalized to percent of WT (WT 100.0±3.5, n=18 regions of interest (ROIs;) MUT 97.36±3.3, n=18 ROIs; t33.9=0.5509, p=0.5853). (E,F) Representative images of excitatory synaptic staining in aged adult WT (E) and MUT (F) brain. (G) Graph of the average number of synaptic puncta per 250×250 µm region of interest, normalized to percent of WT (WT 100.0±3.4, n=18 ROIs; MUT 80.80±2.4, n=18 ROIs; t30.9=4.599, p<0.0001). Analyses included three separate animals per condition. Scale bars, 5 µm (B–F). Data reported as mean ± SEM, error bars are SEM. ****p<0.0001, two-tailed t-tests.

Besides these endo-lysosomal changes, module-level alterations were evident for an endoplasmic reticulum (ER) module (M6), supporting a shift in the proteostasis of mutant neurons (Figure 4—figure supplement 1C–D). Notably, within the ER module, M6, there was increased abundance of chaperones (e.g. HSPA5, PDIA3, PDIA4, PDIA6, and DNAJC3) that are commonly engaged in presence of misfolded proteins (Bartels et al., 2019; Kim et al., 2020; Montibeller and de Belleroche, 2018; Synofzik et al., 2014; Wang et al., 2016). This elevation of ER stress modulators can be indicative of neurodegenerative states, in which the unfolded protein response (UPR) is activated to resolve misfolded species (Garcia-Huerta et al., 2016; Hetz and Saxena, 2017). These data demonstrate that loss of WASH function not only alters endo-lysosomal trafficking, but also causes increased stress on cellular homeostasis.

In addition, we also observed a synaptic module (M27) that was reduced in MUT brain (Figure 4—figure supplement 1E–F). This module included core excitatory post-synaptic proteins such as SHANK2 and DLGAP4 (also identified in WASH1-BioID, Figure 1), consistent with endosomal WASH influencing synaptic regulation. Decreased abundance of these modules indicates that loss of the WASH complex may result in failure of these proteins to be properly trafficked to the synapse. In line with these findings, we observed fewer excitatory synapses in adult MUT brain compared to WT (Figure 4—figure supplement 2), validating that these module-level differences correlate with cellular alterations in vivo.

### Mutant neurons display structural abnormalities in endo-lysosomal compartments in vitro

Combined, the proteomics data strongly suggested that endo-lysosomal pathways are altered in adult SWIPP1019R mutant mouse brain. Next, we analyzed whether structural changes in this system were evident in primary neurons. Cortical neurons from littermate WT and MUT P0 pups were cultured for 15 days in vitro (DIV15, Figure 5A), then fixed and stained for established markers of early endosomes (early endosome antigen 1 [EEA1]; Figure 5B and C) and lysosomes (Cathepsin D [CathD]; Figure 5D and E). Reconstructed three-dimensional volumes of EEA1 and Cathepsin D puncta revealed that MUT neurons display larger EEA1+ somatic puncta than WT neurons (Figure 5G and J), but no difference in the total number of EEA1+ puncta (Figure 5F). This finding is consistent with a loss-of-function mutation, as loss of WASH activity prevents cargo scission from endosomes and leads to cargo accumulation (Bartuzi et al., 2016; Gomez et al., 2012). Conversely, MUT neurons exhibited significantly less Cathepsin D+ puncta than WT neurons (Figure 5H), but the remaining puncta were significantly larger than those of WT neurons (Figure 5I and K). These data support the finding that the SWIPP1019R mutation results in both molecular and morphological abnormalities in the endo-lysosomal pathway.

![Figure 5.](https://cdn.elifesciences.org/articles/61590/elife-61590-fig5-v1.jpg)

**Figure 5.:** (A) Experimental design. Cortices were dissected from P0 pups, and neurons were dissociated and cultured on glass coverslips for 15 days. Cultures were fixed, stained, and imaged using confocal microscopy. 3D puncta volumes were reconstructed from z-stack images using Imaris software. (B,C) Representative 3D reconstructions of WT and MUT DIV15 neurons (respectively) stained for EEA1 (yellow) and MAP2 (magenta). (D,E) Representative 3D reconstructions of WT and MUT DIV15 neurons (respectively) stained for Cathepsin D (cyan) and MAP2 (magenta). (F) Graph of the average number of EEA1+ volumes per soma in each image (WT 95.0±5.5, n = 24 neurons; MUT 103.7±3.7, n = 24 neurons; U = 208.5, p=0.1024). (G) Graph of the average EEA1+ volume size per soma shows larger EEA1+ volumes in MUT neurons (WT 0.15±0.01 µm3, n=24 neurons; MUT 0.30±0.02 µm3, n=24 neurons; U=50, p<0.0001). (H) Graph of the average number of Cathepsin D+ volumes per soma illustrates less Cathepsin D+ volumes in MUT neurons (WT 30.4±1.4, n=42; MUT 17.2±0.9, n=42; U=204, p<0.0001). (I) Graph of the average Cathepsin D+ volume size per soma demonstrates larger Cathepsin D+ volumes in MUT neurons (WT 0.54±0.02 µm3, n=42; MUT 0.69±0.04 µm3, n=42; t63=3.701, p=0.0005). (J) Histogram of EEA1+ volumes illustrate differences in size distributions between MUT and WT neurons (D=0.2661, p<0.0001). (K) Histogram of CathD+ volumes show differences in size distributions between MUT and WT neurons (D=0.1307, p<0.0001). Analyses included at least three separate culture preparations. Scale bars, 5 µm (B–E). Data reported as mean ± SEM, error bars are SEM. ***p<0.001, ****p<0.0001, Mann–Whitney U test (F–H), two-tailed t-test (I), or Kolmogorov–Smirnov test (J,K).

### SWIPP1019R mutant brains exhibit markers of abnormal endo-lysosomal structures and cell death in vivo

As there is strong evidence that dysfunctional endo-lysosomal trafficking and elevated ER stress are associated with neurodegenerative disorders, adolescent (P42) and adult (10 month old, 10mo) WT and MUT brain tissues were analyzed for the presence of cleaved caspase-3, a marker of apoptotic pathway activation, in four brain regions (Boatright and Salvesen, 2003; Porter and Jänicke, 1999). Very little cleaved caspase-3 staining was present in WT and MUT mice at adolescence (Figure 6A and B, and Figure 6—figure supplement 1). However, at 10mo, the MUT motor cortices displayed significantly greater cleaved caspsase-3 staining compared to age-matched WT littermate controls (Figures 6D, E and H). Furthermore, this difference appeared to be selective for the motor cortex, as we did not observe significant differences in cleaved caspase-3 staining at either age for hippocampal, striatal, or cerebellar regions (Figure 6—figure supplement 1). Consistent with these findings, there were no significant differences in dopaminergic cell number in the substantia nigra pars compacta or in dopaminergic innervation of the striatum in adult brain, suggesting that the motor cortex was the primary movement-related region altered in SWIPP109R brain (Figure 6—figure supplement 2). These data suggested that neurons of the motor cortex were particularly susceptible to disruption of endo-lysosomal pathways downstream of SWIPP109R, perhaps because long-range corticospinal projections require high fidelity of trafficking pathways (Blackstone et al., 2011; Slosarek et al., 2018; Wang et al., 2014).

![Figure 6.](https://cdn.elifesciences.org/articles/61590/elife-61590-fig6-v1.jpg)

**Figure 6.:** (A,B) Representative images of adolescent (P42) WT and MUT motor cortex stained with cleaved caspase-3 (CC3, green). (C) Anatomical representation of mouse brain with motor cortex highlighted in red, adapted from the Allen Brain Atlas (Oh et al., 2014). (D,E) Representative image of adult (10 mo) WT and MUT motor cortex stained with CC3 (green). (F, G, I, and J) DAPI co-stained images for (A, B, D, and E, respectively). Scale bar for (A–J), 15 µm. (H) Graph depicting the normalized percentage of DAPI+ nuclei that are positive for CC3 per image. No difference is seen at P42, but the amount of CC3+ nuclei is significantly higher in aged MUT mice (P42 WT 6.97 ± 0.80%, P42 MUT 5.26 ± 0.90%, 10mo WT 25.38 ± 2.05%, 10mo MUT 44.01 ± 1.90%, H=74.12, p<0.0001). We observed no difference in number of nuclei per image between genotypes. (K) Representative transmission electron microscopy (TEM) image taken of soma from adult (7mo) WT motor cortex. Arrowheads delineate electron-dense lipofuscin material, Nuc=nucleus. (L) Representative transmission electron microscopy (TEM) image taken of soma from adult (7mo) MUT motor cortex. (M) Inset from (K) highlights lysosomal structure in WT soma. Pseudo-colored region depicts lipofuscin area, demarcated as L. (N) Inset from (L) highlights large lipofuscin deposit in MUT soma (L, pseudo-colored region) with electron-dense and electron-lucent lipid-like (asterisk) components. (O) Graph of areas of electron-dense regions of interest (ROI) shows increased ROI size in MUT neurons (WT 2.4×105 ± 2.8×104 nm2, n=50 ROIs; MUT 8.2×105±9.7×104 nm2, n=75 ROIs; U=636, p<0.0001). (P) Graph of the average number of presumptive lysosomes with associated electron-dense material reveals increased number in MUT samples (WT 3.14±0.72 ROIs, n=14 images; MUT 10.86 ± 1.42 ROIs, n=14 images; U=17, p<0.0001). For (O) and (P), images were taken from multiple TEM grids, prepared from n=3 animals per genotype. Scale bar for all TEM images, 1 µm. Data reported as mean ± SEM, error bars are SEM. *p<0.05, ****p<0.0001, Kruskal–Wallis test (H), Mann–Whitney U test (O,P).

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/61590/elife-61590-fig6-figsupp1-v1.jpg)

**Figure 6—figure supplement 1.:** (A) Representative image of adolescent (P42) WT striatum stained with cleaved caspase-3 (CC3, green). (B) Representative image of adolescent (P42) MUT striatum stained with cleaved caspase-3 (CC3, green). (C,D) DAPI co-stained images of A and B, respectively. (E) Anatomical representation of mouse brain with striatum highlighted in red, adapted from the Allen Brain Atlas (Oh et al., 2014). (F) Representative image of adult (10 mo) WT striatum stained with CC3 (green). (G) Representative image of adult (10 mo) MUT striatum stained with CC3 (green). (H,I) DAPI co-stained images of F and G, respectively. Scale bars for A-I are 15 µm. (J) Graph depicting the normalized % of DAPI+ nuclei that are positive for CC3 per image. No difference is seen between genotypes at either age (P42 WT 3.70 ± 0.99%, P42 MUT 1.95 ± 0.49%, 10mo WT 16.77 ± 2.09%, 10mo MUT 24.86 ± 2.17%, H=61.87, p<0.0001). (K) Representative image of adolescent (P42) WT cerebellum stained with cleaved caspase-3 (CC3, green). (L) Representative image of adolescent (P42) MUT cerebellum stained with cleaved caspase-3 (CC3, green). (M,N) DAPI and Calbindin co-stained images of K and L, respectively. (O) Anatomical representation of mouse cerebellum, adapted from the Allen Brain Atlas (Oh et al., 2014). Red region highlights area used for imaging. (P) Representative image of adult (10 mo) WT cerebellum stained with CC3 (green). (Q) Representative image of adult (10 mo) MUT cerebellum stained with CC3 (green). No significant CC3 staining is observed at either age. (R,S) DAPI and Calbindin co-stained images of P and Q, respectively. Scale bars for K-S are 50 µm. (T) Graph depicting the number of Calbindin+ somas per image, a marker for Purkinje cells. No difference is seen between genotypes at either age (P42 WT 20.50 ± 0.53, P42 MUT 20.67 ± 0.59, 10mo WT 21.42 ± 0.85, 10mo MUT 22.63 ± 0.74, H=4.891, p=0.1799). (U) Representative image of adolescent (P42) WT hippocampus stained with cleaved caspase-3 (CC3, green). (V) Representative image of adolescent (P42) MUT hippocampus stained with cleaved caspase-3 (CC3, green). (W,X) DAPI co-stained images of U and V, respectively. (Y) Anatomical representation of mouse hippocampus CA1, adapted from the Allen Brain Atlas (Oh et al., 2014). Red region highlights area used for imaging. (Z) Representative image of adult (10 mo) WT hippocampus stained with cleaved caspase-3 (CC3, green). (AA) Representative image of adult (10 mo) MUT hippocampus stained with cleaved caspase-3 (CC3, green). (BB and CC) DAPI co-stained images of Z and AA, respectively. (DD) Graph of the normalized % of DAPI+ nuclei that are positive for CC3 per image. Very little CC3 staining is seen at either age, regardless of genotype (P42 WT 0.21±0.11%, P42 MUT 0.15±0.11%, 10mo WT 0.81±0.28%, 10mo MUT 4.13±0.96%, H=20.27, p=0.0001). Data obtained from four animals per condition and reported as mean ± standard error of the mean (SEM), with error bars as SEM. Kruskal–Wallis test (J, T, and DD).

![Figure 6—figure supplement 2.](https://cdn.elifesciences.org/articles/61590/elife-61590-fig6-figsupp2-v1.jpg)

**Figure 6—figure supplement 2.:** (A) Representative 10x image of tyrosine hydroxylase (TH) staining in the substantia nigra pars compacta (SNpc) of an 8-month-old WT mouse. Scale bar is 50 µm. (B–D) Representative 40x image of WT SNpc, depicting tyrosine hydroxylase+ (TH+) dopaminergic cell bodies (B), NeuN+ neuronal marker (C), and their merged image (D). Scale bars are 15 µm. (E) Schematic representation of brain region analyzed, substantia nigra pars compacta, adapted from Allen Brain Atlas (Oh et al., 2014). (F) Representative 10x image of TH staining in the substantia nigra pars compacta (SNpc) of an 8-month-old MUT mouse. Scale bar is 50 µm. (G–I) Representative 40x image of MUT SNpc, depicting tyrosine hydroxylase+ (TH+) dopaminergic cell bodies (G), NeuN+ neuronal marker (H), and their merged image (I). Scale bars are 15 µm. (J) Graph depicting the mean number of TH+ neurons per 40x image reveals no difference between WT and MUT SNpc (8mo WT 30.5±1.78 cells, n=24 images, 8mo MUT 28.33 ± 1.77 cells, n=24 images; U=234, p=0.2695). (K) Representative 10x image of TH staining in the striatum of an 8-month-old WT mouse. Scale bar is 50 µm. (L–N) Representative 40x image of WT striatum depicting TH+ dopaminergic innervation (L), NeuN+ neuronal marker (M), and their merged image (N). Scale bars are 15 µm. (O) Schematic representation of brain region analyzed, striatum, adapted from Allen Brain Atlas (Oh et al., 2014). (P) Representative 10x image of TH staining in the striatum of an 8-month-old MUT mouse. Scale bar is 50 µm. (Q–S) Representative 40x image of MUT striatum depicting tyrosine hydroxylase+ (TH+) dopaminergic innervation (Q), NeuN+ neuronal marker (R), and their merged image (S). Scale bars are 15 µm. (T) Graph depicting the mean intensity of TH+ signal per 40x image reveals no significant difference between WT and MUT dopaminergic innervation (8mo WT 31.48 ± 0.97, n=24 images, 8mo MUT 31.80 ± 1.35, n=24 images; t41.82=0.1955, p=0.8459). Data obtained from three animals per condition and reported as mean ± standard error of the mean (SEM), with error bars as SEM. Mann–Whitney test (J) and two-tailed t-test (T).

To further examine the morphology of primary motor cortex neurons at a subcellular resolution, samples from age-matched 7-month-old WT and MUT mice (7mo, three animals each) were imaged by transmission electron microscopy (TEM). Strikingly, we observed large electron-dense inclusions in the cell bodies of MUT neurons (arrows, Figure 6L; pseudo-colored region, 6N). These dense structures were associated electron-lucent lipid-like inclusions (asterisk, Figure 6N), which supported the conclusion that these structures were lipofuscin accumulation at lysosomal residual bodies (Poët et al., 2006; Valdez et al., 2017; Yoshikawa et al., 2002). Lipofuscin is a by-product of lysosomal breakdown of lipids, proteins, and carbohydrates, which naturally accumulates over time in non-dividing cells such as neurons (Höhn and Grune, 2013; Moreno-García et al., 2018; Terman and Brunk, 1998). However, excessive lipofuscin accumulation is thought to be detrimental to cellular homeostasis by inhibiting lysosomal function and promoting oxidative stress, often leading to cell death (Brunk and Terman, 2002; Powell et al., 2005). As a result, elevated lipofuscin is considered a biomarker of neurodegenerative disorders, including Alzheimer’s disease, Parkinson’s disease, and neuronal ceroid lipofuscinoses (Moreno-García et al., 2018). Therefore, the marked increase in lipofuscin area and number seen in MUT electron micrographs (Figure 6O and P, respectively) is consistent with the increased abundance of lysosomal proteins observed by proteomics and likely reflects an increase in lysosomal breakdown of cellular material. Together these data indicate that SWIPP1019R results in pathological lysosomal function that could lead to neurodegeneration.

### SWIPP1019R mutant mice display persistent deficits in cued fear memory recall

To observe the functional consequences of the SWIPP1019R mutation, we next studied WT and MUT mouse behavior. Given that children with homozygous SWIPP1019R point mutations display intellectual disability (Ropers et al., 2011) and SWIPP1019R mutant mice exhibit endo-lysosomal disruptions implicated in neurodegenerative processes, behavior was assessed at two ages: adolescence (P40–50), and mid-late adulthood (5.5–6.5 mo). Interestingly, MUT mice performed equivalently to WT mice in episodic and working memory paradigms, including novel object recognition and Y-maze alternations (Figure 7—figure supplement 1). However, in a fear conditioning task, MUT mice displayed a significant deficit in cued fear memory (Figure 7). This task tests the ability of a mouse to associate an aversive event (a mild electric footshock) with a paired tone (Figure 7A). Freezing behavior of mice during tone presentation is attributed to hippocampal or amygdala-based fear memory processes (Goosens and Maren, 2001; Maren and Holt, 2000; Vazdarjanova and McGaugh, 1998). Forty-eight hours after exposure to the paired tone and footshock, MUT mice showed a significant decrease in conditioned freezing to tone presentation compared to their WT littermates (Figure 7B,C). To ensure that this difference was not due to altered sensory capacities of MUT mice, we measured the startle response of mice to both electric foot shock and presented tones. In line with intact sensation, MUT mice responded comparably to WT mice in these tests (Figure 7—figure supplement 2). These data demonstrate that although MUT mice perceive footshock sensations and auditory cues, it is their memory of these paired events that is significantly impaired. Additionally, this deficit in fear response was evident at both adolescence and adulthood (top panels, and bottom panels, respectively, Figure 7B and C). These changes are consistent with the hypothesis that SWIPP109R is the cause of cognitive impairments in humans.

![Figure 7.](https://cdn.elifesciences.org/articles/61590/elife-61590-fig7-v1.jpg)

**Figure 7.:** (A) Experimental fear conditioning paradigm. After acclimation to a conditioning chamber, mice received a mild aversive 0.4mA footshock paired with a 2900 Hz tone. 48 hr later, the mice were placed in a chamber with different tactile and visual cues. The mice acclimated for two minutes and then the 2900 Hz tone was played (no footshock) and freezing behavior was assessed. (B) Line graphs of WT and MUT freezing response during cued tone memory recall. Data represented as average freezing per genotype in 30 s time bins. The tone is presented after t=120 s, and remains on for 120 s (Tone ON). Two different cohorts of mice were used for age groups P42 (top) and 6.5mo (bottom). Two-way ANOVA analysis of average freezing during Pre-Tone and Tone periods reveal a Genotype x Time effect at P42 (WT n=10, MUT n=10, F1,18=4.944, p=0.0392) and 6.5mo (WT n=13, MUT n=11, F1,22=13.61, p=0.0013). (C) Graphs showing the average %time freezing per animal before and during tone presentation. Top: freezing is reduced by 20% in MUT adolescent mice compared to WT littermates (Pre-tone WT 16.5 ± 2.2%, n=10; Pre-tone MUT 13.0 ± 1.8%, n=10; t36=0.8569, p=0.6366; Tone WT 52.8 ± 3.8%, n=10; Tone MUT 38.0 ± 3.6%, n=10; t36=3.539, p=0.0023), Bottom: freezing is reduced by over 30% in MUT adult mice compared to WT littermates (Pre-tone WT 21.1 ± 2.7%, n=13; Pre-tone MUT 23.7±3.8%, n=11; t44=0.4675, p=0.8721; Tone WT 69.7 ± 4.3%, n=13; Tone MUT 53.1 ± 5.2%, n=11; t44=2.921, p=0.0109). Data reported as mean ± SEM, error bars are SEM. *p<0.05, **p<0.01, two-way ANOVAs (B) and Sidak’s post hoc analyses (C).

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/61590/elife-61590-fig7-figsupp1-v1.jpg)

**Figure 7—figure supplement 1.:** (A) Y-maze paradigm. Mice were placed in the center of the maze and allowed to explore all three arms freely for five minutes. Each arm had distinct visual cues. (B) Graph depicting the percent alternations achieved for each mouse at adolescence (WT 51.48 ± 2.47%, MUT 50.81 ± 2.19%, t24=0.2036, p=0.8404). (C) Graph depicting the percent alternations achieved for each mouse at adulthood (WT 56.12 ± 1.53%, MUT 57.93 ± 2.56%, t18=0.6074, p=0.5511). (D) Graphs of the number of direct revisits mice made to the arm they just explored reveal no difference between genotypes at adolescence (WT 2.64 ± 0.50, MUT 2.42 ± 0.42, t24=0.3482, p=0.7308). (E) Graphs of the number of direct revisits mice made at adulthood (WT 1.36 ± 0.33, MUT 1.42 ± 0.36, t24=0.1231, p=0.9031). (F) Similar to D-E, there were no differences in the number of indirect revisits (ex: arm A→ arm B→arm A) between genotypes at adolescence (WT 10.21 ± 1.03, MUT 12.00 ± 1.48, U=69, p=0.4515). (G) Indirect revisits at adulthood (WT 12.86 ± 1.26, MUT 15.17 ± 1.43, t23=1.211, p=0.2380). (H) There were no significant differences in total distance traveled at adolescence, suggesting that motor function did not affect Y-maze performance (WT 2401 ± 98.9 cm, MUT 2406 ± 121.0 cm, t22=0.03281, p=0.9741). (I) No difference in distanced traveled at adulthood (WT 2761 ± 111.6 cm, MUT 3124 ± 191.1 cm, t18=1.638, p=0.1189). (J) Novel object task. Mice first performed a 5 min trial in which they were placed in an arena with two identical objects and allowed to explore freely, while their behavior was tracked with video software. Mice were returned to their home cage and then re-introduced to the arena a half an hour later, where one of the objects had been replaced with a novel object, and their behavior was again tracked. Twenty-four hours later the same test was performed, but the novel object was replaced with another new object. (K) Graph depicting adolescent animals’ preference for the novel object during the three phases of the task, training (Train), short-term memory (STM), and long-term memory (LTM). No significant difference in object preference is seen between genotypes for any phase (Train WT −0.092 ± 0.065, Train MUT −0.123 ± 0.072, STM WT 0.488 ± 0.076, STM MUT 0.315 ± 0.094, LTM WT 0.479 ± 0.046, LTM MUT 0.373 ± 0.076, F1,22=1.840, p=0.1887). (L) Graph depicting adult animals’ preference for the novel object. (Train WT −0.066 ± 0.053, Train MUT −0.130 ± 0.089, STM WT 0.416 ± 0.060, STM MUT 0.274 ± 0.096, LTM WT 0.316 ± 0.059, LTM MUT 0.306 ± 0.050, F1,22=0.9735, p=0.3345). (M) Graph depicting the total amount of time (in seconds) adolescent animals spent exploring both objects in each phase of the task. No significant difference in exploration time was observed across genotypes, suggesting that genotype does not hinder object exploration (Train P44 WT 38.10 ± 2.45 s, Train P44 MUT 50.04 ± 5.44 s, STM P44 WT 55.02 ± 4.31 s, STM P44 MUT 63.60 ± 4.50 s, LTM P45 WT 46.75 ± 3.34 s, LTM P45 MUT 68.08 ± 7.54 s, F1,22=7.373, p=0.0126). (N) Graph depicting the total time adult animals spent exploring both objects in each the task (Train WT 39.10 ± 3.62 s, Train MUT 51.15 ± 4.91 s, STM WT 44.75 ± 4.87 s, STM MUT 49.56 ± 6.16 s, LTM WT 39.02 ± 5.29 s, LTM MUT 55.15 ± 7.34 s, F1,22=2.936, p=0.1007). For all Y-maze measures, WT n=14, MUT n=12. For all novel object measures, WT n=13, MUT n=11. Data reported as mean ± SEM, error bars are SEM. Two-tailed t-tests or Mann–Whitney U tests (B–I), two-way ANOVAs (K–N).

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/61590/elife-61590-fig7-figsupp2-v1.jpg)

**Figure 7—figure supplement 2.:** (A) Experimental fear conditioning scheme. After acclimation, mice received a mild aversive 0.4mA footshock paired with a 2900 Hz tone in a conditioning chamber. 24 hr later, the mice were placed back in the same chamber to assess freezing behavior (without footshock or tone). (B) Experimental startle response setup used to assess hearing and somatosensation. Mice were placed in a plexiglass tube atop a load cell that measured startle movements in response to stimuli. (C) Line graphs of WT and MUT freezing response during the contextual memory recall task. Data represented as average freezing per genotype in 30 s time bins. The task was performed with two different cohorts for the different ages, P42 (top) and 6.5mo (bottom). Top: no significant difference in freezing at P42 (Two-way repeated measure ANOVA, Genotype effect, F1,18=0.088, p=0.7698. Sidak’s post-hoc analysis, 30 s p=0.8388, 60 s p=0.9990, 90 s p=0.9964, 120 s p=0.3281), Bottom: no significant difference in freezing at 6.5mo (Two-way repeated measure ANOVA, Genotype effect, F1,22=3.723, p=0.0667. Sidak’s post-hoc analysis, 30 s p=0.8977, 60 s p=0.1636, 90 s p=0.9979, 120 s p=0.0037). (D) Graphs showing the average total freezing time per animal during context exposure. Top: no significant difference is seen between WT and MUT mice at P42 (WT 34.01 ± 6.32%, MUT 36.99 ± 7.81%, t17=2.985, p=0.7699). Bottom: no significant different is seen between genotypes at 6.5mo (WT 43.94 ± 6.00%, MUT 28.73 ± 4.80%, t21.6=1.980, p=0.0606). (E) Graphs of individual animals’ startle response to a 2900 Hz tone played at 80 dB. MUT mice were not significantly more reactive to the tone than WT at P50 (WT 25.96 ± 4.95, MUT 40.68 ± 5.05, U=35, p=0.2799), or at 6.5mo (WT 14.07 ± 3.27, MUT 14.85 ± 1.49, U=47, p=0.2768). (F) Graphs of individual animals’ startle response to a 0.4mA footshock. No significant difference observed between genotypes at either age (P55 WT 1527 ± 215.7, P55 MUT 1996 ± 51.0, U=28.50, p=0.0542; 6.5mo WT 1545 ± 179.5, 6.5mo MUT 1817 ± 119.1, U=47, p=0.2360). Startle response reported in arbitrary units (AU). For all adolescent measures: WT n=10, MUT n=10. For adult freezing measures: WT n=13, MUT n=11. For adult startle responses: WT n=13, MUT n=10. Data reported as mean ± SEM, error bars are SEM.*p<0.05, **p<0.01, two-way repeated measure ANOVAs (C), two-tailed t-tests (D), and Mann–Whitney U tests (E–F).

### SWIPP1019R mutant mice exhibit surprising motor deficits that are confirmed in human patients

Because SWIPP1019R results in endo-lysosomal pathology consistent with neurodegenerative disorders in the motor cortex, we next analyzed motor function of the mice over time. First, we tested the ability of WT and MUT mice to remain on a rotating rod for 5 min (Rotarod, Figure 8A–C). At both adolescence and adulthood, MUT mice performed markedly worse than WT littermate controls (Figure 8C). Mouse performance was not significantly different across trials, which suggested that this difference in retention time was not due to progressive fatigue, but more likely due to an overall difference in motor control (Mann and Chesselet, 2015).

![Figure 8.](https://cdn.elifesciences.org/articles/61590/elife-61590-fig8-v1.jpg)

**Figure 8.:** (A) Rotarod experimental setup. Mice walked atop a rod rotating at 32 rpm for 5 min, and the duration of time they remained on the rod before falling was recorded. (B) Line graph of average duration animals remained on the rod per genotype across four trials, with an inter-trial interval of 40 min. The same cohort of animals was tested at two different ages, P45 (top) and 5.5 months (bottom). Genotype had a significant effect on task performance at both ages (top, P45: genotype effect, F1,25=7.821, p=0.0098. bottom, 5.5mo: genotype effect, F1,23=7.573, p=0.0114). (C) Graphs showing the average duration each animal remained on the rod across trials. At both ages, the MUT mice exhibited an almost 50% reduction in their ability to remain on the rod (top, P45: WT 169.9 ± 25.7 s, MUT 83.8 ± 15.9 s, U=35, p=0.0054; bottom, 5.5mo: WT 135.9 ± 20.9 s, MUT 66.7 ± 9.5 s, t18=3.011, p=0.0075). (D) TreadScan task. Mice walked on a treadmill for 20 s while their gate was captured with a high-speed camera. Diagrams of gait parameters measured in (E–G) are shown below the TreadScan apparatus. (E) Average swing time per stride for hindlimbs. At P45 (top), there is no significant difference in rear swing time (WT 156.2 ± 22.4 ms, MUT 132.3 ± 19.6 ms, U=83, p=0.7203). At 5.5mo (bottom), MUT mice display significantly longer rear swing time (WT 140 ± 6.2 ms, MUT 252.0 ± 21.6 ms, t12=4.988, p=0.0003). (F) Average stride length for hindlimbs. At P45 (top), there is no significant difference in stride length (WT 62.3 ± 2.0 mm, MUT 60.5 ± 2.1 mm, U=75, p=0.4583). At 5.5mo (bottom), MUT mice take significantly longer strides with their hindlimbs (WT 60.8 ± 0.8 mm, MUT 73.6 ± 2.7 mm, t11.7=4.547, p=0.0007). (G) Average homologous coupling for front and rear limbs. Homologous coupling is 0.5 when the left and right feet are completely out of phase. At P45 (top), WT and MUT mice exhibit normal homologous coupling (WT 0.48 ± 0.005, MUT 0.48 ± 0.004, U=76.5, p=0.4920). At 5.5 mo (bottom), MUT mice display decreased homologous coupling, suggestive of abnormal gait symmetry (WT 0.48 ± 0.003, MUT 0.46 ± 0.004, t18.8=3.715, p=0.0015). At P45: n=14 WT, n=13 MUT; At 5.5mo: n=14 WT, n=11 MUT. (H) Table of motor findings in clinical exam of human patients with the homozygous SWIPP1019R mutation. All patients exhibit motor dysfunction (+ = symptom present). Data reported as mean ± SEM, error bars are SEM. *p<0.05, **p<0.01, ***p<0.001, ****p<0.0001, two-way repeated measure ANOVAs (B), Mann–Whitney U tests and two-tailed t-tests (C–G).

![Figure 8—figure supplement 1.](https://cdn.elifesciences.org/articles/61590/elife-61590-fig8-figsupp1-v1.jpg)

**Figure 8—figure supplement 1.:** (A) Graph of average swing time per stride for front limbs. At P45 (top), there is no significant difference in front swing time (WT 177.5 ± 10.9 ms, MUT 175.3 ± 8.7 ms, t24=0.1569, p=0.8766). At 5.5 mo (bottom), MUT mice take significantly longer to swing their forelimbs (WT 178.6 ± 6.2 ms, MUT 206.3 ± 7.2 ms, t21.4=2.927, p=0.0079). (B) Graph of average stride length for front limbs. At P45 (top), there is no difference in WT and MUT stride length (WT 57.0 ± 0.9 mm, MUT 59.2 ± 1.4 mm, U=68, p=0.2800). At 5.5mo (bottom), MUT mice take significantly longer strides with their forelimbs (WT 60.0 ± 0.6 mm, MUT 63.7 ± 0.9 mm, t17=3.545, p=0.0024). (C) Graph of average homolateral coupling, the fraction of a reference foot’s stride when its ipsilateral foot starts its stride. At P45, there is no significant difference in homolateral coupling (WT 0.48 ± 0.005, MUT 0.48 ± 0.004, U=90, p=0.9713), but at 5.5mo, MUT mice display decreased homolateral coupling (WT 0.48 ± 0.002, MUT 0.45 ± 0.005, t13.5=3.469, p=0.0039). (D) Graph of average track width between front limbs. At P45 (top), there is a significantly narrower front track width in MUT compared to WT (WT 16.99 ± 0.15 mm, MUT 15.12 ± 0.33 mm, t17=5.192, p<0.0001). This difference persists into adulthood at 5.5mo (WT 19.36 ± 0.23 mm, MUT 16.74 ± 0.46 mm, t15=5.055, p=0.0001). (E) Graph of average track width between rear limbs. At P45 (top), there is no difference in WT and MUT rear track widths (WT 29.58 ± 0.51 mm, MUT 28.77 ± 0.36 mm, t23=1.292, p=0.2091). At 5.5mo (bottom), mutants display significantly narrower rear track widths (WT 32.59 ± 0.34 mm, MUT 30.01 ± 0.46 mm, t19.4=4.502, p=0.0002). For P45 measures: WT n=14, MUT n=13; for 5.5mo measures: WT n=14, MUT n=11. Data reported as mean ± SEM, error bars are SEM. **p<0.01, ***p<0.001, ****p<0.0001, two-tailed t-tests or Mann–Whitney U tests.

To study the animals’ movement at a finer scale, the gait of WT and MUT mice was also analyzed using a TreadScan system containing a high-speed camera coupled with a transparent treadmill (Figure 8D; Beare et al., 2009). Interestingly, while gait parameters of the mice were largely indistinguishable across genotypes at adolescence, a striking difference was seen when the same mice were aged to adulthood (Figure 8E–G). In particular, MUT mice took slower (Figure 8E), longer strides (Figure 8F), stepping closer to the midline of their body (track width, Figure 8—figure supplement 1), and their gait symmetry was altered, so that their strides were no longer perfectly out of phase (out of phase=0.5, Figure 8G). While these differences were most pronounced in the rear limbs (as depicted in Figure 8E–G), the same trends were present in front limbs (Figure 8—figure supplement 1). These findings demonstrate that SWIPP1019R results in progressive motor function decline that was detectable by the rotarod task at adolescence, but which became more prominent with age, as both gait and strength functions deteriorated.

These marked motor findings prompted us to re-evaluate the original reports of human SWIPP1019R patients (Ropers et al., 2011). While developmental delay or learning difficulties were the primary impetus for medical evaluation, all patients also exhibited motor symptoms (mean age=10.4 years old, Figure 8H). The patients’ movements were described as ‘clumsy’ with notable fine motor difficulties, dysmetria, dysdiadochokinesia, and mild dysarthria on clinical exam (Figure 8H). Recent communication with the parents of these patients, who are now an average of 21 years old, revealed no notable symptom exacerbation. It is therefore possible that the SWIPP1019R mouse model either exhibits differences from human patients or may predict future disease progression for these individuals, given that we observed significant worsening at 5–6 months old in mice (which is thought to be equivalent to ~30–35 years old in humans) (Dutta and Sengupta, 2016; Zhang et al., 2019).

## Discussion

Taken together, the data presented here support a mechanistic model whereby SWIPP1019R causes a loss of WASH complex function, resulting in endo-lysosomal disruption and accumulation of neurodegenerative markers, such as upregulation of unfolded protein response modulators and lysosomal enzymes, as well as build-up of lipofuscin and cleaved caspase-3 over time. To our knowledge, this study provides the first mechanistic evidence of WASH complex impairment having direct and indirect organellar effects that lead to cognitive deficits and progressive motor impairments (Figure 9).

![Figure 9.](https://cdn.elifesciences.org/articles/61590/elife-61590-fig9-v1.jpg)

**Figure 9.:** (A) Wild-type WASH function in mouse brain. Under normal conditions, the WASH complex interacts with many endosomal proteins and cytoskeletal regulators, such as the Arp2/3 complex. These interactions enable restructuring of the endosome surface (actin in gray) and allow for cargo segregation and scission of vesicles. Substrates are transported to the late endosome for lysosomal degradation, to the Golgi network for modification, or to the cell surface for recycling. (B) Loss of WASH function leads to increased lysosomal degradation in mouse brain. Destabilization of the WASH complex leads to enlarged endosomes and lysosomes, with increased substrate accumulation at the lysosome. This suggests an increase in flux through the endo-lysosomal pathway, possibly as a result of mis-localized endosomal substrates. (C) Wild-type mice exhibit normal motor function. (D) SWIPP1019R mutant mice display progressive motor dysfunction in association with these subcellular alterations.

Using in vivo proximity-based proteomics in wild-type mouse brain, we found that the WASH complex closely interacts with the CCC (COMMD9 and CCDC93) and Retriever (VPS35L) cargo selective complexes (Bartuzi et al., 2016; Singla et al., 2019). Interestingly, we did not find significant enrichment of the Retromer sorting complex, a well-known WASH interactor (Figure 1), which may be the by-product of using WASH1 rather than another WASH subunit for BioID tagging. Future studies on these protein candidates may clarify how these molecular interactions occur and influence WASH function in mouse brain.

These data are consistent with our spatial proteomics analyses of SWIPP1019R mutant brain, which clustered the WASH, CCC, Retriever, and CORVET/HOPS complexes together in M38 (Figure 3) and the Retromer complex in a different endosomal-enriched module, M22 (Figure 4—figure supplement 1A). Spatial proteomics analyses also revealed that disruption of these WASH–CCC–Retriever–CORVET/HOPS interactions may have multiple downstream effects on the endosomal machinery, since both endosomal-enriched modules exhibited significant decrease in SWIPP1019R brain (M38 and M22, Figure 3 and Figure 4—figure supplement 1A). These modules include corresponding decreases in the abundance of endosomal proteins including Retromer subunits (VPS29, VPS26B, and VPS35; M22), associated sorting nexins (SNX27; M22), known WASH interactors (FKBP15; M38), and cargos (e.g. LRP1; M22) (Figure 3 and Figure 4—figure supplement 1; Del Olmo et al., 2019; Farfán et al., 2013; Fedoseienko et al., 2018; Halff et al., 2019; Harbour et al., 2012; McNally et al., 2017; Pan et al., 2010; Ye et al., 2020; Zimprich et al., 2011). While previous studies have indicated that Retromer and CCC influence the endosomal localization of WASH (Harbour et al., 2012; Phillips-Krawczak et al., 2015; Singla et al., 2019), our findings demonstrate both protein- and module-level decreases in abundance of these proteins, pointing to a cascade of endosomal dysfunction. Future studies defining the hierarchical interplay between the WASH, Retromer, Retriever, and CCC complexes in neurons could provide clarity on how these mechanisms are organized.

Of note, some of the lysosomal enzymes with elevated levels in MUT brain (GRN, HEXA, and GLB1 – M36; Figure 4) are also implicated in lysosomal storage disorders, where they generally have decreased, rather than increased, function or expression (Boles and Proia, 1995; Regier and Tifft, 1993; Smith et al., 2012; Ward et al., 2017). This divergent lysosomal effect in our SWIPP1019R model compared to other degenerative models could represent either a distinct endo-lysosomal disruption that culminates in similar cellular pathology or a transient compensatory state that may ultimately lead to declined lysosomal function in SWIPP1019R neurons. We speculate that loss of WASH function in our mutant mouse model may lead to increased accumulation of cargo and associated machinery at early endosomes (as seen in Figure 5, enlarged EEA1+ puncta), eventually overburdening early endosomal vesicles and triggering transition to late endosomes for subsequent fusion with degradative lysosomes (Figure 9). This would effectively increase delivery of endosomal substrates to the lysosome compared to baseline, resulting in enlarged, overloaded lysosomal structures, and elevated demand for degradative enzymes. For example, since mutant neurons display increased abundance of a lysosomal module (Figure 4), and larger lysosomal structures (Figures 5 and 6), they may require higher quantities of progranulin (GRN, M36; Figure 4) for sufficient lysosomal acidification (Tanaka et al., 2017).

Our findings that SWIPP1019R results in reduced WASH complex stability and function, which may ultimately drive lysosomal dysfunction, are supported by studies in non-mammalian cells. For example, expression of a dominant-negative form of WASH1 in amoebae impairs recycling of lysosomal V-ATPases (Carnell et al., 2011) and loss of WASH in Drosophila plasmocytes affects lysosomal acidification (Gomez et al., 2012; Nagel et al., 2017; Zech et al., 2011). Moreover, mouse embryonic fibroblasts lacking WASH1 display abnormal lysosomal morphologies, akin to the structures we observed in cultured SWIPP1019R MUT neurons (Gomez et al., 2012). Consistent with the idea that WASH regulates lysosomal V-ATPase function either directly or indirectly, we observed a significant decrease in the overall abundance of module M35, a module containing 6 of the 13 components of the vacuolar-associated ATPase complex subunits (CORUM: ATP6V1A, ATP6V1E1, ATP6V0C, ATP6V1F, ATP6V1C1, and ATP6V0A1; Supplementary files 3–4). The overall significant decrease in this module resonates with previous studies linking WASH to V-ATPase acidification of lysosomes.

In addition to lysosomal dysfunction, endoplasmic reticulum (ER) stress is commonly observed in neurodegenerative states, where accumulation of misfolded proteins disrupts cellular proteostasis (Cai et al., 2016; Hetz and Saxena, 2017; Montibeller and de Belleroche, 2018). This cellular strain triggers the adaptive unfolded protein response (UPR), which attempts to restore cellular homeostasis by increasing the cell’s capacity to retain misfolded proteins within the ER, remedy misfolded substrates, and trigger degradation of persistently misfolded species. Involved in this process are ER chaperones that we identified as increased in SWIPP1019R mutant brain including BiP (HSPA5), calreticulin (CALR), calnexin (CANX), and the protein disulfide isomerase family members (PDIA1, PDIA4, PDIA6; M6 Figure 4—figure supplement 1C–D; Garcia-Huerta et al., 2016). Many of these proteins were identified in the ER protein module found to be significantly altered in MUT mouse brain (M6), supporting a network-level change in the ER stress response (Figure 4—figure supplement 1D). One notable exception to this trend was the chaperone endoplasmin (HSP90B1, M22), which exhibited significantly decreased abundance in SWIPP1019R mutant brain (Supplementary file 2). This is surprising given that endoplasmin has been shown to coordinate with BiP in protein folding (Sun et al., 2019); however, it may highlight a possible compensatory mechanism. Additionally, prolonged UPR can stimulate autophagic pathways in neurons, where misfolded substrates are delivered to the lysosome for degradation (Cai et al., 2016). These data highlight a potential pathogenic relationship between ER and endo-lysosomal disturbances as an exciting avenue for future research.

Strikingly, we observed modules enriched for resident proteins corresponding to all 10 of the major subcellular compartments mapped by Geladaki et al., 2019: nucleus, mitochondria, golgi apparatus, ER, peroxisome, proteasome, plasma membrane, lysosome, cytoplasm, and ribosome; Figure 3—figure supplement 5. The greatest dysregulations, as quantified by log2Fold-Change between genotypes, were in lysosomal, endosomal, ER, and synaptic modules, supporting the hypothesis that SWIPP1019R primarily results in disrupted endo-lysosomal trafficking. While analysis of these dysregulated modules informs the pathobiology of SWIPP1019R, our spatial proteomics approach also identified numerous biologically cohesive modules, which remained unaltered (Figure 3—figure supplement 5). Given that many of these modules contained proteins of unknown function, we anticipate that future analyses of these modules and their protein constituents have great potential to inform our understanding of protein networks and their influence on neuronal cell biology.

It has become clear that preservation of the endo-lysosomal system is critical to neuronal function, as mutations in mediators of this process are implicated in neurological diseases such as Parkinson’s disease, Huntington’s disease, Alzheimer’s disease, frontotemporal dementia, neuronal ceroid lipofuscinoses (NCLs), and hereditary spastic paraplegia (Baker et al., 2006; Connor-Robson et al., 2019; Edvardson et al., 2012; Follett et al., 2019; Harold et al., 2009; Mukherjee et al., 2019; Pal et al., 2006; International Parkinsonism Genetics Network et al., 2013; Seshadri et al., 2010; Tachibana et al., 2019; Valdmanis et al., 2007). These genetic links to predominantly neurodegenerative conditions have supported the proposition that loss of endo-lysosomal integrity can have compounding effects over time and contribute to progressive disease pathologies. In particular, mutations associated with Parkinson’s disease have been found in a close endosomal interactor of the WASH complex – the retromer protein VPS35 (VPS35D620N and VPS35R524W) – and have been linked to pathological α-synuclein aggregation in vitro (Chen et al., 2019; Follett et al., 2014; Tang et al., 2015). While α-synuclein (SNCA) was highly enriched in our WASH1-BioID assay in WT brain (Figure 1), its protein abundance was not found to be significantly different in SWIPP1019R mutant brain fractions compared to WT in our TMT spatial proteomic analysis (Supplementary file 2).

In addition, unlike many Parkinson’s disease models, which display specific deficits in dopaminergic cells, we did not observe any dopaminergic cell-specific changes in SWIPP1019R brain (Figure 6—figure supplement 2). This suggests that the motor pathology of SWIPP1019R mice diverges from that of α-synuclein-driven Parkinson’s mouse models. The more parsimonious explanation may be that α-synuclein’s enrichment in the WASH1-BioID proteome results from its colocalization with the WASH complex at the endosome and throughout the endo-vesicular system in neurons (Boassa et al., 2013; Bodain, 1965; Burre et al., 2010; Iwai et al., 1995; Lee et al., 2005).

While our SWIPP1019R model appears to diverge in pathology from Parkinson’s disease models, it does exhibit parallels to NCL models. NCLs are lysosomal storage disorders primarily found in children rather than adults, with heterogenous presentations and multigenic causations (Mukherjee et al., 2019). The majority of genes implicated in NCLs affect lysosomal enzymatic function or transport of proteins to the lysosome (Mukherjee et al., 2019; Poët et al., 2006; Ramirez-Montealegre and Pearce, 2005; Yoshikawa et al., 2002). Most patients present with marked neurological impairments, such as learning disabilities, motor abnormalities, vision loss, and seizures, and have the unifying feature of lysosomal lipofuscin accumulation upon pathological examination (Mukherjee et al., 2019). While the human SWIPP1019R mutation has not been classified as an NCL (Ropers et al., 2011), findings from our mutant mouse model suggest that loss of WASH complex function leads to phenotypes bearing strong resemblance to NCLs, including lipofuscin accumulation (Figures 5–8). As a result, our mouse model could provide the opportunity to study these pathologies at a mechanistic level, while also enabling preclinical development of treatments for their human counterparts.

Currently, there is an urgent need for greater mechanistic investigations of neurodegenerative disorders, particularly in the domain of endo-lysosomal trafficking. Despite the continual increase in identification of human disease-associated genes, our molecular understanding of how their protein equivalents function and contribute to pathogenesis remains limited. Here we employ a system-level analysis of proteomic datasets to uncover biological perturbations linked to SWIPP1019R. We demonstrate the power of combining in vivo proteomics and system network analyses with in vitro and in vivo functional studies to uncover relationships between genetic mutations and molecular disease pathologies. Applying this platform to study organellar dysfunction in other neurodegenerative and neurodevelopmental disorders may facilitate the identification of convergent disease pathways driving brain disorders.

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
      <td>Gene (Homo sapiens)</td>
      <td>WASHC4</td>
      <td>GenBank</td>
      <td>Gene ID: 23325</td>
      <td>Aka SWIP</td>
    </tr>
    <tr>
      <td>Gene (Mus musculus)</td>
      <td>Washc4</td>
      <td>Ensembl</td>
      <td>ENSMUSG00000034560</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Mus musculus)</td>
      <td>SWIPP1019R</td>
      <td>This paper, Duke Transgenic Mouse Facility</td>
      <td>ENSMUSG00000034560</td>
      <td>Mouse line maintained by Soderling lab</td>
    </tr>
    <tr>
      <td>Strain, strain background (Mus musculus)</td>
      <td>B6SJLF1/J</td>
      <td>Jackson Laboratories</td>
      <td>Cat# 100012 RRID:IMSR_JAX:100012</td>
      <td></td>
    </tr>
    <tr>
      <td>Strain, strain background (Mus musculus)</td>
      <td>C57BL/6J</td>
      <td>Jackson Laboratories</td>
      <td>Cat# 000664 RRID:IMSR_JAX:000664</td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pmCAG-SWIP-WT-HA (plasmid)</td>
      <td>This paper</td>
      <td>SWIP-WT</td>
      <td>AAV construct to transfect and express the recombinant DNA Sequence</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pmCAG-SWIP-MUT-HA (plasmid)</td>
      <td>This paper</td>
      <td>SWIP-MUT</td>
      <td>AAV construct to transfect and express the recombinant DNA Sequence</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>phSyn1-WASH1-BioID2-HA (plasmid)</td>
      <td>This paper</td>
      <td>WASH1-BioID2</td>
      <td>Transduced AAV construct Sequence</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>phSyn1- solubleBioID2-HA (plasmid)</td>
      <td>This paper</td>
      <td>SolubleBioID2 control</td>
      <td>Transduced AAV construct Sequence</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pAd-DeltaF6</td>
      <td>Addgene</td>
      <td>pAd-DeltaF6</td>
      <td>Helper plasmid for AAV2/9 viral preparation Sequence</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>pAAV2/9</td>
      <td>Addgene</td>
      <td>pAAV2/9</td>
      <td>Viral capsid Sequence</td>
    </tr>
    <tr>
      <td>Cell line (Mus musculus)</td>
      <td>Primary mouse cortical cultures</td>
      <td>This paper</td>
      <td>SWIP WT, SWIPP1019RMUT neurons</td>
      <td>Freshly isolated from wild-type or SWIPP1019R P0 mouse brains</td>
    </tr>
    <tr>
      <td>Cell line (Homo sapiens)</td>
      <td>Human Embryonic Kidney 293 T cells</td>
      <td>Duke Cell Culture Facility</td>
      <td>ATTC Cat# CRL-11268 RRID:CVCL_1926</td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Washc4 CRISPR sgRNA</td>
      <td>This paper</td>
      <td>Oligonucleotide sequence</td>
      <td>N20+ PAM sequence targeting mouse Washc4 gene for introducing C/G mutation 5′ttgagaatactcacaagagg agg3′</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Washc4_F repair</td>
      <td>This paper</td>
      <td>Forward repair oligonucleotide</td>
      <td>Forward strand of the repair oligo used to introduce C/G mutation into mouse Washc4 gene 5′atttcgaaggccaaagaatatacatctccgaaatttctatatcattgttcgtcctcttgtgagtattctcaaaactagaagtgagttattgatgggtgttaatacagattcagtttccataaagca3′</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Washc4_R repair</td>
      <td>This paper</td>
      <td>Reverse repair oligonucleotide</td>
      <td>Reverse strand of the repair oligo used to introduce C/G mutation into mouse Washc4 gene 5′tgctttatggaaactgaatctgtattaacacccatcaataactcacttctagttttgagaatactcacaagaggacgaacaatgatatagaaatttcggagatgtatattctttggccttcgaaat3′</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Washc4_F mutagenesis</td>
      <td>This paper</td>
      <td>Forward primer</td>
      <td>Washc4 C/G mutagenesis forward primer 5′ctacaaagttgagggtcagacggggaacaattatatagaaa3′</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Washc4_R mutagenesis</td>
      <td>This paper</td>
      <td>Reverse primer</td>
      <td>Washc4 C/G mutagenesis reverse primer 5′tttctatataattgttccccgtctgaccctcaactttgtag3′</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Washc4_F genotyping</td>
      <td>This paper</td>
      <td>Forward primer</td>
      <td>Washc4 forward primer for genotyping SWIPP1019R mice 5′tgcttgtagatgtttttcct3′</td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>Washc4_R genotyping</td>
      <td>This paper</td>
      <td>Reverse primer</td>
      <td>Washc4 reverse primer for genotyping SWIPP1019R mice 5′gttaacatgatcctatggcg3′</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-human WASH1 (C-terminal, rabbit monoclonal)</td>
      <td>Sigma Aldrich</td>
      <td>Cat# SAB42200373</td>
      <td>WB (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-human Strumpellin (rabbit polyclonal)</td>
      <td>Santa Cruz</td>
      <td>Cat# sc-87442 RRID:AB_2234159</td>
      <td>WB (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-human EEA1 (rabbit monoclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>Clone# C45B10 Cat# 3288 RRID:AB_2096811</td>
      <td>WB (1:1500) ICC (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-human LAMP1 (rabbit monoclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>Clone# C54H11 Cat# 3243 RRID:AB_2134478</td>
      <td>WB (1:2000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-human Beta Tubulin III (mouse monoclonal)</td>
      <td>Sigma Aldrich</td>
      <td>Clone# SDL.3D10 Cat# T8660 RRID:AB_477590</td>
      <td>WB (1:10,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-human HA (mouse monoclonal)</td>
      <td>BioLegend</td>
      <td>Clone# 16B12 Cat# MMS-101P RRID:AB_10064068</td>
      <td>WB (1:5000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-mouse Cathepsin D (rat monoclonal)</td>
      <td>Novus Biologicals</td>
      <td>Clone# 204712 Cat# MAB1029 RRID:AB_2292411</td>
      <td>ICC (1:250)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-human MAP2 (guinea pig polyclonal)</td>
      <td>Synaptic Systems</td>
      <td>Cat# 188004 RRID:AB_2138181</td>
      <td>ICC (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-human Cleaved Caspase-3 (rabbit polyclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>Specificity Asp175 Cat#9661 RRID:AB_2341188</td>
      <td>IHC (1:2000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-human Calbindin (mouse monoclonal)</td>
      <td>Sigma Aldrich</td>
      <td>Clone# CB-955 Cat# C9848 RRID:AB_476894</td>
      <td>IHC (1:2000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-human HA (rat monoclonal)</td>
      <td>Sigma Aldrich</td>
      <td>Clone# 3F10 Cat# 11867423001 RRID:AB_390918</td>
      <td>IHC (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-human Bassoon (mouse monoclonal)</td>
      <td>Abcam</td>
      <td>Clone# SAP7F407 Cat# ab82958 RRID:AB_1860018</td>
      <td>IHC (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-human Homer1 (rabbit polyclonal)</td>
      <td>Synaptic Systems</td>
      <td>Cat# 160002 RRID:AB_2120990</td>
      <td>IHC (1:500)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-human Tyrosine Hydroxylase (chicken polyclonal)</td>
      <td>Abcam</td>
      <td>Cat# ab76442 RRID:AB_1524535</td>
      <td>IHC (1:1000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-human NeuN (mouse monoclonal)</td>
      <td>Abcam</td>
      <td>Clone# 1B7 Cat# ab104224 RRID:AB_10711040</td>
      <td>IHC (1:1000)</td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>TMTpro 16plex Label Reagent</td>
      <td>Thermo Fisher</td>
      <td>Cat# A44520</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>NeutrAvidin Agarose Resins</td>
      <td>Thermo Fisher</td>
      <td>Cat# 29201</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>S-Trap Binding Buffer</td>
      <td>Profiti</td>
      <td>Cat# K02-micro-10</td>
      <td></td>
    </tr>
    <tr>
      <td>Commercial assay or kit</td>
      <td>QuikChange XL Site-Directed Mutagenesis Kit</td>
      <td>Agilent</td>
      <td>Cat# 200517</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Courtland et al., source code</td>
      <td>GitHub</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>MSstatsTMT</td>
      <td>GitHub</td>
      <td></td>
      <td>PubMed</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>leidenalg Python Library</td>
      <td>conda</td>
      <td></td>
      <td>Version 0.8.1</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Cytoscape</td>
      <td>https://cytoscape.org/</td>
      <td>RRID:SCR_003032</td>
      <td>Version 3.7.2</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Imaris</td>
      <td>Oxford Instruments</td>
      <td>RRID:SCR_007370</td>
      <td>Version 9.2.0</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Zen</td>
      <td>Zeiss</td>
      <td>RRID:SCR_018163</td>
      <td>Version 2.3</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Fiji</td>
      <td>https://fiji.sc/</td>
      <td>RRID:SCR_002285</td>
      <td>Version 2.0.0-rc-69/1.52 p</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GraphPad Prism</td>
      <td>GraphPad Software</td>
      <td>RRID:SCR_002798</td>
      <td>Version 8.0</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Proteome Discoverer</td>
      <td>Thermo Fisher</td>
      <td>RRID:SCR_014477</td>
      <td>Versions 2.2 and 2.4</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>TreadScan NeurodegenScanSuite</td>
      <td>CleverSysInc</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>EthoVision XT</td>
      <td>Noldus Information Technology</td>
      <td>RRID:SCR_000441</td>
      <td>Version 11.0</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Rotarod apparatus for mouse</td>
      <td>Med Associates</td>
      <td>Cat# ENV-575M</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Fear conditioning chamber</td>
      <td>Med Associates</td>
      <td>Cat# VFC-008-LP</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>FreezeScan software</td>
      <td>CleverSysInc</td>
      <td>RRID:SCR_014495</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Startle reflex chamber and software</td>
      <td>Med Associates</td>
      <td>Cat# MED-ASR-PRO1</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Geladaki et al.’s, LOPIT-DC protocol</td>
      <td>PubMed</td>
      <td>PMCID:PMC6338729</td>
      <td>Subcellular fractionation protocol</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Orbitrap Fusion Lumos Tribrid Mass Spectrometer</td>
      <td>Duke Proteomics and Metabolomics Shared Resource</td>
      <td></td>
      <td>Mass spectrometer used for spatial proteomics</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Thermo QExactive HF-X Mass Spectrometer</td>
      <td>Duke Proteomics and Metabolomics Shared Resource</td>
      <td></td>
      <td>Mass spectrometer used for iBioID</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Zeiss 710 LSM confocal microscope</td>
      <td>Duke Light Microscopy Core Facility (LCMF)</td>
      <td>RRID:SCR_018063</td>
      <td>Confocal microscope used for image acquisition of ICC and IHC samples</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Reichert Ultracut E Microtome</td>
      <td>Duke Department of Pathology</td>
      <td></td>
      <td>Microtome used to prepare TEM samples</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Phillips CM12 Electron Microscope</td>
      <td>Duke Department of Pathology</td>
      <td></td>
      <td>Transmission electron microscope used for TEM image acquisition</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Beckman XL-90 Centrifuge and Ti-70 rotor</td>
      <td>Duke Department of Cell Biology</td>
      <td></td>
      <td>Ultracentrifuge used for AAV virus preparation</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Beckman TLA-100 Ultracentrifuge and TLA-55 rotor</td>
      <td>Duke Department of Cell Biology</td>
      <td></td>
      <td>Ultracentrifuge used for spatial proteomics sample preparation</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>DAPI stain</td>
      <td>Thermo Fisher</td>
      <td>Cat# D1306 RRID:AB_2629482</td>
      <td>(1 µg/mL)</td>
    </tr>
  </tbody>
</table>

### Animals

We generated Washc4 mutant (SWIPP1019R) mice in collaboration with the Duke Transgenic Core Facility to mimic the de novo human variant at amino acid 1019 of human WASHC4. A CRISPR-induced CCT>CGT point mutation was introduced into exon 29 of Washc4. Fifty nanograms per microliter of the sgRNA (5′-ttgagaatactcacaagaggagg-3′), 100 ng/µL Cas9 mRNA, and 100 ng/µL of a repair oligonucleotide containing the C>G mutation were injected into the cytoplasm of B6SJLF1/J mouse embryos (Jax #100012) (see Key Resources Table for the sequence of the repair oligonucleotide). Mice with germline transmission were then backcrossed into a C57BL/6J background (Jax #000664). At least five backcrosses were obtained before animals were used for behavior. We bred heterozygous SWIPP1019R mice together to obtain age-matched mutant and wild-type genotypes for cell culture and behavioral experiments. Genetic sequencing was used to screen for germline transmission of the C>G point mutation (FOR: 5′-tgcttgtagatgtttttcct-3′, REV: 5′-gttaacatgatcctatggcg-3′). All mice were housed in the Duke University′s Division of Laboratory Animal Resources or Behavioral Core facilities at two to five animals per cage on a 14:10 hr light:dark cycle. All experiments were conducted with a protocol approved by the Duke University Institutional Animal Care and Use Committee in accordance with NIH guidelines.

### Human subjects

We retrospectively analyzed clinical findings from seven children with homozygous WASHC4c.3056C>G mutations (obtained by Dr. Rajab in 2010 at the Royal Hospital, Muscat, Oman). The original report of these human subjects and parental consent for data use can be found in Ropers et al., 2011.

### Cell lines

HEK293T cells (ATCC #CRL-11268) were purchased from the Duke Cell Culture facility and were tested for mycoplasma contamination. HEK239T cells were used for co-immunoprecipitation experiments and preparation of AAV viruses.

### Primary neuronal culture

Primary neuronal cultures were prepared from P0 mouse cortex. P0 mouse pups were rapidly decapitated and cortices were dissected and kept individually in 5 mL Hibernate A (Thermo #A1247501) supplemented with 2% B27(Thermo #17504044) at 4°C overnight to allow for individual animal genotyping before plating. Neurons were then treated with Papain (Worthington #LS003120) and DNAse (VWR #V0335)-supplemented Hibernate A for 18 min at 37°C and washed twice with plating medium (plating medium: Neurobasal A [Thermo #10888022] supplemented with 10% horse serum, 2% B-27, and 1% GlutaMAX [Thermo #35050061]), and triturated before plating at 250,000 cells/well on poly-l-lysine-treated coverslips (Sigma #P2636) in 24-well plates. Plating medium was replaced with growth medium (Neurobasal A, 2% B-27, 1% GlutaMAX) 2 hr later. Cell media was supplemented and treated with AraC at DIV5 (5 uM final concentration/well). Half-media changes were then performed every 4 days.

### Plasmid DNA constructs

For immunoprecipitation experiments, a pmCAG-SWIP-WT-HA construct was generated by PCR amplification of the human WASHC4 sequence, which was then inserted between NheI and SalI restriction sites of a pmCAG-HA backbone generated in our lab. Site-directed mutagenesis (Agilent #200517) was used to introduce a C>G point mutation into this pmCAG-SWIP-WT-HA construct for generation of a pmCAG-SWIP-MUT-HA construct (FOR: 5′-ctacaaagttgagggtcagacggggaacaattatatagaaa-3′, REV: 5′-tttctatataattgttccccgtctgaccctcaactttgtag-3′). For iBioID experiments, an AAV construct expressing hSyn1-WASH1-BioID2-HA was generated by cloning a Washc1 insert between SalI and HindIII sites of a pAAV-hSyn1-Actin Chromobody-Linker-BioID2-pA construct (replacing Actin Chromobody) generated in our lab. This backbone included a 25 nm GS linker-BioID2-HA fragment from Addgene #80899, generated by Kim et al., 2016. An hSyn1-solubleBioID2-HA construct was created similarly, by removing Actin Chromobody from the above construct. Oligonucleotide sequences are reported in Key Resources Table. Links to sequences of the plasmid DNA constructs are available in Supplementary file 5.

### AAV viral preparation

AAV preparations were performed as described previously (Uezu et al., 2016). The day before transfection, HEK293T cells were plated at a density of 1.5 × 107 cells per 15 cm2 plate in DMEM media with 10% fetal bovine serum and 1% Pen/Strep (Thermo #11965–092, Sigma #F4135, Thermo #15140–122). Six HEK293T 15 cm2 plates were used per viral preparation. The next day, 30 µg of pAd-DeltaF6 helper plasmid, 15 µg of AAV2/9 plasmid, and 15 µg of an AAV plasmid carrying the transgene of interest were mixed in OptiMEM with PEI-MAX (final concentration 80 µg/mL, Polysciences #24765). Two milliliters of this solution were then added dropwise to each of the 6 HEK293T 15 cm2 plates. Eight hours later, the media was replaced with 20 mL DMEM+10%FBS. Seventy-two hours post-transfection, cells were scraped and collected in the media, pooled, and centrifuged at 1500 rpm for 5 min at RT. The final pellet from the six cell plates was resuspended in 5 mL of cell lysis buffer (15 mM NaCl, 5 mM Tris–HCl, pH 8.5), and freeze-thawed three times using an ethanol/dry ice bath. The lysate was then treated with 50 U/mL of Benzonase (Novagen #70664), for 30 min in a 37°C water bath, vortexed, and then centrifuged at 4500 rpm for 30 min at 4°C. The resulting supernatant containing AAV particles was added to the top of an iodixanol gradient (15%, 25%, 40%, 60% top to bottom) in an Optiseal tube (Beckman Coulter #361625). The gradient was then centrifuged using a Beckman Ti-70 rotor in a Beckman XL-90 ultracentrifuge at 67,000 rpm for 70 min, 18°C. The purified viral solution was extracted from the 40%/60% iodixanol interface using a syringe and placed into an Amicon 100 kDa filter unit (#UFC910024). The viral solution was washed in this filter three times with 1× ice-cold PBS by adding 5 mL of PBS and centrifuging at 4900 rpm for 45 min at 4°C to obtain a final volume of approximately 200 µL of concentrated virus that was aliquoted into 5–10 µL aliquots and stored at −80°C until use.

### Immunocytochemistry

#### Primary antibodies

Rabbit anti-EEA1 (Cell Signaling Technology #C45B10, 1:500), Rat anti-Cathepsin D (Novus #204712, 1:250), and Guinea Pig anti-MAP2 (Synaptic Systems #188004, 1:500).

#### Secondary antibodies

Goat anti-Rabbit Alexa Fluor 568 (Invitrogen #A11036, 1:1000), Goat anti-Guinea Pig Alexa Fluor 488 (Invitrogen #A11073, 1:1000), Goat anti-Rat Alexa Fluor 488 (Invitrogen #A11006, 1:1000), and Goat anti-Guinea Pig Alexa Fluor 555 (Invitrogen #A21435, 1:1000).

At DIV15, neurons were fixed for 15 min using ice-cold 4%PFA/4% sucrose in 1× PBS, pH 7.4 (for EEA1 staining), or 30 min with 50% Bouin’s solution/4% sucrose (for CathepsinD staining, Sigma #HT10132), pH 7.4 (Cheng et al., 2018). Fixed neurons were washed with 1× PBS, then permeabilized with 0.25% TritonX-100 in PBS for 8 min at room temperature (RT), and blocked with 5%normal goat serum/0.2%Triton-X100 in PBS (blocking buffer) for 1 hr at RT with gentle rocking. For EEA1/MAP2 staining, samples were incubated with primary antibodies diluted in blocking buffer at RT for 1 hr. For CathepsinD/MAP2 staining, samples were incubated with primary antibodies diluted in blocking buffer overnight at 4°C. For both conditions, samples were washed three times with 1× PBS and incubated for 30 min at RT with secondary antibodies, protected from light. After secondary antibody staining, coverslips were washed three times with 1× PBS and mounted with FluoroSave mounting solution (Sigma #345789). See antibody section for primary and secondary antibody concentrations.

### Immunohistochemistry

#### Primary antibodies

Rabbit anti-Cleaved Caspase-3 (Cell Signaling Technology #9661, 1:2000), Mouse anti-Calbindin (Sigma #C9848, 1:2000), Rat anti-HA 3F10 (Sigma #12158167001, 1:500), Mouse anti-Bassoon (Abcam #ab82958, 1:500), Rabbit anti-Homer1 (Synaptic Systems #160002, 1:500), Chick anti-Tyrosine Hydroxylase (Abcam #ab76442, 1:1000), and Mouse anti-NeuN (Abcam #ab104224, 1:1000).

#### Secondary antibodies

Donkey anti-Rabbit Alexa Fluor 488 (Invitrogen #A21206, 1:2000), Goat anti-Mouse Alexa Fluor 594 (Invitrogen #A11032, 1:2000), Goat anti-Rat Alexa Fluor 488 (Invitrogen #A11006, 1:5000), Streptavidin Alexa Fluor 594 conjugate (Invitrogen #S32356, 1:5000), Goat anti-Mouse Alexa Fluor 594 (Invitrogen #A11032, 1:500), Donkey anti-Rabbit Alexa Fluor 488 (Invitrogen #A21206, 1:500), Goat anti-Chick Alexa Fluor 568 (Invitrogen #A11041, 1:1000), Goat anti-Mouse Alexa Fluor 647 (Invitrogen #A21235, 1:1000), and 4′,6-diamidino-2-phenylindole (DAPI, Sigma #D9542, 1:1000 for 10 min at RT).

Mice were deeply anesthetized with isoflurane and then transcardially perfused with ice-cold heparinized PBS (25 U/mL) by gravity flow. After clearing of liver and lungs (~2 min), perfusate was switched to ice-cold 4% PFA in 1× PBS (pH 7.4) for 15 min. Brains were dissected, post-fixed in 4%PFA overnight at 4°C, and then cryoprotected in 30% sucrose/1× PBS for 48 hr at 4°C. Fixed brains were then mounted in OTC (Sakura TissueTek #4583) and stored at −20°C until cryosectioning. Every third sagittal section (30 µm thickness) was collected from the motor cortex and striatal regions. Free-floating sections were then permeabilized with 1%TritonX-100 in 1X PBS at RT for 2 hr, and blocked in 1X blocking solution (Abcam #126587) diluted in 0.2%TritonX-100 in 1× PBS for 1 hr at RT. Sections were then incubated in primary antibodies diluted in the 1× blocking solution for two overnights at 4°C. After three washes with 0.2%TritonX-100 in 1× PBS, the sections were then incubated in secondary antibodies diluted in 1× blocking buffer for one overnight at 4°C. Sections were then washed four times with 0.2%TritonX-100 in 1× PBS at RT and mounted onto coverslips with FluoroSave mounting solution (Sigma #345789).

### Western blotting

#### Primary antibodies

Rabbit anti-Strumpellin (Santa Cruz #sc-87442, 1:500), Rabbit anti-WASH1 c-terminal (Sigma #SAB4200373, 1:500), Mouse anti-Beta Tubulin III (Sigma #T8660, 1:10,000), Mouse anti-HA (BioLegend #MMS-101P, 1:5000), Rabbit anti-LAMP1 (Cell Signaling Technology #C54H11, 1:2000), and Rabbit anti-EEA1 (Cell Signaling Technology #C45B10, 1:1500).

#### Secondary antibodies

Donkey anti-Rabbit-HRP (GE Life Sciences #NA934, 1:5,000), Goat anti-mouse-HRP (GE Life Sciences #NA931, 1:5000), Goat anti-Rabbit IR Dye 800CW (LI-COR # 926–32211).

#### Western blotting of whole-brain lysates (Figure 2)

Ten micrograms of each sample were electrophoresed through a 12-well, 4–20% SDS–PAGE gel (Bio-Rad #4561096) at 100V for 1 hr at RT, transferred onto a nitrocellulose membrane (GE Life Sciences #GE10600002) at 100 V for 70 min at RT on ice, and blocked with 5% nonfat dry milk in TRIS-buffered saline containing 0.05% Tween-20 (TBST, pH 7.4). Gels were saved for Coomassie staining at RT for 30 min. Membranes were probed with one primary antibody at a time for 24 hr at 4°C and then washed four times with TBST at RT before incubating with the corresponding species-specific secondary antibody at RT for 1 hr. Membranes were washed with TBST, and then enhanced chemiluminescence (ECL) substrate was added (Thermo Fischer #32109). Membranes were exposed to autoradiography films and scanned with an Epson 1670 at 600dpi. We probed each membrane with one antibody at a time, stripped the membrane with stripping buffer (Thermo Fischer #21059) for 10 min at RT, and then blocked for 1 hr at RT before probing with the next antibody. Order of probes: Strumpellin, β-tubulin, and then WASH1. We determined the optical density of the bands using Image J software (NIH). Data obtained from three independent experiments were plotted and statistically analyzed using GraphPad Prism (version 8) software.

#### Western blotting of subcellular brain fractions (Figure 3—figure supplements 1–3)

Eight micrograms of each sample were electrophoresed through a 15-well, 4–20% SDS–PAGE gel (Bio-Rad #4561096) at 100 V for 1 hr at RT and transferred onto a nitrocellulose membrane (GE Life Sciences #GE10600002) at 100 V for 70 min at RT on ice. Membranes were incubated with Total Protein Stain for 5 min at RT (LI-COR # 926–11015), rinsed, and imaged at 700 nm using an Odyssey Fc imaging system (LI-COR) to determine protein loading. Membranes were then briefly incubated with REVERT solution and blocked with Odyssey blocking buffer (LI-COR #927–50000) for 1 hr at RT. Membranes were probed with one primary antibody at a time for 24 hr at 4°C and then washed four times with 1× TBST before incubating with secondary antibody at RT for 1 hr. Membranes were washed four times with TBST and then imaged with an Odyssey Fc imaging system at 700 nm and 800 nm. Order of probes: LAMP1 then EEA1. We determined the optical density of the bands using Odyssey Fc Image Studio software. Data obtained from three independent experiments and statistically analyzed using GraphPad Prism (version 8) software.

### Immunoprecipitation

HEK293T cells were transfected with pmCAG-SWIP-WT-HA or pmCAG-SWIP-MUT-HA constructs for three days, as previously described (Mason et al., 2011). Cells were lysed with lysis buffer (25 mM HEPES, 150 mM NaCl, 1 mM EDTA, 1% NonidetP-40, pH 7.4) containing protease inhibitors (5 mM NaF, 1 mM orthovanadate, 1 mM AEBSF, and 2 μg/mL leupeptin/pepstatin) and centrifuged at 1700 g for 5 min. Collected supernatant was incubated with 30 µL of pre-washed anti-HA agarose beads (Sigma #A2095) on a sample rotator (15 rpm) for 2 hr at 4°C. Beads were then washed three times with lysis buffer, and sample buffer was added before subjecting to immunoblotting as described above. The protein-transferred membrane was probed individually for WASH1, Strumpellin, and HA. Data were collected from four separate preparations of WT and MUT conditions.

### Electron microscopy

Adult (7mo) WT and MUT SWIPP1019R mice were deeply anesthetized with isoflurane and then transcardially perfused with warmed heparinized saline (25 U/mL heparin) for 4 min, followed by ice-cold 0.15 M cacodylate buffer pH 7.4 containing 2.5% glutaraldehyde (Electron Microscopy Sciences #16320), 3% paraformaldehyde, and 2 mM CaCl2 for 15 min. Brain samples were dissected and stored on ice in the same fixative for 2 hr before washing in 0.1 M sodium cacodylate buffer (three changes for 15 min each). Samples were then post-fixed in 1.0% OsO4 in 0.1 M sodium cacodylate buffer for 1 hr on a rotator. Samples were then washed in three 15 min changes of 0.1 M sodium cacodylate. Samples were then placed into en bloc stain (1% uranyl acetate) overnight at 4°C. Subsequently, samples were dehydrated in a series of ascending acetone concentrations including 50%, 70%, 95%, and 100% for three cycles with 15 min incubation at each concentration change. Samples were then placed in a 50:50 mixture of epoxy resin (Epon) and acetone overnight on a rotator. This solution was then replaced twice with 100% fresh Epon for at least 2 hr at room temperature on a rotator. Samples were embedded with 100% Epon resin in BEEM capsules (Ted Pella) for 48 hr at 60°C. Samples were ultrathin sectioned to 60–70 nm on a Reichert Ultracut E ultramicrotome. Harvested grids were then stained with 2% uranyl acetate in 50% ethanol for 30 min and Sato’s lead stain for 1 min. Micrographs were acquired using a Phillips CM12 electron microscope operating at 80 kV, at 1700× magnification. Micrographs were analyzed in Adobe Photoshop 2019, using the ‘magic wand’ tool to demarcate and measure the area of electron-dense and electron-lucent regions of interest (ROIs). Statistical analyses of ROI measurements were performed in GraphPad Prism (version 8) software. The experimenter was blinded to genotype for image acquisition and analysis.

### iBioID Protein Sample Preparation

AAV2/9 viral probes, hSyn1-WASH1-BioID2-HA or hSyn1-solubleBioID2-HA, were injected into wild-type CD1 mouse brains using a Hamilton syringe (#7635–01) at age P0–P1 to ensure viral spread throughout the forebrain (Glascock et al., 2011). Fifteen days post-viral injection, biotin was subcutaneously administered at 24 mg/kg for seven consecutive days for biotinylation of proteins in proximity to BioID2 probes. Whole brains were extracted on the final day of biotin injections, snap frozen, and stored in liquid nitrogen until protein purification. Seven brains were used for protein purification of each probe, and each purification was performed three times independently (21 brains total for WASH1-BioID2, 21 for solubleBioID2).

We performed all homogenization and protein purification on ice. A 2 mL Dounce homogenizer was used to individually homogenize each brain in a 1:1 solution of Lysis-R:2X-RIPA buffer solution with protease inhibitors (Roche cOmplete tablets #11836153001). Each sample was sonicated three times for 7 s and then centrifuged at 5000 g for 5 min at 4°C. Samples were transferred to Beckman Coulter 1.5 mL tubes (#344059) and then spun at 45,000 rpm in a Beckman Coulter tabletop ultracentrifuge (TLA-55 rotor) for 1 hr at 4°C. SDS was added to supernatants (final 1%), and samples were then boiled for 5 min at 95°C. We next combined supernatants from the same condition together (WASH1-BioID2 vs. solubleBioID2) in 15 mL conical tubes to rotate with 30 µL high-capacity NeutrAvidin beads overnight at 4°C (Thermo #29204).

The following day, all steps were performed under a hood with keratin-free reagents. Samples were spun down at 6000 rpm, 4°C for 5 min to pellet the beads and remove supernatant. The pelleted beads then went through a series of washes, each for 10 min at RT with 500 µL of solvent, and then spun down on a tabletop centrifuge to pellet the beads for the next wash. The washes were as follows: 2% SDS twice, 1% TritonX100–1% deoxycholate-25 mM LiCl2 once, 1 M NaCL twice, 50 mM ammonium bicarbonate (Ambic) five times. Beads were then mixed 1:1 with a 2× Laemmli sample buffer that contained 3 mM biotin/50 mM Ambic, boiled for 5 min at 95°C, vortexed three times, and then biotinylated protein supernatants were stored at −80°C until LC–MS/MS.

### LC–MS/MS for iBioID

We gave the Duke Proteomics and Metabolomics Shared Resource (DPMSR) six eluents from streptavidin resins (3× WASH1-BioID2, 3× solubleBioID2), stored on dry ice. Samples were reduced with 10 mM dithiolthreitol for 30 min at 80°C and alkylated with 20 mM iodoacetamide for 30 min at room temperature. Next, samples were supplemented with a final concentration of 1.2% phosphoric acid and 256 μL of S-Trap (Protifi) binding buffer (90% MeOH/100 mM triethylammonium bicarbonate [TEAB]). Proteins were trapped on the S-Trap, digested using 20 ng/μL sequencing grade trypsin (Promega) for 1 hr at 47°C, and eluted using 50 mM TEAB, followed by 0.2% formic acid (FA), and lastly using 50% acetonitrile (ACN)/0.2% FA. All samples were then lyophilized to dryness and resuspended in 20 μL 1%TFA/2% ACN containing 25 fmol/μL yeast alcohol dehydrogenase (UniProtKB P00330; ADH_YEAST). From each sample, 3 μL was removed to create a pooled QC sample (SPQC) which was run analyzed in technical triplicate throughout the acquisition period.

Quantitative LC/MS/MS was performed on 2 μL of each sample, using a nanoAcquity UPLC system (Waters) coupled with a Thermo QExactive HF-X high-resolution accurate mass tandem mass spectrometer (Thermo) via a nanoelectrospray ionization source. Briefly, the sample was first trapped on a Symmetry C18 20 mm × 180 μm trapping column (5 μL/min at 99.9/0.1 vol/vol water/ACN), after which the analytical separation was performed using a 1.8 μm Acquity HSS T3 C18 75 μm × 250 mm column (Waters) with a 90 min linear gradient of 5–30% ACN with 0.1% formic acid at a flow rate of 400 nL/min with a column temperature of 55°C. Data collection on the QExactive HF-X mass spectrometer was performed in a data-dependent acquisition (DDA) mode of acquisition with a r=120,000,000 (@ m/z 200) full MS scan from m/z 375–1600 with a target AGC value of 3e6 ions followed by 30 MS/MS scans at r=15,000,000 (@ m/z 200) at a target AGC value of 5e4 ions and 45 ms. A 20 s dynamic exclusion was employed to increase depth of coverage. The total analysis cycle time for each sample injection was approximately 2 hr.

### LOPIT-DC subcellular fractionation

We performed three independent fractionation experiments with one adult SWIP mutant brain and one WT mouse brain fractionated in each experiment. Each mouse was sacrificed by isoflurane inhalation and its brain was immediately extracted and placed into a 2 mL Dounce homogenizer on ice with 1 mL isotonic TEVP homogenization buffer (320 mM sucrose, 10 mM Tris base, 1 mM EDTA, 1 mM EGTA, 5 mM NaF, pH7.4 [Hallett et al., 2008]). A complete mini protease inhibitor cocktail tablet (Sigma #11836170001) was added to a 50 mL TEVP buffer aliquot immediately before use. Brains were homogenized for 15 passes with a Dounce homogenizer to break the tissue, and then this lysate was brought up to a 5 mL volume with additional TEVP buffer. Lysates were then passed through a 0.5 mL ball-bearing homogenizer for two passes (14 µm ball, Isobiotec) to release organelles. Final brain lysate volumes were approximately 7.5 mL each. Lysates were then divided into replicate microfuge tubes (Beckman Coulter #357448) to perform differential centrifugation, following Geladaki et. al’s LOPIT-DC protocol (Geladaki et al., 2019). Centrifugation was carried out at 4°C in a tabletop Eppendorf 5424 centrifuge for spins at 200 g, 1000 g, 3000 g, 5000 g, 9000 g, 12,000 g, and 15,000 g. To isolate the final three fractions, a tabletop Beckman TLA-100 ultracentrifuge with a TLA-55 rotor was used at 4°C with speeds of 30,000 g, 79,000 g, and 120,000 g, respectively. Samples were kept on ice at all times, and pellets were stored at −80°C. Pellets from seven fractions (5000 g–120,000g) were used for proteomic analyses.

### 16-plex TMT LC–MS/MS

The Duke Proteomics and Metabolomics Shared Resource (DPMSR) processed and prepared fraction pellets from all 42 frozen samples simultaneously (seven fractions per brain from three WT and three MUT brains). Due to volume constraints, each sample was split into three tubes, for a total of 126 samples, which were processed in the following manner: 100 µL of 8 M urea was added to the first aliquot then probe sonicated for 5 s with an energy setting of 30%. This volume was then transferred to the second and then third aliquots after sonication in the same manner. All tubes were centrifuged at 10,000 g, and any residual volume from tubes 1 and 2 were added to tube 3. Protein concentrations were determined by BCA on the supernatant in duplicate (5 μL each assay). Total protein concentrations for each replicate ranged from 1.1 mg/mL to 7.8 mg/mL with total protein quantities ranging from 108.3 to 740.81 µg. 60 µg of each sample was removed and normalized to 52.6 µL with 8 M urea and 14.6 µL 20% SDS. Samples were reduced with 10 mM dithiolthreitol for 30 min at 80°C and alkylated with 20 mM iodoacetamide for 30 min at room temperature. Next, they were supplemented with 7.4 μL of 12% phosphoric acid and 574 μL of S-Trap (Protifi) binding buffer (90% MeOH/100 mM TEAB). Proteins were trapped on the S-Trap, digested using 20 ng/μL sequencing grade trypsin (Promega) for 1 hr at 47°C, and eluted using 50 mM TEAB, followed by 0.2% FA, and lastly using 50% ACN/0.2% FA. All samples were then lyophilized to dryness.

Each sample was resuspended in 120 μL 200 mM TEAB, pH 8.0. From each sample, 20 µL was removed and combined to form a pooled quality control sample (SPQC). Fresh TMTPro reagent (0.5 mg for each 16-plex reagent) was resuspended in 20 μL 100% ACN and was added to each sample. Samples were incubated for 1 hr at RT. After the 1 hr reaction, 5 μL of 5% hydroxylamine was added and incubated for 15 min at room temperature to quench the reaction. Each 16-plex TMT experiment consisted of the WT and MUT fractions from one mouse, as well as the two SPQC samples. Samples corresponding to each experiment were concatenated and lyophilized to dryness.

Samples were resuspended in 800 µL 0.1% formic acid. 400 µg was fractionated into 48 unique high-pH reversed-phase fractions using pH 9.0 20 mM ammonium formate as mobile phase A and neat ACN as mobile phase B. The column used was a 2.1 mm × 50 mm XBridge C18 (Waters), and fractionation was performed on an Agilent 1100 HPLC with G1364C fraction collector. Throughout the method, the flow rate was 0.4 mL/min and the column temperature was 55°C. The gradient method was set as follows: 0 min, 3%B; 1 min, 7% B; 50 min, 50%B; 51 min, 90% B; 55 min, 90% B; 56 min, 3% B; 70 min, 3% B. 48 fractions were collected in equal time segments from 0 to 52 min, then concatenated into 12 unique samples using every 12th fraction. For instance, fractions 1, 13, 25, and 37 were combined, fractions 2, 14, 26, and 38 were combined, etc. Fractions were frozen and lyophilized overnight. Samples were resuspended in 66 μL 1% TFA/2% ACN prior to LC–MS analysis.

Quantitative LC/MS/MS was performed on 2 μL (1 μg) of each sample, using a nanoAcquity UPLC system (Waters) coupled with a Thermo Orbitrap Fusion Lumos high-resolution accurate mass tandem mass spectrometer (Thermo) equipped with a FAIMS Pro ion-mobility device via a nanoelectrospray ionization source to enhance precursor ion selectivity and quantitative accuracy without losing the depth of coverage. Briefly, the sample was first trapped on a Symmetry C18 20 mm × 180 μm trapping column (5 μL/min at 99.9/0.1 vol/vol water/ACN), after which the analytical separation was performed using a 1.8 μm Acquity HSS T3 C18 75 μm × 250 mm column (Waters) with a 90 min linear gradient of 5–30% ACN with 0.1% formic acid at a flow rate of 400 nL/min with a column temperature of 55°C. Data collection on the Fusion Lumos mass spectrometer was performed for three different compensation voltages (CV: −40 V, −60 V, −80 V). Within each CV, a DDA mode of acquisition with a r=120,000,000 (@ m/z 200) full MS scan from m/z 375–1600 with a target AGC value of 4e5 ions was performed. MS/MS scans were acquired in the Orbitrap at r=50,000,000 (@ m/z 200) from m/z 100 with a target AGC value of 1e5 and max fill time of 105 ms. The total cycle time for each CV was 1 s, with total cycle times of 3 s between like full MS scans. A 45 s dynamic exclusion was employed to increase depth of coverage. The total analysis cycle time for each sample injection was approximately 2 hr.

Following UPLC–MS/MS analyses, data were imported into Proteome Discoverer 2.4 (Thermo Scientific). The MS/MS data were searched against a SwissProt Mouse database (downloaded November 2019) plus additional common contaminant proteins, including yeast alcohol dehydrogenase (ADH), bovine casein, bovine serum albumin, as well as an equal number of reversed-sequence ‘decoys’ for FDR determination. Mascot Distiller and Mascot Server (v 2.5, Matrix Sciences) were utilized to produce fragment ion spectra and to perform the database searches. Database search parameters included fixed modification on Cys (carbamidomethyl) and variable modification on Met (oxidation), Asn/Gln (deamindation), Lys (TMTPro), and peptide N-termini (TMTPro). Data were searched at 5 ppm precursor and 0.02 product mass accuracy with full trypsin enzyme rules. Reporter ion intensities were calculated using the Reporter Ions Quantifier algorithm in Proteome Discoverer. Percolator node in Proteome Discoverer was used to annotate the data at a maximum 1% protein FDR.

### Mouse behavioral assays

Behavioral tests were performed on age-matched WT and homozygous SWIPP1019R mutant littermates. Male and female mice were used in all experiments. Testing was performed at two time points: P42–55 days old as a young adult age and 5.5 months old as mid-adulthood, so that we could compare disease progression in this mouse model to human patients (Ropers et al., 2011). The sequence of behavioral testing was as follows: Y-maze (to measure working memory), object novelty recognition (to measure short- and long-term object recognition memory), TreadScan (to assess gait), and steady-speed rotarod (to assess motor control and strength) for 40–55 day old mice. Testing was performed over 1.5 weeks, interspersed with rest days for acclimation. This sequence was repeated with the same cohort at 5.5–6 months old, with three additional measures added to the end of testing: fear conditioning (to assess associative fear memory), a hearing test (to measure tone response), and a shock threshold test (to assess somatosensation). Of note, a separate, second cohort of mice was evaluated for fear conditioning, hearing, and shock threshold testing at adolescence. After each trial, equipment was cleaned with Labsan to remove residual odors. The experimenter was blinded to genotype for all behavioral analyses.

### Y-maze

Working memory was evaluated by measuring spontaneous alternations in a three-arm Y-maze under indirect illumination (80–90 lux). A mouse was placed in the center of the maze and allowed to freely explore all arms, each of which had different visual cues for spatial recognition. Trials were 5 min in length, with video data and analyses captured by EthoVision XT 11.0 software (Noldus Information Technology). Entry to an arm was define as the mouse being >1 body length into a given arm. An alternation was defined as three successive entries into each of the different arms. Total % alternation was calculated as the total number of alternations/the total number of arm entries minus 2 × 100.

### Novel object recognition

One hour before testing, mice were individually exposed to the testing arena (a 48×22×18 cm white opaque arena) for 10 min under 80–100 lux illumination without any objects. The test consisted of three phases: training (day 1), short-term memory test (STM, day 1), and long-term memory test (LTM, day 2). For the training phase, two identical objects were placed 10 cm apart, against opposing walls of the arena. A mouse was placed in the center of the arena and given full access to explore both objects for 5 min and then returned to its home cage. For STM testing, one of the training objects remained (the now familiar object), and a novel object replaced one of the training objects (similar in size, different shapes). The mouse was returned to the arena 30 min after the training task and allowed to explore freely for 5 min. For LTM testing, the novel object was replaced with another object, and the familiar object remained unchanged. The LTM test was also 5 min in duration, conducted 24 hr after the training task. Behavior was scored using Ethovision 11.0 XT software (Noldus) and analyzed by a blind observer. Object contact was defined as the mouse’s nose within 1 cm of the object. We analyzed both number of nose contacts with each object and duration of contacts. Preference scores were calculated as follows: (duration contactnovel− duration contactfamiliar)/total duration contactnovel+familiar. Positive scores signified a preference for the novel object, whereas negative scores denoted a preference for the familiar object, and scores approaching zero indicated no preference.

### TreadScan

A TreadScan forced locomotion treadmill system (CleversSys Inc, Reston, VA) was used for gait recording and analysis. Each mouse was recorded walking on a transparent treadmill at 45 days old and again at 5.5 months old. Mice were acclimated to the treadmill chamber for 1 min before the start of recording to eliminate exploratory behavior confounding normal gait. Trials were 20 s in length, with mice walking at speeds between 13.83 and 16.53 cm/s (P45 WT average 15.74 cm/s; P45 MUT average 15.80 cm/s; 5.5mo WT average 15.77 cm/s; 5.5mo MUT average 15.85 cm/s). A high-speed digital camera attached to the treadmill-captured limb movement at a frame rate of 100 frames/s. We used TreadScan software (CleversSys) and representative WT and MUT videos to generate footprint templates, which were then used to identify individual paw profiles for each limb. Parameters such as stance time, swing time, step length, track width, and limb coupling were recorded for the entire 20 s duration for each animal. Output gait tracking was verified manually by a blinded experimenter to ensure consistent limb tracking throughout the duration of each video.

### Steady speed rotarod

A 5-lane rotarod (Med Associates, St. Albans, VT) was used for steady-speed motor analysis. The rod was run at a steady speed of 32 rpm for four 5 min trials, with a 40 min inter-trial interval. We recorded mouse latency to fall by infrared beam break or manually for any mouse that completed two or more rotations on the rod without walking. Mice were randomized across lanes for each trial.

### Fear conditioning

Animals were examined in contextual and cued fear conditioning as described by Rodriguiz and Wetsel, 2006. Two separate cohorts of mice were used in testing the two age groups. A 3-day testing paradigm was used to assess memory: conditioning on day 1, context testing 24 hr post-conditioning on day 2, and cued tone testing 48 hr post-conditioning on day 3. All testing was conducted in fear conditioning chambers (Med Associates). In the conditioning phase, mice were first acclimated to the test chamber for 2 min under ~100 lux illumination. Then a 2900 Hz, 80 dB tone (conditioned stimulus, CS) played for 30 s, which terminated with a paired 0.4 mA, 2 s scrambled foot shock (unconditioned stimulus, US). Mice were removed from the chamber and returned to their home cage 30 s later. In the context testing phase, mice were placed in the same conditioning chamber and monitored for freezing behavior for a 5 min trial period, in the absence of the CS and US. For cued tone testing, the chambers were modified to different dimensions and shapes, contained different floors and wall textures, and lighting was adjusted to 50 lux. Mice acclimated to the chamber for 2 min, and then the CS was presented continuously for 3 min. Contextual and cued fear memory was assessed by freezing behavior, captured by automated video software (CleversSys).

### Hearing test

We tested mouse hearing using a startle platform (Med Associates) connected to Startle Pro Software in a sound-proof chamber. Mice were placed in a ventilated restraint cylinder connected to the startle response detection system to measure startle to each acoustic stimulus. After 2 min of acclimation, mice were assessed for an acoustic startle response to seven different tone frequencies, 2 kHz, 3 kHz, 4 kHz, 8 kHz, 12 kHz, 16 kHz, and 20 kHz that were randomly presented three times each at four different decibels, 80, 100, 105, and 110 dB, for a total of 84 trials. A random inter-trial interval of 15–60 s (average 30 s) was used to prevent anticipation of a stimulus. An animal’s reaction to the tone was recorded as startle reactivity in the first 100 ms of the stimulus presentation, which was transduced through the platform’s load cell and expressed in arbitrary units (AU).

### Startle response (somatosensation)

Mouse somatosensation was tested by placing mice in a startle chamber (Med Associates) connected to Startle Pro Software. Mice were placed atop a multi-bar cradle within a ventilated plexiglass restraint cylinder, which allows for horizontal movement within the chamber, but not upright rearing. After 2 min of acclimation, each mouse was exposed to 10 different scrambled shock intensities, ranging from 0 to 0.6 mA with randomized inter-trial intervals of 20–90 s. Each animal’s startle reactivity during the first 100 ms of the shock was transduced through the platform’s load cell and recorded as area under the curve (AUC) in AU.

### Quantification and statistical analysis

Experimental conditions, number of replicates, and statistical tests used are stated in each figure legend. Each experiment was replicated at least three times (or on at least three separate animals) to assure rigor and reproducibility. Both male and female age-matched mice were used for all experiments, with data pooled from both sexes. Data compilation and statistical analyses for all non-proteomic data were performed using GraphPad Prism (version 8, GraphPad Software, CA), using a significance level of alpha=0.05. Prism provides exact p-values unless p<0.0001. All data are reported as mean ± SEM. Each data set was tested for normal distribution using a D’Agostino–Person normality test to determine whether parametric (unpaired Student’s t-test, one-way ANOVA, two-way ANOVA) or non-parametric (Mann–Whitney, Kruskal–Wallis, Kolmogorov–Smirnov) tests should be used. Parametric assumptions were confirmed with the Shapiro–Wilk test (normality) and Levine’s test (error variance homogeneity) for ANOVA with repeated-measures testing. The analysis of iBioID and TMT proteomics data are described below. All proteomic data and analysis scripts are available online (see key resources table).

### Imaris 3D reconstruction

For EEA1+ and CathepsinD+ puncta analyses, coverslips were imaged on a Zeiss LSM 710 confocal microscope. Images were sampled at a resolution of 1024 × 1024 pixels with a dwell time of 0.45 µs using a 63×/1.4 oil immersion objective, a 2.0 times digital zoom, and a z-step size of 0.37 µm. Images were saved as ‘.lsm’ formatted files, and quantification was performed on a POGO Velocity workstation in the Duke Light Microscopy Core Facility using Imaris 9.2.0 software (Bitplane, South Windsor, CT). For analyses, we first used the ‘surface’ tool to make a solid fill surface of the MAP2-stained neuronal soma and dendrites, with the background subtraction option enabled. We selected a threshold that demarcated the neuron structure accurately while excluding background. For EEA1 puncta analyses, a 600 × 800 µm selection box was placed around the soma in each image and surfaces were created for EEA1 puncta within the selection box. Similarly, for CathepsinD puncta analyses, a 600 × 600 µm selection box was placed around the soma(s) in each image for surface creation. The same threshold settings were used across all images, and individual surface data from each soma were exported for aggregate analyses. The experimenter was blinded to sample conditions for both image acquisition and analysis.

### Cleaved caspase-3 image analysis

Z-stack images were acquired on a Zeiss 710 LSM confocal microscope. Images were sampled at a resolution of 1024 × 1024 pixels with a dwell time of 1.58 µs, using a 63×/1.4 oil immersion objective (for cortex, striatum, and hippocampus) or 20×/0.8 dry objective (cerebellum), a 1.0 times digital zoom, and a z-step size of 0.67 µm. Images were saved as ‘.lsm’ formatted files and then converted into maximum intensity projections (MIPs) using Zen 2.3 SP1 software. Quantification of CC3 colocalization with DAPI was performed on the MIPs using the Particle Analyzer function in FIJI ImageJ software. The experimenter was blind to sample conditions for both image acquisition and analysis.

### Synapse quantification image analysis

Z-stack images of the motor cortex were acquired on a Zeiss 710 LSM confocal microscope. Images were sampled at a resolution of 1024 × 1024 pixels with a dwell time of 1.58 µs, using a 63×/1.4 oil immersion objective, a 1.0 times digital zoom, and a z-step size of 0.34 µm, acquiring five steps per image. Images were saved as ‘.lsm’ formatted files and then converted into maximum intensity projections (MIPs) using Zen 2.3 SP1 software. We selected 250 µm x 250 µm regions in the MIPs for analyses. Quantification of bassoon and homer1 colocalization was performed using the Particle Analyzer function of FIJI ImageJ software. The experimenter was blind to sample conditions for both image acquisition and analysis.

### Tyrosine hydroxylase image analysis

Z-stack images of the substantia nigra and striatum were acquired on a Zeiss 710 LSM confocal microscope. Images were sampled at a resolution of 1024 × 1024 pixels with a dwell time of 1.58 µs, using a 40×/1.3 oil immersion objective or 10×/0.45 dry objective, a 1.0 times digital zoom, and a z-step size of 0.67 µm, acquiring five steps per image. Images were saved as ‘.lsm’ formatted files and then converted into maximum intensity projections (MIPs) using Zen 2.3 SP1 software. Quantification of Tyrosine Hydroxlyase+ (TH+) neurons was performed using the Particle Analyzer function of FIJI ImageJ software. Quantification of dopaminergic innervation of the striatum was obtained by measuring the mean TH+ signal intensity for each image. The experimenter was blind to sample conditions for both image acquisition and analysis.

### iBioID quantitative analysis

Following UPLC–MS/MS analyses, data was imported into Proteome Discoverer 2.2 (Thermo Scientific Inc) and aligned based on the accurate mass and retention time of detected ions (‘features’) using Minora Feature Detector algorithm in Proteome Discoverer. Relative peptide abundance was calculated based on AUC of the selected ion chromatograms of the aligned features across all runs. The MS/MS data was searched against the SwissProt Mus musculus database (downloaded in April 2018) with additional proteins, including yeast ADH1, bovine serum albumin, as well as an equal number of reversed-sequence ‘decoys’ for false discovery rate (FDR) determination. Mascot Distiller and Mascot Server (v 2.5, Matrix Sciences) were utilized to produce fragment ion spectra and to perform the database searches. Database search parameters included fixed modification on Cys (carbamidomethyl), variable modifications on Meth (oxidation), and Asn and Gln (deamidation) and were searched at 5 ppm precursor and 0.02 Da product mass accuracy with full trypsin enzymatic rules. Peptide Validator and Protein FDR Validator nodes in Proteome Discoverer were used to annotate the data at a maximum 1% protein FDR.

Protein-level intensities were exported from Proteome Discoverer and processed using custom R scripts. Carboxylases, keratins, and mitochondrial proteins (Calvo et al., 2016) were removed from the identified proteins as known contaminants. Sample loading normalization was performed to account for technical variation between the nine individual MS runs. In brief, this is done by multiplying intensities from each MS run by a scaling factor, such that total run intensities are equal. We created a pooled QC sample by pooling equivalent aliquots of peptides from each biological replicate and analyzed this in technical duplicate in each experiment. We performed sample pool normalization to SPQC samples to standardize protein measurements across all samples and correct for batch effects between MS analyses. Sample pool normalization adjusts the protein-wise mean of all biological replicates to be equal to the mean of all SPQC replicates. Finally, proteins that were identified by a single peptide and/or identified in less than 50% of samples were removed. Any remaining missing values were inferred to be missing not-at-random due to the left shifted distribution of proteins with missing values and imputed using the k-nearest neighbors algorithm using the impute.knn function in the R package impute (impute::impute.knn). Normalized protein data were then fit with a simple linear model to derive a model-based statistical comparison of WASH iBioID and solubleBioID2 control groups (Huang et al., 2020). To consider a protein enriched in the WASH interactome, we required that a protein exhibit a fold-change greater than 4 over the negative control with a Benjamini−Hochberg false discovery rate (FDR) less than 0.05 (Benjamini and Hochberg, 1995). With these criteria, 175 proteins were identified as WASH1 interactome proteins. The statistical results can be found in Supplementary file 1.

Proteins that function together often interact directly. We compiled experimentally determined protein–protein interactions (PPIs) among the WASH1 interactome from the HitPredict database (López et al., 2015) using a custom R package, getPPIs (available online at twesleyb/getPPIs). We report PPIs among the WASH1 interactome in Supplementary file 1.

Bioinformatic GO analysis was conducted by manual annotation of identified proteins and confirmed with Metascape analysis (Zhou et al., 2019) of WASH1-BioID2-enriched proteins using the 2102 proteins identified in the mass spectrometry analysis as background.

### Protein-level statistical inference with MSstatsTMT

PSM-level data were exported from Proteome Discover 2.2 and prepared for analysis with MSstatsTMT, an R package for data normalization and hypothesis testing in multiplex TMT proteomics experiments (Huang et al., 2020). MSstatsTMT performs statistical inference in two steps. First, each protein in the dataset is fit with a LMM expressing the major sources of variation in the experimental design. Second, given the fitted model, a model-based comparison is made between pairs of treatment conditions.

Given our experimental design, MSstatsTMT fits the following LMM to each protein-level subset of the data:

$$
Y_{mcbt}=\mu+Condition_{c}+Mixture_{m}+ϵ_{mcb}
$$

The model’s constraints delimit the response as a function of fixed and mixed effects:

$$
\sumc=1CCondition_{c}=0\frac{Mixture_{m}∼iid N(0,\sigma_{M}^{2})}{ϵ_{mcb}∼iid N(0,\sigma^{2})}
$$

Condition is a fixed effect and represents the 14 combinations of Genotype and BioFraction in our experimental design. The term Mixture is a mixed effect and represents variation between the three TMT mixtures. Mixed effects are normally and independently distributed (i.i.d.). The term epsilon (ε) is a mixed effect and represents both biological and technical variations, quantifying any remaining error.

Pairwise contrasts between MUT and WT conditions are obtained by comparing estimates obtained from the LMM fit by restricted maximum likelihood (Bates et al., 2015). We are interested in testing the null hypothesis: $l^{T}*\beta=0$. Where the contrast, $l^{T}$ is a vector of sum 0 specifying the positive and negative coefficients of the contrast. Beta (β) is the model-based estimates of Mutant and Control conditions. A test statistic for such a two-way contrast is given by Kuznetsova et al., 2017:

$$
t=\frac{l^{T}\beta^}{\sqrt{l\sigma^{2}V^l^{T}}}
$$

We obtain the model’s estimates (β), error (σ2), and variance–covariance matrix ($V^$) from the fit LMM. The numerator is the log fold-change of a comparison. Together, the denominator represents the standard error of the comparison. The degrees of freedom for the contrast are derived using the Satterthwaite moment of approximation method (Kuznetsova et al., 2017). Finally, a p-value is calculated given the t-statistic and degrees of freedom. p-values for all tests of a given contrast are adjusted using the FDR method (Huang et al., 2020). Using MSstatsTMT we assessed two types of contrasts. Statistical results for both intra-BioFraction and the overall ‘Mutant-Control’ comparison are found in Supplementary file 2.

### Quantitative TMT proteomics analysis for spatial proteomics

Peptide-level data from the spatial proteomics analysis of SWIPP1019R WT and MUT brain were exported from Proteome Discoverer (version 2.4) and analyzed using custom R scripts. Peptides from contaminant and non-mouse proteins were removed. First, we performed sample loading normalization, normalizing the total ion intensity for each TMT channel within an experiment to be equal. Sample loading normalization corrects for small differences in the amount of sample analyzed and labeling reaction efficiency differences between individual TMT channels within an experiment.

We found that in each TMT experiment there were a small number of missing values (mean percent missing=1.6±0.17%). Missing values were inferred to be missing at random imputed using the k-nearest neighbor algorithm in the R package impute (impute::impute.knn). Missing values for SPQC samples were not imputed. Peptides with any missing SPQC data were removed.

Following sample loading normalization, SPQC replicates within each experiment should yield identical measurements. As peptides with irreproducible QC measurements are unlikely to be quantitatively robust, and their inclusion may bias downstream normalization, we sought to remove them. To assess intra-batch peptide variability, we adapted the method described by Ping et al., 2018. Briefly, peptides were binned into five groups based on the average intensity of the two SPQC replicates. For each pair of SPQC measurements, the log ratio of SPQC intensities was calculated. To identify outlier QC peptides, we plotted the distribution of these log ratios binned into five intensity bins. Peptides with ratios that were more than 4 standard deviations away from the mean of its intensity bin were considered outliers and removed.

Proteins were summarized as the sum of all unique peptide intensities corresponding to a unique UniProtKB Accession identifier, and sample loading normalization was performed across all three experiments to account for inter-experimental technical variability. In a TMT experiment, the peptides selected for MS2 fragmentation are partially random, especially at lower signal-to-noise ratios. This stochasticity means that proteins are typically quantified by different peptides in each experiment. Thus, although SPQC samples should yield identical protein measurements in each of the three experiments (as it is the same sample analyzed in each experiment), the observed protein measurements exhibit variability due to their quantification by different peptides. To account for this protein-level bias, we utilized the internal reference scaling (IRS) approach described by Plubell et al., 2017. IRS normalization scales the protein-wise geometric average of all SPQC measurements across all experiments to be equal and simultaneously adjusts biological replicates. In brief, each protein is multiplied by a scaling factor, which adjusts its intra-experimental SPQC values to be equal to the geometric mean of all SPQC values for the three experiments. This normalization step effectively standardizes protein measurements between different mass spectrometry experiments.

Before downstream analyses, we removed irreproducible proteins. This included proteins that were quantified in less than 50% of all samples, proteins that were identified by a single peptide, and proteins that had missing SPQC values. Across all 42 biological replicates, we observed that a small number of proteins had potential outlier measurements that were either several orders of magnitude greater or less than the mean of its replicates. In order to identify and remove these proteins, we assessed the reproducibility of protein measurements within a fraction in the same manner used to identify and filter SPQC outlier peptides. A small number of proteins were identified as outliers if the average log ratio of their three QC technical replicates was more than 4 standard deviations away from the mean of its intensity bin. In total, we retained 5897 proteins in the final spatial proteomics dataset.

### Spatial proteomics network construction

To construct a protein covariation graph, we assessed the pairwise covariation (correlation) between all 5897 proteins quantified in all 42 biological samples using the Pearson correlation statistic (Freedman et al., 2007). The resulting complete, signed, weighted, and symmetric adjacency matrix was then re-weighted using ‘Network Enhancement’. We implemented network enhancement in R based on microbma’s translation of the original Matlab code (https://github.com/microbma/neten). Network enhancement removes noise from the graph and facilitates downstream community detection (Wang et al., 2018).

### Clustering the spatial proteomics network

The enhanced adjacency matrix was clustered in Python using the Leiden algorithm (Traag et al., 2019), a recent extension and improvement of the well-known Louvain algorithm (Mucha et al., 2010). The Leiden algorithm functions to optimize the partition of a graph into modules by maximizing a quality statistic. We utilized the ‘Surprise’ quality statistic (Traag et al., 2015) to identify optimal partitions of the protein covariation graph. Clustering of the network resulted in the identification of 49 modules.

### Module-level statistical inference

To evaluate modules that were changing between WT and MUT genotypes, we extended MSstatsTMT’s LMM framework. In this statistical design, we were interested in the average effect of genotype on the common response of all proteins in a module. After scaling normalized protein intensity measurements, we fit each module-level subset of the data with a linear mixed-model expressing the term Protein as a random effect:

$$
log_{2}⁡(Relative Protein Intensity)=\mu+Condition+Protein+ ϵ
$$

When fitting the module-level models, we omitted the term Mixture as the variance attributable to Mixture after normalization is negligible (Figure 3—figure supplement 4). The response variable is the log2-transformed scaled (sum-normalized) protein intensity measurements for all proteins in a spatial proteomics module. An overall comparison is assessed given the fitted model and a contrast vector specifying a comparison between WT and MUT groups, as described above, for protein-wise comparisons. We utilized the Bonferroni method to adjust p-values for k=49 module comparisons and considered modules with an adjusted p-value less than 0.05 significant (n=23). For plotting, log2-transformed relative protein intensity measurements were scaled into the range of 0–1 to avoid plotting negative numbers.

### Module gene set enrichment analysis

Modules were analyzed for enrichment of the WASH interactome (this paper, Figure 1), Retriever complex (McNally et al., 2017), CORUM protein complexes (Giurgiu et al., 2019), and subcellular predictions generated by Geladaki et al., 2019 using the hypergeometric test with Bonferroni p-value correction for multiple comparisons. The union of all clustered and pathway proteins was used as background for the hypergeometric test. In addition to analysis of these general cellular pathways, we analyzed modules for enrichment of neuron-specific subcellular compartments – this included the presynapse (Takamori et al., 2006), excitatory post-synapse (Uezu et al., 2016), and inhibitory post-synapse (Uezu et al., 2016). Gene set enrichment results are found in Supplementary file 4 and are available online at https://github.com/soderling-lab/SwipProteomics.

### Network visualization

Network graphs were visualized in Cytoscape (Version 3.7.2). Node location was manually adjusted to visualize the module more compactly. Node size was set to be proportional to the weighted degree centrality of a node in its module subgraph. Node size thus reflects node importance in the module. Visualizing co-expression or covariation networks is challenging because every node is connected to every other node (the graph is complete). To aid visualization of module topology, we removed weak edges from the graphs. A threshold for each module was set to remove the maximal number of edges before the module subgraph split into multiple components. This strategy enables visualization of the strongest paths in a network.
