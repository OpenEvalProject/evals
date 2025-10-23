# Epigenetic conservation at gene regulatory elements revealed by non-methylated DNA profiling in seven vertebrates

## Authors

- Hannah K Long<sup>1</sup>
- David Sims<sup>3</sup>
- Andreas Heger<sup>3</sup>
- Neil P Blackledge<sup>1</sup>
- Claudia Kutter<sup>4</sup>
- Megan L Wright<sup>5</sup>
- Frank Grützner<sup>5</sup>
- Duncan T Odom<sup>4</sup>
- Roger Patient<sup>2</sup>
- Chris P Ponting<sup>3</sup> †
- Robert J Klose<sup>1</sup> †

### Affiliations

1. Department of Biochemistry University of Oxford Oxford United Kingdom
2. Weatherall Institute of Molecular Medicine, University of Oxford Oxford United Kingdom
3. CGAT, MRC Functional Genomics Unit, Department of Physiology, Anatomy and Genetics University of Oxford Oxford United Kingdom
4. Cancer Research UK – Cambridge Institute, University of Cambridge Cambridge United Kingdom
5. School of Molecular and Biomedical Science The Robinson Institute, University of Adelaide Adelaide Australia
6. Wellcome Trust Sanger Institute Cambridge United Kingdom

† Corresponding author

## Abstract

10.7554/eLife.00348.001 Two-thirds of gene promoters in mammals are associated with regions of non-methylated DNA, called CpG islands (CGIs), which counteract the repressive effects of DNA methylation on chromatin. In cold-blooded vertebrates, computational CGI predictions often reside away from gene promoters, suggesting a major divergence in gene promoter architecture across vertebrates. By experimentally identifying non-methylated DNA in the genomes of seven diverse vertebrates, we instead reveal that non-methylated islands (NMIs) of DNA are a central feature of vertebrate gene promoters. Furthermore, NMIs are present at orthologous genes across vast evolutionary distances, revealing a surprising level of conservation in this epigenetic feature. By profiling NMIs in different tissues and developmental stages we uncover a unifying set of features that are central to the function of NMIs in vertebrates. Together these findings demonstrate an ancient logic for NMI usage at gene promoters and reveal an unprecedented level of epigenetic conservation across vertebrate evolution. DOI: http://dx.doi.org/10.7554/eLife.00348.001

## Introduction

Short contiguous regions of non-methylated DNA are found associated with most human and mouse gene promoters, where they create a transcriptionally permissive chromatin environment (Blackledge et al., 2010; Thomson et al., 2010; Blackledge and Klose, 2011; Deaton and Bird, 2011; Jones, 2012) that opposes the repressive effects of DNA methylation (Klose and Bird, 2006; Weber and Schubeler, 2007). In non-methylated regions, CpG dinucleotide frequency is elevated compared to surrounding sequence (Bird et al., 1985; Bird, 1987). This is due to accelerated methyl-cytosine mutability, which over evolutionary time leads to a reduction in CpG dinucleotide frequency in densely methylated regions of the genome, while CpG frequency is preserved in non-methylated regions (Coulondre et al., 1978; Bird, 1980). Taking advantage of the methylation-dependent variations in nucleotide frequency observed in mammals, algorithms were developed to predict non-methylated regions of DNA based primarily on elevated local G+C content and CpG dinucleotide frequency (Gardiner-Garden and Frommer, 1987; Takai and Jones, 2002).

For more than two decades, CpG island (CGI) predictions (and other nucleotide-based analyses; Saxonov et al., 2006) have been used as a proxy for non-methylated DNA in vertebrate comparative genomics, promoter mapping, and epigenetic studies, often despite little or no experimental evidence that CGIs correspond to bona fide regions of non-methylated DNA outside of mammals (Ioshikhes and Zhang, 2000; Hannenhalli and Levy, 2001; Bock et al., 2007; Han and Zhao, 2008). In mouse and human roughly 50–65% of transcription starts sites (TSSs) overlap with CGI predictions. Interestingly, CGI predictions in cold-blooded vertebrates often reside away from gene promoters, with only 16% of zebrafish and 17% of frog TSSs overlapping predicted CGIs. This has led to the suggestion that non-methylated DNA is a unique feature of gene promoters in endotherms, potentially representing a major divergence in the usage of this epigenetic system between warm-blooded and cold-blooded vertebrates (Aïssani and Bernardi, 1991; Sharif et al., 2010).

