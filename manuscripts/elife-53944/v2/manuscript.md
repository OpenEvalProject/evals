# Loss of centromere function drives karyotype evolution in closely related Malassezia species

## Authors

- Sundar Ram Sankaranarayanan<sup>1</sup>
- Giuseppe Ianiri<sup>2</sup> ([ORCID: 0000-0002-3278-8678](https://orcid.org/0000-0002-3278-8678))
- Marco A Coelho<sup>2</sup>
- Md Hashim Reza<sup>1</sup>
- Bhagya C Thimmappa<sup>1</sup>
- Promit Ganguly<sup>1</sup>
- Rakesh Netha Vadnala<sup>3</sup>
- Sheng Sun<sup>2</sup>
- Rahul Siddharthan<sup>3</sup> ([ORCID: 0000-0002-2233-0954](https://orcid.org/0000-0002-2233-0954))
- Christian Tellgren-Roth<sup>4</sup>
- Thomas L Dawson<sup>5</sup>
- Joseph Heitman<sup>2</sup> †
- Kaustuv Sanyal<sup>1</sup> ([ORCID: 0000-0002-6611-4073](https://orcid.org/0000-0002-6611-4073)) †

### Affiliations

1. Molecular Mycology Laboratory, Molecular Biology and Genetics Unit, Jawaharlal Nehru Centre for Advanced Scientific Research Bengaluru India
2. Department of Molecular Genetics and Microbiology, Duke University Medical Center Durham United States
3. The Institute of Mathematical Sciences/HBNI Chennai India
4. National Genomics Infrastructure, Science for Life Laboratory, Department of Immunology, Genetics and Pathology, Uppsala University Uppsala Sweden
5. Skin Research Institute Singapore, Agency for Science, Technology and Research (A*STAR) Singapore Singapore
6. Department of Drug Discovery, Medical University of South Carolina, School of Pharmacy Charleston United States

† Corresponding author

## Abstract

Genomic rearrangements associated with speciation often result in variation in chromosome number among closely related species. Malassezia species show variable karyotypes ranging between six and nine chromosomes. Here, we experimentally identified all eight centromeres in M. sympodialis as 3–5-kb long kinetochore-bound regions that span an AT-rich core and are depleted of the canonical histone H3. Centromeres of similar sequence features were identified as CENP-A-rich regions in Malassezia furfur, which has seven chromosomes, and histone H3 depleted regions in Malassezia slooffiae and Malassezia globosa with nine chromosomes each. Analysis of synteny conservation across centromeres with newly generated chromosome-level genome assemblies suggests two distinct mechanisms of chromosome number reduction from an inferred nine-chromosome ancestral state: (a) chromosome breakage followed by loss of centromere DNA and (b) centromere inactivation accompanied by changes in DNA sequence following chromosome–chromosome fusion. We propose that AT-rich centromeres drive karyotype diversity in the Malassezia species complex through breakage and inactivation.

## Introduction

Centromeres are the genomic loci on which the kinetochore, a multi-subunit complex, assembles to facilitate high-fidelity chromosome segregation. The centromere-specific histone H3 variant CENP-A is the epigenetic hallmark of centromeres, as it replaces canonical histone H3 in the nucleosomes to make specialized centromeric chromatin that acts as the foundation to recruit other kinetochore proteins. A remarkable diversity in the organization of centromere DNA sequences has been observed to accomplish this conserved role (Roy and Sanyal, 2011; Yadav et al., 2018b).

The smallest known centromeres are the point centromeres present in budding yeasts of the family Saccharomycetaceae that span <200 bp in length (Clarke and Carbon, 1980; Gordon et al., 2011; Kobayashi et al., 2015). These centromeres are organized into conserved DNA elements I, II, and III that are recognized by a cognate kinetochore protein complex called the CBF3 complex, making them genetically defined centromeres. Small regional centromeres, identified in several Candida species, form the second category (Sanyal et al., 2004; Padmanabhan et al., 2008; Kapoor et al., 2015; Chatterjee et al., 2016) and have a 2–5-kb region enriched by kinetochore proteins. These centromeres can either have unique DNA sequences or a homogenized core that is flanked by inverted repeats. The third type of centromere structure is the large regional centromere, which is often repetitive in sequence and spans more than 15 kb. Large regional centromeres can be transposon-enriched, as in Cryptococcus species, or organized into repeat structures around a central core, as in Schizosaccharomyces pombe (Chikashige et al., 1989; Clarke and Baum, 1990; Sun et al., 2017; Yadav et al., 2018b).

Although the organization of DNA elements is variable, a majority of known centromeres share AT-richness as a common feature. Examples include the CDEII of point centromeres, central core sequences in S. pombe, and centromeres of Neurospora crassa, Magnaporthe oryzae, Plasmodium falciparum, and diatoms (Fitzgerald-Hayes et al., 1982; Iwanaga et al., 2010; Rhind et al., 2011; Kapoor et al., 2015; Diner et al., 2017; Yadav et al., 2019). Even the recently described mosaic centromere structure observed in Mucor circinelloides that has lost CENP-A comprises an AT-rich kinetochore-bound core region (Navarro-Mendoza et al., 2019). Although suppression of recombination around centromeres has been correlated with reduced GC content (Lynch et al., 2010), the genetic underpinning that determines how an AT-rich DNA region favors kinetochore assembly remains unclear. Ironically, AT-rich sequences have been shown to be fragile sites within a chromosome (Zhang and Freudenreich, 2007).

Several lines of evidence suggest that centromeres are species-specific and are among the most rapidly evolving genomic regions, showing variation even between closely related species (Bensasson et al., 2008; Padmanabhan et al., 2008; Rhind et al., 2011; Roy and Sanyal, 2011). This evolution is accompanied by the concomitant evolution of CENP-A and the associated kinetochore proteins (Talbert et al., 2004). Functional incompatibilities between centromeres result in uniparental genome elimination in interspecies hybrids (Ravi and Chan, 2010; Sanei et al., 2011). The divergent nature of centromeres is proposed to be a driving force for speciation (Henikoff et al., 2001; Malik and Henikoff, 2009).

Asexual organisms, by virtue of inter- and intra-chromosomal rearrangements, diversify into species clusters that are distinct in genotype and morphology (Barraclough et al., 2003). These genotypic differences include changes in both chromosomal organization and number. Centromere function is directly related to karyotype stabilization following a change in chromosome number. Rearrangements in the form of telomere–telomere fusions and nested chromosome insertions (NCIs), wherein an entire donor chromosome is ‘inserted’ into or near the centromere of a non-homologous recipient chromosome, are among the major sources of chromosome number reduction (Lysak, 2014). Such events often result in the formation of dicentric chromosomes that are subsequently stabilized by breakage-fusion-bridge cycles (McClintock, 1941) or via inactivation of one centromere through different mechanisms (Han et al., 2009; Sato et al., 2012). Well-known examples of telomere–telomere fusions include the formation of extant human chromosome 2 by fusion of two ancestral chromosomes (Yunis and Prakash, 1982; IJdo et al., 1991), the reduction in karyotype observed within members of the Saccharomycotina such as Candida glabrata, Vanderwaltozyma polyspora, Kluyveromyces lactis, and Zygosaccharomyces rouxii (Gordon et al., 2011), and the exchange of chromosomal arms seen in plants and fungi (Schubert and Lysak, 2011; Sun et al., 2017). NCIs have predominantly shaped karyotype evolution in grasses (Murat et al., 2010). Reduction of chromosome number by centromere loss has also been reported (Gordon et al., 2011).

To investigate whether centromere breakage can be a natural source of karyotype diversity in closely related species, we sought to identify centromeres in a group of Malassezia yeast species that exhibit variation in chromosome number. Malassezia species are lipid-dependent basidiomycetous fungi that are naturally found as part of the animal skin microbiome (Theelen et al., 2018). At present, the Malassezia genus includes 18 species divided into three clades: A, B, and C. These species also have unusually compact genomes of less than 9 Mb, organized into six to nine chromosomes as revealed by electrophoretic karyotyping of some of these species (Boekhout and Bosboom, 1994; Boekhout et al., 1998; Wu et al., 2015). Fungemia-associated species such as Malassezia furfur belong to Clade A. Clade B includes common inhabitants of human skin that are phylogenetically clustered into two subgroups, namely Clade B1 that contains Malassezia globosa and Malassezia restricta and Clade B2 that contains Malassezia sympodialis and related species. Clade C includes Malassezia slooffiae and Malassezia cuniculi, which diverged earlier from a Malassezia common ancestor (Wu et al., 2015; Lorch et al., 2018).

Besides humans, Malassezia species have been detected on the skin of other animals. For example, M. slooffiae was isolated from cows and goats, M. equina from horses, M. brasiliensis and M. psittaci from parrots, and the cold-tolerant species M. vespertilionis from bats (Lorch et al., 2018; Theelen et al., 2018). In addition, culture-independent studies of fungi from environmental samples showed that Malassezia species that are closely related to those found on human skin were also detected in diverse niches, such as deep-sea vents, soil invertebrates, hydrothermal vents, corals, and Antarctic soils (Amend, 2014). More than ten Malassezia species have been detected as a part of the human skin microbiome (Findley and Grice, 2014). The human skin commensals such as M. globosa, M. restricta, and M. sympodialis have been associated with dermatological conditions such as dandruff/seborrheic dermatitis, atopic dermatitis, and folliculitis (Theelen et al., 2018). Recent reports implicate M. restricta in conditions such as Crohn’s disease and M. globosa in the progression of pancreatic cancer (pancreatic ductal adenocarcinoma) (Aykut et al., 2019; Limon et al., 2019). Elevated levels of Malassezia species and the resulting inflammatory host response have been implicated in both of these disease states. The nature of genomic rearrangements in each species may influence its ability to adapt and cause disease in a specific host niche. Thus, studying the mechanisms of karyotype evolution is an important step towards understanding the evolution of the Malassezia species complex.

Kinetochore proteins serve as useful tools in the identification of centromeres because of their centromere-exclusive localization. CENP-A replaces histone H3 in the centromeric nucleosomes. This has been shown as a reduction in histone H3 levels at the centromeres in Candida lusitaniae (Kapoor et al., 2015) and in a human neocentromere (Lo et al., 2001). These CENP-A nucleosomes act as a foundation to recruit CENP-C, the KMN (KNL1C-MIS12C-NDC80C) network, and other kinetochore proteins (Musacchio and Desai, 2017).

In this study, we experimentally validated all of the eight centromeres of M. sympodialis using the Mtw1 protein (Mis12 in S. pombe), a subunit of the KMN complex, as the kinetochore marker. The Mis12 complex proteins are evolutionarily conserved outer kinetochore proteins that link the chromatin-associated inner kinetochore proteins to the microtubule-associated outer kinetochore proteins. Members of the Mis12 complex localize to centromeres in other organisms (Goshima et al., 1999; Goshima et al., 2003; Westermann et al., 2003; Roy et al., 2011). Recent studies suggest that the protein domains associated with the Mis12 complex members are exclusive to kinetochore proteins and are not detected in any other proteins, making them attractive tools for identifying centromere sequences (Tromer et al., 2019). Using the features of centromeres of M. sympodialis and newly generated chromosome-level genome assemblies, we predicted centromeres in related Malassezia species carrying seven, eight, or nine chromosomes, and experimentally validated the centromere identity in representative species of each karyotype, each belonging to a different Malassezia clade. We employed gene synteny conservation across these centromeres to understand their transitions from an inferred ancestral state of nine chromosomes. On the basis of our results, we propose that centromere loss by two distinct mechanisms drives karyotype diversity.

## Results

### Chromosome number varies in the Malassezia species complex

Previous reports that are based on pulsed-field gel electrophoresis (PFGE) have suggested that chromosome number varies within the Malassezia species complex. The early diverged species M. slooffiae of Clade C was reported to have nine chromosomes (Boekhout et al., 1998). Clade B Malassezia species are reported to have nine (M. globosa and M. restricta), eight (M. sympodialis), or six chromosomes (M. pachydermatis). Among the Clade A species, M. obtusa and M. furfur CBS14141 were both reported to have seven chromosomes (Boekhout and Bosboom, 1994; Zhu et al., 2017). A high-quality reference genome is a prerequisite to understanding the rearrangements associated with chromosome number variation. In addition, such a reference genome will also assist in resolving ambiguities in PFGE-based estimates of chromosome number when similar-sized chromosomes are present. Complete genome assemblies were not available for many of the species with reported numbers of chromosomes. To obtain better-assembled reference genomes, we sequenced the genomes of M. slooffiae and M. globosa as representatives of the nine-chromosome state, and of M. furfur as a representative of the seven-chromosome state, using PacBio SMRT sequencing technology (Figure 1, Figure 1—figure supplement 1).

![Figure 1.](https://cdn.elifesciences.org/articles/53944/elife-53944-fig1-v2.jpg)

**Figure 1.:** The genomes of (A) M. globosa, (B) M. slooffiae, and (C) M. furfur were sequenced and assembled in this study, whereas the genome assembly of (D) M. sympodialis was reported earlier (Zhu et al., 2017) and is shown for comparison. In each panel, bar plots represent the assembled chromosomes of the indicated Malassezia species, with the telomeres and the ribosomal DNA (rDNA) marked as dark gray and blue bars, respectively. Telomere-repeat motifs are shown at the 5′- and 3′-ends of the Chr1 in each species. Electrophoretic karyotypes of M. globosa (Mg) and M. sloffiiae (Msl), are shown in (A) and (B), respectively, with chromosome sizes estimated from the genome assembly. Chromosomes of Saccharomyces cerevisiae (Sc) served as size markers. The chromosome containing the rDNA (marked with an ‘r’), in M. globosa, co-migrates with Chr3. This was assessed by chromoblot hybridization using unique sequences from Chr3, Chr4, Chr5, and Chr6 as probes (regions indicated by red arrowheads). Chromosomes of similar size (denoted in red) migrate together in the gel and appear as a doublet band (i.e. MgChr3–MgChr5, MslChr2–MslChr3, and MslChr5–MslChr6).

![Figure 1—figure supplement 1.](https://cdn.elifesciences.org/articles/53944/elife-53944-fig1-figsupp1-v2.jpg)

The M. globosa genome was completely assembled into nine contigs with telomeres on both ends (BioSample accession SAMN10720087). We validated these contigs by matching each band on the pulsed-field gel with the contig sizes from the genome assembly, and further confirmed these by chromoblot analysis following PFGE. This analysis shows that chromosome 5 contains the rDNA locus and migrates further than the expected size of 902 kb, as a diffuse ensemble of different sizes along with chromosome 3 (Figure 1A). The assembled genome of M. slooffiae has 14 contigs of which nine contigs have telomeres on both ends, indicative of nine chromosomes (BioSample accession SAMN10720088). Each of the nine contigs could be assigned to the bands observed in the pulsed-field gel (Figure 1B). For M. furfur, the final genome assembly consisted of seven contigs with telomeres on both ends and matched the expected chromosome sizes obtained from an earlier PFGE analysis of CBS14141 (Figure 1C). The complete genome assembly of M. sympodialis reported earlier is distributed into eight chromosomes with telomere repeats on both ends (Figure 1D), and serves as a representative of an eight-chromosome state in this study.

Changes in chromosome number are always associated with the birth or loss of centromeres, which stabilizes the karyotype in organisms with monocentric chromosomes. To understand the transitions between these different karyotypic states observed in the Malassezia species complex, we sought to validate centromeres in species representative of each karyotype experimentally.

### Kinetochores cluster and localize to the nuclear periphery in M. sympodialis

Organisms that have point centromeres possess Ndc10, Cep3, and Ctf13 of the CBF3 complex, a cognate protein complex that is specific to point centromeres. None of these point-centromere-specific proteins could be detected in M. sympodialis. However, we could detect homologs of CENP-A, CENP-C, and most of the outer kinetochore proteins in the genome of M. sympodialis (Figure 2A and Figure 2—figure supplement 1). We functionally expressed an N-terminally GFP-tagged Mtw1 protein (Protein ID: SHO76526.1) from its native promoter, and the expression of the fusion protein was confirmed by western blotting (Figure 2B). Upon staining with anti-GFP antibodies and DAPI (4′,6-diamidino-2-phenylindole), we were able to detect punctate localization of Mtw1 at the nuclear periphery (Figure 2C), consistent with the clustered kinetochore localization observed in other yeasts (Goshima et al., 1999; Euskirchen, 2002; Roy et al., 2011). Live-cell images of MSY001 (GFP-MTW1) cells revealed that the kinetochores (GFP-Mtw1) remained clustered throughout the cell cycle, starting from unbudded G1 cells in interphase to large-budded cells in mitosis (Figure 2D).

![Figure 2.](https://cdn.elifesciences.org/articles/53944/elife-53944-fig2-v2.jpg)

**Figure 2.:** (A) Schematic of the kinetochore organization of M. sympodialis. Gray boxes indicate proteins absent in M. sympodialis. The outer kinetochore protein Mtw1 (a component of Mis12C) served as the kinetochore marker in the present study. (B) Line diagram representation of Mtw1 tagged with GFP at the N- terminus. Immunoblot analysis of whole-cell lysates prepared from the untagged M. sympodialis strain (ATCC42132) and from GFP-Mtw1 expressing cells (MSY001) probed with anti-GFP antibodies and anti-PSTAIRE antibodies. PSTAIRE served as a loading control. Relative intensity values normalized to PSTAIRE are indicated below each lane. (C) Logarithmically grown MSY001 cells expressing GFP-Mtw1 were fixed and stained with DAPI (blue) and anti-GFP antibodies (pseudo-colored in red). Scale bar, 2.5 µm. (D) Cell cycle stage-specific localization dynamics of GFP-Mtw1. Scale bar, 2.5 µm.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/53944/elife-53944-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** Putative homologs of the indicated proteins in M. sympodialis were identified by BLAST analysis using corresponding protein sequences of C. neoformans as the query. An asterisk (*) indicates cases where corresponding protein sequences from Ustilago maydis were used as query. To detect proteins of the CBF3 complex, protein sequences of Ndc10, Cep3, and Ctf13 from S. cerevisiae were used as query. ‘n.d.’ indicates homolog not detected.

### Mtw1 is localized to a single region at the GC minima of each M. sympodialis chromosome

Having identified Mtw1 as an authentic kinetochore protein, we performed ChIP-sequencing using the GFP-Mtw1 expressing strain of M. sympodialis (MSY001). Mapping the reads to the reference genome of M. sympodialis strain ATCC42132 (Zhu et al., 2017) identified one significantly enriched locus on each of the eight chromosomes (Figure 3A). The lengths of the Mtw1-enriched centromere regions identified from the ChIP-seq analysis ranged from 3167 bp to 5143 bp with an average length of 4165 bp (Table 1). However, the region of maximum Mtw1 enrichment on each chromosome (based on the number of sequenced reads aligned) mapped to the intergenic region harboring the GC trough (approximately 1 kb long), which was previously predicted to be the centromeres of M. sympodialis (Figure 3B) (Zhu et al., 2017). The regions of Mtw1 enrichment span beyond the core centromeres and include active genes located proximal to these troughs (Figure 3B, Figure 3—figure supplement 1A). However, these open reading frames (ORFs) do not show consensus features such as the orientation of transcription or functional classification. We validated this enrichment by ChIP-qPCR analysis with primers homologous to the predicted centromeres compared to those homologous to a control region distant from the centromere (Figure 3—figure supplement 1B).

![Figure 3.](https://cdn.elifesciences.org/articles/53944/elife-53944-fig3-v2.jpg)

**Figure 3.:** (A) GFP-Mtw1 ChIP-seq reads were mapped to each chromosome. The x-axis indicates chromosomal coordinates (in kb) and the y-axis indicates read depth. ‘Input’, reads from total DNA; ‘IP,’ reads from immunoprecipitated sample; CEN, Mtw1-enriched regions derived by subtracting input reads from those of the IP sample (peak values 0–2500). Additional peaks observed in both IP and input tracks on Chr5 are from the rDNA locus. (B) A 13 kb-window of the Mtw1 enrichment profile (CEN, represented as peaks and heat-map in two different tracks, red) plotted along with the GC content (%GC, blue) and regions of transcription (RNA-seq, green). Numbers in the topmost track in every panel indicate chromosomal coordinates (in kb). The scales for the y-axis are as follows: CEN (0–8000), %GC (0–75), RNA-seq reads (0–1500). Gray arrows in each panel indicate predicted ORFs based on RNA-seq data with arrowheads indicating the direction of transcription of the corresponding gene, also marked as ‘+’ and ‘–’ in the axis label. (C) Fold difference in Mtw1 and histone H3 enrichment at CEN8, as compared to a non-centromeric control region (190 kb away on the right of CEN1) by qPCR analysis. Schematic of a 4-kb region of Chr8 with the CEN8 core (yellow box) is depicted below the graph. Blue lines indicate regions assayed by PCR: core-region corresponding to the GC trough; L1 and R1, 750 bp away from the core; L2, 1500 bp away from the core; and a non-centromeric control region (190 kb away from centromere in Chr1). The x-axis indicates regions across the CEN8 probed by PCR and the y-axis indicates fold difference in the enrichment of Mtw1 and histone H3 as compared to the control region. Error bars indicate standard deviations (SD). Values from three experiments, each performed with three technical replicates, were used to generate the plot. (D) Logo of the consensus DNA sequence identified from M. sympodialis centromeres, graphically represented with the size of the base corresponding with the frequency of occurrence.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/53944/elife-53944-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Normalized read counts (RPKM) for transcripts from ORFs flanking the centromere as compared with the genome average RPKM value calculated from RNA-seq data of M. sympodialis (ATCC42132). The x-axis represents ORFs labeled L1–L5 and R1–R5, with L1 and R1 being proximal to the GC trough of the centromere. The genome average considered for comparison is labeled as global. The y-axis represents Log2 RPKM values. (B) ChIP-qPCR assays validating the enrichment of Mtw1 at the centromeres identified by ChIP-sequencing analysis. The x-axis indicates individual CEN regions assayed with primers mapping to the chromosomal GC troughs (see Supplementary file 1 for primer sequences) and the y-axis indicates enrichment of Mtw1 over a centromere-unlinked control region as ‘normalized % input immunoprecipitated’. Values from three experiments, each performed with three technical replicates, were used to generate the plot. Error bars indicate standard deviations (SD).

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/53944/elife-53944-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** (A) The genome of M. sympodialis was scanned for matches to the 12-bp AT-rich motif using a 500 bp sliding window. Hit counts (y-axis) were plotted against the chromosomal coordinates (x-axis, in kb). Red asterisks near the line corresponding to maximum enrichment in every chromosome mark the regions predicted as centromeres. (B) Comparison of the maximum motif counts in a 500-bp window in each M. sympodialis chromosome (y-axis) estimated with the position weight matrix (PWM) of the 12 bp motif (blue bars, labeled real) and a scrambled version of the matrix (orange bars, labeled shuffled). The x-axis indicates individual chromosomes in M. sympodialis. (C) A dot-plot generated by plotting sequences that include 5 kb flanking the Mtw1-enriched regions in M. sympodialis against themselves is depicted. The coordinates of regions used in M. sympodialis are: CEN1, 781716–791716; CEN2, 350852–360852; CEN3, 232777–242777; CEN4, 413320–423320; CEN5, 120251–130251; CEN6, 97796–107796; CEN7, 426611–436611; and CEN8, 19905–29905.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/53944/elife-53944-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** The sequences corresponding to the Mtw1-enriched regions in Chr1 (with the AT-rich core region highlighted in pink) are taken as being representative of M. sympodialis centromeres. The sequences corresponding to the 12-bp motif shown in Figure 3D are highlighted. Red and blue boxes highlight the forward and reverse orientation of motif occurrence.

**Table 1.**
 Coordinates of centromeres and their GC content in M. sympodialis.Coordinates and length of Mtw1-enriched regions in comparison with those of the core centromeres in M. sympodialis.


<table>
  <thead>
    <tr>
      <th rowspan="3">Chromosome number</th>
      <th colspan="4">Core centromere</th>
      <th colspan="3">Full-length centromere</th>
    </tr>
    <tr>
      <th colspan="2">Coordinates</th>
      <th rowspan="2">Length (bp)</th>
      <th rowspan="2">%GC</th>
      <th colspan="2">Coordinates</th>
      <th rowspan="2">Length (bp)</th>
    </tr>
    <tr>
      <th>Start</th>
      <th>End</th>
      <th>Start</th>
      <th>End</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>786,541</td>
      <td>787,061</td>
      <td>520</td>
      <td>16.4</td>
      <td>784,833</td>
      <td>788,599</td>
      <td>3767</td>
    </tr>
    <tr>
      <td>2</td>
      <td>355,760</td>
      <td>355,841</td>
      <td>81</td>
      <td>20</td>
      <td>354,218</td>
      <td>357,486</td>
      <td>3269</td>
    </tr>
    <tr>
      <td>3</td>
      <td>237,534</td>
      <td>238,686</td>
      <td>1152</td>
      <td>15.6</td>
      <td>235,615</td>
      <td>239,940</td>
      <td>4326</td>
    </tr>
    <tr>
      <td>4</td>
      <td>418,202</td>
      <td>418,728</td>
      <td>526</td>
      <td>15.2</td>
      <td>415,985</td>
      <td>420,656</td>
      <td>4672</td>
    </tr>
    <tr>
      <td>5</td>
      <td>125,056</td>
      <td>125,220</td>
      <td>164</td>
      <td>18</td>
      <td>123,219</td>
      <td>127,284</td>
      <td>4066</td>
    </tr>
    <tr>
      <td>6</td>
      <td>101,950</td>
      <td>102,502</td>
      <td>552</td>
      <td>14.4</td>
      <td>100,342</td>
      <td>105,251</td>
      <td>4910</td>
    </tr>
    <tr>
      <td>7</td>
      <td>431,542</td>
      <td>431,987</td>
      <td>445</td>
      <td>13.2</td>
      <td>430,028</td>
      <td>433,194</td>
      <td>3167</td>
    </tr>
    <tr>
      <td>8</td>
      <td>24,694</td>
      <td>25,564</td>
      <td>870</td>
      <td>18.4</td>
      <td>22,334</td>
      <td>27,476</td>
      <td>5143</td>
    </tr>
  </tbody>
</table>

_Genome average GC content (in %): 58.5._

### Histone H3 is depleted at the core centromere with active genes at the pericentric regions in M. sympodialis

The presence of CENP-A nucleosomes at the kinetochore should result in reduced histone H3 enrichment at the centromeres when compared to a non-centromeric locus. To test this, we performed ChIP with anti-histone H3 antibodies and analyzed the immunoprecipitated (IP) DNA by qPCR. As compared to a control ORF region that is unlinked to the centromere (190 kb away from CEN1), the pericentric regions flanking the core centromere showed a marginal reduction in histone H3 enrichment, which was further reduced at the core, that maps to the GC trough with the highest enrichment of the kinetochore protein Mtw1. That the core centromere region showing the maximum depletion of histone H3 coincided with the regions most enriched with Mtw1 further supports that histone H3, in these regions, is possibly replaced by its centromere-specific variant CENP-A (Figure 3C).

### The short regional centromeres of M. sympodialis are enriched with a 12-bp-long AT-rich consensus sequence motif

To understand the features of M. sympodialis centromeres, we analyzed the centromere DNA sequences for the presence of consensus motifs or structures such as inverted repeats. PhyloGibbs-MP (Siddharthan et al., 2005; Siddharthan, 2008) predicted a 12-bp-long AT-rich motif common to all of the centromere sequences of M. sympodialis (Figure 3D). We swept the PWM from the PhyloGibbs-MP output across each chromosome of M. sympodialis and counted the number of motif predictions in a sliding 500-bp window, sliding by 100 bp at a time. Sites with log-likelihood-ratio (LLR) of >7.5 were counted as motif predictions. The LLR is the natural logarithm of the ratio of the likelihood of the12-bp substring arising as a sample from the PWM to the likelihood of it being generic ‘background’. In each case, the global peak coincides with the centromere (Figure 3—figure supplement 2A). In each chromosome, the centromere region shows between 7 and 13 motif matches, whereas no other 500-bp window shows more than three matches. This suggests that the AT-rich motif is more enriched at the centromeres than at any other region in the M. sympodialis genome (Figure 3—figure supplement 2A). To ensure that this is not an artifact of the GC-poor nature of the centromere, we repeated the analysis with a synthetic shuffled PWM, created by scrambling the order of the columns of the original PWM (that is, scrambling the positions in the motif while keeping the corresponding weight vectors the same). This shuffled motif showed more matches in the centromeres than are seen in the non-centromeric genomic sequence, but significantly fewer than are seen in the authentic centromeric sequences of most chromosomes (Figure 3—figure supplement 2B). A dot-plot analysis was performed to detect the presence of any direct or inverted-repeat structure associated with the centromeres in M. sympodialis. Analysis of all of the centromere sequences and 5-kb flanking sequences using SyMap confirmed the lack of direct/inverted repeat structures (Figure 3—figure supplement 2C).

In the absence of any centromere-exclusive DNA sequence, the unique and distinguishing features of centromere regions in M. sympodialis are an AT-rich core region of <1 kb (average AT content of 78% as compared to the genome average of 41.5%) that is enriched with the 12-bp motif (Figure 3—figure supplement 3) within a kinetochore protein-bound region of 3–5 kb. As expected, the kinetochore-bound region contains a reduced level of histone H3.

### Centromeres in M. furfur, M. slooffiae, and M. globosa map to chromosomal GC minima

Using the unique centromere features identified in M. sympodialis, we predicted one centromere locus on each of the seven M. furfur chromosomes, and these all map to chromosomal GC troughs (Figure 4—figure supplement 1A, Table 2). We also predicted the centromeres in M. slooffiae, M. globosa, and M. restricta, each of which contains nine chromosomes (Figure 4—figure supplement 1B–D, Table 2). Each of the predicted centromere regions is enriched with the 12-bp AT-rich motif identified in M. sympodialis centromere sequences as compared to other regions in the genomes (Figure 4—figure supplement 2).

**Table 2.**
 Coordinates, length, and GC content (in %) of the centromeres predicted in M. furfur, M. globosa, M. slooffiae, and M. restricta.


<table>
  <thead>
    <tr>
      <th rowspan="2"></th>
      <th rowspan="2">Chr./scaffold</th>
      <th rowspan="2">CEN</th>
      <th colspan="4">Core centromere</th>
      <th rowspan="2">% GC genome</th>
    </tr>
    <tr>
      <th>Start</th>
      <th>End</th>
      <th>Length (bp)</th>
      <th>% GC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="7">M. furfur CBS14141</td>
      <td>Chr1</td>
      <td>CEN1</td>
      <td>2,850,135</td>
      <td>2,850,402</td>
      <td>268</td>
      <td>15.7</td>
      <td rowspan="7">64.9</td>
    </tr>
    <tr>
      <td>Chr2</td>
      <td>CEN2</td>
      <td>68,763</td>
      <td>68,931</td>
      <td>168</td>
      <td>15.4</td>
    </tr>
    <tr>
      <td>Chr3</td>
      <td>CEN3</td>
      <td>717,557</td>
      <td>718,084</td>
      <td>528</td>
      <td>22.9</td>
    </tr>
    <tr>
      <td>Chr4</td>
      <td>CEN4</td>
      <td>155,897</td>
      <td>156,301</td>
      <td>405</td>
      <td>18.3</td>
    </tr>
    <tr>
      <td>Chr5</td>
      <td>CEN5</td>
      <td>342,885</td>
      <td>343,372</td>
      <td>488</td>
      <td>21.5</td>
    </tr>
    <tr>
      <td>Chr6</td>
      <td>CEN6</td>
      <td>86,112</td>
      <td>86,832</td>
      <td>721</td>
      <td>27</td>
    </tr>
    <tr>
      <td>Chr7</td>
      <td>CEN7</td>
      <td>56,894</td>
      <td>57,339</td>
      <td>445</td>
      <td>20.9</td>
    </tr>
    <tr>
      <td rowspan="9">M. globosa CBS7966</td>
      <td>Chr1</td>
      <td>CEN1</td>
      <td>981,894</td>
      <td>982,242</td>
      <td>349</td>
      <td>17.7</td>
      <td rowspan="9">52.05</td>
    </tr>
    <tr>
      <td>Chr2</td>
      <td>CEN2</td>
      <td>362,480</td>
      <td>362,807</td>
      <td>327</td>
      <td>25.9</td>
    </tr>
    <tr>
      <td>Chr3</td>
      <td>CEN3</td>
      <td>219,647</td>
      <td>220,121</td>
      <td>474</td>
      <td>27.2</td>
    </tr>
    <tr>
      <td>Chr4</td>
      <td>CEN4</td>
      <td>152,635</td>
      <td>152,994</td>
      <td>359</td>
      <td>18.3</td>
    </tr>
    <tr>
      <td>Chr5</td>
      <td>CEN5</td>
      <td>215,437</td>
      <td>215,595</td>
      <td>158</td>
      <td>17</td>
    </tr>
    <tr>
      <td>Chr6</td>
      <td>CEN6</td>
      <td>464,007</td>
      <td>464,114</td>
      <td>107</td>
      <td>32.4</td>
    </tr>
    <tr>
      <td>Chr7</td>
      <td>CEN7</td>
      <td>736,701</td>
      <td>737,015</td>
      <td>314</td>
      <td>18.1</td>
    </tr>
    <tr>
      <td>Chr8</td>
      <td>CEN8</td>
      <td>59,472</td>
      <td>59,817</td>
      <td>345</td>
      <td>19.7</td>
    </tr>
    <tr>
      <td>Chr9</td>
      <td>CEN9</td>
      <td>114,080</td>
      <td>114,535</td>
      <td>455</td>
      <td>23.5</td>
    </tr>
    <tr>
      <td rowspan="9">M. slooffiae CBS7956</td>
      <td>Chr1</td>
      <td>CEN1</td>
      <td>138,919</td>
      <td>139,465</td>
      <td>547</td>
      <td>26</td>
      <td rowspan="9">66.31</td>
    </tr>
    <tr>
      <td>Chr2</td>
      <td>CEN2</td>
      <td>132,717</td>
      <td>133,193</td>
      <td>477</td>
      <td>23.1</td>
    </tr>
    <tr>
      <td>Chr3</td>
      <td>CEN3</td>
      <td>367,665</td>
      <td>368,177</td>
      <td>513</td>
      <td>23.8</td>
    </tr>
    <tr>
      <td>Chr4</td>
      <td>CEN4</td>
      <td>130,942</td>
      <td>131,501</td>
      <td>560</td>
      <td>27</td>
    </tr>
    <tr>
      <td>Chr5</td>
      <td>CEN5</td>
      <td>183,442</td>
      <td>183,981</td>
      <td>540</td>
      <td>28.5</td>
    </tr>
    <tr>
      <td>Chr6</td>
      <td>CEN6</td>
      <td>411,984</td>
      <td>412,552</td>
      <td>569</td>
      <td>27.4</td>
    </tr>
    <tr>
      <td>Chr7</td>
      <td>CEN7</td>
      <td>54,307</td>
      <td>54,889</td>
      <td>583</td>
      <td>30</td>
    </tr>
    <tr>
      <td>Chr8</td>
      <td>CEN8</td>
      <td>497,637</td>
      <td>498,149</td>
      <td>513</td>
      <td>24</td>
    </tr>
    <tr>
      <td>Chr9</td>
      <td>CEN9</td>
      <td>55,948</td>
      <td>56,479</td>
      <td>532</td>
      <td>26.7</td>
    </tr>
    <tr>
      <td rowspan="9">M. restricta CBS877</td>
      <td>Chr1</td>
      <td>CEN1</td>
      <td>347,813</td>
      <td>348,406</td>
      <td>594</td>
      <td>29.7</td>
      <td rowspan="9">55.73</td>
    </tr>
    <tr>
      <td>Chr2</td>
      <td>CEN2</td>
      <td>87,190</td>
      <td>87,806</td>
      <td>617</td>
      <td>33.3</td>
    </tr>
    <tr>
      <td>Chr3</td>
      <td>CEN3</td>
      <td>1,101,494</td>
      <td>1,102,083</td>
      <td>590</td>
      <td>33.9</td>
    </tr>
    <tr>
      <td>Chr4</td>
      <td>CEN4</td>
      <td>754,356</td>
      <td>754,989</td>
      <td>634</td>
      <td>34.2</td>
    </tr>
    <tr>
      <td>Chr5</td>
      <td>CEN6</td>
      <td>621,177</td>
      <td>621,863</td>
      <td>687</td>
      <td>31.7</td>
    </tr>
    <tr>
      <td>Chr6</td>
      <td>CEN7</td>
      <td>390,657</td>
      <td>391,286</td>
      <td>630</td>
      <td>35.1</td>
    </tr>
    <tr>
      <td>Chr7</td>
      <td>CEN8</td>
      <td>362,842</td>
      <td>363,381</td>
      <td>540</td>
      <td>32</td>
    </tr>
    <tr>
      <td>Chr8</td>
      <td>CEN9</td>
      <td>117,021</td>
      <td>117,603</td>
      <td>583</td>
      <td>32.8</td>
    </tr>
    <tr>
      <td>Chr9</td>
      <td>CENR</td>
      <td>70,306</td>
      <td>70,913</td>
      <td>608</td>
      <td>36.3</td>
    </tr>
  </tbody>
</table>

To validate the centromeric loci in M. furfur experimentally, we functionally expressed the centromeric histone H3 variant CENP-A with a 3xFLAG tag at the C-terminus (Figure 4A). We performed ChIP in strain MF001 (CENP-A-3xFLAG) and analyzed immunoprecipitated DNA by qPCR using primers specific to each of the seven predicted centromeres and to a centromere-unlinked control locus 1.3 Mb away from CEN1. Enrichment of CENP-A at all seven centromeres over the control locus confirmed that the predicted regions are indeed centromeres in M. furfur CBS14141 (Figure 4B,C).

![Figure 4.](https://cdn.elifesciences.org/articles/53944/elife-53944-fig4-v2.jpg)

**Figure 4.:** (A) Schematic of epitope tagging of CENP-A with 3xFLAG at the C-terminus. (Bottom) Immunoblot analysis using whole-cell lysates prepared from the untagged wild-type M. furfur (CBS14141) cells and CENP-A-3xFLAG expressing cells (MF001) probed with anti-FLAG antibodies and anti-PSTAIRE antibodies. PSTAIRE served as the loading control. (B) Abundance of CENP-A at each of the predicted M. furfur centromeres by qPCR analysis of DNA immunoprecipitated with anti-FLAG affinity gel in MF001 cells expressing CENP-A-3xFLAG. The x-axis indicates individual CEN regions assayed with primers that are homologous to the GC troughs on each chromosome that were predicted to be centromeres (see Supplementary file 1 for primer sequences). The non-centromeric control sequence maps to a region 1.3 Mb away from predicted CEN1. The y-axis indicates enrichment of CENP-A estimated as the percentage of input immunoprecipitated. (C) Abundance of CENP-A across MfCEN7 by ChIP-qPCR analysis in MF001 cells. A schematic representation of a 2-kb region is shown below the graph. The yellow bar indicates the centromere core of CEN7 corresponding to the GC trough. Blue bars indicate regions analyzed by qPCR: L1 and R1, which are 750 bp away from the centromere core. ‘Control’ refers to a region 1.3 Mb away from CEN1. CENP-A enrichment is plotted along the y-axis as the percentage of input immunoprecipitated. (D, E) Comparison of the relative abundance of histone H3 compared to histone H4 at the predicted centromeres to a non-centromeric control locus in M. slooffiae (D) and M. globosa (E), respectively. Enrichment was estimated as the percentage of input immunoprecipitated with histone H3 and histone H4 antibodies and their ratio is plotted as relative enrichment (y-axis). The x-axis indicates centromeres in each species and these were assayed with primers homologous to GC troughs (i.e. predicted centromeres) in each chromosome (see Supplementary file 1 for primer sequences). The control region that is unlinked to the centromere corresponds to a locus 630 kb away from CEN1 in M. slooffiae and 416 kb away from CEN2 in M. globosa. (F) The relative abundance of histone H3 compared to histone H4 across MslCEN1 as determined by qPCR analysis of the DNA immunoprecipitated using histone H3 and histone H4 antibodies. A schematic of the MslCEN1 locus is shown below the graph. The yellow bar indicates the CEN1 core region corresponding to the GC trough. Blue bars indicate regions analyzed by qPCR: L1 and L2 map to regions 750 bp and 1.5 kb to the left of the CEN1 core; R1 maps to a region 750 bp to the right of the CEN1 core. The control region corresponds to a locus 630 kb away from the CEN1 core. The ratio of enrichment of histone H3 to that of histone H4 is plotted as the relative enrichment (y-axis). (G) The relative abundance of histone H3 compared to histone H4 across MgCEN2 by qPCR analysis of the DNA immunoprecipitated using histone H3 and histone H4 antibodies. A schematic of a 5-kb region containing MgCEN2 is shown below the graph. The yellow bar indicates the CEN2 core region corresponding to the GC trough. Blue bars indicate regions analyzed by qPCR: L1 and L2 indicate regions 750 bp and 1.5 kb to the left of the CEN2 core; R1 and R2 indicate regions 750 bp and 1.5 kb to the right of the CEN2 core. The control region corresponds to a locus 416 kb away from the CEN2 core. The ratio of enrichment of histone H3 to that of histone H4 is plotted as the relative enrichment (y-axis). Values from three experiments, each performed with three technical replicates, were used to generate the plots in panels (B–G). Error bars indicate standard deviations (SD). Statistical significance was tested by one-way ANOVA: *, significant at p<0.05, *** , significant at p<0.001.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/53944/elife-53944-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** (A–D) Graphs indicating the GC content (red lines) and GC3 content (black lines) of each chromosome of M. furfur, M. slooffiae, M. globosa, and M. restricta. The GC3 content is measured by estimating the G or C content at the third position in each codon of all genes across a chromosome (Lynch et al., 2010; Zhu et al., 2017). Position of putative centromeres mapping to chromosomal GC minima are marked in blue. The x-axis indicates chromosomal coordinates in Mb.

![Figure 4—figure supplement 2.](https://cdn.elifesciences.org/articles/53944/elife-53944-fig4-figsupp2-v2.jpg)

**Figure 4—figure supplement 2.:** (A–D) The genomes of M. furfur, M. slooffiae, M. globosa, and M. restricta were scanned for matches to the 12-bp AT-rich motif using a 500-bp sliding window. Hit counts (y-axis) were plotted against the chromosomal coordinates (x-axis, in kb) for each of the above species. Red asterisks near the line corresponding to maximum enrichment in every chromosome or scaffold mark the regions predicted as centromeres in each species.

Given the lack of genetic manipulation methods for M. slooffiae and M. globosa, we tested the enrichment of histone H3 at the predicted centromeres in these two species. All of the nine centromeric loci in these two species contained a reduced histone H3 level when compared to a control locus that was unlinked to centromeres (Figure 4D,E). Furthermore, upon analyzing the enrichment profile at one centromere (CEN1) in M. slooffiae, we observed a reduction in the enrichment levels of histone H3 at the GC troughs as compared to the flanking regions (Figure 4F). In the case of M. globosa, the regions spanning a centromere (CEN2) also depicted a similar reduction in the histone H3 levels (Figure 4G). Taken together, the significant reduction in the histone H3 levels at the predicted centromeres, indicative of the presence of CENP-A, suggests that these putative centromere regions are indeed bona fide centromeres in these species.

### Centromere loss by breakage resulted in chromosome number reduction in M. sympodialis

Synteny of genes across centromeres is largely conserved in closely related species (Byrne and Wolfe, 2005; Padmanabhan et al., 2008; Yadav et al., 2018b). To understand the transition between different chromosome number states, we analyzed the conservation of gene synteny across centromeres in these species. By mapping gene synteny at the centromeres of M. globosa and M. slooffiae (each with nine chromosomes), compared with that of M. sympodialis (containing eight chromosomes), we found complete gene synteny conservation in eight of the nine centromeres (Figure 5A,B). Thus, syntenic regions of all eight M. sympodialis centromeres are present in the genomes of M. globosa and M. slooffiae. In the case of M. restricta, seven putative centromeres are completely syntenic with M. sympodialis centromeres and one centromere retained partial gene synteny (Table 3). However, no gene synteny conservation was observed at the centromeres of Chr2 in M. globosa, Chr5 in M. slooffiae, or Chr8 in M. restricta (Table 3), indicating the loss of a centromere during the transition from the nine-chromosome state to the eight-chromosome state.

![Figure 5.](https://cdn.elifesciences.org/articles/53944/elife-53944-fig5-v2.jpg)

**Figure 5.:** (A, B) Circos plots depicting the gene synteny blocks that are conserved between M. globosa and M. sympodialis chromosomes and between M. slooffiae and M. sympodialis chromosomes. Tracks from outside to inside represent the positions of centromeres and telomeres, GC content (plotted as blue and red lines indicating GC content below or above genome average, calculated in 0.4-kb non-overlapping windows), and colored connectors indicate regions of conserved gene synteny between the two species. (C, D) Linear chromosome plots depicting syntenic regions between Chr2 of M. globosa and Chr5 of M. slooffiae with chromosomes of M. sympodialis. GC content (in %) is shown as red/blue lines above each chromosome. Circular labels mark the gene synteny breakpoints. The synteny breakpoint at MgCEN2 and MslCEN5 is marked as III. The regions on MsyChr2 and MsyChr4 where the homologs of ORFs flanking the breakpoint are located are marked II and IV, respectively. Labels I and V indicate gene synteny conservation on the other side of the fusion points II and IV on MsyChr2 and MsyChr4 as compared to M. globosa and M. slooffiae chromosomes, respectively. (E, F) Zoomed-in image of the gene synteny breakpoint at MgCEN2 and MslCEN5, representing the conservation of genes flanking these centromeres in M. sympodialis chromosomes at the ORF level.

**Table 3.**
 Synteny of centromeres across all of the Malassezia species analyzed in this study.


<table>
  <thead>
    <tr>
      <th>Clade C</th>
      <th colspan="3">Clade B1</th>
      <th colspan="2">Clade B2</th>
      <th colspan="3">Clade A</th>
    </tr>
    <tr>
      <th>M. slooffiae (9 Chr)</th>
      <th>M. dermatis (8 Chr)</th>
      <th>M. nana (8 Chr)</th>
      <th>M. sympodialis (8 Chr)</th>
      <th>M. globosa (9 Chr)</th>
      <th>M. restricta (9 Chr)</th>
      <th>M. vespertilionis (9 Chr)</th>
      <th>M. japonica (9 Chr)</th>
      <th>M. furfur (7 Chr)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CEN2</td>
      <td>CEN1</td>
      <td>CEN1</td>
      <td>CEN1</td>
      <td>CEN3</td>
      <td>CEN5 partial</td>
      <td>CEN6</td>
      <td>CEN8</td>
      <td>CEN4</td>
    </tr>
    <tr>
      <td>CEN6</td>
      <td>CEN2</td>
      <td>CEN2</td>
      <td>CEN2</td>
      <td>CEN6</td>
      <td>CEN7</td>
      <td>CEN9</td>
      <td>CEN4 partial</td>
      <td>CEN2 partial</td>
    </tr>
    <tr>
      <td>CEN3</td>
      <td>CEN3</td>
      <td>CEN3</td>
      <td>CEN3</td>
      <td>CEN1</td>
      <td>CEN3</td>
      <td>CEN7 partial</td>
      <td>CEN6 partial</td>
      <td>CEN3 partial</td>
    </tr>
    <tr>
      <td>CEN4</td>
      <td>CEN4</td>
      <td>CEN4</td>
      <td>CEN4</td>
      <td>CEN4</td>
      <td>CEN1</td>
      <td>CEN1</td>
      <td>CEN2</td>
      <td>CEN7 partial</td>
    </tr>
    <tr>
      <td>CEN1</td>
      <td>CEN6</td>
      <td>CEN6</td>
      <td>CEN5</td>
      <td>CEN5</td>
      <td>CEN2</td>
      <td>CEN4</td>
      <td>CEN7</td>
      <td>CEN1</td>
    </tr>
    <tr>
      <td>CEN7</td>
      <td>CEN5</td>
      <td>CEN5</td>
      <td>CEN6</td>
      <td>CEN7</td>
      <td>CEN6</td>
      <td>CEN5 partial</td>
      <td>CEN5 partial</td>
      <td>CEN6</td>
    </tr>
    <tr>
      <td>CEN8</td>
      <td>CEN7</td>
      <td>CEN7</td>
      <td>CEN7</td>
      <td>CEN9</td>
      <td>CEN4</td>
      <td>CEN2</td>
      <td>CEN9 partial</td>
      <td>Inactivated</td>
    </tr>
    <tr>
      <td>CEN9</td>
      <td>CEN8</td>
      <td>CEN8</td>
      <td>CEN8</td>
      <td>CEN8</td>
      <td>CEN9</td>
      <td>CEN8</td>
      <td>CEN1</td>
      <td>Inactivated</td>
    </tr>
    <tr>
      <td>CEN5</td>
      <td>BP</td>
      <td>BP</td>
      <td>BP</td>
      <td>CEN2</td>
      <td>CEN8 partial</td>
      <td>CEN3</td>
      <td>CEN3 partial</td>
      <td>CEN5</td>
    </tr>
  </tbody>
</table>

_‘BP’ indicates the presence of a gene synteny break. ‘Inactivated’ indicates centromere inactivation resulting from sequence divergence and erosion of AT-richness._

The GC trough corresponding to MgCEN2/MslCEN5 is flanked by genes that map to MsyChr2 on one arm and MsyChr4 on the other (Figure 5C,D). The centromere region in each of MgChr2 and MslChr5 marks a synteny breakpoint showing no homologous region in the M. sympodialis genome, indicating a loss of this centromere DNA sequence. We also observed that the genes flanking the breakpoint are conserved in M. sympodialis, suggesting that the specific intergenic region was involved (Figure 5E,F). Evidence for the internalization of telomere-adjacent ORFs or for the presence of interstitial telomere repeats that are indicative of telomere–telomere fusions was not detected in the M. sympodialis genome. These observations strongly support our hypothesis that breakage of MgCEN2/MslCEN5 (or the orthologous ancestral CEN) and fusion of the two acentric arms to other chromosomes resulted in the reduction in chromosome number observed when comparing these species.

### Centromere inactivation by sequence divergence and loss of AT-richness resulted in chromosome number reduction in M. furfur

To understand the basis of the change in chromosome number from nine to seven in Malassezia species, we compared the synteny of ORFs flanking the M. slooffiae or M. globosa centromeres with that of M. furfur. Of the nine centromeres in M. slooffiae, three centromeres belonged to conserved gene synteny blocks and four others retained partial gene synteny conservation in M. furfur (Figure 6A, Table 3). A similar pattern of gene synteny conservation was observed between M. globosa and M. furfur (Figure 6B, Table 3). The genes flanking the remaining two centromeres (CEN8 and CEN9) in M. slooffiae were present in conserved gene synteny blocks in the two arms of MfChr3 (Figure 6C). However, the regions corresponding to CEN8 and CEN9 in M. slooffiae appear to have evolved to decreased AT-richness in M. furfur. A similar centromere inactivation mechanism was observed when CEN8 and CEN9 of M. globosa were compared to the corresponding syntenic regions in M. furfur (Figure 6D). These results suggest centromere inactivation by changes in the centromeric DNA sequence in this species (Figure 6—figure supplement 1).

![Figure 6.](https://cdn.elifesciences.org/articles/53944/elife-53944-fig6-v2.jpg)

**Figure 6.:** (A, B) Circos plots depicting the gene synteny blocks that are conserved between the M. slooffiae or M. globosa chromosomes and the M. furfur chromosomes. Tracks from outside to inside represent positions of centromeres and telomeres, GC content (plotted as blue and red lines indicating GC content below or above genome average, calculated in 0.4-kb non-overlapping windows), and colored connectors indicate regions of conserved gene synteny between each pair of two species. (C) Linear chromosome plot depicting the regions that show synteny between Chr3 of M. furfur and Chr3, Chr4, Chr7, Chr8, and Chr9 of M. slooffiae. GC content (in %) is shown as red/blue lines above each chromosome. Regions corresponding to MslCEN8 and MslCEN9 in MfChr3 are marked I and II, respectively. (D) Linear chromosome plot depicting the conservation of gene synteny between Chr3 of M. furfur and Chr1, Chr4, Chr8, and Chr9 of M. globosa. Regions corresponding to MgCEN9 and MgCEN8 in MfChr3 are marked I and II, respectively.

![Figure 6—figure supplement 1.](https://cdn.elifesciences.org/articles/53944/elife-53944-fig6-figsupp1-v2.jpg)

**Figure 6—figure supplement 1.:** (A, B) Zoomed-in view of regions marked I (A) and II (B) in Figure 6C, corresponding to inactivated MslCEN8 and MslCEN9 in M. furfur, respectively, along with the regions of gene synteny are represented. GC content (in %) is shown as a red/blue line diagram above each chromosome. (C, D) Zoomed-in view of the regions marked I (C) and II (D) in Figure 6D, corresponding to inactivated MgCEN9 and MgCEN8 in M. furfur, respectively, along with the regions of gene synteny are represented. GC content (in %) is shown as red/blue lines above each chromosome.

### The common ancestral Malassezia species contained nine chromosomes

To trace the ancestral karyotype in Malassezia, we predicted centromeres and inferred chromosome numbers in other species of clades A and B on the basis of GC troughs and gene synteny. We identified putative centromeres in M. dermatis and M. nana in Clade B because of their relatively better-assembled genomes distributed in 18 and 13 scaffolds, respectively. Of these, we could predict eight centromeric regions marked by GC troughs that were also enriched with the 12-bp motif in each species (Figure 7—figure supplement 1A–B, Figure 7—figure supplement 2A–B and Table 4). Furthermore, in both of these species, the eight putative centromeres shared complete gene synteny with the regions spanning M. sympodialis centromeres, indicating that their common ancestor had eight chromosomes (green circle in Figure 7A, Figure 7—figure supplement 3 and Table 3). To map the common ancestor in Clade B Malassezia species, we analyzed regions flanking centromeres of Chr2 of M. globosa and Chr8 of M. restricta, both of which mapped to the gene synteny breakpoint of the genome of the Malassezia species that have eight chromosomes suggesting that their common ancestor, named as Ancestor B (Anc. B), also had nine chromosomes (Figure 7A, Figure 7—figure supplement 3). On the basis of our centromere predictions in Clade B species and synteny analysis, we propose that centromere breakage would have occurred in the common ancestor of M. sympodialis, M. nana, and M. dermatis after divergence from the common ancestor of M. globosa and M. restricta, which retained a nine-chromosome configuration (Figure 7A,B).

![Figure 7.](https://cdn.elifesciences.org/articles/53944/elife-53944-fig7-v2.jpg)

**Figure 7.:** (A) Phylogenetic relationships between the Malassezia species analyzed in this study are represented and their chromosome numbers are shown. Species representing each clade are color-coded on the basis of previous reports (Theelen et al., 2018). The chromosome numbers for M. slooffiae and M. globosa are based on results from this study. In the case of M. sympodialis, M. restricta, and M. furfur, the chromosome numbers are based on previous reports (Boekhout and Bosboom, 1994; Senczek et al., 1999; Zhu et al., 2017). For M. dermatis, M. nana, M. vespertilionis, and M. japonica, the number of chromosomes were estimated from the predicted number of centromeres. The nodes corresponding to the ancestral state for Clade A and Clade B are labeled ‘Anc. A’ and ‘Anc. B’, respectively. Green and red circles indicate the origins of karyotypes that have eight and seven chromosomes, respectively, from an ancestral state of nine chromosomes. (B) Schematic of the centromere loss by breakage and the resulting reduction in chromosome number as observed in M. sympodialis (represented as the current state). A karyotype with nine chromosomes (as shown for M. globosa) is depicted as the ancestral state. (C) Proposed model of centromere inactivation observed in M. furfur as a consequence of fusion of AnChr8 and AnChr9 to the AnMfChr3 equivalent, resulting in a seven-chromosome configuration. The fusion product corresponding to extant MfChr3 is represented as the current state.

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/53944/elife-53944-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** (A–D) Graphs indicating the GC content (red lines) and GC3 content (black lines) of each chromosome of M. dermatis, M. nana, M. vespertilionis, and M. japonica. The positions of putative centromeres mapping to chromosomal GC minima are marked in blue. The x-axis indicates chromosomal coordinates in Mb.

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/53944/elife-53944-fig7-figsupp2-v2.jpg)

**Figure 7—figure supplement 2.:** The genomes of M. dermatis, M. nana, M. vespertilionis, and M. japonica were scanned for matches to the 12-bp AT-rich motif using a 500 bp sliding window. Hit counts (y-axis) were plotted against the chromosomal coordinates (x-axis, in kb) for each of the above species. Red asterisks near the line corresponding to maximum enrichment in every chromosome or scaffold mark the regions predicted as centromeres in each species.

![Figure 7—figure supplement 3.](https://cdn.elifesciences.org/articles/53944/elife-53944-fig7-figsupp3-v2.jpg)

**Figure 7—figure supplement 3.:** The gene order and synteny of ORFs flanking the centromeres of six Malassezia species, which are representative of clades B and C, analyzed by BLAST analysis using the protein sequences from M. sympodialis as query. Species included are: Mna, M. nana; Mde, M. dermatis; Msy, M. sympodialis; Mgl, M. globosa; Mre, M. restricta; and Msl, M. slooffiae. Chromosome/scaffold numbers are indicated at the start of every track. Boxes represent ORFs with the numbers inside them indicating percentage identity from BLAST analysis. Broken lines marked with a filled circle towards the ends indicate gene synteny breakpoints. Red arrows indicate inverted orientation of the scaffold/chromosome.

![Figure 7—figure supplement 4.](https://cdn.elifesciences.org/articles/53944/elife-53944-fig7-figsupp4-v2.jpg)

**Figure 7—figure supplement 4.:** The secondary structure of the centromere cores of MgCEN2 and MgCEN3 predicted by the ViennaRNA, generated using Geneious 9.0 (Lorenz et al., 2011). Blue and red circles mark the 5′- and the 3′- DNA ends, respectively.

**Table 4.**
 Coordinates, length, and GC content (in %) of the centromeres predicted in M. dermatis, M. nana, M. vespertilionis, and M. japonica.


<table>
  <thead>
    <tr>
      <th rowspan="2"></th>
      <th rowspan="2">Chr./scaffold</th>
      <th rowspan="2">CEN</th>
      <th colspan="4">Core centromere</th>
      <th rowspan="2">% GC genome</th>
    </tr>
    <tr>
      <th>Start</th>
      <th>End</th>
      <th>Length (bp)</th>
      <th>% GC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="8">M. dermatis JCM11348</td>
      <td>BCKX01000001.1 (Scf1)</td>
      <td>CEN1</td>
      <td>711,456</td>
      <td>711,978</td>
      <td>523</td>
      <td>22.8</td>
      <td rowspan="8">59.05</td>
    </tr>
    <tr>
      <td>BCKX01000002.1 (Scf2)</td>
      <td>CEN2</td>
      <td>1,014,281</td>
      <td>1,014,977</td>
      <td>697</td>
      <td>31.7</td>
    </tr>
    <tr>
      <td>BCKX01000003.1 (Scf3)</td>
      <td>CEN3</td>
      <td>232,065</td>
      <td>232,795</td>
      <td>731</td>
      <td>29.3</td>
    </tr>
    <tr>
      <td>BCKX01000004.1 (Scf4)</td>
      <td>CEN4</td>
      <td>409,839</td>
      <td>410,631</td>
      <td>793</td>
      <td>29.5</td>
    </tr>
    <tr>
      <td>BCKX01000005.1 (Scf5)</td>
      <td>CEN5</td>
      <td>94,520</td>
      <td>95,018</td>
      <td>499</td>
      <td>18.2</td>
    </tr>
    <tr>
      <td>BCKX01000006.1 (Scf6)</td>
      <td>CEN6</td>
      <td>473,487</td>
      <td>474,334</td>
      <td>848</td>
      <td>30.4</td>
    </tr>
    <tr>
      <td>BCKX01000007.1 (Scf7)</td>
      <td>CEN7</td>
      <td>76,361</td>
      <td>76,975</td>
      <td>615</td>
      <td>26</td>
    </tr>
    <tr>
      <td>BCKX01000008.1 (Scf8)</td>
      <td>CEN8</td>
      <td>17,893</td>
      <td>18,540</td>
      <td>648</td>
      <td>26.4</td>
    </tr>
    <tr>
      <td rowspan="8">M. nana JCM12085</td>
      <td>BCLA01000001.1 (Scf1)</td>
      <td>CEN1</td>
      <td>715,036</td>
      <td>715,592</td>
      <td>557</td>
      <td>27.8</td>
      <td rowspan="8">57.95</td>
    </tr>
    <tr>
      <td>BCLA01000002.1 (Scf2)</td>
      <td>CEN2</td>
      <td>349,428</td>
      <td>350,120</td>
      <td>693</td>
      <td>33</td>
    </tr>
    <tr>
      <td>BCLA01000003.1 (Scf3)</td>
      <td>CEN3</td>
      <td>220,773</td>
      <td>221,345</td>
      <td>573</td>
      <td>27.9</td>
    </tr>
    <tr>
      <td>BCLA01000004.1 (Scf4)</td>
      <td>CEN4</td>
      <td>410,594</td>
      <td>411,387</td>
      <td>794</td>
      <td>33.2</td>
    </tr>
    <tr>
      <td>BCLA01000005.1 (Scf5)</td>
      <td>CEN5</td>
      <td>524,594</td>
      <td>525,105</td>
      <td>512</td>
      <td>24.8</td>
    </tr>
    <tr>
      <td>BCLA01000006.1 (Scf6)</td>
      <td>CEN6</td>
      <td>133,647</td>
      <td>134,324</td>
      <td>678</td>
      <td>33.6</td>
    </tr>
    <tr>
      <td>BCLA01000007.1 (Scf7)</td>
      <td>CEN7</td>
      <td>408,363</td>
      <td>409,067</td>
      <td>705</td>
      <td>34.2</td>
    </tr>
    <tr>
      <td>BCLA01000008.1 (Scf8)</td>
      <td>CEN8</td>
      <td>398,756</td>
      <td>399,423</td>
      <td>668</td>
      <td>32.5</td>
    </tr>
    <tr>
      <td rowspan="9">M. vespertilionis CBS15041</td>
      <td>KZ454987.1 (Scf1)</td>
      <td>CEN1</td>
      <td>410,820</td>
      <td>411,340</td>
      <td>521</td>
      <td>15.7</td>
      <td rowspan="9">56.6</td>
    </tr>
    <tr>
      <td>KZ454988.1 (Scf2)</td>
      <td>CEN2</td>
      <td>1,275,509</td>
      <td>1,276,238</td>
      <td>730</td>
      <td>25.8</td>
    </tr>
    <tr>
      <td>KZ454989.1 (Scf3)</td>
      <td>CEN3</td>
      <td>322,361</td>
      <td>323,277</td>
      <td>917</td>
      <td>38.2</td>
    </tr>
    <tr>
      <td>KZ454990.1 (Scf4)</td>
      <td>CEN4</td>
      <td>583,450</td>
      <td>584,319</td>
      <td>870</td>
      <td>28.9</td>
    </tr>
    <tr>
      <td>KZ454991.1 (Scf5)</td>
      <td>CEN5</td>
      <td>802,843</td>
      <td>804,042</td>
      <td>1200</td>
      <td>28.8</td>
    </tr>
    <tr>
      <td>KZ454992.1 (Scf6)</td>
      <td>CEN6</td>
      <td>739,896</td>
      <td>740,558</td>
      <td>663</td>
      <td>22.3</td>
    </tr>
    <tr>
      <td>KZ454993.1 (Scf7)</td>
      <td>CEN7</td>
      <td>268,699</td>
      <td>269,626</td>
      <td>928</td>
      <td>28.8</td>
    </tr>
    <tr>
      <td>KZ454994.1 (Scf8)</td>
      <td>CEN8</td>
      <td>10,985</td>
      <td>11,865</td>
      <td>881</td>
      <td>28</td>
    </tr>
    <tr>
      <td>KZ454995.1 (Scf9)</td>
      <td>CEN9</td>
      <td>19,047</td>
      <td>19,724</td>
      <td>678</td>
      <td>29.1</td>
    </tr>
    <tr>
      <td rowspan="9">M. japonica JCM11963</td>
      <td>BCKY01000001.1 (Scf1)</td>
      <td>CEN1</td>
      <td>1,068,050</td>
      <td>1,068,614</td>
      <td>564</td>
      <td>25.1</td>
      <td rowspan="9">62.35</td>
    </tr>
    <tr>
      <td>BCKY01000002.1 (Scf2)</td>
      <td>CEN2</td>
      <td>139,423</td>
      <td>139,920</td>
      <td>497</td>
      <td>20.3</td>
    </tr>
    <tr>
      <td>BCKY01000003.1 (Scf3)</td>
      <td>CEN3</td>
      <td>350,068</td>
      <td>350,603</td>
      <td>535</td>
      <td>24.3</td>
    </tr>
    <tr>
      <td>BCKY01000004.1 (Scf4)</td>
      <td>CEN4</td>
      <td>380,877</td>
      <td>381,439</td>
      <td>562</td>
      <td>24.2</td>
    </tr>
    <tr>
      <td>BCKY01000005.1 (Scf5)</td>
      <td>CEN5</td>
      <td>507,632</td>
      <td>508,230</td>
      <td>598</td>
      <td>24.5</td>
    </tr>
    <tr>
      <td>BCKY01000006.1 (Scf6)</td>
      <td>CEN6</td>
      <td>240,968</td>
      <td>250,550</td>
      <td>582</td>
      <td>23.7</td>
    </tr>
    <tr>
      <td>BCKY01000007.1 (Scf7)</td>
      <td>CEN7</td>
      <td>286,711</td>
      <td>287,234</td>
      <td>523</td>
      <td>24.9</td>
    </tr>
    <tr>
      <td>BCKY01000008.1 (Scf8)</td>
      <td>CEN8</td>
      <td>87,314</td>
      <td>87,873</td>
      <td>559</td>
      <td>23.9</td>
    </tr>
    <tr>
      <td>BCKY01000010.1 (Scf10)</td>
      <td>CEN9</td>
      <td>230,906</td>
      <td>231,456</td>
      <td>530</td>
      <td>24.1</td>
    </tr>
  </tbody>
</table>

As mentioned earlier, M. furfur and M. obtusa of Clade A contain seven chromosomes each (Boekhout and Bosboom, 1994; Boekhout et al., 1998). To further understand the karyotype variations within this clade, we predicted the chromosome number in Malassezia vespertilionis and Malassezia japonica because their genomes are relatively well assembled (Sugita et al., 2003; Lorch et al., 2018). In both of these species, we were able to predict nine GC troughs, indicative of the centromeres of nine chromosomes (Figure 7—figure supplement 1C–D, Table 4). In the case of M. vespertilionis, all of the predicted centromeres showed enrichment of the 12-bp motif (Figure 7—figure supplement 2C). However, the 12-bp motif was found to be enriched in all of the predicted centromeres except the centromere of scaffold 7 of M. japonica (Figure 7—figure supplement 2D). The presence of species with nine chromosomes in Clade A suggests that the ancestral state in this clade, Anc. A, also contained nine chromosomes (Figure 7A).

We identified nine centromeres in M. slooffiae, the only species in Clade C with a well-assembled genome. The presence of species with nine chromosomes in each of the three clades of Malassezia species, the conservation of gene synteny across orthologous centromeres, and the similar centromere features shared by all nine species analyzed in this study suggest that Malassezia species diverged from a common ancestor that had nine chromosomes with short regional centromeres enriched with the 12-bp AT-rich DNA sequence motif.

## Discussion

In this study, we experimentally validated the chromosome number in M. slooffiae and M. globosa by PFGE analysis. We sequenced and assembled the genomes of M. slooffiae, M. globosa, and M. furfur and compared each one with the genome of M. sympodialis in order to understand the karyotype differences observed in members of the Malassezia species complex. These species represent each of the three major clades of Malassezia species with chromosome numbers ranging from seven to nine. Because centromere loss or gain directly influences the chromosome number of a given species, we experimentally identified the centromeres of these representative species to understand the mechanisms of karyotype diversity. Kinetochore proteins are useful tools in identifying the centromeres of an organism. The localization of the evolutionarily conserved kinetochore protein Mtw1 suggested that kinetochores are clustered throughout the cell cycle in M. sympodialis. ChIP-sequencing analysis identified short regional (<5 kb long) centromeres in M. sympodialis that are depleted of histone H3, but enriched with an AT-rich sequence motif. The identification of centromeres in M. slooffiae, M. globosa, and M. furfur further suggested that centromere properties are conserved across these Malassezia species. By predicting putative centromeres in five other species and by considering four species with experimentally mapped centromeres described above across three clades of Malassezia, we concluded that an AT-rich centromere core of <1 kb in length enriched with the 12-bp sequence motif is a potential signature of centromeres in the nine Malassezia species analyzed in this study. Comparative genomics analysis revealed two major mechanisms of centromere inactivation resulting in karyotype change. The presence of a nine-chromosome state in each of the three clades, along with conserved centromere features and conserved gene synteny, helped us infer that the ancestral Malassezia species had nine chromosomes that had short regional centromeres with an AT-rich core enriched with the 12-bp sequence motif.

Centromeres in the Malassezia species complex represent the first example of short regional centromeres in basidiomycetes. Centromeres reported in other basidiomycetes, such as those in Cryptococcus and Ustilago species, are of the large regional type (Yadav et al., 2018b). The Malassezia species analyzed in this study have a significantly smaller genome (<9 Mb) than other basidiomycetes and lack RNAi machinery. The occurrence of short regional centromeres in RNAi-deficient Malassezia species is in line with a previous finding showing a reduction in centromere size in RNAi-deficient basidiomycete species as compared to their RNAi-proficient relatives (Yadav et al., 2018b). With the presence of clustered kinetochores across cell cycle stages, and the absence of key genes encoding the RNAi machinery, these Malassezia species resemble ascomycetes such as many of the CTG clade species with short regional centromeres (Sanyal et al., 2004; Nakayashiki et al., 2006; Padmanabhan et al., 2008; Kapoor et al., 2015; Chatterjee et al., 2016; Yadav et al., 2018a), rather than the basidiomycetes with large regional centromeres. By combining these features, we conclude that the genome size and the presence of complete RNAi machinery could determine the centromere type of a species, irrespective of the phylum to which it belongs.

Based on the binding patterns of the kinetochore protein across the M. sympodialis genome, the 3–5-kb long region can be divided into two domains: (a) an AT-rich CEN core that maps to the intergenic region containing the GC trough, which shows maximum kinetochore binding (<1 kb); and (b) the regions flanking the core, which show basal levels of kinetochore protein binding. We observed conservation of the 12-bp AT-rich motif in the centromere core across the nine Malassezia species. It should also be noted that the 12-bp motif is significantly enriched at the centromeres but is not exclusive to the centromeres as it is detected across the chromosomes. We did not observe any orientation bias for these motifs. The functional significance of the frequent occurrence of this motif at centromeres is unknown. It will be intriguing to test the roles played by this motif, the core, and the flanking sequences in centromere function. Testing these domains for centromere function in vivo by making centromeric plasmids in various Malassezia species is challenging at present because of technical limitations. Other than M. sympodialis, M. pachydermatis, and M. furfur, no other Malassezia species have been successfully transformed (Ianiri et al., 2016; Celis et al., 2017; Ianiri et al., 2017a). Moreover, in all of these cases, the genetic manipulations are performed by Agrobacterium-mediated transconjugation, which cannot be used for the introduction of circular plasmids. Hence, the functional significance of the 12-bp motif remains unknown and remains an important question to be addressed in the future to provide an understanding of centromere function in these species.

The centromeres in M. sympodialis contain transcribed ORFs, which have also been documented in the centromeres of rice, maize, and Zymoseptoria tritici (Nagaki et al., 2004; Wang et al., 2014). In contrast to these cases, our read count analysis did not reveal any significant difference in the transcription (RPKM values) of centromere-associated ORFs and ORFs elsewhere in the genome of M. sympodialis. We posit that the 12-bp AT-rich motif sequences could facilitate the transcription of these genes by recruiting transcription factors that have a possible role in kinetochore assembly. Binding of Cbf1 at CDEI in S. cerevisiae centromeres and of Ams2 at the central core sequences of S. pombe centromeres are classic examples of transcription factors facilitating kinetochore stability in fungal systems (Hemmerich et al., 2000; Chen et al., 2003). A fine regulation of transcription by Cbf1, Ste12, and Htz1, and the resulting low-level cenRNAs, have been implicated in proper chromosome segregation in budding yeast (Ohkuni and Kitagawa, 2011; Ling and Yuen, 2019). These studies reinforce the role of transcription in centromere function irrespective of the centromere structure.

In this study, we report three high-quality chromosome-level genome assemblies and identified centromeres in nine Malassezia species, representing all of the three Malassezia clades with differing numbers of chromosomes. This will serve as a rich resource for comparative genomics in the context of niche adaptation and speciation. Analysis of gene synteny conservation across centromeres using these genomes revealed breakage at the centromere as one of the mechanisms that results in a karyotype change between closely related species — those with nine chromosomes, such as M. slooffiae and M. globosa, and those with eight chromosomes, such as M. sympodialis. Gene synteny breakpoints adjacent to the centromeres have been reported in C. tropicalis, which has seven chromosomes, one less than C. albicans (Chatterjee et al., 2016). Centromere loss by breakage was proposed to have reduced the Ashbya gossypii karyotype by one when compared to the pre-whole genome duplication ancestor (Gordon et al., 2011). Breakpoints of conserved gene synteny between mammalian and chicken chromosomes were also mapped to the centromeres (International Chicken Genome Sequencing Consortium, 2004). Similar consequences in the karyotype have been reported in cases where centromeres were experimentally excised. Besides neocentromere formation, survival by fusion of acentric chromosome arms has been shown in S. pombe (Ishii et al., 2008). Such fusions are detected upon deletion of centromeres in another basidiomycete, C. deuterogattii (Schotanus and Heitman, 2019). By comparing the ancestral state (M. slooffiae) and other Malassezia species with either the same number or fewer chromosomes, we observed gene synteny breaks that were adjacent to centromeres (indicated by partial synteny conservation), in addition to the break observed at MgCEN2 or MslCEN5. Does this suggest that Malassezia centromeres are fragile in nature? We advance the following hypothesis to explain the observed breaks at centromeres.

Studies of the common fragile sites in the human genome suggest different forms of replication stress as a major source of instability and subsequent breakage at these sites (Helmrich et al., 2011; Letessier et al., 2011; Ozeri-Galai et al., 2011). The resolution of the resulting replication fork stall has been shown to be critical for the stability of these fragile sites (Schwartz et al., 2005). Studies of the human fragile site FRA16D show that the AT-rich DNA (Flex1) results in fork stalling as a consequence of cruciform or secondary structure formation (Zhang and Freudenreich, 2007). Centromeres are natural replication fork stall sites in the genome (Greenfeder and Newlon, 1992; Smith et al., 1995; Mitra et al., 2014). The AT-rich core centromere sequence in M. globosa is also predicted to form secondary structures (Figure 7—figure supplement 4), which can be facilitated by the inherent replication fork stall at the centromeres. Whenever these secondary structures are unresolved and the fork restart fails, double strand breaks (DSBs) can occur at the centromeres. Chromosomal breakage and aneuploidy resulting from such defects are known to occur in cancers (Kops et al., 2005). In mammals, centromeric DSBs are repaired efficiently compared to regions elsewhere in the genome, largely because of the presence of several homology tracts in the form of repetitive DNA sequences and the stiffness provided by the inherent heterochromatic state, which facilitates ligation (Rief and Löbrich, 2002). Malassezia species are haploid in nature and lack typical pericentric heterochromatin marks. Although the efficiency of centromeric DSB repair in the absence of long tracts of homologous sequences is not known in this species complex, we propose that the AT-rich core sequences, by virtue of secondary structure formation during DNA replication, could occasionally undergo DNA breakage at the centromere in Malassezia species.

The second mechanism of chromosome number reduction suggested by our analyses comparing the M. furfur genome with the genomes of M. slooffiae or M. globosa involves the inactivation of centromeres in the process of transition from a nine-chromosome state to a seven-chromosome state. Centromere inactivation occurs in cases involving the fusion of centric chromosomal fragments, stabilizing the fusion product and generating a functionally monocentric chromosome, as seen during the origin of human Chr2 from the ancestor shared with the great apes (Yunis and Prakash, 1982; IJdo et al., 1991). A larger proportion of known centromere inactivation events were shown to be mediated by epigenetic modifications, in which inactivated centromeres are enriched with marks such as H3K9me2/3, H3K27me2/3, or DNA methylation, emphasizing the role of heterochromatin in this process (Zhang et al., 2010; Koo et al., 2011; Sato et al., 2012). Deletion of the centromere sequence corresponding to kinetochore binding has also been reported as an alternate mechanism, albeit a less frequent mechanism, in both humans and in yeast (Stimpson et al., 2010; Gordon et al., 2011; Sato et al., 2012). In difference to what might be expected according to the two modes described above, we observed divergence in the sequences corresponding to the inactivated centromeres (CEN8 and CEN9 of both M. slooffiae and M. globosa) in the arms of M. furfur Chr3, resulting in the loss of AT-richness of these centromere core regions (Figure 7C). This is also suggestive of a functional role for AT-rich DNA in centromere function in these species.

A change in chromosome number between two closely related species such as C. albicans and C. tropicalis is associated with a change in centromere structure: centromeres in C. albicans are unique short regions that are epigenetically regulated, whereas those in C. tropicalis are associated with genetically defined homogenized inverted repeats (Chatterjee et al., 2016). Strikingly, in both the transitions described above for Malassezia species, we did not observe any change in the centromere structure. The emergence of evolutionarily new centromeres, as seen in primate evolution, was not detected in Malassezia species (Rocchi et al., 2009; Kalitsis and Choo, 2012). This is particularly striking in the absence of conservation of any specific centromere-exclusive DNA sequence. This suggests that a strong driving force helps to maintain the highly conserved centromere properties in closely related Malassezia species that descended from a common ancestor, even after extensive chromosomal rearrangements involving centromeres that might have driven speciation. Furthermore, centromere inactivation/loss of centromere function seems to be a conserved theme mediating variation in chromosome number from unicellular yeast species to metazoans, including primates.

## Materials and methods

The reagents, strains, plasmids, and primers used in this study are listed in the Key Resources Table below.

**Key resources table**


<table>
  <thead>
    <tr>
      <th>Reagent type (species) or resource</th>
      <th>Designation</th>
      <th>Source or reference</th>
      <th>Identifier</th>
      <th>Additional information</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Biological sample (Malassezia globosa)</td>
      <td>CBS7966</td>
      <td>CBS</td>
      <td></td>
      <td>Wild-type strain</td>
    </tr>
    <tr>
      <td>Biological sample (Malassezia slooffiae)</td>
      <td>CBS7956</td>
      <td>CBS</td>
      <td></td>
      <td>Wild-type strain</td>
    </tr>
    <tr>
      <td>Biological sample (Malassezia furfur)</td>
      <td>CBS14141</td>
      <td>CBS</td>
      <td></td>
      <td>Wild-type strain</td>
    </tr>
    <tr>
      <td>Biological sample (Malassezia sympodialis)</td>
      <td>ATCC42132</td>
      <td>ATCC</td>
      <td></td>
      <td>Wild-type strain</td>
    </tr>
    <tr>
      <td>Biological sample (Saccharomyces cerevisiae)</td>
      <td>BY4741</td>
      <td></td>
      <td></td>
      <td>Wild-type strain (MATa his3Δ1 leu2Δ0 met15Δ0 ura3Δ0)</td>
    </tr>
    <tr>
      <td>Genetic reagent (Malassezia sympodialis)</td>
      <td>MSY001</td>
      <td>This study</td>
      <td></td>
      <td>M. sympodialis (ATCC42132) cells expressing GFP-Mtw1</td>
    </tr>
    <tr>
      <td>Genetic reagent (Malassezia furfur)</td>
      <td>MF001</td>
      <td>This study</td>
      <td></td>
      <td>M. furfur (CBS14141) cells expressing CENP-A-3xFLAG</td>
    </tr>
    <tr>
      <td>RecombinantDNA reagent</td>
      <td>Plasmid pGI3</td>
      <td>(Ianiri et al., 2017b)</td>
      <td></td>
      <td>Vector backbone for Agrobacterium-mediated transconjugation</td>
    </tr>
    <tr>
      <td>RecombinantDNA reagent</td>
      <td>Plasmid pAIM1</td>
      <td>(Ianiri et al., 2016)</td>
      <td></td>
      <td>Plasmid with NAT marker, used as template for PCR</td>
    </tr>
    <tr>
      <td>RecombinantDNA reagent</td>
      <td>Plasmid pVY7</td>
      <td>(Kozubowski et al., 2013)</td>
      <td></td>
      <td>Plasmid with GFP, used as template for PCR</td>
    </tr>
    <tr>
      <td>RecombinantDNA reagent</td>
      <td>Plasmid pMHR04</td>
      <td>This study</td>
      <td></td>
      <td>Construct used to tag MsyMtw1 with GFP tag at the amino-terminus</td>
    </tr>
    <tr>
      <td>RecombinantDNA reagent</td>
      <td>Plasmid pMF1</td>
      <td>This study</td>
      <td></td>
      <td>Construct used to tag MfCENP-A with 3xFLAG tag at the carboxyl terminus</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-GFP (mouse monoclonal)</td>
      <td>Roche</td>
      <td>11814460001</td>
      <td>IF (1:100) WB (1:3000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-PSTAIRE (mouse monoclonal)</td>
      <td>Abcam</td>
      <td>Cat. no. 10345</td>
      <td>WB (1:5000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-mouse IgG HRP (goat polyclonal)</td>
      <td>Abcam</td>
      <td>Cat. no. ab97023</td>
      <td>WB (1:10,000)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-H3 (rabbit polyclonal)</td>
      <td>Abcam</td>
      <td>Cat. no. ab1791</td>
      <td>ChIP (5 μL per 500 μL IP fraction)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-H4 (rabbit polyclonal)</td>
      <td>Abcam</td>
      <td>Cat. no. ab10158</td>
      <td>ChIP (5 μL per 500 μL IP fraction)</td>
    </tr>
    <tr>
      <td>Antibody</td>
      <td>Anti-FLAG (M2) (mouse monoclonal)</td>
      <td>Sigma</td>
      <td>Cat. no. F1804</td>
      <td>WB (1: 2500)</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>GFP-trap beads</td>
      <td>ChromoTek</td>
      <td>Cat. no. gta-20</td>
      <td>ChIP (20 μL per 500 μL fraction)</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Blocked agarose beads</td>
      <td>ChromoTek</td>
      <td>Cat. no. bab-20</td>
      <td>ChIP (20 μL per 500 μL fraction)</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Protein-A sepharose beads</td>
      <td>Sigma</td>
      <td>Cat. no. P3391</td>
      <td>ChIP (20 μL per 500 μL fraction)</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>M2 anti-FLAG affinity gel</td>
      <td>Sigma</td>
      <td>Cat. no. A2220</td>
      <td>ChIP (20 μL per 500 μL fraction)</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Lysing enzymes from Trichoderma harzianum</td>
      <td>Sigma</td>
      <td>Cat. no. L1412</td>
      <td>Enzyme to prepare spheroplasts</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Zymolyase 20T</td>
      <td>MP biomedicals</td>
      <td>Cat. no. 320921</td>
      <td>Enzyme to prepare spheroplasts</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>Chitosanase</td>
      <td>Sigma</td>
      <td>Cat. no. C0794</td>
      <td>Enzyme to prepare spheroplasts</td>
    </tr>
    <tr>
      <td>Other</td>
      <td>SensiFAST SYBR No ROX Kit</td>
      <td>Bioline</td>
      <td>Cat. no. BIO-98020</td>
      <td>qPCR assay reagent</td>
    </tr>
    <tr>
      <td>Chemical compound, drug</td>
      <td>2-mercaptoethanol</td>
      <td>HiMedia</td>
      <td>Cat. no. MB041</td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Geneious 9.0</td>
      <td>Biomatters Ltd.</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>SyMap</td>
      <td>(Soderlund et al., 2011)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>PhylloGibbs-MP</td>
      <td>(Siddharthan, 2008)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Circos</td>
      <td>(Krzywinski et al., 2009)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Satsuma</td>
      <td>(Grabherr et al., 2010)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Easyfig</td>
      <td>(Sullivan et al., 2011)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>GET_HOMOLOGUES</td>
      <td>(Contreras-Moreira and Vinuesa, 2013)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>IQ-TREE v1.6.5</td>
      <td>(Nguyen et al., 2015)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>iTOL v4.3.3</td>
      <td>(Letunic and Bork, 2019)</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>SMRTPortal v2.3</td>
      <td>PacBio, Menlo Park, CA, USA</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Fiji</td>
      <td>National Institutes of Health</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Illustrator</td>
      <td>Adobe Systems</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Excel</td>
      <td>Microsoft</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Software, algorithm</td>
      <td>Word</td>
      <td>Microsoft</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Sequence-based reagent</td>
      <td>List of primers used in this study</td>
      <td>Sigma</td>
      <td></td>
      <td>In Supplementary file 1</td>
    </tr>
  </tbody>
</table>

### Media and growth conditions for Malassezia strains

Malassezia strains were grown on modified Dixon's media (malt extract 36 g/L, desiccated ox-bile 20 g/L, Tween40 10 mL/L, peptone 6 g/L, glycerol 2 mL/L, oleic acid 2.89 mL/L). M. sympodialis, M. furfur strains were grown at 30°C. Cultures of M. globosa and M. slooffiae were grown at 32°C.

### Construction of the M. sympodialis strain expressing GFP-Mtw1

The allele for N-terminal tagging of Mtw1 with GFP was prepared by gap repair in the Saccharomyces cerevisiae BY4741 strain (Eckert-Boulet et al., 2012). Briefly, a 1.6-kb fragment consisting of the upstream and promoter sequence of the MTW1 gene and a 1.6-kb fragment having the MTW1 ORF (Protein ID: SHO76526) along with the downstream sequence were amplified from M. sympodialis genomic DNA. The GFP ORF (without the stop codon) and NAT were amplified from plasmids pVY7 and pAIM1, respectively. S. cerevisiae was transformed with all four fragments and the linearized plasmid pGI3 (digested with KpnI and BamHI) and the epitope-tagged allele were assembled in an ordered way by gap repair. Total DNA was isolated from S. cerevisiae and the E. coli DH5α strain was transformed. The pGFP-Mtw1 construct was screened by restriction digestion and further confirmed by sequencing. The pGFP-Mtw1 construct was used to transform M. sympodialis strain ATCC42132 by Agrobacterium tumefaciens-mediated transconjugation (Ianiri et al., 2016; Ianiri et al., 2017a).

### Construction of the M. furfur strain expressing CENP-A FLAG

The allele for C-terminal tagging of CENP-A with a 3xFLAG epitope tag was prepared by gap repair in the Saccharomyces cerevisiae BY4741 strain (Eckert-Boulet et al., 2012). Briefly, a 1-kb fragment consisting of the upstream and promoter sequence of the CENP-A gene of M. furfur including the ORF (CENP-A ORF coordinates in Chr1: 1,453,468–1,453,921), as well as a 1-kb fragment containing the sequence downstream of CENP-A ORF, were amplified from M. furfur genomic DNA. The 3xFLAG tag was introduced in the reverse primer annealing to the CENP-A ORF. The NAT marker was amplified from plasmid pAIM1 as above. S. cerevisiae was transformed with all three fragments and plasmid pGI3 (digested with KpnI and BamHI) and the epitope-tagged allele were assembled in an ordered way by gap repair. Total DNA was isolated from S. cerevisiae and the E. coli DH5α strain was transformed. The resulting pMF1 construct was screened by restriction digestion and further confirmed by sequencing. The pMF1 construct was used to transform M. furfur strain CBS14141 by Agrobacterium tumefaciens-mediated transconjugation (Ianiri et al., 2016; Ianiri et al., 2017a) to obtain the epitope-tagged strain MF001.

### Microscopic imaging of live cells and processing

The GFP-Mtw1 strain was inoculated to 1% v/v from a saturated starter culture grown in mDixon medium. After growth for 6 hr at 30 °C/ 150 rpm, these cells were pelleted at 4,000 rpm and washed three times with 1x phosphate-buffered saline (PBS), and the cell suspension was placed on a clean glass slide. A coverslip was placed on the spot and sealed prior to imaging. The images were acquired at room temperature using a laser scanning inverted confocal microscope LSM 880-Airyscan (ZEISS, Plan Apochromat 63x, NA oil 1.4) equipped with highly sensitive photo-detectors. The filters used were GFP/FITC 488 excitation and GFP/FITC 500/550 band pass, long pass for emission. Z-stack images were taken every 0.3 μm and processed using ZEISS Zen software or ImageJ. All of the images were processed post-acquisition with minimal adjustments to levels and linear contrast until the signals were highlighted.

### Preparation of spheroplasts

Cells were grown on mDixon’s medium and washed with water by centrifugation at 4000 rpm for 5 min. Cells were resuspended in 10 mL of 5% (v/v) 2-mercaptoethanol solution in water and incubated at 30 °C/ 150 rpm for 45 min. The cells were pelleted, washed, and resuspended in 3 mL spheroplasting buffer (40 mM citric acid, 120 mM Na2HPO4 and 1.2 M sorbitol) for every 1.5 × 109 cells. Cell clumps were dissociated by mild sonication for 30 s using the medium-intensity setting in a Bioruptor (Diagenode). Lysing enzymes from Trichoderma harzianum (Sigma), chitosanase (Sigma), and zymolyase-20T (MP Biomedicals) were added at 20 mg/mL, 0.2 µg/mL, and 100 µg/mL, respectively. The spheroplasting suspension was incubated at 30°C/65 rpm for 6–8 hr. The suspension was examined under a microscope to estimate the proportion of spheroplasts. Spheroplasts were washed with ice-cold 1xPBS and used as per the experimental design (adapted from Boekhout, 2003).

### Indirect immunofluorescence

The GFP-Mtw1 strain was inoculated to 1% (v/v) from a saturated starter culture grown in mDixon medium. After growth for 6 hr, the cells were fixed by the addition of formaldehyde to a final concentration of 3.7% for 1 hr. Post-fixing, the cells were washed with water and taken for preparation of spheroplasts (as described above). Spheroplasts were washed with ice-cold 1xPBS and resuspended in ice-cold 1xPBS to a cell density suitable for microscopy. Slides for microscopy were washed with water and coated with poly L-lysine (15 µL of 10 mg/mL solution per well) for 5 min at room temperature. The solution was aspirated and washed once with water. The cell suspension was added to each well (15–20 µL) and allowed to stand at room temperature for 5 min. The cell suspension was aspirated and the slides were washed once with water to remove unbound cells. The slides were fixed in ice-cold methanol for 6 min followed by treatment with ice-cold acetone for 30 s. Post fixing, blocking solution (2% non-fat skim milk in 1xPBS) was added to each well, and slides were incubated at room temperature for 30 min. After this, the blocking solution was aspirated and primary antibodies were added (mouse anti-GFP antibodies [Sigma] at 1:100 dilution). After incubation for 1 hr at room temperature, each slide was washed eight times with 1xPBS giving a 2 min incubation for every wash. Secondary antibody solution (goat anti-mouse-AlexaFluor488 [Invitrogen] at 1:500 dilution) was added to each well and incubated for 1 hr in the dark at room temperature. Post-incubation, slides were washed as described above. Mounting medium (DAPI at 100 ng/mL in 70% glycerol) was added, incubated for 5 min and aspirated out. Slides were sealed with a clean coverslip before imaging. The images were acquired at room temperature using an inverted fluorescence microscope (ZEISS Axio Observer, Plan Apochromat 100x, NA oil 1.4). Z- stack images were taken every 0.3 μm and processed using ZEISS Zen software/ImageJ.

### Chromatin immunoprecipitation (ChIP)

The ChIP protocol was adapted from that implemented for C. neoformans (Yadav et al., 2018b). Logarithmically grown cells were fixed with formaldehyde at a final concentration of 1% for 30 min for Mtw1 ChIP and 15 min for CENP-A, histone H3, and histone H4 ChIP. The reaction was quenched by the addition of glycine to a final concentration of 0.135 M. Cells were pelleted and processed for spheroplasting as described above. Spheroplasts were washed once sequentially using 10 mL of the following ice-cold buffers: 1xPBS, Buffer-I (0.25% Triton X-100, 10 mM EDTA, 0.5 mM EGTA, 10 mM Na-HEPES [pH 6.5]), and Buffer-II (200 mM NaCl, 1 mM EDTA, 0.5 mM EGTA, 10 mM Na-HEPES [pH 6.5]). The pellet after the final wash was resuspended in 1 mL lysis buffer (50 mM HEPES [pH 7.4], 1% Triton X-100, 140 mM NaCl, 0.1% Na-deoxycholate, 1 mM EDTA) for every 1.5 × 109 cells. Protease inhibitor cocktail was added to 1x final concentration.

The resuspended spheroplasts were sonicated with a Bioruptor (Diagenode) using a 30 s ON/OFF pulse at high-intensity mode with intermittent incubation on ice to obtain chromatin fragments in the size range of 100–300 bp. The lysate was cleared after sonication by centrifugation at 13,000 rpm for 10 min at 4°C. The input DNA fraction was separated at this step (1/10th volume of lysate) and processed for de-crosslinking by the addition of 400 µL elution buffer (0.1 M NaHCO3, 1% SDS) per 100 µL lysate (processing for de-crosslinking is mentioned below). The remaining lysate was split equally and processed as IP and control samples. For GFP-Mtw1 ChIP, 20 µL GFP-trap beads and blocked agarose beads, respectively, were used for IP and control. For CENP-A-3xFLAG ChIP, 20 µL anti-FLAG affinity gel and blocked agarose beads, respectively, were used for IP and control. In the case of histone H3 or histone H4 ChIP, 5 µL of antibodies were used per IP fraction along with 20 µL Protein-A sepharose beads. Samples were rotated for 6 hr at 4°C. Post incubation, samples were sequentially washed as follows: twice with 1 mL low salt wash buffer (0.1% SDS, 1% Triton X-100, 2 mM EDTA, 20 mM Tris [pH 8.0], 150 mM NaCl), twice with 1 mL high salt wash buffer (0.1% SDS, 1% Triton X-100, 2 mM EDTA, 20 mM Tris [pH 8.0], 500 mM NaCl), once with 1 mL LiCl wash buffer (0.25 M LiCl, 1% NP-40, 1% Na-deoxycholate, 1 mM EDTA, 10 mM Tris [pH 8.0]) and twice with 1 mL 1xTE (10 mM Tris [pH 8.0], 1 mM EDTA). Samples were rotated in a rotaspin for 5 min at room temperature for every wash (15 min in case of histone H3 or histone H4 ChIP). After washing, DNA was eluted from the beads twice using 250 µL elution buffer. The samples for elution were incubated at 65°C for 5 min, rotated for 15 min and then collected by centrifugation.

Samples were decrosslinked by the addition of 20 µL 5 M NaCl and incubation at 65°C for 6 hr. Following this, samples were deproteinized by the addition of 10 µL 0.5 M EDTA, 20 µL 1 M Tris [pH6.8], 2 µL Proteinase K (20 mg/L) and incubation at 45°C for 2 hr. After incubation, samples were treated with an equal volume of phenol-chloroform-isoamyl alcohol (25:24:1) mix, and the aqueous phase was extracted by centrifugation. DNA was precipitated by the addition of 1/10th volume of 3 M Na-acetate, 1 µL glycogen (20 mg/mL), 1 mL absolute ethanol and incubation at −20°C for at least 12 hr. Finally, the samples were harvested by centrifugation at 13,000 rpm for 45 min at 4°C followed by washing the pellet once with ice-cold 70% ethanol. Air-dried pellets were then resuspended in 20 µL sterile MilliQ water with 10 µg/mL RNAse. Samples were either processed for library preparation for ChIP-sequencing or analyzed by qPCR with the primers listed in Supplementary file 1.

### Analysis of sequencing data

GFP-Mtw1 ChIP sequencing was performed at the Clevergene Biocorp. Pvt. Ltd., Bengaluru, India. A total of 46,704,720 and 63,524,912 150-bp paired-end reads were obtained for IP and Input samples, respectively. The reads were mapped to the M. sympodialis ATCC42132 genome using Geneious 9.0 (http://www.geneious.com/) with default conditions. Each read was allowed to map only once randomly anywhere in the genome. The alignments were exported to BAM files, sorted, and visualized using the Integrative Genomics Viewer (IGV, Broad Institute). The images from IGV were imported into Adobe Photoshop (Adobe) and scaled for representation purposes. RNA-sequencing data (E-MTAB-4589) from a previous study was downloaded from the ArrayExpress website, sorted, and visualized using IGV. GC-content was calculated using Geneious 9.0 with a sliding window size of 250 bp. The data were exported as wig files and further visualized using IGV.

### Western blotting

Protein lysates for western blot were prepared by the TCA method. Overnight grown cultures of 1 mL were harvested, washed, and resuspended in 400 μL of 12.5% ice-cold TCA solution. The suspension was vortexed briefly and stored at – 20°C for 4–6 hr. The suspension was thawed on ice, pelleted at 14,000 rpm for 10 min, and washed twice with 350 μL of 80% acetone (ice-cold). The washed pellets were air-dried completely and resuspended in the desired volume of lysis buffer (0.1 N NaOH+1% SDS). Samples were separated in 12% polyacrylamide gels and transferred onto nitrocellulose membranes. For probing, mouse anti-GFP antibody (Roche) and the HRP conjugated goat anti-mouse secondary antibody (Abcam) were used at 1:3000 and 1:5000 dilution, respectively, in 2.5% skim milk powder in 1xPBS. The blots were developed using Chemiluminescence Ultra substrate (BioRad) and imaged using the VersaDoc imaging system (BioRad).

### PFGE analysis for M. globosa and M. slooffiae

For CHEF analysis of M. globosa (CBS7966) and M. slooffiae (CBS7956), the cells were grown on solid mDixon medium and then collected and resuspended in 1xPBS. CHEF plugs were prepared as described in previous studies (Sun et al., 2014; Sun et al., 2017). Chromosomes were separated in 1% Megabase certified agarose gels made with 0.5 × TBE, using a BioRad CHEF-DR II System running at 3.2 V/cm with linear ramping switching time from 90 to 360 s for 120 hr in 0.5xTBE at 14°C. The gel was stained with EtBr and visualized under UV.

For the chromoblot analyses of M. globosa (CBS7966), the gel from the CHEF analysis was first transferred to a membrane, and the resulting chromoblots were then hybridized sequentially with four probes from chromosomes 3, 4, 5, and 6 of the CBS7966 genome assembly, respectively (see the Supplementary file 1 for the primer information), as described in previous studies (Findley et al., 2012; Yadav et al., 2018b).

### M. globosa genome assembly

Sequence reads were assembled with HGAP3 included in SMRTPortal v2.3 (PacBio, Menlo Park, CA, USA) and default parameters, except for the genome size set to 9 Mb. Assembly completeness was evaluated by checking for telomeric repeats. Non-telomeric contig-ends were aligned to other contigs using BLAST and unique overlaps were used to build complete chromosomes. Short telomere ends were extended using uniquely mapped reads longer than 10 kb and repolishing of the assembly using the resequencing pipeline in SMRTPortal v2.3. The assembly resulted in 19 contigs, with a total length of 9.2 Mb. 17 long and one short telomere could be identified. Six contigs had telomeres on both the 5'- and the 3'-end, and thus represent full-length chromosomes (Chr1, 2, 3, 6, 7, and 8). Six contigs had only one telomere and seven contigs had no telomeric sequence. Two contigs without telomeres were from the mitochondrion and two were from the ribosomal repeats. Chromosome 5 was constructed from two contigs ending in ribosomal rDNA repeats. The assembly contains six copies of the repeat, but read coverage suggests a length of 30–40 repeat units that cannot be resolved with the available read-length. The remaining contigs were used to build chromosomes 4 and 9, which share highly similar 5'-ends. The two ends can be distinguished by two microsatellite expansions. Chromosome 4 had a very short 3'-telomere from the default assembly, but the raw data contained a uniquely mapping read that extended several repeat units past the assembly end. After polishing the reference, all nine chromosomes had clear 5′- and 3′- telomeres.

### M. slooffiae genome assembly

Sequence reads were assembled using HGAP3 included in SMRTPortal v2.3 (PacBio, Menlo Park, CA, USA) with default parameters. This resulted in an assembly with 14 scaffolds with telomeric repeats at both ends in nine contigs. Of the remaining five contigs, three of them could be assigned to mitochondrial DNA on the basis of BLAST analysis with M. globosa. The remaining two contigs, of size 5.8 kb and 2.3 kb, did not show BLAST hits against the M. globosa or M. sympodialis genomes.

### M. furfur genome assembly

Sequence reads generated from CBS14141 were assembled using HGAP3 included in SMRTPortal v2.3 (PacBio, Menlo Park, CA, USA) with default parameters. This resulted in an assembly with eight scaffolds, of which the nuclear genome was organized in seven scaffolds that had telomere repeats at both ends.

### Gene synteny analysis

Analysis of gene synteny conservation across the centromeres was performed by BLAST as follows. The genomes for M. restricta, M. nana, and M. dermatis were downloaded from the NCBI genomes portal. The PacBio assembled genomes of M. globosa and M. slooffiae were used for synteny analysis. Synteny analysis was done in the context of ORFs flanking the centromeres of M. sympodialis. The protein sequences for each of these ORFs served as the query in BLAST analysis against the genome of other species. The local database for each genome was set up in the Geneious software for this analysis. The percentage identity values for each of the ORFs are mentioned in the boxes in Figure 7—figure supplement 3. In addition, synteny analyses between M. globosa and M. sympodialis were conducted with megablast (word size: 28) and plotted together with GC content (calculated as the deviation from the genomic mean, in non-overlapping 1-kb windows), using Circos (v0.69–6) (Krzywinski et al., 2009). Additional whole-genome alignments were conducted with Satsuma (Grabherr et al., 2010), with default parameters. The linear synteny comparisons shown in Figures 5 and 6 were generated with the Python application EasyFig (Sullivan et al., 2011).

### Species phylogeny

To reconstruct the phylogenetic relationship among the nine Malassezia species selected, orthologs were identified using the bidirectional best-hit (BDBH), COGtriangles (v2.1), and OrthoMCL (v1.4) algorithms implemented in the GET_HOMOLOGUES software package (Contreras-Moreira and Vinuesa, 2013). The proteome of M. sympodialis ATCC42132 was used as a reference. A phylogeny was inferred from a set of 738 protein sequences as follows. Individual protein sequences were aligned using MAFFT v7.310 (L-INS-i strategy), and poorly aligned regions were trimmed with TrimAl (-gappyout). The resulting alignments were concatenated to obtain a final supermatrix consisting of a total of 441,200 amino acid sites (159,270 parsimony-informative). This sequence was input to IQ-TREE v1.6.5 (Nguyen et al., 2015) and a maximum likelihood phylogeny was estimated using the LG+F+R4 amino acid model of substitution. Branch support values were obtained from 10,000 replicates of both ultrafast bootstrap approximation (UFBoot) and the nonparametric variant of the approximate likelihood ratio test (SH-aLRT) implemented in IQ-TREE. The best likelihood tree was graphically visualized with iTOL v4.3.3 (Letunic and Bork, 2019).
