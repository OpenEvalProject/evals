# A high-throughput yeast display approach to profile pathogen proteomes for MHC-II binding

## Authors

- Brooke D Huisman<sup>1</sup> ([ORCID: 0000-0002-6229-6498](https://orcid.org/0000-0002-6229-6498))
- Zheng Dai<sup>3</sup>
- David K Gifford<sup>2</sup>
- Michael E Birnbaum<sup>1</sup> ([ORCID: 0000-0002-2281-3518](https://orcid.org/0000-0002-2281-3518)) †

### Affiliations

1. Koch Institute for Integrative Cancer Research Cambridge United States
2. Department of Biological Engineering, Massachusetts Institute of Technology Cambridge United States ([ROR:042nb2s44](https://ror.org/042nb2s44))
3. Computer Science and Artificial Intelligence Laboratory, Massachusetts Institute of Technology Cambridge United States ([ROR:042nb2s44](https://ror.org/042nb2s44))
4. Department of Electrical Engineering and Computer Science, Massachusetts Institute of Technology Cambridge United States ([ROR:042nb2s44](https://ror.org/042nb2s44))
5. Ragon Institute of MGH, MIT and Harvard Cambridge United States

† Corresponding author

## Abstract

T cells play a critical role in the adaptive immune response, recognizing peptide antigens presented on the cell surface by major histocompatibility complex (MHC) proteins. While assessing peptides for MHC binding is an important component of probing these interactions, traditional assays for testing peptides of interest for MHC binding are limited in throughput. Here, we present a yeast display-based platform for assessing the binding of tens of thousands of user-defined peptides in a high-throughput manner. We apply this approach to assess a tiled library covering the SARS-CoV-2 proteome and four dengue virus serotypes for binding to human class II MHCs, including HLA-DR401, -DR402, and -DR404. While the peptide datasets show broad agreement with previously described MHC-binding motifs, they additionally reveal experimentally validated computational false positives and false negatives. We therefore present this approach as able to complement current experimental datasets and computational predictions. Further, our yeast display approach underlines design considerations for epitope identification experiments and serves as a framework for examining relationships between viral conservation and MHC binding, which can be used to identify potentially high-interest peptide binders from viral proteins. These results demonstrate the utility of our approach to determine peptide-MHC binding interactions in a manner that can supplement and potentially enhance current algorithm-based approaches.

## Introduction

Major histocompatibility complex (MHC) proteins play a critical role in adaptive immunity by presenting peptide fragments on the surface of cells. Peptide-MHCs (pMHCs) are then surveilled by T cells via their T cell receptors (TCRs), enabling immune cells to sense dysfunction, such as the presence of pathogen-derived peptides (Chaplin, 2010; Hennecke and Wiley, 2001). Class II MHC molecules (MHC-II) are expressed primarily on professional antigen-presenting cells, and are recognized by antigen-specific CD4+ T cells that drive the coordination of innate and adaptive immune responses (Chaplin, 2010; Swain et al., 2012). MHC-II molecules have an open peptide-binding groove, allowing for display of long peptides, consisting of a nine amino acid ‘core’ flanked by a variable number of additional residues on each side (Jones et al., 2006).

Generating reliable and rapid data on peptide-MHC binding is beneficial for understanding the underlying biology of adaptive immunity and for clinical applications, including for optimized T cell epitopes in vaccine design (Dai et al., 2021; Keskin et al., 2019; Liu et al., 2020; Liu et al., 2021b; Moise et al., 2015; Ott et al., 2017; Patronov and Doytchinova, 2013; Rosati et al., 2021). In fact, therapeutics to generate antigen-specific T cell responses have shown great promise in cancer (Keskin et al., 2019; Ott et al., 2017) and infectious disease (Gambino et al., 2021). Since understanding peptide-MHC binding is critical for identifying and engineering T cell epitopes, there have been sustained efforts to produce high-quality experimental data and predictive algorithms.

Initial experimental methods for determining peptide binding to MHC relied upon the analysis of synthesized candidate peptides via MHC stability or functional assays, and can produce high-confidence data, but can be difficult to scale beyond a small number of candidate peptides (Altmann and Boyton, 2020; Justesen et al., 2009; Mateus et al., 2020; Sidney et al., 2010; Yin and Stern, 2014). More recently, mass spectrometry-based approaches have been demonstrated for determining the MHC-presented peptide repertoire of cells. These approaches include monoallelic mass spectrometry, which allows for the unambiguous assignment of presented peptides to a given MHC allele. However, mass spectrometry-based approaches are not necessarily quantitative measures of presented peptide affinity or abundance, although there have been advances in quantitation using internal standards (Stopfer et al., 2021; Stopfer et al., 2020). Additionally, the peptides endogenously expressed by a cell can crowd out exogenously examined peptides of interest, and mass spectrometry approaches typically require large numbers of input cells (Abelin et al., 2019; Abelin et al., 2017; Parker et al., 2021; Purcell et al., 2019).

A wave of higher throughput approaches have been recently developed for studying peptide-MHC interactions, including yeast display (Jiang and Boder, 2010; Liu et al., 2021a; Rappazzo et al., 2020; Wen et al., 2008) and mammalian display-based methods (Obermair et al., 2022). Many of these assays rely upon construction of DNA-based libraries (Jiang and Boder, 2010; Obermair et al., 2022; Rappazzo et al., 2020; Wen et al., 2008), although approaches using chemically synthesized peptides have also recently been described (Liu et al., 2021a; Smith et al., 2019). DNA libraries have been generated either via DNA oligonucleotide synthesis (Jiang and Boder, 2010; Obermair et al., 2022; Rappazzo et al., 2020) or random fragmentation and insertion of viral genomic material (Wen et al., 2008). Upon assembly of the peptide libraries, peptide stabilization and surface expression (Jiang and Boder, 2010; Obermair et al., 2022; Wen et al., 2008) or peptide dissociation (Rappazzo et al., 2020) were used to assess peptide-MHC binding.

In addition to experimental advances, computational approaches for peptide-MHC binding prediction have advanced markedly over the past decade. These developments are due to algorithmic advances (O’Donnell et al., 2020; Racle et al., 2019; Reynisson et al., 2020; Zeng and Gifford, 2019) and the availability of large, high-quality training data (Abelin et al., 2019; Abelin et al., 2017; Rappazzo et al., 2020; Reynisson et al., 2020). However, despite the improvements in predicting peptide binding to MHC in a broad sense, the predictive power for individual peptides often remains imperfect relative to experimental measurements (Rappazzo et al., 2020; Zhao and Sher, 2018).

Here, we present a yeast display approach to directly assess peptide-MHC binding for large collections of defined peptide antigens to screen whole viral proteomes for MHC-II binding in high throughput. We utilize this approach to screen the full proteome of SARS-CoV-2, a present, global threat to public health, and identify and experimentally validate SARS-CoV-2-derived MHC binders, including both algorithmically predicted and algorithmically missed peptide binders, highlighting the potential of this approach to supplement or augment prediction algorithms. We additionally apply this approach to screen proteomes from serotypes 1–4 of dengue viruses, in which antibody-dependent enhancement results in more severe disease upon second infection with a different dengue virus serotype (Guzman et al., 2016), and thus represents a potential important application area for T cell-directed therapeutics. Our approach enables exploration of peptide binding to MHCs in the context of serotype-specific mutations, identifying homologous, pan-serotype regions of interest that are capable of MHC binding and thus may represent desirable targets for immune interventions.

## Results

### Generation of yeast display libraries for profiling the SARS-CoV-2 proteome

Previous studies have reported the use of yeast-displayed MHC-II for characterizing peptide-MHC and pMHC-TCR interactions (Rappazzo et al., 2020; Birnbaum et al., 2014; Rappazzo et al., 2020, Fernandes et al., 2020). We adapted MHC-II yeast display constructs (Rappazzo et al., 2020) to generate a defined library of peptides that cover the SARS-CoV-2 proteome to assess them for MHC binding. To compare SARS-CoV-2 with a related coronavirus, we also included peptides from the spike and nucleocapsid proteins from SARS-CoV.

Each protein was windowed into peptides of 15 amino acids in length, with a step size of 1 to cover every possible 15mer peptide in the protein (Figure 1a). Each peptide was encoded in DNA and cloned in a pooled format into yeast vectors containing MHC-II proteins. The generated library was linked to three MHC-II alleles: HLA-DR401 (HLA-DRA1*01:01, HLA-DRB1*04:01), HLA-DR402 (HLA-DRA1*01:01, HLA-DRB1*04:02), and HLA-DR404 (HLA-DRA1*01:01, HLA-DRB1*04:04). Yeast were formatted with a flexible linker connecting the peptide and MHC, containing a 3C protease site and a Myc epitope tag, which can be used for selections (Figure 1a; Rappazzo et al., 2020). The final library contained 11,040 unique peptides, with 99% of the designed peptides present in each cloned yeast library, as assessed by next-generation sequencing.

![Figure 1.](https://cdn.elifesciences.org/articles/78589/elife-78589-fig1-v2.jpg)

**Figure 1.:** (a) The defined library contains pathogen proteome peptides (length 15, sliding window 1). Poor binding peptides are displaced with addition of protease, competitor peptide, and HLA-DM. (b) Schematic of doped and undoped libraries: in the doped selection strategy, the library is added to a library of null, non-expressing constructs. (c) Representative flow plots showing enrichment of MHC-expressing yeast over rounds of selection for the library containing SARS-CoV-2 and SARS-CoV peptides on HLA-DR401.

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/78589/elife-78589-fig1-figsupp1-v2.jpg)

**Figure 1—figure supplement 1.:** Pearson correlation for HLA-DR401 SARS-CoV-2 and SARS-CoV defined library members (+/- signs indicate enriched (+) or not enriched (-) yeast in undoped library; rounds of selection are indicated, e.g. ‘R1’ indicates ‘Round 1’ and ‘R0’ is the unselected ‘Round 0’ library).

### Strategies for selecting defined libraries

To enrich for peptide binders, iterative selections were performed (Figure 1a): the library is first incubated with competitor peptide and 3C protease, which cleaves the covalent linkage between peptide and MHC, followed by the addition of HLA-DM at lower pH. These conditions allow for the encoded peptide to be displaced from the peptide-binding groove. The Myc epitope tag is proximal to the peptide, which can be identified via incubation with an anti-epitope tag antibody followed by enrichment via magnetic bead selection if the yeast-expressed peptide remains bound to the MHC after the peptide exchange reaction.

Three rounds of selection were iteratively performed. Representative enrichment of yeast expressing Myc-tagged peptides can be seen in Figure 1c (‘undoped library’), for the library displayed by HLA-DR401. Here, the pre-selection Myc-positive population starts at 29.3% and quickly converges, with 65.0% positive in the pre-selection Round 2 population and 74.1% in the pre-selection Round 3 population.

Given the rapid convergence of the library, we performed a second set of selections in which we doped the defined library into a randomized, null library to enable a greater degree of enrichment as compared to non-binding peptides. The null library was generated by fully randomizing 10 amino acids in the peptide region of the peptide-MHC-II construct while fixing three amino acids to encode stop codons. This library provides a baseline population of yeast which should not express pMHC, and therefore not enrich in our selections. We doped our defined peptide library into a 500-fold excess of null library, such that each peptide member was represented at approximately the same frequency (Figure 1b). The null library provides baseline competition, which true binders must enrich beyond, and increases the stringency of the enrichment task.

We performed four rounds of selection on the doped library. Because of the excess of null yeast, the initial pre-selection stain is low (1.6%) compared to the initial undoped library (Figure 1c). This staining enriched over the first three rounds of selection, reflective of the stringency of the task and clarity of enrichment. This is in contrast to the initial undoped library, which began with a much higher pre-selection stain, with a lower fold change in staining over rounds of selection. The low frequency of each member in the starting doped library, however, increases the likelihood of stochastic dropout for any given member.

### Analysis of selection data

After selections, peptide identities were determined through deep sequencing of enriched yeast populations, providing us with a dataset comprised of positive enrichment over four rounds of selection from the doped library and both positive and negative enrichment for three rounds of selection from the undoped library (Supplementary file 1a). Figure 1—figure supplement 1 shows the correlation between defined library members on HLA-DR401. As expected, the unselected library correlated poorly with post-selection rounds. Consistent with the observed staining (Figure 1c), the doped library essentially converged after Round 3. Similarly, the undoped library appears converged following Round 2.

Next, we established metrics for enrichment for each mode of selection. Given the high starting frequency of members in the undoped library, we classify enrichment based on fold change between Round 1 and Round 2, and we define criteria for enriched yeast in the undoped library as making up a higher fraction of reads following Round 2 compared to Round 1. In contrast, in the doped library, members start at low frequencies, and we define enrichment based on presence above a threshold in Round 3 of selection, specifically as having greater than or equal to 10 reads following Round 3. Figure 2b illustrates the correspondence between enrichment metrics in the doped and undoped library for the library on HLA-DR401. Of the 11,040 peptides in the library, 2467 enriched in both the doped and undoped libraries displayed by HLA-DR401 (Figure 2a). An additional 1252 enriched in the doped library only and 797 enriched in the undoped library only.

![Figure 2.](https://cdn.elifesciences.org/articles/78589/elife-78589-fig2-v2.jpg)

**Figure 2.:** (a) Overview of filtering peptides and correspondence between selection strategies for SARS-CoV and SARS-CoV-2 library on HLA-DR401. Peptides are filtered for enrichment in both doped and undoped libraries. Further, the relationship between these peptides and peptides which contain a 9mer that is enriched in five or more of the seven peptides containing it is shown. (b) Relationships between enrichment in doped and undoped libraries. Absolute counts following Round 3 of selection of the doped library are plotted against the log2 fold change between read fraction for peptides in Round 2 and Round 1. Data are shown for the library on HLA-DR401. (c) Sequence logo of 2467 peptides that enriched in both doped and undoped selected libraries for HLA-DR401. Registers are inferred with a position weight matrix-based alignment method. Logos were generated with Seq2Logo-2.0.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/78589/elife-78589-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** (a) Schematic showing use of overlapping 15mers, containing redundant 9mers. Each 9mer is present in seven 15mers; for each 9mer, we calculate how many of these seven 15mers enriched. (b) Number of peptides containing a given 9mer that are hits, for SARS-CoV-2 nucleocapsid on HLA-DR401. Black = hits in both undoped and doped libraries; blue = hits in undoped library only; red = hits in doped library only. Enrichment categories are stacked, for a maximum of seven 15mer hits, since each 9mer is present in seven 15mers.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/78589/elife-78589-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Full Venn diagrams showing relationships between peptides which enriched in the doped library (‘Doped’) and undoped library (‘Undoped’), and contained a 9mer peptide which enriched in five or more of the seven 15mers containing it (‘≥5/7’), for (a) HLA-DR401, (b) HLA-DR402, and (c) HLA-DR404.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/78589/elife-78589-fig2-figsupp3-v2.jpg)

**Figure 2—figure supplement 3.:** (a) HLA-DR402: Sequence logo of 1690 peptides that enriched in both doped and undoped selections of the SARS-CoV and SARS-CoV-2 library for HLA-DR402. (b) HLA-DR404: Sequence logo of 2094 peptides that enriched in both doped and undoped selections of the SARS-CoV and SARS-CoV-2 library for HLA-DR404. Logos were generated with Seq2Logo-2.0.

Because the library is designed with a step size of 1, we next utilized overlap between adjacent peptides to determine high-confidence binders. This analysis allows us to address the potential that peptide sequences could register shift in such a way that invariant portions of the linker sequences could inadvertently be incorporated into the peptide-binding groove. To do this, we develop and implement a smoothing method, examining overlapping peptides for shared enrichment behavior. Classically, the strongest determinant of peptide affinity for an MHC is the nine amino acid stretch sitting within the peptide-binding groove (Jones et al., 2006; Stern et al., 1994), although proximal peptide flanking residues can also affect binding (Lovitch et al., 2006; O’Brien et al., 2008; Zavala-Ruiz et al., 2004). In our libraries, a given 9mer is present in seven overlapping 15mer peptides, and we calculate how many of these seven 15mers have enriched. This calculation is shown schematically in Figure 2—figure supplement 1a with toy sequences and applied to enrichment data for SARS-CoV-2 nucleocapsid on HLA-DR401 in Figure 2—figure supplement 1b. Sequences with good 9mer cores should enrich along with neighboring sequences with the same 9mer sequence. In contrast, sequences which enrich spuriously or due to linker sequence in the peptide groove or other stochastic factors should have few neighbor sequences also enriching. Thus, we define a cutoff for high-confidence 9mer enrichment of five out of seven 9mer-containing sequences enriching. This cutoff tolerates some stochastic dropout, while still disallowing any cores that may solely enrich by register shifting the Gly-Ser linker residues into the Position 9 pocket, which are favorable for each MHC allele in our study (Abelin et al., 2019; Rappazzo et al., 2020; Reynisson et al., 2020). Of the 2467 peptides which enriched in both the doped and undoped libraries for HLA-DR401, 1791 also contain a 9mer sequence which enriched in five or more peptides of the seven neighboring sequences containing it (Figure 2a), with 676 peptides enriching in both doped and undoped libraries but not containing a 9mer core enriched in five or more peptides, and 788 15mers containing a 9mer which enriched in five or more peptides but enriched in zero or one of the doped and undoped libraries. These full relationships are captured in Venn diagrams in Figure 2—figure supplement 2 for all three MHC alleles studied here.

### Sequence motifs of enriched peptides are consistent with known binders and highlight considerations for designing epitope identification experiments

To examine the 9mer core motifs of enriched peptides, we utilized a position weight matrix (PWM) method to infer the peptide register and generated visualizations of the 9mer cores using Seq2Logo (Thomsen and Nielsen, 2012). Figure 2c shows a sequence logo of the aligned 9mer cores from the 2467 15mer peptides which enriched on HLA-DR401 in both doped and undoped libraries. The peptide motif is consistent with previously reported motifs for HLA-DR401 (Abelin et al., 2019; Rappazzo et al., 2020): hydrophobic amino acids are preferred at P1, acidic residues at P4, polar residues at P6, and small residues at P9. We also observe some preference for glycine at P8 in the sequence logo, which is potentially an artifact of non-native registers with linker at P8 and P9.

The other alleles used in the study, HLA-DR402 and HLA-DR404, have polymorphisms in their peptide-binding groove sequences as compared to HLA-DR401, which affect binding preferences. HLA-DR401 differs from HLA-DR402 at four amino acids and from HLA-DR404 at two amino acids, with all polymorphisms located in the beta chain. HLA-DR402 and HLA-DR404 share an amino acid distinct from HLA-DR401 affecting the P1 pocket (Gly86Val), resulting in a preference for smaller hydrophobic residues (Figure 3a). Three polymorphisms in HLA-DR402 affect P4, P5, and P7 compared to HLA-DR401 (Leu67Ile, Gln70Asp, and Lys71Glu), while HLA-DR404 has only one (Lys71Arg). Sequence logos for HLA-DR402 and HLA-DR404 are consistent with previously reported motifs and MHC polymorphisms (Figure 2—figure supplement 3). For HLA-DR402, we observe less P4 preference compared to the motif of HLA-DR402 binders enriched from a randomized yeast display peptide library (Rappazzo et al., 2020), albeit consistent with mass spectrometry-generated motifs which also showed minimal P4 preference for HLA-DR402 (Abelin et al., 2019).

![Figure 3.](https://cdn.elifesciences.org/articles/78589/elife-78589-fig3-v2.jpg)

**Figure 3.:** (a) Sequence alignment showing sequence differences in HLA-DR402 and HLA-DR404 compared to HLA-DR401 and highlighted on HLA-DR401 structure (PDB 1J8H). Colors are: red for amino acids shared between HLA-DR401 and HLA-DR404, green for amino acids shared between HLA-DR402 and HLA-DR404, and yellow for amino acids different in all three alleles. Affected peptide positions (P1, P4, P5, P7) are colored in blue and labelled on the structure. (b) Conservation and enrichment of 9mer peptides from SARS-CoV-2 and SARS-CoV spike proteins. Conserved 9mers are indicated in black. If a 9mer along the proteome enriched in five or more of the adjacent peptides containing it, its enrichment is indicated with a vertical line with color for allele (HLA-DR401: blue; HLA-DR402: red; HLA-DR404: gray) and opacity for virus (SARS-CoV-2: dark; SARS-CoV: light). (b–e) Zoomed regions show enrichment of individual 15mer peptides. Only peptides containing the bolded 9mer sequence are shown. Amino acids in the bolded 9mer that are not conserved between SARS-CoV-2 and SARS-CoV are highlighted in yellow.

To explore differences between mass spectrometry, defined libraries, and random libraries, and to probe the differing strengths of P4 peptide preference observed for HLA-DR402 between these modalities, we examined the compositions of randomized and defined libraries. We hypothesized that skewed amino acid abundances in nature, which are reflected in the defined library, could result in an apparent diminished amino acid preference. Indeed, three of the most preferred P4 residues for binding HLA-DR402, Trp, His, and Met (Rappazzo et al., 2020), are all low abundance in the SARS-CoV-2 proteome (Trp 1.1%, His 1.9%, Met 2.2%). In comparison, a randomized peptide library for HLA-DR402 (Rappazzo et al., 2020) had a higher representation of these amino acids (Trp 3.8%, His 2.9%, Met 3.8%). Additionally, the randomized library had approximately 9000-fold more members than the defined library, providing more instances of all amino acids. The low abundance and underrepresentation of these amino acids likely underlies the apparent lack of amino acid consensus at P4 in enriched peptides. Interestingly, Arg and Lys, which have also been reported as preferred HLA-DR402 P4 residues, are more abundant than Trp, His, and Met in the SARS-CoV-2 proteome (Arg 3.4% and Lys 5.9%; compare to Arg 9.7%, Lys 4.0% in the random library), but still show less representation at P4 in the defined library enriched peptides compared to the random library-enriched peptides. These differences in motifs between randomized and defined libraries highlight the utility of randomized libraries for downstream applications such as training prediction algorithms. Approaches influenced by amino acid abundance in nature, such as defined libraries and mass spectrometry approaches, could inadvertently bias against possible binders because of absence of amino acids in their null distribution, rather than true binding preference.

Next, we wanted to examine the distribution of peptides among the possible 9mer registers along each 15 amino acid sequence. Based on our register inference, of the 2467 enriched peptides from the HLA-DR401 library, 1610 peptides bound native 9mer cores without using any linker sequence residues in the 9mer core, which is consistent with theoretical ratios of possible native and non-native cores for a given 9mer (Supplementary file 1b). The peptides with predicted native 9mer cores were approximately equally distributed between possible registers, with the exception of the N-terminal register, which had one-third fewer peptides. This register had only a single N-terminal flanking residue (a fixed Ala), which is likely disfavored.

Because the library was designed with step size of one, many of the 9mer cores will be repeated among neighboring peptides. Of the 1610 HLA-DR401 peptides which enriched using a native 9mer core, there are 563 unique 9mer cores identified through register inference. Table 1 summarizes enrichment for each protein included in the library, highlighting the number of 15mers which enriched in both the doped and undoped libraries, the number of unique native 9mer cores, and the number of 15mers containing a 9mer enriched in at least five of seven overlapping peptides.

**Table 1.**
 Summary of enriched peptides for each source protein, including: the number of unique 15mers which each enriched in both of the doped and undoped libraries; the number of unique 9mer cores identified by register inference in these enriched 15mers (native cores only, so linker-containing inferred cores excluded); and the number of unique enriched 15mers that contain 9mer sequences enriched in five or more of overlapping neighbors.


<table>
  <thead>
    <tr>
      <th>Virus</th>
      <th>Protein</th>
      <th>Protein length(# of amino acids)</th>
      <th>MHC allele</th>
      <th># of 15mers</th>
      <th># of 9mer cores</th>
      <th># of smoothed 15mers</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">SARS-CoV</td>
      <td rowspan="3">Spike</td>
      <td rowspan="3">1255</td>
      <td>HLA-DR401</td>
      <td>324</td>
      <td>74</td>
      <td>221</td>
    </tr>
    <tr>
      <td>HLA-DR402</td>
      <td>217</td>
      <td>65</td>
      <td>110</td>
    </tr>
    <tr>
      <td>HLA-DR404</td>
      <td>289</td>
      <td>61</td>
      <td>193</td>
    </tr>
    <tr>
      <td rowspan="3">SARS-CoV</td>
      <td rowspan="3">Nucleocapsid</td>
      <td rowspan="3">422</td>
      <td>HLA-DR401</td>
      <td>40</td>
      <td>8</td>
      <td>34</td>
    </tr>
    <tr>
      <td>HLA-DR402</td>
      <td>34</td>
      <td>13</td>
      <td>12</td>
    </tr>
    <tr>
      <td>HLA-DR404</td>
      <td>31</td>
      <td>6</td>
      <td>20</td>
    </tr>
    <tr>
      <td rowspan="3">SARS-CoV-2</td>
      <td rowspan="3">Spike</td>
      <td rowspan="3">1273</td>
      <td>HLA-DR401</td>
      <td>305</td>
      <td>67</td>
      <td>221</td>
    </tr>
    <tr>
      <td>HLA-DR402</td>
      <td>230</td>
      <td>62</td>
      <td>130</td>
    </tr>
    <tr>
      <td>HLA-DR404</td>
      <td>290</td>
      <td>64</td>
      <td>217</td>
    </tr>
    <tr>
      <td rowspan="3">SARS-CoV-2</td>
      <td rowspan="3">Nucleocapsid</td>
      <td rowspan="3">419</td>
      <td>HLA-DR401</td>
      <td>34</td>
      <td>8</td>
      <td>24</td>
    </tr>
    <tr>
      <td>HLA-DR402</td>
      <td>33</td>
      <td>10</td>
      <td>15</td>
    </tr>
    <tr>
      <td>HLA-DR404</td>
      <td>30</td>
      <td>8</td>
      <td>18</td>
    </tr>
    <tr>
      <td rowspan="3">SARS-CoV-2</td>
      <td rowspan="3">Replicase polyprotein 1ab</td>
      <td rowspan="3">7096</td>
      <td>HLA-DR401</td>
      <td>1652</td>
      <td>388</td>
      <td>1204</td>
    </tr>
    <tr>
      <td>HLA-DR402</td>
      <td>1104</td>
      <td>325</td>
      <td>678</td>
    </tr>
    <tr>
      <td>HLA-DR404</td>
      <td>1368</td>
      <td>350</td>
      <td>890</td>
    </tr>
    <tr>
      <td rowspan="3">SARS-CoV-2</td>
      <td rowspan="3">Non-structural protein 8</td>
      <td rowspan="3">121</td>
      <td>HLA-DR401</td>
      <td>41</td>
      <td>10</td>
      <td>32</td>
    </tr>
    <tr>
      <td>HLA-DR402</td>
      <td>21</td>
      <td>7</td>
      <td>17</td>
    </tr>
    <tr>
      <td>HLA-DR404</td>
      <td>32</td>
      <td>8</td>
      <td>19</td>
    </tr>
    <tr>
      <td rowspan="3">SARS-CoV-2</td>
      <td rowspan="3">Protein 7a</td>
      <td rowspan="3">121</td>
      <td>HLA-DR401</td>
      <td>27</td>
      <td>8</td>
      <td>18</td>
    </tr>
    <tr>
      <td>HLA-DR402</td>
      <td>7</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <td>HLA-DR404</td>
      <td>13</td>
      <td>2</td>
      <td>6</td>
    </tr>
    <tr>
      <td rowspan="3">SARS-CoV-2</td>
      <td rowspan="3">Non-structural protein 6</td>
      <td rowspan="3">61</td>
      <td>HLA-DR401</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>HLA-DR402</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>HLA-DR404</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td rowspan="3">SARS-CoV-2</td>
      <td rowspan="3">Membrane protein</td>
      <td rowspan="3">222</td>
      <td>HLA-DR401</td>
      <td>40</td>
      <td>7</td>
      <td>29</td>
    </tr>
    <tr>
      <td>HLA-DR402</td>
      <td>26</td>
      <td>6</td>
      <td>19</td>
    </tr>
    <tr>
      <td>HLA-DR404</td>
      <td>23</td>
      <td>7</td>
      <td>21</td>
    </tr>
    <tr>
      <td rowspan="3">SARS-CoV-2</td>
      <td rowspan="3">Envelope small membrane protein</td>
      <td rowspan="3">75</td>
      <td>HLA-DR401</td>
      <td>6</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>HLA-DR402</td>
      <td>7</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <td>HLA-DR404</td>
      <td>6</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <td rowspan="3">SARS-CoV-2</td>
      <td rowspan="3">Protein 3a</td>
      <td rowspan="3">275</td>
      <td>HLA-DR401</td>
      <td>22</td>
      <td>4</td>
      <td>11</td>
    </tr>
    <tr>
      <td>HLA-DR402</td>
      <td>13</td>
      <td>4</td>
      <td>10</td>
    </tr>
    <tr>
      <td>HLA-DR404</td>
      <td>10</td>
      <td>2</td>
      <td>0</td>
    </tr>
    <tr>
      <td rowspan="3">SARS-CoV-2</td>
      <td rowspan="3">Replicase polyprotein 1a</td>
      <td rowspan="3">4405</td>
      <td>HLA-DR401</td>
      <td>948</td>
      <td>228</td>
      <td>658</td>
    </tr>
    <tr>
      <td>HLA-DR402</td>
      <td>657</td>
      <td>196</td>
      <td>409</td>
    </tr>
    <tr>
      <td>HLA-DR404</td>
      <td>865</td>
      <td>222</td>
      <td>582</td>
    </tr>
    <tr>
      <td rowspan="3">SARS-CoV-2</td>
      <td rowspan="3">ORF10 protein</td>
      <td rowspan="3">38</td>
      <td>HLA-DR401</td>
      <td>6</td>
      <td>1</td>
      <td>6</td>
    </tr>
    <tr>
      <td>HLA-DR402</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>HLA-DR404</td>
      <td>5</td>
      <td>1</td>
      <td>5</td>
    </tr>
    <tr>
      <td rowspan="3">SARS-CoV-2</td>
      <td rowspan="3">Protein non-structural 7b</td>
      <td rowspan="3">43</td>
      <td>HLA-DR401</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>HLA-DR402</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td>HLA-DR404</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <td rowspan="3">SARS-CoV-2</td>
      <td rowspan="3">Uncharacterized protein 14</td>
      <td rowspan="3">73</td>
      <td>HLA-DR401</td>
      <td>8</td>
      <td>4</td>
      <td>6</td>
    </tr>
    <tr>
      <td>HLA-DR402</td>
      <td>20</td>
      <td>5</td>
      <td>16</td>
    </tr>
    <tr>
      <td>HLA-DR404</td>
      <td>22</td>
      <td>4</td>
      <td>21</td>
    </tr>
    <tr>
      <td rowspan="3">SARS-CoV-2</td>
      <td rowspan="3">Protein 9b</td>
      <td rowspan="3">97</td>
      <td>HLA-DR401</td>
      <td>29</td>
      <td>7</td>
      <td>27</td>
    </tr>
    <tr>
      <td>HLA-DR402</td>
      <td>35</td>
      <td>6</td>
      <td>31</td>
    </tr>
    <tr>
      <td>HLA-DR404</td>
      <td>37</td>
      <td>9</td>
      <td>34</td>
    </tr>
  </tbody>
</table>

### Examining relationships between MHC-specific binding and spike proteins from SARS-CoV-2 and SARS-CoV

To further explore relationships between the MHCs studied here and their virally derived peptide repertoires, we compared the binding of SARS-CoV-2 and SARS-CoV spike proteins to all three MHC alleles. Sequence alignment of these three MHC alleles is shown in Figure 3a, with polymorphic regions highlighted on an HLA-DR401 structure (adapted from PDB 1J8H). Interplay between viral conservation and binding are illustrated in Figure 3b, highlighting conserved regions of the proteome in black and binders to each allele in gray, red, and blue. Regions are highlighted where sequences enrich in overlapping peptides; that is, for each nine amino acid stretch along the proteome, we calculated how many of the seven 15mer peptides enrich in the yeast display assay, and if a 9mer enriched five or more times, it is marked as a hit. Specific examples of these relationships are probed in Figure 3c,d,e, where individually enriched 15mer sequences are represented as horizontal lines above 15mer stretches in the proteome. Bolded 9mers are identified through register inference as consensus binding cores for these peptides. Only 15mers which contain the bolded 9mer are included in this representation. Non-conserved amino acids within this 9mer are highlighted in yellow.

Figure 3c illustrates a region that is not conserved between SARS-CoV-2 and SARS-CoV, where the SARS-CoV-2 peptides containing the core IYQAGSTPC are enriched for binding to all three MHCs, but mutations, including at both P1 and P4 to Proline, discourage binding of the aligned SARS-CoV peptide. Figure 3e illustrates a core that is conserved between SARS-CoV and SARS-CoV-2, which can bind only to HLA-DR401, but not to HLA-DR402 or HLA-DR404, likely due to the size of the P1 hydrophobic residue and, for HLA-DR402, the acidic P4 residue. Figure 3d illustrates relationships between both viral conservation and MHC preference. In Figure 3d, the SARS-CoV peptides containing the core IKNQCVNFN can bind to all three alleles. However, the aligned SARS-CoV-2 peptides containing the core VKNKCVNFN do not bind to HLA-DR401, likely because of the less preferable P1 Valine and basic P4 Lysine, but can bind to HLA-DR402, which prefers these residues. These peptides can bind to HLA-DR404, although only four of the adjacent peptides containing this core enrich, which is below the cutoff of five or more, and since no other adjacent peptides enriched, this would not have been classified as a binder (reflected in Figure 3b). This marginal, but below-threshold binding is logical, given that the P4 pocket for HLA-DR404 is similar to HLA-DR401, which does not prefer P4 Lysine, but HLA-DR404 has the same P1 binding pocket as HLA-DR402, which both prefer the P1 Valine in the SARS-CoV-2 peptide.

### Identifying peptide binders missed by computational prediction

Next, we compared our direct experimental assessments with results from computational MHC binding predictions. Prediction algorithms allow for rapid computational screening of potential peptide binders (Abelin et al., 2019; Reynisson et al., 2020), although they can contain systemic biases (Rappazzo et al., 2020). To test the outputs of our direct assessment approach and computational prediction algorithms, we assessed binding of several peptides using a fluorescence polarization competition assay to determine IC50 values, as described previously (Rappazzo et al., 2020; Yin and Stern, 2014). Yeast-formatted peptides (Ala + 15mer + Gly + Gly + Ser) from SARS-CoV-2 spike protein were run through NetMHCIIpan4.0 for binding to HLA-DR401, with binders defined as having ≤10%Rank (Eluted Ligand mode). Yeast display binders to HLA-DR401 were defined via the stringent criteria of (1) enriching in both doped and undoped selections and (2) containing a 9mer that enriched in five or more of the overlapping seven 15mers. 15mers were selected such that they could contain a maximum overlap of eight amino acids with other selected peptides, to avoid selecting peptides with redundant 9mer cores. While yeast-enriched peptides were largely consistent with computational prediction, we selected sets of sequences which disagreed between computation and experiment, as well as a several sequences that yeast display and NetMHCIIpan4.0 both classified as either binders or non-binders (Table 2). A length-matched version of the commonly studied Influenza A Virus HA306-318 peptide (APKYVKQNTLKLATG) known to bind HLA-DR401 (Hennecke and Wiley, 2002; Rappazzo et al., 2020) was also included as a positive control. Figure 4—figure supplement 1 shows a comparison of yeast-enriched and NetMHCpan4.0 predicted binders, with boxed sequences selected for testing by fluorescence polarization.

**Table 2.**
 Peptides selected for fluorescence polarization (FP) experiments for binding to HLA-DR401.NetMHCIIpan4.0 predictions for HLA-DR401 binding are performed on 15mers plus invariant flanking residues (N-terminal Ala, C-terminal Gly-Gly-Ser) and percent rank values generated using Eluted Ligand mode. Fluorescence polarization is performed on native 15mer peptides without invariant flanking residues.


<table>
  <thead>
    <tr>
      <th></th>
      <th>Spike position</th>
      <th>Peptide + flank(A + 15mer + GGS)</th>
      <th>NetMHCIIpan4.0predicted core(A + 15mer + GGS)</th>
      <th>NetMHCIIpan4.0 %Rank(A + 15mer + GGS)</th>
      <th>15mer affinity from FP (IC50, nM)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="6">Agreed Binders</td>
      <td>34–48</td>
      <td>ARGVYYPDKVFRSSVLGGS</td>
      <td>YYPDKVFRS</td>
      <td>1.49</td>
      <td>15.8</td>
    </tr>
    <tr>
      <td>87–101</td>
      <td>ANDGVYFASTEKSNIIGGS</td>
      <td>VYFASTEKS</td>
      <td>4.28</td>
      <td>2117</td>
    </tr>
    <tr>
      <td>303–317</td>
      <td>ALKSFTVEKGIYQTSNGGS</td>
      <td>FTVEKGIYQ</td>
      <td>8.41</td>
      <td>396.9</td>
    </tr>
    <tr>
      <td>362–376</td>
      <td>AVADYSVLYNSASFSTGGS</td>
      <td>YSVLYNSAS</td>
      <td>8.36</td>
      <td>113.7</td>
    </tr>
    <tr>
      <td>1015–1029</td>
      <td>AAAEIRASANLAATKMGGS</td>
      <td>IRASANLAA</td>
      <td>3.13</td>
      <td>105.4</td>
    </tr>
    <tr>
      <td>1112–1126</td>
      <td>APQIITTDNTFVSGNCGGS</td>
      <td>ITTDNTFVS</td>
      <td>7.32</td>
      <td>527.0</td>
    </tr>
    <tr>
      <td rowspan="8">Yeast-Enriched Binders</td>
      <td>165–179</td>
      <td>ANCTFEYVSQPFLMDLGGS</td>
      <td>YVSQPFLMD</td>
      <td>64.83</td>
      <td>14,652</td>
    </tr>
    <tr>
      <td>172–186</td>
      <td>ASQPFLMDLEGKQGNFGGS</td>
      <td>FLMDLEGKQ</td>
      <td>20.34</td>
      <td>123.2</td>
    </tr>
    <tr>
      <td>286–300</td>
      <td>ATDAVDCALDPLSETKGGS</td>
      <td>VDCALDPLS</td>
      <td>32.68</td>
      <td>521.6</td>
    </tr>
    <tr>
      <td>373–387</td>
      <td>ASFSTFKCYGVSPTKLGGS</td>
      <td>YGVSPTKLG</td>
      <td>16.59</td>
      <td>18,452</td>
    </tr>
    <tr>
      <td>469–483</td>
      <td>ASTEIYQAGSTPCNGVGGS</td>
      <td>IYQAGSTPC</td>
      <td>18.22</td>
      <td>67.7</td>
    </tr>
    <tr>
      <td>580–594</td>
      <td>AQTLEILDITPCSFGGGGS</td>
      <td>LEILDITPC</td>
      <td>62.00</td>
      <td>119.9</td>
    </tr>
    <tr>
      <td>739–753</td>
      <td>ATMYICGDSTECSNLLGGS</td>
      <td>YICGDSTEC</td>
      <td>70.91</td>
      <td>14.4</td>
    </tr>
    <tr>
      <td>920–934</td>
      <td>AQKLIANQFNSAIGKIGGS</td>
      <td>FNSAIGKIG</td>
      <td>20.47</td>
      <td>1121</td>
    </tr>
    <tr>
      <td rowspan="3">NetMHC-Predicted Binders</td>
      <td>113–127</td>
      <td>AKTQSLLIVNNATNVVGGS</td>
      <td>IVNNATNVV</td>
      <td>8.74</td>
      <td>&gt;50,000</td>
    </tr>
    <tr>
      <td>492–506</td>
      <td>ALQSYGFQPTNGVGYQGGS</td>
      <td>YGFQPTNGV</td>
      <td>4.11</td>
      <td>454.7</td>
    </tr>
    <tr>
      <td>1151–1165</td>
      <td>AELDKYFKNHTSPDVDGGS</td>
      <td>YFKNHTSPD</td>
      <td>5.74</td>
      <td>35,510</td>
    </tr>
    <tr>
      <td rowspan="2">Agreed Non-Binders</td>
      <td>534–548</td>
      <td>AVKNKCVNFNFNGLTGGGS</td>
      <td>FNFNGLTGG</td>
      <td>57.13</td>
      <td>&gt;50,000</td>
    </tr>
    <tr>
      <td>1079–1093</td>
      <td>APAICHDGKAHFPREGGGS</td>
      <td>ICHDGKAHF</td>
      <td>80.47</td>
      <td>&gt;50,000</td>
    </tr>
  </tbody>
</table>

The resulting fluorescence polarization IC50 data from the native 15mer peptides are shown in Table 2 and Figure 4—figure supplement 2. Peptides which both enriched in yeast display and were predicted by NetMHCIIpan4.0 to bind (‘Agreed Binders’) all showed IC50 values consistent with binding, each with IC50 < 2.2 µM. Similarly, peptides which were agreed non-binders showed no affinity for HLA-DR401, with IC50 > 50 µM.

All eight ‘Yeast-Enriched Binders’, which enriched in the yeast display assay but were not predicted to bind via NetMHCIIpan4.0, showed some degree of binding, with IC50 values distributed from 14 nM (higher affinity than the HA control peptide) to 18 µM (weak, but measurable, binding). Retrospectively, the weakest two binders appear to be enriching in the yeast display assay using the peptide linker or have a binding core offset from center. Interestingly, NetMHCIIpan4.0 predictions on the peptides identified via yeast display proved highly sensitive to the length or content of the flanking sequences: if we repeat predictions on only the antigen-derived 15mer sequences without the flanking sequences, NetMHCIIpan4.0 recovers four of its former false-negative peptides (Table 3; peptides listed at the top in each section of the table). We will refer to these four peptides as ‘flank-sensitive centered peptides’, as they each have the consensus 9mer core centered in the peptide.

**Table 3.**
 Effects of peptide flanking sequences on NetMHCIIpan4.0 predictions for HLA-DR401 binding and measured fluorescence polarization (FP) values for overlapping peptides.Yeast display-enriched peptides that are predicted to bind by NetMHCIIpan4.0 when without flanking residues, plus offset variants of these peptides, which are not predicted to bind, with or without flanking sequence. Yeast display register-inferred consensus cores are highlighted in bold. NetMHCIIpan4.0 percent rank values are generated using Eluted Ligand mode.


<table>
  <thead>
    <tr>
      <th>Spike position</th>
      <th>Sequence</th>
      <th>NetMHCIIpan4.0 predicted core(A + 15mer + GGS)</th>
      <th>NetMHCIIpan4.0 %Rank(A + 15mer + GGS)</th>
      <th>NetMHCIIpan4.0 predicted core(15mer)</th>
      <th>NetMHCIIpan4.0 %Rank(15mer)</th>
      <th>15mer affinity from FP (IC50, nM)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>172–186</td>
      <td>SQPFLMDLEGKQGNF</td>
      <td>FLMDLEGKQ</td>
      <td>20.34</td>
      <td>FLMDLEGKQ</td>
      <td>4.1</td>
      <td>123.2</td>
    </tr>
    <tr>
      <td>173–187</td>
      <td>QPFLMDLEGKQGNFK</td>
      <td>FLMDLEGKQ</td>
      <td>27.73</td>
      <td>FLMDLEGKQ</td>
      <td>12.21</td>
      <td>8613</td>
    </tr>
    <tr>
      <td>286–300</td>
      <td>TDAVDCALDPLSETK</td>
      <td>VDCALDPLS</td>
      <td>32.68</td>
      <td>VDCALDPLS</td>
      <td>9.8</td>
      <td>1154</td>
    </tr>
    <tr>
      <td>287–301</td>
      <td>DAVDCALDPLSETKC</td>
      <td>VDCALDPLS</td>
      <td>42.42</td>
      <td>VDCALDPLS</td>
      <td>22.57</td>
      <td>4,393</td>
    </tr>
    <tr>
      <td>469–483</td>
      <td>STEIYQAGSTPCNGV</td>
      <td>IYQAGSTPC</td>
      <td>18.22</td>
      <td>IYQAGSTPC</td>
      <td>5.41</td>
      <td>67.7</td>
    </tr>
    <tr>
      <td>467–481</td>
      <td>DISTEIYQAGSTPCN</td>
      <td>IYQAGSTPC</td>
      <td>11.47</td>
      <td>IYQAGSTPC</td>
      <td>12.61</td>
      <td>4875</td>
    </tr>
    <tr>
      <td>471–485</td>
      <td>EIYQAGSTPCNGVEG</td>
      <td>YQAGSTPCN</td>
      <td>39.17</td>
      <td>YQAGSTPCN</td>
      <td>21.81</td>
      <td>12,519</td>
    </tr>
    <tr>
      <td>920–934</td>
      <td>QKLIANQFNSAIGKI</td>
      <td>FNSAIGKIG</td>
      <td>20.47</td>
      <td>IANQFNSAI</td>
      <td>7.89</td>
      <td>1495</td>
    </tr>
    <tr>
      <td>921–935</td>
      <td>KLIANQFNSAIGKIQ</td>
      <td>FNSAIGKIQ</td>
      <td>18.3</td>
      <td>IANQFNSAI</td>
      <td>19.79</td>
      <td>11,937</td>
    </tr>
  </tbody>
</table>

To further investigate the relationship with flanking residues, we selected five additional peptides (‘offset peptides’) matching three criteria; these offset peptides were (1) enriched in the yeast display assay, (2) share an overlapping core with the four flank-sensitive centered peptides, but are (3) not predicted by NetMHCIIpan4.0 to be binders (either with or without invariant flanking sequence added). All five offset peptides have their predicted cores offset by one to two amino acids from center, leaving at minimum one amino acid on both ends of the 9mer core for each peptide. All five offset peptides exhibit some binding, with IC50 values below 13 µM. Each peptide is lower affinity than its overlapping centered counterpart, illustrating effects of flanking residues on peptide binding, although some over-estimation of these effects in NetMHCIIpan4.0 predictions are present.

We tested three 'NetMHC-Predicted Binders’, which were predicted to bind by NetMHCIIpan4.0, but were not enriched (nor did any neighboring sequences within an offset of four amino acids) in the yeast display assay (Table 2). Of these, one bound to HLA-DR401 (IC50 475 nM), while two showed minimal binding with IC50 > 35 µM, which is above the maximum 20 µM concentration tested. All three were predicted by NetMHCIIpan4.0 to bind with or without the invariant flanking sequences (Eluted Ligand mode %Rank: 5.7, 4.1, 8.7 (with flanking residues) and 2.3, 0.6, 7.0 (without flanking residues), for ELDKYFKNHTSPDVD, LQSYGFQPTNGVGYQ, and KTQSLLIVNNATNVV, respectively).

Of the eight ‘Yeast-Enriched Binders’ in Table 2, six contain cysteine residues, which have been shown to be systematically absent from other datasets, including those from monoallelic mass spectrometry (Abelin et al., 2019; Barra et al., 2018), yet present in yeast display-derived datasets (Rappazzo et al., 2020). To test for non-specific binding due to cysteine, two cysteine-containing ‘Agreed Non-Binders’ were also tested and showed no affinity for HLA-DR401, suggesting that cysteine itself is not causing non-specific binding. In the fluorescence polarization dataset, the highest affinity binder (14 nM) contained cysteine and was missed by NetMHCIIpan4.0 predictions (Eluted Ligand mode %Rank: 71 [with flanking residues] and 28 [without flanking residues]).

The relationship between measured IC50 values and NetMHCIIpan4.0 predicted values for all 15mer SARS-CoV-2 spike peptides tested is shown in Figure 4, Figure 4—figure supplement 2, Figure 4—figure supplement 3.

![Figure 4.](https://cdn.elifesciences.org/articles/78589/elife-78589-fig4-v2.jpg)

**Figure 4.:** Relationship between measured IC50 values and NetMHCIIpan4.0 predicted ranks in Eluted Ligand mode (EL) on invariant-flanked sequences. Data points are colored by label, and IC50 values ≥ 50 µM are set to 50 µM.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/78589/elife-78589-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** 15mer peptides which enriched for binding to HLA-DR401 in both the doped and undoped libraries are indicated with horizontal lines above the enriched 15mer sequence (blue). NetMHCIIpan4.0 predicted binders (rank ≤ 10%) on yeast-formatted peptides are shown in red. Boxed sequences are tested in subsequent fluorescent polarization experiments, and colored as indicated in the legend.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/78589/elife-78589-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (a) Agreed binder peptides which are predicted to bind by NetMHCIIpan4.0 and enriched in yeast display experiments. Dashed line is the positive control HA peptide. (b) Agreed non-binder peptides which did not enrich in yeast display experiments and were not predicted to bind by NetMHCIIpan4.0. (c) Yeast enriched peptides from Table 2 and Table 3. Offset variants from Table 3 are dashed lines. (d) NetMHCIIpan4.0 predicted peptides which are not enriched in the yeast display library. Mean and standard deviation from three replicates are plotted for each peptide concentration. Source data are provided as Figure 4—figure supplement 2—source data 1.

![Figure 4—figure supplement 3.](https://cdn.elifesciences.org/articles/78589/elife-78589-fig4-figsupp3-v2.jpg)

**Figure 4—figure supplement 3.:** Relationship between measured IC50 values and NetMHCIIpan4.0 predicted ranks in Eluted Ligand mode (EL) on unflanked (native) 15mer sequences. Data points are colored by label, and IC50 values ≥ 50 µM are set to 50 µM.

### Comparing whole dengue serotype proteomes for common MHC-binding peptides

Defined yeast display libraries can generate data for diverse objectives. Dengue viruses typically cause most severe disease after a second infection with a serotype different from the first infection, due to antibody-dependent enhancement (Guzman et al., 2016), which makes T cell-directed therapeutics a potentially attractive means of combating disease. To profile and compare MHC binding across serotypes, we generated libraries containing 12,672 dengue-derived peptides, covering the entire proteomes of dengue serotypes 1–4. These libraries were on HLA-DR401 and HLA-DR402 and had coverage of 98% and 96% of the dengue library members after construction, respectively (Supplementary file 1c).

Peptides from homologous regions of the four dengue serotypes have different MHC binding ability, as illustrated in Figure 5a for binding to HLA-DR401. The proteins encoded in the dengue genome are indicated along the horizontal axis (C: capsid; M: membrane; E: envelope; NS: nonstructural proteins). Peptides that enriched in the yeast display assay are marked by a line (serotype 1 in blue, serotype 2 in purple, serotype 3 in red, and serotype 4 in gray). The proteome is smoothed to nine amino acid stretches (as in Figure 3b), with a given nine amino acid region marked as a hit if five or more of the seven adjacent peptides enrich. For each 9mer, the maximum number of serotypes with a conserved identical 9mer at that position is indicated at the top in black.

![Figure 5.](https://cdn.elifesciences.org/articles/78589/elife-78589-fig5-v2.jpg)

**Figure 5.:** (a) Conservation and enrichment of 9mer peptides along four aligned dengue serotypes. All stretches of nine amino acids are compared across the four serotypes and conservation is indicated with a black vertical line (i.e. 2, 3, or 4 of four serotypes conserved). 9mers which enriched on HLA-DR401 are also indicated, colored by virus serotype. (b–d) Zoomed regions, showing enrichment for individual 15mer peptides to HLA-DR401. Only peptides which contain the bolded 9mer sequence are shown. Amino acids in the bolded 9mer that are not conserved between serotypes are highlighted in yellow. Insets show regions which are differently conserved and enriched: (b) non-conserved sequences with peptides from one serotype enriched; (c) conserved sequences enriched across all serotypes; (d) non-conserved sequences which are enriched.

These data can reveal relationships between conservation and binding ability. Figure 5b–d shows enrichment data for individual 15mer peptides, with consensus inferred 9mer cores in bold and non-conserved amino acids in these cores highlighted in yellow, as in Figure 3c–e. Conserved cores which show binding ability (Figure 5c) may be ideal T cell targets. However, the permissiveness of the binding groove allows for peptides to bind that have mutations at the anchors, such as in NS5 (Figure 5d), where P4 Asn and P4 Met both allow binding. Interestingly, the serotype 3 core (LASNAICSA) only enriched in four peptides, which is below our described cutoff for high-confidence peptide cores. However, three adjacent peptides enriched and register inference for these peptides identifies the non-native, linker-containing version of the LASNAICSA core as binding in the MHC-binding groove. This results in an adjacent 9mer being highlighted as a binder in this region (Figure 5a) because overlapping 15mers enrich in five or more of the seven adjacent peptides. With this in mind, care must be taken for core identification in enriched regions and can be aided by coupling enrichment with register inference of enriched peptides. Further, we can also see relationships between conservation and binding in non-conserved regions, such as in the envelope protein (Figure 5b) with the mutations in serotype 3 enabling binding.

## Discussion

CD4+ T cell responses play important roles in infection, autoimmunity, and cancer. By extension, understanding peptide-MHC binding is critical for identifying and engineering T cell epitopes. Here, we present an approach to directly assess defined libraries of peptides covering whole pathogen proteomes for binding to MHC-II proteins. We examine alternative modes of selection and utilize overlapping peptides to determine high-confidence binders. We demonstrate the utility of this approach by identifying binders that are missed by prediction algorithms, highlighting a prediction algorithm bias against cysteine-containing peptides and sensitivity to peptide flanking residues (Table 2 and Table 3). Finally, this approach can be utilized for different objectives, including comparing binding to multiple MHC alleles (Figure 3) or comparing peptides from related pathogen sequences for MHC-II binding (Figure 5). Whole protein- or proteome-scale analysis across related viruses provides insight into relationships between conserved epitopes and MHC binding (Figures 3b and 5a) and specific examples validate the consistency with the underlying biophysics of peptide-MHC binding (Figures 3c–e ,–5b–d).

When compared to previously described yeast display approaches to identify peptides binding to MHC-II molecules, our approach benefits from recent advances in next-generation sequencing and pooled oligonucleotide synthesis. Other library generation methods for peptide-MHC-II binding have relied on synthetic peptides (Liu et al., 2021a), randomized, DNA-encoded peptides (Rappazzo et al., 2020), or digested DNA from amplified viral genomes (Wen et al., 2008), which are impractical for comprehensive assessment of defined proteome-scale libraries. Next-generation sequencing further enables a comprehensive and granular view of peptide enrichment, beyond sequencing and validation of individual clones (Wen et al., 2008).

This approach for direct assessment shows benefit compared to prediction algorithms for identifying binders, particularly for finding weak peptide binders. Weak binding peptides have been reported to be less immunodominant than strong MHC-binding peptides (Burger et al., 2021; Lazarski et al., 2005; Wu et al., 2019); however, there are also examples of weak MHC-binding peptides which can elicit T cell responses and be of clinical relevance in disease contexts, including in autoimmunity and cancer (Latek et al., 2000; Levisetti et al., 2008; Valmori et al., 1998; Zarour et al., 2000). As such, information about weak binding peptides can be of potential scientific and clinical relevance.

The overlapping peptides in our library were useful for identifying enriched cores, especially when combined with our register inference to identify consensus cores shared between these overlapping peptides. NetMHCIIpan4.0 exhibits a sensitivity to length and register, which may cause users to miss binders, albeit potentially of lower affinity. Of the overlapping peptides we tested to study this phenomenon, NetMHCIIpan4.0 correctly ranked the affinities of the overlapping peptides (Table 3), but missed binders. Figure 4—figure supplement 1 also highlights the sensitivity of NetMHCIIpan4.0 to flanking sequences, where neighboring peptides with shared cores often are not predicted to bind, resulting in fewer clusters of peptides. Comparison with yeast display datasets also highlights several non-binding peptides predicted by NetMHCIIpan4.0 to be binders. Coupling this yeast display approach with computational predictions can be useful for identifying false positive predicted peptides in order to correctly prioritize peptides of interest.

Our work reveals insights on the design of epitope identification experiments, including the utility of overlapping peptides and considerations for comparing libraries of unbiased and proteome-derived peptides. Design of defined libraries with sources of redundancy, such as overlapping peptides, was critical for determining binders with higher degrees of confidence and allowed us to apply stringent cutoffs for individual peptides. Overlapping peptides allowed us to account for construct-specific confounding effects, such as the peptides binding using non-native residues in the linker. Future iterations can change the sequence of the linker, such as defining favorable P(–1) and P10 anchors to fix the register (Rappazzo et al., 2020), although these adaptations would likely require MHC-specific knowledge in advance and may need to be altered for different MHCs. Additionally, the engineered redundancy and multiple modes of selection result in hyperparameters that can be tuned to meet users’ stringency requirements, such as defining different thresholds for calling individual 15mer binders or alternative integration of overlapping binders. Additionally, our comparison of unbiased and proteome-derived libraries highlights how aggregate motifs may be affected by underlying amino acid preferences found in protein sequences themselves, which may inadvertently disfavor sequences that can bind strongly to MHC molecules yet consist of amino acid covariates that are not as commonly found in proteins.

Further, this approach can be used to study MHC binding between similar viruses, as done with the dengue proteomes and the spike proteins from SARS-CoV-2 and SARS-CoV, highlighting regions where mutations disrupt binding as well as regions where binding is unperturbed. This method can also be rapidly adapted to study future sequences if pathogens evolve over time.

As experimental approaches and computational approaches continue to co-develop, they present complementary benefits. Though this platform allows for rapid assessment of peptide-MHC binding, the speed of computational prediction surpasses experimental approaches. NetMHCIIpan4.0 prediction and yeast display selections identified sets of non-overlapping misses, highlighting a utility for both. Additionally, all agreed binders and non-binders matched fluorescence polarization results, suggesting a consensus of yeast display enrichment and algorithmic prediction provide high-confidence results. Approaches such as yeast display assessment can be used to complement computational approaches, such as for identifying cysteine-containing peptides which are still under-predicted by algorithms. Similarly, prediction algorithms can be trained using large, quality datasets to account for biases. Training sets can specifically be augmented with data from defined peptide libraries designed to study peptides where current algorithmic predictions are of lower confidence. In another application, our platform to assess peptide-MHC binding can be used to design high-throughput assays to test peptide immunogenicity in clinical samples (Klinger et al., 2015; Snyder et al., 2020).

Defined yeast display peptide libraries can also be readily applied to identification of T cell ligands and present an opportunity for identifying unknown ligands from orphan TCRs known to respond to a proteome of interest (Birnbaum et al., 2014; Gee et al., 2018). Yeast have also been previously utilized as artificial antigen-presenting cells to stimulate T cell hybridomas (Wen et al., 2008), making it possible to further streamline antigen discovery efforts. As DNA synthesis and sequencing continue to advance, defined peptide libraries expanding beyond viral proteomes to covering whole bacterial or human proteomes will be possible, and could present opportunities for investigating autoimmune diseases, which frequently have strong MHC-II associations (Karnes et al., 2017). Such tools would be rich resources for identifying both peptide-MHC binders and TCR ligands.

## Methods

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
      <td>Strain, strain background (Saccharomyces cerevisiae)</td>
      <td>RJY100</td>
      <td>PMID:26333274</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Trichoplusia ni)</td>
      <td>High Five cells</td>
      <td>Thermo Fisher</td>
      <td>Cat#:B85502</td>
      <td></td>
    </tr>
    <tr>
      <td>Cell line (Spodoptera frugiperda)</td>
      <td>Sf9 cells</td>
      <td>Thermo Fisher</td>
      <td>Cat#:11496015</td>
      <td></td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-Myc-AlexaFluor647 (Mouse monoclonal)</td>
      <td>Cell Signaling Technology</td>
      <td>Cat#:2233</td>
      <td>Library selections: 1:100</td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>Peptide-MHC-II with cleavable peptide linker in pYal (plasmid)</td>
      <td>PMID:32887877</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>HLA-DR401 in pAcGP67a (plasmid)</td>
      <td>PMID:32887877</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Recombinant DNA reagent</td>
      <td>HLA-DM in pAcGP67a (plasmid)</td>
      <td>PMID:32887877</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Peptide, recombinant protein</td>
      <td>3C protease</td>
      <td>Other</td>
      <td></td>
      <td>Purified from Escherichia coli BL21 cells</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>PandaSeq</td>
      <td>PMID:22333067</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>NetMHCIIpan4.0</td>
      <td>PMID:32406916</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Peptide register inference algorithm</td>
      <td>This paper</td>
      <td></td>
      <td>See Code Availability</td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Prism</td>
      <td>GraphPad Prism software (http://www.graphpad.com/)</td>
      <td></td>
      <td>Version: 9.3</td>
    </tr>
  </tbody>
</table>

### Library design and creation

Yeast display libraries were designed to cover all 15mer sequences within a given proteome, with step size 1. Reference proteomes used in creating defined libraries were accessed from Uniprot, with the following Proteome IDs. SARS-CoV-2: UP000464024, SARS-CoV: UP000000354, dengue serotype 1: UP000002500, dengue serotype 2: UP000180751, dengue serotype 3: UP000007200, dengue serotype 4: UP000000275. The dengue proteome is expressed as a single polypeptide, and peptides were generated from that contiguous stretch.

Each library peptide is encoded in DNA space, with specific codons selected randomly from possible codons, with probabilities matching yeast codon usage (GenScript Codon Usage Frequency Table). The DNA-encoded peptide sequences were flanked by invariant sequences from the yeast construct for handles in amplification and cloning, and the DNA oligonucleotide sequences were ordered from Twist Bioscience (South San Francisco, CA), with maximum length of 120 nucleotides. The DNA oligo pool was amplified in low cycle PCR, followed by amplification with construct DNA using overlap extension PCR. This extended product was assembled in yeast with linearized pYal vector at a 5:1 insert:vector via electroporation with electrocompetent Saccharomyces cerevisiae RJY100 yeast (Van Deventer et al., 2015). Primers utilized in this study are included in Supplementary file 1d.

HLA-DR401 and HLA-DR402 libraries were generated using previously described vectors (Rappazzo et al., 2020) which contain mutations from wild type Metα36Leu, Valα132Met, Hisβ33Asn, and Aspβ43Glu to enable proper folding without disrupting TCR or peptide contact residues (Rappazzo et al., 2020). HLA-DR404 was generated using the same stabilizing mutations. As previously described (Rappazzo et al., 2020), the peptide C-terminus is connected to the MHC construct via a Gly-Ser linker (Figure 1a), and the N-terminus of the peptide includes an extra alanine to ensure consistent cleavage between the construct and its signal peptide.

The previously described null library (Dai et al., 2021) was generated with a peptide encoded as ‘NNNTAANNNNNNNNNTAGNNNNNNNNNNNNTGANNNNNN’, where ‘N’ indicates any nucleotide and encodes 10 random amino acids and three stop codons. This library was similarly generated in yeast using electrocompetent RJY100 yeast.

### Peptide visualizations and predictions

Data visualizations of viral conservation and enrichment were generated using custom scripts. For each 9mer stretch in a protein of interest, there are seven 15mer sequences that overlap and contain that 9mer. We calculate how many of these seven 15mers enriched in both the doped and undoped libraries. If five or more of the seven 15mers enriched, that stretch is marked as a ‘hit’. To examine conservation between viruses, viral proteins are aligned using ClustalOmega (Madeira et al., 2019). Aligned 9mer stretches are compared between viruses and identical stretches are considered conserved. Hits are determined individually for each virus before merging, such that gaps in sequence alignments do not affect calculations of enrichment for a given virus.

Representations of 15mer hits (as in Figure 3, Figure 5 and Figure 4—figure supplement 1) were generated using in-house scripts, such that a 15mer that enriched in both the doped and undoped library was marked as a horizontal line above the relevant 15mer sequence. Only 15mers containing the bolded 9mer in Figure 3 and Figure 5 were included.

NetMHCIIpan4.0 webserver was used for computational predictions (Reynisson et al., 2020), where a binder is defined as having a predicted percent rank ≤10%, as defined in the webserver instructions.

### Yeast library selections

Library selections were consistent with previous peptide-MHC-II yeast display dissociation studies (Dai et al., 2021; Rappazzo et al., 2020). Yeast were washed into pH 7.2 PBS with 1 µM 3C protease and incubated at room temperature for 45 min. Yeast were then washed into 4°C acid saline (150 mM NaCl, 20 mM citric acid, pH 5) with 1 µM HLA-DM and incubated at 4°C overnight. Each step takes place in the presence of competitor peptide (HLA-DR401: HA306-318 PKYVKQNTLKLAT, 1 µM; HLA-DR402: CD4836-51 FDQKIVEWDSRKSKYF, 5 µM; HLA-DR404: NKVKSLRILNTRRKL, 5 µM Vita et al., 2019). Non-specific binders are removed by incubating yeast with anti-AlexaFluor647 magnetic beads and flowed over a magnetic Milltenyi column at 4°C. A positive selection follows, comprised of incubation with anti-Myc-AlexaFluor647 antibody (1:100 volume:volume; Myc tag (9B11) Mouse mAb AlexaFluor647 Conjugate #2233 Cell Signaling Technology) and anti-AlexaFluor647 magnetic beads (1:10 volume:volume) and flowed over a Milltenyi column on a magnet at 4°C, such that yeast with bound peptide are retained on the column. These yeast are eluted, grown to confluence in at 30°C in SDCAA media (pH 5), and sub-cultured in at 20°C SGCAA media (pH 5) at OD600=1 for 2 days. The first round of selections of doped libraries were conducted on 180 million yeast (SARS-CoV-2 library) or 400 million yeast (dengue library) to ensure at least 20-fold coverage of peptides. Subsequent rounds of doped library selection, and all rounds of undoped library selections, were performed on 20–25 million yeast. Before each round of selection, a sample of yeast are stained with an anti-Myc antibody to check induction of protein expression, as in Figure 1c.

### Library sequencing and analysis

Libraries were deep sequenced to determine their composition after each round of selection. Plasmid DNA was extracted from 10 million yeast from each round of selection using the Zymoprep Yeast Miniprep Kit (Zymo Research), following the manufacturer’s instructions. Amplicons were generated through PCR, covering the peptide sequence through the 3C cut site. A second PCR round was performed to add i5 and i7 sequencing handles and in-line index barcodes unique to each round of selection. Amplicons were sequenced on an Illumina MiSeq using paired-end MiSeq v2 300 bp kits at the MIT BioMicroCenter.

Paired-end reads were assembled using PandaSeq (Masella et al., 2012). Peptide sequences were extracted by identifying correctly encoded flanking regions, and were filtered to ensure they matched designed members of the library or the randomized null construct encoding, providing a stringent threshold for contamination and PCR and read errors.

The resulting data are analyzed for convergence, as described in the main text. Once a library has converged, it is likely that changes in subsequent rounds of selection are due to stochastic variation rather than improved binding.

Peptide and read count data are in Supplementary file 1a and c. Columns are labelled as: [count]_[doped or undoped library]-[HLA-DR allele] post-R[round number]-[positive or negative, for undoped libraries]. For unselected ‘R0’ libraries, an additional suffix may be present to indicate whether the library was sequenced before or after doping into the null library. Also indicated are: amino acid sequence (‘aa’), encoding DNA sequence (‘dna’), and whether the sequence matched the null library (indicated in ‘doped_match’ or ‘name’).

### Register inference and sequence logos

The 9mer core of enriched sequences was inferred using an in-house alignment algorithm. In this approach, we utilize a 9mer PWM, which we assess at different offsets along the peptide. We one-hot encode sequences and pad with zeros on the C-terminus of the peptide; to assess seven native registers and four non-native registers, we pad the peptides with four zeros. Three of the non-native registers utilize the linker at the P9 anchor but not the P6 anchor, and the addition of a fourth register captures a minority set of peptides which utilize Gly-Gly-Ser-Gly of the linker at P6 through P9 in the groove. Register-setting is performed with zero-padded 15mers, rather than 15mers flanked by invariant flanking residues, because the PWM would otherwise align all sequences to the invariant region.

At the start, we randomly assign peptides to registers and generate a 9mer PWM. Over subsequent iterations, peptides are assigned to new registers and the PWM was updated. Assignments are random but biased, such that clusters corresponding to registers that match the PWM are favored. Specifically, at each assignment we first take out the sequence under consideration from the PWM. The PWM then defines an energy value for each register shift of a given peptide, which is then used to generate a Boltzmann distribution from which we sample the updated register shift. The stochasticity is decreased over time by raising the inverse temperature linearly from 0.05 to 1 over 60 iterations, simulating ‘cooling’ (Andreatta et al., 2017). A final deterministic iteration was carried out, where the distribution concentrates entirely on the optimal register shift.

After register inference, sequence logo visualizations of the 9mer cores were generated using Seq2Logo-2.0 with default settings, except using background frequencies from the SARS-CoV-2 proteome and SARS-CoV spike and nucleocapsid proteins (Thomsen and Nielsen, 2012). For registers with the C-terminus utilizing the C-terminal linker, the relevant linker sequence was added to achieve a full 9mer sequence for visualizing the full 9mer core. For HLA-DR401, distribution among registers, starting from N-terminally to C-terminally aligned in the peptide, is: 161, 237, 227, 238, 231, 279, 237, 266, 271, 202, 118.

### Recombinant protein expression

HLA-DM and HLA-DR401 were expressed recombinantly in High Five insect cells (species Trichoplusia ni; Thermo Fisher B85502) using a baculovirus expression system, as previously described (Birnbaum et al., 2014; Rappazzo et al., 2020). Ectodomain sequences of each chain were formatted with a C-terminal poly-histidine purification tag and cloned into pAcGP67a vectors. Each vector was individually transfected into Sf9 insect cells (species Spodoptera frugiperda; Thermo Fisher 11496015) with BestBac 2.0 linearized baculovirus DNA (Expression Systems; Davis, CA) and Cellfectin II Reagent (Thermo Fisher), and propagated to high titer. Viruses were co-titrated for optimal expression to maximize balanced MHC heterodimer formation, co-transduced into High Five cells, and grown for 48–72 hr at 27°C. The secreted protein was purified from pre-conditioned media supernatant with Ni-NTA resin and purified via size exclusion chromatography with an S200 increase column on an AKTA PURE FPLC (GE Healthcare). To improve protein yields, the HLA-DRB1*04:01 chain was expressed with a CLIP87-101 peptide (PVSKMRMATPLLMQA) connected to the N-terminus of the MHC chain via a flexible, 3C protease-cleavable linker.

### Fluorescence polarization experiments for peptide IC50 determination

Peptide IC50 values were determined following a protocol modified from Yin and Stern, 2014, as in Rappazzo et al., 2020. In the assay, recombinantly expressed HLA-DR401 is incubated with fluorescently labelled modified HA306-318 (APRFV{Lys(5,6 FAM)}QNTLRLATG) peptide and a titration series for each unlabelled competitor peptide is added (1.28 nM to 20 µM). A change in polarization value resulting from displacement of fluorescent peptide from the binding groove is used to determine IC50 values.

Relative binding at each concentration is calculated as (FPsample – FPfree)/(FPno_comp – FPfree). Here, FPfree is the polarization value for the fluorescent peptide alone with no added MHC, FPno_comp is polarization value for MHC with no competitor peptide added, and FPsample is the polarization value with both MHC and competitor peptide added. Relative binding curves were then generated and fit in Prism 9.3 to the equation y=1/(1+[pep]/IC50), where [pep] is the concentration of unlabelled competitor peptide, in order to determine the concentration of half-maximal inhibition, the IC50 value.

Each assay was performed at 200 µL, with 100 nM recombinant MHC, 25 nM fluorescent peptide, and competitor peptide (GenScript). This mixture co-incubates in pH 5 binding buffer at 37°C for 72 hr in black flat bottom 96-well plates. Competitor peptide concentrations ranged from 1.28 nM to 20 µM, as a fivefold dilution series. Three replicates are performed for each peptide concentration. Fluorescent peptide-only, no competitor peptide, and binding buffer controls were also included. Our MHC was expressed with a linked CLIP peptide, so prior to co-incubation, the peptide linker is cleaved by addition of 3C protease at 1:10 molar ratio at room temperature for 1 hr; the residual cleaved 100 nM CLIP peptide is not expected to alter peptide-binding measurements.

Measurements were taken on a Molecular Devices SpectraMax M5 instrument. G-value was 1.1 for each plate, as calculated per the manufacturer’s instructions for each plate based on fluorescent peptide-only wells minus buffer blank wells, with 35 mP reference for 5,6FAM (Fluorescein setting). Measurements were made with 470 nm excitation and 520 nm emission, 10 flashes per read, and default PMT gain high.

### Cell lines

High Five insect cells (species T. ni; Thermo Fisher B85502) and Sf9 insect cells (species S. frugiperda; Thermo Fisher 11496015) were utilized for recombinant protein production. Their identities have been confirmed functionally through characterization of their secreted baculovirus and protein production.

RJY100 (S. cerevisiae) (Van Deventer et al., 2015) were utilized for yeast surface display. Yeast identity has been confirmed through analysis of growth and library generation characteristics and engineered protein surface expression profiling.

Sf9 cells have tested mycoplasma negative, and High Five cells have not been independently tested since purchased from the manufacturer. RJY100 yeast have not been mycoplasma tested.

### Code availability

Scripts used for data processing and visualization are publicly available at https://github.com/birnbaumlab/Huisman-et-al-2022, copy archived at swh:1:rev:694c6976275bb02d1d498d0e8a01523a1cb1799d; Huisman, 2022.