Here we experimentally identify non-methylated islands (NMIs) of DNA in the genomes of seven diverse vertebrates, encompassing major evolutionary branch points and including both warm and cold-blooded vertebrates. Interestingly we reveal that CGI prediction does not accurately identify islands of non-methylated DNA, particularly in lower vertebrates. Using our new NMI maps we are able to examine for the first time the relationship between these epigenetically specified features and gene regulatory elements. Interestingly, in contrast to expectation based on CGI predictions in some cold-blooded vertebrates, we now reveal that NMIs are a central and conserved feature of vertebrate gene promoters. Together this work uncovers a unifying set of features that are common to NMI systems across vertebrates and details an unexpected level of epigenetic conservation at vertebrate gene promoters.

## Results

## CGIs poorly predict the location of experimentally determined non-methylated islands in vivo

In order to understand whether the prevailing views about non-methylated DNA function and proposed divergence amongst vertebrate species based on CGI prediction are correct, we isolated genomic DNA from the testes of seven representative vertebrates and carried out non-methylated DNA profiling using biotinylated CxxC affinity purification (Bio-CAP) (

![Figure 1.](https://cdn.elifesciences.org/articles/00348/elife-00348-fig1-v1.jpg)

**Figure 1.:** (A) Non-methylated DNA profiles in testes at a representative syntenic region for seven vertebrate species. Genes are shown in black (improved annotation of gene TSSs using RNA-seq data is shown in red), CpG island predictions in green (CGI), and non-methylated DNA profiles are shown in blue. A phylogenetic tree (left) highlights the evolutionary relationship among the seven species. Dashed grey lines highlight the relationship between the gene TSSs across the species. A gap in the zebrafish profile indicates that aptx is found at a separate locus from dnaja1 and smu1. (B) The genome-wide overlap between CpG islands (green) and non-methylated islands (blue) is depicted as a Venn diagram for each of the species. (C) Nucleotide properties of non-methylated islands and control regions are depicted as density plots. CpG observed/expected (left) and GC content (right) are shown for NMI and control regions of the genome. Median values are shown as dark vertical lines. Thresholds for CpG island prediction are indicated (black dashed line).DOI: http://dx.doi.org/10.7554/eLife.00348.003

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/00348/elife-00348-fig1-figsupp1-v1.jpg)

**Figure 1—figure supplement 1.:** (A) and (B) Profiles of non-methylated DNA are shown in testes at two representative syntenic regions for seven vertebrate species. Genes are shown in black (improved annotation of gene TSSs using RNA-seq data is shown in red), CpG island predications in green, and non-methylated DNA profiles are shown in blue. A phylogenetic tree (left) highlights the evolutionary relationship among the seven species and dashed grey lines highlight the relationship between the gene TSSs across the species.DOI: http://dx.doi.org/10.7554/eLife.00348.004

## Nucleotide properties within NMIs are variable in different vertebrate genomes

To understand why CGI prediction algorithms often fail, we analysed in detail the nucleotide features of NMIs for all species with a focus on the ratio of observed CpG over expected CpG dinucleotides (CpG O/E) and total G+C nucleotide content (GC content). These are the two features commonly used to identify CGIs genome-wide (Gardiner-Garden and Frommer, 1987). We hypothesised that the algorithms may struggle when faced with greatly contrasting genome-wide nucleotide compositions characteristic of diverse phyla. As expected, human and mouse NMIs show elevated CpG O/E and GC content compared to control regions of the genome (Figure 1C). However, many human and mouse NMIs have lower CpG O/E and GC content than the CGI predictions, explaining why the CGI predictions do not accurately identify all NMIs in these species. CGI predictions in chicken are surprisingly accurate. This appears to be due to the fact that NMIs in this species have the highest CpG O/E and GC content compared to the surrounding genome amongst all the vertebrates examined. Although platypus NMIs have a similarly high CpG O/E and GC content, its genome is on average more CpG and GC rich than chicken. This causes the algorithm to massively over-predict CGIs. Lizard and frog encode NMIs with CpG O/E content similar to those in mammals, but with lower GC content. In zebrafish, NMI CpG O/E is high yet the GC content is almost indistinguishable from surrounding DNA sequence (Cross et al., 1991). Again, in these species this leads to a general failure of CGI prediction to accurately identify NMIs.

The failure of CpG island prediction algorithms to accurately identify NMIs in different species is almost certainly dependent on the variation in CpG density and G+C content amongst vertebrate genomes, but also will rely on genome assembly and annotation quality, particularly of repetitive elements. Indeed, based on genome variations in CpG and G+C content, it has been suggested previously that species-specific CpG island annotation may be required (Glass et al., 2007). These sequence variations between species are likely driven by the relative strengths of two processes: reductions of G+C content due to imperfect repair of spontaneous 5-methylcytosine deamination events (Coulondre et al., 1978; Bird, 1980) and increases in G+C content in species and genomic regions that are especially prone to GC-biased gene conversion, an outcome of recombination (Duret and Galtier, 2009). Species differences in these antagonistic processes are likely to have caused the varying levels of G+C content both among vertebrates and across different regions of most amniotic genomes. Unlike CGI predictions, Bio-CAP identifies NMIs through an affinity based isolation of non-methylated CpGs and therefore does not solely rely on nucleotide content in the same way prediction algorithms do. Nevertheless, we considered whether the efficiency of NMI identification by Bio-CAP among species differs due to non-methylated CpG content and density. In contrast, non-methylated DNA fragments, even with low CpG density, are effectively detected by Bio-CAP (Blackledge et al., 2012) and a broad distribution of CpG density within NMIs is identified in all species. Therefore, although CGI prediction does function with some degree of accuracy in mammals and bird, CGI prediction maps are in general a poor indicator of where NMIs exist in vivo, presumably due to varying nucleotide content amongst diverse phyla. In light of the fact that CGI prediction maps largely fail to accurately detect experimentally-identified non-methylated regions of DNA, work over the past 25 years that has extensively used these maps as a proxy for non-methylated DNA and evolutionary comparison clearly requires re-evaluation.

## NMIs are a highly conserved feature of vertebrate gene promoters

Using our new genome-wide maps of non-methylated DNA, we first set out to directly examine whether NMIs are a specific feature of warm-blooded vertebrate gene promoters as has previously been suggested (

![Figure 2.](https://cdn.elifesciences.org/articles/00348/elife-00348-fig2-v1.jpg)

**Figure 2.:** (A) A histogram depicting the proportion of protein-coding transcription start sites (TSSs) which are overlapped by an NMI for all seven species. Blue bars indicate overlap with annotated TSSs and red bars indicate overlap with additional TSSs identified using RNA-seq data (platypus, chicken and lizard) or Xtev gene sets (frog). (B) Profiles of non-methylated DNA were plotted over a 6-kb window centred on all TSSs with an NMI (dark blue), without an NMI (blue), and for all transcription termination sites (TTS, black). The non-methylated DNA signal peaks at the TSS of gene promoters in all vertebrates.DOI: http://dx.doi.org/10.7554/eLife.00348.005

Although DNA sequence within gene regulatory elements is often conserved across vertebrate species, it remains almost completely unknown whether epigenetic features are subject to a similar selective pressure. Interestingly, some evidence has emerged recently indicating that certain epigenetic features may be conserved between mammalian species (

![Figure 3.](https://cdn.elifesciences.org/articles/00348/elife-00348-fig3-v1.jpg)

**Figure 3.:** (A) The presence of NMIs at orthologous gene TSSs is preserved as illustrated by a pairwise analysis of NMIs at vertebrate gene orthologues. The percentage of NMIs conserved at orthologous gene TSSs was calculated in a pairwise manner and found to be highly statistically significant for all comparisons across the seven vertebrate species (p<10−10, hypergeometric test). (B) A proportional Venn diagram illustrating the three-way comparison of NMI presence at conserved human-mouse-zebrafish gene orthologue TSSs.DOI: http://dx.doi.org/10.7554/eLife.00348.006

## Intergenic NMIs are associated with distal regulatory elements, non-coding RNAs, and unannotated transcripts

In addition to gene associated NMIs, an unexpectedly large proportion of vertebrate NMIs lie within intergenic regions (

![Figure 4.](https://cdn.elifesciences.org/articles/00348/elife-00348-fig4-v1.jpg)

**Figure 4.:** (A) Most NMIs are associated with known protein-coding genes (left) but a substantial proportion are located within intergenic regions of the genome (right). (B) NMIs (green) are found at 45% and 64% of all known long non-coding RNA (lncRNA) TSSs (black) in mouse and zebrafish respectively. (C) A pie chart depicting the proportion of intergenic NMIs (>5 kb from a protein-coding gene) associated with different genomic features in mouse embryonic stem (ES) cells and zebrafish 24 hpf embryos. The association was performed hierarchically in the following order: lncRNA TSSs, other non-coding RNA TSSs (miRNAs, rRNAs, snRNAs, or snoRNAs), other TSSs (pseudogenes and processed transcripts), putative enhancer mark H3K4me1 and novel RNA-seq TSSs. This analysis indicates that intergenic NMIs mark novel transcriptional units or regulatory elements.DOI: http://dx.doi.org/10.7554/eLife.00348.007

## Differentially methylated islands are found away from gene promoters

In general NMIs in mammals are thought to be maintained in the non-methylated state in most tissues, even if their associated gene is not appreciably transcribed. Recently this belief has been challenged and it appears that some NMIs in human and mouse are more susceptible to differential methylation during tissue specification (

![Figure 5.](https://cdn.elifesciences.org/articles/00348/elife-00348-fig5-v1.jpg)

**Figure 5.:** (A) All vertebrate genomes have a subset of NMIs that are subject to differential methylation as illustrated by a heat map of non-methylated DNA signal from testes and liver in human, mouse and zebrafish. In each case NMIs are ranked according to length and clustered as shared (upper) or unique (lower) between the two tissues. A 5-kb window centred at the NMI is shown and read density is indicated by colour intensity. (B) The overlap of NMIs identified in liver and testes is depicted by Venn diagrams for NMIs associated with protein-coding TSSs (upper) and for NMIs away from TSSs (lower). NMIs at TSSs are generally non-methylated in both tissues whereas differentially methylated NMIs tend to be found away from TSSs. (C) NMI length distribution plots for shared (Shared NMIs, solid line) or unique (Unique NMIs, dashed line) NMIs from testes (blue) or liver (red). Shared NMIs tend to be longer than tissue-specific unique NMIs. (D) CpG density distribution plots for shared (solid line) or unique (dashed line) NMIs from testes (blue) or liver (red). Shared NMIs tend to have higher CpG density than unique NMIs.DOI: http://dx.doi.org/10.7554/eLife.00348.008

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/00348/elife-00348-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** (A, i–iv) Mouse NMIs unique to liver or testes were analysed by bisulfite sequencing to verify that the regions were indeed differentially methylated. Traces of non-methylated DNA are depicted for differentially methylated regions in mouse liver (red) and testes (blue) with NMIs depicted as bars under the traces. The y-axis depicts read density. Methylation status of the unique NMIs was confirmed using the indicated bisulfite PCR amplicon (BA, black rectangle). Empty and filled circles represent non-methylated and methylated CpG dinucleotides, respectively. (B, (i–iii) Zebrafish NMIs unique to liver or testes were validated by bisulfite sequencing as in (A).DOI: http://dx.doi.org/10.7554/eLife.00348.009

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/00348/elife-00348-fig5-figsupp2-v1.jpg)

**Figure 5—figure supplement 2.:** (A) A heat map of non-methylated DNA signal from testes and liver in platypus, chicken, lizard and frog. In each case NMIs are ranked according to length and clustered as shared (upper) or unique (lower) between the two tissues. A 5-kb window centred at the NMI is shown and read density is indicated by colour intensity. (B) Venn diagrams demonstrate that shared NMIs are found predominantly at protein-coding gene TSSs (upper) and unique NMIs tend to be found away from TSSs (lower). (C) NMI length distribution plots for shared (Shared NMIs, solid line) or unique (Unique NMIs, dashed line) NMIs from testes (blue) or liver (red). Shared NMIs tend to be longer than tissue-specific unique NMIs. (D) CpG density distribution plots for shared (solid line) or unique (dashed line) NMIs from testes (blue) or liver (red). Shared NMIs tend to have higher CpG density than unique NMIs.DOI: http://dx.doi.org/10.7554/eLife.00348.010

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/00348/elife-00348-fig5-figsupp3-v1.jpg)

**Figure 5—figure supplement 3.:** MA plots depicting expression differences for genes with TSS-associated NMIs from liver and testes for human, mouse, platypus and chicken. Genes are coloured according to whether they share an NMI in both liver and testes (grey) or have an NMI only in liver (red) or testes (blue). Genes are further distinguished as being differentially expressed or overexpressed in a tissue-specific manner (dark, filled circle) or not (light, open circles). The log mean expression of the gene from both liver and testes is displayed on the x axis (A) and the log ratio of gene expression is displayed on the y axis (M). The dotted lines indicate a fold change threshold of two. Genes with tissue-specific NMIs were significantly over-represented in the set of genes which had increased differential expression in seven out of eight cases (Fisher's exact test, human testes p<10−21, liver p<10−27; mouse testes p<10−18, liver p<10−8; platypus testes p<10−2, liver p<10−17; chicken liver p<10−6).DOI: http://dx.doi.org/10.7554/eLife.00348.011

## Chromatin modifications at differentially methylated NMIs are dependent on the underlying DNA methylation state

Most tissue-specific NMIs are intergenic, indicating that differential methylation of these elements in vertebrate genomes is generally found away from known gene promoters (

![Figure 6.](https://cdn.elifesciences.org/articles/00348/elife-00348-fig6-v1.jpg)

**Figure 6.:** (A) H3K4me3 read density from testes (blue) and liver (red) is profiled over testes unique (left) and liver unique (right) NMIs for human (upper) and mouse (lower) and displayed as an average profile. At differentially methylated loci, the histone H3K4me3 modification is found preferentially in the tissue with the non-methylated NMI. (B) The H3K4me3 signal (profiled in frog stage 11–12 embryos and zebrafish 24 hpf) is present specifically at unique NMIs from frog stage 11–12 and zebrafish 24 hpf (green) and not at unique NMIs from the liver (red).DOI: http://dx.doi.org/10.7554/eLife.00348.012

## A unique class of ‘broad’ NMIs are associated with developmental genes and subject to polycomb regulation

The majority of vertebrate genes have a punctate peak of non-methylated DNA at their TSS in fitting with the canonical view of an NMI (

![Figure 7.](https://cdn.elifesciences.org/articles/00348/elife-00348-fig7-v1.jpg)

**Figure 7.:** (A) An example of a broad region of non-methylated DNA associated with the sp9 gene for four representative species (human, mouse, frog and fish). Dashed grey lines highlight the location of the gene TSSs across the four species. (B) Non-methylated DNA profiles are depicted for genes associated with broad NMIs (dark blue) and canonical NMIs (light blue) in mouse embryonic stem (ES) cells and frog stage 11–12. The profile is scaled to show an averaged gene with one gene length depicted upstream and downstream. (C) H3K4me3 ChIP-seq signal from mouse and frog was plotted as in (B). H3K4me3 profiles reflect the underlying non-methylated DNA profiles. (D) Genes associated with broad NMIs were analysed by gene ontology (GO) analysis for mouse ES cell and frog stage 11–12. Broad NMIs are found to be significantly enriched for GO term categories associated with sequence-specific DNA binding, transcriptional regulation and development. MF: molecular function; BP: biological process. p<10−5 for all GO terms. (E) H3K27me3 ChIP-seq signal from mouse and frog was plotted for the same gene sets as in (B). The profile is scaled to show an averaged gene with three gene lengths depicted upstream and downstream. As for H3K4me3, H3K27me3 ChIP-seq profiles correspond to the underlying non-methylated DNA profile. (F) A representative example of two broadly non-methylated genes gsx1 and nkx2.2 for mouse and frog. In both species, the broad non-methylated regions (green) are associated with the polycomb repressive mark H3K27me3 (red). In addition, in mouse, polycomb repressive complex 2 (ezh2, yellow and suz12, orange) and polycomb repressive complex 1 (ring1b, purple) components are associated with the broad non-methylated regions. The y-axis depicts read density. Genes are depicted above the profiles in black.DOI: http://dx.doi.org/10.7554/eLife.00348.013

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/00348/elife-00348-fig7-figsupp1-v1.jpg)

**Figure 7—figure supplement 1.:** Hox gene clusters are characterized by broad NMIs.The hoxa gene cluster from all seven vertebrate species is associated with broad regions of non-methylated DNA. Genes are shown in black and non-methylated DNA profiles are shown in blue and dashed grey lines highlight the relationship between conserved gene TSSs across the species.DOI: http://dx.doi.org/10.7554/eLife.00348.014

## Discussion

Although the DNA methylation system is conserved across vertebrate evolution, CGI maps had previously indicated that this epigenetic system may have significantly diverged between vertebrate species and even acquired unique properties at TSSs during the evolution of warm-blooded vertebrates (Aïssani and Bernardi, 1991; Sharif et al., 2010). Despite some recent indications that DNA methylation profiles may be more conserved than previously realised (Feng et al., 2010; Zemach et al., 2010; Wu et al., 2011; Andersen et al., 2012), a lack of experimentally identified regions of non-methylated DNA outside of eutherian mammals has hindered the capacity to specifically address whether this system has significantly diverged among vertebrates. To address this fundamental question and to better understand the level of evolutionary conservation in epigenetic systems, we identified NMIs genome-wide in seven diverse vertebrate species demonstrating for the first time that NMIs are in fact a highly conserved feature of vertebrate gene promoters. Importantly, this paradigm shift also revealed that three distinct yet highly conserved classes of NMIs have emerged during vertebrate evolution. The first class is a canonical NMI that best fits the classical definition of a CGI. These NMIs are narrow, associated with gene promoters, and generally remain free of DNA methylation regardless of the tissue or associated gene expression state. The second class of plastic NMIs are shorter, have lower CpG density than canonical NMIs, are usually found away from gene promoters at alternative regulatory elements, and are subject to differential methylation between tissues. Importantly, this class of NMI demonstrates that epigenetic plasticity in the form of differential methylation is a highly conserved mechanism utilised by all vertebrates. Finally, a third and unique class of broad NMIs were identified that often cover an entire gene, are specifically associated with transcription factors or developmental genes, and are associated with polycomb mediated silencing during early development. These three classes of NMIs appear to form a highly conserved logic for the utilisation of non-methylated DNA in vertebrate genomes. Therefore, in contrast to the suggestion that NMIs may have diverged during vertebrate evolution (Aïssani and Bernardi, 1991; Sharif et al., 2010), we demonstrate that the central properties that underpin the NMI system are instead highly conserved across vertebrates. Perhaps most importantly, TSS-associated NMIs appears to be under strong selective pressure as part of what appears to be a highly conserved epigenetic system used to specify and control gene regulatory elements in large and complex vertebrate genomes.

## Materials and methods

## Preparation of genomic DNA

Samples were obtained either as purified genomic DNA, as fresh-frozen samples or were dissected in-house and fresh-frozen. Samples were subjected to manual homogenisation followed by DNA purification by phenol chloroform extraction or using the QIAGEN 100/G genomic tip kit (Manchester, UK).

## Bio-CAP sequencing

Bio-CAP was performed as previously described (Blackledge et al., 2012). All Bio-CAP experiments were performed in duplicate with matched input controls. Next generation sequencing was performed using two Illumina sequencing platforms: Genome Analyser IIx and HiSeq Systems yielding 51-bp single-end reads.

## External datasets

Computationally predicted CpG islands for all seven species were obtained from the UCSC genome browser (Kent et al., 2002). LncRNA datasets from recent publications for mouse (Guttman et al., 2010; Belgard et al., 2011; GSE20851, GSE27243) and zebrafish (Ulitsky et al., 2011; Pauli et al., 2012; GSE32900 and GSE32880) were obtained from GEO (Edgar et al., 2002) or from supplementary material. H3K4me1 datasets for zebrafish 24 hpf (Aday et al., 2011; GSE20600) and mouse ES cell (Stadler et al., 2011; GSE30206, GSE11172) were obtained from GEO. Mouse (Smagulova et al., 2011; GSE24438) and human (Hammoud et al., 2009; Bernstein et al., 2010; GSE15594 and GSE19465, testes and liver), frog (Akkers et al., 2009; GSE14025, stage 11–12) and zebrafish (Aday et al., 2011; GSE20600; 24 hpf) H3K4me3 datasets were obtained from GEO. H3K4me3 and H3K27Me3 datasets for mouse (Mikkelsen et al., 2007; GSE12241, ES cells) and frog (Akkers et al., 2009; GSE14025, stage 11–12) were obtained from GEO. RNAseq datasets for human, mouse, platypus and chicken (Brawand et al., 2011; Stadler et al., 2011; Julien et al., 2012; GSE30352, GSE30280 and GSE36120) were obtained from GEO. RNAseq datasets for lizard were obtained from Kutter and Odom pre-publication (Barbosa-Morais et al., 2012; now available at GSE41338) and zebrafish RNAseq data were obtained from the EBI (ERP000016, Sample ERS000081). The XTev dataset (Akkers et al., 2010) was obtained from the Veenstra lab website (http://131.174.221.43/gertjanveenstra/genomedata.asp). ChIP-seq data for a number of polycomb factors profiles for mouse ES cells (Ku et al., 2008; GSE13084) were obtained from GEO.

## Read alignment and peak calling

Sequencing reads were aligned to the appropriate reference genome (anoCar2, danRer7, galGal3, hg19, mm9, ornAna1, xenTro3) using the Bowtie short-read aligner (v0.12.7) (Langmead et al., 2009). Only uniquely mapping reads, with a maximum of two mismatches across the entire read length were used. Non-methylated islands (NMIs) were identified using MACS (v1.4.0) (Zhang et al. 2008) using a bandwidth of 300 and an mfold range of 10–30. Binding intervals were filtered by a q value of 0.01. Data analysis was performed in R and python using bespoke scripts available online (http://www.cgat.org/hg/cgat/).

## Nucleotide properties of NMIs

CpG observed/expected (CpG O/E) and GC content were calculated as in Gardiner-Garden and Frommer (1987). Both measures were calculated for each NMI and for a control region of the same size 10 kb upstream of each NMI interval.

## NMI genomic localisation

Ensembl (release 66) genes were annotated as having an NMI at their TSS using a single base pair overlap of an NMI with a window extending 1 kb upstream and downstream from each transcript TSS. Multi-tissue RNAseq datasets for platypus, chicken and lizard were used to improve the annotation of gene TSSs. Where transcript models were not provided by the authors TopHat (Trapnell et al., 2009) and Cufflinks (Trapnell et al., 2010) were used to construct transcript models from short-read data. Similarly, the XTev gene dataset was used to improve the annotation of TSSs in the frog genome. NMIs were annotated with respect to both Ensembl (release 66) and RNAseq-based genome annotation as being associated with the following features in a hierarchical manner: protein-coding gene TSS (±1 kb), gene body, upstream or downstream of a gene (within 5 kb of the annotated gene model). Remaining NMIs were annotated as intergenic.

For mouse ES cell and zebrafish 24 hpf embyros, published lncRNA models, Ensembl non-coding RNA annotations, tissue-specific H3K4me1 and RNAseq data were used to account for intergenic NMIs in a hierarchical manner. Where short read genomic alignments were not provided by the authors, chromatin mark datasets were aligned to the appropriate reference genome using Bowtie and peaks were called using MACS as above. Throughout, overlap of genomic intervals (e.g., NMIs compared to CGIs, Figure 1B) was assessed using BEDTools (Quinlan and Hall, 2010) and statistical significance calculated using the Genomic Association Tester (GAT) (Ponjavic et al., 2007).

## Evolutionary conservation of NMIs

Evolutionary conservation of protein-coding genes was calculated using OPTIC (Heger and Ponting, 2008). Conserved genes (pairwise 1:1 orthologues) were defined as having an NMI or not as above. The conservation score was calculated as: n/min(x, y) where n is the number of conserved genes with an NMI at the TSS of both orthologues and x and y are the numbers of conserved genes with a TSS-associated NMI in each species. For three-way conservation, 1:1:1 orthologues from human, mouse and zebrafish were defined as having an NMI in one, two or all species.

## Tissue-specific & broad NMIs

NMIs were called from non-methylated DNA profiles in both testes and liver using MACS (as above). An NMI was defined as tissue-specific if it did not overlap with an NMI in the other tissue. Broad NMI-associated genes were defined as having greater than 90% of their gene length covered by NMIs. Short NMI-associated genes had less than 10% (but greater than 0%) gene coverage by NMIs.

## Gene expression analysis

DESeq (Anders and Huber, 2010) was used to identify genes differentially expressed between liver and testes in human, mouse, platypus and chicken RNAseq data (p<0.05, fold change > 2).

## Data visualisation

H3K4me3 signal was profiled across tissue-specific NMIs using sitepro from the CEAS package (Shin et al., 2009). Two-way Venn diagrams were generated in R using the ‘VennDiagram’ package (Chen and Boutros, 2011). The three-way Venn diagram was generated using the EulerAPE drawing tool (http://www.eulerdiagrams.org/eulerAPE/). Genomic peaks and intervals were visualised using the Integrated Genome Browser (IGB) (Nicol et al., 2009).

## Gene ontology

Gene Ontology (GO) analysis was performed using a hypergeometic test. Terms were clustered using a modified ReVigo (Supek et al., 2011) script and a representative term from each cluster was plotted using the GO term enrichment score.
