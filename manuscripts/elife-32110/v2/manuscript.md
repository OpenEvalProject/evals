# Functional genomics of lipid metabolism in the oleaginous yeast Rhodosporidium toruloides

## Authors

- Samuel T Coradetti<sup>1</sup> ([ORCID: 0000-0003-0173-0403](https://orcid.org/0000-0003-0173-0403))
- Dominic Pinel<sup>2</sup>
- Gina M Geiselman<sup>2</sup>
- Masakazu Ito<sup>2</sup>
- Stephen J Mondo<sup>3</sup> ([ORCID: 0000-0001-5797-0647](https://orcid.org/0000-0001-5797-0647))
- Morgann C Reilly<sup>4</sup>
- Ya-Fang Cheng<sup>2</sup>
- Stefan Bauer<sup>2</sup>
- Igor V Grigoriev<sup>3</sup>
- John M Gladden<sup>4</sup> ([ORCID: 0000-0002-6985-2485](https://orcid.org/0000-0002-6985-2485))
- Blake A Simmons<sup>4</sup>
- Rachel B Brem<sup>1</sup>
- Adam P Arkin<sup>2</sup> ([ORCID: 0000-0002-4999-2931](https://orcid.org/0000-0002-4999-2931)) †
- Jeffrey M Skerker<sup>2</sup> ([ORCID: 0000-0003-2653-1566](https://orcid.org/0000-0003-2653-1566)) †

### Affiliations

1. The Buck Institute for Research on Aging Novato United States
2. Energy Biosciences Institute Berkeley United States
3. United States Department of Energy Joint Genome Institute Walnut Creek United States
4. Joint BioEnergy Institute Emeryville United States
5. Chemical and Biological Processes Development Group Pacific Northwest National Laboratory Richland United States
6. Department of Plant and Microbial Biology University of California, Berkeley Berkeley United States
7. Environmental Genomics and Systems Biology Division Lawrence Berkeley National Laboratory Berkeley United States
8. Biological Systems and Engineering Division Lawrence Berkeley National Laboratory Berkeley United States
9. Department of Bioengineering University of California, Berkeley Berkeley United States

† Corresponding author

## Abstract

The basidiomycete yeast Rhodosporidium toruloides (also known as Rhodotorula toruloides) accumulates high concentrations of lipids and carotenoids from diverse carbon sources. It has great potential as a model for the cellular biology of lipid droplets and for sustainable chemical production. We developed a method for high-throughput genetics (RB-TDNAseq), using sequence-barcoded Agrobacterium tumefaciens T-DNA insertions. We identified 1,337 putative essential genes with low T-DNA insertion rates. We functionally profiled genes required for fatty acid catabolism and lipid accumulation, validating results with 35 targeted deletion strains. We identified a high-confidence set of 150 genes affecting lipid accumulation, including genes with predicted function in signaling cascades, gene expression, protein modification and vesicular trafficking, autophagy, amino acid synthesis and tRNA modification, and genes of unknown function. These results greatly advance our understanding of lipid metabolism in this oleaginous species and demonstrate a general approach for barcoded mutagenesis that should enable functional genomics in diverse fungi.

## Introduction

Rhodosporidium toruloides (also known as Rhodotorula toruloides [Wang et al., 2015]) is a basidiomycete yeast (subdivision Pucciniomycotina). Rhodotorula/Rhodosporidium species are widely distributed in the phyllosphere and diverse soils (Rosa and Peter, 2006; Sláviková et al., 2009; Butinar et al., 2005; Pulschen et al., 2015). They accumulate high concentrations of carotenoid pigments (Mata-Gómez et al., 2014; Lee et al., 2014), giving their colonies a distinctive orange, red, or pink hue. When R. toruloides is cultured under nitrogen (Zhu et al., 2012), sulfur (Wu et al., 2011), or phosphorus (Wu et al., 2010) limitation, it can accumulate as much as 70% of cellular biomass as lipids (Wiebe et al., 2012), primarily as triacylglycerides (TAG).

Eukaryotes accumulate neutral lipids in complex, dynamic organelles called lipid droplets. Lipid droplets emerge from the endoplasmic reticulum (ER) membrane as a core of TAG surrounded by sterol esters, a phospholipid monolayer derived from ER phospholipids, and a targeted ensemble of proteins mediating inter-organelle interaction, protein trafficking, cellular lipid trafficking and regulated carbon flux in and out of the lipid droplet (Walther and Farese, 2012; Farese and Walther, 2009; Gao and Goodman, 2015). Aberrant lipid droplet formation contributes to many human diseases (Krahmer et al., 2013a; Welte, 2015) and impacts cellular processes as diverse as autophagy (Shpilka et al., 2015) and mitosis (Yang et al., 2016). The propensity of R. toruloides to form large lipid droplets under a variety of conditions makes it an attractive platform to study conserved aspects of the cellular biology of these important organelles across diverse eukaryotes.

Rhodosporidium toruloides is also an attractive host for production of sustainable chemicals and fuels from low-cost lignocellulosic feedstocks. Wild isolates of R. toruloides can produce lipids and carotenoids from a wide variety of carbon sources including glucose (Wiebe et al., 2012), xylose (Wiebe et al., 2012), and acetate (Huang et al., 2016), as well as complex biomass hydrolysates (Fei et al., 2016). They are relatively tolerant to many forms of stress including osmotic stress (Singh et al., 2016) and growth-inhibiting compounds in biomass hydrolysates (Hu et al., 2009; Kitahara et al., 2014). Rhodosporidium toruloides has been engineered to produce lipid-derived bioproducts such as fatty alcohols (Fillet et al., 2015) and erucic acid (Fillet et al., 2017) from synthetic pathways. To enable more efficient production of terpene-derived and lipid-derived chemicals, it has also been engineered for enhanced carotenoid (Lee et al., 2016) and lipid (Zhang et al., 2016a) production. These efforts, while promising, have for the most part employed strategies adapted from those demonstrated in evolutionarily distant species such as Saccharomyces cerevisiae and Yarrowia lipolytica. To truly tap the biosynthetic potential of R. toruloides, a better understanding of the unique aspects of its biosynthetic pathways, gene regulation and cellular biology will be required.

Recently, transcriptomic and proteomic analysis of R. toruloides in nitrogen limited conditions (Zhu et al., 2012) identified over 2,000 genes with altered transcript abundance and over 500 genes with altered protein abundance during lipid accumulation. These genes included many enzymes involved in the TCA cycle, a putative PYC1/MDH2/Malic Enzyme NADPH conversion cycle (Wynn et al., 1999), fatty acid synthesis, fatty acid beta-oxidation, nitrogen catabolite repression, assimilation and scavenging, autophagy, and protein turnover. Proteomics of isolated lipid droplets (Zhu et al., 2015) identified over 250 lipid droplet-associated proteins including fatty acid synthesis genes, several putative lipases, a homolog of the lipolysis-regulating protein perilipin (Bickel et al., 2009), vesicle trafficking proteins such as Rab GTPases and SNARE proteins, as well as several mitochondrial and peroxisomal proteins.

While these studies were unambiguous advances for the field, significant work remains to establish the genetic determinants of lipid accumulation in R. toruloides. Differential transcript or protein abundance under nitrogen limitation is suggestive of function in lipid accumulation, but transcriptional regulation and gene function are often poorly correlated in laboratory conditions (Price et al., 2013). Similarly, sequestration in the lipid droplet may help regulate availability of some proteins for functions not necessarily related to lipid metabolism (Cermelli et al., 2006). More direct functional data would help the R. toruloides community prioritize this extensive list of genes for more detailed study and identify additional genes not identifiable by proteomic and transcriptomic methods. Finally, these studies highlighted dozens of genes with no known function, and hundreds more with only limited functional predictions. A more functional approach may yield more insights into unique aspects of R. toruloides biology.

Fitness analysis of gene deletion or disruption mutants within pooled populations is a flexible, powerful approach for elucidating gene function. In these experiments the relative growth rate of thousands of mutant strains are simultaneously measured by tracking the relative abundance of unique sequence identifiers for each mutant. These identifying sequences could be short sequence ‘barcodes’ inserted into targeted deletion mutants (Giaever et al., 2002), or genomic DNA flanking random transposon insertions (Sassetti et al., 2001). Early fitness experiments tracked strain abundance by hybridization of identifier sequences to DNA micro-arrays (Giaever et al., 2002; Sassetti et al., 2001). The advent of high-throughput sequencing and the development of broad host range transposons enabled more widespread use of fitness analysis in bacteria by direct sequencing of transposon insertion sites (TnSeq) (Gawronski et al., 2009; Langridge et al., 2009). The scalability and precision of TnSeq is improved when random sequence barcodes are added to each randomly integrated transposon (RB-TnSeq) (Wetmore et al., 2015). Once insertions sites have been mapped, strain abundance can then be more accurately measured with a simple, consistent PCR amplification of the barcode sequences from known priming sites (BarSeq).

TnSeq and RB-TnSeq have been employed extensively in bacteria (Kwon et al., 2016), and in a few eukaryotic species (Michel et al., 2017; Pettitt et al., 2017). Although some of the first barcoded fitness experiments were performed on mutant pools of S. cerevisiae (Giaever et al., 2002) and advances in TnSeq methods continue in that species (Michel et al., 2017), to date relatively low transformation efficiencies and a lack of functional transposon systems has limited the application of TnSeq and RB-TnSeq in most fungal species. Random mutagenesis of fungi by the bacterium Agrobacterium tumefaciens is one route to overcome these technical barriers. Agrobacterium tumefaciens, an opportunistic plant pathogen, has evolved an efficient system to transfer virulence genes into eukaryotic cells (Gelvin, 2003). Once in the host cell, these transfer DNAs (T-DNAs) integrate randomly into the genome (Bundock et al., 2002). Agrobacterium tumefaciens-mediated transformation (ATMT) has been used extensively in plants (Gelvin, 2003) and to transform diverse fungi at high efficiency (Bundock et al., 2002; Michielse et al., 2005; Walton et al., 2005; Kunitake et al., 2011; Sullivan et al., 2002; Blaise et al., 2007). Recently, Esher et al. used ATMT followed by mutant selection and high-throughput sequencing to identify several mutants with altered cell wall biosynthesis in the basidiomycete yeast Cryptococcus neoformans (Zhang et al., 2016a). The methods they employed were only viable for characterization of a small pool of highly enriched mutants, but they demonstrated an effective paradigm to bring high-throughput functional genomics to diverse fungi.

In this study, we demonstrate the construction of a randomly barcoded, random insertion library in R. toruloides by ATMT and its application for functional genomics (RB-TDNAseq). We report a list of 1,337 genes, including 36 unique to basidiomycetes, that were recalcitrant to T-DNA insertion, the first full genome survey of putatively essential genes in a basidiomycete fungus. We use our barcoded mutant library to explore fatty acid catabolism in R. toruloides, demonstrating its utility in rapidly assessing mutant phenotypes. We show that mitochondrial beta-oxidation is important for fatty acid utilization in this species and that some members of its expanded complement of peroxisomal acyl-CoA dehydrogenases are necessary for growth on different fatty acids, suggesting substrate specificity or conditional optimality for each enzyme. We investigate perturbed lipid accumulation in the mutant pool by fractionation of the population by buoyancy and fluorescence activated cell sorting. We identify 150 genes with significant roles in lipid accumulation, notably genes involved in signaling cascades (28 genes), gene expression (15 genes), protein modification or trafficking (15 genes), ubiquitination or proteolysis (nine genes), autophagy (nine genes), and amino acid synthesis (eight genes). We also find evidence that tRNA modification affects lipid accumulation in R. toruloides, identifying five genes with likely roles in thiolation of tRNA wobble residues. These results significantly advance our understanding of lipid metabolism in R toruloides; identify key biological processes that should be explored and optimized in any oleaginous yeast engineered for lipid production; support emerging evidence of deep connections between lipid droplet dynamics, vesicular trafficking, and protein sorting; and demonstrate a general approach for barcoded mutagenesis that should enable functional genomics in a wide variety of fungal species.

## Results

### A functional genomics platform for R. toruloides

To enable functional genomics in R. toruloides IFO 0880, we first improved the existing genome assembly and annotation (Zhang et al., 2016a) using a combination of long-read PacBio sequencing for a more complete de novo assembly, a more comprehensive informatics approach for gene model predictions and functional annotation, and manual refinement of those models using evidence from mRNA sequencing (Genbank accession LCTV02000000), also available at the Mycocosm genome portal (Grigoriev et al., 2014) (see Appendix 1 for details). Summary tables of gene IDs, predicted functions, and probable orthologs in other systems are included in Supplementary file 1. For brevity, we will refer to R. toruloides genes by the common name for their Saccharomyces cerevisiae orthologs (e.g. MET2) when such orthologous relationships are unambiguous. Otherwise, we will give the Mycocosm protein ID, e.g. RTO4_12154 and RTO4_14576 are both orthologs of GPD1.

Because no method existed for high-throughput genetics in R. toruloides, we adapted established protocols for mapping barcoded transposon insertions (RB-TnSeq) (Wetmore et al., 2015), to mapping barcoded T-DNA insertions introduced with Agrobacterium tumefaciens-mediated transformation (ATMT). We call this method RB-TDNAseq (Figure 1A). In brief, we generated a diverse library of binary ATMT plasmids bearing nourseothricin resistance cassettes with ~10 million unique 20 base-pair sequence ‘barcodes’ by efficient Type IIS restriction enzyme cloning (Engler et al., 2008), introduced the library into A. tumefaciens EHA105 by electroporation, then transformed R. toruloides with ATMT. Using a TnSeq-like protocol, we mapped the unique locations of 293,613 individual barcoded T-DNA insertions in the R. toruloides genome (see Appendix 1 for details). Once insertion sites were associated with their barcodes, pooled fitness experiments were performed using a simple, scalable BarSeq protocol as previously described (Wetmore et al., 2015).

![Figure 1.](https://cdn.elifesciences.org/articles/32110/elife-32110-fig1-v2.jpg)

**Figure 1.:** (A) General strategy of RB-TDNAseq. A library of binary plasmids bearing an antibiotic resistance cassette (NATR) and a random 20 base-pair sequence ‘barcode’ (N20) flanked by specific priming sites (P1/P2) is introduced into a population of A. tumefaciens carrying a vir helper plasmid. A. tumefaciens efficiently transforms a T-DNA fragment into the target fungus (ATMT). NATR colonies are then combined to make a mutant pool. T-DNA-genome junctions are sequenced by TnSeq, thereby associating barcodes with the location of the insertion (Map). The mutant pool is then cultured under specific conditions and the relative abundance of mutant strains is measured by sequencing a short, specific, PCR on the barcodes (BarSeq) and counting the occurrence of each sequence (Count). Finally, for each gene, count data is combined across all barcodes mapping to insertions in that gene to obtain a robust measure of relative fitness for strains bearing mutations in that gene (Fitness Estimation). (B) Histogram of insert density in coding regions (start codon to stop codon) for all genes, and genes with orthologs reported to be essential in A. nidulans, C. neoformans, N. crassa, S. cerevisiae, or S. pombe. The following figure supplements are available for Figure 1.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/32110/elife-32110-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** (A) In the TnSeq protocol, genomic DNA is sheared into ~300 bp fragments, and Illumina TruSeq adapters are ligated on both ends. T-DNA junctions are then specifically enriched by PCR with a T-DNA-specific and an adapter-specific primer. (B) In the BarSeq protocol, genomic DNA is used as a template for a more robust and quantitative PCR on the barcoded region of the T-DNA insert. Phasing error caused by the identical T-DNA sequences flanking the random barcodes was reduced by adding sequence diversity at the beginning of each read, either by the introduction of a short random 6 bp sequence or a 2–4 bp random sequence for TnSeq and BarSeq, respectively.

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/32110/elife-32110-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** (A) Inferred topology of T-DNA insertions from associations of barcodes and adjacent genomic or T-DNA sequence. Only three of the observed insertion types could be mapped using the TnSeq protocol. (B) Sanger sequencing of barcodes from single colonies isolated from the pool. Multiple overlapping peaks in the barcode region suggest multiple T-DNAs are present in a single strain. Note that these T-DNAs may be integrated at the same, or different loci. Inherent noise in barcode amplification and sequencing introduces significant ambiguity in this analysis. The inferred rate of multiple barcode insertion (29%) should be considered a maximum estimate.

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/32110/elife-32110-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** (A) Frequency of T-DNA insertion mapping was consistent across all 30 IFO 0880 scaffolds. (B) Histogram of GC content in 100 base pair regions flanking insertion sites and in random 100 base pair regions. (C) Proportion of the R. toruloides IFO 0880 genome in promoter regions, terminator regions, untranslated regions transcribed to mRNA, coding exons, and introns versus the proportion of T-DNA insertions mapped to those sequences. (D) Distribution of T-DNA insertion density across the length of scaffold 1. Total inserts were summed across a rolling 1,000 base pair window using the observed insertions and a simulated random mutant pool assuming biases for insertion in promoters, terminators and untranslated transcribed regions.

Insertions were sufficiently well dispersed to map at least one T-DNA in 93% of nuclear genes, despite some local and fine-scale biases in insertion rates (see Appendix 1 for details). Insertion density in coding regions followed an approximately normal distribution (as expected for random integration) centered on nine inserts per thousand base pairs, except for a subpopulation of genes with fewer than two inserts/kb (Figure 1B). These very low-insertion genes were highly enriched for orthologs of genes reported as essential in Aspergillus nidulans (Arnaud et al., 2012), Cryptococcus neoformans (Ianiri and Idnurm, 2015), Saccharomyces cerevisiae (Cherry et al., 2012), or Schizosaccharomyces pombe (Wood et al., 2012), or for which only heterokaryons could be obtained in the Neurospora crassa deletion collection (Colot et al., 2006). We therefore infer that the majority of these genes recalcitrant to T-DNA insertion are likely essential in our library construction conditions, or at least that mutants for these genes have severely compromised growth. Based on the above criterion, we identified 1,337 probable essential genes, which we report in Supplementary file 1. This list includes over 400 genes not reported as essential in the above-mentioned model fungi and is enriched for genes with homologs implicated in mitochondrial respiratory chain I assembly and function, dynein complex, the Swr1 complex, and mRNA nonsense mediated decay. For a full list of GO term enrichments see Supplementary file 1. This list also includes 36 genes unique to basidiomycetes.

### Mapping biosynthetic pathways using RB-TDNAseq

Before investigating more novel aspects of R. toruloides’ biology, we tested if RB-TDNAseq could be used to correctly identify gene function in well-conserved amino acid biosynthetic pathways. We cultured the mutant pool in defined medium (DM), consisting of glucose and yeast nitrogen base without amino acids and in DM supplemented with ‘drop-out mix complete’ (DOC), a mix of amino acids, adenine, uracil, p-aminobenzoic acid, and inositol. To establish if RB-TDNAseq could produce statistically robust results with minimal experimental replication, we recovered three independent starter cultures from frozen aliquots of the mutant pool and used each replicate to inoculate both supplemented and non-supplemented cultures. We grew these cultures for seven generations and measured fitness across the mutant pool with BarSeq.

Secondary mutations are prevalent even in well-curated mutant collections (Comyn et al., 2017) and ATMT can introduce several types of confounding mutations (see Appendix 1 for details). To mitigate the influence of such mutations on our analysis, we adapted the established methods and software of Wetmore et al. (Wetmore et al., 2015; Price et al., 2016; Cole et al., 2017; Sagawa et al., 2017) for our BarSeq analysis. These algorithms compute a fitness score for each mutant strain as a log2 ratio of abundance in the experimental condition to abundance in a ‘Time 0’ sample from its seed culture. A composite fitness score (F) is then computed for each gene by combining multiple fitness scores from strains bearing insertions in that gene. A ‘moderated T-statistic’ calculated from the average and variance of strain fitness scores indicates the consistency of F across strains and experiments. See the Materials and methods section and (Wetmore et al., 2015) for more information on how these metrics are calculated. For more information on sequencing depth, behavior of T-statistics and detailed examples of how individual strain fitness scores contribute to F, see Appendix 1. All fitness scores and T-statistics (combined across biological replicates) are available in Supplementary file 2 and online in a dynamic fitness browser, adapted from (Price et al., 2016): http://fungalfit.genomics.lbl.gov/.

Different aliquots of the mutant pool have subtly different starting compositions and experience stochastic variations in the length of lag phase as they recover from frozen stocks. Subtle variations in Illumina library preparation and sequencing for samples processed at different times may add further batch-specific biases to count data. For these reasons, direct comparisons of BarSeq counts between conditions tested in different batches and seeded from different starter cultures are not advisable. Expressing the data as F and T relative to Time 0 reduces it to a more portable format, allowing for comparisons of mutant fitness across conditions not necessarily tested in the same experiment. Given F and T in two different conditions (FC1, TC1 and FC2, TC2), we calculate relative fitness FC1-C2 = FC1-FC2 and relative T-statistics TC1-C2 = (FC1-FC2)/sqrt(var(FC1)+var(FC2)).

Fitness scores for 6,558 genes in cultures grown on DM and DM supplemented with DOC are shown in Figure 2A. Mutants for 28 genes had fitness scores suggesting auxotrophy: fitness defects in non-supplemented media (FDM < −1) with consistently different scores in supplemented versus non-supplemented media (TDM-DOC < −3). When we grew the mutant pool in defined media with methionine or arginine supplementation (Figure 2B), the 28 auxotrophic mutants partitioned into 11 mutants rescued by methionine, eight mutants rescued by arginine, seven mutants rescued by neither amino acid and two mutants rescued by both amino acids. All of the identified methionine and arginine auxotrophic mutants have orthologous genes for which mutants are auxotrophic for methionine/cysteine or arginine, respectively, in S. cerevisiae or A. nidulans. Alternatively, when we hierarchically clustered the fitness scores for genes with F < −1 and T < −3 versus Time 0 in any supplementation condition (Figure 2C), the resulting clusters included twelve and nine mutants rescued by methionine and arginine respectively; this was a nearly complete recovery of genes with predicted functions in this pathway (shown in Figure 2D–E with additional discussion in Appendix 1). Based on these data, we chose |T| > 3 as a conservative threshold for consistent, reliable fitness scores in further BarSeq experiments.

![Figure 2.](https://cdn.elifesciences.org/articles/32110/elife-32110-fig2-v2.jpg)

**Figure 2.:** (A) Fitness scores for 6,558 genes in media with and without amino acid supplementation (drop-out complete mix). Gene fitness scores are log ratios of final versus starting abundance averaged over multiple barcoded insertions per gene across three biological replicates. Genes that had consistently different enrichment scores between treatments (∆F > 1, |T| statistic >3) are highlighted and represent genes for which mutant strains are auxotrophic for one or more amino acids, nucleotides, or vitamins present in the drop-out complete mixture. (B) Fitness scores in media supplemented with arginine or methionine. Highlighted genes are the same as highlighted in (A). Deletion strains for circled or boxed genes are auxotrophic for methionine or arginine, respectively, in S. cerevisiae or A. nidulans. See Supplementary file 2 for full fitness data. (C) Hierarchical clusters of fitness scores in supplemented and non-supplemented media. Fitness scores for each biological replicate versus its Time 0 replicate for genes with a consistent fitness defect (F < −1, T < −3) in one or more of the following conditions: Yeast extract/Peptone/Dextrose media (YPD) or defined media (DM, composed of yeast nitrogen base plus glucose) with or without the following supplements: (+DOC), arginine (+ARG), or methionine (+MET). (D) Sulfur amino acid biosynthesis in R. toruloides as inferred from fitness experiments. CysA/CysB are named according to their A. nidulans orthologs, all others by orthologs in S. cerevisiae. Auxotrophic mutants had F < −1 in non-supplemented media (DM) and T < −3 in DM versus supplemented media (DOC). Multiple insertions were mapped in STR3, suggesting non-essentiality, but strain abundance was too low to estimate fitness in BarSeq data. *MET16 had fitness scores that clustered with the other auxotrophic mutants, but TDM-DOC was −2.7. **Fitness scores for insertions in MET8 were not inconsistent with auxotrophy, but only two insertions were abundant enough to be tracked. 5MTHTG: 5-methyltetrahydropteroyltri-L-glutamate, THTG: tetrahydropteroyltri-L-glutamate, SAM: S-adenosyl-L-methionine, SAH: S-adenosyl-homocysteine, APS: adenylyl-sulfate, PAPS: 3'-phosphoadenylyl-sulfate. (E) Arginine biosynthesis in R. toruloides as inferred from fitness experiments. *ARG8 had fitness scores that clustered with the other auxotrophic mutants, but TDM-DOC was −2.9. NAG: N-acetylglutamate, NAGSA: N-acetylglutamate semialdehyde, NAAO: N-alpha-acetylornithine. The following figure supplements are available for Figure 2.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/32110/elife-32110-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (A) Histogram of barcode abundance in a typical BarSeq experiment with 20 million reads per sample. (B) Histogram of tracked barcodes per gene in a typical BarSeq experiment. Median seven barcodes per gene, 68,021 total barcodes in 6,558 genes. See Supplementary file 1 for a full list of insert density by gene and orthologs reported as essential in model fungi. (C) Histogram of total reads per sample per gene in a typical experiment. This is the sum of counts for all the barcodes that were used in gene fitness estimation for each gene, averaged across all samples.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/32110/elife-32110-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** (A) Raw counts for barcoded insertions inside and flanking the coding region for RTO4_9377 ARG5 in Time 0 samples and after growth in non-supplemented defined media (DM). The gene structure is shown below the plot with coding exons as large blue boxes and five prime/three prime untranslated regions as smaller blue boxes. The location of each insertion is noted with a black line between the gene model and the corresponding data on the bar chart. Counts from each biological replicate for each insertion are clustered together in the order they were mapped to the gene. The dark grey area of the plot indicates insertions in the central 80% of the coding region, and the flanking area in light grey indicates insertions in the first or last 10% of the coding region. (B) Fitness scores for individual insertions in ARG5, plotted in the same order as (A). The height of the bar indicates the fitness score derived from the log2 ratio of counts shown in (A). Shading of the bar indicates the weight assigned to each insertion in calculating F for the gene. F and T for each individual replicate and the average F and combined T for this condition are displayed above the plot. (C) Raw counts for insertions in ARG5 in Time 0 and after growth in arginine-supplemented media (+DOC: DM plus drop-out complete mix). (D) Fitness scores for ARG5 on arginine-supplemented media (+DOC). (E) Raw counts for insertions in RTO4_11741 MET16 on non-supplemented media. (F) Fitness scores for insertions in MET16 on non-supplemented media. (G) Raw counts for insertions in MET16 on methionine-supplemented media (+DOC). (H) Fitness scores for insertions in MET16 on methionine-supplemented media (+DOC).

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/32110/elife-32110-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** (A) Distributions of T-statistics for mock comparisons between individual replicate Time 0 samples from our auxotrophy experiments, shown as a quantile-quantile (QQ) plot. A perfect fit to the standard normal distribution would be on the x = y line (dashed grey line). (B) Distributions of T-statistics for mock comparisons between shuffled sets of Time 0 samples from three experiments, shown as a quantile-quantile plot. (C) Histogram of gene lengths for all genes with sufficient data to compute fitness scores, and for observations with |T| > 3 versus Time 0 for combined T-statistics across biological triplicates. (D) Histogram of the number of inserts per gene with sufficient depth in BarSeq experiments to contribute to fitness estimation. All genes and observations with |T| > 3 versus Time 0 for combined T-statistics across biological triplicates. (E) Histogram of total counts per gene per sample for all genes and for observations with |T| > 3 versus Time 0 for combined T-statistics across biological triplicates. (F) Histogram of GC content for all genes and for observations with |T| > 3 versus Time 0 for combined T-statistics across biological triplicates. (G) Average fitness score and T-statistics for observations with |T| > 3 versus gene length. Fitness scores and T-statistics were binned by gene length in intervals of 500 bp and averaged across each bin.

### Fatty acid catabolism in R. toruloides

We next sought to understand how R. toruloides utilizes distinct fatty acids as growth substrates, as a window onto the complex lipid metabolism in this fungus. For this purpose, we used RB-TDNAseq to measure mutant fitness on three fatty acids as the sole carbon source: oleic acid (the most abundant fatty acid in R. toruloides [Li et al., 2007]) ricinoleic acid (a high-value fatty acid produced naturally in plants (Dyer et al., 2008) and synthetically in fungi [Holic et al., 2012]), and methyl ricinoleic acid (a ricinoleic acid derivative used in lactone production [Endrizzi et al., 1996]). A total of 129 genes had consistently low fitness scores on one or more fatty acids including genes implicated in beta-oxidation of fatty acids, gluconeogenesis, mitochondrial amino acid metabolism, and several other aspects of cellular metabolism and gene regulation (See Figure 3—figure supplement 1 and Appendix 1 for a clustering analysis of fitness scores for these genes and Supplemental file 2 for a complete list).

We were particularly interested in beta-oxidation of fatty acids in the peroxisome and mitochondria, as these pathways are critical for lipid homeostasis (Kohlwein et al., 2013; Rambold et al., 2015), with major implications for both human health (Houten et al., 2016; Waterham et al., 2016) and metabolic engineering in fungi (Dulermo and Nicaud, 2011; Beopoulos et al., 2014). Fitness scores for R. toruloides genes homologous to enzymes with known roles in beta-oxidation of fatty acids are shown in Figure 3A. The localization for these enzymes is inferred mostly from observations in distantly related species, but orthologs of five enzymes localized to the predicted compartments in the basidiomycete yeast Ustilago maydis (Camões et al., 2015) adding some confidence to these predicted locations.

![Figure 3.](https://cdn.elifesciences.org/articles/32110/elife-32110-fig3-v2.jpg)

**Figure 3.:** (A) Heatmap of fitness scores for R. toruloides genes with predicted roles in beta-oxidation of fatty acids. Enzyme classes and predicted locations were inferred from homologous proteins in Ustilago maydis as reported by Camões et al. (Camões et al., 2015). See Supplementary file 2 for full fitness data. (B) Log2 optical density ratio for single deletion mutants versus the YKU70∆ control strain at mid-log phase on 1% oleic acid as carbon source are plotted against the fitness scores for each gene from BarSeq experiments on 1% oleic acid. (C) Log2 optical density ratio for single deletion mutants versus the YKU70∆ control strain at mid-log phase on 1% ricinoleic acid as carbon source are plotted against the fitness scores for mutants in each gene from BarSeq experiments on 1% ricinoleic acid. See Supplementary file 2 for a statistical summary for all strains shown in (B) and (C), including P values and effect sizes. The following figure supplements are available for Figure 3.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/32110/elife-32110-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** Fitness scores for individual biological replicates were clustered in this analysis (six replicates on glucose, three for each fatty acid). OA: oleic acid, RA: ricinoleic acid, MRA: methyl ricinoleic acid. Seven clusters were identified based on carbon utilization patterns; FA1 - fitness defects on all fatty acids, FA2 and FA3 - fitness defects on MRA and RA, FA4 and FA5 – fitness defects on RA only, FA6 – fitness defects on MRA only, and FA7 – fitness defects on OA only. Major categories of predicted gene functions are summarized for the clusters. See Supplementary file 2 and 3 for full fitness data and gene ontology enrichments.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/32110/elife-32110-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** Fitness scores for genes with predicted roles in mitochondrial and peroxisomal beta-oxidation are represented by the width of green or blue borders around each protein, with wider borders corresponding to lower fitness scores. Green and blue borders represent fitness on oleic and ricinoleic acid, respectively. Fitness scores on fatty acids were consistently most severe for a few genes predicted to mediate steps in mitochondrial beta-oxidation with little to no predicted redundancy in the R. toruloides genome. Fitness scores were more variable between different fatty acids for peroxisomal enzymes, for which more paralogs are present.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/32110/elife-32110-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** Growth curves for deletion mutants of (A) RTO4_14567 (similar to H. sapiens ACAD11), (B) RTO4_8963 (similar to H. sapiens ACAD11), and (C) RTO4_8673 (similar to PEX11) on 1% oleic acid and 1% ricinoleic acid as the sole carbon source. See Supplementary file 2 for a statistical summary for all strains including P values and effect sizes.

Mutants for mitochondrial enzymes had the most consistent fitness scores across all three fatty acids, whereas mutants for the peroxisomal enzymes and peroxins had more variable fitness scores among fatty acids. Mutants for seven peroxisomal beta-oxidation enzymes and three peroxins had different fitness scores on oleic acid versus ricinoleic acid and methylricinoleic acid (listed in Appendix 1, full fitness scores in Supplementary file 2), while 11 other predicted peroxisomal beta-oxidation enzymes had no consistent fitness scores at all. These results demonstrate how RB-TDNAseq can be used to rapidly identify condition-specific phenotypes among closely related members of a gene family. All together our data are consistent with a model of fatty acid beta-oxidation in R. toruloides in which diverse long-chain fatty acids are shortened in the peroxisome and a less structurally diverse set of short-chain fatty acids are oxidized to acetyl-CoA in the mitochondria (Figure 3—figure supplement 2).

To validate our fitness data on fatty acids, we made targeted deletion mutants for several predicted peroxisomal and mitochondrial proteins by homologous recombination into a non-homologous end joining deficient YKU70∆ strain (also known as KU70) (Ninomiya et al., 2004; Zhang et al., 2016b). We grew these mutant strains on oleic or ricinoleic acid media and compared their growth to the parental YKU70∆ strain in mid-log phase. Relative growth for the deletion strain for each gene is compared to its fitness scores in the BarSeq experiment in Figure 3B and Figure 3C. The PEX7∆ mutant had similar fitness defects on both fatty acids, but mutants for RTO4_8673 (similar to PEX11) and RTO4_14567 (similar to H. sapiens ACAD11), had stronger fitness defects on ricinoleic acid, and the mutant for acyl-CoA dehydrogenase RTO4_8963 had stronger fitness defects on oleic acid as predicted from fitness scores. Over a 96 hr time course, the RTO4_14567∆ mutant failed to grow at all on ricinoleic acid, whereas the RTO4_8963∆ mutant and the PEX11 homolog RTO4_8673∆ mutant had more subtle phenotypes, approaching the same final density of the YKU70∆ control strain after a longer growth phase (Figure 3—figure supplement 3). These data showed that BarSeq fitness scores were reliable predictors of significant growth defects for mutants in pure culture.

### Functional genomics of lipid accumulation in R. toruloides

To dissect the genetic basis of lipid accumulation in R. toruloides, we induced lipid accumulation by nitrogen limitation (R. toruloides lipid droplets visualized in Figure 4A), and used two measures of cellular lipid content to fractionate the mutant pool (Figure 4B and Appendix 1). We used the neutral-lipid stain BODIPY 493/503 (Bozaquel-Morais et al., 2010) and fluorescence activated cell sorting (FACS) to enrich populations with larger/more or smaller/fewer lipid droplets (Terashima et al., 2015). We also used buoyancy separation on sucrose gradients to enrich for populations with higher or lower total lipid content (Eroglu and Melis, 2009; Kamisaka et al., 2006; Liu et al., 2015). Because many mutations can affect cell buoyant density independent of lipid accumulation (Novick et al., 1980; Bryan et al., 2010), we also grew the mutant pool in rich media (YPD) and subjected it to sucrose gradient separation as a control for lipid-independent buoyancy phenotypes. For each pair of high and low lipid fractions, we then calculated an ‘enrichment score’, E, and T-statistic for each gene. E is analogous to our fitness scores based on growth, except that it is the log2 ratio of abundance in the high lipid fraction to the low lipid fraction, whereas F is the log2 ratio of final to initial abundance. Hierarchical clusters of enrichment scores for 271 genes for which mutants have consistently altered lipid accumulation (|E| > 1 and |T| > 3) are shown in Figure 5A. Enrichment scores and T-statistics for all 6,558 genes with sufficient BarSeq data are reported in Supplementary file 2.

![Figure 4.](https://cdn.elifesciences.org/articles/32110/elife-32110-fig4-v2.jpg)

**Figure 4.:** (A) Lipid accumulation in R. toruloides under nitrogen limitation. DIC microscopy of R. toruloides grown in low nitrogen media for 40 hr and stained with BODIPY 493/503 to label lipid droplets. (B) Two strategies to enrich populations for high or low TAG content cells. (Top) Buoyant density separation on sucrose gradients. Lipid accumulated cells are loaded onto a linear sucrose gradient and centrifuged. Cells settle at their neutral buoyancy, with the size of the low-density lipid droplet as the main driver of buoyancy differences. The gradient is then split into several fractions, and fractions representing the most and least buoyant 5–10% of the population, as well as a no-separation control are subjected to DNA extraction and strain quantification with BarSeq. For each gene an enrichment score is calculated as the log2 ratio of mutant abundance in the high buoyancy versus low buoyancy fractions. (Bottom) FACS sorting on BODIPY signal. Cells cultured in lipid accumulation conditions (limited nitrogen) are stained with BODIPY 493/503, then sorted in a FACS system. The 10% of the population with the highest and lowest BODIPY signal are sorted into enriched populations, as well as non-gated control. These small populations (10 million cells each) are then cultured for additional biomass and subjected to DNA extraction and strain quantification with BarSeq. For each gene, a FACS enrichment score is calculated as the log2 ratio of mutant abundance in the high BODIPY versus low BODIPY fractions. The following figure supplements are available for Figure 4.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/32110/elife-32110-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A) Total fatty acid methyl ester (FAME) content in R. toruloides cultures, quantified using gas chromatography and flame ionization detection (GC-FID), correlates with average cellular BODIPY signal determined by flow cytometry. (B) Standards used for quantification of FAME content. Peak area/concentration ratios for ten commercially available fatty acid standards were used to quantify FAME peaks from experimental samples. (C) Example FAME profile for IFO 0880. Peak area/concentration ratios for C18:2 were used to quantify C18:3.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/32110/elife-32110-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (A) Time course of lipid accumulation (measured by BODIPY intensity) in nitrogen limited media (C/N 120; 12, 40, and 88 hr). Rich media control shown for comparison (YPD at 40 hr). Kernel Density plots for three biological replicates are shown for each growth condition. (B) Time course of buoyant density on sucrose gradients in nitrogen limited media (C/N 120; 18, 40, and 110 hr). Rich media control shown for comparison (YPD at 40 hr). Relative cell numbers were measured by OD 600 nm. Density was measured directly by weight of a 100 µl sample.

![Figure 5.](https://cdn.elifesciences.org/articles/32110/elife-32110-fig5-v2.jpg)

**Figure 5.:** (A) Hierarchical clusters of enrichment scores for 271 genes with consistent enrichment (|E| > 1, |T| > 3) in high/low fractions separated by buoyant density or FACS sorting of BODIPY stained cells after lipid accumulation on low nitrogen media. Enrichment scores for individual biological replicates (three per condition) were clustered in this analysis. Eight major clusters were identified (LA1-LA8). See Supplementary file 2 for full enrichment data. (B and C) Relative BODIPY signal for deletion mutants. Points are the average BODIPY/cell for 10,000 cells from independent biological replicate cultures normalized to three control YKU70∆ cultures processed on the same day. Three biological replicates were processed for each strain in any given experiment and each strain was included in at least two experiments processed on different days (N ≥ 6). A statistical summary for all strains including N, P values, and effect sizes is included in Supplementary file 2. **p<0.01, *p<0.05 by homoscedastic T-test versus YKU70∆. 1Human homolog, 2C. neoformans homolog, 3A. nidulans homolog. The following figure supplements are available for Figure 5.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/32110/elife-32110-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** Relative levels of tRNA thiolation for S. cerevisiae mutants as reported by Huang et al. (Huang et al., 2008) versus enrichment scores for orthologous R. toruloides genes in the FACS separation experiment after lipid accumulation. Low lipid content (i.e. negative enrichment scores) for R. toruloides mutants corresponds to lower levels of tRNA thiolation in S. cerevisiae mutants.

To assess the reliability of these enrichment scores in predicting phenotypes for null mutants, we constructed 29 single gene deletion mutants by homologous recombination in a YKU70∆ strain of IFO 0880 and measured lipid accumulation by average BODIPY fluorescence for 10,000 cells from each strain using flow cytometry. Figure 5B and C show relative BODIPY signal for targeted deletion mutants versus the YKU70∆ parental strain (see Appendix 1 for more information on normalization and power analysis). When enrichment scores from both assays were strongly positive (LA1), we found that 7 of 8 deletion mutants had the expected phenotype (i.e. increased lipid accumulation). When only one assay yielded a strongly positive score (clusters LA2 and LA3), only 3 of 5 mutants had apparent increases in lipid content as measured by flow cytometry. Further, for the two mutants for genes in cluster LA3 with the greatest apparent increase in lipid content (PMT4 and RTO4_10302, similar to C. neoformans CMT1) that measurement was likely an artifact of incomplete cell separation. Both mutants formed long chains of cells (see Figure 7—figure supplement 1 for microscopy images), which would be analyzed as a single cell by our FACS assay. Genes in clusters LA4 and LA5 had conflicting enrichment scores between the two assays. Of three targeted deletion strains for genes in these clusters, only one (CCC1∆) had a statistically significant phenotype, with decreased lipid accumulation. When the FACS assay gave a strongly negative score and there was no strong contrary buoyancy score (clusters LA6, LA7, and LA8), 11 of 13 mutants had reduced lipid accumulation. These data confirm that both separation techniques are fundamentally sound, though in isolation each method has a significant rate of false positives. In combination, the two assays identified a large set of high-confidence candidate genes with important roles in lipid accumulation.

### Diverse predicted functions for lipid accumulation mutants

We manually curated homology-based predicted functions for the 393 genes with consistent fitness or enrichment scores in this study (Supplementary file 1). An overview of predicted localizations and functions for genes we identified with roles in fatty acid utilization or lipid accumulation is shown in Figure 6, with more detail for mutants with increased and decreased lipid accumulation in Tables 1 and 2, respectively. Note that we have excluded genes for which only one enrichment technique indicated altered lipid accumulation from this analysis.

![Figure 6.](https://cdn.elifesciences.org/articles/32110/elife-32110-fig6-v2.jpg)

**Figure 6.:** Key metabolic pathways and cellular functions mediating lipid metabolism as identified from fitness scores on fatty acid and enrichment scores from lipid accumulation screens. Fitness and/or enrichment scores for individual genes are depicted graphically by relative size of hexagonal, circular or star icons respectively. Only fitness scores for genes with consistent growth defects on at least one fatty acid (see Supplementary file 2) and enrichment scores from high confidence clusters (see Figure 5 and Supplementary file 2) are shown. Enrichment scores were averaged between buoyancy and FACS experiments, except for genes with confounding enrichment scores in rich media conditions, for which only FACS data were averaged. Positive scores (orange circles) represent genes for which mutants have increased lipid accumulation. Negative fitness scores (blue stars) represent genes for which mutants have decreased lipid accumulation. Genes detected in proteomics of R. toruloides lipid droplets by Zhu et al. (RAC1, GUT2, PLIN1, EGH1, RIP1, MGL2, AAT1, CIR2, MLS1, and RTO4_8963) or found in lipid droplets of many organisms (DGA1 and BSCL2) (see Supplementary file 5) are depicted under ‘Lipid Droplet’ and also their molecular functions, e.g. ‘G Protein Switches’ for RAC1. The following figure supplements are available for Figure 6.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/32110/elife-32110-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** Model pathway illustrating genes involved in glycolysis, triacylglyceride (TAG) synthesis, and cytosolic NAD+/NADH balance during TAG synthesis. Genes for which mutants had altered lipid accumulation (enrichment scores in clusters LA1, LA6, LA7, or LA8) are highlighted in orange or blue. Genes with low rates of T-DNA insertion (essential genes and genes for which mutants have a strong growth defect) are highlighted in grey. The primary source of NADPH in R. toruloides remains unclear (see Appendix 1 for detail). Speculative pathways mediating NADPH production are indicated with dashed grey arrows. DAG: diacylglycerol, PA: phosphatidic acid, LPA: lysophosphatidic acid, G3P: glycerol-3-phosphate, DHAP: dihydroxy-acetone-phosphate, GADP: glycerate 3-phosphate, 1,3BPG: 1,3-bisphosphoglycerate, 3 PG: 3-phosphoglycerate, 2 PG: 2-phosphoglycerate, PEP: phosphoenolpyruvate, OAA: oxaloacetate.

**Table 1.**
 Predicted gene function: Mutants with increased lipid accumulation.Predicted functions for genes for which mutants were high-confidence candidates for increased lipid accumulation (enrichment scores clustered in LA1, Figure 5).


<table>
  <thead>
    <tr>
      <th rowspan="2"></th>
      <th rowspan="2">Gene ID</th>
      <th rowspan="2">Short name</th>
      <th rowspan="2">Annotation from</th>
      <th rowspan="2">Description</th>
      <th colspan="2">Enrichment</th>
    </tr>
    <tr>
      <th>BD</th>
      <th>FACS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="3">G Protein Switches</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>*</td>
      <td>RTO4_15883</td>
      <td>RAS1</td>
      <td>S. cerevisiae</td>
      <td>GTPase</td>
      <td>2.0</td>
      <td>2.3</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_14088</td>
      <td>RAC1</td>
      <td>H. sapiens</td>
      <td>GTPase</td>
      <td>2.0</td>
      <td>0.9</td>
    </tr>
    <tr>
      <td>*</td>
      <td>RTO4_16215</td>
      <td>GNAI1-like</td>
      <td>H. sapiens</td>
      <td>GTPase</td>
      <td>1.6</td>
      <td>1.0</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_11402</td>
      <td>gapA</td>
      <td>A. nidulans</td>
      <td>GTPase-activating protein</td>
      <td>0.6</td>
      <td>1.4</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_13336</td>
      <td>RIC8A</td>
      <td>H. sapiens</td>
      <td>Guanine nucleotide exchange factor</td>
      <td>1.3</td>
      <td>1.4</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_16170</td>
      <td>sif-like</td>
      <td>D. melanogaster</td>
      <td>Guanine nucleotide exchange factor</td>
      <td>1.5</td>
      <td>0.9</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_16644</td>
      <td>BMH1</td>
      <td>S. cerevisiae</td>
      <td>14-3-3 protein</td>
      <td>1.3</td>
      <td>2.2</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_16068</td>
      <td>BMH1</td>
      <td>S. cerevisiae</td>
      <td>14-3-3 protein</td>
      <td>0.7</td>
      <td>1.2</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="3">Kinases and Phosphatases</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_13246</td>
      <td>CNA1</td>
      <td>S. cerevisiae</td>
      <td>Phosphatase (Calcineurin catalytic subunit)</td>
      <td>0.8</td>
      <td>1.2</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_11675</td>
      <td>CNB1</td>
      <td>S. cerevisiae</td>
      <td>Phosphatase (Calcineurin regulatory subunit)</td>
      <td>1.1</td>
      <td>1.2</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_11667</td>
      <td>PTC1</td>
      <td>S. cerevisiae</td>
      <td>Phosphatase</td>
      <td>0.9</td>
      <td>1.2</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_10638</td>
      <td>CLA4</td>
      <td>S. cerevisiae</td>
      <td>Kinase</td>
      <td>3.4</td>
      <td>4.5</td>
    </tr>
    <tr>
      <td>*</td>
      <td>RTO4_16605</td>
      <td>TPK1</td>
      <td>S. cerevisiae</td>
      <td>Kinase</td>
      <td>1.1</td>
      <td>0.5</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="2">Gene Expresssion</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_10333</td>
      <td>SET1</td>
      <td>S. cerevisiae</td>
      <td>Chromatin modifying</td>
      <td>3.0</td>
      <td>1.1</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_10279</td>
      <td>BRE2</td>
      <td>S. cerevisiae</td>
      <td>Chromatin modifying</td>
      <td>2.5</td>
      <td>1.0</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_12689</td>
      <td>SPP1</td>
      <td>S. cerevisiae</td>
      <td>Chromatin modifying</td>
      <td>2.0</td>
      <td>1.3</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_15412</td>
      <td>RCO1</td>
      <td>S. cerevisiae</td>
      <td>Chromatin modifying</td>
      <td>3.5</td>
      <td>1.6</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_10209</td>
      <td>MIT1-like</td>
      <td>S. cerevisiae</td>
      <td>Transcripition factor</td>
      <td>1.4</td>
      <td>0.3</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_14550</td>
      <td>CYC8</td>
      <td>S. cerevisiae</td>
      <td>Transcription factor</td>
      <td>3.7</td>
      <td>3.8</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_10274</td>
      <td>SKN7-like</td>
      <td>S. cerevisiae</td>
      <td>Transcription factor</td>
      <td>2.2</td>
      <td>1.5</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_13346</td>
      <td>CBC2</td>
      <td>S. cerevisiae</td>
      <td>RNA splicing factor</td>
      <td>1.6</td>
      <td>1.2</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="3">Protein Modification</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_11272</td>
      <td>ALG12</td>
      <td>S. cerevisiae</td>
      <td>Alpha-1,6-mannosyltransferase</td>
      <td>3.5</td>
      <td>1.7</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_14881</td>
      <td>CAP10-like</td>
      <td>C. neoformans</td>
      <td>Xylosyltransferase</td>
      <td>1.5</td>
      <td>2.0</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_16598</td>
      <td>LARGE1</td>
      <td>H. sapiens</td>
      <td>N-acetylglucosaminyltransferase-like protein</td>
      <td>1.8</td>
      <td>1.3</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="3">Protein Trafficking</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_12145</td>
      <td>ERP1</td>
      <td>S. cerevisiae</td>
      <td>COPII cargo adapter protein (p24 family)</td>
      <td>2.4</td>
      <td>2.7</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_16731</td>
      <td>ERP2</td>
      <td>S. cerevisiae</td>
      <td>COPII cargo adapter protein (p24 family)</td>
      <td>1.7</td>
      <td>2.0</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_12521</td>
      <td>EMP24</td>
      <td>S. cerevisiae</td>
      <td>COPII cargo adapter protein (p24 family)</td>
      <td>1.9</td>
      <td>2.4</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_14054</td>
      <td>BST1</td>
      <td>S. cerevisiae</td>
      <td>GPI inositol-deacylase</td>
      <td>1.5</td>
      <td>0.2</td>
    </tr>
    <tr>
      <td>*</td>
      <td>RTO4_15883</td>
      <td>RAS1</td>
      <td>S. cerevisiae</td>
      <td>GTPase</td>
      <td>2.0</td>
      <td>2.3</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="3">Other ER/Golgi Proteins</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_10371</td>
      <td>KDELC1-like</td>
      <td>H. sapiens</td>
      <td>Endoplasmic reticulum protein EP58</td>
      <td>3.1</td>
      <td>6.0</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_15763</td>
      <td></td>
      <td></td>
      <td>SH3 Domain-containing ER Protein</td>
      <td>1.0</td>
      <td>1.5</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="3">Amino Acid Biosynthesis</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_11050</td>
      <td>MET1</td>
      <td>S. cerevisiae</td>
      <td>Uroporphyrinogen III transmethylase</td>
      <td>3.8</td>
      <td>2.0</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_8744</td>
      <td>MET5</td>
      <td>S. cerevisiae</td>
      <td>Sulfite reductase</td>
      <td>4.4</td>
      <td>2.1</td>
    </tr>
    <tr>
      <td>§</td>
      <td>RTO4_10374</td>
      <td>MET10</td>
      <td>S. cerevisiae</td>
      <td>Sulfite reductase</td>
      <td>2.5</td>
      <td>1.3</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_8709</td>
      <td>MET14</td>
      <td>S. cerevisiae</td>
      <td>Adenylylsulfate kinase</td>
      <td>4.1</td>
      <td>1.1</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_11741</td>
      <td>MET16</td>
      <td>S. cerevisiae</td>
      <td>Phosphoadenosine phosphosulfate reductase</td>
      <td>1.7</td>
      <td>1.1</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_12031</td>
      <td>cysB</td>
      <td>A. nidulans</td>
      <td>Cysteine synthase A</td>
      <td>3.3</td>
      <td>2.1</td>
    </tr>
    <tr>
      <td>*</td>
      <td>RTO4_16196</td>
      <td>ARG1</td>
      <td>S. cerevisiae</td>
      <td>Argininosuccinate synthase</td>
      <td>1.3</td>
      <td>1.8</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="2">Translation</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_12273</td>
      <td>MRN1</td>
      <td>S. cerevisiae</td>
      <td>RNA-binding protein</td>
      <td>2.5</td>
      <td>1.6</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_8595</td>
      <td>EIF4E2</td>
      <td>H. sapiens</td>
      <td>Translation initiation factor</td>
      <td>2.0</td>
      <td>0.5</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="3">Ubiquitination and Proteolysis</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_11150</td>
      <td>Mub1-like</td>
      <td>S. cerevisiae</td>
      <td>Ubiquitin ligase complex member</td>
      <td>3.8</td>
      <td>2.0</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_15576</td>
      <td>CDC4</td>
      <td>S. cerevisiae</td>
      <td>Ubiquitin ligase complex member</td>
      <td>1.7</td>
      <td>1.8</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="3">Triacylglyceride Synthesis</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>†</td>
      <td>RTO4_8972</td>
      <td>NDE1</td>
      <td>S. cerevisiae</td>
      <td>NADH dehydrogenase</td>
      <td>1.6</td>
      <td>1.9</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="3">Lipid Droplet Associated</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_14088</td>
      <td>RAC1</td>
      <td>H. sapiens</td>
      <td>GTPase</td>
      <td>2.0</td>
      <td>0.9</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="3">Mitochondrial Beta-oxidation</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_16284</td>
      <td>HSD17B10</td>
      <td>H. sapiens</td>
      <td>3-hydroxyacyl-CoA dehydrogenase</td>
      <td>1.6</td>
      <td>0.5</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="2">Other</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_12175</td>
      <td>mesA</td>
      <td>A. nidulans</td>
      <td>Myosin binding protein</td>
      <td>1.3</td>
      <td>1.8</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_8401</td>
      <td>SHE4</td>
      <td>S. cerevisiae</td>
      <td>Transmembrane protein involved in cell polarity</td>
      <td>1.0</td>
      <td>1.3</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="3">Unknown Function</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_16524</td>
      <td></td>
      <td></td>
      <td>Protein of unknown function</td>
      <td>3.1</td>
      <td>1.9</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_11613</td>
      <td></td>
      <td></td>
      <td>Protein of unknown function</td>
      <td>2.5</td>
      <td>1.7</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_12505</td>
      <td></td>
      <td></td>
      <td>Protein of unknown function</td>
      <td>2.1</td>
      <td>2.1</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_13512</td>
      <td></td>
      <td></td>
      <td>Protein of unknown function</td>
      <td>1.5</td>
      <td>1.9</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_10805</td>
      <td></td>
      <td></td>
      <td>Protein of unknown function</td>
      <td>1.2</td>
      <td>1.8</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_15251</td>
      <td></td>
      <td></td>
      <td>Protein of unknown function</td>
      <td>1.6</td>
      <td>1.3</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_15358</td>
      <td></td>
      <td></td>
      <td>Protein of unknown function</td>
      <td>2.0</td>
      <td>0.5</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_13513</td>
      <td></td>
      <td></td>
      <td>Protein of unknown function</td>
      <td>1.3</td>
      <td>1.2</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_12461</td>
      <td></td>
      <td></td>
      <td>Protein of unknown function</td>
      <td>1.5</td>
      <td>0.8</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_13351</td>
      <td></td>
      <td></td>
      <td>Protein of unknown function</td>
      <td>1.2</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>

_Cellular processes grouped as in Figure 6. BD: Enrichment score from buoyant density separation. FACS: Enrichment score from fluorescence activated cell sorting.Protein abundance under nitrogen limitation: * increased; † increased 10-fold or more; ‡ decreased; § decreased 10-fold or more (Zhu et al., 2012)._

**Table 2.**
 Predicted gene function: Mutants with decreased lipid accumulation.Predicted functions for genes for which mutants were high-confidence candidates for decreased lipid accumulation (enrichment scores clustered in LA6 - LA8, Figure 5).


<table>
  <thead>
    <tr>
      <th rowspan="2"></th>
      <th rowspan="2">Gene ID</th>
      <th rowspan="2">Short name</th>
      <th rowspan="2">Annotation from</th>
      <th rowspan="2">Description</th>
      <th rowspan="2">Cluster</th>
      <th colspan="2">Enrichment</th>
    </tr>
    <tr>
      <th>BD</th>
      <th>FACS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="2">tRNA thiolation</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_10764</td>
      <td>NCS2</td>
      <td>S. cerevisiae</td>
      <td>tRNA 2-thiolation protein</td>
      <td>LA7</td>
      <td>0.5</td>
      <td>−2.3</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_12817</td>
      <td>NCS6</td>
      <td>S. cerevisiae</td>
      <td>tRNA 2-thiolation protein</td>
      <td>LA7</td>
      <td>0.7</td>
      <td>−2.6</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_14918</td>
      <td>ELP2</td>
      <td>S. cerevisiae</td>
      <td>Elongator complex protein</td>
      <td>LA7</td>
      <td>0.7</td>
      <td>−1.2</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_14716</td>
      <td>IKI3</td>
      <td>S. cerevisiae</td>
      <td>Elongator complex protein</td>
      <td>LA7</td>
      <td>0.4</td>
      <td>−1.1</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_11341</td>
      <td>UBA4</td>
      <td>S. cerevisiae</td>
      <td>Adenylyltransferase and sulfurtransferase</td>
      <td>LA7</td>
      <td>0.6</td>
      <td>−2.6</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="3">G Protein Switches</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>†</td>
      <td>RTO4_15198</td>
      <td>Rab6</td>
      <td>H. sapiens</td>
      <td>GTPase</td>
      <td>LA6</td>
      <td>−1.3</td>
      <td>−1.6</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_14622</td>
      <td>RGP1</td>
      <td>H. sapiens</td>
      <td>Guanine nucleotide exchange factor</td>
      <td>LA6</td>
      <td>−1.4</td>
      <td>−1.5</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="3">Kinases and Phosphatases</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_10698</td>
      <td>VHS1</td>
      <td>S. cerevisiae</td>
      <td>Kinase</td>
      <td>LA6</td>
      <td>0.8</td>
      <td>−3.7</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_16375</td>
      <td>HRK1</td>
      <td>S. cerevisiae</td>
      <td>Kinase</td>
      <td>LA6</td>
      <td>0.4</td>
      <td>−2.2</td>
    </tr>
    <tr>
      <td>*</td>
      <td>RTO4_11453</td>
      <td>GLC7</td>
      <td>S. cerevisiae</td>
      <td>Kinase</td>
      <td>LA8</td>
      <td>−1.2</td>
      <td>−0.9</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_16810</td>
      <td>KIN1</td>
      <td>S. cerevisiae</td>
      <td>Kinase</td>
      <td>LA6</td>
      <td>0.1</td>
      <td>−1.1</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_10025</td>
      <td>SAT4</td>
      <td>S. cerevisiae</td>
      <td>Kinase</td>
      <td>LA7</td>
      <td>1.6</td>
      <td>−3.6</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_13327</td>
      <td>ATG1</td>
      <td>S. cerevisiae</td>
      <td>Kinase</td>
      <td>LA6</td>
      <td>0.1</td>
      <td>−2.5</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_14907</td>
      <td>SCH9</td>
      <td>S. cerevisiae</td>
      <td>Kinase</td>
      <td>LA6</td>
      <td>−0.6</td>
      <td>−2.0</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_14906</td>
      <td>kinase-like</td>
      <td>S. cerevisiae</td>
      <td>Kinase</td>
      <td>LA6</td>
      <td>−0.3</td>
      <td>−1.8</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_13290</td>
      <td>YAK1</td>
      <td>S. cerevisiae</td>
      <td>Kinase</td>
      <td>LA8</td>
      <td>−1.1</td>
      <td>−0.9</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_11732</td>
      <td>PPH3</td>
      <td>S. cerevisiae</td>
      <td>Phosphatase 4 catalytic subunit</td>
      <td>LA6</td>
      <td>0.9</td>
      <td>−3.6</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_12586</td>
      <td>PSY2</td>
      <td>S. cerevisiae</td>
      <td>Phosphatase 4 regulatory subunit</td>
      <td>LA6</td>
      <td>0.2</td>
      <td>−1.2</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_16463</td>
      <td>PTC7-like</td>
      <td>S. cerevisiae</td>
      <td>Phosphatase</td>
      <td>LA6</td>
      <td>0.1</td>
      <td>−2.0</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="2">Autophagy</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_13327</td>
      <td>ATG1</td>
      <td>S. cerevisiae</td>
      <td>Kinase</td>
      <td>LA6</td>
      <td>0.1</td>
      <td>−2.5</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_13598</td>
      <td>ATG2</td>
      <td>S. cerevisiae</td>
      <td>Membrane protein</td>
      <td>LA6</td>
      <td>−0.6</td>
      <td>−3.4</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_12968</td>
      <td>ATG3</td>
      <td>S. cerevisiae</td>
      <td>Ubiquitin-like-conjugating enzyme</td>
      <td>LA6</td>
      <td>−0.8</td>
      <td>−4.5</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_13496</td>
      <td>ATG4</td>
      <td>S. cerevisiae</td>
      <td>Cysteine protease</td>
      <td>LA6</td>
      <td>−0.1</td>
      <td>−2.3</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_11901</td>
      <td>ATG7</td>
      <td>S. cerevisiae</td>
      <td>Ubiquitin-like modifier-activating enzyme</td>
      <td>LA6</td>
      <td>−0.8</td>
      <td>−4.2</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_13543</td>
      <td>ATG8</td>
      <td>S. cerevisiae</td>
      <td>Ubiquitin-like protein</td>
      <td>LA6</td>
      <td>−1.0</td>
      <td>−4.2</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_11326</td>
      <td>ATG9</td>
      <td>S. cerevisiae</td>
      <td>Membrane protein</td>
      <td>LA6</td>
      <td>0.0</td>
      <td>−1.3</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_9008</td>
      <td>ATG14</td>
      <td>S. cerevisiae</td>
      <td>Autophagy-specific subunit of PtdIns3P-kinase complex</td>
      <td>LA6</td>
      <td>0.0</td>
      <td>−5.0</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_16723</td>
      <td>ATG18</td>
      <td>S. cerevisiae</td>
      <td>Phosphoinositide binding protein</td>
      <td>LA6</td>
      <td>−0.9</td>
      <td>−5.8</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="3">Ubiquitination and Proteolysis</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>†</td>
      <td>RTO4_16672</td>
      <td>PRB1</td>
      <td>S. cerevisiae</td>
      <td>Vacuolar proteinase</td>
      <td>LA6</td>
      <td>−0.2</td>
      <td>−1.7</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_15345</td>
      <td>SIS1</td>
      <td>S. cerevisiae</td>
      <td>Protein chaperone</td>
      <td>LA6</td>
      <td>−0.4</td>
      <td>−1.2</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_10423</td>
      <td>RMD5</td>
      <td>S. cerevisiae</td>
      <td>GID complex E3 ubiquitin ligase</td>
      <td>LA6</td>
      <td>−0.4</td>
      <td>−2.0</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_11737</td>
      <td>GID8</td>
      <td>H. sapiens</td>
      <td>GID complex member</td>
      <td>LA6</td>
      <td>−0.1</td>
      <td>−1.5</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_9816</td>
      <td>LONRF1</td>
      <td>H. sapiens</td>
      <td>E3 ubiquitin ligase</td>
      <td>LA6</td>
      <td>−0.5</td>
      <td>−4.5</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_15320</td>
      <td>USP48</td>
      <td>H. sapiens</td>
      <td>Ubiquitin carboxyl-terminal hydrolase</td>
      <td>LA6</td>
      <td>0.0</td>
      <td>−1.2</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_9600</td>
      <td>COPS3</td>
      <td>H. sapiens</td>
      <td>COP9 signalosome complex subunit</td>
      <td>LA1</td>
      <td>1.4</td>
      <td>0.6</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_11569</td>
      <td>GPS1</td>
      <td>H. sapiens</td>
      <td>COP9 signalosome complex subunit</td>
      <td>LA6</td>
      <td>0.7</td>
      <td>−2.1</td>
    </tr>
    <tr>
      <td colspan="3">Triacylglyceride Synthesis</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>†</td>
      <td>RTO4_12154</td>
      <td>GPD1</td>
      <td>S. cerevisiae</td>
      <td>Glycerol-3-phosphate dehydrogenase</td>
      <td>LA6</td>
      <td>−1.7</td>
      <td>−4.0</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_11043</td>
      <td>BCSL2-like</td>
      <td>H. sapiens</td>
      <td>Seipin</td>
      <td>LA6</td>
      <td>−0.8</td>
      <td>−2.9</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_16460</td>
      <td>DGA1</td>
      <td>H. sapiens</td>
      <td>Diacylglycerol acyltransferase</td>
      <td>LA6</td>
      <td>−0.7</td>
      <td>−4.0</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_14597</td>
      <td>ACS1</td>
      <td>S. cerevisiae</td>
      <td>Acetyl-CoA synthetase</td>
      <td>LA8</td>
      <td>−1.7</td>
      <td>−1.0</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_10182</td>
      <td>YEF1</td>
      <td>S. cerevisiae</td>
      <td>NAD+/NADH kinase</td>
      <td>LA6</td>
      <td>−0.1</td>
      <td>−1.6</td>
    </tr>
    <tr>
      <td>‡</td>
      <td>RTO4_11039</td>
      <td>GUT2</td>
      <td>S. cerevisiae</td>
      <td>Glycerol-3-phosphate dehydrogenase</td>
      <td>LA6</td>
      <td>−0.2</td>
      <td>−1.1</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="3">Lipid Droplet Associated</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_16381</td>
      <td>PLIN1-like</td>
      <td>S. cerevisiae</td>
      <td>Perilipin</td>
      <td>LA6</td>
      <td>−1.7</td>
      <td>−4.3</td>
    </tr>
    <tr>
      <td>‡</td>
      <td>RTO4_11039</td>
      <td>GUT2</td>
      <td>S. cerevisiae</td>
      <td>Glycerol-3-phosphate dehydrogenase</td>
      <td>LA6</td>
      <td>−0.2</td>
      <td>−1.1</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_15372</td>
      <td>EGH1</td>
      <td>S. cerevisiae</td>
      <td>Steryl-beta-glucosidase</td>
      <td>LA6</td>
      <td>0.7</td>
      <td>−2.5</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_13614</td>
      <td>RIP1</td>
      <td>S. cerevisiae</td>
      <td>Mitochondrial complex III iron-sulfur protein</td>
      <td>LA6</td>
      <td>−0.5</td>
      <td>−2.8</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_11043</td>
      <td>BCSL2-like</td>
      <td>H. sapiens</td>
      <td>Seipin</td>
      <td>LA6</td>
      <td>−0.8</td>
      <td>−2.9</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_16460</td>
      <td>DGA1</td>
      <td>H. sapiens</td>
      <td>Diacylglycerol acyltransferase</td>
      <td>LA6</td>
      <td>−0.7</td>
      <td>−4.0</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="3">Protein Modification</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_12670</td>
      <td>B3GALT1-like</td>
      <td>H. sapiens</td>
      <td>Beta-1,3-Galactosyltransferase</td>
      <td>LA6</td>
      <td>−0.9</td>
      <td>−3.1</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="3">Protein Trafficking</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>†</td>
      <td>RTO4_15198</td>
      <td>Rab6</td>
      <td>H. sapiens</td>
      <td>GTPase</td>
      <td>LA6</td>
      <td>−1.3</td>
      <td>−1.6</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="3">Other ER/Golgi Proteins</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_8838</td>
      <td>DNAJC4</td>
      <td>H. sapiens</td>
      <td>DnaJ family chaperone</td>
      <td>LA6</td>
      <td>−0.8</td>
      <td>−1.3</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_13971</td>
      <td>DNAJC3</td>
      <td>H. sapiens</td>
      <td>DnaJ family chaperone</td>
      <td>LA6</td>
      <td>−1.1</td>
      <td>−2.2</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="2">Gene Expression</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_11333</td>
      <td>KLF18-like</td>
      <td>H. sapiens</td>
      <td>Transcription factor</td>
      <td>LA6</td>
      <td>−0.2</td>
      <td>−1.1</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_15641</td>
      <td>SKN7</td>
      <td>S. cerevisiae</td>
      <td>Transcription factor</td>
      <td>LA6</td>
      <td>0.9</td>
      <td>−2.9</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_14676</td>
      <td>LHX5-like</td>
      <td>H. sapiens</td>
      <td>Transcription factor</td>
      <td>LA6</td>
      <td>−0.2</td>
      <td>−2.8</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_11891</td>
      <td>HAP2</td>
      <td>S. cerevisiae</td>
      <td>Transcription factor</td>
      <td>LA6</td>
      <td>−0.8</td>
      <td>−2.4</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_12420</td>
      <td>OPI1-like</td>
      <td>S. cerevisiae</td>
      <td>Transcription factor</td>
      <td>LA6</td>
      <td>0.0</td>
      <td>−3.7</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_14100</td>
      <td>HAPX</td>
      <td>C. neoformans</td>
      <td>Transcription factor</td>
      <td>LA8</td>
      <td>−1.2</td>
      <td>−1.7</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_13255</td>
      <td>SGF73</td>
      <td>S. cerevisiae</td>
      <td>SAGA-associated factor</td>
      <td>LA6</td>
      <td>0.4</td>
      <td>−1.5</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="3">Methylcitrate Cycle</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_14162</td>
      <td>ICL2</td>
      <td>S. cerevisiae</td>
      <td>2-methylisocitrate lyase</td>
      <td>LA6</td>
      <td>−0.3</td>
      <td>−1.8</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_12642</td>
      <td>PDH1</td>
      <td>S. cerevisiae</td>
      <td>2-methylcitrate dehydratase</td>
      <td>LA6</td>
      <td>−0.1</td>
      <td>−1.7</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="4">Electron Transport and Redox Balancing</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_11165</td>
      <td>CBP4</td>
      <td>S. cerevisiae</td>
      <td>Mitochondrial complex III assembly factor</td>
      <td>LA6</td>
      <td>−0.4</td>
      <td>−2.5</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_13614</td>
      <td>RIP1</td>
      <td>S. cerevisiae</td>
      <td>Mitochondrial complex III iron-sulfur protein</td>
      <td>LA6</td>
      <td>−0.5</td>
      <td>−2.8</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_13902</td>
      <td>AFG1</td>
      <td>S. cerevisiae</td>
      <td>Mitochondrial complex IV assembly factor</td>
      <td>LA6</td>
      <td>−0.3</td>
      <td>−1.3</td>
    </tr>
    <tr>
      <td>‡</td>
      <td>RTO4_10010</td>
      <td>NDUFS4</td>
      <td>H. sapiens</td>
      <td>Mitochondrial complex I accessory factor</td>
      <td>LA8</td>
      <td>−1.3</td>
      <td>−0.1</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_13925</td>
      <td>NDUFAF3</td>
      <td>H. sapiens</td>
      <td>Mitochondrial complex I assembly factor</td>
      <td>LA8</td>
      <td>−1.0</td>
      <td>−1.6</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="3">Amino Acid Biosynthesis</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>†</td>
      <td>RTO4_12302</td>
      <td>CPA2</td>
      <td>S. cerevisiae</td>
      <td>Large subunit of carbamoyl phosphate synthetase</td>
      <td>LA6</td>
      <td>−0.4</td>
      <td>−2.4</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="3">Glucose and Energy Metabolism</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_10423</td>
      <td>RMD5</td>
      <td>S. cerevisiae</td>
      <td>GID complex E3 ubiquitin ligase</td>
      <td>LA6</td>
      <td>−0.4</td>
      <td>−2.0</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_11737</td>
      <td>GID8</td>
      <td>H. sapiens</td>
      <td>GID complex member</td>
      <td>LA6</td>
      <td>−0.1</td>
      <td>−1.5</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_12034</td>
      <td>TPS2</td>
      <td>S. cerevisiae</td>
      <td>Trehalose 6-phosphate synthase</td>
      <td>LA6</td>
      <td>0.0</td>
      <td>−3.8</td>
    </tr>
    <tr>
      <td>*</td>
      <td>RTO4_10264</td>
      <td>GLK1</td>
      <td>S. cerevisiae</td>
      <td>Hexokinase</td>
      <td>LA7</td>
      <td>2.1</td>
      <td>−2.0</td>
    </tr>
    <tr>
      <td colspan="2">Transporters</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>†</td>
      <td>RTO4_12909</td>
      <td>OAT1</td>
      <td>C. neoformans</td>
      <td>Nucleobase transporter</td>
      <td>LA6</td>
      <td>−0.2</td>
      <td>−1.1</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_11397</td>
      <td>COT1</td>
      <td>S. cerevisiae</td>
      <td>Vacuolar zinc transporter</td>
      <td>LA6</td>
      <td>−0.2</td>
      <td>−1.1</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_11924</td>
      <td>SNF3</td>
      <td>S. cerevisiae</td>
      <td>Plasma membrane low glucose sensor</td>
      <td>LA6</td>
      <td>0.0</td>
      <td>−2.8</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="2">Other</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_12512</td>
      <td>cry</td>
      <td>N. crassa</td>
      <td>Blue-light photoreceptor cryptochrome</td>
      <td>LA7</td>
      <td>0.6</td>
      <td>−1.6</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_14974</td>
      <td></td>
      <td></td>
      <td>Steroidogenesis/phosphatidylcholine transfer domain</td>
      <td>LA6</td>
      <td>−0.3</td>
      <td>−1.2</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_15889</td>
      <td>MAEA</td>
      <td>H. sapiens</td>
      <td>EMP macrophage erythroblast attacher</td>
      <td>LA6</td>
      <td>−0.1</td>
      <td>−1.7</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_16287</td>
      <td>CDD1</td>
      <td>S. cerevisiae</td>
      <td>Cytidine deaminase</td>
      <td>LA6</td>
      <td>0.3</td>
      <td>−2.3</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_15247</td>
      <td>WDR26</td>
      <td>H. sapiens</td>
      <td>WD repeat protein</td>
      <td>LA6</td>
      <td>−0.9</td>
      <td>−1.3</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_8764</td>
      <td>MGS1</td>
      <td>S. cerevisiae</td>
      <td>DNA-dependent ATPase and ssDNA annealing protein</td>
      <td>LA6</td>
      <td>0.2</td>
      <td>−1.2</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td colspan="2">Unknown</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_10431</td>
      <td></td>
      <td></td>
      <td>Protein of unknown function</td>
      <td>LA6</td>
      <td>0.7</td>
      <td>−1.6</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_8973</td>
      <td></td>
      <td></td>
      <td>Protein of unknown function</td>
      <td>LA8</td>
      <td>−0.2</td>
      <td>−1.1</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_13195</td>
      <td></td>
      <td></td>
      <td>Protein of unknown function</td>
      <td>LA6</td>
      <td>−0.2</td>
      <td>−1.1</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_10367</td>
      <td></td>
      <td></td>
      <td>Protein of unknown function</td>
      <td>LA6</td>
      <td>−0.1</td>
      <td>−1.3</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_10102</td>
      <td></td>
      <td></td>
      <td>Protein of unknown function</td>
      <td>LA6</td>
      <td>−0.3</td>
      <td>−1.2</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_14926</td>
      <td></td>
      <td></td>
      <td>Protein of unknown function</td>
      <td>LA6</td>
      <td>0.2</td>
      <td>−1.7</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_12045</td>
      <td></td>
      <td></td>
      <td>Protein of unknown function</td>
      <td>LA6</td>
      <td>0.0</td>
      <td>−1.5</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_13600</td>
      <td></td>
      <td></td>
      <td>Protein of unknown function</td>
      <td>LA6</td>
      <td>−0.3</td>
      <td>−1.3</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_10976</td>
      <td></td>
      <td></td>
      <td>Protein of unknown function</td>
      <td>LA6</td>
      <td>−0.2</td>
      <td>−1.5</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_9970</td>
      <td>LDB17</td>
      <td>S. cerevisiae</td>
      <td>Protein of unknown function</td>
      <td>LA8</td>
      <td>−1.3</td>
      <td>−0.5</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_13435</td>
      <td></td>
      <td></td>
      <td>Protein of unknown function</td>
      <td>LA7</td>
      <td>0.2</td>
      <td>−2.0</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_9692</td>
      <td></td>
      <td></td>
      <td>Protein of unknown function</td>
      <td>LA6</td>
      <td>−0.5</td>
      <td>−1.4</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_15521</td>
      <td></td>
      <td></td>
      <td>Protein of unknown function</td>
      <td>LA6</td>
      <td>0.2</td>
      <td>−2.2</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_8769</td>
      <td></td>
      <td></td>
      <td>Protein of unknown function</td>
      <td>LA6</td>
      <td>−0.5</td>
      <td>−1.6</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_8770</td>
      <td></td>
      <td></td>
      <td>Protein of unknown function</td>
      <td>LA6</td>
      <td>−0.5</td>
      <td>−1.9</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_11259</td>
      <td></td>
      <td></td>
      <td>Protein of unknown function</td>
      <td>LA7</td>
      <td>0.7</td>
      <td>−3.3</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_9490</td>
      <td></td>
      <td></td>
      <td>Protein of unknown function</td>
      <td>LA6</td>
      <td>−0.6</td>
      <td>−2.4</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_15520</td>
      <td></td>
      <td></td>
      <td>Protein of unknown function</td>
      <td>LA6</td>
      <td>−0.5</td>
      <td>−2.5</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_8771</td>
      <td></td>
      <td></td>
      <td>Protein of unknown function</td>
      <td>LA6</td>
      <td>−0.6</td>
      <td>−2.5</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_13452</td>
      <td></td>
      <td></td>
      <td>Protein of unknown function</td>
      <td>LA6</td>
      <td>−1.3</td>
      <td>−4.0</td>
    </tr>
    <tr>
      <td></td>
      <td>RTO4_15211</td>
      <td></td>
      <td></td>
      <td>Protein of unknown function</td>
      <td>LA8</td>
      <td>−1.1</td>
      <td>−1.5</td>
    </tr>
  </tbody>
</table>

_Cellular processes grouped as in Figure 6. BD: Enrichment score from buoyant density separation. FACS: Enrichment score from fluorescence activated cell sorting.Protein abundance under nitrogen limitation: * increased; † increased 10-fold or more; ‡ decreased; § decreased 10-fold or more (Zhu et al., 2012)._

Mutants with increased lipid accumulation (cluster LA1, 56 genes) were most notably enriched for genes involved in signaling cascades, post-translational protein modification and trafficking, and in amino acid biosynthesis. Genes involved in signaling cascades included several homologs to G-proteins such as RAS1 and mammalian RAC1 and their effectors, as well as several kinases, indicating a complex signaling network regulating lipid accumulation. Genes involved in protein trafficking included P24 adapter proteins, suggesting they play an important role in delivering lipid-mobilizing genes to the lipid droplet or removing lipid biosynthesis genes from the endomembrane network. Mutants for several genes identified in our auxotrophy experiments also had increased lipid accumulation, most notably genes involved in sulfate assimilation for cysteine and methionine biosynthesis. Not all auxotrophic mutants had altered lipid accumulation, suggesting that arrested protein synthesis is not necessarily sufficient to increase lipid accumulation.

Mutants with decreased lipid accumulation (clusters LA6, LA7, and LA8, 94 genes) were most notably enriched for genes with roles in autophagy, protein phosphorylation, and tRNA-modifcation. Mutants in nine core components of autophagy were deficient for lipid accumulation, consistent with previous findings that chemical inhibition of autophagy reduced lipid accumulation in Y. lipolytica (Qiao et al., 2015). Mutants in several proteases and ubiquitin ligases also had reduced lipid accumulation, highlighting the importance of efficient recycling of cellular materials to refactor the cell for high lipid accumulation. Mutants in at least nine protein kinases, three phosphatases or their binding partners had reduced lipid accumulation; likely these genes mediate nutrient sensing cascades that stimulated lipid accumulation. Several genes with likely roles in thiolation of tRNA wobble residues had lower lipid accumulation. Though these mutants also had apparent buoyancy phenotypes on YPD, two deletion strains (NCS6∆ and NCS2∆) had reduced lipid content in pure culture (Figure 5C). They may play a role in regulating global carbon metabolism (Laxman et al., 2013). RTO4_16381, a distant homolog of H. sapiens PLIN1 (perilipin), was also necessary for high lipid accumulation, consistent with its homolog’s known roles in lipid body maintenance and regulation of triglyceride hydrolysis (Bickel et al., 2009) and previous observations that it localized to lipid droplets in R. toruloides (Zhu et al., 2015).

### Diverse morphological phenotypes for lipid accumulation mutants

To further characterize the phenotypes of our lipid accumulation mutants, we performed differential interference contrast (DIC) and fluorescence microscopy. The mutants showed a variety of phenotypes with respect to both cellular and lipid droplet morphology. Eight examples are highlighted in Figure 7. While wild type cells most commonly had two lipid droplets of similar size, several high lipid accumulation mutants had qualitatively more cells with three or more lipid droplets (e.g. MET14∆, Figure 7)) or cells with a single dominant droplet (e.g. RAC1∆, Figure 7). RAC1∆ also had qualitatively larger, more spherical cells. A KDELC-like∆ mutant with increased lipid accumulation also showed a defect in cell separation likely reflective of combined defects in lipid accumulation, secretion, and cell wall/septum formation. All strains had a wide cell-to-cell variation in lipid droplet size, consistent with high variance in BODIPY intensity measured by flow cytometry (Figure 4—figure supplement 2A). Most low-lipid strains appeared morphologically similar to wild type with smaller lipid bodies (Figure 7—figure supplement 1). However, a BSCL2-like∆ (seipin) mutant showed an even larger variation in droplet size than wild type, consistent with observations in S. cerevisiae mutants for the homolog SEI1/FLD1 (Fei et al., 2008) and likely reflective of a conserved function in lipid droplet formation and efficient delivery of lipid biosynthetic proteins to the growing lipid droplet (Wang et al., 2016; Pagac et al., 2016; Salo et al., 2016). Autophagy mutants (ATG2∆) had the most uniformly small lipid droplets in elongated cells with enlarged vacuoles. Overall, the morphological phenotypes we observed in R. toruloides are similar to a number of previous microscopic screens for altered lipid accumulation in diverse eukaryotes (Fei et al., 2008; Szymanski et al., 2007; Guo et al., 2008; Zehmer et al., 2009; Ashrafi et al., 2003).

![Figure 7.](https://cdn.elifesciences.org/articles/32110/elife-32110-fig7-v2.jpg)

**Figure 7.:** DIC microscopy on eight deletion mutants for lipid accumulation genes. All deletion mutants (C–J) were constructed in a YKU70∆ background to enable homologous recombination at the targeted locus. Cells were grown 40 hr in low nitrogen lipid accumulation media. DIC, BODIPY 493/503 fluorescence, and composite images are shown for ten strains. (A) R. toruloides IFO 0880 (WT). (B) RTO4_11920∆ ortholog of YKU70. (C) RTO4_11043∆ similar to H. sapiens BSCL2. (D) RTO4_14088∆ ortholog of H. sapiens RAC1. (E) RTO4_10371∆ similar to H. sapiens KDELC1. (F) RTO4_16215∆ similar to H. sapiens GNAI1. (G) RTO4_8709∆ ortholog of MET14. (H) RTO4_16381∆ similar to H. sapiens PLIN1. (I) RTO4_13598∆ ortholog of ATG2. (J) RTO4_12154∆ ortholog of GPD1. The following figure supplements are available for Figure 7.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/32110/elife-32110-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** DIC microscopy on 21 deletion mutants for lipid accumulation genes. All deletion mutants (C–W) were constructed in a YKU70∆ background to enable homologous recombination at the targeted locus. Cells were grown 40 hr in low nitrogen lipid accumulation media. DIC, BODIPY 493/503 fluorescence, and composite images are shown for 23 strains. (A) R. toruloides IFO 0880 (WT). (B) RTO4_11920∆ ortholog of YKU70. (C) RTO4_11272∆ ortholog of ALG12. (D) RTO4_8709∆ ortholog of MET14. (E) RTO4_12031∆ ortholog of A. nidulans CysB. (F) RTO4_16215∆ similar to H. sapiens GNAI1. (G) RTO4_14088∆ ortholog of H. sapiens RAC1. (H) RTO4_10371∆ similar to H. sapiens KDELC1. (I) RTO4_16644∆ ortholog of BMH1. (J) RTO4_16731∆ ortholog of ERP2. (K) RTO4_9026∆ ortholog of UBP13. (L) RTO4_15890∆ similar to H. sapiens MYCL. (M) RTO4_8506∆ ortholog of CCC1. (N) RTO4_12817∆ ortholog of NCS6. (O) RTO4_10764∆ ortholog of NCS2. (P) RTO4_9970∆ ortholog of LDB17. (Q) RTO4_13598∆ ortholog of ATG2. (R) RTO4_16381∆ similar to H. sapiens PLIN1. (S) RTO4_12154∆ ortholog of GPD1. (T) RTO4_11043∆ similar to H. sapiens BSCL2. (U) RTO4_12121∆ ortholog of PMT4. (V) RTO4_10302∆ similar to C. neoformans CMT1. (W) RTO4_11380∆ ortholog of PPZ1.

## Discussion

### Bringing functional genomics to non-model fungi with RB-TDNAseq

We employed an established method, Agrobacterium tumefaciens-mediated transformation, to extend barcoded insertion library techniques (Wetmore et al., 2015) into a non-model basidiomycetous fungus. The efficiency of A. tumefaciens transformation in diverse fungal species (Michielse et al., 2005; Martínez-Cruz et al., 2017; Wu et al., 2016; Zhang et al., 2015; Liu et al., 2013; Zhang et al., 2014; Li et al., 2013; Han et al., 2012; Muniz et al., 2014; Rodrigues et al., 2013; Celis et al., 2017) will enable use of RB-TDNAseq in many fungal species with limited genetic tools. We used RB-TDNAseq to simultaneously track mutants in over 6,500 genes for altered lipid catabolism and neutral lipid accumulation using a simple, scalable BarSeq protocol. The phenotypes measured in our high-throughput experiments were consistent with those observed for single gene deletion strains, demonstrating the reliability of this approach. In some respects R. toruloides was an ideal species to develop these methods. The R. toruloides genome is relatively compact (just over 20% of the sequence is predicted to be intergenic), and it grows as a haploid yeast. Effective BarSeq analysis on species with larger, less dense genomes will require greater sequence depth per sample. Typical fungal genomes are only modestly larger, though, around 35–45 Mb (Mohanta and Bae, 2015) vs 20 Mb for R. toruloides. Sequencing limitations are thus already minimal and will only decrease in the foreseeable future. A greater challenge will be adapting this technology in fungi that grow mainly as diploids or in filamentous, multicellular, or multinucleate forms harboring genetically distinct nuclei. Many of those species also produce haploid, uninucleate spores for sexual reproduction, asexual dispersal, or both. RB-TDNAseq can be applied to study the germination of these spores and their growth into nascent, isogenic colonies prior to their fusion into more physiologically and genetically complex networks of mycelia and fruiting bodies.

We found that genes recalcitrant to T-DNA insertion were highly enriched in orthologs for known essential genes, suggesting that most genes with very low insertion rates were likely essential in our mutagenesis conditions. Previous studies employing high-density transposon mutagenesis in fungi and bacteria have demonstrated the general utility of this approach (Michel et al., 2017; Le Breton et al., 2015). The high efficiency of A. tumefaciens-mediated transformation in diverse fungi should enable similar surveys in many poorly annotated fungi. We hope the provisional list of essential genes identified here will serve as a useful resource for genetics in R. toruloides and related species. In particular, orthologs to these genes may be potential targets for new antifungal strategies against basidiomycete pathogens, such as the closely related rusts of the Pucciniomycotina subphylum (Singh et al., 2015; Park et al., 2015) and the more distantly related human pathogen Cryptococcus neoformans (May et al., 2016).

### New insights into fatty acid catabolism in R. toruloides

The presence of a probable mitochondrial fatty acid beta-oxidation pathway in R. toruloides has been noted previously (Zhu et al., 2012). Our results confirm that this pathway is functional and essential for fatty acid utilization and add to mounting evidence that mitochondrial beta-oxidation is widespread in fungi (Khan et al., 2012). In mammals, some branched long-chain fatty acids are shortened in the peroxisome, then transferred via the acylcarnitine shuttle to the mitochondria for complete oxidation (Wanders et al., 2015; Swigonová et al., 2009), while other long-chain fatty acids are metabolized solely in the mitochondria (Chegary et al., 2009). Rhodosporidium toruloides has orthologs to the mammalian mitochondrial short, branched-chain and medium-chain acyl-CoA dehydrogenases ACADSB and ACADM, but not to the long-chain and very long-chain acyl-CoA dehydrogenases ACADL and ACADVL. Rhodosporidium toruloides also has several homologs to peroxisomal long chain acyl-CoA dehydrogenases ACAD10 and ACAD11. In our experiments, both peroxisomal and mitochondrial beta-oxidation were necessary for robust growth on fatty acids and peroxisomal beta-oxidation enzymes had more variable fitness scores between different fatty acids. These observations are consistent with a model of beta-oxidation in which a large ensemble of peroxisomal enzymes shorten diverse long-chain fatty acids in the peroxisome and a smaller ensemble of enzymes metabolize short-chain fatty acids in the mitochondria. Our results demonstrate how a barcoded insertion library can accelerate discrimination of function between closely related members of a diversified gene family. Fitness assays on a much larger panel of substrates should yield further insights into the individual functions of R. toruloides’ diverse complement of peroxisomal enzymes and guide experimental design for their biochemical characterization.

### Extending high-throughput fitness techniques to lipid production

While pooled fitness experiments have been used extensively to identify novel gene function, work so far has primarily focused on growth-based phenotypes, with only limited exploration of other phenotypes (Sliva et al., 2016; Hassan et al., 2016; Tyo et al., 2009). In this study we used two proven strategies for differentiating between cells with altered lipid accumulation, buoyant density centrifugation (Eroglu and Melis, 2009; Kamisaka et al., 2006; Liu et al., 2015) and FACS (Terashima et al., 2015; Xie et al., 2014), and applied them to our barcoded mutant pool. Inconsistencies between the two assays and with respect to independent BODIPY staining of targeted deletion strains suggests significant false positive rates for each assay in isolation. When both assays were in agreement, however, 18 of 21 deletion mutants had the expected phenotype in independent experiments. This approach identified 150 high confidence candidate genes with strong impacts on lipid accumulation under nitrogen limitation. While this set is likely incomplete, it complements previous transcriptional and proteomic studies to establish critical genes and cellular processes supporting lipid accumulation that deserve more intensive study. As has been noted in previous functional screens (Smith et al., 2006), there was limited overlap between genes for which mutants had a detectable lipid accumulation phenotype in our study and genes with altered protein abundance in R. toruloides during lipid accumulation (Zhu et al., 2012) (14 genes) or genes that co-purified with R. toruloides lipid droplets (five genes) (Zhu et al., 2015). The different ensembles of genes identified by each technique illustrate that these systems-level approaches complement each other.

### New insights into regulation of lipid metabolism in R. toruloides

Proteomic, transcriptomic, mutagenic and over-expression surveys of lipid metabolism have been carried out in several model eukaryotic systems including S. cerevisiae (Bozaquel-Morais et al., 2010; Fei et al., 2008; Szymanski et al., 2007; Grillitsch et al., 2011; Fei et al., 2011; Ruggles et al., 2014; Currie et al., 2014; Bouchez et al., 2015), C. elegans (Ashrafi et al., 2003; Zhang et al., 2010; Liu et al., 2014; Lee et al., 2014; Lapierre et al., 2011), D. melanogaster (Cermelli et al., 2006; Guo et al., 2008; Beller et al., 2006; Beller et al., 2008; Krahmer et al., 2013b), various mammalian cell lines (Zehmer et al., 2009; Nishino et al., 2008; Tu et al., 2009), and Y. lipolytica (Athenstaedt et al., 2006; Pomraning et al., 2017; Silverman et al., 2016) (see Supplementary file 5 for a summary of genes identified in 35 studies). These studies employed different analytical techniques and culture conditions, and identified many genes without clear orthologs across the different species used, making a granular meta-analysis extremely difficult. A few broad themes are apparent, however. Protein trafficking and organelle interaction are inextricably linked with lipid body formation, growth and mobilization. Membrane-bound G proteins in the endomembrane network have conserved roles regulating trafficking and cellular morphology in response to metabolic states. A complex network of signaling cascades, protein modifications and transcription factors mediate the transition to lipid accumulation or lipid mobilization. A major output of this regulation is amino acid metabolism. Lipid metabolism and autophagy are deeply linked in a complex manner. Our findings were consistent with these general themes, including some orthologs to genes identified in the studies above, but the importance of general functions was more conserved across species than the roles of specific orthologous gene sets. The genes and processes we identify here should be considered in any strategy to optimize lipid metabolism in R. toruloides specifically or oleaginous yeasts in general. Comparative study of these processes across diverse species in standardized conditions will likely be required to uncover which aspects are fundamental to lipid droplet accumulation, maintenance and variation, and which processes are integrated by specific regulatory circuits in a given organism. See Appendix 1 for a deeper discussion of the individual genes for which mutants had altered lipid accumulation in our experiments and how those observations relate to previous work.

### Uncovering function for novel genes

In this study, we identified 46 R. toruloides genes with no functional predictions (Supplementary file 1), but which had important functions in lipid metabolism as evidenced by reduced fitness when grown on fatty acids or altered lipid accumulation. These included nine genes with broad conservation across ascomycete and basidiomycete fungi and seven genes with conservation across several basidiomycete species. These genes are of particular interest for further study into their specific functions in lipid metabolism. Moreover, the mutant pool generated in this study should be an excellent tool to assign functions for uncharacterized R. toruloides genes. Cofitness analysis is a particularly powerful method for uncovering the function of novel genes in pathways and processes for which one or more well-characterized genes is also required (Hillenmeyer et al., 2010). Closely interacting genes exhibit strongly correlated fitness scores across large panels of diverse conditions. Because the T-DNA insertions in the mutant pool are barcoded, fitness experiments are inherently scalable to a large number of conditions. Because the analytical methods we employed maximize portability and scalability across large compendiums of experiments (Wetmore et al., 2015), individual experiments can be conducted at different times under specialized culture conditions, at different scales, and even by different laboratories, yet the data can be effectively compared, maximizing the power of cofitness analysis. We encourage the R. toruloides community and the broader fungal community to make use of this new resource and collaborate with us to maximize its potential.

### Conclusions

In conclusion, we believe that RB-TDNAseq holds great promise for rapid exploration of gene function in diverse fungi. Because ATMT has been demonstrated in numerous, diverse fungi, we expect this method will be portable to many non-model species. Because the fitness analysis is inherently scalable, it will enable rapid fitness analysis over large compendia of conditions. Cofitness analysis of such compendia will accelerate the annotation of new genomes and identify new classes of genes not abundant in established model fungi. In this study, we demonstrated the application of RB-TDNAseq to the study of lipid metabolism in an oleaginous yeast that has significant potential to become a new model system for both applied and fundamental applications. We identified a large set of genes from a wide array of subcellular functions and compartments that impact lipid catabolism and accumulation. These processes and genes must be considered and addressed in any metabolic engineering strategy to optimize lipid metabolism in R. toruloides and other oleaginous yeasts. Deeper understanding of the extreme cell-to-cell variation in lipid accumulation seen across eukaryotes will likely require deeper mechanistic understanding of these processes and their interaction with the lipid droplet. The principles learned from exploring lipid metabolism and storage across diverse eukaryotes will inform biotechnological innovations for the production of biofuels and bioproducts, as well as new therapies for metabolic disorders.

## Materials and methods

### Strains

We used R. toruloides IFO 0880 (also called NBRC 0880, obtained from Biological Resource Center, NITE (NBRC), Japan) as the starting strain for all subsequent manipulations. We used Agrobacterium tumefaciens EHA 105 and plasmids derived from pGI2 (Abbott et al., 2013) for A. tumefaciens-mediated transformation (ATMT) of R. toruloides (strain and plasmid kindly provided by Chris Rao, UIUC). The barcoded mutant pool was constructed by ATMT. We made all gene deletions in a non-homologous end-joining deficient YKU70∆ background (Zhang et al., 2016b) by homologous recombination of a nourseothricin resistance cassette introduced by either ATMT or electroporation of a PCR product. For deletions made by ATMT we used flanking arms of ~1000–1500 bp for homologous recombination. We found that as few as 40 bp of flanking sequence were sufficient for homologous recombination of PCR products at many loci. All strains used in this study, and primers used for strain construction and verification are listed in Supplementary file 4.

### Culture conditions

For most experiments, we used optical density (OD) as measured by absorbance at 600 nm on a GENESYS 20 spectrophotometer (Thermo Fisher Scientific, 4001–000, Waltham, MA) as a metric for growth and to control inoculation density. For IFO 0880 grown in rich media, 1 OD unit represents approximately 30 million cells/mL. Unless otherwise noted, cultures were grown at 30°C in 100 mL liquid media in 250 mL baffled flasks (Kimble Chase, 25630250, Vineland, New Jersey) with 250 rpm shaking on a New Brunswick Innova 2300 platform shaker (Eppendorf, M1191-0000, Hauppauge, New York) with constant illumination using a LUMAPRO 6W LED lamp (Grainger, 33L570, San Leandro, CA). We used yeast-peptone-dextrose (YPD) media (BD Biosciences, BD242820, San Jose, CA) for general strain maintenance and rich media conditions. For auxotrophy experiments we used 0.67% w/v yeast nitrogen base (YNB) w/o amino acids (BD Biosciences, BD291940) with 111 mM glucose (Sigma-Aldrich, G7528, St. Louis, MO) as our defined media and supplemented with 75 mM L-methionine (Sigma-Aldrich, M9625), 75 mM L-arginine (Sigma-Aldrich, A5006), or 0.2% w/v drop-out mix complete (DOC), which contains all 20 amino acids, adenine, uracil, p-aminobenzoic acid, and inositol (US Biological, D9515, Salem, MA). To test growth and fitness on oleic acid (Sigma-Aldrich, O1008 and 364525), ricinoleic acid (Sigma-Aldrich, R7257), and methyl ricinoleic acid (Sigma-Aldrich, R8750), we used this same defined media formulation with 1% fatty acid (by volume) instead of glucose. For lipid accumulation experiments, we pre-cultured strains for two generations in YPD (OD 0.2 to OD 0.8) then washed them twice and resuspended them at OD 0.1 in low nitrogen medium; 0.17% w/v yeast nitrogen base (YNB) w/o amino acids or ammonium sulfate (BD Biosciences, BD233520), 166 mM D-glucose, 7 mM NH4Cl (Thermo Fisher Scientific, S25168A), 25 mM KH2PO4 (Thermo Fisher Scientific, P285-3), and 25 mM Na2HPO4 (Sigma-Aldrich, S0876). This is the C:N 120 formulation from Nicaud et al. (Nicaud et al., 2014). Unless otherwise specified, cultures were harvested for lipid quantification or fractionation after 40 hr of growth and lipid accumulation. In all experiments biological replicates refer to samples from independent cultures in the experimental condition. Biological replicates processed on the same day were usually inoculated from the same YPD pre-culture, except for BarSeq experiments. For BarSeq experiments we seeded independent starter cultures in YPD and collected a ‘Time 0’ reference sample after two generations. In downstream fitness or enrichment analysis, we explicitly paired each sample from an experimental condition with the Time 0 sample from the starter culture replicate from which it was seeded.

### Genome sequencing and de novo assembly

To generate an improved genome assembly for IFO 0880 we prepared genomic DNA for PacBio RS II sequencing (Pacific Biosciences, Menlo Park, CA). Genomic DNA was purified using a two-step protocol, first using glass bead lysis and phenol-chloroform extraction, as previously described (Zhang et al., 2016a), followed by a QIAGEN Genomic-tip 100/G method (QIAGEN, 10243, Germantown, MD). All QIAGEN buffers were obtained from a Genomic DNA Buffer Set (QIAGEN, 19060). Briefly, the dry genomic DNA pellet was first resuspended in G2 buffer supplemented with 200 µg/mL RNase A (QIAGEN, 19101) and 13.5 mAU/ml Proteinase K (QIAGEN, 19131), incubated at 50°C for one hour, and then loaded on a Tip-100 column. After three washes with QC buffer and elution with QF buffer, the DNA was precipitated with isopropanol and removed by spooling using a glass Pasteur pipet. The genomic DNA was washed with 70% ethanol and after air-drying, resuspended in EB buffer (pH 7.5). DNA concentration was determined using a Qubit 3.0 fluorometer (Thermo Fisher Scientific, Q33218) and submitted to University of Maryland Genomics Resource Center for library preparation and sequencing. A 10 kb insert, size selected (BluePippin, Sage Science, Beverly, MA) SMRTbell library was prepared and sequenced on a PacBio RS II platform using P4C2 chemistry and 10 SMRT cells. De novo assembly of 610,663 polymerase reads (mean subread length of 5,193 bp) was performed using SMRT Analysis version 2.3.0.140936 (http://www.pacb.com/support/software-downloads/) and the RS_HGAP_Assembly.3 protocol (HGAP3) using default settings except for a genome size of 20,000,000 bp. The final assembly contained 30 polished contigs (mean coverage of 131-fold) with a total genome size of 20,810,536 bp. Paired-end Illumina data (17,817,326 PE100 reads, [Zhang et al., 2016a]) was used for error correction using Pilon version 1.13 (https://github.com/broadinstitute/pilon). As expected, the most common type of correction (569 in total) was insertion or deletion of a nucleotide in homopolymer regions. The final error corrected scaffolds were annotated by JGI and submitted to Genbank under the accession LCTV02000000. Raw sequence data (PacBio and Illumina) has been deposited in the NCBI SRA (SRP114401 and SRP058059, respectively).

### RNA sequencing and analysis

To harvest RNA for improved gene model prediction, we inoculated R. toruloides into 50 mL cultures in M9 Minimal Salts Solution (BD Biosciences, BD248510), 2 mM MgSO4 (Sigma-Aldrich, M7506), 100 µM CaCl2 (Sigma-Aldrich, C5670), and Yeast Trace Elements Solution (88 µg/mL nitrilotriacetic acid, 175 µg/mL MgSO4 7H2O, 29 µg/mL MnSO4 H2O, 59 µg/mL NaCl, 4 µg/mL FeCl2, 6 µg/mL CoSO4, 6 µg/mL CaCl2 2H2O, 6 µg/mL ZnSO4 7H2O, 0.6 µg/mL CuSO4 5H2O, 0.6 µg/mL KAl(SO4)2 12H2O, 6 µg/mL H3BO3, 0.6 µg/mL Na2MoO4 H2O), pH 7.0, with 2% glucose (Sigma-Aldrich, D9434) or 10 mM p-coumaric acid (trans-4-hydroxycinnamic acid; Alfa Aesar, A15167, Tewksbury, MA), and incubated overnight at 30°C with 200 rpm shaking. We harvested cultures at mid-log phase, centrifuged at 3,000 RCF for 10 min at room temperature, removed the supernatant and flash-froze the cell pellet in an ethanol/dry ice bath and stored at −80°C. We lyophilized pellets overnight in a FreeZone-12 freeze dry system (Labconco, 7754030, Kansas City, MO) and extracted total RNA with a Maxwell RSC Plant RNA Kit (Promega, AS1500, Madison, WI) using a Maxwell RSC instrument (Promega, AS4500). RNA was sequenced and mapped to the R. toruloides IFO 0880 genome at the Department of Energy Joint Genome Institute (JGI) in Walnut Creek, CA with in-house protocols.

### Gene model predictions and curation

The improved genome assembly was annotated using the JGI Annotation pipeline (Grigoriev et al., 2014). Owing to relatively small intergenic spacing in the R. toruloides genome, fused gene models were a common problem. We hand curated over 500 gene models by searching for homology to unrelated proteins at each end of the automated gene models and inspecting agreement with assembled transcripts from our RNAseq experiments. Briefly, for all protein models over 400 amino acids long, we used the N-terminal and C-terminal 30% of each sequence in separate BLAST queries (NCBI BLAST-plus software 2.2.30) to a custom database of proteins from 22 other eukaryotic genomes (see Orthology relationships, below). We then compared the significant alignments for each terminus of a given gene and scored them for disagreement in regards to the respective orthology groups to which each target sequence belonged with a custom Python script (Coradetti, 2018a; copy archived at https://github.com/elifesciences-publications/fusedgenemodels). The top-scoring 500 gene models were manually inspected for uncharacteristically long introns and for predicted introns and exons not supported by RNAseq reads and modified as required using the Mycocosm genome browser. The current genome annotation is publicly available at the JGI Mycocosm web portal (Grigoriev et al., 2014): http://genome.jgi.doe.gov/Rhoto_IFO0880_4

### Orthology relationships

We predicted orthologous proteins for our R. toruloides gene models in H. sapiens, D. melanogaster, C. elegans, A. thaliana, C. reinhartii, S. cerevisiae, and 16 other fungi with the orthomcl software suite version 2.0.9 (Li et al., 2003). See Supplementary file 1 for a full list of ortholog groups and details on the genomes used in this analysis.

### Vector library construction

To efficiently construct a large and diverse mutant pool of barcoded mutants we first constructed a large library of barcoded vectors with an optimized Type IIS endonuclease cloning strategy (Engler et al., 2008). We modified the ATMT vector pGI2 (Abbott et al., 2013) to act as a barcode receiving vector by first removing the two pGI2 SapI sites already present on the vector backbone through SapI restriction digestion, treatment with T4 DNA polymerase for blunt end formation and subsequent blunt end ligation. Next, we introduced two divergent SapI recognition sites just inside the right border of the T-DNA (vector pDP11) as the integration site for random barcoding. We added the barcodes by synthesizing the oligonucleotide GATGTCCACGAGGTCTCTNNNNNNNNNNNNNNNNNNNNCGTACGCTGCAGGTCGAC and amplifying with primers TCACACAAGTTTGTACAAAAAAGCAGGCTGGAGCTCGGCTCTTCGCCCGATGTCCACGAGGTCTCT and CTCAACCACTTTGTACAAGAAAGCTGGGTGGATCCGCTCTTCAATTGTCGACCTGCAGCGTACG. We then combined 4 μg of vector and 140 ng of barcode fragments in a 50 µl reaction with 5 µl 10x T4 ligase buffer, 5 µl 10x NEB CutSmart buffer (NEB, B7204S, Ipswich, MA), 2.5 µl T7 ligase (NEB, M0318L), and 2.5 µl of SapI (NEB, R0569S). We incubated the reaction at 37°C for 5 min, then 25 cycles of 37°C for 2 min and 20°C for 5 min, before denaturing the enzymes for 10 min at 65°C. Without cooling the product, we added 1 µl SapI and incubated for 30 min at 37°C to digest any uncut vector, then cooled to 10°C. We purified the barcoded plasmids using a Zymo DNA clean and concentrator kit (Zymo Research, D4014, Irvine, CA), eluting in 15 µl of elution buffer and pooled 10 barcoding reactions. We then transformed E. coli electrocompetent 10-beta cells (NEB, C3019I) according to the manufacturers specifications in 30 independent transformations. We estimated the diversity of the barcoded vector pool by performing barcode sequencing as described below, sequencing on an Illumina MiSeq system and estimating the true pool size by the relative proportion of barcodes with 1 or 2 counts. See the script Multicodes.pl from Wetmore et al. (Wetmore et al., 2015) for details. This yielded a barcoded pool estimated to consist of ~100 million clones.

### Agrobacterium mediated transformation of R. toruloides

We transformed the barcoded vector pool into A. tumefaciens EHA 105 with a protocol adapted from established methods (Mersereau et al., 1990). We diluted a stationary phase starter culture 1:100 in 500 ml Luria-Bertani broth (BD Biosciences, BD244620) and cultured for 6 hr at 30°C. We pelleted cells at 3,000 RCF for 10 min at 4°C, washed pellets in ice-cold 1 mM HEPES (Thermo Fisher Scientific, BP310), pH 7.0, then washed them in ice-cold 10% glycerol 1 mM HEPES, suspended cells in 5 ml ice-cold 10% glycerol 1 mM HEPES, and flash froze 50 µl aliquots in liquid nitrogen. To produce a large transformant pool of A. tumefaciens bearing millions of unique barcode sequences, we electroporated 5 ml of competent cells with 50 µg of plasmid DNA (50 µl per well) in a HT100 96-well plate chamber (BTX, 45-0400, Holliston, MA) with a 2.5 kV pulse, 400 ohm resistance and 25 µF capacitance from an ECM 630 wave generator (BTX, 45-0051). We recovered cells in LB for 2 hr at 30°C, and plated on LB agar with 50 µg/ml kanamycin (Sigma-Aldrich, K4000). Approximately 14 million transformation events were scraped and collected into a mixed pool for transformation of R. toruloides.

We grew the barcoded A. tumefaciens pool to OD 1 in 50 mL YPD in a baffled flask at 30°C, then pelleted the cells and suspended in 10 mL induction medium (1 g/L NH4Cl, 300 mg/L MgSO4 7H2O, 150 mg/L KCl (Thermo Fisher Scientific, P267-500), 10 mg/L CaCl2 (VWR, 0556, Radnor, PA), 750 µg/L FeSO4 7H2O (Thermo Fisher Scientific, AC423731000), 144 mg/L K2HPO4 (VWR, 0705), 48 mg/L NaH2PO4 (Thermo Fisher Scientific, BP329), 2 g/L D-Glucose, 10 mg/L thiamine (Sigma-Aldrich, T4625), 20 mg/L acetosyringone (Sigma-Aldrich, D134406), and 3.9 g/L MES (Sigma-Aldrich, 69892), adjusted to pH 5.5 with KOH) and incubated 24 hr at room temperature in culture tubes on a roller drum. We cultured R. toruloides in 10 mL YPD to OD 0.8, then pelleted the cells and suspended in the induced A. tumefaciens culture for 5 min at room temperature. We filtered the mixed culture on a 0.45 µm membrane filter (EMD Millipore, HAWP04700, Bedford, MA) then transferred the filter to induction media 2% agar (BD Biosciences, BD214010) plates for incubation at 26°C for 4 days. We then washed the filters in YPD and plated on YPD 2% agar with 300 µg/ml cefotaxime (Sigma-Aldrich, C7039) and 300 µg/ml carbenicillin (Sigma-Aldrich, C1389) and incubated at 30°C for two days. We scraped these plates to collect transformed R. toruloides, recovered the mutant pool in YPD plus cefotaxime and carbenicillin for 24 hr, added glycerol to 15% by volume and stored at −80°C. We repeated this protocol 40 times to recover approximately 2 million transformation events. In some rounds of transformation, we also included 0.05% casamino acids (BD Biosciences, BD223120) or 1% CD lipid concentrate (Thermo Fisher Scientific,11905–031) in the induction media plates to promote recovery of mutants with impaired amino acid or lipid biosynthesis. We then recovered each of these transformation subpools on YPD plus cefotaxime and carbenicillin 12 hr to clear residual A. tumefaciens and combined them into one master pool, divided it into 1 ml aliquots in YPD 15% glycerol and stored them at −80°C. Laboratories with an interest in experimenting with this mutant pool should contact the corresponding authors.

### TnSeq library preparation

To isolate high quality genomic DNA we harvested ~108 cells from a fresh YPD culture of the mutant pool, washed the pellet in water and suspended in 200 µl TSENT buffer (2% Triton X-100 (Sigma-Aldrich, T8787), 1% SDS (Thermo Fisher Scientific, AM9820), 1 mM EDTA (Sigma-Aldrich, ED2SS), 100 mM NaCl (Sigma-Aldrich, S5150), 10 mM Tris-HCl, pH 8.0 (Invitrogen, 15568–025, Carlsbad CA)). We then added the sample to 200 µl 25:24:1 phenol/chloroform/isoamyl alcohol (Invitrogen, 15593–031) in screw-top tubes with glass beads (Sigma-Aldrich, Z763748) on ice and vortexed for 10 min at 4°C. We added 200 µl TE buffer (Thermo Fisher Scientific, AM9858), centrifuged at 21,000 RCF for 20 min at 4°C, removed the aqueous phase to 1 mL 200 Proof ethanol (Koptec, V1016, King of Prussia, PA) and centrifuged at 21,000 RCF for 20 min at 4°C to pellet DNA. DNA was dried and suspended in 200 µl TE, treated with 0.5 µl RNase A (Qiagen, 19101), then purified with a Genomic DNA Clean and Concentrator Kit (Zymo Research, D4064). We checked DNA quality on a 0.8% agarose E-Gel (Thermo Fisher Scientific, G51808) and quantified with a Qubit 3.0 fluorometer using the dsDNA HS reagent (Invitrogen, 1799096).

To sequence sites of genomic insertions we followed the TnSeq protocol of Wetmore et al. (Wetmore et al., 2015), using their Nspacer_barseq_universal primer and P7_MOD_TS_index primers for final amplification (Supplementary file 4). Because we found a high proportion of non-specific products in our TnSeq mapping and highly variable recovery of the same insertions between technical replicates, we sequenced multiple replicates for each batch of ATMT mutants (around 10,000–100,000 mutants per batch) and used at least two annealing temperatures for the final PCR enrichment for each batch. In total, we sequenced about 900 million reads from 64 independent TnSeq libraries. A full summary of TnSeq libraries used to map the mutant pool is listed in Supplementary file 4. Libraries were submitted for single-end 150 bp Illumina sequencing on a HiSeq 2500 platform at the UC Berkeley Vincent J. Coates Genomics Sequencing Laboratory, except for a subset of smaller runs on an Illumina MiSeq platform as indicated in Supplementary file 4. Sequence data have been submitted to the NCBI Short Read Archive (SRP116146).

### Mapping insertion locations

We used a similar strategy as Wetmore et al. (Wetmore et al., 2015) to map the location of each barcoded T-DNA insertion, with minor alterations (Coradetti, 2018b).

MapTnSeq_trimmed.pl processes the TnSeq reads to identify the barcode sequence and is a modified version of MapTnSeq.pl (Wetmore et al., 2015), with three minor alterations. We ignore the last 10 bases of the T-DNA sequence, as the length of T-DNA border sequence included in the final insertion is variable. We also allow for barcode sequences of 17–23 base pairs instead of exactly 20. We relaxed this restriction because on manual inspection of our TnSeq data we found that approximately 10% of barcodes appeared to be slightly shorter or longer than 20 base pairs, likely a result of imperfect PAGE purification after oligonucleotide synthesis. We report all TnSeq reads in which sequence past the end of the expected T-DNA insert aligns with other regions of the T-DNA sequence, or with the outside vector as ‘past end’ reads. These are mappings of junctions between concatemeric T-DNA inserts and unprocessed T-DNA vectors, respectively.

RandomPoolConcatemers.py is a custom script that associates barcode sequences mapped in MapTnSeq_trimmed.pl with genomic locations and then filters those barcodes for insertions at unique, unambiguous locations. First, for all barcodes sequenced, the number of reads mapping to any genomic location and the number of reads mapping to concatemeric junctions are tabulated. Any barcodes that only differ by a single base pair from a barcode with 100 times more reads are removed as likely sequencing errors and reported as ‘off by one’ barcodes. Any barcode for which there are more than seven times as many ‘past end’ reads as reads mapping to genomic locations as ‘past-end’ barcodes. The past-end barcodes are further characterized as ‘head-to-tail’ concatemers (majority of Tnseq reads map to the left border T-DNA sequence), ‘head-to-head’ concatemers (majority of the reads map to the right border T-DNA sequence), or ‘Run-on’ insertions (majority of reads map to pGI2 outside the T-DNA sequence). Any barcodes for which the majority of TnSeq reads map ambiguously to the genome are removed and reported as ambiguous barcodes. Any barcodes for which 20% or more of the TnSeq reads map to a different location than the most commonly observed location are removed and reported as ‘multilocus’ barcodes. Finally, any barcodes mapped within 10 bases of a more abundant barcode for which there is a Levenshtein edit distance (Levenshtein, 1966) less than five are removed as likely sequencing errors and reported as ‘off by two’ barcodes. The remaining unfiltered barcodes are reported as the mutant pool.

InsertionLocationJGI.py is a custom script to match the genomic locations of barcodes in the mutant pool to the nearest gene in the current JGI R. toruloides gene catalog and report whether the insertion is in a 5-prime intergenic region, a 5-prime UTR, an exon, an intron, a 3-prime UTR, or a 3-prime intergenic region of that gene.

InsertBias.py is a custom script to analyze potential biases in T-DNA insertion rates. The script tracks number of insertions versus scaffold length for all scaffolds in the genome, GC content in the local regions of insertion, and insertion rates in promoter regions, 5-prime untranslated mRNA, exons, introns, 3-prime untranslated mRNA, and terminator regions. To assess fine-scale biases in insertion locations, all locations in the genome are apportioned to one of the above feature types, then for each feature type, the same number of insertions as were observed for that feature type in the mutant pool are sampled at random (without replacement) from all the genomic locations assigned to that feature type.

### Barcode sequencing

We isolated genomic DNA with a Fungal/Bacterial DNA MiniPrep kit (Zymo Research, D6005). We used Q5 high-fidelity polymerase with GC-enhancer (NEB, M0491S) to amplify unique barcode sequences flanked by specific priming sites, yielding a 185 bp Illumina-sequencing-ready product (Figure 1—figure supplement 1). We used BarSeq primers from Wetmore et al. (de Hoon et al., 2004) (Supplementary file 4), except we replaced primer P1 with a mix of primers with 2–4 random bases to improve nucleotide balance for optimal sequencing of low-diversity sequences (Illumina, 2013). We cleaned PCR products with a DNA clean and concentrator kit (Zymo Research, D4014). We quantified product yield with a Qubit 3.0 fluorometer system and mixed as appropriate for sequencing as multiplexed libraries. We sequenced libraries on an Illumina HiSeq 4000 system at the UC Berkeley Vincent J. Coates Genomics Sequencing Laboratory. If necessary, libraries were purified further with a Pippin Prep system (Sage Biosciences) before loading with 15% PhiX DNA as a phasing control for low diversity samples (Illumina, 2013). We sequenced each biological replicate to a depth of at least 20 million reads. We counted occurrences of T-DNA barcodes in each sample with the script MultiCodes_Variable_Length.pl, a modified version of MultiCodes.pl from Wetmore et al. (Wetmore et al., 2015) that allows for barcodes of 17–23 base pairs.

### Fitness analysis

For all BarSeq experiments, we thawed frozen aliquots of the mutant pool on ice and inoculated them into YPD at OD 0.2. Cultures were recovered for about 12 hr until OD 600 was approximately 0.8. Cultures were pelleted at 3,000 RCF for 5 min, washed twice in the appropriate media, and transferred to the condition of interest. Samples were taken from the YPD starter cultures (Time 0) and after 5–7 doublings in the experimental condition. Average fitness scores and T-like statistics as metrics for consistency between individual insertion mutants in each gene were calculated with the scripts combineBarSeq.pl and FEBA.R from Wetmore et al. (Wetmore et al., 2015).

Briefly, for each biological replicate and condition, for any barcode with an average of at least three counts in Time 0 samples, a strain fitness score is calculated as Fstrain = log2(Ccondition +sqrt(P)) – log2(CTime0 +1/sqrt(P)), where C is the raw counts for the barcode and P is a gene-specific ‘pseudocount’ added to reduce noise in fitness scores for low-count strains. These strain fitness scores are then normalized such that the median score is 0 to correct for coverage differences between the samples. The strain fitness scores are then assigned a weight proportional to the harmonic mean of counts at Time 0 and in the condition sample. For any one barcode, the weighting mean is capped at 20 reads, which has the effect of limiting the influence of generally more abundant outlier strains (Wetmore et al., 2015). T is calculated as the gene fitness divided by the square root of the variance in strain fitness scores. This variance is estimated as the maximum value of a naïve estimate based on Poisson noise or the observed variance (a weighted sum squares of differences in strain fitness versus gene fitness scores plus an estimate of global variance in gene fitness scores calculated by comparing fitness scores in the first and second half of every gene). See the methods subsection ‘BarSeq data analysis and calculation of gene fitness’ in the original publication by Wetmore et al. (Wetmore et al., 2015) for more detail on these algorithms. Wetmore et al. limited their analysis to genes with an average of at least 30 total counts at Time 0, spread across three strains. Because the list of genes satisfying this requirement can change from experiment to experiment, we established a list of genes that met this requirement in any of our experiments and used that list for our analysis. As a result, a minority of genes (649) have fitness scores based on data from one or two barcodes. The number of barcodes used in fitness analysis of each gene is listed in all relevant tables in Supplementary file 2. In general, genes with data from only one or two barcodes had smaller T-statistics and thus were filtered out in later analyses.

Because Wetmore et al.’s software does not consider biological replication between independent cultures, we then averaged fitness scores for each condition and combined T-statistics across replicates with the script AverageReplicates.py, treating them as true T-statistics. That is: Tcondition = Sum(Treplicates)/Sqrt(Nreplicates). To assess consistency of differences in observed fitness between growth conditions we computed Tc1 – c2 = (Fc1 – Fc2)/Sqrt ((Fc1/ Tc1)2 + ((Fc2/ Tc2)2) with the script ResultsSummary.py. We generated K-means clusters of fitness scores using Pearson correlation as the similarity metric using Cluster 3.0 (de Hoon et al., 2004). For comparing enrichment in density and FACS separated fractions we computed F and T for each fraction versus the T0 control. The enrichment score E and T between fractions was then calculated as E = Fhigh lipid – Flow lipid and Thigh lipid – low lipid = (Fhigh lipid – Flow lipid)/Sqrt ((Fhigh lipid/ Thigh lipid)2 + ((Flow lipid/ Tlow lipid)2) with the script ResultsSummary.py. We generated hierarchical clusters of enrichment scores using Pearson correlation as the similarity metric and average linkage as the clustering method. All fitness data are available in Supplementary file 2 and the fitness browser (http://fungalfit.genomics.lbl.gov/). Custom Python scripts are available at (Coradetti, 2018b; copy archived at https://github.com/elifesciences-publications/rb-tdnaseq). Sequence data have been submitted to the NCBI Short Read Archive (SRP116193)

### Transformation of R. toruloides by electroporation

We cultured R. toruloides overnight in 10 mL YPD on a roller drum to an OD 600 of 2, then pelleted cells at 3,000 RCF for 5 min at 4°C in a benchtop centrifuge (Eppendorf, 5810 R). Cells were kept at 4°C from this point. We transferred the pellets to 1.5 mL tubes and washed them four times with ice cold 0.75 M D-sorbitol (Sigma-Aldrich, S1876), centrifuging each wash 30 s at 8,000 RCF, 4°C (Eppendorf, 5424). After the final wash, we removed excess D-sorbitol and added 35 µl of cell pellet to 10 µl of fresh 0.75 M D-sorbitol and ~1 µg of PCR product in 5 µl water in a chilled 0.1 cm cuvette. We electroporated cells at 1.5 kV, 200 ohms and 25 µF with an ECM 630 (BTX) electroporation system. We then added 1 mL cold 1:1 mixture of YPD and 0.75 M D-sorbitol and transferred to 14 mL round bottom culture tubes for a 3 hr recovery culture at 30°C with shaking at 200 rpm on a platform shaker. We then pelleted the cultures at 8,000 RCF for 30 s, suspended in 200 µl YPD, and then plated on YPD with 100 µg/mL nourseothricin (5.005.000, Werner Bioagents, Germany).

### Gene ontology enrichment

We scored enrichment of gene ontology terms with a custom script that performs a hypergeometric test on the frequency of each term in the genome versus the frequency in given gene set (script GOenrich.py, available at [Coradetti, 2018b]). We corrected for multiple hypothesis testing with the Benjamini-Hochberg correction (Benjamini and Hochberg, 1995). We extended the GO terms associated with R. toruloides genes in the current JGI annotation by collecting terms for orthologous genes in Arabidopsis thaliana, Aspergillus nidulans, Caenorhabditis elegans, Candida albicans, Homo sapiens, Mus musculus, and Saccharomyces cerevisiae, obtained from the Gene Ontology Consortium (Ashburner et al., 2000; Gene Ontology Consortium, 2015).

### Total fatty acid quantification with gas chromatography

Cell lysis, extraction of total lipids, and conversion to fatty acid methyl esters (FAMEs) was based on a published protocol (Browse et al., 1986). We cultured IFO 0880, a selection of seven targeted deletion strains (see Supplementary file 6) and one overexpression strain (RT880-AD, [Zhang et al., 2016a]) in low nitrogen medium for 48 or 96 hr. We collected paired 5 mL samples from each in screw-top glass tubes (Corning, 99502–10, Corning, NY) and 15 mL polyethylene tubes (Corning, 352096) for lipid extraction and mass determination, respectively. We pelleted samples by centrifugation at 2,000 RCF for 20 min at 4°C, and washed once in water to remove salts and unused glucose. We then transferred the mass determination sample to a pre-tared 1.5 mL microcentrifuge tube. We froze both samples at −20°C overnight, then lyophilized them 48 hr in a FreeZone freeze dry system (Labconco, 7754042) before weighing/extraction. We added 1 mL methanol spiked with 250 µg methyl tridecanoate to each sample to serve as an internal standard (ISTD). We then resuspended lipid extraction samples (usually about 10–20 mg) by vortexing in 3 mL 3N methanolic HCl (Sigma-Aldrich, 33050-U) and 200 µl chloroform (Sigma-Aldrich, 472476) and incubated at 80°C water bath for 1 hr. Cell lysis and conversion to FAMEs occurs during this incubation. To extract FAMEs we then added 2 mL hexane (Sigma-Aldrich, 650552) and vortexed samples well before centrifugation at 3,000 RCF for 3 min. One µL of the hexane layer was injected in split mode (1:10) onto a SP-2330 capillary column (30 m x 0.25 mm x 0.2 µm, Sigma-Aldrich, 24019). An Agilent 7890A gas chromatograph equipped with a flame ionization detector (FID) was used for analysis with the following settings: Injector temperature 250°C, carrier gas: helium at 1 mL/min, temperature program: 140°C, 3 min isocratic, 10 °C/min to 220°C, 40 °C/min to 240°C, 5 min isocratic. FAME concentrations were calculated by comparing the peak areas in the samples to the peak areas of ten commercially available high-purity standards (C16:0, C16:1, C17:0, C18:0, C18:1, C18:2, C20:0, C20:1, C22:0, C24:0) (Sigma-Aldrich) in known concentration relative to the internal standard, respectively.

### Relative TAG measurement with BODIPY and flow cytometry

We inoculated deletion mutants and the YKU70∆ parental strain at OD 0.1 in low nitrogen medium and cultured for 40 hr. We fixed samples by adding 180 µl cell culture to 20 µl 37% formaldehyde (Electron Microscopy Sciences, Hatfield, PA) and incubating for 15 min at room temperature. We then diluted fixed cells 1:100 in 200 µl PBS (from 10X concentrate, Thermo Fisher Scientific, 70011–44) with 0.5 M KI and 0.25 µg/mL BODIPY 493/503 (Thermo Fisher Scientific, D-3922), then incubated 30 min at room temperature. We quantified BODIPY signal for 10,000 cells per sample on a Guava HT easyCyte system (EMD Millipore) in the green channel (excitation 488 nm, emission 525 nm) using InCyte software (EMD Millipore). Due to logistical constraints, samples were processed in batches of at most 30 cultures at a time. Each batch included three biological replicates of the YKU70∆ parental strain as an internal reference. Distribution of mutant strains into these batches was not explicitly randomized, but each batch included both strains expected to accumulate more lipid and strains expected to accumulate less lipid than the parent. Each mutant was processed in at least two different batches.

### Population enrichment with FACS

We cultured the barcoded mutant pool in low nitrogen medium for 40 hr. We then diluted unfixed cells 1:100 in 10 ml PBS with 0.5 M KI and 0.25 µg/mL BODIPY 493/503, then incubated 30 min at 30°C with shaking. We then sorted the population on a Sony SH800 cell sorter with a 70 µM fluidic chip, sorting in semi-purity mode. We first applied a gate for single cell events with forward scatter height within 15% of forward scatter area. We sorted a sample of 10 million cells with the scattering gate alone as a control population, to account for effects of growth, sorting, and collection that are independent of lipid accumulation. Then we collected the 10% of the size-filtered population with the highest and lowest signals in the FITC channel. We collected 10 million cells each for the high and low signal populations. We collected all sorted cells in YPD with 300 µg/ml cefotaxime (Sigma-Aldrich, C7039) and 300 µg/ml carbenicillin (Sigma-Aldrich, C1389), then grew them to saturation in our standard culture conditions and pelleted 1 mL sample, and then stored at −20°C for BarSeq analysis.

### Population enrichment with sucrose density gradients

We prepared linear sucrose gradients with the method of Luthe et al. (Luthe, 1983). For example, to prepare a 65–35% sucrose gradient; we prepared four solutions of sucrose (Sigma-Aldrich, G7528) at 65, 55, 45, and 35 grams per 100 mL in PBS, then successively froze 10 mL layers of each concentration in a 50 mL conical tube (Corning, 430829) on dry ice and stored the gradient at −20°C. We selected appropriate gradients to maximize the physical separation of the cell population by running trial experiments with wild type IFO 0880 cultures on a number of sucrose gradients. The gradients used in each experiment are described in Table 3. Approximately 24 hr before performing density separation on cell population, the appropriate step gradient was moved to 4°C to thaw, yielding a linear gradient (Luthe, 1983).

**Table 3.**
 Sucrose density gradients used in this study


<table>
  <thead>
    <tr>
      <th>Media</th>
      <th>Time</th>
      <th>Sucrose range (Density)*</th>
      <th>Average density ±StDev</th>
      <th>High buoyancy fractions (Density)</th>
      <th>Median buoyancy fractions (Density)</th>
      <th>Low buoyancy fractions (Density)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Low Nitrogen</td>
      <td>40 hr</td>
      <td>50–20% (1.22–1.10)</td>
      <td>1.177 ±0.003</td>
      <td>17–20 (&lt;1.11)</td>
      <td>6–7 (1.18–1.19)</td>
      <td>1–2 (&gt;1.21)</td>
    </tr>
    <tr>
      <td>YPD</td>
      <td>40 hr</td>
      <td>80–50% (1.29–1.16)</td>
      <td>1.234 ±0.012</td>
      <td>19–22† (&lt;1.14)</td>
      <td>4–8† (1.24–1.27)</td>
      <td>1 (&gt;1.28)</td>
    </tr>
  </tbody>
</table>

_All density measurements in g/mL*Highest and lowest specific density measured in any collected fraction in the linear portion of the gradient.†Some biological replicates differ in exact fractions collected. Fractions were collected within this range such that the high buoyancy fraction constituted the most buoyant 5–10% of the population, the median buoyancy fraction constituted the median 30–50% of the population and the low buoyancy fraction constituted the least buoyant 5–10% of the population._

To perform the separation, we centrifuged 50 mL of culture at 6,000 RCF at 4°C for 20 min. We then suspended the pellet in 5 ml PBS at 4°C and carefully loaded it onto a sucrose gradient. We centrifuged the gradients for 1 hr at 5,000 RCF at 4°C with slow acceleration and no brake for deceleration in an Avanti J-26 XP centrifuge with a JS5.3 swinging bucket rotor (Beckman Coulter, Brea, CA). To collect fractions, we pierced the bottom of each tube with the tip of a 16 gauge needle (BD Biosciences, 305197), to slowly drain the gradient from the bottom, at 1 drop every 1–5 s. We collected 2 mL fractions, estimated average fraction density by weighing a 100 µl sample and measured the distribution of the cell population across the sample by optical density. The appropriate fractions were then combined to sample the least buoyant (highest density) 5–10%, median buoyancy 30–50%, and most buoyant (lowest density) 5–10% of the population. For each biological replicate, we also collected a 1 mL sample from the culture before separation to monitor growth in the experimental condition.

### Microscopy

Cover slips were submerged in 0.1% v/v polylysine (Sigma-Aldrich, P8920) for 15 min. Cover slips were removed from polylysine and blotted dry from the bottom of vertically-held slips. Slips were then washed several times with ddH2O and rapidly dried with compressed air. Directly prior to imaging, slips were visually inspected for streaks and dust and softly cleaned with lens paper. Cells were grown 40 hr in low nitrogen medium, 1 mL of culture was transferred to 2 mL microcentrifuge tubes with 1 mL of PBS, and tubes were mixed briefly by vortexing. Cells were pelleted at 9,000 RCF for 1 min in a microcentrifuge, and then resuspended in 100 µl of fluorescent staining solution (PBS with 0.5 M KI and 0.25 µg/mL BODIPY 493/503) to visualize intracellular lipid droplets. Four µl of stained cells were pipetted up and down and transferred to the clean slides. Polylysine-coated cover slips were carefully placed on the 4 µl drop to ensure even spreading of liquid. Cells were observed on an Axio Observer microscope (Carl Zeiss Microscopy, Thornwood, NY) with a plan-apochromat 100x DIC objective (Carl Zeiss Microscopy, 440782-9902-000), ORCA-Flash 4.0 camera (Hamamatsu, C11440-22CU, Japan), and ZenPro 2012 (blue edition) software. For BODIPY imaging cells were illuminated with an X-cite Series 120 arc-lamp (EXFO Photonics Solutions, Canada) and 38HE filter set, 450–490 excitation, 500–550 emission (Carl Zeiss Microscopy, 489038-9901-000). Zvi files were converted to 16 bit TIFF images and representative fields of view were cropped and channels merged using FIJI image processing software (Schindelin et al., 2012).
