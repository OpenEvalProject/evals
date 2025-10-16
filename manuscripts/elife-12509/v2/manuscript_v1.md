# Trifunctional cross-linker for mapping protein-protein interaction networks and comparing protein conformational states

## Authors

- Dan Tan<sup>1</sup>
- Qiang Li<sup>2</sup>
- Mei-Jun Zhang<sup>2</sup>
- Chao Liu<sup>6</sup>
- Chengying Ma<sup>7</sup>
- Pan Zhang<sup>1</sup>
- Yue-He Ding<sup>1</sup>
- Sheng-Bo Fan<sup>6</sup>
- Li Tao<sup>1</sup>
- Bing Yang<sup>2</sup>
- Xiangke Li<sup>2</sup>
- Shoucai Ma<sup>2</sup>
- Junjie Liu<sup>7</sup>
- Boya Feng<sup>7</sup>
- Xiaohui Liu<sup>2</sup>
- Hong-Wei Wang<sup>7</sup>
- Si-Min He<sup>6</sup>
- Ning Gao<sup>7</sup>
- Keqiong Ye<sup>2</sup>
- Meng-Qiu Dong<sup>1</sup> †
- Xiaoguang Lei<sup>2</sup> †

### Affiliations

1. Graduate Program Peking Union Medical College, Chinese Academy of Medical Sciences Beijing China
2. National Institute of Biological Sciences Beijing China
3. Synthetic and Functional Biomolecules Center Peking University Beijing China
4. Peking-Tsinghua Center for Life Sciences Peking University Beijing China
5. Department of Chemical Biology, College of Chemistry and Molecular Engineering Peking University Beijing China
6. Key Lab of Intelligent Information Processing of Chinese Academy of Sciences Institute of Computing Technology, Chinese Academy of Sciences Beijing China
7. Ministry of Education Key Laboratory of Protein Sciences, School of Life Sciences Tsinghua University Beijing China

† Corresponding author

## Abstract

10.7554/eLife.12509.001 To improve chemical cross-linking of proteins coupled with mass spectrometry (CXMS), we developed a lysine-targeted enrichable cross-linker containing a biotin tag for affinity purification, a chemical cleavage site to separate cross-linked peptides away from biotin after enrichment, and a spacer arm that can be labeled with stable isotopes for quantitation. By locating the flexible proteins on the surface of 70S ribosome, we show that this trifunctional cross-linker is effective at attaining structural information not easily attainable by crystallography and electron microscopy. From a crude Rrp46 immunoprecipitate, it helped identify two direct binding partners of Rrp46 and 15 protein-protein interactions (PPIs) among the co-immunoprecipitated exosome subunits. Applying it to E. coli and C. elegans lysates, we identified 3130 and 893 inter-linked lysine pairs, representing 677 and 121 PPIs. Using a quantitative CXMS workflow we demonstrate that it can reveal changes in the reactivity of lysine residues due to protein-nucleic acid interaction. DOI: http://dx.doi.org/10.7554/eLife.12509.001

## Introduction

Proteins execute diverse functions by interacting with multiple protein partners in different complexes. The study of protein complex structures and protein-protein interactions is critical for understanding their functions. Recently, chemical cross-linking of proteins coupled with mass spectrometry analysis (CXMS) has emerged as a powerful tool for the analysis of such structures and interactions (Sinz, 2006; Leitner et al., 2010; Petrotchenko and Borchers, 2010; Singh et al., 2010; Rappsilber, 2011; Bruce, 2012). CXMS methods are less time-consuming and less demanding of sample purity than are traditional methods; this technology has thus been increasing in popularity.

Recent progress in the development of analytical instruments, cross-linking reagents, and software has catapulted CXMS from obscurity to prominence, as witnessed by an explosion of successful applications (Bohn et al., 2010; Chen et al., 2010; Kao et al., 2011; Lauber and Reilly, 2011; Herzog et al., 2012; Jennebach et al., 2012; Kalisman et al., 2012; Kao et al., 2012; Leitner et al., 2012; Bui et al., 2013; Murakami et al., 2013; Tosi et al., 2013). However, CXMS is still limited by sample complexity and by low abundances of cross-linked peptides. Extensive fractionation is often required to reduce the complexity of samples that contain macromolecular complexes (Chen et al., 2010; Lauber and Reilly, 2011; Jennebach et al., 2012; Kalisman et al., 2012; Kao et al., 2012; Murakami et al., 2013; Tosi et al., 2013). The identification of cross-linked peptides in more heterogeneous samples such as crude immunoprecipitates and whole-cell lysates is even more difficult (Rinner et al., 2008; Luo et al., 2012; Yang et al., 2012; Liu et al., 2015).

Given the sparsity of cross-linked peptides in samples, it would be beneficial to purify them from complex mixtures using affinity tags after cross-linking. However, despite increased efforts to develop chemical cross-linkers with enrichment functions (Luo et al., 2012; Trester-Zedlitz et al., 2003; Fujii et al., 2004; Chowdhury et al., 2006; Chu et al., 2006; Chowdhury et al., 2009; Kang et al., 2009; Nessen et al., 2009; Yan et al., 2009; Vellucci et al., 2010; Petrotchenko et al., 2011; Sohn et al., 2012; Kaake et al., 2014), few such agents have been shown to improve identification capabilities in complex samples. Two exceptions include Azide-A-DSBSO, which is used with biarylazacyclooctynone (Kaake et al., 2014), and the protein interaction reporter (PIR) (Chavez et al., 2013; Weisbrod et al., 2013). However, special instrument control is recommended for their application (Chavez et al., 2013; Weisbrod et al., 2013).

In this work, we developed a series of chemical cross-linkers with a modular design as pioneered previously (Trester-Zedlitz et al., 2003). They each contain a biotin tag for affinity purification and a cleavage site that can be used to release cross-linked peptides from streptavidin beads. We selected the cross-linker with the best performance and developed a robust enrichment protocol with >97% enrichment efficiency. We termed it Lysine-targeted enrichable cross-linker (Leiker). Using our previously developed pLink identification software (Yang et al., 2012), we here demonstrate that the use of Leiker effectively facilitates CXMS analysis in a variety of sample types, from purified complexes, crude immunoprecipitates, to highly complex whole-cell lysates.

Quantification of cross-linker modified peptides has the potential to detect protein conformational changes and changes in molecular interactions, though these methods are not mature. To address this potentially critical application of our technology, we synthesized stable isotope-labeled Leiker. Also, we established an automated data analysis workflow for the relative quantitation of light and heavy Leiker cross-links. As a proof of concept, we carried out a quantitative CXMS analysis of an RNA-binding protein L7Ae. Using deuterium-labeled Leiker, we found that for the three L7Ae lysine residues that are buried upon RNA binding, their mono-links decreased dramatically in the presence of RNA, exactly as expected. We further extended the application of quantitative CXMS to a highly complex system consisting of log-phase and stationary-phase E. coli cells and identified a growth phase specific protein interaction.

## Results

## Design, synthesis and evaluation of Leiker

We aimed to develop a cross-linker similar to the widely used BS

![Figure 1.](https://cdn.elifesciences.org/articles/12509/elife-12509-fig1-v2.jpg)

**Figure 1.:** The top panel shows four designs of two-piece Leiker with a photo-cleavage site (sulfo-PL, PL, and PEG-PL) or an azobenzene-based cleavage site (AL). Biotin is attached via click chemistry by reacting with bio-aizde. The bottom panel shows two unlabeled (bAL1, bAL2) and deuterium-labeled ([d6]-bAL2) one-piece Leiker molecules. The biotin moiety is colored magenta.DOI: http://dx.doi.org/10.7554/eLife.12509.003

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/12509/elife-12509-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** A) sulfo-PL, (B) AL, (C) bAL1, and (D) bAL2.DOI: http://dx.doi.org/10.7554/eLife.12509.004

![Figure 1—figure supplement 2.](https://cdn.elifesciences.org/articles/12509/elife-12509-fig1-figsupp2-v2.jpg)

**Figure 1—figure supplement 2.:** DOI: http://dx.doi.org/10.7554/eLife.12509.005

![Figure 1—figure supplement 3.](https://cdn.elifesciences.org/articles/12509/elife-12509-fig1-figsupp3-v2.jpg)

**Figure 1—figure supplement 3.:** DOI: http://dx.doi.org/10.7554/eLife.12509.006

![Figure 1—figure supplement 4.](https://cdn.elifesciences.org/articles/12509/elife-12509-fig1-figsupp4-v2.jpg)

**Figure 1—figure supplement 4.:** DOI: http://dx.doi.org/10.7554/eLife.12509.007

![Figure 1—figure supplement 5.](https://cdn.elifesciences.org/articles/12509/elife-12509-fig1-figsupp5-v2.jpg)

**Figure 1—figure supplement 5.:** DOI: http://dx.doi.org/10.7554/eLife.12509.008

![Figure 1—figure supplement 6.](https://cdn.elifesciences.org/articles/12509/elife-12509-fig1-figsupp6-v2.jpg)

**Figure 1—figure supplement 6.:** A) [d0]-bAL2 and (B) [d6]-bAL2.DOI: http://dx.doi.org/10.7554/eLife.12509.009

![Figure 2.](https://cdn.elifesciences.org/articles/12509/elife-12509-fig2-v2.jpg)

**Figure 2.:** (A) Leiker contains a biotin moiety (magenta), a cleavage site (arrows), and six hydrogen atoms that are accessible to isotope labeling (asterisks). (B) The workflow for purification of Leiker-linked peptides. (C) Three types of Leiker-linked peptides. (D) Leiker-linked peptides generate a reporter ion of 122.06 m/z in HCD, as shown in the spectrum of an inter-linked peptide NYQEAKDAFLGSFLYEYSR-LAKEYEATLEECCAK (+4 charged, MH+ 4433.0553), in which C denotes carbamidomethylated cysteine.DOI: http://dx.doi.org/10.7554/eLife.12509.010

## Leiker enabled robust enrichment of cross-linked peptides

To assess to what extent Leiker could improve the identification of low-abundance cross-linked peptides from a complex background, a mixture of ten standard proteins (

![Figure 3.](https://cdn.elifesciences.org/articles/12509/elife-12509-fig3-v2.jpg)

**Figure 3.:** (A) Leiker allowed near 100% enrichment of target peptides from a cross-linked ten-protein mixture diluted with increasing amounts of non-cross-linked E. coli lysates. Dark blue, inter-links; light blue, mono-links; green, loop-links; grey, regular peptides not modified by Leiker. (B) Number of cross-link identifications from E. coli lysates treated with Leiker or BS3. Shown in the left and right panels are the identified spectra and peptides, respectively.DOI: http://dx.doi.org/10.7554/eLife.12509.01110.7554/eLife.12509.012Figure 3—source data 1.DOI: http://dx.doi.org/10.7554/eLife.12509.01210.7554/eLife.12509.013Figure 3—source data 2.DOI: http://dx.doi.org/10.7554/eLife.12509.013

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/12509/elife-12509-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** DOI: http://dx.doi.org/10.7554/eLife.12509.014

The ten standard proteins also allowed us to assess the specificity of Leiker. Because Leiker has more functional groups than BS3 does, a concern arises that Leiker may produce more cross-linking artifacts. Cross-links between non-interacting proteins are surely artifacts, which include all the inter-protein cross-links identified from the ten-protein mixture except those between the light-chain and the heavy-chain of myosin, between the light-chain and the heavy-chain of an IgG antibody, and between PUD-1 and PUD-2, which form a heterodimer. We found that the percentage of artifactual cross-links is 3% for both Leiker and BS3 (Figure 3—source data 2), fitting with the filtering criteria that were applied (FDR cutoff 0.05 followed by E-value cutoff 0.01). The results demonstrate that Leiker is as specific as BS3.

Further, we cross-linked highly complex E. coli lysates with either Leiker or BS3 for a side-by-side comparison. After enrichment and a single reverse phase LC-MS/MS analysis, Leiker yielded at least a fourfold increase in the number of inter-links identified (Figure 3B).

## Application of Leiker to large protein assemblies and immunoprecipitates

Next, we applied Leiker to real-world samples, starting with purified E. coli 70S ribosome, a 2.5 MDa ribonucleoprotein (RNP) complex consisting of more than 50 proteins. A total of 222 inter-linked lysine pairs were identified with high confidence, including 95 inter-molecular and 127 intra-molecular cross-links (Figure 4—source data 1). This is three times as many as in a previous study (Lauber and Reilly, 2011). Of the 95 cross-links connecting two lysine residues that are both present in the crystal structure of a 70S ribosome (Fischer et al., 2015) (PDB code: 5AFI), 75% are compatible with the crystal structure with a Cα-Cα distance ≤22 Å, which is the length of the spacer arm of Leiker plus two lysine side chains. Among the subset of intra-molecular cross-links, 84% have Cα-Cα distances ≤22 Å; among the subset of inter-molecular cross-links, 50% have Cα-Cα distances ≤22 Å and 73% have Cα-Cα distances ≤30 Å, which could be a reasonable cutoff considering conformation flexibility of proteins in solution (Figure 4—source data 1 and Figure 4—figure supplement 1). One particular ribosomal protein L9 is a good example to illustrate conformational flexibility and the dynamic nature of interactions between proteins or protein complexes. A large b-factor in the crystal structure has suggested that L9 is highly mobile. It has been observed to adopt an extended, rod-like conformation in the crystal structure (Schuwirth et al., 2005) and a strikingly different bent conformation in the solution structure of the ribosome determined using cryo-EM (Fischer et al., 2015; Seidelt et al., 2009). Bending of L9 was echoed in this study, as reflected in the cross-links bridging L9 and L2 and the cross-links bridging the two termini of L9 (Figure 4—figure supplement 2). Three additional cross-links involving L9 have Cα-Cα distances >50 Å if measured within a ribosomal particle (Figure 4—source data 1). We propose these apparently long distance cross-links, which are similar to the ones observed in a previous CXMS study (Lauber and Reilly, 2011), reflect interactions between ribosomal particles. L9 locates at the interface between ribosomal particles in higher-order configurations (e.g. polysome) (Brandt et al., 2009). Dimerization or oligomerization of 70S ribosomes in the absence of mRNA was also observed using negative staining EM from highly purified non-cross-linked 70S ribosomes (Figure 4—figure supplement 3).

The peripheral regions of the ribosome are critical for protein translation and regulation (

![Figure 4.](https://cdn.elifesciences.org/articles/12509/elife-12509-fig4-v2.jpg)

**Figure 4.:** (A) Analysis of a purified E. coli 70S ribosome revealed the locations of highly dynamic periphery ribosomal proteins S1, L1, and L7/12 that were refractory to crystallography and cryo-EM analysis. Cross-links to S1, L1, and L7/12 are colored red, blue, and yellow, respectively, and the cross-linked residues on these three proteins are numbered according to the Uniprot sequences. (B) Analysis of a crude immunoprecipitate of the yeast exosome complex. Dashed blue and grey lines denote 50 compatible and 22 incompatible cross-links, respectively, according to the structure of the RNA-bound 11-subunit exosome complex (PDB code: 4IFD). Rrp44, green; Rrp40, orange; Rrp4, violet; Rrp42, gold; other exosome subunits, yellow; RNA, black. Known and candidate exosome regulators revealed by Leiker-cross-links are shown along the periphery and highlighted in green and yellow circles, respectively. (C) Connectivity maps of the ten-subunit exosome core complex based on the inter-molecular cross-links identified in the current IP-CXMS experiments or on previous yeast two-hybrid (Y2H) studies (Stark et al., 2006; Uetz et al., 2000; Oliveira et al., 2002; Luz et al., 2007; Yu et al., 2008). Blue solid lines: experimentally identified putative direct protein-protein interactions; grey dashed lines: theoretical cross-links according to the crystal structure; Cα-Cα distance cutoff ≤30 Å.DOI: http://dx.doi.org/10.7554/eLife.12509.01510.7554/eLife.12509.016Figure 4—source data 1.E. coli 70S ribosomes.DOI: http://dx.doi.org/10.7554/eLife.12509.01610.7554/eLife.12509.017Figure 4—source data 2.DOI: http://dx.doi.org/10.7554/eLife.12509.01710.7554/eLife.12509.018Figure 4—source data 3.DOI: http://dx.doi.org/10.7554/eLife.12509.01810.7554/eLife.12509.019Figure 4—source data 4.Saccharomyces cerevisiae exosome complex.DOI: http://dx.doi.org/10.7554/eLife.12509.019

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/12509/elife-12509-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** DOI: http://dx.doi.org/10.7554/eLife.12509.020

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/12509/elife-12509-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** DOI: http://dx.doi.org/10.7554/eLife.12509.021

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/12509/elife-12509-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** E. coli 70S ribosome.DOI: http://dx.doi.org/10.7554/eLife.12509.022

![Figure 4—figure supplement 4.](https://cdn.elifesciences.org/articles/12509/elife-12509-fig4-figsupp4-v2.jpg)

**Figure 4—figure supplement 4.:** A) S1, (B) L1, (C) L7/12, and (D) L31.DOI: http://dx.doi.org/10.7554/eLife.12509.023

![Figure 4—figure supplement 5.](https://cdn.elifesciences.org/articles/12509/elife-12509-fig4-figsupp5-v2.jpg)

**Figure 4—figure supplement 5.:** DOI: http://dx.doi.org/10.7554/eLife.12509.024

![Figure 4—figure supplement 6.](https://cdn.elifesciences.org/articles/12509/elife-12509-fig4-figsupp6-v2.jpg)

**Figure 4—figure supplement 6.:** After enrichment, 30% (orange) or 60% (blue) of each sample was analyzed by LC-MS/MS.DOI: http://dx.doi.org/10.7554/eLife.12509.025

Combining CXMS and immunoprecipitation (IP) has great potential for the detection of binding partners in close proximity among co-immunoprecipitated proteins; such method may be widely adopted in biology laboratories. Much progress has been made recently in this area by the use of a modified anti-GFP single-chain antibody that cannot be cross-linked so that GFP-tagged protein complexes can be cross-linked on beads and separated away from the antibody for CXMS analysis (Shi et al., 2015). For highly heterogeneous IP samples, however, cross-linked peptides can be inundated by non-cross-linked peptides even if the antibody is removed from the background. As a test, we prepared a crude immunoprecipitate of a TAP-tagged yeast exosome subunit Rrp46 (Figure 4—figure supplement 5), from which 740 proteins were identified at 0.1% protein FDR. The immunoprecipitated proteins were eluted off IgG beads and cross-linked with Leiker. To evaluate the sensitivity of the method, we varied the amount of immunoprecipitates from 40 μg to 3 μg of proteins and found that the number of inter-link identifications did not change much as the input decreased from 40 to 20 μg (Figure 4—figure supplement 6). From three experiments starting with 40 μg of proteins, a total of 195 cross-linked lysine pairs (43 inter-molecular and 152 intra-molecular) were identified (Figure 4B and Figure 4—source data 4). Thanks to cross-linking, not only did we identify all ten exosome core subunits, but also 15 putative direct protein-protein interactions amongst the core subunits, which generated a connectivity map more complete than the one from yeast two-hybrid experiments (Stark et al., 2006; Uetz et al., 2000; Oliveira et al., 2002; Luz et al., 2007; Yu et al., 2008) and showed that among the co-immunoprecipitated proteins, Rrp41 and Rrp45 directly bind to the bait protein Rrp46 (Figure 4C). Of the cross-links identified, 69% were compatible with the crystal structure of an RNA-bound 11-subunit exosome complex (Makino et al., 2013) (PDB code: 4IFD). Among the cross-links that disagreed with the RNA-bound structure, 68% involved the catalytic subunit Rrp44, which has a large rotation relative to the rest of the exosome core between the RNA-bound and the RNA-free states (Makino et al., 2013; Liu et al., 2014). The crude Rrp46 immunoprecipitate should mainly contain apo exosome, because magnesium was included in the buffer to activate the nuclease activity of exosome. Therefore, the presence (in the crystal structure) or absence (in our exosome preparation) of bound RNA is likely to be the primary reason behind most of the seemingly inconsistent inter-molecular cross-links.

To fulfill different functions in multiple biological processes (Houseley and Tollervey, 2009), the core exosome complex must recruit additional regulators, of which only a few are known. Here we found two known (Mpp6 [Milligan et al., 2008] and Ski7 Araki et al., 2001) and four potential exosome regulators through nine cross-links with core exosome subunits (Figure 4B and Figure 4—source data 4). These cross-links revealed residues in close proximity. Ski7 was found to cross-link with Rrp4 via K111, which fits well with previous co-IP results obtained by using different fragments of Ski7 (Araki et al., 2001) and a recently published CXMS study of the yeast exosome (Shi et al., 2015). Among the newly identified candidate regulators, the translation initiation factor Tif1 stood out; it had interactions with the Rrp4 and Rrp44 exosome subunits (Figure 4B). Translation has been implicated in RNA quality control (Shoemaker and Green, 2012). The linkages identified here support the hypothesis that exosome complexes ‘stand by’ the translation machinery and recognize and degrade aberrant mRNA molecules.

## Application of Leiker to lysates

We further tested Leiker for the purpose of mapping protein-protein interaction networks using

![Figure 5.](https://cdn.elifesciences.org/articles/12509/elife-12509-fig5-v2.jpg)

**Figure 5.:** E. coli and C. elegans lysates.(A) The best protein-protein interaction cluster extracted from the Leiker-identified or BS3-identified (Yang et al., 2012) inter-links from E. coli whole-cell lysates. Node size represents the degree of connectivity of the indicated protein in the network. Line width represents the spectral counts of every inter-molecular cross-link. The line color is set to blue when the two peptides of an inter-link are both attributed to unique proteins, to grey if either could be assigned to multiple proteins. All the lines connected to EF-Tu1 are grey because EF-Tu1 differs from EF-Tu2 by only one amino acid. (B) Comparison of the identified inter-links in E. coli whole-cell lysates and ribo-free lysates (5% FDR, E-value < 0.01, spectral count ≥ 3). (C and D) Comparison of the number of Leiker-identified inter-links and that of BS3-identified inter-links (Yang et al., 2012) from C. elegans (C) and E. coli (D) whole-cell lysates (5% FDR, E-value < 0.01, spectral count ≥ 1).DOI: http://dx.doi.org/10.7554/eLife.12509.02610.7554/eLife.12509.027Figure 5—source data 1.E. coli whole-cell lysates.DOI: http://dx.doi.org/10.7554/eLife.12509.02710.7554/eLife.12509.028Figure 5—source data 2.E. coli ribo-free lysates.DOI: http://dx.doi.org/10.7554/eLife.12509.02810.7554/eLife.12509.029Figure 5—source data 3.C. elegans whole-cell lysates.DOI: http://dx.doi.org/10.7554/eLife.12509.02910.7554/eLife.12509.030Figure 5—source data 4.C. elegans mitochondrial proteins.DOI: http://dx.doi.org/10.7554/eLife.12509.030

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/12509/elife-12509-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** E. coli lysates.DOI: http://dx.doi.org/10.7554/eLife.12509.031

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/12509/elife-12509-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** E. coli lysates (FDR < 0.05, E-value < 0.01, and spectral count ≥ 3).DOI: http://dx.doi.org/10.7554/eLife.12509.032

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/12509/elife-12509-fig5-figsupp3-v2.jpg)

**Figure 5—figure supplement 3.:** A) E. coli and (B) C. elegans.The labeling scheme is the same as described in Figure 5A except for the node color. For E. coli, node color is set to orange if the protein was only identified in the whole-cell lysates, to yellow only identified in the ribo-free lysates, or to green if identified in both. There are 626 proteins in the E. coli network and 155 proteins in the C. elegans network.DOI: http://dx.doi.org/10.7554/eLife.12509.033

Applying Leiker to an even more complex lysate from C. elegans, which has a similar number of protein coding genes as human (~20,000), we identified 459 inter-links (5% FDR, E-value < 0.01, spectral count ≥ 3) (Figure 5—source data 3). We also analyzed a C. elegans mitochondrial fraction and identified 547 inter-linked lysine pairs (5% FDR, E-value < 0.01, spectral count ≥ 3), of which 434 were not detected in the whole-worm lysate (Figure 5—source data 4). Together, we identified 893 non-redundant cross-linked lysine pairs from C. elegans and constructed protein-protein interactions between 155 proteins (Figure 5—figure supplement 3B).

In order to compare with previous studies, we also applied a less stringent cutoff (5% FDR, E-value < 0.01, spectral count ≥ 1) to the data sets of E. coli and C. elegans whole-cell lysates. This allowed us to determine that the number of C. elegans cross-links identified in this study was 23 times as many as the previous record (Figure 5C) (Yang et al., 2012). The number of E. coli cross-links identified in this study is four times greater than the number of PIR-identified inter-links (Chavez et al., 2013) and eight times greater than the number of BS3-identified inter-links (Yang et al., 2012). Half of the BS3-identified cross-links (Yang et al., 2012) were recapitulated in this study (Figure 5D).

## Leiker-based quantitative CXMS analysis

Relative quantification of cross-linker modified peptides can reveal changes in protein conformation and/or interactions between a protein and another molecule (e.g. nucleic acid, ligand, or protein). To apply Leiker in quantitative CXMS, we synthesized deuterium-labeled Leiker ([d

![Figure 6.](https://cdn.elifesciences.org/articles/12509/elife-12509-fig6-v2.jpg)

**Figure 6.:** For each identified cross-link spectrum, an extracted ion chromatogram (EIC) is constructed for each isotopic peak of the [d0]- and [d6]-labeled precursor. The [d6]/[d0] ratios can be calculated based on the monoisotopic peak, the most intense peak, or the least interfered peak of each isotopic cluster as specified by users. The accuracy of the ratio calculation was evaluated with the confidence score σ (range: 0–1, from the most to the least reliable). If a cross-link have ratios with σ < 0.5, the median of these ratios is assigned to this cross-link. The cross-link ratios of the proteins of interest are normalized to the median ratio of all BSA cross-links. For each cross-link, the median [state1]/[state2] ratio of three independent forward labeling experiments is plotted against the median ratio of three independent reverse labeling experiments. Cross-links that are only present in state1 or state2 due to a dramatic conformational change cannot be quantified as described above because the ratios would be zero or infinite and their σ values would be 1. Therefore, if a cross-link does not have a valid ratio after automatic quantification, the EICs were manually inspected to determine if it was an all-or-none change.DOI: http://dx.doi.org/10.7554/eLife.12509.034

![Figure 7.](https://cdn.elifesciences.org/articles/12509/elife-12509-fig7-v2.jpg)

**Figure 7.:** (A) Reciprocal labeling of RNA-free (F) and RNA-bound (B) L7Ae with [d0]/[d6]-Leiker. (B) Abundance ratios of mono-links (F/B) in the forward (F[d0]/B[d6]) and the reverse labeling experiment (F[d6]/B[d0]). Each circle represents a mono-linked lysine residue and is colored red if it has a ratio greater than five in both labeling schemes. (C) The three lysine residues affected by RNA binding are highlighted in the structure model (PDB code: 2HVY). The number below each such lysine residue indicates the buried surface area (Å2) upon RNA binding. (D) Extracted ion chromatograms (left) and representative MS1 spectra (right) of a K42 mono-link.DOI: http://dx.doi.org/10.7554/eLife.12509.03510.7554/eLife.12509.036Figure 7—source data 1.DOI: http://dx.doi.org/10.7554/eLife.12509.036

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/12509/elife-12509-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** A) K35 and (B) K84.DOI: http://dx.doi.org/10.7554/eLife.12509.037

Mono-linked peptides are usually neglected in CXMS, but they are valuable because they indicate that the modified lysine residues are exposed to solvent. Mono-links at all 15 lysine residues and the N-terminus of L7Ae were reliably quantified (Figure 6) in both forward and reverse labeling experiments. Three mono-links at K35, K42, and K84 consistently had significantly higher abundance (>5 fold) in the RNA-free state (F) than in the RNA-bound state (B) (Figure 7B–D, Figure 7—figure supplement 1 and Figure 7—source data 1). None of inter-links passed the quantification criteria described above. These results suggest that the three lysine residues are buried upon RNA binding, either due to direct protein-RNA binding or indirect protein conformational changes induced by RNA binding. This is in perfect agreement with the crystal structure (Li and Ye, 2006) (PDB code: 2HVY), which shows that K35, K42, and K84 all bind to the RNA, each with a buried area greater than 20 Å2 (Figure 7C).

Lastly, we applied quantitative CXMS to

![Figure 8.](https://cdn.elifesciences.org/articles/12509/elife-12509-fig8-v2.jpg)

**Figure 8.:** E. coli lysates.Abundance ratios of (A) inter-linked lysine pairs and (B) mono-linked sites in the forward ([log phase]d0/[stationary phase]d6) and the reverse labeling experiment ([log phase]d6/[stationary phase]d0).DOI: http://dx.doi.org/10.7554/eLife.12509.03810.7554/eLife.12509.039Figure 8—source data 1.E. coli lysates.DOI: http://dx.doi.org/10.7554/eLife.12509.039

## Discussion

In this study, we developed an MS-friendly and isotope-encodable cross-linker called Leiker that enables the efficient enrichment of cross-linked peptides through biotin-based immobilization and azobenzene-based chemical cleavage. With an enrichment efficiency of 97% or more, Leiker yields a fourfold increase in the number of identified cross-linked peptide pairs from complex samples. Also established is a workflow for quantitative CXMS based on deuterium-labeled Leiker.

In theory, a comprehensive network of putative direct protein-protein interactions could be obtained by applying Leiker to lysates. However, the interaction networks obtained as such are limited, because the cross-links identified are dominated by those from highly abundant proteins, for example, EF-Tu and ribosomal proteins in E. coli. This can be overcome with subcellular fractionation, which can separate abundant proteins from less abundant ones. We increased the number of unique inter-link identifications by more than 50% (from 2003 to 3130) by simply removing ribosomes from the E. coli lysates (Figure 5B). This is also obvious by contrasting the CXMS results of the whole-worm lysate and the mitochondrial fraction of C. elegans, from which 459 and 547 inter-linked lysine pairs were detected, respectively, with an overlap of only 113. We anticipate that extensive protein fractionation coupled with Leiker-assisted CXMS will pave the way towards constructing comprehensive interactomes for different model organisms, and next-generation cross-link identification software of higher sensitivity will also help. Further, with the advantage of heavy isotope labeling for quantification in addition to the enrichment function, Leiker shows promise for use in differential interactome analysis (Ideker and Krogan, 2012).

When we examined the cross-links identified from E. coli against the protein structures deposited in the PDB database, we noted that the intra-molecular cross-links in both the whole-cell lysates and the ribo-free samples had similar rates of structural compatibility (80% and 84%, respectively). This shows that the quality of our Leiker-based CXMS data is high. Interestingly, the inter-molecular cross-links detected from the ribo-free samples had a much higher rate of structural compatibility (69%) than those detected in the whole-cell lysates (12%). Given that 92% of the inter-links with existing structural information in the whole-cell lysate involved at least one ribosomal protein and many were between ribosomal proteins, we think that most of the apparently incompatible inter-molecular cross-links seen in the whole-cell lysates likely result from cross-linking of adjacent ribosomal particles.

Previous cross-linking studies have typically treated mono-linked peptides as by-products, and have ignored them. This is regrettable, as they carry structural information about proteins and always outnumber inter-links (Figure 3). Leiker also generates abundant mono-links. In this study, we demonstrate that mono-links are highly valuable in mapping RNA-binding lysine residues. As the positively charged lysine residue is frequently involved in binding the negatively charged phosphate backbone of DNA and RNA, relative quantification of lysine mono-links would be particularly suited for mapping the DNA or RNA binding surface on a protein. We suggest that mono-link data should be used in routine practice.

## Materials and methods

## Materials

Acetonitrile, methanol, formic acid, ammonium bicarbonate, and acetone were purchased from J.T. Baker (Center Valley, PA). Dimethylsulfoxide (DMSO), HEPES, urea, thiourea, and other general chemicals were purchased from Sigma-Aldrich (St. Louis, MO). Trypsin and Lys-C were purchased from Promega (Wisconsin, WI). Bis(sulfosuccinimidyl) suberate (BS3), streptavidin agarose resin, and high capacity streptavidin agarose resin were purchased from Pierce (Rockford, IL). Dynabeads M-280 streptavidin was purchased from Invitrogen (Carlsbad, CA).

## Preparation of protein samples

RNase A, lysozyme, aldolase, BSA, lactoferrin, β-galactosidase, and myosin were obtained from Sigma-Aldrich. Recombinant GST containing an N-terminal His tag was expressed in E. coli BL21 cells from the pDYH24 plasmid and purified with glutathione sepharose (GE Healthcare, Piscataway, NJ). PUD-1/PUD-2 heterodimers were purified on a HisTrap column followed by gel filtration. Stock solutions of the ten standard proteins were individually buffer exchanged into 20 mM HEPES, pH8.0 by ultrafiltration, and then mixed to make a total protein mixture with a 2 µg/µl protein concentration.

Purification of 70S ribosomes from E. coli cells was performed as previously described (Guo et al., 2011). E. coli cells (DH5α) were grown in 2 L LB medium to an OD600=0.8. Cells were collected by centrifugation, washed with 100 mL lysis buffer (50 mM HEPES-KOH, pH 7.5, 500 mM KCl, 12 mM MgCl2, 1 mM DTT, 1 mM PMSF) and resuspended in 100 mL of lysis buffer. Cells were then disrupted with an Ultrasonic Cell Disruptor. The lysate was clarified at 13,000 rpm for 1 hr at 4°C in a JA 25.50 motor (Beckman Coulter, UK). The supernatant was layered on a sucrose cushion (50 mM HEPES-KOH, pH 7.5, 500 mM KCl, 12 mM MgCl2, 33% sucrose) and centrifuged at 30,000 rpm for 18 hr in a 70Ti rotor (Beckman Coulter) at 4°C. The supernatant was collected as the ribo-free lysate. The pellet was resolved with a buffer containing 50 mM HEPES-KOH, pH 7.5, 500 mM KCl, and 12 mM MgCl2. The crude ribosomes were then layered on a 10–50% sucrose gradient (50 mM HEPES-KOH, pH 7.5, 500 mM KCl, 12 mM MgCl2, 10% to 50% sucrose) and centrifuged at 28,000 rpm for 5 hr in an SW28 rotor (Beckman Coulter) at 4°C. The gradient was scanned at 260 nm and fractionated in an ISCO gradient collector. The fractions of 70S ribosomes were pooled and concentrated with Amicon Ultra centrifugation filters (Millipore, China) with a buffer containing 50 mM HEPES-KOH, pH 7.5, 500 mM KCl, and 12 mM MgCl2.

The yeast exosome complex was immunoprecipitated with IgG beads as described previously (Liu et al., 2014), with the following modifications: a gentle wash buffer (150 mM NaCl) was applied and the mono-Q anion exchange step was not performed. These modifications were made in order to maintain the interaction of the proteins in the sample. Eluted proteins were exchanged into 20 mM HEPES, pH 8.0, 150 mM NaCl.

E. coli OP50 lysates and C. elegans N2 lysates were prepared following a protocol from Bing et al. (Yang et al., 2012; Zhao et al., 2015). Mitochondria were isolated from the wild-type N2 worms as described previously (Shen et al., 2014) and lysed by incubation in 100 mM HEPES pH 8.0, 1% NP-40, 10 mM CaCl2 at 4°C for 30 min.

The Pyrococcus furiosus L7Ae and the H/ACA RNA were prepared as described previously (Li and Ye, 2006). The buffer was exchanged to 50 mM HEPES, pH 7.6, 1 M NaCl.

E. coli (MG1665) cells were grown at 37°C in 500 mL M9 minimal medium from a 1 mL overnight culture. Log phase cells were harvested after 11 hr at OD600 0.7; stationary phase cells were harvested after 26 hr at OD600 2.3. Cell lysates were prepared in 50 mM HEPES pH 8.0, 150 mM NaCl using a FastPrep system (MP Biomedicals, Santa Ana, CA) using two volumes of glass beads at 6.5 m/s, 20 s per pulse for four pulses, with 5 min of cooling on ice between pulses. The lysates were cleared by centrifugation at top speed in a tabletop microfuge for 30 min. Protein concentrations were determined using the bicinchoninic acid assay.

## Trypsin digestion

At room temperate (RT), protein pellets were dissolved (assisted by sonication) in 8 M urea, 20 mM methylamine (to reduce carbamylation), 100 mM Tris, pH 8.5, reduced with 5 mM TCEP for 20 min and alkylated with 10 mM iodoacetamide for 15 min in the dark. Then, the samples were diluted with 3 volumes of 100 mM Tris, pH 8.5 and digested with trypsin at 1/50 (w/w) enzyme/substrate ratio at 37°C for 16–18 hr.

## CXMS analysis of model proteins

The optimal protein-to-cross-linker mass ratio was determined by a titration experiment. 1 µl of cross-linker at increasing concentrations (2.5 µg/µl, 5 µg/µl, 10 µg/µl, 20 µg/µl, 40 µg/µl) in DMSO was incubated with 20 µl of 2 µg/µl of the ten-protein mixture at RT for 1 hr to make 16:1, 8:1, 4:1, 2:1, and 1:1 protein-to-cross-linker mass ratios, respectively. The reactions were quenched with 20 mM NH4HCO3 at RT for 20 min. Cross-linking products were analyzed by SDS-PAGE. The 4:1 ratio was ultimately chosen for both the one-piece and the two-piece Leiker. Higher dosages were avoided to minimize excessive cross-linking.

For comparison of the one-piece and two-piece Leikers, 50 µl of the 2 µg/µl ten-protein mixture was incubated with 0.5 µl of 50 µg/µl AL or bAL1 at RT for 1 hr. The reactions were quenched as described above. For AL, the solution was mixed with 350 µl of 8 M urea, 100 mM Tris, pH 8.5, and filtered with an Amicon Ultra-0.5 10-kD filter device (Millipore). Excess cross-linker molecules were removed by two additional washes with urea. Click chemistry was subsequently performed on the membrane. In a 100 µl reaction, 28 nmol of azide-biotin was added (an amount equal to the starting amount of the alkyne group of AL), followed by the addition of 2 mM CuSO4, 2 mM TCEP, and 200 µM TBTA. Samples were gently rotated and incubated at RT for 2 hr. The excess free azide-biotin was then removed by washes with urea in the filter device. Finally, the proteins were collected by centrifugation with the filter device placed upside down inside the tube. Recovered proteins were transferred to a new 1.5 mL tube, precipitated at -20°C with four volumes of pre-cooled acetone for at least 30 min, and digested with trypsin. The bAL1 samples were processed in the same way except that the reaction mixture was precipitated directly without going through the 10-kD filter device.

The AL- and bAL1-cross-linked peptides were enriched in parallel. The tryptic digests, without formic acid (FA) acidification, were directly mixed with an equal volume of 20 mM HEPES, pH 8.0 and incubated with 40 µl pre-washed high capacity streptavidin agarose for 2 hr. Then, the beads were washed three times with 20 mM HEPES, pH 8.0, 1 M KCl, once with H2O, three times with 10% acetonitrile (ACN), and another three times with H2O, each time with 1 mL buffer or H2O, with 5-min rotation. Supernatants were removed carefully with a 1 mL syringe needle connected to a vacuum pump. Loss of beads was avoided by keeping the beveled surface of the needle tip in contact with the wall of the tube. After the extensive washes, the peptides were released by incubating the beads with 5× bed volumes of cleavage buffer (300 mM Na2S2O4 in 6 M urea, 2 M thiourea, 10 mM HEPES, pH8.2) (Yang et al., 2010) at 37°C for 30 min, with end-to-end rotation. Recovered peptides were acidified with 5% FA and subsequently desalted on home-made C18 desalting columns, followed by elution with 70% ACN/0.1% FA. Eluates were vacuum dried and reconstituted in 0.1% FA for mass spectrometry analyses. The color of the beads could be used to monitor the entire enrichment process: a bright yellow color indicated the binding of Leiker-linked peptides; a return to a white color occurred when the cleavage reaction was successful.

Comparison of bAL1 and bAL2 was carried out in two samples. For the first comparison, 50 µg of the ten-protein mixture was cross-linked with bAL1 or bAL2 at 4:1 protein-to-cross-linker mass ratio and then digested with trypsin. After mixing with the tryptic digest of an E. coli lysate containing 500 µg of total proteins, the digested Leiker-linked peptides were affinity purified with 20 µl of high-capacity streptavidin agarose. For the second comparison, 30 µg of ribosome was treated with bAL1 or bAL2 at 8:1, 4:1, or 2:1 protein-to-cross-linker mass ratios, digested, and enriched using 20 µl of high-capacity streptavidin agarose.

For the serial dilution experiment (Figure 3), 200 µg of the ten-protein mixture was treated with 50 µg of bAL1 at RT for 1 hr. After quenching, the proteins were precipitated and digested with trypsin. Four equal aliquots of this digest were either not diluted to serve as a control (1:0) or diluted with the tryptic digest of a non-cross-linked E. coli lysate at 1:1, 1:10, or 1:100 (w/w) ratio. Each mixture was enriched with 200 µl of pre-washed streptavidin agarose.

## CXMS analysis of purified ribosomes and the immunoprecipitated exosome complex

30 µg of ribosome was treated with bAL2 at 8:1, 4:1, or 2:1 protein-to-cross-linker mass ratios. 40 µl of the exosome complex sample (1 µg/µl) was incubated with 0.25 µl of 40 µg/µl bAL2 at RT for 1 hr. 20 µl of high-capacity streptavidin agarose was used to enrich Leiker-linked peptides in each sample.

## Negative staining of E. coli 70S ribosome

70S ribosomes were negatively stained with 0.2% uranyl acetate. Carbon coated grids were first glow-discharged to increase the surface hydrophilicity using a Harrick Plasma cleaner. 4 µL aliquots of 70S ribosomes (~10 nM) were placed on grids for about 1 min, and excessive liquid was absorbed by filter paper. After that 0.2% uranyl acetate was applied on the grid for about 1 min and absorbed using filter paper. The grids were air-dried and examined using an FEI Tecnai Spirit BioTwin microscope (FEI, Hillsboro, OR) (120 KV) at 49,000× magnification.

## CXMS analysis of E. coli and C. elegans cell lysates

E. coli or C. elegans lysates prepared as described previously (Yang et al., 2012; Zhao et al., 2015) (1 mg of total proteins) were treated with 250 µg bAL1 at RT for 1 hr, in 300 µl reactions; NH4HCO3 was added to quench the reactions. Proteins were precipitated and digested with trypsin. After centrifugation in a bench top centrifuge at top speed for 30 min and filtering with a 50-kD cutoff filter, the digested peptides were brought to a volume of 3 mL with 2% ACN, 20 mM HEPES, pH 8.2; the pH was adjusted to 10.0 with ammonia prior to high-pH reverse phase separation on an Xtimate column (10×250 mm) packed with 5 μm C18 resin (Welch Materials, China) at a flow rate of 2 mL/min. A 70 min gradient was applied as follows: 0-6% B in 10 min, 6-40% B in 40 min, 40-100% B in 10 min, 100% B for 10 min (A = 4% ACN, 5 mM NH4COOH, pH 10, B = 80% ACN, 5 mM NH4COOH, pH 10). A total of 39 two-min fractions were collected, and then combined into 9–11 fractions of similar shades of color judging by naked eyes. These pooled samples were evaporated to 200–300 µl volumes before Leiker-linked peptides were enriched with 50 µl of high-capacity streptavidin beads from each sample. For the ribo-free lysates, 3 mg of proteins were cross-linked with 0.75 mg bAL2 at RT for 1 hr, and subjected to tryptic digestion and fractionation as described above.

C. elegans mitochondria were prepared as described previously (Shen et al., 2014), and the CXMS analysis was performed as described above except with two differences: 3.2 mg of total proteins was used as the starting material and the collected fractions were pooled into 5 fractions.

## Quantitative CXMS analysis of the L7Ae-RNA complex

In the forward and reverse labeling experiments, 0.7 nmol of RNA-free L7Ae was treated with [d0]-bAL2 and [d6]-bAL2, respectively; an equal amount of L7Ae was pre-incubated with 1 nmol of the 65 nt H/ACA RNA at 4°C for 30 min and then treated with [d6]-bAL2 and [d0]-bAL2, respectively. An equal amount of BSA was spiked into each cross-linking reaction. A 4:1 protein-to-cross-linker ratio (w/w) was used for each reaction. The cross-linking reactions were quenched with ammonium bicarbonate after 1 hr at RT. The paired [d0]- and [d6]-bAL2 samples were combined and subjected to acetone precipitation and trypsin digestion.

## Quantitative CXMS analysis of E. coli lysates

In the forward labeling experiment, the log phase and the stationary phase cell lysates (100 µg proteins each) were cross-linked with 50 µg of [d0]-bAL2 and 50 µg of [d6]-bAL2, respectively, with 1 µg of BSA spiked into each sample. After 1 hr at RT, the two reactions were quenched, mixed, precipitated with acetone, and digested with trypsin. The reverse labeling experiment was conducted in the same way except that the log phase lysate was cross-linked with [d6]-bAL2 and the stationary phase lysate was cross-linked with [d0]-bAL2.

## LC-MS/MS analysis

All protein samples were analyzed with an EASY-nLC 1000 system (Thermo Fisher Scientific, Waltham, MA) interfaced with a Q-Exactive mass spectrometer (Thermo Fisher Scientific). A two-column setup was used, consisting of a pre-column (100 μm×4 cm, 3 μm C18) with a frit at each end and an analytical column (75 μm×10 cm, 1.8 μm C18) with a 5 µm tip. For the Leiker-cross-linked samples after enrichment, typically one third of a reconstituted sample was injected and separated with a 65 min linear gradient at a flow rate of 300 nl/min as follows: 0–5% B in 2 min, 5–28% B in 41 min, 28–80% in 10 min, 80% for 12 min (A = 0.1% FA, B = 100% ACN, 0.1% FA). Slight modifications to the separation method were made for different samples. A 120 min gradient was used with a more gradual ramp to 28% buffer B. The Q-Exactive mass spectrometer was operated in data-dependent mode with one full MS scan at R = 70000 (m/z = 200), followed by ten HCD MS/MS scans at R = 17,500 (m/z = 200), NCE = 27, with an isolation width of 2 m/z. The AGC targets for the MS1 and MS2 scans were 3e6 and 1e5, respectively, and the maximum injection times for MS1 and MS2 were both 60 ms. For cross-linked samples, precursors of the +1, +2, +7 or above, or unassigned charge states were rejected; exclusion of isotopes was disabled; dynamic exclusion was set to 30 s.

For accurate mass analysis, 20 µg/ml of [d0]-bAL2 or [d6]-bAL2 in methanol was sprayed directly into a LTQ Orbitrap XL mass spectrometer (Thermo Fisher Scientific) operated in the negative mode with a spray voltage of 0.8 kV and a scan mass range of 150–1000 m/z.

## Identification of cross-linked peptides with pLink

The Xcalibur raw data was converted to ms2 files using RawExtract (McDonald et al., 2004). Cross-linked peptides were identified using pLink software as described previously (Yang et al., 2012), with the following modifications Cross-linker was set to AL, bAL1, bAL2, [d6]-bAL2, or BS3; The minimum peptide length was 5 amino acids for lysate samples; oxidation on Met was set as a variable modification.

For the ten-protein mixture and ribosome complexes, the search databases consisted of the sequences of all of the proteins in question. The sequences were downloaded from NCBI or Uniprot.

Prior to the CXMS analysis of the exosome complex, LC-MS/MS analyses of digested, uncross-linked samples were carried out to identify the proteins present in the samples. For protein identification, the precursors of +1 or unassigned charge states were rejected; MS2 spectra were searched against a S. cerevisiae protein database (downloaded from Uniprot on 2013-04-03) using ProLuCID2 (Xu et al., 2006) and filtered using DTASelect 2.0 (Tabb et al., 2002) with a spectral false identification rate ≤1% and a minimum of two identified peptides for each protein. A restricted database containing only the identified proteins (740 in total) was generated using Contrast 2.0 (Tabb et al., 2002). MS2 spectra from the cross-linked samples were then searched against this small database using pLink.

For the CXMS analysis of E. coli whole-cell lysates and ribo-free lysates, the sequences of the entire proteome of the K12 strain were downloaded from Uniprot on 2014-07-31 and used for searching.

For the CXMS analysis of C. elegans lysates, a database consisting of proteins identified from N2 C. elegans lysates generated with ProLuCID2 was used for searching (unpublished).

For the CXMS analysis of C. elegans mitochondrial proteins, a restricted database was constructed in a similar way as for the exosome complex.

## Quantification of cross-linked peptides with pQuant

pQuant (Liu et al., 2014) was used to determine the heavy-to-light ratio (H/L) of each cross-link. The regression model Y = aX +e is used to calculate peptide ratios. The optimal value of a is solved using the least-squares method as a^=∑​XjYj/∑​XjXj, and the estimated standard error of a^ is σ^=(K−1∙∑​(Yj−a^Xj)2/∑​Xj2)1/2. is then normalized to the interval of [0,1], and is named confidence score. If the value of σ^ is zero (the highest confidence), there is no interference signal; if the value is one (the lowest confidence), the peptide signals are inundated by interference signals. For each identified cross-link spectrum, an extracted ion chromatogram (EIC) was constructed for each isotopic peak of the light- and heavy-labeled precursor. The H/L ratios can be calculated based on the monoisotopic peak, the most intense peak, or the least interfered peak of each isotopic cluster as specified by users. For L7Ae, all options yielded similar results and we selected the monoisotopic peak. For the highly complex samples of the log phase versus stationary phase E. coli, the option of the least interfered peak performed the best. For each cross-link, every identified spectrum (E-value < 0.001) will lead to a H/L ratio and a confidence score σ, because pQuant conducts the quantitation independently starting from each identified MS/MS spectrum. In most cases, the H/L ratios obtained for the same precursor ion are close, but sometimes the ratios may differ due to multiple reasons including local interference signals or a sudden decrease followed by recovery in signal intensity in the chromatograms, all of which can affect the calling of the start and the end of a chromatogram peak. Ratios with σ values above or equal to 0.5 were discarded. The median H/L ratio obtained from the remaining spectra was assigned to a cross-linked lysine pair or a mono-linked lysine residue as the final quantification value. If a cross-link had no assigned ratio value (i.e., none of its ratios had a σ value less than 0.5), we manually evaluated the reconstructed ion chromatograms to assess abundance changes. All the ratios were normalized against the median value of all the H/L ratios belonging to the spiked-in BSA.
